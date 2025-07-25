import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_1584 = relay.var("var_1584", dtype = "float32", shape = ())#candidate|1584|()|var|float32
var_1585 = relay.var("var_1585", dtype = "float32", shape = (1, 4, 7))#candidate|1585|(1, 4, 7)|var|float32
bop_1586 = relay.divide(var_1584.astype('float32'), var_1585.astype('float32')) # shape=(1, 4, 7)
output = bop_1586
output2 = bop_1586
func_1598 = relay.Function([var_1584,var_1585,], output)
mod['func_1598'] = func_1598
mod = relay.transform.InferType()(mod)
mutated_mod['func_1598'] = func_1598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1598_call = mutated_mod.get_global_var('func_1598')
var_1600 = relay.var("var_1600", dtype = "float32", shape = ())#candidate|1600|()|var|float32
var_1601 = relay.var("var_1601", dtype = "float32", shape = (1, 4, 7))#candidate|1601|(1, 4, 7)|var|float32
call_1599 = func_1598_call(var_1600,var_1601,)
output = call_1599
func_1602 = relay.Function([var_1600,var_1601,], output)
mutated_mod['func_1602'] = func_1602
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1694 = relay.const([[[-8.795001,-7.983032,-3.547541],[6.410310,2.593560,-7.414054],[-0.030691,-9.432619,-8.777082],[-9.575950,-2.219968,7.412903],[-5.429123,0.327041,9.423069],[-6.228149,2.870530,9.152126],[8.545333,-5.055373,4.554939],[8.369666,-8.217097,1.045262],[-8.893732,9.971574,-1.127285],[-9.173759,-0.021403,-1.784858],[-5.329201,0.098572,-5.679972],[-7.529901,4.791035,-7.065167],[6.877250,6.036570,9.973875],[-6.414925,-2.367430,8.168105]],[[2.545638,4.473832,6.553901],[7.522956,-0.214641,6.133220],[-3.683853,-2.128357,-0.020113],[-6.915230,5.175989,-6.959954],[-5.942422,-6.119432,-2.160690],[9.319801,9.405509,3.114724],[2.280075,-2.773514,7.736900],[-8.779103,7.190354,0.752984],[0.476756,-1.000022,0.836568],[0.839695,3.533507,-4.238999],[9.419575,1.299477,0.346784],[0.311294,-8.195778,-9.606652],[1.336135,9.293766,-7.538799],[4.610097,-2.441440,-9.308990]],[[-6.628615,6.890323,8.058540],[2.825643,4.205891,5.727355],[0.337710,3.588807,-6.615327],[3.134464,-4.788533,8.006642],[2.291369,-2.584029,-7.392153],[-7.912182,4.237121,-5.859175],[7.833481,3.700583,0.791448],[4.935064,-7.907558,-8.745306],[5.975453,-5.781642,-3.686329],[-4.138708,-6.173798,7.926268],[6.442148,2.024804,0.493668],[1.897695,0.915414,7.047617],[4.542590,3.270907,-0.603585],[-3.637335,1.565463,4.991555]],[[-9.165773,-2.727217,0.026570],[9.763991,5.431653,1.546332],[7.707345,3.838624,3.763881],[0.626366,-5.701737,-2.434529],[-7.288201,-5.269583,-8.123491],[7.526517,5.605023,9.643361],[0.280702,9.035847,-3.936648],[7.451521,0.264500,-6.342468],[2.822173,8.293867,0.069731],[-2.024366,-3.594926,0.047601],[9.683431,-0.517795,-7.863146],[2.599601,-3.703602,-6.589739],[9.734596,-5.350366,7.271771],[2.066592,-1.947016,-9.875647]],[[6.754400,8.803815,3.146100],[-5.566619,5.747997,8.487871],[-1.682849,0.186037,1.792264],[3.507813,0.482561,1.462577],[6.048962,-0.466969,4.819146],[9.287046,2.131846,-0.704307],[4.947448,5.397575,0.526267],[2.449444,5.251508,6.399899],[-2.751704,3.116768,-2.171297],[-5.898148,-5.249434,-0.714769],[0.433622,-8.646939,-4.740920],[1.233430,2.292346,3.666196],[0.977855,-0.983049,3.262798],[8.138371,7.936171,-2.329628]],[[7.656535,6.244029,6.029454],[6.391271,6.545555,1.052982],[8.997723,2.284186,-5.823312],[2.279180,0.106089,-0.017762],[2.659983,9.950040,8.350946],[4.274305,-5.659008,-9.550903],[-9.283118,8.988527,9.281265],[6.014906,9.094462,4.848361],[9.776181,-4.740888,-1.730800],[-9.245640,-5.813601,-7.178285],[8.512335,9.205062,-1.236786],[9.182522,7.399479,-9.466120],[9.293026,2.508020,6.660321],[-4.914643,-0.490252,6.130071]],[[-5.639481,-7.034430,2.278834],[-2.407487,-8.096664,8.079618],[9.799723,7.344236,5.794021],[8.710666,-1.034288,0.381179],[5.526858,-5.735238,-7.339963],[-3.141879,2.720828,-1.399644],[-6.782161,6.626205,-5.384059],[7.940545,7.967811,-9.055930],[2.834079,-9.752923,9.028529],[8.809012,9.537908,-0.481750],[6.350712,-5.221588,1.513188],[-6.853118,1.269687,1.018314],[-9.397306,7.773265,9.456520],[-3.706207,8.082914,-9.840993]],[[-2.179267,7.513834,-4.127209],[-7.041986,4.560823,-7.170529],[4.164404,-9.588071,3.998470],[-8.162737,-2.242502,3.747330],[6.835831,-1.782226,-5.467378],[6.938346,-4.621334,3.677886],[-4.965318,5.033896,-5.677340],[8.945747,-3.820343,5.617668],[9.092989,4.712526,4.594366],[3.175017,-9.150247,-0.185106],[2.244730,1.222447,-1.758928],[-8.088895,-8.463584,-3.426792],[4.206541,-9.955613,1.228363],[5.109061,1.586989,9.655233]],[[-1.242818,-1.503237,-4.272968],[6.786597,-8.691050,-0.887605],[8.388155,-9.078867,-1.326990],[7.206882,-4.777398,4.183165],[2.907653,-4.814866,8.201969],[7.886994,-1.887563,-8.432341],[-1.043210,-8.109309,-0.883465],[-3.699385,3.706750,-3.991347],[0.443074,-4.060719,4.617897],[-6.677526,-0.029463,-1.499011],[-2.243292,3.596935,0.429262],[7.298052,-7.693558,-0.210875],[-8.357937,-1.491569,7.799157],[3.534697,-4.966528,-9.257561]],[[9.496121,-8.921235,5.265799],[5.413788,9.998824,3.099497],[-5.829489,-8.976082,-4.266899],[-5.849679,6.999015,8.769139],[5.700450,-3.291790,-5.259034],[1.918375,9.901283,9.881470],[-8.507587,-5.915394,-7.206034],[-2.498719,-6.704415,1.166238],[-4.327405,-5.719770,-4.029902],[-8.792507,-3.228125,-5.731168],[-6.896455,4.800127,5.806485],[-4.574283,7.329268,6.218318],[-2.921335,5.352135,8.465215],[-7.205515,-2.543214,3.289286]],[[-6.029796,-3.001724,-1.549771],[9.951592,-6.071010,-9.606132],[7.872799,-2.734161,2.033354],[-2.923006,8.484645,9.377165],[-2.125770,-2.457541,-5.066639],[-8.439552,-8.514318,7.379302],[7.950287,1.357213,3.419510],[5.753750,-0.661986,-8.164723],[-2.765593,-7.680760,-6.718118],[-7.299301,3.292761,5.283856],[-3.451661,-8.626344,-5.390386],[-6.495785,-6.100531,6.336101],[1.828103,-7.834752,-5.869485],[-1.266220,-7.901647,7.513384]]], dtype = "float64")#candidate|1694|(11, 14, 3)|const|float64
uop_1695 = relay.asinh(const_1694.astype('float64')) # shape=(11, 14, 3)
func_1598_call = mod.get_global_var('func_1598')
func_1602_call = mutated_mod.get_global_var('func_1602')
const_1704 = relay.const(-7.168565, dtype = "float32")#candidate|1704|()|const|float32
var_1705 = relay.var("var_1705", dtype = "float32", shape = (28,))#candidate|1705|(28,)|var|float32
call_1703 = func_1598_call(relay.reshape(const_1704.astype('float32'), []), relay.reshape(var_1705.astype('float32'), [1, 4, 7]), )
call_1706 = func_1598_call(relay.reshape(const_1704.astype('float32'), []), relay.reshape(var_1705.astype('float32'), [1, 4, 7]), )
output = relay.Tuple([uop_1695,call_1703,const_1704,var_1705,])
output2 = relay.Tuple([uop_1695,call_1706,const_1704,var_1705,])
func_1712 = relay.Function([var_1705,], output)
mod['func_1712'] = func_1712
mod = relay.transform.InferType()(mod)
mutated_mod['func_1712'] = func_1712
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1713 = relay.var("var_1713", dtype = "float32", shape = (28,))#candidate|1713|(28,)|var|float32
func_1712_call = mutated_mod.get_global_var('func_1712')
call_1714 = func_1712_call(var_1713)
output = call_1714
func_1715 = relay.Function([var_1713], output)
mutated_mod['func_1715'] = func_1715
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2043 = relay.var("var_2043", dtype = "float64", shape = ())#candidate|2043|()|var|float64
var_2044 = relay.var("var_2044", dtype = "float64", shape = (10, 1, 11))#candidate|2044|(10, 1, 11)|var|float64
bop_2045 = relay.divide(var_2043.astype('float64'), var_2044.astype('float64')) # shape=(10, 1, 11)
func_1598_call = mod.get_global_var('func_1598')
func_1602_call = mutated_mod.get_global_var('func_1602')
const_2054 = relay.const([0.717186,-1.269044,-6.086852,2.346280,4.706560,9.810322,-3.360316,-9.623186,5.052068,3.150791,9.032232,-0.252725,4.028805,6.089172,-7.954053,1.780708,-8.577740,-4.561720,-2.891514,0.023912,9.157255,3.141629,6.059161,-3.867813,8.277128,-4.420491,-7.836460,-2.081426], dtype = "float32")#candidate|2054|(28,)|const|float32
call_2053 = func_1598_call(relay.reshape(var_2043.astype('float32'), []), relay.reshape(const_2054.astype('float32'), [1, 4, 7]), )
call_2055 = func_1598_call(relay.reshape(var_2043.astype('float32'), []), relay.reshape(const_2054.astype('float32'), [1, 4, 7]), )
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2056 = relay.TupleGetItem(func_1712_call(relay.reshape(const_2054.astype('float32'), [28,])), 1)
call_2057 = relay.TupleGetItem(func_1715_call(relay.reshape(const_2054.astype('float32'), [28,])), 1)
output = relay.Tuple([bop_2045,call_2053,const_2054,call_2056,])
output2 = relay.Tuple([bop_2045,call_2055,const_2054,call_2057,])
func_2062 = relay.Function([var_2043,var_2044,], output)
mod['func_2062'] = func_2062
mod = relay.transform.InferType()(mod)
var_2063 = relay.var("var_2063", dtype = "float64", shape = ())#candidate|2063|()|var|float64
var_2064 = relay.var("var_2064", dtype = "float64", shape = (10, 1, 11))#candidate|2064|(10, 1, 11)|var|float64
output = func_2062(var_2063,var_2064,)
func_2065 = relay.Function([var_2063,var_2064,], output)
mutated_mod['func_2065'] = func_2065
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2157 = relay.var("var_2157", dtype = "float32", shape = (2, 6, 12))#candidate|2157|(2, 6, 12)|var|float32
uop_2158 = relay.rsqrt(var_2157.astype('float32')) # shape=(2, 6, 12)
output = uop_2158
output2 = uop_2158
func_2160 = relay.Function([var_2157,], output)
mod['func_2160'] = func_2160
mod = relay.transform.InferType()(mod)
mutated_mod['func_2160'] = func_2160
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2161 = relay.var("var_2161", dtype = "float32", shape = (2, 6, 12))#candidate|2161|(2, 6, 12)|var|float32
func_2160_call = mutated_mod.get_global_var('func_2160')
call_2162 = func_2160_call(var_2161)
output = call_2162
func_2163 = relay.Function([var_2161], output)
mutated_mod['func_2163'] = func_2163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2170 = relay.var("var_2170", dtype = "int16", shape = (4, 4, 12))#candidate|2170|(4, 4, 12)|var|int16
const_2171 = relay.const([[[-3,-8,7,3,-7,-3,-4,-8,-6,-10,-1,5],[-6,8,-9,1,-5,7,9,4,-4,-6,3,-9],[-2,1,9,-9,-6,10,-1,7,9,10,6,5],[-10,10,-6,-4,7,4,-1,10,9,-1,10,10]],[[4,9,-5,1,7,9,-10,6,8,1,4,-7],[3,7,7,-5,7,-2,8,6,-3,-3,-9,10],[10,7,5,8,1,3,1,9,-10,10,2,-5],[4,10,6,9,1,1,7,6,-5,5,5,-5]],[[5,-2,3,6,7,9,3,-1,-5,10,2,-1],[3,2,-10,-2,4,5,-5,-5,4,6,-3,2],[9,-1,8,-7,-5,-10,8,3,-9,-1,9,7],[-1,3,-9,-3,8,9,-5,-8,7,-9,-1,-1]],[[1,5,8,-3,4,-5,10,-3,-4,-6,-1,1],[-4,7,3,8,-9,-3,-6,8,-4,-4,2,5],[-2,-7,5,10,-8,-7,-4,4,1,-10,6,8],[2,-6,-1,-2,-2,-5,7,-10,-4,-8,3,2]]], dtype = "int16")#candidate|2171|(4, 4, 12)|const|int16
bop_2172 = relay.right_shift(var_2170.astype('int16'), relay.reshape(const_2171.astype('int16'), relay.shape_of(var_2170))) # shape=(4, 4, 12)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
var_2181 = relay.var("var_2181", dtype = "float64", shape = ())#candidate|2181|()|var|float64
const_2182 = relay.const([7.239465,-0.785603,6.787960,-4.248191,-9.327325,-1.134157,-6.246151,7.912669,-5.043278,-9.354256,-6.917094,6.813511,-7.090920,-8.696577,-5.376951,6.917017,-0.363238,6.014510,1.034041,4.164257,-7.983667,-7.831421,1.798794,0.048998,5.022993,-6.201816,2.426181,0.552774,4.884304,2.537987,-5.850858,-6.752184,-6.969262,-4.335895,9.110572,-5.780856,2.123926,-9.091966,-9.108402,-9.905992,4.321192,8.232809,0.999678,7.563358,0.381384,-7.889122,4.550214,-7.659733,-3.789209,5.878418,-5.280989,-5.112955,-8.231560,-0.476201,-4.761184,7.630638,1.327779,-6.723571,7.408462,-9.574352,2.055017,-1.917207,8.758453,-0.531072,1.976806,3.488131,3.798582,0.343828,-7.941059,-0.378063,-3.725944,9.639814,6.469923,-5.379194,2.697726,3.040758,3.897790,2.299661,-3.025986,5.474020,-3.214508,1.853568,-7.951292,1.535168,-3.368992,5.152876,4.034739,-1.478914,-8.752919,0.535011,8.731770,-0.434044,-1.456216,7.111751,-5.201516,-6.745245,8.240388,-7.795896,-9.526569,4.548557,-6.668773,-2.153573,3.877163,-5.404395,0.851955,2.760037,-0.760440,-1.773655,5.469626,6.912895], dtype = "float64")#candidate|2182|(110,)|const|float64
call_2180 = relay.TupleGetItem(func_2062_call(relay.reshape(var_2181.astype('float64'), []), relay.reshape(const_2182.astype('float64'), [10, 1, 11]), ), 3)
call_2183 = relay.TupleGetItem(func_2065_call(relay.reshape(var_2181.astype('float64'), []), relay.reshape(const_2182.astype('float64'), [10, 1, 11]), ), 3)
output = relay.Tuple([bop_2172,call_2180,var_2181,const_2182,])
output2 = relay.Tuple([bop_2172,call_2183,var_2181,const_2182,])
func_2187 = relay.Function([var_2170,var_2181,], output)
mod['func_2187'] = func_2187
mod = relay.transform.InferType()(mod)
var_2188 = relay.var("var_2188", dtype = "int16", shape = (4, 4, 12))#candidate|2188|(4, 4, 12)|var|int16
var_2189 = relay.var("var_2189", dtype = "float64", shape = ())#candidate|2189|()|var|float64
output = func_2187(var_2188,var_2189,)
func_2190 = relay.Function([var_2188,var_2189,], output)
mutated_mod['func_2190'] = func_2190
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2453 = relay.const([[[0.167797,6.459885,-9.348653],[8.661635,1.387902,4.729173],[9.887002,9.086482,-7.269943],[6.917324,2.205038,-5.053815],[1.221346,-0.496214,-6.505194],[1.929009,-9.526338,1.822655],[-5.880161,-8.980420,4.476098],[-3.662656,-3.079138,6.678927]],[[7.434631,-6.448491,-1.116558],[-6.610602,1.058152,-3.627562],[-9.639063,-2.336544,-5.500675],[1.887471,-7.536276,-0.063830],[9.885369,0.544667,0.946025],[4.943666,5.057611,8.492048],[-8.089363,1.107120,9.502835],[1.801203,0.272252,-0.348919]],[[3.475156,-3.235739,1.573835],[6.833297,-8.184960,-6.695376],[7.220034,-5.736382,6.835934],[-7.741597,3.165162,-8.316944],[2.425776,-8.585102,8.222596],[9.664813,-5.482956,-5.063935],[-1.045877,9.424277,-4.450227],[-4.302521,2.824799,-2.332061]],[[2.314685,-2.760319,-4.095242],[8.865773,-0.587929,2.762830],[-7.109113,-6.768605,-1.205064],[-1.533689,-0.076235,8.504619],[8.459315,2.094130,1.146376],[1.683977,-0.261512,0.898701],[-7.319914,3.320050,0.308478],[-5.360570,7.611777,-6.946701]],[[-6.563969,-9.761250,-8.275987],[1.784619,-6.083294,-3.561974],[2.502089,-7.688508,0.419677],[-1.230855,-3.225470,-8.130068],[-2.791901,9.848206,2.147416],[-4.522817,-8.128505,3.466311],[-8.467736,-1.459268,8.295740],[-3.556474,-9.955117,-0.977968]],[[2.872113,-5.854364,-9.339135],[5.270504,3.085376,-5.560782],[-3.845375,-5.061395,-9.110789],[-3.305334,0.680356,2.750249],[8.577841,5.782894,-0.710269],[-8.290198,-2.478326,4.274731],[8.854294,-6.976169,7.453201],[-1.941817,6.971831,-8.047627]],[[-2.818092,-3.777258,7.485923],[-0.483541,-1.056005,-2.460695],[3.135550,-8.820403,7.868050],[6.321877,-5.114859,-5.400827],[-5.259388,1.721191,3.921275],[8.865970,-2.558424,8.611953],[5.577564,0.699201,1.278388],[-2.826730,-6.493152,6.176601]],[[-0.467562,-9.046490,-5.516909],[-1.569834,0.173760,-2.704712],[1.458487,-0.118854,7.910428],[4.915719,5.095499,-0.793148],[8.185878,-7.873564,2.029807],[7.222194,-4.428366,-4.164278],[-4.461144,9.290049,5.064933],[8.202178,-4.827186,-5.690620]],[[5.521846,-0.748343,-5.035686],[-2.501620,-4.691113,3.030398],[-0.233450,3.597757,3.742604],[2.444990,1.155375,0.862770],[-8.063978,0.338704,6.106183],[-1.046623,-6.600691,8.763078],[-1.340428,-1.230701,-9.657049],[-7.533773,-7.775824,4.340145]],[[-8.841462,-7.097134,-0.517107],[-7.873079,-6.817440,5.308809],[0.073766,-2.046129,-5.264950],[6.820305,1.411621,7.764160],[1.607703,-3.968000,-8.156563],[4.626178,-8.226398,-9.177603],[-0.511949,8.537490,-0.516136],[-4.452911,1.869552,6.508442]],[[-6.853496,-5.706038,-9.527426],[-3.928200,0.832559,-9.733970],[-3.150540,-9.036576,3.934928],[8.654752,4.593028,-3.801115],[2.705083,-3.495373,0.473336],[5.210461,-7.681086,-5.043117],[0.765776,-2.011063,3.623411],[-2.197920,5.272496,3.820119]],[[4.525612,-3.736746,9.260363],[5.958406,4.206778,9.016804],[6.275509,-5.078189,-0.260389],[2.440948,2.853071,7.743543],[-1.950341,6.519145,-9.517778],[-7.544011,5.257646,5.282219],[8.161307,-5.823872,-1.953871],[0.018089,-6.495658,9.825112]],[[-7.691156,-0.236647,-0.241041],[4.534787,-6.157257,-1.676143],[7.915234,-0.977684,8.354097],[0.830605,-6.048573,9.869930],[-0.284272,6.423518,7.466755],[8.874968,4.465022,5.467454],[4.873636,-2.803185,7.085558],[6.136484,2.269315,-3.789431]],[[3.207820,6.600875,0.819304],[-3.332400,0.737324,-1.010786],[-6.459429,9.897752,6.855774],[5.275968,9.070362,-3.994094],[1.060392,0.139780,-3.269619],[5.135191,4.192946,5.406762],[-7.288101,-7.462883,0.923787],[-7.124464,4.896400,6.895016]],[[-6.768587,6.954032,-6.890193],[5.786965,1.123833,-3.781252],[-0.090136,2.608887,-6.397033],[-4.549416,-3.373813,5.364860],[5.473297,7.284139,7.574260],[2.731343,-7.626656,8.136517],[9.059902,-0.792540,0.901093],[-3.017858,-7.910714,5.745808]]], dtype = "float64")#candidate|2453|(15, 8, 3)|const|float64
uop_2454 = relay.sinh(const_2453.astype('float64')) # shape=(15, 8, 3)
func_1598_call = mod.get_global_var('func_1598')
func_1602_call = mutated_mod.get_global_var('func_1602')
const_2457 = relay.const(-6.604711, dtype = "float32")#candidate|2457|()|const|float32
const_2458 = relay.const([-3.936037,5.808360,7.989103,-8.058721,-6.495994,-1.514936,7.838014,-5.811398,-8.410684,-5.138172,-2.449253,-6.832621,-2.481822,-9.508158,-0.014554,-3.243455,7.758266,-9.350773,-7.508110,-9.967523,-1.498450,0.795395,-9.759137,-1.689125,8.213162,-0.421885,-4.151877,3.067901], dtype = "float32")#candidate|2458|(28,)|const|float32
call_2456 = func_1598_call(relay.reshape(const_2457.astype('float32'), []), relay.reshape(const_2458.astype('float32'), [1, 4, 7]), )
call_2459 = func_1598_call(relay.reshape(const_2457.astype('float32'), []), relay.reshape(const_2458.astype('float32'), [1, 4, 7]), )
output = relay.Tuple([uop_2454,call_2456,const_2457,const_2458,])
output2 = relay.Tuple([uop_2454,call_2459,const_2457,const_2458,])
func_2467 = relay.Function([], output)
mod['func_2467'] = func_2467
mod = relay.transform.InferType()(mod)
output = func_2467()
func_2468 = relay.Function([], output)
mutated_mod['func_2468'] = func_2468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_2471 = relay.TupleGetItem(func_2467_call(), 0)
call_2472 = relay.TupleGetItem(func_2468_call(), 0)
uop_2483 = relay.atanh(call_2471.astype('float64')) # shape=(15, 8, 3)
uop_2485 = relay.atanh(call_2472.astype('float64')) # shape=(15, 8, 3)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_2507 = relay.const(4.831018, dtype = "float64")#candidate|2507|()|const|float64
const_2508 = relay.const([4.740147,-4.663164,-0.326676,-6.476677,9.842436,0.670115,0.294484,8.889148,9.611374,-7.714611,-6.062222,2.735052,-4.321671,5.751158,-1.110477,7.831129,-5.450610,1.480794,8.152605,-7.719795,-9.165713,-9.138081,-2.173361,6.652823,6.264880,-2.022437,3.577451,-2.424210,3.271517,2.239668,6.774922,0.533407,-2.723858,7.216132,7.524974,-9.809928,0.844414,1.308686,-5.569734,-7.304423,0.716228,7.235489,-3.713624,-1.050300,-4.203963,9.280593,-7.337105,0.130257,2.676080,5.880402,-8.899747,3.017540,-1.268611,-8.512228,6.850258,5.411960,7.924751,4.852760,-3.576302,2.874502,-2.971646,-0.864758,-4.330828,6.486761,-8.619783,-6.888954,3.863865,0.956237,-1.595630,-3.956661,-8.093311,-6.806821,3.229483,4.771638,7.398139,-8.835234,-1.065110,2.042943,-4.656657,-1.382643,0.423602,2.602287,-7.662530,-1.886518,-7.667688,3.351225,-6.095528,4.571851,8.252027,6.275751,3.358357,-7.205192,0.722245,-2.786272,3.325295,-1.078348,0.445319,4.754599,-0.597731,7.822447,-9.247158,1.288438,-3.661672,-7.445747,-1.319560,5.196779,5.712060,5.823089,6.193707,-3.989984], dtype = "float64")#candidate|2508|(110,)|const|float64
call_2506 = relay.TupleGetItem(func_2062_call(relay.reshape(const_2507.astype('float64'), []), relay.reshape(const_2508.astype('float64'), [10, 1, 11]), ), 1)
call_2509 = relay.TupleGetItem(func_2065_call(relay.reshape(const_2507.astype('float64'), []), relay.reshape(const_2508.astype('float64'), [10, 1, 11]), ), 1)
output = relay.Tuple([uop_2483,call_2506,const_2507,const_2508,])
output2 = relay.Tuple([uop_2485,call_2509,const_2507,const_2508,])
func_2512 = relay.Function([], output)
mod['func_2512'] = func_2512
mod = relay.transform.InferType()(mod)
output = func_2512()
func_2513 = relay.Function([], output)
mutated_mod['func_2513'] = func_2513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_2514 = relay.TupleGetItem(func_2512_call(), 1)
call_2515 = relay.TupleGetItem(func_2513_call(), 1)
output = relay.Tuple([call_2514,])
output2 = relay.Tuple([call_2515,])
func_2526 = relay.Function([], output)
mod['func_2526'] = func_2526
mod = relay.transform.InferType()(mod)
mutated_mod['func_2526'] = func_2526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mutated_mod.get_global_var('func_2526')
call_2527 = func_2526_call()
output = call_2527
func_2528 = relay.Function([], output)
mutated_mod['func_2528'] = func_2528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2531 = relay.var("var_2531", dtype = "float64", shape = (2, 10, 5))#candidate|2531|(2, 10, 5)|var|float64
var_2532 = relay.var("var_2532", dtype = "float64", shape = (2, 10, 5))#candidate|2532|(2, 10, 5)|var|float64
bop_2533 = relay.power(var_2531.astype('float64'), relay.reshape(var_2532.astype('float64'), relay.shape_of(var_2531))) # shape=(2, 10, 5)
output = bop_2533
output2 = bop_2533
func_2539 = relay.Function([var_2531,var_2532,], output)
mod['func_2539'] = func_2539
mod = relay.transform.InferType()(mod)
var_2540 = relay.var("var_2540", dtype = "float64", shape = (2, 10, 5))#candidate|2540|(2, 10, 5)|var|float64
var_2541 = relay.var("var_2541", dtype = "float64", shape = (2, 10, 5))#candidate|2541|(2, 10, 5)|var|float64
output = func_2539(var_2540,var_2541,)
func_2542 = relay.Function([var_2540,var_2541,], output)
mutated_mod['func_2542'] = func_2542
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2544 = relay.var("var_2544", dtype = "int32", shape = (13, 13, 13))#candidate|2544|(13, 13, 13)|var|int32
var_2545 = relay.var("var_2545", dtype = "int32", shape = (13, 13, 13))#candidate|2545|(13, 13, 13)|var|int32
bop_2546 = relay.add(var_2544.astype('int32'), relay.reshape(var_2545.astype('int32'), relay.shape_of(var_2544))) # shape=(13, 13, 13)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
var_2552 = relay.var("var_2552", dtype = "float32", shape = (28,))#candidate|2552|(28,)|var|float32
call_2551 = relay.TupleGetItem(func_1712_call(relay.reshape(var_2552.astype('float32'), [28,])), 2)
call_2553 = relay.TupleGetItem(func_1715_call(relay.reshape(var_2552.astype('float32'), [28,])), 2)
output = relay.Tuple([bop_2546,call_2551,var_2552,])
output2 = relay.Tuple([bop_2546,call_2553,var_2552,])
func_2565 = relay.Function([var_2544,var_2545,var_2552,], output)
mod['func_2565'] = func_2565
mod = relay.transform.InferType()(mod)
var_2566 = relay.var("var_2566", dtype = "int32", shape = (13, 13, 13))#candidate|2566|(13, 13, 13)|var|int32
var_2567 = relay.var("var_2567", dtype = "int32", shape = (13, 13, 13))#candidate|2567|(13, 13, 13)|var|int32
var_2568 = relay.var("var_2568", dtype = "float32", shape = (28,))#candidate|2568|(28,)|var|float32
output = func_2565(var_2566,var_2567,var_2568,)
func_2569 = relay.Function([var_2566,var_2567,var_2568,], output)
mutated_mod['func_2569'] = func_2569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_2571 = relay.TupleGetItem(func_2512_call(), 1)
call_2572 = relay.TupleGetItem(func_2513_call(), 1)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_2578 = relay.TupleGetItem(func_2467_call(), 2)
call_2579 = relay.TupleGetItem(func_2468_call(), 2)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
var_2581 = relay.var("var_2581", dtype = "float64", shape = (22, 5))#candidate|2581|(22, 5)|var|float64
call_2580 = relay.TupleGetItem(func_2062_call(relay.reshape(call_2578.astype('float64'), []), relay.reshape(var_2581.astype('float64'), [10, 1, 11]), ), 3)
call_2582 = relay.TupleGetItem(func_2065_call(relay.reshape(call_2578.astype('float64'), []), relay.reshape(var_2581.astype('float64'), [10, 1, 11]), ), 3)
output = relay.Tuple([call_2571,call_2578,call_2580,var_2581,])
output2 = relay.Tuple([call_2572,call_2579,call_2582,var_2581,])
func_2587 = relay.Function([var_2581,], output)
mod['func_2587'] = func_2587
mod = relay.transform.InferType()(mod)
var_2588 = relay.var("var_2588", dtype = "float64", shape = (22, 5))#candidate|2588|(22, 5)|var|float64
output = func_2587(var_2588)
func_2589 = relay.Function([var_2588], output)
mutated_mod['func_2589'] = func_2589
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2697 = relay.var("var_2697", dtype = "float32", shape = (13, 12, 4))#candidate|2697|(13, 12, 4)|var|float32
uop_2698 = relay.sinh(var_2697.astype('float32')) # shape=(13, 12, 4)
output = relay.Tuple([uop_2698,])
output2 = relay.Tuple([uop_2698,])
func_2702 = relay.Function([var_2697,], output)
mod['func_2702'] = func_2702
mod = relay.transform.InferType()(mod)
var_2703 = relay.var("var_2703", dtype = "float32", shape = (13, 12, 4))#candidate|2703|(13, 12, 4)|var|float32
output = func_2702(var_2703)
func_2704 = relay.Function([var_2703], output)
mutated_mod['func_2704'] = func_2704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_2798 = relay.TupleGetItem(func_2512_call(), 1)
call_2799 = relay.TupleGetItem(func_2513_call(), 1)
output = relay.Tuple([call_2798,])
output2 = relay.Tuple([call_2799,])
func_2808 = relay.Function([], output)
mod['func_2808'] = func_2808
mod = relay.transform.InferType()(mod)
mutated_mod['func_2808'] = func_2808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2808_call = mutated_mod.get_global_var('func_2808')
call_2809 = func_2808_call()
output = call_2809
func_2810 = relay.Function([], output)
mutated_mod['func_2810'] = func_2810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_2813 = relay.TupleGetItem(func_2467_call(), 3)
call_2814 = relay.TupleGetItem(func_2468_call(), 3)
output = call_2813
output2 = call_2814
func_2845 = relay.Function([], output)
mod['func_2845'] = func_2845
mod = relay.transform.InferType()(mod)
output = func_2845()
func_2846 = relay.Function([], output)
mutated_mod['func_2846'] = func_2846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_2864 = relay.TupleGetItem(func_2526_call(), 0)
call_2865 = relay.TupleGetItem(func_2528_call(), 0)
func_2187_call = mod.get_global_var('func_2187')
func_2190_call = mutated_mod.get_global_var('func_2190')
const_2876 = relay.const([-10,-2,10,1,-6,-7,10,-2,10,-9,7,6,-8,3,9,-9,9,-6,-3,4,-7,4,4,4,10,-10,-1,10,1,5,5,10,3,-10,-5,10,9,9,1,-1,9,10,8,-9,5,-2,6,-6,-10,-9,-5,8,2,7,-3,4,10,3,-8,-10,6,5,3,-3,10,-7,1,-8,3,6,-6,9,8,5,-4,-1,6,-2,-9,-2,-9,3,6,-2,-9,-8,-3,-10,-9,-7,9,-5,3,-5,-6,-3,-10,4,-10,-7,-7,1,-2,-8,-7,7,-2,2,-4,2,-4,5,-1,-1,3,9,3,-9,10,-9,4,-2,10,6,1,-4,-10,10,-5,-4,9,10,3,8,-7,-10,-4,-9,-8,-10,10,-5,-2,6,6,-8,5,-8,9,4,4,9,8,-6,-3,-5,-10,-5,-5,-2,3,7,-1,-8,2,6,-6,6,3,8,8,-8,4,-3,-6,-4,-6,-1,-8,7,9,-6,10,-6,-5,8,-8,2,-2,4,1,-1], dtype = "int16")#candidate|2876|(192,)|const|int16
const_2877 = relay.const(0.124844, dtype = "float64")#candidate|2877|()|const|float64
call_2875 = relay.TupleGetItem(func_2187_call(relay.reshape(const_2876.astype('int16'), [4, 4, 12]), relay.reshape(const_2877.astype('float64'), []), ), 3)
call_2878 = relay.TupleGetItem(func_2190_call(relay.reshape(const_2876.astype('int16'), [4, 4, 12]), relay.reshape(const_2877.astype('float64'), []), ), 3)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2879 = relay.TupleGetItem(func_1712_call(relay.reshape(call_2864.astype('float32'), [28,])), 3)
call_2880 = relay.TupleGetItem(func_1715_call(relay.reshape(call_2864.astype('float32'), [28,])), 3)
uop_2889 = relay.acos(call_2864.astype('float64')) # shape=(1, 4, 7)
uop_2891 = relay.acos(call_2865.astype('float64')) # shape=(1, 4, 7)
func_2845_call = mod.get_global_var('func_2845')
func_2846_call = mutated_mod.get_global_var('func_2846')
call_2897 = func_2845_call()
call_2898 = func_2845_call()
bop_2913 = relay.floor_divide(uop_2889.astype('float32'), relay.reshape(call_2864.astype('float32'), relay.shape_of(uop_2889))) # shape=(1, 4, 7)
bop_2916 = relay.floor_divide(uop_2891.astype('float32'), relay.reshape(call_2865.astype('float32'), relay.shape_of(uop_2891))) # shape=(1, 4, 7)
output = relay.Tuple([call_2875,const_2876,const_2877,call_2879,call_2897,bop_2913,])
output2 = relay.Tuple([call_2878,const_2876,const_2877,call_2880,call_2898,bop_2916,])
func_2920 = relay.Function([], output)
mod['func_2920'] = func_2920
mod = relay.transform.InferType()(mod)
mutated_mod['func_2920'] = func_2920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mutated_mod.get_global_var('func_2920')
call_2921 = func_2920_call()
output = call_2921
func_2922 = relay.Function([], output)
mutated_mod['func_2922'] = func_2922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_2926 = relay.TupleGetItem(func_2808_call(), 0)
call_2927 = relay.TupleGetItem(func_2810_call(), 0)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_2934 = relay.TupleGetItem(func_2920_call(), 3)
call_2935 = relay.TupleGetItem(func_2922_call(), 3)
output = relay.Tuple([call_2926,call_2934,])
output2 = relay.Tuple([call_2927,call_2935,])
func_2945 = relay.Function([], output)
mod['func_2945'] = func_2945
mod = relay.transform.InferType()(mod)
mutated_mod['func_2945'] = func_2945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mutated_mod.get_global_var('func_2945')
call_2946 = func_2945_call()
output = call_2946
func_2947 = relay.Function([], output)
mutated_mod['func_2947'] = func_2947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_2972 = relay.TupleGetItem(func_2526_call(), 0)
call_2973 = relay.TupleGetItem(func_2528_call(), 0)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_2978 = relay.const(7.791120, dtype = "float64")#candidate|2978|()|const|float64
var_2979 = relay.var("var_2979", dtype = "float64", shape = (110,))#candidate|2979|(110,)|var|float64
call_2977 = relay.TupleGetItem(func_2062_call(relay.reshape(const_2978.astype('float64'), []), relay.reshape(var_2979.astype('float64'), [10, 1, 11]), ), 1)
call_2980 = relay.TupleGetItem(func_2065_call(relay.reshape(const_2978.astype('float64'), []), relay.reshape(var_2979.astype('float64'), [10, 1, 11]), ), 1)
uop_2984 = relay.sigmoid(call_2972.astype('float32')) # shape=(1, 4, 7)
uop_2986 = relay.sigmoid(call_2973.astype('float32')) # shape=(1, 4, 7)
bop_3011 = relay.logical_or(const_2978.astype('bool'), call_2972.astype('bool')) # shape=(1, 4, 7)
bop_3014 = relay.logical_or(const_2978.astype('bool'), call_2973.astype('bool')) # shape=(1, 4, 7)
output = relay.Tuple([call_2977,var_2979,uop_2984,bop_3011,])
output2 = relay.Tuple([call_2980,var_2979,uop_2986,bop_3014,])
func_3023 = relay.Function([var_2979,], output)
mod['func_3023'] = func_3023
mod = relay.transform.InferType()(mod)
var_3024 = relay.var("var_3024", dtype = "float64", shape = (110,))#candidate|3024|(110,)|var|float64
output = func_3023(var_3024)
func_3025 = relay.Function([var_3024], output)
mutated_mod['func_3025'] = func_3025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3029 = relay.TupleGetItem(func_2920_call(), 2)
call_3030 = relay.TupleGetItem(func_2922_call(), 2)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_3073 = relay.const([5.546732,-8.889622,-3.411295,-2.844322,7.350322,-3.591641,-9.654457,-5.424448,-5.796818,-9.348971,-9.127672,1.761294,2.280248,-5.471637,-9.510649,0.569923,6.951421,-9.285889,-5.274410,-6.233340,6.952222,-7.589961,-7.264622,4.944206,-3.482062,3.126332,8.531358,4.932565,1.072667,7.698082,7.638673,4.533834,-5.875186,-7.555745,1.532363,0.451755,-5.999292,-1.782348,-0.454279,9.673709,-5.541873,0.879882,-3.861761,-3.004560,-5.818721,9.263520,-2.608495,-4.914057,3.773382,0.285564,6.126827,8.219516,-1.281975,-8.960363,5.597283,9.971263,7.226633,6.938635,-2.090720,5.583782,4.943145,-3.916565,-7.879900,-3.781858,-5.230522,-2.151295,-6.015913,4.713017,5.205624,4.426635,8.435375,-7.994535,0.826184,-7.474112,7.246762,-2.153689,9.519454,-6.868761,0.635455,9.536387,-8.382898,-9.982852,2.432901,-7.407535,5.615040,4.003092,-0.831263,1.344007,7.704971,5.315274,-1.762153,1.258581,4.076960,5.151593,-9.893047,-9.273636,-0.939749,-6.043796,-6.532891,-9.802295,-1.563389,-7.594402,-0.262939,2.839662,-9.786939,-0.444249,-3.545296,-0.232118,-1.599782,4.326327], dtype = "float64")#candidate|3073|(110,)|const|float64
call_3072 = relay.TupleGetItem(func_2062_call(relay.reshape(call_3029.astype('float64'), []), relay.reshape(const_3073.astype('float64'), [10, 1, 11]), ), 3)
call_3074 = relay.TupleGetItem(func_2065_call(relay.reshape(call_3029.astype('float64'), []), relay.reshape(const_3073.astype('float64'), [10, 1, 11]), ), 3)
var_3080 = relay.var("var_3080", dtype = "float64", shape = (110,))#candidate|3080|(110,)|var|float64
bop_3081 = relay.equal(const_3073.astype('bool'), relay.reshape(var_3080.astype('bool'), relay.shape_of(const_3073))) # shape=(110,)
func_2539_call = mod.get_global_var('func_2539')
func_2542_call = mutated_mod.get_global_var('func_2542')
var_3095 = relay.var("var_3095", dtype = "float64", shape = (100,))#candidate|3095|(100,)|var|float64
call_3094 = func_2539_call(relay.reshape(var_3095.astype('float64'), [2, 10, 5]), relay.reshape(var_3095.astype('float64'), [2, 10, 5]), )
call_3096 = func_2539_call(relay.reshape(var_3095.astype('float64'), [2, 10, 5]), relay.reshape(var_3095.astype('float64'), [2, 10, 5]), )
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_3097 = relay.TupleGetItem(func_2512_call(), 1)
call_3098 = relay.TupleGetItem(func_2513_call(), 1)
uop_3101 = relay.tan(call_3072.astype('float32')) # shape=(1, 4, 7)
uop_3103 = relay.tan(call_3074.astype('float32')) # shape=(1, 4, 7)
output = relay.Tuple([call_3029,bop_3081,call_3094,var_3095,call_3097,uop_3101,])
output2 = relay.Tuple([call_3030,bop_3081,call_3096,var_3095,call_3098,uop_3103,])
func_3118 = relay.Function([var_3080,var_3095,], output)
mod['func_3118'] = func_3118
mod = relay.transform.InferType()(mod)
mutated_mod['func_3118'] = func_3118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3118_call = mutated_mod.get_global_var('func_3118')
var_3120 = relay.var("var_3120", dtype = "float64", shape = (110,))#candidate|3120|(110,)|var|float64
var_3121 = relay.var("var_3121", dtype = "float64", shape = (100,))#candidate|3121|(100,)|var|float64
call_3119 = func_3118_call(var_3120,var_3121,)
output = call_3119
func_3122 = relay.Function([var_3120,var_3121,], output)
mutated_mod['func_3122'] = func_3122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2845_call = mod.get_global_var('func_2845')
func_2846_call = mutated_mod.get_global_var('func_2846')
call_3124 = func_2845_call()
call_3125 = func_2845_call()
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_3140 = relay.TupleGetItem(func_2467_call(), 2)
call_3141 = relay.TupleGetItem(func_2468_call(), 2)
output = relay.Tuple([call_3124,call_3140,])
output2 = relay.Tuple([call_3125,call_3141,])
func_3157 = relay.Function([], output)
mod['func_3157'] = func_3157
mod = relay.transform.InferType()(mod)
mutated_mod['func_3157'] = func_3157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3157_call = mutated_mod.get_global_var('func_3157')
call_3158 = func_3157_call()
output = call_3158
func_3159 = relay.Function([], output)
mutated_mod['func_3159'] = func_3159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_3272 = relay.TupleGetItem(func_2945_call(), 0)
call_3273 = relay.TupleGetItem(func_2947_call(), 0)
output = relay.Tuple([call_3272,])
output2 = relay.Tuple([call_3273,])
func_3287 = relay.Function([], output)
mod['func_3287'] = func_3287
mod = relay.transform.InferType()(mod)
mutated_mod['func_3287'] = func_3287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mutated_mod.get_global_var('func_3287')
call_3288 = func_3287_call()
output = call_3288
func_3289 = relay.Function([], output)
mutated_mod['func_3289'] = func_3289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3358 = relay.TupleGetItem(func_2920_call(), 3)
call_3359 = relay.TupleGetItem(func_2922_call(), 3)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_3366 = relay.TupleGetItem(func_2526_call(), 0)
call_3367 = relay.TupleGetItem(func_2528_call(), 0)
func_2539_call = mod.get_global_var('func_2539')
func_2542_call = mutated_mod.get_global_var('func_2542')
const_3380 = relay.const([[-0.750574,-4.071471,6.925479,4.248271,5.363920,-8.876147,4.616100,3.615619,3.098048,5.256390,0.009237,8.826988,8.747551,-7.273313,-3.756245,-2.573480,0.827188,-5.427377,-1.405127,5.619548,5.692880,0.008693,8.139923,4.879966,-6.739472,5.516032,1.042446,-2.152929,1.095499,-0.264873,5.464672,-0.131907,-8.029000,-2.145115,-8.562661,-1.541226,7.754435,6.858243,-3.447608,-1.016311,2.198866,-0.859770,-2.306137,-0.516703,4.787496,3.488950,6.359541,-6.052118,3.072018,-3.027376,-9.415986,4.422012,-7.079375,3.395022,7.591808,0.263944,4.261572,-4.055842,-8.947774,6.348518,8.448061,7.154146,-5.819061,-4.202869,-4.039283,-6.280348,-7.355324,-3.114685,-9.747971,9.863218,6.396439,-2.162365,1.416981,4.224901,6.313364,2.437006,7.261593,0.754331,-1.707042,0.039682,-8.846407,-4.426710,-8.392405,0.092757,-5.544160,-2.642959,9.493379,-5.112439,7.336229,2.528041,-6.010475,-0.849945,5.532707,6.224225,8.476721,-9.953111,-4.481454,-9.032520,3.624934,4.289056]], dtype = "float64")#candidate|3380|(1, 100)|const|float64
call_3379 = func_2539_call(relay.reshape(const_3380.astype('float64'), [2, 10, 5]), relay.reshape(const_3380.astype('float64'), [2, 10, 5]), )
call_3381 = func_2539_call(relay.reshape(const_3380.astype('float64'), [2, 10, 5]), relay.reshape(const_3380.astype('float64'), [2, 10, 5]), )
output = relay.Tuple([call_3358,call_3366,call_3379,const_3380,])
output2 = relay.Tuple([call_3359,call_3367,call_3381,const_3380,])
func_3390 = relay.Function([], output)
mod['func_3390'] = func_3390
mod = relay.transform.InferType()(mod)
mutated_mod['func_3390'] = func_3390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3390_call = mutated_mod.get_global_var('func_3390')
call_3391 = func_3390_call()
output = call_3391
func_3392 = relay.Function([], output)
mutated_mod['func_3392'] = func_3392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3157_call = mod.get_global_var('func_3157')
func_3159_call = mutated_mod.get_global_var('func_3159')
call_3395 = relay.TupleGetItem(func_3157_call(), 0)
call_3396 = relay.TupleGetItem(func_3159_call(), 0)
func_2845_call = mod.get_global_var('func_2845')
func_2846_call = mutated_mod.get_global_var('func_2846')
call_3397 = func_2845_call()
call_3398 = func_2845_call()
func_2187_call = mod.get_global_var('func_2187')
func_2190_call = mutated_mod.get_global_var('func_2190')
const_3407 = relay.const([-9,3,6,1,-2,4,7,-9,4,-3,-6,-9,1,-3,1,-5,2,2,-5,-7,-3,10,-9,-5,7,-5,-4,-7,2,-9,-7,-3,-4,7,10,-4,-7,3,3,10,9,-4,-2,7,2,-6,4,-8,-4,8,10,-7,8,4,-1,3,2,2,-8,-7,-8,-9,-2,-9,-1,10,-8,-10,-10,-10,-9,-10,10,-4,-2,-9,3,1,5,2,8,9,1,-4,4,-4,7,-3,-8,5,7,10,-4,-5,-4,4,9,8,5,-10,4,-1,10,7,-2,-7,6,10,10,-8,-2,-6,8,-10,-4,1,8,8,-7,-3,-5,9,-10,3,2,-6,-2,7,4,2,-2,5,-6,-6,-8,-3,1,-6,8,-3,-9,-7,9,2,3,-3,-8,3,-3,-8,-9,-4,4,1,9,4,-1,2,7,7,-9,-5,1,10,6,-3,-2,5,-8,8,10,-7,5,3,5,-1,2,-1,3,-7,1,6,-8,9,-7,3,-9,8,-2,-5,5,-1], dtype = "int16")#candidate|3407|(192,)|const|int16
var_3408 = relay.var("var_3408", dtype = "float64", shape = ())#candidate|3408|()|var|float64
call_3406 = relay.TupleGetItem(func_2187_call(relay.reshape(const_3407.astype('int16'), [4, 4, 12]), relay.reshape(var_3408.astype('float64'), []), ), 2)
call_3409 = relay.TupleGetItem(func_2190_call(relay.reshape(const_3407.astype('int16'), [4, 4, 12]), relay.reshape(var_3408.astype('float64'), []), ), 2)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_3410 = relay.TupleGetItem(func_1712_call(relay.reshape(call_3397.astype('float32'), [28,])), 3)
call_3411 = relay.TupleGetItem(func_1715_call(relay.reshape(call_3397.astype('float32'), [28,])), 3)
output = relay.Tuple([call_3395,call_3397,call_3406,const_3407,var_3408,call_3410,])
output2 = relay.Tuple([call_3396,call_3398,call_3409,const_3407,var_3408,call_3411,])
func_3414 = relay.Function([var_3408,], output)
mod['func_3414'] = func_3414
mod = relay.transform.InferType()(mod)
var_3415 = relay.var("var_3415", dtype = "float64", shape = ())#candidate|3415|()|var|float64
output = func_3414(var_3415)
func_3416 = relay.Function([var_3415], output)
mutated_mod['func_3416'] = func_3416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_3533 = relay.TupleGetItem(func_2467_call(), 3)
call_3534 = relay.TupleGetItem(func_2468_call(), 3)
output = call_3533
output2 = call_3534
func_3544 = relay.Function([], output)
mod['func_3544'] = func_3544
mod = relay.transform.InferType()(mod)
output = func_3544()
func_3545 = relay.Function([], output)
mutated_mod['func_3545'] = func_3545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_3635 = relay.TupleGetItem(func_2512_call(), 3)
call_3636 = relay.TupleGetItem(func_2513_call(), 3)
output = relay.Tuple([call_3635,])
output2 = relay.Tuple([call_3636,])
func_3639 = relay.Function([], output)
mod['func_3639'] = func_3639
mod = relay.transform.InferType()(mod)
mutated_mod['func_3639'] = func_3639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3639_call = mutated_mod.get_global_var('func_3639')
call_3640 = func_3639_call()
output = call_3640
func_3641 = relay.Function([], output)
mutated_mod['func_3641'] = func_3641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3651 = relay.TupleGetItem(func_2920_call(), 3)
call_3652 = relay.TupleGetItem(func_2922_call(), 3)
output = relay.Tuple([call_3651,])
output2 = relay.Tuple([call_3652,])
func_3655 = relay.Function([], output)
mod['func_3655'] = func_3655
mod = relay.transform.InferType()(mod)
output = func_3655()
func_3656 = relay.Function([], output)
mutated_mod['func_3656'] = func_3656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3671 = relay.TupleGetItem(func_2920_call(), 5)
call_3672 = relay.TupleGetItem(func_2922_call(), 5)
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_3673 = relay.TupleGetItem(func_3390_call(), 2)
call_3674 = relay.TupleGetItem(func_3392_call(), 2)
func_2587_call = mod.get_global_var('func_2587')
func_2589_call = mutated_mod.get_global_var('func_2589')
const_3686 = relay.const([0.642904,0.405446,5.023873,2.804826,-9.170332,5.555426,4.423876,9.783474,-7.012520,-5.030162,1.307813,3.188541,7.374652,-4.343360,3.201655,8.896617,5.524523,-3.219102,-6.137466,-6.477074,-1.434112,-3.246282,-2.711393,7.687940,1.680097,-6.628914,-2.445164,5.872831,6.541932,-0.850102,-9.396562,5.931197,-4.680421,-5.579474,-2.309022,8.323520,-6.441124,-2.772346,1.803015,6.126116,-3.296039,7.065986,-3.660205,-9.908982,-3.819493,-8.161596,-2.823610,9.595735,8.027005,3.136920,-8.528962,0.959553,-5.427396,2.726203,3.791659,-9.484896,-8.227483,-2.328788,0.890395,1.737179,9.471415,-8.439094,4.315601,-2.449822,-6.464139,-3.148972,-4.613963,0.323761,-0.229566,3.926387,-2.473269,0.615085,8.318869,1.321179,-8.639749,0.541556,-2.255340,6.317771,2.009622,-5.684671,0.878154,-2.438263,-4.785595,-7.435555,6.342016,-3.015741,-5.770881,-4.937293,2.770695,-2.432140,-8.338293,1.047757,8.376591,9.073833,-1.452217,-1.982045,-0.783764,-4.140705,0.536632,4.266840,-8.824879,-5.033387,7.986858,-2.296749,-8.362065,-1.324143,-5.835708,6.582283,-9.995709,-1.199251], dtype = "float64")#candidate|3686|(110,)|const|float64
call_3685 = relay.TupleGetItem(func_2587_call(relay.reshape(const_3686.astype('float64'), [22, 5])), 3)
call_3687 = relay.TupleGetItem(func_2589_call(relay.reshape(const_3686.astype('float64'), [22, 5])), 3)
bop_3689 = relay.greater_equal(const_3686.astype('bool'), relay.reshape(call_3685.astype('bool'), relay.shape_of(const_3686))) # shape=(110,)
bop_3692 = relay.greater_equal(const_3686.astype('bool'), relay.reshape(call_3687.astype('bool'), relay.shape_of(const_3686))) # shape=(110,)
bop_3701 = relay.less_equal(call_3685.astype('bool'), relay.reshape(bop_3689.astype('bool'), relay.shape_of(call_3685))) # shape=(22, 5)
bop_3704 = relay.less_equal(call_3687.astype('bool'), relay.reshape(bop_3692.astype('bool'), relay.shape_of(call_3687))) # shape=(22, 5)
func_2702_call = mod.get_global_var('func_2702')
func_2704_call = mutated_mod.get_global_var('func_2704')
var_3712 = relay.var("var_3712", dtype = "float32", shape = (624,))#candidate|3712|(624,)|var|float32
call_3711 = relay.TupleGetItem(func_2702_call(relay.reshape(var_3712.astype('float32'), [13, 12, 4])), 0)
call_3713 = relay.TupleGetItem(func_2704_call(relay.reshape(var_3712.astype('float32'), [13, 12, 4])), 0)
var_3714 = relay.var("var_3714", dtype = "float64", shape = (2, 10, 5))#candidate|3714|(2, 10, 5)|var|float64
bop_3715 = relay.logical_xor(call_3673.astype('uint32'), relay.reshape(var_3714.astype('uint32'), relay.shape_of(call_3673))) # shape=(2, 10, 5)
bop_3718 = relay.logical_xor(call_3674.astype('uint32'), relay.reshape(var_3714.astype('uint32'), relay.shape_of(call_3674))) # shape=(2, 10, 5)
func_2702_call = mod.get_global_var('func_2702')
func_2704_call = mutated_mod.get_global_var('func_2704')
call_3723 = relay.TupleGetItem(func_2702_call(relay.reshape(var_3712.astype('float32'), [13, 12, 4])), 0)
call_3724 = relay.TupleGetItem(func_2704_call(relay.reshape(var_3712.astype('float32'), [13, 12, 4])), 0)
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_3729 = relay.TupleGetItem(func_3655_call(), 0)
call_3730 = relay.TupleGetItem(func_3656_call(), 0)
output = relay.Tuple([call_3671,bop_3701,call_3711,var_3712,bop_3715,call_3723,call_3729,])
output2 = relay.Tuple([call_3672,bop_3704,call_3713,var_3712,bop_3718,call_3724,call_3730,])
func_3733 = relay.Function([var_3712,var_3714,], output)
mod['func_3733'] = func_3733
mod = relay.transform.InferType()(mod)
var_3734 = relay.var("var_3734", dtype = "float32", shape = (624,))#candidate|3734|(624,)|var|float32
var_3735 = relay.var("var_3735", dtype = "float64", shape = (2, 10, 5))#candidate|3735|(2, 10, 5)|var|float64
output = func_3733(var_3734,var_3735,)
func_3736 = relay.Function([var_3734,var_3735,], output)
mutated_mod['func_3736'] = func_3736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mod.get_global_var('func_3287')
func_3289_call = mutated_mod.get_global_var('func_3289')
call_3775 = relay.TupleGetItem(func_3287_call(), 0)
call_3776 = relay.TupleGetItem(func_3289_call(), 0)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_3777 = func_3544_call()
call_3778 = func_3544_call()
func_3639_call = mod.get_global_var('func_3639')
func_3641_call = mutated_mod.get_global_var('func_3641')
call_3785 = relay.TupleGetItem(func_3639_call(), 0)
call_3786 = relay.TupleGetItem(func_3641_call(), 0)
uop_3787 = relay.log2(call_3775.astype('float32')) # shape=(1, 4, 7)
uop_3789 = relay.log2(call_3776.astype('float32')) # shape=(1, 4, 7)
output = relay.Tuple([call_3777,call_3785,uop_3787,])
output2 = relay.Tuple([call_3778,call_3786,uop_3789,])
func_3803 = relay.Function([], output)
mod['func_3803'] = func_3803
mod = relay.transform.InferType()(mod)
mutated_mod['func_3803'] = func_3803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3803_call = mutated_mod.get_global_var('func_3803')
call_3804 = func_3803_call()
output = call_3804
func_3805 = relay.Function([], output)
mutated_mod['func_3805'] = func_3805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_3825 = relay.TupleGetItem(func_3655_call(), 0)
call_3826 = relay.TupleGetItem(func_3656_call(), 0)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_3835 = func_3544_call()
call_3836 = func_3544_call()
func_3118_call = mod.get_global_var('func_3118')
func_3122_call = mutated_mod.get_global_var('func_3122')
const_3857 = relay.const([-5.990374,-1.005171,8.549855,2.399817,-2.262277,0.780246,7.958188,-6.486917,-6.818277,-3.914459,-7.276232,-2.739784,9.369673,4.907151,-9.726311,-9.471099,9.266298,7.496756,-5.829422,6.451348,8.403320,-7.018719,-6.174529,-5.052832,9.345616,1.060202,9.030082,9.452402,2.019147,-2.472411,-3.380898,2.309922,6.999705,-8.651048,3.583134,-3.662343,-9.380656,2.189406,-1.084002,5.425710,-0.768917,5.730290,-2.438603,-5.922197,4.563365,1.309458,-4.108094,5.543838,8.385156,3.819133,6.877384,0.011370,3.097086,-4.920134,-0.876834,0.863471,-6.404636,9.895856,-6.026380,5.675204,-4.348185,9.129962,9.098522,-6.273713,-2.688468,2.868662,0.031187,6.491932,1.991343,-7.945576,4.043718,1.444026,-9.501806,-7.178792,-6.567391,0.991054,-2.431000,6.477980,5.001696,-5.996845,-9.213990,-4.354792,-0.035120,-3.709052,3.406467,-1.419949,-9.849330,2.902665,-9.206403,9.763382,1.341527,0.654063,3.646778,3.688510,-6.947302,-4.933105,3.582399,-0.982010,-0.254796,8.250493,-4.965937,-0.640798,8.402070,2.915811,9.035820,0.887187,6.097048,-9.553918,8.186004,-2.242118], dtype = "float64")#candidate|3857|(110,)|const|float64
const_3858 = relay.const([3.974051,4.573068,2.309885,4.771352,-6.993376,1.046390,7.775644,8.876688,7.077563,8.036485,6.978879,-7.548054,2.034767,-7.179264,0.347924,4.236941,1.454111,9.134051,-6.999686,-4.021205,-4.025521,-5.890326,4.119197,4.285409,-1.190109,8.815265,-8.645553,2.977735,-1.554350,0.896887,-2.237863,-1.033726,4.871745,4.029283,1.394725,-4.034799,3.838061,4.748901,-9.193272,1.104884,-6.444875,-2.026392,-4.756518,-9.631531,0.168219,7.540098,4.756995,3.148201,8.952847,-1.479441,6.826445,-8.426206,1.210396,4.771870,-6.702260,7.452213,9.024041,-7.314976,6.398454,2.563228,-3.814729,-7.305491,-8.329115,-4.294571,-3.632591,-0.681109,5.409313,-2.010283,8.797349,-3.526083,3.729381,-0.776041,8.774676,-5.225374,0.624583,8.337541,-2.758070,5.045570,0.882440,-8.534187,-3.308064,0.061310,-0.149341,2.742063,3.888177,1.590843,8.051237,-1.366124,-7.732605,8.306419,-1.444332,3.737174,-1.639870,2.481086,-0.398295,-7.988712,7.295371,-5.441162,9.605281,4.061503], dtype = "float64")#candidate|3858|(100,)|const|float64
call_3856 = relay.TupleGetItem(func_3118_call(relay.reshape(const_3857.astype('float64'), [110,]), relay.reshape(const_3858.astype('float64'), [100,]), ), 4)
call_3859 = relay.TupleGetItem(func_3122_call(relay.reshape(const_3857.astype('float64'), [110,]), relay.reshape(const_3858.astype('float64'), [100,]), ), 4)
output = relay.Tuple([call_3825,call_3835,call_3856,const_3857,const_3858,])
output2 = relay.Tuple([call_3826,call_3836,call_3859,const_3857,const_3858,])
func_3892 = relay.Function([], output)
mod['func_3892'] = func_3892
mod = relay.transform.InferType()(mod)
mutated_mod['func_3892'] = func_3892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mutated_mod.get_global_var('func_3892')
call_3893 = func_3892_call()
output = call_3893
func_3894 = relay.Function([], output)
mutated_mod['func_3894'] = func_3894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3920 = relay.TupleGetItem(func_2920_call(), 3)
call_3921 = relay.TupleGetItem(func_2922_call(), 3)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_3931 = relay.const(-8.717800, dtype = "float64")#candidate|3931|()|const|float64
const_3932 = relay.const([[3.772218,-5.337490,9.226349,1.328907,2.551596,0.106548,-2.131874,2.918865,6.719805,9.581136,4.871420,4.453057,-2.441524,-5.257587,3.287423,-3.034586,-3.100763,-7.118592,-6.757913,4.261250,7.885133,-0.950795,-6.737337,-7.702486,-6.257073,4.958055,7.888946,9.306721,5.106542,-4.266118,-7.822603,7.153331,3.518936,-6.498842,5.296530,-0.036821,-5.211146,5.245679,-2.050965,3.137402,5.645457,-8.191602,3.046948,-2.283822,4.341448,3.011762,4.888061,2.789517,-8.849685,-6.297483,6.638534,-6.424115,9.884563,-2.546130,4.393325,-8.516010,-1.087650,1.207052,-2.500752,-9.938710,1.993790,7.270040,-7.727671,7.876814,5.298672,7.530228,-7.852514,-9.156446,7.481270,5.428386,-7.335233,3.999748,7.261558,-1.927471,-7.754945,5.344675,-6.214387,-3.107556,2.750752,9.362242,0.482248,-2.616543,-8.116806,1.270875,8.109906,7.551078,-9.331597,0.385081,1.824029,5.600267,-8.075991,3.361770,-4.330108,-9.039788,-3.510552,-4.865529,-9.467479,9.646614,7.632259,-5.140620,-6.304612,3.647678,-6.794732,-8.110606,-1.156385,3.459668,-6.813202,-6.667092,-5.033442,2.338669]], dtype = "float64")#candidate|3932|(1, 110)|const|float64
call_3930 = relay.TupleGetItem(func_2062_call(relay.reshape(const_3931.astype('float64'), []), relay.reshape(const_3932.astype('float64'), [10, 1, 11]), ), 3)
call_3933 = relay.TupleGetItem(func_2065_call(relay.reshape(const_3931.astype('float64'), []), relay.reshape(const_3932.astype('float64'), [10, 1, 11]), ), 3)
output = relay.Tuple([call_3920,call_3930,const_3931,const_3932,])
output2 = relay.Tuple([call_3921,call_3933,const_3931,const_3932,])
func_3947 = relay.Function([], output)
mod['func_3947'] = func_3947
mod = relay.transform.InferType()(mod)
output = func_3947()
func_3948 = relay.Function([], output)
mutated_mod['func_3948'] = func_3948
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3949 = relay.var("var_3949", dtype = "float32", shape = (5, 12, 11))#candidate|3949|(5, 12, 11)|var|float32
const_3950 = relay.const([[[-2.520149,0.175784,4.529582,-5.693917,5.117816,-7.561723,-9.035869,-6.075783,7.165860,5.591660,-7.117641],[-4.317745,-7.521993,5.457156,9.918244,-4.652373,6.970341,5.818047,-4.561999,3.570773,1.027291,-6.716619],[6.267387,-9.063044,-8.544227,-9.572024,-5.341426,2.054313,-4.809004,5.277460,8.385641,-6.070143,0.821358],[-2.186185,2.280293,1.751030,8.262211,-2.003137,2.066917,2.239787,5.805217,-2.174552,-7.878990,-0.584460],[-4.924431,-9.672884,-6.080199,-9.752231,0.284617,1.628260,-5.976511,0.163757,-2.815226,-0.591109,-1.700131],[6.972713,7.137499,9.426172,7.938411,4.577483,8.956358,-7.276972,-4.258883,0.045045,4.918260,-7.799627],[-2.386328,2.609653,-8.125339,-6.109230,7.022661,-0.421859,2.451474,-0.477807,8.687128,-0.167596,-3.760662],[-7.696200,5.906934,-6.906996,-3.976224,-0.347430,-2.433584,-9.389534,-4.537611,9.474353,-2.018691,-8.808417],[4.213455,3.345075,-7.080133,1.234872,-7.555355,3.207666,0.217207,-2.944725,2.942386,-7.444712,-8.899738],[-1.755801,9.159434,-0.007759,8.928968,9.849443,8.160763,7.125710,-8.777981,-7.080432,4.907863,-5.481920],[6.444869,-6.168850,-7.543768,-9.080846,0.843486,0.673474,-2.987253,9.632050,-7.263036,-1.725125,2.940068],[-2.011672,-1.622901,-4.236998,-7.282171,7.593488,7.010862,-1.065246,-6.258101,-3.306072,3.286390,0.672326]],[[5.926412,3.202072,9.546455,1.038592,-6.894960,1.129142,4.617965,-3.553908,-8.313224,1.050990,8.130571],[7.672177,7.427517,-6.726521,9.882260,-6.621132,-7.765955,8.111955,-6.474262,-9.111289,-8.243783,4.337049],[5.300830,8.017000,0.192853,8.799994,7.249490,9.641444,-4.083329,0.046911,7.764920,-6.202736,-9.900009],[4.395947,-5.358778,3.917815,5.074489,-3.521544,-9.113151,1.378627,2.891364,-8.539549,8.567109,8.640546],[4.645622,-3.423303,-1.180754,-9.944149,-4.543819,3.025178,8.387388,2.503233,-3.589491,0.548491,0.143856],[-0.283328,8.594524,2.251253,-0.869007,-3.247850,-3.689614,-0.227675,4.125786,6.869053,7.330154,3.469871],[6.377302,7.972951,-7.577018,-3.089179,2.976825,-7.453496,2.333138,-5.294082,-4.027362,-5.163161,1.430159],[-8.022922,7.072233,-7.808362,-4.138485,-3.808991,-0.827245,2.271436,-4.303496,-2.573754,1.014383,1.421847],[7.951646,-1.769049,-2.428847,-8.956013,-8.325692,4.541989,-5.037736,-2.058694,1.841818,-2.358677,-1.156624],[-9.673070,7.097718,7.440826,-6.597189,3.427306,-2.499231,6.167604,-6.240228,-9.247670,-3.147437,7.053577],[0.140855,-6.019998,-9.531302,-7.663656,-1.549721,6.099561,8.010750,-0.580744,4.004629,9.732583,-3.662720],[5.443691,-4.106280,2.883339,5.098649,0.490971,-6.017953,4.921061,-3.143505,3.858176,-5.239291,-6.796458]],[[4.286571,0.993713,8.325457,-3.705487,-7.536886,-1.158662,8.445083,7.877719,-2.831598,0.885746,-0.316178],[6.405137,-3.787945,-1.515144,-7.043217,7.086767,2.660174,-5.143766,9.647441,-5.107877,-4.619958,8.629081],[-3.299795,-0.314261,8.774869,3.492350,-8.588062,9.287653,-4.725807,-0.067571,-6.281669,-4.407204,-4.284804],[-9.201357,-9.482772,9.109629,-7.362633,-5.232284,-2.885975,5.879770,0.508332,6.624591,-1.346371,-9.068480],[-8.582640,8.577852,-1.991668,9.453452,-3.183740,9.316168,-3.188409,-5.534713,2.217762,-7.945690,5.344406],[2.191413,-9.013159,4.444642,7.752574,8.580035,-9.756430,7.847238,3.904781,6.686025,-8.198001,-6.627586],[-2.824482,4.070726,3.395561,1.770224,-8.229687,7.426893,7.867253,6.227488,4.134424,9.443336,6.710383],[-5.660988,2.927812,-7.623827,-6.740329,-5.274493,3.649780,-3.308781,5.147085,-6.055597,5.605396,2.553773],[-4.435662,4.902892,4.089636,1.962116,3.381014,2.550702,0.355500,5.799458,-2.021410,-9.524905,0.653959],[9.187356,-2.944894,-4.140185,2.846375,4.333390,-8.176968,8.005400,0.296544,-3.899694,4.398317,7.079106],[-8.496162,-8.840724,-0.261646,-1.515382,-8.238902,2.919595,7.687714,-3.026270,7.857928,-7.659354,-0.180913],[6.563731,-3.600925,6.478272,-8.639361,7.830414,9.381769,9.660915,-2.399294,4.996352,5.256869,-1.740183]],[[0.214303,-5.808959,-9.195579,-5.476557,-3.005346,-2.810857,-8.919496,-3.515897,-4.996113,6.141890,-2.563158],[9.529493,-8.344017,3.718467,2.128306,1.675002,-4.342302,1.461331,-7.454382,7.260480,-1.290234,-0.148173],[0.852894,4.778367,-3.544153,3.663835,8.370032,7.317555,-8.128715,-7.630417,-4.217254,-0.405025,8.591371],[4.249487,6.990069,-7.214121,-2.882114,-7.972478,-0.286433,8.870201,-4.514872,1.148676,-1.339643,-3.516978],[7.143795,-0.119011,-4.756067,-4.202542,9.760567,0.789047,-2.964367,-6.893197,-2.728384,9.130041,-6.527275],[4.538007,9.629936,-2.545181,-3.927031,-5.123571,9.171155,6.452128,6.528567,3.217075,-2.628153,-1.353296],[4.653738,0.042260,6.459114,-2.311079,-7.653244,6.226059,-5.384120,8.666602,-3.786572,-6.150943,-9.664597],[6.741251,4.128406,-6.635541,1.365256,-1.228773,1.862733,3.206874,-3.594079,-9.676508,0.338858,0.308305],[-9.690957,-7.701012,-4.662392,-8.637724,7.372947,6.350024,8.941151,-0.598516,-6.790874,3.049756,-8.161023],[-3.810548,-3.937297,6.610357,-7.455664,3.260152,1.801645,0.934596,-0.196260,5.823054,3.784143,-2.862286],[-9.881050,-2.949116,6.117166,0.642725,-0.828823,2.649032,-0.998669,-4.533223,2.536333,2.565551,-7.147478],[-8.873768,0.280234,-5.573548,-0.379836,4.284261,4.915488,7.189508,1.337524,-0.190359,8.111117,-6.489060]],[[1.558791,-9.782647,-2.252543,7.227448,4.909949,4.954626,1.108451,2.491273,-6.742581,2.749594,-7.767063],[-9.322846,8.534445,9.023792,-5.052938,-7.902948,6.956395,-3.855760,9.409105,-9.435378,-4.413604,9.767860],[9.897069,0.053117,9.836431,5.294964,-0.303767,0.144772,-4.372093,-8.107117,-4.574270,-5.950353,2.274664],[6.628591,1.829874,5.270431,4.880886,7.705775,-8.499696,-2.716888,8.109422,6.112600,2.334041,9.707147],[-9.947686,6.334040,0.557671,-5.787070,-5.297824,4.253778,1.752323,7.199023,9.177316,9.373081,-8.859896],[0.742789,6.457209,0.163489,0.165294,-8.494940,-2.096931,-8.582560,-4.914392,-6.674202,-2.454443,-9.438818],[8.981168,-6.742769,-9.696603,-9.173100,6.778604,7.629494,-7.422213,0.679046,2.127156,0.069679,8.338396],[4.408525,-0.844064,1.314598,1.196245,-5.251442,3.836632,2.683432,-0.526587,-4.479024,9.769466,-4.876320],[-1.788111,6.029848,-2.422151,7.050850,-3.615117,4.869504,8.383166,5.200663,-3.790205,6.216931,-8.138304],[6.508158,-5.592601,-6.104231,5.202992,1.999227,5.107488,-3.383038,-4.817893,3.063937,-0.673735,2.455480],[2.397011,9.990746,9.101598,-1.358006,5.125552,-3.739238,4.577800,-5.250233,-5.563055,5.955713,-6.421755],[5.971945,5.293813,-6.907959,8.055211,5.321907,-8.626168,-9.577267,0.834876,-8.310354,-1.887022,-3.866540]]], dtype = "float32")#candidate|3950|(5, 12, 11)|const|float32
bop_3951 = relay.mod(var_3949.astype('float32'), relay.reshape(const_3950.astype('float32'), relay.shape_of(var_3949))) # shape=(5, 12, 11)
bop_3954 = relay.less_equal(bop_3951.astype('bool'), relay.reshape(const_3950.astype('bool'), relay.shape_of(bop_3951))) # shape=(5, 12, 11)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_3960 = func_3544_call()
call_3961 = func_3544_call()
output = relay.Tuple([bop_3954,call_3960,])
output2 = relay.Tuple([bop_3954,call_3961,])
func_3973 = relay.Function([var_3949,], output)
mod['func_3973'] = func_3973
mod = relay.transform.InferType()(mod)
mutated_mod['func_3973'] = func_3973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3974 = relay.var("var_3974", dtype = "float32", shape = (5, 12, 11))#candidate|3974|(5, 12, 11)|var|float32
func_3973_call = mutated_mod.get_global_var('func_3973')
call_3975 = func_3973_call(var_3974)
output = call_3975
func_3976 = relay.Function([var_3974], output)
mutated_mod['func_3976'] = func_3976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2845_call = mod.get_global_var('func_2845')
func_2846_call = mutated_mod.get_global_var('func_2846')
call_4004 = func_2845_call()
call_4005 = func_2845_call()
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_4019 = relay.TupleGetItem(func_2512_call(), 1)
call_4020 = relay.TupleGetItem(func_2513_call(), 1)
output = relay.Tuple([call_4004,call_4019,])
output2 = relay.Tuple([call_4005,call_4020,])
func_4021 = relay.Function([], output)
mod['func_4021'] = func_4021
mod = relay.transform.InferType()(mod)
mutated_mod['func_4021'] = func_4021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4021_call = mutated_mod.get_global_var('func_4021')
call_4022 = func_4021_call()
output = call_4022
func_4023 = relay.Function([], output)
mutated_mod['func_4023'] = func_4023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_4027 = func_3544_call()
call_4028 = func_3544_call()
func_2539_call = mod.get_global_var('func_2539')
func_2542_call = mutated_mod.get_global_var('func_2542')
var_4033 = relay.var("var_4033", dtype = "float64", shape = (100,))#candidate|4033|(100,)|var|float64
call_4032 = func_2539_call(relay.reshape(var_4033.astype('float64'), [2, 10, 5]), relay.reshape(var_4033.astype('float64'), [2, 10, 5]), )
call_4034 = func_2539_call(relay.reshape(var_4033.astype('float64'), [2, 10, 5]), relay.reshape(var_4033.astype('float64'), [2, 10, 5]), )
output = relay.Tuple([call_4027,call_4032,var_4033,])
output2 = relay.Tuple([call_4028,call_4034,var_4033,])
func_4038 = relay.Function([var_4033,], output)
mod['func_4038'] = func_4038
mod = relay.transform.InferType()(mod)
var_4039 = relay.var("var_4039", dtype = "float64", shape = (100,))#candidate|4039|(100,)|var|float64
output = func_4038(var_4039)
func_4040 = relay.Function([var_4039], output)
mutated_mod['func_4040'] = func_4040
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4042 = relay.var("var_4042", dtype = "uint16", shape = (15, 1, 14))#candidate|4042|(15, 1, 14)|var|uint16
const_4043 = relay.const([[[10,3,-9,6,-7,10,-4,4,-10,-7,5,-5,8,1],[-4,-3,4,-8,2,-9,-5,-3,-7,4,4,-10,-3,-2],[-10,-4,-7,-9,-2,-3,5,3,9,6,-5,-7,-4,-9],[-3,9,-3,10,-7,-10,9,3,-3,3,2,-2,-2,7],[-8,-4,-5,-6,5,10,-4,2,4,-7,-4,3,-10,5],[3,-9,-6,4,5,2,4,5,-6,1,-4,9,9,-6]],[[-6,-10,-10,-2,1,8,3,-7,3,7,10,-9,8,-2],[9,-5,-8,-4,5,3,-1,3,10,-3,3,4,1,8],[1,-8,10,5,-10,4,-6,-3,-7,-1,6,2,5,1],[-9,-7,10,3,9,-6,9,-6,7,10,-6,3,-6,-1],[2,6,2,-4,-9,10,6,-6,-6,-2,10,8,-4,7],[-9,10,4,-7,-1,1,-9,-5,9,-2,4,9,-5,-9]],[[2,-8,8,-6,-5,-9,3,6,10,-9,-5,-5,6,-2],[-3,-9,-8,-7,4,-9,6,7,9,-3,7,10,-4,2],[1,10,-6,8,-7,-10,-8,-2,-10,-4,-2,-10,1,-4],[6,-7,-9,-10,8,-9,-5,-6,2,7,-6,-3,-8,-1],[4,5,1,-9,-3,-5,9,5,-5,-6,10,-8,-4,9],[5,-2,5,-1,3,9,10,-4,10,-4,-2,-1,-6,1]],[[2,-2,9,-6,-5,-3,8,2,-5,-9,-8,1,5,-2],[-3,-1,-2,3,-8,4,-7,-10,8,-5,10,2,-10,8],[5,4,-3,-4,-7,4,8,-9,-8,2,-10,-1,-4,8],[5,7,6,-9,-8,5,2,1,9,6,8,3,6,10],[-8,2,-4,3,-2,-10,5,-8,-5,8,-10,3,-2,-7],[2,-8,6,4,-1,-2,9,-5,-5,3,1,-6,-6,8]],[[5,6,-5,-10,4,-2,2,8,-4,-10,-6,-1,-6,8],[5,-2,3,2,2,-10,-7,-1,-4,2,4,9,7,-6],[8,-7,-10,-5,-8,-3,-8,-9,3,6,1,-9,2,-4],[9,-3,4,10,-10,-8,-4,1,4,-7,-1,6,2,6],[3,-2,10,1,-7,9,-8,10,-10,3,2,-10,-4,-5],[-4,-8,-3,-3,-10,-8,-5,-6,5,-4,6,8,-1,1]],[[7,-10,10,-1,-2,7,-7,9,-5,-5,-3,-5,10,9],[2,-5,-7,-1,6,-2,-4,-8,-8,-3,4,-3,-8,-5],[2,8,-3,2,-1,-9,-4,-3,9,-1,10,10,-1,10],[1,-8,7,-8,2,-2,-4,-7,-1,-9,6,9,-2,-10],[2,-4,5,-10,9,-3,-8,1,-4,-10,-3,-7,-7,-4],[3,-5,6,-2,1,-3,7,-1,-1,-7,-5,1,-4,-6]],[[5,1,6,5,-5,-2,8,-9,3,10,-6,-2,1,-8],[4,-7,4,6,-6,-1,-9,-1,10,2,2,9,8,-9],[-7,-6,-1,-9,-5,-4,-8,-3,-7,4,6,3,7,-6],[-5,3,-3,2,-4,-8,6,1,8,10,10,-5,9,4],[1,-10,4,10,-4,3,1,-8,-5,10,-5,-9,4,1],[3,1,5,4,-7,-9,5,1,-3,-3,-8,-10,-1,9]],[[-4,-1,6,-4,-5,10,-3,5,9,3,4,10,9,6],[10,7,6,4,-2,-2,-9,9,1,9,9,-4,8,-7],[-6,6,8,4,3,-7,8,-2,-2,-8,-4,-5,-9,-7],[4,3,-7,-10,4,3,3,4,7,-8,-6,4,-5,4],[1,-8,-3,7,-2,9,10,-5,9,-4,-3,7,-3,1],[3,10,5,1,1,-10,-6,8,8,-8,-1,5,-9,3]],[[-7,-7,-8,-4,-5,2,4,8,2,5,7,9,8,-2],[-8,8,-9,-4,10,-1,5,-2,9,7,3,-1,9,-8],[4,3,-5,5,-6,3,9,2,9,-2,-1,10,-3,4],[-3,-9,2,-8,5,-1,6,-6,9,-8,-1,9,-1,7],[1,8,-4,10,-2,-3,4,7,-7,5,-2,-6,-5,-6],[3,-2,7,-8,-6,-8,-7,-5,-4,-8,-9,1,-6,-6]],[[-2,-7,8,-9,9,5,-6,-6,-4,1,-5,-3,4,6],[10,10,6,7,9,8,-5,-5,-6,3,4,-9,7,-3],[-5,10,3,-5,1,5,-10,-10,-6,8,-6,1,9,8],[4,-6,2,-2,7,-6,-3,-8,3,-10,3,-10,-2,-10],[3,-6,1,3,7,-10,7,3,-6,3,-1,6,-2,4],[9,5,-3,-6,1,10,9,4,-4,3,10,-9,8,4]],[[4,-6,-3,5,-9,2,4,-2,10,6,3,-7,-5,5],[-4,5,-8,-2,-1,-10,-2,2,4,9,-10,-1,-6,7],[5,-7,10,8,5,2,9,-8,-4,-6,-6,4,2,8],[-4,-1,6,7,-4,-5,-4,-6,-9,-3,7,-9,8,7],[-9,-8,-2,1,9,-4,-2,1,-6,-7,1,5,-3,1],[10,-9,-4,3,10,-2,1,-1,4,6,-10,2,7,1]],[[4,9,-1,4,-9,-1,-10,-7,10,-3,-1,4,-4,-7],[6,10,2,-3,-10,-10,3,-8,-6,-1,3,3,-2,9],[5,-8,-6,10,-8,4,-9,6,6,2,-9,10,-8,-7],[-10,-8,-4,4,5,-9,7,2,8,6,10,-7,3,-10],[-10,3,5,5,-8,-1,-4,-7,-6,7,-6,9,4,-6],[3,10,-5,5,4,1,-10,-6,-7,-7,3,6,-8,-5]],[[10,9,-7,9,2,6,-4,8,1,8,9,10,9,9],[-10,-2,-8,-4,-10,9,-6,7,-3,-2,9,4,-7,-9],[-2,-4,5,-3,-6,9,1,-7,-4,7,-9,6,2,7],[-6,-4,7,1,5,-6,-2,-9,5,-3,2,8,10,-1],[-6,10,7,8,-5,7,-4,2,-1,10,1,-5,-3,6],[1,-6,8,-8,-1,10,-7,7,-1,7,2,-8,-1,7]],[[9,9,-3,-6,-2,-7,-1,10,-3,7,-8,7,-2,-6],[-9,-10,8,-8,-6,-3,7,3,8,-3,-2,6,5,-1],[-10,1,-10,6,10,-9,8,-5,4,10,1,3,-6,-5],[-4,-1,3,-2,4,-1,3,3,3,-6,-5,-9,2,2],[-10,-2,-3,-9,-6,3,2,-4,-5,-8,-4,5,1,-8],[5,4,6,2,-8,8,-3,-3,5,9,6,-10,2,-10]],[[9,-5,-7,-10,4,2,2,-7,1,9,9,5,5,-4],[1,9,3,4,4,2,-5,-3,4,-1,10,-10,10,-4],[3,2,-3,3,7,-7,3,-1,4,5,-4,1,-8,4],[-8,-3,-8,4,7,9,-7,7,6,8,3,-9,2,4],[-3,-6,-7,-10,3,6,1,4,-4,8,10,-1,9,-2],[2,-9,-4,-3,-3,8,7,5,-3,-8,3,-8,-1,-8]]], dtype = "uint16")#candidate|4043|(15, 6, 14)|const|uint16
bop_4044 = relay.greater_equal(var_4042.astype('bool'), const_4043.astype('bool')) # shape=(15, 6, 14)
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_4050 = relay.TupleGetItem(func_3655_call(), 0)
call_4051 = relay.TupleGetItem(func_3656_call(), 0)
output = relay.Tuple([bop_4044,call_4050,])
output2 = relay.Tuple([bop_4044,call_4051,])
func_4052 = relay.Function([var_4042,], output)
mod['func_4052'] = func_4052
mod = relay.transform.InferType()(mod)
mutated_mod['func_4052'] = func_4052
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4053 = relay.var("var_4053", dtype = "uint16", shape = (15, 1, 14))#candidate|4053|(15, 1, 14)|var|uint16
func_4052_call = mutated_mod.get_global_var('func_4052')
call_4054 = func_4052_call(var_4053)
output = call_4054
func_4055 = relay.Function([var_4053], output)
mutated_mod['func_4055'] = func_4055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_4063 = func_3544_call()
call_4064 = func_3544_call()
uop_4100 = relay.sigmoid(call_4063.astype('float64')) # shape=(28,)
uop_4102 = relay.sigmoid(call_4064.astype('float64')) # shape=(28,)
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_4116 = relay.TupleGetItem(func_3655_call(), 0)
call_4117 = relay.TupleGetItem(func_3656_call(), 0)
func_3973_call = mod.get_global_var('func_3973')
func_3976_call = mutated_mod.get_global_var('func_3976')
const_4140 = relay.const([-3.486825,-2.310342,5.886722,1.786974,5.802758,-1.690706,-3.133483,1.575534,-2.039706,4.435341,2.682387,-9.720626,0.840948,2.175095,5.773266,-3.695740,-0.338864,1.872868,3.020355,-7.041076,-2.893596,5.280526,-5.701137,-5.429163,1.292262,-3.526398,-2.697197,-2.984096,4.268417,-4.037614,-3.553327,-1.987476,-4.616205,-3.849977,-4.100353,-1.792583,8.795675,8.624205,-5.070108,-4.744580,-3.104974,-2.502095,-5.784867,-6.658517,-6.629485,-8.423501,5.720302,0.643409,-5.774922,6.442196,9.159977,6.900097,1.485320,-8.649116,1.938823,-4.335720,5.199823,-5.623400,7.169257,1.869457,-3.410023,-6.899056,7.539300,3.574678,1.218220,-6.750752,-2.484702,3.763418,1.250972,8.153168,5.430576,-8.110691,8.769780,-7.741060,1.203165,-1.217179,0.272414,7.988686,4.023937,-7.422479,5.667177,5.371185,1.805280,-8.068329,-5.750639,4.013890,5.127003,6.879207,-6.914814,0.972747,8.365769,0.156770,-2.545062,5.174501,1.727799,-8.673737,4.080262,-5.474380,-8.561276,9.858026,0.048294,-9.289187,-8.350970,0.773619,0.131308,-6.318847,-8.441903,6.860172,-4.126266,-6.635493,6.661025,-3.680195,-9.801107,7.557371,4.424842,-4.996774,5.145070,1.150475,-0.885016,-3.285413,2.828090,-5.718642,6.231061,-0.397447,5.111832,6.463636,2.146708,0.128434,1.965755,2.234081,7.299301,6.201062,-0.889887,-2.907556,2.613509,6.695178,7.026117,-5.007411,2.915430,-5.948380,-5.905851,4.528149,2.393143,5.511012,8.995995,-1.815502,-3.390027,5.806402,-2.560384,1.063021,6.495389,2.064863,1.165188,7.971348,-2.322972,8.645104,8.154782,9.370587,1.925527,9.513457,2.535267,0.752354,3.323671,-6.357700,-2.030171,6.809888,-2.116270,-2.065035,6.823862,9.956520,8.600579,-9.777462,7.025846,4.285980,-7.670595,-2.465083,-9.260669,-9.173295,-9.870884,-4.453897,-9.276620,-7.065672,-8.415547,-9.336597,-6.086145,8.886870,-3.911212,0.313422,1.501105,-3.483614,9.950215,1.547067,-3.447550,-7.205278,6.591340,3.630959,-9.237372,-2.635957,-9.009527,-3.085082,-3.665303,-7.796854,1.785589,1.225020,1.652559,1.632459,-3.661042,-3.187790,-1.087533,8.035884,2.473602,4.720215,8.689903,-0.453064,2.862007,-6.976899,0.018354,-1.380957,-4.790768,6.690401,-6.213962,0.218429,-9.630803,2.897178,-5.744644,-2.705409,-3.670855,8.822156,0.411732,8.563296,0.722790,1.782175,8.805845,7.428012,3.184204,6.984812,9.245949,-0.368735,-4.751561,-9.191912,-5.584924,7.270047,9.448269,-8.479780,-2.015948,1.847641,-0.211822,-5.990075,-4.559074,4.262210,1.447671,3.334353,4.974615,-1.819491,-8.452196,-1.487973,6.528298,1.521809,9.277588,4.765215,5.797373,9.050345,1.571729,1.810174,4.051908,3.384292,9.030485,-8.781617,-4.527082,6.703389,8.717815,-5.548050,4.562562,0.982139,2.119841,-3.362281,8.729613,-7.925595,-2.288231,7.294461,7.110829,-7.641869,9.297574,8.741928,9.418126,-0.001066,5.242083,1.014918,-4.593204,1.685192,5.331193,9.579357,3.343766,-3.374775,4.871102,1.013877,-4.740779,-4.888663,-4.000304,-2.398847,-4.715974,6.028249,6.492646,-9.108230,1.289552,0.940769,0.165426,-8.208137,1.926806,-5.692706,-5.747131,2.991496,7.739246,-1.739848,1.282016,2.179330,-8.629045,3.740287,4.971320,4.112260,4.730279,-1.068496,6.971413,4.740989,6.999687,-9.410766,-3.194236,-4.414471,5.113454,9.038807,0.200004,-5.579114,7.998938,9.349088,3.065552,-3.944535,-8.931836,6.004778,5.706553,-6.821200,0.134308,-7.282506,-9.955764,9.269075,3.580021,-7.495593,-0.045480,-0.415776,6.665773,-2.002128,8.467157,8.308482,3.910443,3.627135,-1.591278,0.186820,-9.825975,9.919860,5.301259,-3.213636,7.952635,6.937163,3.235837,-0.552766,-6.758736,9.009381,5.689967,0.824748,-0.993336,8.350418,-2.345123,-0.715258,-5.933886,6.374203,-1.226536,-9.159044,-9.653792,7.550344,-7.863127,-6.393121,0.615926,-4.445197,6.754679,3.679290,-3.192255,-9.041441,-7.305236,-8.264790,-2.604569,-2.016945,7.227799,-1.758562,-4.898837,-6.707949,4.731612,1.379204,-8.810591,5.978909,6.169973,1.577931,3.123215,-3.402218,-4.921292,-4.751959,-8.577803,-7.129058,-5.663930,-4.919519,-2.690701,9.466305,5.326031,-3.328850,-2.250529,2.873946,2.326217,1.893063,-6.034059,-6.750220,-2.101003,5.762638,6.607679,3.227864,0.425938,-0.610097,-6.855553,8.912690,9.272436,6.710136,-3.524315,3.168627,-0.196077,-8.845592,0.699146,2.548244,-3.726619,-7.966121,-9.407512,8.806231,5.924644,-2.131808,7.391982,-2.965940,0.713651,-4.254574,-1.830586,5.501706,-0.793074,-1.156811,-6.200449,-5.249664,-0.367618,-2.741657,-5.705731,-5.931215,-3.758123,5.006417,1.096860,-7.076723,8.001505,-4.212240,-0.118138,-6.670845,4.910045,-9.686462,6.949923,-2.422783,-0.402155,-1.896884,-3.734104,-8.303011,4.867312,-0.955438,0.983749,-6.062737,8.118134,9.961746,-0.649868,4.976532,-4.405381,-3.293727,-4.933962,2.920237,0.815307,6.914419,8.317709,-2.598804,0.678387,2.410806,8.086151,3.272922,-4.209942,0.652712,3.496816,-6.865024,-6.605798,8.743305,-0.789726,4.825627,-5.237315,9.779050,5.888170,6.950983,0.865711,4.220735,-1.885461,8.674645,9.177884,1.072083,0.008757,-7.628026,-8.498984,-5.951685,6.299721,8.953320,-3.217406,1.940345,-4.630995,-3.170995,7.817641,6.741913,3.451097,-6.369797,9.677564,0.089204,0.282572,-9.956628,6.042360,-2.821051,6.082940,-0.951858,1.704628,8.629057,-0.821341,4.883686,8.475476,8.869140,5.925878,-7.404514,-2.271728,-8.084750,9.889816,6.429120,4.492204,8.399701,9.849287,1.800228,6.984821,2.158244,-9.802454,8.049179,4.026026,-6.721591,-4.052765,7.532804,-7.587033,7.718825,-8.147316,-0.288749,-7.581548,-8.504661,-8.584725,-4.668277,-2.660246,8.581310,-9.269636,0.270054,-3.776598,5.175506,-5.517016,6.341260,-2.167640,-0.954251,6.148030,-6.763572,5.553396,-4.271098,-9.369283,4.014218,-2.537211,-2.181371,-4.798362,-5.251592,0.835960,5.484055,-3.143601,7.929274,3.703336,5.559891,-8.445873,5.742331,9.339142,6.730800,-8.122215,-1.041621,-2.082694,-1.307696,-2.736014,5.346104,-7.329154,7.608365,2.990738,0.557996,6.361479,1.266401,-3.742276,8.168565,-6.202063,-5.717538,8.038212,9.123772,1.906930,-2.557991,-0.912205,4.677937,3.411168,6.557078,3.516938,7.505261,-8.146383,5.801229,0.241910,-5.028400,6.201528,0.706095,0.525056,-0.758986,-5.630507,9.928438,-1.000703,5.297297,2.031640,-8.478743,9.964242,3.518935,4.105233,-0.527321,0.430391,-8.537772,3.783735,-3.279880,4.455211,8.682232,3.924654,-0.910746,-6.809959,5.094979,0.740652,-5.951130,-3.182903,-1.706126,-2.951390,-0.521411,6.611078,4.795300,-6.496778,6.733989,-1.460788,4.344906,0.872038,-9.592240], dtype = "float32")#candidate|4140|(660,)|const|float32
call_4139 = relay.TupleGetItem(func_3973_call(relay.reshape(const_4140.astype('float32'), [5, 12, 11])), 1)
call_4141 = relay.TupleGetItem(func_3976_call(relay.reshape(const_4140.astype('float32'), [5, 12, 11])), 1)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_4147 = relay.TupleGetItem(func_2526_call(), 0)
call_4148 = relay.TupleGetItem(func_2528_call(), 0)
func_3973_call = mod.get_global_var('func_3973')
func_3976_call = mutated_mod.get_global_var('func_3976')
call_4157 = relay.TupleGetItem(func_3973_call(relay.reshape(const_4140.astype('float32'), [5, 12, 11])), 0)
call_4158 = relay.TupleGetItem(func_3976_call(relay.reshape(const_4140.astype('float32'), [5, 12, 11])), 0)
func_1598_call = mod.get_global_var('func_1598')
func_1602_call = mutated_mod.get_global_var('func_1602')
var_4166 = relay.var("var_4166", dtype = "float32", shape = ())#candidate|4166|()|var|float32
call_4165 = func_1598_call(relay.reshape(var_4166.astype('float32'), []), relay.reshape(call_4139.astype('float32'), [1, 4, 7]), )
call_4167 = func_1598_call(relay.reshape(var_4166.astype('float32'), []), relay.reshape(call_4139.astype('float32'), [1, 4, 7]), )
output = relay.Tuple([uop_4100,call_4116,call_4139,const_4140,call_4147,call_4157,call_4165,var_4166,])
output2 = relay.Tuple([uop_4102,call_4117,call_4141,const_4140,call_4148,call_4158,call_4167,var_4166,])
func_4168 = relay.Function([var_4166,], output)
mod['func_4168'] = func_4168
mod = relay.transform.InferType()(mod)
var_4169 = relay.var("var_4169", dtype = "float32", shape = ())#candidate|4169|()|var|float32
output = func_4168(var_4169)
func_4170 = relay.Function([var_4169], output)
mutated_mod['func_4170'] = func_4170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_4193 = relay.TupleGetItem(func_2945_call(), 0)
call_4194 = relay.TupleGetItem(func_2947_call(), 0)
func_2160_call = mod.get_global_var('func_2160')
func_2163_call = mutated_mod.get_global_var('func_2163')
var_4204 = relay.var("var_4204", dtype = "float32", shape = (144, 1))#candidate|4204|(144, 1)|var|float32
call_4203 = func_2160_call(relay.reshape(var_4204.astype('float32'), [2, 6, 12]))
call_4205 = func_2160_call(relay.reshape(var_4204.astype('float32'), [2, 6, 12]))
uop_4209 = relay.asinh(var_4204.astype('float32')) # shape=(144, 1)
var_4216 = relay.var("var_4216", dtype = "float32", shape = (2, 6, 12))#candidate|4216|(2, 6, 12)|var|float32
bop_4217 = relay.floor_divide(call_4203.astype('float64'), relay.reshape(var_4216.astype('float64'), relay.shape_of(call_4203))) # shape=(2, 6, 12)
bop_4220 = relay.floor_divide(call_4205.astype('float64'), relay.reshape(var_4216.astype('float64'), relay.shape_of(call_4205))) # shape=(2, 6, 12)
uop_4223 = relay.log10(uop_4209.astype('float64')) # shape=(144, 1)
output = relay.Tuple([call_4193,bop_4217,uop_4223,])
output2 = relay.Tuple([call_4194,bop_4220,uop_4223,])
func_4226 = relay.Function([var_4204,var_4216,], output)
mod['func_4226'] = func_4226
mod = relay.transform.InferType()(mod)
mutated_mod['func_4226'] = func_4226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4226_call = mutated_mod.get_global_var('func_4226')
var_4228 = relay.var("var_4228", dtype = "float32", shape = (144, 1))#candidate|4228|(144, 1)|var|float32
var_4229 = relay.var("var_4229", dtype = "float32", shape = (2, 6, 12))#candidate|4229|(2, 6, 12)|var|float32
call_4227 = func_4226_call(var_4228,var_4229,)
output = call_4227
func_4230 = relay.Function([var_4228,var_4229,], output)
mutated_mod['func_4230'] = func_4230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_4235 = relay.TupleGetItem(func_3892_call(), 2)
call_4236 = relay.TupleGetItem(func_3894_call(), 2)
output = call_4235
output2 = call_4236
func_4249 = relay.Function([], output)
mod['func_4249'] = func_4249
mod = relay.transform.InferType()(mod)
mutated_mod['func_4249'] = func_4249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4249_call = mutated_mod.get_global_var('func_4249')
call_4250 = func_4249_call()
output = call_4250
func_4251 = relay.Function([], output)
mutated_mod['func_4251'] = func_4251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4021_call = mod.get_global_var('func_4021')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_4278 = relay.TupleGetItem(func_4021_call(), 0)
call_4279 = relay.TupleGetItem(func_4023_call(), 0)
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_4288 = relay.TupleGetItem(func_3390_call(), 3)
call_4289 = relay.TupleGetItem(func_3392_call(), 3)
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_4290 = relay.TupleGetItem(func_2512_call(), 1)
call_4291 = relay.TupleGetItem(func_2513_call(), 1)
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_4295 = relay.TupleGetItem(func_3390_call(), 2)
call_4296 = relay.TupleGetItem(func_3392_call(), 2)
var_4300 = relay.var("var_4300", dtype = "float64", shape = (2, 10, 5))#candidate|4300|(2, 10, 5)|var|float64
bop_4301 = relay.minimum(call_4295.astype('float32'), relay.reshape(var_4300.astype('float32'), relay.shape_of(call_4295))) # shape=(2, 10, 5)
bop_4304 = relay.minimum(call_4296.astype('float32'), relay.reshape(var_4300.astype('float32'), relay.shape_of(call_4296))) # shape=(2, 10, 5)
func_2565_call = mod.get_global_var('func_2565')
func_2569_call = mutated_mod.get_global_var('func_2569')
const_4315 = relay.const([-1,3,8,8,2,-10,-9,2,-3,8,9,4,-8,-2,-5,5,-8,4,8,3,-1,-10,1,8,6,5,-6,9,-8,-6,1,-9,-10,6,-6,-9,-3,9,2,-2,-3,-6,-8,3,-7,10,-10,1,-3,-9,8,-6,-8,-7,-2,1,-7,-4,-3,2,-6,1,1,-6,-1,-3,-1,-9,4,9,6,1,8,-8,-2,4,5,4,9,2,2,-8,6,6,-5,6,-7,-5,-4,-8,5,6,7,-8,1,4,-5,10,10,-1,-1,6,-8,10,6,-10,-10,-3,-8,3,10,3,-2,7,9,8,-7,-5,-5,-6,-5,-4,-5,-1,-9,-2,-2,6,-10,-5,-1,6,-7,-4,7,5,-8,-4,7,6,10,7,-7,-5,4,-7,-10,6,5,10,-9,4,6,-10,7,-1,8,-8,-8,5,10,-10,6,-8,5,-6,4,4,10,-3,4,4,9,-8,-3,-1,-4,5,-9,4,2,-10,8,4,-10,6,10,-5,-2,-8,-5,-7,-1,10,5,4,3,-4,10,10,-7,-5,6,6,4,-2,4,-1,-2,-3,-6,-6,2,10,8,-1,8,-3,-7,-4,-4,1,6,3,4,6,-4,7,-2,6,-6,-6,5,9,-10,-3,9,-2,-8,4,-10,10,-3,-8,3,-7,-4,-3,4,-1,7,7,-1,-3,-4,1,-9,6,9,9,1,-2,10,-4,-9,9,2,-6,-6,2,-7,-4,5,10,-5,5,-6,-10,2,1,10,1,-5,-7,-5,-1,-3,9,-6,-3,10,8,4,-4,-4,10,-4,-8,-8,-2,-5,5,9,-9,5,-5,-9,-10,-10,9,-9,8,2,4,2,-10,2,-6,-9,7,6,-8,-6,-5,-3,10,7,-7,7,-8,-1,7,-6,-6,7,-1,-7,7,-7,10,1,6,-10,-7,-6,6,-5,-3,-6,-8,-4,8,-7,-3,-9,8,2,8,-5,-9,-1,-10,-5,-9,-4,6,7,-7,8,1,-4,-7,-1,10,-7,-10,-3,-5,3,-9,-3,5,8,-6,-6,4,-6,-8,-4,-6,7,-9,4,9,10,-6,-3,-4,-5,-7,-7,-10,-2,1,-9,6,3,-6,-3,-6,-3,7,5,6,2,-10,-4,4,-1,1,4,-5,7,3,6,-3,6,-6,-1,-1,-6,4,1,8,-2,1,-10,-2,10,5,7,-7,-9,-3,5,-5,-5,3,-6,-10,-3,4,-9,-8,-2,-5,2,1,4,4,-8,-10,-8,10,5,-10,-5,10,1,-5,3,-1,1,-8,5,-4,-9,-5,7,-10,-9,1,-7,8,-10,-2,-2,-10,6,-7,10,-6,-6,-7,-8,5,7,9,-8,-3,-9,-5,-9,-3,-5,-6,2,3,2,-10,6,10,-3,7,-8,-2,-5,-8,-4,-9,-1,-3,6,-2,-5,-1,-8,-4,9,-2,2,-4,3,-1,-2,7,7,8,-5,4,-3,-2,-7,1,6,5,-9,6,2,10,-10,-9,4,-10,8,-10,-10,-1,7,-5,7,-2,10,8,-5,-7,-5,2,6,10,-6,6,-3,5,10,4,1,-4,5,-4,-2,7,-9,-9,-1,-8,1,2,-2,-5,-8,-10,6,1,-5,6,-8,-5,2,-2,2,7,-4,7,-8,8,1,7,3,-1,-5,-6,-9,-1,-4,1,3,-1,-9,-4,-1,2,-2,1,9,4,8,8,-10,6,4,-3,-5,7,-3,10,-3,5,-3,1,-10,-5,-4,6,6,1,1,-8,-6,-2,-5,-4,5,6,-8,10,-1,-6,10,10,-6,-5,-2,-3,7,9,8,-2,3,-10,2,-8,-7,-7,-6,4,-5,7,5,8,-7,-5,10,-7,3,3,1,10,6,6,6,2,-2,-1,-10,8,5,2,1,8,9,1,3,-8,1,-10,8,8,-2,-5,-9,-2,8,-2,3,3,3,2,7,8,-5,-5,-10,-3,6,-5,-2,-1,-2,9,5,9,-8,-8,2,3,2,-2,-4,5,2,-5,8,7,9,7,-10,5,-9,2,-9,-1,-6,-5,10,10,-3,-8,-3,1,3,-7,4,10,3,7,9,-4,2,5,9,-6,2,-3,1,6,-4,8,3,3,1,9,-7,5,2,3,-7,6,-3,4,-5,-9,-1,10,4,-3,3,-5,7,-4,-9,-2,6,-6,7,2,-8,2,7,-7,-5,-7,6,-1,-1,-4,1,-9,-4,-5,-4,-4,9,6,-9,-8,5,5,7,-4,10,-3,4,8,-6,10,10,-6,1,7,-7,6,-2,5,6,10,-7,-7,-4,10,9,-1,5,10,-1,8,1,2,-5,-3,-6,7,5,-6,-10,-10,-8,10,10,9,-4,-1,-3,8,-10,8,-3,1,10,8,6,1,-9,-5,-8,2,3,8,-6,3,5,-4,-6,-8,-4,8,-4,-2,-9,-4,3,-2,-9,4,5,5,-1,-10,-6,5,3,-10,4,10,10,4,-1,-2,7,8,-3,1,4,3,10,-9,-3,1,-2,-3,-6,6,3,8,3,-1,-10,2,-6,1,-3,8,-1,3,2,6,3,3,-7,4,-8,-8,-9,-10,5,8,6,-4,-7,-10,1,4,5,9,-10,-4,10,-7,-2,2,10,5,-6,-3,-4,-1,-9,10,-6,-8,2,5,5,8,8,-5,10,2,-7,-10,-8,-9,-7,10,7,-10,-1,-2,-6,6,-10,10,-10,-9,-1,-9,1,-5,6,2,5,-4,-8,5,-7,-7,9,-9,4,-6,-7,2,-5,-8,4,4,-3,-6,-5,4,9,8,-9,-8,7,5,-1,3,6,6,-1,-9,-1,5,5,7,-1,3,4,-4,-5,6,-8,1,2,5,-10,-8,-9,-6,-4,-8,9,-6,3,5,-9,-6,-4,2,-4,9,-1,-2,2,5,-2,1,-6,-4,7,9,-2,2,9,10,-10,7,8,2,-9,5,1,3,-5,8,-6,-9,-1,-6,6,6,-7,-9,-6,2,-9,-9,5,10,8,-3,7,7,-4,10,9,7,-3,-8,7,-4,-10,-9,-6,-6,-6,-1,2,1,-10,-7,-9,2,3,10,-3,8,-9,8,-5,10,-5,6,-10,5,-10,-9,-9,2,5,1,8,1,6,3,-6,-3,-7,-10,8,6,-2,-6,10,-2,-9,2,4,-5,3,-2,-2,-1,5,-5,-9,-8,10,1,-3,-2,7,2,-7,10,6,10,8,-8,-3,6,5,-10,-10,-2,5,7,-10,-1,-7,-7,-4,4,6,-7,-4,10,6,4,-2,-9,2,7,7,7,1,-9,-10,-9,5,-7,6,6,-7,8,-7,-6,-4,-1,3,7,5,-10,-10,-3,-6,2,8,-4,10,-6,-10,10,-5,5,10,-3,9,-1,-2,-4,7,-10,7,1,7,-6,10,-3,6,3,9,4,9,6,2,-2,7,-5,8,-2,5,-6,-4,10,-6,-10,10,2,9,-3,-10,-9,8,1,-10,-5,-1,-10,7,-6,6,7,-10,-7,8,10,-6,-9,3,-10,-3,9,-3,10,2,2,-2,4,-9,2,3,-7,1,1,6,-6,-8,2,6,3,7,-6,6,4,-10,-5,8,-2,-10,10,6,-4,3,-8,-7,4,10,-5,-9,2,-5,4,10,10,-9,-3,-8,-1,-4,-9,2,7,3,-8,2,4,8,-9,-4,-6,3,9,-8,-2,1,-3,7,5,-3,4,7,-1,8,3,2,6,-3,-7,-5,-3,-10,-9,6,7,-9,3,1,-10,7,-2,7,2,-4,10,8,8,-10,7,3,5,6,-9,-5,9,-6,-1,-10,-10,-4,6,4,1,10,-9,-3,8,-6,10,10,3,2,-9,-9,-7,-9,-4,-6,6,5,3,-2,9,10,1,-1,-5,10,-5,3,1,-6,7,-10,-10,-10,2,3,-4,-1,4,1,4,5,10,3,2,-6,1,-3,10,-5,-9,-2,-3,8,-4,9,10,-7,-4,4,10,-6,-6,4,-6,8,7,-8,2,10,-5,-6,-4,9,-5,-3,-5,-4,10,8,-6,1,4,-4,5,6,6,7,7,6,-9,7,-8,6,8,3,-8,-7,-2,-3,-8,7,3,2,9,3,8,3,-10,5,-1,-4,-3,-3,4,1,7,6,3,-1,7,-2,4,3,4,-2,4,-6,-8,1,-5,6,4,1,9,2,5,-2,-1,1,-1,-2,10,4,-7,10,9,5,7,1,-7,3,-8,1,10,-5,-6,7,-3,5,-6,-3,2,-8,-3,6,-1,3,6,9,5,-6,-8,-8,2,2,-10,-2,-2,-1,7,-6,6,10,-3,-7,-10,1,6,1,-5,-5,-10,5,-5,-7,-4,3,-4,4,-1,-6,-4,8,-8,-7,4,8,-10,3,1,-10,-7,-9,-7,6,3,-6,1,-8,-5,-4,8,-2,-6,4,7,6,-8,-4,-5,-2,4,-7,5,4,10,-8,1,-5,-7,6,-4,9,-5,-8,3,1,1,10,1,6,3,10,-6,-1,-5,-8,-9,-4,7,-5,3,6,3,-9,-2,-6,3,-1,2,-3,-8,7,-5,10,-4,-2,2,-2,-6,1,-8,-6,-4,1,6,-2,-4,-2,9,-10,-8,1,-2,6,4,7,6,-6,-8,-6,-10,1,-7,-2,4,1,-6,-5,-5,-6,10,-2,7,-7,-4,1,1,-9,-2,9,3,-9,4,7,7,-8,-7,5,10,-8,7,10,9,8,-10,-9,-9,-4,-6,-2,-6,-2,-5,-6,-9,1,4,-3,3,-8,10,-8,8,4,4,-7,-10,-3,5,2,-8,9,-6,-8,-6,4,4,7,-3,-7,8,-7,-2,3,-4,3,-10,5,-7,-7,-7,-10,-2,-2,9,1,-3,6,-3,-5,6,10,-10,-1,7,-9,8,5,6,4,9,3,-6,-9,9,-7,-4,10,1,3,7,2,1,5,7,5,7,-7,-10,-3,4,4,10,-4,-3,-8,-10,10,-10,-1,6,-2,-7,-7,7,5,-1,-1,-3,1,3,10,4,5,5,-10,3,4,-10,6,-1,1,10,-3,7,10,-7,-3,10,-4,5,6,3,9,-8,-1,6,1,3,10,1,-2,-2,-9,5,7,-5,-8,-2,-2,-10,9,6,-3,-5,-3,-4,-7,1,9,1,-6,1,-7,-8,3,-5,-5,4,1,2,-8,-10,3,2,7,-9,2,-6,-3,7,4,10,-2,-9,6,9,-8,-10,2,4,-7,-4,-3,5,3,-3,3,-8,10,2,-9,-9,-1,9,-4,5,-5,8,7,7,-7,-9,-6,9,-4,-1,1,-1,2,8,-4,5,9,-9,-1,8,-9,-10,6,10,-2,7,4,6,10,9,-6,-3,-2,-3,1,10,-10,4,2,10,-6,7,-4,3,8,8,-8,9,5,2,-3,3,-5,-1,-2,10,7,5,4,-5,-2,6,-2,-10,5,3,4,-3,-5,-5,7,-3,7,-4,-10,3,2,1,-2,-10,-5,-7,1,10,-6,2,-2,-6,5,-10,-10,6,-2,-5,2,-3,10,-7,-4,6,-2,3,-5,5,-10,-4,9,2,9,-8,-5,-9,3,-6,3,-6,2,2,-10,-7,3,-3,-3,4,4,-4,-2,-6,9,3,7,8,9,-5,7,1,3,-2,1,-10,-7,6,7,4,5,7,-9,1,7,8,8,-3,3,1,1,-7,-8,-8,6,-1,1,4,5,7,1,-5,5,4,-5,-10,-6,5,-1,-9,4,1,-9,5,-10,5,8,-4,8,-8,3,-9,6,-5,6,-5,5,8,-1,-8,-5,-6,-3,-5,10,-3,-1,4,-8,-6,4,-7,-5,4,9,-9,-5,7,-5,10,-8,-10,7,8,-4,2,-4,-8,-7,9,6,-10,2,10,2,5,-5,10,-9,-9,-3,-3,-3,9,5,6,3,4,-7,-5,6], dtype = "int32")#candidate|4315|(2197,)|const|int32
call_4314 = relay.TupleGetItem(func_2565_call(relay.reshape(const_4315.astype('int32'), [13, 13, 13]), relay.reshape(const_4315.astype('int32'), [13, 13, 13]), relay.reshape(call_4290.astype('float32'), [28,]), ), 2)
call_4316 = relay.TupleGetItem(func_2569_call(relay.reshape(const_4315.astype('int32'), [13, 13, 13]), relay.reshape(const_4315.astype('int32'), [13, 13, 13]), relay.reshape(call_4290.astype('float32'), [28,]), ), 2)
bop_4323 = relay.bitwise_and(call_4288.astype('int32'), relay.reshape(var_4300.astype('int32'), relay.shape_of(call_4288))) # shape=(1, 100)
bop_4326 = relay.bitwise_and(call_4289.astype('int32'), relay.reshape(var_4300.astype('int32'), relay.shape_of(call_4289))) # shape=(1, 100)
output = relay.Tuple([call_4278,call_4290,bop_4301,call_4314,const_4315,bop_4323,])
output2 = relay.Tuple([call_4279,call_4291,bop_4304,call_4316,const_4315,bop_4326,])
func_4333 = relay.Function([var_4300,], output)
mod['func_4333'] = func_4333
mod = relay.transform.InferType()(mod)
mutated_mod['func_4333'] = func_4333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4334 = relay.var("var_4334", dtype = "float64", shape = (2, 10, 5))#candidate|4334|(2, 10, 5)|var|float64
func_4333_call = mutated_mod.get_global_var('func_4333')
call_4335 = func_4333_call(var_4334)
output = call_4335
func_4336 = relay.Function([var_4334], output)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_4343 = relay.TupleGetItem(func_2526_call(), 0)
call_4344 = relay.TupleGetItem(func_2528_call(), 0)
output = call_4343
output2 = call_4344
func_4349 = relay.Function([], output)
mod['func_4349'] = func_4349
mod = relay.transform.InferType()(mod)
output = func_4349()
func_4350 = relay.Function([], output)
mutated_mod['func_4350'] = func_4350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3639_call = mod.get_global_var('func_3639')
func_3641_call = mutated_mod.get_global_var('func_3641')
call_4357 = relay.TupleGetItem(func_3639_call(), 0)
call_4358 = relay.TupleGetItem(func_3641_call(), 0)
func_2702_call = mod.get_global_var('func_2702')
func_2704_call = mutated_mod.get_global_var('func_2704')
const_4365 = relay.const([-1.928095,0.179038,-7.886456,3.008487,-2.416429,5.846269,7.618973,0.364141,-9.202069,-8.829026,5.587201,-2.440521,6.078525,-9.910187,-4.148320,5.035559,-8.368321,8.230199,-6.041033,-8.029739,7.132546,2.311520,-0.332785,-8.558436,-6.009096,9.268009,-1.519483,4.383460,1.459015,-4.628610,-7.620928,-7.125531,-5.093962,-5.208382,-6.937257,0.530322,-6.382762,-8.577433,9.281203,-7.135467,-4.798168,-5.377436,7.173543,-9.305354,1.942931,-7.407083,-0.531789,-3.063575,2.075604,-0.638796,1.164471,5.949366,-0.812754,-9.386111,-5.238812,7.581390,1.889453,7.303183,-2.663831,5.233847,-3.101462,5.020482,-7.225691,9.379214,-2.094335,0.623562,-3.442183,-9.412541,-9.042299,-3.968149,6.994143,6.270435,9.345977,4.973060,5.747982,2.001829,-6.365994,-5.608344,-9.892638,-5.397711,2.666495,-3.713949,8.095113,-0.077540,-8.181727,-5.436624,1.805159,-2.040607,1.099999,-3.044382,-0.594417,-3.051873,-3.832048,5.440421,3.620048,-6.737151,1.566341,-7.154528,6.921627,-5.442770,1.521408,5.286257,3.968532,-7.247987,9.684359,1.455942,-2.437154,-0.545192,-8.236825,-0.472614,-1.640543,4.103864,1.831701,-7.195872,-8.325232,-4.512455,4.535011,-7.169123,5.739850,3.874503,3.987427,-7.368775,6.618106,8.313817,-8.496936,7.688948,-4.623319,-1.281258,-5.939869,-1.434869,-7.465117,-5.800949,-5.904397,-9.923301,1.495945,-1.599664,-2.761212,3.290828,9.480170,2.534651,-0.671961,-8.973841,4.405929,-4.356995,4.294821,9.393165,-0.466086,-0.728193,-6.534822,-6.200383,-2.527997,8.362537,-6.546652,-9.143848,5.311759,6.760337,-6.083490,-2.361090,2.848793,4.118851,7.603556,-6.274002,0.743626,-9.269710,0.453235,6.862001,7.552479,-8.456825,5.126701,3.801009,-8.584941,-1.633949,7.748894,6.734637,-8.244350,0.644942,7.963176,4.135404,-1.837568,-7.007192,-8.404562,-3.957879,-3.821120,7.240155,8.586953,-1.708513,-5.913647,8.850416,7.475693,-0.615350,1.072045,2.792746,2.690421,4.095130,-6.700313,7.093804,-6.820740,-7.994757,-8.529885,-7.620354,5.428231,5.054020,-3.507253,4.113949,6.924738,7.838121,9.147893,9.725897,5.825049,4.654125,7.317125,-8.121811,-1.391720,-3.159392,3.496835,-5.220081,-0.516472,-6.950313,-3.668238,-2.169220,7.293292,2.317985,0.485966,9.181455,5.071861,-1.201013,2.142677,-3.675180,-3.455432,-2.077286,-6.316976,-6.550089,-9.471145,7.038411,-4.173024,6.941521,1.736633,-7.850603,2.615785,5.821177,-3.554446,5.034342,-3.652434,7.227642,1.821062,-7.859946,9.136220,-5.085059,4.323254,-9.540528,6.227494,9.817444,-5.363246,5.471622,8.068517,8.022462,2.242535,5.618762,-8.611328,-4.055391,-8.543706,0.523125,4.266089,-3.038298,4.696210,-5.047425,-1.417404,5.066255,3.140167,-2.606035,4.256901,5.308129,8.603940,7.447598,5.378344,6.102712,-0.238733,6.960556,-3.685435,8.128442,5.648932,-1.871604,5.513877,-4.633110,6.400046,-8.636022,-7.895921,4.564719,-1.712937,-9.014421,-3.439739,-4.079583,-7.779391,-8.768940,8.209751,3.306706,0.698201,-8.739171,5.490767,3.123662,3.922486,-1.539897,3.256025,6.435034,-4.341145,-5.072080,4.509688,0.729713,-7.801158,-1.034445,2.122836,-7.827505,-1.466985,-0.234763,-9.638348,-2.432520,4.998957,1.357684,-2.057078,-4.274494,-7.941244,1.478083,3.977190,-7.765944,-5.024628,5.848626,-9.663202,-6.541307,-2.033224,-3.731445,-4.989611,4.861739,3.695266,9.273435,7.871403,-0.621335,-5.950044,-7.638186,7.371214,2.232615,0.090339,3.449624,7.264490,-0.256333,-3.468345,-4.303282,2.462371,-0.197503,-8.174807,-7.112526,-3.981519,-0.657303,-5.334583,-9.409825,5.115897,9.010918,1.626374,-3.060755,-5.244033,-0.052755,8.834124,-0.723471,-3.279083,-2.055486,-2.881649,4.444824,7.702007,8.708526,-5.473122,2.654359,8.874204,-2.253619,-2.895148,8.161650,-9.608878,6.100689,-0.966701,-2.861312,7.580738,-5.294234,-0.225637,-3.810043,1.825625,3.582018,2.877172,8.856205,-3.922693,1.811326,-2.708438,9.573444,3.448838,-0.809219,-1.816096,-6.738245,9.994588,9.427966,-7.810380,-0.655875,2.984880,2.976229,-2.375963,-3.082788,0.430470,0.108384,-6.402084,-2.483546,-9.160296,-5.073132,0.646929,-1.639568,7.729771,-3.279826,7.883175,8.234443,2.729774,2.805595,0.439174,-7.103130,-9.062220,-9.016603,-0.813802,-5.425946,3.118173,-8.513255,0.546140,-1.792735,-0.542371,2.803219,6.577943,5.127729,8.502978,-1.453473,-2.693492,4.176356,0.969342,8.943174,-8.701423,-9.783643,-1.919159,1.902674,1.283334,-7.183581,-6.887098,4.138109,-5.115334,-8.820132,9.267545,-8.722717,1.735914,-6.530700,7.862427,0.159801,3.871274,-4.815108,-6.464047,-3.101276,0.396519,4.931274,-9.901553,2.841111,0.788823,-4.554253,-7.453034,-9.517855,5.605213,-4.164555,5.965550,-1.453824,3.380029,-4.993076,-6.312903,1.117889,-4.246367,-7.947162,2.633617,7.244358,7.560985,-7.899474,2.565967,-5.656470,3.006565,2.403456,-8.309362,-7.963729,-3.745418,4.059022,6.636518,-0.622028,7.289890,-1.970914,-0.647491,-8.400610,6.892062,-7.942449,2.952215,0.133555,3.063460,2.150003,2.398324,-6.110137,9.857196,-3.388945,-0.478765,-2.780863,9.332143,1.998584,-1.985142,-0.712413,-7.983268,-1.146541,3.586564,-7.303792,6.360201,-9.448391,4.650336,-3.361636,-5.513862,7.986715,-8.961152,-9.252204,-0.466062,4.720590,2.381066,1.816687,-2.290593,-2.092410,8.922619,4.289631,-2.548002,5.250506,-7.376852,-7.678855,0.673057,9.806154,5.563651,1.810148,4.976341,5.250234,-0.647796,-8.636804,-9.193487,-4.875250,-7.524125,-9.351754,9.405128,-1.351327,-2.878834,-5.747768,1.314641,7.044425,-3.728141,-5.017397,5.635162,-3.964448,-3.364947,0.411279,9.080589,1.399816,8.838645,9.884612,5.008684,-4.829727,-8.242019,9.212469,-2.898524,1.705259,-2.099829,5.187635,3.385412,2.416681,-5.839185,-6.126476,8.939362,1.664573,-1.771985,1.888728,7.450173,7.756579,5.318816,6.359441,5.220609,-4.851753,-9.986025,1.856375,2.866444,-0.168502,1.706497,-2.373613,-4.542057,2.398146,-7.136386,-7.014134,-4.928606,2.791757,1.832053,-9.733948,0.949347,-0.704195,-1.693248,1.874259,-9.670854,2.041926,3.511915,-7.147794,-2.471026,-0.672746,6.753082,-6.450209,-6.285585,7.620160,-0.698929,-6.005579,-5.911838,7.266592,-7.195601,-5.706160,-6.660947,6.043647,7.812595,6.374505,4.710593,-1.744572,6.307562,0.857752], dtype = "float32")#candidate|4365|(624,)|const|float32
call_4364 = relay.TupleGetItem(func_2702_call(relay.reshape(const_4365.astype('float32'), [13, 12, 4])), 0)
call_4366 = relay.TupleGetItem(func_2704_call(relay.reshape(const_4365.astype('float32'), [13, 12, 4])), 0)
output = relay.Tuple([call_4357,call_4364,const_4365,])
output2 = relay.Tuple([call_4358,call_4366,const_4365,])
func_4372 = relay.Function([], output)
mod['func_4372'] = func_4372
mod = relay.transform.InferType()(mod)
output = func_4372()
func_4373 = relay.Function([], output)
mutated_mod['func_4373'] = func_4373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_4423 = func_3544_call()
call_4424 = func_3544_call()
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
var_4444 = relay.var("var_4444", dtype = "float64", shape = ())#candidate|4444|()|var|float64
const_4445 = relay.const([3.033786,-3.863496,2.936319,-5.689005,-9.638512,7.421202,9.275548,-1.010084,1.790008,5.188364,5.405385,-8.842816,-4.062082,-3.999318,2.658417,-9.494600,1.748392,3.736503,1.298892,-8.152835,-0.215427,4.564608,2.018763,-1.005769,5.188658,4.233208,5.579108,0.372727,-1.805238,-9.979193,2.111375,-5.406175,9.195097,1.595384,3.979977,5.391165,7.366398,5.307365,-1.575622,6.920749,7.018802,-9.331196,3.138143,8.522457,9.936680,7.423692,-5.546464,-5.748867,8.086279,-9.242253,1.525090,7.488301,-2.764152,1.285715,-5.221776,-5.136945,1.703122,3.805426,-3.777471,-5.344438,-9.707335,5.168779,-5.471486,-6.451651,5.356504,-9.259664,-0.108139,-1.405475,0.920462,0.548388,-3.505130,0.438940,-5.250034,-2.221492,8.264875,8.339950,-4.703008,6.712932,-3.708289,6.916397,-9.903439,-2.025479,7.102452,-8.112751,2.177731,-8.697999,8.128660,3.033034,-2.224730,0.217088,2.916577,2.028616,9.494071,-8.325694,5.578051,5.339571,1.542197,-5.204569,-7.684168,4.516406,8.314584,-4.829703,-8.128242,-3.669561,7.910678,-2.161497,-8.358201,9.408241,-8.839016,1.495979], dtype = "float64")#candidate|4445|(110,)|const|float64
call_4443 = relay.TupleGetItem(func_2062_call(relay.reshape(var_4444.astype('float64'), []), relay.reshape(const_4445.astype('float64'), [10, 1, 11]), ), 2)
call_4446 = relay.TupleGetItem(func_2065_call(relay.reshape(var_4444.astype('float64'), []), relay.reshape(const_4445.astype('float64'), [10, 1, 11]), ), 2)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_4468 = relay.TupleGetItem(func_2526_call(), 0)
call_4469 = relay.TupleGetItem(func_2528_call(), 0)
output = relay.Tuple([call_4423,call_4443,var_4444,const_4445,call_4468,])
output2 = relay.Tuple([call_4424,call_4446,var_4444,const_4445,call_4469,])
func_4473 = relay.Function([var_4444,], output)
mod['func_4473'] = func_4473
mod = relay.transform.InferType()(mod)
var_4474 = relay.var("var_4474", dtype = "float64", shape = ())#candidate|4474|()|var|float64
output = func_4473(var_4474)
func_4475 = relay.Function([var_4474], output)
mutated_mod['func_4475'] = func_4475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_4480 = relay.TupleGetItem(func_3892_call(), 1)
call_4481 = relay.TupleGetItem(func_3894_call(), 1)
output = relay.Tuple([call_4480,])
output2 = relay.Tuple([call_4481,])
func_4489 = relay.Function([], output)
mod['func_4489'] = func_4489
mod = relay.transform.InferType()(mod)
output = func_4489()
func_4490 = relay.Function([], output)
mutated_mod['func_4490'] = func_4490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4373_call = mutated_mod.get_global_var('func_4373')
call_4743 = relay.TupleGetItem(func_4372_call(), 0)
call_4744 = relay.TupleGetItem(func_4373_call(), 0)
func_3023_call = mod.get_global_var('func_3023')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_4748 = relay.TupleGetItem(func_3023_call(relay.reshape(call_4743.astype('float64'), [110,])), 0)
call_4749 = relay.TupleGetItem(func_3025_call(relay.reshape(call_4743.astype('float64'), [110,])), 0)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
var_4775 = relay.var("var_4775", dtype = "float64", shape = ())#candidate|4775|()|var|float64
call_4774 = relay.TupleGetItem(func_2062_call(relay.reshape(var_4775.astype('float64'), []), relay.reshape(call_4743.astype('float64'), [10, 1, 11]), ), 1)
call_4776 = relay.TupleGetItem(func_2065_call(relay.reshape(var_4775.astype('float64'), []), relay.reshape(call_4743.astype('float64'), [10, 1, 11]), ), 1)
output = relay.Tuple([call_4743,call_4748,call_4774,var_4775,])
output2 = relay.Tuple([call_4744,call_4749,call_4776,var_4775,])
func_4781 = relay.Function([var_4775,], output)
mod['func_4781'] = func_4781
mod = relay.transform.InferType()(mod)
var_4782 = relay.var("var_4782", dtype = "float64", shape = ())#candidate|4782|()|var|float64
output = func_4781(var_4782)
func_4783 = relay.Function([var_4782], output)
mutated_mod['func_4783'] = func_4783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4373_call = mutated_mod.get_global_var('func_4373')
call_4789 = relay.TupleGetItem(func_4372_call(), 0)
call_4790 = relay.TupleGetItem(func_4373_call(), 0)
output = relay.Tuple([call_4789,])
output2 = relay.Tuple([call_4790,])
func_4792 = relay.Function([], output)
mod['func_4792'] = func_4792
mod = relay.transform.InferType()(mod)
output = func_4792()
func_4793 = relay.Function([], output)
mutated_mod['func_4793'] = func_4793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_4806 = relay.TupleGetItem(func_2512_call(), 1)
call_4807 = relay.TupleGetItem(func_2513_call(), 1)
func_2845_call = mod.get_global_var('func_2845')
func_2846_call = mutated_mod.get_global_var('func_2846')
call_4817 = func_2845_call()
call_4818 = func_2845_call()
output = relay.Tuple([call_4806,call_4817,])
output2 = relay.Tuple([call_4807,call_4818,])
func_4819 = relay.Function([], output)
mod['func_4819'] = func_4819
mod = relay.transform.InferType()(mod)
mutated_mod['func_4819'] = func_4819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4819_call = mutated_mod.get_global_var('func_4819')
call_4820 = func_4819_call()
output = call_4820
func_4821 = relay.Function([], output)
mutated_mod['func_4821'] = func_4821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_4839 = relay.TupleGetItem(func_2526_call(), 0)
call_4840 = relay.TupleGetItem(func_2528_call(), 0)
func_2587_call = mod.get_global_var('func_2587')
func_2589_call = mutated_mod.get_global_var('func_2589')
const_4846 = relay.const([[-1.326465],[-4.276734],[-2.081758],[0.835464],[-7.212482],[-2.135863],[3.600708],[-7.245622],[-8.649610],[4.413732],[3.927214],[8.464302],[-1.477971],[-0.140727],[-0.199388],[-3.523474],[-6.226313],[-9.824573],[-6.780939],[-6.123894],[-0.691108],[6.773112],[7.992847],[-8.388076],[-3.466492],[-8.494641],[-1.419321],[-1.421510],[2.055166],[-2.531979],[4.672387],[-0.482932],[5.312677],[-7.368180],[-7.177733],[-0.772943],[5.860420],[-5.535131],[-6.672615],[-4.954998],[-5.432524],[-6.336670],[-6.705683],[-1.444273],[5.583139],[-8.800770],[1.084325],[1.144246],[8.359222],[9.311666],[-9.714327],[-2.777958],[3.737595],[-6.306266],[5.204304],[-9.512072],[-5.129852],[9.827861],[8.831852],[-2.523742],[-5.166340],[1.671188],[0.848494],[-4.170223],[-6.238489],[8.565034],[0.074182],[-3.275452],[-4.547956],[-6.676111],[2.857962],[-4.331356],[-3.129334],[9.763910],[9.871716],[-5.208675],[-0.984145],[4.616893],[-3.151958],[-2.087275],[0.077797],[3.522640],[-0.132340],[3.136882],[7.998142],[-1.473895],[0.231289],[-1.859290],[-3.269768],[2.485822],[4.885432],[9.397872],[-7.788738],[9.683280],[-3.472669],[7.018898],[8.678945],[3.338183],[7.540145],[6.874539],[-4.157038],[7.900972],[-4.154269],[2.575841],[6.852718],[-1.834894],[0.686411],[-7.975783],[-1.339674],[-2.200307]], dtype = "float64")#candidate|4846|(110, 1)|const|float64
call_4845 = relay.TupleGetItem(func_2587_call(relay.reshape(const_4846.astype('float64'), [22, 5])), 3)
call_4847 = relay.TupleGetItem(func_2589_call(relay.reshape(const_4846.astype('float64'), [22, 5])), 3)
const_4848 = relay.const([[-2.526945,8.511676,-0.123015,-1.840778,-2.786374],[-4.191990,-1.507621,1.654062,-6.379728,-2.272880],[7.625194,6.548551,-6.123916,4.638639,9.568664],[7.857988,-9.566954,-3.067093,-8.490453,-2.976080],[5.396068,-3.223927,-0.051359,-5.891797,2.367579],[2.841895,-0.026098,6.753945,3.917226,2.511133],[2.272667,-4.969822,8.199701,-7.576897,8.036270],[-6.357891,4.838372,9.236965,-5.686735,8.551732],[-0.591733,5.708246,9.239162,6.997987,1.132860],[0.044278,3.274052,-4.702479,-1.096390,-6.899556],[-8.924720,-5.644602,6.078800,6.780866,6.050585],[-9.933663,2.523616,2.843767,-8.876433,0.068476],[9.201060,3.132587,-9.985574,8.449123,-2.499951],[7.354449,3.239515,8.964029,2.569671,-6.147624],[0.698552,-5.145137,-3.104791,4.004104,-9.004223],[2.351620,3.320802,-7.878820,-2.715741,-2.839017],[-4.608811,5.509228,9.477992,-4.659538,9.591080],[2.798152,7.124279,1.479687,2.550214,5.210183],[0.556788,0.776582,1.719897,2.719254,-3.470814],[-9.301353,5.344261,-1.516829,-0.081392,2.360795],[2.616583,-0.806120,-2.127344,0.255390,-7.679863],[2.280456,5.861249,-1.028372,-5.871776,-2.555550]], dtype = "float64")#candidate|4848|(22, 5)|const|float64
bop_4849 = relay.floor_divide(call_4845.astype('float64'), relay.reshape(const_4848.astype('float64'), relay.shape_of(call_4845))) # shape=(22, 5)
bop_4852 = relay.floor_divide(call_4847.astype('float64'), relay.reshape(const_4848.astype('float64'), relay.shape_of(call_4847))) # shape=(22, 5)
output = relay.Tuple([call_4839,const_4846,bop_4849,])
output2 = relay.Tuple([call_4840,const_4846,bop_4852,])
func_4872 = relay.Function([], output)
mod['func_4872'] = func_4872
mod = relay.transform.InferType()(mod)
output = func_4872()
func_4873 = relay.Function([], output)
mutated_mod['func_4873'] = func_4873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_4926 = relay.TupleGetItem(func_2808_call(), 0)
call_4927 = relay.TupleGetItem(func_2810_call(), 0)
func_3639_call = mod.get_global_var('func_3639')
func_3641_call = mutated_mod.get_global_var('func_3641')
call_4942 = relay.TupleGetItem(func_3639_call(), 0)
call_4943 = relay.TupleGetItem(func_3641_call(), 0)
var_4946 = relay.var("var_4946", dtype = "float32", shape = (1, 4, 7))#candidate|4946|(1, 4, 7)|var|float32
bop_4947 = relay.logical_xor(call_4926.astype('uint64'), relay.reshape(var_4946.astype('uint64'), relay.shape_of(call_4926))) # shape=(1, 4, 7)
bop_4950 = relay.logical_xor(call_4927.astype('uint64'), relay.reshape(var_4946.astype('uint64'), relay.shape_of(call_4927))) # shape=(1, 4, 7)
func_3639_call = mod.get_global_var('func_3639')
func_3641_call = mutated_mod.get_global_var('func_3641')
call_4961 = relay.TupleGetItem(func_3639_call(), 0)
call_4962 = relay.TupleGetItem(func_3641_call(), 0)
func_3023_call = mod.get_global_var('func_3023')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_4967 = relay.TupleGetItem(func_3023_call(relay.reshape(call_4942.astype('float64'), [110,])), 2)
call_4968 = relay.TupleGetItem(func_3025_call(relay.reshape(call_4942.astype('float64'), [110,])), 2)
func_3118_call = mod.get_global_var('func_3118')
func_3122_call = mutated_mod.get_global_var('func_3122')
const_5008 = relay.const([-7.539898,2.658050,0.889684,4.992428,0.996251,7.891064,7.548841,-0.187772,0.534829,7.840162,8.010321,-1.586712,-3.905926,3.566754,-5.540945,-0.066502,-9.134474,1.857771,8.686841,-2.714620,9.077655,7.574658,-3.250004,3.570554,8.819437,8.683640,-5.887210,2.505124,-6.169865,-2.458861,9.296301,-5.064573,-0.642707,1.726363,-1.095334,2.105678,-3.759255,-2.738506,-7.187970,-3.952538,3.444677,-9.416731,-2.714933,-0.535730,-3.547904,1.999504,8.230033,-1.982600,7.540452,9.937281,3.069006,3.870296,0.576819,-1.936567,9.351462,-0.314461,-3.157572,-8.727100,-4.905500,-7.772363,-6.692186,5.302290,0.792083,0.734667,3.860265,-2.554930,0.370365,-1.049741,-7.153245,1.116716,-9.869437,-9.876171,-4.091773,8.409653,9.687359,-7.487305,9.261861,-0.948230,9.269783,3.016819,-2.920867,0.514590,1.987244,0.528226,-6.850135,8.518755,-3.497153,4.282806,-9.746313,6.243868,-2.393765,0.376935,4.718214,-0.489995,-6.193411,-8.116859,-4.192589,-7.791167,2.833546,2.258197], dtype = "float64")#candidate|5008|(100,)|const|float64
call_5007 = relay.TupleGetItem(func_3118_call(relay.reshape(call_4961.astype('float64'), [110,]), relay.reshape(const_5008.astype('float64'), [100,]), ), 0)
call_5009 = relay.TupleGetItem(func_3122_call(relay.reshape(call_4961.astype('float64'), [110,]), relay.reshape(const_5008.astype('float64'), [100,]), ), 0)
uop_5010 = relay.log(call_4967.astype('float32')) # shape=(1, 4, 7)
uop_5012 = relay.log(call_4968.astype('float32')) # shape=(1, 4, 7)
func_2845_call = mod.get_global_var('func_2845')
func_2846_call = mutated_mod.get_global_var('func_2846')
call_5022 = func_2845_call()
call_5023 = func_2845_call()
output = relay.Tuple([call_4942,bop_4947,call_4961,call_5007,const_5008,uop_5010,call_5022,])
output2 = relay.Tuple([call_4943,bop_4950,call_4962,call_5009,const_5008,uop_5012,call_5023,])
func_5024 = relay.Function([var_4946,], output)
mod['func_5024'] = func_5024
mod = relay.transform.InferType()(mod)
mutated_mod['func_5024'] = func_5024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5025 = relay.var("var_5025", dtype = "float32", shape = (1, 4, 7))#candidate|5025|(1, 4, 7)|var|float32
func_5024_call = mutated_mod.get_global_var('func_5024')
call_5026 = func_5024_call(var_5025)
output = call_5026
func_5027 = relay.Function([var_5025], output)
mutated_mod['func_5027'] = func_5027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4249_call = mod.get_global_var('func_4249')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_5166 = func_4249_call()
call_5167 = func_4249_call()
output = call_5166
output2 = call_5167
func_5171 = relay.Function([], output)
mod['func_5171'] = func_5171
mod = relay.transform.InferType()(mod)
output = func_5171()
func_5172 = relay.Function([], output)
mutated_mod['func_5172'] = func_5172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_5178 = relay.TupleGetItem(func_2526_call(), 0)
call_5179 = relay.TupleGetItem(func_2528_call(), 0)
output = call_5178
output2 = call_5179
func_5180 = relay.Function([], output)
mod['func_5180'] = func_5180
mod = relay.transform.InferType()(mod)
mutated_mod['func_5180'] = func_5180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mutated_mod.get_global_var('func_5180')
call_5181 = func_5180_call()
output = call_5181
func_5182 = relay.Function([], output)
mutated_mod['func_5182'] = func_5182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mod.get_global_var('func_3287')
func_3289_call = mutated_mod.get_global_var('func_3289')
call_5281 = relay.TupleGetItem(func_3287_call(), 0)
call_5282 = relay.TupleGetItem(func_3289_call(), 0)
func_4349_call = mod.get_global_var('func_4349')
func_4350_call = mutated_mod.get_global_var('func_4350')
call_5294 = func_4349_call()
call_5295 = func_4349_call()
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_5296 = relay.TupleGetItem(func_3892_call(), 4)
call_5297 = relay.TupleGetItem(func_3894_call(), 4)
func_2512_call = mod.get_global_var('func_2512')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_5299 = relay.TupleGetItem(func_2512_call(), 2)
call_5300 = relay.TupleGetItem(func_2513_call(), 2)
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_5306 = relay.TupleGetItem(func_3390_call(), 2)
call_5307 = relay.TupleGetItem(func_3392_call(), 2)
func_3023_call = mod.get_global_var('func_3023')
func_3025_call = mutated_mod.get_global_var('func_3025')
var_5312 = relay.var("var_5312", dtype = "float64", shape = (1, 110))#candidate|5312|(1, 110)|var|float64
call_5311 = relay.TupleGetItem(func_3023_call(relay.reshape(var_5312.astype('float64'), [110,])), 1)
call_5313 = relay.TupleGetItem(func_3025_call(relay.reshape(var_5312.astype('float64'), [110,])), 1)
bop_5314 = relay.logical_and(call_5299.astype('bool'), call_5281.astype('bool')) # shape=(1, 4, 7)
bop_5317 = relay.logical_and(call_5300.astype('bool'), call_5282.astype('bool')) # shape=(1, 4, 7)
func_4168_call = mod.get_global_var('func_4168')
func_4170_call = mutated_mod.get_global_var('func_4170')
call_5325 = relay.TupleGetItem(func_4168_call(relay.reshape(call_5299.astype('float32'), [])), 0)
call_5326 = relay.TupleGetItem(func_4170_call(relay.reshape(call_5299.astype('float32'), [])), 0)
func_3947_call = mod.get_global_var('func_3947')
func_3948_call = mutated_mod.get_global_var('func_3948')
call_5341 = relay.TupleGetItem(func_3947_call(), 3)
call_5342 = relay.TupleGetItem(func_3948_call(), 3)
output = relay.Tuple([call_5294,call_5296,call_5306,call_5311,var_5312,bop_5314,call_5325,call_5341,])
output2 = relay.Tuple([call_5295,call_5297,call_5307,call_5313,var_5312,bop_5317,call_5326,call_5342,])
func_5349 = relay.Function([var_5312,], output)
mod['func_5349'] = func_5349
mod = relay.transform.InferType()(mod)
mutated_mod['func_5349'] = func_5349
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5350 = relay.var("var_5350", dtype = "float64", shape = (1, 110))#candidate|5350|(1, 110)|var|float64
func_5349_call = mutated_mod.get_global_var('func_5349')
call_5351 = func_5349_call(var_5350)
output = call_5351
func_5352 = relay.Function([var_5350], output)
mutated_mod['func_5352'] = func_5352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_5381 = relay.TupleGetItem(func_3655_call(), 0)
call_5382 = relay.TupleGetItem(func_3656_call(), 0)
output = call_5381
output2 = call_5382
func_5406 = relay.Function([], output)
mod['func_5406'] = func_5406
mod = relay.transform.InferType()(mod)
mutated_mod['func_5406'] = func_5406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5406_call = mutated_mod.get_global_var('func_5406')
call_5407 = func_5406_call()
output = call_5407
func_5408 = relay.Function([], output)
mutated_mod['func_5408'] = func_5408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2845_call = mod.get_global_var('func_2845')
func_2846_call = mutated_mod.get_global_var('func_2846')
call_5415 = func_2845_call()
call_5416 = func_2845_call()
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_5419 = relay.TupleGetItem(func_4872_call(), 1)
call_5420 = relay.TupleGetItem(func_4873_call(), 1)
uop_5437 = relay.sigmoid(call_5419.astype('float32')) # shape=(110, 1)
uop_5439 = relay.sigmoid(call_5420.astype('float32')) # shape=(110, 1)
output = relay.Tuple([call_5415,uop_5437,])
output2 = relay.Tuple([call_5416,uop_5439,])
func_5455 = relay.Function([], output)
mod['func_5455'] = func_5455
mod = relay.transform.InferType()(mod)
output = func_5455()
func_5456 = relay.Function([], output)
mutated_mod['func_5456'] = func_5456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5470 = func_5180_call()
call_5471 = func_5180_call()
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_5486 = relay.TupleGetItem(func_3655_call(), 0)
call_5487 = relay.TupleGetItem(func_3656_call(), 0)
func_2587_call = mod.get_global_var('func_2587')
func_2589_call = mutated_mod.get_global_var('func_2589')
const_5501 = relay.const([-6.646182,-7.804344,6.988353,1.619191,-4.808389,1.639014,6.283098,-1.329118,2.468971,-6.619591,2.821695,-8.610947,6.336018,-2.699175,-0.745616,6.909502,2.943947,3.888121,6.808823,2.515759,-9.098045,8.497437,7.887953,-2.198933,6.699477,-5.867266,2.312409,3.194388,0.038317,-9.834799,-1.861970,-3.769901,4.913501,-8.369161,-8.580334,5.743620,-5.728876,-9.399738,-6.010139,-0.984430,2.415514,-4.408756,4.237661,6.307739,8.120411,0.778961,0.554979,-9.249772,1.116161,4.910540,-4.242436,-9.650130,-3.195564,-8.392841,-0.532776,-2.281002,-5.840745,-4.072707,-8.174467,-7.992378,6.521572,7.446199,6.860206,-7.920010,-1.906406,-0.942024,-7.059875,-7.358691,7.893552,1.625079,2.560765,1.176513,2.951369,-8.260464,1.801719,4.302390,-2.276443,9.631935,-0.821363,-9.557704,-7.177160,4.312673,-4.576890,1.236119,5.161213,2.950111,-5.574904,-6.264319,-9.786845,-2.656305,9.054607,7.480472,-3.910932,5.719744,-9.304565,-6.436129,-2.293712,5.561274,6.524369,-1.575493,0.668337,9.035622,-9.569840,2.790029,-3.716786,-2.920270,-2.189446,6.149545,-3.169736,7.526456], dtype = "float64")#candidate|5501|(110,)|const|float64
call_5500 = relay.TupleGetItem(func_2587_call(relay.reshape(const_5501.astype('float64'), [22, 5])), 2)
call_5502 = relay.TupleGetItem(func_2589_call(relay.reshape(const_5501.astype('float64'), [22, 5])), 2)
func_3973_call = mod.get_global_var('func_3973')
func_3976_call = mutated_mod.get_global_var('func_3976')
const_5521 = relay.const([[-0.165603,-0.508084],[-0.585087,-1.064692],[5.414847,1.158347],[-3.320073,6.599384],[7.002101,1.687080],[1.647280,-5.066182],[7.480218,-4.211150],[8.240810,5.198590],[4.064726,9.932024],[9.884346,-9.477304],[1.023468,7.497985],[6.234828,-3.488009],[8.871993,-5.112771],[5.910400,9.763692],[-8.784950,4.070271],[0.598481,5.615311],[-0.973969,7.283252],[-7.769950,-8.311934],[3.437171,8.433185],[-5.617929,3.738086],[7.872666,-7.006347],[-6.147284,1.959733],[5.463718,7.542360],[9.937057,5.565747],[4.324599,-4.261466],[-5.056659,0.994486],[-3.680144,-3.924786],[-7.350222,0.858491],[6.230754,-7.915372],[4.773236,-1.030522],[-1.968493,7.351873],[-4.643597,-6.793858],[0.329663,8.248364],[7.319851,7.465732],[5.510272,1.373770],[-5.476132,-5.282762],[-7.486205,9.677141],[-0.359305,1.678710],[6.494766,0.325847],[3.301570,6.852605],[-8.862392,5.160992],[7.536377,8.324822],[-0.459138,-5.183352],[3.269498,3.887858],[-7.047550,9.998740],[-2.245953,0.098537],[-4.539946,-4.054362],[-8.878795,-4.095527],[-8.029352,7.177495],[0.667053,9.257488],[4.167787,-8.328432],[-1.078166,-2.201807],[-4.646742,6.590170],[-2.510436,8.737202],[3.756215,9.271546],[7.848767,-9.130342],[0.196916,-0.806440],[0.034459,-9.602221],[1.824488,3.971842],[-1.878337,-5.789263],[-0.703114,-5.486224],[0.488265,8.560150],[3.112579,-1.707603],[-5.366194,-1.577775],[-1.612552,-2.870928],[-0.184422,-7.361293],[9.424295,0.300547],[-2.526412,4.245907],[-5.931097,5.488618],[4.723929,-1.359297],[2.513917,1.103829],[-5.727612,9.903045],[-0.624605,-3.702935],[9.513769,4.303682],[-9.691158,-3.447284],[-7.200697,0.636131],[8.726845,-9.385893],[0.642871,4.831030],[-1.999206,6.771574],[1.657318,4.358299],[-2.347350,-2.024552],[3.783941,6.476962],[7.775414,-5.199679],[0.903534,-5.048235],[-9.041552,0.908962],[6.456492,0.287392],[5.743217,-7.160867],[6.878172,4.913457],[5.250352,0.486878],[3.904949,3.397936],[2.248121,-4.281911],[9.857006,8.715262],[-1.205284,-7.505153],[-2.974577,5.473151],[-8.049671,-7.670652],[4.299937,1.879105],[8.560498,6.614862],[0.357456,5.483773],[-7.502524,4.236822],[-9.597459,-2.795190],[1.215116,7.750441],[-6.349003,-0.798443],[-6.755823,-4.302091],[-0.729398,1.306913],[2.265163,-6.297509],[7.956811,0.337663],[2.783845,5.441151],[7.877878,-7.913493],[-4.377253,-3.612778],[-9.713139,7.555048],[0.776980,4.063428],[-5.330664,-1.882415],[4.025924,-1.318320],[-6.933798,4.416605],[6.833761,-4.495200],[-0.566643,9.914482],[-9.644520,8.807865],[-9.411102,8.080915],[-2.066989,5.252957],[3.273832,-3.149647],[-0.121649,2.747407],[-2.669613,9.734236],[-2.533380,3.173135],[-6.156287,3.064719],[-1.302931,-0.408602],[-4.664078,8.623830],[-0.948283,9.850355],[-9.331277,-4.599173],[-7.565144,1.409321],[-1.575550,-6.708954],[-8.882622,3.112153],[2.015604,3.415985],[1.378293,-2.937825],[-8.125686,2.713600],[8.260211,-1.522247],[-5.670215,-0.251046],[1.531463,-9.681841],[-1.746611,-4.006087],[-3.066528,-6.404920],[-7.986694,2.018159],[6.761722,8.035800],[5.049277,-9.533807],[3.182359,-8.004326],[7.147851,1.703916],[0.668806,2.377593],[-6.006702,-1.912342],[7.275028,-4.344105],[2.233509,-5.026126],[-7.524210,-1.434350],[-3.281909,-8.034483],[0.083796,1.922118],[0.620852,6.306331],[-8.317204,9.240492],[-4.388644,4.917548],[-0.638803,-6.349995],[-9.595126,-6.245811],[-7.225554,-8.383306],[6.992859,1.652972],[-8.053937,6.449902],[7.681037,-3.346790],[5.803585,-7.917983],[7.362018,-3.070202],[-6.287901,4.407674],[2.419624,0.544648],[-3.440828,-5.215963],[-3.465428,7.617725],[-4.834640,-3.998283],[0.005161,-6.892513],[-2.726555,7.199508],[-0.723060,3.005765],[-9.326984,6.443669],[-3.434007,2.976488],[7.601852,-0.406851],[6.002346,-1.023118],[4.890000,3.905527],[7.202507,9.169233],[8.083106,4.891944],[-1.952352,-5.693336],[-8.098267,-9.239008],[-7.540279,2.895734],[8.575671,6.013319],[0.577418,2.499984],[-2.359839,-2.926155],[-2.159140,-6.216787],[-3.551758,1.386352],[-2.449112,5.631634],[-3.801660,-4.225042],[5.742011,-9.340118],[2.546749,-8.762579],[0.327269,2.739983],[-6.056154,9.679312],[-4.280351,-0.306222],[4.721453,3.753678],[8.784851,-0.088691],[4.023939,-0.493251],[5.359527,3.460613],[-4.248987,6.666328],[2.645384,-9.132237],[-6.451479,-4.488514],[4.337440,1.846234],[9.100502,-0.930192],[9.868523,-9.760479],[6.520117,-5.954230],[3.064428,-8.974758],[0.422723,3.438383],[-1.792301,-0.845244],[4.469849,7.595535],[-8.786077,6.820803],[-5.015909,-3.706237],[5.505575,-7.978178],[-9.621777,0.518558],[-4.755066,6.392737],[1.069094,5.714132],[-2.199222,3.669487],[-9.965996,-5.489518],[7.670156,-7.233055],[-7.834117,-1.907726],[6.063635,-5.177093],[5.963857,6.343480],[2.949678,2.680565],[2.416526,4.512120],[-6.324824,4.259309],[1.241315,4.143098],[-9.880567,-1.745435],[5.587613,-3.527513],[2.333733,-7.057624],[-0.621755,3.807402],[-5.665014,-3.308774],[7.450829,-7.372177],[-6.240767,-2.754032],[8.345230,4.120257],[-2.009571,-5.089436],[-9.147872,-8.544125],[-8.850997,-5.234475],[5.134741,-9.835419],[-7.148265,0.257332],[-8.460534,6.102958],[-2.357746,3.967146],[-5.039395,8.627738],[-4.488268,-8.370162],[-1.936436,7.279297],[0.303800,3.886845],[5.646898,-2.613054],[-1.428498,1.034714],[1.066943,-7.102277],[-9.664897,-2.082144],[-5.868343,2.511665],[9.252163,9.969777],[8.794315,-2.461593],[-0.189636,2.821420],[-4.264064,7.212770],[7.588267,5.935966],[9.903673,-5.096008],[7.259946,-5.312006],[-9.532285,0.650945],[1.643778,2.678972],[3.126859,4.393779],[0.346454,8.106500],[0.015833,5.440381],[9.321375,8.750703],[-8.468381,-4.951968],[-6.905120,9.815424],[5.317847,4.430540],[7.547634,9.539293],[-2.707296,-8.939218],[6.655091,8.119175],[-1.406906,5.849445],[-0.005895,-3.075751],[9.540695,-9.993167],[-5.006142,-6.583855],[-5.497673,-2.094871],[1.551792,-0.653254],[3.298187,9.080510],[-7.664696,0.268389],[5.078304,-9.887343],[9.053026,-0.290105],[-8.912106,4.596104],[-4.545664,-6.717034],[2.754871,-7.826092],[-0.065021,-8.024733],[1.452111,-6.931093],[9.620449,-6.043418],[-9.091560,-4.298632],[-8.291020,-0.645729],[9.944742,1.314686],[-4.919295,2.783025],[-8.951630,-5.186377],[-1.264568,-1.733439],[-6.063012,-6.281420],[-8.759804,9.960093],[1.005738,8.817800],[-5.169828,-3.755296],[4.855344,-5.356111],[1.883617,0.708895],[6.819850,-0.778570],[-2.715944,-0.439519],[9.468166,-7.038971],[4.540687,0.958712],[6.191823,-2.617820],[-3.974910,-0.840355],[-5.896320,8.557859],[-1.722937,-9.179087],[-6.242856,6.137834],[2.844759,-0.037821],[-3.687028,8.495538],[-4.995691,6.476691],[3.280997,6.885858],[-9.107226,8.401670],[-2.267449,8.258949],[9.887137,8.436651],[-8.870212,-2.347326],[-5.196603,8.411543],[-5.997805,-4.396613],[2.676927,-8.265101],[-1.053800,-4.270797],[1.283585,3.369790],[3.349466,-0.718442],[-3.682259,-6.739622],[4.241998,0.513560],[5.527113,-5.720928],[7.561846,-7.865832],[-8.732882,3.602452],[6.153672,-6.795729],[4.176322,-1.648156],[-4.698294,7.423672],[-3.326212,5.971799],[-1.222321,1.947957],[0.319375,6.279943],[3.381580,3.821828],[5.677653,-0.109630]], dtype = "float32")#candidate|5521|(330, 2)|const|float32
call_5520 = relay.TupleGetItem(func_3973_call(relay.reshape(const_5521.astype('float32'), [5, 12, 11])), 1)
call_5522 = relay.TupleGetItem(func_3976_call(relay.reshape(const_5521.astype('float32'), [5, 12, 11])), 1)
var_5523 = relay.var("var_5523", dtype = "float32", shape = (330, 2))#candidate|5523|(330, 2)|var|float32
bop_5524 = relay.bitwise_or(const_5521.astype('int16'), relay.reshape(var_5523.astype('int16'), relay.shape_of(const_5521))) # shape=(330, 2)
func_4226_call = mod.get_global_var('func_4226')
func_4230_call = mutated_mod.get_global_var('func_4230')
const_5530 = relay.const([7.680525,-3.854774,2.036086,-6.591642,-6.600812,8.658508,-8.497428,9.623226,1.107728,-2.575993,-7.410494,4.893420,-9.881863,7.507275,3.048059,-4.248461,-6.816517,0.496620,-4.196968,2.480080,-5.612126,5.490626,-6.611071,-5.809682,4.078741,4.819119,7.103978,-4.320851,-8.717024,6.398675,4.099029,5.668789,-5.407384,4.185975,-2.005769,9.330577,-9.221424,4.906663,7.516107,-9.372556,-8.127450,7.610231,5.491251,-2.209564,8.729320,0.634025,5.492541,7.213052,4.642263,-0.136282,8.340097,-3.956856,-8.500401,5.854052,4.022317,-1.185235,4.705029,1.058314,8.477977,4.387424,-5.805985,-1.322266,3.945992,0.094053,-4.066534,-0.966365,-5.384261,7.440439,-0.271804,-6.773789,5.909449,3.834770,-2.605379,5.134792,-3.748488,5.713950,2.460161,7.562123,4.212241,6.541520,-0.276507,7.426676,-9.181646,-7.072477,2.884953,2.736262,1.144600,-1.904901,3.315498,-4.682812,-9.365993,-4.480106,2.450306,-6.825033,3.385607,-0.607753,7.667306,-1.237553,4.968508,-6.093497,0.008315,0.481591,-2.803460,7.154560,2.478457,-0.869037,8.191814,4.830211,-4.954987,0.708500,3.314800,8.965726,2.773125,-0.394953,-0.126883,-1.225500,-6.018985,6.250722,8.570015,8.393345,-5.070082,-2.310485,-3.032322,-3.987964,0.930000,-7.628084,1.359026,8.512639,9.960599,3.052626,-4.123790,-6.586203,8.425071,7.704517,-9.966042,7.940341,-2.655214,-1.153029,5.144581,7.276025,-1.412865,4.177440,-6.234728,-1.859579], dtype = "float32")#candidate|5530|(144,)|const|float32
call_5529 = relay.TupleGetItem(func_4226_call(relay.reshape(const_5530.astype('float32'), [144, 1]), relay.reshape(const_5530.astype('float32'), [2, 6, 12]), ), 1)
call_5531 = relay.TupleGetItem(func_4230_call(relay.reshape(const_5530.astype('float32'), [144, 1]), relay.reshape(const_5530.astype('float32'), [2, 6, 12]), ), 1)
func_2187_call = mod.get_global_var('func_2187')
func_2190_call = mutated_mod.get_global_var('func_2190')
const_5533 = relay.const([-4,-10,-9,-1,-10,6,3,-10,3,-1,-4,2,-7,-5,-4,4,-5,-2,1,9,-8,-3,-2,7,1,-10,2,-8,-7,-3,7,-6,-2,-7,4,4,2,-10,-2,-10,6,9,-5,6,10,-10,-7,-1,5,-1,3,8,5,-2,6,2,-3,1,-8,8,6,-6,2,-3,-5,-5,-10,-4,10,3,-7,9,4,5,-9,-1,-9,-10,-2,8,-7,-6,6,1,-7,4,-9,-3,5,6,-1,8,4,2,3,5,-3,-7,2,-6,4,4,-5,8,-7,5,-1,-1,-3,3,3,7,1,-6,4,6,2,-3,9,10,-6,-5,9,4,-8,-9,-6,-8,10,4,6,6,-1,6,10,7,10,-3,-9,1,3,-10,-6,-10,2,2,5,5,-7,-8,-6,1,7,3,8,-5,3,3,-2,6,6,-2,-8,-7,-10,9,9,2,-3,-4,-10,-3,-2,2,9,10,10,6,-2,10,-7,-10,9,4,8,3,7,-10,-2,5,-4,7], dtype = "int16")#candidate|5533|(192,)|const|int16
var_5534 = relay.var("var_5534", dtype = "float64", shape = ())#candidate|5534|()|var|float64
call_5532 = relay.TupleGetItem(func_2187_call(relay.reshape(const_5533.astype('int16'), [4, 4, 12]), relay.reshape(var_5534.astype('float64'), []), ), 3)
call_5535 = relay.TupleGetItem(func_2190_call(relay.reshape(const_5533.astype('int16'), [4, 4, 12]), relay.reshape(var_5534.astype('float64'), []), ), 3)
bop_5536 = relay.bitwise_xor(var_5523.astype('int16'), var_5534.astype('int16')) # shape=(330, 2)
output = relay.Tuple([call_5470,call_5486,call_5500,const_5501,call_5520,bop_5524,call_5529,const_5530,call_5532,const_5533,bop_5536,])
output2 = relay.Tuple([call_5471,call_5487,call_5502,const_5501,call_5522,bop_5524,call_5531,const_5530,call_5535,const_5533,bop_5536,])
func_5547 = relay.Function([var_5523,var_5534,], output)
mod['func_5547'] = func_5547
mod = relay.transform.InferType()(mod)
mutated_mod['func_5547'] = func_5547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5547_call = mutated_mod.get_global_var('func_5547')
var_5549 = relay.var("var_5549", dtype = "float32", shape = (330, 2))#candidate|5549|(330, 2)|var|float32
var_5550 = relay.var("var_5550", dtype = "float64", shape = ())#candidate|5550|()|var|float64
call_5548 = func_5547_call(var_5549,var_5550,)
output = call_5548
func_5551 = relay.Function([var_5549,var_5550,], output)
mutated_mod['func_5551'] = func_5551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_5579 = relay.TupleGetItem(func_3892_call(), 3)
call_5580 = relay.TupleGetItem(func_3894_call(), 3)
output = call_5579
output2 = call_5580
func_5587 = relay.Function([], output)
mod['func_5587'] = func_5587
mod = relay.transform.InferType()(mod)
mutated_mod['func_5587'] = func_5587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5587_call = mutated_mod.get_global_var('func_5587')
call_5588 = func_5587_call()
output = call_5588
func_5589 = relay.Function([], output)
mutated_mod['func_5589'] = func_5589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_5597 = relay.TupleGetItem(func_4792_call(), 0)
call_5598 = relay.TupleGetItem(func_4793_call(), 0)
output = call_5597
output2 = call_5598
func_5600 = relay.Function([], output)
mod['func_5600'] = func_5600
mod = relay.transform.InferType()(mod)
output = func_5600()
func_5601 = relay.Function([], output)
mutated_mod['func_5601'] = func_5601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_5602 = relay.TupleGetItem(func_4872_call(), 2)
call_5603 = relay.TupleGetItem(func_4873_call(), 2)
output = relay.Tuple([call_5602,])
output2 = relay.Tuple([call_5603,])
func_5612 = relay.Function([], output)
mod['func_5612'] = func_5612
mod = relay.transform.InferType()(mod)
mutated_mod['func_5612'] = func_5612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5612_call = mutated_mod.get_global_var('func_5612')
call_5613 = func_5612_call()
output = call_5613
func_5614 = relay.Function([], output)
mutated_mod['func_5614'] = func_5614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_5667 = relay.TupleGetItem(func_3892_call(), 2)
call_5668 = relay.TupleGetItem(func_3894_call(), 2)
uop_5677 = relay.cosh(call_5667.astype('float64')) # shape=(1, 4, 7)
uop_5679 = relay.cosh(call_5668.astype('float64')) # shape=(1, 4, 7)
output = relay.Tuple([uop_5677,])
output2 = relay.Tuple([uop_5679,])
func_5685 = relay.Function([], output)
mod['func_5685'] = func_5685
mod = relay.transform.InferType()(mod)
output = func_5685()
func_5686 = relay.Function([], output)
mutated_mod['func_5686'] = func_5686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_5689 = func_5171_call()
call_5690 = func_5171_call()
output = call_5689
output2 = call_5690
func_5698 = relay.Function([], output)
mod['func_5698'] = func_5698
mod = relay.transform.InferType()(mod)
output = func_5698()
func_5699 = relay.Function([], output)
mutated_mod['func_5699'] = func_5699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_5729 = relay.TupleGetItem(func_2920_call(), 0)
call_5730 = relay.TupleGetItem(func_2922_call(), 0)
output = call_5729
output2 = call_5730
func_5733 = relay.Function([], output)
mod['func_5733'] = func_5733
mod = relay.transform.InferType()(mod)
output = func_5733()
func_5734 = relay.Function([], output)
mutated_mod['func_5734'] = func_5734
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5738 = relay.var("var_5738", dtype = "int64", shape = (7, 14, 16))#candidate|5738|(7, 14, 16)|var|int64
var_5739 = relay.var("var_5739", dtype = "int64", shape = (7, 14, 16))#candidate|5739|(7, 14, 16)|var|int64
bop_5740 = relay.bitwise_and(var_5738.astype('int64'), relay.reshape(var_5739.astype('int64'), relay.shape_of(var_5738))) # shape=(7, 14, 16)
output = bop_5740
output2 = bop_5740
func_5744 = relay.Function([var_5738,var_5739,], output)
mod['func_5744'] = func_5744
mod = relay.transform.InferType()(mod)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5744_call = mutated_mod.get_global_var('func_5744')
var_5746 = relay.var("var_5746", dtype = "int64", shape = (7, 14, 16))#candidate|5746|(7, 14, 16)|var|int64
var_5747 = relay.var("var_5747", dtype = "int64", shape = (7, 14, 16))#candidate|5747|(7, 14, 16)|var|int64
call_5745 = func_5744_call(var_5746,var_5747,)
output = call_5745
func_5748 = relay.Function([var_5746,var_5747,], output)
mutated_mod['func_5748'] = func_5748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mod.get_global_var('func_3287')
func_3289_call = mutated_mod.get_global_var('func_3289')
call_5793 = relay.TupleGetItem(func_3287_call(), 0)
call_5794 = relay.TupleGetItem(func_3289_call(), 0)
func_2160_call = mod.get_global_var('func_2160')
func_2163_call = mutated_mod.get_global_var('func_2163')
var_5800 = relay.var("var_5800", dtype = "float32", shape = (144,))#candidate|5800|(144,)|var|float32
call_5799 = func_2160_call(relay.reshape(var_5800.astype('float32'), [2, 6, 12]))
call_5801 = func_2160_call(relay.reshape(var_5800.astype('float32'), [2, 6, 12]))
output = relay.Tuple([call_5793,call_5799,var_5800,])
output2 = relay.Tuple([call_5794,call_5801,var_5800,])
func_5802 = relay.Function([var_5800,], output)
mod['func_5802'] = func_5802
mod = relay.transform.InferType()(mod)
var_5803 = relay.var("var_5803", dtype = "float32", shape = (144,))#candidate|5803|(144,)|var|float32
output = func_5802(var_5803)
func_5804 = relay.Function([var_5803], output)
mutated_mod['func_5804'] = func_5804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5733_call = mod.get_global_var('func_5733')
func_5734_call = mutated_mod.get_global_var('func_5734')
call_5828 = func_5733_call()
call_5829 = func_5733_call()
var_5864 = relay.var("var_5864", dtype = "float64", shape = (110,))#candidate|5864|(110,)|var|float64
bop_5865 = relay.not_equal(call_5828.astype('bool'), relay.reshape(var_5864.astype('bool'), relay.shape_of(call_5828))) # shape=(110,)
bop_5868 = relay.not_equal(call_5829.astype('bool'), relay.reshape(var_5864.astype('bool'), relay.shape_of(call_5829))) # shape=(110,)
func_4781_call = mod.get_global_var('func_4781')
func_4783_call = mutated_mod.get_global_var('func_4783')
const_5872 = relay.const(-3.667828, dtype = "float64")#candidate|5872|()|const|float64
call_5871 = relay.TupleGetItem(func_4781_call(relay.reshape(const_5872.astype('float64'), [])), 1)
call_5873 = relay.TupleGetItem(func_4783_call(relay.reshape(const_5872.astype('float64'), [])), 1)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_5879 = relay.TupleGetItem(func_4872_call(), 2)
call_5880 = relay.TupleGetItem(func_4873_call(), 2)
func_4333_call = mod.get_global_var('func_4333')
func_4336_call = mutated_mod.get_global_var('func_4336')
const_5891 = relay.const([6.571979,7.258565,4.765848,1.264153,-6.664068,-2.716068,-4.965075,7.348104,5.678276,4.019505,5.420541,5.640810,6.953176,5.611675,-1.089265,-2.160705,-7.870024,-4.910450,3.786314,-0.937673,-2.373756,-9.311578,-2.629458,-9.684377,0.654361,-5.758151,6.532360,9.015561,6.390290,1.616139,5.739688,3.299286,7.364831,5.632505,-6.521050,4.798639,4.772272,7.858361,1.401040,5.069809,4.509543,0.773282,4.345438,2.762896,8.084446,-0.665311,-1.372958,8.665359,8.418286,-6.905941,-0.436594,5.057726,1.517017,6.027445,-6.059192,6.150868,3.409592,8.157876,4.500822,0.912296,9.170192,5.791815,5.105002,-6.152448,7.792690,-2.324993,-1.455980,3.082324,-1.144011,-6.388321,-0.755429,-0.385544,-4.613847,-0.737538,-7.265534,6.504302,-1.537238,1.537838,0.453459,-5.030683,-0.360904,-4.585211,-1.988320,-2.398259,2.931039,-5.826972,-0.367690,8.704145,-2.062870,-5.879236,1.344195,-4.757567,-3.067677,4.830220,5.342792,0.288909,8.202534,-9.986373,5.712117,-6.312907], dtype = "float64")#candidate|5891|(100,)|const|float64
call_5890 = relay.TupleGetItem(func_4333_call(relay.reshape(const_5891.astype('float64'), [2, 10, 5])), 4)
call_5892 = relay.TupleGetItem(func_4336_call(relay.reshape(const_5891.astype('float64'), [2, 10, 5])), 4)
output = relay.Tuple([bop_5865,call_5871,const_5872,call_5879,call_5890,const_5891,])
output2 = relay.Tuple([bop_5868,call_5873,const_5872,call_5880,call_5892,const_5891,])
func_5895 = relay.Function([var_5864,], output)
mod['func_5895'] = func_5895
mod = relay.transform.InferType()(mod)
var_5896 = relay.var("var_5896", dtype = "float64", shape = (110,))#candidate|5896|(110,)|var|float64
output = func_5895(var_5896)
func_5897 = relay.Function([var_5896], output)
mutated_mod['func_5897'] = func_5897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5733_call = mod.get_global_var('func_5733')
func_5734_call = mutated_mod.get_global_var('func_5734')
call_5902 = func_5733_call()
call_5903 = func_5733_call()
output = relay.Tuple([call_5902,])
output2 = relay.Tuple([call_5903,])
func_5912 = relay.Function([], output)
mod['func_5912'] = func_5912
mod = relay.transform.InferType()(mod)
output = func_5912()
func_5913 = relay.Function([], output)
mutated_mod['func_5913'] = func_5913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_5961 = relay.TupleGetItem(func_2920_call(), 3)
call_5962 = relay.TupleGetItem(func_2922_call(), 3)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_5963 = relay.TupleGetItem(func_4872_call(), 1)
call_5964 = relay.TupleGetItem(func_4873_call(), 1)
var_5976 = relay.var("var_5976", dtype = "float64", shape = (110, 2))#candidate|5976|(110, 2)|var|float64
bop_5977 = relay.logical_and(call_5963.astype('bool'), var_5976.astype('bool')) # shape=(110, 2)
bop_5980 = relay.logical_and(call_5964.astype('bool'), var_5976.astype('bool')) # shape=(110, 2)
output = relay.Tuple([call_5961,bop_5977,])
output2 = relay.Tuple([call_5962,bop_5980,])
func_5989 = relay.Function([var_5976,], output)
mod['func_5989'] = func_5989
mod = relay.transform.InferType()(mod)
mutated_mod['func_5989'] = func_5989
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5990 = relay.var("var_5990", dtype = "float64", shape = (110, 2))#candidate|5990|(110, 2)|var|float64
func_5989_call = mutated_mod.get_global_var('func_5989')
call_5991 = func_5989_call(var_5990)
output = call_5991
func_5992 = relay.Function([var_5990], output)
mutated_mod['func_5992'] = func_5992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_6030 = relay.TupleGetItem(func_3892_call(), 0)
call_6031 = relay.TupleGetItem(func_3894_call(), 0)
func_4819_call = mod.get_global_var('func_4819')
func_4821_call = mutated_mod.get_global_var('func_4821')
call_6032 = relay.TupleGetItem(func_4819_call(), 0)
call_6033 = relay.TupleGetItem(func_4821_call(), 0)
output = relay.Tuple([call_6030,call_6032,])
output2 = relay.Tuple([call_6031,call_6033,])
func_6038 = relay.Function([], output)
mod['func_6038'] = func_6038
mod = relay.transform.InferType()(mod)
mutated_mod['func_6038'] = func_6038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6038_call = mutated_mod.get_global_var('func_6038')
call_6039 = func_6038_call()
output = call_6039
func_6040 = relay.Function([], output)
mutated_mod['func_6040'] = func_6040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_6048 = relay.TupleGetItem(func_4792_call(), 0)
call_6049 = relay.TupleGetItem(func_4793_call(), 0)
var_6056 = relay.var("var_6056", dtype = "float64", shape = (110,))#candidate|6056|(110,)|var|float64
bop_6057 = relay.add(call_6048.astype('int16'), relay.reshape(var_6056.astype('int16'), relay.shape_of(call_6048))) # shape=(110,)
bop_6060 = relay.add(call_6049.astype('int16'), relay.reshape(var_6056.astype('int16'), relay.shape_of(call_6049))) # shape=(110,)
output = relay.Tuple([bop_6057,])
output2 = relay.Tuple([bop_6060,])
func_6063 = relay.Function([var_6056,], output)
mod['func_6063'] = func_6063
mod = relay.transform.InferType()(mod)
var_6064 = relay.var("var_6064", dtype = "float64", shape = (110,))#candidate|6064|(110,)|var|float64
output = func_6063(var_6064)
func_6065 = relay.Function([var_6064], output)
mutated_mod['func_6065'] = func_6065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5455_call = mod.get_global_var('func_5455')
func_5456_call = mutated_mod.get_global_var('func_5456')
call_6085 = relay.TupleGetItem(func_5455_call(), 1)
call_6086 = relay.TupleGetItem(func_5456_call(), 1)
output = relay.Tuple([call_6085,])
output2 = relay.Tuple([call_6086,])
func_6087 = relay.Function([], output)
mod['func_6087'] = func_6087
mod = relay.transform.InferType()(mod)
output = func_6087()
func_6088 = relay.Function([], output)
mutated_mod['func_6088'] = func_6088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4819_call = mod.get_global_var('func_4819')
func_4821_call = mutated_mod.get_global_var('func_4821')
call_6107 = relay.TupleGetItem(func_4819_call(), 0)
call_6108 = relay.TupleGetItem(func_4821_call(), 0)
output = relay.Tuple([call_6107,])
output2 = relay.Tuple([call_6108,])
func_6115 = relay.Function([], output)
mod['func_6115'] = func_6115
mod = relay.transform.InferType()(mod)
mutated_mod['func_6115'] = func_6115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6115_call = mutated_mod.get_global_var('func_6115')
call_6116 = func_6115_call()
output = call_6116
func_6117 = relay.Function([], output)
mutated_mod['func_6117'] = func_6117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4373_call = mutated_mod.get_global_var('func_4373')
call_6118 = relay.TupleGetItem(func_4372_call(), 1)
call_6119 = relay.TupleGetItem(func_4373_call(), 1)
const_6132 = relay.const([[[1.872626,-9.542962,-5.639014,9.688367],[8.071103,8.834226,0.931973,-6.742696],[2.787215,4.828164,0.717353,-9.735644],[-1.894421,1.582954,-4.265718,-4.561677],[7.994248,0.611127,-4.678532,0.566154],[9.913072,4.243351,5.067162,-3.564498],[-3.453146,4.103962,-2.848497,-5.793134],[-7.021053,-4.801742,5.139065,-9.571100],[3.304712,-1.963898,0.916262,4.652530],[-4.207563,1.167002,4.753842,7.633187],[-6.569218,3.924054,-5.623361,9.841753],[-6.159183,-2.324375,-7.617134,-6.364217]],[[-5.080658,-8.947832,2.411965,-8.161914],[-0.340355,6.603192,-8.556259,9.418862],[4.703563,1.472569,-0.750879,-6.322353],[8.004734,-0.752634,-7.943810,2.420504],[5.796343,-2.847649,-4.430888,3.840793],[-5.073779,-9.770255,3.927845,9.561594],[-8.873143,-3.870022,9.982518,8.546990],[3.408676,0.802539,0.114437,4.583737],[-2.908335,1.709195,-9.140883,3.003430],[4.757948,5.838787,3.406755,7.291876],[-5.309673,-7.077349,3.462204,-5.831485],[-1.829416,-2.699031,-3.477685,-9.897099]],[[5.142551,8.828995,-8.865216,-5.040275],[-1.389075,-4.159244,2.333398,-0.117154],[-7.694103,7.783393,-0.940561,-3.266316],[6.717434,-4.396222,-0.478691,-2.253071],[-8.490116,-0.585436,-4.537793,-1.413935],[-4.948818,-5.678827,7.907085,6.486218],[-9.286011,5.662564,-1.842192,9.066759],[-5.719952,-7.084455,-4.724810,-2.371082],[-8.859223,-6.600830,9.508248,-1.162676],[6.187260,7.778492,7.591718,-7.877330],[-5.931577,-5.381558,-1.165721,-9.375840],[-9.766276,0.766620,-4.260193,5.019831]],[[-3.439971,1.629951,6.254680,-4.030475],[3.560607,8.897479,-0.554389,-8.607997],[1.248399,-1.360438,-0.250396,-4.812692],[3.582574,1.514310,3.332756,-8.510690],[-8.638376,6.001219,8.771468,9.820246],[-6.041219,3.371553,-7.817947,0.852556],[6.966357,0.780378,-7.903538,-5.346284],[-6.023038,1.638961,-3.644853,5.772410],[-1.915733,-1.525122,-9.322774,-5.690461],[-6.211916,-7.814343,8.573323,-0.400909],[2.809426,-2.050133,0.135752,0.477421],[-0.766167,7.931996,-0.139907,-7.618875]],[[-2.166448,5.746786,-9.913072,4.889932],[9.898245,3.444166,0.399881,3.855205],[-6.693790,-5.935547,-2.232240,1.274453],[3.140795,-0.383259,7.625239,-4.531065],[0.345965,4.696222,0.861873,9.890305],[-4.347433,6.469542,-5.979344,-1.669887],[-3.372967,4.482563,-6.454256,8.351355],[1.591330,4.122611,-5.509245,-7.053374],[4.993044,7.792474,-0.613378,-4.053920],[-8.483212,-9.598558,-2.466609,3.085685],[-3.273188,-1.709242,7.708749,-5.856141],[0.911417,5.847882,5.352242,1.171933]],[[1.172264,4.289686,0.940074,-3.867246],[1.783928,8.512276,5.084006,-9.446523],[2.226638,-1.573417,-1.835477,7.940545],[4.828274,-7.987530,8.473365,5.002467],[-4.892774,-1.029962,-2.770121,7.616562],[-3.804448,-2.683680,2.446004,3.244058],[9.504058,1.876521,-8.275209,2.975745],[-3.136078,-9.305247,8.265212,-3.778082],[-3.445083,-4.278830,-0.985638,-8.735430],[-3.853540,-3.467416,7.050937,-2.745564],[-4.164460,-4.723664,-6.945549,-4.128348],[4.292301,-9.723520,-8.264678,3.143798]],[[-0.372973,-3.765405,7.091967,4.318937],[8.069058,-7.276542,4.281739,5.674432],[-9.015835,-5.940949,8.321264,6.137374],[5.033672,3.996615,1.098366,-7.292772],[-1.904932,-7.170055,6.920749,1.496910],[2.862992,1.687151,-0.384298,-3.808153],[-7.788174,-0.260397,2.141611,2.194599],[8.218761,1.564199,5.833352,-8.712006],[-3.821508,9.420006,-1.536760,-3.982604],[-2.150857,-9.311008,-6.708918,-6.167775],[7.435008,-0.482076,-1.751858,0.458993],[-8.784309,-4.312260,-9.262064,-7.447698]],[[3.051648,-3.313351,-0.812495,-2.235569],[-1.015389,-5.270000,0.267500,-0.036128],[4.172996,-6.742073,-3.740240,3.177578],[-0.015092,-0.913266,5.786556,4.010094],[-5.812887,-5.016282,-2.729339,-6.856577],[-3.858979,4.634911,0.852974,-7.274781],[-1.670590,-5.573423,7.711797,9.804304],[-3.076740,-4.610463,-4.248627,-8.234555],[-7.165438,-5.499092,4.832200,1.473303],[0.833825,-4.433115,-9.111916,3.877842],[5.553651,3.481831,0.358902,-1.584898],[-5.931585,8.470613,-7.084331,-3.660124]],[[4.075659,5.411241,7.080642,-2.732540],[5.422197,5.966373,4.298648,-8.591994],[-4.287131,7.461712,-0.659487,5.455791],[6.525066,-2.781218,6.205538,-2.121187],[5.870983,1.467804,-7.177170,3.606505],[-4.070696,-6.697857,7.530801,-0.480233],[-4.925095,1.119449,2.462941,-7.988745],[-6.987768,-8.157368,7.115471,-4.111499],[-1.866692,3.528860,0.586160,-8.422986],[2.732549,4.997040,8.608222,-7.168774],[-7.128503,3.509387,7.532932,-7.241948],[-3.968257,9.824167,6.499246,-1.079887]],[[4.943065,-5.293798,-3.866603,3.656740],[4.569552,-7.408887,-3.045044,8.666807],[-0.169999,1.143029,-8.521098,8.479853],[-5.394572,-4.218631,-0.717749,-2.862385],[-2.148603,-0.945730,5.446769,-6.519687],[3.602665,-9.390132,7.293748,-2.333911],[-4.868749,2.661914,6.212831,8.464905],[7.100229,4.055052,-5.471517,-8.902648],[-0.020414,1.530051,-0.511297,3.688263],[-5.578497,0.961971,5.169735,2.241500],[0.992182,-3.725966,-3.126461,2.942381],[4.399445,4.837519,-3.866526,-5.627929]],[[9.175949,-3.784106,5.170093,3.664407],[2.312829,7.211513,-8.824001,-0.469165],[-5.171375,-1.734226,-9.987706,-2.462310],[-7.218350,5.470137,4.583612,1.502841],[9.580128,-0.603532,3.839470,-5.973961],[9.338199,0.157352,6.827652,2.336012],[-9.105594,-6.297392,0.909866,-1.444605],[-1.493783,-0.991090,0.256242,-3.355994],[-5.205959,0.854985,-3.899473,-9.694241],[-6.532844,5.497631,-0.660293,6.902330],[-2.383887,1.778409,-8.085320,1.301926],[-8.151860,3.829401,-3.142535,-8.485476]],[[-4.636616,-6.835684,-4.189025,-2.502428],[3.075270,-3.769400,7.610707,-4.968840],[0.304053,4.715871,-4.862317,-0.159739],[0.225575,-7.928344,-6.447327,-9.484385],[3.889827,0.962691,6.296643,-9.964947],[-6.046884,-6.432124,-8.544462,0.702856],[7.477428,1.357721,-1.239420,-2.892560],[0.730221,6.622882,5.236276,4.416341],[-1.325389,-9.042144,-5.015009,-7.051186],[6.098498,-5.278086,-8.129773,5.406632],[3.155450,5.727722,0.330764,8.927570],[-4.074392,-8.467465,-1.679311,-5.355856]],[[-1.404695,-4.024672,1.517303,1.543620],[-9.366848,-8.753151,-0.156092,-6.753847],[9.281772,3.183567,9.636090,8.282739],[4.082189,9.608603,5.952607,-3.116316],[1.086329,0.575247,-3.273358,0.634493],[-8.992000,9.657333,-4.655176,-7.493107],[2.047509,-3.734046,-2.911467,-0.911212],[2.504456,7.092632,-3.026432,-9.708402],[3.443362,-0.505838,5.090591,-1.200846],[-0.140086,-0.283977,8.744694,-7.064559],[-9.157321,4.444641,-3.838357,-4.418151],[1.035035,7.774856,9.315041,6.957980]]], dtype = "float32")#candidate|6132|(13, 12, 4)|const|float32
bop_6133 = relay.mod(call_6118.astype('float64'), relay.reshape(const_6132.astype('float64'), relay.shape_of(call_6118))) # shape=(13, 12, 4)
bop_6136 = relay.mod(call_6119.astype('float64'), relay.reshape(const_6132.astype('float64'), relay.shape_of(call_6119))) # shape=(13, 12, 4)
output = bop_6133
output2 = bop_6136
func_6143 = relay.Function([], output)
mod['func_6143'] = func_6143
mod = relay.transform.InferType()(mod)
output = func_6143()
func_6144 = relay.Function([], output)
mutated_mod['func_6144'] = func_6144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5600_call = mod.get_global_var('func_5600')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_6156 = func_5600_call()
call_6157 = func_5600_call()
func_4249_call = mod.get_global_var('func_4249')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_6175 = func_4249_call()
call_6176 = func_4249_call()
func_3157_call = mod.get_global_var('func_3157')
func_3159_call = mutated_mod.get_global_var('func_3159')
call_6181 = relay.TupleGetItem(func_3157_call(), 0)
call_6182 = relay.TupleGetItem(func_3159_call(), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3736_call = mutated_mod.get_global_var('func_3736')
const_6186 = relay.const([1.042829,-3.577160,6.003615,-4.316705,1.743482,-1.099249,-4.082691,2.656148,-9.162185,-2.573355,8.340460,5.223948,-6.496288,6.757291,7.649172,-3.003747,6.962358,-5.118811,-4.542874,8.942864,-6.389379,-0.991006,-8.066176,-9.990839,-0.795740,-0.135554,4.597415,8.360501,8.695748,4.899390,-8.911185,-7.502053,-3.186893,-5.068213,1.700714,-0.726311,9.075179,-9.513465,-8.185081,4.211343,5.945045,3.193015,9.486020,-7.320646,4.326836,3.869130,5.046335,-6.828378,-8.665338,-4.388378,-0.870560,-4.542585,0.214274,1.109659,4.712191,-3.213004,6.055501,7.682843,2.122984,4.893350,2.293704,-6.306447,-6.721573,-5.987356,-0.941100,5.319771,-7.132436,-3.252210,-1.583513,6.447342,-0.824534,6.253843,3.999199,-9.791211,-0.240670,-2.178535,-9.221583,4.524029,2.703172,-4.124188,-5.644450,-0.190908,8.291830,8.832123,-9.157690,0.628915,-9.982861,-5.759803,-5.914319,-3.877357,9.176604,-6.420028,-1.360108,-6.452970,-6.612592,1.992755,-5.870709,0.363793,-0.085081,-5.764760,6.415154,-5.426800,-4.774763,-2.814191,6.094817,8.625578,6.108308,4.101676,7.707489,6.592895,-6.355810,4.789669,-3.032065,-8.376909,5.443431,1.768062,-9.470151,-6.737591,5.744821,7.405822,-3.842400,5.221120,9.720231,4.151286,-5.048319,-3.088383,9.764993,-0.752806,-2.327835,-8.437512,7.296848,-9.849487,7.002596,-7.566088,9.239248,-2.056085,-9.528517,7.005489,-2.752924,2.285960,0.705833,3.987399,8.601354,-2.997286,-2.791757,9.187650,5.072285,2.287951,-9.226581,5.959717,-2.651593,2.096011,6.338843,-4.125644,0.358491,-3.245687,0.369433,2.648160,2.791062,-7.400418,0.306176,7.857129,5.266474,1.806858,-7.744151,-4.900844,-5.385373,-7.373347,-6.597575,3.140927,-8.104618,0.191827,4.160064,-2.422788,-6.573944,-7.615750,-5.255113,-7.937381,8.724554,1.618366,-1.449065,-8.433264,-6.855770,-3.008895,9.228824,-8.655574,-0.354906,4.403607,0.924193,-4.038483,-0.933258,1.455345,9.993318,-3.263674,2.974950,-1.328475,3.102094,6.701406,3.846383,1.657764,9.668391,-9.476739,1.075156,-7.625905,2.176522,-5.375531,0.596112,-3.175916,-8.208743,4.754018,5.070123,2.389126,-8.600849,-2.044819,8.379773,-8.255723,0.558533,-6.048697,-9.809868,5.237497,4.714561,0.698821,5.581517,2.273150,0.182471,-6.895842,0.577060,5.971360,-0.858825,5.741199,9.902253,-1.318411,8.545886,7.108817,7.162297,3.755062,3.393121,-4.027141,7.144341,-7.784638,-8.986413,8.728568,-5.345118,-5.384195,-6.986557,-5.308316,3.359610,-5.420001,9.717858,4.953763,1.143668,-2.968724,4.204606,5.961146,-5.282030,4.807132,-6.432655,-4.473973,-1.505644,4.720559,8.908241,-9.744206,4.334592,8.710726,9.983048,7.260929,5.647052,8.235560,-0.474618,0.717964,-7.329682,-1.865876,0.332471,1.038859,6.081598,-7.394568,0.215460,7.270871,-0.616079,9.733346,3.994681,-2.395536,-3.064502,-0.192633,-4.250045,-8.066185,-4.780076,-2.616088,5.590348,9.789421,-1.475793,2.550845,9.954983,-2.840998,4.809333,6.957691,2.345520,-6.917530,8.609883,-8.686194,-5.663869,-2.110611,8.576579,8.414617,-1.846130,7.642311,-4.671628,-5.335048,-8.769947,7.488565,6.108614,-2.294672,-9.876159,-9.881913,6.974448,-7.702939,1.136546,6.053128,2.044900,-5.229514,5.937828,-7.771709,-2.133505,8.158587,-0.761423,8.895576,8.690662,-3.990928,-5.720719,7.610833,1.441144,4.498973,-8.608907,-7.412222,7.299364,-2.446222,-8.013770,0.033277,8.802672,2.762360,6.360938,1.766184,1.054049,8.630678,2.056851,1.777881,-4.877255,1.760710,4.635445,-4.375435,-0.323653,-7.247577,6.866007,-1.322656,-7.825861,-7.678953,-2.847064,0.932815,4.979546,5.053329,8.810035,-1.287750,8.297341,7.033193,0.535937,-6.765201,-6.623008,-3.809037,-9.010636,-6.548217,9.569026,-4.786736,5.441374,1.697275,-1.405855,0.064998,2.104504,2.924309,9.808403,-3.372249,-7.316123,8.016933,7.655831,7.376023,-5.018797,-7.557499,-9.325053,1.074185,-2.850907,5.978567,1.654559,1.639698,-9.362245,2.114654,0.476615,-3.207832,-1.430936,-2.003381,0.351230,1.848108,9.037574,2.202671,7.065619,2.949440,6.749853,-4.077595,7.531911,-2.151380,2.209032,-8.357989,1.998902,-7.493706,-8.247777,8.298079,-8.007124,7.488003,-4.278445,-6.766812,5.190481,-1.385213,-5.607305,4.684222,-8.574958,5.098068,0.235047,-1.521350,-2.993619,9.390124,5.492879,-2.598031,3.538338,8.212384,2.702818,5.353381,-2.460967,1.911138,0.342359,-2.481399,-7.017128,6.048212,6.897637,-3.382568,-2.688219,-1.064962,-7.157934,-1.282426,-2.197840,-4.503127,3.226685,-5.171692,2.386597,-9.839996,-0.866141,-8.627079,-7.185845,3.404347,1.253476,4.630280,8.649251,3.845219,-3.542139,1.616703,6.642092,-7.954664,-9.346180,-6.291849,6.793254,-8.577022,-6.439767,-1.543492,-9.763934,-5.596941,-9.114971,3.602418,-1.904326,6.464573,-5.877625,3.187497,-1.798557,-2.132335,4.043475,-6.762940,0.914812,-9.538605,5.088928,-5.990613,-6.892587,8.150798,-1.143227,-0.758975,5.347994,-8.588962,0.537655,-5.335620,3.351727,-0.895600,0.447722,2.668777,7.395539,-7.816566,6.078601,-1.686989,-1.989997,-8.645476,-0.680352,9.470743,-8.123810,-1.807985,5.189481,-5.299005,2.966075,7.126924,4.550368,-0.843221,8.694213,-6.497512,0.275547,-2.379686,-0.297688,0.882641,-4.664226,2.083897,-9.397150,-0.370620,-5.450769,-6.193927,8.951090,-5.617426,7.047154,6.501030,-0.522246,7.695924,-3.332435,3.968620,-4.905833,7.935543,9.258193,2.914239,-6.866382,8.959994,-4.984905,7.304205,-0.351948,0.039453,-4.536529,-5.369094,-2.109309,-8.546606,6.639853,9.793623,-6.200434,-5.252630,2.136818,8.801296,1.013758,-1.217284,0.049765,3.814472,-8.252551,8.040120,4.561971,0.228782,5.241003,-5.712581,6.917617,-8.769367,0.034571,4.603421,-9.364091,-7.497419,0.539023,-2.826872,-3.906062,-1.806510,-0.102542,7.930761,1.777509,0.134361,8.861203,-2.259383,9.839360,-6.545141,6.974108,-4.263480,3.430770,-3.668400,3.027095,0.668124,-6.340558,-3.631300,3.953537,1.821795,-1.793615,1.329643,-8.003058,-7.176765,-5.764202,-8.566871,-0.300835,7.842130,-2.979870,6.754744,-6.525000,8.721065,-5.516920,9.773638,-4.263834,5.183535,5.136173,-1.615942,-6.722036,-1.082526,4.669853,-7.803052,1.482292,9.077345,6.361153,5.418482,1.298370,1.948852,1.831128,0.494039,0.056471,-1.554301], dtype = "float32")#candidate|6186|(624,)|const|float32
const_6187 = relay.const([[-4.196720],[-2.592820],[6.848089],[6.018466],[1.371938],[0.878198],[-1.642480],[2.222646],[7.417587],[0.534799],[-3.653108],[0.633257],[4.225808],[3.986472],[-5.264487],[-9.447029],[-3.276678],[8.197232],[-0.215160],[-9.198325],[-0.635295],[7.039343],[4.552323],[-1.420511],[6.417322],[8.089592],[-5.518135],[-7.389598],[-7.790910],[1.178679],[5.297296],[6.036363],[-4.353374],[-4.359900],[5.972839],[-4.849183],[-9.496117],[6.905641],[1.506194],[-0.874063],[8.574614],[-8.471094],[-9.509273],[6.854518],[4.665688],[0.703597],[1.450664],[-8.420877],[-1.021688],[-3.494401],[7.315378],[9.398278],[-7.231738],[9.359653],[-6.676299],[-5.485402],[-3.289722],[5.971049],[-9.556886],[9.585985],[4.271263],[-3.339547],[2.668432],[9.969058],[2.115737],[-7.175188],[-2.701838],[2.762306],[-1.609180],[-1.648050],[-4.929260],[-8.701013],[-3.700874],[-1.963753],[-9.616531],[-2.069523],[-9.192782],[-8.385978],[0.073978],[5.165873],[-1.350934],[6.389954],[7.336369],[3.959464],[-5.544453],[-2.738391],[4.897129],[2.757290],[-1.603701],[-8.959369],[9.133342],[9.023007],[2.340549],[9.119873],[4.671211],[-0.114214],[-2.463622],[-5.780256],[-1.375992],[1.161439]], dtype = "float64")#candidate|6187|(100, 1)|const|float64
call_6185 = relay.TupleGetItem(func_3733_call(relay.reshape(const_6186.astype('float32'), [624,]), relay.reshape(const_6187.astype('float64'), [2, 10, 5]), ), 3)
call_6188 = relay.TupleGetItem(func_3736_call(relay.reshape(const_6186.astype('float32'), [624,]), relay.reshape(const_6187.astype('float64'), [2, 10, 5]), ), 3)
output = relay.Tuple([call_6156,call_6175,call_6181,call_6185,const_6186,const_6187,])
output2 = relay.Tuple([call_6157,call_6176,call_6182,call_6188,const_6186,const_6187,])
func_6204 = relay.Function([], output)
mod['func_6204'] = func_6204
mod = relay.transform.InferType()(mod)
mutated_mod['func_6204'] = func_6204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6204_call = mutated_mod.get_global_var('func_6204')
call_6205 = func_6204_call()
output = call_6205
func_6206 = relay.Function([], output)
mutated_mod['func_6206'] = func_6206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5406_call = mod.get_global_var('func_5406')
func_5408_call = mutated_mod.get_global_var('func_5408')
call_6233 = func_5406_call()
call_6234 = func_5406_call()
func_3947_call = mod.get_global_var('func_3947')
func_3948_call = mutated_mod.get_global_var('func_3948')
call_6245 = relay.TupleGetItem(func_3947_call(), 2)
call_6246 = relay.TupleGetItem(func_3948_call(), 2)
func_4052_call = mod.get_global_var('func_4052')
func_4055_call = mutated_mod.get_global_var('func_4055')
const_6262 = relay.const([9,-8,3,5,-1,-9,6,1,4,-2,6,-7,-4,8,2,-10,1,6,-3,6,-5,-4,-4,-4,6,7,1,-8,-7,-7,-2,-9,-6,-8,7,4,9,-2,6,-3,3,-6,-6,-9,1,-1,4,7,-7,2,1,6,7,4,6,-8,7,-3,-8,-5,10,-3,6,-8,-7,10,6,9,-6,7,-10,10,8,-10,8,9,-1,-4,-4,-3,3,-10,-9,-2,-2,6,-3,9,2,2,-7,7,5,9,4,-2,-5,-5,3,-1,6,7,4,5,-7,5,7,-4,-3,-2,4,3,-8,4,-6,6,-4,5,9,5,6,2,2,-6,10,4,-5,3,-7,-7,-4,7,6,-6,-10,10,1,-9,-9,-9,-6,5,2,-5,7,-10,-4,8,6,2,-5,4,-8,10,-10,8,-2,5,1,2,1,8,10,-3,10,-4,2,2,1,-9,10,4,10,-7,9,-6,3,6,-10,10,8,8,2,-2,-1,-1,-6,-5,6,7,3,-8,9,-10,6,-2,3,-6,7,7,7,-1,5,-1,-9,-8,2,-1,-1,2], dtype = "uint16")#candidate|6262|(210,)|const|uint16
call_6261 = relay.TupleGetItem(func_4052_call(relay.reshape(const_6262.astype('uint16'), [15, 1, 14])), 1)
call_6263 = relay.TupleGetItem(func_4055_call(relay.reshape(const_6262.astype('uint16'), [15, 1, 14])), 1)
output = relay.Tuple([call_6233,call_6245,call_6261,const_6262,])
output2 = relay.Tuple([call_6234,call_6246,call_6263,const_6262,])
func_6269 = relay.Function([], output)
mod['func_6269'] = func_6269
mod = relay.transform.InferType()(mod)
mutated_mod['func_6269'] = func_6269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6269_call = mutated_mod.get_global_var('func_6269')
call_6270 = func_6269_call()
output = call_6270
func_6271 = relay.Function([], output)
mutated_mod['func_6271'] = func_6271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4249_call = mod.get_global_var('func_4249')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_6306 = func_4249_call()
call_6307 = func_4249_call()
output = relay.Tuple([call_6306,])
output2 = relay.Tuple([call_6307,])
func_6308 = relay.Function([], output)
mod['func_6308'] = func_6308
mod = relay.transform.InferType()(mod)
mutated_mod['func_6308'] = func_6308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6308_call = mutated_mod.get_global_var('func_6308')
call_6309 = func_6308_call()
output = call_6309
func_6310 = relay.Function([], output)
mutated_mod['func_6310'] = func_6310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6327 = relay.var("var_6327", dtype = "float64", shape = (15, 6, 6))#candidate|6327|(15, 6, 6)|var|float64
uop_6328 = relay.cos(var_6327.astype('float64')) # shape=(15, 6, 6)
output = uop_6328
output2 = uop_6328
func_6346 = relay.Function([var_6327,], output)
mod['func_6346'] = func_6346
mod = relay.transform.InferType()(mod)
mutated_mod['func_6346'] = func_6346
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6347 = relay.var("var_6347", dtype = "float64", shape = (15, 6, 6))#candidate|6347|(15, 6, 6)|var|float64
func_6346_call = mutated_mod.get_global_var('func_6346')
call_6348 = func_6346_call(var_6347)
output = call_6348
func_6349 = relay.Function([var_6347], output)
mutated_mod['func_6349'] = func_6349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5600_call = mod.get_global_var('func_5600')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_6358 = func_5600_call()
call_6359 = func_5600_call()
var_6374 = relay.var("var_6374", dtype = "float64", shape = (110,))#candidate|6374|(110,)|var|float64
bop_6375 = relay.less_equal(call_6358.astype('bool'), relay.reshape(var_6374.astype('bool'), relay.shape_of(call_6358))) # shape=(110,)
bop_6378 = relay.less_equal(call_6359.astype('bool'), relay.reshape(var_6374.astype('bool'), relay.shape_of(call_6359))) # shape=(110,)
uop_6409 = relay.sqrt(bop_6375.astype('float32')) # shape=(110,)
uop_6411 = relay.sqrt(bop_6378.astype('float32')) # shape=(110,)
func_2565_call = mod.get_global_var('func_2565')
func_2569_call = mutated_mod.get_global_var('func_2569')
var_6420 = relay.var("var_6420", dtype = "int32", shape = (2197,))#candidate|6420|(2197,)|var|int32
const_6421 = relay.const([-4.075724,6.185127,0.305443,-4.092436,-3.836609,6.231761,-2.513786,-2.932181,6.629442,3.110877,2.744141,4.330581,7.339699,0.765361,0.208969,2.571005,2.773373,-3.758909,6.165397,1.603193,-9.731257,2.808928,5.037087,-5.581373,-8.991311,0.835983,1.291127,-4.292729], dtype = "float32")#candidate|6421|(28,)|const|float32
call_6419 = relay.TupleGetItem(func_2565_call(relay.reshape(var_6420.astype('int32'), [13, 13, 13]), relay.reshape(var_6420.astype('int32'), [13, 13, 13]), relay.reshape(const_6421.astype('float32'), [28,]), ), 2)
call_6422 = relay.TupleGetItem(func_2569_call(relay.reshape(var_6420.astype('int32'), [13, 13, 13]), relay.reshape(var_6420.astype('int32'), [13, 13, 13]), relay.reshape(const_6421.astype('float32'), [28,]), ), 2)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_6426 = relay.TupleGetItem(func_2526_call(), 0)
call_6427 = relay.TupleGetItem(func_2528_call(), 0)
func_6204_call = mod.get_global_var('func_6204')
func_6206_call = mutated_mod.get_global_var('func_6206')
call_6429 = relay.TupleGetItem(func_6204_call(), 2)
call_6430 = relay.TupleGetItem(func_6206_call(), 2)
output = relay.Tuple([uop_6409,call_6419,var_6420,const_6421,call_6426,call_6429,])
output2 = relay.Tuple([uop_6411,call_6422,var_6420,const_6421,call_6427,call_6430,])
func_6432 = relay.Function([var_6374,var_6420,], output)
mod['func_6432'] = func_6432
mod = relay.transform.InferType()(mod)
mutated_mod['func_6432'] = func_6432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6432_call = mutated_mod.get_global_var('func_6432')
var_6434 = relay.var("var_6434", dtype = "float64", shape = (110,))#candidate|6434|(110,)|var|float64
var_6435 = relay.var("var_6435", dtype = "int32", shape = (2197,))#candidate|6435|(2197,)|var|int32
call_6433 = func_6432_call(var_6434,var_6435,)
output = call_6433
func_6436 = relay.Function([var_6434,var_6435,], output)
mutated_mod['func_6436'] = func_6436
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6577 = relay.var("var_6577", dtype = "float32", shape = (3, 8, 5))#candidate|6577|(3, 8, 5)|var|float32
uop_6578 = relay.exp(var_6577.astype('float32')) # shape=(3, 8, 5)
output = relay.Tuple([uop_6578,])
output2 = relay.Tuple([uop_6578,])
func_6584 = relay.Function([var_6577,], output)
mod['func_6584'] = func_6584
mod = relay.transform.InferType()(mod)
var_6585 = relay.var("var_6585", dtype = "float32", shape = (3, 8, 5))#candidate|6585|(3, 8, 5)|var|float32
output = func_6584(var_6585)
func_6586 = relay.Function([var_6585], output)
mutated_mod['func_6586'] = func_6586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4021_call = mod.get_global_var('func_4021')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_6623 = relay.TupleGetItem(func_4021_call(), 0)
call_6624 = relay.TupleGetItem(func_4023_call(), 0)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_6626 = relay.TupleGetItem(func_3892_call(), 2)
call_6627 = relay.TupleGetItem(func_3894_call(), 2)
bop_6637 = relay.greater(call_6626.astype('bool'), relay.reshape(call_6623.astype('bool'), relay.shape_of(call_6626))) # shape=(1, 4, 7)
bop_6640 = relay.greater(call_6627.astype('bool'), relay.reshape(call_6624.astype('bool'), relay.shape_of(call_6627))) # shape=(1, 4, 7)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_6646 = relay.TupleGetItem(func_2945_call(), 1)
call_6647 = relay.TupleGetItem(func_2947_call(), 1)
func_4819_call = mod.get_global_var('func_4819')
func_4821_call = mutated_mod.get_global_var('func_4821')
call_6649 = relay.TupleGetItem(func_4819_call(), 1)
call_6650 = relay.TupleGetItem(func_4821_call(), 1)
output = relay.Tuple([bop_6637,call_6646,call_6649,])
output2 = relay.Tuple([bop_6640,call_6647,call_6650,])
func_6656 = relay.Function([], output)
mod['func_6656'] = func_6656
mod = relay.transform.InferType()(mod)
output = func_6656()
func_6657 = relay.Function([], output)
mutated_mod['func_6657'] = func_6657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6664 = relay.var("var_6664", dtype = "float32", shape = (11, 6, 9))#candidate|6664|(11, 6, 9)|var|float32
uop_6665 = relay.cosh(var_6664.astype('float32')) # shape=(11, 6, 9)
func_6269_call = mod.get_global_var('func_6269')
func_6271_call = mutated_mod.get_global_var('func_6271')
call_6669 = relay.TupleGetItem(func_6269_call(), 3)
call_6670 = relay.TupleGetItem(func_6271_call(), 3)
func_3639_call = mod.get_global_var('func_3639')
func_3641_call = mutated_mod.get_global_var('func_3641')
call_6682 = relay.TupleGetItem(func_3639_call(), 0)
call_6683 = relay.TupleGetItem(func_3641_call(), 0)
func_6432_call = mod.get_global_var('func_6432')
func_6436_call = mutated_mod.get_global_var('func_6436')
var_6685 = relay.var("var_6685", dtype = "int32", shape = (2197,))#candidate|6685|(2197,)|var|int32
call_6684 = relay.TupleGetItem(func_6432_call(relay.reshape(call_6682.astype('float64'), [110,]), relay.reshape(var_6685.astype('int32'), [2197,]), ), 1)
call_6686 = relay.TupleGetItem(func_6436_call(relay.reshape(call_6682.astype('float64'), [110,]), relay.reshape(var_6685.astype('int32'), [2197,]), ), 1)
func_4052_call = mod.get_global_var('func_4052')
func_4055_call = mutated_mod.get_global_var('func_4055')
call_6689 = relay.TupleGetItem(func_4052_call(relay.reshape(call_6669.astype('uint16'), [15, 1, 14])), 1)
call_6690 = relay.TupleGetItem(func_4055_call(relay.reshape(call_6669.astype('uint16'), [15, 1, 14])), 1)
func_3157_call = mod.get_global_var('func_3157')
func_3159_call = mutated_mod.get_global_var('func_3159')
call_6695 = relay.TupleGetItem(func_3157_call(), 0)
call_6696 = relay.TupleGetItem(func_3159_call(), 0)
func_4038_call = mod.get_global_var('func_4038')
func_4040_call = mutated_mod.get_global_var('func_4040')
var_6700 = relay.var("var_6700", dtype = "float64", shape = (100,))#candidate|6700|(100,)|var|float64
call_6699 = relay.TupleGetItem(func_4038_call(relay.reshape(var_6700.astype('float64'), [100,])), 1)
call_6701 = relay.TupleGetItem(func_4040_call(relay.reshape(var_6700.astype('float64'), [100,])), 1)
output = relay.Tuple([uop_6665,call_6669,call_6682,call_6684,var_6685,call_6689,call_6695,call_6699,var_6700,])
output2 = relay.Tuple([uop_6665,call_6670,call_6683,call_6686,var_6685,call_6690,call_6696,call_6701,var_6700,])
func_6713 = relay.Function([var_6664,var_6685,var_6700,], output)
mod['func_6713'] = func_6713
mod = relay.transform.InferType()(mod)
var_6714 = relay.var("var_6714", dtype = "float32", shape = (11, 6, 9))#candidate|6714|(11, 6, 9)|var|float32
var_6715 = relay.var("var_6715", dtype = "int32", shape = (2197,))#candidate|6715|(2197,)|var|int32
var_6716 = relay.var("var_6716", dtype = "float64", shape = (100,))#candidate|6716|(100,)|var|float64
output = func_6713(var_6714,var_6715,var_6716,)
func_6717 = relay.Function([var_6714,var_6715,var_6716,], output)
mutated_mod['func_6717'] = func_6717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4819_call = mod.get_global_var('func_4819')
func_4821_call = mutated_mod.get_global_var('func_4821')
call_6821 = relay.TupleGetItem(func_4819_call(), 1)
call_6822 = relay.TupleGetItem(func_4821_call(), 1)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_6828 = relay.TupleGetItem(func_4872_call(), 2)
call_6829 = relay.TupleGetItem(func_4873_call(), 2)
output = relay.Tuple([call_6821,call_6828,])
output2 = relay.Tuple([call_6822,call_6829,])
func_6830 = relay.Function([], output)
mod['func_6830'] = func_6830
mod = relay.transform.InferType()(mod)
output = func_6830()
func_6831 = relay.Function([], output)
mutated_mod['func_6831'] = func_6831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_6841 = relay.TupleGetItem(func_2920_call(), 0)
call_6842 = relay.TupleGetItem(func_2922_call(), 0)
func_4349_call = mod.get_global_var('func_4349')
func_4350_call = mutated_mod.get_global_var('func_4350')
call_6845 = func_4349_call()
call_6846 = func_4349_call()
output = relay.Tuple([call_6841,call_6845,])
output2 = relay.Tuple([call_6842,call_6846,])
func_6862 = relay.Function([], output)
mod['func_6862'] = func_6862
mod = relay.transform.InferType()(mod)
output = func_6862()
func_6863 = relay.Function([], output)
mutated_mod['func_6863'] = func_6863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6143_call = mod.get_global_var('func_6143')
func_6144_call = mutated_mod.get_global_var('func_6144')
call_6897 = func_6143_call()
call_6898 = func_6143_call()
output = relay.Tuple([call_6897,])
output2 = relay.Tuple([call_6898,])
func_6903 = relay.Function([], output)
mod['func_6903'] = func_6903
mod = relay.transform.InferType()(mod)
output = func_6903()
func_6904 = relay.Function([], output)
mutated_mod['func_6904'] = func_6904
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6948 = relay.var("var_6948", dtype = "float32", shape = (8, 7, 4))#candidate|6948|(8, 7, 4)|var|float32
uop_6949 = relay.erf(var_6948.astype('float32')) # shape=(8, 7, 4)
func_3023_call = mod.get_global_var('func_3023')
func_3025_call = mutated_mod.get_global_var('func_3025')
const_6958 = relay.const([-8.384927,8.776379,-3.823209,2.560580,2.206328,-6.662815,-0.752569,5.685412,8.182901,-8.399432,-7.740886,-7.905933,-8.281085,3.337908,8.009798,2.413012,9.832049,0.096426,8.194476,6.867376,-8.658001,5.182269,-1.966423,-4.680365,-8.602931,-1.418674,0.709116,-3.788273,-1.612769,-8.856391,-0.835079,-9.990069,-1.102317,0.194155,-8.456835,-1.258821,4.006720,0.401428,4.692679,5.686871,-7.713156,-2.152665,-9.579249,1.617382,-5.767227,-0.217428,6.546042,-0.154040,-5.285455,8.923944,-7.576708,-4.163378,-0.401486,4.853506,2.707120,8.159908,3.543744,6.409877,-0.688324,-9.896957,-6.595704,6.255163,7.554973,-3.515422,-6.325581,0.772723,7.382516,-2.243474,1.604169,1.633510,-7.721978,4.915400,-5.195431,8.307143,2.608971,9.736421,-8.107676,-3.797379,-2.156611,4.973510,-2.988411,-8.907192,-8.665293,3.488074,-5.556091,-8.311063,4.954018,-0.155467,2.536676,3.511648,-5.274230,-3.760036,1.978986,-9.348980,4.352118,-3.895580,-5.015058,-6.403431,1.483886,4.113602,-5.430407,-9.763295,0.698594,-1.502969,-7.290550,2.677088,-4.205498,0.173131,-3.716956,-4.174104], dtype = "float64")#candidate|6958|(110,)|const|float64
call_6957 = relay.TupleGetItem(func_3023_call(relay.reshape(const_6958.astype('float64'), [110,])), 0)
call_6959 = relay.TupleGetItem(func_3025_call(relay.reshape(const_6958.astype('float64'), [110,])), 0)
func_5455_call = mod.get_global_var('func_5455')
func_5456_call = mutated_mod.get_global_var('func_5456')
call_6960 = relay.TupleGetItem(func_5455_call(), 0)
call_6961 = relay.TupleGetItem(func_5456_call(), 0)
uop_6962 = relay.sqrt(call_6957.astype('float32')) # shape=(1, 4, 7)
uop_6964 = relay.sqrt(call_6959.astype('float32')) # shape=(1, 4, 7)
func_5744_call = mod.get_global_var('func_5744')
func_5748_call = mutated_mod.get_global_var('func_5748')
const_6988 = relay.const([6,1,5,8,9,3,1,-9,-1,-7,7,2,6,-8,8,-3,7,-4,-7,4,-4,8,-4,-4,-9,-9,-10,10,1,-2,-1,-3,8,-1,-10,2,1,1,-9,2,5,-6,10,-10,4,-2,-8,3,4,2,-8,10,-6,-3,-8,-3,-6,-8,7,-9,-2,7,-8,6,4,-10,4,-10,-2,5,9,5,-9,2,-2,6,-4,6,3,7,-1,10,6,-6,-2,-10,-1,6,7,5,-1,-5,-5,-10,-2,6,4,9,-3,-10,-5,7,3,-7,1,10,-4,8,6,10,5,-3,1,8,-6,10,-7,9,-2,2,10,-5,9,-6,1,4,1,4,-9,5,-1,7,3,9,4,-9,5,9,-9,-10,-10,-6,-10,-10,-3,4,-1,1,9,-9,3,-7,2,-2,-10,3,5,-10,10,-5,6,-6,-2,-9,6,4,-6,8,7,-10,10,-9,-3,-1,-9,-5,-6,2,-7,-9,-8,4,5,1,10,3,5,5,10,-2,-2,6,9,8,-8,10,-1,10,-4,2,-2,-6,-6,8,6,-7,-6,-8,10,2,-4,-3,-5,-3,-4,7,-1,-5,-1,-4,-3,-7,5,-6,1,2,8,-10,-8,6,-1,10,-3,8,-7,4,3,-1,-7,3,4,-5,5,-9,-2,5,-7,5,9,5,6,-8,-3,7,-5,-9,-10,-3,-2,7,7,-7,-8,-4,4,5,-1,10,1,3,10,6,8,4,-2,-4,-5,-3,3,-10,-9,8,-7,5,6,3,-1,7,-8,9,-3,9,6,-1,-1,10,5,1,8,7,5,-1,6,-4,-8,4,-10,9,7,6,8,-8,-6,4,-7,8,-8,-6,5,-1,-7,-6,8,-2,5,2,6,8,-1,3,-3,9,10,-8,-9,9,3,-2,3,5,2,3,7,7,4,-5,-3,-8,4,-9,6,9,-5,10,5,-6,-3,4,-10,8,-2,-3,-9,-9,9,-6,-6,-4,-7,9,-10,-8,3,10,4,-1,3,3,-5,9,-8,10,-1,5,9,-10,8,-9,-2,6,1,2,9,9,8,9,2,-10,-4,-3,-8,1,2,6,-2,-10,8,-8,7,-3,3,1,-3,-10,-7,-1,5,2,3,1,-10,8,-3,5,4,-5,1,-4,-10,-1,-9,-3,-4,4,-4,-3,-8,-2,-7,-2,-6,10,6,2,-2,2,-5,6,1,5,4,10,8,4,-1,-8,5,6,6,5,1,7,-2,3,10,-9,-5,8,-10,-9,-9,8,7,-3,-2,-8,8,6,8,-5,7,-5,-2,-6,-5,3,-1,6,-5,-10,-1,-7,-4,9,4,2,-8,4,10,-2,4,-9,-6,-3,-5,-5,1,-5,9,-9,-8,4,8,7,7,-2,-3,-6,-5,-10,-3,-7,9,1,8,10,-1,-3,2,4,9,2,7,1,-10,4,-5,10,-5,-1,1,8,-6,10,2,9,1,3,1,2,6,5,-9,7,-5,6,2,9,-8,7,-2,1,-8,-1,-10,-10,-9,8,-7,-3,-3,-10,6,2,6,-3,-6,10,-9,-2,-4,-3,-7,-2,-4,-9,-5,-2,6,-4,-5,-3,-9,4,-5,-7,1,3,-9,-2,-1,1,-10,6,9,10,-7,5,-7,-6,-5,3,-2,-4,3,-5,-9,-10,-9,6,-8,-4,-1,-3,-5,-1,3,-8,2,4,-2,-8,5,-9,-8,-4,3,-3,4,3,6,-4,9,2,6,5,-6,8,-2,-6,1,-7,8,9,6,3,-5,1,-9,-5,10,2,2,-7,-8,-7,5,-5,5,-4,3,5,4,-4,-8,9,-7,-3,-2,7,3,9,1,-8,-8,-9,10,1,-9,-9,3,6,1,-1,8,-5,4,-9,-9,-3,-1,-8,-8,7,5,6,-5,8,-2,1,8,2,-9,9,10,-5,-4,-4,-3,2,8,-5,-10,1,3,1,7,5,4,5,6,7,-4,-4,5,-6,4,7,8,6,-1,5,10,-7,-6,2,-4,-5,3,7,5,-10,7,-3,-7,-6,-5,10,3,-2,10,4,-5,4,8,4,7,10,-5,-8,-9,-3,-7,2,10,10,7,6,1,-10,3,10,-9,-3,3,-7,6,-1,-2,-3,-6,-2,5,7,-10,-4,-10,-3,9,5,7,-6,-1,6,-9,-6,1,8,-8,3,9,-10,-6,-9,-7,6,-6,7,-9,-3,-3,3,-8,2,-3,3,4,4,4,-4,-10,5,3,5,6,-10,6,-4,4,10,1,-3,5,-7,-1,-10,-9,8,8,6,9,4,1,10,4,-5,1,1,5,5,-1,8,-1,-4,10,-4,5,-4,5,-2,-2,-5,-6,1,6,-9,2,-9,-6,3,-10,-2,-4,-3,-10,10,-3,7,1,1,5,-6,-9,-9,5,-10,-8,2,-1,-2,10,-5,7,4,-3,9,7,2,-10,3,-2,2,7,3,-1,-1,7,5,9,3,-4,-9,-8,7,3,-3,2,8,-1,7,5,2,3,7,-5,-5,3,-10,-8,-8,8,7,-9,1,-5,-10,6,2,9,5,-10,-5,-6,-5,-1,-5,-6,-8,9,-5,-8,5,-8,5,-6,5,3,-2,-4,-3,-2,3,3,5,3,-6,-6,6,8,3,-4,-4,8,-5,-3,-5,-9,6,-4,-5,10,7,-4,10,-4,10,3,4,7,2,-10,-6,-7,-2,-3,7,10,-9,-7,-8,6,-9,-9,-8,4,8,-7,4,9,5,1,-5,-6,-5,7,-3,1,-10,7,-9,-8,-7,-3,8,-5,4,-5,-8,7,-1,9,7,-8,-2,-7,-7,10,-9,-5,7,-10,-9,-1,-7,2,-3,3,-3,-9,5,-10,10,-6,-4,-5,-2,-3,-1,8,3,5,-3,7,7,-2,1,-5,-3,9,-2,2,1,-5,-8,-8,2,-8,-2,-2,-1,1,8,5,7,-3,-10,6,-8,2,3,8,3,-2,-1,4,-9,-5,3,10,-4,2,8,5,-7,4,7,9,10,-7,-6,-4,-7,3,7,-9,-8,6,7,2,8,-7,-7,-7,8,9,-6,-10,-10,-1,8,-1,-3,2,8,-5,9,-1,8,7,-3,-1,-7,-10,-8,5,2,-4,-3,-4,-10,7,-1,-10,-6,7,1,-6,3,-7,-8,-6,-10,-5,9,-6,-8,-10,9,10,-7,5,-6,-10,9,-9,4,7,-8,-9,-2,5,7,-3,-7,4,-1,-6,1,8,-5,-5,6,3,4,2,6,-10,-5,9,-5,8,1,-4,1,-2,-1,-5,9,-1,-1,-3,-10,-10,-5,9,-4,-9,-2,-9,7,1,-8,-4,-8,2,-10,6,7,7,5,-5,2,5,-4,-8,4,8,-8,9,-1,-5,7,3,7,9,5,-2,5,-2,10,2,1,-7,6,7,8,-8,-3,-2,-10,-4,-4,-3,-4,10,7,9,3,9,4,5,-9,-9,-4,3,-4,9,3,-7,-7,2,-8,-3,9,-10,-9,-4,-8,9,8,5,10,9,6,-2,-6,8,-7,5,-3,8,-10,8,-7,-9,2,-6,8,8,5,8,8,5,6,-3,7,-3,-6,-4,-10,8,8,6,1,-1,-8,6,-4,-1,-3,1,8,6,5,-6,4,8,-8,-10,-10,5,-8,2,-4,-2,9,-6,5,10,-1,-6,-10,8,9,-9,7,-7,-7,-8,-5,-9,-4,-1,6,-1,-8,3,-1,8,-9,1,10,-2,8,-1,10,7,-4,5,2,8,-2,9,-4,-5,3,10,3,-2,3,6,-3,7,3,-9,7,6,10,7,2,6,8,-1,-9,-6,6,6,-4,9,5,4,-7,3,8,1,2,7,7,-4,3,-9,-1,10,-7,5,-9,4,-1,-3,-9,-1,4,-2,10,-7,4,-1,10,2,-2,-9,-6,-7,2,-8,-4,1,-10,9,8,10,2,7,-7,-1,-6,10,-7,-2,6,-1,10,-8,-4,-8,-1,-6,-4,-6,4,1,-2,-3,-9,6,-5,-6,9,-5,1,9,6,6,8,2,-3,-1,4,-2,9,8,6,-8,8,-2,-7,-10,4,-2,9,-4,6,7,-1,5,-6,-3,7,-9,-3,3,-10,2,10,-6,-9,-3,-10,-7,9,1,4,-8,-3,5,8,7,-2,1,4,-3,2,8,-6,10,-4,1,-5,9,7,-6,-4,2,2,8,-3,-9,-6,-6,1,-8,-9,2,-9,1,-7,-1,-2], dtype = "int64")#candidate|6988|(1568,)|const|int64
call_6987 = func_5744_call(relay.reshape(const_6988.astype('int64'), [7, 14, 16]), relay.reshape(const_6988.astype('int64'), [7, 14, 16]), )
call_6989 = func_5744_call(relay.reshape(const_6988.astype('int64'), [7, 14, 16]), relay.reshape(const_6988.astype('int64'), [7, 14, 16]), )
func_4021_call = mod.get_global_var('func_4021')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_7004 = relay.TupleGetItem(func_4021_call(), 1)
call_7005 = relay.TupleGetItem(func_4023_call(), 1)
func_2539_call = mod.get_global_var('func_2539')
func_2542_call = mutated_mod.get_global_var('func_2542')
const_7014 = relay.const([3.293037,-5.260074,2.827482,7.994144,-3.270791,-8.598090,-5.303845,-8.119480,-7.754545,-1.853540,-1.544267,-0.198223,5.773825,0.460412,2.940360,6.572083,3.184565,0.752279,-6.154133,-9.866608,-0.816455,-9.456671,2.003662,-7.840722,5.181285,7.822322,-1.485701,-7.806869,-6.671696,-5.652543,-0.966222,-7.764725,8.015923,-7.198556,-0.199793,7.205748,7.758755,-8.507156,-0.499387,-7.616356,5.448084,1.421426,-1.843393,-6.905817,9.972118,-3.378692,-0.540839,0.818842,-9.813772,0.269228,-3.460302,0.873022,-1.762505,4.622283,-0.756223,-1.281857,5.392723,7.273216,1.502308,-2.917841,8.568943,-3.959279,6.277804,9.956933,9.479442,0.693877,6.896290,1.018885,-8.570448,-6.464918,6.886623,-4.157090,-2.548507,-4.590647,0.220022,-4.994394,1.404826,4.326798,-2.589423,-4.779021,8.395599,-7.342001,-5.314088,7.528450,-2.226021,5.256183,-9.454215,-5.074694,1.869624,4.936711,1.683192,3.119576,-0.605487,5.550621,-4.030851,3.027702,7.677773,-5.685003,9.220505,-8.018051], dtype = "float64")#candidate|7014|(100,)|const|float64
call_7013 = func_2539_call(relay.reshape(const_7014.astype('float64'), [2, 10, 5]), relay.reshape(const_7014.astype('float64'), [2, 10, 5]), )
call_7015 = func_2539_call(relay.reshape(const_7014.astype('float64'), [2, 10, 5]), relay.reshape(const_7014.astype('float64'), [2, 10, 5]), )
var_7032 = relay.var("var_7032", dtype = "float32", shape = (2, 4, 7))#candidate|7032|(2, 4, 7)|var|float32
bop_7033 = relay.add(uop_6962.astype('uint64'), var_7032.astype('uint64')) # shape=(2, 4, 7)
bop_7036 = relay.add(uop_6964.astype('uint64'), var_7032.astype('uint64')) # shape=(2, 4, 7)
output = relay.Tuple([uop_6949,const_6958,call_6960,call_6987,const_6988,call_7004,call_7013,const_7014,bop_7033,])
output2 = relay.Tuple([uop_6949,const_6958,call_6961,call_6989,const_6988,call_7005,call_7015,const_7014,bop_7036,])
func_7044 = relay.Function([var_6948,var_7032,], output)
mod['func_7044'] = func_7044
mod = relay.transform.InferType()(mod)
mutated_mod['func_7044'] = func_7044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7044_call = mutated_mod.get_global_var('func_7044')
var_7046 = relay.var("var_7046", dtype = "float32", shape = (8, 7, 4))#candidate|7046|(8, 7, 4)|var|float32
var_7047 = relay.var("var_7047", dtype = "float32", shape = (2, 4, 7))#candidate|7047|(2, 4, 7)|var|float32
call_7045 = func_7044_call(var_7046,var_7047,)
output = call_7045
func_7048 = relay.Function([var_7046,var_7047,], output)
mutated_mod['func_7048'] = func_7048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7109 = relay.var("var_7109", dtype = "float32", shape = (10, 6, 4))#candidate|7109|(10, 6, 4)|var|float32
const_7110 = relay.const([[[7.142687,7.139444,3.766929,-3.246003],[8.402391,9.485793,-0.878879,5.282166],[8.516234,-8.164237,4.100825,-0.915572],[0.687115,-8.764414,-0.842624,-0.616376],[3.671140,4.939467,6.956288,3.219060],[-2.079243,1.475140,2.620915,-0.563920]],[[8.414733,-9.963909,9.291822,-3.473203],[4.960320,-1.976846,-3.189894,7.651338],[-7.983350,-7.320048,-9.850246,-0.253792],[-6.856889,6.235270,-1.423651,-7.409002],[1.808465,6.044929,7.356208,9.920998],[-8.341820,-0.424320,-7.474683,-5.503034]],[[-5.956139,-6.777328,4.892193,3.428130],[3.888289,6.817951,8.555223,6.261358],[-3.369051,4.141777,-6.082546,-4.795992],[3.893439,3.925274,5.028344,-8.274128],[-2.932498,-0.154984,-2.964460,8.189128],[6.949047,6.920423,-6.206751,4.896916]],[[9.218009,4.780440,6.552418,-2.769020],[-3.127731,-0.705763,-0.784925,-8.091260],[-9.638244,-8.189862,-7.585887,-2.359540],[-4.269399,-3.568548,-5.221273,2.547940],[1.665836,5.160654,-3.935646,3.444100],[1.985598,-5.292127,-0.258844,-3.636688]],[[-6.919374,4.591863,-2.795439,-4.294345],[-4.397224,8.056444,-3.657817,-3.503133],[4.178844,-2.425617,-5.897669,9.327793],[5.034858,0.740171,-9.468521,-0.586231],[-3.114418,6.682593,9.287763,9.772363],[5.414404,-2.983940,7.928080,7.057622]],[[-7.724075,-1.478074,7.259919,-0.836338],[-4.970497,-2.140027,4.245397,4.356496],[8.629149,-4.743020,-2.700167,-7.029458],[5.746368,0.556411,7.013045,9.199494],[-3.653503,-4.007114,5.703180,-9.627981],[-0.198863,-1.965465,-4.641533,3.124054]],[[1.692709,-5.425231,8.079218,6.475433],[-9.737539,6.478433,5.174973,0.828857],[8.379454,1.498660,9.949040,-3.280835],[-7.461611,1.469411,-5.245219,-7.692542],[3.616507,2.506538,9.639425,2.057455],[4.675984,-4.307432,2.047921,-9.301928]],[[5.599530,-4.053805,1.024558,9.592392],[0.329488,-3.048984,4.622133,8.168463],[-0.159383,-9.637488,2.060293,5.910474],[-4.334595,4.170868,3.983627,-5.437573],[7.965411,5.040714,3.721247,8.692261],[-3.058635,-2.295892,-3.318294,-0.037943]],[[-1.706018,2.491967,-3.331164,-9.700680],[-8.471120,-6.926811,1.480650,-6.627767],[7.015626,-4.609453,-8.463805,-6.629955],[8.578876,5.186748,-4.529965,-3.051014],[-6.230892,8.146198,-7.725136,6.958805],[2.705490,4.660339,2.499130,-1.496617]],[[7.776472,4.492708,-2.257024,-1.349914],[5.012076,6.685145,0.132068,-6.505485],[7.205940,-5.139429,-2.400707,-0.847712],[-6.870132,-5.681031,-1.095288,-8.519472],[7.349095,6.324156,9.243178,-1.064031],[3.649723,0.086766,8.434656,-2.092580]]], dtype = "float32")#candidate|7110|(10, 6, 4)|const|float32
bop_7111 = relay.power(var_7109.astype('float32'), relay.reshape(const_7110.astype('float32'), relay.shape_of(var_7109))) # shape=(10, 6, 4)
func_6269_call = mod.get_global_var('func_6269')
func_6271_call = mutated_mod.get_global_var('func_6271')
call_7122 = relay.TupleGetItem(func_6269_call(), 3)
call_7123 = relay.TupleGetItem(func_6271_call(), 3)
output = relay.Tuple([bop_7111,call_7122,])
output2 = relay.Tuple([bop_7111,call_7123,])
func_7126 = relay.Function([var_7109,], output)
mod['func_7126'] = func_7126
mod = relay.transform.InferType()(mod)
mutated_mod['func_7126'] = func_7126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7127 = relay.var("var_7127", dtype = "float32", shape = (10, 6, 4))#candidate|7127|(10, 6, 4)|var|float32
func_7126_call = mutated_mod.get_global_var('func_7126')
call_7128 = func_7126_call(var_7127)
output = call_7128
func_7129 = relay.Function([var_7127], output)
mutated_mod['func_7129'] = func_7129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_7160 = func_3544_call()
call_7161 = func_3544_call()
output = call_7160
output2 = call_7161
func_7162 = relay.Function([], output)
mod['func_7162'] = func_7162
mod = relay.transform.InferType()(mod)
output = func_7162()
func_7163 = relay.Function([], output)
mutated_mod['func_7163'] = func_7163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5612_call = mod.get_global_var('func_5612')
func_5614_call = mutated_mod.get_global_var('func_5614')
call_7164 = relay.TupleGetItem(func_5612_call(), 0)
call_7165 = relay.TupleGetItem(func_5614_call(), 0)
func_5455_call = mod.get_global_var('func_5455')
func_5456_call = mutated_mod.get_global_var('func_5456')
call_7169 = relay.TupleGetItem(func_5455_call(), 0)
call_7170 = relay.TupleGetItem(func_5456_call(), 0)
func_5024_call = mod.get_global_var('func_5024')
func_5027_call = mutated_mod.get_global_var('func_5027')
call_7171 = relay.TupleGetItem(func_5024_call(relay.reshape(call_7169.astype('float32'), [1, 4, 7])), 2)
call_7172 = relay.TupleGetItem(func_5027_call(relay.reshape(call_7169.astype('float32'), [1, 4, 7])), 2)
uop_7181 = relay.tan(call_7164.astype('float64')) # shape=(22, 5)
uop_7183 = relay.tan(call_7165.astype('float64')) # shape=(22, 5)
output = relay.Tuple([call_7169,call_7171,uop_7181,])
output2 = relay.Tuple([call_7170,call_7172,uop_7183,])
func_7204 = relay.Function([], output)
mod['func_7204'] = func_7204
mod = relay.transform.InferType()(mod)
mutated_mod['func_7204'] = func_7204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7204_call = mutated_mod.get_global_var('func_7204')
call_7205 = func_7204_call()
output = call_7205
func_7206 = relay.Function([], output)
mutated_mod['func_7206'] = func_7206
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7281 = relay.const([[[2.208240,8.729426,7.029382,0.253385,-7.122629,2.293570,-3.663225,3.939947,-6.718115,-5.032525,9.366494,9.546789,6.951370,4.675871,5.172348],[9.812057,0.630354,-9.400383,-7.320535,6.673760,-4.107035,-4.510382,0.424074,-1.311764,-5.988394,8.342365,6.638160,-9.061246,-2.233791,9.161194]],[[0.071083,6.367810,8.446752,8.100621,2.510682,-8.627178,4.727576,-7.215853,-4.241140,-0.119508,-6.439676,-0.766393,5.505947,-9.976765,-9.471518],[9.733903,-9.296712,2.321155,-4.247117,9.695757,0.580247,9.179741,5.345857,2.049540,-8.614819,-7.265192,7.198856,-6.441823,-6.033745,2.989769]],[[-8.264956,-7.255202,5.829293,-3.291648,-6.269687,9.027329,6.957857,-1.342773,4.231474,4.088239,9.277967,-0.425397,-7.209451,6.212952,8.167492],[-1.618275,3.624138,-8.132458,-1.262609,-3.979824,8.178758,-3.256721,-8.477546,5.524827,-8.942169,7.650463,-7.219893,-1.401191,-9.848260,8.338666]]], dtype = "float64")#candidate|7281|(3, 2, 15)|const|float64
uop_7282 = relay.log10(const_7281.astype('float64')) # shape=(3, 2, 15)
uop_7288 = relay.log(uop_7282.astype('float32')) # shape=(3, 2, 15)
uop_7291 = relay.acosh(const_7281.astype('float64')) # shape=(3, 2, 15)
output = relay.Tuple([uop_7288,uop_7291,])
output2 = relay.Tuple([uop_7288,uop_7291,])
func_7307 = relay.Function([], output)
mod['func_7307'] = func_7307
mod = relay.transform.InferType()(mod)
mutated_mod['func_7307'] = func_7307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7307_call = mutated_mod.get_global_var('func_7307')
call_7308 = func_7307_call()
output = call_7308
func_7309 = relay.Function([], output)
mutated_mod['func_7309'] = func_7309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_7317 = relay.TupleGetItem(func_4792_call(), 0)
call_7318 = relay.TupleGetItem(func_4793_call(), 0)
func_4168_call = mod.get_global_var('func_4168')
func_4170_call = mutated_mod.get_global_var('func_4170')
const_7323 = relay.const(3.687397, dtype = "float32")#candidate|7323|()|const|float32
call_7322 = relay.TupleGetItem(func_4168_call(relay.reshape(const_7323.astype('float32'), [])), 7)
call_7324 = relay.TupleGetItem(func_4170_call(relay.reshape(const_7323.astype('float32'), [])), 7)
func_3947_call = mod.get_global_var('func_3947')
func_3948_call = mutated_mod.get_global_var('func_3948')
call_7335 = relay.TupleGetItem(func_3947_call(), 1)
call_7336 = relay.TupleGetItem(func_3948_call(), 1)
output = relay.Tuple([call_7317,call_7322,const_7323,call_7335,])
output2 = relay.Tuple([call_7318,call_7324,const_7323,call_7336,])
func_7341 = relay.Function([], output)
mod['func_7341'] = func_7341
mod = relay.transform.InferType()(mod)
mutated_mod['func_7341'] = func_7341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7341_call = mutated_mod.get_global_var('func_7341')
call_7342 = func_7341_call()
output = call_7342
func_7343 = relay.Function([], output)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_7379 = relay.TupleGetItem(func_3892_call(), 2)
call_7380 = relay.TupleGetItem(func_3894_call(), 2)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_7381 = func_5171_call()
call_7382 = func_5171_call()
func_5733_call = mod.get_global_var('func_5733')
func_5734_call = mutated_mod.get_global_var('func_5734')
call_7384 = func_5733_call()
call_7385 = func_5733_call()
func_5744_call = mod.get_global_var('func_5744')
func_5748_call = mutated_mod.get_global_var('func_5748')
var_7406 = relay.var("var_7406", dtype = "int64", shape = (1568,))#candidate|7406|(1568,)|var|int64
call_7405 = func_5744_call(relay.reshape(var_7406.astype('int64'), [7, 14, 16]), relay.reshape(var_7406.astype('int64'), [7, 14, 16]), )
call_7407 = func_5744_call(relay.reshape(var_7406.astype('int64'), [7, 14, 16]), relay.reshape(var_7406.astype('int64'), [7, 14, 16]), )
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_7422 = relay.TupleGetItem(func_4792_call(), 0)
call_7423 = relay.TupleGetItem(func_4793_call(), 0)
output = relay.Tuple([call_7379,call_7381,call_7384,call_7405,var_7406,call_7422,])
output2 = relay.Tuple([call_7380,call_7382,call_7385,call_7407,var_7406,call_7423,])
func_7430 = relay.Function([var_7406,], output)
mod['func_7430'] = func_7430
mod = relay.transform.InferType()(mod)
var_7431 = relay.var("var_7431", dtype = "int64", shape = (1568,))#candidate|7431|(1568,)|var|int64
output = func_7430(var_7431)
func_7432 = relay.Function([var_7431], output)
mutated_mod['func_7432'] = func_7432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6269_call = mod.get_global_var('func_6269')
func_6271_call = mutated_mod.get_global_var('func_6271')
call_7461 = relay.TupleGetItem(func_6269_call(), 2)
call_7462 = relay.TupleGetItem(func_6271_call(), 2)
output = relay.Tuple([call_7461,])
output2 = relay.Tuple([call_7462,])
func_7467 = relay.Function([], output)
mod['func_7467'] = func_7467
mod = relay.transform.InferType()(mod)
mutated_mod['func_7467'] = func_7467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7467_call = mutated_mod.get_global_var('func_7467')
call_7468 = func_7467_call()
output = call_7468
func_7469 = relay.Function([], output)
mutated_mod['func_7469'] = func_7469
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7498 = relay.var("var_7498", dtype = "float64", shape = (9, 15, 11))#candidate|7498|(9, 15, 11)|var|float64
const_7499 = relay.const([[[6.445400,-9.598553,8.462983,-8.157368,-1.379869,0.049905,-8.948852,7.267443,5.168847,2.840973,-1.862055],[-1.654623,-1.028202,8.058784,-2.663802,0.241143,0.919973,-6.330005,-5.039916,-3.660712,2.768068,-9.148255],[-0.622575,-6.660732,0.739064,4.868052,-5.090658,8.899266,4.164807,3.891090,-8.898353,-8.458378,-4.828689],[-7.101484,8.422784,2.370241,-3.446970,-4.764709,7.364691,-0.168779,5.598009,-8.632012,-0.754113,-2.176362],[-7.787637,7.716356,-3.842814,-6.120656,-9.625487,3.336426,9.511745,6.945631,5.656049,3.112924,-9.105762],[1.920718,7.316608,-5.290752,5.787802,-5.124146,-1.972635,-9.542558,2.856572,4.369065,1.584810,7.939758],[7.285273,-2.639495,-5.987645,7.006847,-8.957241,-0.564178,-1.301795,9.881461,5.905878,0.351096,5.665624],[6.511324,-3.456760,-9.904708,9.025985,8.257361,-7.558881,8.161883,9.438751,-8.972278,7.981380,2.419058],[7.106604,-5.503491,-3.444776,-6.320998,2.264619,-2.733987,-1.719144,-6.685035,-7.752536,-7.132154,5.857946],[-5.564442,-8.503453,-8.479522,2.702076,9.070817,-7.292576,-2.858003,2.763637,-4.562472,-5.427674,-2.459995],[-6.121713,-9.874671,-5.251678,3.173894,9.818571,-3.571606,-1.937175,9.329419,9.951785,-2.535099,-3.347380],[-7.278944,4.671976,0.768522,-0.308570,-0.526778,-3.732521,2.711135,5.166579,-5.367415,-7.395732,-1.160685],[-8.070623,4.246682,-5.386336,9.991642,-2.568132,-7.495879,2.665358,8.345016,-6.400497,-3.037382,-5.402375],[4.815677,-0.999730,-8.882634,5.275312,-8.898540,1.604382,4.532674,5.430980,-0.880039,-3.158210,-6.480200],[-2.126496,8.581604,2.347298,3.082637,-9.022695,-9.276480,6.488617,0.188442,0.389271,-9.542952,4.542176]],[[8.827481,-4.281597,-5.569678,-7.410591,-8.055018,-9.389806,3.451179,1.329135,-3.229110,-7.734930,3.055274],[1.023328,-3.835788,-5.246461,4.389094,-9.249075,-3.691453,6.489470,7.569806,0.008281,-8.518660,-3.762088],[-6.744607,2.076503,7.116429,9.475026,3.984426,2.716915,4.936466,-2.988189,-2.801618,1.157521,6.980097],[1.296577,6.941449,2.375199,4.163351,8.493073,4.818573,-5.035732,-6.637405,5.973023,-0.969911,8.603793],[-5.753787,7.036396,-9.347982,-5.106288,8.048923,7.384324,-2.373828,-4.720477,-8.589362,2.989227,-1.503382],[-1.052826,2.276802,-7.335275,-0.588183,-3.627967,9.143088,2.467760,-3.614115,-6.017327,-3.206753,-5.011513],[-6.307198,-4.097599,3.751168,-0.288958,9.369284,-5.086903,0.314297,-9.756813,6.688645,-1.360098,-9.351470],[-6.959545,1.378430,-6.571188,-7.975938,9.176170,-4.355783,3.513228,4.548848,4.299767,-7.308887,-7.583246],[3.860838,-4.294858,5.896607,3.808414,-1.058094,-9.423634,-4.783411,2.328312,-1.267413,9.630336,-1.309371],[-0.119606,4.890712,-5.597450,9.722224,0.572563,-6.749302,2.426555,-4.230161,5.057042,5.865271,2.522057],[6.292844,-9.772237,9.683295,-4.260085,9.870408,0.510164,-6.025135,-7.363659,-8.341897,-8.133657,0.148031],[-7.944145,5.261279,0.753303,-4.486939,-4.388791,9.121233,2.205124,6.603314,0.801355,-2.843638,4.738209],[-6.953489,-8.239865,9.830690,7.802521,8.560134,-6.979624,-9.304297,0.230978,-7.780334,-5.161002,-2.292327],[-9.916038,6.425124,-3.021835,2.240886,-5.252311,-3.909817,-4.021300,-4.838256,-2.681942,-0.590967,-9.018475],[-0.709260,6.252963,9.045268,2.093100,1.112331,9.423320,3.318347,-2.171838,0.686843,-0.991962,7.714204]],[[9.609310,6.153772,4.763926,9.201629,-8.137157,6.382037,-0.080086,0.455463,1.056643,-9.584070,3.078981],[-3.194619,-6.149090,-0.979180,5.805033,6.801545,7.288501,8.716187,-8.798339,-3.016725,-4.685152,-3.444829],[8.740823,-8.270246,-6.902916,4.233603,-6.216399,6.591105,-2.169417,-4.388568,-9.007288,-5.999139,-7.640415],[-7.745179,-1.392602,2.319346,1.436139,-7.843745,1.343328,5.033909,3.224149,4.911114,-7.861595,-0.680102],[-7.524691,6.705810,-2.279000,4.992210,5.814782,-9.479751,-0.883817,-4.848076,1.637558,-1.816931,-8.153257],[1.281239,2.360281,7.154806,1.883618,-5.663412,-2.811487,-9.293435,2.930032,8.175409,-2.937475,1.338345],[4.208218,-2.773086,-6.481305,9.525133,-9.385969,-0.901856,7.136942,0.964469,0.776305,8.467288,6.099313],[-2.648746,4.647462,8.289025,5.541350,-3.866262,6.696767,-0.279241,-2.352313,-7.839886,-7.811772,-8.589498],[-8.001762,-4.969353,2.119323,-7.408557,-5.064442,1.273984,-5.070490,6.857113,7.572057,7.325276,-1.461490],[-7.179408,6.263735,2.933273,9.236846,-5.441657,1.346171,8.392904,-9.289992,-3.825510,2.519583,-5.563369],[-4.621732,4.432798,3.383214,-6.569382,-7.565573,-6.745123,9.667301,5.496467,5.015666,5.427996,2.158714],[0.096427,-7.821718,-7.705933,-8.252457,3.317054,-3.036662,-5.356173,4.260741,1.992180,-0.966504,-3.067455],[6.125306,-8.653884,4.552737,5.294151,4.610272,-8.920362,-4.912855,6.648038,8.055927,-5.720917,6.698841],[8.211038,9.020446,1.002959,3.267421,-1.081534,1.235284,7.910591,-6.556066,4.411387,-6.959864,7.283007],[-8.116104,7.180980,3.509838,1.669842,-1.163500,-5.895253,8.183040,5.467859,7.385677,7.028284,9.518046]],[[8.213893,-4.966150,1.065419,-8.801342,1.017592,1.779323,-0.689677,-8.515247,3.899156,-4.644430,6.961731],[6.876620,-8.941852,-8.482095,-3.233433,5.412765,0.042127,-9.963029,-6.542274,6.763389,-8.452080,-4.578818],[8.627491,-3.784121,6.375861,-7.061630,5.161042,-6.947120,-5.467186,8.267809,-3.699311,-3.166975,-8.231194],[-3.993279,5.604550,5.450394,-2.719505,-6.108235,-9.335481,-2.067198,-3.346009,-8.240353,9.717341,9.867532],[3.303740,-2.905171,4.887781,4.158024,1.371848,-5.820683,9.701493,-4.222966,9.557176,-7.139395,-7.031746],[-7.647581,2.018299,-6.815689,4.488222,9.251036,-6.106534,-1.179128,-5.034468,-8.075277,5.206739,5.572333],[-8.997799,-1.982050,-0.141796,1.906834,1.922348,6.393440,0.043306,1.176884,-2.202006,1.763865,-2.675461],[-8.248409,-0.076042,7.159886,-5.660943,-1.631108,-8.598160,-2.024170,2.729125,9.417469,0.448931,-2.980479],[-5.204026,3.316413,-2.763896,-1.847285,-8.154597,5.662620,0.205082,-1.052105,3.536131,-6.220171,8.781266],[1.981981,-2.549917,-9.984210,0.420099,-1.961058,-0.846969,-2.673884,2.582641,-6.610839,-0.668481,-0.439704],[-5.100733,3.119581,9.574984,6.243156,-3.564577,-5.911686,-0.545251,2.784469,3.605835,9.941952,4.781199],[-0.035094,-8.540999,7.265667,-3.439823,-5.831464,-9.322323,4.999696,5.343634,6.491205,7.921665,6.238374],[-6.889692,5.324537,-9.765465,0.714191,3.092331,-4.604978,-9.156305,-7.316443,1.851688,3.629898,-7.444714],[-3.947860,-8.581062,7.428290,0.580310,6.448241,6.822531,1.425836,9.753018,-2.596570,-2.028207,4.967507],[-4.157295,5.196158,-6.168741,3.527813,4.249511,0.606567,4.751001,4.713004,8.126463,-3.450700,-4.496566]],[[-1.163164,3.606189,-4.732626,-0.179936,-1.368445,2.166528,-1.515612,9.883327,-1.495838,9.382817,-6.047892],[-9.695768,1.700392,-1.516662,6.968969,6.546394,-3.562922,-6.914719,-4.272299,-3.100516,5.245042,1.047927],[-0.122692,2.467135,9.187250,-0.857149,-7.126455,-6.373970,-5.360419,3.071980,7.813544,5.701642,8.784067],[-6.936425,-6.841389,0.954061,-5.643366,-4.897642,0.707797,6.017627,-2.683840,-7.591386,-4.178785,9.819226],[5.779545,-9.725337,3.144152,-6.603784,4.360762,6.639482,-1.501854,2.175321,3.180933,1.189677,-6.776725],[6.353134,-6.986364,6.111248,-6.677502,5.716166,0.005866,-5.064715,2.539011,-7.435858,5.613319,5.223313],[-4.047916,-0.471797,-4.627824,-8.956115,-8.825827,7.881820,9.416150,-9.334231,5.461139,8.784759,9.696188],[-6.084090,-4.634464,-4.209479,-0.838605,9.798543,-4.983944,-1.666199,2.892393,1.352367,-4.363627,-3.151746],[4.524312,-1.016266,-4.479680,-4.553268,7.246566,4.844142,4.974409,-2.231566,9.013654,-5.000604,3.765203],[-0.467360,7.899885,6.505960,-1.287941,4.545327,-9.338282,1.177386,9.599229,-1.434454,-0.881473,-6.037529],[0.355088,0.768217,7.869689,6.707943,-1.942790,3.394248,1.275875,9.187084,9.236932,-4.508165,-0.418964],[-5.167059,2.710378,2.634685,-7.075680,0.629048,-1.821290,-4.825365,-7.935562,-6.319681,7.212427,-3.476760],[-2.428594,1.843267,-2.947847,3.031520,0.853482,-1.140906,5.991883,-5.138694,9.250143,8.109999,-4.685032],[6.181640,9.030234,2.857189,-2.908391,-4.877730,0.572042,-6.737415,1.684966,8.454005,3.499228,1.999695],[0.918248,1.069830,3.562229,-7.700679,-3.651832,-4.322013,5.061783,5.015874,3.641511,6.103391,3.165605]],[[-4.259684,0.350308,4.971735,9.820893,4.329778,-7.722996,0.824633,-8.824272,9.678230,-1.900880,-5.276541],[0.329597,0.018192,9.699557,8.867235,-0.078227,0.377894,4.754128,-3.909222,0.160428,7.503959,-3.426499],[0.620857,-1.203353,-8.390519,-3.554964,6.140302,-2.497265,-5.377626,1.320624,-8.140473,0.766200,7.299064],[-7.424798,5.249246,-3.183919,5.532012,-9.143035,1.135585,7.038018,3.405523,-5.081021,7.081423,1.262666],[6.173973,3.089245,-5.759282,6.680621,-0.542505,9.242935,-7.279340,-3.995801,0.372909,-8.976806,-2.473674],[-0.514973,-7.472878,-3.756667,8.465923,5.454201,-8.783726,-1.436161,-5.711064,-7.409538,6.578144,-1.000009],[3.549456,6.452308,2.448440,6.390913,7.448508,3.351235,5.530439,3.333591,7.047526,3.334128,6.292154],[-5.209435,9.011784,-5.819811,1.254510,-3.989044,-5.624218,8.231795,-3.364914,3.485166,-9.683937,4.697783],[-0.323724,-2.298047,5.725622,5.611414,2.045143,-3.318935,-6.792599,0.544474,-8.259994,5.908031,5.259386],[-4.492778,8.554497,6.316652,0.362621,5.604297,1.232852,5.894263,5.198137,2.688015,1.640064,-2.681406],[6.310870,2.987885,0.506664,-2.974554,2.221262,-3.889938,-4.243216,-6.819186,-2.205834,8.755477,0.229861],[9.080164,2.673986,7.466139,-9.588477,-1.197359,0.777906,9.780668,-2.074086,4.827299,7.550804,0.372321],[8.431125,6.575317,8.291247,2.439335,8.656834,-2.302160,9.780810,4.302971,3.110712,6.451183,7.259253],[4.577468,-1.052104,5.262967,5.628911,7.859456,-6.860205,-0.586859,2.628017,-8.624113,-8.056912,1.237531],[-8.405796,-7.456996,3.932948,-1.468253,-2.570807,-5.167648,-6.140283,-6.815048,-8.486330,-6.456706,-5.396919]],[[1.928784,-8.416732,8.019699,-6.879089,3.516908,7.640229,-9.004663,5.668659,-8.648056,-7.954485,9.291482],[-9.432474,-4.367958,5.499005,-6.022705,-2.433597,-2.734927,6.845827,9.982270,-6.054150,1.271194,-0.808440],[-1.908508,-1.265605,-3.998849,-6.066133,-4.402260,2.115285,8.019511,5.279195,4.805606,9.383368,8.941782],[6.851438,-3.024045,6.299085,2.579815,5.048770,7.699680,-8.929925,2.320769,7.088776,-5.710843,-4.598393],[-1.813454,4.083143,8.281360,4.352091,5.245643,-1.454664,-7.669811,0.357838,3.662053,-2.827197,6.383318],[-7.099126,4.773588,-7.039327,1.604266,7.398580,-4.502633,9.999200,-2.491000,-8.871024,2.738558,8.883080],[-3.153429,7.733466,-2.133634,0.338991,9.960854,-3.220570,8.545924,-0.064526,3.114843,-2.314294,-0.139432],[-1.964750,-7.605427,-5.579139,7.831519,-2.977202,8.399692,8.341209,4.735953,2.088336,4.984272,8.532280],[-3.974775,3.880887,0.903379,9.581812,9.212599,-3.023658,0.499279,7.149122,1.545956,-2.774779,4.212024],[-6.379686,-9.319454,0.306554,1.486229,1.038479,-4.701219,5.553310,-1.825215,0.786345,-7.987748,-2.234484],[8.817753,-8.938432,5.984506,5.482960,0.770566,7.259575,7.210065,2.744033,3.227152,-2.004862,0.580606],[5.333907,-8.750897,2.317262,7.536109,-4.619232,5.722990,3.296333,-9.682288,9.512542,-6.769986,3.520104],[-0.251682,-9.143046,9.173357,6.625191,-1.741333,2.851390,-7.046435,-3.898342,-6.236307,-5.554502,2.775357],[-2.430552,-5.967693,8.702733,-6.041680,-1.043794,2.519498,-3.196667,6.238878,9.485633,-3.196583,-5.034896],[1.450310,-3.500982,-8.886215,4.979005,-4.010749,1.350219,-8.527830,9.522906,9.322752,1.236730,-6.058648]],[[-0.243628,8.768849,-3.900939,-2.016399,-2.213174,3.245156,3.154933,1.323957,2.152525,-1.266919,-6.228449],[-3.563674,1.611944,7.468952,-2.924312,-0.528564,8.344785,4.657639,0.372769,0.457356,9.307892,4.492534],[-9.092664,-2.784409,-1.325812,-5.320265,1.466084,3.339804,-7.779156,8.606155,-0.878954,2.231172,8.661710],[9.765519,-3.998670,4.733863,4.115030,-1.722780,5.229213,-8.148699,4.009112,2.945066,8.991431,3.115503],[7.223958,-1.773670,-6.448049,-7.212343,-8.477928,4.834657,-7.948063,1.642878,4.075817,4.846827,-9.697385],[-2.504432,-1.517505,-4.315091,-4.014899,6.646538,-7.226124,-9.679601,-8.812054,-2.535419,-1.128675,1.135884],[-4.769831,8.356093,4.001116,3.070520,-8.242867,1.249733,6.263834,-3.580285,-8.343162,3.744849,4.179438],[3.993098,-4.749754,5.143329,1.830821,1.201359,6.198962,0.112068,3.071126,-4.831484,5.713614,-2.491877],[3.170893,-0.526876,7.722697,-8.238442,7.138453,-2.680450,7.695630,9.436997,-0.212160,9.633490,4.028270],[-3.140089,8.411086,-5.910091,0.600323,9.127502,2.058242,-2.499243,4.204861,6.592320,-4.453169,1.967973],[8.358347,7.917220,3.650035,1.178782,7.624512,-2.569144,-4.556801,7.325121,2.082428,-5.758248,3.270508],[2.435750,4.996824,0.383832,-3.405550,-2.363937,6.848119,-2.209399,-6.270215,6.744743,0.513716,-1.129877],[-5.400763,1.186965,-9.489482,-2.439772,-9.918377,-7.780954,8.715232,-3.073843,-1.373751,5.659551,-2.875421],[9.504203,-7.023809,-7.440122,-1.339541,5.017364,6.074706,-1.472077,2.789686,9.444499,3.963868,8.436223],[2.745574,-3.484404,-0.966852,-8.466285,2.689935,9.227467,-8.987180,-3.103918,-0.202227,-1.903991,-3.316522]],[[3.270153,9.550229,-0.561205,9.746200,1.208477,2.877528,-5.706366,-0.527313,-5.695544,-0.938164,7.764496],[3.774338,2.716747,0.115892,8.007105,8.600546,6.628286,4.208348,6.092220,-1.146175,-9.607137,-5.508060],[0.737878,4.993408,1.331847,-2.902771,-0.009671,-5.372732,0.143746,4.409169,6.760020,-7.448865,-7.684495],[-0.057267,-1.279081,-8.812712,-2.216825,5.456191,5.009271,5.083366,7.161837,4.026495,-2.404031,0.385833],[-2.883580,-9.737269,5.141388,-3.180556,1.639201,3.690163,5.911243,-7.804903,4.306523,-7.098116,-1.822460],[7.358466,0.515182,5.684848,-7.705096,1.655349,-5.531781,-2.149077,-3.318098,2.974325,-4.691260,6.898526],[-9.670837,4.380783,-8.419126,4.039442,-7.907312,-2.674041,9.847594,6.988942,-7.084087,-2.499538,-3.962862],[9.107992,-1.391744,-9.747248,6.534282,-5.515321,1.301017,9.033220,9.009768,-1.422985,3.748095,2.248348],[0.180091,-6.968204,-1.726657,-6.504633,-5.731109,3.339056,-2.661555,6.190861,-2.571934,9.710710,4.983654],[7.279017,3.680232,-4.013054,-7.284873,-4.406640,-0.725017,0.513193,8.883276,-2.014275,0.656758,-4.359553],[8.855602,-7.440187,-9.373014,-1.144906,-8.470692,-3.566442,1.283726,3.253848,9.720051,0.702457,-8.468134],[-8.521128,-2.207060,6.348956,-5.077081,7.127243,1.561244,5.496890,-5.132383,-4.336294,7.310260,-3.723763],[7.523363,-3.547351,2.020987,7.026518,0.716661,-3.713869,-7.435406,6.435711,5.727561,-1.306805,-7.984940],[-2.030843,0.690150,-0.485746,-7.219561,-4.640264,-5.988770,-8.085302,-1.569333,0.598805,3.032926,-5.466760],[-7.619770,-5.449252,-1.068977,-7.404914,7.820402,5.186815,2.534486,8.838366,1.316236,-0.317831,2.850875]]], dtype = "float64")#candidate|7499|(9, 15, 11)|const|float64
bop_7500 = relay.floor_divide(var_7498.astype('float64'), relay.reshape(const_7499.astype('float64'), relay.shape_of(var_7498))) # shape=(9, 15, 11)
output = relay.Tuple([bop_7500,])
output2 = relay.Tuple([bop_7500,])
func_7511 = relay.Function([var_7498,], output)
mod['func_7511'] = func_7511
mod = relay.transform.InferType()(mod)
mutated_mod['func_7511'] = func_7511
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7512 = relay.var("var_7512", dtype = "float64", shape = (9, 15, 11))#candidate|7512|(9, 15, 11)|var|float64
func_7511_call = mutated_mod.get_global_var('func_7511')
call_7513 = func_7511_call(var_7512)
output = call_7513
func_7514 = relay.Function([var_7512], output)
mutated_mod['func_7514'] = func_7514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4021_call = mod.get_global_var('func_4021')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_7540 = relay.TupleGetItem(func_4021_call(), 0)
call_7541 = relay.TupleGetItem(func_4023_call(), 0)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_7551 = relay.TupleGetItem(func_2808_call(), 0)
call_7552 = relay.TupleGetItem(func_2810_call(), 0)
func_5912_call = mod.get_global_var('func_5912')
func_5913_call = mutated_mod.get_global_var('func_5913')
call_7561 = relay.TupleGetItem(func_5912_call(), 0)
call_7562 = relay.TupleGetItem(func_5913_call(), 0)
func_2187_call = mod.get_global_var('func_2187')
func_2190_call = mutated_mod.get_global_var('func_2190')
var_7575 = relay.var("var_7575", dtype = "int16", shape = (192,))#candidate|7575|(192,)|var|int16
const_7576 = relay.const(-1.002419, dtype = "float64")#candidate|7576|()|const|float64
call_7574 = relay.TupleGetItem(func_2187_call(relay.reshape(var_7575.astype('int16'), [4, 4, 12]), relay.reshape(const_7576.astype('float64'), []), ), 1)
call_7577 = relay.TupleGetItem(func_2190_call(relay.reshape(var_7575.astype('int16'), [4, 4, 12]), relay.reshape(const_7576.astype('float64'), []), ), 1)
output = relay.Tuple([call_7540,call_7551,call_7561,call_7574,var_7575,const_7576,])
output2 = relay.Tuple([call_7541,call_7552,call_7562,call_7577,var_7575,const_7576,])
func_7587 = relay.Function([var_7575,], output)
mod['func_7587'] = func_7587
mod = relay.transform.InferType()(mod)
mutated_mod['func_7587'] = func_7587
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7588 = relay.var("var_7588", dtype = "int16", shape = (192,))#candidate|7588|(192,)|var|int16
func_7587_call = mutated_mod.get_global_var('func_7587')
call_7589 = func_7587_call(var_7588)
output = call_7589
func_7590 = relay.Function([var_7588], output)
mutated_mod['func_7590'] = func_7590
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7609 = relay.var("var_7609", dtype = "float32", shape = (8, 8, 1))#candidate|7609|(8, 8, 1)|var|float32
uop_7610 = relay.rsqrt(var_7609.astype('float32')) # shape=(8, 8, 1)
output = uop_7610
output2 = uop_7610
func_7612 = relay.Function([var_7609,], output)
mod['func_7612'] = func_7612
mod = relay.transform.InferType()(mod)
var_7613 = relay.var("var_7613", dtype = "float32", shape = (8, 8, 1))#candidate|7613|(8, 8, 1)|var|float32
output = func_7612(var_7613)
func_7614 = relay.Function([var_7613], output)
mutated_mod['func_7614'] = func_7614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7204_call = mod.get_global_var('func_7204')
func_7206_call = mutated_mod.get_global_var('func_7206')
call_7649 = relay.TupleGetItem(func_7204_call(), 1)
call_7650 = relay.TupleGetItem(func_7206_call(), 1)
var_7657 = relay.var("var_7657", dtype = "float64", shape = (110,))#candidate|7657|(110,)|var|float64
bop_7658 = relay.power(call_7649.astype('float64'), relay.reshape(var_7657.astype('float64'), relay.shape_of(call_7649))) # shape=(110,)
bop_7661 = relay.power(call_7650.astype('float64'), relay.reshape(var_7657.astype('float64'), relay.shape_of(call_7650))) # shape=(110,)
func_3414_call = mod.get_global_var('func_3414')
func_3416_call = mutated_mod.get_global_var('func_3416')
var_7667 = relay.var("var_7667", dtype = "float64", shape = ())#candidate|7667|()|var|float64
call_7666 = relay.TupleGetItem(func_3414_call(relay.reshape(var_7667.astype('float64'), [])), 3)
call_7668 = relay.TupleGetItem(func_3416_call(relay.reshape(var_7667.astype('float64'), [])), 3)
output = relay.Tuple([bop_7658,call_7666,var_7667,])
output2 = relay.Tuple([bop_7661,call_7668,var_7667,])
func_7671 = relay.Function([var_7657,var_7667,], output)
mod['func_7671'] = func_7671
mod = relay.transform.InferType()(mod)
var_7672 = relay.var("var_7672", dtype = "float64", shape = (110,))#candidate|7672|(110,)|var|float64
var_7673 = relay.var("var_7673", dtype = "float64", shape = ())#candidate|7673|()|var|float64
output = func_7671(var_7672,var_7673,)
func_7674 = relay.Function([var_7672,var_7673,], output)
mutated_mod['func_7674'] = func_7674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_7694 = relay.TupleGetItem(func_2526_call(), 0)
call_7695 = relay.TupleGetItem(func_2528_call(), 0)
func_6432_call = mod.get_global_var('func_6432')
func_6436_call = mutated_mod.get_global_var('func_6436')
var_7706 = relay.var("var_7706", dtype = "float64", shape = (11, 10))#candidate|7706|(11, 10)|var|float64
const_7707 = relay.const([-8,1,-4,7,-5,-5,5,2,-6,-10,8,10,-8,-10,-5,1,9,-1,6,-2,-8,-5,-5,-6,-1,-9,-10,8,7,-6,-10,-6,-9,-2,2,8,-1,4,10,-8,4,2,6,2,10,6,7,1,-8,2,8,-1,-3,-6,-4,-3,-4,4,7,-5,-6,-8,-2,8,3,1,2,-2,-8,-7,5,-3,-7,10,3,-2,4,-1,-1,8,10,7,3,6,-2,-4,-5,5,-5,7,-10,-8,-8,-3,-9,5,2,1,5,-7,-2,-3,9,10,-5,-2,5,9,1,4,-7,-1,-3,6,-10,3,5,9,-4,-10,6,-1,-3,4,-6,-6,-7,2,7,-8,-1,1,6,2,10,8,5,9,-4,2,3,-3,-4,2,4,-10,-2,-3,-10,-8,-8,-8,-10,8,2,-3,9,5,2,-3,-9,3,6,10,10,8,-6,8,-3,-9,-8,10,-8,-9,4,7,8,5,-6,10,2,-6,4,4,2,-4,8,10,-1,-8,-4,10,-7,-4,7,10,9,10,2,5,-9,-8,5,3,-6,2,-8,-2,5,-7,-7,6,5,-3,9,-2,-5,5,8,-5,-1,-6,9,-1,1,9,-6,-8,-10,-7,7,9,-2,3,4,-6,-6,3,10,10,-3,1,-3,-2,10,-3,-1,-10,-9,-2,-2,10,-1,-1,-9,2,9,3,4,6,5,10,4,-8,4,7,-8,-4,-2,-10,8,-4,5,1,-3,3,6,5,-5,2,4,-5,-6,1,-8,10,-3,2,-2,-9,-10,2,-6,-6,1,-10,9,7,-6,5,9,7,8,2,-6,4,1,-4,4,-10,9,-7,-5,4,-3,3,-4,6,4,1,-6,6,2,6,1,8,4,-8,10,-10,3,-4,8,9,7,3,-7,-1,-10,-3,-3,-1,-6,7,5,8,-5,-4,-4,6,-5,5,8,8,-4,-9,2,5,-10,-4,2,-4,-8,-7,-1,6,-1,-7,8,7,4,1,5,-6,8,2,3,4,-4,6,5,-1,-4,5,4,7,5,6,4,5,-1,2,2,-7,-1,2,-6,2,1,-3,-7,-5,-6,2,-2,-4,5,6,3,2,6,-8,6,2,7,-4,-6,7,-9,-4,8,-3,3,10,3,-8,7,1,9,-3,-9,-1,6,-6,8,6,-5,1,-8,-2,3,2,-9,3,4,-4,-3,-7,2,-5,-1,-10,-10,4,2,-1,-7,6,5,4,7,4,3,-10,5,7,4,2,-8,6,-2,6,-1,7,-4,-7,1,1,-5,10,4,-3,7,-6,2,7,-8,-5,-5,-7,7,10,-7,1,1,9,-1,8,10,2,-6,5,-2,-5,5,6,5,-10,-8,-2,6,-6,6,4,-8,7,5,-9,2,-4,5,-1,-7,-3,-5,5,8,6,-5,-1,7,8,8,1,-3,-9,6,-9,2,-9,10,-6,-5,-4,5,5,1,-5,3,1,2,4,-1,-4,-6,-9,7,7,-8,-4,6,6,-3,8,-9,-9,2,-1,-6,-5,-8,-1,10,6,-6,-2,10,-2,10,-6,-1,-10,-10,-6,-5,-9,5,-7,7,-6,6,7,-5,8,1,4,2,-4,8,7,3,6,7,7,-1,-6,9,2,2,-1,5,-6,-3,7,2,-3,-3,7,6,-5,4,-3,-7,-9,6,-4,7,-8,-10,-10,-3,1,5,10,-9,6,6,-8,-4,-4,9,3,-5,6,8,-2,-10,10,9,5,-3,-3,10,-4,8,-7,5,3,-1,-9,-5,-3,-4,-8,-1,2,6,6,7,-2,-7,2,-9,4,-3,10,-4,3,-3,10,6,1,9,7,7,-3,-8,-8,1,6,5,-4,-8,4,9,-9,-7,-6,6,-2,-3,-9,1,8,9,6,2,10,6,-5,-9,-8,3,-3,-7,3,-2,-1,-10,-3,-4,3,-8,8,-7,8,7,2,-10,-10,10,9,8,2,-10,6,-5,-2,2,-8,-2,4,-2,1,9,-3,7,-10,-1,-2,9,-6,7,-1,7,9,-6,3,9,-4,-5,9,6,-6,2,-9,-8,-7,-3,3,8,3,4,5,-10,-2,-5,-7,-10,9,3,-3,5,7,8,1,-1,-3,-10,10,7,-5,5,-5,-8,-5,2,-3,9,4,9,5,-10,7,-9,2,-1,10,10,8,-10,1,2,9,-4,-1,8,5,8,-10,10,-5,-6,6,-10,5,9,2,-8,5,3,4,-5,9,-10,-8,-10,1,10,3,-2,-2,2,4,-4,-3,8,8,6,-5,-8,-7,8,4,5,-7,-4,10,2,8,-7,-3,-10,-8,-8,-3,8,3,-9,-3,4,1,-9,-6,7,7,6,-8,-8,-3,1,-5,7,4,-6,-8,9,8,2,-10,-7,2,-6,-10,-9,5,8,-9,-7,-8,-2,-3,8,10,3,-1,-7,-4,5,1,4,6,-3,6,1,-5,2,5,-7,-2,-5,1,-7,-6,6,10,3,-3,-4,8,-2,-8,3,6,8,-2,-2,6,-7,-4,2,-4,-2,1,5,1,6,-2,3,-9,-6,4,4,-7,-4,8,7,-9,1,6,3,3,-9,6,-1,-4,6,4,10,2,4,-8,-2,-1,8,8,5,9,-6,-5,-2,5,9,-7,-5,-10,9,-2,-4,-5,-10,-6,-6,-8,-1,-1,-4,-10,-8,-1,-6,-3,-9,-9,8,7,-8,-3,-7,-7,8,1,4,6,-8,8,7,2,-4,9,4,-2,-9,7,9,-6,1,10,9,-1,2,3,-9,-5,6,7,-10,-2,-5,6,-2,1,-10,-1,7,-9,9,10,9,-3,9,-4,-10,-9,5,8,-8,1,10,-10,-1,-7,3,8,-3,6,4,3,6,8,-9,-9,7,-6,9,3,-7,2,-8,-1,-3,2,-6,-1,9,4,-10,-5,-2,-4,-9,4,-9,-7,7,9,4,9,-8,-4,4,5,2,10,8,-8,-3,4,-9,3,10,9,-7,6,1,-4,-2,8,6,-2,2,-3,2,-8,-2,-10,5,6,8,-9,6,5,-10,-1,-8,3,3,-6,-7,8,7,10,7,-6,-10,7,8,-3,2,-7,7,2,-7,-6,3,4,4,-4,9,-8,-4,-4,-5,-5,1,9,3,9,-8,-6,9,-2,1,-3,-5,1,6,-4,-4,-9,-10,-4,-10,4,-8,-10,8,1,8,-2,-5,-4,10,-3,6,1,10,10,-10,7,-5,-6,-9,-2,9,7,9,-6,-1,5,-2,-5,2,4,2,-10,8,-7,1,1,-5,5,-2,-3,1,-10,4,7,3,-8,3,-1,1,6,-9,-3,7,-8,-10,-4,9,-6,-1,9,-4,-10,-2,-6,9,9,10,2,-10,8,3,3,-6,-5,3,3,-10,4,6,-8,-3,4,-9,-3,-7,10,-3,-2,-3,-5,4,6,3,-9,-2,-3,-4,-8,-3,1,-2,-10,6,-3,2,7,-8,-1,5,-7,4,1,6,10,-10,9,-2,8,-2,8,9,-1,10,-5,9,1,-3,-3,2,6,4,6,4,-3,5,2,9,-8,-5,-4,-6,-10,-7,-5,6,-1,-7,-6,2,-7,1,8,5,10,10,4,1,6,7,-7,5,5,6,4,1,5,-3,3,-1,-5,7,9,-3,5,8,-5,1,-6,-1,5,2,-5,2,-2,-1,6,-8,5,1,3,4,-4,-8,-2,-9,-3,6,7,-4,-3,-7,4,-3,7,10,5,8,9,-8,-8,-7,-9,7,-2,-6,-7,-3,6,-1,-2,-3,-7,6,10,8,-2,-9,9,-8,8,-10,-5,-7,1,-6,-10,-1,3,-4,3,10,-6,-8,-6,10,2,-10,-2,-2,6,-7,-8,-5,10,-3,-3,8,-4,6,7,-4,5,8,3,-10,7,-9,-8,3,6,-10,-10,8,-7,4,2,4,5,3,-1,9,2,10,-4,7,10,-1,-8,-4,5,10,7,-5,6,-10,-10,-5,-9,-4,10,5,1,-8,-4,3,-10,7,8,10,9,-3,9,5,2,2,-1,10,10,-8,-10,-4,-7,-8,4,-9,7,5,-9,-5,8,-1,-2,-8,8,-7,-10,-1,-3,-1,6,-1,3,9,4,1,1,2,4,8,-9,-2,-7,5,-1,-8,-8,8,-4,-1,2,2,-5,-9,-6,3,-3,2,10,-1,-6,6,7,-5,-4,1,10,1,8,4,-6,-9,4,8,-1,-2,7,10,3,-7,2,3,9,-7,4,3,10,1,-3,5,10,-8,-7,-3,4,9,5,-7,-8,5,6,3,10,-8,-5,-7,-2,1,5,-2,-3,-4,7,-7,4,8,-10,5,-7,2,-8,6,-6,-9,-3,10,4,-8,-5,-5,-5,-8,3,4,6,1,-7,-4,-6,-3,-6,8,-9,10,-9,3,-9,10,6,-4,-2,-8,4,1,5,-10,9,2,4,9,8,-9,5,-8,5,-5,7,-3,3,10,8,-10,7,4,-3,-7,7,7,7,-4,5,7,-1,2,6,6,3,-2,8,-2,-1,4,-6,1,-4,6,-4,-3,7,1,-9,-7,4,3,-5,5,-5,-5,7,4,3,-3,7,2,-1,-7,-3,-3,4,-9,10,-9,10,-5,10,-10,-3,9,-9,4,-5,2,-5,-5,10,2,-5,-6,4,1,3,8,4,-6,10,5,-2,3,4,8,1,4,10,-10,3,10,-5,-2,6,4,-9,-1,-7,-8,-4,5,-6,-1,10,1,-5,7,-7,-10,8,-9,4,10,4,-4,-4,-6,-7,7,8,-1,8,4,-1,-8,-10,-8,7,-8,7,1,-1,4,-2,7,10,5,-8,-3,1,9,-8,-8,6,6,-7,5,-2,8,-1,-5,5,-6,7,3,1,-1,-9,-4,2,8,-6,9,-3,1,-4,-2,-6,-3,10,-1,7,9,-1,-1,-4,-4,2,-8,2,9,-8,4,-1,-7,10,3,-1,5,7,5,-5,-10,4,-3,9,-10,-5,9,1,9,3,1,4,6,-10,-1,-1,5,10,2,10,-6,-8,4,-10,-1,5,-1,-5,-2,-7,3,5,5,-6,7,-1,-2,8,8,-9,5,10,6,-10,-4,1,-6,3,-6,-10,-4,3,-10,4,-1,9,-8,9,-6,-2,7,-8,-2,6,-10,10,-5,-2,6,-5,8,2,-2,-9,1,9,-7,-10,-7,-8,3,5,-4,5,4,8,5,-9,10,-7,1,6,-4,6,5,10,-3,5,1,-7,1,6,-5,3,3,6,-8,2,1,3,4,-3,8,6,8,-4,-1,3,7,1,7,-6,10,-5,7,-8,-1,10,8,9,-9,5,5,-6,-5,4,6,5,7,-8,7,-7,-6,-6,-5,10,-9,-6,2,-9,-10,-9,3,4,-3,8,8,-6,4,-1,-8,3,-8,6,-2,9,9,8,-1,6,5,-1,1,1,1,4,-5,-9,-7,-4,-1,1,-10,-6,3,2,5,-3,3,2,6,-5,5,5,-10,-1,4,5,-2,5,-2,-3,2,-3,-10,1,1,8,-2,7,3,-5,9,9,2,5,10,-10,4,9,10,-9,-6,8,1,9,3,-9,5,-4,-3,-10,-8,9,-6,7,8,9,-4,-1,-4,9,4,2,7,6,-8,6,7,-10,-2,8,-5,-6,-6,4,-7,9,-10,-3,-8,8,7,2,7,-6,-10,-3,-3,-2,5,-9,8,6,-9,-4,9,-5,-5,-10,-10,5,3,3,-4,5,2,2,3,7,-8,-1,4,-3,4,5,-2,-1,6,-10,-10,2,10,1,3,-7,10,7,-5,-7,4,2,2,-10,9,1,-5,-1,-8,-10,2,-1,9,-8,-6,5,9,-7,-3,7,7,3,-10,8,-9,-8,-10,-3,5,-5,-8,-3,8,-6,-5,6,3], dtype = "int32")#candidate|7707|(2197,)|const|int32
call_7705 = relay.TupleGetItem(func_6432_call(relay.reshape(var_7706.astype('float64'), [110,]), relay.reshape(const_7707.astype('int32'), [2197,]), ), 0)
call_7708 = relay.TupleGetItem(func_6436_call(relay.reshape(var_7706.astype('float64'), [110,]), relay.reshape(const_7707.astype('int32'), [2197,]), ), 0)
uop_7716 = relay.rsqrt(const_7707.astype('float32')) # shape=(2197,)
uop_7724 = relay.acosh(uop_7716.astype('float32')) # shape=(2197,)
output = relay.Tuple([call_7694,call_7705,var_7706,uop_7724,])
output2 = relay.Tuple([call_7695,call_7708,var_7706,uop_7724,])
func_7730 = relay.Function([var_7706,], output)
mod['func_7730'] = func_7730
mod = relay.transform.InferType()(mod)
mutated_mod['func_7730'] = func_7730
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7731 = relay.var("var_7731", dtype = "float64", shape = (11, 10))#candidate|7731|(11, 10)|var|float64
func_7730_call = mutated_mod.get_global_var('func_7730')
call_7732 = func_7730_call(var_7731)
output = call_7732
func_7733 = relay.Function([var_7731], output)
mutated_mod['func_7733'] = func_7733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7307_call = mod.get_global_var('func_7307')
func_7309_call = mutated_mod.get_global_var('func_7309')
call_7735 = relay.TupleGetItem(func_7307_call(), 0)
call_7736 = relay.TupleGetItem(func_7309_call(), 0)
uop_7737 = relay.cosh(call_7735.astype('float32')) # shape=(3, 2, 15)
uop_7739 = relay.cosh(call_7736.astype('float32')) # shape=(3, 2, 15)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_7740 = relay.TupleGetItem(func_3892_call(), 0)
call_7741 = relay.TupleGetItem(func_3894_call(), 0)
output = relay.Tuple([uop_7737,call_7740,])
output2 = relay.Tuple([uop_7739,call_7741,])
func_7759 = relay.Function([], output)
mod['func_7759'] = func_7759
mod = relay.transform.InferType()(mod)
mutated_mod['func_7759'] = func_7759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7759_call = mutated_mod.get_global_var('func_7759')
call_7760 = func_7759_call()
output = call_7760
func_7761 = relay.Function([], output)
mutated_mod['func_7761'] = func_7761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5406_call = mod.get_global_var('func_5406')
func_5408_call = mutated_mod.get_global_var('func_5408')
call_7803 = func_5406_call()
call_7804 = func_5406_call()
uop_7809 = relay.acosh(call_7803.astype('float64')) # shape=(28,)
uop_7811 = relay.acosh(call_7804.astype('float64')) # shape=(28,)
output = uop_7809
output2 = uop_7811
func_7812 = relay.Function([], output)
mod['func_7812'] = func_7812
mod = relay.transform.InferType()(mod)
output = func_7812()
func_7813 = relay.Function([], output)
mutated_mod['func_7813'] = func_7813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5612_call = mod.get_global_var('func_5612')
func_5614_call = mutated_mod.get_global_var('func_5614')
call_7887 = relay.TupleGetItem(func_5612_call(), 0)
call_7888 = relay.TupleGetItem(func_5614_call(), 0)
output = relay.Tuple([call_7887,])
output2 = relay.Tuple([call_7888,])
func_7901 = relay.Function([], output)
mod['func_7901'] = func_7901
mod = relay.transform.InferType()(mod)
mutated_mod['func_7901'] = func_7901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7901_call = mutated_mod.get_global_var('func_7901')
call_7902 = func_7901_call()
output = call_7902
func_7903 = relay.Function([], output)
mutated_mod['func_7903'] = func_7903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_7906 = relay.TupleGetItem(func_2467_call(), 1)
call_7907 = relay.TupleGetItem(func_2468_call(), 1)
output = call_7906
output2 = call_7907
func_7911 = relay.Function([], output)
mod['func_7911'] = func_7911
mod = relay.transform.InferType()(mod)
output = func_7911()
func_7912 = relay.Function([], output)
mutated_mod['func_7912'] = func_7912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3803_call = mod.get_global_var('func_3803')
func_3805_call = mutated_mod.get_global_var('func_3805')
call_8028 = relay.TupleGetItem(func_3803_call(), 1)
call_8029 = relay.TupleGetItem(func_3805_call(), 1)
output = relay.Tuple([call_8028,])
output2 = relay.Tuple([call_8029,])
func_8034 = relay.Function([], output)
mod['func_8034'] = func_8034
mod = relay.transform.InferType()(mod)
mutated_mod['func_8034'] = func_8034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8034_call = mutated_mod.get_global_var('func_8034')
call_8035 = func_8034_call()
output = call_8035
func_8036 = relay.Function([], output)
mutated_mod['func_8036'] = func_8036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_8058 = relay.TupleGetItem(func_3892_call(), 4)
call_8059 = relay.TupleGetItem(func_3894_call(), 4)
func_3414_call = mod.get_global_var('func_3414')
func_3416_call = mutated_mod.get_global_var('func_3416')
const_8074 = relay.const(2.926408, dtype = "float64")#candidate|8074|()|const|float64
call_8073 = relay.TupleGetItem(func_3414_call(relay.reshape(const_8074.astype('float64'), [])), 3)
call_8075 = relay.TupleGetItem(func_3416_call(relay.reshape(const_8074.astype('float64'), [])), 3)
output = relay.Tuple([call_8058,call_8073,const_8074,])
output2 = relay.Tuple([call_8059,call_8075,const_8074,])
func_8080 = relay.Function([], output)
mod['func_8080'] = func_8080
mod = relay.transform.InferType()(mod)
output = func_8080()
func_8081 = relay.Function([], output)
mutated_mod['func_8081'] = func_8081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_8101 = relay.TupleGetItem(func_2945_call(), 1)
call_8102 = relay.TupleGetItem(func_2947_call(), 1)
output = relay.Tuple([call_8101,])
output2 = relay.Tuple([call_8102,])
func_8109 = relay.Function([], output)
mod['func_8109'] = func_8109
mod = relay.transform.InferType()(mod)
mutated_mod['func_8109'] = func_8109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8109_call = mutated_mod.get_global_var('func_8109')
call_8110 = func_8109_call()
output = call_8110
func_8111 = relay.Function([], output)
mutated_mod['func_8111'] = func_8111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3803_call = mod.get_global_var('func_3803')
func_3805_call = mutated_mod.get_global_var('func_3805')
call_8127 = relay.TupleGetItem(func_3803_call(), 0)
call_8128 = relay.TupleGetItem(func_3805_call(), 0)
func_7759_call = mod.get_global_var('func_7759')
func_7761_call = mutated_mod.get_global_var('func_7761')
call_8134 = relay.TupleGetItem(func_7759_call(), 0)
call_8135 = relay.TupleGetItem(func_7761_call(), 0)
output = relay.Tuple([call_8127,call_8134,])
output2 = relay.Tuple([call_8128,call_8135,])
func_8146 = relay.Function([], output)
mod['func_8146'] = func_8146
mod = relay.transform.InferType()(mod)
output = func_8146()
func_8147 = relay.Function([], output)
mutated_mod['func_8147'] = func_8147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6204_call = mod.get_global_var('func_6204')
func_6206_call = mutated_mod.get_global_var('func_6206')
call_8171 = relay.TupleGetItem(func_6204_call(), 1)
call_8172 = relay.TupleGetItem(func_6206_call(), 1)
output = call_8171
output2 = call_8172
func_8179 = relay.Function([], output)
mod['func_8179'] = func_8179
mod = relay.transform.InferType()(mod)
mutated_mod['func_8179'] = func_8179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8179_call = mutated_mod.get_global_var('func_8179')
call_8180 = func_8179_call()
output = call_8180
func_8181 = relay.Function([], output)
mutated_mod['func_8181'] = func_8181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4792_call = mod.get_global_var('func_4792')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_8211 = relay.TupleGetItem(func_4792_call(), 0)
call_8212 = relay.TupleGetItem(func_4793_call(), 0)
func_4473_call = mod.get_global_var('func_4473')
func_4475_call = mutated_mod.get_global_var('func_4475')
var_8224 = relay.var("var_8224", dtype = "float64", shape = ())#candidate|8224|()|var|float64
call_8223 = relay.TupleGetItem(func_4473_call(relay.reshape(var_8224.astype('float64'), [])), 1)
call_8225 = relay.TupleGetItem(func_4475_call(relay.reshape(var_8224.astype('float64'), [])), 1)
func_7162_call = mod.get_global_var('func_7162')
func_7163_call = mutated_mod.get_global_var('func_7163')
call_8233 = func_7162_call()
call_8234 = func_7162_call()
output = relay.Tuple([call_8211,call_8223,var_8224,call_8233,])
output2 = relay.Tuple([call_8212,call_8225,var_8224,call_8234,])
func_8236 = relay.Function([var_8224,], output)
mod['func_8236'] = func_8236
mod = relay.transform.InferType()(mod)
mutated_mod['func_8236'] = func_8236
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8237 = relay.var("var_8237", dtype = "float64", shape = ())#candidate|8237|()|var|float64
func_8236_call = mutated_mod.get_global_var('func_8236')
call_8238 = func_8236_call(var_8237)
output = call_8238
func_8239 = relay.Function([var_8237], output)
mutated_mod['func_8239'] = func_8239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_8246 = relay.TupleGetItem(func_2526_call(), 0)
call_8247 = relay.TupleGetItem(func_2528_call(), 0)
output = relay.Tuple([call_8246,])
output2 = relay.Tuple([call_8247,])
func_8265 = relay.Function([], output)
mod['func_8265'] = func_8265
mod = relay.transform.InferType()(mod)
mutated_mod['func_8265'] = func_8265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8265_call = mutated_mod.get_global_var('func_8265')
call_8266 = func_8265_call()
output = call_8266
func_8267 = relay.Function([], output)
mutated_mod['func_8267'] = func_8267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_8304 = func_7812_call()
call_8305 = func_7812_call()
func_3973_call = mod.get_global_var('func_3973')
func_3976_call = mutated_mod.get_global_var('func_3976')
const_8309 = relay.const([[7.374694],[-9.849054],[-9.193351],[6.693442],[-1.756706],[6.706855],[9.491057],[9.875189],[6.604683],[5.319805],[9.776025],[-6.015990],[6.551630],[-7.455602],[-4.079016],[-9.608530],[-9.283929],[-3.567779],[1.648605],[4.859283],[-7.155478],[8.610742],[-9.902900],[-1.777915],[-1.715909],[4.311208],[9.689193],[8.802893],[0.885979],[-2.351866],[-9.158689],[5.346938],[7.711600],[1.795827],[-0.143553],[-8.779117],[8.995867],[-6.548362],[-2.618738],[8.092878],[-7.693672],[4.577128],[-9.919055],[7.343132],[-4.434933],[-2.348020],[-2.731027],[9.168354],[6.180922],[-5.796793],[-9.185384],[-0.019347],[5.990983],[6.377399],[2.656111],[-3.000232],[9.797278],[0.474445],[-0.055451],[8.059213],[-7.393706],[1.449798],[-1.880893],[3.722567],[-2.503540],[3.146628],[-4.156093],[-3.332520],[-1.059843],[-4.281004],[3.753015],[9.207871],[-3.681695],[-2.849997],[4.002609],[1.090495],[0.270127],[4.435527],[-1.492327],[0.961760],[-4.522402],[8.382041],[0.928721],[-2.760613],[0.633901],[3.253191],[8.739751],[-0.037087],[-6.984204],[-2.539909],[-1.831651],[5.678677],[7.375912],[5.970831],[6.183190],[-7.284382],[4.232751],[2.512224],[3.269759],[-5.017741],[-9.864943],[8.138560],[0.475934],[2.614081],[2.901825],[1.988116],[2.332214],[0.277863],[4.888739],[-4.911037],[-3.770892],[8.741345],[-3.312521],[-4.992720],[-7.697426],[7.727040],[-4.747149],[0.711629],[-5.939615],[8.692056],[-2.722351],[2.630981],[-1.582509],[-4.471991],[-1.601103],[-6.238685],[3.129264],[-5.481078],[-6.083627],[-8.471969],[-6.807607],[0.705226],[-3.649492],[-8.555037],[2.209132],[-2.936940],[-4.750463],[-7.117384],[5.466449],[6.371491],[6.861018],[-0.006342],[0.189196],[7.903376],[6.882933],[-0.506857],[1.258919],[-1.116154],[-8.192002],[-0.848063],[8.162779],[-2.677412],[-8.900957],[-1.238439],[4.500250],[9.678970],[2.774061],[-0.305350],[2.572701],[4.785765],[5.021924],[-0.511202],[5.616192],[-5.412487],[5.579886],[-5.664047],[-1.159925],[-8.295466],[2.679745],[-6.165837],[-2.600345],[4.331598],[6.742040],[-7.121875],[1.899695],[2.900910],[-5.677655],[8.690929],[-5.314807],[3.880007],[-1.982280],[-7.362839],[-4.742310],[-4.781367],[8.395427],[8.324915],[-5.579605],[-3.825329],[-1.591598],[-5.870724],[-0.421599],[-9.722962],[4.904416],[-6.423716],[4.377044],[0.709469],[6.639942],[-6.116750],[4.786714],[1.928585],[7.191914],[-0.527444],[-4.854197],[0.857123],[-6.881173],[-0.619006],[5.517123],[4.384616],[2.780115],[2.865252],[1.041970],[-5.148320],[-7.029420],[8.861984],[6.240485],[6.158884],[5.110904],[3.287815],[-4.564889],[-6.192887],[-3.329651],[0.662628],[3.457657],[5.650737],[-7.719534],[8.373130],[1.290466],[5.713750],[0.916347],[5.393514],[2.327639],[4.866792],[1.770181],[-6.561725],[-6.749012],[-9.825280],[-7.661898],[-1.211358],[-2.532113],[-0.238430],[-2.030858],[-2.212825],[9.113691],[-9.105313],[-3.563252],[-2.333797],[-3.990049],[-6.245087],[-3.770121],[8.420934],[1.342015],[9.452567],[1.898168],[8.883456],[6.582816],[-8.794353],[-2.876166],[-7.091683],[-9.710201],[-2.695721],[-1.568746],[4.612174],[-6.156914],[-2.969505],[-5.314933],[8.620502],[5.348098],[7.056803],[9.198266],[-4.962317],[-5.112079],[-7.708437],[-8.671422],[3.205504],[2.047756],[1.160527],[-1.524361],[-7.012852],[4.766209],[5.074278],[-2.629043],[2.318776],[8.662902],[-9.920799],[-4.281375],[-8.010171],[-6.400206],[7.343169],[0.106623],[6.430035],[-6.298676],[-4.708180],[4.984126],[5.031317],[-2.698830],[7.799637],[-8.727752],[-3.158982],[7.080047],[-1.933584],[-3.766997],[8.773254],[7.006290],[9.395116],[4.859990],[-9.476566],[1.830413],[-7.285891],[5.144912],[6.779854],[-8.284380],[8.179513],[-3.393107],[-8.110941],[-8.486331],[0.788673],[0.044397],[0.029904],[2.571739],[0.472755],[-9.347414],[-2.728694],[2.120622],[-0.246590],[-1.256171],[-7.906368],[-6.480395],[8.833039],[9.478298],[7.266358],[-9.173808],[-3.021387],[2.007893],[3.544041],[-9.081278],[5.448598],[-4.832398],[6.813404],[-3.452032],[-1.646392],[9.745725],[6.365370],[-5.105610],[-1.775169],[-1.495515],[-8.429416],[-6.266859],[5.746464],[-1.863045],[-1.027246],[7.083082],[9.452478],[5.802719],[4.153985],[8.200611],[5.218069],[-8.837102],[-0.059924],[0.924201],[2.946581],[-3.019165],[7.511053],[-7.244696],[-4.897017],[4.886631],[-7.366795],[-4.172615],[-4.015094],[-0.170135],[4.047355],[8.453927],[-8.513820],[4.166136],[7.294280],[-3.419607],[9.177530],[-9.147009],[8.338058],[8.744251],[6.263122],[3.678729],[2.974771],[-8.053975],[5.495748],[-8.016056],[-9.829210],[8.196599],[4.144563],[0.386735],[-4.878836],[3.742697],[8.254085],[-8.850271],[1.051638],[-6.969431],[-7.178683],[-3.594615],[-2.210915],[9.621629],[9.676571],[-6.573373],[0.011327],[-6.814994],[6.052155],[4.086227],[4.558001],[7.043766],[-9.205793],[-4.738886],[7.179538],[5.989678],[-1.118921],[5.231251],[-4.005635],[-6.308757],[-2.066781],[5.404232],[3.395615],[9.160508],[9.987087],[-4.833154],[1.308178],[0.771902],[4.202014],[0.594589],[4.304441],[-5.467751],[-9.763218],[-7.732012],[-9.866763],[-8.410664],[0.248935],[-7.992375],[-3.881509],[9.618679],[7.635553],[-1.169955],[0.509938],[-5.915060],[0.083541],[4.648747],[-9.101355],[-6.568974],[-0.849532],[5.323534],[-8.973254],[9.893093],[1.522355],[-4.702022],[6.158317],[-4.825029],[0.583678],[-4.004614],[-9.677273],[5.823323],[-1.218524],[-5.718254],[-6.976934],[-0.954722],[4.186369],[1.800416],[0.382651],[-1.125501],[-8.937924],[-7.181925],[-2.719116],[-0.332503],[-0.756117],[8.801563],[-6.347891],[-8.131656],[2.112510],[4.615964],[-9.143859],[-4.904318],[-3.391604],[4.098937],[7.651958],[-9.029740],[-3.239724],[2.550624],[8.629491],[-8.925261],[-4.467151],[4.345361],[-3.912028],[-3.357760],[-7.629553],[3.669095],[8.073072],[8.079263],[0.800315],[2.866985],[-7.193070],[-1.458135],[0.262496],[9.708578],[-1.781430],[-0.262920],[9.704517],[8.507089],[6.786955],[-9.800593],[4.447677],[-2.655019],[7.921389],[-4.544834],[-3.076091],[8.217267],[-9.528081],[8.027391],[-3.230695],[-5.175664],[-7.166916],[0.139026],[-9.205148],[3.620720],[-9.059133],[-0.113527],[4.132329],[-9.550371],[-4.672235],[7.999923],[4.632702],[8.247186],[8.093204],[4.793134],[3.638251],[-4.213516],[-9.882927],[-0.010858],[-2.005811],[-6.767103],[5.079523],[-2.346790],[-5.655404],[4.273756],[-6.625626],[1.714085],[-0.020358],[2.757069],[-1.295504],[3.430199],[-0.402256],[1.662921],[1.252619],[-7.738214],[-0.833673],[1.428611],[8.597457],[-3.293109],[-8.989699],[-6.378488],[2.509986],[-6.122078],[-7.593535],[7.364289],[-9.678690],[-9.676203],[-0.081391],[9.951312],[3.944252],[2.773273],[3.729235],[0.259560],[-9.648728],[-4.340707],[-1.611623],[2.639567],[-7.270941],[3.303478],[3.555216],[8.142379],[6.163202],[0.274473],[-2.693600],[9.548624],[-5.969972],[4.117510],[7.832365],[-1.214109],[-0.338000],[3.472744],[5.545247],[-2.592487],[-9.221960],[-7.489825],[-1.508066],[-8.072868],[7.255100],[3.634122],[-2.534092],[-8.006453],[9.525937],[-1.035429],[-4.291460],[0.503229],[0.355358],[4.141779],[9.183865],[7.020782],[2.040052],[-9.482173],[9.133671],[0.573688],[-2.154178],[-2.747522],[-5.111360],[6.946079],[-8.655723],[-8.766793],[-7.203581],[-8.593656],[-4.343918],[-0.227022],[6.824881],[-2.054051],[8.071586],[6.906681],[0.384549],[6.417984],[3.864139],[-0.302720],[-4.903570],[-3.046740],[-4.978538],[-1.509231],[-1.148475],[-9.776286],[-6.628728],[-3.799254],[-4.934760],[5.515445],[2.949476],[6.795999],[7.914590],[-1.311442],[-8.475857],[-1.268544],[-2.344441],[-0.434203],[-6.214592],[7.015069],[5.316235],[2.192552],[-6.199438],[1.579503],[-6.228678],[-0.286461],[1.541107],[-6.737601],[9.948140],[-9.223195],[-6.035518],[-8.830993],[2.912725],[7.220576],[6.451042],[-3.529511],[-5.166246]], dtype = "float32")#candidate|8309|(660, 1)|const|float32
call_8308 = relay.TupleGetItem(func_3973_call(relay.reshape(const_8309.astype('float32'), [5, 12, 11])), 1)
call_8310 = relay.TupleGetItem(func_3976_call(relay.reshape(const_8309.astype('float32'), [5, 12, 11])), 1)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_8311 = relay.TupleGetItem(func_4872_call(), 1)
call_8312 = relay.TupleGetItem(func_4873_call(), 1)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_8314 = func_3544_call()
call_8315 = func_3544_call()
bop_8320 = relay.not_equal(call_8304.astype('bool'), const_8309.astype('bool')) # shape=(660, 28)
bop_8323 = relay.not_equal(call_8305.astype('bool'), const_8309.astype('bool')) # shape=(660, 28)
bop_8324 = relay.bitwise_or(call_8314.astype('uint16'), const_8309.astype('uint16')) # shape=(660, 28)
bop_8327 = relay.bitwise_or(call_8315.astype('uint16'), const_8309.astype('uint16')) # shape=(660, 28)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_8339 = relay.TupleGetItem(func_4872_call(), 0)
call_8340 = relay.TupleGetItem(func_4873_call(), 0)
uop_8342 = relay.asinh(const_8309.astype('float64')) # shape=(660, 1)
output = relay.Tuple([call_8308,call_8311,bop_8320,bop_8324,call_8339,uop_8342,])
output2 = relay.Tuple([call_8310,call_8312,bop_8323,bop_8327,call_8340,uop_8342,])
func_8347 = relay.Function([], output)
mod['func_8347'] = func_8347
mod = relay.transform.InferType()(mod)
mutated_mod['func_8347'] = func_8347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8347_call = mutated_mod.get_global_var('func_8347')
call_8348 = func_8347_call()
output = call_8348
func_8349 = relay.Function([], output)
mutated_mod['func_8349'] = func_8349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5912_call = mod.get_global_var('func_5912')
func_5913_call = mutated_mod.get_global_var('func_5913')
call_8374 = relay.TupleGetItem(func_5912_call(), 0)
call_8375 = relay.TupleGetItem(func_5913_call(), 0)
output = call_8374
output2 = call_8375
func_8383 = relay.Function([], output)
mod['func_8383'] = func_8383
mod = relay.transform.InferType()(mod)
mutated_mod['func_8383'] = func_8383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8383_call = mutated_mod.get_global_var('func_8383')
call_8384 = func_8383_call()
output = call_8384
func_8385 = relay.Function([], output)
mutated_mod['func_8385'] = func_8385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7759_call = mod.get_global_var('func_7759')
func_7761_call = mutated_mod.get_global_var('func_7761')
call_8431 = relay.TupleGetItem(func_7759_call(), 1)
call_8432 = relay.TupleGetItem(func_7761_call(), 1)
output = relay.Tuple([call_8431,])
output2 = relay.Tuple([call_8432,])
func_8439 = relay.Function([], output)
mod['func_8439'] = func_8439
mod = relay.transform.InferType()(mod)
mutated_mod['func_8439'] = func_8439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8439_call = mutated_mod.get_global_var('func_8439')
call_8440 = func_8439_call()
output = call_8440
func_8441 = relay.Function([], output)
mutated_mod['func_8441'] = func_8441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6830_call = mod.get_global_var('func_6830')
func_6831_call = mutated_mod.get_global_var('func_6831')
call_8459 = relay.TupleGetItem(func_6830_call(), 0)
call_8460 = relay.TupleGetItem(func_6831_call(), 0)
func_5895_call = mod.get_global_var('func_5895')
func_5897_call = mutated_mod.get_global_var('func_5897')
var_8462 = relay.var("var_8462", dtype = "float64", shape = (22, 5))#candidate|8462|(22, 5)|var|float64
call_8461 = relay.TupleGetItem(func_5895_call(relay.reshape(var_8462.astype('float64'), [110,])), 2)
call_8463 = relay.TupleGetItem(func_5897_call(relay.reshape(var_8462.astype('float64'), [110,])), 2)
output = relay.Tuple([call_8459,call_8461,var_8462,])
output2 = relay.Tuple([call_8460,call_8463,var_8462,])
func_8473 = relay.Function([var_8462,], output)
mod['func_8473'] = func_8473
mod = relay.transform.InferType()(mod)
var_8474 = relay.var("var_8474", dtype = "float64", shape = (22, 5))#candidate|8474|(22, 5)|var|float64
output = func_8473(var_8474)
func_8475 = relay.Function([var_8474], output)
mutated_mod['func_8475'] = func_8475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5600_call = mod.get_global_var('func_5600')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_8492 = func_5600_call()
call_8493 = func_5600_call()
output = call_8492
output2 = call_8493
func_8498 = relay.Function([], output)
mod['func_8498'] = func_8498
mod = relay.transform.InferType()(mod)
output = func_8498()
func_8499 = relay.Function([], output)
mutated_mod['func_8499'] = func_8499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6038_call = mod.get_global_var('func_6038')
func_6040_call = mutated_mod.get_global_var('func_6040')
call_8574 = relay.TupleGetItem(func_6038_call(), 1)
call_8575 = relay.TupleGetItem(func_6040_call(), 1)
uop_8587 = relay.atan(call_8574.astype('float32')) # shape=(1, 4, 7)
uop_8589 = relay.atan(call_8575.astype('float32')) # shape=(1, 4, 7)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_8608 = relay.const(0.170316, dtype = "float64")#candidate|8608|()|const|float64
const_8609 = relay.const([-6.503137,1.547928,7.253480,-0.280450,-9.211654,-1.262890,-9.055823,5.299379,1.326626,-3.956557,7.451500,3.187698,5.481769,7.229289,8.589901,-2.039240,9.453229,-2.808781,-2.530962,8.554376,-0.875450,-4.505253,3.613940,-3.376034,9.588161,7.171101,-5.184578,8.715639,-1.657070,-1.335994,7.939577,4.352047,-6.840416,4.106498,-9.399675,-3.267876,6.998166,0.587977,-5.231596,9.548869,-6.700631,-6.171650,9.970152,-7.424556,0.524184,1.755205,5.049008,2.307392,-0.197435,4.310270,1.490102,4.177349,-3.647163,7.679972,-7.713369,-3.820183,2.900222,-0.865736,-6.324125,-9.665381,1.941054,2.420018,-0.595092,5.901681,6.566678,5.950687,-3.445635,6.327376,-0.238364,2.414090,3.605341,9.212309,5.275113,7.627429,4.031861,9.056695,2.323804,9.233380,1.540497,-9.622135,4.937829,7.868087,-7.977304,3.924353,7.295934,-9.684172,-2.336696,2.627171,6.133010,-8.009257,8.380014,7.711082,-5.465573,-2.943682,0.870383,-3.955902,8.833708,-2.659246,5.696644,-4.348866,5.540464,4.874820,-7.126455,4.838749,-7.101324,-8.093839,3.359678,-7.419160,3.211431,5.683294], dtype = "float64")#candidate|8609|(110,)|const|float64
call_8607 = relay.TupleGetItem(func_2062_call(relay.reshape(const_8608.astype('float64'), []), relay.reshape(const_8609.astype('float64'), [10, 1, 11]), ), 0)
call_8610 = relay.TupleGetItem(func_2065_call(relay.reshape(const_8608.astype('float64'), []), relay.reshape(const_8609.astype('float64'), [10, 1, 11]), ), 0)
output = relay.Tuple([uop_8587,call_8607,const_8608,const_8609,])
output2 = relay.Tuple([uop_8589,call_8610,const_8608,const_8609,])
func_8611 = relay.Function([], output)
mod['func_8611'] = func_8611
mod = relay.transform.InferType()(mod)
mutated_mod['func_8611'] = func_8611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8611_call = mutated_mod.get_global_var('func_8611')
call_8612 = func_8611_call()
output = call_8612
func_8613 = relay.Function([], output)
mutated_mod['func_8613'] = func_8613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5600_call = mod.get_global_var('func_5600')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_8633 = func_5600_call()
call_8634 = func_5600_call()
var_8662 = relay.var("var_8662", dtype = "float64", shape = (110,))#candidate|8662|(110,)|var|float64
bop_8663 = relay.divide(call_8633.astype('float32'), relay.reshape(var_8662.astype('float32'), relay.shape_of(call_8633))) # shape=(110,)
bop_8666 = relay.divide(call_8634.astype('float32'), relay.reshape(var_8662.astype('float32'), relay.shape_of(call_8634))) # shape=(110,)
output = relay.Tuple([bop_8663,])
output2 = relay.Tuple([bop_8666,])
func_8667 = relay.Function([var_8662,], output)
mod['func_8667'] = func_8667
mod = relay.transform.InferType()(mod)
mutated_mod['func_8667'] = func_8667
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8668 = relay.var("var_8668", dtype = "float64", shape = (110,))#candidate|8668|(110,)|var|float64
func_8667_call = mutated_mod.get_global_var('func_8667')
call_8669 = func_8667_call(var_8668)
output = call_8669
func_8670 = relay.Function([var_8668], output)
mutated_mod['func_8670'] = func_8670
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8687 = relay.var("var_8687", dtype = "int32", shape = (16, 9, 12))#candidate|8687|(16, 9, 12)|var|int32
const_8688 = relay.const([[[8,5,-9,4,-9,3,-8,-5,5,9,3,-5],[6,-5,-6,1,4,-2,10,-8,5,-9,2,7],[6,-1,-9,7,4,8,-8,6,8,8,-5,9],[8,4,-3,-9,-6,7,9,-3,-7,-2,4,10],[-5,-10,-3,-2,-6,-2,7,8,-2,-1,1,3],[-8,5,-1,2,1,10,-10,8,-9,4,4,9],[7,6,-7,7,1,7,-7,2,2,6,4,-7],[4,9,3,3,-10,-1,-7,-2,10,-2,8,-9],[-8,10,8,-5,1,10,1,-8,-2,8,7,10]],[[9,6,-8,6,9,5,5,10,3,-2,5,5],[-6,9,-5,1,-10,9,-4,-3,-3,2,10,6],[4,-8,-7,-8,-8,-6,-5,4,8,3,-10,-6],[-7,-3,-10,8,8,-3,-9,-7,6,-7,-4,8],[6,-5,10,-1,10,3,4,4,-7,6,5,-2],[-9,-4,2,7,5,-6,3,-1,-1,3,-6,-7],[1,9,-7,1,-10,10,-8,9,9,8,5,5],[2,3,-4,-10,-4,-2,-8,8,7,9,7,9],[-5,9,6,6,-1,-7,9,-1,4,5,-4,1]],[[1,9,10,-5,2,-5,-8,-6,7,-6,-1,-1],[-10,-1,9,8,-4,9,4,8,-8,4,-3,-6],[6,-9,1,-3,6,5,-8,7,-9,-5,-10,9],[-6,-5,7,-9,5,1,-8,7,10,9,-5,9],[3,-9,7,-5,4,9,-3,-6,6,6,-6,10],[-5,4,-5,7,7,3,5,4,-7,-3,-3,9],[-10,7,-8,-2,4,-2,-10,-9,5,8,9,3],[9,6,-7,-5,-10,3,-7,-10,10,2,-2,-7],[-2,-9,1,6,-8,-3,-9,-1,1,8,8,1]],[[-1,10,-1,-2,-3,3,-5,-1,-3,-9,3,1],[6,1,7,-4,4,-4,10,-9,7,5,3,4],[-2,-8,2,2,1,2,5,8,9,-6,8,-1],[7,6,6,8,4,7,-7,6,2,6,5,9],[-6,4,-10,10,5,-9,-7,-10,-5,10,6,2],[3,5,3,-3,-9,-4,6,-6,1,3,-4,-10],[-2,3,-6,5,-2,-9,-6,-6,3,-4,6,-3],[5,7,-1,-8,-9,10,-3,-7,7,2,10,6],[1,-6,10,-4,-5,4,-9,-10,3,-6,-5,5]],[[-8,-5,6,4,1,-4,9,-8,10,2,-6,10],[2,-8,-8,1,2,6,7,-5,2,-9,-7,7],[9,-7,-2,6,2,3,9,-5,7,-8,3,-3],[3,6,-1,7,2,6,-10,8,-8,-3,-2,-9],[2,-5,1,10,4,-3,-8,-6,4,-4,4,-8],[10,9,-2,3,6,-10,10,2,-5,8,5,6],[3,2,2,2,-3,-6,-1,-10,-10,5,-10,3],[-2,-3,-4,4,8,7,-10,-4,9,-8,10,9],[-10,-8,-3,-8,-2,2,7,-3,6,7,-8,8]],[[10,10,-6,7,-5,-6,6,3,-4,-3,-5,-8],[-6,-6,5,-6,10,4,-6,1,8,2,-1,3],[4,-6,4,-9,-10,-7,-8,1,-10,3,-8,9],[-2,-1,8,6,-9,10,-6,-4,-3,-3,-5,-1],[9,-10,8,2,-2,3,-6,1,-1,9,-9,6],[-5,7,3,-4,1,9,7,1,6,-9,-3,8],[-3,-5,-1,6,-10,-5,-10,5,-4,3,6,1],[10,-4,2,8,8,-8,4,4,-7,-7,7,10],[-4,3,9,-4,3,5,-10,1,-6,-9,-2,-6]],[[-2,-8,5,-4,-3,1,-10,4,-4,1,1,4],[-10,10,5,-3,-1,8,2,-4,-9,-8,3,6],[-10,3,-8,1,-9,-10,-8,-3,-7,-4,-5,4],[7,-6,-6,8,-7,7,8,-3,-8,-3,-9,5],[9,5,-10,-9,2,7,-6,-4,-6,10,9,-10],[6,5,-10,-1,2,5,6,-10,7,-8,4,8],[3,3,1,10,7,-5,8,7,4,5,-6,-10],[-4,-8,10,-8,5,-6,-7,4,-6,2,-6,7],[1,-10,8,-1,-8,-3,-6,1,4,-8,8,4]],[[2,7,5,8,5,-4,-9,7,4,6,-3,-1],[-6,8,2,7,10,-4,5,2,1,3,10,9],[-10,-4,-4,9,-6,6,-1,-6,7,7,-1,2],[-6,3,-4,2,7,-8,2,5,-6,-10,5,9],[3,4,6,7,10,10,10,10,9,-2,-5,1],[-9,-2,6,-4,9,4,-3,-9,-8,-9,-10,-10],[8,10,-9,7,-3,-2,-2,7,-2,9,9,-8],[-7,-9,-7,6,1,9,8,-9,4,-7,8,8],[-4,-5,4,-1,-2,10,9,5,1,-3,-9,-9]],[[4,9,-1,-1,-5,7,4,2,10,7,9,3],[-3,10,-1,-5,4,-8,-3,9,7,-1,6,9],[7,-9,-8,-6,-9,3,5,6,1,4,2,6],[-9,-2,-10,3,9,-4,4,-7,6,4,7,-1],[-1,4,8,3,-7,-2,-10,-8,9,-5,4,8],[2,-1,2,-9,7,-6,-3,2,-6,1,-1,4],[-1,-3,-10,4,2,1,7,7,-3,-9,-4,10],[-5,-7,-10,-6,-9,-7,-1,3,6,7,5,-7],[9,-7,-5,6,-10,6,-5,2,-3,-4,-9,8]],[[-2,9,3,6,-2,-6,1,-8,-4,-10,9,2],[2,8,3,-7,3,2,3,-9,-2,5,6,4],[-10,-10,10,-2,-7,4,-6,-7,-10,-6,-9,-10],[-1,-4,-8,8,7,-8,-9,-1,-1,-10,-7,-10],[6,-2,3,5,6,-3,-2,-4,-9,7,-5,6],[-3,-4,3,-7,-10,-3,-10,-8,-2,5,-2,-4],[-3,8,-9,-3,3,5,1,-5,3,-5,8,3],[4,5,-9,6,-10,-10,-3,5,10,9,4,-4],[4,3,-7,-4,-4,-9,-8,7,-3,10,1,9]],[[-7,-5,-6,9,-2,-2,9,-10,-6,8,-5,-3],[3,2,9,5,4,7,3,-10,8,-4,9,-2],[2,-9,4,-5,3,10,1,-8,-9,6,10,-7],[-7,7,-4,3,8,4,3,-10,-9,10,8,-6],[10,-9,6,-9,6,1,5,-7,-5,9,-2,-4],[-1,-10,2,-8,-6,7,2,8,-3,9,2,-3],[8,-5,-2,9,7,4,3,-6,-8,4,-8,-9],[3,9,3,4,-3,-2,-2,-10,-8,8,6,-4],[-6,2,1,3,9,-9,3,4,4,4,-6,-3]],[[-9,-8,5,-7,10,-5,3,7,1,4,1,1],[-5,9,1,8,5,5,7,2,-3,10,-4,-10],[5,10,-6,-1,-8,-4,4,-9,7,-10,-5,-4],[9,6,3,10,-2,5,-1,-8,-9,-8,-2,4],[10,-4,6,5,1,3,-9,-3,-3,-8,-5,5],[-9,-8,9,-2,6,6,-3,-1,4,10,5,6],[-10,-4,1,10,2,2,-10,2,10,1,-9,-8],[4,-6,-1,-9,-5,9,-4,-7,-7,-10,1,4],[-10,-5,-7,1,2,2,-8,-8,6,10,-4,-6]],[[5,-9,-8,8,-10,-8,-9,-8,-4,6,-1,-6],[10,5,-4,9,7,-8,3,-6,10,-1,10,-1],[10,-6,-2,6,-10,-9,3,6,6,-6,9,-5],[3,9,5,-8,7,-6,8,-4,2,-5,-1,-5],[-6,-9,3,3,10,-1,-1,-10,5,-9,7,-1],[7,5,8,7,3,8,-10,5,-4,4,5,6],[-1,3,8,-8,2,5,7,6,9,-7,-7,-8],[-9,8,8,6,-9,-9,2,6,-3,6,4,-10],[-5,2,9,5,-2,-6,7,2,-10,6,10,-6]],[[4,5,-3,1,-1,-2,-2,-2,1,9,-7,-7],[1,9,-5,6,-8,-9,5,-2,2,-9,-2,3],[9,3,-2,-5,4,-4,-2,8,1,-2,7,3],[8,8,-4,-5,-2,1,9,-6,-3,-1,3,2],[7,10,-7,-5,-6,-7,3,-3,2,-6,-3,1],[-5,8,2,-3,5,-4,6,-1,2,3,2,8],[-2,-5,9,1,-8,3,1,10,-9,2,2,8],[-1,-9,6,7,4,-5,7,8,-6,-7,6,5],[-2,1,-2,9,-9,-8,-6,5,8,4,5,-3]],[[4,8,-9,-7,3,4,8,-1,-2,4,-6,7],[-8,-1,2,3,-8,-7,-5,-8,2,-2,-7,-9],[-1,-6,-9,-3,5,-9,-2,4,3,-6,4,5],[-8,-8,1,4,8,3,5,6,1,-9,-8,-10],[-2,1,10,4,4,-3,-9,1,8,-7,-9,5],[8,3,-4,-1,1,4,8,9,10,-1,10,-6],[-5,3,6,5,1,4,-3,6,6,7,-8,8],[-10,-8,-2,-1,9,-10,-4,-3,-5,2,1,-3],[-8,3,-9,-5,-1,-9,9,-9,-4,3,7,2]],[[-2,-1,-4,2,-5,7,7,2,7,2,-9,-4],[3,10,-3,2,-9,-10,7,5,8,-7,6,-6],[1,8,-10,-5,-10,-1,-9,10,-3,-1,4,-4],[9,-9,1,7,3,1,8,4,-1,10,-7,-6],[-1,-3,-6,-9,-10,-10,-4,-10,4,8,-7,7],[9,-8,8,-9,2,5,-10,-2,3,-1,1,-3],[5,5,4,-2,1,-9,3,-1,-1,4,3,2],[-2,-2,-4,-7,6,3,-6,-5,4,-8,-4,-3],[-5,6,6,3,-1,-10,2,4,-1,-10,-1,-6]]], dtype = "int32")#candidate|8688|(16, 9, 12)|const|int32
bop_8689 = relay.less_equal(var_8687.astype('bool'), relay.reshape(const_8688.astype('bool'), relay.shape_of(var_8687))) # shape=(16, 9, 12)
bop_8693 = relay.greater_equal(const_8688.astype('bool'), relay.reshape(var_8687.astype('bool'), relay.shape_of(const_8688))) # shape=(16, 9, 12)
output = relay.Tuple([bop_8689,bop_8693,])
output2 = relay.Tuple([bop_8689,bop_8693,])
func_8696 = relay.Function([var_8687,], output)
mod['func_8696'] = func_8696
mod = relay.transform.InferType()(mod)
mutated_mod['func_8696'] = func_8696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8697 = relay.var("var_8697", dtype = "int32", shape = (16, 9, 12))#candidate|8697|(16, 9, 12)|var|int32
func_8696_call = mutated_mod.get_global_var('func_8696')
call_8698 = func_8696_call(var_8697)
output = call_8698
func_8699 = relay.Function([var_8697], output)
mutated_mod['func_8699'] = func_8699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5587_call = mod.get_global_var('func_5587')
func_5589_call = mutated_mod.get_global_var('func_5589')
call_8785 = func_5587_call()
call_8786 = func_5587_call()
output = relay.Tuple([call_8785,])
output2 = relay.Tuple([call_8786,])
func_8793 = relay.Function([], output)
mod['func_8793'] = func_8793
mod = relay.transform.InferType()(mod)
output = func_8793()
func_8794 = relay.Function([], output)
mutated_mod['func_8794'] = func_8794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8347_call = mod.get_global_var('func_8347')
func_8349_call = mutated_mod.get_global_var('func_8349')
call_8795 = relay.TupleGetItem(func_8347_call(), 3)
call_8796 = relay.TupleGetItem(func_8349_call(), 3)
output = relay.Tuple([call_8795,])
output2 = relay.Tuple([call_8796,])
func_8801 = relay.Function([], output)
mod['func_8801'] = func_8801
mod = relay.transform.InferType()(mod)
mutated_mod['func_8801'] = func_8801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8801_call = mutated_mod.get_global_var('func_8801')
call_8802 = func_8801_call()
output = call_8802
func_8803 = relay.Function([], output)
mutated_mod['func_8803'] = func_8803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4489_call = mod.get_global_var('func_4489')
func_4490_call = mutated_mod.get_global_var('func_4490')
call_8842 = relay.TupleGetItem(func_4489_call(), 0)
call_8843 = relay.TupleGetItem(func_4490_call(), 0)
func_5547_call = mod.get_global_var('func_5547')
func_5551_call = mutated_mod.get_global_var('func_5551')
var_8849 = relay.var("var_8849", dtype = "float32", shape = (110, 6))#candidate|8849|(110, 6)|var|float32
var_8850 = relay.var("var_8850", dtype = "float64", shape = ())#candidate|8850|()|var|float64
call_8848 = relay.TupleGetItem(func_5547_call(relay.reshape(var_8849.astype('float32'), [330, 2]), relay.reshape(var_8850.astype('float64'), []), ), 4)
call_8851 = relay.TupleGetItem(func_5551_call(relay.reshape(var_8849.astype('float32'), [330, 2]), relay.reshape(var_8850.astype('float64'), []), ), 4)
output = relay.Tuple([call_8842,call_8848,var_8849,var_8850,])
output2 = relay.Tuple([call_8843,call_8851,var_8849,var_8850,])
func_8857 = relay.Function([var_8849,var_8850,], output)
mod['func_8857'] = func_8857
mod = relay.transform.InferType()(mod)
mutated_mod['func_8857'] = func_8857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8857_call = mutated_mod.get_global_var('func_8857')
var_8859 = relay.var("var_8859", dtype = "float32", shape = (110, 6))#candidate|8859|(110, 6)|var|float32
var_8860 = relay.var("var_8860", dtype = "float64", shape = ())#candidate|8860|()|var|float64
call_8858 = func_8857_call(var_8859,var_8860,)
output = call_8858
func_8861 = relay.Function([var_8859,var_8860,], output)
mutated_mod['func_8861'] = func_8861
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8906 = relay.var("var_8906", dtype = "float32", shape = (9, 6, 1))#candidate|8906|(9, 6, 1)|var|float32
uop_8907 = relay.rsqrt(var_8906.astype('float32')) # shape=(9, 6, 1)
bop_8909 = relay.add(uop_8907.astype('int32'), relay.reshape(var_8906.astype('int32'), relay.shape_of(uop_8907))) # shape=(9, 6, 1)
bop_8931 = relay.bitwise_xor(bop_8909.astype('uint8'), relay.reshape(uop_8907.astype('uint8'), relay.shape_of(bop_8909))) # shape=(9, 6, 1)
bop_8935 = relay.equal(bop_8931.astype('bool'), relay.reshape(uop_8907.astype('bool'), relay.shape_of(bop_8931))) # shape=(9, 6, 1)
uop_8944 = relay.log2(bop_8909.astype('float32')) # shape=(9, 6, 1)
bop_8951 = relay.right_shift(uop_8944.astype('uint16'), relay.reshape(bop_8909.astype('uint16'), relay.shape_of(uop_8944))) # shape=(9, 6, 1)
bop_8957 = relay.greater(bop_8951.astype('bool'), relay.reshape(uop_8944.astype('bool'), relay.shape_of(bop_8951))) # shape=(9, 6, 1)
output = relay.Tuple([bop_8935,bop_8957,])
output2 = relay.Tuple([bop_8935,bop_8957,])
func_8977 = relay.Function([var_8906,], output)
mod['func_8977'] = func_8977
mod = relay.transform.InferType()(mod)
var_8978 = relay.var("var_8978", dtype = "float32", shape = (9, 6, 1))#candidate|8978|(9, 6, 1)|var|float32
output = func_8977(var_8978)
func_8979 = relay.Function([var_8978], output)
mutated_mod['func_8979'] = func_8979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6903_call = mod.get_global_var('func_6903')
func_6904_call = mutated_mod.get_global_var('func_6904')
call_8983 = relay.TupleGetItem(func_6903_call(), 0)
call_8984 = relay.TupleGetItem(func_6904_call(), 0)
output = call_8983
output2 = call_8984
func_9003 = relay.Function([], output)
mod['func_9003'] = func_9003
mod = relay.transform.InferType()(mod)
mutated_mod['func_9003'] = func_9003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9003_call = mutated_mod.get_global_var('func_9003')
call_9004 = func_9003_call()
output = call_9004
func_9005 = relay.Function([], output)
mutated_mod['func_9005'] = func_9005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7307_call = mod.get_global_var('func_7307')
func_7309_call = mutated_mod.get_global_var('func_7309')
call_9063 = relay.TupleGetItem(func_7307_call(), 1)
call_9064 = relay.TupleGetItem(func_7309_call(), 1)
uop_9086 = relay.cos(call_9063.astype('float32')) # shape=(3, 2, 15)
uop_9088 = relay.cos(call_9064.astype('float32')) # shape=(3, 2, 15)
output = relay.Tuple([uop_9086,])
output2 = relay.Tuple([uop_9088,])
func_9110 = relay.Function([], output)
mod['func_9110'] = func_9110
mod = relay.transform.InferType()(mod)
mutated_mod['func_9110'] = func_9110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9110_call = mutated_mod.get_global_var('func_9110')
call_9111 = func_9110_call()
output = call_9111
func_9112 = relay.Function([], output)
mutated_mod['func_9112'] = func_9112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4349_call = mod.get_global_var('func_4349')
func_4350_call = mutated_mod.get_global_var('func_4350')
call_9121 = func_4349_call()
call_9122 = func_4349_call()
output = relay.Tuple([call_9121,])
output2 = relay.Tuple([call_9122,])
func_9127 = relay.Function([], output)
mod['func_9127'] = func_9127
mod = relay.transform.InferType()(mod)
mutated_mod['func_9127'] = func_9127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9127_call = mutated_mod.get_global_var('func_9127')
call_9128 = func_9127_call()
output = call_9128
func_9129 = relay.Function([], output)
mutated_mod['func_9129'] = func_9129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6830_call = mod.get_global_var('func_6830')
func_6831_call = mutated_mod.get_global_var('func_6831')
call_9153 = relay.TupleGetItem(func_6830_call(), 1)
call_9154 = relay.TupleGetItem(func_6831_call(), 1)
output = relay.Tuple([call_9153,])
output2 = relay.Tuple([call_9154,])
func_9157 = relay.Function([], output)
mod['func_9157'] = func_9157
mod = relay.transform.InferType()(mod)
output = func_9157()
func_9158 = relay.Function([], output)
mutated_mod['func_9158'] = func_9158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9210 = relay.var("var_9210", dtype = "float32", shape = (13, 8, 8))#candidate|9210|(13, 8, 8)|var|float32
var_9211 = relay.var("var_9211", dtype = "float32", shape = (13, 8, 8))#candidate|9211|(13, 8, 8)|var|float32
bop_9212 = relay.power(var_9210.astype('float32'), relay.reshape(var_9211.astype('float32'), relay.shape_of(var_9210))) # shape=(13, 8, 8)
func_5895_call = mod.get_global_var('func_5895')
func_5897_call = mutated_mod.get_global_var('func_5897')
var_9220 = relay.var("var_9220", dtype = "float64", shape = (110,))#candidate|9220|(110,)|var|float64
call_9219 = relay.TupleGetItem(func_5895_call(relay.reshape(var_9220.astype('float64'), [110,])), 4)
call_9221 = relay.TupleGetItem(func_5897_call(relay.reshape(var_9220.astype('float64'), [110,])), 4)
output = relay.Tuple([bop_9212,call_9219,var_9220,])
output2 = relay.Tuple([bop_9212,call_9221,var_9220,])
func_9225 = relay.Function([var_9210,var_9211,var_9220,], output)
mod['func_9225'] = func_9225
mod = relay.transform.InferType()(mod)
mutated_mod['func_9225'] = func_9225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9225_call = mutated_mod.get_global_var('func_9225')
var_9227 = relay.var("var_9227", dtype = "float32", shape = (13, 8, 8))#candidate|9227|(13, 8, 8)|var|float32
var_9228 = relay.var("var_9228", dtype = "float32", shape = (13, 8, 8))#candidate|9228|(13, 8, 8)|var|float32
var_9229 = relay.var("var_9229", dtype = "float64", shape = (110,))#candidate|9229|(110,)|var|float64
call_9226 = func_9225_call(var_9227,var_9228,var_9229,)
output = call_9226
func_9230 = relay.Function([var_9227,var_9228,var_9229,], output)
mutated_mod['func_9230'] = func_9230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9244 = relay.var("var_9244", dtype = "float64", shape = (8, 13, 2))#candidate|9244|(8, 13, 2)|var|float64
uop_9245 = relay.asin(var_9244.astype('float64')) # shape=(8, 13, 2)
output = relay.Tuple([uop_9245,])
output2 = relay.Tuple([uop_9245,])
func_9251 = relay.Function([var_9244,], output)
mod['func_9251'] = func_9251
mod = relay.transform.InferType()(mod)
mutated_mod['func_9251'] = func_9251
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9252 = relay.var("var_9252", dtype = "float64", shape = (8, 13, 2))#candidate|9252|(8, 13, 2)|var|float64
func_9251_call = mutated_mod.get_global_var('func_9251')
call_9253 = func_9251_call(var_9252)
output = call_9253
func_9254 = relay.Function([var_9252], output)
mutated_mod['func_9254'] = func_9254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4349_call = mod.get_global_var('func_4349')
func_4350_call = mutated_mod.get_global_var('func_4350')
call_9259 = func_4349_call()
call_9260 = func_4349_call()
output = call_9259
output2 = call_9260
func_9263 = relay.Function([], output)
mod['func_9263'] = func_9263
mod = relay.transform.InferType()(mod)
output = func_9263()
func_9264 = relay.Function([], output)
mutated_mod['func_9264'] = func_9264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8109_call = mod.get_global_var('func_8109')
func_8111_call = mutated_mod.get_global_var('func_8111')
call_9291 = relay.TupleGetItem(func_8109_call(), 0)
call_9292 = relay.TupleGetItem(func_8111_call(), 0)
output = relay.Tuple([call_9291,])
output2 = relay.Tuple([call_9292,])
func_9297 = relay.Function([], output)
mod['func_9297'] = func_9297
mod = relay.transform.InferType()(mod)
mutated_mod['func_9297'] = func_9297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9297_call = mutated_mod.get_global_var('func_9297')
call_9298 = func_9297_call()
output = call_9298
func_9299 = relay.Function([], output)
mutated_mod['func_9299'] = func_9299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5600_call = mod.get_global_var('func_5600')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_9327 = func_5600_call()
call_9328 = func_5600_call()
func_9110_call = mod.get_global_var('func_9110')
func_9112_call = mutated_mod.get_global_var('func_9112')
call_9331 = relay.TupleGetItem(func_9110_call(), 0)
call_9332 = relay.TupleGetItem(func_9112_call(), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3736_call = mutated_mod.get_global_var('func_3736')
const_9334 = relay.const([[-2.100652,4.992248,6.797832,-0.449776,7.940840,-9.203596,-3.569806,-5.009846,-7.806295,-3.652669,-0.819971,-6.588334,4.882038,-2.069660,-7.009176,-1.264396,-7.720746,5.518104,-4.894995,0.346860,3.510544,5.110880,-9.301406,-0.057886,5.409275,-4.482066,3.370910,-3.310058,-4.701056,-8.584226,5.803759,9.593467,-9.539776,-3.829596,-6.691063,-8.231129,1.559989,0.070109,-2.193019,-0.821668,-3.464190,8.177543,0.942974,1.939320,-7.220543,0.755073,-5.648751,7.896374,0.822173,-9.668054,-8.112035,6.893722,-8.165637,0.979591,-1.898070,-1.789905,-2.562115,-8.108628,0.301592,-5.554644,-5.338523,9.694729,-0.326604,3.633819,-5.576588,-7.924284,4.672979,-2.156894,-3.445158,-2.054132,-7.580913,-5.330476,-0.356838,-0.107996,-3.622918,-6.378199,-9.813551,0.051327,-5.960060,8.766096,-7.931215,7.051969,0.457456,4.314118,5.684436,9.762223,-9.855316,8.469657,-7.607163,-2.045740,-3.853889,8.818540,7.671005,1.226181,-1.636068,-9.273186,-9.413042,-4.430651,-3.367268,-9.718456,7.336159,0.744102,7.357024,-7.210697,-1.548065,-9.135618,0.695773,-2.506586,-0.473832,7.674224,-0.877795,-0.926702,7.040136,-9.876550,-5.367962,-0.391871,-8.183933,-3.372505,-5.148925,-9.386830,9.987277,5.721548,-5.612382,8.718651,2.022347,0.782140,7.926007,7.456014,-0.646268,-1.477953,-5.032783,-8.213013,-3.939516,-7.920530,-7.449098,4.457349,7.707614,-1.818712,-2.408388,-0.634193,-1.291456,6.058660,2.776182,2.765640,5.409270,2.975022,-0.465256,-3.545810,-8.627467,8.628751,6.374615,-2.515138,7.618980,0.378166,9.253357,3.976131,9.016774,2.015182,9.119242,6.547296,-8.828111,-6.811020,-7.035586,9.445065,1.035680,2.935990,5.623504,7.871161,5.297277,0.356646,3.874084,-2.464114,9.487973,3.851497,-1.847590,9.146654,1.170522,3.012556,1.567382,-5.221598,9.438294,1.377917,-0.543834,0.250287,7.206460,-9.112160,-0.906908,-9.972607,-0.447802,-9.448874,-8.191118,7.759871,-6.521830,4.121784,7.200496,-8.093160,-4.351119,0.703782,8.057468,-7.736300,3.874976,9.081548,0.561830,-1.514967,8.903830,0.373698,-7.121776,-4.284117,3.179894,-7.695051,9.704314,-0.250817,1.283927,-1.537469,-7.244387,4.648666,8.853410,0.711729,-9.421606,-6.343772,0.694250,4.165138,-2.046714,-2.665206,-2.322632,-1.110624,9.714332,8.013911,7.533614,1.977290,-4.240103,6.089514,8.804286,-6.303985,-2.640451,-8.582379,-8.737178,-8.953174,3.742026,5.812434,1.832625,5.165951,-5.456723,1.270903,1.033515,7.108920,-5.703140,8.373333,-3.327767,6.965352,3.473659,-2.342642,-5.712077,-8.734575,9.183843,2.076658,-0.234630,3.331654,2.762481,-8.486314,-0.550422,-5.738183,-7.722201,-9.376307,9.295746,-0.990105,7.563181,5.642889,3.937953,2.383801,6.875295,5.367605,-6.471317,-8.480087,-0.729452,-8.092075,-1.861761,0.374686,-5.282036,6.188121,1.504826,-3.553215,-5.446328,-1.009456,-9.224447,-4.752139,-9.946231,6.759676,2.763855,-9.633259,-6.744310,-0.945344,3.491453,8.682185,9.519154,-9.621564,-2.602230,-3.242611,-4.916276,-8.745148,-5.310581,-6.763946,9.843149,8.085678,0.001366,-5.977669,-0.724969,-5.542073,-0.868026,-2.292580,4.896742,-9.698829],[5.319230,-5.905577,-0.104721,-0.139230,-9.487231,2.665040,-7.698013,-9.841841,2.376224,4.594603,2.259807,5.208985,-0.085541,5.832127,-5.223772,7.120691,-6.345277,2.444410,6.806807,-9.976668,-2.154592,6.542306,-7.549204,-3.660425,-4.322114,-3.208612,-5.365062,0.979061,2.076167,-6.204367,-0.756295,8.177906,9.202489,0.219023,8.222649,-9.029187,-1.691463,-7.520783,8.931413,-0.162352,6.342492,2.530959,-7.046840,-8.938397,-5.356066,-7.939701,-0.800902,6.043941,-3.768910,-3.600232,-7.439216,-4.271430,-9.278348,-2.264745,5.124675,9.573378,8.726309,-7.713520,5.754144,5.110413,7.325335,1.162661,1.787787,-1.408702,2.553889,4.803174,5.461247,-9.068350,4.599759,-9.158015,2.045964,9.739490,-1.041030,2.967836,-3.944383,7.667774,-3.463405,3.738590,-0.875267,1.945252,7.672153,8.138917,-3.514418,-3.550583,-6.534812,3.067866,7.977502,-5.319012,-7.203248,4.349498,-5.703495,1.349089,3.424853,1.322246,-8.087713,-5.912626,2.890119,-8.670533,1.842131,8.375323,5.772868,-1.416693,1.849441,6.328225,-7.986142,-9.543369,7.655694,7.402783,2.314606,-4.715808,7.614631,2.188632,7.199869,2.666346,-2.346844,-9.190222,5.299803,-3.830461,-7.354499,-4.151611,0.890348,3.421741,-6.963101,5.710845,1.626412,2.004335,-9.214893,-7.950119,3.577313,2.108152,-5.015515,1.890706,-5.672568,6.288107,8.179008,8.068864,-0.896400,-9.348103,3.110302,-3.576047,9.806459,2.566349,-9.325079,2.040913,1.231794,-9.672298,0.022122,1.781974,0.310609,-6.188663,4.846919,9.982262,-1.049464,-9.336396,-7.801617,3.015315,0.199659,2.733530,-7.736376,0.617354,2.789651,1.196021,3.457754,-8.021751,7.291381,-5.371565,-1.064501,0.892449,5.274561,-5.516406,-0.172126,3.397512,1.181097,-9.778006,-5.251960,1.071944,2.499986,-8.022685,-1.408584,9.937036,5.039265,-4.036223,-8.787186,-9.932122,5.782980,9.462063,-8.328286,4.965592,5.643703,6.845145,9.890278,-0.007172,-3.040091,-6.904301,9.855129,-2.193676,9.864238,7.809598,-6.319660,1.576143,-5.261763,-9.590274,4.987533,-5.714136,8.282672,-0.433210,2.252948,7.448626,3.305202,-3.313092,3.351101,7.272413,0.604290,-3.830492,2.664920,4.038978,-0.013650,-2.695160,-1.011339,7.505527,3.884754,-6.126233,-1.574193,-9.691196,3.348881,-9.513955,6.596512,2.030897,-1.153093,1.309958,2.534283,-5.701829,-4.262324,-4.677389,9.763740,-6.629615,9.621207,5.707412,-6.546065,-2.908936,-2.553691,-1.034864,-9.980605,-6.000767,-3.834130,-1.347748,8.890227,2.715020,-5.858664,-1.842072,0.876705,-4.689234,4.707563,-3.118199,0.564655,-5.156825,-3.169072,4.627967,-3.556646,5.379167,6.228683,4.860916,-5.944421,-0.720851,-4.270650,3.359506,5.641730,-4.946100,8.171109,-2.445337,3.041365,2.523572,-6.286948,7.944232,-2.157864,8.709789,-9.515619,-1.046559,1.439184,5.581908,0.399396,-4.447874,-4.114540,-3.909259,0.282855,-6.955839,6.518852,-5.982935,4.748866,-5.235653,5.726178,8.459441,-1.371218,-5.457852,4.026751,3.893501,-5.459379,9.959057,1.378072,2.559181,0.835871,4.793462,0.662537,-4.221588,0.889511,-6.412730,-0.390779,5.947010,-5.267797,-6.785702,2.525246,-6.122983]], dtype = "float32")#candidate|9334|(2, 312)|const|float32
const_9335 = relay.const([8.348396,-3.818075,-9.490065,9.925863,1.843511,-2.234440,2.812409,4.993867,5.138095,-7.917596,9.915696,5.650778,2.627565,-3.360206,2.450303,7.557867,-1.384632,2.128346,5.967805,-8.215082,-7.514688,-2.492189,-7.574545,1.229388,-4.519281,1.413291,3.160680,-0.354563,-5.983409,0.356318,-2.943669,7.120724,-3.636006,-7.644448,0.370670,5.212841,3.235530,1.304362,7.431453,0.592922,2.841441,1.358313,6.340525,3.364513,3.463967,-3.091557,8.824808,-1.837269,-2.332501,1.346612,-0.158010,-9.278097,-7.724560,3.281689,-3.005414,7.176003,7.044090,-6.317956,9.209560,-4.429784,0.212842,-7.385656,-1.973543,-6.844406,8.300324,2.172136,-2.832967,-9.672159,6.592061,8.299038,-0.716442,7.565255,0.209087,6.646387,2.543880,5.019611,-1.928734,1.117494,5.446140,5.461514,-7.090237,-3.318009,-6.124848,4.253680,-1.770734,-0.801859,-0.770520,-0.323670,8.973717,-6.182006,9.022459,9.634957,3.505193,9.351714,9.065227,-4.947793,7.553568,-6.511025,4.259617,6.850802], dtype = "float64")#candidate|9335|(100,)|const|float64
call_9333 = relay.TupleGetItem(func_3733_call(relay.reshape(const_9334.astype('float32'), [624,]), relay.reshape(const_9335.astype('float64'), [2, 10, 5]), ), 6)
call_9336 = relay.TupleGetItem(func_3736_call(relay.reshape(const_9334.astype('float32'), [624,]), relay.reshape(const_9335.astype('float64'), [2, 10, 5]), ), 6)
output = relay.Tuple([call_9327,call_9331,call_9333,const_9334,const_9335,])
output2 = relay.Tuple([call_9328,call_9332,call_9336,const_9334,const_9335,])
func_9341 = relay.Function([], output)
mod['func_9341'] = func_9341
mod = relay.transform.InferType()(mod)
mutated_mod['func_9341'] = func_9341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9341_call = mutated_mod.get_global_var('func_9341')
call_9342 = func_9341_call()
output = call_9342
func_9343 = relay.Function([], output)
mutated_mod['func_9343'] = func_9343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6308_call = mod.get_global_var('func_6308')
func_6310_call = mutated_mod.get_global_var('func_6310')
call_9361 = relay.TupleGetItem(func_6308_call(), 0)
call_9362 = relay.TupleGetItem(func_6310_call(), 0)
func_5895_call = mod.get_global_var('func_5895')
func_5897_call = mutated_mod.get_global_var('func_5897')
const_9392 = relay.const([-7.084038,-4.306171,-7.132879,-9.980497,1.095844,0.914201,-3.611598,-6.643404,5.702227,2.794045,1.722756,7.748304,-9.540623,2.294478,4.902550,-6.204381,3.923086,-6.443572,9.321032,-6.663840,-2.844569,-5.948014,0.635951,8.888611,-4.593558,7.944379,6.955519,7.219262,3.796084,3.290552,0.190068,4.270397,-4.626171,-6.446365,-8.902349,5.354384,-7.940087,-0.290098,-4.078132,-7.220936,-7.370478,-6.297233,2.335497,2.924257,-7.537464,4.055900,-4.183168,-3.983749,-8.608004,9.106807,3.515625,5.976672,-2.265560,3.192747,4.041403,-2.183334,-5.296347,1.422410,-5.711751,-3.150787,-2.287701,-3.712985,-3.629525,8.208325,2.532386,-3.849626,8.473225,-0.076921,8.697835,-9.623554,-1.009283,-7.761389,3.338976,-8.158499,-0.163719,-6.536503,-6.755464,9.098505,2.441197,7.922724,1.797714,1.307047,-1.192963,5.359838,-4.819893,-2.093981,-3.880115,9.843445,8.691627,7.540162,-5.170276,-3.226846,-7.239602,-7.553098,-3.142095,-8.013302,8.779251,6.018778,0.263835,0.061313,-3.055298,-7.496084,-3.933712,1.675071,5.442657,3.734041,-7.175763,-8.023837,5.727651,2.681732], dtype = "float64")#candidate|9392|(110,)|const|float64
call_9391 = relay.TupleGetItem(func_5895_call(relay.reshape(const_9392.astype('float64'), [110,])), 0)
call_9393 = relay.TupleGetItem(func_5897_call(relay.reshape(const_9392.astype('float64'), [110,])), 0)
output = relay.Tuple([call_9361,call_9391,const_9392,])
output2 = relay.Tuple([call_9362,call_9393,const_9392,])
func_9398 = relay.Function([], output)
mod['func_9398'] = func_9398
mod = relay.transform.InferType()(mod)
mutated_mod['func_9398'] = func_9398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9398_call = mutated_mod.get_global_var('func_9398')
call_9399 = func_9398_call()
output = call_9399
func_9400 = relay.Function([], output)
mutated_mod['func_9400'] = func_9400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4021_call = mod.get_global_var('func_4021')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_9428 = relay.TupleGetItem(func_4021_call(), 1)
call_9429 = relay.TupleGetItem(func_4023_call(), 1)
func_2187_call = mod.get_global_var('func_2187')
func_2190_call = mutated_mod.get_global_var('func_2190')
var_9441 = relay.var("var_9441", dtype = "int16", shape = (2, 96))#candidate|9441|(2, 96)|var|int16
var_9442 = relay.var("var_9442", dtype = "float64", shape = ())#candidate|9442|()|var|float64
call_9440 = relay.TupleGetItem(func_2187_call(relay.reshape(var_9441.astype('int16'), [4, 4, 12]), relay.reshape(var_9442.astype('float64'), []), ), 0)
call_9443 = relay.TupleGetItem(func_2190_call(relay.reshape(var_9441.astype('int16'), [4, 4, 12]), relay.reshape(var_9442.astype('float64'), []), ), 0)
output = relay.Tuple([call_9428,call_9440,var_9441,var_9442,])
output2 = relay.Tuple([call_9429,call_9443,var_9441,var_9442,])
func_9446 = relay.Function([var_9441,var_9442,], output)
mod['func_9446'] = func_9446
mod = relay.transform.InferType()(mod)
mutated_mod['func_9446'] = func_9446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9446_call = mutated_mod.get_global_var('func_9446')
var_9448 = relay.var("var_9448", dtype = "int16", shape = (2, 96))#candidate|9448|(2, 96)|var|int16
var_9449 = relay.var("var_9449", dtype = "float64", shape = ())#candidate|9449|()|var|float64
call_9447 = func_9446_call(var_9448,var_9449,)
output = call_9447
func_9450 = relay.Function([var_9448,var_9449,], output)
mutated_mod['func_9450'] = func_9450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3639_call = mod.get_global_var('func_3639')
func_3641_call = mutated_mod.get_global_var('func_3641')
call_9489 = relay.TupleGetItem(func_3639_call(), 0)
call_9490 = relay.TupleGetItem(func_3641_call(), 0)
func_8439_call = mod.get_global_var('func_8439')
func_8441_call = mutated_mod.get_global_var('func_8441')
call_9502 = relay.TupleGetItem(func_8439_call(), 0)
call_9503 = relay.TupleGetItem(func_8441_call(), 0)
var_9506 = relay.var("var_9506", dtype = "float64", shape = (110,))#candidate|9506|(110,)|var|float64
bop_9507 = relay.logical_xor(call_9489.astype('uint32'), relay.reshape(var_9506.astype('uint32'), relay.shape_of(call_9489))) # shape=(110,)
bop_9510 = relay.logical_xor(call_9490.astype('uint32'), relay.reshape(var_9506.astype('uint32'), relay.shape_of(call_9490))) # shape=(110,)
uop_9524 = relay.acos(call_9489.astype('float32')) # shape=(110,)
uop_9526 = relay.acos(call_9490.astype('float32')) # shape=(110,)
var_9539 = relay.var("var_9539", dtype = "float32", shape = (110,))#candidate|9539|(110,)|var|float32
bop_9540 = relay.logical_and(uop_9524.astype('bool'), relay.reshape(var_9539.astype('bool'), relay.shape_of(uop_9524))) # shape=(110,)
bop_9543 = relay.logical_and(uop_9526.astype('bool'), relay.reshape(var_9539.astype('bool'), relay.shape_of(uop_9526))) # shape=(110,)
output = relay.Tuple([call_9502,bop_9507,bop_9540,])
output2 = relay.Tuple([call_9503,bop_9510,bop_9543,])
func_9546 = relay.Function([var_9506,var_9539,], output)
mod['func_9546'] = func_9546
mod = relay.transform.InferType()(mod)
mutated_mod['func_9546'] = func_9546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9546_call = mutated_mod.get_global_var('func_9546')
var_9548 = relay.var("var_9548", dtype = "float64", shape = (110,))#candidate|9548|(110,)|var|float64
var_9549 = relay.var("var_9549", dtype = "float32", shape = (110,))#candidate|9549|(110,)|var|float32
call_9547 = func_9546_call(var_9548,var_9549,)
output = call_9547
func_9550 = relay.Function([var_9548,var_9549,], output)
mutated_mod['func_9550'] = func_9550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9263_call = mod.get_global_var('func_9263')
func_9264_call = mutated_mod.get_global_var('func_9264')
call_9604 = func_9263_call()
call_9605 = func_9263_call()
func_6063_call = mod.get_global_var('func_6063')
func_6065_call = mutated_mod.get_global_var('func_6065')
const_9612 = relay.const([[-8.038707,-4.111627,1.907686,-9.781480,9.871619,7.217826,-4.778907,3.387139,-7.364987,7.178103],[1.783879,-3.293500,1.267778,3.128504,0.635761,6.124709,-7.184654,-0.979538,7.821026,-7.753970],[-6.044756,8.270827,-6.758383,8.580468,-5.187430,6.970552,5.158899,-4.882780,2.090744,-7.377150],[4.527364,6.841604,0.073817,1.194518,-0.470263,3.520280,6.835390,6.535628,0.916404,-4.184246],[1.320256,-2.868156,-4.589017,-9.968601,-9.064903,-2.305159,-5.870038,3.156717,3.968702,3.428411],[-1.606928,0.990798,3.039270,-7.710730,4.517897,-2.951441,-2.714303,9.754300,0.176312,2.200804],[-2.243235,6.689450,7.676431,5.539608,3.015808,-3.428931,1.075943,8.170066,0.524216,-8.798616],[8.513669,5.197815,3.201039,-5.582857,-8.088057,-4.741796,8.094832,-7.409329,-7.656678,3.523200],[-9.234801,5.956647,4.111598,-7.430182,-1.484977,-8.207473,4.039972,-4.370673,-2.715962,1.863382],[-4.238884,-3.319555,9.390379,-5.390534,-7.095010,6.813015,5.116881,-2.706213,8.317358,3.241357],[2.531320,8.932190,-1.690765,1.011761,-8.136658,6.629443,-5.078650,-1.498156,-9.784432,2.286516]], dtype = "float64")#candidate|9612|(11, 10)|const|float64
call_9611 = relay.TupleGetItem(func_6063_call(relay.reshape(const_9612.astype('float64'), [110,])), 0)
call_9613 = relay.TupleGetItem(func_6065_call(relay.reshape(const_9612.astype('float64'), [110,])), 0)
func_3118_call = mod.get_global_var('func_3118')
func_3122_call = mutated_mod.get_global_var('func_3122')
const_9634 = relay.const([-4.048011,-0.126957,-1.615491,-3.755420,8.284167,-3.328034,-9.823016,7.410654,-2.276300,2.780295,-6.899388,-1.694322,8.095583,-0.600589,-1.363172,-4.628356,-0.913789,-8.395267,0.936847,-1.607268,9.890650,1.567726,5.147777,-7.784448,3.388362,0.751310,8.058358,-0.063860,6.832621,0.177150,8.452576,-1.964196,-4.899031,-2.430646,-9.942085,7.279495,-7.509862,0.962052,1.574793,6.008028,8.203536,-5.407038,-9.886420,3.258364,5.243108,8.946449,-7.262977,-6.759749,-6.360333,-6.664427,7.400998,1.839004,-5.244193,-1.049908,-0.097134,-3.517460,-4.387187,-6.342131,-9.722751,2.846989,-8.925397,-0.094789,-4.345830,-0.630564,2.214197,9.269808,-8.732037,-7.155793,0.752534,-3.521593,-7.560266,2.563289,4.308375,7.935988,0.402309,4.496326,8.322291,-7.006283,-2.374648,0.265161,7.873579,-2.677874,1.169788,3.724230,1.692428,-2.587835,-5.076078,5.230890,-9.471974,6.411775,3.130389,1.433941,-5.979624,-9.371425,-3.941193,6.965625,0.620260,0.119088,-7.229272,0.297210], dtype = "float64")#candidate|9634|(100,)|const|float64
call_9633 = relay.TupleGetItem(func_3118_call(relay.reshape(const_9612.astype('float64'), [110,]), relay.reshape(const_9634.astype('float64'), [100,]), ), 1)
call_9635 = relay.TupleGetItem(func_3122_call(relay.reshape(const_9612.astype('float64'), [110,]), relay.reshape(const_9634.astype('float64'), [100,]), ), 1)
func_9341_call = mod.get_global_var('func_9341')
func_9343_call = mutated_mod.get_global_var('func_9343')
call_9641 = relay.TupleGetItem(func_9341_call(), 1)
call_9642 = relay.TupleGetItem(func_9343_call(), 1)
output = relay.Tuple([call_9604,call_9611,const_9612,call_9633,const_9634,call_9641,])
output2 = relay.Tuple([call_9605,call_9613,const_9612,call_9635,const_9634,call_9642,])
func_9659 = relay.Function([], output)
mod['func_9659'] = func_9659
mod = relay.transform.InferType()(mod)
mutated_mod['func_9659'] = func_9659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9659_call = mutated_mod.get_global_var('func_9659')
call_9660 = func_9659_call()
output = call_9660
func_9661 = relay.Function([], output)
mutated_mod['func_9661'] = func_9661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8109_call = mod.get_global_var('func_8109')
func_8111_call = mutated_mod.get_global_var('func_8111')
call_9722 = relay.TupleGetItem(func_8109_call(), 0)
call_9723 = relay.TupleGetItem(func_8111_call(), 0)
func_1598_call = mod.get_global_var('func_1598')
func_1602_call = mutated_mod.get_global_var('func_1602')
const_9727 = relay.const(9.627694, dtype = "float32")#candidate|9727|()|const|float32
call_9726 = func_1598_call(relay.reshape(const_9727.astype('float32'), []), relay.reshape(call_9722.astype('float32'), [1, 4, 7]), )
call_9728 = func_1598_call(relay.reshape(const_9727.astype('float32'), []), relay.reshape(call_9722.astype('float32'), [1, 4, 7]), )
output = relay.Tuple([call_9722,call_9726,const_9727,])
output2 = relay.Tuple([call_9723,call_9728,const_9727,])
func_9732 = relay.Function([], output)
mod['func_9732'] = func_9732
mod = relay.transform.InferType()(mod)
mutated_mod['func_9732'] = func_9732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9732_call = mutated_mod.get_global_var('func_9732')
call_9733 = func_9732_call()
output = call_9733
func_9734 = relay.Function([], output)
mutated_mod['func_9734'] = func_9734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8793_call = mod.get_global_var('func_8793')
func_8794_call = mutated_mod.get_global_var('func_8794')
call_9762 = relay.TupleGetItem(func_8793_call(), 0)
call_9763 = relay.TupleGetItem(func_8794_call(), 0)
var_9768 = relay.var("var_9768", dtype = "float64", shape = (110,))#candidate|9768|(110,)|var|float64
bop_9769 = relay.mod(call_9762.astype('float64'), relay.reshape(var_9768.astype('float64'), relay.shape_of(call_9762))) # shape=(110,)
bop_9772 = relay.mod(call_9763.astype('float64'), relay.reshape(var_9768.astype('float64'), relay.shape_of(call_9763))) # shape=(110,)
func_6713_call = mod.get_global_var('func_6713')
func_6717_call = mutated_mod.get_global_var('func_6717')
const_9780 = relay.const([-1.674650,9.980830,0.545348,6.428263,-9.840439,-2.671731,-3.189918,-9.552603,7.374442,0.359177,4.390664,2.194245,-3.674656,9.841542,0.574768,3.480782,8.459600,-0.995457,6.359710,-2.507902,-1.114297,-4.877387,-2.802544,-7.557496,-9.134704,9.242632,-8.943423,8.870090,-7.575628,-0.745694,1.521100,5.181231,2.120320,5.481343,-9.383929,-5.300218,-5.723116,0.052752,0.638703,9.068003,5.610902,9.261208,8.663679,-3.027942,1.560354,1.776534,-2.037449,-8.729487,-1.015110,-6.698122,8.975468,-5.523056,5.824902,-4.123681,7.478164,-9.823135,4.777935,-9.264138,-4.840966,-8.334769,-8.953812,9.049800,-4.539113,-6.321850,3.017582,6.235094,6.870324,7.163601,1.950919,-0.200983,6.215170,8.747476,-9.474005,7.349974,-5.569137,4.094764,1.746915,2.833069,-2.904806,-3.358936,9.446873,-4.779967,0.563796,0.949782,6.462373,-6.035156,3.581684,3.703616,6.404370,-9.040730,-9.212159,-4.873776,-1.252919,-7.383864,5.545613,1.373028,-6.585684,-0.116526,9.726700,5.717264,9.135812,6.463978,7.631363,-5.504568,0.085097,0.237221,-8.440538,0.163265,6.323505,1.581476,-1.976141,1.641034,-9.431134,1.024451,-6.680848,1.546703,-4.348712,-2.305438,2.586331,-0.910391,5.342301,0.057262,-1.007732,7.092897,-7.603000,-3.157255,8.317731,0.364550,1.011269,2.762263,6.502216,6.969622,0.881179,-4.868949,8.752299,8.301274,-6.489915,-1.446229,1.425978,-1.260753,1.742591,-2.049622,5.798427,-9.931471,-0.717889,-7.000906,-0.566314,4.480933,1.153501,2.831927,8.236845,5.913964,4.997466,-0.013387,1.777253,-8.880767,3.048285,7.732855,-4.055366,-5.570952,3.235232,4.014706,-0.790272,9.541999,-9.974646,-6.946738,3.400026,0.835239,-2.588448,1.921188,-0.272184,-6.195073,0.784993,-4.863581,4.957498,-1.723143,0.430424,8.617326,6.921524,0.309269,5.832499,8.623017,-4.966973,7.081472,-7.995441,-2.695396,-8.680049,-0.128524,9.930938,1.281907,3.912735,3.231366,6.370339,0.183293,-5.093994,-1.259034,-3.474402,-2.883648,-1.609176,5.819380,6.930038,-7.075466,-8.616688,0.220873,6.718356,7.380816,-8.441679,-5.368135,4.273177,-7.474673,-2.603876,1.082169,-6.323609,4.214998,9.308558,1.472535,4.988828,-8.595287,5.692963,3.992187,-5.517188,4.380292,7.613050,9.244875,1.355771,-1.500984,-0.942044,2.904813,-7.435722,-6.189213,1.131555,-5.139260,5.423411,1.715051,-7.042087,6.024580,6.527692,5.297161,-7.174208,8.043935,4.557536,-0.260879,0.387197,-6.007563,-8.245336,1.524269,5.368983,-5.047882,-6.247372,3.831725,-0.824592,5.770847,9.893826,2.849269,2.911505,-6.502417,-2.752267,5.842491,-3.799343,0.056376,-3.392443,-3.435297,-2.066961,-5.745970,-6.400441,6.323574,-8.867286,-2.258058,-3.579345,-5.521377,-1.632814,-3.649693,3.317086,-5.431764,3.420398,-1.075509,-4.794603,0.637600,-2.451248,0.120567,0.566626,8.984569,-1.141939,-7.647821,3.178190,-1.921681,0.850701,8.107030,-7.835741,-8.876513,0.477614,9.233536,2.502122,7.564685,-2.868288,7.874857,7.541764,-7.488938,-3.606137,-1.499111,4.375608,-6.469967,0.638408,5.440449,2.492760,-7.368294,-8.898775,4.595912,-6.965578,2.574056,7.072032,4.577059,-2.861718,-2.928398,-6.856837,-8.108904,-2.147929,-7.894735,-1.087898,8.037160,2.737130,3.129901,-6.385194,2.882056,2.101715,8.110943,3.884086,8.493079,-9.036933,0.498073,5.255525,-4.495755,-2.421840,2.994720,-7.040180,-9.088204,-7.763580,-1.531965,-5.489553,-6.563920,-6.867679,3.629224,-2.898487,8.296201,-5.562320,9.379427,1.881805,1.617154,-6.335258,-0.571142,-7.394602,-7.693667,-1.999911,6.407127,-0.495753,-5.717966,5.864126,4.926133,0.074879,5.419847,7.882029,2.627415,-2.254227,-5.089878,4.796266,-1.035353,9.886631,9.065196,2.246039,9.374423,-9.742361,-0.701719,5.561735,1.058738,3.754096,-8.867137,4.256752,7.404158,8.872698,-8.393013,-7.966357,-3.658413,7.781940,-6.166385,-6.866178,-6.249093,7.578943,-2.973828,-4.446260,9.468156,-6.997849,-1.365724,9.132809,-9.566342,3.524116,-4.979379,5.221839,-2.734537,-5.947854,1.672605,-8.143660,7.659752,-9.722180,-2.713341,5.318019,-2.316170,1.531782,4.630220,-5.412946,9.595974,-2.322142,-0.559967,-0.386282,-6.654608,2.623337,3.435710,5.589128,0.594381,6.664454,6.120366,-9.183469,-5.142823,-2.912081,-4.772298,3.060397,2.472380,7.490431,8.103270,-1.691475,-6.300049,2.128076,5.461563,-6.665639,7.604848,-4.109360,-9.256557,-7.778875,-4.386861,-9.371597,-0.526273,7.741455,2.684324,9.705336,-4.607799,-8.829925,6.219037,0.001301,4.935625,1.808542,0.858770,1.031216,-5.214076,-4.654653,-1.619030,-5.160988,5.217010,-4.213573,-8.726469,2.544150,7.500297,-0.878492,-3.502688,7.684665,0.572589,-8.696526,-0.726025,4.292405,6.158609,-4.946193,-5.187044,-2.255625,-3.379791,0.179339,-0.987196,2.673682,-4.607965,-2.633217,5.284729,-8.942381,1.047550,7.732066,-3.564087,-5.025894,4.724901,-1.867418,6.855775,3.096512,9.912463,6.237218,4.980069,-1.329253,-8.394391,-0.174350,-7.699643,-1.660140,5.499732,-8.068342,-4.019839,-7.081187,0.417931,-9.274652,3.707285,-0.994275,-5.404401,1.713922,-0.208696,5.969602,-2.393419,4.257822,9.198432,-6.516367,3.832999,-5.031615,-3.768927,0.415277,6.906305,-6.945635,8.036170,-4.941243,-7.840023,-1.823886,1.960361,8.571601,6.445973,-6.409859,5.942374,-7.589705,8.432972,-8.636464,3.934075,6.047147,5.577735,7.440455,-7.706722,-0.072893,2.980066,-1.563517,5.839122,0.294787,-2.940463,1.167419,-5.037233,-1.074917,-0.132817,3.542479,7.063988,1.727074,8.503873,8.738019,-7.200150,-2.290774,-8.151576,-3.468891,0.289915,9.176254,8.026029,6.819816,-4.103977,-3.833859,-8.393557,-6.584274,-2.802806,2.887430,-2.330503,-9.669047,-6.539269,9.972169,2.467670,-3.842348,2.078582,-1.894898,-8.767675,-9.431162,4.552724,-9.065358,2.359282,1.826564,-4.931042,4.698558,-4.968955,7.644074,-6.300900,0.965619,-8.237524,-9.428201,7.029318,-9.095684,-9.211731,-8.913202,8.095840,-3.109724,6.989421,0.086496,-2.217079], dtype = "float32")#candidate|9780|(594,)|const|float32
const_9781 = relay.const([5,2,7,-8,3,-4,-8,-3,10,9,4,1,-5,6,-5,2,8,-1,1,-3,5,1,2,4,7,-10,-5,7,-7,6,7,-1,-2,-9,2,-7,1,2,-5,-5,-8,-1,5,2,2,-5,-8,3,7,-4,6,-7,3,-8,4,9,10,6,10,9,-8,3,1,7,-10,8,-6,10,-2,6,-6,9,-8,3,-3,-2,-7,8,-2,5,-9,7,7,5,-10,7,-7,-1,-9,5,-7,4,3,-1,6,7,10,-1,3,-8,6,-6,10,-9,2,-3,-10,-2,-9,-10,-2,2,-10,10,-8,6,-4,8,2,6,-1,2,6,-6,8,1,2,-1,-6,-6,1,-8,-6,10,-4,-9,-5,-6,-4,7,-6,-1,10,1,-7,2,-10,-5,-7,-4,3,-3,6,-1,-2,4,7,-8,-1,4,-7,6,-7,6,7,-2,-5,1,6,4,10,-6,7,-3,3,6,4,-9,-4,4,5,4,-2,-3,-4,-6,7,1,-6,-4,-4,8,4,-10,2,-2,1,-9,8,3,9,8,3,-1,6,7,6,9,-5,-2,6,-6,-9,-1,-4,-3,-6,-10,2,10,-5,-9,4,-2,-8,8,8,10,8,8,-10,7,-2,6,6,-4,-3,-3,1,-8,2,5,-9,-1,10,8,-10,5,10,8,7,9,2,-7,-1,-6,-10,-7,7,5,-7,7,-8,9,-4,-5,6,-1,10,-5,-2,6,-3,-2,-10,10,-9,-5,9,-6,9,-4,-9,-7,-4,10,5,-9,-10,1,-7,7,7,-3,-6,-9,-2,3,-9,-8,5,10,-7,-8,-9,7,9,-2,-8,3,5,10,-5,9,-3,7,-7,8,6,-1,7,1,-3,-4,-9,6,9,1,9,7,7,2,1,-7,5,3,7,-10,6,-3,3,9,5,7,10,-10,10,-10,-1,9,7,10,6,4,7,9,7,3,9,-10,4,7,-1,6,-6,-7,-8,8,-10,8,-2,-9,-8,-2,2,8,-9,1,-2,1,-5,2,9,7,-4,7,3,-4,-8,-8,6,6,8,7,-6,9,-9,5,1,-7,9,1,-2,3,-1,8,-8,5,4,8,-10,-1,8,-7,8,-3,10,8,-9,1,5,-7,6,1,-4,9,-3,-5,4,9,-7,-10,-8,-8,1,-7,9,-1,8,2,-8,5,1,4,1,-9,8,5,8,-3,3,7,-5,-6,8,-6,10,2,3,-9,9,-3,7,-3,3,6,-5,9,-3,5,-4,-10,4,8,-7,-10,-4,3,4,6,1,5,-9,10,-9,3,-7,10,6,7,-4,2,-3,-9,3,4,1,2,2,-10,-6,-6,10,2,-3,-9,-5,5,6,-5,-1,-2,6,10,3,-1,-7,-2,3,2,3,3,4,8,-1,-8,-1,5,-6,7,9,10,5,2,8,-3,5,10,1,-9,10,5,2,1,6,-7,6,-8,1,-10,-4,-9,7,10,9,2,-9,-3,8,-8,1,-7,7,9,-5,-7,2,-10,7,-10,-9,8,-1,10,-6,-4,-6,-4,-6,10,-4,10,3,8,10,-8,10,5,-8,3,-5,-1,-7,5,7,-5,-2,-8,5,-7,-4,1,1,-7,5,5,6,1,10,-7,1,10,6,-10,-4,7,-4,-1,-6,-5,10,-1,5,-2,-7,-4,8,6,1,-7,5,-10,2,-3,10,9,10,-8,1,-2,8,1,-9,10,-4,-3,-10,-9,4,1,2,6,2,-8,6,3,5,10,2,-2,-8,7,-7,8,-10,9,-1,-3,1,-5,-9,-10,4,-8,9,-5,6,3,-10,-7,2,-2,1,3,5,8,4,-10,-8,-7,10,-2,-5,10,-7,-8,4,-9,3,8,10,4,6,4,-4,-10,2,1,-8,5,-9,-6,10,8,7,-3,-2,1,-1,-1,-6,9,5,-7,2,-10,-4,-6,4,-10,-9,-8,-8,-2,-5,-5,-6,-1,4,-3,10,9,-4,8,8,6,1,-2,-6,9,7,-2,-8,-3,-3,-1,4,6,-5,-3,-4,-4,-5,-3,1,2,-6,1,1,8,-2,6,-1,1,9,-10,-5,10,-1,2,-7,-9,3,6,-6,8,5,4,-8,-3,9,2,8,-5,-4,-2,-3,3,3,-10,6,-8,1,7,7,6,3,-1,1,1,-4,8,6,-3,-1,-9,-2,7,9,5,-6,-1,1,2,-9,-9,8,2,9,4,-10,-10,-1,8,-3,-5,5,5,-1,10,-2,5,-8,-5,-2,-8,3,5,-7,6,-7,6,-9,8,10,10,-8,-1,1,3,4,-6,-1,2,3,5,-9,1,-6,7,-6,-7,3,-1,5,-8,5,-7,-4,-4,7,6,-2,3,6,3,9,8,-1,8,1,6,-9,-4,-4,-1,-10,6,-4,2,-10,-5,7,3,-10,-6,9,1,-7,-3,5,-3,-1,-1,-9,-6,-7,10,-4,-4,5,7,3,4,-3,2,-10,-7,5,7,-8,-5,-6,3,-9,4,8,-10,1,1,-2,4,-10,-3,6,1,3,-2,-10,-8,-3,-2,6,-2,-7,-1,-7,-1,5,-4,-5,6,10,8,-3,8,9,-7,-6,-1,3,2,-6,-9,-8,-9,-7,-3,-5,6,7,3,7,-2,2,-6,5,5,2,10,6,-2,-8,-9,-6,-10,10,-1,-5,10,6,2,-3,-1,-2,4,4,-2,-3,-3,7,-3,7,4,7,-1,1,2,-2,-10,8,4,-1,2,9,-6,9,3,-1,9,-4,-1,-4,10,8,10,-5,-7,3,4,-7,8,8,-5,10,-9,4,9,2,6,9,-7,-2,-5,-6,-9,-7,-10,-8,-6,-8,-3,4,2,1,-10,-6,9,1,-5,10,9,-8,-4,5,7,6,6,3,-8,8,9,4,1,1,-2,7,10,-2,4,-4,-1,-2,-10,6,1,7,7,-7,5,-4,9,-8,-9,-3,8,-7,-8,5,-5,-6,-5,8,4,-4,-5,6,2,-5,6,7,5,-10,-4,-1,-6,-7,1,6,-3,4,9,-2,-8,3,4,8,3,-4,-3,-5,-3,-3,-8,-2,7,6,8,8,-6,-1,-10,-4,7,9,-3,10,-7,-4,1,-5,-2,6,-1,-7,5,9,-7,10,1,3,-6,-1,7,1,1,-8,-6,-4,-1,8,-9,3,10,-9,5,-6,-4,-7,4,10,-3,-10,-3,8,5,9,-2,1,6,-6,9,-3,1,-5,7,2,-4,-8,7,2,-3,8,-5,-9,7,3,9,1,7,7,-3,-3,1,5,-9,-2,10,-8,-6,-8,-4,1,1,1,1,-4,-7,3,-8,8,9,-8,9,-6,4,-10,-6,-10,-6,-7,-1,3,-5,7,-7,1,-4,-5,-6,8,6,6,10,1,9,4,6,-7,4,-6,-9,-8,-9,-4,5,-5,-1,-3,9,6,1,-7,7,-1,9,5,8,9,-8,2,-6,-4,-10,-7,-2,-10,-4,1,-2,-4,2,7,1,-5,2,2,-6,6,-5,8,7,-2,4,2,-6,7,4,-7,-3,-5,2,4,6,-6,2,-10,-2,7,6,2,-6,1,6,-4,-10,3,-6,10,4,5,-7,-4,-9,-5,-2,10,-9,-5,-9,-1,10,3,-10,10,-8,-1,-1,-4,-5,9,9,5,-10,-10,-1,-10,-6,7,-7,-1,3,1,-4,-8,5,8,5,-1,-4,-4,3,-8,-10,-4,-3,3,6,1,9,1,-7,10,-4,6,2,-5,-7,-4,7,5,3,-5,10,-1,7,4,2,-5,5,-4,-3,-9,-3,7,-1,1,10,4,-4,-10,-6,-5,10,-5,-1,-1,-10,-7,5,5,6,-1,2,8,-10,-8,-3,-7,5,10,-10,2,-3,-7,3,-6,7,-7,7,-6,-2,-5,9,1,-1,2,2,-5,3,7,3,-6,3,1,9,-6,4,-9,3,-7,-1,-10,-4,-9,-7,4,-2,-2,4,-4,1,-5,3,-7,3,3,-2,-6,7,3,4,6,8,10,1,8,-5,-6,6,-9,7,3,-4,-8,-6,7,-10,7,-2,3,-10,5,3,-8,-5,8,-8,1,-1,4,-2,1,-5,2,-3,1,6,-3,-9,8,7,-4,-8,-6,8,10,1,3,-8,-5,10,8,-4,-4,1,7,-7,-2,7,-6,8,-4,5,-6,2,8,7,-9,5,6,-5,-6,3,7,-4,5,-9,10,8,-9,-7,-6,2,-7,-9,5,-5,6,6,10,-8,-3,-5,3,1,8,10,4,9,9,6,2,4,3,-3,4,-7,-8,-2,-8,4,2,-9,-8,-10,8,10,1,-10,-5,-7,-4,-6,7,-5,2,2,-7,-2,1,1,-2,-3,-6,9,-6,10,1,4,3,-2,3,1,-6,5,7,-1,7,-3,-7,-2,-9,4,-8,7,-10,-8,-4,4,-2,-9,5,1,4,-4,-8,-1,-1,-6,-3,-10,-1,-9,9,-7,2,-1,6,8,-6,8,-9,1,-5,-8,-2,-3,-9,10,-6,9,2,7,-4,5,-9,5,3,-9,5,-9,8,-9,-4,4,-5,10,-5,-3,-3,-8,-3,-2,1,7,7,-2,-7,1,-2,-3,-8,-4,3,-3,-8,-9,-5,9,2,-1,-1,-3,6,10,-1,-4,-8,-3,6,7,6,-6,9,-7,1,-2,-1,-1,-1,6,3,-2,-10,4,-2,1,9,10,-3,10,5,6,-7,4,7,-1,-1,3,-1,-7,-8,-2,6,-6,1,2,-8,-3,-7,-4,-8,-7,9,10,9,-2,6,3,-7,10,4,3,4,6,4,8,-4,-1,-6,-10,10,9,5,-9,-10,-10,3,-8,-1,8,4,-7,10,-1,1,-9,-5,-9,2,-5,-9,9,-10,10,-3,7,4,-8,-4,-1,2,7,10,-10,-4,-7,9,4,4,1,10,-7,-1,-3,5,9,-5,7,-2,10,-3,6,2,1,2,5,9,-10,-8,5,-6,3,1,-9,-8,-7,-5,-2,3,-4,7,-8,-1,5,9,3,4,-9,7,-8,-6,-7,-9,9,-4,8,-4,8,-3,5,2,-9,5,1,-5,-8,-5,-3,5,10,-5,-3,-5,4,-3,-1,-8,-9,-10,6,1,-8,10,5,-3,9,1,9,-4,-5,-4,9,-9,-9,-1,8,-1,-10,-8,-10,-8,-3,2,7,6,10,10,-6,-10,-10,9,4,-4,1,-1,-7,2,10,-3,-8,2,-1,-9,-1,-1,1,1,-10,-4,-9,3,-4,7,9,-4,8,-4,8,7,4,10,-8,3,-6,-10,-1,-10,-8,-2,6,3,-2,5,2,-7,10,2,-10,5,-3,10,5,-1,-8,9,9,-8,-1,-10,4,7,-7,-1,7,3,-8,4,-7,-8,7,7,-1,6,-9,-3,4,-9,3,9,4,8,7,7,10,-6,-3,5,-1,6,-7,-7,2,-3,-3,-5,-4,-1,6,4,-3,2,-7,-2,8,-10,-8,10,-2,5,5,4,-2,2,-3,3,-1,2,4,6,-1,-8,3,8,-1,1,-2,7,2,-3,8,-10,3,-6,-5,10,1,6,-6,-9,7,4,7,-5,-1,-5,-4,-5,-7,5,-3,10,3,-8,-10,7,-9,9,2,-6,-10,-1,5,3,-7,6,1,6,1,4,-2,-1,2,10,3,7,8,10,-4,-7,-9,-4,10,6,-5,5,1,-10,-5,9,6,-5,-3,-8,-8,-1,10,1,5,-3,8,-8,3,6,-6,-10,-2,-7,-10,4,-9,-8,10,9,7,-6,10,-7,-1,3,-7,-4,-7,-6,5,4,-6,-5,2,-2,5,-5,3,10,-5,3,-5,3,-7,9,-8,8,-7,-10,4,-7,9,4,4,-6,-6,-10,-8,-4,-9,-7,-8,-3,-5,-4,-5,7,-3,-8,6,5], dtype = "int32")#candidate|9781|(2197,)|const|int32
var_9782 = relay.var("var_9782", dtype = "float64", shape = (100,))#candidate|9782|(100,)|var|float64
call_9779 = relay.TupleGetItem(func_6713_call(relay.reshape(const_9780.astype('float32'), [11, 6, 9]), relay.reshape(const_9781.astype('int32'), [2197,]), relay.reshape(var_9782.astype('float64'), [100,]), ), 8)
call_9783 = relay.TupleGetItem(func_6717_call(relay.reshape(const_9780.astype('float32'), [11, 6, 9]), relay.reshape(const_9781.astype('int32'), [2197,]), relay.reshape(var_9782.astype('float64'), [100,]), ), 8)
uop_9787 = relay.atanh(call_9762.astype('float32')) # shape=(110,)
uop_9789 = relay.atanh(call_9763.astype('float32')) # shape=(110,)
func_8857_call = mod.get_global_var('func_8857')
func_8861_call = mutated_mod.get_global_var('func_8861')
const_9795 = relay.const([3.970575,-4.223660,8.879826,-7.725480,1.258167,-3.149940,3.814618,-7.909324,-2.815116,5.436702,-6.614537,-7.730141,2.316161,0.462818,6.007811,8.527377,1.248215,-6.360447,3.024946,9.388110,-5.318058,4.051642,1.937481,-1.923704,-9.377136,0.569943,4.268064,6.457553,9.625066,-5.849944,-3.371020,1.928348,4.321891,-1.902125,-4.463312,-7.432067,-7.350005,-6.002457,2.619487,5.492718,-1.650505,-0.051479,-8.348597,-8.111371,2.924403,3.885406,7.697174,1.061644,-6.803148,5.765556,-3.350552,0.455858,7.363782,-2.020023,8.415629,-6.103033,-6.970176,5.185938,-4.395437,-3.868940,-4.183201,4.160599,-0.971166,8.284003,5.911462,4.896377,-0.336852,-3.545907,-0.566497,-0.323542,-6.847179,4.585762,1.654176,-2.965510,-8.931953,5.941693,-2.963653,-7.498915,-4.606093,9.089296,-0.441635,8.430579,4.872635,-8.155611,-8.255164,1.069328,-4.928150,7.295171,-5.136675,4.975434,-6.896929,8.008537,-3.769629,3.678832,2.137595,-1.880077,8.403516,-2.045036,8.591766,-1.094158,0.522024,-4.359272,-8.080384,-9.119331,1.845793,3.953866,-0.795810,-0.668377,6.398952,2.288905,-2.562551,-3.643590,8.211163,9.212573,-0.300600,-4.997109,6.060866,5.203570,-2.325671,-1.900712,9.267181,2.173162,7.072155,-4.702398,2.690587,6.508221,5.051231,2.144653,2.483063,4.517195,-0.546259,4.918814,5.555576,8.169489,-9.120862,7.164304,-0.979468,-9.219697,2.175364,-7.343743,-1.308814,-9.714685,1.663766,5.658167,-0.186638,-7.649594,-4.037957,1.493484,-1.832624,-2.342029,-7.715128,2.095914,-3.432480,-6.010411,-8.448914,2.345562,8.989767,4.027905,4.538338,4.024875,4.023991,6.505918,0.005318,2.655690,3.178843,1.624388,-3.775122,-2.167382,-6.575265,-4.696252,2.353906,7.850639,7.605244,-1.667218,6.922955,1.446981,6.416260,8.822686,6.103672,2.540261,-6.301525,-6.992558,7.299598,8.517288,-0.375277,-7.312589,3.564912,-2.276826,-6.501553,-6.204115,-0.552051,1.800186,-0.988964,-5.477176,7.129999,-9.471291,-6.184904,-9.311187,-1.104581,8.057033,6.414549,-0.416731,-3.813794,-3.416492,3.124941,-7.985729,-4.689813,-4.116092,-6.202689,-6.765433,-9.185049,0.200323,6.054860,-0.098519,-9.031958,-3.372194,1.716306,-6.500207,6.817889,5.961462,8.116162,-3.897992,6.245867,-4.031795,-1.498113,8.322002,-0.648875,7.187524,6.183853,3.671068,-9.935583,0.682338,-7.786953,3.740488,-9.234859,1.827383,-5.619607,6.713442,-8.590552,-6.841206,-7.219955,8.527588,-0.875060,8.631258,-2.787369,4.972306,-5.222657,-8.240584,8.881034,7.016322,-6.522553,4.614464,-0.331652,-5.664706,8.764754,6.673158,5.292699,-6.120675,-4.006706,0.426393,-5.639318,6.917054,3.178606,5.691393,5.518491,0.210019,2.520911,-8.124768,8.585575,-0.573265,9.030822,4.045270,-5.890999,5.796768,1.674153,1.900195,9.755914,-1.560127,6.105944,4.115352,-1.778192,-7.926415,-2.088542,-9.879322,-2.659760,-7.910091,-6.923870,-8.740921,1.064295,7.609370,-3.150641,-3.527145,1.367132,-9.013965,-7.729765,2.908413,-8.863087,4.331011,9.971899,1.228666,-5.578503,7.812099,6.699837,-0.700956,8.814318,1.523529,-8.469864,-7.412160,-0.622069,-1.164606,-1.343413,-6.612681,-8.308365,8.744222,0.329158,9.451804,-6.298220,-2.705912,-5.975573,-2.154997,6.018114,9.553796,4.871405,7.019432,-5.547908,1.029703,-9.572737,-1.839981,7.002507,-1.485355,-8.943192,-3.053320,-8.886185,-1.243344,2.393461,5.821702,-8.774370,5.448892,-1.590927,0.864770,-2.316141,2.739182,-4.579723,0.141937,-1.652006,-7.410379,5.006325,2.214911,-1.927509,-4.476396,6.270883,-7.125176,-0.301886,7.670820,-8.639207,-9.079049,9.372672,7.438819,6.692165,4.140658,-2.002973,-1.314015,8.801115,-6.942564,9.704127,6.637423,-2.478116,-1.148427,1.361867,5.366020,-5.276156,0.867908,8.665336,-9.278365,7.522069,-2.680771,0.781186,-1.522987,8.240866,-0.521845,9.946460,6.168920,4.990097,8.556170,0.462665,8.883163,-3.185729,-8.479816,4.867709,-0.599508,-4.684010,6.074726,0.425815,-8.903157,-6.831974,0.337511,2.486648,9.651947,-4.086583,2.498846,9.848230,7.828513,2.158639,7.079451,-3.169152,-2.828502,3.767935,1.941577,3.809290,9.699901,-0.047301,0.842817,9.058920,8.765594,1.356580,8.727249,1.357702,-6.164945,-1.560243,4.480452,7.596471,-1.272583,5.538231,2.223483,4.711004,-6.954575,7.707679,4.957154,-3.635069,-0.186827,-5.226980,-4.955523,7.395729,-6.770332,6.208259,-7.966095,5.627351,1.267501,-7.429270,0.977807,5.649200,-4.585117,-3.690915,6.854011,-7.763100,-6.183123,4.534133,-7.030108,-9.636848,8.820869,-7.258173,-8.797772,-1.163292,0.586840,9.383858,-1.892088,-7.461679,2.614841,6.576843,-8.320690,4.947379,-9.865284,8.862932,9.381333,0.501925,5.902342,-9.879579,-2.772923,1.933646,-4.811001,-1.705981,5.572292,4.109898,8.408529,3.462368,-0.150809,5.520304,-3.111217,6.149227,-6.222979,-3.305353,-5.382711,8.081968,2.066898,-6.916804,3.852234,-7.475451,-2.443607,-1.768835,-4.903404,6.153206,-9.607824,5.013407,9.898892,-9.534327,-4.733085,-1.443261,5.514314,3.454024,-0.517944,-3.105915,-4.585813,1.462287,-7.231437,0.109469,3.654242,5.749016,8.121528,-9.555720,3.548873,-8.967613,9.644315,6.209774,-6.901615,9.245370,-1.296079,7.276741,4.793039,0.451757,-9.407840,-6.025122,3.158603,4.785631,6.549615,-6.232477,-5.607850,-3.036585,2.216094,-7.910738,-3.322998,-9.160729,-4.744325,0.033591,-0.154126,2.510632,7.703110,7.284312,-6.971403,0.046132,-5.492771,-6.739846,-5.115874,3.780783,-4.406419,-0.147161,0.191870,-2.084404,-6.271841,7.937604,-3.435625,7.429401,5.982038,8.730634,5.291927,8.071138,-8.017832,-9.455156,-6.278138,-0.575349,8.587462,3.877514,8.713975,-1.009824,2.882007,7.062482,1.932651,-2.057472,5.297806,-5.153062,-7.602086,-0.049766,9.420994,-8.612263,-5.648364,5.185600,3.651242,4.803430,-9.962549,-8.484684,5.275066,8.384754,-2.226979,0.276448,9.819756,-4.611734,0.317356,-2.105283,8.018681,-6.884726,5.380871,3.140424,-9.295938,-4.763742,9.363967,0.434741,-7.822294,1.422080,-8.283664,-1.740770,-3.960462,7.344016,9.593526,-8.390860,-1.028146,9.829545,-9.340465,-0.595593,0.723001,0.589399,7.074424,4.071823,-3.938341,-9.142070,-5.730352,-2.894865,9.193702,-9.454448,-0.290146,5.213670,-5.784401,-0.477729,-6.594196,6.511558,1.847804,-4.689156,1.820790,-8.884886,-5.190639,-8.321567,7.070225,5.887192,3.006202,-3.550330,-9.301607,-4.279810,-5.983702,-4.824892,-4.694542,-0.194715,-2.890777,-6.573154,-0.327171,5.059212,-0.002156,8.866526,8.595593,-8.836145,0.033245,-9.715978,9.104027,-5.203605,4.802577,-6.256279,-6.838817,-6.792683,1.481055,9.995609,7.035139,-5.124274,-1.660512], dtype = "float32")#candidate|9795|(660,)|const|float32
var_9796 = relay.var("var_9796", dtype = "float64", shape = ())#candidate|9796|()|var|float64
call_9794 = relay.TupleGetItem(func_8857_call(relay.reshape(const_9795.astype('float32'), [110, 6]), relay.reshape(var_9796.astype('float64'), []), ), 2)
call_9797 = relay.TupleGetItem(func_8861_call(relay.reshape(const_9795.astype('float32'), [110, 6]), relay.reshape(var_9796.astype('float64'), []), ), 2)
func_9546_call = mod.get_global_var('func_9546')
func_9550_call = mutated_mod.get_global_var('func_9550')
call_9810 = relay.TupleGetItem(func_9546_call(relay.reshape(var_9768.astype('float64'), [110,]), relay.reshape(uop_9787.astype('float32'), [110,]), ), 2)
call_9811 = relay.TupleGetItem(func_9550_call(relay.reshape(var_9768.astype('float64'), [110,]), relay.reshape(uop_9787.astype('float32'), [110,]), ), 2)
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_9844 = relay.TupleGetItem(func_3655_call(), 0)
call_9845 = relay.TupleGetItem(func_3656_call(), 0)
output = relay.Tuple([bop_9769,call_9779,const_9780,const_9781,var_9782,uop_9787,call_9794,const_9795,var_9796,call_9810,call_9844,])
output2 = relay.Tuple([bop_9772,call_9783,const_9780,const_9781,var_9782,uop_9789,call_9797,const_9795,var_9796,call_9811,call_9845,])
func_9864 = relay.Function([var_9768,var_9782,var_9796,], output)
mod['func_9864'] = func_9864
mod = relay.transform.InferType()(mod)
var_9865 = relay.var("var_9865", dtype = "float64", shape = (110,))#candidate|9865|(110,)|var|float64
var_9866 = relay.var("var_9866", dtype = "float64", shape = (100,))#candidate|9866|(100,)|var|float64
var_9867 = relay.var("var_9867", dtype = "float64", shape = ())#candidate|9867|()|var|float64
output = func_9864(var_9865,var_9866,var_9867,)
func_9868 = relay.Function([var_9865,var_9866,var_9867,], output)
mutated_mod['func_9868'] = func_9868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3655_call = mod.get_global_var('func_3655')
func_3656_call = mutated_mod.get_global_var('func_3656')
call_9918 = relay.TupleGetItem(func_3655_call(), 0)
call_9919 = relay.TupleGetItem(func_3656_call(), 0)
output = relay.Tuple([call_9918,])
output2 = relay.Tuple([call_9919,])
func_9921 = relay.Function([], output)
mod['func_9921'] = func_9921
mod = relay.transform.InferType()(mod)
mutated_mod['func_9921'] = func_9921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9921_call = mutated_mod.get_global_var('func_9921')
call_9922 = func_9921_call()
output = call_9922
func_9923 = relay.Function([], output)
mutated_mod['func_9923'] = func_9923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5406_call = mod.get_global_var('func_5406')
func_5408_call = mutated_mod.get_global_var('func_5408')
call_9945 = func_5406_call()
call_9946 = func_5406_call()
func_8793_call = mod.get_global_var('func_8793')
func_8794_call = mutated_mod.get_global_var('func_8794')
call_9960 = relay.TupleGetItem(func_8793_call(), 0)
call_9961 = relay.TupleGetItem(func_8794_call(), 0)
output = relay.Tuple([call_9945,call_9960,])
output2 = relay.Tuple([call_9946,call_9961,])
func_9997 = relay.Function([], output)
mod['func_9997'] = func_9997
mod = relay.transform.InferType()(mod)
mutated_mod['func_9997'] = func_9997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9997_call = mutated_mod.get_global_var('func_9997')
call_9998 = func_9997_call()
output = call_9998
func_9999 = relay.Function([], output)
mutated_mod['func_9999'] = func_9999
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10065 = relay.var("var_10065", dtype = "uint8", shape = (11, 2, 10))#candidate|10065|(11, 2, 10)|var|uint8
const_10066 = relay.const([[[-1,-5,-9,-5,10,-1,-2,2,-4,-4],[9,3,-2,-6,3,4,-6,-10,-5,-9]],[[7,-2,4,6,-2,5,2,-5,-4,-1],[-8,5,-3,10,-8,-2,10,5,-7,4]],[[-1,1,8,2,-5,-10,-7,9,-10,5],[-8,6,-1,4,3,-7,8,10,4,-7]],[[-6,-3,4,2,-9,-3,-5,8,9,6],[-9,-8,1,-2,-1,-5,6,7,-8,-3]],[[5,-7,-2,-8,7,4,-7,5,-10,2],[-4,8,4,7,6,10,-5,-4,10,-9]],[[-6,-4,-7,10,4,9,-10,7,4,-8],[5,2,5,-6,-7,-3,-9,-3,-6,4]],[[-6,7,9,2,9,2,7,1,-1,6],[-3,9,6,8,9,-1,6,3,-1,9]],[[-4,-3,6,-3,-4,-4,-2,8,-7,1],[2,-10,-9,2,-9,-3,3,-6,-1,-5]],[[-1,-1,-2,-10,-9,6,2,-8,1,4],[-2,-5,-2,-3,1,7,6,5,-9,6]],[[8,7,-8,-5,-6,10,-6,10,-5,3],[10,-10,-8,-4,-1,-2,2,1,6,-8]],[[-4,8,-3,-10,-5,8,10,4,2,6],[-8,-6,-10,10,-2,-8,-9,8,7,4]]], dtype = "uint8")#candidate|10066|(11, 2, 10)|const|uint8
bop_10067 = relay.equal(var_10065.astype('bool'), relay.reshape(const_10066.astype('bool'), relay.shape_of(var_10065))) # shape=(11, 2, 10)
output = bop_10067
output2 = bop_10067
func_10081 = relay.Function([var_10065,], output)
mod['func_10081'] = func_10081
mod = relay.transform.InferType()(mod)
mutated_mod['func_10081'] = func_10081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10082 = relay.var("var_10082", dtype = "uint8", shape = (11, 2, 10))#candidate|10082|(11, 2, 10)|var|uint8
func_10081_call = mutated_mod.get_global_var('func_10081')
call_10083 = func_10081_call(var_10082)
output = call_10083
func_10084 = relay.Function([var_10082], output)
mutated_mod['func_10084'] = func_10084
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10094 = relay.const([[[7.507960,6.024685],[5.317934,0.346160],[7.396949,-1.078640],[-7.896271,-3.709547],[-3.255585,4.372719],[0.240007,-6.081032],[7.112569,-3.505411],[-7.386258,9.050209],[-5.133233,-6.288311],[1.956461,8.838857],[-1.918477,-3.297807],[3.798573,-8.454123],[-2.041948,8.113739],[-9.106754,8.152668],[-8.839624,8.711968]],[[-8.006716,-8.988596],[8.664287,-3.873677],[-7.288680,-8.820225],[-5.222808,2.876657],[7.829336,1.762832],[5.281883,0.820180],[-8.345380,8.709254],[-1.549201,5.923483],[-9.563734,5.686308],[2.623216,-4.704693],[0.352686,-3.780833],[0.003824,6.971315],[6.581308,-8.534446],[-6.155477,-0.921875],[7.443811,3.565324]],[[-0.449671,-1.748925],[-8.879169,8.872800],[2.498146,1.073477],[-6.916631,-7.211853],[-4.370108,-8.345438],[9.363609,-1.481149],[-7.227672,-3.275367],[4.266377,8.729802],[2.198585,-1.536667],[8.325530,9.231100],[7.239342,-8.453578],[-4.052177,-9.625421],[-9.355998,-5.500945],[9.421877,6.935799],[-8.162466,5.297914]],[[2.696456,9.691658],[-7.420995,-4.237679],[3.473008,4.415214],[6.871456,-4.842432],[-3.912991,-9.166785],[8.782060,-5.035024],[3.597257,-5.075114],[-9.152722,5.779054],[-5.908786,-3.472131],[-5.797253,3.263728],[-4.942379,4.788435],[-4.209272,5.102230],[-7.594118,5.305344],[-7.640583,-3.526764],[-3.741540,1.214112]],[[6.838254,-6.635153],[-6.920474,-5.467279],[-6.100328,-2.335824],[-8.957836,-3.023994],[-5.519571,-3.948323],[1.358606,-1.910651],[0.940656,9.066853],[-3.427448,-9.696133],[-7.664874,2.410045],[3.622212,2.789656],[7.635801,-7.550356],[6.124129,-1.136265],[-4.568327,-6.610027],[8.046072,-4.224404],[-5.889124,-0.993389]],[[-9.087104,-2.132005],[5.459412,0.347364],[7.194828,-2.586100],[7.119677,3.923690],[4.141307,-2.624337],[-4.856837,9.209593],[5.537257,-9.133019],[-0.160552,-4.051193],[-7.516783,1.866110],[4.953126,-3.879889],[4.598374,6.233912],[-0.665511,-1.169072],[2.151873,7.656161],[2.910470,5.136765],[-0.990670,-4.013329]]], dtype = "float64")#candidate|10094|(6, 15, 2)|const|float64
uop_10095 = relay.atanh(const_10094.astype('float64')) # shape=(6, 15, 2)
output = relay.Tuple([uop_10095,])
output2 = relay.Tuple([uop_10095,])
func_10099 = relay.Function([], output)
mod['func_10099'] = func_10099
mod = relay.transform.InferType()(mod)
mutated_mod['func_10099'] = func_10099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mutated_mod.get_global_var('func_10099')
call_10100 = func_10099_call()
output = call_10100
func_10101 = relay.Function([], output)
mutated_mod['func_10101'] = func_10101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_10316 = relay.TupleGetItem(func_2808_call(), 0)
call_10317 = relay.TupleGetItem(func_2810_call(), 0)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_10335 = func_5171_call()
call_10336 = func_5171_call()
output = relay.Tuple([call_10316,call_10335,])
output2 = relay.Tuple([call_10317,call_10336,])
func_10341 = relay.Function([], output)
mod['func_10341'] = func_10341
mod = relay.transform.InferType()(mod)
output = func_10341()
func_10342 = relay.Function([], output)
mutated_mod['func_10342'] = func_10342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mod.get_global_var('func_3287')
func_3289_call = mutated_mod.get_global_var('func_3289')
call_10384 = relay.TupleGetItem(func_3287_call(), 0)
call_10385 = relay.TupleGetItem(func_3289_call(), 0)
output = relay.Tuple([call_10384,])
output2 = relay.Tuple([call_10385,])
func_10398 = relay.Function([], output)
mod['func_10398'] = func_10398
mod = relay.transform.InferType()(mod)
mutated_mod['func_10398'] = func_10398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10398_call = mutated_mod.get_global_var('func_10398')
call_10399 = func_10398_call()
output = call_10399
func_10400 = relay.Function([], output)
mutated_mod['func_10400'] = func_10400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9157_call = mod.get_global_var('func_9157')
func_9158_call = mutated_mod.get_global_var('func_9158')
call_10423 = relay.TupleGetItem(func_9157_call(), 0)
call_10424 = relay.TupleGetItem(func_9158_call(), 0)
func_4781_call = mod.get_global_var('func_4781')
func_4783_call = mutated_mod.get_global_var('func_4783')
const_10428 = relay.const(8.291865, dtype = "float64")#candidate|10428|()|const|float64
call_10427 = relay.TupleGetItem(func_4781_call(relay.reshape(const_10428.astype('float64'), [])), 0)
call_10429 = relay.TupleGetItem(func_4783_call(relay.reshape(const_10428.astype('float64'), [])), 0)
uop_10449 = relay.sin(call_10427.astype('float32')) # shape=(110,)
uop_10451 = relay.sin(call_10429.astype('float32')) # shape=(110,)
uop_10461 = relay.rsqrt(uop_10449.astype('float32')) # shape=(110,)
uop_10463 = relay.rsqrt(uop_10451.astype('float32')) # shape=(110,)
output = relay.Tuple([call_10423,const_10428,uop_10461,])
output2 = relay.Tuple([call_10424,const_10428,uop_10463,])
func_10464 = relay.Function([], output)
mod['func_10464'] = func_10464
mod = relay.transform.InferType()(mod)
mutated_mod['func_10464'] = func_10464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10464_call = mutated_mod.get_global_var('func_10464')
call_10465 = func_10464_call()
output = call_10465
func_10466 = relay.Function([], output)
mutated_mod['func_10466'] = func_10466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9659_call = mod.get_global_var('func_9659')
func_9661_call = mutated_mod.get_global_var('func_9661')
call_10467 = relay.TupleGetItem(func_9659_call(), 2)
call_10468 = relay.TupleGetItem(func_9661_call(), 2)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_10471 = func_5180_call()
call_10472 = func_5180_call()
var_10475 = relay.var("var_10475", dtype = "float32", shape = (11, 4, 7))#candidate|10475|(11, 4, 7)|var|float32
bop_10476 = relay.multiply(call_10471.astype('uint32'), var_10475.astype('uint32')) # shape=(11, 4, 7)
bop_10479 = relay.multiply(call_10472.astype('uint32'), var_10475.astype('uint32')) # shape=(11, 4, 7)
output = relay.Tuple([call_10467,bop_10476,])
output2 = relay.Tuple([call_10468,bop_10479,])
func_10490 = relay.Function([var_10475,], output)
mod['func_10490'] = func_10490
mod = relay.transform.InferType()(mod)
mutated_mod['func_10490'] = func_10490
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10491 = relay.var("var_10491", dtype = "float32", shape = (11, 4, 7))#candidate|10491|(11, 4, 7)|var|float32
func_10490_call = mutated_mod.get_global_var('func_10490')
call_10492 = func_10490_call(var_10491)
output = call_10492
func_10493 = relay.Function([var_10491], output)
mutated_mod['func_10493'] = func_10493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9398_call = mod.get_global_var('func_9398')
func_9400_call = mutated_mod.get_global_var('func_9400')
call_10507 = relay.TupleGetItem(func_9398_call(), 0)
call_10508 = relay.TupleGetItem(func_9400_call(), 0)
func_9997_call = mod.get_global_var('func_9997')
func_9999_call = mutated_mod.get_global_var('func_9999')
call_10509 = relay.TupleGetItem(func_9997_call(), 1)
call_10510 = relay.TupleGetItem(func_9999_call(), 1)
func_4052_call = mod.get_global_var('func_4052')
func_4055_call = mutated_mod.get_global_var('func_4055')
var_10513 = relay.var("var_10513", dtype = "uint16", shape = (210,))#candidate|10513|(210,)|var|uint16
call_10512 = relay.TupleGetItem(func_4052_call(relay.reshape(var_10513.astype('uint16'), [15, 1, 14])), 1)
call_10514 = relay.TupleGetItem(func_4055_call(relay.reshape(var_10513.astype('uint16'), [15, 1, 14])), 1)
output = relay.Tuple([call_10507,call_10509,call_10512,var_10513,])
output2 = relay.Tuple([call_10508,call_10510,call_10514,var_10513,])
func_10532 = relay.Function([var_10513,], output)
mod['func_10532'] = func_10532
mod = relay.transform.InferType()(mod)
mutated_mod['func_10532'] = func_10532
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10533 = relay.var("var_10533", dtype = "uint16", shape = (210,))#candidate|10533|(210,)|var|uint16
func_10532_call = mutated_mod.get_global_var('func_10532')
call_10534 = func_10532_call(var_10533)
output = call_10534
func_10535 = relay.Function([var_10533], output)
mutated_mod['func_10535'] = func_10535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6269_call = mod.get_global_var('func_6269')
func_6271_call = mutated_mod.get_global_var('func_6271')
call_10551 = relay.TupleGetItem(func_6269_call(), 3)
call_10552 = relay.TupleGetItem(func_6271_call(), 3)
output = relay.Tuple([call_10551,])
output2 = relay.Tuple([call_10552,])
func_10553 = relay.Function([], output)
mod['func_10553'] = func_10553
mod = relay.transform.InferType()(mod)
output = func_10553()
func_10554 = relay.Function([], output)
mutated_mod['func_10554'] = func_10554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9997_call = mod.get_global_var('func_9997')
func_9999_call = mutated_mod.get_global_var('func_9999')
call_10624 = relay.TupleGetItem(func_9997_call(), 1)
call_10625 = relay.TupleGetItem(func_9999_call(), 1)
func_4333_call = mod.get_global_var('func_4333')
func_4336_call = mutated_mod.get_global_var('func_4336')
const_10631 = relay.const([-9.752067,-1.127482,7.356869,9.530831,5.230770,-4.567789,4.712667,3.990041,-1.751814,-2.152886,-3.152259,-1.977257,-6.412756,4.569376,6.993068,6.457175,0.204745,4.460963,-9.744213,9.115632,-1.418726,6.647535,-8.013382,-6.975925,-9.887894,3.549109,8.646869,-1.283967,3.495440,9.826541,-6.429557,-8.508283,-6.675552,4.076000,2.554644,8.661476,-0.559363,6.195615,3.241282,6.734581,-2.312939,-2.405099,-1.835436,2.068007,7.849564,-3.050975,6.162668,6.946591,-6.252218,-8.708846,4.274496,3.517442,-0.047066,-1.427143,-7.508884,2.347918,-9.588126,-8.552921,3.081119,6.329068,-5.018144,-9.284417,-6.470290,-5.395970,-8.469126,-3.898200,-7.079573,1.026863,-6.943863,-3.524665,-1.399691,5.123279,-3.602662,0.261722,2.914472,-3.085878,0.514882,9.364030,-3.190545,-7.525100,-2.476738,-0.705294,8.876311,4.655022,0.697460,-2.134319,-0.416871,2.114931,-8.949031,-4.283960,7.833642,6.270866,6.183975,-9.309602,-7.679873,6.545010,-1.578464,2.502484,7.829344,0.569270], dtype = "float64")#candidate|10631|(100,)|const|float64
call_10630 = relay.TupleGetItem(func_4333_call(relay.reshape(const_10631.astype('float64'), [2, 10, 5])), 2)
call_10632 = relay.TupleGetItem(func_4336_call(relay.reshape(const_10631.astype('float64'), [2, 10, 5])), 2)
func_6308_call = mod.get_global_var('func_6308')
func_6310_call = mutated_mod.get_global_var('func_6310')
call_10647 = relay.TupleGetItem(func_6308_call(), 0)
call_10648 = relay.TupleGetItem(func_6310_call(), 0)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_10657 = func_3544_call()
call_10658 = func_3544_call()
output = relay.Tuple([call_10624,call_10630,const_10631,call_10647,call_10657,])
output2 = relay.Tuple([call_10625,call_10632,const_10631,call_10648,call_10658,])
func_10692 = relay.Function([], output)
mod['func_10692'] = func_10692
mod = relay.transform.InferType()(mod)
mutated_mod['func_10692'] = func_10692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10692_call = mutated_mod.get_global_var('func_10692')
call_10693 = func_10692_call()
output = call_10693
func_10694 = relay.Function([], output)
mutated_mod['func_10694'] = func_10694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5685_call = mod.get_global_var('func_5685')
func_5686_call = mutated_mod.get_global_var('func_5686')
call_10728 = relay.TupleGetItem(func_5685_call(), 0)
call_10729 = relay.TupleGetItem(func_5686_call(), 0)
output = call_10728
output2 = call_10729
func_10757 = relay.Function([], output)
mod['func_10757'] = func_10757
mod = relay.transform.InferType()(mod)
output = func_10757()
func_10758 = relay.Function([], output)
mutated_mod['func_10758'] = func_10758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9341_call = mod.get_global_var('func_9341')
func_9343_call = mutated_mod.get_global_var('func_9343')
call_10771 = relay.TupleGetItem(func_9341_call(), 0)
call_10772 = relay.TupleGetItem(func_9343_call(), 0)
var_10802 = relay.var("var_10802", dtype = "float64", shape = (110,))#candidate|10802|(110,)|var|float64
bop_10803 = relay.maximum(call_10771.astype('int32'), relay.reshape(var_10802.astype('int32'), relay.shape_of(call_10771))) # shape=(110,)
bop_10806 = relay.maximum(call_10772.astype('int32'), relay.reshape(var_10802.astype('int32'), relay.shape_of(call_10772))) # shape=(110,)
func_9997_call = mod.get_global_var('func_9997')
func_9999_call = mutated_mod.get_global_var('func_9999')
call_10814 = relay.TupleGetItem(func_9997_call(), 1)
call_10815 = relay.TupleGetItem(func_9999_call(), 1)
func_4021_call = mod.get_global_var('func_4021')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_10826 = relay.TupleGetItem(func_4021_call(), 0)
call_10827 = relay.TupleGetItem(func_4023_call(), 0)
uop_10828 = relay.exp(call_10814.astype('float64')) # shape=(110,)
uop_10830 = relay.exp(call_10815.astype('float64')) # shape=(110,)
output = relay.Tuple([bop_10803,call_10826,uop_10828,])
output2 = relay.Tuple([bop_10806,call_10827,uop_10830,])
func_10840 = relay.Function([var_10802,], output)
mod['func_10840'] = func_10840
mod = relay.transform.InferType()(mod)
var_10841 = relay.var("var_10841", dtype = "float64", shape = (110,))#candidate|10841|(110,)|var|float64
output = func_10840(var_10841)
func_10842 = relay.Function([var_10841], output)
mutated_mod['func_10842'] = func_10842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8383_call = mod.get_global_var('func_8383')
func_8385_call = mutated_mod.get_global_var('func_8385')
call_10871 = func_8383_call()
call_10872 = func_8383_call()
output = relay.Tuple([call_10871,])
output2 = relay.Tuple([call_10872,])
func_10880 = relay.Function([], output)
mod['func_10880'] = func_10880
mod = relay.transform.InferType()(mod)
output = func_10880()
func_10881 = relay.Function([], output)
mutated_mod['func_10881'] = func_10881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8793_call = mod.get_global_var('func_8793')
func_8794_call = mutated_mod.get_global_var('func_8794')
call_10898 = relay.TupleGetItem(func_8793_call(), 0)
call_10899 = relay.TupleGetItem(func_8794_call(), 0)
output = call_10898
output2 = call_10899
func_10905 = relay.Function([], output)
mod['func_10905'] = func_10905
mod = relay.transform.InferType()(mod)
output = func_10905()
func_10906 = relay.Function([], output)
mutated_mod['func_10906'] = func_10906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_10910 = func_5180_call()
call_10911 = func_5180_call()
output = relay.Tuple([call_10910,])
output2 = relay.Tuple([call_10911,])
func_10921 = relay.Function([], output)
mod['func_10921'] = func_10921
mod = relay.transform.InferType()(mod)
output = func_10921()
func_10922 = relay.Function([], output)
mutated_mod['func_10922'] = func_10922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10398_call = mod.get_global_var('func_10398')
func_10400_call = mutated_mod.get_global_var('func_10400')
call_10936 = relay.TupleGetItem(func_10398_call(), 0)
call_10937 = relay.TupleGetItem(func_10400_call(), 0)
output = call_10936
output2 = call_10937
func_10960 = relay.Function([], output)
mod['func_10960'] = func_10960
mod = relay.transform.InferType()(mod)
output = func_10960()
func_10961 = relay.Function([], output)
mutated_mod['func_10961'] = func_10961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7911_call = mod.get_global_var('func_7911')
func_7912_call = mutated_mod.get_global_var('func_7912')
call_10981 = func_7911_call()
call_10982 = func_7911_call()
output = relay.Tuple([call_10981,])
output2 = relay.Tuple([call_10982,])
func_10987 = relay.Function([], output)
mod['func_10987'] = func_10987
mod = relay.transform.InferType()(mod)
mutated_mod['func_10987'] = func_10987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10987_call = mutated_mod.get_global_var('func_10987')
call_10988 = func_10987_call()
output = call_10988
func_10989 = relay.Function([], output)
mutated_mod['func_10989'] = func_10989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8347_call = mod.get_global_var('func_8347')
func_8349_call = mutated_mod.get_global_var('func_8349')
call_11052 = relay.TupleGetItem(func_8347_call(), 0)
call_11053 = relay.TupleGetItem(func_8349_call(), 0)
output = relay.Tuple([call_11052,])
output2 = relay.Tuple([call_11053,])
func_11059 = relay.Function([], output)
mod['func_11059'] = func_11059
mod = relay.transform.InferType()(mod)
mutated_mod['func_11059'] = func_11059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11059_call = mutated_mod.get_global_var('func_11059')
call_11060 = func_11059_call()
output = call_11060
func_11061 = relay.Function([], output)
mutated_mod['func_11061'] = func_11061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11108 = relay.var("var_11108", dtype = "float32", shape = (8, 15, 1))#candidate|11108|(8, 15, 1)|var|float32
uop_11109 = relay.sinh(var_11108.astype('float32')) # shape=(8, 15, 1)
output = relay.Tuple([uop_11109,])
output2 = relay.Tuple([uop_11109,])
func_11111 = relay.Function([var_11108,], output)
mod['func_11111'] = func_11111
mod = relay.transform.InferType()(mod)
var_11112 = relay.var("var_11112", dtype = "float32", shape = (8, 15, 1))#candidate|11112|(8, 15, 1)|var|float32
output = func_11111(var_11112)
func_11113 = relay.Function([var_11112], output)
mutated_mod['func_11113'] = func_11113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7341_call = mod.get_global_var('func_7341')
func_7343_call = mutated_mod.get_global_var('func_7343')
call_11138 = relay.TupleGetItem(func_7341_call(), 1)
call_11139 = relay.TupleGetItem(func_7343_call(), 1)
func_5406_call = mod.get_global_var('func_5406')
func_5408_call = mutated_mod.get_global_var('func_5408')
call_11143 = func_5406_call()
call_11144 = func_5406_call()
output = relay.Tuple([call_11138,call_11143,])
output2 = relay.Tuple([call_11139,call_11144,])
func_11146 = relay.Function([], output)
mod['func_11146'] = func_11146
mod = relay.transform.InferType()(mod)
output = func_11146()
func_11147 = relay.Function([], output)
mutated_mod['func_11147'] = func_11147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6903_call = mod.get_global_var('func_6903')
func_6904_call = mutated_mod.get_global_var('func_6904')
call_11153 = relay.TupleGetItem(func_6903_call(), 0)
call_11154 = relay.TupleGetItem(func_6904_call(), 0)
const_11175 = relay.const([[[-4.022153,9.541375,3.985287,4.023023],[-4.414711,-8.077683,-4.042821,-1.042943],[6.347331,4.855070,1.417328,-8.622287],[8.663073,7.843115,-7.273600,0.728126],[-6.400015,-0.043417,0.681735,-4.756457],[4.956390,8.164313,-8.326915,9.426893],[-4.460864,-2.115148,-8.503855,9.647250],[8.330028,-1.998497,-3.306567,-2.868345],[-4.917230,-9.467268,-0.130904,4.798990],[9.732229,-7.509825,9.737354,8.933090],[-7.600683,4.949004,7.346802,-3.103406],[4.732194,-1.849997,-0.397389,-1.007250]],[[-8.292205,6.153287,8.869101,-9.327991],[1.777037,-7.430357,6.408296,2.256362],[-9.908848,-6.355634,3.610570,-3.676308],[1.183745,-4.662040,6.842622,-7.363094],[-1.771238,9.777223,0.341655,-4.090289],[-6.533332,1.423407,4.113453,4.122809],[5.087745,1.282323,9.067569,8.486714],[-8.638873,-3.185962,-6.058541,9.133250],[-8.972481,-5.612036,0.771901,6.955645],[1.964348,3.864793,4.051062,-8.972952],[-8.918013,6.480279,4.520891,7.716329],[2.841897,-6.401773,-6.278304,-4.327834]],[[-7.341431,-8.551192,5.279654,1.774198],[-7.374023,9.869365,2.312657,-6.537801],[7.744020,3.738170,-5.405069,3.008964],[1.430411,8.568605,8.767264,-5.866699],[-8.931066,3.090092,-8.443645,5.414600],[4.752722,-1.133966,-5.533644,5.892394],[3.965498,8.475592,3.317358,6.830284],[-0.281991,-0.613788,-2.295943,4.795151],[-8.104875,-5.555581,3.084629,7.537814],[6.982768,9.831959,1.066069,6.866354],[-3.974307,-5.166611,7.142861,-3.117261],[3.974184,-7.101597,7.639610,-4.458653]],[[-9.324855,3.180463,-7.599069,9.879913],[-2.622034,-8.130709,3.511903,-3.685842],[-7.858794,6.038591,-9.030615,1.109688],[-2.100866,4.363058,0.348041,9.987980],[5.553897,7.865279,-8.119204,8.761006],[4.203479,-1.394895,7.236410,-4.031694],[0.044016,-2.905117,8.515365,3.627834],[8.067161,-3.426193,6.313735,-7.584142],[-0.557674,-3.403318,-1.797141,0.847236],[0.703128,-2.026134,9.952840,-7.921737],[-7.837685,-3.726974,-9.198376,-8.752481],[1.209361,-8.312266,-7.490761,0.799526]],[[-7.410093,1.997559,1.883330,9.960167],[-7.360670,5.831185,-9.912385,5.477288],[-6.724046,0.852803,6.373695,-1.314818],[-8.162036,3.895911,-7.197507,4.317191],[5.946771,3.589531,2.451669,5.178891],[7.172212,1.992573,6.186348,-3.784800],[7.108134,-9.906621,8.347515,9.890329],[-0.288214,7.062080,4.069567,0.787876],[5.662579,3.175338,4.214204,4.918829],[1.701759,1.114035,2.548911,6.779213],[6.867712,8.519384,-1.599038,-1.165004],[-7.767130,1.774534,-4.715737,-8.967462]],[[-0.265418,-1.158308,-9.669139,-0.580604],[3.969303,-0.421668,1.526479,1.824279],[-2.414642,-3.699969,5.129745,4.187865],[-6.997472,8.263324,0.578951,-9.542540],[6.561084,-1.718210,-2.857567,8.761743],[-8.893901,-8.051189,2.052291,-7.618169],[6.206791,1.866012,6.093129,-3.864460],[2.657467,-5.784677,4.327145,-3.164447],[0.866341,-3.744580,0.621365,7.121628],[-2.621985,-8.410604,4.990261,1.115505],[0.647429,8.452291,9.967431,-9.183458],[5.643335,4.144377,5.878291,2.179943]],[[-6.613259,1.876339,-4.772777,2.097380],[-0.297453,-5.894175,-9.172124,-0.345361],[-3.403410,-9.557326,2.427637,3.715514],[9.811216,8.482330,-6.578896,-2.626511],[0.284168,2.621686,-3.338442,-8.499907],[-6.794365,0.518101,-8.548628,-4.650424],[7.641520,-6.050802,1.768082,-6.240238],[-8.967826,3.952055,-4.106421,-8.425071],[1.606587,4.167648,-8.822249,1.177663],[0.703942,-1.192470,-8.432996,-0.743365],[1.600126,7.585380,-6.893866,-4.737790],[2.668843,-1.814516,3.416477,6.475343]],[[-0.439715,-9.071729,-8.444898,3.332648],[-2.431943,5.502281,-4.038093,0.897833],[-2.583574,-1.845598,-3.845253,-8.796650],[-5.799922,2.325764,7.041238,1.802240],[-1.987219,-5.796173,1.305680,-1.624802],[9.158422,-5.885021,6.672333,-3.658796],[-5.128439,1.627126,1.136614,9.473483],[-9.578384,7.548991,4.561127,5.832436],[-9.705269,9.140128,9.140015,-2.861729],[1.079139,-1.475965,-6.316093,0.141170],[1.548489,5.048449,-1.088220,-7.668108],[7.527586,-2.459454,-9.576541,-9.741912]],[[9.480192,-1.678235,0.817580,-3.152243],[-7.548757,-0.185290,5.264020,5.061030],[-9.014890,9.342178,8.323040,9.003487],[4.933938,-7.760423,3.263219,-5.802407],[-4.862343,6.163267,9.341488,-8.970724],[-9.832485,-3.956582,-6.494234,-7.979763],[-7.787763,3.274966,3.162934,7.938736],[-1.155554,5.003575,-9.888983,6.005200],[-6.839851,8.459790,-2.144774,4.099075],[-3.522233,-2.822276,-5.686963,4.875388],[-6.913538,-7.689218,2.440746,-2.214963],[5.161807,2.910061,6.523512,-7.332995]],[[9.116223,-9.595602,-2.127484,-7.101132],[2.420165,1.202832,8.035545,3.018405],[-9.103575,1.859600,6.071268,7.149318],[6.756258,-8.266885,7.013155,0.418760],[-7.718650,-3.963734,5.099353,8.396172],[1.320734,-0.317103,4.732024,-6.237695],[-9.326462,6.545176,5.564285,-0.412197],[1.976846,-6.783747,-1.040311,9.129436],[6.097439,4.151776,-7.047101,5.795975],[5.642954,-7.460919,7.590927,-6.305419],[1.081013,5.158448,4.599097,8.254853],[6.411827,4.238783,2.126708,-0.538217]],[[4.528593,-0.120268,4.084926,9.642489],[9.495744,0.667988,0.506066,-2.953980],[-3.649240,5.572130,-2.923662,-6.415398],[-9.521893,8.743989,9.171462,-8.311076],[3.807047,-3.416424,6.079028,6.307558],[-1.158188,7.156337,7.220745,-5.998793],[-4.536251,2.919514,-5.359377,-5.820017],[7.684821,1.320298,0.444027,1.731830],[-6.357106,0.871216,-3.977470,-4.422823],[-2.224430,-5.618560,-1.374139,4.093382],[-4.241319,5.883474,-3.777656,-5.485221],[3.063981,-3.761285,5.629555,1.721617]],[[-2.551207,5.669208,6.235661,3.838088],[-5.682421,8.780709,-3.341165,2.912554],[1.884850,3.775412,-8.498311,-4.008175],[0.221737,-5.441816,-5.412202,-4.453804],[7.437051,8.814263,-3.148739,-1.266598],[-7.729558,0.595628,-2.979099,-1.723052],[3.602438,1.888164,9.540445,4.177259],[3.367862,2.495874,3.314210,-6.012878],[-9.242919,6.869109,-9.699069,4.093030],[-5.996771,2.198979,7.456509,-2.115094],[2.632737,-6.887598,0.844114,-8.052562],[7.962379,5.256632,2.945332,9.098216]],[[0.816020,-1.080211,-6.540651,2.448020],[-6.467922,6.398156,-4.872103,-8.908719],[-4.696462,-1.324921,-2.671690,-9.278066],[-3.716320,-2.159895,7.561664,5.887224],[7.105854,-2.296181,4.631625,-0.760451],[-6.734400,8.065283,5.815013,-6.376923],[-0.844305,-9.329513,5.673233,7.874266],[-8.395557,-3.354970,3.313518,-7.459779],[5.700794,1.319727,-0.728014,2.734390],[9.944088,5.327618,-9.426430,-6.634059],[-4.404129,-0.273513,0.879759,-6.370306],[1.874112,4.586969,-3.456365,2.145743]]], dtype = "float64")#candidate|11175|(13, 12, 4)|const|float64
bop_11176 = relay.bitwise_and(call_11153.astype('uint8'), relay.reshape(const_11175.astype('uint8'), relay.shape_of(call_11153))) # shape=(13, 12, 4)
bop_11179 = relay.bitwise_and(call_11154.astype('uint8'), relay.reshape(const_11175.astype('uint8'), relay.shape_of(call_11154))) # shape=(13, 12, 4)
output = bop_11176
output2 = bop_11179
func_11191 = relay.Function([], output)
mod['func_11191'] = func_11191
mod = relay.transform.InferType()(mod)
output = func_11191()
func_11192 = relay.Function([], output)
mutated_mod['func_11192'] = func_11192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mod.get_global_var('func_3892')
func_3894_call = mutated_mod.get_global_var('func_3894')
call_11202 = relay.TupleGetItem(func_3892_call(), 4)
call_11203 = relay.TupleGetItem(func_3894_call(), 4)
output = relay.Tuple([call_11202,])
output2 = relay.Tuple([call_11203,])
func_11222 = relay.Function([], output)
mod['func_11222'] = func_11222
mod = relay.transform.InferType()(mod)
output = func_11222()
func_11223 = relay.Function([], output)
mutated_mod['func_11223'] = func_11223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9003_call = mod.get_global_var('func_9003')
func_9005_call = mutated_mod.get_global_var('func_9005')
call_11260 = func_9003_call()
call_11261 = func_9003_call()
output = call_11260
output2 = call_11261
func_11277 = relay.Function([], output)
mod['func_11277'] = func_11277
mod = relay.transform.InferType()(mod)
output = func_11277()
func_11278 = relay.Function([], output)
mutated_mod['func_11278'] = func_11278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3803_call = mod.get_global_var('func_3803')
func_3805_call = mutated_mod.get_global_var('func_3805')
call_11290 = relay.TupleGetItem(func_3803_call(), 0)
call_11291 = relay.TupleGetItem(func_3805_call(), 0)
output = call_11290
output2 = call_11291
func_11298 = relay.Function([], output)
mod['func_11298'] = func_11298
mod = relay.transform.InferType()(mod)
output = func_11298()
func_11299 = relay.Function([], output)
mutated_mod['func_11299'] = func_11299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11222_call = mod.get_global_var('func_11222')
func_11223_call = mutated_mod.get_global_var('func_11223')
call_11323 = relay.TupleGetItem(func_11222_call(), 0)
call_11324 = relay.TupleGetItem(func_11223_call(), 0)
output = relay.Tuple([call_11323,])
output2 = relay.Tuple([call_11324,])
func_11336 = relay.Function([], output)
mod['func_11336'] = func_11336
mod = relay.transform.InferType()(mod)
output = func_11336()
func_11337 = relay.Function([], output)
mutated_mod['func_11337'] = func_11337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9297_call = mod.get_global_var('func_9297')
func_9299_call = mutated_mod.get_global_var('func_9299')
call_11382 = relay.TupleGetItem(func_9297_call(), 0)
call_11383 = relay.TupleGetItem(func_9299_call(), 0)
output = call_11382
output2 = call_11383
func_11398 = relay.Function([], output)
mod['func_11398'] = func_11398
mod = relay.transform.InferType()(mod)
output = func_11398()
func_11399 = relay.Function([], output)
mutated_mod['func_11399'] = func_11399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8793_call = mod.get_global_var('func_8793')
func_8794_call = mutated_mod.get_global_var('func_8794')
call_11463 = relay.TupleGetItem(func_8793_call(), 0)
call_11464 = relay.TupleGetItem(func_8794_call(), 0)
output = relay.Tuple([call_11463,])
output2 = relay.Tuple([call_11464,])
func_11484 = relay.Function([], output)
mod['func_11484'] = func_11484
mod = relay.transform.InferType()(mod)
output = func_11484()
func_11485 = relay.Function([], output)
mutated_mod['func_11485'] = func_11485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8179_call = mod.get_global_var('func_8179')
func_8181_call = mutated_mod.get_global_var('func_8181')
call_11554 = func_8179_call()
call_11555 = func_8179_call()
func_5349_call = mod.get_global_var('func_5349')
func_5352_call = mutated_mod.get_global_var('func_5352')
const_11575 = relay.const([[2.153649,-5.820341,-8.605186,4.212287,-0.938438],[6.339314,-1.187325,-3.897283,-3.092951,-7.907188],[-6.123984,7.843011,-2.933283,-3.560618,4.510497],[4.490958,-6.183838,9.416630,7.543942,2.369790],[-1.629998,-2.542723,-6.689630,-0.527225,-4.255172],[-9.795114,0.459169,1.236258,-2.033833,-6.153035],[-8.942451,-5.762630,5.867773,2.391272,0.319497],[-6.269908,3.049068,-2.275707,9.723254,2.376385],[0.159263,2.491686,0.746342,-1.030707,-4.311335],[7.224717,3.025233,1.654433,3.810261,8.515629],[-4.694504,-9.175689,-9.590552,2.711024,-0.791638],[4.080756,3.233054,-5.606923,4.001917,-5.074983],[6.058166,-8.818146,-8.553311,3.482669,7.975822],[-8.323531,0.955524,3.640776,7.333519,9.692977],[6.161950,0.070388,7.116457,3.868487,-7.865737],[6.158138,5.742804,-0.404056,5.422317,9.180744],[-1.937004,-9.201450,6.869127,3.390522,2.961312],[-2.039726,6.701879,2.341639,2.649624,-9.042709],[-1.091636,2.763739,9.186559,3.016766,3.651486],[7.727210,-0.585453,3.604133,-2.159384,-3.137962],[-2.749688,-4.078280,-6.714878,-8.770081,4.143020],[-5.921632,-5.372335,8.811606,4.500188,4.009673]], dtype = "float64")#candidate|11575|(22, 5)|const|float64
call_11574 = relay.TupleGetItem(func_5349_call(relay.reshape(const_11575.astype('float64'), [1, 110])), 7)
call_11576 = relay.TupleGetItem(func_5352_call(relay.reshape(const_11575.astype('float64'), [1, 110])), 7)
bop_11580 = relay.power(call_11574.astype('float32'), relay.reshape(const_11575.astype('float32'), relay.shape_of(call_11574))) # shape=(1, 110)
bop_11583 = relay.power(call_11576.astype('float32'), relay.reshape(const_11575.astype('float32'), relay.shape_of(call_11576))) # shape=(1, 110)
func_8080_call = mod.get_global_var('func_8080')
func_8081_call = mutated_mod.get_global_var('func_8081')
call_11591 = relay.TupleGetItem(func_8080_call(), 1)
call_11592 = relay.TupleGetItem(func_8081_call(), 1)
output = relay.Tuple([call_11554,bop_11580,call_11591,])
output2 = relay.Tuple([call_11555,bop_11583,call_11592,])
func_11593 = relay.Function([], output)
mod['func_11593'] = func_11593
mod = relay.transform.InferType()(mod)
mutated_mod['func_11593'] = func_11593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11593_call = mutated_mod.get_global_var('func_11593')
call_11594 = func_11593_call()
output = call_11594
func_11595 = relay.Function([], output)
mutated_mod['func_11595'] = func_11595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8179_call = mod.get_global_var('func_8179')
func_8181_call = mutated_mod.get_global_var('func_8181')
call_11616 = func_8179_call()
call_11617 = func_8179_call()
func_6204_call = mod.get_global_var('func_6204')
func_6206_call = mutated_mod.get_global_var('func_6206')
call_11618 = relay.TupleGetItem(func_6204_call(), 0)
call_11619 = relay.TupleGetItem(func_6206_call(), 0)
func_8439_call = mod.get_global_var('func_8439')
func_8441_call = mutated_mod.get_global_var('func_8441')
call_11622 = relay.TupleGetItem(func_8439_call(), 0)
call_11623 = relay.TupleGetItem(func_8441_call(), 0)
func_3639_call = mod.get_global_var('func_3639')
func_3641_call = mutated_mod.get_global_var('func_3641')
call_11631 = relay.TupleGetItem(func_3639_call(), 0)
call_11632 = relay.TupleGetItem(func_3641_call(), 0)
output = relay.Tuple([call_11616,call_11618,call_11622,call_11631,])
output2 = relay.Tuple([call_11617,call_11619,call_11623,call_11632,])
func_11633 = relay.Function([], output)
mod['func_11633'] = func_11633
mod = relay.transform.InferType()(mod)
output = func_11633()
func_11634 = relay.Function([], output)
mutated_mod['func_11634'] = func_11634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4489_call = mod.get_global_var('func_4489')
func_4490_call = mutated_mod.get_global_var('func_4490')
call_11649 = relay.TupleGetItem(func_4489_call(), 0)
call_11650 = relay.TupleGetItem(func_4490_call(), 0)
output = call_11649
output2 = call_11650
func_11668 = relay.Function([], output)
mod['func_11668'] = func_11668
mod = relay.transform.InferType()(mod)
mutated_mod['func_11668'] = func_11668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11668_call = mutated_mod.get_global_var('func_11668')
call_11669 = func_11668_call()
output = call_11669
func_11670 = relay.Function([], output)
mutated_mod['func_11670'] = func_11670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11146_call = mod.get_global_var('func_11146')
func_11147_call = mutated_mod.get_global_var('func_11147')
call_11694 = relay.TupleGetItem(func_11146_call(), 1)
call_11695 = relay.TupleGetItem(func_11147_call(), 1)
output = call_11694
output2 = call_11695
func_11702 = relay.Function([], output)
mod['func_11702'] = func_11702
mod = relay.transform.InferType()(mod)
mutated_mod['func_11702'] = func_11702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11702_call = mutated_mod.get_global_var('func_11702')
call_11703 = func_11702_call()
output = call_11703
func_11704 = relay.Function([], output)
mutated_mod['func_11704'] = func_11704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_11776 = relay.TupleGetItem(func_4872_call(), 2)
call_11777 = relay.TupleGetItem(func_4873_call(), 2)
var_11781 = relay.var("var_11781", dtype = "float64", shape = (22, 5))#candidate|11781|(22, 5)|var|float64
bop_11782 = relay.divide(call_11776.astype('float32'), relay.reshape(var_11781.astype('float32'), relay.shape_of(call_11776))) # shape=(22, 5)
bop_11785 = relay.divide(call_11777.astype('float32'), relay.reshape(var_11781.astype('float32'), relay.shape_of(call_11777))) # shape=(22, 5)
output = bop_11782
output2 = bop_11785
func_11796 = relay.Function([var_11781,], output)
mod['func_11796'] = func_11796
mod = relay.transform.InferType()(mod)
mutated_mod['func_11796'] = func_11796
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11797 = relay.var("var_11797", dtype = "float64", shape = (22, 5))#candidate|11797|(22, 5)|var|float64
func_11796_call = mutated_mod.get_global_var('func_11796')
call_11798 = func_11796_call(var_11797)
output = call_11798
func_11799 = relay.Function([var_11797], output)
mutated_mod['func_11799'] = func_11799
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11903 = relay.const([[[-9,-7,-3,-4,7,1],[2,9,3,-6,-6,10],[7,-5,-6,-4,-7,-2],[5,7,-5,-8,-2,-8],[-9,-3,-1,8,-3,-9],[-4,-3,-4,-1,-1,5],[-7,-5,-7,3,-9,2],[-9,8,-5,-10,9,-2],[-10,-4,-1,9,1,8],[8,6,8,-5,-8,9],[-1,-2,6,-5,-7,9],[9,10,3,10,9,-7],[3,4,-7,5,-5,10]],[[3,8,-8,1,-7,9],[-9,1,4,5,-2,-1],[3,8,-6,-9,-8,10],[6,-3,-2,-2,1,9],[1,-5,2,-3,3,-2],[4,8,8,7,-1,6],[-3,6,-4,-1,8,10],[-5,6,-8,7,-2,3],[-4,4,9,9,-10,9],[-10,1,-8,2,5,1],[8,5,-6,-10,9,6],[-3,1,1,-9,2,-1],[-10,4,-10,-1,7,-6]],[[6,-3,-9,-4,-5,-8],[-7,-9,9,-9,-2,-6],[-2,-1,-7,-1,-5,10],[3,-8,1,7,5,6],[8,2,-2,2,-7,2],[4,-9,-8,-2,-2,-1],[6,-2,-6,2,-8,3],[3,4,2,4,-9,-2],[-1,-10,-5,-8,1,-10],[8,2,-6,-6,4,-1],[-5,-2,-7,3,-1,2],[8,-4,8,7,-6,2],[7,1,7,8,8,-8]],[[6,-4,6,10,-4,2],[-8,9,-1,-6,-10,-8],[10,9,-5,2,10,-8],[-1,-10,-5,-8,5,-7],[-10,-3,-1,-7,6,-8],[5,-4,-5,1,3,3],[-6,-10,-10,-7,9,3],[10,2,8,-1,-9,7],[-9,2,-2,1,5,10],[8,8,-9,9,10,7],[1,-2,5,6,10,8],[-4,1,-10,-7,-10,6],[-5,-9,6,5,-6,-8]],[[6,6,4,9,5,-9],[3,-1,-2,-4,-4,2],[-3,-7,-3,1,-3,-7],[-3,6,8,-10,3,6],[2,2,7,6,-10,8],[-2,-5,7,1,-8,-9],[4,9,-3,-5,-9,1],[-1,-5,-1,-6,-3,7],[5,-4,-5,-1,-2,-6],[-7,2,-8,-1,1,3],[8,-7,2,-3,-2,-10],[-7,5,3,-6,2,6],[2,-10,3,7,5,-2]],[[-9,-4,9,-9,-6,8],[8,10,2,2,5,-7],[7,10,9,9,-5,1],[6,4,4,1,-6,2],[9,3,7,-2,5,6],[-2,-6,-7,-4,-6,-5],[2,2,7,7,-9,-7],[4,1,-1,-5,-2,-1],[7,2,-6,4,10,-6],[-2,-10,7,5,9,1],[5,-3,9,5,-3,-1],[-1,7,-1,-8,-7,-3],[-8,-6,-6,-6,-4,-7]],[[-5,1,7,-5,7,2],[6,-2,-8,9,-3,2],[-3,2,7,10,-10,-8],[-3,9,-6,9,-1,-6],[7,-7,-2,2,9,-3],[-1,-8,6,-2,-8,10],[-2,-9,3,1,3,-10],[9,2,-6,-4,-2,2],[8,-8,4,2,8,-10],[7,10,-1,8,-2,8],[9,-7,-4,-8,2,9],[-5,-4,4,-5,5,-4],[-4,8,5,6,-10,5]],[[-1,-6,-1,2,10,1],[10,-5,-1,-5,1,3],[-9,-8,-1,5,-5,8],[10,4,-6,1,10,4],[7,6,-3,4,7,3],[6,-3,-10,9,-1,-7],[-7,-2,8,-6,-5,3],[-3,-10,-2,10,10,10],[-6,-10,-3,1,-7,7],[-3,10,-7,-6,3,-1],[-10,4,-6,-1,-5,-9],[-10,-8,-5,4,-10,-6],[1,-7,9,-9,1,-10]],[[-8,-9,-4,1,9,2],[-6,4,1,3,1,6],[10,-10,1,-7,-8,3],[-3,5,6,7,-4,-10],[-10,-8,-4,2,2,-4],[9,5,8,-1,-4,4],[-6,4,2,4,8,5],[-6,8,9,4,-3,-9],[-7,-5,-9,-1,-2,4],[8,5,9,7,-9,5],[5,7,-8,-3,7,6],[-7,-2,9,-2,-1,2],[-9,5,-2,-5,2,8]],[[-8,-5,-9,4,5,4],[9,2,4,-2,-10,2],[-9,-10,-1,-1,7,6],[6,-3,-6,-6,4,-9],[-1,-3,9,-5,-4,-1],[1,-4,7,-8,1,-5],[-8,-4,-10,-3,3,4],[-3,2,3,-4,5,-7],[-1,-7,-6,-9,-5,9],[5,6,9,-10,10,2],[7,-2,-6,-7,5,9],[-6,8,-1,-5,-6,-4],[5,-7,-8,-10,7,-5]]], dtype = "uint64")#candidate|11903|(10, 13, 6)|const|uint64
var_11904 = relay.var("var_11904", dtype = "uint64", shape = (10, 13, 6))#candidate|11904|(10, 13, 6)|var|uint64
bop_11905 = relay.bitwise_xor(const_11903.astype('uint64'), relay.reshape(var_11904.astype('uint64'), relay.shape_of(const_11903))) # shape=(10, 13, 6)
var_11911 = relay.var("var_11911", dtype = "uint64", shape = (10, 13, 6))#candidate|11911|(10, 13, 6)|var|uint64
bop_11912 = relay.not_equal(var_11904.astype('bool'), relay.reshape(var_11911.astype('bool'), relay.shape_of(var_11904))) # shape=(10, 13, 6)
func_3973_call = mod.get_global_var('func_3973')
func_3976_call = mutated_mod.get_global_var('func_3976')
var_11937 = relay.var("var_11937", dtype = "float32", shape = (660,))#candidate|11937|(660,)|var|float32
call_11936 = relay.TupleGetItem(func_3973_call(relay.reshape(var_11937.astype('float32'), [5, 12, 11])), 1)
call_11938 = relay.TupleGetItem(func_3976_call(relay.reshape(var_11937.astype('float32'), [5, 12, 11])), 1)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_11940 = func_7812_call()
call_11941 = func_7812_call()
output = relay.Tuple([bop_11905,bop_11912,call_11936,var_11937,call_11940,])
output2 = relay.Tuple([bop_11905,bop_11912,call_11938,var_11937,call_11941,])
func_11944 = relay.Function([var_11904,var_11911,var_11937,], output)
mod['func_11944'] = func_11944
mod = relay.transform.InferType()(mod)
mutated_mod['func_11944'] = func_11944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11944_call = mutated_mod.get_global_var('func_11944')
var_11946 = relay.var("var_11946", dtype = "uint64", shape = (10, 13, 6))#candidate|11946|(10, 13, 6)|var|uint64
var_11947 = relay.var("var_11947", dtype = "uint64", shape = (10, 13, 6))#candidate|11947|(10, 13, 6)|var|uint64
var_11948 = relay.var("var_11948", dtype = "float32", shape = (660,))#candidate|11948|(660,)|var|float32
call_11945 = func_11944_call(var_11946,var_11947,var_11948,)
output = call_11945
func_11949 = relay.Function([var_11946,var_11947,var_11948,], output)
mutated_mod['func_11949'] = func_11949
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11996 = relay.const([[[-2,1,-3,-7],[9,-5,5,-7],[10,7,-3,-3],[7,6,5,-2],[-2,-10,-5,-6],[-7,7,6,6],[-1,-5,4,-1],[-5,-2,3,-7],[6,4,6,-6],[-4,6,6,-7],[5,-3,-1,9],[-1,8,7,-3],[-5,-8,8,8],[8,3,8,-1],[3,1,10,9]],[[2,-7,3,6],[8,10,8,9],[4,10,-1,2],[-6,-5,-6,8],[-2,-9,-9,-6],[10,3,6,6],[4,-9,-8,7],[7,-10,8,10],[-5,6,5,10],[-8,5,-7,-1],[6,5,2,-6],[4,1,-6,-2],[10,-6,2,2],[1,3,8,-8],[-7,-6,5,-9]],[[2,10,10,10],[4,7,-3,5],[6,-3,-3,9],[-4,-8,-1,-9],[-6,10,3,-6],[-7,10,-1,6],[-4,-2,-10,8],[7,6,-4,10],[3,5,-1,10],[1,-8,6,10],[4,8,4,-9],[-3,-9,-9,-6],[9,6,-10,8],[8,-6,1,-8],[-9,-9,4,3]],[[7,6,-1,6],[-4,1,-3,-9],[-6,-7,10,-2],[-4,1,-2,-7],[8,-3,-6,2],[5,5,-2,-9],[9,5,-3,-10],[9,5,8,10],[-3,-9,-6,-8],[4,-9,8,-5],[5,-6,-7,5],[10,9,2,-5],[4,6,5,-1],[7,-5,9,4],[10,-4,6,4]],[[1,-5,-1,-10],[6,-5,9,-2],[-7,3,-7,-9],[7,-5,-5,1],[10,-1,-8,-8],[-6,-7,-10,-3],[-6,-10,-5,1],[6,-7,4,-9],[5,7,-2,8],[-9,-4,4,3],[-4,-2,-6,1],[8,5,5,8],[5,-3,-2,6],[6,10,5,-9],[-10,10,-3,-8]],[[-8,-4,-8,-2],[8,9,-6,1],[4,1,7,-2],[10,-3,-2,5],[5,-10,-10,5],[8,7,-10,8],[-10,-7,1,-5],[1,6,-10,-3],[10,7,6,7],[-5,-9,-3,-1],[8,-9,7,-1],[-2,4,-10,7],[10,10,-4,-1],[-3,4,-9,-6],[-2,9,-1,-10]],[[9,-4,-8,-9],[-7,-6,7,-1],[-10,-4,-1,10],[-9,5,-9,-2],[-8,5,9,6],[-2,8,10,10],[4,10,8,9],[9,7,8,4],[8,-3,5,5],[-2,7,-10,-1],[-4,-10,-1,10],[-4,7,6,7],[3,1,1,-5],[8,-6,-10,-3],[-10,-5,-3,-2]],[[-1,8,-10,-9],[8,9,7,2],[-6,4,-5,-10],[-1,7,-9,-10],[6,8,-4,9],[9,1,9,-3],[-4,-3,-3,6],[-8,-9,-2,9],[-10,5,4,-8],[-9,-10,4,7],[10,9,-1,-9],[-7,-7,-1,10],[1,-5,-7,-9],[2,9,5,-4],[-4,-10,7,5]],[[2,-5,-6,2],[10,4,2,6],[-7,10,8,6],[-6,-8,-10,6],[-3,-2,-8,10],[-6,5,-10,-10],[5,8,3,-5],[2,1,-6,-3],[10,2,4,7],[-6,5,-5,-4],[6,-4,-8,7],[4,-4,-7,-9],[-2,6,-3,-5],[-7,-7,-5,5],[-3,-2,7,10]],[[9,2,-1,-2],[2,-1,3,5],[4,4,-3,5],[-7,-6,6,6],[10,-9,8,3],[9,6,10,4],[3,5,7,1],[-5,-6,1,-6],[9,1,9,7],[8,2,5,1],[-1,4,-6,-2],[10,-4,2,-3],[7,10,9,-6],[1,4,1,3],[-4,2,10,3]],[[-1,-4,-10,4],[2,-5,-1,6],[6,-1,-7,-9],[-1,-1,4,-2],[2,8,4,9],[-7,-5,-5,2],[2,6,-8,-8],[-7,-2,2,4],[2,6,-5,10],[-1,-10,-7,-6],[8,6,-1,4],[5,9,-2,1],[-6,-9,-4,-2],[-5,9,-7,-9],[-9,10,3,-7]],[[2,6,-8,7],[6,4,-3,4],[9,10,-10,-2],[7,-10,7,-9],[-3,2,-3,-5],[3,10,-8,-5],[-10,2,5,-1],[-5,3,8,3],[-8,-5,6,-2],[1,-8,-6,5],[-10,-8,-2,-9],[7,1,5,-7],[10,4,3,-6],[7,1,-7,-3],[-5,3,-7,-6]],[[-4,2,-2,-2],[2,-8,-3,-7],[-8,-6,-7,5],[-10,-1,1,-1],[-4,-6,-1,-7],[-6,6,-3,10],[3,8,6,4],[-2,-1,2,-9],[7,1,4,1],[-6,9,-1,-1],[-6,-6,2,8],[-7,-6,3,5],[9,-7,7,2],[6,5,2,-4],[4,-1,-2,-2]],[[-10,-9,-2,-4],[-4,5,-1,-7],[10,-6,7,-1],[2,9,10,4],[-10,4,7,4],[-1,3,9,10],[-9,4,-6,6],[8,1,-7,-10],[8,-8,2,-6],[-4,-4,8,-4],[10,-4,-4,6],[8,-10,4,1],[-3,-9,-2,7],[-6,10,-7,-3],[-4,-5,9,-2]],[[3,-1,3,-1],[10,1,-4,9],[1,6,-4,5],[7,-8,-5,3],[-4,7,6,-2],[-9,-10,3,-5],[-9,-2,-9,2],[-9,4,3,-4],[-2,4,2,-6],[-3,3,8,-10],[-6,-9,-9,3],[-3,6,4,5],[-2,6,9,2],[-10,5,3,-2],[-8,-4,-4,-7]]], dtype = "uint32")#candidate|11996|(15, 15, 4)|const|uint32
var_11997 = relay.var("var_11997", dtype = "uint32", shape = (15, 15, 4))#candidate|11997|(15, 15, 4)|var|uint32
bop_11998 = relay.multiply(const_11996.astype('uint32'), relay.reshape(var_11997.astype('uint32'), relay.shape_of(const_11996))) # shape=(15, 15, 4)
bop_12002 = relay.subtract(var_11997.astype('uint64'), relay.reshape(const_11996.astype('uint64'), relay.shape_of(var_11997))) # shape=(15, 15, 4)
output = relay.Tuple([bop_11998,bop_12002,])
output2 = relay.Tuple([bop_11998,bop_12002,])
F = relay.Function([var_11997,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11997,], output2)
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
