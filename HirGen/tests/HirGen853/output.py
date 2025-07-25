import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_78 = relay.var("var_78", dtype = "float64", shape = (5, 2, 14))#candidate|78|(5, 2, 14)|var|float64
uop_79 = relay.atan(var_78.astype('float64')) # shape=(5, 2, 14)
output = relay.Tuple([uop_79,])
output2 = relay.Tuple([uop_79,])
func_106 = relay.Function([var_78,], output)
mod['func_106'] = func_106
mod = relay.transform.InferType()(mod)
mutated_mod['func_106'] = func_106
mutated_mod = relay.transform.InferType()(mutated_mod)
var_107 = relay.var("var_107", dtype = "float64", shape = (5, 2, 14))#candidate|107|(5, 2, 14)|var|float64
func_106_call = mutated_mod.get_global_var('func_106')
call_108 = func_106_call(var_107)
output = call_108
func_109 = relay.Function([var_107], output)
mutated_mod['func_109'] = func_109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_195 = relay.var("var_195", dtype = "float64", shape = (15, 3, 7))#candidate|195|(15, 3, 7)|var|float64
uop_196 = relay.acos(var_195.astype('float64')) # shape=(15, 3, 7)
func_106_call = mod.get_global_var('func_106')
func_109_call = mutated_mod.get_global_var('func_109')
var_204 = relay.var("var_204", dtype = "float64", shape = (140,))#candidate|204|(140,)|var|float64
call_203 = relay.TupleGetItem(func_106_call(relay.reshape(var_204.astype('float64'), [5, 2, 14])), 0)
call_205 = relay.TupleGetItem(func_109_call(relay.reshape(var_204.astype('float64'), [5, 2, 14])), 0)
output = relay.Tuple([uop_196,call_203,var_204,])
output2 = relay.Tuple([uop_196,call_205,var_204,])
func_210 = relay.Function([var_195,var_204,], output)
mod['func_210'] = func_210
mod = relay.transform.InferType()(mod)
var_211 = relay.var("var_211", dtype = "float64", shape = (15, 3, 7))#candidate|211|(15, 3, 7)|var|float64
var_212 = relay.var("var_212", dtype = "float64", shape = (140,))#candidate|212|(140,)|var|float64
output = func_210(var_211,var_212,)
func_213 = relay.Function([var_211,var_212,], output)
mutated_mod['func_213'] = func_213
mutated_mod = relay.transform.InferType()(mutated_mod)
var_582 = relay.var("var_582", dtype = "float64", shape = (13, 15, 4))#candidate|582|(13, 15, 4)|var|float64
uop_583 = relay.acos(var_582.astype('float64')) # shape=(13, 15, 4)
output = uop_583
output2 = uop_583
func_589 = relay.Function([var_582,], output)
mod['func_589'] = func_589
mod = relay.transform.InferType()(mod)
var_590 = relay.var("var_590", dtype = "float64", shape = (13, 15, 4))#candidate|590|(13, 15, 4)|var|float64
output = func_589(var_590)
func_591 = relay.Function([var_590], output)
mutated_mod['func_591'] = func_591
mutated_mod = relay.transform.InferType()(mutated_mod)
var_609 = relay.var("var_609", dtype = "float64", shape = (16, 3, 3))#candidate|609|(16, 3, 3)|var|float64
uop_610 = relay.log(var_609.astype('float64')) # shape=(16, 3, 3)
output = relay.Tuple([uop_610,])
output2 = relay.Tuple([uop_610,])
func_613 = relay.Function([var_609,], output)
mod['func_613'] = func_613
mod = relay.transform.InferType()(mod)
mutated_mod['func_613'] = func_613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_614 = relay.var("var_614", dtype = "float64", shape = (16, 3, 3))#candidate|614|(16, 3, 3)|var|float64
func_613_call = mutated_mod.get_global_var('func_613')
call_615 = func_613_call(var_614)
output = call_615
func_616 = relay.Function([var_614], output)
mutated_mod['func_616'] = func_616
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1201 = relay.const([[[9.868171,7.879614,9.195710,3.582970,-3.821808,3.454516,-5.153753,3.557466,6.190427,6.171362],[-2.204068,-9.031723,-7.219869,-5.029748,2.712676,8.471533,0.132085,-3.883658,0.612463,3.675259],[-9.383733,-7.568293,0.895936,9.391069,1.620365,-1.464669,-6.485390,-9.946732,0.983066,3.381822],[-6.843614,-6.161177,-1.239631,-3.456341,-7.238054,5.653716,-8.920408,7.230054,3.408093,2.682470],[8.622010,-9.209323,-5.051823,-9.293142,4.366077,3.481171,-7.888370,3.695043,-4.727213,-0.942208],[-8.477448,9.556471,6.070462,-5.199359,0.348806,5.067619,1.485906,-0.015458,-6.044372,-6.166872],[-2.384020,-1.061322,6.163374,9.394478,7.322890,-3.680810,1.502924,3.138983,-5.691872,-9.180744],[2.752044,-3.514452,7.216263,-5.695588,4.920617,-0.538039,-3.343482,-7.806503,-0.262410,1.167014],[-2.931895,4.370964,2.946714,-7.113535,-5.784403,8.011525,1.309769,1.038774,-1.818330,-1.731791],[-5.039058,-1.559290,5.204693,-8.348585,-8.434286,-9.091260,1.347777,8.580131,-2.659718,-8.170746]],[[-3.100299,-1.151137,5.099749,-0.554889,2.834921,4.646336,0.733884,7.040305,-6.604076,7.396599],[2.969062,9.477440,2.665397,-4.896812,7.923853,3.372769,-4.750298,6.623552,0.235998,-2.405392],[-1.379348,-2.179890,1.311012,1.877697,0.576081,-1.623379,-4.677942,7.833671,-9.174143,9.958816],[-8.778920,3.035758,-8.499865,-5.085829,1.324907,-2.797060,-9.933751,5.209916,-0.484143,6.587994],[9.964473,7.253700,-8.409896,-9.123202,-6.167620,-1.898951,-3.717444,9.330625,-1.041594,-5.574302],[-6.797185,2.986353,0.350341,-5.095810,0.494256,8.800197,-7.560230,-5.651629,0.821624,2.774991],[-5.451790,-8.203731,-1.836475,5.315895,9.692469,-9.050869,9.186472,-7.066451,-7.352807,-3.158687],[-0.879669,0.164885,-2.387534,7.507732,-4.535254,1.487756,-4.476849,2.895723,-3.392198,1.064513],[-8.562473,7.828951,-9.314345,-6.936617,6.945946,-9.992685,-6.430839,-7.931808,-8.057357,-1.710239],[-9.025295,4.724331,2.769046,7.445608,-0.253469,1.100364,-7.263081,-5.640166,-9.951582,-4.820058]],[[1.607765,0.918655,-9.225549,2.949638,-5.988484,5.217208,1.048004,8.729844,9.083259,-4.204320],[-6.465331,-8.537528,0.303445,1.583779,9.088797,7.570706,-1.853947,-8.414598,-9.461102,6.271959],[7.313572,9.720452,-9.931047,7.510224,-7.776316,4.669995,9.817039,3.683297,-0.571666,-7.415319],[-1.438747,-8.268621,-9.091322,8.773983,-8.216844,4.239325,7.075638,0.946922,-3.971179,2.095311],[-7.394515,3.701894,-2.372909,-7.241997,1.648823,-4.552831,-7.367165,-4.088209,1.124660,6.183760],[6.859086,2.853051,-2.148255,-3.609965,8.737718,4.699201,-3.374131,0.075835,4.375546,5.065698],[-8.408312,2.409157,-4.929009,-9.456112,9.556306,-4.757358,-9.195544,-8.443022,-2.899776,7.679007],[-9.592428,2.273209,0.521400,-2.234756,6.177298,9.562503,9.363352,-7.498202,0.189716,-0.726112],[6.859022,9.495492,-7.500732,-4.211044,-2.488481,4.934828,-1.008334,0.501595,6.404439,-8.599051],[8.032000,8.748905,-9.102273,-6.555234,-6.679860,7.958735,0.655036,5.385593,-0.870063,-2.837413]],[[-0.063602,2.649641,6.551298,-9.807564,-4.986380,2.757185,1.156245,4.114544,-3.001006,8.551656],[-5.057788,-4.087313,7.315126,6.198014,0.618932,-2.717007,5.276472,-8.667030,-0.986239,-3.455897],[-5.484362,-8.316357,-1.487279,5.585215,5.283902,9.590755,1.952292,-0.303147,5.081551,-1.721268],[4.823770,-5.539981,9.665460,3.431669,-9.519749,-9.116636,5.724411,-2.086884,-8.398402,8.491589],[-5.306292,6.183828,-1.860456,-6.352746,-3.670023,0.516224,6.459675,-1.536560,-4.900212,-4.072411],[2.492902,6.592940,6.783815,-7.539965,-7.853973,5.832579,-4.433837,-1.248715,-1.962586,8.562830],[-1.518286,5.762246,-0.394172,-2.757596,7.435791,2.840318,4.027203,-6.071128,-5.716188,5.150764],[-5.912647,0.345069,7.043123,4.346382,-5.774049,-9.969551,4.867259,-1.914894,-0.472211,6.207146],[4.998184,-3.583761,2.014883,6.195017,-3.349813,-7.917220,-7.523615,1.784060,-8.772996,1.334908],[4.272919,3.207240,9.048342,9.985396,-1.473924,-2.481848,6.580805,-7.785373,8.340234,3.487179]],[[-7.719662,-3.050360,5.227932,3.898580,-4.500703,0.072856,-8.665617,8.797587,-3.027346,7.608879],[7.019399,1.983269,5.283257,5.767468,2.493626,-4.333428,0.097166,-1.082531,-2.395582,-0.911340],[6.152506,8.337682,-8.076918,4.228601,9.163995,7.412256,-7.243219,4.191683,-6.785573,-6.494586],[5.620343,-5.815631,1.000707,-7.918094,-3.946467,6.228209,-7.224675,9.796319,3.442320,5.484685],[-3.223576,8.610401,9.777201,-3.779043,3.418924,-8.904766,3.251622,4.084076,4.355773,-7.467762],[-1.568242,5.362588,-9.890745,6.632394,-0.325918,-5.045296,1.609688,4.706767,2.398506,3.418602],[2.063241,6.808255,-4.490388,6.394968,-2.588220,1.841053,5.973676,2.927567,3.936749,1.655224],[-3.608113,-9.133266,4.493607,-9.666224,5.394811,-6.660203,7.967218,8.475895,-7.943626,-8.866499],[5.023321,-1.856547,-9.612839,-5.899891,-0.104724,2.904718,-6.878766,4.747130,-1.757090,-5.410093],[5.914435,-0.674737,-4.153883,-4.935664,-0.092431,-1.363796,-4.042036,2.362211,-1.227999,-9.144402]],[[6.541898,7.574160,-4.431605,-2.696003,7.112135,-9.775016,6.674835,6.606491,1.676085,-9.184490],[-1.851472,4.573015,3.455648,-1.214479,-7.363274,7.582852,-5.061527,5.622363,1.243320,0.929516],[-4.151921,3.714489,-7.939259,-6.970600,-3.581195,-4.239579,9.984047,8.968312,-1.904820,-0.767594],[-5.106382,-9.346177,4.754157,3.565819,6.063279,8.906000,7.418205,9.515677,3.896275,8.714808],[6.294084,8.008260,5.128680,8.837313,-8.422067,-6.059228,1.711202,6.318034,5.312647,0.286077],[-2.767931,-2.130299,5.344427,2.133758,2.389053,-7.007605,-7.664969,3.186506,-2.001350,7.261508],[9.127206,-9.323205,0.446667,2.836949,-0.358773,7.756146,8.712784,-8.795486,-4.758826,2.585493],[-7.769663,-2.120085,3.648269,-4.916373,-6.707680,-7.343077,-1.204936,9.736692,7.453527,-4.866625],[8.483738,-9.230456,1.643266,-9.990288,-1.673149,-9.482277,7.692678,-2.693141,-2.213310,5.072582],[-7.403171,-4.355020,-8.575140,-3.342086,-1.801383,8.653031,1.083256,-2.140057,4.506578,-4.120763]],[[0.391508,-2.813600,7.882722,1.630829,-2.740269,-4.155022,5.287225,6.356984,-6.044968,2.456893],[-1.873305,2.057756,-0.112206,-9.549678,-8.883169,8.321377,6.925716,-1.071339,-5.336650,3.774501],[-5.866383,-1.088695,-9.620045,5.120862,3.981319,-2.638918,-3.927313,9.010456,3.656922,-0.798194],[-3.883075,3.085521,0.179341,-7.656572,-6.228830,-7.859157,-5.765878,-5.586557,-6.493675,9.205785],[-6.516138,1.402062,9.904249,7.648712,5.551048,-1.463340,6.588426,2.499025,-9.527326,1.150731],[2.356542,3.284839,-8.873738,8.998876,-7.383516,-0.973841,-8.690315,6.755440,2.702440,-8.686940],[-2.159135,-9.372303,2.034229,-4.334570,-9.608228,-1.811678,-7.021528,8.632303,4.387088,4.182134],[0.983039,-2.621676,-6.310317,-8.178617,-1.810327,-3.759410,4.044303,-9.354990,-1.296299,-5.892182],[-2.747974,1.756665,8.693062,2.803421,1.844372,-3.856513,9.097386,-6.352684,-9.805568,4.815274],[1.015913,6.727082,-2.848846,0.411716,-3.726971,4.151984,-7.136775,7.710945,0.795446,-4.152660]],[[-2.910509,-5.648607,0.573580,2.793329,9.658774,-9.940893,-0.288944,9.782465,-3.424768,3.558556],[1.428954,3.529288,2.255589,5.144827,-1.268461,7.495902,-3.935347,-1.481959,-8.882263,0.293111],[-7.793826,5.745431,5.934243,9.666313,1.666623,-7.502978,-7.999992,8.448775,7.186410,-6.047808],[-4.544050,-5.381245,1.586507,3.074271,-6.551693,8.006292,-5.520869,3.465202,-9.933932,5.047961],[3.774457,-4.293367,-7.016563,-7.855673,-2.784439,8.711291,-9.664987,1.262920,-9.389211,-9.699054],[0.383447,2.654324,-5.836590,8.237375,0.790460,-9.105362,-4.986377,-4.680803,-4.218308,-7.184857],[-7.918946,-4.349619,8.970260,-9.554088,-4.465745,-0.460845,2.755953,7.826096,-8.287727,-8.267518],[-0.780404,4.425200,6.762743,5.585007,-1.749377,-7.282018,0.010824,0.171333,-2.589040,-8.226365],[-3.788108,-7.668127,-6.443923,8.123046,-9.313418,-2.289014,4.321034,9.973254,-2.491886,-8.378568],[7.162918,5.505570,7.524226,5.678181,-1.744061,-2.857782,7.374407,-3.974854,9.307910,-1.470269]],[[6.842707,-8.666679,-3.025210,0.567583,-2.532282,7.726268,-9.715327,-7.032997,-6.652117,6.708486],[9.546882,6.591469,-2.150521,-6.256198,-9.471241,1.015421,0.027724,-8.284738,-9.486164,-7.211389],[9.675342,-3.020617,-9.725923,-5.144929,-1.850389,-8.970482,2.125182,-0.931308,3.368418,7.288683],[-1.958663,-1.192099,-4.717919,0.823420,-9.972461,0.868291,-0.173989,-2.216477,-8.392778,6.646432],[-2.514210,-7.109581,1.916892,-0.892800,5.594431,-5.329328,-8.903162,-6.952705,8.310066,7.905406],[0.834654,-5.328487,-4.636652,3.014429,0.110925,-4.464786,-4.942927,0.931897,0.813615,-0.142459],[-4.041248,-4.184641,8.445491,1.694484,4.409870,5.134166,-6.534043,-6.735977,-4.225036,0.364218],[-4.762501,2.225532,9.286291,-8.598193,-3.746191,6.493802,-1.917275,-1.480512,-0.269617,-7.936069],[-9.645822,6.137934,7.758698,-7.194787,6.777962,4.454335,5.495165,-1.879508,-7.296260,6.102505],[8.205328,7.265712,2.624908,-9.274492,8.253402,5.475090,-7.244898,-9.166850,-0.811259,4.497496]],[[4.221069,5.842228,8.996405,1.253469,-3.417143,6.109213,9.492866,3.859493,-6.159765,4.704421],[0.303047,7.532696,0.980453,8.755764,-1.458802,3.028842,-1.845574,-1.673589,-0.122180,7.149745],[5.463392,-4.790328,9.074526,0.057542,2.357235,7.955919,4.662752,-3.910728,1.503783,-7.925111],[-9.726140,3.478467,-0.123699,9.395734,4.553928,3.610303,4.035177,8.888969,-1.368540,-6.094792],[3.720888,-6.807349,-9.840684,0.991892,-2.671173,-2.518641,3.212184,7.863212,6.974182,-5.824703],[0.831307,7.147466,-0.558750,2.307721,8.988813,-8.732075,-8.700857,3.295705,-6.654914,-6.115834],[-4.257108,4.301560,-7.992346,9.930122,3.339492,-6.587826,-3.395405,2.044488,-0.398579,2.935362],[-9.112525,3.056540,-6.259399,-2.022055,1.981198,8.534910,2.662429,-7.187670,-4.988615,7.095478],[4.250094,-8.676970,-3.171192,-3.127573,1.244423,-5.187591,-6.049082,-1.091371,6.261365,3.489110],[1.239703,-2.355016,8.053990,-2.539049,1.859299,-3.162782,1.044152,-8.040947,-7.086707,-5.388497]],[[-1.755782,-0.513043,-0.304188,3.108631,1.439043,5.216217,7.727737,6.783046,-3.501512,-8.904161],[4.186741,-1.905423,-3.326651,-8.069367,-0.131912,-7.758652,-4.795257,0.589051,6.568590,-5.287260],[7.218982,2.779695,0.349094,5.538393,-5.213227,0.897653,-4.024821,-6.351724,-8.315030,-1.105545],[4.586817,1.500792,6.755901,0.287239,6.372668,4.653113,3.434248,-2.366546,6.961905,-6.436595],[1.802852,7.146662,0.613398,-9.454813,1.537512,-8.141587,1.920770,-8.681360,-7.687576,8.319499],[5.361931,-1.870896,6.860978,9.404439,6.608187,-5.380428,-0.016778,-8.535896,6.546640,9.057325],[0.030709,-8.452667,-3.797174,5.519085,-0.075519,-9.855963,0.612304,-2.608126,1.191604,9.640513],[0.397701,-1.560853,-0.874888,4.664140,8.188652,-9.117150,2.299863,-1.285858,5.792380,-9.885950],[-6.503281,8.703805,-8.927228,6.471960,0.791319,-0.813449,-8.742334,-3.221834,7.368480,2.104939],[0.912341,-4.487195,-2.285590,-5.957043,-1.837187,3.836865,1.561889,0.393379,-7.363557,-2.317341]],[[0.323790,-4.529034,7.246760,-7.251560,-2.523552,6.222312,1.046497,-2.893773,-3.065293,6.666530],[-4.665933,-3.623658,0.147405,7.758202,-0.073568,-2.665347,-6.184366,2.062294,8.010226,-0.894648],[5.232065,7.563981,4.043897,-7.426080,-0.859055,4.480421,-3.445119,2.698913,2.959297,4.357578],[-0.853408,0.015140,-0.110249,-9.008292,5.717614,-2.918540,-8.673993,5.625174,4.474261,-1.920366],[-5.017570,-1.283501,9.384337,-1.417328,-4.995490,-7.289175,2.541204,4.135784,-6.718576,-9.805763],[9.154703,6.557270,-9.717006,1.260123,-4.684942,-7.232966,4.338418,-9.969342,-1.268112,0.226782],[-8.380681,0.572288,-9.562611,-7.224867,-4.415295,-7.314341,2.102473,7.723110,-1.084392,0.166020],[-3.154094,7.914218,7.445839,-5.632401,9.574943,-3.873774,1.156627,1.787722,6.735402,3.293868],[-6.064470,9.397263,4.210400,-7.384166,0.583847,-1.063816,7.383555,-5.486902,3.355220,-6.980947],[-9.802746,9.192886,-7.984156,8.629661,-9.050064,4.772729,-0.552908,-4.254479,6.078515,-0.902512]],[[-1.639404,2.704068,-1.423658,-5.556399,-0.722651,-3.793405,-5.099827,6.214230,8.077576,-9.621241],[8.501104,-7.959614,-6.546239,5.674502,6.075605,-9.828772,-4.389904,2.934147,9.804523,0.217032],[-8.113595,9.532600,7.724152,8.253097,7.664336,-1.989023,3.165259,9.063720,2.080200,-5.894053],[-6.887318,-8.158300,-9.996197,2.816132,-9.889985,1.495942,7.404521,0.772783,7.765048,7.751956],[-9.385336,4.085946,-0.136987,5.496743,6.899674,6.755018,-8.620857,4.885490,9.537914,4.744302],[6.220516,5.838411,4.541284,4.941339,6.417108,3.905811,-0.720279,-3.049653,3.349751,-3.648626],[4.478756,-7.495700,1.813992,-0.951035,0.721704,-9.162005,-3.955674,6.651765,-5.935250,4.420103],[9.218569,6.297796,5.691226,-8.883865,5.569834,-1.778805,-0.857938,3.266725,-8.728960,8.145581],[2.996490,-8.153942,9.462251,0.048029,-0.126452,6.784891,2.854120,6.263106,-6.618463,-6.918911],[-6.525403,-8.771007,3.473896,-2.883331,8.678752,9.810779,-7.928872,6.419716,7.979064,6.635465]],[[4.382939,7.082931,-2.808715,6.524341,2.924209,-9.516484,-9.587821,-1.075400,-9.597777,8.727636],[-2.287394,-8.068442,-2.150863,-1.505645,-6.259155,2.377828,0.472246,6.676808,8.481874,-1.367873],[-1.256168,-9.061621,-9.609315,-0.156602,-8.993421,-2.446257,5.980593,9.513229,-3.695897,5.337607],[0.356177,-9.041180,-2.659526,-3.184468,1.055918,-6.889912,-6.411006,-6.766043,5.274738,1.834391],[0.804677,4.088971,3.864903,-0.072205,-2.644674,-7.823926,8.990145,-2.065517,-8.770637,6.128888],[-4.125559,7.509961,9.496653,7.139290,6.995766,-7.481501,-7.773120,8.256720,-3.078415,-6.653094],[4.743400,-5.934752,6.116671,-8.092159,-9.277533,7.044050,5.336772,3.625527,4.119313,-0.970915],[7.948694,6.249776,-2.025972,6.668005,-3.117113,2.714916,1.323975,-5.490226,7.890125,-4.084906],[6.128138,-2.837822,1.505012,7.525634,-7.966153,7.682123,-6.921921,4.813948,1.464744,6.087997],[-6.673564,1.960244,-2.673880,1.787812,7.003148,2.577186,4.135851,4.650752,4.757746,3.283525]],[[-7.711319,-7.322952,4.391304,6.764693,-0.123108,1.982749,-4.788128,-3.094080,-6.372807,-5.929988],[-9.018403,-0.197168,1.845873,-4.487984,-5.836768,-1.423136,-3.934756,9.419596,-9.263857,-9.282593],[8.990037,-2.829433,-7.707140,4.066103,-9.116606,-3.604900,3.552487,-5.831546,7.571268,-6.660433],[3.094902,-4.116455,0.182358,5.909556,5.435703,-6.672965,8.831240,-8.119186,-6.029118,1.330699],[2.984746,9.353511,-0.899661,1.449082,-1.192285,-6.153916,-0.100656,9.322442,-7.073317,7.736585],[-6.119412,3.197454,-7.666533,3.002081,5.885273,7.476457,8.911326,7.212558,1.507683,8.806107],[-2.712379,2.959658,-7.693933,-7.125764,2.281605,-6.692781,-9.857357,-3.123327,4.136590,9.224365],[-7.946313,0.710954,7.831883,6.311957,6.682143,-1.340674,-2.460878,-2.364347,-0.959503,-8.848643],[7.945966,2.203080,-7.169757,-0.736589,0.974534,-8.509655,4.610487,7.696815,-0.026048,5.194608],[4.937768,-4.758135,8.011367,3.745492,0.972662,6.448830,-9.200490,-0.450464,-2.251194,2.481139]],[[-0.352957,5.995733,5.483366,-9.581846,-4.336710,-3.672636,2.162978,0.632314,9.581970,-0.914680],[-9.382419,7.948719,-8.043649,5.723900,7.778209,7.073831,-8.605608,7.169205,9.439078,-9.623461],[1.642094,-8.034016,4.281661,1.991260,-4.644436,3.685958,4.622650,0.506686,7.978375,4.018395],[5.875336,-4.250494,5.443667,-3.628006,-8.236592,-4.682042,0.953377,-9.167712,7.511705,5.750633],[-2.941649,-5.513704,-4.510959,5.870790,3.443104,-3.145575,7.226752,-4.414579,-4.664845,-2.371007],[1.327115,-9.062343,8.319000,7.222025,-5.257261,-7.627090,-0.653133,-7.770596,-5.956109,-2.583829],[-6.643446,2.453298,5.645702,0.424072,-1.109920,-8.393720,-3.078940,-7.494872,-5.015088,-2.490969],[-7.332120,8.514215,-9.607012,9.735617,2.004408,-2.287603,-9.240177,-5.043615,8.706532,5.179164],[0.166046,-3.411015,-1.041565,6.368184,-8.093254,0.443632,-2.068491,5.634151,6.724040,6.814215],[-8.222546,-2.346226,3.953583,4.755165,-1.523865,-8.105045,-5.090460,-0.267441,1.826733,1.182758]]], dtype = "float32")#candidate|1201|(16, 10, 10)|const|float32
uop_1202 = relay.acosh(const_1201.astype('float32')) # shape=(16, 10, 10)
func_589_call = mod.get_global_var('func_589')
func_591_call = mutated_mod.get_global_var('func_591')
var_1205 = relay.var("var_1205", dtype = "float64", shape = (780,))#candidate|1205|(780,)|var|float64
call_1204 = func_589_call(relay.reshape(var_1205.astype('float64'), [13, 15, 4]))
call_1206 = func_589_call(relay.reshape(var_1205.astype('float64'), [13, 15, 4]))
func_589_call = mod.get_global_var('func_589')
func_591_call = mutated_mod.get_global_var('func_591')
call_1215 = func_589_call(relay.reshape(var_1205.astype('float64'), [13, 15, 4]))
call_1216 = func_589_call(relay.reshape(var_1205.astype('float64'), [13, 15, 4]))
output = relay.Tuple([uop_1202,call_1204,var_1205,call_1215,])
output2 = relay.Tuple([uop_1202,call_1206,var_1205,call_1216,])
func_1222 = relay.Function([var_1205,], output)
mod['func_1222'] = func_1222
mod = relay.transform.InferType()(mod)
mutated_mod['func_1222'] = func_1222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1223 = relay.var("var_1223", dtype = "float64", shape = (780,))#candidate|1223|(780,)|var|float64
func_1222_call = mutated_mod.get_global_var('func_1222')
call_1224 = func_1222_call(var_1223)
output = call_1224
func_1225 = relay.Function([var_1223], output)
mutated_mod['func_1225'] = func_1225
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1243 = relay.var("var_1243", dtype = "bool", shape = (8, 10, 1))#candidate|1243|(8, 10, 1)|var|bool
var_1244 = relay.var("var_1244", dtype = "bool", shape = (8, 10, 15))#candidate|1244|(8, 10, 15)|var|bool
bop_1245 = relay.logical_and(var_1243.astype('bool'), var_1244.astype('bool')) # shape=(8, 10, 15)
uop_1260 = relay.acos(bop_1245.astype('float64')) # shape=(8, 10, 15)
var_1278 = relay.var("var_1278", dtype = "bool", shape = (8, 10, 15))#candidate|1278|(8, 10, 15)|var|bool
bop_1279 = relay.bitwise_and(var_1244.astype('uint16'), relay.reshape(var_1278.astype('uint16'), relay.shape_of(var_1244))) # shape=(8, 10, 15)
output = relay.Tuple([uop_1260,bop_1279,])
output2 = relay.Tuple([uop_1260,bop_1279,])
func_1285 = relay.Function([var_1243,var_1244,var_1278,], output)
mod['func_1285'] = func_1285
mod = relay.transform.InferType()(mod)
mutated_mod['func_1285'] = func_1285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1285_call = mutated_mod.get_global_var('func_1285')
var_1287 = relay.var("var_1287", dtype = "bool", shape = (8, 10, 1))#candidate|1287|(8, 10, 1)|var|bool
var_1288 = relay.var("var_1288", dtype = "bool", shape = (8, 10, 15))#candidate|1288|(8, 10, 15)|var|bool
var_1289 = relay.var("var_1289", dtype = "bool", shape = (8, 10, 15))#candidate|1289|(8, 10, 15)|var|bool
call_1286 = func_1285_call(var_1287,var_1288,var_1289,)
output = call_1286
func_1290 = relay.Function([var_1287,var_1288,var_1289,], output)
mutated_mod['func_1290'] = func_1290
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1321 = relay.var("var_1321", dtype = "float32", shape = (3, 12, 12))#candidate|1321|(3, 12, 12)|var|float32
uop_1322 = relay.asinh(var_1321.astype('float32')) # shape=(3, 12, 12)
func_613_call = mod.get_global_var('func_613')
func_616_call = mutated_mod.get_global_var('func_616')
var_1338 = relay.var("var_1338", dtype = "float64", shape = (144,))#candidate|1338|(144,)|var|float64
call_1337 = relay.TupleGetItem(func_613_call(relay.reshape(var_1338.astype('float64'), [16, 3, 3])), 0)
call_1339 = relay.TupleGetItem(func_616_call(relay.reshape(var_1338.astype('float64'), [16, 3, 3])), 0)
output = relay.Tuple([uop_1322,call_1337,var_1338,])
output2 = relay.Tuple([uop_1322,call_1339,var_1338,])
func_1364 = relay.Function([var_1321,var_1338,], output)
mod['func_1364'] = func_1364
mod = relay.transform.InferType()(mod)
var_1365 = relay.var("var_1365", dtype = "float32", shape = (3, 12, 12))#candidate|1365|(3, 12, 12)|var|float32
var_1366 = relay.var("var_1366", dtype = "float64", shape = (144,))#candidate|1366|(144,)|var|float64
output = func_1364(var_1365,var_1366,)
func_1367 = relay.Function([var_1365,var_1366,], output)
mutated_mod['func_1367'] = func_1367
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2157 = relay.const([[[-7.899274,-3.445148,-0.567839,-5.195041,3.753204,-2.434984,7.989576,4.400078,9.789151,-9.694154,-7.819800],[-5.527497,2.165985,-0.228604,-6.397347,6.175979,-6.828839,-0.252150,-9.059109,-2.397024,-0.893219,-9.863701],[4.391090,4.223932,5.144856,-8.216708,-0.249950,7.796770,3.487555,-2.568721,-4.454532,-8.058735,-2.300644],[8.930184,-9.622037,-0.087655,2.192301,-5.165170,-4.279220,1.213195,7.752779,1.893329,-3.028303,2.787597],[-4.734318,9.325959,0.875446,-3.902404,-8.331137,-8.349071,5.686659,2.458192,1.959283,3.512906,4.685230],[7.423019,-3.654222,-1.666427,-3.825557,3.977161,-5.890008,2.402504,-5.893292,4.831071,4.385780,0.861705],[-1.318634,1.787614,-3.427620,2.383941,4.956106,-6.446282,2.461215,-1.957322,9.295506,-2.698270,1.888655],[8.798946,4.224887,-9.452621,8.851341,-1.308935,1.100710,2.145657,-5.191703,0.320951,-5.855759,-0.768318],[2.500314,3.051781,-6.190015,-7.660964,6.129989,0.794432,-1.407800,2.712103,-5.755077,9.657813,-6.744268],[5.218656,0.306675,-2.761724,9.548755,4.216105,-3.413509,0.754226,-9.063512,-1.938675,6.470215,3.556156]]], dtype = "float32")#candidate|2157|(1, 10, 11)|const|float32
uop_2158 = relay.acos(const_2157.astype('float32')) # shape=(1, 10, 11)
output = uop_2158
output2 = uop_2158
func_2168 = relay.Function([], output)
mod['func_2168'] = func_2168
mod = relay.transform.InferType()(mod)
mutated_mod['func_2168'] = func_2168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mutated_mod.get_global_var('func_2168')
call_2169 = func_2168_call()
output = call_2169
func_2170 = relay.Function([], output)
mutated_mod['func_2170'] = func_2170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_2210 = func_2168_call()
call_2211 = func_2168_call()
output = call_2210
output2 = call_2211
func_2220 = relay.Function([], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mutated_mod.get_global_var('func_2220')
call_2221 = func_2220_call()
output = call_2221
func_2222 = relay.Function([], output)
mutated_mod['func_2222'] = func_2222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2244 = relay.var("var_2244", dtype = "float64", shape = (1, 10, 4))#candidate|2244|(1, 10, 4)|var|float64
uop_2245 = relay.exp(var_2244.astype('float64')) # shape=(1, 10, 4)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_2247 = func_2220_call()
call_2248 = func_2220_call()
func_210_call = mod.get_global_var('func_210')
func_213_call = mutated_mod.get_global_var('func_213')
var_2254 = relay.var("var_2254", dtype = "float64", shape = (105, 3))#candidate|2254|(105, 3)|var|float64
var_2255 = relay.var("var_2255", dtype = "float64", shape = (140,))#candidate|2255|(140,)|var|float64
call_2253 = relay.TupleGetItem(func_210_call(relay.reshape(var_2254.astype('float64'), [15, 3, 7]), relay.reshape(var_2255.astype('float64'), [140,]), ), 0)
call_2256 = relay.TupleGetItem(func_213_call(relay.reshape(var_2254.astype('float64'), [15, 3, 7]), relay.reshape(var_2255.astype('float64'), [140,]), ), 0)
func_1364_call = mod.get_global_var('func_1364')
func_1367_call = mutated_mod.get_global_var('func_1367')
var_2278 = relay.var("var_2278", dtype = "float32", shape = (36, 12))#candidate|2278|(36, 12)|var|float32
var_2279 = relay.var("var_2279", dtype = "float64", shape = (144,))#candidate|2279|(144,)|var|float64
call_2277 = relay.TupleGetItem(func_1364_call(relay.reshape(var_2278.astype('float32'), [3, 12, 12]), relay.reshape(var_2279.astype('float64'), [144,]), ), 2)
call_2280 = relay.TupleGetItem(func_1367_call(relay.reshape(var_2278.astype('float32'), [3, 12, 12]), relay.reshape(var_2279.astype('float64'), [144,]), ), 2)
bop_2286 = relay.bitwise_and(uop_2245.astype('int16'), relay.reshape(var_2244.astype('int16'), relay.shape_of(uop_2245))) # shape=(1, 10, 4)
output = relay.Tuple([call_2247,call_2253,var_2254,var_2255,call_2277,var_2278,var_2279,bop_2286,])
output2 = relay.Tuple([call_2248,call_2256,var_2254,var_2255,call_2280,var_2278,var_2279,bop_2286,])
func_2295 = relay.Function([var_2244,var_2254,var_2255,var_2278,var_2279,], output)
mod['func_2295'] = func_2295
mod = relay.transform.InferType()(mod)
var_2296 = relay.var("var_2296", dtype = "float64", shape = (1, 10, 4))#candidate|2296|(1, 10, 4)|var|float64
var_2297 = relay.var("var_2297", dtype = "float64", shape = (105, 3))#candidate|2297|(105, 3)|var|float64
var_2298 = relay.var("var_2298", dtype = "float64", shape = (140,))#candidate|2298|(140,)|var|float64
var_2299 = relay.var("var_2299", dtype = "float32", shape = (36, 12))#candidate|2299|(36, 12)|var|float32
var_2300 = relay.var("var_2300", dtype = "float64", shape = (144,))#candidate|2300|(144,)|var|float64
output = func_2295(var_2296,var_2297,var_2298,var_2299,var_2300,)
func_2301 = relay.Function([var_2296,var_2297,var_2298,var_2299,var_2300,], output)
mutated_mod['func_2301'] = func_2301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_2313 = func_2168_call()
call_2314 = func_2168_call()
func_1285_call = mod.get_global_var('func_1285')
func_1290_call = mutated_mod.get_global_var('func_1290')
var_2330 = relay.var("var_2330", dtype = "bool", shape = (80,))#candidate|2330|(80,)|var|bool
const_2331 = relay.const([False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False], dtype = "bool")#candidate|2331|(1200,)|const|bool
call_2329 = relay.TupleGetItem(func_1285_call(relay.reshape(var_2330.astype('bool'), [8, 10, 1]), relay.reshape(const_2331.astype('bool'), [8, 10, 15]), relay.reshape(const_2331.astype('bool'), [8, 10, 15]), ), 1)
call_2332 = relay.TupleGetItem(func_1290_call(relay.reshape(var_2330.astype('bool'), [8, 10, 1]), relay.reshape(const_2331.astype('bool'), [8, 10, 15]), relay.reshape(const_2331.astype('bool'), [8, 10, 15]), ), 1)
output = relay.Tuple([call_2313,call_2329,var_2330,const_2331,])
output2 = relay.Tuple([call_2314,call_2332,var_2330,const_2331,])
func_2340 = relay.Function([var_2330,], output)
mod['func_2340'] = func_2340
mod = relay.transform.InferType()(mod)
var_2341 = relay.var("var_2341", dtype = "bool", shape = (80,))#candidate|2341|(80,)|var|bool
output = func_2340(var_2341)
func_2342 = relay.Function([var_2341], output)
mutated_mod['func_2342'] = func_2342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_2350 = func_2220_call()
call_2351 = func_2220_call()
func_106_call = mod.get_global_var('func_106')
func_109_call = mutated_mod.get_global_var('func_109')
var_2360 = relay.var("var_2360", dtype = "float64", shape = (140,))#candidate|2360|(140,)|var|float64
call_2359 = relay.TupleGetItem(func_106_call(relay.reshape(var_2360.astype('float64'), [5, 2, 14])), 0)
call_2361 = relay.TupleGetItem(func_109_call(relay.reshape(var_2360.astype('float64'), [5, 2, 14])), 0)
output = relay.Tuple([call_2350,call_2359,var_2360,])
output2 = relay.Tuple([call_2351,call_2361,var_2360,])
func_2368 = relay.Function([var_2360,], output)
mod['func_2368'] = func_2368
mod = relay.transform.InferType()(mod)
mutated_mod['func_2368'] = func_2368
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2369 = relay.var("var_2369", dtype = "float64", shape = (140,))#candidate|2369|(140,)|var|float64
func_2368_call = mutated_mod.get_global_var('func_2368')
call_2370 = func_2368_call(var_2369)
output = call_2370
func_2371 = relay.Function([var_2369], output)
mutated_mod['func_2371'] = func_2371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_2384 = func_2168_call()
call_2385 = func_2168_call()
func_1364_call = mod.get_global_var('func_1364')
func_1367_call = mutated_mod.get_global_var('func_1367')
var_2389 = relay.var("var_2389", dtype = "float32", shape = (432,))#candidate|2389|(432,)|var|float32
var_2390 = relay.var("var_2390", dtype = "float64", shape = (144,))#candidate|2390|(144,)|var|float64
call_2388 = relay.TupleGetItem(func_1364_call(relay.reshape(var_2389.astype('float32'), [3, 12, 12]), relay.reshape(var_2390.astype('float64'), [144,]), ), 0)
call_2391 = relay.TupleGetItem(func_1367_call(relay.reshape(var_2389.astype('float32'), [3, 12, 12]), relay.reshape(var_2390.astype('float64'), [144,]), ), 0)
output = relay.Tuple([call_2384,call_2388,var_2389,var_2390,])
output2 = relay.Tuple([call_2385,call_2391,var_2389,var_2390,])
func_2402 = relay.Function([var_2389,var_2390,], output)
mod['func_2402'] = func_2402
mod = relay.transform.InferType()(mod)
var_2403 = relay.var("var_2403", dtype = "float32", shape = (432,))#candidate|2403|(432,)|var|float32
var_2404 = relay.var("var_2404", dtype = "float64", shape = (144,))#candidate|2404|(144,)|var|float64
output = func_2402(var_2403,var_2404,)
func_2405 = relay.Function([var_2403,var_2404,], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_2451 = func_2220_call()
call_2452 = func_2220_call()
func_613_call = mod.get_global_var('func_613')
func_616_call = mutated_mod.get_global_var('func_616')
var_2460 = relay.var("var_2460", dtype = "float64", shape = (144,))#candidate|2460|(144,)|var|float64
call_2459 = relay.TupleGetItem(func_613_call(relay.reshape(var_2460.astype('float64'), [16, 3, 3])), 0)
call_2461 = relay.TupleGetItem(func_616_call(relay.reshape(var_2460.astype('float64'), [16, 3, 3])), 0)
func_589_call = mod.get_global_var('func_589')
func_591_call = mutated_mod.get_global_var('func_591')
var_2473 = relay.var("var_2473", dtype = "float64", shape = (390, 2))#candidate|2473|(390, 2)|var|float64
call_2472 = func_589_call(relay.reshape(var_2473.astype('float64'), [13, 15, 4]))
call_2474 = func_589_call(relay.reshape(var_2473.astype('float64'), [13, 15, 4]))
func_106_call = mod.get_global_var('func_106')
func_109_call = mutated_mod.get_global_var('func_109')
var_2477 = relay.var("var_2477", dtype = "float64", shape = (5, 28))#candidate|2477|(5, 28)|var|float64
call_2476 = relay.TupleGetItem(func_106_call(relay.reshape(var_2477.astype('float64'), [5, 2, 14])), 0)
call_2478 = relay.TupleGetItem(func_109_call(relay.reshape(var_2477.astype('float64'), [5, 2, 14])), 0)
output = relay.Tuple([call_2451,call_2459,var_2460,call_2472,var_2473,call_2476,var_2477,])
output2 = relay.Tuple([call_2452,call_2461,var_2460,call_2474,var_2473,call_2478,var_2477,])
func_2479 = relay.Function([var_2460,var_2473,var_2477,], output)
mod['func_2479'] = func_2479
mod = relay.transform.InferType()(mod)
mutated_mod['func_2479'] = func_2479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2479_call = mutated_mod.get_global_var('func_2479')
var_2481 = relay.var("var_2481", dtype = "float64", shape = (144,))#candidate|2481|(144,)|var|float64
var_2482 = relay.var("var_2482", dtype = "float64", shape = (390, 2))#candidate|2482|(390, 2)|var|float64
var_2483 = relay.var("var_2483", dtype = "float64", shape = (5, 28))#candidate|2483|(5, 28)|var|float64
call_2480 = func_2479_call(var_2481,var_2482,var_2483,)
output = call_2480
func_2484 = relay.Function([var_2481,var_2482,var_2483,], output)
mutated_mod['func_2484'] = func_2484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_2542 = func_2220_call()
call_2543 = func_2220_call()
func_210_call = mod.get_global_var('func_210')
func_213_call = mutated_mod.get_global_var('func_213')
const_2558 = relay.const([[3.369952,5.163713,-5.783567,-3.055057,3.261823,-9.503930,-4.639214,9.760039,-8.542043],[-6.624505,-8.065037,-0.595144,-9.997506,-5.354267,6.962647,3.071779,3.205758,3.107467],[3.529478,5.468546,-0.807471,-5.327101,-7.140302,-4.694015,8.062457,3.136999,-3.607497],[-5.228964,-2.393787,6.341519,6.858822,-5.338642,8.451414,-8.850578,-3.652416,2.239796],[-0.694530,4.231040,3.145640,3.489697,9.867750,0.795751,-2.147408,-7.973071,-8.332432],[-3.081049,-3.066476,-5.451365,5.318827,3.231248,4.833947,-1.551412,-7.811361,-3.544756],[0.847560,-9.038440,4.016882,-8.630034,-8.449947,-6.951356,-8.281043,-6.284054,4.183549],[-3.713847,-8.144514,-5.857878,-2.013124,9.016376,7.484646,7.386665,9.145696,9.934847],[9.691727,3.810698,-2.815935,-4.636930,-0.411635,-9.373720,4.599046,-1.633786,-7.998396],[7.292766,1.635204,3.081814,0.366946,-8.206517,-1.064794,2.871575,9.724126,8.314008],[-7.766955,5.925657,0.169181,-9.937385,-8.701938,-7.036194,-0.084315,-9.873266,-4.819901],[-0.368698,-5.416084,-7.658327,-8.834368,-7.923971,-1.405556,7.041337,3.124656,-5.140770],[-8.217548,3.484708,9.881057,9.462065,-1.335137,-3.427767,6.812498,-2.246891,0.547553],[2.232931,-4.166379,4.285526,5.994346,2.733031,9.989249,6.486187,-7.917340,0.037505],[-8.419011,1.035220,-2.515627,9.996506,-9.223038,8.737588,8.426282,9.592418,-2.166623],[-2.722090,-7.578101,-3.580178,9.828164,9.317345,-1.140661,-2.890843,-5.275927,8.564906],[3.427895,-8.078152,-9.582478,2.798516,-7.568347,8.097838,0.769824,5.637670,0.426184],[-0.199222,0.909776,5.912868,-8.926844,0.711004,5.242341,9.679370,6.459252,9.440353],[2.130252,7.938175,4.517388,-1.654610,3.144148,-1.090859,6.173751,9.459998,6.687782],[-6.529648,-7.093870,-9.057176,5.535137,-3.294561,0.556743,-2.926185,-6.111832,1.843303],[4.941198,9.832218,8.459659,0.468818,-8.516852,0.121039,3.886277,1.152686,0.800790],[-7.443354,3.315985,-6.369566,-1.447362,6.334140,-2.277513,-1.024314,-6.152537,-3.753706],[-4.203748,-9.144498,6.276149,-2.098582,4.089270,-3.877562,1.701773,4.198539,-4.023637],[7.430713,8.175154,9.121859,3.584552,4.491545,4.718971,8.932145,5.893704,-4.996232],[-9.831256,-8.412326,-1.564989,-1.131334,7.205450,-8.604986,2.650145,-9.369192,-2.138944],[0.323487,3.230085,3.133896,-5.553523,-0.875034,-0.815390,-6.354902,3.333430,9.641090],[-7.915324,4.393993,1.539891,6.046559,-3.764653,1.206227,8.886324,-2.048139,2.693533],[-7.275728,2.190062,-3.743198,3.005101,-3.795818,6.600968,3.118288,1.475809,3.732167],[-4.586269,-0.709934,-5.430364,-7.603516,-7.879636,-6.780817,-9.694024,5.666704,-9.328238],[-8.724286,2.708128,-5.244995,-1.106095,-2.398547,2.440211,-1.336943,-3.104369,-6.186591],[7.313137,-4.287418,1.752172,9.576553,6.155397,1.301627,-5.911845,-3.867772,-6.470299],[-2.881081,-1.032535,8.509340,-7.593855,0.740458,-0.441915,6.530611,-9.775762,8.482798],[5.394832,-7.717763,3.119986,-5.608457,9.288678,3.322877,5.519269,-9.068287,-2.325859],[8.837232,8.200823,9.725251,-8.435015,4.212032,7.344972,9.146028,-2.432720,0.536354],[3.577417,4.819636,-8.787221,1.740234,1.131957,9.757588,0.525221,-5.510000,-4.738897]], dtype = "float64")#candidate|2558|(35, 9)|const|float64
var_2559 = relay.var("var_2559", dtype = "float64", shape = (140,))#candidate|2559|(140,)|var|float64
call_2557 = relay.TupleGetItem(func_210_call(relay.reshape(const_2558.astype('float64'), [15, 3, 7]), relay.reshape(var_2559.astype('float64'), [140,]), ), 0)
call_2560 = relay.TupleGetItem(func_213_call(relay.reshape(const_2558.astype('float64'), [15, 3, 7]), relay.reshape(var_2559.astype('float64'), [140,]), ), 0)
var_2565 = relay.var("var_2565", dtype = "float32", shape = (13, 10, 11))#candidate|2565|(13, 10, 11)|var|float32
bop_2566 = relay.not_equal(call_2542.astype('bool'), var_2565.astype('bool')) # shape=(13, 10, 11)
bop_2569 = relay.not_equal(call_2543.astype('bool'), var_2565.astype('bool')) # shape=(13, 10, 11)
func_106_call = mod.get_global_var('func_106')
func_109_call = mutated_mod.get_global_var('func_109')
call_2581 = relay.TupleGetItem(func_106_call(relay.reshape(var_2559.astype('float64'), [5, 2, 14])), 0)
call_2582 = relay.TupleGetItem(func_109_call(relay.reshape(var_2559.astype('float64'), [5, 2, 14])), 0)
bop_2604 = relay.greater(const_2558.astype('bool'), relay.reshape(call_2557.astype('bool'), relay.shape_of(const_2558))) # shape=(35, 9)
bop_2607 = relay.greater(const_2558.astype('bool'), relay.reshape(call_2560.astype('bool'), relay.shape_of(const_2558))) # shape=(35, 9)
var_2640 = relay.var("var_2640", dtype = "bool", shape = (35, 9))#candidate|2640|(35, 9)|var|bool
bop_2641 = relay.less(bop_2604.astype('bool'), relay.reshape(var_2640.astype('bool'), relay.shape_of(bop_2604))) # shape=(35, 9)
bop_2644 = relay.less(bop_2607.astype('bool'), relay.reshape(var_2640.astype('bool'), relay.shape_of(bop_2607))) # shape=(35, 9)
var_2649 = relay.var("var_2649", dtype = "float32", shape = (13, 10, 11))#candidate|2649|(13, 10, 11)|var|float32
bop_2650 = relay.greater_equal(var_2565.astype('bool'), relay.reshape(var_2649.astype('bool'), relay.shape_of(var_2565))) # shape=(13, 10, 11)
output = relay.Tuple([var_2559,bop_2566,call_2581,bop_2641,bop_2650,])
output2 = relay.Tuple([var_2559,bop_2569,call_2582,bop_2644,bop_2650,])
func_2653 = relay.Function([var_2559,var_2565,var_2640,var_2649,], output)
mod['func_2653'] = func_2653
mod = relay.transform.InferType()(mod)
mutated_mod['func_2653'] = func_2653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2653_call = mutated_mod.get_global_var('func_2653')
var_2655 = relay.var("var_2655", dtype = "float64", shape = (140,))#candidate|2655|(140,)|var|float64
var_2656 = relay.var("var_2656", dtype = "float32", shape = (13, 10, 11))#candidate|2656|(13, 10, 11)|var|float32
var_2657 = relay.var("var_2657", dtype = "bool", shape = (35, 9))#candidate|2657|(35, 9)|var|bool
var_2658 = relay.var("var_2658", dtype = "float32", shape = (13, 10, 11))#candidate|2658|(13, 10, 11)|var|float32
call_2654 = func_2653_call(var_2655,var_2656,var_2657,var_2658,)
output = call_2654
func_2659 = relay.Function([var_2655,var_2656,var_2657,var_2658,], output)
mutated_mod['func_2659'] = func_2659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_2699 = func_2220_call()
call_2700 = func_2220_call()
var_2702 = relay.var("var_2702", dtype = "float32", shape = (5, 10, 11))#candidate|2702|(5, 10, 11)|var|float32
bop_2703 = relay.bitwise_xor(call_2699.astype('uint8'), var_2702.astype('uint8')) # shape=(5, 10, 11)
bop_2706 = relay.bitwise_xor(call_2700.astype('uint8'), var_2702.astype('uint8')) # shape=(5, 10, 11)
output = bop_2703
output2 = bop_2706
func_2707 = relay.Function([var_2702,], output)
mod['func_2707'] = func_2707
mod = relay.transform.InferType()(mod)
var_2708 = relay.var("var_2708", dtype = "float32", shape = (5, 10, 11))#candidate|2708|(5, 10, 11)|var|float32
output = func_2707(var_2708)
func_2709 = relay.Function([var_2708], output)
mutated_mod['func_2709'] = func_2709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_2722 = func_2168_call()
call_2723 = func_2168_call()
output = call_2722
output2 = call_2723
func_2758 = relay.Function([], output)
mod['func_2758'] = func_2758
mod = relay.transform.InferType()(mod)
output = func_2758()
func_2759 = relay.Function([], output)
mutated_mod['func_2759'] = func_2759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_2773 = func_2168_call()
call_2774 = func_2168_call()
func_589_call = mod.get_global_var('func_589')
func_591_call = mutated_mod.get_global_var('func_591')
const_2789 = relay.const([[-8.452414,1.268438,8.000040,-3.738693,2.522433,-9.239894,-8.415688,8.553935,-4.558340,-1.942316,0.670196,7.520567,1.102405,3.412969,-8.198024,6.986506,-8.847069,9.541443,-9.496314,0.837306,-2.008531,-9.952324,-1.660721,-3.723528,9.729850,1.723901,8.070326,8.760450,3.559935,-5.051696,4.027274,-9.403886,1.782885,-8.401564,-2.676781,0.536902,2.066157,1.685126,-3.154947,-0.864799,-1.844998,-7.373663,-9.625612,-1.432218,-1.037245,3.514735,9.918435,2.095702,4.554046,-1.145242,1.380686,-2.104624,9.633696,1.820988,-6.991196,-2.936494,4.796317,-8.433865,-3.276183,9.816199,1.529668,2.127100,6.420675,7.394861,-2.323463,-3.442089,-0.380914,-1.288408,-9.631784,4.446258,1.196231,-8.598824,-6.003217,-2.248009,0.261790,9.256259,-7.090946,4.282552],[8.343803,8.352641,2.885611,7.347291,-1.117230,3.693507,9.274447,1.642704,-0.925849,2.934688,-9.054771,-6.419350,-0.442648,1.660866,-0.722867,-2.219485,3.740802,4.830477,5.071979,-2.004118,-2.156453,-8.259653,-7.387613,-2.152107,2.403582,5.375948,8.172788,-4.624644,5.481658,-0.764048,-9.836710,3.257527,-5.372152,-2.085121,-9.733324,-8.686526,9.998898,-6.523150,-3.868058,-9.867691,7.913005,-5.738894,1.882351,-4.092963,-4.890673,-9.794589,4.071725,-6.516895,-4.393567,2.162779,-9.890395,6.949097,-5.953413,7.514446,-5.276126,0.564054,-9.552308,-8.169933,-8.607621,-7.288345,-6.351028,3.426511,4.546091,2.608094,8.457082,-8.738922,-0.532163,6.143829,5.914806,-8.410413,-3.299912,6.829708,4.967161,1.306527,-6.464715,-5.843849,-8.903490,-6.768569],[9.981013,-4.088285,-4.048499,-5.855820,-8.642966,-4.749472,4.838215,-3.192570,-0.796139,-2.041371,5.911412,1.233114,9.933968,-7.686938,9.734074,1.006191,3.308810,6.304185,-1.815966,-3.096445,6.833346,5.834614,1.591530,7.996098,3.590848,6.442046,5.858170,6.769261,-6.409762,-6.593906,-9.870393,6.546240,4.806946,-3.330496,-1.650437,4.085717,7.858485,-2.657652,-9.327581,-0.169879,1.109226,-8.797314,-8.486536,-6.784702,-0.683606,-2.228221,-7.450907,-0.023876,7.153644,-0.602129,2.676443,8.333291,-1.387664,-4.567185,8.360204,-9.330105,-3.038410,7.004529,-2.241115,-3.669665,7.753692,-3.627497,-9.739843,6.648791,9.471436,7.394748,8.057632,2.002531,1.443464,-2.155787,-0.536552,8.059249,-1.761438,4.184232,-8.911904,5.524241,-7.813781,-0.122755],[-3.085825,-6.197897,4.062555,-0.829765,4.081248,-9.961139,4.993756,4.958593,2.865177,4.186071,-3.732531,4.015987,-0.129356,-6.820639,-8.639810,1.178369,-4.192383,-6.091480,6.033993,2.926629,-9.390094,0.514582,-8.303621,8.392020,-0.137103,3.571761,2.545507,2.602746,1.081051,-8.195095,-4.926486,-3.600831,-1.905231,-9.132755,-7.802174,-5.002702,9.393348,-6.593049,-5.268227,-1.185014,-7.413962,1.825028,-7.731772,8.481958,-7.345815,1.962035,0.387544,-6.721728,-8.972931,-6.629057,-6.057389,7.938223,-5.215174,0.617535,5.642015,0.169607,-1.193885,4.904416,-3.182409,-6.766455,-0.649964,3.350479,-8.030581,9.918673,8.863507,7.709871,-4.160402,8.117524,-2.089546,-5.350548,-7.383911,-9.116682,-3.882560,5.937995,-5.338526,-8.385663,1.275428,0.603234],[2.090094,-0.154588,-0.514426,-9.179275,-6.344854,9.223085,-7.348376,-7.852449,-5.660042,5.074684,-9.922786,6.076256,5.497789,-0.852052,1.408747,-3.774446,-5.001928,0.345178,-9.493796,-2.222310,-9.030923,5.798182,8.355008,4.447799,-1.544453,-0.846420,-0.529576,-1.401350,7.412097,-7.250499,-5.685725,5.160651,-6.224231,6.471024,-3.235846,5.889541,2.772201,-6.476512,1.219352,-6.546032,-9.581764,-9.000552,-6.341097,-4.225395,5.863217,3.468407,9.474681,8.262400,3.112273,-3.310110,-5.505382,-7.047806,3.845109,-4.620419,8.695171,-7.349536,6.233012,-9.854098,8.953893,-6.014743,2.535311,-9.920789,-1.817843,-6.859576,-4.922394,-3.126380,6.469379,3.088431,0.391759,1.535436,-0.016738,-9.629556,-0.802760,-5.693736,-2.495134,5.874509,-4.300047,-4.869210],[5.254488,-7.019459,-3.192378,-9.384681,-5.582679,-6.222430,7.193167,-3.762521,9.662355,9.368350,1.137487,-0.053597,-6.299486,4.933770,0.436846,-3.929823,5.324425,9.357922,6.982111,9.915967,0.408081,1.540942,0.010003,-6.408968,-3.427814,-7.857519,9.528842,6.379834,-6.574910,-5.943055,7.079574,-1.879224,-9.985738,-7.048211,1.132655,1.477167,9.706733,2.100152,-1.162678,8.192769,-6.524777,-3.314424,-7.144555,9.591291,-1.611028,9.087486,-7.330658,-0.661858,9.868874,-8.122155,-3.643367,2.372217,-6.036864,-4.760411,-2.613587,-1.122672,-8.362468,5.573383,-4.062138,9.952665,-7.013161,-3.645740,8.045164,9.543554,6.547873,5.646447,7.835691,8.183194,-3.866288,-1.367298,-8.354971,9.088211,3.359367,7.837503,4.347804,6.528850,7.474896,4.337377],[-8.342225,8.035981,-7.449566,-6.951928,6.285014,-7.687887,3.877160,6.612051,8.830462,-3.971327,3.513764,-4.890157,7.925770,-7.185983,-8.501726,1.068436,2.508418,-7.296748,3.710911,1.068796,2.464956,-2.731855,4.235513,-1.779278,-3.880571,8.780405,-1.844773,2.098798,8.068362,2.088591,5.900837,4.973590,6.587458,-3.519864,-0.971991,-2.999820,9.043313,-4.971199,-5.194965,6.569977,-0.838473,-4.404977,3.549893,-7.336406,8.695668,-4.487071,-9.723943,5.558488,8.445980,-0.176626,-2.478011,7.107925,-5.191575,-0.908667,-1.204717,8.754913,-8.322635,-2.184703,2.356403,5.365279,-2.182723,8.325957,6.858398,-1.980232,9.235491,-0.746702,6.360288,7.615706,9.323769,-2.396773,-3.815384,-4.686868,8.669697,-4.034143,3.533044,-8.457531,3.665061,-5.200297],[-2.469072,7.868434,-3.131170,7.025580,-3.183044,8.723383,-2.669357,4.252204,3.599350,-1.398815,-9.670914,-0.723071,-0.623310,3.233201,-1.121963,-2.087348,3.861754,-6.360446,2.113627,5.012262,7.629233,1.910124,5.362515,-0.274191,2.151768,3.250304,4.631663,4.499574,-6.175612,2.012477,6.431300,-3.810477,1.146180,-0.430456,-8.504119,-1.050786,-7.448305,-6.819669,5.764752,-2.637026,3.313531,-7.465627,9.053266,-9.339326,0.829322,4.256040,2.952612,9.593946,-4.725955,9.128349,7.352803,-2.788251,4.693575,4.841676,5.313593,4.240171,-5.007138,0.298586,-8.237159,1.758753,7.868958,-2.213393,-1.403880,-7.565910,0.913590,-5.421236,4.862709,-4.072196,9.158347,6.307269,7.272859,0.144730,2.132297,-6.899611,-0.575514,7.606600,-9.088269,-8.020280],[0.610030,0.765231,-9.430833,2.659016,5.637826,-6.994365,-2.930144,2.539903,1.364786,6.001305,-0.280763,-8.612145,3.172471,-0.620351,8.392154,4.830606,0.856602,4.623831,-6.497179,-4.536498,-8.114282,-3.141408,-8.334242,-8.434834,-7.173644,-2.040698,2.832711,7.458485,-5.024884,-3.376497,-9.127188,-9.153707,0.237360,9.443167,0.609120,6.120139,-6.992551,-8.446762,5.453350,-1.875960,-0.322714,-2.218152,1.866181,-7.496007,-6.339385,4.923916,-5.108811,-7.229923,6.969039,3.862752,0.762792,-9.260546,-3.630238,3.460104,-1.392462,5.824751,-0.178775,-3.141502,2.347453,-5.901461,-6.825910,-1.110339,8.681674,-9.630077,-6.631001,2.230364,-7.168647,-8.157008,-4.392171,-6.659015,6.493987,4.535776,-7.501709,-1.839071,7.828622,1.516277,-6.977472,-7.349973],[-7.085459,7.026450,3.578810,1.554630,-4.180356,-1.188093,8.564563,5.526912,8.297772,-9.342780,2.631737,7.020236,1.899117,-3.385134,8.844088,-0.611146,0.129316,-3.199928,-6.666292,-1.054738,3.780124,-1.690207,8.506893,-6.613086,-1.747028,-6.583398,9.425786,-1.122109,-3.438447,-3.318253,-5.966677,-5.669280,-6.816751,-5.088861,-6.380097,-5.575710,8.335459,-1.600005,-9.042309,5.800872,8.962952,-4.348980,-9.575177,-5.230069,9.811761,-6.824085,6.525970,5.696780,7.668760,-7.729729,-0.353205,-5.948051,4.906505,2.905703,6.744187,0.234606,-1.824446,1.523413,-7.295962,-3.698762,-4.966093,5.525121,0.438444,-4.301008,-5.924074,-9.325868,2.775299,4.190431,1.758705,-6.023261,3.360401,6.748711,-6.252944,-5.328232,-3.657333,-7.637967,9.285185,-6.611702]], dtype = "float64")#candidate|2789|(10, 78)|const|float64
call_2788 = func_589_call(relay.reshape(const_2789.astype('float64'), [13, 15, 4]))
call_2790 = func_589_call(relay.reshape(const_2789.astype('float64'), [13, 15, 4]))
output = relay.Tuple([call_2773,call_2788,const_2789,])
output2 = relay.Tuple([call_2774,call_2790,const_2789,])
func_2805 = relay.Function([], output)
mod['func_2805'] = func_2805
mod = relay.transform.InferType()(mod)
output = func_2805()
func_2806 = relay.Function([], output)
mutated_mod['func_2806'] = func_2806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_2829 = func_2168_call()
call_2830 = func_2168_call()
output = call_2829
output2 = call_2830
func_2835 = relay.Function([], output)
mod['func_2835'] = func_2835
mod = relay.transform.InferType()(mod)
output = func_2835()
func_2836 = relay.Function([], output)
mutated_mod['func_2836'] = func_2836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_3051 = func_2220_call()
call_3052 = func_2220_call()
output = relay.Tuple([call_3051,])
output2 = relay.Tuple([call_3052,])
func_3064 = relay.Function([], output)
mod['func_3064'] = func_3064
mod = relay.transform.InferType()(mod)
output = func_3064()
func_3065 = relay.Function([], output)
mutated_mod['func_3065'] = func_3065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2805_call = mod.get_global_var('func_2805')
func_2806_call = mutated_mod.get_global_var('func_2806')
call_3071 = relay.TupleGetItem(func_2805_call(), 0)
call_3072 = relay.TupleGetItem(func_2806_call(), 0)
func_2707_call = mod.get_global_var('func_2707')
func_2709_call = mutated_mod.get_global_var('func_2709')
const_3084 = relay.const([5.429846,-7.352086,-5.889483,7.287513,-6.559584,-9.095833,8.225090,7.343726,4.718907,8.602643,-0.918009,-3.250323,-8.987051,-9.381722,0.436467,-8.063839,-9.491677,8.860888,-9.428758,-3.526037,9.993042,8.546888,7.243533,-7.546027,4.141126,6.888658,-9.470604,5.232673,0.708181,-3.484044,7.173440,2.610209,1.212361,5.876280,7.076467,0.098399,-5.899682,1.408648,3.878347,-7.351872,9.631772,-4.113905,3.450732,-5.197008,9.272979,-1.139722,-6.327974,-7.849602,-1.972958,7.445428,-7.683559,-2.719219,9.959566,-0.293374,-0.118120,6.847203,-4.152135,0.273496,9.545974,-5.124873,-6.421254,-2.772958,-0.802801,-0.569267,-4.238511,-3.696401,-4.270607,5.361776,-8.898631,-3.414519,-9.662250,5.006627,5.178949,5.020698,-4.922080,-8.652299,-7.405295,8.637802,1.542878,4.162613,3.359122,-3.267703,-2.005272,2.272235,1.831698,2.240412,-5.821430,7.523639,9.581899,-0.107357,-1.162184,-8.544916,9.265414,-0.859555,-7.591114,-1.628196,5.484169,6.396103,-6.269290,8.673714,2.954356,-0.163902,7.452858,0.451296,-9.249529,-2.185326,-7.849656,1.054911,9.858894,7.003602,2.561226,0.448058,-7.166633,-7.898024,-7.181318,7.257699,0.698272,5.372061,4.956977,9.994787,-7.946381,-7.027787,7.316063,5.677738,8.338268,-9.033515,-5.263398,-8.304755,-9.480475,-1.646331,-3.214507,-0.981873,9.075448,-4.354564,3.898106,-5.097493,2.538618,-9.500227,-1.544000,6.214616,-9.551295,-6.754133,-6.904485,-9.385963,2.721724,3.026615,-3.710509,4.099535,1.857685,-6.446471,-0.197072,-1.961770,1.011384,-8.990761,-0.827819,-4.887412,1.085386,-2.639157,5.026319,-6.829661,8.502983,-1.427131,-9.241637,2.471366,1.811852,-2.394241,-2.421804,4.079823,4.410834,5.236150,-7.646238,7.270953,-8.046390,2.348284,-9.257335,-7.587195,2.267145,4.687384,0.369451,6.334535,-6.166471,-6.261593,-3.796351,-0.727572,8.171062,-5.220686,8.937026,9.705781,8.946446,4.653444,-0.416673,1.355314,-9.622943,6.981011,9.863674,-8.709691,-6.714988,-7.649337,5.827779,8.214730,-8.162632,-4.874825,5.258120,1.079828,-1.858430,-4.134983,-3.312847,-6.470198,-6.802084,-4.778826,-0.808035,9.266381,3.711771,2.187287,-2.971964,4.765009,-6.854083,3.455721,5.618736,-0.009615,9.227269,7.471990,-3.707014,6.411545,2.288987,-3.397742,-0.185789,1.453146,7.978060,-8.659209,2.320842,-3.804444,5.363256,7.212335,-1.372099,-6.897225,-9.335686,-8.563544,8.610854,4.563054,3.977397,-1.873114,7.681751,-4.375368,0.927881,-4.223832,-0.014021,-1.571419,-0.545903,2.940289,-9.361059,0.341221,7.890071,0.369208,4.453443,9.108479,3.509917,-0.007430,1.014339,8.263706,-0.991925,0.118573,7.810050,-2.105928,4.332526,-1.221274,-2.924538,-5.653325,5.370212,-5.897215,-9.298582,-2.077462,-7.494096,-8.287306,8.509799,-4.369698,-9.433898,-6.371664,6.562395,8.990347,-5.897667,-4.821369,4.931287,-5.727830,5.826936,2.637073,6.775321,3.547076,5.517128,2.130483,8.948297,-2.457635,-9.157757,0.201738,9.486321,-8.038880,6.979088,-3.363972,-8.503281,7.606067,-8.923568,2.969893,-2.555202,2.341373,9.909282,-9.031976,-0.205601,-7.626655,-8.731357,-1.616362,-4.842153,5.376169,-3.335500,5.279510,9.218167,-8.385487,8.138307,1.784018,-3.268319,5.507000,4.239443,-9.809062,-0.911386,-4.168853,1.516684,5.793725,-9.547590,0.948191,-1.507806,1.572154,2.465548,3.130131,7.408344,9.400063,8.129475,6.229866,-2.040722,-8.745345,-2.859856,5.075290,-7.946213,-5.982887,-9.802664,2.506244,-1.858349,-8.673867,-9.373982,-1.129671,-3.049952,4.511759,8.340517,-8.134173,-6.598832,-0.121110,-0.726582,-2.472930,-1.802385,6.587587,-4.044680,-3.069108,7.508603,1.071088,-1.768314,0.030405,9.591273,9.871994,-4.350185,-0.935019,-6.651316,4.907680,7.269027,7.760749,-2.001163,-0.772845,1.589930,3.837195,4.770077,-7.757400,0.636822,-9.206088,-0.792723,9.838648,9.508927,-0.969423,-7.775500,-7.052558,4.905750,-4.858078,-1.022042,5.969693,5.845181,-3.305583,0.596179,-4.093827,3.264682,0.099724,-1.005924,-7.413263,-3.298178,-1.293142,-7.328180,-4.232448,-3.067816,-5.670182,9.137903,8.206605,-7.937281,3.463274,-7.128486,-8.193941,-6.310286,-1.153198,-2.144065,7.842371,8.545755,-0.839064,-8.751597,9.117637,9.252778,-4.935263,6.544199,1.872671,7.619091,6.803830,-5.226520,6.388146,1.082398,-8.014380,-7.786148,3.005256,4.390750,-9.819690,-3.463634,-0.579124,0.942329,4.364600,-3.036691,-2.272388,2.920993,-5.134455,-4.066822,2.750652,7.389860,4.921096,7.906722,4.772875,-4.425501,-5.432069,1.530309,-0.129674,1.145175,-1.153607,-1.028879,-6.805347,-8.933827,-8.878999,-7.920706,7.608902,4.002435,-3.432201,7.299086,4.962976,6.103028,-3.515840,-0.425394,6.581665,-1.128161,-2.513791,-9.673581,5.952699,6.400010,7.750780,0.796790,9.226737,-3.013998,3.863876,3.900948,0.332014,-9.193235,2.784255,3.944249,1.300727,-3.934584,-6.471180,-1.771929,-6.120712,0.704302,7.074747,-0.244531,1.841901,-8.208463,-0.396493,0.027429,-6.365159,7.767702,9.359125,-7.684893,1.830353,-7.757925,-1.289327,5.807574,-1.443521,-6.863142,3.534814,-9.671377,5.099461,4.370851,-1.503232,-4.946929,-1.011495,-3.800914,-9.079477,-1.852040,-7.643342,0.947826,1.346066,9.323662,-1.507385,-4.794612,-2.032278,-1.136377,1.617590,6.438941,5.424091,5.359481,8.860019,4.459273,-6.808195,8.375968,-6.435863,3.193258,8.956814,9.760521,5.129748,6.658135,-1.587367,3.978649,3.670403,7.532607,-0.590213,2.915371,-6.155142,4.671689,-9.720119,6.918205,-3.443328,4.625620,2.952282,5.398176,-3.562517], dtype = "float32")#candidate|3084|(550,)|const|float32
call_3083 = func_2707_call(relay.reshape(const_3084.astype('float32'), [5, 10, 11]))
call_3085 = func_2707_call(relay.reshape(const_3084.astype('float32'), [5, 10, 11]))
output = relay.Tuple([call_3071,call_3083,const_3084,])
output2 = relay.Tuple([call_3072,call_3085,const_3084,])
func_3086 = relay.Function([], output)
mod['func_3086'] = func_3086
mod = relay.transform.InferType()(mod)
output = func_3086()
func_3087 = relay.Function([], output)
mutated_mod['func_3087'] = func_3087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_3088 = func_2758_call()
call_3089 = func_2758_call()
var_3090 = relay.var("var_3090", dtype = "float32", shape = (3, 10, 11))#candidate|3090|(3, 10, 11)|var|float32
bop_3091 = relay.floor_divide(call_3088.astype('float32'), var_3090.astype('float32')) # shape=(3, 10, 11)
bop_3094 = relay.floor_divide(call_3089.astype('float32'), var_3090.astype('float32')) # shape=(3, 10, 11)
output = bop_3091
output2 = bop_3094
func_3095 = relay.Function([var_3090,], output)
mod['func_3095'] = func_3095
mod = relay.transform.InferType()(mod)
var_3096 = relay.var("var_3096", dtype = "float32", shape = (3, 10, 11))#candidate|3096|(3, 10, 11)|var|float32
output = func_3095(var_3096)
func_3097 = relay.Function([var_3096], output)
mutated_mod['func_3097'] = func_3097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_3104 = func_2835_call()
call_3105 = func_2835_call()
output = relay.Tuple([call_3104,])
output2 = relay.Tuple([call_3105,])
func_3115 = relay.Function([], output)
mod['func_3115'] = func_3115
mod = relay.transform.InferType()(mod)
output = func_3115()
func_3116 = relay.Function([], output)
mutated_mod['func_3116'] = func_3116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2805_call = mod.get_global_var('func_2805')
func_2806_call = mutated_mod.get_global_var('func_2806')
call_3148 = relay.TupleGetItem(func_2805_call(), 2)
call_3149 = relay.TupleGetItem(func_2806_call(), 2)
output = call_3148
output2 = call_3149
func_3152 = relay.Function([], output)
mod['func_3152'] = func_3152
mod = relay.transform.InferType()(mod)
mutated_mod['func_3152'] = func_3152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3152_call = mutated_mod.get_global_var('func_3152')
call_3153 = func_3152_call()
output = call_3153
func_3154 = relay.Function([], output)
mutated_mod['func_3154'] = func_3154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_3157 = func_2758_call()
call_3158 = func_2758_call()
output = relay.Tuple([call_3157,])
output2 = relay.Tuple([call_3158,])
func_3161 = relay.Function([], output)
mod['func_3161'] = func_3161
mod = relay.transform.InferType()(mod)
output = func_3161()
func_3162 = relay.Function([], output)
mutated_mod['func_3162'] = func_3162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_3172 = func_2220_call()
call_3173 = func_2220_call()
var_3183 = relay.var("var_3183", dtype = "float32", shape = (7, 10, 11))#candidate|3183|(7, 10, 11)|var|float32
bop_3184 = relay.power(call_3172.astype('float32'), var_3183.astype('float32')) # shape=(7, 10, 11)
bop_3187 = relay.power(call_3173.astype('float32'), var_3183.astype('float32')) # shape=(7, 10, 11)
output = bop_3184
output2 = bop_3187
func_3188 = relay.Function([var_3183,], output)
mod['func_3188'] = func_3188
mod = relay.transform.InferType()(mod)
var_3189 = relay.var("var_3189", dtype = "float32", shape = (7, 10, 11))#candidate|3189|(7, 10, 11)|var|float32
output = func_3188(var_3189)
func_3190 = relay.Function([var_3189], output)
mutated_mod['func_3190'] = func_3190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_3198 = func_2220_call()
call_3199 = func_2220_call()
output = relay.Tuple([call_3198,])
output2 = relay.Tuple([call_3199,])
func_3218 = relay.Function([], output)
mod['func_3218'] = func_3218
mod = relay.transform.InferType()(mod)
output = func_3218()
func_3219 = relay.Function([], output)
mutated_mod['func_3219'] = func_3219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_3245 = relay.TupleGetItem(func_3064_call(), 0)
call_3246 = relay.TupleGetItem(func_3065_call(), 0)
output = relay.Tuple([call_3245,])
output2 = relay.Tuple([call_3246,])
func_3268 = relay.Function([], output)
mod['func_3268'] = func_3268
mod = relay.transform.InferType()(mod)
output = func_3268()
func_3269 = relay.Function([], output)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_3273 = relay.TupleGetItem(func_3268_call(), 0)
call_3274 = relay.TupleGetItem(func_3269_call(), 0)
func_613_call = mod.get_global_var('func_613')
func_616_call = mutated_mod.get_global_var('func_616')
const_3276 = relay.const([[4.019006,-8.976628,3.499157,-2.682017,-4.015465,-6.189315,6.099433,-5.318243,-4.051032,6.691350,5.455543,2.975744,1.161571,8.273617,6.724522,2.575997,-5.416202,8.156090,8.607209,5.920501,-3.778223,0.052512,2.310180,2.346894,7.975944,-9.402259,-5.672710,6.902710,-1.162592,-0.519417,-8.826009,-5.213434,8.517222,3.897623,0.122758,-4.919895],[-4.885259,-7.874341,5.073984,7.597998,-4.004310,6.400672,6.724271,-0.686641,5.358194,9.222618,-9.920300,8.125897,7.920245,4.675021,8.500979,9.854677,3.174623,1.354145,6.733215,3.791256,-0.249989,6.930733,5.827475,-1.524617,-6.280888,1.270190,5.424708,-5.291727,7.004841,-6.139299,3.844098,-5.973498,8.786574,-6.739824,-1.236960,-1.469399],[-0.919462,-0.748493,-4.707545,4.554581,-4.848401,8.367897,9.616662,0.509334,9.002032,6.354538,6.588213,1.051872,-5.544520,0.161170,9.255263,3.762714,1.492108,-4.002604,-8.090792,-0.217989,-0.054873,7.090817,8.724433,-0.232876,-9.365246,-4.067892,7.170179,-1.292040,7.564447,-3.068206,7.536893,-1.158399,8.120789,-4.133908,-5.168474,-6.710112],[8.642226,-2.426606,-7.408845,4.539205,8.921304,-7.889217,-1.234676,-6.766990,4.626090,-1.480078,-1.427555,5.094433,1.288932,-3.091141,2.716243,-9.179478,-2.858192,0.567589,0.265258,5.147460,-0.815991,2.655188,-9.059547,-0.109139,-0.058451,-1.341720,-0.463035,-4.407168,-2.204506,1.454240,-3.295941,-6.146392,7.040661,6.419183,-2.234589,8.177272]], dtype = "float64")#candidate|3276|(4, 36)|const|float64
call_3275 = relay.TupleGetItem(func_613_call(relay.reshape(const_3276.astype('float64'), [16, 3, 3])), 0)
call_3277 = relay.TupleGetItem(func_616_call(relay.reshape(const_3276.astype('float64'), [16, 3, 3])), 0)
func_2653_call = mod.get_global_var('func_2653')
func_2659_call = mutated_mod.get_global_var('func_2659')
const_3294 = relay.const([[-2.043956,9.294618,3.550149,3.377185],[2.811834,-6.156099,-6.792879,-9.255518],[-8.526618,-2.661547,-5.719691,-2.690321],[9.170811,0.775013,0.075271,8.883281],[0.898078,-7.375478,-3.124189,1.414077],[3.512922,-7.579192,-4.217053,9.505189],[2.056240,7.624775,4.487919,4.082294],[2.631707,2.992063,-2.126353,-9.740429],[8.232053,0.817988,6.503496,-2.703840],[-6.907119,-7.078527,8.656559,-7.864450],[9.387130,-0.958843,8.975144,9.333319],[8.853795,7.123327,2.735520,8.949993],[2.501264,2.131276,2.847461,7.830616],[-4.384727,2.378820,7.054763,-2.254306],[3.477196,3.433692,-0.608445,2.074457],[8.140575,-5.724463,-4.970842,-1.220928],[-1.285950,-3.728434,5.591822,2.314267],[8.676968,3.796434,-1.067746,6.049315],[-8.282965,6.677663,-0.546860,-3.881181],[3.422307,-9.170857,9.176721,6.315912],[-0.945608,5.366836,3.580845,-8.994827],[0.264909,2.374707,6.251535,8.036654],[-5.208631,6.153216,1.905646,-7.536131],[-2.698094,2.081985,6.699363,9.490730],[-6.438690,3.127567,4.041694,4.702623],[5.782893,0.974118,8.305189,8.353900],[2.575533,-7.547914,-0.915288,4.414848],[-1.058249,-4.608186,-2.310715,4.336404],[7.526342,-7.973862,-2.277104,6.565179],[9.919073,1.082672,-0.250851,-7.018531],[6.656652,-2.566865,6.978724,-1.722653],[-8.800251,-2.024480,-0.631203,-2.457197],[-7.297378,-9.657800,-3.518209,3.810172],[-5.944387,-2.124973,6.066319,-8.895933],[-3.159253,-8.514468,7.144262,4.848893]], dtype = "float64")#candidate|3294|(35, 4)|const|float64
var_3295 = relay.var("var_3295", dtype = "float32", shape = (1430, 1))#candidate|3295|(1430, 1)|var|float32
var_3296 = relay.var("var_3296", dtype = "bool", shape = (315,))#candidate|3296|(315,)|var|bool
call_3293 = relay.TupleGetItem(func_2653_call(relay.reshape(const_3294.astype('float64'), [140,]), relay.reshape(var_3295.astype('float32'), [13, 10, 11]), relay.reshape(var_3296.astype('bool'), [35, 9]), relay.reshape(var_3295.astype('float32'), [13, 10, 11]), ), 1)
call_3297 = relay.TupleGetItem(func_2659_call(relay.reshape(const_3294.astype('float64'), [140,]), relay.reshape(var_3295.astype('float32'), [13, 10, 11]), relay.reshape(var_3296.astype('bool'), [35, 9]), relay.reshape(var_3295.astype('float32'), [13, 10, 11]), ), 1)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_3299 = func_2835_call()
call_3300 = func_2835_call()
output = relay.Tuple([call_3273,call_3275,const_3276,call_3293,const_3294,var_3295,var_3296,call_3299,])
output2 = relay.Tuple([call_3274,call_3277,const_3276,call_3297,const_3294,var_3295,var_3296,call_3300,])
func_3304 = relay.Function([var_3295,var_3296,], output)
mod['func_3304'] = func_3304
mod = relay.transform.InferType()(mod)
var_3305 = relay.var("var_3305", dtype = "float32", shape = (1430, 1))#candidate|3305|(1430, 1)|var|float32
var_3306 = relay.var("var_3306", dtype = "bool", shape = (315,))#candidate|3306|(315,)|var|bool
output = func_3304(var_3305,var_3306,)
func_3307 = relay.Function([var_3305,var_3306,], output)
mutated_mod['func_3307'] = func_3307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3115_call = mod.get_global_var('func_3115')
func_3116_call = mutated_mod.get_global_var('func_3116')
call_3311 = relay.TupleGetItem(func_3115_call(), 0)
call_3312 = relay.TupleGetItem(func_3116_call(), 0)
var_3319 = relay.var("var_3319", dtype = "float32", shape = (1, 10, 11))#candidate|3319|(1, 10, 11)|var|float32
bop_3320 = relay.floor_divide(call_3311.astype('float32'), relay.reshape(var_3319.astype('float32'), relay.shape_of(call_3311))) # shape=(1, 10, 11)
bop_3323 = relay.floor_divide(call_3312.astype('float32'), relay.reshape(var_3319.astype('float32'), relay.shape_of(call_3312))) # shape=(1, 10, 11)
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
var_3328 = relay.var("var_3328", dtype = "float64", shape = (130, 6))#candidate|3328|(130, 6)|var|float64
call_3327 = relay.TupleGetItem(func_1222_call(relay.reshape(var_3328.astype('float64'), [780,])), 0)
call_3329 = relay.TupleGetItem(func_1225_call(relay.reshape(var_3328.astype('float64'), [780,])), 0)
bop_3331 = relay.not_equal(var_3319.astype('bool'), relay.reshape(call_3311.astype('bool'), relay.shape_of(var_3319))) # shape=(1, 10, 11)
bop_3334 = relay.not_equal(var_3319.astype('bool'), relay.reshape(call_3312.astype('bool'), relay.shape_of(var_3319))) # shape=(1, 10, 11)
var_3343 = relay.var("var_3343", dtype = "float32", shape = (6, 10, 11))#candidate|3343|(6, 10, 11)|var|float32
bop_3344 = relay.multiply(call_3311.astype('float64'), var_3343.astype('float64')) # shape=(6, 10, 11)
bop_3347 = relay.multiply(call_3312.astype('float64'), var_3343.astype('float64')) # shape=(6, 10, 11)
output = relay.Tuple([bop_3320,call_3327,var_3328,bop_3331,bop_3344,])
output2 = relay.Tuple([bop_3323,call_3329,var_3328,bop_3334,bop_3347,])
func_3349 = relay.Function([var_3319,var_3328,var_3343,], output)
mod['func_3349'] = func_3349
mod = relay.transform.InferType()(mod)
var_3350 = relay.var("var_3350", dtype = "float32", shape = (1, 10, 11))#candidate|3350|(1, 10, 11)|var|float32
var_3351 = relay.var("var_3351", dtype = "float64", shape = (130, 6))#candidate|3351|(130, 6)|var|float64
var_3352 = relay.var("var_3352", dtype = "float32", shape = (6, 10, 11))#candidate|3352|(6, 10, 11)|var|float32
output = func_3349(var_3350,var_3351,var_3352,)
func_3353 = relay.Function([var_3350,var_3351,var_3352,], output)
mutated_mod['func_3353'] = func_3353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_3422 = func_2168_call()
call_3423 = func_2168_call()
func_589_call = mod.get_global_var('func_589')
func_591_call = mutated_mod.get_global_var('func_591')
var_3425 = relay.var("var_3425", dtype = "float64", shape = (780,))#candidate|3425|(780,)|var|float64
call_3424 = func_589_call(relay.reshape(var_3425.astype('float64'), [13, 15, 4]))
call_3426 = func_589_call(relay.reshape(var_3425.astype('float64'), [13, 15, 4]))
output = relay.Tuple([call_3422,call_3424,var_3425,])
output2 = relay.Tuple([call_3423,call_3426,var_3425,])
func_3428 = relay.Function([var_3425,], output)
mod['func_3428'] = func_3428
mod = relay.transform.InferType()(mod)
mutated_mod['func_3428'] = func_3428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3429 = relay.var("var_3429", dtype = "float64", shape = (780,))#candidate|3429|(780,)|var|float64
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3430 = func_3428_call(var_3429)
output = call_3430
func_3431 = relay.Function([var_3429], output)
mutated_mod['func_3431'] = func_3431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_3502 = func_2835_call()
call_3503 = func_2835_call()
output = relay.Tuple([call_3502,])
output2 = relay.Tuple([call_3503,])
func_3507 = relay.Function([], output)
mod['func_3507'] = func_3507
mod = relay.transform.InferType()(mod)
output = func_3507()
func_3508 = relay.Function([], output)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_3559 = func_2758_call()
call_3560 = func_2758_call()
output = call_3559
output2 = call_3560
func_3584 = relay.Function([], output)
mod['func_3584'] = func_3584
mod = relay.transform.InferType()(mod)
mutated_mod['func_3584'] = func_3584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3584_call = mutated_mod.get_global_var('func_3584')
call_3585 = func_3584_call()
output = call_3585
func_3586 = relay.Function([], output)
mutated_mod['func_3586'] = func_3586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_3643 = relay.TupleGetItem(func_3064_call(), 0)
call_3644 = relay.TupleGetItem(func_3065_call(), 0)
output = relay.Tuple([call_3643,])
output2 = relay.Tuple([call_3644,])
func_3645 = relay.Function([], output)
mod['func_3645'] = func_3645
mod = relay.transform.InferType()(mod)
mutated_mod['func_3645'] = func_3645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3645_call = mutated_mod.get_global_var('func_3645')
call_3646 = func_3645_call()
output = call_3646
func_3647 = relay.Function([], output)
mutated_mod['func_3647'] = func_3647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3115_call = mod.get_global_var('func_3115')
func_3116_call = mutated_mod.get_global_var('func_3116')
call_3703 = relay.TupleGetItem(func_3115_call(), 0)
call_3704 = relay.TupleGetItem(func_3116_call(), 0)
output = call_3703
output2 = call_3704
func_3711 = relay.Function([], output)
mod['func_3711'] = func_3711
mod = relay.transform.InferType()(mod)
output = func_3711()
func_3712 = relay.Function([], output)
mutated_mod['func_3712'] = func_3712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_3713 = relay.TupleGetItem(func_3507_call(), 0)
call_3714 = relay.TupleGetItem(func_3508_call(), 0)
output = relay.Tuple([call_3713,])
output2 = relay.Tuple([call_3714,])
func_3730 = relay.Function([], output)
mod['func_3730'] = func_3730
mod = relay.transform.InferType()(mod)
output = func_3730()
func_3731 = relay.Function([], output)
mutated_mod['func_3731'] = func_3731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_3738 = relay.TupleGetItem(func_3218_call(), 0)
call_3739 = relay.TupleGetItem(func_3219_call(), 0)
func_3428_call = mod.get_global_var('func_3428')
func_3431_call = mutated_mod.get_global_var('func_3431')
const_3741 = relay.const([-2.431936,-6.317942,-5.467568,-3.734250,-9.580108,-4.544059,5.565907,9.000888,-8.896745,9.585584,0.098756,4.637087,2.598542,3.223106,3.251509,-5.188638,-1.007187,-9.346827,3.751287,4.481292,-2.464439,-5.629752,4.957355,7.068811,-9.670376,8.608024,1.006302,-9.701103,4.889367,5.394382,-9.595019,-5.782694,-8.356564,-2.115309,-7.382657,8.493440,6.704968,-1.596274,-9.687040,-5.302968,-1.603463,-2.014854,-1.728214,-4.183417,-1.642031,-9.114703,0.912198,6.534487,8.045549,-4.462697,-3.855790,-7.201458,0.058117,-4.187106,-2.356703,-9.219834,-3.426685,-0.487757,5.839978,-6.114441,-7.705306,9.455589,2.978334,-4.166613,-8.227816,-4.085835,-3.517557,-0.556439,2.278169,6.752500,2.519288,9.957847,6.351598,-8.735176,-4.525265,-9.195485,2.146872,1.508216,6.358349,6.488555,-8.569576,-6.964129,-7.976886,-8.503362,8.756004,3.252628,6.828897,-8.186550,-1.707706,8.147066,3.776911,6.890023,6.436454,5.161735,-2.002906,-2.680217,6.958878,-5.371235,5.586226,6.960842,-3.596365,1.229224,6.386774,-1.881955,-4.269474,0.954461,-8.403780,-4.877854,6.322838,-4.216121,-3.710202,-7.606582,0.367533,7.806353,8.714278,5.948091,0.850005,1.644817,-0.515374,-1.394799,0.448965,-1.428405,3.160366,-5.530556,-7.250313,-9.381452,4.894111,-3.419726,7.786935,-0.247227,9.939633,3.292400,-3.815742,2.290512,-5.999553,-6.570387,2.828348,5.648266,8.552507,6.695801,-7.415715,3.413053,-6.681968,-5.572289,4.948440,-7.963117,-7.108084,-4.447661,-9.070109,2.997442,8.974078,8.115520,-8.486174,2.039115,-4.305005,-5.128837,4.743158,-9.028581,3.439669,9.547141,3.400103,2.998406,6.953715,9.429238,-0.308613,2.878540,-9.949443,-5.646294,2.776886,-8.219180,5.263527,4.675892,-1.355879,-7.470742,-4.781228,4.149100,-9.433990,-0.126695,-6.228629,9.682115,-8.973259,-8.214457,0.379323,-7.359227,2.056865,-3.090353,1.511983,7.378036,-2.048362,8.786815,2.375115,-8.038813,-3.178897,-4.470760,-3.074957,4.558994,-7.978693,2.522201,-7.454727,-5.787851,0.852153,-4.237909,-0.198493,-0.117845,-3.109735,-6.696186,-6.393314,9.248447,9.270404,9.226135,8.010921,-3.761575,5.608103,-2.184495,1.998466,2.388879,0.715740,7.746985,9.292592,-0.399798,-7.335080,9.237515,-6.036728,0.147872,-4.447909,8.621109,9.268574,0.659821,-3.666210,-0.081466,9.433669,-2.271585,-0.835754,-0.838901,4.000401,0.535719,5.514439,2.298414,2.704689,5.667463,7.011223,7.681854,7.143390,2.833608,-1.726191,7.652651,2.817100,6.822989,-0.396610,6.129864,-2.764677,8.678837,-5.089425,4.681139,2.221988,4.595398,-4.322867,9.914022,-1.202927,0.184874,-6.729242,-3.148947,-2.896711,7.529760,1.113836,-8.587115,3.116931,-2.086045,-7.997131,3.398634,-7.493586,2.656823,-4.446028,-9.278977,9.177480,1.724716,8.483729,-0.001105,8.647107,-6.375431,-0.926706,2.613035,-4.181122,7.892702,7.010413,-8.611520,-0.396630,-7.615925,-7.765226,0.222901,-6.839783,0.191589,-1.598270,4.453686,-7.815499,-1.610488,5.432837,-0.766674,1.534139,-9.080535,0.567406,1.695146,-2.149394,-5.573342,-0.007744,2.785539,-5.940122,-5.272455,-5.135079,2.457344,3.354538,1.678159,5.264760,-2.510863,-3.688687,6.702042,1.398085,2.018681,7.017835,-1.845727,9.337490,-9.375195,6.664067,-2.984384,6.328171,-8.860738,6.994863,9.962466,1.745293,-3.936993,-1.797884,3.734976,-6.007302,-6.170866,-3.423613,7.914355,-7.944464,-1.977987,9.278350,2.061318,-7.345886,5.645213,7.092687,-8.222171,3.408424,-1.920319,-0.815372,9.835260,-1.329347,-6.906302,2.613073,-0.965507,-9.086234,6.393282,7.785486,-1.518182,-9.042498,-8.759947,-7.702665,-3.545099,0.144510,2.253091,9.685791,-3.051120,-4.605650,-0.139587,-4.651440,8.071281,4.616011,-2.460846,1.757837,-7.701804,1.423294,-2.018554,9.806130,6.360928,8.926531,1.036879,1.362385,8.065327,-7.692551,9.263369,-5.429238,7.220161,6.678835,4.025489,-5.277824,-9.598757,-9.829047,9.696144,-3.879782,-6.022004,-6.033997,-3.096298,5.370965,4.993946,0.599642,-0.930447,-3.970307,-9.531798,-8.531644,-3.171587,0.994307,-8.709409,5.714221,-5.409818,-4.002326,-5.202189,-0.476398,-2.424857,-0.312759,1.926236,8.864324,0.953731,-8.018717,1.918195,0.650341,0.315290,5.036511,-9.441352,-2.337230,-3.593653,0.974887,8.636696,8.989541,2.111803,1.515783,5.749858,1.813279,-4.664194,-4.727851,-5.678648,-8.517272,5.853062,4.664220,-7.186463,-6.355352,-5.369617,2.376256,8.954717,3.902766,-5.233559,5.151525,7.575065,1.130928,-8.962026,-8.978064,8.441404,5.016323,-8.617880,6.265053,-5.865277,2.650057,6.163502,-1.296461,3.892502,-3.323059,-8.943998,0.926666,-1.315926,-9.492025,4.055526,9.501163,1.486569,4.214926,0.428448,-1.918581,-6.783267,-7.735893,3.258154,-2.810223,-5.043314,-0.844401,-3.580090,0.940520,-1.396682,-6.761826,-4.869649,1.162285,-1.700549,4.051737,8.873459,8.374816,4.070769,9.394916,-4.253168,6.994463,-9.647167,5.100328,8.029726,5.190593,-4.494600,4.484631,1.742880,-8.567321,1.778615,5.111787,-7.858831,-5.327326,-6.327707,-4.960625,5.166713,-3.282540,3.005623,8.013284,-6.040569,8.519351,-6.245455,6.114539,2.386260,9.453615,4.286562,9.823496,3.825992,7.790666,3.227355,-0.562845,2.193134,9.444920,-9.023765,8.651621,4.747977,-1.621271,-1.262648,-3.986250,1.373913,-3.257094,-9.750739,-9.547334,-4.703740,-5.970710,5.111326,-4.408778,2.308400,-1.103995,-9.824582,-3.021081,-5.311890,0.352933,-8.268581,-2.038340,4.108191,-7.163817,-6.028130,6.894997,-0.004914,-1.666030,-5.166347,-3.711656,-5.089324,-3.806228,-0.926134,0.789959,4.894586,5.130837,-3.825989,0.905278,7.041012,4.594837,8.549440,-4.656313,-8.199667,6.087803,9.830229,-6.426394,-1.631307,6.424805,0.380256,4.158500,2.362679,-7.907515,-2.348640,-8.049923,3.454690,7.963973,-5.245874,-6.864288,9.940938,-4.680115,5.268883,-7.829894,4.001488,4.824957,-9.909341,1.796574,2.137249,3.163044,9.843639,2.107783,-6.336290,3.606805,-9.822310,8.644159,-4.865647,7.306200,6.246770,2.304315,9.102926,0.845924,-5.467413,5.453129,1.455448,7.966678,-0.053953,8.341996,-1.196958,-4.850797,7.600874,-3.053448,1.735858,6.524692,7.471321,7.584647,2.004350,0.108202,6.208853,-6.932649,1.756876,4.908852,-2.638845,-0.455215,-5.472647,-0.524467,2.309967,9.573653,-4.062393,2.040643,3.047306,-9.826475,6.851769,-7.939736,-8.623216,8.018373,5.033695,-2.343069,-6.089288,-8.340390,4.804966,-4.431515,2.381085,6.637328,-4.722120,3.141235,1.033960,4.053270,9.194835,1.859811,-8.595006,-6.555181,9.888015,3.037608,4.370571,-0.042128,-8.824763,4.313459,-8.200149,8.444516,1.202592,3.579632,-7.880885,-9.650784,-1.823877,-4.638232,-4.726236,-9.353734,1.667694,3.589855,5.250886,9.554551,-8.662226,2.432874,2.004504,-0.155882,-0.789700,4.900911,-8.845929,-7.958456,9.777001,7.741089,4.130129,8.859148,1.418422,-7.461390,7.077646,0.230320,-2.238163,-6.124808,0.612869,9.206303,-9.721519,5.282729,-3.432448,-1.380856,-3.947454,0.536276,3.098653,-8.967205,-6.221611,-8.357490,-5.066336,8.689479,-6.767852,-3.405980,-5.858587,4.421318,-4.251405,1.202570,8.971263,-6.858823,4.501186,9.387593,-2.473431,-6.694631,-5.391521,-1.886342,-9.688345,-7.898666,-7.819870,-0.402354,-4.203006,9.269098,-3.983354,6.338920,-5.890224,7.899759,6.866803,8.657607,-6.198608,-3.196680,-4.816994,0.856991,5.881656,1.217937,-5.830960,-9.371108,-6.696245,6.568493,6.954975,-2.317609,-7.564037,4.604892,-9.709119,-0.124977,-3.267774,-3.940205,3.515643,3.384000,2.291749,-5.010002,4.393680,-8.599126,3.263238,-0.967678,-1.236078,-9.480570,1.330694,-6.183202,-9.654860,-9.983855,-5.265269,7.744291,5.125944,-8.652533,-7.199896,-2.456563,7.910675,1.392923,4.748085,6.285763,-7.002028,-3.531654,-0.378740,1.782986,1.078851,7.490754,-2.605859,-9.762947,-6.898880,-2.924453,3.919328], dtype = "float64")#candidate|3741|(780,)|const|float64
call_3740 = relay.TupleGetItem(func_3428_call(relay.reshape(const_3741.astype('float64'), [780,])), 0)
call_3742 = relay.TupleGetItem(func_3431_call(relay.reshape(const_3741.astype('float64'), [780,])), 0)
output = relay.Tuple([call_3738,call_3740,const_3741,])
output2 = relay.Tuple([call_3739,call_3742,const_3741,])
func_3743 = relay.Function([], output)
mod['func_3743'] = func_3743
mod = relay.transform.InferType()(mod)
mutated_mod['func_3743'] = func_3743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3743_call = mutated_mod.get_global_var('func_3743')
call_3744 = func_3743_call()
output = call_3744
func_3745 = relay.Function([], output)
mutated_mod['func_3745'] = func_3745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_3773 = relay.TupleGetItem(func_3064_call(), 0)
call_3774 = relay.TupleGetItem(func_3065_call(), 0)
output = relay.Tuple([call_3773,])
output2 = relay.Tuple([call_3774,])
func_3785 = relay.Function([], output)
mod['func_3785'] = func_3785
mod = relay.transform.InferType()(mod)
mutated_mod['func_3785'] = func_3785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3785_call = mutated_mod.get_global_var('func_3785')
call_3786 = func_3785_call()
output = call_3786
func_3787 = relay.Function([], output)
mutated_mod['func_3787'] = func_3787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3086_call = mod.get_global_var('func_3086')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_3830 = relay.TupleGetItem(func_3086_call(), 1)
call_3831 = relay.TupleGetItem(func_3087_call(), 1)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_3852 = relay.TupleGetItem(func_3161_call(), 0)
call_3853 = relay.TupleGetItem(func_3162_call(), 0)
output = relay.Tuple([call_3830,call_3852,])
output2 = relay.Tuple([call_3831,call_3853,])
func_3860 = relay.Function([], output)
mod['func_3860'] = func_3860
mod = relay.transform.InferType()(mod)
output = func_3860()
func_3861 = relay.Function([], output)
mutated_mod['func_3861'] = func_3861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3584_call = mod.get_global_var('func_3584')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_3907 = func_3584_call()
call_3908 = func_3584_call()
output = call_3907
output2 = call_3908
func_3933 = relay.Function([], output)
mod['func_3933'] = func_3933
mod = relay.transform.InferType()(mod)
mutated_mod['func_3933'] = func_3933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3933_call = mutated_mod.get_global_var('func_3933')
call_3934 = func_3933_call()
output = call_3934
func_3935 = relay.Function([], output)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3584_call = mod.get_global_var('func_3584')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_3966 = func_3584_call()
call_3967 = func_3584_call()
func_3095_call = mod.get_global_var('func_3095')
func_3097_call = mutated_mod.get_global_var('func_3097')
var_3972 = relay.var("var_3972", dtype = "float32", shape = (330,))#candidate|3972|(330,)|var|float32
call_3971 = func_3095_call(relay.reshape(var_3972.astype('float32'), [3, 10, 11]))
call_3973 = func_3095_call(relay.reshape(var_3972.astype('float32'), [3, 10, 11]))
func_3428_call = mod.get_global_var('func_3428')
func_3431_call = mutated_mod.get_global_var('func_3431')
var_3990 = relay.var("var_3990", dtype = "float64", shape = (780, 1))#candidate|3990|(780, 1)|var|float64
call_3989 = relay.TupleGetItem(func_3428_call(relay.reshape(var_3990.astype('float64'), [780,])), 2)
call_3991 = relay.TupleGetItem(func_3431_call(relay.reshape(var_3990.astype('float64'), [780,])), 2)
func_3349_call = mod.get_global_var('func_3349')
func_3353_call = mutated_mod.get_global_var('func_3353')
const_3995 = relay.const([[-8.208013,-0.605448,9.124285,-1.360795,-3.960925,0.904336,-7.066411,5.564445,6.717686,6.704399,-3.456165,4.069814,9.838080,-6.107584,-3.087823,0.024075,8.631652,5.503360,6.351435,5.401802,-8.557430,-9.499650,-1.142400,-2.802092,6.572312,5.324444,-4.575174,7.037036,6.296802,6.524377,9.837575,-6.419211,7.110270,4.697813,3.792304,-6.524233,0.411851,-3.607267,-6.312561,1.454424,-1.827248,-9.204181,9.970457,-4.945374,3.387315,-2.128616,-6.106433,-6.035362,2.584545,-1.548481,-0.775247,-6.900514,2.976892,6.452879,7.773230,3.696107,8.772316,6.726609,7.034707,9.946607,1.239660,1.002290,-3.774405,4.707598,5.039624,-0.294569,-9.308245,9.024389,4.490327,-5.323005,-9.539035,-0.924073,9.379573,-2.456835,9.420777,8.547872,-2.124959,-2.212946,-3.256332,-8.333320,7.859886,2.791952,1.889103,5.435630,-6.408489,-8.884407,6.119079,-5.922693,-6.660311,6.490212,4.601094,-5.879904,2.879484,-9.118285,6.511939,7.191053,-1.405316,-0.183992,-0.364365,-2.016971,8.034345,3.009043,-0.522755,9.390717,-4.333020,-3.476151,-9.560018,1.330727,-6.044487,6.202736,-9.740438,-5.077622,-3.548836,7.987254,3.015040,9.675937,-8.190917,5.181585,-6.943389,2.074985,-7.234126,-6.274848,-8.356008,-1.702677,-5.923247,-0.952357,1.878998,1.407519,-0.476094,-8.416944,-2.164971,-8.439768,-2.944030,7.007342,3.783215,5.277971,7.665824,-1.046101,-9.231954,-1.219367,-9.541442,9.693365,9.164825,8.392259,3.857437,0.780250,7.142886,-9.353370,-6.560125,9.203008,-3.513896,9.711363,-7.307424,-4.457465,-4.304313,3.008030,6.910074,-0.614499,4.503825,-3.569656,6.777442,5.339092,-6.687862,-4.209352,6.182225,-1.669848,1.677551,3.681238,7.609000,-6.074537,-6.604455,-4.932524,-8.604857,4.227486,1.136741,5.393794,6.702255,5.656584,-1.099092,-7.293126,7.118558,-3.672009,-7.795032,4.610347,6.439749,-5.683004,5.128583,5.937694,8.424840,-3.693228,0.857405,-4.907511,-0.189366,-3.843084,5.537959,-4.709118,7.711741,7.793075,5.019620,0.599220,-4.097830,-0.306381,-2.239570,-4.436319,-2.546842,-5.976215,-1.246880,2.953223,5.931179,1.485688,-8.954397,8.637425,-5.231872,-3.394001,5.936127,-4.015782,8.086834,-2.175132,9.580779,2.389573,3.243941,9.010101,-5.520141,-6.127493,-0.425549,1.851979,0.318379,-9.754937,7.327699,1.479814,-5.167696,1.913157,6.314327,4.191273,-4.566870,-8.566470,7.183734,5.939867,-9.076058,3.224991,1.015429,-7.446739,2.334732,2.691688,2.397086,-1.843834,-1.251759,2.492552,6.868619,-6.426811,4.649373,9.642301,-4.566279,1.694525,-5.188676,8.982896,4.685846,-2.124621,-3.358431,6.002015,8.634006,8.627067,3.479591,5.652861,-0.256567,-7.192187,-1.448130,-6.302528,-7.773202,-5.043017,-4.159239,2.574362,3.792856,-1.377433,6.848475,1.346701,4.283363,-9.328515,3.895759,7.329887,-3.598841,0.648172,7.487621,9.572953,3.499839,-6.638670,-1.339140,3.237694,-4.595568,6.032443,-4.842640,-6.785083,-2.848600,-6.486350,-9.603924,6.247538,-8.789632,9.544411,-7.931164,6.963016,-4.852009,7.345819,1.968116,-8.291027,-3.804014,6.020206,-2.551822,1.259270,3.221622,-4.387310,5.369846,-4.796378,1.238789,-8.173016,-6.805943,6.785388,1.359467,8.852065,-5.085452,-2.007918,-5.586274,1.410689,8.228486,8.990162,-4.392721,-0.354461,2.674362,3.893331,5.196590,-8.682661,-2.528792,-3.439564,-7.826967,-7.013033,-1.490278,6.937335,7.383136,7.703059,0.316350,9.545822,9.107120,-2.455200,-2.697992,7.875328,5.263892,7.852741,3.182540,3.283170,-9.553421,-0.615234,2.482159,7.992996,-0.397168,0.985325,7.125041,-6.535510,9.019025,4.394408,-2.710646,3.035455,-6.647518,1.089301,-6.774252,1.719599,0.996016,2.889162,2.542672,9.328668,-7.598582,-1.911063,4.988619,-5.038712,9.448463,-2.563765,-8.294571,6.625179,-9.300137,-1.376077,0.213102,2.698810,-5.613812,4.611113,4.879209,2.149332,-5.768891,3.612395,-0.023986,-8.061590,5.892114,-2.485530,-5.837140,-8.896815,-9.183853,4.236048,-2.178570,-9.001323,-4.031122,0.009901,-1.617180,8.844878,-7.583942,-3.553886,-1.317946,-1.911771,1.225474,6.084711,-1.580222,4.337343,-0.170401,-2.793947,1.434874,9.512735,7.930568,-8.369662,-7.953492,-6.495564,-0.039470,0.289354,6.544417,0.799740,-7.673759,-8.699873,-6.570856,-5.756733,-4.626875,-9.295298,9.812465,5.725063,-8.527086,2.964351,5.962993,7.990672,-3.321827,-5.674061,-0.151036,9.434389,-7.952494,4.702216,4.877918,-7.741520,-8.195149,1.966733,-2.746836,-4.672716,-8.080130,2.025459,6.426638,-2.217594,-1.687414,3.740622,-6.528956,0.354463,-2.486275,6.159532,-5.817178,-2.065095,-1.592351,5.360924,-1.423542,5.079266,1.916305,4.445088,1.385797,-8.634849,-8.453545,-0.299043,-1.017554,-7.496568,-2.308669,-8.406108,7.138492,-9.275748,0.416082,-3.562315,0.154945,-2.048320,3.424557,-3.076340,9.769880,-6.448768,-8.335980,-3.266967,-5.724470,-4.067036,5.999530,-9.173967,4.478259,-4.487326,-3.721920,-6.136290,3.348667,-5.670355,-2.043256,8.178329,6.571697,-7.869988,0.937973,8.849353,0.994472,-4.209313,-4.792919,6.743117,8.001826,-5.538030,-3.091705,-7.213721,-5.605986,-8.731884,4.913970,-5.117813,7.310752,-4.579873,-1.163228,1.938104,3.370119,-0.067817,-9.824715,0.743512,0.529472,6.511692,8.251977,4.541100,-2.452341,-9.703637,-2.937103,-3.422093,9.260762,-4.804621,-9.882781,6.370447,4.313992,-4.393887,5.451707,-0.295629,0.851567,8.127659,6.921213,-9.936794,-1.906422,4.387220,-7.202801,0.588119,-4.721524,0.275326,9.042076,1.783937,-0.880124,-1.438542,8.879383,-6.422976,-2.466335,9.654924,6.361013,0.585061,5.725820,-4.207796,-1.816846,7.484351,5.068029,-1.728784,-1.909750,2.260529,2.940410,-9.538242,-0.045202,9.627543,-0.049352,-8.486872,9.516820,-7.481657,-3.603234,-5.631413,-5.549573,-0.740640,-1.102898,-9.288258,-0.643509,8.321303,9.217733,-2.463078,-2.817109,-4.320258,0.389752,-0.157232,-4.313499,9.845708,5.522371,5.756751,5.258405,6.333532,-8.731765,-6.870127,-1.819470,-8.668503,-6.806574,4.438385,5.968008,0.930055,4.827018,7.256238,-8.799614,-7.232040,-8.822886,3.964713,7.941017,5.574550,-3.920191,-7.038663,7.287982,-5.934306,-0.340407,-2.118011,1.124670,-6.477644,-2.180156,-7.409986,-0.205718,-0.103034,3.467648,-5.442004,9.307461,-9.533394,-3.495099,-4.289908,-0.441187,3.827999,-8.709267,-0.870517,9.610630,-9.974133,-2.950416,7.789905,-8.116442,9.910410,7.902535,-0.213298,3.219562,2.995132,-6.927903,4.124146,-4.171642,4.656293,-7.252210,1.884718,-1.179682,6.427740,-0.526106,5.618394,3.460984,-6.991382,-3.381787,9.960266,-1.606146,2.793808,-1.794892,2.985987,3.384296,2.956966,-1.672395,-4.004299]], dtype = "float32")#candidate|3995|(1, 660)|const|float32
call_3994 = relay.TupleGetItem(func_3349_call(relay.reshape(call_3966.astype('float32'), [1, 10, 11]), relay.reshape(var_3990.astype('float64'), [130, 6]), relay.reshape(const_3995.astype('float32'), [6, 10, 11]), ), 3)
call_3996 = relay.TupleGetItem(func_3353_call(relay.reshape(call_3966.astype('float32'), [1, 10, 11]), relay.reshape(var_3990.astype('float64'), [130, 6]), relay.reshape(const_3995.astype('float32'), [6, 10, 11]), ), 3)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_4002 = func_3152_call()
call_4003 = func_3152_call()
output = relay.Tuple([call_3966,call_3971,var_3972,call_3989,var_3990,call_3994,const_3995,call_4002,])
output2 = relay.Tuple([call_3967,call_3973,var_3972,call_3991,var_3990,call_3996,const_3995,call_4003,])
func_4005 = relay.Function([var_3972,var_3990,], output)
mod['func_4005'] = func_4005
mod = relay.transform.InferType()(mod)
mutated_mod['func_4005'] = func_4005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4005_call = mutated_mod.get_global_var('func_4005')
var_4007 = relay.var("var_4007", dtype = "float32", shape = (330,))#candidate|4007|(330,)|var|float32
var_4008 = relay.var("var_4008", dtype = "float64", shape = (780, 1))#candidate|4008|(780, 1)|var|float64
call_4006 = func_4005_call(var_4007,var_4008,)
output = call_4006
func_4009 = relay.Function([var_4007,var_4008,], output)
mutated_mod['func_4009'] = func_4009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_4073 = func_3933_call()
call_4074 = func_3933_call()
output = call_4073
output2 = call_4074
func_4080 = relay.Function([], output)
mod['func_4080'] = func_4080
mod = relay.transform.InferType()(mod)
mutated_mod['func_4080'] = func_4080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mutated_mod.get_global_var('func_4080')
call_4081 = func_4080_call()
output = call_4081
func_4082 = relay.Function([], output)
mutated_mod['func_4082'] = func_4082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_4135 = relay.TupleGetItem(func_3507_call(), 0)
call_4136 = relay.TupleGetItem(func_3508_call(), 0)
output = call_4135
output2 = call_4136
func_4144 = relay.Function([], output)
mod['func_4144'] = func_4144
mod = relay.transform.InferType()(mod)
mutated_mod['func_4144'] = func_4144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mutated_mod.get_global_var('func_4144')
call_4145 = func_4144_call()
output = call_4145
func_4146 = relay.Function([], output)
mutated_mod['func_4146'] = func_4146
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4168 = relay.var("var_4168", dtype = "int32", shape = (4, 15, 9))#candidate|4168|(4, 15, 9)|var|int32
var_4169 = relay.var("var_4169", dtype = "int32", shape = (4, 15, 9))#candidate|4169|(4, 15, 9)|var|int32
bop_4170 = relay.add(var_4168.astype('int32'), relay.reshape(var_4169.astype('int32'), relay.shape_of(var_4168))) # shape=(4, 15, 9)
output = bop_4170
output2 = bop_4170
func_4188 = relay.Function([var_4168,var_4169,], output)
mod['func_4188'] = func_4188
mod = relay.transform.InferType()(mod)
var_4189 = relay.var("var_4189", dtype = "int32", shape = (4, 15, 9))#candidate|4189|(4, 15, 9)|var|int32
var_4190 = relay.var("var_4190", dtype = "int32", shape = (4, 15, 9))#candidate|4190|(4, 15, 9)|var|int32
output = func_4188(var_4189,var_4190,)
func_4191 = relay.Function([var_4189,var_4190,], output)
mutated_mod['func_4191'] = func_4191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_4222 = func_2220_call()
call_4223 = func_2220_call()
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_4226 = func_2168_call()
call_4227 = func_2168_call()
func_3349_call = mod.get_global_var('func_3349')
func_3353_call = mutated_mod.get_global_var('func_3353')
var_4239 = relay.var("var_4239", dtype = "float64", shape = (780,))#candidate|4239|(780,)|var|float64
var_4240 = relay.var("var_4240", dtype = "float32", shape = (660,))#candidate|4240|(660,)|var|float32
call_4238 = relay.TupleGetItem(func_3349_call(relay.reshape(call_4222.astype('float32'), [1, 10, 11]), relay.reshape(var_4239.astype('float64'), [130, 6]), relay.reshape(var_4240.astype('float32'), [6, 10, 11]), ), 4)
call_4241 = relay.TupleGetItem(func_3353_call(relay.reshape(call_4222.astype('float32'), [1, 10, 11]), relay.reshape(var_4239.astype('float64'), [130, 6]), relay.reshape(var_4240.astype('float32'), [6, 10, 11]), ), 4)
output = relay.Tuple([call_4222,call_4226,call_4238,var_4239,var_4240,])
output2 = relay.Tuple([call_4223,call_4227,call_4241,var_4239,var_4240,])
func_4242 = relay.Function([var_4239,var_4240,], output)
mod['func_4242'] = func_4242
mod = relay.transform.InferType()(mod)
mutated_mod['func_4242'] = func_4242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4242_call = mutated_mod.get_global_var('func_4242')
var_4244 = relay.var("var_4244", dtype = "float64", shape = (780,))#candidate|4244|(780,)|var|float64
var_4245 = relay.var("var_4245", dtype = "float32", shape = (660,))#candidate|4245|(660,)|var|float32
call_4243 = func_4242_call(var_4244,var_4245,)
output = call_4243
func_4246 = relay.Function([var_4244,var_4245,], output)
mutated_mod['func_4246'] = func_4246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3730_call = mod.get_global_var('func_3730')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_4255 = relay.TupleGetItem(func_3730_call(), 0)
call_4256 = relay.TupleGetItem(func_3731_call(), 0)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_4271 = func_2168_call()
call_4272 = func_2168_call()
output = relay.Tuple([call_4255,call_4271,])
output2 = relay.Tuple([call_4256,call_4272,])
func_4275 = relay.Function([], output)
mod['func_4275'] = func_4275
mod = relay.transform.InferType()(mod)
mutated_mod['func_4275'] = func_4275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4275_call = mutated_mod.get_global_var('func_4275')
call_4276 = func_4275_call()
output = call_4276
func_4277 = relay.Function([], output)
mutated_mod['func_4277'] = func_4277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_4280 = relay.TupleGetItem(func_3218_call(), 0)
call_4281 = relay.TupleGetItem(func_3219_call(), 0)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_4286 = func_2220_call()
call_4287 = func_2220_call()
output = relay.Tuple([call_4280,call_4286,])
output2 = relay.Tuple([call_4281,call_4287,])
func_4293 = relay.Function([], output)
mod['func_4293'] = func_4293
mod = relay.transform.InferType()(mod)
mutated_mod['func_4293'] = func_4293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4293_call = mutated_mod.get_global_var('func_4293')
call_4294 = func_4293_call()
output = call_4294
func_4295 = relay.Function([], output)
mutated_mod['func_4295'] = func_4295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4308 = relay.var("var_4308", dtype = "uint8", shape = (3, 9, 8))#candidate|4308|(3, 9, 8)|var|uint8
var_4309 = relay.var("var_4309", dtype = "uint8", shape = (3, 9, 8))#candidate|4309|(3, 9, 8)|var|uint8
bop_4310 = relay.bitwise_or(var_4308.astype('uint8'), relay.reshape(var_4309.astype('uint8'), relay.shape_of(var_4308))) # shape=(3, 9, 8)
func_3860_call = mod.get_global_var('func_3860')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_4321 = relay.TupleGetItem(func_3860_call(), 1)
call_4322 = relay.TupleGetItem(func_3861_call(), 1)
uop_4323 = relay.acosh(var_4308.astype('float64')) # shape=(3, 9, 8)
func_3730_call = mod.get_global_var('func_3730')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_4330 = relay.TupleGetItem(func_3730_call(), 0)
call_4331 = relay.TupleGetItem(func_3731_call(), 0)
output = relay.Tuple([bop_4310,call_4321,uop_4323,call_4330,])
output2 = relay.Tuple([bop_4310,call_4322,uop_4323,call_4331,])
func_4333 = relay.Function([var_4308,var_4309,], output)
mod['func_4333'] = func_4333
mod = relay.transform.InferType()(mod)
var_4334 = relay.var("var_4334", dtype = "uint8", shape = (3, 9, 8))#candidate|4334|(3, 9, 8)|var|uint8
var_4335 = relay.var("var_4335", dtype = "uint8", shape = (3, 9, 8))#candidate|4335|(3, 9, 8)|var|uint8
output = func_4333(var_4334,var_4335,)
func_4336 = relay.Function([var_4334,var_4335,], output)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_4368 = func_4080_call()
call_4369 = func_4080_call()
output = relay.Tuple([call_4368,])
output2 = relay.Tuple([call_4369,])
func_4385 = relay.Function([], output)
mod['func_4385'] = func_4385
mod = relay.transform.InferType()(mod)
mutated_mod['func_4385'] = func_4385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4385_call = mutated_mod.get_global_var('func_4385')
call_4386 = func_4385_call()
output = call_4386
func_4387 = relay.Function([], output)
mutated_mod['func_4387'] = func_4387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3645_call = mod.get_global_var('func_3645')
func_3647_call = mutated_mod.get_global_var('func_3647')
call_4459 = relay.TupleGetItem(func_3645_call(), 0)
call_4460 = relay.TupleGetItem(func_3647_call(), 0)
output = call_4459
output2 = call_4460
func_4475 = relay.Function([], output)
mod['func_4475'] = func_4475
mod = relay.transform.InferType()(mod)
output = func_4475()
func_4476 = relay.Function([], output)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_4482 = func_4080_call()
call_4483 = func_4080_call()
const_4495 = relay.const([[[3.757546,1.927103,8.639434,6.902168,6.181544,0.115559,3.968463,-7.425898,7.348910,1.173037,4.740430],[4.947894,-1.543759,-3.250211,7.341350,6.778396,-2.577308,0.751831,-5.654159,1.438123,3.383344,7.016744],[-0.853939,-2.289813,7.913964,-7.242695,1.155591,8.235539,6.834317,-9.015684,4.850628,8.041546,-7.034168],[3.129655,5.216086,-4.757301,-7.970345,-9.383500,-0.079062,-8.580829,-2.709698,-5.657253,-3.666484,5.898231],[3.311555,-8.994798,5.081620,7.864393,-0.795433,-9.236845,6.092406,3.024093,-0.651552,-4.397649,-1.985191],[-9.197231,-3.897512,-2.779211,-7.128908,-8.020204,2.518916,8.142647,3.904633,5.465486,8.600747,7.360869],[-9.262754,-1.357271,-0.225809,0.015572,7.840507,7.681948,7.330277,-4.730820,6.164501,2.596681,-3.042935],[-6.480685,3.552757,3.526899,5.899232,-2.985492,4.853425,1.370957,6.341208,-2.534585,-5.035694,-3.960124],[6.516876,-4.570877,-7.601448,-2.132983,-6.851303,-1.040335,-4.128896,-7.683830,-7.616313,7.250053,-2.793467],[-1.950237,-3.151986,-5.563440,-3.500699,-4.973024,-1.819488,0.757814,-4.641284,0.378051,-2.560091,0.411523]],[[0.178251,-7.484603,-8.890069,-6.543684,-1.753049,-5.322035,8.096625,-2.780024,-9.901900,-4.035613,9.312933],[0.423804,8.660398,-1.360144,-3.441618,-1.181496,3.341292,1.714925,-9.817834,-0.759254,-1.314810,8.984878],[-0.012382,-6.128401,-0.561920,3.631369,-5.455072,-9.209474,8.681438,2.490218,-5.100240,6.453854,-6.146624],[9.309631,-7.391883,-0.787515,-7.243594,7.292212,4.301744,8.747471,-1.747541,3.532281,1.547145,-2.429413],[-3.858850,-4.689312,5.104276,-7.936719,8.030412,-2.784858,-3.217502,-8.974346,4.159547,7.515160,8.666529],[-5.439687,4.288196,-9.776444,6.789955,0.929185,-0.702681,-7.594490,9.032536,-2.649002,-4.176570,5.517961],[4.988618,-4.625155,6.475835,9.702157,-3.549473,-9.104744,4.828895,6.423978,5.255766,-0.958869,-5.851870],[2.963359,4.049315,-1.216088,-3.385808,-8.094813,-5.643134,-4.834360,-7.384834,-0.758968,-5.559236,-3.247918],[-1.007759,-8.396202,-3.387258,4.301492,-2.664880,0.346127,-0.450684,2.829470,8.196041,-0.460269,-9.042739],[4.260824,-4.078965,-2.157016,-3.797895,-9.992021,-4.012884,-6.389160,2.307508,5.965040,-4.898888,-1.820520]],[[0.498290,2.862690,0.372260,-0.590828,8.222655,7.521326,8.855452,-0.931083,-7.298082,-2.460055,7.018704],[-5.726280,6.274612,-7.490867,-4.133691,-1.521376,9.452490,-8.469583,-9.202350,-6.196337,-2.126649,0.514827],[3.786247,5.840920,2.771467,-3.537112,-7.095139,6.088344,4.378541,0.495250,-1.433977,7.717479,3.536503],[3.588652,-2.750124,1.819441,6.264178,-9.855555,-6.847324,-6.486655,-2.221638,3.976231,0.925861,-5.269526],[-3.802984,-9.219820,5.619479,-1.098311,9.287459,-5.227489,-5.539015,-8.464785,0.089985,-4.199573,-1.545437],[2.716890,-1.984830,1.955731,6.467342,-9.040601,4.255961,4.973039,-8.531050,-7.269980,3.242252,2.742444],[-5.637178,3.871897,-2.825653,-0.373646,-1.778873,2.574912,-7.433553,6.242160,-4.400659,3.568998,-2.236011],[8.164150,4.885532,6.206045,-1.603977,-9.940642,-0.303909,-1.068872,4.413454,-0.669945,-4.649882,-1.671301],[-6.150624,1.172282,4.251422,0.242040,5.702382,-0.990550,-2.482056,5.352284,-2.418657,6.484286,4.116537],[-5.579427,-9.432169,-6.726496,-6.959570,2.690754,-9.162229,-6.487012,-2.832085,-7.940795,-4.068566,-2.565498]],[[-3.360403,3.811251,0.144280,0.012387,9.894194,9.098933,-0.328629,-7.728804,8.612276,-6.862503,-5.339730],[1.164272,-7.322669,-0.974140,6.630605,0.022288,-6.200140,-2.511881,1.981507,-7.741081,3.493371,5.890395],[-3.616859,9.859292,6.918867,2.419678,-0.342198,-2.986696,-6.298094,6.741114,5.824729,7.252617,6.980578],[7.865962,-9.513376,5.951713,-6.617458,1.725665,0.712410,-7.813812,-2.311226,-5.167338,-4.039177,2.643762],[-3.592957,-4.306225,3.809794,5.793768,-2.527027,-4.734091,5.504193,-0.497029,-4.844681,-8.499367,-4.172010],[-3.457723,-2.284695,7.723836,-9.991810,-8.588246,6.716481,-4.800275,-3.374308,-5.344504,9.751502,6.335295],[-0.334234,-9.249684,-4.479633,-4.971402,7.981376,9.454259,-3.027832,-5.540061,-9.580253,8.801028,-4.341676],[-9.808490,4.601893,6.685376,6.639427,3.332400,-7.985103,-9.635946,-6.602108,-4.164917,-1.836889,-4.067617],[-6.273152,6.174451,4.357131,8.019596,-6.178963,-1.522711,-9.382271,-6.451131,5.770354,8.393567,9.752985],[-9.065070,0.742017,1.260915,-4.565830,-8.126649,4.948854,1.234760,-3.123405,-4.300108,2.170223,-9.645697]]], dtype = "float32")#candidate|4495|(4, 10, 11)|const|float32
bop_4496 = relay.multiply(call_4482.astype('int8'), const_4495.astype('int8')) # shape=(4, 10, 11)
bop_4499 = relay.multiply(call_4483.astype('int8'), const_4495.astype('int8')) # shape=(4, 10, 11)
func_3095_call = mod.get_global_var('func_3095')
func_3097_call = mutated_mod.get_global_var('func_3097')
var_4508 = relay.var("var_4508", dtype = "float32", shape = (330,))#candidate|4508|(330,)|var|float32
call_4507 = func_3095_call(relay.reshape(var_4508.astype('float32'), [3, 10, 11]))
call_4509 = func_3095_call(relay.reshape(var_4508.astype('float32'), [3, 10, 11]))
output = relay.Tuple([bop_4496,call_4507,var_4508,])
output2 = relay.Tuple([bop_4499,call_4509,var_4508,])
func_4522 = relay.Function([var_4508,], output)
mod['func_4522'] = func_4522
mod = relay.transform.InferType()(mod)
var_4523 = relay.var("var_4523", dtype = "float32", shape = (330,))#candidate|4523|(330,)|var|float32
output = func_4522(var_4523)
func_4524 = relay.Function([var_4523], output)
mutated_mod['func_4524'] = func_4524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_4529 = func_4144_call()
call_4530 = func_4144_call()
output = call_4529
output2 = call_4530
func_4536 = relay.Function([], output)
mod['func_4536'] = func_4536
mod = relay.transform.InferType()(mod)
mutated_mod['func_4536'] = func_4536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mutated_mod.get_global_var('func_4536')
call_4537 = func_4536_call()
output = call_4537
func_4538 = relay.Function([], output)
mutated_mod['func_4538'] = func_4538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4475_call = mod.get_global_var('func_4475')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_4592 = func_4475_call()
call_4593 = func_4475_call()
output = call_4592
output2 = call_4593
func_4596 = relay.Function([], output)
mod['func_4596'] = func_4596
mod = relay.transform.InferType()(mod)
mutated_mod['func_4596'] = func_4596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4596_call = mutated_mod.get_global_var('func_4596')
call_4597 = func_4596_call()
output = call_4597
func_4598 = relay.Function([], output)
mutated_mod['func_4598'] = func_4598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_4609 = func_3152_call()
call_4610 = func_3152_call()
uop_4611 = relay.exp(call_4609.astype('float64')) # shape=(10, 78)
uop_4613 = relay.exp(call_4610.astype('float64')) # shape=(10, 78)
output = uop_4611
output2 = uop_4613
func_4614 = relay.Function([], output)
mod['func_4614'] = func_4614
mod = relay.transform.InferType()(mod)
output = func_4614()
func_4615 = relay.Function([], output)
mutated_mod['func_4615'] = func_4615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_4639 = relay.TupleGetItem(func_3507_call(), 0)
call_4640 = relay.TupleGetItem(func_3508_call(), 0)
output = relay.Tuple([call_4639,])
output2 = relay.Tuple([call_4640,])
func_4641 = relay.Function([], output)
mod['func_4641'] = func_4641
mod = relay.transform.InferType()(mod)
mutated_mod['func_4641'] = func_4641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mutated_mod.get_global_var('func_4641')
call_4642 = func_4641_call()
output = call_4642
func_4643 = relay.Function([], output)
mutated_mod['func_4643'] = func_4643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_4647 = func_2835_call()
call_4648 = func_2835_call()
output = relay.Tuple([call_4647,])
output2 = relay.Tuple([call_4648,])
func_4656 = relay.Function([], output)
mod['func_4656'] = func_4656
mod = relay.transform.InferType()(mod)
output = func_4656()
func_4657 = relay.Function([], output)
mutated_mod['func_4657'] = func_4657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_4758 = func_3152_call()
call_4759 = func_3152_call()
func_3584_call = mod.get_global_var('func_3584')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_4770 = func_3584_call()
call_4771 = func_3584_call()
var_4780 = relay.var("var_4780", dtype = "float64", shape = (10, 78))#candidate|4780|(10, 78)|var|float64
bop_4781 = relay.bitwise_xor(call_4758.astype('int8'), relay.reshape(var_4780.astype('int8'), relay.shape_of(call_4758))) # shape=(10, 78)
bop_4784 = relay.bitwise_xor(call_4759.astype('int8'), relay.reshape(var_4780.astype('int8'), relay.shape_of(call_4759))) # shape=(10, 78)
uop_4785 = relay.sin(var_4780.astype('float32')) # shape=(10, 78)
output = relay.Tuple([call_4770,bop_4781,uop_4785,])
output2 = relay.Tuple([call_4771,bop_4784,uop_4785,])
func_4788 = relay.Function([var_4780,], output)
mod['func_4788'] = func_4788
mod = relay.transform.InferType()(mod)
mutated_mod['func_4788'] = func_4788
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4789 = relay.var("var_4789", dtype = "float64", shape = (10, 78))#candidate|4789|(10, 78)|var|float64
func_4788_call = mutated_mod.get_global_var('func_4788')
call_4790 = func_4788_call(var_4789)
output = call_4790
func_4791 = relay.Function([var_4789], output)
mutated_mod['func_4791'] = func_4791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3711_call = mod.get_global_var('func_3711')
func_3712_call = mutated_mod.get_global_var('func_3712')
call_4813 = func_3711_call()
call_4814 = func_3711_call()
output = relay.Tuple([call_4813,])
output2 = relay.Tuple([call_4814,])
func_4824 = relay.Function([], output)
mod['func_4824'] = func_4824
mod = relay.transform.InferType()(mod)
output = func_4824()
func_4825 = relay.Function([], output)
mutated_mod['func_4825'] = func_4825
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4867 = relay.var("var_4867", dtype = "float64", shape = ())#candidate|4867|()|var|float64
var_4868 = relay.var("var_4868", dtype = "float64", shape = (15, 8, 6))#candidate|4868|(15, 8, 6)|var|float64
bop_4869 = relay.floor_divide(var_4867.astype('float64'), var_4868.astype('float64')) # shape=(15, 8, 6)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_4881 = relay.TupleGetItem(func_3161_call(), 0)
call_4882 = relay.TupleGetItem(func_3162_call(), 0)
func_589_call = mod.get_global_var('func_589')
func_591_call = mutated_mod.get_global_var('func_591')
var_4911 = relay.var("var_4911", dtype = "float64", shape = (780,))#candidate|4911|(780,)|var|float64
call_4910 = func_589_call(relay.reshape(var_4911.astype('float64'), [13, 15, 4]))
call_4912 = func_589_call(relay.reshape(var_4911.astype('float64'), [13, 15, 4]))
uop_4913 = relay.cosh(call_4910.astype('float32')) # shape=(13, 15, 4)
uop_4915 = relay.cosh(call_4912.astype('float32')) # shape=(13, 15, 4)
uop_4918 = relay.asinh(uop_4913.astype('float32')) # shape=(13, 15, 4)
uop_4920 = relay.asinh(uop_4915.astype('float32')) # shape=(13, 15, 4)
func_4293_call = mod.get_global_var('func_4293')
func_4295_call = mutated_mod.get_global_var('func_4295')
call_4927 = relay.TupleGetItem(func_4293_call(), 0)
call_4928 = relay.TupleGetItem(func_4295_call(), 0)
output = relay.Tuple([bop_4869,call_4881,var_4911,uop_4918,call_4927,])
output2 = relay.Tuple([bop_4869,call_4882,var_4911,uop_4920,call_4928,])
func_4934 = relay.Function([var_4867,var_4868,var_4911,], output)
mod['func_4934'] = func_4934
mod = relay.transform.InferType()(mod)
var_4935 = relay.var("var_4935", dtype = "float64", shape = ())#candidate|4935|()|var|float64
var_4936 = relay.var("var_4936", dtype = "float64", shape = (15, 8, 6))#candidate|4936|(15, 8, 6)|var|float64
var_4937 = relay.var("var_4937", dtype = "float64", shape = (780,))#candidate|4937|(780,)|var|float64
output = func_4934(var_4935,var_4936,var_4937,)
func_4938 = relay.Function([var_4935,var_4936,var_4937,], output)
mutated_mod['func_4938'] = func_4938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3730_call = mod.get_global_var('func_3730')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_4948 = relay.TupleGetItem(func_3730_call(), 0)
call_4949 = relay.TupleGetItem(func_3731_call(), 0)
func_1364_call = mod.get_global_var('func_1364')
func_1367_call = mutated_mod.get_global_var('func_1367')
const_4951 = relay.const([[-1.628563,6.981920,4.711437,-4.208618],[-8.532169,-0.046851,6.674072,2.375722],[1.268376,-7.125855,-8.755608,-4.403805],[-9.859736,0.978920,6.465370,9.256561],[2.991726,-3.919504,-6.363989,-2.320522],[0.139453,-0.524044,-9.681587,5.925875],[9.675545,-0.505343,3.111277,-2.182200],[-9.679223,-1.269538,3.008446,-0.925246],[-4.192525,4.402006,5.703656,4.519460],[-0.041758,-0.690011,3.449182,-7.111596],[9.030510,-9.458580,-3.395102,-6.070710],[9.652356,-0.109910,-4.099283,7.837090],[9.083424,-1.762711,-0.689922,6.586199],[4.646702,5.279354,-2.710853,-2.819984],[3.785838,-3.879578,5.777460,-8.745039],[7.606028,2.271549,9.749485,-5.796882],[7.551571,-4.308937,-6.958490,0.098894],[5.825045,-6.464222,-8.164561,2.840051],[1.046870,6.510680,-4.446202,0.868176],[-4.025333,-7.889112,5.848451,5.360827],[7.052922,-4.076609,6.495965,7.445945],[8.438470,-3.010638,-2.306566,5.091688],[6.493737,-2.121250,-7.944312,4.458575],[-4.359425,6.944294,-5.612795,4.663548],[-0.847325,0.331057,3.353640,-1.099248],[-3.902459,-9.383738,-5.723287,0.442916],[6.485433,8.084572,0.483965,-9.166931],[-0.461092,-3.820555,-6.283005,-0.619447],[9.006128,6.412815,4.979650,2.237147],[-0.210254,-9.420931,2.608902,4.569129],[-3.460254,9.576469,8.794862,8.317981],[1.789426,3.198672,7.177363,-7.864468],[9.679568,1.505495,1.773376,3.750635],[9.554986,-4.938894,0.272532,6.448003],[-9.651574,7.735265,-8.017510,-6.078907],[-4.702848,-3.635123,2.987128,8.647721],[-0.660586,2.244835,0.155622,7.948019],[1.002021,-6.301156,5.285688,-5.299693],[-8.569788,-9.082284,-9.353842,-8.755571],[-4.185740,6.603930,7.317911,-4.503587],[1.273212,2.063059,-5.883588,9.753946],[-6.409781,-0.282505,8.420261,1.383812],[0.314859,3.466352,-6.841369,-9.868850],[-9.888258,7.033539,-6.677801,0.257245],[5.489154,1.366948,6.632991,8.764935],[-2.299557,-5.580566,-6.018213,8.160543],[2.803933,-9.817194,-5.974979,-9.073218],[-7.468894,-3.929596,2.713637,-4.284325],[-0.260285,0.491165,8.176076,4.969732],[-3.488758,3.609195,4.912382,-4.216739],[1.167306,6.435142,-4.487149,-1.421404],[4.872476,0.843460,-8.708487,8.015764],[6.499964,5.805212,-1.512494,-8.908841],[-1.611166,9.906445,-1.063545,-0.818711],[-3.573308,7.760713,0.285774,7.245832],[-3.541490,0.730843,5.070608,0.813469],[0.468416,5.590257,2.463585,3.235197],[0.134497,-1.002306,-5.460528,-4.449919],[-6.998886,4.484071,3.027272,-1.907543],[-9.698683,0.066669,-5.323929,-8.932528],[7.599755,0.241446,-3.151234,-1.527354],[-7.611673,9.780122,0.853674,5.515953],[-6.502319,0.318581,-0.463248,5.789436],[1.781685,-3.660328,-1.578324,-1.713327],[-6.218543,-5.201535,-1.388422,-9.434065],[6.133616,8.075847,6.706128,-7.845702],[-6.925481,-6.667640,7.861249,3.844933],[-4.563852,4.468035,-7.882837,-1.938918],[8.556849,2.959174,8.347512,-5.974784],[-3.263928,1.615176,0.558815,0.822592],[2.488563,-0.251475,9.084019,6.845282],[6.135834,-6.572707,-0.577180,-1.078664],[-9.327845,6.285739,4.252438,-6.689906],[-6.135500,-3.577679,-2.993139,3.226329],[8.953554,-1.174762,6.510817,-9.158588],[-0.143242,-8.248839,8.552777,7.178381],[3.489668,1.343492,-7.682321,-4.861746],[2.539546,-2.184388,-7.490571,3.898062],[3.655418,-1.726222,4.180500,4.040707],[-2.976212,8.460277,-5.314092,0.786135],[8.991567,7.958127,-5.182292,-0.488617],[-3.667936,0.603697,-8.131862,-8.493321],[5.136686,-5.406991,2.549035,-8.236785],[-5.196214,5.581381,-9.896127,-0.304498],[3.684326,-4.108937,1.963514,6.022247],[5.429592,-4.352386,0.143071,-5.815355],[0.276616,2.575772,-3.471617,-7.036165],[1.306854,-9.594140,-9.947621,-8.205716],[-0.889447,-3.386794,1.295258,5.347487],[-5.084880,5.327936,-3.642219,-8.072235],[-8.996262,-1.377900,-2.012882,1.411721],[-6.617754,7.153595,-1.238746,-5.991533],[-8.226728,-6.918316,-5.849541,4.735083],[6.202337,-5.815426,-8.139176,-2.822591],[-7.124171,1.079749,3.809706,2.868431],[-4.788919,3.417505,-4.631390,9.551055],[-6.048573,-8.235262,6.334409,6.576303],[-9.768815,-5.016051,7.360056,-2.465325],[3.591873,-0.491687,-8.421470,-5.170470],[-8.377866,-9.921399,5.256185,-6.442436],[6.305061,-2.583191,-2.679735,-7.185322],[2.803785,1.339795,7.148689,5.041691],[4.183693,3.627724,6.129041,5.646486],[4.964079,-4.362284,5.181691,-8.771515],[8.373330,-3.889857,1.205438,7.038230],[4.123110,9.330242,-2.952293,-4.200808],[-5.228406,0.271280,4.183828,5.918217],[-8.225817,-5.991077,-6.694733,7.089104]], dtype = "float32")#candidate|4951|(108, 4)|const|float32
const_4952 = relay.const([-6.550450,-3.944182,9.711882,-3.967480,-1.049043,-8.079131,-9.361474,-5.649150,-9.231349,3.760113,5.877742,-6.986660,-8.673331,9.913059,8.606704,-6.966483,5.943218,-9.787976,-3.674863,-7.923518,2.450636,0.790665,7.943061,5.011185,-1.203967,-2.012228,-1.108880,0.645516,-3.823149,0.961928,-4.499167,1.280491,-9.258656,-0.195333,-0.684004,7.386700,9.375791,-4.733449,-6.583302,-6.340751,-5.125339,-3.591920,-2.132515,9.292556,-3.007231,-7.715940,0.948564,8.597935,0.974450,-5.067067,-0.070764,8.669344,1.948012,-3.473181,-6.928087,-9.737885,-7.572682,1.145497,-5.345502,3.064680,6.815819,0.602404,-0.263157,-4.014771,5.498696,6.399938,-6.439911,7.375138,-2.462244,8.098162,8.742344,8.240552,-0.750272,-7.485577,-9.945567,-2.788359,1.242408,-7.218554,-8.420594,-4.423948,4.490777,4.909851,-5.304075,8.400952,4.711729,2.224764,-2.175995,-2.843894,-1.963661,-8.468563,-0.210437,-9.614446,-8.506895,7.155748,-1.250577,-7.793096,-3.733651,8.901488,0.757336,2.278054,-1.470239,3.173383,-4.014503,0.049301,-1.820848,0.963932,-7.887523,-2.221604,-0.717460,7.369052,6.231235,-0.410522,-5.029820,4.745807,3.429700,-3.900658,5.902369,-4.328088,1.529982,-5.532419,2.838428,-4.422275,-6.969764,5.398811,7.616602,9.882015,-9.169680,-5.489852,8.794184,-8.877765,-5.063870,-3.910274,-6.660207,8.650917,1.447258,0.392196,1.264858,-0.300611,7.191270,-7.748324,6.343490,5.623425,-9.517740,-8.434142], dtype = "float64")#candidate|4952|(144,)|const|float64
call_4950 = relay.TupleGetItem(func_1364_call(relay.reshape(const_4951.astype('float32'), [3, 12, 12]), relay.reshape(const_4952.astype('float64'), [144,]), ), 1)
call_4953 = relay.TupleGetItem(func_1367_call(relay.reshape(const_4951.astype('float32'), [3, 12, 12]), relay.reshape(const_4952.astype('float64'), [144,]), ), 1)
output = relay.Tuple([call_4948,call_4950,const_4951,const_4952,])
output2 = relay.Tuple([call_4949,call_4953,const_4951,const_4952,])
func_4982 = relay.Function([], output)
mod['func_4982'] = func_4982
mod = relay.transform.InferType()(mod)
output = func_4982()
func_4983 = relay.Function([], output)
mutated_mod['func_4983'] = func_4983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3711_call = mod.get_global_var('func_3711')
func_3712_call = mutated_mod.get_global_var('func_3712')
call_5083 = func_3711_call()
call_5084 = func_3711_call()
output = relay.Tuple([call_5083,])
output2 = relay.Tuple([call_5084,])
func_5085 = relay.Function([], output)
mod['func_5085'] = func_5085
mod = relay.transform.InferType()(mod)
mutated_mod['func_5085'] = func_5085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5085_call = mutated_mod.get_global_var('func_5085')
call_5086 = func_5085_call()
output = call_5086
func_5087 = relay.Function([], output)
mutated_mod['func_5087'] = func_5087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_5108 = relay.TupleGetItem(func_3507_call(), 0)
call_5109 = relay.TupleGetItem(func_3508_call(), 0)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_5123 = relay.TupleGetItem(func_3161_call(), 0)
call_5124 = relay.TupleGetItem(func_3162_call(), 0)
output = relay.Tuple([call_5108,call_5123,])
output2 = relay.Tuple([call_5109,call_5124,])
func_5157 = relay.Function([], output)
mod['func_5157'] = func_5157
mod = relay.transform.InferType()(mod)
mutated_mod['func_5157'] = func_5157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5158 = func_5157_call()
output = call_5158
func_5159 = relay.Function([], output)
mutated_mod['func_5159'] = func_5159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_5175 = relay.TupleGetItem(func_3785_call(), 0)
call_5176 = relay.TupleGetItem(func_3787_call(), 0)
func_2653_call = mod.get_global_var('func_2653')
func_2659_call = mutated_mod.get_global_var('func_2659')
const_5181 = relay.const([0.972070,3.380981,-1.260227,6.435052,8.770144,-2.269046,-7.429891,2.450488,-3.059225,3.287238,8.491416,1.548371,3.327626,-9.546581,8.519127,-6.537554,7.749422,-8.063628,8.502994,-9.150578,2.674976,1.671137,4.441953,5.714327,-1.680045,3.751407,-1.080139,-2.319938,-2.219700,-0.405582,5.449744,6.995867,-9.860047,-5.947476,1.938554,1.415152,-9.640453,-2.096265,3.400314,4.828692,2.648277,-2.874834,-6.781878,6.934896,0.821005,-2.073657,7.383624,7.258550,6.782755,5.612200,8.273991,2.994308,-1.900242,1.383598,-0.555125,2.328556,-0.617311,6.779805,-4.034420,0.484313,-1.326866,-9.135271,0.560087,9.428102,-5.901486,0.079071,4.646131,4.928670,7.875536,-2.982725,8.010757,5.373036,6.540507,-3.379640,2.048145,4.468262,4.872075,1.104582,0.822925,4.066461,-5.943466,3.184457,-6.812728,7.560591,-6.328891,6.744015,3.024545,1.189876,7.721806,-0.826952,3.228657,-6.093778,-3.220072,-7.743537,-1.054757,3.364213,-8.687414,5.748514,6.286056,-1.298356,-2.561502,2.252880,-9.335660,-3.416241,5.284336,5.505453,-8.135088,7.964422,4.955505,-0.950894,-6.442785,-1.666572,8.265880,8.059784,-2.275801,-9.833777,8.861765,-6.692292,-9.731093,1.206156,-3.994489,-8.730977,-5.418451,9.451581,5.651678,1.973120,1.329573,6.073261,1.003825,8.016810,-3.741427,-4.613332,8.760145,-4.430130,6.955951,9.494278,-0.704073,-1.418856,-1.255222,-3.884671], dtype = "float64")#candidate|5181|(140,)|const|float64
var_5182 = relay.var("var_5182", dtype = "float32", shape = (1430,))#candidate|5182|(1430,)|var|float32
var_5183 = relay.var("var_5183", dtype = "bool", shape = (5, 63))#candidate|5183|(5, 63)|var|bool
call_5180 = relay.TupleGetItem(func_2653_call(relay.reshape(const_5181.astype('float64'), [140,]), relay.reshape(var_5182.astype('float32'), [13, 10, 11]), relay.reshape(var_5183.astype('bool'), [35, 9]), relay.reshape(var_5182.astype('float32'), [13, 10, 11]), ), 4)
call_5184 = relay.TupleGetItem(func_2659_call(relay.reshape(const_5181.astype('float64'), [140,]), relay.reshape(var_5182.astype('float32'), [13, 10, 11]), relay.reshape(var_5183.astype('bool'), [35, 9]), relay.reshape(var_5182.astype('float32'), [13, 10, 11]), ), 4)
output = relay.Tuple([call_5175,call_5180,const_5181,var_5182,var_5183,])
output2 = relay.Tuple([call_5176,call_5184,const_5181,var_5182,var_5183,])
func_5189 = relay.Function([var_5182,var_5183,], output)
mod['func_5189'] = func_5189
mod = relay.transform.InferType()(mod)
mutated_mod['func_5189'] = func_5189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5189_call = mutated_mod.get_global_var('func_5189')
var_5191 = relay.var("var_5191", dtype = "float32", shape = (1430,))#candidate|5191|(1430,)|var|float32
var_5192 = relay.var("var_5192", dtype = "bool", shape = (5, 63))#candidate|5192|(5, 63)|var|bool
call_5190 = func_5189_call(var_5191,var_5192,)
output = call_5190
func_5193 = relay.Function([var_5191,var_5192,], output)
mutated_mod['func_5193'] = func_5193
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5248 = relay.const([[[-9.254725,-6.697234,6.796129,-8.414066],[-2.788291,4.422049,-0.840526,4.981962],[6.678567,-7.381321,3.642943,3.406011]],[[-5.536208,-5.887612,-7.299961,-8.832732],[-3.309946,-7.053736,8.064589,7.525385],[9.685068,2.446000,-1.531662,1.414437]],[[-2.880022,2.920092,-6.252203,6.502946],[8.522122,6.768061,4.817577,-7.266385],[9.715068,1.206130,2.554357,-5.050683]],[[4.059998,-7.937273,-3.102506,3.254104],[9.884705,-3.965931,-1.622299,-1.668062],[0.433762,8.601852,7.320878,3.695484]]], dtype = "float64")#candidate|5248|(4, 3, 4)|const|float64
uop_5249 = relay.atanh(const_5248.astype('float64')) # shape=(4, 3, 4)
func_4596_call = mod.get_global_var('func_4596')
func_4598_call = mutated_mod.get_global_var('func_4598')
call_5256 = func_4596_call()
call_5257 = func_4596_call()
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_5270 = relay.TupleGetItem(func_5157_call(), 0)
call_5271 = relay.TupleGetItem(func_5159_call(), 0)
output = relay.Tuple([uop_5249,call_5256,call_5270,])
output2 = relay.Tuple([uop_5249,call_5257,call_5271,])
func_5272 = relay.Function([], output)
mod['func_5272'] = func_5272
mod = relay.transform.InferType()(mod)
mutated_mod['func_5272'] = func_5272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mutated_mod.get_global_var('func_5272')
call_5273 = func_5272_call()
output = call_5273
func_5274 = relay.Function([], output)
mutated_mod['func_5274'] = func_5274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mod.get_global_var('func_4641')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_5342 = relay.TupleGetItem(func_4641_call(), 0)
call_5343 = relay.TupleGetItem(func_4643_call(), 0)
var_5344 = relay.var("var_5344", dtype = "float32", shape = (16, 10, 11))#candidate|5344|(16, 10, 11)|var|float32
bop_5345 = relay.bitwise_or(call_5342.astype('uint16'), var_5344.astype('uint16')) # shape=(16, 10, 11)
bop_5348 = relay.bitwise_or(call_5343.astype('uint16'), var_5344.astype('uint16')) # shape=(16, 10, 11)
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_5354 = relay.TupleGetItem(func_3218_call(), 0)
call_5355 = relay.TupleGetItem(func_3219_call(), 0)
func_2340_call = mod.get_global_var('func_2340')
func_2342_call = mutated_mod.get_global_var('func_2342')
const_5364 = relay.const([True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True], dtype = "bool")#candidate|5364|(80,)|const|bool
call_5363 = relay.TupleGetItem(func_2340_call(relay.reshape(const_5364.astype('bool'), [80,])), 0)
call_5365 = relay.TupleGetItem(func_2342_call(relay.reshape(const_5364.astype('bool'), [80,])), 0)
output = relay.Tuple([bop_5345,call_5354,call_5363,const_5364,])
output2 = relay.Tuple([bop_5348,call_5355,call_5365,const_5364,])
func_5370 = relay.Function([var_5344,], output)
mod['func_5370'] = func_5370
mod = relay.transform.InferType()(mod)
var_5371 = relay.var("var_5371", dtype = "float32", shape = (16, 10, 11))#candidate|5371|(16, 10, 11)|var|float32
output = func_5370(var_5371)
func_5372 = relay.Function([var_5371], output)
mutated_mod['func_5372'] = func_5372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_5406 = func_3152_call()
call_5407 = func_3152_call()
output = call_5406
output2 = call_5407
func_5414 = relay.Function([], output)
mod['func_5414'] = func_5414
mod = relay.transform.InferType()(mod)
mutated_mod['func_5414'] = func_5414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5414_call = mutated_mod.get_global_var('func_5414')
call_5415 = func_5414_call()
output = call_5415
func_5416 = relay.Function([], output)
mutated_mod['func_5416'] = func_5416
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5498 = relay.const([[[-7,-8,4,-6,-6,-5,-3,10,-2,2,-4,-9,-10],[-9,2,-10,-6,9,-10,5,5,-2,10,8,10,-3],[-2,-5,5,-5,-4,7,-7,-2,-1,-2,6,7,-6],[8,-4,4,-3,-6,-3,-7,-8,-6,1,4,4,10],[-10,6,1,-3,6,9,-6,-10,-10,5,1,4,9],[6,4,5,-3,9,6,-9,3,2,4,8,8,3],[5,3,-5,-9,-5,10,-5,3,5,4,9,7,5],[-9,-9,4,10,-9,-6,-2,3,10,3,1,-5,-5],[-8,-8,-6,-8,9,-10,-9,2,5,8,-5,8,-4],[-7,-2,3,-3,-3,-8,-5,-2,6,1,-9,-1,6],[9,-8,-3,-2,-7,4,-4,8,-9,8,7,-7,1],[7,-4,2,9,4,4,4,1,-1,9,8,4,1]],[[2,-2,-3,9,-5,9,-10,3,-1,7,-9,8,8],[5,-3,-5,-4,10,-9,-5,9,-6,10,-6,8,-4],[2,4,9,-3,-6,7,-7,-9,7,1,-1,8,-8],[-4,-8,3,2,9,7,-6,-2,4,2,-6,-7,-5],[-5,10,7,-10,-4,-4,-2,-10,9,-3,8,10,1],[9,4,6,8,1,-10,2,-5,10,3,8,7,3],[-7,5,1,-5,1,4,-9,-9,-7,-3,-9,-2,5],[6,-9,7,-2,-5,-10,9,4,-5,2,2,-4,4],[9,8,5,-8,-3,-4,1,9,2,5,3,10,1],[-5,-8,10,6,-5,-2,-5,10,-1,9,-2,-9,-8],[4,-10,-4,2,5,-1,-10,1,-9,-6,-6,-10,6],[-7,-9,-9,-4,10,5,10,-3,-2,7,-4,10,7]],[[-6,10,-9,9,1,-2,9,5,-3,-6,5,-9,1],[-1,3,6,5,1,2,-3,-8,-2,-9,10,1,10],[6,-10,-3,10,9,5,-4,9,4,3,-6,-10,-9],[7,-8,7,6,-3,-8,-5,10,2,-4,-2,-2,-4],[-9,3,5,-7,7,-7,1,2,-4,8,-6,-10,1],[1,-8,-2,-9,4,-5,5,4,6,3,-5,-4,-10],[3,-3,1,-8,10,5,-6,-1,7,4,-9,5,8],[-8,-4,5,8,2,3,-8,3,-10,10,10,7,-9],[4,-10,-5,-7,7,-6,1,6,-1,4,-8,1,-6],[-7,4,-1,1,1,2,-7,-1,5,5,5,-6,10],[-3,-1,-3,-4,-6,5,8,7,7,8,9,1,5],[-1,-7,4,-3,1,-5,3,1,1,8,-1,2,-3]],[[5,6,-10,-2,10,-6,-2,9,1,-1,3,-6,-9],[-4,-6,-3,-10,4,8,6,-1,10,-9,-1,2,5],[-3,4,7,1,6,-8,-5,-6,-6,8,3,1,7],[-4,-5,4,-1,-9,8,-6,6,-1,-6,-3,-9,2],[-8,-6,6,-6,3,10,-10,-4,9,-5,4,5,4],[2,8,7,-6,3,-5,6,8,-1,3,9,5,-6],[-1,-9,-8,8,3,-1,10,-5,-2,-4,5,1,3],[1,-5,9,9,-10,-8,-10,-6,2,-5,-3,-5,7],[2,-9,7,3,6,-7,9,-9,-8,8,2,-9,6],[-3,-9,-3,10,4,-10,9,-10,-1,6,5,-1,-7],[4,9,10,-3,4,-7,-7,-10,-1,-3,7,-1,-3],[4,-1,6,-7,-7,7,-5,7,-3,-5,1,4,-7]],[[9,-4,4,8,-9,1,1,4,-10,-9,10,-9,-9],[-1,8,3,-7,2,5,7,8,1,-7,-7,3,-4],[-2,-10,-5,3,10,-1,-3,10,-6,-3,6,2,-2],[-2,7,-9,-9,9,1,-9,7,10,4,-9,9,-5],[-9,-2,-7,7,-10,-4,-7,-5,4,9,-6,3,-1],[2,-6,8,-5,-8,3,-8,-2,-4,-7,5,-4,3],[7,2,8,-1,3,2,8,-10,-3,-5,-3,4,-5],[1,7,-9,-2,4,7,6,3,-7,8,-3,8,-8],[5,10,2,1,-7,-4,3,1,-3,9,-5,-8,-6],[3,-9,4,4,-5,-7,-6,9,3,9,-4,-3,8],[-1,-10,-9,10,6,1,-8,-6,3,9,-1,-5,-8],[-3,-4,-8,9,-4,3,-6,8,8,-2,-10,6,10]],[[-4,8,-6,5,-1,-6,1,9,-4,2,2,9,-4],[-10,10,8,7,-10,-4,-6,5,7,4,9,-1,-9],[1,-9,-8,-5,-1,4,8,2,6,9,1,-9,-4],[-2,-1,9,10,-7,7,7,-5,-5,-7,-7,6,-6],[3,-2,6,-1,-7,-9,8,-5,7,2,-7,9,5],[-6,-1,8,2,1,3,4,-2,-7,8,3,6,-1],[2,4,5,8,4,10,-7,-3,2,-2,-2,-3,3],[-10,-1,1,-1,1,-6,-2,7,8,2,4,-1,-6],[-7,5,-7,6,-6,-1,1,2,1,10,5,-1,1],[1,-4,-5,8,-9,-5,-2,2,-7,-5,2,1,5],[-2,-5,2,3,4,6,-9,8,-2,4,-4,-8,-10],[-7,4,8,-8,9,10,-5,1,8,-8,6,9,-5]],[[1,-3,6,1,-4,6,-2,2,-6,-6,-10,-8,3],[10,4,-4,-9,-7,9,-4,8,4,4,2,5,-8],[-4,-5,2,8,1,2,-3,2,8,-6,6,6,6],[-4,8,5,-10,-1,-8,-10,-5,8,1,9,-7,-6],[4,5,-2,2,2,-5,2,7,-7,8,9,-9,7],[10,4,7,9,-10,4,4,1,-10,-5,2,4,-3],[5,3,-1,-6,-10,3,-8,2,-6,7,6,-10,-2],[5,2,7,2,-1,-3,-8,-1,-4,-3,-10,5,-4],[-3,-3,9,-1,6,10,9,2,8,7,-8,-10,-9],[10,8,-6,10,-7,7,-10,9,-2,-1,2,-2,-1],[-4,-3,-1,-9,-9,-1,-4,8,8,4,-7,-6,1],[-10,-9,-5,-3,-5,3,5,-9,-1,-5,-2,-6,-10]],[[3,5,-4,-8,5,-5,4,-5,4,-7,8,-3,6],[8,4,-8,4,10,6,10,-1,-4,-2,2,-10,-8],[8,3,-9,-7,-9,-7,-8,-10,4,8,2,10,2],[2,10,10,1,1,6,-2,-5,-7,-7,7,-6,7],[-8,6,9,-10,7,-9,5,10,-10,-6,1,-5,-2],[-10,-9,6,5,5,-9,-5,9,7,-5,-7,9,-9],[-9,-9,-9,9,5,5,-7,-6,-7,5,6,-2,-10],[8,-4,-10,-1,4,-7,8,-10,1,-3,-6,-7,-8],[6,6,1,-7,-8,8,7,3,-6,-5,-4,-4,3],[-9,2,3,-9,3,-2,-3,-9,-2,-4,10,6,4],[2,-10,7,-5,-7,4,7,6,-10,-2,1,-5,10],[4,-1,-7,6,7,-7,2,-1,1,-6,9,-7,2]],[[6,-2,-3,2,5,-8,-9,4,-9,1,3,-10,-9],[4,2,4,5,6,-2,-3,-10,-8,8,-2,-8,-7],[-4,-1,-7,-1,-3,1,-2,-6,-5,-1,-2,1,-1],[-8,-7,2,-3,-6,-10,-3,1,8,9,8,-5,-9],[8,-10,5,1,-3,3,8,8,6,8,3,3,-2],[-6,-1,-7,-4,-1,-2,-1,5,-3,-5,10,2,1],[8,7,-6,-8,-9,8,-9,-4,-9,-10,-3,7,5],[9,7,-3,1,-4,5,4,6,-1,8,10,4,-4],[-4,-3,8,4,-10,-8,-7,10,4,-9,-7,-5,-8],[4,4,9,9,-7,-5,-2,-8,-10,3,-10,-5,7],[-1,-8,-9,3,10,-3,7,6,1,-7,-8,-5,-6],[-8,-3,-4,9,-7,4,-4,-3,3,-7,2,-9,-6]],[[-7,-8,5,5,-4,4,10,-4,1,-9,6,-6,3],[2,8,-8,8,-7,5,1,-10,-5,-6,3,8,4],[5,1,-10,1,1,-1,7,-2,-10,2,-7,8,-5],[-3,-6,8,-8,9,-2,-6,-10,-1,-4,1,-5,-4],[1,8,-7,-10,-9,-2,9,-7,-4,3,-9,-4,7],[-7,-8,9,-2,-7,9,10,6,-6,-7,-6,-3,8],[-5,-3,6,7,10,7,-2,-1,-10,8,6,2,5],[6,-9,10,-5,-8,-4,8,10,5,10,4,10,-7],[-6,-10,9,10,10,-1,2,9,4,-9,-5,-10,-4],[-4,-6,1,-1,4,-6,-7,-6,-5,-8,4,4,-8],[-2,3,-3,-10,-9,3,-9,10,-3,4,-9,-8,3],[-1,-9,-5,7,7,-4,-1,8,-3,-2,4,3,-7]],[[-9,9,8,1,9,10,-4,6,-6,3,10,2,-2],[-9,8,-7,-10,-3,6,-10,9,-1,-1,-3,5,-2],[1,-8,2,-7,-3,9,3,-6,5,-6,-7,9,5],[4,5,6,2,10,1,-6,4,-8,9,-5,-9,9],[7,4,8,-3,-4,3,-1,1,10,4,3,10,7],[6,-8,4,3,-9,-5,-7,9,6,3,-2,5,7],[-2,-1,4,-7,-2,-6,-8,-9,-7,-6,6,-6,9],[2,-4,3,-5,4,-2,10,3,-1,2,6,6,-6],[3,-1,-10,10,1,-9,-10,6,6,-5,5,-10,8],[6,9,4,4,8,-8,7,2,6,10,3,9,7],[-8,10,-4,-7,10,6,-9,-7,1,-6,1,6,-3],[9,10,5,2,3,-4,8,-6,-8,-9,3,1,6]],[[1,-5,-2,6,10,-2,-7,-8,-7,-4,3,9,-1],[1,-10,-5,-8,7,5,-5,-5,7,2,-2,4,-4],[-10,-6,-3,-2,-5,-6,-7,4,-6,-7,4,4,1],[-6,4,1,-1,4,5,9,-2,2,7,3,5,-6],[-6,-6,8,2,-2,-5,-10,-8,-4,-5,-1,-10,-3],[4,5,-6,10,-9,-5,-10,6,1,4,-2,-4,9],[-6,-4,1,8,7,8,7,8,10,9,3,3,9],[8,-4,9,-5,10,2,-2,1,8,7,10,-4,-3],[-10,4,4,1,8,-10,4,9,-8,-4,-10,7,-8],[5,7,-9,-6,6,-5,-8,8,6,-7,-5,3,-4],[-2,10,-9,4,-3,-4,-7,7,-7,5,-2,-7,-5],[4,2,10,-8,-7,-5,6,5,-7,2,6,-10,5]]], dtype = "int32")#candidate|5498|(12, 12, 13)|const|int32
const_5499 = relay.const([[[-1,-7,5,7,5,-10,10,10,6,8,7,8,-8],[-4,-2,2,9,-8,3,6,-7,-2,-6,-1,-4,-10],[2,4,7,-10,-4,-4,-10,-7,10,-1,-10,6,-5],[-8,7,-9,-6,-8,-2,3,1,-1,2,3,1,-8],[7,9,-4,-1,7,-1,5,-7,10,-3,7,-1,9],[-10,-10,-3,6,-8,-9,1,-1,8,-4,2,-2,4],[-8,10,-10,10,-3,-6,-3,9,-3,7,-5,-1,7],[-2,6,-2,-10,4,5,10,4,-6,10,10,-6,-9],[-9,7,-2,9,-4,4,3,3,-1,5,9,-4,-7],[-2,1,-1,2,8,-8,5,10,-5,7,-3,1,6],[1,8,-6,8,-4,8,10,1,7,-1,5,-9,4],[-1,-2,-4,8,-1,-4,2,10,3,7,10,-10,-10]],[[7,-7,3,-7,-6,-8,-4,-9,-7,-8,2,-9,-7],[-3,-1,2,-4,10,-7,-2,9,9,10,6,10,8],[-5,-3,7,-1,-10,-6,-2,-2,5,-3,-6,10,4],[-7,9,-8,-2,9,8,-8,3,-3,-2,5,10,2],[2,-6,-5,3,-6,-8,-4,6,9,10,-7,6,-1],[5,-10,-9,-8,-1,6,8,-4,10,5,10,9,-5],[-7,6,-3,9,-9,-6,-1,-1,-10,1,-5,-2,7],[2,3,2,10,6,-10,-5,-3,-7,7,-3,5,10],[5,10,-5,-7,2,8,9,3,1,10,2,-8,3],[7,5,8,1,-1,-10,7,-8,-4,-1,6,-7,-5],[4,-8,-5,7,-2,2,-2,-2,-1,-4,3,6,5],[7,-10,2,6,-3,5,-2,4,2,5,8,-2,5]],[[-2,-1,-4,-2,-1,-8,-4,-7,-10,6,3,10,2],[5,2,-9,-10,-5,9,9,-10,6,-10,3,-3,4],[8,5,-3,2,-8,-2,-1,5,2,9,-2,8,-7],[-4,1,-6,1,7,-2,9,-1,-10,-8,4,8,-4],[8,6,2,-8,7,9,7,-2,-8,9,-4,6,6],[3,-3,6,-8,9,-2,10,4,7,-9,10,-4,7],[-10,1,2,9,9,-9,8,7,-6,9,-8,1,7],[-3,10,10,-4,5,-3,3,2,8,-9,-9,-2,5],[7,7,5,7,-3,-7,-6,-5,9,-2,10,-10,-7],[-4,-7,10,4,10,-9,-9,1,-9,10,-7,-2,9],[-1,10,8,-6,6,-1,-5,-4,-7,9,10,-7,4],[9,-5,9,-7,-1,-7,-10,-6,3,-1,8,-9,5]],[[6,10,-8,-7,9,-8,-5,1,-9,-4,3,6,4],[1,-2,-3,-10,8,3,-2,1,9,10,-9,3,4],[3,-2,-6,2,-1,8,-9,-3,2,-5,7,3,7],[8,7,8,6,7,-2,1,6,-7,6,9,5,-2],[-9,-2,7,8,4,2,-5,1,9,-1,1,-2,-5],[-4,-5,3,-9,2,-4,10,6,7,2,-9,10,-6],[7,6,6,-2,-6,7,-1,1,-1,3,-4,9,6],[7,-9,7,-10,7,2,-9,6,4,-6,1,8,5],[4,-8,-3,8,-7,-5,7,2,-3,8,6,-5,8],[10,-1,8,8,-8,10,-2,-9,3,-10,5,-8,1],[4,-6,5,8,10,3,-3,-8,5,1,8,-9,-1],[-10,-9,2,-8,-8,4,-8,4,-2,-10,-10,-2,-10]],[[5,9,-6,-4,9,-10,4,-9,-4,3,-8,-4,7],[7,5,2,-7,-7,-9,9,4,-6,-7,-7,3,10],[-6,4,-8,-5,-8,-4,-9,9,-1,7,-10,-6,-1],[10,4,9,-4,-3,6,7,8,-9,4,4,-8,3],[-7,7,-3,-2,-6,-4,4,3,7,3,1,2,-2],[3,1,-8,-4,-4,1,-3,-7,-9,4,10,-4,-9],[-5,-2,-9,-6,10,9,-10,-2,-1,10,-2,8,3],[-9,10,-3,1,1,2,-2,-3,6,-6,-6,3,-4],[7,1,1,-8,-10,-8,-8,-4,-8,3,-9,-7,-9],[-3,-9,9,10,-7,-2,6,7,4,6,-8,-4,8],[-9,-10,7,3,10,-5,2,5,-8,7,-6,-3,-10],[-7,-1,2,1,2,-5,8,-7,-8,-3,-4,-4,6]],[[-5,-2,-1,1,-3,4,5,4,1,7,-2,-8,10],[8,4,-3,7,5,-4,10,9,3,-1,6,-10,-1],[-10,9,-2,3,5,8,1,7,-10,-5,4,5,-7],[-1,-5,-9,-3,2,-7,5,1,3,-5,-9,1,5],[4,-3,2,7,-6,2,-7,7,1,8,-3,6,-1],[-4,3,-8,-1,7,4,-3,-10,-10,-9,-3,-6,2],[1,-9,7,7,-1,6,-5,-7,8,-9,-3,7,7],[2,-8,5,6,-4,-5,10,5,10,-10,-10,5,7],[10,1,2,3,2,1,-1,-9,-5,6,7,-9,1],[3,9,-5,4,8,-3,-9,-10,1,7,-10,10,-10],[2,-2,-9,10,-5,-8,-4,6,-7,10,-5,-1,-10],[-3,-6,7,-4,-2,6,-2,-8,-1,-7,10,9,-3]],[[1,-7,4,-3,-4,-10,-9,-3,4,-7,6,-7,-4],[8,6,-10,-7,2,-10,4,5,-4,4,-1,-3,-3],[8,-1,-6,8,10,1,-6,9,-7,-9,6,-9,1],[1,10,-10,-3,-1,-9,10,-6,7,1,-5,2,1],[7,10,-9,1,-6,-8,-3,-5,7,-2,-4,2,-8],[4,-2,7,4,-9,-8,-2,3,-3,-8,-9,-4,7],[-1,-7,-7,8,-7,-3,2,-4,4,5,8,6,-8],[3,5,2,-9,4,10,-7,6,-8,4,9,9,-9],[-3,3,9,3,-5,9,-4,2,-6,-2,1,-1,1],[-4,3,7,6,7,-7,-9,-7,-8,1,6,-9,10],[-8,6,8,-2,-1,10,1,5,10,-10,-2,6,8],[-1,-10,-8,1,-2,4,-3,-4,-4,-10,3,-3,-5]],[[-5,8,-4,-2,-1,5,-6,2,-2,5,-6,3,8],[-4,-10,5,1,-9,-4,9,5,7,10,1,4,10],[-7,-6,8,9,10,-3,7,3,-7,7,6,-3,-3],[10,2,-7,-2,7,6,8,-8,-6,7,6,-4,5],[-7,6,-3,-7,-8,-6,-1,10,7,-3,1,1,1],[-1,10,-4,-2,-7,1,-10,10,7,8,-9,5,1],[-3,5,2,10,-2,1,9,1,-3,6,6,5,3],[1,7,-6,-4,6,-5,-10,-3,2,-10,-9,-3,-6],[-2,-5,4,3,-7,2,7,1,-6,-10,-3,-10,-3],[-4,6,7,1,-3,9,-8,6,-10,-10,7,-2,-5],[-7,-6,4,9,1,9,2,-7,-9,-7,-7,-8,-8],[2,-1,-4,10,3,1,-5,9,-4,-6,-10,-8,-10]],[[4,1,-4,-1,-10,5,7,5,9,-10,-3,-9,-7],[-6,8,9,5,-5,5,-5,-2,-8,-8,7,-4,-8],[-1,-6,8,3,-7,9,4,-2,-9,-5,-9,10,-5],[-7,-3,-6,1,-5,3,6,-2,-5,-8,-5,-5,-10],[3,-4,-6,-9,-7,5,6,-9,-10,2,-10,8,5],[-5,-6,-7,-4,9,-3,8,5,9,5,-2,-3,-7],[-3,-10,-8,1,9,-5,10,-2,-4,6,-8,-3,-3],[8,-1,-8,7,5,5,1,5,-9,-2,9,-5,-7],[9,6,5,7,-8,-2,-5,2,2,-3,1,-1,3],[1,6,1,-6,-5,-10,8,-7,2,-5,1,-8,-4],[6,-2,-5,7,10,7,4,8,-6,1,-7,7,-7],[-1,3,-6,1,8,-2,9,4,8,10,3,4,-1]],[[-6,3,9,10,9,10,5,-8,-6,9,-5,-9,4],[-2,5,9,4,-7,-8,-4,5,9,-4,7,7,2],[-6,8,-3,8,6,9,1,-4,3,8,-3,-7,7],[9,-3,-6,9,9,-4,10,-6,9,-7,8,10,7],[6,-10,-2,-7,-7,-4,-6,-8,9,10,9,5,-10],[-5,1,-4,9,-10,-1,8,1,-4,-4,-9,4,-8],[-7,-8,-8,-9,-8,5,-7,10,3,5,7,-3,6],[4,1,3,-9,-7,6,5,1,3,7,5,9,-6],[-1,-9,-2,7,9,1,10,2,-6,-2,-6,-2,-6],[3,-6,6,-9,-6,-10,-6,2,-4,7,-10,4,9],[-7,-3,7,10,6,-5,-3,-7,4,3,-3,2,-4],[3,6,-5,1,6,3,-5,4,-5,-9,-1,8,-2]],[[-10,10,-7,-1,3,6,6,-3,-7,-10,-6,-9,9],[-1,3,-7,8,-8,-10,-9,-7,-8,6,3,-10,8],[10,-5,7,-6,-9,-7,2,-5,-4,-5,1,3,-7],[-3,-9,-4,-8,8,5,10,-8,-5,10,-5,4,5],[-5,3,7,8,-8,-7,-3,2,10,4,-6,-10,-8],[-3,7,10,-10,-4,2,3,6,4,4,7,-9,1],[3,6,-8,-6,10,-7,-10,5,4,-1,7,-10,-5],[-4,2,-2,9,-6,6,2,-9,-4,9,-2,9,-3],[-1,9,10,8,3,6,-7,-8,4,9,-6,-4,-6],[10,-2,-6,-4,8,-10,-7,-8,4,-5,8,-10,-5],[-4,5,-7,-7,-8,1,8,7,6,3,-6,9,9],[3,8,8,-8,2,-8,6,10,9,7,-7,9,-8]],[[5,8,-9,-3,-10,-9,-6,6,9,-1,9,8,5],[2,-5,10,-10,-4,-1,7,2,2,8,3,9,-8],[-5,4,-6,-3,-7,-1,-3,-7,5,-10,10,4,-9],[5,2,-6,-4,6,-7,10,-4,-4,-7,-5,-4,9],[6,-2,-10,-1,-2,9,7,5,4,1,-4,7,5],[6,-7,-3,-6,-6,-2,9,5,-10,-3,8,10,-7],[4,8,8,-1,6,-7,-1,-9,3,-8,7,-1,-3],[-10,-10,-7,-3,-6,-8,-7,10,-9,9,5,9,10],[-1,6,10,7,3,4,1,-8,-6,-7,10,-9,-7],[3,-8,-10,4,1,2,-5,5,10,1,9,4,8],[-4,-5,3,-5,-2,8,-10,1,-10,-6,8,-1,7],[-8,5,-7,5,8,-1,-7,-9,-7,7,-3,-4,9]]], dtype = "int32")#candidate|5499|(12, 12, 13)|const|int32
bop_5500 = relay.less_equal(const_5498.astype('bool'), relay.reshape(const_5499.astype('bool'), relay.shape_of(const_5498))) # shape=(12, 12, 13)
func_3730_call = mod.get_global_var('func_3730')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_5511 = relay.TupleGetItem(func_3730_call(), 0)
call_5512 = relay.TupleGetItem(func_3731_call(), 0)
output = relay.Tuple([bop_5500,call_5511,])
output2 = relay.Tuple([bop_5500,call_5512,])
func_5517 = relay.Function([], output)
mod['func_5517'] = func_5517
mod = relay.transform.InferType()(mod)
mutated_mod['func_5517'] = func_5517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mutated_mod.get_global_var('func_5517')
call_5518 = func_5517_call()
output = call_5518
func_5519 = relay.Function([], output)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4293_call = mod.get_global_var('func_4293')
func_4295_call = mutated_mod.get_global_var('func_4295')
call_5639 = relay.TupleGetItem(func_4293_call(), 0)
call_5640 = relay.TupleGetItem(func_4295_call(), 0)
func_4385_call = mod.get_global_var('func_4385')
func_4387_call = mutated_mod.get_global_var('func_4387')
call_5667 = relay.TupleGetItem(func_4385_call(), 0)
call_5668 = relay.TupleGetItem(func_4387_call(), 0)
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
const_5674 = relay.const([2.048201,3.674158,5.227998,-0.059259,7.853667,6.117030,-9.733019,1.528353,-4.263339,5.587534,-0.190471,-5.799276,9.822215,7.521705,-6.397721,5.864312,-2.175921,-1.705282,5.773464,-2.392550,-9.131153,1.634425,8.938388,5.020551,-3.794852,-6.021458,2.730070,2.580706,9.148245,8.974125,-6.004646,4.224890,-8.369224,-9.117034,-4.621573,-9.056493,-3.472834,4.195885,-3.535467,-3.125271,8.191434,0.139572,3.246970,3.992174,4.013709,-9.696062,5.791227,0.860632,7.158530,7.746571,-1.257838,4.770351,-9.658218,5.171160,6.139930,7.562258,-0.876533,9.771327,0.304379,-6.117697,-2.538444,-1.190359,-8.209180,6.572870,6.751843,-4.711443,-6.146068,3.196561,-9.920195,6.956874,-7.107658,1.846845,9.879420,-0.735699,3.657935,2.823398,4.528445,-8.538733,4.079974,5.782577,-2.130023,3.386938,4.280393,7.266810,3.736348,-0.596718,0.830382,-9.258676,-2.014176,1.269642,-1.822756,5.606742,-9.312523,2.127066,7.258516,2.979144,-7.991554,-5.568921,1.920933,-8.619917,-1.631551,-0.068059,-1.139211,-8.786935,3.518075,-1.207339,5.847566,1.956502,8.045399,7.310469,5.193191,2.886809,1.570755,-0.145184,9.649449,7.982233,7.934442,-7.730716,2.322421,-7.309126,-9.079245,-2.523291,0.193256,-4.014200,-2.798725,3.325129,-3.276896,-3.368176,0.083292,-6.592283,9.801505,-7.323216,1.838015,-8.926534,-2.275112,2.185731,7.739656,-9.869623,3.289732,-7.617305,-8.804398,1.369333,-1.602044,3.287848,-8.143957,-4.117450,7.735260,-8.477981,6.288846,8.617090,-5.649897,1.629233,-3.396832,-6.276735,-4.338702,-3.359053,-5.170202,3.629281,9.543186,-9.389967,-8.117467,5.196915,-5.293061,-2.951748,-1.850565,4.845082,-2.781532,-3.900080,-0.180859,-3.872633,6.442118,9.956590,-7.372563,-7.130527,3.300998,-3.814996,-6.816800,-7.642018,0.887754,-9.961327,-8.986027,-2.031225,-3.314001,-1.956358,9.009297,2.757584,5.961723,8.895042,6.739836,2.597822,-1.942291,-1.243075,1.330728,2.648283,1.533839,-7.719385,9.791456,-5.756025,3.669178,-6.418027,8.275293,-5.897712,2.520786,7.431061,4.354394,0.438976,-8.984663,-9.022335,-0.504380,-6.376660,-3.016209,-0.054418,-2.913792,0.051726,7.039608,-9.047136,-8.720845,2.165365,-3.781299,-1.185470,3.957647,-9.298284,-7.678745,7.523062,-6.193095,-9.036034,-7.845606,6.530717,-4.211861,-9.907860,-0.227274,-8.620677,4.350679,-0.339506,-3.951238,-5.194023,7.854041,0.260509,2.618041,-7.336876,2.545188,-3.380217,9.128710,-9.835030,1.286544,9.317442,5.963845,-5.634312,2.208226,4.025073,8.171322,7.544654,-1.844948,-2.327812,8.735938,4.659088,-0.726464,-3.274701,4.311417,4.671779,-2.223562,5.981712,-4.279443,-4.544961,-9.672373,-3.313950,6.652433,-6.168038,-5.654549,-4.413847,-9.858099,-9.600359,3.021706,-1.515609,4.177765,6.335528,8.205198,-8.460636,-7.080997,6.477517,-3.375154,0.827130,-7.474616,7.437188,-8.427041,-4.939331,2.481810,7.915600,-4.030555,-1.457770,0.878733,9.800272,-1.293640,9.948803,-6.068352,5.150557,-3.657910,8.194040,9.034044,8.838981,-6.080787,-9.084890,1.313495,-2.052555,0.458035,6.427318,6.430808,4.072312,-5.289883,-5.242146,-3.025422,6.462131,-1.341135,2.391845,2.444819,-4.850250,-3.410841,-2.398959,-7.179913,2.301348,3.690711,4.791334,1.819916,-2.928413,8.582345,5.079138,-4.010616,-3.033888,7.938441,-1.592016,-5.829127,-6.551892,5.207359,-2.677211,9.169927,-1.473884,6.295590,7.018848,-3.039261,-5.967290,9.544575,8.144686,4.803351,-1.472412,8.402438,9.428843,3.807856,7.788712,-8.542868,7.607670,9.469057,-2.355889,0.045157,-2.155121,8.864953,3.785449,-4.101017,4.910083,-7.996911,-1.911740,-5.287062,5.184491,4.938165,3.624400,5.006515,5.639242,-2.993411,8.830067,-4.526256,6.032586,-6.512473,-6.274357,-9.053238,-7.321407,5.869232,-9.277469,7.249721,-4.159198,-9.542331,-0.842076,-1.244901,3.841160,-5.963791,-9.919691,-7.039450,-9.805800,-4.748085,7.537984,-0.801395,5.620011,-7.619317,-7.299606,8.783634,-5.367057,-2.338129,7.546929,-0.985265,2.921500,3.609106,2.254059,6.364473,1.338006,-7.476741,-3.115952,-9.711038,5.367371,-9.113729,-6.921320,-4.336363,5.080883,-3.231656,0.013677,0.490073,2.730131,-0.937618,-7.750294,-2.885989,4.337017,-1.240906,-6.694038,8.940144,4.261186,0.557268,6.718528,-0.691488,-8.109600,-8.994727,-0.305053,-7.642273,-7.422595,-4.236300,-0.872803,-2.168769,-5.462383,-1.568255,-9.033276,-0.241347,1.973703,1.731046,6.215699,0.784224,-6.951408,8.023060,-3.216919,-1.105719,-8.970475,5.120172,-1.863443,-2.877394,5.093669,6.362424,-4.255644,1.637440,6.533560,-2.805428,0.018434,-8.147846,7.764090,-4.823363,9.511611,5.048843,6.536333,-3.295185,-0.757937,-2.754883,4.000607,1.139929,3.434753,1.215142,-9.304696,5.985683,-3.726519,3.426703,2.242933,7.686936,7.381111,-5.905797,6.456896,-3.660237,1.401954,7.308412,-9.253332,-3.039244,-6.568440,-7.579171,-5.962755,-8.165683,2.700107,-8.015443,6.898023,0.840816,-8.016907,1.562524,-3.511771,-0.220175,5.992569,3.916122,-5.343722,3.938729,4.233542,7.753355,-6.217483,-7.603452,-6.771547,-0.023781,-5.805242,-9.139366,-3.537406,2.241493,4.102495,-5.770376,5.394344,-4.989897,-5.911492,-0.553277,9.227013,9.533131,8.127624,3.934737,-2.829737,3.554382,8.830046,-1.441418,-0.346377,-0.027058,0.234529,-7.420621,-0.462818,-8.141414,-6.809881,3.581292,0.838597,1.205544,-1.960489,-3.760411,9.344215,-3.454447,7.636489,-1.772552,-4.225549,5.685676,6.024184,-7.679985,-2.371124,-5.288679,-2.781672,-0.441065,-6.655398,-5.225570,-6.983890,-9.208223,2.087431,-1.601998,0.292459,-7.873540,8.803473,7.139846,2.238059,5.192736,-1.434700,-9.518441,5.273319,-3.466177,3.707161,-3.626806,9.786594,1.283471,9.856355,3.621639,-6.871814,-3.667137,1.857166,-8.500718,-8.092316,-2.793220,-5.684595,9.732447,2.744777,1.512448,-2.285402,-6.716468,-1.645679,-9.924617,0.642706,-1.452880,0.528944,-7.826885,-4.918862,9.774165,-5.758204,-7.777994,1.399234,-8.854551,8.735613,7.861022,7.528043,-5.803263,3.049533,-2.197938,-5.713241,-7.322856,0.181727,3.435164,6.129533,-5.722986,-4.617144,-6.949268,-6.373364,2.178772,2.114298,-1.432263,-7.261443,-2.123864,3.756302,6.680540,-8.444170,-3.214164,-7.065889,5.844648,-3.170391,7.286994,-2.300270,-5.809725,-0.525460,1.234482,-0.138089,-3.309597,-4.003378,-1.407024,0.254758,6.108586,0.231087,-1.007645,2.535151,-9.110439,2.252182,2.806205,5.992237,2.588692,6.132274,0.885246,-0.826125,-0.763853,2.081227,-3.003984,-3.864889,-0.552996,9.013581,5.780766,-6.707924,5.927687,3.115597,-8.638436,-8.757139,-5.785709,-3.362632,-6.125928,-6.648888,1.633118,8.324914,-8.050362,1.724419,-5.249930,1.573160,-9.975135,8.672668,-1.636077,-0.946788,7.117211,-0.509512,-9.116881,-9.008685,5.074708,3.141041,-2.698346,-2.029509,2.718045,2.791848,9.254965,6.580392,-6.043743,6.456847,-4.737481,9.219230,-5.541576,4.940265,-3.314602,9.395658,-0.891161,-4.909503,-9.611868,-6.658689,0.242965,4.906027,-0.381865,-7.968278,4.454831,7.283714,6.440399,2.556584,-9.262592,-6.245028,-0.575098,-9.124174,-5.020314,4.580176,-4.621776,-6.593525,8.575403,-8.848576,5.174355,6.917872,-8.668157,-8.054235,9.459774,7.407560,-0.268509,5.415407,-8.667823,-1.790700,-0.061669,3.419854,9.203901,-1.872195,2.485737,-5.302193,1.234596,5.307198,6.977747,4.722801,2.827067,-6.697632,-3.346453,2.923242,-2.557084,-8.197223,6.704099,2.118230,5.962010,-3.614598,-6.217555,9.573833,-1.846591,2.907356,-3.845096,-2.587241,1.529580,-8.008363,-0.297692,-0.794419,7.924339,-7.153027,-3.131959,1.526164,0.631031,-2.335951,-6.718382,-7.218655,-0.058415,-6.230904,-6.071678,9.562235,-8.523014,-2.654063,3.349898,9.866566,4.807773,1.476063,4.967934,3.589348,-2.173513,-1.233890,-0.425572,9.088924,-5.370561,8.128045,2.855248,-6.660620,-1.491394,-4.833778], dtype = "float64")#candidate|5674|(780,)|const|float64
call_5673 = relay.TupleGetItem(func_1222_call(relay.reshape(const_5674.astype('float64'), [780,])), 0)
call_5675 = relay.TupleGetItem(func_1225_call(relay.reshape(const_5674.astype('float64'), [780,])), 0)
func_3115_call = mod.get_global_var('func_3115')
func_3116_call = mutated_mod.get_global_var('func_3116')
call_5677 = relay.TupleGetItem(func_3115_call(), 0)
call_5678 = relay.TupleGetItem(func_3116_call(), 0)
func_2368_call = mod.get_global_var('func_2368')
func_2371_call = mutated_mod.get_global_var('func_2371')
const_5685 = relay.const([-2.990282,-8.064435,4.151140,4.682196,-9.081028,9.701149,6.421122,3.046064,-9.048610,4.043311,-3.026500,-9.297519,-4.361823,-2.301174,-2.441810,-3.694901,2.910529,7.104455,-6.050809,1.662764,3.305330,-2.753902,-6.123569,2.045783,1.938518,-3.510726,9.540247,7.212199,1.363395,5.970285,7.875283,-0.594201,-9.778534,-3.880481,-2.885463,4.817341,-2.299952,4.301981,4.483826,4.361549,3.076484,-5.875104,-7.396990,-7.261043,-3.976236,0.424433,2.050662,-1.069247,-2.246510,8.435085,4.706664,-2.953543,-7.843103,-5.332144,3.234228,-5.881216,4.225831,3.735264,-1.655310,1.609784,4.596580,-0.453454,1.980691,-6.412269,0.369020,-7.882031,-1.966441,-2.151493,-3.509931,-6.339067,2.375361,-0.931198,-4.375800,-1.028228,-5.136103,9.767019,4.543464,-4.390728,-9.732753,-4.728391,-4.712167,-4.389696,6.200885,0.672088,3.313845,6.863196,-8.961190,6.902799,0.761189,9.144336,-4.433290,6.664692,2.426258,-7.404664,-1.399600,5.258919,9.495964,3.130798,2.437190,7.071181,4.355239,9.589749,-6.648608,-6.392534,-7.800117,3.076722,-9.459883,-8.326551,4.784324,3.740965,1.334578,-7.108281,3.157478,-1.874917,7.570106,7.813664,-9.506341,-3.047009,-6.415668,7.685273,9.170341,3.305990,0.867958,2.576704,-9.041431,4.305345,4.925024,-1.013518,8.063391,5.069438,-9.621883,0.585627,0.423696,-4.581439,-8.284743,4.879246,-7.803687,4.235696,-7.675686,-3.598143], dtype = "float64")#candidate|5685|(140,)|const|float64
call_5684 = relay.TupleGetItem(func_2368_call(relay.reshape(const_5685.astype('float64'), [140,])), 0)
call_5686 = relay.TupleGetItem(func_2371_call(relay.reshape(const_5685.astype('float64'), [140,])), 0)
output = relay.Tuple([call_5639,call_5667,call_5673,const_5674,call_5677,call_5684,const_5685,])
output2 = relay.Tuple([call_5640,call_5668,call_5675,const_5674,call_5678,call_5686,const_5685,])
func_5716 = relay.Function([], output)
mod['func_5716'] = func_5716
mod = relay.transform.InferType()(mod)
mutated_mod['func_5716'] = func_5716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5716_call = mutated_mod.get_global_var('func_5716')
call_5717 = func_5716_call()
output = call_5717
func_5718 = relay.Function([], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mod.get_global_var('func_5517')
func_5519_call = mutated_mod.get_global_var('func_5519')
call_5741 = relay.TupleGetItem(func_5517_call(), 0)
call_5742 = relay.TupleGetItem(func_5519_call(), 0)
output = relay.Tuple([call_5741,])
output2 = relay.Tuple([call_5742,])
func_5751 = relay.Function([], output)
mod['func_5751'] = func_5751
mod = relay.transform.InferType()(mod)
mutated_mod['func_5751'] = func_5751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5751_call = mutated_mod.get_global_var('func_5751')
call_5752 = func_5751_call()
output = call_5752
func_5753 = relay.Function([], output)
mutated_mod['func_5753'] = func_5753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5716_call = mod.get_global_var('func_5716')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_5769 = relay.TupleGetItem(func_5716_call(), 1)
call_5770 = relay.TupleGetItem(func_5718_call(), 1)
output = relay.Tuple([call_5769,])
output2 = relay.Tuple([call_5770,])
func_5830 = relay.Function([], output)
mod['func_5830'] = func_5830
mod = relay.transform.InferType()(mod)
mutated_mod['func_5830'] = func_5830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5830_call = mutated_mod.get_global_var('func_5830')
call_5831 = func_5830_call()
output = call_5831
func_5832 = relay.Function([], output)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mod.get_global_var('func_4641')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_5833 = relay.TupleGetItem(func_4641_call(), 0)
call_5834 = relay.TupleGetItem(func_4643_call(), 0)
output = call_5833
output2 = call_5834
func_5846 = relay.Function([], output)
mod['func_5846'] = func_5846
mod = relay.transform.InferType()(mod)
mutated_mod['func_5846'] = func_5846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5846_call = mutated_mod.get_global_var('func_5846')
call_5847 = func_5846_call()
output = call_5847
func_5848 = relay.Function([], output)
mutated_mod['func_5848'] = func_5848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_5877 = func_4536_call()
call_5878 = func_4536_call()
output = call_5877
output2 = call_5878
func_5887 = relay.Function([], output)
mod['func_5887'] = func_5887
mod = relay.transform.InferType()(mod)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5887_call = mutated_mod.get_global_var('func_5887')
call_5888 = func_5887_call()
output = call_5888
func_5889 = relay.Function([], output)
mutated_mod['func_5889'] = func_5889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4596_call = mod.get_global_var('func_4596')
func_4598_call = mutated_mod.get_global_var('func_4598')
call_6006 = func_4596_call()
call_6007 = func_4596_call()
output = relay.Tuple([call_6006,])
output2 = relay.Tuple([call_6007,])
func_6015 = relay.Function([], output)
mod['func_6015'] = func_6015
mod = relay.transform.InferType()(mod)
mutated_mod['func_6015'] = func_6015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6015_call = mutated_mod.get_global_var('func_6015')
call_6016 = func_6015_call()
output = call_6016
func_6017 = relay.Function([], output)
mutated_mod['func_6017'] = func_6017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_6018 = func_4536_call()
call_6019 = func_4536_call()
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
const_6024 = relay.const([3.478304,8.746500,-0.886380,-9.796147,6.245354,-4.576574,-3.617408,-6.692509,-7.703053,-8.356738,-0.993319,-3.496681,-3.717833,-3.944119,2.874715,-8.748906,-3.487944,2.822457,8.750898,1.045122,9.090829,8.255554,8.532296,4.534796,0.062342,7.603633,-8.607975,3.608106,8.231387,-3.847986,3.519562,9.375322,-1.186533,-5.395507,-2.329772,-3.081080,4.561707,-4.146635,3.388487,-1.681784,4.871245,-9.218307,2.627664,-1.733351,4.494091,7.096851,0.282256,0.206660,2.737668,-5.999286,7.663628,0.043816,-3.429681,7.944731,-7.986567,0.161453,8.761037,3.568377,8.406887,3.380725,-5.622658,2.384878,1.654878,3.342408,2.995107,8.294880,3.860080,5.617560,-2.628615,2.194560,5.563280,-8.744378,9.906417,7.448898,8.405306,0.447760,-3.350797,-1.442814,1.517373,-8.150119,5.547773,9.268871,8.398864,-6.793312,-6.940754,-4.944607,-0.981024,-1.805021,-5.396341,-2.505985,9.874760,6.143775,7.750855,5.339130,2.964699,4.225301,7.830789,7.388824,7.040187,-4.001577,-2.601455,8.152504,0.074897,-5.558413,-1.456871,-4.607325,-4.559583,5.710342,3.508871,8.131611,-4.576441,7.098494,3.092190,-6.652666,-0.349441,-6.577934,7.048099,-6.294319,-4.813730,-3.077813,3.725705,-2.401021,-2.366536,4.215804,-4.569670,0.387669,7.886619,4.037667,2.278543,-9.715385,-6.820647,-2.958850,-4.171638,5.022805,1.038547,1.632016,-8.908085,2.861496,8.274178,-7.364244,4.327153,2.912901,-1.805828,7.185167,-1.006949,3.525923,3.235215,8.998530,-0.611479,-7.577380,-0.320774,9.607260,0.598658,-0.388359,1.671554,-5.773184,-8.477970,-0.729671,-2.751593,-7.538987,9.941791,-9.668347,-9.463261,-9.641686,-2.440267,-6.692015,4.417568,7.397638,-3.533579,4.407632,-4.909392,-2.433992,8.323943,6.657891,2.093280,0.049071,4.773720,2.253039,8.309493,6.676513,-1.955382,-4.910508,7.771045,-0.360451,9.806310,4.639915,8.545925,-9.870189,-8.019006,8.192962,-8.361111,-7.358300,-2.860418,2.495211,-0.864526,5.720715,-2.470673,-9.538313,2.782597,-2.368230,-0.116238,-6.694483,5.800153,7.288488,-4.146368,2.999133,8.143914,-9.880032,8.050853,2.498988,-0.352527,-8.331005,-4.231376,-5.119573,8.522666,9.528478,7.627743,-9.676586,-3.987280,-5.241571,-8.332437,3.073706,-5.375107,9.996262,1.246876,6.570976,4.669137,5.911606,-3.988017,7.973239,-3.551830,0.160202,-1.155480,-1.789300,1.629725,3.847694,0.167143,1.413022,-7.824589,1.934965,0.666152,-3.894804,9.255059,0.324650,6.634850,9.467699,9.355042,2.637897,-5.511128,-3.039628,0.817750,7.795729,8.909481,-0.876277,3.824756,7.154671,-4.294209,5.208717,9.642550,6.349152,6.168667,-9.958122,8.115021,-1.273900,-1.933614,-0.742704,-5.267425,-5.574102,-1.570285,-3.151428,-4.039878,3.731979,1.401850,-8.363525,1.392181,6.439708,6.240609,7.785513,-5.496946,-3.234580,-1.942361,-1.242501,5.255211,-0.800885,9.779423,0.935485,0.337648,-8.701165,-2.378501,3.427600,-8.591844,-8.542942,5.022008,-7.138816,-8.734240,-0.048821,6.391346,3.810291,0.388628,1.772472,-8.316511,-4.990113,6.883749,-2.483909,-0.106986,2.051877,0.205717,-8.925274,9.358832,-5.328359,8.824633,-2.942950,8.242511,8.903677,-0.498047,6.442806,-2.968619,-5.046310,-8.663274,2.310420,-2.238580,9.173443,-3.018733,-1.858870,-0.164846,5.664089,5.038473,0.867987,-4.665455,4.590495,5.292549,9.799487,0.627811,8.448415,7.113054,-6.481042,4.091729,4.460068,0.359655,2.132662,-5.560106,0.886357,-3.971206,-3.418867,-0.667542,9.279643,-7.155608,3.860535,-8.021420,1.543813,6.960821,-0.114351,7.841090,-1.275617,8.186912,-0.042899,3.591027,-6.812849,-2.647724,-1.958936,-9.647780,-8.617824,-8.215361,-6.418324,-7.950929,-9.680396,2.824021,-4.214837,-9.548020,7.549793,-4.948495,0.565201,-5.263877,-2.116698,-7.692059,5.515708,-4.773095,3.531159,8.831425,-2.678743,5.538544,7.846031,0.138970,5.869237,-4.882928,0.829037,0.877532,-0.798417,-0.186335,-7.149984,4.008166,-9.943196,-4.547815,4.088286,0.955807,8.245562,-6.854559,-7.453421,8.311646,-7.470279,-5.974822,-6.021347,-8.162414,9.530454,7.859093,-2.418822,8.247736,7.010451,-8.152943,5.121585,-2.628639,8.517089,0.631671,-7.970221,1.507569,3.615732,-3.411056,4.116909,-8.048473,-7.037067,4.284296,1.067413,8.892117,-5.641650,6.381249,8.219257,-6.880833,-2.771325,-4.560791,-1.154245,2.925377,-0.342654,-5.331957,2.624650,-5.806959,-6.187138,-8.282651,8.883609,-1.175027,2.330182,5.666183,8.684273,0.365611,-1.674555,-5.613472,-5.821167,-7.376768,-0.351796,-1.091963,4.654259,1.586790,-7.891261,8.743618,0.583079,2.175810,3.160540,4.862158,6.361325,5.711883,7.473348,-3.145875,4.552912,-5.989071,4.128180,5.550795,2.461878,2.904499,-5.066153,2.547882,-2.721821,3.735063,-9.883404,7.207882,3.912939,0.663488,-9.173884,-7.585690,-8.558329,0.421640,-2.643039,-3.755552,6.822616,7.461931,1.750024,0.858995,-7.299211,4.697369,-5.051587,-9.125971,2.558951,-9.051207,1.959834,-3.310198,5.880269,-0.303706,-6.755264,5.356252,-8.551840,-7.642220,-0.643889,4.022953,-9.014730,7.144509,4.842985,-6.486436,6.345739,8.454382,-2.982564,-1.386467,7.178962,9.426836,5.563563,-7.734921,1.789976,1.943760,-1.502072,-7.957269,-7.191223,1.800146,4.234528,-9.860024,-9.660468,-7.179103,2.342361,-9.496822,9.223276,1.977342,6.333122,-9.112798,-0.066519,-3.232858,-7.513645,3.302429,-3.011768,5.238298,-0.706845,-2.872296,9.746544,8.716563,7.016889,8.028463,4.089707,4.027501,-2.630262,-5.984270,-7.716660,-4.387099,5.031066,2.581407,-7.716480,-3.278389,-8.449008,-3.848562,6.132029,3.814175,5.577276,5.248011,8.079074,2.059628,-7.013512,-1.977724,-6.232283,9.044224,-9.940372,2.086957,4.352855,8.749096,-4.761666,2.347039,-4.080549,-6.901342,-6.804951,-4.953594,3.974343,0.309424,5.743733,-9.915362,-9.179014,-6.539348,-9.375954,-8.218992,7.127911,1.523646,1.015179,9.261451,8.533866,9.380807,9.581309,4.943108,-7.099447,-1.796282,-0.752183,7.891431,-1.103711,4.854045,-5.791433,6.191842,-0.490321,0.834600,4.852547,3.438706,7.858880,-1.231614,-3.436858,2.381861,3.922577,7.316136,-1.143601,-0.690108,-7.720601,7.429562,7.107545,-5.544272,6.613598,3.538043,-0.130157,-3.551853,-3.751103,-0.485282,-6.588891,6.605610,3.329746,-9.706132,3.431814,-7.857259,-3.224157,-9.098064,-2.337756,9.149310,8.394034,6.245524,3.173892,9.131146,-0.632011,3.195132,2.134924,-7.602337,7.825771,-2.897923,-6.882841,-2.827950,-8.265334,-5.056899,7.435852,-0.651244,4.702987,-5.044520,9.676097,-0.962280,1.018488,2.300321,-4.041269,9.718621,-9.500482,-9.752606,-8.191824,7.772082,-2.694493,-0.006885,-8.183234,-5.851206,-8.335665,-4.273402,-4.020214,9.324674,-1.257548,-6.688733,4.440741,-4.177819,4.490643,-6.324828,6.009674,-0.852341,9.147352,9.087612,4.476965,3.470474,-6.669148,-8.341014,-7.597599,-9.539174,-7.611550,2.206297,-1.395165,7.446141,4.768671,-1.412901,7.667704,-5.114400,6.061341,-4.810628,1.483142,-2.236183,-3.420266,-1.137358,-7.229615,8.168422,9.823501,-0.060873,4.847735,3.172634,5.181177,6.802567,-4.373408,-8.392997,-3.464769,-6.890468,-6.639383,8.729497,0.783786,-2.908844,8.853617,-6.403779,-9.944842,-2.601936,-0.297863,-3.184038,9.266591,8.626435,2.680425,6.558771,-6.088341,8.243139,-1.478709,3.680619,-9.145662,-5.980745,-9.777660,-5.099300,5.188496,-5.611395,-0.892453,-4.180930,-4.915317,9.141796,0.430570,0.570336,9.978635,-7.643407,-4.720998,9.833958,6.066667,-6.772787,3.407753,5.032275,9.245811,-3.884347,-2.142264,-1.604470,-8.884936,2.245198,-5.813433,-6.482349,6.555547,-0.086209,-4.519783,0.527512,3.411346,4.716347,-9.285584,0.850654,-4.653234,-2.585488,-8.617513,-6.293174,-4.898289,-2.338229,-0.947971,-2.287102,-0.241901,6.703403,4.509370,-7.760718,-0.391716,4.322704,-8.774981,5.435041,-4.061838,-9.940621,-9.697844], dtype = "float64")#candidate|6024|(780,)|const|float64
call_6023 = relay.TupleGetItem(func_1222_call(relay.reshape(const_6024.astype('float64'), [780,])), 2)
call_6025 = relay.TupleGetItem(func_1225_call(relay.reshape(const_6024.astype('float64'), [780,])), 2)
output = relay.Tuple([call_6018,call_6023,const_6024,])
output2 = relay.Tuple([call_6019,call_6025,const_6024,])
func_6030 = relay.Function([], output)
mod['func_6030'] = func_6030
mod = relay.transform.InferType()(mod)
mutated_mod['func_6030'] = func_6030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6030_call = mutated_mod.get_global_var('func_6030')
call_6031 = func_6030_call()
output = call_6031
func_6032 = relay.Function([], output)
mutated_mod['func_6032'] = func_6032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5085_call = mod.get_global_var('func_5085')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_6053 = relay.TupleGetItem(func_5085_call(), 0)
call_6054 = relay.TupleGetItem(func_5087_call(), 0)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
var_6056 = relay.var("var_6056", dtype = "float32", shape = (330,))#candidate|6056|(330,)|var|float32
call_6055 = relay.TupleGetItem(func_4522_call(relay.reshape(var_6056.astype('float32'), [330,])), 2)
call_6057 = relay.TupleGetItem(func_4524_call(relay.reshape(var_6056.astype('float32'), [330,])), 2)
output = relay.Tuple([call_6053,call_6055,var_6056,])
output2 = relay.Tuple([call_6054,call_6057,var_6056,])
func_6077 = relay.Function([var_6056,], output)
mod['func_6077'] = func_6077
mod = relay.transform.InferType()(mod)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6078 = relay.var("var_6078", dtype = "float32", shape = (330,))#candidate|6078|(330,)|var|float32
func_6077_call = mutated_mod.get_global_var('func_6077')
call_6079 = func_6077_call(var_6078)
output = call_6079
func_6080 = relay.Function([var_6078], output)
mutated_mod['func_6080'] = func_6080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4475_call = mod.get_global_var('func_4475')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_6082 = func_4475_call()
call_6083 = func_4475_call()
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_6087 = func_4080_call()
call_6088 = func_4080_call()
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_6090 = func_3933_call()
call_6091 = func_3933_call()
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_6098 = func_2168_call()
call_6099 = func_2168_call()
bop_6102 = relay.logical_or(call_6098.astype('bool'), relay.reshape(call_6082.astype('bool'), relay.shape_of(call_6098))) # shape=(1, 10, 11)
bop_6105 = relay.logical_or(call_6099.astype('bool'), relay.reshape(call_6083.astype('bool'), relay.shape_of(call_6099))) # shape=(1, 10, 11)
output = relay.Tuple([call_6087,call_6090,bop_6102,])
output2 = relay.Tuple([call_6088,call_6091,bop_6105,])
func_6115 = relay.Function([], output)
mod['func_6115'] = func_6115
mod = relay.transform.InferType()(mod)
output = func_6115()
func_6116 = relay.Function([], output)
mutated_mod['func_6116'] = func_6116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3711_call = mod.get_global_var('func_3711')
func_3712_call = mutated_mod.get_global_var('func_3712')
call_6218 = func_3711_call()
call_6219 = func_3711_call()
output = relay.Tuple([call_6218,])
output2 = relay.Tuple([call_6219,])
func_6224 = relay.Function([], output)
mod['func_6224'] = func_6224
mod = relay.transform.InferType()(mod)
mutated_mod['func_6224'] = func_6224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6224_call = mutated_mod.get_global_var('func_6224')
call_6225 = func_6224_call()
output = call_6225
func_6226 = relay.Function([], output)
mutated_mod['func_6226'] = func_6226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5887_call = mod.get_global_var('func_5887')
func_5889_call = mutated_mod.get_global_var('func_5889')
call_6227 = func_5887_call()
call_6228 = func_5887_call()
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_6241 = func_2758_call()
call_6242 = func_2758_call()
output = relay.Tuple([call_6227,call_6241,])
output2 = relay.Tuple([call_6228,call_6242,])
func_6245 = relay.Function([], output)
mod['func_6245'] = func_6245
mod = relay.transform.InferType()(mod)
output = func_6245()
func_6246 = relay.Function([], output)
mutated_mod['func_6246'] = func_6246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_6335 = relay.TupleGetItem(func_3268_call(), 0)
call_6336 = relay.TupleGetItem(func_3269_call(), 0)
const_6338 = relay.const([[[9.482862,-9.021846,0.370596,-5.763236,-3.209846,4.924964,6.490679,7.015014,-1.763587,7.046030,4.147970],[6.352892,2.125379,-5.584811,-2.213825,-6.676647,-7.200856,1.055242,-4.796947,3.590315,-2.665055,-6.475142],[3.635475,-1.426414,-6.068871,-3.805491,9.789299,3.924463,-4.504603,-3.685135,-1.508931,3.787868,5.511553],[-2.040289,-0.823987,-8.653116,-3.917111,4.834347,-1.386616,1.615008,6.611642,-1.406277,-1.454109,-0.422276],[0.494752,2.914696,0.651460,-9.970652,2.360844,-8.185338,9.135558,4.474249,4.164891,6.914886,-4.577194],[8.663238,-7.148717,-0.054649,3.930585,-8.606398,8.031595,-0.087888,-0.632259,4.701820,5.712325,6.759294],[-0.341237,-6.977531,4.908812,1.111711,0.528663,-3.860742,6.292613,-8.295755,5.057899,9.364690,-7.061432],[4.669929,6.085687,1.474174,-2.367802,6.799791,1.444350,-1.834484,0.637986,-5.302901,-7.454893,-8.330547],[-1.497356,5.292859,5.952794,-5.802157,-3.644735,-6.497531,9.639851,0.281745,2.042646,-9.215734,-1.565253],[0.101124,7.275657,-0.539495,-5.231614,6.541306,7.304117,-5.038929,1.907105,7.851847,-9.394916,2.272909]],[[4.260811,5.344153,8.304009,5.109252,9.877590,9.255319,-6.374764,-6.358089,4.501887,0.593424,-1.147946],[4.104402,8.306319,-4.948067,6.336234,2.058925,-8.201571,4.342061,-7.544633,1.969163,3.746073,-6.995094],[8.292851,1.458777,-6.179065,8.015195,-2.461848,4.249763,2.842270,-8.244349,5.650273,2.875052,-0.317423],[-0.310654,3.860930,-8.596260,-6.374163,4.557720,-0.542007,-4.154649,3.698010,7.122098,3.624659,8.554662],[-6.655765,2.384385,8.504428,9.608796,2.702625,2.108754,-0.099813,3.064881,-5.741705,-4.402585,3.021243],[-7.397507,-5.758475,9.789223,-6.207895,6.732219,-5.976960,-3.940902,2.252606,8.573988,2.834131,-0.006079],[1.796065,0.551353,-9.626711,-9.221052,-3.029721,-4.182220,-9.460585,-1.763243,2.406927,-1.411611,-4.166815],[1.509713,-5.912281,-4.815733,8.514071,9.720825,9.876686,3.328166,-4.676598,5.901194,-9.291558,-9.563390],[6.522537,4.235197,-2.164843,-7.369757,-9.392711,-1.392789,2.982655,5.526346,0.677568,6.943090,8.694843],[-2.177835,-8.904905,-0.173537,-2.295586,4.748011,-1.060224,-7.771646,-4.627552,0.842679,-0.447671,-8.128714]],[[1.286540,7.049847,-5.676904,8.314918,1.030138,-3.273060,0.944985,-9.990414,0.174182,-1.222183,-8.021715],[-7.929696,6.926245,5.095191,8.640025,7.787016,3.387733,-2.123458,7.219050,2.641917,2.565750,-9.304596],[9.850877,-4.276503,3.231014,-2.978971,8.870083,-1.805770,-8.481253,4.371314,7.284036,-5.777908,8.290150],[5.533283,-3.551472,3.044034,-6.640240,0.547581,-6.246779,-1.433711,-7.475825,0.120948,6.561735,-0.830528],[4.473406,4.349201,7.955016,-3.208430,-3.630794,5.917041,-2.639240,9.481589,8.635436,-3.546812,-9.395858],[0.322276,4.345529,3.689407,-2.230694,5.238226,2.362108,5.743072,-6.997683,4.923830,9.266775,-5.961890],[7.702922,-8.640869,-9.984680,-8.133242,2.058480,1.007625,-2.475431,2.877679,-0.103808,-9.080209,4.329225],[-9.019893,4.493436,1.665567,7.379714,2.290777,2.679679,5.294102,-6.134215,-3.563910,9.372930,4.470617],[-6.483839,-3.479547,0.296126,-5.238922,-9.205425,-6.359716,-9.702667,-2.517864,4.307596,-2.431399,3.844787],[-2.012794,8.730088,0.954512,-3.225867,-1.324062,2.883288,-3.607943,-3.368304,-7.450776,8.100417,-8.108083]],[[-4.198469,7.277049,-1.114408,-7.575251,3.279036,-1.496150,9.905437,8.241246,-0.963687,8.943038,7.371248],[-5.169938,-9.365840,-5.308066,1.162541,-8.335189,-1.069064,-2.518769,6.200261,-7.331666,9.653236,-3.954385],[1.290233,2.075672,9.685672,4.618729,-5.427403,-6.807908,-1.660120,-2.217588,-3.978930,5.644109,6.321685],[2.051083,-5.579797,8.271853,-5.952028,5.833471,-4.652046,0.066176,0.733338,-2.103859,-9.392046,-4.089699],[6.584645,1.609538,2.551794,-3.773924,-4.660275,-9.975442,-2.822649,-7.883015,0.041419,-4.494738,-5.949345],[4.530982,-1.571903,4.353373,1.749325,-7.871970,5.297083,-6.157423,-7.423881,4.168183,-5.309029,-7.523268],[7.681315,-9.374510,-4.550606,-4.227958,-7.299028,-9.135660,3.428907,-6.023316,7.121714,-0.698175,-1.434661],[-5.570722,1.863447,9.467162,7.848065,-8.106798,-1.574381,0.690865,8.254872,-7.023305,0.672101,0.441419],[-5.996323,4.184506,-1.475099,-4.924331,-7.480840,0.140754,-2.055040,-1.286293,-4.877236,2.378016,3.137498],[0.012265,-9.183343,-9.129544,-1.331194,0.025408,6.143417,2.898856,-3.202688,-8.383282,-9.200943,-6.043678]],[[-9.496566,-1.765566,-6.889215,-0.738540,-5.108770,-3.859784,2.894986,-3.085888,-4.760300,-1.014858,2.319371],[2.232530,-3.842831,-6.325170,-4.973751,4.018365,8.245326,4.746902,2.115985,2.090101,-8.362560,1.312872],[7.185070,0.043661,1.519082,7.687764,4.164338,-2.246552,0.554366,-4.953906,5.092404,-2.556576,2.887222],[-9.628346,2.684094,-3.997792,-6.894762,6.950360,-4.237152,2.398769,9.185639,-2.450141,-1.092912,-8.148767],[1.862313,1.727901,-5.560373,-5.565337,8.887816,3.444819,-9.611682,-3.257197,8.505636,-3.892539,2.709338],[6.597317,9.663860,6.723834,-5.033404,1.458026,9.009169,-6.295236,-0.609298,6.936725,-7.699270,4.893427],[0.585473,1.802069,6.994412,-7.212463,0.733841,4.526701,8.840824,-5.608795,-8.442765,6.772346,-3.917477],[-7.000086,-5.500122,1.201225,-6.663363,-3.941371,-4.534310,-8.681158,9.647347,-6.767792,-8.855694,5.414299],[6.496075,1.255571,1.732268,1.387130,-7.057868,8.723969,8.146934,8.361088,4.673769,0.364734,7.637034],[1.725210,-8.850993,-1.077553,-0.035990,-5.006341,6.446650,4.544944,9.647728,9.443566,-4.198377,-2.281027]],[[9.007710,5.797617,2.650005,-8.152337,-0.551097,-6.289777,-8.675565,1.427001,-3.349028,-1.472140,2.977226],[5.759538,-4.117091,3.361874,6.166020,-4.722862,2.759049,4.931780,2.386476,-4.009269,4.229416,-5.565238],[1.740103,-6.415859,-3.658749,0.400333,7.402717,-6.424803,9.428936,-9.084704,6.542565,5.659413,2.528769],[-1.552365,3.389747,-7.746678,5.518826,-5.044191,5.835656,-7.666357,7.722964,0.267446,-6.889765,-1.876792],[1.264806,-2.380059,1.552906,-8.389971,-9.990239,5.698373,7.913255,9.654804,1.254305,3.819643,-3.709419],[-7.770790,2.491306,-0.426281,5.493460,-6.032259,-9.790831,8.170495,-4.556322,-3.723683,-0.836541,-7.161115],[7.425092,-9.689281,0.554950,9.211739,-9.050452,7.803040,-0.050885,0.348563,-8.937025,-3.808300,4.587773],[4.820840,6.159328,-0.630520,1.869442,8.976110,-1.812552,7.463976,0.781690,-8.704744,-8.555779,-8.530126],[7.185176,-5.872194,6.214737,-3.322570,0.233314,-9.028654,1.045767,-8.196875,-9.647452,-4.898395,-7.919110],[-5.745741,-9.237694,4.725697,1.819761,1.382607,9.491365,-8.819196,2.681980,4.559728,-5.694166,5.067584]]], dtype = "float32")#candidate|6338|(6, 10, 11)|const|float32
bop_6339 = relay.right_shift(call_6335.astype('uint16'), const_6338.astype('uint16')) # shape=(6, 10, 11)
bop_6342 = relay.right_shift(call_6336.astype('uint16'), const_6338.astype('uint16')) # shape=(6, 10, 11)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_6343 = func_4614_call()
call_6344 = func_4614_call()
uop_6362 = relay.atan(call_6343.astype('float32')) # shape=(10, 78)
uop_6364 = relay.atan(call_6344.astype('float32')) # shape=(10, 78)
func_4242_call = mod.get_global_var('func_4242')
func_4246_call = mutated_mod.get_global_var('func_4246')
call_6365 = relay.TupleGetItem(func_4242_call(relay.reshape(uop_6362.astype('float64'), [780,]), relay.reshape(bop_6339.astype('float32'), [660,]), ), 2)
call_6366 = relay.TupleGetItem(func_4246_call(relay.reshape(uop_6362.astype('float64'), [780,]), relay.reshape(bop_6339.astype('float32'), [660,]), ), 2)
uop_6371 = relay.asin(uop_6362.astype('float64')) # shape=(10, 78)
uop_6373 = relay.asin(uop_6364.astype('float64')) # shape=(10, 78)
output = relay.Tuple([bop_6339,call_6365,uop_6371,])
output2 = relay.Tuple([bop_6342,call_6366,uop_6373,])
func_6390 = relay.Function([], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
mutated_mod['func_6390'] = func_6390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6390_call = mutated_mod.get_global_var('func_6390')
call_6391 = func_6390_call()
output = call_6391
func_6392 = relay.Function([], output)
mutated_mod['func_6392'] = func_6392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6115_call = mod.get_global_var('func_6115')
func_6116_call = mutated_mod.get_global_var('func_6116')
call_6417 = relay.TupleGetItem(func_6115_call(), 1)
call_6418 = relay.TupleGetItem(func_6116_call(), 1)
func_1285_call = mod.get_global_var('func_1285')
func_1290_call = mutated_mod.get_global_var('func_1290')
var_6421 = relay.var("var_6421", dtype = "bool", shape = (80,))#candidate|6421|(80,)|var|bool
const_6422 = relay.const([False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False], dtype = "bool")#candidate|6422|(1200,)|const|bool
call_6420 = relay.TupleGetItem(func_1285_call(relay.reshape(var_6421.astype('bool'), [8, 10, 1]), relay.reshape(const_6422.astype('bool'), [8, 10, 15]), relay.reshape(const_6422.astype('bool'), [8, 10, 15]), ), 0)
call_6423 = relay.TupleGetItem(func_1290_call(relay.reshape(var_6421.astype('bool'), [8, 10, 1]), relay.reshape(const_6422.astype('bool'), [8, 10, 15]), relay.reshape(const_6422.astype('bool'), [8, 10, 15]), ), 0)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_6427 = func_3152_call()
call_6428 = func_3152_call()
output = relay.Tuple([call_6417,call_6420,var_6421,const_6422,call_6427,])
output2 = relay.Tuple([call_6418,call_6423,var_6421,const_6422,call_6428,])
func_6431 = relay.Function([var_6421,], output)
mod['func_6431'] = func_6431
mod = relay.transform.InferType()(mod)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6432 = relay.var("var_6432", dtype = "bool", shape = (80,))#candidate|6432|(80,)|var|bool
func_6431_call = mutated_mod.get_global_var('func_6431')
call_6433 = func_6431_call(var_6432)
output = call_6433
func_6434 = relay.Function([var_6432], output)
mutated_mod['func_6434'] = func_6434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3860_call = mod.get_global_var('func_3860')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_6442 = relay.TupleGetItem(func_3860_call(), 0)
call_6443 = relay.TupleGetItem(func_3861_call(), 0)
func_6077_call = mod.get_global_var('func_6077')
func_6080_call = mutated_mod.get_global_var('func_6080')
var_6474 = relay.var("var_6474", dtype = "float32", shape = (330,))#candidate|6474|(330,)|var|float32
call_6473 = relay.TupleGetItem(func_6077_call(relay.reshape(var_6474.astype('float32'), [330,])), 0)
call_6475 = relay.TupleGetItem(func_6080_call(relay.reshape(var_6474.astype('float32'), [330,])), 0)
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_6495 = relay.TupleGetItem(func_4982_call(), 3)
call_6496 = relay.TupleGetItem(func_4983_call(), 3)
output = relay.Tuple([call_6442,call_6473,var_6474,call_6495,])
output2 = relay.Tuple([call_6443,call_6475,var_6474,call_6496,])
func_6501 = relay.Function([var_6474,], output)
mod['func_6501'] = func_6501
mod = relay.transform.InferType()(mod)
var_6502 = relay.var("var_6502", dtype = "float32", shape = (330,))#candidate|6502|(330,)|var|float32
output = func_6501(var_6502)
func_6503 = relay.Function([var_6502], output)
mutated_mod['func_6503'] = func_6503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_6508 = func_4536_call()
call_6509 = func_4536_call()
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_6515 = func_2758_call()
call_6516 = func_2758_call()
func_2368_call = mod.get_global_var('func_2368')
func_2371_call = mutated_mod.get_global_var('func_2371')
const_6522 = relay.const([-5.783838,-1.133296,8.189313,0.358419,-2.751396,-9.670238,0.301413,7.404456,8.568777,-4.924129,1.258377,4.350547,-6.315984,-3.585696,7.041613,-4.385796,-6.440704,-7.934866,1.793719,8.636549,-9.097881,-7.001178,-9.451879,5.264148,-9.841545,1.409145,-5.308424,-7.123587,2.230386,5.142862,-6.973887,-9.519718,-2.599426,0.428981,5.115349,7.323687,-4.191381,8.993710,0.141008,-3.844240,-4.477576,-3.200698,-4.583978,6.099237,0.264352,-3.264430,-8.853010,-0.220794,-8.167060,9.035705,-3.373783,7.510970,-1.591453,1.988915,1.579510,4.774426,-6.960021,4.610154,-1.408434,-5.690564,1.085457,-6.736426,4.613752,-3.545200,-3.623968,8.285052,-6.023043,1.425327,3.083309,4.510851,-7.165094,-6.326815,-1.753534,8.516971,-5.770790,-8.616535,1.121817,-9.594109,7.909118,-3.290032,-3.373194,-0.455806,-9.927550,3.455437,8.949751,2.109952,2.558400,-1.787048,9.952907,-9.190232,8.635467,7.505305,7.247828,2.782593,-8.504486,-3.164639,-8.765588,7.589787,-9.486472,-1.478937,0.211982,3.547673,-0.425794,-6.491492,-9.449954,1.120794,6.869714,-3.816621,-7.744637,0.327889,9.749602,7.417397,6.773653,-5.392750,6.896067,3.716623,-7.555961,3.778512,-2.476003,-2.613892,6.435237,-0.876669,-7.923426,9.145054,-0.173353,6.335296,2.494098,9.933914,-2.664853,-1.912838,6.548706,-0.066082,7.675370,-7.291349,-2.657497,-4.950378,-8.909128,-3.628867,7.923067,-9.931703], dtype = "float64")#candidate|6522|(140,)|const|float64
call_6521 = relay.TupleGetItem(func_2368_call(relay.reshape(const_6522.astype('float64'), [140,])), 0)
call_6523 = relay.TupleGetItem(func_2371_call(relay.reshape(const_6522.astype('float64'), [140,])), 0)
output = relay.Tuple([call_6508,call_6515,call_6521,const_6522,])
output2 = relay.Tuple([call_6509,call_6516,call_6523,const_6522,])
func_6528 = relay.Function([], output)
mod['func_6528'] = func_6528
mod = relay.transform.InferType()(mod)
output = func_6528()
func_6529 = relay.Function([], output)
mutated_mod['func_6529'] = func_6529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_6547 = func_2835_call()
call_6548 = func_2835_call()
func_4536_call = mod.get_global_var('func_4536')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_6549 = func_4536_call()
call_6550 = func_4536_call()
func_1285_call = mod.get_global_var('func_1285')
func_1290_call = mutated_mod.get_global_var('func_1290')
var_6558 = relay.var("var_6558", dtype = "bool", shape = (80,))#candidate|6558|(80,)|var|bool
var_6559 = relay.var("var_6559", dtype = "bool", shape = (1200,))#candidate|6559|(1200,)|var|bool
call_6557 = relay.TupleGetItem(func_1285_call(relay.reshape(var_6558.astype('bool'), [8, 10, 1]), relay.reshape(var_6559.astype('bool'), [8, 10, 15]), relay.reshape(var_6559.astype('bool'), [8, 10, 15]), ), 1)
call_6560 = relay.TupleGetItem(func_1290_call(relay.reshape(var_6558.astype('bool'), [8, 10, 1]), relay.reshape(var_6559.astype('bool'), [8, 10, 15]), relay.reshape(var_6559.astype('bool'), [8, 10, 15]), ), 1)
output = relay.Tuple([call_6547,call_6549,call_6557,var_6558,var_6559,])
output2 = relay.Tuple([call_6548,call_6550,call_6560,var_6558,var_6559,])
func_6570 = relay.Function([var_6558,var_6559,], output)
mod['func_6570'] = func_6570
mod = relay.transform.InferType()(mod)
var_6571 = relay.var("var_6571", dtype = "bool", shape = (80,))#candidate|6571|(80,)|var|bool
var_6572 = relay.var("var_6572", dtype = "bool", shape = (1200,))#candidate|6572|(1200,)|var|bool
output = func_6570(var_6571,var_6572,)
func_6573 = relay.Function([var_6571,var_6572,], output)
mutated_mod['func_6573'] = func_6573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_6606 = func_3933_call()
call_6607 = func_3933_call()
output = relay.Tuple([call_6606,])
output2 = relay.Tuple([call_6607,])
func_6611 = relay.Function([], output)
mod['func_6611'] = func_6611
mod = relay.transform.InferType()(mod)
output = func_6611()
func_6612 = relay.Function([], output)
mutated_mod['func_6612'] = func_6612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_6615 = func_2758_call()
call_6616 = func_2758_call()
func_2368_call = mod.get_global_var('func_2368')
func_2371_call = mutated_mod.get_global_var('func_2371')
const_6626 = relay.const([1.213936,6.643786,3.481346,0.391264,-7.446022,0.908137,4.808213,-1.927958,-3.156735,7.151788,6.612834,-6.195253,6.465096,-4.724789,-5.534532,-6.041303,-1.933200,-2.226545,9.398440,-7.312848,-6.407340,1.404421,9.901440,-5.746491,-5.918187,0.035615,8.789454,9.894497,-8.832378,1.802547,-0.521057,-3.194718,4.888460,-6.702512,-6.092554,-9.478002,-1.114148,6.470224,1.081608,-2.218728,1.825362,-9.220138,0.577059,3.783645,2.174107,-7.517340,-9.954657,-6.762038,4.077287,-7.096980,3.940672,8.563442,-5.924536,6.925184,-7.895113,-4.068020,8.003221,-1.340469,-7.338626,-0.031560,-7.937306,-9.399997,9.238857,-7.494857,2.605091,8.467448,3.808232,2.523879,6.741537,-7.313458,-6.597449,8.342533,9.981952,-0.235182,4.955586,6.095719,9.916951,-0.975354,-6.489267,-3.755766,-0.103558,-1.162287,-5.354325,1.601830,4.571931,7.046257,-1.022454,7.854802,9.329066,-1.768215,9.225750,-7.837466,1.424258,2.746713,-4.747290,6.349183,4.054818,-9.225226,1.733617,5.711923,8.204275,-0.569317,8.875037,0.150303,1.939065,2.159983,5.762016,-9.383986,8.634409,-9.706719,4.926434,-9.576329,-0.552143,-4.130233,-7.197272,-0.174816,-0.448324,-7.874821,-5.337085,-3.448368,1.257259,-8.718208,-5.116941,0.901534,6.359042,1.352829,5.821707,8.183008,-4.300027,-4.394758,-6.756612,9.787487,0.532648,-5.060898,9.723009,-2.675675,1.853205,-2.400450,1.981476,9.214226], dtype = "float64")#candidate|6626|(140,)|const|float64
call_6625 = relay.TupleGetItem(func_2368_call(relay.reshape(const_6626.astype('float64'), [140,])), 2)
call_6627 = relay.TupleGetItem(func_2371_call(relay.reshape(const_6626.astype('float64'), [140,])), 2)
func_3086_call = mod.get_global_var('func_3086')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_6635 = relay.TupleGetItem(func_3086_call(), 1)
call_6636 = relay.TupleGetItem(func_3087_call(), 1)
func_613_call = mod.get_global_var('func_613')
func_616_call = mutated_mod.get_global_var('func_616')
const_6644 = relay.const([[-4.587786,0.860642,8.094764,1.110601,-9.135995,7.819013],[3.146908,-5.254585,-6.725557,3.672940,-1.001929,2.091925],[-1.561892,-0.910944,-5.031856,-8.126360,-6.281654,-3.986807],[-4.298429,6.784084,-6.112309,-8.143618,-1.513822,9.803593],[-9.621912,-7.848425,-3.226708,-6.251384,-7.324108,-8.600498],[-8.029133,-7.790511,-8.821065,-8.628738,-3.805707,-4.257684],[5.524205,3.146845,6.432004,-7.618248,8.924438,0.185317],[-7.415666,-8.697936,-0.196229,-4.322269,2.722515,-4.770919],[9.219412,4.845276,-6.443264,-1.519750,-2.603853,0.930196],[-1.180557,2.893777,-0.630507,-8.033190,1.195579,4.698966],[7.937904,-1.601168,-3.116228,-9.445788,3.701966,-5.263308],[6.330402,9.099197,-0.364071,-4.442627,4.854751,-2.794853],[-0.749398,-5.262588,5.047205,8.167693,8.338029,-9.399138],[-5.743989,3.743925,-9.925263,3.400529,5.624858,3.803657],[2.321226,-0.661117,4.600052,-2.694647,1.244011,2.612828],[9.650048,7.287670,-6.598961,-2.863381,7.739574,0.031036],[1.735623,5.977322,9.236180,-0.012786,-4.049840,3.761904],[1.701066,8.824821,1.191951,-9.463369,-4.062513,4.990546],[7.544300,0.838507,-2.598422,-5.115569,-5.285165,-5.184860],[-0.765157,-9.231992,7.093046,-3.556537,-2.411710,-9.793531],[0.562218,-7.231550,-1.113723,-1.148665,2.613230,-8.694631],[-9.043396,-7.539267,2.454074,8.946545,4.908799,-5.416825],[7.030763,-4.733856,1.539520,1.978105,2.052609,-7.463509],[-0.083143,6.903673,-7.718204,6.764360,-1.284118,9.601282]], dtype = "float64")#candidate|6644|(24, 6)|const|float64
call_6643 = relay.TupleGetItem(func_613_call(relay.reshape(const_6644.astype('float64'), [16, 3, 3])), 0)
call_6645 = relay.TupleGetItem(func_616_call(relay.reshape(const_6644.astype('float64'), [16, 3, 3])), 0)
output = relay.Tuple([call_6615,call_6625,const_6626,call_6635,call_6643,const_6644,])
output2 = relay.Tuple([call_6616,call_6627,const_6626,call_6636,call_6645,const_6644,])
func_6646 = relay.Function([], output)
mod['func_6646'] = func_6646
mod = relay.transform.InferType()(mod)
mutated_mod['func_6646'] = func_6646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6646_call = mutated_mod.get_global_var('func_6646')
call_6647 = func_6646_call()
output = call_6647
func_6648 = relay.Function([], output)
mutated_mod['func_6648'] = func_6648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4824_call = mod.get_global_var('func_4824')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_6649 = relay.TupleGetItem(func_4824_call(), 0)
call_6650 = relay.TupleGetItem(func_4825_call(), 0)
func_4293_call = mod.get_global_var('func_4293')
func_4295_call = mutated_mod.get_global_var('func_4295')
call_6655 = relay.TupleGetItem(func_4293_call(), 0)
call_6656 = relay.TupleGetItem(func_4295_call(), 0)
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_6671 = relay.TupleGetItem(func_3218_call(), 0)
call_6672 = relay.TupleGetItem(func_3219_call(), 0)
func_4536_call = mod.get_global_var('func_4536')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_6687 = func_4536_call()
call_6688 = func_4536_call()
bop_6704 = relay.bitwise_or(call_6649.astype('uint64'), relay.reshape(call_6671.astype('uint64'), relay.shape_of(call_6649))) # shape=(1, 10, 11)
bop_6707 = relay.bitwise_or(call_6650.astype('uint64'), relay.reshape(call_6672.astype('uint64'), relay.shape_of(call_6650))) # shape=(1, 10, 11)
output = relay.Tuple([call_6655,call_6687,bop_6704,])
output2 = relay.Tuple([call_6656,call_6688,bop_6707,])
func_6715 = relay.Function([], output)
mod['func_6715'] = func_6715
mod = relay.transform.InferType()(mod)
output = func_6715()
func_6716 = relay.Function([], output)
mutated_mod['func_6716'] = func_6716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_6724 = relay.TupleGetItem(func_3218_call(), 0)
call_6725 = relay.TupleGetItem(func_3219_call(), 0)
output = relay.Tuple([call_6724,])
output2 = relay.Tuple([call_6725,])
func_6729 = relay.Function([], output)
mod['func_6729'] = func_6729
mod = relay.transform.InferType()(mod)
output = func_6729()
func_6730 = relay.Function([], output)
mutated_mod['func_6730'] = func_6730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_6738 = relay.TupleGetItem(func_3268_call(), 0)
call_6739 = relay.TupleGetItem(func_3269_call(), 0)
output = call_6738
output2 = call_6739
func_6817 = relay.Function([], output)
mod['func_6817'] = func_6817
mod = relay.transform.InferType()(mod)
output = func_6817()
func_6818 = relay.Function([], output)
mutated_mod['func_6818'] = func_6818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3730_call = mod.get_global_var('func_3730')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_6837 = relay.TupleGetItem(func_3730_call(), 0)
call_6838 = relay.TupleGetItem(func_3731_call(), 0)
output = relay.Tuple([call_6837,])
output2 = relay.Tuple([call_6838,])
func_6842 = relay.Function([], output)
mod['func_6842'] = func_6842
mod = relay.transform.InferType()(mod)
mutated_mod['func_6842'] = func_6842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6842_call = mutated_mod.get_global_var('func_6842')
call_6843 = func_6842_call()
output = call_6843
func_6844 = relay.Function([], output)
mutated_mod['func_6844'] = func_6844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_6845 = relay.TupleGetItem(func_3785_call(), 0)
call_6846 = relay.TupleGetItem(func_3787_call(), 0)
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_6882 = func_3933_call()
call_6883 = func_3933_call()
output = relay.Tuple([call_6845,call_6882,])
output2 = relay.Tuple([call_6846,call_6883,])
func_6906 = relay.Function([], output)
mod['func_6906'] = func_6906
mod = relay.transform.InferType()(mod)
output = func_6906()
func_6907 = relay.Function([], output)
mutated_mod['func_6907'] = func_6907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_6928 = func_2168_call()
call_6929 = func_2168_call()
output = call_6928
output2 = call_6929
func_6934 = relay.Function([], output)
mod['func_6934'] = func_6934
mod = relay.transform.InferType()(mod)
output = func_6934()
func_6935 = relay.Function([], output)
mutated_mod['func_6935'] = func_6935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5887_call = mod.get_global_var('func_5887')
func_5889_call = mutated_mod.get_global_var('func_5889')
call_7003 = func_5887_call()
call_7004 = func_5887_call()
func_3304_call = mod.get_global_var('func_3304')
func_3307_call = mutated_mod.get_global_var('func_3307')
var_7016 = relay.var("var_7016", dtype = "float32", shape = (1430,))#candidate|7016|(1430,)|var|float32
var_7017 = relay.var("var_7017", dtype = "bool", shape = (315,))#candidate|7017|(315,)|var|bool
call_7015 = relay.TupleGetItem(func_3304_call(relay.reshape(var_7016.astype('float32'), [1430, 1]), relay.reshape(var_7017.astype('bool'), [315,]), ), 2)
call_7018 = relay.TupleGetItem(func_3307_call(relay.reshape(var_7016.astype('float32'), [1430, 1]), relay.reshape(var_7017.astype('bool'), [315,]), ), 2)
func_613_call = mod.get_global_var('func_613')
func_616_call = mutated_mod.get_global_var('func_616')
call_7024 = relay.TupleGetItem(func_613_call(relay.reshape(call_7015.astype('float64'), [16, 3, 3])), 0)
call_7025 = relay.TupleGetItem(func_616_call(relay.reshape(call_7015.astype('float64'), [16, 3, 3])), 0)
output = relay.Tuple([call_7003,call_7015,var_7016,var_7017,call_7024,])
output2 = relay.Tuple([call_7004,call_7018,var_7016,var_7017,call_7025,])
func_7044 = relay.Function([var_7016,var_7017,], output)
mod['func_7044'] = func_7044
mod = relay.transform.InferType()(mod)
mutated_mod['func_7044'] = func_7044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7044_call = mutated_mod.get_global_var('func_7044')
var_7046 = relay.var("var_7046", dtype = "float32", shape = (1430,))#candidate|7046|(1430,)|var|float32
var_7047 = relay.var("var_7047", dtype = "bool", shape = (315,))#candidate|7047|(315,)|var|bool
call_7045 = func_7044_call(var_7046,var_7047,)
output = call_7045
func_7048 = relay.Function([var_7046,var_7047,], output)
mutated_mod['func_7048'] = func_7048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_7050 = relay.TupleGetItem(func_3268_call(), 0)
call_7051 = relay.TupleGetItem(func_3269_call(), 0)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_7097 = func_4080_call()
call_7098 = func_4080_call()
func_2479_call = mod.get_global_var('func_2479')
func_2484_call = mutated_mod.get_global_var('func_2484')
const_7114 = relay.const([3.279533,6.323722,-3.334827,-7.788635,4.061583,2.159842,-2.653627,7.432320,3.239984,9.031740,1.805801,-5.245124,-2.832084,-6.467873,-8.731229,7.804150,-0.708285,-7.481575,3.440439,6.211189,6.503609,-2.673778,5.006211,-8.777250,-5.611537,-7.525112,9.366005,-6.354394,-8.575442,4.823970,7.784590,-8.125293,9.834557,-2.129091,8.578019,-7.881310,-2.356424,-5.822529,-2.558778,7.344842,5.888573,-9.311855,-7.064057,-0.879349,9.109790,6.732013,0.118189,6.255713,-0.989000,7.353265,7.026565,-3.018637,-7.038326,-4.304322,-9.805225,5.351935,1.061240,-4.545612,-8.934684,-1.844443,2.370889,-2.117711,6.683000,9.977295,5.767018,-6.060076,-3.710368,8.919432,1.027054,-7.885289,6.231024,9.807715,6.718440,-6.373524,2.596469,-3.333467,7.786893,5.338697,-4.383295,-2.963795,1.486573,-0.829737,-0.467822,-6.265339,9.757435,4.057707,-8.131424,5.518862,-4.480477,-1.994470,-0.494707,-8.867126,5.778163,0.852283,2.591325,-7.923499,-5.207078,-6.565941,-0.695954,-2.542899,0.473914,-3.027115,1.286716,-2.900896,5.973052,4.660080,4.586201,9.916905,6.586080,-8.852592,1.584409,8.340012,7.625771,-8.576972,-3.368787,-2.430710,-3.772386,7.487478,-9.327889,5.811453,-8.115764,-5.385636,1.904188,8.505430,-0.653279,7.175308,-1.351910,7.218153,-2.793461,2.800205,-8.057269,1.483309,-5.107079,-4.351055,-1.645389,-4.199363,-6.020138,-0.967116,9.777484,-4.260115,4.777157,9.876937,-5.844901,9.495962], dtype = "float64")#candidate|7114|(144,)|const|float64
var_7115 = relay.var("var_7115", dtype = "float64", shape = (780,))#candidate|7115|(780,)|var|float64
var_7116 = relay.var("var_7116", dtype = "float64", shape = (140,))#candidate|7116|(140,)|var|float64
call_7113 = relay.TupleGetItem(func_2479_call(relay.reshape(const_7114.astype('float64'), [144,]), relay.reshape(var_7115.astype('float64'), [390, 2]), relay.reshape(var_7116.astype('float64'), [5, 28]), ), 4)
call_7117 = relay.TupleGetItem(func_2484_call(relay.reshape(const_7114.astype('float64'), [144,]), relay.reshape(var_7115.astype('float64'), [390, 2]), relay.reshape(var_7116.astype('float64'), [5, 28]), ), 4)
func_6431_call = mod.get_global_var('func_6431')
func_6434_call = mutated_mod.get_global_var('func_6434')
const_7130 = relay.const([[False,False,True,False],[False,False,True,True],[False,False,True,True],[False,False,False,False],[True,False,False,True],[True,True,True,False],[True,False,False,True],[False,True,False,True],[True,False,True,True],[False,True,True,False],[True,False,True,True],[False,True,True,True],[True,False,True,False],[True,False,False,False],[False,False,True,True],[True,False,False,False],[False,True,False,False],[False,True,False,False],[True,True,True,False],[False,True,True,True]], dtype = "bool")#candidate|7130|(20, 4)|const|bool
call_7129 = relay.TupleGetItem(func_6431_call(relay.reshape(const_7130.astype('bool'), [80,])), 0)
call_7131 = relay.TupleGetItem(func_6434_call(relay.reshape(const_7130.astype('bool'), [80,])), 0)
func_6611_call = mod.get_global_var('func_6611')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_7133 = relay.TupleGetItem(func_6611_call(), 0)
call_7134 = relay.TupleGetItem(func_6612_call(), 0)
output = relay.Tuple([call_7050,call_7097,call_7113,const_7114,var_7115,var_7116,call_7129,const_7130,call_7133,])
output2 = relay.Tuple([call_7051,call_7098,call_7117,const_7114,var_7115,var_7116,call_7131,const_7130,call_7134,])
func_7138 = relay.Function([var_7115,var_7116,], output)
mod['func_7138'] = func_7138
mod = relay.transform.InferType()(mod)
mutated_mod['func_7138'] = func_7138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7138_call = mutated_mod.get_global_var('func_7138')
var_7140 = relay.var("var_7140", dtype = "float64", shape = (780,))#candidate|7140|(780,)|var|float64
var_7141 = relay.var("var_7141", dtype = "float64", shape = (140,))#candidate|7141|(140,)|var|float64
call_7139 = func_7138_call(var_7140,var_7141,)
output = call_7139
func_7142 = relay.Function([var_7140,var_7141,], output)
mutated_mod['func_7142'] = func_7142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_7144 = func_2758_call()
call_7145 = func_2758_call()
var_7148 = relay.var("var_7148", dtype = "float32", shape = (7, 10, 11))#candidate|7148|(7, 10, 11)|var|float32
bop_7149 = relay.floor_mod(call_7144.astype('float64'), var_7148.astype('float64')) # shape=(7, 10, 11)
bop_7152 = relay.floor_mod(call_7145.astype('float64'), var_7148.astype('float64')) # shape=(7, 10, 11)
output = relay.Tuple([bop_7149,])
output2 = relay.Tuple([bop_7152,])
func_7156 = relay.Function([var_7148,], output)
mod['func_7156'] = func_7156
mod = relay.transform.InferType()(mod)
var_7157 = relay.var("var_7157", dtype = "float32", shape = (7, 10, 11))#candidate|7157|(7, 10, 11)|var|float32
output = func_7156(var_7157)
func_7158 = relay.Function([var_7157], output)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_7201 = relay.TupleGetItem(func_3161_call(), 0)
call_7202 = relay.TupleGetItem(func_3162_call(), 0)
func_2653_call = mod.get_global_var('func_2653')
func_2659_call = mutated_mod.get_global_var('func_2659')
var_7208 = relay.var("var_7208", dtype = "float64", shape = (140,))#candidate|7208|(140,)|var|float64
const_7209 = relay.const([[7.289320,-3.737804,-4.179959,8.228042,-0.552688,9.552275,-8.681387,-4.300735,5.879807,-9.276323],[-0.725301,8.997380,-4.345013,5.664899,-5.787854,-5.252402,-4.168491,-8.232594,2.940968,-3.505274],[-9.072258,5.628790,-5.145847,6.130335,0.701564,5.999971,-8.365968,-7.384158,9.388620,5.168136],[-5.350880,-1.020965,-0.026001,8.410508,-7.427480,1.728834,9.089223,-0.591465,-3.557615,3.707367],[0.295206,4.721358,2.268446,-0.664493,2.228999,-5.519043,6.656104,-1.073725,-5.150878,2.694034],[8.640115,8.184024,9.517074,-8.376566,-7.246026,-0.104431,5.025973,5.089028,1.254471,2.297711],[-1.552907,-4.677048,-2.603379,9.141995,3.815247,-7.783039,-0.686150,1.059008,1.302214,9.728937],[-1.098477,7.687569,-5.280625,-0.839401,5.826767,-5.574287,-1.976539,1.550583,-0.950657,0.388243],[-3.254012,-3.131902,8.141083,-7.341462,-5.559692,-6.505955,6.707707,-2.451353,7.816270,2.452827],[-0.837771,-7.983085,1.973142,-9.979107,-1.964901,3.349927,2.561876,1.805179,7.748996,0.725497],[-6.865857,-1.869620,9.445770,3.264117,-2.493274,3.160900,-2.157938,3.009429,-6.870270,9.271676],[3.769158,5.115163,8.633400,6.462937,-6.759856,-5.526856,5.541325,2.745235,5.522333,3.251527],[7.494720,-8.573663,-9.842847,3.410207,7.261523,4.126676,5.564282,5.146861,-8.182309,-6.886839],[8.836691,2.864443,3.179955,-3.585740,6.835222,-3.917938,-3.984580,-1.893790,-6.334016,2.290767],[6.114011,-2.031363,2.662862,8.440185,8.974056,0.339380,-8.126439,2.591420,6.535555,-7.116284],[1.063447,8.217736,2.259066,-7.451206,-5.510838,-0.697835,-0.904371,-8.006010,-5.257805,3.701946],[8.892429,1.687817,6.201890,-0.044844,-3.263239,9.684392,8.140434,2.177200,6.592396,8.520940],[-4.182931,5.094015,-2.355046,-0.080188,4.935627,-0.103185,-5.444812,-7.831569,-5.183791,-9.644938],[3.140485,-7.296851,6.600582,4.236065,8.664122,-3.830123,-8.428906,3.309356,2.352390,-7.244356],[5.605276,-6.574302,-6.883453,-6.902846,8.272816,3.087848,-0.848276,5.277909,2.922591,-9.574999],[2.740889,-7.879042,-8.728436,0.100589,-1.350461,-4.798617,-5.316934,3.896079,6.275547,-0.308790],[1.968403,2.242456,5.727242,6.835577,-2.577639,-3.516188,-5.980167,5.779232,-1.548066,-4.354336],[-5.986655,-1.722369,1.200939,6.988118,1.288500,1.204950,3.042176,1.677874,-3.300673,-2.966134],[-3.297614,-7.789803,4.568124,-7.545962,-8.980075,-9.199407,7.927298,-2.307297,4.760661,-7.272921],[5.428371,5.456176,-3.719988,6.607865,4.889432,9.969871,-8.171513,-8.995088,-1.976327,6.079838],[8.243435,1.098835,5.623534,-3.308406,-5.828278,4.044038,-3.044026,-9.626863,8.461492,5.077523],[8.339916,9.487587,1.495963,-1.312592,-8.233801,-4.507379,5.240151,-5.417773,9.335608,0.701101],[8.688877,6.546268,2.026285,4.469193,-3.931447,1.054479,0.533555,7.765034,-9.144130,-7.087855],[-4.372324,0.056142,8.517043,-1.508940,-6.830899,-7.687151,-8.059849,4.683625,6.988166,9.939497],[-9.336236,-9.772632,8.109879,-5.705806,7.644889,-9.327225,1.079936,6.542128,9.293478,-8.439847],[-9.198278,-4.894082,-9.443225,-5.724819,-9.243502,2.891187,3.159092,-4.686243,-9.309101,-7.163108],[-1.816106,4.204463,-6.768176,-0.342813,-8.411983,9.583930,0.777555,1.212170,-4.103524,2.449047],[8.412561,8.892842,-0.356411,0.261796,-8.442066,-7.541014,-5.220488,-8.614913,5.665414,1.140853],[0.128642,-2.350750,-9.515578,1.825018,3.890483,6.479460,1.057390,1.806394,-3.869831,-6.257942],[7.240930,4.957229,-2.561127,-6.160958,-2.338970,4.057744,1.732693,-1.631564,-4.778460,-3.955249],[3.275986,-5.389064,-0.058177,-5.029383,5.135091,6.261842,-3.413800,-7.668769,-2.784435,-7.720098],[-6.752658,1.412894,1.251111,2.534617,6.485795,4.528105,9.360893,1.780433,-2.571842,0.866778],[3.983530,-6.113350,8.964428,-4.384498,2.476553,3.514599,1.780741,8.062222,-5.904475,-8.546129],[-4.783211,-0.297487,4.929612,1.908208,-0.018627,3.396106,1.161045,4.217451,0.660541,0.391461],[-5.445976,-7.726519,9.913067,-6.923025,5.211055,5.865231,-6.704220,8.542353,4.966205,6.301468],[4.468493,4.697825,-4.834740,-5.180972,9.227067,2.102721,-9.299900,3.980512,9.371039,3.077937],[-2.787487,9.196452,3.033699,-8.376672,5.392800,-1.752114,3.611835,-7.193197,-1.048858,7.164203],[-3.085873,0.982802,-9.577056,-1.683867,-2.988560,-6.579727,-5.262644,4.413354,9.351989,-3.271671],[-4.891150,6.231196,8.436054,7.927828,-3.240439,0.377068,6.248511,7.199053,2.619481,-4.931641],[-8.706291,-1.751741,-0.836879,-3.107995,4.170326,-7.913735,2.061967,1.982976,4.979820,-6.699918],[8.159639,-2.922505,-3.032442,7.631013,3.108687,6.091724,-8.097011,-6.070699,4.812129,-9.401226],[-1.326756,-4.104447,5.095986,-1.848382,4.605933,-2.093113,-5.584522,9.361607,7.951785,-0.091717],[-7.059433,-1.984902,2.052884,3.770757,0.088955,3.255836,0.075478,9.294998,-4.939108,2.775751],[-2.126974,-1.485314,3.007767,6.805524,-4.632816,0.296159,9.495459,-6.127559,2.646038,1.466702],[5.390069,-0.995967,7.326341,9.045030,4.547018,9.264158,0.210333,-4.818226,3.519351,2.923141],[9.797274,4.472062,-1.555340,6.471480,5.621352,-4.817053,0.926200,5.043052,-5.808403,-9.508722],[-3.120280,7.576183,-1.651437,-8.971600,5.145725,4.121575,-2.143800,7.506105,-9.665806,-0.650317],[1.168476,2.109558,7.784316,8.213023,1.891952,8.839555,1.535038,5.098083,-8.328384,-9.098066],[7.932104,-7.937805,-7.749027,-5.077709,-3.539407,-6.550315,6.181453,1.126051,2.100955,-3.616784],[-9.061363,-1.836036,-6.665166,8.055875,6.795055,-1.034812,-6.225660,-9.997438,-6.499899,1.084529],[-5.352413,2.220738,4.302300,-6.928415,1.366526,-8.930768,2.857315,-8.395973,-0.473325,-4.418642],[3.784846,3.557240,-2.168465,-9.910209,-2.172172,1.936328,5.380779,2.967403,8.542722,8.724656],[-9.639554,0.939782,-2.266305,-5.328142,4.107996,-6.157065,8.082078,-5.643543,-0.139807,1.163653],[5.854434,8.188427,7.048128,3.847007,-5.937995,5.016614,-9.798236,-5.772058,-6.773880,-6.161566],[-4.613689,-1.225260,-5.909710,9.436097,1.070641,8.670972,9.161918,-1.131493,8.033747,-1.037932],[-7.146826,8.205571,-1.961601,-1.766070,-9.194603,-0.775263,9.934567,-2.827137,-8.958080,-6.721850],[-0.380747,-4.408548,-3.914405,-2.603319,-3.437814,-6.116410,1.613467,-3.993774,4.790963,-3.249220],[7.910712,-0.279707,-8.589279,-1.972671,-7.745871,-1.665335,-3.354470,7.631638,8.023449,5.933007],[-9.366955,4.003748,8.753448,3.055172,-3.897398,-4.282146,-2.475713,-3.827248,8.201029,4.500839],[-2.844913,2.074707,-6.495745,9.218956,-1.101246,-5.413576,-8.384225,-8.129448,2.942949,7.620244],[-3.637462,4.058735,-4.524436,6.949934,-5.462563,-5.349826,-3.618309,4.195251,-3.661911,7.922391],[9.311055,2.320318,4.915270,2.332016,5.442320,-5.322456,-4.453821,-6.123974,9.898448,9.166064],[2.230313,-8.330148,4.150898,-8.700880,5.613383,-2.283646,4.824797,-1.479576,-7.540401,5.355000],[-5.997437,4.437596,2.376465,-5.593056,7.851494,-0.963206,8.688397,-5.480009,7.349483,-5.753205],[-0.148415,8.441515,-1.685630,-3.767660,-7.885415,-4.323816,8.699172,5.324796,2.863735,-5.137088],[5.009972,0.959700,9.923164,3.593700,4.218770,1.819910,1.973082,1.927840,5.242263,-1.234285],[-3.335014,-4.311417,-0.572015,-2.354739,2.472765,-9.384858,-5.751173,0.853057,3.419117,-9.105324],[-9.942023,0.219694,-9.030737,7.495978,-2.472581,4.740680,-5.567376,2.464010,-2.171731,6.833382],[-7.783135,-8.316035,8.668857,-8.980286,6.649438,0.625677,1.753330,4.548184,-9.309143,0.108836],[-1.812489,5.452704,-2.251928,4.090172,-7.667890,3.215841,-5.231297,2.716164,9.513531,-0.760073],[-4.048664,7.827231,-8.397861,-6.058745,8.136675,-3.104157,-3.813077,9.728857,-5.180283,7.929423],[1.071231,5.423892,1.008970,3.183609,-5.419650,6.480039,-8.365081,-6.990407,7.308703,9.807334],[-9.124572,-0.104213,3.030805,-3.650125,-0.268802,-0.331190,-1.464503,3.877429,7.158601,-1.194336],[-5.995958,-7.235264,-2.797278,-1.203368,7.564390,6.722266,1.123539,9.118754,7.997032,-8.720942],[7.004136,5.295562,-1.000912,0.069342,9.737830,9.523863,8.063564,-3.004328,3.124732,8.679017],[-8.471915,-9.854754,-4.720586,-3.803024,2.908745,7.335089,-2.027625,-7.672488,0.913854,-6.908172],[-7.164647,7.263008,4.084612,1.323804,-5.082189,-0.602756,7.931629,-3.711596,-4.421263,1.041285],[6.422810,-9.833942,0.661305,-7.273741,3.475385,-4.161143,-7.400994,6.608069,4.258959,-1.173298],[-2.068486,5.510511,-3.236862,3.936847,-5.351046,-3.779706,-3.923422,2.553600,-1.095965,-0.181556],[-4.906492,1.249043,-5.473811,2.769255,4.790482,3.180876,-3.580552,-8.091327,-3.242929,3.474307],[-5.494526,-1.420542,-4.125252,7.889173,5.345717,-4.540798,-0.758844,4.869529,9.762532,-1.976016],[-4.238252,-3.185517,-5.053473,6.505916,-1.261919,-9.879904,9.879150,9.954699,-9.619033,-7.830486],[9.604983,-9.125592,-6.700760,-3.950404,-1.641430,-3.547119,5.855139,8.349643,7.347923,-2.251919],[0.075616,5.851775,-4.947759,-3.882278,6.826718,-9.718104,-7.753569,-2.290794,-0.068472,-3.948112],[0.392430,-4.747238,9.581093,5.780429,-9.959249,-1.617935,-6.865891,-5.331099,8.127390,5.122887],[2.542873,1.522122,-0.444623,-4.258482,-5.059731,7.257714,-8.716347,-3.063471,3.778207,-6.094932],[-4.002149,1.061764,-3.493175,4.741574,3.154912,-7.584177,-5.882493,-5.917242,8.197088,-0.932766],[5.529278,-7.320660,7.812607,6.711211,-5.319417,-4.790425,-2.948372,4.272735,-4.232467,-6.416107],[2.426225,-5.279684,-6.162848,8.532661,-4.243143,-1.480491,6.276501,0.803288,0.777354,-0.104226],[-9.573959,-2.860783,-2.223607,-0.086133,-9.468547,-1.482764,6.879149,-4.491545,3.303872,-3.512133],[4.875500,1.370684,6.152004,3.900919,2.327240,-7.348764,-9.530344,4.705470,-8.883465,1.194128],[-2.888874,-3.694969,4.445889,-6.532283,-8.163386,-1.824135,1.601356,9.855810,-6.847936,2.818522],[-1.450448,7.071540,9.234983,9.479084,-3.821766,-9.606092,3.446915,6.651689,6.023735,3.532212],[-4.812789,4.880601,-5.034494,-9.214554,9.302597,-1.447594,7.850063,0.047262,-3.038221,-7.923798],[3.065714,-3.386642,1.528452,0.385000,7.054073,3.037745,-1.467423,8.378271,4.378951,4.038342],[8.663234,-6.317435,-2.376888,6.194279,-2.466025,7.406202,0.053844,-0.395210,9.970144,4.947868],[7.693506,-0.171266,-9.779527,-7.767910,4.655301,-0.886218,0.182344,1.490315,-6.833437,4.883205],[-9.618586,5.668595,-4.082896,6.580761,2.598386,-5.459583,1.854608,4.897750,-1.282864,1.156304],[1.685657,-9.102033,-8.534895,-6.223250,6.414747,5.871873,2.146227,2.661740,6.724290,0.091814],[0.919588,1.087025,8.234458,-5.334686,-5.641054,5.528351,-5.669470,-3.952683,-3.830601,9.825443],[-3.392005,8.649338,5.471958,2.573848,8.859291,-4.704769,-9.471565,2.829515,-5.665637,0.787654],[9.527453,-8.918901,9.674272,-7.224360,-0.916386,7.471189,3.191110,-4.552637,2.888417,3.167497],[-9.106859,0.587430,3.444225,-7.890351,0.534823,-0.962747,3.091064,-8.276720,7.938958,-3.152295],[-0.092283,2.542207,-2.380329,0.648723,4.630746,6.501442,-3.974767,1.379721,9.741163,6.570477],[8.940102,-0.495053,-0.750147,0.521076,7.383085,5.075858,2.344973,2.809482,-2.380982,5.713404],[7.383376,-9.492638,-3.237388,3.988994,4.977961,-1.082691,-8.571032,4.370481,9.009194,7.035294],[-6.367177,-2.332791,9.273432,-6.196855,-0.791098,9.424114,-0.697764,1.645566,1.018309,-3.520909],[6.760845,-1.318018,5.797783,7.389603,-8.832030,-1.795039,4.953798,7.636212,-6.795622,2.468886],[7.595235,4.241141,-3.913474,-7.719252,7.630313,-0.089375,1.779792,7.760032,7.990256,8.427727],[2.597363,-2.713871,4.947588,8.616893,0.633894,-8.808377,2.474301,-8.176206,0.410059,-1.047147],[-2.008621,6.982724,7.114405,-1.520702,1.088223,-3.462970,8.950845,-4.354550,-5.898125,2.234744],[-8.634672,7.837634,4.412837,0.580176,-1.891443,7.682241,-7.757569,9.455982,7.598755,-0.658180],[7.140635,6.544132,-5.646106,8.261073,1.110657,-9.999231,8.812480,-2.429836,-2.879659,2.060007],[7.984675,9.740589,1.681068,4.180341,-8.508040,-1.440347,-9.205470,3.360998,9.479815,-7.114776],[5.359660,-4.593313,-8.223374,8.009223,-6.655816,8.316207,9.651618,9.458564,0.214557,-6.961850],[7.829856,-7.976793,-8.850040,-1.157693,-3.600032,7.061593,8.394406,-2.000706,-3.673400,-4.165091],[-8.446125,-1.167920,-4.058561,4.818553,-6.785043,-4.675903,-6.993825,3.908361,-8.457546,-5.216873],[-2.899662,-7.067732,0.019608,3.202216,-9.970644,-0.619530,-9.056555,-3.475608,-9.455067,-4.741891],[3.069174,-9.775885,9.331390,2.304543,6.362074,2.208101,3.547361,-7.492587,-3.930683,-2.775613],[4.172437,-4.671265,0.110177,2.455067,-5.493243,-3.271290,-4.668996,9.883256,-4.041073,0.757063],[-8.050136,-0.124896,-7.089709,-7.005498,-8.258609,1.306486,4.258100,9.298981,-2.936680,-6.217886],[2.114626,3.202948,-9.457112,2.410332,1.248781,-8.656137,3.556150,5.628037,3.901436,1.204261],[-1.629837,-2.522123,-1.777624,-3.642767,-1.690720,0.952140,8.447508,8.316006,7.931578,-8.475992],[0.016308,-1.651006,7.245113,-7.310894,5.255276,8.589273,-1.703715,3.936105,7.312925,3.196850],[-3.674620,9.807757,6.454378,2.408336,-0.110059,3.701232,1.340556,-1.876103,6.242283,2.084159],[-7.447690,-9.722758,-6.937185,1.638490,8.089625,7.048571,9.635493,6.755001,1.770110,0.969048],[2.469808,9.744929,-8.054516,7.557776,-1.072276,-7.061631,5.857235,3.604184,-4.319610,-1.993381],[-3.941755,-0.688275,-5.077206,-7.906898,-3.930398,9.861970,4.290599,-7.851821,8.536494,6.641869],[2.655521,-0.934132,5.431188,-7.442852,5.955549,7.060826,7.724243,9.063591,-7.266293,4.462068],[-3.537708,-7.871896,-3.894642,8.830039,-6.434186,2.557928,7.151843,0.170775,-8.993210,-4.967110],[-4.869099,8.033148,7.505334,0.826643,-4.736604,0.531277,-5.522415,-5.385643,-6.049530,-9.562798],[6.160315,-5.844286,4.170295,0.598267,-7.611916,0.698261,5.193930,-0.481134,-0.070103,-4.892685],[-0.962624,7.165920,5.759974,4.342526,4.477202,2.081704,-0.665516,9.061521,5.047085,8.601006],[7.063089,-9.006391,3.636634,7.967720,-0.512676,-3.772680,5.866384,4.996483,-0.148946,9.247259],[-2.019063,-1.463449,-7.609484,1.018430,-7.688208,9.516991,3.137660,-5.893435,-0.365887,-9.437345],[-7.667087,-4.717006,-6.222792,-0.196002,-5.890284,4.902433,-6.441688,6.149604,3.270754,-3.994139],[4.538701,0.550139,9.761310,0.861454,-8.941927,3.067669,4.080357,-7.148091,9.727073,-6.941476],[-4.678292,6.027150,2.820766,-9.807152,1.405262,-1.597662,-7.107141,4.828012,2.562873,-2.373538]], dtype = "float32")#candidate|7209|(143, 10)|const|float32
const_7210 = relay.const([False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False], dtype = "bool")#candidate|7210|(315,)|const|bool
call_7207 = relay.TupleGetItem(func_2653_call(relay.reshape(var_7208.astype('float64'), [140,]), relay.reshape(const_7209.astype('float32'), [13, 10, 11]), relay.reshape(const_7210.astype('bool'), [35, 9]), relay.reshape(const_7209.astype('float32'), [13, 10, 11]), ), 4)
call_7211 = relay.TupleGetItem(func_2659_call(relay.reshape(var_7208.astype('float64'), [140,]), relay.reshape(const_7209.astype('float32'), [13, 10, 11]), relay.reshape(const_7210.astype('bool'), [35, 9]), relay.reshape(const_7209.astype('float32'), [13, 10, 11]), ), 4)
func_6646_call = mod.get_global_var('func_6646')
func_6648_call = mutated_mod.get_global_var('func_6648')
call_7235 = relay.TupleGetItem(func_6646_call(), 3)
call_7236 = relay.TupleGetItem(func_6648_call(), 3)
uop_7241 = relay.atanh(call_7235.astype('float64')) # shape=(5, 10, 11)
uop_7243 = relay.atanh(call_7236.astype('float64')) # shape=(5, 10, 11)
func_3304_call = mod.get_global_var('func_3304')
func_3307_call = mutated_mod.get_global_var('func_3307')
call_7245 = relay.TupleGetItem(func_3304_call(relay.reshape(call_7207.astype('float32'), [1430, 1]), relay.reshape(const_7210.astype('bool'), [315,]), ), 3)
call_7246 = relay.TupleGetItem(func_3307_call(relay.reshape(call_7207.astype('float32'), [1430, 1]), relay.reshape(const_7210.astype('bool'), [315,]), ), 3)
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_7250 = func_2758_call()
call_7251 = func_2758_call()
func_1364_call = mod.get_global_var('func_1364')
func_1367_call = mutated_mod.get_global_var('func_1367')
var_7253 = relay.var("var_7253", dtype = "float32", shape = (432,))#candidate|7253|(432,)|var|float32
var_7254 = relay.var("var_7254", dtype = "float64", shape = (144,))#candidate|7254|(144,)|var|float64
call_7252 = relay.TupleGetItem(func_1364_call(relay.reshape(var_7253.astype('float32'), [3, 12, 12]), relay.reshape(var_7254.astype('float64'), [144,]), ), 2)
call_7255 = relay.TupleGetItem(func_1367_call(relay.reshape(var_7253.astype('float32'), [3, 12, 12]), relay.reshape(var_7254.astype('float64'), [144,]), ), 2)
output = relay.Tuple([call_7201,call_7207,var_7208,const_7209,const_7210,uop_7241,call_7245,call_7250,call_7252,var_7253,var_7254,])
output2 = relay.Tuple([call_7202,call_7211,var_7208,const_7209,const_7210,uop_7243,call_7246,call_7251,call_7255,var_7253,var_7254,])
func_7265 = relay.Function([var_7208,var_7253,var_7254,], output)
mod['func_7265'] = func_7265
mod = relay.transform.InferType()(mod)
var_7266 = relay.var("var_7266", dtype = "float64", shape = (140,))#candidate|7266|(140,)|var|float64
var_7267 = relay.var("var_7267", dtype = "float32", shape = (432,))#candidate|7267|(432,)|var|float32
var_7268 = relay.var("var_7268", dtype = "float64", shape = (144,))#candidate|7268|(144,)|var|float64
output = func_7265(var_7266,var_7267,var_7268,)
func_7269 = relay.Function([var_7266,var_7267,var_7268,], output)
mutated_mod['func_7269'] = func_7269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6611_call = mod.get_global_var('func_6611')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_7274 = relay.TupleGetItem(func_6611_call(), 0)
call_7275 = relay.TupleGetItem(func_6612_call(), 0)
output = relay.Tuple([call_7274,])
output2 = relay.Tuple([call_7275,])
func_7286 = relay.Function([], output)
mod['func_7286'] = func_7286
mod = relay.transform.InferType()(mod)
mutated_mod['func_7286'] = func_7286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7286_call = mutated_mod.get_global_var('func_7286')
call_7287 = func_7286_call()
output = call_7287
func_7288 = relay.Function([], output)
mutated_mod['func_7288'] = func_7288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7305 = relay.var("var_7305", dtype = "float64", shape = (8, 14, 16))#candidate|7305|(8, 14, 16)|var|float64
uop_7306 = relay.sin(var_7305.astype('float64')) # shape=(8, 14, 16)
func_2340_call = mod.get_global_var('func_2340')
func_2342_call = mutated_mod.get_global_var('func_2342')
const_7312 = relay.const([True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False], dtype = "bool")#candidate|7312|(80,)|const|bool
call_7311 = relay.TupleGetItem(func_2340_call(relay.reshape(const_7312.astype('bool'), [80,])), 2)
call_7313 = relay.TupleGetItem(func_2342_call(relay.reshape(const_7312.astype('bool'), [80,])), 2)
var_7314 = relay.var("var_7314", dtype = "float64", shape = (8, 14, 16))#candidate|7314|(8, 14, 16)|var|float64
bop_7315 = relay.equal(uop_7306.astype('bool'), relay.reshape(var_7314.astype('bool'), relay.shape_of(uop_7306))) # shape=(8, 14, 16)
bop_7320 = relay.multiply(var_7305.astype('uint16'), relay.reshape(uop_7306.astype('uint16'), relay.shape_of(var_7305))) # shape=(8, 14, 16)
output = relay.Tuple([call_7311,const_7312,bop_7315,bop_7320,])
output2 = relay.Tuple([call_7313,const_7312,bop_7315,bop_7320,])
func_7333 = relay.Function([var_7305,var_7314,], output)
mod['func_7333'] = func_7333
mod = relay.transform.InferType()(mod)
mutated_mod['func_7333'] = func_7333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7333_call = mutated_mod.get_global_var('func_7333')
var_7335 = relay.var("var_7335", dtype = "float64", shape = (8, 14, 16))#candidate|7335|(8, 14, 16)|var|float64
var_7336 = relay.var("var_7336", dtype = "float64", shape = (8, 14, 16))#candidate|7336|(8, 14, 16)|var|float64
call_7334 = func_7333_call(var_7335,var_7336,)
output = call_7334
func_7337 = relay.Function([var_7335,var_7336,], output)
mutated_mod['func_7337'] = func_7337
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7339 = relay.var("var_7339", dtype = "float32", shape = (12, 16, 16))#candidate|7339|(12, 16, 16)|var|float32
uop_7340 = relay.cosh(var_7339.astype('float32')) # shape=(12, 16, 16)
uop_7396 = relay.asinh(uop_7340.astype('float32')) # shape=(12, 16, 16)
output = uop_7396
output2 = uop_7396
func_7401 = relay.Function([var_7339,], output)
mod['func_7401'] = func_7401
mod = relay.transform.InferType()(mod)
var_7402 = relay.var("var_7402", dtype = "float32", shape = (12, 16, 16))#candidate|7402|(12, 16, 16)|var|float32
output = func_7401(var_7402)
func_7403 = relay.Function([var_7402], output)
mutated_mod['func_7403'] = func_7403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7286_call = mod.get_global_var('func_7286')
func_7288_call = mutated_mod.get_global_var('func_7288')
call_7425 = relay.TupleGetItem(func_7286_call(), 0)
call_7426 = relay.TupleGetItem(func_7288_call(), 0)
func_4333_call = mod.get_global_var('func_4333')
func_4336_call = mutated_mod.get_global_var('func_4336')
const_7455 = relay.const([-9,7,-7,-2,-9,9,3,-2,8,6,1,-6,8,9,-10,7,-1,3,3,5,6,-2,3,-3,1,-5,-9,9,2,-5,-4,6,-7,5,6,3,-3,-2,7,9,7,10,-4,-3,-5,-3,-1,4,7,9,9,-5,7,1,3,3,4,5,-2,-6,-9,10,7,-7,3,-10,-9,9,4,-3,-1,-8,2,5,-4,-5,-10,-10,-8,5,-6,-6,-2,3,4,-3,-2,2,-4,8,-9,-10,7,-8,-8,6,8,9,6,5,5,9,-1,-1,-9,5,-1,7,-5,-3,-9,-7,1,-8,7,1,3,9,-10,-9,9,-6,-8,-10,-9,-8,-2,-7,10,-3,9,8,3,-6,-8,-1,10,7,10,3,-10,10,-5,-8,2,-1,-7,-5,-6,3,-7,-1,2,8,-5,3,-3,1,10,4,-3,7,6,8,2,-6,-6,9,-4,9,-10,-5,5,-3,-7,1,4,8,7,-1,-7,-1,1,8,8,5,10,-5,7,-4,-6,2,10,-9,-6,-9,5,-6,9,-4,-3,-7,10,-10,9,-1,6,5,5,-6,-2,4,4,-6,3,-1], dtype = "uint8")#candidate|7455|(216,)|const|uint8
call_7454 = relay.TupleGetItem(func_4333_call(relay.reshape(const_7455.astype('uint8'), [3, 9, 8]), relay.reshape(const_7455.astype('uint8'), [3, 9, 8]), ), 1)
call_7456 = relay.TupleGetItem(func_4336_call(relay.reshape(const_7455.astype('uint8'), [3, 9, 8]), relay.reshape(const_7455.astype('uint8'), [3, 9, 8]), ), 1)
output = relay.Tuple([call_7425,call_7454,const_7455,])
output2 = relay.Tuple([call_7426,call_7456,const_7455,])
func_7457 = relay.Function([], output)
mod['func_7457'] = func_7457
mod = relay.transform.InferType()(mod)
mutated_mod['func_7457'] = func_7457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7457_call = mutated_mod.get_global_var('func_7457')
call_7458 = func_7457_call()
output = call_7458
func_7459 = relay.Function([], output)
mutated_mod['func_7459'] = func_7459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4475_call = mod.get_global_var('func_4475')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_7510 = func_4475_call()
call_7511 = func_4475_call()
func_6431_call = mod.get_global_var('func_6431')
func_6434_call = mutated_mod.get_global_var('func_6434')
var_7519 = relay.var("var_7519", dtype = "bool", shape = (80,))#candidate|7519|(80,)|var|bool
call_7518 = relay.TupleGetItem(func_6431_call(relay.reshape(var_7519.astype('bool'), [80,])), 0)
call_7520 = relay.TupleGetItem(func_6434_call(relay.reshape(var_7519.astype('bool'), [80,])), 0)
func_2340_call = mod.get_global_var('func_2340')
func_2342_call = mutated_mod.get_global_var('func_2342')
call_7524 = relay.TupleGetItem(func_2340_call(relay.reshape(var_7519.astype('bool'), [80,])), 3)
call_7525 = relay.TupleGetItem(func_2342_call(relay.reshape(var_7519.astype('bool'), [80,])), 3)
output = relay.Tuple([call_7510,call_7518,var_7519,call_7524,])
output2 = relay.Tuple([call_7511,call_7520,var_7519,call_7525,])
func_7539 = relay.Function([var_7519,], output)
mod['func_7539'] = func_7539
mod = relay.transform.InferType()(mod)
mutated_mod['func_7539'] = func_7539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7540 = relay.var("var_7540", dtype = "bool", shape = (80,))#candidate|7540|(80,)|var|bool
func_7539_call = mutated_mod.get_global_var('func_7539')
call_7541 = func_7539_call(var_7540)
output = call_7541
func_7542 = relay.Function([var_7540], output)
mutated_mod['func_7542'] = func_7542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5414_call = mod.get_global_var('func_5414')
func_5416_call = mutated_mod.get_global_var('func_5416')
call_7595 = func_5414_call()
call_7596 = func_5414_call()
var_7597 = relay.var("var_7597", dtype = "float64", shape = (10, 78))#candidate|7597|(10, 78)|var|float64
bop_7598 = relay.subtract(call_7595.astype('int64'), relay.reshape(var_7597.astype('int64'), relay.shape_of(call_7595))) # shape=(10, 78)
bop_7601 = relay.subtract(call_7596.astype('int64'), relay.reshape(var_7597.astype('int64'), relay.shape_of(call_7596))) # shape=(10, 78)
func_6817_call = mod.get_global_var('func_6817')
func_6818_call = mutated_mod.get_global_var('func_6818')
call_7604 = func_6817_call()
call_7605 = func_6817_call()
bop_7614 = relay.left_shift(bop_7598.astype('uint16'), relay.reshape(var_7597.astype('uint16'), relay.shape_of(bop_7598))) # shape=(10, 78)
bop_7617 = relay.left_shift(bop_7601.astype('uint16'), relay.reshape(var_7597.astype('uint16'), relay.shape_of(bop_7601))) # shape=(10, 78)
bop_7622 = relay.greater_equal(var_7597.astype('bool'), relay.reshape(bop_7598.astype('bool'), relay.shape_of(var_7597))) # shape=(10, 78)
bop_7625 = relay.greater_equal(var_7597.astype('bool'), relay.reshape(bop_7601.astype('bool'), relay.shape_of(var_7597))) # shape=(10, 78)
bop_7629 = relay.logical_or(var_7597.astype('bool'), relay.reshape(call_7595.astype('bool'), relay.shape_of(var_7597))) # shape=(10, 78)
bop_7632 = relay.logical_or(var_7597.astype('bool'), relay.reshape(call_7596.astype('bool'), relay.shape_of(var_7597))) # shape=(10, 78)
uop_7641 = relay.atanh(bop_7614.astype('float32')) # shape=(10, 78)
uop_7643 = relay.atanh(bop_7617.astype('float32')) # shape=(10, 78)
bop_7645 = relay.logical_and(uop_7641.astype('bool'), relay.reshape(var_7597.astype('bool'), relay.shape_of(uop_7641))) # shape=(10, 78)
bop_7648 = relay.logical_and(uop_7643.astype('bool'), relay.reshape(var_7597.astype('bool'), relay.shape_of(uop_7643))) # shape=(10, 78)
uop_7650 = relay.log(uop_7641.astype('float32')) # shape=(10, 78)
uop_7652 = relay.log(uop_7643.astype('float32')) # shape=(10, 78)
uop_7655 = relay.asinh(uop_7650.astype('float32')) # shape=(10, 78)
uop_7657 = relay.asinh(uop_7652.astype('float32')) # shape=(10, 78)
func_6431_call = mod.get_global_var('func_6431')
func_6434_call = mutated_mod.get_global_var('func_6434')
var_7661 = relay.var("var_7661", dtype = "bool", shape = (20, 4))#candidate|7661|(20, 4)|var|bool
call_7660 = relay.TupleGetItem(func_6431_call(relay.reshape(var_7661.astype('bool'), [80,])), 1)
call_7662 = relay.TupleGetItem(func_6434_call(relay.reshape(var_7661.astype('bool'), [80,])), 1)
output = relay.Tuple([call_7604,bop_7622,bop_7629,bop_7645,uop_7655,call_7660,var_7661,])
output2 = relay.Tuple([call_7605,bop_7625,bop_7632,bop_7648,uop_7657,call_7662,var_7661,])
func_7666 = relay.Function([var_7597,var_7661,], output)
mod['func_7666'] = func_7666
mod = relay.transform.InferType()(mod)
var_7667 = relay.var("var_7667", dtype = "float64", shape = (10, 78))#candidate|7667|(10, 78)|var|float64
var_7668 = relay.var("var_7668", dtype = "bool", shape = (20, 4))#candidate|7668|(20, 4)|var|bool
output = func_7666(var_7667,var_7668,)
func_7669 = relay.Function([var_7667,var_7668,], output)
mutated_mod['func_7669'] = func_7669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3730_call = mod.get_global_var('func_3730')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_7692 = relay.TupleGetItem(func_3730_call(), 0)
call_7693 = relay.TupleGetItem(func_3731_call(), 0)
var_7766 = relay.var("var_7766", dtype = "float32", shape = (16, 10, 11))#candidate|7766|(16, 10, 11)|var|float32
bop_7767 = relay.bitwise_xor(call_7692.astype('uint8'), var_7766.astype('uint8')) # shape=(16, 10, 11)
bop_7770 = relay.bitwise_xor(call_7693.astype('uint8'), var_7766.astype('uint8')) # shape=(16, 10, 11)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_7774 = relay.TupleGetItem(func_3785_call(), 0)
call_7775 = relay.TupleGetItem(func_3787_call(), 0)
output = relay.Tuple([bop_7767,call_7774,])
output2 = relay.Tuple([bop_7770,call_7775,])
func_7779 = relay.Function([var_7766,], output)
mod['func_7779'] = func_7779
mod = relay.transform.InferType()(mod)
mutated_mod['func_7779'] = func_7779
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7780 = relay.var("var_7780", dtype = "float32", shape = (16, 10, 11))#candidate|7780|(16, 10, 11)|var|float32
func_7779_call = mutated_mod.get_global_var('func_7779')
call_7781 = func_7779_call(var_7780)
output = call_7781
func_7782 = relay.Function([var_7780], output)
mutated_mod['func_7782'] = func_7782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7457_call = mod.get_global_var('func_7457')
func_7459_call = mutated_mod.get_global_var('func_7459')
call_7810 = relay.TupleGetItem(func_7457_call(), 1)
call_7811 = relay.TupleGetItem(func_7459_call(), 1)
output = relay.Tuple([call_7810,])
output2 = relay.Tuple([call_7811,])
func_7817 = relay.Function([], output)
mod['func_7817'] = func_7817
mod = relay.transform.InferType()(mod)
mutated_mod['func_7817'] = func_7817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7817_call = mutated_mod.get_global_var('func_7817')
call_7818 = func_7817_call()
output = call_7818
func_7819 = relay.Function([], output)
mutated_mod['func_7819'] = func_7819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3743_call = mod.get_global_var('func_3743')
func_3745_call = mutated_mod.get_global_var('func_3745')
call_7848 = relay.TupleGetItem(func_3743_call(), 2)
call_7849 = relay.TupleGetItem(func_3745_call(), 2)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_7858 = func_4080_call()
call_7859 = func_4080_call()
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_7861 = relay.TupleGetItem(func_6224_call(), 0)
call_7862 = relay.TupleGetItem(func_6226_call(), 0)
output = relay.Tuple([call_7848,call_7858,call_7861,])
output2 = relay.Tuple([call_7849,call_7859,call_7862,])
func_7867 = relay.Function([], output)
mod['func_7867'] = func_7867
mod = relay.transform.InferType()(mod)
mutated_mod['func_7867'] = func_7867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7867_call = mutated_mod.get_global_var('func_7867')
call_7868 = func_7867_call()
output = call_7868
func_7869 = relay.Function([], output)
mutated_mod['func_7869'] = func_7869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_7885 = relay.TupleGetItem(func_3218_call(), 0)
call_7886 = relay.TupleGetItem(func_3219_call(), 0)
output = relay.Tuple([call_7885,])
output2 = relay.Tuple([call_7886,])
func_7914 = relay.Function([], output)
mod['func_7914'] = func_7914
mod = relay.transform.InferType()(mod)
mutated_mod['func_7914'] = func_7914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7914_call = mutated_mod.get_global_var('func_7914')
call_7915 = func_7914_call()
output = call_7915
func_7916 = relay.Function([], output)
mutated_mod['func_7916'] = func_7916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6715_call = mod.get_global_var('func_6715')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_8011 = relay.TupleGetItem(func_6715_call(), 2)
call_8012 = relay.TupleGetItem(func_6716_call(), 2)
func_7867_call = mod.get_global_var('func_7867')
func_7869_call = mutated_mod.get_global_var('func_7869')
call_8015 = relay.TupleGetItem(func_7867_call(), 2)
call_8016 = relay.TupleGetItem(func_7869_call(), 2)
func_6842_call = mod.get_global_var('func_6842')
func_6844_call = mutated_mod.get_global_var('func_6844')
call_8017 = relay.TupleGetItem(func_6842_call(), 0)
call_8018 = relay.TupleGetItem(func_6844_call(), 0)
bop_8025 = relay.greater(call_8017.astype('bool'), relay.reshape(call_8015.astype('bool'), relay.shape_of(call_8017))) # shape=(1, 10, 11)
bop_8028 = relay.greater(call_8018.astype('bool'), relay.reshape(call_8016.astype('bool'), relay.shape_of(call_8018))) # shape=(1, 10, 11)
output = relay.Tuple([call_8011,bop_8025,])
output2 = relay.Tuple([call_8012,bop_8028,])
func_8042 = relay.Function([], output)
mod['func_8042'] = func_8042
mod = relay.transform.InferType()(mod)
output = func_8042()
func_8043 = relay.Function([], output)
mutated_mod['func_8043'] = func_8043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_8063 = relay.TupleGetItem(func_3785_call(), 0)
call_8064 = relay.TupleGetItem(func_3787_call(), 0)
func_4788_call = mod.get_global_var('func_4788')
func_4791_call = mutated_mod.get_global_var('func_4791')
var_8074 = relay.var("var_8074", dtype = "float64", shape = (780,))#candidate|8074|(780,)|var|float64
call_8073 = relay.TupleGetItem(func_4788_call(relay.reshape(var_8074.astype('float64'), [10, 78])), 0)
call_8075 = relay.TupleGetItem(func_4791_call(relay.reshape(var_8074.astype('float64'), [10, 78])), 0)
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_8094 = relay.TupleGetItem(func_5157_call(), 0)
call_8095 = relay.TupleGetItem(func_5159_call(), 0)
output = relay.Tuple([call_8063,call_8073,var_8074,call_8094,])
output2 = relay.Tuple([call_8064,call_8075,var_8074,call_8095,])
func_8115 = relay.Function([var_8074,], output)
mod['func_8115'] = func_8115
mod = relay.transform.InferType()(mod)
mutated_mod['func_8115'] = func_8115
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8116 = relay.var("var_8116", dtype = "float64", shape = (780,))#candidate|8116|(780,)|var|float64
func_8115_call = mutated_mod.get_global_var('func_8115')
call_8117 = func_8115_call(var_8116)
output = call_8117
func_8118 = relay.Function([var_8116], output)
mutated_mod['func_8118'] = func_8118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_8128 = relay.TupleGetItem(func_3064_call(), 0)
call_8129 = relay.TupleGetItem(func_3065_call(), 0)
output = call_8128
output2 = call_8129
func_8136 = relay.Function([], output)
mod['func_8136'] = func_8136
mod = relay.transform.InferType()(mod)
output = func_8136()
func_8137 = relay.Function([], output)
mutated_mod['func_8137'] = func_8137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_8164 = relay.TupleGetItem(func_3064_call(), 0)
call_8165 = relay.TupleGetItem(func_3065_call(), 0)
func_6611_call = mod.get_global_var('func_6611')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_8194 = relay.TupleGetItem(func_6611_call(), 0)
call_8195 = relay.TupleGetItem(func_6612_call(), 0)
output = relay.Tuple([call_8164,call_8194,])
output2 = relay.Tuple([call_8165,call_8195,])
func_8198 = relay.Function([], output)
mod['func_8198'] = func_8198
mod = relay.transform.InferType()(mod)
mutated_mod['func_8198'] = func_8198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8198_call = mutated_mod.get_global_var('func_8198')
call_8199 = func_8198_call()
output = call_8199
func_8200 = relay.Function([], output)
mutated_mod['func_8200'] = func_8200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4656_call = mod.get_global_var('func_4656')
func_4657_call = mutated_mod.get_global_var('func_4657')
call_8260 = relay.TupleGetItem(func_4656_call(), 0)
call_8261 = relay.TupleGetItem(func_4657_call(), 0)
func_4188_call = mod.get_global_var('func_4188')
func_4191_call = mutated_mod.get_global_var('func_4191')
var_8267 = relay.var("var_8267", dtype = "int32", shape = (540,))#candidate|8267|(540,)|var|int32
call_8266 = func_4188_call(relay.reshape(var_8267.astype('int32'), [4, 15, 9]), relay.reshape(var_8267.astype('int32'), [4, 15, 9]), )
call_8268 = func_4188_call(relay.reshape(var_8267.astype('int32'), [4, 15, 9]), relay.reshape(var_8267.astype('int32'), [4, 15, 9]), )
output = relay.Tuple([call_8260,call_8266,var_8267,])
output2 = relay.Tuple([call_8261,call_8268,var_8267,])
func_8285 = relay.Function([var_8267,], output)
mod['func_8285'] = func_8285
mod = relay.transform.InferType()(mod)
mutated_mod['func_8285'] = func_8285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8286 = relay.var("var_8286", dtype = "int32", shape = (540,))#candidate|8286|(540,)|var|int32
func_8285_call = mutated_mod.get_global_var('func_8285')
call_8287 = func_8285_call(var_8286)
output = call_8287
func_8288 = relay.Function([var_8286], output)
mutated_mod['func_8288'] = func_8288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8367 = relay.var("var_8367", dtype = "float32", shape = (2, 5, 7))#candidate|8367|(2, 5, 7)|var|float32
uop_8368 = relay.log(var_8367.astype('float32')) # shape=(2, 5, 7)
output = relay.Tuple([uop_8368,])
output2 = relay.Tuple([uop_8368,])
func_8371 = relay.Function([var_8367,], output)
mod['func_8371'] = func_8371
mod = relay.transform.InferType()(mod)
var_8372 = relay.var("var_8372", dtype = "float32", shape = (2, 5, 7))#candidate|8372|(2, 5, 7)|var|float32
output = func_8371(var_8372)
func_8373 = relay.Function([var_8372], output)
mutated_mod['func_8373'] = func_8373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5751_call = mod.get_global_var('func_5751')
func_5753_call = mutated_mod.get_global_var('func_5753')
call_8426 = relay.TupleGetItem(func_5751_call(), 0)
call_8427 = relay.TupleGetItem(func_5753_call(), 0)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_8428 = relay.TupleGetItem(func_3785_call(), 0)
call_8429 = relay.TupleGetItem(func_3787_call(), 0)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_8445 = func_3152_call()
call_8446 = func_3152_call()
func_6611_call = mod.get_global_var('func_6611')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_8447 = relay.TupleGetItem(func_6611_call(), 0)
call_8448 = relay.TupleGetItem(func_6612_call(), 0)
func_6015_call = mod.get_global_var('func_6015')
func_6017_call = mutated_mod.get_global_var('func_6017')
call_8458 = relay.TupleGetItem(func_6015_call(), 0)
call_8459 = relay.TupleGetItem(func_6017_call(), 0)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_8469 = func_2220_call()
call_8470 = func_2220_call()
output = relay.Tuple([call_8426,call_8428,call_8445,call_8447,call_8458,call_8469,])
output2 = relay.Tuple([call_8427,call_8429,call_8446,call_8448,call_8459,call_8470,])
func_8478 = relay.Function([], output)
mod['func_8478'] = func_8478
mod = relay.transform.InferType()(mod)
output = func_8478()
func_8479 = relay.Function([], output)
mutated_mod['func_8479'] = func_8479
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8480 = relay.var("var_8480", dtype = "float32", shape = (4, 6, 7))#candidate|8480|(4, 6, 7)|var|float32
uop_8481 = relay.sqrt(var_8480.astype('float32')) # shape=(4, 6, 7)
func_2340_call = mod.get_global_var('func_2340')
func_2342_call = mutated_mod.get_global_var('func_2342')
var_8502 = relay.var("var_8502", dtype = "bool", shape = (80,))#candidate|8502|(80,)|var|bool
call_8501 = relay.TupleGetItem(func_2340_call(relay.reshape(var_8502.astype('bool'), [80,])), 1)
call_8503 = relay.TupleGetItem(func_2342_call(relay.reshape(var_8502.astype('bool'), [80,])), 1)
uop_8509 = relay.erf(call_8501.astype('float64')) # shape=(8, 10, 15)
uop_8511 = relay.erf(call_8503.astype('float64')) # shape=(8, 10, 15)
output = relay.Tuple([uop_8481,var_8502,uop_8509,])
output2 = relay.Tuple([uop_8481,var_8502,uop_8511,])
func_8525 = relay.Function([var_8480,var_8502,], output)
mod['func_8525'] = func_8525
mod = relay.transform.InferType()(mod)
var_8526 = relay.var("var_8526", dtype = "float32", shape = (4, 6, 7))#candidate|8526|(4, 6, 7)|var|float32
var_8527 = relay.var("var_8527", dtype = "bool", shape = (80,))#candidate|8527|(80,)|var|bool
output = func_8525(var_8526,var_8527,)
func_8528 = relay.Function([var_8526,var_8527,], output)
mutated_mod['func_8528'] = func_8528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4293_call = mod.get_global_var('func_4293')
func_4295_call = mutated_mod.get_global_var('func_4295')
call_8549 = relay.TupleGetItem(func_4293_call(), 0)
call_8550 = relay.TupleGetItem(func_4295_call(), 0)
func_7286_call = mod.get_global_var('func_7286')
func_7288_call = mutated_mod.get_global_var('func_7288')
call_8575 = relay.TupleGetItem(func_7286_call(), 0)
call_8576 = relay.TupleGetItem(func_7288_call(), 0)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_8588 = relay.TupleGetItem(func_6224_call(), 0)
call_8589 = relay.TupleGetItem(func_6226_call(), 0)
output = relay.Tuple([call_8549,call_8575,call_8588,])
output2 = relay.Tuple([call_8550,call_8576,call_8589,])
func_8600 = relay.Function([], output)
mod['func_8600'] = func_8600
mod = relay.transform.InferType()(mod)
mutated_mod['func_8600'] = func_8600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8600_call = mutated_mod.get_global_var('func_8600')
call_8601 = func_8600_call()
output = call_8601
func_8602 = relay.Function([], output)
mutated_mod['func_8602'] = func_8602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mod.get_global_var('func_5517')
func_5519_call = mutated_mod.get_global_var('func_5519')
call_8624 = relay.TupleGetItem(func_5517_call(), 1)
call_8625 = relay.TupleGetItem(func_5519_call(), 1)
func_6906_call = mod.get_global_var('func_6906')
func_6907_call = mutated_mod.get_global_var('func_6907')
call_8630 = relay.TupleGetItem(func_6906_call(), 1)
call_8631 = relay.TupleGetItem(func_6907_call(), 1)
output = relay.Tuple([call_8624,call_8630,])
output2 = relay.Tuple([call_8625,call_8631,])
func_8635 = relay.Function([], output)
mod['func_8635'] = func_8635
mod = relay.transform.InferType()(mod)
output = func_8635()
func_8636 = relay.Function([], output)
mutated_mod['func_8636'] = func_8636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_8656 = func_4080_call()
call_8657 = func_4080_call()
output = call_8656
output2 = call_8657
func_8662 = relay.Function([], output)
mod['func_8662'] = func_8662
mod = relay.transform.InferType()(mod)
output = func_8662()
func_8663 = relay.Function([], output)
mutated_mod['func_8663'] = func_8663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8478_call = mod.get_global_var('func_8478')
func_8479_call = mutated_mod.get_global_var('func_8479')
call_8689 = relay.TupleGetItem(func_8478_call(), 2)
call_8690 = relay.TupleGetItem(func_8479_call(), 2)
uop_8691 = relay.cosh(call_8689.astype('float64')) # shape=(10, 78)
uop_8693 = relay.cosh(call_8690.astype('float64')) # shape=(10, 78)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_8699 = func_2168_call()
call_8700 = func_2168_call()
func_2368_call = mod.get_global_var('func_2368')
func_2371_call = mutated_mod.get_global_var('func_2371')
const_8707 = relay.const([6.100253,8.813407,1.985590,5.474061,-4.782747,2.204497,-1.671248,9.157392,8.139507,-5.462231,3.585814,-9.081656,-9.939560,-3.872443,4.064891,-0.844817,4.880040,7.081805,1.883420,-7.302914,-2.522505,-0.987310,5.266033,0.050203,-4.250813,-8.516812,-5.400385,2.763351,4.140222,-1.790431,1.770097,1.263446,3.790984,9.210763,1.470908,-0.533252,0.639583,-7.828014,-0.116710,8.589901,-6.683205,-9.370966,-0.051157,3.513432,6.247644,-0.060181,-7.732389,8.763976,-3.907295,-3.004183,-7.547032,4.635801,3.360256,8.536650,4.336987,-5.570072,-5.865946,-8.125949,-1.206804,-3.129670,-3.379056,-3.419634,-7.425584,-8.892790,-2.764685,-6.295409,1.975135,-3.260775,-1.770247,-0.342081,-4.740473,4.468920,3.058241,4.148131,6.881026,-1.554200,6.162951,-5.741088,-4.668602,-9.414821,2.073963,-0.467916,9.793659,6.535128,-5.650097,1.692436,-5.928465,2.178668,5.595011,0.689060,-3.154062,-8.521713,-2.332867,6.094929,2.515261,0.104983,-5.271769,9.975992,-2.265176,3.715192,-7.995456,4.981299,8.432941,-6.791163,5.013724,7.000702,3.127698,4.150313,-5.241194,0.892556,0.575663,-2.581390,-9.889019,1.310276,-9.579969,3.505000,6.677740,3.995816,9.322887,4.831059,5.147246,-5.228965,-5.224368,-4.987003,-7.311831,-5.413973,-9.799972,5.115381,-3.648533,9.583391,-1.083447,4.408271,7.848071,-4.030926,7.851738,-0.881219,8.335017,8.582645,-8.957816,-3.644281], dtype = "float64")#candidate|8707|(140,)|const|float64
call_8706 = relay.TupleGetItem(func_2368_call(relay.reshape(const_8707.astype('float64'), [140,])), 0)
call_8708 = relay.TupleGetItem(func_2371_call(relay.reshape(const_8707.astype('float64'), [140,])), 0)
uop_8714 = relay.sigmoid(uop_8691.astype('float32')) # shape=(10, 78)
uop_8716 = relay.sigmoid(uop_8693.astype('float32')) # shape=(10, 78)
func_6842_call = mod.get_global_var('func_6842')
func_6844_call = mutated_mod.get_global_var('func_6844')
call_8720 = relay.TupleGetItem(func_6842_call(), 0)
call_8721 = relay.TupleGetItem(func_6844_call(), 0)
output = relay.Tuple([call_8699,call_8706,const_8707,uop_8714,call_8720,])
output2 = relay.Tuple([call_8700,call_8708,const_8707,uop_8716,call_8721,])
func_8727 = relay.Function([], output)
mod['func_8727'] = func_8727
mod = relay.transform.InferType()(mod)
output = func_8727()
func_8728 = relay.Function([], output)
mutated_mod['func_8728'] = func_8728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mod.get_global_var('func_5517')
func_5519_call = mutated_mod.get_global_var('func_5519')
call_8858 = relay.TupleGetItem(func_5517_call(), 0)
call_8859 = relay.TupleGetItem(func_5519_call(), 0)
func_4275_call = mod.get_global_var('func_4275')
func_4277_call = mutated_mod.get_global_var('func_4277')
call_8873 = relay.TupleGetItem(func_4275_call(), 0)
call_8874 = relay.TupleGetItem(func_4277_call(), 0)
output = relay.Tuple([call_8858,call_8873,])
output2 = relay.Tuple([call_8859,call_8874,])
func_8905 = relay.Function([], output)
mod['func_8905'] = func_8905
mod = relay.transform.InferType()(mod)
mutated_mod['func_8905'] = func_8905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8905_call = mutated_mod.get_global_var('func_8905')
call_8906 = func_8905_call()
output = call_8906
func_8907 = relay.Function([], output)
mutated_mod['func_8907'] = func_8907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_8926 = relay.TupleGetItem(func_3785_call(), 0)
call_8927 = relay.TupleGetItem(func_3787_call(), 0)
output = call_8926
output2 = call_8927
func_8928 = relay.Function([], output)
mod['func_8928'] = func_8928
mod = relay.transform.InferType()(mod)
mutated_mod['func_8928'] = func_8928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8928_call = mutated_mod.get_global_var('func_8928')
call_8929 = func_8928_call()
output = call_8929
func_8930 = relay.Function([], output)
mutated_mod['func_8930'] = func_8930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_8946 = relay.TupleGetItem(func_3064_call(), 0)
call_8947 = relay.TupleGetItem(func_3065_call(), 0)
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_8951 = func_3933_call()
call_8952 = func_3933_call()
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_8977 = relay.TupleGetItem(func_3161_call(), 0)
call_8978 = relay.TupleGetItem(func_3162_call(), 0)
output = relay.Tuple([call_8946,call_8951,call_8977,])
output2 = relay.Tuple([call_8947,call_8952,call_8978,])
func_8984 = relay.Function([], output)
mod['func_8984'] = func_8984
mod = relay.transform.InferType()(mod)
mutated_mod['func_8984'] = func_8984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8984_call = mutated_mod.get_global_var('func_8984')
call_8985 = func_8984_call()
output = call_8985
func_8986 = relay.Function([], output)
mutated_mod['func_8986'] = func_8986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8662_call = mod.get_global_var('func_8662')
func_8663_call = mutated_mod.get_global_var('func_8663')
call_9014 = func_8662_call()
call_9015 = func_8662_call()
func_8984_call = mod.get_global_var('func_8984')
func_8986_call = mutated_mod.get_global_var('func_8986')
call_9016 = relay.TupleGetItem(func_8984_call(), 1)
call_9017 = relay.TupleGetItem(func_8986_call(), 1)
func_2295_call = mod.get_global_var('func_2295')
func_2301_call = mutated_mod.get_global_var('func_2301')
var_9024 = relay.var("var_9024", dtype = "float64", shape = (40,))#candidate|9024|(40,)|var|float64
var_9025 = relay.var("var_9025", dtype = "float64", shape = (315,))#candidate|9025|(315,)|var|float64
const_9026 = relay.const([-1.938397,-7.687459,3.296135,-7.081958,0.209838,9.782083,-0.125229,8.148412,7.451621,1.961015,-4.268352,-5.205034,7.710021,2.420464,0.922822,2.148176,6.308852,-0.667242,-7.404128,6.791395,6.512453,3.832816,1.654427,-9.057887,-6.715393,-6.037482,-4.726393,6.967170,2.352823,6.383877,7.115812,-2.672332,-8.705791,9.402482,-2.201322,9.971563,-7.834770,5.780492,5.529128,-5.283061,-9.257326,-3.029711,8.064076,-3.531590,-3.182274,-3.015791,-6.806187,-3.886877,1.676759,5.556272,-0.182738,0.155907,1.548973,-5.398538,3.373731,7.183511,-1.765393,-2.571905,7.162893,-2.912521,-1.953696,-9.942465,6.966978,-3.075232,-3.032572,-7.971614,-0.239603,0.332751,5.399223,-3.970211,-8.276289,-0.431225,-3.205227,5.280651,0.415758,9.315925,-5.549279,-4.701129,9.183129,-8.266896,4.483676,-4.876599,-6.485072,5.772517,-1.438881,-1.930211,6.656720,6.303889,-4.929384,-9.404017,-9.605742,4.118453,3.494334,-1.795485,-3.886930,-5.894637,-5.080875,1.390424,0.528517,-5.392756,3.327497,-1.790825,3.156637,-3.499921,-1.111293,3.426164,-5.789883,5.658554,-1.464868,-8.596100,-7.826892,-8.960368,-8.408916,-1.021220,5.134490,3.521553,8.201862,9.867130,4.794590,-4.422967,-6.668685,-7.827275,1.714719,-4.144573,6.422213,-4.485810,-2.553655,-9.806222,2.489863,-9.336916,3.735714,0.456791,3.334909,6.067380,-1.310111,0.097025,7.339291,9.629709,4.623127,7.316653], dtype = "float64")#candidate|9026|(140,)|const|float64
const_9027 = relay.const([-1.227108,-2.166487,-5.626422,-0.515562,-7.421193,-0.700328,6.226160,-5.123741,-6.331388,-1.165059,6.008005,-9.622335,-0.334085,5.390839,9.400406,1.699634,9.553919,5.197034,-1.787212,0.154140,1.241556,-6.537869,-0.775556,-3.534434,-1.165548,-7.533443,1.506454,6.395314,-2.233209,0.748647,0.227292,-1.357774,-7.388265,-3.966836,3.358597,3.843674,8.382049,3.121164,-0.185259,-9.169016,8.496740,-9.428269,6.034569,-4.410080,-3.457334,-0.848240,-5.134608,-5.933169,-2.780964,7.858562,8.395932,1.790589,-1.405002,-4.418782,-4.562301,-1.514523,4.069453,-6.848542,-3.354332,1.446271,-7.441981,-4.377760,-9.931140,8.753660,9.246316,-7.455923,3.552614,8.028913,9.761568,-4.279379,6.368887,6.740169,1.153500,9.728697,-5.708329,2.551054,-7.518529,6.835355,-5.653092,-5.463746,7.854873,-0.628783,-4.879958,-1.455438,0.068022,2.430332,5.871326,-8.527912,4.895545,-6.858373,-5.390325,-8.114366,6.315247,8.288701,6.791116,6.169267,-5.935839,3.743341,-3.564138,-1.407008,6.291037,-6.482966,-5.014854,7.542920,-3.440918,7.412070,9.368943,-4.973767,5.573245,5.753268,4.474677,8.675853,-6.937321,-1.140540,6.302498,8.275751,-6.365378,9.066398,-5.448213,-2.211644,6.963117,2.147133,-7.616591,5.715881,1.526495,-3.291200,-4.973365,-6.425264,-2.395318,4.701376,-9.683746,-0.357939,-9.039246,9.046230,4.438732,9.027609,-2.307306,0.483320,-2.277864,-0.826739,8.400648,-7.660137,3.899408,9.616617,1.513706,1.602087,1.784557,3.541741,5.075868,-6.717440,-6.089075,3.484389,-9.126186,8.746037,-1.324870,-7.111159,-7.258384,8.291593,2.359584,-0.844217,5.056911,-2.507285,4.550110,-6.117871,2.478285,4.384158,-0.672060,-0.548765,-2.488910,-6.863868,0.977712,-8.913935,7.698533,2.095823,-6.262491,-6.852288,6.591532,-2.753279,-2.504168,-0.121159,8.168178,7.336552,-7.063888,-6.036076,-6.302933,4.826304,6.649594,3.081860,4.426897,-5.932646,-7.252008,4.004180,2.003519,7.582135,-1.595493,5.239405,1.285888,-4.673980,-5.202280,-3.802390,1.430258,4.793556,-0.359844,1.741805,2.143081,9.028245,-3.956651,-9.821495,8.278570,4.411593,8.454636,2.929556,-6.827794,-0.272810,0.978625,5.926324,0.478331,7.223077,9.868263,0.511605,-5.897587,5.539985,-4.051880,6.366904,3.835199,8.482121,9.841465,4.335792,-0.794112,0.150052,0.359559,-0.881936,1.220895,-0.222891,7.019644,8.990682,-7.197055,-7.688986,-1.705926,-3.843490,4.528699,-7.707635,9.463987,-0.390716,-7.054138,9.824944,-6.157148,-0.683413,5.570945,-3.985040,-5.906207,4.018240,-6.701457,2.608131,8.686172,-2.250122,-2.703404,7.233016,4.144719,0.697888,4.246756,8.297178,3.897081,1.946581,-7.124255,1.487614,-0.665469,8.420300,-6.053443,8.725153,8.082952,-4.130159,5.681476,1.521843,2.522265,-4.717208,6.949855,-2.650667,4.371292,4.711472,-1.824082,-4.550779,6.958359,9.660292,0.216462,4.753906,7.834736,-5.732070,-9.056932,9.761040,-5.187513,-2.392970,6.481764,-5.076351,7.144363,-7.076680,-1.040400,-5.316389,-1.238381,-1.238859,-3.113741,-5.718476,2.652873,-8.714118,-5.130100,-9.593118,4.412484,-7.049403,0.657313,4.633267,6.254248,-1.537270,2.774969,2.494682,2.456822,9.808209,-7.632955,4.666601,-7.597784,2.005137,1.418180,1.589317,-2.680254,5.481614,9.239018,-0.905890,-8.227111,-7.243682,9.184998,9.750794,7.067408,9.045760,1.097064,-8.861260,-7.604052,-9.445862,2.366855,2.514668,-2.986606,8.986106,5.352256,-1.649668,8.731477,1.616128,-9.519979,9.380321,7.939163,0.821978,5.389283,-0.091795,3.407439,1.406738,4.724472,7.843795,2.245481,4.050197,-3.706639,-3.566023,-1.640389,5.186753,-8.870105,3.223161,4.238993,-3.157267,-7.693331,-7.258594,-4.697722,-7.339166,-1.747174,0.039886,-0.990830,1.332276,-0.881287,-9.899161,9.412292,0.314273,-5.057219,-5.700727,-8.611116,-2.118164,1.734145,-7.663093,-1.860616,3.242609,-7.852232,-8.477971,3.948436,-5.208144,4.566962,7.212302,-3.489835,2.780846,8.908512,-7.009374,-5.545430,-9.672457,6.229314,3.598365,9.731294,5.813173,1.057589,-8.464161,1.088174,-3.768870,-4.035592,7.576752,6.570862,0.837629,-5.960454,-0.144368,2.463455,0.739140,4.293875,-3.803953,5.975949,2.199135,-0.936207,-5.723790,-3.447929,-5.109050,-9.852543,6.119632,-8.364693,-4.787758,-7.367921,-9.805941,5.178739,-8.865932,-5.351865,5.617091,-2.851032,5.752402], dtype = "float32")#candidate|9027|(432,)|const|float32
var_9028 = relay.var("var_9028", dtype = "float64", shape = (144,))#candidate|9028|(144,)|var|float64
call_9023 = relay.TupleGetItem(func_2295_call(relay.reshape(var_9024.astype('float64'), [1, 10, 4]), relay.reshape(var_9025.astype('float64'), [105, 3]), relay.reshape(const_9026.astype('float64'), [140,]), relay.reshape(const_9027.astype('float32'), [36, 12]), relay.reshape(var_9028.astype('float64'), [144,]), ), 3)
call_9029 = relay.TupleGetItem(func_2301_call(relay.reshape(var_9024.astype('float64'), [1, 10, 4]), relay.reshape(var_9025.astype('float64'), [105, 3]), relay.reshape(const_9026.astype('float64'), [140,]), relay.reshape(const_9027.astype('float32'), [36, 12]), relay.reshape(var_9028.astype('float64'), [144,]), ), 3)
output = relay.Tuple([call_9014,call_9016,call_9023,var_9024,var_9025,const_9026,const_9027,var_9028,])
output2 = relay.Tuple([call_9015,call_9017,call_9029,var_9024,var_9025,const_9026,const_9027,var_9028,])
func_9032 = relay.Function([var_9024,var_9025,var_9028,], output)
mod['func_9032'] = func_9032
mod = relay.transform.InferType()(mod)
var_9033 = relay.var("var_9033", dtype = "float64", shape = (40,))#candidate|9033|(40,)|var|float64
var_9034 = relay.var("var_9034", dtype = "float64", shape = (315,))#candidate|9034|(315,)|var|float64
var_9035 = relay.var("var_9035", dtype = "float64", shape = (144,))#candidate|9035|(144,)|var|float64
output = func_9032(var_9033,var_9034,var_9035,)
func_9036 = relay.Function([var_9033,var_9034,var_9035,], output)
mutated_mod['func_9036'] = func_9036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7286_call = mod.get_global_var('func_7286')
func_7288_call = mutated_mod.get_global_var('func_7288')
call_9048 = relay.TupleGetItem(func_7286_call(), 0)
call_9049 = relay.TupleGetItem(func_7288_call(), 0)
func_613_call = mod.get_global_var('func_613')
func_616_call = mutated_mod.get_global_var('func_616')
const_9051 = relay.const([-7.239229,-6.615746,6.919464,0.340175,-2.443610,7.812148,0.350765,9.557159,-2.013636,5.564713,-7.526038,3.649934,-5.482947,3.204013,4.897820,4.519779,-7.775613,-6.055657,5.698759,9.040445,-1.937700,4.190283,4.967293,9.291843,-1.863317,-9.057426,9.526878,6.668326,8.025035,-2.634048,-5.078965,-0.647457,9.630153,-2.179880,-3.575313,1.124365,5.033816,7.479910,5.309009,-0.105684,0.213648,5.049203,-0.930431,-6.356760,2.027518,-6.214607,-5.181845,-9.931674,-6.928346,-4.091828,-7.615616,9.083301,7.274821,-0.117522,9.752556,-4.828400,5.994760,7.835195,-3.502290,-8.566177,-0.375152,6.863069,7.659852,2.765204,1.092438,8.513383,3.093986,6.844052,5.084916,5.144420,-7.494285,0.259864,2.868802,-2.979177,-2.174600,-3.914893,5.606526,8.105219,8.412947,-1.325050,-5.943753,8.718669,-6.157463,-5.276050,-2.610815,-5.865302,9.268586,0.088559,3.496384,8.682884,-4.834880,-1.020824,8.229261,-1.375716,-6.684276,3.921462,-7.712739,-8.437060,1.124136,-6.092782,4.358115,5.313940,-5.885462,6.806480,-3.478330,6.069040,-3.855545,-2.448187,2.064087,6.337512,-0.465091,6.388313,0.110730,5.679727,-5.903455,-4.502472,4.011324,1.421415,-3.361059,0.031219,4.213517,0.013799,-5.565269,8.504770,0.781851,-1.863839,-6.790154,-5.395773,0.294220,-1.578000,-5.156194,9.191959,-8.782565,2.197113,-6.435010,5.321032,-4.703414,6.397935,6.423426,-4.437700,1.740749,-2.777628,-2.014770,2.073710], dtype = "float64")#candidate|9051|(144,)|const|float64
call_9050 = relay.TupleGetItem(func_613_call(relay.reshape(const_9051.astype('float64'), [16, 3, 3])), 0)
call_9052 = relay.TupleGetItem(func_616_call(relay.reshape(const_9051.astype('float64'), [16, 3, 3])), 0)
output = relay.Tuple([call_9048,call_9050,const_9051,])
output2 = relay.Tuple([call_9049,call_9052,const_9051,])
func_9086 = relay.Function([], output)
mod['func_9086'] = func_9086
mod = relay.transform.InferType()(mod)
output = func_9086()
func_9087 = relay.Function([], output)
mutated_mod['func_9087'] = func_9087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7914_call = mod.get_global_var('func_7914')
func_7916_call = mutated_mod.get_global_var('func_7916')
call_9108 = relay.TupleGetItem(func_7914_call(), 0)
call_9109 = relay.TupleGetItem(func_7916_call(), 0)
func_2707_call = mod.get_global_var('func_2707')
func_2709_call = mutated_mod.get_global_var('func_2709')
const_9116 = relay.const([2.398408,-5.299746,5.107145,2.563764,2.246324,-3.665121,8.741559,4.075259,-6.733357,-5.571204,-6.570185,-4.160282,-6.133411,4.742036,-9.562517,-5.354326,2.047568,2.672862,-8.278429,0.735731,-5.775212,-3.417300,-6.339946,-8.601741,-0.894429,-3.293840,5.160556,-2.720561,9.365766,5.301249,-7.106773,4.296323,-4.391390,3.870186,2.072976,-7.839386,-7.075091,1.346583,-3.511011,1.853150,-9.268988,1.584624,-1.145569,-5.549801,7.174770,6.850217,3.211527,6.261121,5.380181,-5.052398,-2.799755,5.162575,3.970111,8.604610,-2.160301,-8.481609,-5.637558,5.684585,1.132952,-6.220487,0.788666,0.032744,2.358080,6.192061,2.352175,8.792316,-0.306904,-7.695204,-5.956867,-2.539680,4.529012,0.546126,-3.174339,-3.156541,-8.811305,0.510614,7.368488,-3.783742,9.443178,7.222719,0.928161,-4.360349,5.454557,-9.668798,6.453965,2.226054,1.511291,-7.491518,2.966919,-3.877404,-5.035048,2.880126,-4.740337,-5.859965,5.903529,-8.269597,-3.290045,7.799610,4.867554,7.772217,-0.879665,4.906867,-3.621938,7.800082,6.640999,1.728907,8.065572,5.971247,6.637986,-7.097412,9.731480,5.346939,7.158756,-1.610808,-0.743790,9.273672,-1.434487,8.064722,3.410109,-5.476886,-2.450962,-2.355207,-1.049158,0.170931,0.790027,6.411938,-4.595882,-9.567552,5.671321,-6.305757,8.428358,-7.885593,1.534640,-9.693432,-6.858378,7.924019,-4.417136,1.162649,5.356865,-4.217160,-9.302255,7.918445,9.874766,-0.592912,-1.852412,-1.598263,3.076262,2.048275,-9.393407,9.762457,-3.886908,7.723472,-8.427254,-8.245178,4.533154,-7.457541,-8.776170,-6.688225,3.027707,-0.411483,-7.333764,1.816828,1.999750,-9.583422,-6.555656,-5.723723,-2.262453,-3.693090,-2.494989,-3.769333,1.232007,1.045388,-4.258954,4.964388,7.222195,-0.791686,9.692535,4.886326,-2.883299,-3.558833,4.832953,-5.056356,0.609505,-5.312513,8.391571,1.952795,9.301841,-8.888034,2.957747,5.527706,2.317327,-9.557431,-1.301166,1.293127,0.080154,6.894956,-4.498821,-3.999676,-9.373417,-6.193171,4.357492,9.518394,-7.784795,-3.675510,1.529314,-2.641996,6.695341,8.693410,-8.820722,6.289984,2.115289,-3.141483,-1.302058,8.015125,4.581503,-9.490077,9.420732,6.087450,6.269325,3.033320,-5.070146,5.002163,-5.757598,6.602653,7.211276,-1.835847,8.164749,-1.747694,5.627551,1.400103,0.187228,6.050386,8.752689,2.561297,1.026046,9.802012,-2.096807,7.930404,-6.414056,-4.845923,8.790522,-9.769759,2.837980,-5.069552,-7.899184,-3.638584,5.205835,-2.053562,-4.016532,7.429942,1.084406,5.017433,7.366010,-0.016606,5.799867,3.255357,-4.281289,-2.690220,0.821481,-8.486277,-2.000821,5.143422,0.584934,-4.001902,6.238608,5.474720,-7.602592,8.335944,6.528225,9.264989,-5.337327,-7.221787,-4.427918,-3.790201,4.121061,2.089014,7.418675,-2.045895,5.364468,4.722558,-3.973681,6.752425,4.617131,3.076589,-5.515655,-8.588358,7.772905,1.589203,3.897887,6.092787,0.824310,-0.210558,-7.388109,5.803133,4.070460,-9.780287,4.030422,-5.625420,-0.170826,9.820006,0.557951,3.563704,-0.344486,-6.971282,7.897863,0.019244,8.124816,9.624964,-8.640350,6.757726,4.767523,8.870380,6.938448,-9.070703,8.685965,-4.584649,6.895981,-0.940742,2.773799,5.184035,-7.437958,2.884357,-7.813825,0.300850,8.550453,-6.468943,6.480891,5.831249,2.833320,-4.520288,2.074680,5.878398,3.004031,4.331728,0.144209,8.326092,1.074529,4.723481,6.304530,-2.418317,7.430647,-1.143428,-6.631554,2.798293,9.950855,5.474167,-9.811910,6.820161,-1.429350,-1.394317,9.837020,0.560326,-0.201676,-5.815388,-7.002537,-0.446138,7.338220,-3.034624,-5.313533,2.892682,5.761479,0.095280,-5.015817,9.098177,8.689375,-4.725621,9.384408,1.711036,-6.697769,-5.987326,-8.744369,-8.688204,0.357060,5.406828,-2.654482,1.297949,1.696065,9.379882,3.188312,-9.361408,9.656979,0.605022,6.398094,-0.251537,-5.069225,-6.364194,-8.817080,-6.593842,7.882654,6.310730,-8.945812,6.766266,4.281898,5.271928,-6.747202,9.482001,-5.192886,-9.510892,5.650908,1.054304,9.755404,-9.506511,-4.327549,8.576560,1.384973,9.020307,2.568657,5.128446,-6.423011,4.878340,6.448178,-6.216406,4.172099,1.229083,9.869263,-7.013211,-4.441109,-4.948947,3.966204,-1.021572,0.766974,0.311499,-2.628602,4.622541,1.210185,6.435271,-6.865892,9.142600,5.006725,-6.747426,4.303883,9.689005,-4.827963,0.964209,-9.851765,-0.968998,5.802340,-2.060301,-5.955384,-8.861905,9.495168,-7.661234,3.506816,2.968925,-6.725910,-3.264861,1.988281,6.713770,3.555004,1.905376,-5.304177,3.013055,4.485092,-5.341572,-9.675484,-9.309973,-1.603795,4.436620,-4.587725,-0.456105,-4.829644,-7.992849,8.015710,8.001069,-1.726856,-1.701532,-2.499130,7.190009,0.490808,-4.291889,-7.708637,1.775747,5.095902,7.164861,-2.403906,0.945729,-3.795634,-8.151327,6.360946,-7.382590,-8.593906,0.978103,4.019415,3.175078,-1.208462,-4.340502,-1.242323,8.929913,-0.816963,8.573449,1.747639,5.146804,-3.844225,6.526899,-2.011163,-2.872120,-9.408234,6.147293,-5.567344,-6.092171,-5.663871,6.510874,9.549686,0.685036,1.641081,-5.805134,8.521745,-8.398337,6.191404,7.829864,-3.152296,-4.219719,7.985912,-0.777298,-2.284448,-4.529661,8.993832,5.814279,3.688358,-2.407561,9.003326,9.019539,-6.142370,0.806103,5.987657,2.856923,-8.843096,-4.366076,-1.540454,6.714837,9.847490,8.691278,2.283244,5.682826,3.914861,-9.136372,-7.097809,0.144120,3.587806,-4.592971,-2.992840,-9.848215,-2.762149,-7.497114,4.529731,1.198923,-5.992290,1.988716,-7.554429,-3.703999], dtype = "float32")#candidate|9116|(550,)|const|float32
call_9115 = func_2707_call(relay.reshape(const_9116.astype('float32'), [5, 10, 11]))
call_9117 = func_2707_call(relay.reshape(const_9116.astype('float32'), [5, 10, 11]))
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_9118 = func_3152_call()
call_9119 = func_3152_call()
func_1364_call = mod.get_global_var('func_1364')
func_1367_call = mutated_mod.get_global_var('func_1367')
const_9122 = relay.const([8.628454,-7.932604,-2.817119,-7.797700,-4.175227,7.862897,9.019041,3.997566,4.600662,3.785069,-4.206162,5.099627,-5.404795,9.919853,8.675162,-2.548738,-0.318270,-0.991660,4.601373,5.431022,4.818240,0.209977,-9.405607,-0.523693,-1.978788,7.989902,-0.029991,6.222711,8.478049,-7.958490,7.277248,-3.123390,8.301911,-9.459867,3.345079,4.505769,-1.665268,0.104465,3.058464,9.598149,0.895863,-9.112990,2.643176,-0.756381,-7.088738,5.442342,-9.991816,-8.643376,-4.796844,-2.469674,-4.607112,3.144501,-8.713351,-3.760565,-1.331974,-7.560675,-8.331695,0.284119,-8.157707,9.746369,6.536227,-9.818362,-0.053779,7.282437,-5.054704,-8.466310,1.710386,6.437123,-5.877280,9.810671,3.484665,3.901413,-0.192980,3.935914,-9.749655,-5.780854,-6.105275,6.306356,9.900410,5.220155,4.822588,-2.722728,2.938819,-3.209218,4.226231,9.588544,0.060229,1.648342,0.384461,-6.087871,1.701135,8.040577,-1.432443,-7.630978,-3.472347,6.201496,8.033461,-3.320753,9.672546,-8.510112,9.844167,-3.870382,-7.213181,-4.094864,-1.208632,-2.350174,3.941281,7.174785,-6.105276,1.002978,-9.490518,-1.938030,0.439848,-4.057617,-3.754460,9.145901,-6.939264,-1.731802,9.016065,5.318038,-0.291528,5.061138,4.213357,8.410362,-5.613872,-9.662011,7.802304,-2.028275,-0.284444,1.900277,-7.849468,-0.550422,-4.309998,9.992167,4.929312,-1.106932,-0.220291,-6.663092,-9.917706,-5.602310,-2.102207,1.019689,6.414382,-9.345748,6.105390,-4.877771,8.762991,-0.727619,-5.318098,9.865402,-3.144227,9.503298,-4.406908,4.779832,7.862874,2.771017,-0.200965,2.324401,9.288131,4.733099,9.369055,-4.061661,-3.124527,2.767982,-5.272845,9.493399,-4.462823,-3.722478,-0.902911,1.596897,9.898124,2.160074,-9.477421,1.635762,2.937407,-7.625715,0.517303,3.305001,0.358527,-2.687814,0.655459,1.974334,-6.489984,-5.881752,2.082897,-7.599318,3.249632,-5.260460,-8.958458,9.764457,9.827616,-5.584455,-4.944356,-2.581825,-3.574347,8.348583,-3.061465,1.908558,-3.924981,1.333159,-1.939076,-4.310857,-4.601498,0.456694,9.386950,-6.550700,-0.146503,8.518953,-3.721675,-4.481786,-7.166678,-8.451853,-9.201707,0.028573,-9.095470,-4.244004,-7.730949,-2.973055,-5.678930,9.011501,-5.958203,-7.659858,-1.113140,2.142025,1.468833,-8.037823,8.755204,9.193464,-8.787257,0.265916,2.909332,8.782603,-6.057676,-9.773263,2.008413,-4.273324,4.886605,-7.646376,-2.619841,-7.072073,-3.041409,1.649645,-0.737554,9.123261,4.003355,4.771051,4.568147,-4.008689,-2.806830,-5.829051,-9.231091,1.208332,2.413519,-8.017679,7.668037,9.091600,2.845488,6.219533,6.469255,-5.216585,8.934281,-9.531295,7.593384,3.755865,1.963239,5.160438,-2.417903,-6.546811,5.982401,-8.617272,2.626711,-8.820009,-0.394807,-1.523003,-0.442614,2.427980,-0.595575,-8.716783,-3.996280,6.946415,0.657602,-5.119902,3.140091,0.718611,9.376973,5.877214,-5.158000,5.993150,-3.274784,-1.937849,-6.817216,-9.403072,4.256648,-6.129804,-4.705695,-3.101068,8.069945,-4.405054,6.161766,9.531032,2.282116,0.756998,-2.671999,-7.542831,9.973158,1.094364,-4.500167,-4.122914,5.082744,-1.954204,6.510285,3.796355,5.853462,4.578812,-6.754415,3.067606,-7.590896,5.353370,7.844239,1.226116,-4.403952,-5.674674,-4.276836,5.680880,-6.845145,-9.616153,-1.100377,-6.999596,3.708613,-0.194419,-9.365658,0.037955,-2.573459,1.440460,-0.832868,-8.595425,2.859084,-5.089841,-2.005372,9.098850,0.767188,-4.279699,-7.436502,1.280022,-8.364921,4.530864,0.162670,4.094689,9.357764,9.002485,0.881831,-0.825952,-7.495136,5.388096,-0.130056,4.560996,-2.810493,9.365446,-6.970083,-1.920099,-7.833388,9.063028,-3.931783,-6.664690,7.654756,3.096762,7.775038,-8.118811,-8.351329,-7.282316,-0.992290,-9.792947,8.287795,2.498234,-6.805555,6.687143,1.364251,-9.891322,0.269848,4.966136,-3.884418,-8.889085,9.457830,-4.419034,-6.543856,-6.920117,-4.041716,3.348028,0.385231,-6.560324,-4.139045,-3.156561,-1.410549,0.309424,8.476608,9.925785,1.870151,-0.748081,-2.441709,8.561490,9.978591,0.438596,-8.614006,-2.652907,-4.507784,-0.568210,-2.218987,-2.521049,0.390585,-1.648747,3.689090,5.150969,7.107298,3.110901,-7.093252,-7.717366,-3.938876,8.604853,-5.185460,-0.732149,-4.372452,7.673428,-8.387383,-3.335977,3.682852,-3.838710,-7.217797,-2.760176,4.068544,9.560892,-5.235508,-3.219463], dtype = "float32")#candidate|9122|(432,)|const|float32
const_9123 = relay.const([3.708120,-2.240950,-8.957284,-1.857272,-3.690089,4.248303,8.372527,-6.554372,9.679845,-0.558158,-9.720602,-0.813889,2.414565,7.180265,-9.037605,1.767533,2.608875,-8.870311,2.216790,-0.128210,7.135337,-7.863524,2.179101,-3.490348,5.811612,-7.949980,-5.758165,-1.175877,4.339552,-2.622638,-7.561372,9.231428,-1.754683,-6.067498,-4.334181,3.226313,-3.912139,-1.227429,-2.001986,-0.123027,5.933078,8.357738,7.149412,-8.826306,1.464529,-6.792693,-8.035489,6.367104,4.593263,-3.440916,-2.267061,0.853946,0.389732,6.933305,-7.812769,4.479649,-8.241510,7.890095,-5.257229,-5.517186,2.525436,-0.356145,-3.924240,-2.448190,2.370973,3.872533,-2.620801,-5.541201,-0.511507,2.542110,8.362296,3.754694,6.537048,9.603951,-7.392503,8.525645,-6.166417,9.642455,-5.436699,0.803428,-7.819033,8.218100,7.306841,0.992905,5.307902,2.619315,2.597751,-0.361564,2.125802,7.509140,7.661708,2.179762,-1.634700,-3.700623,-0.757956,-2.550179,-6.765937,5.491839,7.183302,-8.549333,1.194270,9.659989,-2.770058,1.552577,5.023295,2.565089,-0.463007,-9.126289,6.364063,9.123513,-9.323204,-2.093436,8.664174,9.194460,-9.054404,-1.455769,2.002012,7.403330,5.065328,8.802605,0.064440,-5.777003,-8.468153,-5.612180,2.831950,2.824341,0.218175,3.856186,-1.739955,8.695600,-0.083730,-0.050516,3.237383,3.200651,0.024582,9.291237,7.095970,-4.683857,-0.137991,1.153731,-7.000518,-1.963829,-9.154843,-7.183815], dtype = "float64")#candidate|9123|(144,)|const|float64
call_9121 = relay.TupleGetItem(func_1364_call(relay.reshape(const_9122.astype('float32'), [3, 12, 12]), relay.reshape(const_9123.astype('float64'), [144,]), ), 0)
call_9124 = relay.TupleGetItem(func_1367_call(relay.reshape(const_9122.astype('float32'), [3, 12, 12]), relay.reshape(const_9123.astype('float64'), [144,]), ), 0)
func_7156_call = mod.get_global_var('func_7156')
func_7158_call = mutated_mod.get_global_var('func_7158')
const_9138 = relay.const([6.753960,-3.700960,-5.089655,0.462557,-5.056050,1.169611,-4.692757,-5.492436,5.403829,-4.402595,8.443142,3.585623,-2.852485,-5.846809,3.738620,-3.522186,0.124642,-1.379465,-2.551937,-7.958108,7.353768,-4.563699,3.234319,-0.235344,-6.093852,2.130919,2.170271,-9.934737,-6.316410,0.463759,-2.694334,6.139461,4.899214,8.688072,8.026314,-9.052397,8.664055,3.100552,0.746831,3.655623,-0.856439,4.435139,-1.774447,-2.191234,-6.690937,-5.682132,5.961886,6.160665,5.113147,3.933652,-7.974415,-0.158908,-8.593247,-6.292246,8.079437,-5.477833,-0.333235,8.761873,3.802400,-7.848800,6.651705,-0.818733,-6.908010,2.765671,-5.392096,-2.278460,-4.782042,5.452847,-8.024901,1.295214,7.744624,-6.266802,0.406221,-4.678743,5.889968,1.246007,3.868528,5.735207,5.739648,-5.428949,7.831008,-0.420401,7.539812,3.665678,-0.362207,1.877406,-7.467098,4.365007,2.468231,-5.873602,-1.145485,8.409023,5.427159,7.605089,-8.828697,-9.758587,9.468089,7.527149,-9.956299,-1.572760,3.200021,9.180814,1.505713,-3.189284,-3.291288,4.671791,-1.131839,6.635041,-4.063224,-9.664226,-1.839296,-5.854433,1.145375,-8.883670,-8.811271,-5.395666,-6.264521,2.609645,0.569166,-5.433847,-3.239463,-4.117546,-7.177115,-5.955019,1.299750,4.318577,-6.318686,8.942696,-6.783407,6.371820,-6.322913,-4.659638,5.723739,2.407812,8.887063,2.540535,6.382599,-3.726371,9.766370,-3.259646,8.057882,-0.715956,-0.606536,-4.107266,3.577983,8.854549,4.610575,-6.085084,-4.014691,4.747999,5.519474,3.824504,9.447540,-6.944283,6.859427,5.516582,1.439573,-2.663400,0.849042,-8.526610,-7.835100,-0.938416,5.476358,2.920322,-2.583935,-1.188252,9.902665,6.335689,8.167022,7.124515,-2.045881,-9.428436,-7.726393,7.929539,7.777688,-4.300042,-5.404154,8.679404,0.466722,0.133080,-0.573384,5.852405,9.195229,-4.097398,-4.835884,6.923034,-1.137778,-0.474123,-0.681148,-2.373972,0.107487,-5.473758,8.346636,-4.881482,-5.358977,7.248984,5.147543,-3.942373,3.886544,4.180673,-2.252886,-9.079346,-1.708062,8.318210,3.074048,-4.942751,-8.628252,-4.275030,0.207667,-2.839719,-8.487597,-7.422239,-7.016179,-7.233304,5.765124,0.958473,1.226894,-0.927190,9.576892,-2.014677,8.380403,7.150627,0.942921,6.536787,-3.547489,-0.439360,9.393947,-9.482775,7.892074,5.167129,5.517874,-2.285220,0.335864,-4.466926,-9.641010,5.451995,-5.174485,2.572674,-2.376336,-5.487101,-4.408155,8.798977,4.063509,3.764376,-6.299245,5.973464,-9.175100,-2.781194,-3.831576,-2.006714,-5.540726,-8.639348,-3.752612,-8.978373,-7.853503,-6.922251,-6.757090,8.674693,1.738323,-0.307319,8.023844,0.581158,-4.141330,1.017996,1.347786,4.695418,9.497545,-1.038945,-5.435018,-5.125087,3.863595,1.602304,-3.502166,5.228302,-8.435832,-6.248021,9.946434,3.565847,2.746376,-8.014171,-8.228639,-7.659332,5.540739,9.307154,-6.719463,-5.421070,-4.471690,1.622514,-1.490166,5.799685,-8.417299,4.689525,9.297830,0.257163,4.479693,4.472188,-3.429402,-4.671021,-9.081854,6.362542,3.883125,-0.350039,6.148956,0.296585,-0.828598,-5.878686,-7.283006,-3.491107,-8.823325,-0.921010,3.352351,3.097828,-2.376197,9.075843,-4.973721,3.308077,6.969697,2.114902,0.141828,-3.382805,4.922126,-8.199900,-5.121187,-1.889176,8.870517,9.267756,-0.081294,-1.358440,-0.408459,-7.206383,-4.272078,-3.455085,9.567094,-1.654329,-5.974811,3.604183,-6.976058,1.351938,-9.804277,1.806558,6.061452,6.350812,-3.974194,-4.141824,1.084124,1.447113,-2.991016,2.806667,6.072350,-5.607782,9.441098,-0.224362,2.075369,-6.752590,5.098615,9.961189,-8.184997,-6.235794,-2.582297,6.144339,7.746465,2.411503,9.241231,-1.795588,4.687459,-2.222723,-1.125622,-0.013663,0.181863,4.799366,-3.202385,7.296150,1.729591,6.730340,-0.176739,-7.183591,7.899981,9.108299,-1.419866,-7.711120,-0.751439,-6.677209,0.493410,-6.514429,-3.181676,2.841718,7.427274,0.894491,-7.866623,-3.401482,-5.382732,0.693586,8.156049,-7.735624,-2.812809,6.551893,4.694034,0.703669,-0.908009,6.587690,0.564681,2.134729,1.404182,-0.966524,-2.918828,-9.553737,0.661167,-6.209885,-8.270716,-7.682747,6.492890,6.690695,-7.488088,1.595731,1.139367,0.200854,1.796070,9.763839,2.561239,7.461635,-0.876054,-8.975681,2.162157,-5.635194,9.420531,-5.252895,-5.363725,-8.309079,-3.095159,4.829082,-9.844292,-9.871963,-8.142970,8.067553,4.967805,7.499764,-9.902434,3.634838,-5.823549,-9.951409,5.693290,3.017292,-2.303828,-9.125830,8.995180,-0.785679,-9.594173,-2.330468,-4.701479,-8.883141,-2.502785,-2.349928,-2.339045,-7.116443,2.266167,-4.019170,1.613525,9.406039,0.571055,-4.442348,2.205314,8.270994,1.553059,-3.888191,9.249714,-5.612341,-6.396630,-4.257556,-2.776549,-0.123374,4.352265,-9.313122,-7.990134,0.256500,0.741790,-8.347945,-9.824941,-8.528017,8.796053,-6.307106,-1.245516,-4.155879,5.806004,0.593439,4.170448,5.001070,-1.958497,0.723999,4.359292,4.357844,-3.265794,-8.461692,3.659827,6.775474,2.379309,0.286585,-5.873103,2.103978,-9.022537,4.120292,-5.018360,3.856550,1.540294,7.521951,0.485585,8.112223,-7.745006,-3.910828,8.786228,5.623034,4.406040,-1.407014,-8.975648,6.113775,-9.197832,4.176077,-2.688603,0.138569,0.059193,-0.530445,7.967415,8.423120,7.538096,6.192013,3.014777,-0.567874,7.057222,-6.492305,-4.009301,5.456140,-2.359328,7.956919,9.446196,-9.438093,3.555523,1.807129,7.282229,-9.632319,-5.723919,2.075448,-9.858481,3.849089,-7.270930,-9.023911,5.984515,7.308524,-6.352793,-1.122166,4.599521,-4.130022,-6.616329,-9.979722,-4.532320,-8.140345,-0.014177,-5.116754,5.978265,7.039574,3.586120,-3.183222,6.747716,1.325572,-0.970264,3.133038,-7.244657,-2.158063,0.252040,-3.646501,-5.816810,-2.707019,-3.639091,0.940937,-2.576355,3.615065,-4.913970,5.908846,4.250337,7.475616,-3.050263,-2.865723,9.016428,8.497695,4.604485,-3.347612,5.205851,-3.041500,-7.113574,7.299407,-2.817576,-1.624695,4.858958,-0.828296,-9.403119,-4.613181,-4.768401,-0.027712,-3.220899,-8.053801,2.602723,5.891494,-3.500724,8.254577,9.124254,5.819706,6.031887,0.351084,4.579747,-5.741161,4.231815,6.688480,4.251046,3.773615,2.931477,1.563714,1.583035,9.369619,-3.140196,-7.023135,-2.112867,-5.804938,4.976360,-4.487128,3.561443,8.904567,5.546977,4.272939,-7.158652,-6.037560,-6.230609,-5.558645,-1.760983,9.782539,-6.798542,1.986997,-2.171399,4.031099,1.010480,-7.457841,-9.556038,5.926097,-0.605368,-1.057701,-6.632896,6.452161,-1.900671,-0.551778,0.877338,3.057912,5.422612,-7.799590,-8.201080,2.691974,7.529865,8.095497,5.586161,-9.690073,2.332304,-3.581595,2.658872,-2.090218,-3.902926,4.921953,4.377339,9.637642,6.189686,-1.513823,4.838375,0.712852,4.960066,-4.425928,6.554803,3.334920,0.880854,-5.128761,2.368434,-6.179797,6.535786,5.553558,6.989481,8.413379,6.620907,-4.768366,-7.660099,5.211497,-4.354384,-2.777558,-2.352555,-6.385465,-4.326652,8.586093,-1.847188,1.488279,4.219223,-8.080381,5.308792,0.605431,0.666904,-0.806153,0.514016,2.353175,7.647326,4.510590,8.092697,-7.886431,8.257786,1.863439,9.435227,3.753661,-8.685752,7.459755,-3.218504,-2.831538,0.260017,9.010427,-0.749382,-4.966805,-9.855042,-3.653247,-3.824109,5.668110,-2.212900,2.778366,7.169327,-2.292836,-5.903916,-3.398314,-4.803538,-8.142674,4.689555,-3.065174,-2.075961,9.989800,-0.592728,5.735431,-3.290972,-5.021317,3.816773,5.148422,3.153953,-3.473477,7.608468,-2.380868,9.389919,4.026225,-0.332371,2.790855,6.308637,0.727638,-0.452675,-1.252391,-8.167159,1.853322,-8.851274,-8.260636,-5.533627,9.989285,9.366672,0.742989,-8.696807,5.505508,-7.272723,8.000207,-3.855925,6.074054,5.805182,4.470898,8.979647,-0.027734,0.016538,5.947058], dtype = "float32")#candidate|9138|(770,)|const|float32
call_9137 = relay.TupleGetItem(func_7156_call(relay.reshape(const_9138.astype('float32'), [7, 10, 11])), 0)
call_9139 = relay.TupleGetItem(func_7158_call(relay.reshape(const_9138.astype('float32'), [7, 10, 11])), 0)
output = relay.Tuple([call_9108,call_9115,const_9116,call_9118,call_9121,const_9122,const_9123,call_9137,const_9138,])
output2 = relay.Tuple([call_9109,call_9117,const_9116,call_9119,call_9124,const_9122,const_9123,call_9139,const_9138,])
func_9149 = relay.Function([], output)
mod['func_9149'] = func_9149
mod = relay.transform.InferType()(mod)
output = func_9149()
func_9150 = relay.Function([], output)
mutated_mod['func_9150'] = func_9150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6115_call = mod.get_global_var('func_6115')
func_6116_call = mutated_mod.get_global_var('func_6116')
call_9157 = relay.TupleGetItem(func_6115_call(), 2)
call_9158 = relay.TupleGetItem(func_6116_call(), 2)
func_4333_call = mod.get_global_var('func_4333')
func_4336_call = mutated_mod.get_global_var('func_4336')
var_9162 = relay.var("var_9162", dtype = "uint8", shape = (12, 18))#candidate|9162|(12, 18)|var|uint8
call_9161 = relay.TupleGetItem(func_4333_call(relay.reshape(var_9162.astype('uint8'), [3, 9, 8]), relay.reshape(var_9162.astype('uint8'), [3, 9, 8]), ), 2)
call_9163 = relay.TupleGetItem(func_4336_call(relay.reshape(var_9162.astype('uint8'), [3, 9, 8]), relay.reshape(var_9162.astype('uint8'), [3, 9, 8]), ), 2)
func_4144_call = mod.get_global_var('func_4144')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_9166 = func_4144_call()
call_9167 = func_4144_call()
uop_9168 = relay.sin(var_9162.astype('float64')) # shape=(12, 18)
output = relay.Tuple([call_9157,call_9161,call_9166,uop_9168,])
output2 = relay.Tuple([call_9158,call_9163,call_9167,uop_9168,])
func_9172 = relay.Function([var_9162,], output)
mod['func_9172'] = func_9172
mod = relay.transform.InferType()(mod)
var_9173 = relay.var("var_9173", dtype = "uint8", shape = (12, 18))#candidate|9173|(12, 18)|var|uint8
output = func_9172(var_9173)
func_9174 = relay.Function([var_9173], output)
mutated_mod['func_9174'] = func_9174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_9232 = func_4080_call()
call_9233 = func_4080_call()
func_4824_call = mod.get_global_var('func_4824')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_9262 = relay.TupleGetItem(func_4824_call(), 0)
call_9263 = relay.TupleGetItem(func_4825_call(), 0)
func_9032_call = mod.get_global_var('func_9032')
func_9036_call = mutated_mod.get_global_var('func_9036')
var_9278 = relay.var("var_9278", dtype = "float64", shape = (40,))#candidate|9278|(40,)|var|float64
const_9279 = relay.const([-9.421505,6.979936,-8.156631,-8.981667,-1.258977,-7.647162,8.088429,5.001101,-8.417178,5.055652,9.586126,-1.093954,1.929383,5.528112,8.155354,-5.494828,4.022280,9.456230,9.004816,0.119713,-3.014681,5.153785,-2.163611,0.088161,1.787108,-2.758035,6.773325,5.216541,8.630708,7.135298,9.632591,0.466270,4.209567,-1.685336,-4.902441,-5.280302,7.361854,-3.702915,5.011949,-0.087955,-4.077936,4.852714,8.876336,-0.258596,7.382227,0.990202,4.704726,-6.286610,8.717106,-0.584383,-5.596821,3.044232,-9.834315,3.104893,2.200428,-7.053484,-8.403119,3.189330,-1.210455,-3.258999,1.881494,-3.459985,-5.131534,-6.161624,6.711003,1.971291,5.812956,0.696749,5.994398,2.149383,-6.594898,-5.906585,-7.825492,-4.556166,-6.229740,-2.055848,0.049987,-0.936933,6.704459,0.796656,1.614529,-9.172172,4.261092,-7.109517,-0.159175,-3.933901,-4.848994,6.613523,-4.471875,4.369357,4.937605,6.968706,9.349557,-1.796477,-1.003388,9.905321,2.152239,-3.699303,-4.672492,7.073419,6.518819,3.543568,-8.236331,-6.148173,3.694575,9.858494,7.139433,2.388966,4.932656,-1.446905,4.424729,7.859335,4.016019,-2.361281,4.595153,6.284438,2.378345,-2.181801,8.336676,-0.601451,-8.896607,9.796413,-1.018071,-4.563663,2.603187,1.141913,2.604681,0.190055,9.563249,-0.426773,8.456950,3.899991,-1.294956,-6.692984,-6.111546,-6.574961,5.354054,-4.916567,-2.404747,9.263527,6.342421,9.323917,2.437500,-1.897853,-4.870191,2.643953,-6.047272,-5.110462,-5.017193,-1.074850,9.237860,-4.080103,8.870239,6.604798,5.220089,5.877475,7.578913,9.803932,1.032429,0.417524,-6.895705,8.973717,0.289009,-7.739252,-7.770326,-7.234825,7.130664,-4.760029,-5.565575,4.219733,-7.905728,-5.734193,2.117242,9.473737,0.760767,-0.969231,5.971870,-8.044084,0.629624,0.158919,-3.419510,6.620893,-6.629511,-2.031893,7.588043,-0.049152,-8.881038,-4.189740,5.079947,-0.090590,-4.092929,-9.577014,-5.220136,3.597732,5.516639,1.561512,-0.718758,-9.523521,0.284334,4.771289,-1.332585,-2.218858,5.556987,-5.913027,-7.566663,0.704439,6.451646,2.472296,4.455929,7.401367,6.849853,-4.607190,1.572890,-1.625743,3.088095,-5.297069,3.680969,-0.150943,9.366995,2.696309,1.614481,-2.592843,0.913355,-4.170016,-7.766101,2.055760,-1.821149,-3.645942,-8.686139,-9.877260,-1.547403,9.727855,-5.611116,-0.791060,-2.798464,6.849882,6.410349,-7.938085,3.980487,8.866884,-7.204771,2.389143,-8.754122,5.522392,-5.005715,-4.931101,-2.034518,8.859262,5.991044,-2.848423,1.557931,9.966046,0.903314,7.691736,-4.669424,5.677188,-7.938174,6.198686,-3.437482,0.704398,4.431905,0.912058,-7.221731,-2.381932,6.415864,6.068712,-7.007193,7.619921,0.833581,6.863900,9.844902,-1.205635,2.587179,-6.088102,-7.622344,0.730833,1.161282,3.494201,7.322328,7.588391,-3.628911,8.687349,9.061795,7.587031,-6.650832,-8.777094,4.684497,4.423890,-0.132372,-4.448396,4.092574,-1.765750,-4.962451,-0.812642,1.659648,-0.458400,5.134006,0.580715,-4.632429,0.114847,1.878294,-2.012804,-2.523592,7.521612,7.195448,-0.303758,6.714806,1.302307,-4.979906,5.409593,3.491676,-3.609713,-0.848900,1.945149,-7.839652], dtype = "float64")#candidate|9279|(315,)|const|float64
const_9280 = relay.const([-8.274881,0.966457,-8.287099,5.629290,1.778989,1.907879,-5.214427,1.102951,-9.145046,-8.189999,3.431358,-7.532302,0.501416,6.705482,-6.886946,0.065543,-1.103932,-2.506766,9.386897,7.047339,2.509672,-5.822477,4.858790,3.000045,-6.836434,-0.200829,-8.811885,7.945674,7.568484,-8.020329,-2.562538,-2.268284,-0.366679,3.676480,-7.718278,4.952935,-8.730966,9.221211,7.186851,8.308242,-3.433475,2.373908,-6.910890,2.124676,6.556762,2.404458,1.664499,-8.265778,-7.912727,0.907734,5.876262,-2.895810,-8.074766,1.276892,6.382707,-7.553638,-3.681383,-2.645703,-4.183047,-2.663138,-0.315664,4.271246,8.884457,2.299049,-0.140077,-9.824557,8.146457,8.459120,-2.089560,1.053896,8.678686,-7.147756,1.165238,-9.568751,-1.413042,8.237214,-3.364144,-0.729549,7.005846,7.519612,-4.260561,9.124537,1.513339,-9.071215,8.739648,6.486109,5.642342,-8.277099,-4.284573,-2.342840,0.388118,8.311483,-5.459003,0.830879,-7.246739,3.118069,-5.293649,-1.078830,7.578997,3.322628,3.443220,9.400141,-5.489917,8.740524,-7.168065,8.913987,-9.041692,3.591632,-0.648846,-8.929178,-5.602135,-8.928033,-7.429981,-4.993778,8.720730,-0.515632,-2.135625,3.783416,5.080132,2.657372,-8.027267,3.040565,-4.653868,7.402590,0.347256,3.337326,-1.963420,-5.335707,-7.573329,-2.362604,-5.172103,-7.146641,2.457861,-3.964959,0.873646,-3.837616,-9.595629,-4.053070,3.926018,-9.861699,5.950142,-3.890943,2.168026,-2.528683], dtype = "float64")#candidate|9280|(144,)|const|float64
call_9277 = relay.TupleGetItem(func_9032_call(relay.reshape(var_9278.astype('float64'), [40,]), relay.reshape(const_9279.astype('float64'), [315,]), relay.reshape(const_9280.astype('float64'), [144,]), ), 7)
call_9281 = relay.TupleGetItem(func_9036_call(relay.reshape(var_9278.astype('float64'), [40,]), relay.reshape(const_9279.astype('float64'), [315,]), relay.reshape(const_9280.astype('float64'), [144,]), ), 7)
output = relay.Tuple([call_9232,call_9262,call_9277,var_9278,const_9279,const_9280,])
output2 = relay.Tuple([call_9233,call_9263,call_9281,var_9278,const_9279,const_9280,])
func_9285 = relay.Function([var_9278,], output)
mod['func_9285'] = func_9285
mod = relay.transform.InferType()(mod)
var_9286 = relay.var("var_9286", dtype = "float64", shape = (40,))#candidate|9286|(40,)|var|float64
output = func_9285(var_9286)
func_9287 = relay.Function([var_9286], output)
mutated_mod['func_9287'] = func_9287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_9312 = relay.TupleGetItem(func_4982_call(), 2)
call_9313 = relay.TupleGetItem(func_4983_call(), 2)
func_4188_call = mod.get_global_var('func_4188')
func_4191_call = mutated_mod.get_global_var('func_4191')
const_9336 = relay.const([-9,1,-5,2,-3,-10,4,8,-8,-10,-5,4,-7,9,5,-6,-3,10,-5,-9,5,-9,7,-10,-2,-2,1,-1,8,2,8,-8,4,6,-10,8,-6,-4,-6,-8,5,7,9,4,6,3,-5,4,8,-9,-6,-6,5,5,-6,-10,-4,9,-3,-1,1,4,4,5,9,-2,2,5,-10,7,-3,7,1,1,10,-4,5,-7,7,4,-6,9,6,5,4,4,-8,5,8,5,9,7,9,-4,7,-10,-6,-3,5,-10,10,8,-4,7,-10,-8,-4,-2,10,-7,6,2,-8,-4,-2,4,6,-2,-7,-10,3,-6,4,8,-6,3,-4,-3,9,-7,-10,5,-7,6,-7,-10,6,-7,-6,6,-2,3,3,10,1,-7,2,-9,-10,-2,-3,9,-10,2,3,-5,7,1,-4,-6,-2,-8,-6,3,1,-4,10,4,10,-4,-5,8,-9,-4,3,9,-4,10,-1,-7,-10,7,-4,8,8,-9,-2,-5,-5,5,-2,3,-1,-7,8,7,4,-6,6,6,-5,-8,-9,10,-3,-4,-1,-2,-2,9,2,-5,-1,-9,-4,-2,8,-6,5,3,-4,5,-5,-2,-6,4,6,-6,-10,-3,-10,3,-6,-6,-6,-9,7,-8,2,9,10,8,3,-2,-1,-7,-9,-10,9,6,-7,8,2,8,7,-4,1,2,5,8,8,-8,6,-3,-2,-2,7,-4,-7,5,-10,-10,10,-6,3,-3,-9,-9,-7,-2,3,-9,-6,-9,5,-7,-2,5,-9,7,5,5,10,-1,-6,7,10,10,-1,9,5,-3,2,-7,9,3,3,-9,9,10,-4,-7,-7,10,-5,5,4,-7,8,-7,7,10,-7,-4,9,-4,-3,7,5,9,6,-2,-4,7,2,-8,4,-10,8,-5,-8,-2,-9,2,-6,-8,4,1,10,9,-1,-2,6,-4,-3,-1,-10,-3,-2,7,-3,8,-6,5,-8,7,-1,4,8,-2,-1,-4,-8,1,10,-9,2,10,8,-1,2,-10,6,2,4,-9,-1,-5,9,-10,-4,4,8,-2,-1,-7,-3,-8,10,3,8,-8,-4,-9,-7,-4,9,6,3,-6,-3,9,-7,-2,-9,-1,-8,7,2,-7,-4,-1,-8,-2,5,5,-10,-3,-3,6,-2,10,-5,-4,-10,7,3,-9,-3,3,-7,-7,3,4,6,8,6,-10,3,-10,-6,-9,3,1,6,-7,2,-10,5,-1,-5,-9,-8,-3,-2,6,-8,-8,-2,8,-2,-3,-8,-9,10,-3,2,-5,10,3,-1,-1,-5,-9,-7,9,3,-4,-8,5,5,-2,-8,7,-4,-10,-9,-3,10,-5,2,-6,5,-5,5,10,6,4,10,-3,-2,-1,-6,7,-8,-4,-6,5,-2,-6,-10,4,-10,-1,-10,5,1,-2,10,-2,-4,1,7,-1,6,-6,6,2,8,6], dtype = "int32")#candidate|9336|(540,)|const|int32
call_9335 = func_4188_call(relay.reshape(const_9336.astype('int32'), [4, 15, 9]), relay.reshape(const_9336.astype('int32'), [4, 15, 9]), )
call_9337 = func_4188_call(relay.reshape(const_9336.astype('int32'), [4, 15, 9]), relay.reshape(const_9336.astype('int32'), [4, 15, 9]), )
func_1285_call = mod.get_global_var('func_1285')
func_1290_call = mutated_mod.get_global_var('func_1290')
var_9351 = relay.var("var_9351", dtype = "bool", shape = (1, 80))#candidate|9351|(1, 80)|var|bool
const_9352 = relay.const([False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True], dtype = "bool")#candidate|9352|(1200,)|const|bool
call_9350 = relay.TupleGetItem(func_1285_call(relay.reshape(var_9351.astype('bool'), [8, 10, 1]), relay.reshape(const_9352.astype('bool'), [8, 10, 15]), relay.reshape(const_9352.astype('bool'), [8, 10, 15]), ), 1)
call_9353 = relay.TupleGetItem(func_1290_call(relay.reshape(var_9351.astype('bool'), [8, 10, 1]), relay.reshape(const_9352.astype('bool'), [8, 10, 15]), relay.reshape(const_9352.astype('bool'), [8, 10, 15]), ), 1)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_9360 = func_4080_call()
call_9361 = func_4080_call()
output = relay.Tuple([call_9312,call_9335,const_9336,call_9350,var_9351,const_9352,call_9360,])
output2 = relay.Tuple([call_9313,call_9337,const_9336,call_9353,var_9351,const_9352,call_9361,])
func_9364 = relay.Function([var_9351,], output)
mod['func_9364'] = func_9364
mod = relay.transform.InferType()(mod)
var_9365 = relay.var("var_9365", dtype = "bool", shape = (1, 80))#candidate|9365|(1, 80)|var|bool
output = func_9364(var_9365)
func_9366 = relay.Function([var_9365], output)
mutated_mod['func_9366'] = func_9366
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9441 = relay.var("var_9441", dtype = "float32", shape = (9, 5, 14))#candidate|9441|(9, 5, 14)|var|float32
var_9442 = relay.var("var_9442", dtype = "float32", shape = (9, 5, 14))#candidate|9442|(9, 5, 14)|var|float32
bop_9443 = relay.subtract(var_9441.astype('float32'), relay.reshape(var_9442.astype('float32'), relay.shape_of(var_9441))) # shape=(9, 5, 14)
uop_9446 = relay.rsqrt(bop_9443.astype('float64')) # shape=(9, 5, 14)
output = uop_9446
output2 = uop_9446
func_9453 = relay.Function([var_9441,var_9442,], output)
mod['func_9453'] = func_9453
mod = relay.transform.InferType()(mod)
mutated_mod['func_9453'] = func_9453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9453_call = mutated_mod.get_global_var('func_9453')
var_9455 = relay.var("var_9455", dtype = "float32", shape = (9, 5, 14))#candidate|9455|(9, 5, 14)|var|float32
var_9456 = relay.var("var_9456", dtype = "float32", shape = (9, 5, 14))#candidate|9456|(9, 5, 14)|var|float32
call_9454 = func_9453_call(var_9455,var_9456,)
output = call_9454
func_9457 = relay.Function([var_9455,var_9456,], output)
mutated_mod['func_9457'] = func_9457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_9506 = func_2835_call()
call_9507 = func_2835_call()
func_6431_call = mod.get_global_var('func_6431')
func_6434_call = mutated_mod.get_global_var('func_6434')
var_9529 = relay.var("var_9529", dtype = "bool", shape = (80,))#candidate|9529|(80,)|var|bool
call_9528 = relay.TupleGetItem(func_6431_call(relay.reshape(var_9529.astype('bool'), [80,])), 3)
call_9530 = relay.TupleGetItem(func_6434_call(relay.reshape(var_9529.astype('bool'), [80,])), 3)
output = relay.Tuple([call_9506,call_9528,var_9529,])
output2 = relay.Tuple([call_9507,call_9530,var_9529,])
func_9531 = relay.Function([var_9529,], output)
mod['func_9531'] = func_9531
mod = relay.transform.InferType()(mod)
var_9532 = relay.var("var_9532", dtype = "bool", shape = (80,))#candidate|9532|(80,)|var|bool
output = func_9531(var_9532)
func_9533 = relay.Function([var_9532], output)
mutated_mod['func_9533'] = func_9533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mod.get_global_var('func_5272')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_9554 = relay.TupleGetItem(func_5272_call(), 0)
call_9555 = relay.TupleGetItem(func_5274_call(), 0)
output = call_9554
output2 = call_9555
func_9564 = relay.Function([], output)
mod['func_9564'] = func_9564
mod = relay.transform.InferType()(mod)
output = func_9564()
func_9565 = relay.Function([], output)
mutated_mod['func_9565'] = func_9565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_9572 = func_4144_call()
call_9573 = func_4144_call()
output = relay.Tuple([call_9572,])
output2 = relay.Tuple([call_9573,])
func_9586 = relay.Function([], output)
mod['func_9586'] = func_9586
mod = relay.transform.InferType()(mod)
mutated_mod['func_9586'] = func_9586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9586_call = mutated_mod.get_global_var('func_9586')
call_9587 = func_9586_call()
output = call_9587
func_9588 = relay.Function([], output)
mutated_mod['func_9588'] = func_9588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4824_call = mod.get_global_var('func_4824')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_9630 = relay.TupleGetItem(func_4824_call(), 0)
call_9631 = relay.TupleGetItem(func_4825_call(), 0)
func_7867_call = mod.get_global_var('func_7867')
func_7869_call = mutated_mod.get_global_var('func_7869')
call_9636 = relay.TupleGetItem(func_7867_call(), 2)
call_9637 = relay.TupleGetItem(func_7869_call(), 2)
func_1285_call = mod.get_global_var('func_1285')
func_1290_call = mutated_mod.get_global_var('func_1290')
const_9653 = relay.const([[False,True,True,True],[True,True,False,True],[True,False,True,False],[False,True,True,False],[False,True,False,False],[True,True,False,False],[False,True,True,False],[True,False,True,False],[True,True,True,False],[False,True,True,True],[True,False,True,True],[True,False,True,False],[True,True,False,True],[False,False,True,True],[True,False,True,False],[False,False,False,False],[True,False,False,True],[True,False,True,True],[False,False,False,False],[True,False,False,False]], dtype = "bool")#candidate|9653|(20, 4)|const|bool
var_9654 = relay.var("var_9654", dtype = "bool", shape = (1200,))#candidate|9654|(1200,)|var|bool
call_9652 = relay.TupleGetItem(func_1285_call(relay.reshape(const_9653.astype('bool'), [8, 10, 1]), relay.reshape(var_9654.astype('bool'), [8, 10, 15]), relay.reshape(var_9654.astype('bool'), [8, 10, 15]), ), 1)
call_9655 = relay.TupleGetItem(func_1290_call(relay.reshape(const_9653.astype('bool'), [8, 10, 1]), relay.reshape(var_9654.astype('bool'), [8, 10, 15]), relay.reshape(var_9654.astype('bool'), [8, 10, 15]), ), 1)
uop_9657 = relay.log2(call_9652.astype('float32')) # shape=(8, 10, 15)
uop_9659 = relay.log2(call_9655.astype('float32')) # shape=(8, 10, 15)
func_6077_call = mod.get_global_var('func_6077')
func_6080_call = mutated_mod.get_global_var('func_6080')
var_9661 = relay.var("var_9661", dtype = "float32", shape = (55, 6))#candidate|9661|(55, 6)|var|float32
call_9660 = relay.TupleGetItem(func_6077_call(relay.reshape(var_9661.astype('float32'), [330,])), 1)
call_9662 = relay.TupleGetItem(func_6080_call(relay.reshape(var_9661.astype('float32'), [330,])), 1)
output = relay.Tuple([call_9630,call_9636,const_9653,var_9654,uop_9657,call_9660,var_9661,])
output2 = relay.Tuple([call_9631,call_9637,const_9653,var_9654,uop_9659,call_9662,var_9661,])
func_9666 = relay.Function([var_9654,var_9661,], output)
mod['func_9666'] = func_9666
mod = relay.transform.InferType()(mod)
var_9667 = relay.var("var_9667", dtype = "bool", shape = (1200,))#candidate|9667|(1200,)|var|bool
var_9668 = relay.var("var_9668", dtype = "float32", shape = (55, 6))#candidate|9668|(55, 6)|var|float32
output = func_9666(var_9667,var_9668,)
func_9669 = relay.Function([var_9667,var_9668,], output)
mutated_mod['func_9669'] = func_9669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6115_call = mod.get_global_var('func_6115')
func_6116_call = mutated_mod.get_global_var('func_6116')
call_9709 = relay.TupleGetItem(func_6115_call(), 0)
call_9710 = relay.TupleGetItem(func_6116_call(), 0)
output = call_9709
output2 = call_9710
func_9719 = relay.Function([], output)
mod['func_9719'] = func_9719
mod = relay.transform.InferType()(mod)
output = func_9719()
func_9720 = relay.Function([], output)
mutated_mod['func_9720'] = func_9720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4475_call = mod.get_global_var('func_4475')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_9724 = func_4475_call()
call_9725 = func_4475_call()
func_3645_call = mod.get_global_var('func_3645')
func_3647_call = mutated_mod.get_global_var('func_3647')
call_9738 = relay.TupleGetItem(func_3645_call(), 0)
call_9739 = relay.TupleGetItem(func_3647_call(), 0)
bop_9745 = relay.floor_mod(call_9724.astype('float64'), relay.reshape(call_9738.astype('float64'), relay.shape_of(call_9724))) # shape=(1, 10, 11)
bop_9748 = relay.floor_mod(call_9725.astype('float64'), relay.reshape(call_9739.astype('float64'), relay.shape_of(call_9725))) # shape=(1, 10, 11)
func_7666_call = mod.get_global_var('func_7666')
func_7669_call = mutated_mod.get_global_var('func_7669')
const_9752 = relay.const([[5.433652,-4.384624,-0.059693,8.615683,-9.696696,-9.584204,5.204463,-4.744752,4.773310,-8.947612,-1.297144,-3.089089,-2.105822,6.951373,-0.576469,-4.061316,7.589331,7.495903,5.264640,-1.186083,3.248282,0.789745,-2.698366,-3.354643,5.574672,5.568649,-3.325126,3.299803,3.383682,2.692774,6.536379,4.375656,-6.886653,-5.461976,5.529711,-8.748452,-2.321226,-9.179230,5.581760,-5.380192,5.329395,-0.364365,4.519456,-5.594099,-6.835398,0.354468,6.072464,-0.408883,2.928345,0.339363,9.234949,7.428037,-9.028457,-5.319852,-2.349229,-5.172509,5.018533,-0.630485,-6.435159,9.187918,-0.833623,-3.802987,-7.280723,-3.338467,-4.258015,-2.793496,5.703561,0.673486,6.808322,3.291772,-4.968779,9.872903,-8.460698,9.633347,-6.884212,-2.909229,3.869821,4.847496,5.355132,1.743852,3.169048,-1.843079,4.988638,-8.330482,7.521945,-3.665260,7.857308,2.698129,8.913741,-6.459646,-2.026429,0.016060,-3.404326,4.367191,-9.242377,1.455896,-6.579391,-2.532895,7.312521,9.589763,-3.923761,-0.755843,9.805972,6.764790,-1.398057,7.719222,-4.102170,-9.131775,4.575365,1.000463,-5.517209,9.445222,-3.803296,-7.226332,1.490023,-5.246742,-8.538945,1.977875,1.829930,-8.813543,4.481739,-7.849303,-0.403843,-4.939850,-5.286665,6.541628,-9.824399,0.511188,-7.132891,-8.809091,4.582097,2.561428,7.732479,-1.762661,-8.983656,3.663306,-8.781380,7.689003,-6.752801,-3.219853,2.943119,-3.135412,-7.481877,-2.025598,0.068631,-6.619277,-0.968435,-7.505832,5.926125,-2.722728,-3.774195,8.448245,5.447786,9.737890,-3.480509,-6.952880,-7.836103,9.451334,-6.055964,4.578609,-2.583998,4.575475,-0.101267,-9.681913,-2.354071,0.833489,-8.768451,2.888058,1.939373,-8.151327,-2.890135,-1.490098,7.566199,7.479374,2.848116,7.734432,5.322802,-1.772249,0.006180,3.937577,2.543576,-1.314050,8.891032,5.502390,-3.432429,-3.847309,-6.585698,4.306481,-8.305459,-7.890374,-9.741551,1.214098,-2.604737,5.362406,-7.545268,0.375042,3.672533,-7.392255,6.360820,0.646481,1.826817,-3.329705,-4.279752,9.904146,-4.071796,2.064626,2.054683,-2.779880,-1.832008,3.247763,-2.679774,6.923511,-7.802183,-3.082189,0.780817,-3.878760,1.630951,9.463976,-5.678650,-6.099332,-3.589692,9.677932,-3.947479,6.468841,3.897003,-2.037014,1.183555,1.057573,2.708606,0.887529,-7.790985,6.528985,-3.025958,7.561394,4.803889,8.647792,2.683436,1.973682,1.128155,3.160462,-3.376611,-4.953518,7.385777,3.660874,-5.667724,4.062685,-1.219033,-2.109533,3.878982,-5.554004,-0.397811,-8.772957,-0.723875,0.687232,-7.448845,8.768597,-7.622807,-7.666384,6.045380,-2.763028,-0.605980,-0.028253,-0.622311,7.158348,7.396956,-5.913243,-7.324189,1.422575,0.557347,-8.043708,0.220144,-1.937036,3.166017,5.418248,-4.221977,-1.167335,-5.070680,-7.952481,-2.685862,-7.929909,8.032082,6.281163,-0.296435,-2.160893,8.547871,6.327889,-0.013830,3.826212,7.954697,3.662769,-6.639453,-5.387012,-2.868851,-9.610577,1.355288,-0.815050,2.764575,-3.631985,0.215777,5.853625,9.713264,1.147298,-8.832429,4.193718,-9.025467,-7.734219,8.521794,8.716523,0.998042,-7.351203,-6.317421,6.511446,-3.677805,5.550616,-7.926282,-1.105257,-1.293305,-0.936483,-5.329766,-3.942739,-2.790455,-1.582834,8.188041,3.436576,7.085721,4.770601,9.342480,0.405760,-7.065909,8.211894,-3.009440,-5.378184,4.763166,1.200093,3.325721,-5.474889,-8.922609,2.004411,-5.741441,-2.283260,-2.273215,-8.818988,-8.372752,9.524086,-6.674959,-6.606865,-8.001174,7.964433,9.188339,-2.725699,-7.777875,-1.954053,1.836709,4.222851,-6.361514,1.380836,4.938471,-3.372713,2.404168,3.411211,-7.177758,-9.541079,-6.960073,7.492680,3.942210,-5.788597,-0.044808,-6.810627,-4.306248,-9.492329,-1.956624,1.085950,8.058620,0.477115,5.791795,-6.090406,-6.686458,5.657147,3.194374,-1.862076,-7.406360,-7.762022,5.342801,-5.087045,-9.177096,1.585454,-9.963063,4.048052,-4.038722,-7.904038,9.241330,-5.392425,-5.637863,-6.162149,-9.344757,-1.055194,-8.448815,4.446511,6.424817,4.063569,-6.995319,-5.436376,-6.140343,-3.807934,7.525045,-2.793782,-9.460813,-2.742793,-8.453358,-6.473802,-9.677641,7.027324,8.690006,-1.521090,-6.297597,7.486634,-1.318184,5.228203,6.957620,-6.358137,6.016466,9.571254,7.084975,-3.158918,-1.854506,-1.451072,1.130095,3.955513,-2.131606,9.172490,-5.733004,-2.988415,6.319092,3.918671,2.186366,1.996993,-2.695750,-6.439345,-7.065614,-8.418110,4.426331,0.118707,-7.345774,-3.199169,3.708507,-7.070665,-5.302810,-2.473555,-4.671170,-7.529513,4.623929,-3.827229,-1.916505,1.822554,1.023965,0.419422,-7.378789,4.629098,-5.304141,-7.331172,-8.697153,5.817688,9.044628,-2.613955,3.650806,3.240972,-6.873002,-7.114199,6.277543,8.208140,5.819519,9.336873,-9.511263,1.395839,-1.137111,-4.772361,-7.306393,8.404355,7.395778,7.496580,-6.366359,-1.170759,4.844861,3.256464,-4.997299,5.435114,-1.402450,-3.589568,-5.265974,2.793012,4.065695,2.883715,3.246134,2.711306,-2.293816,0.605318,5.370279,6.059898,-4.146438,0.813137,1.616629,1.428788,-9.665703,-4.242312,9.722747,9.057824,8.138585,-1.910812,-4.099951,-3.308187,-3.568833,5.365810,7.085549,-3.662056,-0.430603,-1.327382,6.141959,2.229564,9.628770,-5.705705,8.123575,0.277056,-3.631920,3.957182,6.652406,2.718950,2.010258,-2.473801,5.662075,-7.865539,-8.313544,9.121383,-3.186961,1.864993,1.508797,-5.776666,-6.373359,7.506343,6.678015,4.423409,-2.266741,9.369503,0.387046,-8.703752,-2.386293,-7.176479,-4.961403,-1.603357,-3.776918,-5.012184,9.319530,-4.410068,9.686755,-1.372898,-8.163087,7.605658,-0.186946,-8.604424,-5.717013,-4.511329,-3.208075,-3.822011,2.520133,4.729603,-5.154286,4.596477,2.689305,6.345768,0.245367,7.543252,7.003405,1.657321,2.378334,-9.725260,-1.462814,4.390746,8.131999,5.493039,-8.244642,9.457460,5.047346,6.476998,-8.793605,5.782872,-0.883578,-2.488764,5.071403,-3.752921,5.229433,9.529012,1.086047,-7.089487,-4.923490,5.614221,6.782397,2.455794,0.144496,1.867572,-0.104886,-9.591466,4.811929,-2.159058,-3.471664,-6.684685,2.423657,8.501676,-6.147353,-9.280944,-9.399074,6.602943,-6.595558,-2.525443,3.873706,4.455507,-3.092749,9.494409,-3.176990,-0.792162,-1.593497,9.224686,-9.702756,-4.106343,-1.470684,5.395662,5.944143,-7.685681,-1.147528,6.553699,-6.653681,8.344416,-2.932262,8.724006,-1.179545,4.289151,-0.786853,9.785689,-8.900856,5.831927,-8.876586,6.897422,2.229096,8.315992,-9.643356,-1.948198,8.878412,8.519995,-4.175331,4.051864,-8.476265,7.715772,0.037491,-5.254576,-4.686237,-9.750585,-3.341308,-1.041410,-9.063632,8.548254,3.895164,4.632356,3.002734,-0.216298,6.088082,9.623132,1.994039,-7.139485,5.869428,-5.992893,-7.835950,-9.207204,-5.681334,7.246274,-6.547467,0.284724,-6.546833,-8.653983,7.645588,8.160891,-1.945321,-3.121407,3.429103,-1.666415,3.908683,-9.850349,-0.546155,0.772182,-2.484529,6.208154,3.202042,-7.137270,3.334287,-2.874983,8.945195,-1.707043,-2.231560,6.212780,5.789577,-2.447158,-2.307599,7.222760,0.797644,1.034856,1.787236,-5.519942,5.995392,-8.025737,4.108661,7.325757,-9.259192,8.009253,6.979871,-8.508930,-2.455563,6.987771,1.720942,4.302201,3.307604,-4.023503,2.252801,-5.086794,9.413267,-8.407136,3.473853,-3.479019,0.531910,-0.808700,-3.688705,5.573611,7.368726,-6.466018,0.432143,4.728105,-7.728098,6.568234,-0.160965,8.717907,-8.590904,-1.662991,1.092556,0.382151,-3.304043,5.833482,-9.981494,-7.218410,-3.320465,5.148438,-8.285045,-0.709094,-0.202098,5.395975,0.490293,0.927886,-6.296936,7.225530,-5.138026,-3.677269,-7.635905,4.129535,-3.492809,-9.712149,-0.870275,3.737812,-0.042591,-1.306863,9.801246,1.618336,-3.157522,0.094647,5.243744,-5.607323,9.237230,-7.965784,3.302247,6.650260,6.154900,-2.130140,3.695163,1.840208,5.536154,-1.871191]], dtype = "float64")#candidate|9752|(1, 780)|const|float64
const_9753 = relay.const([[True,True,False,False],[True,True,True,False],[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,True],[False,False,True,False],[False,False,True,True],[False,False,True,True],[True,True,True,True],[False,True,True,False],[False,True,False,False],[True,True,False,True],[True,True,False,False],[True,False,False,False],[False,True,True,False],[True,True,True,False],[False,True,False,False],[False,True,True,False],[False,True,True,False]], dtype = "bool")#candidate|9753|(20, 4)|const|bool
call_9751 = relay.TupleGetItem(func_7666_call(relay.reshape(const_9752.astype('float64'), [10, 78]), relay.reshape(const_9753.astype('bool'), [20, 4]), ), 3)
call_9754 = relay.TupleGetItem(func_7669_call(relay.reshape(const_9752.astype('float64'), [10, 78]), relay.reshape(const_9753.astype('bool'), [20, 4]), ), 3)
func_6715_call = mod.get_global_var('func_6715')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_9757 = relay.TupleGetItem(func_6715_call(), 2)
call_9758 = relay.TupleGetItem(func_6716_call(), 2)
output = relay.Tuple([bop_9745,call_9751,const_9752,const_9753,call_9757,])
output2 = relay.Tuple([bop_9748,call_9754,const_9752,const_9753,call_9758,])
func_9768 = relay.Function([], output)
mod['func_9768'] = func_9768
mod = relay.transform.InferType()(mod)
mutated_mod['func_9768'] = func_9768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9768_call = mutated_mod.get_global_var('func_9768')
call_9769 = func_9768_call()
output = call_9769
func_9770 = relay.Function([], output)
mutated_mod['func_9770'] = func_9770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3645_call = mod.get_global_var('func_3645')
func_3647_call = mutated_mod.get_global_var('func_3647')
call_9781 = relay.TupleGetItem(func_3645_call(), 0)
call_9782 = relay.TupleGetItem(func_3647_call(), 0)
output = relay.Tuple([call_9781,])
output2 = relay.Tuple([call_9782,])
func_9799 = relay.Function([], output)
mod['func_9799'] = func_9799
mod = relay.transform.InferType()(mod)
output = func_9799()
func_9800 = relay.Function([], output)
mutated_mod['func_9800'] = func_9800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8198_call = mod.get_global_var('func_8198')
func_8200_call = mutated_mod.get_global_var('func_8200')
call_9812 = relay.TupleGetItem(func_8198_call(), 0)
call_9813 = relay.TupleGetItem(func_8200_call(), 0)
func_3860_call = mod.get_global_var('func_3860')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_9823 = relay.TupleGetItem(func_3860_call(), 1)
call_9824 = relay.TupleGetItem(func_3861_call(), 1)
func_7401_call = mod.get_global_var('func_7401')
func_7403_call = mutated_mod.get_global_var('func_7403')
const_9827 = relay.const([-4.933923,-2.331333,6.627243,0.400899,-3.599093,-1.770555,0.052128,-1.337667,0.752384,-0.196718,8.303564,1.144555,-1.843103,-1.013483,-1.176093,9.285631,7.870009,-8.553423,-1.466839,-9.985797,3.620916,7.409767,9.487880,-0.185550,-1.118547,-9.611651,-8.380624,-0.387814,1.996847,-5.782335,-0.643050,-8.306582,6.376384,5.228758,-5.310941,0.962526,-6.947692,-4.038565,-4.717553,0.835414,-1.771625,7.845944,2.080390,5.759459,-2.460058,-2.926387,9.909517,0.877679,4.350411,-0.084704,-4.640202,3.045285,-9.329720,5.698055,7.968649,7.182624,-0.973784,-4.422349,8.092020,-5.691448,0.749246,-6.129569,6.404130,-4.120499,-7.880983,-1.819815,-6.650898,-0.785581,-8.789005,4.289295,-4.289451,7.996253,5.327275,-2.822844,7.671167,2.241144,0.541167,9.614491,1.668322,-9.999919,-8.115198,-8.372561,-9.031591,-9.612265,-1.253922,-0.570029,-3.231621,3.921848,2.019640,-6.149946,-0.221514,-2.926835,-1.820843,-8.654537,8.130103,1.017482,-8.158990,-3.697643,-9.964016,2.582937,-6.091837,9.561223,8.948645,9.894648,-0.824108,3.804198,8.622134,1.742655,3.110683,1.345659,-9.919299,-2.203497,-4.801615,5.624159,0.449060,-2.561731,7.144273,9.868778,-1.272962,2.587871,-7.927699,-8.223220,-3.491532,8.397048,6.302030,-3.750638,-4.208784,-0.540441,2.903566,0.229598,-1.730632,2.302866,-5.702168,-8.558629,0.535456,6.057878,-0.899864,1.919071,1.124888,-4.979985,0.524006,-9.689729,-5.687679,-4.876042,2.395082,-1.990431,8.721562,2.155662,-0.406500,9.504034,2.995347,-1.399001,-9.722627,5.783920,-5.427378,-7.271163,-7.044755,8.184621,-4.599642,2.023277,-0.889997,8.748821,5.951053,8.325508,2.046972,5.795114,6.668111,-7.347002,9.680255,-2.433934,-0.811190,8.434742,5.366005,8.432753,-3.958657,7.123807,-9.440547,6.856065,8.356861,-5.137893,1.126221,-9.636779,1.736377,-8.307976,-7.778844,-9.070577,0.922173,6.185842,5.472230,-3.756469,2.971614,-6.588681,5.350651,6.389462,-7.084406,2.299847,7.671017,-8.127643,-1.907440,8.651110,7.788483,0.529339,5.582056,-1.301967,8.811555,1.156964,-8.244863,7.312453,3.937996,8.106327,-5.742392,1.469514,-5.508680,-0.599385,-0.773139,6.459142,4.396168,-6.722235,7.664581,6.008079,-4.755760,-4.333288,-9.401919,-4.054561,-3.664578,9.103898,-2.028407,5.554673,6.224918,0.090504,0.034762,8.457913,-3.172104,-4.780010,-7.105391,-3.459178,-7.229191,-3.865941,-3.113321,-1.503130,-5.405572,6.449226,-2.223603,4.326504,-8.804261,6.870562,0.710863,0.801056,-3.245624,2.429602,3.483792,2.009318,-5.068944,8.709110,-4.455602,-3.759560,0.355943,9.416203,-7.333381,2.391403,-1.521452,-2.987835,-2.561138,6.146356,5.137119,5.133907,-7.653058,-5.559447,-0.831148,-2.165205,7.456044,9.818983,-4.637339,-9.647779,6.396010,-2.488491,-8.144624,9.017145,-2.406891,-0.125168,-0.958518,-1.958399,-1.611443,9.851234,-7.747613,-9.626309,-9.232982,3.400979,-0.195254,2.006695,3.878002,2.507391,0.176075,-1.495360,7.351357,2.459484,1.954499,9.685176,1.336347,-0.760342,-4.506423,8.811776,6.060362,8.718220,4.572968,3.174561,-3.650013,-3.284352,-6.293616,1.849591,6.434870,2.139540,6.134786,9.912757,3.986216,-8.883763,-9.629915,3.091757,-6.508320,2.340379,4.862135,7.135872,-0.381444,2.006811,-6.090596,-0.806255,-9.818848,-3.078818,-4.850029,-9.570127,-3.197232,4.077495,-3.490845,-4.866847,-0.846233,-1.219142,-4.246994,1.860607,-2.845846,6.244591,-6.642855,-6.926949,5.345144,-7.017486,-2.883759,-7.901523,0.770977,7.174884,-7.192314,5.075322,-6.995835,-9.183596,5.943590,6.472701,8.515949,-9.927885,-1.740298,-6.221704,-8.474884,-3.765098,8.787522,3.240963,-0.609624,-1.932060,-9.014625,6.884530,-6.877311,4.540573,-7.801077,9.787495,-9.477554,3.050347,-0.544624,-8.689875,-3.238241,-6.273261,7.538982,-3.112847,-8.968408,-7.907251,-1.307488,7.211529,-2.680095,-5.837095,3.193836,-7.448059,-2.157029,5.859972,8.035281,1.369814,-3.599483,9.737745,1.256183,7.342401,-5.872990,-1.274829,-8.236746,8.945728,-1.097477,3.645960,1.306843,4.512752,7.489943,2.675173,5.190808,-7.159960,-2.839103,8.858082,7.412812,5.495904,1.290694,0.060739,-4.516041,-8.306816,-0.967599,-6.108821,8.788184,5.870507,-9.572664,5.918311,4.854635,2.165739,8.075794,4.639655,-6.089571,-4.960658,-2.879821,5.021386,5.534851,-8.737549,8.561768,1.824523,-0.347847,5.088273,1.065975,-0.963625,-5.727828,-0.261561,4.412375,-3.743565,1.439208,3.134597,-2.876456,-5.994865,-0.181097,-7.549683,1.926833,-2.857730,-2.192422,0.298660,-9.904942,9.177352,2.522984,-3.412361,7.516237,-6.113226,8.329429,1.457240,-1.098632,4.486736,-6.662247,-4.075061,-8.095466,1.896508,-6.959410,-9.392645,0.614954,5.777540,-0.087512,8.424031,6.918762,-0.408790,9.981776,-5.135059,0.959842,-1.743910,6.651558,6.403267,1.473223,3.491509,2.805160,-8.000647,5.784384,-0.262058,6.459993,1.790920,4.662645,3.575313,8.795312,9.102237,-0.771191,-3.923624,-4.216706,6.064533,6.646260,-4.457162,-2.417565,3.193631,-5.138331,7.282841,5.269266,-6.164845,-3.176862,8.247936,-7.735380,-6.678811,-3.746322,-8.364122,4.006694,-8.574857,-2.864979,8.597123,1.973406,-4.959583,-1.899292,2.515989,0.872738,5.204263,0.196089,5.922064,9.784611,-1.875332,6.895662,-0.010000,-5.179957,7.460659,3.624693,-1.523386,7.408082,4.897443,-9.561507,5.988914,-9.552562,-5.905413,1.713839,5.135499,9.348118,-6.801761,6.792318,7.219528,6.057110,-0.972810,-7.474964,1.138353,-5.802152,3.892436,6.443476,-0.679960,9.057319,0.380210,-0.656152,3.321595,0.387148,-0.998499,1.035921,-6.332973,-1.489696,1.077320,3.566313,-5.383721,7.157480,9.968102,-3.600961,6.900717,-6.779502,-7.485021,4.653294,-4.518872,6.094513,2.027615,7.921287,1.424226,1.411995,-5.763766,4.066494,-0.361914,-2.879632,6.781705,9.034854,7.082233,-3.723868,-1.362549,4.446400,-6.870535,-3.843490,4.073368,5.363895,9.392855,-4.088147,-6.615764,9.310748,-8.245456,-9.907510,-9.156423,-3.502920,0.914210,-5.617069,5.906322,-2.560272,-4.062001,8.851369,-5.707938,7.635845,9.440077,4.216436,6.151109,-9.793111,2.552187,-6.164087,-0.838752,3.567757,9.470078,-9.542203,3.593351,-5.042623,5.992073,-3.992537,-6.465387,5.153251,9.213481,6.883059,7.381099,-5.501809,-6.224594,9.482648,-8.954251,-9.858383,-3.745118,-3.941805,-5.175135,1.255035,-0.655125,7.597714,3.255346,5.078719,-4.333920,-3.225371,-4.201899,-1.604293,1.586500,-9.117994,-7.669656,4.717507,0.167491,-9.983048,-8.740892,3.946142,5.093663,9.877281,6.399527,1.604577,-9.454381,-1.013057,2.265536,7.240434,-4.953053,-9.265892,9.185544,9.810201,1.292565,-1.960201,8.078424,-4.223588,-1.698910,-0.202381,-9.608520,0.731402,9.934121,-7.488290,-4.179948,9.656775,9.982476,7.573153,4.247983,0.592069,2.169862,-7.056609,1.825285,8.374571,-2.956401,9.726280,-9.827949,1.922510,-9.985232,-6.173811,-3.174603,4.009680,9.029648,-8.890492,2.939051,6.380527,0.408514,-6.383136,-4.025030,-3.047281,0.763794,-1.514192,0.684193,9.218829,3.758172,-5.269262,5.429944,5.486874,1.567403,0.221929,9.047937,3.394082,-6.909401,3.876277,8.030038,6.694007,1.803331,-5.985867,-4.288461,0.039404,2.403350,7.697100,6.385209,9.790151,-0.411479,-0.282509,4.982894,-9.092320,6.987058,0.456485,0.866195,7.621462,-4.948823,8.791707,0.997199,-0.305715,6.601315,5.456834,-3.395945,1.065380,4.121551,-3.836996,2.358220,-2.189007,-7.271835,2.226990,-2.334208,-8.753457,6.927361,6.801815,-8.129280,3.883581,5.603186,7.353259,-5.398953,-2.766291,-1.506263,-1.810479,1.273685,-2.067749,-6.011552,-3.366650,-5.724639,7.128603,-3.660080,-9.675043,-9.593044,-7.066052,-7.685643,0.312688,-0.087207,-5.148224,-4.900287,-0.345670,3.235408,3.040863,4.103055,-5.157881,4.555445,3.616158,1.163839,-8.518004,7.468610,5.316549,-1.301659,-3.145207,5.337466,1.749973,-8.558453,1.695488,-5.543124,0.277134,-7.548418,2.785133,-1.063817,-1.163112,-4.770031,1.282468,8.460982,9.888498,-7.750372,8.456680,-3.344531,7.913593,-5.326583,-3.811174,-0.006255,-4.215754,-6.315445,-4.414676,-5.901446,-1.877050,8.313255,0.287488,-0.675658,7.752587,-3.551031,-6.356340,2.394998,3.417987,8.305694,5.358771,-9.538329,-8.193676,5.186522,5.558133,9.150485,8.684404,6.542010,-1.331249,9.703142,-1.220711,-5.423683,9.230446,3.183549,1.185272,-1.097987,-4.404449,2.522678,9.528984,3.427081,-2.327053,-0.195062,4.045057,-9.479885,-0.007749,9.370053,-3.529956,3.305434,-5.061668,-8.236427,2.491565,-8.383171,8.468855,1.434166,-0.203191,3.276187,1.480842,-1.625431,-8.110461,-7.473390,7.901205,9.112775,2.579900,9.839488,6.693795,-3.493327,-7.088683,-8.739777,-8.154059,2.593323,-3.952533,6.054034,-4.327465,7.931599,2.898191,7.776884,9.350898,-6.478576,-3.979435,-3.701126,8.485250,-4.569656,0.225850,-6.848930,-5.778914,1.951465,-0.324366,7.324267,-7.333360,4.776840,-1.575285,-1.310192,-6.614743,5.454771,-3.304900,-3.889091,-5.068677,-7.231896,-2.240925,0.741201,-2.334882,0.941135,4.862324,0.313249,8.068836,6.429672,-0.054514,-9.810817,-6.810956,5.405900,9.750188,2.315101,-6.051320,-3.510059,-7.514904,-3.261565,-5.756560,7.752704,-1.960265,4.249699,-5.565834,0.437050,0.999832,1.510716,4.624847,-5.990332,-7.710202,-2.045837,1.351400,2.834933,-1.624951,-8.523277,-2.169661,4.298228,6.075618,-5.976659,4.258952,-4.957997,3.845756,3.312900,-8.885768,-6.597894,3.925737,5.574715,5.649882,-1.868436,-7.327491,-7.838315,-0.290108,6.265437,-5.157010,8.394102,-3.465406,-3.451456,1.170685,-1.515790,-1.873383,9.920311,-4.861893,-7.289908,0.853084,7.259741,-7.974852,-7.211869,9.614016,-8.065336,-7.955275,-6.748767,4.665550,-7.815232,-0.352412,-6.222499,7.116431,-2.957111,-8.600405,1.441498,6.056668,-5.884171,-6.489030,-1.057826,-1.328532,-4.621504,6.451455,2.303300,6.307935,0.287507,3.320010,-2.311779,8.539192,-7.233366,-3.427040,-6.882444,-4.811725,3.522181,1.158481,5.203703,-2.934563,-2.980626,-0.871458,-4.490148,-1.695400,6.282916,9.150867,-4.219266,-5.319233,-1.730125,2.182269,-5.082545,6.740502,-1.748484,4.018808,3.168758,3.334923,0.639780,3.187566,-9.915148,-0.675850,3.368783,6.406188,-7.857795,-1.899916,-1.998818,0.750152,-8.182149,-8.593140,-6.885126,-9.734026,7.598915,9.072653,7.358934,-3.756814,-3.124700,9.061482,-4.733356,-8.638360,-0.252592,-7.366194,-0.336992,1.880808,-1.474345,4.798490,2.536674,-0.917889,-7.117002,-1.459404,7.142332,0.651829,9.509210,8.989515,3.886841,-6.997327,6.838473,3.384453,4.621373,-8.446088,-3.023272,-6.983517,5.348837,8.302734,-1.733340,9.289775,-9.853733,-5.339898,1.352880,-9.911973,1.958009,-0.460840,8.804706,-1.414892,-5.681263,-3.522566,-2.208731,-2.595138,-5.451849,3.740631,2.205524,-3.606731,4.103076,1.852912,-0.739215,-6.651057,2.911104,-9.071925,-0.754488,0.695102,9.984327,0.296770,-0.294438,2.369805,6.293416,5.607610,8.236883,1.346175,-9.788368,4.029084,-3.812730,-9.299763,-9.557547,-7.114917,9.274409,8.038967,1.597046,1.306848,6.835256,-9.160307,6.662707,6.908043,6.507441,-2.249290,-7.544977,4.803782,4.772719,-5.191299,-4.282733,-8.177745,-6.344792,7.265559,-0.433346,3.770790,3.156340,9.194757,6.801963,-7.124648,9.377523,0.189258,-4.606659,-1.406688,-9.086796,-3.281065,0.474918,1.295181,-0.415824,3.966825,5.476037,-3.508872,8.354996,9.913489,6.520110,9.210803,-0.171006,-6.978296,0.816822,-6.489742,8.145800,2.561724,0.645182,-5.435225,4.056284,3.611135,-6.515360,7.711948,9.837614,-5.086224,-9.858584,7.117364,-9.094795,-3.867097,-3.876141,-7.868364,3.602972,-5.257866,-2.673116,-9.992703,-8.628130,-5.543073,-9.536521,-7.856728,-8.304595,-6.731496,1.507920,-7.514803,8.463589,5.280904,1.309878,9.911418,0.279574,-2.123607,-5.500253,1.224224,-3.117651,1.866189,-3.550143,-9.179476,-1.330501,6.881307,-0.386878,-8.906272,-5.123641,4.113524,6.603645,-1.723489,-9.652840,-1.848626,-7.590279,7.971882,9.248981,0.855502,2.769612,-1.235612,-5.329223,3.988427,5.341884,-8.439958,7.352452,-4.327216,-0.617767,-1.303508,2.391304,9.377717,-8.454775,-6.107320,9.420278,6.129195,7.483869,-0.197376,-1.666671,-2.896537,4.586510,3.280813,-5.166003,1.528577,3.867314,4.712503,-3.588751,-4.434320,9.575305,-2.988884,-3.172107,0.428654,-8.307474,2.289573,1.285391,-4.681379,-2.509376,-5.656685,5.829725,7.251869,1.416145,0.837355,3.195689,-2.794551,-5.589950,7.262179,7.894808,-4.074261,-4.377726,-1.773580,6.846007,8.066233,-8.818134,-9.618925,3.146061,-4.416477,-3.697333,6.891821,8.583418,3.453420,-1.207809,-6.935062,3.598875,9.025343,-5.435666,-9.113437,9.408523,7.857900,1.657640,1.222570,4.185454,1.661243,-2.352128,7.312135,-9.592545,7.090246,4.729664,-0.789111,2.240670,8.189310,3.626363,3.949152,2.726123,8.205798,2.212552,8.961420,-2.594819,-0.697507,9.590165,0.713256,-2.773565,9.594931,-4.474114,2.335820,9.132966,-8.689684,-8.438289,1.993606,-8.884136,-9.770292,-1.336019,7.760658,-0.532442,8.362474,4.685132,8.533837,3.376189,-7.616351,8.772505,7.525035,-3.474788,4.680534,-9.131612,-1.755260,1.423866,-3.753750,-0.281213,7.570967,8.706902,0.249322,6.351178,6.539495,4.593298,-6.085584,2.925389,2.425034,4.787761,-4.728099,-7.177905,8.784108,9.704875,8.340168,6.272866,-1.047160,0.244700,2.333325,-6.059997,3.665330,-0.105036,-0.367391,-0.943453,0.913369,1.287491,2.731984,-8.123069,8.597773,-8.623227,-0.479714,0.316207,-2.690656,-2.938961,0.530161,-9.720548,-8.920367,1.376781,-8.794989,-6.405446,9.099572,5.034327,9.729983,7.372851,6.584517,1.141600,3.873048,-5.660090,2.494987,-6.250417,-6.764311,-0.075377,3.546965,5.416682,9.016184,-7.003936,9.920385,4.459396,8.114347,-4.719360,-9.034510,-4.318568,-9.901951,6.307929,4.868652,4.676928,3.178320,-6.627044,7.174712,-2.280137,-2.328501,3.568044,5.693410,-6.165836,-0.774985,5.313712,5.413228,-4.825985,8.893412,0.147299,8.710179,-1.213307,-3.199106,-5.752098,-4.742843,-5.629531,2.778446,0.655805,-8.175697,7.222922,-6.600385,4.997383,7.622943,3.252938,-9.350173,3.124285,0.317880,-9.690960,4.407105,0.689554,5.766757,-0.455133,-2.456543,5.801252,9.037473,2.978847,-5.451604,0.302406,-8.496945,-1.225263,-4.079811,5.776094,6.294073,0.298076,-5.904422,-1.934022,3.617845,-3.193371,-0.352684,-4.995293,-6.880336,6.612052,0.241488,-1.655236,-3.075449,-1.470230,1.284892,-0.198542,1.006893,6.678377,4.197957,6.596040,-0.616401,-9.299659,-8.044890,-1.790908,-3.808953,3.628725,7.103602,3.295737,-0.718604,-3.057763,0.274194,-1.269789,-5.558784,-6.675530,5.994989,-0.856188,9.257325,5.757612,-3.735962,4.494150,1.174043,-9.389954,-1.422192,-1.207952,1.070387,-9.343909,-2.204357,3.569640,-4.292134,-5.901530,1.790414,2.998477,0.525937,-0.302896,8.450340,-9.590058,-0.879681,5.532772,-3.879592,1.060882,-3.779433,0.422058,-4.812158,9.191599,-4.746078,5.010677,1.208804,6.387388,0.703359,-4.028037,4.462230,8.097663,4.850768,-9.183839,5.557618,6.351340,-7.196935,-8.632633,5.987752,1.496900,9.546688,7.825558,-6.189371,1.293542,9.511343,-4.598295,-7.662929,-7.587418,-3.690743,5.361154,4.425434,7.271018,2.127542,-4.490937,3.023785,1.792592,-8.001893,1.877917,9.526769,-7.132129,-5.972565,2.110810,4.788924,-9.214371,-7.081666,6.945493,-3.269981,2.009366,-5.723558,-7.119318,-1.605213,-1.939045,1.721369,2.438770,-3.980264,3.039668,-4.576290,3.727863,-4.918238,6.913059,0.161485,-1.733280,6.830889,-3.523527,-4.833732,0.703447,-5.498842,4.946288,-1.462344,-5.750390,6.055098,8.076424,-8.832826,9.632498,0.943250,6.084899,9.430251,-7.354412,-7.625063,-6.591305,-1.387922,1.578805,9.061565,-2.404540,9.596736,-6.214528,-8.415409,-5.273970,-8.287734,3.859744,-9.573476,-0.202327,8.833370,-7.614133,9.808008,-2.087310,-3.359333,-0.419745,-5.637733,8.767013,8.792438,-8.771810,-6.420309,-2.403824,-0.765856,-0.905547,9.222209,-7.690904,3.581304,-5.001883,6.798907,-6.086462,-1.412373,9.138815,3.989143,-3.041813,-8.122720,-7.148897,2.216591,2.141277,8.984245,-7.330997,3.683864,4.900941,3.118392,1.543501,-5.883014,-7.997131,7.224254,3.840524,2.933878,4.155567,6.506853,-9.056206,2.840920,-2.322133,6.643905,0.986160,-8.684162,5.144029,-8.468535,-4.308890,0.559332,4.260652,9.504324,7.227478,-5.128423,-6.212689,8.619978,-4.426514,6.175629,6.913513,3.293842,5.237567,4.084761,0.537406,0.876080,-6.765758,-7.305038,2.549216,-8.759988,-1.399313,-9.603814,-6.869773,4.650106,-8.868700,-2.460968,2.478996,-4.275227,0.414369,-3.062954,2.352425,-7.983190,-7.458817,5.566517,-9.724685,-3.309694,-0.983385,-6.186846,-8.543525,9.054327,-3.841752,-7.962114,1.742637,-6.124596,-2.775433,5.749928,-2.531908,7.265645,-4.285399,2.709093,5.591595,-2.936235,-5.015060,-9.021100,-4.855433,5.998359,2.521315,8.094358,-7.136649,5.087408,-0.338973,-9.678376,8.092958,4.699791,-8.187009,-5.608292,-4.958768,0.151843,5.754139,-2.511752,7.309897,-0.113492,7.082328,8.267617,1.593080,8.624645,1.829688,3.560224,0.598009,-1.210027,2.766773,4.974246,0.008422,-1.291256,7.380941,7.930134,-5.830294,3.151362,5.479666,3.356994,-6.786747,-5.791042,-1.244562,-7.952634,-2.204010,6.484706,5.664488,5.085798,2.537787,-2.156942,-7.123209,7.273697,7.191840,9.769731,8.011994,-3.880028,0.278230,5.984779,-1.489694,8.369369,-6.306213,-6.835239,-7.134500,5.068509,3.512797,-0.587513,1.861451,-4.220013,-5.429883,7.929019,-7.646866,9.036555,-2.904993,2.483015,-2.059177,8.535142,6.088221,7.612408,9.996805,9.164136,-8.005811,5.089393,5.686740,-5.261687,9.841046,3.333991,0.605960,2.592184,6.269697,-4.893045,3.245387,-7.197849,6.699997,-4.187547,-0.181351,2.590770,8.111178,-7.471405,-9.936014,7.097768,-6.578824,6.350608,7.259050,4.300307,8.465918,8.774084,8.200435,2.057349,3.119715,-1.416108,7.425768,-9.071767,-6.491713,0.183667,7.685108,-1.323579,9.780840,-5.619687,-8.078876,2.188141,3.282047,-7.345938,0.019584,-7.652149,-4.638227,-5.383651,-5.797131,-8.815400,-4.922029,-6.769750,-3.901733,5.446391,-7.970925,3.908993,-7.677159,2.725303,4.804099,-2.939413,6.602042,9.752663,6.280855,-0.363290,-0.812138,-6.023179,-6.207739,-9.276117,6.842146,0.904963,2.959964,-7.475890,5.948680,-7.169917,-0.924777,4.384138,0.521171,3.434490,5.544131,-4.496837,-9.131073,-7.227341,6.414783,-9.408539,-7.950406,8.229883,-5.679405,2.583900,9.935317,-0.079917,3.311132,1.900940,-0.774334,5.324982,-8.431639,3.503722,4.387221,-5.389507,-1.982915,8.980301,-5.644073,1.557633,2.554731,-9.498119,-4.542453,-7.839876,3.744360,-5.559506,-9.875992,2.106473,0.041032,1.190330,-3.254142,-2.033296,-5.806691,0.874124,-6.891121,4.291319,-6.670146,-2.563758,-3.243061,-5.472859,-3.505957,8.662316,-4.526001,-0.094282,0.596321,-9.263433,4.016417,9.553542,6.266507,-5.474823,0.041567,3.603427,8.460472,-9.793558,-0.660159,1.893341,8.167719,3.725403,3.006775,2.991952,7.311135,-2.969531,-2.241349,1.491706,9.505980,9.284251,7.869097,-1.654360,-9.363841,4.593077,5.374781,-2.624615,2.711294,-4.529840,5.368260,-8.618980,-2.996149,8.833113,-7.051052,-7.122593,-1.135394,-7.398615,-4.231093,-6.347554,1.033474,9.833133,0.501390,4.518147,1.786547,1.480550,8.455804,7.436051,4.014491,1.436789,7.861154,3.368045,1.889539,-8.677052,-8.300217,3.653837,-8.350825,-3.630019,-0.515872,-0.227738,3.365643,-7.713056,6.075604,-0.363874,-7.971688,-3.532584,5.194018,7.722861,8.774828,-0.156273,-7.521042,5.745265,-4.644656,-8.990034,7.546338,-4.706904,0.168354,-5.523840,4.579390,0.537632,-6.933893,1.716396,5.083928,-9.223289,-7.034264,-7.993061,-8.704061,3.779164,2.915189,4.524629,5.755287,9.489346,-1.907937,0.235641,6.511800,9.456698,0.232618,2.649932,9.107734,1.606347,4.568554,6.564073,-5.678563,-5.924648,-5.284282,-4.343279,-7.987675,-7.631463,3.485758,-9.325077,-1.939525,-2.475811,-1.109145,-8.116625,-4.943143,-1.283570,5.413977,6.934581,-2.821291,7.267715,-1.435285,-0.081754,-1.638445,7.428143,2.444175,-0.594924,-4.026520,0.630894,-2.874114,-3.795212,3.486822,-7.719190,-7.263691,-3.971384,-0.576472,-2.313425,-3.815565,5.051970,1.456534,-2.840703,-4.567083,1.545958,-5.751576,9.535367,-2.121266,9.023576,-3.399862,1.426255,2.000588,-9.183723,1.057900,-6.807378,1.221128,-4.298620,7.305807,7.338335,2.179147,-1.675046,9.232047,7.138526,2.757685,-3.967874,-8.210011,3.913757,3.431382,8.125925,-6.619916,-9.887517,3.136291,-7.103109,-2.272563,-8.874558,-4.469401,8.344502,5.779019,-8.135544,9.533442,-6.597925,-9.722337,2.612384,9.075379,-5.081404,3.829068,-6.140332,-5.256584,8.531310,-3.587068,-7.154874,-2.909877,7.188444,-2.038195,-7.330318,-0.093876,-0.857558,-7.298141,-1.230418,-6.078825,2.757952,-6.790389,3.293655,8.250952,1.948340,-7.621202,-8.020798,5.880478,-9.244870,3.631925,5.386191,-4.024713,-2.583363,8.499323,-9.035399,-4.161185,5.463544,0.017917,8.786069,4.822726,5.982669,-3.576618,-2.596621,6.360693,-7.808368,-6.406352,-8.982334,8.420705,9.796444,6.921457,-1.773587,-4.764072,-3.319156,-5.563150,-8.615861,-4.482488,-8.429895,2.461580,-6.224977,7.289235,-2.779149,-8.478620,-6.047224,6.228571,2.309950,-4.925174,-9.385930,3.669188,-9.228991,-2.015361,-8.533652,-0.304477,-9.428814,1.270420,-4.603386,3.756034,-9.974029,9.445274,6.722319,9.287888,-4.374867,-7.183848,-8.538510,5.388611,-2.077462,6.230689,7.719096,9.689657,0.970970,-0.925885,2.087133,-6.639903,-0.164336,4.223506,4.799426,-4.304769,-2.941246,-6.364398,-3.899865,1.623893,-3.996716,1.411700,2.300880,8.818197,-2.409836,-2.222553,5.056013,3.662887,9.568178,4.921923,2.795938,-2.204411,-1.088544,-6.290690,-7.438666,0.756528,-9.311001,-5.467983,5.728151,2.351338,-4.829559,-7.621185,-2.102258,7.896856,-8.270719,-4.871741,-3.116546,5.663643,-6.363383,3.404681,4.166212,5.493616,-4.081905,4.134187,0.754302,2.625929,5.557931,2.224116,7.581812,1.232560,2.274058,-1.097044,-3.562612,-5.246562,0.682252,1.160388,5.792385,0.588043,2.951024,5.422179,4.507900,-9.758701,-2.970440,-9.766810,-5.388839,3.674672,-8.925893,2.859801,8.617516,7.374337,0.050095,-3.959193,5.495086,-3.973126,-2.283260,0.871231,-8.440277,-5.887928,3.962113,5.250621,-7.416133,3.572331,-2.419008,0.769775,-5.809211,-8.686684,-3.241081,-7.867723,-0.875811,-4.629746,5.295270,-0.493757,8.532867,-8.055780,-5.918831,-5.442277,2.979689,4.457658,-9.413012,4.624578,3.792233,-0.450238,-8.676749,4.042412,-2.603723,-1.720586,9.252693,2.473501,9.866810,6.686111,3.193530,1.495298,5.229890,-9.109920,7.308216,-6.814772,-6.010927,-8.624539,-6.137656,0.107845,0.272252,-8.353691,4.052851,0.277974,6.278616,-1.984095,-3.194002,7.431804,-9.725715,4.166226,-0.449314,-0.439508,8.863332,1.315476,-2.684960,-5.688315,-9.088967,-8.312333,-1.727791,5.846599,-9.763063,5.144847,2.094804,-0.062671,-6.039906,3.672023,5.737842,1.946420,5.758597,-5.699421,-5.986608,6.303804,3.493130,-2.604146,-6.691911,-2.421005,3.739466,8.401261,-4.172113,-2.706622,-1.990729,9.095474,5.246925,-9.524708,-3.236890,-9.893014,8.252342,1.417921,0.900613,-7.072182,6.442747,-1.646151,-4.107604,8.748888,2.142306,-0.994229,-4.459418,7.931808,-2.735592,-4.626623,1.390295,6.784055,-0.340720,3.101261,-6.191900,9.052288,-4.234637,-7.884261,-7.633359,-4.461003,6.156723,9.196012,-8.339877,7.171014,-6.839993,2.423720,-7.849866,-5.279032,-8.970702,-3.044795,8.129409,-9.238515,5.311173,3.837450,3.591828,4.188751,-3.112143,-3.977076,-4.068830,0.559841,1.138664,-8.141790,-8.078802,-9.002764,-8.167083,9.871980,5.523390,-2.106141,1.560478,-3.611910,2.139179,7.189088,-5.118043,-9.706432,-0.475514,5.369351,4.036997,1.955315,-5.627321,-6.610399,3.210525,-3.622384,7.308038,3.011134,-8.799913,7.193615,-5.696795,2.953693,-4.041052,9.774140,-0.509302,-4.388681,-5.019831,5.241189,-0.347838,9.877933,4.733753,-0.663774,-8.162928,7.546855,0.753583,-8.217746,-2.614307,-5.325898,-7.681608,5.104826,-0.853724,-3.758596,9.805580,0.359260,9.336979,0.147561,-9.493452,6.899736,-2.397203,-1.692548,-3.001541,1.967617,-6.624294,1.352782,4.926766,8.101164,7.381617,-5.600316,2.156258,-2.536124,-0.789286,-7.720611,9.496879,-4.251170,-5.751300,4.032115,8.449353,6.339268,-2.230643,-4.724836,7.220771,4.062484,9.261732,-7.163847,1.602144,0.772138,-6.782774,-8.411795,-8.952954,3.522098,2.401143,3.145612,7.892688,2.334824,8.409509,5.917150,2.603153,8.527613,-8.783055,-0.088004,-4.445834,-0.039391,4.911535,-0.338471,7.028560,-8.871482,-2.095668,9.272015,6.238797,7.503942,3.047127,2.727798,3.119810,4.534361,-6.248521,2.610606,-5.377119,-6.016070,8.386481,8.144100,-2.378115,2.333664,7.358183,5.456885,2.238912,8.465173,6.430843,-7.703032,-8.590441,8.438018,0.356643,4.538268,-3.374183,3.059507,3.487886,-6.574364,-3.038700,-4.253129,-3.059457,-9.352628,3.812163,-2.939021,1.585025,2.994291,2.252632,-5.396856,-2.214325,-7.281537,4.296688,-0.740627,-1.717916,6.221611,-2.149992,-3.881243,8.709684,2.481433,-5.951147,7.789155,-0.725948,1.304858,3.393027,-5.107083,-5.257598,-7.590702,-2.405288,-0.201270,1.855990,3.067010,1.708266,1.992327,5.881874,2.923416,-8.146082,9.450269,-7.152174,-0.432166,-6.262511,8.032557,3.821527,4.757373,-1.319590,-9.717067,7.474207,0.949591,6.258463,3.076815,4.669836,8.278203,1.943609,-4.286353,2.731616,-3.937230,4.251887,-3.875739,9.205337,-1.314938,9.249640,-4.827439,3.953712,-6.987693,-6.441596,4.434080,-2.498714,3.699266,1.321676,5.227468,9.986011,-6.791723,1.704416,8.493490,-1.380688,-3.913299,0.044214,-4.076399,8.813345,3.956116,-5.780358,6.634875,9.584722,0.613366,1.382829,-7.434668,-2.118428,6.192706,1.311597,-3.007374,6.863456,-9.973055,7.950233,8.266954,4.215002,-1.828043,4.578454,-5.792566,0.587466,6.383584,2.772671,6.241389,-9.772206,1.526340,3.091144,-8.590805,6.466811,4.898016,4.570865,7.232427,-2.120352,5.409165,9.097728,-0.477726,8.795693,1.885858,2.775727,-0.743155,-0.752460,-4.918308,6.368177,-0.541875,4.958614,-1.291657,-1.458759,4.929838,6.855794,-1.165970,-6.297194,5.359151,-8.621546,-8.614503,8.959797,0.745935,3.715593,-4.413719,-6.024057,9.512174,-6.205441,3.925794,6.000867,2.795434,4.892735,1.022637,8.193833,7.977236,-2.441959,5.606279,-5.859265,1.472136,-3.486388,-2.277854,-7.042646,-2.743028,7.422901,3.910680,-1.639708,-9.014020,-9.111327,-0.998206,-2.833239,8.104251,7.507615,9.511084,3.361427,8.355756,-5.681209,5.696044,9.064213,0.555054,3.158445,7.827605,-9.062111,1.413662,-7.877065,-7.469824,3.485440,8.921466,-6.069477,-9.496597,7.337027,-9.955161,6.467484,-3.955345,4.335714,-3.940113,-8.912020,4.443746,9.394439,3.869275,-9.445475,-9.753236,2.469978,-7.070771,-3.556988,8.944225,9.426217,4.710017,1.480361,1.205913,-2.266810,2.068392,-6.937138,4.570024,6.829809,1.970644,-2.710444,2.954821,7.596141,7.810549,-6.556510,8.710602,-6.251349,8.080292,-4.498567,3.607204,-5.025769,6.472886,6.857838,-6.061414,8.045240,-1.454322,5.018498,2.025625,8.569770,5.558444,4.895574,0.178146,6.210098,-1.197240,-8.568326,-0.934227,-7.993162,2.660714,-0.874678,3.130727,0.065473,7.601734,6.134224,2.770092,-2.012366,9.475064,1.046250,3.255585,7.766438,-7.991140,0.959778,-4.961072,-6.455937,5.089167,6.354425,-1.854079,-6.000736,2.954217,-2.074128,6.051817,1.159859,-3.966514,0.055284,-7.904104,3.256389,-5.915944,0.600843,2.536378,-0.400433,6.221056,8.180744,-0.845840,1.894008,5.821151,-5.783243,-4.677306,2.737741,-4.564881,2.203059,1.707065,7.057641,2.654348,-8.950944,-5.656288,-5.904233,-0.059138,5.546812,7.884850,7.727892,-6.785606,0.100732,2.736579,-5.521926,-4.226697,-0.360248,-9.406711,7.978017,4.068959,-5.101595,4.960294,6.835326,-9.555215,-0.251135,0.044913,4.131619,-5.307966,9.277143,9.928957,7.058384,1.433065,-1.474741,-8.478351,6.108327,4.976232,9.234552,-1.658483,4.511550,-7.489249,1.231537,3.077513,6.983238,1.194121,5.978938,-3.931588,-3.265745,8.163472,-7.226232,2.033419,0.265728,0.197446,8.155551,1.937207,8.392976,-0.198712,2.860950,2.271030,1.517016,2.469141,3.751429,-7.395387,2.992542,-1.752828,1.849580,-1.482839,4.205449,0.266607,2.142173,3.911271,-9.060570,8.141893,4.051166,0.383280,-9.415220,3.983190,-0.038405,8.976652,2.368052,3.223638,8.227174,2.009435,-2.158469,7.452704,3.557588,-1.971459,5.807549,-1.392786,-5.047814,0.469457,-8.892101,-1.503257,-8.613865,8.379059,-7.365900,-2.366132,-6.110879,-6.938854,6.028648,-3.259115,-0.164131,-4.023138,6.458860,-9.511980,-9.861004,-1.442670,-2.762865,-2.447234,-9.525050,5.557148,-0.889664,1.687524,4.509082,9.573974,8.242505,-3.463473,-6.015587,8.805502,8.922917,5.530995,-0.051760,-8.470877,4.729538,1.767565,-1.176101,-6.464847,9.433956,8.930615,7.430819,4.393299,1.980685,-1.954791,-9.916589,2.180788,6.362465,-7.163332,-4.479877,-5.335538,6.470418,6.729644,-2.799818,-4.131300,4.564108,8.131472,9.409116,-0.053452,-2.801874,-7.502832,-7.100464,-1.058764,5.747107,6.590163,9.550518,6.324247,-8.513488,2.752767,-6.715873,-5.981579,0.042552,-6.789596,-8.455710,6.770189,4.371458,2.591655,2.933805,0.593641,-9.832659,-9.838260,-2.512818,-1.548588,3.595414,-3.590664,-4.894603,4.381838,-0.503403,-7.165779,-3.973024,0.970852,0.932610,-4.094741,-6.274510,4.214633,-1.482658,-2.637586,6.813743,8.161797,-7.018792,-9.060626,-0.021190,0.142166,0.571772,1.859090,7.443774,4.565812,-6.432523,-0.882247,3.275495,5.949962,3.084741,0.500603,2.943927,9.283455,-4.100170,-5.496586,-9.316203,8.029987,8.993956,3.778107,0.601817,4.359526,-2.997645,-3.611394,-5.650742,-2.070431,6.278018,-9.001972,-4.289710,6.207891,-4.726756,-9.410853,8.841515,-5.930571,-7.880623,8.045214,6.855118,5.606447,-6.505304,8.003168,-2.525003,4.628140,5.213861,-8.559166,5.957159,-7.684921,6.888192,-2.114665,-9.818025,5.118783,7.659830,-6.893860,4.495665,-5.889193,5.318755,-5.698151,1.780910,-5.050292,-8.784893,5.411119,-9.195644,7.887887,-7.350303,-3.125132,-2.055989,3.311452,-7.451662,-2.246372,-2.813307,-2.418825,1.590030,8.152486,-2.933490,1.327463,-0.118612,-2.227337,9.392744,-0.863195,-7.781939,-2.989521,-2.395362,-3.644751,-7.498970,-8.029775,3.086045,-5.755425,-5.561303,-4.803764,2.767800,6.189353,-6.592834,-0.009505,8.713435,2.251944,4.108389,-5.227470,8.492371,7.299839,-9.535076,-4.324032,-4.102293,-3.727275,-4.314452,7.672932,-8.587797,7.643374,-0.445439,-5.435280,-5.166260,4.790313,-4.392246,4.812717,-9.275799,0.360695,5.475899,3.832083,-9.350938,-2.988035,-9.702356,3.091040,-0.332384,3.339348,-6.638836,-4.842164], dtype = "float32")#candidate|9827|(3072,)|const|float32
call_9826 = func_7401_call(relay.reshape(const_9827.astype('float32'), [12, 16, 16]))
call_9828 = func_7401_call(relay.reshape(const_9827.astype('float32'), [12, 16, 16]))
output = relay.Tuple([call_9812,call_9823,call_9826,const_9827,])
output2 = relay.Tuple([call_9813,call_9824,call_9828,const_9827,])
func_9839 = relay.Function([], output)
mod['func_9839'] = func_9839
mod = relay.transform.InferType()(mod)
output = func_9839()
func_9840 = relay.Function([], output)
mutated_mod['func_9840'] = func_9840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_9867 = func_3152_call()
call_9868 = func_3152_call()
output = call_9867
output2 = call_9868
func_9883 = relay.Function([], output)
mod['func_9883'] = func_9883
mod = relay.transform.InferType()(mod)
mutated_mod['func_9883'] = func_9883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9883_call = mutated_mod.get_global_var('func_9883')
call_9884 = func_9883_call()
output = call_9884
func_9885 = relay.Function([], output)
mutated_mod['func_9885'] = func_9885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8984_call = mod.get_global_var('func_8984')
func_8986_call = mutated_mod.get_global_var('func_8986')
call_9912 = relay.TupleGetItem(func_8984_call(), 0)
call_9913 = relay.TupleGetItem(func_8986_call(), 0)
output = call_9912
output2 = call_9913
func_9920 = relay.Function([], output)
mod['func_9920'] = func_9920
mod = relay.transform.InferType()(mod)
output = func_9920()
func_9921 = relay.Function([], output)
mutated_mod['func_9921'] = func_9921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3711_call = mod.get_global_var('func_3711')
func_3712_call = mutated_mod.get_global_var('func_3712')
call_9926 = func_3711_call()
call_9927 = func_3711_call()
func_8478_call = mod.get_global_var('func_8478')
func_8479_call = mutated_mod.get_global_var('func_8479')
call_9932 = relay.TupleGetItem(func_8478_call(), 5)
call_9933 = relay.TupleGetItem(func_8479_call(), 5)
bop_9934 = relay.power(call_9926.astype('float32'), relay.reshape(call_9932.astype('float32'), relay.shape_of(call_9926))) # shape=(1, 10, 11)
bop_9937 = relay.power(call_9927.astype('float32'), relay.reshape(call_9933.astype('float32'), relay.shape_of(call_9927))) # shape=(1, 10, 11)
func_2758_call = mod.get_global_var('func_2758')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_9968 = func_2758_call()
call_9969 = func_2758_call()
func_3645_call = mod.get_global_var('func_3645')
func_3647_call = mutated_mod.get_global_var('func_3647')
call_9985 = relay.TupleGetItem(func_3645_call(), 0)
call_9986 = relay.TupleGetItem(func_3647_call(), 0)
func_7539_call = mod.get_global_var('func_7539')
func_7542_call = mutated_mod.get_global_var('func_7542')
const_9990 = relay.const([False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True], dtype = "bool")#candidate|9990|(80,)|const|bool
call_9989 = relay.TupleGetItem(func_7539_call(relay.reshape(const_9990.astype('bool'), [80,])), 3)
call_9991 = relay.TupleGetItem(func_7542_call(relay.reshape(const_9990.astype('bool'), [80,])), 3)
func_5085_call = mod.get_global_var('func_5085')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_10006 = relay.TupleGetItem(func_5085_call(), 0)
call_10007 = relay.TupleGetItem(func_5087_call(), 0)
func_8198_call = mod.get_global_var('func_8198')
func_8200_call = mutated_mod.get_global_var('func_8200')
call_10016 = relay.TupleGetItem(func_8198_call(), 1)
call_10017 = relay.TupleGetItem(func_8200_call(), 1)
func_2168_call = mod.get_global_var('func_2168')
func_2170_call = mutated_mod.get_global_var('func_2170')
call_10044 = func_2168_call()
call_10045 = func_2168_call()
func_5414_call = mod.get_global_var('func_5414')
func_5416_call = mutated_mod.get_global_var('func_5416')
call_10046 = func_5414_call()
call_10047 = func_5414_call()
func_4242_call = mod.get_global_var('func_4242')
func_4246_call = mutated_mod.get_global_var('func_4246')
const_10053 = relay.const([-7.431603,-9.713129,-7.663878,-9.796972,-1.491687,-0.663836,-2.377118,-7.858701,-6.598242,-9.527870,0.889221,-8.684357,-9.924033,5.389164,4.002132,9.622689,-4.749460,-7.138576,7.271956,-2.978391,0.124948,-6.049120,-2.541062,3.632370,3.964395,-5.709451,7.892006,-3.799719,9.977047,9.112983,-4.431050,6.390454,-3.721881,-8.995185,-6.676232,-8.943011,8.853769,-7.070372,2.312135,5.800574,2.780400,8.597380,-5.277428,4.112430,6.336132,-8.754245,4.771933,-2.634850,8.206749,-4.381928,9.487138,8.814280,7.928715,-1.692054,-4.979807,-2.094842,-6.377009,-3.764886,3.215740,-1.136984,-9.783501,5.680591,-1.152217,-8.032020,-2.019333,-7.865843,2.510220,-7.777773,7.868517,5.744685,-6.863757,4.130857,3.586631,0.746173,6.751407,-0.730687,0.538216,-7.397859,1.477998,8.608704,4.809090,-3.312458,-6.869847,7.287578,5.188058,8.096683,-5.824024,-9.102748,-6.171094,7.947633,-6.306504,2.638911,3.569423,7.332050,-2.833205,-3.069052,-0.384906,-7.974879,8.390135,-2.573696,-4.616225,1.800745,7.078113,2.726759,8.912252,2.647392,-2.805886,4.521148,-8.743628,-1.378324,-6.047680,-8.915720,4.786358,0.922606,9.878855,-6.852231,4.216506,-3.935570,6.593531,-3.982630,-0.334121,-2.796092,-6.896707,-9.401712,6.087394,-9.888371,6.691870,-2.905101,1.128082,-6.679327,-2.250089,8.974495,-7.028937,-7.052576,3.053397,-9.554806,-6.989424,-5.814335,6.020914,-2.845664,7.593190,-8.204797,2.813206,-0.303211,-5.155432,4.381182,4.225705,-5.075634,3.814340,1.212659,4.690380,-2.122463,0.331308,-1.381770,-3.354148,6.484876,9.203234,-5.593871,-6.691903,-4.870478,9.929675,3.474051,-7.385132,-4.398150,-5.940017,-1.046863,-0.111724,-3.714627,5.903790,-2.415758,5.438053,3.963348,2.578327,6.619306,-7.452215,-8.759814,-9.475152,-1.949558,5.427647,-4.674279,8.238109,5.407677,9.759548,5.874075,-8.012883,-8.063944,0.567105,1.665052,-0.860059,-4.586917,-7.136586,-7.347967,2.114112,8.665167,-2.857590,-3.838338,-3.771045,0.666755,9.652044,-3.322546,-6.624454,4.260920,-1.242624,-1.438113,-7.657993,-9.251894,0.987293,3.751823,8.173168,4.463880,-3.453115,0.928368,0.652638,-6.777706,3.356442,-2.936406,-9.614474,1.979021,-1.522523,0.344730,3.257975,3.169980,-8.009591,8.729645,0.735098,1.875198,-5.931558,-5.692057,0.265252,7.449297,6.990091,-4.027669,2.887182,5.855229,0.476648,-4.803313,-6.013904,4.586721,-4.577074,-9.615504,0.999835,3.671393,3.516439,7.690563,9.751508,6.729709,3.966937,-5.676926,-1.261060,-2.003617,-8.608943,-9.680796,5.095699,0.949382,-4.150605,5.382391,-7.232974,7.061545,5.288477,-9.620865,5.414636,2.839885,-4.109819,-3.521160,5.946346,-2.913785,6.934151,-7.628816,1.053243,8.865964,-1.914006,2.098852,0.795927,-9.218523,-7.254374,1.076896,-0.811389,-4.851720,-6.474574,7.730217,7.269728,3.303639,-6.507581,6.503435,-0.067203,8.599729,-2.025586,2.157818,-1.136897,-5.415703,-1.345750,-9.501211,-0.608295,0.868006,0.819638,7.356229,5.762711,-8.797122,-4.733396,2.925350,-5.947469,0.463628,8.529759,-3.277989,-6.385517,-5.691375,4.701171,-4.149913,9.581866,-8.691657,-0.873545,-8.816387,3.240253,-7.100088,-5.311262,-4.579179,-4.530840,0.366476,-2.982479,0.678226,-8.487008,4.134053,8.189335,-6.912211,-6.954815,3.015891,-2.071272,-5.840708,-4.842863,0.093526,-9.894040,5.971324,-5.313356,-8.080900,8.253211,9.337641,-8.759898,8.472485,-0.842883,-4.894322,-7.578656,-8.152968,5.093331,-3.412359,1.154110,2.412950,0.567792,-1.540403,7.911299,-7.369148,5.662525,5.274449,7.135149,2.963352,-8.254583,-6.577349,6.981395,5.850104,7.013251,2.481214,0.444385,-6.619848,1.448673,-1.758721,6.866958,6.619787,7.746404,-5.975465,5.951981,-2.963011,-0.840886,6.981600,0.779730,-3.691890,-6.751357,6.271557,-5.161735,6.236942,0.172507,6.201188,-4.356698,7.850947,1.632606,-4.050500,2.572270,-8.910897,0.177941,3.793596,-4.912836,5.546458,5.378865,-8.115925,-0.603455,-0.865993,-3.763346,0.196316,-8.545548,-7.274833,-9.998664,9.632331,2.691970,6.154072,8.451057,-0.714561,6.985722,-1.076210,-0.660099,-8.568777,-2.007360,-3.346627,-1.519650,-8.396187,-8.805675,-8.828005,5.362075,-9.048573,6.437983,-5.772936,1.602383,-2.814835,-6.163681,6.623611,-5.929840,-2.584754,-6.112136,6.224472,-1.150696,-9.544109,-7.764429,8.452009,-6.448805,-9.390641,-1.655533,-0.292973,2.029678,-4.440385,2.610537,8.225271,0.602794,5.995278,-2.143683,0.463663,-4.065927,-8.795436,-6.737734,-7.617226,0.385125,3.083906,0.331439,8.326546,-1.673698,0.370735,-9.040747,9.361731,-5.018049,4.396279,2.927294,7.769408,-4.078274,-1.769973,2.666764,8.770241,-0.464593,-0.889823,-8.923022,-2.548381,2.206454,5.385592,-7.199625,-9.042424,2.461734,-1.305457,-9.607263,-2.914691,9.916270,1.037586,5.056541,3.967388,3.225019,-3.365682,-2.802985,7.138003,-4.562155,4.027627,3.834557,5.515136,0.322154,-2.367376,9.032674,0.622760,4.903346,1.930896,2.377638,-2.270735,4.120268,6.431952,-5.281705,4.366071,1.317550,7.648590,-1.337451,3.127248,-2.252356,7.463654,-8.205584,-3.005534,-8.075792,-9.301992,5.028373,-0.904778,1.260763,-7.609715,-1.723413,-2.448829,-9.738768,9.439672,-0.588137,-5.402521,-8.126208,-2.967744,-4.001560,-6.279206,6.582607,3.048095,-6.759273,7.070251,0.256470,5.268655,2.877303,5.642771,0.191807,4.799813,3.364696,0.606644,8.115736,-2.087736,-5.413546,-9.523161,2.097672,-5.370775,-8.288110,-1.344867,4.351892,8.122031,4.574976,-7.433205,4.609123,9.493991,-7.581915,-7.323252,-2.400546,5.689286,-1.657412,-5.851141,4.329290,2.120624,-7.937659,7.872846,2.228705,8.706932,5.173827,5.555208,0.027704,5.015608,5.255250,8.844016,-7.752013,6.082318,5.767886,1.082628,-7.516686,-8.284356,-3.688166,0.420230,-0.638600,-2.497923,-6.047823,4.613117,-0.876081,2.984546,-5.553318,-2.527318,-5.045197,4.423005,1.992304,-3.537354,1.764395,8.605927,0.434239,1.882161,3.350120,7.902164,-0.519813,6.651213,-0.330774,-2.882511,1.941927,5.946061,-4.138631,8.691283,0.851866,-7.651661,-1.313264,-9.709193,-9.415869,-2.335355,-9.851823,6.010670,-7.806700,8.966361,-1.321066,4.999617,-1.882665,9.880431,-2.178299,2.755324,-6.764016,-7.336065,1.709485,-2.839379,2.737898,2.938928,3.792948,-1.061149,9.995569,-9.988196,7.436899,0.337263,-6.652761,4.339736,-3.390892,6.544548,-4.972865,8.233616,-4.509913,1.180606,-0.379186,1.363962,5.312958,1.092664,-4.966029,-0.570344,-2.332093,5.224519,-2.495898,4.973961,6.996339,-5.868904,-1.002119,0.664728,9.108574,-8.850003,8.024309,3.438946,7.137077,5.576080,-4.050341,-6.758772,-2.868556,-1.177282], dtype = "float32")#candidate|10053|(660,)|const|float32
call_10052 = relay.TupleGetItem(func_4242_call(relay.reshape(call_10046.astype('float64'), [780,]), relay.reshape(const_10053.astype('float32'), [660,]), ), 0)
call_10054 = relay.TupleGetItem(func_4246_call(relay.reshape(call_10046.astype('float64'), [780,]), relay.reshape(const_10053.astype('float32'), [660,]), ), 0)
output = relay.Tuple([bop_9934,call_9968,call_9985,call_9989,const_9990,call_10006,call_10016,call_10044,call_10046,call_10052,const_10053,])
output2 = relay.Tuple([bop_9937,call_9969,call_9986,call_9991,const_9990,call_10007,call_10017,call_10045,call_10047,call_10054,const_10053,])
func_10066 = relay.Function([], output)
mod['func_10066'] = func_10066
mod = relay.transform.InferType()(mod)
mutated_mod['func_10066'] = func_10066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10066_call = mutated_mod.get_global_var('func_10066')
call_10067 = func_10066_call()
output = call_10067
func_10068 = relay.Function([], output)
mutated_mod['func_10068'] = func_10068
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10086 = relay.var("var_10086", dtype = "uint64", shape = (14, 4, 12))#candidate|10086|(14, 4, 12)|var|uint64
var_10087 = relay.var("var_10087", dtype = "uint64", shape = (14, 4, 12))#candidate|10087|(14, 4, 12)|var|uint64
bop_10088 = relay.bitwise_and(var_10086.astype('uint64'), relay.reshape(var_10087.astype('uint64'), relay.shape_of(var_10086))) # shape=(14, 4, 12)
output = relay.Tuple([bop_10088,])
output2 = relay.Tuple([bop_10088,])
func_10092 = relay.Function([var_10086,var_10087,], output)
mod['func_10092'] = func_10092
mod = relay.transform.InferType()(mod)
mutated_mod['func_10092'] = func_10092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10092_call = mutated_mod.get_global_var('func_10092')
var_10094 = relay.var("var_10094", dtype = "uint64", shape = (14, 4, 12))#candidate|10094|(14, 4, 12)|var|uint64
var_10095 = relay.var("var_10095", dtype = "uint64", shape = (14, 4, 12))#candidate|10095|(14, 4, 12)|var|uint64
call_10093 = func_10092_call(var_10094,var_10095,)
output = call_10093
func_10096 = relay.Function([var_10094,var_10095,], output)
mutated_mod['func_10096'] = func_10096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6729_call = mod.get_global_var('func_6729')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_10098 = relay.TupleGetItem(func_6729_call(), 0)
call_10099 = relay.TupleGetItem(func_6730_call(), 0)
output = call_10098
output2 = call_10099
func_10113 = relay.Function([], output)
mod['func_10113'] = func_10113
mod = relay.transform.InferType()(mod)
output = func_10113()
func_10114 = relay.Function([], output)
mutated_mod['func_10114'] = func_10114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3743_call = mod.get_global_var('func_3743')
func_3745_call = mutated_mod.get_global_var('func_3745')
call_10140 = relay.TupleGetItem(func_3743_call(), 2)
call_10141 = relay.TupleGetItem(func_3745_call(), 2)
func_7286_call = mod.get_global_var('func_7286')
func_7288_call = mutated_mod.get_global_var('func_7288')
call_10142 = relay.TupleGetItem(func_7286_call(), 0)
call_10143 = relay.TupleGetItem(func_7288_call(), 0)
var_10150 = relay.var("var_10150", dtype = "float64", shape = (780,))#candidate|10150|(780,)|var|float64
bop_10151 = relay.divide(call_10140.astype('float64'), relay.reshape(var_10150.astype('float64'), relay.shape_of(call_10140))) # shape=(780,)
bop_10154 = relay.divide(call_10141.astype('float64'), relay.reshape(var_10150.astype('float64'), relay.shape_of(call_10141))) # shape=(780,)
func_4788_call = mod.get_global_var('func_4788')
func_4791_call = mutated_mod.get_global_var('func_4791')
call_10158 = relay.TupleGetItem(func_4788_call(relay.reshape(call_10140.astype('float64'), [10, 78])), 0)
call_10159 = relay.TupleGetItem(func_4791_call(relay.reshape(call_10140.astype('float64'), [10, 78])), 0)
output = relay.Tuple([call_10142,bop_10151,call_10158,])
output2 = relay.Tuple([call_10143,bop_10154,call_10159,])
func_10172 = relay.Function([var_10150,], output)
mod['func_10172'] = func_10172
mod = relay.transform.InferType()(mod)
mutated_mod['func_10172'] = func_10172
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10173 = relay.var("var_10173", dtype = "float64", shape = (780,))#candidate|10173|(780,)|var|float64
func_10172_call = mutated_mod.get_global_var('func_10172')
call_10174 = func_10172_call(var_10173)
output = call_10174
func_10175 = relay.Function([var_10173], output)
mutated_mod['func_10175'] = func_10175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8984_call = mod.get_global_var('func_8984')
func_8986_call = mutated_mod.get_global_var('func_8986')
call_10177 = relay.TupleGetItem(func_8984_call(), 0)
call_10178 = relay.TupleGetItem(func_8986_call(), 0)
output = call_10177
output2 = call_10178
func_10210 = relay.Function([], output)
mod['func_10210'] = func_10210
mod = relay.transform.InferType()(mod)
mutated_mod['func_10210'] = func_10210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10210_call = mutated_mod.get_global_var('func_10210')
call_10211 = func_10210_call()
output = call_10211
func_10212 = relay.Function([], output)
mutated_mod['func_10212'] = func_10212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_10264 = func_4080_call()
call_10265 = func_4080_call()
output = call_10264
output2 = call_10265
func_10268 = relay.Function([], output)
mod['func_10268'] = func_10268
mod = relay.transform.InferType()(mod)
output = func_10268()
func_10269 = relay.Function([], output)
mutated_mod['func_10269'] = func_10269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_10272 = relay.TupleGetItem(func_3161_call(), 0)
call_10273 = relay.TupleGetItem(func_3162_call(), 0)
func_3086_call = mod.get_global_var('func_3086')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_10275 = relay.TupleGetItem(func_3086_call(), 2)
call_10276 = relay.TupleGetItem(func_3087_call(), 2)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_10277 = relay.TupleGetItem(func_6224_call(), 0)
call_10278 = relay.TupleGetItem(func_6226_call(), 0)
bop_10279 = relay.less_equal(call_10277.astype('bool'), relay.reshape(call_10272.astype('bool'), relay.shape_of(call_10277))) # shape=(1, 10, 11)
bop_10282 = relay.less_equal(call_10278.astype('bool'), relay.reshape(call_10273.astype('bool'), relay.shape_of(call_10278))) # shape=(1, 10, 11)
func_8984_call = mod.get_global_var('func_8984')
func_8986_call = mutated_mod.get_global_var('func_8986')
call_10295 = relay.TupleGetItem(func_8984_call(), 1)
call_10296 = relay.TupleGetItem(func_8986_call(), 1)
output = relay.Tuple([call_10275,bop_10279,call_10295,])
output2 = relay.Tuple([call_10276,bop_10282,call_10296,])
func_10298 = relay.Function([], output)
mod['func_10298'] = func_10298
mod = relay.transform.InferType()(mod)
output = func_10298()
func_10299 = relay.Function([], output)
mutated_mod['func_10299'] = func_10299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4293_call = mod.get_global_var('func_4293')
func_4295_call = mutated_mod.get_global_var('func_4295')
call_10356 = relay.TupleGetItem(func_4293_call(), 0)
call_10357 = relay.TupleGetItem(func_4295_call(), 0)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_10371 = relay.TupleGetItem(func_3064_call(), 0)
call_10372 = relay.TupleGetItem(func_3065_call(), 0)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_10373 = relay.TupleGetItem(func_3785_call(), 0)
call_10374 = relay.TupleGetItem(func_3787_call(), 0)
func_9666_call = mod.get_global_var('func_9666')
func_9669_call = mutated_mod.get_global_var('func_9669')
const_10378 = relay.const([[False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True],[True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,False,False,False,True],[True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False],[False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False],[False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False],[True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False],[True,True,False,True,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True],[True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False],[False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True],[True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True],[True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True],[False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True]], dtype = "bool")#candidate|10378|(12, 100)|const|bool
const_10379 = relay.const([[1.916245,9.127711,-9.135362,5.724612,-7.841669,-4.354469,2.955831,3.740934,9.126197,6.634150,6.872029,3.350196,-3.388597,-4.475620,4.497528,-1.512533,-0.901191,9.157226,-8.017824,9.516533,3.138585,-1.174962,-3.949326,-9.139689,-1.705915,-3.698282,-5.143391,-6.979341,3.679836,9.652511,9.507886,2.054271,-0.053541,-5.079066,-8.475163,8.143111,-4.801459,-1.628428,9.956794,-7.100948,-1.507997,9.789264,-6.234601,7.730740,-5.908094,-8.440916,6.644621,4.480510,-4.349961,-7.246095,6.623262,-6.689010,7.369688,-7.771842,9.222446,-2.556322,-3.257645,-1.829015,6.842523,-4.491691,6.249273,2.767140,-8.631413,-1.542858,5.060583,1.605790,-6.564167,-5.103407,-0.462856,-8.885269,4.963834,3.670391,-8.859762,-7.485351,-6.863242,4.016216,1.261087,-1.201135,1.727519,9.946908,7.492076,5.969297,-4.809362,0.098714,-5.976877,0.371133,-2.075715,2.779988,-8.235419,6.268916,-9.354013,-9.332322,9.603232,-8.046236,6.979301,8.924115,-8.229237,-9.090486,-3.704615,-7.369107,1.204413,-8.804528,-3.305757,-2.241345,8.410355,8.857783,-1.639439,-1.989167,-6.503491,-3.581113,-1.354973,-7.269895,-8.169039,5.760148,-6.747649,-2.508454,8.503566,-5.177942,-3.756751,5.234022,-0.228578,-5.878626,-8.683400,-3.059492,8.412568,1.499463,0.623017,-9.345235,-4.896576,-9.728980,1.980848,4.555018,-2.995808,7.987531,-7.181712,-2.191075,5.719021,-5.089256,0.080045,5.250336,5.123595,-0.083872,-0.935868,0.490964,7.280696,-4.596137,-0.704284,0.938934,7.979224,4.392888,8.275056,-8.505066,-8.839544,9.181972,6.138725,-9.252952,8.029492,2.914867,-9.051674,-6.679673,0.259277,-7.337951,-4.462234,-6.461888,-7.149622,-2.929412,8.408629,6.671459,7.927004,-0.578700,9.157434,7.655364,7.147692,-0.441228,7.835974,4.230448,0.088536,-5.481146,-6.391045,3.609609,9.449222,-2.697658,-5.240702,-4.274673,-0.308144,8.157979,-4.474641,-6.063670,6.029673,9.325045,-3.619337,0.042201,-4.528978,5.033401,-8.497613,-1.790295,-4.584174,8.253154,-2.371592,-9.919656,-3.184153,-0.791097,6.676944,-0.538748,2.416525,3.306999,3.725739,-8.394691,2.110600,-6.772427,-6.224533,6.937992,3.310589,-8.031103,-3.761754,2.338293,-8.343645,9.258301,-8.535662,-9.031885,5.555518,7.728918,5.276197,7.580563,-1.005585,-6.396912,-3.672108,8.190393,-8.266919,3.719458,2.063718,4.202918,-5.561643,4.253892,6.242744,-0.297284,2.357965,2.150630,2.541767,5.164041,-4.884637,1.613687,1.776412,-3.166994,-7.269296,8.777608,-5.959450,4.584656,4.715900,-1.350784,-5.141522,-9.346469,-3.261579,-0.418461,-1.835723,8.644940,-6.850143,6.318690,-6.793624,9.113217,5.328326,-8.476128,-8.227689,-9.111540,-6.425996,-2.418399,2.635564,-3.708514,-4.538189,-7.269664,5.612381,5.725093,-4.864997,4.029210,-5.572446,8.260844,5.450477,-3.799430,8.749242,-5.474922,2.757110,-5.235823,2.557550,-0.798264,-4.532292,-2.716525,6.925303,3.389183,-5.252403,-8.431332,4.271156,-4.273626,9.361067,-5.501288,8.002441,-8.746384,3.663294,5.702210,8.275084,-2.740152,-8.155816,6.219467,-6.637737,2.731836,-2.591486,-1.718225,3.295895,-7.029441,4.919637,8.403068,8.120048,3.640265,1.613206,9.526614,-4.087199,-4.932559,-5.333443,-6.202861,-7.322499,8.224247,5.690949,-9.509960,-5.587002,7.243517,-6.156638,-0.454864,-6.595341,-2.493026,6.464244,2.090519]], dtype = "float32")#candidate|10379|(1, 330)|const|float32
call_10377 = relay.TupleGetItem(func_9666_call(relay.reshape(const_10378.astype('bool'), [1200,]), relay.reshape(const_10379.astype('float32'), [55, 6]), ), 6)
call_10380 = relay.TupleGetItem(func_9669_call(relay.reshape(const_10378.astype('bool'), [1200,]), relay.reshape(const_10379.astype('float32'), [55, 6]), ), 6)
uop_10384 = relay.atanh(const_10378.astype('float32')) # shape=(12, 100)
output = relay.Tuple([call_10356,call_10371,call_10373,call_10377,const_10379,uop_10384,])
output2 = relay.Tuple([call_10357,call_10372,call_10374,call_10380,const_10379,uop_10384,])
func_10388 = relay.Function([], output)
mod['func_10388'] = func_10388
mod = relay.transform.InferType()(mod)
output = func_10388()
func_10389 = relay.Function([], output)
mutated_mod['func_10389'] = func_10389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4385_call = mod.get_global_var('func_4385')
func_4387_call = mutated_mod.get_global_var('func_4387')
call_10399 = relay.TupleGetItem(func_4385_call(), 0)
call_10400 = relay.TupleGetItem(func_4387_call(), 0)
func_4934_call = mod.get_global_var('func_4934')
func_4938_call = mutated_mod.get_global_var('func_4938')
var_10402 = relay.var("var_10402", dtype = "float64", shape = ())#candidate|10402|()|var|float64
var_10403 = relay.var("var_10403", dtype = "float64", shape = (720,))#candidate|10403|(720,)|var|float64
const_10404 = relay.const([[1.235184,-0.370641,3.732256,-5.858620,1.083927,3.052437,5.601560,-9.606190,1.773225,6.039159,4.128734,4.594745,-7.133833,-9.019051,-4.320712,-2.761033,3.451486,-2.821921,6.442747,-3.797450,2.840683,-0.682853,5.187565,3.807927,0.549336,-1.305378,3.658366,5.396365,6.745290,-0.212465,-8.703952,2.715700,5.794009,-7.921253,6.648175,-0.554700,-0.516299,0.779251,0.400202,-1.273754,-7.347997,-6.596592,-3.801631,0.366769,4.660791,7.472392,-5.146217,7.064093,-6.377464,-9.520779,-3.853892,-8.203579,5.278826,-4.961907,8.361156,3.804809,-8.780983,6.679300,5.361687,-6.347874,-8.450687,-4.653190,-0.257157,5.773114,1.786985,-6.248368,-8.885272,-7.487363,2.958951,-0.656948,-6.421246,-9.204256,6.551028,9.626935,-5.718257,7.882430,-2.782468,2.341787,-2.898351,7.309030,-4.925606,7.498320,2.587123,-7.634507,3.781930,2.837680,-6.175468,-7.590697,7.853067,2.053195,0.980954,-8.213583,-5.674678,-7.888441,-5.932545,5.331495,-6.945358,2.815130,-0.773544,-6.455570,6.160695,7.882422,9.382973,6.137443,-5.468768,-8.891035,-8.428105,1.024079,-4.052712,5.592313,3.255261,7.473065,4.314274,8.378349,-6.143925,9.523852,7.796251,3.912952,-8.272654,8.116063,8.318095,-5.180681,2.211468,0.794800,-1.714099,-3.706377,6.987751,8.164121,0.094531,-5.280323,-1.736620,5.548772,0.304789,-4.018281,4.501469,-8.085605,1.028280,-6.871048,-1.570378,-5.142233,-4.647053,-9.079651,-2.131571,1.440913,4.120961,3.199053,9.428891,6.568458,5.850211,3.346655,-0.389561,-6.860099,-1.474845,-9.097940,-8.904019,4.912873],[5.712255,-6.028627,2.928408,4.468406,4.712209,-8.159273,9.499969,2.928628,2.755088,-5.193116,-4.777871,5.881802,8.625779,7.757005,-5.860622,5.906948,9.148627,0.278151,2.689350,5.034560,8.604453,8.152091,2.831525,-3.157829,9.559970,-2.402550,7.282335,6.382157,5.561567,-8.037027,3.063311,-4.175470,4.841094,-6.358734,-8.028611,1.522654,6.772564,2.516603,-7.710003,-5.552159,-8.549883,8.603623,-0.418182,-7.319431,-0.641217,-6.145456,-9.390890,-2.607706,-3.398706,-0.509400,-7.722497,3.487242,5.665625,-7.476680,-8.320935,5.795027,-6.635617,-5.995544,9.428994,-2.283267,3.456485,-2.021447,0.159745,3.597050,7.307022,1.863832,6.322385,4.096939,7.795579,-5.407306,-7.046395,-3.353341,6.867800,-9.574145,7.836005,-2.398403,0.983875,2.069826,4.125495,-0.515991,-5.303769,-2.237344,-6.217198,-7.465303,8.474133,1.334653,4.596620,-8.118348,-1.614181,6.049320,-4.243529,-9.616508,-7.342812,-3.337809,-3.904486,-3.982788,-6.132636,9.853130,2.227171,-5.987720,-6.570896,-2.215697,4.662681,-0.950073,4.108589,-9.727035,5.634105,2.679281,-1.949537,8.635382,5.341080,2.987091,-1.439593,-1.174862,6.547354,6.198356,4.750996,5.201290,-1.134114,-0.266941,9.019921,3.079794,-3.856247,3.773211,7.690391,8.669906,-1.590916,-9.507132,3.706659,-8.046663,-0.419519,0.145871,-4.620296,-3.063168,-6.278726,-2.372683,5.348824,7.738019,5.141781,-4.729236,3.090662,2.115596,3.713212,5.624375,-3.732130,5.025345,3.753367,-7.176203,0.992136,-4.435418,-7.149663,8.603328,4.463721,1.770440,5.894824,1.992059],[4.086885,6.999979,-8.089981,-0.119211,-8.748425,0.748012,-5.584081,5.640172,0.032168,8.112682,0.606814,4.935852,0.378314,4.110947,4.312721,-4.478155,7.562408,3.481794,-4.866771,-8.061401,8.794103,-8.830406,-5.791492,6.026313,1.421676,6.517663,7.895109,0.415719,2.363474,-6.532953,2.836007,6.814640,-8.039006,4.551312,-1.863321,0.547738,0.503041,3.852051,-0.772313,8.426689,-8.820753,-2.384360,-2.087199,-3.887742,-9.075986,-0.018921,3.589950,-7.544599,-6.485374,-0.105845,4.525019,-9.024339,0.055510,-6.184846,-2.202827,-0.924173,-2.589415,-0.464551,-6.925394,-6.771820,7.028023,7.208570,0.764476,-6.829169,3.212721,-7.436184,7.273493,8.331669,6.336177,-6.293349,-5.907974,-1.593451,8.561302,8.483354,2.224784,-8.160781,-9.345965,-7.504593,3.555093,4.122670,8.845924,5.164583,-5.985667,-9.661244,3.636467,7.553846,6.108815,-4.676019,-1.262618,-8.511113,-7.136286,5.842843,-7.682909,-4.813372,-6.548487,-4.282208,8.128865,-1.205413,6.451578,3.559299,0.079828,-5.465731,-7.304419,9.238648,-3.664098,4.964169,-6.698576,6.534656,-6.311864,-7.124653,4.923011,-1.845574,2.641149,-5.853449,0.833872,8.438673,-1.642066,4.131855,-2.587323,8.101203,4.116222,6.416489,2.512723,-3.379755,-3.395510,9.676707,-2.309989,2.115314,-5.422943,-1.329002,8.167958,1.419414,6.166133,4.032031,2.944296,-6.363279,0.378626,6.858686,-4.284492,-0.046285,-3.685389,-2.827144,0.853931,-7.953128,9.647066,-8.184147,-1.087291,-0.543834,-4.450736,-7.767719,-5.219150,-1.527817,-9.024079,0.902864,-8.526929,-1.968601],[8.517135,9.291059,-8.108682,-5.334995,-3.765658,-1.892200,-1.441048,-5.634725,-8.041350,1.430514,2.416642,-0.668190,3.565569,-5.254576,0.336244,-2.337018,7.873491,-3.585221,-0.603623,9.712052,5.173363,8.678693,-1.372792,-3.687859,-1.674583,3.881453,-1.073383,-6.629041,0.153418,5.496132,5.505406,1.744373,7.496005,-2.736392,4.429892,-1.354675,7.747470,-9.807145,7.569772,5.873938,-0.781243,8.112469,-7.642036,-3.188746,-5.574265,3.004720,-9.070198,-2.498170,-8.615510,6.855806,-4.752370,-2.401401,5.684783,3.131497,3.942638,2.352517,6.603360,-6.226989,-6.203282,-3.284753,-1.858909,-7.339177,-6.388212,-4.697882,3.774578,-8.466142,7.604888,3.252849,-1.815643,2.377320,8.388045,1.420585,5.127863,9.973393,0.657377,-2.019394,2.315475,-5.818684,1.146238,-9.123444,-1.533163,-9.980655,2.980942,-2.979844,-3.663111,2.135592,-6.512506,9.663667,5.738010,0.385015,-9.539040,-4.214531,-4.958360,1.834518,-7.350410,-4.958811,8.193668,-8.553468,6.449942,-3.099423,6.470640,9.131113,-6.650880,9.912154,3.545052,-4.354208,6.146722,4.074962,9.289079,2.942820,-9.057796,-7.697715,7.766015,-6.709494,-3.830683,-7.996820,0.814881,4.557869,-2.384445,7.042800,-8.712744,0.218766,-2.167191,2.241384,-7.141705,6.277821,1.575657,-2.855496,8.570060,7.145232,2.722272,9.348021,3.103903,-0.678273,2.887517,-3.896945,-9.945285,9.579700,-4.080309,-1.813225,-3.535917,-8.810272,-8.670281,-6.271716,4.673311,5.183936,5.627505,9.545575,6.214063,6.794273,4.726373,-5.319008,1.448310,6.196317,4.617740,-1.498924],[7.970457,8.532043,1.980637,4.799366,1.600908,5.202251,6.426919,4.670334,5.975091,-3.500680,-9.633544,-1.287709,-1.900768,-4.900338,0.468576,6.186635,4.181158,-9.701520,-9.877525,8.155198,-0.920274,9.128538,-2.480189,6.849735,5.703019,-0.788816,-1.381631,8.698696,-1.959581,-6.995327,3.464372,0.572330,-6.214047,9.807574,3.126874,-9.143149,-1.206180,-4.146224,9.826572,-0.659715,3.696248,-8.709987,0.159180,-8.131203,0.272138,7.201180,2.507743,7.936317,2.492661,-9.819139,-7.911328,-5.296381,-8.510407,9.913511,-5.745229,-2.003227,-8.278852,-2.259056,2.349790,-2.346107,9.796495,5.376767,-4.174326,4.442676,0.227040,-3.752992,-2.304567,-2.620731,4.188410,-8.887001,0.754600,9.907416,-6.663735,6.488450,2.220291,-9.249542,-0.057461,9.268147,6.715522,-9.971832,-9.103663,-3.501383,0.525112,-0.756255,-7.588254,4.491617,8.437516,6.057396,-6.086588,5.208535,-2.235951,-3.011908,1.541444,1.636491,-8.810260,-6.035981,5.666051,-0.150822,1.531666,2.878669,5.758922,-5.932259,-7.551987,-9.061175,-2.327130,-4.316455,-2.440953,4.639377,-3.451409,-2.550373,-1.106456,4.358271,7.182463,1.889817,-8.655256,-5.893320,7.928576,7.154509,-4.816490,-7.403564,8.376924,-5.432262,6.928859,-8.684533,-0.570255,8.669017,5.584531,-2.066069,-8.349126,4.354583,0.512236,-8.073950,-2.139979,-4.067337,-0.798309,-1.686823,3.908264,6.589151,-5.247978,-7.439404,-7.889049,-1.527446,-2.811236,-9.140241,-6.522336,-0.704983,1.655476,-1.666217,-2.064674,-7.187572,4.974552,-3.379836,9.846440,7.300101,7.545701,6.269550]], dtype = "float64")#candidate|10404|(5, 156)|const|float64
call_10401 = relay.TupleGetItem(func_4934_call(relay.reshape(var_10402.astype('float64'), []), relay.reshape(var_10403.astype('float64'), [15, 8, 6]), relay.reshape(const_10404.astype('float64'), [780,]), ), 1)
call_10405 = relay.TupleGetItem(func_4938_call(relay.reshape(var_10402.astype('float64'), []), relay.reshape(var_10403.astype('float64'), [15, 8, 6]), relay.reshape(const_10404.astype('float64'), [780,]), ), 1)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_10406 = relay.TupleGetItem(func_6224_call(), 0)
call_10407 = relay.TupleGetItem(func_6226_call(), 0)
bop_10408 = relay.greater_equal(var_10402.astype('bool'), const_10404.astype('bool')) # shape=(5, 156)
output = relay.Tuple([call_10399,call_10401,var_10403,call_10406,bop_10408,])
output2 = relay.Tuple([call_10400,call_10405,var_10403,call_10407,bop_10408,])
func_10413 = relay.Function([var_10402,var_10403,], output)
mod['func_10413'] = func_10413
mod = relay.transform.InferType()(mod)
var_10414 = relay.var("var_10414", dtype = "float64", shape = ())#candidate|10414|()|var|float64
var_10415 = relay.var("var_10415", dtype = "float64", shape = (720,))#candidate|10415|(720,)|var|float64
output = func_10413(var_10414,var_10415,)
func_10416 = relay.Function([var_10414,var_10415,], output)
mutated_mod['func_10416'] = func_10416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3584_call = mod.get_global_var('func_3584')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_10427 = func_3584_call()
call_10428 = func_3584_call()
var_10429 = relay.var("var_10429", dtype = "float32", shape = (16, 10, 11))#candidate|10429|(16, 10, 11)|var|float32
bop_10430 = relay.bitwise_and(call_10427.astype('uint64'), var_10429.astype('uint64')) # shape=(16, 10, 11)
bop_10433 = relay.bitwise_and(call_10428.astype('uint64'), var_10429.astype('uint64')) # shape=(16, 10, 11)
func_4656_call = mod.get_global_var('func_4656')
func_4657_call = mutated_mod.get_global_var('func_4657')
call_10436 = relay.TupleGetItem(func_4656_call(), 0)
call_10437 = relay.TupleGetItem(func_4657_call(), 0)
output = relay.Tuple([bop_10430,call_10436,])
output2 = relay.Tuple([bop_10433,call_10437,])
func_10442 = relay.Function([var_10429,], output)
mod['func_10442'] = func_10442
mod = relay.transform.InferType()(mod)
mutated_mod['func_10442'] = func_10442
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10443 = relay.var("var_10443", dtype = "float32", shape = (16, 10, 11))#candidate|10443|(16, 10, 11)|var|float32
func_10442_call = mutated_mod.get_global_var('func_10442')
call_10444 = func_10442_call(var_10443)
output = call_10444
func_10445 = relay.Function([var_10443], output)
mutated_mod['func_10445'] = func_10445
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10526 = relay.var("var_10526", dtype = "float32", shape = (1, 10, 16))#candidate|10526|(1, 10, 16)|var|float32
var_10527 = relay.var("var_10527", dtype = "float32", shape = (1, 10, 16))#candidate|10527|(1, 10, 16)|var|float32
bop_10528 = relay.floor_mod(var_10526.astype('float32'), relay.reshape(var_10527.astype('float32'), relay.shape_of(var_10526))) # shape=(1, 10, 16)
output = bop_10528
output2 = bop_10528
func_10539 = relay.Function([var_10526,var_10527,], output)
mod['func_10539'] = func_10539
mod = relay.transform.InferType()(mod)
mutated_mod['func_10539'] = func_10539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10539_call = mutated_mod.get_global_var('func_10539')
var_10541 = relay.var("var_10541", dtype = "float32", shape = (1, 10, 16))#candidate|10541|(1, 10, 16)|var|float32
var_10542 = relay.var("var_10542", dtype = "float32", shape = (1, 10, 16))#candidate|10542|(1, 10, 16)|var|float32
call_10540 = func_10539_call(var_10541,var_10542,)
output = call_10540
func_10543 = relay.Function([var_10541,var_10542,], output)
mutated_mod['func_10543'] = func_10543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_10554 = func_4080_call()
call_10555 = func_4080_call()
output = relay.Tuple([call_10554,])
output2 = relay.Tuple([call_10555,])
func_10559 = relay.Function([], output)
mod['func_10559'] = func_10559
mod = relay.transform.InferType()(mod)
mutated_mod['func_10559'] = func_10559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10559_call = mutated_mod.get_global_var('func_10559')
call_10560 = func_10559_call()
output = call_10560
func_10561 = relay.Function([], output)
mutated_mod['func_10561'] = func_10561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6015_call = mod.get_global_var('func_6015')
func_6017_call = mutated_mod.get_global_var('func_6017')
call_10629 = relay.TupleGetItem(func_6015_call(), 0)
call_10630 = relay.TupleGetItem(func_6017_call(), 0)
func_3584_call = mod.get_global_var('func_3584')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_10639 = func_3584_call()
call_10640 = func_3584_call()
output = relay.Tuple([call_10629,call_10639,])
output2 = relay.Tuple([call_10630,call_10640,])
func_10644 = relay.Function([], output)
mod['func_10644'] = func_10644
mod = relay.transform.InferType()(mod)
output = func_10644()
func_10645 = relay.Function([], output)
mutated_mod['func_10645'] = func_10645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5751_call = mod.get_global_var('func_5751')
func_5753_call = mutated_mod.get_global_var('func_5753')
call_10690 = relay.TupleGetItem(func_5751_call(), 0)
call_10691 = relay.TupleGetItem(func_5753_call(), 0)
func_6431_call = mod.get_global_var('func_6431')
func_6434_call = mutated_mod.get_global_var('func_6434')
var_10714 = relay.var("var_10714", dtype = "bool", shape = (80,))#candidate|10714|(80,)|var|bool
call_10713 = relay.TupleGetItem(func_6431_call(relay.reshape(var_10714.astype('bool'), [80,])), 0)
call_10715 = relay.TupleGetItem(func_6434_call(relay.reshape(var_10714.astype('bool'), [80,])), 0)
func_9149_call = mod.get_global_var('func_9149')
func_9150_call = mutated_mod.get_global_var('func_9150')
call_10719 = relay.TupleGetItem(func_9149_call(), 5)
call_10720 = relay.TupleGetItem(func_9150_call(), 5)
output = relay.Tuple([call_10690,call_10713,var_10714,call_10719,])
output2 = relay.Tuple([call_10691,call_10715,var_10714,call_10720,])
func_10727 = relay.Function([var_10714,], output)
mod['func_10727'] = func_10727
mod = relay.transform.InferType()(mod)
var_10728 = relay.var("var_10728", dtype = "bool", shape = (80,))#candidate|10728|(80,)|var|bool
output = func_10727(var_10728)
func_10729 = relay.Function([var_10728], output)
mutated_mod['func_10729'] = func_10729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7914_call = mod.get_global_var('func_7914')
func_7916_call = mutated_mod.get_global_var('func_7916')
call_10767 = relay.TupleGetItem(func_7914_call(), 0)
call_10768 = relay.TupleGetItem(func_7916_call(), 0)
func_3086_call = mod.get_global_var('func_3086')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_10772 = relay.TupleGetItem(func_3086_call(), 1)
call_10773 = relay.TupleGetItem(func_3087_call(), 1)
output = relay.Tuple([call_10767,call_10772,])
output2 = relay.Tuple([call_10768,call_10773,])
func_10774 = relay.Function([], output)
mod['func_10774'] = func_10774
mod = relay.transform.InferType()(mod)
output = func_10774()
func_10775 = relay.Function([], output)
mutated_mod['func_10775'] = func_10775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8198_call = mod.get_global_var('func_8198')
func_8200_call = mutated_mod.get_global_var('func_8200')
call_10778 = relay.TupleGetItem(func_8198_call(), 0)
call_10779 = relay.TupleGetItem(func_8200_call(), 0)
func_6646_call = mod.get_global_var('func_6646')
func_6648_call = mutated_mod.get_global_var('func_6648')
call_10787 = relay.TupleGetItem(func_6646_call(), 0)
call_10788 = relay.TupleGetItem(func_6648_call(), 0)
func_9586_call = mod.get_global_var('func_9586')
func_9588_call = mutated_mod.get_global_var('func_9588')
call_10802 = relay.TupleGetItem(func_9586_call(), 0)
call_10803 = relay.TupleGetItem(func_9588_call(), 0)
output = relay.Tuple([call_10778,call_10787,call_10802,])
output2 = relay.Tuple([call_10779,call_10788,call_10803,])
func_10807 = relay.Function([], output)
mod['func_10807'] = func_10807
mod = relay.transform.InferType()(mod)
output = func_10807()
func_10808 = relay.Function([], output)
mutated_mod['func_10808'] = func_10808
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10844 = relay.var("var_10844", dtype = "uint32", shape = (15, 12, 4))#candidate|10844|(15, 12, 4)|var|uint32
var_10845 = relay.var("var_10845", dtype = "uint32", shape = (15, 12, 4))#candidate|10845|(15, 12, 4)|var|uint32
bop_10846 = relay.bitwise_xor(var_10844.astype('uint32'), relay.reshape(var_10845.astype('uint32'), relay.shape_of(var_10844))) # shape=(15, 12, 4)
output = relay.Tuple([bop_10846,])
output2 = relay.Tuple([bop_10846,])
func_10849 = relay.Function([var_10844,var_10845,], output)
mod['func_10849'] = func_10849
mod = relay.transform.InferType()(mod)
var_10850 = relay.var("var_10850", dtype = "uint32", shape = (15, 12, 4))#candidate|10850|(15, 12, 4)|var|uint32
var_10851 = relay.var("var_10851", dtype = "uint32", shape = (15, 12, 4))#candidate|10851|(15, 12, 4)|var|uint32
output = func_10849(var_10850,var_10851,)
func_10852 = relay.Function([var_10850,var_10851,], output)
mutated_mod['func_10852'] = func_10852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8136_call = mod.get_global_var('func_8136')
func_8137_call = mutated_mod.get_global_var('func_8137')
call_10946 = func_8136_call()
call_10947 = func_8136_call()
func_9768_call = mod.get_global_var('func_9768')
func_9770_call = mutated_mod.get_global_var('func_9770')
call_10959 = relay.TupleGetItem(func_9768_call(), 3)
call_10960 = relay.TupleGetItem(func_9770_call(), 3)
output = relay.Tuple([call_10946,call_10959,])
output2 = relay.Tuple([call_10947,call_10960,])
func_10969 = relay.Function([], output)
mod['func_10969'] = func_10969
mod = relay.transform.InferType()(mod)
mutated_mod['func_10969'] = func_10969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10969_call = mutated_mod.get_global_var('func_10969')
call_10970 = func_10969_call()
output = call_10970
func_10971 = relay.Function([], output)
mutated_mod['func_10971'] = func_10971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5085_call = mod.get_global_var('func_5085')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_10983 = relay.TupleGetItem(func_5085_call(), 0)
call_10984 = relay.TupleGetItem(func_5087_call(), 0)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_11019 = func_4614_call()
call_11020 = func_4614_call()
func_8727_call = mod.get_global_var('func_8727')
func_8728_call = mutated_mod.get_global_var('func_8728')
call_11021 = relay.TupleGetItem(func_8727_call(), 1)
call_11022 = relay.TupleGetItem(func_8728_call(), 1)
var_11029 = relay.var("var_11029", dtype = "float64", shape = (10, 78))#candidate|11029|(10, 78)|var|float64
bop_11030 = relay.minimum(call_11019.astype('uint8'), relay.reshape(var_11029.astype('uint8'), relay.shape_of(call_11019))) # shape=(10, 78)
bop_11033 = relay.minimum(call_11020.astype('uint8'), relay.reshape(var_11029.astype('uint8'), relay.shape_of(call_11020))) # shape=(10, 78)
func_6934_call = mod.get_global_var('func_6934')
func_6935_call = mutated_mod.get_global_var('func_6935')
call_11035 = func_6934_call()
call_11036 = func_6934_call()
bop_11041 = relay.bitwise_xor(call_11035.astype('int32'), relay.reshape(call_10983.astype('int32'), relay.shape_of(call_11035))) # shape=(1, 10, 11)
bop_11044 = relay.bitwise_xor(call_11036.astype('int32'), relay.reshape(call_10984.astype('int32'), relay.shape_of(call_11036))) # shape=(1, 10, 11)
func_9564_call = mod.get_global_var('func_9564')
func_9565_call = mutated_mod.get_global_var('func_9565')
call_11045 = func_9564_call()
call_11046 = func_9564_call()
output = relay.Tuple([call_11021,bop_11030,bop_11041,call_11045,])
output2 = relay.Tuple([call_11022,bop_11033,bop_11044,call_11046,])
func_11049 = relay.Function([var_11029,], output)
mod['func_11049'] = func_11049
mod = relay.transform.InferType()(mod)
mutated_mod['func_11049'] = func_11049
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11050 = relay.var("var_11050", dtype = "float64", shape = (10, 78))#candidate|11050|(10, 78)|var|float64
func_11049_call = mutated_mod.get_global_var('func_11049')
call_11051 = func_11049_call(var_11050)
output = call_11051
func_11052 = relay.Function([var_11050], output)
mutated_mod['func_11052'] = func_11052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7817_call = mod.get_global_var('func_7817')
func_7819_call = mutated_mod.get_global_var('func_7819')
call_11054 = relay.TupleGetItem(func_7817_call(), 0)
call_11055 = relay.TupleGetItem(func_7819_call(), 0)
func_10268_call = mod.get_global_var('func_10268')
func_10269_call = mutated_mod.get_global_var('func_10269')
call_11056 = func_10268_call()
call_11057 = func_10268_call()
func_10413_call = mod.get_global_var('func_10413')
func_10416_call = mutated_mod.get_global_var('func_10416')
const_11063 = relay.const(-5.549272, dtype = "float64")#candidate|11063|()|const|float64
var_11064 = relay.var("var_11064", dtype = "float64", shape = (720,))#candidate|11064|(720,)|var|float64
call_11062 = relay.TupleGetItem(func_10413_call(relay.reshape(const_11063.astype('float64'), []), relay.reshape(var_11064.astype('float64'), [720,]), ), 4)
call_11065 = relay.TupleGetItem(func_10416_call(relay.reshape(const_11063.astype('float64'), []), relay.reshape(var_11064.astype('float64'), [720,]), ), 4)
output = relay.Tuple([call_11054,call_11056,call_11062,const_11063,var_11064,])
output2 = relay.Tuple([call_11055,call_11057,call_11065,const_11063,var_11064,])
func_11071 = relay.Function([var_11064,], output)
mod['func_11071'] = func_11071
mod = relay.transform.InferType()(mod)
mutated_mod['func_11071'] = func_11071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11072 = relay.var("var_11072", dtype = "float64", shape = (720,))#candidate|11072|(720,)|var|float64
func_11071_call = mutated_mod.get_global_var('func_11071')
call_11073 = func_11071_call(var_11072)
output = call_11073
func_11074 = relay.Function([var_11072], output)
mutated_mod['func_11074'] = func_11074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mod.get_global_var('func_4641')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_11198 = relay.TupleGetItem(func_4641_call(), 0)
call_11199 = relay.TupleGetItem(func_4643_call(), 0)
output = call_11198
output2 = call_11199
func_11203 = relay.Function([], output)
mod['func_11203'] = func_11203
mod = relay.transform.InferType()(mod)
output = func_11203()
func_11204 = relay.Function([], output)
mutated_mod['func_11204'] = func_11204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6934_call = mod.get_global_var('func_6934')
func_6935_call = mutated_mod.get_global_var('func_6935')
call_11283 = func_6934_call()
call_11284 = func_6934_call()
func_8115_call = mod.get_global_var('func_8115')
func_8118_call = mutated_mod.get_global_var('func_8118')
var_11291 = relay.var("var_11291", dtype = "float64", shape = (780,))#candidate|11291|(780,)|var|float64
call_11290 = relay.TupleGetItem(func_8115_call(relay.reshape(var_11291.astype('float64'), [780,])), 3)
call_11292 = relay.TupleGetItem(func_8118_call(relay.reshape(var_11291.astype('float64'), [780,])), 3)
func_8600_call = mod.get_global_var('func_8600')
func_8602_call = mutated_mod.get_global_var('func_8602')
call_11303 = relay.TupleGetItem(func_8600_call(), 1)
call_11304 = relay.TupleGetItem(func_8602_call(), 1)
output = relay.Tuple([call_11283,call_11290,var_11291,call_11303,])
output2 = relay.Tuple([call_11284,call_11292,var_11291,call_11304,])
func_11309 = relay.Function([var_11291,], output)
mod['func_11309'] = func_11309
mod = relay.transform.InferType()(mod)
var_11310 = relay.var("var_11310", dtype = "float64", shape = (780,))#candidate|11310|(780,)|var|float64
output = func_11309(var_11310)
func_11311 = relay.Function([var_11310], output)
mutated_mod['func_11311'] = func_11311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mod.get_global_var('func_5517')
func_5519_call = mutated_mod.get_global_var('func_5519')
call_11316 = relay.TupleGetItem(func_5517_call(), 1)
call_11317 = relay.TupleGetItem(func_5519_call(), 1)
var_11322 = relay.var("var_11322", dtype = "float32", shape = (9, 10, 11))#candidate|11322|(9, 10, 11)|var|float32
bop_11323 = relay.mod(call_11316.astype('float32'), var_11322.astype('float32')) # shape=(9, 10, 11)
bop_11326 = relay.mod(call_11317.astype('float32'), var_11322.astype('float32')) # shape=(9, 10, 11)
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_11329 = func_3152_call()
call_11330 = func_3152_call()
output = relay.Tuple([bop_11323,call_11329,])
output2 = relay.Tuple([bop_11326,call_11330,])
func_11347 = relay.Function([var_11322,], output)
mod['func_11347'] = func_11347
mod = relay.transform.InferType()(mod)
var_11348 = relay.var("var_11348", dtype = "float32", shape = (9, 10, 11))#candidate|11348|(9, 10, 11)|var|float32
output = func_11347(var_11348)
func_11349 = relay.Function([var_11348], output)
mutated_mod['func_11349'] = func_11349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_11354 = relay.TupleGetItem(func_3161_call(), 0)
call_11355 = relay.TupleGetItem(func_3162_call(), 0)
output = relay.Tuple([call_11354,])
output2 = relay.Tuple([call_11355,])
func_11370 = relay.Function([], output)
mod['func_11370'] = func_11370
mod = relay.transform.InferType()(mod)
mutated_mod['func_11370'] = func_11370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11370_call = mutated_mod.get_global_var('func_11370')
call_11371 = func_11370_call()
output = call_11371
func_11372 = relay.Function([], output)
mutated_mod['func_11372'] = func_11372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mod.get_global_var('func_5272')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_11409 = relay.TupleGetItem(func_5272_call(), 2)
call_11410 = relay.TupleGetItem(func_5274_call(), 2)
output = relay.Tuple([call_11409,])
output2 = relay.Tuple([call_11410,])
func_11430 = relay.Function([], output)
mod['func_11430'] = func_11430
mod = relay.transform.InferType()(mod)
output = func_11430()
func_11431 = relay.Function([], output)
mutated_mod['func_11431'] = func_11431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_11487 = func_4614_call()
call_11488 = func_4614_call()
output = relay.Tuple([call_11487,])
output2 = relay.Tuple([call_11488,])
func_11504 = relay.Function([], output)
mod['func_11504'] = func_11504
mod = relay.transform.InferType()(mod)
mutated_mod['func_11504'] = func_11504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11504_call = mutated_mod.get_global_var('func_11504')
call_11505 = func_11504_call()
output = call_11505
func_11506 = relay.Function([], output)
mutated_mod['func_11506'] = func_11506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3645_call = mod.get_global_var('func_3645')
func_3647_call = mutated_mod.get_global_var('func_3647')
call_11530 = relay.TupleGetItem(func_3645_call(), 0)
call_11531 = relay.TupleGetItem(func_3647_call(), 0)
func_11430_call = mod.get_global_var('func_11430')
func_11431_call = mutated_mod.get_global_var('func_11431')
call_11535 = relay.TupleGetItem(func_11430_call(), 0)
call_11536 = relay.TupleGetItem(func_11431_call(), 0)
func_7333_call = mod.get_global_var('func_7333')
func_7337_call = mutated_mod.get_global_var('func_7337')
const_11563 = relay.const([0.115386,3.172680,2.101684,-5.860433,-3.919183,2.184374,-0.387158,-0.438313,7.815705,4.456925,0.817154,-9.633479,5.978962,-9.645011,-3.642191,6.136128,6.877515,1.079317,8.734015,8.652274,7.540255,-8.686639,1.504645,-0.846164,-4.600689,-3.167286,-3.781110,-5.252742,9.722287,-0.198234,9.824234,9.833863,-0.150187,0.803671,6.484137,-9.188688,9.823982,-3.473930,0.167029,6.296745,-8.906372,2.791598,-4.261128,8.954243,-1.103088,-8.608392,6.608481,-9.442725,-7.868294,3.311439,8.676651,2.912447,-2.327802,8.783294,-2.506421,8.353106,-6.865599,-7.167112,-2.594821,-5.790973,4.434579,-9.343469,5.057597,2.151096,9.662446,6.504841,-9.744054,8.314692,-2.224757,-8.056098,-9.534384,0.352480,-6.332314,7.055495,7.210606,8.992276,-5.633416,9.764179,6.049183,-8.896168,6.304153,2.818523,-3.503296,-1.290157,4.670442,4.379165,5.908289,0.647114,-7.463972,-3.643326,-1.257865,9.043520,-1.484039,-0.801749,9.490258,-9.905602,-6.379711,-9.383960,-3.969985,5.150620,6.240941,6.565126,-4.560711,-5.112663,-6.149012,-1.171330,-2.062962,8.815408,0.001113,-8.406627,-0.573696,5.831161,-1.269099,0.312228,2.562008,4.542950,-4.774404,8.506563,0.866189,3.916635,-6.209585,-9.842592,9.485976,3.082175,-3.612450,4.273422,-8.793201,6.297995,-0.890946,-4.148257,-7.048179,-7.992435,-3.716597,4.906035,6.191172,2.266187,-0.793148,8.015874,-3.432286,-3.483051,-7.679377,8.441326,8.495622,-8.506284,-7.782643,7.559762,-0.027925,6.382009,4.696776,-3.737411,9.334403,-4.929373,4.205453,-4.335657,2.195372,-7.005945,-3.086989,-4.502729,5.212767,-6.398463,8.326254,-4.716342,5.300380,0.986799,-1.980036,-0.750682,8.363300,3.218355,-8.677495,-0.329132,4.271922,7.492818,9.277994,6.406642,-2.222975,-3.239976,7.098350,9.837658,-7.760951,4.785447,-3.643211,-7.341262,-5.282085,6.641278,5.509550,-0.441616,-9.307041,2.177421,-2.238045,-1.316388,-7.008829,-2.800725,8.735113,-8.722175,-4.329084,-1.755748,9.766158,8.248925,1.047859,-1.432625,-7.878869,3.240991,1.454257,-8.454612,5.903676,-8.973083,0.716423,1.265009,8.979541,-3.306972,3.275020,-9.657236,-7.850637,-5.380546,-8.601402,-0.560409,-0.363211,-9.289261,-4.538502,6.816843,7.308804,6.510836,-1.295140,-4.601088,6.945878,-4.344719,1.873047,5.789850,-0.681217,6.564942,7.024972,3.305168,9.379121,5.857210,1.620863,1.267076,-5.520247,6.519685,7.652573,-8.780087,6.364072,8.126370,-6.790284,-1.268191,1.044461,8.032897,6.225594,-1.984721,-7.201081,6.512858,-2.677374,6.102887,4.548855,2.274822,-2.797226,0.129855,-2.032351,-0.867854,-0.353363,0.343709,3.932286,-4.752543,-0.491744,7.453468,-8.243056,-6.929779,-0.037629,5.643764,-6.622661,-0.620510,0.663764,-8.352329,6.501944,-5.577008,1.158090,4.404635,-1.677133,-6.902130,-7.096128,-0.004911,-8.098458,7.530354,-8.746531,-2.907182,0.835039,9.301289,0.752690,2.758357,-5.762159,-1.288314,0.815855,-6.478744,1.219262,-4.006296,4.719599,-8.560382,8.565069,-4.380271,-8.004908,0.599156,6.978888,-9.764140,-6.665082,5.615007,1.778361,6.287240,7.809503,0.058776,-6.676745,-7.804213,-7.182297,3.159936,-3.687954,7.711820,-4.620578,1.515434,9.393441,-9.060627,4.823136,-2.105100,0.133664,6.821152,-6.838639,9.678064,0.629544,-5.160322,-1.745916,7.911519,2.884090,-4.740942,5.185842,3.225587,5.341090,1.297499,-1.303578,-1.129407,5.911605,-2.477006,-9.536307,-7.420881,-9.120101,4.074403,-4.373759,7.775264,9.536183,6.406726,1.229789,5.916290,3.357620,0.095140,-9.564615,4.369653,-1.683461,1.018227,-2.494215,-2.173944,-4.032700,9.422032,-1.750257,-0.597857,-9.038084,4.963461,6.018365,1.557704,8.293694,-7.390533,-7.002759,5.871948,9.528630,6.555872,-5.411187,-9.711338,5.038265,9.990022,3.046136,6.885620,2.868394,2.361889,8.945337,0.902597,-5.189900,-0.266135,-5.205013,1.522196,4.411297,3.136451,-2.633610,-7.672619,2.280058,9.647077,-3.740437,8.289194,7.046612,-4.836135,5.258623,9.072189,5.744220,-3.880371,8.581581,8.465016,-7.809303,-9.979412,4.934511,-7.589804,-4.681270,9.614997,-0.378811,5.432642,2.177873,-0.073713,0.113677,-6.408329,1.017899,-1.973192,-5.556369,9.745047,-1.520693,6.460133,1.002082,3.443597,-6.911113,-0.419896,7.410444,-9.925855,3.101945,6.079975,7.043805,3.435222,-9.856862,8.833480,0.339747,2.346080,4.744536,3.920438,-5.090029,-1.244697,1.590754,2.594816,-5.752891,-6.555152,-0.121940,9.111672,4.785653,-2.484451,-0.711633,5.945085,8.229596,-5.069864,4.197607,5.691792,-5.645827,-1.283700,-9.623011,-0.846115,-1.939496,-0.467843,-2.188875,-4.784800,-2.813545,8.338593,-1.944443,-2.202135,4.795958,-2.125984,4.474151,-2.841005,-0.451110,4.615593,-1.276987,5.476114,-8.954825,5.583462,2.670289,2.507780,-3.682219,2.400723,4.385084,-6.093229,-7.160915,8.375527,-3.860661,9.131367,9.756064,7.928063,-3.381201,-3.402477,-3.740882,4.458695,6.632013,7.497316,4.984011,-8.756203,1.780249,5.896544,-7.582100,7.903188,-7.484001,0.015811,0.181710,4.306002,6.820949,8.112706,9.823909,-2.293545,1.526828,-6.839387,-9.287724,8.844851,-4.472903,5.073957,5.214823,4.777833,2.022284,4.624055,-2.315110,-6.723010,-5.716205,7.999327,-8.500311,-5.126387,-2.255180,-5.155861,-9.821245,-7.347844,-5.421909,6.013583,-1.176199,4.994128,7.380125,-0.079546,6.688340,2.265722,-1.403802,4.543763,-4.007732,-2.800604,-6.078004,3.462376,-8.382234,3.760570,6.272623,4.880178,-1.956446,2.903301,3.505882,3.501542,-4.051189,5.251752,7.909983,4.117994,-5.859147,-9.105363,-2.801652,4.426759,2.313189,5.753284,9.385345,-0.630926,5.247174,6.550254,-6.557877,6.050544,-5.406151,1.131382,6.335946,0.923372,2.240529,0.845156,-0.446419,-1.716321,4.973527,-2.332281,-0.692462,-6.724137,3.478304,6.680451,-7.253369,-2.355579,5.292534,5.665003,2.059048,-4.373451,-4.713805,-6.174315,4.237041,9.365169,0.413074,8.658676,-2.301675,7.949686,-2.626692,0.617313,-9.186748,8.517259,-2.401522,-8.827336,3.977019,-0.029571,-8.260431,-4.246677,5.582631,0.956843,-2.989520,8.381384,-9.732323,-1.224830,3.039912,-0.075291,5.594317,4.370453,-1.795501,6.577629,-1.654859,9.151476,4.380870,-3.386314,7.862178,1.088460,0.359861,1.046194,9.947174,-8.898019,0.032934,-9.244438,-8.135484,-3.952885,-7.582683,-6.675571,7.164624,2.791503,-1.162745,-5.772438,7.099369,3.190425,-3.889687,7.212629,-5.261615,-5.546737,-3.489430,-6.639057,-7.781165,3.205381,2.011877,8.136785,9.684475,3.073268,4.851189,-8.182754,3.047799,8.758079,-8.974201,1.392766,-5.174178,-2.662668,3.610561,6.305075,-1.991553,-2.658316,-4.393120,-5.582627,-8.633190,2.194119,9.907146,5.826799,7.231918,-5.907848,5.611938,-3.604943,3.389719,-7.175375,-6.854735,-9.534948,-0.172703,-8.704612,5.249512,-5.292602,-6.766186,7.788028,0.585802,-5.901700,3.263073,-4.794569,-5.572696,-6.677304,-9.846944,-7.203699,-8.870971,4.092280,5.347749,8.880304,-2.181031,9.386103,-4.100255,1.125334,1.505766,-2.658687,-2.583865,9.258206,-4.645144,6.391676,-0.699287,2.082067,-9.880043,5.394067,-4.003811,-9.994487,-6.148092,4.329465,-5.089113,9.764616,-2.557215,-6.208509,-1.066295,1.281729,0.203158,5.419320,5.114184,-3.235137,4.054186,7.291812,1.634221,8.759994,8.178803,-1.250921,6.137511,4.693591,9.307451,-3.943064,5.929011,-7.980303,-5.443102,-2.193859,-6.214547,-7.757210,-0.540854,4.163220,2.194519,-4.101372,7.570436,0.310828,-2.430478,-8.217551,-5.306755,7.955295,5.624187,3.330477,-3.822448,2.581890,-6.905118,-0.013749,3.701152,-9.083488,-9.683092,-5.113114,4.775253,-4.981946,-3.971448,-6.352593,-8.127074,1.857774,0.835593,4.871721,-6.069812,3.377048,-0.192003,-3.505944,3.090012,9.011651,6.079497,-5.043011,1.576184,-4.972406,2.661640,-3.166463,-0.880312,8.377309,-4.233925,3.594863,4.239953,-6.606634,9.690529,-8.586536,1.693904,-3.438213,6.205674,-8.377689,-9.929367,-0.631376,4.254251,9.235754,-5.580183,1.267793,0.325546,-9.792598,0.052571,9.294995,5.563576,-4.120752,0.783270,3.651714,0.261803,6.843329,-7.721742,9.804432,-0.536696,3.281011,-5.406119,-1.915353,-0.664336,-9.067654,4.119605,-3.666479,6.430023,8.486196,1.172017,9.677475,-8.392865,-8.792841,9.233116,-1.029357,-7.339606,-4.664160,4.625895,4.815282,8.969700,3.145142,2.212496,7.554159,-4.150560,0.520223,3.371355,-7.046965,6.275739,-5.444726,7.660623,-1.718428,1.046976,-9.318490,7.485890,-5.678770,2.127290,0.799318,4.521140,-1.078108,-3.022571,4.685697,-3.180501,9.699674,5.825443,-4.093646,2.307908,-6.511404,-9.038536,3.751354,-2.531952,-3.725066,3.594727,-3.811992,0.725326,5.562790,-2.705286,6.840713,-8.143152,-2.930142,2.309738,-8.708862,-3.604605,5.771621,4.988456,-4.604095,-9.101637,-7.135427,5.540260,-7.157244,4.236334,-9.483160,-7.932610,-0.321040,-7.271362,-2.660985,-4.667516,-1.131831,-8.938785,6.737585,-1.717390,7.184832,-3.255757,9.300492,4.190983,-7.939483,6.294940,-8.925952,2.327582,-0.790591,-8.269801,5.274455,-4.255934,9.004234,6.080779,-9.654824,-8.420446,-9.373411,3.543201,-2.444806,6.624352,5.171067,0.058566,-5.188843,7.757990,4.228526,-9.146484,-0.045401,-3.126090,4.648509,-6.351679,-0.256535,1.088295,5.645152,-9.915744,9.862992,9.309694,-4.602512,6.514832,1.393568,1.040333,-9.576471,9.935685,-6.477026,-5.338658,1.453693,-3.098486,8.964045,-6.542749,-2.610179,5.605955,-3.926095,9.779473,5.946833,7.407342,9.466087,8.300782,-7.706010,-0.139935,2.937124,-7.626050,2.127118,-6.735938,1.210118,9.066686,0.693773,8.321675,5.165145,-1.049220,5.763502,1.553714,-5.149442,-9.226615,4.493126,-0.259857,4.962329,6.174759,5.566682,-0.369165,-1.356935,-1.487331,-8.043923,0.423193,-4.355507,-3.845049,-2.044663,-0.182161,1.775396,7.220216,9.192726,1.283560,0.536560,5.827111,-0.396981,4.456015,-1.343143,-1.173022,4.115817,-3.606784,4.617127,-0.031504,4.675903,-3.893735,6.924244,0.483980,0.054193,-6.534742,-5.269535,3.622887,3.183674,0.485583,1.477356,-9.410368,-5.343981,-1.352509,2.312262,3.072910,-7.542648,4.219864,2.426574,-5.545701,3.761401,4.987174,5.809247,-0.927301,7.279808,-8.749651,2.234521,-8.212114,9.914801,7.391417,2.117413,8.077489,8.445179,3.178216,-5.050319,1.568606,-0.866227,3.123706,-9.468948,-6.341382,8.901603,-1.563211,6.822450,-1.265454,5.029279,-2.604285,-2.055930,-3.875335,-0.936821,8.158108,-6.810213,1.540817,0.700030,-8.927875,-2.009272,-9.826649,4.930132,2.769943,2.511079,1.484257,6.619206,8.172350,-1.113668,6.146162,8.461602,5.952145,-6.115532,0.678423,5.614963,6.880017,-2.615552,1.454000,-3.795588,6.818790,1.420926,-6.885033,-5.310021,-6.177096,-3.174119,7.866505,-0.094868,2.385450,0.300628,3.254844,-5.978019,2.070174,-0.086823,-8.619460,2.362809,-5.622287,-4.110659,1.223857,-4.384148,8.470894,-8.106463,-4.767582,2.508407,0.312477,-1.531146,2.460329,3.084401,-9.400752,-7.392859,-0.148309,-2.868454,-6.260646,1.415799,3.093081,2.260990,-7.410793,1.171005,8.053785,-2.550027,-3.318495,7.608707,4.128284,-1.650737,-1.584234,-8.859050,-2.745917,0.972403,-8.563460,-3.940408,-5.608597,-6.924347,6.830505,4.024774,3.184365,6.997038,9.670976,6.360147,3.049987,-3.347955,-1.077415,-3.900844,5.413719,0.384527,6.922940,2.571813,-7.407451,-8.432154,2.043504,-9.650919,-2.043730,-0.969585,-1.037110,-4.627301,1.156869,9.147371,-9.662435,-5.540609,6.739879,1.136006,-5.979573,-6.817139,-9.647796,-8.704587,-3.218662,-0.316994,9.267481,-9.899497,7.655280,8.520238,2.499565,-8.021903,4.068202,8.507815,3.833494,2.643738,7.566325,-5.229507,-8.937287,-1.505397,2.732191,4.529117,9.137595,-7.095407,0.842117,-9.867788,-3.002516,-4.310957,4.391047,-6.218532,-7.366702,-4.109053,0.342233,3.982570,-6.325767,-0.873410,2.177006,-3.691644,-2.773954,9.199074,-5.483996,-5.002195,-1.106706,-3.126592,4.026887,-2.616764,-2.076584,7.975120,6.886920,-1.041771,-2.472683,2.566033,-4.512664,1.852119,-8.788348,-0.897301,-2.824189,3.666381,4.006651,-6.220877,-3.722689,-0.336167,-2.452582,-5.936668,1.558793,1.339650,-9.234020,5.425047,-0.521819,1.606109,8.255891,7.533006,-8.784157,-7.160389,3.033757,-0.255181,-1.469068,-2.006693,3.971076,-8.247612,0.012060,-6.560196,1.514893,4.001271,-0.146398,-7.672691,-8.308991,7.264886,2.776629,6.952671,2.172784,-2.483192,-7.745647,-6.005654,-7.875246,-5.766591,-6.126242,1.056418,-5.392167,7.956348,3.085810,-0.974726,0.140488,-8.173615,-4.425074,3.937561,-9.134227,7.322950,7.998856,-8.167727,-3.041231,7.777951,6.636972,-4.958363,9.293398,9.242726,-9.898212,6.449522,2.117183,-0.538467,2.117147,5.320683,2.068225,-8.719802,-1.219450,-1.515671,-3.166700,2.050802,-7.635117,0.088321,0.659811,-5.701778,5.095135,-6.762689,-6.066850,-7.478139,-6.102238,2.472042,-0.192400,-5.302569,-8.770030,8.540013,6.704598,-5.298227,8.802571,5.271289,-1.411088,-8.116463,2.344039,5.321073,1.571145,9.593397,9.465748,4.351852,4.266820,6.615591,4.702133,-5.805920,2.120406,-4.514845,-4.020597,-2.053970,-0.479134,-3.988385,5.400551,9.227365,3.393216,-4.246069,5.996794,-1.590941,-2.284135,-5.309074,1.489277,-4.945738,5.368114,6.174080,-9.374138,5.240567,-1.370814,7.273824,3.096941,-2.817792,2.950350,2.774305,-6.143476,7.220901,1.003268,-0.442480,-7.213443,-5.636387,-2.392608,-4.191820,0.700954,4.257966,3.615493,9.744124,2.329153,-4.238147,-4.771867,4.537680,2.056241,0.591708,-6.384192,5.702322,-6.490353,-0.100653,2.241381,-4.544288,-8.559312,-8.091880,-4.720750,-5.785000,9.824368,-6.075338,5.044304,6.761089,6.183688,9.328474,-9.440895,-0.410798,-7.184413,9.349049,5.450276,-6.526000,0.513598,-0.969286,-6.757271,6.274897,2.288998,-6.230173,2.230447,7.324763,-5.580104,-6.094596,-9.533863,-1.312155,-1.748501,-9.142352,8.137232,3.069166,-5.270754,-7.196264,3.085716,-6.364252,7.823070,2.330387,-1.640611,7.058145,9.631440,-6.776232,5.288654,9.763014,-1.272316,2.199697,-0.376741,8.311978,-9.927402,-4.583410,7.621931,-6.484849,9.319495,-5.755132,2.024987,-9.794596,5.650231,-5.660686,0.843877,-2.200674,9.836146,3.830880,5.815766,-5.083250,-2.185172,1.570950,-9.735023,0.816290,8.381459,5.152985,1.485018,4.533141,-8.722183,2.156994,2.121050,-1.504044,-3.455595,4.189184,-2.317720,4.266286,-1.337826,-4.526944,8.099759,-2.044700,4.508738,4.777950,2.770282,-8.785269,-4.488059,-8.470430,5.110428,-6.140347,-2.700005,9.456900,-9.008793,-4.409350,4.613097,5.749608,-0.260331,1.068045,9.343416,-8.842751,-9.690263,6.312671,1.853970,-7.738969,-2.270224,-9.650717,-3.076328,9.424216,-5.901125,7.355054,-1.318474,-8.880952,-0.397053,9.009771,-8.386398,5.150349,-5.722527,4.966062,-3.755097,-6.593110,0.767181,7.146458,8.812670,-5.882791,-7.072396,6.106734,-0.139616,8.174992,-5.895251,-7.445358,1.743741,2.454777,-6.229333,7.788555,-1.021995,6.809020,-5.368132,-3.242087,3.366419,0.807780,-7.389987,4.447809,2.423319,-9.177221,9.406042,-8.054012,-8.783266,-2.046983,4.871627,9.976994,1.228725,9.423491,0.954343,7.521324,-5.214926,5.680887,-1.824178,0.368707,6.389147,8.502486,-4.723334,7.881480,2.038085,-1.072286,7.340074,-6.392532,-2.229102,-6.810949,9.561979,8.704450,0.143550,6.077226,4.453423,5.815937,-0.422483,5.936559,-2.662108,7.703716,-6.133244,-1.394303,4.959500,-3.662107,-4.405000,3.916677,3.053068,5.641959,7.560526,-3.560278,2.679597,-9.549191,-3.792631,4.457771,-6.097486,-1.060807,-6.683065,0.991490,1.510155,9.813716,-0.282627,-3.810985,3.283574,-8.503469,-0.918408,6.336623,-1.826816,4.190933,4.096749,-7.623282,1.619848,-6.498287,4.682976,3.153166,-7.240472,3.056467,0.699698,-4.916136,2.337083,-3.766836,0.038933,-2.317265,9.918462,-8.129168,-5.992231,-5.283412,1.714303,7.420538,-2.467078,2.687430,9.482391,-0.701929,-9.887230,-4.575646,3.630488,2.912022,-5.472989,3.636106,4.886536,9.584514,-5.630319,3.650040,-9.564217,-7.697144,3.452541,2.309269,-4.609745,-1.588794,-9.161746,2.223003,6.285417,-8.739810,-5.513632,1.831835,6.982458,6.687514,-8.525018,8.475087,0.470361,-2.010268,-1.937022,2.594271,9.183493,4.151213,-5.870047,6.856485,-9.064115,-0.116820,3.720058,-1.220830,-3.255810,-0.655636,6.280294,6.357263,-6.124140,3.410763,-9.137256,0.963762,-2.189757,2.269521,6.368550,-7.609324,8.761056,-8.307139,-7.849645,9.223779,-4.720936,-1.149656,-0.238169,-5.480550,6.239115,5.035956,0.607665,4.071115,0.744177,-2.896620,9.873025,-0.851684,4.563729,-8.707117,-4.377341,-3.860885,2.674404,-9.927665,9.991597,-5.719430,-1.372108,-2.775111,2.278455,-4.956308,-2.300375,6.183453,3.051350,-9.985754,5.360240,7.617336,0.900091,-6.554962,-5.815719,-9.933125,-6.477093,-5.282923,-6.606536,-5.456018,-0.467521,-5.621357,3.006668,-8.630334,-8.594396,-0.024833,5.188869,5.441712,8.010756,-3.560950,-1.097269,1.625910,9.178799,1.688674,-8.262576,4.076363,-0.258590,-3.558403,-9.764917,3.280978,2.616062,-4.582865,1.829741,9.743452,7.695143,-5.707132,-3.879263,-7.749915,0.389207,6.734304,9.554046,-4.220091,8.546223,-5.822772,6.304432,-4.808419,3.310773,-7.825467,-0.373548,4.012235,0.128820,7.703442,-2.037027,0.689326,4.474967,0.079193,-0.747989,8.745553,-8.347231,1.447143,7.869927,8.362811,-8.763401,9.530434,0.161959,-7.193979,-8.706641,0.103875,-2.661484,-9.428801,8.779945,-2.093705,8.955007,0.532813,2.903686,3.638417,-7.223855,5.426065,-4.309408,5.965456,-6.540160,-5.647017,6.262121,6.410302,2.140234,-2.010271,3.403229,-5.876138,-3.474182,9.666376,-8.514409,-4.656259,7.017259,8.926312,-3.523134,0.624985,-5.986942,9.690183,5.989047,7.274931,-1.567740,-8.271847,7.986043,-5.063625,-1.827910,4.726808,-1.040418,-3.166980,-0.854786,-4.066723,-3.763387,1.897258,7.172373,9.172328,3.288315,8.024355,-3.752099,5.608987,-7.513511,9.454706,5.797033,4.923457,-9.138710,7.030662,2.615877,7.779855,-5.174916,1.373625,1.039317,-0.923779,8.234564,-7.818254], dtype = "float64")#candidate|11563|(1792,)|const|float64
call_11562 = relay.TupleGetItem(func_7333_call(relay.reshape(const_11563.astype('float64'), [8, 14, 16]), relay.reshape(const_11563.astype('float64'), [8, 14, 16]), ), 3)
call_11564 = relay.TupleGetItem(func_7337_call(relay.reshape(const_11563.astype('float64'), [8, 14, 16]), relay.reshape(const_11563.astype('float64'), [8, 14, 16]), ), 3)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_11566 = func_2835_call()
call_11567 = func_2835_call()
uop_11569 = relay.sinh(call_11562.astype('float32')) # shape=(8, 14, 16)
uop_11571 = relay.sinh(call_11564.astype('float32')) # shape=(8, 14, 16)
func_6501_call = mod.get_global_var('func_6501')
func_6503_call = mutated_mod.get_global_var('func_6503')
const_11578 = relay.const([9.278959,8.794793,6.176469,0.200793,4.832221,-5.203151,-0.882365,-4.928657,3.802144,2.837641,-8.756401,2.103050,7.809143,-6.143546,1.248738,-7.205090,-2.816277,-4.886389,4.269922,2.492692,3.303625,6.941440,3.905626,6.814986,-2.049968,2.830174,1.737656,1.001721,7.417439,5.137339,-7.843476,0.296462,9.223486,-6.167796,6.116371,7.604805,5.020695,5.119073,1.851930,2.342417,8.409701,-2.438503,-8.957172,1.937316,4.964076,-8.202927,-7.658075,8.878128,9.299106,3.158008,5.890153,7.579218,0.387565,5.470003,5.373732,-1.383520,4.658178,3.693452,-0.762084,2.471055,1.072757,7.006363,-6.690612,5.046570,-2.393925,-2.825570,-9.035438,-3.520111,-1.821740,-5.203097,3.492303,-9.064461,8.310382,-2.887649,8.290878,1.882579,0.336403,-5.188524,8.354621,-3.159254,-9.325333,2.396814,-4.829327,-1.799136,-0.434596,4.189174,0.859459,-0.122849,7.420734,6.985254,6.256354,-4.790822,3.515447,-2.197624,-8.988779,5.066816,9.700911,5.847907,-3.246336,6.702657,-9.741777,-2.779171,-0.956731,-9.637940,3.860488,-7.135990,8.973827,-3.413450,-0.219578,0.448823,3.289807,2.209172,-9.949566,-9.986986,7.684222,0.382034,-5.955020,0.624065,-5.498949,3.521949,2.731856,-2.818523,-5.959119,-6.970602,2.682555,1.737938,-0.972599,-7.323777,-6.892054,6.104271,-5.148220,2.832392,2.801659,8.449745,7.779525,0.718630,4.676677,3.367890,-5.074574,-3.034135,2.572958,-5.541940,-8.904321,-0.657824,-7.220309,-5.850691,-2.670059,7.109825,2.391965,-6.333658,1.403013,5.569641,8.327882,-9.862684,-6.599085,-2.689225,4.082968,6.457416,0.125252,-1.267833,-7.945408,-6.367129,-9.189943,-1.564292,-6.741362,-5.772126,-1.098704,-9.454458,-6.375346,-6.499393,5.710096,3.290190,9.281785,2.852818,-7.170842,-8.279218,-4.570425,-4.052959,0.126227,-6.224243,1.265117,0.139162,4.998882,5.365042,8.436962,-8.405908,-1.953905,0.526870,0.259503,-1.811598,-0.655284,-4.018994,5.427080,6.674204,6.948555,1.313882,7.371179,-6.556939,-9.514488,-6.408098,9.790946,1.622054,-7.399582,-2.917309,2.079997,-4.335906,7.019049,-8.862353,7.607292,2.515225,-6.718590,4.301466,-6.648858,-4.951219,0.681705,-4.920508,8.200117,5.847741,-6.218434,9.692067,-6.256671,2.129290,-0.178412,9.850705,4.676539,-1.619591,9.605071,3.553314,-0.660427,-5.204699,2.620776,-9.445964,-8.453158,-8.035791,9.700902,-9.839645,5.390595,-1.671364,-5.150653,8.741372,-6.898825,2.467848,9.375159,2.030628,-6.572572,-8.417646,-8.543652,-2.993173,-2.493455,5.376140,2.349796,7.685089,2.785966,-3.940177,7.890482,-0.440394,-0.855858,3.121372,-3.893307,4.900665,3.780440,-3.113525,-2.470297,-4.991581,-4.739385,3.958756,-6.367481,-0.167459,-9.731746,6.020450,1.981170,7.537617,6.449348,7.520032,-0.419024,-3.439109,-5.375394,7.733974,2.615676,7.445744,-2.868161,9.787912,-5.112633,-0.108829,2.298160,-6.504676,0.050361,-5.140801,1.281675,4.492546,-5.910202,7.145194,-8.952557,7.803162,-7.760284,0.489222,3.808522,3.519034,4.333021,-8.863253,0.115282,8.634552,7.446703,3.777257,2.713033,-3.653148,-5.366243,2.757606,-4.697994,1.045230,6.855301,7.219480,4.889724,-3.966792,4.930626,4.769742,-9.904576,9.738526,-1.408464,-5.364168,3.270566,0.335967,-9.308946,2.681977,-9.144462,0.509435,5.115812,-2.073663,-0.818079,3.170135], dtype = "float32")#candidate|11578|(330,)|const|float32
call_11577 = relay.TupleGetItem(func_6501_call(relay.reshape(const_11578.astype('float32'), [330,])), 0)
call_11579 = relay.TupleGetItem(func_6503_call(relay.reshape(const_11578.astype('float32'), [330,])), 0)
output = relay.Tuple([call_11530,call_11535,const_11563,call_11566,uop_11569,call_11577,const_11578,])
output2 = relay.Tuple([call_11531,call_11536,const_11563,call_11567,uop_11571,call_11579,const_11578,])
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
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_11628 = relay.TupleGetItem(func_4982_call(), 3)
call_11629 = relay.TupleGetItem(func_4983_call(), 3)
output = relay.Tuple([call_11628,])
output2 = relay.Tuple([call_11629,])
func_11635 = relay.Function([], output)
mod['func_11635'] = func_11635
mod = relay.transform.InferType()(mod)
mutated_mod['func_11635'] = func_11635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11635_call = mutated_mod.get_global_var('func_11635')
call_11636 = func_11635_call()
output = call_11636
func_11637 = relay.Function([], output)
mutated_mod['func_11637'] = func_11637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6646_call = mod.get_global_var('func_6646')
func_6648_call = mutated_mod.get_global_var('func_6648')
call_11660 = relay.TupleGetItem(func_6646_call(), 1)
call_11661 = relay.TupleGetItem(func_6648_call(), 1)
func_4824_call = mod.get_global_var('func_4824')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_11724 = relay.TupleGetItem(func_4824_call(), 0)
call_11725 = relay.TupleGetItem(func_4825_call(), 0)
func_2479_call = mod.get_global_var('func_2479')
func_2484_call = mutated_mod.get_global_var('func_2484')
var_11752 = relay.var("var_11752", dtype = "float64", shape = (144,))#candidate|11752|(144,)|var|float64
var_11753 = relay.var("var_11753", dtype = "float64", shape = (780,))#candidate|11753|(780,)|var|float64
call_11751 = relay.TupleGetItem(func_2479_call(relay.reshape(var_11752.astype('float64'), [144,]), relay.reshape(var_11753.astype('float64'), [390, 2]), relay.reshape(call_11660.astype('float64'), [5, 28]), ), 6)
call_11754 = relay.TupleGetItem(func_2484_call(relay.reshape(var_11752.astype('float64'), [144,]), relay.reshape(var_11753.astype('float64'), [390, 2]), relay.reshape(call_11660.astype('float64'), [5, 28]), ), 6)
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_11758 = relay.TupleGetItem(func_3218_call(), 0)
call_11759 = relay.TupleGetItem(func_3219_call(), 0)
func_10849_call = mod.get_global_var('func_10849')
func_10852_call = mutated_mod.get_global_var('func_10852')
var_11764 = relay.var("var_11764", dtype = "uint32", shape = (720,))#candidate|11764|(720,)|var|uint32
call_11763 = relay.TupleGetItem(func_10849_call(relay.reshape(var_11764.astype('uint32'), [15, 12, 4]), relay.reshape(var_11764.astype('uint32'), [15, 12, 4]), ), 0)
call_11765 = relay.TupleGetItem(func_10852_call(relay.reshape(var_11764.astype('uint32'), [15, 12, 4]), relay.reshape(var_11764.astype('uint32'), [15, 12, 4]), ), 0)
output = relay.Tuple([call_11660,call_11724,call_11751,var_11752,var_11753,call_11758,call_11763,var_11764,])
output2 = relay.Tuple([call_11661,call_11725,call_11754,var_11752,var_11753,call_11759,call_11765,var_11764,])
func_11771 = relay.Function([var_11752,var_11753,var_11764,], output)
mod['func_11771'] = func_11771
mod = relay.transform.InferType()(mod)
mutated_mod['func_11771'] = func_11771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11771_call = mutated_mod.get_global_var('func_11771')
var_11773 = relay.var("var_11773", dtype = "float64", shape = (144,))#candidate|11773|(144,)|var|float64
var_11774 = relay.var("var_11774", dtype = "float64", shape = (780,))#candidate|11774|(780,)|var|float64
var_11775 = relay.var("var_11775", dtype = "uint32", shape = (720,))#candidate|11775|(720,)|var|uint32
call_11772 = func_11771_call(var_11773,var_11774,var_11775,)
output = call_11772
func_11776 = relay.Function([var_11773,var_11774,var_11775,], output)
mutated_mod['func_11776'] = func_11776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mod.get_global_var('func_5272')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_11813 = relay.TupleGetItem(func_5272_call(), 0)
call_11814 = relay.TupleGetItem(func_5274_call(), 0)
output = relay.Tuple([call_11813,])
output2 = relay.Tuple([call_11814,])
func_11819 = relay.Function([], output)
mod['func_11819'] = func_11819
mod = relay.transform.InferType()(mod)
output = func_11819()
func_11820 = relay.Function([], output)
mutated_mod['func_11820'] = func_11820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8905_call = mod.get_global_var('func_8905')
func_8907_call = mutated_mod.get_global_var('func_8907')
call_11922 = relay.TupleGetItem(func_8905_call(), 0)
call_11923 = relay.TupleGetItem(func_8907_call(), 0)
output = call_11922
output2 = call_11923
func_11926 = relay.Function([], output)
mod['func_11926'] = func_11926
mod = relay.transform.InferType()(mod)
mutated_mod['func_11926'] = func_11926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11926_call = mutated_mod.get_global_var('func_11926')
call_11927 = func_11926_call()
output = call_11927
func_11928 = relay.Function([], output)
mutated_mod['func_11928'] = func_11928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5846_call = mod.get_global_var('func_5846')
func_5848_call = mutated_mod.get_global_var('func_5848')
call_11941 = func_5846_call()
call_11942 = func_5846_call()
output = call_11941
output2 = call_11942
func_11962 = relay.Function([], output)
mod['func_11962'] = func_11962
mod = relay.transform.InferType()(mod)
mutated_mod['func_11962'] = func_11962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11962_call = mutated_mod.get_global_var('func_11962')
call_11963 = func_11962_call()
output = call_11963
func_11964 = relay.Function([], output)
mutated_mod['func_11964'] = func_11964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9883_call = mod.get_global_var('func_9883')
func_9885_call = mutated_mod.get_global_var('func_9885')
call_12056 = func_9883_call()
call_12057 = func_9883_call()
output = relay.Tuple([call_12056,])
output2 = relay.Tuple([call_12057,])
func_12067 = relay.Function([], output)
mod['func_12067'] = func_12067
mod = relay.transform.InferType()(mod)
output = func_12067()
func_12068 = relay.Function([], output)
mutated_mod['func_12068'] = func_12068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mod.get_global_var('func_5272')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_12117 = relay.TupleGetItem(func_5272_call(), 2)
call_12118 = relay.TupleGetItem(func_5274_call(), 2)
func_9586_call = mod.get_global_var('func_9586')
func_9588_call = mutated_mod.get_global_var('func_9588')
call_12138 = relay.TupleGetItem(func_9586_call(), 0)
call_12139 = relay.TupleGetItem(func_9588_call(), 0)
func_2479_call = mod.get_global_var('func_2479')
func_2484_call = mutated_mod.get_global_var('func_2484')
const_12152 = relay.const([[-1.295995,3.908629,-1.539406,8.748268,2.467568,-7.588611,9.271465,6.579613,3.213459,-8.087524,1.539652,8.539629,-3.565633,-6.201588,-9.420777,-2.625606,-0.946141,-0.196220],[0.643589,6.853921,4.912241,-9.763244,-2.504658,-3.392368,1.042197,-3.014585,8.397903,1.736382,-4.724635,3.939651,-4.766773,1.617921,6.912873,8.992174,3.596621,5.410728],[-4.539202,-2.701014,0.061181,-4.060141,3.774235,-3.021124,-7.438652,-7.378250,7.233612,0.870291,2.252442,9.595380,-0.854273,6.800125,8.918915,-3.295218,-4.678745,-7.839321],[1.371099,1.508072,1.383876,-0.191197,7.244347,-1.418306,-5.587105,-7.903374,-9.190680,-2.451256,-4.446650,-0.683759,3.109553,1.265086,5.857142,5.208309,-6.058903,2.291458],[-5.550562,6.251849,-3.109474,0.641249,6.221355,-4.922863,1.166225,9.924750,-3.934062,7.951425,-3.038740,-2.065467,-4.355214,7.456643,-4.193755,-9.702245,-3.430444,-9.405168],[1.985722,4.678695,-8.056584,-1.460558,-1.828581,7.860143,0.268528,-0.511581,-9.749791,-6.619513,8.486635,9.294035,-9.131454,-8.895707,-1.710556,-7.453856,-6.126988,-8.161456],[9.188635,-9.860613,-2.809563,1.322930,-1.954581,-7.422611,-4.466234,4.182995,-9.640277,6.798480,-5.604431,6.368759,-8.580154,-7.931065,4.270978,3.994081,4.369677,-4.837512],[-3.883120,-9.997534,-3.768864,2.868756,2.265475,-0.039109,5.434219,-7.376076,2.822765,-4.994075,1.522664,2.194269,-0.338373,-8.212993,-6.761234,3.892312,-8.447155,-5.545148]], dtype = "float64")#candidate|12152|(8, 18)|const|float64
var_12153 = relay.var("var_12153", dtype = "float64", shape = (780,))#candidate|12153|(780,)|var|float64
var_12154 = relay.var("var_12154", dtype = "float64", shape = (140,))#candidate|12154|(140,)|var|float64
call_12151 = relay.TupleGetItem(func_2479_call(relay.reshape(const_12152.astype('float64'), [144,]), relay.reshape(var_12153.astype('float64'), [390, 2]), relay.reshape(var_12154.astype('float64'), [5, 28]), ), 5)
call_12155 = relay.TupleGetItem(func_2484_call(relay.reshape(const_12152.astype('float64'), [144,]), relay.reshape(var_12153.astype('float64'), [390, 2]), relay.reshape(var_12154.astype('float64'), [5, 28]), ), 5)
func_6015_call = mod.get_global_var('func_6015')
func_6017_call = mutated_mod.get_global_var('func_6017')
call_12169 = relay.TupleGetItem(func_6015_call(), 0)
call_12170 = relay.TupleGetItem(func_6017_call(), 0)
output = relay.Tuple([call_12117,call_12138,call_12151,const_12152,var_12153,var_12154,call_12169,])
output2 = relay.Tuple([call_12118,call_12139,call_12155,const_12152,var_12153,var_12154,call_12170,])
func_12179 = relay.Function([var_12153,var_12154,], output)
mod['func_12179'] = func_12179
mod = relay.transform.InferType()(mod)
mutated_mod['func_12179'] = func_12179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12179_call = mutated_mod.get_global_var('func_12179')
var_12181 = relay.var("var_12181", dtype = "float64", shape = (780,))#candidate|12181|(780,)|var|float64
var_12182 = relay.var("var_12182", dtype = "float64", shape = (140,))#candidate|12182|(140,)|var|float64
call_12180 = func_12179_call(var_12181,var_12182,)
output = call_12180
func_12183 = relay.Function([var_12181,var_12182,], output)
mutated_mod['func_12183'] = func_12183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10644_call = mod.get_global_var('func_10644')
func_10645_call = mutated_mod.get_global_var('func_10645')
call_12185 = relay.TupleGetItem(func_10644_call(), 0)
call_12186 = relay.TupleGetItem(func_10645_call(), 0)
var_12196 = relay.var("var_12196", dtype = "float32", shape = (5, 10, 11))#candidate|12196|(5, 10, 11)|var|float32
bop_12197 = relay.floor_divide(call_12185.astype('float32'), var_12196.astype('float32')) # shape=(5, 10, 11)
bop_12200 = relay.floor_divide(call_12186.astype('float32'), var_12196.astype('float32')) # shape=(5, 10, 11)
output = relay.Tuple([bop_12197,])
output2 = relay.Tuple([bop_12200,])
func_12201 = relay.Function([var_12196,], output)
mod['func_12201'] = func_12201
mod = relay.transform.InferType()(mod)
var_12202 = relay.var("var_12202", dtype = "float32", shape = (5, 10, 11))#candidate|12202|(5, 10, 11)|var|float32
output = func_12201(var_12202)
func_12203 = relay.Function([var_12202], output)
mutated_mod['func_12203'] = func_12203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10268_call = mod.get_global_var('func_10268')
func_10269_call = mutated_mod.get_global_var('func_10269')
call_12250 = func_10268_call()
call_12251 = func_10268_call()
output = relay.Tuple([call_12250,])
output2 = relay.Tuple([call_12251,])
func_12277 = relay.Function([], output)
mod['func_12277'] = func_12277
mod = relay.transform.InferType()(mod)
mutated_mod['func_12277'] = func_12277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12277_call = mutated_mod.get_global_var('func_12277')
call_12278 = func_12277_call()
output = call_12278
func_12279 = relay.Function([], output)
mutated_mod['func_12279'] = func_12279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_12280 = relay.TupleGetItem(func_3507_call(), 0)
call_12281 = relay.TupleGetItem(func_3508_call(), 0)
func_5370_call = mod.get_global_var('func_5370')
func_5372_call = mutated_mod.get_global_var('func_5372')
var_12284 = relay.var("var_12284", dtype = "float32", shape = (1760, 1))#candidate|12284|(1760, 1)|var|float32
call_12283 = relay.TupleGetItem(func_5370_call(relay.reshape(var_12284.astype('float32'), [16, 10, 11])), 2)
call_12285 = relay.TupleGetItem(func_5372_call(relay.reshape(var_12284.astype('float32'), [16, 10, 11])), 2)
output = relay.Tuple([call_12280,call_12283,var_12284,])
output2 = relay.Tuple([call_12281,call_12285,var_12284,])
func_12313 = relay.Function([var_12284,], output)
mod['func_12313'] = func_12313
mod = relay.transform.InferType()(mod)
mutated_mod['func_12313'] = func_12313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12314 = relay.var("var_12314", dtype = "float32", shape = (1760, 1))#candidate|12314|(1760, 1)|var|float32
func_12313_call = mutated_mod.get_global_var('func_12313')
call_12315 = func_12313_call(var_12314)
output = call_12315
func_12316 = relay.Function([var_12314], output)
mutated_mod['func_12316'] = func_12316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_12350 = relay.TupleGetItem(func_6224_call(), 0)
call_12351 = relay.TupleGetItem(func_6226_call(), 0)
var_12371 = relay.var("var_12371", dtype = "float32", shape = (11, 10, 11))#candidate|12371|(11, 10, 11)|var|float32
bop_12372 = relay.minimum(call_12350.astype('int16'), var_12371.astype('int16')) # shape=(11, 10, 11)
bop_12375 = relay.minimum(call_12351.astype('int16'), var_12371.astype('int16')) # shape=(11, 10, 11)
output = relay.Tuple([bop_12372,])
output2 = relay.Tuple([bop_12375,])
func_12380 = relay.Function([var_12371,], output)
mod['func_12380'] = func_12380
mod = relay.transform.InferType()(mod)
mutated_mod['func_12380'] = func_12380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12381 = relay.var("var_12381", dtype = "float32", shape = (11, 10, 11))#candidate|12381|(11, 10, 11)|var|float32
func_12380_call = mutated_mod.get_global_var('func_12380')
call_12382 = func_12380_call(var_12381)
output = call_12382
func_12383 = relay.Function([var_12381], output)
mutated_mod['func_12383'] = func_12383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12277_call = mod.get_global_var('func_12277')
func_12279_call = mutated_mod.get_global_var('func_12279')
call_12402 = relay.TupleGetItem(func_12277_call(), 0)
call_12403 = relay.TupleGetItem(func_12279_call(), 0)
output = relay.Tuple([call_12402,])
output2 = relay.Tuple([call_12403,])
func_12459 = relay.Function([], output)
mod['func_12459'] = func_12459
mod = relay.transform.InferType()(mod)
output = func_12459()
func_12460 = relay.Function([], output)
mutated_mod['func_12460'] = func_12460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10113_call = mod.get_global_var('func_10113')
func_10114_call = mutated_mod.get_global_var('func_10114')
call_12545 = func_10113_call()
call_12546 = func_10113_call()
output = relay.Tuple([call_12545,])
output2 = relay.Tuple([call_12546,])
func_12547 = relay.Function([], output)
mod['func_12547'] = func_12547
mod = relay.transform.InferType()(mod)
output = func_12547()
func_12548 = relay.Function([], output)
mutated_mod['func_12548'] = func_12548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6015_call = mod.get_global_var('func_6015')
func_6017_call = mutated_mod.get_global_var('func_6017')
call_12584 = relay.TupleGetItem(func_6015_call(), 0)
call_12585 = relay.TupleGetItem(func_6017_call(), 0)
func_3115_call = mod.get_global_var('func_3115')
func_3116_call = mutated_mod.get_global_var('func_3116')
call_12596 = relay.TupleGetItem(func_3115_call(), 0)
call_12597 = relay.TupleGetItem(func_3116_call(), 0)
const_12602 = relay.const([[[9.389011,-7.807099,7.813004,-5.807733,-6.165520,0.311618,0.982259,1.175186,0.557595,0.331176,-7.330093],[2.628115,-2.346396,9.789080,8.630812,6.650032,-0.767246,1.338092,2.812756,2.701553,6.561615,0.847319],[3.216155,3.782541,4.025155,-3.004512,9.355482,2.027026,-0.897451,1.604547,5.342566,-0.948329,7.931063],[6.686972,-4.953662,-4.428186,7.564277,-6.966550,-3.007998,-0.416690,-3.283621,9.601669,-6.773855,-0.868186],[3.436028,-7.607039,-8.175658,-3.139176,1.526872,-0.411806,-9.140428,5.863280,-0.707235,-5.403842,8.072807],[4.019643,2.067976,1.314962,5.403993,4.737409,-7.022427,0.007836,-6.690118,-1.954932,-5.871489,5.271263],[9.722403,-8.008231,3.085401,-8.712236,9.856909,-1.156283,3.877288,-4.094574,6.234295,4.542282,-0.557233],[-5.222386,0.406081,-2.770840,1.970816,-9.325684,-0.168788,1.470645,-5.572281,6.269183,0.960146,-2.438019],[9.068698,5.332194,-7.873815,-9.315915,3.160939,-9.427654,2.006210,-0.058693,-6.644923,4.545854,-8.225282],[-5.082749,0.645563,-8.997029,-3.908010,1.049710,-9.931367,-7.448091,7.874343,3.217195,-3.782559,3.964091]],[[-1.067671,-7.273161,1.726445,3.939292,-9.022088,-6.140136,1.523868,-1.370332,0.502151,-4.929064,-0.896389],[7.934561,0.806845,3.597380,-7.120380,-2.508631,-1.420562,2.251894,-8.005218,7.587495,1.684772,-7.256356],[6.160690,-6.340299,-8.767923,-8.294644,4.753803,4.928314,-5.320787,-8.790123,9.289631,4.368870,-6.895090],[6.673450,5.722542,8.623588,-5.796022,-2.178852,8.705975,7.318519,1.183498,-9.664823,9.266233,7.780786],[-9.511330,-8.775977,-1.537554,-7.252530,-7.134146,-9.506243,-4.001777,-5.998123,3.997946,-2.378201,0.974886],[1.130949,5.490758,-9.802620,4.718722,-5.080661,6.653733,8.975675,-0.156227,-6.587964,-8.796319,3.108090],[7.424959,2.455142,-8.904240,0.658498,3.185442,-6.538636,-3.040184,4.910588,-9.953782,-8.487969,-1.909093],[-2.703390,8.937236,-1.312368,5.499066,-9.239021,3.851101,3.241216,-5.104788,-1.405556,7.806290,-7.066498],[0.149098,6.878493,-4.872025,5.026054,-6.273410,6.020013,1.583360,7.619604,0.816915,2.349512,1.624583],[-3.328881,7.981396,-4.967236,7.063710,-1.560708,-5.304582,1.796411,5.720568,-6.758791,-6.749001,1.141626]],[[5.329699,-2.060426,6.552484,8.611743,-7.733415,-0.253538,-5.038288,2.165308,1.957549,-0.130988,3.032849],[-9.062399,9.922134,-5.672550,1.331537,4.318622,-4.163192,8.547727,1.962283,7.315304,9.224181,2.721953],[-9.457358,8.992187,-1.736224,3.502101,4.627451,0.870130,-4.587898,-6.733938,0.120324,-8.919828,5.823327],[1.438277,8.287248,1.774405,-9.663503,-0.795439,1.566539,4.044351,-6.746508,9.580632,-9.593827,-6.466904],[7.120193,-6.339669,-0.274873,-8.207161,3.193381,-2.243427,-1.208021,2.244050,-6.561241,5.718649,2.195531],[4.563539,-9.077087,-0.542371,7.248212,5.338079,7.942234,-2.253764,6.047771,-8.310985,-0.383222,2.575805],[-6.141177,-4.584930,-0.160832,-0.586730,-6.604154,7.494377,-0.585056,9.334182,-6.419670,-7.070097,2.036687],[8.524405,-1.442538,8.774606,-5.840799,6.620462,9.680572,6.734252,-0.831570,0.611685,-5.555551,6.881514],[-1.316839,-4.288612,1.577974,3.103276,7.055963,2.693758,-8.121411,4.085189,8.705560,7.858692,-2.774724],[4.537879,-5.394975,9.143699,1.884261,5.375521,4.224108,6.336238,0.041609,5.985363,6.593180,-0.758582]],[[9.092098,4.992695,-8.252869,8.859633,0.533312,7.821558,-1.696504,-4.222405,8.586309,9.492287,-2.364816],[-5.256573,4.597708,-4.652720,-0.072155,-3.421541,-6.074251,4.453532,-5.858534,8.196130,5.556313,6.181345],[8.149869,0.102118,-3.281988,-0.855492,5.645176,-1.378222,-5.888738,-0.105875,1.916896,5.727867,-0.187108],[-9.465980,2.938211,-0.679371,6.042252,-3.201322,-4.750575,7.438155,1.065230,8.047902,-9.811472,8.965105],[-7.986407,-9.228253,8.118295,-9.873620,-6.260992,-2.285666,-1.165775,-0.343030,5.529503,8.368147,-2.796607],[-9.926107,-9.695301,9.421382,7.700593,6.167499,-9.834095,6.514782,3.425662,4.814816,-4.558302,-0.154019],[-1.465553,-6.359073,9.020443,9.378738,5.667724,5.367356,9.434614,-0.378726,-8.109143,4.270928,6.532257],[-2.940274,-0.477943,-1.427556,0.078660,9.719854,2.625919,3.830552,7.570671,3.003410,-8.108213,-9.436278],[5.490765,-6.039765,0.286063,-7.420989,-0.361569,0.788706,-9.734313,-9.867100,-5.055609,7.847015,2.730475],[6.111120,-7.036584,1.016527,6.682500,-4.210519,3.617548,-7.499117,-9.398956,6.699218,2.461123,5.634659]],[[7.698538,-5.052116,-2.675316,2.666659,-9.403724,-0.155366,9.375939,-0.498676,-9.968603,0.824077,1.420680],[-7.747596,-5.710355,2.857112,-4.990849,4.367932,-1.060852,-0.995249,-5.771750,-7.915784,-7.683756,2.372143],[7.815312,-9.495139,-9.992093,1.777960,-2.582202,-0.485029,2.993619,-1.659908,-4.720060,3.989337,8.128700],[4.284018,-2.078756,5.004326,9.392917,-4.144422,-5.920592,-6.045196,8.877960,-9.440474,4.158959,-1.416543],[-0.110239,-4.907847,6.631484,2.918790,4.769474,-6.205283,1.595911,-1.439474,-3.041354,1.937236,-9.397461],[8.025180,1.208912,6.982010,-3.737414,1.712612,-6.005681,-6.888623,-5.241002,8.952949,-1.715562,4.925902],[2.827558,-3.940225,-9.816436,-8.335564,6.217861,-3.827722,4.575447,5.326810,-3.145956,3.760056,1.262742],[-8.631291,2.223325,5.360688,3.990743,2.862066,8.791882,-8.370865,8.773661,-1.949149,-6.921810,5.445862],[-4.978273,-8.781173,-2.706299,8.355562,7.247060,0.664432,6.329761,-3.003716,1.904770,1.923463,-0.878933],[-0.039420,-1.292339,-0.676139,-7.200884,5.082027,4.651135,7.378790,4.494399,7.222893,-3.485847,4.975534]],[[7.630227,-2.442512,-0.783527,2.663140,3.864621,-3.363498,-8.636696,-5.495427,7.640721,4.777327,2.424995],[-1.147275,-9.495313,0.341225,-6.548631,-2.281536,6.992301,-5.328737,1.050173,-8.840970,4.393860,-2.556749],[9.656100,-4.811123,-6.019394,4.191931,-5.175089,-7.516860,1.391719,4.759916,8.788498,-3.007345,-5.149643],[-2.512222,-5.293738,-1.493562,7.270111,-3.852866,-6.788622,2.280110,-2.761632,-3.184881,-4.031062,4.458681],[3.320045,6.168862,1.540712,5.231830,-6.895495,0.561341,-1.111206,4.906862,-9.178457,-0.861826,-2.649329],[-4.018527,4.133457,-1.891561,4.182912,4.979596,-8.201499,7.197072,-8.454592,-8.427126,-3.237089,-2.326300],[2.726006,5.415159,3.550172,-5.349633,9.166709,-9.486334,-6.962251,6.140483,1.735611,-5.595114,0.568903],[2.493756,-7.235315,8.796094,1.184606,2.592155,9.623216,-3.291564,-2.847635,-7.657018,2.178287,-4.737545],[8.795067,-6.241270,2.086150,6.599083,-8.754562,-2.204311,-6.656441,-5.911878,8.988852,-1.227702,-9.937696],[3.903931,-8.163917,-6.581638,6.979724,7.271335,-0.244707,8.141574,-1.498279,8.939357,2.020660,4.423681]],[[4.653243,8.088548,9.087153,9.466472,-0.145768,-8.105990,-1.692612,3.730811,-5.090250,9.089674,-4.835154],[-5.683114,5.252334,7.746413,7.182146,-1.351579,-7.514592,-5.399135,2.021432,1.540265,-8.855974,-1.250243],[8.506238,-7.316172,-3.935096,-5.173987,-3.016114,1.762630,-6.642189,-2.098010,2.737205,-9.552780,-6.757624],[2.289988,-8.108421,-3.899743,4.113321,-7.512853,-9.889212,-5.946954,-4.666215,1.317073,2.285946,-2.889141],[6.757916,5.197609,8.493507,7.860139,-6.368175,4.093681,7.175592,-8.691243,7.021287,8.758959,2.377946],[-3.974477,5.223401,9.517817,9.507290,-9.058764,-9.049608,8.430983,-6.590176,-1.813581,-9.590185,3.929658],[9.760181,-7.471025,-7.838311,-4.048615,4.777327,8.658216,-4.644985,1.671195,-9.308062,-0.332932,5.881471],[-8.612714,-4.448245,2.819713,6.286362,2.452026,-4.928729,5.049112,7.997858,-3.324431,-9.858546,7.773521],[-3.246548,-7.368628,3.763955,-1.745707,5.564829,-7.237896,2.657884,-9.840482,-7.425991,7.423020,5.728207],[-2.629823,-9.851493,7.469903,-2.725068,3.485550,2.046292,-9.073899,-3.516597,7.635657,8.724208,-1.437832]],[[6.485920,7.632637,-9.307732,-3.519706,7.396240,-1.830375,-4.880932,1.763106,7.244117,1.535473,-2.666484],[1.981636,-6.185440,-8.080816,-0.825716,-6.734081,0.475652,6.005243,-9.760064,7.445713,-3.506610,9.339385],[7.242237,-1.161504,7.534387,9.588717,8.103283,3.297884,-6.535725,1.442179,-0.925055,-4.291205,-1.985244],[5.917210,-1.738789,-0.131998,-8.330943,2.342894,-9.583252,-6.862500,0.090583,-2.186052,-8.834070,3.599152],[2.142604,7.125543,-7.820818,-6.959617,-9.857909,-6.589201,-6.749609,9.691296,-7.750900,5.633318,-7.558845],[7.730493,9.912905,-6.849774,0.340591,-2.214844,5.988215,-6.446542,-9.108606,-7.070258,-0.769042,4.773653],[3.185599,3.489698,8.677915,9.108045,3.668617,4.107486,-7.822959,-0.063947,4.857142,-9.589305,8.361289],[1.169036,8.911294,-8.130051,-1.735149,1.957421,-8.951904,5.888848,6.777759,-1.427761,4.812393,9.741935],[4.363357,5.111963,5.588287,0.102087,-8.469133,-5.114530,-6.925625,7.090125,-4.788687,2.075365,-4.032447],[-8.354542,9.775141,-1.251818,-7.385108,-5.533716,7.433579,0.265756,8.284424,8.853612,9.981889,-3.044259]],[[-3.087852,-6.001265,-4.489965,-7.825037,-2.433206,-8.123911,9.524684,6.717492,-8.612534,4.716642,2.552777],[-3.290951,-0.332854,7.165328,1.286599,4.660044,7.397797,-6.569402,0.940738,-2.750798,2.073059,4.592565],[8.344912,6.297068,-8.890130,-9.279635,0.537575,9.875015,-5.425985,9.372006,-3.289243,-8.971965,-3.434986],[2.777955,7.673612,1.157160,-3.621694,7.869129,3.807414,2.348029,8.642791,-0.618423,8.712065,-2.600902],[-6.091342,9.076721,1.424921,-2.997513,9.735031,8.534786,-2.485370,7.454161,-5.080975,-1.941296,9.658362],[4.424482,6.289730,6.954517,8.332749,8.529718,0.785003,-8.667865,-8.700776,-6.686929,-2.615205,-1.384983],[3.212525,3.635394,-6.700864,5.183978,-9.250316,-7.579936,-1.612073,-1.204363,-3.729958,5.151793,-0.954425],[-3.342217,3.774394,-8.437727,-3.480751,-6.228370,8.836913,1.721562,5.064087,5.326785,-9.689166,-9.900953],[-5.121162,-3.706370,-3.243308,-1.187896,-9.798388,2.727311,-5.818116,2.415373,-8.144972,-0.345274,-5.076229],[8.187486,-6.749905,4.513630,-6.258201,-0.014399,-3.455183,6.754614,-7.825454,2.561652,-8.922548,-6.090321]]], dtype = "float32")#candidate|12602|(9, 10, 11)|const|float32
bop_12603 = relay.bitwise_xor(call_12596.astype('uint8'), const_12602.astype('uint8')) # shape=(9, 10, 11)
bop_12606 = relay.bitwise_xor(call_12597.astype('uint8'), const_12602.astype('uint8')) # shape=(9, 10, 11)
output = relay.Tuple([call_12584,bop_12603,])
output2 = relay.Tuple([call_12585,bop_12606,])
func_12610 = relay.Function([], output)
mod['func_12610'] = func_12610
mod = relay.transform.InferType()(mod)
output = func_12610()
func_12611 = relay.Function([], output)
mutated_mod['func_12611'] = func_12611
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12624 = relay.const([[[False,False,True,True,False,True,False,True,True,False,False],[True,False,False,True,False,False,False,True,True,True,True],[True,True,True,False,False,False,False,False,False,False,True],[False,True,True,True,True,False,True,True,False,False,False],[True,True,False,True,False,False,False,True,True,True,False],[False,False,True,False,False,True,True,True,False,True,False],[True,False,False,True,True,True,False,False,True,True,True],[False,False,True,False,False,True,True,False,True,True,False],[False,False,False,False,True,True,False,False,False,False,False],[False,True,False,True,True,False,True,False,True,True,False],[True,True,True,False,False,True,True,True,True,False,True]],[[True,False,False,True,False,False,True,False,True,True,False],[True,False,True,True,True,False,False,False,False,True,True],[True,True,True,False,True,True,True,True,False,True,True],[True,False,True,True,True,False,False,False,False,True,False],[True,False,False,True,True,False,False,False,False,True,False],[True,False,True,False,True,False,True,False,True,False,False],[False,True,True,False,False,True,False,True,False,False,False],[False,True,True,False,True,True,False,True,True,False,True],[False,False,False,False,True,True,True,True,True,False,True],[True,False,True,False,True,False,False,True,False,False,False],[True,True,False,True,True,True,False,True,False,True,False]],[[False,True,True,True,True,True,True,True,False,False,True],[True,False,False,True,True,True,False,True,False,True,False],[False,False,False,True,True,True,True,False,True,True,True],[True,True,False,False,False,True,False,False,True,True,False],[True,False,True,True,False,True,True,False,True,True,False],[True,False,True,True,True,True,False,False,True,True,True],[True,True,True,True,True,True,False,False,False,True,True],[True,False,True,False,True,True,False,False,False,True,False],[True,False,True,True,True,False,False,False,True,True,False],[True,False,True,False,False,False,False,False,True,False,False],[False,False,False,False,False,False,False,False,True,True,False]],[[False,False,True,False,False,False,False,False,False,True,False],[True,True,True,True,False,True,False,False,True,True,False],[True,True,True,False,True,True,True,False,True,True,True],[True,False,True,True,False,True,True,True,False,False,False],[True,False,False,False,False,False,True,True,True,True,False],[False,True,True,True,False,False,False,True,True,True,True],[False,False,True,False,True,False,False,False,True,True,False],[True,True,False,False,False,False,True,True,False,True,False],[False,False,False,False,False,False,True,False,True,True,False],[True,True,False,True,True,False,False,False,False,False,True],[False,False,False,False,True,True,True,False,False,True,False]],[[False,True,False,False,False,False,False,True,True,True,True],[True,False,False,True,True,True,True,True,False,True,True],[False,False,False,False,True,False,False,False,False,False,True],[False,True,True,True,True,False,False,False,True,True,False],[False,False,True,True,True,False,True,False,True,False,False],[True,False,True,True,False,True,True,False,False,False,True],[True,True,False,False,True,False,True,False,True,True,False],[False,False,True,True,False,True,False,False,False,False,False],[True,True,False,True,True,False,True,True,False,True,False],[False,True,True,True,False,True,False,False,True,False,False],[False,True,False,True,False,False,True,False,False,True,True]],[[False,False,False,True,True,True,True,False,True,True,True],[False,False,False,True,False,False,False,True,False,False,False],[True,False,False,True,True,False,False,False,False,False,False],[False,True,False,False,False,False,True,False,False,False,False],[False,True,True,False,False,False,False,False,False,True,False],[True,True,False,True,True,False,True,True,True,False,True],[True,False,True,True,True,True,True,True,False,True,True],[True,True,True,True,False,True,True,True,False,False,False],[False,False,True,False,True,True,True,True,False,False,True],[True,False,True,True,True,False,True,True,True,False,False],[False,True,False,False,False,False,False,True,False,False,True]],[[False,False,False,True,False,False,True,False,True,False,False],[False,True,False,True,False,True,False,False,True,True,True],[False,True,False,False,True,True,False,True,False,False,True],[False,True,True,False,False,False,False,True,False,False,False],[False,True,True,True,False,True,True,True,True,True,False],[True,True,True,False,True,False,False,False,True,False,True],[True,True,False,True,True,True,True,True,True,False,True],[False,True,True,False,False,False,True,True,False,False,False],[True,False,False,True,False,False,False,False,True,True,True],[True,False,False,False,False,False,False,False,True,False,True],[False,False,False,False,True,True,False,True,False,True,True]]], dtype = "bool")#candidate|12624|(7, 11, 11)|const|bool
const_12625 = relay.const([[[False,True,False,False,False,True,False,True,True,False,False],[True,False,False,True,False,True,False,False,True,False,False],[True,False,True,True,True,True,False,True,True,False,False],[True,False,False,True,False,False,False,True,False,True,True],[False,True,False,True,True,False,False,True,False,True,True],[True,False,True,True,False,False,False,False,False,False,False],[True,True,True,True,True,False,True,False,True,True,True],[True,False,False,True,False,False,True,True,True,True,True],[False,False,True,False,False,True,True,False,True,False,True],[False,True,False,False,False,True,False,True,False,True,True],[True,True,True,True,False,False,False,True,True,True,True]],[[False,True,False,True,False,False,False,False,False,True,True],[False,True,True,True,True,False,False,True,True,True,False],[False,False,False,False,False,False,True,True,True,True,True],[True,False,True,False,True,False,False,False,True,False,True],[True,False,True,True,False,False,True,True,False,True,True],[False,False,True,False,True,True,False,True,False,True,True],[True,True,False,True,True,False,True,False,False,False,False],[True,True,False,True,False,True,True,False,False,True,False],[True,False,True,False,False,False,False,True,False,False,True],[False,True,False,True,False,False,True,False,False,False,False],[False,True,False,True,False,False,True,True,False,True,True]],[[False,True,True,False,False,True,False,False,False,True,True],[False,False,False,True,True,False,True,True,False,False,False],[True,True,False,True,True,True,False,False,True,False,True],[False,False,True,True,True,True,True,False,True,False,False],[True,True,True,True,False,False,False,False,False,True,False],[False,False,True,True,False,True,False,False,False,True,True],[False,False,False,True,False,False,False,False,False,True,True],[True,True,True,True,True,False,True,False,False,True,False],[True,False,True,False,True,True,False,False,False,False,False],[False,False,False,False,False,False,False,False,True,True,True],[True,False,False,True,True,False,True,False,False,False,True]],[[True,False,False,True,False,False,True,True,False,False,True],[True,False,True,True,True,True,True,False,False,False,True],[False,True,False,False,False,True,True,False,False,False,False],[False,True,False,False,True,True,False,True,False,True,True],[False,True,False,True,False,True,False,False,False,False,True],[False,True,True,True,False,True,True,False,True,True,False],[True,True,True,True,False,False,True,True,True,True,False],[False,True,False,True,True,False,True,True,True,True,False],[False,True,False,True,False,True,False,False,True,False,True],[False,True,True,False,False,True,True,False,True,True,True],[False,False,False,False,True,True,False,True,False,False,False]],[[False,False,False,True,False,False,False,False,False,False,True],[True,False,False,False,False,False,False,True,True,False,False],[True,False,True,False,False,False,False,True,False,True,True],[True,False,True,True,True,False,True,True,True,True,False],[True,True,False,True,True,True,False,True,True,True,False],[True,False,False,True,False,True,False,True,False,True,False],[False,False,True,False,False,False,True,True,False,True,False],[False,False,False,False,True,True,True,False,True,False,False],[False,False,True,True,False,False,False,True,False,False,True],[True,False,True,False,True,False,False,False,True,True,True],[True,True,False,False,False,False,False,True,True,False,True]],[[False,True,True,False,True,False,True,True,True,False,True],[True,False,True,True,True,True,False,False,False,True,True],[False,False,True,True,False,False,False,False,True,False,True],[False,False,True,False,True,False,False,False,False,True,False],[True,False,True,False,True,True,True,False,False,True,False],[False,False,False,False,False,False,False,False,False,False,True],[True,True,False,True,True,False,True,False,True,False,False],[False,True,True,False,False,False,False,True,False,False,False],[True,True,False,True,True,True,True,True,False,False,False],[False,False,True,True,True,True,False,False,False,False,True],[True,False,True,True,True,False,False,True,False,True,False]],[[True,False,True,False,False,True,False,False,True,False,False],[True,True,False,False,True,False,False,False,True,False,False],[False,True,True,False,True,True,True,False,True,False,True],[True,False,True,False,False,True,True,False,False,False,False],[False,True,True,False,True,True,True,True,False,True,True],[True,True,False,False,False,True,False,False,False,True,False],[True,True,False,False,False,True,False,True,True,False,False],[False,False,True,False,True,True,False,False,False,True,False],[False,False,False,True,False,True,True,True,True,False,False],[False,True,False,True,True,True,False,False,True,False,False],[True,False,False,False,False,False,False,False,False,False,False]]], dtype = "bool")#candidate|12625|(7, 11, 11)|const|bool
bop_12626 = relay.logical_and(const_12624.astype('bool'), relay.reshape(const_12625.astype('bool'), relay.shape_of(const_12624))) # shape=(7, 11, 11)
output = relay.Tuple([bop_12626,])
output2 = relay.Tuple([bop_12626,])
func_12645 = relay.Function([], output)
mod['func_12645'] = func_12645
mod = relay.transform.InferType()(mod)
mutated_mod['func_12645'] = func_12645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12645_call = mutated_mod.get_global_var('func_12645')
call_12646 = func_12645_call()
output = call_12646
func_12647 = relay.Function([], output)
mutated_mod['func_12647'] = func_12647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8662_call = mod.get_global_var('func_8662')
func_8663_call = mutated_mod.get_global_var('func_8663')
call_12685 = func_8662_call()
call_12686 = func_8662_call()
output = relay.Tuple([call_12685,])
output2 = relay.Tuple([call_12686,])
func_12687 = relay.Function([], output)
mod['func_12687'] = func_12687
mod = relay.transform.InferType()(mod)
output = func_12687()
func_12688 = relay.Function([], output)
mutated_mod['func_12688'] = func_12688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_12714 = func_4144_call()
call_12715 = func_4144_call()
func_4144_call = mod.get_global_var('func_4144')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_12721 = func_4144_call()
call_12722 = func_4144_call()
output = relay.Tuple([call_12714,call_12721,])
output2 = relay.Tuple([call_12715,call_12722,])
func_12731 = relay.Function([], output)
mod['func_12731'] = func_12731
mod = relay.transform.InferType()(mod)
mutated_mod['func_12731'] = func_12731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12731_call = mutated_mod.get_global_var('func_12731')
call_12732 = func_12731_call()
output = call_12732
func_12733 = relay.Function([], output)
mutated_mod['func_12733'] = func_12733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12277_call = mod.get_global_var('func_12277')
func_12279_call = mutated_mod.get_global_var('func_12279')
call_12836 = relay.TupleGetItem(func_12277_call(), 0)
call_12837 = relay.TupleGetItem(func_12279_call(), 0)
output = call_12836
output2 = call_12837
func_12856 = relay.Function([], output)
mod['func_12856'] = func_12856
mod = relay.transform.InferType()(mod)
output = func_12856()
func_12857 = relay.Function([], output)
mutated_mod['func_12857'] = func_12857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mod.get_global_var('func_5272')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_12872 = relay.TupleGetItem(func_5272_call(), 2)
call_12873 = relay.TupleGetItem(func_5274_call(), 2)
func_7044_call = mod.get_global_var('func_7044')
func_7048_call = mutated_mod.get_global_var('func_7048')
var_12877 = relay.var("var_12877", dtype = "float32", shape = (11, 130))#candidate|12877|(11, 130)|var|float32
var_12878 = relay.var("var_12878", dtype = "bool", shape = (105, 3))#candidate|12878|(105, 3)|var|bool
call_12876 = relay.TupleGetItem(func_7044_call(relay.reshape(var_12877.astype('float32'), [1430,]), relay.reshape(var_12878.astype('bool'), [315,]), ), 4)
call_12879 = relay.TupleGetItem(func_7048_call(relay.reshape(var_12877.astype('float32'), [1430,]), relay.reshape(var_12878.astype('bool'), [315,]), ), 4)
output = relay.Tuple([call_12872,call_12876,var_12877,var_12878,])
output2 = relay.Tuple([call_12873,call_12879,var_12877,var_12878,])
func_12909 = relay.Function([var_12877,var_12878,], output)
mod['func_12909'] = func_12909
mod = relay.transform.InferType()(mod)
mutated_mod['func_12909'] = func_12909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12909_call = mutated_mod.get_global_var('func_12909')
var_12911 = relay.var("var_12911", dtype = "float32", shape = (11, 130))#candidate|12911|(11, 130)|var|float32
var_12912 = relay.var("var_12912", dtype = "bool", shape = (105, 3))#candidate|12912|(105, 3)|var|bool
call_12910 = func_12909_call(var_12911,var_12912,)
output = call_12910
func_12913 = relay.Function([var_12911,var_12912,], output)
mutated_mod['func_12913'] = func_12913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11430_call = mod.get_global_var('func_11430')
func_11431_call = mutated_mod.get_global_var('func_11431')
call_12915 = relay.TupleGetItem(func_11430_call(), 0)
call_12916 = relay.TupleGetItem(func_11431_call(), 0)
func_4656_call = mod.get_global_var('func_4656')
func_4657_call = mutated_mod.get_global_var('func_4657')
call_12927 = relay.TupleGetItem(func_4656_call(), 0)
call_12928 = relay.TupleGetItem(func_4657_call(), 0)
output = relay.Tuple([call_12915,call_12927,])
output2 = relay.Tuple([call_12916,call_12928,])
func_12929 = relay.Function([], output)
mod['func_12929'] = func_12929
mod = relay.transform.InferType()(mod)
mutated_mod['func_12929'] = func_12929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12929_call = mutated_mod.get_global_var('func_12929')
call_12930 = func_12929_call()
output = call_12930
func_12931 = relay.Function([], output)
mutated_mod['func_12931'] = func_12931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_12939 = relay.TupleGetItem(func_5157_call(), 0)
call_12940 = relay.TupleGetItem(func_5159_call(), 0)
func_4144_call = mod.get_global_var('func_4144')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_12945 = func_4144_call()
call_12946 = func_4144_call()
func_7914_call = mod.get_global_var('func_7914')
func_7916_call = mutated_mod.get_global_var('func_7916')
call_12961 = relay.TupleGetItem(func_7914_call(), 0)
call_12962 = relay.TupleGetItem(func_7916_call(), 0)
output = relay.Tuple([call_12939,call_12945,call_12961,])
output2 = relay.Tuple([call_12940,call_12946,call_12962,])
func_12974 = relay.Function([], output)
mod['func_12974'] = func_12974
mod = relay.transform.InferType()(mod)
mutated_mod['func_12974'] = func_12974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12974_call = mutated_mod.get_global_var('func_12974')
call_12975 = func_12974_call()
output = call_12975
func_12976 = relay.Function([], output)
mutated_mod['func_12976'] = func_12976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6715_call = mod.get_global_var('func_6715')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_12981 = relay.TupleGetItem(func_6715_call(), 2)
call_12982 = relay.TupleGetItem(func_6716_call(), 2)
func_3785_call = mod.get_global_var('func_3785')
func_3787_call = mutated_mod.get_global_var('func_3787')
call_12984 = relay.TupleGetItem(func_3785_call(), 0)
call_12985 = relay.TupleGetItem(func_3787_call(), 0)
func_3743_call = mod.get_global_var('func_3743')
func_3745_call = mutated_mod.get_global_var('func_3745')
call_13007 = relay.TupleGetItem(func_3743_call(), 2)
call_13008 = relay.TupleGetItem(func_3745_call(), 2)
func_8478_call = mod.get_global_var('func_8478')
func_8479_call = mutated_mod.get_global_var('func_8479')
call_13010 = relay.TupleGetItem(func_8478_call(), 5)
call_13011 = relay.TupleGetItem(func_8479_call(), 5)
func_12687_call = mod.get_global_var('func_12687')
func_12688_call = mutated_mod.get_global_var('func_12688')
call_13024 = relay.TupleGetItem(func_12687_call(), 0)
call_13025 = relay.TupleGetItem(func_12688_call(), 0)
var_13028 = relay.var("var_13028", dtype = "float64", shape = (780,))#candidate|13028|(780,)|var|float64
bop_13029 = relay.right_shift(call_13007.astype('int64'), relay.reshape(var_13028.astype('int64'), relay.shape_of(call_13007))) # shape=(780,)
bop_13032 = relay.right_shift(call_13008.astype('int64'), relay.reshape(var_13028.astype('int64'), relay.shape_of(call_13008))) # shape=(780,)
func_9149_call = mod.get_global_var('func_9149')
func_9150_call = mutated_mod.get_global_var('func_9150')
call_13037 = relay.TupleGetItem(func_9149_call(), 8)
call_13038 = relay.TupleGetItem(func_9150_call(), 8)
output = relay.Tuple([call_12981,call_12984,call_13010,call_13024,bop_13029,call_13037,])
output2 = relay.Tuple([call_12982,call_12985,call_13011,call_13025,bop_13032,call_13038,])
func_13043 = relay.Function([var_13028,], output)
mod['func_13043'] = func_13043
mod = relay.transform.InferType()(mod)
mutated_mod['func_13043'] = func_13043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13044 = relay.var("var_13044", dtype = "float64", shape = (780,))#candidate|13044|(780,)|var|float64
func_13043_call = mutated_mod.get_global_var('func_13043')
call_13045 = func_13043_call(var_13044)
output = call_13045
func_13046 = relay.Function([var_13044], output)
mutated_mod['func_13046'] = func_13046
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13075 = relay.var("var_13075", dtype = "int8", shape = (9, 3, 6))#candidate|13075|(9, 3, 6)|var|int8
const_13076 = relay.const([[[-9,-2,5,-9,1,7],[-5,-5,10,-5,-10,6],[8,-1,-2,9,-9,10]],[[-1,2,2,6,-10,10],[-4,3,-5,-9,-6,-2],[-7,-2,1,10,-2,6]],[[4,1,4,6,-8,5],[-7,-8,7,1,-2,2],[-4,5,-7,-10,-2,8]],[[4,-5,-2,-8,7,2],[-8,7,6,1,-4,-8],[7,3,-10,-7,-5,-1]],[[-5,6,4,5,2,10],[-3,-10,9,-7,5,-8],[-1,3,7,4,2,-3]],[[9,10,10,-9,-3,8],[-6,-8,7,8,-1,5],[-7,-10,-1,7,1,-3]],[[-7,3,-1,4,8,-8],[10,-2,-9,10,7,4],[3,10,-9,4,-5,-10]],[[8,2,7,-8,8,-9],[8,-4,9,5,-1,5],[-7,-10,4,9,-3,7]],[[-2,9,8,6,7,-2],[-10,-8,1,-3,-10,1],[2,-7,10,6,-10,2]]], dtype = "int8")#candidate|13076|(9, 3, 6)|const|int8
bop_13077 = relay.greater(var_13075.astype('bool'), relay.reshape(const_13076.astype('bool'), relay.shape_of(var_13075))) # shape=(9, 3, 6)
output = relay.Tuple([bop_13077,])
output2 = relay.Tuple([bop_13077,])
func_13081 = relay.Function([var_13075,], output)
mod['func_13081'] = func_13081
mod = relay.transform.InferType()(mod)
mutated_mod['func_13081'] = func_13081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13082 = relay.var("var_13082", dtype = "int8", shape = (9, 3, 6))#candidate|13082|(9, 3, 6)|var|int8
func_13081_call = mutated_mod.get_global_var('func_13081')
call_13083 = func_13081_call(var_13082)
output = call_13083
func_13084 = relay.Function([var_13082], output)
mutated_mod['func_13084'] = func_13084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7817_call = mod.get_global_var('func_7817')
func_7819_call = mutated_mod.get_global_var('func_7819')
call_13091 = relay.TupleGetItem(func_7817_call(), 0)
call_13092 = relay.TupleGetItem(func_7819_call(), 0)
output = call_13091
output2 = call_13092
func_13093 = relay.Function([], output)
mod['func_13093'] = func_13093
mod = relay.transform.InferType()(mod)
mutated_mod['func_13093'] = func_13093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13093_call = mutated_mod.get_global_var('func_13093')
call_13094 = func_13093_call()
output = call_13094
func_13095 = relay.Function([], output)
mutated_mod['func_13095'] = func_13095
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13152 = relay.var("var_13152", dtype = "float64", shape = (11, 5, 13))#candidate|13152|(11, 5, 13)|var|float64
uop_13153 = relay.atan(var_13152.astype('float64')) # shape=(11, 5, 13)
func_2835_call = mod.get_global_var('func_2835')
func_2836_call = mutated_mod.get_global_var('func_2836')
call_13155 = func_2835_call()
call_13156 = func_2835_call()
output = relay.Tuple([uop_13153,call_13155,])
output2 = relay.Tuple([uop_13153,call_13156,])
func_13163 = relay.Function([var_13152,], output)
mod['func_13163'] = func_13163
mod = relay.transform.InferType()(mod)
var_13164 = relay.var("var_13164", dtype = "float64", shape = (11, 5, 13))#candidate|13164|(11, 5, 13)|var|float64
output = func_13163(var_13164)
func_13165 = relay.Function([var_13164], output)
mutated_mod['func_13165'] = func_13165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7867_call = mod.get_global_var('func_7867')
func_7869_call = mutated_mod.get_global_var('func_7869')
call_13167 = relay.TupleGetItem(func_7867_call(), 0)
call_13168 = relay.TupleGetItem(func_7869_call(), 0)
func_7156_call = mod.get_global_var('func_7156')
func_7158_call = mutated_mod.get_global_var('func_7158')
var_13180 = relay.var("var_13180", dtype = "float32", shape = (770,))#candidate|13180|(770,)|var|float32
call_13179 = relay.TupleGetItem(func_7156_call(relay.reshape(var_13180.astype('float32'), [7, 10, 11])), 0)
call_13181 = relay.TupleGetItem(func_7158_call(relay.reshape(var_13180.astype('float32'), [7, 10, 11])), 0)
output = relay.Tuple([call_13167,call_13179,var_13180,])
output2 = relay.Tuple([call_13168,call_13181,var_13180,])
func_13187 = relay.Function([var_13180,], output)
mod['func_13187'] = func_13187
mod = relay.transform.InferType()(mod)
var_13188 = relay.var("var_13188", dtype = "float32", shape = (770,))#candidate|13188|(770,)|var|float32
output = func_13187(var_13188)
func_13189 = relay.Function([var_13188], output)
mutated_mod['func_13189'] = func_13189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8662_call = mod.get_global_var('func_8662')
func_8663_call = mutated_mod.get_global_var('func_8663')
call_13220 = func_8662_call()
call_13221 = func_8662_call()
output = call_13220
output2 = call_13221
func_13222 = relay.Function([], output)
mod['func_13222'] = func_13222
mod = relay.transform.InferType()(mod)
mutated_mod['func_13222'] = func_13222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13222_call = mutated_mod.get_global_var('func_13222')
call_13223 = func_13222_call()
output = call_13223
func_13224 = relay.Function([], output)
mutated_mod['func_13224'] = func_13224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13093_call = mod.get_global_var('func_13093')
func_13095_call = mutated_mod.get_global_var('func_13095')
call_13263 = func_13093_call()
call_13264 = func_13093_call()
func_2479_call = mod.get_global_var('func_2479')
func_2484_call = mutated_mod.get_global_var('func_2484')
const_13267 = relay.const([6.639429,-8.929104,-7.027662,3.221849,3.078007,-5.511353,-3.967101,8.748418,-0.412512,-1.415279,0.132857,-6.824606,-3.257626,-7.822434,-3.538256,-9.093466,5.298493,7.094320,5.299655,-4.496024,-9.763620,7.166767,-9.101881,-6.342876,-7.370842,-4.517726,-7.705863,3.095559,4.830295,-5.387548,0.035896,0.043598,0.979117,-9.078788,9.164583,1.090013,0.153507,-1.017658,4.058807,1.947850,-5.127628,-0.075890,-4.461576,8.958713,7.603072,3.377325,-7.631833,4.648985,6.497317,-8.724765,-2.521824,-8.384169,1.754287,4.947267,-1.199136,-9.761050,-3.707796,9.320592,-7.358807,-5.370446,4.249952,-2.703404,7.467293,3.891876,9.243987,3.704395,-3.745857,-1.327150,1.548301,-7.227703,-5.515390,-5.359814,3.183762,3.289446,-6.496086,-3.945521,5.280025,2.872849,-7.221196,6.848869,5.675227,-9.028756,-5.808787,1.063440,-3.440901,8.768603,-2.827040,-5.708470,-8.435630,2.588175,6.524364,-9.549541,4.987211,0.368381,-4.445876,5.180447,-2.464403,2.284102,-3.904774,-4.700220,7.216531,1.736085,8.927656,8.452305,3.485066,-0.218487,-7.033171,8.908406,-7.918643,-7.303604,7.008112,-4.254230,3.320003,1.932084,-5.059841,-5.865628,2.208939,2.947108,2.092915,-7.344018,-5.676667,-5.511663,0.273103,-7.769410,-6.267364,3.910233,-2.620943,2.614547,3.082750,-4.353037,-7.599068,3.443389,-4.323447,-1.164620,-1.536175,8.057052,1.650662,4.999495,7.246582,4.733206,-6.438155,-3.580830,-8.166279,-7.488088], dtype = "float64")#candidate|13267|(144,)|const|float64
var_13268 = relay.var("var_13268", dtype = "float64", shape = (130, 6))#candidate|13268|(130, 6)|var|float64
var_13269 = relay.var("var_13269", dtype = "float64", shape = (140,))#candidate|13269|(140,)|var|float64
call_13266 = relay.TupleGetItem(func_2479_call(relay.reshape(const_13267.astype('float64'), [144,]), relay.reshape(var_13268.astype('float64'), [390, 2]), relay.reshape(var_13269.astype('float64'), [5, 28]), ), 5)
call_13270 = relay.TupleGetItem(func_2484_call(relay.reshape(const_13267.astype('float64'), [144,]), relay.reshape(var_13268.astype('float64'), [390, 2]), relay.reshape(var_13269.astype('float64'), [5, 28]), ), 5)
func_11309_call = mod.get_global_var('func_11309')
func_11311_call = mutated_mod.get_global_var('func_11311')
call_13282 = relay.TupleGetItem(func_11309_call(relay.reshape(var_13268.astype('float64'), [780,])), 2)
call_13283 = relay.TupleGetItem(func_11311_call(relay.reshape(var_13268.astype('float64'), [780,])), 2)
func_8115_call = mod.get_global_var('func_8115')
func_8118_call = mutated_mod.get_global_var('func_8118')
call_13312 = relay.TupleGetItem(func_8115_call(relay.reshape(call_13282.astype('float64'), [780,])), 1)
call_13313 = relay.TupleGetItem(func_8118_call(relay.reshape(call_13282.astype('float64'), [780,])), 1)
output = relay.Tuple([call_13263,call_13266,const_13267,var_13268,var_13269,call_13282,call_13312,])
output2 = relay.Tuple([call_13264,call_13270,const_13267,var_13268,var_13269,call_13283,call_13313,])
func_13326 = relay.Function([var_13268,var_13269,], output)
mod['func_13326'] = func_13326
mod = relay.transform.InferType()(mod)
mutated_mod['func_13326'] = func_13326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13326_call = mutated_mod.get_global_var('func_13326')
var_13328 = relay.var("var_13328", dtype = "float64", shape = (130, 6))#candidate|13328|(130, 6)|var|float64
var_13329 = relay.var("var_13329", dtype = "float64", shape = (140,))#candidate|13329|(140,)|var|float64
call_13327 = func_13326_call(var_13328,var_13329,)
output = call_13327
func_13330 = relay.Function([var_13328,var_13329,], output)
mutated_mod['func_13330'] = func_13330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5414_call = mod.get_global_var('func_5414')
func_5416_call = mutated_mod.get_global_var('func_5416')
call_13419 = func_5414_call()
call_13420 = func_5414_call()
output = relay.Tuple([call_13419,])
output2 = relay.Tuple([call_13420,])
func_13432 = relay.Function([], output)
mod['func_13432'] = func_13432
mod = relay.transform.InferType()(mod)
mutated_mod['func_13432'] = func_13432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13432_call = mutated_mod.get_global_var('func_13432')
call_13433 = func_13432_call()
output = call_13433
func_13434 = relay.Function([], output)
mutated_mod['func_13434'] = func_13434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_13471 = relay.TupleGetItem(func_3064_call(), 0)
call_13472 = relay.TupleGetItem(func_3065_call(), 0)
func_10413_call = mod.get_global_var('func_10413')
func_10416_call = mutated_mod.get_global_var('func_10416')
const_13477 = relay.const(-1.604241, dtype = "float64")#candidate|13477|()|const|float64
var_13478 = relay.var("var_13478", dtype = "float64", shape = (60, 12))#candidate|13478|(60, 12)|var|float64
call_13476 = relay.TupleGetItem(func_10413_call(relay.reshape(const_13477.astype('float64'), []), relay.reshape(var_13478.astype('float64'), [720,]), ), 1)
call_13479 = relay.TupleGetItem(func_10416_call(relay.reshape(const_13477.astype('float64'), []), relay.reshape(var_13478.astype('float64'), [720,]), ), 1)
output = relay.Tuple([call_13471,call_13476,const_13477,var_13478,])
output2 = relay.Tuple([call_13472,call_13479,const_13477,var_13478,])
func_13481 = relay.Function([var_13478,], output)
mod['func_13481'] = func_13481
mod = relay.transform.InferType()(mod)
mutated_mod['func_13481'] = func_13481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13482 = relay.var("var_13482", dtype = "float64", shape = (60, 12))#candidate|13482|(60, 12)|var|float64
func_13481_call = mutated_mod.get_global_var('func_13481')
call_13483 = func_13481_call(var_13482)
output = call_13483
func_13484 = relay.Function([var_13482], output)
mutated_mod['func_13484'] = func_13484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8984_call = mod.get_global_var('func_8984')
func_8986_call = mutated_mod.get_global_var('func_8986')
call_13499 = relay.TupleGetItem(func_8984_call(), 2)
call_13500 = relay.TupleGetItem(func_8986_call(), 2)
func_6245_call = mod.get_global_var('func_6245')
func_6246_call = mutated_mod.get_global_var('func_6246')
call_13511 = relay.TupleGetItem(func_6245_call(), 1)
call_13512 = relay.TupleGetItem(func_6246_call(), 1)
output = relay.Tuple([call_13499,call_13511,])
output2 = relay.Tuple([call_13500,call_13512,])
func_13514 = relay.Function([], output)
mod['func_13514'] = func_13514
mod = relay.transform.InferType()(mod)
mutated_mod['func_13514'] = func_13514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13514_call = mutated_mod.get_global_var('func_13514')
call_13515 = func_13514_call()
output = call_13515
func_13516 = relay.Function([], output)
mutated_mod['func_13516'] = func_13516
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13622 = relay.var("var_13622", dtype = "uint16", shape = (3, 9, 3))#candidate|13622|(3, 9, 3)|var|uint16
var_13623 = relay.var("var_13623", dtype = "uint16", shape = (3, 9, 3))#candidate|13623|(3, 9, 3)|var|uint16
bop_13624 = relay.bitwise_or(var_13622.astype('uint16'), relay.reshape(var_13623.astype('uint16'), relay.shape_of(var_13622))) # shape=(3, 9, 3)
func_3095_call = mod.get_global_var('func_3095')
func_3097_call = mutated_mod.get_global_var('func_3097')
var_13630 = relay.var("var_13630", dtype = "float32", shape = (330,))#candidate|13630|(330,)|var|float32
call_13629 = func_3095_call(relay.reshape(var_13630.astype('float32'), [3, 10, 11]))
call_13631 = func_3095_call(relay.reshape(var_13630.astype('float32'), [3, 10, 11]))
output = relay.Tuple([bop_13624,call_13629,var_13630,])
output2 = relay.Tuple([bop_13624,call_13631,var_13630,])
func_13652 = relay.Function([var_13622,var_13623,var_13630,], output)
mod['func_13652'] = func_13652
mod = relay.transform.InferType()(mod)
var_13653 = relay.var("var_13653", dtype = "uint16", shape = (3, 9, 3))#candidate|13653|(3, 9, 3)|var|uint16
var_13654 = relay.var("var_13654", dtype = "uint16", shape = (3, 9, 3))#candidate|13654|(3, 9, 3)|var|uint16
var_13655 = relay.var("var_13655", dtype = "float32", shape = (330,))#candidate|13655|(330,)|var|float32
output = func_13652(var_13653,var_13654,var_13655,)
func_13656 = relay.Function([var_13653,var_13654,var_13655,], output)
mutated_mod['func_13656'] = func_13656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6030_call = mod.get_global_var('func_6030')
func_6032_call = mutated_mod.get_global_var('func_6032')
call_13709 = relay.TupleGetItem(func_6030_call(), 1)
call_13710 = relay.TupleGetItem(func_6032_call(), 1)
func_6817_call = mod.get_global_var('func_6817')
func_6818_call = mutated_mod.get_global_var('func_6818')
call_13713 = func_6817_call()
call_13714 = func_6817_call()
output = relay.Tuple([call_13709,call_13713,])
output2 = relay.Tuple([call_13710,call_13714,])
func_13717 = relay.Function([], output)
mod['func_13717'] = func_13717
mod = relay.transform.InferType()(mod)
output = func_13717()
func_13718 = relay.Function([], output)
mutated_mod['func_13718'] = func_13718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3086_call = mod.get_global_var('func_3086')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_13721 = relay.TupleGetItem(func_3086_call(), 1)
call_13722 = relay.TupleGetItem(func_3087_call(), 1)
output = call_13721
output2 = call_13722
func_13729 = relay.Function([], output)
mod['func_13729'] = func_13729
mod = relay.transform.InferType()(mod)
output = func_13729()
func_13730 = relay.Function([], output)
mutated_mod['func_13730'] = func_13730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10113_call = mod.get_global_var('func_10113')
func_10114_call = mutated_mod.get_global_var('func_10114')
call_13875 = func_10113_call()
call_13876 = func_10113_call()
func_12179_call = mod.get_global_var('func_12179')
func_12183_call = mutated_mod.get_global_var('func_12183')
var_13889 = relay.var("var_13889", dtype = "float64", shape = (780,))#candidate|13889|(780,)|var|float64
var_13890 = relay.var("var_13890", dtype = "float64", shape = (140,))#candidate|13890|(140,)|var|float64
call_13888 = relay.TupleGetItem(func_12179_call(relay.reshape(var_13889.astype('float64'), [780,]), relay.reshape(var_13890.astype('float64'), [140,]), ), 4)
call_13891 = relay.TupleGetItem(func_12183_call(relay.reshape(var_13889.astype('float64'), [780,]), relay.reshape(var_13890.astype('float64'), [140,]), ), 4)
func_5517_call = mod.get_global_var('func_5517')
func_5519_call = mutated_mod.get_global_var('func_5519')
call_13900 = relay.TupleGetItem(func_5517_call(), 0)
call_13901 = relay.TupleGetItem(func_5519_call(), 0)
func_9453_call = mod.get_global_var('func_9453')
func_9457_call = mutated_mod.get_global_var('func_9457')
var_13930 = relay.var("var_13930", dtype = "float32", shape = (630,))#candidate|13930|(630,)|var|float32
call_13929 = func_9453_call(relay.reshape(var_13930.astype('float32'), [9, 5, 14]), relay.reshape(var_13930.astype('float32'), [9, 5, 14]), )
call_13931 = func_9453_call(relay.reshape(var_13930.astype('float32'), [9, 5, 14]), relay.reshape(var_13930.astype('float32'), [9, 5, 14]), )
func_6842_call = mod.get_global_var('func_6842')
func_6844_call = mutated_mod.get_global_var('func_6844')
call_13945 = relay.TupleGetItem(func_6842_call(), 0)
call_13946 = relay.TupleGetItem(func_6844_call(), 0)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_13956 = relay.TupleGetItem(func_3268_call(), 0)
call_13957 = relay.TupleGetItem(func_3269_call(), 0)
func_9032_call = mod.get_global_var('func_9032')
func_9036_call = mutated_mod.get_global_var('func_9036')
const_13959 = relay.const([7.680943,4.258180,-1.314874,-2.715376,1.945254,1.210782,6.335850,-9.468048,-6.448381,6.699984,-7.931750,-1.171807,1.537744,-3.077172,-5.496701,-5.656353,-9.259966,2.194315,-9.340263,4.917365,6.324327,-0.514712,-7.248371,1.358238,-5.320164,8.258214,2.409811,-8.948748,-6.040963,9.794350,-5.723440,2.825402,3.819810,-9.306402,-2.862173,-9.457391,-1.712744,0.407342,3.759668,7.487709], dtype = "float64")#candidate|13959|(40,)|const|float64
const_13960 = relay.const([[8.372017,-4.519136,2.590875,-9.949758,0.436324,-2.930353,3.859177,6.645166,-3.458974,-8.530543,-5.313727,-5.379509,8.474928,-5.539384,-7.933756,-9.841176,-6.178838,-1.057862,-7.825379,-7.388730,1.326753,7.537123,4.879975,-1.685382,-3.356218,8.067927,-2.547526,-7.787708,7.082696,7.871523,-9.011372,4.391787,-6.316749,-6.750363,-1.451858,-5.222139,1.163149,-0.447062,-5.296072,6.227212,-2.810052,8.216186,-7.850706,-3.127769,9.387247,-3.960796,-1.792571,-3.738571,0.185692,7.806068,1.989611,7.358716,5.977644,4.406331,-7.434507,-0.965079,-1.590860,5.789014,0.488257,-7.959658,-6.040991,-8.325934,5.479964,6.013863,-0.545817,-5.648800,6.335441,-1.012335,-9.474711,-3.788680,-0.569428,8.146745,6.548324,-4.479941,-3.184980,3.725718,8.050737,6.342362,-8.522347,1.258297,4.548547,-7.315511,-8.688985,0.369193,-8.536696,0.321813,-6.715474,2.020375,-1.832369,1.296987,6.989057,7.502543,-8.926716,0.188908,7.000637,7.119631,-0.532350,2.789684,6.152748,4.112170,6.030478,-9.159576,0.784066,1.164323,1.435862,7.891560,8.563674,0.258139,5.190068,-5.665498,-2.786733,-8.853475,2.801162,8.361455,-7.988668,-3.120832,5.222804,-8.484301,3.750984,-0.641877,-5.971447,9.092124,-0.102583,2.322355,8.099866,1.514675,-7.940663,-5.509198,5.849710,-4.192222,3.560657,8.025886,0.779530,3.040327,9.592091,-2.459013,3.608564,9.090101,-4.673982,-8.451963,-8.390756,0.459328,1.943980,-3.966851,6.525156,-8.292994,-4.697294,-0.691268,8.246844,-1.132029,2.604937,-1.184038,-9.665476,0.476080,0.694665,-7.364329,0.547317,-6.229835,7.423006,5.906312,4.599285,0.196632,-8.148964,3.316850,-9.171941,-1.695189,-4.171896,-8.502092,8.343926,-1.202257,3.255839,-6.793558,-3.525618,1.965784,-8.345316,6.976175,2.621715,5.583442,-8.000121,3.270134,-7.934259,-0.471252,5.106839,8.981172,-2.490532,6.819408,-4.731230,-0.403807,-3.214100,-0.218906,9.360361,-7.044357,5.638861,-0.179022,-4.910369,-0.364789,9.718757,-6.955660,8.230544,8.678472,7.828905,-3.482656,2.412242,-8.690620,-0.086124,-2.249716,-1.688882,-2.036357,-4.712804,1.298301,0.509868,1.049705,9.989904,5.784679,3.889614,-7.721338,7.799983,-0.573955,-1.965859,-4.088809,9.923334,-5.913849,6.482871,5.521741,6.651882,-1.466585,-0.841122,3.156887,9.589603,3.823879,-8.011497,0.999886,-5.438171,-9.805017,2.071326,0.511382,0.083804,-9.180884,5.123450,-4.806970,1.024764,2.879629,-1.993010,0.652573,0.228987,-7.820243,-0.115987,9.836409,9.059537,5.613636,-7.422205,1.589364,-1.234410,-2.863928,-9.141457,-3.389891,7.728293,3.186748,8.134971,-0.968422,1.317511,-8.898849,-1.739849,-2.213039,7.681719,-9.398468,6.589371,8.954382,-7.319832,7.338653,-0.081083,-5.636569,7.096920,5.372782,-4.337785,3.523801,-9.859338,9.968784,0.805601,-5.146006,-4.199455,-3.854763,-7.510215,9.781287,8.205351,5.614150,5.577409,4.290712,-0.438165,6.190958,-1.907944,-9.831522,-5.081227,-4.105207,-2.811443,-8.105377,9.659189,-4.793559,-7.148328,-7.768926,-5.079695,7.828827,1.958938,-4.744496,9.644083,-2.674536,-8.001285,-1.887312,9.505812,-8.149794,6.420099,-3.762237,4.377214,-3.098767,-2.270542]], dtype = "float64")#candidate|13960|(1, 315)|const|float64
const_13961 = relay.const([-4.418929,6.589267,-7.643892,-0.723028,9.962995,6.343897,4.055872,-6.460663,-0.420027,-9.322437,-7.806144,7.204158,9.961840,-5.780797,-0.525871,7.154392,-7.617816,7.422386,6.495822,-0.866094,-9.947896,-7.638087,-1.465546,4.846478,-3.607497,1.323615,5.083661,-6.383110,-5.313167,4.745650,-3.479116,-2.774675,-2.543591,4.793573,2.797412,-9.356371,4.979093,-0.538871,6.587868,1.769810,1.648132,-6.414011,8.801059,-7.067003,2.214353,4.438182,-5.569675,4.178925,2.584717,6.998716,-0.529584,9.037830,-3.563018,9.619269,8.441870,-6.168373,9.223699,-4.952358,2.568700,-8.287407,-2.988583,-4.561586,2.885511,7.983860,-2.924157,-9.445616,-9.234728,-2.262498,5.622769,-6.935078,-6.615630,1.605896,-1.237101,2.376545,-3.194687,-1.064947,6.742036,-4.824244,-1.960473,1.277453,-9.841169,0.157854,1.419190,3.987012,7.236285,-3.869040,-6.783673,8.217748,1.917309,-2.089638,8.617177,-6.706254,7.013047,8.230452,2.082920,-0.032465,-3.520123,-2.508501,-0.459434,-7.081165,-2.113679,8.130889,7.351487,6.738586,3.763961,-2.276801,-8.072448,0.403740,2.578432,-9.901791,-5.665951,-6.760996,-2.410749,-1.838917,9.567866,3.835744,6.527557,-6.675260,8.887667,7.466685,-1.674082,4.286989,8.931896,-3.257957,-7.846125,1.132588,-1.884418,1.224671,-0.444912,5.855394,3.653823,0.856035,1.107119,0.228328,4.468303,-6.088043,-1.476058,9.920304,-7.889484,4.930002,-0.524756,0.651130,-3.832412,6.475233], dtype = "float64")#candidate|13961|(144,)|const|float64
call_13958 = relay.TupleGetItem(func_9032_call(relay.reshape(const_13959.astype('float64'), [40,]), relay.reshape(const_13960.astype('float64'), [315,]), relay.reshape(const_13961.astype('float64'), [144,]), ), 1)
call_13962 = relay.TupleGetItem(func_9036_call(relay.reshape(const_13959.astype('float64'), [40,]), relay.reshape(const_13960.astype('float64'), [315,]), relay.reshape(const_13961.astype('float64'), [144,]), ), 1)
const_13972 = relay.const([[[8.768217,2.309122,6.419711,-5.060677,6.975708,-5.070873,1.357414,-0.947630,9.166474,-3.159711,7.042283],[-0.694946,6.942813,3.268417,1.544233,5.635516,-4.173898,9.198300,7.143908,-2.445982,9.507425,-0.800617],[-7.024825,7.920601,-4.282032,4.680350,1.533622,-6.049097,-6.841516,-8.590103,-3.871933,0.366778,-4.905983],[3.118049,-5.249949,-9.854313,-4.491726,-4.504760,8.664333,2.169116,7.627495,9.946064,-9.251932,-2.890674],[0.007937,-8.259759,-1.756212,9.668926,2.871591,-1.383816,-9.064773,9.447431,-9.682173,-8.399376,7.943885],[4.616885,-4.293197,-3.154070,-5.828579,6.878040,0.787981,-8.055934,9.685564,-3.542789,-4.380550,9.244123],[4.440243,5.278021,-1.289126,-7.887814,7.666502,8.464746,-0.370236,5.934723,-3.976575,4.218299,-1.766693],[2.718975,9.825464,-9.596762,-8.511670,-5.616843,4.987218,9.638939,5.074892,7.790205,7.512833,-6.457190],[-0.045460,2.532185,0.316659,-2.471664,-8.477075,2.094193,3.512034,2.800595,9.886497,-8.926281,9.814571],[1.145382,4.742780,-1.351637,7.054117,-1.347927,-8.547805,-7.615188,-6.834541,2.867207,-1.492171,-4.057557]],[[3.928230,9.834045,-4.428721,6.162457,-0.641841,-4.155235,2.154008,-2.672057,-4.976856,7.958039,-4.751620],[-1.803922,-7.070692,8.689312,-7.936088,5.798832,3.155150,8.029909,-4.051878,-8.749617,1.309423,-9.148832],[1.090300,9.685286,5.183078,-2.765987,-4.650275,8.221476,-1.009363,9.701676,-8.533670,-2.505643,9.823489],[0.505433,-1.571414,-5.809022,0.905744,6.220586,-9.825131,-0.845358,6.254310,0.974131,7.795640,-5.289687],[-0.562013,-2.039606,-4.964828,-5.309073,-3.044447,6.668618,5.551545,-5.901032,-9.839509,9.139719,-8.391918],[6.219106,-1.959351,8.381134,2.162311,-5.439867,2.532493,-6.435743,0.565879,-2.614737,4.637710,4.022894],[6.298744,8.299528,8.561491,-4.333044,-2.251348,7.138969,7.671251,-6.158945,-3.884394,-2.714006,7.214843],[-1.375518,4.481420,1.597472,-4.148589,-5.031502,-3.315270,-1.148612,-8.915158,-6.081585,-1.248491,-1.971707],[-7.295447,-2.688222,1.478472,5.440724,5.224697,5.776909,-7.083247,7.462698,6.821117,-6.886871,2.907408],[5.753507,-0.216685,-6.432378,3.536610,-5.185850,0.676557,4.313421,1.732967,-1.242241,-0.142010,0.240732]],[[-9.211195,1.285586,-0.809181,7.782448,-9.846640,-6.392562,-2.066514,8.488735,7.149365,-4.420453,-4.851692],[5.395909,-3.267194,9.261939,2.641698,7.995769,7.426905,-5.330168,-8.964706,-7.794431,-8.524986,3.476338],[5.248404,3.869243,-4.750595,-6.206845,6.212961,-0.908461,4.702205,-0.156701,3.897251,-8.070445,-0.714985],[-2.283584,-2.452374,-0.499747,2.654307,-3.308892,-1.465626,6.248334,4.396018,-4.321418,5.190658,-2.852223],[-7.174182,-8.430744,-2.417647,-0.548432,2.168055,7.143093,0.869899,-5.714671,-7.766180,-4.284064,-7.638200],[7.432174,7.408319,-1.419655,0.827261,9.576909,0.175151,0.539970,-3.906062,6.065303,-4.004194,8.682430],[-4.228616,1.957813,-0.283141,7.265094,6.184958,-5.764901,-8.502254,-3.921354,9.403142,4.579488,0.811282],[-7.806855,4.125300,5.032762,8.004476,0.760971,-9.265596,-4.128120,-6.760606,-7.305581,-2.796266,-0.882524],[4.275766,-3.429215,-2.854079,-2.182900,-5.291375,2.142907,-4.147272,-4.517213,-3.229482,0.588905,-0.371146],[4.740471,1.296958,-7.491244,2.084479,5.246022,1.956625,7.890661,7.243032,8.112209,3.099074,0.874906]],[[5.591904,1.628063,-0.204876,2.049342,-8.666792,5.732459,-8.598528,6.931978,6.291298,-9.767769,0.811021],[-8.308855,1.769717,-1.784713,3.991295,-0.241316,8.641825,-6.530611,-2.182700,-1.311873,-4.937113,1.570081],[-9.661143,-5.201932,0.191565,-5.421274,0.026738,3.208705,0.832201,8.217444,-4.841006,6.129180,5.949956],[1.112487,9.838383,-2.982634,7.509029,-7.147259,-0.663862,0.922092,-9.426109,-4.074809,7.997424,-3.252735],[-8.818877,1.777737,-8.221310,-0.260972,-7.068599,2.955797,-5.015648,2.806019,8.164193,7.639747,9.042101],[9.513104,-2.060430,1.836589,-8.444074,-1.508156,0.732944,6.624805,1.457325,1.191959,3.801839,2.061551],[-9.527082,6.039200,0.896693,9.647792,-6.845516,-8.470908,5.395627,-5.623485,6.181225,-1.173029,-1.421329],[-4.095552,9.711424,7.851060,5.285323,-1.276700,2.217644,2.115350,-6.414508,4.461370,-1.425084,-8.188061],[9.897614,4.865070,5.815232,1.062291,3.725582,9.779631,5.834796,3.267502,-8.189603,-4.006562,6.578726],[-5.029276,9.357873,-6.276924,9.305009,1.409627,0.417517,0.713093,-3.496563,-6.964409,4.385951,-0.939484]],[[-4.031654,2.200703,-1.920823,7.499191,8.279285,6.693210,9.699522,-3.097299,-3.666869,-4.688613,-9.957767],[9.911406,-1.036847,-5.399013,9.159963,5.151629,-1.697983,-8.267196,-6.658262,9.815220,6.194881,-6.634712],[-5.605184,3.382839,-6.621745,1.028672,-5.214899,8.517125,-0.252306,-1.472977,4.180829,-9.770235,-0.828047],[-2.722829,-8.314343,-2.499290,-4.834942,-5.400725,-9.736972,-5.039586,7.498892,0.237600,-3.525490,8.678478],[9.971370,-2.505931,9.180438,-0.850123,-0.790813,-4.663938,-8.821864,-2.766902,-0.020927,-6.775160,4.087884],[7.624946,-0.619324,-0.293653,-8.652392,4.279731,5.621907,-2.892846,-0.473601,-9.815146,0.238585,0.995338],[0.947071,-6.818692,9.201614,-7.227564,8.002511,2.895738,8.070600,-8.777427,0.421112,5.378285,-2.166493],[5.874359,-9.743499,3.794762,7.727080,-2.737692,-7.714738,-9.011262,0.688036,-0.666099,-1.785735,-5.312772],[6.133018,2.653819,-3.907973,2.003163,-7.688988,-6.344928,-5.810089,-4.803303,-1.743752,3.957677,-2.557140],[-9.343071,-0.553443,-0.976799,9.854741,-5.298648,-3.884016,9.086405,-2.783984,5.834395,-8.332011,-4.887686]],[[3.702822,-4.926512,3.917103,-7.239520,7.456752,4.520306,-2.901537,-0.594255,-1.144011,-1.752255,7.251043],[8.708304,4.719153,-2.894376,-3.162456,-5.600627,-6.614829,-7.588088,-5.250340,9.878118,5.252809,-7.067830],[-5.970777,2.724261,4.585965,7.962277,-2.407362,0.530604,0.004365,9.320661,-3.696104,5.189452,-4.744979],[-9.334387,7.732544,-5.376120,-2.407758,-6.754614,5.215218,8.860710,8.674954,0.293174,8.362548,0.967052],[3.074760,4.395787,7.301622,-3.957779,-2.458023,-7.485171,-0.975621,-0.893311,4.600406,2.651247,4.031667],[-6.790274,-9.742170,-4.468416,-2.446211,-0.529636,-8.438812,6.817481,1.023418,4.635288,-6.223482,0.643077],[-8.392447,2.775438,-0.848070,-6.955232,3.672500,-9.512701,6.251242,1.617548,6.009057,3.781310,3.763831],[1.170129,-8.343498,-1.137808,-5.791930,2.599117,-6.502348,8.891700,2.362152,-4.846217,-4.936033,-5.690120],[4.994148,0.794175,-4.387716,-9.619898,7.078638,-3.852419,-0.298010,-1.927892,-5.583666,2.439970,-1.340896],[7.474974,-4.711665,-8.595419,-7.371669,-0.795928,-9.914513,-9.577703,-9.103275,2.809304,-7.599832,2.667775]],[[-7.447765,-3.463495,4.900466,7.818320,-7.584801,-5.282473,-6.852273,5.319007,0.531358,-1.162783,6.369901],[-6.812340,8.895810,4.781780,0.560812,-4.463418,-3.470599,-1.661344,-5.055661,8.012905,-3.802942,-9.646383],[-4.804082,-8.087639,5.691225,4.254384,2.492997,1.440098,4.750180,2.360371,3.994183,1.563934,-5.364958],[-1.621131,6.951890,0.043406,8.923086,8.597645,6.272596,2.484113,-0.446387,7.718415,0.646775,0.055519],[9.028187,8.675667,-8.525692,-4.256727,1.929978,-1.167839,-2.423146,-8.601154,7.952503,3.997977,2.636495],[0.337411,3.171313,-5.311319,3.437358,-2.552265,-5.025797,-7.145242,-9.107125,2.210654,1.928242,-2.334215],[9.532877,1.212520,-7.604062,3.799144,3.990505,-0.068341,4.342854,9.195906,-0.241014,3.242719,-0.434858],[6.842230,-8.880298,-7.889110,-1.053910,1.064518,9.848188,-8.979182,0.104440,-7.286577,7.294467,8.092146],[8.259353,2.156627,-7.232657,-5.071600,-3.224186,5.159476,-0.847118,-7.807648,8.958333,-7.599845,-9.533658],[-8.417633,-6.572411,9.889780,5.665238,-8.375077,5.519094,-2.825949,-5.346194,-6.061271,7.463891,7.091281]],[[3.424364,-5.820373,4.000162,-4.398092,-0.425055,7.828227,3.238410,-1.572725,1.096369,1.593566,-7.181197],[0.220994,-2.821604,-6.330881,1.650177,0.527915,1.286204,3.875394,-4.563983,3.598988,7.803388,7.232463],[2.319886,0.846659,-0.182495,7.257091,2.494067,0.037840,4.863916,6.619071,2.014244,4.418601,-2.954887],[1.887909,-5.880306,5.850289,1.607459,-0.111727,-8.588339,6.829567,-4.036991,-7.453828,4.952247,8.251460],[7.119453,-7.224452,7.883522,4.582060,-5.494372,-2.348182,3.105500,-8.939491,-3.729720,2.609907,1.286657],[1.345099,-9.483664,0.010092,6.631441,-0.636861,7.079417,1.500150,-2.067620,-0.124829,7.820387,-5.159764],[9.710840,3.223174,6.357096,-0.050794,-2.915730,4.331858,7.586114,-9.409261,2.148479,2.331055,8.268606],[-4.525155,-4.238971,9.507237,3.763197,-5.597228,-6.397461,8.328762,2.060512,-9.083030,1.764197,-9.619907],[-8.958150,-7.498168,5.271900,-7.266835,-5.262737,-2.096661,-9.304358,3.719835,2.202482,-6.257026,0.828574],[-7.463785,6.634823,-0.562587,-9.485317,-7.406590,-5.418966,-6.478516,-3.080147,-7.777284,7.471211,0.325175]],[[-0.733766,-7.387999,5.443083,-5.243899,-9.357413,5.434730,8.558278,-4.463769,-6.100346,0.098593,6.751801],[-7.490558,-7.669820,1.870869,9.282882,8.027592,2.004099,-1.200426,-7.280636,1.658199,8.020218,0.107667],[6.549147,-6.203669,-3.323206,-8.251030,8.096550,8.066019,2.564772,-4.005365,-3.873707,1.009992,2.643022],[-0.759843,-9.616656,-5.118477,-4.542948,-6.648794,4.286448,6.650582,-2.869724,-3.488844,-9.395258,-7.325348],[-7.141787,-2.329319,-0.040872,-2.750401,6.799280,-3.230826,-7.427775,9.849693,-9.148750,-0.211888,-1.016076],[8.076254,0.912515,9.398668,1.602977,-3.229710,-4.571264,-3.136160,-0.633346,-9.292649,7.065215,3.271522],[0.695860,-8.187520,-0.913709,4.941483,-1.745542,-7.260262,-4.035889,1.113510,0.182207,1.196882,5.869365],[-8.590816,-8.666149,2.579302,4.860082,-7.571529,-1.009823,-3.394651,3.049453,9.650377,-8.470961,-8.077579],[6.136134,0.203523,0.795986,-1.087087,-7.633414,-5.814134,4.429476,2.851165,-1.358844,1.769139,-9.835122],[8.260598,-2.522672,-3.105755,-6.541669,1.104252,-4.136541,-1.155033,-0.828876,-5.858195,-8.385938,3.988336]]], dtype = "float32")#candidate|13972|(9, 10, 11)|const|float32
bop_13973 = relay.logical_xor(call_13875.astype('int32'), const_13972.astype('int32')) # shape=(9, 10, 11)
bop_13976 = relay.logical_xor(call_13876.astype('int32'), const_13972.astype('int32')) # shape=(9, 10, 11)
output = relay.Tuple([call_13888,var_13889,var_13890,call_13900,call_13929,var_13930,call_13945,call_13956,call_13958,const_13959,const_13960,const_13961,bop_13973,])
output2 = relay.Tuple([call_13891,var_13889,var_13890,call_13901,call_13931,var_13930,call_13946,call_13957,call_13962,const_13959,const_13960,const_13961,bop_13976,])
func_13997 = relay.Function([var_13889,var_13890,var_13930,], output)
mod['func_13997'] = func_13997
mod = relay.transform.InferType()(mod)
var_13998 = relay.var("var_13998", dtype = "float64", shape = (780,))#candidate|13998|(780,)|var|float64
var_13999 = relay.var("var_13999", dtype = "float64", shape = (140,))#candidate|13999|(140,)|var|float64
var_14000 = relay.var("var_14000", dtype = "float32", shape = (630,))#candidate|14000|(630,)|var|float32
output = func_13997(var_13998,var_13999,var_14000,)
func_14001 = relay.Function([var_13998,var_13999,var_14000,], output)
mutated_mod['func_14001'] = func_14001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13729_call = mod.get_global_var('func_13729')
func_13730_call = mutated_mod.get_global_var('func_13730')
call_14006 = func_13729_call()
call_14007 = func_13729_call()
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_14010 = relay.TupleGetItem(func_5157_call(), 0)
call_14011 = relay.TupleGetItem(func_5159_call(), 0)
func_12909_call = mod.get_global_var('func_12909')
func_12913_call = mutated_mod.get_global_var('func_12913')
const_14013 = relay.const([4.096209,2.396513,6.843609,5.105523,1.877931,0.752242,8.695647,-4.484692,-6.815304,4.553718,-3.834586,6.313412,-7.491347,3.906887,8.075508,9.365661,-8.413847,6.311481,-1.833859,8.614632,0.775593,-3.659920,-2.398646,-4.444873,2.353176,-9.610688,-0.884755,-3.800023,5.048192,-3.431998,2.757454,6.647272,-1.586216,3.774586,6.094199,-1.090826,-9.350563,3.590268,-1.583457,8.177814,5.361146,6.492419,8.625089,-3.458275,6.007714,5.165370,-7.685980,8.601099,-1.383455,3.278905,5.874063,-1.444032,7.159400,-2.512859,7.901073,5.734955,-4.611514,-1.397571,-3.571007,-2.263646,1.606042,0.365031,2.852826,-0.636439,9.220211,9.682843,-2.742985,-9.801536,-7.558103,1.798098,-8.760990,-8.486646,2.140966,7.404672,-4.171026,2.189829,9.013379,5.012873,7.452646,-4.543200,-9.064032,0.225316,-1.168280,-7.347939,8.136467,-9.708541,-0.521343,-7.449422,-2.117140,1.215923,3.833213,-9.334225,0.893468,3.310746,-1.672223,-9.093400,-9.383672,4.560480,0.795895,4.711602,2.039368,5.944109,-5.815840,0.803268,1.949509,5.538759,9.743657,4.935578,-1.811735,-2.930455,1.493036,9.178717,-8.896781,-2.780930,-7.547968,-6.159815,9.460524,9.150091,5.210667,-8.163782,3.569101,-6.356083,-5.803527,-9.949152,-5.936182,0.696956,8.349916,9.857183,0.011775,1.865985,3.289830,1.142986,9.417761,5.326942,9.395553,5.024595,1.939374,6.379031,-8.869357,-9.067402,-5.719339,-1.779024,-6.082966,-0.035550,0.046996,1.824584,4.518270,2.352502,8.070767,-7.528711,3.088820,-9.390470,6.244412,-9.205467,0.964333,-5.631566,-4.051436,1.382483,8.710280,-1.253214,1.824979,4.460840,-3.983395,-7.754887,7.434384,-1.384803,-4.038962,-0.432397,-5.718346,7.546781,2.602740,-1.308817,-7.677929,8.272421,5.348909,-1.476588,2.697506,8.155775,5.412824,-1.031568,-2.783942,2.675249,1.985829,-5.749281,-5.686386,2.386370,-0.612922,7.412537,2.845718,-9.198690,-3.483455,4.332821,-4.131654,3.485616,-5.567930,1.393130,-7.069372,-6.329887,-6.893686,4.647580,-5.886152,-2.430798,-5.545583,-7.481473,-3.228883,-3.376578,7.177268,8.151400,5.664309,0.590205,-4.308203,-5.919759,2.551647,-4.513943,-1.148122,-6.893925,-0.125380,7.826575,-5.039194,-8.554840,-6.719936,4.934178,-0.115598,0.407847,9.908979,-5.183696,6.150143,-6.243356,8.922695,-8.343183,4.776858,-5.718841,-8.322678,-6.061904,5.706734,0.526563,-8.920078,-6.126533,7.326335,-0.759050,-8.528968,-9.723659,6.987984,3.593301,1.144485,-6.373135,-6.066057,-0.527394,-3.312202,-3.572378,5.485465,6.227890,-1.108842,2.126638,-2.928678,6.099041,-1.051542,-7.997846,-0.701541,-5.094314,-7.353818,-5.975396,2.135029,4.643953,-3.654024,-0.592053,6.668309,9.707287,9.879710,-6.902884,-1.264238,-8.554530,1.082876,-0.309313,-8.049224,-6.169455,-4.539055,-7.181108,4.135699,9.299341,6.330043,-4.920661,-4.164312,-0.663156,-0.094973,0.242833,-5.991978,9.854864,-7.327355,-0.198535,-9.448814,4.660965,0.371145,-7.696757,3.110597,-5.031796,8.457483,-3.250152,-2.805257,4.570660,6.240579,0.154422,1.005480,4.230217,1.247114,-6.723345,-6.663391,-6.192529,3.740621,1.829848,-8.721228,7.462434,-1.635269,6.951247,1.384328,9.465323,4.114776,-9.371355,1.188339,1.766528,8.291674,-9.756100,2.373957,-8.441585,5.756182,-6.046690,8.262517,-1.717611,8.478403,4.918154,-5.317375,7.390697,9.710314,-7.410130,1.367498,4.478191,-6.942982,1.992327,-0.893292,-2.664673,7.735497,-6.021779,1.984488,-5.502858,-7.876728,0.395352,-8.405025,1.872522,-8.125008,-2.498719,6.874466,8.985761,4.451276,5.790865,-9.815206,7.137267,-0.929307,-2.483715,-0.591839,-8.856192,-7.848939,-4.094357,-3.765758,8.432850,7.254818,7.115969,3.850312,-5.273711,0.131783,8.375562,-6.656984,9.035181,-4.099316,-4.561904,-1.511004,1.461386,-1.754522,5.687112,8.132616,7.786103,-0.602668,9.479841,1.503734,-7.960104,-6.752888,-6.327944,-3.650644,2.268709,-0.319020,-0.157285,2.942716,2.412585,7.406686,-8.882405,9.307848,3.385463,-6.847896,-5.076098,4.603262,-7.250967,-3.053591,-3.315944,-8.513497,1.743179,8.958004,0.173547,6.100898,-8.237338,1.577472,-3.135292,-6.006623,-1.836640,-3.033356,9.375229,9.167899,4.152859,-4.219940,3.476680,-5.854166,1.373477,-2.556664,-9.273031,-7.939109,-9.425096,6.046813,-3.643257,-5.245029,2.183142,9.827491,-7.523667,-4.326791,-1.213757,4.295234,-9.030766,-9.028124,5.178771,-8.112958,4.357535,-9.664669,6.967537,-1.674312,-3.468200,-3.652485,3.079702,-7.866998,3.455745,-8.235208,6.102947,6.780613,5.773519,-1.811393,-7.881960,-1.010284,5.348606,7.635835,-1.001162,-5.986459,-2.442680,-0.065953,6.466900,-9.374567,-4.976636,-8.068012,-2.197661,4.915378,-2.235435,5.060686,-6.910352,-3.112820,-6.807477,-6.049651,0.324005,5.635479,-0.795129,1.748269,-2.255792,-3.363478,-3.781015,8.759812,-6.586166,-2.789492,-9.619220,7.547050,7.994241,-2.873792,1.935779,2.530915,1.177086,-9.977692,-6.805701,1.197011,0.725891,8.785668,9.791777,6.780974,8.413344,-4.358556,6.452384,7.812782,2.417539,-5.421426,-2.845602,8.592177,1.706564,9.921850,1.166518,-7.404728,-0.540895,3.333649,-9.725605,5.580413,-2.798400,9.294925,8.292419,6.050520,-9.420313,8.051604,6.993120,1.488119,7.686977,-3.313123,7.964111,9.121961,1.761168,5.587512,9.588747,4.642394,-4.998189,4.088108,6.689282,-8.152401,2.744277,9.965419,-7.559045,1.144879,5.919709,6.604654,-3.814189,5.890209,0.599194,-6.299395,1.523379,-0.179415,-2.782136,-6.998532,-6.807481,-0.204204,-4.247537,-5.392947,-3.454404,-4.112658,-2.809041,-6.027280,2.753816,-7.526977,9.897864,0.478504,-3.283653,-7.322061,-2.073689,3.667111,-9.926580,-0.613205,7.100654,7.526540,-6.837508,1.971782,0.398766,6.402503,0.903443,6.497740,-5.321834,-3.219630,0.433800,-6.828757,0.350253,-2.182858,5.757739,-4.299962,-8.745908,-6.788281,-4.368375,1.287603,9.161499,-5.913480,-7.763866,0.723746,-5.964671,0.287730,6.470866,3.816859,2.748679,-1.943386,-5.601591,9.840543,-8.530415,6.961783,-3.457144,8.562901,-8.983304,-6.805984,7.811390,6.347618,4.801048,5.045358,-9.726621,1.956721,2.310028,-0.807263,6.756876,-8.600055,3.566616,-5.266571,-7.453433,-3.969498,8.671971,8.790939,-7.190690,-6.308428,1.827481,-5.422863,6.883842,-0.924492,9.813978,-4.729707,-7.755323,3.274760,0.657937,6.310589,4.113343,-6.592750,7.641978,0.555051,-0.491393,0.732912,-4.182010,-6.224515,-6.441796,-0.564233,5.999557,-4.474232,4.540413,-0.923750,0.798513,-5.195156,9.578098,6.171892,-3.774656,-5.746693,-5.587981,-9.784241,-5.911992,-1.613480,5.775395,-3.695540,-9.683464,4.789620,-3.922200,-4.686620,0.507687,-8.232061,0.374889,1.685506,5.682637,-8.891579,-9.975263,-6.634355,7.846693,7.940450,4.680818,-4.766738,-9.421710,3.920796,4.215975,-1.769193,-1.518651,5.043046,-3.115969,4.851378,-4.364414,6.637315,-1.648310,0.047961,4.101591,1.007428,4.990711,-1.497644,2.480727,-5.835578,2.942287,8.852195,-5.079317,8.851131,-9.368685,-5.625434,-9.681914,3.514020,8.154842,6.592490,0.901166,6.974020,-7.389179,-6.542503,1.634805,-9.712738,7.375646,-2.112781,-1.619566,-2.954576,-5.328124,9.589474,-5.540324,5.462197,-3.495051,-4.538915,3.654626,-5.494654,7.141961,6.681928,3.877969,2.065423,-6.911145,-4.398623,7.670111,1.784178,8.695574,0.761991,1.855473,7.005373,5.319530,1.125946,9.831311,-7.781382,-9.160313,2.000332,9.633032,-9.006268,-1.038172,-4.185004,7.327742,6.948588,-3.867668,-5.366507,-0.866962,9.861236,-1.910894,-1.495832,-5.535267,-9.982601,6.978634,2.926776,9.940833,-1.605816,-4.003342,6.136498,-9.522775,7.282244,0.485030,-5.114779,2.149114,0.092298,-5.791141,-8.203656,-6.064683,1.010871,-3.675017,-8.726226,-0.321734,-3.605740,7.029921,-1.590007,-2.822992,1.197202,0.621390,2.157866,7.975590,-8.806545,5.234216,6.474256,-3.103422,3.745428,2.630308,-2.714457,-2.172551,-9.579650,-3.648501,6.884631,-1.835965,7.921395,-9.427630,4.801031,0.793756,7.972019,-9.608683,0.372184,6.925635,7.750809,-5.658747,-2.977191,-8.067891,3.304838,8.868891,-4.277140,0.502107,8.202030,-4.905960,5.145427,6.090296,-9.871454,3.850760,-1.298292,-9.405919,0.977294,8.535692,3.449593,5.558145,-3.512152,1.366507,-7.561414,-1.725909,-2.982961,-9.682721,2.761743,-3.456509,8.499732,1.472599,-9.209233,-9.973669,-3.972325,9.449530,4.801646,-9.431350,7.753560,-6.154673,-9.654003,-5.613295,-5.335597,7.247351,-9.386957,7.929433,5.195689,5.784433,4.504581,-4.910809,7.168624,8.396890,-1.986669,-4.160946,-9.143390,8.821424,-2.511068,8.195477,1.376040,-8.184486,2.755813,3.169592,-4.596693,-4.545216,-9.249585,1.215155,3.594943,2.704762,1.750380,8.798345,-1.315311,-6.581552,-1.788739,0.402213,-7.207419,9.269950,-8.341023,0.623617,9.576345,-6.843457,-7.850835,9.248944,-3.769788,1.037467,7.446748,7.425061,5.086342,-5.839304,-2.633642,8.709255,7.552009,-0.415019,-9.142458,-8.544287,9.455415,0.999122,-4.381031,9.267898,4.399994,-4.075635,-3.893037,0.079247,-0.277998,8.403289,3.824559,3.926851,-9.239653,-2.588763,5.706678,-2.826882,6.512213,-8.028871,1.944099,4.525960,-4.902770,6.679375,4.451560,6.924494,-2.809499,-6.805774,3.583753,-7.814657,5.552229,-8.358385,3.710122,-3.368738,8.430096,-8.078891,-0.612077,7.128656,-8.988392,7.128043,1.454516,9.604790,-6.518636,-7.397225,5.432155,1.190196,6.409845,-3.504558,-7.626279,-6.485012,3.898296,-8.020001,-5.182754,6.410869,-1.569985,-4.095810,7.687484,3.719043,-5.219610,4.517493,-5.077534,-9.266031,1.140936,-8.628519,1.948481,8.213277,-5.907718,4.350932,6.887555,3.740822,8.384194,-3.166968,9.343846,-6.498702,5.827700,4.398964,-1.951637,8.240937,-2.315012,-8.630210,-0.316286,2.096093,9.526317,0.537052,3.555360,4.740665,4.320800,4.785165,8.853702,-4.310468,5.007947,7.412420,9.474872,4.903053,-8.107425,-5.711704,3.463139,5.989277,-7.419351,-2.129322,5.405542,-8.325601,1.842187,8.158759,-1.188428,8.438647,-5.570351,8.199600,1.103247,1.256580,-7.682464,8.527098,1.799064,1.596593,0.694420,0.072746,6.718437,8.274879,4.456058,5.778823,-0.869121,-2.408757,3.685354,8.866410,-2.667521,2.887714,-5.629062,8.321812,0.451139,8.538063,-0.809163,-8.391091,-6.020083,-8.327457,-6.891934,0.341416,-0.179397,3.001043,-6.240291,-5.877861,-9.757221,0.363968,-6.637734,-0.407547,0.195172,6.028513,4.900881,4.345297,6.632617,1.618007,-9.323734,4.287846,-1.048230,-1.512945,3.647877,-4.200500,-1.425813,-2.975246,-2.570756,1.397295,-6.418042,5.293555,-5.581599,2.343604,-1.851082,2.817492,-5.435575,5.878114,-2.957606,1.105396,-8.140490,4.936030,0.499236,-1.297087,-0.984435,-8.517590,-5.237628,-9.928619,-8.689343,-9.216217,0.504428,9.344752,-0.268377,-2.292928,4.875301,-1.874987,8.406549,-6.194688,9.292749,-1.706727,-4.819393,-4.462007,-3.597662,4.373124,1.057596,7.149439,-8.515491,-5.651131,8.191539,5.564886,-5.618743,8.419010,1.064623,-4.011657,-9.229292,-2.436286,2.444103,8.392052,-5.479312,0.427312,-9.865283,-7.828884,2.709999,-9.007721,0.713165,9.994206,3.066616,-1.232391,9.755128,-1.395975,5.925898,-2.302035,4.731180,6.684916,4.827756,9.811462,3.535648,-5.119457,-6.327475,-6.135890,-3.306247,0.213290,-8.184967,-1.887279,8.852085,9.170462,0.291373,3.098231,0.003395,-0.559002,9.207991,-5.281469,1.915593,-5.953239,6.370434,-1.462561,-4.233374,-8.860843,9.397518,-6.058585,2.550725,9.020631,-9.500093,3.231446,5.145149,-4.364060,-4.907285,-9.076568,8.161785,3.752472,4.953846,-7.051501,-3.875791,-7.205644,4.006122,-1.967279,-7.259745,8.916636,-9.779017,-7.981970,2.779065,9.918648,0.271153,8.239298,-2.637712,-0.743400,-3.407557,9.429481,9.535400,-8.187924,7.349423,6.573675,8.478746,-9.650591,3.402078,3.054640,4.452724,-9.627760,-4.333252,2.296664,7.154257,-4.793301,-3.660298,-5.401301,7.701863,-8.804564,7.143331,-5.954607,-4.839977,-6.218788,0.916906,-8.707105,-1.887298,-2.916531,1.052024,8.462484,5.764101,-3.827189,-6.592455,9.659282,-0.843568,-0.432053,5.218776,-1.101085,0.747078,1.134383,-3.195661,7.889556,9.910173,-8.680234,6.454665,0.181401,6.514204,-6.550722,-0.314839,-7.240889,5.000999,-7.233591,9.990403,-4.740069,4.641357,-7.400901,-8.737291,4.224661,9.010924,-6.243004,9.136215,7.671665,1.026488,-9.811132,7.159505,-6.887699,0.897284,0.347149,3.050403,8.898333,5.173015,8.558295,7.770597,0.363766,-9.085272,5.156215,6.774090,-7.071467,-4.967585,-8.340156,3.499070,-5.446495,5.463320,-6.469621,-9.913475,-0.215729,7.941437,4.080566,-7.075004,4.921275,-6.003878,-1.821756,1.376861,-2.223403,-5.980279,4.560361,-2.890912,-1.806338,7.354534,-1.313582,5.379361,6.790500,-1.336631,2.619437,-2.351639,4.486147,-2.761852,-7.952132,1.840770,6.550437,-6.080625,9.686370,7.037053,-3.684735,-3.132360,-7.883023,2.662181,-4.365820,-1.230853,-2.868916,-2.942860,1.489808,-5.545690,-1.564798,-8.587574,7.806883,-8.984426,4.384887,-2.565407,-6.498407,1.124849,-0.726262,6.172725,-6.639915,7.707084,-3.166422,9.228125,-5.510602,5.279751,3.321407,-8.730478,-0.935737,3.201166,-1.084881,-5.311484,9.869085,0.625702,-4.532654,-2.684900,-3.254117,-1.852314,-7.220021,-2.094466,7.323569,7.715894,-9.181574,2.734382,6.698497,-6.514487,-4.729309,-8.145773,-0.174225,-4.892873,-6.478075,-2.787359,-8.166381,2.190585,-6.239451,0.722126,-2.254036,-7.247647,-6.547002,0.496208,-2.542915,-8.763761,-9.129995,-0.073770,-4.433546,-2.230510,-2.092851,-5.051233,1.159765,7.009133,6.264022,4.244032,0.726744,-2.373320,6.807346,3.796463,-3.495816,-7.886997,2.636475,8.120434,5.720086,-9.190474,-4.182365,-9.911560,8.665489,2.079751,-4.853986,-9.561897,-1.502604,-3.864836,-3.319509,-4.656691,5.108963,-0.166940,1.364370,-7.265349,0.938126,-0.938666,5.151582,6.403500,-0.464722,-5.058825,3.257385,2.450564,5.190002,3.711963,5.539047,-0.135205,-2.299572,0.962644,8.024765,9.105911,2.404083,-4.019588,-2.002128,9.952009,7.639990,-8.232964,-6.988911,-7.515763,3.240734,8.866659,0.160367,1.285325,-9.817670,-2.895843,-9.183919,-0.215077,3.064188,7.871523,-2.884882,0.021249,-8.508817,-6.019214,8.244716,-1.293483,-3.873424,2.369466,-2.001616,-5.868237,-8.418236,-0.053979,-8.631539,-7.811210,0.945077,8.415166,-6.364356,1.057913,-7.692630,3.814152,3.131303,-5.262558,8.034401,5.012891,-0.291540], dtype = "float32")#candidate|14013|(1430,)|const|float32
const_14014 = relay.const([[True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True],[True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False],[False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,True,False,True,False],[True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True],[True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True]], dtype = "bool")#candidate|14014|(5, 63)|const|bool
call_14012 = relay.TupleGetItem(func_12909_call(relay.reshape(const_14013.astype('float32'), [11, 130]), relay.reshape(const_14014.astype('bool'), [105, 3]), ), 1)
call_14015 = relay.TupleGetItem(func_12913_call(relay.reshape(const_14013.astype('float32'), [11, 130]), relay.reshape(const_14014.astype('bool'), [105, 3]), ), 1)
func_13514_call = mod.get_global_var('func_13514')
func_13516_call = mutated_mod.get_global_var('func_13516')
call_14019 = relay.TupleGetItem(func_13514_call(), 1)
call_14020 = relay.TupleGetItem(func_13516_call(), 1)
func_11504_call = mod.get_global_var('func_11504')
func_11506_call = mutated_mod.get_global_var('func_11506')
call_14026 = relay.TupleGetItem(func_11504_call(), 0)
call_14027 = relay.TupleGetItem(func_11506_call(), 0)
output = relay.Tuple([call_14006,call_14010,call_14012,const_14013,const_14014,call_14019,call_14026,])
output2 = relay.Tuple([call_14007,call_14011,call_14015,const_14013,const_14014,call_14020,call_14027,])
func_14033 = relay.Function([], output)
mod['func_14033'] = func_14033
mod = relay.transform.InferType()(mod)
output = func_14033()
func_14034 = relay.Function([], output)
mutated_mod['func_14034'] = func_14034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6390_call = mod.get_global_var('func_6390')
func_6392_call = mutated_mod.get_global_var('func_6392')
call_14035 = relay.TupleGetItem(func_6390_call(), 1)
call_14036 = relay.TupleGetItem(func_6392_call(), 1)
output = call_14035
output2 = call_14036
func_14043 = relay.Function([], output)
mod['func_14043'] = func_14043
mod = relay.transform.InferType()(mod)
mutated_mod['func_14043'] = func_14043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14043_call = mutated_mod.get_global_var('func_14043')
call_14044 = func_14043_call()
output = call_14044
func_14045 = relay.Function([], output)
mutated_mod['func_14045'] = func_14045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_14066 = relay.TupleGetItem(func_3161_call(), 0)
call_14067 = relay.TupleGetItem(func_3162_call(), 0)
output = relay.Tuple([call_14066,])
output2 = relay.Tuple([call_14067,])
func_14113 = relay.Function([], output)
mod['func_14113'] = func_14113
mod = relay.transform.InferType()(mod)
output = func_14113()
func_14114 = relay.Function([], output)
mutated_mod['func_14114'] = func_14114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13514_call = mod.get_global_var('func_13514')
func_13516_call = mutated_mod.get_global_var('func_13516')
call_14136 = relay.TupleGetItem(func_13514_call(), 0)
call_14137 = relay.TupleGetItem(func_13516_call(), 0)
output = relay.Tuple([call_14136,])
output2 = relay.Tuple([call_14137,])
func_14157 = relay.Function([], output)
mod['func_14157'] = func_14157
mod = relay.transform.InferType()(mod)
output = func_14157()
func_14158 = relay.Function([], output)
mutated_mod['func_14158'] = func_14158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14192 = relay.var("var_14192", dtype = "float64", shape = (6, 9, 7))#candidate|14192|(6, 9, 7)|var|float64
var_14193 = relay.var("var_14193", dtype = "float64", shape = (6, 9, 7))#candidate|14193|(6, 9, 7)|var|float64
bop_14194 = relay.divide(var_14192.astype('float64'), relay.reshape(var_14193.astype('float64'), relay.shape_of(var_14192))) # shape=(6, 9, 7)
func_2479_call = mod.get_global_var('func_2479')
func_2484_call = mutated_mod.get_global_var('func_2484')
var_14206 = relay.var("var_14206", dtype = "float64", shape = (144,))#candidate|14206|(144,)|var|float64
var_14207 = relay.var("var_14207", dtype = "float64", shape = (780,))#candidate|14207|(780,)|var|float64
const_14208 = relay.const([3.274989,-1.492870,-0.815646,-5.876531,7.594999,6.184756,6.221452,6.829145,-3.641257,5.818076,-5.381015,-1.350929,1.042172,2.306083,-0.855319,-6.551332,9.936349,9.064861,5.243685,2.634237,-1.588066,4.305089,9.458148,5.691485,-9.517666,-3.827623,4.570073,5.715125,-8.635612,3.461642,8.530040,-1.524443,8.166898,-8.737318,8.678435,8.573537,6.565378,-0.881496,-9.214811,-5.117008,-7.821200,1.734184,-0.186354,-5.067950,-6.259146,5.517779,-0.216924,-4.008697,6.904041,-4.322146,1.123092,-6.873533,-9.787735,5.071101,-9.708242,5.153837,-7.725596,7.878213,8.154340,5.312924,2.372061,1.419061,7.880392,5.167465,0.211244,0.189867,-9.101784,5.283542,-7.492225,8.098771,-2.911374,-5.822497,0.889410,2.812154,6.292384,-4.525808,-2.163702,-3.387895,-7.329330,-7.489898,8.416496,-9.041266,-5.484249,-3.312618,-6.281858,2.665024,-7.907780,8.961534,5.423154,5.205798,2.394652,-9.374073,3.548295,9.392589,-6.512303,9.865761,-1.429957,7.061913,0.508794,6.869595,3.434409,2.094417,-3.222271,-6.129014,6.143227,4.437497,6.566118,-3.612222,-3.706206,-0.119986,-0.477032,7.741714,7.213100,3.930195,-8.746678,-0.511910,9.096973,-6.529471,-9.822158,-7.197372,-9.291049,8.285815,5.651966,-5.392019,0.190685,-0.564362,5.583573,-1.245969,2.529847,6.268030,8.007428,8.998856,9.542951,-1.882357,-8.174952,-1.167492,-6.743563,4.617367,8.932597,-6.460439], dtype = "float64")#candidate|14208|(140,)|const|float64
call_14205 = relay.TupleGetItem(func_2479_call(relay.reshape(var_14206.astype('float64'), [144,]), relay.reshape(var_14207.astype('float64'), [390, 2]), relay.reshape(const_14208.astype('float64'), [5, 28]), ), 2)
call_14209 = relay.TupleGetItem(func_2484_call(relay.reshape(var_14206.astype('float64'), [144,]), relay.reshape(var_14207.astype('float64'), [390, 2]), relay.reshape(const_14208.astype('float64'), [5, 28]), ), 2)
func_3095_call = mod.get_global_var('func_3095')
func_3097_call = mutated_mod.get_global_var('func_3097')
var_14217 = relay.var("var_14217", dtype = "float32", shape = (330,))#candidate|14217|(330,)|var|float32
call_14216 = func_3095_call(relay.reshape(var_14217.astype('float32'), [3, 10, 11]))
call_14218 = func_3095_call(relay.reshape(var_14217.astype('float32'), [3, 10, 11]))
func_3711_call = mod.get_global_var('func_3711')
func_3712_call = mutated_mod.get_global_var('func_3712')
call_14234 = func_3711_call()
call_14235 = func_3711_call()
output = relay.Tuple([bop_14194,call_14205,var_14206,var_14207,const_14208,call_14216,var_14217,call_14234,])
output2 = relay.Tuple([bop_14194,call_14209,var_14206,var_14207,const_14208,call_14218,var_14217,call_14235,])
func_14243 = relay.Function([var_14192,var_14193,var_14206,var_14207,var_14217,], output)
mod['func_14243'] = func_14243
mod = relay.transform.InferType()(mod)
var_14244 = relay.var("var_14244", dtype = "float64", shape = (6, 9, 7))#candidate|14244|(6, 9, 7)|var|float64
var_14245 = relay.var("var_14245", dtype = "float64", shape = (6, 9, 7))#candidate|14245|(6, 9, 7)|var|float64
var_14246 = relay.var("var_14246", dtype = "float64", shape = (144,))#candidate|14246|(144,)|var|float64
var_14247 = relay.var("var_14247", dtype = "float64", shape = (780,))#candidate|14247|(780,)|var|float64
var_14248 = relay.var("var_14248", dtype = "float32", shape = (330,))#candidate|14248|(330,)|var|float32
output = func_14243(var_14244,var_14245,var_14246,var_14247,var_14248,)
func_14249 = relay.Function([var_14244,var_14245,var_14246,var_14247,var_14248,], output)
mutated_mod['func_14249'] = func_14249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11504_call = mod.get_global_var('func_11504')
func_11506_call = mutated_mod.get_global_var('func_11506')
call_14307 = relay.TupleGetItem(func_11504_call(), 0)
call_14308 = relay.TupleGetItem(func_11506_call(), 0)
output = relay.Tuple([call_14307,])
output2 = relay.Tuple([call_14308,])
func_14314 = relay.Function([], output)
mod['func_14314'] = func_14314
mod = relay.transform.InferType()(mod)
mutated_mod['func_14314'] = func_14314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14314_call = mutated_mod.get_global_var('func_14314')
call_14315 = func_14314_call()
output = call_14315
func_14316 = relay.Function([], output)
mutated_mod['func_14316'] = func_14316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13432_call = mod.get_global_var('func_13432')
func_13434_call = mutated_mod.get_global_var('func_13434')
call_14368 = relay.TupleGetItem(func_13432_call(), 0)
call_14369 = relay.TupleGetItem(func_13434_call(), 0)
func_3304_call = mod.get_global_var('func_3304')
func_3307_call = mutated_mod.get_global_var('func_3307')
var_14381 = relay.var("var_14381", dtype = "float32", shape = (1430, 1))#candidate|14381|(1430, 1)|var|float32
const_14382 = relay.const([True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False], dtype = "bool")#candidate|14382|(315,)|const|bool
call_14380 = relay.TupleGetItem(func_3304_call(relay.reshape(var_14381.astype('float32'), [1430, 1]), relay.reshape(const_14382.astype('bool'), [315,]), ), 1)
call_14383 = relay.TupleGetItem(func_3307_call(relay.reshape(var_14381.astype('float32'), [1430, 1]), relay.reshape(const_14382.astype('bool'), [315,]), ), 1)
output = relay.Tuple([call_14368,call_14380,var_14381,const_14382,])
output2 = relay.Tuple([call_14369,call_14383,var_14381,const_14382,])
func_14384 = relay.Function([var_14381,], output)
mod['func_14384'] = func_14384
mod = relay.transform.InferType()(mod)
mutated_mod['func_14384'] = func_14384
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14385 = relay.var("var_14385", dtype = "float32", shape = (1430, 1))#candidate|14385|(1430, 1)|var|float32
func_14384_call = mutated_mod.get_global_var('func_14384')
call_14386 = func_14384_call(var_14385)
output = call_14386
func_14387 = relay.Function([var_14385], output)
mutated_mod['func_14387'] = func_14387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6715_call = mod.get_global_var('func_6715')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_14400 = relay.TupleGetItem(func_6715_call(), 2)
call_14401 = relay.TupleGetItem(func_6716_call(), 2)
output = relay.Tuple([call_14400,])
output2 = relay.Tuple([call_14401,])
func_14403 = relay.Function([], output)
mod['func_14403'] = func_14403
mod = relay.transform.InferType()(mod)
mutated_mod['func_14403'] = func_14403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14403_call = mutated_mod.get_global_var('func_14403')
call_14404 = func_14403_call()
output = call_14404
func_14405 = relay.Function([], output)
mutated_mod['func_14405'] = func_14405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6390_call = mod.get_global_var('func_6390')
func_6392_call = mutated_mod.get_global_var('func_6392')
call_14414 = relay.TupleGetItem(func_6390_call(), 1)
call_14415 = relay.TupleGetItem(func_6392_call(), 1)
output = call_14414
output2 = call_14415
func_14421 = relay.Function([], output)
mod['func_14421'] = func_14421
mod = relay.transform.InferType()(mod)
mutated_mod['func_14421'] = func_14421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14421_call = mutated_mod.get_global_var('func_14421')
call_14422 = func_14421_call()
output = call_14422
func_14423 = relay.Function([], output)
mutated_mod['func_14423'] = func_14423
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14438 = relay.var("var_14438", dtype = "uint64", shape = ())#candidate|14438|()|var|uint64
var_14439 = relay.var("var_14439", dtype = "uint64", shape = (1, 16, 7))#candidate|14439|(1, 16, 7)|var|uint64
bop_14440 = relay.equal(var_14438.astype('bool'), var_14439.astype('bool')) # shape=(1, 16, 7)
output = bop_14440
output2 = bop_14440
func_14448 = relay.Function([var_14438,var_14439,], output)
mod['func_14448'] = func_14448
mod = relay.transform.InferType()(mod)
mutated_mod['func_14448'] = func_14448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14448_call = mutated_mod.get_global_var('func_14448')
var_14450 = relay.var("var_14450", dtype = "uint64", shape = ())#candidate|14450|()|var|uint64
var_14451 = relay.var("var_14451", dtype = "uint64", shape = (1, 16, 7))#candidate|14451|(1, 16, 7)|var|uint64
call_14449 = func_14448_call(var_14450,var_14451,)
output = call_14449
func_14452 = relay.Function([var_14450,var_14451,], output)
mutated_mod['func_14452'] = func_14452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4385_call = mod.get_global_var('func_4385')
func_4387_call = mutated_mod.get_global_var('func_4387')
call_14467 = relay.TupleGetItem(func_4385_call(), 0)
call_14468 = relay.TupleGetItem(func_4387_call(), 0)
output = call_14467
output2 = call_14468
func_14476 = relay.Function([], output)
mod['func_14476'] = func_14476
mod = relay.transform.InferType()(mod)
output = func_14476()
func_14477 = relay.Function([], output)
mutated_mod['func_14477'] = func_14477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14421_call = mod.get_global_var('func_14421')
func_14423_call = mutated_mod.get_global_var('func_14423')
call_14500 = func_14421_call()
call_14501 = func_14421_call()
output = call_14500
output2 = call_14501
func_14508 = relay.Function([], output)
mod['func_14508'] = func_14508
mod = relay.transform.InferType()(mod)
output = func_14508()
func_14509 = relay.Function([], output)
mutated_mod['func_14509'] = func_14509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9719_call = mod.get_global_var('func_9719')
func_9720_call = mutated_mod.get_global_var('func_9720')
call_14525 = func_9719_call()
call_14526 = func_9719_call()
output = call_14525
output2 = call_14526
func_14527 = relay.Function([], output)
mod['func_14527'] = func_14527
mod = relay.transform.InferType()(mod)
output = func_14527()
func_14528 = relay.Function([], output)
mutated_mod['func_14528'] = func_14528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8662_call = mod.get_global_var('func_8662')
func_8663_call = mutated_mod.get_global_var('func_8663')
call_14554 = func_8662_call()
call_14555 = func_8662_call()
output = call_14554
output2 = call_14555
func_14560 = relay.Function([], output)
mod['func_14560'] = func_14560
mod = relay.transform.InferType()(mod)
output = func_14560()
func_14561 = relay.Function([], output)
mutated_mod['func_14561'] = func_14561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8478_call = mod.get_global_var('func_8478')
func_8479_call = mutated_mod.get_global_var('func_8479')
call_14567 = relay.TupleGetItem(func_8478_call(), 3)
call_14568 = relay.TupleGetItem(func_8479_call(), 3)
output = call_14567
output2 = call_14568
func_14569 = relay.Function([], output)
mod['func_14569'] = func_14569
mod = relay.transform.InferType()(mod)
output = func_14569()
func_14570 = relay.Function([], output)
mutated_mod['func_14570'] = func_14570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12687_call = mod.get_global_var('func_12687')
func_12688_call = mutated_mod.get_global_var('func_12688')
call_14690 = relay.TupleGetItem(func_12687_call(), 0)
call_14691 = relay.TupleGetItem(func_12688_call(), 0)
func_9364_call = mod.get_global_var('func_9364')
func_9366_call = mutated_mod.get_global_var('func_9366')
var_14715 = relay.var("var_14715", dtype = "bool", shape = (80,))#candidate|14715|(80,)|var|bool
call_14714 = relay.TupleGetItem(func_9364_call(relay.reshape(var_14715.astype('bool'), [1, 80])), 3)
call_14716 = relay.TupleGetItem(func_9366_call(relay.reshape(var_14715.astype('bool'), [1, 80])), 3)
output = relay.Tuple([call_14690,call_14714,var_14715,])
output2 = relay.Tuple([call_14691,call_14716,var_14715,])
func_14723 = relay.Function([var_14715,], output)
mod['func_14723'] = func_14723
mod = relay.transform.InferType()(mod)
mutated_mod['func_14723'] = func_14723
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14724 = relay.var("var_14724", dtype = "bool", shape = (80,))#candidate|14724|(80,)|var|bool
func_14723_call = mutated_mod.get_global_var('func_14723')
call_14725 = func_14723_call(var_14724)
output = call_14725
func_14726 = relay.Function([var_14724], output)
mutated_mod['func_14726'] = func_14726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14113_call = mod.get_global_var('func_14113')
func_14114_call = mutated_mod.get_global_var('func_14114')
call_14768 = relay.TupleGetItem(func_14113_call(), 0)
call_14769 = relay.TupleGetItem(func_14114_call(), 0)
output = relay.Tuple([call_14768,])
output2 = relay.Tuple([call_14769,])
func_14772 = relay.Function([], output)
mod['func_14772'] = func_14772
mod = relay.transform.InferType()(mod)
mutated_mod['func_14772'] = func_14772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14772_call = mutated_mod.get_global_var('func_14772')
call_14773 = func_14772_call()
output = call_14773
func_14774 = relay.Function([], output)
mutated_mod['func_14774'] = func_14774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12687_call = mod.get_global_var('func_12687')
func_12688_call = mutated_mod.get_global_var('func_12688')
call_14806 = relay.TupleGetItem(func_12687_call(), 0)
call_14807 = relay.TupleGetItem(func_12688_call(), 0)
func_9172_call = mod.get_global_var('func_9172')
func_9174_call = mutated_mod.get_global_var('func_9174')
var_14809 = relay.var("var_14809", dtype = "uint8", shape = (108, 2))#candidate|14809|(108, 2)|var|uint8
call_14808 = relay.TupleGetItem(func_9172_call(relay.reshape(var_14809.astype('uint8'), [12, 18])), 3)
call_14810 = relay.TupleGetItem(func_9174_call(relay.reshape(var_14809.astype('uint8'), [12, 18])), 3)
output = relay.Tuple([call_14806,call_14808,var_14809,])
output2 = relay.Tuple([call_14807,call_14810,var_14809,])
func_14835 = relay.Function([var_14809,], output)
mod['func_14835'] = func_14835
mod = relay.transform.InferType()(mod)
mutated_mod['func_14835'] = func_14835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14836 = relay.var("var_14836", dtype = "uint8", shape = (108, 2))#candidate|14836|(108, 2)|var|uint8
func_14835_call = mutated_mod.get_global_var('func_14835')
call_14837 = func_14835_call(var_14836)
output = call_14837
func_14838 = relay.Function([var_14836], output)
mutated_mod['func_14838'] = func_14838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9799_call = mod.get_global_var('func_9799')
func_9800_call = mutated_mod.get_global_var('func_9800')
call_14939 = relay.TupleGetItem(func_9799_call(), 0)
call_14940 = relay.TupleGetItem(func_9800_call(), 0)
output = relay.Tuple([call_14939,])
output2 = relay.Tuple([call_14940,])
func_14941 = relay.Function([], output)
mod['func_14941'] = func_14941
mod = relay.transform.InferType()(mod)
output = func_14941()
func_14942 = relay.Function([], output)
mutated_mod['func_14942'] = func_14942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9586_call = mod.get_global_var('func_9586')
func_9588_call = mutated_mod.get_global_var('func_9588')
call_14950 = relay.TupleGetItem(func_9586_call(), 0)
call_14951 = relay.TupleGetItem(func_9588_call(), 0)
func_9920_call = mod.get_global_var('func_9920')
func_9921_call = mutated_mod.get_global_var('func_9921')
call_14965 = func_9920_call()
call_14966 = func_9920_call()
func_4641_call = mod.get_global_var('func_4641')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_14967 = relay.TupleGetItem(func_4641_call(), 0)
call_14968 = relay.TupleGetItem(func_4643_call(), 0)
output = relay.Tuple([call_14950,call_14965,call_14967,])
output2 = relay.Tuple([call_14951,call_14966,call_14968,])
func_14974 = relay.Function([], output)
mod['func_14974'] = func_14974
mod = relay.transform.InferType()(mod)
output = func_14974()
func_14975 = relay.Function([], output)
mutated_mod['func_14975'] = func_14975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9883_call = mod.get_global_var('func_9883')
func_9885_call = mutated_mod.get_global_var('func_9885')
call_14991 = func_9883_call()
call_14992 = func_9883_call()
func_7265_call = mod.get_global_var('func_7265')
func_7269_call = mutated_mod.get_global_var('func_7269')
const_15016 = relay.const([-0.021529,7.856013,2.434716,7.328996,-6.559120,1.425767,1.167543,3.711653,3.979579,1.008793,3.726484,7.804702,-4.571318,-2.270410,7.789642,-3.102093,5.709136,9.450573,4.555495,2.474006,-9.723270,-4.714774,-2.518765,8.854798,2.749567,9.400946,-5.862948,-1.212950,-9.263402,-1.738120,-4.443284,5.528035,-0.508250,3.380433,4.658755,8.431511,2.298306,0.824557,7.732364,-1.448487,4.542614,-7.696301,-6.887245,-1.980916,1.458379,-6.329445,9.695529,7.529370,2.900853,1.999209,6.924795,-9.508403,-4.758034,-0.766651,3.824624,8.804503,-6.961771,-7.003466,-5.256755,6.943229,0.500295,2.056394,0.596363,-6.476006,0.713127,2.361763,0.549181,-6.919155,1.946938,5.765602,6.460320,-7.264274,-4.225441,-5.309417,1.923096,9.052231,-9.235928,-1.954984,1.024827,-5.101885,-3.567287,-9.998278,0.731673,-1.333167,8.516171,5.760054,-4.673252,5.868282,-6.280504,0.714551,2.540209,-7.799937,2.245932,-6.044735,-5.283368,-0.853763,-2.868988,-2.638373,4.170129,9.813110,-5.743308,3.810641,-8.075128,-8.198347,-0.447552,-6.410711,-8.287768,8.901049,7.763835,-3.158341,-6.550565,2.272023,5.535453,6.215747,-2.378065,-8.704921,8.220262,9.435675,-1.412032,2.823000,7.453324,-3.745029,-6.349717,3.285316,0.697462,2.812401,-7.375244,3.688943,-2.666422,-1.610640,1.343392,-4.962567,-2.412337,-8.993186,8.009320,-8.673857,4.918527,-0.071001,-2.115809,-8.992455], dtype = "float64")#candidate|15016|(140,)|const|float64
const_15017 = relay.const([-6.890756,-5.542915,-0.368495,3.049383,3.743809,-6.988290,0.394968,-8.731587,-0.165728,3.989499,2.996436,-7.520346,1.287973,-1.457959,-9.350106,6.230251,-0.168980,-9.548983,-5.079136,-8.184868,9.906560,-5.131821,4.673459,2.137015,2.001056,7.431692,-3.724785,-1.451798,-7.527088,-7.042781,1.231392,7.107040,6.922458,-6.920343,5.692802,1.442889,-8.120923,8.804042,-7.158321,2.896584,9.611948,8.445295,-2.953685,-6.771804,-6.828872,-8.739648,-7.007763,7.769476,7.316803,5.308635,-7.591308,4.630429,-6.786732,-8.915320,5.620623,-0.187725,-5.239302,-0.417893,-8.952589,-6.208545,8.021701,-4.715833,-9.001044,-0.198068,-2.258889,6.283218,-5.260279,5.428780,2.623594,-1.728735,5.277809,-7.968455,-6.086787,2.693457,8.064365,1.182276,-5.462077,-4.766088,8.672710,-7.073425,-3.168229,-2.191977,-9.962773,-5.813082,6.978008,-1.140205,5.741788,-1.813549,1.523058,-5.751260,4.139813,5.285785,-6.113245,0.514241,-0.581410,5.013407,1.886403,-8.286717,7.990890,6.524007,6.826887,7.534238,-8.935028,-8.313073,3.032160,-3.468576,-4.859473,-6.259401,6.150034,-9.957042,6.872499,5.800236,4.233443,-1.201561,-5.567293,0.858979,8.452627,-8.671140,-2.130746,4.181056,-9.082829,9.701757,-4.593955,5.151549,8.894418,1.510376,6.405644,6.903006,-2.361770,9.542508,9.870132,-5.919102,0.719970,8.815132,2.303223,-3.411471,-3.390283,-5.906748,7.187504,2.570736,7.967755,-6.437740,6.136006,4.123771,2.959883,-2.550644,8.102405,-0.401554,3.752759,8.963549,-4.638806,-0.207190,4.786066,7.221285,-5.311098,8.991813,-0.232669,-0.494089,8.635429,3.529019,-0.291619,2.705289,3.728374,4.829052,8.653235,4.434579,-9.138439,5.377944,8.043590,-0.771162,7.745845,7.780606,5.286288,3.949394,-6.012327,-7.776586,-6.590249,-5.994064,9.972044,-0.369882,-6.925494,-3.091680,-5.071750,-7.057550,9.313623,7.163106,-6.023006,-7.992794,9.922223,-7.170560,-3.858067,-7.170117,3.839291,-3.833434,-6.822970,5.358515,5.956918,4.636924,0.619682,7.150403,3.441179,6.953784,6.127985,0.217553,8.776545,-6.958830,-4.634043,-1.961160,-7.613261,-7.019603,-7.286548,8.874784,-3.625857,3.427565,8.830312,-1.523523,8.172451,-9.347564,1.028062,1.161984,-2.178412,-3.625922,5.952023,-7.534188,-6.449681,-9.334511,-5.487766,-4.620053,8.465823,6.737724,-5.102607,4.162323,2.998100,-7.616227,8.839148,-7.055358,-1.631151,7.943272,1.669036,7.959518,-4.381875,-6.281517,8.884724,7.505127,-2.276618,7.976829,-9.745520,6.892532,0.228319,-6.246551,7.833725,-9.079912,-5.859137,4.706063,4.805821,5.680147,8.068243,-0.235775,-9.686667,6.193869,-5.117141,2.445495,6.041588,4.977296,-4.295094,7.817993,-1.138548,0.863045,5.225030,-3.698325,6.568655,4.548864,-8.829984,-6.547947,0.775892,3.756692,-9.352047,7.309571,3.486491,-2.037754,-8.635153,-8.169382,1.091514,8.589391,-2.750817,6.249688,5.138897,-6.900241,9.813812,-4.598407,-5.320514,-8.420556,-9.200799,-3.336736,-6.115221,-6.268859,0.843045,1.636761,-7.938785,9.346470,0.268986,1.920022,5.126862,-4.867872,-4.100976,-1.437241,-7.959102,4.038849,-5.808332,3.910883,0.800452,4.018065,-2.557435,2.267089,-5.646564,0.056435,-8.307650,-4.220972,9.624282,-1.101415,-7.722815,-0.982995,4.262406,6.794874,-4.138495,3.371120,-8.136017,-0.977588,6.271692,-4.909485,-5.927229,8.795711,-1.087322,8.326475,-5.138020,0.964956,-7.582494,-8.561274,9.558459,4.438998,-8.594449,4.643301,6.322306,7.521725,-4.001504,-1.652467,4.098141,8.853529,-2.694486,3.488675,-5.578914,0.315992,5.331665,-6.786992,6.833554,-1.766461,-8.416525,9.333153,1.925817,4.986846,-3.348630,-0.204837,5.855927,9.309584,-2.172881,5.666544,1.230787,0.496277,-6.798189,9.235026,7.132884,0.971565,-4.873824,-2.796297,7.676955,8.128485,2.826563,2.532608,7.627713,-2.182003,-1.375071,-2.795273,-6.087900,-8.807427,4.500232,3.277815,0.895590,3.764300,0.430286,1.732535,0.302364,-4.264756,-7.002438,1.217751,-2.922544,-7.300779,8.585740,-6.216867,-5.774172,-1.814002,-7.163319,8.658634,-2.244881,4.065685,-1.003548,-4.650715,3.568601,-9.475708,4.025014,7.398413,-0.111356,-6.588866,-5.148869,5.428008,3.315233,3.043458,1.155551,8.598580,6.742369,8.533053,7.182103,9.651106,-1.343332,-9.046839,9.670639,1.475020,3.564800,-8.780888,-9.680736,4.600765,6.597477,-7.139216], dtype = "float32")#candidate|15017|(432,)|const|float32
const_15018 = relay.const([-2.494176,-1.196133,-2.244602,9.555019,3.380640,-6.290999,7.227293,-4.329374,3.324134,6.679006,3.483647,4.544238,4.826225,2.957827,3.508168,2.612118,-7.387520,6.074479,1.358387,4.641486,5.991397,2.080645,-7.555219,5.788347,-9.261541,9.029953,5.210671,5.292766,-2.441500,8.839493,3.375413,-3.937422,-3.734384,-2.014003,-8.965223,2.369125,-5.189041,-8.662621,-5.646184,-3.934558,-1.213064,-6.249452,6.039126,-8.848144,8.330591,9.547981,-6.598935,-3.897141,-8.140454,-3.013842,-8.828487,-2.813447,0.163921,4.097297,-3.349697,-0.322429,-0.974118,1.647150,-2.678759,1.166334,3.442263,-4.137496,-8.423059,9.632528,-7.051902,7.169678,7.615365,0.452238,9.829651,-5.924965,-7.557663,-4.007872,-9.470875,-3.900794,-9.529191,-4.735654,1.881193,7.056416,5.623843,-9.534397,4.859641,-6.340360,4.393450,1.753043,6.948673,-2.024537,-0.080683,-1.923284,-0.679211,-2.214526,-9.314488,4.400403,6.348995,-0.316214,4.399694,-8.296621,-9.875530,5.017047,-4.630628,-5.938732,-5.066923,-0.136418,-4.749592,8.538609,0.494352,3.423529,-2.494704,7.254284,4.416461,-0.076746,-4.272989,6.184010,-2.756785,-6.031262,3.768631,-3.447870,-3.410179,8.687017,0.403737,7.504189,-0.991329,-7.965691,9.892532,-7.743764,4.197118,1.022397,-8.474132,2.716211,8.594628,1.899028,-2.080091,2.525514,-9.889661,3.638289,7.194174,5.705334,6.274822,3.846252,5.424812,-9.509416,-8.619163,6.251172,-3.539101,7.359004], dtype = "float64")#candidate|15018|(144,)|const|float64
call_15015 = relay.TupleGetItem(func_7265_call(relay.reshape(const_15016.astype('float64'), [140,]), relay.reshape(const_15017.astype('float32'), [432,]), relay.reshape(const_15018.astype('float64'), [144,]), ), 7)
call_15019 = relay.TupleGetItem(func_7269_call(relay.reshape(const_15016.astype('float64'), [140,]), relay.reshape(const_15017.astype('float32'), [432,]), relay.reshape(const_15018.astype('float64'), [144,]), ), 7)
func_12179_call = mod.get_global_var('func_12179')
func_12183_call = mutated_mod.get_global_var('func_12183')
call_15026 = relay.TupleGetItem(func_12179_call(relay.reshape(call_14991.astype('float64'), [780,]), relay.reshape(const_15016.astype('float64'), [140,]), ), 4)
call_15027 = relay.TupleGetItem(func_12183_call(relay.reshape(call_14991.astype('float64'), [780,]), relay.reshape(const_15016.astype('float64'), [140,]), ), 4)
func_13163_call = mod.get_global_var('func_13163')
func_13165_call = mutated_mod.get_global_var('func_13165')
const_15030 = relay.const([7.171957,9.443233,-5.491078,-5.114171,-9.913298,2.245525,6.000235,5.976125,9.266014,-3.659050,7.075831,-8.651564,-9.605063,-2.309478,-2.263456,-4.860095,3.828295,7.422196,2.333774,3.147045,-1.103597,7.954220,-2.357449,2.568434,8.261017,7.648542,-2.322629,7.515444,4.667366,-7.496167,6.543132,-0.063964,-8.226445,-3.133691,3.015045,5.137586,-7.031770,4.931516,-0.885011,7.002876,5.773586,-5.273024,-3.840859,-7.091317,4.502146,6.904559,3.317254,3.205457,-1.702833,-8.528860,-9.611588,9.200428,-3.404028,3.243208,2.508991,9.192641,3.913674,-9.047052,3.698640,-7.304539,-5.393003,6.099546,7.705205,2.909671,-0.996838,2.579954,-7.957189,1.725214,-8.052929,3.828430,6.604140,-1.988182,-6.645790,-2.739338,8.489179,-2.769514,3.486285,-6.639190,-7.169378,-3.222802,3.678207,6.946677,-9.415107,-1.738866,-3.172249,1.179136,-4.778498,-1.783116,-8.495009,-0.191302,2.201472,1.930726,-2.706321,7.461048,-9.608829,4.627219,-2.682123,6.606544,-6.250597,1.396614,8.836573,-0.471724,-1.396469,-4.837759,-9.197580,-9.684658,1.121282,-4.084125,9.690490,-0.872404,8.340175,2.271946,5.830607,-2.531361,6.892437,-8.899401,-0.962031,-2.588238,8.752770,-8.581887,-8.197522,-0.569749,-3.286122,0.182564,-2.843100,1.917999,-3.280358,1.563616,5.805661,5.589472,6.404012,9.596641,-0.655157,-0.035205,-9.849840,4.917686,-5.051392,-3.572877,-2.094309,-2.936631,-2.233255,-8.890108,6.793057,-9.339756,-0.801679,9.555517,3.736357,8.929006,-3.147986,2.171198,-5.824879,2.822718,-5.550100,-6.885025,-7.566567,-5.376071,-4.087991,8.974748,-4.264347,2.553896,1.253925,6.373841,7.121712,-2.506849,-1.743262,3.429918,5.097662,4.253972,-0.646214,-4.536798,9.365992,0.633377,-6.981340,6.752871,-6.757405,8.786082,3.957068,-5.791156,8.661134,-8.397321,9.922765,1.409894,1.745782,-4.084900,-4.538894,-4.189115,6.115081,2.592102,-0.635303,3.780197,0.010441,-8.561915,4.680440,-7.436576,8.338762,-5.536656,-3.399882,0.688956,1.395860,4.117727,8.220601,6.129428,-6.329332,-0.497033,8.160194,6.097932,-7.254325,1.185947,8.182941,-6.097620,-9.001960,4.649126,-9.334205,-4.299455,-3.699082,3.969215,2.948979,1.351644,-0.712187,-8.177003,5.073568,-0.784085,6.504087,4.320785,8.712819,-9.842722,-2.804219,-0.424577,-8.335106,-4.869886,9.011788,-9.454911,-9.408062,-9.201410,5.019347,-9.047680,-6.691269,-0.633645,-7.359249,-5.001726,-9.538801,-2.062433,-5.245990,3.295361,2.957890,-6.789509,-1.342075,-9.089834,-3.831821,7.471147,3.828154,-9.505862,-6.838508,-2.882377,-3.466896,9.173676,8.496817,3.603163,-6.915134,-9.917244,5.135608,-5.280156,-7.724757,-0.594281,4.787285,-4.386279,-4.640187,5.841231,-1.587552,2.578009,-3.235835,1.927623,-1.215607,-8.313105,8.150610,7.224625,8.447817,-6.541666,-5.307478,-8.892135,-6.040670,-3.492061,5.792266,-5.963157,3.495919,-1.946361,-2.716704,9.444220,-9.973759,2.601183,5.557305,-8.033906,4.182168,-2.618107,-2.545382,9.356502,3.704726,0.473640,0.029702,-6.098993,5.050762,8.466943,-4.239299,5.017315,-6.937704,5.346160,2.687925,-1.216854,-0.595496,-5.724943,6.501898,-1.023507,6.138602,1.101132,9.546455,-2.509404,-6.421597,-6.999415,-2.055806,7.576489,-8.288132,-0.376066,6.477295,-0.040375,4.746023,-6.480722,7.418749,-4.084794,-5.962948,9.146404,2.132824,-1.502196,0.586716,4.161692,-9.254049,-6.695188,0.344117,-2.113169,7.166569,-7.405538,3.354788,1.582520,4.628909,-0.239430,5.437875,1.933188,3.389597,-1.316475,-8.496772,-9.750743,0.585675,-4.438650,-0.543567,1.001134,5.417298,-4.693609,-6.976665,1.501345,4.984311,8.247307,-9.968399,-1.900508,-2.844006,-3.443701,-4.495557,-4.185669,-1.579971,-6.352364,6.085774,-9.043030,8.828932,-0.409070,4.319935,-4.286028,4.700362,5.142082,-4.378455,4.160921,3.856718,-9.729795,-7.305967,4.437081,7.274492,0.114043,7.038498,1.795813,4.750332,-8.242429,-9.367407,0.844941,-6.986449,9.090596,-2.522782,6.484223,-6.214356,6.292016,-5.230088,6.113282,-8.356454,0.460766,7.908365,4.465835,-0.666477,1.008275,-9.132883,-0.119467,2.001698,0.023491,-8.465094,7.526384,-0.367701,1.749513,9.350923,-7.136820,-4.936144,9.201302,1.157293,-0.950614,-5.736592,-0.012504,-7.204108,1.959351,-1.258081,-3.890624,-1.137747,4.319348,-4.436200,2.245243,-5.557412,-8.137547,2.485466,-1.675477,-8.007879,-2.118750,-7.407323,0.515293,1.132878,-1.923306,9.573248,-4.058096,7.785184,2.032093,1.775365,7.790089,-3.389867,-9.290978,-5.395467,-6.827865,0.973258,6.590032,0.501698,-4.206092,-9.610196,-0.315008,4.496296,1.985267,0.913683,2.797421,5.790398,-6.434738,-1.886945,-3.884085,3.051694,3.273161,1.000589,-7.252649,0.201338,-2.814861,8.201713,2.601578,6.069794,4.795577,8.782765,8.936000,-3.172411,0.582808,-2.890459,9.193752,-0.477945,-1.486684,3.136481,9.759506,-6.216328,-3.981988,-3.080754,-5.139815,-4.022912,-4.415010,-7.523357,9.726693,1.598333,9.932196,-7.690830,4.264638,6.395468,-1.393398,-1.137754,8.950247,3.126172,1.536705,-8.306245,-8.433229,8.005613,-0.411489,-2.307587,-8.938066,-0.399486,-8.005714,-9.946019,-7.378427,1.715994,2.833894,-8.970951,-0.794074,-6.998624,4.802656,-5.541956,-0.366430,9.617647,7.647105,-0.025588,6.545038,-1.213162,0.690994,-4.312412,-0.129601,-9.733300,9.075429,5.135118,6.459845,9.952387,-1.316397,-1.312080,-4.027645,9.488495,2.231310,8.006943,3.962855,-1.917289,2.406336,-0.767450,6.195137,6.376249,6.505598,-6.032978,-1.931308,2.291949,2.549761,7.174291,2.019258,-5.113573,-9.072161,-6.288893,5.219366,-1.522648,5.365078,-3.483478,-3.967574,2.912691,-1.637604,-5.811246,-5.378341,7.784456,8.916983,4.691085,-6.185441,5.283359,8.204769,-7.066225,4.895597,7.733364,9.319830,8.776292,3.961684,5.873964,-3.637201,0.901090,1.708943,4.273167,1.884134,-9.192052,-5.816070,7.180106,7.808419,-1.714285,-7.080982,5.681862,2.043422,7.092383,9.606721,0.738717,-5.148537,-7.244512,9.105389,-1.804403,-7.892184,-8.192757,0.779526,0.682707,6.866921,9.131429,2.706126,1.692676,2.270260,-0.468157,1.853933,-1.132600,-5.761040,-6.235199,-0.390654,-4.440775,9.311369,5.737400,-9.090786,5.553907,-5.519110,-2.798464,9.853482,5.831637,-2.259844,8.220728,8.282126,-1.531041,4.873365,5.048979,4.734498,-8.677710,5.487976,6.803165,-1.683275,4.787229,4.613273,6.892438,-8.238372,9.955518,-9.259555,-0.368594,8.704081,2.048767,8.816523,-8.671532,-9.018508,4.001227,4.466225,-9.437726,1.494380,-6.423942,9.103263,6.751676,-2.887979,-0.369112,-7.096926,-6.643811,9.358075,-2.905482,3.144780,-4.037245,6.438862,1.253075,-6.527636,1.865108,1.310531,0.919022,9.992393,-5.070026,2.807919,-4.311663,-5.768247,3.007397,-1.789644,-7.999577,3.988419,3.329978,0.830326,1.139736,-3.292200,0.169299,-1.418870,-9.140882,-4.047903,-3.618665,-7.476828,3.796295,6.486838,-8.044741,-2.536088,4.028452,9.310367,-8.347312,9.518902,3.315452,-1.271204,-3.924428,0.788640,-7.693969,7.786508,1.412092,7.324047,-6.903676,-1.098106,-5.681113,-9.030160,-9.833659,5.412307,-2.666850,-9.284704,-5.411668,-4.286755,5.289488,-7.230466,9.209871,-9.838305,6.650126,5.449293,2.954916], dtype = "float64")#candidate|15030|(715,)|const|float64
call_15029 = relay.TupleGetItem(func_13163_call(relay.reshape(const_15030.astype('float64'), [11, 5, 13])), 0)
call_15031 = relay.TupleGetItem(func_13165_call(relay.reshape(const_15030.astype('float64'), [11, 5, 13])), 0)
output = relay.Tuple([call_14991,call_15015,const_15016,const_15017,const_15018,call_15026,call_15029,const_15030,])
output2 = relay.Tuple([call_14992,call_15019,const_15016,const_15017,const_15018,call_15027,call_15031,const_15030,])
func_15037 = relay.Function([], output)
mod['func_15037'] = func_15037
mod = relay.transform.InferType()(mod)
mutated_mod['func_15037'] = func_15037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15037_call = mutated_mod.get_global_var('func_15037')
call_15038 = func_15037_call()
output = call_15038
func_15039 = relay.Function([], output)
mutated_mod['func_15039'] = func_15039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_15045 = relay.TupleGetItem(func_6224_call(), 0)
call_15046 = relay.TupleGetItem(func_6226_call(), 0)
output = relay.Tuple([call_15045,])
output2 = relay.Tuple([call_15046,])
func_15062 = relay.Function([], output)
mod['func_15062'] = func_15062
mod = relay.transform.InferType()(mod)
mutated_mod['func_15062'] = func_15062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15062_call = mutated_mod.get_global_var('func_15062')
call_15063 = func_15062_call()
output = call_15063
func_15064 = relay.Function([], output)
mutated_mod['func_15064'] = func_15064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_15081 = relay.TupleGetItem(func_3161_call(), 0)
call_15082 = relay.TupleGetItem(func_3162_call(), 0)
output = relay.Tuple([call_15081,])
output2 = relay.Tuple([call_15082,])
func_15113 = relay.Function([], output)
mod['func_15113'] = func_15113
mod = relay.transform.InferType()(mod)
output = func_15113()
func_15114 = relay.Function([], output)
mutated_mod['func_15114'] = func_15114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_15193 = relay.TupleGetItem(func_14157_call(), 0)
call_15194 = relay.TupleGetItem(func_14158_call(), 0)
func_15037_call = mod.get_global_var('func_15037')
func_15039_call = mutated_mod.get_global_var('func_15039')
call_15197 = relay.TupleGetItem(func_15037_call(), 3)
call_15198 = relay.TupleGetItem(func_15039_call(), 3)
output = relay.Tuple([call_15193,call_15197,])
output2 = relay.Tuple([call_15194,call_15198,])
func_15208 = relay.Function([], output)
mod['func_15208'] = func_15208
mod = relay.transform.InferType()(mod)
mutated_mod['func_15208'] = func_15208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15208_call = mutated_mod.get_global_var('func_15208')
call_15209 = func_15208_call()
output = call_15209
func_15210 = relay.Function([], output)
mutated_mod['func_15210'] = func_15210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5085_call = mod.get_global_var('func_5085')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_15229 = relay.TupleGetItem(func_5085_call(), 0)
call_15230 = relay.TupleGetItem(func_5087_call(), 0)
func_11309_call = mod.get_global_var('func_11309')
func_11311_call = mutated_mod.get_global_var('func_11311')
var_15238 = relay.var("var_15238", dtype = "float64", shape = (780,))#candidate|15238|(780,)|var|float64
call_15237 = relay.TupleGetItem(func_11309_call(relay.reshape(var_15238.astype('float64'), [780,])), 0)
call_15239 = relay.TupleGetItem(func_11311_call(relay.reshape(var_15238.astype('float64'), [780,])), 0)
output = relay.Tuple([call_15229,call_15237,var_15238,])
output2 = relay.Tuple([call_15230,call_15239,var_15238,])
func_15269 = relay.Function([var_15238,], output)
mod['func_15269'] = func_15269
mod = relay.transform.InferType()(mod)
var_15270 = relay.var("var_15270", dtype = "float64", shape = (780,))#candidate|15270|(780,)|var|float64
output = func_15269(var_15270)
func_15271 = relay.Function([var_15270], output)
mutated_mod['func_15271'] = func_15271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_15301 = relay.TupleGetItem(func_4982_call(), 0)
call_15302 = relay.TupleGetItem(func_4983_call(), 0)
func_11347_call = mod.get_global_var('func_11347')
func_11349_call = mutated_mod.get_global_var('func_11349')
const_15311 = relay.const([3.534476,2.892666,-1.888387,4.368894,5.195849,-9.906863,0.830888,-0.675441,-5.516118,5.469150,7.306303,-8.941202,-5.436315,-5.535701,-7.548112,3.452864,2.699389,9.103683,-8.833586,-7.984486,5.549884,6.258497,2.878393,-6.578384,-6.354497,-0.311660,-0.619499,3.314001,-2.093008,-0.339080,-7.804537,9.137128,5.868854,-9.752678,8.644333,2.325772,1.462194,9.988445,-3.289906,-3.417494,3.879780,-9.416677,7.949090,4.568466,7.721680,-7.148800,7.940232,1.151819,-3.129000,-3.975880,-8.982118,-2.137213,3.007839,-2.693161,-0.218493,-5.139319,-6.622468,8.965618,7.536797,2.307477,0.982599,-6.493763,4.055414,2.303234,5.375281,0.877030,1.275197,7.627458,-4.739822,4.117783,-1.904486,-8.769342,-6.234985,-2.217539,-5.507599,3.022301,1.669665,-3.469084,3.689874,4.091588,-5.128694,6.678943,-5.022067,-6.157207,-4.220349,4.623448,4.176671,4.354955,-4.895118,6.074603,-0.538331,-6.321954,8.795485,-2.207905,-5.238822,7.444597,8.377418,-2.331391,-0.694729,-4.127458,-7.824232,0.980897,9.589665,-1.869245,8.092377,8.048087,-9.271957,2.702193,-4.554147,-6.791430,5.161469,1.022269,-8.195749,9.385055,-9.355365,-7.459335,4.881643,1.917292,-0.757440,-0.829594,8.825204,7.988829,8.160059,8.799045,6.344670,-4.581317,-2.640893,2.919087,-3.959349,6.042318,-1.058498,7.938481,5.142508,-6.710705,-8.480566,7.157175,-0.025465,3.301965,-7.781183,-0.508359,7.212560,-9.360823,-7.536875,-1.275402,-8.689745,-1.867404,6.538535,6.667130,-0.702788,7.168548,-7.047473,-8.920388,4.010022,2.010416,5.039362,1.540212,-7.456136,-8.274610,7.389233,2.179805,-3.839461,-8.411123,-1.634331,-0.095442,-0.341617,9.041540,2.487042,7.189478,-1.783785,-3.414892,-9.975927,-8.893482,5.952942,-2.163318,4.420877,9.539502,0.316344,-0.185668,9.425945,-9.110001,-7.753785,-5.758042,5.524011,-3.500693,-7.542437,6.688143,1.189221,-8.657062,-7.841909,6.421841,-6.229498,5.426253,1.644109,8.216775,0.857430,-9.937668,-5.562852,5.645081,-9.415099,2.983968,-7.530649,-1.194820,-7.845330,-5.419013,2.193788,-7.362712,-4.683161,0.746061,8.236055,-4.998373,-2.257493,-9.294997,-8.932598,-5.615450,-3.095730,2.076367,6.439472,-8.272511,-0.934723,-7.125909,-7.657116,-6.111465,4.284999,-0.173493,-7.667227,7.713060,9.658380,8.149851,3.027754,3.553853,4.453966,-6.751008,-6.174038,-4.974349,4.817015,-2.683221,-8.872877,2.183717,-0.953015,-8.019838,-0.091576,5.618816,-6.188553,1.685908,-8.898225,7.822851,-1.573399,-6.794357,-2.268294,7.454863,-2.278551,3.447728,-3.939722,-2.279479,7.852871,-0.883200,-9.206860,5.519572,-3.828309,-9.215810,7.400034,4.279611,0.640686,-6.948330,-0.781942,3.603539,2.753872,7.019043,6.351855,-9.775379,1.359637,3.987203,-6.954603,-1.324743,7.741573,-5.581581,-0.071584,-3.501246,0.239434,4.073680,4.060138,-1.085025,6.413771,-2.413069,8.336206,3.797531,5.312120,-0.426240,-8.754850,5.920317,9.357326,-0.408194,2.964663,4.885180,-5.286299,-7.666337,-3.213287,-8.745972,7.039443,-2.112706,-0.260716,9.362063,-4.609758,7.256045,-1.537812,5.097355,-8.438034,2.185093,-7.621438,0.612487,3.891328,-7.620912,-1.574243,1.898940,-8.660035,1.918331,-9.938115,-9.604646,-1.638085,3.457156,-0.305430,8.837818,-2.017106,-3.636160,4.625915,9.025148,-0.467154,-4.306824,4.080869,-3.387350,-6.148764,-7.424650,-0.775367,5.382401,-7.603768,4.106724,5.868696,-6.588590,1.897897,6.208900,-3.726932,9.010196,-2.053667,5.040216,0.012871,7.948025,1.724363,-2.422156,8.658530,2.305080,-9.768914,-8.293606,9.294345,-7.341193,-7.384846,1.699933,-6.483074,9.087323,9.176105,-9.917319,-2.600736,-2.137631,6.556420,6.167587,-6.492740,4.729066,5.222112,2.010629,-8.730266,9.760169,3.554815,1.999152,6.606424,-5.334270,0.708801,3.686183,1.160069,-5.593434,8.696256,9.264143,-2.213891,-1.197156,-4.381021,-0.882650,8.214166,4.469534,-3.419294,7.990493,9.397828,-5.612352,-6.856622,-8.217837,4.559417,9.973794,-3.857306,9.647486,0.133947,-7.720527,8.769822,-9.520902,-0.348885,9.958005,-0.418717,-3.062994,-9.930912,-0.681656,0.338617,-2.378693,9.201224,2.628162,-3.386845,-1.083095,-0.259885,-0.559526,0.027404,7.720313,-8.363067,7.278199,9.972198,9.574258,-0.462396,-2.497040,-6.396210,2.491701,-1.287822,-5.123610,0.311764,-5.736144,7.169325,8.792646,5.163426,7.033915,0.153707,-1.680458,-3.798648,-6.807831,-8.884262,-1.286580,-5.823298,-5.046700,-4.069906,3.919251,-9.606154,-8.204441,-5.429169,-1.220575,-1.171149,-1.545530,-7.734736,-9.676165,-1.873357,-8.934099,0.137741,8.445104,-9.997996,2.817721,-4.609234,-7.037406,-3.938344,7.716978,-4.934757,8.391781,1.637740,-7.088903,-8.720616,-3.489423,1.756551,6.413643,-1.175801,-7.407654,4.749713,8.477036,6.601136,-6.077830,-9.774236,-5.482057,5.853437,8.200133,1.468221,6.060226,-4.765600,-2.538347,-4.528706,4.568161,6.874594,4.730622,5.685696,-9.190207,-6.712991,-1.493270,-6.685575,7.959349,-4.520363,-5.193951,-0.575310,-9.844894,-4.533979,-5.155887,-2.015789,3.923434,-8.880899,-6.115212,6.916902,-3.136239,2.071382,2.159954,2.693101,-7.465144,8.208966,-0.423748,-7.201012,4.961314,0.796632,6.641206,2.145631,3.784533,7.557772,9.819275,4.559756,-9.203725,-3.333846,-3.060718,-2.255876,-0.280171,-8.730129,3.964254,8.367082,2.002328,-3.398675,-3.334277,5.890185,2.954474,-7.773116,5.581066,-8.402088,-7.136264,3.572921,7.094066,5.596436,-7.137911,-8.076682,-2.312430,-2.361013,-0.656872,-8.247564,-5.097110,2.871122,-4.180961,-8.188159,8.190394,5.580385,8.269535,-9.916579,-3.785327,-3.071502,7.738857,-6.003101,-1.942442,6.508678,-2.577122,-4.028950,1.762137,-5.493264,8.955788,-5.113080,-8.476584,-0.023161,-1.229223,-7.840369,7.997285,4.882593,1.634776,-4.498811,-5.425399,-2.873357,-3.097429,8.259768,-7.802586,1.066380,-7.354401,-4.538828,-5.758849,0.441855,-0.110075,6.841772,-3.867841,-6.254202,8.951095,-6.601571,1.423935,-1.715556,7.439766,5.634277,3.645209,5.198719,-8.978446,-8.604538,-0.208873,-3.156040,8.255615,-5.579981,-3.450601,0.182600,-7.484333,-6.419661,6.110713,6.847246,-7.346196,-6.926666,2.284919,-0.098939,-8.005615,-1.698218,-3.822589,9.103948,4.129546,6.832937,-7.339023,3.799533,-4.419868,-5.295233,-7.753014,-4.533513,0.082844,-3.350993,-1.535876,-5.817942,-5.271201,-1.422061,2.580861,-4.075476,0.262870,2.998487,0.222097,-4.351576,-0.463040,7.085040,-6.952316,8.966491,-4.937162,3.956620,-4.923822,2.649526,-8.926476,2.599675,6.661457,-9.724584,-7.437599,1.866331,-8.748754,0.458462,-3.155660,6.723048,3.553554,-6.895993,4.729997,-4.806209,-3.922253,-2.449569,7.572400,-9.046952,7.724347,-9.528398,-2.722547,5.522813,7.855135,0.840342,3.528479,1.928647,-6.373807,9.593363,3.360458,3.239475,5.511466,-6.144325,-9.599898,-4.388811,-2.030951,0.327099,-5.864676,0.668526,5.243689,6.715656,-1.451454,4.277833,6.078837,-3.690117,5.732759,-1.246109,4.238851,0.877401,3.346766,4.139782,-0.106130,0.619780,-5.078377,1.283550,2.735280,-9.077844,4.517055,-1.370025,-6.032191,2.147621,3.337711,9.014158,-7.888852,-0.696033,-0.893104,7.954976,-9.280315,0.165971,-7.607767,-4.732224,2.154706,7.236305,6.568241,4.134031,-4.438904,9.253783,-3.459149,-7.334666,6.370623,5.088509,-7.615271,6.945246,4.650166,8.455443,3.448854,6.887541,7.144625,0.217472,6.722143,-5.442523,4.954836,3.206150,-5.082176,-4.638212,-3.045914,8.988149,1.560062,4.812485,3.440073,-1.107634,-7.576877,-5.370939,-1.177488,-2.190000,-5.069877,9.214318,-4.762352,-5.809106,-8.940378,2.893374,-5.148798,6.349175,3.460404,-0.924531,-3.474420,1.590042,-3.399486,-5.135968,2.041058,-2.576993,2.899665,5.219853,-7.623756,2.267632,-9.624794,3.182475,5.230070,-4.906305,4.261409,-8.724725,5.553222,4.481060,9.944459,-4.150329,-8.344031,-4.618773,-6.947535,-6.765915,2.302836,8.519553,-7.455077,-9.592660,-4.374307,-3.117504,1.634726,4.818409,-8.443415,1.378592,-5.224099,-1.026839,-3.029640,-7.123579,-3.664687,-4.237689,-8.613447,5.004011,-4.302396,1.638703,4.757109,3.719345,-0.882663,5.386116,8.803602,-0.235316,4.267241,-1.037487,0.245725,-1.926891,4.446646,-0.704749,9.495053,-2.841003,3.090459,-7.261454,3.212368,-9.004704,-9.587359,-6.173238,-8.798091,5.053046,7.410236,1.232647,-4.208973,-4.959068,-7.404189,-8.023620,9.981847,-7.044879,-1.994828,7.834021,-8.822155,5.988575,7.808858,-2.601959,-6.092618,8.915844,0.172769,-4.188002,7.380944,-8.110303,0.686672,1.190883,9.254162,-2.821747,-4.303536,-1.389424,1.106625,8.382606,0.757210,-2.838622,3.606257,-4.934092,-3.044572,-5.998951,3.176186,-8.374365,9.286102,6.749453,7.825791,-7.072408,9.995781,-8.998279,-9.235834,-6.565979,9.616065,3.214242,-3.626817,0.497623,2.981060,-2.627810,-0.665453,0.872035,-0.389837,2.570870,-6.086789,0.936838,-1.194644,-5.524636,3.115009,-6.849758,2.187651,8.239464,5.176655,1.440751,0.489336,-1.420541,-6.967442,6.627427,-4.107809,-5.043232,4.122724,6.215616,5.176870,-3.253115,-5.337166,8.067751,8.649976,9.150267,8.812732,3.732521,8.168193,5.306003,2.143786,-5.403651,4.614841,2.492995,6.724843,-4.353939,-4.457071,4.053242,6.707783,3.059106,-4.105865,-6.406821,2.880646,-4.022729,5.766227,-1.767055,-5.302756,-0.491711,3.612841,-3.667719,-4.924123,5.357156,-7.145477,5.057708,4.335476,-1.743312,-7.399848,9.457205,-3.557496,-2.438079,3.008144,-6.265092,8.550068,0.022653,-5.870247,8.790458,-7.208066,-1.874854,-3.577044,0.149613,-8.038946,4.436644,-5.562585,-2.272276,-2.958578,-3.025813,0.654198,4.601304,4.632964,0.083355,9.319600,5.869768,1.235607,-3.197654,9.222568,6.177888,6.794273,-6.049111,4.304872,-0.974605,8.230542,-9.057561,2.429630,-9.296694,-4.418850,7.956443,-3.853467,-5.515295,-3.175981,7.416498,-1.695602,4.786322,5.489500,2.280717,-3.904054,-3.020929,-8.976584,-0.484412,5.020157,-0.707430,-7.811353,5.696900,-8.454809,-1.904598,-9.553393], dtype = "float32")#candidate|15311|(990,)|const|float32
call_15310 = relay.TupleGetItem(func_11347_call(relay.reshape(const_15311.astype('float32'), [9, 10, 11])), 0)
call_15312 = relay.TupleGetItem(func_11349_call(relay.reshape(const_15311.astype('float32'), [9, 10, 11])), 0)
output = relay.Tuple([call_15301,call_15310,const_15311,])
output2 = relay.Tuple([call_15302,call_15312,const_15311,])
func_15315 = relay.Function([], output)
mod['func_15315'] = func_15315
mod = relay.transform.InferType()(mod)
mutated_mod['func_15315'] = func_15315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15315_call = mutated_mod.get_global_var('func_15315')
call_15316 = func_15315_call()
output = call_15316
func_15317 = relay.Function([], output)
mutated_mod['func_15317'] = func_15317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12610_call = mod.get_global_var('func_12610')
func_12611_call = mutated_mod.get_global_var('func_12611')
call_15322 = relay.TupleGetItem(func_12610_call(), 0)
call_15323 = relay.TupleGetItem(func_12611_call(), 0)
func_9172_call = mod.get_global_var('func_9172')
func_9174_call = mutated_mod.get_global_var('func_9174')
var_15331 = relay.var("var_15331", dtype = "uint8", shape = (216,))#candidate|15331|(216,)|var|uint8
call_15330 = relay.TupleGetItem(func_9172_call(relay.reshape(var_15331.astype('uint8'), [12, 18])), 0)
call_15332 = relay.TupleGetItem(func_9174_call(relay.reshape(var_15331.astype('uint8'), [12, 18])), 0)
func_14243_call = mod.get_global_var('func_14243')
func_14249_call = mutated_mod.get_global_var('func_14249')
const_15346 = relay.const([[-4.343664,-2.191615,4.492217,-3.171198,-3.261082,-1.946221,2.250045,-9.849506,1.177774,6.971503,8.551961,8.138527,3.842355,-7.036769,5.106657,-8.197776,7.789130,0.097736,9.093285,4.671856,-6.114921,4.315795,-0.081785,-9.410731,2.375607,-2.492088,6.643628,-9.159020,-6.400348,9.396770,-2.372802,-3.973313,-1.267081,-7.924529,6.127901,5.297014,-9.772942,-0.510106,-9.729472,-6.064325,-3.238511,3.626505,-0.614518,-6.585766,-1.183449,-7.201713,1.411745,4.627166,1.484243,-5.758339,8.552382,-5.332869,-2.868756,-1.909175,3.774969,-2.308049,7.075291,-6.000124,1.836401,-2.388891,-5.010821,-4.527011,5.531834],[7.453114,-2.891688,-6.475447,-5.810737,2.849304,5.827291,8.928227,-3.201154,-6.992160,2.081725,1.682051,6.248693,8.683301,7.527246,0.209810,7.906959,7.023888,-8.073964,8.895855,-8.755684,-1.374689,-5.393703,-4.089130,4.161662,-6.017869,5.058253,-5.547850,9.505893,-7.381908,0.170851,-4.807160,5.003151,-5.014261,6.720526,-0.590961,-7.817118,3.349276,-7.024669,3.735585,-5.684136,7.655832,-5.237015,-1.222358,0.527601,-4.625171,-3.655023,8.517200,-2.571638,-4.642888,6.349887,4.609808,1.356363,-3.383236,-8.336461,8.425951,9.352187,6.205264,-2.492896,9.999517,-7.241068,2.445009,-4.982978,-3.448704],[-9.888075,-5.645973,1.384616,-4.678749,-1.672747,8.226548,-4.671125,0.055656,7.693899,2.591133,-3.576001,0.306334,-0.168484,-4.191777,1.123906,2.312593,9.170826,3.687917,8.106999,8.394142,-4.318163,1.465607,1.937318,-0.082425,1.522533,6.695085,-8.874879,-8.619172,0.154157,-1.923518,-8.971016,-6.516266,1.163499,-6.483498,8.623640,7.626317,-5.242145,9.864933,1.640735,-4.510876,9.663485,7.288784,-2.249662,4.149321,-9.229123,-5.826870,5.320660,-9.472344,-4.164927,-7.114149,-5.846653,3.249456,-8.879086,-1.102024,-6.547078,-0.497231,-4.188126,-3.546381,1.171115,-5.790417,7.817558,-3.757428,-5.334769],[1.576569,-6.887045,-1.388634,3.258503,4.085705,-3.857812,-1.068532,2.341753,9.941688,-2.506778,-0.368154,5.945278,1.157187,-6.757487,8.344556,-3.298472,1.561313,-4.087311,5.481115,-7.621602,5.749972,-5.624196,7.909779,-4.761174,-9.943580,-5.362344,3.698405,8.620080,-4.927625,-0.806710,-2.938600,2.940796,9.131505,-4.605103,0.558190,-1.806559,0.304163,-9.012831,-2.621119,0.480553,4.954920,8.720909,9.661601,6.700274,-2.028743,-8.275743,-4.183663,4.568720,5.778246,-1.875151,-9.790966,-4.001072,-1.669959,-3.668939,2.066441,2.995239,-9.843091,7.361452,1.786724,3.656244,3.352884,9.337512,2.484537],[1.553699,-9.054399,-3.109862,-0.301679,-7.678083,1.323931,6.005120,1.926933,-9.186056,-1.425896,9.214311,-9.740077,0.887947,-8.173697,-7.732716,6.558432,3.931662,9.631881,-0.612592,-5.249969,-8.567032,-5.433291,-8.031114,-3.836363,1.883400,8.026461,2.246301,6.549561,9.259674,0.044389,-0.509026,2.713613,-9.772994,3.064177,7.018431,1.505180,4.038475,5.145012,2.385393,-1.943455,-3.803155,-7.348001,-3.365429,1.005065,3.982721,5.206048,1.919947,7.779862,3.950512,3.557502,-7.894298,6.652563,-9.489377,-9.834570,-3.706351,-3.034036,-3.541769,-6.588717,-8.636898,-4.663040,-5.235047,0.560505,-0.636678],[7.920460,7.060029,-7.083587,-5.247664,-0.229834,6.961786,-8.488873,7.869052,-1.427553,0.949374,-6.092441,-4.584083,-5.604501,-4.272229,2.616777,-1.113654,1.089375,2.958800,-6.289189,8.725505,-4.584457,5.977897,-8.484219,5.977798,-7.594425,-6.267434,-7.511128,4.716006,8.345887,3.229676,-9.073147,-8.183686,5.748177,-2.648789,2.020670,-2.176866,-3.994422,-0.605390,2.464227,9.723265,6.688979,-3.406201,3.617255,-9.829427,-0.804039,3.203709,4.088634,-9.035553,0.453641,-1.694823,-3.758086,-4.263228,-1.596754,2.558221,-2.975807,1.505175,-2.349486,5.381548,0.764770,3.409163,0.022001,6.008747,-5.309030]], dtype = "float64")#candidate|15346|(6, 63)|const|float64
var_15347 = relay.var("var_15347", dtype = "float64", shape = (1, 144))#candidate|15347|(1, 144)|var|float64
const_15348 = relay.const([2.595859,9.984623,9.357810,4.438838,6.455365,-6.079800,-6.335592,8.673137,7.617665,1.727973,4.347774,-8.653816,-7.090064,-1.855714,-7.033828,-2.948777,6.423283,-0.906158,-1.835148,-1.784937,1.702595,-0.469087,-9.000467,2.206053,1.302995,5.460601,-4.633577,-5.134293,-5.931087,-1.055872,-2.887556,-1.987998,-1.591025,0.909880,-5.521902,0.934489,-8.199274,6.949685,7.390147,-1.546307,7.793303,-3.667380,-1.924820,-7.532122,3.228422,0.124495,-0.428683,-2.380868,-6.028848,1.777882,2.248098,-9.171658,-7.409318,-2.375016,-6.332020,-5.291534,9.029517,0.645074,3.633537,-3.045417,-5.651228,-9.837959,0.842005,-0.621450,-0.295505,7.476360,-3.533181,-9.751376,6.523061,-3.326460,2.231202,-5.635453,3.709216,-1.160043,7.265752,-4.004257,-4.619154,-2.237248,7.226359,-0.809601,-4.768944,3.793318,1.356421,3.604535,-3.928053,3.074292,-2.135530,-5.945852,4.556457,-7.479125,7.666331,5.036559,-6.013718,-4.280606,-4.662009,9.349450,-7.122364,0.446595,-1.154334,-4.468759,-8.012636,0.236178,0.776196,2.994610,-3.029879,-0.133878,-9.815839,-5.859676,3.967548,-7.379812,6.473992,5.116345,-2.030275,6.887281,0.286558,8.811642,4.246273,1.918440,6.286710,-7.240182,-8.821116,9.315911,-6.089888,4.887454,-0.322423,4.498444,-7.869417,5.401523,1.012417,0.261367,1.130318,-6.479980,3.824319,2.815973,-5.886629,1.852589,-5.081180,3.701110,-3.060340,9.691816,-5.260287,-7.054101,6.378900,8.904261,-9.007982,9.176199,-8.574719,7.277999,8.194139,-2.179084,-5.584859,5.146472,-6.787003,7.119215,2.502812,-0.798814,3.670076,-3.935247,-9.793031,8.211310,6.336112,-6.481936,-2.474977,7.116684,6.279596,-0.256328,9.104936,-4.091539,-0.555302,-0.995798,-6.936511,-7.451147,3.342705,-4.787927,-6.089748,7.205609,8.214972,9.882479,6.833074,6.880797,-7.312438,-3.844453,5.522221,-7.594393,-3.514982,-6.475077,8.829685,-2.710331,7.215587,-8.296446,-9.723170,4.321450,-4.402254,8.977383,-1.849355,-5.095745,-0.997937,-5.991911,2.423444,-7.211982,-0.204517,7.579416,0.366184,-8.742914,-3.815343,-5.825520,-2.407224,-6.005653,0.539978,-8.614602,2.016768,-1.314414,0.367807,2.629578,4.248322,-7.175004,-4.908576,5.666763,3.186159,3.655982,4.423115,-4.929466,1.639934,-6.625795,8.651351,-9.707204,8.184517,-2.590129,-1.302123,9.839163,6.780358,7.668646,9.512263,4.999753,-2.601172,5.727520,1.544127,-4.010838,-6.234004,9.853343,1.301963,-2.364687,-8.850812,-2.938015,7.093733,8.762108,5.149721,-5.410308,0.732152,-0.004027,-2.677349,6.970776,7.792194,9.155270,-0.553667,6.189514,-6.705432,-9.066999,5.526412,1.514672,9.937070,5.052110,8.492125,1.655639,-3.558109,2.321883,1.451410,-9.744376,-3.634918,8.608058,-4.313073,-6.151337,-6.210881,3.983462,9.566285,-1.043691,0.228022,-9.687870,-5.281395,-1.232834,8.420258,1.051705,-1.840458,8.769690,9.180260,-3.849807,-3.373127,5.953126,3.712581,-1.484875,2.070448,9.556823,-9.334079,-2.160829,-6.769009,9.728417,-2.125573,-3.903254,-6.456673,6.255615,-9.616830,8.312742,-5.939596,-0.369496,-7.944027,7.900134,6.084742,-2.538889,-3.481782,-4.532412,1.445791,-3.504355,2.972062,1.538561,-8.160782,8.599659,-4.393582,9.241398,6.360401,-2.125994,-5.507416,-0.297865,8.632198,-0.380550,2.032191,-3.172868,-1.656852,-6.962528,0.557210,-7.991444,-9.536039,5.239162,-7.941086,0.111964,-4.171195,8.316407,3.326437,-3.315659,8.693262,-5.399896,-0.249666,0.833695,1.739276,-5.614388,6.257165,7.167017,-1.461244,-7.137346,0.588928,2.624627,-9.526987,5.820538,-5.571499,-5.420863,-9.871576,-1.702893,6.332614,5.058060,1.873337,3.561201,-6.814084,-5.679533,1.630345,-3.523327,-8.757367,-7.638557,-9.377000,2.012975,-0.233787,-7.371651,-1.472516,1.904809,7.578751,7.722115,-1.863938,5.918164,4.201568,4.613165,6.423680,2.756460,4.276840,-9.077497,1.562086,-9.449782,7.934129,-9.410187,3.624222,8.250370,6.117813,6.891153,3.722841,-4.748564,-0.447131,-1.552401,3.942033,-5.175830,2.340804,0.492042,-3.649949,-4.014584,-1.354133,2.111220,-3.699297,-9.729819,2.401485,0.690032,9.590507,2.770828,-0.189461,7.170281,-5.322154,-5.979107,-1.550561,-6.816353,-4.556203,-1.414600,-4.883796,-2.053918,-5.801342,-5.254805,4.056030,-2.959781,7.743873,-8.837073,8.445314,-6.601081,8.433665,-2.726858,-3.542446,-0.694434,5.234717,3.201175,9.829854,1.555852,5.179308,3.273660,4.634816,0.451094,-1.117459,-4.380499,2.978541,9.696870,-6.550166,-0.680261,-6.412481,3.468010,8.080257,4.787173,-3.676017,-6.074580,-5.806262,-4.397935,2.105010,5.894737,-0.091460,-7.626285,-0.514101,-2.292531,9.185139,7.334000,-7.371047,5.502805,0.781412,-5.384793,7.101156,6.005405,-8.899761,-5.432961,7.603082,2.663447,4.019906,8.484985,6.854178,-9.022793,-0.783142,9.534705,-1.635857,-1.555931,9.825833,-7.733566,6.291487,1.616609,2.420826,-2.961870,9.012207,-4.269193,3.473453,-6.905273,-0.057463,4.896139,-1.817848,0.654256,7.694677,-8.776780,-3.715179,-3.051739,8.397343,4.541036,4.705225,1.732855,-7.773315,5.745391,-6.606442,-0.793159,4.565093,5.675715,-2.697877,-4.630797,7.768236,6.256756,5.158587,8.637427,9.247187,-1.641158,-8.391025,4.363187,1.209555,-4.321404,-6.694116,-3.787882,-4.658706,3.735206,-5.752436,6.801233,-1.458289,0.746269,-8.089906,-1.206064,-0.681597,-8.704746,2.677495,9.858276,-5.475700,-0.058314,-6.031069,-6.812448,-5.176809,-3.003541,-4.019016,-4.836711,-9.574218,-0.462733,4.704322,-9.590518,3.953578,-4.513049,-7.025533,-1.910502,-5.943471,2.739650,6.472883,9.246433,6.366771,9.433983,8.584639,-1.245717,1.223706,-9.941086,-4.745226,-2.518032,5.019067,-4.941451,-1.822710,2.377204,7.912330,-4.573504,-2.542184,-9.342600,9.316108,7.635414,-6.888058,-3.204174,3.220887,-7.799307,3.960367,2.198136,8.817028,-8.584597,-7.797280,-7.575555,-6.835092,7.064876,0.819589,-5.987786,3.637733,8.347032,1.156405,2.688137,2.836235,-8.411138,2.563355,3.612249,4.451428,-7.140058,7.472643,9.399850,8.794090,6.644187,3.423716,1.815267,9.836804,-3.852024,-8.105125,9.333129,6.352265,-2.683176,-1.684152,1.254520,5.622695,9.414408,3.753230,-3.273401,1.703401,1.870156,2.958234,0.406627,2.103136,-7.463754,-6.306086,6.389041,2.290222,-6.174381,-3.089079,-3.362958,8.549914,-5.494438,-4.474726,-3.181866,-0.662612,-9.965632,-0.913324,7.390004,3.304923,-8.177004,6.480123,6.304215,9.648975,-1.012668,-2.727178,-1.056240,1.568435,-9.303640,5.375410,8.876898,-7.823134,-0.425080,-9.322530,-4.922718,5.834788,4.269885,7.484832,9.816307,-7.853050,-8.626897,-9.439318,-5.991184,1.828143,-8.350331,6.139326,1.256541,9.036841,8.330002,8.768435,-5.977887,-8.534107,1.155740,-5.642330,-9.707785,8.125870,3.187921,3.274283,7.261365,-1.075086,-6.398688,3.568244,9.211313,5.454314,-3.055555,0.414400,9.153058,-2.542622,8.212541,6.387197,1.686785,-9.017872,4.420871,6.299891,-1.436484,-4.368357,3.006441,-9.627515,-1.828399,2.790687,-9.567959,7.938048,-8.805210,1.639526,6.626765,-3.822178,2.558235,9.315404,-9.495788,8.426460,9.732319,2.382985,5.622273,6.142757,5.651143,7.686965,6.495518,4.478198,-9.703850,7.057537,-7.884781,4.622959,-3.514789,-2.663027,1.275840,-3.825599,9.185315,8.819683,0.276330,-3.976855,-6.887372,6.108058,2.033654,1.679418,2.833553,9.981767,-9.374638,9.665924,4.459635,-8.112832,1.095721,3.821855,-8.057261,9.630449,-6.102143,1.621513,8.829342,-5.656936,5.498027,5.462686,8.005731,-0.036676,4.815860,-9.843509,4.315760,1.064260,1.952322,9.138958,9.551088,-5.531704,7.727639,-6.733825,-1.591622,5.373725,6.618365,-6.231213,0.143081,-7.699551,-7.856741,5.659165,7.199969,-4.334201,-9.446600,9.670250,-7.615459,7.649735,9.173896,5.328428,-7.551658,7.549154,4.753120,-9.371233,6.933588,5.136592,-3.767115,9.634203,4.028834], dtype = "float64")#candidate|15348|(780,)|const|float64
var_15349 = relay.var("var_15349", dtype = "float32", shape = (330,))#candidate|15349|(330,)|var|float32
call_15345 = relay.TupleGetItem(func_14243_call(relay.reshape(const_15346.astype('float64'), [6, 9, 7]), relay.reshape(const_15346.astype('float64'), [6, 9, 7]), relay.reshape(var_15347.astype('float64'), [144,]), relay.reshape(const_15348.astype('float64'), [780,]), relay.reshape(var_15349.astype('float32'), [330,]), ), 7)
call_15350 = relay.TupleGetItem(func_14249_call(relay.reshape(const_15346.astype('float64'), [6, 9, 7]), relay.reshape(const_15346.astype('float64'), [6, 9, 7]), relay.reshape(var_15347.astype('float64'), [144,]), relay.reshape(const_15348.astype('float64'), [780,]), relay.reshape(var_15349.astype('float32'), [330,]), ), 7)
uop_15351 = relay.sigmoid(var_15347.astype('float64')) # shape=(1, 144)
output = relay.Tuple([call_15322,call_15330,var_15331,call_15345,const_15346,const_15348,var_15349,uop_15351,])
output2 = relay.Tuple([call_15323,call_15332,var_15331,call_15350,const_15346,const_15348,var_15349,uop_15351,])
func_15370 = relay.Function([var_15331,var_15347,var_15349,], output)
mod['func_15370'] = func_15370
mod = relay.transform.InferType()(mod)
var_15371 = relay.var("var_15371", dtype = "uint8", shape = (216,))#candidate|15371|(216,)|var|uint8
var_15372 = relay.var("var_15372", dtype = "float64", shape = (1, 144))#candidate|15372|(1, 144)|var|float64
var_15373 = relay.var("var_15373", dtype = "float32", shape = (330,))#candidate|15373|(330,)|var|float32
output = func_15370(var_15371,var_15372,var_15373,)
func_15374 = relay.Function([var_15371,var_15372,var_15373,], output)
mutated_mod['func_15374'] = func_15374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mod.get_global_var('func_4641')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_15422 = relay.TupleGetItem(func_4641_call(), 0)
call_15423 = relay.TupleGetItem(func_4643_call(), 0)
func_3304_call = mod.get_global_var('func_3304')
func_3307_call = mutated_mod.get_global_var('func_3307')
const_15429 = relay.const([4.101251,0.626911,-4.689706,-0.757933,-7.661179,8.451442,2.931077,1.503081,7.601065,-0.215298,9.942071,5.348633,1.698564,-5.120362,-1.500812,-5.700300,-8.953902,-8.577165,1.517604,4.185539,-4.916769,2.266075,5.389781,0.146999,-7.062922,-1.602367,-6.291914,-2.160453,3.119849,-5.849491,-4.599302,0.101098,5.625733,5.419344,5.925049,-7.847110,8.460687,8.638615,-8.584141,-7.520223,-8.947443,1.816473,-1.491159,-5.055403,-2.554422,4.707736,-3.164148,0.889876,-2.959134,-1.242186,-8.753459,-5.069124,-6.238087,-8.879509,-8.363554,-7.908483,-3.869914,-1.043202,3.911797,-5.798821,4.045058,0.680358,1.613030,9.189648,9.825158,1.907301,-5.080145,-0.905630,8.424078,-9.980421,8.279764,-3.862826,-3.085311,-6.924309,-2.991556,5.646748,6.361997,2.592492,9.124375,-2.680046,-7.116223,-1.055406,7.195363,0.912652,-8.333284,6.874058,-4.857960,0.395853,-3.790466,6.599688,-1.295449,-2.184244,5.140471,-8.084944,3.032935,8.760894,-2.350145,-7.744579,-7.915894,-7.837343,9.480517,-1.110025,-5.897859,-8.349650,-7.986387,0.937489,-1.975318,-9.723301,0.273729,7.659756,4.704565,-7.926569,-0.410921,-4.797592,-7.167044,9.852574,-5.602670,-4.824958,4.007398,1.030909,-5.147741,9.384172,-8.879958,-1.459267,-6.046434,-9.640152,-1.377158,-2.371800,-4.264646,-1.212644,9.121075,-4.919307,6.523315,-6.332596,-9.855694,-1.811694,-5.748328,6.473649,8.275190,-9.026401,1.676703,-2.654060,0.546954,7.872308,0.802532,0.972808,5.112708,-6.428166,-2.811633,-6.840361,-6.418144,2.622463,-5.815408,3.023310,-4.485924,3.823194,0.183786,2.540252,-7.758098,-2.581321,-6.955600,4.364668,7.725803,4.195272,-9.829130,-8.370005,-3.677681,-7.848897,5.862915,0.641904,3.716403,6.739130,-7.898802,-8.929893,9.347190,-9.723532,-0.215207,-3.381528,0.353949,8.479320,2.803314,-0.075335,5.076411,-0.346700,-4.063690,-3.684274,-9.326238,-5.262223,-9.906963,-7.921768,8.878820,-1.918207,-5.880044,-4.951078,-2.910391,5.902327,0.396491,8.247620,-9.412002,9.030652,1.286571,1.954003,-4.678576,-3.757896,-7.099248,-2.734778,9.718018,2.159196,0.684662,6.761461,5.590096,8.953459,-7.948073,7.332321,-9.857344,-0.408240,-7.801280,-7.473103,0.933767,2.743797,6.744076,-4.268457,-6.826123,-9.530155,0.681524,9.583229,-5.467435,4.750281,-4.653195,-9.519574,-7.836141,-9.278200,-8.649762,8.690685,-4.254709,1.459354,-8.292712,-5.482227,7.804717,8.059571,8.812499,1.677580,4.435662,-0.955989,4.755953,8.439189,8.509693,-1.556680,-8.471563,-2.093743,-5.846428,-9.186623,0.982904,-7.046847,9.412731,3.278181,-8.983896,-9.294262,6.932645,0.943014,7.843915,-3.719386,4.117904,-6.775089,-6.397897,-2.787922,-3.840156,-8.251590,0.880577,-4.867361,-9.774344,8.955941,-8.894125,-6.021945,6.062096,-6.623384,-7.688182,2.686981,3.063158,4.482454,-2.693890,9.820973,-9.834780,-4.371947,-7.430619,-4.452062,-3.396372,8.373458,-3.190157,1.314118,-3.575176,-4.125245,-5.919812,-1.225755,-8.652005,-6.050647,9.690219,4.524901,0.278210,8.050983,0.400756,-0.630988,-1.280626,-5.066174,4.790052,-9.439501,-4.758822,6.355125,-6.759799,-6.220140,7.261077,-1.473546,-8.470492,2.418218,6.954910,4.751825,-8.478791,2.639072,-2.140624,9.052676,6.115859,5.852992,0.053244,-4.331540,-0.591683,-7.695265,3.022480,-6.084021,-7.266995,4.990246,-0.008715,-0.488116,-0.534233,7.936974,-8.225718,9.998425,-1.505882,9.042905,2.377778,-7.379033,-8.616557,5.832352,0.324045,-9.905490,3.119943,4.743825,-9.655088,3.934749,4.715005,6.557204,4.517048,3.259593,2.047040,5.626975,9.771248,-0.641187,-0.138423,9.836587,3.935291,-8.628771,-9.005708,5.182831,8.821425,7.219933,6.078420,-7.385658,1.624123,1.850697,-7.338113,0.477147,-2.295941,-4.648947,-6.833222,-6.616628,0.915956,-3.825887,-4.777489,-8.743986,-8.554688,1.711351,4.431704,7.669889,2.519102,9.459406,0.790065,4.700697,4.090834,8.305684,-7.846930,2.321571,-6.664057,8.919124,2.250927,-0.357526,8.977917,-1.243166,-0.257199,-0.481355,-0.631935,9.388514,-7.087147,9.469310,-3.129980,9.377447,-8.256772,-5.273350,6.638044,8.358340,-8.232234,-5.105916,2.605637,-2.362845,-9.864850,-9.364203,-8.766881,0.930320,-1.716332,-2.189882,3.936299,2.818193,1.624617,-9.008994,5.836926,7.127454,5.475603,-8.157436,-6.820484,-9.476066,7.149472,1.141214,4.292143,-2.977666,0.613231,-8.893762,7.224016,-3.909871,-7.414095,0.459626,3.325806,3.486715,-2.715875,2.473009,-6.167335,-9.570331,-4.478956,4.696966,-9.445573,-9.073892,3.058277,-5.811162,-9.735329,4.479620,4.533564,9.766761,1.252641,2.757512,-1.606247,0.337577,5.073609,-3.803027,9.766982,7.344491,5.493959,-7.262594,-4.180675,0.727310,7.864062,2.857007,2.477126,4.429374,5.832950,4.523832,-8.722106,-2.272231,-6.910569,9.051404,5.371374,8.804492,-0.618024,5.725111,-3.514443,-8.236286,0.778067,-1.382322,-2.842456,9.033596,-8.373983,9.641508,3.341487,-6.057636,-9.250695,-3.102096,-4.356022,-5.398884,7.169195,-3.922850,0.093050,6.777602,-2.185317,2.573956,-1.583072,3.295941,0.684836,9.250454,-0.365953,-1.009711,9.673862,-3.323760,-4.356319,0.421408,-5.059618,0.902145,-6.493775,-8.402624,-4.636666,7.471799,1.813353,-7.421464,1.338731,4.244562,5.401353,-2.877297,-0.894013,5.647209,1.508637,-4.854684,-6.120492,7.518811,8.328587,2.339755,-8.841839,-6.509681,4.256764,-6.755752,-0.638157,8.247893,-3.752709,-5.710537,-0.523853,9.405907,-5.600913,-9.952321,-1.714818,6.155990,3.878333,7.872032,4.916390,3.193304,-9.539583,6.275944,-2.156283,6.288030,-3.319156,9.383934,5.199240,4.016535,7.446527,-6.958712,9.383544,5.472522,-6.523644,-3.190604,-1.405765,4.864184,-1.183153,3.631425,4.097144,7.706365,-7.686367,-3.934240,9.007812,-7.232147,2.752881,-4.122960,-8.142680,-1.788790,9.716327,6.150978,-8.962551,-3.723622,3.926062,9.842210,-3.787098,6.794488,-4.280839,-4.471018,1.805006,-6.719975,9.166085,4.432700,-0.062270,5.118200,2.548235,7.116195,2.262450,-6.273964,5.897166,8.215943,-3.044592,-2.191954,-6.608109,-5.358644,9.409754,8.276263,-0.047669,6.628067,-4.209573,-7.270740,4.227452,2.798443,4.817400,9.987577,-0.655447,1.647302,8.186047,1.444226,-2.367486,5.953788,-8.641114,9.206052,-3.440017,8.104181,2.738023,-0.373658,0.992739,5.175448,2.803391,1.960535,0.512268,-5.155257,-1.658040,-2.759211,3.735943,2.832437,-7.291205,-5.554064,8.122154,1.096536,5.293372,0.258629,-5.123342,-2.863946,6.092415,1.006353,-7.816384,-0.408517,0.827830,9.203103,-7.216325,-5.028615,8.103779,9.061170,-2.619100,3.433444,-5.871530,-3.808215,6.519071,-3.852689,-9.960178,8.433489,1.470723,1.028126,9.078620,-8.552083,1.358824,-3.042895,4.984993,9.002037,5.695594,-8.385354,9.292846,-1.496382,4.735707,-3.309788,-8.767104,-7.182736,7.977820,-2.706602,-6.990663,-1.168332,2.442476,9.994349,6.670561,-3.306845,6.774778,-6.798705,9.591715,-8.268040,-9.542121,-7.709182,-1.188176,-2.603132,-9.590787,-9.055757,1.586708,0.690455,-0.745531,-6.606294,7.193409,-2.651960,8.654569,-7.234233,1.367218,2.502472,5.015194,-1.901255,-7.630524,1.596761,2.996273,4.347809,-3.301938,7.150553,3.923935,-7.853349,-0.659876,-4.478620,-0.907181,-5.734426,3.686283,3.931573,2.125550,-7.821557,-3.595545,-0.684723,-8.263398,6.342558,-3.847200,5.369236,-7.332560,3.434594,-6.179290,-3.475642,-2.401194,-6.003461,-7.458961,-6.448401,1.226791,0.391919,-1.981418,6.583892,4.885219,5.009451,3.826172,-5.271456,2.444435,-9.988011,2.688348,-2.020575,0.895464,0.785701,-2.957213,7.076178,-5.921435,3.684605,-7.929877,9.402846,7.096311,-8.010748,4.009312,-1.169231,-3.605817,-3.705989,5.533756,0.226372,2.622134,-2.426808,-2.912182,8.625857,-9.279327,3.550624,8.290173,5.732102,3.793300,4.109489,-6.959982,7.775516,-5.757478,-1.721976,-9.790709,-6.928855,-1.265283,7.060226,-4.858018,0.840551,-2.000594,-8.661848,-2.524118,-2.824904,9.834911,-7.308112,-7.366227,-1.335315,-2.282791,-3.329661,-2.351461,-8.422583,-4.936828,1.389998,3.960357,8.979686,6.252889,7.150325,9.567014,7.176074,-8.654074,-3.307840,-3.679943,5.954920,7.529000,1.304597,2.971572,-3.155180,-4.882106,-1.444241,0.765121,0.058003,4.276230,-3.559306,-6.502056,0.775893,0.269589,4.069571,-2.170768,-1.893808,8.144388,7.135620,-8.935236,-5.077380,8.692693,-5.359082,-9.932625,6.057544,-4.842399,4.455890,-9.050328,1.310663,-1.874241,3.203716,-8.939970,6.165606,5.099884,-7.581579,-3.375227,-2.868865,4.576001,-3.594166,-2.800272,-2.374766,6.021906,-7.732663,-1.583879,-1.187874,-3.731222,-4.890792,5.168157,-8.643643,-4.059757,-6.559607,0.138406,0.196464,0.769929,2.749141,9.577886,3.205523,5.034615,-0.363873,9.008817,-9.829242,-0.369387,-8.130939,-6.410683,3.470967,2.686768,-3.366586,-0.978450,-5.476455,3.632586,-9.902289,6.743197,-6.930991,4.073325,-8.871802,4.053001,-3.921530,1.160151,0.185329,-8.453407,6.049943,5.487830,-2.486302,1.351577,8.628415,-8.307776,7.011733,6.422726,-4.821761,5.486260,-1.717131,-3.777566,-9.211823,4.408202,5.819478,-2.408598,-2.801668,-7.935891,-4.358860,3.841041,8.747757,4.942527,4.874781,-9.947502,5.565365,-5.132649,-9.115322,-0.822663,8.597602,-6.916814,0.387770,8.315162,-8.649349,7.772380,3.824674,8.324564,-7.404928,0.611345,4.416526,-5.875152,6.183395,-3.404794,1.813374,1.723021,7.313358,4.862377,-5.853581,-4.065318,8.644374,0.390702,-3.612034,2.304420,9.094052,-7.415875,-9.706206,6.482999,8.288451,3.028597,0.596007,5.258200,-5.847536,0.773059,7.042213,-0.071839,4.851423,9.818355,-1.521880,5.428031,-0.870933,-6.097750,-0.256998,-6.843729,-7.905319,-4.130613,-3.657281,-8.865700,-0.925441,-2.718082,3.457475,-3.620121,-8.694198,-5.680206,-9.906673,3.702878,3.260042,6.452447,9.384089,9.063883,1.441604,0.973169,-0.299519,1.385006,-3.131698,-8.275938,-5.639270,-8.904237,8.957884,4.022234,-6.874245,-4.548047,-5.755006,8.100261,1.080583,8.734420,-3.765983,4.706931,-2.874359,-6.602291,-9.532821,-0.745868,5.607272,3.478137,5.561938,5.494948,0.676899,5.211217,4.756711,-0.535212,-3.832760,-1.689210,-5.245821,6.667933,-4.625786,6.577317,-6.990999,4.662406,1.545264,-4.323074,0.033984,-0.888610,9.522264,-5.924721,3.168732,-6.254583,5.338705,-4.857958,-2.900330,-4.346783,6.244511,4.484685,-9.976468,-2.474572,6.471122,-7.190255,-9.398272,-6.428163,7.165980,-7.136726,8.933224,-1.005880,6.832362,-3.141558,-5.278150,-4.119406,4.217180,0.373089,-6.278437,9.813445,4.897177,-4.087972,-8.634131,7.664691,-3.441768,-7.124964,-3.982933,-8.499920,-9.330217,0.558777,1.607613,-1.523821,6.640901,-3.902454,6.644510,-6.014004,-3.099717,-1.241883,5.894143,-3.308295,-8.464948,4.449783,8.866627,-6.485153,-7.915073,-1.397566,-5.434589,-5.355794,-6.571378,5.492835,-7.205197,-1.080271,6.046903,-7.354217,3.624394,-5.744831,9.308198,-6.199982,7.290644,-1.623602,0.072030,2.554697,-5.193436,7.865318,8.048115,-2.865532,-5.589740,-9.227476,-8.524412,-0.577276,4.659598,9.559556,-8.076059,9.598112,-5.021908,-0.800615,-1.263868,5.140524,4.836854,5.790564,-6.113521,6.062931,5.824730,-6.539043,-6.002003,7.577022,3.398565,-0.449630,-6.975848,8.890791,-1.015432,-7.642832,3.553456,7.419151,8.589784,7.143245,-3.846108,-9.828902,-5.455761,8.073266,-5.416319,-9.952163,4.756938,0.946192,-4.608562,5.969328,-7.459379,3.212736,9.252728,0.882041,-1.158752,-8.613913,6.360838,-6.521735,5.292109,-5.789823,-0.758560,4.067017,5.218633,5.872607,0.957110,-4.430457,5.527083,-7.471275,-4.311319,3.204053,-0.051560,-3.022322,-2.232547,-7.813842,-5.288133,1.496468,6.013221,9.175765,-6.007593,3.698759,8.410434,1.015509,9.495654,3.176065,8.765423,-4.412982,6.024818,9.642431,2.855146,1.646020,-3.487888,-1.476068,-3.944477,2.689324,1.871466,-7.308331,-6.415569,9.019054,0.045520,-1.733195,1.375545,4.681359,3.210874,-9.183194,-4.552841,-7.919411,1.592249,-8.768478,-5.666364,-1.506693,-8.753287,-1.395476,-9.483334,4.573086,3.097142,2.402367,-3.582136,9.168769,3.829976,6.961066,1.082655,0.882398,-8.307387,-0.020857,3.495760,-5.954286,-8.920936,-7.074805,-7.504026,-7.254427,4.640498,-6.057133,-9.131997,4.570744,-2.913063,9.138101,8.690150,-4.702083,2.512905,-3.240347,2.843450,-9.050818,-2.305633,-5.497141,-5.140250,-3.742701,-1.230380,-9.131314,-6.874946,5.617809,-7.184966,-9.482259,4.592684,4.795076,-1.091012,1.634028,6.248847,1.556890,-5.624760,-3.244676,-1.149982,8.969004,-1.638681,-7.581541,4.693637,5.809696,-4.857687,2.394087,-7.211790,-6.660272,7.551121,-1.156826,-1.072859,-6.427751,4.819270,1.634256,8.693407,3.288030,-0.733295,-8.342129,2.286850,5.383779,4.656328,1.757475,-0.317090,-3.957898,1.336293,-8.759409,-7.667974,-9.635282,5.100148,-9.245636,-7.322664,-5.098484,5.418998,3.174902,-8.092739,-2.009745,8.442853,5.989302,-3.970766,8.885629,-4.876855,2.814429,-7.546179,2.778174,3.423653,-0.326479,4.401087,2.133607,1.146430,9.431449,7.641495,-7.238321,5.121446,-6.216564,6.647235,0.163629,7.103952,3.585522,-0.819217,-5.444768,-4.029236,-6.981079,2.603612,-7.742671,-5.453103,8.191631,4.904942,-6.300714,9.618501,-0.982061,9.734779,9.471679,-8.942601,-6.675434,6.863150,1.363158,-3.685498,2.166790,3.800258,-6.427239,1.795388,3.338860,9.440448,0.371849,4.380938,-4.105756,1.121190,5.324671,-5.916992,-6.811070,-6.623192,0.686344,7.210111,3.770050,-8.130512,-0.234815,4.760447,-8.194401,-4.332339,0.739508,-8.250822,-7.217044,4.038330,2.629095,1.442205,6.608315,8.350310,-6.141029,1.873316,4.384512,-2.794631,5.565047,-5.101030,-7.256019,9.040766,-4.778430,2.655712,3.091896,-7.419758,-9.711734,0.690584,-4.851814,-6.655326,1.889114,-7.381310,6.801172,2.612850,-4.696117,1.673315,-4.535116,-5.346650,-9.859704,0.815086,8.766369,-8.302334,2.841157,3.745446,2.796300,3.862291,-7.455037,7.443396,-8.436301,-4.824431,-4.459826,5.298174,8.483809,2.899770,-0.131627,8.936852,3.621018,3.847519,2.462894,-2.511622,7.012507,-9.333580,9.047190,9.426021,-7.798328,-4.380417,1.544829,4.219570,6.199379,-5.488383,2.212837,7.993224,-7.315225,8.944727,-3.185780,-4.738071,1.991531,8.578881,-0.147585,-0.488486,-6.200310,-0.853524,3.300553,-0.570624,-8.903659,-5.411978,4.470704,-1.694831,-1.614274,5.299512,3.245253,-7.158774,-9.811232,1.269112], dtype = "float32")#candidate|15429|(1430,)|const|float32
const_15430 = relay.const([True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,False,True], dtype = "bool")#candidate|15430|(315,)|const|bool
call_15428 = relay.TupleGetItem(func_3304_call(relay.reshape(const_15429.astype('float32'), [1430, 1]), relay.reshape(const_15430.astype('bool'), [315,]), ), 1)
call_15431 = relay.TupleGetItem(func_3307_call(relay.reshape(const_15429.astype('float32'), [1430, 1]), relay.reshape(const_15430.astype('bool'), [315,]), ), 1)
output = relay.Tuple([call_15422,call_15428,const_15429,const_15430,])
output2 = relay.Tuple([call_15423,call_15431,const_15429,const_15430,])
func_15436 = relay.Function([], output)
mod['func_15436'] = func_15436
mod = relay.transform.InferType()(mod)
mutated_mod['func_15436'] = func_15436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15436_call = mutated_mod.get_global_var('func_15436')
call_15437 = func_15436_call()
output = call_15437
func_15438 = relay.Function([], output)
mutated_mod['func_15438'] = func_15438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15208_call = mod.get_global_var('func_15208')
func_15210_call = mutated_mod.get_global_var('func_15210')
call_15481 = relay.TupleGetItem(func_15208_call(), 0)
call_15482 = relay.TupleGetItem(func_15210_call(), 0)
output = call_15481
output2 = call_15482
func_15488 = relay.Function([], output)
mod['func_15488'] = func_15488
mod = relay.transform.InferType()(mod)
mutated_mod['func_15488'] = func_15488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15488_call = mutated_mod.get_global_var('func_15488')
call_15489 = func_15488_call()
output = call_15489
func_15490 = relay.Function([], output)
mutated_mod['func_15490'] = func_15490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11504_call = mod.get_global_var('func_11504')
func_11506_call = mutated_mod.get_global_var('func_11506')
call_15552 = relay.TupleGetItem(func_11504_call(), 0)
call_15553 = relay.TupleGetItem(func_11506_call(), 0)
output = relay.Tuple([call_15552,])
output2 = relay.Tuple([call_15553,])
func_15554 = relay.Function([], output)
mod['func_15554'] = func_15554
mod = relay.transform.InferType()(mod)
mutated_mod['func_15554'] = func_15554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15554_call = mutated_mod.get_global_var('func_15554')
call_15555 = func_15554_call()
output = call_15555
func_15556 = relay.Function([], output)
mutated_mod['func_15556'] = func_15556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4596_call = mod.get_global_var('func_4596')
func_4598_call = mutated_mod.get_global_var('func_4598')
call_15559 = func_4596_call()
call_15560 = func_4596_call()
func_11504_call = mod.get_global_var('func_11504')
func_11506_call = mutated_mod.get_global_var('func_11506')
call_15591 = relay.TupleGetItem(func_11504_call(), 0)
call_15592 = relay.TupleGetItem(func_11506_call(), 0)
output = relay.Tuple([call_15559,call_15591,])
output2 = relay.Tuple([call_15560,call_15592,])
func_15637 = relay.Function([], output)
mod['func_15637'] = func_15637
mod = relay.transform.InferType()(mod)
output = func_15637()
func_15638 = relay.Function([], output)
mutated_mod['func_15638'] = func_15638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15661 = relay.var("var_15661", dtype = "float32", shape = (6, 15, 9))#candidate|15661|(6, 15, 9)|var|float32
const_15662 = relay.const([[[1.885914,-7.663900,5.934385,-4.504681,-4.010821,7.809971,0.156507,6.306518,4.674745],[4.521860,9.004605,3.552859,2.508984,9.829752,4.676580,6.823176,5.359133,-4.551720],[3.399919,2.925853,2.797466,-3.225786,7.104024,1.803687,-7.642038,8.307693,0.446781],[-2.241368,7.507815,-7.807369,-3.458506,4.283343,1.247030,6.826167,-8.858215,2.849075],[9.872986,5.347539,4.389771,-5.685210,2.586561,7.267105,-3.861637,7.789910,-4.913319],[6.980727,5.005188,-0.487033,-3.018529,1.177449,4.397991,4.043588,2.960649,1.919248],[3.956939,-7.915923,1.046540,9.607998,7.795123,0.347995,2.682114,1.931612,8.932742],[8.968587,1.015614,3.026697,2.994427,9.263437,7.939762,-9.040364,-7.697940,4.176757],[-7.843020,-8.804864,7.605911,3.556569,-1.380594,7.761400,4.318278,7.951393,5.097125],[6.431383,2.239657,6.502208,4.993084,-8.885083,-6.437767,-2.635132,-9.695851,7.064127],[-3.031920,-0.776092,2.352794,5.584537,1.553143,7.213941,1.422873,5.316396,9.206029],[5.146190,-4.838775,2.679963,0.243620,-6.601067,-1.937221,9.506333,-9.953764,9.557058],[2.764952,-0.795455,3.976343,5.854223,-2.461078,-5.323756,-7.675647,1.096618,1.706996],[2.952934,-1.054227,-2.982524,4.455523,6.318620,-0.195339,4.564475,2.046825,-5.486603],[9.014921,0.345937,-1.683574,-3.659692,8.806673,-2.942103,-2.533426,8.592822,3.310286]],[[9.138202,3.912051,-2.502694,8.871368,5.532198,-3.896543,4.443392,-7.171169,8.055997],[-2.610922,8.112236,8.283494,-6.885987,5.719109,-5.908767,-2.238885,-5.830761,1.944281],[6.805629,-2.221787,9.978603,-8.538824,7.032371,-8.487787,0.514320,-9.600750,-0.691127],[-8.790725,6.153722,8.880064,-0.811187,7.734721,2.100466,-1.877619,3.192793,-6.004379],[5.011541,1.224862,7.242607,7.567735,7.031427,0.810701,-4.276363,-0.624550,1.150280],[8.109625,2.340259,-5.972861,9.415488,4.242703,-5.700014,-3.129896,-6.809603,-1.857950],[6.447021,9.942013,6.938301,-4.846567,-0.574196,2.039614,-2.608270,-3.061066,6.249689],[4.800835,0.400943,5.631162,-5.654367,2.651856,0.661162,-6.390943,0.545374,7.037703],[-2.743640,-3.898491,8.596487,-9.333081,7.231513,6.623177,-9.993051,1.967882,-7.856628],[7.806640,-2.897353,5.111926,-0.487285,-1.627849,5.177310,-9.613832,-7.090495,9.374194],[-8.052007,2.048316,-7.409335,-3.986748,3.751822,-4.668137,-0.835350,-3.166959,-7.084682],[-5.701338,4.726900,-6.053438,3.356139,-2.355476,-5.837741,8.320767,-2.665342,-6.536684],[2.314640,2.330737,-0.709317,-2.243832,5.061248,-1.853976,4.247420,-8.601931,9.432423],[1.277674,2.355171,-7.803604,2.439071,-1.103105,0.925006,-0.407235,9.618237,3.260640],[8.926602,-6.639320,3.911451,-6.765952,1.250727,6.022319,-7.427789,5.191125,8.327020]],[[6.652479,9.150148,-6.853630,-6.309555,-0.003388,-5.578235,3.132674,9.277245,-9.788102],[-7.298327,9.728371,8.276235,0.450856,-8.933822,7.146461,-9.534340,-3.972263,-6.711353],[-8.428513,-0.124548,-2.517546,5.952996,-0.731763,2.492718,5.971386,-3.258715,7.296675],[9.771373,3.997249,-5.011136,5.320015,5.724337,-6.750479,-4.732653,-8.830997,7.185410],[6.783646,-8.110168,-5.521966,-3.609525,-4.986663,-1.768073,-2.758086,-2.422253,7.691845],[-2.701167,3.725874,5.451734,2.929588,0.699227,-5.786195,-8.104548,4.972134,4.000013],[-8.612360,0.163615,-6.269583,4.769796,2.844210,-2.361911,-3.637623,-8.285716,-0.985422],[7.159969,2.903172,5.851829,-4.636312,-2.578104,9.781377,4.029703,7.008068,-9.984385],[-5.614716,1.136393,3.925269,0.607687,-6.789543,9.600271,3.702575,0.248658,9.519103],[-4.539800,-4.290945,4.080331,-3.761615,-4.940708,9.338803,-0.501637,-1.438835,-7.569759],[6.727931,8.227318,3.829620,3.503854,9.436561,2.031066,8.175604,-7.361822,-0.958159],[3.669660,-4.034166,9.422903,-6.931845,-6.570093,0.347574,-9.860514,-8.921494,-9.511358],[7.005946,-4.547782,-3.590369,5.709696,3.804442,-1.219243,-7.568969,-0.794929,2.563302],[-1.205079,0.046704,-1.497182,9.533086,-2.822766,-8.443274,9.272732,-1.194654,-5.631135],[-3.684310,-2.893390,-4.387376,6.760253,6.299729,2.257463,5.829055,-5.508680,-5.728814]],[[2.489004,-1.314090,9.398704,9.925745,-5.100993,-7.519106,-2.925839,-0.353534,-7.629173],[7.106542,6.150499,-4.001996,0.240274,1.031013,-9.307807,-8.477563,9.216319,1.790263],[1.844488,-8.124233,-1.678242,3.026873,6.813020,-6.895557,-0.705546,8.140809,-4.833906],[-9.916634,-6.558034,5.925039,-4.185878,-9.453082,-5.053117,-2.180203,-5.669642,1.119154],[-7.852084,-3.814949,3.361450,5.300660,-1.834965,2.398717,-4.917844,9.934984,1.546848],[-5.995623,-1.981832,-5.505727,-5.160952,4.014891,6.777116,-1.019457,4.461680,7.846077],[9.802710,-4.775363,1.523657,-4.933891,8.627453,-8.216256,-8.841822,-8.983499,-1.932097],[-3.138551,-8.445961,0.348674,-5.486432,4.875887,-0.370813,-8.826607,3.962980,-4.303281],[2.565514,5.493602,-0.218574,1.279470,-7.686645,7.626487,-2.087542,5.680213,8.060371],[-8.756896,-2.464774,3.291023,-4.872321,-4.001969,-8.210261,6.796768,7.915759,9.068616],[-1.749935,1.381773,-7.622937,1.944636,-5.934950,3.407928,-6.211534,8.657012,6.376267],[4.697102,2.603263,-6.264281,-3.465769,2.097910,-1.008066,8.928894,6.083970,5.729638],[-2.196841,4.206666,5.700549,-8.993912,-9.422816,3.502108,4.261387,-4.263853,-5.428744],[-6.598063,-6.243333,3.321027,-7.161127,0.892241,8.083979,-0.278042,-4.532668,-8.072657],[-0.245799,4.809969,-6.775625,6.213003,6.773133,-7.267436,-8.951895,5.257708,-4.026028]],[[2.749630,0.925047,4.319584,4.807866,-9.283078,3.608778,6.047791,-1.631970,-9.676268],[5.998863,-3.922083,3.896877,7.956629,1.584717,-3.071393,0.485545,2.328063,7.194719],[6.427401,-3.684869,-4.673678,-5.140444,8.274445,-8.036639,9.245178,1.177926,-4.489937],[8.219917,-9.467910,-7.787412,-3.300244,-1.432304,0.686512,-4.506879,-7.283680,-0.181994],[-7.276550,5.078065,5.872272,-4.540381,3.149011,-4.772963,-6.575875,3.171430,2.593391],[-7.134891,8.320284,2.641053,-4.683559,0.410915,-2.209694,0.833880,-2.621717,-5.645967],[-8.021482,9.180349,2.959481,5.969705,6.782615,-6.239117,8.459940,-2.323818,-6.331140],[2.176485,-4.602092,9.544640,-5.778911,4.459421,4.562531,0.444800,-0.571601,-0.285785],[-8.835373,-4.844207,-3.004637,-4.441018,3.177818,8.710687,-6.068939,-7.182284,3.044162],[1.638531,-6.102893,9.967664,5.493838,3.604401,2.158914,1.588701,2.699547,2.923818],[-9.503957,3.943585,-3.588354,5.202844,4.350959,7.653035,-1.615877,2.798799,-7.216962],[-6.081440,3.545597,6.122605,5.249566,-9.300849,-8.401761,7.938933,-3.951397,-7.637275],[9.954422,7.089164,4.583547,0.379504,-7.054017,-2.901298,2.579166,-1.287730,-0.609614],[3.438006,-4.043970,6.805432,3.776893,9.573064,6.757699,6.357986,-1.805120,-3.464283],[6.257093,3.034996,-4.542005,-2.345316,-7.430321,-8.766868,2.241516,4.477156,3.728451]],[[-1.080777,2.291853,-9.908390,-8.221506,1.881661,3.615883,-3.573968,8.645857,-1.781177],[-0.726703,-7.784381,3.282674,9.750032,-5.625510,-3.177221,7.745949,8.418492,-2.526016],[-2.475525,4.326661,6.901429,8.259829,4.836464,8.655887,-6.768196,9.734310,4.330957],[5.036910,6.974900,6.772664,3.667324,-0.278756,3.523411,0.397332,1.374148,6.370012],[5.011553,2.832632,2.382593,-9.475245,-7.518796,-8.679557,-1.829665,-9.809316,-7.094548],[9.328081,1.851784,-9.712170,-8.919089,-9.472834,-3.413385,9.260643,-9.618947,-2.459383],[6.033236,8.036234,-9.640466,7.496158,8.413389,-2.567834,7.150675,5.269313,-3.151856],[4.085301,6.283500,-1.528207,2.721253,3.877908,-0.274343,-1.577195,-6.588062,5.576694],[3.090727,3.280226,5.486382,-2.554085,2.026722,5.754645,8.390459,5.558326,-9.207611],[-7.946122,7.740762,1.071223,-2.816588,7.244603,1.478448,7.802516,-9.657680,8.307404],[4.404655,-4.034622,4.005607,-2.512337,1.896872,-2.564559,0.961381,1.205294,-8.996494],[2.955092,-2.043632,-5.073110,5.371228,7.423373,-0.762787,9.092106,-6.932474,0.707232],[1.927489,2.943026,0.004619,-3.311262,-3.163484,3.114379,-6.088757,4.129483,1.926331],[-0.560931,-1.790056,-0.907860,-9.413383,-8.868789,-8.675377,6.409768,1.573430,-2.140318],[-0.929836,2.311808,-9.483082,0.089167,0.759542,-7.511712,-7.554989,-6.437660,-4.419290]]], dtype = "float32")#candidate|15662|(6, 15, 9)|const|float32
bop_15663 = relay.floor_mod(var_15661.astype('float32'), relay.reshape(const_15662.astype('float32'), relay.shape_of(var_15661))) # shape=(6, 15, 9)
uop_15673 = relay.sqrt(var_15661.astype('float64')) # shape=(6, 15, 9)
func_6715_call = mod.get_global_var('func_6715')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_15675 = relay.TupleGetItem(func_6715_call(), 0)
call_15676 = relay.TupleGetItem(func_6716_call(), 0)
output = relay.Tuple([bop_15663,uop_15673,call_15675,])
output2 = relay.Tuple([bop_15663,uop_15673,call_15676,])
func_15682 = relay.Function([var_15661,], output)
mod['func_15682'] = func_15682
mod = relay.transform.InferType()(mod)
var_15683 = relay.var("var_15683", dtype = "float32", shape = (6, 15, 9))#candidate|15683|(6, 15, 9)|var|float32
output = func_15682(var_15683)
func_15684 = relay.Function([var_15683], output)
mutated_mod['func_15684'] = func_15684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15315_call = mod.get_global_var('func_15315')
func_15317_call = mutated_mod.get_global_var('func_15317')
call_15706 = relay.TupleGetItem(func_15315_call(), 1)
call_15707 = relay.TupleGetItem(func_15317_call(), 1)
func_14314_call = mod.get_global_var('func_14314')
func_14316_call = mutated_mod.get_global_var('func_14316')
call_15725 = relay.TupleGetItem(func_14314_call(), 0)
call_15726 = relay.TupleGetItem(func_14316_call(), 0)
output = relay.Tuple([call_15706,call_15725,])
output2 = relay.Tuple([call_15707,call_15726,])
func_15733 = relay.Function([], output)
mod['func_15733'] = func_15733
mod = relay.transform.InferType()(mod)
output = func_15733()
func_15734 = relay.Function([], output)
mutated_mod['func_15734'] = func_15734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9883_call = mod.get_global_var('func_9883')
func_9885_call = mutated_mod.get_global_var('func_9885')
call_15752 = func_9883_call()
call_15753 = func_9883_call()
func_3152_call = mod.get_global_var('func_3152')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_15754 = func_3152_call()
call_15755 = func_3152_call()
func_12313_call = mod.get_global_var('func_12313')
func_12316_call = mutated_mod.get_global_var('func_12316')
const_15777 = relay.const([-5.660444,0.363547,9.877667,-7.466752,-7.489731,0.302615,-7.830706,-9.606078,4.839068,-2.615285,-4.519752,3.847310,-4.827030,-4.761206,-0.339682,-6.577585,-3.580131,5.039613,-6.840217,-3.001797,2.277513,-1.049525,-4.015714,7.505461,9.741660,0.400111,0.678319,-0.596791,6.759031,1.293833,-5.747005,0.067954,-6.893686,7.143723,-0.219508,4.330189,7.807490,-0.525968,-3.347975,5.261499,9.214519,2.496985,-0.538116,-3.226384,2.746682,0.603106,-4.964394,-4.369035,2.388797,3.380337,7.371236,-1.578377,-8.045632,-0.289041,-5.943896,-2.181131,-4.325123,3.409966,-9.543237,2.269247,2.658932,7.174544,8.321460,-5.839408,6.231395,-8.082228,-3.573448,-7.621123,7.428642,-2.686500,-1.112330,9.043011,-9.317177,9.697815,8.858263,-4.558795,-6.448151,-9.824565,-2.679789,-1.898777,-7.753137,-7.937701,3.707048,-4.721559,-1.246186,7.481043,6.816692,6.344653,4.092147,-7.601802,8.507265,2.357154,7.933195,4.242245,8.533235,1.957057,1.686494,-5.157310,-1.514853,8.278460,9.974852,-4.966464,-2.843075,4.778705,-9.154184,-1.774764,-9.041500,5.859314,1.969856,6.408260,4.941986,-8.993436,0.266579,7.387277,5.483580,-5.919396,2.872454,-4.225210,-2.673438,3.287683,5.145934,2.552672,-6.845315,9.376720,4.312978,-9.909937,-6.310951,0.721161,2.015721,2.772648,-7.732268,-6.197509,-5.201773,0.294079,-8.985724,-4.363630,-4.525720,3.119848,-0.928482,-0.810651,-0.954969,-8.550506,6.179528,-7.370656,2.332838,-5.384704,2.086102,9.885008,4.336376,-5.082248,-1.966680,7.174764,-6.307859,1.983097,-6.457083,0.885372,-6.400900,8.563771,9.396640,-0.848357,1.388043,-1.893129,6.645280,4.676387,-1.553424,-4.506114,-1.136691,6.179182,9.876552,7.694908,-7.469055,-0.956573,3.757140,5.272680,4.879261,5.104212,-2.050828,9.629272,5.063115,-0.437383,-5.347331,-0.830668,-6.177095,-7.537806,-5.266423,8.018563,-0.057478,9.325825,4.784098,-1.791307,5.807373,-6.057393,-5.374716,6.278949,-1.768801,4.186878,5.886167,4.819625,-5.897756,6.108909,7.472796,8.081610,-6.418995,5.101791,0.827977,-9.567669,1.957068,-3.920383,-5.702207,-0.553946,8.171396,1.779383,1.675503,5.710827,-2.130291,2.797797,7.740684,8.331608,1.492136,-7.212276,9.764100,3.571530,0.595477,-0.906972,-3.442848,-7.528420,-7.130846,-2.630748,-8.639111,0.636167,-3.321661,-6.937825,-0.914105,3.969711,3.726269,-2.706756,-4.988069,2.904969,-4.052258,6.993020,-8.741667,-0.065915,4.824334,6.430853,-9.874713,0.200681,9.991498,9.946684,3.006013,4.389594,-0.694205,2.707211,-0.289625,-2.715733,-0.711987,0.561091,0.208839,-0.936820,-7.583330,-9.806423,-9.987250,3.162932,1.436292,3.520314,5.616834,4.401419,2.049687,-4.315029,-9.127887,-2.014712,-3.227765,5.958590,8.345388,-5.818927,9.027944,6.716296,-9.153697,8.066124,9.422687,6.109058,-4.564717,-9.946869,6.898637,5.993300,0.461717,5.031578,3.856772,4.700191,-5.293443,-1.273345,-6.038273,3.594206,-6.307707,-6.411690,-2.492084,-0.031637,2.027343,-1.087346,5.129216,-0.872440,3.738391,-1.521288,-4.143481,9.532048,2.199557,9.615924,9.279210,9.999460,9.783761,2.398135,9.692182,-4.450162,-8.461231,0.689101,-4.043370,-8.416601,1.510060,-9.003068,-0.318227,-7.942320,7.625771,1.510838,5.262652,-1.083728,3.871709,-9.965503,9.653291,6.103097,3.330170,6.661616,-5.478444,0.344817,-2.972999,4.712502,9.268452,8.524749,0.022544,-0.287045,9.320644,-6.499400,-8.808356,9.440764,4.678293,-3.835316,0.540527,2.167044,0.126441,-5.526875,-1.689028,2.391058,8.498366,6.535456,8.090581,8.343371,-9.489345,2.650687,-5.614104,9.273318,1.586601,-6.353814,5.813402,-5.302430,-1.928744,2.268733,4.352342,6.324390,2.854950,5.749590,-0.785680,1.241791,-3.801514,4.135907,9.299635,1.536445,-9.265388,4.690385,5.118150,2.195126,-7.629583,-7.823046,6.780063,4.649647,-5.267572,4.485917,8.629505,-3.920151,-2.824619,9.833451,-8.889954,-7.321988,-1.228187,-7.182608,-7.416207,-7.947215,-5.040819,-1.213383,-6.582265,-9.538764,-8.701305,9.002593,-7.433529,-3.799434,3.814589,-9.863127,-0.426563,5.752134,1.660392,-7.321288,9.600618,-4.192058,7.957877,5.159959,-1.026671,4.885401,0.252672,9.502434,-0.306685,-9.196012,9.077848,1.869516,-4.152199,-0.455451,-4.645768,7.681382,0.785446,-5.462227,-1.722505,-2.369046,4.254543,5.423460,-7.537301,9.106548,-9.151886,7.307995,-7.063041,9.825642,9.334448,-8.242135,-1.394852,9.400681,-4.029379,8.465010,2.365977,5.993106,1.480195,0.528504,6.191390,-3.475437,6.140280,1.108952,-8.972466,-1.999027,7.012574,4.214397,-8.231806,8.095394,-7.642086,8.210262,7.122488,3.050046,2.664956,-8.343560,1.188985,1.647005,-4.980021,-7.230913,5.574558,-2.873418,-2.243784,5.612223,-7.105051,6.587428,5.670922,-8.023191,2.236389,7.868911,4.497523,-1.025150,-8.114451,9.273885,-4.321468,5.483110,-9.059038,-0.772435,1.832160,8.561009,9.530667,7.847040,5.666124,2.331787,1.073127,2.311791,-8.283158,8.048794,7.588029,-6.027332,-0.706650,-7.445375,1.367070,7.242458,-3.592620,0.574181,1.596769,-9.570263,-4.652494,-4.039673,-0.500882,-3.015612,5.751249,8.544584,-4.280186,-2.936003,7.684360,8.293857,-6.889276,8.466011,6.734114,-7.281384,5.697922,1.643811,-1.389229,1.042864,-0.888120,7.312751,7.309083,-2.093713,-2.708457,2.684426,2.428879,8.031867,4.542871,-0.480674,7.068348,-0.456658,6.203913,-4.569958,9.761661,-6.608713,-3.252529,7.033899,-4.968982,7.443837,-6.760155,-0.400405,-3.100467,2.522018,3.862646,-7.335379,-1.108642,7.842392,9.021321,3.190933,-2.835135,-7.338032,-3.307705,-7.157748,6.073094,9.201357,-0.763652,-1.870570,3.296008,9.814661,8.919648,4.646855,-3.730182,-9.049305,7.912564,-9.698448,4.644898,-8.799062,-4.208936,4.462528,-7.874931,1.864978,-5.459883,9.261383,-5.456133,-5.900596,0.009913,4.576915,7.997906,6.999061,-3.280679,-5.392711,-9.551252,3.951415,2.353437,-7.443453,4.837344,8.296888,7.226496,-6.930752,2.482137,-1.760504,-3.705524,-4.913473,6.558411,-0.825758,1.238164,7.283658,2.274083,-2.575685,0.001659,4.349030,-3.039522,6.305513,4.771950,6.750109,-9.508464,6.089119,-3.501400,-8.862814,8.592493,1.457671,2.167637,-4.068715,5.261807,-8.685455,-7.604947,9.440122,-3.402792,-5.893092,-6.440118,-4.148323,4.035985,-8.743430,6.525973,8.584307,0.718286,7.984612,-4.377316,-3.116973,-8.181441,-3.802397,-9.481362,4.597051,-4.671689,-2.538064,-8.078394,-3.096302,2.586807,5.986900,5.679885,2.671548,9.728497,-2.372360,0.978017,8.244220,5.428683,-7.408933,4.663394,-8.834359,3.183891,7.917687,3.086177,-1.195240,-8.356732,1.140282,-6.902050,-1.088697,4.821790,8.840815,7.471598,-8.616524,0.060012,-2.727697,-9.554905,-4.684506,-0.358922,1.485231,4.106423,-3.176816,0.388031,-3.847953,-1.507365,4.741529,7.204943,-9.470761,1.393200,4.630695,3.148525,-4.837826,-3.231316,-1.303435,-9.755847,-9.373043,9.002528,7.210355,-6.448824,-7.461735,-7.754593,-7.307668,9.816440,8.173127,7.960487,9.348222,-8.063563,-8.271688,-1.649700,5.389158,9.684874,9.326665,-2.733164,6.475688,-0.973530,-5.514893,-6.625340,-5.466389,5.625694,-0.902131,-6.129731,-4.130828,5.554898,8.358339,0.387651,-0.264977,-2.986300,9.568395,-3.120721,4.065598,-6.310232,-4.045277,-4.878437,-3.872225,-7.310801,-3.038188,-9.343770,2.999355,7.861428,-9.656050,-3.419812,4.958978,-0.447949,7.549554,-6.844579,0.771821,-8.467258,0.279316,-4.749747,1.179737,-9.770263,4.350105,-2.005914,3.804196,0.857804,-7.010241,-2.734387,-1.852368,-3.029415,-1.644794,-5.621183,1.907732,2.693107,0.030968,2.337069,-0.571980,-4.797735,-0.010665,-2.088368,-7.098189,8.260479,6.384343,2.097152,-0.624556,-4.305372,-2.159472,-7.968582,2.596045,-6.794879,7.843848,8.870050,3.873055,5.114658,-8.375561,0.938732,9.119450,1.707585,3.281750,-6.189155,-0.942045,-9.121722,3.367145,9.156106,-5.802541,0.040023,4.745584,9.367365,-5.500862,-1.794155,-2.578346,-2.795511,5.279109,5.510032,-4.619062,-6.685139,-3.101846,1.145106,-3.182614,-4.525909,-9.060451,-9.789648,5.094751,-2.901425,6.373579,-8.156358,4.234472,0.886938,6.525152,5.038251,6.915535,-7.660067,-2.630552,3.719752,-3.978940,6.869572,-0.831507,-9.187493,8.697006,7.355776,-3.387806,-8.961202,-7.450504,-7.941150,-1.687466,9.655437,5.399881,9.451136,9.105745,-1.217376,7.690712,-3.522047,-9.600821,6.298488,-6.509530,-4.819800,-8.493960,-3.904642,-6.163400,-4.744157,-1.558340,-9.179671,-4.429416,7.361216,2.857755,0.479799,8.566662,-5.948658,6.690219,5.192347,-7.905184,-0.756726,-3.295286,-2.148245,3.499022,-4.171624,-4.548884,4.763786,-9.358875,2.036468,1.488168,-9.474722,-8.319865,-0.217809,-8.824565,5.740156,8.224754,-0.824436,-2.427439,-1.726457,9.497455,2.824874,-6.125167,-6.284337,4.195615,-5.177331,2.469876,3.615003,2.325037,6.578739,8.566525,-5.518144,-3.352355,1.329861,8.711589,-2.850641,-8.926496,7.180911,-2.435191,7.506818,7.196577,-7.231978,5.055449,-2.754629,9.006603,-8.486248,2.260299,8.294976,5.624819,-3.082954,4.316263,-7.279452,5.338677,-9.201176,7.946612,7.864251,8.547549,2.430585,-0.466311,0.293554,6.807640,-2.364424,-5.474587,-2.831826,-4.592956,2.216190,2.664808,9.785034,6.579918,5.092187,-0.946343,2.899013,-1.505376,-6.548828,-5.234868,0.451518,8.108621,-9.309992,6.783050,-3.017182,-5.483500,0.131278,4.894050,-1.988746,-1.634761,2.179389,-7.584686,-3.180257,-2.227074,2.165822,-4.160095,-9.977336,6.773113,-0.530197,-4.982999,-1.483022,-5.055121,-4.229831,1.416742,-9.308360,-0.348044,-3.791948,-0.302764,-8.597905,0.411132,5.251798,-4.200502,6.526776,9.152523,-0.819837,-7.107682,-2.284911,6.128734,-3.933520,1.165313,-8.077432,7.730168,-0.100710,-4.515465,-2.236871,7.198401,5.177312,4.637821,5.210396,-5.100649,-8.117255,-1.638703,6.721744,-4.486878,-6.476607,-9.712836,3.507186,9.140930,8.285697,-9.956830,6.190270,-2.411472,1.633630,-2.946496,-6.755969,8.890165,2.583355,4.428661,1.357498,5.163159,1.598597,-1.596821,0.905655,-3.337200,9.186123,-6.253082,-7.274256,-5.957838,-5.690333,-8.051471,1.827672,-7.716610,-9.884364,-7.599753,7.789491,9.298881,3.381549,1.289611,-9.736701,-3.027429,6.745456,-9.281315,0.439435,0.266728,1.258921,-3.162444,4.575174,-0.222437,-8.640158,0.206204,-8.513961,-0.474598,1.881893,-8.169059,9.586121,3.206488,8.254065,0.434805,-1.563619,-7.046461,-3.862860,3.209536,1.294268,3.933608,-3.975005,3.158309,-6.667496,-0.010495,-5.412936,8.407434,0.046741,-9.049967,-2.942186,1.379091,-1.470154,8.326946,-0.307267,8.464220,-6.670678,4.541000,8.551631,2.718271,-9.713034,2.741652,-2.636720,5.003051,-8.210747,-0.382597,1.750662,6.975084,7.449095,-6.017436,6.485615,-2.726452,0.232530,-2.679978,-6.434884,-1.220912,-1.727987,2.678541,-5.702611,-7.857457,-0.681376,5.827058,1.482182,-9.433363,5.951752,-6.675505,-4.528646,-5.820787,2.031851,-9.324149,-8.396198,-7.972460,3.856120,8.269547,-3.961538,-9.842118,-0.059939,-0.196931,-2.929782,4.491476,-8.629790,6.015047,-7.311745,-6.855938,-7.771823,1.579687,9.744690,5.469071,-4.873208,-3.281603,4.994942,5.459333,-3.136318,8.972214,-6.355078,4.541131,-1.777972,4.416545,-4.475005,-0.560290,4.343048,-5.640153,-4.627015,8.145835,-1.097464,2.330655,-9.113138,-6.860004,2.901651,8.120450,-6.178740,-1.197294,9.288411,0.835064,2.440435,9.117633,4.972760,7.694149,2.880016,-0.629404,-4.393879,0.192575,7.597190,1.993144,0.392764,-0.405925,3.334692,7.786191,2.072981,4.625838,-8.236187,3.609350,-3.983293,7.957867,7.769682,6.464076,-6.958721,-1.928586,-7.662747,-0.586347,-3.068839,4.995231,2.260955,3.563024,1.871969,9.507661,3.387846,-7.580494,7.757815,1.206911,2.112247,-9.434943,-8.211979,8.278689,-4.579475,-2.202101,8.988562,8.837700,-8.608587,2.821474,7.007584,-2.996961,1.549849,-8.773310,-2.326312,9.816723,-8.702638,8.603124,-5.629405,-1.371717,-4.825097,6.369311,-6.763119,-2.348054,6.290112,6.407480,-4.539329,1.719275,-8.977287,-5.296926,-8.851341,-6.122043,1.755554,2.888838,9.457991,0.451277,-7.393387,3.252564,4.164991,-1.028310,3.774624,3.765364,8.797595,2.977849,-8.072455,-1.746691,8.355276,0.635918,0.101820,-9.320581,-3.720156,-7.437465,-9.922168,-6.225421,-6.466450,7.465597,-5.383324,9.130203,3.257014,0.098149,9.916226,-4.195679,-9.291672,5.576870,-2.908689,-5.773944,7.099372,-0.516565,-9.851666,9.914447,7.504485,-9.063662,7.009145,3.410285,-0.764783,-5.406958,-5.278898,-8.927285,2.249161,-6.912201,3.908462,-4.504498,-5.791411,4.040000,6.607790,6.803170,4.625442,-6.342657,4.156285,9.699520,-5.711519,0.367648,8.060886,-5.781607,-1.483884,-5.201452,3.823647,-3.112959,5.209326,4.829976,9.115736,8.658947,-4.475496,8.871598,6.288523,-3.516093,0.551406,9.915736,8.993958,2.041454,-1.249044,-5.584503,-3.914265,9.713694,-4.918474,6.675347,5.434054,-1.420671,-2.635344,-2.374405,-0.232905,-8.398812,-6.444627,-1.315048,4.672649,1.770355,-8.528000,5.441806,7.465963,-5.955722,4.758245,7.314793,0.550235,4.491186,3.478234,8.053821,-1.856811,4.857824,1.331082,-3.089876,9.789978,1.539734,2.882507,7.495354,8.806130,-4.400498,1.964783,-4.646746,7.081073,-3.341927,4.983120,1.091894,5.094311,-4.831959,-4.615684,0.212391,4.126093,9.766292,-7.420774,0.260796,6.108591,-3.084716,8.770899,4.160833,-7.484464,3.629065,3.516270,5.721488,-9.457871,-3.177362,6.477175,-1.059988,-2.695108,6.922334,-2.307123,-2.937936,8.870320,-7.623767,7.488582,9.696538,-1.921841,5.728181,6.952657,-9.288756,8.158638,2.713220,2.882927,3.588886,2.352953,-7.602949,7.007854,0.613934,0.810483,4.232723,1.730257,2.890842,4.507459,-0.051825,8.374261,-2.125685,0.294183,1.495169,-0.557420,-4.678916,-9.884610,6.786246,7.691111,-6.915767,9.090017,-9.848349,-8.423082,-6.557442,-0.161448,7.631846,0.607064,-8.142841,2.440420,9.498701,-9.286127,4.644969,-2.528454,-2.594262,-4.557069,0.570287,-6.193815,-1.572739,7.969199,8.015307,1.164630,2.561954,-3.864977,7.581654,-6.954750,9.513132,-9.476177,7.581970,-4.734857,3.947877,-6.405603,-7.175646,-7.545202,8.602531,2.843178,6.318956,8.342098,7.196895,1.637663,6.022364,-1.441933,-7.315100,-4.096565,8.105815,-1.913061,1.213478,1.206766,9.532182,-0.004375,2.916075,5.035399,4.263839,-6.379824,9.293318,5.165251,7.056830,0.074190,7.623835,6.419259,-6.470503,2.465822,-1.928439,4.931930,-2.719565,-5.194579,7.972423,-4.334886,1.745941,-4.743389,-7.918075,7.184717,9.984812,-2.458024,-1.556647,3.811805,8.591752,-3.876736,-6.080354,4.944140,-8.454456,-4.644516,-7.950139,-6.927558,4.750797,-6.339549,-3.259914,8.539559,-8.863028,-7.408062,2.840457,-8.470406,-5.154849,-0.945035,-7.466972,2.359513,-8.331745,4.230996,4.111524,-4.043069,-4.485478,-2.772395,-8.135483,-7.274536,7.688271,-8.477151,-2.654426,2.120177,4.952419,5.292570,-0.162108,-4.860703,7.731646,0.526224,7.478224,4.641883,-1.917765,1.028898,-5.763335,4.331520,-8.182422,-2.568637,-4.007131,-3.641696,-4.651968,-6.669443,-6.236245,6.489607,-4.173167,-3.317785,-3.585992,5.842989,-9.073035,8.177251,-3.882763,-0.791242,-1.600414,3.275298,0.323214,3.013490,-9.478937,-1.011003,-0.644567,-6.083961,-3.036860,0.102210,-4.330638,3.263886,1.756074,1.774626,9.387643,-2.797818,3.100036,9.891881,0.331839,-1.843946,-2.599008,2.899945,-0.014856,0.508113,-9.793062,8.137017,9.721839,1.886881,6.396743,-4.769710,6.575032,9.822162,-8.438068,6.592736,9.228725,2.854208,-4.795943,-3.393813,-1.010022,7.090694,-4.735463,-8.862198,8.398871,-0.076900,-2.316780,5.025315,-5.304301,-8.282221,3.159382,-0.155651,3.549020,-9.396705,-3.368101,-8.026449,-3.475869,-1.912504,-7.154130,-5.173533,-5.630190,0.288118,6.041117,-5.351582,8.152822,1.957090,-4.909257,6.429744,2.198322,0.893294,-5.302273,1.152099,6.392298,-4.971722,-1.536150,9.970771,1.123294,5.356285,-2.643466,-6.915339,3.513713,-2.367115,-4.625784,2.889090,-6.762010,4.390263,4.793159,2.128277,-0.651304,-1.271307,9.541581,-7.472096,-6.142513,4.614677,5.149430,-1.226208,4.689864,6.247120,-8.680552,-3.403276,4.682030,-7.719761,-4.796197,-4.262937,1.187829,3.321880,-3.779894,5.480668,2.572700,2.036811,1.572470,7.799511,3.262315,-1.108408,-0.652862,-1.973521,-3.127977,-7.001183,-0.569076,-0.975060,1.942121,-0.760651,3.535600,8.921876,8.092476,1.321877,-4.515550,6.261433,7.468315,-2.768319,-3.223024,-0.802625,6.102346,8.712465,7.144170,6.511719,6.040116,-7.084495,3.216782,-4.023981,6.490698,7.864741,-6.045199,1.930683,-4.316677,8.029488,-4.776684,-5.241783,-1.722613,2.191858,2.856132,1.189370,7.912404,6.235595,3.083381,5.164418,9.464699,-0.977171,1.694964,-6.605415,9.503391,9.024934,0.921272,5.465928,2.913185,6.532551,1.001561,-1.642810,-8.095830,-6.145244,3.208064,-1.274067,-5.637945,-8.099433,-5.505511,-8.422881,7.401395,7.269362,7.500910,-9.453210,-2.111538,3.466171,-9.917440,-3.816970,0.952439,-3.095865,-0.645362,2.972604,-6.389729,-1.873303,-4.637048,-2.738394,-7.951145,-4.856720,8.310354,8.949526,-7.902022,3.000161,-4.579275,-2.276379,-9.160893,-4.553219,3.903526,-7.428878,5.762493,3.417791,6.855239,8.196032,8.331685,2.807280,6.118970,-4.970498,5.143931,-0.645713,1.933490,5.408434,-1.100204,-3.868287,9.586200,2.029918,-0.898953,0.872405,-3.781472,7.035670,-3.824861,-1.082307,8.446352,-4.683161,6.739034,-7.989522,4.664454,-1.807251,4.428402,8.637010,7.647131,-6.602701,9.904119,9.078570,-3.521432,-1.050294,4.950030,-5.682694,0.272842,2.227909,-3.067977,-2.244843,5.957104,6.080775,8.917924,-9.946281,4.074085,-8.266178,-8.107150], dtype = "float32")#candidate|15777|(1760,)|const|float32
call_15776 = relay.TupleGetItem(func_12313_call(relay.reshape(const_15777.astype('float32'), [1760, 1])), 1)
call_15778 = relay.TupleGetItem(func_12316_call(relay.reshape(const_15777.astype('float32'), [1760, 1])), 1)
func_2653_call = mod.get_global_var('func_2653')
func_2659_call = mutated_mod.get_global_var('func_2659')
var_15780 = relay.var("var_15780", dtype = "float64", shape = (140,))#candidate|15780|(140,)|var|float64
var_15781 = relay.var("var_15781", dtype = "float32", shape = (1430, 1))#candidate|15781|(1430, 1)|var|float32
var_15782 = relay.var("var_15782", dtype = "bool", shape = (315,))#candidate|15782|(315,)|var|bool
call_15779 = relay.TupleGetItem(func_2653_call(relay.reshape(var_15780.astype('float64'), [140,]), relay.reshape(var_15781.astype('float32'), [13, 10, 11]), relay.reshape(var_15782.astype('bool'), [35, 9]), relay.reshape(var_15781.astype('float32'), [13, 10, 11]), ), 1)
call_15783 = relay.TupleGetItem(func_2659_call(relay.reshape(var_15780.astype('float64'), [140,]), relay.reshape(var_15781.astype('float32'), [13, 10, 11]), relay.reshape(var_15782.astype('bool'), [35, 9]), relay.reshape(var_15781.astype('float32'), [13, 10, 11]), ), 1)
func_14113_call = mod.get_global_var('func_14113')
func_14114_call = mutated_mod.get_global_var('func_14114')
call_15784 = relay.TupleGetItem(func_14113_call(), 0)
call_15785 = relay.TupleGetItem(func_14114_call(), 0)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_15789 = relay.TupleGetItem(func_3268_call(), 0)
call_15790 = relay.TupleGetItem(func_3269_call(), 0)
output = relay.Tuple([call_15752,call_15754,call_15776,const_15777,call_15779,var_15780,var_15781,var_15782,call_15784,call_15789,])
output2 = relay.Tuple([call_15753,call_15755,call_15778,const_15777,call_15783,var_15780,var_15781,var_15782,call_15785,call_15790,])
func_15795 = relay.Function([var_15780,var_15781,var_15782,], output)
mod['func_15795'] = func_15795
mod = relay.transform.InferType()(mod)
mutated_mod['func_15795'] = func_15795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15795_call = mutated_mod.get_global_var('func_15795')
var_15797 = relay.var("var_15797", dtype = "float64", shape = (140,))#candidate|15797|(140,)|var|float64
var_15798 = relay.var("var_15798", dtype = "float32", shape = (1430, 1))#candidate|15798|(1430, 1)|var|float32
var_15799 = relay.var("var_15799", dtype = "bool", shape = (315,))#candidate|15799|(315,)|var|bool
call_15796 = func_15795_call(var_15797,var_15798,var_15799,)
output = call_15796
func_15800 = relay.Function([var_15797,var_15798,var_15799,], output)
mutated_mod['func_15800'] = func_15800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9883_call = mod.get_global_var('func_9883')
func_9885_call = mutated_mod.get_global_var('func_9885')
call_15827 = func_9883_call()
call_15828 = func_9883_call()
func_12645_call = mod.get_global_var('func_12645')
func_12647_call = mutated_mod.get_global_var('func_12647')
call_15841 = relay.TupleGetItem(func_12645_call(), 0)
call_15842 = relay.TupleGetItem(func_12647_call(), 0)
output = relay.Tuple([call_15827,call_15841,])
output2 = relay.Tuple([call_15828,call_15842,])
func_15859 = relay.Function([], output)
mod['func_15859'] = func_15859
mod = relay.transform.InferType()(mod)
output = func_15859()
func_15860 = relay.Function([], output)
mutated_mod['func_15860'] = func_15860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3860_call = mod.get_global_var('func_3860')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_15878 = relay.TupleGetItem(func_3860_call(), 1)
call_15879 = relay.TupleGetItem(func_3861_call(), 1)
output = call_15878
output2 = call_15879
func_15918 = relay.Function([], output)
mod['func_15918'] = func_15918
mod = relay.transform.InferType()(mod)
mutated_mod['func_15918'] = func_15918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15918_call = mutated_mod.get_global_var('func_15918')
call_15919 = func_15918_call()
output = call_15919
func_15920 = relay.Function([], output)
mutated_mod['func_15920'] = func_15920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15037_call = mod.get_global_var('func_15037')
func_15039_call = mutated_mod.get_global_var('func_15039')
call_15941 = relay.TupleGetItem(func_15037_call(), 2)
call_15942 = relay.TupleGetItem(func_15039_call(), 2)
output = relay.Tuple([call_15941,])
output2 = relay.Tuple([call_15942,])
func_15981 = relay.Function([], output)
mod['func_15981'] = func_15981
mod = relay.transform.InferType()(mod)
output = func_15981()
func_15982 = relay.Function([], output)
mutated_mod['func_15982'] = func_15982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14033_call = mod.get_global_var('func_14033')
func_14034_call = mutated_mod.get_global_var('func_14034')
call_16016 = relay.TupleGetItem(func_14033_call(), 3)
call_16017 = relay.TupleGetItem(func_14034_call(), 3)
func_5830_call = mod.get_global_var('func_5830')
func_5832_call = mutated_mod.get_global_var('func_5832')
call_16018 = relay.TupleGetItem(func_5830_call(), 0)
call_16019 = relay.TupleGetItem(func_5832_call(), 0)
output = relay.Tuple([call_16016,call_16018,])
output2 = relay.Tuple([call_16017,call_16019,])
func_16020 = relay.Function([], output)
mod['func_16020'] = func_16020
mod = relay.transform.InferType()(mod)
mutated_mod['func_16020'] = func_16020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16020_call = mutated_mod.get_global_var('func_16020')
call_16021 = func_16020_call()
output = call_16021
func_16022 = relay.Function([], output)
mutated_mod['func_16022'] = func_16022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5414_call = mod.get_global_var('func_5414')
func_5416_call = mutated_mod.get_global_var('func_5416')
call_16038 = func_5414_call()
call_16039 = func_5414_call()
func_9285_call = mod.get_global_var('func_9285')
func_9287_call = mutated_mod.get_global_var('func_9287')
const_16044 = relay.const([0.535697,7.563778,-1.705791,-4.769102,-1.323045,-9.026758,0.179165,-6.444765,5.894615,-8.161642,5.401812,-4.714079,1.789501,0.018174,4.048276,-4.543173,-2.353383,8.034872,2.437748,-1.221264,4.227793,6.434330,4.634483,-6.285331,-4.328287,-7.208062,0.757011,-9.398665,-3.269538,9.269024,-6.222911,-1.312974,6.461139,6.170671,-9.228649,1.137166,-5.306933,-6.416486,-2.828048,-6.248772], dtype = "float64")#candidate|16044|(40,)|const|float64
call_16043 = relay.TupleGetItem(func_9285_call(relay.reshape(const_16044.astype('float64'), [40,])), 0)
call_16045 = relay.TupleGetItem(func_9287_call(relay.reshape(const_16044.astype('float64'), [40,])), 0)
func_8371_call = mod.get_global_var('func_8371')
func_8373_call = mutated_mod.get_global_var('func_8373')
const_16061 = relay.const([3.768901,-8.658400,-0.297286,-9.191457,-4.887584,-0.847428,1.350284,4.541838,9.127599,-1.691264,0.926714,9.635222,3.114554,-7.673667,-9.345273,-6.974792,3.306062,-9.142890,-1.992232,6.817366,4.006246,-7.198673,6.708959,-7.263361,5.908507,6.249756,-6.743267,2.669500,-6.666856,-4.361145,0.162564,2.577173,3.599527,7.311324,-9.420380,8.443616,-0.038411,-3.865975,8.760783,4.297805,-0.835484,-9.100657,7.955630,-5.463629,2.791343,-8.287081,6.965956,4.680081,-8.610900,-0.953868,4.744441,-2.441620,-5.079913,1.114979,2.093447,-9.998055,-1.895311,4.788998,-6.246610,0.844476,-7.736235,8.880898,9.434827,4.225405,0.201606,7.526671,0.404525,-2.799898,-1.747117,0.020100], dtype = "float32")#candidate|16061|(70,)|const|float32
call_16060 = relay.TupleGetItem(func_8371_call(relay.reshape(const_16061.astype('float32'), [2, 5, 7])), 0)
call_16062 = relay.TupleGetItem(func_8373_call(relay.reshape(const_16061.astype('float32'), [2, 5, 7])), 0)
func_6611_call = mod.get_global_var('func_6611')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_16063 = relay.TupleGetItem(func_6611_call(), 0)
call_16064 = relay.TupleGetItem(func_6612_call(), 0)
output = relay.Tuple([call_16038,call_16043,const_16044,call_16060,const_16061,call_16063,])
output2 = relay.Tuple([call_16039,call_16045,const_16044,call_16062,const_16061,call_16064,])
func_16077 = relay.Function([], output)
mod['func_16077'] = func_16077
mod = relay.transform.InferType()(mod)
output = func_16077()
func_16078 = relay.Function([], output)
mutated_mod['func_16078'] = func_16078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9719_call = mod.get_global_var('func_9719')
func_9720_call = mutated_mod.get_global_var('func_9720')
call_16094 = func_9719_call()
call_16095 = func_9719_call()
func_11593_call = mod.get_global_var('func_11593')
func_11595_call = mutated_mod.get_global_var('func_11595')
call_16106 = relay.TupleGetItem(func_11593_call(), 1)
call_16107 = relay.TupleGetItem(func_11595_call(), 1)
func_589_call = mod.get_global_var('func_589')
func_591_call = mutated_mod.get_global_var('func_591')
const_16109 = relay.const([-4.516549,1.428469,-1.828483,6.587983,2.729560,-4.352175,-8.882314,-6.040241,-4.608036,5.717353,2.998494,-6.414747,2.127726,3.807522,6.777610,-4.703231,6.092645,-8.877015,-3.517291,1.783654,6.720057,9.456483,-8.127196,5.241238,8.044952,7.179497,8.456156,-9.318301,-5.985362,-9.824534,-4.376477,7.638925,-7.298059,5.796491,4.846710,-3.768569,4.399680,-9.625297,8.296514,-3.777114,1.138916,-8.955972,8.776891,1.079088,-3.042943,-6.055827,-3.765679,9.524863,8.099392,-1.048874,3.212425,9.764403,-1.371532,-6.552833,-5.522724,4.530287,6.536953,-8.804342,-4.515416,-9.025283,5.267155,3.686631,-5.994345,6.220366,-1.510228,-3.700462,-4.647220,-5.053959,9.254030,8.102935,9.640122,9.900635,-0.941630,1.094395,8.638884,6.802007,-2.217226,8.585061,3.981201,-5.535156,-2.508937,-6.605347,8.238923,2.598841,8.755209,-0.449482,4.721516,7.621330,5.741322,7.945157,-0.497758,-3.399396,5.602197,9.035227,-3.053084,-7.246789,-6.479922,2.002822,8.046149,9.178546,5.862760,6.476788,4.163618,-9.583072,-0.907355,-3.798206,3.377530,9.717446,-2.999823,3.710696,6.066338,7.723474,-6.622316,7.260473,2.996589,7.901255,-8.405553,-7.472708,9.195893,-9.432265,-7.212157,9.424812,8.908161,-4.086943,7.595116,-3.623794,-0.685270,3.196138,8.110972,-1.132771,4.351898,8.142972,9.000608,3.051318,7.718184,-0.961350,-4.243503,1.349519,-3.758787,9.049655,1.797724,-0.293037,8.821813,5.136171,-4.805876,-0.674681,7.654914,5.452747,8.351689,4.761700,0.418002,-6.502467,3.167574,4.119424,3.943406,-2.981126,9.343337,-2.539845,-0.233757,0.382534,-4.264522,-7.651062,7.814500,-3.241409,-1.267286,1.921869,3.402632,-4.868345,2.725950,-8.951448,-7.503982,-8.434331,-6.715657,0.876560,-4.538010,0.412723,-2.808276,-5.186856,-0.321791,-1.056479,-2.525890,-4.157298,1.797045,6.108649,-0.281320,8.517840,-0.935623,-0.075606,0.514096,1.730157,-7.775401,-1.579073,-0.766055,2.814955,0.678769,1.004225,8.530902,5.077022,-3.536765,-5.032469,-7.430302,-7.305836,3.198855,7.420710,-8.975766,-8.672000,-9.862005,6.415792,7.499699,6.437608,-8.810737,-1.958342,-3.260209,-5.913674,-0.278615,5.472971,-3.750764,8.162452,2.169231,-2.603202,3.088666,-7.503816,8.816545,-8.762852,-0.745499,0.602345,1.351591,6.613271,4.794487,-3.095143,-2.430427,4.932954,3.234393,-9.882347,7.201260,-4.746832,1.312931,-8.614221,-8.548251,7.455014,-2.572859,4.486321,-0.140891,2.466768,-2.965252,-3.829620,-8.051793,-8.271713,-4.934989,-5.518054,5.814469,9.375823,1.684605,-3.969361,-8.905029,2.682247,-0.406495,-1.663106,6.605658,8.825720,-5.205781,-8.594236,4.371935,-9.639799,8.472635,9.573747,-0.682835,3.026932,6.209407,7.194321,5.307355,-2.786984,-9.525543,-8.671622,7.024392,5.555891,0.028769,-3.732749,-9.966229,6.187960,2.389708,6.972425,0.712933,4.563437,-5.886662,-8.985446,6.388943,8.263778,-8.343269,4.926813,0.404650,8.491041,-6.304981,3.333143,-6.243410,-7.352822,-4.593469,9.442234,-3.364499,-5.646480,-7.925839,-9.301000,4.816233,2.600022,-5.805573,4.665335,9.320449,-5.360844,-8.971015,1.982082,-2.417219,-6.590392,8.965219,-7.122774,3.613025,-6.269636,-0.557112,3.251303,-9.489902,4.681032,-7.739677,6.277391,6.903036,2.193555,9.945276,-4.280979,0.524884,-9.877442,2.895983,-8.053268,7.606985,-1.981786,-1.792577,-7.381216,-9.483514,7.737446,-2.832946,-8.336383,-7.619258,-6.619460,-5.854952,-3.947371,5.109531,-1.638143,9.868388,7.776616,3.073692,-6.562601,-2.466774,6.012330,-5.611287,5.889567,5.652920,-5.637949,8.408619,8.173730,-9.380804,0.186338,4.370405,-4.663836,6.235950,0.677339,6.670429,-5.244122,-8.854523,-9.061313,-9.107178,-7.816687,1.857737,5.278864,1.010915,8.918929,-0.073479,5.922677,-3.587081,7.971453,-3.181674,0.233821,-7.726852,1.715459,8.892860,-2.580530,1.903120,5.852463,0.745875,0.677457,0.420934,-3.031849,-4.121997,9.077223,9.684826,-5.817540,-3.325899,2.006576,0.245944,5.407293,-6.000014,-8.339913,-2.425929,2.033273,-1.320885,-5.187008,6.427095,-5.939354,2.335895,-5.381703,-9.019834,-8.462533,-5.384958,1.517621,-6.122021,-6.820698,-7.545945,-6.548304,-2.154959,7.868019,-0.574221,2.808840,-5.817215,8.932532,7.033678,5.711477,-7.073172,-0.114189,8.491203,-4.885215,1.546116,4.141529,4.920594,-6.626523,6.592247,3.685768,-6.414783,9.770942,-0.269428,-3.791869,-8.668942,7.335607,1.245126,-2.456096,1.076081,-0.502255,6.738615,9.026999,3.997376,8.175933,3.432275,-0.464417,8.020870,-3.729317,1.998222,8.101522,-5.287434,-0.895053,0.489332,7.348041,-9.744767,6.943761,3.955443,-6.561524,-1.086885,7.663396,-6.527597,3.878652,9.496931,6.370594,-2.093483,-3.299536,5.632840,-5.714353,8.417309,-2.527364,8.408221,-0.283961,-9.201579,6.789074,-4.895586,-1.518263,6.445149,-4.360259,8.650214,9.258802,-5.781093,2.339553,-4.081906,-4.843575,0.864763,4.334284,-9.791586,2.933385,0.314116,-1.473736,7.102877,-0.386684,-9.531509,0.621886,0.914309,-0.109083,-6.947512,0.145100,5.996447,1.600087,-7.998936,-6.189002,-5.549495,8.205538,-5.905402,0.171520,-4.024575,-0.486936,-4.532860,7.018736,-6.066953,2.916349,7.087752,-8.348823,7.001443,1.008549,-4.497472,-0.243478,3.715547,-0.555659,3.233483,4.345156,-9.659343,7.440579,9.511205,-5.610930,-2.419509,-5.387748,-8.611164,-5.497469,-0.686448,-0.580949,8.385511,5.692441,-1.856582,8.119612,0.968240,-7.591905,-9.655466,-5.265461,-2.343157,-5.931301,5.248749,-8.191756,8.946985,7.060743,-1.647528,-1.360249,-0.036512,-1.211186,-1.287923,1.009770,-4.092709,7.052150,1.844108,-6.511182,-2.574980,-7.271417,3.323360,0.373316,8.140113,3.696233,-3.856515,-5.287591,7.462021,-7.101431,-8.807671,-3.342551,4.383084,9.883742,1.072331,-2.511799,-7.455589,9.786816,1.381829,-4.005970,5.101362,-2.258016,-1.103766,2.139325,5.851684,1.578391,7.406824,-3.541845,9.704274,1.183482,4.511023,-5.535116,-7.739259,0.270336,-1.441389,-9.554515,5.266190,-0.293416,5.486293,-2.087076,3.531152,-2.184570,1.918167,7.713564,4.139756,8.148897,-6.260198,-4.926004,-0.901871,-1.350265,-7.399231,-1.536925,3.262028,9.502792,-6.164130,4.175243,9.183735,-3.839301,-0.965640,4.695034,-2.900718,-5.537615,-1.518224,9.658989,-4.706537,5.617825,6.906123,0.937348,-9.158213,6.350299,-7.618313,-6.750421,7.748740,-1.051028,-0.541600,8.707168,-1.932650,5.429778,-1.419385,5.393194,-8.350595,4.796660,9.602575,-5.844450,0.053609,-3.510015,-8.781872,7.602913,-0.129678,3.897919,0.507103,3.373886,-6.314054,-0.102832,-6.474922,-7.458915,4.082124,-0.355568,-5.105589,-6.664703,-9.085652,6.248103,-2.625890,-4.895333,-2.750300,4.615972,-1.079728,9.373121,-9.820043,-6.323985,-2.238887,2.743310,-7.275382,-9.129571,0.272457,6.225714,5.458288,-1.965713,7.736976,-2.160775,4.573855,-2.892768,8.641043,-4.046293,3.923024,-7.134555,4.680522,1.307769,6.549998,-0.732004,7.348680,-4.636609,-5.003674,-7.441744,-1.921923,8.518879,-6.413135,8.069659,-5.612076,0.595823,-8.466436,6.931103,-6.457930,-8.619242,-3.556364,-4.769778,-8.455422,-3.253726,5.397570,-8.255491,-4.046094,3.333737,9.083317,-8.087587,6.228407,-4.911928,9.636151,9.074560,-3.108567,7.873004,3.219608,-1.365149,-0.590555,-9.557927,5.583679,4.285345,4.115998,1.666462,-2.421462,-2.127983,7.652298,9.054570,-9.602915,-3.634054,-5.874490,7.442207,5.489663,0.653331,-6.708681,-6.794191,9.227577,9.863918,-5.910498,5.088763,-5.015514,-2.918159,-6.848038,-2.761672,9.020489,-2.674616,-4.521587,0.004459,8.210619,-7.799504,-9.111933,-2.365325,-7.688458,-9.300236,-8.988824,9.555488,0.504122,-2.618790,-1.142125,-9.893679,-3.168927,4.587015,-6.462955,-5.153820,-2.240008,-5.762954,3.091219,-9.597262,-2.155415,3.555516,-3.325317,-9.431422,-7.754311,-5.465280,6.346023,-4.845849,1.668083,5.070752], dtype = "float64")#candidate|16109|(780,)|const|float64
call_16108 = func_589_call(relay.reshape(const_16109.astype('float64'), [13, 15, 4]))
call_16110 = func_589_call(relay.reshape(const_16109.astype('float64'), [13, 15, 4]))
func_4242_call = mod.get_global_var('func_4242')
func_4246_call = mutated_mod.get_global_var('func_4246')
var_16116 = relay.var("var_16116", dtype = "float32", shape = (660,))#candidate|16116|(660,)|var|float32
call_16115 = relay.TupleGetItem(func_4242_call(relay.reshape(call_16108.astype('float64'), [780,]), relay.reshape(var_16116.astype('float32'), [660,]), ), 2)
call_16117 = relay.TupleGetItem(func_4246_call(relay.reshape(call_16108.astype('float64'), [780,]), relay.reshape(var_16116.astype('float32'), [660,]), ), 2)
output = relay.Tuple([call_16094,call_16106,call_16108,const_16109,call_16115,var_16116,])
output2 = relay.Tuple([call_16095,call_16107,call_16110,const_16109,call_16117,var_16116,])
func_16119 = relay.Function([var_16116,], output)
mod['func_16119'] = func_16119
mod = relay.transform.InferType()(mod)
mutated_mod['func_16119'] = func_16119
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16120 = relay.var("var_16120", dtype = "float32", shape = (660,))#candidate|16120|(660,)|var|float32
func_16119_call = mutated_mod.get_global_var('func_16119')
call_16121 = func_16119_call(var_16120)
output = call_16121
func_16122 = relay.Function([var_16120], output)
mutated_mod['func_16122'] = func_16122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6030_call = mod.get_global_var('func_6030')
func_6032_call = mutated_mod.get_global_var('func_6032')
call_16163 = relay.TupleGetItem(func_6030_call(), 0)
call_16164 = relay.TupleGetItem(func_6032_call(), 0)
output = relay.Tuple([call_16163,])
output2 = relay.Tuple([call_16164,])
func_16165 = relay.Function([], output)
mod['func_16165'] = func_16165
mod = relay.transform.InferType()(mod)
mutated_mod['func_16165'] = func_16165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16165_call = mutated_mod.get_global_var('func_16165')
call_16166 = func_16165_call()
output = call_16166
func_16167 = relay.Function([], output)
mutated_mod['func_16167'] = func_16167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4275_call = mod.get_global_var('func_4275')
func_4277_call = mutated_mod.get_global_var('func_4277')
call_16176 = relay.TupleGetItem(func_4275_call(), 0)
call_16177 = relay.TupleGetItem(func_4277_call(), 0)
func_11309_call = mod.get_global_var('func_11309')
func_11311_call = mutated_mod.get_global_var('func_11311')
var_16181 = relay.var("var_16181", dtype = "float64", shape = (780,))#candidate|16181|(780,)|var|float64
call_16180 = relay.TupleGetItem(func_11309_call(relay.reshape(var_16181.astype('float64'), [780,])), 3)
call_16182 = relay.TupleGetItem(func_11311_call(relay.reshape(var_16181.astype('float64'), [780,])), 3)
output = relay.Tuple([call_16176,call_16180,var_16181,])
output2 = relay.Tuple([call_16177,call_16182,var_16181,])
func_16188 = relay.Function([var_16181,], output)
mod['func_16188'] = func_16188
mod = relay.transform.InferType()(mod)
mutated_mod['func_16188'] = func_16188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16189 = relay.var("var_16189", dtype = "float64", shape = (780,))#candidate|16189|(780,)|var|float64
func_16188_call = mutated_mod.get_global_var('func_16188')
call_16190 = func_16188_call(var_16189)
output = call_16190
func_16191 = relay.Function([var_16189], output)
mutated_mod['func_16191'] = func_16191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3086_call = mod.get_global_var('func_3086')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_16290 = relay.TupleGetItem(func_3086_call(), 1)
call_16291 = relay.TupleGetItem(func_3087_call(), 1)
func_8042_call = mod.get_global_var('func_8042')
func_8043_call = mutated_mod.get_global_var('func_8043')
call_16312 = relay.TupleGetItem(func_8042_call(), 1)
call_16313 = relay.TupleGetItem(func_8043_call(), 1)
output = relay.Tuple([call_16290,call_16312,])
output2 = relay.Tuple([call_16291,call_16313,])
func_16324 = relay.Function([], output)
mod['func_16324'] = func_16324
mod = relay.transform.InferType()(mod)
mutated_mod['func_16324'] = func_16324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16324_call = mutated_mod.get_global_var('func_16324')
call_16325 = func_16324_call()
output = call_16325
func_16326 = relay.Function([], output)
mutated_mod['func_16326'] = func_16326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10774_call = mod.get_global_var('func_10774')
func_10775_call = mutated_mod.get_global_var('func_10775')
call_16330 = relay.TupleGetItem(func_10774_call(), 1)
call_16331 = relay.TupleGetItem(func_10775_call(), 1)
output = relay.Tuple([call_16330,])
output2 = relay.Tuple([call_16331,])
func_16341 = relay.Function([], output)
mod['func_16341'] = func_16341
mod = relay.transform.InferType()(mod)
output = func_16341()
func_16342 = relay.Function([], output)
mutated_mod['func_16342'] = func_16342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6115_call = mod.get_global_var('func_6115')
func_6116_call = mutated_mod.get_global_var('func_6116')
call_16404 = relay.TupleGetItem(func_6115_call(), 0)
call_16405 = relay.TupleGetItem(func_6116_call(), 0)
func_1222_call = mod.get_global_var('func_1222')
func_1225_call = mutated_mod.get_global_var('func_1225')
var_16412 = relay.var("var_16412", dtype = "float64", shape = (780,))#candidate|16412|(780,)|var|float64
call_16411 = relay.TupleGetItem(func_1222_call(relay.reshape(var_16412.astype('float64'), [780,])), 0)
call_16413 = relay.TupleGetItem(func_1225_call(relay.reshape(var_16412.astype('float64'), [780,])), 0)
func_14569_call = mod.get_global_var('func_14569')
func_14570_call = mutated_mod.get_global_var('func_14570')
call_16431 = func_14569_call()
call_16432 = func_14569_call()
func_4144_call = mod.get_global_var('func_4144')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_16446 = func_4144_call()
call_16447 = func_4144_call()
output = relay.Tuple([call_16404,call_16411,var_16412,call_16431,call_16446,])
output2 = relay.Tuple([call_16405,call_16413,var_16412,call_16432,call_16447,])
func_16448 = relay.Function([var_16412,], output)
mod['func_16448'] = func_16448
mod = relay.transform.InferType()(mod)
var_16449 = relay.var("var_16449", dtype = "float64", shape = (780,))#candidate|16449|(780,)|var|float64
output = func_16448(var_16449)
func_16450 = relay.Function([var_16449], output)
mutated_mod['func_16450'] = func_16450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_16490 = relay.TupleGetItem(func_4982_call(), 0)
call_16491 = relay.TupleGetItem(func_4983_call(), 0)
output = relay.Tuple([call_16490,])
output2 = relay.Tuple([call_16491,])
func_16532 = relay.Function([], output)
mod['func_16532'] = func_16532
mod = relay.transform.InferType()(mod)
output = func_16532()
func_16533 = relay.Function([], output)
mutated_mod['func_16533'] = func_16533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5751_call = mod.get_global_var('func_5751')
func_5753_call = mutated_mod.get_global_var('func_5753')
call_16577 = relay.TupleGetItem(func_5751_call(), 0)
call_16578 = relay.TupleGetItem(func_5753_call(), 0)
output = relay.Tuple([call_16577,])
output2 = relay.Tuple([call_16578,])
func_16592 = relay.Function([], output)
mod['func_16592'] = func_16592
mod = relay.transform.InferType()(mod)
output = func_16592()
func_16593 = relay.Function([], output)
mutated_mod['func_16593'] = func_16593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15637_call = mod.get_global_var('func_15637')
func_15638_call = mutated_mod.get_global_var('func_15638')
call_16646 = relay.TupleGetItem(func_15637_call(), 1)
call_16647 = relay.TupleGetItem(func_15638_call(), 1)
func_12856_call = mod.get_global_var('func_12856')
func_12857_call = mutated_mod.get_global_var('func_12857')
call_16654 = func_12856_call()
call_16655 = func_12856_call()
output = relay.Tuple([call_16646,call_16654,])
output2 = relay.Tuple([call_16647,call_16655,])
func_16659 = relay.Function([], output)
mod['func_16659'] = func_16659
mod = relay.transform.InferType()(mod)
output = func_16659()
func_16660 = relay.Function([], output)
mutated_mod['func_16660'] = func_16660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14508_call = mod.get_global_var('func_14508')
func_14509_call = mutated_mod.get_global_var('func_14509')
call_16663 = func_14508_call()
call_16664 = func_14508_call()
func_3218_call = mod.get_global_var('func_3218')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_16686 = relay.TupleGetItem(func_3218_call(), 0)
call_16687 = relay.TupleGetItem(func_3219_call(), 0)
output = relay.Tuple([call_16663,call_16686,])
output2 = relay.Tuple([call_16664,call_16687,])
func_16702 = relay.Function([], output)
mod['func_16702'] = func_16702
mod = relay.transform.InferType()(mod)
output = func_16702()
func_16703 = relay.Function([], output)
mutated_mod['func_16703'] = func_16703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16324_call = mod.get_global_var('func_16324')
func_16326_call = mutated_mod.get_global_var('func_16326')
call_16725 = relay.TupleGetItem(func_16324_call(), 0)
call_16726 = relay.TupleGetItem(func_16326_call(), 0)
uop_16729 = relay.tan(call_16725.astype('float32')) # shape=(5, 10, 11)
uop_16731 = relay.tan(call_16726.astype('float32')) # shape=(5, 10, 11)
output = relay.Tuple([uop_16729,])
output2 = relay.Tuple([uop_16731,])
func_16734 = relay.Function([], output)
mod['func_16734'] = func_16734
mod = relay.transform.InferType()(mod)
output = func_16734()
func_16735 = relay.Function([], output)
mutated_mod['func_16735'] = func_16735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5751_call = mod.get_global_var('func_5751')
func_5753_call = mutated_mod.get_global_var('func_5753')
call_16754 = relay.TupleGetItem(func_5751_call(), 0)
call_16755 = relay.TupleGetItem(func_5753_call(), 0)
func_613_call = mod.get_global_var('func_613')
func_616_call = mutated_mod.get_global_var('func_616')
const_16759 = relay.const([[2.246308,2.797267,-9.677190,6.707950,-6.827299,1.742629,1.944421,-0.101437,-1.451564,-1.177103,-1.907635,6.161239,8.029187,3.040209,0.768887,7.513953,2.968688,6.894479,2.251010,4.097600,1.343722,3.118581,-3.478387,-3.426531,4.579591,-7.095808,-1.724946,0.451011,-9.637726,8.593725,0.449099,-2.105763,3.821842,0.060696,-2.359383,-2.998419,5.094145,0.203313,-9.442500,-5.746451,-7.829679,5.006592,-7.779875,-0.016874,3.724528,-5.220184,3.675215,-2.270425,-1.053836,2.081068,-9.454812,-6.483226,0.137758,-1.690098,9.855370,9.205182,5.469069,-1.378211,3.795767,5.524815,-8.608752,-4.349316,-1.054287,-2.676438,-3.344851,-2.091290,-6.846096,-3.931222,-1.846357,7.697638,7.793535,3.006853,5.444920,-0.785562,7.229780,-3.425673,9.908653,6.043222,4.758081,-2.941601,8.779586,-0.952171,4.193173,6.820250,2.034701,3.030935,0.263358,-7.947198,6.072424,-3.464436,-7.033010,-0.003239,5.121087,7.983729,-2.406890,-1.408089,-4.505523,7.644708,2.813731,4.668209,8.598702,3.776569,-4.114411,6.273043,-6.893760,-4.961770,-1.507301,-4.168370,-5.145590,-8.007266,2.680017,-9.594843,-1.254004,3.053918,-6.618028,-7.109205,6.975653,-9.064875,9.883472,6.251717,2.805405,-3.839444,6.652764,1.894633,1.415065,-2.725812,-0.579685,-8.207288,-0.105131,-9.161548,6.195284,-8.838101,-6.165002,-0.490580,-6.680144,4.447697,3.401921,-8.026040,-6.180328,-7.744532,0.061726,-1.875268,3.330089,-8.571343]], dtype = "float64")#candidate|16759|(1, 144)|const|float64
call_16758 = relay.TupleGetItem(func_613_call(relay.reshape(const_16759.astype('float64'), [16, 3, 3])), 0)
call_16760 = relay.TupleGetItem(func_616_call(relay.reshape(const_16759.astype('float64'), [16, 3, 3])), 0)
uop_16788 = relay.asin(call_16758.astype('float64')) # shape=(16, 3, 3)
uop_16790 = relay.asin(call_16760.astype('float64')) # shape=(16, 3, 3)
const_16792 = relay.const([[[-9.521561,-7.999303,9.172590],[6.010064,-0.966445,-1.940691],[-4.863024,-9.601136,-4.663287]],[[0.988725,2.652365,0.010386],[-2.608107,2.999853,-3.757956],[-4.853911,-8.617538,-0.884852]],[[9.069201,9.200143,1.374872],[4.368220,4.255910,4.449164],[-5.755202,-3.780522,-5.998212]],[[1.601141,-9.678861,1.784213],[4.280019,2.903415,-3.647814],[3.382665,5.182410,4.663720]],[[9.177471,6.348520,-0.330523],[-4.048546,6.241406,-1.432472],[-2.567965,-3.970216,2.332182]],[[-0.502856,2.712339,-5.704332],[7.038021,-8.637966,1.070796],[8.044195,-8.281698,7.028124]],[[-7.559443,1.604349,4.788497],[9.434374,-0.316947,-8.077481],[5.856545,-3.837059,-2.769831]],[[8.875841,7.196525,-6.837539],[8.032750,4.956219,-2.238324],[7.251335,-8.596243,7.368641]],[[-0.911656,3.995930,-6.308190],[-0.716943,-9.723333,1.137251],[-6.557477,-0.988803,-2.698665]],[[-0.312317,9.577606,3.772095],[-4.431127,-5.451525,4.950125],[-6.186032,-7.457793,-7.505391]],[[7.766789,-3.638384,-7.164729],[-6.864724,-6.677536,-1.801293],[-9.296575,4.489077,-3.431994]],[[2.589350,7.061825,9.776592],[9.934865,-9.797027,4.313079],[4.791165,-3.373673,1.223203]],[[8.857632,1.802192,-6.375098],[-3.905302,-6.365306,-9.287894],[-6.542200,3.171422,6.411630]],[[-2.718474,9.650745,-6.790542],[-0.067656,0.439576,-6.856926],[2.941542,7.265771,8.154858]],[[-7.067097,-6.791521,3.148625],[1.018921,-3.735956,5.709770],[8.734143,3.898052,8.816720]],[[8.050171,9.228544,-5.331657],[4.506761,9.384480,-4.954747],[9.596846,-9.012762,5.643420]]], dtype = "float64")#candidate|16792|(16, 3, 3)|const|float64
bop_16793 = relay.left_shift(uop_16788.astype('int64'), relay.reshape(const_16792.astype('int64'), relay.shape_of(uop_16788))) # shape=(16, 3, 3)
bop_16796 = relay.left_shift(uop_16790.astype('int64'), relay.reshape(const_16792.astype('int64'), relay.shape_of(uop_16790))) # shape=(16, 3, 3)
func_8285_call = mod.get_global_var('func_8285')
func_8288_call = mutated_mod.get_global_var('func_8288')
const_16817 = relay.const([-2,-5,-4,4,-7,7,-8,9,4,-10,-1,-1,2,6,-2,-2,-2,5,-4,-3,-8,6,1,-2,7,1,8,2,-2,6,3,-10,4,10,4,7,-6,-8,8,-1,1,-6,-1,-7,-5,9,-8,5,-6,-10,-10,10,1,10,-7,8,-10,7,1,8,-6,7,8,7,-7,-4,-5,-3,-4,8,6,9,10,-1,9,-8,6,10,7,10,4,3,8,-8,2,6,-1,4,-3,4,-4,-7,-8,-8,4,-1,2,10,3,-2,3,3,-5,7,3,9,6,10,3,-10,-4,7,-6,-5,4,-6,-7,3,7,9,-3,-7,-4,-4,-3,-6,-5,2,-2,2,8,7,6,-9,-1,-3,7,-5,5,10,2,-4,2,10,-6,-2,-10,-10,-8,-9,9,5,-2,-9,-10,4,6,10,-5,-2,3,-5,-4,9,-6,-2,10,1,8,8,8,1,-1,1,-1,7,8,5,7,-3,4,-9,1,-6,-1,-8,-8,2,9,-5,6,-4,-6,-6,5,-7,3,3,8,-4,6,10,10,-5,-7,1,6,10,4,-4,-3,8,-9,-9,-10,7,-4,4,-1,5,3,1,-9,9,7,2,8,-6,-1,-7,-10,9,-1,10,-3,-10,-10,4,-4,-3,-10,-10,7,7,-3,-8,-9,8,3,-4,2,-3,-4,2,-3,8,-1,4,-4,-5,7,9,4,8,5,4,-5,-10,5,9,-8,-3,-5,7,10,-6,7,3,-3,9,-4,-7,-1,9,10,5,-7,7,5,-9,7,-2,-1,8,-7,-3,-3,1,1,1,10,-1,4,8,3,-4,3,7,-2,-9,5,9,6,1,10,9,5,6,8,-9,-1,1,1,-9,4,-2,-2,6,-9,-5,8,10,4,5,9,-2,10,-6,5,4,3,-10,-4,-1,5,3,-10,9,10,7,-9,-2,6,10,3,-3,-9,-9,1,-10,-8,10,-6,3,4,-5,-10,-3,-7,8,-8,-6,1,-2,9,-9,-4,6,-7,-6,-8,-3,2,-5,-9,-8,-1,4,10,-6,-7,-6,3,3,-3,-10,-1,-9,9,1,6,-4,4,1,-5,4,10,-5,4,-3,-6,-7,-6,-2,-2,-4,4,5,8,-3,3,-7,9,-5,1,-1,-3,-5,-7,-3,-10,7,-4,2,-8,-7,4,3,-9,8,8,-4,-10,-9,6,7,-10,-1,-7,-8,-10,8,-10,-7,3,8,9,-4,1,-7,7,4,-8,-2,8,2,7,-1,-4,6,6,-1,-6,-5,8,5,-5,3,-3,-10,6,-8,3,2,6,7,3,-8,-2,-7,4,-8,-10,2,-9,-4,-4,10,10,9,1,1,-5,-3,1,-1,-2,5,1,7,2,7,-6,7,10,-3,1,2,-4,-5,5,-1,5,10,5,-6,-1,-5,1,-2,-8,-1,-10,5,8,-8,-5,3,-6,6], dtype = "int32")#candidate|16817|(540,)|const|int32
call_16816 = relay.TupleGetItem(func_8285_call(relay.reshape(const_16817.astype('int32'), [540,])), 0)
call_16818 = relay.TupleGetItem(func_8288_call(relay.reshape(const_16817.astype('int32'), [540,])), 0)
uop_16825 = relay.cosh(bop_16793.astype('float32')) # shape=(16, 3, 3)
uop_16827 = relay.cosh(bop_16796.astype('float32')) # shape=(16, 3, 3)
output = relay.Tuple([call_16754,const_16759,call_16816,const_16817,uop_16825,])
output2 = relay.Tuple([call_16755,const_16759,call_16818,const_16817,uop_16827,])
func_16828 = relay.Function([], output)
mod['func_16828'] = func_16828
mod = relay.transform.InferType()(mod)
mutated_mod['func_16828'] = func_16828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16828_call = mutated_mod.get_global_var('func_16828')
call_16829 = func_16828_call()
output = call_16829
func_16830 = relay.Function([], output)
mutated_mod['func_16830'] = func_16830
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16861 = relay.var("var_16861", dtype = "bool", shape = ())#candidate|16861|()|var|bool
var_16862 = relay.var("var_16862", dtype = "bool", shape = (4, 1, 6))#candidate|16862|(4, 1, 6)|var|bool
bop_16863 = relay.logical_or(var_16861.astype('bool'), var_16862.astype('bool')) # shape=(4, 1, 6)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_16884 = relay.TupleGetItem(func_3161_call(), 0)
call_16885 = relay.TupleGetItem(func_3162_call(), 0)
output = relay.Tuple([bop_16863,call_16884,])
output2 = relay.Tuple([bop_16863,call_16885,])
func_16887 = relay.Function([var_16861,var_16862,], output)
mod['func_16887'] = func_16887
mod = relay.transform.InferType()(mod)
mutated_mod['func_16887'] = func_16887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16887_call = mutated_mod.get_global_var('func_16887')
var_16889 = relay.var("var_16889", dtype = "bool", shape = ())#candidate|16889|()|var|bool
var_16890 = relay.var("var_16890", dtype = "bool", shape = (4, 1, 6))#candidate|16890|(4, 1, 6)|var|bool
call_16888 = func_16887_call(var_16889,var_16890,)
output = call_16888
func_16891 = relay.Function([var_16889,var_16890,], output)
mutated_mod['func_16891'] = func_16891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6245_call = mod.get_global_var('func_6245')
func_6246_call = mutated_mod.get_global_var('func_6246')
call_16926 = relay.TupleGetItem(func_6245_call(), 0)
call_16927 = relay.TupleGetItem(func_6246_call(), 0)
func_13514_call = mod.get_global_var('func_13514')
func_13516_call = mutated_mod.get_global_var('func_13516')
call_16933 = relay.TupleGetItem(func_13514_call(), 0)
call_16934 = relay.TupleGetItem(func_13516_call(), 0)
func_4293_call = mod.get_global_var('func_4293')
func_4295_call = mutated_mod.get_global_var('func_4295')
call_16943 = relay.TupleGetItem(func_4293_call(), 1)
call_16944 = relay.TupleGetItem(func_4295_call(), 1)
output = relay.Tuple([call_16926,call_16933,call_16943,])
output2 = relay.Tuple([call_16927,call_16934,call_16944,])
func_16949 = relay.Function([], output)
mod['func_16949'] = func_16949
mod = relay.transform.InferType()(mod)
mutated_mod['func_16949'] = func_16949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16949_call = mutated_mod.get_global_var('func_16949')
call_16950 = func_16949_call()
output = call_16950
func_16951 = relay.Function([], output)
mutated_mod['func_16951'] = func_16951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15436_call = mod.get_global_var('func_15436')
func_15438_call = mutated_mod.get_global_var('func_15438')
call_16995 = relay.TupleGetItem(func_15436_call(), 0)
call_16996 = relay.TupleGetItem(func_15438_call(), 0)
output = call_16995
output2 = call_16996
func_17002 = relay.Function([], output)
mod['func_17002'] = func_17002
mod = relay.transform.InferType()(mod)
mutated_mod['func_17002'] = func_17002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17002_call = mutated_mod.get_global_var('func_17002')
call_17003 = func_17002_call()
output = call_17003
func_17004 = relay.Function([], output)
mutated_mod['func_17004'] = func_17004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9839_call = mod.get_global_var('func_9839')
func_9840_call = mutated_mod.get_global_var('func_9840')
call_17123 = relay.TupleGetItem(func_9839_call(), 2)
call_17124 = relay.TupleGetItem(func_9840_call(), 2)
func_9920_call = mod.get_global_var('func_9920')
func_9921_call = mutated_mod.get_global_var('func_9921')
call_17132 = func_9920_call()
call_17133 = func_9920_call()
uop_17135 = relay.sin(call_17123.astype('float32')) # shape=(12, 16, 16)
uop_17137 = relay.sin(call_17124.astype('float32')) # shape=(12, 16, 16)
output = relay.Tuple([call_17132,uop_17135,])
output2 = relay.Tuple([call_17133,uop_17137,])
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
