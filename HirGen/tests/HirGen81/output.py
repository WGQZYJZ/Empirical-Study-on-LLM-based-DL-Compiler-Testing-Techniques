import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_116 = relay.var("var_116", dtype = "float64", shape = (2, 15, 5))#candidate|116|(2, 15, 5)|var|float64
uop_117 = relay.log(var_116.astype('float64')) # shape=(2, 15, 5)
output = uop_117
output2 = uop_117
func_124 = relay.Function([var_116,], output)
mod['func_124'] = func_124
mod = relay.transform.InferType()(mod)
mutated_mod['func_124'] = func_124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_125 = relay.var("var_125", dtype = "float64", shape = (2, 15, 5))#candidate|125|(2, 15, 5)|var|float64
func_124_call = mutated_mod.get_global_var('func_124')
call_126 = func_124_call(var_125)
output = call_126
func_127 = relay.Function([var_125], output)
mutated_mod['func_127'] = func_127
mutated_mod = relay.transform.InferType()(mutated_mod)
var_155 = relay.var("var_155", dtype = "uint8", shape = (11, 1, 8))#candidate|155|(11, 1, 8)|var|uint8
const_156 = relay.const([[[-6,2,-3,3,3,-7,10,10]],[[-1,-1,2,2,-5,-7,3,-4]],[[-4,-7,3,-1,1,1,2,-5]],[[-6,8,8,-9,2,7,9,4]],[[-8,-2,-1,1,-3,-5,-6,9]],[[-9,-9,8,-2,-3,6,10,5]],[[3,3,10,-9,-8,7,-7,5]],[[3,4,1,4,7,-4,-1,9]],[[6,-9,-7,9,-3,9,-3,7]],[[-6,1,-9,3,-6,6,-8,3]],[[-10,10,3,3,6,-7,4,-8]]], dtype = "uint8")#candidate|156|(11, 1, 8)|const|uint8
bop_157 = relay.bitwise_and(var_155.astype('uint8'), relay.reshape(const_156.astype('uint8'), relay.shape_of(var_155))) # shape=(11, 1, 8)
var_170 = relay.var("var_170", dtype = "uint8", shape = (11, 1, 8))#candidate|170|(11, 1, 8)|var|uint8
bop_171 = relay.right_shift(const_156.astype('uint8'), relay.reshape(var_170.astype('uint8'), relay.shape_of(const_156))) # shape=(11, 1, 8)
uop_195 = relay.sinh(const_156.astype('float32')) # shape=(11, 1, 8)
output = relay.Tuple([bop_157,bop_171,uop_195,])
output2 = relay.Tuple([bop_157,bop_171,uop_195,])
func_201 = relay.Function([var_155,var_170,], output)
mod['func_201'] = func_201
mod = relay.transform.InferType()(mod)
var_202 = relay.var("var_202", dtype = "uint8", shape = (11, 1, 8))#candidate|202|(11, 1, 8)|var|uint8
var_203 = relay.var("var_203", dtype = "uint8", shape = (11, 1, 8))#candidate|203|(11, 1, 8)|var|uint8
output = func_201(var_202,var_203,)
func_204 = relay.Function([var_202,var_203,], output)
mutated_mod['func_204'] = func_204
mutated_mod = relay.transform.InferType()(mutated_mod)
var_312 = relay.var("var_312", dtype = "int32", shape = ())#candidate|312|()|var|int32
var_313 = relay.var("var_313", dtype = "int32", shape = (1, 1, 4))#candidate|313|(1, 1, 4)|var|int32
bop_314 = relay.bitwise_xor(var_312.astype('int32'), var_313.astype('int32')) # shape=(1, 1, 4)
output = bop_314
output2 = bop_314
func_322 = relay.Function([var_312,var_313,], output)
mod['func_322'] = func_322
mod = relay.transform.InferType()(mod)
mutated_mod['func_322'] = func_322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_322_call = mutated_mod.get_global_var('func_322')
var_324 = relay.var("var_324", dtype = "int32", shape = ())#candidate|324|()|var|int32
var_325 = relay.var("var_325", dtype = "int32", shape = (1, 1, 4))#candidate|325|(1, 1, 4)|var|int32
call_323 = func_322_call(var_324,var_325,)
output = call_323
func_326 = relay.Function([var_324,var_325,], output)
mutated_mod['func_326'] = func_326
mutated_mod = relay.transform.InferType()(mutated_mod)
const_396 = relay.const([[[8.981259,1.059087,8.331365,-7.370719,-8.848725,-3.040830,-3.960845,-8.369199],[-4.455405,6.611205,6.801740,0.949360,5.960126,-2.203319,-9.261260,5.924001],[4.062621,-5.863686,5.972995,-4.042772,-7.296739,9.945999,-0.461431,-5.540652],[-1.851034,-0.335994,-7.881250,-8.494575,-5.124340,2.195631,6.158042,-3.180349],[3.429372,2.210953,-1.189767,-7.894958,-2.437531,5.241693,4.867084,6.921251],[6.905384,5.894168,-1.509414,5.128241,7.344241,9.922288,9.860318,6.748468]],[[-8.785873,-9.255361,-6.431686,0.864496,-4.883473,3.236581,1.906193,7.972471],[3.027501,-3.013567,0.196503,-5.767574,-1.179436,9.465443,7.741850,-6.232859],[9.603057,-1.357274,2.332466,-3.190340,-8.459553,-1.846466,0.237002,-8.289242],[-1.424397,-3.120727,2.080870,-7.936282,-3.809755,6.295554,-8.321387,6.212447],[-9.503424,1.476558,-5.420200,6.132567,-0.218037,-0.747238,-7.031635,-1.502591],[0.102978,-9.978079,7.966650,-7.031816,-9.628905,5.240959,7.646848,-0.591753]],[[0.887837,2.746757,4.594406,-9.147066,-6.309956,8.543196,-1.869610,-6.999580],[-3.887796,-1.772407,3.770882,2.565946,-7.721083,9.374608,-6.631847,-0.159833],[1.820664,9.196954,-2.019914,-4.707007,-8.293161,2.523093,9.346884,-8.465213],[-0.105378,4.247722,6.385724,1.409642,-8.047310,9.143644,-2.815984,-2.982074],[8.433814,6.936635,2.562648,4.844152,6.139410,-2.065373,-4.792553,1.185350],[4.663880,-4.272100,6.418111,3.604304,-3.480597,-1.432776,-3.005394,8.163044]],[[-9.211155,0.715707,-7.752664,3.942578,-3.439597,6.159815,-6.212579,4.121941],[3.096354,-7.378737,-2.318584,-7.195229,-0.487070,7.879227,2.825284,3.921161],[8.718028,-1.754883,6.112127,-2.057816,2.733011,-2.009034,-8.011916,-2.453759],[4.212105,-8.488897,-1.664907,4.979472,-4.647649,1.672346,3.694740,9.645411],[0.459002,-8.603970,-9.384435,-8.458353,-9.665640,7.808276,6.864698,1.541338],[0.344352,-5.120985,-3.774710,-6.870624,-8.180207,1.102389,-2.377518,1.632253]],[[-3.105041,-4.965951,-5.344747,-0.388016,6.577893,5.837929,5.431063,-1.262814],[-4.212149,-4.376674,-6.146950,4.172096,-2.700175,-6.017097,-1.547462,8.348347],[7.311622,0.797808,-1.425258,7.045434,2.574551,-3.474355,3.817199,9.333603],[6.730179,-7.293446,3.837535,4.489891,-2.581720,-4.994824,7.657126,3.806993],[-5.659802,-4.535728,6.044904,-0.327486,-9.166505,3.021502,5.379031,4.190489],[9.089303,-0.511792,-4.034296,-9.857694,2.012341,8.471573,-7.417302,-4.369059]],[[6.820018,-2.682656,-9.891500,1.126580,4.999219,-7.574519,-6.349632,-8.504410],[6.598035,-7.645481,-3.641658,9.948857,5.739855,-3.362274,2.938598,-7.308333],[6.768212,0.388686,-6.831845,-6.821535,-8.597259,-3.414267,-9.842060,-7.232263],[-4.489506,0.151970,1.956237,-2.770944,5.503272,7.552393,6.922532,7.524496],[-3.534586,-3.571963,-1.303981,-8.734937,8.716897,9.048862,1.785607,-7.179126],[-4.843987,-1.352096,-4.855621,-1.287726,0.161531,-7.678309,-1.360062,2.871271]],[[7.351656,2.853534,-8.502957,-2.361639,-7.134958,-4.264460,7.332232,5.386301],[-6.201867,7.236705,0.205558,9.691451,8.709384,3.231774,7.007755,-1.366453],[3.637780,-8.729999,-0.054315,5.332878,-6.052464,-8.758975,-4.844039,0.029834],[-7.918859,7.968617,9.070549,-8.806913,8.892751,-5.679255,0.845680,6.946755],[-9.812413,-3.678794,-3.968070,6.282687,0.037515,-0.030323,-5.666076,9.859938],[-2.558886,-7.240830,5.728275,1.141000,-3.189594,0.949200,-0.829520,-0.632456]],[[2.912467,8.792606,3.730076,-6.808502,0.751124,-5.683988,5.990484,-7.031109],[1.283886,5.551668,8.342440,5.046103,-6.693452,5.460615,7.943406,9.556422],[0.594328,-0.781397,9.370557,1.863647,6.902477,-4.599806,2.883668,-6.900241],[7.039621,4.082451,-7.270194,8.776325,-7.870749,-5.352318,-2.755443,-0.331312],[-5.729573,-9.522664,1.702060,-4.869008,-1.210340,6.967923,6.926053,-5.138002],[5.905603,-1.617603,-1.140540,-3.793491,-2.510856,-4.150653,-2.216922,-4.747734]],[[7.221639,1.515985,9.841080,8.197829,-2.894328,3.094771,-6.206137,2.286337],[-8.928114,-0.829273,7.546634,1.219853,6.782092,-6.819163,-2.846936,-9.101702],[-5.233667,-5.316049,-1.460036,1.121168,0.917696,-0.771068,-9.106523,8.807403],[4.115738,6.702271,2.406941,8.192639,-0.159791,-1.765288,-7.751506,-6.424681],[-7.845808,-1.613876,-2.234796,-8.962612,2.210267,0.628368,-0.526796,-1.939790],[-1.691961,-0.253549,-5.803183,-9.161154,0.698898,0.375952,-2.769914,-9.478936]]], dtype = "float64")#candidate|396|(9, 6, 8)|const|float64
uop_397 = relay.erf(const_396.astype('float64')) # shape=(9, 6, 8)
const_402 = relay.const([[[-5.337927,3.293442,-5.518910,4.022844,-9.579876,9.287969,-7.970731,-0.643184],[8.247485,-7.232537,8.160656,5.612810,6.211597,6.464631,-6.515144,6.396936],[-0.380418,7.242458,6.121622,-5.256573,9.941950,4.981268,-7.312511,6.460327],[-8.813085,-5.803306,7.360587,8.382251,9.787456,3.348325,1.490212,-3.158500],[8.847992,-7.570349,-1.822430,-0.029373,-1.829890,7.257128,5.379074,2.866271],[-9.912193,3.184051,1.280125,-4.799192,4.056293,-0.877672,-2.631966,4.328681]],[[-5.977420,-8.260756,-2.169386,5.320484,-6.977912,-4.157732,1.001201,-4.652001],[2.578555,7.249834,-8.458960,2.477337,6.067367,9.470727,-2.907181,2.425797],[-9.542282,4.129346,8.127635,-4.620158,9.280544,5.297919,-6.559361,-8.417632],[-4.493390,-7.561678,0.467883,-7.838688,3.789675,6.000088,-5.469314,9.141238],[-5.928988,-7.547214,6.795072,-0.690915,8.495132,7.357891,9.300135,2.195849],[2.187309,-1.897726,1.902529,-2.882775,-6.165899,-4.954379,-5.948198,-5.535571]],[[-1.911950,-3.475186,8.464072,-8.893504,5.026069,-4.447541,6.294565,-1.463473],[6.431372,9.493508,8.442878,9.903582,1.076274,3.243971,8.737900,5.997691],[-7.534764,0.170426,-6.697182,-0.327780,2.432762,-2.839219,-3.029668,-4.396380],[3.504835,-1.834646,5.423289,8.058726,4.167784,-7.804242,-0.738143,-8.922880],[-2.521057,-5.175305,8.656896,-5.118379,2.306646,9.258404,0.114200,2.987042],[7.442881,7.054410,1.805313,-9.971629,7.553951,-7.394147,-6.189525,-9.613060]],[[-8.490825,7.575291,8.969102,0.470200,-4.325021,-0.526201,-0.435003,-1.337896],[3.028487,-9.990920,-3.946239,7.621104,5.222430,2.129877,-5.522057,-8.917759],[-9.855995,-4.253472,9.477272,-0.254612,-6.940080,4.923732,-1.897869,7.847477],[-9.095547,1.053708,-7.872850,-5.911850,-5.754084,8.863234,-5.083225,3.590137],[6.167404,-5.005697,5.447428,-7.102044,-5.240066,-6.887032,4.487792,-0.934455],[9.669520,3.212130,9.933922,-8.420049,3.676580,-7.732587,8.930431,2.033548]],[[-1.825434,-1.258103,-1.602353,5.954542,-4.194051,-4.217061,4.890100,4.630052],[-5.488801,-7.897486,1.162154,3.896799,-3.427983,-0.785595,9.188719,-6.589069],[3.328554,-8.740782,1.100232,-2.007217,8.111507,-9.143794,-4.097523,-3.056031],[-6.799512,-0.070815,8.944569,-1.787790,0.820733,1.895368,-1.079527,-1.030331],[-6.683252,-5.625764,0.019854,-7.863725,3.950982,8.917374,-3.935345,-6.624301],[9.183702,-7.308204,-3.231292,-9.797624,9.053753,-0.929963,-9.243396,-2.834384]],[[0.261413,-0.389893,5.015335,-9.420054,4.903426,-4.616238,2.491978,-7.495614],[5.324209,3.124349,-3.763206,-5.999293,1.662086,9.201854,1.982470,7.758313],[-4.135025,2.615354,-7.312191,-9.381068,-3.325801,6.519805,8.424350,-7.207028],[6.140166,-3.221567,0.457616,7.254337,-0.949741,-2.059309,-9.031042,-6.274227],[-7.377196,2.788650,9.758943,-2.422702,-2.017460,1.128606,-3.352199,9.266712],[8.055765,0.131238,-0.208023,-6.179117,4.509043,-2.866685,-5.672869,9.777143]],[[9.866781,2.022550,-3.877518,-8.219196,6.772090,7.024877,9.121020,4.503806],[-8.909117,7.286686,-8.483348,6.540996,6.804759,0.462707,3.757642,-4.121579],[4.135745,5.505417,9.147524,8.535571,-5.930740,-6.934786,2.583077,-4.722468],[-1.426544,-9.727806,7.592352,3.125119,7.830070,-3.573442,2.996630,0.673539],[-4.642001,-1.358109,-7.042764,4.845418,-2.787278,-9.496904,5.520964,-7.888313],[0.036589,-4.742261,-3.264538,7.523085,7.608762,-8.955971,-9.265622,1.302902]],[[9.696506,-5.691498,9.723411,-7.150512,-4.908459,2.534938,1.031494,8.929720],[-4.138841,-9.165267,1.186970,7.982766,2.192114,9.687173,3.239324,0.347639],[3.054751,6.145535,1.582794,-6.548938,-2.222222,0.809599,8.011041,-4.186707],[1.837075,0.685888,-1.171691,9.063060,-5.811845,8.396067,5.357402,-9.976254],[7.158093,-2.777727,4.817530,-1.164820,-7.321881,-7.911414,-1.430191,-0.642899],[4.748168,9.886590,-3.777861,0.457818,2.437743,-1.105958,5.413438,3.021290]],[[-1.460411,3.447693,1.477345,-9.782202,-3.518240,4.388664,9.595780,-1.998609],[6.005536,3.166161,-8.192336,6.449003,4.244459,-5.622116,-0.878358,0.478969],[8.461889,7.576775,-8.180088,0.491942,-7.163336,-0.108176,-5.009467,-2.963399],[-7.825357,4.675516,-3.552705,-7.323670,-4.292500,4.500934,3.367750,-0.942516],[1.547449,8.715920,7.342811,-3.647145,7.731754,6.412766,0.830753,-2.536258],[3.141147,-0.674957,-0.186967,-7.265121,-1.343988,2.273609,-8.461645,-8.926151]]], dtype = "float64")#candidate|402|(9, 6, 8)|const|float64
bop_403 = relay.left_shift(uop_397.astype('int16'), relay.reshape(const_402.astype('int16'), relay.shape_of(uop_397))) # shape=(9, 6, 8)
func_124_call = mod.get_global_var('func_124')
func_127_call = mutated_mod.get_global_var('func_127')
var_422 = relay.var("var_422", dtype = "float64", shape = (5, 30))#candidate|422|(5, 30)|var|float64
call_421 = func_124_call(relay.reshape(var_422.astype('float64'), [2, 15, 5]))
call_423 = func_124_call(relay.reshape(var_422.astype('float64'), [2, 15, 5]))
output = relay.Tuple([bop_403,call_421,var_422,])
output2 = relay.Tuple([bop_403,call_423,var_422,])
func_435 = relay.Function([var_422,], output)
mod['func_435'] = func_435
mod = relay.transform.InferType()(mod)
var_436 = relay.var("var_436", dtype = "float64", shape = (5, 30))#candidate|436|(5, 30)|var|float64
output = func_435(var_436)
func_437 = relay.Function([var_436], output)
mutated_mod['func_437'] = func_437
mutated_mod = relay.transform.InferType()(mutated_mod)
var_612 = relay.var("var_612", dtype = "int16", shape = (2, 9, 6))#candidate|612|(2, 9, 6)|var|int16
var_613 = relay.var("var_613", dtype = "int16", shape = (2, 9, 6))#candidate|613|(2, 9, 6)|var|int16
bop_614 = relay.minimum(var_612.astype('int16'), relay.reshape(var_613.astype('int16'), relay.shape_of(var_612))) # shape=(2, 9, 6)
func_201_call = mod.get_global_var('func_201')
func_204_call = mutated_mod.get_global_var('func_204')
const_633 = relay.const([10,-5,-3,8,-5,10,3,-10,7,5,-4,-4,6,8,-8,2,-6,2,-5,-1,1,2,3,2,-9,-5,4,10,5,-2,2,1,-3,9,-3,10,2,-9,5,-5,6,9,-1,-2,8,9,9,10,-5,2,9,-4,-6,-6,-4,-7,-4,2,7,2,-5,-7,-3,8,6,-5,-4,8,4,2,6,10,-6,-5,-4,8,8,-8,2,8,-6,5,-4,3,-8,7,4,3], dtype = "uint8")#candidate|633|(88,)|const|uint8
call_632 = relay.TupleGetItem(func_201_call(relay.reshape(const_633.astype('uint8'), [11, 1, 8]), relay.reshape(const_633.astype('uint8'), [11, 1, 8]), ), 0)
call_634 = relay.TupleGetItem(func_204_call(relay.reshape(const_633.astype('uint8'), [11, 1, 8]), relay.reshape(const_633.astype('uint8'), [11, 1, 8]), ), 0)
output = relay.Tuple([bop_614,call_632,const_633,])
output2 = relay.Tuple([bop_614,call_634,const_633,])
func_635 = relay.Function([var_612,var_613,], output)
mod['func_635'] = func_635
mod = relay.transform.InferType()(mod)
mutated_mod['func_635'] = func_635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_635_call = mutated_mod.get_global_var('func_635')
var_637 = relay.var("var_637", dtype = "int16", shape = (2, 9, 6))#candidate|637|(2, 9, 6)|var|int16
var_638 = relay.var("var_638", dtype = "int16", shape = (2, 9, 6))#candidate|638|(2, 9, 6)|var|int16
call_636 = func_635_call(var_637,var_638,)
output = call_636
func_639 = relay.Function([var_637,var_638,], output)
mutated_mod['func_639'] = func_639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_680 = relay.var("var_680", dtype = "float32", shape = (1, 1, 14))#candidate|680|(1, 1, 14)|var|float32
uop_681 = relay.cosh(var_680.astype('float32')) # shape=(1, 1, 14)
func_435_call = mod.get_global_var('func_435')
func_437_call = mutated_mod.get_global_var('func_437')
const_687 = relay.const([4.259495,-0.734453,8.410047,3.520245,2.560831,3.447149,-1.590633,-1.282070,1.904547,6.057647,7.902348,5.616519,8.553047,4.286321,5.370790,1.787822,5.051835,7.121647,-0.740823,9.636143,5.857197,2.416212,-8.509838,-9.055184,0.669412,9.761238,2.667193,7.058822,6.041091,0.835005,2.147538,3.107602,-0.357700,-3.166018,8.393130,-9.903710,-0.399094,-3.884280,-2.797130,9.388041,-7.248618,-1.979782,4.885173,-4.111294,7.281353,-2.533631,-6.296898,3.337946,-7.535372,-2.003939,8.779386,9.397682,-4.653147,-2.496604,-2.355857,-4.839922,-1.529893,-3.001545,-4.289809,-3.831796,-7.076932,5.813814,-3.457247,9.694606,-1.525534,-4.562880,-9.130423,6.978747,-5.649124,9.977362,8.164962,0.281498,7.160577,-9.327970,6.684532,8.310531,6.116453,-9.095785,7.126243,-2.711689,3.685161,7.319978,-9.438675,-0.815181,-4.760803,8.532740,2.732282,-7.305336,-4.566748,0.666729,4.163580,3.599501,4.541678,7.800871,5.413067,-5.324715,-8.936384,1.950746,-4.128579,3.477512,9.210144,2.411220,-8.989387,9.823499,-5.103233,-7.152651,3.330533,-8.817067,4.284344,5.873038,8.064309,-9.443159,0.496187,0.607831,1.713194,3.322881,2.916757,-3.918022,-7.983785,4.230556,-4.533448,-9.557631,4.889883,-0.333881,-3.450830,-5.608967,6.582821,-0.004013,-1.824649,-2.547604,-4.253914,-7.787497,-8.614501,9.807784,1.497841,6.707654,-8.092285,3.649095,-1.683466,9.824779,-2.410122,9.900316,-8.638940,-0.024204,3.635366,-8.150488,-3.284482,8.747616,8.130074,3.844070], dtype = "float64")#candidate|687|(150,)|const|float64
call_686 = relay.TupleGetItem(func_435_call(relay.reshape(const_687.astype('float64'), [5, 30])), 1)
call_688 = relay.TupleGetItem(func_437_call(relay.reshape(const_687.astype('float64'), [5, 30])), 1)
uop_689 = relay.sigmoid(uop_681.astype('float32')) # shape=(1, 1, 14)
output = relay.Tuple([call_686,const_687,uop_689,])
output2 = relay.Tuple([call_688,const_687,uop_689,])
func_691 = relay.Function([var_680,], output)
mod['func_691'] = func_691
mod = relay.transform.InferType()(mod)
mutated_mod['func_691'] = func_691
mutated_mod = relay.transform.InferType()(mutated_mod)
var_692 = relay.var("var_692", dtype = "float32", shape = (1, 1, 14))#candidate|692|(1, 1, 14)|var|float32
func_691_call = mutated_mod.get_global_var('func_691')
call_693 = func_691_call(var_692)
output = call_693
func_694 = relay.Function([var_692], output)
mutated_mod['func_694'] = func_694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_798 = relay.var("var_798", dtype = "uint8", shape = (4, 12, 6))#candidate|798|(4, 12, 6)|var|uint8
var_799 = relay.var("var_799", dtype = "uint8", shape = (4, 12, 6))#candidate|799|(4, 12, 6)|var|uint8
bop_800 = relay.equal(var_798.astype('bool'), relay.reshape(var_799.astype('bool'), relay.shape_of(var_798))) # shape=(4, 12, 6)
bop_803 = relay.subtract(var_798.astype('uint16'), relay.reshape(bop_800.astype('uint16'), relay.shape_of(var_798))) # shape=(4, 12, 6)
uop_808 = relay.sin(var_799.astype('float64')) # shape=(4, 12, 6)
output = relay.Tuple([bop_803,uop_808,])
output2 = relay.Tuple([bop_803,uop_808,])
func_813 = relay.Function([var_798,var_799,], output)
mod['func_813'] = func_813
mod = relay.transform.InferType()(mod)
var_814 = relay.var("var_814", dtype = "uint8", shape = (4, 12, 6))#candidate|814|(4, 12, 6)|var|uint8
var_815 = relay.var("var_815", dtype = "uint8", shape = (4, 12, 6))#candidate|815|(4, 12, 6)|var|uint8
output = func_813(var_814,var_815,)
func_816 = relay.Function([var_814,var_815,], output)
mutated_mod['func_816'] = func_816
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1182 = relay.var("var_1182", dtype = "uint8", shape = (10, 14, 2))#candidate|1182|(10, 14, 2)|var|uint8
var_1183 = relay.var("var_1183", dtype = "uint8", shape = (10, 14, 2))#candidate|1183|(10, 14, 2)|var|uint8
bop_1184 = relay.add(var_1182.astype('uint8'), relay.reshape(var_1183.astype('uint8'), relay.shape_of(var_1182))) # shape=(10, 14, 2)
bop_1187 = relay.bitwise_or(var_1183.astype('uint8'), relay.reshape(var_1182.astype('uint8'), relay.shape_of(var_1183))) # shape=(10, 14, 2)
output = relay.Tuple([bop_1184,bop_1187,])
output2 = relay.Tuple([bop_1184,bop_1187,])
func_1191 = relay.Function([var_1182,var_1183,], output)
mod['func_1191'] = func_1191
mod = relay.transform.InferType()(mod)
mutated_mod['func_1191'] = func_1191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1191_call = mutated_mod.get_global_var('func_1191')
var_1193 = relay.var("var_1193", dtype = "uint8", shape = (10, 14, 2))#candidate|1193|(10, 14, 2)|var|uint8
var_1194 = relay.var("var_1194", dtype = "uint8", shape = (10, 14, 2))#candidate|1194|(10, 14, 2)|var|uint8
call_1192 = func_1191_call(var_1193,var_1194,)
output = call_1192
func_1195 = relay.Function([var_1193,var_1194,], output)
mutated_mod['func_1195'] = func_1195
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1220 = relay.const(2, dtype = "int16")#candidate|1220|()|const|int16
const_1221 = relay.const([[[-10,5,-10,-3,6,-7,10,7,-4,-8,-3,2],[-5,9,-4,10,-7,-4,-1,-7,2,-6,-2,10],[1,4,2,-8,-8,-2,3,6,1,7,5,-1],[-8,3,-1,7,2,9,-9,10,-3,2,8,-6],[-6,-1,4,1,-10,-5,-5,4,-6,-1,10,-4]],[[6,1,-4,1,7,-2,-5,-7,5,-5,-2,10],[-3,-5,-4,8,-5,-4,-5,8,8,-4,-2,7],[1,-2,2,-3,4,-8,6,-8,6,-9,-6,2],[8,-8,-5,2,6,10,-5,-3,-10,-5,8,9],[-5,4,7,7,9,8,10,-1,3,6,-6,-6]],[[1,-7,5,2,2,3,-9,-5,-6,4,4,-4],[-1,-6,7,-5,3,9,6,10,-7,-9,5,-9],[-10,9,-10,-2,3,-8,-10,-1,5,-1,-1,-2],[5,-7,5,3,8,-1,5,9,-1,-8,-10,-2],[-9,9,-5,8,-10,2,10,-3,7,5,7,-2]],[[1,-7,-1,7,5,9,6,-2,2,-4,-9,-1],[10,2,1,6,-6,-4,-4,-8,-8,-9,-4,-1],[-4,1,3,-2,9,2,8,2,3,-2,7,-7],[6,-9,8,-1,4,-8,3,2,5,-1,-4,-8],[9,5,7,10,8,6,-9,8,8,-2,7,-4]],[[-10,5,10,-8,-3,-6,4,6,7,-10,10,2],[6,-10,8,3,-10,9,-2,-10,1,-5,-4,-9],[-4,7,-6,1,-3,-5,6,-8,-8,8,-5,7],[6,2,-5,-1,7,3,5,5,5,-8,8,9],[4,-8,-8,4,6,-4,-7,10,-2,-7,-6,-6]]], dtype = "int16")#candidate|1221|(5, 5, 12)|const|int16
bop_1222 = relay.bitwise_and(const_1220.astype('int16'), const_1221.astype('int16')) # shape=(5, 5, 12)
func_635_call = mod.get_global_var('func_635')
func_639_call = mutated_mod.get_global_var('func_639')
const_1232 = relay.const([2,-4,-7,1,5,9,3,-4,5,-10,-1,-4,-5,8,6,2,7,6,-1,9,8,10,9,-6,-3,3,9,1,-2,1,-10,-5,-1,1,7,-7,-10,-6,-1,5,-1,8,-8,3,7,7,8,-4,-2,-2,5,-3,8,-3,-2,-5,-9,-2,-1,6,-10,7,4,1,-4,-4,-4,-3,-6,3,7,10,10,-4,8,9,2,8,-7,3,-1,2,3,2,-4,-7,3,-8,1,2,-1,-7,-8,10,-3,-9,-9,4,8,3,-10,-4,10,-4,5,10,8,8], dtype = "int16")#candidate|1232|(108,)|const|int16
call_1231 = relay.TupleGetItem(func_635_call(relay.reshape(const_1232.astype('int16'), [2, 9, 6]), relay.reshape(const_1232.astype('int16'), [2, 9, 6]), ), 1)
call_1233 = relay.TupleGetItem(func_639_call(relay.reshape(const_1232.astype('int16'), [2, 9, 6]), relay.reshape(const_1232.astype('int16'), [2, 9, 6]), ), 1)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
var_1237 = relay.var("var_1237", dtype = "uint8", shape = (288,))#candidate|1237|(288,)|var|uint8
call_1236 = relay.TupleGetItem(func_813_call(relay.reshape(var_1237.astype('uint8'), [4, 12, 6]), relay.reshape(var_1237.astype('uint8'), [4, 12, 6]), ), 0)
call_1238 = relay.TupleGetItem(func_816_call(relay.reshape(var_1237.astype('uint8'), [4, 12, 6]), relay.reshape(var_1237.astype('uint8'), [4, 12, 6]), ), 0)
output = relay.Tuple([bop_1222,call_1231,const_1232,call_1236,var_1237,])
output2 = relay.Tuple([bop_1222,call_1233,const_1232,call_1238,var_1237,])
func_1247 = relay.Function([var_1237,], output)
mod['func_1247'] = func_1247
mod = relay.transform.InferType()(mod)
mutated_mod['func_1247'] = func_1247
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1248 = relay.var("var_1248", dtype = "uint8", shape = (288,))#candidate|1248|(288,)|var|uint8
func_1247_call = mutated_mod.get_global_var('func_1247')
call_1249 = func_1247_call(var_1248)
output = call_1249
func_1250 = relay.Function([var_1248], output)
mutated_mod['func_1250'] = func_1250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1523 = relay.var("var_1523", dtype = "uint32", shape = (10, 1, 4))#candidate|1523|(10, 1, 4)|var|uint32
const_1524 = relay.const([[[2,-5,-8,-7],[6,-8,-8,10],[-4,-6,4,7],[-2,-4,9,4],[1,-2,-4,9],[2,7,-6,5]],[[-3,6,-5,-3],[-6,-9,6,-6],[5,-6,-8,8],[-2,2,-9,-9],[10,-2,-8,1],[-4,9,-4,-7]],[[-5,-7,-7,3],[-2,-9,-3,-7],[-6,7,-6,8],[-7,-9,3,1],[8,3,4,5],[10,-9,4,4]],[[-7,-4,9,4],[-8,-8,-1,-1],[6,-6,-9,-8],[-5,-9,-7,9],[-6,-8,4,1],[-6,-4,-8,10]],[[10,-6,-7,7],[-5,2,-1,-5],[-5,-4,-4,-2],[-3,-1,-5,7],[-7,4,1,-9],[-8,-8,4,-10]],[[6,-10,8,-5],[2,4,-9,3],[-7,-1,8,5],[-10,7,-4,-5],[-10,3,10,-8],[3,2,-6,7]],[[3,2,-9,9],[9,5,4,4],[-8,-1,2,-3],[-3,7,1,3],[-4,-5,-1,2],[2,-3,-9,10]],[[3,-6,-1,2],[-3,1,4,7],[-8,-9,-9,-7],[10,9,7,5],[-1,9,-9,5],[-9,-5,2,-1]],[[6,-9,2,-10],[-8,-10,-10,-8],[-7,2,7,9],[6,9,7,10],[9,-2,7,-3],[-1,-3,9,2]],[[6,3,1,-9],[5,-7,-9,8],[6,9,2,-10],[7,3,-3,-2],[-9,2,7,9],[1,-6,2,-8]]], dtype = "uint32")#candidate|1524|(10, 6, 4)|const|uint32
bop_1525 = relay.logical_xor(var_1523.astype('uint32'), const_1524.astype('uint32')) # shape=(10, 6, 4)
func_635_call = mod.get_global_var('func_635')
func_639_call = mutated_mod.get_global_var('func_639')
var_1530 = relay.var("var_1530", dtype = "int16", shape = (108,))#candidate|1530|(108,)|var|int16
call_1529 = relay.TupleGetItem(func_635_call(relay.reshape(var_1530.astype('int16'), [2, 9, 6]), relay.reshape(var_1530.astype('int16'), [2, 9, 6]), ), 0)
call_1531 = relay.TupleGetItem(func_639_call(relay.reshape(var_1530.astype('int16'), [2, 9, 6]), relay.reshape(var_1530.astype('int16'), [2, 9, 6]), ), 0)
bop_1536 = relay.logical_and(bop_1525.astype('bool'), relay.reshape(const_1524.astype('bool'), relay.shape_of(bop_1525))) # shape=(10, 6, 4)
bop_1548 = relay.multiply(var_1523.astype('int16'), bop_1536.astype('int16')) # shape=(10, 6, 4)
var_1552 = relay.var("var_1552", dtype = "uint32", shape = (10, 15, 4))#candidate|1552|(10, 15, 4)|var|uint32
bop_1553 = relay.bitwise_xor(var_1523.astype('int64'), var_1552.astype('int64')) # shape=(10, 15, 4)
output = relay.Tuple([call_1529,var_1530,bop_1548,bop_1553,])
output2 = relay.Tuple([call_1531,var_1530,bop_1548,bop_1553,])
func_1569 = relay.Function([var_1523,var_1530,var_1552,], output)
mod['func_1569'] = func_1569
mod = relay.transform.InferType()(mod)
mutated_mod['func_1569'] = func_1569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1569_call = mutated_mod.get_global_var('func_1569')
var_1571 = relay.var("var_1571", dtype = "uint32", shape = (10, 1, 4))#candidate|1571|(10, 1, 4)|var|uint32
var_1572 = relay.var("var_1572", dtype = "int16", shape = (108,))#candidate|1572|(108,)|var|int16
var_1573 = relay.var("var_1573", dtype = "uint32", shape = (10, 15, 4))#candidate|1573|(10, 15, 4)|var|uint32
call_1570 = func_1569_call(var_1571,var_1572,var_1573,)
output = call_1570
func_1574 = relay.Function([var_1571,var_1572,var_1573,], output)
mutated_mod['func_1574'] = func_1574
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1581 = relay.const([[[-1.514224,5.880468,-9.592294,2.172078,7.236765,-7.179946,7.360168],[8.298986,3.396407,8.459631,-5.796440,4.133247,-4.879375,8.456815],[7.067451,2.612060,8.812830,-1.710756,-3.361302,-4.193450,1.675103],[5.074299,2.617116,6.191819,5.240908,9.368971,-8.556736,5.414259],[-3.217666,-9.421362,9.012394,-9.537803,8.962976,-7.563386,-0.960077],[1.618694,5.714672,8.888174,2.665418,9.660769,1.253859,-1.215671],[-7.576812,-7.852075,-5.908905,-4.505024,-0.783171,8.252325,1.622804],[-1.431320,-5.694756,-2.291624,-4.310186,5.559624,-5.706432,1.632463],[7.665713,8.240664,2.278347,2.873386,1.711615,-3.411107,-6.619887],[6.740330,7.285807,5.783049,3.999833,-1.427573,8.650280,5.748110],[-8.772523,7.412064,5.626995,3.236893,-4.040351,-4.179480,4.397805],[-0.600045,-7.100932,3.246758,4.418264,-3.584179,-6.945923,-2.458534],[-5.775072,2.034884,-5.164390,-0.572766,-8.197225,4.254995,-2.688094],[-3.003997,-9.639797,4.307710,-4.546707,-1.769275,-3.471659,-7.912638],[7.500827,-0.679834,-9.298559,2.811096,5.475145,-4.094020,8.888906],[-0.902720,-8.505136,8.938905,5.399627,1.069171,-9.016385,7.830278]]], dtype = "float64")#candidate|1581|(1, 16, 7)|const|float64
uop_1582 = relay.log2(const_1581.astype('float64')) # shape=(1, 16, 7)
output = uop_1582
output2 = uop_1582
func_1593 = relay.Function([], output)
mod['func_1593'] = func_1593
mod = relay.transform.InferType()(mod)
mutated_mod['func_1593'] = func_1593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1593_call = mutated_mod.get_global_var('func_1593')
call_1594 = func_1593_call()
output = call_1594
func_1595 = relay.Function([], output)
mutated_mod['func_1595'] = func_1595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1593_call = mod.get_global_var('func_1593')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_1603 = func_1593_call()
call_1604 = func_1593_call()
output = relay.Tuple([call_1603,])
output2 = relay.Tuple([call_1604,])
func_1605 = relay.Function([], output)
mod['func_1605'] = func_1605
mod = relay.transform.InferType()(mod)
output = func_1605()
func_1606 = relay.Function([], output)
mutated_mod['func_1606'] = func_1606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1593_call = mod.get_global_var('func_1593')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_1625 = func_1593_call()
call_1626 = func_1593_call()
uop_1627 = relay.rsqrt(call_1625.astype('float32')) # shape=(1, 16, 7)
uop_1629 = relay.rsqrt(call_1626.astype('float32')) # shape=(1, 16, 7)
func_1605_call = mod.get_global_var('func_1605')
func_1606_call = mutated_mod.get_global_var('func_1606')
call_1632 = relay.TupleGetItem(func_1605_call(), 0)
call_1633 = relay.TupleGetItem(func_1606_call(), 0)
output = relay.Tuple([uop_1627,call_1632,])
output2 = relay.Tuple([uop_1629,call_1633,])
func_1634 = relay.Function([], output)
mod['func_1634'] = func_1634
mod = relay.transform.InferType()(mod)
mutated_mod['func_1634'] = func_1634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mutated_mod.get_global_var('func_1634')
call_1635 = func_1634_call()
output = call_1635
func_1636 = relay.Function([], output)
mutated_mod['func_1636'] = func_1636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1605_call = mod.get_global_var('func_1605')
func_1606_call = mutated_mod.get_global_var('func_1606')
call_1688 = relay.TupleGetItem(func_1605_call(), 0)
call_1689 = relay.TupleGetItem(func_1606_call(), 0)
output = call_1688
output2 = call_1689
func_1692 = relay.Function([], output)
mod['func_1692'] = func_1692
mod = relay.transform.InferType()(mod)
mutated_mod['func_1692'] = func_1692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mutated_mod.get_global_var('func_1692')
call_1693 = func_1692_call()
output = call_1693
func_1694 = relay.Function([], output)
mutated_mod['func_1694'] = func_1694
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1741 = relay.const([[[-2.055463,-8.501674,-5.274789,-7.521676,-3.531086,-8.965470,-5.396559,-3.644758,9.979697,3.894969,-0.152149,4.845510,0.976906,7.033974,7.937207,-3.049251],[5.432641,-4.595206,-9.508322,-2.294807,-8.984411,-3.764840,-5.708312,6.041665,9.724568,-3.581352,-0.656724,6.624252,-6.099528,8.209276,-9.683527,-4.748431],[-1.548332,8.044716,1.480530,2.226947,-7.910698,9.661343,-9.094037,-7.804616,4.339228,6.191964,-1.817340,1.776930,-9.214900,-3.382177,-6.912841,-8.623735],[1.060820,1.766880,8.020994,-0.828610,-2.744686,-3.176967,-7.429810,-6.637465,-8.525574,8.367965,7.100671,0.972252,-9.127402,-2.857638,-9.969456,4.123642],[-9.289891,5.258083,-0.945220,2.826545,4.448633,4.881947,-7.811864,1.695165,-7.916674,6.752076,7.840072,1.157920,-9.416234,-5.105302,-1.133051,-8.975350],[9.254482,1.514745,3.113413,-9.601486,-8.547795,8.532597,-2.496535,8.522315,6.654197,-3.799821,-9.713441,-6.784168,4.761114,8.570991,9.463488,-1.018547],[3.671732,-1.384131,-5.507869,8.994430,-0.340732,9.545026,8.293865,2.309365,7.514414,3.785033,4.337537,-9.106481,3.440175,4.586538,3.811472,6.704014],[2.902428,8.400031,-8.864378,-6.275017,6.441696,9.589242,6.960942,-1.736123,-0.552459,-5.134944,9.936605,-9.133164,-3.352437,1.968114,2.532849,7.465010],[-6.597458,-8.954472,2.571064,-2.506169,-4.845734,-4.942784,-7.315459,-5.675132,-9.642593,5.876379,1.027226,-5.136036,0.800976,5.179946,-3.006409,9.839653],[-4.826307,-9.377613,-9.151679,-3.288530,-2.063123,-2.758712,8.258823,-8.763354,2.423956,-0.131399,1.319856,8.522913,-9.607077,-6.716883,8.240566,-6.124928],[2.402750,7.628782,9.816105,0.652817,-8.785322,-3.286692,-6.354654,-8.329810,-4.861803,1.370769,2.098279,-3.348513,6.623558,7.046354,-3.238312,-1.148791]],[[-1.569808,-5.666308,-1.517878,1.124637,1.281536,-6.737874,-9.230032,-1.636109,3.473230,8.445664,-7.667785,6.061840,-6.347172,-4.449831,-2.229450,-8.264869],[-3.028907,-3.514971,-7.092120,-2.028867,5.249321,-3.482273,7.053876,8.300903,-9.674820,5.717733,-5.559427,-2.909178,7.399102,-3.959170,-5.360556,-1.521324],[2.580154,2.038491,6.598497,8.946470,-6.955792,-3.760864,-4.846896,5.547697,-7.053732,7.005634,5.882929,0.992674,-8.754993,-3.964419,5.582313,-7.084275],[2.954024,-1.233975,2.730969,6.068804,4.540802,2.630910,9.224744,-7.049057,1.529278,5.630772,-3.595937,-4.168039,-8.006971,2.667203,8.406278,-3.494031],[2.711887,4.525341,-3.088126,-5.086804,4.732381,-4.177808,-8.117095,-5.698976,-6.830931,-5.862665,7.455994,-0.798552,1.136864,1.009229,0.413678,9.262446],[-1.512422,8.614133,-9.387031,0.539769,5.053308,-0.944966,-1.484251,1.531525,-7.088769,9.983682,-7.445640,4.735645,1.790320,0.332761,-4.783410,8.907688],[3.429729,-8.712954,8.360369,7.936986,6.775929,-4.230916,3.280463,-9.872003,-0.447135,5.553684,5.930898,-4.890564,0.482565,0.757681,0.806288,-1.146782],[8.173876,-1.734204,-0.103895,8.083578,3.864645,-1.798709,-0.311533,3.878536,-6.341574,3.859521,2.501860,6.834108,0.668468,6.353479,2.666632,-7.242480],[-1.946804,5.479690,-6.708324,-7.184057,8.192211,-7.535825,0.617126,-3.689074,-6.695780,-6.410119,5.533704,-3.330803,-2.370951,7.564161,-4.425084,8.886687],[-3.186406,3.790199,3.469970,2.009170,-7.708940,-8.253901,5.311746,-2.925346,5.041207,1.720021,-1.160379,2.411753,2.164811,-9.753328,-5.609080,-1.777885],[6.735608,-9.012856,6.613063,0.989895,4.911177,-2.136482,-0.058935,2.391989,4.282211,-5.934918,-7.347234,-2.202770,3.775335,6.313706,-3.342073,-2.285589]],[[-2.884137,3.685498,-0.593340,4.681145,-1.416740,-3.313639,-4.556356,-6.563997,7.018358,1.085086,8.658984,6.012587,6.910913,-8.515317,0.434109,6.087161],[9.883850,6.836081,4.676155,-8.049271,-8.278392,-0.189311,-8.115996,-6.607987,3.926138,7.374283,-7.284848,8.383268,-5.153205,5.920199,1.051280,8.417600],[5.581692,-5.324393,1.219194,1.313456,-2.326198,6.944938,-4.779641,-4.652086,8.949337,-3.005135,-2.262414,6.791585,-9.393268,-0.256331,2.765038,-0.289848],[3.130934,6.118468,2.537370,-3.950531,-3.045569,-0.814692,-0.062434,0.126584,1.861968,2.682027,0.046309,-8.177991,2.905716,2.515520,-0.909172,-0.619495],[1.684341,-9.563696,-9.114805,-1.959761,-3.763750,6.110082,4.293754,6.223217,9.565409,-8.548789,8.077569,-3.449160,-2.027239,-9.688964,2.557510,-9.108393],[-6.706010,-0.511649,9.910989,-7.244806,2.110393,-3.307928,-0.437891,9.717395,-7.614064,-2.802656,-3.373735,3.409930,5.514228,6.196133,-0.698005,8.649968],[7.842455,5.589149,-7.280867,-3.399762,3.075420,-9.234375,-3.786157,7.584724,5.734663,7.173294,-3.683264,-2.250038,-0.533917,6.468099,3.899299,0.032913],[-5.724284,-4.298307,-3.364056,-7.175068,8.465607,7.828864,4.235995,2.564741,0.064538,-4.159022,5.202307,9.656455,2.826137,-6.603967,7.193884,7.568903],[-4.702726,-8.017832,-7.667901,-2.451254,1.891964,-9.627505,7.027659,6.732835,-3.477590,-2.257787,0.738521,5.345198,-0.128689,7.438654,7.890940,8.863873],[-6.550375,1.399907,8.676389,3.837526,5.030165,9.884226,6.244716,8.409228,-3.839351,6.641954,1.362115,-5.627095,-9.101803,4.736053,-9.647158,6.035347],[-5.505025,-1.399923,-7.172780,-6.447042,0.793107,-7.246776,2.014965,-4.845233,-6.415159,5.558819,-0.919926,1.953984,9.059622,-1.984844,-1.872254,7.911261]]], dtype = "float64")#candidate|1741|(3, 11, 16)|const|float64
uop_1742 = relay.cos(const_1741.astype('float64')) # shape=(3, 11, 16)
output = uop_1742
output2 = uop_1742
func_1756 = relay.Function([], output)
mod['func_1756'] = func_1756
mod = relay.transform.InferType()(mod)
output = func_1756()
func_1757 = relay.Function([], output)
mutated_mod['func_1757'] = func_1757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1593_call = mod.get_global_var('func_1593')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_1809 = func_1593_call()
call_1810 = func_1593_call()
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
var_1819 = relay.var("var_1819", dtype = "uint8", shape = (8, 36))#candidate|1819|(8, 36)|var|uint8
call_1818 = relay.TupleGetItem(func_1247_call(relay.reshape(var_1819.astype('uint8'), [288,])), 0)
call_1820 = relay.TupleGetItem(func_1250_call(relay.reshape(var_1819.astype('uint8'), [288,])), 0)
output = relay.Tuple([call_1809,call_1818,var_1819,])
output2 = relay.Tuple([call_1810,call_1820,var_1819,])
func_1836 = relay.Function([var_1819,], output)
mod['func_1836'] = func_1836
mod = relay.transform.InferType()(mod)
mutated_mod['func_1836'] = func_1836
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1837 = relay.var("var_1837", dtype = "uint8", shape = (8, 36))#candidate|1837|(8, 36)|var|uint8
func_1836_call = mutated_mod.get_global_var('func_1836')
call_1838 = func_1836_call(var_1837)
output = call_1838
func_1839 = relay.Function([var_1837], output)
mutated_mod['func_1839'] = func_1839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_1854 = relay.TupleGetItem(func_1634_call(), 0)
call_1855 = relay.TupleGetItem(func_1636_call(), 0)
output = call_1854
output2 = call_1855
func_1863 = relay.Function([], output)
mod['func_1863'] = func_1863
mod = relay.transform.InferType()(mod)
output = func_1863()
func_1864 = relay.Function([], output)
mutated_mod['func_1864'] = func_1864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_1868 = relay.TupleGetItem(func_1634_call(), 0)
call_1869 = relay.TupleGetItem(func_1636_call(), 0)
uop_1876 = relay.cosh(call_1868.astype('float32')) # shape=(1, 16, 7)
uop_1878 = relay.cosh(call_1869.astype('float32')) # shape=(1, 16, 7)
output = uop_1876
output2 = uop_1878
func_1879 = relay.Function([], output)
mod['func_1879'] = func_1879
mod = relay.transform.InferType()(mod)
mutated_mod['func_1879'] = func_1879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mutated_mod.get_global_var('func_1879')
call_1880 = func_1879_call()
output = call_1880
func_1881 = relay.Function([], output)
mutated_mod['func_1881'] = func_1881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1881_call = mutated_mod.get_global_var('func_1881')
call_1975 = func_1879_call()
call_1976 = func_1879_call()
uop_1988 = relay.asinh(call_1975.astype('float32')) # shape=(1, 16, 7)
uop_1990 = relay.asinh(call_1976.astype('float32')) # shape=(1, 16, 7)
bop_1991 = relay.multiply(uop_1988.astype('uint64'), relay.reshape(call_1975.astype('uint64'), relay.shape_of(uop_1988))) # shape=(1, 16, 7)
bop_1994 = relay.multiply(uop_1990.astype('uint64'), relay.reshape(call_1976.astype('uint64'), relay.shape_of(uop_1990))) # shape=(1, 16, 7)
func_124_call = mod.get_global_var('func_124')
func_127_call = mutated_mod.get_global_var('func_127')
var_1997 = relay.var("var_1997", dtype = "float64", shape = (150,))#candidate|1997|(150,)|var|float64
call_1996 = func_124_call(relay.reshape(var_1997.astype('float64'), [2, 15, 5]))
call_1998 = func_124_call(relay.reshape(var_1997.astype('float64'), [2, 15, 5]))
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_2000 = relay.TupleGetItem(func_1634_call(), 1)
call_2001 = relay.TupleGetItem(func_1636_call(), 1)
func_435_call = mod.get_global_var('func_435')
func_437_call = mutated_mod.get_global_var('func_437')
call_2002 = relay.TupleGetItem(func_435_call(relay.reshape(call_1996.astype('float64'), [5, 30])), 1)
call_2003 = relay.TupleGetItem(func_437_call(relay.reshape(call_1996.astype('float64'), [5, 30])), 1)
uop_2006 = relay.cos(call_2002.astype('float32')) # shape=(2, 15, 5)
uop_2008 = relay.cos(call_2003.astype('float32')) # shape=(2, 15, 5)
func_124_call = mod.get_global_var('func_124')
func_127_call = mutated_mod.get_global_var('func_127')
call_2020 = func_124_call(relay.reshape(call_1996.astype('float64'), [2, 15, 5]))
call_2021 = func_124_call(relay.reshape(call_1996.astype('float64'), [2, 15, 5]))
uop_2022 = relay.acos(call_2020.astype('float64')) # shape=(2, 15, 5)
uop_2024 = relay.acos(call_2021.astype('float64')) # shape=(2, 15, 5)
output = relay.Tuple([bop_1991,call_1996,var_1997,call_2000,uop_2006,uop_2022,])
output2 = relay.Tuple([bop_1994,call_1998,var_1997,call_2001,uop_2008,uop_2024,])
func_2027 = relay.Function([var_1997,], output)
mod['func_2027'] = func_2027
mod = relay.transform.InferType()(mod)
var_2028 = relay.var("var_2028", dtype = "float64", shape = (150,))#candidate|2028|(150,)|var|float64
output = func_2027(var_2028)
func_2029 = relay.Function([var_2028], output)
mutated_mod['func_2029'] = func_2029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1881_call = mutated_mod.get_global_var('func_1881')
call_2055 = func_1879_call()
call_2056 = func_1879_call()
func_124_call = mod.get_global_var('func_124')
func_127_call = mutated_mod.get_global_var('func_127')
const_2065 = relay.const([2.714393,1.412955,-9.619831,2.570728,-2.895315,8.634422,7.185520,-9.470219,-5.290083,-0.030208,-5.133765,9.629544,-8.527209,4.805936,5.229378,3.190324,0.102565,-5.607142,8.548827,-6.474606,8.701201,7.336787,-7.705598,-2.183492,-7.177408,-9.182979,-3.443570,-0.740853,-8.331869,2.730650,-1.003236,9.962586,4.440257,-0.366311,4.389734,-8.464433,-9.131804,8.877676,4.050170,3.944104,-1.454884,0.080006,9.568926,9.346875,1.019486,0.535287,-2.875802,8.989087,-3.495906,-7.150617,6.711128,-9.877645,-2.949284,-5.814867,5.754346,8.662339,2.521787,1.452937,-7.463915,4.496178,1.641227,-8.826062,5.568109,8.367842,4.875367,0.459532,-5.878426,-6.592306,7.030396,-4.458732,-0.948490,-3.586929,-9.469422,-1.138889,-1.236488,-9.500309,2.115922,5.733502,9.995501,-2.619644,1.810525,9.232421,-2.972909,-9.986605,-4.728296,-6.247727,9.339925,-6.534864,-2.889682,-4.780522,-3.468609,-0.654728,1.600571,-9.396006,-0.682706,1.007533,-9.274857,4.147186,-7.180080,-2.422971,9.631810,3.315550,3.933725,-5.615064,6.572624,4.920812,-5.436973,9.534929,4.142039,-3.639151,-4.857990,3.671477,-8.069994,3.125344,6.987674,7.668520,3.416532,9.717855,-1.342761,-7.321669,-0.241414,-3.372519,-0.093146,6.046919,1.925998,7.349724,9.230021,4.607585,-6.747542,5.716384,-4.792433,-9.363452,1.830336,7.433359,6.902450,8.678414,6.198082,-6.781607,0.800734,0.602087,6.211646,9.830106,-3.883564,-9.156198,0.452404,-9.359318,-7.962151,6.453593,-8.965607,-3.580093], dtype = "float64")#candidate|2065|(150,)|const|float64
call_2064 = func_124_call(relay.reshape(const_2065.astype('float64'), [2, 15, 5]))
call_2066 = func_124_call(relay.reshape(const_2065.astype('float64'), [2, 15, 5]))
output = relay.Tuple([call_2055,call_2064,const_2065,])
output2 = relay.Tuple([call_2056,call_2066,const_2065,])
func_2072 = relay.Function([], output)
mod['func_2072'] = func_2072
mod = relay.transform.InferType()(mod)
mutated_mod['func_2072'] = func_2072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mutated_mod.get_global_var('func_2072')
call_2073 = func_2072_call()
output = call_2073
func_2074 = relay.Function([], output)
mutated_mod['func_2074'] = func_2074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_2104 = relay.TupleGetItem(func_1634_call(), 0)
call_2105 = relay.TupleGetItem(func_1636_call(), 0)
output = relay.Tuple([call_2104,])
output2 = relay.Tuple([call_2105,])
func_2107 = relay.Function([], output)
mod['func_2107'] = func_2107
mod = relay.transform.InferType()(mod)
mutated_mod['func_2107'] = func_2107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2107_call = mutated_mod.get_global_var('func_2107')
call_2108 = func_2107_call()
output = call_2108
func_2109 = relay.Function([], output)
mutated_mod['func_2109'] = func_2109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1605_call = mod.get_global_var('func_1605')
func_1606_call = mutated_mod.get_global_var('func_1606')
call_2110 = relay.TupleGetItem(func_1605_call(), 0)
call_2111 = relay.TupleGetItem(func_1606_call(), 0)
output = relay.Tuple([call_2110,])
output2 = relay.Tuple([call_2111,])
func_2117 = relay.Function([], output)
mod['func_2117'] = func_2117
mod = relay.transform.InferType()(mod)
output = func_2117()
func_2118 = relay.Function([], output)
mutated_mod['func_2118'] = func_2118
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2145 = relay.var("var_2145", dtype = "uint32", shape = (10, 3, 8))#candidate|2145|(10, 3, 8)|var|uint32
const_2146 = relay.const([[[-1,-4,-10,-6,-5,-3,6,-10],[2,3,-10,-8,2,3,-8,-1],[6,6,4,-2,-10,-8,1,-5]],[[7,6,4,-4,7,-2,-10,6],[8,4,3,9,-3,10,-6,-6],[-3,-10,-6,7,-4,8,2,2]],[[5,-2,-1,4,1,-7,8,-7],[6,10,-4,7,6,1,-9,-9],[-8,5,-5,1,-4,2,2,5]],[[-9,-1,-3,-8,-4,-8,4,1],[10,9,-6,1,9,-2,-3,2],[-3,4,1,-5,-2,2,-2,-6]],[[-9,-8,-7,5,-4,-8,5,8],[3,3,3,1,-3,-1,-5,9],[-4,-1,8,7,-4,-9,-7,6]],[[-1,3,9,1,-8,8,1,-7],[4,6,-5,-4,-9,7,-1,5],[-4,-6,-4,-4,1,-6,-9,9]],[[-1,5,-1,-5,3,-8,5,-6],[4,3,-1,2,10,8,3,3],[4,9,9,6,8,-8,-9,-3]],[[8,-3,-2,5,-5,1,10,-1],[4,-10,6,6,-3,-8,-9,-5],[6,10,-5,1,-5,5,8,2]],[[7,-4,-1,6,3,4,4,10],[9,9,-2,1,3,-7,-3,-3],[-2,-3,7,6,-5,3,2,-1]],[[-3,5,1,5,2,-4,-2,5],[-4,-6,10,-1,4,6,7,-7],[10,-6,-7,-6,4,6,-9,-9]]], dtype = "uint32")#candidate|2146|(10, 3, 8)|const|uint32
bop_2147 = relay.add(var_2145.astype('uint32'), relay.reshape(const_2146.astype('uint32'), relay.shape_of(var_2145))) # shape=(10, 3, 8)
func_322_call = mod.get_global_var('func_322')
func_326_call = mutated_mod.get_global_var('func_326')
const_2156 = relay.const(8, dtype = "int32")#candidate|2156|()|const|int32
var_2157 = relay.var("var_2157", dtype = "int32", shape = (2, 2))#candidate|2157|(2, 2)|var|int32
call_2155 = func_322_call(relay.reshape(const_2156.astype('int32'), []), relay.reshape(var_2157.astype('int32'), [1, 1, 4]), )
call_2158 = func_322_call(relay.reshape(const_2156.astype('int32'), []), relay.reshape(var_2157.astype('int32'), [1, 1, 4]), )
func_1756_call = mod.get_global_var('func_1756')
func_1757_call = mutated_mod.get_global_var('func_1757')
call_2177 = func_1756_call()
call_2178 = func_1756_call()
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_2179 = relay.TupleGetItem(func_1634_call(), 1)
call_2180 = relay.TupleGetItem(func_1636_call(), 1)
output = relay.Tuple([bop_2147,call_2155,const_2156,var_2157,call_2177,call_2179,])
output2 = relay.Tuple([bop_2147,call_2158,const_2156,var_2157,call_2178,call_2180,])
func_2184 = relay.Function([var_2145,var_2157,], output)
mod['func_2184'] = func_2184
mod = relay.transform.InferType()(mod)
mutated_mod['func_2184'] = func_2184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2184_call = mutated_mod.get_global_var('func_2184')
var_2186 = relay.var("var_2186", dtype = "uint32", shape = (10, 3, 8))#candidate|2186|(10, 3, 8)|var|uint32
var_2187 = relay.var("var_2187", dtype = "int32", shape = (2, 2))#candidate|2187|(2, 2)|var|int32
call_2185 = func_2184_call(var_2186,var_2187,)
output = call_2185
func_2188 = relay.Function([var_2186,var_2187,], output)
mutated_mod['func_2188'] = func_2188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2117_call = mod.get_global_var('func_2117')
func_2118_call = mutated_mod.get_global_var('func_2118')
call_2279 = relay.TupleGetItem(func_2117_call(), 0)
call_2280 = relay.TupleGetItem(func_2118_call(), 0)
func_322_call = mod.get_global_var('func_322')
func_326_call = mutated_mod.get_global_var('func_326')
const_2282 = relay.const(2, dtype = "int32")#candidate|2282|()|const|int32
const_2283 = relay.const([-2,3,-8,-7], dtype = "int32")#candidate|2283|(4,)|const|int32
call_2281 = func_322_call(relay.reshape(const_2282.astype('int32'), []), relay.reshape(const_2283.astype('int32'), [1, 1, 4]), )
call_2284 = func_322_call(relay.reshape(const_2282.astype('int32'), []), relay.reshape(const_2283.astype('int32'), [1, 1, 4]), )
output = relay.Tuple([call_2279,call_2281,const_2282,const_2283,])
output2 = relay.Tuple([call_2280,call_2284,const_2282,const_2283,])
func_2286 = relay.Function([], output)
mod['func_2286'] = func_2286
mod = relay.transform.InferType()(mod)
output = func_2286()
func_2287 = relay.Function([], output)
mutated_mod['func_2287'] = func_2287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1605_call = mod.get_global_var('func_1605')
func_1606_call = mutated_mod.get_global_var('func_1606')
call_2288 = relay.TupleGetItem(func_1605_call(), 0)
call_2289 = relay.TupleGetItem(func_1606_call(), 0)
uop_2303 = relay.sinh(call_2288.astype('float64')) # shape=(1, 16, 7)
uop_2305 = relay.sinh(call_2289.astype('float64')) # shape=(1, 16, 7)
bop_2309 = relay.logical_and(uop_2303.astype('bool'), relay.reshape(call_2288.astype('bool'), relay.shape_of(uop_2303))) # shape=(1, 16, 7)
bop_2312 = relay.logical_and(uop_2305.astype('bool'), relay.reshape(call_2289.astype('bool'), relay.shape_of(uop_2305))) # shape=(1, 16, 7)
output = bop_2309
output2 = bop_2312
func_2313 = relay.Function([], output)
mod['func_2313'] = func_2313
mod = relay.transform.InferType()(mod)
mutated_mod['func_2313'] = func_2313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2313_call = mutated_mod.get_global_var('func_2313')
call_2314 = func_2313_call()
output = call_2314
func_2315 = relay.Function([], output)
mutated_mod['func_2315'] = func_2315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1756_call = mod.get_global_var('func_1756')
func_1757_call = mutated_mod.get_global_var('func_1757')
call_2319 = func_1756_call()
call_2320 = func_1756_call()
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
var_2324 = relay.var("var_2324", dtype = "float64", shape = (150,))#candidate|2324|(150,)|var|float64
call_2323 = relay.TupleGetItem(func_2027_call(relay.reshape(var_2324.astype('float64'), [150,])), 3)
call_2325 = relay.TupleGetItem(func_2029_call(relay.reshape(var_2324.astype('float64'), [150,])), 3)
const_2335 = relay.const([[[0.282075,-9.641895,1.756539,-8.462439,0.543748,-4.165047,-2.105835],[6.638517,-5.506764,-1.969349,-1.813186,6.192608,-2.612680,6.237885],[-4.172090,-6.290275,9.966625,-2.319145,9.920537,-6.081496,9.048314],[-9.584039,-4.081598,0.385352,-6.270455,-6.506755,-5.080163,-4.554479],[-5.246385,4.811392,5.219712,-9.079783,8.215433,6.163767,7.589027],[6.346206,-3.791815,-2.264172,9.462100,-8.123232,9.041983,-5.396267],[-9.412766,-2.581409,-6.237497,7.047324,-9.047545,8.368738,5.579691],[-6.970019,-6.817453,7.796993,1.704762,-9.969231,5.161861,-4.851993],[3.787079,-4.738201,-2.714500,-1.938148,9.702117,-2.377191,0.163313],[1.703784,-0.122492,9.099110,2.309153,3.726818,-0.248742,9.349926],[-3.016885,2.980646,4.882477,-3.090241,-2.120346,-1.134439,-0.871977],[4.839795,-9.348531,-0.994085,-3.195097,-9.596124,-1.842970,2.051050],[1.013290,4.162169,-0.867266,5.781915,-9.829705,0.242012,-4.733513],[-4.852171,-3.265479,-5.521354,-9.249587,8.763163,-4.229620,-2.427729],[-3.393774,5.417753,5.818280,4.035360,8.769729,3.924411,-5.746343],[2.801439,-7.321578,-4.586924,9.451528,-7.445344,6.765542,6.229617]],[[0.019937,4.113191,7.231204,4.243731,3.444389,-5.752044,5.828078],[-0.354284,3.596040,-0.278071,-0.616575,-7.843011,3.442886,7.196018],[0.655295,-3.430659,9.848717,-3.192707,-5.670752,7.268091,-2.472555],[7.154163,2.594802,-0.749825,4.667097,-3.138712,4.365818,4.292639],[4.042720,8.034067,8.636980,3.199991,0.471595,2.763080,5.183615],[2.020569,9.588008,6.584782,8.012174,8.147217,-5.346698,-6.357184],[-7.606204,-9.249364,-6.281706,-1.860236,3.207332,-5.062750,6.460826],[5.018460,-8.656147,5.353449,4.745083,-9.593076,-5.323835,9.737556],[-7.111018,-8.515139,5.159479,-1.595736,-2.941704,-5.957418,4.332364],[2.094184,-5.117787,0.919003,4.578005,-3.155050,-2.427419,1.233543],[-0.775374,5.816669,-2.411047,-2.581006,5.566992,-3.789607,2.121065],[4.408875,5.267992,-7.967610,3.941443,4.808192,-7.785248,0.736391],[-0.138075,4.704553,7.486984,4.827091,-1.589363,-5.358795,0.891510],[3.934282,4.575465,7.675864,7.865747,-4.417697,6.703698,-9.536357],[-4.845617,-4.516355,-4.671930,0.925204,7.491646,-2.412499,-6.812226],[6.594785,8.520036,6.474797,3.056635,5.311303,-2.536781,-9.133071]],[[4.358041,2.738418,-7.461518,0.079769,2.002383,2.180688,8.546191],[-0.167078,-7.747951,4.204769,-1.418134,-2.068853,5.210349,6.048169],[6.517375,-3.275617,-8.838832,-1.059131,0.377551,1.979994,6.538454],[8.558661,-6.265218,-9.233439,4.917935,-6.779324,-2.443774,-6.099129],[3.314577,7.101687,5.727926,8.659211,9.005708,-4.390798,3.461911],[3.026517,-8.642993,-5.526231,-3.064172,8.044681,-9.979912,-5.114942],[-7.922821,9.819516,-5.938689,7.135681,-5.770912,9.062140,-1.425216],[-1.874349,7.233454,-9.424815,1.166081,7.466921,-2.297361,4.650261],[-8.740641,2.952468,-6.175014,-2.336026,-4.813863,-1.419949,3.382640],[-0.182764,-1.668489,4.157294,0.855547,1.866418,-0.794425,-5.656275],[-3.885040,-9.457914,0.778849,9.328665,-3.455202,-9.829501,5.369737],[2.687841,-5.620240,2.327842,-1.908552,5.683407,-2.819725,-4.426085],[4.756091,7.161903,5.702064,-6.566106,-6.601182,-1.295992,-8.313378],[4.494574,-4.986518,-4.736963,-3.956083,7.425026,-7.800536,-3.575255],[6.212803,-3.826510,-0.292974,-9.598477,5.170328,-7.100702,0.272270],[-0.860891,-9.048682,7.655278,-6.369759,3.774097,4.337517,9.165760]],[[7.148234,0.151381,0.783966,1.072383,2.517852,0.088072,9.866753],[-2.993462,-6.822569,-5.048815,-6.681793,2.364680,3.845631,-7.938099],[5.762511,-0.167583,6.794182,-6.696555,3.526268,-2.168351,1.997652],[4.320220,-9.864939,4.852999,-4.336886,8.809133,-2.768223,4.480051],[5.007555,-8.799016,-2.366065,-8.106817,-1.250170,-5.770223,-5.723312],[4.981705,-2.789353,-1.758817,-9.229442,0.809563,8.990896,-7.486563],[-7.957616,5.694037,0.440667,-8.252116,3.061082,1.391459,1.474018],[8.193093,7.744860,-8.693896,-4.488494,-2.564398,-0.449896,6.363515],[-0.892239,6.262653,-8.281150,-2.760384,6.602435,5.648815,9.593412],[-6.316175,-0.338374,7.024554,-6.245883,2.507680,-1.464990,-7.825810],[2.047934,8.639196,5.828898,-2.658490,7.158885,3.830249,-3.766005],[5.452606,1.945442,-1.118209,-6.500151,9.164217,2.387290,2.207874],[-0.081686,6.583685,1.144961,0.164206,1.576870,-1.508507,9.407440],[9.684777,-3.243920,0.847450,4.005554,6.196283,1.687258,-4.992363],[3.887415,7.045766,0.632235,-7.643871,7.925959,5.584017,6.254983],[1.938408,9.086117,-0.532562,-7.168998,-7.113767,-5.716189,8.936574]]], dtype = "float64")#candidate|2335|(4, 16, 7)|const|float64
bop_2336 = relay.maximum(call_2323.astype('uint8'), const_2335.astype('uint8')) # shape=(4, 16, 7)
bop_2339 = relay.maximum(call_2325.astype('uint8'), const_2335.astype('uint8')) # shape=(4, 16, 7)
uop_2345 = relay.asinh(call_2319.astype('float64')) # shape=(3, 11, 16)
uop_2347 = relay.asinh(call_2320.astype('float64')) # shape=(3, 11, 16)
bop_2356 = relay.less(uop_2345.astype('bool'), relay.reshape(call_2319.astype('bool'), relay.shape_of(uop_2345))) # shape=(3, 11, 16)
bop_2359 = relay.less(uop_2347.astype('bool'), relay.reshape(call_2320.astype('bool'), relay.shape_of(uop_2347))) # shape=(3, 11, 16)
var_2361 = relay.var("var_2361", dtype = "float64", shape = (3, 11, 16))#candidate|2361|(3, 11, 16)|var|float64
bop_2362 = relay.maximum(uop_2345.astype('uint8'), relay.reshape(var_2361.astype('uint8'), relay.shape_of(uop_2345))) # shape=(3, 11, 16)
bop_2365 = relay.maximum(uop_2347.astype('uint8'), relay.reshape(var_2361.astype('uint8'), relay.shape_of(uop_2347))) # shape=(3, 11, 16)
output = relay.Tuple([var_2324,bop_2336,bop_2356,bop_2362,])
output2 = relay.Tuple([var_2324,bop_2339,bop_2359,bop_2365,])
func_2367 = relay.Function([var_2324,var_2361,], output)
mod['func_2367'] = func_2367
mod = relay.transform.InferType()(mod)
var_2368 = relay.var("var_2368", dtype = "float64", shape = (150,))#candidate|2368|(150,)|var|float64
var_2369 = relay.var("var_2369", dtype = "float64", shape = (3, 11, 16))#candidate|2369|(3, 11, 16)|var|float64
output = func_2367(var_2368,var_2369,)
func_2370 = relay.Function([var_2368,var_2369,], output)
mutated_mod['func_2370'] = func_2370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2286_call = mod.get_global_var('func_2286')
func_2287_call = mutated_mod.get_global_var('func_2287')
call_2386 = relay.TupleGetItem(func_2286_call(), 3)
call_2387 = relay.TupleGetItem(func_2287_call(), 3)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_2388 = relay.TupleGetItem(func_2072_call(), 2)
call_2389 = relay.TupleGetItem(func_2074_call(), 2)
output = relay.Tuple([call_2386,call_2388,])
output2 = relay.Tuple([call_2387,call_2389,])
func_2394 = relay.Function([], output)
mod['func_2394'] = func_2394
mod = relay.transform.InferType()(mod)
mutated_mod['func_2394'] = func_2394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2394_call = mutated_mod.get_global_var('func_2394')
call_2395 = func_2394_call()
output = call_2395
func_2396 = relay.Function([], output)
mutated_mod['func_2396'] = func_2396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1593_call = mod.get_global_var('func_1593')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_2414 = func_1593_call()
call_2415 = func_1593_call()
output = call_2414
output2 = call_2415
func_2424 = relay.Function([], output)
mod['func_2424'] = func_2424
mod = relay.transform.InferType()(mod)
mutated_mod['func_2424'] = func_2424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2424_call = mutated_mod.get_global_var('func_2424')
call_2425 = func_2424_call()
output = call_2425
func_2426 = relay.Function([], output)
mutated_mod['func_2426'] = func_2426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2445 = relay.var("var_2445", dtype = "float64", shape = (14, 8, 15))#candidate|2445|(14, 8, 15)|var|float64
uop_2446 = relay.log10(var_2445.astype('float64')) # shape=(14, 8, 15)
func_635_call = mod.get_global_var('func_635')
func_639_call = mutated_mod.get_global_var('func_639')
const_2454 = relay.const([8,-10,7,4,10,-2,1,-2,8,-7,9,-9,-8,-7,8,8,8,-7,-5,-3,-8,-7,-5,-5,-3,1,-4,1,3,-4,6,7,1,10,-6,2,-10,-2,-9,7,-1,-2,-1,8,2,4,-5,3,4,3,-8,3,-5,-2,4,-6,10,-10,2,-4,2,-4,9,-3,9,-5,3,5,-5,-2,-8,5,-6,-10,7,-5,-2,-5,6,-5,6,-4,-10,-8,-7,5,1,-5,9,7,9,-2,-1,-3,-7,-2,8,3,-4,-2,-3,8,1,1,9,5,-10,-9], dtype = "int16")#candidate|2454|(108,)|const|int16
call_2453 = relay.TupleGetItem(func_635_call(relay.reshape(const_2454.astype('int16'), [2, 9, 6]), relay.reshape(const_2454.astype('int16'), [2, 9, 6]), ), 0)
call_2455 = relay.TupleGetItem(func_639_call(relay.reshape(const_2454.astype('int16'), [2, 9, 6]), relay.reshape(const_2454.astype('int16'), [2, 9, 6]), ), 0)
bop_2458 = relay.less(uop_2446.astype('bool'), relay.reshape(var_2445.astype('bool'), relay.shape_of(uop_2446))) # shape=(14, 8, 15)
func_2184_call = mod.get_global_var('func_2184')
func_2188_call = mutated_mod.get_global_var('func_2188')
var_2473 = relay.var("var_2473", dtype = "uint32", shape = (2, 120))#candidate|2473|(2, 120)|var|uint32
const_2474 = relay.const([6,-6,-7,10], dtype = "int32")#candidate|2474|(4,)|const|int32
call_2472 = relay.TupleGetItem(func_2184_call(relay.reshape(var_2473.astype('uint32'), [10, 3, 8]), relay.reshape(const_2474.astype('int32'), [2, 2]), ), 3)
call_2475 = relay.TupleGetItem(func_2188_call(relay.reshape(var_2473.astype('uint32'), [10, 3, 8]), relay.reshape(const_2474.astype('int32'), [2, 2]), ), 3)
uop_2477 = relay.cos(uop_2446.astype('float64')) # shape=(14, 8, 15)
func_2367_call = mod.get_global_var('func_2367')
func_2370_call = mutated_mod.get_global_var('func_2370')
var_2482 = relay.var("var_2482", dtype = "float64", shape = (150,))#candidate|2482|(150,)|var|float64
const_2483 = relay.const([1.490530,0.254961,-4.747034,-1.833816,-7.703646,-0.281922,4.870321,-6.361063,8.093359,9.613060,-4.197850,2.821184,7.683882,0.929857,-5.984340,-1.197409,-8.923228,4.384585,-5.166686,7.082591,-9.918614,6.054802,-3.672614,-3.797497,-7.127373,3.592939,-5.791450,5.253457,-1.533564,-6.609141,-4.686362,-5.669706,-0.789575,9.412387,6.930109,-2.725588,-9.494093,0.899728,1.482156,-9.359588,-1.684506,7.095228,1.562651,-0.503667,5.543864,-9.376827,0.295235,-5.816567,-7.859675,0.349431,-8.644949,-7.842326,2.364135,-7.148708,0.041271,-1.819144,-1.813936,6.151651,4.546768,8.761662,-2.952373,-1.169940,-1.198428,-4.532633,-0.755796,-5.479042,1.978058,-7.351018,8.167635,1.989979,6.604477,-6.657486,3.279650,7.371789,7.993178,1.034535,9.732075,1.418334,6.641540,-6.146172,6.246895,-0.220077,4.580519,-4.819899,9.028851,-7.602486,5.601351,9.589089,-8.046540,4.345766,7.698630,9.765436,-5.395117,0.932612,-6.721188,-2.127748,-2.679420,-1.504406,6.017807,-4.620668,8.285248,1.181807,4.237416,5.396418,-9.055039,9.026078,-6.075757,-5.684533,-0.874424,-0.215964,9.314588,-2.987559,0.879937,-1.903318,1.464869,-2.255197,6.073159,-2.942511,-9.734826,-2.198127,-7.713597,-0.548644,-3.609573,-0.753264,-9.952427,-1.021115,8.862708,-8.652185,5.746835,9.365960,6.992187,7.860163,3.654757,-9.870298,-5.554673,-6.897994,-6.825057,1.676723,8.742553,2.831903,-0.193735,-0.305750,2.375651,-7.793368,6.455650,6.484023,6.240790,7.881517,-6.173978,-5.215000,-6.721663,-5.389638,-7.661456,2.544210,3.295408,8.120481,-5.399723,9.084160,-5.104829,5.161029,1.929671,7.236099,0.872475,3.414462,-0.542987,-9.145543,4.642431,9.791972,-5.231853,9.020338,-0.189554,4.388800,-6.894997,-2.227836,9.889719,-0.386597,-9.917522,2.028895,-2.377263,-9.805293,9.340743,3.796435,3.102285,-4.047394,-9.766052,7.374387,-5.432596,3.377909,4.269620,-9.337668,5.093561,6.441026,-1.306412,-0.370597,7.994462,9.179519,3.205633,9.908986,2.505330,0.344272,-3.338481,-8.243016,9.483727,5.143850,6.121465,9.412845,9.729927,3.898860,-7.775136,-3.847858,-4.525493,-6.404881,2.500649,-6.106072,5.935216,-7.839129,-9.543367,-0.111684,-0.464467,-2.503065,9.513142,2.614241,-8.764246,-9.660738,-7.673484,-1.807424,-4.064985,-9.541208,8.557351,5.059913,-2.554306,-1.028793,-0.744934,6.087979,-8.865675,9.389117,0.482685,-1.611966,6.093729,-9.861647,-5.222554,-0.329343,1.607884,-6.499847,9.266593,5.349350,7.858836,-3.235499,3.507862,-9.276561,8.749571,4.837289,-3.848126,-0.712443,0.808139,2.154243,2.481584,-4.312346,9.967084,9.242826,-6.461272,-9.266692,-2.040714,-5.108186,-5.087682,-8.786429,-0.306026,2.673928,0.232743,-0.311806,-9.196138,-3.092542,8.698042,2.584994,6.053030,9.217496,8.191161,2.794515,-5.330653,5.259198,4.806221,-9.842518,-1.549320,-5.000404,2.946384,-2.426952,3.610694,9.092198,3.069464,2.309732,-6.039872,6.047158,-4.759960,6.700220,-5.680087,-5.085935,-7.520791,8.643616,-5.945712,8.014688,-1.123738,7.321556,-3.741331,-5.349800,6.781231,0.321372,-4.426599,-2.468796,4.653276,0.667239,-0.562537,8.743407,-4.703163,3.617179,2.546076,-9.377769,-3.681219,0.428776,-2.889851,5.046859,3.879826,5.238368,3.226895,-9.042570,-3.734612,-3.837307,5.138298,8.475876,-0.975222,-4.869509,3.443564,4.495384,5.685843,0.364554,-6.293095,1.019156,2.824673,7.765549,-8.317533,1.492687,1.288184,-3.277575,-2.211892,-8.554868,-2.999599,-7.320492,2.881937,-9.554563,-5.008481,-7.175601,-5.390249,-6.436588,8.090819,-1.217197,7.743102,-8.106756,0.453332,-8.614004,-2.963565,-9.500370,5.531443,0.794296,-9.484252,1.470811,0.903635,9.143086,-2.273530,4.987999,0.310883,9.001328,4.567773,4.028813,-8.759998,-9.374775,-2.522238,-3.263235,5.271892,-4.032454,2.912498,-0.412780,4.637243,-2.197638,8.653858,4.843300,0.989807,-7.414564,-3.198983,8.914004,3.514487,-7.377898,-4.727127,0.009714,-0.420964,2.296772,-5.453752,-7.265243,7.333971,2.085878,-4.467035,8.374637,4.197957,-9.458521,8.882697,3.136446,-0.849535,-9.486705,-7.038338,-5.195538,4.544265,-3.889753,-9.504199,9.616992,3.041749,-5.760060,-6.900328,5.442326,4.632978,5.690804,5.227141,1.287004,-4.407293,-4.740743,-1.715541,9.350887,-7.413282,1.593218,-3.488062,-8.442780,2.511117,8.445502,-6.988253,7.928038,3.088668,-8.254070,0.412212,-7.885089,2.625178,-5.494596,6.988191,1.769395,9.412978,-6.306745,7.612163,3.532191,-5.798235,-8.132104,3.120020,-9.852469,4.756654,6.191007,1.272817,-7.950985,-6.642912,-0.485102,4.187491,9.140703,-4.138506,-0.685050,-2.658465,-7.828904,1.011834,7.669471,-3.436303,1.568956,-7.772469,2.027650,-8.772407,-5.406042,-2.623724,-7.634089,-5.400925,7.085830,-3.968056,3.290436,4.187760,0.526576,-2.891033,-6.181463,-6.606356,-0.009388,-8.537617,-5.010359,-3.317874,-1.114189,4.734063,-6.097699,-7.185917,-8.504945,8.361406,-5.804055,5.513320,8.808734,-9.049952,9.515574,6.222819,-0.880335,2.933448,-1.510206,5.409743,-9.136307,-1.754421,3.585312,-9.728831,9.165870,9.189119,7.355680,7.910620,-5.369279,-6.976083,-2.308756,-4.131869,9.944703,-2.142260,0.512697,-8.141545,-1.653449,-7.401875,-5.856317,-7.919055,-4.789643,0.147300,-4.886609,0.257117,-2.314679,-1.100276,2.179526,5.518891,-8.020829], dtype = "float64")#candidate|2483|(528,)|const|float64
call_2481 = relay.TupleGetItem(func_2367_call(relay.reshape(var_2482.astype('float64'), [150,]), relay.reshape(const_2483.astype('float64'), [3, 11, 16]), ), 0)
call_2484 = relay.TupleGetItem(func_2370_call(relay.reshape(var_2482.astype('float64'), [150,]), relay.reshape(const_2483.astype('float64'), [3, 11, 16]), ), 0)
func_2286_call = mod.get_global_var('func_2286')
func_2287_call = mutated_mod.get_global_var('func_2287')
call_2488 = relay.TupleGetItem(func_2286_call(), 0)
call_2489 = relay.TupleGetItem(func_2287_call(), 0)
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_2490 = relay.TupleGetItem(func_1634_call(), 1)
call_2491 = relay.TupleGetItem(func_1636_call(), 1)
var_2495 = relay.var("var_2495", dtype = "float64", shape = (14, 8, 15))#candidate|2495|(14, 8, 15)|var|float64
bop_2496 = relay.greater(uop_2477.astype('bool'), relay.reshape(var_2495.astype('bool'), relay.shape_of(uop_2477))) # shape=(14, 8, 15)
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
var_2500 = relay.var("var_2500", dtype = "uint8", shape = (288,))#candidate|2500|(288,)|var|uint8
call_2499 = relay.TupleGetItem(func_1247_call(relay.reshape(var_2500.astype('uint8'), [288,])), 2)
call_2501 = relay.TupleGetItem(func_1250_call(relay.reshape(var_2500.astype('uint8'), [288,])), 2)
const_2514 = relay.const([[[True,False,False,True,True,False,False,False,False,True,True,False,True,True,True],[False,True,False,False,False,True,False,True,True,False,False,False,False,True,True],[True,False,True,True,False,False,True,False,True,True,True,False,False,False,True],[True,True,False,True,True,False,True,True,False,False,True,False,True,True,True],[False,False,True,True,False,True,True,True,False,False,True,True,True,True,False],[False,False,True,True,True,False,True,False,True,True,True,False,True,False,True],[False,False,False,False,True,False,True,False,True,True,True,False,True,False,True],[True,False,True,False,True,True,False,True,True,True,False,False,True,False,False]],[[False,False,False,False,False,True,False,False,False,False,True,True,False,False,True],[False,True,True,True,True,True,False,True,False,False,False,False,False,True,False],[True,False,True,True,False,True,True,True,True,True,True,True,False,True,True],[True,True,True,False,True,False,True,True,False,True,True,False,False,False,False],[False,True,False,True,False,False,True,True,True,False,False,False,True,False,False],[True,True,True,False,False,False,False,True,False,False,True,True,True,True,True],[True,True,False,True,True,True,True,False,False,True,False,True,True,False,True],[True,True,True,True,True,True,True,True,False,True,False,True,True,True,False]],[[False,False,False,True,True,True,False,False,True,False,True,True,True,True,True],[True,False,False,False,True,True,True,True,True,True,False,True,True,True,False],[True,False,False,True,True,True,False,True,True,True,True,True,True,True,False],[False,False,False,True,False,False,False,True,True,True,False,True,False,True,True],[False,True,True,False,False,False,True,True,True,True,False,False,False,True,True],[False,False,True,False,True,True,False,True,False,True,True,True,True,True,False],[False,False,True,True,False,False,True,False,True,False,True,True,False,True,True],[False,True,True,True,True,False,True,False,True,True,True,False,False,False,False]],[[True,False,False,False,True,False,False,False,False,True,False,True,True,True,False],[False,True,True,True,False,True,True,True,True,False,True,False,True,True,True],[True,False,True,True,True,True,True,True,True,False,True,False,True,False,True],[False,False,False,True,True,False,False,False,False,True,False,True,False,True,False],[True,False,True,False,True,False,True,True,True,True,True,False,True,False,False],[False,False,False,False,False,True,False,False,True,False,False,False,True,False,True],[False,True,False,True,True,True,True,True,False,False,False,True,True,True,False],[True,True,False,False,True,False,True,True,True,True,False,True,True,True,True]],[[False,True,False,False,False,True,False,True,False,False,False,False,False,True,True],[False,False,False,False,False,True,True,False,True,False,True,True,True,False,False],[False,False,False,False,True,False,True,True,False,False,True,False,False,True,True],[False,True,True,False,False,False,False,True,False,True,True,True,False,False,True],[False,False,True,False,False,False,True,True,True,True,True,True,True,False,False],[False,False,False,True,False,False,True,False,True,True,True,False,False,True,False],[True,False,False,True,False,False,True,True,True,True,False,True,False,True,True],[False,True,True,False,True,True,False,False,False,True,False,True,True,False,True]],[[True,False,True,True,True,True,True,False,True,True,True,True,False,True,True],[True,False,False,False,False,True,True,True,False,True,False,False,True,False,False],[False,True,False,True,True,True,False,False,False,True,True,True,True,True,True],[False,False,True,False,False,True,False,False,False,False,True,True,False,False,True],[False,False,False,True,True,True,False,False,False,False,True,True,False,False,True],[True,False,True,False,True,False,True,True,False,False,True,True,True,True,False],[False,True,False,False,False,False,False,True,False,False,True,True,True,True,False],[False,False,False,False,False,True,False,False,False,False,False,True,True,True,False]],[[True,True,False,False,True,False,False,True,True,False,True,True,True,True,False],[True,True,True,False,True,True,True,True,True,False,True,True,True,True,False],[False,False,True,False,False,True,False,False,False,False,False,False,True,False,True],[True,True,False,False,True,False,False,True,True,True,True,True,True,False,False],[True,False,False,True,False,True,False,True,True,False,True,False,False,False,False],[True,True,True,False,False,True,False,False,False,True,True,True,False,False,True],[False,False,False,True,True,False,False,True,True,True,True,False,True,False,False],[True,True,False,True,True,False,False,True,False,False,True,True,True,True,False]],[[False,False,False,False,True,True,True,True,False,False,False,True,True,False,True],[True,True,True,True,False,False,True,False,False,True,False,True,True,True,False],[True,False,False,True,False,True,False,True,False,False,False,True,True,True,True],[True,False,False,False,False,True,False,True,True,False,True,False,True,False,True],[False,True,True,False,False,False,False,False,True,False,False,True,True,True,False],[False,False,True,True,False,True,False,True,False,True,True,True,True,True,True],[True,True,False,False,True,False,False,True,False,False,False,False,True,True,False],[False,False,False,True,True,True,False,True,False,False,False,True,False,False,False]],[[True,True,True,False,True,True,False,False,False,True,False,False,True,True,False],[True,True,False,False,False,True,True,False,False,True,True,False,False,True,False],[True,False,True,False,False,True,True,True,True,False,False,True,False,True,False],[False,True,False,False,True,False,True,False,True,True,True,False,False,True,True],[False,False,True,False,True,False,True,False,True,False,False,True,True,True,False],[True,True,True,True,False,False,False,True,False,True,True,True,True,True,True],[False,True,True,True,True,False,True,False,True,False,False,True,True,True,False],[False,True,False,True,False,False,False,False,True,False,True,False,False,False,True]],[[True,False,True,False,False,False,True,True,True,False,False,True,True,True,True],[False,True,False,False,True,False,False,True,True,True,True,False,False,True,True],[True,False,True,False,True,True,True,False,True,False,False,True,True,True,False],[False,True,False,False,True,True,True,True,False,False,True,True,False,True,True],[True,False,True,True,True,False,False,False,False,True,False,False,False,True,False],[True,False,True,True,False,True,False,True,False,False,True,True,True,False,False],[False,True,True,False,False,False,False,True,False,True,False,False,True,True,True],[True,False,True,True,True,False,False,True,True,False,True,True,False,False,True]],[[False,True,False,True,True,True,True,True,False,True,False,False,True,False,True],[True,True,True,False,False,False,False,False,True,False,True,False,True,True,True],[False,True,False,False,True,True,True,False,False,True,False,True,False,True,True],[True,False,False,True,True,True,True,True,True,True,True,False,True,False,True],[False,False,True,False,True,False,True,False,False,False,False,False,True,False,False],[False,True,False,False,False,True,True,False,True,True,True,False,True,False,True],[True,True,True,False,True,False,False,True,True,False,True,True,True,False,True],[True,False,False,True,False,True,True,False,True,False,True,False,False,False,False]],[[True,True,True,True,True,True,True,True,False,False,False,True,True,True,True],[False,False,True,True,True,True,False,False,True,True,False,False,True,True,True],[True,False,False,True,True,False,False,True,True,False,True,True,True,True,False],[False,True,False,True,False,False,False,False,False,False,True,True,False,False,False],[True,False,False,False,True,False,False,True,True,True,True,False,True,False,True],[True,False,True,False,True,True,False,True,False,False,True,True,True,False,False],[True,True,False,False,True,True,False,True,False,True,True,True,True,False,True],[True,True,True,False,True,False,True,True,True,True,False,True,True,True,True]],[[True,True,False,True,True,False,False,True,True,False,False,False,True,True,False],[False,False,False,True,False,True,True,False,True,False,True,True,True,False,False],[False,True,True,True,False,False,True,False,True,False,False,True,True,True,True],[True,True,True,True,False,False,True,True,False,False,False,True,True,True,False],[True,False,True,True,True,False,True,False,False,True,False,True,False,True,False],[True,True,False,True,False,False,True,True,False,True,True,False,False,False,True],[False,False,True,False,True,False,False,False,False,False,True,True,True,False,False],[False,True,True,False,False,False,False,True,True,False,False,True,False,True,True]],[[False,True,True,True,True,False,False,True,True,False,False,False,True,True,False],[False,True,False,True,True,False,True,False,False,True,False,False,False,True,True],[True,True,True,True,False,False,True,False,False,False,True,False,True,False,True],[True,False,True,True,False,False,False,True,False,False,False,True,False,False,False],[False,False,True,True,True,True,True,False,False,True,True,True,True,False,True],[True,True,False,False,True,False,False,True,True,True,True,False,False,True,False],[False,True,False,True,False,True,False,False,False,False,True,True,True,True,True],[True,False,False,True,False,True,True,False,False,False,True,True,False,True,True]]], dtype = "bool")#candidate|2514|(14, 8, 15)|const|bool
bop_2515 = relay.left_shift(bop_2496.astype('uint16'), relay.reshape(const_2514.astype('uint16'), relay.shape_of(bop_2496))) # shape=(14, 8, 15)
func_124_call = mod.get_global_var('func_124')
func_127_call = mutated_mod.get_global_var('func_127')
call_2520 = func_124_call(relay.reshape(call_2481.astype('float64'), [2, 15, 5]))
call_2521 = func_124_call(relay.reshape(call_2481.astype('float64'), [2, 15, 5]))
uop_2541 = relay.sqrt(bop_2458.astype('float32')) # shape=(14, 8, 15)
output = relay.Tuple([call_2453,const_2454,call_2472,var_2473,const_2474,call_2481,var_2482,const_2483,call_2488,call_2490,call_2499,var_2500,bop_2515,call_2520,uop_2541,])
output2 = relay.Tuple([call_2455,const_2454,call_2475,var_2473,const_2474,call_2484,var_2482,const_2483,call_2489,call_2491,call_2501,var_2500,bop_2515,call_2521,uop_2541,])
func_2543 = relay.Function([var_2445,var_2473,var_2482,var_2495,var_2500,], output)
mod['func_2543'] = func_2543
mod = relay.transform.InferType()(mod)
mutated_mod['func_2543'] = func_2543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mutated_mod.get_global_var('func_2543')
var_2545 = relay.var("var_2545", dtype = "float64", shape = (14, 8, 15))#candidate|2545|(14, 8, 15)|var|float64
var_2546 = relay.var("var_2546", dtype = "uint32", shape = (2, 120))#candidate|2546|(2, 120)|var|uint32
var_2547 = relay.var("var_2547", dtype = "float64", shape = (150,))#candidate|2547|(150,)|var|float64
var_2548 = relay.var("var_2548", dtype = "float64", shape = (14, 8, 15))#candidate|2548|(14, 8, 15)|var|float64
var_2549 = relay.var("var_2549", dtype = "uint8", shape = (288,))#candidate|2549|(288,)|var|uint8
call_2544 = func_2543_call(var_2545,var_2546,var_2547,var_2548,var_2549,)
output = call_2544
func_2550 = relay.Function([var_2545,var_2546,var_2547,var_2548,var_2549,], output)
mutated_mod['func_2550'] = func_2550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1756_call = mod.get_global_var('func_1756')
func_1757_call = mutated_mod.get_global_var('func_1757')
call_2580 = func_1756_call()
call_2581 = func_1756_call()
func_1863_call = mod.get_global_var('func_1863')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_2594 = func_1863_call()
call_2595 = func_1863_call()
var_2610 = relay.var("var_2610", dtype = "float64", shape = (3, 11, 16))#candidate|2610|(3, 11, 16)|var|float64
bop_2611 = relay.logical_or(call_2580.astype('bool'), relay.reshape(var_2610.astype('bool'), relay.shape_of(call_2580))) # shape=(3, 11, 16)
bop_2614 = relay.logical_or(call_2581.astype('bool'), relay.reshape(var_2610.astype('bool'), relay.shape_of(call_2581))) # shape=(3, 11, 16)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_2617 = relay.TupleGetItem(func_2072_call(), 2)
call_2618 = relay.TupleGetItem(func_2074_call(), 2)
func_201_call = mod.get_global_var('func_201')
func_204_call = mutated_mod.get_global_var('func_204')
var_2629 = relay.var("var_2629", dtype = "uint8", shape = (88,))#candidate|2629|(88,)|var|uint8
call_2628 = relay.TupleGetItem(func_201_call(relay.reshape(var_2629.astype('uint8'), [11, 1, 8]), relay.reshape(var_2629.astype('uint8'), [11, 1, 8]), ), 1)
call_2630 = relay.TupleGetItem(func_204_call(relay.reshape(var_2629.astype('uint8'), [11, 1, 8]), relay.reshape(var_2629.astype('uint8'), [11, 1, 8]), ), 1)
func_201_call = mod.get_global_var('func_201')
func_204_call = mutated_mod.get_global_var('func_204')
call_2635 = relay.TupleGetItem(func_201_call(relay.reshape(var_2629.astype('uint8'), [11, 1, 8]), relay.reshape(call_2628.astype('uint8'), [11, 1, 8]), ), 1)
call_2636 = relay.TupleGetItem(func_204_call(relay.reshape(var_2629.astype('uint8'), [11, 1, 8]), relay.reshape(call_2628.astype('uint8'), [11, 1, 8]), ), 1)
func_1191_call = mod.get_global_var('func_1191')
func_1195_call = mutated_mod.get_global_var('func_1195')
var_2649 = relay.var("var_2649", dtype = "uint8", shape = (280,))#candidate|2649|(280,)|var|uint8
call_2648 = relay.TupleGetItem(func_1191_call(relay.reshape(var_2649.astype('uint8'), [10, 14, 2]), relay.reshape(var_2649.astype('uint8'), [10, 14, 2]), ), 1)
call_2650 = relay.TupleGetItem(func_1195_call(relay.reshape(var_2649.astype('uint8'), [10, 14, 2]), relay.reshape(var_2649.astype('uint8'), [10, 14, 2]), ), 1)
bop_2652 = relay.add(call_2635.astype('int8'), relay.reshape(call_2628.astype('int8'), relay.shape_of(call_2635))) # shape=(11, 1, 8)
bop_2655 = relay.add(call_2636.astype('int8'), relay.reshape(call_2630.astype('int8'), relay.shape_of(call_2636))) # shape=(11, 1, 8)
func_1863_call = mod.get_global_var('func_1863')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_2668 = func_1863_call()
call_2669 = func_1863_call()
uop_2674 = relay.atanh(call_2635.astype('float64')) # shape=(11, 1, 8)
uop_2676 = relay.atanh(call_2636.astype('float64')) # shape=(11, 1, 8)
func_2367_call = mod.get_global_var('func_2367')
func_2370_call = mutated_mod.get_global_var('func_2370')
call_2677 = relay.TupleGetItem(func_2367_call(relay.reshape(call_2617.astype('float64'), [150,]), relay.reshape(var_2610.astype('float64'), [3, 11, 16]), ), 3)
call_2678 = relay.TupleGetItem(func_2370_call(relay.reshape(call_2617.astype('float64'), [150,]), relay.reshape(var_2610.astype('float64'), [3, 11, 16]), ), 3)
output = relay.Tuple([call_2594,bop_2611,call_2617,var_2629,call_2648,var_2649,bop_2652,call_2668,uop_2674,call_2677,])
output2 = relay.Tuple([call_2595,bop_2614,call_2618,var_2629,call_2650,var_2649,bop_2655,call_2669,uop_2676,call_2678,])
func_2680 = relay.Function([var_2610,var_2629,var_2649,], output)
mod['func_2680'] = func_2680
mod = relay.transform.InferType()(mod)
mutated_mod['func_2680'] = func_2680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2680_call = mutated_mod.get_global_var('func_2680')
var_2682 = relay.var("var_2682", dtype = "float64", shape = (3, 11, 16))#candidate|2682|(3, 11, 16)|var|float64
var_2683 = relay.var("var_2683", dtype = "uint8", shape = (88,))#candidate|2683|(88,)|var|uint8
var_2684 = relay.var("var_2684", dtype = "uint8", shape = (280,))#candidate|2684|(280,)|var|uint8
call_2681 = func_2680_call(var_2682,var_2683,var_2684,)
output = call_2681
func_2685 = relay.Function([var_2682,var_2683,var_2684,], output)
mutated_mod['func_2685'] = func_2685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2107_call = mod.get_global_var('func_2107')
func_2109_call = mutated_mod.get_global_var('func_2109')
call_2717 = relay.TupleGetItem(func_2107_call(), 0)
call_2718 = relay.TupleGetItem(func_2109_call(), 0)
var_2753 = relay.var("var_2753", dtype = "float32", shape = (9, 16, 7))#candidate|2753|(9, 16, 7)|var|float32
bop_2754 = relay.less(call_2717.astype('bool'), var_2753.astype('bool')) # shape=(9, 16, 7)
bop_2757 = relay.less(call_2718.astype('bool'), var_2753.astype('bool')) # shape=(9, 16, 7)
uop_2779 = relay.sigmoid(call_2717.astype('float32')) # shape=(1, 16, 7)
uop_2781 = relay.sigmoid(call_2718.astype('float32')) # shape=(1, 16, 7)
var_2788 = relay.var("var_2788", dtype = "float32", shape = (4, 16, 7))#candidate|2788|(4, 16, 7)|var|float32
bop_2789 = relay.divide(uop_2779.astype('float32'), var_2788.astype('float32')) # shape=(4, 16, 7)
bop_2792 = relay.divide(uop_2781.astype('float32'), var_2788.astype('float32')) # shape=(4, 16, 7)
output = relay.Tuple([bop_2754,bop_2789,])
output2 = relay.Tuple([bop_2757,bop_2792,])
func_2797 = relay.Function([var_2753,var_2788,], output)
mod['func_2797'] = func_2797
mod = relay.transform.InferType()(mod)
mutated_mod['func_2797'] = func_2797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2797_call = mutated_mod.get_global_var('func_2797')
var_2799 = relay.var("var_2799", dtype = "float32", shape = (9, 16, 7))#candidate|2799|(9, 16, 7)|var|float32
var_2800 = relay.var("var_2800", dtype = "float32", shape = (4, 16, 7))#candidate|2800|(4, 16, 7)|var|float32
call_2798 = func_2797_call(var_2799,var_2800,)
output = call_2798
func_2801 = relay.Function([var_2799,var_2800,], output)
mutated_mod['func_2801'] = func_2801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2286_call = mod.get_global_var('func_2286')
func_2287_call = mutated_mod.get_global_var('func_2287')
call_2819 = relay.TupleGetItem(func_2286_call(), 0)
call_2820 = relay.TupleGetItem(func_2287_call(), 0)
func_2680_call = mod.get_global_var('func_2680')
func_2685_call = mutated_mod.get_global_var('func_2685')
var_2824 = relay.var("var_2824", dtype = "float64", shape = (24, 22))#candidate|2824|(24, 22)|var|float64
var_2825 = relay.var("var_2825", dtype = "uint8", shape = (88,))#candidate|2825|(88,)|var|uint8
const_2826 = relay.const([5,5,10,6,7,-6,-9,-5,-1,-10,-9,-4,-3,-4,-8,-3,9,-8,-3,-10,4,9,8,-8,4,-7,6,-3,-2,8,-3,3,-8,5,-5,6,-5,-5,-8,4,-10,-6,-2,5,-5,6,-5,4,-9,-9,-5,6,-7,-3,-3,-10,7,9,-6,-5,-1,-2,9,-2,-4,5,-3,9,1,8,8,8,3,-5,6,-9,-9,1,-7,-8,-3,2,3,7,-3,1,2,-5,9,-3,7,1,-3,6,7,-2,-9,8,6,-10,-10,-8,-10,-7,-2,3,-2,-7,-7,8,-9,6,-5,-1,-2,1,10,6,2,-9,4,6,-6,-3,-6,-1,-1,4,-1,-10,4,5,-9,-3,4,7,-6,4,-6,9,7,-8,6,6,-6,10,-6,-5,-8,7,-2,10,9,-2,-8,-8,10,5,9,3,8,5,-2,8,-1,-2,3,-3,-3,-9,5,-7,-5,-10,4,10,-9,-5,-7,1,-1,-3,4,-7,10,-9,5,-9,-8,5,-4,-3,3,-6,-2,8,-1,-8,-6,1,10,10,-5,6,-10,7,-9,7,-10,-2,-1,6,3,6,-6,7,6,-3,-6,6,3,10,-6,4,1,6,8,3,-5,-3,7,-9,7,5,3,1,-5,-8,9,6,-9,3,6,1,6,-2,-3,-5,-5,4,-4,-5,-8,-9,-6,9,9,5,10,7,-9,1,2,-10,8,8,-1,-10,-8,5,8,-3,6,4,-3,5,2,4,4,4], dtype = "uint8")#candidate|2826|(280,)|const|uint8
call_2823 = relay.TupleGetItem(func_2680_call(relay.reshape(var_2824.astype('float64'), [3, 11, 16]), relay.reshape(var_2825.astype('uint8'), [88,]), relay.reshape(const_2826.astype('uint8'), [280,]), ), 1)
call_2827 = relay.TupleGetItem(func_2685_call(relay.reshape(var_2824.astype('float64'), [3, 11, 16]), relay.reshape(var_2825.astype('uint8'), [88,]), relay.reshape(const_2826.astype('uint8'), [280,]), ), 1)
uop_2841 = relay.asin(call_2819.astype('float32')) # shape=(1, 16, 7)
uop_2843 = relay.asin(call_2820.astype('float32')) # shape=(1, 16, 7)
func_1569_call = mod.get_global_var('func_1569')
func_1574_call = mutated_mod.get_global_var('func_1574')
var_2852 = relay.var("var_2852", dtype = "uint32", shape = (40,))#candidate|2852|(40,)|var|uint32
var_2853 = relay.var("var_2853", dtype = "int16", shape = (3, 36))#candidate|2853|(3, 36)|var|int16
const_2854 = relay.const([-6,-6,-6,-9,-8,5,-5,-7,8,5,-6,-8,9,-5,8,-4,7,-1,-2,1,-5,3,1,-6,-1,-7,-3,4,-6,-3,-7,7,6,8,10,-1,-6,-4,-6,7,1,-6,1,-8,-9,9,7,-1,-6,2,6,9,-8,10,5,-1,1,3,-5,9,2,-1,6,4,9,-7,9,-9,-1,1,8,4,-9,-3,10,10,2,10,1,1,10,-7,4,-6,-6,-2,-10,4,-5,-6,9,-6,-7,-10,-10,10,-8,9,-6,-8,-5,-7,-9,4,9,9,-6,-10,1,1,10,-1,2,-2,-8,-1,3,8,2,-5,2,9,-1,10,1,-5,-5,-3,10,-5,6,-9,-5,-8,-9,-8,-1,8,7,5,-9,3,9,-1,9,-7,-2,-1,-5,4,6,-4,8,-8,-2,-5,3,7,3,-1,3,-7,-6,4,9,-5,9,-9,-5,-3,10,-10,-5,-5,4,-1,5,6,6,3,7,8,9,-4,-6,1,-5,7,7,-10,-7,10,7,-3,5,8,-4,-7,-6,9,-7,8,-3,-4,6,-3,-3,4,10,-4,-3,-6,-1,-2,-5,-8,5,-4,10,1,10,-8,-9,-4,10,-4,2,-10,3,9,6,10,-3,2,-4,9,10,-6,2,8,10,6,1,3,9,2,9,-9,-8,-8,-5,-6,-8,4,6,3,5,8,-3,-2,2,10,-7,6,9,10,2,-10,10,-10,7,2,1,10,10,-8,7,6,8,-1,-7,-2,-9,-9,8,7,1,1,-9,5,2,-4,3,3,3,10,-7,8,7,-6,7,2,5,9,4,-5,-9,-7,8,-6,6,-2,-10,-8,10,-4,1,2,-9,10,-4,2,-2,8,9,-3,-3,7,-5,-2,10,1,-2,-7,-5,6,2,5,-9,5,8,-2,-5,4,-3,-7,2,6,1,7,-10,5,5,5,-2,1,-10,-3,-9,7,3,4,-9,1,4,8,-5,6,-3,-3,3,7,4,-10,-6,4,10,7,10,1,-8,-8,2,-2,-4,9,8,3,-7,4,10,5,7,1,-1,-1,-1,-1,-2,-7,-9,-6,-4,8,3,-5,1,-5,1,4,-8,1,4,2,7,2,8,1,-8,1,3,8,-3,10,1,-8,-9,-10,-10,-8,-4,1,8,-1,-2,-2,8,9,-5,7,-3,6,-1,6,1,-8,-4,-8,-10,-3,-3,9,6,-3,7,8,-5,3,-3,9,4,-2,4,-3,8,1,2,3,6,-9,-7,4,-3,2,-7,-1,-8,-9,2,-9,9,-4,-9,-9,6,-9,-6,7,-9,7,-9,7,3,2,-2,-6,10,-2,-8,6,-8,8,-8,-7,-5,-3,5,4,7,-3,-6,10,10,6,2,3,7,-5,-8,1,7,10,3,-9,-9,-1,-3,2,4,5,-2,-5,-2,3,3,5,-8,-3,8,-3,-6,1,-7,5,1,-7,-10,1,5,2,-9,-9,2,10,-5,7,9,-3,1,10,-9,4,-9,1,-10,-1,2,4,3,-3,8,2,-10,-4,4,-2,10,2,2,3,-8,8,6,5,-7,2,10,3,-8,10,2,6,-9,-1,-2,10,-1,-2,-4,8], dtype = "uint32")#candidate|2854|(600,)|const|uint32
call_2851 = relay.TupleGetItem(func_1569_call(relay.reshape(var_2852.astype('uint32'), [10, 1, 4]), relay.reshape(var_2853.astype('int16'), [108,]), relay.reshape(const_2854.astype('uint32'), [10, 15, 4]), ), 2)
call_2855 = relay.TupleGetItem(func_1574_call(relay.reshape(var_2852.astype('uint32'), [10, 1, 4]), relay.reshape(var_2853.astype('int16'), [108,]), relay.reshape(const_2854.astype('uint32'), [10, 15, 4]), ), 2)
output = relay.Tuple([call_2823,var_2824,var_2825,const_2826,uop_2841,call_2851,var_2852,var_2853,const_2854,])
output2 = relay.Tuple([call_2827,var_2824,var_2825,const_2826,uop_2843,call_2855,var_2852,var_2853,const_2854,])
func_2856 = relay.Function([var_2824,var_2825,var_2852,var_2853,], output)
mod['func_2856'] = func_2856
mod = relay.transform.InferType()(mod)
mutated_mod['func_2856'] = func_2856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2856_call = mutated_mod.get_global_var('func_2856')
var_2858 = relay.var("var_2858", dtype = "float64", shape = (24, 22))#candidate|2858|(24, 22)|var|float64
var_2859 = relay.var("var_2859", dtype = "uint8", shape = (88,))#candidate|2859|(88,)|var|uint8
var_2860 = relay.var("var_2860", dtype = "uint32", shape = (40,))#candidate|2860|(40,)|var|uint32
var_2861 = relay.var("var_2861", dtype = "int16", shape = (3, 36))#candidate|2861|(3, 36)|var|int16
call_2857 = func_2856_call(var_2858,var_2859,var_2860,var_2861,)
output = call_2857
func_2862 = relay.Function([var_2858,var_2859,var_2860,var_2861,], output)
mutated_mod['func_2862'] = func_2862
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2884 = relay.var("var_2884", dtype = "int32", shape = (9, 16, 13))#candidate|2884|(9, 16, 13)|var|int32
var_2885 = relay.var("var_2885", dtype = "int32", shape = (9, 16, 13))#candidate|2885|(9, 16, 13)|var|int32
bop_2886 = relay.bitwise_or(var_2884.astype('int32'), relay.reshape(var_2885.astype('int32'), relay.shape_of(var_2884))) # shape=(9, 16, 13)
func_691_call = mod.get_global_var('func_691')
func_694_call = mutated_mod.get_global_var('func_694')
var_2891 = relay.var("var_2891", dtype = "float32", shape = (14,))#candidate|2891|(14,)|var|float32
call_2890 = relay.TupleGetItem(func_691_call(relay.reshape(var_2891.astype('float32'), [1, 1, 14])), 2)
call_2892 = relay.TupleGetItem(func_694_call(relay.reshape(var_2891.astype('float32'), [1, 1, 14])), 2)
uop_2904 = relay.rsqrt(var_2884.astype('float64')) # shape=(9, 16, 13)
output = relay.Tuple([bop_2886,call_2890,var_2891,uop_2904,])
output2 = relay.Tuple([bop_2886,call_2892,var_2891,uop_2904,])
func_2913 = relay.Function([var_2884,var_2885,var_2891,], output)
mod['func_2913'] = func_2913
mod = relay.transform.InferType()(mod)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2913_call = mutated_mod.get_global_var('func_2913')
var_2915 = relay.var("var_2915", dtype = "int32", shape = (9, 16, 13))#candidate|2915|(9, 16, 13)|var|int32
var_2916 = relay.var("var_2916", dtype = "int32", shape = (9, 16, 13))#candidate|2916|(9, 16, 13)|var|int32
var_2917 = relay.var("var_2917", dtype = "float32", shape = (14,))#candidate|2917|(14,)|var|float32
call_2914 = func_2913_call(var_2915,var_2916,var_2917,)
output = call_2914
func_2918 = relay.Function([var_2915,var_2916,var_2917,], output)
mutated_mod['func_2918'] = func_2918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2286_call = mod.get_global_var('func_2286')
func_2287_call = mutated_mod.get_global_var('func_2287')
call_2954 = relay.TupleGetItem(func_2286_call(), 1)
call_2955 = relay.TupleGetItem(func_2287_call(), 1)
const_2958 = relay.const([[[4,4,3,10],[2,7,3,-7],[-6,7,6,-5],[-9,7,-9,-6],[3,2,-1,-3],[2,-10,9,5]],[[4,-5,5,1],[-7,6,3,10],[-1,9,9,-4],[-2,-5,4,6],[3,8,3,1],[-6,-7,10,-5]],[[2,-2,-8,1],[1,-10,-7,2],[-8,-7,10,1],[5,-6,-7,-6],[5,-9,6,-2],[7,1,8,3]],[[6,9,6,-3],[-9,-7,-8,-5],[-5,-5,-6,8],[-10,-7,-4,8],[-8,5,6,8],[5,-2,-10,-7]],[[5,6,2,5],[2,-2,-4,-6],[7,8,-9,9],[-2,8,-1,-7],[-8,8,-6,2],[6,-4,-6,3]]], dtype = "int32")#candidate|2958|(5, 6, 4)|const|int32
bop_2959 = relay.right_shift(call_2954.astype('int32'), const_2958.astype('int32')) # shape=(5, 6, 4)
bop_2962 = relay.right_shift(call_2955.astype('int32'), const_2958.astype('int32')) # shape=(5, 6, 4)
var_2976 = relay.var("var_2976", dtype = "int32", shape = (6, 2, 4))#candidate|2976|(6, 2, 4)|var|int32
bop_2977 = relay.subtract(call_2954.astype('int64'), var_2976.astype('int64')) # shape=(6, 2, 4)
bop_2980 = relay.subtract(call_2955.astype('int64'), var_2976.astype('int64')) # shape=(6, 2, 4)
output = relay.Tuple([bop_2959,bop_2977,])
output2 = relay.Tuple([bop_2962,bop_2980,])
func_2998 = relay.Function([var_2976,], output)
mod['func_2998'] = func_2998
mod = relay.transform.InferType()(mod)
mutated_mod['func_2998'] = func_2998
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2999 = relay.var("var_2999", dtype = "int32", shape = (6, 2, 4))#candidate|2999|(6, 2, 4)|var|int32
func_2998_call = mutated_mod.get_global_var('func_2998')
call_3000 = func_2998_call(var_2999)
output = call_3000
func_3001 = relay.Function([var_2999], output)
mutated_mod['func_3001'] = func_3001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1605_call = mod.get_global_var('func_1605')
func_1606_call = mutated_mod.get_global_var('func_1606')
call_3007 = relay.TupleGetItem(func_1605_call(), 0)
call_3008 = relay.TupleGetItem(func_1606_call(), 0)
uop_3009 = relay.exp(call_3007.astype('float64')) # shape=(1, 16, 7)
uop_3011 = relay.exp(call_3008.astype('float64')) # shape=(1, 16, 7)
bop_3013 = relay.floor_mod(call_3007.astype('float32'), relay.reshape(uop_3009.astype('float32'), relay.shape_of(call_3007))) # shape=(1, 16, 7)
bop_3016 = relay.floor_mod(call_3008.astype('float32'), relay.reshape(uop_3011.astype('float32'), relay.shape_of(call_3008))) # shape=(1, 16, 7)
bop_3023 = relay.bitwise_xor(bop_3013.astype('uint16'), relay.reshape(uop_3009.astype('uint16'), relay.shape_of(bop_3013))) # shape=(1, 16, 7)
bop_3026 = relay.bitwise_xor(bop_3016.astype('uint16'), relay.reshape(uop_3011.astype('uint16'), relay.shape_of(bop_3016))) # shape=(1, 16, 7)
bop_3033 = relay.logical_or(uop_3009.astype('bool'), relay.reshape(call_3007.astype('bool'), relay.shape_of(uop_3009))) # shape=(1, 16, 7)
bop_3036 = relay.logical_or(uop_3011.astype('bool'), relay.reshape(call_3008.astype('bool'), relay.shape_of(uop_3011))) # shape=(1, 16, 7)
uop_3041 = relay.log10(call_3007.astype('float64')) # shape=(1, 16, 7)
uop_3043 = relay.log10(call_3008.astype('float64')) # shape=(1, 16, 7)
output = relay.Tuple([bop_3023,bop_3033,uop_3041,])
output2 = relay.Tuple([bop_3026,bop_3036,uop_3043,])
func_3057 = relay.Function([], output)
mod['func_3057'] = func_3057
mod = relay.transform.InferType()(mod)
output = func_3057()
func_3058 = relay.Function([], output)
mutated_mod['func_3058'] = func_3058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mod.get_global_var('func_1863')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_3105 = func_1863_call()
call_3106 = func_1863_call()
output = relay.Tuple([call_3105,])
output2 = relay.Tuple([call_3106,])
func_3112 = relay.Function([], output)
mod['func_3112'] = func_3112
mod = relay.transform.InferType()(mod)
mutated_mod['func_3112'] = func_3112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3112_call = mutated_mod.get_global_var('func_3112')
call_3113 = func_3112_call()
output = call_3113
func_3114 = relay.Function([], output)
mutated_mod['func_3114'] = func_3114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2286_call = mod.get_global_var('func_2286')
func_2287_call = mutated_mod.get_global_var('func_2287')
call_3123 = relay.TupleGetItem(func_2286_call(), 3)
call_3124 = relay.TupleGetItem(func_2287_call(), 3)
func_3057_call = mod.get_global_var('func_3057')
func_3058_call = mutated_mod.get_global_var('func_3058')
call_3140 = relay.TupleGetItem(func_3057_call(), 2)
call_3141 = relay.TupleGetItem(func_3058_call(), 2)
func_1593_call = mod.get_global_var('func_1593')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_3148 = func_1593_call()
call_3149 = func_1593_call()
uop_3153 = relay.tan(call_3148.astype('float64')) # shape=(1, 16, 7)
uop_3155 = relay.tan(call_3149.astype('float64')) # shape=(1, 16, 7)
func_2394_call = mod.get_global_var('func_2394')
func_2396_call = mutated_mod.get_global_var('func_2396')
call_3159 = relay.TupleGetItem(func_2394_call(), 1)
call_3160 = relay.TupleGetItem(func_2396_call(), 1)
output = relay.Tuple([call_3123,call_3140,uop_3153,call_3159,])
output2 = relay.Tuple([call_3124,call_3141,uop_3155,call_3160,])
func_3167 = relay.Function([], output)
mod['func_3167'] = func_3167
mod = relay.transform.InferType()(mod)
output = func_3167()
func_3168 = relay.Function([], output)
mutated_mod['func_3168'] = func_3168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2286_call = mod.get_global_var('func_2286')
func_2287_call = mutated_mod.get_global_var('func_2287')
call_3182 = relay.TupleGetItem(func_2286_call(), 1)
call_3183 = relay.TupleGetItem(func_2287_call(), 1)
var_3185 = relay.var("var_3185", dtype = "int32", shape = (6, 3, 4))#candidate|3185|(6, 3, 4)|var|int32
bop_3186 = relay.greater(call_3182.astype('bool'), var_3185.astype('bool')) # shape=(6, 3, 4)
bop_3189 = relay.greater(call_3183.astype('bool'), var_3185.astype('bool')) # shape=(6, 3, 4)
func_124_call = mod.get_global_var('func_124')
func_127_call = mutated_mod.get_global_var('func_127')
const_3198 = relay.const([-6.898746,-1.736911,-1.577463,1.799805,-6.390619,3.742809,1.744224,2.499986,-2.087908,-9.052893,7.274378,-1.728683,-4.010862,-0.707054,-1.627336,7.795094,-8.882342,7.452072,1.978643,-6.958451,-1.028804,7.768976,5.637851,3.007549,-4.087356,7.664075,1.727592,1.664911,0.539059,7.331599,7.927760,-5.390053,-4.804575,0.183477,-2.001890,-1.336174,3.654050,-5.092713,-3.732584,4.247034,7.136406,-5.730699,-6.926248,3.074262,6.198967,0.437948,1.336685,9.980658,6.684554,6.857403,-2.374313,-8.550326,-1.081327,-2.942144,6.627361,7.262022,-7.275915,5.539622,8.000332,-5.085041,3.394545,-8.329630,4.814726,5.262186,-0.750814,-7.759339,-2.603323,-7.677450,-7.758147,7.509944,-1.396320,-9.657268,6.353907,3.361372,-9.133924,6.281620,-9.726653,-5.721800,4.287506,-9.586125,3.547869,-1.219579,-5.167101,-7.911444,-9.207819,-6.236837,-6.697354,0.709212,-2.082531,8.069181,6.001648,-6.477753,-7.945087,1.121654,-1.507291,0.710187,9.632756,7.577754,-5.290457,-2.151975,-9.046349,-5.600337,3.016443,-7.551767,-3.605888,7.020869,-2.630849,9.275654,-7.045218,8.159134,9.384441,-7.209281,-3.551844,-3.901519,3.590912,4.546687,4.843342,4.615464,-7.284284,-8.480054,1.693039,-2.804426,4.115041,-7.203827,-7.079402,7.909418,-1.879620,-0.738079,0.091567,7.024746,1.645286,-5.317767,-5.064511,-0.519961,5.268751,-7.785450,-2.817339,1.302571,-8.345753,9.049226,9.656609,-6.867944,6.539041,-6.787524,9.701813,1.668578,3.498631,2.343074,9.788843,-8.628382], dtype = "float64")#candidate|3198|(150,)|const|float64
call_3197 = func_124_call(relay.reshape(const_3198.astype('float64'), [2, 15, 5]))
call_3199 = func_124_call(relay.reshape(const_3198.astype('float64'), [2, 15, 5]))
output = relay.Tuple([bop_3186,call_3197,const_3198,])
output2 = relay.Tuple([bop_3189,call_3199,const_3198,])
func_3207 = relay.Function([var_3185,], output)
mod['func_3207'] = func_3207
mod = relay.transform.InferType()(mod)
mutated_mod['func_3207'] = func_3207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3208 = relay.var("var_3208", dtype = "int32", shape = (6, 3, 4))#candidate|3208|(6, 3, 4)|var|int32
func_3207_call = mutated_mod.get_global_var('func_3207')
call_3209 = func_3207_call(var_3208)
output = call_3209
func_3210 = relay.Function([var_3208], output)
mutated_mod['func_3210'] = func_3210
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3212 = relay.var("var_3212", dtype = "int32", shape = (10, 14, 10))#candidate|3212|(10, 14, 10)|var|int32
var_3213 = relay.var("var_3213", dtype = "int32", shape = (10, 14, 10))#candidate|3213|(10, 14, 10)|var|int32
bop_3214 = relay.add(var_3212.astype('int32'), relay.reshape(var_3213.astype('int32'), relay.shape_of(var_3212))) # shape=(10, 14, 10)
func_2856_call = mod.get_global_var('func_2856')
func_2862_call = mutated_mod.get_global_var('func_2862')
const_3219 = relay.const([1.025926,-0.137581,-5.998965,-0.062100,7.840060,-1.923790,-0.426864,-1.049016,-7.978042,-4.404668,2.525148,5.046320,8.673122,-0.588873,2.118015,-8.845588,1.126463,-4.482185,-5.796156,-8.674164,0.623984,-1.936461,-5.284208,-6.056183,7.659038,0.582529,2.370104,-2.035746,7.669845,5.676912,9.036931,-0.111339,7.791815,-4.925119,4.083654,7.753179,8.148846,-0.776584,-7.817805,0.716481,9.070539,-2.120180,0.500423,5.723269,-1.150337,0.850925,-0.117750,-7.112918,-8.521716,5.270332,-2.154854,0.232737,-4.648760,5.665939,-9.983875,-2.299117,5.068174,-2.226934,-7.563043,-6.100054,-6.535574,-2.319266,0.759909,-9.435163,-7.011106,3.642679,-4.668762,-0.233529,-8.650846,1.631143,-7.810359,-6.643311,1.186043,9.637969,-7.567880,-8.475588,8.832544,5.243108,5.229710,1.748876,7.055878,-6.835591,6.622064,6.701257,-2.844482,-6.208209,-3.520486,5.639930,6.552195,8.022748,-5.102271,-7.896130,6.184552,-3.211463,-3.927270,-3.896770,-1.808356,3.872107,3.006681,8.484441,-9.566024,4.065521,-1.175339,-6.126947,5.077752,2.396589,2.132808,1.682728,9.184467,5.784631,6.911313,7.952012,2.528958,4.290146,6.598743,-8.762379,-4.462162,0.003593,-2.973150,-5.413138,4.569203,3.510696,-2.901966,8.981583,-0.275942,6.677219,-2.970047,5.075289,1.399564,0.144019,0.765492,-6.077616,5.624430,-2.791973,8.856648,4.553799,-1.057675,8.065337,7.417973,-2.320145,-3.566992,-9.114850,8.904078,-5.801925,-1.821714,2.526090,7.872360,-9.667219,1.083404,5.371154,5.790914,-6.050437,5.617449,-3.615886,-0.202221,2.106559,-0.788826,-2.747333,1.076775,7.917976,-4.779122,-4.153765,-1.466103,-4.205939,4.646961,6.816141,-4.460085,9.863687,7.689948,-7.443058,-3.715299,-8.377735,5.782467,-4.270304,0.513354,6.955229,9.545405,-4.681800,-8.107220,8.514442,-5.078800,-2.579291,-3.617472,-9.066501,-1.323780,-6.333605,-3.317628,2.072255,7.452847,5.487603,1.050009,-0.656705,-5.916068,1.764616,4.225224,-5.169736,9.337856,-1.770714,-7.563287,7.756923,3.336941,-1.264003,9.573954,-8.790060,0.263398,3.590261,-6.185908,4.418477,-6.552137,8.685528,-5.593291,2.308539,-3.281498,8.634773,7.985757,3.261749,-0.903121,-4.308206,-9.649361,-6.828170,-6.397954,-0.462876,4.770777,3.561923,-6.682082,5.907351,7.902103,-6.837139,-8.551561,-4.159059,9.678968,7.111512,1.029022,0.084620,-1.323803,-4.469316,4.747014,2.706671,-4.288869,5.189279,1.198331,5.995210,3.101774,-0.706760,-9.063370,2.409963,7.561764,4.592773,5.215696,-3.357365,2.694212,-1.579981,2.589808,5.332114,2.614115,8.002508,-5.427668,7.295169,-5.300016,8.041369,-2.300761,-4.416917,2.562253,9.168814,-1.659834,-5.496517,-0.148270,6.822224,-6.816334,6.347829,7.693393,-0.932039,-2.963876,3.897374,-0.496796,6.044228,-6.793774,-2.027233,2.452110,-2.804741,5.850588,9.467651,8.537425,5.346915,-7.050662,8.894979,2.454720,0.267637,0.607603,3.654881,6.486468,0.707980,-1.117883,-2.495576,4.407983,-0.582686,3.891462,-6.111720,-5.487701,7.905462,-8.856469,-4.705521,-0.363341,4.015643,-4.193158,0.646873,6.474627,0.610568,-8.459956,-1.754745,-8.834179,-3.586137,-0.722587,7.722743,5.843437,3.254834,8.560396,5.724618,9.158759,-9.685278,4.960581,-0.123826,-6.607283,7.861236,8.004635,-0.960704,-4.043217,0.054637,7.154111,4.674616,7.597089,-5.626056,-5.689217,5.810812,9.483475,4.052144,7.090108,3.325645,-7.872888,8.109806,-7.484691,6.878362,-5.601765,-3.956701,5.487829,-9.852904,-9.871371,-4.228645,9.996073,7.710858,2.377897,5.652376,-1.664862,-4.899329,5.081752,-8.620022,0.769012,-6.413266,-0.615529,9.024813,-9.683235,9.746574,-9.377998,4.388643,1.896886,-1.618254,-4.546393,7.980955,5.915741,3.678415,8.597133,-0.360551,3.572648,6.374208,5.461650,-1.955609,-1.855114,2.807066,4.805610,-6.796585,0.867428,2.989130,1.873000,-6.958364,-2.546231,4.915944,0.183392,-0.361179,9.305363,-9.348388,-1.390602,-0.498045,-5.015545,9.827459,0.538268,-1.920307,6.074258,-9.989779,9.628580,1.203297,-4.152091,5.121147,-3.802447,-4.009472,7.423065,9.907270,8.954456,8.704874,8.854602,5.360233,-4.965706,5.554347,1.592654,-2.057993,-1.023973,-6.073425,2.267549,-8.978434,5.835913,4.780360,1.256459,-8.214857,-8.165471,0.197546,4.215925,-6.975402,-7.616589,6.944080,6.639741,-3.458915,1.418476,-4.021335,0.793313,-7.780922,-0.637738,1.359807,-6.137531,-6.745285,7.579598,-5.180463,4.255863,5.404674,-7.424358,2.973940,-5.933729,9.064416,7.798604,-8.824215,-2.760759,3.386951,-5.694405,9.194804,1.257311,-5.279179,1.701562,8.676934,8.755657,-0.769303,7.645316,-2.635586,-6.473455,8.692485,4.694080,-7.576977,-7.626308,-7.833006,-5.608461,-7.369846,-8.582932,0.511308,1.274756,-7.304925,5.893959,6.046665,-3.686802,-1.324481,5.580134,-0.852707,-6.147322,5.700088,7.362479,5.678437,4.969592,0.305010,-6.875649,3.096531,6.721602,6.500279,-6.111390,1.743890,-1.767972,6.618142,3.985076,-5.424455,-2.152243,-7.417108,-1.041405,-3.565352,1.292848,5.176239,-5.267008,-5.824908,-2.444262,-8.485135,-1.730281,1.455039,0.919338,-9.609806,0.429239,-5.516403,-6.622309,7.110420,0.023083,-5.967034,4.696127,-8.822579,-9.250638,6.878192,-9.324466,-4.890167,7.894191,2.093357,-5.177451,9.510040,4.969056,-5.733525,-1.815547,-7.740798], dtype = "float64")#candidate|3219|(528,)|const|float64
const_3220 = relay.const([-10,10,9,9,2,-7,7,9,8,-1,2,2,-1,6,-7,-9,-7,8,2,6,-7,-10,8,2,7,-8,-3,-4,-9,-8,-1,-5,7,-4,1,2,-4,4,-2,-2,2,-7,-2,1,-3,-8,-7,1,-6,-2,-7,-7,-7,-7,-9,-7,10,-8,-6,6,8,-2,-6,-9,-9,1,5,1,9,2,-8,1,-2,-2,7,-6,1,10,-2,-2,-1,-9,9,10,-9,-7,9,4], dtype = "uint8")#candidate|3220|(88,)|const|uint8
var_3221 = relay.var("var_3221", dtype = "uint32", shape = (40, 1))#candidate|3221|(40, 1)|var|uint32
const_3222 = relay.const([-5,3,9,-4,2,1,-5,3,7,-3,-10,-9,4,4,-10,-2,-5,-10,6,5,1,-4,-2,2,1,-8,-8,9,-8,1,1,-6,8,-5,1,-2,6,1,-5,7,10,-8,-4,-8,2,-2,-5,-3,4,7,6,10,-5,9,-3,5,-4,10,10,8,-1,6,9,-7,5,-8,3,-4,8,10,2,5,-10,1,6,3,10,-1,9,1,4,-9,-9,9,6,9,9,-1,-10,9,4,1,-1,2,-2,8,-4,7,7,3,7,3,-7,-3,9,-10,3,-6], dtype = "int16")#candidate|3222|(108,)|const|int16
call_3218 = relay.TupleGetItem(func_2856_call(relay.reshape(const_3219.astype('float64'), [24, 22]), relay.reshape(const_3220.astype('uint8'), [88,]), relay.reshape(var_3221.astype('uint32'), [40,]), relay.reshape(const_3222.astype('int16'), [3, 36]), ), 6)
call_3223 = relay.TupleGetItem(func_2862_call(relay.reshape(const_3219.astype('float64'), [24, 22]), relay.reshape(const_3220.astype('uint8'), [88,]), relay.reshape(var_3221.astype('uint32'), [40,]), relay.reshape(const_3222.astype('int16'), [3, 36]), ), 6)
output = relay.Tuple([bop_3214,call_3218,const_3219,const_3220,var_3221,const_3222,])
output2 = relay.Tuple([bop_3214,call_3223,const_3219,const_3220,var_3221,const_3222,])
func_3249 = relay.Function([var_3212,var_3213,var_3221,], output)
mod['func_3249'] = func_3249
mod = relay.transform.InferType()(mod)
mutated_mod['func_3249'] = func_3249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3249_call = mutated_mod.get_global_var('func_3249')
var_3251 = relay.var("var_3251", dtype = "int32", shape = (10, 14, 10))#candidate|3251|(10, 14, 10)|var|int32
var_3252 = relay.var("var_3252", dtype = "int32", shape = (10, 14, 10))#candidate|3252|(10, 14, 10)|var|int32
var_3253 = relay.var("var_3253", dtype = "uint32", shape = (40, 1))#candidate|3253|(40, 1)|var|uint32
call_3250 = func_3249_call(var_3251,var_3252,var_3253,)
output = call_3250
func_3254 = relay.Function([var_3251,var_3252,var_3253,], output)
mutated_mod['func_3254'] = func_3254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_3273 = relay.TupleGetItem(func_2072_call(), 1)
call_3274 = relay.TupleGetItem(func_2074_call(), 1)
output = relay.Tuple([call_3273,])
output2 = relay.Tuple([call_3274,])
func_3286 = relay.Function([], output)
mod['func_3286'] = func_3286
mod = relay.transform.InferType()(mod)
output = func_3286()
func_3287 = relay.Function([], output)
mutated_mod['func_3287'] = func_3287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3286_call = mod.get_global_var('func_3286')
func_3287_call = mutated_mod.get_global_var('func_3287')
call_3304 = relay.TupleGetItem(func_3286_call(), 0)
call_3305 = relay.TupleGetItem(func_3287_call(), 0)
var_3306 = relay.var("var_3306", dtype = "float64", shape = (2, 15, 5))#candidate|3306|(2, 15, 5)|var|float64
bop_3307 = relay.logical_and(call_3304.astype('bool'), relay.reshape(var_3306.astype('bool'), relay.shape_of(call_3304))) # shape=(2, 15, 5)
bop_3310 = relay.logical_and(call_3305.astype('bool'), relay.reshape(var_3306.astype('bool'), relay.shape_of(call_3305))) # shape=(2, 15, 5)
uop_3312 = relay.atanh(bop_3307.astype('float32')) # shape=(2, 15, 5)
uop_3314 = relay.atanh(bop_3310.astype('float32')) # shape=(2, 15, 5)
output = relay.Tuple([uop_3312,])
output2 = relay.Tuple([uop_3314,])
func_3321 = relay.Function([var_3306,], output)
mod['func_3321'] = func_3321
mod = relay.transform.InferType()(mod)
var_3322 = relay.var("var_3322", dtype = "float64", shape = (2, 15, 5))#candidate|3322|(2, 15, 5)|var|float64
output = func_3321(var_3322)
func_3323 = relay.Function([var_3322], output)
mutated_mod['func_3323'] = func_3323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2394_call = mod.get_global_var('func_2394')
func_2396_call = mutated_mod.get_global_var('func_2396')
call_3413 = relay.TupleGetItem(func_2394_call(), 0)
call_3414 = relay.TupleGetItem(func_2396_call(), 0)
func_691_call = mod.get_global_var('func_691')
func_694_call = mutated_mod.get_global_var('func_694')
const_3418 = relay.const([-2.302860,-9.549442,6.933984,-3.410340,0.653441,-5.765020,8.996763,3.706043,7.216331,-7.187582,1.833552,5.786856,4.217778,9.236928], dtype = "float32")#candidate|3418|(14,)|const|float32
call_3417 = relay.TupleGetItem(func_691_call(relay.reshape(const_3418.astype('float32'), [1, 1, 14])), 0)
call_3419 = relay.TupleGetItem(func_694_call(relay.reshape(const_3418.astype('float32'), [1, 1, 14])), 0)
output = relay.Tuple([call_3413,call_3417,const_3418,])
output2 = relay.Tuple([call_3414,call_3419,const_3418,])
func_3427 = relay.Function([], output)
mod['func_3427'] = func_3427
mod = relay.transform.InferType()(mod)
output = func_3427()
func_3428 = relay.Function([], output)
mutated_mod['func_3428'] = func_3428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3436 = relay.var("var_3436", dtype = "uint16", shape = (3, 7, 10))#candidate|3436|(3, 7, 10)|var|uint16
var_3437 = relay.var("var_3437", dtype = "uint16", shape = (3, 7, 10))#candidate|3437|(3, 7, 10)|var|uint16
bop_3438 = relay.maximum(var_3436.astype('uint16'), relay.reshape(var_3437.astype('uint16'), relay.shape_of(var_3436))) # shape=(3, 7, 10)
bop_3442 = relay.bitwise_or(var_3437.astype('int32'), relay.reshape(var_3436.astype('int32'), relay.shape_of(var_3437))) # shape=(3, 7, 10)
var_3457 = relay.var("var_3457", dtype = "uint16", shape = (3, 7, 10))#candidate|3457|(3, 7, 10)|var|uint16
bop_3458 = relay.floor_mod(var_3437.astype('float64'), relay.reshape(var_3457.astype('float64'), relay.shape_of(var_3437))) # shape=(3, 7, 10)
uop_3462 = relay.cosh(bop_3438.astype('float32')) # shape=(3, 7, 10)
uop_3467 = relay.sqrt(uop_3462.astype('float64')) # shape=(3, 7, 10)
output = relay.Tuple([bop_3442,bop_3458,uop_3467,])
output2 = relay.Tuple([bop_3442,bop_3458,uop_3467,])
func_3469 = relay.Function([var_3436,var_3437,var_3457,], output)
mod['func_3469'] = func_3469
mod = relay.transform.InferType()(mod)
var_3470 = relay.var("var_3470", dtype = "uint16", shape = (3, 7, 10))#candidate|3470|(3, 7, 10)|var|uint16
var_3471 = relay.var("var_3471", dtype = "uint16", shape = (3, 7, 10))#candidate|3471|(3, 7, 10)|var|uint16
var_3472 = relay.var("var_3472", dtype = "uint16", shape = (3, 7, 10))#candidate|3472|(3, 7, 10)|var|uint16
output = func_3469(var_3470,var_3471,var_3472,)
func_3473 = relay.Function([var_3470,var_3471,var_3472,], output)
mutated_mod['func_3473'] = func_3473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mod.get_global_var('func_1863')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_3482 = func_1863_call()
call_3483 = func_1863_call()
func_3249_call = mod.get_global_var('func_3249')
func_3254_call = mutated_mod.get_global_var('func_3254')
var_3492 = relay.var("var_3492", dtype = "int32", shape = (1400,))#candidate|3492|(1400,)|var|int32
var_3493 = relay.var("var_3493", dtype = "uint32", shape = (40,))#candidate|3493|(40,)|var|uint32
call_3491 = relay.TupleGetItem(func_3249_call(relay.reshape(var_3492.astype('int32'), [10, 14, 10]), relay.reshape(var_3492.astype('int32'), [10, 14, 10]), relay.reshape(var_3493.astype('uint32'), [40, 1]), ), 2)
call_3494 = relay.TupleGetItem(func_3254_call(relay.reshape(var_3492.astype('int32'), [10, 14, 10]), relay.reshape(var_3492.astype('int32'), [10, 14, 10]), relay.reshape(var_3493.astype('uint32'), [40, 1]), ), 2)
output = relay.Tuple([call_3482,call_3491,var_3492,var_3493,])
output2 = relay.Tuple([call_3483,call_3494,var_3492,var_3493,])
func_3495 = relay.Function([var_3492,var_3493,], output)
mod['func_3495'] = func_3495
mod = relay.transform.InferType()(mod)
var_3496 = relay.var("var_3496", dtype = "int32", shape = (1400,))#candidate|3496|(1400,)|var|int32
var_3497 = relay.var("var_3497", dtype = "uint32", shape = (40,))#candidate|3497|(40,)|var|uint32
output = func_3495(var_3496,var_3497,)
func_3498 = relay.Function([var_3496,var_3497,], output)
mutated_mod['func_3498'] = func_3498
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3500 = relay.var("var_3500", dtype = "float64", shape = (15, 7, 10))#candidate|3500|(15, 7, 10)|var|float64
uop_3501 = relay.log10(var_3500.astype('float64')) # shape=(15, 7, 10)
bop_3503 = relay.greater_equal(uop_3501.astype('bool'), relay.reshape(var_3500.astype('bool'), relay.shape_of(uop_3501))) # shape=(15, 7, 10)
output = bop_3503
output2 = bop_3503
func_3506 = relay.Function([var_3500,], output)
mod['func_3506'] = func_3506
mod = relay.transform.InferType()(mod)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3507 = relay.var("var_3507", dtype = "float64", shape = (15, 7, 10))#candidate|3507|(15, 7, 10)|var|float64
func_3506_call = mutated_mod.get_global_var('func_3506')
call_3508 = func_3506_call(var_3507)
output = call_3508
func_3509 = relay.Function([var_3507], output)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1756_call = mod.get_global_var('func_1756')
func_1757_call = mutated_mod.get_global_var('func_1757')
call_3567 = func_1756_call()
call_3568 = func_1756_call()
func_2998_call = mod.get_global_var('func_2998')
func_3001_call = mutated_mod.get_global_var('func_3001')
var_3570 = relay.var("var_3570", dtype = "int32", shape = (48,))#candidate|3570|(48,)|var|int32
call_3569 = relay.TupleGetItem(func_2998_call(relay.reshape(var_3570.astype('int32'), [6, 2, 4])), 1)
call_3571 = relay.TupleGetItem(func_3001_call(relay.reshape(var_3570.astype('int32'), [6, 2, 4])), 1)
output = relay.Tuple([call_3567,call_3569,var_3570,])
output2 = relay.Tuple([call_3568,call_3571,var_3570,])
func_3577 = relay.Function([var_3570,], output)
mod['func_3577'] = func_3577
mod = relay.transform.InferType()(mod)
mutated_mod['func_3577'] = func_3577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3578 = relay.var("var_3578", dtype = "int32", shape = (48,))#candidate|3578|(48,)|var|int32
func_3577_call = mutated_mod.get_global_var('func_3577')
call_3579 = func_3577_call(var_3578)
output = call_3579
func_3580 = relay.Function([var_3578], output)
mutated_mod['func_3580'] = func_3580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2313_call = mod.get_global_var('func_2313')
func_2315_call = mutated_mod.get_global_var('func_2315')
call_3602 = func_2313_call()
call_3603 = func_2313_call()
output = call_3602
output2 = call_3603
func_3625 = relay.Function([], output)
mod['func_3625'] = func_3625
mod = relay.transform.InferType()(mod)
mutated_mod['func_3625'] = func_3625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3625_call = mutated_mod.get_global_var('func_3625')
call_3626 = func_3625_call()
output = call_3626
func_3627 = relay.Function([], output)
mutated_mod['func_3627'] = func_3627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2117_call = mod.get_global_var('func_2117')
func_2118_call = mutated_mod.get_global_var('func_2118')
call_3631 = relay.TupleGetItem(func_2117_call(), 0)
call_3632 = relay.TupleGetItem(func_2118_call(), 0)
func_1605_call = mod.get_global_var('func_1605')
func_1606_call = mutated_mod.get_global_var('func_1606')
call_3633 = relay.TupleGetItem(func_1605_call(), 0)
call_3634 = relay.TupleGetItem(func_1606_call(), 0)
output = relay.Tuple([call_3631,call_3633,])
output2 = relay.Tuple([call_3632,call_3634,])
func_3638 = relay.Function([], output)
mod['func_3638'] = func_3638
mod = relay.transform.InferType()(mod)
mutated_mod['func_3638'] = func_3638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mutated_mod.get_global_var('func_3638')
call_3639 = func_3638_call()
output = call_3639
func_3640 = relay.Function([], output)
mutated_mod['func_3640'] = func_3640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2117_call = mod.get_global_var('func_2117')
func_2118_call = mutated_mod.get_global_var('func_2118')
call_3671 = relay.TupleGetItem(func_2117_call(), 0)
call_3672 = relay.TupleGetItem(func_2118_call(), 0)
output = relay.Tuple([call_3671,])
output2 = relay.Tuple([call_3672,])
func_3697 = relay.Function([], output)
mod['func_3697'] = func_3697
mod = relay.transform.InferType()(mod)
output = func_3697()
func_3698 = relay.Function([], output)
mutated_mod['func_3698'] = func_3698
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3707 = relay.var("var_3707", dtype = "uint32", shape = (2, 2, 10))#candidate|3707|(2, 2, 10)|var|uint32
var_3708 = relay.var("var_3708", dtype = "uint32", shape = (2, 2, 10))#candidate|3708|(2, 2, 10)|var|uint32
bop_3709 = relay.less(var_3707.astype('bool'), relay.reshape(var_3708.astype('bool'), relay.shape_of(var_3707))) # shape=(2, 2, 10)
uop_3712 = relay.sqrt(var_3708.astype('float64')) # shape=(2, 2, 10)
bop_3717 = relay.add(uop_3712.astype('uint8'), relay.reshape(bop_3709.astype('uint8'), relay.shape_of(uop_3712))) # shape=(2, 2, 10)
bop_3722 = relay.subtract(bop_3717.astype('int16'), relay.reshape(var_3707.astype('int16'), relay.shape_of(bop_3717))) # shape=(2, 2, 10)
func_3427_call = mod.get_global_var('func_3427')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3725 = relay.TupleGetItem(func_3427_call(), 0)
call_3726 = relay.TupleGetItem(func_3428_call(), 0)
output = relay.Tuple([bop_3722,call_3725,])
output2 = relay.Tuple([bop_3722,call_3726,])
func_3732 = relay.Function([var_3707,var_3708,], output)
mod['func_3732'] = func_3732
mod = relay.transform.InferType()(mod)
var_3733 = relay.var("var_3733", dtype = "uint32", shape = (2, 2, 10))#candidate|3733|(2, 2, 10)|var|uint32
var_3734 = relay.var("var_3734", dtype = "uint32", shape = (2, 2, 10))#candidate|3734|(2, 2, 10)|var|uint32
output = func_3732(var_3733,var_3734,)
func_3735 = relay.Function([var_3733,var_3734,], output)
mutated_mod['func_3735'] = func_3735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3427_call = mod.get_global_var('func_3427')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3737 = relay.TupleGetItem(func_3427_call(), 0)
call_3738 = relay.TupleGetItem(func_3428_call(), 0)
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
const_3747 = relay.const([-5,-5,-10,5,9,9,-10,10,5,-1,-6,9,5,7,-7,-10,-9,7,8,-3,-2,7,-3,1,3,-4,-5,5,5,6,10,6,4,1,7,-9,8,-3,2,-9,-8,-6,-4,-4,2,-2,-7,4,-4,-1,10,-2,-5,9,10,4,1,-10,-10,-5,-4,7,-5,-3,7,-10,6,-5,-8,8,-2,-6,2,-9,2,-7,1,10,-6,-5,-8,1,-8,5,-1,-5,-7,6,-9,-2,-9,9,-2,5,3,4,-6,7,1,1,-7,7,-9,1,-7,1,3,-5,-9,4,2,-3,-5,4,2,-10,-2,-1,9,1,7,2,-1,5,-9,2,-9,2,7,9,-1,-10,-5,6,-5,10,8,-3,10,9,-9,3,-9,-3,2,8,3,10,9,4,2,7,7,-9,8,-6,-10,-8,-7,3,-4,-5,-9,9,-1,-3,6,-3,9,-9,1,-5,-6,7,-3,3,3,6,-2,-1,7,-8,-3,-7,-4,-9,-2,3,5,-3,10,8,3,5,-1,10,10,3,8,4,-6,4,-7,-8,-7,-3,-7,2,4,-7,6,5,5,7,-9,5,6,-7,-8,-5,8,-4,6,-4,5,-7,3,5,3,-3,-5,-2,-10,3,-4,5,-6,-6,6,5,5,10,-8,-6,-9,5,-7,-6,-4,5,9,1,-10,8,-10,5,8,1,-10,-7,6,-4,7,-10,-9,2,-6,3,-1,-1,-5,6,4,9,6,5,-8,-7,-9,9,-1,-5,-3,4,-1,-6,-5,-10], dtype = "uint8")#candidate|3747|(288,)|const|uint8
call_3746 = relay.TupleGetItem(func_1247_call(relay.reshape(const_3747.astype('uint8'), [288,])), 4)
call_3748 = relay.TupleGetItem(func_1250_call(relay.reshape(const_3747.astype('uint8'), [288,])), 4)
output = relay.Tuple([call_3737,call_3746,const_3747,])
output2 = relay.Tuple([call_3738,call_3748,const_3747,])
func_3750 = relay.Function([], output)
mod['func_3750'] = func_3750
mod = relay.transform.InferType()(mod)
output = func_3750()
func_3751 = relay.Function([], output)
mutated_mod['func_3751'] = func_3751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3112_call = mod.get_global_var('func_3112')
func_3114_call = mutated_mod.get_global_var('func_3114')
call_3754 = relay.TupleGetItem(func_3112_call(), 0)
call_3755 = relay.TupleGetItem(func_3114_call(), 0)
var_3766 = relay.var("var_3766", dtype = "float32", shape = (4, 16, 7))#candidate|3766|(4, 16, 7)|var|float32
bop_3767 = relay.bitwise_or(call_3754.astype('int16'), var_3766.astype('int16')) # shape=(4, 16, 7)
bop_3770 = relay.bitwise_or(call_3755.astype('int16'), var_3766.astype('int16')) # shape=(4, 16, 7)
uop_3777 = relay.sqrt(var_3766.astype('float64')) # shape=(4, 16, 7)
bop_3779 = relay.add(uop_3777.astype('float64'), relay.reshape(bop_3767.astype('float64'), relay.shape_of(uop_3777))) # shape=(4, 16, 7)
bop_3782 = relay.add(uop_3777.astype('float64'), relay.reshape(bop_3770.astype('float64'), relay.shape_of(uop_3777))) # shape=(4, 16, 7)
output = bop_3779
output2 = bop_3782
func_3802 = relay.Function([var_3766,], output)
mod['func_3802'] = func_3802
mod = relay.transform.InferType()(mod)
var_3803 = relay.var("var_3803", dtype = "float32", shape = (4, 16, 7))#candidate|3803|(4, 16, 7)|var|float32
output = func_3802(var_3803)
func_3804 = relay.Function([var_3803], output)
mutated_mod['func_3804'] = func_3804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1694_call = mutated_mod.get_global_var('func_1694')
call_3859 = func_1692_call()
call_3860 = func_1692_call()
func_691_call = mod.get_global_var('func_691')
func_694_call = mutated_mod.get_global_var('func_694')
const_3870 = relay.const([-3.669217,2.967468,8.455799,-0.354703,-3.002705,-0.038897,9.672269,-8.022862,8.763245,-1.108263,6.580856,7.724810,7.144047,4.743782], dtype = "float32")#candidate|3870|(14,)|const|float32
call_3869 = relay.TupleGetItem(func_691_call(relay.reshape(const_3870.astype('float32'), [1, 1, 14])), 0)
call_3871 = relay.TupleGetItem(func_694_call(relay.reshape(const_3870.astype('float32'), [1, 1, 14])), 0)
output = relay.Tuple([call_3859,call_3869,const_3870,])
output2 = relay.Tuple([call_3860,call_3871,const_3870,])
func_3873 = relay.Function([], output)
mod['func_3873'] = func_3873
mod = relay.transform.InferType()(mod)
output = func_3873()
func_3874 = relay.Function([], output)
mutated_mod['func_3874'] = func_3874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3286_call = mod.get_global_var('func_3286')
func_3287_call = mutated_mod.get_global_var('func_3287')
call_3897 = relay.TupleGetItem(func_3286_call(), 0)
call_3898 = relay.TupleGetItem(func_3287_call(), 0)
func_3750_call = mod.get_global_var('func_3750')
func_3751_call = mutated_mod.get_global_var('func_3751')
call_3899 = relay.TupleGetItem(func_3750_call(), 1)
call_3900 = relay.TupleGetItem(func_3751_call(), 1)
uop_3915 = relay.cosh(call_3899.astype('float32')) # shape=(288,)
uop_3917 = relay.cosh(call_3900.astype('float32')) # shape=(288,)
var_3934 = relay.var("var_3934", dtype = "float64", shape = (2, 15, 5))#candidate|3934|(2, 15, 5)|var|float64
bop_3935 = relay.left_shift(call_3897.astype('int16'), relay.reshape(var_3934.astype('int16'), relay.shape_of(call_3897))) # shape=(2, 15, 5)
bop_3938 = relay.left_shift(call_3898.astype('int16'), relay.reshape(var_3934.astype('int16'), relay.shape_of(call_3898))) # shape=(2, 15, 5)
func_2424_call = mod.get_global_var('func_2424')
func_2426_call = mutated_mod.get_global_var('func_2426')
call_3942 = func_2424_call()
call_3943 = func_2424_call()
func_3321_call = mod.get_global_var('func_3321')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_3945 = relay.TupleGetItem(func_3321_call(relay.reshape(bop_3935.astype('float64'), [2, 15, 5])), 0)
call_3946 = relay.TupleGetItem(func_3323_call(relay.reshape(bop_3935.astype('float64'), [2, 15, 5])), 0)
output = relay.Tuple([uop_3915,bop_3935,call_3942,call_3945,])
output2 = relay.Tuple([uop_3917,bop_3938,call_3943,call_3946,])
func_3947 = relay.Function([var_3934,], output)
mod['func_3947'] = func_3947
mod = relay.transform.InferType()(mod)
mutated_mod['func_3947'] = func_3947
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3948 = relay.var("var_3948", dtype = "float64", shape = (2, 15, 5))#candidate|3948|(2, 15, 5)|var|float64
func_3947_call = mutated_mod.get_global_var('func_3947')
call_3949 = func_3947_call(var_3948)
output = call_3949
func_3950 = relay.Function([var_3948], output)
mutated_mod['func_3950'] = func_3950
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4009 = relay.const([[[2.484554,-9.218130,-2.085722,3.583686],[3.834654,-8.172644,-4.485012,-0.429278],[-8.946617,2.966646,-8.218837,-5.620147]],[[-4.052469,-6.201896,4.363693,7.871627],[8.162606,4.554184,7.167305,2.397887],[7.430465,-0.786358,-7.781167,3.320500]],[[-1.392189,-6.413558,-2.677301,0.855506],[-9.927063,-8.333542,5.576080,-7.307827],[8.713599,8.380980,-3.190500,-7.537852]],[[-8.348976,-4.287516,2.150004,9.076981],[-9.886951,-0.025765,-0.267468,6.241680],[6.877893,6.117966,2.872146,-7.382225]],[[0.068985,2.108845,-2.013102,9.307714],[-5.163569,4.928479,4.270733,-1.175400],[6.000062,4.676090,-7.807730,-2.395878]],[[-5.879735,3.983558,-3.278602,-5.059926],[0.966134,3.735593,3.425699,-0.035967],[-3.942050,-2.651893,6.931153,6.531980]],[[7.646486,-1.271250,6.012408,-2.520794],[-0.097774,2.741758,5.449023,-7.535626],[1.159434,-0.523530,-2.874789,9.312138]],[[-6.664740,8.177326,-3.678205,-3.138126],[1.524254,8.824140,-8.482228,-1.220344],[5.549832,4.167594,1.508154,4.400368]],[[3.687536,-7.537397,7.073255,7.213492],[6.013881,5.119596,3.325633,9.024342],[-0.204290,-1.767231,-9.936627,-8.180254]],[[-1.340949,-2.791421,8.466278,5.269202],[3.158715,5.884618,9.920215,7.876645],[5.323356,-0.222514,-7.102709,5.296796]],[[-5.593214,3.779378,-4.994515,9.418814],[7.108839,-3.652655,0.907013,-0.818654],[6.958333,3.144791,-8.267182,6.612749]],[[3.711202,-3.126478,-6.727027,2.671687],[6.564313,1.818367,-7.779601,3.758501],[3.382184,-8.362161,7.871171,0.246273]]], dtype = "float64")#candidate|4009|(12, 3, 4)|const|float64
uop_4010 = relay.asinh(const_4009.astype('float64')) # shape=(12, 3, 4)
bop_4012 = relay.mod(uop_4010.astype('float64'), relay.reshape(const_4009.astype('float64'), relay.shape_of(uop_4010))) # shape=(12, 3, 4)
func_2184_call = mod.get_global_var('func_2184')
func_2188_call = mutated_mod.get_global_var('func_2188')
const_4018 = relay.const([10,-8,3,-2,-9,-4,-9,2,-5,-2,10,10,8,-10,-7,-6,6,5,-4,-4,7,9,-5,2,4,10,3,-1,-3,10,3,9,2,7,-3,8,-10,-6,10,4,5,7,-5,10,1,-8,-8,4,-10,-5,-3,-3,-1,-8,8,-2,8,-2,10,-3,-2,5,-7,-1,9,2,-10,-5,-5,-2,4,7,-3,-7,10,4,-10,-3,8,-5,-1,-7,3,4,4,2,-1,-4,-9,9,-2,3,-2,10,-2,4,-4,-8,4,7,-9,-10,2,-7,4,10,9,-9,-2,8,5,-1,5,-8,-3,-9,-5,-5,2,6,7,5,1,-6,2,-1,6,-6,1,-1,8,-1,10,8,9,1,1,-4,9,-9,4,6,10,-2,-5,-9,7,-3,-7,3,6,4,2,-4,-9,-10,1,-4,9,5,-3,4,-6,8,-10,1,-5,-7,-4,7,-2,-8,-4,-7,10,-4,8,-4,-7,-8,-1,4,4,4,10,3,10,-8,-6,7,9,-1,-1,1,-5,-4,-8,4,-10,1,-2,6,6,6,9,9,5,4,3,6,2,6,-10,1,-1,-2,7,-4,-9,6,-4,-5,5,6,5,-5,2,9,2,-10,4,-5,-9,5,-7,-8,-8,-9,4,-10], dtype = "uint32")#candidate|4018|(240,)|const|uint32
const_4019 = relay.const([-6,-6,1,-4], dtype = "int32")#candidate|4019|(4,)|const|int32
call_4017 = relay.TupleGetItem(func_2184_call(relay.reshape(const_4018.astype('uint32'), [10, 3, 8]), relay.reshape(const_4019.astype('int32'), [2, 2]), ), 0)
call_4020 = relay.TupleGetItem(func_2188_call(relay.reshape(const_4018.astype('uint32'), [10, 3, 8]), relay.reshape(const_4019.astype('int32'), [2, 2]), ), 0)
func_2184_call = mod.get_global_var('func_2184')
func_2188_call = mutated_mod.get_global_var('func_2188')
call_4023 = relay.TupleGetItem(func_2184_call(relay.reshape(call_4017.astype('uint32'), [10, 3, 8]), relay.reshape(const_4019.astype('int32'), [2, 2]), ), 1)
call_4024 = relay.TupleGetItem(func_2188_call(relay.reshape(call_4017.astype('uint32'), [10, 3, 8]), relay.reshape(const_4019.astype('int32'), [2, 2]), ), 1)
bop_4025 = relay.logical_or(bop_4012.astype('bool'), call_4023.astype('bool')) # shape=(12, 3, 4)
bop_4028 = relay.logical_or(bop_4012.astype('bool'), call_4024.astype('bool')) # shape=(12, 3, 4)
const_4031 = relay.const([[[-4.088207,-4.029019,-9.450489,-4.340534],[-8.393798,-0.610959,-3.663511,9.354448],[-1.807593,2.595331,1.581047,-8.648857]],[[0.027605,-0.040438,-9.777515,-5.976794],[2.565855,-1.725700,-8.415252,4.960131],[7.829118,4.969623,-9.244522,-6.351008]],[[-2.371443,2.129478,-7.647979,-8.599041],[6.770015,-4.498305,-9.975458,4.995721],[-5.114002,4.210276,-9.449870,9.508078]],[[7.540903,6.025804,7.764609,-1.627632],[3.385464,6.385183,2.060740,4.379190],[6.795334,9.772830,-6.663362,1.615224]],[[-0.333956,5.364350,8.543178,-5.616470],[1.128672,-3.991400,-7.017967,-5.035827],[-4.822839,4.579780,5.256224,1.727129]],[[5.225810,-7.327539,0.684250,-0.185535],[6.805956,-5.468635,-2.039734,1.395532],[-4.465524,-8.942316,-8.854732,-6.385777]],[[3.844347,7.572094,-7.724044,3.071162],[9.259594,6.738762,0.444451,-1.190503],[9.286937,2.073938,-7.310075,3.031840]],[[-7.063762,1.811692,7.057041,6.082806],[8.851857,8.504304,4.611444,6.377258],[9.207926,7.073046,-6.143075,2.372994]],[[-5.579802,3.141609,7.417216,0.324630],[9.354636,-9.654917,-7.943660,0.497953],[-1.698968,5.325323,3.223524,-0.173153]],[[6.212261,9.914933,-4.206101,0.375048],[1.590772,2.052463,-9.428024,-0.802218],[6.762275,-6.642259,-6.278497,5.232499]],[[-4.012877,8.052404,-4.681067,-2.904557],[9.683315,1.278566,-4.351659,9.999047],[-7.093050,-9.854237,5.780367,-3.312077]],[[-0.736960,4.962599,-9.914060,7.630873],[9.069200,-7.126102,0.866969,-2.173539],[-0.876162,-1.355609,-8.894477,-1.170423]]], dtype = "float64")#candidate|4031|(12, 3, 4)|const|float64
bop_4032 = relay.multiply(bop_4012.astype('int8'), relay.reshape(const_4031.astype('int8'), relay.shape_of(bop_4012))) # shape=(12, 3, 4)
output = relay.Tuple([call_4017,const_4018,const_4019,bop_4025,bop_4032,])
output2 = relay.Tuple([call_4020,const_4018,const_4019,bop_4028,bop_4032,])
func_4037 = relay.Function([], output)
mod['func_4037'] = func_4037
mod = relay.transform.InferType()(mod)
mutated_mod['func_4037'] = func_4037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4037_call = mutated_mod.get_global_var('func_4037')
call_4038 = func_4037_call()
output = call_4038
func_4039 = relay.Function([], output)
mutated_mod['func_4039'] = func_4039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3167_call = mod.get_global_var('func_3167')
func_3168_call = mutated_mod.get_global_var('func_3168')
call_4043 = relay.TupleGetItem(func_3167_call(), 0)
call_4044 = relay.TupleGetItem(func_3168_call(), 0)
output = relay.Tuple([call_4043,])
output2 = relay.Tuple([call_4044,])
func_4047 = relay.Function([], output)
mod['func_4047'] = func_4047
mod = relay.transform.InferType()(mod)
output = func_4047()
func_4048 = relay.Function([], output)
mutated_mod['func_4048'] = func_4048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4037_call = mod.get_global_var('func_4037')
func_4039_call = mutated_mod.get_global_var('func_4039')
call_4109 = relay.TupleGetItem(func_4037_call(), 2)
call_4110 = relay.TupleGetItem(func_4039_call(), 2)
func_1191_call = mod.get_global_var('func_1191')
func_1195_call = mutated_mod.get_global_var('func_1195')
const_4113 = relay.const([-6,7,-6,3,-7,7,-3,9,8,-7,-10,4,2,-10,-6,1,1,-9,4,-10,-10,-6,-7,2,7,-8,2,6,8,8,-6,-5,9,-3,-5,-2,3,-8,7,8,1,-10,9,-7,-2,2,-4,-7,10,-7,-5,2,9,10,1,-9,-5,-7,6,1,1,-8,-10,-9,6,-7,-5,1,-10,1,9,6,-10,6,9,4,1,-6,-6,1,-10,-3,9,2,-2,-1,-4,5,-3,10,8,-3,-5,-8,-3,10,-7,-8,-6,-6,-3,1,7,1,-7,-2,-4,-4,2,-9,2,8,-2,-6,9,9,10,-9,-8,-4,3,9,-1,-6,6,-7,5,-10,2,-9,9,-2,10,5,-4,-2,-7,6,-6,10,-10,-2,10,3,-7,2,-2,4,-8,9,-10,-8,-4,4,9,-1,8,-3,3,-2,-8,-6,-9,-2,1,-8,4,7,-2,-5,-2,-9,2,-1,-8,7,7,8,-6,-4,4,8,-10,6,-4,3,9,-6,-4,8,-8,-7,8,3,-6,1,-9,-7,-3,-10,-6,-1,-7,-8,4,2,-10,-8,-4,4,-6,-9,-5,-3,-1,-3,8,-4,3,-7,-7,-10,7,7,9,-1,-6,1,9,10,-8,7,-7,4,-2,-8,9,-7,-5,8,-6,10,-9,5,-6,-8,-8,-2,-7,-6,7,-1,1,3,-4,2,1,-4,-7,-10,6,9,6,-10,10,-3,1,3,2,9,-10,6,7,2,10,6,4,9,-9,-3], dtype = "uint8")#candidate|4113|(280,)|const|uint8
call_4112 = relay.TupleGetItem(func_1191_call(relay.reshape(const_4113.astype('uint8'), [10, 14, 2]), relay.reshape(const_4113.astype('uint8'), [10, 14, 2]), ), 0)
call_4114 = relay.TupleGetItem(func_1195_call(relay.reshape(const_4113.astype('uint8'), [10, 14, 2]), relay.reshape(const_4113.astype('uint8'), [10, 14, 2]), ), 0)
output = relay.Tuple([call_4109,call_4112,const_4113,])
output2 = relay.Tuple([call_4110,call_4114,const_4113,])
func_4119 = relay.Function([], output)
mod['func_4119'] = func_4119
mod = relay.transform.InferType()(mod)
mutated_mod['func_4119'] = func_4119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4119_call = mutated_mod.get_global_var('func_4119')
call_4120 = func_4119_call()
output = call_4120
func_4121 = relay.Function([], output)
mutated_mod['func_4121'] = func_4121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4119_call = mod.get_global_var('func_4119')
func_4121_call = mutated_mod.get_global_var('func_4121')
call_4125 = relay.TupleGetItem(func_4119_call(), 2)
call_4126 = relay.TupleGetItem(func_4121_call(), 2)
func_4119_call = mod.get_global_var('func_4119')
func_4121_call = mutated_mod.get_global_var('func_4121')
call_4143 = relay.TupleGetItem(func_4119_call(), 0)
call_4144 = relay.TupleGetItem(func_4121_call(), 0)
uop_4146 = relay.exp(call_4125.astype('float32')) # shape=(280,)
uop_4148 = relay.exp(call_4126.astype('float32')) # shape=(280,)
func_3249_call = mod.get_global_var('func_3249')
func_3254_call = mutated_mod.get_global_var('func_3254')
var_4153 = relay.var("var_4153", dtype = "int32", shape = (1400,))#candidate|4153|(1400,)|var|int32
const_4154 = relay.const([-2,6,1,3,-1,-6,6,-7,-5,-9,-6,-3,1,1,1,-2,8,-1,9,-8,8,5,3,10,3,-6,-6,-3,9,10,7,1,1,-6,-7,-9,8,9,-7,9], dtype = "uint32")#candidate|4154|(40,)|const|uint32
call_4152 = relay.TupleGetItem(func_3249_call(relay.reshape(var_4153.astype('int32'), [10, 14, 10]), relay.reshape(var_4153.astype('int32'), [10, 14, 10]), relay.reshape(const_4154.astype('uint32'), [40, 1]), ), 0)
call_4155 = relay.TupleGetItem(func_3254_call(relay.reshape(var_4153.astype('int32'), [10, 14, 10]), relay.reshape(var_4153.astype('int32'), [10, 14, 10]), relay.reshape(const_4154.astype('uint32'), [40, 1]), ), 0)
output = relay.Tuple([call_4143,uop_4146,call_4152,var_4153,const_4154,])
output2 = relay.Tuple([call_4144,uop_4148,call_4155,var_4153,const_4154,])
func_4164 = relay.Function([var_4153,], output)
mod['func_4164'] = func_4164
mod = relay.transform.InferType()(mod)
mutated_mod['func_4164'] = func_4164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4165 = relay.var("var_4165", dtype = "int32", shape = (1400,))#candidate|4165|(1400,)|var|int32
func_4164_call = mutated_mod.get_global_var('func_4164')
call_4166 = func_4164_call(var_4165)
output = call_4166
func_4167 = relay.Function([var_4165], output)
mutated_mod['func_4167'] = func_4167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3427_call = mod.get_global_var('func_3427')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_4197 = relay.TupleGetItem(func_3427_call(), 2)
call_4198 = relay.TupleGetItem(func_3428_call(), 2)
output = call_4197
output2 = call_4198
func_4213 = relay.Function([], output)
mod['func_4213'] = func_4213
mod = relay.transform.InferType()(mod)
output = func_4213()
func_4214 = relay.Function([], output)
mutated_mod['func_4214'] = func_4214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2394_call = mod.get_global_var('func_2394')
func_2396_call = mutated_mod.get_global_var('func_2396')
call_4218 = relay.TupleGetItem(func_2394_call(), 1)
call_4219 = relay.TupleGetItem(func_2396_call(), 1)
func_2313_call = mod.get_global_var('func_2313')
func_2315_call = mutated_mod.get_global_var('func_2315')
call_4235 = func_2313_call()
call_4236 = func_2313_call()
output = relay.Tuple([call_4218,call_4235,])
output2 = relay.Tuple([call_4219,call_4236,])
func_4237 = relay.Function([], output)
mod['func_4237'] = func_4237
mod = relay.transform.InferType()(mod)
output = func_4237()
func_4238 = relay.Function([], output)
mutated_mod['func_4238'] = func_4238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_4241 = relay.TupleGetItem(func_2072_call(), 2)
call_4242 = relay.TupleGetItem(func_2074_call(), 2)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_4243 = relay.TupleGetItem(func_2072_call(), 0)
call_4244 = relay.TupleGetItem(func_2074_call(), 0)
func_4037_call = mod.get_global_var('func_4037')
func_4039_call = mutated_mod.get_global_var('func_4039')
call_4254 = relay.TupleGetItem(func_4037_call(), 4)
call_4255 = relay.TupleGetItem(func_4039_call(), 4)
var_4268 = relay.var("var_4268", dtype = "float32", shape = (4, 16, 7))#candidate|4268|(4, 16, 7)|var|float32
bop_4269 = relay.bitwise_xor(call_4243.astype('int8'), var_4268.astype('int8')) # shape=(4, 16, 7)
bop_4272 = relay.bitwise_xor(call_4244.astype('int8'), var_4268.astype('int8')) # shape=(4, 16, 7)
output = relay.Tuple([call_4241,call_4254,bop_4269,])
output2 = relay.Tuple([call_4242,call_4255,bop_4272,])
func_4281 = relay.Function([var_4268,], output)
mod['func_4281'] = func_4281
mod = relay.transform.InferType()(mod)
mutated_mod['func_4281'] = func_4281
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4282 = relay.var("var_4282", dtype = "float32", shape = (4, 16, 7))#candidate|4282|(4, 16, 7)|var|float32
func_4281_call = mutated_mod.get_global_var('func_4281')
call_4283 = func_4281_call(var_4282)
output = call_4283
func_4284 = relay.Function([var_4282], output)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3167_call = mod.get_global_var('func_3167')
func_3168_call = mutated_mod.get_global_var('func_3168')
call_4286 = relay.TupleGetItem(func_3167_call(), 0)
call_4287 = relay.TupleGetItem(func_3168_call(), 0)
output = call_4286
output2 = call_4287
func_4288 = relay.Function([], output)
mod['func_4288'] = func_4288
mod = relay.transform.InferType()(mod)
output = func_4288()
func_4289 = relay.Function([], output)
mutated_mod['func_4289'] = func_4289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_4341 = relay.TupleGetItem(func_2072_call(), 0)
call_4342 = relay.TupleGetItem(func_2074_call(), 0)
func_4119_call = mod.get_global_var('func_4119')
func_4121_call = mutated_mod.get_global_var('func_4121')
call_4368 = relay.TupleGetItem(func_4119_call(), 2)
call_4369 = relay.TupleGetItem(func_4121_call(), 2)
func_3947_call = mod.get_global_var('func_3947')
func_3950_call = mutated_mod.get_global_var('func_3950')
var_4377 = relay.var("var_4377", dtype = "float64", shape = (150,))#candidate|4377|(150,)|var|float64
call_4376 = relay.TupleGetItem(func_3947_call(relay.reshape(var_4377.astype('float64'), [2, 15, 5])), 2)
call_4378 = relay.TupleGetItem(func_3950_call(relay.reshape(var_4377.astype('float64'), [2, 15, 5])), 2)
output = relay.Tuple([call_4341,call_4368,call_4376,var_4377,])
output2 = relay.Tuple([call_4342,call_4369,call_4378,var_4377,])
func_4381 = relay.Function([var_4377,], output)
mod['func_4381'] = func_4381
mod = relay.transform.InferType()(mod)
var_4382 = relay.var("var_4382", dtype = "float64", shape = (150,))#candidate|4382|(150,)|var|float64
output = func_4381(var_4382)
func_4383 = relay.Function([var_4382], output)
mutated_mod['func_4383'] = func_4383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4424 = relay.var("var_4424", dtype = "float32", shape = (2, 13, 5))#candidate|4424|(2, 13, 5)|var|float32
uop_4425 = relay.exp(var_4424.astype('float32')) # shape=(2, 13, 5)
bop_4427 = relay.bitwise_or(var_4424.astype('uint8'), relay.reshape(uop_4425.astype('uint8'), relay.shape_of(var_4424))) # shape=(2, 13, 5)
output = bop_4427
output2 = bop_4427
func_4432 = relay.Function([var_4424,], output)
mod['func_4432'] = func_4432
mod = relay.transform.InferType()(mod)
mutated_mod['func_4432'] = func_4432
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4433 = relay.var("var_4433", dtype = "float32", shape = (2, 13, 5))#candidate|4433|(2, 13, 5)|var|float32
func_4432_call = mutated_mod.get_global_var('func_4432')
call_4434 = func_4432_call(var_4433)
output = call_4434
func_4435 = relay.Function([var_4433], output)
mutated_mod['func_4435'] = func_4435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3057_call = mod.get_global_var('func_3057')
func_3058_call = mutated_mod.get_global_var('func_3058')
call_4437 = relay.TupleGetItem(func_3057_call(), 2)
call_4438 = relay.TupleGetItem(func_3058_call(), 2)
uop_4460 = relay.acosh(call_4437.astype('float32')) # shape=(1, 16, 7)
uop_4462 = relay.acosh(call_4438.astype('float32')) # shape=(1, 16, 7)
output = relay.Tuple([uop_4460,])
output2 = relay.Tuple([uop_4462,])
func_4468 = relay.Function([], output)
mod['func_4468'] = func_4468
mod = relay.transform.InferType()(mod)
mutated_mod['func_4468'] = func_4468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4468_call = mutated_mod.get_global_var('func_4468')
call_4469 = func_4468_call()
output = call_4469
func_4470 = relay.Function([], output)
mutated_mod['func_4470'] = func_4470
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4579 = relay.var("var_4579", dtype = "uint16", shape = (16, 15, 11))#candidate|4579|(16, 15, 11)|var|uint16
var_4580 = relay.var("var_4580", dtype = "uint16", shape = (16, 15, 11))#candidate|4580|(16, 15, 11)|var|uint16
bop_4581 = relay.logical_xor(var_4579.astype('uint16'), relay.reshape(var_4580.astype('uint16'), relay.shape_of(var_4579))) # shape=(16, 15, 11)
var_4586 = relay.var("var_4586", dtype = "uint16", shape = (16, 15, 11))#candidate|4586|(16, 15, 11)|var|uint16
bop_4587 = relay.left_shift(var_4580.astype('uint16'), relay.reshape(var_4586.astype('uint16'), relay.shape_of(var_4580))) # shape=(16, 15, 11)
output = relay.Tuple([bop_4581,bop_4587,])
output2 = relay.Tuple([bop_4581,bop_4587,])
func_4606 = relay.Function([var_4579,var_4580,var_4586,], output)
mod['func_4606'] = func_4606
mod = relay.transform.InferType()(mod)
var_4607 = relay.var("var_4607", dtype = "uint16", shape = (16, 15, 11))#candidate|4607|(16, 15, 11)|var|uint16
var_4608 = relay.var("var_4608", dtype = "uint16", shape = (16, 15, 11))#candidate|4608|(16, 15, 11)|var|uint16
var_4609 = relay.var("var_4609", dtype = "uint16", shape = (16, 15, 11))#candidate|4609|(16, 15, 11)|var|uint16
output = func_4606(var_4607,var_4608,var_4609,)
func_4610 = relay.Function([var_4607,var_4608,var_4609,], output)
mutated_mod['func_4610'] = func_4610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1756_call = mod.get_global_var('func_1756')
func_1757_call = mutated_mod.get_global_var('func_1757')
call_4672 = func_1756_call()
call_4673 = func_1756_call()
func_2856_call = mod.get_global_var('func_2856')
func_2862_call = mutated_mod.get_global_var('func_2862')
const_4686 = relay.const([9,-7,-10,-3,-10,-5,-1,-6,-9,-9,-3,9,-7,-8,10,3,1,-4,-4,1,7,6,-2,6,-5,6,-3,-5,3,-7,7,2,-1,8,-5,-9,6,-10,-10,-10,1,-2,-10,-7,2,-5,6,-6,4,-4,4,-1,1,-1,-8,-5,-6,7,3,8,-10,4,-10,4,-4,-5,4,-1,7,-7,2,6,-8,-5,-7,-6,-7,4,1,-5,8,3,4,-8,-3,-6,6,4], dtype = "uint8")#candidate|4686|(88,)|const|uint8
var_4687 = relay.var("var_4687", dtype = "uint32", shape = (40,))#candidate|4687|(40,)|var|uint32
const_4688 = relay.const([-3,-9,-5,10,-1,-1,3,-3,-6,-7,-8,8,6,-10,-3,3,-9,-6,5,10,-1,9,5,-2,-4,3,-6,8,3,4,4,-1,2,-9,5,5,10,-1,-7,-5,-6,3,-9,3,6,7,-7,-4,6,-7,3,-7,7,8,-5,-3,3,-2,-6,4,6,-3,-10,3,-10,-8,-4,8,5,5,2,2,5,-8,2,-4,-5,-1,-4,4,-7,-9,-7,2,2,3,-7,-9,-10,-5,3,9,6,5,-4,-6,-1,-4,9,-2,5,-4,10,-7,2,-1,1,3], dtype = "int16")#candidate|4688|(108,)|const|int16
call_4685 = relay.TupleGetItem(func_2856_call(relay.reshape(call_4672.astype('float64'), [24, 22]), relay.reshape(const_4686.astype('uint8'), [88,]), relay.reshape(var_4687.astype('uint32'), [40,]), relay.reshape(const_4688.astype('int16'), [3, 36]), ), 5)
call_4689 = relay.TupleGetItem(func_2862_call(relay.reshape(call_4672.astype('float64'), [24, 22]), relay.reshape(const_4686.astype('uint8'), [88,]), relay.reshape(var_4687.astype('uint32'), [40,]), relay.reshape(const_4688.astype('int16'), [3, 36]), ), 5)
output = relay.Tuple([call_4672,call_4685,const_4686,var_4687,const_4688,])
output2 = relay.Tuple([call_4673,call_4689,const_4686,var_4687,const_4688,])
func_4730 = relay.Function([var_4687,], output)
mod['func_4730'] = func_4730
mod = relay.transform.InferType()(mod)
mutated_mod['func_4730'] = func_4730
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4731 = relay.var("var_4731", dtype = "uint32", shape = (40,))#candidate|4731|(40,)|var|uint32
func_4730_call = mutated_mod.get_global_var('func_4730')
call_4732 = func_4730_call(var_4731)
output = call_4732
func_4733 = relay.Function([var_4731], output)
mutated_mod['func_4733'] = func_4733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3873_call = mod.get_global_var('func_3873')
func_3874_call = mutated_mod.get_global_var('func_3874')
call_4737 = relay.TupleGetItem(func_3873_call(), 2)
call_4738 = relay.TupleGetItem(func_3874_call(), 2)
func_3112_call = mod.get_global_var('func_3112')
func_3114_call = mutated_mod.get_global_var('func_3114')
call_4740 = relay.TupleGetItem(func_3112_call(), 0)
call_4741 = relay.TupleGetItem(func_3114_call(), 0)
output = relay.Tuple([call_4737,call_4740,])
output2 = relay.Tuple([call_4738,call_4741,])
func_4742 = relay.Function([], output)
mod['func_4742'] = func_4742
mod = relay.transform.InferType()(mod)
output = func_4742()
func_4743 = relay.Function([], output)
mutated_mod['func_4743'] = func_4743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_4759 = relay.TupleGetItem(func_1634_call(), 0)
call_4760 = relay.TupleGetItem(func_1636_call(), 0)
const_4768 = relay.const([[[-8.208688,-6.872644,-0.737701,-0.510611,-4.930726,-8.207594,-9.243934],[6.565996,-7.758734,-8.237858,9.726460,-1.928172,-4.688089,4.525467],[-5.196983,-6.330171,-0.245608,-4.168597,3.658947,7.098175,2.255613],[6.882484,9.502481,-6.896881,4.518486,4.693761,4.428051,1.840847],[4.764512,-4.332080,1.085058,-7.620009,-6.197002,5.332921,1.698026],[5.568927,-9.365621,-0.786987,6.042941,-7.884407,-0.699128,-6.278779],[8.692155,5.813389,-4.863655,-0.020792,1.053671,5.686157,2.882846],[3.001869,5.447724,3.151909,-1.465461,7.158338,-7.439759,-1.988681],[3.448240,9.090461,-2.681643,4.618361,-0.555419,2.589231,-2.894838],[9.131209,5.239777,-7.967513,3.485415,-0.290557,-4.707079,-5.687988],[1.174597,2.094151,9.429320,5.863234,8.362111,-7.073766,-0.467994],[9.502478,-2.616818,-3.218480,-5.752665,-2.906469,-2.479006,1.734450],[-1.757565,-5.929162,-5.443303,-1.559017,-7.625412,-6.641582,9.726639],[2.209206,-5.919534,-2.005230,-6.613370,-2.936358,-6.099508,-3.539934],[9.923120,8.619925,2.391989,-9.374813,8.280538,4.578457,-9.135933],[3.380642,-3.477651,-0.082809,-7.683882,4.626763,1.013292,5.727779]],[[-5.917537,8.886893,3.731661,2.136480,-6.108306,-5.922108,6.455452],[5.105715,0.612188,2.460117,1.360685,-7.610886,-6.145246,-7.303101],[6.556765,0.080507,-1.572231,-1.978980,8.161623,-0.021334,5.962152],[3.525197,9.128487,-2.026980,-0.361739,-0.815519,5.927403,9.815631],[6.897389,-3.500687,4.244278,-3.442013,-8.031940,1.912682,4.031329],[7.526016,-8.263532,5.012287,3.579340,1.916519,8.451244,5.067016],[-3.078855,-3.477638,2.600082,2.570316,9.829034,-2.058758,-0.375541],[9.320124,6.344455,-1.943648,-3.600302,8.064369,7.155503,3.818400],[9.704865,-5.484935,1.410412,6.704777,8.755575,2.943595,-0.064879],[-9.957861,6.599366,-6.705849,-3.637592,-3.129952,-8.727780,-7.657979],[-4.397191,-8.332252,-1.623016,-7.598504,-0.592994,-0.070932,-6.630790],[-0.243660,8.689845,5.844124,-7.724477,-6.737510,-0.433555,7.878237],[-4.665656,-8.075917,7.572475,-8.615750,1.362370,4.275687,-3.316698],[9.989840,2.927405,-2.862569,-4.350524,2.010206,8.759693,2.757457],[6.623579,6.286933,-8.999070,-8.608078,-6.304150,-5.991722,1.430822],[7.363517,7.685385,-0.699045,-4.478820,-3.941021,-4.140901,-5.552315]],[[7.635222,8.903867,-4.085889,-3.609465,9.129206,2.704200,-4.984528],[2.576008,9.435115,8.988304,-7.416960,-4.761158,-6.086763,3.408195],[-6.655239,6.480144,-7.192426,-1.019324,9.959140,9.185483,-4.557795],[-8.735009,-0.037286,-5.988683,7.717976,2.519449,-7.937975,-7.557374],[-3.765966,1.007969,1.161639,-2.728595,-8.369527,3.729226,7.120067],[-5.741530,9.550672,-1.092001,-5.781498,3.960737,8.380110,5.448215],[-1.291691,-9.268872,-9.752200,-9.694357,-0.273217,7.773203,4.537772],[-0.760563,6.457316,-0.322044,-7.206867,1.874879,-3.541582,-7.793566],[2.148975,8.701483,4.640785,-7.938007,7.958169,-0.006800,7.326791],[-0.537966,-2.094285,3.794906,7.568452,-4.515784,3.559458,1.676139],[-8.264965,7.391729,2.353136,-7.364732,-1.761941,-3.188943,2.043563],[-3.966102,-6.473630,9.472356,4.199318,0.396871,8.117100,-1.975292],[7.407770,-8.147824,1.863191,3.707986,-1.091583,-4.402061,-5.457234],[-6.910890,0.411220,-1.192979,-4.763521,-9.799512,-6.760756,-5.754824],[6.726699,-8.222156,-3.099430,-0.928785,-4.675380,3.895448,0.972286],[-1.076641,-0.669666,5.811207,2.199335,-0.201399,-9.870995,2.767446]],[[-1.027045,-4.872586,6.620618,-2.253559,1.419320,9.471962,-8.407966],[-3.222326,-0.473545,3.689840,3.840490,-8.605408,-8.906062,-1.352711],[4.456178,1.998339,-6.650353,5.337326,5.924238,7.689547,4.482744],[-4.635081,0.892688,6.785002,2.385332,5.913830,-3.143188,3.111878],[-5.498595,3.800240,-3.053292,8.743948,-2.753249,-6.325846,-1.785031],[-8.303110,-1.538070,1.666653,0.143360,-3.670631,4.883150,7.739928],[5.421075,-0.691673,0.098623,-9.773496,-7.002056,-9.190623,-7.905410],[-0.033465,-5.691648,-3.789382,-9.631536,8.708491,7.360429,-4.436364],[5.890431,-6.852366,1.782811,-1.958834,-5.508595,-9.236368,-1.067883],[8.994670,6.428153,1.474189,-4.580071,-2.164009,8.159769,-7.319990],[0.697352,1.559883,-5.018441,-2.153122,-7.705339,-1.279014,4.107357],[3.734184,3.196242,-9.105684,3.623077,6.358781,-8.801462,-7.067659],[7.696766,-3.046986,1.991192,2.514071,3.331620,6.718889,-3.519010],[-7.708227,-4.132611,3.802406,-1.514170,-3.486562,2.386505,7.087017],[-9.784922,9.958879,-4.225307,-1.346752,3.910042,2.030017,4.325178],[-6.494647,6.195593,6.106260,-5.333695,0.569626,7.870409,-2.009967]],[[4.424964,-1.427486,9.762460,9.310619,9.391671,-5.273078,9.775224],[0.544038,-8.504734,-7.519357,-1.293437,-1.761100,-8.729463,1.908004],[4.878525,-4.068471,5.375036,-4.207657,-1.422663,-6.071859,-1.888892],[-0.633441,-8.401701,-7.499939,1.598517,-8.407339,6.379362,8.124831],[2.213956,3.525209,-5.432559,3.377637,-1.607008,1.039141,-1.600513],[-0.559419,-7.040430,-3.843916,-8.593172,4.129094,-8.964633,7.538575],[-2.268535,7.312869,0.312672,2.675080,5.568258,5.777898,-9.416230],[-0.176315,-7.959567,9.880987,-3.026027,3.398039,6.680434,-2.470123],[5.252744,1.498286,-2.263392,3.182801,3.609608,-1.791058,1.031162],[-9.592032,-7.916555,-2.707608,2.717241,8.125358,-9.082510,-3.633241],[3.069239,2.611922,-9.046599,6.572188,2.814434,-8.795819,9.732362],[8.196864,-4.735291,-5.123716,2.713549,1.822644,3.669362,-2.922515],[9.193144,7.105038,6.220433,7.944121,2.768401,1.186044,3.021879],[7.528310,-8.634555,-0.667298,-1.141473,7.966535,7.319710,-1.155893],[4.003080,-3.577233,7.486821,9.638308,-6.888287,-4.806144,2.701803],[7.519761,5.740249,6.646335,5.611727,-1.344368,8.769201,9.785117]],[[-6.768407,0.843771,-5.266816,-8.273368,8.794050,1.538847,3.498120],[7.572786,2.921197,9.173343,1.726136,-6.533883,-2.039416,-8.886673],[-4.727671,9.370924,6.189527,-6.769241,-7.184245,9.397585,-7.623805],[-5.530708,-7.303201,1.375155,-9.003903,-3.082999,3.163224,-1.277671],[6.426650,8.246305,4.882941,-4.416948,7.353196,-4.498966,0.996990],[5.320596,-8.931532,2.392944,1.024169,-1.627271,-3.008368,5.875004],[9.215738,1.675780,-6.292324,-2.366196,0.004679,-2.622755,3.175661],[6.387861,-7.778537,4.176464,-7.061244,1.548703,5.272503,8.817293],[-1.921700,4.191305,-1.688008,-4.853910,-0.514742,-3.120406,6.180348],[-4.803148,-2.381958,-3.727057,1.828110,1.741029,-5.037245,9.173681],[8.189013,3.781097,-1.800093,3.528027,-4.264790,6.653399,5.122394],[-5.933868,8.913382,3.545566,-9.460958,-1.720790,3.877115,0.044325],[7.550434,2.521060,9.593642,-9.770852,-3.113288,6.869918,-5.552584],[1.755840,-0.743179,-2.778304,-2.734607,0.596944,0.581988,-9.630298],[-6.793346,5.434265,6.792622,-3.837706,0.821405,-9.998472,-0.377526],[-0.859787,-5.732869,-8.859984,-2.264299,-6.087090,0.559634,4.516243]],[[-3.424186,6.547680,-5.838954,-4.808621,-1.178320,-6.779029,9.312986],[4.560368,-0.992767,-1.721238,9.668982,-7.219723,-9.260105,-1.960265],[-4.024449,-9.977746,-0.039591,9.035801,-4.396715,-3.033212,-1.604552],[9.721127,5.025265,-2.826492,-8.655630,-8.464249,3.573300,5.300349],[-2.972044,3.791166,-9.582064,6.864842,-9.268149,7.014825,-7.856954],[8.991476,-9.760664,-3.577375,6.910831,-4.586348,-4.211518,4.937396],[6.195164,0.040678,-0.775594,-4.594150,-9.180405,4.966825,6.048746],[-9.911475,-9.563736,-6.508777,-5.912842,-3.260191,9.559822,7.081648],[-5.728760,-9.217092,-7.780817,4.541138,-2.327787,6.430738,9.511153],[1.197687,4.678875,-8.583888,3.275758,-1.480380,2.192047,8.062500],[1.200068,-8.770798,2.570110,1.439687,-9.734533,6.883426,2.806415],[-4.941507,7.564458,2.144499,7.764895,7.041467,-3.389611,-1.365237],[-0.368284,5.149913,-1.537603,5.236606,-7.921875,4.056468,0.521198],[2.955722,2.665242,2.102425,-5.471204,8.245546,-7.949973,-5.784663],[0.117122,2.005516,1.528945,6.501158,-2.453523,0.576648,-7.065098],[-4.747588,4.586424,-1.928897,2.840662,-4.848231,-7.546704,6.553591]],[[-1.008624,1.620942,-4.544781,9.321127,6.515002,3.680523,-3.950232],[-3.839223,-7.490029,-9.692198,8.232131,-8.549244,6.111578,-9.786140],[8.448042,-1.069077,8.564643,8.122314,-5.049021,4.151973,6.484154],[-7.507986,-8.673683,-8.879641,8.588732,-2.631719,2.895861,5.538526],[3.345287,-1.652144,7.339401,-6.950971,9.894134,-3.304998,3.454329],[6.385427,-0.456153,-4.895210,5.104800,9.764313,6.724092,4.151801],[9.166216,9.966201,-1.162834,2.276244,5.535538,-3.261943,6.749854],[-4.070440,6.624352,1.731913,5.542558,-5.241078,2.541093,2.278893],[4.008288,4.621137,0.100836,-7.767391,3.117801,9.925183,7.212016],[0.137903,-3.959830,1.584820,8.415475,-7.095598,-5.550476,7.806916],[-5.691665,8.409420,1.391665,-6.169564,3.367826,-9.556707,-9.781105],[3.205109,-9.259124,-9.068675,7.679604,-6.914736,9.329358,4.228403],[7.299869,4.020288,-1.122657,8.686471,4.945007,-4.568251,-2.093192],[4.810130,0.429997,8.350717,4.736942,-1.344515,4.716680,-1.148991],[4.523454,7.262251,-3.191079,3.685433,0.841169,5.545617,-8.309161],[9.464764,-8.745097,-3.424277,-0.079297,2.502399,2.882019,-0.318634]],[[-2.862183,1.894252,-7.386395,-7.607248,1.992815,6.406222,4.245331],[-0.589763,0.752919,-6.858498,-2.167378,6.447060,-7.413525,8.591986],[-3.935550,1.970112,-5.388253,9.447941,7.648410,6.237384,3.549373],[9.385525,4.814564,-0.753571,5.894280,4.225932,2.574570,-7.066887],[4.465637,-3.266783,5.740675,4.033807,-3.075843,1.681677,-2.311191],[4.277732,1.430622,-3.788852,-9.743438,5.153028,-1.830667,3.677141],[2.461040,8.157818,3.545427,2.232703,9.121383,-0.421968,0.360765],[7.663762,2.252242,1.294609,8.681525,4.826701,-2.358721,-0.177663],[8.090277,1.518341,8.228448,-5.130638,-9.235604,-9.546738,-0.552623],[9.443334,-5.026707,2.058078,3.195226,-4.125626,9.839288,-5.409716],[3.607366,-7.078418,8.819642,8.454391,-0.007831,7.562142,0.340366],[4.866882,9.174414,6.251471,9.850124,7.899523,5.587011,-7.157778],[2.111099,4.256798,7.672586,-9.984688,6.008691,4.588141,2.585220],[-2.016531,-5.266056,-9.665995,-5.089894,0.947923,-5.645385,3.298114],[4.265011,-2.697112,-1.135905,2.067112,9.797127,-3.722659,1.548904],[7.542340,2.305629,-7.507030,7.994082,5.230613,-9.286179,2.067596]],[[9.655506,1.221957,-8.296434,7.892452,4.637395,-0.070137,-3.557185],[8.183661,9.541639,-4.470420,-6.788515,-9.617166,9.637527,6.278057],[6.178959,0.801634,6.755240,9.228907,-5.279698,3.537169,5.376106],[3.528917,-5.248816,9.957643,5.944760,-1.896412,-2.769244,1.677862],[-9.540200,-3.116982,1.954031,-2.080439,-3.688941,9.444361,8.781132],[-0.106928,-1.149907,-9.762430,-4.295028,-5.752987,-2.074054,9.643970],[-4.409507,-7.387938,2.314596,-4.578323,-3.376954,-3.070884,-9.349884],[-5.317750,-8.199853,-2.449010,-7.840278,0.683185,-3.266726,-2.685919],[3.493392,-0.750874,-6.004783,-1.458914,0.111645,-8.240464,-4.772593],[-1.570408,-6.145937,-4.281685,8.899711,-3.222134,9.035957,-3.512898],[7.729733,-7.057932,-7.476992,-5.121173,-6.965886,-5.577841,3.900920],[0.813839,8.123401,-7.216209,-4.546920,-1.035325,5.282498,7.348620],[6.665520,7.418923,-7.615477,2.140963,-8.400991,4.524630,-0.830906],[-4.316851,3.048316,9.053664,9.314263,-1.117485,-1.028827,3.931135],[2.694441,0.312966,-3.285546,-1.637780,-5.835767,0.096272,1.476410],[0.632018,-4.331574,-3.042212,-3.687384,6.978288,6.184760,9.319460]]], dtype = "float32")#candidate|4768|(10, 16, 7)|const|float32
bop_4769 = relay.power(call_4759.astype('float64'), const_4768.astype('float64')) # shape=(10, 16, 7)
bop_4772 = relay.power(call_4760.astype('float64'), const_4768.astype('float64')) # shape=(10, 16, 7)
output = relay.Tuple([bop_4769,])
output2 = relay.Tuple([bop_4772,])
func_4775 = relay.Function([], output)
mod['func_4775'] = func_4775
mod = relay.transform.InferType()(mod)
mutated_mod['func_4775'] = func_4775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4775_call = mutated_mod.get_global_var('func_4775')
call_4776 = func_4775_call()
output = call_4776
func_4777 = relay.Function([], output)
mutated_mod['func_4777'] = func_4777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1756_call = mod.get_global_var('func_1756')
func_1757_call = mutated_mod.get_global_var('func_1757')
call_4790 = func_1756_call()
call_4791 = func_1756_call()
var_4798 = relay.var("var_4798", dtype = "float64", shape = (3, 11, 16))#candidate|4798|(3, 11, 16)|var|float64
bop_4799 = relay.power(call_4790.astype('float64'), relay.reshape(var_4798.astype('float64'), relay.shape_of(call_4790))) # shape=(3, 11, 16)
bop_4802 = relay.power(call_4791.astype('float64'), relay.reshape(var_4798.astype('float64'), relay.shape_of(call_4791))) # shape=(3, 11, 16)
bop_4807 = relay.multiply(bop_4799.astype('uint64'), relay.reshape(call_4790.astype('uint64'), relay.shape_of(bop_4799))) # shape=(3, 11, 16)
bop_4810 = relay.multiply(bop_4802.astype('uint64'), relay.reshape(call_4791.astype('uint64'), relay.shape_of(bop_4802))) # shape=(3, 11, 16)
func_3873_call = mod.get_global_var('func_3873')
func_3874_call = mutated_mod.get_global_var('func_3874')
call_4821 = relay.TupleGetItem(func_3873_call(), 0)
call_4822 = relay.TupleGetItem(func_3874_call(), 0)
func_3947_call = mod.get_global_var('func_3947')
func_3950_call = mutated_mod.get_global_var('func_3950')
var_4831 = relay.var("var_4831", dtype = "float64", shape = (5, 30))#candidate|4831|(5, 30)|var|float64
call_4830 = relay.TupleGetItem(func_3947_call(relay.reshape(var_4831.astype('float64'), [2, 15, 5])), 3)
call_4832 = relay.TupleGetItem(func_3950_call(relay.reshape(var_4831.astype('float64'), [2, 15, 5])), 3)
func_4213_call = mod.get_global_var('func_4213')
func_4214_call = mutated_mod.get_global_var('func_4214')
call_4841 = func_4213_call()
call_4842 = func_4213_call()
var_4843 = relay.var("var_4843", dtype = "float64", shape = (10, 16, 7))#candidate|4843|(10, 16, 7)|var|float64
bop_4844 = relay.less_equal(call_4821.astype('bool'), var_4843.astype('bool')) # shape=(10, 16, 7)
bop_4847 = relay.less_equal(call_4822.astype('bool'), var_4843.astype('bool')) # shape=(10, 16, 7)
uop_4849 = relay.atanh(var_4831.astype('float32')) # shape=(5, 30)
func_1692_call = mod.get_global_var('func_1692')
func_1694_call = mutated_mod.get_global_var('func_1694')
call_4851 = func_1692_call()
call_4852 = func_1692_call()
output = relay.Tuple([bop_4807,call_4830,call_4841,bop_4844,uop_4849,call_4851,])
output2 = relay.Tuple([bop_4810,call_4832,call_4842,bop_4847,uop_4849,call_4852,])
func_4856 = relay.Function([var_4798,var_4831,var_4843,], output)
mod['func_4856'] = func_4856
mod = relay.transform.InferType()(mod)
var_4857 = relay.var("var_4857", dtype = "float64", shape = (3, 11, 16))#candidate|4857|(3, 11, 16)|var|float64
var_4858 = relay.var("var_4858", dtype = "float64", shape = (5, 30))#candidate|4858|(5, 30)|var|float64
var_4859 = relay.var("var_4859", dtype = "float64", shape = (10, 16, 7))#candidate|4859|(10, 16, 7)|var|float64
output = func_4856(var_4857,var_4858,var_4859,)
func_4860 = relay.Function([var_4857,var_4858,var_4859,], output)
mutated_mod['func_4860'] = func_4860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1593_call = mod.get_global_var('func_1593')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_4881 = func_1593_call()
call_4882 = func_1593_call()
output = relay.Tuple([call_4881,])
output2 = relay.Tuple([call_4882,])
func_4883 = relay.Function([], output)
mod['func_4883'] = func_4883
mod = relay.transform.InferType()(mod)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mutated_mod.get_global_var('func_4883')
call_4884 = func_4883_call()
output = call_4884
func_4885 = relay.Function([], output)
mutated_mod['func_4885'] = func_4885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4119_call = mod.get_global_var('func_4119')
func_4121_call = mutated_mod.get_global_var('func_4121')
call_4894 = relay.TupleGetItem(func_4119_call(), 2)
call_4895 = relay.TupleGetItem(func_4121_call(), 2)
func_4047_call = mod.get_global_var('func_4047')
func_4048_call = mutated_mod.get_global_var('func_4048')
call_4910 = relay.TupleGetItem(func_4047_call(), 0)
call_4911 = relay.TupleGetItem(func_4048_call(), 0)
output = relay.Tuple([call_4894,call_4910,])
output2 = relay.Tuple([call_4895,call_4911,])
func_4916 = relay.Function([], output)
mod['func_4916'] = func_4916
mod = relay.transform.InferType()(mod)
output = func_4916()
func_4917 = relay.Function([], output)
mutated_mod['func_4917'] = func_4917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4047_call = mod.get_global_var('func_4047')
func_4048_call = mutated_mod.get_global_var('func_4048')
call_4923 = relay.TupleGetItem(func_4047_call(), 0)
call_4924 = relay.TupleGetItem(func_4048_call(), 0)
output = call_4923
output2 = call_4924
func_4936 = relay.Function([], output)
mod['func_4936'] = func_4936
mod = relay.transform.InferType()(mod)
mutated_mod['func_4936'] = func_4936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4936_call = mutated_mod.get_global_var('func_4936')
call_4937 = func_4936_call()
output = call_4937
func_4938 = relay.Function([], output)
mutated_mod['func_4938'] = func_4938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4742_call = mod.get_global_var('func_4742')
func_4743_call = mutated_mod.get_global_var('func_4743')
call_4947 = relay.TupleGetItem(func_4742_call(), 1)
call_4948 = relay.TupleGetItem(func_4743_call(), 1)
output = call_4947
output2 = call_4948
func_4951 = relay.Function([], output)
mod['func_4951'] = func_4951
mod = relay.transform.InferType()(mod)
output = func_4951()
func_4952 = relay.Function([], output)
mutated_mod['func_4952'] = func_4952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1605_call = mod.get_global_var('func_1605')
func_1606_call = mutated_mod.get_global_var('func_1606')
call_4971 = relay.TupleGetItem(func_1605_call(), 0)
call_4972 = relay.TupleGetItem(func_1606_call(), 0)
func_3249_call = mod.get_global_var('func_3249')
func_3254_call = mutated_mod.get_global_var('func_3254')
var_4978 = relay.var("var_4978", dtype = "int32", shape = (1400,))#candidate|4978|(1400,)|var|int32
var_4979 = relay.var("var_4979", dtype = "uint32", shape = (2, 20))#candidate|4979|(2, 20)|var|uint32
call_4977 = relay.TupleGetItem(func_3249_call(relay.reshape(var_4978.astype('int32'), [10, 14, 10]), relay.reshape(var_4978.astype('int32'), [10, 14, 10]), relay.reshape(var_4979.astype('uint32'), [40, 1]), ), 5)
call_4980 = relay.TupleGetItem(func_3254_call(relay.reshape(var_4978.astype('int32'), [10, 14, 10]), relay.reshape(var_4978.astype('int32'), [10, 14, 10]), relay.reshape(var_4979.astype('uint32'), [40, 1]), ), 5)
func_3577_call = mod.get_global_var('func_3577')
func_3580_call = mutated_mod.get_global_var('func_3580')
const_4982 = relay.const([7,-2,-8,-1,-6,1,-3,-7,1,-2,10,4,-6,-2,-4,-1,-4,4,-10,4,5,3,4,-1,-1,-9,-8,-1,-6,1,1,-9,-4,9,-7,1,8,-2,-3,9,-9,7,1,-4,-10,-7,8,7], dtype = "int32")#candidate|4982|(48,)|const|int32
call_4981 = relay.TupleGetItem(func_3577_call(relay.reshape(const_4982.astype('int32'), [48,])), 0)
call_4983 = relay.TupleGetItem(func_3580_call(relay.reshape(const_4982.astype('int32'), [48,])), 0)
const_4989 = relay.const([6,1,-1,-7,-4,7,-4,-10,4,-10,-1,4,-6,-9,1,-4,-1,5,7,-5,1,-1,-2,9,6,1,-8,-7,7,1,7,8,-2,1,5,10,-7,2,2,5,5,-5,2,-7,-9,10,-8,3,-1,9,2,5,10,1,1,10,-4,10,9,7,-10,4,-5,-7,-5,6,6,7,9,10,3,-9,-4,-3,10,1,-4,7,-5,-10,1,-8,-7,6,10,-7,5,10,-7,-4,-10,7,1,-7,-8,-9,-1,9,9,-4,-1,-3,-9,6,5,-4,-5,1,5,-4,-5,4,-7,5,-10,6,2,-8,10,10,5,2,-3,8,3,2,5,3,1,-10,7,-10,5,3,-3,-3,-4,-8,8,-6,-8,-8,-4,-6,8,-4,2,-5,4,-4,-10,-5,2,3,7,-10,8,7,8,7,-9,-3,8,10,6,1,1,-10,9,-2,3,-1,-9,-2,-2,-2,-3,2,3,-3,7,6,-8,-2,2,-3,-7,7,-5,-2,-10,-7,-1,2,2,6,-9,-7,1,-4,-5,-7,3,8,-2,4,7,5,-2,-4,4,4,-2,-10,2,5,5,10,5,8,10,-1,5,7,-5,-2,2,-4,-10,-7,-10,-2,4,5,-1,9,4,10,-8,-5,-9,5,4,6,-4,8,3,1,1,-9,6,4,9,-7,1,3,-10,3,-8,10,10,-5,8,-2,-9,-3,-8,5,1,6,6,3,-8,2,5,-5,9,-10,8,-8,-5,-4,-8,-10,-2,4,-6,6,5,-7,7,5,-5,-5,-9,10,1,-6,-2,1,-5,-4,2,-6,-5,7,-6,-1,9,2,6,1,7,-10,8,-4,4,5,-7,5,3,-7,-4,9,-2,-9,-4,-10,2,9,9,4,-3,-3,9,2,8,2,-8,3,-2,10,7,-7,10,-8,1,-4,10,-5,-3,-10,8,3,2,8,10,-2,-8,5,-6,6,-2,2,-10,-10,3,4,-3,7,-4,-9,-3,-1,-9,8,7,3,-6,3,1,9,-5,-7,-1,-4,-9,9,-4,-2,7,10,-4,5,-7,6,-4,-4,-7,9,-5,-2,8,8,-2,-6,-10,2,9,-6,8,6,6,-2,1,10,6,10,-3,-7,9,-3,10,-7,-3,-7,6,2,3,4,5,2,3,-5,-2,-1,-8,2,-8,-8,3,-3,-9,10,10,10,7,9,3,6,10,6,2,5,8,-2,-9,1,-3,-3,-6,-10,-2,5,-7,-1,-8,3,7,-1,-1,10,-9,9,-4,5,-5,5,8,-3,10,-1,2,-8,2,-8,4,5,8,5,8,4,-9,-1,6,1,9,-4,-6,2,4,2,-7,-1,-1,-9,-10,-2,-9,-5,6,-10,-8,6,9,-1,-9,2,8,-10,-2,9,9,1,2,-2,-2,3,-7,3,8,-10,4,10,-7,-2,1,-1,3,-8,-9,-5,-5,2,-7,9,-6,-10,-2,4,-3,10,-8,-4,-4,5,-7,6,-9,3,3,3,4,2,8,-7,2,6,-8,-2,5,8,10,-3,4,8,9,-9,-7,-10,8,-5,-5,-2,-1,7,-2,7,1,-2,7,4,-1,10,-5,10,-2,-6,6,-1,-2,3,5,7,-2,-3,-1,7,-2,-8,1,-2,3,-9,-6,5,1,4,-10,4,-2,-4,-5,-4,10,-4,2,-4,-4,5,3,7,-10,10,2,3,-2,-8,8,4,6,8,3,-4,-5,6,10,2,6,9,7,-5,-1,-7,-5,-8,8,10,10,-10,-2,2,4,2,-7,8,-5,4,6,-6,2,-3,-1,-4,6,5,2,9,-1,-6,2,-4,-8,4,2,6,-3,6,1,-5,6,2,7,-6,4,9,-7,-4,3,-9,-7,1,-4,-4,-7,-10,6,2,7,4,-9,7,5,-1,9,-5,6,6,3,5,-6,-2,8,8,2,-7,4,-7,7,-7,-9,-5,-8,-5,1,-10,4,1,-8,9,2,10,-2,-5,4,-5,6,-6,-1,5,10,10,7,-9,-2,-4,-6,10,-1,7,9,-8,2,-9,-6,6,10,-1,-7,4,9,-4,4,3,9,3,-1,-2,9,-7,-8,3,7,8,4,-5,-2,2,-3,3,4,-9,-9,8,-4,2,-8,-1,9,-10,3,-10,4,-1,6,8,-10,-4,8,8,9,-6,-5,3,-6,10,10,-4,-3,-3,9,-8,-8,1,-6,-2,8,-1,4,-8,-9,-10,10,5,-9,10,-10,10,-3,-8,9,-2,-5,-2,7,9,-8,-4,5,2,8,3,-4,-5,-5,4,2,-2,8,-6,-4,10,-4,-2,6,4,-10,9,1,9,-9,-1,-8,6,7,-3,-6,4,-9,-10,4,6,-10,-6,-1,8,-7,-8,4,-2,-5,3,-8,-5,7,2,1,3,-3,4,-5,3,-3,-10,-5,7,5,-5,-9,10,8,-5,-1,2,-1,-9,9,10,-1,9,3,9,-6,-3,-5,-10,6,-3,8,-1,2,-5,10,-2,-8,-10,-9,-10,-3,1,-5,-4,10,8,-3,-7,8,5,-9,-2,10,-9,1,5,2,4,8,-10,5,4,-6,-10,-3,4,-6,3,6,-6,-3,3,-6,5,-6,2,-1,-7,7,1,6,6,-2,7,-2,7,1,-1,8,1,-8,-5,-9,-8,-4,10,6,10,-4,-6,-10,-2,-6,10,-8,7,-5,-7,-7,-5,-3,8,1,-9,-7,-1,-9,-9,-5,-8,3,-9,10,-5,10,-5,-4,-4,5,10,-8,8,-4,-2,-8,-2,-8,1,6,4,-5,8,-3,4,4,9,-9,-1,6,3,-6,6,5,-3,-3,-4,-5,8,5,-8,-10,-2,6,3,9,-9,-1,10,-2,5,-7,4,1,1,-7,-4,-8,5,10,-7,4,-3,-10,-8,-5,10,4,-7,7,3,-9,-3,5,-2,-6,3,4,4,10,-8,7,-10,-3,9,5,6,-1,10,4,3,10,1,-6,1,7,3,-9,-6,-10,-4,9,8,6,-7,1,-2,8,6,-8,-9,8,10,7,-10,5,3,-4,5,10,-10,-4,1,-8,3,3,5,-8,-9,-5,3,4,3,8,6,1,-6,-10,4,-3,8,-3,-7,7,5,6,-1,5,-6,3,-8,10,9,2,-2,2,-2,10,-3,7,1,7,4,8,-2,6,7,-7,-7,-8,5,8,5,9,7,8,-9,-1,-7,-7,-2,-1,10,-3,-9,8,3,1,4,-5,-6,-8,-8,-10,-8,3,1,-8,4,-7,-4,-6,1,-4,7,-5,-2,8,3,-4,6,-2,-3,-5,2,1,7,3,-5,4,-6,-3,-3,8,-8,1,-2,-10,-3,-4,-6,-3,10,-2,2,-7,6,-7,-10,7,9,-3,-2,8,7,-2,-6,-6,2,-1,6,5,7,-1,8,8,-7,-8,3,4,-7,1,-3,10,-6,2,-1,4,-10,7,-4,-5,6,-9,1,-7,4,-2,6,4,4,-8,4,5,8,2,-6,4,-2,1,8,2,7,-1,-9,-8,5,-10,-7,-5,-8,8,3,6,-5,-7,-6,-7,6,-9,-2,-7,-3,8,-3,-7,-7,5,-7,5,9,-2,-2,9,6,-2,4,-7,-6,9,7,10,-2,-4,-5,8,-1,-8,-1,1,-4,-8,-2,-5,2,-10,1,3,-5,2,-5,4,3,1,9,-3,-6,-1,-6,9,-2,6,-8,-7,-5,-5,-1,10,-10,-10,-2,-4,-4,7,1,9,-4,7,4,-9,4,3,2], dtype = "int32")#candidate|4989|(1400,)|const|int32
bop_4990 = relay.left_shift(var_4978.astype('int16'), relay.reshape(const_4989.astype('int16'), relay.shape_of(var_4978))) # shape=(1400,)
func_1191_call = mod.get_global_var('func_1191')
func_1195_call = mutated_mod.get_global_var('func_1195')
var_4997 = relay.var("var_4997", dtype = "uint8", shape = (280, 1))#candidate|4997|(280, 1)|var|uint8
call_4996 = relay.TupleGetItem(func_1191_call(relay.reshape(var_4997.astype('uint8'), [10, 14, 2]), relay.reshape(var_4997.astype('uint8'), [10, 14, 2]), ), 1)
call_4998 = relay.TupleGetItem(func_1195_call(relay.reshape(var_4997.astype('uint8'), [10, 14, 2]), relay.reshape(var_4997.astype('uint8'), [10, 14, 2]), ), 1)
uop_4999 = relay.sin(var_4997.astype('float32')) # shape=(280, 1)
uop_5011 = relay.rsqrt(uop_4999.astype('float32')) # shape=(280, 1)
uop_5027 = relay.sigmoid(uop_5011.astype('float32')) # shape=(280, 1)
output = relay.Tuple([call_4971,call_4977,var_4979,call_4981,const_4982,bop_4990,call_4996,uop_5027,])
output2 = relay.Tuple([call_4972,call_4980,var_4979,call_4983,const_4982,bop_4990,call_4998,uop_5027,])
func_5033 = relay.Function([var_4978,var_4979,var_4997,], output)
mod['func_5033'] = func_5033
mod = relay.transform.InferType()(mod)
var_5034 = relay.var("var_5034", dtype = "int32", shape = (1400,))#candidate|5034|(1400,)|var|int32
var_5035 = relay.var("var_5035", dtype = "uint32", shape = (2, 20))#candidate|5035|(2, 20)|var|uint32
var_5036 = relay.var("var_5036", dtype = "uint8", shape = (280, 1))#candidate|5036|(280, 1)|var|uint8
output = func_5033(var_5034,var_5035,var_5036,)
func_5037 = relay.Function([var_5034,var_5035,var_5036,], output)
mutated_mod['func_5037'] = func_5037
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5050 = relay.const([[[-4,-2,-2,9,-9,-9,8,-2,1],[-2,-4,-4,7,7,-5,7,1,2],[-8,-1,3,-9,-9,1,-8,7,-3],[-2,10,-8,-10,-2,4,4,6,-2],[-5,-1,6,6,-4,6,5,-10,7],[-8,4,-8,8,2,-5,-5,7,-7],[-10,5,-8,-1,-8,6,10,-4,7],[-3,-2,-9,9,-1,9,-9,3,-3],[4,-1,-7,-2,4,3,6,6,-3],[8,8,10,9,6,-3,2,5,4],[2,-2,1,-8,3,6,-9,-8,6],[-4,-7,-7,-3,10,4,-1,9,5],[-1,7,-6,-8,1,-2,7,-4,-8]],[[7,-1,9,-2,-2,-6,-10,-9,-8],[4,-10,5,-2,7,7,6,-7,2],[10,8,4,10,-8,-3,-4,4,9],[-5,2,-4,7,4,7,-2,7,-1],[-6,4,-10,2,-1,-7,8,1,3],[-10,7,4,7,1,8,4,2,9],[5,7,10,6,5,-9,-5,9,-10],[-6,-9,-2,8,2,-3,4,-10,4],[7,7,9,10,-4,6,2,-2,6],[9,-9,-7,-1,2,4,-3,-10,-2],[-6,-3,-1,-6,-10,5,4,1,6],[8,9,-9,8,3,-2,-8,-9,-1],[-9,-5,-7,6,-4,-3,-7,8,-2]],[[10,-6,-9,7,-7,8,7,6,6],[-2,-3,9,9,-8,1,-3,-2,-3],[-7,8,-9,3,6,9,1,4,2],[-9,-1,-7,6,3,-8,1,-1,9],[-7,-5,2,-3,-7,-8,-2,9,3],[-8,-7,1,9,1,10,9,6,8],[-10,-2,2,6,-6,-9,-3,10,-8],[-7,2,9,2,9,2,6,10,8],[6,6,-1,3,-2,5,-3,-6,-2],[6,3,-2,3,-6,3,-5,-2,-3],[7,-8,-8,-6,-7,7,-9,3,-10],[-6,2,8,-10,8,-5,4,8,1],[-4,8,-1,-3,2,2,-3,-7,-4]],[[2,-9,3,-3,7,8,-7,5,8],[-2,8,-8,-6,-3,-8,7,9,2],[1,1,-7,6,-5,-9,8,-3,5],[-9,4,1,8,-6,3,1,5,2],[2,6,-8,8,8,2,-3,-4,4],[-3,-5,-9,8,4,3,5,-3,-1],[-10,5,-2,-3,2,4,-5,8,7],[-8,-9,-8,8,8,-8,10,-9,6],[-6,6,8,-3,10,-1,-1,2,1],[4,5,9,-10,9,-6,1,-6,7],[1,-5,3,6,6,8,9,-7,4],[6,-6,5,4,1,5,3,2,-6],[5,1,-1,-9,10,3,-3,-8,-7]],[[-9,9,2,2,9,-5,-8,-7,2],[-7,6,-8,-1,-1,-7,10,-1,10],[2,-9,5,-3,4,4,-8,8,10],[5,8,8,8,3,-6,3,4,-8],[5,2,3,-7,6,-5,3,8,9],[7,4,7,3,-8,3,6,7,-9],[-3,-1,2,-7,-9,-6,-1,-6,-5],[4,4,-6,10,-4,1,9,-8,5],[8,6,-9,8,7,4,8,1,2],[6,1,-10,3,-6,-10,2,-7,7],[-1,5,-10,10,-8,9,-10,3,7],[4,1,-1,-5,10,1,5,4,-10],[10,2,2,-8,-10,-4,2,-7,9]],[[5,2,3,3,-7,-9,-1,6,-5],[-7,-1,-3,4,-2,-2,10,5,3],[7,-8,-4,1,4,-9,6,-3,10],[1,-5,4,3,3,8,-6,3,-1],[-10,2,-2,4,-4,-6,-5,8,-1],[5,8,4,5,5,5,-5,-10,9],[-8,1,-2,-8,-3,6,1,-8,1],[-7,3,6,-7,2,-10,1,-6,9],[7,-6,6,-4,5,-7,5,5,-7],[-5,4,4,-10,1,5,-3,-9,-5],[-1,5,-3,4,-8,6,-10,2,8],[-7,2,4,9,-2,-6,-5,-5,5],[-3,-6,6,8,10,-1,7,7,-5]],[[7,-8,-2,3,3,6,-6,7,-9],[3,-10,-7,-3,10,-2,-1,-10,-7],[3,-10,9,-6,-4,-8,-5,-2,4],[-7,-4,7,3,6,-6,6,4,-8],[1,-2,5,9,3,-7,1,-5,3],[2,9,7,-2,7,-8,-10,6,-5],[-4,-5,8,-5,7,5,-2,-6,-4],[8,-8,1,-7,7,5,-8,-8,5],[6,6,-9,-3,-7,-2,4,8,-5],[9,2,-7,8,7,10,-10,1,8],[-7,9,-4,7,-2,-1,6,9,6],[6,-1,9,-4,-8,5,4,-8,7],[5,1,9,-4,-4,6,9,3,6]],[[1,-1,6,6,-9,3,8,10,-7],[1,-7,-4,-4,-4,1,1,9,-3],[-1,4,-5,7,-7,1,9,7,9],[-8,2,-2,-1,9,8,-4,-10,8],[-5,9,4,-8,-3,7,-4,-5,-7],[1,3,-8,1,9,-10,9,1,-9],[-7,8,-2,2,-9,4,7,6,5],[-10,-7,8,-7,5,4,-5,-3,-2],[7,4,-2,-4,4,-10,5,5,-10],[-1,9,-7,2,-3,2,-1,-1,4],[3,-4,-7,8,-4,-6,-8,-3,3],[-2,-1,-3,2,1,8,7,-3,-2],[3,4,7,-6,-7,1,-1,8,-10]],[[5,4,5,3,-5,1,9,-9,3],[-5,10,10,-3,-6,2,-9,-8,-5],[4,3,6,-9,7,-2,-4,1,-8],[-7,3,1,9,-4,-2,8,-9,-5],[4,-4,4,5,-2,3,-9,-10,-4],[-10,2,10,5,7,-8,10,8,6],[9,-9,-10,-10,3,-3,-4,9,-9],[7,-6,9,-1,-9,3,1,9,-5],[-2,-9,-9,-3,-7,7,1,9,10],[-3,-7,10,-8,-5,10,-7,5,9],[-10,6,-7,3,-7,-7,-2,-8,5],[-10,8,1,5,10,1,5,4,-1],[4,-8,8,-10,8,-1,5,-5,9]],[[10,-1,8,-2,5,6,-6,2,3],[-9,-2,2,-7,7,1,7,1,-4],[2,-4,3,-5,-10,2,6,-8,-8],[2,-7,-7,-6,-2,2,10,3,3],[1,4,2,5,-7,6,3,-1,8],[1,-4,-5,-10,-2,-6,-10,2,8],[-9,-2,6,-2,-6,1,4,-10,-6],[7,-9,-2,6,1,7,-2,4,5],[-1,-1,3,-3,-4,5,9,8,3],[-2,-2,-6,4,-5,1,-10,-8,-3],[1,-8,-10,-4,7,4,10,8,1],[-10,2,-3,7,7,-2,-8,6,-7],[9,3,3,-5,-5,4,-6,1,2]],[[-3,7,8,-10,-4,2,-5,5,6],[-7,-1,-1,10,-1,-5,5,6,8],[3,8,-8,-9,1,1,1,8,4],[-7,9,3,3,-4,10,-2,-1,10],[-1,2,-2,1,3,-5,3,1,-4],[-7,-2,5,-10,5,-7,3,-4,2],[-8,-1,-6,-9,-2,10,5,-2,-6],[-9,6,-10,-8,3,-7,-10,-9,7],[-9,2,-7,7,10,6,-8,4,8],[-9,6,8,6,-8,9,2,-2,-1],[-9,-10,10,4,-1,-4,-2,-5,4],[2,1,4,-7,-10,-3,7,-9,-8],[3,9,-8,-4,5,-1,-3,8,4]],[[4,10,-10,4,2,4,-4,-2,2],[-5,2,-4,-8,5,10,8,1,-7],[9,-10,-7,-1,-3,4,-4,-10,1],[-7,-2,5,-10,-6,-10,-3,6,-2],[-8,-4,5,-6,6,-3,-9,-6,-1],[-3,-3,-3,5,2,1,-4,6,-2],[3,9,-2,-8,5,4,-4,-8,-9],[10,10,5,5,-10,7,-3,8,4],[8,-4,6,10,6,-7,-10,-1,8],[-2,7,-7,2,9,-3,1,-4,4],[-3,-10,-4,-4,-1,-7,-2,5,8],[6,-1,1,9,-5,7,3,-6,8],[9,6,-8,-10,-9,10,4,-7,-2]]], dtype = "int32")#candidate|5050|(12, 13, 9)|const|int32
var_5051 = relay.var("var_5051", dtype = "int32", shape = (12, 13, 9))#candidate|5051|(12, 13, 9)|var|int32
bop_5052 = relay.add(const_5050.astype('int32'), relay.reshape(var_5051.astype('int32'), relay.shape_of(const_5050))) # shape=(12, 13, 9)
bop_5082 = relay.bitwise_and(const_5050.astype('int64'), relay.reshape(bop_5052.astype('int64'), relay.shape_of(const_5050))) # shape=(12, 13, 9)
output = bop_5082
output2 = bop_5082
F = relay.Function([var_5051,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5051,], output2)
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
	relay.transform.DefuseOps(),
	relay.transform.SimplifyExpr(),
	relay.transform.InferType(),
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
