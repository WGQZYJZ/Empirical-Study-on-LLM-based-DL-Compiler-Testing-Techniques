import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_389 = relay.var("var_389", dtype = "float64", shape = (14, 9, 12))#candidate|389|(14, 9, 12)|var|float64
uop_390 = relay.sin(var_389.astype('float64')) # shape=(14, 9, 12)
output = relay.Tuple([uop_390,])
output2 = relay.Tuple([uop_390,])
func_424 = relay.Function([var_389,], output)
mod['func_424'] = func_424
mod = relay.transform.InferType()(mod)
var_425 = relay.var("var_425", dtype = "float64", shape = (14, 9, 12))#candidate|425|(14, 9, 12)|var|float64
output = func_424(var_425)
func_426 = relay.Function([var_425], output)
mutated_mod['func_426'] = func_426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_472 = relay.var("var_472", dtype = "uint8", shape = (13, 4, 14))#candidate|472|(13, 4, 14)|var|uint8
var_473 = relay.var("var_473", dtype = "uint8", shape = (13, 4, 14))#candidate|473|(13, 4, 14)|var|uint8
bop_474 = relay.left_shift(var_472.astype('uint8'), relay.reshape(var_473.astype('uint8'), relay.shape_of(var_472))) # shape=(13, 4, 14)
func_424_call = mod.get_global_var('func_424')
func_426_call = mutated_mod.get_global_var('func_426')
const_478 = relay.const([4.205485,8.957826,-2.568363,-6.485265,-0.674551,4.359854,1.967979,7.402594,-0.381849,-6.158129,1.832267,0.074460,-6.655957,0.134124,6.785538,-6.915120,1.708577,6.044458,9.540715,-0.193101,6.431298,0.702967,8.066033,-1.611344,9.725873,-1.287355,-5.386721,-8.023404,1.639326,-0.858659,0.859549,0.480697,9.613326,0.684209,-0.065422,-7.033736,2.792366,8.283326,-4.486866,-5.984601,-7.980287,-9.874379,-0.764429,8.755612,-6.979136,-3.627879,8.082776,-6.948807,-6.236897,0.808641,7.647298,2.241386,9.990640,-1.011394,-7.423851,-9.273513,8.435646,-8.513033,7.198513,4.861830,3.356220,-6.833884,7.187957,0.161807,-1.374458,1.870981,-4.528495,-6.954182,6.814132,9.934482,6.700531,-5.416216,-1.694293,-6.170841,1.377819,3.211386,-6.930974,1.214090,-1.850695,3.381456,9.900768,6.944910,3.481361,-3.276389,-7.051414,3.335548,3.121105,-7.957301,-8.321777,8.077620,-7.281117,-4.241548,-4.255962,-4.537305,5.142993,7.614793,-5.886587,-6.844778,-5.553863,-8.274011,3.944251,-7.140924,-2.988784,-7.932674,-0.554546,-8.554262,8.979960,3.682574,-1.546105,-0.330123,5.283267,-1.247628,-1.023677,-8.159215,5.727529,6.849853,-8.892488,3.074624,-3.115968,9.189951,-5.138778,4.312518,-7.059022,4.969204,8.198303,-7.827633,-9.223711,-0.084054,-7.845006,5.420697,-5.082300,-8.669371,7.948107,8.792685,3.259290,-5.214199,-0.103684,3.407222,-3.677946,3.532954,8.427157,-4.721398,-5.325060,-2.122982,3.370082,9.073605,8.142599,-4.787632,2.124973,-7.347131,-5.474607,-1.149868,3.393681,-6.996261,2.483438,6.419001,6.504943,-6.996751,-9.913467,-8.517184,-2.544662,4.001033,6.530215,-6.800206,8.844237,-8.885590,3.932654,-1.848496,-3.320443,-1.906410,-5.907225,-7.202164,-6.902044,-1.160636,-9.575155,-6.561361,-2.967923,-3.202081,-3.845883,-7.145595,2.679729,0.418072,-8.883525,8.064027,-8.365465,-1.387661,5.037688,5.094587,9.641772,0.147514,-7.522532,-6.001461,3.183336,3.785436,-6.994754,-6.639022,-2.012086,-8.225827,4.497374,9.669199,-1.817400,1.612539,8.038826,2.337694,-0.694828,-6.689142,-5.948254,2.730296,9.822061,8.290081,-9.271813,3.173214,-6.321792,6.564267,-2.948979,8.123021,-0.924162,-1.749553,6.395401,-8.860921,-2.479131,0.969634,-2.747703,0.060081,7.340480,9.112690,-0.926478,-2.555910,-4.054624,-5.866714,-1.766082,9.960011,-6.195748,-7.572469,4.443168,9.094799,6.930194,3.540505,2.276129,3.531399,5.351781,5.954256,-3.301234,-8.346688,6.328533,4.058759,0.736186,2.239930,-8.854031,6.283273,-8.765871,-9.716982,7.689114,2.234983,-8.009399,5.504515,5.889880,6.496172,-7.257142,7.131951,-1.276019,-4.042386,1.545464,-1.586465,5.830886,-7.186198,-0.042727,-3.374952,-9.648063,0.625760,-7.631715,-1.784220,3.931339,4.424094,-4.413710,2.726746,6.101314,-9.120001,4.846583,0.488027,-4.537264,3.054027,-3.693026,5.249826,1.563222,5.561502,7.462735,-3.660831,7.429605,5.079608,-8.739847,-3.199793,-2.157355,-6.368382,3.112230,-9.456130,6.440505,5.326731,7.433067,-1.847068,2.929787,6.403377,-4.846664,3.462747,3.305263,3.169146,9.927537,-5.243448,-4.530291,-7.003540,-4.464128,4.241348,-5.190240,4.492183,3.977401,-6.656904,7.433330,-3.879431,1.687811,3.116929,-7.976356,-6.004715,-1.534521,9.927110,-9.188640,5.951916,-2.068132,-3.510014,0.798713,2.670040,-9.052376,6.670192,0.531053,7.800329,9.245341,7.555278,4.550384,8.030965,-2.880496,-0.778782,-8.987126,1.535600,-0.823302,2.905388,7.383414,4.682908,9.673896,7.234254,-2.987163,5.832972,4.674123,0.925245,2.561464,7.443603,5.092382,-6.996484,4.826849,-5.304993,2.768389,8.536382,-0.765930,-6.120893,2.451618,-7.982823,-7.710281,6.528161,8.481238,-4.282847,0.828652,-5.927686,8.199208,4.029118,2.593097,4.512776,2.608723,9.933360,4.279346,4.540243,-0.526244,-9.557244,-2.290241,-6.453225,-9.045647,-5.701234,-9.370071,-5.831632,5.048394,-5.759473,0.142991,1.363032,-0.350874,9.847420,6.327394,-2.645778,-3.090009,-3.134151,-3.142004,-7.692282,-9.240396,5.854591,-7.667594,-2.202358,9.356010,-0.184809,-2.200451,2.524135,-5.949279,-9.528311,-3.374071,2.316719,7.950465,0.672592,3.652889,-7.106335,-2.861993,-8.194581,9.734392,-8.288481,-5.355604,-6.754166,-5.080448,0.750152,-8.080792,-3.804988,3.175438,2.667612,-5.817949,-9.459782,3.963350,9.906226,-3.340746,-6.766697,-7.853534,-4.193765,8.386677,-8.880326,7.172338,-0.874960,4.712608,-5.211456,4.773245,-2.284509,-3.399564,1.070218,7.321227,3.800528,-0.118943,-5.783462,-0.682610,3.961438,4.882495,1.810224,-0.956008,-2.218502,6.824000,-5.057251,-7.499539,-7.796648,6.112191,-2.844042,-4.904536,4.030412,3.400733,1.936087,-7.062133,4.494947,-6.982007,-7.367328,6.943576,1.770736,0.838361,3.336109,-1.923434,-3.278747,5.500262,-3.279789,-1.670245,-5.812075,5.644059,7.703569,9.181509,6.032140,-2.090169,-2.716812,-9.804284,-8.302083,9.256402,-2.648460,7.762233,6.026841,5.379069,-5.274800,4.326719,-1.741671,-8.783808,2.967821,-3.530883,-7.322108,-0.302856,-6.693823,-3.612996,9.938366,-8.848096,1.134442,-9.508956,-0.764340,-1.574889,-3.089952,-9.124783,7.075721,-6.127776,-2.901726,3.563813,1.195808,0.030189,3.876060,-6.001158,8.479424,-6.752810,-9.150284,7.725558,-6.135444,2.811289,-3.672618,7.626368,5.954596,-4.164003,0.517512,-3.431468,4.337137,-4.743558,5.938649,2.767926,-3.030041,8.642626,7.843379,3.537339,-4.741730,-2.726164,-1.913939,-0.695628,5.027058,4.236084,3.311937,-8.061269,0.044296,0.482966,1.480075,9.865449,-9.702930,2.524058,-1.698174,4.603739,2.886156,9.300456,-9.928304,1.535655,-0.061078,-1.611270,-8.143860,-6.702652,1.665672,-0.510107,9.664881,-3.323707,-7.623394,7.655886,1.032180,-2.240239,-7.649391,-9.482505,2.849911,-3.383233,5.292479,4.793657,4.282374,1.412574,7.218460,-0.876713,-7.662171,-3.838837,-4.239319,1.259344,1.449385,-9.370244,3.838147,-3.735632,3.542225,-5.989815,0.203184,-4.119170,9.330252,6.949645,-2.936039,6.892228,6.023069,0.996423,2.289515,4.594049,-8.882658,-0.837600,-2.317763,2.249487,-2.778460,-4.466963,3.986209,-5.180953,7.286583,-7.697881,3.765828,-1.206525,0.437474,-3.084434,-4.876125,2.598250,-4.196527,-6.456708,-4.544565,-4.923657,0.454458,-0.735934,4.760377,9.656559,5.300282,-4.727211,-7.375120,6.743363,9.849507,-0.150052,3.010934,-7.453601,-2.598085,-8.072854,-3.454093,2.062229,-6.871831,4.397614,-8.514676,-5.128465,-1.978971,7.849226,8.098103,-1.940915,-1.061020,-2.191952,7.132372,8.221900,2.507582,-7.727324,-9.410314,1.724523,-9.923652,1.308685,7.213472,-9.462811,-7.433668,-9.923815,-1.626574,-7.195317,-5.530106,-4.863662,-5.835906,5.254755,0.564746,7.945694,2.397182,-5.013587,5.051913,-0.376272,2.444439,-1.494924,-6.561535,1.999700,-8.045484,-0.866833,-7.768759,-5.229531,-6.335118,-5.695831,7.260433,-8.020800,-6.879120,-4.353810,-5.581397,2.380086,2.845334,1.913411,-9.498551,-9.299598,8.398898,3.748626,8.054021,-8.202820,0.248375,-9.959234,-4.502885,1.900832,8.431117,6.551813,2.432014,-4.682933,-7.061112,-4.328628,-2.348047,8.331224,8.072251,-7.765067,-1.310594,2.074013,9.482450,2.018876,-3.902508,3.483305,-3.572945,4.901349,7.777187,1.676073,6.956972,-5.177445,-9.500707,7.833640,1.853674,4.495810,-3.033711,9.958084,-8.630635,-7.980316,-1.841890,-1.138213,-9.572195,-8.299908,6.781953,9.116153,1.755864,9.694869,-8.774124,-3.388484,-5.280728,6.582071,-6.851172,-7.840878,6.112537,0.495396,-3.761028,2.852620,8.384782,-6.241363,3.152078,4.813808,-9.746018,-8.344491,-3.225592,-8.457139,-2.141317,7.474520,-2.257420,9.578307,-5.486147,6.445529,2.400723,9.964131,-0.020521,1.168218,-0.434978,1.660506,3.761098,8.592537,-1.168039,-8.619770,4.414256,7.479900,-7.694374,-9.834212,9.680346,7.444322,-1.417070,1.839690,4.832312,-6.751227,8.160240,-9.267561,7.641449,-4.888752,1.366366,7.645135,3.250052,-4.775770,2.947365,-8.211142,3.184996,9.446842,9.457800,-8.064259,-8.881837,-0.039804,-6.495987,-6.871955,-8.146626,1.595023,-2.340843,-0.012757,0.117292,8.355810,4.068216,1.327598,8.016828,-0.982771,3.459144,1.273018,9.006674,-9.601755,-6.423186,-0.217859,4.373011,-9.694052,-2.288858,3.593447,-8.637343,-0.682415,5.011641,-5.144630,8.186210,7.396794,6.849420,-2.425808,-1.604583,6.594870,4.500812,9.727962,5.291075,-9.563942,-6.582725,-3.472311,-6.266806,3.559821,-5.011803,8.547369,-3.118783,5.193565,9.747148,1.065728,-4.747956,4.282018,-9.040614,-3.356907,-5.032640,8.663793,8.412136,6.726525,-4.969196,4.176164,-5.780526,-1.151800,7.095810,0.686488,1.002038,-3.191162,9.929535,-6.981224,-8.110942,4.628899,0.584615,1.393299,-7.203947,4.880528,3.871136,-3.344435,3.294339,6.278854,-6.784059,6.124202,4.213209,2.184225,0.464151,-7.812793,-1.206405,3.352650,-4.530233,-6.447826,7.655299,5.599938,-2.873752,5.290845,6.381699,-1.718148,7.336219,3.289924,8.204863,8.601494,-5.658067,-5.660366,9.030397,4.073851,4.628076,5.846236,1.598180,7.791012,-1.767808,9.392020,2.319173,7.184431,1.122904,5.950765,0.790638,-4.481220,-1.100165,-3.788839,-2.959045,7.244196,-9.623775,-5.895289,-8.458117,6.622106,-9.724812,-6.042036,4.571423,-9.147372,-8.047671,6.565619,-5.059350,-8.725674,3.499815,0.750102,-5.087457,5.228884,0.971606,-8.052698,0.127064,-4.818838,-6.155169,-8.314433,-5.855689,-5.565630,-7.837251,-1.009645,6.385861,-8.963929,9.509193,-9.862892,-8.774659,-4.450086,-4.843289,3.118246,5.673270,8.776580,-5.764064,3.098301,2.897863,-5.962007,5.636662,-2.251270,4.906264,4.698198,-4.818869,-8.410140,2.371750,-9.181827,0.071653,-5.897014,3.438534,-8.029558,9.392007,-3.847868,9.543228,-5.402049,1.518104,-4.394784,5.268377,-5.047225,4.241061,5.954365,1.994290,-9.479181,6.385160,3.995433,3.279657,4.823766,0.290856,7.681162,-7.866292,-6.530065,-4.458566,-7.043288,-4.173920,-5.575646,9.373376,9.121525,0.106554,7.319078,-1.548281,-5.309990,-1.620731,-7.887480,9.829170,-8.431388,5.069050,-3.529206,2.507042,-9.819988,3.470467,-9.455226,-8.083653,8.357609,4.498699,-2.625319,-8.895607,3.892132,-0.279599,-7.326298,0.474075,1.592264,6.526818,7.038989,-0.634245,8.013621,-2.769977,-4.017282,0.481934,-4.767061,-8.730255,-8.418181,7.397032,6.128450,9.390671,-4.909076,2.768768,9.471036,3.884683,3.739209,-0.279982,5.078257,-3.709858,1.681678,4.724125,3.186468,3.849207,-9.362370,3.707135,-0.826497,-3.735154,-7.990985,7.998048,-8.561626,-1.083845,-8.222683,-0.325039,8.603392,-9.177554,-3.576476,-1.311308,3.367203,1.481260,3.204658,-6.530538,7.929426,-7.518359,-4.592186,-5.235905,-5.983203,-3.696721,1.236462,-0.972583,-2.892216,-2.052301,-6.981777,-3.575576,-7.464760,-1.075612,-7.207165,0.876158,1.125832,0.887858,6.791739,-9.090446,-3.808290,9.965647,-6.771731,-6.110297,-9.991919,7.611225,-7.258745,-4.997623,-5.216956,-7.426605,1.884683,-2.948050,7.676687,-0.417073,1.395219,-9.624110,-5.165675,-7.571586,6.292910,2.229892,7.863274,-4.244871,-0.556720,-4.624776,9.018458,4.018688,-4.960097,9.477897,-0.849043,8.285164,8.672244,2.438132,5.882197,-9.631029,9.888738,-3.478111,-1.164485,-0.727171,2.243166,0.395532,1.398172,-6.531994,0.103508,0.229118,0.284891,6.322156,-5.354843,-9.730588,-8.459838,-9.403963,-0.623724,-0.681147,7.729140,3.555737,9.291907,-6.786149,-1.973889,4.869866,-7.110472,8.652849,6.457386,-1.658600,4.033767,9.667406,5.644524,8.528088,-5.816291,1.668393,-1.193881,-8.675091,8.137045,-8.266697,9.176774,3.075274,-6.707896,-2.851098,-8.307481,2.977020,4.307388,8.322620,-9.790447,3.325152,3.688375,8.670832,4.425435,6.973793,-3.059698,-2.169481,1.011888,7.544832,-0.115846,7.704689,2.683944,3.695819,2.648632,7.844823,6.628445,-7.030840,5.161044,7.506356,-0.123113,-6.426410,-4.104463,-7.796284,-9.329716,-9.740753,6.891504,1.384244,-1.932325,-0.505612,-5.905692,-6.490417,-9.759651,-8.262452,-6.664010,-8.261857,-8.822943,6.632847,-4.024604,5.215122,1.119946,1.962709,1.852460,5.492434,4.613849,-1.527941,-1.392664,-8.948193,0.619331,-9.522834,-6.920914,-7.344474,1.769040,1.469584,-0.817840,0.510009,-1.662884,-2.716245,1.302696,-5.649470,2.172195,-3.430987,4.049797,-1.821356,2.807587,-2.429461,-4.377658,5.486230,-6.067438,4.102829,2.001213,-1.075917,7.414703,9.824875,8.273130,-4.261703,-2.801248,-0.407269,0.382141,1.204441,2.458654,-0.352106,-5.235409,-7.406099,-1.532864,7.843381,-3.793992,-4.743859,8.566385,-1.177708,2.499748,5.569079,-8.949681,9.062319,2.907973,-6.916400,-4.980583,-3.606761,-9.562154,5.793560,-1.246959,-1.161311,-8.321940,-6.968805,3.660429,-4.970964,8.800188,-7.408697,8.631862,7.525584,-2.184877,-3.578017,-1.872752,-1.782911,1.668863,-5.220707,-2.778039,-3.087396,3.111623,-8.376026,4.788050,3.633691,4.773267,-3.467499,6.972490,6.229427,-5.135943,-6.715297,-8.523985,9.141067,-0.798475,6.515300,4.314011,8.609023,-0.324645,2.817592,1.529525,0.927680,-8.660495,0.010957,8.324163,-4.251407,-9.585141,3.245997,4.012090,-6.711337,-2.603341,-6.152013,8.267847,-0.898298,-1.283370,-3.456342,-4.358315,-7.625945,6.922603,-7.603669,-2.478070,-2.813492,2.307076,1.468485,7.829077,-5.540965,5.155728,1.025505,-9.823506,-7.284123,7.767076,-6.369502,-3.179903,-1.212685,4.488133,1.065214,1.472084,-1.988760,4.738411,7.291578,-9.493054,-3.859872,8.687394,-4.848378,2.299286,-6.659355,5.434841,-4.956514,3.009445,-1.779776,8.822744,-8.119268,5.049359,1.086204,-1.238344,3.180435,-6.293023,-7.429378,9.327307,5.141351,0.253577,9.162708,0.511474,0.614680,9.222554,9.926327,7.379242,2.072161,-4.927757,3.163114,-7.605639,5.527401,-8.363323,-0.371778,8.701020,-6.553843,9.275098,5.687914,6.287195,4.010372,-5.701115,0.496473,-2.320112,0.602660,1.328401,6.989670,9.179081,-9.773894,-9.969270,-4.129565,-9.091791,-6.744227,-0.203195,-2.143496,-5.544838,-7.705216,-9.419600,-6.575681,9.595485,-7.585158,-5.667146,-2.591849,-2.797632,8.989936,7.779088,-7.759939,-5.547382,5.858678,4.341262,-1.216096,9.618993,-7.006900,-0.743014,-8.766675,-1.376238,-9.251251,-6.280547,6.961655,1.410111,8.626598,-7.827219,0.342463,-1.326376,3.781419,-8.696136,-3.314581,1.837395,-0.444061,7.436339,7.719885,3.025354,6.368335,-6.722142,-3.463066,7.765703,-5.913616,-8.916712,1.267390,-1.294088,-0.367473,-6.475736,-6.193750,0.059868,-4.768429,3.620636,7.655590,3.811913,-8.046435,6.884875,-1.890654,-2.214588,-2.565788,-0.338023,0.874053,-8.730289,7.373376,-5.339565,-6.941796,-6.680846,5.049804,-3.116689,-6.912173,7.426999,9.646530,-1.418897,7.924598,-8.100959,8.034907,0.917492,2.214973,-5.738593,1.349437,-3.402466,-1.286275,-7.530405,-6.285337,-1.620826,-4.082694,6.592888,-7.387955,6.658177,-2.936617,4.483061,-6.992324,2.854734,2.286252,9.529762,-3.766316,-2.787188,-1.969736,-3.676637,-7.537792,-3.079029,-4.340784,-1.544073,2.917796,1.391227,-5.466154,1.872156,3.263423,-0.660015,-5.869883,6.297463,-6.616444,6.362549,-2.458023,0.242533,8.985603,-9.409321,-5.395969,-1.437011,-0.146544,8.556016,4.763688,-8.605543,0.381915,3.348276,-5.022147,5.860024,-6.968221,5.164302,-9.357384], dtype = "float64")#candidate|478|(1512,)|const|float64
call_477 = relay.TupleGetItem(func_424_call(relay.reshape(const_478.astype('float64'), [14, 9, 12])), 0)
call_479 = relay.TupleGetItem(func_426_call(relay.reshape(const_478.astype('float64'), [14, 9, 12])), 0)
func_424_call = mod.get_global_var('func_424')
func_426_call = mutated_mod.get_global_var('func_426')
call_489 = relay.TupleGetItem(func_424_call(relay.reshape(call_477.astype('float64'), [14, 9, 12])), 0)
call_490 = relay.TupleGetItem(func_426_call(relay.reshape(call_477.astype('float64'), [14, 9, 12])), 0)
func_424_call = mod.get_global_var('func_424')
func_426_call = mutated_mod.get_global_var('func_426')
call_508 = relay.TupleGetItem(func_424_call(relay.reshape(const_478.astype('float64'), [14, 9, 12])), 0)
call_509 = relay.TupleGetItem(func_426_call(relay.reshape(const_478.astype('float64'), [14, 9, 12])), 0)
func_424_call = mod.get_global_var('func_424')
func_426_call = mutated_mod.get_global_var('func_426')
call_541 = relay.TupleGetItem(func_424_call(relay.reshape(call_508.astype('float64'), [14, 9, 12])), 0)
call_542 = relay.TupleGetItem(func_426_call(relay.reshape(call_508.astype('float64'), [14, 9, 12])), 0)
output = relay.Tuple([bop_474,call_477,const_478,call_489,call_508,call_541,])
output2 = relay.Tuple([bop_474,call_479,const_478,call_490,call_509,call_542,])
func_546 = relay.Function([var_472,var_473,], output)
mod['func_546'] = func_546
mod = relay.transform.InferType()(mod)
var_547 = relay.var("var_547", dtype = "uint8", shape = (13, 4, 14))#candidate|547|(13, 4, 14)|var|uint8
var_548 = relay.var("var_548", dtype = "uint8", shape = (13, 4, 14))#candidate|548|(13, 4, 14)|var|uint8
output = func_546(var_547,var_548,)
func_549 = relay.Function([var_547,var_548,], output)
mutated_mod['func_549'] = func_549
mutated_mod = relay.transform.InferType()(mutated_mod)
var_735 = relay.var("var_735", dtype = "float64", shape = (14, 11, 6))#candidate|735|(14, 11, 6)|var|float64
var_736 = relay.var("var_736", dtype = "float64", shape = (14, 11, 6))#candidate|736|(14, 11, 6)|var|float64
bop_737 = relay.floor_mod(var_735.astype('float64'), relay.reshape(var_736.astype('float64'), relay.shape_of(var_735))) # shape=(14, 11, 6)
uop_748 = relay.sin(bop_737.astype('float32')) # shape=(14, 11, 6)
output = relay.Tuple([uop_748,])
output2 = relay.Tuple([uop_748,])
func_758 = relay.Function([var_735,var_736,], output)
mod['func_758'] = func_758
mod = relay.transform.InferType()(mod)
mutated_mod['func_758'] = func_758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_758_call = mutated_mod.get_global_var('func_758')
var_760 = relay.var("var_760", dtype = "float64", shape = (14, 11, 6))#candidate|760|(14, 11, 6)|var|float64
var_761 = relay.var("var_761", dtype = "float64", shape = (14, 11, 6))#candidate|761|(14, 11, 6)|var|float64
call_759 = func_758_call(var_760,var_761,)
output = call_759
func_762 = relay.Function([var_760,var_761,], output)
mutated_mod['func_762'] = func_762
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1243 = relay.const([[[-0.417143,-4.746911,1.521489,-7.866853],[-3.316691,-4.123056,3.293978,4.142725],[9.907062,-7.197528,-6.145380,6.129920],[6.595603,4.595867,-5.195239,-4.560146],[8.145604,3.846063,-1.698118,9.594405],[-6.480413,-7.632191,8.774920,-3.480047],[-5.900773,7.298631,0.876349,-3.806956],[9.575553,-5.225683,-1.400416,-6.755853],[-4.160093,-0.096466,4.906757,0.932251],[-0.659577,6.486609,6.782637,-7.345869]],[[-9.041143,9.685575,-9.344382,9.794690],[8.839160,4.238841,-7.998268,6.894683],[9.396653,-2.351848,-4.066213,-4.625471],[4.850249,-4.646378,7.821499,-2.801735],[9.021224,-3.506898,3.771679,4.729459],[8.493794,1.704498,-1.721502,-6.270987],[-8.687113,-1.081199,9.125642,9.343238],[8.983418,8.080696,7.593308,-8.825865],[4.135142,-7.008421,-9.338288,-9.529488],[3.470764,-8.132298,-6.177973,5.438313]],[[0.701905,9.277561,8.431065,4.474130],[1.753633,8.169267,4.916257,8.326599],[-9.870766,2.602288,1.552200,5.041831],[7.237372,-9.842883,-4.608618,9.762890],[4.703057,-6.892583,3.843792,5.736797],[0.727714,1.966047,9.168382,5.995407],[3.408515,-0.111634,-2.056170,4.106403],[6.743113,-9.665842,9.100528,1.854229],[-8.546218,9.391245,-8.933902,-6.331837],[-7.919195,-0.833437,-1.154404,6.071423]],[[-9.830227,-6.304002,9.309130,6.912289],[2.130878,8.088030,6.347486,-3.436717],[-5.897928,0.266201,-7.842459,-8.358439],[-9.246948,-1.796417,5.216025,-4.469934],[-6.647650,-0.931485,-0.498812,-2.737420],[4.411721,-3.287873,4.610278,3.062478],[2.730852,-0.282065,-4.643195,-9.967465],[1.405343,-4.879602,-6.312162,-0.190182],[1.028904,3.293295,-8.921649,-3.556736],[8.789561,-1.507790,2.486119,-3.186996]],[[2.745726,-6.123469,-4.207347,-9.931880],[-5.445773,-1.462999,4.439718,2.044617],[6.201126,-9.677654,-8.869602,-3.438439],[6.516568,-9.036003,-0.734001,1.695886],[1.093068,8.743018,-1.078813,8.465518],[-3.429171,-9.490109,4.144375,2.436231],[-8.286489,-7.690084,-1.984960,-3.509093],[-3.144954,-5.221408,3.737663,-6.372874],[3.798281,-8.085379,1.925706,-9.844576],[8.576729,5.977469,-8.235515,-1.281222]],[[-5.414698,-0.780732,5.175726,-1.421149],[7.689323,-0.532618,1.826241,-9.535700],[-1.923912,-7.405866,-6.777159,-7.116918],[2.035208,-9.662833,-3.907930,-2.416631],[-9.963155,6.133914,7.652825,3.431340],[-8.868486,-8.472039,-6.850671,-4.336967],[7.845611,-9.533520,-0.999683,-4.488797],[-0.718098,7.254541,2.352993,9.854376],[-4.164949,9.647486,-1.137505,7.623389],[-2.921515,-0.937247,-7.544688,4.848312]],[[-3.003317,7.198891,-9.914408,-4.136418],[3.157403,6.260441,-4.698512,-2.680942],[4.519172,-6.312258,-1.647872,-6.677157],[7.453464,8.166948,-5.963475,-5.326593],[-9.670232,4.879803,0.521973,2.155444],[5.823209,4.218847,8.065222,9.648457],[8.645221,-0.729056,2.165597,-5.909349],[-4.831709,-7.314204,-4.763063,4.903082],[-9.076936,-9.095964,-3.217098,-4.841425],[-6.584271,0.373646,4.281769,8.519308]],[[9.090635,-1.225134,-3.554460,7.237951],[-1.611122,6.415177,-3.409529,9.529247],[9.729419,-4.522676,3.930002,-2.659535],[-2.250297,2.487200,-7.802411,-3.712436],[4.598348,-0.883807,9.946829,-4.965371],[4.352428,3.264398,-8.174383,-5.892045],[-9.211121,0.099768,-4.759506,4.653389],[-0.689677,-1.845948,6.232728,-2.852482],[-4.264642,2.716871,-9.635649,7.032994],[3.462319,-8.293918,-7.271761,-8.473309]],[[1.719056,-1.647046,3.041366,1.612349],[5.395465,-4.876544,-6.247034,1.525412],[7.806744,4.054480,-3.698866,6.956489],[7.862915,2.717961,-7.088767,-3.919245],[4.731896,3.130065,-0.423740,-5.802821],[8.841042,6.745242,6.289676,-2.378724],[3.800823,0.096706,-4.360114,9.674537],[-4.038131,1.031865,-4.796490,-9.922676],[0.578348,-3.791729,-9.478192,0.831214],[7.352027,-0.707957,5.821124,2.516534]]], dtype = "float64")#candidate|1243|(9, 10, 4)|const|float64
var_1244 = relay.var("var_1244", dtype = "float64", shape = (9, 10, 4))#candidate|1244|(9, 10, 4)|var|float64
bop_1245 = relay.floor_mod(const_1243.astype('float64'), relay.reshape(var_1244.astype('float64'), relay.shape_of(const_1243))) # shape=(9, 10, 4)
func_758_call = mod.get_global_var('func_758')
func_762_call = mutated_mod.get_global_var('func_762')
var_1254 = relay.var("var_1254", dtype = "float64", shape = (154, 6))#candidate|1254|(154, 6)|var|float64
call_1253 = relay.TupleGetItem(func_758_call(relay.reshape(var_1254.astype('float64'), [14, 11, 6]), relay.reshape(var_1254.astype('float64'), [14, 11, 6]), ), 0)
call_1255 = relay.TupleGetItem(func_762_call(relay.reshape(var_1254.astype('float64'), [14, 11, 6]), relay.reshape(var_1254.astype('float64'), [14, 11, 6]), ), 0)
uop_1265 = relay.atan(var_1254.astype('float64')) # shape=(154, 6)
bop_1276 = relay.less_equal(uop_1265.astype('bool'), relay.reshape(call_1253.astype('bool'), relay.shape_of(uop_1265))) # shape=(154, 6)
bop_1279 = relay.less_equal(uop_1265.astype('bool'), relay.reshape(call_1255.astype('bool'), relay.shape_of(uop_1265))) # shape=(154, 6)
output = relay.Tuple([bop_1245,bop_1276,])
output2 = relay.Tuple([bop_1245,bop_1279,])
func_1280 = relay.Function([var_1244,var_1254,], output)
mod['func_1280'] = func_1280
mod = relay.transform.InferType()(mod)
var_1281 = relay.var("var_1281", dtype = "float64", shape = (9, 10, 4))#candidate|1281|(9, 10, 4)|var|float64
var_1282 = relay.var("var_1282", dtype = "float64", shape = (154, 6))#candidate|1282|(154, 6)|var|float64
output = func_1280(var_1281,var_1282,)
func_1283 = relay.Function([var_1281,var_1282,], output)
mutated_mod['func_1283'] = func_1283
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1432 = relay.var("var_1432", dtype = "int32", shape = ())#candidate|1432|()|var|int32
var_1433 = relay.var("var_1433", dtype = "int32", shape = (14, 12, 2))#candidate|1433|(14, 12, 2)|var|int32
bop_1434 = relay.equal(var_1432.astype('bool'), var_1433.astype('bool')) # shape=(14, 12, 2)
output = bop_1434
output2 = bop_1434
func_1445 = relay.Function([var_1432,var_1433,], output)
mod['func_1445'] = func_1445
mod = relay.transform.InferType()(mod)
var_1446 = relay.var("var_1446", dtype = "int32", shape = ())#candidate|1446|()|var|int32
var_1447 = relay.var("var_1447", dtype = "int32", shape = (14, 12, 2))#candidate|1447|(14, 12, 2)|var|int32
output = func_1445(var_1446,var_1447,)
func_1448 = relay.Function([var_1446,var_1447,], output)
mutated_mod['func_1448'] = func_1448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2124 = relay.var("var_2124", dtype = "uint64", shape = (12, 16, 6))#candidate|2124|(12, 16, 6)|var|uint64
var_2125 = relay.var("var_2125", dtype = "uint64", shape = (12, 16, 6))#candidate|2125|(12, 16, 6)|var|uint64
bop_2126 = relay.right_shift(var_2124.astype('uint64'), relay.reshape(var_2125.astype('uint64'), relay.shape_of(var_2124))) # shape=(12, 16, 6)
output = bop_2126
output2 = bop_2126
func_2152 = relay.Function([var_2124,var_2125,], output)
mod['func_2152'] = func_2152
mod = relay.transform.InferType()(mod)
var_2153 = relay.var("var_2153", dtype = "uint64", shape = (12, 16, 6))#candidate|2153|(12, 16, 6)|var|uint64
var_2154 = relay.var("var_2154", dtype = "uint64", shape = (12, 16, 6))#candidate|2154|(12, 16, 6)|var|uint64
output = func_2152(var_2153,var_2154,)
func_2155 = relay.Function([var_2153,var_2154,], output)
mutated_mod['func_2155'] = func_2155
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2443 = relay.const([[[False,False,True],[True,True,True],[False,False,True],[True,False,False],[False,False,False],[False,True,False],[True,True,False],[True,True,False],[False,False,True],[True,True,True],[True,True,True],[False,True,False],[True,True,False],[False,True,False],[False,True,True],[False,True,False]]], dtype = "bool")#candidate|2443|(1, 16, 3)|const|bool
var_2444 = relay.var("var_2444", dtype = "bool", shape = (7, 16, 3))#candidate|2444|(7, 16, 3)|var|bool
bop_2445 = relay.logical_and(const_2443.astype('bool'), var_2444.astype('bool')) # shape=(7, 16, 3)
func_1445_call = mod.get_global_var('func_1445')
func_1448_call = mutated_mod.get_global_var('func_1448')
var_2461 = relay.var("var_2461", dtype = "int32", shape = ())#candidate|2461|()|var|int32
call_2460 = func_1445_call(relay.reshape(var_2461.astype('int32'), []), relay.reshape(var_2444.astype('int32'), [14, 12, 2]), )
call_2462 = func_1445_call(relay.reshape(var_2461.astype('int32'), []), relay.reshape(var_2444.astype('int32'), [14, 12, 2]), )
var_2466 = relay.var("var_2466", dtype = "bool", shape = (14, 16, 3))#candidate|2466|(14, 16, 3)|var|bool
bop_2467 = relay.less(const_2443.astype('bool'), var_2466.astype('bool')) # shape=(14, 16, 3)
output = relay.Tuple([bop_2445,call_2460,var_2461,bop_2467,])
output2 = relay.Tuple([bop_2445,call_2462,var_2461,bop_2467,])
func_2477 = relay.Function([var_2444,var_2461,var_2466,], output)
mod['func_2477'] = func_2477
mod = relay.transform.InferType()(mod)
mutated_mod['func_2477'] = func_2477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2477_call = mutated_mod.get_global_var('func_2477')
var_2479 = relay.var("var_2479", dtype = "bool", shape = (7, 16, 3))#candidate|2479|(7, 16, 3)|var|bool
var_2480 = relay.var("var_2480", dtype = "int32", shape = ())#candidate|2480|()|var|int32
var_2481 = relay.var("var_2481", dtype = "bool", shape = (14, 16, 3))#candidate|2481|(14, 16, 3)|var|bool
call_2478 = func_2477_call(var_2479,var_2480,var_2481,)
output = call_2478
func_2482 = relay.Function([var_2479,var_2480,var_2481,], output)
mutated_mod['func_2482'] = func_2482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2730 = relay.var("var_2730", dtype = "float64", shape = (12, 3, 14))#candidate|2730|(12, 3, 14)|var|float64
var_2731 = relay.var("var_2731", dtype = "float64", shape = (12, 3, 14))#candidate|2731|(12, 3, 14)|var|float64
bop_2732 = relay.less_equal(var_2730.astype('bool'), relay.reshape(var_2731.astype('bool'), relay.shape_of(var_2730))) # shape=(12, 3, 14)
var_2737 = relay.var("var_2737", dtype = "float64", shape = (12, 3, 14))#candidate|2737|(12, 3, 14)|var|float64
bop_2738 = relay.subtract(var_2730.astype('int64'), relay.reshape(var_2737.astype('int64'), relay.shape_of(var_2730))) # shape=(12, 3, 14)
output = relay.Tuple([bop_2732,bop_2738,])
output2 = relay.Tuple([bop_2732,bop_2738,])
func_2745 = relay.Function([var_2730,var_2731,var_2737,], output)
mod['func_2745'] = func_2745
mod = relay.transform.InferType()(mod)
var_2746 = relay.var("var_2746", dtype = "float64", shape = (12, 3, 14))#candidate|2746|(12, 3, 14)|var|float64
var_2747 = relay.var("var_2747", dtype = "float64", shape = (12, 3, 14))#candidate|2747|(12, 3, 14)|var|float64
var_2748 = relay.var("var_2748", dtype = "float64", shape = (12, 3, 14))#candidate|2748|(12, 3, 14)|var|float64
output = func_2745(var_2746,var_2747,var_2748,)
func_2749 = relay.Function([var_2746,var_2747,var_2748,], output)
mutated_mod['func_2749'] = func_2749
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2783 = relay.var("var_2783", dtype = "float64", shape = ())#candidate|2783|()|var|float64
var_2784 = relay.var("var_2784", dtype = "float64", shape = (2, 10, 4))#candidate|2784|(2, 10, 4)|var|float64
bop_2785 = relay.power(var_2783.astype('float64'), var_2784.astype('float64')) # shape=(2, 10, 4)
func_2477_call = mod.get_global_var('func_2477')
func_2482_call = mutated_mod.get_global_var('func_2482')
const_2791 = relay.const([[False,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False],[True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True]], dtype = "bool")#candidate|2791|(2, 168)|const|bool
const_2792 = relay.const([True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True], dtype = "bool")#candidate|2792|(672,)|const|bool
call_2790 = relay.TupleGetItem(func_2477_call(relay.reshape(const_2791.astype('bool'), [7, 16, 3]), relay.reshape(var_2783.astype('int32'), []), relay.reshape(const_2792.astype('bool'), [14, 16, 3]), ), 1)
call_2793 = relay.TupleGetItem(func_2482_call(relay.reshape(const_2791.astype('bool'), [7, 16, 3]), relay.reshape(var_2783.astype('int32'), []), relay.reshape(const_2792.astype('bool'), [14, 16, 3]), ), 1)
output = relay.Tuple([bop_2785,call_2790,const_2791,const_2792,])
output2 = relay.Tuple([bop_2785,call_2793,const_2791,const_2792,])
func_2795 = relay.Function([var_2783,var_2784,], output)
mod['func_2795'] = func_2795
mod = relay.transform.InferType()(mod)
var_2796 = relay.var("var_2796", dtype = "float64", shape = ())#candidate|2796|()|var|float64
var_2797 = relay.var("var_2797", dtype = "float64", shape = (2, 10, 4))#candidate|2797|(2, 10, 4)|var|float64
output = func_2795(var_2796,var_2797,)
func_2798 = relay.Function([var_2796,var_2797,], output)
mutated_mod['func_2798'] = func_2798
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2869 = relay.var("var_2869", dtype = "float32", shape = (9, 15, 10))#candidate|2869|(9, 15, 10)|var|float32
var_2870 = relay.var("var_2870", dtype = "float32", shape = (9, 15, 10))#candidate|2870|(9, 15, 10)|var|float32
bop_2871 = relay.mod(var_2869.astype('float32'), relay.reshape(var_2870.astype('float32'), relay.shape_of(var_2869))) # shape=(9, 15, 10)
output = relay.Tuple([bop_2871,])
output2 = relay.Tuple([bop_2871,])
func_2874 = relay.Function([var_2869,var_2870,], output)
mod['func_2874'] = func_2874
mod = relay.transform.InferType()(mod)
var_2875 = relay.var("var_2875", dtype = "float32", shape = (9, 15, 10))#candidate|2875|(9, 15, 10)|var|float32
var_2876 = relay.var("var_2876", dtype = "float32", shape = (9, 15, 10))#candidate|2876|(9, 15, 10)|var|float32
output = func_2874(var_2875,var_2876,)
func_2877 = relay.Function([var_2875,var_2876,], output)
mutated_mod['func_2877'] = func_2877
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3012 = relay.var("var_3012", dtype = "float32", shape = (8, 8, 4))#candidate|3012|(8, 8, 4)|var|float32
var_3013 = relay.var("var_3013", dtype = "float32", shape = (8, 8, 4))#candidate|3013|(8, 8, 4)|var|float32
bop_3014 = relay.power(var_3012.astype('float32'), relay.reshape(var_3013.astype('float32'), relay.shape_of(var_3012))) # shape=(8, 8, 4)
func_1445_call = mod.get_global_var('func_1445')
func_1448_call = mutated_mod.get_global_var('func_1448')
var_3019 = relay.var("var_3019", dtype = "int32", shape = ())#candidate|3019|()|var|int32
const_3020 = relay.const([[-8,5],[9,-9],[7,-10],[2,2],[6,-10],[3,3],[8,-3],[-9,-2],[4,-7],[3,-1],[-9,-3],[-10,9],[-3,6],[5,-3],[1,-7],[5,-5],[1,1],[8,-6],[3,-10],[-4,-1],[-9,2],[-8,7],[3,10],[-5,4],[-9,-2],[6,-5],[-9,6],[-1,-10],[-5,4],[-7,5],[-5,7],[-9,10],[5,6],[1,-2],[4,6],[4,8],[10,5],[5,9],[-2,-1],[-7,-1],[-2,8],[8,-8],[8,8],[1,3],[9,1],[5,-3],[-8,2],[-7,2],[1,5],[-9,-10],[6,-1],[5,8],[-2,-8],[-3,-6],[5,-8],[2,-2],[-7,-10],[9,-3],[9,1],[8,10],[10,-8],[8,4],[3,-8],[10,-6],[8,-5],[-10,-3],[4,5],[-5,3],[2,10],[5,-7],[-6,3],[-6,4],[7,-2],[-10,7],[3,8],[-6,7],[2,2],[-1,-8],[-2,4],[-2,-4],[10,5],[3,3],[-4,5],[-10,2],[8,-1],[-10,8],[10,2],[10,10],[-1,9],[-8,9],[-3,-4],[5,-5],[7,-3],[-7,-1],[-5,-8],[8,-7],[4,3],[10,6],[8,-4],[-5,7],[-9,10],[-3,10],[5,-7],[7,-2],[-9,2],[10,-3],[-9,1],[-8,-5],[9,2],[8,4],[-1,6],[4,-6],[6,-4],[-8,-3],[4,1],[2,-10],[3,7],[-3,3],[-1,-9],[-9,-9],[6,9],[8,3],[8,5],[-9,-5],[6,-4],[-4,-10],[-5,9],[7,9],[1,7],[2,1],[-3,-3],[1,7],[-1,-6],[-9,1],[7,-10],[-10,-8],[-8,10],[5,3],[-10,-4],[-6,10],[-3,4],[3,8],[5,-6],[6,6],[9,4],[-1,-5],[3,4],[2,9],[-10,-7],[-8,5],[-2,10],[5,2],[4,-9],[2,6],[3,7],[3,1],[8,-8],[-3,-10],[6,-3],[-8,6],[-10,6],[8,9],[1,-7],[3,10],[7,8],[3,-7],[9,-1],[-4,6]], dtype = "int32")#candidate|3020|(168, 2)|const|int32
call_3018 = func_1445_call(relay.reshape(var_3019.astype('int32'), []), relay.reshape(const_3020.astype('int32'), [14, 12, 2]), )
call_3021 = func_1445_call(relay.reshape(var_3019.astype('int32'), []), relay.reshape(const_3020.astype('int32'), [14, 12, 2]), )
bop_3026 = relay.subtract(var_3012.astype('uint8'), relay.reshape(var_3013.astype('uint8'), relay.shape_of(var_3012))) # shape=(8, 8, 4)
output = relay.Tuple([bop_3014,call_3018,var_3019,const_3020,bop_3026,])
output2 = relay.Tuple([bop_3014,call_3021,var_3019,const_3020,bop_3026,])
func_3036 = relay.Function([var_3012,var_3013,var_3019,], output)
mod['func_3036'] = func_3036
mod = relay.transform.InferType()(mod)
var_3037 = relay.var("var_3037", dtype = "float32", shape = (8, 8, 4))#candidate|3037|(8, 8, 4)|var|float32
var_3038 = relay.var("var_3038", dtype = "float32", shape = (8, 8, 4))#candidate|3038|(8, 8, 4)|var|float32
var_3039 = relay.var("var_3039", dtype = "int32", shape = ())#candidate|3039|()|var|int32
output = func_3036(var_3037,var_3038,var_3039,)
func_3040 = relay.Function([var_3037,var_3038,var_3039,], output)
mutated_mod['func_3040'] = func_3040
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3116 = relay.const([[[3.249969,3.270749,6.740617,0.982232],[-6.113892,5.836549,-0.010513,-5.638765],[-9.721860,-1.629498,1.442091,3.623430],[-5.290113,-9.181507,-3.502480,2.884005],[-5.088394,8.185750,7.193492,-4.373997],[-5.671839,-9.640892,-4.172251,9.947585],[5.616960,3.882430,-1.540927,5.329227],[8.702754,6.857852,2.782436,-9.497452],[-3.994944,0.646745,-7.370321,2.408609],[2.049556,8.857889,-5.974318,9.095820],[-0.300262,-7.353774,1.532066,2.913941],[-7.822719,-8.542433,-9.450338,8.258967],[-4.279104,-6.925476,7.023319,3.300919],[1.931094,-7.694696,-5.670939,5.396361],[-1.021922,5.532787,5.545702,1.243417]],[[-1.736224,0.736950,-9.838095,3.318144],[-6.941805,7.534103,9.386759,-5.853533],[1.217801,-1.847143,-6.644852,-6.611954],[-5.015429,-3.736751,3.781887,9.596915],[4.230126,-1.651708,8.730013,-0.307853],[8.502552,5.379071,1.550248,0.710370],[-8.716947,-8.891397,4.155623,-1.597676],[-9.071545,-0.273464,-1.320601,9.197755],[-1.986576,7.922318,5.722028,2.787610],[2.204698,7.307640,7.952364,5.170836],[5.314086,-3.086329,-9.295637,-2.147281],[-1.804237,-6.350708,-9.348413,-9.793034],[1.958099,-7.202768,-3.044426,5.717670],[8.083759,-3.215226,5.629591,-5.917627],[0.323757,-9.990580,1.185424,-8.411930]],[[6.389282,-4.507692,8.281354,-4.452098],[-5.116445,7.579342,0.410809,-0.387541],[-0.610592,0.310780,-2.518389,-8.813495],[-2.728313,-2.189406,6.395148,1.706810],[9.479594,-0.719831,8.732865,-5.371748],[6.632482,-6.951217,-6.422445,1.193346],[6.395825,5.317073,4.430575,8.678774],[-5.788778,2.790614,-2.185290,-8.482818],[9.354873,-9.047848,8.496622,-6.454376],[3.495722,2.262089,-8.487957,-7.443564],[4.340233,0.766072,7.279334,4.837870],[-4.346455,9.046416,8.064336,3.381491],[-3.156265,4.475937,-2.767916,-2.996847],[-3.241577,4.293856,3.368060,-2.217951],[3.251078,9.108178,-1.459954,-6.494734]],[[8.514702,-7.173436,1.558577,6.395514],[6.954411,-6.039714,5.859732,4.633935],[-0.153710,-1.815247,-3.868125,8.922458],[-5.148670,-3.504066,3.721679,-4.258388],[-9.888772,2.324534,-5.706131,3.566417],[-4.790944,2.039313,6.469485,6.746661],[1.459101,4.125490,3.013947,-8.072323],[2.525703,-2.021500,8.385438,7.099055],[1.935804,-4.543426,-7.518817,-2.250484],[1.373742,-2.028848,-7.399118,-9.778732],[2.887376,-0.195109,-4.212323,-3.112009],[2.543035,-0.045147,3.087252,9.307653],[0.927093,-2.493184,2.545963,-7.105813],[-9.859170,5.733517,-6.150595,7.393364],[2.494194,-6.686767,-5.111265,1.024465]],[[-6.221444,-1.818771,-6.694544,-4.876951],[4.705395,2.461228,0.939970,5.882610],[-6.981147,6.547282,3.344769,-8.798155],[-7.652103,-6.355485,7.859376,-5.667041],[-3.841260,-7.169491,-0.158578,-8.457353],[1.341138,3.267308,3.941617,5.171076],[9.091697,-3.239788,6.071308,-3.864644],[-4.434538,-8.300574,-3.057864,1.122325],[8.133050,3.459099,-5.324422,-8.734248],[0.665105,1.224605,-3.583891,-4.238291],[5.842371,-8.678523,2.377471,-0.824909],[-4.127425,-0.496851,5.599238,0.537077],[8.797972,0.368336,-8.282826,0.145841],[3.606504,-2.503477,2.112902,9.034305],[9.769340,1.703306,-8.390207,-8.584051]],[[-6.832371,-7.068052,-7.140821,5.459014],[-7.473401,-7.643958,-2.892793,8.121788],[-7.500887,2.581923,-5.345831,-1.805101],[1.631691,8.687125,8.518525,-5.743349],[-6.680281,3.906574,-2.673303,-9.998032],[7.388118,1.262773,-8.086654,6.462324],[-5.962658,1.004408,-1.461257,-1.551416],[8.412521,6.565273,-3.757074,6.408854],[-9.438085,3.369426,3.391086,-5.730620],[-0.875795,-5.812159,-8.499164,6.730993],[-0.096380,2.994749,-4.983731,-4.235410],[2.742859,-7.432879,9.213715,-2.710552],[6.053914,-1.932934,3.204257,7.233928],[-7.530514,7.937305,-0.310754,4.770312],[4.223016,8.835282,2.513792,7.094305]],[[8.529307,-2.619021,9.255401,8.858918],[-5.450535,8.949582,-4.804069,-4.764249],[-6.813927,6.630765,-4.055505,-7.291638],[2.628408,-7.981952,3.654196,-5.114341],[1.438338,-1.599067,6.629194,3.875758],[1.650251,-9.424611,-6.363672,6.357925],[-4.774812,5.708795,0.851990,-1.848715],[6.762278,9.989271,-7.776584,6.117937],[-2.031335,7.606641,7.047753,-3.365571],[2.869246,-4.231352,8.423334,9.683957],[-6.562816,-1.081895,-8.537187,3.610443],[2.001052,-4.219831,-6.857806,-4.470171],[0.047735,-5.791334,-0.967634,-3.605535],[7.196153,1.446586,-6.921340,-7.924712],[7.244045,-8.961960,9.699593,4.659244]],[[4.629135,8.859070,-6.104575,-2.561725],[2.321261,-0.244255,3.754254,6.412119],[-2.325819,0.413457,7.239219,4.081332],[6.526986,-3.642848,8.993747,1.026504],[-6.558510,-9.611508,-9.971989,-0.909875],[-7.223777,-2.337295,7.126210,-5.565232],[-4.778448,-7.238942,-4.821290,9.253794],[-2.284239,-2.248820,1.102332,-7.036278],[-0.228370,-0.587338,7.298493,-0.661501],[-3.844235,-7.204423,7.133053,3.278481],[-2.664721,7.149687,3.636855,-6.244216],[5.027105,-3.186304,6.516048,-1.949586],[8.874202,-1.879628,1.617106,-2.236469],[8.703458,-4.354117,-1.397310,1.781336],[6.886880,6.712157,6.836875,-3.302605]]], dtype = "float32")#candidate|3116|(8, 15, 4)|const|float32
uop_3117 = relay.cos(const_3116.astype('float32')) # shape=(8, 15, 4)
output = relay.Tuple([uop_3117,])
output2 = relay.Tuple([uop_3117,])
func_3130 = relay.Function([], output)
mod['func_3130'] = func_3130
mod = relay.transform.InferType()(mod)
output = func_3130()
func_3131 = relay.Function([], output)
mutated_mod['func_3131'] = func_3131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3180 = relay.TupleGetItem(func_3130_call(), 0)
call_3181 = relay.TupleGetItem(func_3131_call(), 0)
output = call_3180
output2 = call_3181
func_3182 = relay.Function([], output)
mod['func_3182'] = func_3182
mod = relay.transform.InferType()(mod)
output = func_3182()
func_3183 = relay.Function([], output)
mutated_mod['func_3183'] = func_3183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3265 = relay.TupleGetItem(func_3130_call(), 0)
call_3266 = relay.TupleGetItem(func_3131_call(), 0)
output = relay.Tuple([call_3265,])
output2 = relay.Tuple([call_3266,])
func_3274 = relay.Function([], output)
mod['func_3274'] = func_3274
mod = relay.transform.InferType()(mod)
output = func_3274()
func_3275 = relay.Function([], output)
mutated_mod['func_3275'] = func_3275
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3279 = relay.const([[[-8.966140,7.760417,4.999321,-5.641833,-2.945681,-6.749126,-3.920730,-6.403665,1.697086,1.021547,-4.500363,1.818465,7.114678,-1.161463,2.541774],[5.813102,1.119966,-7.469591,6.488144,-8.098098,-8.992944,1.381719,8.048090,8.820943,5.612677,-3.079830,7.575602,-3.920777,-4.496466,4.358687],[-5.284268,6.059608,-8.258161,-9.962907,-7.672198,5.295938,7.968072,-6.662076,-6.519808,0.295999,-8.530006,5.182859,-9.972149,-6.144960,2.298875],[-9.203577,-9.688750,1.860659,8.062653,-1.352890,-1.002481,-7.254631,6.883227,-9.773256,-8.356547,8.147893,-0.665057,-2.552216,9.615089,6.908287],[5.076123,-8.707824,-4.367431,-8.371857,-4.274102,5.103625,-7.028853,-9.405501,-2.847985,-9.222297,1.188975,4.794150,-5.874603,-0.365127,1.404428]],[[-0.189196,8.408983,-1.952980,7.740868,1.278553,-9.078975,-3.167547,-4.088036,-1.884533,-4.642055,1.606187,-0.159399,6.723176,2.664084,-6.929154],[4.837204,8.247876,-3.829505,-6.811992,-1.603131,6.141375,1.604298,1.194241,-9.869267,-4.258835,-0.786824,-6.150603,6.451084,-5.071581,7.873248],[3.298295,8.529433,5.206856,-8.278606,4.787246,7.025863,7.991204,0.384320,-6.200596,-5.354220,-6.148167,0.484473,-1.470340,-4.012260,9.523053],[5.591998,-0.787290,3.173613,-1.223288,-2.716774,-9.066107,-0.978659,-6.068784,-3.693373,-0.295029,8.234631,-6.432284,1.795705,2.394173,5.772430],[-7.501047,0.825132,3.640139,-4.697130,6.070127,-4.291246,0.957540,2.230126,-4.617833,-7.293971,4.374905,0.113130,-7.029115,-2.337577,-0.652101]],[[-8.565783,-1.085439,8.638153,-8.491500,-5.297057,-4.494195,1.691081,8.445816,2.183302,7.110493,-5.619511,-7.244291,-3.442147,9.604202,-6.038798],[-6.844098,-7.971008,1.605561,-8.668915,2.426783,1.571587,8.863549,5.711645,0.057211,-3.274157,9.759016,4.644848,-4.327238,-0.995404,-7.763631],[7.833456,-4.974714,-8.021133,-2.824369,6.419277,4.695360,1.614423,-9.055292,5.391276,-0.044999,-8.427474,7.933955,1.092834,7.866784,0.410202],[-3.464761,-5.548009,-0.021139,-6.968100,5.997344,-5.760826,-4.169786,-3.064691,4.779283,1.865395,1.915868,4.766022,0.863213,6.240462,-7.548033],[0.417128,5.070611,3.898725,-4.092873,-9.745936,-8.682623,-7.408886,2.097368,8.989044,-7.612234,-8.351724,-8.599357,-5.481191,-3.365067,-5.509264]],[[-7.365190,9.384344,2.248765,7.134370,9.550249,8.379882,6.491008,-8.938047,-5.696884,3.114117,-6.737102,8.975174,7.059394,9.140297,5.287499],[-2.384526,1.224299,0.216975,6.969600,-7.202274,0.405782,-9.819910,0.073397,3.247144,-9.901919,-3.852682,-5.255241,4.024521,-6.122468,2.682224],[-6.414233,8.321755,3.288604,-3.443788,-2.162127,8.237887,-0.319609,-4.218855,9.068667,-4.062856,-4.680493,-6.177754,-4.250209,-4.139049,-3.784829],[-0.978459,4.645993,-7.279309,-0.850032,3.978951,1.060880,-1.624914,-4.742633,2.455036,-7.654163,3.168495,3.675687,7.055620,6.665228,-5.870777],[5.788755,-9.350832,-0.638211,-3.521768,4.638729,2.288524,-5.326957,3.218486,-8.765867,-3.913905,-8.496810,0.510781,-8.053271,6.408842,-5.493865]],[[7.581788,-1.272489,3.800501,3.429722,2.119796,3.569286,5.231942,5.385444,9.406256,-3.103307,-8.464426,1.212926,-7.508983,8.467895,-1.632963],[8.155727,6.204427,5.885289,-1.731487,-4.213231,-1.828268,1.846872,-8.851104,-4.526194,-4.591161,7.085697,1.017516,5.376546,-8.072227,4.697149],[-0.547036,4.216795,-5.060355,-2.446140,0.925211,-5.737492,3.414038,1.428296,-9.417303,1.234606,-3.073482,-7.999467,8.879820,4.938481,-6.294482],[-6.337717,2.818668,-7.081950,2.377716,7.336862,-4.151740,-4.341328,4.149613,2.690949,9.636035,-5.629309,9.425887,0.099845,-8.299129,4.552999],[8.221392,-4.070687,1.453299,-1.353402,3.838788,5.829184,5.112525,2.470222,9.625191,0.684019,8.921030,0.805262,-5.661324,-7.259626,4.291083]],[[8.322390,2.756529,-6.661991,-5.695509,0.969235,-6.756054,4.276917,-9.823286,-6.945653,8.896489,-4.220013,4.928503,-1.095860,-7.244444,2.035689],[-9.134230,-9.244285,-8.756275,-4.248337,3.666624,-9.077231,-1.036122,-3.438379,1.523325,-4.824514,-9.892870,8.818932,-3.884241,6.101441,-7.626973],[6.778180,2.889047,5.638999,-8.568438,-9.791263,1.493642,6.808171,1.889938,1.734351,-0.077468,3.095004,-7.056625,-1.435967,-1.545936,-8.187737],[-1.859904,9.678643,5.757801,9.155888,-7.889137,-9.951771,1.249282,3.040226,6.650449,7.567013,3.550954,-9.480857,0.019118,-6.728908,-7.111538],[9.262098,-6.959927,-5.769102,6.902097,0.877577,0.244687,5.465917,0.073452,6.698448,0.152462,-1.940495,-3.872845,5.387371,-0.202781,9.906825]],[[-5.131093,1.014527,-2.546151,-0.080329,-5.449792,9.253305,1.955483,-8.210298,-7.258122,0.713333,-0.686880,-9.838749,-2.431686,-1.948889,2.385578],[9.595478,-8.064891,6.659595,-2.786360,-1.816136,3.274828,3.450701,8.450626,-1.973283,9.158162,1.448825,0.801469,-3.772757,5.883122,-1.004136],[4.178220,-2.874971,6.346180,-9.591974,-3.763206,-6.884948,-2.971037,-6.226878,6.292287,4.051545,8.097705,-6.905434,-8.412670,-6.292458,9.110994],[5.513927,5.918744,4.617667,5.071405,-0.726256,-4.564453,0.182426,-6.176114,-4.444925,-1.236642,5.215975,1.883223,6.754768,-9.924645,2.330432],[-5.879301,-4.174074,7.467643,-2.526580,1.832095,-9.133367,4.964252,8.757651,8.410369,9.136946,5.987883,8.274119,-4.666839,2.123840,6.343945]],[[8.015413,3.664042,5.410375,9.263958,9.795037,-3.179815,-8.511943,4.724754,-3.650864,-5.225111,2.206231,-9.020902,-2.018538,0.864480,7.802595],[-0.921920,-0.364656,6.739159,-9.980910,-6.592509,6.790788,5.773055,-6.977658,4.816919,-9.849534,6.027227,-3.492725,-3.280193,-3.150140,-7.810486],[-8.324333,-8.561301,-8.978763,-7.621881,-4.356987,-1.683395,-3.864802,-4.926213,-9.552596,8.844436,0.551037,-3.380833,-7.681720,-2.341649,-3.565639],[-4.966378,9.339631,-6.824168,-0.283477,1.456941,4.413401,5.545210,7.933524,-6.407951,8.794119,-9.640857,-5.667432,-5.537008,-9.774745,-1.969320],[0.715630,2.837944,7.191777,-4.050439,8.423015,7.741792,3.496038,-8.643435,-3.456456,5.497946,-2.602970,-0.127563,-3.784182,5.707796,9.783226]],[[-6.120550,-0.077029,7.595468,5.260553,-3.243104,1.658482,7.270475,-3.815450,-7.571208,-4.208494,-6.492629,9.313629,-6.961923,-9.187364,-8.074728],[2.176821,-1.265326,5.819594,3.261192,-0.929895,9.926352,7.519108,-1.512650,-0.080738,-3.274366,-5.280533,2.868609,1.207880,-3.926767,9.494140],[8.872076,3.719255,-0.907014,-6.919534,8.871645,0.334514,-6.345766,0.561994,-9.803432,3.544154,-5.129867,-3.482140,-3.053641,3.737773,6.839572],[7.831932,6.005368,-3.507858,5.460590,-6.592668,6.212012,2.119716,-8.905758,9.458095,-8.312393,-9.406902,-8.633547,-0.670399,-9.647578,1.067823],[-9.238793,0.340662,0.981783,-7.569304,-8.836094,5.576330,-1.249809,3.537725,7.159057,-0.679890,-4.146615,9.254438,0.201606,2.533245,1.352422]],[[7.645106,9.485814,-9.553603,-7.423466,-0.863672,3.426585,2.677957,-9.309519,-5.577214,5.653292,-1.017607,9.739275,-7.675434,2.330192,9.582412],[6.617785,1.124152,0.651589,1.799360,-6.627390,-9.659487,-4.130217,8.260951,-0.524332,-9.851466,-4.761913,7.877655,-8.408406,-3.149781,8.998444],[9.035630,-4.304690,-7.480234,-0.767278,-4.444494,4.704298,-0.640166,-1.629771,-1.207330,1.798562,-9.840211,3.513915,-2.065389,3.472184,-0.470142],[-5.876889,2.666731,-5.961698,-0.363770,-1.498647,8.843789,6.042523,5.555547,2.204231,-4.936359,-5.310693,5.935391,8.958437,-7.543724,-8.087869],[5.049289,-4.593788,-6.776220,-7.998736,8.427973,2.468085,-9.672587,-4.494894,-5.738798,-9.264573,-5.268742,8.090976,-2.893245,2.786108,0.185664]],[[1.147768,-3.086016,-5.172003,-5.121475,6.152697,8.276832,-7.903248,7.943350,5.266970,9.152287,0.511842,-9.462757,4.626352,9.747934,2.149648],[-1.360087,1.931204,-4.338273,7.873915,7.398015,-3.141115,2.929971,-7.078523,6.493396,-3.290526,2.964775,8.991970,-4.664382,6.027350,4.362195],[9.886357,1.816413,1.493968,-0.525045,7.752852,8.714168,-5.547078,-9.109313,-7.911582,-6.295086,-4.473462,-6.710672,2.669781,-8.377864,-9.924957],[-2.802881,-4.118496,-0.581922,5.903313,-1.481490,-2.176066,7.555103,6.155567,-9.717814,3.624023,-6.407954,-0.863647,4.074621,-9.247285,-8.353030],[-3.911614,-3.715050,1.965119,-1.221588,9.934529,3.123714,-7.135301,-7.668238,-7.470785,2.446814,4.798250,-2.062096,-3.313959,8.240477,7.794233]],[[2.591054,-5.363140,-9.321060,8.516097,3.371980,-3.519598,-4.167119,9.112298,-9.026970,6.034813,0.024441,9.869384,5.015443,-2.374629,-8.500350],[-0.203947,9.871483,3.437811,-6.457549,-5.733323,9.459767,-9.068798,7.283807,-1.663562,-0.527804,-1.039327,-2.904697,9.703626,1.758450,6.158147],[5.896421,-3.894931,-5.670330,8.512108,-8.325724,-0.329154,-4.909980,1.483389,-4.363015,4.168645,-8.762380,7.832076,7.792087,-2.734404,-9.470393],[4.704570,3.345288,-2.628773,0.113593,0.512202,3.308468,-8.024341,-2.919919,7.149758,5.206987,5.363534,-2.323559,8.559139,9.542980,4.923671],[6.598321,-8.331135,-6.925389,-4.938948,-9.671876,0.385958,-6.415912,8.541857,1.571053,2.455188,7.087164,-1.644654,2.168136,9.639444,8.362795]],[[-3.787245,2.015498,-1.583696,3.207464,-7.768718,-4.241458,7.229803,2.605331,0.993109,-2.225869,7.716780,-0.292071,0.123471,4.751391,-9.658345],[1.695580,3.002850,1.815947,-1.657180,4.109201,-6.603107,-3.667264,-3.075355,-3.373391,8.247115,-4.396167,-9.297185,-4.802022,5.699544,7.314281],[8.429002,-5.737902,1.226801,-0.135951,2.746378,-6.753204,0.153402,6.466886,-7.713589,7.208835,-2.147535,4.320250,-2.308631,0.987692,7.311901],[-7.773233,6.883915,-2.381896,-8.510506,7.392094,-1.307252,-5.310293,-0.520798,1.568273,2.245853,-7.101381,-2.979749,8.532775,-1.885893,-5.249724],[7.352339,-2.254996,-5.762489,8.665711,4.222674,-3.278335,1.916476,6.701199,-6.208602,-6.872275,1.570678,-4.874412,-6.199582,4.078389,-3.813823]],[[2.932875,-5.505669,-0.417272,-1.923640,7.985595,-4.092543,3.905450,-7.686194,-5.386927,4.839707,3.670647,5.491066,-5.300993,9.078226,-3.054444],[-1.667663,8.595671,8.377433,1.052759,5.470898,7.659939,-1.249813,7.677312,8.547108,9.443262,3.687827,-8.292943,-7.203086,-3.946711,-9.673515],[3.548872,-9.456379,3.875041,6.212219,7.206511,7.777380,-0.919821,8.061726,2.050091,6.458706,1.850412,2.440835,-4.113339,4.102608,8.860268],[8.551058,-2.258178,8.666526,-2.870609,-1.486621,2.582042,-4.800606,0.083957,-4.937063,2.834840,2.267012,-3.549051,-5.099010,7.981198,4.476240],[2.394818,0.294067,5.535725,3.705888,2.184413,6.165445,5.892932,9.694227,-7.816229,8.073636,3.246065,-2.147965,1.559955,-2.300076,-3.749623]],[[2.718577,8.314434,3.686437,1.375934,-2.571206,-4.673442,-7.851275,7.775731,-7.069923,2.230141,2.201593,6.091835,-1.228063,-5.999041,7.736815],[-4.091265,-4.800719,0.600094,-5.825553,-1.612358,-2.829332,8.633219,6.924223,-2.759580,-1.324725,1.514355,-0.936306,1.614500,-4.807599,-5.304504],[3.997524,-3.562354,-5.559078,8.679688,1.229244,9.350654,0.297137,-2.553860,8.418832,-0.289311,-6.096804,-7.447031,-1.729501,8.603699,9.857893],[-0.279156,-3.641993,1.986170,1.775011,-9.160162,-0.355609,-1.141494,-2.367393,-4.623014,9.081777,9.112643,9.695345,-6.426346,9.751803,-3.411276],[8.609276,8.463340,6.088679,-3.515686,-1.215388,6.170501,-3.123651,-3.222861,-8.089034,9.809747,8.440144,0.843684,-8.063930,1.353841,1.914041]],[[-5.345602,-6.947689,9.294057,-3.931220,-3.613602,-1.091470,-7.659955,9.975695,8.083013,6.219826,7.953897,8.738956,3.419886,6.209182,6.547569],[-4.738903,1.961528,-3.727451,4.253640,2.600895,5.690211,8.217617,-8.573552,-4.120334,0.192137,-0.711070,-0.314902,3.872802,1.698040,-8.849833],[-0.900918,0.995624,-4.056898,-4.856927,-9.221251,1.147598,3.672650,7.880892,-5.046258,7.433619,-3.103561,-1.345026,1.156470,-8.545824,-1.386407],[8.087787,-1.886051,5.485946,-1.991633,-2.611365,0.935963,-3.007468,-5.223593,-7.605158,2.368672,-1.622027,-2.598692,4.998963,9.123606,-6.137718],[-5.844878,-9.754371,-9.638775,9.874562,8.041983,-1.475458,-4.845834,6.485032,-3.796244,3.594777,3.513917,7.986364,-0.173320,6.950964,9.575078]]], dtype = "float32")#candidate|3279|(16, 5, 15)|const|float32
uop_3280 = relay.sqrt(const_3279.astype('float32')) # shape=(16, 5, 15)
bop_3282 = relay.less(uop_3280.astype('bool'), relay.reshape(const_3279.astype('bool'), relay.shape_of(uop_3280))) # shape=(16, 5, 15)
func_2745_call = mod.get_global_var('func_2745')
func_2749_call = mutated_mod.get_global_var('func_2749')
const_3295 = relay.const([[5.327146],[4.325517],[-8.218879],[2.773090],[-2.151939],[0.981472],[-2.387885],[-2.955678],[-6.716441],[-6.073835],[-9.960757],[-1.603892],[-3.924851],[5.763409],[-9.275982],[-0.998009],[5.690913],[-6.710260],[8.630283],[4.347005],[3.686040],[1.565970],[7.547217],[-0.139920],[0.568097],[3.314304],[4.688188],[5.417830],[6.491765],[-2.715101],[7.725956],[4.701082],[6.164218],[-5.838099],[-8.415025],[-4.368297],[-9.332476],[3.500945],[7.932532],[-0.186562],[-3.634557],[6.651586],[5.961883],[0.783064],[7.344551],[-0.509082],[-4.384204],[-7.415195],[-4.473923],[-2.620001],[-5.325078],[-8.080685],[-0.693862],[2.357042],[4.390566],[6.554384],[5.501018],[-7.459273],[2.181230],[-6.858640],[6.279177],[4.911351],[-0.403554],[3.940114],[-1.056638],[0.476183],[-7.995712],[-7.731668],[2.617181],[4.381936],[8.921702],[-7.416950],[2.041782],[8.511976],[-0.041480],[4.604265],[5.890987],[4.466074],[-7.595951],[-3.706222],[8.579448],[-9.305977],[9.502580],[-5.862290],[-9.737199],[-8.413916],[-4.062956],[-4.997669],[2.949512],[-0.420880],[8.536352],[2.280760],[-9.165950],[0.418021],[-8.196375],[-8.605650],[7.549340],[5.760404],[8.509837],[-8.640947],[4.539233],[7.755070],[5.886087],[4.432987],[9.394553],[2.158587],[-0.080304],[7.807318],[5.586765],[3.313908],[-7.526186],[3.481894],[-5.869081],[6.040419],[6.839941],[2.596494],[-9.027498],[-0.870642],[0.048684],[-2.832935],[-5.355402],[7.854715],[-3.073741],[0.729712],[6.040207],[6.146026],[-6.719591],[-1.280110],[-5.233117],[-3.251062],[5.033259],[-5.950111],[-0.633196],[8.652155],[0.754036],[7.773809],[8.400327],[-2.268335],[1.800711],[-2.913710],[-1.935347],[0.453190],[-3.574964],[-3.509219],[8.914228],[-3.388123],[-4.194570],[-8.698671],[-6.839742],[-7.196286],[6.660640],[3.632605],[0.325907],[-1.275528],[5.973917],[3.590494],[7.983244],[9.834737],[-4.818313],[-2.646328],[-7.484984],[-3.036544],[2.665578],[-0.812232],[9.562640],[7.994998],[-5.444241],[0.917400],[-3.845114],[-3.692827],[-8.989329],[-4.856643],[-4.354813],[-5.034768],[3.188669],[-0.235411],[4.704150],[-7.211635],[8.245514],[-6.786826],[-1.044900],[2.453211],[-6.660991],[-7.943592],[8.513242],[8.950821],[-5.428229],[1.608049],[6.332191],[-9.969363],[-9.207224],[-3.191812],[3.610199],[-5.812715],[4.667639],[7.751795],[2.341486],[-7.049594],[-1.457725],[-8.303150],[-2.015768],[9.907415],[3.007306],[5.080511],[-7.133846],[9.171324],[9.640492],[3.375896],[3.847989],[5.648512],[-9.312613],[-5.153662],[-3.927481],[-1.050530],[8.001917],[-5.954016],[-6.003447],[-5.841345],[-5.114525],[-8.644747],[6.879424],[1.519778],[8.521093],[-9.968394],[-2.543570],[-7.102839],[-4.001297],[-0.163118],[8.471846],[8.232195],[-3.937111],[-1.826711],[-9.930660],[-9.564531],[5.408398],[9.005883],[1.180338],[2.710919],[0.309843],[3.036434],[0.976174],[9.376992],[-3.914911],[-5.339791],[-4.404992],[-5.478893],[9.768049],[7.609898],[1.796844],[-9.655556],[-6.406708],[-1.685120],[-9.016631],[-5.738301],[8.550421],[-1.552086],[2.067785],[-4.395518],[7.960874],[-7.422843],[9.269275],[-9.916305],[7.263890],[-0.431256],[-5.919864],[3.171915],[-9.063412],[-3.565247],[9.465227],[4.852685],[-1.833475],[-9.780439],[3.690552],[6.212077],[3.545782],[-0.498915],[-0.174899],[-5.803574],[-9.515380],[-6.945146],[9.316449],[6.957018],[5.393857],[8.788122],[-3.845906],[9.496106],[-6.728035],[6.524061],[6.067746],[-0.243023],[-4.801715],[2.877546],[-7.043873],[-1.862066],[-4.227135],[8.878113],[5.438630],[1.441484],[-5.216048],[6.317458],[0.017174],[9.467412],[-0.992365],[1.576967],[1.307825],[1.978403],[-4.353826],[-7.472588],[-8.021984],[4.288659],[1.714302],[-1.499598],[8.996132],[-2.807393],[-1.862859],[1.191872],[-0.493272],[2.868832],[4.443274],[-7.137440],[5.416054],[-4.301159],[-1.038064],[-1.690290],[4.264182],[5.007215],[-3.470387],[5.077740],[-0.070395],[0.567295],[-6.019288],[-0.983954],[8.224216],[5.705729],[0.433067],[0.804443],[7.694624],[-1.360417],[-0.546498],[-5.231315],[9.838177],[-8.288652],[-9.319017],[5.122291],[0.350793],[1.984337],[5.756872],[3.582505],[-8.682467],[7.563710],[-4.968434],[-2.354391],[-8.951550],[-3.240948],[5.757916],[3.389814],[-7.170658],[-4.524884],[3.480476],[9.570806],[-8.332280],[-7.737636],[6.474321],[-1.646533],[2.173001],[3.211177],[-4.321126],[2.712925],[-9.612218],[8.423055],[1.056254],[-1.543591],[-1.532316],[-9.273642],[0.734840],[7.497275],[-8.279282],[0.093526],[8.761307],[2.791863],[-6.099591],[-4.090269],[-7.069552],[1.579688],[6.624257],[-2.140104],[0.912906],[9.405917],[1.136585],[-7.595937],[3.060645],[-5.438659],[4.542849],[6.103110],[6.959938],[1.815573],[6.235082],[-4.209371],[-2.470729],[2.318077],[-5.252297],[-8.783291],[-7.168720],[-1.142002],[8.023793],[-3.848840],[-8.506406],[-4.707011],[5.087347],[-9.078710],[5.044221],[-1.908523],[0.540471],[-3.486784],[-4.366038],[-6.078395],[-4.629106],[4.687883],[-3.307538],[-4.433643],[-4.496547],[-9.527115],[-0.081348],[-1.629340],[0.080070],[-8.573449],[6.090372],[6.684144],[-9.990745],[-3.648338],[3.954169],[1.743290],[3.496307],[1.721188],[-8.621621],[1.967767],[-8.644261],[0.316374],[-2.288099],[-8.610483],[-2.075179],[-3.418731],[2.298254],[5.628347],[-9.535525],[3.350777],[-9.510905],[8.849749],[3.439028],[6.254152],[-5.491146],[-5.433288],[-4.434298],[1.226867],[1.897339],[-5.338084],[7.020239],[7.272289],[0.511729],[-4.873995],[-8.846130],[1.205536],[-4.772379],[-0.589118],[0.544956],[-9.917896],[-8.360274],[8.702008],[-3.598145],[-3.286326],[-2.043999],[-9.846309],[0.809399],[7.019415],[-7.833653],[-9.617214],[1.211409],[9.621358],[-3.188687],[0.674086],[8.992423],[-7.494528],[-6.691278],[-8.039999],[-4.926360],[-2.399255],[-7.872525],[-8.245823],[9.603474],[-9.433112],[1.331700],[-3.261514],[-5.588323],[0.752175],[-6.297859],[8.157525],[-1.453354],[5.910304],[1.206079],[9.019660],[-5.110201],[-1.073366],[-2.968183],[2.209371]], dtype = "float64")#candidate|3295|(504, 1)|const|float64
call_3294 = relay.TupleGetItem(func_2745_call(relay.reshape(const_3295.astype('float64'), [12, 3, 14]), relay.reshape(const_3295.astype('float64'), [12, 3, 14]), relay.reshape(const_3295.astype('float64'), [12, 3, 14]), ), 1)
call_3296 = relay.TupleGetItem(func_2749_call(relay.reshape(const_3295.astype('float64'), [12, 3, 14]), relay.reshape(const_3295.astype('float64'), [12, 3, 14]), relay.reshape(const_3295.astype('float64'), [12, 3, 14]), ), 1)
output = relay.Tuple([bop_3282,call_3294,const_3295,])
output2 = relay.Tuple([bop_3282,call_3296,const_3295,])
func_3314 = relay.Function([], output)
mod['func_3314'] = func_3314
mod = relay.transform.InferType()(mod)
mutated_mod['func_3314'] = func_3314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3314_call = mutated_mod.get_global_var('func_3314')
call_3315 = func_3314_call()
output = call_3315
func_3316 = relay.Function([], output)
mutated_mod['func_3316'] = func_3316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_3353 = relay.TupleGetItem(func_3274_call(), 0)
call_3354 = relay.TupleGetItem(func_3275_call(), 0)
func_546_call = mod.get_global_var('func_546')
func_549_call = mutated_mod.get_global_var('func_549')
const_3358 = relay.const([2,4,-8,3,-4,5,10,1,9,6,6,8,6,-4,-8,3,-4,3,5,8,-9,-5,4,-8,9,-5,-9,8,-4,8,3,1,-2,3,-2,-7,1,-2,8,-10,-6,-4,7,-10,-2,4,-4,5,1,3,9,4,2,7,-6,8,1,6,-2,10,9,-1,10,8,6,-5,-1,-4,-7,-6,-9,6,6,9,-10,-4,-6,-1,3,-8,-3,3,-3,9,-10,-4,9,1,4,5,-3,-5,4,-3,-7,5,3,-4,-4,8,-7,-3,2,4,-5,2,-8,5,2,8,-1,7,-8,2,-3,-6,-1,-9,-2,-9,-9,-7,7,-8,1,6,6,6,6,6,8,-10,-10,2,-1,10,-1,7,-8,6,-1,-3,-8,1,-7,-3,-8,4,3,9,-8,-4,-6,8,7,5,-6,5,9,10,-4,1,-8,-7,2,7,-4,10,3,8,-9,8,-1,-1,-10,6,-6,3,5,-6,-5,-8,3,3,-3,-6,1,-2,-6,5,-6,7,2,-5,-1,4,6,-6,-10,-3,-7,-9,-2,5,4,3,2,3,9,1,-10,7,-6,3,2,-1,6,1,1,-5,7,6,-7,5,6,7,10,-10,-6,4,-2,9,5,7,6,-2,9,4,4,3,3,5,-3,-4,1,-9,5,2,-7,-7,-10,-6,4,6,-9,-9,10,-8,1,6,-9,5,-2,-3,6,2,6,7,-9,-1,4,1,-6,-9,-10,-10,-9,-1,2,7,-4,3,6,4,-5,-4,-5,-4,-3,-7,-9,9,2,6,6,3,4,-1,-8,-8,8,-1,-6,-3,10,-9,8,7,-10,7,8,-5,6,5,-9,-8,-4,1,5,-6,-7,-4,-4,7,3,9,4,6,-10,-5,-5,-7,1,6,3,9,-10,4,-3,8,-7,-9,-3,-2,-7,5,9,10,1,3,9,-3,-6,-5,-2,-7,1,9,-3,10,-9,2,6,-5,8,-2,-2,8,-4,9,7,4,-3,4,7,10,9,-1,5,-2,3,-2,9,-5,4,-10,3,8,10,-6,8,-10,-7,1,-6,-5,-7,6,-10,10,8,-6,5,-8,8,9,-7,2,-9,-6,-4,-3,-1,-8,9,-4,9,7,3,-6,-9,-8,3,2,1,-4,-10,-9,-6,-1,-4,-4,-4,6,6,10,-6,-2,10,-10,4,7,2,5,2,5,-1,-10,1,4,-7,-5,-5,-9,-2,6,-4,-10,-3,-4,-2,-3,-9,-8,9,10,-8,-7,3,-8,7,-1,-10,-7,5,-8,-10,2,3,2,1,8,-6,-4,4,-3,7,2,-2,-10,10,-8,10,2,7,7,-5,-1,1,9,7,-6,6,4,7,-9,-4,7,-4,-9,-2,-2,3,-7,7,2,10,10,6,-5,10,9,-8,1,-5,4,-7,4,10,-6,1,-2,-6,8,8,6,-7,5,-3,-9,5,8,2,3,5,-10,5,-9,6,-4,3,4,9,7,-6,-10,2,4,-10,-5,-4,5,-8,-2,-4,-1,-8,-8,6,9,-2,4,7,-7,3,-5,-8,8,-7,-2,-9,-9,-2,4,-2,10,1,7,2,-8,7,-5,6,-3,-6,-5,10,1,-2,-9,-7,-8,5,-10,-1,-5,4,5,3,-2,-5,-3,-10,8,-9,-6,-8,-7,-4,-1,5,-5,-5,-8,10,-7,-6,3,-5,10,10,10,-4,2,-4,-3,10,-8,8,-5,-6,7,-3,10,1,-9,9,8,6,1,6,9,-10,3,4,10,8,-2,8,-8,5,10,7,-7,-10,5,2,2,-2,2,10,-6,9,-1,3,6,7,3,-3,-10,-1,-7,-8,5,-1,-8,10,1,-3,8,2,-5,7,-4,10,-3,9,-4,-10,-1,-7,-4,-2,-8,-7,-4,-8,9,-8,-8,-9,1,-5,-6,-5,6,3,-1,-6,3,-5,4,5,3,-8,-4,-3,4], dtype = "uint8")#candidate|3358|(728,)|const|uint8
call_3357 = relay.TupleGetItem(func_546_call(relay.reshape(const_3358.astype('uint8'), [13, 4, 14]), relay.reshape(const_3358.astype('uint8'), [13, 4, 14]), ), 1)
call_3359 = relay.TupleGetItem(func_549_call(relay.reshape(const_3358.astype('uint8'), [13, 4, 14]), relay.reshape(const_3358.astype('uint8'), [13, 4, 14]), ), 1)
var_3367 = relay.var("var_3367", dtype = "float64", shape = (14, 9, 12))#candidate|3367|(14, 9, 12)|var|float64
bop_3368 = relay.right_shift(call_3357.astype('int16'), relay.reshape(var_3367.astype('int16'), relay.shape_of(call_3357))) # shape=(14, 9, 12)
bop_3371 = relay.right_shift(call_3359.astype('int16'), relay.reshape(var_3367.astype('int16'), relay.shape_of(call_3359))) # shape=(14, 9, 12)
uop_3374 = relay.erf(call_3353.astype('float64')) # shape=(8, 15, 4)
uop_3376 = relay.erf(call_3354.astype('float64')) # shape=(8, 15, 4)
func_2477_call = mod.get_global_var('func_2477')
func_2482_call = mutated_mod.get_global_var('func_2482')
var_3383 = relay.var("var_3383", dtype = "bool", shape = (336,))#candidate|3383|(336,)|var|bool
const_3384 = relay.const(3, dtype = "int32")#candidate|3384|()|const|int32
var_3385 = relay.var("var_3385", dtype = "bool", shape = (672,))#candidate|3385|(672,)|var|bool
call_3382 = relay.TupleGetItem(func_2477_call(relay.reshape(var_3383.astype('bool'), [7, 16, 3]), relay.reshape(const_3384.astype('int32'), []), relay.reshape(var_3385.astype('bool'), [14, 16, 3]), ), 1)
call_3386 = relay.TupleGetItem(func_2482_call(relay.reshape(var_3383.astype('bool'), [7, 16, 3]), relay.reshape(const_3384.astype('int32'), []), relay.reshape(var_3385.astype('bool'), [14, 16, 3]), ), 1)
output = relay.Tuple([const_3358,bop_3368,uop_3374,call_3382,var_3383,const_3384,var_3385,])
output2 = relay.Tuple([const_3358,bop_3371,uop_3376,call_3386,var_3383,const_3384,var_3385,])
func_3391 = relay.Function([var_3367,var_3383,var_3385,], output)
mod['func_3391'] = func_3391
mod = relay.transform.InferType()(mod)
var_3392 = relay.var("var_3392", dtype = "float64", shape = (14, 9, 12))#candidate|3392|(14, 9, 12)|var|float64
var_3393 = relay.var("var_3393", dtype = "bool", shape = (336,))#candidate|3393|(336,)|var|bool
var_3394 = relay.var("var_3394", dtype = "bool", shape = (672,))#candidate|3394|(672,)|var|bool
output = func_3391(var_3392,var_3393,var_3394,)
func_3395 = relay.Function([var_3392,var_3393,var_3394,], output)
mutated_mod['func_3395'] = func_3395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_3436 = relay.TupleGetItem(func_3274_call(), 0)
call_3437 = relay.TupleGetItem(func_3275_call(), 0)
func_2874_call = mod.get_global_var('func_2874')
func_2877_call = mutated_mod.get_global_var('func_2877')
const_3447 = relay.const([8.967731,-8.666566,-0.157796,1.077095,-6.446591,9.542031,8.610911,-0.219177,-4.503769,2.125841,4.200027,6.437365,-6.896443,4.783944,8.696644,-1.286092,-1.593461,4.711949,9.991739,3.382660,6.878281,0.243038,-3.358907,-8.650286,-0.323686,2.071705,7.734395,1.081032,-2.105900,-5.283151,2.224748,-3.700748,2.821037,-1.080370,0.209929,-9.503608,-2.903088,4.336363,6.264515,-0.183789,5.396239,2.859726,-9.090065,-1.588608,-8.178250,-6.619991,6.514380,2.508897,-5.806345,-2.461331,-1.226729,-4.440290,-5.428328,2.179012,-4.260643,-3.726341,8.343728,-5.732634,-4.893193,-1.461952,4.006528,0.839308,5.826544,3.255225,-4.171042,1.222755,-6.919954,-5.853499,6.053870,3.295778,5.978745,-9.133405,2.386071,-3.970566,8.527334,-9.485942,7.745774,-5.781786,0.476765,9.570396,4.905658,-1.542027,-4.846596,-4.555988,-5.633397,0.685421,4.738183,-8.808099,5.664531,8.870867,7.473875,4.343137,6.650980,9.939886,-1.807933,-5.148852,-0.058453,6.976304,8.907056,-2.192441,1.291891,4.827757,4.267402,-0.016357,-1.619444,-2.383831,0.527565,2.467389,3.351504,0.609489,2.305020,1.591112,-5.287181,-0.747508,-9.252060,5.537454,5.990784,5.208378,-5.029781,9.198082,2.477732,-2.010986,5.703215,4.609803,1.455865,-3.013339,-1.866730,-0.543201,6.552565,1.172502,8.101181,4.510996,7.057251,-7.052361,-7.477339,7.300438,8.162152,5.642388,4.362473,7.000052,6.929608,5.961568,0.574643,6.923116,-6.815343,-1.860347,1.647793,-0.014305,-9.635314,6.541752,-8.266405,-5.833304,-7.712674,7.210723,-5.461049,-0.590190,-8.836785,-1.364300,7.590811,-8.933345,-0.888702,-2.433331,5.228875,-4.002056,2.039602,-3.557299,-0.109091,6.168164,-2.739455,-5.756361,3.844703,1.672202,-0.066960,7.006804,8.416451,-1.844684,-4.507566,1.019063,1.214835,-2.136566,5.971404,2.696601,2.876259,9.372703,2.115652,3.356891,-8.219024,-5.873003,-9.347438,4.295078,-7.682300,9.812910,-7.744929,-2.530637,-1.858906,-6.710107,0.710107,-2.955962,-9.728427,9.567391,6.272520,-6.363172,7.728817,1.585026,-2.859188,8.683540,-5.733952,4.571808,7.568805,-4.771736,-8.210755,-4.242390,-8.235542,7.159372,-9.154201,-0.916552,3.016023,8.305889,-4.307384,-9.258808,8.476784,8.663754,-1.289305,-9.956322,-6.434418,2.926284,3.315897,-1.499476,-2.094651,-4.978364,-2.993696,3.542425,9.063999,-0.584485,5.548647,-3.297279,-6.057100,-9.644682,7.344171,6.704269,9.867980,-9.991460,-1.333360,4.090071,-4.763866,9.314025,-8.817054,-9.920833,1.543366,2.307417,9.007607,-8.748926,6.313420,-7.024916,0.353244,-0.749173,7.668891,-8.781390,-0.823100,-5.482272,1.241895,9.663715,-1.601930,-9.106853,0.913495,-8.532262,1.501935,-2.458577,6.536541,1.190085,-9.092825,-4.420504,8.638763,2.855733,-6.791993,-3.861536,8.500814,6.266192,-3.227714,-6.935095,-7.352933,-9.234762,1.139434,-6.411150,-5.021162,2.350011,-7.441366,-8.244178,-6.651610,7.942595,7.237967,1.504895,2.662749,2.041155,-4.697338,7.287926,-5.331945,-1.277013,7.215960,4.696417,9.145761,-9.319155,-2.719260,1.770438,7.065715,9.105596,-8.593124,7.446787,4.378554,0.226799,-7.477443,-1.919774,2.083787,-5.434229,-4.998446,-0.436527,3.367207,0.797297,7.211594,-7.011725,4.544261,0.491757,-8.627743,7.515324,1.230040,0.961326,-2.611275,1.340877,8.898435,-0.396611,7.019605,8.189564,3.424444,-3.264469,1.126052,0.662484,-7.291746,-2.194439,-5.906828,-2.203570,1.455949,4.844633,-9.156428,1.233714,4.981119,3.545899,-7.057377,1.363365,8.838506,-3.646703,-9.544679,8.614725,-9.706498,-0.344838,7.968714,0.698552,-2.379138,-7.207547,3.718359,-7.554334,9.692678,4.519409,-9.490158,-4.919990,-9.006493,-8.002387,-2.795659,6.819022,-2.184712,9.189578,-3.103091,-3.710445,-9.584208,1.333770,-7.852405,-2.400158,0.422051,7.799913,-7.350988,0.901606,-9.697970,8.160567,7.636266,1.976245,-7.429927,-8.075200,8.737860,-9.605912,0.842583,7.119337,1.842479,-2.303252,8.362853,9.702269,4.640153,-7.219624,-8.604667,-8.425817,-4.112479,4.281596,5.133091,-4.095983,-7.576944,-7.500693,-7.413141,3.212092,1.507047,2.660329,5.026643,-4.199306,7.492503,-3.132753,-2.230279,-7.111821,1.561703,-3.731170,0.751666,0.514457,2.065354,3.256755,-7.141704,7.074389,-0.845211,-5.523538,8.660227,-3.375300,-1.792006,2.599749,-7.091632,1.425301,7.823553,-1.966055,-8.892850,7.112009,4.604714,-6.718414,1.780066,4.195507,-1.160932,-6.255407,-6.043999,-8.425551,8.446673,1.926924,4.413502,5.024631,-5.829281,6.152339,-9.596401,-5.593237,-5.707619,8.122528,5.379115,1.833381,-0.089547,2.920017,4.866421,5.126980,8.571168,-8.655800,-0.790377,-4.112738,9.491391,5.748310,-3.832950,5.046279,-0.219058,-0.833754,5.570048,6.235497,5.968960,-9.192853,8.548000,-4.000095,-2.617269,1.365721,-1.463584,-6.143952,-2.365314,4.865678,4.710902,3.968399,1.862530,0.720734,6.190375,8.690810,-2.132178,9.342318,6.801341,-6.870126,-6.876144,-4.333499,9.551817,-5.657010,7.040285,-4.209160,-3.889170,-8.429495,-9.864902,-4.057409,7.116711,-3.927269,1.733769,0.598064,4.435815,8.990476,6.101532,6.717118,-8.775780,-5.115411,8.367680,-5.540244,-1.247907,-5.928478,4.597866,7.462682,-2.340213,-4.707880,3.116156,-9.425407,9.448222,9.949276,-1.861596,-8.514422,-8.575750,-5.298561,9.247767,-2.670786,4.352591,-8.068436,6.013398,7.189119,-0.447818,-8.351953,5.166477,-6.125155,-2.185518,-7.888406,-8.793057,2.704095,5.230880,5.984821,-7.352511,1.098165,-6.448805,-1.344090,4.017738,2.217051,7.070132,1.053338,-3.215840,-3.780496,8.555112,7.860210,7.880731,9.239356,-7.049600,4.046427,-1.072833,7.140763,7.088740,-5.346322,3.871095,-5.403106,6.188885,-4.527792,5.918808,-9.005838,7.078993,0.537350,-3.027042,6.065331,4.651532,-9.248063,7.138301,-8.823177,8.858182,4.265266,-2.407444,-0.528182,-1.237289,1.808739,3.046524,-6.716126,-7.603600,3.672857,-0.805882,0.187343,0.927946,8.769055,9.610173,6.274207,3.069987,-8.353100,-1.713042,2.619324,4.503891,4.681184,0.286055,9.024461,3.362448,-2.252448,4.167462,2.702917,9.733683,-7.059515,-0.134859,-0.872421,-4.292569,1.695098,1.868254,9.171452,7.902804,7.061064,2.497261,-7.683320,1.341774,-4.120977,2.215034,5.947465,2.536667,8.272999,-0.303385,1.290721,-1.324632,2.342375,5.134605,-5.228129,4.928907,6.605373,-8.796606,1.011752,7.960330,5.152649,8.137198,2.155600,-9.835139,-1.375036,-8.292658,4.919953,-1.401222,-8.382364,-3.632849,1.206938,-0.310737,-5.812658,-8.683642,-9.424887,4.750559,-8.136902,9.151440,9.621627,0.184371,-0.416768,5.482147,-9.041070,-0.276151,-3.818149,-8.137128,2.244169,-4.521603,5.730124,0.533119,-2.327972,1.026860,-2.730277,8.590691,-8.811885,5.994079,-1.049488,6.517047,2.400658,-3.948347,-0.591619,4.723753,5.100690,1.310687,-0.331083,1.173172,0.230065,-2.343382,1.830221,-1.131180,-6.783198,-4.584402,-2.594486,9.277240,2.993292,7.573871,-5.232463,4.597445,4.552739,1.248442,-5.819412,-2.287238,1.466510,3.779762,-4.910350,4.757208,6.761277,-8.679771,3.586835,6.102730,8.963508,-7.561272,2.673962,1.024866,-1.677317,1.699637,5.225665,-3.803371,-8.101115,3.528091,5.998189,4.694928,-1.654398,6.673488,5.946259,5.199654,7.427252,4.310765,4.761290,0.237811,1.357081,-2.796430,3.470855,9.055769,-5.660071,-0.172798,8.410056,7.783378,9.667897,1.798539,0.336454,8.218368,-9.551474,-3.144769,-3.379082,1.191695,-4.990333,-2.528248,7.027587,8.206431,2.429250,9.598860,9.001379,-1.116899,1.459966,1.767643,-4.459156,-7.052447,2.267693,6.855103,-0.948148,8.999537,-6.978918,-6.880169,-4.121680,-2.911476,-2.632144,-5.278868,-9.442068,-2.143512,5.474356,-8.535222,8.838475,-4.819118,1.594398,-0.275821,9.391205,-2.134506,6.262254,5.042010,-4.069681,4.066006,3.785715,-1.393463,9.971496,-6.380507,0.240006,-4.692306,0.621855,7.557254,-8.417057,-4.796186,-7.736008,-2.236655,-7.214216,2.576985,8.611622,5.679790,-3.732902,-9.020410,-6.432875,-3.545856,6.863960,-2.150861,-7.627695,-2.202348,6.492026,-7.355947,6.922905,-0.151115,-6.612201,4.543649,-4.576777,-1.390491,-1.868604,-0.207399,5.642761,-3.098107,-1.410748,6.617645,9.792048,4.019418,7.673853,-5.304526,-1.622937,-0.793999,-7.929619,-6.751647,-7.525569,6.487392,5.554727,5.231095,0.976081,-4.998859,0.004037,-0.714745,1.780226,9.346275,2.901833,9.990882,-2.380708,-2.794493,4.995556,-3.677444,4.614502,8.671091,7.333417,-7.772931,-9.607533,-3.365011,-5.777264,-6.866376,8.263847,-2.391323,9.902635,-7.002445,5.771244,-0.923068,-9.073478,-9.175844,3.415584,-3.520017,0.926244,9.413121,2.205191,1.509676,-4.463792,6.804437,6.394028,-8.440873,-9.253451,7.101161,7.126705,-1.694825,-1.615058,0.894005,-5.158132,-8.331355,-3.866298,-4.834917,-3.826353,-7.287255,3.211170,-3.063853,5.211082,-1.979049,4.499999,-4.182141,5.867333,-2.980895,9.904610,0.972968,-9.960012,2.847237,8.803842,-4.653793,0.456396,-2.818916,1.107223,-0.953887,4.287541,-2.325922,-6.845201,9.450299,2.328338,8.074315,-9.005941,5.670176,-0.388615,0.240248,-8.303748,6.286153,-1.640616,-6.561284,-5.441477,7.071587,2.428213,3.190536,-2.172768,-6.330642,-9.517755,-6.369772,-2.826042,8.724020,7.063149,3.941237,0.775890,3.820160,-6.789341,4.099450,-3.260717,1.236831,-4.753391,7.522942,7.997467,-0.556692,9.853620,-5.542548,-6.960845,0.819378,0.014388,6.949000,7.535117,-1.626874,6.740487,3.826112,-3.663272,6.347842,0.448306,2.872351,-8.928829,-7.986369,4.421467,-5.790493,3.196803,5.464523,-1.662715,9.090718,5.141939,8.964993,4.676420,1.386613,8.683915,-8.487394,2.204839,-1.354225,0.340497,-3.139175,6.274296,3.690576,-7.393745,0.931273,6.796008,-7.730917,3.951508,5.463219,-3.473827,-2.204102,-1.895813,-3.782712,6.922183,5.188796,-2.011142,7.070077,-5.768271,-2.047595,8.368631,7.989921,-7.604529,3.545121,-6.749318,-3.642756,8.368174,-0.324782,3.200517,-1.400471,4.751157,4.640945,6.962442,-8.718597,1.780919,-1.067937,-0.170419,-2.400004,9.219529,-0.006126,-6.775785,9.967321,-8.041942,2.652236,-7.995193,-8.854650,-7.219055,9.956010,-4.248485,6.805179,-2.057148,-3.583888,-0.971817,9.579003,-8.878986,2.588631,-1.755595,2.933456,-0.189444,-7.848664,-5.892587,5.358241,5.957015,-2.903219,-2.021887,0.457602,0.109530,4.213017,-3.483517,1.538755,2.614796,-7.606544,6.137319,-7.153787,-0.031117,1.564830,1.824872,0.661341,4.914015,-7.517148,-4.638119,1.683841,8.743755,1.637817,2.121910,-7.531999,6.872500,1.946205,-4.201046,-2.402577,-2.954335,5.022740,-5.478024,-4.307455,-9.766268,1.042426,0.007857,-0.386398,-8.849025,-2.354887,1.021711,-9.474893,0.727942,5.617277,3.420802,6.122576,7.127084,0.740298,2.585990,-0.180820,-6.828196,-3.850360,-6.491749,-8.566711,-4.231059,-9.328167,2.236379,-8.954008,-5.434475,1.970339,-1.301015,-8.305957,9.656393,8.328702,3.368483,8.610567,-6.143135,6.663973,-5.037148,4.201248,9.850969,-7.194148,-0.107915,8.311673,9.797429,-4.724377,7.042258,7.851587,-7.653510,-5.038033,-5.676952,4.514131,8.034828,8.899818,-0.562805,8.180940,4.059624,-0.075774,-2.222557,-1.654953,-2.084548,8.900559,2.144837,4.093190,-2.347259,-4.890777,2.071046,5.845073,-7.632048,-1.570256,6.305507,-8.219231,-2.935199,-6.194387,5.355763,-5.585987,5.456659,0.223742,-7.183041,-5.962965,-7.128271,-1.395161,-2.401019,2.262607,-3.202374,7.452603,7.598177,-6.465215,-0.372694,-7.125123,-1.152581,-2.583881,3.017202,-3.394727,-8.945756,-9.760431,2.815764,-2.295374,-6.039586,7.910689,6.314600,-7.758207,-2.835350,-8.827879,9.338826,-4.160372,8.276888,1.306348,6.845669,3.639022,-4.668158,-9.107630,-4.589795,2.551383,-7.648621,0.018980,3.507640,-0.217606,7.914886,-4.579216,-1.020927,-7.989490,1.022124,-1.591365,0.238804,-0.401678,5.834835,-7.063165,5.763024,-8.657654,-2.765591,-1.773601,9.935143,0.113501,7.614374,2.737844,3.618038,-8.944176,8.385763,2.454448,-7.506669,-2.126615,-5.742155,7.698026,-7.150814,-4.326250,4.785354,-8.499193,2.766691,9.840294,8.415813,-6.297722,-1.199632,-0.863984,0.138825,2.407801,4.108859,2.202903,-9.063732,-3.619433,-2.352364,7.971955,3.475576,-0.409886,7.104218,8.681847,-7.719434,8.865451,-0.387228,-9.117808,2.603399,4.246914,1.256667,7.515947,6.658165,-1.197768,-3.032473,-9.414175,6.040281,-8.581676,-0.102382,-9.603394,-7.573942,-8.397294,2.445259,-4.811935,-8.522217,9.551478,0.723145,6.341337,-3.543183,-0.050662,0.918453,-5.330520,-3.765236,8.007065,3.248308,4.457825,-5.443888,-4.533769,6.024715,-1.286579,6.796573,7.403181,-8.835997,5.256788,5.389008,2.623935,-6.227815,4.382024,3.128436,-3.204936,-7.919608,-2.588036,1.813877,-4.301509,1.771591,-0.916425,8.186626,2.930574,-9.253250,-9.896117,3.057045,-3.816698,-0.820808,-9.441063,-8.879263,-4.585742,-9.648542,2.620082,6.909585,-8.261487,0.978468,8.207469,8.369576,-8.599490,-6.590063,9.653608,3.100791,1.621877,5.596256,5.185263,-7.218511,9.793092,-5.059890,-7.522855,-6.345903,-2.520694,7.713341,-9.318666,0.339309,-5.538742,-9.958393,2.472795,4.946819,5.418826,-9.061469,5.952703,-4.934382,8.623451,6.459267,-9.181266,1.269298,1.583523,2.783416,2.402585,9.981025,-1.126707,5.152392,8.444004,-4.923669,5.865367,6.064696,-5.775866,2.250612,-1.541209,8.771487,5.724910,0.520281,-6.225302,-1.118901,3.260866,1.075486,4.584130,4.206076,-1.234256,3.295571,-6.665299,-6.461525,-6.057365,5.187684,-9.342857,-2.896017,2.434728,9.285458,-8.648308,8.667713,7.045220,8.470808,2.342369,0.757891], dtype = "float32")#candidate|3447|(1350,)|const|float32
call_3446 = relay.TupleGetItem(func_2874_call(relay.reshape(const_3447.astype('float32'), [9, 15, 10]), relay.reshape(const_3447.astype('float32'), [9, 15, 10]), ), 0)
call_3448 = relay.TupleGetItem(func_2877_call(relay.reshape(const_3447.astype('float32'), [9, 15, 10]), relay.reshape(const_3447.astype('float32'), [9, 15, 10]), ), 0)
func_3036_call = mod.get_global_var('func_3036')
func_3040_call = mutated_mod.get_global_var('func_3040')
const_3460 = relay.const([7.678155,-1.519825,-2.381854,3.688304,8.771975,-8.972406,5.190929,1.242896,-6.765350,0.267419,-6.911541,-9.183116,0.194875,7.368307,-4.205609,0.749548,-6.866754,-1.424702,4.905108,4.236241,-7.871180,-5.140548,4.624638,-7.507462,3.175502,6.035770,9.018077,2.972307,5.515574,3.503901,-1.738681,9.739564,0.646042,6.202172,-4.118959,2.490361,-8.339137,-2.012232,-2.524691,7.403165,1.794209,5.473205,-5.757638,3.305907,-3.248548,4.848779,-5.090385,4.727898,5.802850,-0.142711,9.760229,-5.380798,-8.311307,5.074227,8.412828,-7.606136,2.487029,-4.124033,-7.214504,3.747165,-9.033010,-5.811581,-8.890701,-9.206040,-8.799561,2.341686,7.994411,-6.149421,-6.796856,-3.035221,-8.504723,-2.435436,-8.018800,-8.755503,5.315470,4.078404,-5.600716,-9.688231,0.101241,-7.608693,6.594354,3.689969,7.982246,-1.527050,5.912681,-8.581301,7.221780,8.937190,1.149419,5.339362,-8.980958,-6.878553,-2.368436,7.817095,-8.538728,0.780132,2.876264,-2.402247,-6.202265,-9.398152,0.430282,-1.520833,-3.781825,-1.892246,2.397885,-7.644314,4.082063,-6.798302,0.360090,8.898431,-7.773162,2.679146,-0.452796,-8.259941,5.450339,-6.800081,8.889550,4.818475,1.945634,3.054019,0.029546,-8.848857,1.808084,-2.844253,-4.307366,-9.710917,6.240389,-1.633860,8.796093,-9.679934,1.567355,8.736224,1.034043,-6.835916,-5.467305,3.162981,5.503274,-4.759913,7.109040,6.590075,4.449999,-5.311411,-5.525057,-6.744477,1.915606,-3.926552,8.753859,-7.400903,-8.940240,0.751748,-2.731498,6.720519,-3.935411,-8.649422,-4.948012,8.021556,2.496584,-4.797338,-3.759810,5.122175,-8.444275,9.105516,3.737229,-6.485521,-8.972726,3.063392,0.811344,9.717303,-1.502952,4.857764,4.832573,-9.247296,-5.769301,-5.292464,8.137415,-1.017206,0.676179,-4.805194,1.907567,9.884728,-6.178918,4.621844,4.310196,-3.994393,-0.269859,-2.529648,-1.710873,7.208061,-2.615198,-6.419467,3.482523,9.004375,-6.025892,-9.144147,-7.636675,4.841600,-4.650120,-9.514515,1.231943,7.749675,-1.253403,-8.782882,0.713352,9.181334,3.150409,8.416738,5.824137,-9.188785,-2.199404,0.638202,-8.402620,-5.468724,7.992665,-4.291338,0.141654,5.971513,4.287124,-5.429369,5.664735,-0.285978,1.982726,5.973888,-3.052915,-8.247191,-3.992193,-0.178695,7.734800,3.962067,7.430417,6.833052,-0.882359,4.505348,-8.180819,-3.342046,0.897728,4.982316,-0.210734,3.121056,-8.012538,-7.403604,-5.693239,9.280571,3.268666,-6.806853,-1.771171,5.208272,-6.711043,-0.554195,-4.652410,-7.182557,-4.789824,9.851888,5.635652,1.738772,-6.403153,-0.551764], dtype = "float32")#candidate|3460|(256,)|const|float32
var_3461 = relay.var("var_3461", dtype = "int32", shape = ())#candidate|3461|()|var|int32
call_3459 = relay.TupleGetItem(func_3036_call(relay.reshape(const_3460.astype('float32'), [8, 8, 4]), relay.reshape(const_3460.astype('float32'), [8, 8, 4]), relay.reshape(var_3461.astype('int32'), []), ), 3)
call_3462 = relay.TupleGetItem(func_3040_call(relay.reshape(const_3460.astype('float32'), [8, 8, 4]), relay.reshape(const_3460.astype('float32'), [8, 8, 4]), relay.reshape(var_3461.astype('int32'), []), ), 3)
func_1445_call = mod.get_global_var('func_1445')
func_1448_call = mutated_mod.get_global_var('func_1448')
call_3463 = func_1445_call(relay.reshape(var_3461.astype('int32'), []), relay.reshape(call_3459.astype('int32'), [14, 12, 2]), )
call_3464 = func_1445_call(relay.reshape(var_3461.astype('int32'), []), relay.reshape(call_3459.astype('int32'), [14, 12, 2]), )
var_3465 = relay.var("var_3465", dtype = "int32", shape = (168, 2))#candidate|3465|(168, 2)|var|int32
bop_3466 = relay.bitwise_or(call_3459.astype('uint8'), relay.reshape(var_3465.astype('uint8'), relay.shape_of(call_3459))) # shape=(168, 2)
bop_3469 = relay.bitwise_or(call_3462.astype('uint8'), relay.reshape(var_3465.astype('uint8'), relay.shape_of(call_3462))) # shape=(168, 2)
output = relay.Tuple([call_3436,call_3446,const_3447,const_3460,var_3461,call_3463,bop_3466,])
output2 = relay.Tuple([call_3437,call_3448,const_3447,const_3460,var_3461,call_3464,bop_3469,])
func_3472 = relay.Function([var_3461,var_3465,], output)
mod['func_3472'] = func_3472
mod = relay.transform.InferType()(mod)
mutated_mod['func_3472'] = func_3472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3472_call = mutated_mod.get_global_var('func_3472')
var_3474 = relay.var("var_3474", dtype = "int32", shape = ())#candidate|3474|()|var|int32
var_3475 = relay.var("var_3475", dtype = "int32", shape = (168, 2))#candidate|3475|(168, 2)|var|int32
call_3473 = func_3472_call(var_3474,var_3475,)
output = call_3473
func_3476 = relay.Function([var_3474,var_3475,], output)
mutated_mod['func_3476'] = func_3476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3519 = relay.TupleGetItem(func_3130_call(), 0)
call_3520 = relay.TupleGetItem(func_3131_call(), 0)
uop_3530 = relay.sinh(call_3519.astype('float64')) # shape=(8, 15, 4)
uop_3532 = relay.sinh(call_3520.astype('float64')) # shape=(8, 15, 4)
output = uop_3530
output2 = uop_3532
func_3536 = relay.Function([], output)
mod['func_3536'] = func_3536
mod = relay.transform.InferType()(mod)
output = func_3536()
func_3537 = relay.Function([], output)
mutated_mod['func_3537'] = func_3537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_3554 = func_3536_call()
call_3555 = func_3536_call()
func_758_call = mod.get_global_var('func_758')
func_762_call = mutated_mod.get_global_var('func_762')
var_3563 = relay.var("var_3563", dtype = "float64", shape = (924,))#candidate|3563|(924,)|var|float64
call_3562 = relay.TupleGetItem(func_758_call(relay.reshape(var_3563.astype('float64'), [14, 11, 6]), relay.reshape(var_3563.astype('float64'), [14, 11, 6]), ), 0)
call_3564 = relay.TupleGetItem(func_762_call(relay.reshape(var_3563.astype('float64'), [14, 11, 6]), relay.reshape(var_3563.astype('float64'), [14, 11, 6]), ), 0)
output = relay.Tuple([call_3554,call_3562,var_3563,])
output2 = relay.Tuple([call_3555,call_3564,var_3563,])
func_3573 = relay.Function([var_3563,], output)
mod['func_3573'] = func_3573
mod = relay.transform.InferType()(mod)
var_3574 = relay.var("var_3574", dtype = "float64", shape = (924,))#candidate|3574|(924,)|var|float64
output = func_3573(var_3574)
func_3575 = relay.Function([var_3574], output)
mutated_mod['func_3575'] = func_3575
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3645 = relay.var("var_3645", dtype = "float64", shape = (1, 10, 9))#candidate|3645|(1, 10, 9)|var|float64
uop_3646 = relay.exp(var_3645.astype('float64')) # shape=(1, 10, 9)
bop_3653 = relay.add(var_3645.astype('float32'), relay.reshape(uop_3646.astype('float32'), relay.shape_of(var_3645))) # shape=(1, 10, 9)
bop_3658 = relay.less_equal(bop_3653.astype('bool'), relay.reshape(uop_3646.astype('bool'), relay.shape_of(bop_3653))) # shape=(1, 10, 9)
var_3670 = relay.var("var_3670", dtype = "float64", shape = (11, 10, 9))#candidate|3670|(11, 10, 9)|var|float64
bop_3671 = relay.multiply(uop_3646.astype('uint16'), var_3670.astype('uint16')) # shape=(11, 10, 9)
func_3391_call = mod.get_global_var('func_3391')
func_3395_call = mutated_mod.get_global_var('func_3395')
var_3686 = relay.var("var_3686", dtype = "float64", shape = (1512,))#candidate|3686|(1512,)|var|float64
var_3687 = relay.var("var_3687", dtype = "bool", shape = (4, 84))#candidate|3687|(4, 84)|var|bool
var_3688 = relay.var("var_3688", dtype = "bool", shape = (672,))#candidate|3688|(672,)|var|bool
call_3685 = relay.TupleGetItem(func_3391_call(relay.reshape(var_3686.astype('float64'), [14, 9, 12]), relay.reshape(var_3687.astype('bool'), [336,]), relay.reshape(var_3688.astype('bool'), [672,]), ), 6)
call_3689 = relay.TupleGetItem(func_3395_call(relay.reshape(var_3686.astype('float64'), [14, 9, 12]), relay.reshape(var_3687.astype('bool'), [336,]), relay.reshape(var_3688.astype('bool'), [672,]), ), 6)
func_3391_call = mod.get_global_var('func_3391')
func_3395_call = mutated_mod.get_global_var('func_3395')
call_3697 = relay.TupleGetItem(func_3391_call(relay.reshape(var_3686.astype('float64'), [14, 9, 12]), relay.reshape(var_3687.astype('bool'), [336,]), relay.reshape(call_3685.astype('bool'), [672,]), ), 4)
call_3698 = relay.TupleGetItem(func_3395_call(relay.reshape(var_3686.astype('float64'), [14, 9, 12]), relay.reshape(var_3687.astype('bool'), [336,]), relay.reshape(call_3685.astype('bool'), [672,]), ), 4)
bop_3700 = relay.floor_mod(bop_3671.astype('float32'), var_3645.astype('float32')) # shape=(11, 10, 9)
uop_3706 = relay.cosh(bop_3700.astype('float32')) # shape=(11, 10, 9)
func_2152_call = mod.get_global_var('func_2152')
func_2155_call = mutated_mod.get_global_var('func_2155')
var_3713 = relay.var("var_3713", dtype = "uint64", shape = (1152,))#candidate|3713|(1152,)|var|uint64
call_3712 = func_2152_call(relay.reshape(var_3713.astype('uint64'), [12, 16, 6]), relay.reshape(var_3713.astype('uint64'), [12, 16, 6]), )
call_3714 = func_2152_call(relay.reshape(var_3713.astype('uint64'), [12, 16, 6]), relay.reshape(var_3713.astype('uint64'), [12, 16, 6]), )
output = relay.Tuple([bop_3658,call_3685,var_3686,var_3687,var_3688,call_3697,uop_3706,call_3712,var_3713,])
output2 = relay.Tuple([bop_3658,call_3689,var_3686,var_3687,var_3688,call_3698,uop_3706,call_3714,var_3713,])
func_3727 = relay.Function([var_3645,var_3670,var_3686,var_3687,var_3688,var_3713,], output)
mod['func_3727'] = func_3727
mod = relay.transform.InferType()(mod)
mutated_mod['func_3727'] = func_3727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3727_call = mutated_mod.get_global_var('func_3727')
var_3729 = relay.var("var_3729", dtype = "float64", shape = (1, 10, 9))#candidate|3729|(1, 10, 9)|var|float64
var_3730 = relay.var("var_3730", dtype = "float64", shape = (11, 10, 9))#candidate|3730|(11, 10, 9)|var|float64
var_3731 = relay.var("var_3731", dtype = "float64", shape = (1512,))#candidate|3731|(1512,)|var|float64
var_3732 = relay.var("var_3732", dtype = "bool", shape = (4, 84))#candidate|3732|(4, 84)|var|bool
var_3733 = relay.var("var_3733", dtype = "bool", shape = (672,))#candidate|3733|(672,)|var|bool
var_3734 = relay.var("var_3734", dtype = "uint64", shape = (1152,))#candidate|3734|(1152,)|var|uint64
call_3728 = func_3727_call(var_3729,var_3730,var_3731,var_3732,var_3733,var_3734,)
output = call_3728
func_3735 = relay.Function([var_3729,var_3730,var_3731,var_3732,var_3733,var_3734,], output)
mutated_mod['func_3735'] = func_3735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3182_call = mod.get_global_var('func_3182')
func_3183_call = mutated_mod.get_global_var('func_3183')
call_3754 = func_3182_call()
call_3755 = func_3182_call()
output = call_3754
output2 = call_3755
func_3759 = relay.Function([], output)
mod['func_3759'] = func_3759
mod = relay.transform.InferType()(mod)
mutated_mod['func_3759'] = func_3759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mutated_mod.get_global_var('func_3759')
call_3760 = func_3759_call()
output = call_3760
func_3761 = relay.Function([], output)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3764 = relay.TupleGetItem(func_3130_call(), 0)
call_3765 = relay.TupleGetItem(func_3131_call(), 0)
uop_3845 = relay.log(call_3764.astype('float32')) # shape=(8, 15, 4)
uop_3847 = relay.log(call_3765.astype('float32')) # shape=(8, 15, 4)
bop_3852 = relay.floor_divide(uop_3845.astype('float64'), relay.reshape(call_3764.astype('float64'), relay.shape_of(uop_3845))) # shape=(8, 15, 4)
bop_3855 = relay.floor_divide(uop_3847.astype('float64'), relay.reshape(call_3765.astype('float64'), relay.shape_of(uop_3847))) # shape=(8, 15, 4)
output = bop_3852
output2 = bop_3855
func_3859 = relay.Function([], output)
mod['func_3859'] = func_3859
mod = relay.transform.InferType()(mod)
mutated_mod['func_3859'] = func_3859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mutated_mod.get_global_var('func_3859')
call_3860 = func_3859_call()
output = call_3860
func_3861 = relay.Function([], output)
mutated_mod['func_3861'] = func_3861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_3884 = func_3759_call()
call_3885 = func_3759_call()
const_3890 = relay.const([[[7.451060,0.160233,9.402846,7.716104],[-0.719690,4.831609,2.443565,4.557096],[-5.061098,-1.709026,0.095817,9.011753],[-2.966651,9.297727,-9.013573,-8.841313],[2.538655,-5.870691,-9.228422,-9.874182],[-2.227683,8.606823,9.765701,8.184868],[6.904083,-9.669749,-9.034429,-6.553280],[-7.944985,-9.457407,-7.130963,-0.506849],[-9.497355,3.640265,-5.401364,1.833685],[6.686298,7.078858,-9.818933,-1.636433],[-2.202414,-9.814805,9.337896,6.351708],[-5.366764,-6.457317,-6.992543,-7.198291],[-6.841778,3.554804,-3.444882,8.686029],[3.716552,-3.311411,8.877626,-8.927139],[-5.906748,-3.165276,4.648706,3.426065]],[[1.409601,5.042574,-0.797576,-9.003914],[4.961682,4.435657,3.864310,3.048364],[5.265501,-5.753954,-5.998976,-2.192523],[5.556980,-9.309024,-6.186275,-8.832307],[-3.497137,7.989696,4.663648,6.008052],[-1.001915,-0.839534,1.879443,-8.006021],[-5.127761,-6.845385,3.601432,5.715759],[1.227895,-7.826016,4.139738,-7.104447],[-4.071946,-0.963167,0.664117,-7.113538],[-8.876909,2.188150,-0.197313,4.838870],[-0.229340,4.863930,-7.528774,-0.360716],[5.043487,-8.300901,8.698682,-6.372226],[-2.842860,-0.401033,-5.807814,9.195531],[3.574716,-5.089530,3.677983,-8.834548],[8.155300,3.348533,-7.287783,-1.576558]],[[-5.570299,-3.369339,8.882353,0.641938],[4.775646,5.843115,-8.344644,1.608748],[-6.156964,1.754670,7.472082,3.833763],[-3.602324,-6.837783,1.885797,-2.314179],[6.435990,3.176383,0.812537,6.532016],[-7.422695,-9.468442,1.854332,0.063539],[0.026055,7.690570,-6.520804,-1.134521],[-9.661289,-7.455446,5.087042,1.602277],[3.395456,2.357944,-1.120421,-3.896694],[5.876013,4.752040,-8.624257,-7.458729],[-2.014593,-4.015938,0.498716,4.001667],[7.494870,9.774659,-4.186598,-1.490349],[7.846489,-0.112402,-7.702991,6.020594],[0.993595,-5.586696,0.819650,2.819740],[3.599448,-7.440631,-8.822331,-7.913215]],[[7.200766,-5.780236,-9.772184,-2.802428],[-1.458434,4.877133,3.044223,4.431149],[-4.225593,-5.037719,-8.796776,3.003608],[7.053094,-7.947438,3.692933,0.439366],[-0.076386,-9.523765,-4.715275,8.458844],[1.588732,3.941336,3.449879,3.707932],[5.144626,6.197797,4.902569,4.044359],[-9.367438,0.201797,-8.571832,2.822341],[-8.150581,7.582588,-1.352995,-3.658617],[-3.001978,-6.000275,-1.346230,2.808365],[2.991831,4.196551,4.636547,2.261631],[0.872369,7.968321,0.691308,-3.430698],[-0.188700,5.542627,-7.700979,-7.768303],[3.339605,-9.290773,-4.660124,3.693684],[-8.257278,-4.620392,4.277081,-4.438416]],[[-9.500680,-1.978412,-3.410790,-4.157043],[5.284007,1.118442,8.882787,-6.223612],[-1.151454,-7.390683,-1.944257,-8.761813],[-8.274882,-4.209899,-1.752513,-9.568691],[-3.919854,-9.274820,-3.585880,2.557025],[-1.995085,9.824675,-6.751907,2.703542],[6.907197,6.821549,5.637644,-9.565908],[-8.676931,-5.200744,9.511371,-5.412367],[2.494854,-7.680192,8.754951,9.595880],[-3.184256,2.485415,-0.745036,2.469216],[-7.709633,1.883598,-3.107519,5.104788],[-2.448181,3.230179,8.091118,7.809575],[8.875955,-0.635226,5.408671,-8.633283],[-2.024106,-0.952612,-3.665645,-5.207976],[-4.531088,5.419166,-6.801221,-4.856406]],[[-4.826899,-2.020069,9.004546,-4.566010],[-1.312291,8.013249,8.275585,9.953007],[3.761384,-4.836802,-5.941241,-9.861409],[0.347980,3.694089,-4.229494,-1.914694],[-5.483056,-4.331853,0.748535,-9.625667],[0.377961,4.318275,6.974536,5.289098],[7.860228,8.887387,-8.213594,-0.182284],[2.898794,3.933064,5.073219,-6.136922],[9.754466,2.814737,6.477656,-3.247874],[1.942104,0.265094,-4.728285,0.440180],[0.138754,6.755175,-3.981340,8.340624],[-8.981740,-7.387502,-7.555918,8.772164],[6.929370,-6.853268,-5.983388,-7.192645],[1.729626,-7.078267,-0.581576,0.916356],[-5.495152,5.543001,-8.142000,-3.334183]],[[-5.394468,0.055659,4.021894,-9.242721],[5.892545,-8.734815,3.677610,-4.845153],[-8.745578,-9.413082,-4.651677,-5.756662],[2.229290,-1.342879,-0.753345,-4.155575],[9.768950,-8.843790,-2.387925,9.919215],[8.434949,7.980115,-7.360362,1.889877],[-5.507357,1.556799,7.454975,-9.519155],[-7.812462,1.301764,4.836529,0.546821],[3.935566,-0.583793,-0.766982,6.555035],[6.868216,-7.139498,-2.169392,-6.160294],[4.649595,-5.650261,-6.967640,0.330022],[7.338349,6.592543,-5.637372,3.611202],[-4.943464,3.602954,1.140181,8.137911],[9.489102,1.715083,9.235874,0.855495],[6.036379,-4.592551,-4.053604,-3.714664]],[[-0.949265,-6.048761,-1.334976,-6.369002],[0.167493,9.520154,-1.635849,7.613570],[-0.243918,-9.027534,3.414481,7.445783],[2.756428,-2.215228,0.702620,1.887078],[-7.105768,0.384035,2.959769,-8.957309],[4.500249,1.619316,-0.778364,-1.032757],[4.979055,-8.424247,-2.469487,-3.233793],[1.478565,1.542364,2.517359,-4.168081],[-7.961736,9.605492,8.903522,5.048262],[2.498620,6.968037,5.837588,5.823216],[-2.318420,5.532099,8.983317,-2.415051],[-6.802891,5.583240,-0.061429,-1.277334],[4.916411,-4.095469,7.527584,-9.397095],[-7.633121,-8.907267,4.074627,4.491187],[2.713671,-5.975193,-9.867676,-0.935647]]], dtype = "float32")#candidate|3890|(8, 15, 4)|const|float32
bop_3891 = relay.logical_and(call_3884.astype('bool'), relay.reshape(const_3890.astype('bool'), relay.shape_of(call_3884))) # shape=(8, 15, 4)
bop_3894 = relay.logical_and(call_3885.astype('bool'), relay.reshape(const_3890.astype('bool'), relay.shape_of(call_3885))) # shape=(8, 15, 4)
output = bop_3891
output2 = bop_3894
func_3896 = relay.Function([], output)
mod['func_3896'] = func_3896
mod = relay.transform.InferType()(mod)
mutated_mod['func_3896'] = func_3896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mutated_mod.get_global_var('func_3896')
call_3897 = func_3896_call()
output = call_3897
func_3898 = relay.Function([], output)
mutated_mod['func_3898'] = func_3898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_3901 = relay.TupleGetItem(func_3274_call(), 0)
call_3902 = relay.TupleGetItem(func_3275_call(), 0)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_3905 = func_3896_call()
call_3906 = func_3896_call()
func_3314_call = mod.get_global_var('func_3314')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_3912 = relay.TupleGetItem(func_3314_call(), 0)
call_3913 = relay.TupleGetItem(func_3316_call(), 0)
func_3727_call = mod.get_global_var('func_3727')
func_3735_call = mutated_mod.get_global_var('func_3735')
var_3920 = relay.var("var_3920", dtype = "float64", shape = (15, 6))#candidate|3920|(15, 6)|var|float64
const_3921 = relay.const([-2.102428,9.823156,-3.472961,9.122988,2.040117,-0.445066,-9.572204,-9.480758,-9.622430,6.168909,-7.432946,-0.869859,-5.036108,-1.905482,8.630645,-7.477024,7.639468,3.989248,1.775188,-7.616861,0.866707,-1.896094,-7.219566,0.567083,3.818292,-9.008923,-2.460699,-2.243594,-4.170996,-2.862783,-1.125703,-5.395432,-4.627190,-2.003336,-3.034384,9.363539,1.408788,-7.785265,-6.514157,-1.376811,-7.291499,4.952328,-6.741031,-1.626507,0.301325,-1.360448,8.033544,9.914535,-4.146719,0.864925,6.059661,-8.453838,4.090596,-4.411080,-1.787461,0.320111,3.316538,6.403832,9.538798,3.603827,-1.902837,-3.366210,-7.124110,-3.737955,4.000963,8.821205,-9.588600,-6.832482,-4.662275,2.141469,1.544902,-7.132344,-3.292902,-8.003872,2.762269,-2.946154,0.044388,0.472595,-2.492409,-0.630762,-7.021951,-2.716012,-7.954639,-2.963430,-8.839081,6.989355,-8.970212,-2.734822,-1.518262,-7.514391,-1.499631,3.354022,-1.409696,0.577112,-0.274419,-2.643551,-0.532973,9.990661,9.686270,0.294669,-2.832839,-6.037363,-0.457660,8.663890,9.057412,-4.326321,-9.411749,-0.508573,3.920666,6.350487,5.480057,-0.916731,4.395432,-5.643346,4.767991,-3.323465,8.473845,-4.397070,8.583946,-3.566471,-1.680019,3.458930,-7.925913,7.667862,0.274872,-1.103678,-9.330851,-5.335240,-3.668686,6.858554,0.012344,8.069365,-6.236791,-9.654059,4.515668,-9.210998,-4.852486,-5.723285,1.701765,-1.971645,5.375365,-2.406664,1.535130,6.965510,1.874166,4.265345,-9.148221,9.533474,-7.541058,-6.228425,-6.419461,0.141354,-9.501954,-5.286044,4.628377,6.897794,3.862544,2.781693,-6.075641,-8.277539,1.409362,-8.109706,3.866296,-6.745983,-2.673504,3.479924,7.407040,7.114075,7.489540,-4.838872,-6.038541,2.312445,7.622383,-0.815158,7.955639,7.848824,-3.015030,-1.825623,-8.957632,9.236026,3.763033,0.991759,-9.184207,6.079003,-0.061127,-1.119045,8.398141,-4.554502,-1.363036,-8.517633,-0.301175,-4.161167,-6.339803,-7.535121,1.955387,4.301463,-0.504818,-4.570425,0.505469,-2.748503,6.393350,-8.775122,-0.193714,9.375497,1.252216,-9.056172,5.001972,-4.972369,7.507686,-5.394632,-7.317056,-6.067724,5.623892,9.595329,-5.875989,-7.144265,9.669023,-8.451485,-4.767763,-4.961450,4.180843,7.032026,-6.145456,-0.885837,-6.821031,-7.677641,-1.230626,1.292939,4.126505,-0.691592,2.185179,3.642690,7.255262,-5.573960,5.710327,9.113419,-0.290412,-0.220373,-0.662068,-5.514161,6.734278,-3.699306,9.268152,9.098314,-8.882602,-2.273815,5.527799,-6.601437,6.329064,-0.887085,-5.078847,-5.986484,-5.426235,1.899779,0.328954,7.507687,-6.239461,5.930942,7.496515,4.119517,-5.212413,2.575329,7.613178,2.309452,4.716435,-2.559482,9.942747,-5.285642,5.585244,9.180198,5.718893,9.034688,-7.498406,-0.570376,-4.783078,5.999320,6.286644,-2.672131,3.036980,-4.098468,8.338240,-4.165622,0.382611,-2.067013,-1.305501,4.504466,-4.634531,0.659257,4.666247,-7.336136,8.534879,3.620368,4.795302,-8.746541,1.553189,3.151615,4.826922,0.249097,-7.590425,4.399202,8.098305,-4.734474,0.773289,-2.675137,5.748481,-0.102598,8.997905,-6.135827,4.685288,3.995590,1.017036,5.213983,-7.246458,4.648228,-9.691379,5.398713,0.665430,2.343342,9.798216,-1.938866,7.875459,-3.252887,-5.292845,2.151278,1.277236,-0.184549,3.970695,6.845795,-1.146398,-9.290367,5.843548,6.375141,9.696166,6.534361,-0.515457,-3.155689,1.755956,-0.473345,6.960813,7.770874,-7.414043,6.064962,-8.716764,4.231525,1.045797,0.954786,7.370171,6.502403,-8.555007,-2.776839,-1.619008,-8.265762,6.331857,1.467500,-8.835653,3.280235,-4.374182,-4.594159,3.444273,-5.190875,4.492275,9.824273,-3.558450,2.339574,2.175459,7.462746,-9.651862,7.119463,5.122599,-1.910781,-8.285509,-9.166716,-1.463061,5.396780,9.727337,-7.937912,3.357997,1.410372,9.020872,-3.121673,-0.782023,-1.846695,0.181473,-7.459593,2.817716,-0.776110,-9.390758,-3.461947,9.098490,-6.657830,5.916461,0.540470,-9.825942,-6.300882,-7.056687,7.218910,4.205126,6.006962,6.908719,7.061496,1.065907,-0.717919,-0.534346,-5.805005,-5.495950,-7.174524,-7.144798,6.519965,1.120875,-3.584722,-5.229467,-6.163543,5.068697,0.561557,-3.118068,8.655914,-0.197001,2.642419,4.218483,8.770385,5.388680,5.322707,2.522087,-6.243946,1.034765,-5.444960,-9.790959,8.368030,9.258598,8.698610,8.430052,3.966103,-9.103991,-1.441227,-6.919089,-5.970945,-3.380982,0.812447,-4.991219,-3.426415,-1.277935,5.962865,9.734565,8.253752,2.037981,-9.742039,3.807553,8.529164,6.571308,8.166174,0.912872,3.371373,-4.007475,3.550203,-4.142435,-0.643208,8.212688,-6.457006,-1.302679,0.188567,-8.252221,-8.599479,0.539522,6.135291,2.562186,-3.527584,-4.683314,-2.438426,6.204979,3.246139,7.011791,-7.894988,-6.513998,-7.977724,-8.563698,-3.393844,0.589017,3.717175,-3.197361,8.992256,9.761813,-7.236627,3.999237,-3.813739,7.296857,8.224329,4.789782,1.705946,-7.073166,-1.335997,4.743281,7.570044,2.925920,9.213414,5.724143,-5.964246,-1.827745,4.706275,9.349891,-7.792030,3.458603,-2.131274,-1.164947,-7.938691,2.359718,2.847754,-2.986373,3.417327,9.578600,7.075047,-0.324109,-6.232441,8.571623,-8.244366,0.190461,2.704431,-8.746497,-4.533408,2.606530,7.104835,1.406865,7.666440,8.137520,-7.523166,7.568334,-9.241754,4.585401,-5.249134,-8.432827,1.387860,-9.791490,-7.097462,-7.116910,0.077433,-7.821251,-2.876229,4.318818,1.431566,8.673311,-1.552835,9.137045,-1.234072,5.717962,8.322459,4.119886,4.254510,1.086077,5.979220,-7.314622,0.287884,5.891120,1.748920,5.045846,-1.911643,-3.401561,2.654693,2.944517,-2.771967,6.953190,-6.484277,-5.889117,-9.505162,1.334924,-8.294542,-7.405971,-7.037705,6.191368,-3.014436,-7.587070,6.256492,1.273940,9.866259,-4.094707,7.540606,0.865696,7.434611,-2.722704,-8.213975,4.779562,1.981866,-3.986257,4.613166,1.143692,0.659700,-1.193147,-8.526636,3.043229,-9.086477,4.461338,4.000364,9.739563,3.279584,-6.995343,-7.991306,-6.702414,0.107001,6.264041,-4.440099,8.451438,4.854325,2.200215,3.569483,1.818397,-2.719648,-9.589429,6.805885,-5.906064,6.517187,-8.045316,-9.131976,7.205758,-8.723258,5.446174,-4.356228,-2.787699,-8.953301,8.353814,-6.939910,-8.764513,-7.543758,8.811015,-2.824824,-6.543850,-0.790531,6.562484,6.471596,1.907396,-1.157860,-9.755054,5.606813,-4.788362,-1.860660,3.602636,-3.487415,-8.933351,-7.120223,-8.863160,1.862422,-5.937278,-9.368179,9.081114,1.388675,6.896340,8.300382,-1.484280,-4.220256,-3.026398,-1.353513,5.167562,8.346273,6.072764,1.135427,9.453461,-8.253901,8.339823,4.490739,-8.035604,4.346418,-8.295153,-6.484407,1.330142,1.565184,7.581843,7.201548,-0.589587,-2.742793,1.155753,-2.388252,1.336194,-2.618828,4.067313,1.796206,-5.767229,1.291062,4.288980,0.740710,-8.868308,-4.883293,2.481083,-8.239208,9.800524,6.392750,7.041898,7.114703,4.847595,6.013398,7.123355,-0.777331,6.238386,9.723244,2.008005,3.283720,5.940795,-8.204216,7.569411,0.602547,9.586479,1.774623,-3.134494,6.998130,5.381342,-1.806138,6.449698,-9.088972,-3.462935,8.221141,9.692257,7.075624,0.175072,2.760982,-2.114643,3.479167,3.899526,-8.816097,5.578092,0.232419,-8.858516,9.800029,4.859902,-9.537117,6.861350,7.708780,-6.517665,-0.835364,-5.587192,4.105459,-0.409912,9.746640,1.904568,9.101755,1.065081,1.171243,-5.434121,-3.349768,2.444413,9.985424,-8.842800,3.484349,6.973324,-5.858950,4.979364,-7.011297,-8.210329,6.781873,-6.581343,-6.779809,-1.864403,2.908731,9.941097,-8.272765,6.823805,7.043182,-5.237571,-1.522456,-2.563495,-8.238798,-7.557169,2.155414,-1.573977,2.264022,3.197086,-7.105532,7.118672,-0.757967,6.101060,8.120338,-0.087718,4.730817,2.187645,-0.382393,-2.224010,9.830995,-1.979994,-2.135888,-3.229555,9.902919,5.442791,9.653145,4.797634,0.797918,-0.788367,5.884003,-3.642541,4.373419,4.177247,1.184842,-9.902657,-6.361041,-3.222110,1.161731,-4.923723,-3.294182,7.676991,9.975669,-4.673081,4.192627,7.116755,3.675619,9.370108,-2.619080,6.032440,0.657669,-5.285709,-7.133734,-5.288316,3.730924,-0.325008,-9.481107,0.051105,-4.587941,7.401190,-7.451300,2.223429,-8.095079,6.569018,4.365311,-7.259534,-1.227600,-3.796980,3.265358,3.212200,-9.597444,8.047962,0.105289,-5.215370,-9.788524,0.522600,-8.052337,-6.981928,-8.323197,3.294712,-7.643898,-5.119351,6.496957,6.825811,5.756224,7.480307,-7.305529,-8.256569,-8.438860,-6.542129,-3.384353,3.827952,-1.752352,5.211982,2.801767,-6.574710,1.080774,7.205230,8.801977,4.587692,8.464559,-3.200558,6.097600,1.446090,0.809091,-0.751999,1.780941,9.192838,-0.631251,-4.858654,8.857313,2.784916,5.645888,8.686057,-7.338594,2.347318,-6.772133,4.422650,2.585246,8.606216,-9.212382,-1.932017,4.494601,1.001443,9.162813,-4.086788,-6.486165,0.888999,-5.657106,6.878389,0.889718,-7.449173,-0.695639,-4.014845,-4.841453,8.215910,2.223876,-7.688989,3.779690,-3.014551,-9.901049,6.278801,5.872390,-1.343190,-9.184953,-1.829439,9.690602,6.036767,-2.719720,8.247682,6.396741,-0.479287,-2.745290,9.836751,-2.498359,-8.414637,-8.505233,-5.326573,-3.942131,3.690493,-7.772010,1.194150,-4.114506,9.212906,-8.866666,8.686891,6.128718,-3.209603,0.175220,9.198007,-7.376034,-2.438254,-4.636538,-7.431710,6.825480,1.759898,2.343489,6.825667,8.427974,-1.233183,5.535315,0.715873,7.336212,8.368928,2.420296,8.355768,-7.553352,1.630934,-1.077630,-2.176319,9.153836,9.989169,-9.495877,3.035680,3.213444,9.610884,2.581002,-6.096891,-2.833947,9.625243,-8.785199,3.128222,-3.595145,6.524563,-9.559149,4.288379,3.429644,-5.892635,7.936579,4.686260,-2.110852,-6.919626,3.792251,-5.337374,-8.814964,-1.573731,-4.091629,6.689326,-3.310640,5.037593,-4.383685,-2.041971,7.885039,3.378998,-3.395439,-1.137373,6.487473,0.912662,9.434693,6.160796,7.194634,-7.912699,7.659371,7.316185,4.013534,3.676797,7.583026,9.569745,-7.257467], dtype = "float64")#candidate|3921|(990,)|const|float64
const_3922 = relay.const([[-8.143906,-1.304450,2.027445,6.879542,8.172708,-8.810191,-4.220264,-5.721939,0.516615,1.813879,-2.478534,9.818427],[-3.817583,3.101094,-9.658958,-2.745807,5.556276,-3.164494,-5.478738,-5.552848,-0.406550,3.123674,-7.487306,-6.500056],[5.742215,-1.704907,-4.992398,-5.889453,-1.917679,1.983725,2.450385,-0.942211,7.541170,9.937566,-0.360280,7.526327],[-2.789493,8.376777,7.750590,-3.209184,-2.821179,-3.478879,5.027600,1.969792,-2.440786,-3.638358,-3.291989,5.229306],[-1.649194,-6.810411,-1.619659,9.398367,-0.892258,2.999325,-1.964419,-3.988057,-3.629781,9.689401,2.844923,9.390794],[-8.201648,9.278341,-2.961538,-6.447711,2.495133,-1.304815,-6.216664,2.352954,-7.427651,-1.462061,-0.968153,5.966402],[4.737099,-3.797415,9.186609,1.715151,-5.280425,7.979374,3.630580,1.648026,-8.616562,-4.553180,5.323720,5.734561],[-9.847378,-1.354468,-8.129723,5.834104,-6.696339,-8.561140,4.448918,9.846208,7.549113,4.484965,-6.676016,3.117320],[-0.376769,-5.847480,3.397976,6.290302,8.850250,3.693716,-0.039680,-1.384211,-3.761899,-7.343859,-4.543484,7.851689],[-3.529172,-5.491568,8.187780,0.443744,6.415611,8.597241,9.661976,-5.550807,-3.017263,-4.764328,-8.729631,-1.988817],[-3.804602,-3.195270,-7.835761,-9.556578,-1.384819,-1.354510,-8.340087,9.661700,0.786831,7.795104,-4.818402,0.404204],[7.595055,8.371057,-9.771775,-1.747520,-3.512634,4.457108,3.119127,-4.755946,-9.692612,0.616551,-1.507138,-6.839120],[-6.180178,2.145593,1.654333,6.711912,-3.237645,-8.307616,-4.462928,6.126507,-0.144960,-3.369959,-2.186223,6.663879],[2.962754,-7.365566,-5.460152,7.263633,-9.365560,8.710891,4.780362,-7.982901,6.133147,3.151128,5.578494,-9.876986],[0.903988,4.060519,1.735003,8.459993,-3.369176,3.060917,-1.531447,5.776978,0.795685,2.876246,6.870452,-3.529236],[-4.927742,2.223961,9.930521,5.603245,-0.794442,-7.313096,-4.278627,-5.852941,8.506078,8.538263,-1.438647,-5.602287],[6.908630,-5.877257,1.327658,9.750714,-8.117954,-5.437316,-4.075740,8.802921,-1.876163,3.891560,7.834921,7.311002],[9.329559,-2.684966,7.523274,0.252338,-6.858458,-8.648229,-3.638205,-0.515162,-9.264193,-2.817110,-8.975073,2.045248],[-5.286070,8.609591,-7.820480,-9.659609,5.453251,1.194962,-9.706584,0.471145,-0.234876,-0.596692,4.615716,-9.639408],[7.336666,7.848808,-7.786632,1.209734,0.787337,-9.123260,8.325801,5.293731,6.526912,-1.012110,3.345929,3.153681],[0.336145,-9.392979,-4.518483,-8.590032,-5.460054,8.802466,-7.698631,1.706694,-7.773690,6.776372,-0.485196,-9.502725],[8.839908,2.385609,2.836648,-7.074865,6.702686,5.548520,1.741570,4.318373,7.414809,-1.049504,1.139628,2.171438],[5.404827,-7.898001,6.820305,-9.620797,6.584135,3.243911,-6.235172,3.155548,4.297237,3.968804,-1.220543,-3.368735],[7.259068,0.654384,-2.410974,-4.562975,3.494352,6.338456,-8.062849,0.802102,-4.086414,-8.952847,-3.438558,-3.766131],[-9.650087,0.843462,-0.576271,6.511429,-8.777990,1.302018,4.116989,2.228112,-4.769876,-5.953136,-6.199465,-1.244652],[-3.642238,2.380339,-8.383415,-7.660334,3.333312,9.392893,4.970737,5.940601,0.495860,-2.242487,4.780174,7.741537],[6.287472,-8.090656,2.466213,-4.135067,0.803574,-5.199784,4.613731,-5.064394,-7.785918,-8.631336,-2.659861,-3.508151],[-8.881381,0.341143,-5.633171,7.312203,-9.779826,1.446544,-0.679261,6.520830,2.599708,6.590945,3.985461,2.035968],[5.959074,4.389707,3.511837,1.290985,7.291163,7.312633,6.071733,4.844324,-1.035814,4.135554,-6.924779,-7.111234],[2.534446,-8.245774,-8.982800,-3.818084,3.655525,1.145230,8.920996,0.969325,4.931079,-1.655620,0.024611,-1.525294],[-4.672970,3.887552,8.725850,-3.263690,9.947370,0.398509,-2.851333,-4.532925,0.835598,1.691649,-1.836711,6.976647],[8.711913,7.407379,1.778886,3.463757,1.885219,-0.228956,-7.523180,2.201394,4.663412,5.537576,8.810193,-0.019948],[-3.944729,4.692487,-1.339329,-9.588550,7.659280,-0.515635,-3.137781,-6.926877,-2.895324,-5.251813,-3.643297,1.494665],[-7.610977,1.273389,-7.944196,-2.994200,4.149913,6.805946,0.087000,-7.018434,8.204466,8.990620,-3.917951,-4.016596],[8.126355,4.132903,-1.732198,4.252984,-3.072547,-0.395641,-1.694851,0.009613,2.065975,0.241142,-7.610532,7.731695],[6.951416,6.906430,-7.084412,-3.523073,-1.652716,9.838663,-9.444423,0.924022,-8.970480,5.102440,9.456956,-4.583672],[-6.827231,7.113687,0.734747,-3.478919,7.243108,-9.282518,1.747407,2.248379,1.059189,7.850611,-0.109722,-8.505632],[-8.152094,1.742539,-6.399541,-1.016214,-8.958383,8.151890,-3.387653,-4.236993,-5.172850,-9.784404,9.785676,9.807048],[-3.473729,3.873221,-6.099483,5.598532,3.989586,-0.889092,9.800242,-3.104475,-8.434042,1.046211,-4.441351,-8.978757],[8.517808,-1.599719,2.268888,7.019556,-9.042612,-7.287958,-7.202793,-6.084762,-2.932011,5.116222,2.576599,6.268556],[0.129072,4.925290,-3.131489,-4.345980,-6.930407,8.073003,8.547363,8.523157,4.764655,-7.769818,-2.878342,9.631073],[5.013562,-0.307163,8.345165,-3.398277,-8.245899,-2.233527,3.163418,-9.099274,1.614959,0.030110,-4.465303,2.458943],[-1.993053,0.352654,-1.835407,-5.061519,8.641380,-5.954119,-8.271212,-7.756745,-4.783939,-2.721628,2.665246,0.234910],[-9.171228,7.787203,-1.601337,-3.769927,-3.889868,1.010280,-5.417282,-6.016451,-9.001634,-3.957057,6.984960,4.662999],[0.419344,-9.761663,6.880055,-9.071750,-1.721530,-6.621270,-1.375972,-6.571742,8.084127,8.746071,1.442230,5.661706],[-8.882362,-2.483078,-7.732329,-9.356419,3.970603,3.863251,-7.953940,-1.121585,1.488825,0.038763,8.611059,5.149610],[7.047008,2.376261,-4.828942,-4.845237,-4.077782,7.719818,0.924394,5.009731,-7.627595,7.849430,-6.150064,4.594106],[-1.774715,7.859308,-4.231326,-5.981835,1.270412,-8.766092,7.165709,-0.615614,-8.660311,-9.544036,2.561852,-0.912089],[-0.441824,4.469779,-0.649348,2.121499,9.446227,-9.342074,5.058047,-0.571998,-6.679162,-2.804082,4.021870,-3.217981],[-1.566892,5.913503,-0.158838,3.426555,7.294372,2.497668,-0.534598,9.801489,3.965137,7.498911,-7.566952,3.659583],[7.710874,-6.810084,-8.842703,-7.161578,-9.817409,6.375254,7.732656,7.295300,9.779222,-6.116341,1.849303,6.432783],[-8.620514,2.679987,-9.759478,3.203456,5.538031,2.122347,-2.871635,-9.697454,5.628204,1.594906,0.680811,-8.827837],[2.974690,-6.965643,-2.116450,9.140278,-7.901111,6.830562,8.122324,-5.937822,1.548844,8.060966,1.994322,-4.778305],[0.506147,-5.307250,-5.916033,7.526175,0.543385,8.872528,1.190059,-5.222631,1.113176,3.847640,0.233475,3.386127],[6.857477,-9.206237,0.517034,8.706352,3.656493,9.188602,-3.436124,7.573569,-3.256333,0.180880,-4.745516,1.008481],[-2.507959,-4.426560,2.703436,-9.297653,-9.195985,1.147030,2.239192,-0.235882,-5.692437,-4.047533,-2.672461,5.438689],[-9.822688,5.602828,-6.485435,2.164368,2.359120,-3.059201,6.137860,4.445749,-1.358090,8.771463,7.544602,-4.737523],[2.702297,9.003533,-9.607115,-0.293154,6.801740,5.039590,1.676004,-3.807373,4.440803,7.098840,2.750316,-0.862707],[7.243326,0.435904,-6.216157,0.354792,5.213555,3.313940,8.640059,-8.384127,4.726856,-7.125326,-5.898139,3.509149],[-1.514677,9.301734,4.329457,1.132190,7.522915,-3.649299,-5.993520,-3.754393,-8.249765,8.457563,6.780113,-3.749796],[-1.981617,1.053916,-8.735848,-5.902558,3.848912,-7.522421,3.556595,-3.418993,4.641344,-3.624978,-1.727041,7.224004],[4.774550,-2.506393,-8.786929,9.904282,7.914735,-3.627694,-8.984123,-1.152711,-6.963139,-6.431467,-0.382596,-2.636766],[7.019708,6.953856,9.276327,-5.664815,-7.248470,-8.027250,-3.275053,1.810201,-4.929113,9.994323,-5.406884,1.787578],[-9.170697,-7.768267,-0.601710,-9.196552,-0.209806,6.506859,-6.624165,-0.731416,-3.478343,-0.414645,-3.355231,-7.927557],[3.662895,5.916387,-3.990935,-7.905240,6.541663,5.877625,6.088452,2.362644,-4.860629,-5.312780,7.577133,5.828740],[4.483262,-2.587109,9.697182,-5.483474,-2.686361,-1.336925,-4.943845,6.241045,3.504359,4.115035,9.495848,-4.490758],[6.672672,-6.338857,5.018603,-3.897412,0.130138,1.193618,-7.156134,7.111981,1.083785,7.596605,-7.923060,8.274029],[9.293790,3.770915,-4.154279,-7.270475,-0.324927,-0.426379,-0.019996,-1.564152,6.797231,-9.405630,9.927260,-0.851177],[1.678322,2.713505,-5.415385,-8.738121,4.139182,-5.173509,8.925957,-2.165406,-3.173066,-4.026504,8.646640,-5.495754],[-9.444890,-2.144307,4.217425,-9.378545,-2.150530,-7.163221,7.935099,6.296948,-1.447102,-3.046068,-5.025216,3.276023],[4.975125,-2.300797,-3.278566,4.396136,3.905396,7.694150,-3.776185,-3.960231,4.929553,3.801940,0.321861,8.449804],[2.729119,4.491589,-4.607202,-4.193317,-6.986438,2.794235,8.136021,6.506178,-4.754926,7.148063,0.912112,-7.761456],[3.904633,6.888688,-3.010995,-5.471716,-3.381724,5.571045,2.825939,-6.949466,-0.112895,-0.181816,-3.670028,1.390869],[-0.792666,7.224875,-5.362758,-2.725011,9.627487,-3.025289,8.495180,4.853841,-2.531164,-0.512616,-9.355170,-9.284682],[-7.695995,9.704951,-7.712465,-7.962313,5.147559,-8.965249,8.996747,5.814385,-6.454418,-5.561549,6.526190,0.565253],[-3.138691,1.484628,-5.486896,-8.171541,-6.783830,2.543804,-8.382556,-7.459740,4.866855,5.853154,3.237746,-5.565618],[-4.031530,4.382648,-7.910115,5.418163,9.515667,-9.628853,-4.534774,-1.746673,-5.942478,-1.464312,0.630750,-9.950482],[1.439188,7.091547,0.671879,4.198159,-9.618839,8.242024,3.734891,-7.123173,1.192963,0.080648,2.415760,-1.333064],[5.093148,-2.938238,5.732726,-3.374592,-9.264786,-1.118450,4.308333,8.295792,-9.465010,-9.332856,7.854265,-2.317661],[7.662210,4.742310,-6.205295,-0.753689,-6.451455,-5.156180,-0.504782,-6.399236,8.112644,-3.447722,-7.222307,-6.309410],[-3.995582,6.698562,9.708094,-0.534932,0.873443,5.814186,5.508636,5.647290,-4.916393,-2.410376,-2.355625,7.106441],[5.782916,-8.946662,2.885705,-5.961147,-1.939212,-8.101440,-1.893989,-4.119530,-6.173845,9.791232,-8.883997,4.721171],[-0.429723,0.343882,-7.752119,-8.833828,-1.310861,-7.077085,-2.216689,8.294986,-0.221239,-4.366629,-5.565512,-9.731375],[5.813721,-3.033463,-1.733041,-8.732546,4.310036,-3.003870,0.025195,9.915427,9.420427,1.741970,7.939939,-3.801797],[-0.093589,-9.200234,-2.978362,6.869001,-0.425123,3.605616,0.825448,2.228790,3.703440,1.470659,6.909094,-6.394687],[-9.208608,-7.733254,-6.777239,6.409380,8.536435,2.645107,-1.355518,6.123725,-4.417361,4.434807,4.716565,3.483743],[-1.148602,6.727010,7.834007,9.520545,3.237304,8.376011,-6.942971,2.799184,-7.854686,6.895409,6.391252,5.374206],[9.219805,-3.343608,-1.595404,1.933789,-0.605463,-3.730850,-6.430615,2.223200,4.804270,1.234971,1.673627,4.001117],[1.093056,-0.747297,-6.781680,6.157641,-2.044327,-0.735054,2.992092,-5.126035,-0.748200,7.917314,-3.844440,-8.880558],[-5.377465,0.828545,-3.398314,3.290664,-1.100189,4.461432,-5.082323,-0.372675,-9.150808,4.447516,1.809041,8.267895],[-1.261077,-2.216173,9.097205,-1.576739,4.094216,1.577711,-2.738548,6.644431,-5.496828,5.471678,5.638237,8.946321],[-4.178774,3.233081,-7.946658,1.971287,-1.371933,0.907394,3.029781,4.706443,-9.434538,-6.139237,2.495988,4.196315],[-6.314489,-4.906150,-9.058612,0.136664,-5.726367,-0.380754,9.435547,8.030834,-0.739041,2.538900,-6.284783,-1.354255],[2.970946,-2.760902,-4.006863,-8.174529,-3.341043,8.534878,7.271888,-7.640156,8.936147,-7.317869,-6.216619,-3.365477],[8.960985,-9.432052,-9.688496,-9.153366,-9.072689,4.316686,-2.829929,7.048587,-0.342432,0.650969,-0.084767,-8.787437],[8.664394,-9.818890,-8.195991,-0.091761,0.893441,-9.578366,1.281955,6.039532,6.630101,-4.063103,9.559831,-4.898810],[-1.286341,5.029190,6.185216,5.064723,-2.488548,1.193432,-1.200568,-8.580386,-3.518126,-4.946583,7.432135,9.612293],[-5.552815,-4.186990,-1.806573,9.394653,5.987354,6.014172,-8.530713,9.730403,-1.286770,-9.525716,-4.249298,-2.512390],[0.238903,-9.257929,9.671132,6.384930,2.474743,7.403928,-0.798505,0.712101,4.242576,1.442790,7.000680,-8.907054],[6.499878,-6.921146,-1.671078,-5.536745,8.616157,-6.920870,7.640514,-0.010265,-3.806990,-5.917933,6.116731,-6.754533],[-1.686689,-7.537714,-9.847965,8.943214,6.813451,0.775431,8.225297,2.199401,-5.210483,9.169235,6.807508,-6.066646],[4.353151,4.011610,-7.840965,3.372048,6.601636,-6.643952,-7.335788,3.549294,-7.179489,9.585970,-2.002137,-9.497312],[8.077616,-6.104620,-2.410847,-4.761728,1.156458,-8.797563,4.831251,-2.490374,0.419600,-7.496361,6.194173,-6.471575],[-6.749494,0.047498,-2.879968,2.652012,6.533443,1.719556,-3.678090,0.773678,5.220623,-4.143970,0.999827,6.900302],[2.632350,-5.666087,8.863907,-2.846204,3.009859,-6.498113,-8.727927,3.869051,-5.303857,5.803780,-6.141590,-3.842322],[-7.646202,-2.284119,-5.600672,-4.106178,1.514377,-2.851255,2.041625,-4.589352,-3.237292,7.146568,-8.497540,-3.529183],[2.197974,4.001898,-9.048371,7.643889,-3.877244,-0.320115,2.751561,7.609999,9.013507,7.310681,-1.814499,1.860905],[-2.019297,8.078816,0.997425,8.293309,6.946601,-8.641786,6.740508,-3.738530,8.507678,-6.257843,-8.477876,4.244067],[3.355962,-2.453892,-2.591908,-9.637246,-6.073562,5.427996,3.464885,-4.353381,-4.228872,-7.384618,-9.230851,6.960702],[3.062891,-0.653111,9.980650,8.544434,-9.187362,7.045353,-1.511378,-5.623125,7.509389,-8.944083,-6.062228,-6.722210],[-4.794729,-9.995471,5.386185,-1.136222,3.117629,-5.719697,5.814045,8.993574,-4.939102,-1.116452,-7.093216,4.598188],[5.082276,-7.294728,5.028344,-7.940126,3.142470,-4.373323,-6.543961,3.647259,-6.446115,0.595724,-8.489433,7.923536],[2.574101,0.495481,-3.446717,4.882456,-5.857735,-9.112971,-4.047897,9.689770,4.362957,2.548090,7.084071,-4.986932],[-4.125817,4.837457,-1.326191,3.141426,-7.297922,-8.926404,-9.263949,-5.298366,7.220290,-6.000704,0.104535,-3.135325],[2.650689,8.171796,-0.977887,-7.184578,3.909276,0.149103,8.540061,3.568266,4.257108,-7.603495,5.680677,5.353784],[2.249690,9.125337,0.634038,-4.736258,2.552528,1.262223,4.651606,-7.829012,1.487923,-7.821613,6.310908,5.065716],[1.670849,-8.320803,-7.541823,-0.076539,3.242884,0.152804,9.154941,2.192123,1.311897,-7.381875,9.849882,1.860673],[6.877181,7.230606,1.175133,1.079205,-5.113563,7.197225,3.657876,0.943783,6.427346,-1.086937,-0.920206,3.926069],[-7.074898,-6.687083,2.777759,3.934902,0.278648,7.880705,7.611946,-1.240302,-5.465284,-1.485644,4.353273,-3.328923],[-1.068421,2.723991,-1.731912,-4.824615,-8.579184,-0.305618,-8.615242,-0.737872,-8.619150,-9.266226,9.801878,-7.979812],[7.753481,6.281296,-0.407166,7.202955,-9.419052,2.288024,-3.802471,-2.366419,-5.546189,-5.545000,-4.706475,-4.514669],[-2.334784,-3.000420,8.135271,6.845945,1.291453,4.739666,-9.624233,7.943905,7.475313,1.998109,-9.102860,3.986234],[4.519645,-5.184118,-8.567866,-5.556376,4.449117,-4.244041,7.423709,8.076766,5.316802,-3.773732,-2.829296,-6.591544],[-5.350087,4.183614,6.435131,3.239645,-7.616533,-6.194977,0.975369,7.089714,2.273456,9.661431,0.646086,-0.564882],[-2.433427,-1.450616,-5.229030,-9.097478,-8.309203,9.415186,-7.238293,-0.113826,-9.021356,-1.592002,-2.266641,6.176956],[8.110059,-0.495737,1.330522,7.643591,-9.396747,-5.657494,7.834502,7.756228,-1.382791,7.587854,-0.277838,1.076669]], dtype = "float64")#candidate|3922|(126, 12)|const|float64
const_3923 = relay.const([[False,True],[False,True],[False,True],[False,False],[True,True],[True,False],[False,False],[True,False],[True,True],[True,True],[False,False],[True,False],[False,False],[True,False],[False,False],[True,False],[False,True],[False,False],[True,False],[False,False],[True,False],[False,False],[False,False],[False,True],[True,True],[True,True],[False,False],[True,False],[False,True],[False,False],[True,True],[True,True],[True,True],[False,False],[True,False],[False,True],[False,False],[True,True],[False,True],[False,True],[True,True],[False,True],[False,False],[True,False],[True,True],[True,False],[True,False],[False,False],[True,False],[False,False],[False,False],[True,True],[False,False],[False,True],[False,False],[False,True],[False,True],[False,False],[True,True],[False,False],[False,True],[False,True],[True,False],[True,False],[False,True],[True,True],[True,False],[False,False],[True,False],[True,True],[False,True],[False,False],[False,False],[False,True],[True,True],[True,True],[False,False],[True,False],[False,False],[False,True],[False,True],[False,True],[False,False],[True,True],[False,False],[False,False],[False,False],[True,False],[False,True],[False,True],[False,True],[False,True],[True,True],[True,False],[False,True],[True,False],[True,True],[True,True],[True,True],[False,True],[True,False],[True,True],[False,False],[False,False],[False,False],[True,False],[True,True],[True,True],[True,False],[True,True],[False,False],[True,True],[True,False],[False,False],[True,False],[True,True],[False,False],[False,False],[True,False],[False,True],[False,True],[True,False],[False,True],[True,True],[True,False],[False,True],[False,True],[False,True],[False,False],[True,True],[False,False],[False,False],[False,True],[False,True],[True,False],[False,False],[True,False],[False,False],[True,True],[True,False],[True,False],[False,True],[True,False],[False,True],[True,True],[True,True],[True,True],[False,True],[False,False],[True,False],[True,True],[False,False],[True,False],[False,False],[True,False],[True,False],[False,True],[True,True],[True,True],[True,False],[False,False],[False,True],[True,False],[False,False],[False,True],[False,True],[True,False],[False,False]], dtype = "bool")#candidate|3923|(168, 2)|const|bool
const_3924 = relay.const([True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True], dtype = "bool")#candidate|3924|(672,)|const|bool
var_3925 = relay.var("var_3925", dtype = "uint64", shape = (1152,))#candidate|3925|(1152,)|var|uint64
call_3919 = relay.TupleGetItem(func_3727_call(relay.reshape(var_3920.astype('float64'), [1, 10, 9]), relay.reshape(const_3921.astype('float64'), [11, 10, 9]), relay.reshape(const_3922.astype('float64'), [1512,]), relay.reshape(const_3923.astype('bool'), [4, 84]), relay.reshape(const_3924.astype('bool'), [672,]), relay.reshape(var_3925.astype('uint64'), [1152,]), ), 2)
call_3926 = relay.TupleGetItem(func_3735_call(relay.reshape(var_3920.astype('float64'), [1, 10, 9]), relay.reshape(const_3921.astype('float64'), [11, 10, 9]), relay.reshape(const_3922.astype('float64'), [1512,]), relay.reshape(const_3923.astype('bool'), [4, 84]), relay.reshape(const_3924.astype('bool'), [672,]), relay.reshape(var_3925.astype('uint64'), [1152,]), ), 2)
output = relay.Tuple([call_3901,call_3905,call_3912,call_3919,var_3920,const_3921,const_3922,const_3923,const_3924,var_3925,])
output2 = relay.Tuple([call_3902,call_3906,call_3913,call_3926,var_3920,const_3921,const_3922,const_3923,const_3924,var_3925,])
func_3950 = relay.Function([var_3920,var_3925,], output)
mod['func_3950'] = func_3950
mod = relay.transform.InferType()(mod)
mutated_mod['func_3950'] = func_3950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mutated_mod.get_global_var('func_3950')
var_3952 = relay.var("var_3952", dtype = "float64", shape = (15, 6))#candidate|3952|(15, 6)|var|float64
var_3953 = relay.var("var_3953", dtype = "uint64", shape = (1152,))#candidate|3953|(1152,)|var|uint64
call_3951 = func_3950_call(var_3952,var_3953,)
output = call_3951
func_3954 = relay.Function([var_3952,var_3953,], output)
mutated_mod['func_3954'] = func_3954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_4046 = func_3536_call()
call_4047 = func_3536_call()
func_2152_call = mod.get_global_var('func_2152')
func_2155_call = mutated_mod.get_global_var('func_2155')
const_4064 = relay.const([-5,2,10,-2,3,9,7,-10,-10,-7,-4,10,3,7,9,2,1,-5,2,-1,1,4,5,5,4,10,-8,-2,-2,-6,3,2,4,4,-7,2,-7,8,-2,-7,4,6,8,2,7,9,-6,3,-10,-7,-3,5,-7,2,-5,-6,6,10,10,-4,-9,-6,-5,6,-7,2,-4,-10,1,2,2,-4,10,4,3,-6,2,7,10,-5,-8,6,6,-5,-9,3,-7,-10,1,8,4,8,5,-3,1,-1,-5,-3,5,9,6,-3,-1,9,-9,-7,10,-8,3,7,1,4,-7,8,6,-5,-1,5,-1,5,-3,2,-10,-6,4,-8,5,3,-9,-3,-10,7,-7,5,-9,10,5,-5,6,9,-9,5,6,-6,-10,-2,-7,2,-1,4,9,4,-7,8,-2,-3,3,5,-7,6,9,-8,7,10,6,10,9,-9,4,-2,-6,7,3,9,-10,9,-5,6,4,-1,-2,-8,-6,-9,-4,-7,6,-10,-6,10,7,5,-4,-3,-9,-3,-5,3,-7,2,-5,-4,2,9,6,-4,-9,-5,2,-5,2,3,8,1,-10,7,-3,-6,6,5,-7,4,-7,-2,9,-9,3,10,-10,7,5,5,6,5,1,5,-8,-5,-10,-6,-2,9,7,-7,4,6,7,-9,7,6,-3,-3,9,-8,4,-5,-6,-2,-8,1,4,-1,-1,5,-6,5,9,2,7,-5,3,7,-8,4,9,-8,-5,5,3,5,10,-1,-7,7,5,4,3,7,10,9,-9,4,10,-3,9,2,-9,8,-8,-1,-6,8,6,-3,7,8,1,-3,1,-3,5,10,8,9,1,-6,-4,-6,-10,-9,-3,6,-6,6,-4,-8,4,-2,-5,8,-10,1,-1,-6,-8,-1,-1,6,5,-7,-2,-9,-4,-1,-1,-5,5,6,-4,8,-9,-4,5,2,-3,2,-5,-4,-9,7,3,-10,-7,4,-1,3,1,-4,9,-8,-2,-8,9,-5,-6,-10,-4,7,1,3,2,-3,5,-9,3,7,-8,-4,6,7,4,10,2,-1,9,-4,-4,-3,-6,3,8,5,-4,2,8,3,1,-2,-3,3,-1,-2,-5,1,-5,-9,4,-10,-2,-8,4,-4,7,7,3,1,-6,-6,-5,-2,-3,5,6,-4,10,1,-5,10,-3,1,6,9,-6,4,-3,-4,-9,4,6,2,-3,-1,-9,10,7,-9,7,6,-4,5,-9,6,7,3,-1,1,-9,-2,-1,-10,8,-1,7,6,-10,-1,-9,-6,8,-2,-4,2,-5,-2,7,-5,1,-7,3,-10,-6,1,9,-2,7,-3,-8,6,9,8,-8,-10,8,7,-5,-4,9,4,3,4,-1,2,-2,-3,-6,7,-3,-5,8,-2,-1,4,2,-10,4,-4,1,-6,-6,-5,9,8,-3,-5,-7,4,5,-9,-5,-1,-5,6,3,-10,-1,3,9,4,-4,-2,7,-8,5,-9,-10,-1,-7,2,9,3,9,1,-7,1,-7,-4,-3,9,2,8,10,9,-6,-9,5,6,8,-3,6,6,-8,-8,-3,-9,-4,-10,-6,-2,-2,-7,3,-2,-5,-5,10,2,4,-1,8,-5,-8,-7,-4,9,1,2,1,6,10,7,-7,-9,1,-9,9,1,8,4,-8,9,-8,7,6,5,7,5,-1,4,-4,2,8,3,-3,10,-1,-3,10,10,3,2,-9,5,-1,3,3,-1,9,9,-2,-5,5,-1,10,-3,-7,5,3,-6,-9,2,-6,-5,8,7,2,-4,-2,4,-6,-4,-3,1,-9,4,7,1,10,8,-1,-1,-9,-10,2,2,2,-3,5,4,-2,-3,6,-4,-4,-6,9,8,4,8,1,-4,-8,-9,-4,8,-1,6,-6,6,3,5,-1,10,10,-1,-10,5,5,-10,8,4,-10,9,-9,6,-6,3,-3,-5,1,-5,3,6,5,-7,-5,-6,-9,10,1,1,-8,-7,5,5,7,6,9,8,-9,1,-5,-8,-4,-4,6,-4,-8,-7,-10,1,-4,9,-9,9,1,-4,9,-1,-2,-7,10,5,10,-3,6,-10,-2,-6,-6,-1,-7,5,6,-6,-3,-7,4,-3,5,9,-1,-2,9,-6,-2,-4,-9,-4,5,1,3,-10,-9,-5,10,-6,2,4,7,-8,6,-10,1,9,-4,-3,-8,5,-8,4,4,-1,-7,8,4,4,8,-4,-8,4,-3,8,-3,-3,-3,1,4,-4,6,8,7,-9,-6,3,-5,-3,-3,-2,-3,-7,1,-4,9,-7,-9,4,-6,3,5,-5,3,1,-8,2,9,10,9,-4,-1,3,7,-7,8,5,6,-4,-8,4,-7,1,-8,-5,-4,-5,-1,4,4,8,-1,-7,-3,-5,5,8,6,9,10,-10,4,-9,4,2,-7,1,-5,5,7,-10,-9,-6,8,8,-1,2,4,2,-7,5,9,1,4,4,6,-6,4,10,9,-2,8,8,7,1,6,-7,-4,9,-4,9,-8,-7,-7,6,6,-6,4,-8,6,7,5,-9,2,-7,10,10,-1,2,-3,3,6,6,5,-1,3,-5,1,9,1,-2,4,-10,-9,4,-1,-5,-8,7,7,6,-5,10,4,-1,-9,-7,7,9,-10,-9,-10,7,7,1,1,6,8,-6,-7,-9,-2,-1,-6,6,-5,-8,-1,-3,9,4,3,8,6,-6,-10,1,-3,-2,5,6,5,5,9,6,-3,-7,-10,8,8,-1,10,8,-4,-6,-8,-1,6,-1,-5,4,9,4,6,-5,7,1,-8,5,-1,3,3,2,-9,6,-2,-1,4,8,7,-4,-9,-4,-6,-1,9,-8,-7,4,5,-1,2,6,9,-4,9,-3,-3,-7,5,7,1,6,6,-7,2,6,2,-8,7,-7,1,7,8,-4,4,-9,-7,-7,7,-3,-2,10,2,4,3,-8,-3,10,-10,6,-8,-1,2,-7,1,-7,-1,-6,-7,4,2,-4,-6,-6,-9,-2,-7,-1,2,7,9,6,-3,5,-1,-1,3,-7,10,-7,4,-5,4,-10,-7,8,3,8,-6,-7,3,9,-3,-5], dtype = "uint64")#candidate|4064|(1152,)|const|uint64
call_4063 = func_2152_call(relay.reshape(const_4064.astype('uint64'), [12, 16, 6]), relay.reshape(const_4064.astype('uint64'), [12, 16, 6]), )
call_4065 = func_2152_call(relay.reshape(const_4064.astype('uint64'), [12, 16, 6]), relay.reshape(const_4064.astype('uint64'), [12, 16, 6]), )
output = relay.Tuple([call_4046,call_4063,const_4064,])
output2 = relay.Tuple([call_4047,call_4065,const_4064,])
func_4068 = relay.Function([], output)
mod['func_4068'] = func_4068
mod = relay.transform.InferType()(mod)
output = func_4068()
func_4069 = relay.Function([], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_4095 = relay.TupleGetItem(func_3130_call(), 0)
call_4096 = relay.TupleGetItem(func_3131_call(), 0)
var_4123 = relay.var("var_4123", dtype = "float32", shape = (8, 15, 4))#candidate|4123|(8, 15, 4)|var|float32
bop_4124 = relay.divide(call_4095.astype('float32'), relay.reshape(var_4123.astype('float32'), relay.shape_of(call_4095))) # shape=(8, 15, 4)
bop_4127 = relay.divide(call_4096.astype('float32'), relay.reshape(var_4123.astype('float32'), relay.shape_of(call_4096))) # shape=(8, 15, 4)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_4136 = func_3896_call()
call_4137 = func_3896_call()
output = relay.Tuple([bop_4124,call_4136,])
output2 = relay.Tuple([bop_4127,call_4137,])
func_4139 = relay.Function([var_4123,], output)
mod['func_4139'] = func_4139
mod = relay.transform.InferType()(mod)
var_4140 = relay.var("var_4140", dtype = "float32", shape = (8, 15, 4))#candidate|4140|(8, 15, 4)|var|float32
output = func_4139(var_4140)
func_4141 = relay.Function([var_4140], output)
mutated_mod['func_4141'] = func_4141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3314_call = mod.get_global_var('func_3314')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_4150 = relay.TupleGetItem(func_3314_call(), 0)
call_4151 = relay.TupleGetItem(func_3316_call(), 0)
const_4154 = relay.const([[[True,False,True,False,True,True,True,True,False,True,False,True,False,True,False],[False,False,True,False,True,False,True,False,False,True,True,False,True,False,False],[True,False,False,False,False,True,True,True,True,True,False,True,True,False,False],[True,False,True,False,True,False,True,False,False,True,False,True,True,True,True],[True,True,True,False,True,True,True,True,False,False,False,False,True,True,False]],[[False,True,True,True,True,False,True,False,False,True,True,False,False,True,False],[True,False,True,True,False,False,False,False,True,True,False,False,True,False,True],[False,False,False,True,True,False,True,False,False,True,True,False,False,True,True],[False,False,True,True,True,False,True,False,False,True,True,False,True,False,False],[False,False,False,True,True,True,True,False,True,True,False,False,True,False,True]],[[False,False,False,False,True,True,False,False,True,False,True,False,False,False,True],[True,True,True,True,False,True,True,True,True,False,False,True,True,False,True],[False,False,True,False,False,False,False,False,True,True,False,False,False,True,True],[True,False,False,False,True,False,True,False,True,True,True,True,False,False,True],[False,False,False,True,True,False,False,True,True,True,False,True,True,False,False]],[[False,True,False,False,False,False,False,True,False,True,False,True,True,True,True],[False,True,False,False,False,True,True,False,False,False,True,False,True,True,True],[False,True,False,False,False,False,False,False,False,True,False,False,False,True,True],[False,True,False,False,False,True,True,True,True,True,True,True,True,False,False],[False,False,True,True,True,True,True,True,False,True,False,False,False,True,True]],[[True,True,False,False,True,False,True,False,True,False,True,False,True,False,True],[True,True,True,True,False,False,False,True,False,False,True,False,False,True,True],[True,False,False,False,False,True,False,True,True,False,False,False,False,True,True],[True,True,False,True,False,False,True,False,True,True,True,False,False,True,True],[True,True,False,False,True,False,True,True,False,True,True,False,True,False,True]],[[False,True,False,False,False,False,False,False,True,False,True,False,False,True,True],[False,True,False,False,True,True,False,False,True,False,True,False,False,True,False],[False,True,False,False,False,False,True,False,False,False,False,False,False,True,True],[True,True,False,False,True,True,True,True,False,False,False,True,True,False,False],[True,False,False,True,True,False,False,False,False,False,False,True,False,False,False]],[[False,True,True,False,True,False,False,True,True,False,True,True,True,False,False],[False,False,False,False,True,True,False,True,True,False,False,True,True,False,True],[True,False,True,False,True,False,False,True,True,False,True,True,True,False,True],[True,False,True,False,False,True,True,False,False,True,True,False,False,False,True],[False,False,True,True,False,False,True,True,True,True,True,False,False,False,True]],[[True,False,True,True,False,False,False,True,False,False,False,True,True,True,False],[False,True,False,True,False,False,False,True,True,True,False,False,False,False,True],[True,False,True,False,True,True,False,True,False,True,True,True,False,False,False],[False,False,True,False,False,True,True,False,False,False,True,True,True,True,True],[False,False,True,True,True,False,False,True,True,False,False,True,True,True,True]],[[True,True,False,False,False,False,True,True,False,False,True,True,True,False,True],[False,False,True,False,True,False,False,True,False,False,False,False,True,True,True],[False,True,True,False,True,True,False,True,False,False,True,True,False,False,False],[True,False,False,False,False,False,True,True,True,True,True,True,True,False,True],[True,False,False,False,True,True,True,True,False,True,False,True,False,False,True]],[[False,True,False,True,True,False,True,False,True,False,True,False,False,True,False],[True,False,True,True,False,False,False,True,True,True,False,True,False,False,True],[False,True,False,False,False,False,False,True,False,False,True,False,False,True,True],[True,False,True,False,True,True,False,False,False,True,True,False,True,True,False],[False,True,True,True,True,True,True,False,False,True,False,False,True,False,True]],[[False,True,False,True,True,True,False,True,True,False,True,False,False,False,False],[True,False,True,False,True,True,False,False,True,False,False,True,False,True,True],[False,False,True,False,True,False,True,False,False,True,False,True,True,True,True],[True,False,True,True,False,True,False,False,True,True,True,True,False,True,True],[True,True,True,False,True,False,True,True,False,True,False,True,False,True,False]],[[True,True,False,False,False,False,True,False,True,True,True,False,False,True,True],[True,False,True,False,True,False,True,False,True,True,True,True,False,True,True],[False,False,False,False,False,False,True,False,False,False,True,True,False,True,False],[True,True,False,False,True,True,True,False,True,False,False,False,False,False,True],[True,True,True,True,True,False,True,False,False,True,False,True,False,False,False]],[[False,False,True,False,False,True,False,True,True,True,False,True,False,False,False],[True,True,True,True,False,False,True,True,True,True,False,True,False,False,False],[False,False,False,False,False,False,True,False,False,False,False,False,False,False,False],[False,True,True,True,False,True,True,True,False,False,False,False,False,False,False],[False,True,False,False,True,False,False,False,True,False,False,True,False,False,True]],[[False,False,False,True,True,True,False,True,False,False,True,True,False,True,True],[False,True,False,False,True,True,True,False,True,False,False,False,True,True,False],[False,True,True,False,True,False,True,True,True,False,False,True,True,False,False],[False,True,False,True,True,True,False,False,True,False,False,False,False,True,True],[False,True,False,True,False,True,False,True,True,True,True,True,False,False,True]],[[True,True,False,True,False,False,False,False,False,False,False,True,False,False,False],[True,True,False,True,False,False,True,False,True,False,False,True,True,False,True],[False,True,False,True,False,False,True,True,True,True,True,True,False,True,False],[True,False,True,True,True,True,True,False,False,False,False,False,True,True,False],[True,False,False,True,True,False,False,False,True,True,True,False,False,False,True]],[[False,True,True,True,False,True,True,True,True,True,True,False,True,True,True],[True,False,True,True,True,False,False,True,False,True,False,False,False,True,False],[True,True,True,True,True,True,False,False,False,True,True,True,True,False,False],[True,True,False,False,True,False,True,True,True,True,False,False,True,False,True],[True,False,False,False,True,True,True,True,True,True,False,False,True,False,False]]], dtype = "bool")#candidate|4154|(16, 5, 15)|const|bool
bop_4155 = relay.less_equal(call_4150.astype('bool'), relay.reshape(const_4154.astype('bool'), relay.shape_of(call_4150))) # shape=(16, 5, 15)
bop_4158 = relay.less_equal(call_4151.astype('bool'), relay.reshape(const_4154.astype('bool'), relay.shape_of(call_4151))) # shape=(16, 5, 15)
output = relay.Tuple([bop_4155,])
output2 = relay.Tuple([bop_4158,])
func_4162 = relay.Function([], output)
mod['func_4162'] = func_4162
mod = relay.transform.InferType()(mod)
output = func_4162()
func_4163 = relay.Function([], output)
mutated_mod['func_4163'] = func_4163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4163_call = mutated_mod.get_global_var('func_4163')
call_4174 = relay.TupleGetItem(func_4162_call(), 0)
call_4175 = relay.TupleGetItem(func_4163_call(), 0)
output = call_4174
output2 = call_4175
func_4197 = relay.Function([], output)
mod['func_4197'] = func_4197
mod = relay.transform.InferType()(mod)
mutated_mod['func_4197'] = func_4197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4197_call = mutated_mod.get_global_var('func_4197')
call_4198 = func_4197_call()
output = call_4198
func_4199 = relay.Function([], output)
mutated_mod['func_4199'] = func_4199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4163_call = mutated_mod.get_global_var('func_4163')
call_4210 = relay.TupleGetItem(func_4162_call(), 0)
call_4211 = relay.TupleGetItem(func_4163_call(), 0)
var_4218 = relay.var("var_4218", dtype = "bool", shape = (16, 5, 15))#candidate|4218|(16, 5, 15)|var|bool
bop_4219 = relay.logical_or(call_4210.astype('bool'), relay.reshape(var_4218.astype('bool'), relay.shape_of(call_4210))) # shape=(16, 5, 15)
bop_4222 = relay.logical_or(call_4211.astype('bool'), relay.reshape(var_4218.astype('bool'), relay.shape_of(call_4211))) # shape=(16, 5, 15)
func_2477_call = mod.get_global_var('func_2477')
func_2482_call = mutated_mod.get_global_var('func_2482')
var_4231 = relay.var("var_4231", dtype = "bool", shape = (336,))#candidate|4231|(336,)|var|bool
const_4232 = relay.const(9, dtype = "int32")#candidate|4232|()|const|int32
var_4233 = relay.var("var_4233", dtype = "bool", shape = (56, 12))#candidate|4233|(56, 12)|var|bool
call_4230 = relay.TupleGetItem(func_2477_call(relay.reshape(var_4231.astype('bool'), [7, 16, 3]), relay.reshape(const_4232.astype('int32'), []), relay.reshape(var_4233.astype('bool'), [14, 16, 3]), ), 0)
call_4234 = relay.TupleGetItem(func_2482_call(relay.reshape(var_4231.astype('bool'), [7, 16, 3]), relay.reshape(const_4232.astype('int32'), []), relay.reshape(var_4233.astype('bool'), [14, 16, 3]), ), 0)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_4237 = func_3536_call()
call_4238 = func_3536_call()
func_2152_call = mod.get_global_var('func_2152')
func_2155_call = mutated_mod.get_global_var('func_2155')
const_4240 = relay.const([[-3,-4,-9,-8,-3,-7,3,2,9,2,3,9,4,7,-7,7,-7,8,-5,-8,7,-5,-5,-8,7,4,5,2,-7,1,-1,5,9,-4,10,-5,7,-1,6,-7,-1,-5,-4,-8,-7,4,7,-5],[-3,-3,1,3,-7,-10,-4,-6,-10,1,-9,5,-8,-1,10,-1,7,9,-1,7,7,-1,-6,7,-1,2,-9,-3,7,2,-1,2,9,7,-6,-10,-4,3,1,8,10,9,8,-4,5,6,-1,6],[-2,1,-9,-8,-1,3,-2,-3,2,10,3,6,-2,-6,1,-2,-6,10,4,-6,-10,9,1,-4,6,-2,-8,1,-9,4,10,4,8,1,9,-7,8,10,-9,-2,-8,6,-3,7,-5,-3,-6,-10],[8,-6,-1,-7,-10,8,-3,4,5,9,-6,-9,7,5,8,8,9,4,-9,-10,-1,-6,-9,8,-10,-3,5,-9,-5,-8,2,-10,1,10,8,-7,-8,-3,-3,4,-8,-4,-8,-5,-7,-5,-8,1],[-10,7,1,-7,7,10,1,-7,-1,-1,-4,-2,-1,2,-4,9,4,-4,-2,-7,-10,-2,9,1,-10,8,1,7,-9,-3,3,-8,10,3,-2,-4,7,5,-5,7,9,1,7,3,-8,10,-10,10],[2,-3,-4,-9,3,7,10,-5,-9,-2,4,-4,-4,4,5,-4,-7,-3,6,-4,-8,8,6,9,-10,4,8,6,2,-6,2,-6,-8,2,5,-2,-6,2,-4,7,-4,5,9,-6,1,-10,3,-4],[6,-3,-1,-3,5,-10,8,2,10,-6,9,2,5,5,-7,-8,-6,-6,-8,-7,-6,-4,6,-8,3,7,-7,4,-10,-9,9,-4,2,5,8,-5,-10,-1,-4,3,3,9,-9,-2,-3,10,10,-8],[-3,-4,-6,-7,9,3,7,1,7,9,-3,7,-2,10,10,-8,-3,-5,-5,-3,2,-8,-3,-8,8,-6,-8,7,-1,-6,4,-5,-6,6,-5,-6,7,4,4,8,-1,3,7,-1,-8,9,-1,-1],[-5,10,7,6,1,-4,4,-9,6,6,3,-2,-4,-6,-7,2,3,-3,10,-6,1,-8,-2,2,8,-3,-3,5,-10,-2,6,-9,10,1,1,-2,9,-7,-6,1,7,8,-3,-9,2,7,9,-8],[10,-8,-9,5,-10,-9,3,4,-5,2,-3,-10,4,2,-5,-4,-2,-8,-3,-10,-5,-1,2,8,6,-7,1,-6,5,10,-10,7,-7,6,-7,-4,9,3,-1,-9,3,7,-1,10,-3,-6,-7,9],[-7,3,-3,-10,-2,-2,-6,-9,-6,2,1,5,-4,-1,3,2,-4,8,4,10,9,-7,4,3,-6,9,-6,-3,5,-1,3,10,10,7,-6,-10,-10,9,4,-5,-6,10,-7,2,9,10,-7,-3],[8,3,-8,10,-9,-3,-2,5,-1,2,10,-9,9,2,2,5,5,6,8,-1,-5,-1,-1,5,-1,-1,2,9,1,-5,7,3,-7,-3,-4,-3,-9,8,-1,1,9,-3,3,-10,5,7,9,-2],[-10,-3,-1,5,-1,7,5,1,1,-7,-8,-9,6,5,-6,2,-3,-2,9,2,10,1,-1,-3,8,7,7,-9,1,-8,10,-5,-3,7,4,-4,-1,2,-7,4,-5,3,8,6,-7,-6,-4,-2],[-6,3,-8,-6,1,-3,-5,6,-10,3,-3,5,5,9,-2,8,-7,10,7,-8,-6,-9,-8,2,-5,5,-5,-8,-2,10,7,2,9,1,7,-6,-10,5,-9,-5,-3,-4,1,-9,-8,-6,6,-9],[9,-3,-9,1,-4,-7,-5,-9,3,7,5,6,6,10,-2,-9,1,7,-10,9,-7,9,1,8,-9,-9,-2,10,8,10,-9,9,2,9,-6,-8,-7,3,-4,3,8,10,6,8,9,4,-8,7],[-2,-5,-7,1,9,3,9,-9,-7,-6,8,-8,3,-7,6,-2,2,-7,10,4,-6,-5,2,-3,-2,5,5,6,-5,9,-7,-2,-10,-8,8,2,-7,-10,-10,10,-4,-1,-8,6,-2,-7,-8,7],[-9,-8,5,3,-8,2,8,9,9,-2,9,-2,-5,-9,9,10,-9,5,8,-7,-4,4,3,5,-7,10,-5,6,-3,-2,3,2,-10,-7,6,-5,-4,-2,6,10,-6,-9,5,2,2,-2,-4,8],[-3,4,-8,-10,10,1,3,9,-2,-10,-4,2,-6,3,-1,6,6,3,-9,-8,7,6,9,-9,4,5,-4,3,3,2,7,-8,-5,6,-6,-4,-4,-2,4,3,3,-5,6,8,6,-5,-5,-5],[-6,4,-5,-4,9,-1,9,2,-1,10,-6,9,6,4,-9,-4,2,-8,8,-8,-9,-1,-3,10,-9,3,9,-5,10,-8,10,5,-2,9,-4,-9,3,1,3,4,-2,-5,-1,-9,4,9,1,-4],[-8,7,7,6,5,10,1,-10,-10,-5,9,-3,3,-5,-9,-9,1,10,-9,-9,-6,-4,2,-9,1,7,-7,-3,6,5,6,-2,-10,-6,-1,-5,6,3,3,2,5,4,-10,4,-4,1,5,-8],[10,-3,-8,7,6,-2,1,3,-3,-9,3,-9,4,-6,7,-1,-5,-7,1,-9,-3,7,4,9,-6,-10,-2,5,-1,3,2,-5,8,-4,-6,-7,-3,-1,4,-4,-8,1,-5,8,-7,6,-6,-10],[2,3,-6,-5,5,-8,7,1,-8,9,-1,1,-7,9,7,8,-3,7,1,8,9,-7,2,6,-10,-5,-2,-9,3,-4,9,-2,-3,10,3,2,-8,2,6,-9,-3,-9,1,7,10,-6,3,9],[-9,4,1,-3,6,6,-3,10,9,4,1,-6,3,8,-4,-4,8,-4,-3,-7,-4,10,-9,-7,4,-10,3,6,2,3,-2,10,4,-10,-2,-5,9,-6,-8,7,-6,-4,7,-6,5,4,8,-9],[7,-9,-4,7,-10,2,-10,9,-7,7,-5,2,2,-7,-1,3,6,9,4,5,-3,-3,5,-8,-5,6,-8,9,-6,2,-5,-5,5,-10,2,-7,10,7,-10,-10,2,4,-6,-9,9,10,-6,-4]], dtype = "uint64")#candidate|4240|(24, 48)|const|uint64
call_4239 = func_2152_call(relay.reshape(const_4240.astype('uint64'), [12, 16, 6]), relay.reshape(const_4240.astype('uint64'), [12, 16, 6]), )
call_4241 = func_2152_call(relay.reshape(const_4240.astype('uint64'), [12, 16, 6]), relay.reshape(const_4240.astype('uint64'), [12, 16, 6]), )
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_4264 = relay.TupleGetItem(func_4068_call(), 0)
call_4265 = relay.TupleGetItem(func_4069_call(), 0)
output = relay.Tuple([bop_4219,call_4230,var_4231,const_4232,var_4233,call_4237,call_4239,const_4240,call_4264,])
output2 = relay.Tuple([bop_4222,call_4234,var_4231,const_4232,var_4233,call_4238,call_4241,const_4240,call_4265,])
func_4275 = relay.Function([var_4218,var_4231,var_4233,], output)
mod['func_4275'] = func_4275
mod = relay.transform.InferType()(mod)
mutated_mod['func_4275'] = func_4275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4275_call = mutated_mod.get_global_var('func_4275')
var_4277 = relay.var("var_4277", dtype = "bool", shape = (16, 5, 15))#candidate|4277|(16, 5, 15)|var|bool
var_4278 = relay.var("var_4278", dtype = "bool", shape = (336,))#candidate|4278|(336,)|var|bool
var_4279 = relay.var("var_4279", dtype = "bool", shape = (56, 12))#candidate|4279|(56, 12)|var|bool
call_4276 = func_4275_call(var_4277,var_4278,var_4279,)
output = call_4276
func_4280 = relay.Function([var_4277,var_4278,var_4279,], output)
mutated_mod['func_4280'] = func_4280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_4371 = func_3896_call()
call_4372 = func_3896_call()
var_4397 = relay.var("var_4397", dtype = "bool", shape = (8, 15, 4))#candidate|4397|(8, 15, 4)|var|bool
bop_4398 = relay.subtract(call_4371.astype('float32'), relay.reshape(var_4397.astype('float32'), relay.shape_of(call_4371))) # shape=(8, 15, 4)
bop_4401 = relay.subtract(call_4372.astype('float32'), relay.reshape(var_4397.astype('float32'), relay.shape_of(call_4372))) # shape=(8, 15, 4)
output = bop_4398
output2 = bop_4401
func_4402 = relay.Function([var_4397,], output)
mod['func_4402'] = func_4402
mod = relay.transform.InferType()(mod)
var_4403 = relay.var("var_4403", dtype = "bool", shape = (8, 15, 4))#candidate|4403|(8, 15, 4)|var|bool
output = func_4402(var_4403)
func_4404 = relay.Function([var_4403], output)
mutated_mod['func_4404'] = func_4404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_4415 = func_3759_call()
call_4416 = func_3759_call()
output = relay.Tuple([call_4415,])
output2 = relay.Tuple([call_4416,])
func_4417 = relay.Function([], output)
mod['func_4417'] = func_4417
mod = relay.transform.InferType()(mod)
output = func_4417()
func_4418 = relay.Function([], output)
mutated_mod['func_4418'] = func_4418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4197_call = mod.get_global_var('func_4197')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_4448 = func_4197_call()
call_4449 = func_4197_call()
func_4417_call = mod.get_global_var('func_4417')
func_4418_call = mutated_mod.get_global_var('func_4418')
call_4457 = relay.TupleGetItem(func_4417_call(), 0)
call_4458 = relay.TupleGetItem(func_4418_call(), 0)
output = relay.Tuple([call_4448,call_4457,])
output2 = relay.Tuple([call_4449,call_4458,])
func_4475 = relay.Function([], output)
mod['func_4475'] = func_4475
mod = relay.transform.InferType()(mod)
output = func_4475()
func_4476 = relay.Function([], output)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4197_call = mod.get_global_var('func_4197')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_4487 = func_4197_call()
call_4488 = func_4197_call()
output = relay.Tuple([call_4487,])
output2 = relay.Tuple([call_4488,])
func_4504 = relay.Function([], output)
mod['func_4504'] = func_4504
mod = relay.transform.InferType()(mod)
mutated_mod['func_4504'] = func_4504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4504_call = mutated_mod.get_global_var('func_4504')
call_4505 = func_4504_call()
output = call_4505
func_4506 = relay.Function([], output)
mutated_mod['func_4506'] = func_4506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4417_call = mod.get_global_var('func_4417')
func_4418_call = mutated_mod.get_global_var('func_4418')
call_4587 = relay.TupleGetItem(func_4417_call(), 0)
call_4588 = relay.TupleGetItem(func_4418_call(), 0)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
call_4618 = relay.TupleGetItem(func_4139_call(relay.reshape(call_4587.astype('float32'), [8, 15, 4])), 0)
call_4619 = relay.TupleGetItem(func_4141_call(relay.reshape(call_4587.astype('float32'), [8, 15, 4])), 0)
output = relay.Tuple([call_4587,call_4618,])
output2 = relay.Tuple([call_4588,call_4619,])
func_4634 = relay.Function([], output)
mod['func_4634'] = func_4634
mod = relay.transform.InferType()(mod)
mutated_mod['func_4634'] = func_4634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4634_call = mutated_mod.get_global_var('func_4634')
call_4635 = func_4634_call()
output = call_4635
func_4636 = relay.Function([], output)
mutated_mod['func_4636'] = func_4636
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4687 = relay.var("var_4687", dtype = "int16", shape = ())#candidate|4687|()|var|int16
var_4688 = relay.var("var_4688", dtype = "int16", shape = (11, 12, 7))#candidate|4688|(11, 12, 7)|var|int16
bop_4689 = relay.minimum(var_4687.astype('int16'), var_4688.astype('int16')) # shape=(11, 12, 7)
output = bop_4689
output2 = bop_4689
func_4696 = relay.Function([var_4687,var_4688,], output)
mod['func_4696'] = func_4696
mod = relay.transform.InferType()(mod)
mutated_mod['func_4696'] = func_4696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4696_call = mutated_mod.get_global_var('func_4696')
var_4698 = relay.var("var_4698", dtype = "int16", shape = ())#candidate|4698|()|var|int16
var_4699 = relay.var("var_4699", dtype = "int16", shape = (11, 12, 7))#candidate|4699|(11, 12, 7)|var|int16
call_4697 = func_4696_call(var_4698,var_4699,)
output = call_4697
func_4700 = relay.Function([var_4698,var_4699,], output)
mutated_mod['func_4700'] = func_4700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_4735 = relay.TupleGetItem(func_4068_call(), 1)
call_4736 = relay.TupleGetItem(func_4069_call(), 1)
uop_4738 = relay.sinh(call_4735.astype('float64')) # shape=(12, 16, 6)
uop_4740 = relay.sinh(call_4736.astype('float64')) # shape=(12, 16, 6)
output = relay.Tuple([uop_4738,])
output2 = relay.Tuple([uop_4740,])
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
func_3314_call = mod.get_global_var('func_3314')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_4776 = relay.TupleGetItem(func_3314_call(), 0)
call_4777 = relay.TupleGetItem(func_3316_call(), 0)
var_4782 = relay.var("var_4782", dtype = "bool", shape = (16, 5, 15))#candidate|4782|(16, 5, 15)|var|bool
bop_4783 = relay.mod(call_4776.astype('float32'), relay.reshape(var_4782.astype('float32'), relay.shape_of(call_4776))) # shape=(16, 5, 15)
bop_4786 = relay.mod(call_4777.astype('float32'), relay.reshape(var_4782.astype('float32'), relay.shape_of(call_4777))) # shape=(16, 5, 15)
output = bop_4783
output2 = bop_4786
func_4788 = relay.Function([var_4782,], output)
mod['func_4788'] = func_4788
mod = relay.transform.InferType()(mod)
var_4789 = relay.var("var_4789", dtype = "bool", shape = (16, 5, 15))#candidate|4789|(16, 5, 15)|var|bool
output = func_4788(var_4789)
func_4790 = relay.Function([var_4789], output)
mutated_mod['func_4790'] = func_4790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4634_call = mod.get_global_var('func_4634')
func_4636_call = mutated_mod.get_global_var('func_4636')
call_4800 = relay.TupleGetItem(func_4634_call(), 0)
call_4801 = relay.TupleGetItem(func_4636_call(), 0)
func_2152_call = mod.get_global_var('func_2152')
func_2155_call = mutated_mod.get_global_var('func_2155')
const_4806 = relay.const([[3,9,-8,-7,-6,-3,6,-9,2,-1,-1,6,5,4,-3,1,6,-9,3,-9,-5,-4,-6,3,6,-6,1,5,-9,3,-1,10,-8,-2,-5,10,3,2,-8,7,10,-3,3,-7,4,6,8,-5,-5,7,-7,-3,-2,10,-1,-6,-8,2,-4,8,2,-5,10,-5,6,8,-9,-6,7,3,-10,-10,7,-4,2,-2,5,-3,7,1,-1,1,-1,3,2,5,6,-2,7,7,-7,-6,-6,7,-8,-9,9,-9,6,8,7,-1,9,7,1,-7,-2,-3,1,-2,-10,8,-4,2,8,-9,5,9,5,-10,-1,-5,10,-1,-9,10,7,-1,-6,10,-4,10,-9,3,-6,-8,-10,1,-2,10,7,-1,9,-3,4,8,10,-9,-8,3,-5,-2,6,6,-8,-1,8,9,-3,-4,-6,9,10,-7,8,4,-10,8,-4,8,-1,-6,3,8,-8,5,5,-9,1,5,5,3,-8,5,-7,3,-2,-9,-2,2,-9,3,-2,9,10,3,3,-3,10,2,-3,-5,4,1,-1,8,-10,2,-3,5,4,1,5,10,-3,3,9,-10,-4,-9,-4,2,7,-3,-4,-6,-6,10,10,-9,6,9,-1,-8,-2,9,3,-9,5,3,-2,-10,7,-2,-1,9,6,-3,-9,-2,-8,-6,-2,5,8,-9,-8,-9,-10,-1,-5,-8,-10,-7,-2,1,-2,2,3,3,7,10,-10,10,1,3,-4,6,-4,5,4,5,-3,1,-6,7,-4,-1],[-7,6,-2,5,-2,2,-6,9,2,-5,4,-3,8,-6,-9,9,-7,8,-6,7,-6,3,5,1,7,-6,-1,5,-1,4,-7,-9,-1,-6,-2,4,-2,-1,8,-6,-7,10,-1,9,-6,-3,-9,-7,-7,-7,6,6,-10,-4,-8,-7,-3,7,10,8,-1,8,1,-10,8,9,3,-1,4,-3,-8,-9,5,-6,2,-2,-3,2,-8,4,2,-2,-1,-7,-10,7,-9,8,-2,3,-6,-6,-7,-5,-3,-5,-2,-1,9,8,-8,-7,1,3,10,7,2,7,4,-6,-2,-5,7,-7,-5,8,-10,-10,-10,4,2,-8,-7,-4,8,9,3,2,1,8,6,9,3,-5,-4,-5,-10,-1,-7,-9,6,-4,-3,9,-8,10,-7,8,-8,-6,-3,9,5,2,4,6,-1,-9,7,-10,6,-8,9,-4,-10,9,1,-9,-9,-8,-2,5,7,8,1,-10,8,-2,6,3,-6,1,2,6,1,-4,-8,-6,2,-10,4,2,8,8,-1,1,-3,9,-2,-7,-6,-4,2,1,6,9,-1,-3,-6,-4,1,-6,-10,2,-9,3,-3,-2,-10,9,6,7,10,10,-10,4,-2,8,7,-3,10,-10,6,-8,-6,-2,6,2,7,1,-6,9,-7,-1,-8,9,-2,-10,2,7,-6,2,8,7,8,3,5,6,-10,4,-1,7,-3,-6,-7,-5,-9,5,5,-3,2,-8,1,-6,-9,10,-5,-7,-5,3,3,-5,7,2,-1,-4,2,-9],[6,-5,-8,-6,3,1,-6,10,-2,-4,6,-8,10,2,-4,6,-6,4,7,9,5,7,-2,-3,-3,-1,10,6,3,-1,-8,-6,7,10,-2,-3,7,-10,-9,3,-7,-9,-6,-8,-2,6,7,4,-2,9,3,2,-4,-1,5,-4,-10,1,9,-7,-10,1,-4,3,-1,-1,2,6,-6,-8,-1,-3,-5,-9,6,5,8,5,-1,8,-9,-6,-2,9,-9,7,7,-3,6,7,9,-8,-8,-8,1,10,-5,-1,9,5,6,10,-3,8,-6,-9,-8,9,-2,-2,-3,1,1,6,-3,-9,-4,6,1,-7,10,-1,5,-4,-9,9,1,1,-5,1,2,1,-7,5,1,-7,10,-9,8,-3,10,-8,-4,-2,-7,-9,2,-5,4,-1,2,8,-3,-6,-2,5,-2,4,1,-5,8,-5,5,-3,10,6,9,-3,-2,-1,-7,-6,-9,-5,6,-9,7,9,6,10,4,-7,9,5,-8,-6,7,3,4,-8,-9,7,3,-7,9,-4,-3,-8,-10,4,3,2,-3,6,5,8,-3,2,-2,-6,6,6,2,2,8,1,-7,1,-9,5,-3,2,9,-3,-4,-4,8,10,3,-1,9,2,6,-7,-10,-1,-7,-10,-8,7,-9,-10,8,-6,-3,2,10,1,-7,1,1,2,-6,2,5,-5,10,-1,7,-1,-6,-6,1,2,-6,-7,8,4,-2,-7,-8,1,-8,-10,10,9,6,-2,-3,-5,9,3,-1,-1,-5,-10,-3,-1],[-3,-7,-2,-1,-2,-7,9,-1,4,-8,-2,10,9,10,-10,4,4,10,-8,8,6,-4,-7,-5,-8,10,4,-7,9,-7,-10,4,-2,10,5,-1,-3,-6,-7,-3,-6,7,2,-4,-3,10,2,5,-10,6,-3,6,10,-6,5,-6,-4,-2,8,7,-7,-5,3,-2,7,10,-3,-5,8,-1,-3,-5,-1,3,-1,3,7,6,7,5,-6,-3,-9,1,10,-4,3,1,-4,-3,3,4,3,-10,-10,2,7,-2,-4,8,8,-8,-9,5,3,2,-6,-8,8,7,4,-3,-7,-9,-9,6,9,10,-4,5,5,-7,-4,7,-4,2,-6,-9,10,-3,-7,8,-2,7,-3,5,-10,8,7,7,-10,7,4,8,-6,-4,-9,-10,-3,8,9,-4,6,-2,7,-4,10,4,9,-9,4,-7,-8,-3,6,-6,5,-6,4,-3,9,10,9,3,-6,3,8,1,9,-6,9,1,-4,4,5,10,7,3,-2,3,1,-5,6,-4,4,-1,1,-7,-1,4,-2,-9,-2,4,1,1,-3,-10,6,5,3,5,10,-1,-4,-6,-9,5,9,7,-7,1,-7,-9,4,-5,10,1,1,-2,6,3,-4,7,10,-3,-2,-6,-5,4,-9,-6,-8,-8,8,-7,-9,-2,-1,-6,2,-7,-6,-5,-8,-10,-9,-5,-3,7,-4,-6,7,3,6,10,-1,-6,9,-7,2,3,6,-10,10,10,4,-6,5,-10,1,1,-6,-10,-10,-6,-6,6]], dtype = "uint64")#candidate|4806|(4, 288)|const|uint64
call_4805 = func_2152_call(relay.reshape(const_4806.astype('uint64'), [12, 16, 6]), relay.reshape(const_4806.astype('uint64'), [12, 16, 6]), )
call_4807 = func_2152_call(relay.reshape(const_4806.astype('uint64'), [12, 16, 6]), relay.reshape(const_4806.astype('uint64'), [12, 16, 6]), )
func_3950_call = mod.get_global_var('func_3950')
func_3954_call = mutated_mod.get_global_var('func_3954')
var_4813 = relay.var("var_4813", dtype = "float64", shape = (90,))#candidate|4813|(90,)|var|float64
call_4812 = relay.TupleGetItem(func_3950_call(relay.reshape(var_4813.astype('float64'), [15, 6]), relay.reshape(const_4806.astype('uint64'), [1152,]), ), 4)
call_4814 = relay.TupleGetItem(func_3954_call(relay.reshape(var_4813.astype('float64'), [15, 6]), relay.reshape(const_4806.astype('uint64'), [1152,]), ), 4)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_4815 = func_3536_call()
call_4816 = func_3536_call()
output = relay.Tuple([call_4800,call_4805,const_4806,call_4812,var_4813,call_4815,])
output2 = relay.Tuple([call_4801,call_4807,const_4806,call_4814,var_4813,call_4816,])
func_4817 = relay.Function([var_4813,], output)
mod['func_4817'] = func_4817
mod = relay.transform.InferType()(mod)
var_4818 = relay.var("var_4818", dtype = "float64", shape = (90,))#candidate|4818|(90,)|var|float64
output = func_4817(var_4818)
func_4819 = relay.Function([var_4818], output)
mutated_mod['func_4819'] = func_4819
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4846 = relay.var("var_4846", dtype = "bool", shape = ())#candidate|4846|()|var|bool
var_4847 = relay.var("var_4847", dtype = "bool", shape = (6, 1, 7))#candidate|4847|(6, 1, 7)|var|bool
bop_4848 = relay.logical_or(var_4846.astype('bool'), var_4847.astype('bool')) # shape=(6, 1, 7)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
var_4852 = relay.var("var_4852", dtype = "float32", shape = (120, 4))#candidate|4852|(120, 4)|var|float32
call_4851 = relay.TupleGetItem(func_4139_call(relay.reshape(var_4852.astype('float32'), [8, 15, 4])), 0)
call_4853 = relay.TupleGetItem(func_4141_call(relay.reshape(var_4852.astype('float32'), [8, 15, 4])), 0)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_4857 = func_3859_call()
call_4858 = func_3859_call()
bop_4868 = relay.divide(var_4846.astype('float64'), var_4852.astype('float64')) # shape=(120, 4)
var_4874 = relay.var("var_4874", dtype = "bool", shape = (6, 1, 7))#candidate|4874|(6, 1, 7)|var|bool
bop_4875 = relay.less(bop_4848.astype('bool'), relay.reshape(var_4874.astype('bool'), relay.shape_of(bop_4848))) # shape=(6, 1, 7)
var_4885 = relay.var("var_4885", dtype = "float32", shape = (8, 15, 4))#candidate|4885|(8, 15, 4)|var|float32
bop_4886 = relay.power(call_4851.astype('float32'), relay.reshape(var_4885.astype('float32'), relay.shape_of(call_4851))) # shape=(8, 15, 4)
bop_4889 = relay.power(call_4853.astype('float32'), relay.reshape(var_4885.astype('float32'), relay.shape_of(call_4853))) # shape=(8, 15, 4)
output = relay.Tuple([call_4857,bop_4868,bop_4875,bop_4886,])
output2 = relay.Tuple([call_4858,bop_4868,bop_4875,bop_4889,])
func_4895 = relay.Function([var_4846,var_4847,var_4852,var_4874,var_4885,], output)
mod['func_4895'] = func_4895
mod = relay.transform.InferType()(mod)
mutated_mod['func_4895'] = func_4895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4895_call = mutated_mod.get_global_var('func_4895')
var_4897 = relay.var("var_4897", dtype = "bool", shape = ())#candidate|4897|()|var|bool
var_4898 = relay.var("var_4898", dtype = "bool", shape = (6, 1, 7))#candidate|4898|(6, 1, 7)|var|bool
var_4899 = relay.var("var_4899", dtype = "float32", shape = (120, 4))#candidate|4899|(120, 4)|var|float32
var_4900 = relay.var("var_4900", dtype = "bool", shape = (6, 1, 7))#candidate|4900|(6, 1, 7)|var|bool
var_4901 = relay.var("var_4901", dtype = "float32", shape = (8, 15, 4))#candidate|4901|(8, 15, 4)|var|float32
call_4896 = func_4895_call(var_4897,var_4898,var_4899,var_4900,var_4901,)
output = call_4896
func_4902 = relay.Function([var_4897,var_4898,var_4899,var_4900,var_4901,], output)
mutated_mod['func_4902'] = func_4902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_4960 = relay.TupleGetItem(func_3274_call(), 0)
call_4961 = relay.TupleGetItem(func_3275_call(), 0)
output = call_4960
output2 = call_4961
func_4962 = relay.Function([], output)
mod['func_4962'] = func_4962
mod = relay.transform.InferType()(mod)
output = func_4962()
func_4963 = relay.Function([], output)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4163_call = mutated_mod.get_global_var('func_4163')
call_4971 = relay.TupleGetItem(func_4162_call(), 0)
call_4972 = relay.TupleGetItem(func_4163_call(), 0)
func_2152_call = mod.get_global_var('func_2152')
func_2155_call = mutated_mod.get_global_var('func_2155')
const_4981 = relay.const([5,-5,6,-2,2,9,-3,2,-9,1,9,5,4,9,-10,-5,10,2,9,2,-4,-9,-7,5,7,4,-10,3,-2,-9,7,-7,-6,-2,5,-6,-5,5,7,8,4,1,-2,7,9,6,9,-2,4,-10,5,7,-3,2,10,6,-1,-9,1,6,-3,-7,-8,7,-10,3,5,5,-2,-9,-6,-8,4,-9,5,-7,8,1,1,-1,7,6,4,1,8,-8,-9,-1,-6,-7,6,9,8,-1,10,-9,6,10,-9,-7,4,-1,-2,5,-3,-8,8,2,-7,-6,4,5,-3,1,-7,8,2,6,2,-3,-6,3,-10,10,7,-4,3,1,4,7,8,7,-3,-5,4,9,1,-4,6,-8,-9,-1,2,8,4,1,1,2,-9,-10,-7,3,-2,8,-10,-10,-9,-3,5,-10,9,10,9,3,-1,3,1,-7,-2,10,9,10,2,-10,-7,5,2,-3,7,1,8,-7,9,-9,-7,2,8,6,9,7,6,9,7,-9,9,-4,3,3,5,4,10,10,9,-10,-1,4,10,7,7,-4,5,1,-1,-1,-6,-10,10,6,5,-10,2,-8,-7,-2,1,1,5,-6,-4,-5,-2,9,-5,3,-1,-8,7,5,-1,10,-2,7,-1,-6,-10,7,5,3,-9,10,9,2,6,-4,6,-8,-5,8,8,2,6,-7,5,9,-6,5,8,3,-7,-10,1,3,-1,-1,-6,6,-2,3,4,-3,-10,6,-6,-4,8,-5,-10,-4,-1,9,-9,1,9,-9,5,-1,-10,5,-10,8,10,6,6,-2,-6,-6,7,6,-9,-9,9,-1,9,-5,-4,-6,8,6,-3,-1,-9,-7,4,2,-10,-10,-3,8,-5,-2,7,5,1,1,8,-6,-1,-3,6,-8,6,-5,-7,10,7,-2,1,2,-7,-7,-7,1,-6,10,-10,8,8,-5,-8,8,-1,2,8,-4,-8,-3,2,10,-8,9,1,-6,-3,-6,9,8,4,10,5,10,-4,6,-7,-5,-9,5,-2,-10,3,5,10,2,3,-10,7,-2,5,7,8,-6,-6,8,-3,10,6,8,9,4,1,2,5,8,-4,1,7,-9,-10,1,-9,9,-6,-3,-6,-7,-10,6,-3,-3,-9,8,-2,1,6,-5,-2,-10,1,3,10,-6,-7,4,-7,8,9,-4,-5,-3,8,7,2,10,1,-3,-1,9,-9,9,-10,-4,3,2,-4,10,-4,-5,4,-2,-9,6,-3,-2,-8,10,8,-6,1,-10,4,-10,6,-5,-1,5,-3,1,-8,8,-4,3,-10,4,9,-8,-3,-1,4,-1,-6,-6,-9,-3,-2,4,-7,9,-8,-1,-8,-1,-9,-1,-10,-7,-1,3,2,9,-7,1,10,3,4,6,-3,4,-9,5,9,6,-7,-10,-7,2,-3,-9,-4,2,6,-1,-7,3,9,-7,-1,8,4,-6,10,8,-4,6,-1,7,8,-10,-4,1,2,2,1,-3,10,9,-9,3,5,-3,-10,6,10,-5,1,-8,5,6,1,-2,-9,3,1,-5,-7,-5,-9,-7,6,-3,-9,10,2,10,7,6,-7,8,-7,4,-9,1,9,9,3,4,3,-5,-4,-10,-9,9,-7,3,7,-8,-6,6,-8,-3,-7,2,-3,-6,-2,-5,3,8,-10,4,8,-6,2,10,-9,2,9,7,-10,8,7,4,9,10,3,-9,-5,-5,-8,-6,9,-2,-1,-2,-10,-5,-6,-7,-1,4,-10,-2,7,1,-4,10,-6,-2,1,-7,6,10,-1,5,-5,-3,-2,-1,2,-4,-10,10,9,2,-7,5,-1,3,3,3,9,-4,-10,-3,6,1,-4,-1,-2,-4,-3,4,5,7,7,9,-3,10,7,-8,-1,-10,-7,-7,-5,-1,4,-4,3,9,1,-8,3,10,9,3,-6,-2,-4,-3,4,9,9,6,-7,2,5,6,7,-5,3,-6,-1,-3,9,-5,-2,-8,-10,-5,-9,8,-6,-9,-10,9,4,-4,4,-1,-3,-6,1,-8,-8,1,-9,-3,-1,7,-9,-7,-2,8,-8,8,5,8,10,10,-8,-7,-8,-3,-3,10,-9,-4,8,8,1,7,2,4,3,9,-5,-10,7,1,4,-3,-10,5,-7,2,-8,5,-6,1,-3,1,-7,10,-4,7,4,-2,-4,-10,9,10,3,-7,-6,-8,-9,8,2,3,1,-4,7,-9,3,2,5,9,-1,9,-5,8,-8,1,6,-5,-1,4,-7,8,6,3,-6,-9,1,4,-7,-1,9,-6,-5,4,4,-5,-10,-10,-7,-8,-5,9,7,1,6,-10,3,1,-10,5,2,-2,7,1,-7,6,-9,8,-10,1,-3,4,8,-6,-2,-2,-3,1,8,-3,-2,-9,-5,7,7,3,9,-6,5,-5,4,-1,2,8,-3,-7,1,-6,-4,-4,-8,-1,-6,-4,-10,8,-6,1,-1,10,-10,-1,-4,9,-9,-6,-2,6,5,-9,-10,-7,5,6,6,2,-4,7,7,5,9,-4,10,2,-1,10,-7,-10,6,-10,6,6,-2,-10,-9,8,-6,-2,2,2,5,5,-1,-6,-2,9,8,-8,10,-3,2,-8,4,3,-2,-9,8,-10,-10,-8,-3,-10,2,-3,-7,1,8,8,-9,-7,-5,-9,10,-4,4,-5,-8,-9,-7,5,9,-3,-7,-10,-1,7,-1,1,-6,4,-8,6,-5,10,-7,6,-3,4,10,-6,9,9,2,5,-8,7,-7,-1,9,-4,8,-2,-7,-3,-2,-9,6,5,9,-5,9,2,6,10,-7,-2,2,-8,-4,-9,-9,7,8,3,-2,-6,-2,-8,-4,-6,5,-5,-1,8,-3,-2,-7,10,-3,-5,-3,5,-9,-6,3,3,-7,5,-3,-5,-1,-1,-8,-8,-1,-3,5,-2,2,7,-7,3,3,5,-2,2,-9,-6,3,-5,6,-1,-7,5,-10,-7,7,2,-8,5,9,-5,-2,5,-4,2,-2,1,5,-9,8,-3,-5,-4,3,-5,9,-3,3,-8,2,-5,4,-4,-1,5,10,-6,-4,10,-2,-2,-6,-5,4,-6], dtype = "uint64")#candidate|4981|(1152,)|const|uint64
call_4980 = func_2152_call(relay.reshape(const_4981.astype('uint64'), [12, 16, 6]), relay.reshape(const_4981.astype('uint64'), [12, 16, 6]), )
call_4982 = func_2152_call(relay.reshape(const_4981.astype('uint64'), [12, 16, 6]), relay.reshape(const_4981.astype('uint64'), [12, 16, 6]), )
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_5002 = relay.TupleGetItem(func_4068_call(), 0)
call_5003 = relay.TupleGetItem(func_4069_call(), 0)
output = relay.Tuple([call_4971,call_4980,const_4981,call_5002,])
output2 = relay.Tuple([call_4972,call_4982,const_4981,call_5003,])
func_5012 = relay.Function([], output)
mod['func_5012'] = func_5012
mod = relay.transform.InferType()(mod)
output = func_5012()
func_5013 = relay.Function([], output)
mutated_mod['func_5013'] = func_5013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4962_call = mod.get_global_var('func_4962')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_5040 = func_4962_call()
call_5041 = func_4962_call()
output = relay.Tuple([call_5040,])
output2 = relay.Tuple([call_5041,])
func_5042 = relay.Function([], output)
mod['func_5042'] = func_5042
mod = relay.transform.InferType()(mod)
mutated_mod['func_5042'] = func_5042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5042_call = mutated_mod.get_global_var('func_5042')
call_5043 = func_5042_call()
output = call_5043
func_5044 = relay.Function([], output)
mutated_mod['func_5044'] = func_5044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3314_call = mod.get_global_var('func_3314')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_5072 = relay.TupleGetItem(func_3314_call(), 1)
call_5073 = relay.TupleGetItem(func_3316_call(), 1)
uop_5079 = relay.acosh(call_5072.astype('float32')) # shape=(12, 3, 14)
uop_5081 = relay.acosh(call_5073.astype('float32')) # shape=(12, 3, 14)
output = uop_5079
output2 = uop_5081
func_5082 = relay.Function([], output)
mod['func_5082'] = func_5082
mod = relay.transform.InferType()(mod)
mutated_mod['func_5082'] = func_5082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5082_call = mutated_mod.get_global_var('func_5082')
call_5083 = func_5082_call()
output = call_5083
func_5084 = relay.Function([], output)
mutated_mod['func_5084'] = func_5084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_5111 = func_3896_call()
call_5112 = func_3896_call()
var_5122 = relay.var("var_5122", dtype = "bool", shape = (8, 15, 4))#candidate|5122|(8, 15, 4)|var|bool
bop_5123 = relay.not_equal(call_5111.astype('bool'), relay.reshape(var_5122.astype('bool'), relay.shape_of(call_5111))) # shape=(8, 15, 4)
bop_5126 = relay.not_equal(call_5112.astype('bool'), relay.reshape(var_5122.astype('bool'), relay.shape_of(call_5112))) # shape=(8, 15, 4)
output = bop_5123
output2 = bop_5126
func_5128 = relay.Function([var_5122,], output)
mod['func_5128'] = func_5128
mod = relay.transform.InferType()(mod)
mutated_mod['func_5128'] = func_5128
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5129 = relay.var("var_5129", dtype = "bool", shape = (8, 15, 4))#candidate|5129|(8, 15, 4)|var|bool
func_5128_call = mutated_mod.get_global_var('func_5128')
call_5130 = func_5128_call(var_5129)
output = call_5130
func_5131 = relay.Function([var_5129], output)
mutated_mod['func_5131'] = func_5131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4634_call = mod.get_global_var('func_4634')
func_4636_call = mutated_mod.get_global_var('func_4636')
call_5147 = relay.TupleGetItem(func_4634_call(), 0)
call_5148 = relay.TupleGetItem(func_4636_call(), 0)
output = relay.Tuple([call_5147,])
output2 = relay.Tuple([call_5148,])
func_5151 = relay.Function([], output)
mod['func_5151'] = func_5151
mod = relay.transform.InferType()(mod)
output = func_5151()
func_5152 = relay.Function([], output)
mutated_mod['func_5152'] = func_5152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_5217 = relay.TupleGetItem(func_4068_call(), 2)
call_5218 = relay.TupleGetItem(func_4069_call(), 2)
func_3950_call = mod.get_global_var('func_3950')
func_3954_call = mutated_mod.get_global_var('func_3954')
const_5220 = relay.const([-6.203247,9.421766,6.207238,1.689048,5.690276,3.414865,7.097560,7.094242,-3.518924,0.392671,0.085579,-7.275869,-8.429623,5.975096,5.003742,6.303680,7.898102,-9.343923,1.492133,-5.694486,5.268542,1.596916,2.911849,-7.709338,-6.364831,2.347991,3.826642,4.820674,2.119680,3.215340,5.113345,3.339211,9.141401,-6.938548,7.036716,3.266624,-8.251133,-8.429211,-3.739909,2.516110,-2.554492,-7.703424,-0.754932,2.242900,-7.175687,-7.025586,-0.100845,-8.781528,8.652156,-5.304207,0.464485,1.818004,-9.233862,8.975699,-3.432491,3.687102,5.167244,2.519658,5.814826,-1.260389,2.227925,-8.973627,-0.461150,-4.536227,6.206561,-5.959419,-5.380409,-3.979434,4.049299,9.045905,5.663453,-7.194818,5.490393,-9.301192,2.634741,-7.611871,-8.239309,-2.605727,-8.972606,-3.670806,7.732264,-2.929128,4.836485,-1.867699,2.900446,-9.267133,1.293157,9.266655,-3.265054,5.710522], dtype = "float64")#candidate|5220|(90,)|const|float64
call_5219 = relay.TupleGetItem(func_3950_call(relay.reshape(const_5220.astype('float64'), [15, 6]), relay.reshape(call_5217.astype('uint64'), [1152,]), ), 4)
call_5221 = relay.TupleGetItem(func_3954_call(relay.reshape(const_5220.astype('float64'), [15, 6]), relay.reshape(call_5217.astype('uint64'), [1152,]), ), 4)
func_4417_call = mod.get_global_var('func_4417')
func_4418_call = mutated_mod.get_global_var('func_4418')
call_5225 = relay.TupleGetItem(func_4417_call(), 0)
call_5226 = relay.TupleGetItem(func_4418_call(), 0)
func_3391_call = mod.get_global_var('func_3391')
func_3395_call = mutated_mod.get_global_var('func_3395')
var_5272 = relay.var("var_5272", dtype = "float64", shape = (1512,))#candidate|5272|(1512,)|var|float64
const_5273 = relay.const([[False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False],[True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False],[True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,False],[True,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True],[True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True],[False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False],[False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False],[False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False]], dtype = "bool")#candidate|5273|(8, 42)|const|bool
const_5274 = relay.const([True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False], dtype = "bool")#candidate|5274|(672,)|const|bool
call_5271 = relay.TupleGetItem(func_3391_call(relay.reshape(var_5272.astype('float64'), [14, 9, 12]), relay.reshape(const_5273.astype('bool'), [336,]), relay.reshape(const_5274.astype('bool'), [672,]), ), 6)
call_5275 = relay.TupleGetItem(func_3395_call(relay.reshape(var_5272.astype('float64'), [14, 9, 12]), relay.reshape(const_5273.astype('bool'), [336,]), relay.reshape(const_5274.astype('bool'), [672,]), ), 6)
output = relay.Tuple([call_5217,call_5219,const_5220,call_5225,call_5271,var_5272,const_5273,const_5274,])
output2 = relay.Tuple([call_5218,call_5221,const_5220,call_5226,call_5275,var_5272,const_5273,const_5274,])
func_5289 = relay.Function([var_5272,], output)
mod['func_5289'] = func_5289
mod = relay.transform.InferType()(mod)
var_5290 = relay.var("var_5290", dtype = "float64", shape = (1512,))#candidate|5290|(1512,)|var|float64
output = func_5289(var_5290)
func_5291 = relay.Function([var_5290], output)
mutated_mod['func_5291'] = func_5291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_5313 = func_3759_call()
call_5314 = func_3759_call()
output = call_5313
output2 = call_5314
func_5315 = relay.Function([], output)
mod['func_5315'] = func_5315
mod = relay.transform.InferType()(mod)
output = func_5315()
func_5316 = relay.Function([], output)
mutated_mod['func_5316'] = func_5316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5315_call = mod.get_global_var('func_5315')
func_5316_call = mutated_mod.get_global_var('func_5316')
call_5353 = func_5315_call()
call_5354 = func_5315_call()
func_5082_call = mod.get_global_var('func_5082')
func_5084_call = mutated_mod.get_global_var('func_5084')
call_5355 = func_5082_call()
call_5356 = func_5082_call()
func_3727_call = mod.get_global_var('func_3727')
func_3735_call = mutated_mod.get_global_var('func_3735')
const_5365 = relay.const([3.664609,-1.237368,8.956582,8.348629,-4.598704,-5.029836,3.610608,-7.947294,3.029912,5.796958,9.482270,4.304263,7.327639,8.585336,3.488070,1.406311,-3.416963,5.801068,-5.842738,-5.808583,9.442806,-4.744214,7.939663,-6.716371,-4.123664,3.955657,3.836285,3.565030,-6.677722,9.235516,-0.497787,-3.613658,-1.593210,-0.392074,0.143917,8.982724,9.719868,8.132794,9.040310,5.373973,1.024551,5.760597,-4.095682,-0.253031,4.878411,-8.116256,-1.432560,-6.678259,-9.182007,7.455834,3.393657,9.430004,-1.087958,-3.553298,-9.803845,-3.387162,-9.868090,-4.405650,-4.567700,-5.455550,-5.933969,2.943620,6.282140,2.967329,-6.806742,3.809637,-7.107769,8.196163,-6.825548,-2.249395,7.797689,-5.149064,-3.154820,-5.421711,1.588323,-8.825743,-2.657269,-3.127867,7.401133,4.746324,-0.410975,-3.660810,5.849641,-0.105073,6.338317,-9.971621,8.493349,-9.955392,3.224516,-0.070212], dtype = "float64")#candidate|5365|(90,)|const|float64
const_5366 = relay.const([[-7.797699],[9.037469],[6.470159],[-7.428767],[-9.838643],[5.475271],[2.344870],[1.828737],[-5.500257],[2.024068],[-8.673570],[7.834659],[9.774882],[7.153182],[-3.592724],[1.453742],[2.434275],[7.897382],[-9.304728],[-4.146542],[7.237488],[6.347983],[-8.733712],[1.900054],[4.692371],[-1.779808],[5.446108],[-1.251265],[-7.983483],[9.635920],[2.402865],[9.059320],[1.547272],[-8.063574],[0.521562],[-7.022786],[-0.290551],[0.047929],[-8.297123],[8.596680],[4.926873],[0.482548],[-3.678078],[-9.497878],[0.767879],[6.088791],[-3.452902],[8.616960],[4.813247],[6.582934],[0.204594],[-3.038201],[-2.478675],[-4.891825],[-1.309115],[-4.348260],[2.459713],[-7.602080],[-3.062046],[2.217151],[-8.201418],[-2.730797],[8.398969],[-2.876947],[5.572260],[6.399277],[0.488117],[7.378296],[-2.146578],[-9.804608],[1.730629],[-6.620340],[-3.995550],[-6.375702],[1.779405],[-3.657234],[3.061811],[-6.671233],[6.701680],[8.620642],[5.536920],[9.710117],[-9.245720],[-9.948786],[-6.311935],[5.097775],[8.605269],[5.192726],[1.779091],[-3.152152],[0.974514],[-4.145280],[-0.271529],[7.921510],[-1.663851],[-8.186709],[-1.472269],[-0.817056],[-2.163864],[4.479147],[-8.624464],[8.724625],[-4.897410],[0.186302],[-8.283003],[9.110744],[1.962792],[-3.256030],[-7.353569],[9.563742],[7.153132],[-6.172111],[0.486321],[-0.738932],[7.641319],[-8.619410],[4.747290],[-1.047809],[-5.132804],[8.906011],[6.397888],[-7.825107],[-8.977722],[-3.834905],[0.477276],[8.987184],[-3.945569],[-3.703234],[5.516487],[3.002507],[-1.516260],[-1.347409],[8.336658],[5.535157],[-2.071236],[9.904954],[3.377981],[-7.377629],[-7.940399],[4.446350],[-6.873953],[-8.769192],[-7.200979],[-3.955739],[-3.991727],[1.424096],[-7.319622],[-1.434353],[-7.282953],[1.550414],[-1.057244],[-6.290588],[8.399471],[0.627234],[-1.094417],[4.365823],[-1.813036],[5.586729],[-4.606012],[-3.362532],[8.961485],[3.870785],[1.853419],[-4.754461],[3.041530],[-2.952520],[-6.793848],[-0.971304],[-5.623287],[8.495554],[-6.143471],[9.178384],[8.561103],[1.822283],[5.955465],[-4.204636],[4.180587],[-1.271632],[8.050317],[-8.937441],[-0.557542],[-5.490663],[-8.471115],[-1.626388],[-2.462193],[9.665008],[-9.090046],[4.505246],[7.476768],[6.630759],[-0.402176],[1.578626],[4.881411],[-1.134823],[-9.182424],[-2.443656],[-9.892255],[8.139195],[8.206389],[7.468398],[-9.935520],[-8.517620],[2.432895],[-2.531930],[-1.024278],[4.767038],[6.993205],[6.404310],[-9.713267],[5.823412],[-3.607769],[-4.324306],[-1.095700],[6.277902],[3.555913],[9.549525],[1.394019],[7.806739],[-5.081214],[0.545903],[8.490213],[9.225088],[-3.150981],[-8.383127],[8.316981],[3.115219],[0.566910],[-9.078017],[-7.153560],[7.656719],[-6.040901],[2.158511],[-3.051294],[-9.066525],[-4.694386],[2.665636],[6.305802],[-8.620074],[4.720189],[-8.142337],[-6.263024],[9.615418],[7.880822],[0.782786],[3.315673],[-4.008380],[3.810168],[-9.939996],[-1.821509],[-5.115623],[-8.606733],[-6.184168],[7.383077],[5.923822],[4.487055],[5.079944],[-9.950729],[6.634946],[-3.893624],[2.330148],[0.071206],[1.997620],[6.606700],[-1.653847],[-1.727618],[-2.016513],[0.881271],[-6.371140],[4.903773],[9.885753],[-9.503045],[-3.344146],[7.415348],[-1.382533],[-0.242504],[-3.682552],[4.012421],[-1.652583],[4.215850],[-5.497650],[-7.483174],[-2.253390],[-4.880706],[-3.338949],[6.852914],[-6.282638],[-3.105686],[-2.714213],[3.051741],[3.521928],[-2.375209],[1.527694],[1.445855],[-3.453312],[6.182994],[-7.192443],[4.702714],[8.332135],[-6.250620],[8.143132],[3.463506],[3.805202],[-1.805337],[-9.593136],[-9.305328],[2.314349],[4.896105],[1.237609],[-1.532441],[4.138260],[-9.479818],[0.079068],[-4.503005],[6.646779],[-0.667604],[-3.681034],[7.493054],[6.818922],[4.366994],[2.299697],[6.003126],[-1.455893],[3.353417],[7.577635],[2.759401],[3.458629],[4.516684],[4.715973],[0.320931],[-7.189005],[3.463875],[-1.749928],[-4.885268],[-4.429138],[4.863664],[2.822529],[-9.088046],[9.594284],[2.385682],[-2.021745],[9.586887],[9.798415],[-6.597322],[-1.662891],[3.774780],[-4.418039],[-2.826277],[1.550831],[-3.562066],[-9.906992],[4.872836],[8.570197],[-0.979581],[-8.155467],[5.867595],[-8.006110],[-1.697431],[8.259234],[0.546423],[6.528491],[-4.695422],[5.935918],[-8.030834],[9.486918],[4.384715],[-7.702109],[-1.813124],[-0.947657],[-4.306834],[-6.308912],[4.557409],[-0.658161],[-3.842381],[4.686574],[2.304409],[4.881388],[-8.818776],[-9.631762],[3.657643],[4.142440],[-9.369072],[-5.419049],[5.325360],[0.381547],[0.010192],[-7.586516],[-9.870428],[-7.928161],[-6.548641],[-7.796354],[-2.107467],[-0.528014],[3.753507],[0.263189],[-4.956447],[7.032337],[-7.188611],[0.254979],[-9.998920],[4.471090],[1.334677],[5.182622],[-1.984195],[-2.949325],[5.697788],[4.177748],[-3.929368],[-3.982728],[-2.452243],[3.250774],[-6.410177],[9.352428],[-1.199839],[7.705077],[0.028814],[-7.196470],[-8.881331],[4.916149],[6.703509],[6.187130],[-4.626348],[9.472589],[-0.888018],[-3.099685],[0.203483],[-6.674076],[-8.611860],[3.867245],[-1.529220],[-4.739875],[5.234925],[-5.744055],[-7.263370],[4.667662],[-9.227431],[-7.365265],[9.853401],[2.750785],[4.871794],[-9.608244],[3.803462],[-7.368597],[1.132654],[-8.306184],[-0.035044],[1.917503],[8.258748],[2.549970],[1.373006],[-9.218655],[-3.317009],[6.727569],[-3.162084],[7.760330],[-6.121845],[-5.563228],[-9.025725],[-2.869960],[-9.740193],[-4.305282],[9.295118],[8.930418],[1.529513],[-8.148721],[3.394786],[-5.599135],[9.301725],[1.595939],[6.896446],[0.012486],[-0.699229],[6.067826],[-3.352601],[-5.470652],[1.161070],[-7.501165],[7.582210],[5.924871],[-3.565820],[3.520151],[-6.801299],[5.056792],[4.701304],[7.301269],[-9.296442],[2.654014],[4.376316],[2.952527],[-0.466031],[-2.802446],[-2.389756],[-5.516260],[-2.941752],[2.000976],[7.947428],[-8.832619],[-1.473146],[9.261099],[-2.546899],[-1.116468],[9.078707],[-2.101819],[5.892758],[-6.733788],[5.056465],[9.425647],[3.308626],[0.369652],[7.702784],[5.618258],[-3.547768],[1.071894],[6.568452],[-2.100379],[2.133333],[-2.409762],[-6.468345],[9.382039],[6.506181],[0.559793],[2.815140],[-7.973732],[-3.097890],[-2.171702],[-8.381617],[-9.469657],[-6.072436],[-0.826624],[-9.996958],[2.866253],[0.824845],[-3.586626],[-6.974098],[1.215025],[-3.332356],[4.294196],[8.905285],[-6.580295],[7.144156],[-8.999824],[-6.567519],[-8.279790],[-1.780475],[7.583410],[-6.282885],[-8.921019],[-8.163931],[5.951654],[2.111796],[-8.777842],[-9.067330],[4.648206],[-6.996747],[3.537291],[-9.011905],[2.559691],[8.808972],[8.776557],[-1.126085],[-1.527706],[-8.017478],[6.153296],[-0.298736],[2.406743],[0.631428],[5.730158],[3.717896],[-3.796463],[-1.715710],[-4.248760],[5.586371],[-7.449744],[0.650660],[-2.538346],[-8.184100],[-2.890477],[8.342898],[2.225927],[9.393312],[9.434612],[8.537711],[-3.581811],[6.030703],[-9.015130],[-4.908592],[5.161957],[-3.274559],[-1.778119],[4.196305],[-2.461632],[-7.190645],[-8.582712],[-3.765176],[1.140817],[6.362033],[-7.595248],[0.028749],[6.204478],[4.724503],[-9.684010],[-3.624341],[9.261654],[3.018612],[3.116055],[-4.366261],[-3.256730],[-6.922324],[0.034468],[2.291834],[-5.943889],[7.418033],[4.433843],[1.358379],[-4.167414],[-8.387097],[2.687162],[-6.706350],[5.770453],[-8.217212],[-4.519623],[-4.250941],[8.408937],[-6.808965],[7.027257],[4.937553],[-4.324289],[6.324092],[8.676106],[-6.568820],[8.946753],[8.845211],[-7.176541],[-9.393453],[9.487904],[-3.368682],[1.453135],[6.679828],[7.675370],[6.048118],[4.888737],[5.581669],[-4.715193],[2.925725],[5.731597],[4.857511],[-7.007179],[9.601341],[-3.335922],[-1.192236],[2.180105],[9.973494],[-1.366863],[4.974398],[-2.530297],[-5.045332],[-6.063998],[5.792729],[-7.987465],[-1.453757],[6.266376],[7.948458],[-4.516944],[-2.846370],[-3.894492],[0.501287],[4.621624],[-2.226436],[0.383741],[2.435758],[0.517930],[1.855406],[7.514937],[-5.439670],[2.790504],[-1.847193],[-4.368390],[-3.963317],[-3.603455],[4.622914],[9.695107],[-5.445028],[8.795338],[-3.826497],[8.035210],[0.187746],[-7.392058],[-3.212843],[4.844715],[0.684914],[9.410946],[3.439668],[5.756165],[9.389314],[-1.334425],[-3.869630],[9.998831],[-4.957870],[-6.125683],[7.231842],[2.673837],[-1.810562],[8.657636],[2.387221],[0.371419],[6.294854],[-1.181597],[-4.270435],[-8.652529],[-7.688450],[-2.816045],[-1.283309],[1.286994],[-4.713360],[-4.071900],[7.253908],[-5.889743],[8.169400],[-5.463386],[6.473453],[8.139191],[4.682290],[9.141133],[-9.925426],[2.695822],[8.245824],[9.804919],[4.566011],[-1.893533],[-9.466358],[2.735882],[-7.707845],[3.049550],[2.744899],[6.674612],[1.289965],[6.312154],[-5.268673],[-9.673656],[-0.237573],[6.665250],[2.289238],[0.027463],[-0.636791],[2.956508],[-0.131513],[-5.797300],[-8.465502],[-9.976641],[-0.078997],[-7.953558],[4.303337],[-6.869292],[2.077593],[-9.153280],[-2.947509],[4.765603],[-4.092085],[-7.928463],[-5.642998],[-2.499365],[-9.921997],[-7.919667],[-6.659325],[-9.891622],[-9.220495],[4.983726],[-5.022432],[6.239041],[-9.668328],[5.169418],[-3.962075],[5.714504],[8.451153],[9.468800],[5.236795],[5.129222],[-7.068690],[-9.586462],[-5.842923],[9.530737],[-9.453839],[-6.110367],[-3.687094],[-7.153507],[6.866019],[3.184098],[-6.264286],[3.478511],[-0.807929],[7.042220],[-2.552342],[7.709132],[-3.711408],[8.930504],[-6.514118],[8.690592],[5.835322],[2.151987],[-8.453295],[7.503267],[4.985875],[7.754732],[6.629365],[-5.450205],[2.463372],[0.585327],[-9.187572],[-7.408028],[-3.223363],[5.170127],[8.225860],[4.426977],[5.672032],[-4.647046],[-3.255337],[5.233676],[4.957083],[0.510677],[3.257878],[-2.186897],[-1.831524],[-5.149257],[3.921407],[7.529776],[9.359119],[-4.416720],[-7.346212],[2.445312],[5.699099],[5.004743],[5.455742],[8.444769],[5.462641],[3.149073],[-0.993639],[9.632739],[7.030037],[9.979242],[-3.530775],[6.934305],[-8.463097],[-2.729141],[6.410369],[-4.802412],[-5.808593],[0.204731],[-1.164760],[-9.523694],[1.371603],[0.377095],[3.730130],[-9.263926],[-5.232306],[4.186016],[7.591342],[-5.859436],[9.248767],[-8.471417],[8.007257],[9.780529],[-4.152133],[9.184677],[0.604887],[-7.382285],[-1.529137],[8.969271],[-7.599422],[-0.264782],[0.820587],[7.019930],[-2.356620],[-1.326994],[3.395890],[8.656248],[8.176475],[-8.560909],[4.788827],[0.519063],[4.030877],[8.848054],[0.621996],[6.003889],[3.563045],[-2.912713],[-4.735037],[3.696213],[-4.414549],[-6.788292],[-8.971859],[-7.241783],[-9.866744],[3.749915],[-9.775959],[-4.306780],[-4.442353],[2.693608],[-1.716168],[6.485857],[7.384275],[6.308708],[3.788478],[-9.966021],[-1.565028],[1.749887],[-0.694261],[4.028272],[-2.427730],[-8.257473],[4.535604],[-1.152707],[3.780070],[2.277768],[5.434537],[4.643122],[-8.384476],[-5.039129],[2.270837],[0.545802],[2.139358],[-3.673582],[-3.528209],[-8.313088],[-4.985890],[-7.164968],[0.968029],[2.055659],[-8.969072],[8.103732],[6.436211],[-1.861351],[4.759829],[8.528306],[-2.273561],[-7.604524],[-4.519363],[9.680613],[-4.060986],[6.970945],[6.201424],[-9.318985],[5.165387],[2.348432],[-6.460192],[9.554847],[5.918509],[-9.888413],[-9.331226],[6.809868],[-8.903258],[-6.183329],[-3.072279],[-7.027766],[5.915455],[2.308637],[8.479072],[0.175715],[4.704544],[-1.707608],[1.770193],[4.057058],[-8.283934],[0.901606],[7.566232],[6.537468],[0.564157],[-9.065089],[2.259787],[-5.334974],[5.898121],[7.661197],[-7.812545],[9.935306],[0.949513],[0.468757],[2.071766],[2.334571],[-7.141774],[-9.971193],[6.563611],[-1.138693],[6.217796],[-7.194849],[1.684949],[6.176164],[-6.302578],[9.260270],[4.888648],[-6.518370],[-2.667471],[-4.190839]], dtype = "float64")#candidate|5366|(990, 1)|const|float64
var_5367 = relay.var("var_5367", dtype = "float64", shape = (1512,))#candidate|5367|(1512,)|var|float64
var_5368 = relay.var("var_5368", dtype = "bool", shape = (336,))#candidate|5368|(336,)|var|bool
const_5369 = relay.const([[True,True,True,True],[False,True,False,False],[True,False,False,False],[True,True,False,False],[True,False,False,True],[True,True,False,False],[True,True,True,True],[True,True,False,False],[False,False,False,False],[True,False,False,True],[False,False,True,True],[True,False,False,False],[False,False,True,True],[True,False,True,False],[True,True,True,False],[False,False,True,False],[False,True,False,True],[True,False,False,True],[True,False,True,False],[False,True,True,False],[True,False,False,False],[False,True,True,True],[False,False,False,False],[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,True,False,False],[False,True,True,True],[False,True,False,False],[False,True,False,True],[True,False,True,False],[True,False,False,True],[False,False,False,True],[True,False,True,True],[False,False,False,False],[True,True,False,True],[False,False,False,False],[True,False,True,False],[False,True,False,True],[True,True,False,True],[True,False,True,False],[False,False,False,False],[False,False,True,False],[True,True,True,True],[True,True,True,False],[True,True,False,True],[False,True,False,True],[False,False,False,True],[False,True,False,True],[False,False,True,False],[False,False,False,True],[True,False,False,False],[True,True,False,True],[False,True,False,False],[False,True,True,False],[True,False,True,False],[True,True,True,True],[True,False,False,True],[True,False,False,False],[False,False,True,False],[False,True,True,False],[False,True,True,False],[False,False,False,False],[False,False,False,False],[True,True,True,True],[True,True,False,False],[False,True,True,False],[True,False,False,True],[True,True,False,False],[True,True,False,True],[True,True,True,False],[True,True,False,False],[False,True,True,False],[True,False,False,True],[True,True,True,False],[True,False,False,True],[True,False,True,False],[True,True,False,False],[False,True,False,True],[True,False,False,True],[False,True,True,True],[True,False,False,False],[True,True,True,True],[True,True,False,True],[True,True,True,False],[False,True,False,True],[True,True,False,False],[True,False,True,True],[False,True,False,True],[True,False,False,False],[False,True,True,True],[False,True,False,True],[False,False,True,True],[True,True,False,False],[False,False,False,False],[True,False,True,True],[True,False,False,False],[False,False,False,False],[True,False,False,True],[True,False,False,False],[False,True,True,False],[True,True,False,True],[True,True,True,False],[True,True,True,False],[True,False,False,True],[False,False,False,False],[False,False,True,False],[False,False,False,True],[True,True,True,False],[False,True,False,True],[False,True,False,True],[False,True,True,True],[True,True,True,False],[False,True,False,False],[True,True,False,True],[True,False,False,True],[True,True,True,True],[True,True,True,True],[True,True,True,True],[False,False,True,False],[False,False,False,False],[True,False,False,False],[True,True,True,True],[True,False,False,True],[True,True,False,False],[True,True,False,False],[False,True,True,True],[True,False,True,True],[False,True,True,True],[True,False,True,False],[True,True,True,False],[True,True,True,False],[True,False,True,False],[True,True,False,False],[False,True,True,True],[False,False,True,False],[True,False,False,False],[False,True,False,True],[False,False,False,True],[True,True,False,False],[True,True,False,True],[False,False,True,False],[False,False,True,False],[False,False,False,True],[True,False,True,True],[False,True,True,False],[True,True,False,True],[False,False,True,False],[True,False,True,True],[False,False,True,False],[False,False,False,False],[True,True,True,False],[True,False,True,True],[True,False,False,True],[True,False,False,False],[False,True,False,True],[True,True,False,False],[True,True,False,True],[True,True,True,False],[False,False,False,True],[False,False,True,True],[False,True,False,False],[True,False,False,True],[False,False,False,True],[True,False,True,False],[True,False,True,False],[True,False,True,True],[False,True,False,False]], dtype = "bool")#candidate|5369|(168, 4)|const|bool
var_5370 = relay.var("var_5370", dtype = "uint64", shape = (1152,))#candidate|5370|(1152,)|var|uint64
call_5364 = relay.TupleGetItem(func_3727_call(relay.reshape(const_5365.astype('float64'), [1, 10, 9]), relay.reshape(const_5366.astype('float64'), [11, 10, 9]), relay.reshape(var_5367.astype('float64'), [1512,]), relay.reshape(var_5368.astype('bool'), [4, 84]), relay.reshape(const_5369.astype('bool'), [672,]), relay.reshape(var_5370.astype('uint64'), [1152,]), ), 4)
call_5371 = relay.TupleGetItem(func_3735_call(relay.reshape(const_5365.astype('float64'), [1, 10, 9]), relay.reshape(const_5366.astype('float64'), [11, 10, 9]), relay.reshape(var_5367.astype('float64'), [1512,]), relay.reshape(var_5368.astype('bool'), [4, 84]), relay.reshape(const_5369.astype('bool'), [672,]), relay.reshape(var_5370.astype('uint64'), [1152,]), ), 4)
bop_5372 = relay.logical_or(const_5365.astype('bool'), const_5366.astype('bool')) # shape=(990, 90)
func_1445_call = mod.get_global_var('func_1445')
func_1448_call = mutated_mod.get_global_var('func_1448')
var_5387 = relay.var("var_5387", dtype = "int32", shape = ())#candidate|5387|()|var|int32
call_5386 = func_1445_call(relay.reshape(var_5387.astype('int32'), []), relay.reshape(var_5368.astype('int32'), [14, 12, 2]), )
call_5388 = func_1445_call(relay.reshape(var_5387.astype('int32'), []), relay.reshape(var_5368.astype('int32'), [14, 12, 2]), )
output = relay.Tuple([call_5353,call_5355,call_5364,var_5367,var_5368,const_5369,var_5370,bop_5372,call_5386,var_5387,])
output2 = relay.Tuple([call_5354,call_5356,call_5371,var_5367,var_5368,const_5369,var_5370,bop_5372,call_5388,var_5387,])
func_5389 = relay.Function([var_5367,var_5368,var_5370,var_5387,], output)
mod['func_5389'] = func_5389
mod = relay.transform.InferType()(mod)
var_5390 = relay.var("var_5390", dtype = "float64", shape = (1512,))#candidate|5390|(1512,)|var|float64
var_5391 = relay.var("var_5391", dtype = "bool", shape = (336,))#candidate|5391|(336,)|var|bool
var_5392 = relay.var("var_5392", dtype = "uint64", shape = (1152,))#candidate|5392|(1152,)|var|uint64
var_5393 = relay.var("var_5393", dtype = "int32", shape = ())#candidate|5393|()|var|int32
output = func_5389(var_5390,var_5391,var_5392,var_5393,)
func_5394 = relay.Function([var_5390,var_5391,var_5392,var_5393,], output)
mutated_mod['func_5394'] = func_5394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4163_call = mutated_mod.get_global_var('func_4163')
call_5408 = relay.TupleGetItem(func_4162_call(), 0)
call_5409 = relay.TupleGetItem(func_4163_call(), 0)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_5410 = func_3859_call()
call_5411 = func_3859_call()
output = relay.Tuple([call_5408,call_5410,])
output2 = relay.Tuple([call_5409,call_5411,])
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
func_4197_call = mod.get_global_var('func_4197')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_5491 = func_4197_call()
call_5492 = func_4197_call()
output = call_5491
output2 = call_5492
func_5496 = relay.Function([], output)
mod['func_5496'] = func_5496
mod = relay.transform.InferType()(mod)
mutated_mod['func_5496'] = func_5496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5496_call = mutated_mod.get_global_var('func_5496')
call_5497 = func_5496_call()
output = call_5497
func_5498 = relay.Function([], output)
mutated_mod['func_5498'] = func_5498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_5530 = func_3536_call()
call_5531 = func_3536_call()
func_3950_call = mod.get_global_var('func_3950')
func_3954_call = mutated_mod.get_global_var('func_3954')
const_5538 = relay.const([-1.321377,-4.743297,-8.137862,-2.371808,-8.513992,-3.568422,8.941853,-3.898086,-3.345086,-3.788552,6.595694,3.022395,9.242672,2.306725,-3.804324,7.914371,-4.790916,-6.982110,6.166980,-1.811465,2.180085,6.938996,1.561952,7.416093,4.642574,5.432771,9.929079,-8.437437,5.251172,-4.271858,2.402639,-3.654249,2.849872,6.369560,-6.650575,-7.184437,-1.402024,-6.187260,-5.363677,2.571442,-8.508171,-0.662650,2.972672,-7.499171,9.919999,-6.320270,-6.684855,-6.230561,-1.840005,3.744505,-1.267249,-3.824405,8.289728,-8.219427,-7.122746,-1.067148,-0.521842,4.394011,5.381912,-2.374521,-6.293392,-6.169384,0.278239,-9.936684,-6.892100,-7.176017,4.991917,7.573347,-0.056761,-9.448342,6.315171,3.029355,-8.774301,7.354825,-8.218886,-7.709252,-4.655854,3.330332,1.684694,8.862983,3.072460,-4.444052,5.866758,-8.600975,1.371277,-9.882316,9.278054,-2.208383,-7.711243,6.820749], dtype = "float64")#candidate|5538|(90,)|const|float64
const_5539 = relay.const([-4,6,1,-3,4,10,7,4,6,-9,2,7,5,-10,8,1,-6,-8,-2,-8,1,2,-8,7,-8,6,10,-3,1,-6,-7,-3,-3,1,-3,4,7,-4,-2,10,5,10,-9,-2,8,-1,4,7,-6,5,-7,5,-4,-8,8,-8,4,-10,-1,-5,-8,-2,-10,-4,-7,-6,-7,-8,-10,9,6,10,-5,5,1,-5,-6,-3,-7,-3,-5,9,-1,-7,5,6,-3,-1,7,6,-4,8,9,-8,-10,1,1,-9,8,3,2,-3,8,-7,10,4,6,5,7,2,-4,5,4,8,-2,3,2,2,2,6,3,-5,4,-6,3,10,-2,1,-1,-8,-1,8,1,-3,9,4,-1,-5,-8,10,9,-9,7,9,-10,-2,9,4,1,-2,1,6,-4,-9,-2,-6,-8,-1,4,2,6,6,-5,-5,2,-9,-3,4,-6,2,1,8,-10,2,-1,-9,-8,4,7,-10,-7,1,5,-9,-8,6,6,9,-5,1,9,4,-7,3,-8,-3,3,8,9,7,-6,-9,1,10,10,1,-3,9,5,-4,-4,-9,2,4,-3,-9,8,-3,5,-2,-5,6,-1,-8,6,9,-2,6,-6,-5,3,-9,-1,7,-4,-5,-5,-6,8,1,9,-4,8,5,2,4,4,-6,6,3,6,8,10,10,-2,-2,2,-2,-7,6,-4,5,-4,3,8,-9,-3,-8,4,1,-8,7,-8,-10,-5,-4,-7,-9,4,10,-9,8,9,-4,-3,-9,9,-1,-4,-2,7,9,7,-4,9,2,-2,-9,6,4,-10,8,-8,6,2,-2,-4,-1,-9,9,-9,-6,-1,4,2,-5,-10,4,4,1,-8,4,-3,10,-10,-2,1,-1,-6,-10,-4,1,-9,-3,4,10,-8,1,-9,-5,-3,-7,-6,-9,-5,9,3,3,-4,5,-2,-8,-7,-2,-4,-5,-4,3,3,10,-8,-5,-8,3,5,-10,2,7,-8,8,-6,1,5,7,6,8,-6,-7,3,6,5,-7,3,8,3,-5,7,6,-10,4,10,-1,4,1,-5,5,5,9,-6,-1,-3,5,-2,5,-5,1,-8,-2,-10,8,-1,9,7,-4,-7,1,1,1,10,-7,-3,-8,1,-3,-4,8,6,-1,-5,7,2,-3,7,-8,10,-9,4,-3,-9,7,7,-9,3,9,7,-2,-5,1,9,-8,5,-1,7,5,10,9,7,2,8,-10,7,-1,10,-6,-3,9,4,-8,-4,6,7,3,3,-6,9,3,1,-10,-8,-10,-3,-1,-7,-7,-6,-6,8,6,7,2,9,1,1,-9,-10,-2,-5,9,3,-4,-8,-1,10,-10,1,-2,-7,-10,-6,9,-9,-10,-7,-8,-4,-1,-5,-1,-10,-1,-2,3,5,10,-6,1,4,-2,2,-1,-4,-3,5,-1,4,7,-4,5,-8,3,6,9,-7,10,1,-10,-6,-4,-6,5,7,-3,-6,2,-5,-8,-1,10,-10,-1,-4,7,-3,-8,-6,-8,6,-5,10,-8,4,-6,5,-5,6,9,7,7,-7,-9,-9,9,10,10,3,5,-4,-2,-8,-5,3,4,9,9,8,2,-7,-5,-5,9,4,7,6,10,-8,-8,-10,10,4,9,9,1,2,-5,4,-7,7,-10,-5,6,-7,4,-7,-7,4,-4,7,1,3,8,-9,8,1,10,10,9,10,-3,8,7,7,-6,-9,4,4,-1,-9,2,9,-5,-8,6,-10,5,2,1,-3,4,8,6,-1,9,-8,-9,-3,-7,9,-8,-4,-6,-5,4,7,-4,9,7,4,10,-6,-10,1,9,9,-8,2,-7,-2,9,-2,-4,-10,9,-8,-8,7,-3,-5,10,-2,7,4,-3,9,-8,6,10,-3,-1,-1,5,-9,6,-3,-8,-7,-2,-10,-7,-8,10,7,9,-10,-2,1,8,-8,-6,3,9,-8,10,6,7,-4,-8,-6,2,-7,-8,4,2,2,-6,-9,-6,-5,-7,6,5,-10,3,-9,-1,-1,-9,-6,-10,7,3,10,5,6,6,-5,-3,3,-8,-1,1,1,-9,-8,-5,-7,-3,10,2,-1,9,9,-8,8,-5,8,-2,-3,-5,-2,-8,-9,-5,10,-6,-8,-4,8,1,1,-4,-1,7,7,-9,-2,-7,-9,-1,-2,7,-3,10,6,-7,7,-5,8,-6,-3,6,-1,8,5,-8,-10,10,-9,-7,10,-9,7,-7,7,-2,10,6,2,1,7,6,-6,1,5,-8,1,-3,-3,-5,-6,1,-6,-7,-4,6,10,7,8,-9,7,7,-7,6,3,-10,-10,-4,9,5,-2,3,2,-5,-9,3,-2,-3,3,8,-5,-6,9,-1,3,-10,-6,-8,4,-9,10,10,-4,-2,4,-4,10,4,-2,-8,1,-2,4,7,5,-2,10,8,4,-3,-10,9,-9,-9,-8,-5,-8,7,-9,1,-10,9,-4,-6,-5,-1,7,6,3,-4,6,-1,8,-8,4,-1,2,-6,4,-9,10,7,9,1,1,-6,-7,-3,7,-2,-1,-7,2,1,3,7,9,-9,9,4,-9,7,9,3,-1,9,9,-5,7,-6,-8,-2,-9,7,4,10,-2,-9,6,7,6,-9,9,-5,2,7,-6,-6,1,-5,-5,-8,1,-5,7,4,7,-10,7,-3,7,-10,-8,-8,-10,-3,7,9,9,4,-6,-1,2,-9,7,10,9,-4,6,5,-6,-8,-10,-2,-1,-4,3,-9,-7,3,-8,7,-3,-4,5,-5,-8,6,10,-4,4,-9,3,1,-6,-3,9,4,1,3,7,-8,8,2,4,10,-4,-5,9,-5,4,1,-8,-7,5,6,5,7,-10,5,5,-3,6,-5,6,10,-10,3,-6,-6,10,2,-7,-3,10,-4,3,3,5,-4,8,1,5,-5,-8,-3,-4,-6,-6,10,6,10,-1,-1,-2,7,7,7,4,4,-2,2,9,-9,-8,-2,4,6,-6,-2,-9,8,7,-9,-7,4,-7,-7,4,-5,6,-9,-9,8,1,4,8,-8,-7,-9,2,-4,-10,7,-9,-8,-10,-7,-1,6,2,-2,4,-7], dtype = "uint64")#candidate|5539|(1152,)|const|uint64
call_5537 = relay.TupleGetItem(func_3950_call(relay.reshape(const_5538.astype('float64'), [15, 6]), relay.reshape(const_5539.astype('uint64'), [1152,]), ), 8)
call_5540 = relay.TupleGetItem(func_3954_call(relay.reshape(const_5538.astype('float64'), [15, 6]), relay.reshape(const_5539.astype('uint64'), [1152,]), ), 8)
var_5543 = relay.var("var_5543", dtype = "float64", shape = (8, 15, 4))#candidate|5543|(8, 15, 4)|var|float64
bop_5544 = relay.logical_xor(call_5530.astype('int64'), relay.reshape(var_5543.astype('int64'), relay.shape_of(call_5530))) # shape=(8, 15, 4)
bop_5547 = relay.logical_xor(call_5531.astype('int64'), relay.reshape(var_5543.astype('int64'), relay.shape_of(call_5531))) # shape=(8, 15, 4)
output = relay.Tuple([call_5537,const_5538,const_5539,bop_5544,])
output2 = relay.Tuple([call_5540,const_5538,const_5539,bop_5547,])
func_5560 = relay.Function([var_5543,], output)
mod['func_5560'] = func_5560
mod = relay.transform.InferType()(mod)
mutated_mod['func_5560'] = func_5560
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5561 = relay.var("var_5561", dtype = "float64", shape = (8, 15, 4))#candidate|5561|(8, 15, 4)|var|float64
func_5560_call = mutated_mod.get_global_var('func_5560')
call_5562 = func_5560_call(var_5561)
output = call_5562
func_5563 = relay.Function([var_5561], output)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_5565 = func_3536_call()
call_5566 = func_3536_call()
output = call_5565
output2 = call_5566
func_5583 = relay.Function([], output)
mod['func_5583'] = func_5583
mod = relay.transform.InferType()(mod)
output = func_5583()
func_5584 = relay.Function([], output)
mutated_mod['func_5584'] = func_5584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_5621 = relay.TupleGetItem(func_5418_call(), 1)
call_5622 = relay.TupleGetItem(func_5420_call(), 1)
output = call_5621
output2 = call_5622
func_5625 = relay.Function([], output)
mod['func_5625'] = func_5625
mod = relay.transform.InferType()(mod)
output = func_5625()
func_5626 = relay.Function([], output)
mutated_mod['func_5626'] = func_5626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5012_call = mod.get_global_var('func_5012')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_5640 = relay.TupleGetItem(func_5012_call(), 3)
call_5641 = relay.TupleGetItem(func_5013_call(), 3)
func_546_call = mod.get_global_var('func_546')
func_549_call = mutated_mod.get_global_var('func_549')
var_5645 = relay.var("var_5645", dtype = "uint8", shape = (728,))#candidate|5645|(728,)|var|uint8
call_5644 = relay.TupleGetItem(func_546_call(relay.reshape(var_5645.astype('uint8'), [13, 4, 14]), relay.reshape(var_5645.astype('uint8'), [13, 4, 14]), ), 5)
call_5646 = relay.TupleGetItem(func_549_call(relay.reshape(var_5645.astype('uint8'), [13, 4, 14]), relay.reshape(var_5645.astype('uint8'), [13, 4, 14]), ), 5)
func_5315_call = mod.get_global_var('func_5315')
func_5316_call = mutated_mod.get_global_var('func_5316')
call_5654 = func_5315_call()
call_5655 = func_5315_call()
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_5693 = func_3896_call()
call_5694 = func_3896_call()
func_3950_call = mod.get_global_var('func_3950')
func_3954_call = mutated_mod.get_global_var('func_3954')
var_5712 = relay.var("var_5712", dtype = "float64", shape = (90,))#candidate|5712|(90,)|var|float64
var_5713 = relay.var("var_5713", dtype = "uint64", shape = (1152,))#candidate|5713|(1152,)|var|uint64
call_5711 = relay.TupleGetItem(func_3950_call(relay.reshape(var_5712.astype('float64'), [15, 6]), relay.reshape(var_5713.astype('uint64'), [1152,]), ), 4)
call_5714 = relay.TupleGetItem(func_3954_call(relay.reshape(var_5712.astype('float64'), [15, 6]), relay.reshape(var_5713.astype('uint64'), [1152,]), ), 4)
func_5042_call = mod.get_global_var('func_5042')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_5717 = relay.TupleGetItem(func_5042_call(), 0)
call_5718 = relay.TupleGetItem(func_5044_call(), 0)
func_4743_call = mod.get_global_var('func_4743')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_5735 = relay.TupleGetItem(func_4743_call(), 0)
call_5736 = relay.TupleGetItem(func_4745_call(), 0)
output = relay.Tuple([call_5640,call_5644,var_5645,call_5654,call_5693,call_5711,var_5712,var_5713,call_5717,call_5735,])
output2 = relay.Tuple([call_5641,call_5646,var_5645,call_5655,call_5694,call_5714,var_5712,var_5713,call_5718,call_5736,])
func_5738 = relay.Function([var_5645,var_5712,var_5713,], output)
mod['func_5738'] = func_5738
mod = relay.transform.InferType()(mod)
mutated_mod['func_5738'] = func_5738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5738_call = mutated_mod.get_global_var('func_5738')
var_5740 = relay.var("var_5740", dtype = "uint8", shape = (728,))#candidate|5740|(728,)|var|uint8
var_5741 = relay.var("var_5741", dtype = "float64", shape = (90,))#candidate|5741|(90,)|var|float64
var_5742 = relay.var("var_5742", dtype = "uint64", shape = (1152,))#candidate|5742|(1152,)|var|uint64
call_5739 = func_5738_call(var_5740,var_5741,var_5742,)
output = call_5739
func_5743 = relay.Function([var_5740,var_5741,var_5742,], output)
mutated_mod['func_5743'] = func_5743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_5753 = func_3759_call()
call_5754 = func_3759_call()
output = call_5753
output2 = call_5754
func_5768 = relay.Function([], output)
mod['func_5768'] = func_5768
mod = relay.transform.InferType()(mod)
mutated_mod['func_5768'] = func_5768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5768_call = mutated_mod.get_global_var('func_5768')
call_5769 = func_5768_call()
output = call_5769
func_5770 = relay.Function([], output)
mutated_mod['func_5770'] = func_5770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5315_call = mod.get_global_var('func_5315')
func_5316_call = mutated_mod.get_global_var('func_5316')
call_5816 = func_5315_call()
call_5817 = func_5315_call()
uop_5823 = relay.tan(call_5816.astype('float32')) # shape=(8, 15, 4)
uop_5825 = relay.tan(call_5817.astype('float32')) # shape=(8, 15, 4)
output = uop_5823
output2 = uop_5825
func_5833 = relay.Function([], output)
mod['func_5833'] = func_5833
mod = relay.transform.InferType()(mod)
mutated_mod['func_5833'] = func_5833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5833_call = mutated_mod.get_global_var('func_5833')
call_5834 = func_5833_call()
output = call_5834
func_5835 = relay.Function([], output)
mutated_mod['func_5835'] = func_5835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5838 = relay.var("var_5838", dtype = "int64", shape = ())#candidate|5838|()|var|int64
const_5839 = relay.const([[[-10,-3,-3,10,1,-2,5,1,1,10,-8],[-3,4,-3,-2,4,-5,8,10,-1,1,3],[9,-3,-9,-2,-2,5,-6,5,-1,1,-8],[4,-8,10,-6,5,-8,6,3,-4,4,-1],[8,-10,8,4,10,-5,-1,-8,-9,4,3],[-5,-9,3,8,6,1,6,-7,5,-8,-6],[7,-8,6,2,-4,-6,-5,8,5,3,10],[-7,-2,4,5,1,-1,10,10,7,-8,9],[-3,1,1,-6,-5,-7,7,9,1,-8,8],[2,-10,4,-3,3,9,6,10,-2,8,6],[-3,1,-4,6,7,-1,-6,-4,9,-7,-5],[-10,-8,2,4,-3,-2,10,-3,9,6,-6]],[[-7,3,10,-4,-4,10,1,-10,-1,-3,-7],[-8,-1,2,-8,-2,-9,-1,-5,-5,-1,5],[-8,-6,-7,-1,-2,-7,-7,10,7,8,-7],[6,4,-4,-8,-7,-3,-7,-2,7,9,-6],[-4,2,10,-7,9,-10,-7,-9,3,-3,-9],[-9,1,2,1,-6,8,-8,8,-9,1,1],[4,-2,6,-5,8,-5,-7,8,-6,-5,-10],[7,8,-6,-3,-6,-9,-8,-4,1,5,10],[2,2,-10,-4,-1,10,-5,8,-5,9,-3],[-8,-7,10,2,4,7,4,4,-10,9,4],[-8,3,7,7,8,6,4,-7,-5,2,8],[9,-2,-7,-1,-6,-1,2,3,-7,-5,-8]],[[8,-7,10,-5,3,-10,-7,9,-6,-8,-4],[-7,10,-9,9,-3,-7,-2,-8,-5,2,-10],[-10,8,-2,5,5,-6,-7,9,6,-1,-2],[10,-1,-5,-8,-4,3,-6,-6,-2,4,7],[5,-5,10,4,10,-4,-6,-4,3,5,-9],[1,-4,8,3,9,-3,-8,2,-7,-5,1],[-9,10,-4,9,7,-9,-5,1,4,5,-4],[-2,-9,7,9,7,-7,-3,-3,-4,-10,-3],[2,2,-2,5,4,-10,-6,6,7,7,-2],[4,-1,-8,-1,-8,3,-1,9,-10,-5,5],[-7,1,8,-9,8,-8,10,-2,4,-6,-9],[1,4,2,-2,-3,2,5,9,10,5,-6]],[[3,8,7,-6,10,6,-9,-3,9,-1,7],[-1,-10,-4,1,2,8,-3,3,-3,7,6],[10,-6,-3,-10,-3,-7,-1,7,-2,6,-6],[-7,8,-1,9,-10,7,8,5,10,-8,-10],[-9,3,-6,5,7,3,2,-10,-3,2,8],[-2,7,-2,1,5,1,-3,-4,10,-10,9],[-7,5,-9,2,6,-4,-5,7,10,-6,-10],[9,7,7,10,-9,5,9,-10,5,6,-8],[-8,9,-9,-3,7,-2,9,2,-7,8,-7],[-8,-1,-3,-4,10,-6,-2,-5,3,-4,6],[6,5,-3,7,-2,-6,-8,10,10,4,10],[-2,-10,8,-1,9,4,-3,7,-8,-5,-9]],[[-5,-6,10,2,5,-6,-10,1,1,-3,2],[-4,5,7,6,4,-7,-8,-10,9,-6,-2],[-9,10,-3,-5,-8,-3,10,-7,-7,10,3],[1,8,-1,-4,1,-6,-3,5,-3,8,-7],[7,7,-7,8,-2,-3,10,5,7,-9,-8],[-3,2,-7,3,9,10,-5,-10,4,3,-2],[-3,7,2,6,-8,-4,-4,-9,5,-8,3],[-9,-6,6,-4,10,-7,9,3,-1,2,-1],[4,-7,9,3,9,-6,-9,-4,-5,10,5],[1,-5,-9,8,7,-10,-3,10,-3,-2,-5],[3,3,6,-10,-5,9,5,-8,7,-7,10],[8,-7,-6,-9,-1,-10,10,10,-7,3,6]],[[3,1,1,-1,-9,8,7,5,7,-8,-10],[5,2,-8,9,5,10,-3,5,10,2,-9],[4,-5,-2,7,5,4,5,2,-6,5,-6],[-6,4,-4,6,5,9,-2,-5,5,-3,7],[10,2,-8,-3,7,5,7,-8,-3,4,3],[5,7,9,-8,7,-6,8,-8,-8,10,6],[3,10,-7,1,2,-1,5,-8,4,3,-8],[4,9,1,-7,9,-1,7,-5,1,4,8],[-9,10,-4,3,-3,-8,-3,4,-5,10,-1],[-7,5,6,9,-9,-10,2,-4,-8,6,-1],[-6,-6,7,-9,5,7,-4,-1,6,-1,-1],[-2,2,1,-7,-6,7,-4,-10,-7,10,6]],[[8,9,7,2,-7,-4,6,6,10,-8,3],[-3,6,-9,3,-2,-3,5,-3,2,3,8],[1,-7,-5,8,-9,-3,1,3,9,7,8],[-4,10,10,1,-5,3,1,-8,-6,-2,-4],[-10,8,-4,-1,-8,-5,2,2,-5,-4,-2],[4,6,9,-10,-10,1,10,-3,-10,-10,9],[-2,5,-9,-6,6,1,2,9,-2,-4,6],[-10,7,-2,-7,-10,4,-8,4,4,-8,1],[6,3,8,-2,-1,7,-4,-6,-2,4,10],[8,8,6,-8,5,7,-1,5,-3,-6,4],[-1,-3,-7,-6,-10,2,6,-3,5,8,6],[-8,1,-7,4,-8,-2,-8,9,7,-8,-5]],[[-7,1,-6,3,-8,-3,4,7,1,-3,-6],[1,4,-3,7,1,8,-7,10,-6,-2,-7],[-1,2,-8,5,5,9,4,-4,-4,6,-6],[6,-10,2,3,8,-4,6,-7,-7,-6,4],[10,10,4,6,6,5,6,10,7,-5,-10],[4,-1,10,5,7,3,-1,-3,6,-1,-5],[-8,-6,3,-7,-4,10,10,-5,5,2,9],[-6,2,-2,-3,-8,4,-8,-9,9,4,1],[1,-10,-9,-6,-10,3,-6,-3,-3,-10,8],[3,-10,1,4,-1,7,3,8,6,-4,7],[3,-9,-2,-5,-6,6,-3,-4,-8,-5,-8],[2,-10,1,-7,-3,10,-1,2,3,-4,-6]],[[7,-7,-6,-9,-1,-8,1,-4,-10,1,1],[-2,-5,3,-5,10,10,6,-10,-8,-8,-9],[-8,7,9,9,9,-5,8,6,8,7,3],[-1,10,3,10,9,6,7,6,-7,9,1],[-9,-5,5,4,7,3,7,-7,10,6,-2],[1,-2,4,10,1,2,-8,-9,-5,10,-4],[-3,-5,-5,-9,5,-8,8,-8,-5,2,6],[4,-2,2,6,8,-4,-2,-5,9,-1,-9],[-7,9,-8,9,1,-9,-10,-7,-6,-6,10],[-1,-9,7,5,8,2,4,-8,-4,-6,-2],[-6,5,-3,-2,8,-8,-2,-4,-10,1,-10],[10,9,7,-8,4,-9,6,9,-7,-9,-4]]], dtype = "int64")#candidate|5839|(9, 12, 11)|const|int64
bop_5840 = relay.add(var_5838.astype('int64'), const_5839.astype('int64')) # shape=(9, 12, 11)
output = bop_5840
output2 = bop_5840
func_5879 = relay.Function([var_5838,], output)
mod['func_5879'] = func_5879
mod = relay.transform.InferType()(mod)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5880 = relay.var("var_5880", dtype = "int64", shape = ())#candidate|5880|()|var|int64
func_5879_call = mutated_mod.get_global_var('func_5879')
call_5881 = func_5879_call(var_5880)
output = call_5881
func_5882 = relay.Function([var_5880], output)
mutated_mod['func_5882'] = func_5882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_5894 = relay.TupleGetItem(func_3274_call(), 0)
call_5895 = relay.TupleGetItem(func_3275_call(), 0)
output = relay.Tuple([call_5894,])
output2 = relay.Tuple([call_5895,])
func_5927 = relay.Function([], output)
mod['func_5927'] = func_5927
mod = relay.transform.InferType()(mod)
output = func_5927()
func_5928 = relay.Function([], output)
mutated_mod['func_5928'] = func_5928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4197_call = mod.get_global_var('func_4197')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_5967 = func_4197_call()
call_5968 = func_4197_call()
func_1280_call = mod.get_global_var('func_1280')
func_1283_call = mutated_mod.get_global_var('func_1283')
const_6002 = relay.const([[-2.821376,8.413676,-7.730554,4.931361,-3.522396,-2.578902,-8.984845,6.872398,3.398001,-8.906781,8.782119,2.883903,6.376363,1.425143,6.055191,6.277057,1.325431,9.606825,1.881094,-3.621589,8.667099,8.425802,-1.936770,-1.766440,7.314662,8.710028,4.527359,-0.271368,1.862230,0.972205,3.201510,-1.523334,1.352347,-3.025455,-9.054861,7.418438,0.324476,-3.210218,9.440475,0.118083,1.967205,0.602149,-7.734394,3.820104,8.628126,-9.986424,-4.237500,-9.713402,8.496998,-8.834167,8.047200,2.253878,-2.920354,-4.102067,-3.782126,5.360282,-9.302293,-1.445332,-8.026272,-1.919762,-2.272111,-3.250147,8.698639,2.053834,-3.547623,7.762548,4.677100,-8.780121,-8.490088,5.505940,8.596147,-3.344410,9.307857,-9.244850,-1.520720,-2.525162,7.061362,4.579538,3.034872,6.847109,-9.596217,1.708828,4.602427,-5.171079,-8.970612,-0.257073,-5.419219,-3.279600,-5.330680,9.925537,7.235937,4.291482,1.930857,-4.304613,7.536526,-5.111486,-1.558066,5.618780,2.889323,9.922365,0.500814,6.178005,-9.129552,-1.834887,-1.155536,9.228320,1.288131,9.003947,-1.144209,0.211168,9.678555,3.739570,1.857559,-3.777587,-5.919670,-5.407267,7.475006,9.950996,9.569331,-8.073560,-4.136208,-1.008419,5.139898,-3.729304,6.134988,8.494301,2.856051,-4.998241,-2.967131,4.928479,-4.129636,-2.525384,-1.311921,8.607669,4.864408,0.138560,0.532819,0.802121,1.206575,-8.921061,5.095778,-1.937996,0.487669,0.811427,7.699066,-6.458070,0.610536,6.137732,5.223405,9.222057,5.232164,-5.707762,-6.437179,8.559472,7.843671,-0.720567,1.998335,9.073183,4.431839,-1.071765,1.457592,-4.927557,-1.976876,-2.648118,-5.009698,-0.339509,1.469990,7.166241,1.694564,1.033179,-1.772461,0.465838,-3.995945,-7.580028,-0.530625,-7.671749,-4.152942,-3.924561,9.952897,-4.881691,-5.056617,9.310638,9.844070,-6.173307,2.352508,0.549931,5.934828,1.493627,9.872370,-4.367545,9.184613,3.631056,2.620629,-7.745556,2.017471,8.946291,1.476906,3.746744,8.908219,4.205897,1.803966,-4.322752,-3.448697,4.872236,-8.488788,7.933960,-9.163557,9.444207,-4.830596,-4.566625,-4.962229,3.862676,-6.910172,-2.269805,-6.859397,-5.553046,-3.278886,6.708708,1.562956,-9.504395,-6.244795,0.006551,-4.799536,-9.298396,-8.969270,-3.206253,-3.929062,-9.545441,-4.524996,-6.307305,9.623312,3.742836,-9.251594,-7.130821,0.742495,9.798691,-1.527170,-3.530562,1.562565,8.836876,-2.776962,-5.929624,9.776785,7.634042,3.675249,9.398877,1.974066,-3.437535,6.167938,5.973140,5.964671,-7.062560,3.599765,-6.956860,7.752894,-7.149240,-0.878377,6.813872,7.013425,9.790305,-7.615114,1.368832,9.858001,1.256895,-1.042978,1.930363,5.480089,1.092682,5.934118,3.276264,6.390348,-1.894494,-5.504012,-2.341749,-6.201620,-0.705248,-6.790751,-0.952104,8.508500,-0.170721,-0.877964,5.522997,3.423920,-6.621708,6.528023,7.202096,3.249698,-7.553161,4.550583,-9.236334,-7.198604,1.577768,-5.942771,0.045349,7.543422,-7.995314,2.738599,-3.072078,-4.458398,4.004457,-7.195140,7.404453,-7.172532,-7.024441,-8.247657,-5.329507,0.621284,0.134554,7.060269,-5.675541,-3.521660,3.607260,-9.582949,-2.629080,-7.236242,-2.474834,-6.781287,8.542474,3.913245,0.486538,-0.857747,3.198532,6.523090,7.581854,0.007181,1.272165,-3.015304,1.879947,-8.489786,-3.160509,-0.502800,-0.159936,-7.889433,4.654868,8.371146,4.654235,-5.688120,9.289965,5.222369,8.115057,-1.665167,-3.628245,2.079095,-2.417710,2.266014,-1.346403,4.152215,-6.627062,-7.877054,-6.634471,-3.028021,4.040997,-6.846880,-3.732212,-4.762995,-9.701649,7.407568,5.073015,-3.240615,-3.469423]], dtype = "float64")#candidate|6002|(1, 360)|const|float64
var_6003 = relay.var("var_6003", dtype = "float64", shape = (924,))#candidate|6003|(924,)|var|float64
call_6001 = relay.TupleGetItem(func_1280_call(relay.reshape(const_6002.astype('float64'), [9, 10, 4]), relay.reshape(var_6003.astype('float64'), [154, 6]), ), 1)
call_6004 = relay.TupleGetItem(func_1283_call(relay.reshape(const_6002.astype('float64'), [9, 10, 4]), relay.reshape(var_6003.astype('float64'), [154, 6]), ), 1)
output = relay.Tuple([call_5967,call_6001,const_6002,var_6003,])
output2 = relay.Tuple([call_5968,call_6004,const_6002,var_6003,])
func_6010 = relay.Function([var_6003,], output)
mod['func_6010'] = func_6010
mod = relay.transform.InferType()(mod)
var_6011 = relay.var("var_6011", dtype = "float64", shape = (924,))#candidate|6011|(924,)|var|float64
output = func_6010(var_6011)
func_6012 = relay.Function([var_6011], output)
mutated_mod['func_6012'] = func_6012
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6019 = relay.var("var_6019", dtype = "float64", shape = (3, 6, 16))#candidate|6019|(3, 6, 16)|var|float64
uop_6020 = relay.log2(var_6019.astype('float64')) # shape=(3, 6, 16)
func_5738_call = mod.get_global_var('func_5738')
func_5743_call = mutated_mod.get_global_var('func_5743')
const_6026 = relay.const([-6,7,1,-8,1,-9,-6,-5,5,8,-3,-8,-1,-1,7,5,-8,-9,-10,-2,-8,-9,-8,-7,2,-2,4,10,-8,2,-2,9,9,-7,-7,-1,-1,-1,-7,-3,-6,4,6,-7,-6,10,-6,-5,8,-4,-10,2,-7,2,3,-1,-4,-3,10,5,-1,-3,5,-1,-10,8,2,-5,4,1,7,-8,-8,9,1,3,10,-8,-3,-8,6,7,7,-4,-1,8,-10,7,7,5,2,1,-5,-7,-10,3,10,-3,-4,-5,6,3,2,-4,-7,-9,9,1,3,-2,2,8,-7,-8,-9,-8,-8,1,-10,-9,5,8,-9,10,8,4,9,-1,-2,9,-1,6,-7,-9,1,-6,5,-2,6,6,-2,-1,2,-9,-10,-10,5,-2,5,1,-9,-2,-2,1,-6,1,9,1,5,-10,8,8,5,6,-1,-6,6,7,4,-8,-6,8,-1,9,-9,-1,-6,-2,8,3,-7,-2,-10,-10,8,5,-7,1,4,-5,6,1,6,-7,1,8,10,10,-10,6,-10,-3,-6,6,2,-2,-9,4,-8,4,10,7,1,-2,8,8,-9,-5,-5,4,2,8,2,-1,-1,-10,-6,-5,-4,7,-6,-10,-7,-9,-7,2,2,-3,9,3,-10,5,7,2,-6,5,-7,9,1,-8,3,-8,-7,-7,6,10,-2,1,-4,3,3,4,-3,5,10,-10,1,-8,-10,9,-5,-3,4,6,-8,-8,7,2,4,3,9,7,-3,2,-1,3,-8,5,-2,-9,-10,-3,10,6,-3,8,-2,3,1,1,6,8,-10,-7,-3,-3,3,1,-1,7,-8,5,-1,7,4,4,4,4,-4,-8,-7,-2,-7,4,-4,2,-8,-1,-3,-9,-10,7,-6,10,1,-8,1,9,-5,-7,-5,-10,-6,-10,-3,8,-3,-7,-7,8,9,6,-6,-9,9,-1,-7,-7,-3,-1,-9,2,-3,10,8,-8,4,6,-3,4,-10,-8,5,9,-4,8,7,-5,9,-2,5,-3,-6,-10,5,-10,-8,-4,-6,5,-1,-3,-1,3,-4,-8,-3,-8,1,7,-4,10,7,-7,7,3,4,-8,-4,8,6,-9,-6,-9,6,2,-4,2,-8,-4,-2,5,-3,-5,-6,7,7,-10,-2,10,6,8,8,-3,2,1,6,-1,9,-10,-7,6,10,8,8,1,-2,5,-10,6,10,5,-5,9,-2,-8,3,-4,-3,-6,-10,4,6,4,10,8,-9,-7,1,8,-2,-4,-4,9,-1,-6,-2,5,-10,3,-10,1,6,-6,2,10,-2,-9,3,2,3,-4,-10,2,-1,1,8,3,-8,10,-2,-3,5,1,-8,-1,-2,-5,-6,-4,1,-10,-7,-2,-3,6,5,2,-1,-9,7,-9,4,3,10,9,-5,10,-4,-9,-9,6,4,3,2,-4,1,-10,-7,9,2,-9,-8,1,5,3,-4,-7,7,-4,3,6,3,-1,8,-10,-9,-9,1,-1,9,10,10,-4,7,-4,7,-4,-7,-3,-4,-7,-3,10,-6,8,-4,1,-6,-3,-2,-1,10,-1,8,-1,-8,-7,-7,-3,-7,-10,-1,-9,5,-8,-8,10,-4,-4,-7,-7,5,4,-1,7,-9,-3,8,-9,-1,-2,6,8,10,-2,-6,2,3,5,4,-5,9,-5,-9,9,-1,-10,10,-7,-9,9,-10,-7,8,10,-4,-7,3,7,6,4,7,-6,-2,-9,-4,6,-9,8,7,-9,2,-1,8,9,-5,5,8,9,6,3,-6,5,-4,-5,2,-9,10,1,9,3,-4,-6,-10,2,-2,-10,-4,6,-10,8,-4,6,8,-1,-7,10,3,-4,2,-2,3,-5,-7,-6,1,-8,-10,9,2,-6,4,-2,4,3,2,-2,-7,1,-9,10,-10,5,3,-9,-3,3,10,6,1,-10,5,7,9,6,6,8], dtype = "uint8")#candidate|6026|(728,)|const|uint8
var_6027 = relay.var("var_6027", dtype = "float64", shape = (90, 1))#candidate|6027|(90, 1)|var|float64
var_6028 = relay.var("var_6028", dtype = "uint64", shape = (24, 48))#candidate|6028|(24, 48)|var|uint64
call_6025 = relay.TupleGetItem(func_5738_call(relay.reshape(const_6026.astype('uint8'), [728,]), relay.reshape(var_6027.astype('float64'), [90,]), relay.reshape(var_6028.astype('uint64'), [1152,]), ), 9)
call_6029 = relay.TupleGetItem(func_5743_call(relay.reshape(const_6026.astype('uint8'), [728,]), relay.reshape(var_6027.astype('float64'), [90,]), relay.reshape(var_6028.astype('uint64'), [1152,]), ), 9)
uop_6033 = relay.acos(uop_6020.astype('float64')) # shape=(3, 6, 16)
output = relay.Tuple([call_6025,const_6026,var_6027,var_6028,uop_6033,])
output2 = relay.Tuple([call_6029,const_6026,var_6027,var_6028,uop_6033,])
func_6035 = relay.Function([var_6019,var_6027,var_6028,], output)
mod['func_6035'] = func_6035
mod = relay.transform.InferType()(mod)
mutated_mod['func_6035'] = func_6035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6035_call = mutated_mod.get_global_var('func_6035')
var_6037 = relay.var("var_6037", dtype = "float64", shape = (3, 6, 16))#candidate|6037|(3, 6, 16)|var|float64
var_6038 = relay.var("var_6038", dtype = "float64", shape = (90, 1))#candidate|6038|(90, 1)|var|float64
var_6039 = relay.var("var_6039", dtype = "uint64", shape = (24, 48))#candidate|6039|(24, 48)|var|uint64
call_6036 = func_6035_call(var_6037,var_6038,var_6039,)
output = call_6036
func_6040 = relay.Function([var_6037,var_6038,var_6039,], output)
mutated_mod['func_6040'] = func_6040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_6069 = relay.TupleGetItem(func_3274_call(), 0)
call_6070 = relay.TupleGetItem(func_3275_call(), 0)
func_5042_call = mod.get_global_var('func_5042')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_6079 = relay.TupleGetItem(func_5042_call(), 0)
call_6080 = relay.TupleGetItem(func_5044_call(), 0)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_6082 = relay.TupleGetItem(func_5418_call(), 1)
call_6083 = relay.TupleGetItem(func_5420_call(), 1)
func_2745_call = mod.get_global_var('func_2745')
func_2749_call = mutated_mod.get_global_var('func_2749')
const_6092 = relay.const([4.432648,-8.818408,-1.009340,5.580479,4.010094,-3.620577,1.894319,-6.778321,-7.061581,-2.106099,-0.750108,-5.288012,6.937135,-1.818545,9.656626,-7.164013,6.066358,5.925168,2.877655,5.804770,7.324844,-0.358567,1.576820,-4.702119,-6.343486,7.162903,-2.058434,-8.578580,-7.300476,-0.701260,-4.575162,-8.277602,-0.105823,6.435937,-1.828176,-0.268779,3.479900,-4.455493,-6.752390,-4.855878,6.080980,6.880269,7.233249,2.499530,-4.517535,-1.756430,4.305866,7.441388,-9.094246,3.066292,6.171288,0.272633,-0.064769,0.431917,-4.407789,-0.283725,3.056322,8.200237,3.584788,-6.829890,8.403240,-7.271498,2.932153,-3.140247,-1.464336,-8.988300,5.790929,-1.770864,9.073261,-3.853363,-7.283656,8.634962,1.183586,-0.918328,-6.070522,-0.059830,7.265672,-7.150713,-9.124593,5.937703,-7.338588,-3.753200,7.421484,4.236114,-5.172164,-5.847536,-7.000177,8.513490,3.230030,-7.684478,-9.008890,9.054081,7.282366,2.594907,-9.088114,5.233578,-7.536193,-2.002117,-1.705454,7.753833,-0.353815,6.121326,4.277047,-8.893399,1.065757,-1.619950,4.518241,9.420598,0.409943,9.926511,5.989790,-6.442286,-1.227511,5.689396,3.943758,-7.900116,4.167823,-6.318856,-4.919378,2.938935,-7.049068,5.137707,5.034258,-3.702996,8.535718,-0.579333,-9.772894,8.003557,1.287918,-1.875978,1.343889,-2.381451,-8.121099,7.645045,9.215211,-4.892064,1.824029,-6.691434,6.893527,6.592748,-6.823453,1.989814,5.642995,7.267649,-7.106094,6.235009,-3.520626,-8.327957,-2.931028,0.369149,-6.623960,9.882276,-7.585123,-7.660875,9.297115,-3.706875,3.385907,-4.761048,-3.190128,5.001331,6.083664,-8.697478,2.634691,9.180243,0.188680,5.243089,-3.968987,6.421402,-3.390923,-9.065832,5.515268,3.947200,1.733605,9.552628,-9.714671,-5.181588,7.368383,7.395331,7.503609,8.254332,-9.410660,-9.811555,3.994471,7.333845,9.972379,4.441004,-4.031393,9.545036,1.427541,-6.884424,2.480603,5.280601,1.095883,2.026978,7.646503,0.433271,-7.898853,5.531953,0.101894,6.442753,-3.596263,-7.591359,-1.012242,-2.039635,-8.205184,1.633862,2.056387,5.685342,2.068133,4.408982,9.879336,-8.721242,-1.944302,1.246572,-5.152877,-7.381750,-5.344242,-9.906222,-6.630652,-2.824930,9.110855,8.257282,-8.496948,7.452916,8.678530,3.955894,-3.609599,-9.098607,6.969976,-6.761424,0.704513,-6.908651,8.233632,-6.759926,-8.628210,5.559528,-1.901224,-7.676482,2.145757,-4.365561,7.882538,0.890980,-5.099983,-2.618442,6.924215,3.374467,-7.325147,-9.262009,-1.500493,2.706340,6.841868,-8.933118,3.004953,7.717944,0.135596,-5.692642,1.237454,-0.496515,0.779067,9.360858,8.853515,5.058310,-5.930566,-9.249271,-0.249377,7.691249,-5.431991,1.786494,2.596608,-7.126161,7.651948,9.134679,-1.538068,-9.474350,-1.224873,-1.756850,-3.676784,1.931616,-9.869892,-3.395614,-4.398839,-3.863937,2.574027,-2.260494,-2.478316,5.777519,2.247697,-9.268255,-7.285832,-4.948955,-7.884324,4.411726,-4.749937,-5.328198,-6.939780,-9.909752,-0.026185,4.194766,-4.739790,-0.464401,-1.133636,-1.911082,-8.373110,7.335358,0.206763,-2.789456,-0.423590,8.083900,-4.209247,6.435895,-1.109632,6.160278,5.529502,-1.673763,0.454390,-4.269399,9.901339,9.031726,-6.390693,-4.855626,-6.563104,2.517916,-2.630573,-9.382988,-4.720798,1.813827,3.222337,-4.869471,1.124053,-8.717697,3.325462,-0.114952,-2.954084,9.369434,-0.645668,-3.917605,-4.199823,-5.537216,-2.451747,1.493822,-8.250722,4.647860,-5.250203,-6.034221,4.236517,-3.767662,-6.478467,1.972661,-7.859222,8.747422,-8.065596,-3.422361,8.240787,-4.430167,5.786572,1.636119,-1.403908,5.684738,-8.674738,2.620705,-2.131229,-4.498211,-1.424663,2.117782,-1.247103,-0.397604,7.456511,7.780980,9.318998,-7.700723,-2.476819,-0.441509,6.006209,3.888360,-5.181921,2.891246,-5.085478,4.699874,6.748839,4.442993,9.739346,-1.322921,-4.210255,0.062251,7.681424,-9.790306,6.900107,3.423692,-6.350848,-3.009705,1.348327,-6.915421,-9.754223,-7.283157,-6.209505,6.739128,7.830463,-7.943421,-4.735783,9.611730,-8.685727,5.208375,1.459894,-9.402654,5.336448,-1.462198,-0.422294,-2.686695,-7.901815,-4.529091,-6.036413,-7.727144,5.371358,-7.697260,-6.525060,-5.765796,3.790967,4.902940,-3.899601,4.459169,-2.800476,-5.111051,-8.739765,7.927394,6.763946,3.489669,-3.511145,-5.914182,4.606516,4.612050,-4.579329,-2.945263,6.717898,-0.535061,0.300908,4.307171,0.626812,-5.056224,-2.825669,-7.463820,2.064734,9.349990,5.731441,7.299928,-6.180834,0.836170,-8.077127,8.517217,7.600087,0.953545,3.477334,-4.971616,-9.568157,-3.073651,0.450806,5.059972,-1.535032,-7.120409,-6.142600,-8.269551,-4.562340,1.539228,3.193180,-6.433249,2.122238,8.862463,-5.511851,9.033891,-5.926713,4.195973,1.366749,-9.251376,7.431404,4.770736,1.602183,5.837571,1.974171,-2.265883,5.175656,1.916874,4.803137,9.354007,3.392226,-4.527839,-7.469264,4.420971,-4.074055,8.471190,-5.155947,6.432402,3.350454,6.405420,-6.497847,3.586247,-0.406958,-6.689603,-6.507712,1.100032,-5.438378,2.718294,0.965098,-6.267630,3.187951,6.152113], dtype = "float64")#candidate|6092|(504,)|const|float64
call_6091 = relay.TupleGetItem(func_2745_call(relay.reshape(const_6092.astype('float64'), [12, 3, 14]), relay.reshape(const_6092.astype('float64'), [12, 3, 14]), relay.reshape(const_6092.astype('float64'), [12, 3, 14]), ), 0)
call_6093 = relay.TupleGetItem(func_2749_call(relay.reshape(const_6092.astype('float64'), [12, 3, 14]), relay.reshape(const_6092.astype('float64'), [12, 3, 14]), relay.reshape(const_6092.astype('float64'), [12, 3, 14]), ), 0)
output = relay.Tuple([call_6069,call_6079,call_6082,call_6091,const_6092,])
output2 = relay.Tuple([call_6070,call_6080,call_6083,call_6093,const_6092,])
func_6094 = relay.Function([], output)
mod['func_6094'] = func_6094
mod = relay.transform.InferType()(mod)
mutated_mod['func_6094'] = func_6094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6094_call = mutated_mod.get_global_var('func_6094')
call_6095 = func_6094_call()
output = call_6095
func_6096 = relay.Function([], output)
mutated_mod['func_6096'] = func_6096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4163_call = mutated_mod.get_global_var('func_4163')
call_6111 = relay.TupleGetItem(func_4162_call(), 0)
call_6112 = relay.TupleGetItem(func_4163_call(), 0)
output = call_6111
output2 = call_6112
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
func_5496_call = mod.get_global_var('func_5496')
func_5498_call = mutated_mod.get_global_var('func_5498')
call_6150 = func_5496_call()
call_6151 = func_5496_call()
output = call_6150
output2 = call_6151
func_6171 = relay.Function([], output)
mod['func_6171'] = func_6171
mod = relay.transform.InferType()(mod)
mutated_mod['func_6171'] = func_6171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6171_call = mutated_mod.get_global_var('func_6171')
call_6172 = func_6171_call()
output = call_6172
func_6173 = relay.Function([], output)
mutated_mod['func_6173'] = func_6173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4504_call = mod.get_global_var('func_4504')
func_4506_call = mutated_mod.get_global_var('func_4506')
call_6206 = relay.TupleGetItem(func_4504_call(), 0)
call_6207 = relay.TupleGetItem(func_4506_call(), 0)
output = relay.Tuple([call_6206,])
output2 = relay.Tuple([call_6207,])
func_6243 = relay.Function([], output)
mod['func_6243'] = func_6243
mod = relay.transform.InferType()(mod)
output = func_6243()
func_6244 = relay.Function([], output)
mutated_mod['func_6244'] = func_6244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_6304 = relay.TupleGetItem(func_3130_call(), 0)
call_6305 = relay.TupleGetItem(func_3131_call(), 0)
output = call_6304
output2 = call_6305
func_6309 = relay.Function([], output)
mod['func_6309'] = func_6309
mod = relay.transform.InferType()(mod)
output = func_6309()
func_6310 = relay.Function([], output)
mutated_mod['func_6310'] = func_6310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6094_call = mod.get_global_var('func_6094')
func_6096_call = mutated_mod.get_global_var('func_6096')
call_6378 = relay.TupleGetItem(func_6094_call(), 4)
call_6379 = relay.TupleGetItem(func_6096_call(), 4)
output = call_6378
output2 = call_6379
func_6387 = relay.Function([], output)
mod['func_6387'] = func_6387
mod = relay.transform.InferType()(mod)
output = func_6387()
func_6388 = relay.Function([], output)
mutated_mod['func_6388'] = func_6388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5833_call = mod.get_global_var('func_5833')
func_5835_call = mutated_mod.get_global_var('func_5835')
call_6471 = func_5833_call()
call_6472 = func_5833_call()
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_6473 = relay.TupleGetItem(func_3274_call(), 0)
call_6474 = relay.TupleGetItem(func_3275_call(), 0)
func_5012_call = mod.get_global_var('func_5012')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_6479 = relay.TupleGetItem(func_5012_call(), 2)
call_6480 = relay.TupleGetItem(func_5013_call(), 2)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_6488 = func_3896_call()
call_6489 = func_3896_call()
func_4162_call = mod.get_global_var('func_4162')
func_4163_call = mutated_mod.get_global_var('func_4163')
call_6497 = relay.TupleGetItem(func_4162_call(), 0)
call_6498 = relay.TupleGetItem(func_4163_call(), 0)
func_5082_call = mod.get_global_var('func_5082')
func_5084_call = mutated_mod.get_global_var('func_5084')
call_6518 = func_5082_call()
call_6519 = func_5082_call()
uop_6528 = relay.sqrt(call_6518.astype('float32')) # shape=(12, 3, 14)
uop_6530 = relay.sqrt(call_6519.astype('float32')) # shape=(12, 3, 14)
func_3950_call = mod.get_global_var('func_3950')
func_3954_call = mutated_mod.get_global_var('func_3954')
var_6534 = relay.var("var_6534", dtype = "float64", shape = (90,))#candidate|6534|(90,)|var|float64
call_6533 = relay.TupleGetItem(func_3950_call(relay.reshape(var_6534.astype('float64'), [15, 6]), relay.reshape(call_6479.astype('uint64'), [1152,]), ), 2)
call_6535 = relay.TupleGetItem(func_3954_call(relay.reshape(var_6534.astype('float64'), [15, 6]), relay.reshape(call_6479.astype('uint64'), [1152,]), ), 2)
func_6243_call = mod.get_global_var('func_6243')
func_6244_call = mutated_mod.get_global_var('func_6244')
call_6541 = relay.TupleGetItem(func_6243_call(), 0)
call_6542 = relay.TupleGetItem(func_6244_call(), 0)
output = relay.Tuple([call_6471,call_6473,call_6479,call_6488,call_6497,uop_6528,call_6533,var_6534,call_6541,])
output2 = relay.Tuple([call_6472,call_6474,call_6480,call_6489,call_6498,uop_6530,call_6535,var_6534,call_6542,])
func_6547 = relay.Function([var_6534,], output)
mod['func_6547'] = func_6547
mod = relay.transform.InferType()(mod)
mutated_mod['func_6547'] = func_6547
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6548 = relay.var("var_6548", dtype = "float64", shape = (90,))#candidate|6548|(90,)|var|float64
func_6547_call = mutated_mod.get_global_var('func_6547')
call_6549 = func_6547_call(var_6548)
output = call_6549
func_6550 = relay.Function([var_6548], output)
mutated_mod['func_6550'] = func_6550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_6583 = relay.TupleGetItem(func_4068_call(), 1)
call_6584 = relay.TupleGetItem(func_4069_call(), 1)
func_4696_call = mod.get_global_var('func_4696')
func_4700_call = mutated_mod.get_global_var('func_4700')
const_6586 = relay.const(-9, dtype = "int16")#candidate|6586|()|const|int16
const_6587 = relay.const([[-10,-4,3,-5,5,4,-2,-2,9,-4,-7,10,6,3,-7,-1,-6,-1,1,5,-8,1,-6,-6,6,-1,4,9,3,1,9,-8,-1,3,7,-5,-4,6,3,9,3,-4,-1,8,-5,5,-2,-8,-4,-2,6,9,-8,-4,-10,-10,-4,1,-9,1,-9,-7,-1,-4,5,-9,5,-5,-4,6,1,-8,-2,2,9,5,-2,-9,-9,-10,-8,7,7,-10,10,-9,-2,8,8,-7,-3,-5,7,6,8,10,4,-1,7,6,-7,-8,1,-5,6,-6,-4,-2,6,5,-5,-1,-2,4,6,-7,-4,-2,-3,-6,8,-7,-4,1,10,-3,3,-6,8,4,-9,-7,-10,-9,-7,-3,6,5,-1,-1,6,-6,10,4,1,2,-1,-2,-7,5,8,8,9,6,-2,1,-1,-7,-10,-8,10,-8,6,-3,2,6,-7,-4,8,6,-6,-9,5,-7,8,-3,-3,9,-4,-4,-4,8,7,-8,3,8,-1,6,3,-1,9,9,-9,-3,5,-9,2,-10,9,-5,-10,-2,9,8,-1,5,5,2,-4,-6,4,8,5,4,-4,8,1,-6,8,-4,-5,7,-3,-5,-5,8,8,-3,5,-7,-8,4,5,-2,6,-1,7,10,-8,8,5,3,3,-6,-5,9,10,-5,-3,-9,4,-1,-10,10,-5,-3,6,6,4,-10,-7,-4,-2,5,5,6,3,-8,-10,3,9,-8,2,8,7,6,-7,-2,-9,-6,-10,4,2,8,-4,-7,-5,-8,10,4,6,-3,10,3,4,-6,4,10,5,9,-9,10,3,2,6,3,3,6,-5,3,-8,6,10,-1,-5,2,-7,7,-4,5,2,3,-8,-1,8,2,4,2,-3,-8,-3,2,7,-2,-6,-5,7,-6,-7,-7,10,10,7,-7,-5,1,-7,8,10,-7,8,-7,-9,1,-7,-10,-8,-10,-4,-5,3,-5,-9,-6,-4,7,4,7,6,-9,4,9,-2,7,7,-3,10,-3,-2,9,-4,5,2,-3,-10,1,-2,6,-1,-7,8,1,9,-8,4,6,6,6,-3,-6,1,-9,-10,-6,9,-9,5,-5,-3,5,10,5,-3,6,2,-1,3,-8,6,-4,-9,-1,3,1,9,-5,-7,9,-5,-10,-10,2,2,6,3,-4,-3,7,3,3,-3,-2,-3,4,7,5,-6,1,-4,-7,-7,9,6,-3,5,-10,6,-1,-5,7,9,-1,8,5,1,10,3,-5,7,-9,-5,1,2,-2,-6,-1,10,10,-4,-1,6,-2,-3,1,4,-4,-8,-10,-8,-7,1,7,-10,9,-1,8,4,-10,4,8,-1,6,-9,10,-1,10,-5,-5,-4,-8,7,-6,-5,-7,-8,-8,9,-8,4,-6,7,9,2,8,8,-5,-1,5,5,-8,1,2,3,10,10,-4,-1,10,7,-3,1,2,-9,1,-1,9,-6,-1,2,8,-7,-10,7,6,-5,1,-7,1,9,1,2,3,-2,-1,-8,-8,-1,-5,-8,4,-10,-1,-7,-4,-6,-8,7,-10,-6,7,8,-8,6,9,6,7,-8,2,5,-2,1,1,1,-10,10,10,-3,-9,4,2,1,6,2,-5,-4,-7,-6,6,10,4,-1,10,-7,-4,-8,10,10,1,6,8,-2,6,5,-5,5,-7,-6,-4,-7,-3,-9,-6,-1,-10,2,6,6,2,-1,8,-6,4,-1,4,-9,5,-2,-6,8,1,-5,-4,8,-2,-2,-6,-5,-10,-1,6,-1,-7,-10,5,8,-1,-10,3,10,-8,-8,-1,-7,1,3,-9,8,5,-8,7,-6,-8,-3,6,-10,8,-1,3,7,-7,1,7,1,-7,-4,-4,5,9,-4,-3,-3,2,-7,-3,9,9,7,1,-7,6,5,4,-3,9,-9,-2,1,-8,9,7,1,-1,-9,8,-1,9,-6,7,5,-7,-8,7,-4,-10,-6,2,10,-8,6,-6,2,-4,-8,8,-6,-8,-5,-4,1,2,10,9,-7,-2,4,-9,-5,3,-3,7,-5,6,1,8,3,-1,6,-4,6,-6,-3,-7,6,-2,-2,-2,3,8,7,7,-8,2,10,-4,1,-9,5,-3,-5,-1,5,3,-9,-3,8,6,-10,-7,6,9,3,2,-1,8,1,2,-3,3,7,-8,-7,9,5,-2,-9,-8,6,-8,-8,-6,6,-6,-4,-10,-6,7,5,5,-4,-10,-5,-5,2,-1,-2,9,4,6,4,-10,-4,-8,-3,-10,-7,1,-1,-6,-4,1,-3,-5,-8,6,6,-4,2,-1,4,-5,-2,-4,5,-3,-6,-4,-9,-7,-9,-8,-8,-7,-6,-7,-10,1,9,6,-7,2,5,4,4,-10,-2,-7,-1,-1,5,-7,-8,-8,6,-10,2,6,-5,-3,10,3,-10,-2,-5,1,-9,-4,9,-6,5,-7,6,-6,4,2,-3,-5,3,5,10,-9,-4,-8,4,-7]], dtype = "int16")#candidate|6587|(1, 924)|const|int16
call_6585 = func_4696_call(relay.reshape(const_6586.astype('int16'), []), relay.reshape(const_6587.astype('int16'), [11, 12, 7]), )
call_6588 = func_4696_call(relay.reshape(const_6586.astype('int16'), []), relay.reshape(const_6587.astype('int16'), [11, 12, 7]), )
output = relay.Tuple([call_6583,call_6585,const_6586,const_6587,])
output2 = relay.Tuple([call_6584,call_6588,const_6586,const_6587,])
func_6592 = relay.Function([], output)
mod['func_6592'] = func_6592
mod = relay.transform.InferType()(mod)
output = func_6592()
func_6593 = relay.Function([], output)
mutated_mod['func_6593'] = func_6593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5626_call = mutated_mod.get_global_var('func_5626')
call_6614 = func_5625_call()
call_6615 = func_5625_call()
func_2874_call = mod.get_global_var('func_2874')
func_2877_call = mutated_mod.get_global_var('func_2877')
const_6632 = relay.const([0.196874,2.179559,4.896154,5.787221,-6.874950,6.500737,-2.298108,9.486644,3.925458,-0.577653,1.989818,4.259333,-9.719148,5.649434,-2.925197,9.139217,4.323817,-0.858087,-4.419230,-2.049085,4.813391,-0.751469,-0.835320,-9.091595,8.564868,0.387773,2.545239,-7.635293,-4.233807,5.137784,7.148663,-6.174779,9.821327,-8.275670,-4.803740,-1.193905,-0.611683,3.289904,-3.095608,-9.333612,-5.738841,-1.233847,0.494336,8.380097,-8.644976,-6.044743,4.387656,-6.015631,3.778277,-0.290629,7.530907,-8.909796,-9.313619,1.389606,2.487182,-2.977537,0.903055,7.017688,-5.486453,-3.358242,4.814567,-8.478097,0.494855,2.501896,1.507692,-0.511963,-7.416444,6.153550,-9.703679,-5.334513,-2.213043,1.248247,6.685044,-6.059379,5.250400,1.430558,-3.239409,1.972135,-4.041601,-7.851083,-5.450259,2.661532,2.296523,1.796385,0.857483,-3.971426,5.370034,6.654917,-0.466667,-7.777187,-3.841875,3.585220,0.887844,-0.445423,6.024392,-4.286255,1.061182,2.795139,-5.971304,-5.063358,-7.164431,1.041743,-7.954634,-6.109667,3.660353,-2.551892,-0.293091,-6.093282,-2.289131,-0.201548,3.016809,2.339746,-1.988195,-4.913270,-4.812898,-4.946286,5.820812,-2.773881,-1.700709,-6.836855,4.758075,0.788246,-7.703805,4.725425,-0.077369,4.189478,-6.578967,-4.573987,9.549520,7.828326,4.321956,-4.838905,-1.439871,-7.305919,9.628208,-4.584492,4.016180,2.416337,5.511028,-2.808253,-9.982150,4.807742,-7.981786,0.949596,-7.388770,0.665469,-2.381260,-3.227286,-8.675853,7.388699,-7.820423,-0.920282,7.944531,1.720281,4.676355,-3.907455,6.488347,-8.051558,3.367710,3.807377,0.493041,7.618504,-0.654526,-1.014618,-4.315843,3.484650,0.366843,-7.854299,3.159473,1.539109,2.732196,-1.013379,9.945454,-3.690295,-8.861085,6.784042,7.716432,2.036911,-7.952319,-5.115196,9.914986,7.021611,-9.277190,4.577383,-1.819502,-2.402920,-9.772819,-6.388127,1.277660,-9.539411,8.278168,4.750312,-1.264814,-0.708498,-2.703481,5.529516,-7.671410,-9.745202,-7.057446,-7.724581,-7.316507,-8.804227,2.135722,3.025473,4.529023,-0.693292,1.320878,1.981263,-5.491345,-2.867340,2.708984,-4.737282,3.694034,-7.377805,-9.011544,-2.309698,3.175083,7.424392,5.553256,6.168039,-3.341792,9.028998,-1.765487,3.825393,1.422878,5.408091,1.302557,-9.397871,7.716471,-2.527224,-9.708489,-9.563940,5.112579,-4.501343,-2.109661,-1.855316,-0.193214,-8.364433,-7.697907,5.221563,-3.842996,-2.265234,0.432626,-9.559118,8.422767,-6.635062,1.221363,8.321760,9.444278,6.740322,-4.066261,-3.976076,-5.859288,1.705760,4.771768,-4.797224,3.281996,9.200484,2.331246,8.507336,1.228974,-7.301457,7.172161,1.595031,-8.511046,-7.784352,-4.811370,5.923845,-7.594009,-5.544072,5.003995,0.141746,6.520724,9.883209,-9.091647,-3.038247,0.125340,-9.161278,-8.330559,0.961135,-5.982451,5.714441,-6.708915,0.193375,3.825073,-0.042792,-0.574656,-0.018625,7.347263,8.095521,-1.132668,5.118086,-2.581233,-1.176266,8.679982,4.518120,-1.734570,2.160317,1.397525,6.143958,-8.220067,-1.675970,9.873577,-5.081520,-4.484851,-8.998490,8.339837,-7.215234,2.949093,7.685974,-7.578874,-9.894436,9.271708,-6.521662,6.108007,-6.244793,1.879754,-6.669853,0.586680,9.658055,-6.298260,-7.146861,6.775199,-5.424584,-6.526360,-5.482071,-6.418466,0.500481,-9.860013,3.171577,8.766319,0.666976,-0.568510,0.223458,-4.539468,2.676812,-8.311238,0.676735,1.228558,-1.496481,7.210987,-7.127231,3.428144,0.877751,1.941503,3.259315,-1.952685,-7.493070,4.180479,-6.259726,-5.152211,-3.272987,-0.833093,5.144296,1.401232,8.825316,-5.062715,3.250063,0.820639,9.856734,0.428195,3.940268,3.044362,-3.398095,6.659145,-3.223020,-3.345640,-4.065802,-1.034337,-8.625909,8.304128,-6.837769,-7.436744,1.414290,3.016883,-1.784594,-1.827693,-4.986280,5.604644,-9.408703,-5.000152,9.604219,9.975883,4.740025,5.074569,-4.824634,5.720750,-7.744353,-1.572517,9.828704,-4.835105,-4.327523,2.634994,-6.824756,1.482657,4.134812,4.090136,-5.448935,-1.045049,6.038910,-0.926596,-3.873218,-7.788941,8.630340,-2.051216,-9.676520,-4.493576,9.030902,-8.627885,5.852972,-0.461672,7.245938,1.115478,6.096984,7.036203,4.455166,-8.888024,9.155644,-7.368728,0.033892,9.037387,9.533925,-3.470807,4.874069,-1.495643,-2.699588,6.953133,-4.201940,1.941062,-6.219637,-2.204701,-4.976750,5.063055,-1.988741,-0.121752,-3.249384,4.768098,-3.014262,2.972842,-8.889046,-0.104737,-8.273279,-7.495665,-2.954390,-5.005454,-5.649576,-6.419813,1.543954,-5.037555,2.817777,2.729523,-3.728236,4.222142,-8.580239,-6.452364,-6.441707,5.215796,-3.620612,0.935362,-1.949820,8.851751,5.864495,4.791667,0.077720,-0.273235,3.997276,3.383225,-5.442113,-1.583896,9.278835,-3.104472,7.088528,-3.001149,2.015250,-5.896692,-0.859576,7.355285,6.711202,-8.051145,-0.716756,2.740200,3.298164,-2.691119,4.282247,-8.346862,9.016599,-1.165440,1.601746,2.286811,-9.196784,-8.720827,0.166724,-1.913745,-0.627075,-1.080684,1.119044,-0.273073,-8.101479,6.214653,9.664223,-7.185698,-7.076584,0.332780,5.847567,-7.689773,-0.678401,-8.848658,-7.874449,-9.162033,-4.185154,-7.436912,-5.806311,-0.809199,8.126209,-8.333493,3.282269,4.599360,7.849813,9.818828,8.388129,0.218594,-4.189201,-5.857539,-9.230697,-1.176279,8.215280,5.037181,2.377070,-9.002479,1.141883,-2.660892,3.059520,-7.835089,-8.536811,9.293649,0.107789,-6.099372,6.047965,7.900635,8.051758,-6.411944,-5.814809,1.295855,9.799548,-7.102487,-4.574038,1.484285,-3.116059,1.634272,-6.682420,8.135307,2.297940,2.283218,-2.024289,-9.845923,-3.153745,-1.428925,-4.676554,2.943114,2.878072,-5.099452,-6.863512,7.089621,8.631496,6.097286,8.027777,-2.692072,-2.939047,5.098849,-4.705418,5.810912,-0.511746,1.953533,5.666721,-5.717495,-4.149663,-4.402251,9.980291,5.338155,-2.583616,-2.221234,3.667726,-1.884596,-8.919411,-7.995028,-1.031985,-9.261260,4.738623,4.418701,-5.614184,2.596661,4.527429,7.968554,8.148887,5.993045,7.587138,-0.923116,-3.854643,6.148563,-7.541155,6.195418,6.146179,-1.216649,3.032201,4.600271,3.036935,-7.997826,-4.738787,9.877080,6.529951,-9.056325,-4.931524,3.166546,7.987259,-0.594551,0.047577,-6.264058,1.900461,7.819341,1.975111,-9.648315,-1.292458,0.219931,-1.740907,-3.226381,2.495997,-2.037674,7.819440,5.048271,-4.744961,8.838832,3.096303,-7.304640,-4.301061,-8.000601,-4.255530,-7.724491,9.157822,-1.501981,6.364661,3.665820,8.607740,-6.762439,-7.947959,7.577249,4.891656,-8.360071,2.052127,7.144191,-4.895656,2.864449,-7.264953,1.570156,3.916411,3.939753,4.388114,0.328171,5.516574,4.220582,0.652856,-9.886175,7.883227,-0.011505,-4.919570,-4.607714,4.926238,2.045351,-8.532427,1.930323,-4.927584,-6.918650,-8.284068,-5.306391,5.597446,4.938771,7.798439,-9.168230,-7.950201,6.263728,-0.780512,2.245304,4.208449,-9.861131,-1.221890,5.382462,-6.683636,-9.891639,5.352722,-8.025553,-2.531418,-0.605974,-2.444886,3.876873,9.402722,9.333932,-8.799594,7.964449,0.313704,4.920107,3.832887,4.996783,-6.419400,-5.226979,-2.572104,0.194680,-9.255308,-6.194807,-1.373767,6.793362,-9.558831,9.682318,-1.807885,-1.661296,-2.044872,8.477157,-2.653127,-5.397360,-9.448842,6.535684,7.341596,7.977975,-5.857513,-2.597288,4.966834,-4.523758,-5.210703,0.202783,-7.417424,5.456050,4.251397,-2.026078,5.158546,9.585718,-3.417943,-4.935394,6.243437,9.514880,-3.907058,-9.974193,-7.932218,5.998923,-7.396893,3.616065,0.795120,-4.180506,9.341144,-1.249538,5.161769,-0.137270,-8.913110,7.143531,-9.234705,6.822939,8.219689,6.624780,-9.159204,-4.233249,3.694872,7.032819,-8.449660,7.739355,8.002901,-2.699755,0.889074,-5.918044,-7.265732,0.317213,-0.961094,5.135931,-6.574305,0.466199,9.779466,-6.883217,3.964633,0.308471,0.063669,6.254854,0.720776,8.933636,-4.350895,-2.065759,9.063736,-9.576172,5.546756,5.443903,-5.831953,-5.357335,4.753663,-0.836708,6.632941,-9.117431,-0.978819,1.722247,-4.808911,0.971531,-3.214577,0.913691,9.867827,5.787431,7.320193,6.810125,-0.013810,3.908761,-4.918194,-0.491580,-9.177263,-2.087357,2.640769,-8.280823,-8.028484,-7.412231,1.317266,-9.680403,4.282490,9.339371,9.616683,-5.711395,3.419694,7.688320,3.879506,7.265384,-8.095258,2.141999,2.219880,6.836824,3.582009,-5.994768,7.152692,2.309793,-0.578842,9.778801,4.529259,2.132395,-3.342223,-7.982573,0.780871,1.406220,4.419396,2.038648,-6.458648,-2.940378,-3.863345,-3.896223,-9.040602,6.514757,7.914121,-9.006671,-9.209179,3.633438,-9.674528,7.559431,1.028114,4.607280,0.204670,9.103073,-3.658612,4.046379,-6.833891,-2.933779,0.551973,9.102577,8.456455,-7.004597,-2.519959,-5.362353,7.992847,-5.499542,-8.000549,-6.656461,-0.693069,6.184413,8.927200,7.267131,-2.187615,-8.783394,3.821380,-2.706599,0.198358,9.523461,-4.424642,-9.746452,7.633122,-6.700010,2.795547,9.443977,-0.939402,-0.178838,5.855593,6.751521,8.745186,6.909142,-1.261589,2.546137,-3.644268,2.462311,-8.662414,6.101999,-0.604766,4.972769,-4.488082,2.485314,6.872025,-1.510218,1.659776,5.421129,-4.310091,-4.478116,-2.698408,-7.577460,-3.346988,-8.913810,-6.233460,-0.885599,1.953239,-2.708046,-2.765674,5.584961,0.941880,-4.004061,1.604646,7.047787,-5.030741,-6.702759,-9.782113,-2.860666,-8.559772,2.765600,-0.277696,3.190507,-6.433752,0.163909,4.596679,-8.292865,-2.829289,-2.283961,-7.136550,4.110747,4.587753,-1.767147,7.687561,-6.936130,8.679118,-3.213072,5.517942,3.193912,6.248556,-7.922761,0.734224,4.587786,8.938852,-4.745542,8.863550,-6.769212,5.570505,-5.520483,3.375513,2.817853,4.220609,-2.571935,5.285372,-2.637273,-7.267022,-4.404253,9.456171,-8.914110,9.220679,0.217213,-4.054455,1.570161,-0.886697,-4.157639,-8.153035,-6.212477,3.700329,-0.146451,-5.682398,7.309355,4.722978,3.259652,4.900247,9.198372,-4.812386,-7.755633,-1.404808,-2.355073,2.104784,0.994879,-6.146839,9.308320,-0.646804,4.166725,-6.908370,-7.835244,-2.638766,0.596952,7.025576,-2.648933,8.784208,-3.750091,-9.228325,-7.815932,-4.135412,4.444882,0.736976,-7.956148,-1.134062,-9.785350,5.475098,-1.441719,-3.684734,1.418981,-9.741172,4.209231,-1.607921,6.631721,9.939355,0.255335,6.367509,-8.361148,4.620146,1.630178,-2.060942,6.359720,-1.242999,4.119814,4.721898,-4.351346,-1.984978,8.338021,8.660123,8.882578,-3.017956,-5.473055,7.910482,-5.536996,-8.656440,-1.990598,5.591900,-4.334971,4.951873,7.876857,-0.853551,-8.151224,9.602923,-1.541716,2.594032,9.125664,-6.444327,5.869351,0.148229,-1.791562,3.076005,-5.192446,-4.959550,-0.928881,3.451911,-8.439389,2.457490,-3.514297,-5.358246,-3.252308,1.786104,5.921208,4.458494,8.520601,-4.680755,-6.682249,2.336887,8.471729,9.860544,4.679457,9.785938,4.909983,0.340076,9.367692,-2.364182,1.408606,-8.080453,8.037432,7.626864,-2.939309,-0.360356,-0.379778,3.235997,-4.133381,2.950708,4.630506,7.853696,-2.803091,6.902703,9.427186,0.183326,3.271478,3.226976,2.328896,8.407217,6.090084,8.275712,5.979616,3.090101,0.485605,-5.033064,0.696264,1.941934,-8.557500,9.433594,-1.705354,-2.404187,-0.527085,-3.726281,-0.202233,9.780403,-4.753529,3.777186,-0.690629,6.291462,-5.835813,-9.439907,6.113537,3.054557,-8.670639,7.391629,8.392306,-3.709749,-0.587147,9.171280,4.493362,-4.673011,6.910938,1.790184,-6.547618,-4.296101,-6.389523,-8.914868,-3.632660,3.167634,-3.469672,-0.378292,-6.213435,-4.449113,8.583382,-2.757274,-5.380678,-8.246185,-7.743597,8.246664,-7.483862,5.408839,8.873064,5.945783,5.101743,-7.201751,1.278383,5.008327,-9.392210,-8.110019,-2.726022,-6.956774,5.127922,-0.775792,-4.533716,-2.979172,3.173182,-6.092271,9.721072,8.855414,-4.745013,7.145463,-8.049259,-3.924692,-6.026757,-3.499089,7.818918,8.523524,-5.830289,-8.010176,-0.039990,2.128252,9.374781,-5.654220,9.496194,9.607146,0.665885,-8.140895,-6.880585,-6.227684,0.957019,3.243215,4.701960,-1.590422,-4.968171,8.210769,3.460354,8.759945,-5.187230,-7.935549,6.781449,5.392478,-3.057895,-1.545473,-9.160273,5.980731,6.995331,-4.458712,4.665454,-7.605211,-7.831987,-5.064897,9.053769,-6.553514,6.881438,9.019058,-6.652603,-4.785731,-3.223535,6.899585,7.226516,3.007395,0.904086,-8.584073,-0.150034,9.850446,-9.493579,-4.826970,0.508773,5.736946,5.741292,6.701642,4.862678,-2.962329,-5.797785,7.479293,-9.307093,-4.549087,-9.154079,0.868267,-2.424742,9.149571,-0.041739,-3.784925,-0.135433,0.961803,-3.409174,-5.066079,-3.804478,-0.598607,-6.169628,-3.671680,-3.187786,5.190146,1.364714,6.977903,0.118568,-1.203047,-1.853535,6.304288,-1.033455,4.075264,9.654191,6.099478,-3.445480,-8.418798,8.769579,-6.285099,5.850856,-4.394219,-7.963641,-1.289944,6.217979,3.201559,7.564790,-4.810854,7.598686,1.348769,5.681721,-4.454570,-2.792892,5.825928,-5.500395,0.601824,7.540485,-1.634057,5.779451,5.558381,-0.491477,-7.835703,6.554109,2.486346,-4.942581,0.509201,2.444009,-1.222228,-9.505900,2.242269,4.474401,-5.594826,9.521663,-5.576913,-1.362209,9.337139,-0.599579,-3.742819,-8.786306,1.692789,-0.983264,2.353843,-3.753590,5.539475,6.719771,2.380967,5.399293,7.016802,9.963083,4.793957,9.359061,-1.171658,3.593010,3.033782,-9.051183,-2.574435,8.844374,5.276448,7.592455,-7.800890,1.055365,9.313331,4.304821,3.816749,-4.413529,-9.051761,0.830383,-5.647365,-1.248598,3.515122,-9.352063,0.372253,3.249608,2.806210,-9.699865,6.917695,-2.869979,-8.183436,1.884788,-9.364546,9.282323,8.883237,0.430465,1.831885,3.251511,-9.233909], dtype = "float32")#candidate|6632|(1350,)|const|float32
call_6631 = relay.TupleGetItem(func_2874_call(relay.reshape(const_6632.astype('float32'), [9, 15, 10]), relay.reshape(const_6632.astype('float32'), [9, 15, 10]), ), 0)
call_6633 = relay.TupleGetItem(func_2877_call(relay.reshape(const_6632.astype('float32'), [9, 15, 10]), relay.reshape(const_6632.astype('float32'), [9, 15, 10]), ), 0)
uop_6638 = relay.sin(call_6631.astype('float32')) # shape=(9, 15, 10)
uop_6640 = relay.sin(call_6633.astype('float32')) # shape=(9, 15, 10)
output = relay.Tuple([call_6614,const_6632,uop_6638,])
output2 = relay.Tuple([call_6615,const_6632,uop_6640,])
func_6643 = relay.Function([], output)
mod['func_6643'] = func_6643
mod = relay.transform.InferType()(mod)
mutated_mod['func_6643'] = func_6643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mutated_mod.get_global_var('func_6643')
call_6644 = func_6643_call()
output = call_6644
func_6645 = relay.Function([], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6711 = relay.const([[[-2],[10],[-5],[5],[5],[5],[8],[-3],[-7],[-9],[1],[-10],[6],[3]],[[2],[-7],[5],[4],[-6],[-3],[4],[4],[10],[-1],[6],[-7],[5],[-2]],[[-7],[5],[1],[6],[7],[-5],[8],[6],[8],[7],[7],[4],[-10],[-2]],[[10],[6],[-7],[7],[-2],[5],[4],[4],[9],[-7],[10],[-6],[2],[2]],[[-3],[-6],[6],[-8],[-4],[-4],[-9],[-8],[8],[4],[-4],[6],[-5],[-10]],[[-4],[-8],[9],[-8],[8],[10],[3],[8],[3],[-3],[-2],[2],[-10],[-9]],[[-1],[-9],[-3],[10],[10],[7],[-5],[10],[2],[-10],[-6],[8],[3],[-3]],[[8],[-5],[10],[6],[2],[-7],[5],[10],[2],[-10],[8],[1],[-4],[-3]],[[1],[-8],[-7],[-10],[1],[-4],[1],[5],[5],[7],[-5],[-4],[-6],[8]],[[-4],[-7],[-6],[-3],[-9],[2],[8],[-3],[7],[-4],[3],[-2],[8],[-3]],[[8],[4],[-2],[-8],[7],[-1],[-6],[-8],[-1],[5],[9],[10],[3],[-2]],[[5],[7],[5],[-7],[4],[5],[-9],[-10],[3],[1],[-7],[10],[8],[-7]],[[2],[-3],[-5],[2],[4],[8],[7],[9],[-2],[-10],[7],[9],[-10],[1]],[[8],[2],[-9],[9],[-7],[-3],[10],[-9],[5],[-2],[-9],[1],[6],[1]]], dtype = "uint16")#candidate|6711|(14, 14, 1)|const|uint16
const_6712 = relay.const([[[-5,-9,-8,-3,-10,6,1,5,3,-2],[-8,-7,-8,-9,-8,-10,-5,1,-7,10],[5,3,4,-10,9,-1,-4,7,1,10],[5,4,6,5,10,-3,5,-4,3,7],[-5,-10,-9,8,3,9,7,7,-9,-7],[2,-5,-5,8,-3,1,-5,7,-5,4],[-5,3,-8,-5,7,-7,3,7,-1,5],[2,-1,6,3,-3,9,-1,7,-7,6],[6,4,-5,7,-8,7,-8,-8,-6,-6],[-7,-6,7,8,10,7,-5,-3,-2,6],[3,-1,-4,7,-10,-1,-8,-5,-4,1],[5,8,-1,-2,-3,2,-2,9,1,-5],[9,-6,-5,-3,4,-1,-4,-2,-1,-5],[-5,-10,-1,2,-5,3,-5,10,-1,-8]],[[-7,-7,7,-5,6,-3,-8,-5,-2,-2],[-7,10,3,-3,2,-1,-8,1,8,4],[-7,-2,-9,-5,7,9,-2,8,-6,-2],[-10,-9,-1,-6,8,2,6,-10,2,-8],[-3,-5,-4,2,1,2,7,10,4,9],[-5,-7,7,-7,-3,10,-4,2,-5,9],[8,-5,-3,-3,2,-8,2,-7,-3,8],[1,-3,-10,-2,9,10,5,10,-2,-4],[4,-1,-1,3,-3,1,8,9,-9,2],[-2,-3,8,4,6,-4,4,-7,4,-1],[3,-10,-6,-9,-10,2,5,-1,-9,-5],[-7,-7,6,7,8,-6,-8,3,7,-8],[5,3,5,3,10,-1,8,-9,-4,4],[-4,2,-9,9,-9,7,7,5,3,-8]],[[-7,4,-8,8,1,3,-2,-1,-2,-1],[7,6,-7,8,1,4,6,3,-1,6],[-5,-9,-4,10,-1,8,10,-2,6,-6],[7,-7,8,-6,3,2,1,-4,4,-2],[6,2,5,-2,5,10,-8,6,-8,-6],[6,-10,-3,-9,-10,-1,10,-2,-7,-6],[2,4,-6,7,-3,-7,-5,6,-1,3],[8,8,7,-3,-6,-5,-8,10,9,7],[2,-3,-9,3,5,-1,-1,-1,3,-3],[4,9,8,5,9,-3,6,-8,-4,6],[10,-2,-8,-9,6,2,-1,1,2,-7],[8,4,6,8,4,1,1,6,6,-10],[9,-10,3,-10,-9,-6,6,10,1,-6],[-2,-10,10,-4,-3,-7,-8,-3,-10,8]],[[9,-6,-3,9,-6,10,1,3,-7,-10],[-1,3,5,2,8,-7,-3,3,1,1],[-8,5,2,3,-3,2,-9,5,4,1],[7,-10,-3,6,7,-1,-8,-6,-4,-2],[1,5,2,6,-9,-7,-9,7,-1,7],[-10,-5,-7,-9,-10,-8,-6,3,-2,5],[7,8,-10,-7,-7,3,3,4,-10,10],[5,-1,10,-10,-2,-6,8,5,8,-10],[-4,-10,10,-6,-8,-10,-4,-5,-6,1],[-1,-9,10,6,-3,2,-7,6,-8,-8],[1,-9,-9,-1,9,-5,8,9,5,7],[2,-7,4,6,8,-6,2,-5,-8,-9],[10,-9,-7,8,6,2,-7,-4,-4,10],[-6,2,2,2,4,8,5,-4,-10,4]],[[10,-1,-5,-7,-7,1,-3,-3,2,6],[-9,2,6,6,-8,9,6,-6,-4,10],[-10,-5,5,2,5,5,-4,8,3,-3],[4,-1,-1,1,-10,7,3,-6,1,-6],[-6,2,8,-10,-6,1,7,2,9,-5],[4,2,5,-6,8,5,-4,3,-9,-10],[8,-6,-3,4,2,2,1,-3,-4,3],[2,-7,4,-6,-5,-9,10,-9,-4,5],[-4,1,-5,-10,-3,2,-10,10,8,-1],[4,7,5,-7,1,-4,2,-8,10,-5],[-2,6,3,10,-4,4,10,2,-7,8],[-2,3,-10,9,1,-10,-1,9,-4,5],[9,-8,1,8,-8,6,-1,-3,1,10],[8,-9,8,-2,6,-10,7,7,7,-7]],[[-6,-6,3,-7,-3,-8,-6,-9,6,9],[-1,8,9,7,5,-3,-9,7,10,8],[-2,6,5,4,-9,3,4,-7,9,8],[-9,4,-2,10,6,7,4,7,3,1],[4,1,5,10,-5,9,-9,-2,5,-3],[9,10,5,5,9,-9,9,-1,-1,10],[7,-10,4,7,1,4,-2,-5,2,-3],[5,-3,4,-3,-3,3,-4,-8,2,-10],[7,-4,8,4,-1,-10,2,3,5,3],[10,-2,8,3,-7,-4,10,-3,-1,-10],[-5,9,4,-5,9,-9,-3,-3,10,10],[2,-2,-6,-1,-2,-7,9,-6,1,2],[-9,-9,3,-5,10,10,1,-2,-7,-4],[-4,-7,1,6,7,2,-10,-10,4,5]],[[1,8,9,3,-3,-6,9,9,-9,4],[4,1,8,8,7,10,9,1,7,4],[10,8,7,3,-4,-3,-2,4,-8,-6],[6,-2,-1,4,9,-10,10,-2,5,5],[2,-2,2,8,8,4,9,10,-1,10],[4,10,-7,-3,8,6,5,6,-1,7],[6,7,9,7,-4,1,6,4,-6,8],[4,-5,9,6,4,3,-7,5,-10,8],[-9,3,-4,9,-3,-5,-10,-6,2,10],[5,5,-6,10,5,1,8,-9,3,4],[8,3,-10,8,-10,5,4,7,-2,-7],[4,-1,3,5,-10,4,-8,6,5,-9],[4,8,4,9,2,-3,7,-9,3,-6],[4,-1,-6,-10,10,-6,3,-4,1,7]],[[3,-2,-3,1,-6,9,7,-4,-6,6],[4,-10,-7,-8,-10,-4,4,-3,8,10],[-1,7,8,2,6,10,1,-8,6,9],[-10,1,10,10,-8,-3,1,6,1,-3],[-8,-6,-3,-7,2,-7,8,8,-1,-5],[1,7,-10,-1,-3,-8,5,9,-10,-7],[2,-7,-1,8,3,3,3,-6,-5,6],[9,-8,-9,2,-3,2,-2,-8,3,-9],[1,-10,1,9,-5,3,-8,10,-8,-7],[-1,8,5,10,-4,-4,-10,7,-2,-7],[-1,1,-1,-9,3,-2,4,-2,6,6],[-1,-2,7,-2,10,-6,-10,-2,-9,-2],[6,9,-1,-8,-2,-8,-5,4,4,10],[5,-4,-4,10,9,6,-3,7,5,-5]],[[-2,-10,7,-10,1,-4,-6,5,-7,3],[-4,-3,-3,5,8,7,-2,8,2,-2],[-5,-1,-5,3,9,9,-7,2,-7,-10],[-6,-4,5,-10,9,1,-8,-7,7,6],[9,1,2,-8,2,-3,-6,-9,-10,-9],[2,-4,-2,-3,2,7,9,-7,-3,1],[4,6,-2,2,-5,-2,3,-5,-9,-6],[-2,-2,10,3,6,-9,-7,-2,-9,4],[7,10,3,7,-6,3,-3,-8,-4,-8],[-6,-3,-1,3,-1,-5,4,-10,-1,-9],[9,4,6,-7,-6,5,2,-4,-2,5],[5,-4,5,7,1,2,9,2,-1,-10],[-3,-8,2,8,-6,-9,-4,1,-7,5],[4,9,-5,-9,-1,-5,3,-9,-3,8]],[[1,2,10,-5,2,6,9,-7,6,3],[6,-2,-1,-1,8,-8,7,-6,-3,-6],[3,9,9,6,-6,3,-9,1,7,-8],[3,6,6,-1,-5,4,-10,9,2,5],[6,-10,-6,-9,-4,8,1,-1,7,5],[-8,-9,-1,8,-4,1,-4,9,3,10],[2,-9,1,-1,-4,10,3,-10,10,10],[-4,5,6,-5,1,10,-5,-8,1,-5],[-4,-4,-6,5,-6,-9,-10,8,8,4],[-1,3,-3,2,-10,8,-6,5,9,-8],[-7,-7,3,2,9,3,2,7,10,-9],[8,6,-10,-8,3,5,-4,8,8,-3],[7,6,-5,-5,2,-5,1,-6,4,-3],[-1,8,3,-5,5,-5,-5,2,-5,2]],[[10,10,1,-4,4,-2,6,-10,-8,-7],[4,-7,-6,-8,-5,10,10,-9,-10,5],[-10,6,-9,-4,-3,9,-6,8,-5,-5],[-7,-8,-7,-7,9,8,3,5,2,10],[-4,-5,-5,-2,-9,1,-4,-2,-5,5],[-5,3,-8,-9,-10,8,-7,-4,-5,-5],[5,-10,-6,-9,3,4,8,-5,6,1],[-4,9,1,6,-10,-2,-8,4,-5,4],[9,-8,-5,-5,1,-6,4,-10,9,-5],[-8,1,-9,1,-8,-4,5,5,-8,-3],[-6,-8,4,-9,6,1,-9,2,-7,-4],[10,-3,-1,-4,-9,-2,6,7,-7,-5],[10,-9,-8,7,-5,-2,8,-9,6,-1],[-2,9,-10,10,-5,-2,-2,-4,-1,-8]],[[3,-1,-7,-1,4,7,-3,-6,7,2],[-2,4,5,-4,10,-3,2,-3,2,4],[-8,-4,9,5,5,-7,4,-2,-1,5],[8,4,2,1,-1,-4,5,-9,-7,10],[4,10,9,8,10,-1,3,-10,-1,1],[-7,-3,2,-7,-10,2,6,-3,3,5],[7,2,1,5,5,8,-2,4,-4,-4],[2,10,7,3,7,5,-5,-5,1,8],[7,-9,8,-2,8,9,-9,8,-4,-8],[-10,-6,2,-1,1,-10,-5,7,4,-8],[-3,-2,5,10,2,4,-1,-7,2,-5],[-7,-3,-3,8,8,-10,2,-5,2,8],[-1,6,-5,-4,-8,1,-1,-10,5,-2],[1,-5,-3,-1,6,-1,-4,-1,-9,-5]],[[4,-4,2,-9,-9,9,-4,4,5,-2],[-5,-9,9,5,5,-7,-7,3,-7,8],[5,8,4,-7,-5,1,2,-8,-10,-1],[4,1,2,-5,-6,5,-8,1,4,2],[-6,1,1,-1,4,-3,3,-4,-9,4],[-9,7,1,-1,7,-4,6,-3,5,-7],[9,9,-7,-8,1,-2,-10,-10,-8,-4],[6,-9,5,9,-9,1,8,9,7,2],[9,10,2,8,3,-6,-2,-1,-9,9],[9,-6,-1,4,2,6,7,-1,-6,-10],[3,-1,-3,3,5,1,-1,-2,-2,10],[10,7,2,8,-7,10,-4,-6,-3,10],[3,3,6,8,-10,4,-6,1,9,9],[-8,7,-10,-1,-5,3,10,-2,9,-6]],[[8,-1,3,6,3,-9,4,5,10,-7],[6,-3,-3,-3,-4,-3,1,1,-8,-7],[10,-2,-3,-6,-2,9,2,4,-6,-8],[-8,-5,5,-6,-10,-3,-10,-5,-1,-7],[6,1,-10,5,-2,8,-6,-10,8,-5],[8,1,1,10,-8,5,4,4,-10,2],[2,1,-5,-8,-8,3,10,-3,-3,5],[3,7,-5,-3,-8,7,5,9,-9,-2],[1,-3,3,-2,-3,8,-6,-3,-6,5],[1,5,10,-5,2,-5,5,3,-8,-6],[1,-4,9,-9,-4,-10,-6,1,10,4],[3,4,-9,-10,4,-7,10,-4,-1,-5],[-7,1,9,-7,8,-10,3,1,-2,1],[8,3,-1,8,-1,-8,7,2,-1,-2]]], dtype = "uint16")#candidate|6712|(14, 14, 10)|const|uint16
bop_6713 = relay.maximum(const_6711.astype('uint16'), const_6712.astype('uint16')) # shape=(14, 14, 10)
output = bop_6713
output2 = bop_6713
func_6717 = relay.Function([], output)
mod['func_6717'] = func_6717
mod = relay.transform.InferType()(mod)
mutated_mod['func_6717'] = func_6717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6717_call = mutated_mod.get_global_var('func_6717')
call_6718 = func_6717_call()
output = call_6718
func_6719 = relay.Function([], output)
mutated_mod['func_6719'] = func_6719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6717_call = mod.get_global_var('func_6717')
func_6719_call = mutated_mod.get_global_var('func_6719')
call_6776 = func_6717_call()
call_6777 = func_6717_call()
uop_6783 = relay.atan(call_6776.astype('float64')) # shape=(14, 14, 10)
uop_6785 = relay.atan(call_6777.astype('float64')) # shape=(14, 14, 10)
output = relay.Tuple([uop_6783,])
output2 = relay.Tuple([uop_6785,])
func_6786 = relay.Function([], output)
mod['func_6786'] = func_6786
mod = relay.transform.InferType()(mod)
mutated_mod['func_6786'] = func_6786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6786_call = mutated_mod.get_global_var('func_6786')
call_6787 = func_6786_call()
output = call_6787
func_6788 = relay.Function([], output)
mutated_mod['func_6788'] = func_6788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5927_call = mod.get_global_var('func_5927')
func_5928_call = mutated_mod.get_global_var('func_5928')
call_6818 = relay.TupleGetItem(func_5927_call(), 0)
call_6819 = relay.TupleGetItem(func_5928_call(), 0)
output = relay.Tuple([call_6818,])
output2 = relay.Tuple([call_6819,])
func_6838 = relay.Function([], output)
mod['func_6838'] = func_6838
mod = relay.transform.InferType()(mod)
mutated_mod['func_6838'] = func_6838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mutated_mod.get_global_var('func_6838')
call_6839 = func_6838_call()
output = call_6839
func_6840 = relay.Function([], output)
mutated_mod['func_6840'] = func_6840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3314_call = mod.get_global_var('func_3314')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_6876 = relay.TupleGetItem(func_3314_call(), 1)
call_6877 = relay.TupleGetItem(func_3316_call(), 1)
func_758_call = mod.get_global_var('func_758')
func_762_call = mutated_mod.get_global_var('func_762')
var_6884 = relay.var("var_6884", dtype = "float64", shape = (924,))#candidate|6884|(924,)|var|float64
call_6883 = relay.TupleGetItem(func_758_call(relay.reshape(var_6884.astype('float64'), [14, 11, 6]), relay.reshape(var_6884.astype('float64'), [14, 11, 6]), ), 0)
call_6885 = relay.TupleGetItem(func_762_call(relay.reshape(var_6884.astype('float64'), [14, 11, 6]), relay.reshape(var_6884.astype('float64'), [14, 11, 6]), ), 0)
output = relay.Tuple([call_6876,call_6883,var_6884,])
output2 = relay.Tuple([call_6877,call_6885,var_6884,])
func_6895 = relay.Function([var_6884,], output)
mod['func_6895'] = func_6895
mod = relay.transform.InferType()(mod)
var_6896 = relay.var("var_6896", dtype = "float64", shape = (924,))#candidate|6896|(924,)|var|float64
output = func_6895(var_6896)
func_6897 = relay.Function([var_6896], output)
mutated_mod['func_6897'] = func_6897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6309_call = mod.get_global_var('func_6309')
func_6310_call = mutated_mod.get_global_var('func_6310')
call_6928 = func_6309_call()
call_6929 = func_6309_call()
output = call_6928
output2 = call_6929
func_6933 = relay.Function([], output)
mod['func_6933'] = func_6933
mod = relay.transform.InferType()(mod)
output = func_6933()
func_6934 = relay.Function([], output)
mutated_mod['func_6934'] = func_6934
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7011 = relay.var("var_7011", dtype = "float32", shape = (9, 11, 2))#candidate|7011|(9, 11, 2)|var|float32
var_7012 = relay.var("var_7012", dtype = "float32", shape = (9, 11, 2))#candidate|7012|(9, 11, 2)|var|float32
bop_7013 = relay.floor_mod(var_7011.astype('float32'), relay.reshape(var_7012.astype('float32'), relay.shape_of(var_7011))) # shape=(9, 11, 2)
output = bop_7013
output2 = bop_7013
func_7039 = relay.Function([var_7011,var_7012,], output)
mod['func_7039'] = func_7039
mod = relay.transform.InferType()(mod)
var_7040 = relay.var("var_7040", dtype = "float32", shape = (9, 11, 2))#candidate|7040|(9, 11, 2)|var|float32
var_7041 = relay.var("var_7041", dtype = "float32", shape = (9, 11, 2))#candidate|7041|(9, 11, 2)|var|float32
output = func_7039(var_7040,var_7041,)
func_7042 = relay.Function([var_7040,var_7041,], output)
mutated_mod['func_7042'] = func_7042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5626_call = mutated_mod.get_global_var('func_5626')
call_7044 = func_5625_call()
call_7045 = func_5625_call()
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_7056 = func_5583_call()
call_7057 = func_5583_call()
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_7059 = relay.TupleGetItem(func_3130_call(), 0)
call_7060 = relay.TupleGetItem(func_3131_call(), 0)
uop_7086 = relay.log10(call_7056.astype('float32')) # shape=(8, 15, 4)
uop_7088 = relay.log10(call_7057.astype('float32')) # shape=(8, 15, 4)
func_3573_call = mod.get_global_var('func_3573')
func_3575_call = mutated_mod.get_global_var('func_3575')
var_7123 = relay.var("var_7123", dtype = "float64", shape = (1, 924))#candidate|7123|(1, 924)|var|float64
call_7122 = relay.TupleGetItem(func_3573_call(relay.reshape(var_7123.astype('float64'), [924,])), 1)
call_7124 = relay.TupleGetItem(func_3575_call(relay.reshape(var_7123.astype('float64'), [924,])), 1)
output = relay.Tuple([call_7044,call_7059,uop_7086,call_7122,var_7123,])
output2 = relay.Tuple([call_7045,call_7060,uop_7088,call_7124,var_7123,])
func_7125 = relay.Function([var_7123,], output)
mod['func_7125'] = func_7125
mod = relay.transform.InferType()(mod)
mutated_mod['func_7125'] = func_7125
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7126 = relay.var("var_7126", dtype = "float64", shape = (1, 924))#candidate|7126|(1, 924)|var|float64
func_7125_call = mutated_mod.get_global_var('func_7125')
call_7127 = func_7125_call(var_7126)
output = call_7127
func_7128 = relay.Function([var_7126], output)
mutated_mod['func_7128'] = func_7128
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7134 = relay.var("var_7134", dtype = "uint8", shape = (13, 4, 14))#candidate|7134|(13, 4, 14)|var|uint8
var_7135 = relay.var("var_7135", dtype = "uint8", shape = (13, 4, 14))#candidate|7135|(13, 4, 14)|var|uint8
bop_7136 = relay.maximum(var_7134.astype('uint8'), relay.reshape(var_7135.astype('uint8'), relay.shape_of(var_7134))) # shape=(13, 4, 14)
output = relay.Tuple([bop_7136,])
output2 = relay.Tuple([bop_7136,])
func_7141 = relay.Function([var_7134,var_7135,], output)
mod['func_7141'] = func_7141
mod = relay.transform.InferType()(mod)
var_7142 = relay.var("var_7142", dtype = "uint8", shape = (13, 4, 14))#candidate|7142|(13, 4, 14)|var|uint8
var_7143 = relay.var("var_7143", dtype = "uint8", shape = (13, 4, 14))#candidate|7143|(13, 4, 14)|var|uint8
output = func_7141(var_7142,var_7143,)
func_7144 = relay.Function([var_7142,var_7143,], output)
mutated_mod['func_7144'] = func_7144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3314_call = mod.get_global_var('func_3314')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_7174 = relay.TupleGetItem(func_3314_call(), 1)
call_7175 = relay.TupleGetItem(func_3316_call(), 1)
func_5042_call = mod.get_global_var('func_5042')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_7194 = relay.TupleGetItem(func_5042_call(), 0)
call_7195 = relay.TupleGetItem(func_5044_call(), 0)
func_4275_call = mod.get_global_var('func_4275')
func_4280_call = mutated_mod.get_global_var('func_4280')
const_7208 = relay.const([False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,True], dtype = "bool")#candidate|7208|(1200,)|const|bool
const_7209 = relay.const([False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False], dtype = "bool")#candidate|7209|(336,)|const|bool
var_7210 = relay.var("var_7210", dtype = "bool", shape = (672,))#candidate|7210|(672,)|var|bool
call_7207 = relay.TupleGetItem(func_4275_call(relay.reshape(const_7208.astype('bool'), [16, 5, 15]), relay.reshape(const_7209.astype('bool'), [336,]), relay.reshape(var_7210.astype('bool'), [56, 12]), ), 3)
call_7211 = relay.TupleGetItem(func_4280_call(relay.reshape(const_7208.astype('bool'), [16, 5, 15]), relay.reshape(const_7209.astype('bool'), [336,]), relay.reshape(var_7210.astype('bool'), [56, 12]), ), 3)
func_7141_call = mod.get_global_var('func_7141')
func_7144_call = mutated_mod.get_global_var('func_7144')
var_7220 = relay.var("var_7220", dtype = "uint8", shape = (728,))#candidate|7220|(728,)|var|uint8
call_7219 = relay.TupleGetItem(func_7141_call(relay.reshape(var_7220.astype('uint8'), [13, 4, 14]), relay.reshape(var_7220.astype('uint8'), [13, 4, 14]), ), 0)
call_7221 = relay.TupleGetItem(func_7144_call(relay.reshape(var_7220.astype('uint8'), [13, 4, 14]), relay.reshape(var_7220.astype('uint8'), [13, 4, 14]), ), 0)
output = relay.Tuple([call_7174,call_7194,call_7207,const_7208,const_7209,var_7210,call_7219,var_7220,])
output2 = relay.Tuple([call_7175,call_7195,call_7211,const_7208,const_7209,var_7210,call_7221,var_7220,])
func_7258 = relay.Function([var_7210,var_7220,], output)
mod['func_7258'] = func_7258
mod = relay.transform.InferType()(mod)
mutated_mod['func_7258'] = func_7258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7258_call = mutated_mod.get_global_var('func_7258')
var_7260 = relay.var("var_7260", dtype = "bool", shape = (672,))#candidate|7260|(672,)|var|bool
var_7261 = relay.var("var_7261", dtype = "uint8", shape = (728,))#candidate|7261|(728,)|var|uint8
call_7259 = func_7258_call(var_7260,var_7261,)
output = call_7259
func_7262 = relay.Function([var_7260,var_7261,], output)
mutated_mod['func_7262'] = func_7262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4197_call = mod.get_global_var('func_4197')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_7273 = func_4197_call()
call_7274 = func_4197_call()
output = call_7273
output2 = call_7274
func_7279 = relay.Function([], output)
mod['func_7279'] = func_7279
mod = relay.transform.InferType()(mod)
output = func_7279()
func_7280 = relay.Function([], output)
mutated_mod['func_7280'] = func_7280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6786_call = mod.get_global_var('func_6786')
func_6788_call = mutated_mod.get_global_var('func_6788')
call_7322 = relay.TupleGetItem(func_6786_call(), 0)
call_7323 = relay.TupleGetItem(func_6788_call(), 0)
func_5768_call = mod.get_global_var('func_5768')
func_5770_call = mutated_mod.get_global_var('func_5770')
call_7324 = func_5768_call()
call_7325 = func_5768_call()
func_4788_call = mod.get_global_var('func_4788')
func_4790_call = mutated_mod.get_global_var('func_4790')
var_7346 = relay.var("var_7346", dtype = "bool", shape = (1200, 1))#candidate|7346|(1200, 1)|var|bool
call_7345 = func_4788_call(relay.reshape(var_7346.astype('bool'), [16, 5, 15]))
call_7347 = func_4788_call(relay.reshape(var_7346.astype('bool'), [16, 5, 15]))
func_7141_call = mod.get_global_var('func_7141')
func_7144_call = mutated_mod.get_global_var('func_7144')
const_7352 = relay.const([1,4,-8,-5,-4,2,10,8,-4,1,7,-3,4,-8,-10,-10,3,-8,2,-9,-4,4,6,-2,-2,-4,5,-6,3,-5,-10,-4,9,-4,-5,-9,-6,3,-6,4,-1,7,-10,-4,-6,4,6,-1,-9,-7,-9,-5,9,7,-6,3,3,-3,4,4,8,8,-7,10,3,2,6,-7,9,2,8,3,7,4,5,3,-9,7,9,4,9,-4,-5,-3,6,10,-3,5,8,1,-1,-7,5,-4,3,8,6,-8,4,7,-7,2,-9,9,-8,3,7,8,5,-6,-4,10,-6,-10,2,-10,2,10,-1,-3,1,8,5,10,2,8,-2,-3,-9,-9,-10,-9,-3,8,-7,-2,-4,-8,10,8,-6,7,5,6,-5,-4,-4,-1,-1,10,7,-8,-6,-9,6,8,4,-2,9,2,5,-1,8,-7,-9,8,-10,-9,5,-3,-7,-5,-8,1,-6,-1,10,9,6,-6,-4,-2,-1,9,1,8,-2,-1,1,8,-7,-8,3,-5,-5,3,-5,4,-8,-1,4,6,-4,8,7,3,-9,10,-10,10,-6,-5,-9,-9,1,-5,1,2,-6,-9,10,-8,-2,-10,5,-8,-4,2,-1,2,2,6,9,-7,2,-2,9,-1,10,3,-1,6,5,9,-10,-7,-10,-4,-3,-6,8,-7,-9,7,-8,-5,-3,-4,-1,-4,6,3,-4,-9,-1,-2,-4,-5,-5,-2,-7,4,2,-10,-1,-5,-6,6,-9,-9,-9,-9,-9,-6,9,9,-9,-5,1,5,10,2,10,7,3,10,-6,5,-3,10,-2,-7,-4,-1,8,8,8,7,7,9,-2,4,-8,-3,-1,-5,6,4,-4,4,3,-3,3,8,6,2,6,5,-6,-5,5,-1,-1,10,2,-9,-7,7,-2,2,2,-5,-1,-2,-1,5,8,5,-1,-7,9,9,10,-8,10,-10,7,1,-8,-4,-4,4,-4,-3,6,-7,8,2,9,8,-1,2,-6,5,-9,-2,9,5,7,-8,10,7,-1,-3,1,2,2,10,-8,-3,-4,-10,-2,-6,-2,1,10,-7,-9,3,-4,9,-10,7,4,7,-4,2,-9,-5,5,-5,6,-5,-4,2,-5,7,2,5,3,-7,-6,-5,7,10,-7,-6,6,-5,-4,-10,10,4,3,-9,1,5,4,4,9,-5,8,-9,-7,-5,-1,-9,4,4,-3,6,-10,-3,1,8,-1,8,6,-4,-2,-1,-7,6,4,-1,-7,-2,5,9,-3,8,10,5,-3,-9,9,-8,2,8,-7,6,-3,9,6,-6,7,-4,1,-4,-8,9,-3,-2,4,3,-8,-3,7,-10,2,-1,1,-7,-5,-7,4,-10,5,-3,3,-10,5,3,7,-3,3,-9,9,9,9,-7,-3,1,1,7,-2,-7,10,6,-5,-6,3,3,1,6,-7,2,-1,8,-9,-6,-1,7,-4,9,-4,-8,-10,8,4,-9,8,10,6,-1,-4,7,1,9,7,-7,-4,-7,-9,-4,-3,-3,-4,-10,3,-7,-10,6,-6,-1,4,-5,4,-1,-9,3,7,2,-10,-4,-6,2,5,1,3,-6,1,-3,3,7,8,3,7,9,-10,10,3,-5,-2,-10,10,1,-7,-4,10,-10,1,-6,-9,-6,7,6,-10,10,9,6,-6,-9,-3,3,4,4,9,6,4,-8,7,-2,-6,6,4,3,1,5,4,-9,-1,6,4,9,-1,10,-10,-5,-7,-2,-3,3,8,9,-5,-2,3,8,9,7,4,-8,-4,-3,-3,3,3,-1,-3,-2,-9,7,-2,1,-10,-1,-6,1,3,-10,-10,-4,9,1,-8,-10,-9,10,2,5,8,8,-7,5,-2,6,-9,2,-8,10,8,-2,9,-10,-1,-2,-3,4,-9,1,3,-1,10,10,8,1,-2,-5,-2,1,-2,-2,-3,-8,-5,-4], dtype = "uint8")#candidate|7352|(728,)|const|uint8
call_7351 = relay.TupleGetItem(func_7141_call(relay.reshape(const_7352.astype('uint8'), [13, 4, 14]), relay.reshape(const_7352.astype('uint8'), [13, 4, 14]), ), 0)
call_7353 = relay.TupleGetItem(func_7144_call(relay.reshape(const_7352.astype('uint8'), [13, 4, 14]), relay.reshape(const_7352.astype('uint8'), [13, 4, 14]), ), 0)
output = relay.Tuple([call_7322,call_7324,call_7345,var_7346,call_7351,const_7352,])
output2 = relay.Tuple([call_7323,call_7325,call_7347,var_7346,call_7353,const_7352,])
func_7369 = relay.Function([var_7346,], output)
mod['func_7369'] = func_7369
mod = relay.transform.InferType()(mod)
mutated_mod['func_7369'] = func_7369
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7370 = relay.var("var_7370", dtype = "bool", shape = (1200, 1))#candidate|7370|(1200, 1)|var|bool
func_7369_call = mutated_mod.get_global_var('func_7369')
call_7371 = func_7369_call(var_7370)
output = call_7371
func_7372 = relay.Function([var_7370], output)
mutated_mod['func_7372'] = func_7372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_7420 = func_3759_call()
call_7421 = func_3759_call()
output = relay.Tuple([call_7420,])
output2 = relay.Tuple([call_7421,])
func_7430 = relay.Function([], output)
mod['func_7430'] = func_7430
mod = relay.transform.InferType()(mod)
output = func_7430()
func_7431 = relay.Function([], output)
mutated_mod['func_7431'] = func_7431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6243_call = mod.get_global_var('func_6243')
func_6244_call = mutated_mod.get_global_var('func_6244')
call_7456 = relay.TupleGetItem(func_6243_call(), 0)
call_7457 = relay.TupleGetItem(func_6244_call(), 0)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_7476 = func_6126_call()
call_7477 = func_6126_call()
output = relay.Tuple([call_7456,call_7476,])
output2 = relay.Tuple([call_7457,call_7477,])
func_7482 = relay.Function([], output)
mod['func_7482'] = func_7482
mod = relay.transform.InferType()(mod)
mutated_mod['func_7482'] = func_7482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7482_call = mutated_mod.get_global_var('func_7482')
call_7483 = func_7482_call()
output = call_7483
func_7484 = relay.Function([], output)
mutated_mod['func_7484'] = func_7484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6786_call = mod.get_global_var('func_6786')
func_6788_call = mutated_mod.get_global_var('func_6788')
call_7544 = relay.TupleGetItem(func_6786_call(), 0)
call_7545 = relay.TupleGetItem(func_6788_call(), 0)
func_4743_call = mod.get_global_var('func_4743')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_7562 = relay.TupleGetItem(func_4743_call(), 0)
call_7563 = relay.TupleGetItem(func_4745_call(), 0)
uop_7583 = relay.sqrt(call_7544.astype('float32')) # shape=(14, 14, 10)
uop_7585 = relay.sqrt(call_7545.astype('float32')) # shape=(14, 14, 10)
uop_7586 = relay.atanh(uop_7583.astype('float64')) # shape=(14, 14, 10)
uop_7588 = relay.atanh(uop_7585.astype('float64')) # shape=(14, 14, 10)
output = relay.Tuple([call_7562,uop_7586,])
output2 = relay.Tuple([call_7563,uop_7588,])
func_7596 = relay.Function([], output)
mod['func_7596'] = func_7596
mod = relay.transform.InferType()(mod)
output = func_7596()
func_7597 = relay.Function([], output)
mutated_mod['func_7597'] = func_7597
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7618 = relay.const([[[9.024463,-0.779105,8.710243,6.514366,9.576516,6.936820,0.118949,6.478918,8.905528,-2.229948,6.537685,-7.404555],[-8.182304,9.645375,9.782763,-8.226064,-4.453405,-4.229690,-4.759662,0.547244,4.002029,-4.032039,-6.166920,-1.403540],[-6.044550,-4.379236,9.907258,-1.336347,0.373522,9.953438,-6.143682,4.174243,-7.294587,-0.234258,0.653293,-9.048988],[-9.171084,0.181323,-8.977747,0.377825,5.500466,4.619704,-6.710250,-3.672199,1.676579,5.778568,-9.788064,-7.564983]],[[-8.665226,3.502721,-4.017685,-0.262970,-7.792068,0.452161,4.713310,8.854910,-0.335632,-3.491421,0.627082,8.712146],[-2.795861,-2.929446,5.208811,9.022774,-4.636119,-2.423232,-5.479634,6.726509,-7.583527,-2.601249,9.479778,-4.016323],[-9.521770,4.889977,-8.801741,-8.563997,6.987458,3.863369,8.945191,-7.356508,1.725137,-8.112610,3.861428,2.326960],[-9.948352,-4.200512,3.106972,-2.055671,4.421848,0.618102,-3.460137,-9.321965,9.438429,-8.375531,-7.010468,-7.958731]],[[0.293843,8.377846,-8.503623,6.147613,-5.923332,1.864883,-0.270072,3.287525,6.383862,3.032428,-3.820615,7.929106],[6.475668,-3.888458,-9.909073,-8.697664,4.265511,-8.796094,-3.341966,5.677357,2.428911,-0.385081,-4.960377,0.999604],[8.374317,4.705404,-6.503521,5.723291,-1.456971,7.461656,-2.978771,4.568663,-6.217595,7.696265,1.149905,6.994729],[0.641652,-3.327356,-4.491627,3.296102,4.688925,6.998998,6.686396,3.689385,3.319987,-4.001042,-0.775482,2.597658]],[[-6.792572,7.817577,6.539853,-5.766321,4.847279,-2.044836,0.790176,0.020705,-2.806839,-4.980053,6.443639,-5.108869],[1.403593,-8.156069,-2.385816,-6.773173,-9.663924,-3.168067,-7.216944,1.515875,8.459741,0.154122,2.766641,8.788240],[-0.169685,-0.645883,-3.996282,-0.813235,1.425755,7.639939,-3.314495,-8.513917,-9.505633,0.474896,-0.165923,-4.886680],[-9.359129,-2.512496,-2.573035,-0.106275,6.543389,-4.472404,4.169285,7.672374,5.703884,-1.980056,-4.523916,-8.565888]],[[0.725927,-2.989442,-5.024480,2.636930,-3.855466,3.898631,-3.554584,3.108777,-5.313942,5.291963,-1.035762,-4.334671],[2.200563,-3.159653,-9.583015,-8.633106,-4.854809,6.315784,9.954459,5.970381,-1.093573,-1.170109,-5.122183,-8.778011],[7.528573,-5.225653,0.231141,2.788647,4.087753,-3.403955,9.475407,2.208602,3.368293,-7.805665,-0.541916,2.830922],[-7.256784,6.507927,1.032422,0.044169,4.321044,6.183531,9.448271,5.243040,-3.701622,-3.640645,1.231345,8.618797]],[[-6.390418,8.332492,2.860372,5.128597,2.487718,2.901707,-1.370224,7.367146,-2.716906,-1.671489,-9.600217,8.648854],[-2.134794,-8.175749,0.765123,-0.395116,5.419313,-3.451504,-2.713744,3.474313,-6.837153,6.946740,8.041955,-3.216622],[6.062224,5.958683,7.783863,-4.397786,-5.446700,2.586122,-0.425464,1.856982,5.170143,-2.289283,8.023350,6.342441],[-1.104849,2.130704,-5.081969,-7.683186,-7.887471,8.173349,-6.093577,3.722486,-2.023316,-4.240587,5.439107,-2.310934]],[[-4.815138,-2.551267,-3.695426,8.543436,-3.958578,1.349392,7.070354,-9.749968,7.635327,1.541315,4.875415,0.398963],[4.568098,-7.723254,8.384690,4.256484,-3.628894,-5.642448,-3.947135,2.448655,-5.684593,3.392699,-3.895537,0.705917],[7.308392,7.722640,-7.514173,-9.874580,4.953227,-6.169658,1.986337,-3.048793,1.160075,4.204543,-6.900801,7.412261],[0.636819,-2.828723,-3.381449,5.635888,-5.383835,6.588533,7.603072,-6.243314,-4.639528,-7.977319,0.540680,8.217166]],[[3.831949,-4.129628,-9.145630,-0.662437,-6.568987,5.387547,-4.208048,-9.369455,-2.623220,1.855603,9.562448,-5.246963],[-2.796929,7.286952,0.464356,7.962250,4.133036,-6.357388,1.066950,7.111339,-6.352167,-2.238859,-4.966206,8.422891],[-3.736970,-8.448892,3.696591,-1.845397,8.429341,8.150584,-7.162758,4.292904,-4.617628,1.562225,-3.103269,2.030475],[-4.040557,-6.113229,-6.600046,5.514276,-1.002803,-8.919034,-6.822212,-0.289764,-2.811203,-5.363588,-9.049136,8.288400]],[[5.755121,-1.217519,2.181808,-6.834313,8.676126,-7.158579,9.987276,9.257258,-6.157317,0.404001,-4.483536,-7.784261],[7.582275,0.976561,3.484572,-0.381749,-8.152702,-2.880109,-9.079897,7.809080,8.660773,0.798755,7.360108,4.831512],[-1.396253,-6.190878,-0.899277,1.927070,5.359210,5.638157,9.673923,8.149413,-8.428651,-9.758614,8.514199,-4.616508],[3.975589,0.550273,-2.261987,-1.323134,7.422549,6.089006,-8.285700,3.553264,-2.122994,-4.553985,-3.989888,9.281588]],[[4.479833,0.490363,1.942606,-3.687052,4.060463,0.993572,-8.244629,-5.929375,-2.791329,9.215514,-9.696470,-1.512502],[7.933386,0.856458,-6.960757,-8.791589,-8.964944,-4.238440,9.901370,-4.690144,-8.720669,8.368782,-5.710444,-7.177413],[0.105947,3.169081,-4.811000,-7.221971,-7.635154,1.340265,-4.639990,-9.809770,9.722799,-0.198355,9.076484,0.266987],[-0.593911,-2.516836,-0.558328,8.801254,-6.046687,-7.947903,-7.306816,-1.554406,-1.497627,-5.084085,2.903764,4.815544]],[[4.285971,-9.319564,-8.065425,7.958140,-4.074030,0.780271,-6.672858,-5.493070,0.086737,-4.144465,-3.334764,-5.076020],[-2.752758,3.104950,-4.582244,7.055484,5.543519,-8.305533,7.167019,-3.479533,-5.797342,9.153204,4.632348,6.558937],[-2.257253,-6.779794,3.099988,8.067072,5.123800,2.564379,8.134654,-1.975547,-6.084066,-3.809240,-8.682199,1.047161],[6.468539,4.300012,4.118280,4.122807,-5.871442,-6.374807,6.408643,-6.505644,-5.987983,-3.442012,-0.732275,-2.278859]]], dtype = "float32")#candidate|7618|(11, 4, 12)|const|float32
uop_7619 = relay.rsqrt(const_7618.astype('float32')) # shape=(11, 4, 12)
bop_7621 = relay.maximum(uop_7619.astype('uint16'), relay.reshape(const_7618.astype('uint16'), relay.shape_of(uop_7619))) # shape=(11, 4, 12)
func_4475_call = mod.get_global_var('func_4475')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_7624 = relay.TupleGetItem(func_4475_call(), 0)
call_7625 = relay.TupleGetItem(func_4476_call(), 0)
uop_7636 = relay.acosh(const_7618.astype('float64')) # shape=(11, 4, 12)
output = relay.Tuple([bop_7621,call_7624,uop_7636,])
output2 = relay.Tuple([bop_7621,call_7625,uop_7636,])
func_7640 = relay.Function([], output)
mod['func_7640'] = func_7640
mod = relay.transform.InferType()(mod)
mutated_mod['func_7640'] = func_7640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7640_call = mutated_mod.get_global_var('func_7640')
call_7641 = func_7640_call()
output = call_7641
func_7642 = relay.Function([], output)
mutated_mod['func_7642'] = func_7642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5626_call = mutated_mod.get_global_var('func_5626')
call_7663 = func_5625_call()
call_7664 = func_5625_call()
func_5496_call = mod.get_global_var('func_5496')
func_5498_call = mutated_mod.get_global_var('func_5498')
call_7665 = func_5496_call()
call_7666 = func_5496_call()
func_546_call = mod.get_global_var('func_546')
func_549_call = mutated_mod.get_global_var('func_549')
const_7676 = relay.const([[-3,-7,1,-5],[-7,-8,10,1],[-2,9,4,-9],[1,6,7,-9],[2,9,10,-4],[-4,5,-6,-4],[-1,-8,8,-4],[9,-10,-7,1],[5,-3,-3,1],[9,1,-10,-4],[1,-10,3,-7],[3,1,6,-1],[1,5,1,3],[-2,5,-1,-7],[-5,1,-2,-10],[-4,6,4,-1],[1,1,2,2],[-10,7,10,-4],[-10,2,-3,-6],[-5,9,10,-6],[-3,-3,-3,-10],[5,-4,9,9],[3,1,4,-5],[10,8,-1,10],[-3,3,-1,-1],[-10,1,-3,1],[2,3,1,-4],[-1,10,-1,10],[-7,-2,-5,7],[7,5,10,5],[-7,-9,6,9],[8,-1,-2,-2],[1,-9,6,2],[-4,3,-2,-8],[-7,-9,-2,10],[8,8,-2,10],[8,-2,5,-10],[-10,5,-1,10],[9,1,-8,1],[4,-9,-4,2],[8,8,7,-4],[-9,8,1,-8],[-9,-4,-3,6],[-6,6,4,4],[3,9,8,-8],[2,8,7,-8],[8,5,6,-9],[-6,4,2,-6],[-10,6,6,-8],[1,6,4,4],[3,-1,3,-3],[4,3,-7,-2],[1,8,1,10],[2,8,7,7],[-3,10,2,-9],[1,4,-10,-5],[-4,10,9,-7],[-3,8,-9,1],[5,2,-3,4],[4,1,6,-4],[-1,8,-2,10],[2,-7,-2,6],[10,-5,-10,8],[-8,-5,7,9],[-2,7,-3,-1],[-2,7,7,-3],[3,1,-8,-5],[-7,5,10,1],[2,-7,-4,10],[-9,2,-4,2],[-5,-9,3,3],[6,6,-1,-9],[-5,-8,7,5],[-8,-1,-3,8],[-7,1,4,-9],[-2,-6,2,-8],[2,-7,3,-4],[-8,3,-7,9],[9,5,4,4],[1,-2,7,-1],[3,9,-10,9],[7,1,-3,9],[10,7,-10,-3],[5,5,3,-3],[3,-4,-3,3],[3,4,-4,-9],[-9,-10,1,9],[9,8,-9,10],[-2,-7,5,5],[-5,5,-3,6],[5,10,-1,4],[2,-4,4,3],[6,1,3,1],[-6,-9,-3,3],[-3,3,-2,8],[10,5,5,8],[-9,7,4,1],[-4,-10,-7,4],[8,6,6,-3],[7,10,5,5],[8,7,-10,3],[9,3,-8,6],[6,-5,-7,1],[-6,5,-1,-5],[-4,1,3,8],[-7,7,-9,3],[-6,-10,-7,-8],[3,4,6,1],[4,-4,3,-8],[-6,-10,-10,10],[9,1,-2,9],[-2,7,2,8],[9,-4,7,-5],[-7,-7,5,-2],[-7,10,-2,5],[2,2,10,-2],[5,3,8,-4],[-2,1,-8,4],[8,7,5,-3],[-3,-2,6,-4],[-10,2,5,-4],[-9,-4,9,-4],[-4,-8,2,5],[-10,-10,1,-7],[1,8,7,2],[-6,-5,-6,6],[8,6,-9,5],[6,-6,-1,7],[-4,7,8,7],[6,10,1,-10],[2,-10,7,-8],[3,1,7,-4],[-4,2,10,5],[-3,10,3,-4],[-7,7,2,-8],[-1,8,6,1],[-5,-9,4,3],[-3,3,2,-2],[-4,3,-4,10],[10,5,10,-6],[-9,-9,1,2],[4,1,-5,-5],[1,4,10,3],[1,-8,4,-3],[-8,-3,6,-4],[-3,6,-7,-8],[2,-8,-5,4],[8,7,5,2],[6,-6,-5,1],[-5,-5,-2,3],[-4,-6,-1,-8],[-4,3,-7,-5],[-4,-5,1,-6],[-5,-9,3,-2],[-4,-9,1,-5],[2,-6,-7,-4],[-2,-10,5,7],[9,10,9,-3],[10,-7,-9,8],[4,-10,3,-2],[3,7,-1,1],[-2,4,-10,-4],[8,1,-6,9],[-1,1,-5,10],[-6,-7,1,7],[-6,5,-7,-6],[10,2,-6,-6],[-2,-2,9,-6],[-9,3,10,5],[10,-3,1,-4],[7,-7,-7,-10],[9,7,-4,-4],[-7,-4,7,-4],[-1,6,8,-5],[5,10,6,-2],[-3,-4,3,1],[6,-8,9,10],[1,-4,-5,6],[2,2,7,4],[5,9,7,-10],[7,6,10,-8],[3,1,-10,7]], dtype = "uint8")#candidate|7676|(182, 4)|const|uint8
call_7675 = relay.TupleGetItem(func_546_call(relay.reshape(const_7676.astype('uint8'), [13, 4, 14]), relay.reshape(const_7676.astype('uint8'), [13, 4, 14]), ), 0)
call_7677 = relay.TupleGetItem(func_549_call(relay.reshape(const_7676.astype('uint8'), [13, 4, 14]), relay.reshape(const_7676.astype('uint8'), [13, 4, 14]), ), 0)
func_3727_call = mod.get_global_var('func_3727')
func_3735_call = mutated_mod.get_global_var('func_3735')
var_7687 = relay.var("var_7687", dtype = "float64", shape = (90,))#candidate|7687|(90,)|var|float64
const_7688 = relay.const([-4.691945,-1.690105,2.012129,-0.189632,7.269401,4.862015,2.324284,3.932261,6.516934,8.788830,-0.641755,-9.773050,-2.992507,-4.958250,0.283516,-7.006375,-0.349347,4.121845,6.957760,3.813457,-0.698697,-4.674596,3.170593,8.448310,1.960719,-6.903656,-3.084878,-3.830804,-1.692682,7.122966,-6.216625,-5.985819,-4.318366,-2.612909,3.060816,-0.689751,-3.901138,-3.258839,-3.050273,0.643478,-7.206813,-3.079615,-1.475115,5.769999,1.026854,-8.540890,-3.953751,-3.567312,-1.887362,5.783669,-9.182783,-1.267905,-8.140741,-6.188675,-5.107540,9.639634,-5.877454,0.704196,-9.189397,6.701760,0.753844,8.077349,-0.376948,-1.382274,4.919571,0.753059,-0.154593,-7.316597,-1.620349,1.097165,-6.077702,8.758471,-1.040601,5.811789,-7.373566,-2.332606,3.328261,5.374541,0.544733,-4.261123,4.917628,3.529751,7.356882,2.730682,-4.135098,-5.723248,5.378704,8.857731,8.815101,-7.424787,-4.264165,9.692021,0.292628,2.712389,2.714208,1.751123,6.931750,-9.418726,-9.406027,-1.848509,-4.912472,-1.621040,7.208427,-9.786781,-8.541491,-4.093392,4.922224,-9.726889,-8.212044,-4.879475,-6.713871,3.814882,-2.243847,-8.809959,6.409857,5.731982,-1.022219,1.165367,-1.630475,-7.831787,-9.414372,6.792494,-2.680427,-3.047951,0.859531,-8.464583,-6.584088,-2.243395,9.221504,-3.806285,7.015530,5.459135,2.802310,8.202436,-4.068920,-0.303187,-0.700309,-3.929352,-4.117098,-2.139341,0.842873,9.954731,-1.073055,-8.650777,-6.928538,-0.388152,3.006645,9.600917,-4.559890,-7.078962,-4.411064,6.999476,-0.231361,-3.962062,1.385134,-9.664093,6.865021,-3.214807,4.081154,-6.382493,9.530059,-3.787958,-1.432311,7.217369,-1.432868,1.235387,1.848924,-9.833492,-6.513687,-6.330004,8.775984,7.250831,-2.086040,-5.063914,-3.725241,6.077666,3.426686,-3.689914,-9.601130,-0.004651,0.093862,2.905504,-7.246401,-8.189215,-5.412262,-8.661964,-2.426763,8.998406,-9.800591,-8.057415,-4.841518,-6.128561,3.323626,7.126229,8.665898,6.938573,4.229315,0.021503,-6.810484,-6.120175,-9.614523,-2.940737,-7.476474,2.129472,2.292674,-2.624276,8.941797,0.073771,6.940067,-5.664168,-4.798572,-3.602135,4.744208,3.992075,4.802158,-4.241608,6.507561,-4.497503,-0.577223,-9.385523,-1.084953,5.382844,6.780458,-1.820534,6.545753,1.217628,-7.912142,0.410865,1.061185,6.767852,8.219617,-5.164781,-1.011499,-2.462064,-7.791738,-0.327025,5.758845,7.589640,-6.345494,-3.349080,-0.297065,4.498525,9.371062,-4.282115,-1.206631,7.725265,-9.074373,-3.625917,5.533185,4.645342,4.740218,-9.314841,-0.151931,2.886027,8.958027,-8.980691,-0.406877,4.695833,5.637114,-3.785288,4.131053,0.905323,-6.605830,8.163343,-3.018360,1.785866,-9.229143,8.576136,6.141304,-5.335208,-1.138141,0.676837,-4.661023,-5.025404,-9.320652,3.017601,-7.557758,4.772273,-8.495863,-7.965953,-1.899658,-4.495348,5.463712,8.357222,8.699998,-6.831427,-6.367473,-9.202718,-7.693356,-3.211666,1.966202,-9.192043,-0.982076,-6.213777,-8.763858,-2.379868,2.917107,-7.929854,-0.591725,4.940261,9.504426,6.370216,9.733327,-4.383277,-8.266030,6.600308,1.637263,0.551695,2.749671,-0.709413,1.317720,-6.239690,-8.299111,7.278092,-8.142650,-1.936930,-3.261275,-2.425064,6.828080,9.606730,5.652269,7.656591,2.092103,6.999063,7.937781,-0.584005,-6.349675,3.797099,9.013001,2.841999,5.711520,2.122487,8.991869,-9.630573,4.585011,-8.981537,-3.795101,2.261843,-3.273878,-8.631249,-7.977809,-6.025655,-2.623799,1.032180,1.870896,3.159400,-6.446985,-0.493894,-4.303589,-3.603741,9.587956,7.897572,0.014195,9.648895,5.165304,0.570984,-5.391805,-2.046053,6.762757,8.100405,-4.776660,8.401578,1.167191,-5.601850,-2.859401,1.265792,3.837076,3.784656,3.163818,-1.487622,4.817748,5.987230,-9.558605,-1.869106,1.739675,-0.079658,-7.962441,3.296955,2.292640,-7.440964,-2.264927,0.755526,-0.849037,-4.128907,2.329242,-9.886501,-8.350306,7.109285,2.880404,-3.288439,4.343958,-4.087294,3.077248,0.714638,8.345649,-8.346129,-0.792735,4.076255,9.419466,-1.451898,-5.119000,5.935308,-7.801050,5.555925,-2.248805,3.804288,-7.336360,4.845691,0.278005,4.414266,-1.434105,-7.533547,7.223791,3.228256,-0.919170,-5.385338,-7.412621,2.657302,-9.944250,-2.934134,4.039227,-7.038051,5.793742,1.504621,-1.061415,4.183558,-8.476618,5.597512,8.020956,-6.119132,1.453958,2.330788,-0.096003,-1.632669,4.149486,7.226185,-2.896781,6.543410,-9.689338,-8.083923,9.656089,0.786248,-4.787168,1.034220,-7.379551,4.694154,-7.739418,9.164658,3.197058,8.175025,9.932767,2.081817,-5.333351,7.813451,1.306464,-4.086329,-8.877077,7.741009,-6.428310,-0.178948,-5.533266,-7.471701,-0.664783,-8.261347,-4.034424,4.917075,-9.533544,1.166076,7.352681,4.849569,6.125672,4.719053,-9.264426,-7.922340,5.913437,9.408553,-3.212242,5.685466,3.359369,-0.307478,5.371842,1.287151,5.444852,7.320183,-4.633943,8.487363,-8.918725,6.812895,0.755429,1.755078,-0.383583,0.341335,5.732563,-7.126050,-0.191279,-2.096707,-8.934023,8.639033,-0.034627,-5.567417,-3.900128,-7.064632,-6.167545,7.021772,3.901849,-4.091669,8.650862,-5.415790,-8.837442,5.393098,-1.219817,1.711920,-5.973174,-1.111760,9.170567,2.696941,-4.649073,-6.238821,2.169114,5.222766,-1.939771,-5.275218,9.644740,-7.649500,5.870474,-5.179205,7.553363,-2.547890,-1.658862,4.548495,6.907213,4.024653,-5.737342,-6.575728,1.463009,3.951059,-4.349310,6.995407,-2.304768,6.646597,-1.691865,7.333920,6.791759,0.900354,-1.405251,7.356284,2.333153,-8.652557,-8.363028,1.792256,-4.496295,-8.610224,-2.180507,-5.372529,6.445068,2.558238,8.058503,-5.007364,-8.405675,-7.500562,-1.812064,0.952044,2.666563,7.307293,-7.006484,8.300935,9.480900,2.109345,-0.854746,7.152679,-2.668593,9.852738,1.411840,-3.504455,6.413327,1.696051,7.241246,4.918853,-2.040133,-0.339184,3.311625,9.665824,2.200771,-5.522803,-0.020458,-8.098982,-6.714324,-2.647531,9.043663,-7.895997,1.172428,-6.222524,-3.680620,0.365086,-0.763375,3.527674,-4.875608,5.741585,-8.183175,8.856679,1.511867,3.450366,3.731498,6.033133,-3.809112,1.138998,3.773272,-0.494281,8.036576,-5.855317,-9.173813,9.981942,-0.858090,-3.960352,-6.780397,6.299264,3.453405,-7.650922,-4.869026,5.163342,6.962315,8.939554,-1.845142,-0.464161,1.100783,-7.959830,-9.350974,-7.420753,-7.092594,4.490186,-8.386949,-9.736550,3.463628,-7.855427,-0.936667,4.586001,-7.563395,6.175897,-7.130944,-0.462643,-6.852449,9.649625,-5.291468,-7.308179,0.628246,-3.829857,-1.376184,3.002958,8.812999,-1.242727,-3.612208,8.099023,-8.435279,4.800012,-7.969359,-4.647765,-4.756302,1.402554,-0.690459,7.366442,-9.655699,3.130505,-8.733811,-8.957316,7.176796,-7.139109,-1.906662,-6.471061,-2.958272,-4.725053,-1.380102,3.562918,-0.669043,4.154799,-7.723012,-1.895995,-5.780956,-2.163689,4.003799,-2.904955,0.500436,-7.344093,-7.214690,-2.109759,-4.084850,9.358833,1.304800,-9.544010,-7.269579,-4.672264,-7.991187,6.751844,3.040883,-1.103693,-0.369411,3.292364,8.068016,-5.566169,-7.356829,-4.780855,8.685007,6.550923,-8.126211,-5.989234,-3.603722,-0.067847,-1.829275,9.668996,9.474018,-8.683240,1.671048,2.670758,1.941996,-6.430590,-5.204757,-9.188829,0.781275,-7.346346,5.742099,-6.393657,-9.294747,2.825020,-9.827012,-9.876340,-7.155726,0.523674,-6.861797,-5.427321,-7.646683,2.795428,2.874940,-5.195484,-9.159316,-8.300313,-6.408988,4.132561,9.543787,1.612547,5.351749,0.569351,-9.020582,0.040404,5.177663,-0.851111,5.086859,-9.388989,5.017517,3.314896,-5.755377,-0.500725,-5.492747,4.869089,-4.183407,8.467433,-0.734723,7.591668,7.612496,9.470902,-8.570712,0.231913,8.277918,-3.619656,-7.620295,-2.656918,0.428324,4.339289,-2.659249,-7.561994,4.861942,0.366940,-3.682603,-5.659112,0.996390,8.914443,6.339549,0.355764,-8.478580,-8.414640,8.446604,7.668427,8.788269,-0.373110,9.213691,-1.460512,-7.496751,-2.837387,-7.435720,5.695790,-9.584491,3.357152,7.800829,7.636563,-9.104623,-0.874728,-9.482878,-9.037062,5.496327,-4.354294,5.830279,6.001843,-3.543159,4.277819,9.456905,-9.812114,5.037880,8.240578,7.101440,-2.376800,-2.603163,3.048863,4.930795,-1.218777,7.484833,1.721992,7.216899,-5.408807,2.058150,-9.299231,-2.566157,-8.664056,-7.635974,-0.135776,-4.726506,3.750942,-8.134701,-2.869556,4.893161,-4.926300,1.700330,6.181053,-0.053253,-1.579892,9.507158,-5.158429,8.680277,5.024701,8.948886,1.678437,8.595675,-3.979324,-4.356608,2.420195,-0.091776,-1.861063,1.624759,-4.309574,5.764875,4.694747,-3.490333,0.751040,2.121926,2.692641,-5.004712,-9.733668,-2.160663,3.351021,1.227074,-0.365308,-9.279192,1.706845,-5.874473,-6.249012,-2.082844,9.832760,9.617946,1.665111,3.375923,8.859705,5.089458,2.770381,2.824604,-3.930145,6.297060,-0.710437,1.302412,-7.389943,8.201892,-1.196232,-4.435172,-7.989366,-7.196316,-3.515590,2.171434,7.310497,-6.178243,-5.388045,-0.489569,-9.659178,9.640362,2.743641,2.310704,-0.444530,-6.494151,-3.425216,-4.757413,8.670249,-1.853923,9.471301,1.649386,9.997602,6.416750,9.564143,-7.217517,-7.699277,-3.690985,1.250505,8.026940,5.101392,-5.709358,-6.732470,-8.532219,2.447922,-9.066791,-8.978035,1.137643,0.045588,6.790356,-6.599405,-7.729020,3.898310,6.182427,-6.559151,1.234963,-3.637557,-8.775192,-7.181680,-2.200191,4.878160,-0.770571,5.501285,9.049449,0.790451,4.888987,4.705621,-9.413390,5.514140,1.536949,-2.640790,9.675322,-0.039613,8.206590,-7.913873,-2.976229,-1.840804,-7.973178,-8.158725,-1.503953,-7.577126,-3.244987,-7.070503,0.018698,-0.695154,2.941668,4.767339,4.478693,-3.106631,-1.329495,5.256004,5.338260,-8.829906,1.263376,3.683717,-4.057686,2.117411,1.006377,0.321438,1.644445,4.344999,-5.283996,0.764732,-1.816940,-1.801311,2.570367,4.732434,-9.019058,-6.069921,7.556671,1.599482,3.615657,-5.255307,-7.693045,8.204488,6.897627,3.771527,2.717365,6.764655,-1.823195,4.148187,1.792887,-5.131243], dtype = "float64")#candidate|7688|(990,)|const|float64
var_7689 = relay.var("var_7689", dtype = "float64", shape = (1512,))#candidate|7689|(1512,)|var|float64
const_7690 = relay.const([True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True], dtype = "bool")#candidate|7690|(336,)|const|bool
var_7691 = relay.var("var_7691", dtype = "bool", shape = (168, 4))#candidate|7691|(168, 4)|var|bool
const_7692 = relay.const([-6,-9,-6,-9,-5,-9,-1,8,-7,-1,7,6,8,2,2,5,2,5,6,-7,2,-1,6,-10,-4,-4,2,-2,-4,4,-2,6,-1,-2,-4,10,-6,-3,-2,-7,-4,7,9,-8,-6,10,3,1,-6,3,-3,10,-5,2,-3,-4,-8,-5,-2,1,-7,-5,-7,-4,-1,-5,-1,-4,7,6,4,9,2,-10,-6,2,4,-6,6,-5,9,3,-8,-8,2,-7,5,8,-9,-4,3,-10,7,-9,-6,-2,-6,-6,-4,9,10,2,-1,5,-3,7,-6,3,3,-6,4,-5,-5,-7,5,4,-2,-1,9,5,4,7,8,-3,10,9,9,8,-5,10,-1,-7,1,7,3,-5,1,9,2,10,3,-9,5,6,-2,-2,-1,7,-9,5,6,1,1,-7,-1,-6,8,5,-3,-7,-7,8,-10,-1,1,10,-5,-5,10,9,10,-4,-1,4,-9,-8,10,8,3,8,7,-9,1,-9,5,10,5,4,4,9,10,2,3,1,-9,-8,-1,9,1,2,-9,-1,-6,-2,6,-4,9,8,7,-8,10,-3,6,-2,-3,3,7,-6,-3,-3,-10,-7,6,2,7,-10,-9,8,6,-2,-4,-8,-1,6,-3,-4,10,3,-9,9,-7,2,3,-1,2,7,8,-9,-2,-4,-5,-1,2,-1,10,-4,9,5,8,1,1,9,5,-10,-4,3,5,-4,-7,5,-5,6,-6,7,9,5,-8,-9,4,-2,-4,-8,9,3,9,5,8,1,2,-8,-8,1,9,10,7,-2,7,9,3,3,-1,-9,2,3,-8,5,5,-3,-5,-6,5,5,-7,9,8,6,-4,8,-5,-10,-3,-10,-10,-3,-5,7,-8,-3,7,-6,8,4,-7,6,5,-4,2,9,6,-8,2,3,10,-4,10,3,2,-9,-2,-10,2,7,7,-7,9,-5,1,-8,6,9,2,3,9,-4,9,-8,-7,7,5,8,-9,5,-1,-10,-7,-2,-1,4,8,-9,-1,10,-5,5,-10,6,-3,9,5,10,10,-10,6,-9,3,1,-8,-3,9,5,-10,9,1,9,7,10,1,8,-6,-4,-6,3,8,-9,6,6,-4,-9,-3,2,8,-7,2,8,4,-6,-9,-4,-7,-3,6,8,4,-6,-6,7,2,4,-1,3,4,-6,10,-1,-5,-1,6,3,-9,-9,9,10,1,-7,-6,-10,2,5,-7,3,3,-3,5,10,-4,10,6,7,4,2,6,2,9,4,-6,-6,-10,9,-4,3,10,3,3,-5,-4,7,-10,-10,8,5,-10,4,-1,-7,-4,4,4,-1,-7,-2,-7,5,-9,6,-8,1,3,7,-10,10,-7,-9,-4,-7,-1,4,-7,-5,3,-4,-4,8,-2,-1,1,8,8,8,10,-2,2,8,4,-8,5,-7,-8,-6,10,-7,-9,-9,-2,8,10,-4,-6,6,8,-9,7,-3,3,-9,7,3,1,-4,9,-9,-1,-3,-7,-9,4,-9,-7,10,-10,-2,7,4,7,2,-9,7,6,-9,3,-10,-9,10,9,-4,10,-7,-3,-6,-10,-8,-1,-3,7,2,1,6,10,5,-7,2,7,6,-2,-10,-1,5,5,9,-9,3,4,1,-7,-5,5,6,7,-10,4,-3,-8,9,8,7,-10,9,-10,-7,-5,3,-10,-2,1,-5,-1,2,-9,-5,8,6,2,1,4,-9,2,10,3,6,3,-2,2,-4,-4,9,10,-1,1,-6,-4,5,-9,6,7,7,-3,-4,3,-7,-6,-3,2,-1,-8,7,2,-7,-8,-4,-5,7,-1,5,9,-3,10,5,9,-6,-3,-10,8,-9,-8,-3,5,1,3,2,-9,10,10,-3,1,8,4,-10,-3,9,1,6,-6,-4,4,2,10,3,5,-8,5,10,-4,-2,-1,-10,-4,10,3,8,9,-1,10,-8,-7,-1,2,4,4,-3,-8,9,9,-2,3,-10,-10,3,2,-6,8,3,-3,-4,-4,3,-9,-4,2,-1,-7,-9,-1,-10,-4,5,-6,-1,-7,7,3,-3,-4,1,4,1,2,-10,-4,7,7,-1,-10,3,9,-9,1,7,1,-1,9,-6,-4,5,7,10,-5,8,-5,-5,2,-9,7,8,1,3,-1,-2,-5,5,-10,-7,-5,-2,-5,-5,2,10,9,9,7,-1,-1,5,9,-10,-4,5,2,-10,-4,-4,10,-10,-1,-10,-1,7,5,9,-10,4,-6,5,-6,-6,9,-9,-1,-9,-7,1,1,9,-9,-1,-7,-5,4,2,-3,2,-6,3,9,-4,-1,6,2,-8,-6,-10,-6,8,4,-1,8,-3,4,6,7,2,4,2,5,-6,10,6,4,-7,-5,7,10,10,5,-7,-5,-2,9,4,5,7,-10,3,-6,-2,7,-4,9,-8,9,9,-6,-2,7,7,8,7,-6,1,1,4,-3,4,2,6,-9,9,8,-8,-9,-6,10,6,6,-9,1,4,2,3,1,-9,-8,6,2,-10,-1,-10,2,9,5,6,1,-9,-7,9,4,10,8,8,2,-1,-4,5,8,5,-4,-1,-10,-10,-3,-7,-8,-10,3,-6,-8,9,9,10,-10,5,4,8,4,-1,8,-7,4,-3,-7,-3,8,-7,-6,6,-9,-9,-7,-9,5,-10,-9,-9,6,2,-3,-6,-7,-9,9,-10,-6,-5,5,4,5,3,2,-9,-6,-2,7,1,3,8,5,4,6,4,3,-3,3,4,-10,6,3,-6,-7,4,-6,6,10,-3,-7,-10,-7,1,-9,-9,-8,-6,4,1,8,3,-10,7,9,8,9,8,-9,5,-6,8,9,8,5,-5,7,-8,9,6,-5,3,2,-9,-4,10,9,5,1,3,3,10,-8,-6,4,-2,-8,-3,8,-1,6,-2,1,-5,3,10,-6,5,-1,-10,4,-3,6,-3,10,7,-7,-3,8,-3,-7,-6,-5,6,3,10,7,2,-1,-2,-10,7,9,8,-7,8,-3,-7,-7,-4,-1,10,8,-5,-6,10,-5,-3,-6,-4,9,-8,-8,3,-10,-6,1,-8,7,-10], dtype = "uint64")#candidate|7692|(1152,)|const|uint64
call_7686 = relay.TupleGetItem(func_3727_call(relay.reshape(var_7687.astype('float64'), [1, 10, 9]), relay.reshape(const_7688.astype('float64'), [11, 10, 9]), relay.reshape(var_7689.astype('float64'), [1512,]), relay.reshape(const_7690.astype('bool'), [4, 84]), relay.reshape(var_7691.astype('bool'), [672,]), relay.reshape(const_7692.astype('uint64'), [1152,]), ), 2)
call_7693 = relay.TupleGetItem(func_3735_call(relay.reshape(var_7687.astype('float64'), [1, 10, 9]), relay.reshape(const_7688.astype('float64'), [11, 10, 9]), relay.reshape(var_7689.astype('float64'), [1512,]), relay.reshape(const_7690.astype('bool'), [4, 84]), relay.reshape(var_7691.astype('bool'), [672,]), relay.reshape(const_7692.astype('uint64'), [1152,]), ), 2)
output = relay.Tuple([call_7663,call_7665,call_7675,const_7676,call_7686,var_7687,const_7688,var_7689,const_7690,var_7691,const_7692,])
output2 = relay.Tuple([call_7664,call_7666,call_7677,const_7676,call_7693,var_7687,const_7688,var_7689,const_7690,var_7691,const_7692,])
func_7696 = relay.Function([var_7687,var_7689,var_7691,], output)
mod['func_7696'] = func_7696
mod = relay.transform.InferType()(mod)
var_7697 = relay.var("var_7697", dtype = "float64", shape = (90,))#candidate|7697|(90,)|var|float64
var_7698 = relay.var("var_7698", dtype = "float64", shape = (1512,))#candidate|7698|(1512,)|var|float64
var_7699 = relay.var("var_7699", dtype = "bool", shape = (168, 4))#candidate|7699|(168, 4)|var|bool
output = func_7696(var_7697,var_7698,var_7699,)
func_7700 = relay.Function([var_7697,var_7698,var_7699,], output)
mutated_mod['func_7700'] = func_7700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6387_call = mod.get_global_var('func_6387')
func_6388_call = mutated_mod.get_global_var('func_6388')
call_7720 = func_6387_call()
call_7721 = func_6387_call()
func_4817_call = mod.get_global_var('func_4817')
func_4819_call = mutated_mod.get_global_var('func_4819')
var_7725 = relay.var("var_7725", dtype = "float64", shape = (90,))#candidate|7725|(90,)|var|float64
call_7724 = relay.TupleGetItem(func_4817_call(relay.reshape(var_7725.astype('float64'), [90,])), 4)
call_7726 = relay.TupleGetItem(func_4819_call(relay.reshape(var_7725.astype('float64'), [90,])), 4)
output = relay.Tuple([call_7720,call_7724,var_7725,])
output2 = relay.Tuple([call_7721,call_7726,var_7725,])
func_7731 = relay.Function([var_7725,], output)
mod['func_7731'] = func_7731
mod = relay.transform.InferType()(mod)
var_7732 = relay.var("var_7732", dtype = "float64", shape = (90,))#candidate|7732|(90,)|var|float64
output = func_7731(var_7732)
func_7733 = relay.Function([var_7732], output)
mutated_mod['func_7733'] = func_7733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_7771 = func_3896_call()
call_7772 = func_3896_call()
output = call_7771
output2 = call_7772
func_7782 = relay.Function([], output)
mod['func_7782'] = func_7782
mod = relay.transform.InferType()(mod)
mutated_mod['func_7782'] = func_7782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7782_call = mutated_mod.get_global_var('func_7782')
call_7783 = func_7782_call()
output = call_7783
func_7784 = relay.Function([], output)
mutated_mod['func_7784'] = func_7784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5012_call = mod.get_global_var('func_5012')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_7821 = relay.TupleGetItem(func_5012_call(), 3)
call_7822 = relay.TupleGetItem(func_5013_call(), 3)
func_5560_call = mod.get_global_var('func_5560')
func_5563_call = mutated_mod.get_global_var('func_5563')
call_7855 = relay.TupleGetItem(func_5560_call(relay.reshape(call_7821.astype('float64'), [8, 15, 4])), 3)
call_7856 = relay.TupleGetItem(func_5563_call(relay.reshape(call_7821.astype('float64'), [8, 15, 4])), 3)
output = relay.Tuple([call_7821,call_7855,])
output2 = relay.Tuple([call_7822,call_7856,])
func_7858 = relay.Function([], output)
mod['func_7858'] = func_7858
mod = relay.transform.InferType()(mod)
output = func_7858()
func_7859 = relay.Function([], output)
mutated_mod['func_7859'] = func_7859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_7910 = relay.TupleGetItem(func_3130_call(), 0)
call_7911 = relay.TupleGetItem(func_3131_call(), 0)
output = call_7910
output2 = call_7911
func_7913 = relay.Function([], output)
mod['func_7913'] = func_7913
mod = relay.transform.InferType()(mod)
output = func_7913()
func_7914 = relay.Function([], output)
mutated_mod['func_7914'] = func_7914
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8079 = relay.const([[[-5,-7,-5,-4],[-8,8,7,7],[6,4,-1,5],[4,3,-5,9],[3,-2,9,-1],[-5,1,8,1],[4,-2,-10,7]]], dtype = "int8")#candidate|8079|(1, 7, 4)|const|int8
var_8080 = relay.var("var_8080", dtype = "int8", shape = (10, 7, 4))#candidate|8080|(10, 7, 4)|var|int8
bop_8081 = relay.minimum(const_8079.astype('int8'), var_8080.astype('int8')) # shape=(10, 7, 4)
output = relay.Tuple([bop_8081,])
output2 = relay.Tuple([bop_8081,])
func_8087 = relay.Function([var_8080,], output)
mod['func_8087'] = func_8087
mod = relay.transform.InferType()(mod)
var_8088 = relay.var("var_8088", dtype = "int8", shape = (10, 7, 4))#candidate|8088|(10, 7, 4)|var|int8
output = func_8087(var_8088)
func_8089 = relay.Function([var_8088], output)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7279_call = mod.get_global_var('func_7279')
func_7280_call = mutated_mod.get_global_var('func_7280')
call_8096 = func_7279_call()
call_8097 = func_7279_call()
output = call_8096
output2 = call_8097
func_8122 = relay.Function([], output)
mod['func_8122'] = func_8122
mod = relay.transform.InferType()(mod)
mutated_mod['func_8122'] = func_8122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8122_call = mutated_mod.get_global_var('func_8122')
call_8123 = func_8122_call()
output = call_8123
func_8124 = relay.Function([], output)
mutated_mod['func_8124'] = func_8124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4417_call = mod.get_global_var('func_4417')
func_4418_call = mutated_mod.get_global_var('func_4418')
call_8133 = relay.TupleGetItem(func_4417_call(), 0)
call_8134 = relay.TupleGetItem(func_4418_call(), 0)
func_6094_call = mod.get_global_var('func_6094')
func_6096_call = mutated_mod.get_global_var('func_6096')
call_8155 = relay.TupleGetItem(func_6094_call(), 4)
call_8156 = relay.TupleGetItem(func_6096_call(), 4)
output = relay.Tuple([call_8133,call_8155,])
output2 = relay.Tuple([call_8134,call_8156,])
func_8167 = relay.Function([], output)
mod['func_8167'] = func_8167
mod = relay.transform.InferType()(mod)
output = func_8167()
func_8168 = relay.Function([], output)
mutated_mod['func_8168'] = func_8168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7430_call = mod.get_global_var('func_7430')
func_7431_call = mutated_mod.get_global_var('func_7431')
call_8214 = relay.TupleGetItem(func_7430_call(), 0)
call_8215 = relay.TupleGetItem(func_7431_call(), 0)
output = relay.Tuple([call_8214,])
output2 = relay.Tuple([call_8215,])
func_8222 = relay.Function([], output)
mod['func_8222'] = func_8222
mod = relay.transform.InferType()(mod)
output = func_8222()
func_8223 = relay.Function([], output)
mutated_mod['func_8223'] = func_8223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5012_call = mod.get_global_var('func_5012')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_8277 = relay.TupleGetItem(func_5012_call(), 2)
call_8278 = relay.TupleGetItem(func_5013_call(), 2)
func_3727_call = mod.get_global_var('func_3727')
func_3735_call = mutated_mod.get_global_var('func_3735')
var_8296 = relay.var("var_8296", dtype = "float64", shape = (90,))#candidate|8296|(90,)|var|float64
const_8297 = relay.const([-1.864552,-1.174350,-7.869326,-7.485569,-9.427097,-2.557034,-9.244782,1.892682,3.122640,-1.890079,-9.646941,7.508558,-2.639808,-6.485390,2.726234,6.045808,-5.222075,-2.211709,9.676773,9.207020,5.342793,-8.542822,-0.409492,6.471319,-4.382282,-0.525096,4.999284,-2.732727,-9.615228,0.125357,-2.687977,-4.994159,-4.756318,2.546256,2.765877,-9.817596,-0.180675,-1.685222,-0.375224,2.232058,4.982979,-9.636338,9.182348,-2.331996,2.106054,2.687599,-5.175848,-0.357548,-3.994284,-3.138978,-8.592237,5.021946,-6.229905,5.685040,7.106655,0.011101,-6.159719,-1.944458,-9.483349,5.417954,-0.114602,-9.462380,-8.341826,-3.525227,-3.780445,8.553776,3.802398,-4.561035,-0.462689,-9.897437,-2.460828,4.750013,5.178367,-1.640169,-7.263599,9.064963,-3.889055,-6.313486,-3.711258,2.490783,3.347203,0.952618,1.640491,-6.699879,0.883458,-5.263992,7.348104,-6.017367,8.534847,-7.937364,0.538668,-7.027998,3.793599,-1.167496,4.881015,3.958641,-5.413304,3.270369,-3.510828,-3.331708,8.123466,6.706741,-3.781115,5.991177,-2.900595,9.869077,-3.589166,8.925519,-8.088447,0.898568,4.568020,8.257338,-9.849731,-3.049591,-0.264497,-0.592059,2.888351,-3.685068,-7.561366,3.674912,-4.821449,-7.110969,-1.127867,-9.249431,4.211783,9.338794,-8.460037,0.063527,0.730875,1.321817,-4.647546,2.154057,3.164661,0.023419,-5.148083,-7.495844,4.409226,1.617651,-9.093618,3.199220,1.085529,7.067076,1.726627,-3.886859,-2.570682,-9.521737,-0.977898,-0.394065,-8.339288,1.332070,-9.508378,7.567300,-0.585167,6.184451,-4.501879,-3.916127,1.938599,-5.880393,-4.373916,-7.908125,-4.475486,5.269443,-0.774928,2.665175,3.389482,5.453268,-6.511565,-7.514975,1.653320,-8.058301,-5.863586,-4.084986,-3.878242,-0.082141,2.054043,7.267689,3.522245,-4.869389,-5.929441,-6.631408,-7.375704,0.631988,-9.509994,2.203844,4.372887,-6.929154,2.441737,-8.505395,7.517992,-4.467857,5.462165,-6.892492,1.539081,-6.862593,-5.809017,7.210855,6.151444,-3.241167,-6.731639,5.207470,4.772043,2.825211,-5.186366,-7.291547,-6.885283,2.825390,-0.133080,2.397316,-5.333833,6.488006,-9.056695,-0.890172,4.679465,-4.191921,-9.484789,2.287826,6.531091,-7.632693,-3.700472,4.757511,-6.376249,-9.668105,-5.200187,-3.822451,-7.849347,-3.043357,-1.329656,-3.168843,4.999592,-3.518446,-0.537745,4.094666,-0.506490,-1.719893,-3.347433,-8.981990,-3.324979,1.985313,-3.846101,6.937451,3.944714,4.619751,-5.211095,6.420567,-2.666363,-5.388741,5.791415,-3.012691,5.581302,9.063423,-9.073949,-9.295865,-8.227175,-9.626801,1.979715,6.103566,9.573369,5.329182,-3.869137,3.219743,-5.429754,-0.210266,3.378097,0.902860,5.974668,-7.373029,-0.959858,-8.356938,-0.789048,4.106279,-8.764620,-6.616247,-1.106590,-6.076583,-2.694724,0.027217,7.336783,-7.965177,6.976758,3.297680,-6.833730,-0.473568,7.876711,-1.305758,0.234358,5.219138,-7.474086,1.969485,4.326712,-9.211704,6.313551,-0.110686,1.821396,5.090313,7.331776,2.764784,-6.050707,-4.225763,-4.399240,5.669651,5.080570,6.336022,-1.489377,-4.421907,-6.404598,6.621332,-1.593529,-8.144384,3.783159,-0.481799,3.152625,-9.496423,-5.904552,7.496115,4.405168,-9.283293,3.983307,2.812087,2.573625,-1.382042,-6.267765,3.609157,2.566776,-5.020148,-4.672983,9.071012,-3.450154,4.628757,9.351566,0.046554,-3.482905,3.491894,5.574441,5.125916,-4.031183,2.098994,-1.218380,4.430867,-0.751039,-9.778888,5.814760,-1.781984,7.296844,-8.186728,-6.841516,-3.216050,7.141691,2.884450,-5.623285,6.851593,-2.203046,6.381766,-4.346148,-7.558513,-5.804965,0.791618,0.417070,4.711972,9.993509,5.010319,8.706767,-4.024902,4.974957,7.832524,4.531766,-7.415163,4.149887,-3.066864,-4.276412,0.840928,5.150594,-4.649390,-7.393255,8.799412,6.670076,-1.092015,-6.018109,-4.540791,-3.621304,8.948201,-7.399054,7.563744,5.046793,3.380835,-9.151938,-3.146467,7.945850,-2.730983,-4.599886,-2.742034,-3.574362,-0.619244,6.143411,-7.422678,8.336842,7.089517,6.615318,8.664794,-7.113793,6.883733,3.042373,-5.816907,-8.655809,5.227392,5.675340,2.888431,-6.475819,-8.784057,-6.003365,8.646752,9.434810,2.295384,5.473501,6.322547,-8.151010,-9.369031,6.508147,-5.965867,-6.145490,-2.437971,5.262680,6.478841,-9.896918,-4.221620,5.864620,-2.674596,-9.936792,3.775729,-0.469689,-2.920614,4.339775,9.809633,7.132826,6.372871,1.596805,5.358948,8.724148,-8.060593,3.214302,-7.750678,-9.869709,3.154839,-1.340982,-5.274072,9.553162,1.392705,5.418102,9.557559,7.867307,-6.209641,4.275601,8.089264,6.283619,-9.940883,-3.290973,0.409255,5.461663,-6.278875,2.500599,-9.920357,2.594590,-3.705798,-5.513596,3.892864,-2.906517,-6.654066,-7.147254,-3.107668,6.296244,-7.730381,3.762078,-2.914385,-5.205158,-6.847322,7.192409,-8.794465,1.693230,-4.123863,4.759679,9.205868,3.713914,3.068339,8.917198,4.469020,-4.527137,7.135406,4.426959,-0.591010,-9.332951,-5.332025,8.986084,-4.729375,7.239836,8.744722,-5.290148,-3.397420,-9.227284,6.627571,1.692009,3.814269,-8.693828,1.573428,-4.347513,1.429175,-3.945343,5.375742,0.114538,-3.049398,-5.121427,1.165432,-0.398482,-7.220791,3.190825,6.368372,5.556964,-6.540651,5.102978,4.833893,7.650864,-1.739798,-0.093532,6.081791,6.128836,-4.716036,5.283785,-4.414434,6.889369,1.964565,3.904919,3.397967,1.177313,-7.913618,9.261260,-4.347834,5.584977,6.159090,-5.783153,4.017781,-3.777609,9.911944,6.780417,-0.321153,7.669460,3.954644,-4.295692,3.460480,-0.364754,-8.654103,4.378748,-1.443270,3.283638,6.665040,-8.073766,2.233936,-5.461045,2.140114,-0.112846,8.998416,2.144344,-2.373797,9.241870,4.427960,-0.057249,-1.381855,-3.447263,-1.463296,-2.000528,-1.272961,-6.508491,9.037711,-6.978516,-7.117610,-4.963724,-4.208359,-0.414804,0.117148,-9.424297,4.821369,-9.862805,9.643932,-9.790959,-5.010517,7.160941,8.127160,-6.811780,-0.259255,3.877697,-4.336939,-4.853045,4.391733,5.586178,9.948694,5.885501,-5.328201,-3.981824,6.757817,1.216255,9.805009,-9.410109,-2.077864,3.650413,8.083623,0.304299,8.679888,6.601266,-1.854340,2.737738,-4.733914,-7.096272,2.067506,-5.205295,7.679897,-4.478882,-1.641760,-4.494468,-8.290489,-1.833190,-0.184269,7.522790,0.413917,2.249548,2.967040,0.131059,2.563807,2.101277,-6.578974,1.504582,9.509895,-7.079112,-7.667930,0.499340,2.671667,8.634176,4.162561,8.597621,7.539938,9.288761,7.772997,-8.627183,-5.057839,1.433661,-7.625216,7.465645,3.813858,8.591560,-1.441263,-3.507205,-8.119099,8.493325,-3.469072,7.468112,9.749370,-2.578829,1.240864,-0.381935,-3.144085,6.336175,-1.146428,2.051205,-6.379651,-3.990114,3.088315,-7.724643,-0.846151,5.665745,-5.902945,-0.451379,8.584646,7.364615,2.823702,6.611800,4.423875,-1.236353,5.134752,8.156489,8.483479,-3.292118,-7.807656,-8.908094,-5.938742,9.215120,-5.213388,3.540738,2.754124,3.002844,-4.336795,-2.176781,4.330026,7.732912,-1.535629,-9.634162,-5.447582,-4.582516,-6.928033,7.220265,4.123515,7.786924,-9.353239,6.171625,3.217977,3.498279,7.140450,-0.355524,-7.033104,5.728646,-7.910872,-2.566596,-2.547613,-0.131480,-8.289116,-9.868653,-5.488038,6.298411,-3.449686,-4.445530,4.507829,5.944906,-7.467977,5.473376,3.405928,7.294308,3.838384,6.907286,3.291034,-8.455262,3.759017,5.639916,-1.108506,6.257115,2.454945,4.373940,6.644533,-9.990172,-3.132081,-2.769977,-1.143922,6.331488,-6.763809,-0.966820,-5.088712,0.810641,7.213080,-5.455176,9.986659,-0.787672,9.569086,-1.123195,-8.894944,-2.252430,-3.239495,-7.719279,0.552047,-7.956949,-7.950981,2.982854,3.765057,1.008758,8.604092,1.156646,9.289517,8.405255,3.884973,6.829259,-5.451516,-6.038982,-3.925825,-6.202637,-9.550487,6.761843,1.731814,-1.867671,2.385808,0.113117,9.510453,-4.874160,-0.774817,3.192569,5.883535,7.287154,7.687587,-2.771167,-0.914003,3.941565,-0.767346,-6.956080,9.628343,-8.731003,-1.546288,2.814102,-6.893246,-8.845805,5.013867,-8.757917,-0.947094,6.525024,9.681618,9.805212,-6.175241,5.615839,-7.351311,-2.502822,-0.469252,-2.137877,-8.508280,-1.219990,1.783165,4.963188,-4.528058,1.348824,8.814397,-6.249798,7.041688,-6.273721,-9.813153,-4.427012,6.067197,-3.715628,1.884249,-7.952521,-6.887527,7.113683,2.734657,2.311054,-2.148588,-0.252699,9.850833,6.895697,5.122824,-6.030141,9.581231,-7.343212,9.059488,-8.487071,0.909706,-5.725901,5.381392,-0.495874,-9.358442,-7.515227,-0.271741,-5.599028,-8.809609,-1.614357,9.394994,8.500704,7.453040,-1.223114,1.522218,-7.299759,4.731085,-6.247546,-2.197799,-1.401586,-3.082653,9.388661,6.350424,-2.666751,4.374236,2.840289,8.903461,6.903854,-3.677817,9.964992,-2.559017,7.644911,-5.732507,-6.189851,-7.223345,2.814997,-3.194892,7.456885,-7.931961,3.163512,4.247951,1.593437,1.081801,4.218122,-0.669263,9.930507,-0.702234,-0.938068,5.770379,1.737981,0.776350,-4.226766,-1.812683,-7.287264,-1.923740,-6.477765,-2.038233,-8.661983,7.361779,-3.760366,6.697592,-7.996315,-1.251963,-3.722160,-6.170876,8.165112,5.192270,3.879739,6.382407,-1.654810,1.723826,0.048250,-6.168218,7.612098,-4.117569,9.269280,-5.608051,9.658603,0.438240,-4.201441,-8.395735,5.115820,7.476277,7.572358,-1.929044,-8.277807,-1.557994,-2.608545,-5.763301,-5.052767,5.346759,-3.328791,-1.661670,-0.858227,8.938988,2.632296,-4.958115,0.638198,5.623584,-6.574799,8.351116,6.462076,3.651714,-7.527289,3.567049,-4.686126,8.438681,-0.471600,-9.660505,1.018052,0.711027,6.225119,4.759427,-0.169639,4.510245,4.669936,9.359313,8.621807,-0.243886,-5.800765,-6.025312,-9.518673,0.932086,3.470013,1.105697,-5.893821,2.399857,-4.616146,-0.989058,8.463038,7.231467,-3.075826,4.474905,6.899308,-5.425194,-8.048610,-9.092649,-3.494965,2.119383,-5.504924,-2.365345,-9.182949,-0.279324,-4.694748,3.902063,2.474450,-7.856255,3.078252,1.740425,6.140458,4.796101,-2.325712,-1.420148,2.317900,6.272222,-3.149985,-2.625661], dtype = "float64")#candidate|8297|(990,)|const|float64
const_8298 = relay.const([-6.534021,-6.102080,-0.873874,8.465658,-0.147834,-5.470063,-2.691926,9.769813,-8.576984,9.095642,-0.741305,3.175324,-4.793760,5.171369,-0.842720,-8.646900,8.184891,-3.921338,7.481839,7.781782,-3.677172,-9.491219,1.155690,-7.305264,1.023001,-0.330921,-0.958610,0.805671,4.925632,-7.338811,8.228167,-6.412927,2.423092,-2.684387,1.492657,1.748293,-9.198885,-8.898343,3.768993,3.864947,6.422721,-7.119498,6.889762,-7.363755,-4.315269,-5.322673,1.991511,-5.911955,-4.011816,-4.866997,7.050076,9.602601,8.466254,7.646122,-2.745546,2.281388,-8.711057,5.327608,8.115898,1.169796,3.626901,-8.036275,-8.286734,9.588201,7.050335,-3.645918,2.923247,-5.775648,-8.256848,-0.803017,-9.239129,-4.300713,3.411522,-9.586366,8.722375,1.299718,-4.294923,-0.973787,-9.245683,4.006397,7.646574,-1.905203,3.493084,9.389225,2.083431,4.684912,7.582090,-5.323026,5.256293,-0.421222,-0.713618,1.201865,8.349366,-6.525680,-1.815724,8.555926,6.505173,-8.195837,2.826241,-8.036996,5.830712,-8.270063,8.245764,-5.712337,-4.253135,-6.416935,-3.362874,0.659534,2.166872,2.911892,9.943053,6.628887,1.379187,2.768765,1.023791,0.364613,1.303977,1.233241,-3.880341,-2.402295,-0.980233,-0.421392,-7.609517,-1.620572,7.214882,9.973813,9.185384,9.981841,1.392340,8.917776,1.387447,9.157003,-5.712127,7.635474,-9.188965,1.468127,-1.606391,8.770965,4.344212,-1.782991,-0.024554,6.976952,-1.079738,-3.718998,-4.199196,-9.599459,-6.806488,-3.183465,8.132622,3.983685,8.892839,-5.589205,-3.780861,9.590107,-1.917066,-3.161078,0.637031,-0.652198,8.648422,5.875690,-3.534726,7.163737,-3.079908,0.923348,6.430707,9.614786,-9.142289,3.037885,-9.436478,-3.171642,-1.313312,3.571259,1.587118,-4.486461,-3.061118,-0.173697,3.244944,9.832479,2.823478,7.909114,7.358583,-0.740458,6.670341,0.216278,-6.527389,-1.606601,-9.229345,-8.855409,8.881713,-4.442946,4.642351,-2.198778,-4.204589,-5.483130,-9.386353,1.152592,-3.828691,6.763710,0.198450,4.543208,1.147911,-5.383097,8.195294,9.089631,4.914205,-0.370907,-8.008747,-3.182422,-0.249547,-3.779890,-4.539322,7.170122,8.022412,-7.280072,4.727181,-1.086594,3.535300,-0.713012,-0.437521,7.067870,-3.470742,-3.329696,-4.107992,1.097866,6.452563,-7.763121,9.819845,-9.864580,-2.558708,0.213202,4.860049,-0.065617,1.445066,4.934701,-4.164720,1.149522,3.453390,0.732653,-0.802588,-0.415024,9.962357,-6.942768,-1.904712,6.685317,0.436403,-4.821893,3.331822,-9.555895,-1.039393,-5.074604,-8.476552,1.556556,7.234574,-6.464821,2.728179,6.025064,8.501369,-0.415521,-5.379868,-1.184166,-3.903595,-7.326577,-1.401943,-5.771997,1.963343,8.966792,2.885792,8.177440,-9.841834,-7.062224,-1.753321,-7.229986,4.901963,-0.761878,-6.511042,-4.234330,3.660333,-2.517934,0.613529,-1.666295,2.372068,-3.221401,-5.698863,0.821956,7.474294,5.688755,3.245028,8.596297,-3.390189,0.519201,2.029116,8.963580,-7.586252,-6.830258,4.814427,-3.440749,-3.027162,4.773314,-6.667300,2.304986,-1.702293,-4.094818,-8.461770,6.168036,4.602583,-7.109415,-8.910090,1.720711,8.968039,-7.738146,8.054455,-4.229631,4.924948,-5.034837,-7.666460,-2.313105,-1.715084,6.632123,-0.237446,1.739176,3.998459,-0.895093,-8.238214,-0.676179,1.602398,-9.962804,-2.913633,2.696349,-4.983882,7.058182,6.772078,5.099405,-5.119311,2.698716,5.267149,-0.309514,-6.983006,-8.028868,3.805572,-7.991987,8.674550,2.621614,9.343687,-6.246969,-1.116025,2.553021,8.794977,-8.194060,5.828796,-8.881200,-4.719228,3.056293,-8.794145,9.032964,-6.324146,-7.651297,-4.511721,9.629509,-5.715924,4.567796,-6.335920,4.359490,-0.947284,8.436068,7.005226,-1.302452,0.993439,-1.944109,-2.694620,5.696356,7.874973,-8.970453,0.901401,-6.484219,0.009676,-3.627639,-3.567039,8.528094,7.870134,-7.123085,2.346194,5.576427,-7.222082,-3.047588,7.322263,9.167362,2.707950,3.804886,-9.610684,7.705127,3.453598,0.661788,1.926450,-4.652759,5.670534,3.382013,-6.555155,6.539616,-8.262342,7.689661,6.433943,-6.967310,-2.206535,6.101029,5.647265,1.830996,8.766048,-1.048766,7.047337,1.217672,1.702991,9.395367,7.576209,-1.349870,-6.520915,-9.012522,1.417886,9.516131,-3.627559,-3.539220,4.690133,-2.985372,-9.593898,7.979641,-2.561057,-2.660772,3.378481,9.878711,6.738485,-5.320548,5.755881,1.460401,4.609929,-0.569000,-8.804607,-8.464092,-7.460876,-2.682300,7.807063,8.485216,-8.222639,-5.904922,9.450514,1.981779,0.777187,7.691055,-3.625631,2.968733,0.480622,3.230670,-7.559377,5.889148,-4.936594,4.076490,7.910322,9.597954,0.835290,4.034451,6.935184,3.914251,-1.767328,8.700041,8.832158,-6.146441,1.644288,-3.328489,4.803049,-1.389365,5.004596,-3.409418,-4.397931,6.567505,8.599882,8.610107,4.310776,1.968910,1.905347,-1.955286,-1.019296,8.518528,-4.471688,9.417001,6.064087,0.144087,-8.062088,3.131105,-8.761063,-6.457654,7.383818,-6.218871,-1.566921,-4.527995,7.225722,-8.457497,2.114774,3.108169,-6.072770,-4.979857,-0.781076,-2.488384,2.227290,-4.456813,-0.198394,2.784633,-7.227867,-4.370160,9.276419,-4.853865,2.744698,-1.670697,-2.437761,-1.271289,8.517943,-0.385565,8.576967,-8.233122,-3.023755,-9.006419,3.365825,-2.167860,8.920817,-1.644182,1.019258,5.936490,0.303710,9.131668,6.718007,-3.718529,-6.758520,3.958217,-7.523353,-6.664024,-1.207954,3.493722,-5.248902,8.012929,6.636788,8.982744,-1.205453,8.163705,-7.027934,5.903401,2.769368,-5.703500,-0.585558,1.474401,2.023233,3.878851,-6.961468,6.529796,-2.952853,-0.558163,-7.589795,-4.846762,7.620541,2.544507,-3.795112,4.593328,-2.447568,-7.300418,0.778499,8.691902,9.864260,-0.008762,-3.670692,2.914383,-2.503416,-1.318068,5.281655,8.202148,-0.581623,-7.551884,5.751907,-7.390178,-6.919136,-3.096684,-6.941744,-0.638849,-7.388705,0.371870,7.637802,3.182469,5.586749,-7.913041,-5.827677,0.708607,-8.097640,-2.589014,5.651651,-5.154155,6.094172,-6.498501,-1.463324,3.892151,6.775016,6.478382,8.502293,8.258586,-4.881377,3.106574,6.386183,-1.028170,1.198637,-9.128752,3.644860,-0.175016,4.959542,6.809258,0.109913,6.538245,2.189145,4.943788,4.965672,9.570687,0.892599,1.465367,2.383298,-7.967761,-6.826527,-3.041098,9.088679,-8.535240,6.368726,1.363684,-1.197356,2.364779,6.551363,0.747964,2.103476,2.326180,1.932464,-6.996316,-8.073530,9.022084,3.022133,-2.315993,-2.714005,2.228542,-8.629076,5.640629,4.399153,8.455331,4.769968,-1.519966,2.210720,0.624654,-9.285397,-6.074826,1.067172,9.600668,6.366128,5.779208,-4.278742,0.130683,1.606290,9.858100,7.458954,-9.943805,4.660291,-7.960176,-9.482834,-1.554327,4.732755,1.241246,-0.547883,2.317891,-3.181801,-2.443234,2.823205,-5.826188,-7.163260,-0.399668,-0.073941,-4.565218,2.468935,-1.408733,9.138649,-6.670024,3.211711,0.315563,-6.211860,2.248395,9.331859,9.875573,2.261374,-4.640888,8.762617,-1.407949,3.630193,-6.965404,3.653631,-4.673716,0.859143,4.237751,-5.958230,-4.719059,8.947640,1.236118,0.446303,5.066288,-1.024293,-8.596075,-7.784826,2.265696,-9.288341,-5.030057,7.877267,-0.615017,8.222455,0.999603,-4.198074,-5.438492,-9.683930,-5.585955,-7.880789,-2.310167,6.831582,8.007988,5.707626,5.256833,-0.882989,1.989735,-8.393186,-1.943475,8.190661,4.836893,6.141359,6.123997,-2.237546,-1.521061,-0.158120,3.020234,5.245073,2.496339,-2.090020,-5.765709,2.208790,-5.949892,5.930609,1.809021,-6.832938,-3.736722,5.248869,5.900219,-7.904442,-2.163158,4.223173,-3.948272,-6.049002,0.255411,8.108100,2.648100,-5.341341,-4.834639,-6.410571,-0.602671,4.393585,6.439842,6.755030,-5.701174,-6.714366,-2.050657,-3.659029,-8.129824,-3.883560,3.703534,-7.279482,-9.280161,-8.404199,-9.636979,2.027238,-6.497341,-4.576691,1.752243,-4.936611,2.686867,-5.413623,-0.406827,-2.232426,-2.595527,0.606859,-5.797386,-6.646037,-0.342633,-0.190847,-6.354139,5.395957,-2.183206,-4.097820,3.381091,0.661953,8.823003,-5.656489,-9.137852,-8.049959,-3.387438,2.920370,0.702666,6.495437,-4.693325,1.090276,3.622550,8.944599,-9.730231,6.980481,7.599398,-0.138220,6.736704,-9.203051,3.539071,-3.829933,-8.750697,6.524183,6.627977,5.572974,-2.360333,-5.128314,-1.460589,2.942975,5.020259,-1.403951,8.502910,5.911819,-3.866813,-3.853603,5.798027,9.993091,-0.208607,8.269308,4.237340,-7.453803,0.228181,-2.159388,-0.048390,-3.753513,-7.314628,-4.702305,6.860988,-8.264619,-9.029217,-2.087024,6.195818,6.889195,-4.161058,-7.097693,-0.803146,4.815947,1.345028,2.581997,2.081257,-6.093154,-7.160961,8.923529,-1.676630,3.896797,-3.658043,-7.025289,7.910155,-8.333740,6.310329,-3.064773,5.924390,1.540227,7.215121,-3.770427,3.493262,-3.233795,-3.502425,5.205901,-6.524494,0.781280,-1.629860,-3.695512,4.425018,7.261300,4.151320,-1.757388,7.876403,-8.285325,-3.085469,3.048958,5.552753,-4.045781,5.882948,-5.413305,-0.081669,7.407693,-8.657258,9.215320,-6.715632,-0.393436,-3.213267,-6.161498,-1.075115,-0.656935,1.470039,-6.044981,1.310817,-8.400732,8.982645,-0.515335,-8.537711,-8.744329,-1.471199,5.204141,1.326590,-2.729838,-6.866780,1.772081,5.673289,-9.386202,-4.696191,0.356031,1.382029,-2.342648,7.302604,-1.098540,-1.481972,-2.507966,-7.534634,1.528942,7.616458,9.830434,-2.295066,-0.313067,-7.548241,7.454453,-7.860498,7.384582,-2.177281,-5.761997,-7.126340,-3.909721,4.841514,3.586681,-6.651901,2.577854,6.616959,9.451952,-3.095666,5.505723,-3.233321,7.410413,-1.132055,-5.310777,-5.035353,-7.901690,-7.696740,-7.291359,8.957341,9.345275,-1.747938,4.491719,-0.864331,-9.569100,-7.480207,2.148646,-2.162487,9.914626,0.943824,4.986683,-8.347794,9.864166,-3.486194,3.651005,2.308566,9.436986,5.163076,7.943638,-0.564784,-0.549004,-2.441383,3.191856,-0.143672,1.729320,9.787672,-4.560081,-9.775710,-2.101342,3.718465,-3.978144,-6.686817,-3.579964,-2.753489,2.692265,0.930166,8.854626,-4.645050,-5.748190,-7.824509,-8.128492,7.610148,7.951748,-0.885176,-5.842303,5.277356,6.559045,5.771887,-2.011276,1.319360,-3.393303,3.808913,-8.989209,-4.766455,5.513353,-6.884377,-2.969370,-8.214294,0.483939,8.297140,-7.499711,-8.212722,4.144853,6.094141,1.407501,6.203767,-5.915611,-2.035583,-6.796574,5.632157,6.046212,-8.078607,9.299265,6.996419,1.606433,7.667893,-0.729469,7.593867,3.251864,3.023971,-9.091855,-1.344237,6.836107,3.689641,1.209925,3.073857,8.174249,7.834489,-5.127318,0.485000,1.753001,9.173413,5.596057,7.673095,-6.207501,8.250553,-5.932914,2.273637,-8.722011,6.508031,4.013958,-2.053734,-1.080763,-2.870204,9.967142,8.282010,-9.362754,-8.276222,2.807053,-9.932653,-3.358326,-5.437594,2.765803,-7.488444,5.864072,8.132625,0.317163,0.093930,6.722063,-7.553946,2.019421,-1.892793,4.324970,4.275987,-3.649428,-7.689730,-8.891056,1.807352,-1.731376,9.743761,-9.520135,-1.359511,0.029197,8.193692,8.098762,7.531830,2.118031,-5.405231,-8.665742,-6.291491,1.255392,7.523922,2.651736,6.593596,-5.760791,0.647775,-9.785089,-5.766242,8.688547,-8.119356,-0.650602,-4.206326,0.943434,-0.943353,-2.550191,2.291285,0.910879,5.679333,0.542517,-7.897460,-8.363855,-9.528426,0.546112,-3.860779,4.394223,-9.593315,-3.905297,3.693704,4.113877,6.855816,-9.610161,-3.175675,3.214683,7.786620,-8.227557,-8.768048,2.151118,9.148623,-1.667333,-3.505467,8.028795,1.886514,6.143313,6.573393,-6.790529,-9.700212,8.382885,-7.125158,5.354131,-4.560673,2.924465,-4.597364,9.816201,8.585226,8.903724,0.031568,-7.392802,-5.803642,-5.945915,3.500553,-5.526675,7.549688,-1.312052,-3.205846,2.845002,5.753177,0.562178,-6.537131,-6.120758,-5.042105,6.030658,-0.043749,-6.083949,8.267408,-7.779098,5.993750,-7.670580,7.451873,-0.542549,-4.999612,-0.941457,-0.861477,1.086484,-3.991078,6.333152,2.987046,9.511986,-0.918530,-5.096045,-8.609738,-5.637515,3.677484,-6.469808,6.628662,-0.901157,8.592771,-7.185265,1.257020,-8.193701,6.541483,-7.653176,-2.183672,-7.172376,-0.843592,-7.588325,8.830086,-3.895374,0.706161,4.940994,-1.331696,2.766083,-8.577825,6.226869,6.224340,-5.638040,8.149533,-6.532162,-9.009100,1.221805,5.316172,8.066472,-8.646113,-2.180416,-5.019184,0.031220,9.546898,-1.000280,-8.594521,6.159454,7.854587,-3.933730,9.011457,-7.534254,3.296380,-2.655295,5.555049,6.154842,4.808755,-3.279722,-5.216600,-1.630956,-3.965172,7.203279,7.603062,-6.875922,-2.724625,8.079899,0.603713,9.163919,6.723376,-8.287650,9.887774,4.095864,5.746721,1.564443,1.045818,0.534113,-4.575496,-3.308833,-7.566080,5.436775,5.648903,-2.994218,-0.314001,9.827219,0.779734,8.278902,4.504496,3.408587,-4.030908,-0.475785,0.546396,1.099246,5.080139,8.599980,-4.006448,-1.994711,0.235009,9.708733,7.845557,-0.824617,-3.943692,0.691899,-7.858253,-8.203236,1.160410,-9.327980,-7.847387,8.625063,9.813445,1.315193,1.665500,1.450382,-0.995392,-0.297023,0.226178,-0.446208,-3.139877,8.923889,3.919971,6.364904,5.830045,4.944840,7.083499,8.120289,0.587435,5.193068,-7.458924,4.442368,7.108970,-0.856074,-1.066928,-2.096456,2.783349,3.918109,8.098545,5.608515,-3.232694,-1.167898,7.360117,-8.450360,8.484213,2.966083,-8.463790,-6.984014,0.847947,-0.731033,-6.551355,-3.419669,0.607330,-7.219196,6.546240,9.683611,-7.634183,9.506974,0.963976,-0.872688,2.693680,-3.232426,-3.258686,0.288665,-2.663326,-9.818727,-8.002098,-0.741434,-1.861032,-5.695955,-4.954346,-9.004084,-9.184613,3.594446,6.784048,-3.376348,2.081101,2.411212,8.155677,4.573236,-2.925626,-1.090363,9.977640,-6.993270,6.426931,0.896513,-0.572657,-8.729716,7.739244,-6.484927,2.329289,-2.955770,-0.627677,5.565773,-4.319222,8.071801,-9.674556,-5.065256,-0.171086,9.150291,4.703504,7.955382,-7.994688,-2.217307,1.161284,3.082045,1.393064,-6.338413,7.737442,-9.050658,-4.755922,-6.461258,7.631720,-2.792382,-4.291415,-4.648492,-3.219677,3.462524,4.142330,9.967511,5.241862,-2.812814,-5.008054,-7.710444,-5.703220,8.146476,-8.880913,6.252964,-5.805984,8.440148,2.164888,6.235146,7.506661,8.423407,-0.863494,-3.774892,4.973684,3.400244,6.144142,8.165285,-2.890366,-1.818385,-4.889985,-2.614062,-0.552499,3.556013,8.458288,0.871076,-9.846169,-2.284793,8.464294,-6.329045,2.640057,-5.506849,0.538727,-5.430437,0.747806,-5.214098,-6.335305,-5.399619,-7.994945,-4.394963,-8.000095,-4.519026,-2.468934,-7.720304,8.314207,-7.264703,-1.733807,6.728373,-6.101603,5.106459,9.792744,-6.506332,-1.355509,-4.281743,-7.754171,6.793285,-9.332005,1.031901,-3.269620,9.337101,-0.910658,-0.550228,-5.587621,-9.645183,8.694062,-6.604158,7.087785,-3.732110,-7.671416,-9.245382,6.096401,6.916458,-8.755070,3.009193,-9.598419,-3.576284,-7.493731,0.146405,3.491407,-2.755697,1.206016,6.671427,2.395682,1.631736,-1.817652,-1.495754,6.497243,0.155740,8.378774,-8.537785,5.664346,-7.242210,1.268441,3.537235,-8.454515,7.540261,-1.672987,-2.850286,-9.739371,6.506658,-1.491490,-4.927875,-0.924051,7.594220,-2.490411,0.552844,-4.509064,-0.150607,-4.226913,-0.400090,0.730764,-5.600409,-0.030386,4.624248,-2.168258,5.292835,-9.029723,-3.540551,-7.691929,-7.293239,0.510498,-0.407348,-2.682512], dtype = "float64")#candidate|8298|(1512,)|const|float64
const_8299 = relay.const([[False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True],[False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False],[True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True],[False,True,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,True,True,False,True,False],[True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True],[True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True],[True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True],[False,False,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False]], dtype = "bool")#candidate|8299|(8, 42)|const|bool
var_8300 = relay.var("var_8300", dtype = "bool", shape = (672,))#candidate|8300|(672,)|var|bool
call_8295 = relay.TupleGetItem(func_3727_call(relay.reshape(var_8296.astype('float64'), [1, 10, 9]), relay.reshape(const_8297.astype('float64'), [11, 10, 9]), relay.reshape(const_8298.astype('float64'), [1512,]), relay.reshape(const_8299.astype('bool'), [4, 84]), relay.reshape(var_8300.astype('bool'), [672,]), relay.reshape(call_8277.astype('uint64'), [1152,]), ), 5)
call_8301 = relay.TupleGetItem(func_3735_call(relay.reshape(var_8296.astype('float64'), [1, 10, 9]), relay.reshape(const_8297.astype('float64'), [11, 10, 9]), relay.reshape(const_8298.astype('float64'), [1512,]), relay.reshape(const_8299.astype('bool'), [4, 84]), relay.reshape(var_8300.astype('bool'), [672,]), relay.reshape(call_8277.astype('uint64'), [1152,]), ), 5)
uop_8306 = relay.asin(const_8298.astype('float32')) # shape=(1512,)
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
call_8310 = relay.TupleGetItem(func_7482_call(), 0)
call_8311 = relay.TupleGetItem(func_7484_call(), 0)
output = relay.Tuple([call_8277,call_8295,var_8296,const_8297,const_8299,var_8300,uop_8306,call_8310,])
output2 = relay.Tuple([call_8278,call_8301,var_8296,const_8297,const_8299,var_8300,uop_8306,call_8311,])
func_8318 = relay.Function([var_8296,var_8300,], output)
mod['func_8318'] = func_8318
mod = relay.transform.InferType()(mod)
var_8319 = relay.var("var_8319", dtype = "float64", shape = (90,))#candidate|8319|(90,)|var|float64
var_8320 = relay.var("var_8320", dtype = "bool", shape = (672,))#candidate|8320|(672,)|var|bool
output = func_8318(var_8319,var_8320,)
func_8321 = relay.Function([var_8319,var_8320,], output)
mutated_mod['func_8321'] = func_8321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_8345 = func_5583_call()
call_8346 = func_5583_call()
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_8349 = relay.TupleGetItem(func_3274_call(), 0)
call_8350 = relay.TupleGetItem(func_3275_call(), 0)
output = relay.Tuple([call_8345,call_8349,])
output2 = relay.Tuple([call_8346,call_8350,])
func_8351 = relay.Function([], output)
mod['func_8351'] = func_8351
mod = relay.transform.InferType()(mod)
output = func_8351()
func_8352 = relay.Function([], output)
mutated_mod['func_8352'] = func_8352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3182_call = mod.get_global_var('func_3182')
func_3183_call = mutated_mod.get_global_var('func_3183')
call_8439 = func_3182_call()
call_8440 = func_3182_call()
output = call_8439
output2 = call_8440
func_8463 = relay.Function([], output)
mod['func_8463'] = func_8463
mod = relay.transform.InferType()(mod)
output = func_8463()
func_8464 = relay.Function([], output)
mutated_mod['func_8464'] = func_8464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mod.get_global_var('func_6838')
func_6840_call = mutated_mod.get_global_var('func_6840')
call_8531 = relay.TupleGetItem(func_6838_call(), 0)
call_8532 = relay.TupleGetItem(func_6840_call(), 0)
output = call_8531
output2 = call_8532
func_8535 = relay.Function([], output)
mod['func_8535'] = func_8535
mod = relay.transform.InferType()(mod)
mutated_mod['func_8535'] = func_8535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8535_call = mutated_mod.get_global_var('func_8535')
call_8536 = func_8535_call()
output = call_8536
func_8537 = relay.Function([], output)
mutated_mod['func_8537'] = func_8537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8535_call = mod.get_global_var('func_8535')
func_8537_call = mutated_mod.get_global_var('func_8537')
call_8547 = func_8535_call()
call_8548 = func_8535_call()
output = call_8547
output2 = call_8548
func_8565 = relay.Function([], output)
mod['func_8565'] = func_8565
mod = relay.transform.InferType()(mod)
mutated_mod['func_8565'] = func_8565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8565_call = mutated_mod.get_global_var('func_8565')
call_8566 = func_8565_call()
output = call_8566
func_8567 = relay.Function([], output)
mutated_mod['func_8567'] = func_8567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6171_call = mod.get_global_var('func_6171')
func_6173_call = mutated_mod.get_global_var('func_6173')
call_8590 = func_6171_call()
call_8591 = func_6171_call()
func_5738_call = mod.get_global_var('func_5738')
func_5743_call = mutated_mod.get_global_var('func_5743')
var_8601 = relay.var("var_8601", dtype = "uint8", shape = (728,))#candidate|8601|(728,)|var|uint8
var_8602 = relay.var("var_8602", dtype = "float64", shape = (3, 30))#candidate|8602|(3, 30)|var|float64
var_8603 = relay.var("var_8603", dtype = "uint64", shape = (1152,))#candidate|8603|(1152,)|var|uint64
call_8600 = relay.TupleGetItem(func_5738_call(relay.reshape(var_8601.astype('uint8'), [728,]), relay.reshape(var_8602.astype('float64'), [90,]), relay.reshape(var_8603.astype('uint64'), [1152,]), ), 5)
call_8604 = relay.TupleGetItem(func_5743_call(relay.reshape(var_8601.astype('uint8'), [728,]), relay.reshape(var_8602.astype('float64'), [90,]), relay.reshape(var_8603.astype('uint64'), [1152,]), ), 5)
func_5625_call = mod.get_global_var('func_5625')
func_5626_call = mutated_mod.get_global_var('func_5626')
call_8605 = func_5625_call()
call_8606 = func_5625_call()
output = relay.Tuple([call_8590,call_8600,var_8601,var_8602,var_8603,call_8605,])
output2 = relay.Tuple([call_8591,call_8604,var_8601,var_8602,var_8603,call_8606,])
func_8609 = relay.Function([var_8601,var_8602,var_8603,], output)
mod['func_8609'] = func_8609
mod = relay.transform.InferType()(mod)
var_8610 = relay.var("var_8610", dtype = "uint8", shape = (728,))#candidate|8610|(728,)|var|uint8
var_8611 = relay.var("var_8611", dtype = "float64", shape = (3, 30))#candidate|8611|(3, 30)|var|float64
var_8612 = relay.var("var_8612", dtype = "uint64", shape = (1152,))#candidate|8612|(1152,)|var|uint64
output = func_8609(var_8610,var_8611,var_8612,)
func_8613 = relay.Function([var_8610,var_8611,var_8612,], output)
mutated_mod['func_8613'] = func_8613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6243_call = mod.get_global_var('func_6243')
func_6244_call = mutated_mod.get_global_var('func_6244')
call_8621 = relay.TupleGetItem(func_6243_call(), 0)
call_8622 = relay.TupleGetItem(func_6244_call(), 0)
output = relay.Tuple([call_8621,])
output2 = relay.Tuple([call_8622,])
func_8655 = relay.Function([], output)
mod['func_8655'] = func_8655
mod = relay.transform.InferType()(mod)
output = func_8655()
func_8656 = relay.Function([], output)
mutated_mod['func_8656'] = func_8656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8726 = relay.var("var_8726", dtype = "int16", shape = (12, 16, 9))#candidate|8726|(12, 16, 9)|var|int16
var_8727 = relay.var("var_8727", dtype = "int16", shape = (12, 16, 9))#candidate|8727|(12, 16, 9)|var|int16
bop_8728 = relay.minimum(var_8726.astype('int16'), relay.reshape(var_8727.astype('int16'), relay.shape_of(var_8726))) # shape=(12, 16, 9)
uop_8740 = relay.asin(var_8726.astype('float64')) # shape=(12, 16, 9)
var_8746 = relay.var("var_8746", dtype = "float64", shape = (12, 16, 9))#candidate|8746|(12, 16, 9)|var|float64
bop_8747 = relay.equal(uop_8740.astype('bool'), relay.reshape(var_8746.astype('bool'), relay.shape_of(uop_8740))) # shape=(12, 16, 9)
output = relay.Tuple([bop_8728,bop_8747,])
output2 = relay.Tuple([bop_8728,bop_8747,])
func_8756 = relay.Function([var_8726,var_8727,var_8746,], output)
mod['func_8756'] = func_8756
mod = relay.transform.InferType()(mod)
mutated_mod['func_8756'] = func_8756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8756_call = mutated_mod.get_global_var('func_8756')
var_8758 = relay.var("var_8758", dtype = "int16", shape = (12, 16, 9))#candidate|8758|(12, 16, 9)|var|int16
var_8759 = relay.var("var_8759", dtype = "int16", shape = (12, 16, 9))#candidate|8759|(12, 16, 9)|var|int16
var_8760 = relay.var("var_8760", dtype = "float64", shape = (12, 16, 9))#candidate|8760|(12, 16, 9)|var|float64
call_8757 = func_8756_call(var_8758,var_8759,var_8760,)
output = call_8757
func_8761 = relay.Function([var_8758,var_8759,var_8760,], output)
mutated_mod['func_8761'] = func_8761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8655_call = mod.get_global_var('func_8655')
func_8656_call = mutated_mod.get_global_var('func_8656')
call_8778 = relay.TupleGetItem(func_8655_call(), 0)
call_8779 = relay.TupleGetItem(func_8656_call(), 0)
func_3573_call = mod.get_global_var('func_3573')
func_3575_call = mutated_mod.get_global_var('func_3575')
var_8781 = relay.var("var_8781", dtype = "float64", shape = (462, 2))#candidate|8781|(462, 2)|var|float64
call_8780 = relay.TupleGetItem(func_3573_call(relay.reshape(var_8781.astype('float64'), [924,])), 0)
call_8782 = relay.TupleGetItem(func_3575_call(relay.reshape(var_8781.astype('float64'), [924,])), 0)
output = relay.Tuple([call_8778,call_8780,var_8781,])
output2 = relay.Tuple([call_8779,call_8782,var_8781,])
func_8784 = relay.Function([var_8781,], output)
mod['func_8784'] = func_8784
mod = relay.transform.InferType()(mod)
mutated_mod['func_8784'] = func_8784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8785 = relay.var("var_8785", dtype = "float64", shape = (462, 2))#candidate|8785|(462, 2)|var|float64
func_8784_call = mutated_mod.get_global_var('func_8784')
call_8786 = func_8784_call(var_8785)
output = call_8786
func_8787 = relay.Function([var_8785], output)
mutated_mod['func_8787'] = func_8787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mod.get_global_var('func_6838')
func_6840_call = mutated_mod.get_global_var('func_6840')
call_8799 = relay.TupleGetItem(func_6838_call(), 0)
call_8800 = relay.TupleGetItem(func_6840_call(), 0)
output = relay.Tuple([call_8799,])
output2 = relay.Tuple([call_8800,])
func_8808 = relay.Function([], output)
mod['func_8808'] = func_8808
mod = relay.transform.InferType()(mod)
output = func_8808()
func_8809 = relay.Function([], output)
mutated_mod['func_8809'] = func_8809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5833_call = mod.get_global_var('func_5833')
func_5835_call = mutated_mod.get_global_var('func_5835')
call_8814 = func_5833_call()
call_8815 = func_5833_call()
output = relay.Tuple([call_8814,])
output2 = relay.Tuple([call_8815,])
func_8816 = relay.Function([], output)
mod['func_8816'] = func_8816
mod = relay.transform.InferType()(mod)
mutated_mod['func_8816'] = func_8816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8816_call = mutated_mod.get_global_var('func_8816')
call_8817 = func_8816_call()
output = call_8817
func_8818 = relay.Function([], output)
mutated_mod['func_8818'] = func_8818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6786_call = mod.get_global_var('func_6786')
func_6788_call = mutated_mod.get_global_var('func_6788')
call_8852 = relay.TupleGetItem(func_6786_call(), 0)
call_8853 = relay.TupleGetItem(func_6788_call(), 0)
func_7141_call = mod.get_global_var('func_7141')
func_7144_call = mutated_mod.get_global_var('func_7144')
const_8862 = relay.const([-10,-1,4,-2,-3,-10,5,-6,-9,-7,-10,1,-6,-4,-10,10,-3,-1,-4,-3,5,9,-3,10,2,2,-2,7,-9,-8,9,1,1,-8,-6,2,-6,3,6,3,3,-1,6,2,2,-4,-2,-10,8,-7,-10,-8,-2,8,-6,-7,6,-5,-9,-10,9,-1,-1,-3,8,5,-1,-6,6,10,-7,-3,8,-5,-5,9,9,4,-10,8,6,-7,6,9,-9,4,-7,-7,4,-5,9,2,1,-7,-2,-8,8,-5,-9,8,5,-4,-10,-9,-4,-3,8,10,-1,10,-2,6,-4,-6,-7,-2,6,-5,8,-1,10,-7,7,-6,6,4,4,10,10,2,-10,-10,-2,-3,10,-5,5,-7,-1,3,-10,-7,-8,4,-3,-5,-1,-9,1,3,5,-2,-4,-3,3,-4,4,9,10,-9,-8,-8,-1,-1,-1,4,6,6,-4,-7,-6,1,-4,-1,-4,9,-5,10,-6,-10,9,4,-9,-7,1,1,-7,-7,-3,-7,-9,8,5,-3,10,9,7,-7,2,-1,-10,-2,3,9,-10,-2,5,6,-7,-3,2,8,-3,-8,-9,-2,1,5,3,-1,-2,-3,-2,-9,8,8,3,-1,-1,5,-8,-10,-1,3,10,-9,9,-1,3,-10,3,-10,3,7,10,7,-1,7,3,5,5,8,-6,-5,-9,9,-4,-10,-10,-5,1,8,-9,1,6,5,-2,7,10,-8,-8,2,-5,1,1,8,5,3,3,-4,-2,2,2,3,-3,2,7,3,8,9,-9,-3,-7,8,10,10,-3,-7,4,-6,8,-8,1,7,5,-1,5,9,-10,-3,-1,4,7,-8,1,8,3,6,-7,-3,1,9,8,9,6,-8,-4,2,6,-2,5,8,-8,-2,-7,9,1,-5,7,8,-5,10,-1,-1,-4,3,7,-9,-6,-1,-8,-3,10,1,-2,-1,-3,6,-3,10,4,-9,5,-7,9,-7,10,-9,8,8,-6,8,-9,-3,5,-2,-9,9,8,-6,-4,5,3,-4,1,2,2,7,8,6,7,2,8,9,-7,-3,8,-5,-2,-1,-5,-10,-4,-10,1,6,3,-2,-9,-7,4,7,7,-2,-5,2,7,-6,-9,3,-10,5,-9,4,-8,6,2,5,-7,8,1,9,2,-8,2,10,-2,-7,4,9,-4,-7,10,8,10,-9,-6,8,6,8,7,9,-4,10,-8,3,6,10,3,-3,-4,3,-1,-7,-7,4,-6,3,9,-10,-4,1,-3,6,-9,-9,1,2,-5,10,7,-5,-9,2,4,9,5,10,10,-3,6,1,-8,-1,1,6,-7,10,-3,-8,-4,-7,-6,6,6,7,5,-1,-1,9,-4,-2,8,-1,-2,-8,-5,-5,3,-8,-3,8,3,3,2,7,-7,-10,-9,-5,-9,9,-7,4,-6,-8,-9,10,-6,7,-5,5,-3,8,-6,-5,10,-9,-8,9,-9,-6,-3,-2,9,8,-6,-7,-10,3,2,10,-3,8,-6,-7,4,-3,10,-6,9,-3,9,-3,7,-4,5,-10,5,-2,-7,-5,-4,5,-8,-3,5,1,7,2,2,-4,9,7,-4,-6,10,9,4,8,-7,8,-10,-5,-2,3,-2,-1,1,-7,-7,-5,4,10,7,9,-10,5,5,9,8,9,10,-1,10,-5,8,-3,-3,-2,3,-6,10,3,1,3,5,-9,4,6,-5,2,-3,10,7,8,-5,3,6,-3,1,6,9,-8,5,-8,7,4,4,5,5,-1,8,10,-3,2,-8,-7,4,-10,1,9,-8,5,-6,3,-6,6,10,9,-6,7,-9,-10,2,-4,-10,1,6,7,-8,7,-7,-9,6,2,1,5,4,7,-9,-10,-3,-6,7,-3,6,-9,3,-1,8,-1,3,-10,-5,-4,7,-3,5,9,5,-4,-4,-5,3,-3,9,9], dtype = "uint8")#candidate|8862|(728,)|const|uint8
call_8861 = relay.TupleGetItem(func_7141_call(relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), ), 0)
call_8863 = relay.TupleGetItem(func_7144_call(relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), ), 0)
func_5496_call = mod.get_global_var('func_5496')
func_5498_call = mutated_mod.get_global_var('func_5498')
call_8867 = func_5496_call()
call_8868 = func_5496_call()
func_546_call = mod.get_global_var('func_546')
func_549_call = mutated_mod.get_global_var('func_549')
call_8873 = relay.TupleGetItem(func_546_call(relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), ), 0)
call_8874 = relay.TupleGetItem(func_549_call(relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), relay.reshape(const_8862.astype('uint8'), [13, 4, 14]), ), 0)
func_5738_call = mod.get_global_var('func_5738')
func_5743_call = mutated_mod.get_global_var('func_5743')
var_8886 = relay.var("var_8886", dtype = "float64", shape = (45, 2))#candidate|8886|(45, 2)|var|float64
var_8887 = relay.var("var_8887", dtype = "uint64", shape = (1152,))#candidate|8887|(1152,)|var|uint64
call_8885 = relay.TupleGetItem(func_5738_call(relay.reshape(call_8861.astype('uint8'), [728,]), relay.reshape(var_8886.astype('float64'), [90,]), relay.reshape(var_8887.astype('uint64'), [1152,]), ), 1)
call_8888 = relay.TupleGetItem(func_5743_call(relay.reshape(call_8861.astype('uint8'), [728,]), relay.reshape(var_8886.astype('float64'), [90,]), relay.reshape(var_8887.astype('uint64'), [1152,]), ), 1)
func_7039_call = mod.get_global_var('func_7039')
func_7042_call = mutated_mod.get_global_var('func_7042')
var_8892 = relay.var("var_8892", dtype = "float32", shape = (198,))#candidate|8892|(198,)|var|float32
call_8891 = func_7039_call(relay.reshape(var_8892.astype('float32'), [9, 11, 2]), relay.reshape(var_8892.astype('float32'), [9, 11, 2]), )
call_8893 = func_7039_call(relay.reshape(var_8892.astype('float32'), [9, 11, 2]), relay.reshape(var_8892.astype('float32'), [9, 11, 2]), )
func_7696_call = mod.get_global_var('func_7696')
func_7700_call = mutated_mod.get_global_var('func_7700')
var_8923 = relay.var("var_8923", dtype = "bool", shape = (2, 336))#candidate|8923|(2, 336)|var|bool
call_8922 = relay.TupleGetItem(func_7696_call(relay.reshape(var_8886.astype('float64'), [90,]), relay.reshape(call_8885.astype('float64'), [1512,]), relay.reshape(var_8923.astype('bool'), [168, 4]), ), 5)
call_8924 = relay.TupleGetItem(func_7700_call(relay.reshape(var_8886.astype('float64'), [90,]), relay.reshape(call_8885.astype('float64'), [1512,]), relay.reshape(var_8923.astype('bool'), [168, 4]), ), 5)
var_8926 = relay.var("var_8926", dtype = "uint8", shape = (13, 4, 14))#candidate|8926|(13, 4, 14)|var|uint8
bop_8927 = relay.mod(call_8861.astype('float32'), relay.reshape(var_8926.astype('float32'), relay.shape_of(call_8861))) # shape=(13, 4, 14)
bop_8930 = relay.mod(call_8863.astype('float32'), relay.reshape(var_8926.astype('float32'), relay.shape_of(call_8863))) # shape=(13, 4, 14)
func_3036_call = mod.get_global_var('func_3036')
func_3040_call = mutated_mod.get_global_var('func_3040')
var_8934 = relay.var("var_8934", dtype = "float32", shape = (256,))#candidate|8934|(256,)|var|float32
var_8935 = relay.var("var_8935", dtype = "int32", shape = ())#candidate|8935|()|var|int32
call_8933 = relay.TupleGetItem(func_3036_call(relay.reshape(var_8934.astype('float32'), [8, 8, 4]), relay.reshape(var_8934.astype('float32'), [8, 8, 4]), relay.reshape(var_8935.astype('int32'), []), ), 4)
call_8936 = relay.TupleGetItem(func_3040_call(relay.reshape(var_8934.astype('float32'), [8, 8, 4]), relay.reshape(var_8934.astype('float32'), [8, 8, 4]), relay.reshape(var_8935.astype('int32'), []), ), 4)
func_1280_call = mod.get_global_var('func_1280')
func_1283_call = mutated_mod.get_global_var('func_1283')
var_8951 = relay.var("var_8951", dtype = "float64", shape = (360,))#candidate|8951|(360,)|var|float64
const_8952 = relay.const([[0.950695,-0.907789,-4.624883,8.266427,-3.701879,-7.009991,-5.446715,-5.463132,4.099314,-3.722659,4.718425,-0.144932,-7.027274,3.222692,6.660956,6.510827,-8.053949,0.973892,-3.914303,-8.205734,5.298554,2.215854,3.846079,6.876907,3.612804,2.294515,-1.156364,3.993460,9.338020,-5.641436,-9.851717,0.868857,2.273186,4.093959,-3.433307,-1.295849,-5.501908,9.899573,-3.086075,-9.529618,-9.036292,-6.456008,-2.636374,2.999304,-8.581903,-3.335846,1.489483,-7.877205,-4.782655,0.425108,9.624927,-1.870743,9.024386,7.579973,-6.000109,2.101811,7.989934,-6.472158,4.997275,-8.191539,4.572812,-5.681439,-3.541093,5.542843,-9.739268,4.279648,-5.617902,6.927548,9.896552,1.766226,3.806748,-2.371185,-3.639799,-1.559343,-7.870106,-1.214649,1.738723,4.170974,4.733412,-3.909839,5.501570,0.961290,6.582575,2.452969,-1.370090,-0.039334,-5.287843,-4.050010,1.101704,-9.526385,8.290556,2.253435,-4.857392,1.194632,1.756015,2.161710,3.412498,1.060671,-8.240913,-5.274690,4.948265,-7.635065,5.102867,8.283614,3.914082,7.387139,-7.300489,2.942428,6.931325,-3.584978,-0.867199,0.473053,-4.066703,-0.027182,6.608131,8.598768,0.346872,-8.087650,3.953817,-4.042875,-2.116787,4.385236,-4.309405,8.516857,8.986306,9.390276,7.539313,-1.531774,9.886283,-7.769788,1.359946,8.765766],[5.664769,9.440796,5.940005,3.811559,4.468881,-1.847788,1.278387,4.313543,6.045008,-1.091834,0.349948,6.839070,6.985171,-5.887587,6.695779,-7.425070,4.370587,6.129066,4.978642,-4.881170,-5.046150,-5.106471,-1.652459,-4.331580,-3.613012,7.556693,4.757725,-0.355615,-1.849046,8.460665,0.860359,9.132156,-4.315657,6.331372,0.783088,-3.937296,2.274549,-9.549513,2.500104,2.070451,5.233936,1.443310,0.159711,-2.118119,-7.660852,-4.004313,1.327660,3.316353,-3.266261,3.401709,-1.816254,9.127451,-3.225026,-7.419113,9.266887,-3.379101,-9.975048,2.804856,3.086670,1.856569,-7.015700,0.083173,7.670663,7.808113,-7.593237,-3.975311,-5.133282,-1.441836,9.905781,-5.988651,-8.765133,6.938187,7.536603,2.322216,-9.937443,-4.867491,-6.008020,-7.474611,-8.080060,9.781033,-8.200238,-3.613235,-8.831195,-5.204473,5.043043,-0.685146,1.487130,-1.304025,-8.134707,1.569801,-5.223398,6.992332,-1.371942,4.932924,1.104458,4.586348,-3.362325,5.451039,-0.464208,-8.122441,-2.205613,3.945427,-3.086403,-1.411496,9.099544,-8.307071,-7.840584,-9.420450,0.579462,6.606881,3.624044,2.165376,-7.627891,-4.969206,-6.754006,-6.857148,1.085138,-1.324160,9.365616,-8.317664,-2.297478,1.190581,3.565330,7.195476,4.670835,3.453241,6.487804,-1.426470,8.382260,-9.879196,6.083613,5.995989],[5.118400,-2.675651,-3.002133,2.065680,1.107155,3.645847,3.677318,-4.579164,-2.877453,2.462337,-9.663930,8.967626,-9.969568,8.895561,2.141199,-6.246724,-5.367219,0.914285,9.036138,9.853869,0.672228,2.389835,-9.047707,4.746645,-4.206747,-1.583673,-7.331993,-3.430342,-6.816152,-3.796499,-4.080545,-0.847409,-9.839498,-7.948384,-8.649782,-0.694583,-3.347508,-3.033618,3.913076,1.183634,-5.313919,-4.432262,-3.789534,9.491368,-8.179443,-5.395522,-5.923320,5.886048,-2.610885,5.734524,-6.539638,4.707961,8.751464,6.481478,7.379538,-3.550055,-1.224127,5.948691,-7.611866,9.320348,-5.006924,1.782198,-0.327523,3.293930,-8.139562,-6.701560,6.607390,-4.837607,7.620977,2.393305,-9.039222,5.668902,8.869305,4.447159,0.234735,-0.850896,-5.712971,1.938073,0.970321,-5.748746,7.522208,-9.353554,-3.604644,5.465751,-1.049209,-2.293738,3.559621,1.928481,-7.374073,-5.369436,-8.114726,-8.797890,-8.941095,9.492784,-9.479318,-7.886504,-2.930157,-2.394945,9.679553,8.764803,3.185079,-1.274349,7.805125,0.543649,9.120498,0.670120,-8.647157,-1.049594,3.575270,-1.024249,6.782169,5.604900,0.177301,-5.070730,-0.413855,-1.863251,-1.230310,-2.892871,1.398159,9.036123,5.498203,-7.694567,-3.510516,-0.361645,-0.672411,-2.816866,5.915344,-5.272571,0.989467,2.988522,-3.881787,9.519354],[4.579066,-8.541729,0.265978,8.224116,-3.196369,6.925435,-6.335237,0.490934,-9.531834,9.901209,7.069347,3.644799,-4.604620,-3.278490,-4.445265,3.730082,0.416173,-6.704945,-7.319691,6.514712,5.031995,0.582957,8.301489,8.747949,-7.491407,8.813117,-8.756969,2.403330,-3.423213,3.036266,6.922074,-6.730611,-5.722914,-0.406191,-1.882858,2.161687,-5.442364,5.420447,1.899500,5.538410,5.744251,-9.704006,5.487076,1.694374,7.697905,7.763338,0.176329,-0.622227,-2.567535,-2.608458,-0.573578,2.790546,0.187831,-3.126655,8.186400,-7.979892,6.876399,-5.453640,-1.970900,-6.193816,-0.173788,5.115074,5.525639,5.801255,-0.229355,-4.344115,8.594398,3.263681,-1.239957,-5.520622,6.620337,7.758668,1.871346,-5.610113,1.296205,4.212103,-2.058029,6.767716,-1.973492,8.984020,0.776243,-3.732956,2.553183,5.673330,9.551683,7.672996,-6.208050,0.282776,-4.377360,-7.966139,-2.255500,0.468084,-2.321411,-5.647473,7.422788,6.679865,1.575172,-8.649271,0.808535,6.109247,8.280305,3.743873,4.008854,9.824715,-3.494222,9.070868,6.315906,4.346643,8.731535,6.774781,-8.729112,7.398600,-5.815743,-0.392786,1.245855,-5.957516,6.310311,2.673346,5.473564,-7.778776,-8.034649,-4.523531,9.612610,0.283615,-2.725011,4.299926,1.430718,-6.105274,-0.974155,4.207543,-3.743532,-1.205128],[4.559108,-7.725609,-9.858613,7.990917,-1.891127,2.613630,1.664138,2.684771,8.337867,-1.428045,2.322401,-7.283151,-0.110999,-1.117032,0.582631,-1.356651,-0.874230,2.786389,6.316039,1.656823,3.467166,1.119404,8.486261,-5.957407,-3.478183,4.034239,7.122566,2.998166,7.756939,4.157420,1.420480,0.054392,-6.913909,-8.595835,5.450024,-0.304727,-7.012807,-0.107570,-7.689943,-6.166444,4.415723,-6.187630,5.516943,-7.946300,1.661464,-7.936072,7.154623,-7.565802,-4.038766,-3.601326,-4.659956,-2.291599,-5.526168,-9.824986,5.562830,8.485124,-9.171213,-2.667624,-9.979273,-3.069450,-6.411664,-6.908494,6.880005,9.560519,4.353678,6.213180,-1.760767,4.251509,-9.620068,2.935218,-4.869842,5.403476,5.267925,5.045669,-4.016575,4.498480,-0.703348,7.104791,8.392427,7.853806,-9.754315,-4.574671,7.916779,8.610680,-7.799089,7.481400,-6.562196,2.709516,-0.958668,8.316138,4.972025,5.835058,-5.099189,4.318802,-2.555885,-9.627039,3.752321,8.144360,-9.250732,7.786978,-2.701978,-7.675990,3.923986,-2.328680,-5.585102,-7.644491,-5.839665,0.814519,-7.926742,-3.943563,6.365210,4.472289,-3.578538,2.450831,-3.912870,0.418119,-0.580651,2.474740,0.443377,6.319093,1.542972,9.696730,-0.481004,-5.156401,8.748094,1.813810,8.788587,-3.405271,5.622710,9.621543,-8.713760,-1.087831],[-9.851048,-0.243833,6.467103,1.744752,7.407263,5.023157,2.576183,6.055254,-1.228911,5.474060,2.566483,0.513217,-7.092635,-0.759894,2.283890,5.658325,-8.139450,-9.502405,1.090678,-0.528405,-6.498120,-7.609690,6.420546,4.891175,-6.036398,-2.155765,-2.236601,6.915565,-3.960189,7.404880,-3.344867,0.667104,-2.874850,0.525292,1.354965,-6.806973,0.509633,0.861002,-0.319916,-0.655791,9.151280,0.008020,3.881959,-3.868596,-5.000385,7.639823,-9.753163,-7.437502,-3.118101,7.296492,7.721431,-4.439772,-8.870428,-4.691533,-4.621200,-3.497450,8.415072,0.616761,-4.099874,-4.813734,5.336497,4.301893,-7.412599,-0.411353,5.168533,-1.025008,9.151862,0.038929,-5.721715,5.898408,7.413821,-0.651627,9.448187,5.804380,-7.059523,-2.368292,0.662046,5.078255,0.351383,9.498636,6.706391,-1.308364,-4.790751,1.924830,6.584958,5.877542,-3.354458,2.031986,5.653459,8.665748,-0.605770,0.115127,0.862140,9.444857,-3.342948,-6.052935,-9.931358,-7.305604,-4.934512,7.723495,-1.074748,-9.427932,-9.635686,-1.796584,-7.728411,9.305653,-1.679295,1.590100,-4.275710,-3.088725,8.922414,-5.714394,2.663293,-3.378492,-5.432239,3.474986,-6.294721,0.803940,0.030188,-7.879713,8.591798,-7.312559,-4.675165,-1.516188,-4.801761,8.759561,9.196118,6.357747,-8.686404,-1.581741,8.762200,-7.962531],[-4.399077,8.357993,3.894007,7.294005,5.266200,-4.249154,0.193547,-4.149011,-4.056306,9.508381,-8.191627,-1.755147,-7.418975,0.695755,4.665460,0.122526,-9.084092,7.876669,-7.786105,-1.026617,9.216816,8.413964,4.101531,-1.453626,7.508817,0.165645,4.415516,7.810004,6.661405,3.084889,-1.702337,-5.085511,9.963020,-3.358764,-7.302441,-3.201641,-9.564896,0.532976,5.459015,2.469839,9.413913,-1.117807,-0.853026,4.113883,3.891363,-8.217960,6.569099,-7.496894,5.348169,2.509467,0.713622,4.310325,8.683994,-4.025351,-6.919669,-0.625968,-3.262521,-9.751365,-4.450044,-8.750708,7.776431,9.329999,5.420005,8.532880,-1.198462,7.324244,-5.027252,3.406332,9.291915,3.733242,0.158897,9.642680,-0.787304,3.662298,1.397925,-5.010741,-6.690623,-0.014565,7.106132,-5.830320,-9.532500,-8.850883,-2.549629,-6.211481,3.197601,-0.936258,0.405199,-7.669197,1.386054,-1.199157,-4.200347,8.195911,-3.959837,-7.378380,-7.938321,-3.648649,-7.687948,5.278167,-4.543396,-2.854487,6.333523,9.777896,4.967675,1.854235,1.950885,3.799764,-1.887119,-7.772221,-6.741992,7.206798,-9.517881,3.230979,-5.488008,0.040478,8.429807,-5.455252,-8.246281,4.623162,4.958241,8.690044,5.202008,-9.674920,8.526397,-8.537646,-7.947256,-9.507870,1.872457,9.120145,5.225025,6.826076,8.627788,5.436430]], dtype = "float64")#candidate|8952|(7, 132)|const|float64
call_8950 = relay.TupleGetItem(func_1280_call(relay.reshape(var_8951.astype('float64'), [9, 10, 4]), relay.reshape(const_8952.astype('float64'), [154, 6]), ), 0)
call_8953 = relay.TupleGetItem(func_1283_call(relay.reshape(var_8951.astype('float64'), [9, 10, 4]), relay.reshape(const_8952.astype('float64'), [154, 6]), ), 0)
func_5389_call = mod.get_global_var('func_5389')
func_5394_call = mutated_mod.get_global_var('func_5394')
var_8960 = relay.var("var_8960", dtype = "bool", shape = (2, 168))#candidate|8960|(2, 168)|var|bool
call_8959 = relay.TupleGetItem(func_5389_call(relay.reshape(call_8885.astype('float64'), [1512,]), relay.reshape(var_8960.astype('bool'), [336,]), relay.reshape(var_8887.astype('uint64'), [1152,]), relay.reshape(var_8935.astype('int32'), []), ), 2)
call_8961 = relay.TupleGetItem(func_5394_call(relay.reshape(call_8885.astype('float64'), [1512,]), relay.reshape(var_8960.astype('bool'), [336,]), relay.reshape(var_8887.astype('uint64'), [1152,]), relay.reshape(var_8935.astype('int32'), []), ), 2)
output = relay.Tuple([call_8852,const_8862,call_8867,call_8873,call_8885,var_8886,var_8887,call_8891,var_8892,call_8922,var_8923,bop_8927,call_8933,var_8934,var_8935,call_8950,var_8951,const_8952,call_8959,var_8960,])
output2 = relay.Tuple([call_8853,const_8862,call_8868,call_8874,call_8888,var_8886,var_8887,call_8893,var_8892,call_8924,var_8923,bop_8930,call_8936,var_8934,var_8935,call_8953,var_8951,const_8952,call_8961,var_8960,])
func_8964 = relay.Function([var_8886,var_8887,var_8892,var_8923,var_8926,var_8934,var_8935,var_8951,var_8960,], output)
mod['func_8964'] = func_8964
mod = relay.transform.InferType()(mod)
mutated_mod['func_8964'] = func_8964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8964_call = mutated_mod.get_global_var('func_8964')
var_8966 = relay.var("var_8966", dtype = "float64", shape = (45, 2))#candidate|8966|(45, 2)|var|float64
var_8967 = relay.var("var_8967", dtype = "uint64", shape = (1152,))#candidate|8967|(1152,)|var|uint64
var_8968 = relay.var("var_8968", dtype = "float32", shape = (198,))#candidate|8968|(198,)|var|float32
var_8969 = relay.var("var_8969", dtype = "bool", shape = (2, 336))#candidate|8969|(2, 336)|var|bool
var_8970 = relay.var("var_8970", dtype = "uint8", shape = (13, 4, 14))#candidate|8970|(13, 4, 14)|var|uint8
var_8971 = relay.var("var_8971", dtype = "float32", shape = (256,))#candidate|8971|(256,)|var|float32
var_8972 = relay.var("var_8972", dtype = "int32", shape = ())#candidate|8972|()|var|int32
var_8973 = relay.var("var_8973", dtype = "float64", shape = (360,))#candidate|8973|(360,)|var|float64
var_8974 = relay.var("var_8974", dtype = "bool", shape = (2, 168))#candidate|8974|(2, 168)|var|bool
call_8965 = func_8964_call(var_8966,var_8967,var_8968,var_8969,var_8970,var_8971,var_8972,var_8973,var_8974,)
output = call_8965
func_8975 = relay.Function([var_8966,var_8967,var_8968,var_8969,var_8970,var_8971,var_8972,var_8973,var_8974,], output)
mutated_mod['func_8975'] = func_8975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3182_call = mod.get_global_var('func_3182')
func_3183_call = mutated_mod.get_global_var('func_3183')
call_9025 = func_3182_call()
call_9026 = func_3182_call()
func_8535_call = mod.get_global_var('func_8535')
func_8537_call = mutated_mod.get_global_var('func_8537')
call_9029 = func_8535_call()
call_9030 = func_8535_call()
func_4417_call = mod.get_global_var('func_4417')
func_4418_call = mutated_mod.get_global_var('func_4418')
call_9036 = relay.TupleGetItem(func_4417_call(), 0)
call_9037 = relay.TupleGetItem(func_4418_call(), 0)
func_6243_call = mod.get_global_var('func_6243')
func_6244_call = mutated_mod.get_global_var('func_6244')
call_9041 = relay.TupleGetItem(func_6243_call(), 0)
call_9042 = relay.TupleGetItem(func_6244_call(), 0)
func_7640_call = mod.get_global_var('func_7640')
func_7642_call = mutated_mod.get_global_var('func_7642')
call_9058 = relay.TupleGetItem(func_7640_call(), 2)
call_9059 = relay.TupleGetItem(func_7642_call(), 2)
func_6309_call = mod.get_global_var('func_6309')
func_6310_call = mutated_mod.get_global_var('func_6310')
call_9072 = func_6309_call()
call_9073 = func_6309_call()
bop_9098 = relay.maximum(call_9072.astype('uint16'), relay.reshape(call_9025.astype('uint16'), relay.shape_of(call_9072))) # shape=(8, 15, 4)
bop_9101 = relay.maximum(call_9073.astype('uint16'), relay.reshape(call_9026.astype('uint16'), relay.shape_of(call_9073))) # shape=(8, 15, 4)
output = relay.Tuple([call_9029,call_9036,call_9041,call_9058,bop_9098,])
output2 = relay.Tuple([call_9030,call_9037,call_9042,call_9059,bop_9101,])
func_9102 = relay.Function([], output)
mod['func_9102'] = func_9102
mod = relay.transform.InferType()(mod)
output = func_9102()
func_9103 = relay.Function([], output)
mutated_mod['func_9103'] = func_9103
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9136 = relay.var("var_9136", dtype = "uint16", shape = ())#candidate|9136|()|var|uint16
var_9137 = relay.var("var_9137", dtype = "uint16", shape = (8, 12, 11))#candidate|9137|(8, 12, 11)|var|uint16
bop_9138 = relay.greater_equal(var_9136.astype('bool'), var_9137.astype('bool')) # shape=(8, 12, 11)
func_7279_call = mod.get_global_var('func_7279')
func_7280_call = mutated_mod.get_global_var('func_7280')
call_9144 = func_7279_call()
call_9145 = func_7279_call()
output = relay.Tuple([bop_9138,call_9144,])
output2 = relay.Tuple([bop_9138,call_9145,])
func_9146 = relay.Function([var_9136,var_9137,], output)
mod['func_9146'] = func_9146
mod = relay.transform.InferType()(mod)
var_9147 = relay.var("var_9147", dtype = "uint16", shape = ())#candidate|9147|()|var|uint16
var_9148 = relay.var("var_9148", dtype = "uint16", shape = (8, 12, 11))#candidate|9148|(8, 12, 11)|var|uint16
output = func_9146(var_9147,var_9148,)
func_9149 = relay.Function([var_9147,var_9148,], output)
mutated_mod['func_9149'] = func_9149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5315_call = mod.get_global_var('func_5315')
func_5316_call = mutated_mod.get_global_var('func_5316')
call_9156 = func_5315_call()
call_9157 = func_5315_call()
func_7141_call = mod.get_global_var('func_7141')
func_7144_call = mutated_mod.get_global_var('func_7144')
const_9162 = relay.const([[10,-2,6,3],[2,-5,-4,-2],[-1,3,9,10],[-7,-6,4,6],[5,-6,-8,8],[-3,-9,-3,-3],[-1,6,2,5],[-10,10,10,-9],[6,4,4,-3],[9,4,-4,-4],[5,6,5,-7],[-4,-10,5,-7],[-5,-2,-7,8],[9,-7,10,10],[3,-3,9,3],[8,-6,-3,3],[-6,-8,2,-8],[-7,5,-6,5],[3,8,-7,-3],[-6,-10,-2,8],[-10,2,2,6],[-4,-1,6,-10],[1,8,10,-4],[2,5,9,-3],[-10,2,6,-5],[8,1,-1,4],[-8,1,6,4],[1,4,-5,-8],[4,8,9,10],[-1,-3,1,-4],[2,7,-1,7],[-10,-2,8,9],[2,-1,3,8],[10,6,-1,-10],[-4,-2,-8,6],[10,3,8,1],[1,8,-1,10],[10,-5,-4,5],[-4,2,-7,-1],[6,6,-8,-1],[9,5,-10,3],[8,-2,-5,-10],[-3,2,-3,-9],[-7,-3,4,-5],[7,-2,2,-6],[5,3,-4,-10],[7,9,5,1],[4,8,-9,-10],[-1,-3,8,-3],[7,3,-1,10],[-5,8,-6,-1],[-4,-8,-3,1],[-1,-9,6,-3],[10,-6,-9,6],[5,3,4,4],[4,-3,2,-1],[8,3,-3,-7],[-2,-1,9,-4],[-5,6,2,7],[1,3,4,6],[7,6,-6,1],[7,-9,-1,-9],[-10,6,-4,-8],[-5,-8,-8,-10],[6,4,-8,9],[9,10,-3,-8],[5,-4,9,1],[6,2,6,8],[-6,3,7,9],[-2,-8,1,7],[-10,-2,5,-2],[5,-5,-5,-2],[-3,-5,8,8],[7,4,-10,2],[4,-8,9,1],[5,6,7,1],[2,-4,-1,10],[-6,6,9,-7],[-3,-3,-6,-6],[-8,-1,10,-9],[-9,5,-3,8],[1,-7,-3,5],[-9,8,-1,-8],[-9,-8,-2,-3],[7,-9,-3,2],[-4,-6,3,-2],[-10,-10,5,1],[-9,-2,5,-10],[-1,5,-9,-10],[5,-9,-9,-1],[-9,9,-10,-7],[1,-8,3,9],[8,-2,10,-9],[9,-3,8,7],[-6,-1,-9,3],[-8,-8,-10,8],[2,4,-1,-9],[10,-1,8,4],[-6,-10,5,-7],[-6,-3,2,4],[-1,-8,-1,5],[10,8,5,2],[8,6,-9,8],[8,4,3,5],[-6,8,-9,7],[-10,7,-8,7],[-3,1,6,9],[-1,3,9,-1],[9,2,-2,-7],[-5,-8,-3,1],[7,-10,-1,4],[-2,-9,-5,5],[10,3,-8,6],[5,6,-10,6],[9,10,-6,6],[-3,8,5,-1],[-3,-1,-5,4],[-3,-7,-7,10],[-10,-8,7,2],[-8,8,-4,-10],[-5,9,8,-9],[-4,-3,1,7],[-6,-6,8,2],[10,9,3,2],[8,10,-5,-6],[7,-9,5,-10],[10,3,-7,4],[-7,3,10,-7],[-9,6,-8,-2],[-6,-3,-9,-1],[10,9,-10,-5],[5,8,5,6],[4,7,-8,7],[2,-4,-5,-1],[10,-4,-4,9],[9,5,-5,-6],[-6,-1,4,8],[-9,6,-5,1],[-1,-6,-6,-4],[-4,-8,1,8],[-9,-2,8,-8],[2,5,2,-5],[-2,8,7,2],[-3,10,6,-3],[-8,7,-7,-7],[8,-8,-7,-3],[-5,-7,-5,4],[1,1,-2,4],[1,8,-4,-9],[-4,-3,10,-1],[9,7,-9,9],[3,-9,6,6],[5,-5,10,3],[1,-6,4,-5],[-5,6,-1,8],[-6,-10,-2,-10],[-2,-8,-1,6],[-7,-2,-10,-5],[-1,-3,-5,-8],[-7,3,-9,-6],[8,-3,3,10],[4,2,-2,2],[-7,6,3,-4],[4,-10,10,4],[-8,-8,8,4],[1,9,4,-7],[-6,4,8,-2],[3,5,-9,-3],[8,9,-1,-10],[-10,8,-2,-4],[7,-10,6,-7],[-7,4,1,-3],[9,5,-9,-2],[5,3,-4,-8],[5,-6,-3,1],[5,-5,5,5],[2,-3,4,9],[7,9,-9,4],[6,-6,-5,6],[-4,-8,9,-2],[1,3,5,7],[4,-3,10,8]], dtype = "uint8")#candidate|9162|(182, 4)|const|uint8
call_9161 = relay.TupleGetItem(func_7141_call(relay.reshape(const_9162.astype('uint8'), [13, 4, 14]), relay.reshape(const_9162.astype('uint8'), [13, 4, 14]), ), 0)
call_9163 = relay.TupleGetItem(func_7144_call(relay.reshape(const_9162.astype('uint8'), [13, 4, 14]), relay.reshape(const_9162.astype('uint8'), [13, 4, 14]), ), 0)
func_5738_call = mod.get_global_var('func_5738')
func_5743_call = mutated_mod.get_global_var('func_5743')
const_9171 = relay.const([7.349726,-3.294289,7.819556,-1.262021,-8.314266,-0.470270,3.184801,2.697582,-1.193722,-8.284648,2.249717,1.692253,-2.162366,6.101810,-6.364706,-8.048824,-7.012969,9.997451,-4.277583,1.479045,-9.912737,-1.881193,9.424829,8.967820,5.699938,-6.850720,5.994160,-2.226450,-2.733219,0.642519,-7.674427,-4.139027,-2.670070,-6.172738,6.351929,7.182738,3.281390,-5.694999,8.130808,-0.355917,7.376282,6.807315,-1.161255,-2.906621,-9.830912,8.925943,0.338158,0.604091,8.045842,-3.441969,4.089000,-8.813449,6.820144,3.964603,-7.037686,-9.609285,-4.813174,-4.810689,2.745306,3.227966,-1.204660,-8.825008,-0.330318,9.981954,7.947453,-6.889228,2.620133,4.124034,0.344655,-8.386406,7.364737,3.431874,-3.392798,-6.042926,-1.834741,1.574764,5.901574,-0.405133,5.822903,8.946401,4.375622,6.230951,5.230815,-7.561266,3.213646,-7.842269,9.490855,-7.169853,-2.650572,2.409179], dtype = "float64")#candidate|9171|(90,)|const|float64
var_9172 = relay.var("var_9172", dtype = "uint64", shape = (1152,))#candidate|9172|(1152,)|var|uint64
call_9170 = relay.TupleGetItem(func_5738_call(relay.reshape(const_9162.astype('uint8'), [728,]), relay.reshape(const_9171.astype('float64'), [90,]), relay.reshape(var_9172.astype('uint64'), [1152,]), ), 7)
call_9173 = relay.TupleGetItem(func_5743_call(relay.reshape(const_9162.astype('uint8'), [728,]), relay.reshape(const_9171.astype('float64'), [90,]), relay.reshape(var_9172.astype('uint64'), [1152,]), ), 7)
output = relay.Tuple([call_9156,call_9161,const_9162,call_9170,const_9171,var_9172,])
output2 = relay.Tuple([call_9157,call_9163,const_9162,call_9173,const_9171,var_9172,])
func_9177 = relay.Function([var_9172,], output)
mod['func_9177'] = func_9177
mod = relay.transform.InferType()(mod)
mutated_mod['func_9177'] = func_9177
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9178 = relay.var("var_9178", dtype = "uint64", shape = (1152,))#candidate|9178|(1152,)|var|uint64
func_9177_call = mutated_mod.get_global_var('func_9177')
call_9179 = func_9177_call(var_9178)
output = call_9179
func_9180 = relay.Function([var_9178], output)
mutated_mod['func_9180'] = func_9180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5927_call = mod.get_global_var('func_5927')
func_5928_call = mutated_mod.get_global_var('func_5928')
call_9257 = relay.TupleGetItem(func_5927_call(), 0)
call_9258 = relay.TupleGetItem(func_5928_call(), 0)
output = call_9257
output2 = call_9258
func_9261 = relay.Function([], output)
mod['func_9261'] = func_9261
mod = relay.transform.InferType()(mod)
output = func_9261()
func_9262 = relay.Function([], output)
mutated_mod['func_9262'] = func_9262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_9271 = relay.TupleGetItem(func_3274_call(), 0)
call_9272 = relay.TupleGetItem(func_3275_call(), 0)
output = call_9271
output2 = call_9272
func_9288 = relay.Function([], output)
mod['func_9288'] = func_9288
mod = relay.transform.InferType()(mod)
mutated_mod['func_9288'] = func_9288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9288_call = mutated_mod.get_global_var('func_9288')
call_9289 = func_9288_call()
output = call_9289
func_9290 = relay.Function([], output)
mutated_mod['func_9290'] = func_9290
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9301 = relay.var("var_9301", dtype = "float64", shape = (13, 16, 7))#candidate|9301|(13, 16, 7)|var|float64
uop_9302 = relay.log2(var_9301.astype('float64')) # shape=(13, 16, 7)
uop_9305 = relay.sqrt(var_9301.astype('float32')) # shape=(13, 16, 7)
bop_9310 = relay.right_shift(var_9301.astype('uint16'), relay.reshape(uop_9302.astype('uint16'), relay.shape_of(var_9301))) # shape=(13, 16, 7)
func_8222_call = mod.get_global_var('func_8222')
func_8223_call = mutated_mod.get_global_var('func_8223')
call_9317 = relay.TupleGetItem(func_8222_call(), 0)
call_9318 = relay.TupleGetItem(func_8223_call(), 0)
output = relay.Tuple([uop_9305,bop_9310,call_9317,])
output2 = relay.Tuple([uop_9305,bop_9310,call_9318,])
func_9319 = relay.Function([var_9301,], output)
mod['func_9319'] = func_9319
mod = relay.transform.InferType()(mod)
var_9320 = relay.var("var_9320", dtype = "float64", shape = (13, 16, 7))#candidate|9320|(13, 16, 7)|var|float64
output = func_9319(var_9320)
func_9321 = relay.Function([var_9320], output)
mutated_mod['func_9321'] = func_9321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5768_call = mod.get_global_var('func_5768')
func_5770_call = mutated_mod.get_global_var('func_5770')
call_9345 = func_5768_call()
call_9346 = func_5768_call()
func_7858_call = mod.get_global_var('func_7858')
func_7859_call = mutated_mod.get_global_var('func_7859')
call_9358 = relay.TupleGetItem(func_7858_call(), 0)
call_9359 = relay.TupleGetItem(func_7859_call(), 0)
func_5151_call = mod.get_global_var('func_5151')
func_5152_call = mutated_mod.get_global_var('func_5152')
call_9371 = relay.TupleGetItem(func_5151_call(), 0)
call_9372 = relay.TupleGetItem(func_5152_call(), 0)
output = relay.Tuple([call_9345,call_9358,call_9371,])
output2 = relay.Tuple([call_9346,call_9359,call_9372,])
func_9374 = relay.Function([], output)
mod['func_9374'] = func_9374
mod = relay.transform.InferType()(mod)
mutated_mod['func_9374'] = func_9374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9374_call = mutated_mod.get_global_var('func_9374')
call_9375 = func_9374_call()
output = call_9375
func_9376 = relay.Function([], output)
mutated_mod['func_9376'] = func_9376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6933_call = mod.get_global_var('func_6933')
func_6934_call = mutated_mod.get_global_var('func_6934')
call_9403 = func_6933_call()
call_9404 = func_6933_call()
output = relay.Tuple([call_9403,])
output2 = relay.Tuple([call_9404,])
func_9405 = relay.Function([], output)
mod['func_9405'] = func_9405
mod = relay.transform.InferType()(mod)
output = func_9405()
func_9406 = relay.Function([], output)
mutated_mod['func_9406'] = func_9406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7640_call = mod.get_global_var('func_7640')
func_7642_call = mutated_mod.get_global_var('func_7642')
call_9467 = relay.TupleGetItem(func_7640_call(), 1)
call_9468 = relay.TupleGetItem(func_7642_call(), 1)
func_8784_call = mod.get_global_var('func_8784')
func_8787_call = mutated_mod.get_global_var('func_8787')
const_9470 = relay.const([-0.163553,-4.687391,-0.853727,-2.114282,-3.929948,6.621250,-0.333130,0.018551,9.286185,6.933360,-3.422370,2.871182,3.306479,-4.861497,-0.245709,-8.995542,-8.487748,-9.543404,9.138189,4.803709,-3.141923,-0.631665,3.573139,-6.033501,5.656975,2.576896,-9.803606,-5.597819,-1.519718,-9.608986,2.852543,-0.268833,-8.388142,-0.437839,3.385903,2.147418,-8.932519,-2.463961,-5.058481,0.145291,-6.478527,3.325135,4.270545,6.589021,8.714397,-1.384783,-1.020909,-0.963113,1.636111,-7.406384,-6.805186,0.684342,-8.165285,-8.958849,-2.221096,-7.278376,9.684123,3.826189,8.830911,-2.772705,-2.468246,1.376775,5.472392,4.560748,-0.178219,8.420720,-8.284497,-1.742060,-5.923367,5.330791,-0.900186,-4.061238,1.948923,-8.184104,-3.277844,3.916581,-1.339263,0.865767,7.152546,-4.511364,-8.486631,-4.589111,-9.531167,3.828261,-5.173658,3.437699,1.344521,-2.672238,0.849435,3.425211,6.180102,8.922138,-5.899938,-1.805670,4.792453,1.940770,-7.922255,-9.859509,-5.526749,-2.163559,-8.753206,3.852776,9.877028,6.521634,0.142098,-1.832722,2.581592,-1.047144,-4.880086,9.563328,6.685757,8.061360,8.459365,7.381954,-1.568847,-9.855033,3.501630,-4.084966,8.260353,-5.435457,-8.147935,9.187371,-7.136102,9.785762,-7.613647,-9.154919,-5.207327,-5.219481,-4.676722,5.207536,7.990564,4.271396,-9.345464,0.864013,1.505031,-2.934538,-4.330068,-9.682691,2.168272,4.044995,-0.958215,7.453162,0.172108,-7.311826,9.443435,-7.960033,5.183535,-5.349713,6.386038,7.516215,9.128067,2.824791,-2.810098,-6.444102,4.668269,7.606472,2.863997,-4.565260,-7.079158,-3.271596,7.765394,-7.230738,4.722255,-6.984166,-9.123763,8.100127,4.443087,2.607646,-7.272607,8.063861,5.680774,-8.383253,5.514611,-6.077503,2.741142,-5.712842,3.776617,-7.234613,4.726260,-7.891280,-5.073967,7.716375,-9.026858,7.597459,-0.138968,-3.098534,-2.861391,-2.166392,-6.368137,6.150112,-8.577104,-3.063881,8.641505,-5.942537,3.459200,-8.819937,-4.304126,6.191870,0.852021,-6.851712,1.724183,7.243672,5.471645,7.081022,-8.586391,3.227068,-6.067725,4.082527,-3.448527,-1.918609,-9.793816,-0.980264,-8.612567,2.990273,-7.158550,1.187351,-7.134229,8.964422,6.457940,1.930579,-0.653561,-6.088523,-1.258307,-1.011689,1.996488,-6.381700,3.094278,-8.545957,-6.904438,7.605217,3.574562,-4.383258,-6.191057,9.951311,5.645132,7.202155,-0.604389,-2.061219,0.902295,8.779364,-3.777534,-3.621166,-1.089014,1.970785,-2.253815,-6.879978,-8.013488,-8.459194,-5.121842,-7.495994,-1.484951,5.919450,0.061349,-1.756645,-7.552798,9.494077,5.454413,0.988842,-6.210557,0.325801,8.083499,5.049605,-8.617626,-0.934750,4.368486,-2.540059,1.648093,-9.018670,-7.577495,0.870995,4.252243,4.028997,0.653981,-6.876996,8.555424,-5.001614,9.412093,-4.356905,7.752254,2.174391,2.510684,7.351857,2.984754,5.020355,-7.025984,7.379532,6.249481,-8.373739,3.280754,9.183452,-3.036139,6.924321,8.989311,-3.580360,5.607026,8.008351,9.068798,3.320456,2.493591,-1.893884,8.082495,5.159648,-8.261358,8.253493,-4.245516,5.802745,6.933835,7.355493,-0.751816,0.448632,4.107054,8.073577,5.432245,3.278379,9.850881,-4.963370,6.600845,-3.816062,-7.797127,7.973874,-2.653899,7.632430,-4.664832,-4.643135,-9.001289,-7.499797,-7.879715,6.968180,-1.584807,-9.367648,-4.072915,-7.379650,-4.004375,-1.105583,8.237664,-5.972120,-1.940210,3.790412,-2.225661,7.187140,9.051474,-5.257157,8.282945,-8.723236,-3.250984,-7.237469,3.876961,1.565665,0.732891,-8.043073,6.465944,-8.687140,2.372567,-6.150481,1.571321,-2.564099,9.343482,-9.339731,-2.839065,-9.500292,-8.602678,-5.465858,-4.714220,4.492201,4.909776,-2.702134,-4.260080,-1.173470,-8.554016,0.366066,-5.149536,-4.899917,-6.275912,8.227073,7.555876,-2.297745,-3.572194,-2.431787,-0.160584,-8.874355,3.861125,-2.575989,7.533751,7.972550,-7.690983,0.909202,9.901329,-7.741949,-0.046120,-5.354596,-0.501239,6.057793,5.456967,5.308694,-8.232866,2.217910,-7.603031,5.422267,-8.930892,5.617927,-3.746954,-3.574280,-9.482470,1.243695,-1.357265,5.464462,-4.148433,1.985785,-8.168328,1.165795,-7.564747,-9.286379,6.675517,-2.159939,6.811831,-8.639486,-6.765624,8.060030,8.665671,5.136479,-2.827037,-6.212201,-9.625834,2.112502,-8.512026,9.335565,2.712492,8.961190,2.800105,0.748931,3.139157,-6.357352,-8.269676,3.302106,1.945366,9.685174,2.230549,-1.996887,3.153449,-1.526579,1.603756,-6.051455,5.376167,6.671964,3.695555,2.327328,-5.878628,-0.237769,1.675119,-8.222295,-8.063625,2.743243,-0.746268,6.073538,4.850313,5.159079,4.033647,1.184859,-4.227896,-8.304046,6.602108,-9.896412,4.058733,-3.421891,-7.073026,0.270969,-5.196125,-5.595629,4.753289,-8.773529,9.650968,1.676598,7.282852,-5.811018,6.302660,9.993474,-8.481731,-5.340933,-1.034872,1.127499,2.247744,-8.538022,5.281759,-5.520326,-2.130829,3.450292,5.616373,9.336162,9.096299,-1.118939,-3.958883,-5.719193,6.159069,-0.751736,2.220059,0.170883,1.254693,1.899742,-3.070224,0.996194,-1.478659,6.783543,6.805842,3.507578,-4.325749,7.324827,5.095343,6.945769,-5.120759,7.100526,0.462556,-0.227918,-5.810462,0.300080,-3.077255,4.216637,9.293122,-9.300719,8.752177,-2.467052,3.409965,-2.606033,4.723800,1.637664,-5.542739,6.147841,6.938584,-4.866897,0.434844,6.277399,-1.898336,6.499217,5.392867,-9.909273,6.487655,-5.466592,-3.488274,1.937926,-0.450788,2.407110,0.334916,6.437761,-5.892976,-6.714006,7.862272,3.156509,8.797139,-1.549429,-3.964729,8.647514,7.184984,-0.792181,6.609037,9.369399,0.771239,-2.647026,1.948514,6.327962,8.444037,-1.195251,2.598575,-8.047804,-1.090326,7.423987,8.776005,-3.286653,-4.912668,-1.498643,-2.168393,-9.199768,-2.263070,2.664522,-2.634906,0.559135,-2.742524,-8.039695,-6.151370,-4.422951,2.432766,3.096386,6.056070,0.723551,8.855486,7.187951,8.969802,5.442423,-6.513963,-6.144724,4.521846,-4.074016,7.100928,-1.428768,8.686934,-9.019489,-8.073098,3.669926,1.225757,-1.311970,-9.613583,-6.458161,2.183130,8.237938,-2.545446,-1.006164,8.981745,-8.528715,1.918660,-2.396567,1.208773,-9.827207,8.961049,0.635867,-3.480456,4.248777,0.974352,6.524571,4.691744,-0.951332,-2.628434,8.434631,1.902502,-4.065010,-2.259266,3.788831,0.274647,-9.055150,9.954723,5.295056,7.993585,-2.577518,-9.650835,8.013823,-7.873104,-5.628950,-2.572045,3.575958,9.361348,-3.430760,-1.974483,5.699275,8.330584,-6.131226,-3.986132,1.043958,-4.752334,-9.029129,5.981523,-7.753838,-2.269251,-1.867546,2.997766,-4.139121,4.689324,-1.698986,4.292190,6.439667,4.139321,8.515133,4.704318,6.397315,0.004386,-8.252562,0.399872,-1.549720,7.265607,-7.340452,-8.420315,1.428949,-6.116371,-7.698874,-1.907310,-4.006659,4.648831,8.573110,-9.111460,4.910529,-5.808429,-5.791875,-2.365925,4.069392,8.739567,-4.956917,2.122981,2.836875,-5.119904,8.568695,6.930802,-2.808873,9.553541,1.949301,8.308940,3.506728,8.809594,7.116291,5.588711,8.402550,2.233298,-2.185903,-6.344976,-0.276422,8.370950,9.175299,4.757873,-2.762570,8.736144,8.769459,-6.501902,-8.849321,-3.685533,6.165154,7.970256,8.950611,3.685932,7.825038,0.947687,-3.980385,5.486373,-3.687592,4.397481,8.003322,-4.805606,3.975248,-0.390358,-7.231709,-6.394912,-5.328974,6.073854,-8.323940,2.540752,-1.723541,3.230427,-5.435001,-3.564288,1.634209,5.957695,-4.468331,2.429639,-1.143602,3.643072,6.368448,-0.770829,5.543224,0.990198,-9.578235,6.908233,0.680780,3.420656,3.325728,-1.572599,-4.994002,-0.731178,-9.129437,-6.489602,5.537608,8.885350,5.213691,-1.591927,6.935622,-0.323323,-7.888374,-7.072735,-1.840785,5.199549,9.593048,9.810167,3.099337,-7.717242,3.398338,-5.587273,6.901436,4.954829,-2.465332,2.822580,0.513018,5.496295,-6.475441,-5.272371,-1.132496,-5.859967,1.352306,9.543650,5.450097,-9.963583,-8.927523,3.216577,1.062371,4.340974,-8.238500,4.157004,-5.666143,-0.561134,5.823931,-2.498408,-5.059394,1.633323,-1.972922,5.724823,4.716536,-8.245691,-3.113930,9.223738,5.606345,4.361575,6.873982,9.538865,-7.313362,-4.021834,-3.988417,4.473237,-5.119027,2.005954,2.499354,-7.529273,-8.284696,-9.818190,1.150273,-5.028073,-2.430450,-9.431518,3.093257,-0.337881,1.599527,2.652131,5.523370,5.175609,2.904512,-7.558703,4.043397,5.304781,5.347291,-9.518418,1.869106,5.576611,5.508116,-5.675273,-9.760470,-9.735865,8.379018,5.665790,-9.791553,-4.801927,4.498569,-2.847649,-7.767927,0.581317,1.911187,-2.091130,-5.469735,6.267368,4.690877,-8.157741,-1.033020,-7.588526,-6.007952,-4.150526,-3.496550,7.159299,5.843282,-0.198388,7.658618,3.323861,8.100156,-1.923741,-7.543344,6.485233,1.482092,9.754259,-0.317808,1.403068,4.051211,5.496181,6.945322,-9.468603,-9.355895,-9.916442,-4.367939,7.446903,5.975360,0.339425,6.704314,2.523158,9.676482,-9.619781,-1.279640,-3.831449,5.962303,6.600338,-3.433712,5.001953,-0.899162,1.640420,5.196329,1.022782,-5.483127,-3.600284,9.174024,-8.892285,-3.291047,0.973580,-7.626604,9.268855,0.689690,-4.855863,-5.955238,4.116507,0.052040,2.051575,1.654804,2.209667,3.253607,4.993363,-6.952898,1.191831,-3.573503,1.195505,8.439848,-3.396211,-9.964793,-9.400399,-3.645546,9.614373,-8.281112,-3.694065,6.268372], dtype = "float64")#candidate|9470|(924,)|const|float64
call_9469 = relay.TupleGetItem(func_8784_call(relay.reshape(const_9470.astype('float64'), [462, 2])), 2)
call_9471 = relay.TupleGetItem(func_8787_call(relay.reshape(const_9470.astype('float64'), [462, 2])), 2)
output = relay.Tuple([call_9467,call_9469,const_9470,])
output2 = relay.Tuple([call_9468,call_9471,const_9470,])
func_9482 = relay.Function([], output)
mod['func_9482'] = func_9482
mod = relay.transform.InferType()(mod)
output = func_9482()
func_9483 = relay.Function([], output)
mutated_mod['func_9483'] = func_9483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_9499 = func_5583_call()
call_9500 = func_5583_call()
func_2795_call = mod.get_global_var('func_2795')
func_2798_call = mutated_mod.get_global_var('func_2798')
var_9510 = relay.var("var_9510", dtype = "float64", shape = ())#candidate|9510|()|var|float64
var_9511 = relay.var("var_9511", dtype = "float64", shape = (2, 40))#candidate|9511|(2, 40)|var|float64
call_9509 = relay.TupleGetItem(func_2795_call(relay.reshape(var_9510.astype('float64'), []), relay.reshape(var_9511.astype('float64'), [2, 10, 4]), ), 2)
call_9512 = relay.TupleGetItem(func_2798_call(relay.reshape(var_9510.astype('float64'), []), relay.reshape(var_9511.astype('float64'), [2, 10, 4]), ), 2)
output = relay.Tuple([call_9499,call_9509,var_9510,var_9511,])
output2 = relay.Tuple([call_9500,call_9512,var_9510,var_9511,])
func_9514 = relay.Function([var_9510,var_9511,], output)
mod['func_9514'] = func_9514
mod = relay.transform.InferType()(mod)
mutated_mod['func_9514'] = func_9514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9514_call = mutated_mod.get_global_var('func_9514')
var_9516 = relay.var("var_9516", dtype = "float64", shape = ())#candidate|9516|()|var|float64
var_9517 = relay.var("var_9517", dtype = "float64", shape = (2, 40))#candidate|9517|(2, 40)|var|float64
call_9515 = func_9514_call(var_9516,var_9517,)
output = call_9515
func_9518 = relay.Function([var_9516,var_9517,], output)
mutated_mod['func_9518'] = func_9518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5833_call = mod.get_global_var('func_5833')
func_5835_call = mutated_mod.get_global_var('func_5835')
call_9522 = func_5833_call()
call_9523 = func_5833_call()
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_9525 = func_3859_call()
call_9526 = func_3859_call()
func_9374_call = mod.get_global_var('func_9374')
func_9376_call = mutated_mod.get_global_var('func_9376')
call_9534 = relay.TupleGetItem(func_9374_call(), 2)
call_9535 = relay.TupleGetItem(func_9376_call(), 2)
uop_9561 = relay.asinh(call_9534.astype('float64')) # shape=(8, 15, 4)
uop_9563 = relay.asinh(call_9535.astype('float64')) # shape=(8, 15, 4)
output = relay.Tuple([call_9522,call_9525,uop_9561,])
output2 = relay.Tuple([call_9523,call_9526,uop_9563,])
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
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
call_9585 = relay.TupleGetItem(func_7482_call(), 0)
call_9586 = relay.TupleGetItem(func_7484_call(), 0)
func_7596_call = mod.get_global_var('func_7596')
func_7597_call = mutated_mod.get_global_var('func_7597')
call_9590 = relay.TupleGetItem(func_7596_call(), 1)
call_9591 = relay.TupleGetItem(func_7597_call(), 1)
uop_9595 = relay.asin(call_9590.astype('float32')) # shape=(14, 14, 10)
uop_9597 = relay.asin(call_9591.astype('float32')) # shape=(14, 14, 10)
output = relay.Tuple([call_9585,uop_9595,])
output2 = relay.Tuple([call_9586,uop_9597,])
func_9615 = relay.Function([], output)
mod['func_9615'] = func_9615
mod = relay.transform.InferType()(mod)
mutated_mod['func_9615'] = func_9615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9615_call = mutated_mod.get_global_var('func_9615')
call_9616 = func_9615_call()
output = call_9616
func_9617 = relay.Function([], output)
mutated_mod['func_9617'] = func_9617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6171_call = mod.get_global_var('func_6171')
func_6173_call = mutated_mod.get_global_var('func_6173')
call_9673 = func_6171_call()
call_9674 = func_6171_call()
output = call_9673
output2 = call_9674
func_9675 = relay.Function([], output)
mod['func_9675'] = func_9675
mod = relay.transform.InferType()(mod)
mutated_mod['func_9675'] = func_9675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9675_call = mutated_mod.get_global_var('func_9675')
call_9676 = func_9675_call()
output = call_9676
func_9677 = relay.Function([], output)
mutated_mod['func_9677'] = func_9677
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9683 = relay.var("var_9683", dtype = "int8", shape = ())#candidate|9683|()|var|int8
var_9684 = relay.var("var_9684", dtype = "int8", shape = (10, 1, 9))#candidate|9684|(10, 1, 9)|var|int8
bop_9685 = relay.right_shift(var_9683.astype('int8'), var_9684.astype('int8')) # shape=(10, 1, 9)
output = relay.Tuple([bop_9685,])
output2 = relay.Tuple([bop_9685,])
func_9688 = relay.Function([var_9683,var_9684,], output)
mod['func_9688'] = func_9688
mod = relay.transform.InferType()(mod)
var_9689 = relay.var("var_9689", dtype = "int8", shape = ())#candidate|9689|()|var|int8
var_9690 = relay.var("var_9690", dtype = "int8", shape = (10, 1, 9))#candidate|9690|(10, 1, 9)|var|int8
output = func_9688(var_9689,var_9690,)
func_9691 = relay.Function([var_9689,var_9690,], output)
mutated_mod['func_9691'] = func_9691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6309_call = mod.get_global_var('func_6309')
func_6310_call = mutated_mod.get_global_var('func_6310')
call_9699 = func_6309_call()
call_9700 = func_6309_call()
func_5012_call = mod.get_global_var('func_5012')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_9710 = relay.TupleGetItem(func_5012_call(), 3)
call_9711 = relay.TupleGetItem(func_5013_call(), 3)
output = relay.Tuple([call_9699,call_9710,])
output2 = relay.Tuple([call_9700,call_9711,])
func_9726 = relay.Function([], output)
mod['func_9726'] = func_9726
mod = relay.transform.InferType()(mod)
mutated_mod['func_9726'] = func_9726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mutated_mod.get_global_var('func_9726')
call_9727 = func_9726_call()
output = call_9727
func_9728 = relay.Function([], output)
mutated_mod['func_9728'] = func_9728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5082_call = mod.get_global_var('func_5082')
func_5084_call = mutated_mod.get_global_var('func_5084')
call_9739 = func_5082_call()
call_9740 = func_5082_call()
var_9741 = relay.var("var_9741", dtype = "float32", shape = (12, 3, 14))#candidate|9741|(12, 3, 14)|var|float32
bop_9742 = relay.greater(call_9739.astype('bool'), relay.reshape(var_9741.astype('bool'), relay.shape_of(call_9739))) # shape=(12, 3, 14)
bop_9745 = relay.greater(call_9740.astype('bool'), relay.reshape(var_9741.astype('bool'), relay.shape_of(call_9740))) # shape=(12, 3, 14)
output = relay.Tuple([bop_9742,])
output2 = relay.Tuple([bop_9745,])
func_9747 = relay.Function([var_9741,], output)
mod['func_9747'] = func_9747
mod = relay.transform.InferType()(mod)
mutated_mod['func_9747'] = func_9747
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9748 = relay.var("var_9748", dtype = "float32", shape = (12, 3, 14))#candidate|9748|(12, 3, 14)|var|float32
func_9747_call = mutated_mod.get_global_var('func_9747')
call_9749 = func_9747_call(var_9748)
output = call_9749
func_9750 = relay.Function([var_9748], output)
mutated_mod['func_9750'] = func_9750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5927_call = mod.get_global_var('func_5927')
func_5928_call = mutated_mod.get_global_var('func_5928')
call_9758 = relay.TupleGetItem(func_5927_call(), 0)
call_9759 = relay.TupleGetItem(func_5928_call(), 0)
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
call_9766 = relay.TupleGetItem(func_7482_call(), 1)
call_9767 = relay.TupleGetItem(func_7484_call(), 1)
func_9102_call = mod.get_global_var('func_9102')
func_9103_call = mutated_mod.get_global_var('func_9103')
call_9770 = relay.TupleGetItem(func_9102_call(), 4)
call_9771 = relay.TupleGetItem(func_9103_call(), 4)
uop_9775 = relay.cosh(call_9766.astype('float32')) # shape=(16, 5, 15)
uop_9777 = relay.cosh(call_9767.astype('float32')) # shape=(16, 5, 15)
bop_9781 = relay.left_shift(uop_9775.astype('int8'), relay.reshape(call_9766.astype('int8'), relay.shape_of(uop_9775))) # shape=(16, 5, 15)
bop_9784 = relay.left_shift(uop_9777.astype('int8'), relay.reshape(call_9767.astype('int8'), relay.shape_of(uop_9777))) # shape=(16, 5, 15)
func_6717_call = mod.get_global_var('func_6717')
func_6719_call = mutated_mod.get_global_var('func_6719')
call_9785 = func_6717_call()
call_9786 = func_6717_call()
output = relay.Tuple([call_9758,call_9770,bop_9781,call_9785,])
output2 = relay.Tuple([call_9759,call_9771,bop_9784,call_9786,])
func_9788 = relay.Function([], output)
mod['func_9788'] = func_9788
mod = relay.transform.InferType()(mod)
mutated_mod['func_9788'] = func_9788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9788_call = mutated_mod.get_global_var('func_9788')
call_9789 = func_9788_call()
output = call_9789
func_9790 = relay.Function([], output)
mutated_mod['func_9790'] = func_9790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_9808 = func_5583_call()
call_9809 = func_5583_call()
func_8655_call = mod.get_global_var('func_8655')
func_8656_call = mutated_mod.get_global_var('func_8656')
call_9812 = relay.TupleGetItem(func_8655_call(), 0)
call_9813 = relay.TupleGetItem(func_8656_call(), 0)
uop_9819 = relay.tan(call_9812.astype('float64')) # shape=(16, 5, 15)
uop_9821 = relay.tan(call_9813.astype('float64')) # shape=(16, 5, 15)
func_4696_call = mod.get_global_var('func_4696')
func_4700_call = mutated_mod.get_global_var('func_4700')
const_9827 = relay.const(10, dtype = "int16")#candidate|9827|()|const|int16
const_9828 = relay.const([2,3,1,-8,1,-4,8,5,-10,6,3,-6,-1,-4,-8,7,10,8,8,-2,-5,-6,-2,1,-10,-10,4,5,6,6,8,-6,7,-2,9,-4,8,9,2,4,6,-7,9,-6,3,10,7,-10,9,-9,-5,5,4,-5,-4,10,-4,-8,1,9,8,-5,-5,-9,-6,7,1,5,5,-2,1,-7,-9,10,-1,-3,-8,5,-3,10,-3,3,6,-9,-9,10,-5,5,-3,5,3,4,8,5,-2,-1,9,-10,1,7,-2,-10,-3,-2,-1,10,-7,-7,2,6,-6,-10,2,-1,-1,5,-5,-10,-1,3,-1,7,-7,-5,-8,-6,10,1,-8,-7,1,2,-4,-2,-7,8,-10,-10,-1,8,5,-4,-10,7,7,6,-3,-2,1,3,-1,-9,-7,-7,-1,-6,7,-9,4,4,9,7,-8,-2,-5,8,7,-6,-6,1,-6,-4,-8,9,-1,1,-2,-4,9,9,1,1,-5,-2,-10,8,1,-8,-7,1,1,-7,-2,3,-7,5,-10,-9,3,-7,6,8,7,8,-4,-1,-1,-8,-9,4,3,-7,-8,-9,-8,4,4,-3,10,5,8,-9,-4,2,9,-3,-7,-7,-9,-6,5,-2,3,-9,7,-7,2,6,2,-3,-5,-5,-1,5,-3,8,4,6,-7,10,-3,-1,-10,2,6,-7,4,-1,-6,-4,9,6,1,-1,-1,4,-6,8,1,-2,-7,-6,-2,-7,-5,-7,4,8,-9,6,9,-1,-3,5,-1,1,-5,-1,5,-5,-1,-5,-8,-10,3,7,4,-9,9,4,-10,-7,3,-1,-8,-7,1,-3,4,-7,7,-8,-2,-1,2,10,-10,8,9,-2,-8,-5,10,1,1,-2,2,3,-9,-4,10,3,-2,-3,-10,7,3,-8,-2,-6,7,-3,-8,-2,1,-7,3,-10,1,-6,-8,1,-9,-2,-8,-7,-8,3,-9,4,4,-2,3,1,-5,5,4,-3,-4,5,7,6,-2,-3,5,-10,1,5,-4,-8,-3,-4,-8,9,4,-6,6,8,3,9,-9,9,3,-3,-10,5,3,-2,8,3,-5,-5,-2,-9,4,-5,8,-4,7,7,-8,3,-4,2,-6,4,-5,2,-1,2,-10,-10,-10,9,-4,7,1,-3,4,-4,2,2,6,5,-7,-3,-4,7,-7,-1,5,3,7,8,1,10,10,1,5,3,2,1,9,10,-6,-7,9,4,7,-7,-6,2,-8,3,-6,7,2,-4,6,5,4,-1,-5,9,1,-2,3,-4,-6,6,3,2,1,-4,-9,-7,4,-4,-4,-3,-8,-1,-7,-2,2,-7,-3,-2,-2,-9,7,1,-5,2,-9,6,8,-6,4,9,10,-3,-2,5,-1,-6,4,2,4,1,-7,-1,-6,-1,9,-6,-6,9,-4,-4,3,-5,-7,6,-1,7,6,4,-6,-10,-4,1,-5,-8,9,8,-1,-6,-2,-4,-1,-2,8,9,-2,9,5,-8,2,-3,-9,10,-4,8,3,8,2,1,5,-6,-8,4,4,-8,-9,7,2,8,8,-1,-8,2,-8,-4,4,-1,-4,8,9,6,6,6,3,-3,9,-1,-2,1,-8,2,-4,4,10,-9,9,8,1,5,-7,-4,-4,-5,7,-6,-10,7,-3,-1,-3,1,6,-9,-3,-2,3,-7,10,-3,8,4,-8,-2,-1,4,-3,-8,-4,7,-1,10,-4,1,8,5,-3,-4,1,2,8,8,10,-2,4,6,10,-9,10,2,-4,-6,5,8,3,-8,7,-4,-5,-5,-8,4,4,4,-3,-4,3,-4,7,6,3,2,-3,8,3,-7,-2,-10,-6,2,3,6,3,6,-1,1,8,5,10,-1,7,-3,-1,-7,9,6,-3,-8,2,8,8,-9,-5,-2,-8,-7,1,3,-6,10,-8,-5,-9,-9,9,-6,9,7,-8,8,-2,-10,-8,6,1,-9,-4,-2,-7,6,8,-7,7,-10,1,-2,6,5,-5,8,-8,-7,-1,-7,-9,6,-7,4,-5,9,-4,-10,-5,4,5,-5,9,7,-10,8,-7,9,-9,8,-9,1,-1,6,5,5,-4,-7,4,-2,-8,6,-7,1,-9,-2,-7,-4,6,-4,1,-3,10,9,3,10,4,-9,2,8,1,10,3,-8,-5,9,2,3,3,-7,5,-10,-5,9,2,-9,-7,3,-4,-8,3,-6,-3,-10,3,5,-9,7,5,-3,5,-10,-2,4,-3,-6,-2,-5,3,1,5,6,-10,-7,-10,2,2,-8,4,-10,-4,5,-9,1,6,-10,6,2,-10,1,-9,5,-4,6,7,-4,10,-9,8,1,-1,-4,6,5,4,7,-8,7,-7,1,-6,-7,4,7,5,7,-8,3,6,-1,-3,-8,-1,6,-5,-4,-1,1,-4,-9,-4,-4,-7,8,6,-8,8,-3,-8,-8,3,-7,-10,10,-5,-4,-5,-3,7,10,1,-4], dtype = "int16")#candidate|9828|(924,)|const|int16
call_9826 = func_4696_call(relay.reshape(const_9827.astype('int16'), []), relay.reshape(const_9828.astype('int16'), [11, 12, 7]), )
call_9829 = func_4696_call(relay.reshape(const_9827.astype('int16'), []), relay.reshape(const_9828.astype('int16'), [11, 12, 7]), )
bop_9830 = relay.equal(call_9826.astype('bool'), relay.reshape(const_9828.astype('bool'), relay.shape_of(call_9826))) # shape=(11, 12, 7)
bop_9833 = relay.equal(call_9829.astype('bool'), relay.reshape(const_9828.astype('bool'), relay.shape_of(call_9829))) # shape=(11, 12, 7)
uop_9840 = relay.sqrt(bop_9830.astype('float64')) # shape=(11, 12, 7)
uop_9842 = relay.sqrt(bop_9833.astype('float64')) # shape=(11, 12, 7)
func_4696_call = mod.get_global_var('func_4696')
func_4700_call = mutated_mod.get_global_var('func_4700')
call_9893 = func_4696_call(relay.reshape(const_9827.astype('int16'), []), relay.reshape(call_9826.astype('int16'), [11, 12, 7]), )
call_9894 = func_4696_call(relay.reshape(const_9827.astype('int16'), []), relay.reshape(call_9826.astype('int16'), [11, 12, 7]), )
func_9615_call = mod.get_global_var('func_9615')
func_9617_call = mutated_mod.get_global_var('func_9617')
call_9915 = relay.TupleGetItem(func_9615_call(), 1)
call_9916 = relay.TupleGetItem(func_9617_call(), 1)
output = relay.Tuple([call_9808,uop_9819,const_9827,uop_9840,call_9893,call_9915,])
output2 = relay.Tuple([call_9809,uop_9821,const_9827,uop_9842,call_9894,call_9916,])
func_9920 = relay.Function([], output)
mod['func_9920'] = func_9920
mod = relay.transform.InferType()(mod)
mutated_mod['func_9920'] = func_9920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9920_call = mutated_mod.get_global_var('func_9920')
call_9921 = func_9920_call()
output = call_9921
func_9922 = relay.Function([], output)
mutated_mod['func_9922'] = func_9922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_9960 = relay.TupleGetItem(func_4068_call(), 0)
call_9961 = relay.TupleGetItem(func_4069_call(), 0)
output = call_9960
output2 = call_9961
func_9962 = relay.Function([], output)
mod['func_9962'] = func_9962
mod = relay.transform.InferType()(mod)
output = func_9962()
func_9963 = relay.Function([], output)
mutated_mod['func_9963'] = func_9963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_9972 = func_3859_call()
call_9973 = func_3859_call()
func_5128_call = mod.get_global_var('func_5128')
func_5131_call = mutated_mod.get_global_var('func_5131')
call_9981 = func_5128_call(relay.reshape(call_9972.astype('bool'), [8, 15, 4]))
call_9982 = func_5128_call(relay.reshape(call_9972.astype('bool'), [8, 15, 4]))
func_8816_call = mod.get_global_var('func_8816')
func_8818_call = mutated_mod.get_global_var('func_8818')
call_10000 = relay.TupleGetItem(func_8816_call(), 0)
call_10001 = relay.TupleGetItem(func_8818_call(), 0)
func_6010_call = mod.get_global_var('func_6010')
func_6012_call = mutated_mod.get_global_var('func_6012')
var_10010 = relay.var("var_10010", dtype = "float64", shape = (924,))#candidate|10010|(924,)|var|float64
call_10009 = relay.TupleGetItem(func_6010_call(relay.reshape(var_10010.astype('float64'), [924,])), 0)
call_10011 = relay.TupleGetItem(func_6012_call(relay.reshape(var_10010.astype('float64'), [924,])), 0)
func_6717_call = mod.get_global_var('func_6717')
func_6719_call = mutated_mod.get_global_var('func_6719')
call_10019 = func_6717_call()
call_10020 = func_6717_call()
output = relay.Tuple([call_9972,call_9981,call_10000,call_10009,var_10010,call_10019,])
output2 = relay.Tuple([call_9973,call_9982,call_10001,call_10011,var_10010,call_10020,])
func_10034 = relay.Function([var_10010,], output)
mod['func_10034'] = func_10034
mod = relay.transform.InferType()(mod)
mutated_mod['func_10034'] = func_10034
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10035 = relay.var("var_10035", dtype = "float64", shape = (924,))#candidate|10035|(924,)|var|float64
func_10034_call = mutated_mod.get_global_var('func_10034')
call_10036 = func_10034_call(var_10035)
output = call_10036
func_10037 = relay.Function([var_10035], output)
mutated_mod['func_10037'] = func_10037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_10075 = func_3896_call()
call_10076 = func_3896_call()
output = call_10075
output2 = call_10076
func_10096 = relay.Function([], output)
mod['func_10096'] = func_10096
mod = relay.transform.InferType()(mod)
output = func_10096()
func_10097 = relay.Function([], output)
mutated_mod['func_10097'] = func_10097
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10241 = relay.var("var_10241", dtype = "float64", shape = (9, 14, 5))#candidate|10241|(9, 14, 5)|var|float64
var_10242 = relay.var("var_10242", dtype = "float64", shape = (9, 14, 5))#candidate|10242|(9, 14, 5)|var|float64
bop_10243 = relay.divide(var_10241.astype('float64'), relay.reshape(var_10242.astype('float64'), relay.shape_of(var_10241))) # shape=(9, 14, 5)
var_10254 = relay.var("var_10254", dtype = "float64", shape = (9, 14, 5))#candidate|10254|(9, 14, 5)|var|float64
bop_10255 = relay.minimum(var_10242.astype('uint8'), relay.reshape(var_10254.astype('uint8'), relay.shape_of(var_10242))) # shape=(9, 14, 5)
output = relay.Tuple([bop_10243,bop_10255,])
output2 = relay.Tuple([bop_10243,bop_10255,])
func_10260 = relay.Function([var_10241,var_10242,var_10254,], output)
mod['func_10260'] = func_10260
mod = relay.transform.InferType()(mod)
var_10261 = relay.var("var_10261", dtype = "float64", shape = (9, 14, 5))#candidate|10261|(9, 14, 5)|var|float64
var_10262 = relay.var("var_10262", dtype = "float64", shape = (9, 14, 5))#candidate|10262|(9, 14, 5)|var|float64
var_10263 = relay.var("var_10263", dtype = "float64", shape = (9, 14, 5))#candidate|10263|(9, 14, 5)|var|float64
output = func_10260(var_10261,var_10262,var_10263,)
func_10264 = relay.Function([var_10261,var_10262,var_10263,], output)
mutated_mod['func_10264'] = func_10264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7640_call = mod.get_global_var('func_7640')
func_7642_call = mutated_mod.get_global_var('func_7642')
call_10290 = relay.TupleGetItem(func_7640_call(), 2)
call_10291 = relay.TupleGetItem(func_7642_call(), 2)
output = relay.Tuple([call_10290,])
output2 = relay.Tuple([call_10291,])
func_10306 = relay.Function([], output)
mod['func_10306'] = func_10306
mod = relay.transform.InferType()(mod)
output = func_10306()
func_10307 = relay.Function([], output)
mutated_mod['func_10307'] = func_10307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7596_call = mod.get_global_var('func_7596')
func_7597_call = mutated_mod.get_global_var('func_7597')
call_10378 = relay.TupleGetItem(func_7596_call(), 1)
call_10379 = relay.TupleGetItem(func_7597_call(), 1)
const_10395 = relay.const([[[4.573550,-6.028057,7.572249,-6.306519,6.885579,1.510869,9.785395,6.307436,9.611468,-7.349736],[-9.550996,-6.016462,-8.147403,-9.252683,6.317451,5.994359,4.204726,-1.232705,-1.522796,5.097187],[-8.328208,-6.936829,9.193098,-9.275418,6.824153,7.059233,-3.553391,9.205569,-2.329581,6.047607],[-6.008705,-1.174003,-3.274089,-0.802748,1.315045,-9.589534,9.825597,2.256568,-3.063214,3.292992],[-6.650204,2.222361,-2.209926,-0.732544,-7.882979,7.885569,-1.018777,9.854299,-2.689361,0.907614],[5.836621,7.864760,-9.103535,6.465791,-8.907282,-3.597159,1.851294,5.080508,-5.991362,-1.637452],[7.854929,6.775147,7.922399,-1.427356,7.273038,2.145830,-7.471545,0.606366,2.139771,1.555859],[1.951208,9.499486,-8.367374,3.304379,-3.646655,4.719052,0.919748,2.046309,8.329330,-5.219030],[2.326147,-1.054271,-8.857941,-4.729412,-4.538571,1.042425,3.517027,1.350089,8.434926,-8.755906],[-0.170193,-8.994795,3.658660,6.546397,1.885861,8.329553,1.404222,-6.012012,6.099210,-9.105985],[6.641658,4.536497,-5.899734,-9.928368,8.019847,7.062915,-3.423739,4.492825,2.849838,2.446709],[-7.141885,1.941582,-4.509901,8.336114,-3.902207,2.062516,3.226124,-1.410566,8.084636,-1.425872],[8.720033,1.683700,1.557178,4.249332,6.667596,2.098400,0.479784,3.031725,0.225371,9.648986],[-7.460397,3.162126,-2.905169,5.133733,-3.745312,-5.918547,9.722156,5.155419,3.935995,8.079976]],[[4.831096,-6.841438,4.819186,-1.402050,2.315788,-0.690559,4.747749,2.441420,2.431191,9.697669],[-7.989320,-4.507295,7.458792,-6.708355,-9.871178,1.878276,0.992136,7.376696,-5.556403,3.007148],[1.801888,1.379421,4.869307,-2.500876,-6.113238,-9.219923,-0.580659,-4.854791,-2.800382,-5.754315],[1.827190,0.579269,4.421798,2.638603,-8.709000,9.306410,9.612812,-0.420603,-1.641657,1.265444],[9.501762,7.187056,-0.276951,5.049070,4.831226,-9.380291,-5.011849,0.251238,-3.732107,7.212333],[0.407815,-5.377572,7.834345,8.902530,-6.460374,-7.147937,-0.018743,4.859567,-6.285884,1.644995],[-1.847082,-7.754560,8.053608,-3.791347,-5.016332,5.378737,7.297590,-5.753315,-2.507995,-7.972999],[2.049135,-4.632938,-4.365445,-9.641704,7.171098,-7.841484,9.669211,-2.306617,-8.522777,-9.186892],[-9.477999,-8.284051,-8.692985,-1.421230,-3.892195,0.970375,-3.561244,7.859201,5.807988,5.070727],[-4.730928,-8.744862,-9.666418,-8.784096,3.712448,1.514162,-7.496392,5.444404,0.751716,-8.467501],[-6.659860,9.338641,9.423566,-9.617750,-7.147229,6.227967,5.425770,2.008110,-5.798391,4.587067],[-3.075682,0.197338,-9.221212,3.638641,2.872197,-9.185969,4.592900,-8.036599,-0.477643,5.169613],[-7.257647,6.695792,-0.818291,2.620898,2.207113,9.190503,6.596701,-7.043844,0.121488,8.518698],[7.099988,1.659858,6.727563,-9.071493,-9.183342,8.709452,-7.791396,-7.257687,8.605604,-4.375446]],[[-2.588915,-3.327035,-0.401399,-3.180234,0.054416,-1.080383,0.047064,7.844472,1.690391,-0.394378],[-9.754988,-8.784755,6.747138,1.977641,-2.833124,4.811494,1.311223,3.108472,-2.727015,-5.285994],[5.630867,6.844568,-2.076680,-3.083882,-1.695653,4.356835,-4.648995,0.941260,-4.338457,-0.867407],[-9.525624,-0.883695,7.063636,-6.387659,5.469899,9.961703,2.436395,0.209118,-8.047000,-0.035679],[-0.721228,6.149605,0.263496,-6.153922,5.554488,0.325555,-2.087867,-3.561158,9.989078,-5.263959],[4.751011,7.795345,-8.287737,-1.666001,-0.866054,6.722906,-0.698957,6.669003,4.152921,4.149356],[-4.434807,7.712536,-9.650379,9.277771,-2.282426,-1.383685,5.775542,-0.521140,-6.634030,-7.329624],[1.328258,-2.835083,-8.580805,-2.566822,3.236262,5.524355,-0.482530,2.503450,-0.820465,-9.158454],[-4.937952,-6.549375,-5.848178,1.479650,2.138268,-4.905725,6.807213,-5.782509,-9.512189,3.845257],[-2.235215,-1.347269,0.079940,-6.019014,-9.699672,-6.080448,9.382340,-5.957286,-8.589098,0.775059],[-9.005663,-9.976288,-7.183054,4.393938,6.827162,-4.318351,5.017119,-2.237796,-2.406835,-2.956520],[0.676620,7.893390,5.267557,5.678161,7.528794,2.656642,-7.940528,6.548721,-9.674578,2.687390],[-2.606004,-1.465401,-2.781919,-4.908825,5.518384,0.418478,-3.060020,7.039962,7.837708,7.608820],[4.739922,-2.670960,-0.258266,-8.433396,-1.271765,8.926926,-2.042531,8.189764,-0.803033,5.250344]],[[-8.334779,4.449806,-8.034458,6.413837,9.067843,-9.495654,6.471226,-0.527689,4.716869,1.995560],[-6.097565,-1.912713,-3.101109,-2.747552,5.934381,-1.298866,-4.149287,-5.317599,-7.344043,-7.899306],[-9.419991,7.258442,6.959738,-8.701273,-7.659815,6.222217,-2.160224,9.655545,0.464424,8.832818],[-1.907312,-2.257350,6.964340,0.140161,-1.322960,9.407672,-0.042790,4.059629,-0.284348,-6.335693],[7.382224,-5.108050,9.522895,-5.993261,3.928066,-4.250018,7.496802,-4.836857,6.558400,-4.245904],[-1.918760,1.308508,-2.351215,-6.018743,-2.416039,-5.276140,-0.935521,3.406300,-7.223724,-1.128268],[7.316199,6.695499,-8.971458,-1.216973,2.336358,4.968485,-1.540457,8.837010,9.711848,-3.766026],[-0.001175,3.069638,2.026765,2.919172,-0.948408,0.890534,-6.641289,-5.626241,-8.829318,-0.315539],[-2.807561,4.642157,-9.254059,2.353086,8.418115,5.897926,-8.067762,-4.024857,6.037365,-4.093926],[-6.568752,-2.981328,-4.925533,1.390452,3.418101,1.356766,6.256847,-6.091372,7.927234,-8.016101],[7.583723,-2.547469,-8.329372,4.298281,-9.471656,-0.694206,1.241549,8.645776,8.032442,1.567996],[0.119291,-5.908070,6.733193,-3.668880,3.700679,1.821252,4.780878,-3.891457,3.250089,4.555251],[0.391769,-7.226747,-2.753159,3.849137,-1.092385,-5.073516,4.348595,-9.434122,-3.656174,8.617462],[0.075116,-2.668752,-6.433751,7.771164,9.692992,-9.501623,-3.810178,1.142876,-1.988410,-5.050877]],[[3.663612,-4.814306,-9.658247,-4.632446,-1.216145,-3.384161,-4.489926,-3.409658,2.845129,-3.580342],[-0.821905,-8.086075,7.920511,-6.400846,-3.690534,-4.098930,5.424962,-8.801055,-4.558501,-6.499920],[-4.762167,-4.693342,-5.306050,4.989877,-1.687771,-2.351666,-8.318261,8.145013,-6.663372,-0.073505],[9.235517,3.904664,4.476658,-0.291939,-7.746768,-3.599036,9.740988,7.842293,8.070323,1.297960],[2.605174,8.736326,-0.990644,5.521559,-5.105021,5.342143,8.375812,-1.182013,-4.783087,-5.404604],[-3.237427,8.303090,0.218811,1.689563,-9.826801,7.114939,-2.378764,9.285317,9.180104,0.198328],[-7.194345,4.452678,3.898779,2.329123,-0.312430,-9.580787,-0.507683,-2.850575,3.022526,8.154504],[7.210487,4.147525,3.109106,-0.422554,9.215767,-8.134095,3.364378,6.494175,0.678385,-4.632667],[-6.897076,-3.693604,2.804134,6.465843,-1.613209,-8.879684,1.677488,8.660405,-6.447882,9.366798],[-8.920657,-0.670393,-4.318752,-8.777563,-5.334176,0.359137,-7.487880,2.583719,5.208154,-8.552968],[1.362859,8.696330,-4.404282,9.879935,-9.089571,-2.749378,-1.805467,-2.523083,1.526226,8.159458],[-3.133881,-3.250592,-5.093619,-8.775911,-1.466723,-5.627905,4.518346,-3.924296,-5.124102,-5.746436],[2.807312,6.599758,1.092751,-8.699879,3.159432,-2.018098,-5.633510,-8.942137,4.624957,-5.132505],[3.300963,0.053852,-3.229291,-1.337059,-6.034604,-7.636191,8.825844,3.935487,3.030155,8.248975]],[[6.665951,-8.813518,8.606456,4.208670,2.106866,-0.644744,-1.101018,5.313059,-2.378077,2.938896],[7.293159,-8.984548,-5.856974,8.024959,1.846852,-2.076493,4.403148,-7.508727,7.006192,9.402239],[-4.819532,4.893912,2.565159,3.333405,-0.259156,-4.809148,-7.631588,-2.553498,9.397545,0.539506],[3.654602,6.951428,-2.640610,7.851088,4.856948,2.579057,-9.109212,-8.964698,3.557122,5.514571],[0.180411,7.052183,-6.819617,-0.427003,-2.363332,-2.615418,8.257529,-1.893508,-4.887489,6.988602],[-8.569285,5.982796,4.051191,-1.721685,9.968522,-6.807504,-0.517998,8.041961,4.841283,-7.158827],[5.603901,0.841643,-5.249802,-7.585086,0.720200,5.063326,-4.417095,6.475153,-3.133273,1.489253],[3.034111,-4.062636,9.533768,2.931303,9.281488,-6.956139,-4.568848,5.660267,5.107305,7.366624],[1.729110,-6.505695,5.336596,2.777215,-0.556934,-8.311443,-4.908220,4.255151,-7.198414,1.384433],[-2.598441,-3.976958,8.360179,3.728758,8.335706,-0.775461,1.957989,9.727111,-1.055354,7.227882],[4.402271,-7.142251,-8.172913,8.255001,-8.535084,0.202187,7.491521,-7.319238,7.188190,7.216552],[-3.513299,-2.449995,3.751888,1.879782,-2.008880,-6.594270,-7.844901,-9.482511,-3.947501,6.368037],[-9.922808,7.489130,-0.566509,-4.223605,9.210357,-7.068331,7.059163,-9.444499,-4.959119,-4.709514],[-4.460737,-4.880543,-9.676614,0.462832,0.927844,7.188666,3.748528,5.271648,-4.300669,-9.752325]],[[9.780579,-1.274359,3.627488,2.713722,-3.297490,-8.242221,-9.609410,3.930963,5.925153,1.867364],[7.545338,-3.994247,1.745276,-8.670126,-9.318143,-7.482810,3.907778,-1.575033,6.611839,6.722534],[-6.731338,-3.011173,-0.273138,4.560355,-8.126465,-4.239372,2.713652,0.304640,-0.837832,3.645154],[-3.125480,4.093635,-4.238288,-1.656524,0.454022,8.013219,9.251925,5.354144,6.538260,-6.101208],[0.889561,6.161489,5.031046,-9.000385,-7.423195,-5.957356,3.497413,-5.512454,-4.328663,8.009851],[-5.948897,2.217217,-5.576947,-2.595879,2.717650,4.663527,3.240890,9.892767,3.972124,0.284975],[6.672758,-8.374471,1.274775,-6.195960,4.039985,3.440299,-7.828916,-0.933616,4.815121,-6.696812],[6.357569,-0.499095,-3.686588,1.267911,0.338894,6.261827,5.214704,7.723274,1.385348,-4.824791],[6.180482,-7.657652,-9.754061,-1.022436,5.459671,-2.045509,-3.437380,-0.153301,-4.360684,4.445429],[-2.214032,4.155815,-1.426487,-5.495636,-4.793944,4.020873,-5.347522,-8.790531,-0.161368,3.743954],[0.338898,-8.665173,-6.384627,1.905271,-7.422273,-8.900582,9.938323,-5.967357,-9.914968,8.186049],[0.968193,-8.219960,3.657364,-9.219051,9.709900,1.243534,4.556407,-2.748912,-8.530972,8.909059],[-3.335941,4.102218,8.728962,-4.837752,-8.386186,-5.237682,-4.284176,-5.385243,2.915208,6.563004],[-1.424317,-1.861217,-4.135856,4.721745,-0.056863,0.761711,-5.561441,-0.488841,1.965940,0.162770]],[[3.290332,3.887657,-3.825330,2.416270,7.593624,-3.641055,6.049324,1.794361,0.365774,1.005128],[3.086014,4.224105,5.600511,6.308443,-0.028782,7.890814,3.924720,0.855976,-0.788395,2.517358],[4.532771,2.090082,-2.107096,-1.218736,4.838456,4.084265,-2.799104,-9.863623,4.556805,-2.385910],[-2.562550,4.362773,0.602589,6.973671,8.659230,2.425847,-9.949609,9.230670,8.031863,-0.513824],[8.004942,-8.309683,-0.725805,-9.342542,-7.356941,3.956604,-8.925631,-9.741576,6.108664,5.301168],[6.211217,6.475184,4.463666,-9.477913,-8.292332,4.467996,1.081027,-1.738560,-2.034456,3.467048],[7.107722,8.017425,5.975086,6.755773,3.900530,1.638561,5.028733,-0.848861,8.118213,-3.088055],[4.962051,-6.051821,1.438196,9.364327,0.827725,-7.774999,2.656265,-0.515627,-3.726104,-0.376008],[-4.873341,-9.748638,-7.685302,-0.593215,8.350395,-4.147320,-8.764732,6.117547,0.728184,8.560655],[0.007582,0.499172,8.603602,4.706135,-9.543680,8.085041,6.284120,-5.246653,-8.395047,-0.896449],[3.066210,-9.334990,4.499860,4.764452,-9.155003,0.402710,4.533416,0.177529,-0.097392,-3.606066],[-9.771701,6.450793,9.279398,5.774979,-1.039284,2.322356,-0.021260,7.754839,-8.652484,-1.919357],[0.597545,-0.310203,6.817996,3.331125,4.010528,-4.125899,0.905314,3.733873,5.966703,-5.675100],[-5.934322,-1.432283,8.507538,-5.354077,-6.469333,3.300842,-0.071096,-9.653957,1.541301,8.924606]],[[4.297902,-7.386516,4.344662,9.761706,-9.971491,-3.744284,-7.548763,-1.474634,-0.592832,5.347134],[8.581033,-9.174965,-2.938176,1.737478,-6.847436,-4.470563,-0.849789,-2.266955,7.546897,3.044400],[1.776394,-6.501575,-3.746097,-3.557927,-7.608746,7.949250,-7.041368,9.103950,4.512370,-0.482510],[-5.614057,6.273570,0.452823,-5.255426,-4.011091,-8.589685,-9.617760,7.824352,1.986578,7.426104],[7.441497,-6.278648,7.999743,-6.969914,-1.468879,-1.380327,-4.263544,-3.030663,-4.321242,-9.772153],[-4.960586,-3.620917,0.174347,5.953725,6.637347,-6.323671,4.269440,-0.875990,4.899897,6.304602],[2.090143,-0.501284,-3.741366,1.719342,1.255957,9.101110,3.813095,-7.703873,8.992799,8.916651],[4.501325,4.677320,-9.369919,1.471983,-5.542368,-5.605031,-5.525966,5.114634,4.136277,6.916672],[-5.059593,-0.133836,9.413920,7.260111,-5.609531,7.552758,-3.611904,-7.307019,4.966725,-2.707622],[7.477874,2.705388,3.617942,-4.397778,-4.727302,-9.050549,-3.009931,-2.871289,3.582400,-1.366750],[-6.453044,1.208569,-2.854774,-8.748879,8.261202,6.879861,1.618395,4.962337,-4.049213,1.815039],[3.068892,4.100692,-8.126998,4.439874,1.887850,9.627166,-7.580976,5.867172,-7.629267,-5.137014],[-7.184584,-4.714005,-7.882857,2.068607,3.992855,9.762894,-1.627779,-7.314191,-5.257854,-3.782690],[0.312708,-9.069831,0.325294,-2.708070,9.077456,8.420817,3.620776,0.571887,5.736661,-1.772324]],[[1.223509,-4.236304,-2.671691,-5.511026,-7.636712,7.327461,-4.631553,1.685628,5.976730,1.150643],[-5.376588,-7.454273,8.632200,-9.449238,-8.672981,9.202630,-3.516307,2.674805,3.229096,-3.865636],[4.801962,7.261772,5.885768,2.588165,7.477695,7.918933,0.512573,5.712136,1.193181,-6.356447],[-7.601705,8.723921,3.517511,4.794487,-1.746729,-5.244264,8.041431,7.350882,0.455972,7.615800],[2.661344,-0.320690,7.077049,2.182469,1.978268,-9.606032,-1.657916,3.290698,2.428867,-8.132345],[-6.485935,9.809609,-0.055410,-1.165996,3.334610,-5.106283,-7.046621,4.597343,-5.505047,-2.618440],[-5.219714,9.095252,-8.121296,-4.912128,-5.836077,9.132011,-6.461760,-3.669275,2.650855,-7.886269],[9.410402,5.076246,8.697058,9.230161,-4.612234,-2.700343,-7.804795,2.817390,-6.983851,-6.022164],[-6.206439,7.485255,-1.571570,8.514228,-2.633269,-9.777707,8.950692,7.005033,9.109131,-1.667112],[-3.658276,-3.892471,5.922892,2.841832,-7.031720,-3.265660,4.808995,5.535623,0.154191,8.330986],[-9.075135,0.073558,7.267166,-9.749200,6.945573,-2.340010,9.704694,5.680179,-1.308299,-6.551017],[-1.048421,2.830568,-0.266430,-3.966571,-5.517720,8.049455,5.368112,-2.681366,4.204908,7.297988],[6.749980,-3.787015,9.229644,8.254925,-9.970247,-7.648039,-5.509183,-8.796678,-9.543707,4.326723],[-5.885735,6.369082,5.571793,5.030977,-1.607697,-8.727759,-5.498927,8.313077,-0.213328,-8.151583]],[[-6.102856,5.751952,-8.304406,-0.600450,-5.235307,0.637079,-9.150543,4.439829,-5.659647,5.567908],[8.626520,6.247148,-0.489146,3.139964,3.226174,-1.758536,-5.211817,4.568397,1.707568,8.220842],[6.085842,2.609077,1.203776,9.547958,1.527129,2.973808,-9.988676,-2.602003,6.963214,5.747386],[0.299506,-8.588162,-4.011255,6.190259,7.816970,2.261307,9.907835,4.495487,7.095319,5.540333],[6.082441,-5.726348,0.233890,-4.656179,-0.339831,8.225942,9.658074,-7.600322,0.541086,-7.009760],[-4.028973,9.874631,-6.306531,1.324275,-7.779697,-1.786399,3.450230,9.778181,2.826883,9.964684],[-3.848315,-6.581888,-2.911087,0.364083,-9.451753,9.822508,5.318981,-3.098043,3.313569,-7.145419],[-8.135845,5.623549,3.364715,-9.959563,-6.410856,-1.732340,2.553373,9.128725,7.800974,0.763346],[-3.727976,9.615383,-2.403234,7.991355,2.205419,9.534311,-5.176089,6.987233,6.462028,-2.467749],[9.938641,-1.233306,0.276100,-7.779435,-1.137496,-6.297618,-7.617531,8.173707,-7.401644,-2.320331],[-1.561386,5.164904,-1.900735,-2.597978,9.817004,-4.662208,5.304991,5.783900,-9.439999,-6.800733],[9.164569,9.211716,-1.821314,-3.528119,0.605712,-6.619146,-8.682514,-4.597732,-9.069939,2.940569],[1.013521,-0.289915,-4.677894,-7.631292,5.167855,-3.221394,0.057267,6.444895,-9.230765,-3.251823],[-1.741702,1.897845,2.181708,-9.180548,-6.381201,4.931290,0.544001,-2.620379,7.321481,-2.068840]],[[3.376431,1.419785,-1.930066,-9.539662,4.403389,-8.167681,6.259872,-5.884436,0.943940,-2.195091],[-7.420502,4.261574,6.418519,-2.217451,-6.816697,-5.203160,3.163487,9.769854,-3.190885,-7.494683],[-5.927270,7.938863,-1.950565,-7.180723,-3.834209,6.434687,-2.624501,-6.522852,-0.771258,-9.670307],[7.861161,2.378640,7.555062,-2.460901,-4.985421,5.974308,2.784096,9.541008,-6.211504,1.724801],[-2.742146,-4.045079,-4.686201,8.710067,5.375746,2.979847,-4.077664,7.830348,8.434433,8.546943],[-0.239066,4.597579,8.966041,4.065391,-1.173810,1.450623,8.765157,-2.340267,-7.132933,-9.397418],[4.553006,5.708608,-4.061595,6.506590,-1.716838,-2.698999,1.395633,6.097420,-5.575060,1.964000],[7.606033,3.054816,-3.228724,-7.166254,5.381297,-1.874344,2.371737,-0.703544,-8.822696,1.356906],[-0.287361,2.586191,9.198229,5.430056,7.154191,2.584791,0.923376,3.827685,-2.431875,-3.606569],[-9.679823,-7.044062,-4.352018,-2.556211,9.293163,-9.968688,8.121195,0.622537,-1.618597,-1.659802],[0.031715,-8.964712,-5.332203,-3.818134,-3.793034,1.509236,2.947413,-6.884286,-6.852957,-0.008974],[-2.407782,-2.609622,-1.697653,3.673300,-8.650555,-1.046885,5.174996,-6.893499,-9.784228,-9.371519],[9.085648,-5.674761,4.729235,8.857827,1.248790,2.940089,-4.935882,2.752937,-3.238666,5.260862],[-3.162013,-2.540096,-2.023113,2.170262,-8.784509,0.837828,3.377722,-2.048342,-3.683378,0.667955]],[[-4.329572,-4.187816,-7.319987,4.793770,-7.926217,4.974692,3.723618,-0.827403,-6.244629,-8.964798],[2.976321,-7.704077,4.421434,3.281436,-4.682158,3.507701,-5.552513,4.124263,2.525433,9.597985],[1.240793,-9.090129,-9.592498,3.795456,4.016784,6.884350,0.668081,1.450388,8.998036,3.565088],[9.700138,-4.443073,-6.027737,-4.672144,-0.674115,2.867334,-8.015160,-8.823706,-0.017855,0.499302],[-4.116273,-6.709868,9.013376,-1.613682,-0.473924,-1.359179,2.498117,7.123554,8.790784,1.735953],[6.757168,8.433388,3.879521,6.565852,0.385596,5.155975,1.677745,-3.539088,1.375024,2.736284],[-7.845042,-9.781599,-3.624717,5.821181,2.304494,-7.086193,8.923486,3.643123,7.697292,-4.721442],[7.795358,-2.005566,4.269562,4.121803,-4.201584,-2.419107,2.674822,-5.013875,6.816138,9.822776],[-1.320080,2.230658,3.413510,-1.863269,0.355470,-0.171595,-2.869527,-4.633127,7.053125,8.864998],[-2.619515,-7.056816,-7.109202,-9.983801,-5.006691,-0.565922,6.324626,-4.519313,-0.002722,4.517908],[3.607739,9.203864,0.662071,0.295439,3.696315,-8.799143,-3.458425,6.656342,3.511732,-0.505141],[8.410020,-3.286799,7.984717,-4.515274,-4.929642,5.153607,4.364435,8.136456,-1.807017,0.063492],[1.042616,-1.117540,-0.624093,-5.032746,1.391803,5.364859,-9.137089,3.094314,-0.302669,2.153055],[0.751073,-6.907311,3.330306,1.353803,-6.637829,-5.616192,-3.218029,8.861171,-8.354920,-1.831202]],[[0.708841,0.246520,-1.301058,1.482104,-2.055737,3.127759,0.248246,-3.301912,6.428279,7.392273],[-2.724609,-2.909398,-4.396101,4.163484,8.450249,-1.581192,7.537933,-8.431570,-2.242482,-4.857269],[2.960824,-1.408066,8.779734,6.779098,1.608158,-1.322563,-1.363554,-2.865063,-6.612841,-9.929465],[-9.471716,-5.935033,-9.312845,6.837862,-9.232523,6.964427,1.472633,3.213811,-7.237391,7.307890],[0.501179,5.928462,-6.319773,-8.857478,5.877976,2.465462,5.590769,6.263389,-8.693603,-4.632840],[-0.743609,-1.250621,8.906997,-1.597212,1.177890,0.726434,4.654637,-4.806442,6.860647,-4.234453],[6.186083,-2.924895,-0.757743,-1.458990,-6.669073,2.855803,-1.154867,-5.170668,2.941022,9.968983],[-9.341369,4.057271,2.958103,-6.707517,-8.717381,6.304623,-6.117503,-2.006509,1.650085,9.497861],[8.453530,-0.627414,1.590173,-8.863706,7.789200,5.013818,-3.387068,4.210794,-3.160226,-0.548775],[6.713806,9.420351,3.447727,-3.485666,-3.288219,-6.888238,-5.096543,-6.436373,6.246053,7.805553],[-6.057877,6.294257,5.094188,2.830145,-7.720102,7.325997,6.672809,4.989859,-9.400905,-8.679312],[5.650341,7.230447,5.759934,5.460045,-6.112483,-7.537420,9.110677,9.780919,-7.644746,3.867780],[4.940944,-5.271662,0.528548,3.237656,4.115513,-7.383749,4.186236,5.131576,8.552867,6.604947],[7.943329,9.983549,6.545662,7.637376,3.343340,-9.507182,1.943295,0.205022,-7.272448,9.828866]]], dtype = "float64")#candidate|10395|(14, 14, 10)|const|float64
bop_10396 = relay.greater_equal(call_10378.astype('bool'), relay.reshape(const_10395.astype('bool'), relay.shape_of(call_10378))) # shape=(14, 14, 10)
bop_10399 = relay.greater_equal(call_10379.astype('bool'), relay.reshape(const_10395.astype('bool'), relay.shape_of(call_10379))) # shape=(14, 14, 10)
func_8784_call = mod.get_global_var('func_8784')
func_8787_call = mutated_mod.get_global_var('func_8787')
var_10405 = relay.var("var_10405", dtype = "float64", shape = (924,))#candidate|10405|(924,)|var|float64
call_10404 = relay.TupleGetItem(func_8784_call(relay.reshape(var_10405.astype('float64'), [462, 2])), 0)
call_10406 = relay.TupleGetItem(func_8787_call(relay.reshape(var_10405.astype('float64'), [462, 2])), 0)
const_10418 = relay.const([[[-2.499436,-7.050429,-9.777361,-5.127656,-5.966443,2.168113,2.130678,-1.748079,-5.667879,0.913060],[-9.930628,4.770442,9.729939,-3.908797,9.177382,-1.315566,-0.654174,-8.293249,-0.614788,1.693580],[-4.561709,-5.662259,-9.162128,-1.058116,0.116789,0.525854,-7.954437,-5.331050,2.698443,-5.358798],[-3.448632,7.805002,9.194633,-3.542813,-2.500091,6.239470,-2.037565,-6.764907,-6.752752,7.278968],[-2.336329,9.212776,8.995687,-2.152997,-9.585920,-7.194093,-0.702348,5.042043,0.752091,0.830853],[-1.291843,-9.755469,-5.886154,4.302702,-8.376602,9.000095,8.685146,6.591453,-1.431784,-4.774670],[1.994823,2.576556,-2.891050,3.874187,-9.653722,2.095932,4.734872,0.218346,-0.556404,7.242197],[-2.471643,-6.421265,3.007454,-0.388373,4.467591,0.408023,4.971081,-2.187077,2.469280,-9.348829],[7.039734,-5.179095,3.107251,-6.688889,4.093925,-3.659902,-5.966079,2.604373,1.593314,0.665690],[-6.434450,7.802728,-2.015670,4.097187,2.181014,4.480644,1.742359,-0.832566,-4.019807,2.447208],[-1.119688,8.782904,-2.820182,-4.093834,-0.061027,-1.118569,-7.594238,0.603766,-8.024287,4.033428],[-3.518974,-3.719535,-7.958452,-3.883119,3.300161,-4.285512,-5.005017,6.661352,8.633341,-3.248129],[6.369674,-0.249451,-3.618741,-6.007605,6.347876,-0.457439,8.030217,7.878392,7.776697,-5.792972],[2.500996,-5.342645,-6.293737,-5.254186,-9.066715,2.045989,-8.829680,3.600426,3.821110,0.032908]],[[2.210827,-2.240760,-4.377260,8.626770,-7.277423,-8.880010,-1.900987,3.086095,-2.830876,-0.008554],[-7.486304,2.867658,-5.967099,4.402636,-9.994975,-2.852634,-0.512420,-1.144956,-4.781973,3.362955],[3.874953,1.168726,-5.475437,-9.722256,-7.216924,5.438218,5.480858,0.413700,-9.809126,1.067460],[2.058725,-1.644904,6.156656,-2.757601,-1.182132,-3.143334,-1.556710,-6.449806,-0.625600,1.844768],[6.488768,8.802681,6.326790,-9.714501,4.064447,5.543095,4.726740,-6.964912,-7.038337,6.394697],[-6.919025,0.523470,9.707107,-8.395342,-4.547846,-7.918834,-1.234338,-9.419887,5.933465,5.829928],[6.707296,4.385870,8.475891,4.783644,2.718863,-1.539340,-8.308754,-6.036347,0.951828,6.814946],[-2.999275,-9.614277,3.775066,3.912345,2.500307,7.895689,2.085194,-7.711782,-4.254458,-7.862118],[-9.912328,-7.330027,-4.332380,-6.610742,2.281495,-5.884737,7.105821,-1.261105,4.324805,3.640631],[8.262463,5.171527,-6.338998,8.458915,8.511511,-5.531741,-3.160788,-8.913494,0.222399,8.833323],[-4.543472,-6.081360,-7.225921,-9.091397,-7.119215,-5.429388,-3.777291,-5.912214,5.233394,-3.581275],[-2.821306,-1.143176,5.977677,8.992235,8.089498,8.509533,-1.970523,-2.418521,-8.219581,0.671650],[-2.872500,-9.435021,5.697930,6.974064,-5.620950,-1.439797,-0.744851,-5.190575,8.300928,-3.673115],[-7.264820,2.611511,-1.942207,9.277854,-2.241152,7.674314,-9.994334,-7.854498,1.481866,5.269694]],[[0.865606,-7.159943,-7.720883,8.149154,-1.249000,8.485403,6.287665,-1.059863,-9.848832,-2.641570],[-7.523737,5.709508,-8.785165,-2.784790,-4.188818,6.518932,3.295648,2.545672,-4.906431,-0.229230],[9.113034,9.685333,-6.616636,-5.379548,3.190333,6.374416,-6.004189,5.292075,-5.678318,-6.415237],[2.781512,-0.474777,6.330072,-6.640327,-3.539329,5.259475,-5.006433,-8.576819,-2.532700,9.273801],[-5.705710,0.122572,-6.342664,3.185384,-9.815139,2.412717,0.910892,0.485784,9.549194,0.985032],[-6.718540,4.235962,9.791907,2.786768,-4.115810,-8.906494,7.322816,-4.840910,-2.055723,3.340178],[7.053094,-1.360849,-4.149225,-4.788912,6.139181,-1.166628,-4.778761,5.681352,8.664160,0.222893],[6.884989,-8.997648,9.982749,-5.710598,-3.398459,-1.767694,-0.698437,1.326735,-5.090594,3.295929],[0.432660,7.708869,6.401582,8.754098,7.293066,9.145158,-0.456669,-4.701693,-4.940661,8.837475],[-4.321332,-3.504287,-0.732302,1.409878,4.233813,6.752123,-0.231889,-5.537305,4.110113,7.460928],[-7.604862,4.540659,-5.344941,-1.917462,3.995335,-7.846090,-8.849853,-1.138320,-0.717867,4.360074],[-7.735781,-8.383700,-6.530743,8.246445,-4.806836,-5.798190,1.858978,-1.237095,0.072663,-2.544845],[-8.218252,-1.841702,1.444763,-5.269535,1.011588,-2.416553,-9.980308,-8.663786,1.960970,-5.484123],[-4.477042,0.485618,-4.406498,-7.014531,-5.392945,-2.526479,3.427085,3.230935,-6.886286,-7.932816]],[[-3.831403,8.213877,3.214627,6.386036,1.938506,-9.691440,-2.779431,8.142820,1.584625,9.951761],[-1.470999,3.710877,-1.713680,8.087111,-6.369453,-7.646782,-9.823058,9.363893,-0.174959,-2.020477],[-5.458770,9.667092,-4.173700,8.866135,-3.939198,-1.868019,3.893632,-8.796965,-9.593322,-9.102934],[9.793827,8.519764,-2.948848,3.702155,1.290571,7.905155,5.251845,3.878050,6.557257,3.994302],[9.647807,2.367050,5.590764,-6.232804,1.623006,-3.698570,-0.205689,-7.113437,-2.822892,1.832822],[4.334578,5.467498,3.517310,0.980732,-6.787173,3.638761,-8.818722,-2.852078,-4.950331,7.671343],[2.448661,2.114130,-5.212695,-6.105174,3.566194,-0.897511,-9.251185,7.217577,-6.961713,3.448315],[-8.025390,-3.576738,7.453575,-2.528374,-0.629943,6.101528,-1.226507,4.394027,-0.126173,9.449620],[0.316343,-8.529057,-7.746637,3.688921,-3.502357,8.816450,7.838631,0.221719,-0.329684,3.789292],[-5.970936,-9.193550,7.313719,4.618737,0.487920,6.714496,-5.733651,4.117723,-6.587785,-4.478764],[4.724110,5.877910,9.046479,5.785484,-1.855727,-4.410871,5.637458,6.073822,-9.960932,-2.658806],[-1.053399,-5.029304,2.064965,6.204217,3.049778,1.300891,2.307826,8.438165,0.517536,-2.972976],[3.086425,-3.709872,8.023071,9.256037,-1.670007,6.647848,-1.033905,-8.505918,9.766412,8.071875],[9.461140,2.471244,4.685351,3.356182,7.983780,-3.721430,5.296764,2.247406,1.693006,-1.121380]],[[-3.273621,-4.464003,-3.669564,0.661904,-4.716772,-3.862704,6.307106,-7.706636,-6.678103,3.999187],[2.278362,6.648631,4.840906,7.963233,8.368137,-2.226961,7.443632,-7.051870,3.597191,-2.391691],[-9.804771,2.011825,-8.558057,-4.418710,-2.867521,4.700565,-5.235889,-3.496918,0.332019,-2.188162],[9.249981,5.030416,0.874604,-0.760213,9.149658,-8.863858,0.446959,7.120209,4.049883,2.670118],[4.158847,9.406523,1.735873,7.989747,0.651083,9.636324,9.045698,4.243123,0.389956,7.057218],[-8.588244,-8.720110,-7.443042,-3.948517,-1.071591,7.789211,-3.699298,0.622803,-0.301271,-6.491894],[-3.781764,-0.100840,-4.364745,-0.166243,-4.264846,-8.184000,0.300512,-6.577907,-5.461347,2.642984],[-8.944120,9.165058,2.759030,-8.878310,4.464486,1.105853,7.253379,2.818824,1.629089,0.551293],[-1.958044,8.457423,-7.476194,3.309569,-4.671734,1.591329,9.503135,4.321355,1.013160,-8.325566],[-5.336745,-5.822276,7.893431,-6.375064,6.692867,-4.739093,3.228098,2.083705,-9.336282,2.316371],[0.823194,4.931988,7.616703,7.363142,6.624393,7.714572,6.990142,6.268528,-4.841207,-8.634775],[4.206432,8.425135,-8.550802,-3.056811,5.487048,9.436130,5.142449,7.686290,2.081684,7.433903],[-4.018303,-0.921468,8.350827,-5.922547,5.564497,7.488352,-1.610744,-7.129638,-0.327565,8.823168],[-2.945318,-9.113475,9.945562,-1.628673,8.448991,3.313002,-4.074596,8.905274,2.074097,0.269265]],[[-8.908917,0.151763,3.255372,3.588870,2.818635,4.781616,3.746676,3.344709,6.560180,5.248732],[9.012969,-5.118668,8.848513,7.874731,-9.943765,6.712251,-0.183341,9.559379,-1.123877,3.583455],[8.243618,7.302794,-2.761811,3.769609,-7.206703,-3.093810,-7.700169,-2.409218,9.467274,-2.680868],[-1.571790,-0.960106,4.539842,3.286959,5.992447,5.994494,2.541582,4.673341,0.812200,-2.890896],[-3.404309,3.811764,6.630057,-5.978772,-3.930335,-1.341443,-8.905747,4.128791,-6.069455,-3.981040],[4.924140,-6.637609,-7.733417,-8.758996,9.303419,-3.224230,-6.712055,-3.844412,3.695213,-5.957557],[8.090898,-9.042679,1.462033,7.925263,-1.458446,6.037000,6.461392,5.926546,-4.593044,8.316790],[-3.542549,9.544162,-5.121808,-2.430916,-5.952792,3.213232,-5.325798,9.141003,2.545550,8.571017],[-9.147090,3.645157,7.400116,-2.057707,-9.857485,5.244755,8.571704,1.830715,-0.645246,4.529922],[-2.110997,-7.635168,-1.549567,6.725743,5.666969,-7.796868,7.723219,7.850370,-6.615576,-3.928340],[-2.924527,6.561538,-2.619969,0.593060,-1.423025,4.227929,4.254523,3.021128,-6.324123,2.893599],[-7.391327,3.038304,6.636542,-1.786711,-9.073537,-3.721297,-3.115429,-8.530829,5.212975,1.562295],[-1.361757,-4.739229,-7.863108,-8.867608,-2.251982,-4.704786,8.225801,4.011350,9.862385,-1.079507],[-0.677384,-1.440372,-7.956681,-5.618553,-9.877028,1.290585,-0.174405,-1.105190,-9.846985,1.501235]],[[-9.363069,4.442135,-0.362568,-3.219841,-8.840719,2.774986,5.847534,9.801467,9.384859,0.392398],[6.955489,-6.916389,1.381590,-0.125723,1.879460,-4.043412,-2.422001,4.908404,-7.190987,-1.072796],[-6.937722,-5.361716,4.296450,2.726452,0.723918,-7.914663,-1.463106,-5.338378,5.690985,5.542679],[0.837519,-6.349665,3.064198,-6.163245,7.039831,-1.843689,-1.596435,4.323782,-9.522692,-0.006094],[-4.737989,-0.480087,-8.825742,-3.424542,7.758749,-3.112191,7.338174,-5.154045,4.046830,0.068594],[0.500166,-4.494116,-2.600896,6.582429,1.979232,-2.248932,-5.416788,-2.107587,4.559785,-3.796504],[-8.792040,2.143716,9.228338,-7.728467,-0.300879,1.553206,2.814285,-5.064871,-4.397038,-0.252334],[5.713496,1.465802,6.205904,-5.451732,-6.325435,9.359361,-0.104184,-5.622760,8.773255,-3.808374],[-7.283364,5.192671,8.490005,2.336029,-4.671830,1.669444,-5.019007,5.760384,-0.215260,4.052534],[5.086535,2.490634,7.639764,2.621271,-8.745284,7.614800,-2.904615,-2.343215,-9.795749,2.071474],[9.547648,-9.673185,3.389905,5.707947,-3.289579,-4.055878,-3.703373,3.738126,0.188030,-3.936675],[-1.888209,4.216772,-8.943812,-4.003545,9.928043,8.445154,9.186626,1.841551,-9.483128,-3.417927],[6.651414,-0.617996,2.183676,6.194383,-7.774612,-4.916962,4.486295,6.338336,-3.533108,-2.290241],[9.285474,-1.139408,-7.636134,6.075709,5.039517,6.180500,-0.938470,-6.075332,7.793487,4.965084]],[[0.530776,-7.363729,6.531197,-8.883107,0.933429,7.179912,2.354126,5.364404,0.649563,-1.549386],[2.065993,8.217180,9.234204,7.654042,-8.301434,-9.927022,-5.345797,-1.447747,5.145414,2.116154],[-7.413874,6.970527,1.507169,1.960687,-3.625231,3.153637,8.885087,1.628648,-7.319956,1.036726],[8.830750,-6.420120,-0.318705,4.473492,2.612825,-7.164758,-6.623492,3.940034,1.632189,-5.017374],[-8.322394,4.938111,6.927333,-7.443192,3.092360,-0.645142,-5.378289,-4.446789,7.549984,-6.788406],[7.196039,-6.918599,-3.076412,4.486409,-2.290112,6.371907,1.434183,-7.307064,-1.297966,-0.856489],[-2.394408,-9.322642,9.101295,8.516084,1.899321,3.265283,7.676924,-3.201986,-9.647991,2.547370],[5.558211,0.383431,5.139651,5.792705,9.087189,9.463833,-5.197836,-1.044744,-2.160054,2.300763],[9.686818,-0.703186,-3.071921,-7.837434,-8.211938,-8.903952,0.493385,-8.123971,4.889457,-1.867816],[7.526642,8.272596,3.390075,4.014932,7.900263,7.666406,-4.993553,5.475598,-8.245728,1.371700],[6.555426,1.498522,8.260422,6.104412,1.527282,8.190727,6.974880,6.083371,-3.622964,3.781886],[6.709985,-1.833599,-7.387500,-0.685470,-4.298230,-0.746148,5.519516,-7.358815,5.822122,-8.469661],[9.723168,-7.593904,-3.978271,5.647522,-8.482970,-1.134264,-6.825200,6.299079,4.606666,4.807294],[3.395187,9.852517,9.846135,-8.519881,-1.938782,-8.259451,-8.666194,-6.939030,-4.126155,-7.323251]],[[-1.565885,-9.814336,0.824912,-9.443673,7.707684,-7.778804,1.672144,-0.073231,4.441217,7.077291],[1.095839,8.120123,-1.824488,-3.629687,-0.489910,-2.534978,8.502032,3.915324,-2.015354,5.944862],[1.376328,3.864324,-2.226256,-8.548190,-4.066907,1.879754,8.941236,2.752359,-8.010102,-7.057318],[-5.424580,-7.696192,0.506705,4.461188,9.936569,1.640701,-8.304847,1.715542,-6.597894,0.909128],[6.279653,-6.786858,9.851689,0.404951,8.180070,-1.196224,-6.612868,-2.669349,-4.215834,8.155557],[-3.635380,4.948358,0.030524,1.001780,-5.557016,-5.514239,7.698419,-8.053704,0.262907,0.985229],[7.592095,-8.222570,-8.705374,7.687616,-5.725629,-8.280238,0.646677,-6.382741,-2.875774,8.651260],[-8.153890,-6.343602,-0.069429,-4.763697,-1.821840,9.943798,-0.852412,9.068437,-4.459823,0.869952],[-7.412789,8.147816,6.938877,-6.065328,-2.719742,-7.334862,-3.474587,-0.266288,3.625870,-1.625037],[-0.607975,0.305727,2.614576,9.316679,4.995046,4.158416,-6.834516,-6.547957,-1.541220,0.354058],[-9.316819,5.524889,1.196871,1.192920,-9.578337,-5.811169,9.691899,5.406580,1.765333,-0.891675],[-2.248147,-7.008835,9.046666,-2.363327,9.665781,-6.293684,-6.472760,-8.441798,3.430443,-3.506379],[8.742198,0.805333,1.121806,-1.796304,6.633347,9.762446,-1.890871,7.892296,-9.679620,0.572025],[1.646799,0.409604,6.149183,8.706855,-9.086995,-4.196089,0.926332,-0.189914,5.350824,7.644884]],[[-1.365816,-6.072093,-7.269920,-0.838877,1.841063,-3.319619,1.728492,-1.230940,-4.741257,8.808403],[-1.813584,-6.960960,3.952499,-0.761617,0.197521,-1.874412,-5.457622,-6.819398,-8.731361,-6.658435],[-8.190573,-8.529785,-1.865058,-5.966255,4.840487,9.596798,-1.124437,9.487912,4.981468,-9.946350],[3.020819,-0.550959,3.886693,-5.939881,7.537498,1.711526,6.790841,6.811552,9.661990,-5.869398],[5.080003,-1.081331,-1.129446,-3.916327,8.678829,-2.499374,3.260133,-3.882239,-8.663158,-5.313936],[3.139316,3.287960,0.049323,4.752186,5.399305,9.029693,1.845098,-3.027742,2.676575,9.044027],[1.085676,0.275568,-5.715974,9.231440,-5.273665,-2.669432,6.380682,8.548468,-7.926061,2.799774],[-8.045405,2.025741,-8.844127,1.145271,-2.703557,-2.665941,0.785988,-7.709961,-2.835309,-4.261221],[9.281563,-4.427181,-0.183048,6.074411,-7.750027,-9.940710,-6.517438,0.689292,9.647249,-1.295266],[0.318872,1.671722,3.239339,4.204490,8.430203,-3.696002,-1.344198,-4.452885,-9.866317,-6.665053],[-9.102858,-4.182754,-6.219540,-7.379598,-2.493234,9.674998,2.332325,-9.948573,-9.826589,-7.680440],[1.715635,-2.635644,-3.516248,7.595323,-6.926911,6.245090,-4.314745,4.467895,7.549804,8.743457],[6.373504,-1.038612,0.178422,8.304384,-1.971641,-9.280325,-8.802867,6.976382,1.109131,-4.408974],[-9.634427,-3.468773,7.448846,8.797286,7.219863,-9.645260,8.177768,-6.450802,-4.417803,-4.954437]],[[8.999400,-3.034987,7.893306,-3.013309,-2.065681,6.452798,8.836926,-1.808594,0.219623,2.932515],[-8.789795,3.892597,-6.256484,-9.423694,2.651149,3.387720,5.858075,3.003947,-9.943016,7.715438],[-9.808664,6.955910,3.068470,-6.542750,-1.932861,5.596829,8.772625,-2.960217,-0.585938,-5.797058],[-4.993679,4.826185,-6.673920,-1.146631,-8.706569,3.780989,-9.550538,-1.060884,-6.556795,5.541476],[9.678407,7.812692,8.322473,-7.643134,5.054304,-0.684993,5.536594,7.580450,-7.336839,-5.441521],[-3.598234,4.603185,-5.929547,-0.310045,-8.099369,3.619781,-6.601460,-4.140792,6.941859,-7.667085],[-9.791288,-9.840586,-4.948254,4.736733,1.113179,9.671085,5.447762,4.734315,3.897311,2.958876],[1.824531,7.760661,5.174111,2.070764,-9.563555,7.697399,-5.358625,-8.116953,-4.860678,9.109513],[3.026747,1.914337,7.121090,0.577567,-9.598614,-3.293050,9.094279,4.559599,-8.220114,6.958059],[-3.789545,9.313086,-0.697257,1.527732,5.945409,9.868758,-6.164232,4.325745,2.296798,-3.399806],[7.197874,6.832692,-0.890606,-8.753948,7.088224,2.062155,-7.669075,7.252340,5.550750,2.530498],[4.916868,4.007307,6.203948,-7.977829,5.530058,-3.396647,2.975699,-9.068811,3.215445,-4.964200],[-9.912109,-8.062212,-7.943509,-7.875969,5.965656,-6.838826,-6.125460,-3.110998,4.240438,-5.369211],[4.615874,5.869743,-0.782997,-0.831107,-0.298543,-9.558085,-5.886582,-5.436395,-4.136143,-5.246811]],[[-2.924054,8.894825,8.304290,6.496527,-2.352516,7.051507,-6.764792,-3.579541,-4.301658,-2.679610],[-8.968970,-8.944637,-4.084433,5.193921,3.876400,-0.159555,2.254023,-6.634191,0.605851,7.522781],[5.378006,8.286870,4.207111,-6.528291,-3.649603,9.819383,3.402692,4.985406,-8.363441,2.351634],[6.306844,1.006896,2.146851,2.460266,7.510857,-7.904908,7.414225,0.073374,7.722331,1.895048],[-8.893487,-4.678329,-5.736378,5.276644,9.075088,-3.078008,-4.072513,3.158451,6.896117,-2.536690],[8.219861,3.203051,-9.945053,2.247647,-4.775925,0.570016,9.596699,-9.950160,-7.697155,-6.210580],[-2.306908,-8.406045,4.416712,-6.651190,-7.825421,6.033848,5.800882,-3.047029,5.490544,-3.309942],[-1.556698,3.754775,8.244717,1.196660,9.250807,8.626253,-4.770520,5.488465,9.528705,-3.261025],[-2.783519,2.606770,-6.589311,-5.254311,-5.549816,6.118327,-9.682808,-0.934675,3.065414,5.920888],[-9.512949,-1.949635,-5.212046,-8.951048,-9.416439,3.187365,-5.451708,-7.985930,4.441747,8.615067],[8.940848,-2.423347,4.637047,-7.985066,7.693980,1.847018,-7.511265,-7.011365,9.796413,5.529038],[-5.808550,9.974245,1.951757,8.822551,-0.782652,-3.043729,-7.935939,5.883184,-6.732155,-3.857982],[-4.561348,3.102774,7.833979,5.150186,-2.696429,-7.827917,-8.341356,7.919292,-9.648438,-2.233260],[7.415658,-8.143662,4.492051,9.345053,0.256256,2.279280,-3.884566,9.651036,1.640966,-2.428070]],[[7.115335,-2.427384,-0.293666,5.602596,-1.675717,7.220516,7.872707,7.569134,-9.589120,-8.608989],[-8.592026,1.286541,-5.186111,3.473114,5.617049,4.480224,-8.061350,-8.316185,3.451955,7.501391],[9.347897,-9.376046,8.991332,-0.242907,-7.149750,0.923006,-9.260240,8.897440,6.115556,-8.892908],[8.825142,4.340177,1.168600,-5.119192,-0.694535,5.770019,5.428271,-0.875239,5.692722,-7.092451],[5.160716,7.529231,-0.537520,-5.100335,6.326757,-2.106377,-5.986837,-9.995074,-6.022065,-3.226987],[3.471060,-0.328929,5.936522,9.235572,8.811925,3.923731,8.953730,4.667909,2.482781,-0.963664],[-7.341968,4.565090,-1.228749,6.103793,0.525238,8.610788,4.826264,9.022420,-4.326086,1.079015],[-6.521693,-4.125073,9.793549,1.160853,2.222764,7.615472,-6.194471,-2.000550,5.415505,5.147676],[-0.033956,4.662663,8.323177,-3.793493,8.629784,9.581862,-3.857404,9.461866,8.498045,5.528005],[-5.568988,2.007347,4.036460,-6.723443,2.118180,8.717883,-2.050111,1.377832,5.384534,-7.148101],[8.202568,-9.143605,8.601902,-6.713634,-1.182817,-6.294818,-2.902362,-9.192415,4.459883,-9.113557],[-1.106420,-5.693669,-0.859783,-2.559343,-0.547487,-2.910602,0.164186,0.601340,7.193720,8.446889],[5.362133,-2.587452,3.765672,-1.028163,4.287913,2.040962,-5.544361,1.978795,0.441002,0.721558],[-7.317183,-4.444566,-6.333126,-7.321560,3.335422,-0.919391,4.272635,-3.493492,8.856246,-4.151627]],[[-3.577220,-0.874003,8.857686,5.551170,-2.328446,-3.734102,6.442945,-3.800873,0.696351,2.670661],[-6.995217,0.191671,-1.310443,0.937633,-1.277411,6.385701,4.329363,-9.444312,4.585772,-2.221374],[-4.477344,-7.300138,1.659975,9.395389,0.386858,6.700553,-8.163788,-0.968762,-2.147054,-0.753548],[5.668764,7.158564,-2.800117,1.524697,-2.521325,1.388134,1.948903,-6.003241,-9.302046,6.170323],[-6.096061,0.055633,1.318449,2.193420,5.377782,6.172652,6.857190,-7.893508,-5.587510,5.927864],[8.969218,4.418598,-1.457265,0.845381,1.362095,6.087784,6.382325,0.393022,-5.724624,-2.551117],[-0.141113,-6.966837,5.169474,9.921658,-9.418095,-5.096906,2.447861,-6.582193,2.007510,-6.740490],[-3.085077,-1.697661,1.418150,7.672516,-8.018764,8.751486,1.428676,5.506526,-7.150250,-0.240348],[4.282547,-5.060449,-6.601876,2.373299,-1.284782,-3.060772,8.694396,-0.791810,-8.538045,-5.025235],[-1.054755,-0.008944,8.333391,-6.036378,-8.669016,-5.894069,1.442432,8.250576,-9.864879,9.579475],[-0.293580,3.147510,-2.563779,-4.921299,9.508405,4.196122,0.095834,9.769960,1.649746,-2.833753],[-6.759715,-4.641662,-1.529873,4.248744,-8.457342,6.119256,7.311500,-5.527884,6.978236,-7.446517],[6.018472,-2.009437,9.578485,9.384853,4.518741,2.124673,-2.906093,5.281884,4.776299,7.963156],[3.414006,-4.400633,-1.543790,-5.161108,-9.448290,-6.261295,-2.999667,-6.787934,8.124467,7.516922]]], dtype = "float64")#candidate|10418|(14, 14, 10)|const|float64
bop_10419 = relay.left_shift(call_10378.astype('int8'), relay.reshape(const_10418.astype('int8'), relay.shape_of(call_10378))) # shape=(14, 14, 10)
bop_10422 = relay.left_shift(call_10379.astype('int8'), relay.reshape(const_10418.astype('int8'), relay.shape_of(call_10379))) # shape=(14, 14, 10)
output = relay.Tuple([bop_10396,call_10404,var_10405,bop_10419,])
output2 = relay.Tuple([bop_10399,call_10406,var_10405,bop_10422,])
func_10431 = relay.Function([var_10405,], output)
mod['func_10431'] = func_10431
mod = relay.transform.InferType()(mod)
mutated_mod['func_10431'] = func_10431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10432 = relay.var("var_10432", dtype = "float64", shape = (924,))#candidate|10432|(924,)|var|float64
func_10431_call = mutated_mod.get_global_var('func_10431')
call_10433 = func_10431_call(var_10432)
output = call_10433
func_10434 = relay.Function([var_10432], output)
mutated_mod['func_10434'] = func_10434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6243_call = mod.get_global_var('func_6243')
func_6244_call = mutated_mod.get_global_var('func_6244')
call_10473 = relay.TupleGetItem(func_6243_call(), 0)
call_10474 = relay.TupleGetItem(func_6244_call(), 0)
output = relay.Tuple([call_10473,])
output2 = relay.Tuple([call_10474,])
func_10479 = relay.Function([], output)
mod['func_10479'] = func_10479
mod = relay.transform.InferType()(mod)
mutated_mod['func_10479'] = func_10479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10479_call = mutated_mod.get_global_var('func_10479')
call_10480 = func_10479_call()
output = call_10480
func_10481 = relay.Function([], output)
mutated_mod['func_10481'] = func_10481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8535_call = mod.get_global_var('func_8535')
func_8537_call = mutated_mod.get_global_var('func_8537')
call_10498 = func_8535_call()
call_10499 = func_8535_call()
output = relay.Tuple([call_10498,])
output2 = relay.Tuple([call_10499,])
func_10525 = relay.Function([], output)
mod['func_10525'] = func_10525
mod = relay.transform.InferType()(mod)
mutated_mod['func_10525'] = func_10525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10525_call = mutated_mod.get_global_var('func_10525')
call_10526 = func_10525_call()
output = call_10526
func_10527 = relay.Function([], output)
mutated_mod['func_10527'] = func_10527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7430_call = mod.get_global_var('func_7430')
func_7431_call = mutated_mod.get_global_var('func_7431')
call_10531 = relay.TupleGetItem(func_7430_call(), 0)
call_10532 = relay.TupleGetItem(func_7431_call(), 0)
func_4895_call = mod.get_global_var('func_4895')
func_4902_call = mutated_mod.get_global_var('func_4902')
const_10549 = relay.const(False, dtype = "bool")#candidate|10549|()|const|bool
var_10550 = relay.var("var_10550", dtype = "bool", shape = (42,))#candidate|10550|(42,)|var|bool
call_10548 = relay.TupleGetItem(func_4895_call(relay.reshape(const_10549.astype('bool'), []), relay.reshape(var_10550.astype('bool'), [6, 1, 7]), relay.reshape(call_10531.astype('float32'), [120, 4]), relay.reshape(var_10550.astype('bool'), [6, 1, 7]), relay.reshape(call_10531.astype('float32'), [8, 15, 4]), ), 0)
call_10551 = relay.TupleGetItem(func_4902_call(relay.reshape(const_10549.astype('bool'), []), relay.reshape(var_10550.astype('bool'), [6, 1, 7]), relay.reshape(call_10531.astype('float32'), [120, 4]), relay.reshape(var_10550.astype('bool'), [6, 1, 7]), relay.reshape(call_10531.astype('float32'), [8, 15, 4]), ), 0)
func_2152_call = mod.get_global_var('func_2152')
func_2155_call = mutated_mod.get_global_var('func_2155')
var_10556 = relay.var("var_10556", dtype = "uint64", shape = (1152,))#candidate|10556|(1152,)|var|uint64
call_10555 = func_2152_call(relay.reshape(var_10556.astype('uint64'), [12, 16, 6]), relay.reshape(var_10556.astype('uint64'), [12, 16, 6]), )
call_10557 = func_2152_call(relay.reshape(var_10556.astype('uint64'), [12, 16, 6]), relay.reshape(var_10556.astype('uint64'), [12, 16, 6]), )
func_1280_call = mod.get_global_var('func_1280')
func_1283_call = mutated_mod.get_global_var('func_1283')
var_10585 = relay.var("var_10585", dtype = "float64", shape = (360,))#candidate|10585|(360,)|var|float64
var_10586 = relay.var("var_10586", dtype = "float64", shape = (462, 2))#candidate|10586|(462, 2)|var|float64
call_10584 = relay.TupleGetItem(func_1280_call(relay.reshape(var_10585.astype('float64'), [9, 10, 4]), relay.reshape(var_10586.astype('float64'), [154, 6]), ), 0)
call_10587 = relay.TupleGetItem(func_1283_call(relay.reshape(var_10585.astype('float64'), [9, 10, 4]), relay.reshape(var_10586.astype('float64'), [154, 6]), ), 0)
func_9615_call = mod.get_global_var('func_9615')
func_9617_call = mutated_mod.get_global_var('func_9617')
call_10588 = relay.TupleGetItem(func_9615_call(), 1)
call_10589 = relay.TupleGetItem(func_9617_call(), 1)
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
call_10598 = relay.TupleGetItem(func_7482_call(), 0)
call_10599 = relay.TupleGetItem(func_7484_call(), 0)
output = relay.Tuple([call_10531,call_10548,const_10549,var_10550,call_10555,var_10556,call_10584,var_10585,var_10586,call_10588,call_10598,])
output2 = relay.Tuple([call_10532,call_10551,const_10549,var_10550,call_10557,var_10556,call_10587,var_10585,var_10586,call_10589,call_10599,])
func_10604 = relay.Function([var_10550,var_10556,var_10585,var_10586,], output)
mod['func_10604'] = func_10604
mod = relay.transform.InferType()(mod)
mutated_mod['func_10604'] = func_10604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10604_call = mutated_mod.get_global_var('func_10604')
var_10606 = relay.var("var_10606", dtype = "bool", shape = (42,))#candidate|10606|(42,)|var|bool
var_10607 = relay.var("var_10607", dtype = "uint64", shape = (1152,))#candidate|10607|(1152,)|var|uint64
var_10608 = relay.var("var_10608", dtype = "float64", shape = (360,))#candidate|10608|(360,)|var|float64
var_10609 = relay.var("var_10609", dtype = "float64", shape = (462, 2))#candidate|10609|(462, 2)|var|float64
call_10605 = func_10604_call(var_10606,var_10607,var_10608,var_10609,)
output = call_10605
func_10610 = relay.Function([var_10606,var_10607,var_10608,var_10609,], output)
mutated_mod['func_10610'] = func_10610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9920_call = mod.get_global_var('func_9920')
func_9922_call = mutated_mod.get_global_var('func_9922')
call_10631 = relay.TupleGetItem(func_9920_call(), 5)
call_10632 = relay.TupleGetItem(func_9922_call(), 5)
output = relay.Tuple([call_10631,])
output2 = relay.Tuple([call_10632,])
func_10633 = relay.Function([], output)
mod['func_10633'] = func_10633
mod = relay.transform.InferType()(mod)
mutated_mod['func_10633'] = func_10633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10633_call = mutated_mod.get_global_var('func_10633')
call_10634 = func_10633_call()
output = call_10634
func_10635 = relay.Function([], output)
mutated_mod['func_10635'] = func_10635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3182_call = mod.get_global_var('func_3182')
func_3183_call = mutated_mod.get_global_var('func_3183')
call_10687 = func_3182_call()
call_10688 = func_3182_call()
func_9319_call = mod.get_global_var('func_9319')
func_9321_call = mutated_mod.get_global_var('func_9321')
const_10708 = relay.const([8.637670,-8.381289,-6.401573,8.586771,-9.857890,8.082866,4.242985,-8.513039,-1.440359,-0.480141,2.836182,-3.147253,2.703367,4.759750,6.643732,-1.592607,2.377494,0.197955,5.179760,7.475213,-7.158966,-3.256588,-8.861007,-3.367532,6.139897,-0.856313,0.669806,1.435081,6.577653,8.956378,6.304891,2.882207,-7.341765,8.831573,3.336074,-6.585184,7.823253,8.500805,0.378799,-5.878004,-7.999920,-7.206114,-2.092162,8.870801,-9.991358,-2.863184,-1.915804,-3.300555,-0.397173,-7.588317,9.515913,-9.657468,-7.425840,-0.769240,7.588768,-0.035166,-4.152425,7.970394,-1.968814,-4.238594,-1.103161,0.120660,-6.150154,0.866208,4.454982,-9.323318,-5.660393,9.826654,-0.221823,1.385973,2.663998,-4.448158,-2.422713,-7.788052,-3.219127,0.155274,1.788604,4.570140,-3.958922,9.436735,-6.600468,-3.354297,-9.573940,0.174937,-6.076708,-7.729015,5.016512,8.402812,-2.001356,-3.998576,-3.985592,0.360274,-3.739772,7.402118,-7.000238,-7.766755,-5.283915,9.822389,0.588624,7.937266,8.463706,8.230784,-9.975349,-6.274170,-5.104828,4.739515,-5.802146,-2.073453,9.264943,-6.484256,-7.053025,7.568566,6.429609,2.689942,2.615312,-6.722194,-7.697081,6.976824,-6.642448,-9.435248,5.234654,7.926698,-5.975892,-2.741883,0.876935,3.726889,-2.522996,-6.786144,-9.775268,-9.252399,1.958031,-3.843091,-9.956175,-8.820941,-5.128256,1.432434,9.882342,9.454686,-5.051220,8.216164,-6.041867,-4.378351,0.437964,2.875087,-4.297910,-0.591347,-4.737418,-5.416632,-0.840049,-2.969611,4.691797,-0.806914,-5.747638,-4.274016,-7.611323,2.370959,4.363028,4.857151,-3.246845,-1.096859,-3.324789,-7.615735,2.607286,5.857954,-0.604085,-5.444865,2.346314,-8.742082,0.647449,-3.810544,-4.868028,-8.935815,4.020259,0.454231,-8.915414,7.535040,-0.288383,-4.268403,-4.977979,8.975701,6.368802,-0.887233,8.814921,-6.005855,8.529320,-1.778923,-3.441496,8.753690,-9.354270,-8.512175,-5.030863,1.882343,8.832556,2.574191,4.377966,-5.159743,-2.480694,9.959107,6.195561,-7.260519,-5.404795,0.106826,-9.708824,7.380211,5.259057,3.114141,8.448841,-5.629996,-5.130165,-0.161566,-1.373495,-0.035869,6.470991,-8.633334,-1.165315,6.328746,9.662228,5.650436,-3.990631,-9.775083,-3.887175,3.181368,-8.850005,0.738767,5.838272,-1.308047,-2.788731,5.541737,-8.328215,2.975625,-2.154011,-0.792833,8.601742,7.025632,-6.517598,5.442056,-7.744723,-4.924533,-8.287438,4.546203,2.406530,1.649270,3.787396,7.906230,2.763203,-0.970277,9.389720,5.340464,-4.526569,-8.882368,6.183145,-0.740763,1.085705,-6.616238,-0.719818,2.991103,-6.800893,8.566246,9.276418,3.257527,0.340671,6.050678,-9.727663,8.563072,3.595240,3.797993,2.335912,-0.081401,-6.900415,-4.032151,9.595423,-8.472068,5.437054,2.138666,-4.840632,0.133931,-8.808030,1.432417,1.995871,7.215106,-0.831190,2.590066,-4.746907,-4.269749,3.407841,8.093625,0.560599,-9.081816,-1.420810,9.329211,-2.517386,-5.730251,1.922121,-7.170646,6.153901,-0.652273,-8.443734,8.157049,6.633386,-6.532475,7.987406,3.416883,3.150356,4.447250,6.195747,8.844142,6.753583,-5.248312,1.253268,7.043053,4.556784,-0.981274,-3.369807,-4.539260,-4.802466,-1.361145,7.063632,-9.774448,1.604719,-7.562190,-7.577983,-7.630459,8.143982,7.204368,0.999912,1.424722,-4.054078,9.832091,-1.582018,-7.034619,-9.809756,-1.490563,1.352262,-5.503678,-5.660079,6.576526,-9.245769,-1.852273,9.283612,-1.919236,-0.734562,5.659656,-0.055209,9.018607,-6.088296,6.213911,-4.844039,-1.325866,-2.566570,-4.236699,0.107547,2.572164,-9.475336,-7.100847,7.292880,-4.455569,-7.043390,-0.899047,-8.280598,7.728278,-9.719416,6.999796,-3.121495,-4.532408,9.198809,6.223015,-5.512023,-9.730457,-0.106499,-5.037361,-5.857942,-5.447135,-8.064067,0.143720,-0.635903,-9.234244,1.895879,-6.219389,1.010733,-1.993048,6.373816,-9.437284,-3.756117,-1.624187,7.141355,7.095894,-2.007276,-0.769046,-2.971649,6.840134,9.985488,3.441959,-8.151961,-1.948943,-2.426417,-3.693152,1.590820,-2.218949,8.705574,-8.644145,8.635080,-2.265516,9.432043,8.064860,-4.493585,1.196361,-9.700596,-7.237164,-5.066685,-2.014857,3.636785,-9.149623,9.232878,4.133198,-4.234971,6.794278,2.685475,3.031118,2.037334,-1.192848,8.611378,6.478204,1.782434,-2.290635,-1.646441,-6.075305,7.935393,-3.409935,4.015410,-4.628629,-2.128883,-7.743119,3.782283,-9.615845,-2.280673,1.732926,-1.928610,7.752832,-9.400846,5.202250,-6.965195,9.322649,9.884550,8.775049,2.459720,-4.387551,2.159701,7.764285,-8.179235,1.110523,-0.292315,-2.054208,9.509632,-8.989726,-6.325082,6.813684,-7.889788,-8.064573,-0.280875,-3.976798,6.988350,0.864382,2.069782,-4.337691,4.262814,-3.736060,-1.643201,-7.138535,-2.124884,8.963925,2.891562,-8.812695,6.134354,6.327217,-2.435763,4.270264,-8.099832,-8.234440,7.003217,9.349715,4.120208,2.389262,-2.148025,7.158589,-4.563753,5.417446,2.378351,5.789669,5.687763,0.167526,3.551760,4.071681,0.789415,4.700835,-6.406186,3.291831,3.497400,6.047417,3.835580,-2.239258,-7.596123,6.793600,8.545329,-1.941223,1.234368,-2.596473,9.423003,-3.761301,-7.853776,9.223374,-3.239143,-8.491351,1.625724,3.834138,-9.020901,8.586962,-0.902343,5.931724,8.067643,-3.431559,1.918593,9.593648,-5.530662,9.392722,-8.867419,-0.822511,-5.894037,-1.343156,-6.710950,-5.465133,5.457948,4.175503,-0.089143,-3.254162,5.213101,-4.746478,1.378483,6.839808,6.380042,-9.042445,1.419378,-0.324512,3.976683,-1.110903,-1.347325,7.455202,-8.653864,1.768072,3.875850,-8.479302,-4.270991,4.905651,7.718608,-0.809368,5.989663,-8.778401,0.438179,-8.317297,3.466270,-2.869931,3.214422,0.645773,0.419439,-9.378971,-4.508331,7.290620,3.018236,5.496302,5.563515,1.073766,-6.099604,5.431791,-0.294481,4.849384,-3.422926,-2.397164,6.623894,8.533236,-3.779505,3.668659,9.058814,-0.718524,0.833115,3.465933,6.839471,7.791233,-3.324749,5.529836,5.441350,-5.146467,-0.064815,2.212091,-5.768654,-5.576372,3.865527,-2.888791,-9.091117,4.382786,-4.462599,-4.104736,-0.312660,5.293824,9.869469,6.579141,8.426977,-6.326086,-3.650498,9.904987,8.675538,-9.712896,0.877796,0.599418,0.901165,8.936149,0.848139,2.912977,-4.990055,-2.114868,9.817753,-4.268320,1.430628,-2.709233,-0.508580,-9.994617,-5.586743,-5.981682,1.127666,2.056045,5.193258,-6.273422,3.593470,-8.764801,4.720675,7.337088,-6.383847,2.379626,-6.918573,-6.843573,-5.953802,-0.404951,0.601767,-8.477502,-1.487749,0.918046,5.506491,-7.556473,1.583127,-5.831056,3.791729,6.383174,6.157778,3.892422,-4.958572,-2.438172,9.195689,7.916671,-9.610893,4.633562,-8.577337,-6.639610,7.810754,-6.945596,8.805906,5.820288,-2.740301,-3.780671,9.400908,0.006386,4.648736,-0.548821,3.716294,0.390789,-3.577948,-5.751608,6.483400,-4.587877,-9.280476,3.178095,9.224326,-9.688108,1.721036,7.884143,7.212170,8.163463,-5.280984,9.018578,0.240094,9.226960,3.609255,-6.705306,-8.082357,3.644058,1.128789,-8.274112,2.479713,-2.936498,-0.907310,-1.073538,7.335389,-0.432484,7.771953,3.582782,3.556155,-7.199704,-1.822144,7.914290,6.919598,9.854742,-7.643604,3.716752,0.250920,-4.189302,5.497192,2.901828,-0.353927,7.564776,8.132171,9.958553,3.332618,7.985778,-0.282033,4.662386,-4.641896,9.990071,-6.533186,-4.153790,-3.158104,7.978960,6.655151,-4.419162,4.801340,-0.051432,-7.127544,3.576156,8.486718,-4.188793,5.534277,-6.444453,-9.293298,-0.206526,-9.692606,-3.587785,-7.627719,5.200182,-1.211958,4.202772,6.444961,-1.282416,6.466235,0.209028,7.681897,0.705639,6.987046,-0.957191,2.248293,5.768211,9.829695,-5.564659,9.752685,-7.774597,-2.996094,1.450489,5.246325,1.139953,5.648006,1.788585,-8.522592,-7.176748,-9.766554,-8.852005,8.111225,-8.039561,2.811069,-1.473803,-1.661688,2.128627,5.436918,-8.533118,-3.620418,6.797930,-4.186535,-6.530828,4.922423,9.638135,1.356364,8.961222,2.459065,-7.374111,8.545582,9.541356,6.649650,-0.537792,-4.514536,0.423379,-9.979200,-9.631751,8.310565,-6.200900,7.609591,3.627119,6.501338,-2.707907,-7.557503,6.835719,6.541662,9.598622,9.014933,2.188422,-1.355045,9.786938,-0.068771,3.953275,-6.359995,-2.271001,5.837020,6.753353,8.094054,2.754804,-4.805421,0.905630,-5.548417,-0.669882,-6.886956,1.024949,-5.470804,3.945940,-3.655909,-0.544619,-0.141712,3.819177,-5.439064,-1.193767,-8.155127,9.186297,5.595503,-0.509832,3.027377,0.070639,4.998036,-2.574725,2.617293,-6.010201,0.779402,6.070852,2.491669,0.647352,0.507486,9.032939,-0.185941,-9.929211,2.593616,0.708951,2.468712,-2.852987,4.220096,-4.058315,4.949442,-9.206422,2.273582,-5.059319,-2.874730,5.981171,-6.329099,4.319757,8.828659,-4.263915,9.792028,-3.134998,-5.630114,8.664694,6.803077,9.199686,-5.088696,3.936037,9.887134,-6.887608,-3.859539,1.370978,5.276311,3.277552,-7.697204,8.999087,7.870413,-8.165970,4.594579,6.194700,6.801421,7.781462,-8.385206,4.471132,-0.529111,-2.117617,5.564712,6.740219,-8.815363,-2.549483,-1.689070,-5.788464,8.079181,-0.028755,-3.686343,8.933143,-9.989526,4.835254,-1.933929,-8.026528,8.600315,4.914995,-0.602502,2.073040,6.207147,4.967537,8.624279,3.772923,-0.300758,8.454009,8.182077,-9.164887,0.494040,-6.754061,-3.935370,3.231180,4.466226,4.249426,1.767820,8.732031,-0.975857,4.832276,-2.684218,-7.398240,-3.387558,-8.967386,-1.944382,3.812210,-5.923752,5.663770,-9.990731,-0.461557,2.845597,4.842377,-6.978521,5.373133,1.512429,5.255029,5.923102,-6.775826,8.842616,9.409325,7.292436,-2.620893,3.384339,-7.364377,-1.916804,9.649008,-0.445867,-3.426437,0.366769,2.625224,-2.682265,1.881437,-7.694033,6.999377,-4.843346,-7.034194,4.714730,3.175806,-4.869473,-4.385957,2.440057,8.698660,-3.499827,-8.859627,9.619321,-5.996437,-1.246963,-0.221112,3.447635,7.962734,-6.028430,3.708845,-7.861878,-6.206245,3.070949,9.633820,4.104972,-2.337506,-5.280564,1.260734,7.225681,-7.509974,4.552152,-5.515040,-1.994779,-8.408443,1.323594,5.269403,5.949801,0.646634,-5.436743,9.950264,5.930311,-4.054230,-2.103390,5.105296,9.140956,-3.025009,-0.013920,-3.927752,-7.186191,-3.503467,-1.817030,5.928328,3.924170,-5.208731,7.997153,4.635631,-0.632991,-7.743577,-0.612588,-2.839424,0.057414,-1.610287,6.800301,7.932663,-4.554664,-8.654705,4.294919,-1.387874,-7.866036,-1.179878,-6.119570,-9.962219,2.372792,7.827261,-7.710390,-8.302915,-2.321001,-7.658367,6.983313,4.621905,9.184896,-6.461970,8.200751,9.242182,-5.548978,8.738827,-4.364572,7.170060,2.021886,8.681883,-7.525822,6.859973,-5.768423,-3.576154,5.546463,5.260405,2.942481,6.605366,-4.371485,-7.145211,0.635893,2.315541,0.917999,8.620077,-8.269401,5.279516,-6.183366,7.606226,-7.380543,-0.430180,-5.768204,-1.399361,-3.942882,-7.342676,-0.658300,5.403814,8.848136,0.317583,4.840070,2.919142,7.998148,-9.711608,4.441056,3.175345,4.459233,-5.437168,5.877238,-6.049180,-3.975497,1.434679,1.349599,-4.700247,3.699824,-0.583408,0.336531,-1.096743,-2.975350,-2.775525,6.737545,5.905743,-8.590380,-4.812429,-7.813808,8.706192,2.602188,2.233582,3.510418,5.321702,-7.961882,5.036343,5.311856,-2.530171,-2.308684,-6.753925,-4.187576,-1.441650,4.853045,7.410577,4.018779,-8.172029,1.993200,-6.745710,-1.982185,2.648496,0.188673,-4.288809,2.442417,-6.114768,2.715741,3.451042,-8.985564,-3.884378,-1.297390,4.428189,-5.861071,-2.902915,3.416207,-3.087633,8.246928,-2.344490,-7.908065,8.996909,-1.443274,2.661926,-3.667835,5.311093,2.507343,-8.783224,5.284194,2.814912,-7.488648,9.740693,-0.909020,0.960230,-4.499398,-6.691817,-2.200553,-8.339369,9.210097,-1.147440,-6.224744,-1.980559,-6.456020,5.462418,-4.644321,5.094143,-6.522805,8.329100,9.689727,-2.471071,-6.044857,-6.376156,1.487563,7.537633,9.653454,-6.603591,-9.569787,6.735374,-3.223046,-9.148218,5.185528,5.909329,0.391306,3.284127,8.371389,-3.747426,-0.764983,-9.107915,8.209423,2.175466,0.166852,-6.876712,-7.529826,-6.118724,-8.194310,-4.280924,5.505472,4.429622,-8.705383,5.163050,2.124113,2.544631,-5.339109,8.025353,-2.442275,-4.870100,-7.923426,6.159313,-0.642348,5.158854,-7.748754,6.312711,7.851072,-7.637097,8.099990,1.088003,1.162587,-1.400644,-2.059077,6.234874,-5.506569,5.073053,-3.327096,-0.870097,-9.170597,0.204011,8.190511,-5.764475,-0.880244,-3.358446,-0.153518,-2.402688,-8.849417,-5.873141,-7.455924,9.749218,5.937881,1.981580,6.722069,7.227313,-6.553572,0.715559,5.409737,-2.396794,-0.405155,2.396222,6.477931,5.470647,-6.801603,-7.178326,4.493511,-8.018271,-3.021679,1.912657,2.604099,-9.538552,7.577324,0.431382,1.492395,-6.808303,-9.411915,4.649300,2.896684,8.916686,-3.700292,-4.483495,-6.093724,-5.882236,5.922317,-9.934492,-5.491816,-6.028491,-3.610205,-0.714413,7.499265,-1.417182,-1.609638,4.972398,-2.819968,-5.683832,8.672095,-9.462064,2.947484,-2.162271,-0.288027,8.105007,4.577645,2.642847,5.421217,-5.904454,-5.878804,-9.291499,-3.635446,9.736165,-7.884415,1.449600,-9.291817,0.234859,-9.897431,-4.901111,8.166730,-5.882711,0.616650,-5.204373,1.916530,-8.058295,6.540407,3.181819,-9.977007,-7.103658,-1.715028,-9.818121,-0.532568,-2.035835,-3.647317,1.144357,-9.198938,-0.308911,5.648410,-4.492947,6.336210,6.548211,4.382005,-5.246793,7.259657,-3.409016,-2.536456,-4.312164,4.083439,-7.919758,-8.111894,0.856051,3.712838,-9.042257,-5.680582,4.008774,5.977491,4.465292,6.930353,0.069161,-1.314085,-9.698123,-1.017629,9.754538,2.436029,8.530361,-9.630300,-2.110366,7.000349,-8.800707,1.851411,6.691047,-2.460931,0.830142,1.297589,-4.027406,3.234439,-0.628939,-6.400054,0.734302,3.798442,2.013876,3.171038,0.263495,-4.893303,-5.231854,-1.389814,6.796921,-5.779535,-8.131155,6.513541,-3.881583,-8.018612,-5.636938,-6.566782,-2.453921,4.224007,2.407155,-2.641687,4.996878,1.451594,-2.945726,2.078593,-4.021003,1.213347,3.407172,-3.885584,6.013823,5.596015,2.397254,1.904590,7.135569,8.756259,6.257489,-4.424831,-0.715823,-7.251122,4.233163,-9.696517,-6.737350,-6.292501,-5.896595,2.595245,4.248377,-2.158785,-4.139867,1.588582,-5.252217,1.859978,-0.195106,-6.349278,0.611832,7.955234,-9.252322,-7.376583,1.010830,7.219891,7.524379,0.428652,9.836807,4.620806,2.697428,3.798728,9.025518,0.993917,-5.935132,4.634845,7.080830,-4.439543,-0.570076,-5.839915,-1.377997,-5.974563,-7.664381,-4.109040,7.151018,6.911377,-3.607503,-3.019237,0.283724,8.541879,1.950579,0.974824,-2.933360,-5.807364,4.261396,-6.818665,-1.837757,1.146392,5.848761,-3.052689,-4.561330,4.362085,7.272248,-3.974821,-2.657150], dtype = "float64")#candidate|10708|(1456,)|const|float64
call_10707 = relay.TupleGetItem(func_9319_call(relay.reshape(const_10708.astype('float64'), [13, 16, 7])), 0)
call_10709 = relay.TupleGetItem(func_9321_call(relay.reshape(const_10708.astype('float64'), [13, 16, 7])), 0)
output = relay.Tuple([call_10687,call_10707,const_10708,])
output2 = relay.Tuple([call_10688,call_10709,const_10708,])
func_10722 = relay.Function([], output)
mod['func_10722'] = func_10722
mod = relay.transform.InferType()(mod)
mutated_mod['func_10722'] = func_10722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10722_call = mutated_mod.get_global_var('func_10722')
call_10723 = func_10722_call()
output = call_10723
func_10724 = relay.Function([], output)
mutated_mod['func_10724'] = func_10724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8535_call = mod.get_global_var('func_8535')
func_8537_call = mutated_mod.get_global_var('func_8537')
call_10765 = func_8535_call()
call_10766 = func_8535_call()
output = relay.Tuple([call_10765,])
output2 = relay.Tuple([call_10766,])
func_10767 = relay.Function([], output)
mod['func_10767'] = func_10767
mod = relay.transform.InferType()(mod)
output = func_10767()
func_10768 = relay.Function([], output)
mutated_mod['func_10768'] = func_10768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_10796 = func_3759_call()
call_10797 = func_3759_call()
func_8784_call = mod.get_global_var('func_8784')
func_8787_call = mutated_mod.get_global_var('func_8787')
const_10815 = relay.const([-3.817325,8.085590,-5.184212,3.079834,2.709677,-0.702950,0.293316,9.369583,0.264699,-8.953435,-8.320703,-2.307632,2.198848,-4.600542,-3.943872,-0.407231,0.494826,2.665024,-4.971669,7.801950,6.476961,9.565146,-7.315054,-7.169923,8.231049,1.109601,-5.961026,2.513792,-6.309235,9.621212,8.060198,5.067718,7.019798,3.572026,-7.648335,9.581411,-5.415719,-3.398508,0.987743,-6.144634,-4.193877,-7.894034,8.345439,-9.612095,-5.481850,-4.256894,6.901937,-1.350215,-6.384400,-6.012949,-1.778014,4.546633,9.453404,0.654274,-1.363016,3.952971,3.007463,-4.913812,7.754748,-3.281161,-6.852267,1.104605,4.714001,-1.464620,3.788535,-5.465352,0.014039,-2.887816,2.179170,7.855102,3.427804,-6.081044,3.807201,-7.796229,3.261975,-7.657513,6.477224,2.376733,3.918086,7.925061,8.518295,-2.955331,4.303288,5.554635,-3.900634,-8.835628,8.568124,3.473176,2.609407,3.446194,-7.836842,-8.155085,1.963582,-1.060000,-7.722310,-3.953710,9.550218,-7.862202,8.518925,-7.853820,-4.415604,-8.056754,5.999574,-5.670548,0.682428,-3.404597,3.398801,2.850823,-5.348704,2.044672,1.111485,-6.919867,-0.965249,5.060378,-1.527204,-2.247221,6.426309,-7.194482,-4.104888,7.846885,-7.005962,8.287161,9.769928,8.944859,5.939289,-3.487527,-0.715997,6.334086,5.184858,-0.206550,-9.428986,-4.810846,3.314962,0.659035,-2.607464,3.114159,-3.617766,-2.093136,-4.890335,0.870601,8.466886,-7.087741,9.909044,-9.369884,6.849023,-3.695185,8.179773,8.148654,-6.810395,-4.596993,1.440837,9.843034,2.843953,3.680947,0.638623,5.317654,-6.503546,-2.749378,7.802926,-0.924982,-8.640625,0.508287,-1.952316,-9.257306,4.587901,9.448957,4.190381,-6.087511,-9.413943,-7.889215,-0.944555,-3.224055,4.097121,-4.591861,-8.558155,1.152289,-1.415154,-4.976747,5.106011,1.233001,-6.322786,-4.115562,7.536334,-6.219673,-9.585752,-1.808269,-6.433478,-1.885158,2.632657,-5.990963,7.383802,-5.189615,-4.420165,-0.624287,-4.551652,-6.808643,-6.357752,-2.703351,9.115363,-0.270909,4.445910,2.977214,4.996278,3.304726,-7.734206,-3.847244,-2.310825,5.354121,-0.685734,-3.942336,0.660287,3.176455,4.070297,-5.184477,-9.607187,0.872561,8.018763,3.395706,-4.810749,8.374150,-7.071638,-8.146027,5.879854,-0.195281,-4.985470,-7.606288,8.635181,0.290625,4.004976,-5.548456,-7.773162,4.971977,-2.647449,6.019186,3.467801,4.515972,-5.681143,-0.979642,-9.225737,0.994140,-9.295214,-8.473605,3.715772,-0.537044,5.524870,-3.222386,-2.908264,0.630167,-6.851994,8.964097,-7.619416,-6.754557,2.640316,-9.395046,1.991284,-8.842055,8.307125,4.191063,-4.881946,6.365268,-9.063316,-0.118839,7.487354,2.529294,-6.773020,5.691943,-2.257607,5.268582,1.705430,0.637365,-8.098374,-3.995588,-4.094467,-6.470732,5.868139,8.270662,-9.823980,6.163628,0.343857,6.062463,5.896083,-6.420411,-0.334902,3.175195,4.752121,-6.820678,-1.117890,3.097450,9.276027,-8.958819,2.285626,-8.426334,9.310204,5.418310,8.957553,-1.042979,-1.116283,-1.378877,-1.026184,-2.763945,-1.992355,6.921891,7.991633,6.185176,4.525763,4.277812,1.840939,-0.229543,7.191329,-4.988301,-9.589564,-5.651790,5.888195,-3.077952,-4.920569,-8.486687,4.785800,-3.137111,-8.899654,8.310728,5.439454,1.445538,3.493211,4.969252,2.785338,3.308287,-6.032000,-4.866423,-4.788360,6.103422,1.454869,8.769719,-0.557506,2.646396,8.474045,-4.772281,-1.291805,-4.657762,8.102313,-6.823655,3.053462,-6.046865,2.278962,8.933806,8.817656,5.510325,-9.312846,-4.764788,-6.088772,-0.518800,-2.704355,-0.008876,-1.179254,-2.984106,-5.733225,-5.549336,-0.780039,1.253608,-4.860636,0.694287,8.894704,-1.309391,4.767647,-9.960499,3.901566,-1.164141,2.576250,-5.726393,2.596017,1.399259,9.153535,2.143233,3.747749,-3.174280,1.696065,8.781573,-7.060928,7.651607,-6.054595,0.229347,-5.008910,-9.162066,-4.059379,4.520730,7.068328,5.073686,-8.809545,6.193428,9.839409,1.423021,4.764916,9.692168,3.300241,-6.634538,8.662866,8.254066,8.011722,1.458729,-0.666081,4.797665,-0.363252,-2.034714,0.439780,-6.682423,9.643499,3.229740,-8.688940,-4.398233,6.204444,-5.927431,-9.835329,-6.914431,6.920622,2.409121,-5.512061,2.381712,6.850644,-7.717445,4.780641,2.865255,-7.301957,-9.157812,-1.392003,-9.539873,0.411239,-4.222757,-5.558284,6.476003,-8.367500,7.923267,9.291398,8.563704,5.690814,1.470518,-8.247581,8.962415,4.899678,-3.482486,4.552870,-2.197977,1.836559,-8.013170,2.932338,4.218849,0.271895,2.019803,2.247921,3.699264,-3.461405,-3.577299,-1.879114,1.445464,2.917653,1.988162,7.831449,4.078987,-5.664149,-9.643340,8.818919,4.083308,5.579218,3.703803,-9.320793,2.576587,3.560398,0.947742,7.791644,3.845268,-2.423941,1.039143,-0.453451,-3.379447,8.363022,0.713958,-8.498823,9.698465,9.550617,8.921348,8.905332,-7.053150,-9.005005,-8.136406,-8.888703,-5.864494,-0.785386,-6.737149,-7.153227,3.124855,-4.372341,-1.493562,-1.207909,-3.448862,-4.319888,8.073860,-4.567594,-5.824036,2.125914,-4.180639,-6.229908,0.197766,1.652225,-7.103047,-2.747520,0.967522,-0.775518,-0.757983,8.784580,-7.242058,-5.777597,9.001257,7.252874,3.824781,3.640227,-1.982838,-6.326413,-4.727027,-0.826722,3.385850,0.427651,0.262340,-6.401530,-2.986428,-9.187822,1.489448,-9.472594,8.164985,-5.129887,-4.419948,-9.870741,3.107477,-4.400528,-2.046767,-0.652821,-3.966686,-5.659316,3.258345,6.250677,-6.871708,-9.715843,-0.223595,4.343443,-1.812711,-4.147063,0.742461,-3.935274,8.191700,-2.083881,8.868434,0.217540,-0.108146,0.699564,-2.572066,5.035660,-3.782860,-7.942821,-8.167626,-0.482203,8.158933,-9.360025,9.615880,7.267499,6.037954,5.374782,8.011747,-4.424955,-8.291508,0.065587,-3.914231,-8.407569,7.905206,1.488514,-9.342162,-5.052236,-1.091728,-7.810178,1.865057,-8.643835,3.345209,2.540511,-4.731919,7.721606,9.067018,0.241895,4.831233,-0.539196,-1.888062,0.511819,5.580149,-3.293199,-6.609286,-8.518074,1.411367,-5.654346,-0.778307,7.357728,-2.018600,0.156616,6.487711,0.816585,-1.472474,9.407086,-0.467555,7.322953,2.105935,8.839613,-6.864238,0.622046,6.536242,4.097966,-9.517086,-9.779278,0.287727,-3.757394,3.027735,8.108242,-4.828564,-3.887880,1.985827,-9.923072,-7.483322,-2.425660,4.100422,-3.717260,-4.769757,-2.246170,-1.393941,7.001946,7.200103,-3.505048,0.682886,-4.879671,3.389975,-7.255623,6.162774,0.172418,1.921752,-9.460619,3.678224,7.012995,-7.769840,-0.850072,-5.357195,-2.035904,-1.608628,-4.341641,7.814420,3.711647,-1.758085,7.072777,-6.348762,3.850360,0.961556,1.859586,-9.446747,-9.120611,-0.292038,8.578116,-7.036919,-0.158016,-1.680787,-9.174662,-8.549997,-7.161779,-9.661391,-0.879436,-3.662344,-4.464125,0.455621,5.529844,-1.011050,0.586239,-0.282630,0.377087,-1.922508,7.612747,2.566947,-3.746483,9.193978,-8.182468,9.126742,8.131322,-5.737985,7.397009,1.757366,6.299986,-0.321477,-3.928410,8.293291,9.908119,-6.838563,-7.029386,-7.228083,4.651089,-0.123670,6.534294,-8.861569,7.154128,-0.661265,-1.225803,9.053889,1.542254,-1.378443,3.972875,-6.418784,-2.324676,4.562786,-8.687467,8.492755,-1.447333,9.905803,5.137808,-5.422583,-1.772648,8.617520,-8.493116,-0.789022,-5.095219,5.051102,-6.113515,-0.241578,-3.690793,3.742193,-7.553815,-9.831940,-2.452516,-3.650368,6.036627,6.466310,-7.419415,4.900397,0.812277,-1.240767,-1.088144,7.549453,0.430136,1.805261,-7.214069,-3.678903,-2.394170,1.533303,-9.967541,-3.119125,-0.729303,5.930675,7.072878,0.853105,-4.089865,-8.494366,9.782585,1.002908,-7.500974,1.967448,-1.863000,1.065628,-5.776190,7.472159,-5.572781,4.949288,7.415211,5.318359,2.967810,-3.203624,5.444485,-5.988387,-1.581673,9.356550,5.578260,0.190124,9.057417,-2.416481,2.606063,-8.960896,7.358439,-9.505645,7.348160,0.093580,-9.262634,-4.942993,8.885634,0.202139,0.435921,-3.350118,1.785006,-0.243423,-9.503468,-5.226927,-9.345311,7.346869,-5.601633,7.904647,-0.818907,-6.414788,-3.865911,-1.686625,-5.735973,7.815166,-1.317228,-0.204178,-4.770262,-2.972121,7.992098,-5.836678,-6.669179,8.564811,-3.829627,-1.511162,-5.268173,8.206773,5.268676,-3.702866,9.097957,6.817475,7.985808,7.695463,-2.871890,-8.663684,5.475997,-5.401606,-8.985052,-2.435305,-7.984857,8.353915,-5.024179,0.190431,-5.383254,4.665818,3.200529,-7.376100,-8.561625,-8.035180,9.572920,-7.580388,-1.411341,-2.316838,-6.033066,1.752604,8.788542,5.020337,0.529978,-3.146573,-6.472432,-0.850321,-9.404299,-6.007577,-6.302045,-3.792328,7.252235,-1.602114,0.968991,4.199714,-1.669919,-6.304609,7.140280,7.973490,-7.356157,3.572317,8.788873,-0.793557,-4.880966,-7.954447,-4.264856,-2.502906,4.448126,8.102971,-4.266394,-1.031346,4.130615,-6.980204,1.994216,2.318939,9.650065,-3.641192,-0.641596,1.531785,-4.679682,-3.364160,-6.585903,-6.916104,2.495531,-1.054901,-7.095029,-8.779840,8.458392,5.253605,-2.883745,-5.420061,9.322650,-9.402569,0.178563,-9.868275,1.947047,-3.562689,2.954499,9.045674,-9.906388,-3.398328,8.587391,-5.146390,-4.213654,4.470622,4.895329,-1.425820,-5.008572,-3.856259,-8.550057,7.304306,2.888440,1.766718,3.246540,-9.733289,-1.198333,-7.618387,6.360929,-1.290145,-6.003003,7.955271,6.288078,-0.379192,-7.283414,-0.797532,3.568283,4.890752,0.954973,-3.088135], dtype = "float64")#candidate|10815|(924,)|const|float64
call_10814 = relay.TupleGetItem(func_8784_call(relay.reshape(const_10815.astype('float64'), [462, 2])), 1)
call_10816 = relay.TupleGetItem(func_8787_call(relay.reshape(const_10815.astype('float64'), [462, 2])), 1)
func_9319_call = mod.get_global_var('func_9319')
func_9321_call = mutated_mod.get_global_var('func_9321')
var_10826 = relay.var("var_10826", dtype = "float64", shape = (1456,))#candidate|10826|(1456,)|var|float64
call_10825 = relay.TupleGetItem(func_9319_call(relay.reshape(var_10826.astype('float64'), [13, 16, 7])), 2)
call_10827 = relay.TupleGetItem(func_9321_call(relay.reshape(var_10826.astype('float64'), [13, 16, 7])), 2)
output = relay.Tuple([call_10796,call_10814,const_10815,call_10825,var_10826,])
output2 = relay.Tuple([call_10797,call_10816,const_10815,call_10827,var_10826,])
func_10834 = relay.Function([var_10826,], output)
mod['func_10834'] = func_10834
mod = relay.transform.InferType()(mod)
var_10835 = relay.var("var_10835", dtype = "float64", shape = (1456,))#candidate|10835|(1456,)|var|float64
output = func_10834(var_10835)
func_10836 = relay.Function([var_10835], output)
mutated_mod['func_10836'] = func_10836
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10838 = relay.var("var_10838", dtype = "int64", shape = (9, 7, 3))#candidate|10838|(9, 7, 3)|var|int64
var_10839 = relay.var("var_10839", dtype = "int64", shape = (9, 7, 3))#candidate|10839|(9, 7, 3)|var|int64
bop_10840 = relay.multiply(var_10838.astype('int64'), relay.reshape(var_10839.astype('int64'), relay.shape_of(var_10838))) # shape=(9, 7, 3)
func_10306_call = mod.get_global_var('func_10306')
func_10307_call = mutated_mod.get_global_var('func_10307')
call_10843 = relay.TupleGetItem(func_10306_call(), 0)
call_10844 = relay.TupleGetItem(func_10307_call(), 0)
output = relay.Tuple([bop_10840,call_10843,])
output2 = relay.Tuple([bop_10840,call_10844,])
func_10848 = relay.Function([var_10838,var_10839,], output)
mod['func_10848'] = func_10848
mod = relay.transform.InferType()(mod)
var_10849 = relay.var("var_10849", dtype = "int64", shape = (9, 7, 3))#candidate|10849|(9, 7, 3)|var|int64
var_10850 = relay.var("var_10850", dtype = "int64", shape = (9, 7, 3))#candidate|10850|(9, 7, 3)|var|int64
output = func_10848(var_10849,var_10850,)
func_10851 = relay.Function([var_10849,var_10850,], output)
mutated_mod['func_10851'] = func_10851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10633_call = mod.get_global_var('func_10633')
func_10635_call = mutated_mod.get_global_var('func_10635')
call_10859 = relay.TupleGetItem(func_10633_call(), 0)
call_10860 = relay.TupleGetItem(func_10635_call(), 0)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_10866 = func_3536_call()
call_10867 = func_3536_call()
var_10884 = relay.var("var_10884", dtype = "float64", shape = (8, 15, 4))#candidate|10884|(8, 15, 4)|var|float64
bop_10885 = relay.bitwise_xor(call_10866.astype('int8'), relay.reshape(var_10884.astype('int8'), relay.shape_of(call_10866))) # shape=(8, 15, 4)
bop_10888 = relay.bitwise_xor(call_10867.astype('int8'), relay.reshape(var_10884.astype('int8'), relay.shape_of(call_10867))) # shape=(8, 15, 4)
func_1280_call = mod.get_global_var('func_1280')
func_1283_call = mutated_mod.get_global_var('func_1283')
var_10890 = relay.var("var_10890", dtype = "float64", shape = (360,))#candidate|10890|(360,)|var|float64
const_10891 = relay.const([[5.306126],[6.031818],[9.764183],[3.998094],[-0.827870],[2.698108],[3.825372],[-0.793704],[-2.461671],[8.096992],[-2.876407],[-2.089112],[3.713733],[0.019623],[9.200689],[-6.907624],[6.136685],[7.580091],[-6.856178],[-5.148865],[7.621820],[-1.674699],[-8.136161],[4.839351],[3.510927],[-7.020742],[-6.485623],[8.699040],[2.244166],[-9.383006],[4.259376],[0.471066],[-9.006900],[3.488925],[1.042723],[9.713976],[-7.455641],[0.883458],[-7.061095],[9.392029],[6.336401],[3.550462],[-7.522972],[-4.833736],[1.944651],[5.078550],[5.489668],[-1.944273],[0.099007],[8.500103],[1.166774],[9.475196],[-8.686741],[1.464773],[-9.886887],[7.079488],[-8.637517],[7.019605],[2.800326],[-3.300464],[-0.637875],[2.618079],[-2.008409],[6.304569],[-4.799387],[-4.726984],[8.219888],[7.711212],[-4.487643],[-5.904233],[5.549430],[6.923444],[-0.316465],[-6.093130],[-2.280385],[4.201895],[-4.168723],[-2.172779],[-4.291787],[6.316387],[-1.205041],[-5.311717],[6.306408],[-4.951974],[-7.982763],[-4.020116],[-6.786876],[-5.537574],[7.677635],[-5.773012],[2.045676],[-5.124196],[9.368604],[3.669235],[7.395016],[-5.362215],[-8.045167],[9.086796],[-0.807880],[-6.752655],[8.159516],[-6.792538],[-9.161861],[-9.177864],[2.469923],[5.950471],[-1.694207],[5.916149],[-5.581555],[3.928065],[6.932529],[-3.382985],[9.123581],[4.477449],[8.092059],[-6.112273],[9.142980],[-1.634394],[7.950277],[8.532059],[2.670457],[-0.739613],[-0.053346],[9.951439],[-3.875907],[-3.582689],[-3.582664],[2.178500],[4.470730],[0.101461],[-8.518457],[1.335974],[-2.768481],[9.718277],[-1.438962],[1.535394],[2.272865],[-6.359279],[2.250897],[2.583702],[-8.635838],[8.573341],[-2.724957],[-7.152776],[1.188784],[-9.570935],[-0.224201],[6.340256],[6.045581],[-6.754267],[2.722806],[2.987429],[4.731155],[2.638178],[-8.273739],[-6.840016],[-9.849327],[0.187341],[9.369585],[-6.839842],[-1.557028],[-7.886838],[-2.259658],[0.946714],[6.611900],[-5.104644],[7.514706],[9.992027],[7.277549],[9.893742],[3.049252],[-1.421653],[3.250416],[-6.839995],[-7.572950],[-3.988639],[9.980852],[8.431598],[-5.710947],[7.730282],[-2.510085],[2.440222],[-4.086282],[7.016091],[8.579487],[2.864219],[-8.940524],[-1.257283],[4.446926],[-5.751923],[-3.521522],[-1.796867],[-3.691776],[9.030221],[7.251816],[-8.230786],[-2.696306],[0.904052],[-9.399398],[-9.140840],[-9.454296],[4.609541],[-8.645931],[-9.807585],[-2.370914],[4.031941],[6.103315],[2.940499],[9.449261],[6.508270],[0.829515],[-2.016458],[6.686126],[-0.077187],[-5.963508],[5.586373],[-2.411976],[-7.677354],[-5.558516],[8.940874],[2.860300],[9.354281],[-4.108972],[-2.846006],[-4.209719],[-2.559076],[7.694335],[3.812575],[1.104614],[4.684056],[5.648392],[-9.399614],[6.936944],[-1.162740],[1.353815],[-7.674988],[-9.413938],[-6.363821],[-4.002846],[-2.818009],[-6.648886],[5.670291],[6.576141],[-3.773789],[-8.564080],[1.311203],[-5.282962],[-5.511450],[-6.573665],[2.943084],[-9.505709],[-7.403622],[-9.011935],[3.934388],[-5.553539],[4.144352],[7.690441],[-7.850630],[6.994540],[7.718037],[-0.970796],[2.514973],[-2.743847],[-1.021731],[-7.983223],[-7.599717],[-2.838656],[8.897279],[2.043470],[8.716804],[-3.891711],[-9.356873],[4.881175],[1.290170],[7.969655],[1.608010],[6.202712],[-3.739291],[-5.817829],[-5.117150],[9.867985],[8.655355],[1.872237],[-8.818140],[2.766956],[-0.702136],[-7.829944],[1.658139],[-7.330652],[-7.126227],[3.890841],[8.079842],[9.288006],[-5.736528],[9.258320],[-6.218511],[-8.918985],[-4.694197],[0.443509],[-7.142456],[-6.735657],[-1.747908],[-4.520944],[0.663083],[-0.225480],[-8.614183],[7.224274],[-2.178854],[-6.797442],[-1.314450],[2.857419],[-8.958977],[-8.638031],[-8.693662],[7.864314],[-7.741587],[5.163534],[-7.663652],[3.474059],[-2.767329],[5.300510],[0.014849],[4.098330],[9.154588],[8.320034],[6.460715],[8.423949],[-5.343939],[-6.309111],[4.171046],[2.804037],[6.876137],[-4.615962],[-1.840724],[2.197472],[-6.124732],[-1.697322],[3.945045],[8.016444],[4.307729],[-6.427396],[-4.745767],[-7.645614],[7.606847],[1.794397],[-5.305414],[8.786925],[0.280366],[1.382588],[2.029560],[9.754550],[6.025255],[5.546127],[7.024948],[-4.145829],[6.972195],[7.315585],[-4.866876],[-4.451509],[-4.196703],[-3.132333],[0.217673],[-4.235183],[6.859911],[-9.998006],[5.974958],[-1.274380],[5.685578],[7.361603],[1.146346],[9.863732],[4.464734],[-1.220025],[-8.907959],[6.450308],[-6.805268],[0.817015],[3.995029],[-0.194720],[4.755581],[7.714180],[-1.950135],[-0.142568],[-1.223925],[-4.475391],[7.639891],[-9.084318],[-6.729112],[-8.061165],[-9.110700],[7.327042],[2.155355],[-1.721705],[7.832822],[3.763049],[6.333739],[7.831810],[9.260462],[-8.950081],[1.850339],[1.371512],[-0.352750],[0.969365],[-8.388446],[-1.403030],[-1.524379],[0.485680],[-3.022654],[-0.762082],[-5.881733],[7.170903],[5.069176],[-3.072821],[-5.303336],[-5.086470],[5.651734],[-1.541365],[9.047531],[4.206287],[1.791284],[-5.558249],[2.004669],[9.850830],[7.511683],[6.120179],[0.374877],[-2.332997],[5.625205],[6.205583],[4.441669],[-9.145955],[5.681060],[-0.677338],[-8.783960],[-4.808281],[0.188480],[7.723819],[-6.272205],[2.125859],[6.062915],[-4.782000],[1.931815],[5.422884],[9.156225],[-2.570747],[-7.057915],[9.804602],[9.289050],[-7.251578],[5.903142],[0.143568],[-8.699670],[-2.057268],[0.449584],[-1.430007],[-2.942590],[9.788103],[0.502109],[2.880870],[-6.821518],[9.272647],[-2.421946],[-9.896500],[2.511931],[0.720942],[-0.128196],[5.283881],[-7.548728],[5.610427],[6.721276],[-5.252581],[-5.307142],[1.375992],[-1.022129],[-4.533862],[-3.773709],[2.940835],[3.861468],[-6.954986],[-2.065357],[4.088549],[-7.496306],[9.744584],[-9.835551],[-3.159094],[9.553533],[-6.318715],[6.698508],[8.439000],[-4.687570],[-1.230071],[-9.271478],[5.624423],[5.960992],[-2.221699],[8.312189],[-2.821084],[-8.313142],[-7.586041],[4.803592],[0.474922],[0.606446],[-7.154453],[5.191200],[-0.239153],[-8.449001],[6.536480],[-1.349356],[-9.842004],[-8.207242],[-6.654523],[-8.341519],[-7.818610],[-7.201430],[-7.370346],[8.293188],[-5.199869],[6.524569],[4.649259],[5.219811],[-5.993474],[-0.393614],[-2.880059],[-3.062303],[3.353806],[8.488582],[-0.974522],[-3.813265],[-4.335153],[-6.862407],[-7.351142],[-4.235164],[-9.881807],[-8.415598],[0.111517],[-9.959647],[6.920208],[3.258532],[2.610420],[-9.329859],[-4.927676],[-4.180239],[4.836632],[6.575669],[-5.603800],[-4.906151],[-1.939177],[9.290342],[-6.395713],[-9.270907],[4.766891],[8.243160],[-2.434759],[-8.174113],[-1.091940],[-8.199409],[-3.232368],[-6.801824],[5.474283],[-0.556729],[4.984824],[8.489874],[8.698014],[-4.795687],[-4.387367],[9.176300],[9.562146],[-2.107294],[5.894498],[-0.268941],[4.945139],[2.248274],[1.634205],[6.704687],[0.680462],[-8.750263],[5.864093],[-9.469932],[1.723342],[-6.469535],[-6.106851],[2.794619],[7.821813],[4.518164],[9.132047],[-7.437494],[-5.730981],[-7.851762],[4.064639],[-4.732634],[4.045300],[5.644659],[-9.687359],[-9.933312],[5.381771],[7.805359],[-1.018087],[0.911810],[-4.075413],[0.539127],[-3.964107],[-7.407507],[8.241931],[0.134463],[2.290405],[0.520533],[-6.970614],[6.224641],[8.130780],[-2.504858],[-9.951677],[-8.026033],[4.830558],[-9.694540],[-8.408964],[5.573846],[-5.095555],[8.566902],[-3.035758],[-0.016990],[-1.503493],[0.029033],[2.023790],[-1.682060],[-7.770093],[9.000555],[-4.974599],[2.945585],[3.406296],[-3.849598],[4.226373],[1.200699],[9.595000],[6.785872],[7.172245],[7.531423],[-6.634438],[-9.838038],[6.786819],[-2.681635],[-6.147181],[0.337584],[4.089579],[-6.737150],[-9.873642],[-7.086074],[-8.858428],[7.821033],[-5.081317],[3.455118],[6.807754],[3.746898],[6.482199],[5.066527],[-6.475772],[-3.060439],[0.281138],[-9.512044],[0.978293],[7.529730],[4.794452],[3.055000],[6.900414],[6.920197],[-7.712911],[5.601012],[-7.033168],[5.972718],[4.856669],[-1.218236],[-3.072764],[-1.972575],[-0.518659],[-2.744838],[8.108242],[-3.582609],[7.272028],[-2.992438],[-7.739011],[-2.104725],[-1.114481],[-6.602418],[-0.757734],[5.140529],[-7.620049],[-5.576218],[-4.979352],[-8.166780],[6.838266],[-3.791589],[5.425745],[8.643168],[0.199777],[6.527897],[7.373666],[-0.898074],[-0.373583],[-8.849277],[-9.058682],[-2.185623],[-1.985218],[8.329393],[5.670321],[4.238086],[-5.078258],[8.881932],[-2.822923],[-8.007860],[-2.483376],[-8.997727],[5.920244],[7.107574],[5.638988],[-7.781363],[2.226718],[7.344351],[3.603491],[8.090776],[-0.291072],[4.272418],[-6.338110],[-7.646769],[2.592614],[-6.415035],[7.007491],[-6.180704],[6.499038],[-2.110407],[2.588233],[-5.582093],[6.221708],[-8.456939],[-7.849585],[0.350526],[9.773497],[2.956332],[6.260331],[-1.717885],[-7.302822],[-6.337392],[3.747212],[-6.993349],[-6.120471],[-5.318551],[-8.121716],[8.634581],[-7.643143],[-3.849583],[8.732237],[2.866292],[4.554001],[-5.597528],[9.409051],[7.367248],[-8.797206],[0.315609],[-3.975825],[-1.128942],[-4.130199],[9.286288],[-5.609874],[-7.300909],[-3.025371],[3.176741],[-6.970034],[-1.501195],[-4.154786],[-8.996103],[-2.597773],[4.706876],[1.817222],[-1.409693],[9.656901],[-3.055100],[8.070573],[-5.015955],[-9.199446],[-5.399237],[1.287731],[-1.315724],[9.039234],[8.142872],[-0.604865],[8.719971],[-3.154301],[1.882046],[6.199266],[7.567976],[-7.944671],[-7.556828],[3.173185],[5.324762],[8.377291],[6.218861],[-9.405982],[-2.224152],[-9.102303],[9.746014],[2.548223],[1.754582],[2.965084],[0.314336],[6.541990],[2.404218],[-6.416806],[0.355255],[-2.499060],[-0.495238],[6.214497],[0.613106],[0.670778],[3.956573],[4.351602],[-3.022981],[5.385974],[-4.947390],[-5.461937],[6.123893],[8.196170],[-3.414940],[-1.367617],[4.205579],[-6.904258],[-3.565615],[9.374151],[8.269626],[7.166348],[2.387964],[7.579679],[7.012061],[1.458054],[-9.663379],[7.167862],[1.206679],[-6.088481],[-2.735658],[-0.650127],[-2.061091],[4.306114],[-0.600489],[-4.425104],[-5.202670],[-1.711432],[-4.937272],[0.876720],[-9.486174],[-3.501780],[6.811201],[-2.692792],[-8.045945],[-4.947392],[2.277174],[-6.738664],[3.115909],[-4.516098],[6.943496],[-9.381750],[-8.327436],[6.939476],[-1.277980],[-6.285165],[5.356420],[9.580730],[-8.332537],[-6.653345],[4.664881],[1.138243],[7.812741],[-5.990019],[-1.230423],[-2.312590],[9.154593],[8.342515],[4.657520],[-1.099296],[0.931803],[-8.870636],[0.426126],[0.087048],[0.659484],[-9.063668],[-6.709587],[3.725825],[-7.987903],[7.728792],[-5.173634],[-3.096976],[-9.282228],[3.114448],[-2.686298],[6.220274],[-9.794682],[-4.314701],[-2.336338],[1.742304],[9.062836],[-6.588944],[4.692992],[7.310283],[8.128368],[-0.708878],[-7.347840],[2.401900],[-7.597622],[-8.801445],[-0.307703],[6.124617],[1.637639],[9.788115],[9.276402],[1.178125],[-9.183124],[8.860190],[8.826300],[1.095475],[2.558271],[-5.820735],[-3.023162],[-9.938308],[-7.341669],[2.079721],[-9.247889],[2.545971],[2.460164]], dtype = "float64")#candidate|10891|(924, 1)|const|float64
call_10889 = relay.TupleGetItem(func_1280_call(relay.reshape(var_10890.astype('float64'), [9, 10, 4]), relay.reshape(const_10891.astype('float64'), [154, 6]), ), 0)
call_10892 = relay.TupleGetItem(func_1283_call(relay.reshape(var_10890.astype('float64'), [9, 10, 4]), relay.reshape(const_10891.astype('float64'), [154, 6]), ), 0)
output = relay.Tuple([call_10859,bop_10885,call_10889,var_10890,const_10891,])
output2 = relay.Tuple([call_10860,bop_10888,call_10892,var_10890,const_10891,])
func_10895 = relay.Function([var_10884,var_10890,], output)
mod['func_10895'] = func_10895
mod = relay.transform.InferType()(mod)
mutated_mod['func_10895'] = func_10895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10895_call = mutated_mod.get_global_var('func_10895')
var_10897 = relay.var("var_10897", dtype = "float64", shape = (8, 15, 4))#candidate|10897|(8, 15, 4)|var|float64
var_10898 = relay.var("var_10898", dtype = "float64", shape = (360,))#candidate|10898|(360,)|var|float64
call_10896 = func_10895_call(var_10897,var_10898,)
output = call_10896
func_10899 = relay.Function([var_10897,var_10898,], output)
mutated_mod['func_10899'] = func_10899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5151_call = mod.get_global_var('func_5151')
func_5152_call = mutated_mod.get_global_var('func_5152')
call_10921 = relay.TupleGetItem(func_5151_call(), 0)
call_10922 = relay.TupleGetItem(func_5152_call(), 0)
func_7125_call = mod.get_global_var('func_7125')
func_7128_call = mutated_mod.get_global_var('func_7128')
var_10942 = relay.var("var_10942", dtype = "float64", shape = (924,))#candidate|10942|(924,)|var|float64
call_10941 = relay.TupleGetItem(func_7125_call(relay.reshape(var_10942.astype('float64'), [1, 924])), 2)
call_10943 = relay.TupleGetItem(func_7128_call(relay.reshape(var_10942.astype('float64'), [1, 924])), 2)
output = relay.Tuple([call_10921,call_10941,var_10942,])
output2 = relay.Tuple([call_10922,call_10943,var_10942,])
func_10953 = relay.Function([var_10942,], output)
mod['func_10953'] = func_10953
mod = relay.transform.InferType()(mod)
var_10954 = relay.var("var_10954", dtype = "float64", shape = (924,))#candidate|10954|(924,)|var|float64
output = func_10953(var_10954)
func_10955 = relay.Function([var_10954], output)
mutated_mod['func_10955'] = func_10955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7596_call = mod.get_global_var('func_7596')
func_7597_call = mutated_mod.get_global_var('func_7597')
call_10957 = relay.TupleGetItem(func_7596_call(), 0)
call_10958 = relay.TupleGetItem(func_7597_call(), 0)
const_10959 = relay.const([[[3.846534,7.983832,1.148674,-3.691591,-8.615674,6.338279],[1.538060,-6.940145,-3.823342,-2.503640,-0.858264,-5.051597],[9.126355,-8.066277,2.465224,0.972732,-2.383863,-4.352968],[-8.351412,9.704155,3.918066,1.660340,7.580073,3.121066],[3.798274,-6.536605,5.551501,-6.567737,-7.704720,2.098041],[-3.319160,7.200018,-0.187442,-5.211305,-0.965055,4.407857],[7.527625,-5.143052,-0.708929,-8.727077,-5.642419,-9.484412],[5.450532,-5.905429,2.322027,2.084493,9.102933,-7.841528],[-5.939946,-5.253502,-6.886437,2.351043,-7.196642,5.922929],[7.176195,-0.415515,-5.088097,0.509600,4.683711,4.601396],[-2.223118,4.918234,6.516020,5.873105,-0.302951,4.602901],[1.079157,-6.599882,-8.975422,-5.645763,1.277565,7.393706],[9.986665,4.867096,9.864597,-2.257098,7.498780,2.423726],[7.588751,7.470273,-5.450122,9.303673,2.495527,7.401968],[7.988447,8.224686,-0.270313,-4.798124,9.951647,-0.440306],[-1.707025,-4.702403,-2.013455,2.319497,-7.528913,-7.221237]],[[3.286034,-3.751107,3.017503,-0.503719,-6.806842,-7.506565],[4.058445,-2.814131,-1.593406,5.362636,9.470201,1.584334],[1.816268,-0.624732,9.019904,-9.952389,-5.109964,3.551192],[-6.794696,-8.181868,1.736768,6.136918,3.280866,7.885925],[-0.835779,-4.478455,0.238510,-1.585586,-5.672278,-0.627723],[6.267034,-4.399558,-1.695127,6.622229,-8.064949,9.026871],[-1.271786,-9.028968,-7.672811,-8.110111,-1.812232,5.657250],[-1.557494,-9.660898,-4.010393,-2.423506,7.958599,8.597534],[-4.299511,-2.702426,-9.420735,-4.438549,-7.691023,-4.923988],[-3.051627,8.473389,5.103501,-7.531598,-3.349973,3.138711],[-2.168125,-7.693365,-7.748203,4.698580,6.204473,4.830352],[8.636288,-4.906845,-4.964871,-6.040396,6.947660,9.771577],[-4.746307,-9.601532,-3.304347,9.596780,1.693399,-4.034500],[6.976131,-9.706473,0.756526,-5.950916,4.575141,-2.401553],[1.619293,0.147480,4.759358,-9.588854,-7.292106,-1.433304],[-5.424242,7.935918,-4.958694,3.199341,2.893614,-1.690809]],[[-2.095758,0.894621,8.422632,6.495832,1.178601,-4.973790],[-3.307121,-1.804476,4.892111,6.130615,4.356079,-0.477847],[3.783193,6.260913,0.205601,8.706241,5.367285,-2.265525],[4.869577,4.257494,-8.119883,4.287994,-1.679121,1.604382],[-0.054495,6.211907,-7.210380,8.808979,-4.816154,-1.984649],[-6.045752,3.347707,7.857143,9.901727,7.178747,1.893920],[-4.122127,-5.175781,-0.070437,-2.595784,0.351518,-6.637000],[0.551335,6.296184,5.278630,-9.854754,3.496789,7.093190],[6.434598,3.161244,7.552153,-6.700880,6.699187,8.373081],[-6.489625,3.166466,6.419214,2.166923,3.880477,-5.062965],[5.887006,2.904591,-5.335043,8.129372,1.482575,6.842389],[1.958317,-2.476823,-1.757612,-3.714952,9.224092,-9.799032],[-5.067391,-7.954303,-3.470235,-5.195745,9.055930,2.996587],[-6.889794,2.070703,1.599568,-5.403694,-1.595955,-2.035397],[-0.325456,9.041727,-1.688291,7.979555,-7.494364,-5.492635],[-8.137412,-0.005324,-7.379056,-6.897484,-6.570144,-7.494658]],[[-9.287267,-2.573256,2.270898,8.806294,8.991214,-3.795323],[6.329427,-3.194924,6.530994,-5.430357,8.589864,9.055686],[-0.871602,-6.734930,5.856069,5.223859,-5.051772,-0.936317],[-9.589947,3.813160,-4.811500,3.262669,6.438952,2.859291],[-6.671128,8.585333,-0.333628,-9.895218,-0.796434,6.114721],[0.318761,4.867089,-9.556604,-7.710703,8.238463,2.448981],[2.515886,8.548101,-2.962685,3.706852,6.735081,8.626830],[1.913119,-0.772457,-8.308563,5.849845,-1.383335,6.560452],[-9.839923,0.840631,-4.083762,8.917032,1.110248,-1.951167],[-0.024502,5.538684,-1.553237,5.586407,-7.918381,8.304095],[-3.735046,-1.650929,8.394202,1.669988,4.108461,-8.857599],[7.574426,8.094000,-8.484557,2.458171,7.082916,-4.101326],[3.090164,0.138779,-3.984418,-8.284285,9.856786,2.852009],[6.974374,-2.939578,-8.772031,-8.923408,9.242234,-4.257437],[5.448056,-2.585836,-2.380288,3.876836,-1.382844,7.035516],[1.040554,8.676342,8.338750,-0.271002,-4.547394,4.923815]],[[1.153577,-3.058900,-7.928276,-9.865410,-4.445057,-1.257246],[-1.071558,-7.677302,9.006618,3.105520,-6.795169,3.815851],[3.971062,-0.111352,4.610079,-1.594347,7.612909,1.241547],[-1.306942,0.050463,-0.958931,0.305851,9.659509,5.659729],[-4.043790,-9.270281,-1.164602,-2.412872,8.502688,3.750289],[-7.422718,1.692655,-2.387370,5.357871,-5.470037,-9.542803],[0.165831,7.548786,8.962818,4.554135,5.423519,-3.852779],[9.426868,-8.684913,9.745040,1.522460,2.670565,4.878202],[2.966336,-0.178419,-5.631902,-5.354339,5.917917,-3.494431],[2.587787,-5.393364,0.200001,-8.074460,0.673158,9.859693],[-9.199179,-2.769800,2.394306,3.593601,6.157482,8.563795],[-2.713840,5.457000,4.710302,2.842778,6.721866,-3.534131],[-2.891720,9.031528,9.745755,2.799253,-0.952131,1.829021],[5.263741,-6.981247,3.296418,-7.454774,-2.813225,0.763998],[-9.226732,-7.737035,-1.473965,-0.357332,2.338538,-8.301808],[9.097284,-5.965682,1.951719,3.469695,-5.906490,5.277768]],[[4.221537,-9.139847,3.626578,-8.230106,-6.102468,3.988658],[4.859343,0.643637,-9.931511,1.368728,7.323134,2.959228],[5.369414,-3.814858,-7.595883,8.355315,1.080978,6.769068],[8.129808,-8.299699,-7.081590,-2.830890,-2.172968,-5.054636],[5.811424,-5.030442,6.197146,-8.027107,-5.369953,1.996912],[-6.525590,0.116156,-6.073703,6.651673,-8.511442,3.562989],[8.504649,-6.878069,6.192574,-3.357609,-4.035614,-5.637108],[-0.693366,-1.317285,2.614019,-1.284200,5.667939,7.243490],[-1.401449,9.756460,5.282736,-0.061773,0.724259,-1.397993],[3.568957,1.666634,5.857443,-6.988990,-4.581043,-7.018545],[-0.012045,-0.041399,-7.859977,7.742871,-6.682824,5.387769],[1.316904,-6.090340,-5.964491,5.500097,-4.178483,4.853812],[-2.124090,3.832517,3.260184,-7.545164,-3.414013,7.637829],[1.180770,-3.602007,1.768304,5.517702,4.183469,8.812074],[-3.371407,7.932750,-1.030497,-2.119272,-7.273224,9.601538],[4.900150,4.723826,-2.152501,8.746372,5.766611,3.909904]],[[8.107067,5.392170,9.148164,1.660436,-7.464328,-7.642558],[8.612526,3.011433,-4.734537,6.556485,4.823036,-7.416416],[5.226177,8.303111,9.020377,-6.875748,1.859561,1.283991],[-7.268149,-5.509257,9.565543,5.086411,6.764986,3.193351],[-9.422432,1.283993,9.253746,5.726534,8.046089,-6.937832],[-4.190377,-1.157739,-6.714450,-4.182770,-2.525906,0.065426],[3.734356,-0.425635,-6.221156,-3.151766,0.841018,-2.503096],[6.830631,6.371048,-6.407983,9.357026,-1.047027,-0.568709],[7.251587,-6.108087,6.607803,-9.177197,-7.432913,5.408107],[-6.057172,0.029809,7.597971,-2.000366,-6.067020,-9.136609],[6.922959,2.671836,4.933749,5.882174,-2.489589,-0.426923],[1.697331,-2.071665,9.925418,-6.404068,4.769327,6.276564],[0.867722,-2.518336,-0.547750,-1.210108,-1.006880,1.280497],[3.968302,0.733374,-0.436403,3.005575,-4.965826,-6.519131],[0.356734,3.998774,-2.315524,-8.164078,-6.601175,1.570267],[2.411013,4.180650,6.839094,1.176249,6.200006,-8.260440]],[[-1.681988,7.361771,7.379068,-4.245928,7.827844,-5.964211],[7.039498,5.573490,9.526292,-7.584023,7.841566,-1.960753],[-8.750149,1.807374,-9.837978,-5.837190,-5.033459,8.313239],[3.912718,-2.874054,8.315915,-6.094459,2.888812,0.303023],[4.783995,0.048568,7.997117,1.646129,1.557272,9.320397],[8.374019,-3.106249,7.265515,0.646972,-8.180715,3.619947],[-6.476945,-7.587449,-4.815429,-8.777680,0.094897,-1.713359],[-9.210777,-0.281965,-8.811556,7.218414,6.947110,3.645968],[-2.303858,1.656016,7.951064,-5.966103,2.566305,8.037596],[-2.544291,0.644131,-1.062890,-1.439717,1.239991,-1.881076],[-2.371798,8.442810,-3.559176,3.150546,-5.509306,5.096038],[3.038745,5.133100,-6.651037,-8.236923,0.870674,-3.194119],[6.300673,-5.714252,9.283600,0.432318,-5.216353,-9.459715],[5.102743,6.394548,-2.140494,7.332230,4.375182,-6.630369],[-5.330746,-8.184288,-7.614220,1.972499,-5.623432,1.298746],[-2.712354,5.116536,6.861623,2.772136,4.102481,-2.401730]],[[4.751013,-6.100027,9.334429,-2.536147,2.950040,2.620358],[1.908446,-1.459595,-7.337486,-6.979378,-4.986966,1.872295],[9.028577,-1.824979,-5.938964,-4.914146,8.838157,-9.738500],[-4.563279,-4.550331,2.165021,9.135358,-1.554910,-8.549279],[6.878387,0.242430,2.045822,-4.656752,-5.512071,6.632291],[8.198198,-2.485429,-4.927074,8.864526,-6.947760,8.975277],[6.201428,-8.112044,-2.977847,-8.121934,9.597186,8.037675],[4.974749,2.462922,-2.577486,-8.587867,9.752482,-6.310002],[9.330397,-1.557126,5.945547,5.168933,-9.648751,-8.962696],[1.417278,0.312775,2.854722,6.290946,-6.041018,-6.556747],[0.655681,-6.193591,6.754070,8.576717,0.946762,-1.736467],[9.771903,8.700310,-6.068776,-4.271345,3.308697,-9.360023],[-9.043531,6.675493,8.194973,9.749299,-7.965512,6.945240],[4.272369,-9.732936,-6.623984,8.263437,-2.822256,6.025882],[9.532846,-4.594237,9.060606,4.629073,-3.365297,-8.382505],[-2.531981,2.665461,-9.068803,-2.202542,8.286446,-2.031571]],[[-3.788579,2.938992,-6.121896,2.335991,-2.510458,-5.013369],[-5.375334,1.878273,-9.809943,-3.183158,1.144126,9.498359],[-8.530819,9.599867,-4.490043,4.515330,-7.103992,-7.595275],[-3.790183,-4.037579,2.818734,-5.239302,-6.191199,8.665910],[-6.013587,7.028473,4.930691,3.449214,-0.150693,8.629526],[-6.319375,3.375327,8.380927,0.737156,1.043772,-3.825500],[4.231097,3.578623,-9.099378,-2.836664,-2.246577,-7.413876],[1.982122,-7.724976,5.608664,-4.261761,-5.174856,-6.175552],[8.971066,1.926941,7.128953,-9.698569,8.388414,-7.527080],[-9.917676,-5.596249,-9.699663,-2.905392,-3.920030,3.442270],[-2.289198,7.222435,-3.116286,-1.616623,6.482037,-6.003602],[9.048879,9.279380,-4.317848,-0.783252,7.484185,-3.775716],[5.181074,7.831239,2.327814,7.670649,-9.063257,-4.826790],[-5.092126,5.245557,2.617301,-5.126630,-8.730774,6.653635],[6.202365,5.107244,-2.408332,-6.971939,-1.172913,1.535111],[2.591908,6.585175,0.641261,-9.453328,-6.297118,9.142212]],[[6.354107,-2.178699,-3.396676,6.952420,2.022790,-8.313290],[-5.056554,7.667101,-9.131632,-2.231608,-2.771295,0.927546],[8.008411,9.650319,4.865704,8.715558,4.420547,-6.180625],[9.974259,4.379158,-1.288859,-0.996085,1.729105,2.230824],[-0.005145,0.914049,4.019893,-9.775959,-4.784215,-2.616194],[9.965951,-6.624333,1.918782,-8.404413,-2.648623,1.936918],[2.797365,2.300206,-6.112392,-2.413386,-9.313313,3.672736],[-5.538647,4.263735,5.490316,7.504172,3.376426,5.486124],[-2.063758,-7.871167,-9.668752,-9.942355,0.461127,-2.020115],[-5.751832,1.447972,-1.348814,3.112878,-4.901124,7.727605],[-8.710498,-8.759589,-4.344114,0.594941,9.243884,-8.448689],[0.157823,3.773904,-0.981050,-9.404253,-8.772820,-3.216819],[-4.842762,-7.171914,-6.143996,1.281611,-8.227388,-6.838011],[3.570146,3.734098,2.507304,-0.791786,-4.555742,-1.569865],[3.196990,-5.579834,-1.319038,-1.092817,-7.477069,0.848911],[-8.060987,1.895684,9.693379,-8.760071,2.422484,2.749927]],[[7.856389,-5.787921,-0.977889,-3.211545,5.433394,8.771938],[8.206427,3.102266,-8.499399,-3.760529,8.043281,4.169350],[-0.092342,7.272598,-4.523418,-2.607305,4.546772,2.821292],[3.397065,9.194515,-0.606257,-8.981669,2.252143,9.803954],[2.978739,-9.561491,-4.111087,2.942209,7.316610,-0.081512],[9.232443,4.013952,6.840341,-9.171653,4.406914,-5.399374],[3.304305,8.036977,-4.655135,-7.884903,7.317123,-9.204593],[0.595336,-9.624716,-7.843674,-3.693872,4.978334,-4.194097],[-3.383719,-6.373112,2.687513,-1.269881,2.661230,9.763517],[-6.506999,1.668260,-4.993415,8.304152,8.991538,5.735542],[3.789550,-8.010276,4.977811,7.873641,8.603781,0.122492],[-6.674132,5.423711,-7.172576,6.199981,1.603680,-6.833765],[-2.082849,2.547464,3.608965,-8.310499,-2.725387,0.351188],[9.814659,7.108382,-8.383803,4.800648,-2.432991,4.696499],[0.702143,-6.076326,6.010279,4.000432,-0.581497,-6.520012],[2.530823,-0.370066,9.935067,2.208450,9.957309,1.595049]]], dtype = "float64")#candidate|10959|(12, 16, 6)|const|float64
bop_10960 = relay.mod(call_10957.astype('float64'), relay.reshape(const_10959.astype('float64'), relay.shape_of(call_10957))) # shape=(12, 16, 6)
bop_10963 = relay.mod(call_10958.astype('float64'), relay.reshape(const_10959.astype('float64'), relay.shape_of(call_10958))) # shape=(12, 16, 6)
func_9374_call = mod.get_global_var('func_9374')
func_9376_call = mutated_mod.get_global_var('func_9376')
call_10966 = relay.TupleGetItem(func_9374_call(), 0)
call_10967 = relay.TupleGetItem(func_9376_call(), 0)
func_7858_call = mod.get_global_var('func_7858')
func_7859_call = mutated_mod.get_global_var('func_7859')
call_10971 = relay.TupleGetItem(func_7858_call(), 1)
call_10972 = relay.TupleGetItem(func_7859_call(), 1)
func_5012_call = mod.get_global_var('func_5012')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_10986 = relay.TupleGetItem(func_5012_call(), 3)
call_10987 = relay.TupleGetItem(func_5013_call(), 3)
uop_10988 = relay.atan(call_10957.astype('float64')) # shape=(12, 16, 6)
uop_10990 = relay.atan(call_10958.astype('float64')) # shape=(12, 16, 6)
output = relay.Tuple([bop_10960,call_10966,call_10971,call_10986,uop_10988,])
output2 = relay.Tuple([bop_10963,call_10967,call_10972,call_10987,uop_10990,])
func_10992 = relay.Function([], output)
mod['func_10992'] = func_10992
mod = relay.transform.InferType()(mod)
output = func_10992()
func_10993 = relay.Function([], output)
mutated_mod['func_10993'] = func_10993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_11105 = func_3536_call()
call_11106 = func_3536_call()
output = relay.Tuple([call_11105,])
output2 = relay.Tuple([call_11106,])
func_11114 = relay.Function([], output)
mod['func_11114'] = func_11114
mod = relay.transform.InferType()(mod)
mutated_mod['func_11114'] = func_11114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11114_call = mutated_mod.get_global_var('func_11114')
call_11115 = func_11114_call()
output = call_11115
func_11116 = relay.Function([], output)
mutated_mod['func_11116'] = func_11116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6786_call = mod.get_global_var('func_6786')
func_6788_call = mutated_mod.get_global_var('func_6788')
call_11235 = relay.TupleGetItem(func_6786_call(), 0)
call_11236 = relay.TupleGetItem(func_6788_call(), 0)
output = call_11235
output2 = call_11236
func_11243 = relay.Function([], output)
mod['func_11243'] = func_11243
mod = relay.transform.InferType()(mod)
output = func_11243()
func_11244 = relay.Function([], output)
mutated_mod['func_11244'] = func_11244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_11252 = relay.TupleGetItem(func_5418_call(), 1)
call_11253 = relay.TupleGetItem(func_5420_call(), 1)
output = relay.Tuple([call_11252,])
output2 = relay.Tuple([call_11253,])
func_11258 = relay.Function([], output)
mod['func_11258'] = func_11258
mod = relay.transform.InferType()(mod)
output = func_11258()
func_11259 = relay.Function([], output)
mutated_mod['func_11259'] = func_11259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8167_call = mod.get_global_var('func_8167')
func_8168_call = mutated_mod.get_global_var('func_8168')
call_11301 = relay.TupleGetItem(func_8167_call(), 1)
call_11302 = relay.TupleGetItem(func_8168_call(), 1)
func_5738_call = mod.get_global_var('func_5738')
func_5743_call = mutated_mod.get_global_var('func_5743')
const_11307 = relay.const([4,-6,6,-4,-6,-9,-7,-6,-1,3,-1,-6,-3,5,1,-5,10,1,9,-1,6,-7,9,9,-6,-3,-3,-10,-9,10,7,-6,7,4,-5,-1,7,5,1,-9,8,4,10,10,6,-1,5,1,5,10,-2,-4,-10,6,-4,-10,6,-6,7,10,-7,-8,8,-6,9,-4,10,-2,6,-4,5,-5,-6,-9,-8,-8,-2,7,8,-3,-1,9,-7,-4,1,5,9,-6,10,10,6,3,6,8,-5,-2,1,10,2,-1,9,6,-6,7,-10,4,-6,-6,8,6,-6,-2,8,5,3,3,-3,-3,1,-5,-8,-1,-7,-5,-2,10,9,-6,-3,7,8,1,-8,10,-4,-4,-3,7,3,-7,-2,4,-9,8,-3,10,-6,-5,-3,6,10,-10,-5,5,8,3,-10,-3,7,-1,-10,-2,-9,-3,-1,-2,8,-4,-10,1,2,9,-10,1,6,8,2,-2,-8,-5,-1,8,10,4,-10,7,-10,-1,9,-10,3,-8,-9,-8,-5,-3,-2,8,4,10,-9,-5,-3,1,-10,8,-10,-10,9,5,-3,-10,1,6,2,-9,-5,9,-3,-2,3,8,-6,-2,8,-1,-6,-7,1,-2,9,3,8,-2,6,3,3,1,-2,8,-10,5,10,-3,-5,-3,10,8,9,6,3,-5,5,-10,8,-10,-7,-4,-7,7,6,6,-5,2,4,1,1,8,1,2,-7,8,7,10,-1,-6,6,-10,8,-7,2,-2,4,-9,-7,2,5,-10,2,-8,7,-9,-8,4,-3,-8,10,7,9,7,-9,2,1,-8,-1,7,2,1,-4,-6,9,-1,-6,-1,8,-5,-8,-3,-10,-1,7,1,3,9,-8,-6,3,-5,8,5,3,5,8,10,8,1,9,-9,3,-2,5,9,5,-8,-8,-1,5,-2,-3,-3,4,-8,-5,7,-5,2,-5,9,-2,3,1,3,-7,1,7,-10,-9,6,-7,5,-10,-5,5,-4,-10,9,10,-9,8,8,-5,6,1,1,5,-4,-2,-9,-3,-6,-2,8,8,3,-7,-1,1,8,1,2,5,10,-4,-4,6,4,6,1,9,-2,-5,9,-2,8,6,1,7,-7,-2,10,1,-7,-5,-5,-2,-1,1,3,-6,-9,2,-2,-3,1,-9,5,-6,1,1,-8,-2,-8,-8,8,-3,-6,9,5,6,7,-9,-7,5,10,3,-8,6,10,6,-10,7,3,4,7,-4,-7,-7,9,2,9,-7,10,3,-9,-10,-10,-5,-2,-3,-2,3,1,4,3,9,-1,9,10,-3,-2,10,-9,-5,5,-10,-4,-8,3,4,8,-2,-2,2,2,2,10,6,-6,-10,6,10,3,4,10,5,-3,-8,-7,-8,-8,5,-10,-7,9,-9,-7,4,7,-7,-7,-6,9,-5,6,7,2,4,-2,-10,8,7,-10,-9,-10,7,-1,6,-9,-8,4,1,-7,10,5,2,1,3,2,-10,8,-8,10,-1,-6,-4,-4,6,1,3,-8,-1,6,-2,-6,1,-2,3,4,3,-2,-10,-3,10,-4,9,-9,1,-4,4,-9,-4,-5,-5,2,8,-4,-2,5,-10,-4,1,9,7,-6,1,-7,6,-3,-10,8,9,-6,-10,1,-2,-9,6,-4,3,-7,7,1,-5,-4,-7,5,-6,-7,4,6,-4,-6,7,5,-1,-4,6,2,10,-8,-10,-5,4,5,-1,-1,-8,-7,-8,-4,-7,-7,-4,6,-9,-10,-7,-7,8,-6,-5,-6,-5,-7,-7,4,-1,-7,-4,-8,-7,-3,-3,3,2,-2,8,9,1,10,1,10,-7,-7,-9,-3,3,-9,6,-10,3,5,-10,-9,-4,-6,3,5,2,10,-6,10,-8,-8,2,3,9,-9,4,-9,8,-1,1,10,7,9,-4,-5,-7,-5,10,-4,-5,10,-4,-6,-4,1], dtype = "uint8")#candidate|11307|(728,)|const|uint8
const_11308 = relay.const([4.168843,4.652540,4.092292,4.797997,5.047766,1.999297,-2.545973,0.066309,-9.296912,-0.407653,-0.393026,-4.536228,2.659070,6.209749,-6.189316,0.112932,6.854619,-4.744343,-3.240616,-7.529460,-9.612609,-4.618987,8.302994,8.330734,8.241324,2.865039,7.978614,7.296189,1.283486,5.088164,3.214879,5.015955,3.046811,-8.470232,6.547326,-9.223606,-3.139043,-1.343482,-1.915980,4.016314,9.347016,-2.695381,-6.196255,3.650516,-4.979431,8.130075,2.422864,-3.445805,-7.173147,1.561705,0.080404,-8.634674,-8.919644,-6.012844,-2.761006,-4.635843,-5.100231,-3.235731,-2.803198,-2.546140,-0.587409,5.879325,-1.919799,7.748743,-4.691240,-8.776988,-7.786034,2.816424,2.748067,9.928027,1.066881,5.961548,-8.782055,-3.262733,0.685657,-8.865076,-8.529261,-7.929349,7.816503,1.234337,-5.986756,-9.484177,-7.725098,2.779147,0.879633,-9.002435,-2.255589,-8.075549,7.754691,1.873603], dtype = "float64")#candidate|11308|(90,)|const|float64
const_11309 = relay.const([-3,-5,-5,6,-6,-3,3,-5,10,1,-4,-5,-9,-5,1,6,-2,-7,-3,-2,-6,-7,5,-4,-4,5,9,-7,3,7,-8,9,3,9,-9,-6,8,-7,-7,-7,5,-9,4,-5,7,-2,-2,-7,7,2,8,4,-1,-6,2,-9,5,-1,3,-7,-5,-7,2,-5,-1,6,5,3,10,4,5,9,3,-1,6,-7,9,-10,-10,-9,-2,-10,6,2,-5,8,-10,-1,6,9,8,-3,-2,7,9,-2,-2,5,8,-3,-4,4,-9,8,5,-9,7,-1,6,2,-5,-4,9,-4,-9,-3,-2,-8,1,10,5,-2,-3,3,2,-5,-10,-3,-2,-9,8,3,-8,-2,-9,9,-4,-8,6,6,-5,-5,4,5,7,-7,5,-6,3,1,2,7,3,-1,-5,4,-10,8,-9,1,6,-2,8,-3,5,4,-6,-1,6,-7,-3,-2,2,-8,-2,8,5,-10,-7,7,-9,-1,-1,5,6,-8,-2,1,-10,-6,8,-2,-5,7,5,6,-4,-10,-9,2,-6,-2,1,-4,-4,5,6,4,-10,-3,-4,1,-4,-5,-8,8,-7,4,-6,1,1,-10,3,-6,7,-10,-8,1,1,-5,-2,3,-5,-9,5,1,-8,-3,-6,-6,8,-4,-4,-10,-2,6,-10,-5,-5,-8,-6,6,-1,-5,-10,2,4,6,-4,6,1,-1,-10,8,3,-6,6,-1,5,-5,-6,10,-4,1,-3,3,-9,-7,-3,4,2,2,-6,-4,-10,3,-8,5,1,2,-3,10,-1,10,-5,-7,4,4,4,-10,-6,10,6,-8,3,1,-4,7,9,9,-2,10,10,6,9,-10,-9,-1,-8,-1,6,9,6,-7,-3,-10,5,-3,-3,10,-6,-9,1,-9,-8,9,6,-5,-4,-7,1,6,-7,-10,7,-2,-10,-10,-10,9,-1,1,-6,10,-1,1,-4,5,-3,2,8,-4,5,-9,-5,3,9,-3,-2,-7,10,2,-4,-7,-5,8,3,2,-8,-2,-1,8,9,-7,4,2,3,-10,-3,3,-8,-1,-4,8,4,-4,-3,7,2,2,9,10,10,-10,-8,10,3,-6,2,9,-2,-3,3,-6,3,3,-4,7,-2,6,9,6,5,10,-4,5,2,-10,7,2,-5,-3,7,-2,6,-10,2,-8,-8,8,7,-9,-1,-4,6,-10,2,-2,5,7,-2,8,-3,-2,-5,4,-4,-1,-1,-5,2,1,-1,4,-7,-9,7,4,6,-2,8,2,-8,-9,7,-7,-1,4,1,10,-8,8,8,9,2,4,-7,4,-7,-4,8,5,8,-3,-9,9,-4,7,1,-6,7,-4,6,8,2,-10,-3,-2,-8,2,-10,9,7,7,-1,-2,-5,-1,-4,-6,2,7,-3,-8,5,-10,-10,8,2,7,8,-2,-8,4,5,-10,-6,-4,-7,-9,10,-7,6,-10,-1,-6,10,2,2,-2,7,-5,9,3,-2,8,2,4,9,8,3,-8,1,-1,-7,-1,-4,-9,-6,9,-5,-1,10,-4,-1,10,-8,9,10,4,4,4,-2,1,5,7,6,-4,-5,-7,3,-2,-6,10,-10,3,-8,4,-10,-9,4,3,-5,-4,7,7,-9,-9,-10,10,1,-6,2,10,-4,5,6,5,6,2,-3,3,9,-8,1,1,-3,3,-8,5,4,7,1,1,-3,3,5,-1,-8,-7,7,2,-6,5,-10,5,4,5,-6,-3,1,-7,1,-3,7,7,8,3,-6,10,-9,-1,-7,-8,-3,1,6,4,-6,-6,7,-6,-3,-2,7,5,5,1,-2,-4,-10,3,-3,-5,4,-3,-5,9,-9,-6,-3,6,-7,-1,-6,6,-7,5,-5,-10,-2,-1,1,-4,1,9,-1,1,2,8,6,-5,6,5,-10,2,8,-8,1,1,4,-5,7,-6,9,-8,-2,10,-4,-9,7,-8,-3,6,-10,8,-7,2,1,4,2,5,-8,1,-9,6,-10,-3,-1,-10,3,9,-3,7,-7,-5,4,2,-4,-4,3,-1,4,-7,10,-10,-7,5,7,5,-3,-2,10,-9,-9,9,2,-5,1,-3,-1,-6,-1,-8,4,-2,-4,6,-10,-2,9,-1,1,-9,-1,-5,-7,-3,-5,5,-6,8,3,6,10,-2,-1,-10,-10,7,1,-6,-7,5,9,9,10,5,-3,7,-1,2,4,4,-9,7,-5,8,-9,-1,-4,-4,-10,-6,-2,-4,-1,-4,-8,-9,1,7,-9,7,-8,6,1,-8,1,-3,8,7,-6,4,-1,-1,1,8,4,7,6,-6,3,7,8,6,-7,-7,4,-7,6,-7,7,-6,3,-5,-7,5,4,4,1,-10,-3,-3,8,-1,-9,3,8,-9,5,9,4,5,-5,4,1,6,10,-10,-9,-3,3,-8,-7,1,2,5,-3,6,9,6,3,-3,-9,-9,6,-1,-10,-10,-6,9,1,6,2,4,1,1,-9,-4,7,-9,9,-4,8,4,-4,-4,6,-9,-1,2,-2,-5,-7,-9,4,9,-9,2,6,-5,-8,-5,10,-5,-8,2,-7,-9,6,1,10,-5,3,-10,3,1,-6,-8,-4,-7,7,10,-6,10,-1,-4,-1,1,6,4,7,-1,-6,9,-9,10,-8,3,3,6,4,-6,10,-10,-9,4,-4,10,3,7,8,9,2,-9,-5,1,-6,-6,-4,-1,-3,-8,-9,6,-10,5,4,3,5,-3,7,-2,10,-9,4,-7,4,-5,-6,6,-8,3,4,10,-7,2,8,9,9,4,8,2,9,-7,-10,10,-4,2,2,-7,-6,5,2,3,9,-5,-9,9,4,-2,8,2,8,10,-5,-8,-8,6,6,1,5,4,-3,-1,-8,-3,6,8,9,-3,-7,-9,6,4,3,9,3,1,6,-5,4,1,-3,-5,9,1,10,8,5,2,-9,-5,4,-8,-9,-7,1,4,-8,-8,-8,-10,9,8,2,-2,-1,-3,7,7,4,-1,-3,9,-6,8,-6,-6,-8,10,4,-3,1,2,-7,3,5,4,-1,-9,10,4,-8,2,5,-10,-4,-6,8,2], dtype = "uint64")#candidate|11309|(1152,)|const|uint64
call_11306 = relay.TupleGetItem(func_5738_call(relay.reshape(const_11307.astype('uint8'), [728,]), relay.reshape(const_11308.astype('float64'), [90,]), relay.reshape(const_11309.astype('uint64'), [1152,]), ), 9)
call_11310 = relay.TupleGetItem(func_5743_call(relay.reshape(const_11307.astype('uint8'), [728,]), relay.reshape(const_11308.astype('float64'), [90,]), relay.reshape(const_11309.astype('uint64'), [1152,]), ), 9)
bop_11311 = relay.less_equal(call_11306.astype('bool'), relay.reshape(const_11309.astype('bool'), relay.shape_of(call_11306))) # shape=(12, 16, 6)
bop_11314 = relay.less_equal(call_11310.astype('bool'), relay.reshape(const_11309.astype('bool'), relay.shape_of(call_11310))) # shape=(12, 16, 6)
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_11315 = relay.TupleGetItem(func_7731_call(relay.reshape(const_11308.astype('float64'), [90,])), 2)
call_11316 = relay.TupleGetItem(func_7733_call(relay.reshape(const_11308.astype('float64'), [90,])), 2)
func_10722_call = mod.get_global_var('func_10722')
func_10724_call = mutated_mod.get_global_var('func_10724')
call_11323 = relay.TupleGetItem(func_10722_call(), 1)
call_11324 = relay.TupleGetItem(func_10724_call(), 1)
func_8535_call = mod.get_global_var('func_8535')
func_8537_call = mutated_mod.get_global_var('func_8537')
call_11347 = func_8535_call()
call_11348 = func_8535_call()
output = relay.Tuple([call_11301,const_11307,const_11308,bop_11311,call_11315,call_11323,call_11347,])
output2 = relay.Tuple([call_11302,const_11307,const_11308,bop_11314,call_11316,call_11324,call_11348,])
func_11351 = relay.Function([], output)
mod['func_11351'] = func_11351
mod = relay.transform.InferType()(mod)
mutated_mod['func_11351'] = func_11351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11351_call = mutated_mod.get_global_var('func_11351')
call_11352 = func_11351_call()
output = call_11352
func_11353 = relay.Function([], output)
mutated_mod['func_11353'] = func_11353
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11357 = relay.var("var_11357", dtype = "int16", shape = ())#candidate|11357|()|var|int16
const_11358 = relay.const([[[-3],[8],[-9],[-5]],[[-10],[5],[-4],[-6]],[[10],[-2],[6],[7]],[[-1],[-2],[-7],[4]],[[5],[-3],[-4],[3]],[[9],[-9],[4],[4]],[[3],[6],[9],[9]],[[-8],[-7],[-9],[5]],[[3],[-8],[-8],[-3]],[[8],[-10],[9],[-6]],[[-9],[2],[-8],[9]],[[3],[2],[-7],[5]]], dtype = "int16")#candidate|11358|(12, 4, 1)|const|int16
bop_11359 = relay.bitwise_and(var_11357.astype('int16'), const_11358.astype('int16')) # shape=(12, 4, 1)
output = relay.Tuple([bop_11359,])
output2 = relay.Tuple([bop_11359,])
func_11365 = relay.Function([var_11357,], output)
mod['func_11365'] = func_11365
mod = relay.transform.InferType()(mod)
var_11366 = relay.var("var_11366", dtype = "int16", shape = ())#candidate|11366|()|var|int16
output = func_11365(var_11366)
func_11367 = relay.Function([var_11366], output)
mutated_mod['func_11367'] = func_11367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4962_call = mod.get_global_var('func_4962')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_11391 = func_4962_call()
call_11392 = func_4962_call()
func_11258_call = mod.get_global_var('func_11258')
func_11259_call = mutated_mod.get_global_var('func_11259')
call_11398 = relay.TupleGetItem(func_11258_call(), 0)
call_11399 = relay.TupleGetItem(func_11259_call(), 0)
output = relay.Tuple([call_11391,call_11398,])
output2 = relay.Tuple([call_11392,call_11399,])
func_11402 = relay.Function([], output)
mod['func_11402'] = func_11402
mod = relay.transform.InferType()(mod)
output = func_11402()
func_11403 = relay.Function([], output)
mutated_mod['func_11403'] = func_11403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5626_call = mutated_mod.get_global_var('func_5626')
call_11448 = func_5625_call()
call_11449 = func_5625_call()
func_4895_call = mod.get_global_var('func_4895')
func_4902_call = mutated_mod.get_global_var('func_4902')
var_11460 = relay.var("var_11460", dtype = "bool", shape = ())#candidate|11460|()|var|bool
var_11461 = relay.var("var_11461", dtype = "bool", shape = (42,))#candidate|11461|(42,)|var|bool
call_11459 = relay.TupleGetItem(func_4895_call(relay.reshape(var_11460.astype('bool'), []), relay.reshape(var_11461.astype('bool'), [6, 1, 7]), relay.reshape(call_11448.astype('float32'), [120, 4]), relay.reshape(var_11461.astype('bool'), [6, 1, 7]), relay.reshape(call_11448.astype('float32'), [8, 15, 4]), ), 2)
call_11462 = relay.TupleGetItem(func_4902_call(relay.reshape(var_11460.astype('bool'), []), relay.reshape(var_11461.astype('bool'), [6, 1, 7]), relay.reshape(call_11448.astype('float32'), [120, 4]), relay.reshape(var_11461.astype('bool'), [6, 1, 7]), relay.reshape(call_11448.astype('float32'), [8, 15, 4]), ), 2)
func_8609_call = mod.get_global_var('func_8609')
func_8613_call = mutated_mod.get_global_var('func_8613')
var_11464 = relay.var("var_11464", dtype = "uint8", shape = (728,))#candidate|11464|(728,)|var|uint8
const_11465 = relay.const([-6.680895,4.365385,-7.886246,6.633625,3.909671,-0.589758,2.410156,9.763006,6.066819,0.509108,-1.843238,8.947947,-3.052755,-8.770322,0.046305,-8.768549,5.898327,4.204662,2.006384,-5.644906,4.039338,-2.273347,-2.697802,3.683054,3.667747,-4.619057,-1.059722,-2.204338,-3.249129,-9.733489,2.624153,7.054136,8.818851,1.963492,-8.593597,4.643099,-7.979961,-1.478012,-0.284850,-2.352384,-1.183876,7.642625,-1.626879,5.750343,-3.873350,-9.357763,8.121550,-5.411976,-8.239428,4.473347,-8.185174,-6.141847,-0.260422,9.020857,-9.095076,-1.849347,-9.508480,3.036500,3.194385,6.247858,-1.986407,-7.357389,-1.654610,-4.694330,-5.775164,0.114420,0.896938,2.909247,-1.795937,-5.264122,-2.043033,6.463769,-1.300858,7.538739,-8.732930,0.865572,-4.448324,-3.100114,0.989422,3.752485,-6.406891,-1.265563,-2.205192,-2.423330,-7.561423,1.579123,5.419197,1.269639,6.803125,-5.692413], dtype = "float64")#candidate|11465|(90,)|const|float64
const_11466 = relay.const([[-10,-6,-4,7,-9,4,-5,-6,-8,7,-7,6,-3,-1,-9,-6,5,-4,-6,-8,7,10,3,-10,6,-9,-10,-8,-6,-3,-7,-5,-10,1,8,-10,5,1,-9,-9,10,-7,-4,1,-7,-6,3,7],[8,9,1,-5,9,-2,-8,-3,-8,-9,7,-2,-6,9,8,5,5,-6,-1,-1,-6,1,6,2,-2,6,-3,-6,-7,-10,-10,-2,9,9,10,2,-7,-2,5,-4,-7,10,9,8,-8,10,3,1],[4,2,4,-2,7,3,-7,10,-7,3,6,-3,-10,-10,-7,-5,-5,-4,10,-1,9,-8,-10,2,1,-5,-9,-9,3,1,4,-2,-10,-9,4,7,3,2,6,-1,1,3,-6,8,4,9,5,9],[8,8,-10,-7,-10,4,-5,2,3,-6,8,6,3,-1,9,-6,10,10,10,-10,-6,-6,-1,5,-6,3,-6,5,6,-10,6,3,1,-5,-1,-3,1,-8,-10,6,-5,-9,10,10,9,-3,7,2],[-9,3,4,-7,-5,-7,9,10,-4,4,-2,2,-6,8,-10,5,1,-9,2,-10,-2,-4,4,-4,-1,-4,3,-6,-8,-4,9,8,-7,-3,-5,-8,3,10,5,6,2,-1,-6,6,1,4,1,-10],[-9,1,-9,4,10,9,-8,3,7,-7,-1,6,-4,4,2,-8,-8,-8,-8,6,4,5,-10,-2,-4,-9,3,-7,-8,6,4,3,-3,-8,1,10,9,7,-6,6,9,5,1,-1,-4,8,-1,1],[-2,-4,10,8,1,-9,-6,7,10,-7,5,-9,7,6,-8,9,-5,-3,-8,4,-6,-6,-8,10,-6,-9,7,9,-5,9,1,3,2,1,-9,-9,10,9,-10,-5,6,-7,-10,-8,-1,-8,6,10],[-7,9,-8,1,4,3,9,-8,2,1,-2,-4,-5,-7,4,-10,-8,9,7,-3,1,5,-6,8,-10,7,-5,7,5,-2,1,2,-3,7,-10,-3,8,3,-2,-9,10,-8,-1,7,-1,5,-1,1],[-5,-3,9,-7,5,1,1,-4,10,-5,7,6,-1,9,-5,7,1,6,8,-8,-3,2,3,-4,8,-3,-3,2,-8,-7,5,5,-4,9,4,4,-8,-9,2,3,3,4,3,-2,-9,5,3,-2],[-1,-10,8,-10,2,-7,-3,2,-6,-3,-4,-1,-2,-9,-4,-3,-1,10,8,-6,-9,5,-7,9,-5,4,5,-4,-10,3,3,-1,-10,-4,10,1,6,1,-4,7,-3,9,-4,5,6,-2,-6,5],[-5,-6,-10,-4,2,-10,-8,-6,-5,8,-9,-7,-3,-6,-1,4,-10,1,-7,6,2,6,10,10,-8,-7,5,4,3,8,-10,2,-5,10,7,1,-10,9,10,9,2,-5,-2,-7,-8,10,9,8],[6,8,-1,-5,6,5,7,-4,-10,8,-7,-8,1,-2,2,6,5,-3,3,-9,4,-4,8,10,6,-1,-2,-9,8,3,1,-10,-3,5,1,-4,-10,3,-6,-7,10,7,-8,5,8,-8,7,-7],[10,-6,-6,7,-9,-3,5,7,-7,-7,3,-10,10,-1,-5,9,10,8,8,-1,6,-9,-5,6,3,8,-3,-8,-8,2,-5,1,-8,1,-4,10,8,3,-10,-9,10,10,8,8,4,1,1,-5],[3,-3,-8,-1,2,2,-2,-4,8,8,1,4,-6,-5,7,3,3,8,-9,-10,2,-3,-4,-7,-5,8,10,9,7,10,3,-3,-1,2,2,1,5,-6,-4,-1,9,3,1,5,8,-1,3,1],[-7,-2,-4,-2,-8,10,-3,-9,10,4,-5,-7,-6,-6,-4,-3,-10,9,7,-5,-2,-4,-5,9,-6,5,2,6,4,-9,1,-9,-6,-6,-2,7,-7,-8,6,8,-10,5,8,-2,-3,9,2,4],[-8,2,-3,-3,1,-5,-1,-1,5,-3,-5,-5,7,-2,-4,8,7,10,-8,-2,-4,-6,-7,6,-10,7,7,4,8,2,2,-1,-9,-1,-6,3,-10,-7,-5,1,3,9,-3,-3,-8,-10,6,-9],[6,1,5,-2,-5,1,1,3,3,-3,8,-5,10,9,1,-2,-10,-9,-8,-7,9,3,2,-5,2,1,-3,-6,-4,-10,3,-1,4,7,10,-7,5,-10,-5,-2,-2,-7,-9,-9,-8,-9,-2,7],[10,-10,-9,9,4,-1,-4,-8,-7,-1,-7,-9,-1,9,9,-9,-9,7,-5,-4,-6,2,9,6,4,-2,8,-8,-2,-2,3,9,-4,4,5,-10,4,-10,-9,-10,-4,6,6,2,-2,-10,-8,1],[-7,1,2,2,-3,-8,1,-7,-2,8,8,-7,-2,9,6,-4,-2,5,-6,9,-1,2,-7,-8,4,9,4,4,3,-8,3,3,8,-9,-7,6,9,2,8,7,4,4,3,5,-3,-6,6,-2],[-9,1,-3,-4,4,8,-5,-4,2,8,9,-1,8,-7,-9,1,1,-4,8,7,-5,3,-2,1,-8,9,-4,-8,-2,-9,7,10,3,-2,-3,2,-4,8,-6,1,-7,1,-3,-4,-7,5,-4,-10],[1,7,-3,-2,7,-4,-8,-7,7,6,9,6,-4,8,8,-4,-1,2,3,-2,3,-3,1,6,10,-8,4,2,5,-6,9,-1,-3,4,-5,8,2,-1,-3,-1,-10,3,4,-2,5,-1,7,7],[-3,8,9,7,7,-6,-4,-5,-7,10,4,-10,7,-5,3,6,5,7,-10,-5,2,-1,-8,3,-5,-7,-3,1,-8,8,-10,-9,-10,9,3,-9,5,3,6,-9,9,1,-10,-3,1,-10,-8,4],[-7,8,-6,5,6,-5,4,-5,-7,-4,-1,5,-10,2,8,-4,8,-5,10,6,-9,-10,4,-3,-6,-5,-4,10,7,-2,8,10,-9,-2,6,-6,-10,8,-4,2,8,8,10,-5,-9,-2,2,-5],[-8,1,7,-8,6,1,-7,-1,-2,6,-8,-1,-8,4,-4,3,7,5,-3,-1,9,8,-4,-8,9,-8,-4,4,1,-4,-8,-8,-10,9,6,-2,-1,-2,1,-1,5,-7,-2,1,-8,10,-1,-3]], dtype = "uint64")#candidate|11466|(24, 48)|const|uint64
call_11463 = relay.TupleGetItem(func_8609_call(relay.reshape(var_11464.astype('uint8'), [728,]), relay.reshape(const_11465.astype('float64'), [3, 30]), relay.reshape(const_11466.astype('uint64'), [1152,]), ), 1)
call_11467 = relay.TupleGetItem(func_8613_call(relay.reshape(var_11464.astype('uint8'), [728,]), relay.reshape(const_11465.astype('float64'), [3, 30]), relay.reshape(const_11466.astype('uint64'), [1152,]), ), 1)
output = relay.Tuple([call_11448,call_11459,var_11460,var_11461,call_11463,var_11464,const_11465,const_11466,])
output2 = relay.Tuple([call_11449,call_11462,var_11460,var_11461,call_11467,var_11464,const_11465,const_11466,])
func_11468 = relay.Function([var_11460,var_11461,var_11464,], output)
mod['func_11468'] = func_11468
mod = relay.transform.InferType()(mod)
mutated_mod['func_11468'] = func_11468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11468_call = mutated_mod.get_global_var('func_11468')
var_11470 = relay.var("var_11470", dtype = "bool", shape = ())#candidate|11470|()|var|bool
var_11471 = relay.var("var_11471", dtype = "bool", shape = (42,))#candidate|11471|(42,)|var|bool
var_11472 = relay.var("var_11472", dtype = "uint8", shape = (728,))#candidate|11472|(728,)|var|uint8
call_11469 = func_11468_call(var_11470,var_11471,var_11472,)
output = call_11469
func_11473 = relay.Function([var_11470,var_11471,var_11472,], output)
mutated_mod['func_11473'] = func_11473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
call_11623 = relay.TupleGetItem(func_7482_call(), 1)
call_11624 = relay.TupleGetItem(func_7484_call(), 1)
output = relay.Tuple([call_11623,])
output2 = relay.Tuple([call_11624,])
func_11651 = relay.Function([], output)
mod['func_11651'] = func_11651
mod = relay.transform.InferType()(mod)
mutated_mod['func_11651'] = func_11651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11651_call = mutated_mod.get_global_var('func_11651')
call_11652 = func_11651_call()
output = call_11652
func_11653 = relay.Function([], output)
mutated_mod['func_11653'] = func_11653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9615_call = mod.get_global_var('func_9615')
func_9617_call = mutated_mod.get_global_var('func_9617')
call_11731 = relay.TupleGetItem(func_9615_call(), 0)
call_11732 = relay.TupleGetItem(func_9617_call(), 0)
func_11114_call = mod.get_global_var('func_11114')
func_11116_call = mutated_mod.get_global_var('func_11116')
call_11735 = relay.TupleGetItem(func_11114_call(), 0)
call_11736 = relay.TupleGetItem(func_11116_call(), 0)
func_10633_call = mod.get_global_var('func_10633')
func_10635_call = mutated_mod.get_global_var('func_10635')
call_11752 = relay.TupleGetItem(func_10633_call(), 0)
call_11753 = relay.TupleGetItem(func_10635_call(), 0)
func_8964_call = mod.get_global_var('func_8964')
func_8975_call = mutated_mod.get_global_var('func_8975')
const_11755 = relay.const([-7.817218,1.031054,-0.054527,0.122981,7.910055,-4.947222,7.324027,-1.422974,3.209740,-4.481854,6.025920,-7.508499,-9.460553,-9.665419,2.503086,1.758288,-4.537699,-1.787265,-2.868693,7.321950,4.503790,-8.559355,6.893636,4.426564,-5.158171,-1.841630,5.725210,-1.027762,8.444450,-0.392272,7.395897,-5.057128,-3.289783,4.824537,-7.790534,-8.309245,-3.060877,9.685450,3.188309,1.760694,-0.799355,3.063863,-4.745756,7.180397,3.630682,-3.970038,6.733196,-0.733381,0.652187,-1.191297,-3.283275,-0.854799,4.491852,-9.497530,-2.036157,-5.063873,-9.550279,-5.808612,1.018299,-5.425510,4.924405,-0.710242,5.150812,0.499933,-6.673960,1.116354,-1.362675,1.197176,8.280373,1.244990,2.231403,-2.829233,3.137846,4.908294,-1.604542,1.310660,-1.207278,-6.843962,-2.478377,6.497527,9.040784,3.192029,-9.375104,9.599266,5.387521,7.731597,-9.933917,-0.781930,-5.245184,-6.205005], dtype = "float64")#candidate|11755|(90,)|const|float64
const_11756 = relay.const([9,-9,-1,9,8,4,5,3,10,-5,-9,8,6,10,-9,1,9,3,3,-6,1,-8,2,8,-5,5,-9,-6,7,8,9,3,1,5,-7,-5,-3,-7,-8,-8,-7,9,-4,-2,10,-6,-9,-6,7,4,-4,-4,-4,1,7,5,2,9,-8,6,1,7,-5,2,-6,-5,5,-7,-10,1,10,1,-9,-8,3,6,-10,-6,8,6,-2,4,2,-6,-2,2,-2,-5,-7,-9,9,-4,10,3,-8,4,1,7,3,-8,2,-8,4,5,-6,-10,10,3,6,2,6,3,-7,-3,-6,5,10,2,7,-5,-2,8,-1,-5,-9,-2,-2,2,-5,-10,-5,-3,-8,-9,4,6,1,9,-6,-10,1,10,4,3,-9,4,-7,1,2,8,5,2,-9,5,-5,-8,6,-2,-4,-2,7,6,-1,-9,8,8,1,-7,-1,4,9,4,4,6,10,-10,3,3,5,-8,-7,-4,8,-1,-6,-9,-10,2,9,-1,-5,-8,-7,4,-10,4,-1,-10,-4,10,-5,-6,-1,9,6,1,-1,10,1,-1,-8,-10,7,-10,10,-10,-8,-10,-5,-3,8,-10,4,-8,-6,7,6,-3,-9,2,4,4,10,-2,-2,-6,10,1,8,10,6,7,5,5,-4,3,2,-9,3,7,-8,-8,-9,-4,-6,-10,-2,-8,-9,-2,1,1,7,6,-3,5,-6,-10,4,1,-8,6,-7,6,-7,-9,8,-4,1,-2,4,6,4,4,-9,10,5,-7,10,8,-6,8,8,6,3,-8,9,9,-1,1,-8,-7,-7,-3,10,2,10,-9,-1,10,2,3,1,5,2,3,-7,3,7,-8,-9,4,-2,8,5,-9,7,10,-3,3,1,7,6,-1,-6,-3,-3,4,7,1,3,3,-4,-1,8,-2,8,8,-7,-1,1,-10,9,2,-10,-10,-4,5,5,-3,-8,3,-4,3,3,-6,8,-1,-4,4,5,-6,-8,5,5,-6,4,-10,-4,10,7,-2,-6,3,-3,1,-3,-6,-8,-4,-8,-7,-4,1,-1,5,-8,4,-9,3,6,-9,3,-1,6,-5,8,7,8,-1,-8,9,-1,-2,-10,2,1,6,-7,-4,-2,7,10,3,-3,-6,-9,9,-8,2,-5,5,-8,-7,-5,9,-1,-9,-2,8,-7,6,-9,-7,5,-4,-8,4,9,-2,-6,2,-7,8,-3,5,-9,7,-8,-5,-6,3,8,-9,-1,-1,-1,-4,-6,-10,-7,1,9,-5,2,10,-1,-1,2,-3,-2,10,9,-4,6,-4,-10,-2,10,-6,9,10,10,-6,5,5,-6,-3,-9,-10,2,8,8,2,9,-2,-7,8,-8,-10,-6,10,-10,-8,1,-3,-3,-6,-1,1,-10,8,-9,-5,-1,-8,3,-10,1,1,-8,-5,-5,2,-1,8,9,-9,2,-3,-2,-1,-9,8,-3,-1,3,-1,-7,8,9,-9,2,5,3,-1,1,10,5,9,6,8,-4,-10,4,-8,4,1,5,-1,6,-5,-4,-6,-2,-10,4,10,8,8,-7,-5,4,-8,2,1,-1,-6,1,7,-6,6,4,-8,5,4,-4,5,-7,-1,2,8,6,10,5,-5,-2,-10,6,-9,-4,6,-6,-6,-4,1,-8,-9,4,-4,-7,-9,-1,-7,5,-9,-3,-6,8,9,10,-7,-10,5,-8,-2,-9,7,-9,6,-2,-4,-1,-3,4,-10,5,-5,6,10,8,-10,-2,6,3,7,10,-2,2,10,1,-2,-9,-1,6,10,3,2,9,1,1,-9,7,-4,9,7,-5,-6,6,3,1,8,5,1,8,-8,-10,-2,8,-6,-1,7,-1,-2,2,-1,-9,7,8,2,2,9,-8,-8,8,-3,8,4,-5,-8,-2,-10,-7,8,6,3,9,9,4,4,-3,10,-1,3,-3,-4,10,-9,-2,-2,5,8,7,3,-7,3,6,-3,10,-4,7,-9,6,1,4,-8,-9,5,4,-7,-5,-2,4,9,-1,8,-4,6,6,8,3,7,2,7,-9,6,-3,-6,-4,-2,9,5,-8,3,-8,-1,7,-2,1,-5,-2,-4,-9,-3,-7,-8,-6,2,-3,5,8,-4,-6,-5,6,7,1,6,-4,-3,-5,-1,-5,2,-8,1,4,2,-2,7,9,7,-7,-1,1,4,-6,-6,8,9,6,5,-5,-10,-5,6,-10,3,-7,8,2,-5,-9,-1,10,4,-10,-6,5,4,10,4,-5,7,3,10,-9,4,-6,6,5,-2,10,-1,-3,-5,-5,2,7,-1,-5,8,6,6,6,-9,-2,7,-8,-7,3,5,4,-9,-7,3,-1,-9,-4,-10,5,-3,-2,-10,-1,3,-2,6,-6,-9,5,-6,-5,-3,10,-1,-5,-5,-7,1,-6,5,-3,-4,-6,-3,-6,-5,-5,-10,-6,-1,7,9,-3,-3,-5,6,9,-8,-6,-6,-9,3,-1,-9,6,-9,-8,-7,9,1,-8,3,-1,-2,1,9,-1,1,5,-1,4,4,-10,-4,-10,-4,-5,8,9,3,10,-7,-2,4,-2,10,5,-7,-2,-4,9,-3,-7,8,-10,6,-3,-8,-3,4,-7,9,-6,-9,-9,-5,2,-3,-6,7,-2,-6,3,-9,8,10,-8,9,7,-4,-2,-7,6,3,10,8,10,8,7,2,1,-3,2,2,-10,10,-7,6,6,3,-1,10,6,7,-5,9,2,6,-3,-5,-7,7,-3,-5,-4,7,-3,7,4,3,4,7,3,9,-2,-3,1,-2,2,-3,10,-4,-8,-10,-6,2,-4,-5,2,5,8,4,-7,-4,-6,7,-9,-8,-3,-1,-9,8,-4,2,-7,-2,4,-6,4,2,-9,5,10,-6,2,-2,10,6,-5,2,5,6,-1,2,2,-5,-1,-8,-6,5,-2,8,-7,6,3,3,-3,7,3,9,-3,6,-7,-6,1,-10,10,-2,2,-10,-7,3,4,-2,-1,-4,-7,10,-7,6,10,8,6,7,-10,-5,10,5,-9,-2,-9,-7,-9,10,-3,-3,-4,3,2,8,-6,9,10,-1,2,-1,2,-9,5,6], dtype = "uint64")#candidate|11756|(1152,)|const|uint64
var_11757 = relay.var("var_11757", dtype = "float32", shape = (198,))#candidate|11757|(198,)|var|float32
const_11758 = relay.const([False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False], dtype = "bool")#candidate|11758|(672,)|const|bool
var_11759 = relay.var("var_11759", dtype = "uint8", shape = (728,))#candidate|11759|(728,)|var|uint8
var_11760 = relay.var("var_11760", dtype = "float32", shape = (256,))#candidate|11760|(256,)|var|float32
var_11761 = relay.var("var_11761", dtype = "int32", shape = ())#candidate|11761|()|var|int32
const_11762 = relay.const([-5.150015,5.960894,9.015151,-0.550419,0.863351,8.374587,-1.596509,8.545736,-6.745936,7.998614,-8.707435,-4.852052,-9.026951,-6.602428,8.834401,-2.766607,-2.504086,5.316397,-5.350252,7.296629,9.593248,-7.737128,3.983645,1.448597,4.581698,9.911745,-4.840816,7.062037,-7.820508,-8.294993,8.234571,8.478426,8.027521,6.454464,2.367771,0.848318,1.242553,-6.284911,9.544288,-2.116563,-0.168984,-4.549937,2.058069,9.826674,-6.128438,3.879284,-1.655576,9.526466,-7.781832,2.186764,2.213335,-3.562080,-9.105359,6.341555,2.236474,5.994925,3.654092,-6.142887,0.974550,-4.758208,-5.182843,0.826717,5.584348,-9.245952,1.653525,7.055944,-9.739826,7.387922,-0.734582,7.398096,2.904197,4.887281,-1.091399,8.070403,6.969582,1.959557,-9.615133,-1.237913,9.907964,5.190296,-0.923408,-5.911094,-3.486811,2.792892,-1.330921,-0.206243,6.418491,0.241051,-9.319441,-1.078505,-5.307363,6.148547,-4.094239,-0.979387,-3.510430,6.187343,-6.344120,7.737668,7.952547,7.904744,2.656721,6.463725,0.588811,7.604304,-4.450197,8.076646,3.624570,0.975350,-8.035449,-1.905754,1.032699,5.802674,8.582622,-7.455056,-5.475554,-1.380178,-7.079306,-2.138241,-5.562209,9.794668,6.569506,-6.858255,5.474044,6.171616,2.390505,-7.271703,8.593282,5.187845,-3.052409,8.158079,3.069647,8.334752,-7.568182,-6.300716,0.599995,7.387277,-9.386024,7.024497,2.119992,-0.840250,-5.303611,2.778101,-4.254231,-0.681705,-6.772202,1.156844,-2.351819,7.709267,0.703458,6.214088,6.190109,5.049790,-6.805778,2.547505,6.839667,3.899400,-1.082534,8.460626,2.968729,-7.696809,-8.513837,6.540903,-0.245629,1.395656,-2.257103,-3.380906,1.268220,-0.778917,-5.313186,1.633110,2.297056,-8.098347,6.641677,-1.107404,8.734240,-3.263391,6.651664,-3.689723,6.771875,5.697178,8.920341,5.457745,7.364524,-9.360823,-6.207587,-9.413715,-6.962625,6.220982,-8.656946,-2.703309,-1.249231,6.904091,1.262382,4.838780,3.907637,-1.305641,-6.508317,0.333369,7.949032,-9.979738,4.397110,7.694078,3.636412,8.195429,0.962507,8.642796,3.318143,2.079400,8.950056,4.991364,5.047809,9.236564,1.320126,0.098021,-1.087035,-7.948880,-2.228835,-4.906904,9.107090,-5.493396,9.547838,-2.715513,-8.388903,7.099500,1.280323,3.004277,6.331381,-3.755302,6.505901,5.580251,8.584932,-4.528225,-3.363996,5.750670,-2.316308,-2.954943,-6.222864,-5.373401,-0.269132,-8.228406,-0.052147,-5.901977,-9.532110,7.527630,-5.787580,1.424462,-9.430555,-3.518112,-0.437800,-8.933819,5.926252,7.987007,-8.705528,-7.717028,6.621257,-2.586263,-8.833657,9.245638,3.907514,1.088033,-0.641173,-6.161767,-1.842822,9.436858,-8.337544,2.489975,-8.764572,7.259634,2.661697,7.340233,-0.048443,-9.119541,-8.042867,3.073774,-0.739009,9.470852,-1.695940,-4.730038,-0.333305,5.154725,9.664431,-9.874219,7.612770,-9.944273,-5.088071,-2.121937,4.472778,9.643059,-3.751430,-7.566957,4.555107,4.037768,0.924540,-1.736426,0.930500,-4.230060,9.690968,-3.390445,1.335130,2.562203,-1.541766,-3.488626,-6.524809,0.557908,2.861146,-5.226047,-3.207898,-9.771065,1.192468,4.435426,-0.621030,5.465600,1.279694,0.421245,7.443865,-4.171903,-9.530611,3.041115,-4.895756,4.615039,-8.821057,7.451430,-5.438417,-7.421900,-4.368076,-7.753987,-9.574373,-5.997494,-7.902212,-5.347702,-6.683636,6.936107,5.570341,-4.271315,-0.138321,1.630127,8.561411,9.533979,-5.432126,3.789152,4.091550,-4.094184,2.931285,6.951055,-9.514804,8.027504,-3.151500,1.120464,-2.115968,-8.034388,6.863893,8.758634,-8.446459,-0.855230,5.254191,0.563004,-9.596202,-7.648911,5.693637,3.415719], dtype = "float64")#candidate|11762|(360,)|const|float64
const_11763 = relay.const([False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True], dtype = "bool")#candidate|11763|(336,)|const|bool
call_11754 = relay.TupleGetItem(func_8964_call(relay.reshape(const_11755.astype('float64'), [45, 2]), relay.reshape(const_11756.astype('uint64'), [1152,]), relay.reshape(var_11757.astype('float32'), [198,]), relay.reshape(const_11758.astype('bool'), [2, 336]), relay.reshape(var_11759.astype('uint8'), [13, 4, 14]), relay.reshape(var_11760.astype('float32'), [256,]), relay.reshape(var_11761.astype('int32'), []), relay.reshape(const_11762.astype('float64'), [360,]), relay.reshape(const_11763.astype('bool'), [2, 168]), ), 16)
call_11764 = relay.TupleGetItem(func_8975_call(relay.reshape(const_11755.astype('float64'), [45, 2]), relay.reshape(const_11756.astype('uint64'), [1152,]), relay.reshape(var_11757.astype('float32'), [198,]), relay.reshape(const_11758.astype('bool'), [2, 336]), relay.reshape(var_11759.astype('uint8'), [13, 4, 14]), relay.reshape(var_11760.astype('float32'), [256,]), relay.reshape(var_11761.astype('int32'), []), relay.reshape(const_11762.astype('float64'), [360,]), relay.reshape(const_11763.astype('bool'), [2, 168]), ), 16)
output = relay.Tuple([call_11731,call_11735,call_11752,call_11754,const_11755,const_11756,var_11757,const_11758,var_11759,var_11760,var_11761,const_11762,const_11763,])
output2 = relay.Tuple([call_11732,call_11736,call_11753,call_11764,const_11755,const_11756,var_11757,const_11758,var_11759,var_11760,var_11761,const_11762,const_11763,])
func_11772 = relay.Function([var_11757,var_11759,var_11760,var_11761,], output)
mod['func_11772'] = func_11772
mod = relay.transform.InferType()(mod)
mutated_mod['func_11772'] = func_11772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11772_call = mutated_mod.get_global_var('func_11772')
var_11774 = relay.var("var_11774", dtype = "float32", shape = (198,))#candidate|11774|(198,)|var|float32
var_11775 = relay.var("var_11775", dtype = "uint8", shape = (728,))#candidate|11775|(728,)|var|uint8
var_11776 = relay.var("var_11776", dtype = "float32", shape = (256,))#candidate|11776|(256,)|var|float32
var_11777 = relay.var("var_11777", dtype = "int32", shape = ())#candidate|11777|()|var|int32
call_11773 = func_11772_call(var_11774,var_11775,var_11776,var_11777,)
output = call_11773
func_11778 = relay.Function([var_11774,var_11775,var_11776,var_11777,], output)
mutated_mod['func_11778'] = func_11778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5626_call = mutated_mod.get_global_var('func_5626')
call_11791 = func_5625_call()
call_11792 = func_5625_call()
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_11796 = relay.TupleGetItem(func_5418_call(), 0)
call_11797 = relay.TupleGetItem(func_5420_call(), 0)
func_7369_call = mod.get_global_var('func_7369')
func_7372_call = mutated_mod.get_global_var('func_7372')
call_11828 = relay.TupleGetItem(func_7369_call(relay.reshape(call_11796.astype('bool'), [1200, 1])), 3)
call_11829 = relay.TupleGetItem(func_7372_call(relay.reshape(call_11796.astype('bool'), [1200, 1])), 3)
output = relay.Tuple([call_11791,call_11796,call_11828,])
output2 = relay.Tuple([call_11792,call_11797,call_11829,])
func_11861 = relay.Function([], output)
mod['func_11861'] = func_11861
mod = relay.transform.InferType()(mod)
output = func_11861()
func_11862 = relay.Function([], output)
mutated_mod['func_11862'] = func_11862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9788_call = mod.get_global_var('func_9788')
func_9790_call = mutated_mod.get_global_var('func_9790')
call_11866 = relay.TupleGetItem(func_9788_call(), 2)
call_11867 = relay.TupleGetItem(func_9790_call(), 2)
func_9374_call = mod.get_global_var('func_9374')
func_9376_call = mutated_mod.get_global_var('func_9376')
call_11875 = relay.TupleGetItem(func_9374_call(), 1)
call_11876 = relay.TupleGetItem(func_9376_call(), 1)
output = relay.Tuple([call_11866,call_11875,])
output2 = relay.Tuple([call_11867,call_11876,])
func_11894 = relay.Function([], output)
mod['func_11894'] = func_11894
mod = relay.transform.InferType()(mod)
mutated_mod['func_11894'] = func_11894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11894_call = mutated_mod.get_global_var('func_11894')
call_11895 = func_11894_call()
output = call_11895
func_11896 = relay.Function([], output)
mutated_mod['func_11896'] = func_11896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9564_call = mod.get_global_var('func_9564')
func_9566_call = mutated_mod.get_global_var('func_9566')
call_11960 = relay.TupleGetItem(func_9564_call(), 2)
call_11961 = relay.TupleGetItem(func_9566_call(), 2)
func_3391_call = mod.get_global_var('func_3391')
func_3395_call = mutated_mod.get_global_var('func_3395')
var_11963 = relay.var("var_11963", dtype = "float64", shape = (1512,))#candidate|11963|(1512,)|var|float64
var_11964 = relay.var("var_11964", dtype = "bool", shape = (336,))#candidate|11964|(336,)|var|bool
const_11965 = relay.const([False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False], dtype = "bool")#candidate|11965|(672,)|const|bool
call_11962 = relay.TupleGetItem(func_3391_call(relay.reshape(var_11963.astype('float64'), [14, 9, 12]), relay.reshape(var_11964.astype('bool'), [336,]), relay.reshape(const_11965.astype('bool'), [672,]), ), 4)
call_11966 = relay.TupleGetItem(func_3395_call(relay.reshape(var_11963.astype('float64'), [14, 9, 12]), relay.reshape(var_11964.astype('bool'), [336,]), relay.reshape(const_11965.astype('bool'), [672,]), ), 4)
func_8535_call = mod.get_global_var('func_8535')
func_8537_call = mutated_mod.get_global_var('func_8537')
call_11967 = func_8535_call()
call_11968 = func_8535_call()
output = relay.Tuple([call_11960,call_11962,var_11963,var_11964,const_11965,call_11967,])
output2 = relay.Tuple([call_11961,call_11966,var_11963,var_11964,const_11965,call_11968,])
func_11974 = relay.Function([var_11963,var_11964,], output)
mod['func_11974'] = func_11974
mod = relay.transform.InferType()(mod)
var_11975 = relay.var("var_11975", dtype = "float64", shape = (1512,))#candidate|11975|(1512,)|var|float64
var_11976 = relay.var("var_11976", dtype = "bool", shape = (336,))#candidate|11976|(336,)|var|bool
output = func_11974(var_11975,var_11976,)
func_11977 = relay.Function([var_11975,var_11976,], output)
mutated_mod['func_11977'] = func_11977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10722_call = mod.get_global_var('func_10722')
func_10724_call = mutated_mod.get_global_var('func_10724')
call_11988 = relay.TupleGetItem(func_10722_call(), 0)
call_11989 = relay.TupleGetItem(func_10724_call(), 0)
func_2795_call = mod.get_global_var('func_2795')
func_2798_call = mutated_mod.get_global_var('func_2798')
var_11991 = relay.var("var_11991", dtype = "float64", shape = ())#candidate|11991|()|var|float64
const_11992 = relay.const([[5.739029,1.825656],[-2.859950,-8.351832],[-7.875446,3.230606],[-7.250198,-0.921935],[-4.541533,-1.656262],[-9.675079,9.616314],[7.255523,-4.942118],[-9.153816,7.012072],[-1.606201,-2.588128],[-7.274406,-7.245988],[-1.181260,8.113449],[6.804958,5.662987],[8.949837,8.319605],[5.165574,-6.220100],[0.386429,2.863135],[-9.694301,2.538429],[3.364997,-3.026865],[-5.250466,-0.697619],[-2.233740,3.542128],[0.087110,9.785026],[0.401309,1.747597],[1.613719,0.272626],[-6.923280,8.828675],[6.473456,2.528694],[-9.642586,-2.078766],[-9.856045,9.909701],[-5.314297,-3.624354],[9.396223,-6.011308],[8.915107,-5.716900],[5.651961,9.964592],[-5.551328,-5.517688],[-3.792318,-8.814658],[2.763272,3.507856],[-2.431811,-5.988773],[-1.136179,-6.941549],[-8.192138,-9.291239],[-5.045426,8.540337],[-0.008492,-0.479483],[1.179392,-7.604425],[-3.876318,-0.555761]], dtype = "float64")#candidate|11992|(40, 2)|const|float64
call_11990 = relay.TupleGetItem(func_2795_call(relay.reshape(var_11991.astype('float64'), []), relay.reshape(const_11992.astype('float64'), [2, 10, 4]), ), 2)
call_11993 = relay.TupleGetItem(func_2798_call(relay.reshape(var_11991.astype('float64'), []), relay.reshape(const_11992.astype('float64'), [2, 10, 4]), ), 2)
uop_12006 = relay.exp(call_11990.astype('float64')) # shape=(2, 168)
uop_12008 = relay.exp(call_11993.astype('float64')) # shape=(2, 168)
var_12016 = relay.var("var_12016", dtype = "float64", shape = (2, 168))#candidate|12016|(2, 168)|var|float64
bop_12017 = relay.equal(uop_12006.astype('bool'), relay.reshape(var_12016.astype('bool'), relay.shape_of(uop_12006))) # shape=(2, 168)
bop_12020 = relay.equal(uop_12008.astype('bool'), relay.reshape(var_12016.astype('bool'), relay.shape_of(uop_12008))) # shape=(2, 168)
func_5082_call = mod.get_global_var('func_5082')
func_5084_call = mutated_mod.get_global_var('func_5084')
call_12021 = func_5082_call()
call_12022 = func_5082_call()
output = relay.Tuple([call_11988,var_11991,const_11992,bop_12017,call_12021,])
output2 = relay.Tuple([call_11989,var_11991,const_11992,bop_12020,call_12022,])
func_12023 = relay.Function([var_11991,var_12016,], output)
mod['func_12023'] = func_12023
mod = relay.transform.InferType()(mod)
mutated_mod['func_12023'] = func_12023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12023_call = mutated_mod.get_global_var('func_12023')
var_12025 = relay.var("var_12025", dtype = "float64", shape = ())#candidate|12025|()|var|float64
var_12026 = relay.var("var_12026", dtype = "float64", shape = (2, 168))#candidate|12026|(2, 168)|var|float64
call_12024 = func_12023_call(var_12025,var_12026,)
output = call_12024
func_12027 = relay.Function([var_12025,var_12026,], output)
mutated_mod['func_12027'] = func_12027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4962_call = mod.get_global_var('func_4962')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_12029 = func_4962_call()
call_12030 = func_4962_call()
func_10834_call = mod.get_global_var('func_10834')
func_10836_call = mutated_mod.get_global_var('func_10836')
var_12052 = relay.var("var_12052", dtype = "float64", shape = (1456,))#candidate|12052|(1456,)|var|float64
call_12051 = relay.TupleGetItem(func_10834_call(relay.reshape(var_12052.astype('float64'), [1456,])), 4)
call_12053 = relay.TupleGetItem(func_10836_call(relay.reshape(var_12052.astype('float64'), [1456,])), 4)
func_3950_call = mod.get_global_var('func_3950')
func_3954_call = mutated_mod.get_global_var('func_3954')
const_12057 = relay.const([-5.122946,0.391441,-7.507480,0.588509,-4.741678,-8.188117,9.914189,-2.627538,3.939856,3.836231,5.429867,5.322044,-1.280135,-4.432352,-3.909172,9.241566,2.424244,-5.558580,5.581377,0.774396,6.454275,2.907436,4.928235,8.000308,5.089819,4.730017,-2.377766,-9.944893,-2.228409,-2.174840,4.575537,6.865361,-1.134680,-3.464964,9.540444,7.913634,0.756074,-3.124588,-7.793730,-8.689332,-1.406918,6.291677,-4.393186,8.232236,-1.450185,3.501718,9.551203,-0.043310,-7.767788,2.224322,-1.175477,2.109900,2.343922,-8.762479,4.074555,3.640100,-5.394898,-9.336005,6.638992,-5.157682,0.100208,3.911633,-1.597241,-2.000568,-2.569050,5.251157,-2.944887,0.694866,-4.974468,-5.682797,-9.751796,7.986932,-5.718078,5.507201,2.161464,7.705279,-1.370012,-3.505439,3.467184,1.899354,-7.009822,-3.499699,2.260792,9.723897,-5.185186,-3.675654,0.059704,8.037696,0.745098,4.120592], dtype = "float64")#candidate|12057|(90,)|const|float64
var_12058 = relay.var("var_12058", dtype = "uint64", shape = (1152,))#candidate|12058|(1152,)|var|uint64
call_12056 = relay.TupleGetItem(func_3950_call(relay.reshape(const_12057.astype('float64'), [15, 6]), relay.reshape(var_12058.astype('uint64'), [1152,]), ), 9)
call_12059 = relay.TupleGetItem(func_3954_call(relay.reshape(const_12057.astype('float64'), [15, 6]), relay.reshape(var_12058.astype('uint64'), [1152,]), ), 9)
func_10260_call = mod.get_global_var('func_10260')
func_10264_call = mutated_mod.get_global_var('func_10264')
var_12071 = relay.var("var_12071", dtype = "float64", shape = (630,))#candidate|12071|(630,)|var|float64
call_12070 = relay.TupleGetItem(func_10260_call(relay.reshape(var_12071.astype('float64'), [9, 14, 5]), relay.reshape(var_12071.astype('float64'), [9, 14, 5]), relay.reshape(var_12071.astype('float64'), [9, 14, 5]), ), 0)
call_12072 = relay.TupleGetItem(func_10264_call(relay.reshape(var_12071.astype('float64'), [9, 14, 5]), relay.reshape(var_12071.astype('float64'), [9, 14, 5]), relay.reshape(var_12071.astype('float64'), [9, 14, 5]), ), 0)
output = relay.Tuple([call_12029,call_12051,var_12052,call_12056,const_12057,var_12058,call_12070,var_12071,])
output2 = relay.Tuple([call_12030,call_12053,var_12052,call_12059,const_12057,var_12058,call_12072,var_12071,])
func_12078 = relay.Function([var_12052,var_12058,var_12071,], output)
mod['func_12078'] = func_12078
mod = relay.transform.InferType()(mod)
var_12079 = relay.var("var_12079", dtype = "float64", shape = (1456,))#candidate|12079|(1456,)|var|float64
var_12080 = relay.var("var_12080", dtype = "uint64", shape = (1152,))#candidate|12080|(1152,)|var|uint64
var_12081 = relay.var("var_12081", dtype = "float64", shape = (630,))#candidate|12081|(630,)|var|float64
output = func_12078(var_12079,var_12080,var_12081,)
func_12082 = relay.Function([var_12079,var_12080,var_12081,], output)
mutated_mod['func_12082'] = func_12082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_12101 = func_6126_call()
call_12102 = func_6126_call()
output = relay.Tuple([call_12101,])
output2 = relay.Tuple([call_12102,])
func_12107 = relay.Function([], output)
mod['func_12107'] = func_12107
mod = relay.transform.InferType()(mod)
mutated_mod['func_12107'] = func_12107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12107_call = mutated_mod.get_global_var('func_12107')
call_12108 = func_12107_call()
output = call_12108
func_12109 = relay.Function([], output)
mutated_mod['func_12109'] = func_12109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_12110 = relay.TupleGetItem(func_4068_call(), 1)
call_12111 = relay.TupleGetItem(func_4069_call(), 1)
output = call_12110
output2 = call_12111
func_12115 = relay.Function([], output)
mod['func_12115'] = func_12115
mod = relay.transform.InferType()(mod)
output = func_12115()
func_12116 = relay.Function([], output)
mutated_mod['func_12116'] = func_12116
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12186 = relay.var("var_12186", dtype = "float64", shape = (8, 8, 2))#candidate|12186|(8, 8, 2)|var|float64
uop_12187 = relay.asinh(var_12186.astype('float64')) # shape=(8, 8, 2)
func_9146_call = mod.get_global_var('func_9146')
func_9149_call = mutated_mod.get_global_var('func_9149')
var_12193 = relay.var("var_12193", dtype = "uint16", shape = ())#candidate|12193|()|var|uint16
const_12194 = relay.const([-10,-1,-9,-9,4,-7,7,-4,-3,-9,-5,-9,9,5,4,8,-4,-2,8,1,3,4,5,4,7,4,8,9,1,-3,-7,-10,10,3,3,3,-3,-5,6,-6,-5,-7,4,-8,7,9,-2,8,-10,3,4,-9,-4,-5,6,-5,2,1,5,8,-3,-9,-5,-1,7,-8,10,10,-4,4,8,8,-1,-3,-10,-2,9,10,-10,1,-6,10,8,10,5,-9,-5,-3,8,7,-9,3,-2,-6,-5,-10,7,7,-10,-9,-2,7,7,-8,-8,-5,5,6,2,-2,8,7,1,-5,10,-5,-4,4,4,8,-6,-8,-4,10,6,-4,3,-4,-5,7,-2,-2,7,-10,5,-5,-3,-5,9,5,-7,-10,8,7,4,1,-6,-4,8,-8,-2,-5,7,-3,5,-10,7,-3,7,-10,-3,6,-5,-4,2,5,4,10,10,-8,3,7,9,7,-1,-4,10,-4,10,-6,-10,6,-1,-5,-4,-5,-10,-1,4,6,4,10,10,7,-1,-2,-1,5,9,-2,3,-3,4,4,9,5,-10,5,8,1,4,10,-4,-9,3,7,3,-10,4,-6,2,6,6,-1,5,6,5,-7,1,3,9,1,-2,8,-3,-6,-6,6,-6,-8,10,2,-2,-6,5,6,-1,-6,9,6,-6,6,7,-6,10,-5,10,6,8,-4,3,-9,-8,-7,6,-9,-8,-6,9,-9,6,1,-3,7,-1,6,-10,8,7,4,-9,-10,10,-3,8,9,-9,-1,9,6,8,4,5,5,-9,7,-4,6,-5,-4,-4,8,-3,-8,6,4,5,1,2,-4,-8,1,-10,-5,-8,7,-4,-5,-3,-1,6,2,-3,-5,-10,8,-2,10,-5,-6,-6,5,7,6,3,-10,3,4,6,3,-8,3,-9,3,-10,7,1,5,-1,9,-10,-5,-10,1,10,-1,-6,-8,9,-8,-10,4,-6,1,-10,1,1,5,9,-9,-3,-7,7,3,-7,-5,-6,2,6,9,-6,-7,10,-10,9,6,-2,-10,-8,-4,-4,6,6,1,-1,-9,1,-6,10,-10,3,-1,-8,-3,4,5,-6,7,9,5,8,-1,-10,10,10,8,-5,-10,2,3,-3,-3,9,1,7,2,-2,6,7,-3,-7,2,-2,7,8,-9,8,7,1,9,-8,7,3,1,9,-9,-6,10,-5,-1,7,-1,-1,2,10,2,-2,7,2,7,3,10,1,7,-5,9,8,6,-10,-9,-10,8,10,9,-5,-3,-6,-6,-3,3,1,1,-1,7,5,-4,9,-9,9,-2,8,-1,-10,-9,1,-2,-3,-2,-8,-8,8,-10,-7,-7,8,-1,7,-9,2,-2,2,-5,-7,-1,-7,7,-2,2,5,8,-3,8,-2,8,6,6,4,-3,10,5,3,-5,-1,6,8,-9,-2,10,-3,7,8,9,5,-4,-6,-2,-3,5,4,7,-7,5,-3,-3,-3,8,-2,-7,9,-1,10,-5,2,6,3,-10,-2,-8,-9,-3,-1,-6,-8,-1,-4,-1,8,9,5,-6,1,-9,-10,-7,-9,-3,-9,-3,-2,5,7,-2,3,-4,9,7,7,-2,-2,-8,-7,-1,-8,5,-9,7,6,2,5,8,-6,-3,-10,10,1,-4,6,5,2,-7,-10,-8,6,-6,5,-4,-8,4,1,3,-1,-10,-4,3,7,-6,6,3,-5,-2,10,9,-4,-7,6,-7,-7,-6,-4,-7,-10,-7,-9,8,-7,2,8,-9,-4,-7,8,-9,-3,-6,-3,9,7,8,4,8,6,-1,3,7,8,-10,-10,-1,-4,-1,1,-8,7,2,2,5,2,-4,-7,2,7,-10,-3,-1,10,-1,3,9,5,-1,3,-7,-3,-10,2,-6,6,-7,8,5,9,9,5,-3,-1,-7,4,1,-7,-10,5,-7,3,-1,1,1,9,-5,7,-5,4,-5,8,-6,7,3,1,4,-5,8,-10,-7,10,3,1,8,-2,4,6,-6,-5,4,10,-3,-2,2,-10,1,2,-7,-4,8,7,7,-1,6,-1,-3,8,-7,-7,-2,-9,-6,7,-3,8,6,-3,-9,-5,10,3,10,-9,2,7,2,-7,8,-4,6,4,9,6,-6,3,10,1,-9,-8,-6,-7,2,9,-9,-2,-6,10,8,3,8,9,-2,-9,-1,-2,-1,-7,2,-4,10,-9,-4,2,-4,7,-1,-1,7,3,-8,-6,3,-1,-3,7,2,-2,4,10,8,-1,4,-1,-3,-10,7,-9,3,-7,-6,-2,10,-5,-5,-4,2,2,-9,-8,7,-3,-6,-5,4,-5,-6,-1,10,-5,-10,-10,4,8,-6,6,-4,8,-1,1,4,-8,-3,-1,4,8,4,-6,-1,-2,5,-8,6,1,10,-7,-7,7,3,-5,-5,-2,-2,-9,-7,9,10,-10,-5,8,-10,10,-9,9,6,-10,6,1,-2,-8,3,8,-7,4,7,7,-6,-7,5,-8,8,3,-1,2,9,10,-9,7,-7,8,-4,3,4,-6,6,2,-3,-9,-3,8,3,4,-8,-8,4,9,2,10,4,7,-10,-5,7,-9,-7,2,5,-1,-9,-8,-6,-2,8,6,-6,1,5,-10,4,-3,-6,-2,-1,6,2,2,8,6,-6,10,-9,-9,-9,-7,6,-5,-2,-3,-7,-2,2,7,-8,8,7,-7,8,-1,4,-1,5,-3,2,10,7,-10,-6,9,-2,-1,4,7,3,-1,7,9,8,1,-2,-3,4,7,2,7,4,5,5,2,-2,-7,4,3,2,4,-6,2,-10,-2,-7,-6,-7,9,-3,-10,-3], dtype = "uint16")#candidate|12194|(1056,)|const|uint16
call_12192 = relay.TupleGetItem(func_9146_call(relay.reshape(var_12193.astype('uint16'), []), relay.reshape(const_12194.astype('uint16'), [8, 12, 11]), ), 0)
call_12195 = relay.TupleGetItem(func_9149_call(relay.reshape(var_12193.astype('uint16'), []), relay.reshape(const_12194.astype('uint16'), [8, 12, 11]), ), 0)
output = relay.Tuple([uop_12187,call_12192,var_12193,const_12194,])
output2 = relay.Tuple([uop_12187,call_12195,var_12193,const_12194,])
func_12214 = relay.Function([var_12186,var_12193,], output)
mod['func_12214'] = func_12214
mod = relay.transform.InferType()(mod)
mutated_mod['func_12214'] = func_12214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12214_call = mutated_mod.get_global_var('func_12214')
var_12216 = relay.var("var_12216", dtype = "float64", shape = (8, 8, 2))#candidate|12216|(8, 8, 2)|var|float64
var_12217 = relay.var("var_12217", dtype = "uint16", shape = ())#candidate|12217|()|var|uint16
call_12215 = func_12214_call(var_12216,var_12217,)
output = call_12215
func_12218 = relay.Function([var_12216,var_12217,], output)
mutated_mod['func_12218'] = func_12218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_12244 = relay.TupleGetItem(func_3274_call(), 0)
call_12245 = relay.TupleGetItem(func_3275_call(), 0)
output = call_12244
output2 = call_12245
func_12248 = relay.Function([], output)
mod['func_12248'] = func_12248
mod = relay.transform.InferType()(mod)
mutated_mod['func_12248'] = func_12248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12248_call = mutated_mod.get_global_var('func_12248')
call_12249 = func_12248_call()
output = call_12249
func_12250 = relay.Function([], output)
mutated_mod['func_12250'] = func_12250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5151_call = mod.get_global_var('func_5151')
func_5152_call = mutated_mod.get_global_var('func_5152')
call_12253 = relay.TupleGetItem(func_5151_call(), 0)
call_12254 = relay.TupleGetItem(func_5152_call(), 0)
output = call_12253
output2 = call_12254
func_12294 = relay.Function([], output)
mod['func_12294'] = func_12294
mod = relay.transform.InferType()(mod)
mutated_mod['func_12294'] = func_12294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12294_call = mutated_mod.get_global_var('func_12294')
call_12295 = func_12294_call()
output = call_12295
func_12296 = relay.Function([], output)
mutated_mod['func_12296'] = func_12296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5082_call = mod.get_global_var('func_5082')
func_5084_call = mutated_mod.get_global_var('func_5084')
call_12357 = func_5082_call()
call_12358 = func_5082_call()
output = call_12357
output2 = call_12358
func_12364 = relay.Function([], output)
mod['func_12364'] = func_12364
mod = relay.transform.InferType()(mod)
mutated_mod['func_12364'] = func_12364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12364_call = mutated_mod.get_global_var('func_12364')
call_12365 = func_12364_call()
output = call_12365
func_12366 = relay.Function([], output)
mutated_mod['func_12366'] = func_12366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10722_call = mod.get_global_var('func_10722')
func_10724_call = mutated_mod.get_global_var('func_10724')
call_12454 = relay.TupleGetItem(func_10722_call(), 0)
call_12455 = relay.TupleGetItem(func_10724_call(), 0)
func_10633_call = mod.get_global_var('func_10633')
func_10635_call = mutated_mod.get_global_var('func_10635')
call_12456 = relay.TupleGetItem(func_10633_call(), 0)
call_12457 = relay.TupleGetItem(func_10635_call(), 0)
output = relay.Tuple([call_12454,call_12456,])
output2 = relay.Tuple([call_12455,call_12457,])
func_12462 = relay.Function([], output)
mod['func_12462'] = func_12462
mod = relay.transform.InferType()(mod)
output = func_12462()
func_12463 = relay.Function([], output)
mutated_mod['func_12463'] = func_12463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9615_call = mod.get_global_var('func_9615')
func_9617_call = mutated_mod.get_global_var('func_9617')
call_12494 = relay.TupleGetItem(func_9615_call(), 0)
call_12495 = relay.TupleGetItem(func_9617_call(), 0)
output = relay.Tuple([call_12494,])
output2 = relay.Tuple([call_12495,])
func_12520 = relay.Function([], output)
mod['func_12520'] = func_12520
mod = relay.transform.InferType()(mod)
mutated_mod['func_12520'] = func_12520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12520_call = mutated_mod.get_global_var('func_12520')
call_12521 = func_12520_call()
output = call_12521
func_12522 = relay.Function([], output)
mutated_mod['func_12522'] = func_12522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5927_call = mod.get_global_var('func_5927')
func_5928_call = mutated_mod.get_global_var('func_5928')
call_12534 = relay.TupleGetItem(func_5927_call(), 0)
call_12535 = relay.TupleGetItem(func_5928_call(), 0)
output = call_12534
output2 = call_12535
func_12539 = relay.Function([], output)
mod['func_12539'] = func_12539
mod = relay.transform.InferType()(mod)
output = func_12539()
func_12540 = relay.Function([], output)
mutated_mod['func_12540'] = func_12540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10767_call = mod.get_global_var('func_10767')
func_10768_call = mutated_mod.get_global_var('func_10768')
call_12620 = relay.TupleGetItem(func_10767_call(), 0)
call_12621 = relay.TupleGetItem(func_10768_call(), 0)
output = relay.Tuple([call_12620,])
output2 = relay.Tuple([call_12621,])
func_12640 = relay.Function([], output)
mod['func_12640'] = func_12640
mod = relay.transform.InferType()(mod)
output = func_12640()
func_12641 = relay.Function([], output)
mutated_mod['func_12641'] = func_12641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9675_call = mod.get_global_var('func_9675')
func_9677_call = mutated_mod.get_global_var('func_9677')
call_12667 = func_9675_call()
call_12668 = func_9675_call()
func_12294_call = mod.get_global_var('func_12294')
func_12296_call = mutated_mod.get_global_var('func_12296')
call_12676 = func_12294_call()
call_12677 = func_12294_call()
func_8784_call = mod.get_global_var('func_8784')
func_8787_call = mutated_mod.get_global_var('func_8787')
var_12679 = relay.var("var_12679", dtype = "float64", shape = (462, 2))#candidate|12679|(462, 2)|var|float64
call_12678 = relay.TupleGetItem(func_8784_call(relay.reshape(var_12679.astype('float64'), [462, 2])), 1)
call_12680 = relay.TupleGetItem(func_8787_call(relay.reshape(var_12679.astype('float64'), [462, 2])), 1)
output = relay.Tuple([call_12667,call_12676,call_12678,var_12679,])
output2 = relay.Tuple([call_12668,call_12677,call_12680,var_12679,])
func_12686 = relay.Function([var_12679,], output)
mod['func_12686'] = func_12686
mod = relay.transform.InferType()(mod)
mutated_mod['func_12686'] = func_12686
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12687 = relay.var("var_12687", dtype = "float64", shape = (462, 2))#candidate|12687|(462, 2)|var|float64
func_12686_call = mutated_mod.get_global_var('func_12686')
call_12688 = func_12686_call(var_12687)
output = call_12688
func_12689 = relay.Function([var_12687], output)
mutated_mod['func_12689'] = func_12689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6309_call = mod.get_global_var('func_6309')
func_6310_call = mutated_mod.get_global_var('func_6310')
call_12709 = func_6309_call()
call_12710 = func_6309_call()
func_9747_call = mod.get_global_var('func_9747')
func_9750_call = mutated_mod.get_global_var('func_9750')
var_12720 = relay.var("var_12720", dtype = "float32", shape = (504,))#candidate|12720|(504,)|var|float32
call_12719 = relay.TupleGetItem(func_9747_call(relay.reshape(var_12720.astype('float32'), [12, 3, 14])), 0)
call_12721 = relay.TupleGetItem(func_9750_call(relay.reshape(var_12720.astype('float32'), [12, 3, 14])), 0)
output = relay.Tuple([call_12709,call_12719,var_12720,])
output2 = relay.Tuple([call_12710,call_12721,var_12720,])
func_12723 = relay.Function([var_12720,], output)
mod['func_12723'] = func_12723
mod = relay.transform.InferType()(mod)
mutated_mod['func_12723'] = func_12723
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12724 = relay.var("var_12724", dtype = "float32", shape = (504,))#candidate|12724|(504,)|var|float32
func_12723_call = mutated_mod.get_global_var('func_12723')
call_12725 = func_12723_call(var_12724)
output = call_12725
func_12726 = relay.Function([var_12724], output)
mutated_mod['func_12726'] = func_12726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11861_call = mod.get_global_var('func_11861')
func_11862_call = mutated_mod.get_global_var('func_11862')
call_12765 = relay.TupleGetItem(func_11861_call(), 2)
call_12766 = relay.TupleGetItem(func_11862_call(), 2)
func_4162_call = mod.get_global_var('func_4162')
func_4163_call = mutated_mod.get_global_var('func_4163')
call_12769 = relay.TupleGetItem(func_4162_call(), 0)
call_12770 = relay.TupleGetItem(func_4163_call(), 0)
output = relay.Tuple([call_12765,call_12769,])
output2 = relay.Tuple([call_12766,call_12770,])
func_12771 = relay.Function([], output)
mod['func_12771'] = func_12771
mod = relay.transform.InferType()(mod)
mutated_mod['func_12771'] = func_12771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12771_call = mutated_mod.get_global_var('func_12771')
call_12772 = func_12771_call()
output = call_12772
func_12773 = relay.Function([], output)
mutated_mod['func_12773'] = func_12773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8565_call = mod.get_global_var('func_8565')
func_8567_call = mutated_mod.get_global_var('func_8567')
call_12838 = func_8565_call()
call_12839 = func_8565_call()
output = relay.Tuple([call_12838,])
output2 = relay.Tuple([call_12839,])
func_12850 = relay.Function([], output)
mod['func_12850'] = func_12850
mod = relay.transform.InferType()(mod)
output = func_12850()
func_12851 = relay.Function([], output)
mutated_mod['func_12851'] = func_12851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8816_call = mod.get_global_var('func_8816')
func_8818_call = mutated_mod.get_global_var('func_8818')
call_12865 = relay.TupleGetItem(func_8816_call(), 0)
call_12866 = relay.TupleGetItem(func_8818_call(), 0)
func_3573_call = mod.get_global_var('func_3573')
func_3575_call = mutated_mod.get_global_var('func_3575')
var_12871 = relay.var("var_12871", dtype = "float64", shape = (924,))#candidate|12871|(924,)|var|float64
call_12870 = relay.TupleGetItem(func_3573_call(relay.reshape(var_12871.astype('float64'), [924,])), 1)
call_12872 = relay.TupleGetItem(func_3575_call(relay.reshape(var_12871.astype('float64'), [924,])), 1)
uop_12876 = relay.atanh(call_12870.astype('float32')) # shape=(14, 11, 6)
uop_12878 = relay.atanh(call_12872.astype('float32')) # shape=(14, 11, 6)
func_6838_call = mod.get_global_var('func_6838')
func_6840_call = mutated_mod.get_global_var('func_6840')
call_12892 = relay.TupleGetItem(func_6838_call(), 0)
call_12893 = relay.TupleGetItem(func_6840_call(), 0)
const_12895 = relay.const([[[-6.236278,-5.159764,3.839339,4.702287,1.669530,-9.261617],[-6.767543,0.430364,5.672172,6.584375,6.817255,-2.977764],[5.798016,-8.139563,0.045275,4.313166,9.953101,1.435457],[-4.652566,-7.010887,9.523896,8.533545,-1.921693,3.003139],[1.834871,-3.340420,7.393895,-9.973351,-3.302405,2.032940],[-4.879199,1.314467,-8.340887,-7.082384,0.224491,3.239738],[-3.474576,4.884689,3.667969,-5.901741,2.406815,2.360406],[5.665708,4.972125,-6.239931,3.289055,-2.545433,-2.892496],[6.493968,3.763808,-4.782843,4.200450,4.355232,7.123990],[-1.026006,1.058444,-0.634624,-2.817371,-6.591266,5.869850],[-1.097860,-8.440201,-9.388248,9.179849,2.146056,-5.002408]],[[5.490082,-7.117010,-9.596583,6.414792,8.711640,8.330946],[8.101803,-8.617554,1.479560,-9.119689,-0.089124,-0.410937],[-6.295166,6.569566,4.367891,0.467906,7.565676,3.108758],[1.406228,-9.718527,-3.413712,-6.459874,0.188262,2.197054],[-9.025298,-7.129830,-3.413883,0.958163,8.072216,1.223448],[8.350128,5.044405,-6.460599,-6.516537,-5.365611,6.517441],[-9.030853,-6.351882,-8.544356,1.891848,-7.253560,6.015860],[-9.224640,0.722346,6.961874,-5.145713,8.771277,-4.420992],[8.181729,5.981452,5.370810,-3.210676,-1.534230,-7.654342],[-3.926748,2.475932,4.029869,-3.610486,-4.982375,1.673485],[-1.309653,-3.052041,-3.099809,9.278372,8.598571,0.048649]],[[0.918834,7.579865,-8.381877,-9.925833,1.880742,2.545652],[6.365111,-4.324244,0.223886,2.390066,-7.932676,8.055940],[-2.138107,-5.140515,7.066431,6.066542,0.972545,-7.320494],[-2.047370,-9.963449,1.131610,-7.928310,7.774283,-0.380926],[1.628453,-6.880297,4.676973,-7.148853,3.240067,0.401178],[-5.956074,6.313713,2.222165,2.286880,8.376385,8.751984],[-4.217451,9.227082,5.967898,-7.803103,6.957139,-9.484223],[7.982114,4.720173,8.794945,0.047471,8.535889,7.676657],[4.233844,-8.815922,-7.763512,5.204130,8.915652,8.925604],[-4.961642,2.418416,-5.798657,-1.153274,-0.986056,-6.102043],[-9.220880,5.412210,0.746269,4.024057,-8.541861,8.101029]],[[8.752503,3.086940,0.600188,8.204594,-8.084653,5.695740],[-6.819703,-1.915700,2.853131,-4.083411,6.720017,2.943903],[-0.938351,2.771258,-1.860506,-2.474200,4.204810,0.733785],[-9.883639,-1.656011,5.889398,9.835106,7.021218,1.867729],[2.656017,-0.218110,6.644425,5.674074,-3.604472,-1.873772],[5.517746,6.717293,-7.987757,8.982702,7.150617,-1.630342],[4.666215,9.479764,2.431869,-7.475976,-9.565979,9.386999],[-4.455483,-6.048087,0.840721,-1.193231,4.453221,4.170936],[-0.864976,-7.210466,-3.238374,-0.596911,-7.854613,-1.836645],[-5.936923,-9.060251,-7.155218,5.994060,-6.270984,9.227855],[-5.532289,-1.942136,9.070301,-0.099470,-1.358186,-5.716687]],[[5.300006,9.388734,-0.199152,4.573608,-7.856053,1.091299],[-2.900466,7.490761,-2.412679,-1.575194,-0.331551,-3.251799],[9.016655,2.345931,8.033703,-0.876477,4.051094,2.629000],[-4.026842,-1.822763,-6.305152,3.913591,-5.249961,-9.048837],[0.830539,-4.601901,5.000681,-9.191659,5.906933,1.145387],[3.160071,0.508734,7.041822,-6.052135,5.142479,-7.474066],[-0.040099,-3.033430,-2.199209,-3.244773,-1.612821,-0.338163],[2.071056,-8.450116,-9.070846,-3.415440,9.392146,-7.396947],[-1.938041,-2.781043,-5.799774,0.622642,-6.444451,6.483596],[-3.922115,9.736632,-5.949683,9.265278,-4.888003,-5.454593],[2.012041,-9.240396,-5.261542,3.954429,2.584464,4.430083]],[[-9.097951,-9.259288,-5.862756,7.485432,8.826654,9.979105],[-2.558286,-5.161813,-0.692972,-9.188519,3.227706,7.035295],[4.191997,-1.466252,-6.536069,-8.760352,-9.609805,-5.281281],[9.189718,-7.080387,-5.074486,-4.781377,-2.197383,5.410781],[-7.718229,-4.600607,-9.998479,6.071838,-9.263041,-2.154562],[1.809612,0.056329,4.397312,7.001963,0.663334,-3.841613],[1.256467,9.418746,1.845670,5.514603,-3.728638,5.592899],[4.773944,-3.708077,-9.798766,-4.981841,-7.336553,6.110894],[8.018559,-5.993895,-0.127839,-4.666556,0.650515,4.726666],[-9.755329,-6.935181,-2.591879,6.343376,6.810598,9.142217],[-6.161279,8.093180,5.764096,7.918112,2.336117,-1.442668]],[[-1.612125,-8.379041,-9.067333,-1.144191,-2.683433,2.524552],[-0.954605,-9.709623,-2.689225,2.943024,5.305826,7.859307],[5.705687,-0.998619,-9.213236,8.703048,3.517138,7.471792],[4.401755,3.165018,-0.597820,1.201513,1.763022,-0.740817],[1.772892,9.112407,5.711371,-0.187948,1.923810,4.865082],[1.926071,-2.490410,-2.003865,-5.238270,2.719678,7.903041],[-5.358410,-2.772444,-1.798801,8.654459,-4.133736,5.787830],[-7.031950,-8.229480,-0.040366,0.288302,-4.829976,-5.361176],[4.079078,9.553453,-2.203629,4.531173,2.418954,7.485660],[-8.077691,5.313093,1.099647,-9.034559,-9.459660,1.066229],[9.174042,-0.841479,-8.712991,-1.799107,7.592668,-8.300022]],[[6.050760,-0.910455,6.828223,-9.630416,3.110136,-4.634070],[-3.963514,-4.168550,4.159515,5.991814,-7.358835,9.196729],[7.468550,7.115717,6.951439,-0.680729,5.960549,9.438754],[-5.358541,-1.120828,4.264663,-9.051936,-3.082061,4.620220],[-3.681363,-1.852988,-1.605108,3.206908,7.517357,5.691824],[-3.834714,8.674722,-4.392686,-7.764936,4.699149,-6.049026],[2.234981,-7.304123,6.497296,-5.830766,5.673808,2.254989],[-0.283054,6.099067,9.629335,-6.531474,-1.543647,2.839529],[-5.578056,-4.010557,-6.104420,-7.990556,0.901700,0.398345],[-6.964045,8.553536,-9.894758,-0.572431,4.618897,9.247274],[-7.160525,4.482883,7.379233,8.435514,-6.875425,8.859621]],[[8.972816,8.270990,0.690922,1.284976,-4.510922,0.249384],[4.867134,8.142475,1.726999,3.478436,-8.911265,-6.788780],[2.562594,3.703211,9.010335,7.450836,-0.428986,-2.728087],[8.874220,-0.370777,-6.908214,9.607939,5.255372,-0.269370],[6.542051,-8.744790,-9.212508,7.673018,-1.524506,-1.840258],[-0.605646,-1.623700,-3.725661,-3.404165,1.227193,1.821254],[-0.187556,3.031624,0.695136,-3.858890,-6.122970,-7.406534],[5.956441,-2.799954,-4.233212,-9.800788,-4.275380,9.569241],[8.773828,4.151052,-8.272409,-0.725417,7.058045,-2.719677],[6.820477,8.178173,2.622778,1.846924,8.843182,6.679964],[-2.097681,-3.712447,-1.048852,3.022750,5.508640,-8.824566]],[[7.547104,-1.485160,2.157587,9.890350,0.496223,-0.584071],[-7.803450,-3.913899,0.801589,3.061077,8.183624,1.099363],[1.207965,1.388628,8.226438,6.779989,-5.939025,1.715377],[-0.007422,-4.212397,2.159057,4.271977,-1.371017,9.005079],[7.169610,1.175100,8.444003,-8.577688,8.909122,9.131223],[-5.454716,9.904700,1.835025,-3.024055,0.763747,0.134163],[0.517401,-5.240073,-6.293423,6.219253,-8.190149,-2.689898],[4.288064,7.842398,-6.458408,3.540213,9.387344,0.228537],[8.795217,-1.916625,8.290603,6.803291,-2.168276,-1.470544],[-9.346311,-0.152904,4.748026,-5.070648,-5.675025,5.034138],[-2.550094,6.718742,-8.754219,-6.381312,-8.821755,-6.002243]],[[9.566578,-3.698061,-3.714107,-8.427724,-8.976201,0.196130],[-5.203930,5.689204,2.454700,1.945775,1.027916,4.009354],[-2.888941,-8.758513,6.956561,-5.822382,-3.983682,-0.548718],[0.125306,2.671821,-7.102516,7.277592,-0.743141,9.092366],[-4.587661,-1.366861,4.961091,4.651527,1.410953,-5.316717],[-4.259328,0.112521,1.188192,3.057052,8.688586,-7.799139],[-2.278496,-1.629026,-0.220203,-8.137251,-1.867904,8.253658],[4.574750,8.561037,-1.330381,4.877429,-5.964852,6.955431],[-9.420277,6.292333,-2.305331,9.710494,1.098234,0.381871],[6.253282,-4.433718,-0.042010,3.619543,-9.980805,1.149712],[-9.673830,-1.787078,4.054380,-5.672774,-7.129144,9.715673]],[[-3.392015,1.047957,-9.994207,0.622378,1.738581,-6.118789],[6.420603,9.459769,-6.627641,-3.717197,4.460058,-9.041262],[5.035579,-2.899017,-2.772184,-9.358677,8.815457,-3.073818],[-5.372734,7.570110,-2.524370,-4.861081,-7.148957,9.899979],[-4.396608,6.090638,-2.873581,-1.019106,3.787803,-1.664298],[9.033943,-5.605754,-8.477673,-0.442858,-0.846142,-3.634366],[7.125297,3.695823,-2.594948,0.948479,-1.136727,-4.177645],[-7.875889,-3.571612,-9.697847,0.700164,3.293375,-6.159107],[-2.838108,9.989662,-5.870020,2.312269,-7.987776,8.051697],[-3.338407,0.398366,-1.113533,3.378059,-6.260377,-2.531919],[-9.131362,-7.798944,2.673873,-3.803705,-2.953042,-7.226304]],[[0.726368,-7.779717,-8.077757,4.350377,-8.000412,-7.616564],[-3.329084,7.796659,5.813912,3.789456,7.558614,-6.057412],[-3.125982,8.968227,-6.130867,-9.004842,9.327774,9.510807],[-4.142623,-4.429681,0.992755,3.298855,6.567904,-0.415773],[-6.756384,-6.310911,-6.771949,-8.546067,4.676743,5.287159],[-8.478788,-5.556724,-3.476757,3.350781,-4.579664,-7.552139],[-2.552858,4.088666,-3.909521,7.693956,-1.536453,0.932899],[-6.687090,1.370166,6.739791,7.356302,-5.288106,1.877084],[4.880798,-8.158688,2.217657,2.507176,-8.990487,4.614816],[-2.723316,-8.937955,-5.403594,5.017892,3.313963,9.698232],[1.806859,-5.485150,-6.123808,1.906203,8.046828,1.080311]],[[-6.734545,-7.704673,6.339501,6.880041,-4.457273,-8.305933],[8.866155,3.657196,5.881134,6.384897,1.828838,-8.036988],[-7.843944,2.456228,5.549083,-7.381034,9.457997,7.947033],[-2.884733,5.919881,-1.032933,4.458742,4.753672,-7.966195],[9.762974,-1.654413,-5.643626,-0.374738,-4.578033,-7.086299],[-3.930881,1.307814,5.688836,6.539344,7.219478,7.095502],[-0.538201,-6.635172,9.419301,-8.717173,-8.722714,-2.399744],[-9.280910,3.540317,-9.517719,-8.781320,-6.321456,8.602900],[-2.283948,7.520903,9.199255,0.008970,-8.193878,7.595146],[8.566063,-6.055693,-7.604008,-7.100396,-0.918896,0.580620],[0.849622,3.361476,6.396836,7.140647,3.322825,-5.882308]]], dtype = "float32")#candidate|12895|(14, 11, 6)|const|float32
bop_12896 = relay.power(uop_12876.astype('float32'), relay.reshape(const_12895.astype('float32'), relay.shape_of(uop_12876))) # shape=(14, 11, 6)
bop_12899 = relay.power(uop_12878.astype('float32'), relay.reshape(const_12895.astype('float32'), relay.shape_of(uop_12878))) # shape=(14, 11, 6)
output = relay.Tuple([call_12865,var_12871,call_12892,bop_12896,])
output2 = relay.Tuple([call_12866,var_12871,call_12893,bop_12899,])
func_12931 = relay.Function([var_12871,], output)
mod['func_12931'] = func_12931
mod = relay.transform.InferType()(mod)
mutated_mod['func_12931'] = func_12931
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12932 = relay.var("var_12932", dtype = "float64", shape = (924,))#candidate|12932|(924,)|var|float64
func_12931_call = mutated_mod.get_global_var('func_12931')
call_12933 = func_12931_call(var_12932)
output = call_12933
func_12934 = relay.Function([var_12932], output)
mutated_mod['func_12934'] = func_12934
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12939 = relay.const([[[-3.287401,-0.444621,-6.970482,6.088679,-5.434754,8.785175,9.364030,-8.912032,1.644989,5.460238,-4.928552,-1.648758,-5.660717,-5.311571,-7.425752],[2.328704,0.905304,3.200474,-9.082281,5.671354,1.526281,5.863836,6.538547,3.894794,-8.731846,9.391050,-9.640676,-5.986682,8.813747,1.496367],[6.990704,-2.149910,-5.470801,-8.940903,-9.755809,3.326074,-3.020428,-9.728795,-7.666208,-7.174209,-1.501657,-8.258496,-4.373749,9.455860,2.301029],[6.639477,1.727356,7.168557,8.092252,6.531346,-9.226309,7.074892,4.926401,-4.213692,4.748130,1.616137,-9.263184,6.296078,-7.704676,-0.549068],[9.879106,-6.177790,1.015261,-5.251513,2.268305,-6.556595,0.144158,1.808825,3.543806,-2.281697,-4.658798,-1.600103,8.757283,1.852084,-1.582159],[5.850049,4.945100,-0.671904,-1.891333,-0.149169,-1.245232,0.201821,-6.182207,6.767694,-5.311830,9.655268,6.949466,8.440327,5.081919,-5.614080],[-6.235476,0.370622,-4.179340,-6.026910,-2.138740,-2.917230,8.085453,-4.711309,-6.082072,0.603649,-7.932834,-0.624358,-6.465642,-6.549001,-1.428028],[2.642078,2.286582,2.246261,-7.784547,-3.142042,-3.511076,-3.343844,-2.463510,0.787563,-9.302302,4.612774,5.756963,-9.121096,0.917388,6.084303],[6.437512,-0.244767,3.267755,-1.847652,7.905383,8.968220,-1.417606,3.512723,-5.465001,0.922074,0.033380,3.190091,-5.402909,-9.091041,1.886293],[-0.026012,-9.357653,5.757807,-0.744426,1.425967,-3.555969,4.788096,-5.823552,3.207346,4.186131,8.977253,5.255864,-2.823739,-3.724405,8.568857],[-0.748636,5.038589,-0.948710,8.104921,-7.464276,-5.808943,3.456532,1.859818,-1.454637,-1.103107,-8.953087,-3.595753,9.769477,1.579182,7.646187],[0.880767,-1.784853,-2.815478,5.776349,7.602495,-5.426168,-6.552522,9.230686,-8.324202,-8.866235,-5.149061,-6.272598,-3.507918,1.335190,-5.819268],[-9.663806,-5.767118,-6.331519,9.351964,-7.119668,8.200472,-8.058096,-6.745905,-9.083641,7.434262,-1.276710,7.047250,-5.323171,-0.978556,1.006866],[-4.540108,-8.170777,2.851984,7.994188,-8.804977,5.534294,-1.845272,9.410886,-5.241098,2.427963,-0.383322,7.713987,0.646949,3.271227,2.216465],[-4.640357,-9.725441,-2.467992,2.128999,-2.822860,-3.956330,5.726456,2.829121,3.777846,-6.812274,0.248274,-1.184627,-7.624694,-3.334827,2.178736]],[[7.110670,6.205675,-1.050564,8.140839,1.983979,3.083016,0.904561,-1.327369,8.092432,-8.100600,0.443956,-3.946234,-4.754412,3.658230,-9.961873],[-9.367412,-4.418480,0.265981,-2.782503,-6.126111,-9.309923,1.324243,-2.124759,-8.217431,1.464110,-3.751453,-5.595377,4.050741,6.793957,9.566344],[4.189068,2.090662,0.628278,7.783243,0.235829,4.507461,1.076884,-4.766214,6.403096,-6.048443,5.085183,5.190947,6.574865,4.083291,5.985827],[2.956553,-8.366807,-9.061520,8.675395,4.548268,0.537869,8.582212,8.644858,-1.430312,-1.490417,-6.583362,9.595954,-2.764979,-2.445965,-0.728598],[-2.483402,-0.574596,-5.309568,9.669624,-9.009789,0.622871,1.320985,5.448138,-5.656766,0.967335,-0.105652,-2.184581,1.439927,-4.681033,-3.786761],[8.155466,-8.524720,-3.718870,-5.506503,9.388119,-5.612334,-1.012434,0.842657,1.830340,-4.016121,-4.764940,-3.867569,-6.676511,7.870842,6.444431],[8.057729,8.812706,-0.171892,6.447638,7.968476,-9.985714,3.701281,1.517297,-3.390599,-2.315911,-2.149114,1.548485,0.898483,-1.322728,-6.074001],[3.879938,7.658130,-9.195918,-7.146234,-3.810821,-8.569076,8.907625,-0.832197,-2.847731,8.539786,6.225033,9.630123,-7.741919,-3.416955,-2.217523],[-6.077798,1.660431,-2.582179,-1.727621,8.442735,-8.190013,9.318687,0.806994,-1.421626,-1.284969,-7.833071,9.046154,-5.215834,-8.100508,0.550910],[8.247778,-8.560587,2.426564,-7.645985,0.802107,-8.147674,3.643214,-6.789701,9.850481,-3.382280,-2.466390,9.530541,6.112438,-5.078491,7.380626],[-5.616199,0.565722,9.735435,6.810957,-5.810251,5.997481,-8.114369,-6.139757,9.121659,6.638365,0.741937,-6.977841,-3.678938,-2.402381,9.729313],[-9.771929,4.764502,0.586607,-5.990423,-8.025939,5.016847,8.203075,5.785190,-0.244600,-6.193867,-2.842461,-6.203754,-2.770669,-3.737802,4.442269],[-6.936795,5.215898,9.229341,-2.449114,7.042151,4.323374,-0.414964,-8.345053,-9.455564,-2.411388,8.655088,0.920701,0.743422,-2.182963,-6.378582],[-4.248419,0.156698,-6.715360,-6.297142,-3.767561,-3.948047,-2.571581,-8.891299,-4.148662,-4.751681,9.534948,3.123772,7.156959,2.439523,8.924120],[2.894663,-7.603046,4.700905,4.513749,-9.607482,-7.335103,6.063149,4.384291,7.834388,3.400810,1.181112,7.801229,6.750272,5.476727,-5.246334]],[[-2.535199,-6.722991,-0.578599,-2.838616,4.474109,7.692736,5.301338,2.515206,8.800022,-0.899189,-4.835332,4.966290,-8.415588,-7.851841,5.813846],[-5.143493,-5.535170,5.586248,7.609510,-0.113950,-8.470305,-9.825130,2.016623,-8.674184,-8.088382,4.064888,-8.035462,7.123972,5.469182,2.818235],[-8.500827,-6.636567,-0.940905,-5.516669,7.595779,4.190430,-4.196545,6.746224,9.237357,-6.448603,-8.719987,-1.111456,6.307038,-2.306367,8.088546],[0.719992,7.612146,-0.764151,7.897304,3.322486,7.108348,-6.059882,-1.938827,9.899658,-7.851775,-8.450362,1.462671,2.707817,-9.023424,9.795555],[9.234627,7.505313,4.890020,2.010927,-6.352033,6.125259,7.449739,-5.390532,-0.755613,4.686647,6.236300,5.693002,-0.724626,9.098241,-1.015061],[-8.332877,-5.395961,5.959096,0.439905,-8.378103,8.044873,3.989630,-8.982146,9.949883,-4.939229,8.604060,-9.509520,-7.772103,8.982779,0.171940],[5.068929,-2.025259,8.027783,5.012214,-1.875627,5.259037,8.804496,-0.551125,-8.630628,-8.897569,-7.387540,-1.097752,3.393784,8.577593,9.186940],[-9.456651,-7.463734,-6.987278,-6.492095,-9.098145,6.362639,5.863364,-9.764039,-8.168987,7.312632,5.999313,-9.213192,-8.977538,4.780655,4.087494],[-2.229776,7.353395,-8.276905,-6.267647,7.103314,8.415262,-0.857293,4.417721,-1.266591,6.677409,3.387794,7.637587,1.781942,0.831627,4.177381],[6.280523,-3.596548,-0.831908,-1.945587,-2.534577,7.433443,-4.968732,-1.311848,-7.384626,-5.571571,-1.453142,0.233501,9.555523,3.074363,3.029069],[2.731687,-8.025421,4.050846,-5.910140,0.424181,1.274679,-9.452326,0.815138,1.664571,2.994787,9.425012,0.574445,9.929250,4.915372,8.353777],[9.057578,4.018659,7.727754,-5.655220,-9.561531,-6.292079,-7.060396,-7.679169,4.730475,-6.558316,9.051386,-2.580474,-5.429942,7.907606,-5.250238],[-7.562017,-7.226934,7.500006,-7.605745,1.828319,9.443975,-7.331734,2.535269,2.698382,-6.208038,5.096631,-2.095282,1.374604,-1.846905,-5.786437],[0.372726,-0.648345,4.985940,4.026221,-8.131882,-6.589966,-1.868466,7.358822,1.525746,-1.659368,-4.843661,7.052009,1.010419,3.039822,-5.985213],[-6.342098,-8.537773,8.196239,-8.283640,9.993232,0.294767,4.293062,-6.078969,0.929305,2.287364,-0.895733,-4.603109,-5.366477,-1.836406,8.022562]],[[-4.960340,-6.932875,-3.478239,-2.001587,5.152136,9.454778,3.932183,-0.195051,-1.614163,-3.860420,-9.517149,3.745495,-2.364936,-0.919084,-4.998660],[7.215777,-9.387877,3.093233,0.597554,5.833032,-8.241091,-7.115031,7.500705,4.457660,-9.038204,-5.150658,-1.197210,9.343022,9.854207,2.084501],[2.847310,-4.550692,2.940272,0.724298,8.324235,4.307175,2.718507,-2.177274,-0.266060,-6.107126,9.357248,5.905003,0.175420,-8.677340,5.226122],[-3.324946,5.159421,-0.703929,-4.290057,2.290060,-8.070699,6.547642,-2.573599,3.079459,-6.819777,-2.423165,-5.862909,1.576841,-7.917122,-2.112338],[-1.912633,1.038885,-0.510020,-4.481873,6.784632,-9.600143,-0.715249,4.608342,4.667649,3.588724,1.758338,8.485953,-7.029996,4.006131,7.039952],[-9.844222,-4.638016,8.506078,5.099972,7.786249,0.241363,-3.469662,-2.100040,1.481920,-2.417965,2.329550,-6.066309,0.812195,5.127453,1.626507],[8.144329,-0.376276,0.871346,-0.239528,2.294765,1.793377,4.836413,-8.884777,-2.764923,-9.013953,1.862749,-4.433717,-1.407310,-4.008837,-3.857410],[-1.392615,3.397179,0.496969,-7.701242,3.423625,0.537923,0.443280,-8.939574,-2.863798,2.273989,-2.062644,-8.162872,-0.914728,-0.294238,2.840312],[-9.900296,-7.829725,-9.509517,1.627942,5.216277,2.682420,9.451715,-0.852832,-8.417518,-7.859218,4.344411,-1.696905,2.481577,-0.750040,7.529529],[-4.612102,-8.764327,3.505339,-8.425037,5.675886,4.883200,2.446227,4.251270,0.861013,-9.439120,6.856987,-3.604016,-5.215573,-0.040077,4.125334],[-3.172182,-2.642905,7.743063,4.015079,-2.268942,0.055029,1.664745,-1.302662,-2.272361,4.839016,-3.111455,-7.782903,-1.432714,-1.393629,-1.848788],[6.261926,-8.367928,0.015699,1.300292,8.123428,6.664120,-8.344931,7.882747,-4.670027,-3.327168,4.964788,-2.167479,9.236664,-2.543823,-1.900710],[5.593759,4.911995,9.224711,8.771475,8.442927,-1.630225,-3.704214,-9.761597,3.065676,0.695869,-2.581690,-4.846875,9.683545,4.677238,-4.682679],[-6.342327,8.575685,1.389451,-5.792646,-6.534840,0.273953,-5.180796,1.237294,-2.380368,7.855547,-8.762982,-6.242115,1.103391,-8.766153,0.447835],[-1.850202,-9.520558,8.072576,-0.624144,8.940494,8.314246,2.563611,-2.705978,-8.910891,3.057721,-3.266934,3.435019,3.225190,-2.121376,-5.290112]],[[-9.662695,4.290923,-5.884593,-4.861518,-6.888940,1.035345,-4.518779,-3.015622,9.622058,1.101714,-8.240860,-2.445074,-4.714089,-3.263882,2.204119],[-5.322419,7.963962,7.613589,-0.905412,-2.635399,2.373158,4.105188,-7.248790,-7.894706,-0.018936,6.394353,3.439193,7.328089,5.295665,2.303143],[-3.407749,-0.953550,0.696845,7.876127,7.495843,2.668209,-1.123430,-5.030135,-3.266287,-5.161383,5.582553,7.908306,-8.451262,-2.528985,5.609955],[-9.558362,-4.439113,8.922238,-3.258795,0.417791,9.175672,-8.758013,7.716790,-7.302379,0.948225,2.110095,-6.645909,-7.043195,5.275496,-7.911389],[-9.562762,-5.214469,6.894419,-1.074962,-7.878030,8.370008,-5.018713,2.226499,9.164760,7.914639,7.071627,6.258479,-5.841749,-2.150671,-3.502108],[-7.841236,1.878770,7.634062,-8.653442,5.906191,-0.806766,-4.504749,-8.753368,-2.821358,-5.265364,9.540667,-6.442950,8.928322,-3.594089,-6.101599],[6.962874,3.596671,3.319585,8.991853,-4.383801,2.401451,-1.284443,-2.133224,0.962685,-1.356149,-7.631411,4.629140,-2.767661,8.884845,-9.287021],[0.907806,-4.426249,6.083960,-7.556487,-5.711423,6.230552,5.101260,4.481978,-4.548209,-2.711168,-5.561799,-6.655738,-6.679407,8.595606,5.753504],[7.319528,7.702495,8.449245,-1.175961,6.597384,1.524773,-3.354013,-0.767702,-9.942219,-2.208309,4.619469,9.004522,1.125046,-0.503845,-8.954198],[-7.536567,5.524417,8.471924,-1.381417,-4.414521,-6.849537,-9.551217,-4.664293,5.445660,-5.684385,3.107434,-6.792847,7.258442,-1.422468,-1.926700],[-6.788392,6.529655,-6.988241,-1.817960,-1.245235,7.247067,-3.640431,2.684550,-6.893505,0.686292,-9.139024,2.491995,-9.131409,-7.867438,-4.121672],[2.052519,-8.035498,-0.601664,8.286788,0.292413,2.489597,4.752260,4.495472,-6.949756,0.981392,-2.896857,2.653200,-2.862011,-5.246214,-2.814591],[-9.948745,6.854132,-3.528288,8.609427,5.549185,8.355512,6.620657,-3.023950,2.947543,6.916865,0.896490,1.485595,6.835416,-6.273300,-5.955435],[-5.356615,-5.494910,8.766909,-2.639344,-2.703175,-0.788434,-9.323344,-3.304692,-7.307351,-8.491989,-7.799016,4.453540,-4.898926,-3.596395,-9.240805],[0.876549,5.741784,6.299917,7.688809,0.055983,0.549981,8.834895,-6.051897,-6.637031,-6.123179,-2.633466,-9.389337,-3.816873,-3.360718,6.775553]],[[4.907643,2.803203,-5.997551,-1.960510,-0.513846,-1.332412,5.364593,-5.978633,2.133333,-2.125377,2.377198,3.768200,-7.439519,-0.434626,-5.537986],[3.358789,-7.748805,-2.941732,5.120118,-7.676469,-2.268452,7.007233,0.685664,4.130105,2.659984,-9.014072,-2.830248,-5.473622,7.816950,1.306970],[2.362764,7.141341,-0.424805,-6.815018,-0.360204,9.272124,4.466870,-6.534043,-9.787138,-5.116422,6.038711,-0.071546,-0.260485,-5.328743,4.633246],[7.038905,1.460321,2.244492,-1.639207,0.554580,-3.732932,5.372629,-1.926258,-9.592669,-5.192259,-7.203057,5.473371,4.732697,2.972567,6.364670],[-1.370730,1.773820,-5.857672,3.265458,1.746357,5.464350,0.444284,8.336527,6.666108,4.336961,-2.674526,3.614023,-7.606504,6.331168,6.030975],[3.961438,2.948583,0.268974,4.807065,-5.777337,6.279030,-1.721892,9.213231,-0.199886,-3.437469,-9.490301,6.442514,-6.502505,-9.795766,-4.087954],[9.245439,7.581370,-0.388144,-9.374670,7.178031,-7.226824,-3.435806,-0.631815,6.173847,-5.559320,-0.796511,-3.281734,1.420105,8.062276,9.242201],[0.996349,2.824370,3.352160,9.777313,7.751210,8.815861,2.394676,3.084039,4.721517,0.715419,-6.642938,-7.474838,5.611681,5.415676,3.398424],[-6.047966,1.518910,-1.331936,-2.889093,-1.202980,-2.486432,1.496658,-7.101645,4.456846,3.873414,3.575148,-1.785938,7.214622,0.599924,8.346446],[8.664974,5.775318,9.700707,6.755592,0.750896,-8.174161,7.759471,-6.320091,-2.401981,4.835544,-1.495704,4.081984,-3.615030,-2.824714,3.075314],[0.764976,-9.420373,-8.384155,-6.770410,3.761475,5.874480,1.359034,1.501007,-7.169767,-9.717257,-0.513244,3.185358,2.619483,-5.473451,3.380759],[6.952534,-9.464163,-8.158768,-7.017664,-1.776866,-2.795017,8.945008,2.119551,6.036551,-0.637545,3.549151,-0.522521,-3.523500,7.747816,-9.075730],[-2.337744,9.255247,0.899548,4.256798,-4.876310,2.180619,-5.805036,-4.761694,7.787970,2.861642,4.672378,-5.397047,6.780261,-8.725173,0.649034],[-1.790723,-2.081212,-7.696996,8.289150,7.727962,-9.353475,-4.790867,0.865832,-9.523915,0.165919,-8.578622,-3.574692,-2.921395,5.793622,-2.622120],[1.044151,6.287581,-0.963479,7.486073,6.931197,0.202089,3.098848,-3.705075,4.155839,-1.088076,8.432726,9.761632,4.868157,7.679559,-2.055961]],[[-5.645027,-6.018771,-9.819723,2.426864,-2.276955,-0.314059,-1.699224,-9.868540,5.955285,9.650190,-9.937535,-1.668747,9.777409,8.142071,7.005865],[-9.139579,-8.699864,7.911388,-1.220900,-6.798519,5.251227,-5.473390,0.056119,9.552821,-1.972612,-2.946515,2.105825,6.265445,-2.147685,0.436206],[-5.098928,5.557688,1.330151,8.304962,-1.831765,-4.061992,5.796035,0.745002,6.789373,6.732107,-0.842916,-2.096123,-9.596525,-3.029657,1.815017],[-3.775426,4.870660,-6.394756,-2.167895,-5.236983,7.913852,8.525254,-1.298748,2.738870,0.220193,6.885026,-8.986742,2.802451,3.496604,-9.758200],[4.746568,0.091981,-5.406076,6.373514,2.556760,1.028259,1.782457,1.371748,-1.075173,7.368933,8.834274,3.056310,0.344309,4.121267,-3.478240],[1.776456,-1.021221,-3.972542,-7.488447,-1.188514,-5.308586,-3.287794,-9.742085,6.747911,9.688941,-4.561267,7.333145,-3.173047,-6.784172,-8.047584],[7.831347,-5.865543,-7.010807,8.430491,6.156762,-5.565115,1.378759,0.509685,7.342322,-4.069747,4.986369,3.379843,-1.194332,6.668535,9.183574],[6.480985,2.562551,5.105171,2.975511,-2.231417,-7.014490,-0.832006,-5.808053,0.885260,-0.433211,-7.992244,-0.126747,-8.175689,8.539151,0.139816],[0.924903,-3.898389,-3.752945,-2.421802,-5.612202,-4.672674,-4.705912,-9.137068,-3.533051,-5.079593,-3.846520,5.736238,-1.249072,3.218255,6.775026],[4.013758,-2.705294,-7.912980,6.595497,-2.467968,7.898414,-0.983510,3.845106,-5.164090,-0.241555,-7.439236,8.523093,1.655123,6.213889,-9.331178],[1.947724,-9.203480,1.114729,-6.346071,6.352289,-8.879572,-5.695728,-6.627707,5.583163,5.441947,4.115902,-3.804065,3.701130,0.821486,6.615859],[-4.120290,1.219926,-2.491049,8.858174,4.911081,7.936630,4.818007,-2.710079,3.334440,7.280302,3.740373,-4.623876,7.267418,4.467622,-8.501071],[-2.740447,1.586374,6.243913,-4.608148,-9.972262,-6.354653,6.862821,4.012940,2.614606,-0.621951,-6.699279,-6.019567,6.005367,-7.827503,-7.306508],[5.995674,3.393456,-2.267639,-4.787583,3.939128,-9.355545,-2.951933,-5.755276,5.046787,-3.593471,-1.632419,3.767417,3.580484,-1.947899,6.760701],[8.828254,-6.097568,6.764016,0.236356,9.882392,-8.670398,-8.856318,-5.183438,4.076058,9.348099,4.643152,-2.349191,-8.630999,4.522589,3.057532]],[[4.996429,-6.621841,-7.203599,-6.316437,6.980528,-4.067666,4.435635,2.078237,6.669130,8.307522,-2.390795,-1.023635,9.561570,1.410019,-5.647871],[4.448161,1.480676,0.201930,9.622111,7.751431,7.573875,-8.202679,7.462289,-5.932169,-0.649387,4.825150,-3.577070,4.910631,-2.537334,3.968410],[-5.995665,-3.832590,-8.718678,9.071623,3.763949,-0.550984,-2.413168,2.009069,-8.476046,4.124915,2.670385,-2.633122,-5.576594,5.820352,-7.573738],[4.344423,7.724063,-9.891491,5.456855,0.344257,-0.498579,-7.685821,-6.783989,-0.529488,2.742428,-5.172801,-0.610670,4.471170,-8.717940,0.550286],[5.479383,8.704106,-8.240793,-0.084518,6.769276,-3.151053,0.201622,1.755261,-3.140198,3.175917,6.473625,-4.847468,-6.022443,-7.452358,-0.196901],[1.952517,7.260891,-4.514377,-3.390710,4.165180,-4.156011,8.600719,-2.117777,-3.338709,1.678772,8.089537,1.506055,-1.726975,3.946349,-5.926609],[2.803407,2.748407,3.551684,-4.177188,-4.825317,9.789013,-0.618008,-4.295614,0.958337,2.959643,-4.540501,0.286041,1.091132,5.251575,7.206992],[-1.862344,2.709017,7.603962,-4.991517,-2.690808,6.832033,9.139764,9.030965,7.146082,-7.591028,9.261850,1.022230,-9.178279,-8.936601,1.518486],[-9.033623,-8.012778,7.226686,-2.951279,-0.130166,-9.514627,-0.085449,2.895821,8.828389,6.309190,4.265123,2.711273,3.165007,1.023563,8.664695],[7.839594,2.908553,-2.695769,1.649150,-6.306847,2.992476,-2.448804,-9.954180,8.278864,-8.067476,-5.757293,4.750932,-7.261238,2.129448,2.685350],[-8.760045,-0.506047,-3.512216,-6.124380,5.441417,0.197662,3.855947,3.553301,3.137272,2.519368,1.686805,-7.900377,6.140896,8.185152,-0.870217],[-5.674828,-3.845199,-7.169152,0.227206,-9.831794,6.888901,0.867911,7.885667,7.312829,-8.514387,-8.834328,-1.419355,-7.950652,4.242341,-7.288094],[-1.980285,-4.408690,-3.624369,-2.204593,5.069558,-5.137952,-6.459112,8.775017,-3.250220,1.575007,-9.783421,-0.740740,-6.682128,-4.945627,5.605072],[2.207156,2.242404,-3.832423,3.688729,8.490658,8.208846,3.587251,-1.334827,-0.311413,8.024910,8.883686,6.919534,-9.749901,-6.302388,-6.402224],[-2.634973,-0.573479,6.464160,6.219840,1.715432,-0.318441,-8.467301,-4.732456,-2.864777,-6.870984,-8.254641,6.117145,7.881537,4.947430,3.685236]],[[2.127021,-3.536666,8.377297,-3.135348,-7.304223,-8.048142,9.227429,-7.190269,7.131300,-0.589312,7.467677,7.332614,-1.423327,-7.921671,-4.126248],[0.882432,7.349737,1.919480,-3.486955,6.421370,8.182536,0.640873,7.903520,4.992070,-6.202789,-9.614221,-8.238219,7.303844,-2.466582,4.209683],[4.322207,8.545207,-7.868491,4.330937,-1.883897,8.387034,-9.136404,-3.780373,-1.962836,-4.349196,1.225618,-5.612584,-2.830813,8.402923,-0.278521],[-9.563463,5.998881,-1.530809,-6.271391,-3.701244,8.987414,3.135017,-8.140693,9.074081,0.257852,-1.979253,-6.900385,-1.208242,-9.968726,4.270619],[-6.278147,-2.164081,6.784647,4.349503,-6.922755,4.359216,4.144180,-6.445480,-6.247104,8.600345,4.654881,7.886160,-3.861707,3.105434,6.108158],[5.752634,-1.619081,5.045466,1.805002,0.392420,6.882181,2.924125,9.876320,-9.191414,9.440032,6.685831,3.100313,-4.857217,3.887039,-7.543958],[-9.803745,-7.885958,7.848422,4.428443,8.307689,4.923580,0.665492,4.249772,-7.004693,-5.053714,6.515463,-9.182654,-7.959727,4.883659,-7.191147],[-0.796116,2.370536,4.898755,5.601467,8.573132,-7.238461,6.306873,2.113818,-6.772669,-8.816430,9.112832,4.860985,6.865094,-3.416707,3.518006],[-3.134914,-9.295452,-8.168570,2.298668,-0.371714,-6.670313,7.735996,-8.310915,5.604887,-8.558598,6.144412,6.394301,9.551237,0.365530,4.151783],[5.511442,-1.223274,-9.890134,6.810651,-6.315302,-2.971454,-1.307945,-1.726656,5.462116,-0.839419,-0.121915,4.406528,-0.499819,-2.509980,4.728452],[-3.724317,5.320411,-0.338116,5.367709,6.625910,0.247920,6.605184,0.190587,-2.835709,4.774339,-0.742589,-4.176434,2.965401,1.675008,-3.574092],[-4.214100,0.977745,-7.315715,9.331209,4.052638,3.258525,-3.787164,5.139603,7.474686,-7.060582,-1.613249,-2.171328,6.587333,4.351945,8.423420],[9.837256,-5.933465,1.103128,-8.808289,-8.999523,-2.703601,-2.222406,-9.136946,-3.766224,7.571855,-8.517995,-6.313707,-5.584990,0.398114,-8.921143],[-4.670203,-0.351217,-9.533510,4.071291,-1.860772,-4.704161,8.843764,3.528455,-2.197313,7.604686,6.413276,6.580464,-2.816829,7.407620,2.915195],[-9.608819,1.998470,-0.944852,2.284599,-0.746420,-2.630627,-8.716849,7.650463,4.939568,4.141104,3.710780,2.531796,-5.475133,-6.902162,2.725142]],[[1.026206,7.438838,-7.655933,-5.357404,0.189494,2.002770,-9.938414,-1.523454,9.170712,0.569584,-6.695518,9.644786,-7.166318,-9.555769,6.319977],[-6.539410,2.973781,6.231636,-5.545705,9.503707,-4.226136,1.118396,-8.212682,-0.228699,6.616094,0.478953,-9.830059,3.784717,-7.701834,-1.435435],[9.928130,0.785456,-0.432683,-1.276434,-0.588546,2.165089,-1.579487,1.480290,-5.005621,9.743050,-0.053851,8.716717,2.910096,6.554009,-3.630626],[-2.875922,-6.793674,3.010921,-3.755635,3.284258,4.125951,-7.899513,7.492882,0.529232,2.351430,-6.579247,0.118818,3.765953,-8.367709,-5.813547],[-3.190217,9.363713,-6.268261,8.627519,-4.492055,-2.942140,5.173170,-9.304156,-8.945200,-2.417486,-4.362600,8.610034,3.285374,-9.658648,7.966022],[-3.203746,9.777540,6.040556,-7.429794,4.261219,8.595172,0.168137,-1.115066,-4.448360,9.968364,-1.611114,8.832721,2.278522,-8.720173,-8.398186],[-6.105226,9.334320,-5.623629,-6.671918,-5.900900,-3.223305,4.332399,-2.950440,1.186902,-4.312441,-0.622587,-6.736426,3.536832,-9.245203,6.755350],[5.638848,0.564572,-4.603349,8.903589,4.498594,-9.324630,-8.746356,1.566037,6.737768,2.582546,6.936344,-0.877931,1.789619,3.874676,-0.849040],[-0.294467,-6.235677,-8.492685,-8.085981,3.792067,1.077252,8.759747,6.171339,8.117872,6.201926,8.953438,-3.474248,-4.820296,5.716299,8.336207],[-0.847052,6.518276,8.128001,2.363232,-6.696946,1.383277,-7.252478,9.467135,4.665990,-2.849566,1.873574,5.670965,-7.959482,2.172384,3.612432],[0.035771,-6.306902,2.193654,-5.901012,8.342771,4.755409,2.358585,2.491283,-5.710817,0.540973,1.781580,-8.920270,-6.618196,-6.395634,-4.871920],[-6.517450,-4.686196,-3.917709,-4.858277,-1.312931,3.817274,6.273417,-7.956855,8.216042,7.273053,1.780863,9.927658,-2.376035,-6.368496,6.989935],[-6.760583,-2.078700,6.316079,-9.742201,-2.766891,0.012530,5.818154,-1.785882,-5.612567,-6.919139,-1.666300,-5.772550,0.148715,2.525525,-1.523014],[-6.592266,-2.604363,6.632839,6.326910,5.398474,-2.486055,-1.396907,8.080129,5.237715,-4.138374,-2.333529,-4.709416,0.712126,7.171974,6.603085],[1.057908,-0.096676,0.484224,2.691340,-1.967116,-5.516498,-9.771752,-6.670319,7.171558,5.870937,4.437181,-0.346885,-6.269924,4.787175,-4.078509]],[[1.846125,-1.275114,9.169243,6.488771,-9.635533,4.639626,9.672958,0.261391,-7.401793,3.247165,5.318873,4.398127,-4.763006,2.696776,0.259491],[3.193325,3.852985,-9.229619,5.808439,-9.529235,8.467276,-7.493890,0.807096,-2.320470,-8.746459,4.093170,-9.775503,2.149921,-6.138590,-4.841784],[-0.248924,3.140447,8.246369,-3.325454,7.677161,2.315802,-9.389296,5.216593,7.396469,9.809260,-4.317768,9.188721,2.897970,4.184769,6.100864],[6.356709,5.370811,-8.873490,5.967162,5.009471,5.392248,6.230718,-2.798864,3.282835,0.731678,6.635914,0.123807,-8.106566,2.780224,-8.980134],[-9.741106,-7.439231,-1.228755,-4.669519,7.255645,0.597968,-7.456942,8.256932,5.919845,3.825029,0.596679,-5.644206,5.516968,-3.488413,7.249597],[-4.046511,-3.766892,0.378429,8.542618,-2.072608,-1.819708,2.327577,7.882258,1.253268,4.843073,1.402178,-0.226141,6.740526,-9.077417,-0.259932],[-4.744934,5.488885,-4.846189,-4.368259,4.752390,-5.056897,-6.484496,-8.235551,-5.717472,-6.592489,-5.965458,6.496274,-9.774974,3.436564,-6.846110],[-4.314830,-4.269143,3.741613,-4.319640,-4.355528,1.413413,1.330008,-8.258326,7.726835,-0.102495,-1.751470,4.864679,5.741312,-7.468477,-8.401109],[-8.490155,6.757586,2.498972,3.592533,-3.474791,2.795400,6.062749,0.295578,-3.570417,-9.651119,1.258674,-1.628835,-5.546728,-3.062828,-4.432249],[3.863452,4.690776,3.811179,-5.076516,-1.956202,-2.533592,-1.173305,8.037701,2.270555,-8.861082,-3.198327,-1.269024,-3.499606,-5.959784,7.046959],[3.116070,2.795760,9.080301,9.690196,-4.077249,3.179136,7.703142,-8.913501,1.289630,1.875600,2.873403,6.784031,-6.257932,2.352315,-7.276018],[1.039730,1.615391,-5.981639,8.528767,-0.081236,-2.349681,-9.299013,9.038492,-9.998461,-4.234752,-2.814893,0.826897,1.971075,9.976961,-4.898230],[4.791425,-6.279953,-8.104336,6.604154,-8.839755,9.767074,7.401490,7.000726,-7.851874,-6.196382,5.606274,8.191175,-8.442656,-6.197890,5.973550],[-8.753494,-9.080684,3.513009,0.672795,-8.072580,7.863940,-7.150055,2.315944,4.741097,0.355361,-9.162916,5.829921,0.417355,-3.907672,3.567076],[-7.855494,-1.184876,-2.181411,-8.844444,-9.896738,-9.813243,-0.571030,6.122370,-8.889622,-0.372599,-0.917167,-8.068577,-0.674027,5.585711,6.605306]]], dtype = "float64")#candidate|12939|(11, 15, 15)|const|float64
uop_12940 = relay.cosh(const_12939.astype('float64')) # shape=(11, 15, 15)
output = relay.Tuple([uop_12940,])
output2 = relay.Tuple([uop_12940,])
F = relay.Function([], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([], output2)
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
