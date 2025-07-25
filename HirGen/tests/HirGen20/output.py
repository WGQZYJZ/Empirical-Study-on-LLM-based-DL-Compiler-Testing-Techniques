import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_164 = relay.const([[[6.692303,9.436132,0.655604,5.844608,-8.959166,-6.415136,-5.010132,7.426581,-7.263402,-6.873332,6.700993,-3.831147,0.427537,6.309351,3.819393,7.393493],[-2.653297,-9.501496,1.125886,6.362716,0.169767,-3.384062,-8.597083,-6.323221,-4.169801,-5.574365,2.020624,0.404636,0.720436,-0.285519,1.727836,0.857773],[-6.784375,9.970949,-8.498181,9.575915,7.321634,5.017244,-8.249498,-0.305623,-2.841567,-1.891336,9.265514,8.245703,-8.902785,1.410351,5.126238,-0.158632],[-0.815532,-1.954880,-2.282637,-7.974242,6.522068,1.130716,-9.671644,-7.983059,-6.241490,-0.438931,0.256719,-2.576487,-7.172221,3.792037,5.377118,5.041110],[-7.563054,-7.780702,-9.219051,-2.180670,-5.987345,3.731463,9.190866,-7.308711,-2.164397,6.550122,-4.738512,-2.303108,-6.694617,-1.762112,4.406639,6.575941],[2.049262,-6.216891,4.946315,-5.626053,-4.227987,-2.583011,9.196863,-5.005400,7.501581,3.648368,0.391071,-4.614065,-4.895659,8.140734,7.188850,5.268057]],[[-4.361646,-4.026013,-0.703424,-2.502168,-3.695249,-0.988611,6.129944,8.244403,-8.942538,-3.878128,-4.214210,6.930536,7.161616,-0.329471,-8.505170,-1.787955],[2.181439,-6.010417,0.469739,2.410472,9.711722,2.431665,-7.874009,8.602449,-1.186645,-6.860563,7.718226,9.992161,6.641592,3.023586,8.159207,-2.194676],[-5.517044,-2.602718,6.991649,9.818580,5.684465,1.348875,5.762100,-0.447486,-8.758876,4.646615,4.333160,0.912987,-1.738675,-3.944539,-1.485904,2.510203],[9.301809,-3.802301,9.028031,4.510001,-9.283681,-9.202936,9.475232,6.193182,2.009872,2.913319,4.430235,2.531180,4.131895,3.309085,2.142365,-4.001689],[-4.059429,0.988606,-2.145022,-7.090483,-4.716904,9.458262,-7.101136,0.528336,1.988703,-0.944875,2.865337,-4.595869,5.696940,-3.448002,-9.698416,9.448456],[9.359372,-8.176217,0.094904,1.198446,0.149597,2.024030,8.123033,-4.328256,-8.664777,-1.901148,-6.429378,-9.120176,-6.696552,-6.665897,-3.548143,-7.447644]],[[1.699007,9.791690,8.364137,-9.319211,5.600301,-1.523558,-8.501605,1.767936,1.333771,7.504970,5.979888,0.828175,-1.085079,-5.384689,0.452835,4.676347],[-2.830577,2.858197,9.262424,-3.416568,-8.006945,7.527593,9.043035,4.530961,-3.448138,7.210324,-3.621065,-6.061988,-9.913882,4.386939,8.119739,-6.890723],[-9.649191,7.504371,9.023648,-9.125757,0.048345,3.402524,7.869898,8.478972,7.237989,8.192514,-2.247281,-5.948339,-8.979647,-3.602693,-0.272856,1.160905],[5.074337,-7.312585,4.732683,-2.397706,3.314707,5.187323,-3.570356,-3.147049,7.626869,5.184596,1.033134,0.370047,-2.911910,4.776374,-9.366795,8.794158],[-9.865077,4.014218,-2.327875,-7.500051,3.378610,-7.887422,-3.700076,2.164325,-7.048160,7.167486,-9.871049,-7.479465,3.227239,-3.508798,-6.585245,8.495634],[8.998035,-8.129812,-4.014941,4.660011,8.666282,9.003353,1.563440,4.067404,1.126595,4.842354,4.424357,-1.893363,-0.061053,4.933053,-5.294317,5.872994]],[[4.236067,-8.676248,-7.576603,7.889858,1.267105,4.820315,0.953739,3.860395,-1.877431,-4.423756,-6.810371,-9.828907,5.137443,0.160503,-3.085994,-8.264308],[3.569368,2.929636,-0.570350,1.719697,2.806487,-0.536311,9.920342,0.006789,4.004650,-7.290643,3.546469,-2.006241,-8.362229,-3.577333,-8.298780,-1.650870],[2.865743,6.281240,-6.128214,-9.387869,6.234561,-0.064225,-1.620929,-6.340302,3.218969,8.047462,7.005580,-2.894562,4.467774,-5.585233,8.847890,7.499626],[-7.158708,-2.102596,5.989023,-0.266440,-5.281743,-5.328546,0.325567,-7.002848,1.597324,6.866887,8.980502,-7.531758,-0.111635,-7.973586,6.527023,8.115709],[-7.111308,-1.986265,-5.641529,-3.503461,4.417048,8.887892,-8.261589,8.320151,9.972521,-1.850151,-6.654778,2.777529,-8.110966,-6.396168,-7.490417,0.130045],[-1.319819,-9.982156,2.397404,8.520066,6.127248,2.875745,-8.964881,0.804048,9.770421,-0.945746,-7.085329,-3.122246,2.163864,-4.287744,-8.613813,-7.038724]],[[0.355862,7.764166,4.342946,9.322562,9.380526,-3.021865,-8.637237,3.789340,-4.294320,6.373363,-6.366933,1.845128,5.523938,0.199893,5.293181,-5.923015],[-7.017344,8.935435,-0.974745,7.223173,3.250293,0.331467,4.024842,3.506214,-8.183493,9.953073,8.492608,-5.339387,-2.736274,-4.316030,1.476863,0.628645],[1.935886,5.829439,5.561244,4.582467,4.310283,-5.499491,-7.543085,-0.289937,8.198571,8.013824,-0.904598,3.231280,2.869437,-5.032746,-6.691862,-2.870984],[3.234630,6.392011,-5.949716,9.040236,2.614837,5.978136,-4.649818,-9.389716,8.984992,-0.960335,6.089244,-7.809544,9.801234,4.194846,-3.435866,3.291201],[3.187677,9.376707,-1.998203,1.732993,-4.071177,5.056571,-7.524331,-4.597730,6.545770,9.055595,-1.044140,1.051427,2.851944,8.803314,-1.707551,6.671619],[0.218536,-4.411698,9.660478,9.521910,-6.608891,-0.335152,-2.840404,-1.685090,1.077144,-5.145122,5.620413,-5.364094,-0.125092,1.465010,-0.425891,8.930743]],[[0.920442,3.305649,7.598635,-1.318789,5.652680,4.750411,-3.450767,1.801392,8.684697,0.904282,2.209186,8.654214,-1.167166,5.476373,3.641990,-4.515653],[-5.105795,-1.821014,0.850900,9.968266,4.295010,-8.869212,-9.307127,-5.904667,-1.152959,-5.461999,5.929646,7.366498,-1.386771,-2.056722,1.908656,-0.185954],[0.805397,-4.592780,-4.473619,0.200131,-8.221588,4.055113,-9.190525,-5.993883,4.932124,-9.056941,2.454197,-5.112592,-7.130929,1.343022,-3.724308,7.450909],[-7.859527,-1.162919,5.147719,8.140547,7.243202,-9.811791,-5.363707,-3.977791,-0.261003,-7.159088,8.462783,1.965707,9.710328,4.414288,5.933395,8.153078],[-9.932195,-1.405403,-7.636637,9.962574,-1.861116,4.419867,1.989748,-4.464127,-8.295622,7.201391,-9.406645,-3.148278,7.233419,7.120033,-9.159679,4.796620],[-2.328643,9.079450,9.998708,-1.577714,-9.300079,-3.415236,-2.038949,2.715104,2.324235,-8.775707,-7.372803,2.183383,-1.061283,-2.199597,-5.544829,-2.567549]],[[2.916504,7.693493,-6.021507,-2.706961,4.198625,-1.341728,7.655845,-8.091504,-6.637844,-2.711889,8.527462,2.198266,-3.319281,7.519917,0.200715,2.381693],[5.211403,9.728940,5.872820,-8.829461,-2.672747,-4.295787,5.986022,-5.338576,0.495964,-8.212177,-6.839973,-7.830077,4.260992,5.470546,1.226841,2.517756],[4.799368,5.402535,-2.507329,0.315871,-2.639124,-3.935677,6.713672,-3.227801,-0.869670,2.429875,-4.598129,7.648556,3.061512,-1.332320,-7.921525,0.149720],[-4.510218,-4.601279,1.842975,7.048575,8.625359,5.300970,-5.930417,3.767030,-3.458625,8.145006,-0.026438,-3.933228,-5.326508,6.334261,-6.814454,-5.607098],[0.918873,8.189170,6.007711,-5.976531,-9.650478,8.214616,3.054643,1.072034,2.196901,-1.970436,-5.507958,-9.165747,2.378988,8.042723,-9.129472,-4.431625],[-7.333069,-4.471518,-7.711638,-0.982446,-8.647552,1.272411,-2.535100,4.649355,-2.690471,4.541332,-3.026046,6.530449,0.354109,7.201511,-5.943865,5.519054]],[[8.703808,-9.585558,7.034385,1.422155,-8.432348,9.951390,2.384887,7.537239,8.806096,-3.333188,-1.189148,1.593805,-5.680310,9.861575,8.000771,4.133512],[5.092970,-8.356881,-9.313106,-2.001588,7.164984,1.522783,7.800850,-1.297900,-3.028101,-8.592803,-0.710734,-5.261713,2.774108,9.160108,2.152818,8.549663],[6.475080,7.406677,9.874617,-2.089260,0.794467,-4.771694,-0.108468,2.329488,5.949841,9.293445,-8.303547,8.377078,-6.791677,-1.720600,8.207721,-1.569113],[6.969619,2.456586,1.522243,8.434532,4.627366,2.254765,-9.353128,-2.735873,7.774831,2.342695,-6.268390,8.135151,-1.562865,-7.491962,9.100876,-4.730560],[-9.490685,-8.974762,6.181880,-3.900264,8.500939,5.423983,6.678060,6.913105,4.836704,-0.100815,1.176794,-8.158437,2.671113,-3.297633,3.441638,0.253975],[-6.150384,-2.877906,-9.054777,-7.579463,-0.088208,7.252285,-2.584979,-0.423162,-6.923323,1.761351,-0.840616,1.205356,-3.354253,7.398875,-9.509048,5.673810]],[[-9.878975,-2.343191,-3.635200,-7.700690,-6.905991,-5.298430,-6.277702,8.602010,9.663314,6.469761,-9.882711,7.319604,-2.423494,1.781010,-8.457769,7.416699],[-1.763243,9.715405,-7.802372,4.182235,2.846189,9.131072,9.852013,-8.240754,3.348573,-2.596634,-3.484517,-2.052710,-7.985997,5.254857,-4.787941,5.183807],[5.935933,-0.852445,-9.818988,-9.452051,9.107341,-8.548053,-0.564753,-0.029173,-6.120278,-3.872327,-6.116356,1.988249,-8.180716,1.809564,9.455581,8.444242],[3.051800,-4.271336,9.140357,-9.787438,2.187458,1.119552,3.277231,9.252061,9.493245,3.365282,9.198758,-8.783886,6.450449,-0.094856,3.646608,9.636874],[5.000669,-4.962522,4.814269,-2.452838,7.478552,-7.173837,3.338444,-7.779326,2.567789,-1.752880,-8.109567,-4.314524,3.423518,-4.155251,-7.829007,9.806668],[-5.585795,0.009862,-5.567237,-1.163326,6.341450,3.873362,-0.865624,0.049938,4.047504,-1.257817,0.067648,8.937136,-9.552151,8.335950,-2.186477,-6.599103]],[[-7.937280,-7.854424,6.437362,5.720849,9.484235,7.515289,-5.685453,-7.696435,7.561648,-7.183394,1.316597,7.185442,5.213396,8.979548,9.086002,-8.466141],[4.900022,3.344193,9.686689,3.759424,5.177589,1.910352,-9.095192,4.174315,-2.739362,-2.526072,7.608208,3.145723,-2.088749,-9.313732,4.237974,9.482422],[9.284905,3.805002,2.287230,-8.423871,-6.497574,8.498699,5.474097,-6.728109,-1.810601,6.427656,-8.878640,-7.046883,7.631676,-8.949712,-5.525459,7.792138],[-5.525044,-6.220689,-5.398670,-4.546626,-8.583973,7.299786,-9.368100,-9.306024,-3.746410,0.521564,-7.230362,3.376262,-6.117473,-3.972874,9.098109,0.245368],[2.482534,-6.737916,-9.526353,-3.067851,-5.527894,-7.177147,5.393650,3.137659,-8.791074,-4.261899,-4.534685,0.440889,0.293486,8.199142,9.128157,4.470732],[5.227807,-3.491220,-4.160388,-8.660432,-5.148700,-9.395433,6.901026,1.801370,-4.416812,1.252183,6.203817,8.610370,-0.110242,-3.920333,0.639312,-4.123232]],[[7.670739,-3.291187,4.815182,-4.570017,0.780918,3.777948,-4.279552,4.074819,-9.600987,5.627862,0.554124,8.470793,-9.315078,3.121271,8.656999,-9.740612],[2.292185,-6.854811,4.029963,-5.803769,3.977614,-2.965301,9.601144,-1.500418,-0.125737,1.361642,2.233310,8.065479,-1.299489,6.739335,6.641420,-3.115271],[7.069660,2.058022,5.478412,4.833109,-7.492152,-0.891810,6.736172,2.016528,8.492497,5.224327,6.205316,-2.884381,-3.881161,4.112113,3.065755,-0.078127],[8.635593,5.223498,6.515752,8.035355,-5.515404,3.827774,9.815651,9.490057,-4.675154,4.454610,-9.761682,0.259894,7.591146,-6.071046,6.995339,6.409303],[-9.828686,3.904919,-9.689232,4.628108,3.803293,-7.755161,-7.892590,4.566259,8.681953,-0.622603,-2.227517,-6.090324,4.475855,-0.041807,6.952015,1.631865],[-1.870435,7.683467,5.863919,-8.725566,-4.257001,3.999303,-5.763973,4.683368,1.804289,0.963004,9.477912,-6.110642,-6.057494,3.059173,-0.680283,-6.877523]],[[-3.213790,8.840469,-8.123502,-6.005331,3.009511,9.127212,-7.576737,8.983602,5.473343,2.115101,-6.833811,3.906458,-3.233570,-6.106727,1.552892,2.330808],[-9.284956,0.244945,-8.034273,5.759636,-7.765071,-5.307806,4.059750,-0.798465,-5.855756,-6.360333,2.723050,-0.759689,-9.204915,8.713625,0.517118,6.066349],[6.229864,-8.524289,-7.128054,1.099523,4.279296,2.624773,9.742186,0.047981,0.169484,-8.811784,3.731818,-1.768368,0.082124,1.170567,3.793615,8.972656],[8.461366,-7.322311,5.342509,-4.387491,5.225565,-6.299881,-4.844157,5.066713,2.243962,-9.075272,-5.992653,-4.293074,-1.045701,-4.198241,1.327821,2.519941],[3.228515,-8.563251,4.592480,5.074417,4.831789,-5.735861,9.209313,5.986760,5.933885,7.542918,2.821097,-5.172669,9.235377,1.811288,-3.229237,-7.954472],[-1.874230,-2.138492,6.692606,4.837693,2.293332,-6.029121,6.771553,0.105709,-2.864171,-1.464780,9.821339,0.632569,5.034409,8.307130,7.492662,7.458087]],[[-8.032456,-9.973235,-0.850752,-9.011410,6.174040,-5.962860,0.421922,3.055220,3.944754,1.619792,-7.334332,5.761490,1.476765,2.764419,-4.161114,-4.495008],[0.801012,9.014748,-6.314678,0.151529,-7.288687,-0.063349,-3.171454,8.154330,8.519004,-3.338479,-2.659001,2.782138,-4.048633,-0.674957,-6.746894,6.221744],[6.535351,5.625043,3.831172,9.451005,-0.532160,7.372886,-0.863050,-8.210346,0.715683,2.298340,6.384429,2.231386,-1.975690,-4.793903,-1.411340,-8.084266],[-0.649080,-2.512830,-1.538406,-8.225454,2.042311,7.491641,-9.003547,-7.139380,-1.011517,3.764214,-2.023098,7.607217,8.133865,1.428018,-7.964481,4.330462],[2.005206,-5.700471,-3.436560,4.425980,-6.364923,1.111797,-7.294655,-6.170307,9.248132,-7.366228,-4.889763,-8.911412,-3.078745,0.431976,3.825914,0.525059],[-4.914340,9.305193,-0.043875,8.704277,5.189647,-1.265587,-3.227289,4.974091,-4.853249,5.708757,8.797234,-2.689655,-4.763713,-7.474218,4.757645,-7.567105]],[[9.434858,-4.317830,-7.696359,-0.420936,-4.474468,-5.261125,6.301381,-1.253638,9.708701,-0.983707,-5.013943,-8.330825,1.532709,-0.976373,2.724453,-2.481589],[-1.134928,-1.120420,-8.291441,8.199147,5.016455,9.347107,5.615377,8.874590,-7.910377,6.406237,-8.941527,1.047391,4.529758,-3.408055,-7.893639,2.068351],[7.640183,-6.002330,8.556217,-6.612092,3.368045,1.003615,-4.836955,9.602210,4.516088,6.733289,6.364186,7.090919,-2.391057,5.848065,-4.911154,-9.863817],[-2.602310,-9.179306,-3.055371,4.141460,-2.184588,-4.867415,2.334886,7.242410,-0.331508,-7.651705,7.676474,-7.081291,-4.754258,3.253604,0.872474,-9.758412],[-3.068347,3.526035,-2.930477,-9.690919,6.228065,7.549094,-4.239902,5.359395,7.683810,-8.113141,2.639737,-9.350981,-9.763139,4.595018,8.241328,-2.730628],[-8.223179,-4.565068,-4.738552,4.985840,3.273711,-9.778676,-2.086904,3.334651,1.537510,-2.770649,-2.001293,-0.248410,-1.835902,-5.865418,-5.562840,9.182509]]], dtype = "float32")#candidate|164|(14, 6, 16)|const|float32
uop_165 = relay.erf(const_164.astype('float32')) # shape=(14, 6, 16)
uop_177 = relay.sinh(uop_165.astype('float32')) # shape=(14, 6, 16)
output = uop_177
output2 = uop_177
func_191 = relay.Function([], output)
mod['func_191'] = func_191
mod = relay.transform.InferType()(mod)
mutated_mod['func_191'] = func_191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_191_call = mutated_mod.get_global_var('func_191')
call_192 = func_191_call()
output = call_192
func_193 = relay.Function([], output)
mutated_mod['func_193'] = func_193
mutated_mod = relay.transform.InferType()(mutated_mod)
var_210 = relay.var("var_210", dtype = "int64", shape = (12, 4, 7))#candidate|210|(12, 4, 7)|var|int64
var_211 = relay.var("var_211", dtype = "int64", shape = (12, 4, 7))#candidate|211|(12, 4, 7)|var|int64
bop_212 = relay.greater_equal(var_210.astype('bool'), relay.reshape(var_211.astype('bool'), relay.shape_of(var_210))) # shape=(12, 4, 7)
uop_220 = relay.tan(var_210.astype('float32')) # shape=(12, 4, 7)
bop_222 = relay.maximum(bop_212.astype('float64'), relay.reshape(var_211.astype('float64'), relay.shape_of(bop_212))) # shape=(12, 4, 7)
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_227 = func_191_call()
call_228 = func_191_call()
bop_234 = relay.not_equal(uop_220.astype('bool'), relay.reshape(bop_222.astype('bool'), relay.shape_of(uop_220))) # shape=(12, 4, 7)
var_237 = relay.var("var_237", dtype = "float32", shape = (12, 4, 7))#candidate|237|(12, 4, 7)|var|float32
bop_238 = relay.power(uop_220.astype('float32'), relay.reshape(var_237.astype('float32'), relay.shape_of(uop_220))) # shape=(12, 4, 7)
output = relay.Tuple([call_227,bop_234,bop_238,])
output2 = relay.Tuple([call_228,bop_234,bop_238,])
func_246 = relay.Function([var_210,var_211,var_237,], output)
mod['func_246'] = func_246
mod = relay.transform.InferType()(mod)
var_247 = relay.var("var_247", dtype = "int64", shape = (12, 4, 7))#candidate|247|(12, 4, 7)|var|int64
var_248 = relay.var("var_248", dtype = "int64", shape = (12, 4, 7))#candidate|248|(12, 4, 7)|var|int64
var_249 = relay.var("var_249", dtype = "float32", shape = (12, 4, 7))#candidate|249|(12, 4, 7)|var|float32
output = func_246(var_247,var_248,var_249,)
func_250 = relay.Function([var_247,var_248,var_249,], output)
mutated_mod['func_250'] = func_250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_264 = func_191_call()
call_265 = func_191_call()
output = call_264
output2 = call_265
func_294 = relay.Function([], output)
mod['func_294'] = func_294
mod = relay.transform.InferType()(mod)
mutated_mod['func_294'] = func_294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_294_call = mutated_mod.get_global_var('func_294')
call_295 = func_294_call()
output = call_295
func_296 = relay.Function([], output)
mutated_mod['func_296'] = func_296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_324 = func_294_call()
call_325 = func_294_call()
output = call_324
output2 = call_325
func_331 = relay.Function([], output)
mod['func_331'] = func_331
mod = relay.transform.InferType()(mod)
mutated_mod['func_331'] = func_331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_331_call = mutated_mod.get_global_var('func_331')
call_332 = func_331_call()
output = call_332
func_333 = relay.Function([], output)
mutated_mod['func_333'] = func_333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_392 = func_331_call()
call_393 = func_331_call()
var_394 = relay.var("var_394", dtype = "float32", shape = (14, 6, 16))#candidate|394|(14, 6, 16)|var|float32
bop_395 = relay.bitwise_and(call_392.astype('uint8'), relay.reshape(var_394.astype('uint8'), relay.shape_of(call_392))) # shape=(14, 6, 16)
bop_398 = relay.bitwise_and(call_393.astype('uint8'), relay.reshape(var_394.astype('uint8'), relay.shape_of(call_393))) # shape=(14, 6, 16)
bop_402 = relay.less(bop_395.astype('bool'), relay.reshape(var_394.astype('bool'), relay.shape_of(bop_395))) # shape=(14, 6, 16)
bop_405 = relay.less(bop_398.astype('bool'), relay.reshape(var_394.astype('bool'), relay.shape_of(bop_398))) # shape=(14, 6, 16)
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_408 = func_191_call()
call_409 = func_191_call()
var_412 = relay.var("var_412", dtype = "float32", shape = (14, 6, 16))#candidate|412|(14, 6, 16)|var|float32
bop_413 = relay.add(call_392.astype('float64'), relay.reshape(var_412.astype('float64'), relay.shape_of(call_392))) # shape=(14, 6, 16)
bop_416 = relay.add(call_393.astype('float64'), relay.reshape(var_412.astype('float64'), relay.shape_of(call_393))) # shape=(14, 6, 16)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_418 = func_331_call()
call_419 = func_331_call()
func_246_call = mod.get_global_var('func_246')
func_250_call = mutated_mod.get_global_var('func_250')
const_422 = relay.const([4,-9,-4,2,-5,-6,-5,9,9,-7,-4,-6,-1,10,-1,-5,6,-5,4,-2,10,5,-8,1,6,2,8,6,4,7,10,-10,3,-1,-3,-7,10,-10,8,8,3,3,-8,1,4,-7,7,3,5,8,-6,10,-6,-4,4,-8,2,8,-4,-1,-6,-5,10,-4,3,-4,6,-2,-6,9,-8,9,-2,-7,-6,5,1,-5,-7,7,-1,-6,4,-9,6,-2,-7,-2,8,3,2,-5,7,5,1,3,-2,8,1,-6,-7,1,1,-1,5,-4,2,-1,1,3,5,-5,9,2,-3,6,1,4,-1,3,-10,6,-6,3,2,-1,-3,5,-2,-9,7,4,3,10,-4,-3,-9,8,-5,-5,4,3,4,9,-4,10,-6,-1,-6,-6,-5,-7,-7,10,-4,8,-2,-7,-10,4,-9,-7,-3,-5,-1,-9,9,1,-1,-7,-5,-2,5,-7,8,-10,8,-1,8,-9,-8,-7,6,-10,-8,-9,1,2,-3,-2,10,7,1,-6,5,-10,-6,9,-5,-7,7,8,9,5,-8,-10,-10,6,-6,-2,10,3,9,7,10,-8,10,-4,-5,9,-7,4,8,9,-2,5,3,7,-10,9,-8,7,-3,7,10,-3,-8,4,-5,-10,-4,-9,2,10,-10,-2,-5,6,-1,-6,-10,-10,4,-4,7,-7,6,-7,-2,10,5,10,-2,6,9,6,2,8,8,-6,4,3,9,-8,-8,-5,-2,-10,9,-10,9,8,2,7,7,-4,-7,3,-8,9,1,6,8,2,4,-8,7,-6,5,8,1,3,10,5,8,3,-9,5,-7,-7,-8,-7,2,-6,1,8,-10,9,8,-8,-10,-6,-2,-4,-7,-3,7,-1,-7,7,5,-9,6,-4,4,1], dtype = "int64")#candidate|422|(336,)|const|int64
call_421 = relay.TupleGetItem(func_246_call(relay.reshape(const_422.astype('int64'), [12, 4, 7]), relay.reshape(const_422.astype('int64'), [12, 4, 7]), relay.reshape(const_422.astype('float32'), [12, 4, 7]), ), 2)
call_423 = relay.TupleGetItem(func_250_call(relay.reshape(const_422.astype('int64'), [12, 4, 7]), relay.reshape(const_422.astype('int64'), [12, 4, 7]), relay.reshape(const_422.astype('float32'), [12, 4, 7]), ), 2)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_425 = func_294_call()
call_426 = func_294_call()
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_433 = func_294_call()
call_434 = func_294_call()
output = relay.Tuple([bop_402,call_408,bop_413,call_418,call_421,const_422,call_425,call_433,])
output2 = relay.Tuple([bop_405,call_409,bop_416,call_419,call_423,const_422,call_426,call_434,])
func_435 = relay.Function([var_394,var_412,], output)
mod['func_435'] = func_435
mod = relay.transform.InferType()(mod)
var_436 = relay.var("var_436", dtype = "float32", shape = (14, 6, 16))#candidate|436|(14, 6, 16)|var|float32
var_437 = relay.var("var_437", dtype = "float32", shape = (14, 6, 16))#candidate|437|(14, 6, 16)|var|float32
output = func_435(var_436,var_437,)
func_438 = relay.Function([var_436,var_437,], output)
mutated_mod['func_438'] = func_438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_449 = func_191_call()
call_450 = func_191_call()
uop_459 = relay.sqrt(call_449.astype('float64')) # shape=(14, 6, 16)
uop_461 = relay.sqrt(call_450.astype('float64')) # shape=(14, 6, 16)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_469 = func_294_call()
call_470 = func_294_call()
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
call_474 = relay.TupleGetItem(func_435_call(relay.reshape(call_469.astype('float32'), [14, 6, 16]), relay.reshape(uop_459.astype('float32'), [14, 6, 16]), ), 2)
call_475 = relay.TupleGetItem(func_438_call(relay.reshape(call_469.astype('float32'), [14, 6, 16]), relay.reshape(uop_459.astype('float32'), [14, 6, 16]), ), 2)
output = relay.Tuple([uop_459,call_469,call_474,])
output2 = relay.Tuple([uop_461,call_470,call_475,])
func_479 = relay.Function([], output)
mod['func_479'] = func_479
mod = relay.transform.InferType()(mod)
output = func_479()
func_480 = relay.Function([], output)
mutated_mod['func_480'] = func_480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_481 = func_331_call()
call_482 = func_331_call()
uop_525 = relay.cos(call_481.astype('float64')) # shape=(14, 6, 16)
uop_527 = relay.cos(call_482.astype('float64')) # shape=(14, 6, 16)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_528 = func_294_call()
call_529 = func_294_call()
output = relay.Tuple([uop_525,call_528,])
output2 = relay.Tuple([uop_527,call_529,])
func_534 = relay.Function([], output)
mod['func_534'] = func_534
mod = relay.transform.InferType()(mod)
mutated_mod['func_534'] = func_534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mutated_mod.get_global_var('func_534')
call_535 = func_534_call()
output = call_535
func_536 = relay.Function([], output)
mutated_mod['func_536'] = func_536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_631 = relay.TupleGetItem(func_534_call(), 1)
call_632 = relay.TupleGetItem(func_536_call(), 1)
output = relay.Tuple([call_631,])
output2 = relay.Tuple([call_632,])
func_634 = relay.Function([], output)
mod['func_634'] = func_634
mod = relay.transform.InferType()(mod)
mutated_mod['func_634'] = func_634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mutated_mod.get_global_var('func_634')
call_635 = func_634_call()
output = call_635
func_636 = relay.Function([], output)
mutated_mod['func_636'] = func_636
mutated_mod = relay.transform.InferType()(mutated_mod)
var_645 = relay.var("var_645", dtype = "float64", shape = (16, 2))#candidate|645|(16, 2)|var|float64
uop_646 = relay.sigmoid(var_645.astype('float64')) # shape=(16, 2)
output = uop_646
output2 = uop_646
func_655 = relay.Function([var_645,], output)
mod['func_655'] = func_655
mod = relay.transform.InferType()(mod)
mutated_mod['func_655'] = func_655
mutated_mod = relay.transform.InferType()(mutated_mod)
var_656 = relay.var("var_656", dtype = "float64", shape = (16, 2))#candidate|656|(16, 2)|var|float64
func_655_call = mutated_mod.get_global_var('func_655')
call_657 = func_655_call(var_656)
output = call_657
func_658 = relay.Function([var_656], output)
mutated_mod['func_658'] = func_658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_672 = func_331_call()
call_673 = func_331_call()
var_674 = relay.var("var_674", dtype = "float32", shape = (14, 6, 16))#candidate|674|(14, 6, 16)|var|float32
bop_675 = relay.bitwise_xor(call_672.astype('int16'), relay.reshape(var_674.astype('int16'), relay.shape_of(call_672))) # shape=(14, 6, 16)
bop_678 = relay.bitwise_xor(call_673.astype('int16'), relay.reshape(var_674.astype('int16'), relay.shape_of(call_673))) # shape=(14, 6, 16)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_688 = func_331_call()
call_689 = func_331_call()
output = relay.Tuple([bop_675,call_688,])
output2 = relay.Tuple([bop_678,call_689,])
func_692 = relay.Function([var_674,], output)
mod['func_692'] = func_692
mod = relay.transform.InferType()(mod)
var_693 = relay.var("var_693", dtype = "float32", shape = (14, 6, 16))#candidate|693|(14, 6, 16)|var|float32
output = func_692(var_693)
func_694 = relay.Function([var_693], output)
mutated_mod['func_694'] = func_694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_696 = func_294_call()
call_697 = func_294_call()
var_713 = relay.var("var_713", dtype = "float32", shape = (14, 6, 16))#candidate|713|(14, 6, 16)|var|float32
bop_714 = relay.equal(call_696.astype('bool'), relay.reshape(var_713.astype('bool'), relay.shape_of(call_696))) # shape=(14, 6, 16)
bop_717 = relay.equal(call_697.astype('bool'), relay.reshape(var_713.astype('bool'), relay.shape_of(call_697))) # shape=(14, 6, 16)
uop_723 = relay.atanh(var_713.astype('float32')) # shape=(14, 6, 16)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_727 = relay.TupleGetItem(func_534_call(), 0)
call_728 = relay.TupleGetItem(func_536_call(), 0)
output = relay.Tuple([bop_714,uop_723,call_727,])
output2 = relay.Tuple([bop_717,uop_723,call_728,])
func_730 = relay.Function([var_713,], output)
mod['func_730'] = func_730
mod = relay.transform.InferType()(mod)
mutated_mod['func_730'] = func_730
mutated_mod = relay.transform.InferType()(mutated_mod)
var_731 = relay.var("var_731", dtype = "float32", shape = (14, 6, 16))#candidate|731|(14, 6, 16)|var|float32
func_730_call = mutated_mod.get_global_var('func_730')
call_732 = func_730_call(var_731)
output = call_732
func_733 = relay.Function([var_731], output)
mutated_mod['func_733'] = func_733
mutated_mod = relay.transform.InferType()(mutated_mod)
var_735 = relay.var("var_735", dtype = "uint8", shape = (15, 12, 5))#candidate|735|(15, 12, 5)|var|uint8
var_736 = relay.var("var_736", dtype = "uint8", shape = (15, 12, 5))#candidate|736|(15, 12, 5)|var|uint8
bop_737 = relay.subtract(var_735.astype('uint8'), relay.reshape(var_736.astype('uint8'), relay.shape_of(var_735))) # shape=(15, 12, 5)
func_730_call = mod.get_global_var('func_730')
func_733_call = mutated_mod.get_global_var('func_733')
var_742 = relay.var("var_742", dtype = "float32", shape = (1344,))#candidate|742|(1344,)|var|float32
call_741 = relay.TupleGetItem(func_730_call(relay.reshape(var_742.astype('float32'), [14, 6, 16])), 2)
call_743 = relay.TupleGetItem(func_733_call(relay.reshape(var_742.astype('float32'), [14, 6, 16])), 2)
output = relay.Tuple([bop_737,call_741,var_742,])
output2 = relay.Tuple([bop_737,call_743,var_742,])
func_756 = relay.Function([var_735,var_736,var_742,], output)
mod['func_756'] = func_756
mod = relay.transform.InferType()(mod)
mutated_mod['func_756'] = func_756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_756_call = mutated_mod.get_global_var('func_756')
var_758 = relay.var("var_758", dtype = "uint8", shape = (15, 12, 5))#candidate|758|(15, 12, 5)|var|uint8
var_759 = relay.var("var_759", dtype = "uint8", shape = (15, 12, 5))#candidate|759|(15, 12, 5)|var|uint8
var_760 = relay.var("var_760", dtype = "float32", shape = (1344,))#candidate|760|(1344,)|var|float32
call_757 = func_756_call(var_758,var_759,var_760,)
output = call_757
func_761 = relay.Function([var_758,var_759,var_760,], output)
mutated_mod['func_761'] = func_761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_480_call = mutated_mod.get_global_var('func_480')
call_782 = relay.TupleGetItem(func_479_call(), 1)
call_783 = relay.TupleGetItem(func_480_call(), 1)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_785 = relay.TupleGetItem(func_634_call(), 0)
call_786 = relay.TupleGetItem(func_636_call(), 0)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
call_803 = relay.TupleGetItem(func_435_call(relay.reshape(call_782.astype('float32'), [14, 6, 16]), relay.reshape(call_785.astype('float32'), [14, 6, 16]), ), 6)
call_804 = relay.TupleGetItem(func_438_call(relay.reshape(call_782.astype('float32'), [14, 6, 16]), relay.reshape(call_785.astype('float32'), [14, 6, 16]), ), 6)
output = relay.Tuple([call_782,call_785,call_803,])
output2 = relay.Tuple([call_783,call_786,call_804,])
func_811 = relay.Function([], output)
mod['func_811'] = func_811
mod = relay.transform.InferType()(mod)
mutated_mod['func_811'] = func_811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mutated_mod.get_global_var('func_811')
call_812 = func_811_call()
output = call_812
func_813 = relay.Function([], output)
mutated_mod['func_813'] = func_813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_814 = relay.TupleGetItem(func_634_call(), 0)
call_815 = relay.TupleGetItem(func_636_call(), 0)
output = call_814
output2 = call_815
func_834 = relay.Function([], output)
mod['func_834'] = func_834
mod = relay.transform.InferType()(mod)
output = func_834()
func_835 = relay.Function([], output)
mutated_mod['func_835'] = func_835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_836 = relay.TupleGetItem(func_534_call(), 1)
call_837 = relay.TupleGetItem(func_536_call(), 1)
output = relay.Tuple([call_836,])
output2 = relay.Tuple([call_837,])
func_876 = relay.Function([], output)
mod['func_876'] = func_876
mod = relay.transform.InferType()(mod)
mutated_mod['func_876'] = func_876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mutated_mod.get_global_var('func_876')
call_877 = func_876_call()
output = call_877
func_878 = relay.Function([], output)
mutated_mod['func_878'] = func_878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_893 = relay.TupleGetItem(func_534_call(), 0)
call_894 = relay.TupleGetItem(func_536_call(), 0)
func_811_call = mod.get_global_var('func_811')
func_813_call = mutated_mod.get_global_var('func_813')
call_929 = relay.TupleGetItem(func_811_call(), 0)
call_930 = relay.TupleGetItem(func_813_call(), 0)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
const_973 = relay.const([4.711391,7.519252,-3.626891,-2.734549,-5.724496,8.137041,5.863482,3.746540,6.942384,1.946115,4.438397,-9.363467,-4.227210,2.158347,8.843552,0.848731,6.293225,-1.921874,-4.184241,-2.463602,-9.131079,6.130878,-9.186458,-6.307556,-1.252519,-7.801731,-6.567182,6.903254,8.166998,-6.592206,-1.474971,2.157963], dtype = "float64")#candidate|973|(32,)|const|float64
call_972 = func_655_call(relay.reshape(const_973.astype('float64'), [16, 2]))
call_974 = func_655_call(relay.reshape(const_973.astype('float64'), [16, 2]))
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_975 = func_191_call()
call_976 = func_191_call()
output = relay.Tuple([call_893,call_929,call_972,const_973,call_975,])
output2 = relay.Tuple([call_894,call_930,call_974,const_973,call_976,])
func_978 = relay.Function([], output)
mod['func_978'] = func_978
mod = relay.transform.InferType()(mod)
mutated_mod['func_978'] = func_978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_978_call = mutated_mod.get_global_var('func_978')
call_979 = func_978_call()
output = call_979
func_980 = relay.Function([], output)
mutated_mod['func_980'] = func_980
mutated_mod = relay.transform.InferType()(mutated_mod)
var_997 = relay.var("var_997", dtype = "int32", shape = (11, 1, 8))#candidate|997|(11, 1, 8)|var|int32
var_998 = relay.var("var_998", dtype = "int32", shape = (11, 10, 8))#candidate|998|(11, 10, 8)|var|int32
bop_999 = relay.subtract(var_997.astype('int32'), var_998.astype('int32')) # shape=(11, 10, 8)
uop_1011 = relay.rsqrt(bop_999.astype('float32')) # shape=(11, 10, 8)
output = uop_1011
output2 = uop_1011
func_1018 = relay.Function([var_997,var_998,], output)
mod['func_1018'] = func_1018
mod = relay.transform.InferType()(mod)
var_1019 = relay.var("var_1019", dtype = "int32", shape = (11, 1, 8))#candidate|1019|(11, 1, 8)|var|int32
var_1020 = relay.var("var_1020", dtype = "int32", shape = (11, 10, 8))#candidate|1020|(11, 10, 8)|var|int32
output = func_1018(var_1019,var_1020,)
func_1021 = relay.Function([var_1019,var_1020,], output)
mutated_mod['func_1021'] = func_1021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_1032 = relay.TupleGetItem(func_876_call(), 0)
call_1033 = relay.TupleGetItem(func_878_call(), 0)
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_1042 = func_191_call()
call_1043 = func_191_call()
func_1018_call = mod.get_global_var('func_1018')
func_1021_call = mutated_mod.get_global_var('func_1021')
var_1046 = relay.var("var_1046", dtype = "int32", shape = (88,))#candidate|1046|(88,)|var|int32
const_1047 = relay.const([7,1,-6,-3,10,10,4,1,3,4,-1,3,10,3,2,-9,5,-2,-7,-3,-10,10,-4,-8,8,-6,1,-8,5,-8,1,-7,-7,7,-1,10,5,5,-2,8,-7,9,-2,-8,6,6,-3,-4,-2,-4,-1,-6,6,-6,8,-8,-8,2,2,9,-8,-7,-7,-1,2,-4,10,9,-3,6,-1,-6,-1,-9,2,1,2,-3,9,-10,9,-3,-5,-7,-9,2,7,-7,8,-1,5,-2,-2,-7,-7,1,2,7,6,6,6,3,5,4,-7,6,7,-8,3,9,2,-7,3,10,7,5,5,9,-8,-5,-7,7,-1,4,-8,-3,4,3,-2,-7,10,-2,-9,-4,5,-2,-4,-8,-3,6,-9,2,-9,-1,9,-1,1,3,-6,7,-10,-6,1,7,10,5,-4,-1,5,7,-3,2,-2,3,6,1,-2,-10,3,-7,3,-2,-3,4,-8,-2,7,-4,3,-9,9,4,-7,4,-4,-4,-5,5,-1,7,-8,-10,-3,6,-10,-4,4,-2,-2,2,-9,2,5,3,-6,7,7,1,-10,7,-1,-10,-9,-8,9,7,-8,-4,-8,-3,7,-8,-7,-6,9,8,-6,-7,-3,6,-6,-1,-3,9,2,-6,2,-3,5,6,5,-4,-6,-6,7,-2,6,-7,-10,10,8,9,10,-1,-3,10,2,-9,-6,-9,8,4,-7,-2,-7,7,8,7,9,-4,-4,-2,-8,-7,7,-7,-7,8,-4,-1,3,-6,7,9,-1,10,-7,2,-7,-2,-2,1,2,7,10,-6,-7,3,8,-2,5,2,8,7,-2,-10,-8,8,-10,5,-3,4,5,-6,1,10,1,8,-8,5,-6,6,5,3,7,9,2,1,-1,10,4,8,4,7,2,3,8,-1,3,10,3,1,-3,3,-7,5,-5,-1,10,-10,-1,-10,2,1,7,-5,-3,8,-9,9,3,9,9,-6,9,3,9,-6,7,6,1,6,10,-9,4,4,1,7,7,-1,1,6,-9,3,-2,-10,2,6,-2,10,-2,-5,-10,-7,8,-3,1,-9,2,6,10,-6,4,4,-8,1,-9,-6,-1,-7,-10,7,10,2,9,5,-6,2,4,5,10,-3,-4,-9,-2,5,-7,-5,-2,8,-7,-1,-3,-2,-10,-10,-6,-3,-3,-7,-1,9,9,-4,1,2,-4,-10,7,5,-2,2,-9,8,7,7,2,-5,-7,1,2,7,-6,4,-10,3,-5,10,9,-6,-5,-4,8,-7,-10,-5,4,8,-9,-5,1,-1,-2,10,8,10,8,2,5,3,10,10,1,5,-2,9,8,-2,2,4,8,5,7,-4,-9,-10,6,-6,-9,9,9,7,-9,-10,8,10,7,4,5,6,4,6,7,-10,-10,8,-8,-9,-1,-7,4,-7,-7,4,-8,7,-8,5,-2,10,2,3,2,-7,2,3,5,6,-2,1,1,-3,10,4,1,-6,-3,-4,-3,-7,-7,1,-2,-4,-5,4,5,-7,-5,7,-5,10,-1,3,7,9,10,-8,6,7,-6,-9,10,4,-7,3,5,9,10,-2,-2,3,-10,6,-10,7,-8,5,-2,-5,-1,8,4,3,-1,-2,-7,-5,-3,-3,6,9,6,-1,-4,-5,7,-2,-5,6,2,-9,1,4,-6,9,6,-5,-1,-9,3,9,-9,2,7,-10,-5,8,2,2,-8,10,-8,-8,-1,5,3,5,-6,-8,4,2,4,5,-1,-3,-9,-6,-6,-7,1,3,7,-6,5,-6,1,-8,9,2,-2,10,8,2,10,2,-3,-5,-3,3,-6,-6,-8,-3,-8,8,10,5,6,3,-7,7,-2,-8,5,10,2,-8,10,1,8,2,-9,-7,2,-3,9,-9,-4,3,-10,-1,-10,-7,2,-10,7,-10,7,-1,1,10,-4,8,-5,5,7,10,-7,-10,2,9,2,-6,-9,1,-9,-10,7,-10,3,8,3,7,-4,9,9,-5,-9,3,8,-10,3,1,-1,4,10,2,-1,-3,8,-3,10,-7,1,-9,-3,7,10,-10,10,-3,-8,-4,-5,-6,-9,-9,8,-9,7,-7,6,6,1,5,10,2,4,-8,2,-2,-2,-1,-9,9,-8,-4,-10,10,-8,5,-4,5,2,9,-9,7,3,4,-10,-8,1,5,-4,-3,10,10,4,4,-1,1,3,3,-8,8,2,-6,-7,4,-6,2,6,1,-7,5,-7,8,-4,8,10,10,9,2,-7,-7,-3,10,-3,9,-6,-10,3,-3,-2,9,-6,-1,4,-2,2,-5,-2,-4,4,7,-10,-2,-6,9,7,-10,-6,-7,6,3,-3,-3,-3,-10], dtype = "int32")#candidate|1047|(880,)|const|int32
call_1045 = func_1018_call(relay.reshape(var_1046.astype('int32'), [11, 1, 8]), relay.reshape(const_1047.astype('int32'), [11, 10, 8]), )
call_1048 = func_1018_call(relay.reshape(var_1046.astype('int32'), [11, 1, 8]), relay.reshape(const_1047.astype('int32'), [11, 10, 8]), )
output = relay.Tuple([call_1032,call_1042,call_1045,var_1046,const_1047,])
output2 = relay.Tuple([call_1033,call_1043,call_1048,var_1046,const_1047,])
func_1055 = relay.Function([var_1046,], output)
mod['func_1055'] = func_1055
mod = relay.transform.InferType()(mod)
mutated_mod['func_1055'] = func_1055
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1056 = relay.var("var_1056", dtype = "int32", shape = (88,))#candidate|1056|(88,)|var|int32
func_1055_call = mutated_mod.get_global_var('func_1055')
call_1057 = func_1055_call(var_1056)
output = call_1057
func_1058 = relay.Function([var_1056], output)
mutated_mod['func_1058'] = func_1058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_1107 = relay.TupleGetItem(func_534_call(), 0)
call_1108 = relay.TupleGetItem(func_536_call(), 0)
uop_1109 = relay.exp(call_1107.astype('float64')) # shape=(14, 6, 16)
uop_1111 = relay.exp(call_1108.astype('float64')) # shape=(14, 6, 16)
bop_1132 = relay.floor_mod(uop_1109.astype('float32'), relay.reshape(call_1107.astype('float32'), relay.shape_of(uop_1109))) # shape=(14, 6, 16)
bop_1135 = relay.floor_mod(uop_1111.astype('float32'), relay.reshape(call_1108.astype('float32'), relay.shape_of(uop_1111))) # shape=(14, 6, 16)
func_811_call = mod.get_global_var('func_811')
func_813_call = mutated_mod.get_global_var('func_813')
call_1137 = relay.TupleGetItem(func_811_call(), 2)
call_1138 = relay.TupleGetItem(func_813_call(), 2)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
const_1141 = relay.const([[-6.877249,8.886326,1.037082,-3.343919],[-3.591972,9.951113,6.784246,-5.263927],[3.579292,-3.434877,1.743840,-6.283603],[-7.561549,3.207569,-8.346568,-4.187011],[0.436144,-2.647537,-1.991383,-2.848272],[3.984047,-7.626054,9.988035,-3.944884],[-1.464925,0.480494,1.887944,-4.888511],[0.852787,-0.874114,0.699600,4.491361]], dtype = "float64")#candidate|1141|(8, 4)|const|float64
call_1140 = func_655_call(relay.reshape(const_1141.astype('float64'), [16, 2]))
call_1142 = func_655_call(relay.reshape(const_1141.astype('float64'), [16, 2]))
func_811_call = mod.get_global_var('func_811')
func_813_call = mutated_mod.get_global_var('func_813')
call_1143 = relay.TupleGetItem(func_811_call(), 2)
call_1144 = relay.TupleGetItem(func_813_call(), 2)
output = relay.Tuple([bop_1132,call_1137,call_1140,const_1141,call_1143,])
output2 = relay.Tuple([bop_1135,call_1138,call_1142,const_1141,call_1144,])
func_1150 = relay.Function([], output)
mod['func_1150'] = func_1150
mod = relay.transform.InferType()(mod)
mutated_mod['func_1150'] = func_1150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1150_call = mutated_mod.get_global_var('func_1150')
call_1151 = func_1150_call()
output = call_1151
func_1152 = relay.Function([], output)
mutated_mod['func_1152'] = func_1152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_978_call = mod.get_global_var('func_978')
func_980_call = mutated_mod.get_global_var('func_980')
call_1199 = relay.TupleGetItem(func_978_call(), 4)
call_1200 = relay.TupleGetItem(func_980_call(), 4)
func_692_call = mod.get_global_var('func_692')
func_694_call = mutated_mod.get_global_var('func_694')
call_1223 = relay.TupleGetItem(func_692_call(relay.reshape(call_1199.astype('float32'), [14, 6, 16])), 0)
call_1224 = relay.TupleGetItem(func_694_call(relay.reshape(call_1199.astype('float32'), [14, 6, 16])), 0)
output = relay.Tuple([call_1199,call_1223,])
output2 = relay.Tuple([call_1200,call_1224,])
func_1232 = relay.Function([], output)
mod['func_1232'] = func_1232
mod = relay.transform.InferType()(mod)
output = func_1232()
func_1233 = relay.Function([], output)
mutated_mod['func_1233'] = func_1233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_1240 = relay.TupleGetItem(func_534_call(), 0)
call_1241 = relay.TupleGetItem(func_536_call(), 0)
uop_1246 = relay.asin(call_1240.astype('float32')) # shape=(14, 6, 16)
uop_1248 = relay.asin(call_1241.astype('float32')) # shape=(14, 6, 16)
func_811_call = mod.get_global_var('func_811')
func_813_call = mutated_mod.get_global_var('func_813')
call_1257 = relay.TupleGetItem(func_811_call(), 2)
call_1258 = relay.TupleGetItem(func_813_call(), 2)
output = relay.Tuple([uop_1246,call_1257,])
output2 = relay.Tuple([uop_1248,call_1258,])
func_1271 = relay.Function([], output)
mod['func_1271'] = func_1271
mod = relay.transform.InferType()(mod)
output = func_1271()
func_1272 = relay.Function([], output)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1355 = relay.var("var_1355", dtype = "float32", shape = (13, 15, 3))#candidate|1355|(13, 15, 3)|var|float32
uop_1356 = relay.sin(var_1355.astype('float32')) # shape=(13, 15, 3)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_1359 = relay.TupleGetItem(func_634_call(), 0)
call_1360 = relay.TupleGetItem(func_636_call(), 0)
output = relay.Tuple([uop_1356,call_1359,])
output2 = relay.Tuple([uop_1356,call_1360,])
func_1369 = relay.Function([var_1355,], output)
mod['func_1369'] = func_1369
mod = relay.transform.InferType()(mod)
mutated_mod['func_1369'] = func_1369
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1370 = relay.var("var_1370", dtype = "float32", shape = (13, 15, 3))#candidate|1370|(13, 15, 3)|var|float32
func_1369_call = mutated_mod.get_global_var('func_1369')
call_1371 = func_1369_call(var_1370)
output = call_1371
func_1372 = relay.Function([var_1370], output)
mutated_mod['func_1372'] = func_1372
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1374 = relay.var("var_1374", dtype = "float32", shape = (3, 8, 13))#candidate|1374|(3, 8, 13)|var|float32
uop_1375 = relay.atanh(var_1374.astype('float32')) # shape=(3, 8, 13)
output = uop_1375
output2 = uop_1375
func_1380 = relay.Function([var_1374,], output)
mod['func_1380'] = func_1380
mod = relay.transform.InferType()(mod)
var_1381 = relay.var("var_1381", dtype = "float32", shape = (3, 8, 13))#candidate|1381|(3, 8, 13)|var|float32
output = func_1380(var_1381)
func_1382 = relay.Function([var_1381], output)
mutated_mod['func_1382'] = func_1382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1392 = relay.var("var_1392", dtype = "float32", shape = (9, 9, 12))#candidate|1392|(9, 9, 12)|var|float32
uop_1393 = relay.asin(var_1392.astype('float32')) # shape=(9, 9, 12)
bop_1417 = relay.multiply(uop_1393.astype('uint32'), relay.reshape(var_1392.astype('uint32'), relay.shape_of(uop_1393))) # shape=(9, 9, 12)
output = relay.Tuple([bop_1417,])
output2 = relay.Tuple([bop_1417,])
func_1421 = relay.Function([var_1392,], output)
mod['func_1421'] = func_1421
mod = relay.transform.InferType()(mod)
var_1422 = relay.var("var_1422", dtype = "float32", shape = (9, 9, 12))#candidate|1422|(9, 9, 12)|var|float32
output = func_1421(var_1422)
func_1423 = relay.Function([var_1422], output)
mutated_mod['func_1423'] = func_1423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_1430 = func_294_call()
call_1431 = func_294_call()
output = call_1430
output2 = call_1431
func_1440 = relay.Function([], output)
mod['func_1440'] = func_1440
mod = relay.transform.InferType()(mod)
mutated_mod['func_1440'] = func_1440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1440_call = mutated_mod.get_global_var('func_1440')
call_1441 = func_1440_call()
output = call_1441
func_1442 = relay.Function([], output)
mutated_mod['func_1442'] = func_1442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1440_call = mod.get_global_var('func_1440')
func_1442_call = mutated_mod.get_global_var('func_1442')
call_1562 = func_1440_call()
call_1563 = func_1440_call()
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_1565 = relay.TupleGetItem(func_876_call(), 0)
call_1566 = relay.TupleGetItem(func_878_call(), 0)
func_1018_call = mod.get_global_var('func_1018')
func_1021_call = mutated_mod.get_global_var('func_1021')
const_1570 = relay.const([-4,1,-4,5,-2,2,3,-9,-5,-2,-6,-5,-10,10,-8,5,10,1,-2,-3,-3,8,-7,3,-1,1,1,-2,6,10,-9,-5,2,-4,-2,7,-2,-1,5,-10,-10,2,10,10,-6,-1,7,5,-4,4,-3,-1,-9,5,8,-8,8,-10,4,4,4,6,-1,-3,-9,1,9,9,8,-1,9,7,-1,-8,10,-6,7,-6,-4,-7,5,3,2,3,5,-8,-3,-2], dtype = "int32")#candidate|1570|(88,)|const|int32
const_1571 = relay.const([9,1,-8,1,1,4,-6,-6,4,-2,1,8,2,6,8,-5,5,-6,8,-8,1,-7,-10,8,4,-10,7,-4,-1,-4,-2,-8,7,-1,-9,4,-2,9,-5,-7,-6,3,4,4,-8,4,9,6,-6,-9,-7,-7,3,2,-10,6,-3,-9,6,2,-2,-5,-10,7,9,1,8,-6,1,-10,6,-6,6,-8,9,-8,8,-1,4,2,-5,-9,10,-5,-5,3,4,-2,5,5,-2,6,-4,-8,-7,4,-5,5,10,6,9,-9,-9,3,3,-9,-1,-6,-3,7,-5,2,-4,5,10,-1,1,2,-3,5,7,10,8,-4,10,-1,-2,5,3,-2,-3,2,3,5,2,-1,-5,-6,-8,-6,-4,5,1,2,10,-6,4,-9,3,2,-6,-4,-5,6,3,-4,-8,-2,9,-2,7,3,6,-10,-6,6,-7,-2,3,6,9,-4,8,-5,-2,-5,-7,-10,-10,3,3,9,2,-2,1,-4,9,7,-5,-4,1,6,8,2,6,-6,-7,-9,-6,5,-1,6,-8,-9,5,-2,5,-4,-5,10,2,-2,-1,-7,6,-2,2,10,3,2,3,4,-3,-2,5,-2,10,-7,9,-5,7,-3,-7,6,10,-8,2,-4,2,-5,-8,5,3,6,-5,6,-10,8,9,9,-4,6,-1,-2,4,10,-4,-7,-7,8,6,2,2,5,-6,3,-3,5,-9,9,-4,-5,-3,3,7,-2,5,1,5,-7,2,2,-8,1,4,1,8,6,10,5,-1,2,-10,1,9,-10,-9,6,9,-9,7,3,-7,1,8,-7,-3,-5,2,-2,-6,-1,3,6,-7,7,4,3,6,-9,10,-3,4,7,4,8,10,-6,-7,6,-5,9,-10,-1,6,3,7,-10,2,9,-7,-5,-6,-1,-3,-8,10,10,-8,8,-2,-2,7,-1,9,4,-7,-6,-1,-6,6,5,-1,-7,7,-3,-8,-9,6,3,-2,-3,7,-1,-6,3,3,9,-2,-3,4,7,2,9,7,-5,-1,7,-8,8,-7,8,-6,6,-3,-6,-6,1,10,7,-3,8,9,-4,6,-2,3,-5,-7,9,-1,-7,10,6,-9,9,3,10,3,-10,-5,1,2,-9,8,-9,2,5,-5,4,-4,-9,-10,-9,-2,3,-3,5,2,-6,-1,1,-2,-7,-7,-4,6,8,-2,-1,7,-2,-8,-10,1,3,1,-7,-10,2,5,-10,9,7,4,4,1,4,2,-4,-7,7,10,-3,-8,10,10,6,-8,1,-10,3,-10,5,-8,7,3,-5,9,5,-4,-3,-7,-6,-2,6,3,-5,6,-6,-6,-10,-10,6,-5,-7,8,-5,-8,9,-9,4,-4,-6,-9,-5,-7,6,9,7,2,5,5,-6,-5,7,-2,6,7,8,-4,3,-7,-1,10,2,-3,4,1,2,-5,-9,-9,-2,-9,-4,-3,-8,-5,-9,-6,-9,-10,-6,-2,-6,-7,-3,2,-5,-8,-5,6,-1,2,-8,-3,-5,9,-5,-2,-8,-5,-7,8,1,-9,-7,10,5,-10,-10,9,5,9,-1,-10,-1,-1,4,-10,-7,3,-3,-4,7,-3,-6,-4,-2,-10,5,-3,-4,5,-8,-5,4,-9,-1,9,-6,4,-5,-2,3,-2,-1,-5,3,-5,2,6,-7,7,7,-7,8,-4,2,-2,7,3,10,2,-7,6,6,7,6,-3,-10,7,-2,1,-8,-10,6,2,-3,-1,9,2,-9,1,5,-10,2,10,-8,-1,1,-1,9,5,8,-4,3,-2,-7,8,7,-4,5,5,5,2,-1,5,6,2,7,-1,-2,-5,-8,-10,10,3,9,1,-8,-2,-7,7,-8,-7,4,7,5,-6,2,-7,9,-10,-10,2,7,6,-10,7,-3,3,4,-5,10,1,7,-8,8,7,-2,-7,-3,-1,8,-3,4,-8,5,-9,-7,1,-8,4,-9,-7,10,-8,-9,-7,8,-7,5,-3,1,7,4,-3,7,10,8,6,1,2,6,-6,1,-9,9,9,5,9,6,-2,7,2,9,-3,4,10,-7,8,-2,-6,-10,2,-5,-5,-10,5,-8,5,4,8,5,2,6,4,7,-10,7,4,-2,-4,-7,2,-7,-3,-4,1,-10,-5,-4,-6,-9,10,8,-9,-3,1,-3,3,9,-10,-8,-6,5,9,-8,-10,9,2,-2,-6,-5,4,1,5,5,6,-6,6,-4,1,-7,-9,-3,-6,6,-1,-2,-7,2,6,7,5,-4,5,5,10,-10,-10,3,-7,9,-8,-3,-5,-6,6,-1,-5,1,5,-9,-10,5,10,-8,-5,-7,10,-7,-4,-6,-6,-1,-3,2], dtype = "int32")#candidate|1571|(880,)|const|int32
call_1569 = func_1018_call(relay.reshape(const_1570.astype('int32'), [11, 1, 8]), relay.reshape(const_1571.astype('int32'), [11, 10, 8]), )
call_1572 = func_1018_call(relay.reshape(const_1570.astype('int32'), [11, 1, 8]), relay.reshape(const_1571.astype('int32'), [11, 10, 8]), )
output = relay.Tuple([call_1562,call_1565,call_1569,const_1570,const_1571,])
output2 = relay.Tuple([call_1563,call_1566,call_1572,const_1570,const_1571,])
func_1580 = relay.Function([], output)
mod['func_1580'] = func_1580
mod = relay.transform.InferType()(mod)
output = func_1580()
func_1581 = relay.Function([], output)
mutated_mod['func_1581'] = func_1581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_1584 = func_331_call()
call_1585 = func_331_call()
output = call_1584
output2 = call_1585
func_1586 = relay.Function([], output)
mod['func_1586'] = func_1586
mod = relay.transform.InferType()(mod)
mutated_mod['func_1586'] = func_1586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1586_call = mutated_mod.get_global_var('func_1586')
call_1587 = func_1586_call()
output = call_1587
func_1588 = relay.Function([], output)
mutated_mod['func_1588'] = func_1588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_1710 = relay.TupleGetItem(func_634_call(), 0)
call_1711 = relay.TupleGetItem(func_636_call(), 0)
func_246_call = mod.get_global_var('func_246')
func_250_call = mutated_mod.get_global_var('func_250')
var_1724 = relay.var("var_1724", dtype = "int64", shape = (336,))#candidate|1724|(336,)|var|int64
call_1723 = relay.TupleGetItem(func_246_call(relay.reshape(var_1724.astype('int64'), [12, 4, 7]), relay.reshape(var_1724.astype('int64'), [12, 4, 7]), relay.reshape(var_1724.astype('float32'), [12, 4, 7]), ), 2)
call_1725 = relay.TupleGetItem(func_250_call(relay.reshape(var_1724.astype('int64'), [12, 4, 7]), relay.reshape(var_1724.astype('int64'), [12, 4, 7]), relay.reshape(var_1724.astype('float32'), [12, 4, 7]), ), 2)
func_479_call = mod.get_global_var('func_479')
func_480_call = mutated_mod.get_global_var('func_480')
call_1733 = relay.TupleGetItem(func_479_call(), 0)
call_1734 = relay.TupleGetItem(func_480_call(), 0)
func_1380_call = mod.get_global_var('func_1380')
func_1382_call = mutated_mod.get_global_var('func_1382')
var_1761 = relay.var("var_1761", dtype = "float32", shape = (1, 312))#candidate|1761|(1, 312)|var|float32
call_1760 = func_1380_call(relay.reshape(var_1761.astype('float32'), [3, 8, 13]))
call_1762 = func_1380_call(relay.reshape(var_1761.astype('float32'), [3, 8, 13]))
output = relay.Tuple([call_1710,call_1723,var_1724,call_1733,call_1760,var_1761,])
output2 = relay.Tuple([call_1711,call_1725,var_1724,call_1734,call_1762,var_1761,])
func_1771 = relay.Function([var_1724,var_1761,], output)
mod['func_1771'] = func_1771
mod = relay.transform.InferType()(mod)
var_1772 = relay.var("var_1772", dtype = "int64", shape = (336,))#candidate|1772|(336,)|var|int64
var_1773 = relay.var("var_1773", dtype = "float32", shape = (1, 312))#candidate|1773|(1, 312)|var|float32
output = func_1771(var_1772,var_1773,)
func_1774 = relay.Function([var_1772,var_1773,], output)
mutated_mod['func_1774'] = func_1774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_1776 = func_331_call()
call_1777 = func_331_call()
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_1778 = relay.TupleGetItem(func_534_call(), 1)
call_1779 = relay.TupleGetItem(func_536_call(), 1)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
const_1797 = relay.const([[-2.735550,-8.286780,-5.396855,3.898902,8.004294,0.844012,5.684060,-3.379035],[-9.969448,-1.200126,9.500744,-1.281913,7.989215,-1.206143,1.166145,-6.497042],[8.792360,6.694996,1.129065,4.214778,-1.993145,-6.492850,4.062130,-0.971640],[-2.780916,5.433256,-5.422993,-7.882360,8.808150,0.982582,4.655311,7.812539]], dtype = "float64")#candidate|1797|(4, 8)|const|float64
call_1796 = func_655_call(relay.reshape(const_1797.astype('float64'), [16, 2]))
call_1798 = func_655_call(relay.reshape(const_1797.astype('float64'), [16, 2]))
func_978_call = mod.get_global_var('func_978')
func_980_call = mutated_mod.get_global_var('func_980')
call_1807 = relay.TupleGetItem(func_978_call(), 3)
call_1808 = relay.TupleGetItem(func_980_call(), 3)
output = relay.Tuple([call_1776,call_1778,call_1796,const_1797,call_1807,])
output2 = relay.Tuple([call_1777,call_1779,call_1798,const_1797,call_1808,])
func_1818 = relay.Function([], output)
mod['func_1818'] = func_1818
mod = relay.transform.InferType()(mod)
mutated_mod['func_1818'] = func_1818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1818_call = mutated_mod.get_global_var('func_1818')
call_1819 = func_1818_call()
output = call_1819
func_1820 = relay.Function([], output)
mutated_mod['func_1820'] = func_1820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_331_call = mod.get_global_var('func_331')
func_333_call = mutated_mod.get_global_var('func_333')
call_1852 = func_331_call()
call_1853 = func_331_call()
output = relay.Tuple([call_1852,])
output2 = relay.Tuple([call_1853,])
func_1871 = relay.Function([], output)
mod['func_1871'] = func_1871
mod = relay.transform.InferType()(mod)
output = func_1871()
func_1872 = relay.Function([], output)
mutated_mod['func_1872'] = func_1872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1818_call = mod.get_global_var('func_1818')
func_1820_call = mutated_mod.get_global_var('func_1820')
call_1880 = relay.TupleGetItem(func_1818_call(), 4)
call_1881 = relay.TupleGetItem(func_1820_call(), 4)
output = relay.Tuple([call_1880,])
output2 = relay.Tuple([call_1881,])
func_1889 = relay.Function([], output)
mod['func_1889'] = func_1889
mod = relay.transform.InferType()(mod)
mutated_mod['func_1889'] = func_1889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mutated_mod.get_global_var('func_1889')
call_1890 = func_1889_call()
output = call_1890
func_1891 = relay.Function([], output)
mutated_mod['func_1891'] = func_1891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_480_call = mutated_mod.get_global_var('func_480')
call_1946 = relay.TupleGetItem(func_479_call(), 2)
call_1947 = relay.TupleGetItem(func_480_call(), 2)
output = relay.Tuple([call_1946,])
output2 = relay.Tuple([call_1947,])
func_1951 = relay.Function([], output)
mod['func_1951'] = func_1951
mod = relay.transform.InferType()(mod)
output = func_1951()
func_1952 = relay.Function([], output)
mutated_mod['func_1952'] = func_1952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1271_call = mod.get_global_var('func_1271')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_1971 = relay.TupleGetItem(func_1271_call(), 1)
call_1972 = relay.TupleGetItem(func_1272_call(), 1)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
var_1978 = relay.var("var_1978", dtype = "float64", shape = (32,))#candidate|1978|(32,)|var|float64
call_1977 = func_655_call(relay.reshape(var_1978.astype('float64'), [16, 2]))
call_1979 = func_655_call(relay.reshape(var_1978.astype('float64'), [16, 2]))
func_1150_call = mod.get_global_var('func_1150')
func_1152_call = mutated_mod.get_global_var('func_1152')
call_1983 = relay.TupleGetItem(func_1150_call(), 4)
call_1984 = relay.TupleGetItem(func_1152_call(), 4)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
call_1988 = relay.TupleGetItem(func_435_call(relay.reshape(call_1983.astype('float32'), [14, 6, 16]), relay.reshape(call_1983.astype('float32'), [14, 6, 16]), ), 0)
call_1989 = relay.TupleGetItem(func_438_call(relay.reshape(call_1983.astype('float32'), [14, 6, 16]), relay.reshape(call_1983.astype('float32'), [14, 6, 16]), ), 0)
output = relay.Tuple([call_1971,call_1977,var_1978,call_1983,call_1988,])
output2 = relay.Tuple([call_1972,call_1979,var_1978,call_1984,call_1989,])
func_1990 = relay.Function([var_1978,], output)
mod['func_1990'] = func_1990
mod = relay.transform.InferType()(mod)
mutated_mod['func_1990'] = func_1990
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1991 = relay.var("var_1991", dtype = "float64", shape = (32,))#candidate|1991|(32,)|var|float64
func_1990_call = mutated_mod.get_global_var('func_1990')
call_1992 = func_1990_call(var_1991)
output = call_1992
func_1993 = relay.Function([var_1991], output)
mutated_mod['func_1993'] = func_1993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1581_call = mutated_mod.get_global_var('func_1581')
call_1998 = relay.TupleGetItem(func_1580_call(), 0)
call_1999 = relay.TupleGetItem(func_1581_call(), 0)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
var_2004 = relay.var("var_2004", dtype = "int32", shape = (88,))#candidate|2004|(88,)|var|int32
call_2003 = relay.TupleGetItem(func_1055_call(relay.reshape(var_2004.astype('int32'), [88,])), 4)
call_2005 = relay.TupleGetItem(func_1058_call(relay.reshape(var_2004.astype('int32'), [88,])), 4)
output = relay.Tuple([call_1998,call_2003,var_2004,])
output2 = relay.Tuple([call_1999,call_2005,var_2004,])
func_2006 = relay.Function([var_2004,], output)
mod['func_2006'] = func_2006
mod = relay.transform.InferType()(mod)
var_2007 = relay.var("var_2007", dtype = "int32", shape = (88,))#candidate|2007|(88,)|var|int32
output = func_2006(var_2007)
func_2008 = relay.Function([var_2007], output)
mutated_mod['func_2008'] = func_2008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_2024 = relay.TupleGetItem(func_634_call(), 0)
call_2025 = relay.TupleGetItem(func_636_call(), 0)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
call_2041 = relay.TupleGetItem(func_435_call(relay.reshape(call_2024.astype('float32'), [14, 6, 16]), relay.reshape(call_2024.astype('float32'), [14, 6, 16]), ), 3)
call_2042 = relay.TupleGetItem(func_438_call(relay.reshape(call_2024.astype('float32'), [14, 6, 16]), relay.reshape(call_2024.astype('float32'), [14, 6, 16]), ), 3)
output = relay.Tuple([call_2024,call_2041,])
output2 = relay.Tuple([call_2025,call_2042,])
func_2044 = relay.Function([], output)
mod['func_2044'] = func_2044
mod = relay.transform.InferType()(mod)
output = func_2044()
func_2045 = relay.Function([], output)
mutated_mod['func_2045'] = func_2045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_2094 = relay.TupleGetItem(func_534_call(), 1)
call_2095 = relay.TupleGetItem(func_536_call(), 1)
output = call_2094
output2 = call_2095
func_2096 = relay.Function([], output)
mod['func_2096'] = func_2096
mod = relay.transform.InferType()(mod)
mutated_mod['func_2096'] = func_2096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mutated_mod.get_global_var('func_2096')
call_2097 = func_2096_call()
output = call_2097
func_2098 = relay.Function([], output)
mutated_mod['func_2098'] = func_2098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_978_call = mod.get_global_var('func_978')
func_980_call = mutated_mod.get_global_var('func_980')
call_2108 = relay.TupleGetItem(func_978_call(), 0)
call_2109 = relay.TupleGetItem(func_980_call(), 0)
output = call_2108
output2 = call_2109
func_2125 = relay.Function([], output)
mod['func_2125'] = func_2125
mod = relay.transform.InferType()(mod)
mutated_mod['func_2125'] = func_2125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2125_call = mutated_mod.get_global_var('func_2125')
call_2126 = func_2125_call()
output = call_2126
func_2127 = relay.Function([], output)
mutated_mod['func_2127'] = func_2127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_2137 = func_294_call()
call_2138 = func_294_call()
func_1150_call = mod.get_global_var('func_1150')
func_1152_call = mutated_mod.get_global_var('func_1152')
call_2144 = relay.TupleGetItem(func_1150_call(), 2)
call_2145 = relay.TupleGetItem(func_1152_call(), 2)
output = relay.Tuple([call_2137,call_2144,])
output2 = relay.Tuple([call_2138,call_2145,])
func_2153 = relay.Function([], output)
mod['func_2153'] = func_2153
mod = relay.transform.InferType()(mod)
mutated_mod['func_2153'] = func_2153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mutated_mod.get_global_var('func_2153')
call_2154 = func_2153_call()
output = call_2154
func_2155 = relay.Function([], output)
mutated_mod['func_2155'] = func_2155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_978_call = mod.get_global_var('func_978')
func_980_call = mutated_mod.get_global_var('func_980')
call_2234 = relay.TupleGetItem(func_978_call(), 0)
call_2235 = relay.TupleGetItem(func_980_call(), 0)
uop_2238 = relay.asinh(call_2234.astype('float32')) # shape=(14, 6, 16)
uop_2240 = relay.asinh(call_2235.astype('float32')) # shape=(14, 6, 16)
func_834_call = mod.get_global_var('func_834')
func_835_call = mutated_mod.get_global_var('func_835')
call_2242 = func_834_call()
call_2243 = func_834_call()
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
call_2246 = relay.TupleGetItem(func_435_call(relay.reshape(call_2242.astype('float32'), [14, 6, 16]), relay.reshape(uop_2238.astype('float32'), [14, 6, 16]), ), 0)
call_2247 = relay.TupleGetItem(func_438_call(relay.reshape(call_2242.astype('float32'), [14, 6, 16]), relay.reshape(uop_2238.astype('float32'), [14, 6, 16]), ), 0)
output = relay.Tuple([uop_2238,call_2242,call_2246,])
output2 = relay.Tuple([uop_2240,call_2243,call_2247,])
func_2271 = relay.Function([], output)
mod['func_2271'] = func_2271
mod = relay.transform.InferType()(mod)
mutated_mod['func_2271'] = func_2271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mutated_mod.get_global_var('func_2271')
call_2272 = func_2271_call()
output = call_2272
func_2273 = relay.Function([], output)
mutated_mod['func_2273'] = func_2273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_2285 = relay.TupleGetItem(func_2271_call(), 1)
call_2286 = relay.TupleGetItem(func_2273_call(), 1)
output = call_2285
output2 = call_2286
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
var_2411 = relay.var("var_2411", dtype = "float64", shape = (8, 2, 1))#candidate|2411|(8, 2, 1)|var|float64
uop_2412 = relay.log(var_2411.astype('float64')) # shape=(8, 2, 1)
output = relay.Tuple([uop_2412,])
output2 = relay.Tuple([uop_2412,])
func_2440 = relay.Function([var_2411,], output)
mod['func_2440'] = func_2440
mod = relay.transform.InferType()(mod)
mutated_mod['func_2440'] = func_2440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2441 = relay.var("var_2441", dtype = "float64", shape = (8, 2, 1))#candidate|2441|(8, 2, 1)|var|float64
func_2440_call = mutated_mod.get_global_var('func_2440')
call_2442 = func_2440_call(var_2441)
output = call_2442
func_2443 = relay.Function([var_2441], output)
mutated_mod['func_2443'] = func_2443
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2485 = relay.var("var_2485", dtype = "float64", shape = (2, 11, 5))#candidate|2485|(2, 11, 5)|var|float64
uop_2486 = relay.log2(var_2485.astype('float64')) # shape=(2, 11, 5)
uop_2488 = relay.sqrt(uop_2486.astype('float32')) # shape=(2, 11, 5)
output = relay.Tuple([uop_2488,])
output2 = relay.Tuple([uop_2488,])
func_2506 = relay.Function([var_2485,], output)
mod['func_2506'] = func_2506
mod = relay.transform.InferType()(mod)
mutated_mod['func_2506'] = func_2506
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2507 = relay.var("var_2507", dtype = "float64", shape = (2, 11, 5))#candidate|2507|(2, 11, 5)|var|float64
func_2506_call = mutated_mod.get_global_var('func_2506')
call_2508 = func_2506_call(var_2507)
output = call_2508
func_2509 = relay.Function([var_2507], output)
mutated_mod['func_2509'] = func_2509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1581_call = mutated_mod.get_global_var('func_1581')
call_2524 = relay.TupleGetItem(func_1580_call(), 4)
call_2525 = relay.TupleGetItem(func_1581_call(), 4)
output = relay.Tuple([call_2524,])
output2 = relay.Tuple([call_2525,])
func_2533 = relay.Function([], output)
mod['func_2533'] = func_2533
mod = relay.transform.InferType()(mod)
output = func_2533()
func_2534 = relay.Function([], output)
mutated_mod['func_2534'] = func_2534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_2568 = relay.TupleGetItem(func_2271_call(), 2)
call_2569 = relay.TupleGetItem(func_2273_call(), 2)
func_2044_call = mod.get_global_var('func_2044')
func_2045_call = mutated_mod.get_global_var('func_2045')
call_2580 = relay.TupleGetItem(func_2044_call(), 0)
call_2581 = relay.TupleGetItem(func_2045_call(), 0)
func_2506_call = mod.get_global_var('func_2506')
func_2509_call = mutated_mod.get_global_var('func_2509')
const_2597 = relay.const([[-3.106969],[-7.934264],[-4.881398],[-5.095429],[4.703877],[-6.971043],[6.476743],[-8.436162],[1.835069],[0.617991],[0.873699],[-9.791628],[5.791226],[-3.446073],[9.671173],[-7.842459],[-1.159300],[-1.489885],[-8.082951],[-3.996983],[-4.290983],[-3.562078],[-9.501385],[2.700836],[2.511533],[-8.296157],[4.828544],[-8.576368],[-3.547516],[-5.663474],[8.630411],[3.308938],[-9.815004],[9.379219],[1.064835],[-7.983914],[-5.772935],[8.500160],[3.716739],[-7.814507],[1.686507],[-4.517347],[-5.212751],[4.863333],[8.673890],[-7.972521],[2.298405],[-2.733647],[5.659544],[-7.616456],[-1.134383],[3.894749],[6.206498],[2.128337],[3.881201],[3.037868],[-6.485705],[5.255459],[8.403513],[-5.284394],[5.352018],[4.153028],[-8.339679],[-9.206597],[1.869000],[-6.548961],[6.833871],[2.890622],[-3.874233],[-2.449471],[-1.270793],[-0.167151],[6.604179],[9.366935],[0.422973],[3.137264],[8.724546],[3.213276],[9.758954],[5.944913],[-7.491556],[-3.226280],[8.009686],[7.042666],[-3.842548],[-5.812769],[1.954302],[8.491449],[-3.624048],[0.261803],[-7.917909],[-7.842055],[-7.319003],[-2.290331],[1.932098],[-6.750634],[6.161353],[-8.281024],[-2.115910],[7.776236],[0.818535],[-7.549974],[-9.613511],[7.635467],[-7.207787],[-9.601088],[0.131891],[-8.239733],[-6.733707],[1.138519]], dtype = "float64")#candidate|2597|(110, 1)|const|float64
call_2596 = relay.TupleGetItem(func_2506_call(relay.reshape(const_2597.astype('float64'), [2, 11, 5])), 0)
call_2598 = relay.TupleGetItem(func_2509_call(relay.reshape(const_2597.astype('float64'), [2, 11, 5])), 0)
output = relay.Tuple([call_2568,call_2580,call_2596,const_2597,])
output2 = relay.Tuple([call_2569,call_2581,call_2598,const_2597,])
func_2606 = relay.Function([], output)
mod['func_2606'] = func_2606
mod = relay.transform.InferType()(mod)
mutated_mod['func_2606'] = func_2606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2606_call = mutated_mod.get_global_var('func_2606')
call_2607 = func_2606_call()
output = call_2607
func_2608 = relay.Function([], output)
mutated_mod['func_2608'] = func_2608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_2632 = relay.TupleGetItem(func_2153_call(), 0)
call_2633 = relay.TupleGetItem(func_2155_call(), 0)
var_2636 = relay.var("var_2636", dtype = "float32", shape = (14, 6, 16))#candidate|2636|(14, 6, 16)|var|float32
bop_2637 = relay.left_shift(call_2632.astype('uint16'), relay.reshape(var_2636.astype('uint16'), relay.shape_of(call_2632))) # shape=(14, 6, 16)
bop_2640 = relay.left_shift(call_2633.astype('uint16'), relay.reshape(var_2636.astype('uint16'), relay.shape_of(call_2633))) # shape=(14, 6, 16)
func_1889_call = mod.get_global_var('func_1889')
func_1891_call = mutated_mod.get_global_var('func_1891')
call_2647 = relay.TupleGetItem(func_1889_call(), 0)
call_2648 = relay.TupleGetItem(func_1891_call(), 0)
func_730_call = mod.get_global_var('func_730')
func_733_call = mutated_mod.get_global_var('func_733')
call_2649 = relay.TupleGetItem(func_730_call(relay.reshape(call_2632.astype('float32'), [14, 6, 16])), 1)
call_2650 = relay.TupleGetItem(func_733_call(relay.reshape(call_2632.astype('float32'), [14, 6, 16])), 1)
output = relay.Tuple([bop_2637,call_2647,call_2649,])
output2 = relay.Tuple([bop_2640,call_2648,call_2650,])
func_2654 = relay.Function([var_2636,], output)
mod['func_2654'] = func_2654
mod = relay.transform.InferType()(mod)
mutated_mod['func_2654'] = func_2654
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2655 = relay.var("var_2655", dtype = "float32", shape = (14, 6, 16))#candidate|2655|(14, 6, 16)|var|float32
func_2654_call = mutated_mod.get_global_var('func_2654')
call_2656 = func_2654_call(var_2655)
output = call_2656
func_2657 = relay.Function([var_2655], output)
mutated_mod['func_2657'] = func_2657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1586_call = mod.get_global_var('func_1586')
func_1588_call = mutated_mod.get_global_var('func_1588')
call_2734 = func_1586_call()
call_2735 = func_1586_call()
output = relay.Tuple([call_2734,])
output2 = relay.Tuple([call_2735,])
func_2781 = relay.Function([], output)
mod['func_2781'] = func_2781
mod = relay.transform.InferType()(mod)
mutated_mod['func_2781'] = func_2781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mutated_mod.get_global_var('func_2781')
call_2782 = func_2781_call()
output = call_2782
func_2783 = relay.Function([], output)
mutated_mod['func_2783'] = func_2783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_480_call = mutated_mod.get_global_var('func_480')
call_2811 = relay.TupleGetItem(func_479_call(), 0)
call_2812 = relay.TupleGetItem(func_480_call(), 0)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_2829 = relay.TupleGetItem(func_534_call(), 0)
call_2830 = relay.TupleGetItem(func_536_call(), 0)
output = relay.Tuple([call_2811,call_2829,])
output2 = relay.Tuple([call_2812,call_2830,])
func_2848 = relay.Function([], output)
mod['func_2848'] = func_2848
mod = relay.transform.InferType()(mod)
mutated_mod['func_2848'] = func_2848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mutated_mod.get_global_var('func_2848')
call_2849 = func_2848_call()
output = call_2849
func_2850 = relay.Function([], output)
mutated_mod['func_2850'] = func_2850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mod.get_global_var('func_2781')
func_2783_call = mutated_mod.get_global_var('func_2783')
call_2875 = relay.TupleGetItem(func_2781_call(), 0)
call_2876 = relay.TupleGetItem(func_2783_call(), 0)
output = relay.Tuple([call_2875,])
output2 = relay.Tuple([call_2876,])
func_2885 = relay.Function([], output)
mod['func_2885'] = func_2885
mod = relay.transform.InferType()(mod)
output = func_2885()
func_2886 = relay.Function([], output)
mutated_mod['func_2886'] = func_2886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_2929 = relay.TupleGetItem(func_1232_call(), 0)
call_2930 = relay.TupleGetItem(func_1233_call(), 0)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
const_2948 = relay.const([10,-4,-1,3,-6,-1,4,-2,2,-3,-5,-4,6,9,9,4,7,8,-9,-8,-9,-7,2,10,-7,9,-8,10,-8,2,8,-9,-5,7,-2,-8,5,6,7,3,8,9,-6,-2,8,2,-1,5,1,-2,6,-4,5,10,5,-9,5,9,-7,-4,6,-10,-10,-4,6,4,6,-5,-7,5,8,6,-2,-3,-7,-1,-6,1,8,6,1,-6,-7,8,-5,7,8,7], dtype = "int32")#candidate|2948|(88,)|const|int32
call_2947 = relay.TupleGetItem(func_1055_call(relay.reshape(const_2948.astype('int32'), [88,])), 4)
call_2949 = relay.TupleGetItem(func_1058_call(relay.reshape(const_2948.astype('int32'), [88,])), 4)
var_2950 = relay.var("var_2950", dtype = "int32", shape = (880,))#candidate|2950|(880,)|var|int32
bop_2951 = relay.divide(call_2947.astype('float64'), relay.reshape(var_2950.astype('float64'), relay.shape_of(call_2947))) # shape=(880,)
bop_2954 = relay.divide(call_2949.astype('float64'), relay.reshape(var_2950.astype('float64'), relay.shape_of(call_2949))) # shape=(880,)
output = relay.Tuple([call_2929,const_2948,bop_2951,])
output2 = relay.Tuple([call_2930,const_2948,bop_2954,])
func_2955 = relay.Function([var_2950,], output)
mod['func_2955'] = func_2955
mod = relay.transform.InferType()(mod)
var_2956 = relay.var("var_2956", dtype = "int32", shape = (880,))#candidate|2956|(880,)|var|int32
output = func_2955(var_2956)
func_2957 = relay.Function([var_2956], output)
mutated_mod['func_2957'] = func_2957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_2981 = relay.TupleGetItem(func_2153_call(), 1)
call_2982 = relay.TupleGetItem(func_2155_call(), 1)
func_1150_call = mod.get_global_var('func_1150')
func_1152_call = mutated_mod.get_global_var('func_1152')
call_3020 = relay.TupleGetItem(func_1150_call(), 1)
call_3021 = relay.TupleGetItem(func_1152_call(), 1)
func_2781_call = mod.get_global_var('func_2781')
func_2783_call = mutated_mod.get_global_var('func_2783')
call_3043 = relay.TupleGetItem(func_2781_call(), 0)
call_3044 = relay.TupleGetItem(func_2783_call(), 0)
output = relay.Tuple([call_2981,call_3020,call_3043,])
output2 = relay.Tuple([call_2982,call_3021,call_3044,])
func_3045 = relay.Function([], output)
mod['func_3045'] = func_3045
mod = relay.transform.InferType()(mod)
mutated_mod['func_3045'] = func_3045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3045_call = mutated_mod.get_global_var('func_3045')
call_3046 = func_3045_call()
output = call_3046
func_3047 = relay.Function([], output)
mutated_mod['func_3047'] = func_3047
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3096 = relay.var("var_3096", dtype = "uint16", shape = (5, 14, 1))#candidate|3096|(5, 14, 1)|var|uint16
const_3097 = relay.const([[[-2,10,4,1,7],[1,-8,5,5,-4],[-2,9,9,-6,-3],[-6,3,10,5,1],[-9,-8,-3,10,-6],[9,3,10,5,6],[-9,10,-8,9,-4],[-9,-5,10,9,8],[-6,-7,-4,-3,-5],[5,-3,5,-7,-9],[7,6,3,1,-7],[1,-3,-4,-5,6],[-10,-3,-7,-8,-5],[7,-3,5,10,9]],[[-3,5,-9,5,-10],[2,-3,4,-3,8],[7,9,10,-5,-10],[-2,-5,2,-5,-7],[-9,4,-4,-6,9],[5,1,6,-10,4],[7,6,10,-5,-5],[10,1,-8,2,-2],[-9,-9,-2,10,7],[-3,-9,-6,7,3],[-4,-5,-9,-2,10],[4,-10,8,9,4],[-3,10,-8,-10,-8],[6,-8,-8,8,9]],[[-1,-5,-5,5,-2],[-10,7,-8,4,9],[-1,-5,6,7,3],[-1,-9,7,1,8],[10,2,-7,4,8],[-7,-8,9,4,-9],[-2,-1,-7,4,10],[-3,1,-10,4,2],[-7,1,1,-1,-6],[4,-9,8,5,5],[-4,-10,4,3,-5],[-9,6,-8,-2,4],[9,7,-2,5,-4],[7,-9,-1,6,-10]],[[-3,-3,-3,-5,-10],[-2,-6,-7,3,-8],[-2,-5,1,-1,-1],[7,-2,-2,1,-9],[-8,-2,-1,5,-10],[-10,-9,1,-10,8],[-5,-7,5,-9,9],[-9,-8,-3,7,2],[-4,-2,-5,4,5],[-9,7,7,-5,8],[4,-3,6,3,6],[3,-8,-5,-7,-10],[-9,5,5,7,8],[-4,-3,-7,6,4]],[[-7,-4,-3,-8,5],[5,7,1,-1,1],[-6,-2,-5,7,8],[3,-10,8,3,-4],[-6,-4,10,-6,-6],[8,4,-10,-6,-10],[10,-10,8,4,8],[10,8,8,1,-6],[-2,8,4,-5,-5],[-7,-8,-5,-6,10],[6,7,-5,-3,10],[-3,4,8,-9,10],[-10,9,3,6,3],[-1,-7,-5,3,9]]], dtype = "uint16")#candidate|3097|(5, 14, 5)|const|uint16
bop_3098 = relay.minimum(var_3096.astype('uint16'), const_3097.astype('uint16')) # shape=(5, 14, 5)
func_2044_call = mod.get_global_var('func_2044')
func_2045_call = mutated_mod.get_global_var('func_2045')
call_3106 = relay.TupleGetItem(func_2044_call(), 1)
call_3107 = relay.TupleGetItem(func_2045_call(), 1)
bop_3111 = relay.multiply(const_3097.astype('uint32'), var_3096.astype('uint32')) # shape=(5, 14, 5)
uop_3114 = relay.acos(const_3097.astype('float64')) # shape=(5, 14, 5)
var_3117 = relay.var("var_3117", dtype = "uint16", shape = (5, 14, 15))#candidate|3117|(5, 14, 15)|var|uint16
bop_3118 = relay.bitwise_and(var_3096.astype('int16'), var_3117.astype('int16')) # shape=(5, 14, 15)
bop_3122 = relay.add(uop_3114.astype('uint16'), relay.reshape(bop_3111.astype('uint16'), relay.shape_of(uop_3114))) # shape=(5, 14, 5)
const_3129 = relay.const([[[10,-8,-3,-3,-10],[-9,-10,6,-7,-3],[-2,1,-1,-6,-10],[2,-6,10,-7,2],[8,6,6,9,10],[6,-5,7,-9,-8],[-3,9,-9,1,-4],[5,-8,-7,4,8],[1,9,4,2,8],[2,-10,-3,2,7],[8,-7,7,-1,-3],[7,6,10,10,3],[3,9,8,2,-5],[5,5,2,-7,2]],[[-3,-2,7,-6,3],[4,5,-9,5,-5],[4,-6,4,-10,-10],[-1,-5,1,-6,-8],[-6,-6,8,-6,-9],[-7,-10,2,2,7],[6,6,-10,1,4],[6,4,3,-7,6],[9,-7,-6,-7,10],[-10,-9,-6,-1,-6],[8,7,3,-3,8],[-4,-1,-9,9,5],[7,6,2,-6,2],[-10,-5,-2,6,7]],[[-5,4,-4,-4,9],[4,5,-4,5,9],[-4,-8,7,-7,7],[6,9,-9,3,7],[3,1,-5,-4,-7],[-10,6,-1,-9,-4],[6,-10,2,-7,-3],[8,-10,-5,-4,-7],[-3,-3,4,2,6],[-2,7,-7,-1,3],[-1,-1,2,5,-4],[8,-9,8,8,-9],[-5,-7,4,1,-10],[-9,-7,-3,-6,-4]],[[3,10,4,-5,8],[-7,6,-5,-7,6],[-1,8,7,9,-2],[-6,7,-6,5,-5],[7,8,-5,-4,9],[10,4,10,-1,-7],[-3,7,10,-3,5],[10,10,-5,-10,7],[-6,-9,-7,4,-9],[-1,5,-2,-1,3],[-1,-8,-10,-5,-2],[10,-1,2,10,-6],[-8,-9,6,1,-6],[-5,-7,9,-8,8]],[[7,9,6,6,7],[5,2,10,7,7],[-6,-10,7,-2,4],[-4,7,10,5,1],[1,-9,10,-1,1],[-10,-8,1,2,10],[-1,-10,10,-4,-8],[-8,1,-2,-7,9],[8,-6,-10,4,8],[9,-10,10,8,8],[-8,-7,-6,-1,-9],[-10,8,7,-2,-1],[7,-10,8,9,-3],[-2,-5,-2,-7,3]]], dtype = "uint16")#candidate|3129|(5, 14, 5)|const|uint16
bop_3130 = relay.logical_and(const_3097.astype('bool'), relay.reshape(const_3129.astype('bool'), relay.shape_of(const_3097))) # shape=(5, 14, 5)
bop_3135 = relay.floor_divide(uop_3114.astype('float32'), relay.reshape(const_3129.astype('float32'), relay.shape_of(uop_3114))) # shape=(5, 14, 5)
output = relay.Tuple([bop_3098,call_3106,bop_3118,bop_3122,bop_3130,bop_3135,])
output2 = relay.Tuple([bop_3098,call_3107,bop_3118,bop_3122,bop_3130,bop_3135,])
func_3142 = relay.Function([var_3096,var_3117,], output)
mod['func_3142'] = func_3142
mod = relay.transform.InferType()(mod)
mutated_mod['func_3142'] = func_3142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3142_call = mutated_mod.get_global_var('func_3142')
var_3144 = relay.var("var_3144", dtype = "uint16", shape = (5, 14, 1))#candidate|3144|(5, 14, 1)|var|uint16
var_3145 = relay.var("var_3145", dtype = "uint16", shape = (5, 14, 15))#candidate|3145|(5, 14, 15)|var|uint16
call_3143 = func_3142_call(var_3144,var_3145,)
output = call_3143
func_3146 = relay.Function([var_3144,var_3145,], output)
mutated_mod['func_3146'] = func_3146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_978_call = mod.get_global_var('func_978')
func_980_call = mutated_mod.get_global_var('func_980')
call_3220 = relay.TupleGetItem(func_978_call(), 0)
call_3221 = relay.TupleGetItem(func_980_call(), 0)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_3233 = func_294_call()
call_3234 = func_294_call()
func_2533_call = mod.get_global_var('func_2533')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_3236 = relay.TupleGetItem(func_2533_call(), 0)
call_3237 = relay.TupleGetItem(func_2534_call(), 0)
output = relay.Tuple([call_3220,call_3233,call_3236,])
output2 = relay.Tuple([call_3221,call_3234,call_3237,])
func_3238 = relay.Function([], output)
mod['func_3238'] = func_3238
mod = relay.transform.InferType()(mod)
output = func_3238()
func_3239 = relay.Function([], output)
mutated_mod['func_3239'] = func_3239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_3249 = relay.TupleGetItem(func_634_call(), 0)
call_3250 = relay.TupleGetItem(func_636_call(), 0)
output = relay.Tuple([call_3249,])
output2 = relay.Tuple([call_3250,])
func_3261 = relay.Function([], output)
mod['func_3261'] = func_3261
mod = relay.transform.InferType()(mod)
output = func_3261()
func_3262 = relay.Function([], output)
mutated_mod['func_3262'] = func_3262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_3266 = relay.TupleGetItem(func_2848_call(), 1)
call_3267 = relay.TupleGetItem(func_2850_call(), 1)
output = relay.Tuple([call_3266,])
output2 = relay.Tuple([call_3267,])
func_3268 = relay.Function([], output)
mod['func_3268'] = func_3268
mod = relay.transform.InferType()(mod)
output = func_3268()
func_3269 = relay.Function([], output)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1871_call = mod.get_global_var('func_1871')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_3327 = relay.TupleGetItem(func_1871_call(), 0)
call_3328 = relay.TupleGetItem(func_1872_call(), 0)
output = relay.Tuple([call_3327,])
output2 = relay.Tuple([call_3328,])
func_3331 = relay.Function([], output)
mod['func_3331'] = func_3331
mod = relay.transform.InferType()(mod)
mutated_mod['func_3331'] = func_3331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mutated_mod.get_global_var('func_3331')
call_3332 = func_3331_call()
output = call_3332
func_3333 = relay.Function([], output)
mutated_mod['func_3333'] = func_3333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_3382 = relay.TupleGetItem(func_2153_call(), 1)
call_3383 = relay.TupleGetItem(func_2155_call(), 1)
func_3238_call = mod.get_global_var('func_3238')
func_3239_call = mutated_mod.get_global_var('func_3239')
call_3389 = relay.TupleGetItem(func_3238_call(), 2)
call_3390 = relay.TupleGetItem(func_3239_call(), 2)
output = relay.Tuple([call_3382,call_3389,])
output2 = relay.Tuple([call_3383,call_3390,])
func_3444 = relay.Function([], output)
mod['func_3444'] = func_3444
mod = relay.transform.InferType()(mod)
mutated_mod['func_3444'] = func_3444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3444_call = mutated_mod.get_global_var('func_3444')
call_3445 = func_3444_call()
output = call_3445
func_3446 = relay.Function([], output)
mutated_mod['func_3446'] = func_3446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_3453 = relay.TupleGetItem(func_2271_call(), 0)
call_3454 = relay.TupleGetItem(func_2273_call(), 0)
output = relay.Tuple([call_3453,])
output2 = relay.Tuple([call_3454,])
func_3463 = relay.Function([], output)
mod['func_3463'] = func_3463
mod = relay.transform.InferType()(mod)
mutated_mod['func_3463'] = func_3463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mutated_mod.get_global_var('func_3463')
call_3464 = func_3463_call()
output = call_3464
func_3465 = relay.Function([], output)
mutated_mod['func_3465'] = func_3465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_3466 = relay.TupleGetItem(func_3463_call(), 0)
call_3467 = relay.TupleGetItem(func_3465_call(), 0)
output = call_3466
output2 = call_3467
func_3477 = relay.Function([], output)
mod['func_3477'] = func_3477
mod = relay.transform.InferType()(mod)
output = func_3477()
func_3478 = relay.Function([], output)
mutated_mod['func_3478'] = func_3478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_3535 = relay.TupleGetItem(func_2271_call(), 2)
call_3536 = relay.TupleGetItem(func_2273_call(), 2)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
var_3553 = relay.var("var_3553", dtype = "float64", shape = (4, 8))#candidate|3553|(4, 8)|var|float64
call_3552 = func_655_call(relay.reshape(var_3553.astype('float64'), [16, 2]))
call_3554 = func_655_call(relay.reshape(var_3553.astype('float64'), [16, 2]))
func_3238_call = mod.get_global_var('func_3238')
func_3239_call = mutated_mod.get_global_var('func_3239')
call_3561 = relay.TupleGetItem(func_3238_call(), 0)
call_3562 = relay.TupleGetItem(func_3239_call(), 0)
output = relay.Tuple([call_3535,call_3552,var_3553,call_3561,])
output2 = relay.Tuple([call_3536,call_3554,var_3553,call_3562,])
func_3575 = relay.Function([var_3553,], output)
mod['func_3575'] = func_3575
mod = relay.transform.InferType()(mod)
mutated_mod['func_3575'] = func_3575
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3576 = relay.var("var_3576", dtype = "float64", shape = (4, 8))#candidate|3576|(4, 8)|var|float64
func_3575_call = mutated_mod.get_global_var('func_3575')
call_3577 = func_3575_call(var_3576)
output = call_3577
func_3578 = relay.Function([var_3576], output)
mutated_mod['func_3578'] = func_3578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3045_call = mod.get_global_var('func_3045')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3606 = relay.TupleGetItem(func_3045_call(), 0)
call_3607 = relay.TupleGetItem(func_3047_call(), 0)
output = call_3606
output2 = call_3607
func_3613 = relay.Function([], output)
mod['func_3613'] = func_3613
mod = relay.transform.InferType()(mod)
output = func_3613()
func_3614 = relay.Function([], output)
mutated_mod['func_3614'] = func_3614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_3702 = relay.TupleGetItem(func_3463_call(), 0)
call_3703 = relay.TupleGetItem(func_3465_call(), 0)
output = call_3702
output2 = call_3703
func_3717 = relay.Function([], output)
mod['func_3717'] = func_3717
mod = relay.transform.InferType()(mod)
output = func_3717()
func_3718 = relay.Function([], output)
mutated_mod['func_3718'] = func_3718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_3866 = func_191_call()
call_3867 = func_191_call()
output = call_3866
output2 = call_3867
func_3871 = relay.Function([], output)
mod['func_3871'] = func_3871
mod = relay.transform.InferType()(mod)
output = func_3871()
func_3872 = relay.Function([], output)
mutated_mod['func_3872'] = func_3872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_3960 = relay.TupleGetItem(func_634_call(), 0)
call_3961 = relay.TupleGetItem(func_636_call(), 0)
output = call_3960
output2 = call_3961
func_3979 = relay.Function([], output)
mod['func_3979'] = func_3979
mod = relay.transform.InferType()(mod)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3979_call = mutated_mod.get_global_var('func_3979')
call_3980 = func_3979_call()
output = call_3980
func_3981 = relay.Function([], output)
mutated_mod['func_3981'] = func_3981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4059 = relay.var("var_4059", dtype = "int8", shape = (7, 11, 14))#candidate|4059|(7, 11, 14)|var|int8
var_4060 = relay.var("var_4060", dtype = "int8", shape = (7, 11, 14))#candidate|4060|(7, 11, 14)|var|int8
bop_4061 = relay.less(var_4059.astype('bool'), relay.reshape(var_4060.astype('bool'), relay.shape_of(var_4059))) # shape=(7, 11, 14)
func_1018_call = mod.get_global_var('func_1018')
func_1021_call = mutated_mod.get_global_var('func_1021')
const_4068 = relay.const([-7,9,1,1,-9,3,-1,8,-1,-4,8,-2,5,-7,-5,5,3,-5,5,8,-8,5,8,-3,-2,1,2,9,1,8,-8,9,9,8,2,8,-10,1,10,-4,5,-2,-3,4,-7,-1,7,8,5,-10,3,9,4,-1,4,-7,-5,5,10,-3,4,-3,3,7,-9,-7,8,8,-3,-8,-8,-5,-2,10,-10,10,-6,-4,-4,9,9,-8,9,1,-6,-9,4,5], dtype = "int32")#candidate|4068|(88,)|const|int32
var_4069 = relay.var("var_4069", dtype = "int32", shape = (880,))#candidate|4069|(880,)|var|int32
call_4067 = func_1018_call(relay.reshape(const_4068.astype('int32'), [11, 1, 8]), relay.reshape(var_4069.astype('int32'), [11, 10, 8]), )
call_4070 = func_1018_call(relay.reshape(const_4068.astype('int32'), [11, 1, 8]), relay.reshape(var_4069.astype('int32'), [11, 10, 8]), )
func_692_call = mod.get_global_var('func_692')
func_694_call = mutated_mod.get_global_var('func_694')
const_4074 = relay.const([0.894244,-6.503734,-4.695062,1.088071,-3.583473,-8.478068,-7.325009,7.920426,-4.736520,-0.348456,-5.437586,5.666676,-7.798961,1.411663,9.998032,-4.530067,5.701162,1.985204,-4.673782,-1.844069,-9.058491,1.177637,2.343192,-1.752708,0.826332,-0.710434,-0.419115,-9.245410,-7.226693,-8.041624,-4.207573,6.074966,4.698843,-6.964330,2.985742,-9.293748,3.359475,-2.831326,9.995492,-9.672430,4.073185,-1.811268,-0.570697,5.455081,-5.391781,-6.400562,-3.382922,-1.871206,-2.358779,9.324911,-6.591476,1.411364,5.056261,-4.186718,6.380755,7.327088,5.200295,-1.232340,0.847158,4.288990,-0.298036,-9.696218,2.940331,-4.649960,5.755545,5.465008,-8.223953,-6.960566,5.955219,-0.742309,9.944307,8.090245,4.918150,5.462573,3.074545,1.876941,-3.111291,-5.315674,-3.937524,-1.987375,9.997206,5.283891,-6.511205,3.007592,2.860702,-3.941103,-9.758746,5.124918,-0.536924,-8.693801,6.792291,5.781845,5.109336,5.790186,-5.131448,-2.412522,-3.289434,6.464598,3.378685,-6.270730,-7.325853,7.461098,-8.932174,7.108645,8.335365,0.149216,3.675022,6.389259,-6.693873,-7.113724,-0.549735,-8.299758,5.895416,2.056899,7.673541,1.164695,8.492786,-9.558430,2.365191,-3.933146,8.123778,-4.333624,-9.523194,3.769364,-5.560479,7.104061,-8.641470,1.105768,-1.420897,-8.774073,-0.215873,5.214358,7.145210,-1.463637,2.244513,8.008576,-2.500827,0.844938,3.207803,5.031505,3.395481,-2.716276,9.078599,3.083664,6.729072,7.313316,3.673659,4.065540,-7.157326,2.048172,-7.946348,-0.873674,-8.244692,0.673436,-4.325761,-6.212010,7.189466,-0.105486,-6.269411,-5.750518,5.185924,-7.458434,4.265622,2.520607,5.133898,1.949645,-8.207029,-0.653117,-7.374413,-5.367133,-8.758339,-3.295532,-0.516344,-7.889766,-1.091507,-9.001394,-3.602397,-3.173084,-6.769223,3.589777,-8.832315,9.678728,-3.061671,-2.061340,3.237728,-7.489471,6.262953,3.576226,8.507503,-7.004943,1.793203,1.957634,1.278888,1.705669,-9.350878,0.083821,4.165245,1.100438,-9.046392,-2.193266,-8.954813,-4.219052,5.244451,5.624730,5.844792,-7.388104,-0.331903,1.887713,8.171183,9.963950,8.376548,1.660859,4.376823,4.450859,-9.300801,1.634241,-9.867800,-3.792717,-9.772962,-8.502767,9.415773,-3.797490,-3.302767,-5.208523,-0.183112,9.517396,-4.902091,-8.227160,4.181640,-0.548513,-2.880196,5.438962,7.602520,-4.762085,2.462571,9.774775,-1.091470,9.685066,7.094658,-6.761543,6.942563,-9.377697,-5.645530,-6.636144,-3.532014,1.197545,-0.822372,7.146739,-0.193438,4.325028,-8.056476,6.469160,-9.928817,2.784325,-8.563817,6.459266,-4.150500,3.022647,2.453177,-9.338173,-9.525895,-9.357791,-4.178531,-2.575324,4.808800,0.882360,8.115168,-1.753021,2.297579,7.434861,-9.344594,8.484188,-0.899742,9.235110,-1.543124,2.461726,-3.416680,-2.447940,3.273841,3.415859,-4.942405,-1.316718,4.743279,-4.596563,8.927853,-4.438385,-1.852814,-1.404899,4.271430,-1.396514,3.683873,-9.075885,9.021008,4.873244,-0.627464,-3.958710,8.052775,-2.724079,9.738107,9.622353,-0.329666,-5.514986,3.731740,-9.996951,6.421804,8.250142,-8.875290,-0.523955,-3.405943,7.807460,-7.461396,3.928254,-5.967269,8.994887,-1.385771,-0.187312,-8.208962,-1.201890,1.770729,-3.001014,8.235342,-1.935631,-7.713318,-4.005613,-7.922053,9.989304,7.850261,-1.035628,-2.016240,3.983155,-2.666998,3.539752,5.071842,-9.676310,-9.003286,5.835156,-5.927822,-3.957709,-8.471790,0.469993,-3.012770,7.444986,-6.500995,8.473352,3.699970,5.607779,1.361596,5.030340,-3.120437,4.433849,-2.864731,5.004820,-0.100532,7.154425,-1.510583,7.432686,8.136490,-8.806832,-0.039044,-0.248618,-6.034384,1.583309,4.193628,-5.979586,7.299769,-9.021221,-0.264597,-1.639477,1.192378,4.767392,0.123160,-4.666809,-2.204826,-3.526292,4.774588,-4.555601,-9.388303,1.497003,-7.487943,-1.847512,5.805731,-4.480272,-0.268435,2.258175,-2.268057,1.436621,5.155448,9.915704,-4.873916,5.244814,-4.969803,1.430520,3.100464,-5.679718,3.535306,5.448064,-3.258555,-2.882498,6.162229,-4.002595,1.767309,7.404746,-9.443995,-9.608479,-8.325716,-3.842853,1.968961,4.649259,-6.331226,7.535841,-5.933410,-8.529356,-2.608085,6.539373,-5.363503,4.749371,1.600448,6.280669,7.892825,-5.969564,3.701623,5.894556,9.675249,6.680208,-5.336843,9.938873,-7.426609,2.906084,-8.997682,-9.380862,3.478091,-5.387888,-5.741317,-0.080073,9.060767,1.250536,1.535536,-0.150898,7.652488,-8.363392,-2.041697,8.508385,3.746909,9.384842,3.897191,7.494894,8.997539,-0.134890,9.731898,-1.582048,9.549824,4.881758,-3.550453,0.413915,8.836595,5.829461,7.084583,-4.228042,-4.789937,6.236930,1.806089,-5.902854,-3.811736,-6.409356,5.327273,0.522897,-1.568560,3.827091,-3.352767,3.944963,-7.340346,3.766469,3.850148,-1.561084,1.850705,0.653702,-5.836674,7.044078,-9.287975,-2.355631,-5.341547,3.212987,-8.534232,1.051699,3.793073,7.515961,-4.996915,-5.226636,-6.967968,6.626790,-4.311525,9.104929,-2.366900,2.519502,-4.532631,-5.017206,2.852707,-5.833140,-1.842720,-4.218903,-5.272988,5.400678,-4.530855,-3.123285,-6.925686,-4.505132,-0.802166,-6.539160,2.454843,-9.798922,5.302590,-0.537230,-9.479630,0.369763,7.417266,-0.851985,2.240020,-7.142895,8.615074,-2.352768,-2.732792,-4.421174,-2.379736,0.878030,1.281357,-4.820915,-7.004267,2.620883,7.511306,3.025851,5.230397,-0.747971,3.777929,-5.046038,5.617358,-8.111881,-0.578886,-2.380850,2.004753,-5.601896,8.340913,-3.410433,7.318243,-1.523424,-1.984186,0.401317,-0.353719,-4.246947,-3.166581,-8.716549,5.035241,2.094078,-8.963313,6.976301,5.177775,-5.031928,-2.812807,-2.439637,-8.546125,-3.320269,-8.990555,-0.231778,4.541689,-3.019362,-6.666833,0.601325,-9.161361,6.757780,-2.783303,-2.942696,-8.092567,6.778368,5.257985,-9.314801,-8.555705,-6.605731,6.927383,9.995539,9.637970,-0.297680,4.313827,-4.770402,0.870324,-8.611879,-2.639217,0.146713,2.568606,8.559240,7.626961,-7.182302,-1.236633,-6.330507,-3.976123,-0.795666,-0.812884,6.681347,-4.172181,7.161827,8.460862,0.583152,-7.094088,-5.527850,7.857427,8.323482,7.763744,9.413704,-9.356483,4.450375,3.436560,4.396503,5.820251,1.987846,-0.241626,8.708692,-5.227311,4.632885,9.804650,-5.958848,7.718646,9.799902,-4.086391,-3.371125,9.893224,7.011937,1.737984,-9.322140,9.340696,-7.921798,-7.137391,3.001961,-7.800194,9.959637,-7.194320,5.451833,6.566354,-8.992775,7.311826,6.311888,3.966690,1.786546,5.523693,6.762135,-7.485637,-0.223646,2.247026,1.803356,-2.876886,1.021406,6.520780,-6.849681,-0.878765,-4.169656,8.090544,-4.824295,-9.815284,6.789818,2.156416,-7.142640,-3.424556,-4.042335,-5.834950,0.265504,-8.474273,8.367881,1.434552,2.102189,-6.981816,6.700884,6.723392,-7.294144,-7.479986,5.536322,-0.694768,2.945796,-2.831028,-9.551418,6.186176,9.374636,2.465987,9.152289,-8.540560,-1.081906,-8.103101,-0.515650,1.953032,8.736757,-9.582118,0.400885,-2.691664,0.977989,-5.640858,8.716581,8.177141,8.577563,4.027932,-4.713670,1.956893,0.536894,-6.230947,0.833394,-3.710525,0.547168,1.994531,-2.356435,6.627154,-1.915725,2.959980,-9.939093,-1.633886,0.017378,-2.006433,0.613547,-9.398171,-5.194419,-8.238669,-3.143205,-0.668186,9.551671,-9.263605,-4.178539,2.011417,9.009295,-4.698238,-9.862259,-6.428617,0.047266,1.256068,-9.805819,6.535135,-8.494026,5.656826,-0.517299,8.255993,8.056606,4.578117,8.710716,8.835477,-7.577217,-7.281986,-2.483982,-8.214263,-5.541752,2.665885,-8.189485,2.044751,-2.469732,4.931615,-0.632068,9.234464,9.455308,1.293218,5.867226,9.402912,6.620097,-5.973361,-8.714321,3.453860,-3.273300,-8.223247,8.428738,-6.487329,-7.147011,-5.310398,-6.403155,-0.840747,5.500294,-3.151164,-5.732636,-1.497184,-3.667186,-7.442971,3.567160,5.988537,-8.698279,-3.510157,6.744911,7.880654,9.476263,-2.966898,0.304154,4.504219,1.885481,-8.273175,0.288405,0.630080,3.382574,5.897650,6.793392,1.580139,-8.386871,6.639054,-1.444645,0.145635,-4.143643,2.118969,-0.431335,-6.600111,-3.128385,-8.467468,4.262797,9.216037,2.503215,-4.249223,4.081972,-8.448822,0.453569,7.757978,-0.055167,6.125619,4.578373,3.142020,9.977236,9.681332,-6.488457,-0.759942,1.731847,-1.624703,-8.835647,7.889658,-2.089205,2.146466,4.619764,5.765133,9.511473,-8.166274,4.956029,-7.870086,-0.191553,3.408964,1.077525,-6.088210,2.489208,2.434692,4.830809,-2.361420,-6.310176,-1.961683,-0.989022,-9.801086,-0.897883,-8.841554,-7.546140,3.934959,-6.212086,9.204197,-7.676292,-2.161906,-5.476555,7.982223,-4.465407,-6.890929,3.168821,-6.006126,-2.909316,8.778320,-1.552641,1.010217,-3.088835,5.120055,8.720070,7.265228,-1.680048,2.563660,1.870194,0.122479,-4.375332,7.960482,-3.051919,-7.631109,-9.549279,4.275370,8.890017,9.680742,6.653888,9.601617,8.047101,-3.532867,-2.390680,-6.628317,-6.138928,-6.586768,2.472242,-4.528748,8.215956,6.039745,-3.922461,-4.956360,5.931177,-6.450740,-2.020776,7.344268,-8.498106,-4.088086,3.658504,-7.106778,-5.787776,1.784683,-8.443968,4.668076,-2.236197,3.631343,7.374640,-2.644404,0.205472,-9.615115,-6.660981,3.056776,3.142001,-7.152066,7.421789,6.712663,6.747663,8.472507,-0.139795,4.260806,4.461972,-0.746323,3.434674,7.055241,9.810862,-3.967191,1.616418,-5.782962,0.348696,-3.850378,2.648094,-5.751404,-0.053695,7.409485,-7.438918,7.737739,6.499566,7.680408,-3.266278,-2.266303,-3.568033,-3.069096,-3.025113,-3.008463,2.940385,-9.532972,-6.369996,6.805363,2.006325,-5.394600,1.136710,8.350159,1.451491,4.108017,-9.602270,9.182579,0.592210,-5.220462,-0.561859,2.889496,2.971194,-4.734912,5.961566,-4.107945,-5.022290,-6.714805,-1.830260,3.011048,-4.511123,-9.595913,-3.830861,7.181775,2.231094,9.171371,3.963287,3.962997,6.460298,-3.557734,5.821488,7.147218,5.296697,6.540277,7.511853,1.420982,-6.449812,-6.200296,7.163576,-4.494853,-8.365962,-7.830027,-6.328643,-4.167179,-2.188745,-9.592206,-5.059638,0.029326,-7.158813,5.529983,2.402670,9.968242,-1.332822,-5.502305,-1.763788,-0.527292,0.546011,-0.354311,-4.657512,9.160945,8.400832,-5.610414,9.165430,-7.936721,0.374389,3.791262,-1.721934,-7.316147,2.294776,7.082124,8.784193,-4.794339,-5.254878,-9.024898,4.659037,8.842603,-6.344282,-0.895058,-0.831432,2.936994,2.884133,-4.188732,2.290215,-9.631833,-5.244245,-0.538167,-3.744246,-3.984736,1.957008,6.128626,-4.803929,-7.062774,7.769346,-5.238370,6.830636,6.994341,-6.358167,-1.825808,-2.969783,-3.665779,-8.093848,-9.029052,9.721131,-1.327250,4.189918,-3.110888,-2.887633,-6.636553,0.823544,4.418153,-9.563917,1.030644,8.444518,4.047770,2.107615,-9.167021,-1.562451,-0.287966,4.117038,3.702963,-5.063179,-2.525113,-9.651261,-2.651798,6.065084,-8.543233,-4.018064,-9.242232,4.691673,2.706379,-5.759019,9.950101,-6.151522,-3.148996,-9.308437,5.947861,1.959994,2.846390,-9.347057,-3.540055,-6.776093,-1.912186,-4.666267,-9.013625,-7.841377,-2.563796,7.472306,9.220687,4.803622,6.490945,2.436408,9.426059,-2.605244,-7.067423,-8.681948,-9.373588,8.242737,-5.957257,3.679029,-7.836413,-3.587138,-2.796117,-7.320335,-5.871544,-0.505957,7.385956,-6.456280,-3.574980,5.712135,2.324343,5.830618,-9.865440,-9.237437,9.301915,5.050333,9.892035,-6.712653,2.206021,-6.854340,3.787265,5.554318,-6.884545,6.160481,-9.586989,-9.561253,-6.419738,9.321698,-5.445624,8.748701,-9.229658,6.919405,9.079268,7.465815,-0.577983,-2.293877,-3.916126,-5.257135,4.602215,-5.110881,2.822969,0.365418,-7.365084,-0.146967,4.491607,-5.689492,1.598338,2.225711,-1.681757,0.812534,-8.978333,-4.980429,-9.239139,-7.304736,-8.231021,0.226828,1.512287,0.452666,-0.958503,-2.004657,-3.782434,6.259528,2.131952,-7.098250,8.751520,-5.741165,0.460667,6.336679,-8.032315,2.617657,-7.909523,-2.552962,7.632566,8.832114,3.177491,0.012559,8.380770,0.604551,-2.422219,-3.286586,-1.564929,9.921749,2.053639,2.564191,-9.078256,-8.079498,3.643249,-6.136257,-3.572429,-0.850289,-1.722384,5.715502,-5.654590,-9.168000,-9.128749,1.633278,9.414214,-8.194177,4.118155,-2.396823,-2.648587,-3.893076,1.566637,5.161648,-8.064928,-7.160829,2.229088,-9.082812,-3.037174,-5.637639,5.602270,6.274401,9.844560,4.597520,6.150505,-0.153400,-5.697008,-8.105389,-8.387977,-7.037220,0.406108,5.467297,-2.234882,6.219134,-7.904432,-3.011984,5.799891,-8.355093,0.554822,5.852840,-2.023035,3.613689,-4.057310,-8.475061,2.639388,3.957257,1.574230,2.583491,1.627169,0.307914,1.931265,5.931860,4.978320,5.377884,-3.504115,-0.019664,-3.842740,6.259872,4.885237,1.921387,-3.158662,4.644967,1.839090,-3.738843,7.933630,-3.830161,9.149020,4.389364,-3.524621,7.107808,5.758341,2.909400,3.851536,-4.701211,-2.683467,8.626418,4.290179,3.578724,-9.811560,6.834339,0.123698,-8.890973,1.864490,5.071783,-7.506994,-7.326790,-5.108668,4.168737,7.684897,-6.023880,-7.305501,-2.657554,1.093280,-1.787085,7.891071,1.149431,-0.691881,6.782020,-3.323181,5.008697,-0.144566,-4.207980,4.936172,-6.534565,-0.597823,-4.289660,4.663738,-4.728681,-0.864420,-5.152439,-7.894364,-5.459607,7.339116,-0.887491,7.485280,-5.267415,-2.451164,-7.455429,-2.854284,-2.415490,-9.704926,3.797134,2.309640,-9.376748,8.428170,-0.853189,-4.257798,-2.197563,-1.769985,8.826722,-3.577264,3.873972,2.283917,-2.273403,5.798491,-1.315567,2.167039,9.421732,3.557445,0.730205,-4.616443,-6.502372,-2.316694,-1.575606,4.597107,-2.931396,7.989640,-7.706420,-6.929835,-2.268040,6.095276,4.535110], dtype = "float32")#candidate|4074|(1344,)|const|float32
call_4073 = relay.TupleGetItem(func_692_call(relay.reshape(const_4074.astype('float32'), [14, 6, 16])), 0)
call_4075 = relay.TupleGetItem(func_694_call(relay.reshape(const_4074.astype('float32'), [14, 6, 16])), 0)
uop_4077 = relay.asinh(const_4068.astype('float32')) # shape=(88,)
output = relay.Tuple([bop_4061,call_4067,var_4069,call_4073,const_4074,uop_4077,])
output2 = relay.Tuple([bop_4061,call_4070,var_4069,call_4075,const_4074,uop_4077,])
func_4083 = relay.Function([var_4059,var_4060,var_4069,], output)
mod['func_4083'] = func_4083
mod = relay.transform.InferType()(mod)
var_4084 = relay.var("var_4084", dtype = "int8", shape = (7, 11, 14))#candidate|4084|(7, 11, 14)|var|int8
var_4085 = relay.var("var_4085", dtype = "int8", shape = (7, 11, 14))#candidate|4085|(7, 11, 14)|var|int8
var_4086 = relay.var("var_4086", dtype = "int32", shape = (880,))#candidate|4086|(880,)|var|int32
output = func_4083(var_4084,var_4085,var_4086,)
func_4087 = relay.Function([var_4084,var_4085,var_4086,], output)
mutated_mod['func_4087'] = func_4087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_4109 = func_2096_call()
call_4110 = func_2096_call()
output = relay.Tuple([call_4109,])
output2 = relay.Tuple([call_4110,])
func_4111 = relay.Function([], output)
mod['func_4111'] = func_4111
mod = relay.transform.InferType()(mod)
output = func_4111()
func_4112 = relay.Function([], output)
mutated_mod['func_4112'] = func_4112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4111_call = mod.get_global_var('func_4111')
func_4112_call = mutated_mod.get_global_var('func_4112')
call_4122 = relay.TupleGetItem(func_4111_call(), 0)
call_4123 = relay.TupleGetItem(func_4112_call(), 0)
output = call_4122
output2 = call_4123
func_4154 = relay.Function([], output)
mod['func_4154'] = func_4154
mod = relay.transform.InferType()(mod)
mutated_mod['func_4154'] = func_4154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mutated_mod.get_global_var('func_4154')
call_4155 = func_4154_call()
output = call_4155
func_4156 = relay.Function([], output)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_4170 = relay.TupleGetItem(func_3331_call(), 0)
call_4171 = relay.TupleGetItem(func_3333_call(), 0)
output = call_4170
output2 = call_4171
func_4200 = relay.Function([], output)
mod['func_4200'] = func_4200
mod = relay.transform.InferType()(mod)
output = func_4200()
func_4201 = relay.Function([], output)
mutated_mod['func_4201'] = func_4201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2271_call = mod.get_global_var('func_2271')
func_2273_call = mutated_mod.get_global_var('func_2273')
call_4232 = relay.TupleGetItem(func_2271_call(), 0)
call_4233 = relay.TupleGetItem(func_2273_call(), 0)
func_1018_call = mod.get_global_var('func_1018')
func_1021_call = mutated_mod.get_global_var('func_1021')
const_4267 = relay.const([-3,-8,5,-6,10,5,-6,-2,-3,2,10,-1,5,-6,-6,-1,-5,8,6,-9,8,6,6,-7,-9,-9,5,10,9,-5,10,-8,5,-5,9,-1,-1,-1,7,7,6,-6,7,-1,1,-5,-1,6,-8,1,8,-4,-9,5,10,-1,-10,-7,3,7,-1,-5,-5,10,-3,-1,-3,7,8,5,5,-6,2,-4,-9,-9,5,-7,-4,-6,-8,-7,1,-2,-5,9,-2,5], dtype = "int32")#candidate|4267|(88,)|const|int32
var_4268 = relay.var("var_4268", dtype = "int32", shape = (880,))#candidate|4268|(880,)|var|int32
call_4266 = func_1018_call(relay.reshape(const_4267.astype('int32'), [11, 1, 8]), relay.reshape(var_4268.astype('int32'), [11, 10, 8]), )
call_4269 = func_1018_call(relay.reshape(const_4267.astype('int32'), [11, 1, 8]), relay.reshape(var_4268.astype('int32'), [11, 10, 8]), )
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_4294 = relay.TupleGetItem(func_3331_call(), 0)
call_4295 = relay.TupleGetItem(func_3333_call(), 0)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
var_4298 = relay.var("var_4298", dtype = "float64", shape = (32, 1))#candidate|4298|(32, 1)|var|float64
call_4297 = func_655_call(relay.reshape(var_4298.astype('float64'), [16, 2]))
call_4299 = func_655_call(relay.reshape(var_4298.astype('float64'), [16, 2]))
func_2606_call = mod.get_global_var('func_2606')
func_2608_call = mutated_mod.get_global_var('func_2608')
call_4304 = relay.TupleGetItem(func_2606_call(), 0)
call_4305 = relay.TupleGetItem(func_2608_call(), 0)
func_3444_call = mod.get_global_var('func_3444')
func_3446_call = mutated_mod.get_global_var('func_3446')
call_4323 = relay.TupleGetItem(func_3444_call(), 1)
call_4324 = relay.TupleGetItem(func_3446_call(), 1)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_4332 = func_2096_call()
call_4333 = func_2096_call()
output = relay.Tuple([call_4232,call_4266,const_4267,var_4268,call_4294,call_4297,var_4298,call_4304,call_4323,call_4332,])
output2 = relay.Tuple([call_4233,call_4269,const_4267,var_4268,call_4295,call_4299,var_4298,call_4305,call_4324,call_4333,])
func_4343 = relay.Function([var_4268,var_4298,], output)
mod['func_4343'] = func_4343
mod = relay.transform.InferType()(mod)
var_4344 = relay.var("var_4344", dtype = "int32", shape = (880,))#candidate|4344|(880,)|var|int32
var_4345 = relay.var("var_4345", dtype = "float64", shape = (32, 1))#candidate|4345|(32, 1)|var|float64
output = func_4343(var_4344,var_4345,)
func_4346 = relay.Function([var_4344,var_4345,], output)
mutated_mod['func_4346'] = func_4346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1271_call = mod.get_global_var('func_1271')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_4372 = relay.TupleGetItem(func_1271_call(), 1)
call_4373 = relay.TupleGetItem(func_1272_call(), 1)
output = relay.Tuple([call_4372,])
output2 = relay.Tuple([call_4373,])
func_4374 = relay.Function([], output)
mod['func_4374'] = func_4374
mod = relay.transform.InferType()(mod)
output = func_4374()
func_4375 = relay.Function([], output)
mutated_mod['func_4375'] = func_4375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3477_call = mod.get_global_var('func_3477')
func_3478_call = mutated_mod.get_global_var('func_3478')
call_4381 = func_3477_call()
call_4382 = func_3477_call()
func_692_call = mod.get_global_var('func_692')
func_694_call = mutated_mod.get_global_var('func_694')
call_4393 = relay.TupleGetItem(func_692_call(relay.reshape(call_4381.astype('float32'), [14, 6, 16])), 1)
call_4394 = relay.TupleGetItem(func_694_call(relay.reshape(call_4381.astype('float32'), [14, 6, 16])), 1)
output = relay.Tuple([call_4381,call_4393,])
output2 = relay.Tuple([call_4382,call_4394,])
func_4395 = relay.Function([], output)
mod['func_4395'] = func_4395
mod = relay.transform.InferType()(mod)
mutated_mod['func_4395'] = func_4395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4395_call = mutated_mod.get_global_var('func_4395')
call_4396 = func_4395_call()
output = call_4396
func_4397 = relay.Function([], output)
mutated_mod['func_4397'] = func_4397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3045_call = mod.get_global_var('func_3045')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_4448 = relay.TupleGetItem(func_3045_call(), 2)
call_4449 = relay.TupleGetItem(func_3047_call(), 2)
func_1380_call = mod.get_global_var('func_1380')
func_1382_call = mutated_mod.get_global_var('func_1382')
const_4458 = relay.const([9.826449,-1.736161,1.404672,6.439410,-3.325463,-5.959691,7.311942,1.861360,-6.443784,-2.312034,-5.853016,-8.387358,-2.353005,-2.969362,2.133445,8.201202,0.547324,5.746365,-9.328153,-8.890758,-4.023598,-9.799301,-5.156195,-5.096968,-1.173738,1.870148,-3.465069,-6.679408,-0.811953,6.772638,-0.022379,-7.242063,-0.258538,-8.695055,-3.585928,5.604263,-3.482145,1.524086,-8.993129,2.160828,-6.520885,3.580048,-7.915375,-9.514545,0.699301,-1.898528,-7.798202,0.095724,-9.055719,4.620531,8.383931,-5.056871,0.912712,-0.494473,6.588914,-5.447920,-6.393765,7.269300,-5.351902,8.993214,3.397254,6.384984,7.439579,-8.969149,0.586560,-2.199481,-7.158077,-1.772582,-8.336533,7.465435,-4.720389,-5.213677,-3.153007,8.300894,0.662521,-4.610606,-3.455080,-1.553146,-4.480955,-8.343671,6.836942,-4.242387,5.864435,2.674814,3.268690,5.382124,-4.199041,7.488161,8.923141,3.146829,8.235803,1.422760,-9.609376,1.200588,-9.197195,-3.698373,8.205670,-8.029889,2.561650,-5.218065,-8.111679,-5.534544,9.178160,5.368368,-0.771467,7.467176,-6.754357,6.475266,4.984765,-9.257168,-8.155357,8.598901,6.358013,-8.600113,7.974974,-1.486757,3.626607,-1.292787,-8.789011,7.034815,7.966331,-5.449845,-5.443377,-6.574043,8.939869,1.916757,6.855028,3.229473,-4.460980,8.263623,-8.747222,-4.341060,-4.714031,9.903244,-0.480513,0.160280,1.323276,-8.461735,8.367713,3.808809,6.661700,1.863099,0.726610,6.542892,-0.500212,9.614189,-4.958681,-9.486219,1.124058,2.263078,9.932254,4.653738,4.394161,-1.043508,-1.456827,8.521099,-2.508500,-6.998790,5.400232,-4.036744,-5.809620,-0.168377,2.072867,9.277858,-4.060796,-0.879235,6.752934,5.129564,3.865612,9.080768,3.041335,2.371689,3.331083,-9.474983,-7.602668,2.734413,-1.983108,4.109242,-7.704882,-3.754916,-5.824483,-3.954509,-1.669217,-1.052836,2.553154,4.902580,-1.220255,7.987750,-1.079115,-5.677175,-3.598425,9.510365,2.967293,-9.726678,0.688624,8.801977,3.002169,7.172607,6.926349,-2.115931,-0.236638,6.196336,-1.251872,-5.088207,-6.409102,1.433584,-4.964980,-9.854328,-1.918803,-4.710346,5.710224,7.175827,9.581472,6.773414,-6.761677,-5.834757,5.382722,9.478655,-2.858432,1.577028,-9.246294,6.125204,5.227344,-3.992386,-8.627919,-2.703504,-5.471797,-2.365951,-8.774932,-7.931734,8.215558,3.431901,9.654996,0.813049,6.832190,-4.053240,7.973552,-6.072096,8.887505,-4.020346,9.144998,-7.731537,-9.392167,-2.353686,-8.503495,0.741424,7.279638,-1.406369,4.799843,-5.527324,-0.279461,-9.827300,-2.442581,2.561843,-0.999421,0.860122,-2.651709,0.418173,-6.721126,8.066278,0.981767,8.054935,-6.634472,1.708333,2.636746,-9.741337,-2.377764,6.085578,2.035552,8.821507,3.725712,-6.194575,-9.969177,-4.818489,5.706573,2.499078,7.191127,3.056941,-1.799117,7.055604,-7.476445,-7.242870,5.312246,7.810320,-2.491774,-1.605640,7.064558,1.523913,-5.547485,-3.685374,8.035502,-5.826777,-4.200427,-6.301169,-2.827714,-3.943584,2.536487,-5.988001,4.015283,-3.265273,-5.502152,3.487852,9.430867,8.109902,-2.196482,1.244103,4.735689,-4.128367,6.786542,-1.499508,6.668067,-2.941215], dtype = "float32")#candidate|4458|(312,)|const|float32
call_4457 = func_1380_call(relay.reshape(const_4458.astype('float32'), [3, 8, 13]))
call_4459 = func_1380_call(relay.reshape(const_4458.astype('float32'), [3, 8, 13]))
output = relay.Tuple([call_4448,call_4457,const_4458,])
output2 = relay.Tuple([call_4449,call_4459,const_4458,])
func_4461 = relay.Function([], output)
mod['func_4461'] = func_4461
mod = relay.transform.InferType()(mod)
output = func_4461()
func_4462 = relay.Function([], output)
mutated_mod['func_4462'] = func_4462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3979_call = mod.get_global_var('func_3979')
func_3981_call = mutated_mod.get_global_var('func_3981')
call_4463 = func_3979_call()
call_4464 = func_3979_call()
func_2533_call = mod.get_global_var('func_2533')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_4470 = relay.TupleGetItem(func_2533_call(), 0)
call_4471 = relay.TupleGetItem(func_2534_call(), 0)
output = relay.Tuple([call_4463,call_4470,])
output2 = relay.Tuple([call_4464,call_4471,])
func_4501 = relay.Function([], output)
mod['func_4501'] = func_4501
mod = relay.transform.InferType()(mod)
mutated_mod['func_4501'] = func_4501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mutated_mod.get_global_var('func_4501')
call_4502 = func_4501_call()
output = call_4502
func_4503 = relay.Function([], output)
mutated_mod['func_4503'] = func_4503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_4514 = relay.TupleGetItem(func_3268_call(), 0)
call_4515 = relay.TupleGetItem(func_3269_call(), 0)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_4522 = relay.TupleGetItem(func_3268_call(), 0)
call_4523 = relay.TupleGetItem(func_3269_call(), 0)
func_3717_call = mod.get_global_var('func_3717')
func_3718_call = mutated_mod.get_global_var('func_3718')
call_4525 = func_3717_call()
call_4526 = func_3717_call()
output = relay.Tuple([call_4514,call_4522,call_4525,])
output2 = relay.Tuple([call_4515,call_4523,call_4526,])
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
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_4547 = func_2096_call()
call_4548 = func_2096_call()
func_2885_call = mod.get_global_var('func_2885')
func_2886_call = mutated_mod.get_global_var('func_2886')
call_4552 = relay.TupleGetItem(func_2885_call(), 0)
call_4553 = relay.TupleGetItem(func_2886_call(), 0)
uop_4563 = relay.tan(call_4552.astype('float32')) # shape=(14, 6, 16)
uop_4565 = relay.tan(call_4553.astype('float32')) # shape=(14, 6, 16)
output = relay.Tuple([call_4547,uop_4563,])
output2 = relay.Tuple([call_4548,uop_4565,])
func_4568 = relay.Function([], output)
mod['func_4568'] = func_4568
mod = relay.transform.InferType()(mod)
mutated_mod['func_4568'] = func_4568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4568_call = mutated_mod.get_global_var('func_4568')
call_4569 = func_4568_call()
output = call_4569
func_4570 = relay.Function([], output)
mutated_mod['func_4570'] = func_4570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_4592 = relay.TupleGetItem(func_2153_call(), 1)
call_4593 = relay.TupleGetItem(func_2155_call(), 1)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_4602 = relay.TupleGetItem(func_2153_call(), 0)
call_4603 = relay.TupleGetItem(func_2155_call(), 0)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
const_4629 = relay.const([-8,-4,-5,-2,-6,-1,4,5,2,6,3,5,-10,8,-4,6,5,7,-10,3,1,-6,-1,4,4,1,2,3,-7,-10,3,-2,-10,8,-8,-6,7,6,3,-1,-2,6,-2,-3,-9,-9,3,-3,-10,2,2,-9,-10,-6,4,1,2,9,-6,1,9,2,-3,4,-5,-1,4,5,4,-6,9,-6,7,-2,-10,-10,7,1,-8,1,-1,2,2,-9,1,7,-5,2], dtype = "int32")#candidate|4629|(88,)|const|int32
call_4628 = relay.TupleGetItem(func_1055_call(relay.reshape(const_4629.astype('int32'), [88,])), 3)
call_4630 = relay.TupleGetItem(func_1058_call(relay.reshape(const_4629.astype('int32'), [88,])), 3)
output = relay.Tuple([call_4592,call_4602,call_4628,const_4629,])
output2 = relay.Tuple([call_4593,call_4603,call_4630,const_4629,])
func_4637 = relay.Function([], output)
mod['func_4637'] = func_4637
mod = relay.transform.InferType()(mod)
mutated_mod['func_4637'] = func_4637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mutated_mod.get_global_var('func_4637')
call_4638 = func_4637_call()
output = call_4638
func_4639 = relay.Function([], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3477_call = mod.get_global_var('func_3477')
func_3478_call = mutated_mod.get_global_var('func_3478')
call_4640 = func_3477_call()
call_4641 = func_3477_call()
output = call_4640
output2 = call_4641
func_4646 = relay.Function([], output)
mod['func_4646'] = func_4646
mod = relay.transform.InferType()(mod)
output = func_4646()
func_4647 = relay.Function([], output)
mutated_mod['func_4647'] = func_4647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4663 = relay.var("var_4663", dtype = "int64", shape = (3, 12, 9))#candidate|4663|(3, 12, 9)|var|int64
const_4664 = relay.const([[[5,-1,-5,-9,-9,-4,-1,1,-7],[6,4,9,-1,2,-6,7,10,-8],[-4,-10,1,9,10,-6,3,-6,-4],[-6,1,-4,-8,-8,8,3,-4,-8],[-10,5,-7,8,6,8,10,-9,-10],[10,6,8,4,10,8,-1,3,8],[-10,7,-2,-8,-8,5,-9,-8,3],[-1,-9,4,-6,-4,4,6,-10,-2],[9,7,6,-5,-9,2,-1,8,1],[-7,-1,-6,5,-9,-7,9,10,3],[-10,-2,3,2,4,-4,-3,2,2],[-9,9,1,-8,4,-6,5,-9,-8]],[[3,-6,7,-2,1,-4,-3,1,10],[10,2,-9,2,8,-3,4,4,2],[2,-4,9,7,1,-4,9,3,7],[-10,6,-10,2,-6,4,10,2,-2],[-1,5,-6,-7,2,-6,1,-9,6],[7,-3,-6,1,-6,9,-5,6,6],[-8,9,-2,10,5,-10,9,10,-10],[-3,-2,3,-5,-4,8,-3,5,-6],[-8,-10,-8,-3,8,2,-10,7,2],[-5,-10,-9,1,5,-5,2,-9,-8],[1,-5,7,-4,-2,8,3,-2,4],[-1,5,-10,-9,8,3,7,1,2]],[[1,4,-1,7,8,6,3,7,-5],[10,9,6,-6,-5,-6,5,-5,1],[3,-9,-7,5,4,8,8,7,-8],[7,-7,10,-9,1,6,-9,9,-10],[-3,-6,6,10,2,1,-10,5,-3],[3,2,8,-7,4,3,2,-10,6],[-2,2,-4,3,5,3,5,-2,1],[2,6,-4,2,6,-4,-8,9,-8],[4,10,3,7,-1,-2,10,-10,2],[7,10,5,-6,-10,-4,-1,-2,-8],[-4,3,-4,8,9,-10,4,4,-1],[-7,4,5,6,8,4,-4,-3,-6]]], dtype = "int64")#candidate|4664|(3, 12, 9)|const|int64
bop_4665 = relay.minimum(var_4663.astype('int64'), relay.reshape(const_4664.astype('int64'), relay.shape_of(var_4663))) # shape=(3, 12, 9)
output = relay.Tuple([bop_4665,])
output2 = relay.Tuple([bop_4665,])
func_4668 = relay.Function([var_4663,], output)
mod['func_4668'] = func_4668
mod = relay.transform.InferType()(mod)
var_4669 = relay.var("var_4669", dtype = "int64", shape = (3, 12, 9))#candidate|4669|(3, 12, 9)|var|int64
output = func_4668(var_4669)
func_4670 = relay.Function([var_4669], output)
mutated_mod['func_4670'] = func_4670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_4682 = relay.TupleGetItem(func_2153_call(), 1)
call_4683 = relay.TupleGetItem(func_2155_call(), 1)
output = call_4682
output2 = call_4683
func_4689 = relay.Function([], output)
mod['func_4689'] = func_4689
mod = relay.transform.InferType()(mod)
mutated_mod['func_4689'] = func_4689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mutated_mod.get_global_var('func_4689')
call_4690 = func_4689_call()
output = call_4690
func_4691 = relay.Function([], output)
mutated_mod['func_4691'] = func_4691
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4692 = relay.var("var_4692", dtype = "float64", shape = (12, 14, 4))#candidate|4692|(12, 14, 4)|var|float64
uop_4693 = relay.atan(var_4692.astype('float64')) # shape=(12, 14, 4)
uop_4695 = relay.log10(uop_4693.astype('float64')) # shape=(12, 14, 4)
uop_4699 = relay.acos(uop_4693.astype('float32')) # shape=(12, 14, 4)
const_4701 = relay.const([[[2.715992,-9.556975,-2.392605,-4.617303],[-0.484327,0.546844,-7.654360,3.142952],[6.541081,-4.153112,7.168911,6.910915],[-6.464876,-6.198934,-6.172138,-0.463742],[-2.221782,-2.931800,1.858421,-6.605451],[9.809300,-9.631612,-7.942208,5.628618],[-1.529625,7.836425,-5.987817,-4.265904],[8.048876,-2.830889,3.040780,1.826620],[-1.316528,-4.790326,-1.922710,8.824104],[-9.947813,6.131352,7.735227,7.702540],[-6.915898,5.308058,3.913577,9.517706],[-2.946160,-0.801869,-9.937448,3.030243],[-4.424225,3.524342,-1.438757,-0.270250],[-9.164008,1.328026,-2.108271,-3.672912]],[[4.018270,5.596545,2.782448,2.257711],[6.065221,7.974383,8.280093,-0.089711],[-9.253011,0.238590,-8.770673,-7.267840],[6.865579,-5.296871,-5.208104,0.462126],[-7.055601,-1.432024,6.313561,9.731060],[3.650655,8.112260,-1.941429,-5.985034],[0.278558,1.311235,4.158773,-0.984941],[-7.574819,-0.632236,3.406220,-7.104695],[1.582176,-9.093614,3.776680,4.791151],[-7.602242,0.224688,-1.306504,-5.619153],[5.239979,5.270775,1.768349,-8.194470],[-2.764250,-7.532870,-9.435664,3.448240],[1.581941,-0.290325,8.941895,1.961509],[-9.308938,-4.708844,1.165701,-3.957769]],[[3.966065,8.949640,-8.304898,-1.738121],[4.326680,-4.594441,0.799996,6.469560],[3.190003,9.113724,4.135531,0.842421],[-7.049405,-4.312985,-1.038476,-7.170673],[-7.762463,-5.247544,0.667441,8.041757],[9.322308,-9.403756,8.541168,4.532199],[-0.824757,7.839559,6.790942,7.102798],[8.252369,4.362253,7.405724,5.513609],[-0.181757,-4.422310,-0.216472,-7.800051],[5.414491,-4.370994,-5.456661,-6.951162],[9.450950,-7.137309,-2.483895,-1.300114],[6.470704,9.338974,6.602276,-7.094599],[-5.609617,-6.702743,-0.529011,-0.215269],[4.329138,-3.131943,-3.137165,-6.487802]],[[-0.144810,-3.727646,2.285641,-3.251185],[1.614380,6.713593,-9.815013,-1.492973],[-8.578900,4.990423,1.860580,-7.896481],[5.043460,-6.224965,5.267878,7.116665],[3.940499,-7.384113,-3.293501,6.344301],[-0.998540,-5.445559,-4.178020,7.713283],[1.147006,4.262490,-4.874491,-1.398526],[-6.524782,0.923733,2.586844,3.830459],[9.519977,0.045744,3.362733,4.782024],[9.546543,-8.347197,-9.887361,-5.355278],[8.187933,-6.160907,-5.465436,3.215163],[2.147549,-3.465471,0.368811,5.848542],[-6.628035,-7.021792,4.120729,4.717398],[9.953351,-0.817072,-7.255317,-8.136005]],[[-8.390685,9.788921,1.325094,1.731468],[-0.439609,5.933389,2.826946,-7.762122],[-2.694332,7.016471,-0.679343,-0.481147],[7.633701,7.557182,-3.721300,1.904573],[-0.493755,1.926604,3.580670,-1.634145],[-9.530441,6.766339,-2.169173,5.785406],[-0.056339,-9.165269,-5.045174,-0.584063],[4.700607,0.205575,0.309824,-9.246240],[6.106093,9.922583,-0.449771,-4.445461],[-1.699445,-9.789330,0.113100,8.750207],[6.596604,-4.557110,-7.901079,3.189943],[-3.001191,5.529813,2.483491,9.160579],[6.989683,4.271542,-0.943231,7.746956],[1.215099,1.769791,6.079518,-4.369776]],[[-0.330663,-8.193192,8.494501,-7.663911],[-0.212076,-9.817585,1.956046,3.468440],[-1.716389,-7.605118,-8.153275,4.662404],[-1.982301,8.906143,1.640900,-4.687617],[-6.530334,8.751056,-1.768347,-5.660866],[4.879037,-4.817681,-1.235981,-8.724967],[-1.547166,-3.046722,-7.789340,-5.100459],[-1.652813,-4.896586,9.759347,-1.886631],[-5.583551,6.328066,9.771098,8.975488],[-6.660842,-6.621779,5.205674,-7.627719],[9.931237,5.555610,-2.528458,-5.279770],[0.640468,7.395560,2.406015,-4.085847],[8.573145,-8.185719,0.567746,8.609007],[5.763232,7.915625,-1.651767,-1.326112]],[[-5.501935,4.121843,1.185900,7.297935],[0.378424,3.314172,-2.383305,-3.839353],[-9.165014,6.325959,-7.512219,7.648609],[-2.191011,7.973163,-0.670263,-6.422319],[8.701387,-9.945006,-7.768765,9.925030],[-1.067445,-4.722956,-6.487647,-6.567669],[-5.983792,7.653741,-9.935268,-7.736483],[7.025205,-1.059163,-9.869111,-6.607998],[-4.736942,-9.770724,-2.264983,-3.585687],[5.372168,-1.573011,5.197359,-5.667660],[-8.298522,7.601208,-9.303253,8.472891],[6.868479,-8.676370,-5.046722,6.054366],[6.265061,0.124869,3.870186,-0.303945],[6.687616,-3.864844,9.807583,-8.454415]],[[-5.329587,-0.053840,0.478762,-7.383530],[9.397100,-2.856953,5.814905,7.755385],[-7.948181,8.704889,-6.233978,-9.766735],[-7.037916,5.353821,9.241593,7.439997],[6.872775,-2.105790,8.632581,2.356405],[9.991307,-9.068864,2.605688,0.389838],[7.084839,9.133856,-4.153312,5.157897],[-4.657150,-0.756517,-9.770725,-4.229544],[-7.225813,-3.814490,2.738203,-7.348139],[-1.391738,-2.132185,-2.376015,9.155700],[-4.088282,-6.261093,-9.141925,5.644197],[-5.617052,-9.626939,7.332037,-7.782456],[9.267704,5.041682,-2.983835,-9.588011],[-6.212458,-5.385708,-5.728726,-9.578715]],[[-3.351890,-1.886089,-8.038042,5.316307],[1.618620,8.895155,-8.464864,-3.292406],[3.314598,6.558754,-7.372019,-1.355289],[-7.062317,7.980029,-1.157934,2.915590],[-2.364045,7.790998,9.019003,4.655303],[-3.068910,3.462274,-6.598376,-6.304696],[1.201461,0.863041,9.282566,-9.712570],[-6.672648,4.495387,-2.415269,0.228416],[-4.505886,5.302625,-0.958017,-3.558839],[-4.738316,6.254543,-3.435862,-9.064480],[2.793061,1.416576,1.805016,-0.869718],[2.265330,-1.601140,-5.325226,0.872940],[-3.414057,-8.318822,0.264818,5.512099],[-2.523227,2.418063,-3.048940,-3.930179]],[[2.876843,5.562812,-4.577761,0.239747],[9.236528,5.888022,3.061290,-0.454627],[6.715574,-0.607623,1.512894,-4.859299],[5.920573,-4.509454,4.605941,4.379260],[-7.376340,6.432243,3.255859,8.855158],[-2.926688,-4.479681,9.022353,5.670289],[-1.224602,0.821718,3.133028,9.327736],[7.888578,9.590489,2.502812,-0.104091],[9.930883,-1.599722,-6.543643,8.541424],[-2.159723,-5.129076,-9.379987,-9.053223],[-7.035689,-3.959117,-4.810633,-3.105073],[-7.067287,-2.764728,-1.848621,4.372065],[0.422187,-6.488722,3.349273,-3.978750],[-8.736556,3.963313,1.462017,8.020459]],[[-8.111905,6.164742,8.750084,-1.867308],[5.401618,9.400401,7.873224,8.532116],[-6.818683,-8.122083,6.335084,3.482403],[-2.998027,-3.985343,3.240105,7.020066],[-2.376260,-1.843046,-0.376541,2.141983],[2.514721,7.149088,0.583860,6.271962],[4.728196,-1.222752,2.581845,-7.771821],[-6.421479,7.778382,-2.802834,4.936172],[9.169435,-1.040530,4.682310,-5.602283],[7.335944,6.295995,-2.736170,-1.345381],[5.641768,1.893239,7.197718,-8.459972],[-6.504112,6.019477,-8.364745,2.159709],[-9.035092,2.278609,1.488371,-2.970605],[1.340784,-5.181058,8.117179,4.687683]],[[1.543564,2.095414,-4.417089,-2.444063],[2.225557,3.605911,5.707008,5.496881],[4.853320,0.227745,-1.323809,9.556241],[9.540361,-3.237449,-2.634443,3.206965],[-3.190934,-2.741928,-8.919013,1.043736],[-8.692748,5.200431,-1.149424,7.087477],[0.038050,-4.334508,6.238100,-8.789261],[6.231105,7.337534,-0.248107,3.417557],[4.434984,-6.636011,9.010497,6.071272],[-2.163739,1.015813,5.346611,-4.363448],[1.465474,0.142443,-5.502620,8.436770],[-4.880466,-0.081498,-8.568982,6.709617],[3.110200,3.250908,8.755714,7.350836],[-9.098743,-8.366730,7.887000,-9.161634]]], dtype = "float64")#candidate|4701|(12, 14, 4)|const|float64
bop_4702 = relay.maximum(uop_4693.astype('uint16'), relay.reshape(const_4701.astype('uint16'), relay.shape_of(uop_4693))) # shape=(12, 14, 4)
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
var_4710 = relay.var("var_4710", dtype = "float32", shape = (1344,))#candidate|4710|(1344,)|var|float32
call_4709 = relay.TupleGetItem(func_435_call(relay.reshape(var_4710.astype('float32'), [14, 6, 16]), relay.reshape(var_4710.astype('float32'), [14, 6, 16]), ), 3)
call_4711 = relay.TupleGetItem(func_438_call(relay.reshape(var_4710.astype('float32'), [14, 6, 16]), relay.reshape(var_4710.astype('float32'), [14, 6, 16]), ), 3)
output = relay.Tuple([uop_4695,uop_4699,bop_4702,call_4709,var_4710,])
output2 = relay.Tuple([uop_4695,uop_4699,bop_4702,call_4711,var_4710,])
func_4717 = relay.Function([var_4692,var_4710,], output)
mod['func_4717'] = func_4717
mod = relay.transform.InferType()(mod)
var_4718 = relay.var("var_4718", dtype = "float64", shape = (12, 14, 4))#candidate|4718|(12, 14, 4)|var|float64
var_4719 = relay.var("var_4719", dtype = "float32", shape = (1344,))#candidate|4719|(1344,)|var|float32
output = func_4717(var_4718,var_4719,)
func_4720 = relay.Function([var_4718,var_4719,], output)
mutated_mod['func_4720'] = func_4720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3477_call = mod.get_global_var('func_3477')
func_3478_call = mutated_mod.get_global_var('func_3478')
call_4765 = func_3477_call()
call_4766 = func_3477_call()
func_4374_call = mod.get_global_var('func_4374')
func_4375_call = mutated_mod.get_global_var('func_4375')
call_4773 = relay.TupleGetItem(func_4374_call(), 0)
call_4774 = relay.TupleGetItem(func_4375_call(), 0)
func_2506_call = mod.get_global_var('func_2506')
func_2509_call = mutated_mod.get_global_var('func_2509')
var_4781 = relay.var("var_4781", dtype = "float64", shape = (110,))#candidate|4781|(110,)|var|float64
call_4780 = relay.TupleGetItem(func_2506_call(relay.reshape(var_4781.astype('float64'), [2, 11, 5])), 0)
call_4782 = relay.TupleGetItem(func_2509_call(relay.reshape(var_4781.astype('float64'), [2, 11, 5])), 0)
func_4536_call = mod.get_global_var('func_4536')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_4786 = relay.TupleGetItem(func_4536_call(), 1)
call_4787 = relay.TupleGetItem(func_4538_call(), 1)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
var_4801 = relay.var("var_4801", dtype = "int32", shape = (88,))#candidate|4801|(88,)|var|int32
call_4800 = relay.TupleGetItem(func_1055_call(relay.reshape(var_4801.astype('int32'), [88,])), 1)
call_4802 = relay.TupleGetItem(func_1058_call(relay.reshape(var_4801.astype('int32'), [88,])), 1)
func_3142_call = mod.get_global_var('func_3142')
func_3146_call = mutated_mod.get_global_var('func_3146')
const_4806 = relay.const([-8,3,-7,-8,-10,4,1,-2,-7,1,-6,1,1,3,1,3,-2,-3,-9,-2,9,3,-7,2,-4,3,-2,-9,8,-8,2,6,-10,-5,-2,-10,-2,3,-9,-7,-8,2,7,-4,5,-3,5,-3,10,6,6,5,2,-1,-2,6,1,3,-9,-4,-9,3,6,-1,-3,-8,-6,9,2,-10], dtype = "uint16")#candidate|4806|(70,)|const|uint16
var_4807 = relay.var("var_4807", dtype = "uint16", shape = (1050,))#candidate|4807|(1050,)|var|uint16
call_4805 = relay.TupleGetItem(func_3142_call(relay.reshape(const_4806.astype('uint16'), [5, 14, 1]), relay.reshape(var_4807.astype('uint16'), [5, 14, 15]), ), 4)
call_4808 = relay.TupleGetItem(func_3146_call(relay.reshape(const_4806.astype('uint16'), [5, 14, 1]), relay.reshape(var_4807.astype('uint16'), [5, 14, 15]), ), 4)
func_2885_call = mod.get_global_var('func_2885')
func_2886_call = mutated_mod.get_global_var('func_2886')
call_4827 = relay.TupleGetItem(func_2885_call(), 0)
call_4828 = relay.TupleGetItem(func_2886_call(), 0)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_4840 = relay.TupleGetItem(func_3463_call(), 0)
call_4841 = relay.TupleGetItem(func_3465_call(), 0)
func_246_call = mod.get_global_var('func_246')
func_250_call = mutated_mod.get_global_var('func_250')
const_4851 = relay.const([-6,1,-7,-5,2,3,3,7,-9,4,-10,8,1,9,-6,-4,-7,4,2,5,3,-5,-9,4,5,-5,2,-2,5,-2,2,-3,1,-4,-7,8,-8,-8,7,7,9,-8,-9,4,2,5,2,-4,5,7,-9,-4,7,-6,-4,-6,-8,4,7,-1,3,-4,6,-9,7,7,-10,5,-2,2,5,-9,-4,-2,2,-9,-1,-2,-2,2,-7,-5,9,-6,2,-9,8,2,2,3,9,-8,9,-1,-1,10,1,6,-7,3,10,6,1,-10,-4,-6,8,-3,-6,-8,7,-8,7,-10,-6,-6,6,-4,2,1,-8,-8,3,-5,-8,-7,-5,5,6,-6,10,-9,-4,5,-7,-3,-3,3,-2,4,-3,5,3,8,7,4,-8,6,-5,1,9,-7,2,-10,-10,6,-5,-9,-3,2,5,-7,-8,-6,-8,-5,10,1,1,6,-6,-5,3,1,-3,6,-8,2,8,9,6,4,5,5,9,-7,6,-7,-6,-7,-3,8,7,-9,9,-2,-1,10,-4,-2,-10,7,3,-7,4,9,-8,-9,10,-2,6,-5,-2,3,-1,8,-3,7,9,-4,-7,-10,-3,-10,7,-1,7,7,10,7,4,5,10,-3,6,-4,2,2,5,6,5,2,-3,1,-1,-7,4,2,3,-7,-5,-6,6,-4,-9,10,10,-5,-5,8,-5,-10,-8,4,-10,-2,1,5,7,8,-10,9,-2,-2,-1,2,-7,6,7,-9,-3,5,1,3,7,-4,-2,6,-9,3,-1,7,-9,5,7,2,-7,3,-7,7,-8,9,-6,-3,3,7,3,2,-9,6,3,3,7,7,2,7,7,-7,-3,9,10,-2,10,-3,-2,-4,-10,-4,-2,-2,7,4,7,6,-4,6], dtype = "int64")#candidate|4851|(336,)|const|int64
call_4850 = relay.TupleGetItem(func_246_call(relay.reshape(const_4851.astype('int64'), [12, 4, 7]), relay.reshape(const_4851.astype('int64'), [12, 4, 7]), relay.reshape(const_4851.astype('float32'), [12, 4, 7]), ), 0)
call_4852 = relay.TupleGetItem(func_250_call(relay.reshape(const_4851.astype('int64'), [12, 4, 7]), relay.reshape(const_4851.astype('int64'), [12, 4, 7]), relay.reshape(const_4851.astype('float32'), [12, 4, 7]), ), 0)
uop_4863 = relay.sqrt(call_4805.astype('float64')) # shape=(5, 14, 5)
uop_4865 = relay.sqrt(call_4808.astype('float64')) # shape=(5, 14, 5)
output = relay.Tuple([call_4765,call_4773,call_4780,var_4781,call_4786,call_4800,var_4801,const_4806,var_4807,call_4827,call_4840,call_4850,const_4851,uop_4863,])
output2 = relay.Tuple([call_4766,call_4774,call_4782,var_4781,call_4787,call_4802,var_4801,const_4806,var_4807,call_4828,call_4841,call_4852,const_4851,uop_4865,])
func_4866 = relay.Function([var_4781,var_4801,var_4807,], output)
mod['func_4866'] = func_4866
mod = relay.transform.InferType()(mod)
var_4867 = relay.var("var_4867", dtype = "float64", shape = (110,))#candidate|4867|(110,)|var|float64
var_4868 = relay.var("var_4868", dtype = "int32", shape = (88,))#candidate|4868|(88,)|var|int32
var_4869 = relay.var("var_4869", dtype = "uint16", shape = (1050,))#candidate|4869|(1050,)|var|uint16
output = func_4866(var_4867,var_4868,var_4869,)
func_4870 = relay.Function([var_4867,var_4868,var_4869,], output)
mutated_mod['func_4870'] = func_4870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_480_call = mutated_mod.get_global_var('func_480')
call_4907 = relay.TupleGetItem(func_479_call(), 1)
call_4908 = relay.TupleGetItem(func_480_call(), 1)
output = relay.Tuple([call_4907,])
output2 = relay.Tuple([call_4908,])
func_4929 = relay.Function([], output)
mod['func_4929'] = func_4929
mod = relay.transform.InferType()(mod)
output = func_4929()
func_4930 = relay.Function([], output)
mutated_mod['func_4930'] = func_4930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mod.get_global_var('func_1889')
func_1891_call = mutated_mod.get_global_var('func_1891')
call_4988 = relay.TupleGetItem(func_1889_call(), 0)
call_4989 = relay.TupleGetItem(func_1891_call(), 0)
uop_4994 = relay.log2(call_4988.astype('float64')) # shape=(32,)
uop_4996 = relay.log2(call_4989.astype('float64')) # shape=(32,)
output = relay.Tuple([uop_4994,])
output2 = relay.Tuple([uop_4996,])
func_5001 = relay.Function([], output)
mod['func_5001'] = func_5001
mod = relay.transform.InferType()(mod)
mutated_mod['func_5001'] = func_5001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5001_call = mutated_mod.get_global_var('func_5001')
call_5002 = func_5001_call()
output = call_5002
func_5003 = relay.Function([], output)
mutated_mod['func_5003'] = func_5003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3238_call = mod.get_global_var('func_3238')
func_3239_call = mutated_mod.get_global_var('func_3239')
call_5036 = relay.TupleGetItem(func_3238_call(), 1)
call_5037 = relay.TupleGetItem(func_3239_call(), 1)
output = relay.Tuple([call_5036,])
output2 = relay.Tuple([call_5037,])
func_5057 = relay.Function([], output)
mod['func_5057'] = func_5057
mod = relay.transform.InferType()(mod)
output = func_5057()
func_5058 = relay.Function([], output)
mutated_mod['func_5058'] = func_5058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_5106 = relay.TupleGetItem(func_4637_call(), 3)
call_5107 = relay.TupleGetItem(func_4639_call(), 3)
func_4374_call = mod.get_global_var('func_4374')
func_4375_call = mutated_mod.get_global_var('func_4375')
call_5127 = relay.TupleGetItem(func_4374_call(), 0)
call_5128 = relay.TupleGetItem(func_4375_call(), 0)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_5166 = relay.TupleGetItem(func_3463_call(), 0)
call_5167 = relay.TupleGetItem(func_3465_call(), 0)
output = relay.Tuple([call_5106,call_5127,call_5166,])
output2 = relay.Tuple([call_5107,call_5128,call_5167,])
func_5176 = relay.Function([], output)
mod['func_5176'] = func_5176
mod = relay.transform.InferType()(mod)
mutated_mod['func_5176'] = func_5176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5176_call = mutated_mod.get_global_var('func_5176')
call_5177 = func_5176_call()
output = call_5177
func_5178 = relay.Function([], output)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1818_call = mod.get_global_var('func_1818')
func_1820_call = mutated_mod.get_global_var('func_1820')
call_5228 = relay.TupleGetItem(func_1818_call(), 4)
call_5229 = relay.TupleGetItem(func_1820_call(), 4)
func_4395_call = mod.get_global_var('func_4395')
func_4397_call = mutated_mod.get_global_var('func_4397')
call_5259 = relay.TupleGetItem(func_4395_call(), 0)
call_5260 = relay.TupleGetItem(func_4397_call(), 0)
func_1871_call = mod.get_global_var('func_1871')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_5261 = relay.TupleGetItem(func_1871_call(), 0)
call_5262 = relay.TupleGetItem(func_1872_call(), 0)
output = relay.Tuple([call_5228,call_5259,call_5261,])
output2 = relay.Tuple([call_5229,call_5260,call_5262,])
func_5267 = relay.Function([], output)
mod['func_5267'] = func_5267
mod = relay.transform.InferType()(mod)
output = func_5267()
func_5268 = relay.Function([], output)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1271_call = mod.get_global_var('func_1271')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_5296 = relay.TupleGetItem(func_1271_call(), 0)
call_5297 = relay.TupleGetItem(func_1272_call(), 0)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_5298 = relay.TupleGetItem(func_3268_call(), 0)
call_5299 = relay.TupleGetItem(func_3269_call(), 0)
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_5325 = relay.TupleGetItem(func_5176_call(), 0)
call_5326 = relay.TupleGetItem(func_5178_call(), 0)
output = relay.Tuple([call_5296,call_5298,call_5325,])
output2 = relay.Tuple([call_5297,call_5299,call_5326,])
func_5330 = relay.Function([], output)
mod['func_5330'] = func_5330
mod = relay.transform.InferType()(mod)
mutated_mod['func_5330'] = func_5330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5330_call = mutated_mod.get_global_var('func_5330')
call_5331 = func_5330_call()
output = call_5331
func_5332 = relay.Function([], output)
mutated_mod['func_5332'] = func_5332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_5336 = relay.TupleGetItem(func_3463_call(), 0)
call_5337 = relay.TupleGetItem(func_3465_call(), 0)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
var_5349 = relay.var("var_5349", dtype = "int32", shape = (44, 2))#candidate|5349|(44, 2)|var|int32
call_5348 = relay.TupleGetItem(func_2006_call(relay.reshape(var_5349.astype('int32'), [88,])), 0)
call_5350 = relay.TupleGetItem(func_2008_call(relay.reshape(var_5349.astype('int32'), [88,])), 0)
func_1771_call = mod.get_global_var('func_1771')
func_1774_call = mutated_mod.get_global_var('func_1774')
const_5354 = relay.const([[-9,-3,-9,4,-1,6,-2,-10,-2,10,-3,-7,7,-5],[9,4,-4,-8,-8,-9,-3,-10,8,2,8,7,-8,-2],[4,-9,-3,-10,-8,1,1,6,3,-10,5,2,-5,-5],[-5,-8,-4,-3,10,5,-4,-5,-6,-10,8,-9,-2,-6],[-2,-2,8,8,-6,9,6,5,2,-6,2,7,-8,3],[-9,-8,10,8,9,7,6,-5,-2,2,-2,-10,4,2],[-6,-3,4,4,1,-9,7,-10,-4,3,5,9,4,2],[9,-10,-9,-9,-6,6,-6,-10,10,6,-6,9,-4,1],[-10,-6,6,-3,10,-7,-7,-4,9,4,7,-5,-8,-6],[-3,-2,7,3,7,8,9,4,2,9,-5,1,2,6],[-10,-6,-7,-9,8,10,9,-3,-5,4,-8,-9,5,-4],[7,1,-2,2,7,6,1,-1,3,-9,-2,10,-6,-2],[10,-2,-5,2,-9,-7,-6,-2,-8,-9,8,3,-3,-9],[-1,-1,-6,-6,5,-8,-4,3,-7,-9,1,-10,-6,-8],[-6,-7,7,-8,3,5,3,4,-8,9,5,4,6,4],[7,-10,-10,-7,-6,-1,-10,7,-10,3,2,-7,2,5],[-5,1,-3,-2,9,-2,-6,-4,-9,-2,-3,-9,8,4],[-5,-9,7,2,-4,-3,-6,8,7,-10,4,-7,6,-4],[2,-4,6,-7,7,1,6,4,8,-3,5,-3,-5,6],[6,6,7,-5,5,-5,3,-4,1,-10,10,-8,-9,4],[3,7,-3,7,3,4,-8,-2,5,2,4,9,-7,10],[7,-2,-7,10,-2,-9,-3,-4,-2,-1,-2,4,-5,1],[9,-8,9,-7,-8,6,5,4,-10,8,5,-10,-2,-5],[9,-9,-9,-5,6,7,-10,-6,10,-3,-10,-2,-10,-4]], dtype = "int64")#candidate|5354|(24, 14)|const|int64
const_5355 = relay.const([[1.357365,-7.874058],[1.076989,-2.047909],[7.872791,-4.183935],[-5.911455,-9.840027],[0.114157,-4.277505],[-3.234125,-2.311404],[3.681810,2.745588],[7.418925,6.626362],[0.635099,3.921998],[7.433891,-6.561312],[9.273475,-4.649801],[3.861814,-3.108857],[-1.354885,-2.624955],[7.224334,5.987137],[-5.614083,-8.341451],[1.174306,5.536886],[-4.830961,-4.197868],[-1.853146,-1.852307],[6.810546,-5.815832],[5.608477,-2.207731],[7.743547,-3.960370],[5.988152,-8.217918],[-6.308629,2.953514],[-1.507744,-1.999967],[5.289786,-9.557267],[4.235099,9.024622],[8.358729,-4.220610],[8.827853,-0.522220],[2.850958,4.418692],[-1.329965,9.838648],[2.062205,6.129501],[6.285331,-0.321007],[-4.697569,-5.102390],[8.273207,-3.416804],[8.530063,1.471821],[9.628676,-7.013614],[-4.329013,8.598255],[7.865039,1.478028],[9.746015,-0.654581],[5.678596,-6.072371],[4.674583,0.180984],[-0.104918,9.114163],[-6.319881,-8.789217],[7.207665,9.189334],[3.282886,-0.736852],[6.115969,2.948401],[-0.464094,0.235544],[-6.840902,7.396630],[-0.669689,-5.374194],[1.388150,2.922462],[-9.263221,6.783956],[-6.357685,1.162885],[-1.999185,-7.655396],[2.717666,-7.218962],[4.584939,5.101859],[5.940681,3.931487],[-4.158868,3.072613],[1.105789,0.550380],[-6.540737,0.310924],[1.372849,-7.649848],[5.442796,3.328515],[-7.220276,-2.983536],[4.607932,0.414317],[1.136879,4.686064],[-9.470865,9.933268],[4.798606,2.478756],[7.847106,-7.838108],[1.068929,-6.222895],[3.975302,-9.689574],[-8.402111,2.209576],[-1.031148,-1.250296],[3.152218,9.477279],[-1.698383,2.810587],[-2.418046,-4.310790],[-5.615747,-4.669233],[6.053762,-8.374339],[7.312928,0.479269],[0.267204,5.349815],[8.088948,8.496719],[5.932440,5.564245],[6.361447,3.753110],[9.580440,-5.501272],[-7.210762,-8.537992],[6.869542,-6.205480],[8.135603,-3.536350],[-1.684661,-9.895713],[-0.735747,-3.748331],[2.241662,3.433216],[8.507001,-0.574133],[-1.782199,-9.040398],[0.540235,0.117917],[7.111867,4.786196],[9.552843,4.968187],[-6.615203,5.440067],[-9.571538,-6.850076],[0.199984,-9.369255],[6.356198,-6.296192],[7.913063,-6.269877],[0.159243,-3.948379],[-6.557183,0.938385],[4.074850,3.016182],[-2.964043,-2.991026],[9.708816,-7.681682],[5.060680,2.367981],[0.656810,-5.358295],[-9.208918,-5.771634],[-6.764739,-5.776918],[-5.744296,-5.149555],[-2.767233,1.860760],[4.088119,7.933267],[1.159874,1.152233],[7.001893,6.814276],[-6.471235,0.480639],[-1.485377,-1.195799],[-0.560394,8.789399],[-6.697777,7.105268],[-7.606362,-6.716758],[-8.443379,-7.419487],[0.921456,-6.329405],[-9.964944,-4.557181],[-9.022814,6.189339],[5.097127,0.865224],[-6.732413,-9.932128],[0.660824,9.384532],[3.671883,9.445926],[-2.805784,2.039997],[2.017361,-0.442971],[8.862311,4.191353],[-7.296233,-8.717221],[-4.886541,-0.701684],[4.944954,-7.000954],[-4.498426,-4.067835],[2.339846,4.783858],[5.461052,3.964315],[6.917212,-1.352556],[-4.138628,-8.825077],[-3.965724,-9.258399],[-0.607330,7.165017],[-4.651696,-5.461507],[3.058820,-4.031389],[-4.753124,-8.179620],[-4.228434,2.739108],[5.948475,-5.373574],[0.078867,8.270723],[7.442839,-6.310227],[-3.487248,6.701112],[7.586848,7.911348],[-4.112677,4.036644],[2.778419,-7.298976],[-9.059053,0.547220],[9.189276,3.903056],[-0.552488,-8.184905],[6.554339,-2.834757],[-2.559983,-9.525962],[2.593382,6.724106],[4.103905,3.035816]], dtype = "float32")#candidate|5355|(156, 2)|const|float32
call_5353 = relay.TupleGetItem(func_1771_call(relay.reshape(const_5354.astype('int64'), [336,]), relay.reshape(const_5355.astype('float32'), [1, 312]), ), 4)
call_5356 = relay.TupleGetItem(func_1774_call(relay.reshape(const_5354.astype('int64'), [336,]), relay.reshape(const_5355.astype('float32'), [1, 312]), ), 4)
output = relay.Tuple([call_5336,call_5348,var_5349,call_5353,const_5354,const_5355,])
output2 = relay.Tuple([call_5337,call_5350,var_5349,call_5356,const_5354,const_5355,])
func_5360 = relay.Function([var_5349,], output)
mod['func_5360'] = func_5360
mod = relay.transform.InferType()(mod)
var_5361 = relay.var("var_5361", dtype = "int32", shape = (44, 2))#candidate|5361|(44, 2)|var|int32
output = func_5360(var_5361)
func_5362 = relay.Function([var_5361], output)
mutated_mod['func_5362'] = func_5362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5057_call = mod.get_global_var('func_5057')
func_5058_call = mutated_mod.get_global_var('func_5058')
call_5422 = relay.TupleGetItem(func_5057_call(), 0)
call_5423 = relay.TupleGetItem(func_5058_call(), 0)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_5426 = func_294_call()
call_5427 = func_294_call()
output = relay.Tuple([call_5422,call_5426,])
output2 = relay.Tuple([call_5423,call_5427,])
func_5432 = relay.Function([], output)
mod['func_5432'] = func_5432
mod = relay.transform.InferType()(mod)
mutated_mod['func_5432'] = func_5432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5432_call = mutated_mod.get_global_var('func_5432')
call_5433 = func_5432_call()
output = call_5433
func_5434 = relay.Function([], output)
mutated_mod['func_5434'] = func_5434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_5462 = relay.TupleGetItem(func_3331_call(), 0)
call_5463 = relay.TupleGetItem(func_3333_call(), 0)
func_4374_call = mod.get_global_var('func_4374')
func_4375_call = mutated_mod.get_global_var('func_4375')
call_5468 = relay.TupleGetItem(func_4374_call(), 0)
call_5469 = relay.TupleGetItem(func_4375_call(), 0)
output = relay.Tuple([call_5462,call_5468,])
output2 = relay.Tuple([call_5463,call_5469,])
func_5482 = relay.Function([], output)
mod['func_5482'] = func_5482
mod = relay.transform.InferType()(mod)
mutated_mod['func_5482'] = func_5482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5482_call = mutated_mod.get_global_var('func_5482')
call_5483 = func_5482_call()
output = call_5483
func_5484 = relay.Function([], output)
mutated_mod['func_5484'] = func_5484
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5488 = relay.var("var_5488", dtype = "uint8", shape = (16, 4, 14))#candidate|5488|(16, 4, 14)|var|uint8
var_5489 = relay.var("var_5489", dtype = "uint8", shape = (16, 4, 14))#candidate|5489|(16, 4, 14)|var|uint8
bop_5490 = relay.greater(var_5488.astype('bool'), relay.reshape(var_5489.astype('bool'), relay.shape_of(var_5488))) # shape=(16, 4, 14)
bop_5495 = relay.left_shift(bop_5490.astype('uint16'), relay.reshape(var_5489.astype('uint16'), relay.shape_of(bop_5490))) # shape=(16, 4, 14)
output = bop_5495
output2 = bop_5495
func_5507 = relay.Function([var_5488,var_5489,], output)
mod['func_5507'] = func_5507
mod = relay.transform.InferType()(mod)
mutated_mod['func_5507'] = func_5507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5507_call = mutated_mod.get_global_var('func_5507')
var_5509 = relay.var("var_5509", dtype = "uint8", shape = (16, 4, 14))#candidate|5509|(16, 4, 14)|var|uint8
var_5510 = relay.var("var_5510", dtype = "uint8", shape = (16, 4, 14))#candidate|5510|(16, 4, 14)|var|uint8
call_5508 = func_5507_call(var_5509,var_5510,)
output = call_5508
func_5511 = relay.Function([var_5509,var_5510,], output)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1440_call = mod.get_global_var('func_1440')
func_1442_call = mutated_mod.get_global_var('func_1442')
call_5516 = func_1440_call()
call_5517 = func_1440_call()
func_1380_call = mod.get_global_var('func_1380')
func_1382_call = mutated_mod.get_global_var('func_1382')
const_5521 = relay.const([[8.900737,-7.809160,7.513689,3.649257],[7.410761,-9.179658,-3.704166,8.952232],[4.263726,-8.253692,-6.698621,2.043370],[-5.992905,0.011247,2.192915,2.700533],[-9.616450,-3.743074,1.025608,-4.519672],[-2.768838,-1.774481,5.467286,-6.667448],[-7.027905,-7.433476,-9.485699,-2.023197],[-0.714952,6.532396,-1.316609,-7.045371],[-3.790723,-1.099406,3.236723,-8.765780],[3.152135,-2.601519,7.416591,3.399043],[1.404559,-6.427539,-4.273303,-6.417748],[3.149487,-5.002925,2.437078,-8.863933],[4.823647,7.453521,7.632129,4.658091],[-6.545905,4.405167,-4.010511,6.538217],[-6.996814,3.635392,4.771366,-8.162077],[5.431621,-3.349769,4.722524,0.350514],[5.810656,7.006242,-5.211782,-9.073310],[-4.044230,-6.127241,-3.739313,-2.830523],[-3.039577,3.001709,-1.118918,-8.913351],[-6.439893,-7.487366,5.929687,8.786509],[-8.682538,-3.113696,8.429740,1.349900],[-7.084501,-0.476570,0.547329,-4.709969],[4.724086,6.008316,1.131633,0.346091],[-3.199397,4.522724,7.448471,6.981540],[-1.358799,5.893044,-9.495819,1.413480],[-5.627371,4.078900,9.234173,5.930095],[-7.213064,-8.249979,-8.439392,1.247951],[0.370350,8.284930,9.938948,-6.059528],[-1.507711,3.149043,-1.496565,9.222067],[7.867084,-5.552476,-0.609423,0.239001],[1.843470,-9.170499,2.077815,-5.379443],[5.628045,-9.219941,-1.621811,-8.383392],[-7.944790,4.461953,-7.893116,8.406597],[-5.376319,-7.810119,-3.148867,9.354547],[4.913958,2.630629,3.276003,7.741841],[0.360318,-9.080596,-4.018071,-6.061772],[-6.564941,8.356116,2.453265,-5.157656],[4.268552,-6.658044,-7.257967,1.917866],[-3.123986,3.322100,-6.150006,-7.393771],[-7.652925,-4.016851,3.462446,4.694638],[-4.065712,-7.736647,9.399157,9.139937],[-0.839098,-1.667029,1.224522,-8.107672],[5.371750,-7.080328,6.269215,2.772929],[9.808875,-0.978156,3.533171,-5.438864],[3.739442,6.891042,-4.653504,3.191470],[-2.747344,2.952506,4.947874,9.644300],[2.171737,-1.685275,-3.952907,-9.115977],[0.050494,-2.830858,-5.199901,9.036130],[-5.493033,0.043742,9.515162,8.471204],[-0.021569,-2.235663,-6.402108,-7.311177],[6.873626,-2.470114,6.218846,1.161518],[-0.959357,0.196005,-0.841559,-2.347699],[7.401355,9.093028,-7.049592,-0.903445],[-6.871652,-3.400991,4.283122,-9.996280],[1.282380,-4.013677,-9.083352,-3.287436],[-5.172916,8.507102,-8.791666,0.181454],[9.383969,-6.063602,9.038289,2.999300],[1.877699,-4.532293,-5.112680,7.229220],[-5.855815,-8.054372,1.254098,1.216910],[-7.176863,1.299798,-6.343846,-7.431431],[9.422213,5.656461,-6.475455,-8.985742],[-8.150675,-4.333204,-2.652913,-9.171241],[2.372547,4.858261,0.629904,-5.301714],[0.765018,-6.368556,-4.797996,-5.654859],[-5.872702,-9.531102,-1.122213,-8.390348],[-9.048207,6.516159,1.300357,7.867991],[4.965549,9.793904,5.282476,-9.238908],[5.564567,-2.188701,-5.070544,-4.897666],[-4.507423,5.446856,9.112150,3.352313],[-4.061701,-1.981353,-7.886340,-9.344989],[-4.829852,5.989838,-6.637414,8.064799],[-1.199334,4.436158,-2.402277,8.464311],[3.787811,4.387034,8.342707,-8.405504],[1.027592,7.037698,-8.281986,6.303938],[5.910571,-7.583317,8.002141,-3.862398],[7.506769,-3.796017,1.276606,-5.054101],[-6.586773,8.768991,-1.385785,1.157388],[6.676437,5.050437,-6.540449,-8.301569]], dtype = "float32")#candidate|5521|(78, 4)|const|float32
call_5520 = func_1380_call(relay.reshape(const_5521.astype('float32'), [3, 8, 13]))
call_5522 = func_1380_call(relay.reshape(const_5521.astype('float32'), [3, 8, 13]))
func_2606_call = mod.get_global_var('func_2606')
func_2608_call = mutated_mod.get_global_var('func_2608')
call_5561 = relay.TupleGetItem(func_2606_call(), 1)
call_5562 = relay.TupleGetItem(func_2608_call(), 1)
output = relay.Tuple([call_5516,call_5520,const_5521,call_5561,])
output2 = relay.Tuple([call_5517,call_5522,const_5521,call_5562,])
func_5565 = relay.Function([], output)
mod['func_5565'] = func_5565
mod = relay.transform.InferType()(mod)
mutated_mod['func_5565'] = func_5565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5565_call = mutated_mod.get_global_var('func_5565')
call_5566 = func_5565_call()
output = call_5566
func_5567 = relay.Function([], output)
mutated_mod['func_5567'] = func_5567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2606_call = mod.get_global_var('func_2606')
func_2608_call = mutated_mod.get_global_var('func_2608')
call_5604 = relay.TupleGetItem(func_2606_call(), 3)
call_5605 = relay.TupleGetItem(func_2608_call(), 3)
func_3871_call = mod.get_global_var('func_3871')
func_3872_call = mutated_mod.get_global_var('func_3872')
call_5609 = func_3871_call()
call_5610 = func_3871_call()
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_5614 = relay.TupleGetItem(func_3268_call(), 0)
call_5615 = relay.TupleGetItem(func_3269_call(), 0)
output = relay.Tuple([call_5604,call_5609,call_5614,])
output2 = relay.Tuple([call_5605,call_5610,call_5615,])
func_5622 = relay.Function([], output)
mod['func_5622'] = func_5622
mod = relay.transform.InferType()(mod)
output = func_5622()
func_5623 = relay.Function([], output)
mutated_mod['func_5623'] = func_5623
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5653 = relay.var("var_5653", dtype = "int64", shape = (7, 11, 2))#candidate|5653|(7, 11, 2)|var|int64
var_5654 = relay.var("var_5654", dtype = "int64", shape = (7, 11, 2))#candidate|5654|(7, 11, 2)|var|int64
bop_5655 = relay.bitwise_xor(var_5653.astype('int64'), relay.reshape(var_5654.astype('int64'), relay.shape_of(var_5653))) # shape=(7, 11, 2)
uop_5666 = relay.sigmoid(var_5654.astype('float32')) # shape=(7, 11, 2)
var_5668 = relay.var("var_5668", dtype = "int64", shape = (7, 11, 2))#candidate|5668|(7, 11, 2)|var|int64
bop_5669 = relay.logical_and(bop_5655.astype('bool'), relay.reshape(var_5668.astype('bool'), relay.shape_of(bop_5655))) # shape=(7, 11, 2)
func_5482_call = mod.get_global_var('func_5482')
func_5484_call = mutated_mod.get_global_var('func_5484')
call_5687 = relay.TupleGetItem(func_5482_call(), 0)
call_5688 = relay.TupleGetItem(func_5484_call(), 0)
func_5507_call = mod.get_global_var('func_5507')
func_5511_call = mutated_mod.get_global_var('func_5511')
var_5693 = relay.var("var_5693", dtype = "uint8", shape = (896,))#candidate|5693|(896,)|var|uint8
call_5692 = func_5507_call(relay.reshape(var_5693.astype('uint8'), [16, 4, 14]), relay.reshape(var_5693.astype('uint8'), [16, 4, 14]), )
call_5694 = func_5507_call(relay.reshape(var_5693.astype('uint8'), [16, 4, 14]), relay.reshape(var_5693.astype('uint8'), [16, 4, 14]), )
bop_5698 = relay.logical_or(uop_5666.astype('bool'), relay.reshape(var_5654.astype('bool'), relay.shape_of(uop_5666))) # shape=(7, 11, 2)
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
const_5703 = relay.const([[3,-5,7,-1,-5,-6,-10,3,-6,9,-5,-7,-10,-3,10,-5,3,2,-4,-2,2,7,4,9,3,4,-5,-10,6,7,-1,9,-2,5,-3,-5,3,-6,4,-7,-3,8,-1,-2],[10,-5,2,6,-4,-8,-7,2,8,7,5,-10,-6,-6,-5,-6,-8,7,-2,3,-3,2,7,10,-4,-7,2,5,6,-6,10,5,2,9,4,-1,5,6,7,-5,-2,10,-10,5]], dtype = "int32")#candidate|5703|(2, 44)|const|int32
call_5702 = relay.TupleGetItem(func_1055_call(relay.reshape(const_5703.astype('int32'), [88,])), 2)
call_5704 = relay.TupleGetItem(func_1058_call(relay.reshape(const_5703.astype('int32'), [88,])), 2)
uop_5708 = relay.erf(call_5702.astype('float32')) # shape=(11, 10, 8)
uop_5710 = relay.erf(call_5704.astype('float32')) # shape=(11, 10, 8)
bop_5713 = relay.floor_mod(uop_5666.astype('float64'), relay.reshape(bop_5655.astype('float64'), relay.shape_of(uop_5666))) # shape=(7, 11, 2)
func_5360_call = mod.get_global_var('func_5360')
func_5362_call = mutated_mod.get_global_var('func_5362')
call_5722 = relay.TupleGetItem(func_5360_call(relay.reshape(const_5703.astype('int32'), [44, 2])), 4)
call_5723 = relay.TupleGetItem(func_5362_call(relay.reshape(const_5703.astype('int32'), [44, 2])), 4)
func_191_call = mod.get_global_var('func_191')
func_193_call = mutated_mod.get_global_var('func_193')
call_5727 = func_191_call()
call_5728 = func_191_call()
func_4646_call = mod.get_global_var('func_4646')
func_4647_call = mutated_mod.get_global_var('func_4647')
call_5730 = func_4646_call()
call_5731 = func_4646_call()
uop_5749 = relay.sinh(uop_5708.astype('float32')) # shape=(11, 10, 8)
uop_5751 = relay.sinh(uop_5710.astype('float32')) # shape=(11, 10, 8)
func_2533_call = mod.get_global_var('func_2533')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_5756 = relay.TupleGetItem(func_2533_call(), 0)
call_5757 = relay.TupleGetItem(func_2534_call(), 0)
uop_5761 = relay.cos(uop_5708.astype('float32')) # shape=(11, 10, 8)
uop_5763 = relay.cos(uop_5710.astype('float32')) # shape=(11, 10, 8)
output = relay.Tuple([bop_5669,call_5687,call_5692,var_5693,bop_5698,const_5703,bop_5713,call_5722,call_5727,call_5730,uop_5749,call_5756,uop_5761,])
output2 = relay.Tuple([bop_5669,call_5688,call_5694,var_5693,bop_5698,const_5703,bop_5713,call_5723,call_5728,call_5731,uop_5751,call_5757,uop_5763,])
func_5795 = relay.Function([var_5653,var_5654,var_5668,var_5693,], output)
mod['func_5795'] = func_5795
mod = relay.transform.InferType()(mod)
var_5796 = relay.var("var_5796", dtype = "int64", shape = (7, 11, 2))#candidate|5796|(7, 11, 2)|var|int64
var_5797 = relay.var("var_5797", dtype = "int64", shape = (7, 11, 2))#candidate|5797|(7, 11, 2)|var|int64
var_5798 = relay.var("var_5798", dtype = "int64", shape = (7, 11, 2))#candidate|5798|(7, 11, 2)|var|int64
var_5799 = relay.var("var_5799", dtype = "uint8", shape = (896,))#candidate|5799|(896,)|var|uint8
output = func_5795(var_5796,var_5797,var_5798,var_5799,)
func_5800 = relay.Function([var_5796,var_5797,var_5798,var_5799,], output)
mutated_mod['func_5800'] = func_5800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2533_call = mod.get_global_var('func_2533')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_5810 = relay.TupleGetItem(func_2533_call(), 0)
call_5811 = relay.TupleGetItem(func_2534_call(), 0)
func_2506_call = mod.get_global_var('func_2506')
func_2509_call = mutated_mod.get_global_var('func_2509')
const_5847 = relay.const([-4.485514,-2.760534,-4.973349,-2.678530,1.360606,0.179960,-6.497734,-4.351803,-9.329239,-1.689512,-2.925985,8.368549,1.304957,-1.823035,2.724157,-7.017702,9.600270,-4.360641,4.333154,3.590920,-9.975065,3.911134,1.682224,-6.737073,1.339382,9.528648,-8.089999,2.342243,-0.800528,-0.412206,-2.199063,-7.401533,8.982993,9.919149,7.562157,-6.875867,8.374031,-7.176121,8.612103,-3.346555,2.197159,-8.698630,5.860821,9.593810,2.431243,4.489659,-2.773544,3.842340,-7.032686,-8.899727,-8.665567,-0.417895,0.566611,-9.592647,9.180620,8.227396,-1.647020,-8.044866,2.666465,-3.453256,8.482063,-1.149485,6.426541,6.043404,-5.877055,4.744864,-6.742879,1.545796,-1.636395,-6.619764,-1.700419,-4.576861,-3.990780,-3.429225,-0.749365,-6.511241,-2.526563,5.541403,0.518105,-0.397030,-0.031769,-1.922798,2.425252,-8.454910,1.310252,1.514003,-0.548600,2.572652,-8.223470,-7.377261,-3.204164,-4.172880,2.923062,-4.469777,-6.660727,9.344510,-5.971260,-8.467313,0.496220,0.142747,8.430193,-6.716021,-6.468436,-9.130776,-0.016626,5.363389,-1.268876,9.122330,4.452022,-3.140484], dtype = "float64")#candidate|5847|(110,)|const|float64
call_5846 = relay.TupleGetItem(func_2506_call(relay.reshape(const_5847.astype('float64'), [2, 11, 5])), 0)
call_5848 = relay.TupleGetItem(func_2509_call(relay.reshape(const_5847.astype('float64'), [2, 11, 5])), 0)
output = relay.Tuple([call_5810,call_5846,const_5847,])
output2 = relay.Tuple([call_5811,call_5848,const_5847,])
func_5854 = relay.Function([], output)
mod['func_5854'] = func_5854
mod = relay.transform.InferType()(mod)
mutated_mod['func_5854'] = func_5854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5854_call = mutated_mod.get_global_var('func_5854')
call_5855 = func_5854_call()
output = call_5855
func_5856 = relay.Function([], output)
mutated_mod['func_5856'] = func_5856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1871_call = mod.get_global_var('func_1871')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_5857 = relay.TupleGetItem(func_1871_call(), 0)
call_5858 = relay.TupleGetItem(func_1872_call(), 0)
output = relay.Tuple([call_5857,])
output2 = relay.Tuple([call_5858,])
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
func_5001_call = mod.get_global_var('func_5001')
func_5003_call = mutated_mod.get_global_var('func_5003')
call_5896 = relay.TupleGetItem(func_5001_call(), 0)
call_5897 = relay.TupleGetItem(func_5003_call(), 0)
func_5854_call = mod.get_global_var('func_5854')
func_5856_call = mutated_mod.get_global_var('func_5856')
call_5903 = relay.TupleGetItem(func_5854_call(), 1)
call_5904 = relay.TupleGetItem(func_5856_call(), 1)
output = relay.Tuple([call_5896,call_5903,])
output2 = relay.Tuple([call_5897,call_5904,])
func_5910 = relay.Function([], output)
mod['func_5910'] = func_5910
mod = relay.transform.InferType()(mod)
mutated_mod['func_5910'] = func_5910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5910_call = mutated_mod.get_global_var('func_5910')
call_5911 = func_5910_call()
output = call_5911
func_5912 = relay.Function([], output)
mutated_mod['func_5912'] = func_5912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3045_call = mod.get_global_var('func_3045')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_5920 = relay.TupleGetItem(func_3045_call(), 1)
call_5921 = relay.TupleGetItem(func_3047_call(), 1)
output = relay.Tuple([call_5920,])
output2 = relay.Tuple([call_5921,])
func_5928 = relay.Function([], output)
mod['func_5928'] = func_5928
mod = relay.transform.InferType()(mod)
output = func_5928()
func_5929 = relay.Function([], output)
mutated_mod['func_5929'] = func_5929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mod.get_global_var('func_1889')
func_1891_call = mutated_mod.get_global_var('func_1891')
call_5963 = relay.TupleGetItem(func_1889_call(), 0)
call_5964 = relay.TupleGetItem(func_1891_call(), 0)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_5967 = relay.TupleGetItem(func_4501_call(), 0)
call_5968 = relay.TupleGetItem(func_4503_call(), 0)
output = relay.Tuple([call_5963,call_5967,])
output2 = relay.Tuple([call_5964,call_5968,])
func_5975 = relay.Function([], output)
mod['func_5975'] = func_5975
mod = relay.transform.InferType()(mod)
mutated_mod['func_5975'] = func_5975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5975_call = mutated_mod.get_global_var('func_5975')
call_5976 = func_5975_call()
output = call_5976
func_5977 = relay.Function([], output)
mutated_mod['func_5977'] = func_5977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_6014 = relay.TupleGetItem(func_4501_call(), 0)
call_6015 = relay.TupleGetItem(func_4503_call(), 0)
output = call_6014
output2 = call_6015
func_6036 = relay.Function([], output)
mod['func_6036'] = func_6036
mod = relay.transform.InferType()(mod)
output = func_6036()
func_6037 = relay.Function([], output)
mutated_mod['func_6037'] = func_6037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_6049 = func_294_call()
call_6050 = func_294_call()
output = call_6049
output2 = call_6050
func_6053 = relay.Function([], output)
mod['func_6053'] = func_6053
mod = relay.transform.InferType()(mod)
mutated_mod['func_6053'] = func_6053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6053_call = mutated_mod.get_global_var('func_6053')
call_6054 = func_6053_call()
output = call_6054
func_6055 = relay.Function([], output)
mutated_mod['func_6055'] = func_6055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_6062 = relay.TupleGetItem(func_876_call(), 0)
call_6063 = relay.TupleGetItem(func_878_call(), 0)
func_1586_call = mod.get_global_var('func_1586')
func_1588_call = mutated_mod.get_global_var('func_1588')
call_6064 = func_1586_call()
call_6065 = func_1586_call()
output = relay.Tuple([call_6062,call_6064,])
output2 = relay.Tuple([call_6063,call_6065,])
func_6069 = relay.Function([], output)
mod['func_6069'] = func_6069
mod = relay.transform.InferType()(mod)
output = func_6069()
func_6070 = relay.Function([], output)
mutated_mod['func_6070'] = func_6070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3477_call = mod.get_global_var('func_3477')
func_3478_call = mutated_mod.get_global_var('func_3478')
call_6091 = func_3477_call()
call_6092 = func_3477_call()
const_6099 = relay.const([[[-3.227175,8.262993,8.153413,-6.539180,-8.736282,-8.356317,2.678349,-8.465399,-3.833095,-6.250261,5.166962,6.388442,6.267147,7.119097,-5.785619,-8.341960],[-9.120057,0.765572,8.353689,-2.351319,-8.773062,2.599461,0.027222,-8.574608,-7.539462,5.381264,-6.869476,1.747944,8.592908,-9.114205,9.625338,-2.233810],[-8.905056,-4.295233,1.306208,-5.155001,6.471380,6.467797,7.248035,-2.789742,1.820596,-7.937507,-2.137056,4.373727,-1.740763,-5.049367,-4.658697,2.121742],[-9.445862,-8.809734,-8.358791,9.401707,-8.521806,9.049379,4.326271,3.080562,0.783058,-2.612003,-4.325655,3.413109,8.641455,-6.243390,-6.720978,3.692754],[9.142418,-1.490348,-8.486627,-7.539409,1.561474,-0.929684,4.787717,3.561958,7.186842,8.646064,1.221966,-4.775272,-6.794222,-2.459202,-0.678691,7.272709],[-8.143528,-6.732360,7.584895,7.345694,-5.638761,6.127904,-2.789713,-5.993363,-5.903004,2.389817,-4.816716,6.690038,-7.706696,9.233195,7.088571,6.985689]],[[-3.397874,-6.818991,-4.306399,-8.966419,7.324592,-5.292490,-6.544221,-3.167383,-8.318482,-3.598167,6.610926,5.056634,-6.226870,4.797139,3.767336,3.934760],[-1.701237,-0.209195,3.048210,6.847542,-2.170015,-2.018915,-0.922018,-4.103999,-5.915745,0.933430,-3.934968,-1.981854,0.624965,-5.843735,-0.214109,-8.318920],[1.716758,8.700427,-2.191346,7.038889,-2.919473,6.502589,-2.489986,-5.132467,3.517931,3.561395,-3.594215,-0.507567,7.650719,7.206043,-8.199077,-2.241777],[-8.379730,-2.115277,-8.602553,5.949888,-1.441403,8.398073,-9.864224,0.437405,5.619233,8.161639,-9.034018,9.771364,-6.701985,3.434706,-5.368451,-5.979940],[2.951810,8.813287,2.816728,4.958724,-3.758716,-3.796939,-6.170755,-9.048490,-8.387478,5.890134,3.850922,-9.024579,8.470377,-1.280312,9.397958,-3.072523],[6.899822,-7.091074,3.478462,-2.407951,-6.588609,-6.530941,2.539253,-1.590997,2.144327,-3.917017,-4.035940,-5.303142,2.642505,-8.933017,-0.168225,5.803275]],[[-4.304146,-1.773002,5.463212,4.294909,1.296311,-9.591249,-7.485456,9.737059,1.266662,-2.063234,-7.920500,2.582720,4.574759,4.810234,3.090216,-1.710442],[-7.241428,6.385929,3.082106,-3.506505,-6.124894,3.806612,0.554694,-8.506137,1.664703,0.437358,-1.138375,3.696194,-9.732217,0.428679,7.086057,6.859939],[-0.397375,-2.842346,-9.656083,-6.548761,4.607141,3.734427,-9.216955,4.480448,7.087502,-8.183086,-8.331914,4.262274,-8.103894,-9.938226,-6.454419,2.087528],[-4.441805,9.811748,-5.518639,3.778281,6.029553,2.654465,7.538056,0.868112,4.414092,-7.610164,5.583015,-3.015392,-9.037435,-9.390944,-3.269662,9.341369],[4.422576,6.745467,-4.252053,9.365511,-1.214814,-8.160383,-7.101625,-8.615326,7.561399,9.023901,-6.208241,-0.659529,-1.452781,-4.201631,-6.301300,2.983774],[-4.922400,-0.152371,9.565580,-0.983625,-7.710965,0.556136,6.002384,-1.726112,-6.047664,4.499988,2.355493,5.141361,-9.329026,-7.831893,3.399810,-0.491962]],[[7.938558,9.772790,7.545783,-2.027698,-9.362069,-0.256050,8.053500,-3.562051,-7.439876,-7.973362,5.260480,5.470020,5.570569,-3.797073,7.809974,-4.548958],[2.519054,5.701582,-4.690673,-7.924894,-8.366967,-4.804683,0.658336,1.527913,-1.658590,4.244565,-0.606771,-6.093397,7.579128,-4.427464,1.551995,1.602482],[-8.729764,8.216314,-5.162496,9.290719,-0.414266,-6.537302,-4.375796,8.051514,3.813332,-2.481311,8.994969,-1.208313,-8.227125,8.875147,3.249872,-3.807438],[-7.520564,-5.878924,-1.895049,9.420189,5.654744,-3.451089,3.600744,4.553581,8.031303,-1.972746,-6.191824,3.579551,-8.191014,-0.597004,8.315319,6.929683],[2.796137,-5.863961,-3.366289,-2.957866,9.989325,5.199393,4.991599,3.988186,3.353411,2.072610,-4.675891,-8.501130,-4.888964,4.662944,4.060346,0.288440],[-5.834866,-7.700014,0.402645,4.361712,-0.143035,7.052870,8.502364,-5.159549,9.621998,-1.538548,-9.817777,-3.957284,2.080860,-4.407836,-0.941719,2.800613]],[[8.649748,1.001612,3.184094,0.612596,-1.008340,0.953692,9.445111,-2.800950,1.287095,2.915530,7.333788,-7.449170,3.774219,1.756716,-0.600497,-6.702421],[0.173057,-3.981755,-3.062213,-1.736331,1.131607,-3.577420,1.948759,1.540911,5.517289,-6.022034,-0.563790,-1.606585,8.142545,2.476026,-4.865665,6.716869],[-9.103163,-9.823089,4.904534,9.304677,-1.458508,3.083217,-3.656259,5.414456,0.454828,-8.779625,-4.578853,0.552269,-3.021943,-0.540477,4.384970,-4.655279],[0.622815,-7.276742,2.122021,5.194532,-6.979659,4.237319,1.479907,-9.992259,-6.945555,-3.205335,4.430020,-3.354123,1.380702,9.677220,-6.252957,-9.389585],[-1.637377,-3.518263,-7.780531,-0.205882,3.710836,3.162582,-2.961369,3.318688,-4.143678,2.309294,-3.513943,7.223201,-3.866724,-8.716265,3.798405,0.459198],[1.058306,7.800160,6.799708,-6.531746,-1.084692,-0.796547,-8.025862,8.819955,4.187361,-3.805490,4.945307,0.832024,-6.716243,-9.935742,-9.492857,-3.183283]],[[-9.302730,2.547524,8.280718,-3.465991,0.919923,-8.251430,-5.614733,-8.181300,-7.169020,6.417211,7.559562,-8.052357,-0.652467,5.701174,-8.492939,1.344801],[6.939843,-1.982536,-9.727480,-6.356967,1.609034,3.240712,5.201631,-7.163160,3.024738,8.144856,-0.727459,-5.796071,-3.989243,-5.255698,3.258815,7.404045],[-3.443467,7.202297,-1.878381,8.945310,-4.246085,-1.939534,-6.417210,-7.466739,-7.789811,-6.362137,1.010699,-4.087835,-3.982484,-0.882244,-1.753779,8.296909],[4.598178,6.994454,-2.316626,-0.817555,-9.735298,-9.760659,1.372403,-4.350570,-1.709847,-5.756746,5.878659,-4.171849,0.104008,-6.800728,-0.139888,0.636185],[-3.879189,-3.586234,6.156099,-4.934895,5.006145,-3.066925,5.184133,-2.921416,-0.695382,1.200946,3.999713,1.140630,-8.724229,-2.377715,3.127103,-5.160711],[0.531325,0.142201,7.398443,-7.769743,-9.681047,4.831565,0.835650,-2.871631,1.411166,1.490155,8.075137,8.608186,-7.867570,-8.763402,5.064030,-6.515971]],[[1.624594,9.612940,7.334324,4.871067,2.976633,3.841703,4.067580,-5.292129,8.884187,0.694491,-3.988600,-7.879277,6.719443,3.940144,1.026361,6.099278],[1.259930,-4.451070,-9.450051,-4.138572,-1.027655,-8.868899,6.284675,-9.204045,-2.442399,0.877550,4.123161,-4.111493,4.122082,9.828207,9.137027,3.697319],[-5.200612,5.352959,-8.919985,-5.355032,9.424341,-9.815309,9.228213,3.996396,-4.977529,-2.533606,-0.932251,-8.515469,-8.704664,-0.658503,-1.727603,-7.825755],[8.953255,2.872374,-5.754599,9.681651,-4.380860,-5.025755,-1.196036,-2.299171,1.219681,-5.196204,1.862270,7.227531,7.570207,1.285537,8.273931,-4.500441],[2.682495,-5.812455,1.100762,0.527813,6.290872,4.579929,9.894479,6.712190,-8.808090,-8.294891,-9.585807,-8.227444,6.861562,-2.224371,7.086404,-6.730910],[-1.766104,-3.252358,-6.940734,-6.383848,-6.202870,5.839316,1.295013,-9.830779,9.866485,8.024317,-4.118110,8.926074,1.668863,-9.980529,-4.825993,9.769586]],[[-1.707732,-9.754232,4.809142,-6.877035,-7.036397,4.375802,-1.634675,5.028704,-7.024381,-7.967979,-4.247870,-2.760184,7.386610,7.909705,3.307603,-6.577442],[-2.366452,-6.584190,7.088994,4.556184,8.182856,4.107727,-6.804882,7.612329,9.819656,5.679427,4.584309,7.780826,5.639975,-0.949935,7.935006,-7.756948],[4.152274,4.428296,8.557842,-1.116359,7.892372,0.908712,-0.613959,-9.680904,-1.909845,-1.511990,-7.156783,-7.240059,-9.811380,-9.310413,5.795225,6.039459],[-2.350872,-9.658228,-5.367793,-5.064454,-1.158551,6.056442,-7.383656,3.571117,-0.568129,-2.768973,8.298815,-7.289157,3.515637,-3.364583,7.193636,7.522121],[-3.960720,6.962725,-7.458078,6.157163,2.561808,5.126453,-7.650035,-3.319358,-1.627165,7.772955,7.788511,6.026371,3.955977,-9.522963,-8.189303,-7.516866],[2.209663,0.663775,4.704366,-8.705315,5.687730,-8.274806,-8.621949,-3.034459,0.832391,9.658510,1.339007,4.622670,-0.660022,9.597577,9.181957,5.872245]],[[-3.792446,-5.468127,5.800994,-0.886234,-5.081645,9.099328,-0.423084,-9.628113,7.774471,-0.241076,-6.112339,7.431365,6.854185,4.016687,-1.247219,5.825802],[6.962354,-5.972389,0.518068,-5.521134,7.589959,-7.026236,2.638257,1.731981,-2.682807,-2.904431,6.354599,5.227047,-6.426514,0.355500,-1.399787,3.247220],[-1.902447,-9.825304,6.197489,-4.798207,-4.232763,-1.143339,4.388669,7.681848,4.354686,-0.885214,9.409601,-4.555689,8.795947,2.454056,-7.446288,0.875158],[-4.219538,-7.585035,-5.202790,3.997748,-7.875432,0.764228,9.110698,3.912452,-1.694495,-7.890841,-1.668066,6.112088,-7.515303,2.132439,-6.696850,-6.987704],[-9.741086,-7.213048,5.279829,-2.287330,4.091347,3.200195,-6.535061,3.829147,-8.678363,-2.913091,-7.475029,-7.991468,-2.836866,-6.551013,8.430991,-1.269856],[4.077829,-6.862883,-8.266281,-7.260411,-8.280656,-9.295752,1.284141,3.762637,1.211912,-3.642594,-2.495862,5.426003,-5.582039,2.262481,-9.465164,0.605758]],[[-7.663807,-1.930529,-9.678518,-3.655852,-8.721292,0.352781,-6.451253,7.588507,8.011187,-0.731514,8.648703,-8.867765,4.405038,2.980356,6.843923,0.087405],[-4.988563,-4.816600,0.817016,-6.599130,-6.423659,0.959551,-1.454652,-7.180304,-6.837212,0.339367,-9.571042,3.453977,7.286425,8.329574,6.701366,-1.299190],[-2.880561,6.498351,2.211841,3.858778,0.663614,7.210865,-9.410547,7.648933,-5.952798,-6.382723,6.103001,-8.441230,-1.647190,7.911995,-3.387912,8.093549],[3.737527,-3.441855,-3.442743,-3.810523,-1.194230,-1.550096,1.748569,7.556592,-0.838244,0.114673,0.233323,2.225395,6.872887,-5.913154,-8.720675,8.353159],[-4.963797,3.678415,2.970591,-1.242353,4.691231,-7.423772,3.490819,-2.036580,9.447770,4.230447,1.655660,-1.624589,9.869812,-3.662551,9.522931,8.943507],[-9.887449,-4.882073,-6.614761,5.069943,2.414834,7.712722,-6.115382,0.027204,6.715926,-3.358086,1.644520,9.468417,5.111155,-9.449664,3.130971,-6.568797]],[[-2.951448,-4.150201,-6.662861,-5.452686,9.381910,-8.245138,7.680490,-3.233641,-4.039815,7.656941,6.686256,-9.974896,3.372876,2.529148,7.121493,-9.332534],[3.770726,-9.997390,-8.443851,7.581723,-8.653136,4.391985,7.487994,-2.962890,1.775091,4.165483,6.251789,6.554162,7.983032,5.269246,0.739202,-1.251342],[-9.222205,-9.248581,-3.613096,5.627243,1.443814,-2.853704,-9.777728,-0.002703,0.299925,-6.043829,3.647904,2.784923,4.173857,0.366163,-3.218768,8.009787],[9.778913,4.736974,2.349242,-1.757068,-2.725343,-4.115999,-5.974847,-2.958080,-4.048487,-1.719059,-1.636365,-9.481090,-2.782159,-6.652678,-8.196009,-6.072062],[3.873326,2.158179,-1.670948,6.021934,-7.081299,7.052597,-7.764488,-9.670746,-8.588499,2.530440,-7.349016,-7.774826,6.425743,4.022071,-6.678387,5.213660],[-3.662248,9.222933,9.841539,2.848918,-4.203083,-5.796109,-3.035532,1.011061,7.018817,6.046848,0.894222,-3.701354,2.422761,-6.473197,1.773150,2.946233]],[[-8.143915,-5.489803,-8.605031,1.897219,-0.519059,1.839359,9.578058,-8.044375,9.067674,-3.931893,5.455656,-3.174273,6.167979,1.422018,-2.470532,-4.010120],[5.553398,-6.613714,-8.873387,-5.499295,6.068513,2.912146,-8.823508,8.088498,5.098884,-9.634066,3.403462,0.733152,9.739612,9.515512,-7.587298,-4.460965],[7.767604,5.501503,0.155807,-6.831861,4.658511,1.049885,3.477235,-2.300055,-3.898877,-4.085119,8.373742,-4.057747,-2.317777,-5.191692,5.467073,-8.473328],[-9.689391,-7.630971,7.296919,-8.806431,-3.751500,-9.971860,7.464223,3.608842,-2.913536,1.924887,8.980166,-4.756715,3.767738,-4.885315,-6.466454,6.454829],[-7.629632,-5.455949,5.050699,6.211627,-0.139016,3.176810,-3.188144,1.557960,-8.731796,-0.022815,5.588298,5.233210,2.489023,1.601637,-5.990330,-1.495525],[6.277206,-2.454991,-0.190268,-1.852820,-1.377539,-2.743735,-2.458779,2.281623,-5.109865,8.999264,-7.150931,-4.294529,-6.204548,9.476170,3.423784,-0.884751]],[[-1.906456,5.075791,-8.781563,4.383939,6.502584,6.745865,-9.455077,0.629294,-8.123749,-4.058693,5.463910,-6.050100,-2.732531,4.334705,-7.571982,-5.416706],[-4.005474,7.554697,-8.416996,0.154592,-1.952246,2.249335,4.360897,6.600898,8.231606,8.773252,-2.710689,7.316900,5.351478,-1.559786,-5.141930,0.275158],[-0.934693,4.499550,3.115052,7.694578,3.837796,-2.256770,8.456670,-7.366685,4.248577,0.625328,5.769273,2.423893,3.957323,-5.758618,-2.442219,0.916609],[-6.724946,0.134219,8.793396,2.264303,-2.399084,-6.731599,4.272532,-4.851846,-5.017537,5.153892,-1.718528,-0.223591,-0.364759,5.880024,-3.349631,-9.556984],[1.085002,1.560697,-5.578146,7.770038,-8.084495,-7.269218,-4.531485,3.101868,-7.613658,2.437325,8.407064,7.179771,-6.632715,-9.599172,6.839776,-5.648454],[4.488425,5.829762,-5.710666,-9.452425,-7.396947,7.107554,4.701162,2.256620,4.835158,4.781010,4.083063,-9.368911,4.753079,-2.090427,7.035910,-8.182819]],[[-5.149039,-1.380388,-0.089631,-4.178728,0.548663,-9.734944,-2.129620,0.972029,-2.768087,-1.563521,6.244753,1.995961,0.535115,9.954296,-4.107048,8.433730],[8.755785,-6.679068,-5.074146,2.440867,-6.285029,7.566992,7.332886,-5.953657,5.089118,9.427082,3.890282,5.107410,6.783074,-0.318440,-9.490050,-6.984074],[4.583841,-0.969065,0.741376,-0.463875,9.448374,-6.508277,-4.802188,-7.760980,5.761375,-5.361596,-5.457961,-3.937688,-2.467158,-6.644327,-6.369494,-5.439237],[8.733622,-0.174200,-0.725991,-9.298693,-6.072781,9.287508,1.348718,-0.098919,0.483131,9.767346,-0.997791,9.877413,-6.426991,-4.233922,2.289180,1.045116],[1.977668,9.299669,-2.514120,0.530259,1.834373,7.852038,-3.024801,3.448666,-5.126689,6.897731,-0.313529,6.981975,-9.911595,-4.471776,-3.092445,-3.642228],[4.269314,-3.906547,7.157536,-7.462582,-3.134623,2.868018,8.103144,-5.479964,-7.085136,-7.958998,3.746228,1.071158,9.234866,1.081272,2.453818,1.036157]]], dtype = "float32")#candidate|6099|(14, 6, 16)|const|float32
bop_6100 = relay.logical_and(call_6091.astype('bool'), relay.reshape(const_6099.astype('bool'), relay.shape_of(call_6091))) # shape=(14, 6, 16)
bop_6103 = relay.logical_and(call_6092.astype('bool'), relay.reshape(const_6099.astype('bool'), relay.shape_of(call_6092))) # shape=(14, 6, 16)
output = bop_6100
output2 = bop_6103
func_6104 = relay.Function([], output)
mod['func_6104'] = func_6104
mod = relay.transform.InferType()(mod)
mutated_mod['func_6104'] = func_6104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6104_call = mutated_mod.get_global_var('func_6104')
call_6105 = func_6104_call()
output = call_6105
func_6106 = relay.Function([], output)
mutated_mod['func_6106'] = func_6106
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6113 = relay.var("var_6113", dtype = "float32", shape = (2, 5, 14))#candidate|6113|(2, 5, 14)|var|float32
uop_6114 = relay.asin(var_6113.astype('float32')) # shape=(2, 5, 14)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_6118 = func_294_call()
call_6119 = func_294_call()
var_6122 = relay.var("var_6122", dtype = "float32", shape = (2, 5, 14))#candidate|6122|(2, 5, 14)|var|float32
bop_6123 = relay.mod(uop_6114.astype('float64'), relay.reshape(var_6122.astype('float64'), relay.shape_of(uop_6114))) # shape=(2, 5, 14)
bop_6127 = relay.floor_divide(var_6113.astype('float64'), relay.reshape(bop_6123.astype('float64'), relay.shape_of(var_6113))) # shape=(2, 5, 14)
output = relay.Tuple([call_6118,bop_6127,])
output2 = relay.Tuple([call_6119,bop_6127,])
func_6132 = relay.Function([var_6113,var_6122,], output)
mod['func_6132'] = func_6132
mod = relay.transform.InferType()(mod)
mutated_mod['func_6132'] = func_6132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6132_call = mutated_mod.get_global_var('func_6132')
var_6134 = relay.var("var_6134", dtype = "float32", shape = (2, 5, 14))#candidate|6134|(2, 5, 14)|var|float32
var_6135 = relay.var("var_6135", dtype = "float32", shape = (2, 5, 14))#candidate|6135|(2, 5, 14)|var|float32
call_6133 = func_6132_call(var_6134,var_6135,)
output = call_6133
func_6136 = relay.Function([var_6134,var_6135,], output)
mutated_mod['func_6136'] = func_6136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_6146 = relay.TupleGetItem(func_4637_call(), 0)
call_6147 = relay.TupleGetItem(func_4639_call(), 0)
func_5910_call = mod.get_global_var('func_5910')
func_5912_call = mutated_mod.get_global_var('func_5912')
call_6156 = relay.TupleGetItem(func_5910_call(), 1)
call_6157 = relay.TupleGetItem(func_5912_call(), 1)
var_6162 = relay.var("var_6162", dtype = "float32", shape = (2, 11, 5))#candidate|6162|(2, 11, 5)|var|float32
bop_6163 = relay.minimum(call_6156.astype('int64'), relay.reshape(var_6162.astype('int64'), relay.shape_of(call_6156))) # shape=(2, 11, 5)
bop_6166 = relay.minimum(call_6157.astype('int64'), relay.reshape(var_6162.astype('int64'), relay.shape_of(call_6157))) # shape=(2, 11, 5)
func_5928_call = mod.get_global_var('func_5928')
func_5929_call = mutated_mod.get_global_var('func_5929')
call_6176 = relay.TupleGetItem(func_5928_call(), 0)
call_6177 = relay.TupleGetItem(func_5929_call(), 0)
output = relay.Tuple([call_6146,bop_6163,call_6176,])
output2 = relay.Tuple([call_6147,bop_6166,call_6177,])
func_6180 = relay.Function([var_6162,], output)
mod['func_6180'] = func_6180
mod = relay.transform.InferType()(mod)
mutated_mod['func_6180'] = func_6180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6181 = relay.var("var_6181", dtype = "float32", shape = (2, 11, 5))#candidate|6181|(2, 11, 5)|var|float32
func_6180_call = mutated_mod.get_global_var('func_6180')
call_6182 = func_6180_call(var_6181)
output = call_6182
func_6183 = relay.Function([var_6181], output)
mutated_mod['func_6183'] = func_6183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1581_call = mutated_mod.get_global_var('func_1581')
call_6203 = relay.TupleGetItem(func_1580_call(), 4)
call_6204 = relay.TupleGetItem(func_1581_call(), 4)
output = call_6203
output2 = call_6204
func_6209 = relay.Function([], output)
mod['func_6209'] = func_6209
mod = relay.transform.InferType()(mod)
mutated_mod['func_6209'] = func_6209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6209_call = mutated_mod.get_global_var('func_6209')
call_6210 = func_6209_call()
output = call_6210
func_6211 = relay.Function([], output)
mutated_mod['func_6211'] = func_6211
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6220 = relay.var("var_6220", dtype = "float64", shape = (13, 8, 5))#candidate|6220|(13, 8, 5)|var|float64
var_6221 = relay.var("var_6221", dtype = "float64", shape = (13, 8, 5))#candidate|6221|(13, 8, 5)|var|float64
bop_6222 = relay.mod(var_6220.astype('float64'), relay.reshape(var_6221.astype('float64'), relay.shape_of(var_6220))) # shape=(13, 8, 5)
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_6250 = relay.TupleGetItem(func_5176_call(), 2)
call_6251 = relay.TupleGetItem(func_5178_call(), 2)
uop_6255 = relay.cosh(var_6221.astype('float32')) # shape=(13, 8, 5)
output = relay.Tuple([bop_6222,call_6250,uop_6255,])
output2 = relay.Tuple([bop_6222,call_6251,uop_6255,])
func_6261 = relay.Function([var_6220,var_6221,], output)
mod['func_6261'] = func_6261
mod = relay.transform.InferType()(mod)
mutated_mod['func_6261'] = func_6261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6261_call = mutated_mod.get_global_var('func_6261')
var_6263 = relay.var("var_6263", dtype = "float64", shape = (13, 8, 5))#candidate|6263|(13, 8, 5)|var|float64
var_6264 = relay.var("var_6264", dtype = "float64", shape = (13, 8, 5))#candidate|6264|(13, 8, 5)|var|float64
call_6262 = func_6261_call(var_6263,var_6264,)
output = call_6262
func_6265 = relay.Function([var_6263,var_6264,], output)
mutated_mod['func_6265'] = func_6265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1586_call = mod.get_global_var('func_1586')
func_1588_call = mutated_mod.get_global_var('func_1588')
call_6348 = func_1586_call()
call_6349 = func_1586_call()
func_3613_call = mod.get_global_var('func_3613')
func_3614_call = mutated_mod.get_global_var('func_3614')
call_6360 = func_3613_call()
call_6361 = func_3613_call()
func_3871_call = mod.get_global_var('func_3871')
func_3872_call = mutated_mod.get_global_var('func_3872')
call_6364 = func_3871_call()
call_6365 = func_3871_call()
func_4154_call = mod.get_global_var('func_4154')
func_4156_call = mutated_mod.get_global_var('func_4156')
call_6367 = func_4154_call()
call_6368 = func_4154_call()
uop_6373 = relay.sigmoid(call_6348.astype('float64')) # shape=(14, 6, 16)
uop_6375 = relay.sigmoid(call_6349.astype('float64')) # shape=(14, 6, 16)
output = relay.Tuple([call_6360,call_6364,call_6367,uop_6373,])
output2 = relay.Tuple([call_6361,call_6365,call_6368,uop_6375,])
func_6391 = relay.Function([], output)
mod['func_6391'] = func_6391
mod = relay.transform.InferType()(mod)
output = func_6391()
func_6392 = relay.Function([], output)
mutated_mod['func_6392'] = func_6392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_6440 = relay.TupleGetItem(func_1232_call(), 0)
call_6441 = relay.TupleGetItem(func_1233_call(), 0)
uop_6442 = relay.rsqrt(call_6440.astype('float64')) # shape=(14, 6, 16)
uop_6444 = relay.rsqrt(call_6441.astype('float64')) # shape=(14, 6, 16)
func_1232_call = mod.get_global_var('func_1232')
func_1233_call = mutated_mod.get_global_var('func_1233')
call_6445 = relay.TupleGetItem(func_1232_call(), 0)
call_6446 = relay.TupleGetItem(func_1233_call(), 0)
func_3979_call = mod.get_global_var('func_3979')
func_3981_call = mutated_mod.get_global_var('func_3981')
call_6453 = func_3979_call()
call_6454 = func_3979_call()
func_435_call = mod.get_global_var('func_435')
func_438_call = mutated_mod.get_global_var('func_438')
call_6456 = relay.TupleGetItem(func_435_call(relay.reshape(call_6453.astype('float32'), [14, 6, 16]), relay.reshape(call_6440.astype('float32'), [14, 6, 16]), ), 4)
call_6457 = relay.TupleGetItem(func_438_call(relay.reshape(call_6453.astype('float32'), [14, 6, 16]), relay.reshape(call_6440.astype('float32'), [14, 6, 16]), ), 4)
func_3871_call = mod.get_global_var('func_3871')
func_3872_call = mutated_mod.get_global_var('func_3872')
call_6461 = func_3871_call()
call_6462 = func_3871_call()
func_4929_call = mod.get_global_var('func_4929')
func_4930_call = mutated_mod.get_global_var('func_4930')
call_6466 = relay.TupleGetItem(func_4929_call(), 0)
call_6467 = relay.TupleGetItem(func_4930_call(), 0)
func_692_call = mod.get_global_var('func_692')
func_694_call = mutated_mod.get_global_var('func_694')
call_6471 = relay.TupleGetItem(func_692_call(relay.reshape(call_6445.astype('float32'), [14, 6, 16])), 1)
call_6472 = relay.TupleGetItem(func_694_call(relay.reshape(call_6445.astype('float32'), [14, 6, 16])), 1)
output = relay.Tuple([uop_6442,call_6445,call_6453,call_6456,call_6461,call_6466,call_6471,])
output2 = relay.Tuple([uop_6444,call_6446,call_6454,call_6457,call_6462,call_6467,call_6472,])
func_6475 = relay.Function([], output)
mod['func_6475'] = func_6475
mod = relay.transform.InferType()(mod)
mutated_mod['func_6475'] = func_6475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6475_call = mutated_mod.get_global_var('func_6475')
call_6476 = func_6475_call()
output = call_6476
func_6477 = relay.Function([], output)
mutated_mod['func_6477'] = func_6477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2533_call = mod.get_global_var('func_2533')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_6525 = relay.TupleGetItem(func_2533_call(), 0)
call_6526 = relay.TupleGetItem(func_2534_call(), 0)
output = relay.Tuple([call_6525,])
output2 = relay.Tuple([call_6526,])
func_6528 = relay.Function([], output)
mod['func_6528'] = func_6528
mod = relay.transform.InferType()(mod)
mutated_mod['func_6528'] = func_6528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6528_call = mutated_mod.get_global_var('func_6528')
call_6529 = func_6528_call()
output = call_6529
func_6530 = relay.Function([], output)
mutated_mod['func_6530'] = func_6530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6069_call = mod.get_global_var('func_6069')
func_6070_call = mutated_mod.get_global_var('func_6070')
call_6557 = relay.TupleGetItem(func_6069_call(), 1)
call_6558 = relay.TupleGetItem(func_6070_call(), 1)
output = call_6557
output2 = call_6558
func_6573 = relay.Function([], output)
mod['func_6573'] = func_6573
mod = relay.transform.InferType()(mod)
mutated_mod['func_6573'] = func_6573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6573_call = mutated_mod.get_global_var('func_6573')
call_6574 = func_6573_call()
output = call_6574
func_6575 = relay.Function([], output)
mutated_mod['func_6575'] = func_6575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5910_call = mod.get_global_var('func_5910')
func_5912_call = mutated_mod.get_global_var('func_5912')
call_6584 = relay.TupleGetItem(func_5910_call(), 0)
call_6585 = relay.TupleGetItem(func_5912_call(), 0)
output = call_6584
output2 = call_6585
func_6600 = relay.Function([], output)
mod['func_6600'] = func_6600
mod = relay.transform.InferType()(mod)
mutated_mod['func_6600'] = func_6600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6600_call = mutated_mod.get_global_var('func_6600')
call_6601 = func_6600_call()
output = call_6601
func_6602 = relay.Function([], output)
mutated_mod['func_6602'] = func_6602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1871_call = mod.get_global_var('func_1871')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_6618 = relay.TupleGetItem(func_1871_call(), 0)
call_6619 = relay.TupleGetItem(func_1872_call(), 0)
func_1150_call = mod.get_global_var('func_1150')
func_1152_call = mutated_mod.get_global_var('func_1152')
call_6622 = relay.TupleGetItem(func_1150_call(), 2)
call_6623 = relay.TupleGetItem(func_1152_call(), 2)
output = relay.Tuple([call_6618,call_6622,])
output2 = relay.Tuple([call_6619,call_6623,])
func_6634 = relay.Function([], output)
mod['func_6634'] = func_6634
mod = relay.transform.InferType()(mod)
mutated_mod['func_6634'] = func_6634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6634_call = mutated_mod.get_global_var('func_6634')
call_6635 = func_6634_call()
output = call_6635
func_6636 = relay.Function([], output)
mutated_mod['func_6636'] = func_6636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1871_call = mod.get_global_var('func_1871')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_6648 = relay.TupleGetItem(func_1871_call(), 0)
call_6649 = relay.TupleGetItem(func_1872_call(), 0)
output = relay.Tuple([call_6648,])
output2 = relay.Tuple([call_6649,])
func_6654 = relay.Function([], output)
mod['func_6654'] = func_6654
mod = relay.transform.InferType()(mod)
mutated_mod['func_6654'] = func_6654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6654_call = mutated_mod.get_global_var('func_6654')
call_6655 = func_6654_call()
output = call_6655
func_6656 = relay.Function([], output)
mutated_mod['func_6656'] = func_6656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6673 = relay.var("var_6673", dtype = "float32", shape = (9, 15, 16))#candidate|6673|(9, 15, 16)|var|float32
uop_6674 = relay.log(var_6673.astype('float32')) # shape=(9, 15, 16)
uop_6706 = relay.atanh(uop_6674.astype('float32')) # shape=(9, 15, 16)
output = uop_6706
output2 = uop_6706
func_6709 = relay.Function([var_6673,], output)
mod['func_6709'] = func_6709
mod = relay.transform.InferType()(mod)
var_6710 = relay.var("var_6710", dtype = "float32", shape = (9, 15, 16))#candidate|6710|(9, 15, 16)|var|float32
output = func_6709(var_6710)
func_6711 = relay.Function([var_6710], output)
mutated_mod['func_6711'] = func_6711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1818_call = mod.get_global_var('func_1818')
func_1820_call = mutated_mod.get_global_var('func_1820')
call_6723 = relay.TupleGetItem(func_1818_call(), 2)
call_6724 = relay.TupleGetItem(func_1820_call(), 2)
output = relay.Tuple([call_6723,])
output2 = relay.Tuple([call_6724,])
func_6739 = relay.Function([], output)
mod['func_6739'] = func_6739
mod = relay.transform.InferType()(mod)
mutated_mod['func_6739'] = func_6739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mutated_mod.get_global_var('func_6739')
call_6740 = func_6739_call()
output = call_6740
func_6741 = relay.Function([], output)
mutated_mod['func_6741'] = func_6741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3979_call = mod.get_global_var('func_3979')
func_3981_call = mutated_mod.get_global_var('func_3981')
call_6762 = func_3979_call()
call_6763 = func_3979_call()
output = relay.Tuple([call_6762,])
output2 = relay.Tuple([call_6763,])
func_6777 = relay.Function([], output)
mod['func_6777'] = func_6777
mod = relay.transform.InferType()(mod)
output = func_6777()
func_6778 = relay.Function([], output)
mutated_mod['func_6778'] = func_6778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5432_call = mod.get_global_var('func_5432')
func_5434_call = mutated_mod.get_global_var('func_5434')
call_6811 = relay.TupleGetItem(func_5432_call(), 1)
call_6812 = relay.TupleGetItem(func_5434_call(), 1)
output = relay.Tuple([call_6811,])
output2 = relay.Tuple([call_6812,])
func_6821 = relay.Function([], output)
mod['func_6821'] = func_6821
mod = relay.transform.InferType()(mod)
mutated_mod['func_6821'] = func_6821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6821_call = mutated_mod.get_global_var('func_6821')
call_6822 = func_6821_call()
output = call_6822
func_6823 = relay.Function([], output)
mutated_mod['func_6823'] = func_6823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_813_call = mutated_mod.get_global_var('func_813')
call_6829 = relay.TupleGetItem(func_811_call(), 2)
call_6830 = relay.TupleGetItem(func_813_call(), 2)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_6844 = relay.TupleGetItem(func_4501_call(), 0)
call_6845 = relay.TupleGetItem(func_4503_call(), 0)
output = relay.Tuple([call_6829,call_6844,])
output2 = relay.Tuple([call_6830,call_6845,])
func_6848 = relay.Function([], output)
mod['func_6848'] = func_6848
mod = relay.transform.InferType()(mod)
output = func_6848()
func_6849 = relay.Function([], output)
mutated_mod['func_6849'] = func_6849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_6850 = relay.TupleGetItem(func_2153_call(), 1)
call_6851 = relay.TupleGetItem(func_2155_call(), 1)
output = relay.Tuple([call_6850,])
output2 = relay.Tuple([call_6851,])
func_6885 = relay.Function([], output)
mod['func_6885'] = func_6885
mod = relay.transform.InferType()(mod)
mutated_mod['func_6885'] = func_6885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6885_call = mutated_mod.get_global_var('func_6885')
call_6886 = func_6885_call()
output = call_6886
func_6887 = relay.Function([], output)
mutated_mod['func_6887'] = func_6887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4646_call = mod.get_global_var('func_4646')
func_4647_call = mutated_mod.get_global_var('func_4647')
call_6896 = func_4646_call()
call_6897 = func_4646_call()
func_5565_call = mod.get_global_var('func_5565')
func_5567_call = mutated_mod.get_global_var('func_5567')
call_6925 = relay.TupleGetItem(func_5565_call(), 3)
call_6926 = relay.TupleGetItem(func_5567_call(), 3)
func_1369_call = mod.get_global_var('func_1369')
func_1372_call = mutated_mod.get_global_var('func_1372')
var_6938 = relay.var("var_6938", dtype = "float32", shape = (585,))#candidate|6938|(585,)|var|float32
call_6937 = relay.TupleGetItem(func_1369_call(relay.reshape(var_6938.astype('float32'), [13, 15, 3])), 1)
call_6939 = relay.TupleGetItem(func_1372_call(relay.reshape(var_6938.astype('float32'), [13, 15, 3])), 1)
output = relay.Tuple([call_6896,call_6925,call_6937,var_6938,])
output2 = relay.Tuple([call_6897,call_6926,call_6939,var_6938,])
func_6950 = relay.Function([var_6938,], output)
mod['func_6950'] = func_6950
mod = relay.transform.InferType()(mod)
mutated_mod['func_6950'] = func_6950
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6951 = relay.var("var_6951", dtype = "float32", shape = (585,))#candidate|6951|(585,)|var|float32
func_6950_call = mutated_mod.get_global_var('func_6950')
call_6952 = func_6950_call(var_6951)
output = call_6952
func_6953 = relay.Function([var_6951], output)
mutated_mod['func_6953'] = func_6953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_813_call = mutated_mod.get_global_var('func_813')
call_6968 = relay.TupleGetItem(func_811_call(), 1)
call_6969 = relay.TupleGetItem(func_813_call(), 1)
output = call_6968
output2 = call_6969
func_6976 = relay.Function([], output)
mod['func_6976'] = func_6976
mod = relay.transform.InferType()(mod)
output = func_6976()
func_6977 = relay.Function([], output)
mutated_mod['func_6977'] = func_6977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4646_call = mod.get_global_var('func_4646')
func_4647_call = mutated_mod.get_global_var('func_4647')
call_6978 = func_4646_call()
call_6979 = func_4646_call()
output = call_6978
output2 = call_6979
func_6989 = relay.Function([], output)
mod['func_6989'] = func_6989
mod = relay.transform.InferType()(mod)
mutated_mod['func_6989'] = func_6989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6989_call = mutated_mod.get_global_var('func_6989')
call_6990 = func_6989_call()
output = call_6990
func_6991 = relay.Function([], output)
mutated_mod['func_6991'] = func_6991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_6998 = relay.TupleGetItem(func_4536_call(), 1)
call_6999 = relay.TupleGetItem(func_4538_call(), 1)
output = relay.Tuple([call_6998,])
output2 = relay.Tuple([call_6999,])
func_7002 = relay.Function([], output)
mod['func_7002'] = func_7002
mod = relay.transform.InferType()(mod)
mutated_mod['func_7002'] = func_7002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7002_call = mutated_mod.get_global_var('func_7002')
call_7003 = func_7002_call()
output = call_7003
func_7004 = relay.Function([], output)
mutated_mod['func_7004'] = func_7004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_294_call = mod.get_global_var('func_294')
func_296_call = mutated_mod.get_global_var('func_296')
call_7029 = func_294_call()
call_7030 = func_294_call()
uop_7033 = relay.cosh(call_7029.astype('float32')) # shape=(14, 6, 16)
uop_7035 = relay.cosh(call_7030.astype('float32')) # shape=(14, 6, 16)
output = relay.Tuple([uop_7033,])
output2 = relay.Tuple([uop_7035,])
func_7066 = relay.Function([], output)
mod['func_7066'] = func_7066
mod = relay.transform.InferType()(mod)
mutated_mod['func_7066'] = func_7066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7066_call = mutated_mod.get_global_var('func_7066')
call_7067 = func_7066_call()
output = call_7067
func_7068 = relay.Function([], output)
mutated_mod['func_7068'] = func_7068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1150_call = mod.get_global_var('func_1150')
func_1152_call = mutated_mod.get_global_var('func_1152')
call_7092 = relay.TupleGetItem(func_1150_call(), 3)
call_7093 = relay.TupleGetItem(func_1152_call(), 3)
output = call_7092
output2 = call_7093
func_7094 = relay.Function([], output)
mod['func_7094'] = func_7094
mod = relay.transform.InferType()(mod)
output = func_7094()
func_7095 = relay.Function([], output)
mutated_mod['func_7095'] = func_7095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3717_call = mod.get_global_var('func_3717')
func_3718_call = mutated_mod.get_global_var('func_3718')
call_7098 = func_3717_call()
call_7099 = func_3717_call()
func_3979_call = mod.get_global_var('func_3979')
func_3981_call = mutated_mod.get_global_var('func_3981')
call_7104 = func_3979_call()
call_7105 = func_3979_call()
output = relay.Tuple([call_7098,call_7104,])
output2 = relay.Tuple([call_7099,call_7105,])
func_7124 = relay.Function([], output)
mod['func_7124'] = func_7124
mod = relay.transform.InferType()(mod)
mutated_mod['func_7124'] = func_7124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7124_call = mutated_mod.get_global_var('func_7124')
call_7125 = func_7124_call()
output = call_7125
func_7126 = relay.Function([], output)
mutated_mod['func_7126'] = func_7126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7192 = relay.var("var_7192", dtype = "float64", shape = (1, 3, 4))#candidate|7192|(1, 3, 4)|var|float64
uop_7193 = relay.erf(var_7192.astype('float64')) # shape=(1, 3, 4)
bop_7195 = relay.power(var_7192.astype('float64'), relay.reshape(uop_7193.astype('float64'), relay.shape_of(var_7192))) # shape=(1, 3, 4)
var_7198 = relay.var("var_7198", dtype = "float64", shape = (9, 3, 4))#candidate|7198|(9, 3, 4)|var|float64
bop_7199 = relay.multiply(uop_7193.astype('int8'), var_7198.astype('int8')) # shape=(9, 3, 4)
uop_7203 = relay.tan(bop_7199.astype('float64')) # shape=(9, 3, 4)
output = relay.Tuple([bop_7195,uop_7203,])
output2 = relay.Tuple([bop_7195,uop_7203,])
func_7219 = relay.Function([var_7192,var_7198,], output)
mod['func_7219'] = func_7219
mod = relay.transform.InferType()(mod)
var_7220 = relay.var("var_7220", dtype = "float64", shape = (1, 3, 4))#candidate|7220|(1, 3, 4)|var|float64
var_7221 = relay.var("var_7221", dtype = "float64", shape = (9, 3, 4))#candidate|7221|(9, 3, 4)|var|float64
output = func_7219(var_7220,var_7221,)
func_7222 = relay.Function([var_7220,var_7221,], output)
mutated_mod['func_7222'] = func_7222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1150_call = mod.get_global_var('func_1150')
func_1152_call = mutated_mod.get_global_var('func_1152')
call_7344 = relay.TupleGetItem(func_1150_call(), 4)
call_7345 = relay.TupleGetItem(func_1152_call(), 4)
func_2440_call = mod.get_global_var('func_2440')
func_2443_call = mutated_mod.get_global_var('func_2443')
const_7350 = relay.const([[-9.435680,1.687876],[-4.856222,9.219464],[7.510932,-2.128374],[-6.764295,7.913678],[4.097405,-3.277375],[-6.987922,0.392796],[-3.197291,-8.963375],[4.969229,7.417911]], dtype = "float64")#candidate|7350|(8, 2)|const|float64
call_7349 = relay.TupleGetItem(func_2440_call(relay.reshape(const_7350.astype('float64'), [8, 2, 1])), 0)
call_7351 = relay.TupleGetItem(func_2443_call(relay.reshape(const_7350.astype('float64'), [8, 2, 1])), 0)
output = relay.Tuple([call_7344,call_7349,const_7350,])
output2 = relay.Tuple([call_7345,call_7351,const_7350,])
func_7380 = relay.Function([], output)
mod['func_7380'] = func_7380
mod = relay.transform.InferType()(mod)
output = func_7380()
func_7381 = relay.Function([], output)
mutated_mod['func_7381'] = func_7381
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7402 = relay.var("var_7402", dtype = "float32", shape = (4, 2))#candidate|7402|(4, 2)|var|float32
uop_7403 = relay.asinh(var_7402.astype('float32')) # shape=(4, 2)
uop_7423 = relay.exp(uop_7403.astype('float64')) # shape=(4, 2)
func_5432_call = mod.get_global_var('func_5432')
func_5434_call = mutated_mod.get_global_var('func_5434')
call_7426 = relay.TupleGetItem(func_5432_call(), 1)
call_7427 = relay.TupleGetItem(func_5434_call(), 1)
func_1421_call = mod.get_global_var('func_1421')
func_1423_call = mutated_mod.get_global_var('func_1423')
var_7450 = relay.var("var_7450", dtype = "float32", shape = (162, 6))#candidate|7450|(162, 6)|var|float32
call_7449 = relay.TupleGetItem(func_1421_call(relay.reshape(var_7450.astype('float32'), [9, 9, 12])), 0)
call_7451 = relay.TupleGetItem(func_1423_call(relay.reshape(var_7450.astype('float32'), [9, 9, 12])), 0)
func_4668_call = mod.get_global_var('func_4668')
func_4670_call = mutated_mod.get_global_var('func_4670')
var_7454 = relay.var("var_7454", dtype = "int64", shape = (324,))#candidate|7454|(324,)|var|int64
call_7453 = relay.TupleGetItem(func_4668_call(relay.reshape(var_7454.astype('int64'), [3, 12, 9])), 0)
call_7455 = relay.TupleGetItem(func_4670_call(relay.reshape(var_7454.astype('int64'), [3, 12, 9])), 0)
func_4717_call = mod.get_global_var('func_4717')
func_4720_call = mutated_mod.get_global_var('func_4720')
const_7457 = relay.const([-3.897602,5.979598,2.446644,9.492542,-5.300636,6.336187,3.377548,-3.606058,8.778557,6.314365,7.996872,3.020324,-8.758211,-0.385258,-5.389320,-2.289176,2.810165,-2.382900,3.783802,4.496488,6.639332,3.366454,2.419357,5.490143,-0.766343,1.406054,-2.428802,-2.461857,-2.496561,-5.256351,4.804191,3.494352,-3.526096,3.645770,6.809982,7.352047,8.331094,-3.647931,7.912226,-3.643842,-0.297713,6.708811,-3.427962,-7.968200,-6.800646,5.996330,2.207053,7.848306,-1.004418,5.652906,3.893808,-8.187190,0.651886,-0.799344,-5.213322,-7.215113,-8.857112,5.452786,9.008612,7.628736,-6.109752,7.819651,8.142994,1.614043,5.604783,-5.832381,-7.109195,-6.043763,9.212269,-9.796903,3.361283,-1.081381,-8.823513,-8.304978,4.523176,4.990353,-8.898622,9.683271,8.755622,7.261357,3.243494,-0.258280,-7.207122,2.328696,6.773634,8.284389,-6.724556,-9.164571,6.477077,6.653609,-2.805834,-2.755288,8.107792,-3.117418,-3.660591,-7.052189,2.944617,7.401399,4.842209,9.310859,-9.070094,9.183858,4.305971,7.439627,-9.529158,6.595765,-4.913613,7.839668,-1.305364,-2.639879,6.219382,-0.301776,2.927190,-3.294743,8.222136,2.210751,-4.730521,-1.329983,-2.506850,-1.524582,-3.437828,7.982682,5.412747,8.231449,9.110430,-0.896966,-8.161262,3.764745,8.466685,-3.583222,-9.770789,-0.370806,-7.566193,-7.762168,2.993078,4.891387,-9.633482,-0.782759,7.483663,1.547348,6.232132,4.240151,4.330433,-3.160852,-2.675655,3.423025,-9.007366,0.185027,-0.972420,-5.149993,-3.251680,-1.097863,-5.681119,-7.295747,-8.166762,-4.099793,0.141139,7.412391,3.582870,2.463376,-9.553839,-9.438095,7.560990,6.835903,0.778399,8.275915,7.059622,-5.144746,-5.191080,1.515069,8.020514,-1.297801,5.587451,9.962500,5.321043,-0.482292,2.782058,1.400656,-0.950994,-5.610443,-0.907857,7.093020,6.947942,7.390279,-8.345020,-3.158197,8.818088,-4.170032,-6.368546,3.456732,5.237650,5.382204,-0.203616,0.081529,8.661469,-3.113281,0.241114,0.113933,2.123049,-0.971446,1.978005,7.863038,0.903515,5.907501,6.212689,-6.061380,-9.692646,1.360822,-4.801025,1.594474,2.222225,2.958372,0.071410,9.958857,0.333005,-3.955842,8.794483,9.138421,-8.810054,-4.070976,4.010769,-8.247119,9.667764,-5.557013,-3.592524,5.144419,1.885336,-3.380705,-7.403420,-1.779338,8.045719,-3.093269,-9.100325,6.390696,4.030648,9.566125,-7.265299,-4.639004,7.155858,9.019546,8.826644,3.401327,6.088597,1.698586,-7.922831,-5.546048,2.947484,-9.638550,-5.858800,-7.970162,3.860586,2.247527,3.487782,0.749224,-4.914040,-5.908916,-1.873526,1.809738,6.538357,8.711958,-7.089801,7.692572,-9.903213,6.156957,0.911281,-4.475888,9.540727,4.453998,-8.371537,-6.280412,3.775906,-5.915004,-5.120541,-4.574897,-7.783715,2.120651,5.531142,-7.671782,-4.004902,-9.453935,3.919685,7.969326,-1.701054,9.654460,7.092518,-4.817554,-1.001887,-5.166398,-9.184039,-7.090418,-8.958247,1.887877,-1.587052,-3.560272,1.322929,6.348984,6.629565,-0.719615,1.176104,-5.590643,3.403654,1.883126,6.768660,-9.075469,-2.426552,2.896657,7.369450,-4.273120,-5.048746,-2.147900,-3.581396,7.344386,-1.461769,3.709668,6.170184,4.677914,-5.987636,5.473842,-2.279629,1.227643,-1.099546,-6.401007,0.501535,-2.106434,9.212354,-2.618119,-8.729912,6.817651,7.917641,-4.236720,1.956786,5.696679,-7.057273,3.473245,-4.698516,-5.611813,0.757609,-5.237124,5.305673,1.179631,-5.098406,-6.454027,0.919325,9.767427,1.678252,8.643352,1.556683,-9.678160,5.249534,1.204641,7.478111,0.694768,-6.897489,2.857046,-6.411473,-1.673823,-9.130372,0.639130,-9.841361,-7.831901,-5.602709,-2.373776,-4.535820,5.405659,3.257238,-2.719710,-7.323838,7.704792,4.932512,5.179568,6.139122,-8.003700,-4.588237,7.508286,8.498791,-1.362912,-2.721345,3.734225,-4.452869,-9.117282,5.300364,-6.490657,-4.155282,-6.135450,-9.979857,7.379898,9.754384,-2.906558,6.706578,0.397251,8.297058,-4.966744,-0.511348,0.779747,2.990730,-8.877142,-5.017154,-8.670677,0.965461,-3.094125,-4.771518,0.694610,-4.815854,-5.561683,-8.870744,-6.918420,8.686362,1.545146,-7.577513,-6.888619,-5.004501,3.472291,6.285708,-5.400724,-2.014441,3.448564,-4.815124,3.149723,-9.216805,9.345344,9.169458,-4.572674,-4.773639,-5.489858,-4.958754,-2.816954,-2.529872,6.789544,-0.477214,-7.042961,9.053267,8.557578,-3.965238,-2.803301,-8.865794,3.004963,8.075786,8.071268,9.044468,-5.175582,-0.778066,0.091487,-9.995398,9.234376,-7.631536,-4.145936,1.407633,5.391765,-7.956196,-7.504919,7.014143,-4.275531,0.707787,5.480483,3.807551,9.968433,-3.760293,-3.504341,1.373459,3.346849,4.971193,9.359866,-0.709628,1.164264,-4.713263,7.984936,3.880228,-3.236966,5.899090,-8.806427,-3.992632,7.783498,-2.221511,5.697845,8.690153,7.337151,-8.086766,4.999708,7.725167,0.398447,-3.946565,-3.360419,-7.619828,-3.740059,-1.765827,0.544489,-0.968033,4.210322,-1.355396,0.456273,-4.367255,7.187323,8.825764,7.987191,8.459774,5.621348,6.879019,5.597765,-8.451422,-3.179380,-6.060388,0.602628,-0.793379,6.241685,-3.008768,-6.405244,5.743314,6.770059,-1.671168,-7.753645,-7.676245,2.253126,5.570241,9.558640,-7.705632,-8.980262,8.476949,-2.214939,-9.372263,3.706035,-9.340553,3.291656,7.827099,-8.419442,0.276116,8.581776,-6.873263,-9.058756,1.685753,-8.604236,5.275313,6.713525,-8.565374,-0.359476,9.898670,3.430124,2.011331,-3.720993,-7.934105,-9.492195,3.504233,9.681343,-7.456808,2.073445,6.919883,3.410135,-2.293384,-9.350992,-4.249384,8.947282,-1.278726,5.537554,-8.472858,-5.075666,1.064618,-4.762339,-5.342679,-3.646684,2.338399,-8.470183,0.401553,4.988479,-1.221965,4.009629,-6.195479,9.292291,8.733675,-9.440323,-5.796685,-8.419271,7.030879,-8.823692,-5.770476,-8.692633,-6.505168,3.727900,0.451792,8.134789,-6.581907,-7.984354,6.529586,8.159369,0.416996,-6.121815,-7.955976,0.872756,-3.829104,9.265834,-8.281859,-2.519957,-3.636655,0.671532,7.399263,-2.138171,4.294207,-5.678961,-3.652186,4.366146,-8.293723,2.356849,2.376296,-9.842922,-2.777783,-1.340909,-2.011414,5.998334,-3.781609,-0.177446,9.417712,1.375176,5.307707,1.536328,2.199585,4.416352,2.134166,-0.007053,1.989176,-1.805210,-3.112174,7.594643,0.460587,-3.670993,7.354781,2.539714,3.071259,0.372055,2.660999,-5.104358,7.193391,-7.980284,-8.039211,1.289535,5.681789,9.351533,6.230200,-2.251236,8.004372,-7.582236,5.573450,5.764524,8.691076,-9.323194,0.595225,8.615613,-5.636399,6.758404,4.408790,6.892301,-0.173860,-5.252134,3.403671,3.715860,5.685875,1.365108,7.545369,1.617391,9.960383,4.337695,-6.781648,2.743748,-4.394798,8.122974,-7.623537,8.468949,9.697615,-3.053123,-3.558514,5.832491,0.818396,3.637910,2.808378,6.836549], dtype = "float64")#candidate|7457|(672,)|const|float64
call_7456 = relay.TupleGetItem(func_4717_call(relay.reshape(const_7457.astype('float64'), [12, 14, 4]), relay.reshape(call_7426.astype('float32'), [1344,]), ), 0)
call_7458 = relay.TupleGetItem(func_4720_call(relay.reshape(const_7457.astype('float64'), [12, 14, 4]), relay.reshape(call_7426.astype('float32'), [1344,]), ), 0)
uop_7473 = relay.asin(uop_7423.astype('float32')) # shape=(4, 2)
var_7477 = relay.var("var_7477", dtype = "float64", shape = (672,))#candidate|7477|(672,)|var|float64
bop_7478 = relay.equal(const_7457.astype('bool'), relay.reshape(var_7477.astype('bool'), relay.shape_of(const_7457))) # shape=(672,)
func_1369_call = mod.get_global_var('func_1369')
func_1372_call = mutated_mod.get_global_var('func_1372')
const_7491 = relay.const([-3.305657,-0.539055,4.782748,4.389608,-3.777943,3.610478,4.610981,6.985386,-2.007136,-2.490421,5.362023,-2.889990,7.127447,-9.950153,8.896423,2.599109,-0.480663,1.767166,0.474933,-0.925249,6.256518,-2.967560,5.443546,-8.638284,5.671640,-2.678021,6.451413,7.253744,7.215914,6.289724,0.206596,-2.823432,-0.194369,-7.746811,8.755681,5.361419,-1.949543,9.711380,-3.955851,-9.590023,-6.477374,-3.638053,4.684793,-6.059236,-2.656685,6.330814,6.424216,7.635707,4.099550,3.959969,-7.188986,-3.155684,-4.178960,-2.579282,6.728057,6.825642,-7.055898,-1.395566,6.025969,-9.779462,-0.368383,4.049087,2.655598,-3.710807,-0.068136,1.329391,-8.978133,-8.491852,1.850153,1.745670,4.037812,5.647225,7.781713,0.957074,-8.615858,-0.575975,1.831013,-8.075282,-3.772443,5.816072,8.860969,6.062504,-5.542591,-8.565975,0.894555,5.397178,-1.961530,-4.765661,-0.450625,-2.091952,2.354882,5.011133,0.572045,3.889126,-3.989261,-3.404995,-9.265132,-6.961290,2.799079,-2.290298,-4.936453,6.664301,-5.571995,-7.975134,0.116155,-4.359208,4.532605,8.985137,9.983085,-7.166195,-8.559092,8.734019,5.089278,3.910169,8.162392,8.894493,8.542846,-4.105787,-9.618466,-6.945388,-0.103745,-8.982875,6.321414,-3.021628,-4.550653,-3.901341,6.006904,9.142486,7.777714,-6.876080,8.288030,6.935528,-5.691248,-3.471207,-8.169274,1.098061,6.136839,6.032121,2.563117,-2.912609,-2.458343,-6.749210,-7.018528,-7.581456,6.438287,-7.207946,-6.786028,1.220977,-7.572215,1.384749,1.266011,1.452563,-5.727929,5.295491,-2.094321,-8.462196,-8.482148,-3.945854,-3.524729,7.935712,0.790203,-6.974957,3.804541,7.140512,-1.707317,-3.927072,1.899068,-6.467349,-9.968243,5.699718,0.057867,-3.083301,6.754461,3.451448,2.028271,5.983580,-7.699366,4.873770,5.973046,6.918604,0.666521,5.871169,4.273711,0.280996,2.412345,-1.244207,-2.148704,7.649918,-7.881625,0.867295,4.772735,-2.516713,5.556148,9.103835,-8.852408,-3.852667,-2.462697,-3.531710,9.857125,-9.355680,8.257730,-0.177988,3.958692,5.876497,-6.635629,8.954376,9.870537,2.089974,7.414491,6.157978,-6.872697,-5.569471,-5.208564,-2.142511,-6.787911,-6.086571,-7.406983,5.285281,-7.779789,2.513820,6.847730,-5.029071,-2.963233,9.559609,-1.549861,-6.666698,-6.017887,-5.469111,3.697088,8.261927,7.658811,6.081295,-0.382936,4.271233,0.658381,1.616872,6.618444,4.211468,8.619148,-4.239679,-7.690051,-1.803810,0.875401,8.092845,-3.813404,-3.894983,-9.116853,4.993158,-3.444016,-7.735953,5.353957,-8.835975,0.646605,-7.887834,5.333211,6.633441,2.296081,-5.539025,-8.956341,-8.988644,-3.105759,-7.330652,-3.739163,7.797214,-7.748934,7.465004,4.075244,-0.383694,5.959892,-4.408206,6.723582,-2.106009,4.029553,4.029067,-6.767062,-6.730676,-6.710817,-3.226632,-7.995713,0.780090,3.847105,-4.663896,2.706730,6.569426,-0.239968,8.745150,4.210977,-6.025015,-9.128218,-0.162892,8.546040,-4.835348,2.522996,7.986441,-3.631766,-5.085617,5.601177,6.705339,-5.744969,0.369379,-4.860720,-9.560782,2.556262,-8.980867,7.286549,-5.654242,-9.594479,-0.275832,1.856244,6.362845,7.124832,3.686361,8.087016,8.630772,-7.293284,-0.473621,0.572744,-1.758313,4.205180,-2.217594,-9.407227,-0.965768,0.319360,-0.066825,-3.713630,4.721179,-6.279010,-2.854547,3.659941,9.501511,-0.319380,-1.382057,-5.360732,-8.180516,8.264103,-2.299109,-0.782053,-0.396715,-9.024253,-7.292731,4.618539,-8.665360,9.610520,6.791295,-6.829066,-9.196816,-9.891263,-2.664555,3.330746,-8.912258,0.585858,-4.881294,4.820510,-4.541100,-7.609059,-2.878645,-5.011431,0.700145,9.776624,-6.093314,0.445022,4.743956,2.206391,-4.318343,-8.135341,1.855825,-1.844942,9.307079,6.945015,7.338583,5.349671,9.486686,-0.210957,5.255073,9.166616,9.125407,-3.457527,-6.499503,-8.070060,-3.670416,3.038790,-7.447053,-0.937408,-5.646648,9.184365,9.608561,2.155958,-2.177355,3.199088,-5.026642,3.112281,4.752525,-8.249355,4.131006,-4.855078,4.523850,-0.433673,7.741439,-7.064905,-9.033108,2.050811,-6.495121,-0.284484,-4.939783,-2.971150,-0.220991,-5.744726,6.266222,3.154207,6.646448,-9.016531,7.226144,6.154081,9.594723,-2.836399,8.572500,3.699236,0.543518,8.987187,3.935733,-5.854859,8.013154,0.604147,4.100783,-9.695783,7.966753,5.659381,4.713527,5.655566,-4.103920,-8.964816,-0.238433,0.903165,0.705681,0.536578,-1.798045,-5.734313,8.211263,-6.746752,-9.182805,5.385739,-1.529869,-2.650813,4.583370,-2.335304,-9.496054,-1.841805,0.857486,-3.904933,-3.370643,1.507386,9.891055,-1.401726,-6.948017,4.640153,5.796463,-8.005326,0.818554,5.604637,-7.472039,2.837607,-5.741977,1.530023,5.335801,-0.612123,-5.941099,8.749623,2.668336,-0.664405,-1.059813,-0.783539,-1.071842,2.030281,-4.350949,5.142077,6.363831,9.857600,-2.644728,6.310771,-1.149470,0.768629,4.963193,-5.670739,-2.461295,-6.840298,-9.380005,0.723649,5.234109,-2.364200,1.463238,5.746755,-9.390728,9.182355,4.322250,9.060589,-5.386182,-8.073142,9.419904,6.917780,8.949674,-7.320444,-1.012348,7.630110,3.351223,4.469483,6.928700,9.077431,2.031107,-8.597987,8.857868,-4.209795,-5.280083,8.510289,1.862085,4.598000,4.480234,-0.341312,5.434667,3.837280,-7.282296,-2.110665,1.924280,6.818393,-5.353953,-6.903145,8.764234,7.932656,1.432972,4.298824,6.073467,-6.991829,3.133117,1.237718,-9.275689,3.016958,5.060357,-7.971808,5.407748,-9.949870,4.349497,8.783323,0.515753,-2.127627,5.588750,-3.495189,-4.862087,8.162055,5.909949,4.527497,-3.697216,-5.319954,-7.067729,-2.486727,0.836036,8.497817,9.940273,8.399100,0.106221,-5.612469,-9.909150,-3.720329,4.267082,-8.884725,-0.806353,-7.817591,-8.165154,-4.054277,0.550776,-8.400406,2.206670,6.389027,-5.913110,-2.854461,-6.396608,-7.566187,9.766728,3.420126,5.079859,4.492892,5.268029,-8.140423,4.427242,-7.183330,3.680181,5.269128], dtype = "float32")#candidate|7491|(585,)|const|float32
call_7490 = relay.TupleGetItem(func_1369_call(relay.reshape(const_7491.astype('float32'), [13, 15, 3])), 0)
call_7492 = relay.TupleGetItem(func_1372_call(relay.reshape(const_7491.astype('float32'), [13, 15, 3])), 0)
output = relay.Tuple([call_7426,call_7449,var_7450,call_7453,var_7454,call_7456,uop_7473,bop_7478,call_7490,const_7491,])
output2 = relay.Tuple([call_7427,call_7451,var_7450,call_7455,var_7454,call_7458,uop_7473,bop_7478,call_7492,const_7491,])
func_7503 = relay.Function([var_7402,var_7450,var_7454,var_7477,], output)
mod['func_7503'] = func_7503
mod = relay.transform.InferType()(mod)
var_7504 = relay.var("var_7504", dtype = "float32", shape = (4, 2))#candidate|7504|(4, 2)|var|float32
var_7505 = relay.var("var_7505", dtype = "float32", shape = (162, 6))#candidate|7505|(162, 6)|var|float32
var_7506 = relay.var("var_7506", dtype = "int64", shape = (324,))#candidate|7506|(324,)|var|int64
var_7507 = relay.var("var_7507", dtype = "float64", shape = (672,))#candidate|7507|(672,)|var|float64
output = func_7503(var_7504,var_7505,var_7506,var_7507,)
func_7508 = relay.Function([var_7504,var_7505,var_7506,var_7507,], output)
mutated_mod['func_7508'] = func_7508
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7517 = relay.var("var_7517", dtype = "float32", shape = (1, 12, 7))#candidate|7517|(1, 12, 7)|var|float32
uop_7518 = relay.log10(var_7517.astype('float32')) # shape=(1, 12, 7)
output = relay.Tuple([uop_7518,])
output2 = relay.Tuple([uop_7518,])
func_7520 = relay.Function([var_7517,], output)
mod['func_7520'] = func_7520
mod = relay.transform.InferType()(mod)
var_7521 = relay.var("var_7521", dtype = "float32", shape = (1, 12, 7))#candidate|7521|(1, 12, 7)|var|float32
output = func_7520(var_7521)
func_7522 = relay.Function([var_7521], output)
mutated_mod['func_7522'] = func_7522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_7534 = relay.TupleGetItem(func_5267_call(), 1)
call_7535 = relay.TupleGetItem(func_5268_call(), 1)
func_4374_call = mod.get_global_var('func_4374')
func_4375_call = mutated_mod.get_global_var('func_4375')
call_7560 = relay.TupleGetItem(func_4374_call(), 0)
call_7561 = relay.TupleGetItem(func_4375_call(), 0)
output = relay.Tuple([call_7534,call_7560,])
output2 = relay.Tuple([call_7535,call_7561,])
func_7565 = relay.Function([], output)
mod['func_7565'] = func_7565
mod = relay.transform.InferType()(mod)
output = func_7565()
func_7566 = relay.Function([], output)
mutated_mod['func_7566'] = func_7566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2044_call = mod.get_global_var('func_2044')
func_2045_call = mutated_mod.get_global_var('func_2045')
call_7593 = relay.TupleGetItem(func_2044_call(), 1)
call_7594 = relay.TupleGetItem(func_2045_call(), 1)
output = call_7593
output2 = call_7594
func_7612 = relay.Function([], output)
mod['func_7612'] = func_7612
mod = relay.transform.InferType()(mod)
mutated_mod['func_7612'] = func_7612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7612_call = mutated_mod.get_global_var('func_7612')
call_7613 = func_7612_call()
output = call_7613
func_7614 = relay.Function([], output)
mutated_mod['func_7614'] = func_7614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6634_call = mod.get_global_var('func_6634')
func_6636_call = mutated_mod.get_global_var('func_6636')
call_7632 = relay.TupleGetItem(func_6634_call(), 1)
call_7633 = relay.TupleGetItem(func_6636_call(), 1)
func_3238_call = mod.get_global_var('func_3238')
func_3239_call = mutated_mod.get_global_var('func_3239')
call_7642 = relay.TupleGetItem(func_3238_call(), 1)
call_7643 = relay.TupleGetItem(func_3239_call(), 1)
output = relay.Tuple([call_7632,call_7642,])
output2 = relay.Tuple([call_7633,call_7643,])
func_7656 = relay.Function([], output)
mod['func_7656'] = func_7656
mod = relay.transform.InferType()(mod)
output = func_7656()
func_7657 = relay.Function([], output)
mutated_mod['func_7657'] = func_7657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7749 = relay.var("var_7749", dtype = "bool", shape = (12, 13, 9))#candidate|7749|(12, 13, 9)|var|bool
var_7750 = relay.var("var_7750", dtype = "bool", shape = (12, 13, 9))#candidate|7750|(12, 13, 9)|var|bool
bop_7751 = relay.logical_and(var_7749.astype('bool'), relay.reshape(var_7750.astype('bool'), relay.shape_of(var_7749))) # shape=(12, 13, 9)
output = relay.Tuple([bop_7751,])
output2 = relay.Tuple([bop_7751,])
func_7758 = relay.Function([var_7749,var_7750,], output)
mod['func_7758'] = func_7758
mod = relay.transform.InferType()(mod)
mutated_mod['func_7758'] = func_7758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7758_call = mutated_mod.get_global_var('func_7758')
var_7760 = relay.var("var_7760", dtype = "bool", shape = (12, 13, 9))#candidate|7760|(12, 13, 9)|var|bool
var_7761 = relay.var("var_7761", dtype = "bool", shape = (12, 13, 9))#candidate|7761|(12, 13, 9)|var|bool
call_7759 = func_7758_call(var_7760,var_7761,)
output = call_7759
func_7762 = relay.Function([var_7760,var_7761,], output)
mutated_mod['func_7762'] = func_7762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mod.get_global_var('func_1889')
func_1891_call = mutated_mod.get_global_var('func_1891')
call_7773 = relay.TupleGetItem(func_1889_call(), 0)
call_7774 = relay.TupleGetItem(func_1891_call(), 0)
output = call_7773
output2 = call_7774
func_7806 = relay.Function([], output)
mod['func_7806'] = func_7806
mod = relay.transform.InferType()(mod)
output = func_7806()
func_7807 = relay.Function([], output)
mutated_mod['func_7807'] = func_7807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2044_call = mod.get_global_var('func_2044')
func_2045_call = mutated_mod.get_global_var('func_2045')
call_7810 = relay.TupleGetItem(func_2044_call(), 1)
call_7811 = relay.TupleGetItem(func_2045_call(), 1)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_7836 = relay.TupleGetItem(func_4637_call(), 2)
call_7837 = relay.TupleGetItem(func_4639_call(), 2)
output = relay.Tuple([call_7810,call_7836,])
output2 = relay.Tuple([call_7811,call_7837,])
func_7849 = relay.Function([], output)
mod['func_7849'] = func_7849
mod = relay.transform.InferType()(mod)
mutated_mod['func_7849'] = func_7849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7849_call = mutated_mod.get_global_var('func_7849')
call_7850 = func_7849_call()
output = call_7850
func_7851 = relay.Function([], output)
mutated_mod['func_7851'] = func_7851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6600_call = mod.get_global_var('func_6600')
func_6602_call = mutated_mod.get_global_var('func_6602')
call_7866 = func_6600_call()
call_7867 = func_6600_call()
func_6573_call = mod.get_global_var('func_6573')
func_6575_call = mutated_mod.get_global_var('func_6575')
call_7873 = func_6573_call()
call_7874 = func_6573_call()
func_4461_call = mod.get_global_var('func_4461')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_7886 = relay.TupleGetItem(func_4461_call(), 0)
call_7887 = relay.TupleGetItem(func_4462_call(), 0)
output = relay.Tuple([call_7866,call_7873,call_7886,])
output2 = relay.Tuple([call_7867,call_7874,call_7887,])
func_7895 = relay.Function([], output)
mod['func_7895'] = func_7895
mod = relay.transform.InferType()(mod)
output = func_7895()
func_7896 = relay.Function([], output)
mutated_mod['func_7896'] = func_7896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_7899 = relay.TupleGetItem(func_4501_call(), 1)
call_7900 = relay.TupleGetItem(func_4503_call(), 1)
func_7895_call = mod.get_global_var('func_7895')
func_7896_call = mutated_mod.get_global_var('func_7896')
call_7908 = relay.TupleGetItem(func_7895_call(), 0)
call_7909 = relay.TupleGetItem(func_7896_call(), 0)
output = relay.Tuple([call_7899,call_7908,])
output2 = relay.Tuple([call_7900,call_7909,])
func_7914 = relay.Function([], output)
mod['func_7914'] = func_7914
mod = relay.transform.InferType()(mod)
output = func_7914()
func_7915 = relay.Function([], output)
mutated_mod['func_7915'] = func_7915
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7919 = relay.const(-3, dtype = "uint16")#candidate|7919|()|const|uint16
const_7920 = relay.const([[[-5,9,-4,-4],[-2,5,-5,-1],[3,-2,2,-8],[-9,7,-3,-7],[7,-2,-2,10],[-7,4,-1,1],[-10,6,2,6],[-8,1,8,-10],[3,-10,10,8],[4,-7,6,-10],[2,-10,-7,8],[-9,-9,-6,-4]],[[10,-3,-5,-8],[-3,-5,-5,-7],[10,-1,-6,-4],[-7,-4,1,1],[3,4,7,6],[-6,-8,5,-8],[-5,-3,10,-5],[-10,10,-6,-5],[-5,6,10,1],[-2,-9,-6,-3],[-9,-1,-4,6],[5,9,4,-10]],[[-2,2,-8,-2],[-2,7,-9,9],[7,-9,-6,8],[8,1,-1,5],[-9,7,-8,10],[-9,9,9,8],[-8,10,-1,-3],[6,-2,-7,10],[2,5,-6,1],[2,-5,-8,9],[-1,7,-7,-10],[-4,-8,9,-1]],[[7,4,-1,-9],[7,-5,9,8],[-3,2,7,3],[-4,4,-10,6],[-3,1,7,8],[-3,6,1,4],[3,3,7,1],[8,-7,-2,-6],[-5,-8,6,-4],[-3,5,-8,-7],[4,-1,8,2],[-7,6,2,-4]],[[-10,9,8,-7],[8,4,-2,7],[1,-6,-7,-6],[-7,-6,4,-8],[-10,-2,-2,1],[2,6,-4,-7],[10,-5,4,-3],[-2,2,9,-2],[-8,-9,-3,2],[6,9,-2,7],[2,1,3,-6],[5,5,-9,2]],[[1,-10,2,2],[-10,9,7,-4],[-2,-4,-8,-2],[-8,6,-3,-5],[-2,1,-6,3],[1,-8,2,7],[6,8,2,9],[-6,9,5,-4],[-10,-2,-7,4],[9,-8,3,-2],[9,-7,10,2],[2,5,-7,6]],[[-5,6,1,2],[2,-10,5,8],[-4,6,-10,9],[-2,-9,7,-8],[4,-6,4,7],[-8,-10,3,-7],[-2,10,-1,-4],[-7,-4,10,5],[-6,9,9,-3],[-4,-9,3,-3],[-1,7,-4,-9],[-3,3,2,7]],[[1,7,1,8],[-7,10,7,4],[-6,3,1,-1],[2,-8,-6,-4],[1,8,3,7],[4,-7,1,-10],[2,9,3,8],[5,-2,2,-9],[-7,-5,4,-10],[9,1,1,-9],[5,6,7,3],[-1,5,1,8]],[[-3,-8,-7,7],[-6,-8,-2,-9],[6,-4,9,-6],[-2,-6,7,1],[-7,8,7,-1],[-6,7,-7,-4],[2,-5,5,1],[-4,-10,-9,2],[-10,-1,10,8],[-3,5,-3,-5],[6,4,-3,9],[-4,-10,-10,10]],[[-5,-4,4,-2],[-9,9,7,-7],[-5,-4,-7,-6],[4,3,-8,-3],[-7,9,-9,10],[-1,1,4,1],[-8,8,10,6],[7,7,6,10],[4,-5,-4,4],[4,1,1,9],[-9,-7,-8,2],[-4,-3,-6,4]],[[-4,-7,-3,-2],[-4,7,7,7],[1,-4,6,-6],[-4,3,-2,3],[5,2,9,-5],[9,8,-7,1],[-8,-7,-4,5],[4,9,4,-1],[2,-8,-7,3],[6,1,8,-1],[10,1,3,-1],[3,-2,-4,9]],[[-6,4,-2,1],[-10,-1,-6,-5],[2,-8,1,3],[-1,-4,-8,8],[9,-9,-3,-9],[3,-1,4,-3],[1,3,-3,7],[-3,-9,-3,-5],[3,5,4,-8],[4,6,-7,-6],[4,-2,8,-3],[2,2,-10,-2]],[[-2,-8,-1,-5],[-6,-4,-4,3],[2,7,9,-8],[3,-10,6,-6],[7,7,2,4],[7,-1,10,10],[-1,1,6,-3],[-1,2,3,8],[-5,1,-10,-3],[4,-7,2,-8],[4,-5,1,9],[-10,-1,-2,4]],[[-5,3,9,2],[4,10,9,-8],[-7,5,-2,-10],[-7,5,2,-7],[6,4,-7,-9],[-10,-6,-6,1],[-9,9,-1,2],[-2,9,8,-2],[-7,-10,-5,-5],[9,-3,6,-6],[2,-6,8,3],[7,-3,10,-1]]], dtype = "uint16")#candidate|7920|(14, 12, 4)|const|uint16
bop_7921 = relay.bitwise_xor(const_7919.astype('uint16'), const_7920.astype('uint16')) # shape=(14, 12, 4)
func_1990_call = mod.get_global_var('func_1990')
func_1993_call = mutated_mod.get_global_var('func_1993')
var_7933 = relay.var("var_7933", dtype = "float64", shape = (32,))#candidate|7933|(32,)|var|float64
call_7932 = relay.TupleGetItem(func_1990_call(relay.reshape(var_7933.astype('float64'), [32,])), 4)
call_7934 = relay.TupleGetItem(func_1993_call(relay.reshape(var_7933.astype('float64'), [32,])), 4)
uop_7940 = relay.rsqrt(const_7920.astype('float64')) # shape=(14, 12, 4)
uop_7947 = relay.asin(uop_7940.astype('float32')) # shape=(14, 12, 4)
func_5622_call = mod.get_global_var('func_5622')
func_5623_call = mutated_mod.get_global_var('func_5623')
call_7955 = relay.TupleGetItem(func_5622_call(), 2)
call_7956 = relay.TupleGetItem(func_5623_call(), 2)
func_5910_call = mod.get_global_var('func_5910')
func_5912_call = mutated_mod.get_global_var('func_5912')
call_7962 = relay.TupleGetItem(func_5910_call(), 1)
call_7963 = relay.TupleGetItem(func_5912_call(), 1)
func_3045_call = mod.get_global_var('func_3045')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_7964 = relay.TupleGetItem(func_3045_call(), 2)
call_7965 = relay.TupleGetItem(func_3047_call(), 2)
uop_7967 = relay.exp(uop_7947.astype('float64')) # shape=(14, 12, 4)
func_6475_call = mod.get_global_var('func_6475')
func_6477_call = mutated_mod.get_global_var('func_6477')
call_7975 = relay.TupleGetItem(func_6475_call(), 3)
call_7976 = relay.TupleGetItem(func_6477_call(), 3)
output = relay.Tuple([bop_7921,call_7932,var_7933,call_7955,call_7962,call_7964,uop_7967,call_7975,])
output2 = relay.Tuple([bop_7921,call_7934,var_7933,call_7956,call_7963,call_7965,uop_7967,call_7976,])
func_7980 = relay.Function([var_7933,], output)
mod['func_7980'] = func_7980
mod = relay.transform.InferType()(mod)
mutated_mod['func_7980'] = func_7980
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7981 = relay.var("var_7981", dtype = "float64", shape = (32,))#candidate|7981|(32,)|var|float64
func_7980_call = mutated_mod.get_global_var('func_7980')
call_7982 = func_7980_call(var_7981)
output = call_7982
func_7983 = relay.Function([var_7981], output)
mutated_mod['func_7983'] = func_7983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1951_call = mod.get_global_var('func_1951')
func_1952_call = mutated_mod.get_global_var('func_1952')
call_8034 = relay.TupleGetItem(func_1951_call(), 0)
call_8035 = relay.TupleGetItem(func_1952_call(), 0)
output = relay.Tuple([call_8034,])
output2 = relay.Tuple([call_8035,])
func_8036 = relay.Function([], output)
mod['func_8036'] = func_8036
mod = relay.transform.InferType()(mod)
mutated_mod['func_8036'] = func_8036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8036_call = mutated_mod.get_global_var('func_8036')
call_8037 = func_8036_call()
output = call_8037
func_8038 = relay.Function([], output)
mutated_mod['func_8038'] = func_8038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5330_call = mod.get_global_var('func_5330')
func_5332_call = mutated_mod.get_global_var('func_5332')
call_8076 = relay.TupleGetItem(func_5330_call(), 2)
call_8077 = relay.TupleGetItem(func_5332_call(), 2)
output = relay.Tuple([call_8076,])
output2 = relay.Tuple([call_8077,])
func_8080 = relay.Function([], output)
mod['func_8080'] = func_8080
mod = relay.transform.InferType()(mod)
mutated_mod['func_8080'] = func_8080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8080_call = mutated_mod.get_global_var('func_8080')
call_8081 = func_8080_call()
output = call_8081
func_8082 = relay.Function([], output)
mutated_mod['func_8082'] = func_8082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8151 = relay.var("var_8151", dtype = "int8", shape = (12, 15, 8))#candidate|8151|(12, 15, 8)|var|int8
var_8152 = relay.var("var_8152", dtype = "int8", shape = (12, 15, 8))#candidate|8152|(12, 15, 8)|var|int8
bop_8153 = relay.bitwise_and(var_8151.astype('int8'), relay.reshape(var_8152.astype('int8'), relay.shape_of(var_8151))) # shape=(12, 15, 8)
output = bop_8153
output2 = bop_8153
func_8159 = relay.Function([var_8151,var_8152,], output)
mod['func_8159'] = func_8159
mod = relay.transform.InferType()(mod)
var_8160 = relay.var("var_8160", dtype = "int8", shape = (12, 15, 8))#candidate|8160|(12, 15, 8)|var|int8
var_8161 = relay.var("var_8161", dtype = "int8", shape = (12, 15, 8))#candidate|8161|(12, 15, 8)|var|int8
output = func_8159(var_8160,var_8161,)
func_8162 = relay.Function([var_8160,var_8161,], output)
mutated_mod['func_8162'] = func_8162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_8205 = relay.TupleGetItem(func_4501_call(), 0)
call_8206 = relay.TupleGetItem(func_4503_call(), 0)
func_5886_call = mod.get_global_var('func_5886')
func_5888_call = mutated_mod.get_global_var('func_5888')
call_8229 = relay.TupleGetItem(func_5886_call(), 0)
call_8230 = relay.TupleGetItem(func_5888_call(), 0)
func_5910_call = mod.get_global_var('func_5910')
func_5912_call = mutated_mod.get_global_var('func_5912')
call_8234 = relay.TupleGetItem(func_5910_call(), 0)
call_8235 = relay.TupleGetItem(func_5912_call(), 0)
func_6475_call = mod.get_global_var('func_6475')
func_6477_call = mutated_mod.get_global_var('func_6477')
call_8250 = relay.TupleGetItem(func_6475_call(), 2)
call_8251 = relay.TupleGetItem(func_6477_call(), 2)
output = relay.Tuple([call_8205,call_8229,call_8234,call_8250,])
output2 = relay.Tuple([call_8206,call_8230,call_8235,call_8251,])
func_8256 = relay.Function([], output)
mod['func_8256'] = func_8256
mod = relay.transform.InferType()(mod)
mutated_mod['func_8256'] = func_8256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8256_call = mutated_mod.get_global_var('func_8256')
call_8257 = func_8256_call()
output = call_8257
func_8258 = relay.Function([], output)
mutated_mod['func_8258'] = func_8258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8273 = relay.var("var_8273", dtype = "float64", shape = (9, 6, 5))#candidate|8273|(9, 6, 5)|var|float64
const_8274 = relay.const([[[6.318373,-8.707593,5.290118,-9.599697,6.089327],[-7.671818,8.270964,-1.112087,1.464253,-5.605133],[0.779208,3.019206,6.263632,7.197853,5.606024],[2.178625,-7.434414,1.793881,3.650539,8.780054],[-7.098241,6.541050,0.958674,3.181465,7.179622],[-8.030307,-7.145162,-9.857684,4.669075,-2.436911]],[[5.092104,0.808282,8.456540,0.825104,-9.681502],[2.105652,-8.189713,-1.911959,-9.709858,-9.477639],[-8.963421,-3.191233,-7.577807,-6.860080,-4.678177],[2.119108,6.407651,5.357338,5.640974,6.308242],[1.703975,-7.819680,7.661162,6.272624,0.043897],[-7.853145,0.262290,-9.338616,9.080588,0.385624]],[[9.521798,9.609356,6.327237,9.645380,2.197660],[-7.029568,6.862356,-5.298018,-6.124650,-3.116230],[4.316937,5.606297,-0.556355,5.161290,-0.408043],[1.375268,2.443742,-8.155041,-6.769137,9.283571],[6.753273,-5.759416,-0.434129,8.093040,2.166869],[-5.268809,-3.283140,1.813564,4.358780,9.379932]],[[5.541478,9.082321,7.312376,8.926390,7.060654],[-7.954463,-0.477707,8.714480,5.014285,3.122688],[9.491225,-0.061046,1.116378,-6.251724,-0.502482],[3.142248,-6.683049,-3.055831,-1.937692,6.418131],[-5.271048,-8.531562,9.585251,7.780174,7.890187],[7.442877,9.811514,-9.868801,4.822634,7.941373]],[[-4.117012,5.891904,-0.889345,5.623748,9.191312],[-1.333228,-7.645933,-4.132343,3.254868,-2.257642],[7.571874,3.754154,5.400323,0.006278,-4.763698],[-7.565965,9.446133,7.734935,4.187808,9.582123],[-8.385909,-3.270997,-4.961184,-3.129140,6.913761],[-0.372375,-3.476427,7.926043,-8.003854,-4.315222]],[[1.754716,9.998628,-5.954094,-5.094211,7.388982],[-8.326118,-8.163617,-7.649450,1.555386,-9.754949],[-8.413758,1.929532,-9.170110,-9.953734,-4.637548],[8.209542,-0.688116,-1.110190,5.513042,-3.629736],[-8.995488,-6.399900,-9.010615,-3.153544,6.848090],[-7.595477,7.615668,-0.197316,-2.811885,-2.044038]],[[1.063242,-1.804406,6.084314,-4.428872,-4.056381],[2.516533,9.170613,4.812797,1.254274,-3.995072],[-7.486965,-5.032105,-9.415840,3.082410,1.748146],[8.242932,2.724910,-5.175469,2.670623,7.129582],[-8.150285,-8.602275,8.816934,7.305842,4.873260],[0.086500,-9.522158,-9.905369,0.365648,4.791154]],[[6.202697,5.483596,-5.145270,9.913118,7.393628],[2.984326,-6.054569,4.003193,9.613173,-3.543521],[-5.425321,-1.279441,4.065034,-8.199641,-1.072622],[5.637218,-0.950770,-8.694282,8.424918,-8.479614],[5.397008,-0.679076,-2.142774,0.156465,-5.711267],[-3.187452,6.231602,8.212846,1.684134,7.514056]],[[7.548018,-7.963028,-2.142350,-6.126628,-3.400212],[-2.404766,1.942191,9.301740,-4.588110,0.964885],[-0.576019,-2.814884,8.334457,-5.256000,9.493901],[-6.272107,6.013612,-7.970460,-6.430024,4.142771],[-7.834207,-5.514410,-8.360869,4.747441,-6.434920],[1.934861,-1.319990,-9.044758,7.897533,2.440029]]], dtype = "float64")#candidate|8274|(9, 6, 5)|const|float64
bop_8275 = relay.divide(var_8273.astype('float64'), relay.reshape(const_8274.astype('float64'), relay.shape_of(var_8273))) # shape=(9, 6, 5)
output = bop_8275
output2 = bop_8275
func_8314 = relay.Function([var_8273,], output)
mod['func_8314'] = func_8314
mod = relay.transform.InferType()(mod)
var_8315 = relay.var("var_8315", dtype = "float64", shape = (9, 6, 5))#candidate|8315|(9, 6, 5)|var|float64
output = func_8314(var_8315)
func_8316 = relay.Function([var_8315], output)
mutated_mod['func_8316'] = func_8316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_8426 = relay.TupleGetItem(func_3268_call(), 0)
call_8427 = relay.TupleGetItem(func_3269_call(), 0)
uop_8433 = relay.log(call_8426.astype('float64')) # shape=(14, 6, 16)
uop_8435 = relay.log(call_8427.astype('float64')) # shape=(14, 6, 16)
func_2153_call = mod.get_global_var('func_2153')
func_2155_call = mutated_mod.get_global_var('func_2155')
call_8444 = relay.TupleGetItem(func_2153_call(), 1)
call_8445 = relay.TupleGetItem(func_2155_call(), 1)
func_6976_call = mod.get_global_var('func_6976')
func_6977_call = mutated_mod.get_global_var('func_6977')
call_8451 = func_6976_call()
call_8452 = func_6976_call()
func_1150_call = mod.get_global_var('func_1150')
func_1152_call = mutated_mod.get_global_var('func_1152')
call_8461 = relay.TupleGetItem(func_1150_call(), 1)
call_8462 = relay.TupleGetItem(func_1152_call(), 1)
output = relay.Tuple([uop_8433,call_8444,call_8451,call_8461,])
output2 = relay.Tuple([uop_8435,call_8445,call_8452,call_8462,])
func_8467 = relay.Function([], output)
mod['func_8467'] = func_8467
mod = relay.transform.InferType()(mod)
mutated_mod['func_8467'] = func_8467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8467_call = mutated_mod.get_global_var('func_8467')
call_8468 = func_8467_call()
output = call_8468
func_8469 = relay.Function([], output)
mutated_mod['func_8469'] = func_8469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3238_call = mod.get_global_var('func_3238')
func_3239_call = mutated_mod.get_global_var('func_3239')
call_8490 = relay.TupleGetItem(func_3238_call(), 0)
call_8491 = relay.TupleGetItem(func_3239_call(), 0)
output = relay.Tuple([call_8490,])
output2 = relay.Tuple([call_8491,])
func_8521 = relay.Function([], output)
mod['func_8521'] = func_8521
mod = relay.transform.InferType()(mod)
output = func_8521()
func_8522 = relay.Function([], output)
mutated_mod['func_8522'] = func_8522
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8556 = relay.var("var_8556", dtype = "uint16", shape = (4, 1, 13))#candidate|8556|(4, 1, 13)|var|uint16
var_8557 = relay.var("var_8557", dtype = "uint16", shape = (4, 7, 13))#candidate|8557|(4, 7, 13)|var|uint16
bop_8558 = relay.left_shift(var_8556.astype('uint16'), var_8557.astype('uint16')) # shape=(4, 7, 13)
uop_8563 = relay.sin(var_8556.astype('float32')) # shape=(4, 1, 13)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_8570 = relay.TupleGetItem(func_6739_call(), 0)
call_8571 = relay.TupleGetItem(func_6741_call(), 0)
uop_8584 = relay.log(var_8557.astype('float64')) # shape=(4, 7, 13)
output = relay.Tuple([bop_8558,uop_8563,call_8570,uop_8584,])
output2 = relay.Tuple([bop_8558,uop_8563,call_8571,uop_8584,])
func_8588 = relay.Function([var_8556,var_8557,], output)
mod['func_8588'] = func_8588
mod = relay.transform.InferType()(mod)
var_8589 = relay.var("var_8589", dtype = "uint16", shape = (4, 1, 13))#candidate|8589|(4, 1, 13)|var|uint16
var_8590 = relay.var("var_8590", dtype = "uint16", shape = (4, 7, 13))#candidate|8590|(4, 7, 13)|var|uint16
output = func_8588(var_8589,var_8590,)
func_8591 = relay.Function([var_8589,var_8590,], output)
mutated_mod['func_8591'] = func_8591
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8639 = relay.var("var_8639", dtype = "uint32", shape = (4, 3, 15))#candidate|8639|(4, 3, 15)|var|uint32
const_8640 = relay.const([[[3,-5,-5,-8,8,4,8,1,-8,-10,-2,3,-1,2,3],[5,5,-6,7,-1,-4,1,10,-2,3,-9,4,-8,2,-2],[1,-10,7,1,10,3,5,-7,-5,3,1,-3,-5,2,1]],[[4,-3,-2,-2,6,-5,7,-2,6,1,3,1,-9,-9,6],[6,5,4,-2,10,-8,7,-6,-8,-4,10,-3,7,9,-6],[7,-3,-3,-2,3,3,9,-9,-6,-5,-5,2,-8,-3,-5]],[[4,-1,4,5,-7,10,-2,-9,-1,-7,7,-3,-4,-8,-10],[4,-2,-10,-8,-4,5,-6,-10,9,10,-8,-10,8,2,10],[8,5,-10,-8,-1,-5,6,-3,-6,10,8,5,-10,3,10]],[[5,7,7,6,6,-10,2,-2,-4,7,4,-3,5,-5,-7],[-10,-2,4,-6,7,-6,5,-4,-4,5,4,7,10,3,10],[10,-4,-9,-2,-7,-9,5,-2,10,9,7,5,-3,6,2]]], dtype = "uint32")#candidate|8640|(4, 3, 15)|const|uint32
bop_8641 = relay.bitwise_or(var_8639.astype('uint32'), relay.reshape(const_8640.astype('uint32'), relay.shape_of(var_8639))) # shape=(4, 3, 15)
output = relay.Tuple([bop_8641,])
output2 = relay.Tuple([bop_8641,])
func_8644 = relay.Function([var_8639,], output)
mod['func_8644'] = func_8644
mod = relay.transform.InferType()(mod)
mutated_mod['func_8644'] = func_8644
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8645 = relay.var("var_8645", dtype = "uint32", shape = (4, 3, 15))#candidate|8645|(4, 3, 15)|var|uint32
func_8644_call = mutated_mod.get_global_var('func_8644')
call_8646 = func_8644_call(var_8645)
output = call_8646
func_8647 = relay.Function([var_8645], output)
mutated_mod['func_8647'] = func_8647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8663 = relay.var("var_8663", dtype = "uint32", shape = ())#candidate|8663|()|var|uint32
var_8664 = relay.var("var_8664", dtype = "uint32", shape = (3, 10, 6))#candidate|8664|(3, 10, 6)|var|uint32
bop_8665 = relay.not_equal(var_8663.astype('bool'), var_8664.astype('bool')) # shape=(3, 10, 6)
bop_8676 = relay.mod(bop_8665.astype('float32'), var_8663.astype('float32')) # shape=(3, 10, 6)
func_1580_call = mod.get_global_var('func_1580')
func_1581_call = mutated_mod.get_global_var('func_1581')
call_8689 = relay.TupleGetItem(func_1580_call(), 2)
call_8690 = relay.TupleGetItem(func_1581_call(), 2)
func_4646_call = mod.get_global_var('func_4646')
func_4647_call = mutated_mod.get_global_var('func_4647')
call_8694 = func_4646_call()
call_8695 = func_4646_call()
bop_8702 = relay.minimum(bop_8665.astype('int32'), relay.reshape(var_8664.astype('int32'), relay.shape_of(bop_8665))) # shape=(3, 10, 6)
output = relay.Tuple([bop_8676,call_8689,call_8694,bop_8702,])
output2 = relay.Tuple([bop_8676,call_8690,call_8695,bop_8702,])
func_8707 = relay.Function([var_8663,var_8664,], output)
mod['func_8707'] = func_8707
mod = relay.transform.InferType()(mod)
var_8708 = relay.var("var_8708", dtype = "uint32", shape = ())#candidate|8708|()|var|uint32
var_8709 = relay.var("var_8709", dtype = "uint32", shape = (3, 10, 6))#candidate|8709|(3, 10, 6)|var|uint32
output = func_8707(var_8708,var_8709,)
func_8710 = relay.Function([var_8708,var_8709,], output)
mutated_mod['func_8710'] = func_8710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3613_call = mod.get_global_var('func_3613')
func_3614_call = mutated_mod.get_global_var('func_3614')
call_8722 = func_3613_call()
call_8723 = func_3613_call()
output = call_8722
output2 = call_8723
func_8759 = relay.Function([], output)
mod['func_8759'] = func_8759
mod = relay.transform.InferType()(mod)
mutated_mod['func_8759'] = func_8759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8759_call = mutated_mod.get_global_var('func_8759')
call_8760 = func_8759_call()
output = call_8760
func_8761 = relay.Function([], output)
mutated_mod['func_8761'] = func_8761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6821_call = mod.get_global_var('func_6821')
func_6823_call = mutated_mod.get_global_var('func_6823')
call_8809 = relay.TupleGetItem(func_6821_call(), 0)
call_8810 = relay.TupleGetItem(func_6823_call(), 0)
func_6391_call = mod.get_global_var('func_6391')
func_6392_call = mutated_mod.get_global_var('func_6392')
call_8825 = relay.TupleGetItem(func_6391_call(), 3)
call_8826 = relay.TupleGetItem(func_6392_call(), 3)
func_479_call = mod.get_global_var('func_479')
func_480_call = mutated_mod.get_global_var('func_480')
call_8836 = relay.TupleGetItem(func_479_call(), 1)
call_8837 = relay.TupleGetItem(func_480_call(), 1)
func_7094_call = mod.get_global_var('func_7094')
func_7095_call = mutated_mod.get_global_var('func_7095')
call_8844 = func_7094_call()
call_8845 = func_7094_call()
func_5507_call = mod.get_global_var('func_5507')
func_5511_call = mutated_mod.get_global_var('func_5511')
const_8864 = relay.const([[-7,1,-4,-5,8,-1,-5,9],[1,1,8,-9,8,4,-7,3],[5,-4,-2,1,10,-7,9,8],[-5,-9,6,1,9,-6,-10,-10],[5,-3,-2,9,6,-10,3,3],[8,3,10,-2,9,-5,6,-3],[-1,8,-3,-7,4,-2,-7,6],[-8,1,-3,7,8,-1,7,-5],[-10,-4,-1,-10,2,1,8,5],[6,-4,-7,-1,10,9,-3,10],[7,-8,6,-1,-1,-8,-10,5],[-8,-5,9,-2,-7,10,3,-5],[3,9,1,-10,4,1,2,4],[-4,-7,-6,-4,7,-10,4,-5],[9,10,5,10,9,-7,-7,1],[9,-8,4,-5,6,5,3,8],[-3,-9,8,2,-3,8,-10,-3],[6,4,-3,-3,8,-10,-8,-2],[7,-1,-5,4,-2,7,-1,10],[2,-9,5,-6,2,4,6,-2],[9,10,6,9,-6,9,9,-5],[3,7,-6,9,-1,-7,-8,10],[2,-9,-5,6,9,1,5,8],[-9,-4,-10,-4,-5,-7,-2,10],[10,4,-2,-9,8,-6,7,10],[2,3,-8,-4,2,6,2,-9],[5,-8,-8,7,-8,-6,8,-10],[-10,4,-2,1,-2,9,2,6],[3,-6,2,6,8,-4,-10,9],[-9,-9,1,-6,-8,-9,-3,10],[1,-9,-1,5,-7,-6,-5,-6],[-9,-7,5,-5,8,-5,-9,9],[5,2,-10,-5,-8,-1,-7,-1],[-4,-7,2,3,-6,-1,5,4],[5,-6,-5,-2,-4,-9,-4,7],[9,-8,-8,10,-9,-10,2,-4],[1,4,1,-2,10,7,-2,-1],[-10,3,-10,-3,-6,5,8,7],[-9,9,8,8,5,-4,-10,9],[4,10,-6,4,8,2,-9,5],[-1,-2,6,-8,3,-9,9,-5],[-9,-8,9,-9,-3,1,1,2],[2,2,3,-8,-4,-1,4,-7],[-4,10,-8,10,-9,3,-1,-1],[-8,1,-4,8,-6,10,-9,-7],[-3,6,-5,3,9,3,1,-3],[8,10,2,10,1,10,-9,10],[-3,5,5,1,4,-6,-1,-5],[2,2,5,2,6,-5,10,-8],[4,-2,-1,-4,8,-9,-8,9],[-10,-2,5,-3,9,-5,-5,-3],[-6,9,7,-2,3,5,8,9],[-6,-4,-6,-1,5,3,1,-9],[10,-4,-1,-3,10,4,-5,5],[-4,2,8,-5,1,4,-4,7],[-3,3,9,-8,8,-4,-5,-4],[-10,8,-10,-2,1,-3,1,10],[-2,7,1,-8,-9,9,5,-2],[-10,4,5,2,-4,-2,-6,-10],[-5,2,4,2,4,5,7,-6],[-10,-8,6,3,-7,-6,7,-3],[-3,-8,-5,-8,4,-10,-5,-7],[-9,-1,4,-7,-1,8,-7,10],[-8,-6,-9,-3,10,-3,4,-9],[2,7,6,-9,-5,2,-9,-3],[-3,9,-3,-4,-8,7,4,4],[-6,3,3,8,2,3,2,-6],[4,6,10,10,6,1,-3,-9],[-3,2,8,-7,10,10,5,9],[-1,-5,-7,-8,-2,5,3,-6],[-8,-4,8,5,-9,-2,-10,2],[-5,4,-3,5,3,-1,-3,3],[-7,8,-6,5,-9,-2,5,-2],[-2,-10,-1,10,-4,10,-10,-1],[-10,2,3,3,-4,10,-8,10],[1,7,-7,-7,8,10,-2,4],[-1,6,-4,3,4,9,-8,-6],[-1,2,-7,-8,-8,-2,-9,-10],[3,-4,7,-6,3,-6,2,-1],[-2,8,-3,4,-5,10,3,4],[-8,-2,6,-7,-1,1,3,-8],[-4,-6,-3,8,9,3,10,7],[-6,6,-6,10,-5,3,-2,5],[-7,4,-1,1,-4,1,2,3],[-6,-9,-1,-2,-1,-6,-5,-10],[2,-4,8,-5,8,6,4,9],[10,2,8,-8,8,1,-7,-6],[6,-3,3,-9,-2,4,-6,-5],[8,8,3,6,-9,5,-9,4],[10,2,-5,-8,-7,4,3,10],[9,9,5,3,2,10,10,-9],[-3,-6,3,5,4,3,-9,1],[2,-1,-5,1,-4,-9,8,5],[-8,-8,-4,-8,2,-6,-6,-8],[6,7,6,7,2,-6,-3,-10],[3,1,-10,-6,2,-1,8,9],[1,-5,6,10,-9,8,7,-4],[-5,8,4,6,-7,-4,-8,-10],[1,-9,7,-6,-6,-10,-2,5],[-7,-3,-8,-5,-5,9,4,-6],[5,5,-5,-8,-7,3,-3,7],[1,1,8,-4,6,10,-5,6],[-4,-3,2,-9,2,-10,-2,4],[-6,5,-2,-7,-4,-8,-3,-10],[5,-5,7,-8,8,3,-5,-3],[2,5,9,-2,-8,4,5,8],[9,9,-9,-4,-4,-9,4,10],[-2,-9,6,3,-10,-5,3,6],[-9,10,1,9,1,-6,1,-10],[-10,1,-8,10,-1,4,-10,-8],[3,-1,1,2,7,6,4,9],[5,-8,6,1,-2,-3,-3,-3]], dtype = "uint8")#candidate|8864|(112, 8)|const|uint8
call_8863 = func_5507_call(relay.reshape(const_8864.astype('uint8'), [16, 4, 14]), relay.reshape(const_8864.astype('uint8'), [16, 4, 14]), )
call_8865 = func_5507_call(relay.reshape(const_8864.astype('uint8'), [16, 4, 14]), relay.reshape(const_8864.astype('uint8'), [16, 4, 14]), )
uop_8866 = relay.sigmoid(const_8864.astype('float64')) # shape=(112, 8)
func_1380_call = mod.get_global_var('func_1380')
func_1382_call = mutated_mod.get_global_var('func_1382')
var_8871 = relay.var("var_8871", dtype = "float32", shape = (312,))#candidate|8871|(312,)|var|float32
call_8870 = func_1380_call(relay.reshape(var_8871.astype('float32'), [3, 8, 13]))
call_8872 = func_1380_call(relay.reshape(var_8871.astype('float32'), [3, 8, 13]))
bop_8877 = relay.power(uop_8866.astype('float32'), relay.reshape(call_8863.astype('float32'), relay.shape_of(uop_8866))) # shape=(112, 8)
bop_8880 = relay.power(uop_8866.astype('float32'), relay.reshape(call_8865.astype('float32'), relay.shape_of(uop_8866))) # shape=(112, 8)
output = relay.Tuple([call_8809,call_8825,call_8836,call_8844,call_8870,var_8871,bop_8877,])
output2 = relay.Tuple([call_8810,call_8826,call_8837,call_8845,call_8872,var_8871,bop_8880,])
func_8881 = relay.Function([var_8871,], output)
mod['func_8881'] = func_8881
mod = relay.transform.InferType()(mod)
mutated_mod['func_8881'] = func_8881
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8882 = relay.var("var_8882", dtype = "float32", shape = (312,))#candidate|8882|(312,)|var|float32
func_8881_call = mutated_mod.get_global_var('func_8881')
call_8883 = func_8881_call(var_8882)
output = call_8883
func_8884 = relay.Function([var_8882], output)
mutated_mod['func_8884'] = func_8884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_8969 = relay.TupleGetItem(func_6739_call(), 0)
call_8970 = relay.TupleGetItem(func_6741_call(), 0)
output = relay.Tuple([call_8969,])
output2 = relay.Tuple([call_8970,])
func_8971 = relay.Function([], output)
mod['func_8971'] = func_8971
mod = relay.transform.InferType()(mod)
output = func_8971()
func_8972 = relay.Function([], output)
mutated_mod['func_8972'] = func_8972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_534_call = mod.get_global_var('func_534')
func_536_call = mutated_mod.get_global_var('func_536')
call_8998 = relay.TupleGetItem(func_534_call(), 0)
call_8999 = relay.TupleGetItem(func_536_call(), 0)
func_3261_call = mod.get_global_var('func_3261')
func_3262_call = mutated_mod.get_global_var('func_3262')
call_9024 = relay.TupleGetItem(func_3261_call(), 0)
call_9025 = relay.TupleGetItem(func_3262_call(), 0)
func_1018_call = mod.get_global_var('func_1018')
func_1021_call = mutated_mod.get_global_var('func_1021')
var_9034 = relay.var("var_9034", dtype = "int32", shape = (88,))#candidate|9034|(88,)|var|int32
var_9035 = relay.var("var_9035", dtype = "int32", shape = (880,))#candidate|9035|(880,)|var|int32
call_9033 = func_1018_call(relay.reshape(var_9034.astype('int32'), [11, 1, 8]), relay.reshape(var_9035.astype('int32'), [11, 10, 8]), )
call_9036 = func_1018_call(relay.reshape(var_9034.astype('int32'), [11, 1, 8]), relay.reshape(var_9035.astype('int32'), [11, 10, 8]), )
func_1871_call = mod.get_global_var('func_1871')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_9039 = relay.TupleGetItem(func_1871_call(), 0)
call_9040 = relay.TupleGetItem(func_1872_call(), 0)
func_7565_call = mod.get_global_var('func_7565')
func_7566_call = mutated_mod.get_global_var('func_7566')
call_9049 = relay.TupleGetItem(func_7565_call(), 1)
call_9050 = relay.TupleGetItem(func_7566_call(), 1)
func_1990_call = mod.get_global_var('func_1990')
func_1993_call = mutated_mod.get_global_var('func_1993')
const_9058 = relay.const([4.269637,7.754114,5.798200,8.439757,3.493719,-5.160274,6.912675,-4.255574,-2.469823,5.382891,-3.353549,-2.812900,-4.225790,-7.502358,-9.425230,-3.734588,-2.905040,8.083975,-4.041492,1.984421,4.664992,1.499942,-1.494504,-7.403226,1.034303,-1.611587,9.640564,9.702243,-8.427581,-1.420561,1.972385,-6.476987], dtype = "float64")#candidate|9058|(32,)|const|float64
call_9057 = relay.TupleGetItem(func_1990_call(relay.reshape(const_9058.astype('float64'), [32,])), 0)
call_9059 = relay.TupleGetItem(func_1993_call(relay.reshape(const_9058.astype('float64'), [32,])), 0)
output = relay.Tuple([call_8998,call_9024,call_9033,var_9034,var_9035,call_9039,call_9049,call_9057,const_9058,])
output2 = relay.Tuple([call_8999,call_9025,call_9036,var_9034,var_9035,call_9040,call_9050,call_9059,const_9058,])
func_9060 = relay.Function([var_9034,var_9035,], output)
mod['func_9060'] = func_9060
mod = relay.transform.InferType()(mod)
mutated_mod['func_9060'] = func_9060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9060_call = mutated_mod.get_global_var('func_9060')
var_9062 = relay.var("var_9062", dtype = "int32", shape = (88,))#candidate|9062|(88,)|var|int32
var_9063 = relay.var("var_9063", dtype = "int32", shape = (880,))#candidate|9063|(880,)|var|int32
call_9061 = func_9060_call(var_9062,var_9063,)
output = call_9061
func_9064 = relay.Function([var_9062,var_9063,], output)
mutated_mod['func_9064'] = func_9064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_9079 = relay.TupleGetItem(func_4501_call(), 1)
call_9080 = relay.TupleGetItem(func_4503_call(), 1)
output = call_9079
output2 = call_9080
func_9083 = relay.Function([], output)
mod['func_9083'] = func_9083
mod = relay.transform.InferType()(mod)
output = func_9083()
func_9084 = relay.Function([], output)
mutated_mod['func_9084'] = func_9084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7565_call = mod.get_global_var('func_7565')
func_7566_call = mutated_mod.get_global_var('func_7566')
call_9101 = relay.TupleGetItem(func_7565_call(), 1)
call_9102 = relay.TupleGetItem(func_7566_call(), 1)
func_1889_call = mod.get_global_var('func_1889')
func_1891_call = mutated_mod.get_global_var('func_1891')
call_9103 = relay.TupleGetItem(func_1889_call(), 0)
call_9104 = relay.TupleGetItem(func_1891_call(), 0)
func_7849_call = mod.get_global_var('func_7849')
func_7851_call = mutated_mod.get_global_var('func_7851')
call_9112 = relay.TupleGetItem(func_7849_call(), 1)
call_9113 = relay.TupleGetItem(func_7851_call(), 1)
output = relay.Tuple([call_9101,call_9103,call_9112,])
output2 = relay.Tuple([call_9102,call_9104,call_9113,])
func_9128 = relay.Function([], output)
mod['func_9128'] = func_9128
mod = relay.transform.InferType()(mod)
output = func_9128()
func_9129 = relay.Function([], output)
mutated_mod['func_9129'] = func_9129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2533_call = mod.get_global_var('func_2533')
func_2534_call = mutated_mod.get_global_var('func_2534')
call_9145 = relay.TupleGetItem(func_2533_call(), 0)
call_9146 = relay.TupleGetItem(func_2534_call(), 0)
output = call_9145
output2 = call_9146
func_9156 = relay.Function([], output)
mod['func_9156'] = func_9156
mod = relay.transform.InferType()(mod)
mutated_mod['func_9156'] = func_9156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9156_call = mutated_mod.get_global_var('func_9156')
call_9157 = func_9156_call()
output = call_9157
func_9158 = relay.Function([], output)
mutated_mod['func_9158'] = func_9158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3871_call = mod.get_global_var('func_3871')
func_3872_call = mutated_mod.get_global_var('func_3872')
call_9184 = func_3871_call()
call_9185 = func_3871_call()
func_9083_call = mod.get_global_var('func_9083')
func_9084_call = mutated_mod.get_global_var('func_9084')
call_9187 = func_9083_call()
call_9188 = func_9083_call()
func_2506_call = mod.get_global_var('func_2506')
func_2509_call = mutated_mod.get_global_var('func_2509')
const_9194 = relay.const([0.657937,-8.506615,2.958991,4.094569,1.920670,-7.983333,5.483901,2.730821,0.413062,-2.390268,6.733335,4.738883,-9.753681,-5.781583,-6.664248,8.948349,-5.975905,6.709306,0.072285,5.235960,-0.084886,-9.642677,-8.227885,-4.775044,-8.078704,-0.719755,6.064270,2.415118,-4.355324,0.500467,5.539752,-8.196548,-4.736146,8.729191,-5.870325,7.556071,-2.722394,-5.809718,1.043785,-4.329799,6.992672,-7.893499,-8.044094,-5.830884,7.963732,-9.537841,-4.593017,-2.524369,-9.763657,-1.191765,5.258839,0.090439,-3.831384,-1.872465,-2.943481,1.577558,8.496935,-2.429818,8.637045,-1.801496,3.503629,6.128227,-3.972054,-1.201903,5.407830,1.575267,-6.924220,7.864428,0.218012,5.786173,-2.787041,2.904715,-3.713404,-8.592895,3.740483,-2.607535,7.315425,-9.026189,-8.398597,-8.031861,-4.616204,-7.748496,-7.700208,9.859596,4.395827,-1.688814,0.950455,6.389647,7.541786,9.780700,-8.421271,2.154264,-6.504695,3.784403,4.582405,-6.956155,-4.990635,-9.358984,-4.478706,-3.530115,-5.447754,-5.123118,-2.204980,3.207324,9.730877,-4.920425,7.691881,9.929646,-4.587061,-5.668537], dtype = "float64")#candidate|9194|(110,)|const|float64
call_9193 = relay.TupleGetItem(func_2506_call(relay.reshape(const_9194.astype('float64'), [2, 11, 5])), 0)
call_9195 = relay.TupleGetItem(func_2509_call(relay.reshape(const_9194.astype('float64'), [2, 11, 5])), 0)
output = relay.Tuple([call_9184,call_9187,call_9193,const_9194,])
output2 = relay.Tuple([call_9185,call_9188,call_9195,const_9194,])
func_9199 = relay.Function([], output)
mod['func_9199'] = func_9199
mod = relay.transform.InferType()(mod)
output = func_9199()
func_9200 = relay.Function([], output)
mutated_mod['func_9200'] = func_9200
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9227 = relay.var("var_9227", dtype = "float32", shape = (16, 9, 13))#candidate|9227|(16, 9, 13)|var|float32
uop_9228 = relay.acos(var_9227.astype('float32')) # shape=(16, 9, 13)
bop_9231 = relay.less_equal(uop_9228.astype('bool'), relay.reshape(var_9227.astype('bool'), relay.shape_of(uop_9228))) # shape=(16, 9, 13)
func_6821_call = mod.get_global_var('func_6821')
func_6823_call = mutated_mod.get_global_var('func_6823')
call_9234 = relay.TupleGetItem(func_6821_call(), 0)
call_9235 = relay.TupleGetItem(func_6823_call(), 0)
func_2288_call = mod.get_global_var('func_2288')
func_2290_call = mutated_mod.get_global_var('func_2290')
call_9236 = func_2288_call()
call_9237 = func_2288_call()
output = relay.Tuple([bop_9231,call_9234,call_9236,])
output2 = relay.Tuple([bop_9231,call_9235,call_9237,])
func_9244 = relay.Function([var_9227,], output)
mod['func_9244'] = func_9244
mod = relay.transform.InferType()(mod)
mutated_mod['func_9244'] = func_9244
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9245 = relay.var("var_9245", dtype = "float32", shape = (16, 9, 13))#candidate|9245|(16, 9, 13)|var|float32
func_9244_call = mutated_mod.get_global_var('func_9244')
call_9246 = func_9244_call(var_9245)
output = call_9246
func_9247 = relay.Function([var_9245], output)
mutated_mod['func_9247'] = func_9247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_9288 = relay.TupleGetItem(func_6739_call(), 0)
call_9289 = relay.TupleGetItem(func_6741_call(), 0)
output = relay.Tuple([call_9288,])
output2 = relay.Tuple([call_9289,])
func_9295 = relay.Function([], output)
mod['func_9295'] = func_9295
mod = relay.transform.InferType()(mod)
mutated_mod['func_9295'] = func_9295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9295_call = mutated_mod.get_global_var('func_9295')
call_9296 = func_9295_call()
output = call_9296
func_9297 = relay.Function([], output)
mutated_mod['func_9297'] = func_9297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_9321 = relay.TupleGetItem(func_876_call(), 0)
call_9322 = relay.TupleGetItem(func_878_call(), 0)
func_8080_call = mod.get_global_var('func_8080')
func_8082_call = mutated_mod.get_global_var('func_8082')
call_9369 = relay.TupleGetItem(func_8080_call(), 0)
call_9370 = relay.TupleGetItem(func_8082_call(), 0)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_9390 = relay.TupleGetItem(func_4637_call(), 0)
call_9391 = relay.TupleGetItem(func_4639_call(), 0)
output = relay.Tuple([call_9321,call_9369,call_9390,])
output2 = relay.Tuple([call_9322,call_9370,call_9391,])
func_9397 = relay.Function([], output)
mod['func_9397'] = func_9397
mod = relay.transform.InferType()(mod)
output = func_9397()
func_9398 = relay.Function([], output)
mutated_mod['func_9398'] = func_9398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8759_call = mod.get_global_var('func_8759')
func_8761_call = mutated_mod.get_global_var('func_8761')
call_9411 = func_8759_call()
call_9412 = func_8759_call()
output = call_9411
output2 = call_9412
func_9431 = relay.Function([], output)
mod['func_9431'] = func_9431
mod = relay.transform.InferType()(mod)
output = func_9431()
func_9432 = relay.Function([], output)
mutated_mod['func_9432'] = func_9432
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9453 = relay.const([[[-4.139341,-8.469884,4.071172,-5.609777,9.060084,7.061518,-7.578939,-2.704933,3.661416,-8.833327,3.578302,2.639389],[-1.417878,4.703275,9.520222,8.563607,-3.641636,-1.387864,1.793185,-7.664456,9.545449,-9.110218,-2.723634,6.657011],[-9.337404,3.646378,-1.193984,-1.183994,-0.782929,3.057672,-5.089861,-5.291867,-2.608061,-4.143642,0.544520,1.732645],[4.368502,-1.479643,-7.114304,0.051416,-8.112128,0.107125,-8.941996,1.712458,0.977169,-4.652511,3.044677,1.700546],[-0.843170,8.634052,-4.757228,-4.592296,2.896970,7.932470,-2.491965,-2.354889,-3.139422,6.395070,7.703427,2.579838],[9.059720,-6.414305,-8.471941,-8.532920,-9.538458,-3.970191,-4.281467,-8.668188,-6.031597,-2.587070,-8.189122,0.695446],[-4.412608,9.295143,7.653534,-6.120146,8.831954,6.724316,-4.405475,-5.875454,7.853433,3.313457,8.444016,3.203643],[-1.355051,-3.204624,9.368856,7.684546,-8.124787,7.060167,5.515595,-6.138531,4.365033,2.069303,4.566118,-7.303896],[-3.607905,7.358997,2.786276,3.114557,-9.387549,-5.495543,9.942582,7.472334,4.421264,3.275524,-2.743719,3.620702],[6.886122,-7.085094,-0.429409,-9.168469,-2.226054,-9.436781,-9.676835,7.469883,4.379474,-3.396175,8.680937,-4.994750],[0.932869,-0.325582,9.124097,6.203267,-0.152798,6.085016,-8.410479,8.033059,2.989405,-9.936495,-1.263626,-5.508007],[7.665305,-9.923090,-5.189352,5.843640,6.329744,-3.276697,9.919183,7.413362,4.723807,-5.094779,-5.453204,-5.099913],[3.129348,-5.324025,6.371016,7.510616,1.587858,9.710369,-6.674460,8.833363,-0.082946,-7.722752,7.094137,1.746464],[7.830224,-0.662994,-7.287178,6.348404,1.882376,1.417959,9.406269,-8.783578,-0.219282,-4.415781,-6.065574,-3.575497],[5.892483,8.742390,7.526452,7.327522,-2.324435,-2.102706,2.340375,8.327367,1.538683,4.161839,8.330304,-8.985199],[7.837668,6.432636,-0.524369,6.656735,-3.285324,0.787114,3.396886,-6.204112,-9.651539,-8.389223,8.234878,6.345933]],[[-7.063183,3.634585,-2.352668,-2.196617,-4.164641,0.003613,5.298638,8.168317,2.903415,1.138427,1.415359,7.283915],[7.884884,9.211763,3.054042,8.504584,8.450357,3.368840,-7.174613,-5.717569,5.598327,-5.248765,-3.740278,8.863454],[-0.844001,-4.365601,-8.043898,0.933919,-8.125990,-7.745130,5.858562,7.339378,-3.460186,-0.164731,-0.285563,-3.420504],[4.109266,2.285289,-3.003439,0.381451,1.032482,-4.952762,4.993177,7.785332,8.163695,4.826621,-4.266686,9.513294],[-4.167330,8.478692,-6.316936,-5.194335,-4.181158,3.523360,-5.366719,2.457363,3.343485,-0.434100,-5.042936,-8.200583],[1.609618,-1.841475,-0.400353,9.782412,-5.093090,-1.745203,-8.979126,-4.807337,-0.437100,6.803434,-8.431633,-6.964106],[-7.519284,3.311164,3.586600,-0.934475,1.947799,-7.170291,9.714881,-2.478975,-1.618377,-3.320536,-9.647161,-3.249636],[6.345449,7.088178,-0.134081,8.856536,-9.709619,8.554743,-4.612403,1.299737,0.829147,5.194638,5.545143,-0.277950],[-5.259988,-5.116685,5.438417,1.384865,-3.702457,-6.868714,9.585245,4.419909,-4.114271,1.149957,7.836041,0.303070],[-1.846000,0.087407,-8.799083,2.617688,-6.977707,5.535945,-0.398816,-9.926185,-5.733701,-0.622870,-7.433632,3.254768],[-3.304957,3.723772,1.333596,-7.588828,-2.947542,4.890825,2.233937,5.698219,-7.954522,2.393975,-1.427623,1.417701],[1.353520,-1.539664,-4.637296,-8.232922,-8.049677,-7.080170,-5.688644,5.663873,-2.799192,-1.625226,2.690889,3.493960],[-0.435951,7.807948,8.182407,4.641100,-7.871583,-7.936926,-5.252303,8.252046,0.244237,-9.116489,6.369947,-6.488431],[6.375145,6.399437,-1.248385,-5.319248,-0.836265,7.735129,3.370505,-6.515193,-0.345140,-7.266433,9.483100,3.126350],[8.366662,6.353786,4.120915,-9.581951,-0.900708,-1.918165,-4.370959,6.769788,-5.318255,-5.489819,-6.310097,3.934137],[-5.563978,8.305120,0.580395,-8.153638,-9.407849,2.955979,0.316669,-3.278941,-4.205538,-3.588018,-0.634078,1.530806]],[[1.737477,-5.770322,-9.034756,-9.597329,4.276672,-6.522363,5.695788,6.768888,-7.769417,3.816840,-9.577578,6.977923],[-9.530360,2.124421,-2.067796,9.181147,0.556403,4.586894,1.688697,-1.079179,6.898387,-3.387813,1.553917,-9.619801],[-8.846281,3.197213,-8.149057,4.498886,-5.601087,9.932698,4.260386,-8.742544,-1.376375,-3.871674,-3.517041,-1.970097],[-6.047374,-1.486589,-0.506353,2.203753,-9.780504,0.944845,-9.052679,-1.801978,0.611957,6.713829,-5.417717,9.640585],[2.618982,8.764502,-3.949958,0.470549,-0.665376,-7.860378,-4.117399,8.064891,-8.704724,5.323686,-1.629958,-5.808513],[4.151783,-3.338336,7.597925,-6.392965,-3.288135,-0.178107,0.848018,1.244250,6.665745,-5.003625,1.841607,3.518147],[-9.703978,-8.343397,-5.471826,7.674247,-4.601890,9.136374,8.660622,-8.249066,0.136872,4.262948,-1.314434,-6.400622],[-4.958276,-5.169373,2.751708,-5.199633,-5.441892,-8.053932,8.344363,5.668519,2.623548,1.520181,-8.040097,-5.350110],[5.727356,6.973936,-6.713243,6.408176,-7.484386,2.554269,1.412113,-6.310997,-0.347340,-5.423255,-6.172805,-8.719797],[9.695359,-8.084505,6.885398,1.351933,-0.865175,2.276025,8.403246,-6.746012,-9.818476,0.756344,9.411190,8.002646],[-9.773266,5.855374,7.329991,-7.389589,0.163608,6.175257,-3.670872,5.024768,6.725926,4.577737,-8.860233,-1.871580],[3.348754,-9.687465,0.770646,1.955621,-3.688824,-2.966095,-9.936497,-7.242911,-7.145535,-9.414738,-6.901832,0.986942],[-7.208778,-9.199972,-9.656042,5.261837,-9.356920,-5.725817,-0.760944,1.363913,-2.025476,-5.796455,3.155493,1.322086],[-1.800711,-8.666377,5.727713,-6.164453,-7.961114,-6.978850,-4.692842,7.958219,-0.659304,-7.871735,6.948697,3.663768],[-7.300850,-8.317479,-6.402169,0.894693,1.340154,3.471326,4.100465,6.022894,6.537113,2.880054,3.466470,-7.024660],[-8.201579,-4.074741,9.045126,-4.693779,-1.599301,1.979273,-5.274612,9.490550,-5.657403,-1.541870,9.603370,2.854038]],[[-5.020347,-2.620920,7.386915,9.473705,5.153251,7.087562,4.329504,-2.063768,-0.946227,-6.495448,-0.860116,1.065989],[-2.675554,6.964942,7.477014,-3.801743,6.131494,8.009301,-6.754136,-1.144829,2.283537,-4.184040,5.017070,-8.336802],[-7.302967,-6.391249,-1.106065,8.144690,-1.855932,-0.515100,8.085124,2.021367,5.204382,-2.072087,5.030110,-6.412717],[-1.815808,8.624069,5.668948,-1.771600,-8.716468,7.341570,-4.087322,5.794349,7.245930,-9.512433,6.773614,1.976839],[-6.361075,-7.229217,-0.048842,-8.244754,9.884023,4.629926,2.788910,-0.315929,-6.547882,3.105370,-4.741580,7.490743],[-0.258924,-3.368794,8.230436,9.486314,3.676598,2.205288,-3.990168,1.000515,7.979931,-8.277810,-8.383726,-0.399714],[-2.353312,8.387853,5.418152,-0.653342,-9.422773,6.426186,-1.281538,6.460097,-7.109183,-7.502300,7.708093,-7.492667],[-9.846010,8.672688,6.712870,5.168994,1.023170,-3.653591,-1.179942,7.650432,3.091262,-2.224434,8.439225,-2.502388],[2.124028,-8.356263,-9.445123,0.901348,5.349839,5.042591,3.130252,2.147361,8.085983,7.018532,-3.300765,-9.863250],[6.969104,-5.769475,-7.836228,-8.294028,1.714914,-5.206456,3.815819,-1.427846,4.278099,9.642595,-8.693977,4.481416],[-0.334439,8.067290,2.530810,-5.122323,3.003707,6.440802,5.756782,0.772167,-6.412826,-8.204830,3.393688,8.117420],[-1.393901,6.702613,5.548805,-7.835429,2.105802,-5.082154,3.844921,3.000798,3.252609,5.030919,-9.055795,8.077689],[-3.391141,-0.244277,-8.075773,-8.329868,-1.820820,-6.935369,0.835182,7.552877,-6.939036,1.573391,4.507528,-0.792918],[-9.687495,6.664545,-6.489800,5.776294,2.360183,6.789216,5.125993,-6.388199,8.928378,2.042851,-1.182970,-0.192537],[9.472127,-3.721072,-1.698901,6.019541,-6.323427,-1.424123,-4.206576,-2.810122,6.639513,1.000914,4.206007,0.294734],[-0.306219,6.769636,3.646739,-0.559305,-4.225904,5.550668,3.741482,9.459759,-2.621442,9.829421,0.766167,-4.314371]],[[9.358282,-6.872335,6.954984,3.562999,-7.332374,-7.772101,-9.870600,-3.075267,-3.017054,-9.897930,4.770321,6.891712],[1.123397,-1.768042,-0.020495,1.042984,-4.965481,2.845911,4.900126,-5.710849,2.227006,-6.301703,8.181108,-8.794915],[-5.430357,2.613335,-9.709167,0.973042,4.017838,4.308295,-1.530475,6.444999,-7.550920,3.606421,-0.194022,2.335631],[-1.028508,8.854587,3.300475,0.808413,-2.234951,5.742640,-9.962136,-1.905847,-0.528392,0.849723,2.855872,1.444613],[2.135024,4.273921,-8.355916,-5.045729,-5.075059,-3.611358,9.449957,-9.920363,1.915917,7.079267,-7.399267,0.043031],[4.133102,-6.159136,-4.674813,-4.230749,-3.382785,1.062007,-6.483024,2.602343,6.055822,-8.827012,-8.278671,5.371131],[-3.247021,7.532658,-5.478640,0.126458,0.921659,-1.913198,-6.098217,-9.785627,7.680797,9.836726,3.924288,-5.462661],[4.209800,3.734788,2.062788,6.433273,6.136546,2.258339,2.630093,6.349177,-0.448336,-8.383510,-9.107024,6.023519],[-9.259073,-5.178823,1.906562,4.993047,3.164905,-3.316705,1.774164,4.109778,-0.143729,-2.879240,9.972826,6.020305],[-3.639072,-5.033372,-2.682036,-8.962858,0.418655,-5.387125,5.900353,7.522932,-7.616589,-6.613588,4.248022,7.214534],[-8.828895,1.804645,2.205579,1.060988,9.481952,2.653462,6.788082,-0.912293,-2.875749,2.531719,-0.435502,-4.756560],[2.912098,-2.224207,-4.530138,-0.870439,-3.513515,3.027904,-4.873722,9.921320,-1.775819,7.048284,-7.135417,-6.221264],[-1.598058,-4.477723,-9.589893,-1.714680,7.002575,-6.978783,-5.728683,-9.666021,3.656198,-0.029011,-6.602022,2.406217],[-3.675247,-2.629856,-3.671388,1.847864,8.630055,-9.266539,8.363528,9.921844,0.365029,-6.546065,-0.003413,-3.625029],[-1.893962,-9.445722,-1.684896,-9.901288,-7.272870,3.645905,4.154750,-5.190349,5.113064,4.153679,8.387373,0.524003],[-1.112290,-6.392376,4.324643,-0.210542,2.184033,-1.005594,-1.485788,2.576390,-0.570990,-7.638883,5.945036,-0.178342]],[[2.734199,1.509594,-0.615770,8.754743,6.663753,6.136881,3.368732,-3.337403,-3.523382,-7.384130,7.610527,-1.935873],[3.382839,-8.132474,6.699741,4.063596,-7.723361,1.483599,1.417345,9.219384,-0.274810,2.815977,7.307937,-8.638993],[6.693364,-8.452297,-5.655085,-6.583370,9.720344,1.760874,5.238416,8.609274,1.045653,-2.994035,-9.509287,1.407085],[-7.373729,-5.567616,3.567039,-6.517964,0.681305,7.297550,3.583958,3.600056,-6.500551,9.600745,7.872858,5.450655],[6.303686,-1.558621,-8.728887,-5.676667,-4.001852,-0.765606,9.767088,-5.959344,5.594098,0.448424,3.888053,-2.093811],[2.371193,7.446754,-7.024242,4.005357,-1.804715,1.618288,-2.213215,-9.256020,-9.315617,-1.469295,2.285613,1.225983],[-4.350121,9.685185,2.537787,-7.617703,5.751918,-6.961526,-1.868764,3.404079,6.184000,2.689384,-8.802681,-2.609637],[-9.375025,-3.020552,-7.486712,7.072958,-5.307384,-3.411949,-8.133982,-9.320045,3.515688,3.415047,2.767900,-6.316316],[-0.285495,-9.908143,2.622021,3.131024,7.035940,1.641248,8.240523,-1.448223,7.830527,-1.841284,3.659923,7.950755],[2.847076,1.121006,5.499287,4.081093,3.573521,-5.462910,-1.198281,6.921439,-8.410135,9.924833,3.222900,7.669651],[9.826491,-9.595389,6.587490,2.890447,-5.822611,8.550964,-8.965059,3.579049,-5.466560,7.038267,-3.210602,-4.191338],[9.327709,-8.416730,7.957464,-2.023467,1.615313,-8.638659,-0.584621,3.844912,-0.730710,0.874312,3.610749,-1.276741],[-6.021880,0.847803,-2.558076,1.408028,4.868055,-4.958972,-5.017744,5.254429,4.113978,-0.854154,0.351431,5.305212],[-6.534446,8.835460,7.729913,0.917034,3.325952,-8.132286,-3.516489,8.047662,-5.904795,-7.252843,-4.245064,-5.870551],[5.109035,-1.039190,2.984070,-8.131670,-0.270854,4.027566,-0.570910,4.853106,1.761878,8.204057,-1.874216,-1.951866],[8.273451,2.528540,-2.076311,9.255572,-0.282171,6.814138,8.324303,6.943436,9.528014,-0.332199,2.762108,4.303842]],[[4.761049,-9.893160,4.319727,-0.307215,8.342222,8.755496,-7.817330,-9.638294,-6.044595,-7.401439,7.299328,4.485280],[-8.008759,-6.626491,9.907685,3.395458,0.659728,-8.598260,-3.257867,2.530085,-4.942720,6.826453,5.267778,6.350019],[3.553113,-9.506316,8.507889,0.968246,2.606551,8.610052,0.593467,5.553859,-8.172719,-0.357304,8.075149,8.522527],[-9.555607,-4.560214,-9.887875,2.385182,8.955261,-1.333010,9.695384,-3.034935,-1.464977,4.237867,-9.718103,-8.923052],[2.198759,5.064093,-8.065415,-3.528355,-1.758661,-3.819930,6.795018,-3.679270,2.652516,6.213414,0.817230,2.156316],[-4.565572,2.201088,-4.940749,1.888310,-5.143499,-1.132791,1.763808,8.929345,3.579091,-0.798396,3.731585,9.837801],[-6.610967,3.030518,-9.524653,8.796461,-0.261381,-5.868074,-2.588814,-6.502378,-2.765451,1.112830,3.838693,1.638046],[-4.427254,5.598020,9.674532,2.723701,-7.014642,4.532683,9.777574,0.120609,1.968246,-9.151481,5.349596,1.661329],[3.622603,-5.337394,1.254289,4.778532,1.886639,-6.836534,9.879212,-2.853592,-4.100542,1.785196,-6.824890,1.146523],[-5.479382,7.544296,-6.762107,8.846081,4.205552,6.890754,-5.222412,6.357450,9.802254,-7.789213,7.252757,-9.778702],[-1.373742,9.960432,-5.236069,-4.327692,7.090612,4.425467,-9.423382,1.678226,-9.406417,7.089399,-9.302078,-0.491620],[-6.249698,-9.324945,-1.259015,2.520559,-2.114823,2.452900,-9.437489,7.085394,-1.562496,7.081403,-6.112911,-0.699979],[8.051906,4.133494,-2.447670,-3.934447,-5.536030,-1.690098,3.836761,2.773819,3.713447,6.225174,-7.391808,8.675615],[3.422529,-1.107660,6.660807,-0.891555,-2.668816,-0.227191,9.514350,6.284036,-8.303371,-3.766793,6.285525,7.996496],[0.244776,-8.389668,-5.650214,-1.193708,0.190636,5.500679,3.033173,2.200688,3.281055,1.270697,-0.662619,-9.947216],[-9.655034,2.529407,-6.502261,-8.296034,0.530258,9.377255,-3.014775,2.860519,-5.147994,1.010327,-6.502171,1.814448]],[[-2.723511,-9.580419,9.631464,1.183782,-6.569387,-9.313739,-0.412286,-5.666721,5.093785,8.559346,5.107459,7.958573],[6.158028,0.601237,-8.749915,8.605805,0.359975,5.486149,-6.079549,4.071615,5.027623,8.898365,-3.716690,3.164276],[2.619782,-8.513084,2.962949,1.439363,-5.618337,-2.120528,5.245656,3.652206,-8.163474,-2.007413,-7.273111,3.818695],[4.620978,3.722232,-9.128768,6.225930,8.671956,-4.326496,-6.163170,1.327797,-0.739463,4.709036,5.128346,2.470018],[9.595612,-7.100103,5.041671,-2.447427,-2.579602,-9.588139,-6.233796,-9.305175,1.019803,5.100036,-3.768969,-6.706058],[-4.108879,3.015024,4.941594,7.737402,-9.296674,-1.227999,8.588845,-4.202782,-3.511178,-1.383282,-7.163500,-5.520438],[4.711572,6.437279,-5.982433,0.327808,4.377272,-1.893346,0.105003,-4.347665,8.335142,1.853884,0.889169,-1.760706],[-8.589539,-6.412798,6.747009,5.792158,-8.941757,1.508327,-3.445049,-3.573924,8.973917,-7.311292,-2.116024,-8.310850],[2.989332,1.703745,0.172580,-7.889878,-6.711148,-4.494008,3.614190,3.099027,3.505975,-0.920792,4.300170,5.125978],[3.712342,0.011936,-0.368941,5.668390,8.507114,-6.875366,-0.930730,-9.000552,-4.964291,0.397591,-5.295022,3.281228],[1.831287,-1.802354,-4.690425,1.217703,7.136684,-6.213783,-8.646190,-9.648358,-4.457762,-1.554491,1.094338,9.536268],[3.242614,-1.941111,7.651245,7.303293,0.519096,0.822473,-2.837158,-6.567117,5.600652,4.133323,-0.384044,5.031413],[5.745586,-1.754188,0.770862,-7.083011,-5.874651,-5.511543,-5.539843,-1.287332,5.830688,-2.364213,-6.546609,-8.361522],[1.536137,2.718583,0.368196,-2.888707,-2.180760,0.726278,-5.004401,-1.964757,-4.124537,6.247727,6.246554,2.954923],[5.496463,-6.185473,-7.534547,-0.990471,-4.121690,9.853399,-0.515501,-1.568670,-3.981763,-2.953507,0.091711,8.977879],[-9.234375,2.773395,-0.780832,-5.968440,-3.707234,4.639884,0.609043,-1.712022,0.719553,3.271989,9.797425,-3.511369]],[[-6.948686,-1.221038,-0.824897,9.787939,-1.267071,-1.691646,1.790939,9.447728,1.871416,-0.117601,-1.756101,-3.428725],[3.849450,0.686715,-3.642071,-4.001483,0.191759,-5.051839,2.604553,-3.120228,-5.912274,-4.776792,4.903332,4.615813],[4.483101,-7.417405,-5.373614,7.636667,-6.275640,-5.762815,7.700936,1.270323,-1.122057,-2.726666,-0.073663,6.551892],[3.381281,-9.546779,9.321864,3.330576,-6.181171,-3.846871,-4.273890,-3.223434,8.507769,0.497476,6.600240,8.420272],[3.009661,8.096098,-5.133412,-2.299529,2.132177,-1.208797,7.109462,5.573410,9.547490,-7.740365,3.445884,6.881273],[-8.567515,4.182739,3.655153,5.235573,-5.991566,-4.472726,6.092871,-6.975075,-1.124678,-8.949139,-0.173150,3.396956],[0.293233,-9.033941,-6.007464,5.333116,-5.082010,-8.150874,7.240981,-3.988900,3.337297,-8.802301,-5.062472,6.537599],[-2.131127,-0.653461,8.124797,-0.862992,7.533244,8.206258,-8.041796,-6.710020,-5.998175,3.361763,-4.598908,8.879257],[-6.217094,3.500221,1.021419,8.580846,-3.274489,-7.654886,9.963258,-1.599087,3.522279,-8.553090,7.563908,5.912697],[-2.521104,3.729291,-6.061049,-5.157076,7.862244,5.935294,-3.703277,-2.933621,-5.265533,-5.470075,5.503503,8.255307],[-9.198318,5.112190,-6.848354,2.013896,5.438377,-0.744250,-3.675026,-6.342772,-8.485681,-9.154264,8.807527,4.160506],[2.478753,8.503279,-6.526816,-6.559762,0.007437,-3.229255,-8.822758,-4.672219,6.692797,9.489839,6.635694,4.203227],[-9.293010,-7.437231,-5.126450,4.083849,0.887762,-6.812513,6.369742,-8.767580,-7.954022,4.270605,1.821773,-1.660692],[-3.714914,-2.692334,-9.347856,5.070785,1.724550,-5.871916,1.755276,1.336133,-3.355828,-7.870173,-3.494882,-6.713544],[-2.317187,8.282182,0.191384,-5.705612,-6.264274,5.986562,-0.969800,3.920362,-9.036707,8.837458,5.002388,-9.249792],[-6.587898,-2.526859,-5.740169,-8.873305,-9.773855,-2.867877,5.377422,1.572904,6.576346,-3.294342,9.962732,4.767047]],[[2.623166,5.385369,7.243916,9.562072,-3.456942,2.935621,-1.989072,3.525565,6.764866,3.942475,-5.173847,-4.655992],[4.489035,1.059992,-6.178377,7.494422,8.119022,4.734365,-4.002733,4.611422,-9.333510,9.082266,-5.711542,1.566410],[-2.088837,-2.490876,0.427658,-9.569517,-8.934220,2.263055,-2.029793,-1.399363,4.685974,6.252586,-6.086262,-0.578884],[9.600623,-9.882735,7.018853,2.733389,-3.832708,-1.880685,4.406558,-3.692960,1.029762,-7.916502,-7.455223,6.320377],[-8.232506,-4.739540,1.424504,5.023099,-5.381664,-2.583456,5.280039,-5.704868,-0.384932,5.872894,0.375242,2.754627],[1.519101,1.346378,-8.820689,1.640332,0.580649,-1.927658,1.519530,0.658418,1.244653,8.829297,0.649171,-7.669909],[-0.842768,9.564433,7.199727,-7.553354,7.828486,6.782854,5.267054,-7.432685,-4.438698,1.017957,6.273835,8.471234],[0.284052,5.997206,-1.970615,-9.620054,-2.459345,3.650352,-3.401165,-6.375559,5.956872,1.172561,2.933966,9.222180],[-4.908542,6.715370,3.876336,-1.432445,2.682916,0.650127,9.912267,-7.788885,-3.093183,-7.272523,-2.272030,-6.074573],[-7.909250,-9.314049,2.704738,3.155635,-5.713315,9.798834,0.721914,-5.672492,-0.470237,9.979350,8.929600,6.373665],[3.253593,-7.684444,-9.464161,1.445190,5.837608,-0.423059,6.687961,-8.319518,-0.194840,5.850923,-8.393117,-8.605664],[6.183611,-1.448504,-8.996792,-1.355036,7.659077,8.333481,7.695309,-8.644710,-5.742082,-3.795755,-4.153604,8.164366],[-0.164226,3.585762,8.397432,0.199380,7.588713,5.276938,3.904987,0.156694,1.511137,9.252622,5.267877,3.312807],[-2.049114,0.594948,-3.113675,-7.669004,5.306228,7.340183,0.470063,4.312947,0.767309,-4.465238,1.960858,0.834046],[-6.432639,1.153418,8.053565,9.239537,-8.577353,-8.454341,-7.149963,-2.588391,-3.936152,-3.656004,-5.670725,-3.470162],[-2.573979,1.283181,-9.792810,-4.849540,0.373241,-5.453465,-1.243547,-7.643504,-6.116910,-3.310704,5.298555,-2.308629]],[[-4.929139,-6.601289,8.777109,-2.093633,6.473730,1.555568,4.048986,4.004415,7.531160,6.931611,2.499670,9.259272],[-0.561522,-7.836538,-8.190486,-7.614117,2.316055,6.139970,0.548899,2.786207,8.398446,1.319449,-3.802916,7.384426],[-3.325246,-6.951550,9.583367,-0.505540,6.309766,2.709961,3.556596,-3.017536,-6.815819,9.542317,-2.410971,3.213162],[4.238268,-9.910863,2.014474,-7.245661,-5.102310,2.854160,-8.573693,4.813538,6.503407,0.848814,-6.139737,1.749550],[1.776154,0.692770,3.502352,-1.662696,2.537636,1.275611,-3.941562,-0.542994,-9.558547,-9.501261,3.105844,-9.359945],[7.263746,-0.793845,2.550741,-2.475134,-4.012184,-2.427395,-9.745196,8.112677,3.607763,-6.789630,-2.204413,-5.035988],[4.547303,4.550787,4.509133,9.646396,5.591054,-3.924471,1.595786,2.319420,-2.918308,-7.906230,-5.012395,-3.508042],[-1.216644,-7.561240,-3.764303,4.609389,4.142767,-2.364944,-4.162766,3.693660,2.779712,-0.025182,3.986897,1.984698],[-1.363247,-0.868298,8.749725,-6.761387,-4.771641,-1.254085,-8.824609,-2.039721,-7.213510,-4.617960,-5.326969,-6.489846],[7.742161,-1.106789,-6.811518,9.083565,3.731913,-0.794004,-8.350296,-8.665811,9.240766,2.741566,-2.773241,0.339309],[4.179249,5.337660,-1.984639,1.959143,6.695942,-4.646416,4.400946,-8.836601,5.335987,1.262695,5.771481,-2.604497],[-3.290247,-7.289840,5.030787,7.964826,2.592959,-2.761302,-1.672890,-9.533066,-6.434850,-2.755185,-4.139088,-9.839017],[0.575963,1.151372,-8.916462,2.809334,-6.872214,8.326361,8.022901,-2.494286,-0.949507,-4.887170,-8.837208,-9.429176],[3.177665,6.954680,8.054539,-5.142671,1.840378,5.419175,8.157310,8.061655,5.136334,-8.204323,0.027463,1.087751],[4.226388,2.925052,-6.615095,-7.905646,-0.748677,5.504838,-2.426226,-5.115698,-3.684620,3.995319,-9.412609,8.754233],[7.285874,-1.319682,-5.473754,-3.165552,-7.987448,5.845314,2.771461,-3.058165,0.361646,8.629349,7.106079,-4.855618]],[[-7.018093,-3.423659,-9.045644,-4.510678,2.974844,-1.581862,-1.483818,0.490504,-9.857851,-6.084823,7.189593,1.095446],[-1.599267,-4.519851,-2.395675,1.513296,-2.327431,6.426662,3.664901,-6.966918,5.038213,-6.981045,-5.904064,-6.643371],[8.182830,-1.818786,1.403625,6.489035,2.407864,-6.901341,-4.069483,-7.083185,7.405915,4.271051,7.662709,5.660983],[4.347708,-5.950877,5.984931,-2.620252,1.651896,3.223168,3.379356,9.138366,-9.962014,-3.976835,1.685018,9.671032],[9.819170,-6.490826,9.507643,4.758478,7.449456,-4.025059,-8.762062,7.599523,2.986809,-5.297869,-1.357488,0.939351],[7.803714,8.440590,-1.818698,9.805624,-3.234749,-1.639481,3.215709,-0.797660,-1.873181,-6.640442,1.330527,-9.066589],[-3.485610,7.507788,-3.046459,-1.016303,0.312935,3.266031,-4.659920,3.335815,-7.380940,-5.117864,5.449651,-8.111280],[6.305404,-5.584211,8.477892,-8.094035,6.294319,-3.174636,-8.926808,-9.563971,-6.885023,-6.386943,-7.347614,0.303668],[6.177175,7.084409,-9.193277,-0.899091,-6.513109,5.588864,-0.828875,0.916121,8.629198,8.544739,-1.397785,6.641034],[1.079440,-2.166839,8.392646,-8.078032,9.692325,5.618076,-8.344736,-5.984893,-8.551811,-5.100529,0.191852,9.996888],[7.130888,-1.262753,-9.887010,-2.016249,2.255981,3.696869,6.130182,-3.828293,6.571994,-4.076720,9.525532,-8.472442],[-7.409159,-0.595421,4.922980,1.704090,5.441565,-4.052786,7.261601,1.712218,5.541310,-9.425609,2.784667,-1.945439],[-5.645578,-7.705215,5.370711,-1.137615,3.580758,9.176210,-8.777040,4.404570,-6.069267,3.991566,-4.616709,8.714209],[2.524618,-8.063555,-2.402335,-7.527937,-2.624406,-1.574601,4.302187,5.331864,-9.305603,7.275251,3.148409,-3.816164],[8.413361,-2.297416,-9.666496,6.099596,8.406007,-0.471657,-0.771011,-8.344427,1.593919,-7.599244,3.014006,4.696840],[-2.609499,-5.857428,7.807658,-1.939895,-5.479957,7.194332,-4.726370,6.417186,-5.669914,5.433412,-9.035516,2.771980]],[[-2.481959,-1.497996,-1.881815,9.015785,8.895087,-0.821590,-3.115617,1.247825,8.792475,-8.522727,4.179941,0.377667],[3.733332,0.727468,2.897178,-9.574005,-4.405594,8.046164,-5.117397,-7.657971,9.890167,7.870346,6.415249,-0.451095],[6.285940,-2.943953,-0.295056,-1.659682,-2.374935,6.443638,4.351799,3.030528,6.889622,-1.674961,-7.715786,8.530763],[0.729735,8.418514,8.274870,-0.780743,-4.173095,0.645707,-2.250502,9.949954,0.566313,-5.145296,-8.048475,2.743257],[2.257810,9.445927,-5.682128,3.990920,2.623582,-7.277240,-0.566026,9.941117,9.452630,-6.206337,6.548665,-5.063351],[-0.037457,2.047234,-8.449402,-9.421048,-5.120981,8.313605,-9.423963,-3.579529,-9.983859,-7.991406,5.750434,4.086932],[9.241784,7.590056,1.033709,1.076441,-3.404957,-4.520946,4.642034,-2.372753,2.339093,-9.535616,-3.123895,3.404237],[2.406751,-6.440122,-1.940146,5.878894,1.880024,-7.666178,-7.953954,-7.951896,-8.889411,-6.315723,-3.616320,0.801823],[-6.420954,0.153892,-8.787068,7.264528,5.177182,5.642656,-5.964129,9.072965,4.726598,-6.176763,3.583875,-6.011978],[-7.111595,-4.797997,-7.812960,-3.728068,1.660665,0.283697,-6.969219,-5.812310,-2.947525,0.067403,-9.180578,-1.296605],[-7.287894,-4.123538,-6.316057,6.765336,4.040934,9.183656,1.006722,-3.191957,6.758159,0.041366,0.892665,7.135260],[3.058853,-5.050741,5.735893,0.523218,3.657425,-9.956566,-8.893943,-1.829236,7.712371,9.331028,8.804409,2.111769],[-5.108353,7.897149,-9.147151,0.137391,3.939640,-6.285449,4.330943,4.139167,4.492392,-6.655586,6.735460,9.861505],[-0.529456,-5.385874,-3.138643,-5.972217,-6.559521,-7.844058,3.187448,-8.049388,9.884775,2.602685,-2.880511,-0.313260],[-2.767803,2.963066,4.120944,-3.822957,-9.687748,-7.400604,2.498041,4.490107,-1.079280,-7.234243,6.753734,-5.579046],[4.963353,3.597500,-8.999226,3.661030,-0.036713,3.724493,7.863558,4.257781,-7.492521,1.091212,7.096222,8.690002]],[[-6.424422,4.699777,-8.848787,5.277917,3.898415,3.790649,-7.287437,6.876809,4.361174,-4.208895,-9.859895,-8.529703],[9.041502,-1.197019,-7.654576,-3.064173,-1.147607,4.999255,-6.263246,-4.328872,2.019355,5.483713,2.052781,5.199306],[2.463145,7.336807,7.091818,-4.725791,1.372370,5.811578,-5.586311,5.058352,8.141217,6.683382,4.220964,-3.455015],[6.771042,-9.861459,-2.369121,-2.074457,8.869831,1.135012,9.838677,-2.472083,1.498160,9.625231,4.556648,-4.566993],[3.597367,-5.103546,6.414617,8.182803,9.945927,7.712683,5.975233,6.094992,-2.385523,-5.106417,2.061118,-2.683548],[-6.137530,-6.234366,-4.117353,1.926648,5.506502,-1.974380,-3.403273,1.938593,8.237388,0.950061,-5.979828,-5.533032],[9.727361,2.227429,0.542747,4.901897,4.717121,4.140433,-5.804235,8.848854,3.032343,3.202716,8.022873,8.523533],[8.237214,-7.765958,3.674959,-9.454434,0.974684,4.089848,-1.801618,-3.567532,9.428223,3.072428,-7.683509,2.888870],[8.624611,8.217569,6.647510,9.023333,4.383004,1.886945,-3.680641,-6.658483,6.973781,-9.278047,-4.613670,5.089334],[1.306682,-2.815713,2.828706,5.603753,-6.149312,4.625593,9.718503,-1.898647,-2.573452,8.652527,-6.089374,-5.774803],[-2.169805,0.859597,-8.462195,-7.710879,3.300158,3.146089,-1.981409,5.931096,-5.952210,-3.069394,-5.431660,-6.296061],[-8.606809,2.868416,8.606318,-6.250018,3.343454,3.582754,-8.410811,4.414286,-0.150615,-9.511621,0.429921,5.933916],[2.879793,5.975387,-5.668701,-7.497445,4.732982,5.688388,-5.667177,-3.632995,6.635428,3.213528,2.285616,-1.583247],[1.827860,-5.755967,-3.967845,-0.662316,-9.371617,0.178449,-4.738826,6.995744,-0.671436,-1.464224,5.386131,-6.527179],[-1.453067,-9.334682,-0.343191,6.552407,-6.820758,-7.004495,9.375692,-4.222408,-1.251389,1.834123,5.788350,-7.097040],[6.952875,-9.458925,-6.139532,-6.034499,-7.862283,-9.415707,9.978956,8.228426,-8.498306,-5.257392,-9.660501,6.397071]]], dtype = "float32")#candidate|9453|(14, 16, 12)|const|float32
uop_9454 = relay.rsqrt(const_9453.astype('float32')) # shape=(14, 16, 12)
output = uop_9454
output2 = uop_9454
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
	relay.transform.MergeCompilerRegions(),
	relay.transform.Inline(),
	relay.transform.LambdaLift(),
	relay.transform.LazyGradientInit(),
	relay.transform.PartialEvaluate(),
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
