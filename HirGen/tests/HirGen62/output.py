import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_26 = relay.const([[[2.512047,-9.143875,2.781276,4.290887,-2.374991,8.879127],[-8.812206,0.689427,9.697478,2.898142,-4.857761,-1.216305],[9.488296,5.863156,0.654395,-6.391260,-3.005788,0.640172],[8.042317,-4.194675,6.478085,6.756425,-6.945613,-1.540438],[-4.044182,-6.188741,1.863026,1.477111,0.422295,-3.801659],[7.236810,7.067138,-3.113278,4.679495,8.503310,3.623641],[2.781693,-0.184044,-7.677925,7.470930,-4.577146,0.804374],[-1.538615,2.271753,9.183618,1.142641,-5.304377,5.597065],[7.648918,7.415316,-2.335505,8.414306,4.775214,2.932634],[4.440545,-6.226975,0.450750,3.026434,8.419251,3.898438],[7.330392,6.321686,7.801502,-7.474510,-4.338305,9.296935],[-7.259357,-1.115929,-9.214189,3.494628,6.311662,4.241992],[9.766523,-8.516428,8.766834,-3.406945,-2.165144,8.949579]],[[-7.928762,8.753862,8.386979,5.854682,4.999447,2.254932],[2.009194,3.902629,-6.037863,6.871929,-6.578777,-8.274917],[8.984216,-8.903999,6.345977,8.904944,9.671907,-3.315109],[0.097548,-9.292121,6.727428,-0.603963,1.987780,2.327051],[8.616380,8.423360,2.146847,1.779148,-3.851783,-8.324537],[4.494249,6.164072,-1.916890,5.797838,8.977287,7.875208],[7.306300,-0.216706,9.502546,2.601288,-4.514465,-4.821484],[-7.338563,6.667430,6.710594,-2.756396,0.677362,1.991081],[5.337909,-4.273648,1.268402,-2.054908,1.462165,5.403635],[-8.149835,1.158919,3.158359,-4.513890,-4.516236,0.945915],[-2.118268,-7.162365,3.831427,5.909643,3.225925,-2.492879],[0.805878,4.555421,6.945967,-1.175652,0.663885,-6.955911],[4.216844,9.845821,-5.304292,-6.502235,-7.831026,3.977988]],[[-8.688837,3.531112,-6.946064,-0.816243,-6.325442,-3.424440],[-4.461042,1.488835,6.377976,4.070054,3.641573,-9.315327],[0.422175,-0.834405,8.940659,4.443280,-9.767939,3.102232],[-4.443001,0.665219,-2.473017,-8.462566,-7.876080,-2.880704],[-4.462634,-9.829897,-1.027572,5.643414,7.170938,-0.601923],[8.325059,8.519120,-6.286996,-1.677535,-6.009477,5.683526],[-1.503527,-1.140762,5.560930,-6.376208,-0.226094,1.957351],[1.651583,-6.079248,-1.202336,6.900332,-5.930073,-6.755359],[-9.527288,-1.417707,-1.859158,7.450667,3.332217,6.555509],[-0.095841,-8.521602,-7.956098,-8.942682,3.727583,5.814783],[9.741594,4.274790,6.056735,-8.425100,1.377059,-2.941062],[-4.334331,-9.612170,6.163501,-1.763409,7.817524,-9.704000],[2.011592,4.328125,3.850948,-6.527479,7.583256,9.443077]],[[1.702115,-8.841091,-6.530171,-9.395700,-4.639768,-5.741809],[-5.300190,-3.389371,-6.291433,-8.057103,7.210629,-8.162862],[-4.057863,1.355489,-2.240968,-6.560224,-2.538080,-9.171900],[9.192769,1.436534,4.108985,-9.272520,-8.580542,5.359036],[0.041166,-7.575016,8.527021,-6.848401,-3.223745,-2.497895],[-8.283810,-0.840788,9.576998,7.872887,-1.782696,8.668058],[-9.266309,0.901403,-0.677737,4.631889,-4.383791,-8.189709],[-8.682345,2.253087,-4.924189,-8.916712,-9.452923,9.600897],[1.197191,6.281017,8.175056,-3.696216,-7.495499,-2.592839],[-6.687262,-7.664048,-8.462392,6.539371,5.639814,7.346598],[-2.167949,-9.174957,-4.921257,-3.562050,-8.704716,7.109438],[-6.776815,-9.084290,-8.367611,1.693218,-1.581148,2.036210],[-4.287048,-0.779772,-2.540024,4.247849,5.019483,5.869965]],[[4.825979,4.767465,9.573743,4.479216,-5.852783,-4.887358],[4.587970,-4.020829,-1.069433,-9.718961,-3.004071,-8.326313],[-2.853821,3.384818,-9.715835,5.598562,-8.332654,2.408154],[-8.571489,-0.772673,-1.466795,1.211044,-9.946148,-0.398802],[3.107559,-5.255099,4.009977,-1.272360,-2.348448,7.038296],[4.491929,6.974983,2.321721,4.105728,4.871304,6.165720],[3.969643,7.794194,-9.498306,-8.324099,-0.451760,9.003673],[7.008251,5.274506,2.168127,-2.507412,-1.193845,-7.740068],[5.376617,2.673278,6.123092,-4.271076,2.184398,1.112820],[8.064283,8.325103,-9.671564,8.301865,6.822346,4.389891],[4.088905,4.377669,9.197842,-9.063727,5.082730,-6.891416],[-0.997880,3.749428,-2.470846,3.666882,-4.007102,-3.333209],[5.386348,7.055086,-0.723459,5.458448,-2.373207,1.902726]],[[-9.757209,-1.615831,5.016733,7.322493,-3.933875,5.267573],[4.600363,-4.316911,-1.648976,-2.762783,5.986937,-2.459474],[-8.438772,5.978025,-9.395123,7.495496,-4.046354,-9.768716],[-2.293946,7.725613,7.184721,6.463304,5.516813,-2.097657],[-6.926250,9.650664,-3.392177,-8.287127,8.853592,-3.386755],[-9.982297,6.350811,0.608613,3.615992,2.401703,-5.250074],[5.067498,9.087239,-2.881084,-1.601918,-1.771877,-9.352462],[5.855196,0.304811,-7.889781,-6.222753,7.376329,-0.794557],[-1.713527,-3.868915,-8.578519,-6.006454,4.587418,1.921949],[2.316927,-2.689201,1.741231,1.606358,5.541385,-5.816545],[-3.301705,8.560422,-8.176309,-8.255664,3.766761,-2.374813],[-4.792612,1.144235,-9.753814,6.348908,7.592968,0.472965],[-9.579643,1.371087,5.112142,7.954732,4.593186,-4.635093]],[[-0.184028,-4.551886,0.336025,-6.948408,8.344678,2.503257],[-6.757838,2.074564,6.051444,-4.370959,7.265250,1.572683],[2.139479,-4.267541,3.275323,-3.560211,-9.240392,8.256201],[9.048576,5.071235,-8.134446,-8.487291,2.747504,-9.864238],[-3.197709,-8.548350,-8.599197,8.084155,-3.049984,-2.896360],[-1.986559,-0.462729,7.214981,-3.124252,9.262229,7.988792],[6.684660,-6.043627,-1.873390,6.996905,2.826044,-4.049618],[3.033414,-1.067985,-1.259658,-1.907982,3.136124,3.551913],[-4.088332,-8.370103,3.622818,4.838091,9.232362,5.369910],[-1.431131,6.752023,-5.895427,-6.472770,2.533680,5.141135],[9.910838,-7.577838,-5.170478,-9.736125,9.478978,-0.163194],[-8.282583,2.222893,1.502157,7.002894,8.696360,-3.808039],[6.650009,-1.838433,0.938881,-6.754438,5.315716,5.215459]],[[-5.688473,-5.175491,-3.868756,-7.763664,6.647061,9.877423],[-1.629923,-2.662488,1.784486,5.515195,8.431813,6.938555],[7.162008,-7.480142,-9.528199,9.817342,2.401915,-7.279567],[-4.543144,-4.822625,1.917265,2.830313,5.562909,9.884445],[-5.452046,7.163888,-8.941483,-4.192317,-9.611166,-0.314440],[-4.034789,0.044378,-0.883005,-1.917715,-4.469098,-4.075024],[-6.645481,2.897842,6.649748,-2.185700,3.693902,-5.147970],[-9.558571,1.584665,1.795373,0.750977,3.680323,8.459875],[-8.573947,2.960000,-6.324266,-1.985838,0.077052,-3.184807],[0.067809,-3.861719,-8.589804,-4.162014,0.270441,6.368534],[-4.738463,-5.323070,5.978176,3.653266,2.648027,-7.059463],[-3.003516,-5.331272,-8.033857,-3.633155,4.245089,-7.683413],[5.380370,-6.442500,9.397554,1.188811,-9.665243,4.148491]],[[9.216789,-5.050044,0.271407,9.886641,0.785481,7.415637],[-6.081796,3.960351,-2.857249,-8.864237,1.927349,-6.547109],[-1.857796,-7.792917,-8.451136,2.947296,-4.035761,-7.852939],[-9.055226,4.303611,-7.437756,-0.229632,-4.811058,-4.146011],[4.314499,0.117304,-6.072905,0.553705,7.457744,9.792395],[-6.066677,-2.653970,-1.409858,-5.317231,-7.215280,0.554816],[5.438839,4.966510,5.102403,-7.702720,-3.458109,0.385709],[-8.888891,-0.204145,-8.394562,6.446146,-6.341302,2.757779],[-4.852980,5.626112,4.064102,2.287463,-0.979246,5.300088],[2.306402,4.189822,4.683409,-3.020656,7.450972,6.927589],[-2.911911,-1.469183,-8.917899,-8.196356,-3.484334,7.706993],[-8.866562,-4.272340,-7.443586,-2.294633,5.559727,5.267883],[9.239863,-0.130362,-0.986461,-1.188493,-4.721021,5.865252]],[[8.374368,-2.387213,-7.612588,0.032828,-8.088782,4.036570],[2.565218,-0.396921,8.130258,4.504338,7.629338,-6.906081],[-8.449296,8.447066,3.073014,6.347331,-6.225919,-7.786039],[-5.965745,5.838729,7.278137,4.996740,-4.825027,-9.559792],[2.060871,-3.843374,0.740496,2.435510,-0.302380,5.040195],[1.462150,-4.955080,-2.982032,-3.935505,-2.296089,8.887282],[4.651459,7.965004,1.563694,1.686840,5.353609,0.164480],[-4.706720,-7.801910,8.740460,6.684713,2.848139,-7.796189],[-6.801251,-4.436732,-6.523444,8.433393,-3.277217,-2.602017],[-2.072983,-5.356685,1.300014,-1.790664,-6.504099,-6.214597],[-6.480520,2.504001,8.403567,1.569042,-1.975130,4.422014],[-9.709440,-8.207200,0.117597,-1.360792,7.336762,2.957734],[-7.292007,-5.238645,1.730356,1.260034,-1.914386,1.005639]],[[-7.541114,-9.317078,-0.885108,-9.362451,-8.517690,4.454951],[8.766571,2.744681,-9.515697,4.103817,-9.405663,-7.918720],[6.699474,-2.766179,-5.056277,1.851281,-0.868211,3.012929],[8.440803,3.274693,4.924048,8.123275,-6.008765,0.195102],[-9.140932,-9.614404,-7.029304,-1.252262,-7.133280,-3.255185],[-9.472211,7.774334,8.966950,0.984675,-8.634729,-7.855352],[5.254284,-1.502271,-6.116332,-2.150130,7.135131,7.511151],[5.151342,4.588669,-9.553733,-7.784306,0.789488,-8.765265],[2.380393,-3.135266,-3.921175,1.265733,-7.774622,-4.917004],[9.878000,3.044936,5.701246,-0.930169,-0.435063,-3.022056],[8.083818,7.119371,-3.125523,6.133989,1.731214,-2.155505],[-0.119579,6.818784,0.137470,7.436965,2.811924,8.517976],[-0.044136,9.612421,8.635166,4.242156,2.148460,-8.727015]],[[-9.414521,2.437372,6.487186,-7.200796,3.854234,-5.537164],[7.578941,8.257374,2.198998,4.770492,-7.003390,-2.029779],[-6.889291,1.244206,4.067366,1.527976,4.056540,2.383189],[-6.024240,9.884526,-5.082066,1.132955,1.485064,-6.953926],[0.115525,-5.069359,-7.231751,-2.797719,4.766648,-0.660366],[6.099413,-8.395638,-0.527724,9.483405,7.877889,-4.651337],[-4.791854,7.335047,-5.272378,-3.608413,3.191570,-4.496311],[-8.916115,-1.472467,-9.553144,-0.301798,0.923950,-5.211578],[-5.274572,-0.925940,-3.346376,0.104375,-8.694511,4.308930],[-1.706488,1.165039,-9.596517,-2.197896,-9.905203,-1.443771],[8.824894,-1.066130,-4.231346,0.645332,-0.770457,-6.417833],[-7.576223,2.151381,8.664977,-9.168483,7.698080,9.051261],[4.119923,-2.075071,7.762974,-6.927636,7.039329,9.678672]]], dtype = "float64")#candidate|26|(12, 13, 6)|const|float64
uop_27 = relay.atanh(const_26.astype('float64')) # shape=(12, 13, 6)
bop_36 = relay.divide(const_26.astype('float32'), relay.reshape(uop_27.astype('float32'), relay.shape_of(const_26))) # shape=(12, 13, 6)
output = relay.Tuple([bop_36,])
output2 = relay.Tuple([bop_36,])
func_39 = relay.Function([], output)
mod['func_39'] = func_39
mod = relay.transform.InferType()(mod)
output = func_39()
func_40 = relay.Function([], output)
mutated_mod['func_40'] = func_40
mutated_mod = relay.transform.InferType()(mutated_mod)
var_41 = relay.var("var_41", dtype = "float64", shape = (2, 5, 5))#candidate|41|(2, 5, 5)|var|float64
uop_42 = relay.sqrt(var_41.astype('float64')) # shape=(2, 5, 5)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_47 = relay.TupleGetItem(func_39_call(), 0)
call_48 = relay.TupleGetItem(func_40_call(), 0)
uop_53 = relay.erf(call_47.astype('float64')) # shape=(12, 13, 6)
uop_55 = relay.erf(call_48.astype('float64')) # shape=(12, 13, 6)
output = relay.Tuple([uop_42,uop_53,])
output2 = relay.Tuple([uop_42,uop_55,])
func_67 = relay.Function([var_41,], output)
mod['func_67'] = func_67
mod = relay.transform.InferType()(mod)
var_68 = relay.var("var_68", dtype = "float64", shape = (2, 5, 5))#candidate|68|(2, 5, 5)|var|float64
output = func_67(var_68)
func_69 = relay.Function([var_68], output)
mutated_mod['func_69'] = func_69
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_198 = relay.TupleGetItem(func_39_call(), 0)
call_199 = relay.TupleGetItem(func_40_call(), 0)
var_222 = relay.var("var_222", dtype = "float32", shape = (12, 13, 6))#candidate|222|(12, 13, 6)|var|float32
bop_223 = relay.logical_or(call_198.astype('bool'), relay.reshape(var_222.astype('bool'), relay.shape_of(call_198))) # shape=(12, 13, 6)
bop_226 = relay.logical_or(call_199.astype('bool'), relay.reshape(var_222.astype('bool'), relay.shape_of(call_199))) # shape=(12, 13, 6)
const_239 = relay.const([[[8.294011,0.807504,9.640486,4.422832,-9.433884,-3.593875],[-3.765098,-8.128040,5.034791,1.455889,6.207710,7.623685],[-9.651312,1.317840,-7.244985,-5.298979,5.946040,8.168939],[5.632603,-8.202441,-5.836888,7.290335,4.997495,7.067778],[0.897629,-9.058518,3.564918,-2.581726,-9.105998,-3.017535],[-8.570841,-8.784481,-3.430371,9.534511,-9.504242,-0.954773],[-0.052248,-3.699749,8.950202,-4.985050,-2.071805,6.319262],[-2.871584,-6.212352,5.327289,8.072535,8.725941,-7.730998],[1.905072,2.742962,8.985962,9.614333,3.671240,1.808274],[6.172540,8.224512,6.913229,7.699239,-9.074663,-0.605990],[-6.944514,-1.220998,5.339396,-1.325564,-0.296870,1.670598],[3.579619,4.944708,-0.799203,8.469650,-6.238985,8.513820],[-0.252212,0.154926,-0.851396,-9.941884,-8.336204,-0.222341]],[[7.714023,-9.282130,2.131679,6.601696,-6.372592,8.765080],[-8.173583,4.440393,-5.804759,-0.615692,6.965726,9.110560],[9.098462,1.312278,-9.325467,6.290047,-2.251513,3.774811],[2.072119,-5.745899,9.293216,-9.501004,-9.731126,-1.134316],[1.917531,6.603034,8.544486,-4.151794,3.012615,-3.827546],[-0.123824,4.181326,4.699232,-2.468699,-2.445926,5.677130],[-2.003142,4.374180,2.381276,7.784095,-1.997064,4.580285],[-2.919742,-7.613351,5.004767,2.706970,-3.893678,-0.019568],[-6.744737,6.113448,1.754371,-8.549916,-6.589952,3.895417],[-0.609563,-0.092584,8.855685,-7.513603,-8.805732,8.526567],[1.216930,9.863793,-5.318030,9.802803,-7.758696,8.978043],[5.026504,5.918355,5.602210,9.056652,-9.980463,-3.933516],[-6.819899,5.517818,6.537331,-5.343740,8.503323,-2.094732]],[[-5.634535,-9.658479,-8.170849,-8.183994,-1.520594,-4.574724],[-7.839809,0.350100,5.072474,5.053019,-2.535608,-0.096977],[8.811781,-1.625323,-9.196807,-3.295714,-1.708701,3.902329],[-5.590218,5.850673,-9.996508,-4.296155,4.697834,2.805140],[2.465662,-3.457718,0.212534,7.247217,-6.356188,5.965555],[0.688936,6.008240,7.948355,-5.666650,-6.716433,-1.366249],[0.310803,-9.965121,-8.242713,-4.917258,-1.499024,6.206160],[2.454912,-3.424214,-0.151680,6.164191,-5.569564,4.840813],[4.233278,6.170338,2.095020,-9.352421,6.942023,-5.955967],[-7.720435,8.547767,6.022328,-7.523624,-5.240480,-8.128609],[8.321644,-4.901267,-4.739235,9.311016,1.526776,-4.386545],[-2.595310,-2.134299,2.098728,8.615654,5.200902,-8.742883],[6.241119,9.585610,3.012520,-4.370877,8.825623,-0.394240]],[[-1.504437,-5.945394,6.895858,9.643560,6.888561,2.762276],[-1.076917,4.840262,8.605226,-4.645494,-9.950204,-6.330141],[-7.526736,-7.038662,0.983214,0.644886,-7.492052,-0.343576],[-8.857196,3.911099,8.782685,-5.402066,7.810230,2.824215],[5.198720,7.115224,7.144876,-3.680652,-7.748122,-5.652911],[3.254219,-3.465612,3.834701,7.946927,-2.500460,4.905432],[3.332997,7.913665,8.467037,-3.987154,-7.774523,9.047731],[5.061946,2.802971,-3.825696,-5.547168,-0.865237,-0.440879],[2.133571,2.425176,-3.677635,4.276846,6.007756,0.476137],[0.628547,4.334239,5.528537,1.904881,-6.350437,0.372227],[-6.422387,0.650787,-3.148511,-9.172794,8.650950,1.343829],[3.510111,-6.262354,9.058667,6.605646,0.019718,-1.622318],[4.226293,2.178369,1.321758,0.543766,-5.920994,-3.028934]],[[-2.255419,-5.419343,-4.252284,6.989379,-4.671013,-9.826456],[7.235718,-8.210769,6.350864,-8.482604,5.755852,-1.495712],[-1.036773,-9.795091,-5.705439,6.240565,-5.691103,1.562739],[9.162625,-5.467388,-2.894259,8.107749,-0.922867,-3.412709],[-2.153190,3.158790,-8.221798,-4.748656,2.108180,-6.353478],[2.907481,-2.654639,5.671869,0.314292,-0.382346,1.825428],[-2.173715,1.998667,-8.018915,-1.116801,-6.797260,-0.682475],[-9.903170,3.541526,-9.938343,4.518246,0.401344,4.229016],[6.802825,3.612289,-8.959409,-9.517622,3.945418,2.847720],[2.132340,-3.841824,7.984601,3.876565,-5.793788,5.198620],[-2.022356,-8.978895,-1.956492,-5.106788,-6.429841,-6.650117],[-4.400834,-3.276696,-3.358225,-8.582505,9.753174,5.675382],[2.256645,-4.999904,7.923341,-2.202616,7.157860,8.446139]],[[-3.263955,1.808975,1.954473,5.232259,3.753643,3.132019],[-3.020963,5.503428,-9.066497,-2.039141,3.090831,1.374312],[2.935360,-4.595842,9.542958,-4.988084,-5.253651,-6.889726],[1.738029,4.841313,3.847881,-9.118015,-0.867573,-3.166805],[-8.776229,1.549973,0.477884,-7.245778,-6.968631,1.966146],[-3.550635,-7.779467,-6.018553,-3.141740,-1.040196,-9.583345],[-8.730545,4.160816,-1.291659,-7.776908,3.933698,9.401032],[-7.725738,4.786577,-5.296744,-7.349057,-9.668064,9.192693],[-9.669135,2.615841,-8.393842,-0.031462,-3.925270,3.713217],[5.253350,-5.784859,4.033306,-6.608421,4.505639,9.042620],[-4.431301,8.396248,-0.478040,8.517369,-0.750979,9.257589],[-4.906767,-9.576042,-6.054585,-1.794514,3.116832,-7.696352],[-4.386060,-6.002879,-0.303155,5.984491,-8.200334,6.087827]],[[-2.806837,9.289006,2.716941,0.218954,-3.418915,8.521728],[8.624394,6.283287,-2.083116,-8.480616,-3.652887,-1.883357],[-1.895860,8.920692,-0.770910,2.074744,-2.160933,-2.845949],[1.045879,7.692327,8.308988,-0.842051,-3.375627,7.856889],[0.735457,0.175051,-4.874790,-2.105325,-2.438566,1.924998],[7.297556,8.828821,5.262127,7.353930,0.484902,3.221453],[0.491209,7.606245,9.746761,-5.396052,-6.144961,-6.411552],[-0.690968,5.208431,-5.950962,5.136348,9.054640,7.867728],[-3.462848,-2.873976,-6.585961,-2.072105,1.794520,8.272051],[-4.092484,-5.318060,-0.378027,-1.217646,3.161619,3.079055],[-9.073314,9.970118,8.000081,4.108875,-0.199674,6.211458],[8.200978,-0.790450,9.936139,8.915974,-7.790858,2.875009],[-5.842520,8.424798,0.167038,4.278070,5.610227,-9.994488]],[[-9.081327,8.493619,2.219400,1.647163,-6.977011,2.810973],[3.331974,-1.168544,-5.466777,-8.880056,1.302450,7.005232],[-8.032344,-9.905744,2.937818,-8.369423,-4.371104,-9.575872],[-0.371926,-8.822260,-5.259906,6.907251,-3.467429,4.546167],[5.567969,5.154179,2.549174,5.261481,-2.696518,3.271773],[-5.688925,5.794978,3.223127,-4.876394,3.412652,0.031598],[3.907288,2.914478,-0.347110,-5.725811,4.689822,-0.639586],[-8.441681,-0.873164,7.132510,3.076819,-6.155948,1.332101],[-5.392684,8.488785,-5.875774,4.464471,8.355340,-6.803848],[6.050685,1.796816,-2.044750,4.072705,-3.801623,0.751231],[-7.635307,7.266051,3.440072,-7.572321,2.006639,6.789349],[-5.447144,7.355353,-4.365279,5.807865,-6.991866,-9.722804],[-0.726399,-2.586020,5.474109,4.176502,-5.126367,-1.916822]],[[0.085361,2.068486,3.781685,-8.744347,-1.683199,3.225555],[8.139236,-1.399364,-1.084070,4.089683,3.082828,8.551122],[8.039829,-7.474231,8.149444,-0.648387,4.133940,1.623082],[-4.436971,7.152712,8.119019,8.831290,0.195045,1.865741],[-0.120179,8.274897,-2.442638,3.269155,6.043964,8.919920],[-6.474062,7.316121,3.881382,-4.447543,-7.014185,-7.733447],[9.409707,4.306540,-2.859096,-2.836185,0.379854,-1.646035],[-6.649594,3.285837,6.433773,-9.034932,-0.359052,1.122519],[1.275430,-1.335982,5.571700,3.999662,-7.661986,-8.760060],[8.165465,-4.610280,-5.539300,-6.782986,-5.411729,-6.187636],[-6.364700,5.916419,-4.264394,3.271017,4.370312,3.688840],[-7.795028,2.949159,1.664697,3.092554,-6.876565,1.557379],[-0.497474,3.921327,-0.492654,-6.201625,-0.746141,5.992445]],[[2.138999,-8.630271,-6.095904,2.614921,1.482298,-8.590361],[-5.792992,1.580224,4.773391,5.405863,8.244810,-0.976136],[-3.343955,-0.540996,-3.960117,8.334600,-7.040105,-6.236874],[-6.622213,-7.661325,-3.476737,-5.797672,-7.807830,2.587191],[7.668746,-2.536698,3.827034,-3.978961,4.947789,4.613335],[-6.411409,0.135651,-3.322983,-3.393190,-0.746772,-0.467694],[7.581382,1.298821,1.818969,7.743843,-1.626364,5.397181],[-4.039005,1.677978,-5.929419,1.192284,-7.001529,-1.102602],[6.071913,8.427223,1.831567,-2.153317,-0.637914,-4.186425],[2.947823,-9.845210,5.847868,2.515742,9.739630,-8.247241],[5.063331,6.203075,-7.160347,0.181319,-6.118000,8.196996],[-4.223228,-2.338787,-6.814131,-6.874597,-1.233847,1.764282],[-9.954867,5.689400,2.394568,-3.267906,8.289346,-1.895287]],[[1.151942,1.732556,-7.368988,0.272266,4.384944,-6.685901],[-0.913313,6.979446,0.541689,5.751758,4.768387,-3.229720],[-3.576131,-9.143015,-5.632895,1.624829,-2.726657,3.565503],[-6.773738,4.052866,-3.891288,2.538088,6.108321,5.748283],[9.617892,-4.259705,2.451981,9.152387,7.397003,8.633036],[7.283471,9.165053,-2.767558,-0.279320,5.970812,-3.025721],[5.047190,2.679311,-3.043143,-4.034695,8.698627,-0.425833],[4.333958,-8.378104,9.002218,-4.306443,-7.726301,-6.903973],[-1.728511,2.580653,6.907689,5.697583,5.296931,8.448438],[7.932122,9.632720,-6.729460,4.066439,-5.458323,8.803422],[2.732545,-8.319414,2.373727,-2.354223,7.270697,-0.288805],[0.131771,-1.488523,-9.868976,-7.088836,0.635119,-4.856750],[-0.431014,3.490432,1.302737,-1.571002,-3.206919,-4.704189]],[[-2.898265,8.965424,1.997543,-7.426889,5.701942,1.572463],[-7.149082,7.393374,-4.308098,1.567992,6.677848,9.283132],[5.790199,5.587469,-9.008215,-9.929170,9.722612,-3.037605],[1.977283,4.384758,2.449649,-6.275198,7.798986,4.136270],[4.714213,-4.633814,8.976178,0.915721,2.472100,-7.212324],[-4.520934,-6.175592,-3.624492,-7.847879,8.493525,-6.682922],[6.011112,-2.599397,-5.970355,-4.879457,4.251694,-2.916524],[-6.556626,8.659590,5.652005,1.321189,-3.436252,7.278280],[-8.207189,-3.963969,4.439498,5.907611,3.800548,2.821872],[4.429467,8.432795,-4.169130,-5.854501,1.397881,7.391939],[8.372166,6.473416,-1.892100,2.689112,-8.881143,9.618778],[-3.459158,-8.850391,-5.561460,-0.666887,1.797397,-9.191825],[2.888446,-7.192561,5.517350,3.661156,-9.055539,-0.131767]]], dtype = "float32")#candidate|239|(12, 13, 6)|const|float32
bop_240 = relay.minimum(var_222.astype('uint64'), relay.reshape(const_239.astype('uint64'), relay.shape_of(var_222))) # shape=(12, 13, 6)
output = relay.Tuple([bop_223,bop_240,])
output2 = relay.Tuple([bop_226,bop_240,])
func_243 = relay.Function([var_222,], output)
mod['func_243'] = func_243
mod = relay.transform.InferType()(mod)
var_244 = relay.var("var_244", dtype = "float32", shape = (12, 13, 6))#candidate|244|(12, 13, 6)|var|float32
output = func_243(var_244)
func_245 = relay.Function([var_244], output)
mutated_mod['func_245'] = func_245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_292 = relay.TupleGetItem(func_39_call(), 0)
call_293 = relay.TupleGetItem(func_40_call(), 0)
output = relay.Tuple([call_292,])
output2 = relay.Tuple([call_293,])
func_296 = relay.Function([], output)
mod['func_296'] = func_296
mod = relay.transform.InferType()(mod)
mutated_mod['func_296'] = func_296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mutated_mod.get_global_var('func_296')
call_297 = func_296_call()
output = call_297
func_298 = relay.Function([], output)
mutated_mod['func_298'] = func_298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_328 = relay.TupleGetItem(func_39_call(), 0)
call_329 = relay.TupleGetItem(func_40_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_336 = relay.TupleGetItem(func_296_call(), 0)
call_337 = relay.TupleGetItem(func_298_call(), 0)
output = relay.Tuple([call_328,call_336,])
output2 = relay.Tuple([call_329,call_337,])
func_345 = relay.Function([], output)
mod['func_345'] = func_345
mod = relay.transform.InferType()(mod)
output = func_345()
func_346 = relay.Function([], output)
mutated_mod['func_346'] = func_346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_345_call = mod.get_global_var('func_345')
func_346_call = mutated_mod.get_global_var('func_346')
call_353 = relay.TupleGetItem(func_345_call(), 1)
call_354 = relay.TupleGetItem(func_346_call(), 1)
uop_362 = relay.atan(call_353.astype('float32')) # shape=(12, 13, 6)
uop_364 = relay.atan(call_354.astype('float32')) # shape=(12, 13, 6)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_371 = relay.TupleGetItem(func_296_call(), 0)
call_372 = relay.TupleGetItem(func_298_call(), 0)
func_345_call = mod.get_global_var('func_345')
func_346_call = mutated_mod.get_global_var('func_346')
call_374 = relay.TupleGetItem(func_345_call(), 0)
call_375 = relay.TupleGetItem(func_346_call(), 0)
output = relay.Tuple([uop_362,call_371,call_374,])
output2 = relay.Tuple([uop_364,call_372,call_375,])
func_393 = relay.Function([], output)
mod['func_393'] = func_393
mod = relay.transform.InferType()(mod)
mutated_mod['func_393'] = func_393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mutated_mod.get_global_var('func_393')
call_394 = func_393_call()
output = call_394
func_395 = relay.Function([], output)
mutated_mod['func_395'] = func_395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_508 = relay.TupleGetItem(func_296_call(), 0)
call_509 = relay.TupleGetItem(func_298_call(), 0)
uop_512 = relay.sqrt(call_508.astype('float64')) # shape=(12, 13, 6)
uop_514 = relay.sqrt(call_509.astype('float64')) # shape=(12, 13, 6)
bop_516 = relay.less_equal(uop_512.astype('bool'), relay.reshape(call_508.astype('bool'), relay.shape_of(uop_512))) # shape=(12, 13, 6)
bop_519 = relay.less_equal(uop_514.astype('bool'), relay.reshape(call_509.astype('bool'), relay.shape_of(uop_514))) # shape=(12, 13, 6)
func_243_call = mod.get_global_var('func_243')
func_245_call = mutated_mod.get_global_var('func_245')
call_524 = relay.TupleGetItem(func_243_call(relay.reshape(call_508.astype('float32'), [12, 13, 6])), 1)
call_525 = relay.TupleGetItem(func_245_call(relay.reshape(call_508.astype('float32'), [12, 13, 6])), 1)
output = relay.Tuple([bop_516,call_524,])
output2 = relay.Tuple([bop_519,call_525,])
func_537 = relay.Function([], output)
mod['func_537'] = func_537
mod = relay.transform.InferType()(mod)
mutated_mod['func_537'] = func_537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mutated_mod.get_global_var('func_537')
call_538 = func_537_call()
output = call_538
func_539 = relay.Function([], output)
mutated_mod['func_539'] = func_539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_584 = relay.TupleGetItem(func_39_call(), 0)
call_585 = relay.TupleGetItem(func_40_call(), 0)
output = relay.Tuple([call_584,])
output2 = relay.Tuple([call_585,])
func_601 = relay.Function([], output)
mod['func_601'] = func_601
mod = relay.transform.InferType()(mod)
mutated_mod['func_601'] = func_601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mutated_mod.get_global_var('func_601')
call_602 = func_601_call()
output = call_602
func_603 = relay.Function([], output)
mutated_mod['func_603'] = func_603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_539_call = mutated_mod.get_global_var('func_539')
call_661 = relay.TupleGetItem(func_537_call(), 1)
call_662 = relay.TupleGetItem(func_539_call(), 1)
output = call_661
output2 = call_662
func_664 = relay.Function([], output)
mod['func_664'] = func_664
mod = relay.transform.InferType()(mod)
output = func_664()
func_665 = relay.Function([], output)
mutated_mod['func_665'] = func_665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_681 = relay.TupleGetItem(func_39_call(), 0)
call_682 = relay.TupleGetItem(func_40_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_713 = relay.TupleGetItem(func_296_call(), 0)
call_714 = relay.TupleGetItem(func_298_call(), 0)
bop_719 = relay.multiply(call_681.astype('int16'), relay.reshape(call_713.astype('int16'), relay.shape_of(call_681))) # shape=(12, 13, 6)
bop_722 = relay.multiply(call_682.astype('int16'), relay.reshape(call_714.astype('int16'), relay.shape_of(call_682))) # shape=(12, 13, 6)
uop_723 = relay.sin(call_681.astype('float32')) # shape=(12, 13, 6)
uop_725 = relay.sin(call_682.astype('float32')) # shape=(12, 13, 6)
func_345_call = mod.get_global_var('func_345')
func_346_call = mutated_mod.get_global_var('func_346')
call_727 = relay.TupleGetItem(func_345_call(), 1)
call_728 = relay.TupleGetItem(func_346_call(), 1)
var_736 = relay.var("var_736", dtype = "int16", shape = (12, 13, 6))#candidate|736|(12, 13, 6)|var|int16
bop_737 = relay.maximum(bop_719.astype('uint16'), relay.reshape(var_736.astype('uint16'), relay.shape_of(bop_719))) # shape=(12, 13, 6)
bop_740 = relay.maximum(bop_722.astype('uint16'), relay.reshape(var_736.astype('uint16'), relay.shape_of(bop_722))) # shape=(12, 13, 6)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_743 = relay.TupleGetItem(func_601_call(), 0)
call_744 = relay.TupleGetItem(func_603_call(), 0)
bop_751 = relay.power(uop_723.astype('float64'), relay.reshape(call_681.astype('float64'), relay.shape_of(uop_723))) # shape=(12, 13, 6)
bop_754 = relay.power(uop_725.astype('float64'), relay.reshape(call_682.astype('float64'), relay.shape_of(uop_725))) # shape=(12, 13, 6)
func_345_call = mod.get_global_var('func_345')
func_346_call = mutated_mod.get_global_var('func_346')
call_755 = relay.TupleGetItem(func_345_call(), 0)
call_756 = relay.TupleGetItem(func_346_call(), 0)
output = relay.Tuple([call_727,bop_737,call_743,bop_751,call_755,])
output2 = relay.Tuple([call_728,bop_740,call_744,bop_754,call_756,])
func_764 = relay.Function([var_736,], output)
mod['func_764'] = func_764
mod = relay.transform.InferType()(mod)
mutated_mod['func_764'] = func_764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_765 = relay.var("var_765", dtype = "int16", shape = (12, 13, 6))#candidate|765|(12, 13, 6)|var|int16
func_764_call = mutated_mod.get_global_var('func_764')
call_766 = func_764_call(var_765)
output = call_766
func_767 = relay.Function([var_765], output)
mutated_mod['func_767'] = func_767
mutated_mod = relay.transform.InferType()(mutated_mod)
var_779 = relay.var("var_779", dtype = "float32", shape = (13, 5, 6))#candidate|779|(13, 5, 6)|var|float32
uop_780 = relay.sinh(var_779.astype('float32')) # shape=(13, 5, 6)
uop_788 = relay.acosh(var_779.astype('float64')) # shape=(13, 5, 6)
output = relay.Tuple([uop_780,uop_788,])
output2 = relay.Tuple([uop_780,uop_788,])
func_791 = relay.Function([var_779,], output)
mod['func_791'] = func_791
mod = relay.transform.InferType()(mod)
var_792 = relay.var("var_792", dtype = "float32", shape = (13, 5, 6))#candidate|792|(13, 5, 6)|var|float32
output = func_791(var_792)
func_793 = relay.Function([var_792], output)
mutated_mod['func_793'] = func_793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_806 = relay.TupleGetItem(func_296_call(), 0)
call_807 = relay.TupleGetItem(func_298_call(), 0)
var_808 = relay.var("var_808", dtype = "float32", shape = (12, 13, 6))#candidate|808|(12, 13, 6)|var|float32
bop_809 = relay.mod(call_806.astype('float32'), relay.reshape(var_808.astype('float32'), relay.shape_of(call_806))) # shape=(12, 13, 6)
bop_812 = relay.mod(call_807.astype('float32'), relay.reshape(var_808.astype('float32'), relay.shape_of(call_807))) # shape=(12, 13, 6)
func_345_call = mod.get_global_var('func_345')
func_346_call = mutated_mod.get_global_var('func_346')
call_818 = relay.TupleGetItem(func_345_call(), 1)
call_819 = relay.TupleGetItem(func_346_call(), 1)
output = relay.Tuple([bop_809,call_818,])
output2 = relay.Tuple([bop_812,call_819,])
func_823 = relay.Function([var_808,], output)
mod['func_823'] = func_823
mod = relay.transform.InferType()(mod)
var_824 = relay.var("var_824", dtype = "float32", shape = (12, 13, 6))#candidate|824|(12, 13, 6)|var|float32
output = func_823(var_824)
func_825 = relay.Function([var_824], output)
mutated_mod['func_825'] = func_825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_835 = relay.TupleGetItem(func_296_call(), 0)
call_836 = relay.TupleGetItem(func_298_call(), 0)
output = relay.Tuple([call_835,])
output2 = relay.Tuple([call_836,])
func_839 = relay.Function([], output)
mod['func_839'] = func_839
mod = relay.transform.InferType()(mod)
output = func_839()
func_840 = relay.Function([], output)
mutated_mod['func_840'] = func_840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_345_call = mod.get_global_var('func_345')
func_346_call = mutated_mod.get_global_var('func_346')
call_857 = relay.TupleGetItem(func_345_call(), 1)
call_858 = relay.TupleGetItem(func_346_call(), 1)
output = call_857
output2 = call_858
func_859 = relay.Function([], output)
mod['func_859'] = func_859
mod = relay.transform.InferType()(mod)
output = func_859()
func_860 = relay.Function([], output)
mutated_mod['func_860'] = func_860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_867 = relay.TupleGetItem(func_601_call(), 0)
call_868 = relay.TupleGetItem(func_603_call(), 0)
output = relay.Tuple([call_867,])
output2 = relay.Tuple([call_868,])
func_907 = relay.Function([], output)
mod['func_907'] = func_907
mod = relay.transform.InferType()(mod)
output = func_907()
func_908 = relay.Function([], output)
mutated_mod['func_908'] = func_908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_930 = relay.TupleGetItem(func_296_call(), 0)
call_931 = relay.TupleGetItem(func_298_call(), 0)
output = relay.Tuple([call_930,])
output2 = relay.Tuple([call_931,])
func_933 = relay.Function([], output)
mod['func_933'] = func_933
mod = relay.transform.InferType()(mod)
mutated_mod['func_933'] = func_933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_933_call = mutated_mod.get_global_var('func_933')
call_934 = func_933_call()
output = call_934
func_935 = relay.Function([], output)
mutated_mod['func_935'] = func_935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_933_call = mod.get_global_var('func_933')
func_935_call = mutated_mod.get_global_var('func_935')
call_943 = relay.TupleGetItem(func_933_call(), 0)
call_944 = relay.TupleGetItem(func_935_call(), 0)
output = call_943
output2 = call_944
func_952 = relay.Function([], output)
mod['func_952'] = func_952
mod = relay.transform.InferType()(mod)
output = func_952()
func_953 = relay.Function([], output)
mutated_mod['func_953'] = func_953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_539_call = mutated_mod.get_global_var('func_539')
call_1006 = relay.TupleGetItem(func_537_call(), 1)
call_1007 = relay.TupleGetItem(func_539_call(), 1)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
call_1012 = relay.TupleGetItem(func_764_call(relay.reshape(call_1006.astype('int16'), [12, 13, 6])), 3)
call_1013 = relay.TupleGetItem(func_767_call(relay.reshape(call_1006.astype('int16'), [12, 13, 6])), 3)
func_664_call = mod.get_global_var('func_664')
func_665_call = mutated_mod.get_global_var('func_665')
call_1015 = func_664_call()
call_1016 = func_664_call()
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_1025 = relay.TupleGetItem(func_393_call(), 1)
call_1026 = relay.TupleGetItem(func_395_call(), 1)
output = relay.Tuple([call_1006,call_1012,call_1015,call_1025,])
output2 = relay.Tuple([call_1007,call_1013,call_1016,call_1026,])
func_1041 = relay.Function([], output)
mod['func_1041'] = func_1041
mod = relay.transform.InferType()(mod)
mutated_mod['func_1041'] = func_1041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1041_call = mutated_mod.get_global_var('func_1041')
call_1042 = func_1041_call()
output = call_1042
func_1043 = relay.Function([], output)
mutated_mod['func_1043'] = func_1043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_840_call = mutated_mod.get_global_var('func_840')
call_1044 = relay.TupleGetItem(func_839_call(), 0)
call_1045 = relay.TupleGetItem(func_840_call(), 0)
uop_1046 = relay.exp(call_1044.astype('float32')) # shape=(12, 13, 6)
uop_1048 = relay.exp(call_1045.astype('float32')) # shape=(12, 13, 6)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_1049 = relay.TupleGetItem(func_39_call(), 0)
call_1050 = relay.TupleGetItem(func_40_call(), 0)
output = relay.Tuple([uop_1046,call_1049,])
output2 = relay.Tuple([uop_1048,call_1050,])
func_1053 = relay.Function([], output)
mod['func_1053'] = func_1053
mod = relay.transform.InferType()(mod)
output = func_1053()
func_1054 = relay.Function([], output)
mutated_mod['func_1054'] = func_1054
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1055 = relay.var("var_1055", dtype = "bool", shape = (11, 2, 6))#candidate|1055|(11, 2, 6)|var|bool
var_1056 = relay.var("var_1056", dtype = "bool", shape = (11, 2, 6))#candidate|1056|(11, 2, 6)|var|bool
bop_1057 = relay.logical_or(var_1055.astype('bool'), relay.reshape(var_1056.astype('bool'), relay.shape_of(var_1055))) # shape=(11, 2, 6)
output = bop_1057
output2 = bop_1057
func_1071 = relay.Function([var_1055,var_1056,], output)
mod['func_1071'] = func_1071
mod = relay.transform.InferType()(mod)
var_1072 = relay.var("var_1072", dtype = "bool", shape = (11, 2, 6))#candidate|1072|(11, 2, 6)|var|bool
var_1073 = relay.var("var_1073", dtype = "bool", shape = (11, 2, 6))#candidate|1073|(11, 2, 6)|var|bool
output = func_1071(var_1072,var_1073,)
func_1074 = relay.Function([var_1072,var_1073,], output)
mutated_mod['func_1074'] = func_1074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_664_call = mod.get_global_var('func_664')
func_665_call = mutated_mod.get_global_var('func_665')
call_1132 = func_664_call()
call_1133 = func_664_call()
uop_1144 = relay.log2(call_1132.astype('float64')) # shape=(12, 13, 6)
uop_1146 = relay.log2(call_1133.astype('float64')) # shape=(12, 13, 6)
output = relay.Tuple([uop_1144,])
output2 = relay.Tuple([uop_1146,])
func_1160 = relay.Function([], output)
mod['func_1160'] = func_1160
mod = relay.transform.InferType()(mod)
output = func_1160()
func_1161 = relay.Function([], output)
mutated_mod['func_1161'] = func_1161
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1204 = relay.const([[[4,-2,-3,-4],[-1,6,3,-10]],[[8,5,2,2],[9,4,4,10]],[[8,-5,-10,5],[-1,5,-6,7]],[[7,-2,4,-4],[-3,-8,8,6]],[[-10,8,-9,-3],[-3,-4,-3,5]]], dtype = "uint16")#candidate|1204|(5, 2, 4)|const|uint16
const_1205 = relay.const([[[-6,-8,6,4],[6,4,6,-6]],[[-10,-8,1,-8],[-3,-4,2,10]],[[6,10,7,9],[7,-1,-5,-1]],[[5,9,9,6],[-6,9,-4,9]],[[-7,4,-4,-1],[6,-3,-10,8]]], dtype = "uint16")#candidate|1205|(5, 2, 4)|const|uint16
bop_1206 = relay.less_equal(const_1204.astype('bool'), relay.reshape(const_1205.astype('bool'), relay.shape_of(const_1204))) # shape=(5, 2, 4)
var_1209 = relay.var("var_1209", dtype = "bool", shape = (5, 2, 4))#candidate|1209|(5, 2, 4)|var|bool
bop_1210 = relay.logical_xor(bop_1206.astype('int32'), relay.reshape(var_1209.astype('int32'), relay.shape_of(bop_1206))) # shape=(5, 2, 4)
func_791_call = mod.get_global_var('func_791')
func_793_call = mutated_mod.get_global_var('func_793')
const_1214 = relay.const([[3.525218,-9.065151,-5.159232,-1.568918,2.379931,7.124220,-6.973138,9.331385,-2.401868,5.394195,-7.115160,5.390275,8.911463,3.702681,-7.162352,-2.349176,0.829763,7.116311,0.077436,-7.988097,-7.934491,2.923767,-6.654960,-5.578174,0.126047,8.569988,-0.729243,-0.894798,5.713048,-7.613977,-1.862483,8.986631,6.801521,-1.686534,7.859939,5.731927,-2.248320,-7.623310,-9.278324,-9.112094,-5.632334,8.565220,-0.011403,-8.376273,3.888308,7.229888,2.289161,-3.134118,4.590853,-0.544194,6.157061,-7.107148,-7.233339,-7.933457,-3.197791,-1.687429,-9.670425,7.687023,0.434385,-2.339103,-3.824307,7.963069,-2.079512,9.357165,-5.907531,-9.521170,5.525769,5.131779,6.941109,-1.372508,-7.706866,0.373788,-0.437712,2.378458,-5.308733,7.611501,0.265297,9.454838,-9.149300,9.483402,-0.773830,-2.415832,3.734589,9.102236,8.815134,-1.942000,-3.899797,-5.270840,-7.061507,1.439786,1.502315,-3.244392,9.241652,-9.231106,-9.191679,-3.169414,-1.874349,-1.652632,-6.391986,-5.864320,-5.625288,-6.448972,-7.257242,9.090892,-7.344739,-6.069891,7.495508,9.509810,-2.296769,-4.450461,3.687276,9.386121,2.924963,3.099528,5.855433,5.488054,-2.740539,-0.898366,-9.764544,-1.544542,-9.085680,-3.702661,2.193136,-0.062045,-6.644356,-4.113973,6.168688,9.005284,5.218334,1.519089,-5.590446,-7.803008,-4.536500,-7.821165,3.858860,7.644891,3.329535,8.943864,6.976295,-3.739200,9.142587,-8.788707,-4.691772,1.591043,-4.542027,-4.404018,-0.971507,-5.395301,4.531715,0.449212,7.537407,6.881956,1.820828,4.102842,-2.338820,-6.077479,-4.953824,6.446337,-2.672118,-4.769801,9.454057,4.881329,-3.891199,-6.650061,-2.025725,-4.646804,-0.630273,-6.078329,-3.774828,3.547402,3.432333,-9.410072,-0.970742,-9.221987,0.994494,4.174691,9.428431,-2.091208,-4.873274,-8.593254,-8.315555,-8.316359,-9.403829,-1.221536,-9.863270,9.872380,7.654099,5.476441,8.398540,-7.365225,0.769183,5.144899,8.830593,-1.690138,-9.264554,-0.453639,1.082473,-3.954576,-0.095260,-6.763773,-7.106711,-0.841609,-8.558714,4.486948,-7.301498,-3.739739,7.665230,-1.788026,5.993671,6.398312,3.235145,-7.961874,-9.678976,-2.910421,-7.115721,-7.753871,0.060074,-2.449852,-0.623895,5.804368,-0.999269,-2.727712,-0.020328,-5.262954,8.065562,2.347612,1.342102,6.648819,-8.261129,-3.584402,5.423743,8.122937,-2.977267,-5.023658,7.128513,3.618031,5.751494,-8.218423,-6.213297,4.084732,-6.872986,2.996926,-7.719738,3.897582,-7.027368,9.692671,-6.501293,-6.525273,9.470268,-7.197337,8.019943,-4.229032,5.982329,-7.899280,8.691886,-9.111553,-8.880351,3.464565,-9.071138,-8.424073,1.418521,-1.014746,-2.226695,-7.718362,0.089020,0.523709,-1.181459,0.579851,-6.070795,0.813616,0.698892,9.135756,0.355112,3.491207,2.541836,6.173179,5.187486,7.572545,-2.202430,1.763944,-3.028016,-8.345652,-3.624835,-4.501034,4.415748,-2.893423,9.122316,2.520386,0.543024,6.514997,-8.096910,2.714942,-0.185137,1.276932,-9.989294,2.208816,9.640433,0.200364,9.611907,-4.051217,9.663746,-9.129842,-9.905724,-6.292474,-7.349951,7.141526,-1.934305,-1.106862,4.404395,7.982821,1.961398,-8.532953,6.528157,-7.209144,9.151870,5.994648,-5.658040,-7.825541,9.188995,-0.386255,-1.454766,-3.026695,-1.476221,4.170483,0.969752,1.820877,0.385257,0.052922,7.265310,-1.349156,0.722134,5.187697,7.785033,-6.148519,-0.612586,-2.955096,-8.307141,8.413066,5.179592,-2.069016,-8.214379,3.132210,3.735843,-6.220964,4.797585,-4.589259,-8.624166,-3.524338,8.585768,7.630147,1.987326,-5.890839,-5.256861,-5.256733,-1.535556,-2.768717,-2.287993,5.660952,4.248728,-7.384949,-5.537345,6.756956,-7.531378,-5.092655,-3.258440,-9.067510,0.788000,-0.661153,-4.139576,1.621727,8.827812,3.713009,-3.789836,-5.823735,-7.480091,-3.051922,2.465530,-4.862169,2.844745,3.093606,-7.916071,6.591235,-6.003986,4.258072,-1.745413,9.187125,8.124010,2.007755,1.664321,4.462244]], dtype = "float32")#candidate|1214|(1, 390)|const|float32
call_1213 = relay.TupleGetItem(func_791_call(relay.reshape(const_1214.astype('float32'), [13, 5, 6])), 0)
call_1215 = relay.TupleGetItem(func_793_call(relay.reshape(const_1214.astype('float32'), [13, 5, 6])), 0)
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_1220 = relay.TupleGetItem(func_907_call(), 0)
call_1221 = relay.TupleGetItem(func_908_call(), 0)
bop_1225 = relay.power(bop_1206.astype('float32'), relay.reshape(var_1209.astype('float32'), relay.shape_of(bop_1206))) # shape=(5, 2, 4)
func_537_call = mod.get_global_var('func_537')
func_539_call = mutated_mod.get_global_var('func_539')
call_1235 = relay.TupleGetItem(func_537_call(), 1)
call_1236 = relay.TupleGetItem(func_539_call(), 1)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_1239 = relay.TupleGetItem(func_601_call(), 0)
call_1240 = relay.TupleGetItem(func_603_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_1243 = relay.TupleGetItem(func_296_call(), 0)
call_1244 = relay.TupleGetItem(func_298_call(), 0)
bop_1251 = relay.logical_or(bop_1206.astype('bool'), relay.reshape(var_1209.astype('bool'), relay.shape_of(bop_1206))) # shape=(5, 2, 4)
output = relay.Tuple([bop_1210,call_1213,const_1214,call_1220,bop_1225,call_1235,call_1239,call_1243,bop_1251,])
output2 = relay.Tuple([bop_1210,call_1215,const_1214,call_1221,bop_1225,call_1236,call_1240,call_1244,bop_1251,])
func_1257 = relay.Function([var_1209,], output)
mod['func_1257'] = func_1257
mod = relay.transform.InferType()(mod)
var_1258 = relay.var("var_1258", dtype = "bool", shape = (5, 2, 4))#candidate|1258|(5, 2, 4)|var|bool
output = func_1257(var_1258)
func_1259 = relay.Function([var_1258], output)
mutated_mod['func_1259'] = func_1259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_1269 = relay.TupleGetItem(func_601_call(), 0)
call_1270 = relay.TupleGetItem(func_603_call(), 0)
output = relay.Tuple([call_1269,])
output2 = relay.Tuple([call_1270,])
func_1272 = relay.Function([], output)
mod['func_1272'] = func_1272
mod = relay.transform.InferType()(mod)
output = func_1272()
func_1273 = relay.Function([], output)
mutated_mod['func_1273'] = func_1273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_1276 = relay.TupleGetItem(func_393_call(), 1)
call_1277 = relay.TupleGetItem(func_395_call(), 1)
func_243_call = mod.get_global_var('func_243')
func_245_call = mutated_mod.get_global_var('func_245')
call_1278 = relay.TupleGetItem(func_243_call(relay.reshape(call_1276.astype('float32'), [12, 13, 6])), 1)
call_1279 = relay.TupleGetItem(func_245_call(relay.reshape(call_1276.astype('float32'), [12, 13, 6])), 1)
output = relay.Tuple([call_1276,call_1278,])
output2 = relay.Tuple([call_1277,call_1279,])
func_1291 = relay.Function([], output)
mod['func_1291'] = func_1291
mod = relay.transform.InferType()(mod)
mutated_mod['func_1291'] = func_1291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mutated_mod.get_global_var('func_1291')
call_1292 = func_1291_call()
output = call_1292
func_1293 = relay.Function([], output)
mutated_mod['func_1293'] = func_1293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1328 = relay.var("var_1328", dtype = "float64", shape = ())#candidate|1328|()|var|float64
const_1329 = relay.const([[[4.387966,-5.551718,3.479633,-5.166999,0.368054,3.652356,-5.030167,-4.135121,-5.507817,1.328048,-9.071277],[9.265488,-0.503329,2.459144,-6.993405,2.516922,0.736749,-6.876371,-6.503288,-2.753510,-1.608210,-3.185015],[8.688072,-7.486607,6.888870,-0.944095,6.370487,0.633223,-4.696317,8.083386,2.303798,-9.026448,-0.017594],[0.106062,7.314042,9.059969,9.883698,-7.003145,-2.575055,4.863793,-4.262595,6.198424,3.632796,3.302931],[-2.682591,2.620425,1.116240,-7.867088,-5.225176,-7.209055,7.617637,8.967717,-2.686868,-7.094628,-2.943894],[-8.477380,9.762425,-6.024714,-6.090447,-0.756761,-5.012679,-9.254887,7.997779,-1.217549,-4.781754,6.812452]],[[-7.297269,4.482246,-7.042002,0.664974,8.040838,1.667267,-8.304893,9.566716,-0.953347,4.723014,5.510580],[-1.987003,-2.590717,-9.718000,-0.709826,-6.638843,-7.635692,0.649975,7.530444,0.858164,-2.635111,-3.701608],[-4.263707,6.631600,9.223048,-1.572905,-8.414587,-9.482336,1.618339,5.543620,-0.755389,-8.099311,6.114712],[-8.616863,-5.795480,9.441668,-1.204541,7.368156,-3.095187,1.311251,8.593111,-5.868125,1.983954,-4.845035],[-7.282913,-9.003162,-0.336849,0.032866,-1.297247,-9.750049,-5.836527,4.161827,5.606655,3.312208,0.668651],[-8.894065,-5.450129,-4.263385,0.783003,-6.698747,-3.026203,-8.686365,4.677490,7.504206,5.858353,9.169705]],[[0.291927,0.698062,6.918973,-4.977177,0.988878,-1.239650,-6.076130,5.371819,6.642376,1.978538,-9.459075],[-5.471137,7.660686,2.525985,-8.564268,-3.944871,7.527689,-1.324272,9.094098,0.393357,8.258350,-8.113259],[-0.453309,7.731537,-1.947320,-4.043943,4.963587,-3.115813,-0.604111,7.004504,-1.171857,-7.044903,3.146352],[5.488870,-4.753731,-0.224786,-0.005108,5.289275,-8.122514,-0.835704,9.704692,-0.078777,-6.577038,6.361996],[-8.428050,3.473064,4.363730,1.565548,-3.592597,7.103825,8.002317,4.658034,-6.934664,9.022870,9.700067],[0.563016,-0.758810,7.871076,2.935305,7.395859,-4.345678,-6.841022,-9.500513,-2.029077,-4.083893,8.074528]],[[6.769281,6.980370,8.404650,1.365880,0.509037,3.358251,-3.588240,-4.248175,-2.483551,1.056707,-5.225225],[-4.698570,9.972322,0.440304,-4.991517,-6.421390,1.066260,0.455667,-2.370196,-3.706739,-1.953986,9.112579],[-9.870971,-7.446349,1.774452,7.690280,7.341282,-7.100782,9.091422,5.499093,0.440099,7.404585,7.201491],[5.026272,9.375333,5.561304,-3.930454,-5.158966,-5.543395,3.673334,9.617042,4.028897,-6.302699,9.909923],[-2.782135,5.192424,-7.740977,-8.866582,6.022856,6.169058,9.830565,-7.908643,4.881709,7.873554,4.892064],[1.598405,0.073526,-9.528480,2.691030,0.270459,-9.408048,2.322677,-0.293166,-0.021208,1.099428,-8.073735]],[[2.555784,-9.084196,-7.929239,-8.289814,-3.417092,-3.121120,2.158497,6.540089,-1.918297,-1.719213,5.328541],[-7.126860,2.073932,-6.534504,-8.749832,-2.976851,1.444644,2.209043,-1.455327,-2.444685,6.445434,-3.272557],[8.970399,5.449394,9.506328,-1.215306,0.059322,-0.301920,5.155063,-5.870947,6.907216,0.968073,3.553277],[-3.736530,0.669649,7.452774,4.917626,3.083158,8.289012,3.903466,-4.700289,-7.315522,-3.016339,-8.429387],[4.737157,8.358988,1.432465,0.185346,5.350770,-3.257325,-7.595299,-9.328456,-6.672038,-9.385454,-4.508849],[-0.852556,6.388659,1.913663,1.839548,-3.040661,-9.938806,8.537741,-4.331227,-5.858067,8.049821,-2.365305]],[[-1.725335,3.993519,-1.450487,4.769872,5.705644,6.090250,-1.668428,-6.302082,9.801353,-3.557484,0.252571],[5.019912,-6.055949,8.987465,8.729129,-3.492956,-2.131419,-0.311264,6.531256,-6.961160,5.966636,-0.401981],[-3.992639,6.751768,8.062197,8.953271,2.227449,-6.415133,-7.261155,7.721716,-1.324047,-5.943307,-7.809313],[0.444599,-0.387764,-5.587041,-3.708911,3.269658,-0.412836,-2.017305,-6.288777,-3.497260,-3.681382,9.402192],[-7.840153,-3.329647,-2.888442,-9.613799,6.161474,6.288983,4.267437,4.630247,-4.454280,-7.502607,1.027275],[-6.657079,-7.109870,-1.390323,7.672424,6.787322,-3.035372,-2.802345,-3.852569,6.126624,4.267674,6.419436]],[[5.737304,-3.177737,5.209256,-4.139855,6.103404,-2.811760,3.571866,-9.488761,4.261697,-9.156068,-5.859105],[-8.209781,5.723880,-0.121210,-0.388285,6.439651,2.752086,7.138023,-4.857328,1.467618,-0.654999,3.219274],[-2.995460,7.633890,-6.649646,-9.853907,-7.881476,3.033933,-0.386408,-2.459270,-4.356966,-3.826715,8.725893],[-2.352437,2.707839,9.232283,-1.624183,9.763899,1.754661,-5.886472,2.383731,-1.471404,4.332270,8.430401],[0.058007,1.216848,-4.957823,8.744949,2.672346,1.463775,-1.833361,6.676968,-1.911350,5.167001,7.739772],[4.006445,-9.254071,-4.953081,5.207906,-9.369935,-2.756226,-6.402746,7.952893,-2.639960,-5.787025,-4.326719]],[[2.645690,3.957097,-5.635001,9.516535,-5.812025,-0.723763,-7.831933,-6.356809,7.667298,-4.486418,-8.145476],[-9.747512,7.900343,7.781148,-1.634013,-9.024761,8.087879,5.182018,-9.330666,9.259767,0.556446,-2.720868],[-6.641062,-4.904829,9.256233,6.039946,7.151850,9.042141,0.269181,-3.871393,-7.235397,1.496880,-7.334220],[-2.829297,6.205394,3.728124,3.264724,-8.929313,2.633305,5.694423,5.336758,-5.622487,-6.206369,3.264021],[-7.330269,-6.147582,-7.600418,-6.794730,-3.771654,-0.172951,-7.212933,7.766981,5.299036,-9.142612,-6.076681],[6.974587,-4.190770,-8.063362,0.341092,-1.815025,-7.095552,3.579815,-2.670208,7.985012,-1.524618,-8.913367]],[[-0.220929,-4.049171,0.446916,-4.660744,9.449853,-2.356614,2.334040,-0.806575,-9.554436,6.694355,3.577995],[-6.018441,-3.686015,2.536298,7.447941,-1.811802,8.321131,0.233979,7.009766,-8.437489,1.948579,-3.343054],[4.435479,7.916340,-8.030765,-8.396704,0.712741,9.537679,1.634472,-3.432283,5.694150,-8.881262,-3.964445],[4.614534,0.839154,-2.923423,-1.033073,3.446034,7.731763,-2.375902,5.074725,-0.768195,6.939206,1.642357],[-0.952292,3.493273,-7.667046,-0.135281,2.947715,-3.086870,9.576035,2.772400,9.099075,6.383720,0.844190],[-9.336287,5.380912,-0.159478,5.834149,3.528510,1.373191,0.993061,-5.839899,-3.316524,7.455311,-1.338669]],[[2.088697,6.450287,-2.289818,-8.114255,-0.462071,7.076624,6.543262,-1.828600,6.487668,-4.431453,-6.298391],[-8.856208,9.242157,-1.634006,3.721532,6.837469,-2.751013,3.185884,3.645724,-8.585618,5.652749,0.538007],[6.432435,0.127711,1.769440,-6.609023,5.565984,-0.346365,3.410801,0.029046,1.403760,-5.155872,2.786802],[9.335561,4.967091,-0.447820,6.978640,0.321199,0.743837,6.685432,-2.242177,-4.517019,-6.748143,-8.334829],[8.407433,-3.280376,-7.753052,-2.320272,-4.327365,-2.212719,-1.542072,-9.365590,5.375120,-7.613973,-6.537835],[7.728277,3.825661,-4.501145,3.412991,-6.434004,5.919070,7.924094,2.264606,0.895313,3.814929,3.620752]],[[4.454800,6.472802,2.054543,8.683982,9.911404,-3.795535,8.903192,-9.432577,6.585954,0.887472,5.268622],[-0.077920,9.121671,6.809266,1.194274,-0.867999,-9.300957,9.208722,6.427675,-8.001545,-8.799780,-1.965949],[4.165607,-6.741848,6.718323,0.193998,-8.717504,8.821425,-0.347739,7.802028,6.564240,-5.883454,5.840178],[3.463531,-1.179083,-7.772127,-6.050126,-7.712463,9.570376,-1.144601,6.309235,-2.877032,5.233053,4.652698],[-8.159941,9.460581,-4.479354,7.277288,-5.809148,-0.433356,-6.594258,0.782285,9.549082,8.843634,-9.286854],[2.905546,4.155517,0.295734,3.103057,-2.737787,5.827698,0.848821,4.509659,-8.101971,7.907656,4.803017]],[[1.423813,-8.637716,-5.980090,4.938691,0.998652,-1.655567,-0.144884,5.799688,-1.270187,7.530561,-8.254976],[5.901624,-0.514452,5.860009,0.975536,7.025663,3.720721,2.032162,5.100654,-8.722326,-0.244334,-6.409797],[-6.007784,-1.411354,7.869699,6.261568,6.055866,-7.240909,-2.766416,9.813758,-7.270750,-3.943373,6.487557],[7.499248,-2.949115,7.989463,7.139445,-5.499138,-2.670538,-7.661668,-8.647450,2.475397,0.095278,4.094265],[6.468689,7.192333,-0.783071,6.140658,8.113012,-1.223422,-4.572756,-7.019142,6.187147,3.954919,-7.815980],[-6.856566,8.249729,-0.093243,9.370034,-3.548275,-9.107643,-2.949433,7.664498,-0.188714,-5.748325,8.584541]],[[1.529619,-7.537738,-2.078129,-5.903349,-9.706285,5.931455,-2.947296,-7.062919,-3.026904,-2.819027,-6.350544],[1.246829,-6.679573,-5.134736,-3.151332,4.952505,-5.796130,1.260381,3.722861,0.957486,-1.322200,-2.044126],[-6.532235,-2.753513,9.857174,2.527926,7.647766,-7.759410,4.526711,-9.594743,-4.410881,6.155240,-4.908747],[0.099268,-0.314077,5.513030,0.052649,0.768316,-3.368840,-6.699713,-6.642723,6.319724,-8.839886,8.431084],[-4.696759,-9.262515,0.965320,9.260108,-5.648763,1.287278,7.089660,6.251304,-7.761207,-1.300198,-6.986346],[9.826063,1.155198,-9.901168,-0.452858,8.898359,1.385970,8.687906,2.499307,-9.422052,1.664280,-1.500341]]], dtype = "float64")#candidate|1329|(13, 6, 11)|const|float64
bop_1330 = relay.mod(var_1328.astype('float64'), const_1329.astype('float64')) # shape=(13, 6, 11)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_1336 = relay.TupleGetItem(func_1053_call(), 0)
call_1337 = relay.TupleGetItem(func_1054_call(), 0)
func_664_call = mod.get_global_var('func_664')
func_665_call = mutated_mod.get_global_var('func_665')
call_1340 = func_664_call()
call_1341 = func_664_call()
uop_1345 = relay.rsqrt(const_1329.astype('float32')) # shape=(13, 6, 11)
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_1351 = relay.TupleGetItem(func_39_call(), 0)
call_1352 = relay.TupleGetItem(func_40_call(), 0)
func_1257_call = mod.get_global_var('func_1257')
func_1259_call = mutated_mod.get_global_var('func_1259')
var_1377 = relay.var("var_1377", dtype = "bool", shape = (40,))#candidate|1377|(40,)|var|bool
call_1376 = relay.TupleGetItem(func_1257_call(relay.reshape(var_1377.astype('bool'), [5, 2, 4])), 0)
call_1378 = relay.TupleGetItem(func_1259_call(relay.reshape(var_1377.astype('bool'), [5, 2, 4])), 0)
uop_1381 = relay.log2(uop_1345.astype('float32')) # shape=(13, 6, 11)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
call_1390 = relay.TupleGetItem(func_764_call(relay.reshape(call_1351.astype('int16'), [12, 13, 6])), 2)
call_1391 = relay.TupleGetItem(func_767_call(relay.reshape(call_1351.astype('int16'), [12, 13, 6])), 2)
uop_1408 = relay.asin(uop_1381.astype('float64')) # shape=(13, 6, 11)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
call_1410 = relay.TupleGetItem(func_764_call(relay.reshape(call_1351.astype('int16'), [12, 13, 6])), 4)
call_1411 = relay.TupleGetItem(func_767_call(relay.reshape(call_1351.astype('int16'), [12, 13, 6])), 4)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_1425 = relay.TupleGetItem(func_296_call(), 0)
call_1426 = relay.TupleGetItem(func_298_call(), 0)
output = relay.Tuple([bop_1330,call_1336,call_1340,call_1351,call_1376,var_1377,call_1390,uop_1408,call_1410,call_1425,])
output2 = relay.Tuple([bop_1330,call_1337,call_1341,call_1352,call_1378,var_1377,call_1391,uop_1408,call_1411,call_1426,])
func_1427 = relay.Function([var_1328,var_1377,], output)
mod['func_1427'] = func_1427
mod = relay.transform.InferType()(mod)
var_1428 = relay.var("var_1428", dtype = "float64", shape = ())#candidate|1428|()|var|float64
var_1429 = relay.var("var_1429", dtype = "bool", shape = (40,))#candidate|1429|(40,)|var|bool
output = func_1427(var_1428,var_1429,)
func_1430 = relay.Function([var_1428,var_1429,], output)
mutated_mod['func_1430'] = func_1430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1041_call = mod.get_global_var('func_1041')
func_1043_call = mutated_mod.get_global_var('func_1043')
call_1432 = relay.TupleGetItem(func_1041_call(), 2)
call_1433 = relay.TupleGetItem(func_1043_call(), 2)
output = call_1432
output2 = call_1433
func_1434 = relay.Function([], output)
mod['func_1434'] = func_1434
mod = relay.transform.InferType()(mod)
mutated_mod['func_1434'] = func_1434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1434_call = mutated_mod.get_global_var('func_1434')
call_1435 = func_1434_call()
output = call_1435
func_1436 = relay.Function([], output)
mutated_mod['func_1436'] = func_1436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_1450 = relay.TupleGetItem(func_1053_call(), 0)
call_1451 = relay.TupleGetItem(func_1054_call(), 0)
output = call_1450
output2 = call_1451
func_1456 = relay.Function([], output)
mod['func_1456'] = func_1456
mod = relay.transform.InferType()(mod)
output = func_1456()
func_1457 = relay.Function([], output)
mutated_mod['func_1457'] = func_1457
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1541 = relay.var("var_1541", dtype = "uint64", shape = (10, 14, 14))#candidate|1541|(10, 14, 14)|var|uint64
var_1542 = relay.var("var_1542", dtype = "uint64", shape = (10, 14, 14))#candidate|1542|(10, 14, 14)|var|uint64
bop_1543 = relay.maximum(var_1541.astype('uint64'), relay.reshape(var_1542.astype('uint64'), relay.shape_of(var_1541))) # shape=(10, 14, 14)
uop_1546 = relay.cos(var_1542.astype('float32')) # shape=(10, 14, 14)
output = relay.Tuple([bop_1543,uop_1546,])
output2 = relay.Tuple([bop_1543,uop_1546,])
func_1557 = relay.Function([var_1541,var_1542,], output)
mod['func_1557'] = func_1557
mod = relay.transform.InferType()(mod)
var_1558 = relay.var("var_1558", dtype = "uint64", shape = (10, 14, 14))#candidate|1558|(10, 14, 14)|var|uint64
var_1559 = relay.var("var_1559", dtype = "uint64", shape = (10, 14, 14))#candidate|1559|(10, 14, 14)|var|uint64
output = func_1557(var_1558,var_1559,)
func_1560 = relay.Function([var_1558,var_1559,], output)
mutated_mod['func_1560'] = func_1560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_1562 = relay.TupleGetItem(func_296_call(), 0)
call_1563 = relay.TupleGetItem(func_298_call(), 0)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_1566 = relay.TupleGetItem(func_1053_call(), 1)
call_1567 = relay.TupleGetItem(func_1054_call(), 1)
output = relay.Tuple([call_1562,call_1566,])
output2 = relay.Tuple([call_1563,call_1567,])
func_1571 = relay.Function([], output)
mod['func_1571'] = func_1571
mod = relay.transform.InferType()(mod)
mutated_mod['func_1571'] = func_1571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mutated_mod.get_global_var('func_1571')
call_1572 = func_1571_call()
output = call_1572
func_1573 = relay.Function([], output)
mutated_mod['func_1573'] = func_1573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_840_call = mutated_mod.get_global_var('func_840')
call_1584 = relay.TupleGetItem(func_839_call(), 0)
call_1585 = relay.TupleGetItem(func_840_call(), 0)
func_67_call = mod.get_global_var('func_67')
func_69_call = mutated_mod.get_global_var('func_69')
const_1592 = relay.const([-2.281589,2.325763,5.146191,-8.273484,9.047605,4.844404,9.782892,4.143768,5.515569,3.115117,4.076109,3.746424,2.214602,6.131920,-2.994953,1.279657,8.724587,6.174322,-6.568064,-0.874128,-6.215133,0.046875,4.874708,-7.242060,-5.807543,3.183481,-9.921840,9.538987,6.062326,8.838197,6.392212,-4.296254,8.077534,7.653325,7.917280,7.941098,-0.522919,-2.714265,3.197902,-1.627628,-0.558630,4.236745,-2.440874,-6.683026,0.916252,3.630946,8.832135,3.208417,3.481818,-1.807539], dtype = "float64")#candidate|1592|(50,)|const|float64
call_1591 = relay.TupleGetItem(func_67_call(relay.reshape(const_1592.astype('float64'), [2, 5, 5])), 1)
call_1593 = relay.TupleGetItem(func_69_call(relay.reshape(const_1592.astype('float64'), [2, 5, 5])), 1)
const_1601 = relay.const([[[-9.070686,-1.257339,-6.706849,2.044248,-7.968328,-5.098515],[-5.961922,2.106844,5.670527,6.110439,-5.329811,-2.894452],[-4.031814,-7.681224,4.471919,4.322166,8.835044,4.073558],[-6.581976,4.474046,-4.555408,8.052386,1.117372,2.727766],[4.719763,-2.488195,-5.943086,4.957408,1.830649,5.197284],[7.546672,-9.687781,-0.383967,-0.844906,-9.827752,-2.933323],[6.329541,3.366193,-9.173385,6.944040,6.375204,1.750792],[-0.222791,9.381248,8.917384,9.125245,2.899811,2.517730],[1.560736,-4.578083,-3.938486,-7.974381,3.228786,-7.585053],[-0.251623,8.614868,6.798934,-2.747520,3.160971,-3.514299],[-0.859947,3.066577,2.059831,-4.248117,-4.909559,2.046248],[9.380700,-1.507289,0.427364,-6.852426,3.521053,-2.467253],[-1.533831,-7.438753,-7.064801,-9.445915,-9.117106,-6.200832]],[[7.969922,1.909057,8.432814,-7.967632,-6.176004,7.718349],[8.934710,-8.452177,9.517632,1.073209,9.521399,8.108438],[-2.706116,-9.916536,9.546727,1.567994,6.766884,-3.275841],[9.437466,9.935398,-7.182139,1.219759,-4.986083,-2.115003],[-0.917522,-6.414934,7.485872,6.247741,3.235197,7.586560],[-5.677866,7.586227,4.398920,3.750951,-2.694155,-8.681120],[2.451382,-3.726201,1.112233,-0.730138,7.836907,6.645935],[-9.375829,-9.002127,0.899684,7.604052,-1.889017,4.660263],[-9.957886,-4.098958,-1.311963,1.748887,8.800459,2.277668],[-5.353112,-6.882530,-0.908621,3.046504,6.105883,7.772377],[9.452819,-0.192694,2.822217,1.258216,-8.424393,2.180949],[-9.146319,5.318127,-8.777155,0.303283,-1.198212,-8.586830],[6.317479,2.238534,-1.615406,0.371576,5.626375,9.960451]],[[-9.370286,6.548226,8.540333,9.186505,7.866257,2.210568],[9.220861,0.905350,-5.281498,5.881185,5.453612,-9.354163],[7.276770,6.145866,-9.754305,4.075506,1.969524,5.366503],[0.062992,-2.271158,0.588981,2.580520,-1.461044,-1.625639],[-3.096903,5.188394,1.801330,7.068495,2.877905,9.923933],[-0.006873,-9.626273,1.461104,-1.434559,-9.044019,-2.032419],[-7.726914,2.304832,-9.343950,1.420144,3.016095,-9.672232],[0.046929,6.841393,-2.258778,-7.794382,3.555707,-6.737629],[-8.353856,-1.814836,9.160472,0.819838,-8.930910,2.059011],[-0.522818,4.651602,2.336539,-2.209194,-3.211759,8.055296],[0.425299,8.049986,8.267671,7.606266,-6.074721,-7.533481],[-5.824393,0.890337,-0.932841,7.255608,4.035036,-7.537394],[-4.448290,6.207149,-4.508563,6.620661,-6.579484,5.257229]],[[-3.463947,-1.035675,-7.517582,3.266651,-3.083009,5.271078],[0.366539,6.116598,3.635938,6.242590,4.385740,-9.442614],[0.790325,4.988181,-2.765607,2.081315,0.132885,1.724003],[1.663750,9.517673,9.987251,-6.416823,8.441007,-8.521262],[-3.222331,7.385697,-6.660527,1.072865,2.957350,-2.440742],[4.995081,2.997686,6.445315,-4.429176,8.675578,-6.572489],[-8.570765,1.828597,-4.593400,2.031302,6.177672,-6.364445],[-1.851689,9.456070,-0.025074,-3.019409,-6.730791,1.703204],[-3.849250,-6.666203,9.904040,4.019106,6.137210,3.378489],[-7.249882,-9.630954,3.515855,9.097394,9.697284,-5.920442],[-0.590481,2.805605,-2.192425,-3.850578,3.487573,-0.461155],[6.298634,-3.981828,-1.976545,1.117358,-9.209440,-4.067002],[-2.494703,-9.484745,-3.035459,-7.696009,5.161606,5.764089]],[[-3.422675,-0.138532,-0.239416,-8.323360,-8.409540,8.635039],[-0.485259,6.694341,-2.196804,7.482022,-7.009265,-4.651838],[-0.198608,3.276015,9.319277,7.268578,1.527606,7.132057],[-8.992630,1.692013,-1.615211,7.550928,4.240444,-1.170712],[-4.712627,0.015681,9.140455,6.184031,-8.830147,6.080911],[-0.969421,2.227443,-2.621783,8.513568,-3.877992,-9.021005],[9.917456,5.667395,-3.175674,5.493851,3.169899,5.570081],[-4.669291,-9.995440,-1.074908,-8.017271,-7.573692,-2.360740],[-9.775659,6.240703,-7.463467,-1.882549,0.470965,0.749679],[4.347427,-9.041450,2.798799,5.310210,8.371451,-9.544000],[4.617270,-3.497838,-2.784080,-1.567297,-2.391090,6.740288],[5.345909,9.763153,3.560129,3.950562,8.120712,-9.123241],[0.279631,-0.295442,6.239316,-0.427648,-7.991281,5.495816]],[[2.316530,2.482872,1.962211,3.146320,-4.035762,-9.582122],[0.609201,-4.139426,0.781231,8.314347,-2.508870,5.157711],[-5.249965,-6.688533,-2.174052,7.221165,-1.227792,-4.172635],[2.607149,-4.991895,-5.460764,8.479423,-2.147644,-8.514934],[-7.841776,6.021138,7.078675,9.657305,-4.090822,-0.884193],[8.625312,4.700297,2.682405,6.040170,6.779849,-5.210575],[-3.387398,7.534539,-3.960736,0.646277,2.748351,1.557106],[9.104048,-9.776910,3.011705,0.287784,-9.528829,-4.542977],[-7.411471,-5.837937,3.819195,6.289602,-7.624358,5.654437],[-7.235306,-2.251611,9.671884,-0.099039,-2.679211,-8.169639],[-5.681573,-1.642105,-9.684065,-1.910767,-7.706682,-2.459905],[5.811710,-1.597744,-4.020779,-7.402476,-2.835553,-3.851759],[0.703886,-2.088589,9.947078,4.342257,-0.214609,-0.447523]],[[-4.700943,7.521552,6.569197,-4.707906,3.681546,8.268193],[-1.467556,-5.927619,-4.029134,-1.227043,-9.084326,5.039497],[-8.428232,0.014995,-2.680878,4.221367,-8.715433,6.186493],[4.761570,-5.355907,-1.496921,-7.629922,-0.913993,2.977439],[-1.114918,-1.282765,5.736999,-6.432010,-8.325217,-8.889724],[-6.816517,1.887886,5.146288,-9.569541,-6.640385,2.939902],[-3.630171,-1.542687,5.425666,9.440371,9.841560,-2.440107],[2.769538,-4.769821,-5.535158,-7.427120,5.553455,1.359077],[3.062139,4.121528,-0.140177,-0.009929,-1.676256,8.051910],[3.427978,3.434215,-8.325736,9.241789,6.969653,3.497993],[-7.021416,-7.860376,2.202847,-1.053777,2.080102,4.475900],[4.381336,1.486325,-2.482309,3.961824,5.581788,-8.198216],[-5.075532,-7.464923,-4.495746,0.848216,4.112474,-2.474508]],[[0.408768,1.821487,-1.127836,-4.531982,4.278054,6.617139],[8.495186,8.891826,-2.296472,-7.711482,3.809260,-8.023297],[0.274846,-3.340963,8.231393,0.590723,-8.930099,0.174122],[3.851706,-2.584372,7.176632,-5.563565,-0.194421,-3.009287],[-4.174903,9.203373,7.627933,0.092457,2.577243,7.761021],[-0.124656,2.379545,-5.889663,8.540950,-0.111642,-0.344228],[2.813563,-2.143253,-5.008616,-5.152675,-1.288705,-3.892570],[9.315888,-5.510785,9.890175,2.629907,-0.928535,-5.162992],[-4.335670,1.671429,6.048750,-1.966528,-1.346019,-3.881697],[8.389792,0.499189,-6.374815,5.470829,8.630256,-3.978879],[-6.967909,-6.069872,-1.844714,7.016317,-8.825976,-3.485824],[-6.792914,0.164232,9.699907,2.854226,-0.268499,-6.363683],[-3.455186,3.850692,6.350136,-0.348659,7.222282,0.666543]],[[-4.855015,-2.045198,3.418973,-5.954176,-2.659263,-1.549494],[-0.722745,-7.264753,6.706538,5.710159,4.373977,6.146273],[1.591342,-3.686778,2.751266,-9.064014,-3.446872,-3.504002],[1.020633,9.018214,-7.561662,-1.044346,9.926145,-2.918229],[5.050447,-2.557157,-2.856180,-9.767936,6.959563,-2.722601],[-3.247846,-3.534500,-1.422409,-6.338124,-4.584761,3.161046],[7.953431,3.932255,-7.260187,5.857978,1.987527,-3.189292],[-7.775646,6.610793,0.415212,-3.443171,8.892922,-8.092498],[7.977614,9.883751,-6.063627,0.154625,-3.385361,-6.683569],[-7.985327,9.175543,0.261450,7.669405,-5.095939,-7.430685],[-6.644911,0.116852,6.577046,6.661695,-4.006640,-8.409327],[4.964069,-7.619963,-1.109999,9.179968,2.747682,5.985483],[-4.235353,-5.174350,3.472078,2.790534,4.948562,6.416429]],[[-8.808346,7.283641,-3.670732,-4.697131,5.278523,1.965153],[8.626285,-5.143849,6.645031,-6.323824,-8.800164,-6.141671],[4.556253,-2.097932,-5.150655,2.826984,-4.841990,6.166555],[8.141952,6.182444,6.635342,-6.242575,7.956668,0.541484],[-2.115772,-4.737149,-7.530906,1.681938,-4.548254,-9.243747],[1.176563,-9.789246,-6.692264,-4.478331,7.092523,6.062441],[4.999695,8.439807,-2.776412,9.376319,-8.832476,-0.107383],[8.222169,-6.205475,1.075910,-9.958455,6.175637,-5.370726],[0.930274,8.070894,-6.739379,2.425663,-1.570082,-9.936447],[4.362273,-7.039332,-2.386974,-3.786723,-8.765510,3.149840],[9.742332,-8.777007,-5.530765,-2.313610,-6.934992,-8.120679],[-8.931862,-6.139907,2.685032,-8.274116,-3.136588,-7.080988],[2.635800,-3.356947,-4.651732,2.323536,-5.026269,-2.337871]],[[-0.364434,-7.260738,-8.665504,-2.761017,-5.749710,8.884107],[7.831828,-7.417965,-3.104981,-8.146329,5.129545,9.515584],[8.216556,4.579156,7.451125,-9.172403,-0.005047,-8.639469],[-6.352681,-8.625098,8.478568,-2.603369,2.435416,-5.389440],[7.345796,4.653696,-6.036128,-6.934715,6.566809,8.952513],[8.539984,-0.552381,-8.693101,-8.941532,4.462274,0.282111],[3.756380,-1.077891,-3.446982,-4.832911,4.781195,-9.010816],[6.471423,7.986961,-7.689776,2.119983,7.836143,9.243846],[-7.526828,-3.131618,-9.558735,-3.631409,1.375658,-0.057196],[5.440613,9.204479,-8.516888,-9.984363,8.804232,-6.907356],[-8.846881,7.931653,-5.291115,9.565104,6.209043,-6.707321],[8.498787,3.029626,6.944802,-9.245567,-7.037553,-9.144431],[6.561989,-4.693533,-2.615169,-4.555812,-4.206321,-5.128538]],[[5.259725,8.084602,5.592407,-4.836301,-9.298540,5.942480],[-2.755363,7.379363,-0.351633,6.606352,-5.144151,-7.642491],[4.569442,-5.906454,-3.596743,-1.493262,-1.819985,-1.102913],[9.123066,4.843153,-3.198182,-4.708774,-5.819160,-6.782711],[4.596020,1.885452,2.486362,-6.563056,-9.971760,9.444727],[-0.603496,-9.624199,2.212099,-7.497028,-3.215761,8.427065],[8.370359,8.595709,7.125123,-8.802605,5.906240,-9.389207],[0.163007,4.773214,6.760402,-1.953191,-6.283091,0.066263],[-3.734657,6.434543,6.144343,2.422234,-2.321649,-8.560604],[-9.616169,-1.493706,-7.901373,2.248295,3.922303,-0.821398],[2.716274,-8.934271,6.031301,8.706807,-3.526947,-1.348028],[7.342566,-5.106400,-7.362006,0.263263,1.570067,5.291412],[6.207976,0.335162,3.466520,6.811988,-3.588777,2.760772]]], dtype = "float32")#candidate|1601|(12, 13, 6)|const|float32
bop_1602 = relay.left_shift(call_1584.astype('uint8'), relay.reshape(const_1601.astype('uint8'), relay.shape_of(call_1584))) # shape=(12, 13, 6)
bop_1605 = relay.left_shift(call_1585.astype('uint8'), relay.reshape(const_1601.astype('uint8'), relay.shape_of(call_1585))) # shape=(12, 13, 6)
output = relay.Tuple([call_1591,const_1592,bop_1602,])
output2 = relay.Tuple([call_1593,const_1592,bop_1605,])
func_1616 = relay.Function([], output)
mod['func_1616'] = func_1616
mod = relay.transform.InferType()(mod)
output = func_1616()
func_1617 = relay.Function([], output)
mutated_mod['func_1617'] = func_1617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_952_call = mod.get_global_var('func_952')
func_953_call = mutated_mod.get_global_var('func_953')
call_1644 = func_952_call()
call_1645 = func_952_call()
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_1654 = relay.TupleGetItem(func_601_call(), 0)
call_1655 = relay.TupleGetItem(func_603_call(), 0)
bop_1656 = relay.not_equal(call_1654.astype('bool'), relay.reshape(call_1644.astype('bool'), relay.shape_of(call_1654))) # shape=(12, 13, 6)
bop_1659 = relay.not_equal(call_1655.astype('bool'), relay.reshape(call_1645.astype('bool'), relay.shape_of(call_1655))) # shape=(12, 13, 6)
func_1427_call = mod.get_global_var('func_1427')
func_1430_call = mutated_mod.get_global_var('func_1430')
const_1664 = relay.const(-4.203808, dtype = "float64")#candidate|1664|()|const|float64
const_1665 = relay.const([True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True], dtype = "bool")#candidate|1665|(40,)|const|bool
call_1663 = relay.TupleGetItem(func_1427_call(relay.reshape(const_1664.astype('float64'), []), relay.reshape(const_1665.astype('bool'), [40,]), ), 3)
call_1666 = relay.TupleGetItem(func_1430_call(relay.reshape(const_1664.astype('float64'), []), relay.reshape(const_1665.astype('bool'), [40,]), ), 3)
func_952_call = mod.get_global_var('func_952')
func_953_call = mutated_mod.get_global_var('func_953')
call_1676 = func_952_call()
call_1677 = func_952_call()
output = relay.Tuple([bop_1656,call_1663,const_1664,const_1665,call_1676,])
output2 = relay.Tuple([bop_1659,call_1666,const_1664,const_1665,call_1677,])
func_1696 = relay.Function([], output)
mod['func_1696'] = func_1696
mod = relay.transform.InferType()(mod)
mutated_mod['func_1696'] = func_1696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1696_call = mutated_mod.get_global_var('func_1696')
call_1697 = func_1696_call()
output = call_1697
func_1698 = relay.Function([], output)
mutated_mod['func_1698'] = func_1698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_1751 = relay.TupleGetItem(func_1053_call(), 1)
call_1752 = relay.TupleGetItem(func_1054_call(), 1)
uop_1772 = relay.log10(call_1751.astype('float32')) # shape=(12, 13, 6)
uop_1774 = relay.log10(call_1752.astype('float32')) # shape=(12, 13, 6)
func_537_call = mod.get_global_var('func_537')
func_539_call = mutated_mod.get_global_var('func_539')
call_1791 = relay.TupleGetItem(func_537_call(), 1)
call_1792 = relay.TupleGetItem(func_539_call(), 1)
func_1616_call = mod.get_global_var('func_1616')
func_1617_call = mutated_mod.get_global_var('func_1617')
call_1794 = relay.TupleGetItem(func_1616_call(), 1)
call_1795 = relay.TupleGetItem(func_1617_call(), 1)
output = relay.Tuple([uop_1772,call_1791,call_1794,])
output2 = relay.Tuple([uop_1774,call_1792,call_1795,])
func_1801 = relay.Function([], output)
mod['func_1801'] = func_1801
mod = relay.transform.InferType()(mod)
output = func_1801()
func_1802 = relay.Function([], output)
mutated_mod['func_1802'] = func_1802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1293_call = mutated_mod.get_global_var('func_1293')
call_1840 = relay.TupleGetItem(func_1291_call(), 1)
call_1841 = relay.TupleGetItem(func_1293_call(), 1)
output = relay.Tuple([call_1840,])
output2 = relay.Tuple([call_1841,])
func_1844 = relay.Function([], output)
mod['func_1844'] = func_1844
mod = relay.transform.InferType()(mod)
output = func_1844()
func_1845 = relay.Function([], output)
mutated_mod['func_1845'] = func_1845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_1858 = relay.TupleGetItem(func_1272_call(), 0)
call_1859 = relay.TupleGetItem(func_1273_call(), 0)
output = call_1858
output2 = call_1859
func_1869 = relay.Function([], output)
mod['func_1869'] = func_1869
mod = relay.transform.InferType()(mod)
output = func_1869()
func_1870 = relay.Function([], output)
mutated_mod['func_1870'] = func_1870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_1903 = relay.TupleGetItem(func_1272_call(), 0)
call_1904 = relay.TupleGetItem(func_1273_call(), 0)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
call_1906 = relay.TupleGetItem(func_764_call(relay.reshape(call_1903.astype('int16'), [12, 13, 6])), 0)
call_1907 = relay.TupleGetItem(func_767_call(relay.reshape(call_1903.astype('int16'), [12, 13, 6])), 0)
func_243_call = mod.get_global_var('func_243')
func_245_call = mutated_mod.get_global_var('func_245')
call_1909 = relay.TupleGetItem(func_243_call(relay.reshape(call_1903.astype('float32'), [12, 13, 6])), 0)
call_1910 = relay.TupleGetItem(func_245_call(relay.reshape(call_1903.astype('float32'), [12, 13, 6])), 0)
output = relay.Tuple([call_1903,call_1906,call_1909,])
output2 = relay.Tuple([call_1904,call_1907,call_1910,])
func_1923 = relay.Function([], output)
mod['func_1923'] = func_1923
mod = relay.transform.InferType()(mod)
mutated_mod['func_1923'] = func_1923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1923_call = mutated_mod.get_global_var('func_1923')
call_1924 = func_1923_call()
output = call_1924
func_1925 = relay.Function([], output)
mutated_mod['func_1925'] = func_1925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1869_call = mod.get_global_var('func_1869')
func_1870_call = mutated_mod.get_global_var('func_1870')
call_1965 = func_1869_call()
call_1966 = func_1869_call()
func_1041_call = mod.get_global_var('func_1041')
func_1043_call = mutated_mod.get_global_var('func_1043')
call_1977 = relay.TupleGetItem(func_1041_call(), 2)
call_1978 = relay.TupleGetItem(func_1043_call(), 2)
output = relay.Tuple([call_1965,call_1977,])
output2 = relay.Tuple([call_1966,call_1978,])
func_1983 = relay.Function([], output)
mod['func_1983'] = func_1983
mod = relay.transform.InferType()(mod)
output = func_1983()
func_1984 = relay.Function([], output)
mutated_mod['func_1984'] = func_1984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_1993 = relay.TupleGetItem(func_296_call(), 0)
call_1994 = relay.TupleGetItem(func_298_call(), 0)
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_2006 = relay.TupleGetItem(func_1272_call(), 0)
call_2007 = relay.TupleGetItem(func_1273_call(), 0)
uop_2019 = relay.acos(call_1993.astype('float32')) # shape=(12, 13, 6)
uop_2021 = relay.acos(call_1994.astype('float32')) # shape=(12, 13, 6)
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_2025 = relay.TupleGetItem(func_1272_call(), 0)
call_2026 = relay.TupleGetItem(func_1273_call(), 0)
output = relay.Tuple([call_2006,uop_2019,call_2025,])
output2 = relay.Tuple([call_2007,uop_2021,call_2026,])
func_2034 = relay.Function([], output)
mod['func_2034'] = func_2034
mod = relay.transform.InferType()(mod)
output = func_2034()
func_2035 = relay.Function([], output)
mutated_mod['func_2035'] = func_2035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2050 = relay.var("var_2050", dtype = "float32", shape = (4, 7, 3))#candidate|2050|(4, 7, 3)|var|float32
uop_2051 = relay.acos(var_2050.astype('float32')) # shape=(4, 7, 3)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_2059 = relay.TupleGetItem(func_2034_call(), 2)
call_2060 = relay.TupleGetItem(func_2035_call(), 2)
output = relay.Tuple([uop_2051,call_2059,])
output2 = relay.Tuple([uop_2051,call_2060,])
func_2070 = relay.Function([var_2050,], output)
mod['func_2070'] = func_2070
mod = relay.transform.InferType()(mod)
var_2071 = relay.var("var_2071", dtype = "float32", shape = (4, 7, 3))#candidate|2071|(4, 7, 3)|var|float32
output = func_2070(var_2071)
func_2072 = relay.Function([var_2071], output)
mutated_mod['func_2072'] = func_2072
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2135 = relay.var("var_2135", dtype = "bool", shape = (12, 2, 12))#candidate|2135|(12, 2, 12)|var|bool
var_2136 = relay.var("var_2136", dtype = "bool", shape = (12, 2, 12))#candidate|2136|(12, 2, 12)|var|bool
bop_2137 = relay.logical_and(var_2135.astype('bool'), relay.reshape(var_2136.astype('bool'), relay.shape_of(var_2135))) # shape=(12, 2, 12)
output = relay.Tuple([bop_2137,])
output2 = relay.Tuple([bop_2137,])
func_2141 = relay.Function([var_2135,var_2136,], output)
mod['func_2141'] = func_2141
mod = relay.transform.InferType()(mod)
var_2142 = relay.var("var_2142", dtype = "bool", shape = (12, 2, 12))#candidate|2142|(12, 2, 12)|var|bool
var_2143 = relay.var("var_2143", dtype = "bool", shape = (12, 2, 12))#candidate|2143|(12, 2, 12)|var|bool
output = func_2141(var_2142,var_2143,)
func_2144 = relay.Function([var_2142,var_2143,], output)
mutated_mod['func_2144'] = func_2144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_2168 = relay.TupleGetItem(func_1571_call(), 0)
call_2169 = relay.TupleGetItem(func_1573_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_2173 = relay.TupleGetItem(func_296_call(), 0)
call_2174 = relay.TupleGetItem(func_298_call(), 0)
func_952_call = mod.get_global_var('func_952')
func_953_call = mutated_mod.get_global_var('func_953')
call_2175 = func_952_call()
call_2176 = func_952_call()
output = relay.Tuple([call_2168,call_2173,call_2175,])
output2 = relay.Tuple([call_2169,call_2174,call_2176,])
func_2191 = relay.Function([], output)
mod['func_2191'] = func_2191
mod = relay.transform.InferType()(mod)
output = func_2191()
func_2192 = relay.Function([], output)
mutated_mod['func_2192'] = func_2192
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2198 = relay.var("var_2198", dtype = "bool", shape = (5, 15, 12))#candidate|2198|(5, 15, 12)|var|bool
var_2199 = relay.var("var_2199", dtype = "bool", shape = (5, 15, 12))#candidate|2199|(5, 15, 12)|var|bool
bop_2200 = relay.logical_or(var_2198.astype('bool'), relay.reshape(var_2199.astype('bool'), relay.shape_of(var_2198))) # shape=(5, 15, 12)
uop_2205 = relay.sqrt(bop_2200.astype('float64')) # shape=(5, 15, 12)
uop_2216 = relay.sin(var_2199.astype('float32')) # shape=(5, 15, 12)
func_1801_call = mod.get_global_var('func_1801')
func_1802_call = mutated_mod.get_global_var('func_1802')
call_2219 = relay.TupleGetItem(func_1801_call(), 2)
call_2220 = relay.TupleGetItem(func_1802_call(), 2)
func_1434_call = mod.get_global_var('func_1434')
func_1436_call = mutated_mod.get_global_var('func_1436')
call_2221 = func_1434_call()
call_2222 = func_1434_call()
var_2224 = relay.var("var_2224", dtype = "uint64", shape = (12, 13, 6))#candidate|2224|(12, 13, 6)|var|uint64
bop_2225 = relay.greater_equal(call_2221.astype('bool'), relay.reshape(var_2224.astype('bool'), relay.shape_of(call_2221))) # shape=(12, 13, 6)
bop_2228 = relay.greater_equal(call_2222.astype('bool'), relay.reshape(var_2224.astype('bool'), relay.shape_of(call_2222))) # shape=(12, 13, 6)
bop_2238 = relay.divide(uop_2205.astype('float32'), relay.reshape(var_2198.astype('float32'), relay.shape_of(uop_2205))) # shape=(5, 15, 12)
uop_2242 = relay.acosh(uop_2205.astype('float64')) # shape=(5, 15, 12)
bop_2249 = relay.floor_divide(uop_2242.astype('float32'), relay.reshape(uop_2216.astype('float32'), relay.shape_of(uop_2242))) # shape=(5, 15, 12)
bop_2252 = relay.multiply(bop_2249.astype('int16'), relay.reshape(uop_2205.astype('int16'), relay.shape_of(bop_2249))) # shape=(5, 15, 12)
output = relay.Tuple([call_2219,bop_2225,bop_2238,bop_2252,])
output2 = relay.Tuple([call_2220,bop_2228,bop_2238,bop_2252,])
func_2259 = relay.Function([var_2198,var_2199,var_2224,], output)
mod['func_2259'] = func_2259
mod = relay.transform.InferType()(mod)
mutated_mod['func_2259'] = func_2259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mutated_mod.get_global_var('func_2259')
var_2261 = relay.var("var_2261", dtype = "bool", shape = (5, 15, 12))#candidate|2261|(5, 15, 12)|var|bool
var_2262 = relay.var("var_2262", dtype = "bool", shape = (5, 15, 12))#candidate|2262|(5, 15, 12)|var|bool
var_2263 = relay.var("var_2263", dtype = "uint64", shape = (12, 13, 6))#candidate|2263|(12, 13, 6)|var|uint64
call_2260 = func_2259_call(var_2261,var_2262,var_2263,)
output = call_2260
func_2264 = relay.Function([var_2261,var_2262,var_2263,], output)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1869_call = mod.get_global_var('func_1869')
func_1870_call = mutated_mod.get_global_var('func_1870')
call_2274 = func_1869_call()
call_2275 = func_1869_call()
output = relay.Tuple([call_2274,])
output2 = relay.Tuple([call_2275,])
func_2303 = relay.Function([], output)
mod['func_2303'] = func_2303
mod = relay.transform.InferType()(mod)
output = func_2303()
func_2304 = relay.Function([], output)
mutated_mod['func_2304'] = func_2304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_539_call = mutated_mod.get_global_var('func_539')
call_2314 = relay.TupleGetItem(func_537_call(), 1)
call_2315 = relay.TupleGetItem(func_539_call(), 1)
output = relay.Tuple([call_2314,])
output2 = relay.Tuple([call_2315,])
func_2358 = relay.Function([], output)
mod['func_2358'] = func_2358
mod = relay.transform.InferType()(mod)
output = func_2358()
func_2359 = relay.Function([], output)
mutated_mod['func_2359'] = func_2359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_2383 = func_859_call()
call_2384 = func_859_call()
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_2389 = relay.TupleGetItem(func_907_call(), 0)
call_2390 = relay.TupleGetItem(func_908_call(), 0)
func_345_call = mod.get_global_var('func_345')
func_346_call = mutated_mod.get_global_var('func_346')
call_2391 = relay.TupleGetItem(func_345_call(), 1)
call_2392 = relay.TupleGetItem(func_346_call(), 1)
output = relay.Tuple([call_2383,call_2389,call_2391,])
output2 = relay.Tuple([call_2384,call_2390,call_2392,])
func_2393 = relay.Function([], output)
mod['func_2393'] = func_2393
mod = relay.transform.InferType()(mod)
mutated_mod['func_2393'] = func_2393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2393_call = mutated_mod.get_global_var('func_2393')
call_2394 = func_2393_call()
output = call_2394
func_2395 = relay.Function([], output)
mutated_mod['func_2395'] = func_2395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_2396 = relay.TupleGetItem(func_1571_call(), 0)
call_2397 = relay.TupleGetItem(func_1573_call(), 0)
func_1983_call = mod.get_global_var('func_1983')
func_1984_call = mutated_mod.get_global_var('func_1984')
call_2398 = relay.TupleGetItem(func_1983_call(), 1)
call_2399 = relay.TupleGetItem(func_1984_call(), 1)
func_839_call = mod.get_global_var('func_839')
func_840_call = mutated_mod.get_global_var('func_840')
call_2400 = relay.TupleGetItem(func_839_call(), 0)
call_2401 = relay.TupleGetItem(func_840_call(), 0)
output = relay.Tuple([call_2396,call_2398,call_2400,])
output2 = relay.Tuple([call_2397,call_2399,call_2401,])
func_2403 = relay.Function([], output)
mod['func_2403'] = func_2403
mod = relay.transform.InferType()(mod)
mutated_mod['func_2403'] = func_2403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2404 = func_2403_call()
output = call_2404
func_2405 = relay.Function([], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1160_call = mod.get_global_var('func_1160')
func_1161_call = mutated_mod.get_global_var('func_1161')
call_2411 = relay.TupleGetItem(func_1160_call(), 0)
call_2412 = relay.TupleGetItem(func_1161_call(), 0)
output = relay.Tuple([call_2411,])
output2 = relay.Tuple([call_2412,])
func_2421 = relay.Function([], output)
mod['func_2421'] = func_2421
mod = relay.transform.InferType()(mod)
output = func_2421()
func_2422 = relay.Function([], output)
mutated_mod['func_2422'] = func_2422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_2442 = relay.TupleGetItem(func_907_call(), 0)
call_2443 = relay.TupleGetItem(func_908_call(), 0)
output = call_2442
output2 = call_2443
func_2448 = relay.Function([], output)
mod['func_2448'] = func_2448
mod = relay.transform.InferType()(mod)
mutated_mod['func_2448'] = func_2448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2448_call = mutated_mod.get_global_var('func_2448')
call_2449 = func_2448_call()
output = call_2449
func_2450 = relay.Function([], output)
mutated_mod['func_2450'] = func_2450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2448_call = mod.get_global_var('func_2448')
func_2450_call = mutated_mod.get_global_var('func_2450')
call_2461 = func_2448_call()
call_2462 = func_2448_call()
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
call_2477 = relay.TupleGetItem(func_764_call(relay.reshape(call_2461.astype('int16'), [12, 13, 6])), 4)
call_2478 = relay.TupleGetItem(func_767_call(relay.reshape(call_2461.astype('int16'), [12, 13, 6])), 4)
uop_2482 = relay.asinh(call_2461.astype('float64')) # shape=(12, 13, 6)
uop_2484 = relay.asinh(call_2462.astype('float64')) # shape=(12, 13, 6)
func_1923_call = mod.get_global_var('func_1923')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_2490 = relay.TupleGetItem(func_1923_call(), 0)
call_2491 = relay.TupleGetItem(func_1925_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_2510 = relay.TupleGetItem(func_296_call(), 0)
call_2511 = relay.TupleGetItem(func_298_call(), 0)
func_2070_call = mod.get_global_var('func_2070')
func_2072_call = mutated_mod.get_global_var('func_2072')
const_2528 = relay.const([-7.152158,-1.005970,3.332683,5.411738,2.979268,9.190327,9.979631,9.751622,-8.158567,-6.742293,6.830974,-6.682490,9.173692,6.609271,-0.175661,-8.336873,5.828935,1.249513,-5.386681,7.666381,5.694877,1.865636,-6.736649,4.740943,2.371640,-7.108644,9.095658,-1.693571,-4.033709,3.492530,-3.459391,5.717939,-3.081929,-4.645241,1.066850,5.945561,-6.213173,5.591421,0.449536,6.865238,8.942496,0.464870,5.185954,1.369333,9.200447,-3.744282,-1.875548,5.910389,6.415627,-8.760020,3.976256,3.326739,-0.666341,-9.121624,-7.484316,-4.764298,5.739783,-2.259516,9.488556,-0.811335,-4.179360,-4.257985,-0.577180,6.607762,7.314017,6.274155,4.373687,0.584473,3.260616,4.370205,3.903968,7.602864,7.613037,8.127683,-2.867417,1.436331,2.135521,2.252907,6.473500,9.512140,-9.580897,5.412378,1.960516,7.263641], dtype = "float32")#candidate|2528|(84,)|const|float32
call_2527 = relay.TupleGetItem(func_2070_call(relay.reshape(const_2528.astype('float32'), [4, 7, 3])), 0)
call_2529 = relay.TupleGetItem(func_2072_call(relay.reshape(const_2528.astype('float32'), [4, 7, 3])), 0)
const_2531 = relay.const([[[-0.315720,0.210392,0.105979,5.175562,-6.346201,-5.911201],[9.497170,-3.078919,-3.408541,-5.397509,7.697914,-1.379863],[6.641539,8.563916,-3.292945,-8.277594,-3.213438,5.233891],[7.048615,-9.839822,-8.563835,4.325288,-3.499511,0.670160],[6.295585,-6.302056,-9.672516,9.181877,-6.495222,-3.414086],[-3.182072,0.174804,8.556850,-7.438226,0.740989,-6.218740],[8.208654,-2.553762,9.273354,5.888530,2.104839,5.212279],[-6.345691,2.680853,-8.850681,-6.276666,4.563892,3.544153],[-5.911463,4.267796,-2.701732,5.155531,5.223718,5.314660],[1.802373,2.770930,4.408522,7.435821,-6.637774,-8.478885],[-8.722742,1.834170,-8.573839,-3.050326,-6.606702,2.625876],[8.971189,8.796027,-4.700593,-3.628099,5.414874,-6.577836],[-0.952132,-3.210521,2.867391,2.776089,3.362329,6.806508]],[[0.114677,-4.070261,9.023748,-6.995918,6.311600,2.789396],[6.158267,6.142316,0.019447,7.201626,7.599115,-2.670153],[-1.472364,5.261001,-1.631657,4.858956,-6.249899,-3.228019],[3.038721,5.662226,-7.932201,-1.037755,-0.946841,-6.637723],[-6.890413,3.427605,3.540124,-6.111631,-9.879406,-8.690056],[-3.234159,-0.541330,5.190867,-9.059416,-2.266855,2.130857],[-5.977348,-7.243116,-6.982170,-1.547122,-1.315949,-9.487991],[-0.557298,9.332616,-7.991121,7.249851,1.825558,-9.617217],[-2.379556,-1.232002,-5.848266,2.758155,3.246738,5.500436],[-5.481366,-1.269595,7.875873,4.492270,9.871376,-4.734014],[-8.808718,-5.540093,-5.223056,-6.693270,0.452548,9.028218],[4.737445,-6.751523,-0.354232,-6.263181,-6.402679,2.170639],[7.098132,4.744447,7.712527,0.731310,8.962510,8.616953]],[[-0.016799,5.695351,-1.932455,3.717844,3.798003,8.489157],[2.932549,7.706333,-6.403637,5.816089,5.342321,1.188772],[2.895712,-8.068641,-2.608424,-8.829703,6.263647,2.298423],[-8.095140,5.035754,-4.048719,1.849323,-2.325752,1.524543],[1.387262,8.290687,4.873772,1.864028,0.913144,-5.634459],[6.000974,-7.427636,-0.959909,8.914785,-8.342376,-5.482241],[8.153173,-2.624427,-8.819250,-7.513143,-9.789934,-8.999241],[-9.042008,-7.619377,0.248897,-8.326122,4.588897,-3.591608],[-5.834880,-2.675662,-0.585264,9.148360,-3.247438,-0.824018],[-5.999550,-8.750323,-8.388938,-3.031916,-6.818212,-7.678295],[1.751119,0.447582,4.823766,-9.299586,2.072402,-9.499040],[-1.012759,4.901521,1.958242,8.473746,-8.911287,-6.947773],[6.435296,-7.883134,-4.870500,5.494256,7.642634,-9.223562]],[[-4.236586,-2.850859,-5.450002,-6.628210,-6.731477,1.905312],[4.643981,0.668469,6.419685,-2.317878,9.471344,-7.908610],[2.983936,6.168188,-6.262022,2.349418,1.309806,-7.301140],[-1.531269,-9.858423,-2.632774,-6.219311,-2.653247,-0.624836],[5.426334,-3.211391,5.356001,-5.980059,5.410914,0.499884],[-7.758997,-3.982508,-3.297395,7.570910,9.410724,8.199934],[8.093000,0.655669,-9.259544,9.492911,-8.211869,-2.126959],[9.045295,-4.097002,-1.059713,-0.591174,-5.074788,-1.688558],[-5.557489,8.806600,7.082523,9.115203,-9.552238,2.516391],[-3.602590,1.780512,-5.188438,-6.092800,-5.466661,-5.161303],[-8.907270,1.611172,-4.462013,1.932861,8.412686,-0.567542],[-9.098447,-5.202737,0.579626,7.506926,-7.574994,-0.573352],[-5.725241,-6.539096,-1.829544,5.760372,-5.726592,0.727072]],[[3.718205,7.689181,-6.083865,6.898668,8.567367,9.259456],[2.032728,1.962929,5.762841,6.774959,-4.617526,7.519780],[-6.887530,-1.914731,4.720360,4.119961,-9.395592,-0.886003],[9.757366,4.899887,3.758860,8.237357,0.548363,-4.956940],[-6.258316,-5.561454,-3.574040,5.396292,2.436648,3.573097],[-7.300684,3.067265,2.275757,9.916320,1.003203,6.384773],[0.967280,-3.799401,8.038041,-8.461713,-0.082827,6.140874],[-5.411048,6.562814,-4.541287,-1.107525,-4.047259,8.253137],[3.242131,-9.679774,-7.310031,0.390143,-6.824754,-2.206158],[5.231753,5.670472,-2.733034,-7.572130,-2.859991,-2.216417],[-6.748860,1.448058,-9.477165,-8.887482,6.420138,-2.534026],[-5.286714,6.845526,7.444007,5.167876,-8.687609,-6.081915],[1.184246,4.183626,5.603075,-4.937482,9.341310,-3.705227]],[[-0.096573,1.451802,5.205134,5.638750,-5.468459,-2.786024],[6.436258,-6.615212,-0.199135,-8.650215,7.949590,9.726354],[8.072727,-6.792395,3.456975,-9.171424,6.775228,6.957845],[3.373796,-9.141086,-4.770872,-9.352955,-6.305014,3.340181],[5.433172,-5.485003,-6.268858,4.044374,6.999124,-8.423292],[-7.373756,8.001103,-6.664055,-0.349428,9.961056,5.420065],[7.549435,1.371793,-1.103405,3.077318,-7.227099,-7.552982],[1.898755,-2.394971,5.861608,-5.723621,5.535725,4.400928],[-4.874865,-9.335554,6.058259,6.598310,9.869979,-3.220865],[-6.309710,0.745412,-5.811199,1.033109,-0.179904,-6.157959],[-8.850306,3.066909,-8.716205,0.105436,9.870905,5.670386],[-7.155575,8.380250,1.912328,7.777269,8.655898,2.161953],[4.333163,-7.580727,-4.249835,8.323486,5.897556,2.133125]],[[-4.205660,-1.470751,-1.980278,-7.625425,4.190675,-3.698280],[0.748729,-8.521738,-2.112592,-6.803685,-9.533592,2.634551],[-6.364455,0.866499,-2.160748,7.064861,6.236320,-9.532553],[3.430560,-9.840377,-9.742532,-2.354954,4.685998,6.416936],[-4.272606,6.167422,-8.811434,8.334342,8.019783,-1.587977],[2.282833,-2.913830,6.169909,-7.255787,5.704333,2.310409],[1.361707,-9.455478,-1.973368,5.235532,2.435447,3.768829],[1.392982,-4.547394,9.873323,-4.053671,8.606051,-7.855767],[4.967044,9.925613,3.711834,3.558941,-8.382904,5.769676],[6.039143,0.653294,2.836984,-2.239532,-2.375761,-9.430230],[9.875340,-8.334728,2.899760,2.596477,-5.953665,-7.313455],[-6.529865,-0.727568,8.251190,9.897954,-6.713526,6.856742],[-3.885291,4.866713,2.460817,-9.357767,-4.050430,3.731171]],[[2.004037,0.342808,3.874432,-4.859636,1.450315,2.003494],[-4.364621,9.646913,9.597309,8.000733,-5.239001,-5.195011],[-7.211290,-7.998130,-4.741137,-1.394155,-3.460745,4.030951],[9.694946,6.271574,-7.399204,4.039658,-5.024673,-3.728759],[-0.250547,1.533555,-8.864046,-1.993842,-7.985511,2.660425],[-8.207512,9.425710,5.545398,-6.734347,-0.582676,4.021555],[-6.574307,0.615680,8.103478,3.510492,9.470062,-0.163879],[-2.372803,-7.189670,1.345753,5.906516,-5.458159,7.092786],[5.215222,-4.133925,3.646849,0.846690,4.598673,-8.821354],[-9.970697,-6.642202,-6.541447,7.892642,0.464851,-2.694694],[5.571883,-9.648983,-6.372667,-9.688486,4.476263,3.046035],[-7.206620,6.375511,6.114177,7.242062,7.015153,-7.685548],[-7.399246,-3.709377,5.680201,9.833151,6.358793,-1.131379]],[[2.323656,4.588947,-7.946836,6.568004,9.890276,-7.818228],[6.303058,-0.592372,5.101874,-1.331780,-6.005229,2.443255],[9.317974,8.174347,-2.547939,-9.932272,-1.254452,-6.455750],[-8.269724,1.537629,-1.700870,8.180419,4.628709,-5.841738],[-4.669209,0.776034,-0.206958,-3.036161,9.280136,-8.655241],[-7.308282,7.240207,-1.021701,2.480743,8.090402,6.350948],[-0.854294,3.202150,-6.825467,-9.769352,1.965789,-8.913098],[-1.656895,2.040178,-1.339211,7.729880,4.415438,4.380791],[-7.755645,-7.544352,2.092832,-8.237019,-2.379493,-8.036454],[2.941875,6.000827,-7.309447,-0.033123,0.618744,-4.731929],[4.892686,-7.802481,-6.289176,9.012514,-6.243935,-3.643385],[8.713096,1.778768,3.447407,-2.873163,-5.686613,5.689907],[8.088105,5.370399,2.137702,-4.461857,6.942946,7.326404]],[[-3.590427,-9.835624,0.416033,2.136098,5.708336,-9.054824],[-7.012578,-9.672210,0.057456,3.111244,4.748486,1.133421],[-2.908015,-5.757753,-8.457173,3.187633,-2.479058,1.869516],[-5.189293,-3.253232,2.062262,-8.441850,2.040983,-4.131591],[-6.976117,-2.905545,-3.087652,5.541732,9.516273,-8.409752],[0.354636,5.067580,7.253246,0.419667,7.700731,-0.964524],[0.156905,-6.558714,8.745560,7.088854,-0.559028,7.840168],[1.551479,4.117421,-5.594768,-7.660157,2.550201,3.204044],[-3.858360,-3.940809,-4.019377,-7.040170,-6.383885,6.362585],[3.770379,2.368647,-1.932859,-6.968758,2.761287,-1.399767],[8.489066,-3.532684,-8.222877,1.514790,-6.025757,-7.392468],[-2.237988,-6.965107,8.119458,-0.389714,-5.079455,-2.781337],[5.455413,-8.408300,-2.539701,-0.859963,5.422715,-6.733903]],[[3.003339,-9.947429,-7.153986,-4.876895,6.202668,8.673209],[-6.761120,3.895820,7.009402,4.446123,-9.437493,-1.678492],[0.818244,-2.409232,9.385241,-8.398515,5.073676,-5.034155],[-0.474151,-2.471208,-4.638731,-9.396910,-1.311599,4.296679],[-2.044945,-0.318009,7.886419,1.156225,2.770134,7.968122],[3.040408,0.170206,5.945362,-5.218965,0.349064,0.355501],[-8.281302,-7.982338,-2.930697,-7.803636,2.528365,6.766975],[6.193993,2.457398,2.001139,9.325527,-0.063295,3.533163],[6.350101,5.720874,-5.950239,-0.606131,1.071446,6.337489],[-3.783860,-4.201194,-5.807105,-2.655604,-6.722623,9.008081],[1.813768,-2.093591,0.602181,1.212107,1.769175,4.073349],[5.303478,-2.556672,5.063270,-0.475595,-7.651772,4.437842],[7.555194,-0.145686,9.111902,1.631562,7.001762,-9.963741]],[[4.116846,4.526915,0.636929,-4.980647,-3.243968,0.277721],[5.729413,3.902617,-0.600546,-4.093770,5.787436,3.245633],[-6.599933,3.054137,5.413852,5.357878,6.825687,5.914593],[9.227249,6.340984,5.380390,6.285934,5.288427,-5.044223],[9.623586,7.985517,2.694323,8.143021,1.011257,3.148549],[6.147212,5.940746,9.196024,0.985601,-8.178443,-4.756739],[2.720962,-5.774541,8.066015,-3.684047,-7.766374,8.832291],[-7.153239,9.641973,7.367434,-0.662503,6.549440,0.081056],[5.761499,-2.049590,8.717074,8.594518,-9.808462,8.541937],[-7.643537,0.528253,1.117902,-7.544119,7.516448,0.635371],[9.415230,2.950384,5.100813,3.073720,9.033125,5.905191],[8.821611,8.381191,-9.431978,6.512728,-7.190864,3.005234],[3.576211,-8.341903,-5.648067,8.200818,9.693168,-1.932564]]], dtype = "float64")#candidate|2531|(12, 13, 6)|const|float64
bop_2532 = relay.right_shift(uop_2482.astype('uint8'), relay.reshape(const_2531.astype('uint8'), relay.shape_of(uop_2482))) # shape=(12, 13, 6)
bop_2535 = relay.right_shift(uop_2484.astype('uint8'), relay.reshape(const_2531.astype('uint8'), relay.shape_of(uop_2484))) # shape=(12, 13, 6)
func_2141_call = mod.get_global_var('func_2141')
func_2144_call = mutated_mod.get_global_var('func_2144')
const_2538 = relay.const([True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False], dtype = "bool")#candidate|2538|(288,)|const|bool
call_2537 = relay.TupleGetItem(func_2141_call(relay.reshape(const_2538.astype('bool'), [12, 2, 12]), relay.reshape(const_2538.astype('bool'), [12, 2, 12]), ), 0)
call_2539 = relay.TupleGetItem(func_2144_call(relay.reshape(const_2538.astype('bool'), [12, 2, 12]), relay.reshape(const_2538.astype('bool'), [12, 2, 12]), ), 0)
func_1801_call = mod.get_global_var('func_1801')
func_1802_call = mutated_mod.get_global_var('func_1802')
call_2540 = relay.TupleGetItem(func_1801_call(), 0)
call_2541 = relay.TupleGetItem(func_1802_call(), 0)
output = relay.Tuple([call_2477,call_2490,call_2510,call_2527,const_2528,bop_2532,call_2537,const_2538,call_2540,])
output2 = relay.Tuple([call_2478,call_2491,call_2511,call_2529,const_2528,bop_2535,call_2539,const_2538,call_2541,])
func_2542 = relay.Function([], output)
mod['func_2542'] = func_2542
mod = relay.transform.InferType()(mod)
output = func_2542()
func_2543 = relay.Function([], output)
mutated_mod['func_2543'] = func_2543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_2577 = relay.TupleGetItem(func_296_call(), 0)
call_2578 = relay.TupleGetItem(func_298_call(), 0)
output = relay.Tuple([call_2577,])
output2 = relay.Tuple([call_2578,])
func_2579 = relay.Function([], output)
mod['func_2579'] = func_2579
mod = relay.transform.InferType()(mod)
output = func_2579()
func_2580 = relay.Function([], output)
mutated_mod['func_2580'] = func_2580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1293_call = mutated_mod.get_global_var('func_1293')
call_2673 = relay.TupleGetItem(func_1291_call(), 0)
call_2674 = relay.TupleGetItem(func_1293_call(), 0)
uop_2704 = relay.log(call_2673.astype('float64')) # shape=(12, 13, 6)
uop_2706 = relay.log(call_2674.astype('float64')) # shape=(12, 13, 6)
func_1616_call = mod.get_global_var('func_1616')
func_1617_call = mutated_mod.get_global_var('func_1617')
call_2717 = relay.TupleGetItem(func_1616_call(), 0)
call_2718 = relay.TupleGetItem(func_1617_call(), 0)
output = relay.Tuple([uop_2704,call_2717,])
output2 = relay.Tuple([uop_2706,call_2718,])
func_2730 = relay.Function([], output)
mod['func_2730'] = func_2730
mod = relay.transform.InferType()(mod)
output = func_2730()
func_2731 = relay.Function([], output)
mutated_mod['func_2731'] = func_2731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2769 = relay.var("var_2769", dtype = "float32", shape = (14, 11, 3))#candidate|2769|(14, 11, 3)|var|float32
uop_2770 = relay.acosh(var_2769.astype('float32')) # shape=(14, 11, 3)
output = uop_2770
output2 = uop_2770
func_2775 = relay.Function([var_2769,], output)
mod['func_2775'] = func_2775
mod = relay.transform.InferType()(mod)
mutated_mod['func_2775'] = func_2775
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2776 = relay.var("var_2776", dtype = "float32", shape = (14, 11, 3))#candidate|2776|(14, 11, 3)|var|float32
func_2775_call = mutated_mod.get_global_var('func_2775')
call_2777 = func_2775_call(var_2776)
output = call_2777
func_2778 = relay.Function([var_2776], output)
mutated_mod['func_2778'] = func_2778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1456_call = mod.get_global_var('func_1456')
func_1457_call = mutated_mod.get_global_var('func_1457')
call_2790 = func_1456_call()
call_2791 = func_1456_call()
output = call_2790
output2 = call_2791
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
func_1291_call = mod.get_global_var('func_1291')
func_1293_call = mutated_mod.get_global_var('func_1293')
call_2817 = relay.TupleGetItem(func_1291_call(), 0)
call_2818 = relay.TupleGetItem(func_1293_call(), 0)
output = relay.Tuple([call_2817,])
output2 = relay.Tuple([call_2818,])
func_2819 = relay.Function([], output)
mod['func_2819'] = func_2819
mod = relay.transform.InferType()(mod)
mutated_mod['func_2819'] = func_2819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2819_call = mutated_mod.get_global_var('func_2819')
call_2820 = func_2819_call()
output = call_2820
func_2821 = relay.Function([], output)
mutated_mod['func_2821'] = func_2821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_2964 = relay.TupleGetItem(func_2421_call(), 0)
call_2965 = relay.TupleGetItem(func_2422_call(), 0)
output = relay.Tuple([call_2964,])
output2 = relay.Tuple([call_2965,])
func_2966 = relay.Function([], output)
mod['func_2966'] = func_2966
mod = relay.transform.InferType()(mod)
mutated_mod['func_2966'] = func_2966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2966_call = mutated_mod.get_global_var('func_2966')
call_2967 = func_2966_call()
output = call_2967
func_2968 = relay.Function([], output)
mutated_mod['func_2968'] = func_2968
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2986 = relay.var("var_2986", dtype = "uint16", shape = (13, 16, 7))#candidate|2986|(13, 16, 7)|var|uint16
var_2987 = relay.var("var_2987", dtype = "uint16", shape = (13, 16, 7))#candidate|2987|(13, 16, 7)|var|uint16
bop_2988 = relay.multiply(var_2986.astype('uint16'), relay.reshape(var_2987.astype('uint16'), relay.shape_of(var_2986))) # shape=(13, 16, 7)
func_2730_call = mod.get_global_var('func_2730')
func_2731_call = mutated_mod.get_global_var('func_2731')
call_2997 = relay.TupleGetItem(func_2730_call(), 1)
call_2998 = relay.TupleGetItem(func_2731_call(), 1)
uop_3000 = relay.sigmoid(var_2986.astype('float64')) # shape=(13, 16, 7)
bop_3002 = relay.mod(var_2987.astype('float32'), relay.reshape(uop_3000.astype('float32'), relay.shape_of(var_2987))) # shape=(13, 16, 7)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_3006 = relay.TupleGetItem(func_2034_call(), 1)
call_3007 = relay.TupleGetItem(func_2035_call(), 1)
output = relay.Tuple([bop_2988,call_2997,bop_3002,call_3006,])
output2 = relay.Tuple([bop_2988,call_2998,bop_3002,call_3007,])
func_3008 = relay.Function([var_2986,var_2987,], output)
mod['func_3008'] = func_3008
mod = relay.transform.InferType()(mod)
mutated_mod['func_3008'] = func_3008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3008_call = mutated_mod.get_global_var('func_3008')
var_3010 = relay.var("var_3010", dtype = "uint16", shape = (13, 16, 7))#candidate|3010|(13, 16, 7)|var|uint16
var_3011 = relay.var("var_3011", dtype = "uint16", shape = (13, 16, 7))#candidate|3011|(13, 16, 7)|var|uint16
call_3009 = func_3008_call(var_3010,var_3011,)
output = call_3009
func_3012 = relay.Function([var_3010,var_3011,], output)
mutated_mod['func_3012'] = func_3012
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3033 = relay.var("var_3033", dtype = "float64", shape = (6, 15, 2))#candidate|3033|(6, 15, 2)|var|float64
var_3034 = relay.var("var_3034", dtype = "float64", shape = (6, 15, 2))#candidate|3034|(6, 15, 2)|var|float64
bop_3035 = relay.floor_divide(var_3033.astype('float64'), relay.reshape(var_3034.astype('float64'), relay.shape_of(var_3033))) # shape=(6, 15, 2)
output = bop_3035
output2 = bop_3035
func_3041 = relay.Function([var_3033,var_3034,], output)
mod['func_3041'] = func_3041
mod = relay.transform.InferType()(mod)
var_3042 = relay.var("var_3042", dtype = "float64", shape = (6, 15, 2))#candidate|3042|(6, 15, 2)|var|float64
var_3043 = relay.var("var_3043", dtype = "float64", shape = (6, 15, 2))#candidate|3043|(6, 15, 2)|var|float64
output = func_3041(var_3042,var_3043,)
func_3044 = relay.Function([var_3042,var_3043,], output)
mutated_mod['func_3044'] = func_3044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1983_call = mod.get_global_var('func_1983')
func_1984_call = mutated_mod.get_global_var('func_1984')
call_3159 = relay.TupleGetItem(func_1983_call(), 1)
call_3160 = relay.TupleGetItem(func_1984_call(), 1)
output = call_3159
output2 = call_3160
func_3161 = relay.Function([], output)
mod['func_3161'] = func_3161
mod = relay.transform.InferType()(mod)
mutated_mod['func_3161'] = func_3161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mutated_mod.get_global_var('func_3161')
call_3162 = func_3161_call()
output = call_3162
func_3163 = relay.Function([], output)
mutated_mod['func_3163'] = func_3163
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3170 = relay.const(2, dtype = "int16")#candidate|3170|()|const|int16
var_3171 = relay.var("var_3171", dtype = "int16", shape = (12, 5, 1))#candidate|3171|(12, 5, 1)|var|int16
bop_3172 = relay.subtract(const_3170.astype('int16'), var_3171.astype('int16')) # shape=(12, 5, 1)
var_3175 = relay.var("var_3175", dtype = "int16", shape = (12, 5, 8))#candidate|3175|(12, 5, 8)|var|int16
bop_3176 = relay.less_equal(var_3171.astype('bool'), var_3175.astype('bool')) # shape=(12, 5, 8)
func_1696_call = mod.get_global_var('func_1696')
func_1698_call = mutated_mod.get_global_var('func_1698')
call_3191 = relay.TupleGetItem(func_1696_call(), 0)
call_3192 = relay.TupleGetItem(func_1698_call(), 0)
func_2966_call = mod.get_global_var('func_2966')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3196 = relay.TupleGetItem(func_2966_call(), 0)
call_3197 = relay.TupleGetItem(func_2968_call(), 0)
var_3203 = relay.var("var_3203", dtype = "int16", shape = (12, 5, 11))#candidate|3203|(12, 5, 11)|var|int16
bop_3204 = relay.subtract(var_3171.astype('uint16'), var_3203.astype('uint16')) # shape=(12, 5, 11)
output = relay.Tuple([bop_3172,bop_3176,call_3191,call_3196,bop_3204,])
output2 = relay.Tuple([bop_3172,bop_3176,call_3192,call_3197,bop_3204,])
func_3208 = relay.Function([var_3171,var_3175,var_3203,], output)
mod['func_3208'] = func_3208
mod = relay.transform.InferType()(mod)
mutated_mod['func_3208'] = func_3208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3208_call = mutated_mod.get_global_var('func_3208')
var_3210 = relay.var("var_3210", dtype = "int16", shape = (12, 5, 1))#candidate|3210|(12, 5, 1)|var|int16
var_3211 = relay.var("var_3211", dtype = "int16", shape = (12, 5, 8))#candidate|3211|(12, 5, 8)|var|int16
var_3212 = relay.var("var_3212", dtype = "int16", shape = (12, 5, 11))#candidate|3212|(12, 5, 11)|var|int16
call_3209 = func_3208_call(var_3210,var_3211,var_3212,)
output = call_3209
func_3213 = relay.Function([var_3210,var_3211,var_3212,], output)
mutated_mod['func_3213'] = func_3213
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3318 = relay.var("var_3318", dtype = "float32", shape = (2, 5, 1))#candidate|3318|(2, 5, 1)|var|float32
uop_3319 = relay.sinh(var_3318.astype('float32')) # shape=(2, 5, 1)
func_2393_call = mod.get_global_var('func_2393')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_3324 = relay.TupleGetItem(func_2393_call(), 1)
call_3325 = relay.TupleGetItem(func_2395_call(), 1)
output = relay.Tuple([uop_3319,call_3324,])
output2 = relay.Tuple([uop_3319,call_3325,])
func_3328 = relay.Function([var_3318,], output)
mod['func_3328'] = func_3328
mod = relay.transform.InferType()(mod)
mutated_mod['func_3328'] = func_3328
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3329 = relay.var("var_3329", dtype = "float32", shape = (2, 5, 1))#candidate|3329|(2, 5, 1)|var|float32
func_3328_call = mutated_mod.get_global_var('func_3328')
call_3330 = func_3328_call(var_3329)
output = call_3330
func_3331 = relay.Function([var_3329], output)
mutated_mod['func_3331'] = func_3331
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3333 = relay.const([[[-1.599832,-0.914787,8.656274,-3.001378,0.699769,-4.056856,-9.937641],[7.467708,-6.497881,6.829339,8.908586,2.365451,1.727170,-8.249782],[8.011332,9.258818,-6.674501,-2.163811,4.960862,-8.173149,-4.913872]],[[8.960765,7.727304,8.464032,5.948469,0.376169,-4.670719,-3.512024],[1.637754,-3.430025,2.014602,6.835841,3.946436,4.979385,-5.536021],[3.144735,-9.227906,6.512539,-5.983675,5.685261,-0.166564,-5.774615]],[[-5.632034,-1.240549,-0.711617,-7.170816,-7.818374,5.017027,1.074342],[9.693712,-7.796869,-5.863809,1.321375,-9.558327,-1.350382,1.279565],[3.748128,6.348264,-7.448649,0.908120,-0.244580,-7.680207,5.230405]],[[-6.428711,-8.189936,-5.788174,0.766596,-9.004866,3.425321,-1.456784],[-9.396719,-0.714781,2.870518,5.266109,3.151471,-6.716749,-9.465439],[2.489591,2.263502,-6.652382,4.047600,-6.204044,-3.701707,2.219255]]], dtype = "float64")#candidate|3333|(4, 3, 7)|const|float64
uop_3334 = relay.atan(const_3333.astype('float64')) # shape=(4, 3, 7)
output = uop_3334
output2 = uop_3334
func_3336 = relay.Function([], output)
mod['func_3336'] = func_3336
mod = relay.transform.InferType()(mod)
output = func_3336()
func_3337 = relay.Function([], output)
mutated_mod['func_3337'] = func_3337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_3375 = relay.TupleGetItem(func_1053_call(), 0)
call_3376 = relay.TupleGetItem(func_1054_call(), 0)
output = call_3375
output2 = call_3376
func_3410 = relay.Function([], output)
mod['func_3410'] = func_3410
mod = relay.transform.InferType()(mod)
mutated_mod['func_3410'] = func_3410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3410_call = mutated_mod.get_global_var('func_3410')
call_3411 = func_3410_call()
output = call_3411
func_3412 = relay.Function([], output)
mutated_mod['func_3412'] = func_3412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_3523 = relay.TupleGetItem(func_1571_call(), 0)
call_3524 = relay.TupleGetItem(func_1573_call(), 0)
output = call_3523
output2 = call_3524
func_3536 = relay.Function([], output)
mod['func_3536'] = func_3536
mod = relay.transform.InferType()(mod)
mutated_mod['func_3536'] = func_3536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mutated_mod.get_global_var('func_3536')
call_3537 = func_3536_call()
output = call_3537
func_3538 = relay.Function([], output)
mutated_mod['func_3538'] = func_3538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1869_call = mod.get_global_var('func_1869')
func_1870_call = mutated_mod.get_global_var('func_1870')
call_3594 = func_1869_call()
call_3595 = func_1869_call()
func_2141_call = mod.get_global_var('func_2141')
func_2144_call = mutated_mod.get_global_var('func_2144')
var_3613 = relay.var("var_3613", dtype = "bool", shape = (288, 1))#candidate|3613|(288, 1)|var|bool
call_3612 = relay.TupleGetItem(func_2141_call(relay.reshape(var_3613.astype('bool'), [12, 2, 12]), relay.reshape(var_3613.astype('bool'), [12, 2, 12]), ), 0)
call_3614 = relay.TupleGetItem(func_2144_call(relay.reshape(var_3613.astype('bool'), [12, 2, 12]), relay.reshape(var_3613.astype('bool'), [12, 2, 12]), ), 0)
output = relay.Tuple([call_3594,call_3612,var_3613,])
output2 = relay.Tuple([call_3595,call_3614,var_3613,])
func_3616 = relay.Function([var_3613,], output)
mod['func_3616'] = func_3616
mod = relay.transform.InferType()(mod)
var_3617 = relay.var("var_3617", dtype = "bool", shape = (288, 1))#candidate|3617|(288, 1)|var|bool
output = func_3616(var_3617)
func_3618 = relay.Function([var_3617], output)
mutated_mod['func_3618'] = func_3618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_664_call = mod.get_global_var('func_664')
func_665_call = mutated_mod.get_global_var('func_665')
call_3620 = func_664_call()
call_3621 = func_664_call()
output = relay.Tuple([call_3620,])
output2 = relay.Tuple([call_3621,])
func_3637 = relay.Function([], output)
mod['func_3637'] = func_3637
mod = relay.transform.InferType()(mod)
mutated_mod['func_3637'] = func_3637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3637_call = mutated_mod.get_global_var('func_3637')
call_3638 = func_3637_call()
output = call_3638
func_3639 = relay.Function([], output)
mutated_mod['func_3639'] = func_3639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2542_call = mod.get_global_var('func_2542')
func_2543_call = mutated_mod.get_global_var('func_2543')
call_3691 = relay.TupleGetItem(func_2542_call(), 5)
call_3692 = relay.TupleGetItem(func_2543_call(), 5)
func_1616_call = mod.get_global_var('func_1616')
func_1617_call = mutated_mod.get_global_var('func_1617')
call_3698 = relay.TupleGetItem(func_1616_call(), 0)
call_3699 = relay.TupleGetItem(func_1617_call(), 0)
output = relay.Tuple([call_3691,call_3698,])
output2 = relay.Tuple([call_3692,call_3699,])
func_3700 = relay.Function([], output)
mod['func_3700'] = func_3700
mod = relay.transform.InferType()(mod)
output = func_3700()
func_3701 = relay.Function([], output)
mutated_mod['func_3701'] = func_3701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2191_call = mod.get_global_var('func_2191')
func_2192_call = mutated_mod.get_global_var('func_2192')
call_3705 = relay.TupleGetItem(func_2191_call(), 1)
call_3706 = relay.TupleGetItem(func_2192_call(), 1)
func_933_call = mod.get_global_var('func_933')
func_935_call = mutated_mod.get_global_var('func_935')
call_3750 = relay.TupleGetItem(func_933_call(), 0)
call_3751 = relay.TupleGetItem(func_935_call(), 0)
output = relay.Tuple([call_3705,call_3750,])
output2 = relay.Tuple([call_3706,call_3751,])
func_3758 = relay.Function([], output)
mod['func_3758'] = func_3758
mod = relay.transform.InferType()(mod)
output = func_3758()
func_3759 = relay.Function([], output)
mutated_mod['func_3759'] = func_3759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_3795 = func_859_call()
call_3796 = func_859_call()
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_3803 = relay.TupleGetItem(func_2034_call(), 1)
call_3804 = relay.TupleGetItem(func_2035_call(), 1)
func_1923_call = mod.get_global_var('func_1923')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_3805 = relay.TupleGetItem(func_1923_call(), 2)
call_3806 = relay.TupleGetItem(func_1925_call(), 2)
uop_3823 = relay.sigmoid(call_3805.astype('float32')) # shape=(12, 13, 6)
uop_3825 = relay.sigmoid(call_3806.astype('float32')) # shape=(12, 13, 6)
output = relay.Tuple([call_3795,call_3803,uop_3823,])
output2 = relay.Tuple([call_3796,call_3804,uop_3825,])
func_3826 = relay.Function([], output)
mod['func_3826'] = func_3826
mod = relay.transform.InferType()(mod)
mutated_mod['func_3826'] = func_3826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3826_call = mutated_mod.get_global_var('func_3826')
call_3827 = func_3826_call()
output = call_3827
func_3828 = relay.Function([], output)
mutated_mod['func_3828'] = func_3828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3829 = relay.var("var_3829", dtype = "uint8", shape = ())#candidate|3829|()|var|uint8
var_3830 = relay.var("var_3830", dtype = "uint8", shape = (2, 11, 14))#candidate|3830|(2, 11, 14)|var|uint8
bop_3831 = relay.left_shift(var_3829.astype('uint8'), var_3830.astype('uint8')) # shape=(2, 11, 14)
func_2358_call = mod.get_global_var('func_2358')
func_2359_call = mutated_mod.get_global_var('func_2359')
call_3835 = relay.TupleGetItem(func_2358_call(), 0)
call_3836 = relay.TupleGetItem(func_2359_call(), 0)
func_3616_call = mod.get_global_var('func_3616')
func_3618_call = mutated_mod.get_global_var('func_3618')
const_3851 = relay.const([False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True], dtype = "bool")#candidate|3851|(288,)|const|bool
call_3850 = relay.TupleGetItem(func_3616_call(relay.reshape(const_3851.astype('bool'), [288, 1])), 0)
call_3852 = relay.TupleGetItem(func_3618_call(relay.reshape(const_3851.astype('bool'), [288, 1])), 0)
func_2542_call = mod.get_global_var('func_2542')
func_2543_call = mutated_mod.get_global_var('func_2543')
call_3872 = relay.TupleGetItem(func_2542_call(), 6)
call_3873 = relay.TupleGetItem(func_2543_call(), 6)
func_791_call = mod.get_global_var('func_791')
func_793_call = mutated_mod.get_global_var('func_793')
const_3875 = relay.const([-7.780437,0.327646,-5.594775,-7.690479,-7.103655,7.507399,-4.818564,-3.338701,-1.789865,-5.607072,3.580929,-3.736433,-5.248484,-1.978013,2.389836,-3.547556,-0.729878,3.697938,-5.367415,9.356463,-2.586498,8.026070,-1.164171,1.321708,0.105577,8.488580,-2.428990,9.370827,-6.760332,-7.490958,-9.390852,4.556635,-4.055824,5.760166,-7.780513,2.024871,-2.121947,5.212995,1.327540,5.709372,-7.645159,3.115448,-7.700350,8.846028,-3.908972,4.846323,-5.651252,3.229104,7.235120,-4.494545,-5.688737,5.510372,-0.906981,0.639740,7.163594,-6.145504,8.701059,-2.749815,-1.718456,-2.723716,4.787093,1.386460,-7.356912,-8.368538,-1.322646,1.606778,2.023291,9.661453,3.416964,2.470544,0.434336,1.026048,2.385800,4.301438,4.835105,8.295616,2.507040,0.020432,3.066942,4.329458,-6.531224,-7.528030,7.709190,0.160916,-9.237173,3.825118,-1.074075,-7.125415,-7.515914,0.217502,2.403524,-8.092634,-7.942533,-1.307176,-6.581839,8.924072,-2.642394,-5.016419,8.589124,5.066291,-1.014717,0.802430,1.455012,-4.028753,0.251371,9.322405,-8.362825,9.620411,8.775260,7.423565,-9.892392,-6.137262,-5.808012,-3.970154,-7.458942,-5.262146,7.054812,5.528816,2.782342,-7.644518,-4.473191,-8.601207,-7.916323,0.866414,4.228354,6.118761,1.869355,0.978523,-5.581932,6.982507,4.084153,3.023845,0.818342,4.513355,-8.744692,-6.459542,8.025419,-6.410698,-4.299295,-8.921087,-1.117700,5.445597,6.461741,4.030823,4.140304,1.796777,-9.575151,5.344934,4.885970,6.346908,-1.156340,-4.392392,-0.824218,9.987621,-7.128363,-4.850966,7.766381,-1.006241,-2.747279,-4.629471,-6.548519,-9.530889,-2.988700,6.343723,-4.039911,-4.969175,-0.995976,1.130834,2.420027,9.293780,-2.957967,-9.127628,-2.301238,-4.629219,-1.141795,-6.946949,-8.501656,-3.379492,-5.288906,1.815943,-5.335559,9.436478,-2.267871,6.208350,-2.520090,-4.807337,-5.002490,-5.200671,4.521393,-1.890670,-5.107450,8.971148,9.975974,3.140747,4.271238,4.386381,-2.427717,-1.156587,5.130195,-5.810397,-8.611972,-6.762641,8.383715,7.064262,6.285507,7.487995,-0.535628,4.043042,-9.367148,5.286122,5.434059,6.736171,-3.898547,-6.430628,9.919790,3.292164,9.744913,-7.540068,-7.765134,-8.567788,2.340794,3.369758,-2.538297,-8.983937,-7.698817,-4.524695,-2.870377,1.570178,4.028384,-7.889837,3.116489,-8.483729,8.289521,3.324434,6.100567,2.790978,9.202317,-5.728434,8.823971,-2.985531,4.222122,0.857270,-6.136630,-0.966470,6.962351,-9.899572,-9.936721,2.971477,-1.260769,6.276362,-5.697186,-0.311852,-1.676522,8.382176,9.774965,1.633010,-2.484440,-1.836500,6.149707,-8.901600,6.177276,2.237405,-5.223670,2.316609,-5.941279,-7.008627,-9.039646,-0.002351,9.781713,-5.004428,-1.121943,1.578437,3.587303,0.656089,-7.634002,4.234030,2.439269,3.188385,7.894580,-4.646170,-4.904265,9.897345,4.602944,0.320688,9.221267,-1.988800,9.773869,0.564201,7.400586,0.298187,-9.847897,-0.333181,-9.159003,7.989145,-3.530424,9.507646,-8.135968,0.301397,-3.170308,7.786681,4.004697,8.146921,5.316334,2.971061,-6.025928,5.029500,9.019429,-1.764592,3.918131,1.431766,7.957838,-5.728005,6.044399,9.079527,-0.363413,-5.202606,-3.779711,-3.823467,-9.498173,6.430779,3.525198,0.844453,-1.611200,-6.114653,-8.744281,4.226304,-8.112437,8.730001,-2.791353,1.359348,3.255087,-3.734457,-9.176693,-9.168137,-3.670149,6.612357,-4.024635,-4.198338,-5.347882,-3.308607,-1.479753,-4.610464,-9.316693,1.748106,-6.844454,8.956661,-2.113888,-8.062459,3.147950,0.999185,-1.668273,5.450775,5.919619,0.124973,-4.837853,-3.079159,9.110665,9.408644,4.218867,-4.341530,6.472408,0.113902,0.879377,-1.534172,-4.875508,-7.853306,-4.799104,2.581625,2.058310,2.117122,5.139687,3.101548,-1.469834,-7.300904,9.471847,-6.843375,-6.233327,-8.910121,9.215002,-6.758460,-3.589865,-9.250712,-9.138096,-7.387418,-7.181108,9.323241,-0.015375,-6.191899,0.437955,-3.636389], dtype = "float32")#candidate|3875|(390,)|const|float32
call_3874 = relay.TupleGetItem(func_791_call(relay.reshape(const_3875.astype('float32'), [13, 5, 6])), 1)
call_3876 = relay.TupleGetItem(func_793_call(relay.reshape(const_3875.astype('float32'), [13, 5, 6])), 1)
output = relay.Tuple([bop_3831,call_3835,call_3850,const_3851,call_3872,call_3874,const_3875,])
output2 = relay.Tuple([bop_3831,call_3836,call_3852,const_3851,call_3873,call_3876,const_3875,])
func_3883 = relay.Function([var_3829,var_3830,], output)
mod['func_3883'] = func_3883
mod = relay.transform.InferType()(mod)
var_3884 = relay.var("var_3884", dtype = "uint8", shape = ())#candidate|3884|()|var|uint8
var_3885 = relay.var("var_3885", dtype = "uint8", shape = (2, 11, 14))#candidate|3885|(2, 11, 14)|var|uint8
output = func_3883(var_3884,var_3885,)
func_3886 = relay.Function([var_3884,var_3885,], output)
mutated_mod['func_3886'] = func_3886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2542_call = mod.get_global_var('func_2542')
func_2543_call = mutated_mod.get_global_var('func_2543')
call_3891 = relay.TupleGetItem(func_2542_call(), 7)
call_3892 = relay.TupleGetItem(func_2543_call(), 7)
func_1160_call = mod.get_global_var('func_1160')
func_1161_call = mutated_mod.get_global_var('func_1161')
call_3904 = relay.TupleGetItem(func_1160_call(), 0)
call_3905 = relay.TupleGetItem(func_1161_call(), 0)
func_933_call = mod.get_global_var('func_933')
func_935_call = mutated_mod.get_global_var('func_935')
call_3911 = relay.TupleGetItem(func_933_call(), 0)
call_3912 = relay.TupleGetItem(func_935_call(), 0)
func_67_call = mod.get_global_var('func_67')
func_69_call = mutated_mod.get_global_var('func_69')
var_3914 = relay.var("var_3914", dtype = "float64", shape = (50,))#candidate|3914|(50,)|var|float64
call_3913 = relay.TupleGetItem(func_67_call(relay.reshape(var_3914.astype('float64'), [2, 5, 5])), 0)
call_3915 = relay.TupleGetItem(func_69_call(relay.reshape(var_3914.astype('float64'), [2, 5, 5])), 0)
output = relay.Tuple([call_3891,call_3904,call_3911,call_3913,var_3914,])
output2 = relay.Tuple([call_3892,call_3905,call_3912,call_3915,var_3914,])
func_3918 = relay.Function([var_3914,], output)
mod['func_3918'] = func_3918
mod = relay.transform.InferType()(mod)
var_3919 = relay.var("var_3919", dtype = "float64", shape = (50,))#candidate|3919|(50,)|var|float64
output = func_3918(var_3919)
func_3920 = relay.Function([var_3919], output)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1616_call = mod.get_global_var('func_1616')
func_1617_call = mutated_mod.get_global_var('func_1617')
call_3936 = relay.TupleGetItem(func_1616_call(), 1)
call_3937 = relay.TupleGetItem(func_1617_call(), 1)
output = call_3936
output2 = call_3937
func_3965 = relay.Function([], output)
mod['func_3965'] = func_3965
mod = relay.transform.InferType()(mod)
mutated_mod['func_3965'] = func_3965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3965_call = mutated_mod.get_global_var('func_3965')
call_3966 = func_3965_call()
output = call_3966
func_3967 = relay.Function([], output)
mutated_mod['func_3967'] = func_3967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_3982 = relay.TupleGetItem(func_1272_call(), 0)
call_3983 = relay.TupleGetItem(func_1273_call(), 0)
func_3700_call = mod.get_global_var('func_3700')
func_3701_call = mutated_mod.get_global_var('func_3701')
call_4006 = relay.TupleGetItem(func_3700_call(), 0)
call_4007 = relay.TupleGetItem(func_3701_call(), 0)
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_4024 = relay.TupleGetItem(func_907_call(), 0)
call_4025 = relay.TupleGetItem(func_908_call(), 0)
output = relay.Tuple([call_3982,call_4006,call_4024,])
output2 = relay.Tuple([call_3983,call_4007,call_4025,])
func_4034 = relay.Function([], output)
mod['func_4034'] = func_4034
mod = relay.transform.InferType()(mod)
output = func_4034()
func_4035 = relay.Function([], output)
mutated_mod['func_4035'] = func_4035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3758_call = mod.get_global_var('func_3758')
func_3759_call = mutated_mod.get_global_var('func_3759')
call_4058 = relay.TupleGetItem(func_3758_call(), 0)
call_4059 = relay.TupleGetItem(func_3759_call(), 0)
func_3008_call = mod.get_global_var('func_3008')
func_3012_call = mutated_mod.get_global_var('func_3012')
var_4067 = relay.var("var_4067", dtype = "uint16", shape = (2, 728))#candidate|4067|(2, 728)|var|uint16
call_4066 = relay.TupleGetItem(func_3008_call(relay.reshape(var_4067.astype('uint16'), [13, 16, 7]), relay.reshape(var_4067.astype('uint16'), [13, 16, 7]), ), 0)
call_4068 = relay.TupleGetItem(func_3012_call(relay.reshape(var_4067.astype('uint16'), [13, 16, 7]), relay.reshape(var_4067.astype('uint16'), [13, 16, 7]), ), 0)
func_933_call = mod.get_global_var('func_933')
func_935_call = mutated_mod.get_global_var('func_935')
call_4070 = relay.TupleGetItem(func_933_call(), 0)
call_4071 = relay.TupleGetItem(func_935_call(), 0)
uop_4076 = relay.cos(call_4066.astype('float64')) # shape=(13, 16, 7)
uop_4078 = relay.cos(call_4068.astype('float64')) # shape=(13, 16, 7)
uop_4086 = relay.asin(uop_4076.astype('float64')) # shape=(13, 16, 7)
uop_4088 = relay.asin(uop_4078.astype('float64')) # shape=(13, 16, 7)
output = relay.Tuple([call_4058,var_4067,call_4070,uop_4086,])
output2 = relay.Tuple([call_4059,var_4067,call_4071,uop_4088,])
func_4098 = relay.Function([var_4067,], output)
mod['func_4098'] = func_4098
mod = relay.transform.InferType()(mod)
var_4099 = relay.var("var_4099", dtype = "uint16", shape = (2, 728))#candidate|4099|(2, 728)|var|uint16
output = func_4098(var_4099)
func_4100 = relay.Function([var_4099], output)
mutated_mod['func_4100'] = func_4100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2966_call = mod.get_global_var('func_2966')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_4102 = relay.TupleGetItem(func_2966_call(), 0)
call_4103 = relay.TupleGetItem(func_2968_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_4134 = relay.TupleGetItem(func_296_call(), 0)
call_4135 = relay.TupleGetItem(func_298_call(), 0)
bop_4136 = relay.bitwise_or(call_4134.astype('int16'), relay.reshape(call_4102.astype('int16'), relay.shape_of(call_4134))) # shape=(12, 13, 6)
bop_4139 = relay.bitwise_or(call_4135.astype('int16'), relay.reshape(call_4103.astype('int16'), relay.shape_of(call_4135))) # shape=(12, 13, 6)
output = relay.Tuple([bop_4136,])
output2 = relay.Tuple([bop_4139,])
func_4143 = relay.Function([], output)
mod['func_4143'] = func_4143
mod = relay.transform.InferType()(mod)
mutated_mod['func_4143'] = func_4143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4143_call = mutated_mod.get_global_var('func_4143')
call_4144 = func_4143_call()
output = call_4144
func_4145 = relay.Function([], output)
mutated_mod['func_4145'] = func_4145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_4153 = func_859_call()
call_4154 = func_859_call()
output = call_4153
output2 = call_4154
func_4168 = relay.Function([], output)
mod['func_4168'] = func_4168
mod = relay.transform.InferType()(mod)
mutated_mod['func_4168'] = func_4168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4168_call = mutated_mod.get_global_var('func_4168')
call_4169 = func_4168_call()
output = call_4169
func_4170 = relay.Function([], output)
mutated_mod['func_4170'] = func_4170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2191_call = mod.get_global_var('func_2191')
func_2192_call = mutated_mod.get_global_var('func_2192')
call_4185 = relay.TupleGetItem(func_2191_call(), 2)
call_4186 = relay.TupleGetItem(func_2192_call(), 2)
output = relay.Tuple([call_4185,])
output2 = relay.Tuple([call_4186,])
func_4189 = relay.Function([], output)
mod['func_4189'] = func_4189
mod = relay.transform.InferType()(mod)
mutated_mod['func_4189'] = func_4189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4189_call = mutated_mod.get_global_var('func_4189')
call_4190 = func_4189_call()
output = call_4190
func_4191 = relay.Function([], output)
mutated_mod['func_4191'] = func_4191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_664_call = mod.get_global_var('func_664')
func_665_call = mutated_mod.get_global_var('func_665')
call_4219 = func_664_call()
call_4220 = func_664_call()
output = call_4219
output2 = call_4220
func_4274 = relay.Function([], output)
mod['func_4274'] = func_4274
mod = relay.transform.InferType()(mod)
output = func_4274()
func_4275 = relay.Function([], output)
mutated_mod['func_4275'] = func_4275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1160_call = mod.get_global_var('func_1160')
func_1161_call = mutated_mod.get_global_var('func_1161')
call_4337 = relay.TupleGetItem(func_1160_call(), 0)
call_4338 = relay.TupleGetItem(func_1161_call(), 0)
output = call_4337
output2 = call_4338
func_4339 = relay.Function([], output)
mod['func_4339'] = func_4339
mod = relay.transform.InferType()(mod)
mutated_mod['func_4339'] = func_4339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4339_call = mutated_mod.get_global_var('func_4339')
call_4340 = func_4339_call()
output = call_4340
func_4341 = relay.Function([], output)
mutated_mod['func_4341'] = func_4341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_4364 = relay.TupleGetItem(func_1571_call(), 1)
call_4365 = relay.TupleGetItem(func_1573_call(), 1)
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_4374 = relay.TupleGetItem(func_393_call(), 0)
call_4375 = relay.TupleGetItem(func_395_call(), 0)
func_2966_call = mod.get_global_var('func_2966')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_4389 = relay.TupleGetItem(func_2966_call(), 0)
call_4390 = relay.TupleGetItem(func_2968_call(), 0)
output = relay.Tuple([call_4364,call_4374,call_4389,])
output2 = relay.Tuple([call_4365,call_4375,call_4390,])
func_4391 = relay.Function([], output)
mod['func_4391'] = func_4391
mod = relay.transform.InferType()(mod)
mutated_mod['func_4391'] = func_4391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4391_call = mutated_mod.get_global_var('func_4391')
call_4392 = func_4391_call()
output = call_4392
func_4393 = relay.Function([], output)
mutated_mod['func_4393'] = func_4393
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4452 = relay.var("var_4452", dtype = "float64", shape = (9, 10, 14))#candidate|4452|(9, 10, 14)|var|float64
var_4453 = relay.var("var_4453", dtype = "float64", shape = (9, 10, 14))#candidate|4453|(9, 10, 14)|var|float64
bop_4454 = relay.divide(var_4452.astype('float64'), relay.reshape(var_4453.astype('float64'), relay.shape_of(var_4452))) # shape=(9, 10, 14)
uop_4458 = relay.log10(var_4452.astype('float64')) # shape=(9, 10, 14)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_4465 = relay.TupleGetItem(func_1571_call(), 1)
call_4466 = relay.TupleGetItem(func_1573_call(), 1)
output = relay.Tuple([bop_4454,uop_4458,call_4465,])
output2 = relay.Tuple([bop_4454,uop_4458,call_4466,])
func_4468 = relay.Function([var_4452,var_4453,], output)
mod['func_4468'] = func_4468
mod = relay.transform.InferType()(mod)
var_4469 = relay.var("var_4469", dtype = "float64", shape = (9, 10, 14))#candidate|4469|(9, 10, 14)|var|float64
var_4470 = relay.var("var_4470", dtype = "float64", shape = (9, 10, 14))#candidate|4470|(9, 10, 14)|var|float64
output = func_4468(var_4469,var_4470,)
func_4471 = relay.Function([var_4469,var_4470,], output)
mutated_mod['func_4471'] = func_4471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1434_call = mod.get_global_var('func_1434')
func_1436_call = mutated_mod.get_global_var('func_1436')
call_4501 = func_1434_call()
call_4502 = func_1434_call()
output = call_4501
output2 = call_4502
func_4511 = relay.Function([], output)
mod['func_4511'] = func_4511
mod = relay.transform.InferType()(mod)
output = func_4511()
func_4512 = relay.Function([], output)
mutated_mod['func_4512'] = func_4512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3758_call = mod.get_global_var('func_3758')
func_3759_call = mutated_mod.get_global_var('func_3759')
call_4524 = relay.TupleGetItem(func_3758_call(), 0)
call_4525 = relay.TupleGetItem(func_3759_call(), 0)
func_2259_call = mod.get_global_var('func_2259')
func_2264_call = mutated_mod.get_global_var('func_2264')
var_4528 = relay.var("var_4528", dtype = "bool", shape = (900,))#candidate|4528|(900,)|var|bool
call_4527 = relay.TupleGetItem(func_2259_call(relay.reshape(var_4528.astype('bool'), [5, 15, 12]), relay.reshape(var_4528.astype('bool'), [5, 15, 12]), relay.reshape(call_4524.astype('uint64'), [12, 13, 6]), ), 0)
call_4529 = relay.TupleGetItem(func_2264_call(relay.reshape(var_4528.astype('bool'), [5, 15, 12]), relay.reshape(var_4528.astype('bool'), [5, 15, 12]), relay.reshape(call_4524.astype('uint64'), [12, 13, 6]), ), 0)
uop_4530 = relay.asin(call_4527.astype('float32')) # shape=(50,)
uop_4532 = relay.asin(call_4529.astype('float32')) # shape=(50,)
output = relay.Tuple([call_4524,var_4528,uop_4530,])
output2 = relay.Tuple([call_4525,var_4528,uop_4532,])
func_4533 = relay.Function([var_4528,], output)
mod['func_4533'] = func_4533
mod = relay.transform.InferType()(mod)
mutated_mod['func_4533'] = func_4533
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4534 = relay.var("var_4534", dtype = "bool", shape = (900,))#candidate|4534|(900,)|var|bool
func_4533_call = mutated_mod.get_global_var('func_4533')
call_4535 = func_4533_call(var_4534)
output = call_4535
func_4536 = relay.Function([var_4534], output)
mutated_mod['func_4536'] = func_4536
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4547 = relay.var("var_4547", dtype = "uint64", shape = ())#candidate|4547|()|var|uint64
var_4548 = relay.var("var_4548", dtype = "uint64", shape = (15, 13, 13))#candidate|4548|(15, 13, 13)|var|uint64
bop_4549 = relay.maximum(var_4547.astype('uint64'), var_4548.astype('uint64')) # shape=(15, 13, 13)
uop_4552 = relay.tan(var_4548.astype('float64')) # shape=(15, 13, 13)
bop_4557 = relay.right_shift(uop_4552.astype('uint32'), var_4547.astype('uint32')) # shape=(15, 13, 13)
var_4560 = relay.var("var_4560", dtype = "float64", shape = (15, 13, 13))#candidate|4560|(15, 13, 13)|var|float64
bop_4561 = relay.minimum(uop_4552.astype('uint16'), relay.reshape(var_4560.astype('uint16'), relay.shape_of(uop_4552))) # shape=(15, 13, 13)
output = relay.Tuple([bop_4549,bop_4557,bop_4561,])
output2 = relay.Tuple([bop_4549,bop_4557,bop_4561,])
func_4565 = relay.Function([var_4547,var_4548,var_4560,], output)
mod['func_4565'] = func_4565
mod = relay.transform.InferType()(mod)
var_4566 = relay.var("var_4566", dtype = "uint64", shape = ())#candidate|4566|()|var|uint64
var_4567 = relay.var("var_4567", dtype = "uint64", shape = (15, 13, 13))#candidate|4567|(15, 13, 13)|var|uint64
var_4568 = relay.var("var_4568", dtype = "float64", shape = (15, 13, 13))#candidate|4568|(15, 13, 13)|var|float64
output = func_4565(var_4566,var_4567,var_4568,)
func_4569 = relay.Function([var_4566,var_4567,var_4568,], output)
mutated_mod['func_4569'] = func_4569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4663 = relay.var("var_4663", dtype = "int16", shape = (15, 12, 14))#candidate|4663|(15, 12, 14)|var|int16
var_4664 = relay.var("var_4664", dtype = "int16", shape = (15, 12, 14))#candidate|4664|(15, 12, 14)|var|int16
bop_4665 = relay.minimum(var_4663.astype('int16'), relay.reshape(var_4664.astype('int16'), relay.shape_of(var_4663))) # shape=(15, 12, 14)
uop_4677 = relay.rsqrt(var_4663.astype('float32')) # shape=(15, 12, 14)
func_3883_call = mod.get_global_var('func_3883')
func_3886_call = mutated_mod.get_global_var('func_3886')
var_4687 = relay.var("var_4687", dtype = "uint8", shape = ())#candidate|4687|()|var|uint8
const_4688 = relay.const([-3,-9,5,-10,-1,4,4,-7,-3,-6,3,-2,3,1,10,10,-6,-8,-6,9,-5,3,5,2,-7,10,6,-2,-7,4,10,-9,-5,-5,-7,-8,-5,4,1,7,-8,7,-10,2,-1,-3,10,-5,-10,6,3,4,5,10,-5,5,6,7,8,-1,8,9,-9,3,-5,9,-4,-7,-2,-6,-6,2,10,7,-1,-10,6,6,-4,-5,9,8,-8,2,-4,6,-9,3,8,-9,2,-5,-9,-2,-2,-3,-2,6,-5,-9,-7,10,-5,-7,-3,-1,8,-3,-9,-9,3,-3,2,-6,-8,-6,4,-2,7,2,-6,6,1,10,-6,10,-2,6,-10,8,1,-4,-10,-2,4,10,8,-3,-5,6,3,-1,-9,-6,1,-9,-10,5,-7,-8,4,-10,-3,-9,5,10,-5,2,9,-5,4,3,8,5,-9,-8,-10,-5,-3,-3,-4,-6,-5,-3,6,7,3,-5,1,8,-4,5,7,9,6,6,-5,9,1,-8,-1,9,8,6,-4,1,1,10,-8,5,10,-6,-6,-9,-6,-5,2,10,8,9,-8,-7,-8,6,7,2,5,-6,-10,1,10,2,2,3,-7,9,7,-6,-5,3,-6,-1,10,3,10,7,-1,-5,-2,-2,-5,4,-7,6,-3,-3,-1,-9,10,2,-7,2,-9,-1,-7,8,2,-1,4,-2,-6,5,9,-8,-5,3,-1,-10,-3,-1,-1,-10,3,-5,-1,-4,-4,-4,-3,4,-7,10,1,8,10,-4,-8,-6,-8,-6,8,7,8,-4,6,-7,-4,-10,-8,1,-6,8,1,-3,-5,-1,-10,2], dtype = "uint8")#candidate|4688|(308,)|const|uint8
call_4686 = relay.TupleGetItem(func_3883_call(relay.reshape(var_4687.astype('uint8'), []), relay.reshape(const_4688.astype('uint8'), [2, 11, 14]), ), 2)
call_4689 = relay.TupleGetItem(func_3886_call(relay.reshape(var_4687.astype('uint8'), []), relay.reshape(const_4688.astype('uint8'), [2, 11, 14]), ), 2)
output = relay.Tuple([bop_4665,uop_4677,call_4686,var_4687,const_4688,])
output2 = relay.Tuple([bop_4665,uop_4677,call_4689,var_4687,const_4688,])
func_4693 = relay.Function([var_4663,var_4664,var_4687,], output)
mod['func_4693'] = func_4693
mod = relay.transform.InferType()(mod)
var_4694 = relay.var("var_4694", dtype = "int16", shape = (15, 12, 14))#candidate|4694|(15, 12, 14)|var|int16
var_4695 = relay.var("var_4695", dtype = "int16", shape = (15, 12, 14))#candidate|4695|(15, 12, 14)|var|int16
var_4696 = relay.var("var_4696", dtype = "uint8", shape = ())#candidate|4696|()|var|uint8
output = func_4693(var_4694,var_4695,var_4696,)
func_4697 = relay.Function([var_4694,var_4695,var_4696,], output)
mutated_mod['func_4697'] = func_4697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1802_call = mutated_mod.get_global_var('func_1802')
call_4707 = relay.TupleGetItem(func_1801_call(), 1)
call_4708 = relay.TupleGetItem(func_1802_call(), 1)
output = relay.Tuple([call_4707,])
output2 = relay.Tuple([call_4708,])
func_4743 = relay.Function([], output)
mod['func_4743'] = func_4743
mod = relay.transform.InferType()(mod)
output = func_4743()
func_4744 = relay.Function([], output)
mutated_mod['func_4744'] = func_4744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3700_call = mod.get_global_var('func_3700')
func_3701_call = mutated_mod.get_global_var('func_3701')
call_4822 = relay.TupleGetItem(func_3700_call(), 0)
call_4823 = relay.TupleGetItem(func_3701_call(), 0)
func_4743_call = mod.get_global_var('func_4743')
func_4744_call = mutated_mod.get_global_var('func_4744')
call_4832 = relay.TupleGetItem(func_4743_call(), 0)
call_4833 = relay.TupleGetItem(func_4744_call(), 0)
output = relay.Tuple([call_4822,call_4832,])
output2 = relay.Tuple([call_4823,call_4833,])
func_4840 = relay.Function([], output)
mod['func_4840'] = func_4840
mod = relay.transform.InferType()(mod)
mutated_mod['func_4840'] = func_4840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4840_call = mutated_mod.get_global_var('func_4840')
call_4841 = func_4840_call()
output = call_4841
func_4842 = relay.Function([], output)
mutated_mod['func_4842'] = func_4842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3637_call = mod.get_global_var('func_3637')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_4868 = relay.TupleGetItem(func_3637_call(), 0)
call_4869 = relay.TupleGetItem(func_3639_call(), 0)
output = relay.Tuple([call_4868,])
output2 = relay.Tuple([call_4869,])
func_4870 = relay.Function([], output)
mod['func_4870'] = func_4870
mod = relay.transform.InferType()(mod)
mutated_mod['func_4870'] = func_4870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4870_call = mutated_mod.get_global_var('func_4870')
call_4871 = func_4870_call()
output = call_4871
func_4872 = relay.Function([], output)
mutated_mod['func_4872'] = func_4872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2542_call = mod.get_global_var('func_2542')
func_2543_call = mutated_mod.get_global_var('func_2543')
call_4913 = relay.TupleGetItem(func_2542_call(), 8)
call_4914 = relay.TupleGetItem(func_2543_call(), 8)
func_3700_call = mod.get_global_var('func_3700')
func_3701_call = mutated_mod.get_global_var('func_3701')
call_4923 = relay.TupleGetItem(func_3700_call(), 1)
call_4924 = relay.TupleGetItem(func_3701_call(), 1)
func_3410_call = mod.get_global_var('func_3410')
func_3412_call = mutated_mod.get_global_var('func_3412')
call_4934 = func_3410_call()
call_4935 = func_3410_call()
output = relay.Tuple([call_4913,call_4923,call_4934,])
output2 = relay.Tuple([call_4914,call_4924,call_4935,])
func_4939 = relay.Function([], output)
mod['func_4939'] = func_4939
mod = relay.transform.InferType()(mod)
mutated_mod['func_4939'] = func_4939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4939_call = mutated_mod.get_global_var('func_4939')
call_4940 = func_4939_call()
output = call_4940
func_4941 = relay.Function([], output)
mutated_mod['func_4941'] = func_4941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3410_call = mod.get_global_var('func_3410')
func_3412_call = mutated_mod.get_global_var('func_3412')
call_4990 = func_3410_call()
call_4991 = func_3410_call()
func_3965_call = mod.get_global_var('func_3965')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_5019 = func_3965_call()
call_5020 = func_3965_call()
uop_5034 = relay.asinh(call_5019.astype('float64')) # shape=(50,)
uop_5036 = relay.asinh(call_5020.astype('float64')) # shape=(50,)
output = relay.Tuple([call_4990,uop_5034,])
output2 = relay.Tuple([call_4991,uop_5036,])
func_5037 = relay.Function([], output)
mod['func_5037'] = func_5037
mod = relay.transform.InferType()(mod)
output = func_5037()
func_5038 = relay.Function([], output)
mutated_mod['func_5038'] = func_5038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2542_call = mod.get_global_var('func_2542')
func_2543_call = mutated_mod.get_global_var('func_2543')
call_5093 = relay.TupleGetItem(func_2542_call(), 2)
call_5094 = relay.TupleGetItem(func_2543_call(), 2)
func_2070_call = mod.get_global_var('func_2070')
func_2072_call = mutated_mod.get_global_var('func_2072')
var_5101 = relay.var("var_5101", dtype = "float32", shape = (84, 1))#candidate|5101|(84, 1)|var|float32
call_5100 = relay.TupleGetItem(func_2070_call(relay.reshape(var_5101.astype('float32'), [4, 7, 3])), 0)
call_5102 = relay.TupleGetItem(func_2072_call(relay.reshape(var_5101.astype('float32'), [4, 7, 3])), 0)
output = relay.Tuple([call_5093,call_5100,var_5101,])
output2 = relay.Tuple([call_5094,call_5102,var_5101,])
func_5104 = relay.Function([var_5101,], output)
mod['func_5104'] = func_5104
mod = relay.transform.InferType()(mod)
mutated_mod['func_5104'] = func_5104
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5105 = relay.var("var_5105", dtype = "float32", shape = (84, 1))#candidate|5105|(84, 1)|var|float32
func_5104_call = mutated_mod.get_global_var('func_5104')
call_5106 = func_5104_call(var_5105)
output = call_5106
func_5107 = relay.Function([var_5105], output)
mutated_mod['func_5107'] = func_5107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1983_call = mod.get_global_var('func_1983')
func_1984_call = mutated_mod.get_global_var('func_1984')
call_5125 = relay.TupleGetItem(func_1983_call(), 1)
call_5126 = relay.TupleGetItem(func_1984_call(), 1)
output = call_5125
output2 = call_5126
func_5129 = relay.Function([], output)
mod['func_5129'] = func_5129
mod = relay.transform.InferType()(mod)
mutated_mod['func_5129'] = func_5129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5129_call = mutated_mod.get_global_var('func_5129')
call_5130 = func_5129_call()
output = call_5130
func_5131 = relay.Function([], output)
mutated_mod['func_5131'] = func_5131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1160_call = mod.get_global_var('func_1160')
func_1161_call = mutated_mod.get_global_var('func_1161')
call_5147 = relay.TupleGetItem(func_1160_call(), 0)
call_5148 = relay.TupleGetItem(func_1161_call(), 0)
output = call_5147
output2 = call_5148
func_5161 = relay.Function([], output)
mod['func_5161'] = func_5161
mod = relay.transform.InferType()(mod)
mutated_mod['func_5161'] = func_5161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5161_call = mutated_mod.get_global_var('func_5161')
call_5162 = func_5161_call()
output = call_5162
func_5163 = relay.Function([], output)
mutated_mod['func_5163'] = func_5163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1616_call = mod.get_global_var('func_1616')
func_1617_call = mutated_mod.get_global_var('func_1617')
call_5179 = relay.TupleGetItem(func_1616_call(), 0)
call_5180 = relay.TupleGetItem(func_1617_call(), 0)
var_5205 = relay.var("var_5205", dtype = "float64", shape = (12, 13, 6))#candidate|5205|(12, 13, 6)|var|float64
bop_5206 = relay.floor_divide(call_5179.astype('float64'), relay.reshape(var_5205.astype('float64'), relay.shape_of(call_5179))) # shape=(12, 13, 6)
bop_5209 = relay.floor_divide(call_5180.astype('float64'), relay.reshape(var_5205.astype('float64'), relay.shape_of(call_5180))) # shape=(12, 13, 6)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_5210 = relay.TupleGetItem(func_2034_call(), 1)
call_5211 = relay.TupleGetItem(func_2035_call(), 1)
output = relay.Tuple([bop_5206,call_5210,])
output2 = relay.Tuple([bop_5209,call_5211,])
func_5221 = relay.Function([var_5205,], output)
mod['func_5221'] = func_5221
mod = relay.transform.InferType()(mod)
mutated_mod['func_5221'] = func_5221
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5222 = relay.var("var_5222", dtype = "float64", shape = (12, 13, 6))#candidate|5222|(12, 13, 6)|var|float64
func_5221_call = mutated_mod.get_global_var('func_5221')
call_5223 = func_5221_call(var_5222)
output = call_5223
func_5224 = relay.Function([var_5222], output)
mutated_mod['func_5224'] = func_5224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1041_call = mod.get_global_var('func_1041')
func_1043_call = mutated_mod.get_global_var('func_1043')
call_5226 = relay.TupleGetItem(func_1041_call(), 0)
call_5227 = relay.TupleGetItem(func_1043_call(), 0)
func_1923_call = mod.get_global_var('func_1923')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_5234 = relay.TupleGetItem(func_1923_call(), 1)
call_5235 = relay.TupleGetItem(func_1925_call(), 1)
output = relay.Tuple([call_5226,call_5234,])
output2 = relay.Tuple([call_5227,call_5235,])
func_5238 = relay.Function([], output)
mod['func_5238'] = func_5238
mod = relay.transform.InferType()(mod)
mutated_mod['func_5238'] = func_5238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5238_call = mutated_mod.get_global_var('func_5238')
call_5239 = func_5238_call()
output = call_5239
func_5240 = relay.Function([], output)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2448_call = mod.get_global_var('func_2448')
func_2450_call = mutated_mod.get_global_var('func_2450')
call_5250 = func_2448_call()
call_5251 = func_2448_call()
output = relay.Tuple([call_5250,])
output2 = relay.Tuple([call_5251,])
func_5254 = relay.Function([], output)
mod['func_5254'] = func_5254
mod = relay.transform.InferType()(mod)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5254_call = mutated_mod.get_global_var('func_5254')
call_5255 = func_5254_call()
output = call_5255
func_5256 = relay.Function([], output)
mutated_mod['func_5256'] = func_5256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_5352 = func_859_call()
call_5353 = func_859_call()
func_4693_call = mod.get_global_var('func_4693')
func_4697_call = mutated_mod.get_global_var('func_4697')
var_5364 = relay.var("var_5364", dtype = "int16", shape = (2520,))#candidate|5364|(2520,)|var|int16
var_5365 = relay.var("var_5365", dtype = "uint8", shape = ())#candidate|5365|()|var|uint8
call_5363 = relay.TupleGetItem(func_4693_call(relay.reshape(var_5364.astype('int16'), [15, 12, 14]), relay.reshape(var_5364.astype('int16'), [15, 12, 14]), relay.reshape(var_5365.astype('uint8'), []), ), 3)
call_5366 = relay.TupleGetItem(func_4697_call(relay.reshape(var_5364.astype('int16'), [15, 12, 14]), relay.reshape(var_5364.astype('int16'), [15, 12, 14]), relay.reshape(var_5365.astype('uint8'), []), ), 3)
func_1160_call = mod.get_global_var('func_1160')
func_1161_call = mutated_mod.get_global_var('func_1161')
call_5369 = relay.TupleGetItem(func_1160_call(), 0)
call_5370 = relay.TupleGetItem(func_1161_call(), 0)
func_3637_call = mod.get_global_var('func_3637')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_5407 = relay.TupleGetItem(func_3637_call(), 0)
call_5408 = relay.TupleGetItem(func_3639_call(), 0)
func_4533_call = mod.get_global_var('func_4533')
func_4536_call = mutated_mod.get_global_var('func_4536')
var_5411 = relay.var("var_5411", dtype = "bool", shape = (900,))#candidate|5411|(900,)|var|bool
call_5410 = relay.TupleGetItem(func_4533_call(relay.reshape(var_5411.astype('bool'), [900,])), 2)
call_5412 = relay.TupleGetItem(func_4536_call(relay.reshape(var_5411.astype('bool'), [900,])), 2)
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_5421 = relay.TupleGetItem(func_2421_call(), 0)
call_5422 = relay.TupleGetItem(func_2422_call(), 0)
func_1801_call = mod.get_global_var('func_1801')
func_1802_call = mutated_mod.get_global_var('func_1802')
call_5431 = relay.TupleGetItem(func_1801_call(), 2)
call_5432 = relay.TupleGetItem(func_1802_call(), 2)
func_2303_call = mod.get_global_var('func_2303')
func_2304_call = mutated_mod.get_global_var('func_2304')
call_5433 = relay.TupleGetItem(func_2303_call(), 0)
call_5434 = relay.TupleGetItem(func_2304_call(), 0)
output = relay.Tuple([call_5352,call_5363,var_5364,var_5365,call_5369,call_5407,call_5410,var_5411,call_5421,call_5431,call_5433,])
output2 = relay.Tuple([call_5353,call_5366,var_5364,var_5365,call_5370,call_5408,call_5412,var_5411,call_5422,call_5432,call_5434,])
func_5438 = relay.Function([var_5364,var_5365,var_5411,], output)
mod['func_5438'] = func_5438
mod = relay.transform.InferType()(mod)
var_5439 = relay.var("var_5439", dtype = "int16", shape = (2520,))#candidate|5439|(2520,)|var|int16
var_5440 = relay.var("var_5440", dtype = "uint8", shape = ())#candidate|5440|()|var|uint8
var_5441 = relay.var("var_5441", dtype = "bool", shape = (900,))#candidate|5441|(900,)|var|bool
output = func_5438(var_5439,var_5440,var_5441,)
func_5442 = relay.Function([var_5439,var_5440,var_5441,], output)
mutated_mod['func_5442'] = func_5442
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5452 = relay.var("var_5452", dtype = "uint32", shape = (9, 16, 3))#candidate|5452|(9, 16, 3)|var|uint32
var_5453 = relay.var("var_5453", dtype = "uint32", shape = (9, 16, 3))#candidate|5453|(9, 16, 3)|var|uint32
bop_5454 = relay.less_equal(var_5452.astype('bool'), relay.reshape(var_5453.astype('bool'), relay.shape_of(var_5452))) # shape=(9, 16, 3)
func_1257_call = mod.get_global_var('func_1257')
func_1259_call = mutated_mod.get_global_var('func_1259')
var_5462 = relay.var("var_5462", dtype = "bool", shape = (40,))#candidate|5462|(40,)|var|bool
call_5461 = relay.TupleGetItem(func_1257_call(relay.reshape(var_5462.astype('bool'), [5, 2, 4])), 5)
call_5463 = relay.TupleGetItem(func_1259_call(relay.reshape(var_5462.astype('bool'), [5, 2, 4])), 5)
bop_5465 = relay.subtract(var_5452.astype('int32'), relay.reshape(var_5453.astype('int32'), relay.shape_of(var_5452))) # shape=(9, 16, 3)
bop_5468 = relay.logical_or(var_5453.astype('bool'), relay.reshape(bop_5465.astype('bool'), relay.shape_of(var_5453))) # shape=(9, 16, 3)
output = relay.Tuple([bop_5454,call_5461,var_5462,bop_5468,])
output2 = relay.Tuple([bop_5454,call_5463,var_5462,bop_5468,])
func_5474 = relay.Function([var_5452,var_5453,var_5462,], output)
mod['func_5474'] = func_5474
mod = relay.transform.InferType()(mod)
mutated_mod['func_5474'] = func_5474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5474_call = mutated_mod.get_global_var('func_5474')
var_5476 = relay.var("var_5476", dtype = "uint32", shape = (9, 16, 3))#candidate|5476|(9, 16, 3)|var|uint32
var_5477 = relay.var("var_5477", dtype = "uint32", shape = (9, 16, 3))#candidate|5477|(9, 16, 3)|var|uint32
var_5478 = relay.var("var_5478", dtype = "bool", shape = (40,))#candidate|5478|(40,)|var|bool
call_5475 = func_5474_call(var_5476,var_5477,var_5478,)
output = call_5475
func_5479 = relay.Function([var_5476,var_5477,var_5478,], output)
mutated_mod['func_5479'] = func_5479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1293_call = mutated_mod.get_global_var('func_1293')
call_5503 = relay.TupleGetItem(func_1291_call(), 0)
call_5504 = relay.TupleGetItem(func_1293_call(), 0)
output = relay.Tuple([call_5503,])
output2 = relay.Tuple([call_5504,])
func_5516 = relay.Function([], output)
mod['func_5516'] = func_5516
mod = relay.transform.InferType()(mod)
output = func_5516()
func_5517 = relay.Function([], output)
mutated_mod['func_5517'] = func_5517
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5590 = relay.var("var_5590", dtype = "float32", shape = (12, 15, 14))#candidate|5590|(12, 15, 14)|var|float32
uop_5591 = relay.sin(var_5590.astype('float32')) # shape=(12, 15, 14)
output = relay.Tuple([uop_5591,])
output2 = relay.Tuple([uop_5591,])
func_5598 = relay.Function([var_5590,], output)
mod['func_5598'] = func_5598
mod = relay.transform.InferType()(mod)
var_5599 = relay.var("var_5599", dtype = "float32", shape = (12, 15, 14))#candidate|5599|(12, 15, 14)|var|float32
output = func_5598(var_5599)
func_5600 = relay.Function([var_5599], output)
mutated_mod['func_5600'] = func_5600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_5602 = relay.TupleGetItem(func_296_call(), 0)
call_5603 = relay.TupleGetItem(func_298_call(), 0)
output = call_5602
output2 = call_5603
func_5604 = relay.Function([], output)
mod['func_5604'] = func_5604
mod = relay.transform.InferType()(mod)
output = func_5604()
func_5605 = relay.Function([], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2393_call = mod.get_global_var('func_2393')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_5611 = relay.TupleGetItem(func_2393_call(), 2)
call_5612 = relay.TupleGetItem(func_2395_call(), 2)
output = relay.Tuple([call_5611,])
output2 = relay.Tuple([call_5612,])
func_5639 = relay.Function([], output)
mod['func_5639'] = func_5639
mod = relay.transform.InferType()(mod)
output = func_5639()
func_5640 = relay.Function([], output)
mutated_mod['func_5640'] = func_5640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2730_call = mod.get_global_var('func_2730')
func_2731_call = mutated_mod.get_global_var('func_2731')
call_5651 = relay.TupleGetItem(func_2730_call(), 1)
call_5652 = relay.TupleGetItem(func_2731_call(), 1)
output = call_5651
output2 = call_5652
func_5661 = relay.Function([], output)
mod['func_5661'] = func_5661
mod = relay.transform.InferType()(mod)
mutated_mod['func_5661'] = func_5661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5661_call = mutated_mod.get_global_var('func_5661')
call_5662 = func_5661_call()
output = call_5662
func_5663 = relay.Function([], output)
mutated_mod['func_5663'] = func_5663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2542_call = mod.get_global_var('func_2542')
func_2543_call = mutated_mod.get_global_var('func_2543')
call_5691 = relay.TupleGetItem(func_2542_call(), 3)
call_5692 = relay.TupleGetItem(func_2543_call(), 3)
func_791_call = mod.get_global_var('func_791')
func_793_call = mutated_mod.get_global_var('func_793')
const_5701 = relay.const([8.235930,-6.784242,8.007625,-5.967164,0.977368,4.045626,-0.614976,-8.105740,-1.184916,3.099558,8.913372,-0.634301,-0.191139,4.831233,-4.856497,3.223451,4.134394,-5.604385,9.854584,1.440919,5.109329,7.185898,0.524845,8.342780,-2.307248,-6.753531,-2.701301,-1.816281,0.025828,-9.944888,4.963031,2.229634,8.528810,7.089487,-6.103221,-8.486974,3.770517,7.683320,5.665130,-1.054242,-3.833695,0.312256,-5.740131,3.519701,0.618916,3.814468,6.112486,8.713698,-3.814327,-7.502777,1.227180,-0.676704,-0.742815,4.525234,9.163903,-2.673616,-1.298956,-8.449973,7.786935,-1.134462,3.787670,5.168124,-3.405849,-8.512462,3.770227,1.546225,6.035623,0.474340,-5.742834,8.863212,9.403491,4.978439,-5.714646,-6.787079,2.671441,-6.265798,-3.662052,0.639918,1.001859,5.724555,-6.587765,2.015542,4.524083,-8.463415,-1.133675,8.989370,2.551719,2.088863,-9.237862,4.116177,4.621030,-2.077964,-0.590631,-2.567288,9.391612,-4.289681,7.970460,5.498066,1.259774,-4.366686,-9.004258,4.571098,-1.527080,6.817810,-3.176344,-5.751198,-1.252143,3.302844,-4.967314,-4.338769,4.634415,-8.906416,8.863217,1.930648,2.824892,-3.852146,2.780972,7.133461,-2.597772,-2.414768,0.082608,-7.157174,-9.050274,-7.766112,-5.937179,-9.265349,-2.487384,-6.860485,9.970544,-5.839340,7.365170,-8.030187,-3.277240,-9.711614,-8.487870,3.995532,3.967319,1.359531,2.788434,-6.394293,1.858335,5.079152,0.783772,5.058281,-8.830983,0.489887,-4.892140,-9.801625,5.298294,2.147551,-9.066810,-0.273254,1.626879,7.129645,8.489496,-8.213684,-2.699888,-7.153580,1.534502,-2.954816,6.451450,0.506970,6.367946,-0.160519,-7.994584,-9.858140,-6.178236,-1.496507,5.439369,-6.872778,0.410271,7.975905,4.186008,-5.691273,3.287798,-4.099446,-4.889789,-3.593496,6.153498,3.315454,-2.944293,-6.092315,-8.007990,-9.084171,-8.037902,-6.967688,8.721814,-4.235468,-5.377684,3.768776,2.542144,-7.646294,2.016384,-5.997133,-2.940926,-8.426352,9.239977,8.009347,8.846802,1.247501,6.791865,-1.427293,5.455116,2.787892,4.674898,6.416764,-4.598520,-5.412685,-4.042126,-3.269187,-4.562957,-2.847173,-5.500679,5.868502,8.796282,4.898142,2.621337,-0.724098,-3.136212,-7.328822,-8.886611,3.354391,0.144981,1.777545,-1.760755,-8.145797,-9.150147,-6.789492,5.706119,3.356285,1.942782,1.217797,-9.954871,6.883076,1.414907,-0.696653,-1.176187,-2.120521,1.394702,5.399837,3.613119,5.619676,-9.626780,-9.821371,8.508327,9.933037,1.673238,0.075983,-7.735973,-7.225737,-8.333889,0.252504,-1.929595,0.215067,7.087660,6.834542,-6.743343,8.341023,0.617302,-7.744134,8.897582,9.948692,-8.894609,-3.641152,6.074335,-5.645407,6.674213,-8.001593,6.760122,9.709961,1.596279,-9.555693,1.930387,-3.814359,5.269715,-9.547994,-7.506868,4.005476,-2.326624,0.377121,2.777183,-8.127100,-3.343886,-1.880258,-4.767846,-3.489610,5.619496,0.303657,-1.203956,3.441495,1.775530,-3.153427,8.909365,-7.051809,8.272035,5.129099,-7.443096,1.162309,3.135052,-3.795386,-1.558339,2.890661,4.039387,-1.336593,-3.302751,-9.143332,2.932875,-6.101116,-0.364572,0.942730,-6.084822,-9.809964,-0.576526,9.996626,-1.534469,8.353994,3.398369,-0.256211,4.696635,-3.370103,-0.410392,9.948322,-4.711948,-5.147822,0.361452,-2.013704,-3.835066,-3.378787,0.738948,-9.425568,4.128401,-4.953285,-4.181362,-4.027718,7.406634,-9.137926,7.299378,-4.069773,0.952906,-9.457160,-6.568870,-7.933146,-2.805359,5.540325,6.809906,6.087767,6.551229,0.227714,-0.458393,9.275095,-3.100654,6.061822,-0.697317,8.591893,-2.478319,-9.646050,6.962252,2.321297,0.333576,2.914578,3.637553,3.068443,-2.014969,-0.773509,-5.984515,-0.624020,3.430364,-5.687836,4.301241,1.023062,-9.253970,-8.556879,7.591485,1.861847,-9.413796,6.141625,4.590426,-5.496052,0.815539,-6.151073,3.004321,-9.539345,-8.756167,-2.873119,1.502964,4.077658,2.717600,5.088839,8.280610,6.589220], dtype = "float32")#candidate|5701|(390,)|const|float32
call_5700 = relay.TupleGetItem(func_791_call(relay.reshape(const_5701.astype('float32'), [13, 5, 6])), 1)
call_5702 = relay.TupleGetItem(func_793_call(relay.reshape(const_5701.astype('float32'), [13, 5, 6])), 1)
uop_5713 = relay.erf(call_5700.astype('float32')) # shape=(13, 5, 6)
uop_5715 = relay.erf(call_5702.astype('float32')) # shape=(13, 5, 6)
func_1869_call = mod.get_global_var('func_1869')
func_1870_call = mutated_mod.get_global_var('func_1870')
call_5727 = func_1869_call()
call_5728 = func_1869_call()
bop_5734 = relay.bitwise_or(uop_5713.astype('uint16'), relay.reshape(const_5701.astype('uint16'), relay.shape_of(uop_5713))) # shape=(13, 5, 6)
bop_5737 = relay.bitwise_or(uop_5715.astype('uint16'), relay.reshape(const_5701.astype('uint16'), relay.shape_of(uop_5715))) # shape=(13, 5, 6)
uop_5738 = relay.exp(uop_5713.astype('float64')) # shape=(13, 5, 6)
uop_5740 = relay.exp(uop_5715.astype('float64')) # shape=(13, 5, 6)
output = relay.Tuple([call_5691,call_5727,bop_5734,uop_5738,])
output2 = relay.Tuple([call_5692,call_5728,bop_5737,uop_5740,])
func_5742 = relay.Function([], output)
mod['func_5742'] = func_5742
mod = relay.transform.InferType()(mod)
mutated_mod['func_5742'] = func_5742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5742_call = mutated_mod.get_global_var('func_5742')
call_5743 = func_5742_call()
output = call_5743
func_5744 = relay.Function([], output)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_539_call = mutated_mod.get_global_var('func_539')
call_5758 = relay.TupleGetItem(func_537_call(), 0)
call_5759 = relay.TupleGetItem(func_539_call(), 0)
output = call_5758
output2 = call_5759
func_5762 = relay.Function([], output)
mod['func_5762'] = func_5762
mod = relay.transform.InferType()(mod)
output = func_5762()
func_5763 = relay.Function([], output)
mutated_mod['func_5763'] = func_5763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_5764 = func_2808_call()
call_5765 = func_2808_call()
func_5762_call = mod.get_global_var('func_5762')
func_5763_call = mutated_mod.get_global_var('func_5763')
call_5814 = func_5762_call()
call_5815 = func_5762_call()
func_1557_call = mod.get_global_var('func_1557')
func_1560_call = mutated_mod.get_global_var('func_1560')
var_5822 = relay.var("var_5822", dtype = "uint64", shape = (1960,))#candidate|5822|(1960,)|var|uint64
call_5821 = relay.TupleGetItem(func_1557_call(relay.reshape(var_5822.astype('uint64'), [10, 14, 14]), relay.reshape(var_5822.astype('uint64'), [10, 14, 14]), ), 0)
call_5823 = relay.TupleGetItem(func_1560_call(relay.reshape(var_5822.astype('uint64'), [10, 14, 14]), relay.reshape(var_5822.astype('uint64'), [10, 14, 14]), ), 0)
uop_5828 = relay.atan(var_5822.astype('float32')) # shape=(1960,)
bop_5831 = relay.bitwise_xor(uop_5828.astype('uint32'), relay.reshape(call_5821.astype('uint32'), relay.shape_of(uop_5828))) # shape=(1960,)
bop_5834 = relay.bitwise_xor(uop_5828.astype('uint32'), relay.reshape(call_5823.astype('uint32'), relay.shape_of(uop_5828))) # shape=(1960,)
func_4939_call = mod.get_global_var('func_4939')
func_4941_call = mutated_mod.get_global_var('func_4941')
call_5851 = relay.TupleGetItem(func_4939_call(), 0)
call_5852 = relay.TupleGetItem(func_4941_call(), 0)
uop_5854 = relay.log2(uop_5828.astype('float64')) # shape=(1960,)
output = relay.Tuple([call_5764,call_5814,bop_5831,call_5851,uop_5854,])
output2 = relay.Tuple([call_5765,call_5815,bop_5834,call_5852,uop_5854,])
func_5867 = relay.Function([var_5822,], output)
mod['func_5867'] = func_5867
mod = relay.transform.InferType()(mod)
var_5868 = relay.var("var_5868", dtype = "uint64", shape = (1960,))#candidate|5868|(1960,)|var|uint64
output = func_5867(var_5868)
func_5869 = relay.Function([var_5868], output)
mutated_mod['func_5869'] = func_5869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5918 = relay.var("var_5918", dtype = "float32", shape = (4, 3, 9))#candidate|5918|(4, 3, 9)|var|float32
uop_5919 = relay.log(var_5918.astype('float32')) # shape=(4, 3, 9)
bop_5922 = relay.bitwise_xor(uop_5919.astype('int8'), relay.reshape(var_5918.astype('int8'), relay.shape_of(uop_5919))) # shape=(4, 3, 9)
uop_5928 = relay.cosh(var_5918.astype('float32')) # shape=(4, 3, 9)
func_3328_call = mod.get_global_var('func_3328')
func_3331_call = mutated_mod.get_global_var('func_3331')
const_5948 = relay.const([5.182736,3.522795,2.878560,-5.521159,3.130393,7.691297,1.599599,0.240461,-2.312791,-7.746387], dtype = "float32")#candidate|5948|(10,)|const|float32
call_5947 = relay.TupleGetItem(func_3328_call(relay.reshape(const_5948.astype('float32'), [2, 5, 1])), 0)
call_5949 = relay.TupleGetItem(func_3331_call(relay.reshape(const_5948.astype('float32'), [2, 5, 1])), 0)
bop_5950 = relay.equal(uop_5919.astype('bool'), relay.reshape(bop_5922.astype('bool'), relay.shape_of(uop_5919))) # shape=(4, 3, 9)
func_5639_call = mod.get_global_var('func_5639')
func_5640_call = mutated_mod.get_global_var('func_5640')
call_5954 = relay.TupleGetItem(func_5639_call(), 0)
call_5955 = relay.TupleGetItem(func_5640_call(), 0)
func_839_call = mod.get_global_var('func_839')
func_840_call = mutated_mod.get_global_var('func_840')
call_5958 = relay.TupleGetItem(func_839_call(), 0)
call_5959 = relay.TupleGetItem(func_840_call(), 0)
output = relay.Tuple([uop_5928,call_5947,const_5948,bop_5950,call_5954,call_5958,])
output2 = relay.Tuple([uop_5928,call_5949,const_5948,bop_5950,call_5955,call_5959,])
func_5966 = relay.Function([var_5918,], output)
mod['func_5966'] = func_5966
mod = relay.transform.InferType()(mod)
mutated_mod['func_5966'] = func_5966
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5967 = relay.var("var_5967", dtype = "float32", shape = (4, 3, 9))#candidate|5967|(4, 3, 9)|var|float32
func_5966_call = mutated_mod.get_global_var('func_5966')
call_5968 = func_5966_call(var_5967)
output = call_5968
func_5969 = relay.Function([var_5967], output)
mutated_mod['func_5969'] = func_5969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_5977 = func_3161_call()
call_5978 = func_3161_call()
output = call_5977
output2 = call_5978
func_5981 = relay.Function([], output)
mod['func_5981'] = func_5981
mod = relay.transform.InferType()(mod)
mutated_mod['func_5981'] = func_5981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5981_call = mutated_mod.get_global_var('func_5981')
call_5982 = func_5981_call()
output = call_5982
func_5983 = relay.Function([], output)
mutated_mod['func_5983'] = func_5983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_6013 = relay.TupleGetItem(func_1272_call(), 0)
call_6014 = relay.TupleGetItem(func_1273_call(), 0)
output = relay.Tuple([call_6013,])
output2 = relay.Tuple([call_6014,])
func_6017 = relay.Function([], output)
mod['func_6017'] = func_6017
mod = relay.transform.InferType()(mod)
output = func_6017()
func_6018 = relay.Function([], output)
mutated_mod['func_6018'] = func_6018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3336_call = mod.get_global_var('func_3336')
func_3337_call = mutated_mod.get_global_var('func_3337')
call_6036 = func_3336_call()
call_6037 = func_3336_call()
output = relay.Tuple([call_6036,])
output2 = relay.Tuple([call_6037,])
func_6043 = relay.Function([], output)
mod['func_6043'] = func_6043
mod = relay.transform.InferType()(mod)
mutated_mod['func_6043'] = func_6043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6043_call = mutated_mod.get_global_var('func_6043')
call_6044 = func_6043_call()
output = call_6044
func_6045 = relay.Function([], output)
mutated_mod['func_6045'] = func_6045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_6104 = relay.TupleGetItem(func_2421_call(), 0)
call_6105 = relay.TupleGetItem(func_2422_call(), 0)
output = relay.Tuple([call_6104,])
output2 = relay.Tuple([call_6105,])
func_6108 = relay.Function([], output)
mod['func_6108'] = func_6108
mod = relay.transform.InferType()(mod)
output = func_6108()
func_6109 = relay.Function([], output)
mutated_mod['func_6109'] = func_6109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2448_call = mod.get_global_var('func_2448')
func_2450_call = mutated_mod.get_global_var('func_2450')
call_6130 = func_2448_call()
call_6131 = func_2448_call()
output = call_6130
output2 = call_6131
func_6144 = relay.Function([], output)
mod['func_6144'] = func_6144
mod = relay.transform.InferType()(mod)
mutated_mod['func_6144'] = func_6144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6144_call = mutated_mod.get_global_var('func_6144')
call_6145 = func_6144_call()
output = call_6145
func_6146 = relay.Function([], output)
mutated_mod['func_6146'] = func_6146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_6147 = relay.TupleGetItem(func_1272_call(), 0)
call_6148 = relay.TupleGetItem(func_1273_call(), 0)
output = relay.Tuple([call_6147,])
output2 = relay.Tuple([call_6148,])
func_6163 = relay.Function([], output)
mod['func_6163'] = func_6163
mod = relay.transform.InferType()(mod)
output = func_6163()
func_6164 = relay.Function([], output)
mutated_mod['func_6164'] = func_6164
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6170 = relay.const([[5.532472],[0.415030],[-9.793331],[-9.801376],[-9.758086],[-7.580751],[-6.407233],[-7.181776],[5.504371]], dtype = "float32")#candidate|6170|(9, 1)|const|float32
uop_6171 = relay.sigmoid(const_6170.astype('float32')) # shape=(9, 1)
bop_6180 = relay.less_equal(uop_6171.astype('bool'), relay.reshape(const_6170.astype('bool'), relay.shape_of(uop_6171))) # shape=(9, 1)
output = bop_6180
output2 = bop_6180
func_6197 = relay.Function([], output)
mod['func_6197'] = func_6197
mod = relay.transform.InferType()(mod)
output = func_6197()
func_6198 = relay.Function([], output)
mutated_mod['func_6198'] = func_6198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4391_call = mod.get_global_var('func_4391')
func_4393_call = mutated_mod.get_global_var('func_4393')
call_6228 = relay.TupleGetItem(func_4391_call(), 1)
call_6229 = relay.TupleGetItem(func_4393_call(), 1)
output = relay.Tuple([call_6228,])
output2 = relay.Tuple([call_6229,])
func_6230 = relay.Function([], output)
mod['func_6230'] = func_6230
mod = relay.transform.InferType()(mod)
mutated_mod['func_6230'] = func_6230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6230_call = mutated_mod.get_global_var('func_6230')
call_6231 = func_6230_call()
output = call_6231
func_6232 = relay.Function([], output)
mutated_mod['func_6232'] = func_6232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_6298 = relay.TupleGetItem(func_2403_call(), 0)
call_6299 = relay.TupleGetItem(func_2405_call(), 0)
output = call_6298
output2 = call_6299
func_6306 = relay.Function([], output)
mod['func_6306'] = func_6306
mod = relay.transform.InferType()(mod)
output = func_6306()
func_6307 = relay.Function([], output)
mutated_mod['func_6307'] = func_6307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4391_call = mod.get_global_var('func_4391')
func_4393_call = mutated_mod.get_global_var('func_4393')
call_6355 = relay.TupleGetItem(func_4391_call(), 0)
call_6356 = relay.TupleGetItem(func_4393_call(), 0)
func_1616_call = mod.get_global_var('func_1616')
func_1617_call = mutated_mod.get_global_var('func_1617')
call_6375 = relay.TupleGetItem(func_1616_call(), 2)
call_6376 = relay.TupleGetItem(func_1617_call(), 2)
var_6389 = relay.var("var_6389", dtype = "float32", shape = (12, 13, 6))#candidate|6389|(12, 13, 6)|var|float32
bop_6390 = relay.add(call_6355.astype('float32'), relay.reshape(var_6389.astype('float32'), relay.shape_of(call_6355))) # shape=(12, 13, 6)
bop_6393 = relay.add(call_6356.astype('float32'), relay.reshape(var_6389.astype('float32'), relay.shape_of(call_6356))) # shape=(12, 13, 6)
output = relay.Tuple([call_6375,bop_6390,])
output2 = relay.Tuple([call_6376,bop_6393,])
func_6412 = relay.Function([var_6389,], output)
mod['func_6412'] = func_6412
mod = relay.transform.InferType()(mod)
var_6413 = relay.var("var_6413", dtype = "float32", shape = (12, 13, 6))#candidate|6413|(12, 13, 6)|var|float32
output = func_6412(var_6413)
func_6414 = relay.Function([var_6413], output)
mutated_mod['func_6414'] = func_6414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3700_call = mod.get_global_var('func_3700')
func_3701_call = mutated_mod.get_global_var('func_3701')
call_6423 = relay.TupleGetItem(func_3700_call(), 0)
call_6424 = relay.TupleGetItem(func_3701_call(), 0)
func_1427_call = mod.get_global_var('func_1427')
func_1430_call = mutated_mod.get_global_var('func_1430')
const_6450 = relay.const(4.077225, dtype = "float64")#candidate|6450|()|const|float64
var_6451 = relay.var("var_6451", dtype = "bool", shape = (40,))#candidate|6451|(40,)|var|bool
call_6449 = relay.TupleGetItem(func_1427_call(relay.reshape(const_6450.astype('float64'), []), relay.reshape(var_6451.astype('bool'), [40,]), ), 1)
call_6452 = relay.TupleGetItem(func_1430_call(relay.reshape(const_6450.astype('float64'), []), relay.reshape(var_6451.astype('bool'), [40,]), ), 1)
output = relay.Tuple([call_6423,call_6449,const_6450,var_6451,])
output2 = relay.Tuple([call_6424,call_6452,const_6450,var_6451,])
func_6462 = relay.Function([var_6451,], output)
mod['func_6462'] = func_6462
mod = relay.transform.InferType()(mod)
var_6463 = relay.var("var_6463", dtype = "bool", shape = (40,))#candidate|6463|(40,)|var|bool
output = func_6462(var_6463)
func_6464 = relay.Function([var_6463], output)
mutated_mod['func_6464'] = func_6464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4274_call = mod.get_global_var('func_4274')
func_4275_call = mutated_mod.get_global_var('func_4275')
call_6474 = func_4274_call()
call_6475 = func_4274_call()
output = call_6474
output2 = call_6475
func_6481 = relay.Function([], output)
mod['func_6481'] = func_6481
mod = relay.transform.InferType()(mod)
mutated_mod['func_6481'] = func_6481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6481_call = mutated_mod.get_global_var('func_6481')
call_6482 = func_6481_call()
output = call_6482
func_6483 = relay.Function([], output)
mutated_mod['func_6483'] = func_6483
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6484 = relay.var("var_6484", dtype = "float64", shape = (8, 8, 6))#candidate|6484|(8, 8, 6)|var|float64
uop_6485 = relay.exp(var_6484.astype('float64')) # shape=(8, 8, 6)
func_5981_call = mod.get_global_var('func_5981')
func_5983_call = mutated_mod.get_global_var('func_5983')
call_6500 = func_5981_call()
call_6501 = func_5981_call()
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_6502 = relay.TupleGetItem(func_1571_call(), 0)
call_6503 = relay.TupleGetItem(func_1573_call(), 0)
output = relay.Tuple([uop_6485,call_6500,call_6502,])
output2 = relay.Tuple([uop_6485,call_6501,call_6503,])
func_6508 = relay.Function([var_6484,], output)
mod['func_6508'] = func_6508
mod = relay.transform.InferType()(mod)
mutated_mod['func_6508'] = func_6508
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6509 = relay.var("var_6509", dtype = "float64", shape = (8, 8, 6))#candidate|6509|(8, 8, 6)|var|float64
func_6508_call = mutated_mod.get_global_var('func_6508')
call_6510 = func_6508_call(var_6509)
output = call_6510
func_6511 = relay.Function([var_6509], output)
mutated_mod['func_6511'] = func_6511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6197_call = mod.get_global_var('func_6197')
func_6198_call = mutated_mod.get_global_var('func_6198')
call_6529 = func_6197_call()
call_6530 = func_6197_call()
func_2303_call = mod.get_global_var('func_2303')
func_2304_call = mutated_mod.get_global_var('func_2304')
call_6533 = relay.TupleGetItem(func_2303_call(), 0)
call_6534 = relay.TupleGetItem(func_2304_call(), 0)
output = relay.Tuple([call_6529,call_6533,])
output2 = relay.Tuple([call_6530,call_6534,])
func_6555 = relay.Function([], output)
mod['func_6555'] = func_6555
mod = relay.transform.InferType()(mod)
mutated_mod['func_6555'] = func_6555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6555_call = mutated_mod.get_global_var('func_6555')
call_6556 = func_6555_call()
output = call_6556
func_6557 = relay.Function([], output)
mutated_mod['func_6557'] = func_6557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3965_call = mod.get_global_var('func_3965')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_6572 = func_3965_call()
call_6573 = func_3965_call()
output = relay.Tuple([call_6572,])
output2 = relay.Tuple([call_6573,])
func_6595 = relay.Function([], output)
mod['func_6595'] = func_6595
mod = relay.transform.InferType()(mod)
mutated_mod['func_6595'] = func_6595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6595_call = mutated_mod.get_global_var('func_6595')
call_6596 = func_6595_call()
output = call_6596
func_6597 = relay.Function([], output)
mutated_mod['func_6597'] = func_6597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1160_call = mod.get_global_var('func_1160')
func_1161_call = mutated_mod.get_global_var('func_1161')
call_6619 = relay.TupleGetItem(func_1160_call(), 0)
call_6620 = relay.TupleGetItem(func_1161_call(), 0)
func_67_call = mod.get_global_var('func_67')
func_69_call = mutated_mod.get_global_var('func_69')
const_6641 = relay.const([3.682525,4.724288,-3.061991,1.152944,4.059926,-5.101889,-4.472664,-6.360905,8.561612,-9.518743,-9.801096,-2.681692,-1.148459,8.953061,-9.992366,6.398573,-9.256516,7.853272,8.612463,6.063310,9.063061,-1.055836,9.683759,6.675341,5.710054,-2.599370,-7.826747,-3.732966,-0.146434,8.705987,9.632316,2.029361,3.230370,-3.598584,8.507366,4.956500,7.869212,-7.783826,-7.705097,8.906496,9.855031,4.045560,5.854521,-1.233184,-0.126276,-1.615742,-1.518965,0.322682,-3.836769,1.519065], dtype = "float64")#candidate|6641|(50,)|const|float64
call_6640 = relay.TupleGetItem(func_67_call(relay.reshape(const_6641.astype('float64'), [2, 5, 5])), 0)
call_6642 = relay.TupleGetItem(func_69_call(relay.reshape(const_6641.astype('float64'), [2, 5, 5])), 0)
uop_6660 = relay.log(call_6640.astype('float32')) # shape=(2, 5, 5)
uop_6662 = relay.log(call_6642.astype('float32')) # shape=(2, 5, 5)
func_1291_call = mod.get_global_var('func_1291')
func_1293_call = mutated_mod.get_global_var('func_1293')
call_6672 = relay.TupleGetItem(func_1291_call(), 0)
call_6673 = relay.TupleGetItem(func_1293_call(), 0)
output = relay.Tuple([call_6619,const_6641,uop_6660,call_6672,])
output2 = relay.Tuple([call_6620,const_6641,uop_6662,call_6673,])
func_6683 = relay.Function([], output)
mod['func_6683'] = func_6683
mod = relay.transform.InferType()(mod)
mutated_mod['func_6683'] = func_6683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6683_call = mutated_mod.get_global_var('func_6683')
call_6684 = func_6683_call()
output = call_6684
func_6685 = relay.Function([], output)
mutated_mod['func_6685'] = func_6685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5762_call = mod.get_global_var('func_5762')
func_5763_call = mutated_mod.get_global_var('func_5763')
call_6692 = func_5762_call()
call_6693 = func_5762_call()
func_3328_call = mod.get_global_var('func_3328')
func_3331_call = mutated_mod.get_global_var('func_3331')
var_6698 = relay.var("var_6698", dtype = "float32", shape = (10,))#candidate|6698|(10,)|var|float32
call_6697 = relay.TupleGetItem(func_3328_call(relay.reshape(var_6698.astype('float32'), [2, 5, 1])), 1)
call_6699 = relay.TupleGetItem(func_3331_call(relay.reshape(var_6698.astype('float32'), [2, 5, 1])), 1)
func_4511_call = mod.get_global_var('func_4511')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_6707 = func_4511_call()
call_6708 = func_4511_call()
output = relay.Tuple([call_6692,call_6697,var_6698,call_6707,])
output2 = relay.Tuple([call_6693,call_6699,var_6698,call_6708,])
func_6712 = relay.Function([var_6698,], output)
mod['func_6712'] = func_6712
mod = relay.transform.InferType()(mod)
mutated_mod['func_6712'] = func_6712
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6713 = relay.var("var_6713", dtype = "float32", shape = (10,))#candidate|6713|(10,)|var|float32
func_6712_call = mutated_mod.get_global_var('func_6712')
call_6714 = func_6712_call(var_6713)
output = call_6714
func_6715 = relay.Function([var_6713], output)
mutated_mod['func_6715'] = func_6715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3637_call = mod.get_global_var('func_3637')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_6717 = relay.TupleGetItem(func_3637_call(), 0)
call_6718 = relay.TupleGetItem(func_3639_call(), 0)
func_4939_call = mod.get_global_var('func_4939')
func_4941_call = mutated_mod.get_global_var('func_4941')
call_6767 = relay.TupleGetItem(func_4939_call(), 1)
call_6768 = relay.TupleGetItem(func_4941_call(), 1)
output = relay.Tuple([call_6717,call_6767,])
output2 = relay.Tuple([call_6718,call_6768,])
func_6775 = relay.Function([], output)
mod['func_6775'] = func_6775
mod = relay.transform.InferType()(mod)
output = func_6775()
func_6776 = relay.Function([], output)
mutated_mod['func_6776'] = func_6776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_6824 = func_3161_call()
call_6825 = func_3161_call()
func_1272_call = mod.get_global_var('func_1272')
func_1273_call = mutated_mod.get_global_var('func_1273')
call_6830 = relay.TupleGetItem(func_1272_call(), 0)
call_6831 = relay.TupleGetItem(func_1273_call(), 0)
uop_6855 = relay.asin(call_6830.astype('float32')) # shape=(12, 13, 6)
uop_6857 = relay.asin(call_6831.astype('float32')) # shape=(12, 13, 6)
func_5598_call = mod.get_global_var('func_5598')
func_5600_call = mutated_mod.get_global_var('func_5600')
var_6869 = relay.var("var_6869", dtype = "float32", shape = (2520,))#candidate|6869|(2520,)|var|float32
call_6868 = relay.TupleGetItem(func_5598_call(relay.reshape(var_6869.astype('float32'), [12, 15, 14])), 0)
call_6870 = relay.TupleGetItem(func_5600_call(relay.reshape(var_6869.astype('float32'), [12, 15, 14])), 0)
func_1557_call = mod.get_global_var('func_1557')
func_1560_call = mutated_mod.get_global_var('func_1560')
const_6874 = relay.const([-7,4,8,3,9,-2,6,-2,-8,4,10,-1,-6,-8,-9,1,-7,-9,8,-4,3,5,-3,6,8,1,9,-10,6,-2,-4,-8,9,5,-1,-4,3,6,8,7,3,-6,9,7,-4,2,-3,-9,10,-8,3,9,-1,3,-8,7,-10,4,-1,-7,-10,-2,-9,-3,-5,4,-5,5,10,7,-8,-9,-9,8,-2,6,-5,-4,9,7,-8,-3,4,9,6,1,-2,2,1,-5,8,6,-8,-8,-6,3,6,9,4,3,7,3,4,3,7,2,-9,-9,-9,-6,-3,-10,-6,8,-10,1,-9,-7,2,-2,-9,-4,-3,5,-1,-6,1,3,7,-9,-6,-4,-5,-8,10,5,4,-8,-4,8,6,-10,-2,-4,6,-7,4,-5,-10,-5,3,-2,1,6,2,3,-8,5,-7,10,-2,4,-8,-4,-2,-1,-1,3,-4,1,3,-6,-8,2,1,9,-10,-9,1,-7,4,-9,-2,9,5,1,-6,10,7,-9,5,4,-10,2,-8,-4,8,9,10,-3,2,3,-3,9,-5,8,6,-5,-7,-8,5,-9,-9,-10,-10,6,-9,7,-1,1,7,-8,-3,1,-8,-5,5,6,4,-5,-1,6,9,3,2,-8,7,-3,-6,2,-7,9,-3,-6,-2,-3,3,4,-5,-1,-5,5,2,-4,-6,4,-5,5,-7,7,3,2,-1,7,-7,2,-9,4,9,-2,6,8,1,1,4,9,10,-5,-10,-9,-3,9,-2,-3,-4,-5,3,4,-7,-3,-5,-10,4,9,10,-10,-1,-4,3,5,4,-10,3,10,8,-3,-4,9,-10,1,-6,-4,-2,-1,8,2,6,-1,-5,1,4,6,10,-7,4,2,-9,-9,7,-5,6,8,-1,-2,-8,10,8,-2,-5,-9,-7,1,9,8,-1,-10,-2,8,-7,-2,5,9,-1,-2,-9,5,5,-3,-7,-10,-6,7,1,3,-8,-3,8,6,4,-6,-2,1,9,2,5,-8,2,-8,3,-1,8,-3,7,-8,1,3,6,-3,-8,-3,-4,-1,-6,-1,2,-9,-5,7,-4,-2,8,10,-9,-7,7,7,2,-10,-9,-7,-1,1,1,-8,10,1,5,-2,-6,9,-10,5,-6,-10,5,6,-4,-2,5,-9,9,-5,-3,9,5,-1,6,-6,-2,-9,-6,3,-2,-4,-4,-3,4,9,2,-7,6,1,7,-6,6,5,10,1,-2,10,9,-1,1,4,-8,2,2,-7,3,-7,-9,-8,-8,-3,-5,6,-8,8,-9,-7,-3,2,-4,-4,2,-5,-2,2,-3,10,-9,9,7,1,2,-2,6,-10,-3,-7,-4,4,5,-5,10,-4,4,-10,-3,-7,-6,-9,3,3,4,8,10,3,9,-4,5,-2,3,2,-3,-2,7,1,1,-5,4,2,-9,-1,-2,1,-5,8,5,4,8,6,7,7,-3,-4,10,-3,10,-9,-1,2,3,1,-10,7,3,5,-3,2,5,-5,2,3,-3,6,3,9,-10,8,-7,9,-2,-2,7,3,9,-8,-7,3,-5,6,-7,-6,3,-6,-2,-2,9,9,7,-9,-1,7,8,-10,9,1,-8,2,4,4,4,8,10,-3,-9,-3,-9,-8,8,-2,-3,4,1,-5,-5,10,-6,5,8,-3,10,9,4,-8,7,-1,2,-6,-1,-9,1,-6,-10,3,6,-6,1,6,7,10,-4,6,6,9,2,-4,7,-2,-8,6,-2,-2,2,-8,2,2,-9,-1,10,-2,10,-7,-3,-6,5,-7,-6,8,9,-6,-4,-8,-7,-9,1,-1,-5,-5,-9,-1,5,-9,-9,1,-7,-10,7,5,6,-3,3,-5,-4,1,5,8,-2,-3,8,-10,4,5,7,-5,3,-10,-6,9,9,-3,-3,-4,-2,5,-4,-4,-4,-10,-10,-6,5,-3,2,10,1,-6,8,9,-9,-7,-1,1,-1,-8,6,-6,-9,3,-9,5,-8,-6,10,-4,4,-2,-4,2,-6,6,4,4,-9,7,9,1,2,6,5,-1,-3,3,9,-5,-8,6,1,7,6,1,5,-5,-9,9,10,4,6,-3,5,-8,8,-6,2,2,-9,-5,5,1,10,-10,1,-8,-3,10,10,4,-1,-9,-4,-3,4,-7,-8,2,10,2,6,-8,2,9,-5,-10,-3,-9,9,-2,-10,1,7,7,3,-1,-9,10,-7,3,-3,-8,5,-5,-9,-7,-6,-6,2,-2,-3,6,10,-3,-6,-10,-3,-7,-6,-3,9,-6,10,8,5,7,-3,-10,-8,1,-1,-4,9,-3,6,-2,7,10,9,-1,1,10,10,8,-3,3,2,-10,-1,-8,10,1,-9,9,2,10,-6,5,2,-6,-4,1,-6,-9,-6,5,-6,-7,9,2,-4,3,5,-7,-3,2,-2,5,3,-9,8,5,8,10,-8,9,5,3,9,-4,5,-10,-8,8,-7,-8,-9,-1,-7,-6,-1,4,-4,5,8,-6,7,9,10,-5,-4,-4,-8,-2,5,-7,-3,-4,1,-2,1,2,-3,1,8,-2,1,-5,-10,5,5,4,4,-6,-9,3,-6,8,-6,3,-7,6,1,-8,-6,-8,4,8,-2,-4,-3,-9,-2,8,-5,1,8,-1,-9,-1,9,-8,1,-10,2,-4,-1,-4,1,2,-5,-10,-2,-1,8,-8,1,-2,3,5,-8,-2,3,3,-8,-10,9,5,10,2,9,-7,-5,-3,2,6,9,10,-6,4,9,-8,-3,-10,10,-3,2,-7,10,7,-10,-2,3,-10,7,2,7,6,4,5,6,2,9,-6,1,-10,8,-1,6,-1,-5,-10,-6,4,-2,1,8,-7,3,5,7,-7,9,-10,-7,-9,8,5,-8,2,-10,8,-8,-7,8,-7,7,-4,1,-1,-6,3,2,8,8,9,-4,-10,-2,3,8,5,-5,-2,-2,7,5,-4,7,-8,1,-5,-2,5,-1,-4,-10,4,9,-2,-9,10,6,-5,-5,9,10,-9,10,-6,6,-10,10,-4,10,-9,4,6,-3,-4,-4,4,-9,-6,-9,-2,4,-3,-7,-1,-2,7,2,-7,-4,5,6,-2,2,-5,-10,-10,-10,9,10,6,2,8,-7,-9,6,1,-3,6,-2,-10,8,9,3,-5,7,4,5,1,5,-4,-6,-2,1,8,-6,8,-8,-10,-2,-3,6,-6,9,4,-1,-6,7,-8,3,2,4,-3,-4,3,-10,4,-8,-9,-10,-3,-3,-8,5,7,-1,7,-8,6,-3,-7,-9,-9,3,-4,-2,4,5,4,-7,6,-1,-1,-3,-10,-10,-7,9,-8,5,5,-10,-3,-10,-3,-9,7,3,-8,7,-1,4,-7,-6,-5,-8,2,-1,1,1,10,-4,-9,-5,3,4,10,-4,1,4,4,-8,10,-9,-1,-6,4,10,-8,2,-8,7,-4,-6,2,-3,-2,3,10,-2,4,-4,7,-4,8,6,10,-3,-4,-1,9,-3,7,-10,7,10,9,2,7,-10,-9,2,-2,6,-5,4,-1,2,2,4,3,5,-9,9,2,-2,8,2,10,7,3,9,8,-3,-5,-2,-3,2,5,-8,1,-7,6,8,-7,5,-6,-5,8,-7,-5,3,7,7,-7,6,-7,-8,2,2,2,-9,-2,3,2,-2,8,-2,1,4,4,-7,-4,-3,2,8,-3,-2,-1,2,4,8,-9,6,10,7,3,5,10,6,5,6,10,10,5,-5,-8,-1,-5,-7,9,9,10,9,-1,-2,6,-2,-7,8,-6,1,7,-1,10,-7,3,-3,7,-5,-7,-5,-6,-1,-1,7,3,-3,1,-5,1,-2,-6,-9,8,-1,10,10,-5,1,10,-5,-5,5,2,6,10,2,-4,-8,5,-7,-7,3,8,10,-3,2,5,5,-7,-3,-3,-4,-5,9,-6,-7,5,-7,-5,10,-1,-9,2,-6,-6,-10,5,6,-8,10,-3,-9,6,-1,2,-2,-6,1,-4,8,5,9,-2,2,9,-8,-8,1,10,8,3,-4,10,6,-2,3,2,9,-4,8,2,8,-10,5,-10,1,-2,2,-2,-7,-5,-4,-2,-5,-4,2,6,8,-6,7,6,1,4,-4,-4,-3,-9,9,9,-10,4,3,-9,-7,3,-4,5,1,-9,-8,-3,-5,7,6,6,3,7,2,-6,-4,7,10,-1,1,-5,4,-9,2,3,-4,-5,10,10,9,-3,6,1,3,-6,-4,3,-9,-7,8,1,8,8,6,-10,-5,10,-6,-5,2,1,-4,-6,-7,-6,-4,9,-10,9,-5,3,-3,-9,-3,-6,-8,1,-3,5,-1,-7,7,-6,-2,-5,6,-5,10,-10,8,7,4,10,-6,-9,7,3,-3,10,-6,2,-2,10,3,-6,5,9,-3,9,3,6,8,-5,-8,8,-10,5,9,6,7,-3,5,-4,-10,-8,2,4,-3,1,-3,-7,-1,-7,-10,-2,-4,1,-4,6,7,6,7,-1,10,6,-3,6,-7,-4,-5,6,-9,9,-10,-7,10,-8,7,1,-3,1,-2,-8,10,-8,6,6,-8,1,1,-9,-3,-10,-8,8,-10,5,-5,-2,7,-2,3,10,-3,3,9,7,-9,-4,1,-8,10,2,-8,-2,6,8,2,-3,9,2,-8,-1,7,-5,9,9,9,-7,-8,2,5,-3,7,3,-2,3,-4,-6,-2,-9,-4,-2,-4,10,2,-5,-1,3,6,6,-10,5,-3,-7,10,8,6,7,-3,-1,-8,-9,7,-8,9,-9,3,3,7,-3,-7,2,-2,-3,-5,-7,3,3,9,4,-5,7,9,6,-1,2,1,-3,-3,8,-3,3,5,7,-9,-4,-6,-2,2,-10,8,-2,5,2,2,-8,-6,-2,-8,5,-1,-2,9,-1,-4,5,-2,1,-10,5,-4,8,5,1,2,1,-6,-10,10,7,2,-6,-6,-10,-1,-10,-2,-4,-10,-10,-2,6,7,4,-9,1,-10,-6,5,5,-2,10,-3,1,-1,8,4,-3,1,-8,6,-4,6,5,5,-9,4,1,6,-3,-4,10,4,-1,-1,-7,-8,-5,8,-8,-9,10,-4,1,6,7,-2,2,-10,-2,3,8,-10,-8,3,3,-10,-5,5,-6,-7,-3,-10,6,-9,3,-8,3,-3,8,4,-10,-4,9,-9,2,-8,7,-9,1,1,-10,-2,9,-2,3,-6,-2,-8,-2,8,4,-9,5,6,-8,10,6,-10,9], dtype = "uint64")#candidate|6874|(1960,)|const|uint64
call_6873 = relay.TupleGetItem(func_1557_call(relay.reshape(const_6874.astype('uint64'), [10, 14, 14]), relay.reshape(const_6874.astype('uint64'), [10, 14, 14]), ), 0)
call_6875 = relay.TupleGetItem(func_1560_call(relay.reshape(const_6874.astype('uint64'), [10, 14, 14]), relay.reshape(const_6874.astype('uint64'), [10, 14, 14]), ), 0)
output = relay.Tuple([call_6824,uop_6855,call_6868,var_6869,call_6873,const_6874,])
output2 = relay.Tuple([call_6825,uop_6857,call_6870,var_6869,call_6875,const_6874,])
func_6896 = relay.Function([var_6869,], output)
mod['func_6896'] = func_6896
mod = relay.transform.InferType()(mod)
var_6897 = relay.var("var_6897", dtype = "float32", shape = (2520,))#candidate|6897|(2520,)|var|float32
output = func_6896(var_6897)
func_6898 = relay.Function([var_6897], output)
mutated_mod['func_6898'] = func_6898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7053 = relay.var("var_7053", dtype = "int8", shape = (16, 9, 16))#candidate|7053|(16, 9, 16)|var|int8
var_7054 = relay.var("var_7054", dtype = "int8", shape = (16, 9, 16))#candidate|7054|(16, 9, 16)|var|int8
bop_7055 = relay.less_equal(var_7053.astype('bool'), relay.reshape(var_7054.astype('bool'), relay.shape_of(var_7053))) # shape=(16, 9, 16)
var_7060 = relay.var("var_7060", dtype = "int8", shape = (16, 9, 16))#candidate|7060|(16, 9, 16)|var|int8
bop_7061 = relay.multiply(var_7053.astype('uint32'), relay.reshape(var_7060.astype('uint32'), relay.shape_of(var_7053))) # shape=(16, 9, 16)
uop_7070 = relay.sigmoid(bop_7055.astype('float32')) # shape=(16, 9, 16)
output = relay.Tuple([bop_7061,uop_7070,])
output2 = relay.Tuple([bop_7061,uop_7070,])
func_7075 = relay.Function([var_7053,var_7054,var_7060,], output)
mod['func_7075'] = func_7075
mod = relay.transform.InferType()(mod)
mutated_mod['func_7075'] = func_7075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mutated_mod.get_global_var('func_7075')
var_7077 = relay.var("var_7077", dtype = "int8", shape = (16, 9, 16))#candidate|7077|(16, 9, 16)|var|int8
var_7078 = relay.var("var_7078", dtype = "int8", shape = (16, 9, 16))#candidate|7078|(16, 9, 16)|var|int8
var_7079 = relay.var("var_7079", dtype = "int8", shape = (16, 9, 16))#candidate|7079|(16, 9, 16)|var|int8
call_7076 = func_7075_call(var_7077,var_7078,var_7079,)
output = call_7076
func_7080 = relay.Function([var_7077,var_7078,var_7079,], output)
mutated_mod['func_7080'] = func_7080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_7111 = func_3161_call()
call_7112 = func_3161_call()
output = call_7111
output2 = call_7112
func_7125 = relay.Function([], output)
mod['func_7125'] = func_7125
mod = relay.transform.InferType()(mod)
mutated_mod['func_7125'] = func_7125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7125_call = mutated_mod.get_global_var('func_7125')
call_7126 = func_7125_call()
output = call_7126
func_7127 = relay.Function([], output)
mutated_mod['func_7127'] = func_7127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2819_call = mod.get_global_var('func_2819')
func_2821_call = mutated_mod.get_global_var('func_2821')
call_7128 = relay.TupleGetItem(func_2819_call(), 0)
call_7129 = relay.TupleGetItem(func_2821_call(), 0)
output = relay.Tuple([call_7128,])
output2 = relay.Tuple([call_7129,])
func_7137 = relay.Function([], output)
mod['func_7137'] = func_7137
mod = relay.transform.InferType()(mod)
mutated_mod['func_7137'] = func_7137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7137_call = mutated_mod.get_global_var('func_7137')
call_7138 = func_7137_call()
output = call_7138
func_7139 = relay.Function([], output)
mutated_mod['func_7139'] = func_7139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5254_call = mod.get_global_var('func_5254')
func_5256_call = mutated_mod.get_global_var('func_5256')
call_7202 = relay.TupleGetItem(func_5254_call(), 0)
call_7203 = relay.TupleGetItem(func_5256_call(), 0)
output = call_7202
output2 = call_7203
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
func_1434_call = mod.get_global_var('func_1434')
func_1436_call = mutated_mod.get_global_var('func_1436')
call_7212 = func_1434_call()
call_7213 = func_1434_call()
func_39_call = mod.get_global_var('func_39')
func_40_call = mutated_mod.get_global_var('func_40')
call_7232 = relay.TupleGetItem(func_39_call(), 0)
call_7233 = relay.TupleGetItem(func_40_call(), 0)
output = relay.Tuple([call_7212,call_7232,])
output2 = relay.Tuple([call_7213,call_7233,])
func_7249 = relay.Function([], output)
mod['func_7249'] = func_7249
mod = relay.transform.InferType()(mod)
mutated_mod['func_7249'] = func_7249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7249_call = mutated_mod.get_global_var('func_7249')
call_7250 = func_7249_call()
output = call_7250
func_7251 = relay.Function([], output)
mutated_mod['func_7251'] = func_7251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6144_call = mod.get_global_var('func_6144')
func_6146_call = mutated_mod.get_global_var('func_6146')
call_7263 = func_6144_call()
call_7264 = func_6144_call()
const_7278 = relay.const([[[3.846946,2.155556,-7.115749,-9.723534,-2.672682,-6.503995],[5.391724,-3.920901,6.741591,7.949977,8.745634,-4.971304],[3.170589,-2.947037,-4.084614,3.800518,-9.308030,-9.950759],[4.387515,-5.622662,6.800188,6.259282,-2.739118,-3.152155],[8.097630,-7.253138,2.668753,-1.676120,-7.023974,3.359826],[0.943177,-2.495378,2.209719,-1.833441,9.521663,-5.536278],[9.398047,3.029088,9.856674,-5.193989,-7.820553,9.637410],[2.444123,-0.631745,7.341225,-9.762775,-9.069712,-3.308806],[-5.330926,-3.196644,5.252774,-6.807429,-3.616724,4.675580],[7.397682,2.291132,-5.314826,7.524503,-5.361972,0.950369],[2.126768,-0.575078,-3.167442,-9.627311,-3.679796,-5.254614],[5.099667,-4.635554,-1.861517,-1.524132,0.684927,5.172756],[-9.433112,5.817195,-1.920623,-4.246216,7.278592,-7.114418]],[[1.521971,-8.558277,8.078123,-9.615964,4.477759,2.212017],[-2.606993,1.937362,0.861851,8.458908,-4.099596,-9.905992],[4.916267,-4.934886,-9.816285,-1.219448,5.068086,8.442754],[4.001325,-0.236828,-8.517514,-8.038261,5.988057,8.309715],[8.662829,-3.523694,2.575953,-2.582923,-8.119815,4.616513],[2.865714,-5.958995,-9.577208,-4.423273,7.736805,-8.177448],[-4.180928,-0.434802,9.342376,-0.586912,-3.889194,-0.204749],[7.009856,-2.841406,4.468586,-4.645237,8.372555,-3.399474],[-0.090116,3.729306,3.326800,-7.580825,2.763859,3.471031],[-0.879689,9.174989,-2.133614,-2.914060,-3.736519,7.902823],[9.855702,7.220749,1.259380,-6.691589,-5.480208,2.801189],[-8.062999,0.760927,0.217745,-5.463333,-5.101079,-5.845562],[1.775541,-1.390909,-4.144524,4.856574,-3.508897,-9.445214]],[[-2.740901,7.983945,8.104183,-0.449013,-5.319451,2.053757],[-3.559271,2.181707,2.176304,-0.168252,5.554787,-0.689515],[-2.888176,3.620382,-7.070411,-0.899588,-3.816072,7.068016],[6.157076,0.107239,2.268408,6.862948,-1.251461,-1.868692],[-0.942173,-2.524225,-3.238917,8.320902,1.235463,5.139230],[8.141490,-0.013320,9.126788,8.944261,-4.523624,2.494381],[6.770980,7.337875,3.828332,6.603577,-4.042837,3.195504],[-5.943591,-2.941578,8.478364,-1.992249,2.236417,2.742391],[-2.964155,8.257777,0.040017,6.734424,2.690339,7.603163],[-6.309112,5.479776,-5.433016,8.472576,7.475695,-7.678735],[3.277490,1.306320,-1.453760,-8.507689,4.670282,3.517949],[-8.514116,8.490777,8.948355,-6.665693,3.360987,5.355430],[6.166390,1.479492,-0.923858,5.742420,-3.975069,-4.205374]],[[3.433705,8.215490,6.797676,-8.911983,1.531592,2.079659],[-0.301634,4.514322,3.118000,0.304294,6.801587,-1.073340],[5.501720,-8.821027,-0.976899,-4.904205,4.371756,5.669807],[-5.589557,-6.133552,9.672550,-8.727169,1.073782,-7.782335],[-3.751650,5.964541,-9.240329,3.429417,-7.715321,3.327093],[2.233793,-1.649838,4.885107,3.722089,9.670140,-1.901600],[0.508828,-9.672665,-5.017033,-8.792048,1.529583,-3.787286],[2.890323,9.047290,9.372205,-7.421378,-4.250350,2.922313],[-9.781611,5.096775,-7.127723,8.882229,-8.607480,4.878987],[-5.294721,-5.762467,2.938620,4.604059,-9.292977,-1.009262],[1.866583,-3.400644,-4.197254,3.232531,-9.308414,-1.214477],[-2.536053,6.845777,-1.732732,6.615185,-9.926298,-7.290981],[8.930158,-9.287173,-3.360525,8.109412,6.064079,9.527426]],[[-2.123107,4.935625,6.428120,6.127263,7.651802,-2.417820],[5.335670,-1.504595,0.177937,-5.588715,-6.791860,5.353375],[9.119007,-3.515605,-0.408426,-6.910840,-7.458924,-6.271366],[-6.115172,-4.316803,-9.040121,4.211545,-7.711793,3.282736],[-0.428175,-5.747589,-7.539508,7.133709,0.091599,-2.771848],[6.374810,-3.295645,-5.348145,0.354325,-6.936060,-9.288545],[-0.622611,4.659188,7.177063,9.998033,-5.388323,-7.904381],[0.440591,-7.337529,2.116779,-0.034180,-0.119016,6.747548],[2.029200,6.274404,-7.909881,-9.624299,2.507903,2.417067],[-8.841972,-0.861207,2.364698,9.781507,-6.396523,6.717206],[6.041494,-3.887805,-2.878845,-7.053379,-3.566833,0.931214],[-9.336855,2.937199,5.150702,-0.907117,9.028277,-8.684197],[-5.458314,0.191711,-2.249606,-8.816058,1.840242,1.640219]],[[-9.356451,8.626500,0.027548,7.323022,4.655070,9.476766],[-5.186158,-0.360996,-2.278943,-4.923200,1.081067,6.376653],[-1.185734,2.675517,-1.642103,5.617440,-2.978649,1.670739],[3.371374,7.506153,9.834191,-2.638216,4.777189,-5.852518],[9.281738,-9.994394,-7.471699,-1.424519,7.828130,-2.078470],[-1.450353,5.952702,7.427542,-2.164232,6.099725,7.689440],[-9.185365,-2.320007,-9.746318,2.023197,8.146301,-4.526081],[5.821633,-6.604819,-5.668097,-5.389670,-0.710151,-3.412382],[-7.547392,2.616965,-2.254899,2.864634,-0.517759,-7.958484],[-7.673755,-5.295387,3.324002,6.873130,-1.231869,-3.802708],[9.477503,3.931957,-2.630854,9.194863,7.297464,-2.478218],[5.057556,-0.948540,-4.128077,-2.424960,8.196788,-2.236516],[-6.241393,8.016518,-2.981819,3.115367,7.359595,1.566184]],[[-7.267885,-9.395051,1.791348,-5.933525,-8.806972,-3.017297],[2.166977,7.720972,-4.660383,-4.459530,-4.502497,0.554831],[3.049156,-2.974625,3.928054,-2.053739,-2.876478,2.147541],[1.487222,-9.035542,6.407248,-6.018327,5.891933,1.449287],[-2.503890,-8.414975,0.729425,7.581235,0.618171,2.782753],[7.381233,-5.334644,6.836972,-9.334633,6.708451,-9.225282],[0.155503,-4.979744,6.795763,-0.419519,7.804749,-9.620462],[-3.316278,5.794186,0.529899,0.824447,-0.343984,-2.026765],[5.606391,-8.202967,6.640249,9.719099,-8.605926,2.046483],[5.059967,3.055567,8.585417,-6.433816,9.539104,1.190739],[-2.053261,0.977207,-7.821969,-9.650615,-2.231180,1.350657],[-3.479833,0.257923,-6.929690,-6.171821,-7.550056,-1.734085],[9.660105,-1.368172,-2.199116,9.099399,-2.399575,7.687648]],[[-5.245483,-2.757192,-6.644306,-6.304216,7.290278,7.728126],[-5.411298,1.379757,8.356578,-1.973612,-4.868096,8.965405],[-2.489597,-6.195701,-3.232817,-3.109471,0.164388,6.700543],[-4.601342,-2.462785,2.200771,6.920712,8.351693,4.838651],[-8.427978,1.843792,-6.062500,2.165444,4.750681,1.870399],[7.261600,-9.017991,-1.700192,-9.087414,0.598074,-7.855057],[3.210474,3.940210,9.763448,3.732089,-4.869147,-4.268383],[-1.056141,-6.866082,1.830941,0.750604,4.661804,-7.088305],[5.080515,-5.279071,3.100329,-0.218614,-7.432280,-2.587328],[-3.158095,1.543025,-4.952846,3.361902,7.047495,1.396638],[8.931972,8.500668,-8.178181,-7.661751,-3.902237,8.595404],[-1.480094,-8.661069,6.843139,-2.212492,3.628193,-1.896282],[6.424934,-1.219574,3.826360,-1.879227,-6.968578,8.974476]],[[2.763837,-8.046014,-0.588300,3.233371,6.221857,6.977456],[-4.777231,-2.594696,2.400532,-0.182692,-3.858796,6.567836],[-3.182212,-9.340420,8.111147,4.189916,-6.987597,8.776008],[2.293304,3.105144,-9.342659,4.503649,-9.490335,-7.394447],[2.192144,-8.711695,4.226705,1.143153,1.556209,-0.767708],[-2.003107,0.847459,-8.265083,3.752400,-7.529130,-7.687295],[-6.985880,4.679321,-8.962506,-3.372555,-0.210113,2.549701],[7.618544,5.977761,7.471541,9.742195,-1.150118,-5.452276],[6.960357,-2.269648,-5.742817,6.444705,7.807681,2.229880],[-5.847710,9.157229,-8.483553,3.406382,6.830693,1.004208],[-0.964762,-6.818542,8.353019,1.163176,8.164631,-4.026063],[7.284176,-7.880217,0.449995,-4.514609,9.272057,-1.333193],[-0.758911,0.095856,3.248992,-7.919862,-7.896998,-0.590137]],[[5.730910,-3.029140,0.693960,-9.537852,-1.865855,2.382556],[-9.808680,-3.197243,9.393565,-6.888877,-5.970938,-4.042207],[-8.260891,1.739049,9.833535,-0.490303,-6.932855,2.398055],[-9.692265,-5.013831,-5.537657,-3.286378,1.462115,4.963770],[7.590650,-3.979533,7.303492,3.668959,-6.402988,-7.269672],[-2.957642,-9.616034,-5.613911,7.140468,-8.075460,8.630375],[2.242483,1.693712,-7.191953,-0.387057,-7.533756,7.973556],[5.040007,5.212400,-3.591750,3.049929,1.750801,9.689861],[-1.159540,-6.082897,-4.216464,6.897788,7.153737,-4.875142],[5.173978,9.300809,6.534981,-6.050814,-6.098533,-6.757996],[7.553866,6.817398,-1.619402,-0.281715,5.470331,6.466504],[4.166702,-3.476927,3.385660,-1.857421,3.746683,7.446894],[2.955472,2.639317,5.707820,-3.154622,5.102380,8.896606]],[[-4.053301,-4.671690,-4.597564,1.151220,0.458357,-9.957298],[-4.064502,8.537939,5.103842,-9.573509,-1.629477,-5.068672],[-3.017225,5.356589,-5.395741,9.503514,-6.829016,8.470441],[6.347552,-1.092698,-4.520765,3.807371,-2.878314,-0.119592],[7.732039,-9.968240,-0.287980,-3.060242,7.499701,-3.158913],[-2.746139,-8.223383,-5.893261,-2.709694,-6.690806,-9.451393],[6.552819,2.773969,-2.586067,8.720552,-0.953819,-7.722246],[-7.937916,2.598459,-7.823831,-7.685495,7.434958,5.667160],[-3.721644,1.796077,1.697477,0.586476,-5.000417,-2.700136],[-2.974838,-8.031481,6.276390,1.096529,8.063943,7.123854],[-6.086917,2.453116,-4.258812,7.845608,-7.002375,7.671791],[-9.436522,-6.139398,8.515473,-2.231105,7.649846,-7.224838],[8.778385,-0.727566,5.358129,-5.214152,1.349580,7.867817]],[[-6.092839,-9.408964,-2.442236,-4.546154,-4.329082,5.456984],[2.059025,3.178589,-2.218789,3.123032,1.083639,6.525908],[2.629959,0.128800,5.642397,-2.328316,6.901676,-2.715983],[-9.874141,4.262570,0.198712,-5.053791,-3.619004,8.477747],[-2.878759,-3.374184,3.339973,-2.001359,1.829852,4.977945],[-9.055069,-4.773435,8.877348,7.129465,-4.328401,-8.494078],[2.378741,-1.718975,5.698833,0.123081,0.222438,1.676747],[2.681379,4.324144,9.728349,8.913201,0.062294,-7.777714],[-4.829071,-8.230832,-2.915637,-6.749295,-5.577632,1.862136],[5.594287,1.426371,-3.708875,0.592988,-2.761259,-2.881599],[2.679101,2.132274,4.015038,1.553264,-5.317603,-5.111414],[0.964995,-0.613443,-9.985608,6.967441,-7.156289,-3.157557],[3.677554,-0.621729,-0.485888,-9.818026,-1.155544,-6.516962]]], dtype = "float32")#candidate|7278|(12, 13, 6)|const|float32
bop_7279 = relay.less(call_7263.astype('bool'), relay.reshape(const_7278.astype('bool'), relay.shape_of(call_7263))) # shape=(12, 13, 6)
bop_7282 = relay.less(call_7264.astype('bool'), relay.reshape(const_7278.astype('bool'), relay.shape_of(call_7264))) # shape=(12, 13, 6)
func_296_call = mod.get_global_var('func_296')
func_298_call = mutated_mod.get_global_var('func_298')
call_7299 = relay.TupleGetItem(func_296_call(), 0)
call_7300 = relay.TupleGetItem(func_298_call(), 0)
output = relay.Tuple([bop_7279,call_7299,])
output2 = relay.Tuple([bop_7282,call_7300,])
func_7302 = relay.Function([], output)
mod['func_7302'] = func_7302
mod = relay.transform.InferType()(mod)
mutated_mod['func_7302'] = func_7302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7302_call = mutated_mod.get_global_var('func_7302')
call_7303 = func_7302_call()
output = call_7303
func_7304 = relay.Function([], output)
mutated_mod['func_7304'] = func_7304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7204_call = mod.get_global_var('func_7204')
func_7206_call = mutated_mod.get_global_var('func_7206')
call_7310 = func_7204_call()
call_7311 = func_7204_call()
func_4468_call = mod.get_global_var('func_4468')
func_4471_call = mutated_mod.get_global_var('func_4471')
const_7320 = relay.const([1.419463,1.280111,-0.622517,-9.024012,-1.543715,-2.337450,-5.177476,0.373672,-4.956755,5.692777,-4.809118,9.759221,-8.107725,9.823610,-5.121135,5.771840,4.073049,1.245188,-7.673377,-0.970096,-8.254156,-6.745516,-0.911831,-8.819281,-7.326094,9.684331,2.790604,-7.426367,-1.810554,0.628988,5.609224,-7.274926,6.145881,-7.403494,2.902248,7.843512,-3.190413,2.130047,9.840014,1.082315,6.907775,-5.996248,6.408726,-4.945788,6.969210,-1.880874,3.119797,3.486619,3.912736,-1.385122,8.417991,-4.736482,1.255618,-8.655391,3.842568,-7.582325,-5.715370,4.716484,8.457458,9.778657,5.450735,9.067229,8.940686,-3.717506,7.174049,3.271943,-1.623257,-6.203454,1.964564,-1.405650,-2.849870,5.055525,7.262603,-7.950567,7.296158,8.889614,3.485754,6.426975,-4.140856,7.488242,-2.962289,-8.118588,2.442294,-0.820735,5.421697,6.078265,7.192427,-2.707101,-2.694381,4.319040,-8.668943,-6.148987,-2.037306,-9.880216,7.853025,-8.284578,3.302955,-4.577940,1.756185,4.784747,8.344578,-0.979883,-5.694113,-3.266203,2.105120,-0.201554,-1.850766,4.820692,-8.230588,2.888217,-6.208220,5.479370,-4.915050,-0.397191,-1.951027,-3.952617,-6.080407,-1.284668,3.759783,1.307791,-7.732735,3.133374,4.798505,6.505770,-6.265556,6.913020,-6.887102,-1.666702,8.865321,-8.875095,4.350163,2.138775,0.589536,-9.511647,-8.952383,9.680225,2.535443,-2.481677,-9.282388,-6.190716,-3.176932,4.344024,-9.318731,-7.156771,-5.200865,9.652414,0.012064,6.045907,-1.376036,-0.989735,-2.551189,8.199483,-1.537519,-5.777959,-9.141378,0.343676,-1.123674,6.756311,2.015045,-7.814246,4.566585,0.353440,6.715408,5.726250,-1.560102,-0.822976,-7.011445,-1.510377,7.875048,6.734028,9.871590,4.159144,8.219669,-5.900534,-1.757417,-3.348268,-8.169059,-6.666745,-8.411567,3.249142,7.908350,4.126708,9.269395,-1.526833,-2.921799,-6.320385,8.291792,-9.104091,5.013167,6.269805,6.587395,7.206263,6.056966,0.576633,4.982265,-1.144981,4.760605,-7.625878,4.744572,5.887817,-7.437915,4.353675,9.580061,-2.689552,-8.976836,-4.968814,8.660548,8.403624,-4.692171,7.277945,1.515643,-8.523483,2.973170,0.239960,-0.331474,1.044130,0.928779,-8.214701,-6.933474,3.358989,-8.583719,-5.886893,6.744221,-5.248116,7.174929,5.654411,3.369717,0.974682,5.255068,4.674569,6.267575,-7.418379,0.121537,-7.579735,-3.058598,-6.547746,7.804074,-8.342285,-0.081111,-2.528367,-0.009196,-1.251588,-2.273856,5.286286,-8.115709,7.911182,0.121819,-1.854225,-8.796802,-6.089306,-0.007269,7.505683,3.132353,-2.881863,-6.961462,1.398636,2.552417,-8.679489,8.373989,5.483530,-0.543023,-7.867822,-0.708371,-4.523028,5.529815,9.372019,1.667295,1.707830,1.813520,-4.900263,5.652982,-5.373077,6.341988,-7.158864,-5.766616,-0.460547,-2.448015,-5.536929,-7.871031,3.678644,6.036541,3.851243,6.835755,-5.965732,3.075235,-8.999096,-0.998277,3.670652,4.495865,1.019814,0.648305,-3.711691,-5.003055,-6.714029,4.847540,-6.185838,8.857527,0.517990,-6.301715,1.013228,-7.578574,-9.985709,-2.398275,-3.245840,8.548865,-5.092328,4.339041,-4.415345,9.716547,-0.433787,-1.345618,-1.926738,4.578717,-7.469930,2.605080,0.339861,4.797658,-2.894874,5.349945,4.574890,-2.129153,7.650922,-3.016654,4.251290,-0.018166,-4.699536,-7.507342,-0.814496,-2.085478,-5.812628,-3.492613,2.261721,2.637640,-9.059111,-1.248888,-7.648504,9.451939,7.388508,7.734696,7.867125,-9.168932,6.357087,-1.927363,-9.180123,-3.576813,-6.677261,-4.715143,5.845329,-2.082707,-4.840511,4.096796,0.340251,-6.635797,5.102645,-9.169947,-1.907969,-1.448885,1.108439,5.960747,-5.582009,-1.740375,7.663016,-6.577026,8.142326,-3.935947,-7.546494,-4.799549,-8.189667,-6.793951,-6.800491,-0.504103,9.416072,-7.943134,-2.980593,0.289189,-9.990837,7.746428,-5.969154,-5.613237,-4.809918,-1.920796,-1.713315,0.202615,8.938589,-3.170732,-3.274049,-7.240525,-2.362825,-2.760799,1.912046,9.635653,-7.464000,2.435176,-0.125743,-6.510761,-0.584871,4.911619,9.124606,9.122519,-7.362180,-7.499988,-6.623673,1.504446,-7.396726,7.500861,6.654891,2.538405,-2.033358,-6.428026,-6.120078,7.653796,1.189223,8.001328,7.126080,-6.502737,9.148029,-0.253886,2.120738,-0.572069,-3.754517,5.133731,-9.008170,2.607816,1.841713,7.463944,-5.893866,-7.373988,-8.744614,-4.963110,-2.256835,2.221238,6.573191,-2.545938,9.061722,-6.279792,-5.949054,5.398509,-8.355092,7.798077,2.602307,3.240917,-6.118747,2.236315,-4.120118,-3.781275,-3.992319,-7.570962,-4.365656,5.047242,0.905188,5.799594,1.393812,-4.905903,3.537833,-4.249191,-5.690251,-5.926451,2.415315,0.906533,3.278401,1.845496,-7.004124,7.381127,-3.912667,-0.957828,1.823668,9.584946,3.608555,-3.047387,-7.951818,8.092162,5.545452,4.629586,9.859587,-2.974944,-7.027470,7.319869,3.337867,8.062336,1.811971,7.318027,4.700995,5.800671,-6.889415,1.334616,-8.590994,6.435585,-1.118502,8.605566,-4.764352,-7.328476,9.847976,5.878785,5.254920,-1.969976,-3.479457,7.961201,-5.925373,-6.864412,-2.364078,6.760439,-8.177345,-5.475978,5.531888,6.234215,0.980079,2.516911,7.059500,2.710153,3.950147,0.431090,2.573812,-1.664047,8.514176,-1.144673,-8.141150,8.429978,1.630457,-4.785179,8.616434,-3.112600,1.516928,5.862245,-3.489841,2.830260,-1.206789,1.108473,6.786283,6.903464,1.856882,8.741122,-0.800137,-9.295357,-3.927144,-1.420638,-9.795177,7.526888,-4.331382,-3.141403,0.388513,0.800522,-5.669019,-1.752345,-5.468273,2.363741,1.188090,8.215810,8.695432,7.430241,-6.239230,6.217039,-9.569050,5.657439,1.555353,0.254335,9.921455,-1.612042,-1.097789,-1.348511,-8.545357,-3.121913,-9.430658,0.772018,8.377516,2.592551,2.540134,4.192746,8.178604,-6.476381,-1.473062,-4.794864,-7.839781,-8.562106,5.278499,4.052596,-5.070087,8.142027,-8.208275,-0.297218,-5.683004,8.467034,-7.020727,2.548868,2.415380,-2.486497,-6.824141,-0.759784,3.467877,5.219084,2.924379,-7.500230,-0.166968,-1.959091,8.238895,-2.691191,-3.219838,9.936522,-6.848341,7.201876,-9.315868,-9.585171,-7.337309,-0.832428,3.208613,-1.612334,-9.209421,-8.770790,-0.311791,3.003000,7.627253,0.662525,-8.022133,-4.262415,-8.295844,-8.401935,6.596269,0.515313,2.954347,4.285178,6.583691,8.187725,-1.760673,-2.515123,-8.879597,-7.483665,1.351316,-8.347946,-5.524721,6.919156,-6.058483,-4.965147,-2.617031,3.414658,2.254384,-4.640723,-7.363843,-3.825580,0.411966,1.326061,1.419847,5.670249,-6.544871,-9.302787,-9.643119,8.765535,8.172218,-5.210377,4.355539,-3.467191,-9.583755,2.560325,-1.770083,0.820055,-1.463066,-0.012998,0.955054,-0.359634,4.444252,-6.513037,-9.677868,-5.756537,3.615154,6.849981,-6.336050,6.839568,-1.701494,7.835877,9.707901,-8.809972,5.644837,9.627774,-5.806710,-9.977048,-7.136534,2.104322,-2.566934,-4.712292,-6.303117,-8.045521,1.454796,4.581742,-0.368062,4.537509,-7.486863,7.530069,-8.965770,-3.941279,4.486035,-2.521636,1.639198,-4.683556,1.694706,-1.633298,2.184526,-9.127433,-1.981737,-8.461719,-1.717836,-3.607469,-4.399954,-5.369934,-5.264715,1.440586,-1.781876,4.411366,-9.349287,9.555120,2.824197,7.323325,0.906721,7.807762,-6.598673,-3.467748,5.369286,9.627002,0.141685,-4.732635,-1.624298,4.850852,9.958308,-2.797525,-8.662363,2.510210,1.676585,-6.611112,-3.540103,1.713597,-3.036407,5.352507,-6.803966,6.872172,1.262184,-8.115321,4.105399,-5.156410,-4.600652,-6.625448,-3.094106,-2.012528,1.946664,-5.988482,8.836133,-8.448357,-2.809854,3.537881,-2.996795,-9.229598,4.643743,3.388040,-2.091824,7.432065,-1.719737,9.767824,-5.169843,4.429950,8.936200,9.012623,5.087765,-1.772262,-3.755984,-5.666551,-8.773145,-5.482516,3.318939,-4.280372,2.632696,9.744985,-3.899842,-1.228518,-3.720313,-8.452528,-8.811406,-0.834122,9.808296,7.332791,2.828777,-0.698505,-1.009858,7.769073,-3.411645,6.600475,1.943243,8.966252,2.541154,-3.859405,3.388889,7.735418,2.952478,6.194315,-1.397225,-7.802898,3.217588,4.570837,5.080669,0.268021,3.390630,3.637685,9.866545,-8.355120,-2.204586,7.130943,8.301853,8.962443,-0.475124,7.513927,2.223168,-9.444683,-0.316872,-5.171419,-5.671354,1.779509,-1.210342,9.179860,1.534603,5.418338,-6.434538,-4.463166,9.406982,-0.228330,-3.218432,9.210233,5.795091,-8.986022,1.211366,8.590546,9.549193,1.923998,7.948711,2.386351,-7.942515,4.608175,7.493517,-9.093484,7.609458,3.478448,-9.514112,-7.552687,-5.130271,3.035181,5.604466,-2.009403,5.346900,7.070122,-9.136906,-7.346758,7.420314,9.485707,6.926817,0.861464,6.145894,-1.788279,6.463244,9.021669,-6.769611,-6.285210,-1.259357,-9.101443,-1.419788,-4.337612,-4.756960,-4.667522,-9.578839,0.762953,6.652055,7.959342,2.840987,4.958259,-5.900063,-0.224669,0.018417,-3.914816,6.443536,-6.091145,-6.921042,-5.798047,5.034656,-6.946579,7.669154,8.908821,0.107610,0.685600,-5.226861,1.928391,3.003217,6.452742,-6.972384,-8.898512,-9.043329,-3.344586,-1.859599,-9.022667,5.280268,2.014670,-8.764246,2.535691,5.031108,-1.990681,9.608922,-1.039303,8.660596,-8.465591,-8.911208,-5.411339,4.200448,7.929554,1.610084,1.560591,2.487716,4.948468,4.328507,9.310945,0.545497,-7.167183,3.563066,-9.531120,8.136688,4.138910,8.793617,-6.821572,-1.077545,-8.419856,2.606598,-9.031597,3.007683,-9.915582,-8.561086,0.489009,4.093989,0.327690,7.956702,-6.439371,-7.272571,-3.553407,7.315026,-0.104285,-5.337939,5.365375,-0.216166,-2.449787,-8.249753,-4.033445,-0.911733,-9.718281,5.441796,3.638150,1.754658,6.346147,1.383393,-1.251697,0.192247,-0.862382,0.882738,0.463914,3.403321,2.880783,1.276934,-0.820683,-5.230793,1.281848,-0.673373,-2.516819,-7.655118,2.145024,6.577656,-3.903246,-1.852638,-8.805914,3.680893,7.915710,-0.657319,-1.354040,-7.544470,3.343997,9.412131,4.645820,0.860570,-6.937990,5.492134,8.891784,5.708650,8.154245,-8.709819,4.689338,-4.077664,-3.690050,-6.021582,-9.431101,-0.781214,0.146075,-0.642213,7.268922,-9.900186,-1.631060,-8.934831,-1.287163,6.528851,8.929352,6.711071,9.042773,-7.787080,-6.321884,-6.796332,4.081427,9.686527,6.212909,8.420280,4.248645,-8.811483,-7.026787,-7.173495,-0.455732,-2.045641,6.085065,-9.695856,8.370515,3.366549,4.807325,-2.749124,-8.606637,7.295784,-4.307504,-9.473579,-8.454746,6.863979,1.953738,6.804050,2.269510,-2.985268,-6.228671,-6.250081,0.583533,5.687314,1.186897,9.326430,2.007422,1.244439,-0.746617,-4.459753,-1.634711,9.523094,5.787890,2.251148,-6.053037,1.346969,8.595187,2.015138,8.837665,6.237217,-9.017146,-4.133211,-1.798079,5.934778,-6.354519,2.992402,4.504859,-5.731144,-2.952243,-1.757905,5.758176,0.234192,9.191202,7.971029,1.179023,1.255951,-3.152783,-4.888369,-7.795115,3.454125,9.330611,9.148666,9.540681,3.718458,-5.472567,-2.936924,4.780240,-1.574368,-9.488999,-0.157363,-8.830684,-5.159268,0.757094,0.633301,-3.447315,-8.355610,-5.427070,3.322168,-3.357002,4.114333,-6.283688,-3.400215,4.641990,-5.482803,2.874488,6.223088,-4.803543,-2.008761,-7.731288,1.979632,-0.946718,-1.650567,-8.438466,-7.016202,-1.124640,1.451021,4.749073,9.878702,-8.013829,1.616718,-2.271309,4.778111,-2.003723,-7.339883,-3.632728,2.348236,-4.080979,5.062187,2.807405,3.883762,7.316835,-9.812653,-9.665035,7.015375,5.797108,-6.892439,9.154801,9.885404,7.646347,2.869551,6.123218,-3.589737,-9.193934,-8.989758,7.493245,-3.770452,-0.756613,-2.940759,-6.493371,1.888715,-5.995033,8.136380,-1.696282,2.647646,-6.118315,8.065148,5.329995,2.359227,8.892680,-1.630116,5.612040,8.921486,6.826350,1.413602,9.627163,-9.887805,-5.086597,7.770374,-8.300293,3.010302,1.464361,-0.044489,-1.997167,0.866050,-2.145571,1.919858,-1.292419,1.844216,-5.104817,4.075676,-4.331292,1.691768,8.935371,9.827390,1.237910,-3.666144,6.291653,6.998775,0.562407,8.986796,-6.642295,3.909188,1.510849,3.718452,5.067445,1.452139,-8.551544,2.965342,8.585609,3.894378,9.565964,-1.325078,-7.309218,-4.383845,-1.562098,7.719107,-9.440966,4.220567,-1.362653,3.742430,3.355364,2.745981,1.083591,5.412062,3.169021,1.572276,-6.868916,3.560694,-7.251902,-9.889045,2.548199,2.628655,7.873839,1.852788,4.578940,5.201650,0.864738,-0.817155,5.861096,2.336792,-6.826772,5.882051,-0.077243,-5.263890,2.544714,7.308246,-4.917633,-2.067216,6.774873,7.931368,1.165385,8.931266,1.519517,4.765348,1.251510,4.143221,-3.593579,7.265840,2.587901,3.294385,-0.788643,7.548620,0.731856,-5.163497,8.648433,-4.372950,6.519626,0.391676,8.583187,3.317165,-9.721368,0.177694,-0.202894,2.334880,-1.547410,-4.606607,-4.921628,7.283141,9.363681,-7.031212,-3.394580,5.249755], dtype = "float64")#candidate|7320|(1260,)|const|float64
call_7319 = relay.TupleGetItem(func_4468_call(relay.reshape(const_7320.astype('float64'), [9, 10, 14]), relay.reshape(const_7320.astype('float64'), [9, 10, 14]), ), 0)
call_7321 = relay.TupleGetItem(func_4471_call(relay.reshape(const_7320.astype('float64'), [9, 10, 14]), relay.reshape(const_7320.astype('float64'), [9, 10, 14]), ), 0)
output = relay.Tuple([call_7310,call_7319,const_7320,])
output2 = relay.Tuple([call_7311,call_7321,const_7320,])
func_7330 = relay.Function([], output)
mod['func_7330'] = func_7330
mod = relay.transform.InferType()(mod)
output = func_7330()
func_7331 = relay.Function([], output)
mutated_mod['func_7331'] = func_7331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4034_call = mod.get_global_var('func_4034')
func_4035_call = mutated_mod.get_global_var('func_4035')
call_7348 = relay.TupleGetItem(func_4034_call(), 1)
call_7349 = relay.TupleGetItem(func_4035_call(), 1)
output = call_7348
output2 = call_7349
func_7366 = relay.Function([], output)
mod['func_7366'] = func_7366
mod = relay.transform.InferType()(mod)
mutated_mod['func_7366'] = func_7366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7366_call = mutated_mod.get_global_var('func_7366')
call_7367 = func_7366_call()
output = call_7367
func_7368 = relay.Function([], output)
mutated_mod['func_7368'] = func_7368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7249_call = mod.get_global_var('func_7249')
func_7251_call = mutated_mod.get_global_var('func_7251')
call_7443 = relay.TupleGetItem(func_7249_call(), 0)
call_7444 = relay.TupleGetItem(func_7251_call(), 0)
output = call_7443
output2 = call_7444
func_7454 = relay.Function([], output)
mod['func_7454'] = func_7454
mod = relay.transform.InferType()(mod)
mutated_mod['func_7454'] = func_7454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7454_call = mutated_mod.get_global_var('func_7454')
call_7455 = func_7454_call()
output = call_7455
func_7456 = relay.Function([], output)
mutated_mod['func_7456'] = func_7456
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7466 = relay.var("var_7466", dtype = "float32", shape = (11, 3, 5))#candidate|7466|(11, 3, 5)|var|float32
const_7467 = relay.const([[[8.996319,-6.441921,7.304319,-1.326682,8.903350],[-6.634105,8.109796,6.353557,-1.157404,2.091557],[5.557201,-8.537420,0.409287,-0.138001,2.560284]],[[5.716098,1.866091,3.417590,-0.883026,7.526168],[6.181486,-8.783448,-4.827701,-0.320364,5.545047],[9.854139,-9.118496,8.144871,6.036885,-9.241602]],[[3.400956,1.234693,9.022629,1.143825,-0.815050],[9.415033,0.722513,-6.678889,6.947220,-7.101127],[7.998982,-8.261909,0.558930,3.820424,8.211671]],[[-7.848927,4.677811,2.366881,-8.666254,8.326065],[8.304840,-8.571945,-6.149192,-6.551238,9.822522],[-5.057620,-3.949287,-4.016457,-8.695305,-6.025428]],[[-0.425100,-9.765621,-0.604403,-7.564093,-0.407329],[0.003089,4.158858,-1.765130,-0.343056,3.181276],[-9.042858,-0.761214,-9.242891,-4.347413,4.647950]],[[-0.320683,7.936754,0.601334,-9.209540,-8.652752],[6.111887,-2.106430,1.894604,-4.057561,1.764681],[8.215106,8.436843,-5.531662,7.088094,-7.132549]],[[1.933494,-0.979612,6.128951,-9.576199,5.569305],[9.440484,-4.288487,1.654108,-5.042455,-8.510956],[-9.522121,9.765046,9.704339,1.180892,5.024718]],[[9.322145,1.361338,2.529487,-4.810400,-2.525971],[1.309539,-3.739609,-1.024711,0.596333,-2.504585],[-8.705012,-1.405944,-9.519175,-2.246082,-7.917876]],[[-1.058082,-7.995333,0.640292,-6.441896,-9.550077],[1.551305,-8.408224,0.287424,-1.022093,-3.333978],[-5.754422,7.389194,-4.748441,7.378685,6.710941]],[[-5.674482,6.841584,0.081675,1.674633,-4.566906],[9.360673,7.784365,-0.449031,-8.966588,7.713567],[2.945675,8.411685,-7.066248,-9.783396,-8.567818]],[[8.579222,5.834970,-4.308042,0.824174,4.752526],[1.184985,-9.430575,-2.898608,9.013685,7.510317],[4.116972,7.428868,9.677654,0.462565,8.836075]]], dtype = "float32")#candidate|7467|(11, 3, 5)|const|float32
bop_7468 = relay.divide(var_7466.astype('float32'), relay.reshape(const_7467.astype('float32'), relay.shape_of(var_7466))) # shape=(11, 3, 5)
output = bop_7468
output2 = bop_7468
func_7478 = relay.Function([var_7466,], output)
mod['func_7478'] = func_7478
mod = relay.transform.InferType()(mod)
var_7479 = relay.var("var_7479", dtype = "float32", shape = (11, 3, 5))#candidate|7479|(11, 3, 5)|var|float32
output = func_7478(var_7479)
func_7480 = relay.Function([var_7479], output)
mutated_mod['func_7480'] = func_7480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7490 = relay.var("var_7490", dtype = "float64", shape = (2, 2, 13))#candidate|7490|(2, 2, 13)|var|float64
uop_7491 = relay.acosh(var_7490.astype('float64')) # shape=(2, 2, 13)
output = relay.Tuple([uop_7491,])
output2 = relay.Tuple([uop_7491,])
func_7499 = relay.Function([var_7490,], output)
mod['func_7499'] = func_7499
mod = relay.transform.InferType()(mod)
mutated_mod['func_7499'] = func_7499
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7500 = relay.var("var_7500", dtype = "float64", shape = (2, 2, 13))#candidate|7500|(2, 2, 13)|var|float64
func_7499_call = mutated_mod.get_global_var('func_7499')
call_7501 = func_7499_call(var_7500)
output = call_7501
func_7502 = relay.Function([var_7500], output)
mutated_mod['func_7502'] = func_7502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_933_call = mod.get_global_var('func_933')
func_935_call = mutated_mod.get_global_var('func_935')
call_7523 = relay.TupleGetItem(func_933_call(), 0)
call_7524 = relay.TupleGetItem(func_935_call(), 0)
func_2303_call = mod.get_global_var('func_2303')
func_2304_call = mutated_mod.get_global_var('func_2304')
call_7534 = relay.TupleGetItem(func_2303_call(), 0)
call_7535 = relay.TupleGetItem(func_2304_call(), 0)
func_1696_call = mod.get_global_var('func_1696')
func_1698_call = mutated_mod.get_global_var('func_1698')
call_7547 = relay.TupleGetItem(func_1696_call(), 2)
call_7548 = relay.TupleGetItem(func_1698_call(), 2)
output = relay.Tuple([call_7523,call_7534,call_7547,])
output2 = relay.Tuple([call_7524,call_7535,call_7548,])
func_7553 = relay.Function([], output)
mod['func_7553'] = func_7553
mod = relay.transform.InferType()(mod)
output = func_7553()
func_7554 = relay.Function([], output)
mutated_mod['func_7554'] = func_7554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4939_call = mod.get_global_var('func_4939')
func_4941_call = mutated_mod.get_global_var('func_4941')
call_7571 = relay.TupleGetItem(func_4939_call(), 1)
call_7572 = relay.TupleGetItem(func_4941_call(), 1)
func_3616_call = mod.get_global_var('func_3616')
func_3618_call = mutated_mod.get_global_var('func_3618')
const_7595 = relay.const([True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,True], dtype = "bool")#candidate|7595|(288,)|const|bool
call_7594 = relay.TupleGetItem(func_3616_call(relay.reshape(const_7595.astype('bool'), [288, 1])), 1)
call_7596 = relay.TupleGetItem(func_3618_call(relay.reshape(const_7595.astype('bool'), [288, 1])), 1)
output = relay.Tuple([call_7571,call_7594,const_7595,])
output2 = relay.Tuple([call_7572,call_7596,const_7595,])
func_7597 = relay.Function([], output)
mod['func_7597'] = func_7597
mod = relay.transform.InferType()(mod)
output = func_7597()
func_7598 = relay.Function([], output)
mutated_mod['func_7598'] = func_7598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1293_call = mutated_mod.get_global_var('func_1293')
call_7614 = relay.TupleGetItem(func_1291_call(), 0)
call_7615 = relay.TupleGetItem(func_1293_call(), 0)
output = call_7614
output2 = call_7615
func_7616 = relay.Function([], output)
mod['func_7616'] = func_7616
mod = relay.transform.InferType()(mod)
output = func_7616()
func_7617 = relay.Function([], output)
mutated_mod['func_7617'] = func_7617
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7628 = relay.const([[[9.181627,0.275052,-7.700977,-5.900842,-0.929257,-0.603287,-4.409001,1.889139,-7.330254,8.399265,-8.253649,7.355050,6.372043],[3.988191,5.571760,7.584595,2.374402,6.228094,-4.690712,8.884649,-3.827246,-1.841571,-1.872395,1.329589,-8.195369,5.229678],[-7.836930,-6.177230,-1.981819,-1.318932,6.036528,-0.553900,-0.031730,-6.085818,6.157133,1.733592,-0.376059,-9.848159,-2.592835],[8.987797,-8.033778,3.871607,8.864067,-8.358606,0.872422,9.129359,-4.623853,-8.749194,6.946267,0.863991,-2.362258,-9.541022]],[[-3.442572,4.442433,-5.252707,-3.082150,6.086671,-4.053777,9.749202,5.355965,2.547540,6.621339,-0.738633,3.281621,9.940535],[2.349934,7.457871,-2.468407,-1.077439,-7.890154,-6.791204,-8.064202,-9.739377,8.713956,8.709583,5.311470,6.657962,8.109705],[-0.870773,-8.137216,0.500535,0.474218,4.109409,7.596142,5.676655,9.853788,-4.696615,-2.327865,-1.048629,-2.396706,-6.961670],[-4.757462,1.276055,0.613329,-9.638373,1.663155,5.978856,2.023173,-5.542669,7.610389,-6.585749,1.416536,-4.417526,-5.426167]],[[9.105001,-6.613460,-4.036751,-9.902778,-0.609043,6.370578,9.791010,5.951919,9.366254,6.347404,5.177257,3.067690,9.275097],[-4.346467,-8.474257,-1.163637,0.147631,6.183319,-7.828555,1.071151,-3.682811,6.319638,7.027086,-9.740115,5.877239,-1.174376],[-0.177848,6.780908,3.754485,8.909091,-9.018961,3.141269,4.169970,5.697975,-5.241947,-8.523788,1.721506,-1.684859,-4.560807],[9.171582,5.691877,-0.716331,9.222254,6.633585,2.288488,2.487985,4.205776,-4.430981,8.853509,-1.646580,-4.394925,-1.182346]],[[-7.076469,7.009368,-7.813792,8.171777,-0.451416,0.833422,8.782445,-6.187077,-8.502283,-4.874892,8.745117,-7.808952,-9.984620],[-3.759647,8.593958,-1.433727,-8.177583,8.662879,-4.557589,-4.402744,-1.670930,-7.248029,-5.357534,4.039666,-3.675348,-2.898733],[-8.843901,7.429385,2.979885,0.831014,-8.232242,6.321571,5.803036,7.435494,4.738199,0.815450,-2.012969,3.875262,-1.775565],[6.362189,-9.841371,-8.439210,-7.763365,8.099664,-1.166600,-3.142208,-7.365351,9.281659,-2.327778,5.366871,-1.283417,-3.110356]],[[-0.231123,5.566991,-3.083795,-5.578450,4.740119,3.735846,-0.214408,7.773741,1.955472,4.278445,5.724933,-7.727904,-8.256478],[3.237731,-1.979192,1.777695,1.120828,9.013520,2.403490,-4.663244,4.270126,-4.070280,-0.470745,-9.557305,1.572428,0.307219],[-6.416369,5.852414,1.648934,9.280474,-7.297484,7.579008,0.193547,4.560429,-4.276391,7.761981,0.203599,3.898849,-8.334211],[4.627591,9.570528,-3.490013,-5.591764,-4.091316,7.019923,7.296295,-2.194165,5.422641,-4.964730,-1.708382,5.565021,-3.068531]],[[4.627305,-3.846412,9.786733,-6.957654,5.826369,-0.965106,-9.683388,6.234947,-0.658602,7.944119,7.307193,-8.446662,6.822059],[-4.491328,4.880521,9.801542,-1.590219,-6.901926,9.778395,1.017449,3.824561,7.071467,-2.846880,9.287098,5.302549,-2.788947],[-4.599443,-4.237225,8.685013,-5.936588,3.386641,-7.068860,8.848073,6.137907,1.543961,3.025278,-9.490474,-5.594104,-8.110430],[2.561413,-8.960028,-6.976301,3.564953,-5.993486,-6.141648,9.830708,-7.086845,3.302181,-3.428210,-4.059627,9.779265,-7.363822]],[[-8.259138,1.795551,5.276169,3.679589,-1.514234,-7.467487,-3.729189,-5.648652,5.434812,7.819414,4.205423,2.659335,9.486387],[6.409164,-3.860898,5.692549,-4.627043,3.043876,6.463117,7.965553,-3.074311,1.424701,-1.827416,1.804196,3.761262,0.273231],[-0.885711,-6.242742,8.760259,-6.644961,-3.379383,-7.244489,-9.491751,-8.954353,-0.083634,5.870007,7.036776,-0.327642,5.639994],[9.838879,-7.459374,6.841302,7.036809,-4.517753,-2.117721,-6.464410,-7.012997,3.275559,-8.744153,5.244573,-6.941760,-1.058464]],[[9.161245,5.940973,-6.194959,-5.870775,-3.807442,9.204720,1.375020,-9.087610,0.371140,-8.105634,0.589801,-7.708100,9.581835],[1.866605,5.237937,5.645003,-9.624898,7.735461,5.026498,1.999479,5.472938,-3.829149,-4.060111,-4.465659,3.446505,-0.258281],[0.067038,7.056282,-6.889373,-2.003389,-9.072783,-4.088528,-0.599511,5.036904,4.593674,8.380173,-3.456209,-0.231554,-3.814729],[-7.308054,9.227507,6.663615,0.498915,-3.909625,3.141821,3.926714,-9.698565,-5.444534,7.372251,5.655288,-2.473044,-1.519847]],[[-8.106478,7.151329,5.103256,-0.516744,-4.905595,6.606361,-1.938992,1.095356,-5.050503,5.294236,6.656218,-0.709314,-1.465243],[7.822888,-0.743345,8.102928,-5.481349,-6.794381,-2.997531,9.897583,-0.330127,-1.918619,-1.700199,-2.300149,7.404808,7.035494],[8.162999,5.354779,3.664798,-4.634760,-8.821418,-7.874340,-9.189592,9.682314,-9.032693,-1.335758,7.778017,6.568653,-8.881533],[7.964297,-7.558064,-3.250203,-7.231766,3.637270,6.951471,2.056195,6.756930,-5.275656,-8.230816,-1.765028,-1.807854,1.672624]],[[5.905290,6.376687,-5.281527,5.236570,-3.677730,-5.058355,-1.181547,-8.056196,0.104937,7.334292,-6.211455,4.965440,0.711679],[6.986901,-6.087606,-9.222656,1.646463,2.983855,-2.822077,-6.315478,7.813574,7.948093,-0.043416,7.705132,0.491776,-1.053481],[-1.591903,4.658736,8.918198,-2.253863,7.996494,-7.129171,-4.766400,4.039165,-9.381750,3.417660,-2.375823,9.662970,5.170511],[1.647616,-3.091783,-3.766022,2.426710,-7.425633,-7.704241,-7.379264,4.983589,-7.265779,-2.597013,-8.230892,-0.233058,-8.875431]],[[-3.114338,9.346146,-2.576318,5.485843,6.649101,-5.177282,9.804766,4.326003,9.428160,6.067962,-7.613435,-9.501459,5.086016],[-6.996042,3.342123,5.089197,-0.066608,3.107634,0.755511,5.994201,-9.054845,9.449920,0.257583,9.346982,-9.213221,8.613772],[-4.990548,4.830686,9.678578,4.821819,8.847333,-1.420824,-3.137577,-8.979344,-5.905643,-7.080002,1.409228,-0.478919,-3.492241],[1.975086,6.521641,-1.439606,1.469971,5.378133,9.254522,8.831062,9.311984,-6.215242,2.152311,3.801591,5.335135,-9.065625]],[[9.020761,8.847400,-9.104463,-0.968345,2.626471,0.794348,4.421689,3.335690,-4.965314,1.392962,8.356354,1.747115,-2.254993],[-9.060799,-0.198187,5.464880,-9.597478,5.750042,9.399398,-4.199823,-0.780700,4.021396,-0.711610,-2.051568,3.627467,3.151940],[-9.605571,0.601776,7.692630,-0.134303,-6.231352,-4.161071,-9.414027,4.327668,2.212941,-4.452003,-4.309144,8.777535,7.312420],[1.932153,1.149728,6.212783,2.920300,4.782926,-9.978224,-9.293658,9.788520,7.904502,-9.361809,7.091329,-7.679295,-7.605091]],[[-6.537461,-8.391404,9.241832,-3.668588,-2.531349,-8.378524,5.521676,-4.865307,5.946748,-3.637816,7.986076,-1.350644,6.748028],[-8.398525,-1.718678,-8.805962,-3.094748,-6.432164,-6.398663,4.498600,-8.554319,-3.365179,0.224233,4.178030,4.837152,2.895408],[-2.731078,-8.606959,4.522998,9.612963,3.195829,-8.210496,-8.158436,-9.195287,-9.664021,1.791277,6.336058,-1.164624,7.382992],[-5.748213,5.823917,2.964353,7.548932,1.901008,-7.300043,-1.074497,-0.718907,-0.212252,8.558146,0.517048,-9.048808,-3.689901]]], dtype = "float64")#candidate|7628|(13, 4, 13)|const|float64
var_7629 = relay.var("var_7629", dtype = "float64", shape = (13, 4, 13))#candidate|7629|(13, 4, 13)|var|float64
bop_7630 = relay.divide(const_7628.astype('float64'), relay.reshape(var_7629.astype('float64'), relay.shape_of(const_7628))) # shape=(13, 4, 13)
output = relay.Tuple([bop_7630,])
output2 = relay.Tuple([bop_7630,])
func_7633 = relay.Function([var_7629,], output)
mod['func_7633'] = func_7633
mod = relay.transform.InferType()(mod)
var_7634 = relay.var("var_7634", dtype = "float64", shape = (13, 4, 13))#candidate|7634|(13, 4, 13)|var|float64
output = func_7633(var_7634)
func_7635 = relay.Function([var_7634], output)
mutated_mod['func_7635'] = func_7635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2579_call = mod.get_global_var('func_2579')
func_2580_call = mutated_mod.get_global_var('func_2580')
call_7663 = relay.TupleGetItem(func_2579_call(), 0)
call_7664 = relay.TupleGetItem(func_2580_call(), 0)
output = call_7663
output2 = call_7664
func_7665 = relay.Function([], output)
mod['func_7665'] = func_7665
mod = relay.transform.InferType()(mod)
output = func_7665()
func_7666 = relay.Function([], output)
mutated_mod['func_7666'] = func_7666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5254_call = mod.get_global_var('func_5254')
func_5256_call = mutated_mod.get_global_var('func_5256')
call_7707 = relay.TupleGetItem(func_5254_call(), 0)
call_7708 = relay.TupleGetItem(func_5256_call(), 0)
output = relay.Tuple([call_7707,])
output2 = relay.Tuple([call_7708,])
func_7720 = relay.Function([], output)
mod['func_7720'] = func_7720
mod = relay.transform.InferType()(mod)
output = func_7720()
func_7721 = relay.Function([], output)
mutated_mod['func_7721'] = func_7721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5516_call = mod.get_global_var('func_5516')
func_5517_call = mutated_mod.get_global_var('func_5517')
call_7846 = relay.TupleGetItem(func_5516_call(), 0)
call_7847 = relay.TupleGetItem(func_5517_call(), 0)
output = call_7846
output2 = call_7847
func_7850 = relay.Function([], output)
mod['func_7850'] = func_7850
mod = relay.transform.InferType()(mod)
output = func_7850()
func_7851 = relay.Function([], output)
mutated_mod['func_7851'] = func_7851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1696_call = mod.get_global_var('func_1696')
func_1698_call = mutated_mod.get_global_var('func_1698')
call_7860 = relay.TupleGetItem(func_1696_call(), 1)
call_7861 = relay.TupleGetItem(func_1698_call(), 1)
func_4189_call = mod.get_global_var('func_4189')
func_4191_call = mutated_mod.get_global_var('func_4191')
call_7863 = relay.TupleGetItem(func_4189_call(), 0)
call_7864 = relay.TupleGetItem(func_4191_call(), 0)
func_1557_call = mod.get_global_var('func_1557')
func_1560_call = mutated_mod.get_global_var('func_1560')
var_7879 = relay.var("var_7879", dtype = "uint64", shape = (1960,))#candidate|7879|(1960,)|var|uint64
call_7878 = relay.TupleGetItem(func_1557_call(relay.reshape(var_7879.astype('uint64'), [10, 14, 14]), relay.reshape(var_7879.astype('uint64'), [10, 14, 14]), ), 1)
call_7880 = relay.TupleGetItem(func_1560_call(relay.reshape(var_7879.astype('uint64'), [10, 14, 14]), relay.reshape(var_7879.astype('uint64'), [10, 14, 14]), ), 1)
func_5604_call = mod.get_global_var('func_5604')
func_5605_call = mutated_mod.get_global_var('func_5605')
call_7897 = func_5604_call()
call_7898 = func_5604_call()
bop_7907 = relay.bitwise_xor(call_7860.astype('uint32'), relay.reshape(call_7897.astype('uint32'), relay.shape_of(call_7860))) # shape=(12, 13, 6)
bop_7910 = relay.bitwise_xor(call_7861.astype('uint32'), relay.reshape(call_7898.astype('uint32'), relay.shape_of(call_7861))) # shape=(12, 13, 6)
output = relay.Tuple([call_7863,call_7878,var_7879,bop_7907,])
output2 = relay.Tuple([call_7864,call_7880,var_7879,bop_7910,])
F = relay.Function([var_7879,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7879,], output2)
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
