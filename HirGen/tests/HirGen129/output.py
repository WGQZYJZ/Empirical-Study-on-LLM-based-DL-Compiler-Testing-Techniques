import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_33 = relay.var("var_33", dtype = "float64", shape = (13, 10, 1))#candidate|33|(13, 10, 1)|var|float64
const_34 = relay.const([[[-3.137048,2.172360,1.736859,-8.165026,-9.486103,-5.245277,-7.950572,-2.409526,2.859420],[-1.999626,9.051118,7.129200,-4.638452,-2.201390,-3.339710,5.220840,3.786337,-3.508985],[4.795516,-9.943765,7.552906,2.898286,3.253532,-0.273571,-2.556926,6.396828,1.226882],[5.795262,8.666962,5.688640,3.236681,-0.571559,5.400759,-4.599622,3.746142,-9.711735],[2.238520,-5.239510,-3.512138,0.317077,3.418699,-6.922710,3.193280,1.516759,-6.634173],[5.736084,3.322736,-8.869212,-4.158893,-0.987736,5.935840,5.287322,-7.464926,-6.060849],[-3.904369,9.576717,-6.085009,-8.479743,7.362536,-2.938286,-6.372128,-2.062989,3.187567],[-7.820440,1.381093,3.221961,-8.534514,6.451133,-2.360798,9.632773,-1.956051,5.771151],[-7.308830,-6.584191,5.857319,3.097036,-2.459036,7.145857,-3.278299,-0.742797,-4.619893],[7.632917,-7.800445,7.048898,-3.781188,3.222877,-1.336672,7.176321,-6.213179,-0.155006]],[[2.274256,2.228431,0.449550,9.163100,-8.089731,8.912377,-2.377804,9.374762,-5.588898],[7.842319,1.476963,0.602582,2.998480,9.913462,-5.056593,0.437668,8.910366,-7.557603],[-9.780135,3.671430,6.617591,7.685893,2.880833,-9.576510,-2.769287,-3.149332,-6.990467],[6.697204,-6.435828,0.591066,-4.424009,-7.486803,0.346807,0.789078,5.107925,-0.495588],[3.684644,-4.713279,7.136686,-6.924021,-6.141638,7.344386,-7.458522,8.150646,4.626780],[-6.651841,3.999085,-1.386104,7.520002,-2.811152,-5.091305,5.941062,7.300860,-2.281127],[-4.502503,-0.867490,8.640032,3.159714,-8.429871,-0.067328,0.525525,3.193412,-6.667903],[3.640270,1.000578,-5.518216,-9.593255,-9.813119,5.705697,-1.424687,2.641929,-9.121070],[4.058212,3.914247,-6.956134,5.723022,-0.498806,4.028638,-8.960560,-8.767670,-0.107306],[8.668494,-2.794095,-2.054206,-8.952620,3.800229,5.034140,-5.034936,3.807824,-8.142093]],[[-1.078567,9.345809,2.064827,8.315356,4.884920,0.286302,-5.684238,-5.733061,-4.875528],[-8.355195,-3.658409,7.596125,5.818430,-7.526602,9.441980,6.523357,-4.900402,-6.949642],[3.465996,-8.225783,7.850500,-6.018744,-4.255869,-0.314223,-5.269484,-0.425047,-7.225938],[-1.315385,6.148605,-2.378157,-2.563729,-6.439438,-1.369076,-6.174818,-3.591057,-4.203588],[-9.943335,5.395238,8.262386,-8.343551,-9.399445,-4.472532,-3.825450,4.213821,3.036350],[-0.890463,3.473979,4.274420,2.877964,3.269627,-5.424635,2.279520,-5.804898,8.797562],[-2.123250,8.403372,-3.736200,0.575107,6.590728,3.165698,-3.191353,-0.370805,-6.261391],[3.171105,0.823769,-1.119786,-5.568201,-6.672965,-8.524912,-5.939635,1.565987,-5.461073],[-4.186928,-3.066838,-9.355054,-1.722660,0.893178,-5.264584,-5.309134,7.955008,-3.035122],[3.260920,4.581294,2.556663,-0.270623,-0.465698,-5.821037,9.607024,-7.121726,-5.171442]],[[2.368241,0.905334,0.956031,8.285490,6.030416,7.604726,-1.344257,-4.944332,-2.826988],[8.095455,-1.587670,7.276081,-7.381023,7.365629,-6.453862,3.297006,-7.600167,9.821569],[-8.914647,-7.383471,8.951642,7.426493,-7.009668,-4.341819,-1.537620,3.272981,9.360454],[1.538062,-6.085812,3.024187,-1.773355,-4.523173,7.962748,-2.117294,-9.351042,-0.803348],[-3.475290,8.679694,8.321976,0.320300,-5.561563,-0.896411,0.527864,5.602573,-7.370089],[3.947210,-5.219363,-7.179015,0.597425,5.087522,1.755053,2.379555,-2.718744,-5.551080],[-7.203280,6.628643,0.064800,0.811761,3.539774,-2.201034,2.851896,-5.929862,4.238986],[1.883146,8.705378,3.970304,-4.713048,-7.507473,6.091632,1.969427,-6.360372,-5.801429],[-6.573874,2.281517,7.190956,-2.106536,2.559497,-8.006314,8.108980,1.274881,-3.062085],[4.567017,1.236911,3.114195,-3.984009,6.667009,7.707541,-6.256113,8.739352,7.537708]],[[8.693889,0.346603,-7.027847,-5.349536,3.002186,-8.811655,-7.575868,1.139566,7.257700],[-4.954608,1.508603,0.709668,-7.524552,-9.686822,6.812949,-9.668064,2.668434,1.875611],[0.758169,2.953102,9.569380,-6.188424,0.030936,2.765567,4.911751,2.598504,8.029367],[6.572247,-8.467971,9.777724,-0.368110,2.589890,2.409681,5.369267,-9.647445,-0.130777],[2.614564,3.230217,-8.322876,1.358993,-9.826382,-3.195889,5.313721,3.618115,1.631089],[4.868710,-8.511281,-3.927901,3.456998,-2.333288,-4.137415,8.888948,-4.675440,7.159489],[-6.541870,-0.401871,5.685192,-2.395173,-8.915147,-4.640706,1.565702,0.967415,-9.334888],[7.759139,-3.068315,6.742790,-7.286625,-0.814339,6.232903,1.350726,-8.852821,1.793339],[-3.091699,9.927883,5.170055,9.853208,8.569672,8.704257,-8.629931,-1.691782,-6.120706],[2.673471,-8.212625,2.188100,1.522219,9.665072,-5.705197,5.918557,6.149244,-2.289303]],[[9.782553,9.277671,-7.966132,-1.506527,0.699279,7.034787,3.679808,8.575112,-7.081205],[7.975535,8.894023,-4.300925,3.059253,6.259749,-3.472911,-2.367048,1.800989,-9.337126],[-1.660370,-6.136861,7.411578,9.907121,-9.709946,2.532546,-6.146625,2.460786,1.834104],[4.141556,8.093430,4.394241,-8.093506,6.635120,9.643787,-6.626168,5.423561,-7.058863],[-4.955495,5.175700,-5.612218,-2.355906,9.547021,-8.140784,5.179599,-6.763823,-0.390517],[-1.403156,3.830173,-1.546915,1.951341,-1.536186,0.756373,-4.924161,-5.882892,6.681192],[-6.492252,2.721039,3.255778,-2.588635,-5.140042,7.585017,1.143923,0.746949,-2.403382],[9.333408,-2.276507,-6.741804,-0.110187,-2.153573,-0.525081,5.501516,9.153145,-9.163906],[4.683495,4.274498,6.392884,-7.532500,-4.255666,8.076987,-3.819414,-7.923163,-1.232393],[-5.893786,2.479388,-6.598741,-8.484635,-3.338955,-9.314899,-2.985029,-6.590062,6.404215]],[[8.151783,-3.936944,-1.408861,-1.224577,-4.115128,4.389317,6.908169,-1.439725,-6.828190],[-2.795662,-5.062826,-1.130489,5.826272,-2.860261,-6.196874,-6.513184,-7.995781,0.980871],[-5.181337,6.871586,3.524800,-4.574752,-0.511196,8.561714,4.992884,-7.780417,4.759840],[-3.488594,9.467667,-1.707303,1.017072,8.127966,5.658625,-7.586418,-3.412404,-5.342829],[-2.671827,-9.016184,0.720895,-0.857707,5.868662,3.223094,5.118734,-3.600177,-4.642226],[5.320933,3.201884,3.155438,1.533074,-4.914796,4.253702,1.809667,5.069686,8.265117],[-3.571883,6.346992,-0.841649,-5.617510,6.254090,-9.352930,2.151688,5.802597,1.702597],[7.687547,-6.009592,-6.283590,-7.155531,1.940047,-9.959606,1.818513,-7.883954,-6.956064],[0.747982,1.034874,7.613274,-0.668715,3.038994,3.381967,1.054061,5.652147,7.892792],[1.495062,-5.417013,8.311668,1.936831,7.230013,-1.273016,-7.115536,-5.537833,-2.527494]],[[-9.857080,-9.611789,-1.235771,-9.408406,-7.222816,9.345240,1.726024,0.702284,3.753308],[-1.509990,9.487417,0.494674,-8.944425,4.638781,2.977017,-4.828430,0.666795,8.491095],[9.405842,4.714806,1.025835,1.532669,0.456786,-1.927933,0.833518,-3.889554,-8.127150],[-0.098282,7.266602,2.936343,3.199548,-4.619722,-0.442048,-2.251229,1.941163,1.535548],[-4.737022,-6.969174,-0.018323,8.904729,3.065053,-4.896715,3.031141,-2.532121,9.961708],[7.853484,-9.377546,5.100862,5.557120,-6.552099,2.971082,8.441430,-5.216015,6.187280],[0.879962,-6.642355,-3.209522,-6.322714,-4.717998,1.184503,1.639704,-4.494583,-1.047129],[-9.354811,-5.945556,4.009933,7.439344,9.576035,-1.635595,-4.729212,3.780251,-1.525070],[6.281064,5.281639,-1.684110,3.734348,4.027949,5.867143,0.501040,7.783532,-6.491012],[2.409322,-0.067018,4.495768,-4.418439,-6.868441,-9.044341,0.621264,8.733370,5.275241]],[[3.223752,9.439550,9.016710,7.583201,1.181382,-7.023345,1.063590,5.571812,-1.649826],[-3.482939,-0.765683,3.731001,0.644448,-9.226267,2.621202,-6.117053,6.644212,-4.901779],[-3.296036,0.849388,-7.405638,5.462170,-5.259007,7.126014,6.333468,0.641885,-5.285700],[3.598552,0.040033,7.981830,8.459618,-3.096565,8.214114,0.829897,-7.616075,6.646475],[-0.357003,-5.479215,2.501473,-5.361882,0.844787,-4.695863,-0.601854,3.901584,-4.210794],[-6.211378,4.511544,-5.052810,0.622728,-0.567926,-9.228515,8.628216,9.839691,3.079478],[5.533830,3.955661,6.540141,4.864695,4.818553,-2.618642,9.078019,-4.148303,4.630863],[4.476921,-2.831340,-4.287025,-7.955161,-6.824909,2.548377,-1.179506,5.188160,5.612351],[-4.152606,-2.366263,1.671489,3.167987,5.523061,1.615292,-3.238879,-5.352677,1.285667],[4.666549,-3.132716,8.044913,-2.833565,-3.088988,8.788093,-1.852915,-8.678964,-3.823136]],[[9.294546,-3.113947,0.590203,3.023410,5.848358,-5.668266,-1.473694,-4.978648,0.343601],[-4.129559,4.602533,0.416221,-7.503586,-0.975214,-6.105507,7.271901,-0.086729,5.301548],[2.632322,3.160226,-3.525468,8.501992,-3.267847,9.738833,2.928614,6.805618,-7.034037],[-8.526903,-8.211560,-5.683928,4.193900,6.914981,6.418664,7.543157,8.885107,9.859113],[-6.771198,1.699776,-3.343261,5.249034,-5.432451,1.975842,1.407002,-8.165451,-4.772872],[6.707315,-7.676457,-3.593539,2.730492,-2.707699,-4.973963,-2.179278,4.679359,2.373376],[-4.834257,1.593751,1.496348,6.265931,-4.399939,8.802459,-5.229905,-1.884794,2.866499],[5.193021,-6.986562,9.944012,6.781006,-8.517312,1.564134,2.544079,-3.591973,1.179400],[3.282400,-9.496192,-4.401412,-6.361974,-0.594727,6.438390,1.380257,-8.255626,-1.415404],[7.596446,3.874613,-6.263722,3.161202,-1.177159,8.773847,-8.692631,4.544692,-3.130637]],[[-4.622437,-6.612349,-2.046672,-6.751708,-7.221038,8.732260,-0.030559,5.158819,-6.124299],[7.447194,2.345553,2.880875,3.671528,3.567287,2.425803,-2.192467,-8.401301,-1.688151],[-7.671314,0.300762,-3.880053,9.782132,8.442853,-4.713002,3.957835,6.745296,-3.697375],[8.814391,-9.958889,-5.255869,-8.672144,4.493450,7.188391,4.172678,-0.070967,3.926583],[-6.251919,-3.599566,9.137283,6.711228,-7.605647,5.015334,-6.691695,-4.671921,9.867620],[-0.778432,0.571384,-7.011613,0.293457,-5.471343,-2.164617,-3.454486,-2.674765,-9.045219],[-8.457807,-3.962917,9.251997,3.889668,-4.201195,-2.912382,-6.651859,-8.428813,3.105679],[-3.119975,-9.234285,-7.225182,-0.647602,5.404865,8.737367,-8.722590,-4.585909,-3.877348],[-0.520558,4.528768,3.668666,-5.581985,-7.353658,5.762223,-1.393036,-0.047114,-4.689654],[2.555508,-5.294003,-9.099172,6.818532,0.718944,4.698130,4.472626,2.154869,7.298594]],[[-0.424540,-8.912577,-3.494705,-8.334680,4.863650,1.007123,-5.628526,1.574821,-0.309254],[-6.892590,-6.824681,4.460793,-7.097329,-2.887237,6.444638,-2.208868,9.484673,-3.289894],[9.461457,-8.087134,1.543812,-5.190916,8.144684,-3.656415,0.967057,9.605982,-2.107861],[-6.537189,2.500769,-3.622158,-9.790554,-6.737782,4.928270,0.722908,-4.592816,-8.582642],[1.013097,1.290576,-3.135108,-2.181500,-1.945475,8.417880,-7.818677,6.305955,-6.614403],[-8.152632,3.752456,8.506386,0.572415,7.928978,-0.813529,-6.868308,-9.492347,-4.102763],[1.860961,3.838839,-8.747363,9.815222,-7.273642,-7.264117,-4.947087,1.818223,-7.218403],[9.630473,7.776736,5.832639,-3.812752,3.379578,1.475270,1.743542,7.234157,-2.712765],[6.716881,-0.365793,8.905549,2.342903,-4.670298,9.989052,7.605769,-3.869790,5.593579],[-1.287619,9.660037,-1.887843,-5.634171,-2.591170,-4.058426,5.371903,-0.463369,4.748719]],[[8.605957,8.170260,0.755951,-2.838708,5.419773,7.942177,-2.690042,-9.468035,-5.249044],[-9.064080,-1.984135,-7.079518,5.301468,1.641420,5.631078,5.587912,9.974733,-3.781206],[7.490786,2.235422,-6.073880,0.680050,-1.071536,-0.470501,3.130996,0.857976,0.998017],[-9.551474,-4.369935,-9.930021,1.692912,-4.511158,0.908663,7.471154,5.702639,5.725615],[-8.544480,-2.105098,6.285656,2.268832,0.669117,-3.138213,-8.539127,3.489313,-9.300839],[-1.152418,-0.232313,-3.579884,-3.455862,-3.376023,-5.505900,5.075782,2.341070,-1.473370],[-0.462276,6.518531,-2.925382,5.934054,-2.537560,2.122264,-9.907926,-3.381009,-4.813319],[-8.017414,8.920252,-9.813607,1.130916,-8.612940,5.620793,0.543462,-1.282610,3.859065],[-6.057265,3.265503,-0.986859,-4.200772,-0.464679,6.386435,9.513835,6.325174,-6.426320],[2.250716,6.795896,-9.602124,-7.459153,4.273058,-8.251367,7.058016,6.046246,-4.228296]]], dtype = "float64")#candidate|34|(13, 10, 9)|const|float64
bop_35 = relay.add(var_33.astype('float64'), const_34.astype('float64')) # shape=(13, 10, 9)
output = relay.Tuple([bop_35,])
output2 = relay.Tuple([bop_35,])
func_50 = relay.Function([var_33,], output)
mod['func_50'] = func_50
mod = relay.transform.InferType()(mod)
var_51 = relay.var("var_51", dtype = "float64", shape = (13, 10, 1))#candidate|51|(13, 10, 1)|var|float64
output = func_50(var_51)
func_52 = relay.Function([var_51], output)
mutated_mod['func_52'] = func_52
mutated_mod = relay.transform.InferType()(mutated_mod)
var_161 = relay.var("var_161", dtype = "float64", shape = (1, 10, 7))#candidate|161|(1, 10, 7)|var|float64
uop_162 = relay.log2(var_161.astype('float64')) # shape=(1, 10, 7)
bop_189 = relay.bitwise_xor(var_161.astype('int64'), relay.reshape(uop_162.astype('int64'), relay.shape_of(var_161))) # shape=(1, 10, 7)
uop_197 = relay.cos(bop_189.astype('float64')) # shape=(1, 10, 7)
bop_204 = relay.right_shift(uop_197.astype('int8'), relay.reshape(var_161.astype('int8'), relay.shape_of(uop_197))) # shape=(1, 10, 7)
uop_207 = relay.tan(bop_204.astype('float64')) # shape=(1, 10, 7)
bop_211 = relay.power(bop_204.astype('float32'), relay.reshape(uop_197.astype('float32'), relay.shape_of(bop_204))) # shape=(1, 10, 7)
func_50_call = mod.get_global_var('func_50')
func_52_call = mutated_mod.get_global_var('func_52')
const_218 = relay.const([9.197954,-4.179336,1.981529,0.980942,-0.761425,-4.345415,6.926874,-7.766955,8.313710,1.517697,-7.298798,9.385552,-6.643761,7.204408,0.566297,4.878483,-4.638410,-0.464948,3.473923,8.817454,5.128641,9.230724,5.378925,-1.456168,6.373197,9.562481,6.129675,-5.255884,-2.877937,-8.137324,-7.816841,5.674766,4.972955,9.875438,5.635483,-2.632887,-3.136835,9.802854,1.297374,7.717856,-5.087167,1.822698,5.704611,1.573862,0.915464,-0.528952,7.169517,-4.745520,3.151393,-0.023822,-5.512127,6.679439,-2.230651,-9.150565,-5.275176,-0.011292,-1.389792,0.633987,9.580864,-8.841299,-2.431483,-0.352274,-5.490986,-0.358136,-6.238677,-6.295328,-0.121672,-3.636420,5.075904,-0.964529,-4.958756,-4.847069,-0.817341,-6.061969,-7.466313,-4.159240,8.758578,4.490916,4.682452,2.460279,-9.876287,-9.739911,-4.203221,8.091374,7.208396,0.057089,-1.332726,5.085214,1.843447,-0.695269,-6.306139,-3.573530,0.260032,5.113041,-3.482518,7.686430,-3.414099,5.277017,-9.332053,-9.530526,-5.229751,4.806860,6.762653,-8.859647,-1.338082,9.626799,2.161245,3.678476,2.286160,-2.873420,0.110949,-6.136785,2.666882,-7.613823,-2.424641,-5.275711,2.539327,3.734954,-6.980552,8.481876,-8.761597,6.397469,7.946508,-7.009846,0.699870,-1.388957,-9.359722,-0.451703,-8.800062,7.698451], dtype = "float64")#candidate|218|(130,)|const|float64
call_217 = relay.TupleGetItem(func_50_call(relay.reshape(const_218.astype('float64'), [13, 10, 1])), 0)
call_219 = relay.TupleGetItem(func_52_call(relay.reshape(const_218.astype('float64'), [13, 10, 1])), 0)
func_50_call = mod.get_global_var('func_50')
func_52_call = mutated_mod.get_global_var('func_52')
call_233 = relay.TupleGetItem(func_50_call(relay.reshape(const_218.astype('float64'), [13, 10, 1])), 0)
call_234 = relay.TupleGetItem(func_52_call(relay.reshape(const_218.astype('float64'), [13, 10, 1])), 0)
output = relay.Tuple([uop_207,bop_211,call_217,const_218,call_233,])
output2 = relay.Tuple([uop_207,bop_211,call_219,const_218,call_234,])
func_235 = relay.Function([var_161,], output)
mod['func_235'] = func_235
mod = relay.transform.InferType()(mod)
var_236 = relay.var("var_236", dtype = "float64", shape = (1, 10, 7))#candidate|236|(1, 10, 7)|var|float64
output = func_235(var_236)
func_237 = relay.Function([var_236], output)
mutated_mod['func_237'] = func_237
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1265 = relay.const([[[7,-2,-10,-5,7,7],[5,8,-3,-10,-4,9],[3,-2,-10,-2,10,9],[3,8,9,-5,1,4],[4,9,8,-2,10,6],[2,6,-6,-3,8,-8],[1,3,-9,-5,3,-3],[-10,10,10,-1,-5,-4],[1,-9,3,7,-1,5]],[[7,4,-4,1,-1,5],[8,-4,2,-6,-9,3],[10,-5,2,2,-2,1],[3,-1,10,6,1,-3],[-1,-7,3,10,1,6],[-7,-3,3,4,-4,10],[10,-4,-9,-3,5,9],[-9,-1,6,4,-6,-2],[-10,6,-1,10,6,2]],[[2,-4,-5,-4,3,5],[-3,-3,-5,-9,-1,-9],[-3,2,2,3,-1,-10],[1,3,9,3,8,-4],[-1,7,10,-4,4,10],[-2,-9,-3,1,3,10],[-3,-6,1,5,-3,-5],[10,-5,5,-10,10,2],[-8,-9,-7,3,-2,-3]],[[10,-6,-10,-5,-10,7],[-8,4,6,-3,-9,5],[1,-7,8,-7,-8,1],[-6,10,-9,-3,4,4],[3,6,10,-9,-1,6],[-6,10,-8,2,9,9],[-9,-4,-10,-2,-6,7],[2,-8,2,-4,7,-10],[7,6,-4,-4,7,-3]]], dtype = "int8")#candidate|1265|(4, 9, 6)|const|int8
var_1266 = relay.var("var_1266", dtype = "int8", shape = (4, 9, 6))#candidate|1266|(4, 9, 6)|var|int8
bop_1267 = relay.logical_xor(const_1265.astype('int8'), relay.reshape(var_1266.astype('int8'), relay.shape_of(const_1265))) # shape=(4, 9, 6)
bop_1271 = relay.less_equal(const_1265.astype('bool'), relay.reshape(var_1266.astype('bool'), relay.shape_of(const_1265))) # shape=(4, 9, 6)
uop_1278 = relay.sqrt(var_1266.astype('float64')) # shape=(4, 9, 6)
output = relay.Tuple([bop_1267,bop_1271,uop_1278,])
output2 = relay.Tuple([bop_1267,bop_1271,uop_1278,])
func_1286 = relay.Function([var_1266,], output)
mod['func_1286'] = func_1286
mod = relay.transform.InferType()(mod)
mutated_mod['func_1286'] = func_1286
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1287 = relay.var("var_1287", dtype = "int8", shape = (4, 9, 6))#candidate|1287|(4, 9, 6)|var|int8
func_1286_call = mutated_mod.get_global_var('func_1286')
call_1288 = func_1286_call(var_1287)
output = call_1288
func_1289 = relay.Function([var_1287], output)
mutated_mod['func_1289'] = func_1289
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1487 = relay.var("var_1487", dtype = "int64", shape = (7, 3, 14))#candidate|1487|(7, 3, 14)|var|int64
var_1488 = relay.var("var_1488", dtype = "int64", shape = (7, 3, 14))#candidate|1488|(7, 3, 14)|var|int64
bop_1489 = relay.not_equal(var_1487.astype('bool'), relay.reshape(var_1488.astype('bool'), relay.shape_of(var_1487))) # shape=(7, 3, 14)
bop_1495 = relay.bitwise_or(var_1487.astype('int32'), relay.reshape(bop_1489.astype('int32'), relay.shape_of(var_1487))) # shape=(7, 3, 14)
bop_1506 = relay.logical_xor(var_1488.astype('uint16'), relay.reshape(var_1487.astype('uint16'), relay.shape_of(var_1488))) # shape=(7, 3, 14)
bop_1509 = relay.power(bop_1506.astype('float32'), relay.reshape(bop_1489.astype('float32'), relay.shape_of(bop_1506))) # shape=(7, 3, 14)
uop_1512 = relay.cosh(var_1488.astype('float32')) # shape=(7, 3, 14)
uop_1519 = relay.asin(uop_1512.astype('float32')) # shape=(7, 3, 14)
var_1530 = relay.var("var_1530", dtype = "float32", shape = (7, 3, 14))#candidate|1530|(7, 3, 14)|var|float32
bop_1531 = relay.greater(uop_1512.astype('bool'), relay.reshape(var_1530.astype('bool'), relay.shape_of(uop_1512))) # shape=(7, 3, 14)
output = relay.Tuple([bop_1495,bop_1509,uop_1519,bop_1531,])
output2 = relay.Tuple([bop_1495,bop_1509,uop_1519,bop_1531,])
func_1534 = relay.Function([var_1487,var_1488,var_1530,], output)
mod['func_1534'] = func_1534
mod = relay.transform.InferType()(mod)
mutated_mod['func_1534'] = func_1534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1534_call = mutated_mod.get_global_var('func_1534')
var_1536 = relay.var("var_1536", dtype = "int64", shape = (7, 3, 14))#candidate|1536|(7, 3, 14)|var|int64
var_1537 = relay.var("var_1537", dtype = "int64", shape = (7, 3, 14))#candidate|1537|(7, 3, 14)|var|int64
var_1538 = relay.var("var_1538", dtype = "float32", shape = (7, 3, 14))#candidate|1538|(7, 3, 14)|var|float32
call_1535 = func_1534_call(var_1536,var_1537,var_1538,)
output = call_1535
func_1539 = relay.Function([var_1536,var_1537,var_1538,], output)
mutated_mod['func_1539'] = func_1539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1573 = relay.var("var_1573", dtype = "float64", shape = (10, 3, 7))#candidate|1573|(10, 3, 7)|var|float64
uop_1574 = relay.atan(var_1573.astype('float64')) # shape=(10, 3, 7)
output = uop_1574
output2 = uop_1574
func_1576 = relay.Function([var_1573,], output)
mod['func_1576'] = func_1576
mod = relay.transform.InferType()(mod)
var_1577 = relay.var("var_1577", dtype = "float64", shape = (10, 3, 7))#candidate|1577|(10, 3, 7)|var|float64
output = func_1576(var_1577)
func_1578 = relay.Function([var_1577], output)
mutated_mod['func_1578'] = func_1578
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1700 = relay.const([[8.479912,6.270198,-1.692100,-0.713147,9.542307,-4.504765,0.407582,-9.801492,-5.976971,-4.432299,0.852703,8.604555,-9.167247,-7.758151,9.342842],[-9.905475,-0.591962,-9.630758,4.927679,1.653006,-0.656718,-5.627170,5.545651,4.626577,-2.002537,5.534244,1.587104,-7.381893,5.457843,-6.003925],[6.435047,8.065975,-8.465326,-1.136433,-4.675450,-9.874052,-5.129331,-0.090201,5.084537,1.005282,5.276892,3.344815,8.481561,8.148514,-5.531139],[5.114026,-7.299571,2.566223,-0.944096,-4.863321,4.711652,6.827732,-8.555544,-4.735357,3.879133,1.294356,-9.578417,-9.008766,-0.938402,-7.853905],[9.321215,-5.649773,-7.529874,-2.402297,-2.434590,-2.961527,1.427501,9.378363,0.453801,7.882317,6.505511,-1.371837,8.477576,1.429210,-3.536258],[-4.716236,2.265707,1.736483,-3.804261,-2.478516,-9.332647,9.059375,3.595914,2.361379,-2.139485,4.357366,3.686851,2.814404,-6.504067,1.181394]], dtype = "float64")#candidate|1700|(6, 15)|const|float64
uop_1701 = relay.log10(const_1700.astype('float64')) # shape=(6, 15)
func_1286_call = mod.get_global_var('func_1286')
func_1289_call = mutated_mod.get_global_var('func_1289')
const_1721 = relay.const([-3,7,1,-8,-7,3,-8,1,-7,6,-6,7,-9,3,7,9,-8,7,-6,4,-1,1,7,3,-8,3,-5,-3,-1,2,-4,-10,-9,4,2,-1,6,-2,-5,-8,3,-6,2,-3,-6,10,7,-4,7,-4,-5,-3,6,-5,2,3,-5,-4,-10,9,-3,8,1,8,10,-8,-4,10,-6,-10,-10,-6,2,3,8,-8,3,2,-7,-5,-10,-4,3,4,-10,-10,7,-5,-7,-9,-10,-7,-2,-10,-7,6,7,-4,5,-2,4,5,-9,8,-9,-10,-5,-6,5,-6,9,2,3,6,5,4,3,1,-10,-9,-10,-1,-7,-4,1,5,-3,5,4,-5,-3,-10,-8,8,2,10,6,6,6,-6,-1,8,9,-1,9,3,7,-6,-6,5,-10,9,6,-1,-7,-1,7,4,5,8,1,5,9,-3,6,3,4,-3,-9,-5,9,-7,-9,2,-6,7,-6,-5,4,9,7,5,6,-6,-4,3,8,2,3,-1,-6,6,3,-4,1,-6,-5,-2,2,-6,-8,10,1,3,-5,10,-5,3,8,-6,1,7,-4,5,-8,4], dtype = "int8")#candidate|1721|(216,)|const|int8
call_1720 = relay.TupleGetItem(func_1286_call(relay.reshape(const_1721.astype('int8'), [4, 9, 6])), 1)
call_1722 = relay.TupleGetItem(func_1289_call(relay.reshape(const_1721.astype('int8'), [4, 9, 6])), 1)
output = relay.Tuple([uop_1701,call_1720,const_1721,])
output2 = relay.Tuple([uop_1701,call_1722,const_1721,])
func_1728 = relay.Function([], output)
mod['func_1728'] = func_1728
mod = relay.transform.InferType()(mod)
mutated_mod['func_1728'] = func_1728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mutated_mod.get_global_var('func_1728')
call_1729 = func_1728_call()
output = call_1729
func_1730 = relay.Function([], output)
mutated_mod['func_1730'] = func_1730
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1779 = relay.var("var_1779", dtype = "int8", shape = (10, 2, 10))#candidate|1779|(10, 2, 10)|var|int8
var_1780 = relay.var("var_1780", dtype = "int8", shape = (10, 2, 10))#candidate|1780|(10, 2, 10)|var|int8
bop_1781 = relay.not_equal(var_1779.astype('bool'), relay.reshape(var_1780.astype('bool'), relay.shape_of(var_1779))) # shape=(10, 2, 10)
output = relay.Tuple([bop_1781,])
output2 = relay.Tuple([bop_1781,])
func_1786 = relay.Function([var_1779,var_1780,], output)
mod['func_1786'] = func_1786
mod = relay.transform.InferType()(mod)
mutated_mod['func_1786'] = func_1786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1786_call = mutated_mod.get_global_var('func_1786')
var_1788 = relay.var("var_1788", dtype = "int8", shape = (10, 2, 10))#candidate|1788|(10, 2, 10)|var|int8
var_1789 = relay.var("var_1789", dtype = "int8", shape = (10, 2, 10))#candidate|1789|(10, 2, 10)|var|int8
call_1787 = func_1786_call(var_1788,var_1789,)
output = call_1787
func_1790 = relay.Function([var_1788,var_1789,], output)
mutated_mod['func_1790'] = func_1790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_1841 = relay.TupleGetItem(func_1728_call(), 1)
call_1842 = relay.TupleGetItem(func_1730_call(), 1)
output = call_1841
output2 = call_1842
func_1845 = relay.Function([], output)
mod['func_1845'] = func_1845
mod = relay.transform.InferType()(mod)
output = func_1845()
func_1846 = relay.Function([], output)
mutated_mod['func_1846'] = func_1846
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1849 = relay.var("var_1849", dtype = "float32", shape = (3, 12, 6))#candidate|1849|(3, 12, 6)|var|float32
uop_1850 = relay.asinh(var_1849.astype('float32')) # shape=(3, 12, 6)
output = uop_1850
output2 = uop_1850
func_1885 = relay.Function([var_1849,], output)
mod['func_1885'] = func_1885
mod = relay.transform.InferType()(mod)
mutated_mod['func_1885'] = func_1885
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1886 = relay.var("var_1886", dtype = "float32", shape = (3, 12, 6))#candidate|1886|(3, 12, 6)|var|float32
func_1885_call = mutated_mod.get_global_var('func_1885')
call_1887 = func_1885_call(var_1886)
output = call_1887
func_1888 = relay.Function([var_1886], output)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_1898 = relay.TupleGetItem(func_1728_call(), 1)
call_1899 = relay.TupleGetItem(func_1730_call(), 1)
output = call_1898
output2 = call_1899
func_1903 = relay.Function([], output)
mod['func_1903'] = func_1903
mod = relay.transform.InferType()(mod)
output = func_1903()
func_1904 = relay.Function([], output)
mutated_mod['func_1904'] = func_1904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_1936 = relay.TupleGetItem(func_1728_call(), 1)
call_1937 = relay.TupleGetItem(func_1730_call(), 1)
func_50_call = mod.get_global_var('func_50')
func_52_call = mutated_mod.get_global_var('func_52')
var_1951 = relay.var("var_1951", dtype = "float64", shape = (130, 1))#candidate|1951|(130, 1)|var|float64
call_1950 = relay.TupleGetItem(func_50_call(relay.reshape(var_1951.astype('float64'), [13, 10, 1])), 0)
call_1952 = relay.TupleGetItem(func_52_call(relay.reshape(var_1951.astype('float64'), [13, 10, 1])), 0)
output = relay.Tuple([call_1936,call_1950,var_1951,])
output2 = relay.Tuple([call_1937,call_1952,var_1951,])
func_1956 = relay.Function([var_1951,], output)
mod['func_1956'] = func_1956
mod = relay.transform.InferType()(mod)
var_1957 = relay.var("var_1957", dtype = "float64", shape = (130, 1))#candidate|1957|(130, 1)|var|float64
output = func_1956(var_1957)
func_1958 = relay.Function([var_1957], output)
mutated_mod['func_1958'] = func_1958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_2023 = func_1903_call()
call_2024 = func_1903_call()
output = relay.Tuple([call_2023,])
output2 = relay.Tuple([call_2024,])
func_2027 = relay.Function([], output)
mod['func_2027'] = func_2027
mod = relay.transform.InferType()(mod)
mutated_mod['func_2027'] = func_2027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2028 = func_2027_call()
output = call_2028
func_2029 = relay.Function([], output)
mutated_mod['func_2029'] = func_2029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_2058 = relay.TupleGetItem(func_1728_call(), 0)
call_2059 = relay.TupleGetItem(func_1730_call(), 0)
func_1534_call = mod.get_global_var('func_1534')
func_1539_call = mutated_mod.get_global_var('func_1539')
var_2063 = relay.var("var_2063", dtype = "int64", shape = (294,))#candidate|2063|(294,)|var|int64
call_2062 = relay.TupleGetItem(func_1534_call(relay.reshape(var_2063.astype('int64'), [7, 3, 14]), relay.reshape(var_2063.astype('int64'), [7, 3, 14]), relay.reshape(var_2063.astype('float32'), [7, 3, 14]), ), 3)
call_2064 = relay.TupleGetItem(func_1539_call(relay.reshape(var_2063.astype('int64'), [7, 3, 14]), relay.reshape(var_2063.astype('int64'), [7, 3, 14]), relay.reshape(var_2063.astype('float32'), [7, 3, 14]), ), 3)
output = relay.Tuple([call_2058,call_2062,var_2063,])
output2 = relay.Tuple([call_2059,call_2064,var_2063,])
func_2071 = relay.Function([var_2063,], output)
mod['func_2071'] = func_2071
mod = relay.transform.InferType()(mod)
mutated_mod['func_2071'] = func_2071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2072 = relay.var("var_2072", dtype = "int64", shape = (294,))#candidate|2072|(294,)|var|int64
func_2071_call = mutated_mod.get_global_var('func_2071')
call_2073 = func_2071_call(var_2072)
output = call_2073
func_2074 = relay.Function([var_2072], output)
mutated_mod['func_2074'] = func_2074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_2157 = relay.TupleGetItem(func_1728_call(), 0)
call_2158 = relay.TupleGetItem(func_1730_call(), 0)
output = call_2157
output2 = call_2158
func_2162 = relay.Function([], output)
mod['func_2162'] = func_2162
mod = relay.transform.InferType()(mod)
output = func_2162()
func_2163 = relay.Function([], output)
mutated_mod['func_2163'] = func_2163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2179 = relay.var("var_2179", dtype = "float32", shape = (5, 10, 13))#candidate|2179|(5, 10, 13)|var|float32
var_2180 = relay.var("var_2180", dtype = "float32", shape = (5, 10, 13))#candidate|2180|(5, 10, 13)|var|float32
bop_2181 = relay.divide(var_2179.astype('float32'), relay.reshape(var_2180.astype('float32'), relay.shape_of(var_2179))) # shape=(5, 10, 13)
uop_2190 = relay.log2(bop_2181.astype('float32')) # shape=(5, 10, 13)
output = uop_2190
output2 = uop_2190
func_2194 = relay.Function([var_2179,var_2180,], output)
mod['func_2194'] = func_2194
mod = relay.transform.InferType()(mod)
mutated_mod['func_2194'] = func_2194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2194_call = mutated_mod.get_global_var('func_2194')
var_2196 = relay.var("var_2196", dtype = "float32", shape = (5, 10, 13))#candidate|2196|(5, 10, 13)|var|float32
var_2197 = relay.var("var_2197", dtype = "float32", shape = (5, 10, 13))#candidate|2197|(5, 10, 13)|var|float32
call_2195 = func_2194_call(var_2196,var_2197,)
output = call_2195
func_2198 = relay.Function([var_2196,var_2197,], output)
mutated_mod['func_2198'] = func_2198
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2233 = relay.var("var_2233", dtype = "float64", shape = (13, 16, 2))#candidate|2233|(13, 16, 2)|var|float64
uop_2234 = relay.sinh(var_2233.astype('float64')) # shape=(13, 16, 2)
func_1286_call = mod.get_global_var('func_1286')
func_1289_call = mutated_mod.get_global_var('func_1289')
var_2241 = relay.var("var_2241", dtype = "int8", shape = (36, 6))#candidate|2241|(36, 6)|var|int8
call_2240 = relay.TupleGetItem(func_1286_call(relay.reshape(var_2241.astype('int8'), [4, 9, 6])), 1)
call_2242 = relay.TupleGetItem(func_1289_call(relay.reshape(var_2241.astype('int8'), [4, 9, 6])), 1)
output = relay.Tuple([uop_2234,call_2240,var_2241,])
output2 = relay.Tuple([uop_2234,call_2242,var_2241,])
func_2245 = relay.Function([var_2233,var_2241,], output)
mod['func_2245'] = func_2245
mod = relay.transform.InferType()(mod)
var_2246 = relay.var("var_2246", dtype = "float64", shape = (13, 16, 2))#candidate|2246|(13, 16, 2)|var|float64
var_2247 = relay.var("var_2247", dtype = "int8", shape = (36, 6))#candidate|2247|(36, 6)|var|int8
output = func_2245(var_2246,var_2247,)
func_2248 = relay.Function([var_2246,var_2247,], output)
mutated_mod['func_2248'] = func_2248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_2293 = relay.TupleGetItem(func_2027_call(), 0)
call_2294 = relay.TupleGetItem(func_2029_call(), 0)
func_1534_call = mod.get_global_var('func_1534')
func_1539_call = mutated_mod.get_global_var('func_1539')
var_2315 = relay.var("var_2315", dtype = "int64", shape = (294,))#candidate|2315|(294,)|var|int64
call_2314 = relay.TupleGetItem(func_1534_call(relay.reshape(var_2315.astype('int64'), [7, 3, 14]), relay.reshape(var_2315.astype('int64'), [7, 3, 14]), relay.reshape(var_2315.astype('float32'), [7, 3, 14]), ), 0)
call_2316 = relay.TupleGetItem(func_1539_call(relay.reshape(var_2315.astype('int64'), [7, 3, 14]), relay.reshape(var_2315.astype('int64'), [7, 3, 14]), relay.reshape(var_2315.astype('float32'), [7, 3, 14]), ), 0)
func_1956_call = mod.get_global_var('func_1956')
func_1958_call = mutated_mod.get_global_var('func_1958')
var_2322 = relay.var("var_2322", dtype = "float64", shape = (130,))#candidate|2322|(130,)|var|float64
call_2321 = relay.TupleGetItem(func_1956_call(relay.reshape(var_2322.astype('float64'), [130, 1])), 2)
call_2323 = relay.TupleGetItem(func_1958_call(relay.reshape(var_2322.astype('float64'), [130, 1])), 2)
uop_2333 = relay.exp(var_2315.astype('float32')) # shape=(294,)
output = relay.Tuple([call_2293,call_2314,call_2321,var_2322,uop_2333,])
output2 = relay.Tuple([call_2294,call_2316,call_2323,var_2322,uop_2333,])
func_2338 = relay.Function([var_2315,var_2322,], output)
mod['func_2338'] = func_2338
mod = relay.transform.InferType()(mod)
mutated_mod['func_2338'] = func_2338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2338_call = mutated_mod.get_global_var('func_2338')
var_2340 = relay.var("var_2340", dtype = "int64", shape = (294,))#candidate|2340|(294,)|var|int64
var_2341 = relay.var("var_2341", dtype = "float64", shape = (130,))#candidate|2341|(130,)|var|float64
call_2339 = func_2338_call(var_2340,var_2341,)
output = call_2339
func_2342 = relay.Function([var_2340,var_2341,], output)
mutated_mod['func_2342'] = func_2342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_2375 = func_1903_call()
call_2376 = func_1903_call()
func_1885_call = mod.get_global_var('func_1885')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_2390 = func_1885_call(relay.reshape(call_2375.astype('float32'), [3, 12, 6]))
call_2391 = func_1885_call(relay.reshape(call_2375.astype('float32'), [3, 12, 6]))
func_1956_call = mod.get_global_var('func_1956')
func_1958_call = mutated_mod.get_global_var('func_1958')
var_2398 = relay.var("var_2398", dtype = "float64", shape = (1, 130))#candidate|2398|(1, 130)|var|float64
call_2397 = relay.TupleGetItem(func_1956_call(relay.reshape(var_2398.astype('float64'), [130, 1])), 1)
call_2399 = relay.TupleGetItem(func_1958_call(relay.reshape(var_2398.astype('float64'), [130, 1])), 1)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2401 = func_2162_call()
call_2402 = func_2162_call()
output = relay.Tuple([call_2375,call_2390,call_2397,var_2398,call_2401,])
output2 = relay.Tuple([call_2376,call_2391,call_2399,var_2398,call_2402,])
func_2403 = relay.Function([var_2398,], output)
mod['func_2403'] = func_2403
mod = relay.transform.InferType()(mod)
var_2404 = relay.var("var_2404", dtype = "float64", shape = (1, 130))#candidate|2404|(1, 130)|var|float64
output = func_2403(var_2404)
func_2405 = relay.Function([var_2404], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2412 = relay.var("var_2412", dtype = "float32", shape = (6, 16, 1))#candidate|2412|(6, 16, 1)|var|float32
uop_2413 = relay.acos(var_2412.astype('float32')) # shape=(6, 16, 1)
var_2416 = relay.var("var_2416", dtype = "float32", shape = (6, 16, 15))#candidate|2416|(6, 16, 15)|var|float32
bop_2417 = relay.floor_mod(var_2412.astype('float64'), var_2416.astype('float64')) # shape=(6, 16, 15)
var_2424 = relay.var("var_2424", dtype = "float64", shape = (6, 16, 15))#candidate|2424|(6, 16, 15)|var|float64
bop_2425 = relay.mod(bop_2417.astype('float32'), relay.reshape(var_2424.astype('float32'), relay.shape_of(bop_2417))) # shape=(6, 16, 15)
uop_2436 = relay.rsqrt(uop_2413.astype('float32')) # shape=(6, 16, 1)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_2438 = relay.TupleGetItem(func_1728_call(), 2)
call_2439 = relay.TupleGetItem(func_1730_call(), 2)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
const_2444 = relay.const([[-5.507783,-2.329999,3.846559,8.282607,-6.597620,-5.607117,-7.424739,-6.201068,6.955898,4.389780,0.390471,7.445816,4.659255,-1.834144,6.279411,2.123187,0.737015,-8.931579,-8.788890,8.977119,8.506666,-8.088338,7.966578,0.213578,9.426723,-7.073052,3.906780,0.252230,-7.371889,-2.095785,8.987564,0.987009,8.025514,-4.264471,5.770564,-9.408434,7.831312,-8.283350,2.897417,-0.891930,-9.077817,-4.388773,-3.640962,-1.152067,0.114971,8.342943,7.646304,-0.319959,-0.942110,-2.569987,-9.021160,1.668675,2.222699,-2.625143,2.006369,-5.465766,0.574880,3.797640,-9.283063,-6.492651,5.518312,3.163423,-5.351981,5.883633,-5.397262,-6.184190,3.272435,-1.161676,8.376031,5.623722]], dtype = "float64")#candidate|2444|(1, 70)|const|float64
call_2443 = relay.TupleGetItem(func_235_call(relay.reshape(const_2444.astype('float64'), [1, 10, 7])), 1)
call_2445 = relay.TupleGetItem(func_237_call(relay.reshape(const_2444.astype('float64'), [1, 10, 7])), 1)
bop_2451 = relay.less_equal(uop_2413.astype('bool'), bop_2425.astype('bool')) # shape=(6, 16, 15)
func_2245_call = mod.get_global_var('func_2245')
func_2248_call = mutated_mod.get_global_var('func_2248')
const_2463 = relay.const([[6.596645],[-6.124965],[-6.878053],[-0.839821],[-2.273384],[-1.253285],[1.993530],[-2.468887],[-1.239248],[-2.863332],[-7.099283],[0.575183],[-0.074557],[-3.242450],[3.917665],[7.065883],[2.687701],[5.137896],[5.551832],[9.588666],[-8.885693],[9.072279],[-1.497960],[-7.214023],[1.613271],[2.459391],[3.319403],[-2.541971],[-0.445959],[2.597223],[-6.587240],[-2.433441],[-9.070918],[0.781487],[6.593923],[7.954853],[4.064623],[-6.750687],[-7.812834],[-5.291679],[6.502947],[5.786658],[-1.575716],[-4.576950],[6.612354],[-3.062616],[-7.930203],[5.869973],[-0.542883],[-5.717429],[0.028137],[6.584571],[-7.973046],[2.853880],[-9.239386],[-2.046142],[7.477490],[1.005151],[-0.452100],[-3.381920],[8.810333],[7.087902],[-3.601062],[-3.485271],[-0.375527],[-0.885053],[4.264685],[-7.424229],[3.445843],[-8.970194],[8.598512],[2.843672],[3.629545],[-3.041612],[-0.604423],[2.876344],[2.374838],[0.636380],[8.521084],[-5.325745],[-9.855009],[-4.479659],[-9.004494],[5.776082],[-2.296713],[5.189950],[2.303483],[-9.671720],[4.030353],[-8.127019],[-8.234164],[6.703528],[-5.036546],[5.169875],[9.782075],[0.233251],[-4.891278],[1.898382],[-9.436248],[1.689367],[-7.429266],[-8.723533],[9.830186],[-5.004951],[7.055388],[6.933099],[-8.527019],[7.509061],[9.976310],[2.743369],[-6.415420],[5.376687],[-3.812329],[0.998115],[4.416836],[5.913128],[-3.486916],[7.084399],[-4.332994],[-6.387488],[-1.765822],[1.592134],[9.674942],[-1.060780],[8.332951],[7.201799],[-4.007768],[1.308675],[2.538409],[-2.220999],[8.329290],[-7.137103],[7.964115],[4.833852],[-9.458780],[-5.878643],[6.396246],[2.330536],[-8.602353],[-1.587389],[2.967799],[-0.580145],[-1.809284],[-1.277063],[-7.865725],[-6.501366],[-6.693977],[7.441883],[6.431175],[-2.581919],[7.444955],[-1.096128],[-4.249392],[7.692042],[3.614081],[7.862669],[9.084267],[8.984494],[2.085467],[5.948553],[-9.020956],[0.767171],[-4.322516],[-6.608258],[3.366518],[6.887608],[3.313079],[-5.005734],[-1.077977],[3.359744],[0.860415],[-8.122903],[-6.809864],[-9.262827],[-0.985579],[6.082349],[7.521009],[9.630978],[-2.588111],[6.869019],[-7.351782],[-2.197722],[1.098253],[-9.070034],[-5.701547],[3.961002],[-1.934426],[-4.715540],[8.622406],[-8.682313],[-3.769480],[-8.818192],[-5.033928],[2.863624],[-5.596348],[-1.362064],[-3.399862],[-3.273389],[1.977832],[6.288799],[-5.263787],[6.618502],[-0.395644],[7.765089],[-1.471166],[6.132605],[-4.710662],[3.191628],[-3.916880],[0.493654],[9.143489],[4.342337],[-4.689578],[3.283983],[-1.148605],[7.201148],[-3.180627],[6.272641],[-7.246874],[-5.034332],[-8.912684],[1.596656],[-4.686433],[0.950713],[0.373283],[4.499848],[2.316801],[-3.823416],[-5.932277],[8.107651],[-7.235437],[-3.343196],[-9.158920],[-4.730975],[-2.643096],[0.170364],[-5.492039],[2.135679],[7.262688],[2.249704],[2.470348],[-6.559245],[-3.209507],[-8.571286],[-4.506853],[6.183452],[-3.518667],[4.109774],[-9.693621],[0.958720],[6.110504],[3.057893],[6.603950],[-2.656202],[-9.732725],[-9.217750],[-9.494854],[-6.848030],[0.336967],[6.769771],[-9.383015],[6.080375],[-2.752691],[7.390614],[-5.823175],[-6.609115],[-4.272367],[6.905197],[-8.235767],[-9.015389],[-3.022052],[5.922601],[2.499705],[7.862665],[-4.857078],[3.962541],[7.785100],[-1.304484],[3.990885],[-0.913595],[-0.418099],[5.068066],[7.382668],[8.281172],[-4.892394],[-0.678580],[-9.065041],[9.552073],[1.925567],[-9.732448],[-0.611809],[-3.584278],[-8.359071],[8.679832],[0.369244],[0.704949],[-1.342701],[-2.603447],[-9.011367],[-7.229986],[5.434240],[0.857353],[-4.395939],[-5.112131],[7.526593],[8.399099],[-1.910488],[4.001006],[-7.527658],[-5.202979],[2.970196],[-3.148647],[4.783041],[5.500867],[-5.024080],[-4.998916],[-8.970532],[8.770286],[4.124424],[-9.452218],[-0.720879],[-4.760305],[4.295094],[-2.535180],[-9.536725],[6.850619],[-3.144097],[-5.552756],[-0.072559],[3.845669],[1.030281],[5.120608],[3.096103],[-7.781440],[-1.812569],[3.303484],[-1.386089],[1.060979],[-4.252474],[-9.283255],[-1.948632],[-4.382770],[1.155791],[-7.730302],[-6.189796],[-9.663102],[-1.702367],[2.972167],[-6.281400],[-7.075010],[-2.902263],[9.322371],[5.524466],[-4.323209],[-2.915882],[-9.596158],[4.643416],[-7.879491],[8.311741],[-4.633420],[-3.775847],[5.818622],[-3.702138],[2.935251],[-6.390361],[0.327394],[1.745282],[-9.816194],[6.224821],[-6.415389],[6.820707],[7.380874],[3.449216],[8.148480],[-8.172869],[-4.178456],[-8.044213],[2.189709],[-6.155375],[8.885042],[-5.710827],[5.938401],[3.997865],[-1.373468],[1.938410],[9.737596],[-3.434655],[1.147572],[-6.300654],[-2.045232],[-4.877659],[3.150756],[0.496337],[-9.280310],[7.433859],[-2.766914],[-7.942238],[-8.789609],[4.955055],[1.755096],[3.815606],[2.734639],[6.900592],[-9.050487],[2.469615],[-7.875848],[1.211204],[-7.496125],[2.025278],[7.371457],[-4.984670],[-6.029008],[1.184595],[6.010714],[-8.015402],[0.491214]], dtype = "float64")#candidate|2463|(416, 1)|const|float64
call_2462 = relay.TupleGetItem(func_2245_call(relay.reshape(const_2463.astype('float64'), [13, 16, 2]), relay.reshape(call_2438.astype('int8'), [36, 6]), ), 0)
call_2464 = relay.TupleGetItem(func_2248_call(relay.reshape(const_2463.astype('float64'), [13, 16, 2]), relay.reshape(call_2438.astype('int8'), [36, 6]), ), 0)
func_1534_call = mod.get_global_var('func_1534')
func_1539_call = mutated_mod.get_global_var('func_1539')
var_2486 = relay.var("var_2486", dtype = "int64", shape = (294,))#candidate|2486|(294,)|var|int64
call_2485 = relay.TupleGetItem(func_1534_call(relay.reshape(var_2486.astype('int64'), [7, 3, 14]), relay.reshape(var_2486.astype('int64'), [7, 3, 14]), relay.reshape(var_2486.astype('float32'), [7, 3, 14]), ), 1)
call_2487 = relay.TupleGetItem(func_1539_call(relay.reshape(var_2486.astype('int64'), [7, 3, 14]), relay.reshape(var_2486.astype('int64'), [7, 3, 14]), relay.reshape(var_2486.astype('float32'), [7, 3, 14]), ), 1)
output = relay.Tuple([uop_2436,call_2438,call_2443,const_2444,bop_2451,call_2462,const_2463,call_2485,var_2486,])
output2 = relay.Tuple([uop_2436,call_2439,call_2445,const_2444,bop_2451,call_2464,const_2463,call_2487,var_2486,])
func_2491 = relay.Function([var_2412,var_2416,var_2424,var_2486,], output)
mod['func_2491'] = func_2491
mod = relay.transform.InferType()(mod)
var_2492 = relay.var("var_2492", dtype = "float32", shape = (6, 16, 1))#candidate|2492|(6, 16, 1)|var|float32
var_2493 = relay.var("var_2493", dtype = "float32", shape = (6, 16, 15))#candidate|2493|(6, 16, 15)|var|float32
var_2494 = relay.var("var_2494", dtype = "float64", shape = (6, 16, 15))#candidate|2494|(6, 16, 15)|var|float64
var_2495 = relay.var("var_2495", dtype = "int64", shape = (294,))#candidate|2495|(294,)|var|int64
output = func_2491(var_2492,var_2493,var_2494,var_2495,)
func_2496 = relay.Function([var_2492,var_2493,var_2494,var_2495,], output)
mutated_mod['func_2496'] = func_2496
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2517 = relay.var("var_2517", dtype = "float64", shape = (8, 4, 1))#candidate|2517|(8, 4, 1)|var|float64
uop_2518 = relay.cosh(var_2517.astype('float64')) # shape=(8, 4, 1)
output = uop_2518
output2 = uop_2518
func_2523 = relay.Function([var_2517,], output)
mod['func_2523'] = func_2523
mod = relay.transform.InferType()(mod)
mutated_mod['func_2523'] = func_2523
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2524 = relay.var("var_2524", dtype = "float64", shape = (8, 4, 1))#candidate|2524|(8, 4, 1)|var|float64
func_2523_call = mutated_mod.get_global_var('func_2523')
call_2525 = func_2523_call(var_2524)
output = call_2525
func_2526 = relay.Function([var_2524], output)
mutated_mod['func_2526'] = func_2526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2531 = func_2162_call()
call_2532 = func_2162_call()
output = relay.Tuple([call_2531,])
output2 = relay.Tuple([call_2532,])
func_2536 = relay.Function([], output)
mod['func_2536'] = func_2536
mod = relay.transform.InferType()(mod)
output = func_2536()
func_2537 = relay.Function([], output)
mutated_mod['func_2537'] = func_2537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_2565 = relay.TupleGetItem(func_1728_call(), 2)
call_2566 = relay.TupleGetItem(func_1730_call(), 2)
output = relay.Tuple([call_2565,])
output2 = relay.Tuple([call_2566,])
func_2570 = relay.Function([], output)
mod['func_2570'] = func_2570
mod = relay.transform.InferType()(mod)
output = func_2570()
func_2571 = relay.Function([], output)
mutated_mod['func_2571'] = func_2571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2583 = func_2162_call()
call_2584 = func_2162_call()
output = call_2583
output2 = call_2584
func_2595 = relay.Function([], output)
mod['func_2595'] = func_2595
mod = relay.transform.InferType()(mod)
output = func_2595()
func_2596 = relay.Function([], output)
mutated_mod['func_2596'] = func_2596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_2600 = relay.TupleGetItem(func_1728_call(), 1)
call_2601 = relay.TupleGetItem(func_1730_call(), 1)
output = call_2600
output2 = call_2601
func_2620 = relay.Function([], output)
mod['func_2620'] = func_2620
mod = relay.transform.InferType()(mod)
mutated_mod['func_2620'] = func_2620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2620_call = mutated_mod.get_global_var('func_2620')
call_2621 = func_2620_call()
output = call_2621
func_2622 = relay.Function([], output)
mutated_mod['func_2622'] = func_2622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2628 = func_2162_call()
call_2629 = func_2162_call()
output = call_2628
output2 = call_2629
func_2646 = relay.Function([], output)
mod['func_2646'] = func_2646
mod = relay.transform.InferType()(mod)
output = func_2646()
func_2647 = relay.Function([], output)
mutated_mod['func_2647'] = func_2647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2646_call = mod.get_global_var('func_2646')
func_2647_call = mutated_mod.get_global_var('func_2647')
call_2686 = func_2646_call()
call_2687 = func_2646_call()
output = relay.Tuple([call_2686,])
output2 = relay.Tuple([call_2687,])
func_2707 = relay.Function([], output)
mod['func_2707'] = func_2707
mod = relay.transform.InferType()(mod)
output = func_2707()
func_2708 = relay.Function([], output)
mutated_mod['func_2708'] = func_2708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2753 = func_2162_call()
call_2754 = func_2162_call()
func_2620_call = mod.get_global_var('func_2620')
func_2622_call = mutated_mod.get_global_var('func_2622')
call_2767 = func_2620_call()
call_2768 = func_2620_call()
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_2769 = relay.TupleGetItem(func_2027_call(), 0)
call_2770 = relay.TupleGetItem(func_2029_call(), 0)
output = relay.Tuple([call_2753,call_2767,call_2769,])
output2 = relay.Tuple([call_2754,call_2768,call_2770,])
func_2784 = relay.Function([], output)
mod['func_2784'] = func_2784
mod = relay.transform.InferType()(mod)
mutated_mod['func_2784'] = func_2784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2784_call = mutated_mod.get_global_var('func_2784')
call_2785 = func_2784_call()
output = call_2785
func_2786 = relay.Function([], output)
mutated_mod['func_2786'] = func_2786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2620_call = mod.get_global_var('func_2620')
func_2622_call = mutated_mod.get_global_var('func_2622')
call_2836 = func_2620_call()
call_2837 = func_2620_call()
output = relay.Tuple([call_2836,])
output2 = relay.Tuple([call_2837,])
func_2840 = relay.Function([], output)
mod['func_2840'] = func_2840
mod = relay.transform.InferType()(mod)
mutated_mod['func_2840'] = func_2840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2840_call = mutated_mod.get_global_var('func_2840')
call_2841 = func_2840_call()
output = call_2841
func_2842 = relay.Function([], output)
mutated_mod['func_2842'] = func_2842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2876 = func_2162_call()
call_2877 = func_2162_call()
output = relay.Tuple([call_2876,])
output2 = relay.Tuple([call_2877,])
func_2884 = relay.Function([], output)
mod['func_2884'] = func_2884
mod = relay.transform.InferType()(mod)
mutated_mod['func_2884'] = func_2884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2884_call = mutated_mod.get_global_var('func_2884')
call_2885 = func_2884_call()
output = call_2885
func_2886 = relay.Function([], output)
mutated_mod['func_2886'] = func_2886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2909 = relay.var("var_2909", dtype = "int16", shape = (16, 7, 1))#candidate|2909|(16, 7, 1)|var|int16
var_2910 = relay.var("var_2910", dtype = "int16", shape = (16, 7, 7))#candidate|2910|(16, 7, 7)|var|int16
bop_2911 = relay.less(var_2909.astype('bool'), var_2910.astype('bool')) # shape=(16, 7, 7)
output = bop_2911
output2 = bop_2911
func_2921 = relay.Function([var_2909,var_2910,], output)
mod['func_2921'] = func_2921
mod = relay.transform.InferType()(mod)
mutated_mod['func_2921'] = func_2921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mutated_mod.get_global_var('func_2921')
var_2923 = relay.var("var_2923", dtype = "int16", shape = (16, 7, 1))#candidate|2923|(16, 7, 1)|var|int16
var_2924 = relay.var("var_2924", dtype = "int16", shape = (16, 7, 7))#candidate|2924|(16, 7, 7)|var|int16
call_2922 = func_2921_call(var_2923,var_2924,)
output = call_2922
func_2925 = relay.Function([var_2923,var_2924,], output)
mutated_mod['func_2925'] = func_2925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2646_call = mod.get_global_var('func_2646')
func_2647_call = mutated_mod.get_global_var('func_2647')
call_2966 = func_2646_call()
call_2967 = func_2646_call()
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_2973 = relay.TupleGetItem(func_2570_call(), 0)
call_2974 = relay.TupleGetItem(func_2571_call(), 0)
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_2978 = func_1903_call()
call_2979 = func_1903_call()
output = relay.Tuple([call_2966,call_2973,call_2978,])
output2 = relay.Tuple([call_2967,call_2974,call_2979,])
func_2987 = relay.Function([], output)
mod['func_2987'] = func_2987
mod = relay.transform.InferType()(mod)
mutated_mod['func_2987'] = func_2987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2987_call = mutated_mod.get_global_var('func_2987')
call_2988 = func_2987_call()
output = call_2988
func_2989 = relay.Function([], output)
mutated_mod['func_2989'] = func_2989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2997 = func_2162_call()
call_2998 = func_2162_call()
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_3006 = relay.TupleGetItem(func_2027_call(), 0)
call_3007 = relay.TupleGetItem(func_2029_call(), 0)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3017 = relay.TupleGetItem(func_2536_call(), 0)
call_3018 = relay.TupleGetItem(func_2537_call(), 0)
output = relay.Tuple([call_2997,call_3006,call_3017,])
output2 = relay.Tuple([call_2998,call_3007,call_3018,])
func_3026 = relay.Function([], output)
mod['func_3026'] = func_3026
mod = relay.transform.InferType()(mod)
mutated_mod['func_3026'] = func_3026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3026_call = mutated_mod.get_global_var('func_3026')
call_3027 = func_3026_call()
output = call_3027
func_3028 = relay.Function([], output)
mutated_mod['func_3028'] = func_3028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3041 = relay.TupleGetItem(func_2536_call(), 0)
call_3042 = relay.TupleGetItem(func_2537_call(), 0)
output = call_3041
output2 = call_3042
func_3046 = relay.Function([], output)
mod['func_3046'] = func_3046
mod = relay.transform.InferType()(mod)
output = func_3046()
func_3047 = relay.Function([], output)
mutated_mod['func_3047'] = func_3047
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3064 = relay.var("var_3064", dtype = "float64", shape = (1, 16, 10))#candidate|3064|(1, 16, 10)|var|float64
uop_3065 = relay.log10(var_3064.astype('float64')) # shape=(1, 16, 10)
bop_3072 = relay.right_shift(uop_3065.astype('uint16'), relay.reshape(var_3064.astype('uint16'), relay.shape_of(uop_3065))) # shape=(1, 16, 10)
output = bop_3072
output2 = bop_3072
func_3075 = relay.Function([var_3064,], output)
mod['func_3075'] = func_3075
mod = relay.transform.InferType()(mod)
var_3076 = relay.var("var_3076", dtype = "float64", shape = (1, 16, 10))#candidate|3076|(1, 16, 10)|var|float64
output = func_3075(var_3076)
func_3077 = relay.Function([var_3076], output)
mutated_mod['func_3077'] = func_3077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3084 = relay.TupleGetItem(func_2536_call(), 0)
call_3085 = relay.TupleGetItem(func_2537_call(), 0)
output = relay.Tuple([call_3084,])
output2 = relay.Tuple([call_3085,])
func_3102 = relay.Function([], output)
mod['func_3102'] = func_3102
mod = relay.transform.InferType()(mod)
mutated_mod['func_3102'] = func_3102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3102_call = mutated_mod.get_global_var('func_3102')
call_3103 = func_3102_call()
output = call_3103
func_3104 = relay.Function([], output)
mutated_mod['func_3104'] = func_3104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2707_call = mod.get_global_var('func_2707')
func_2708_call = mutated_mod.get_global_var('func_2708')
call_3105 = relay.TupleGetItem(func_2707_call(), 0)
call_3106 = relay.TupleGetItem(func_2708_call(), 0)
func_2987_call = mod.get_global_var('func_2987')
func_2989_call = mutated_mod.get_global_var('func_2989')
call_3111 = relay.TupleGetItem(func_2987_call(), 1)
call_3112 = relay.TupleGetItem(func_2989_call(), 1)
var_3139 = relay.var("var_3139", dtype = "int8", shape = (216,))#candidate|3139|(216,)|var|int8
bop_3140 = relay.subtract(call_3111.astype('uint32'), relay.reshape(var_3139.astype('uint32'), relay.shape_of(call_3111))) # shape=(216,)
bop_3143 = relay.subtract(call_3112.astype('uint32'), relay.reshape(var_3139.astype('uint32'), relay.shape_of(call_3112))) # shape=(216,)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_3162 = relay.TupleGetItem(func_3026_call(), 2)
call_3163 = relay.TupleGetItem(func_3028_call(), 2)
func_1786_call = mod.get_global_var('func_1786')
func_1790_call = mutated_mod.get_global_var('func_1790')
var_3178 = relay.var("var_3178", dtype = "int8", shape = (1, 200))#candidate|3178|(1, 200)|var|int8
call_3177 = relay.TupleGetItem(func_1786_call(relay.reshape(var_3178.astype('int8'), [10, 2, 10]), relay.reshape(var_3178.astype('int8'), [10, 2, 10]), ), 0)
call_3179 = relay.TupleGetItem(func_1790_call(relay.reshape(var_3178.astype('int8'), [10, 2, 10]), relay.reshape(var_3178.astype('int8'), [10, 2, 10]), ), 0)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
var_3185 = relay.var("var_3185", dtype = "float64", shape = (26, 5))#candidate|3185|(26, 5)|var|float64
call_3184 = relay.TupleGetItem(func_2403_call(relay.reshape(var_3185.astype('float64'), [1, 130])), 3)
call_3186 = relay.TupleGetItem(func_2405_call(relay.reshape(var_3185.astype('float64'), [1, 130])), 3)
func_2840_call = mod.get_global_var('func_2840')
func_2842_call = mutated_mod.get_global_var('func_2842')
call_3221 = relay.TupleGetItem(func_2840_call(), 0)
call_3222 = relay.TupleGetItem(func_2842_call(), 0)
func_2840_call = mod.get_global_var('func_2840')
func_2842_call = mutated_mod.get_global_var('func_2842')
call_3237 = relay.TupleGetItem(func_2840_call(), 0)
call_3238 = relay.TupleGetItem(func_2842_call(), 0)
output = relay.Tuple([call_3105,bop_3140,call_3162,call_3177,var_3178,call_3184,var_3185,call_3221,call_3237,])
output2 = relay.Tuple([call_3106,bop_3143,call_3163,call_3179,var_3178,call_3186,var_3185,call_3222,call_3238,])
func_3246 = relay.Function([var_3139,var_3178,var_3185,], output)
mod['func_3246'] = func_3246
mod = relay.transform.InferType()(mod)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3246_call = mutated_mod.get_global_var('func_3246')
var_3248 = relay.var("var_3248", dtype = "int8", shape = (216,))#candidate|3248|(216,)|var|int8
var_3249 = relay.var("var_3249", dtype = "int8", shape = (1, 200))#candidate|3249|(1, 200)|var|int8
var_3250 = relay.var("var_3250", dtype = "float64", shape = (26, 5))#candidate|3250|(26, 5)|var|float64
call_3247 = func_3246_call(var_3248,var_3249,var_3250,)
output = call_3247
func_3251 = relay.Function([var_3248,var_3249,var_3250,], output)
mutated_mod['func_3251'] = func_3251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3256 = relay.TupleGetItem(func_2536_call(), 0)
call_3257 = relay.TupleGetItem(func_2537_call(), 0)
func_2840_call = mod.get_global_var('func_2840')
func_2842_call = mutated_mod.get_global_var('func_2842')
call_3262 = relay.TupleGetItem(func_2840_call(), 0)
call_3263 = relay.TupleGetItem(func_2842_call(), 0)
func_2921_call = mod.get_global_var('func_2921')
func_2925_call = mutated_mod.get_global_var('func_2925')
var_3290 = relay.var("var_3290", dtype = "int16", shape = (112,))#candidate|3290|(112,)|var|int16
const_3291 = relay.const([-8,3,-6,-3,-7,9,-5,-7,-8,-8,2,7,-2,7,3,-1,2,3,5,1,10,9,-4,2,-7,-6,-10,7,5,7,9,-1,4,-1,9,2,-1,-7,-7,-4,3,-5,2,4,-3,7,9,-7,3,-1,-9,4,-3,-2,1,-7,7,-7,4,-8,2,-3,3,-5,7,1,-10,5,-7,6,-4,-2,6,1,3,-1,5,8,-3,6,-1,-7,1,4,8,6,4,-4,-9,2,-4,-7,-6,-7,-9,2,-10,-1,-8,7,-7,-7,-10,3,6,1,10,-9,4,7,10,3,8,-1,9,2,2,8,2,3,-9,-10,-2,-5,-4,10,-4,4,-5,8,-4,1,-4,9,-4,-6,5,-2,-4,5,-3,-3,-8,-9,-1,-10,-9,-2,1,9,-4,-8,10,7,-9,3,9,-9,3,1,-4,1,-1,-4,-4,8,7,-6,8,-2,-8,-10,-1,6,-6,-7,10,-4,3,-5,-1,5,-3,-9,-8,9,-8,-5,-8,2,-1,-6,9,4,-8,-8,-4,-8,-8,9,10,2,-6,6,9,2,6,-1,-8,4,-3,-6,9,-5,3,-1,-9,8,1,3,-1,-7,3,-2,2,6,10,2,5,6,-1,-8,1,8,-3,1,-6,-1,-8,-9,-10,-6,4,-2,5,-5,-7,9,-3,2,-9,-10,-3,3,3,-4,4,3,-7,-7,3,1,8,-9,-6,-9,-4,-8,-9,10,5,-6,1,-9,6,-3,9,-10,3,-2,-8,1,-9,1,-2,-9,-5,5,6,-6,-1,1,4,-9,-1,-3,-1,5,3,-7,6,-3,-2,-7,-2,9,4,3,3,3,4,-7,10,4,-5,-2,8,-2,-2,9,1,-9,-1,-3,8,-10,-1,9,6,-9,-6,-2,4,5,2,-4,-3,10,-7,8,-8,-8,-5,4,-10,-2,2,9,7,-4,9,4,10,5,6,3,-4,-4,-7,8,-1,-4,-4,3,-8,-2,6,10,-9,-5,10,10,-10,1,-5,5,-1,3,1,-1,-2,7,-9,3,-1,5,-6,-5,1,4,-9,6,-9,7,2,10,-1,3,3,9,4,-5,-1,9,-8,-10,3,7,4,1,-2,-1,7,4,-9,3,-9,8,-9,-3,-1,4,-10,5,6,1,8,-2,7,-4,-9,2,5,9,4,-3,-9,-10,-7,-3,2,1,-8,-6,9,1,-4,7,10,5,1,10,2,-7,6,4,-5,-9,-7,6,-2,-5,10,8,-1,-4,9,-2,-6,4,10,10,-2,-8,4,5,3,-6,4,-10,7,7,2,10,10,-9,-9,-6,10,10,-10,-1,6,3,-1,7,1,-5,5,8,-9,-4,8,1,-5,-1,7,7,9,-7,5,10,8,-8,3,6,2,2,1,-7,6,3,-2,-1,2,-3,10,2,9,2,-7,5,10,1,-3,-10,-8,4,-5,1,1,-4,-7,2,8,9,-2,-5,6,-6,4,-9,10,2,-8,-1,-9,1,-1,2,-5,-5,9,-1,-5,3,-4,-4,4,10,-3,1,7,-7,-7,10,-2,-10,4,-4,-8,-2,9,-7,-4,-5,9,8,-1,6,4,9,2,6,1,-9,-9,1,7,-1,6,-9,-5,3,-1,-2,-7,-10,-10,-7,8,-2,-6,-5,3,-5,3,6,-2,1,-9,8,-6,7,7,-9,-1,-6,-3,10,-8,-5,-9,-8,-9,4,-4,6,-3,5,10,-8,4,5,-4,3,10,-2,6,-1,1,-5,-10,-6,-7,-4,7,-5,4,8,7,-2,7,5,6,-2,-3,-3,-9,3,-1,2,-9,-1,-9,10,10,10,-6,3,-2,10,-2,-8,3,7,-10,-4,-4,-1,3,8,5,-9,6,4,6,5,8,-9,5,-7,-2,4,-5,10,6,9,9,-2,-3,3,10,-9,1,1,3,1,-8,-5,9,3,5,-7,-2,-9,7,6,10,-8,-3,-5,7,-4,-10,-2,-6,6,-6,6,-4,-5,-7,-10,4,5,9,6,9,-4,10,-10,8,-10,9,-4,-10,-3,8,3,-3,1,-2,9,10,-10,7,7,-6,-2,2,7,7,-9,5,-8,10,-2,10,-4,3,9,4,9], dtype = "int16")#candidate|3291|(784,)|const|int16
call_3289 = func_2921_call(relay.reshape(var_3290.astype('int16'), [16, 7, 1]), relay.reshape(const_3291.astype('int16'), [16, 7, 7]), )
call_3292 = func_2921_call(relay.reshape(var_3290.astype('int16'), [16, 7, 1]), relay.reshape(const_3291.astype('int16'), [16, 7, 7]), )
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_3293 = relay.TupleGetItem(func_3026_call(), 2)
call_3294 = relay.TupleGetItem(func_3028_call(), 2)
func_2245_call = mod.get_global_var('func_2245')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_3305 = relay.var("var_3305", dtype = "float64", shape = (416,))#candidate|3305|(416,)|var|float64
call_3304 = relay.TupleGetItem(func_2245_call(relay.reshape(var_3305.astype('float64'), [13, 16, 2]), relay.reshape(call_3262.astype('int8'), [36, 6]), ), 1)
call_3306 = relay.TupleGetItem(func_2248_call(relay.reshape(var_3305.astype('float64'), [13, 16, 2]), relay.reshape(call_3262.astype('int8'), [36, 6]), ), 1)
output = relay.Tuple([call_3256,call_3262,call_3289,var_3290,const_3291,call_3293,call_3304,var_3305,])
output2 = relay.Tuple([call_3257,call_3263,call_3292,var_3290,const_3291,call_3294,call_3306,var_3305,])
func_3309 = relay.Function([var_3290,var_3305,], output)
mod['func_3309'] = func_3309
mod = relay.transform.InferType()(mod)
mutated_mod['func_3309'] = func_3309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3309_call = mutated_mod.get_global_var('func_3309')
var_3311 = relay.var("var_3311", dtype = "int16", shape = (112,))#candidate|3311|(112,)|var|int16
var_3312 = relay.var("var_3312", dtype = "float64", shape = (416,))#candidate|3312|(416,)|var|float64
call_3310 = func_3309_call(var_3311,var_3312,)
output = call_3310
func_3313 = relay.Function([var_3311,var_3312,], output)
mutated_mod['func_3313'] = func_3313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_3369 = func_1903_call()
call_3370 = func_1903_call()
var_3374 = relay.var("var_3374", dtype = "bool", shape = (4, 9, 6))#candidate|3374|(4, 9, 6)|var|bool
bop_3375 = relay.power(call_3369.astype('float64'), relay.reshape(var_3374.astype('float64'), relay.shape_of(call_3369))) # shape=(4, 9, 6)
bop_3378 = relay.power(call_3370.astype('float64'), relay.reshape(var_3374.astype('float64'), relay.shape_of(call_3370))) # shape=(4, 9, 6)
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_3389 = func_1903_call()
call_3390 = func_1903_call()
func_2884_call = mod.get_global_var('func_2884')
func_2886_call = mutated_mod.get_global_var('func_2886')
call_3404 = relay.TupleGetItem(func_2884_call(), 0)
call_3405 = relay.TupleGetItem(func_2886_call(), 0)
uop_3408 = relay.asinh(bop_3375.astype('float64')) # shape=(4, 9, 6)
uop_3410 = relay.asinh(bop_3378.astype('float64')) # shape=(4, 9, 6)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3412 = func_3046_call()
call_3413 = func_3046_call()
bop_3416 = relay.logical_and(uop_3408.astype('bool'), relay.reshape(call_3389.astype('bool'), relay.shape_of(uop_3408))) # shape=(4, 9, 6)
bop_3419 = relay.logical_and(uop_3410.astype('bool'), relay.reshape(call_3390.astype('bool'), relay.shape_of(uop_3410))) # shape=(4, 9, 6)
func_2784_call = mod.get_global_var('func_2784')
func_2786_call = mutated_mod.get_global_var('func_2786')
call_3431 = relay.TupleGetItem(func_2784_call(), 1)
call_3432 = relay.TupleGetItem(func_2786_call(), 1)
output = relay.Tuple([call_3404,call_3412,bop_3416,call_3431,])
output2 = relay.Tuple([call_3405,call_3413,bop_3419,call_3432,])
func_3437 = relay.Function([var_3374,], output)
mod['func_3437'] = func_3437
mod = relay.transform.InferType()(mod)
mutated_mod['func_3437'] = func_3437
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3438 = relay.var("var_3438", dtype = "bool", shape = (4, 9, 6))#candidate|3438|(4, 9, 6)|var|bool
func_3437_call = mutated_mod.get_global_var('func_3437')
call_3439 = func_3437_call(var_3438)
output = call_3439
func_3440 = relay.Function([var_3438], output)
mutated_mod['func_3440'] = func_3440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_3444 = func_1845_call()
call_3445 = func_1845_call()
uop_3449 = relay.sigmoid(call_3444.astype('float64')) # shape=(4, 9, 6)
uop_3451 = relay.sigmoid(call_3445.astype('float64')) # shape=(4, 9, 6)
func_2921_call = mod.get_global_var('func_2921')
func_2925_call = mutated_mod.get_global_var('func_2925')
const_3463 = relay.const([[-3,-1,7,6],[3,7,6,-8],[-10,-7,5,-2],[9,2,5,8],[8,-6,3,9],[2,4,2,4],[-6,5,-6,2],[8,-7,-5,1],[-4,-2,-1,-3],[-9,-10,8,2],[-7,-5,-3,-8],[-10,4,-10,1],[-3,1,6,-6],[2,7,-2,-3],[-6,-9,5,10],[2,1,10,-6],[-6,7,-2,6],[-9,-3,2,9],[6,6,7,7],[1,-1,-1,-4],[-3,-9,-5,8],[-8,6,-9,-7],[-5,6,-1,1],[-2,-3,-9,-10],[-9,5,5,-8],[4,-10,-9,8],[10,-5,-9,-2],[-1,4,3,2]], dtype = "int16")#candidate|3463|(28, 4)|const|int16
var_3464 = relay.var("var_3464", dtype = "int16", shape = (784,))#candidate|3464|(784,)|var|int16
call_3462 = func_2921_call(relay.reshape(const_3463.astype('int16'), [16, 7, 1]), relay.reshape(var_3464.astype('int16'), [16, 7, 7]), )
call_3465 = func_2921_call(relay.reshape(const_3463.astype('int16'), [16, 7, 1]), relay.reshape(var_3464.astype('int16'), [16, 7, 7]), )
func_1286_call = mod.get_global_var('func_1286')
func_1289_call = mutated_mod.get_global_var('func_1289')
call_3475 = relay.TupleGetItem(func_1286_call(relay.reshape(uop_3449.astype('int8'), [4, 9, 6])), 1)
call_3476 = relay.TupleGetItem(func_1289_call(relay.reshape(uop_3449.astype('int8'), [4, 9, 6])), 1)
bop_3488 = relay.minimum(uop_3449.astype('uint32'), relay.reshape(call_3444.astype('uint32'), relay.shape_of(uop_3449))) # shape=(4, 9, 6)
bop_3491 = relay.minimum(uop_3451.astype('uint32'), relay.reshape(call_3445.astype('uint32'), relay.shape_of(uop_3451))) # shape=(4, 9, 6)
output = relay.Tuple([call_3462,const_3463,var_3464,call_3475,bop_3488,])
output2 = relay.Tuple([call_3465,const_3463,var_3464,call_3476,bop_3491,])
func_3505 = relay.Function([var_3464,], output)
mod['func_3505'] = func_3505
mod = relay.transform.InferType()(mod)
mutated_mod['func_3505'] = func_3505
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3506 = relay.var("var_3506", dtype = "int16", shape = (784,))#candidate|3506|(784,)|var|int16
func_3505_call = mutated_mod.get_global_var('func_3505')
call_3507 = func_3505_call(var_3506)
output = call_3507
func_3508 = relay.Function([var_3506], output)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_3514 = func_1845_call()
call_3515 = func_1845_call()
func_2245_call = mod.get_global_var('func_2245')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_3537 = relay.var("var_3537", dtype = "float64", shape = (416,))#candidate|3537|(416,)|var|float64
call_3536 = relay.TupleGetItem(func_2245_call(relay.reshape(var_3537.astype('float64'), [13, 16, 2]), relay.reshape(call_3514.astype('int8'), [36, 6]), ), 1)
call_3538 = relay.TupleGetItem(func_2248_call(relay.reshape(var_3537.astype('float64'), [13, 16, 2]), relay.reshape(call_3514.astype('int8'), [36, 6]), ), 1)
func_2491_call = mod.get_global_var('func_2491')
func_2496_call = mutated_mod.get_global_var('func_2496')
var_3547 = relay.var("var_3547", dtype = "float32", shape = (96,))#candidate|3547|(96,)|var|float32
const_3548 = relay.const([7.960362,-8.034500,9.177754,7.914951,-8.511974,-7.963940,-1.015204,-1.116593,-0.436428,6.379080,7.323590,0.874610,-3.704701,-8.962503,9.926631,-8.744977,2.072951,-2.258059,-8.814504,-4.039681,9.231014,-5.733878,-0.405057,0.762053,-4.325422,-9.703308,-9.649955,0.764957,0.759373,3.638283,3.445609,1.722213,-2.241758,2.576537,8.056315,0.004149,-4.571196,6.181358,-2.370935,1.345668,9.864460,8.720541,2.546584,5.815914,-3.579546,-5.648769,-3.617937,8.549801,4.895803,-7.923280,-2.603134,3.935126,2.694634,5.467326,3.131559,-2.763802,-0.429582,2.286520,1.437304,-8.991365,2.708635,4.494239,3.797541,-1.787212,-0.784851,1.341545,-6.559310,9.729380,5.700839,6.755875,-1.969937,-4.465288,7.889343,-1.004105,-6.460967,5.927524,3.678276,2.381472,2.863825,-9.874557,-8.217897,-3.563931,-4.873338,-0.997655,-1.668638,7.265715,-4.894118,2.007038,6.962190,-0.596698,-6.436675,9.684920,-2.494589,-8.759707,-0.957155,4.423470,2.916122,4.816418,-0.597909,7.636887,6.161242,2.787810,-4.839642,-0.063548,-7.323232,5.541342,-9.596330,9.241331,-7.050778,-4.659932,-4.923390,4.704460,2.205646,0.298604,6.616055,-4.533737,7.742748,-9.104605,-4.628208,9.886342,6.569797,5.295655,8.272738,-2.195684,3.529302,-8.938921,0.507663,5.082790,-9.092792,-8.367760,3.902859,7.371375,-7.392338,9.511687,-3.480432,3.879931,5.937854,4.537032,2.931188,-6.972371,-3.399478,-9.860440,5.314609,-1.127031,0.365716,4.821097,2.922104,5.757698,-7.664916,-9.070431,-8.982587,-2.719923,-4.679221,-3.223895,2.822638,-8.577592,-1.773337,2.745192,-6.863931,3.148994,-2.331711,3.660561,4.019520,7.737559,7.366626,-7.568110,-1.069766,5.435418,-2.222177,-5.618905,7.324818,8.096979,-2.394700,0.137149,-9.418470,-7.862032,2.534085,-4.710811,-2.513432,-8.106612,2.359783,2.131789,9.080293,8.051972,8.102542,0.777625,-2.719540,-1.188865,-7.354755,-9.179917,-9.376730,8.214112,-9.315010,0.029161,-4.828552,-8.514102,-9.919023,8.648554,-5.147812,-7.494630,-6.478579,-5.261923,-8.977337,0.744279,-6.289618,-8.969713,-3.190972,-8.463459,1.488248,-0.856183,6.906678,-1.621751,-5.646016,9.177280,-2.481060,-1.891397,-5.867268,7.699678,5.082128,5.885753,-1.151463,4.389998,9.565965,5.743725,6.274854,-8.313561,-4.035061,-8.557850,-3.217319,-2.260548,9.207650,-8.933343,2.760322,6.285007,-1.537537,7.645960,-9.294870,-1.163639,-8.761101,-4.503841,4.552435,5.654882,5.307348,-2.764904,4.108613,-8.464701,-8.744762,-6.910563,0.889490,-5.649321,-7.535401,-5.526053,-6.144975,8.628996,1.308328,-1.117978,-4.060581,-0.271055,-8.150462,-6.679779,4.527512,-0.438684,4.685879,-9.908808,-1.164999,-4.029863,-3.865380,0.606887,7.168831,4.341686,6.024381,9.608060,3.158356,3.647418,3.831175,-3.296257,0.127247,-5.759796,8.324911,1.671033,4.918206,0.966109,-9.230755,2.168319,7.841707,-3.937717,-0.299201,-7.052537,-8.291574,4.414176,1.989013,-7.802165,9.150524,3.381308,1.962395,-9.519882,9.702875,-5.439069,2.128411,0.435472,1.579688,0.452795,-2.357658,9.980935,0.132684,-0.457575,-5.755927,4.988207,2.626452,0.409168,5.850618,7.913291,7.810218,2.279886,5.593295,5.063645,-4.813514,1.899766,-0.404010,6.453800,5.797672,5.629460,0.228614,0.045782,3.403451,8.874572,1.874723,0.534072,0.837938,0.370457,-6.860156,9.831610,8.260494,0.300768,1.113037,5.102840,-7.180507,2.967258,-7.758079,-0.120542,0.216654,-1.135646,-5.861426,4.509660,-7.682342,0.630556,8.710058,-7.038128,1.076160,-0.104352,-4.722629,2.216285,-9.524495,-8.721396,-9.882132,6.463175,6.015708,-6.527518,0.695332,1.696453,-2.467855,-4.239949,3.396516,-6.428239,-7.911748,0.908156,-1.674986,1.564752,4.092308,9.071306,-6.199551,1.070629,4.384151,-9.195025,2.664640,-9.332023,-2.998844,7.850765,3.549037,-9.152513,8.538105,2.709104,-0.021691,-7.676298,-5.928057,6.179154,-5.235971,-3.045757,-3.570039,5.159431,-4.164677,1.900576,-5.324469,-3.919172,-2.504386,-4.906470,1.081175,-3.481702,-8.973565,7.072287,-6.844502,-9.154736,-2.641296,-0.538926,6.671971,-0.626244,-1.716478,-3.161623,5.093439,-6.022033,4.594290,1.269220,-9.934567,-3.187019,-1.705946,-3.997889,6.852234,-3.211428,2.281557,-9.362991,-8.053156,5.392042,6.853497,6.419992,-2.757494,-3.653861,-2.718254,-9.986844,9.312559,-0.116689,8.054553,2.361460,7.970118,-8.219705,-8.890301,3.047258,2.437868,0.354339,-7.754456,0.154711,1.881316,-8.601963,3.355709,-3.382800,2.971575,9.840321,0.179918,1.266423,-3.573230,-8.634635,0.612342,9.976561,-3.843950,9.056590,8.658673,3.632794,-3.470691,6.484635,9.726195,4.302399,-4.600653,5.379888,5.328323,-1.967507,-4.794261,-2.586349,-0.221548,-9.222939,2.313369,8.565093,8.057529,6.427445,-5.199867,3.652532,-4.913765,-4.368349,4.322162,4.920981,2.683022,-9.056031,-4.865237,3.524176,-7.808696,5.614626,2.851834,5.156907,8.681867,-0.200888,2.967942,8.359295,-9.155726,-6.062898,4.564224,-8.761302,0.057200,-3.934059,-5.372513,-9.766692,-1.889342,-0.762754,-2.654377,-6.022649,-8.498546,1.551558,-6.104464,8.340257,-1.089195,4.509216,7.537665,-5.689997,-9.568724,-8.991109,-2.170416,-4.333455,-2.606023,-5.916503,-9.215761,4.759126,-4.710654,-9.088653,7.930165,3.888236,8.334276,-4.500194,0.497005,0.051120,6.832552,-0.877048,-8.241644,-5.165252,7.727121,8.532359,1.060898,-9.593016,9.103628,7.569650,-8.750060,-3.305190,7.294912,4.950162,-5.193935,-3.544840,-0.657627,7.218198,7.792136,-1.940375,0.887359,-3.775537,-6.290486,-4.747757,2.445622,-7.900731,-2.287556,7.170638,8.203185,-5.575157,9.561227,-3.156431,8.565035,-5.628441,5.006796,0.516202,-5.984668,-7.899941,-2.444905,-4.816621,-8.343183,-9.196274,-1.832887,-8.473322,-2.600883,6.157156,1.514760,5.779941,2.436880,-7.406430,-6.743247,2.784140,3.516676,9.625789,-4.676072,-8.693687,1.590588,-1.345642,-3.607815,6.182006,0.588590,5.284972,-6.999569,-5.412206,-8.901393,6.425451,-8.160796,-5.372533,-7.403909,-6.236726,3.896317,7.323010,6.616221,-1.195601,-3.497520,-1.043534,-0.128860,-1.089929,-0.869409,1.761941,2.184932,-3.404822,0.194979,-8.757915,-9.290841,7.650617,7.583709,-6.366628,-2.432325,-5.925427,7.370403,-5.474105,-0.591166,-2.336012,0.630445,-4.353125,-1.810147,1.100432,1.256236,8.092327,-6.876317,4.673173,4.497882,-9.183370,8.735268,-8.253922,8.867755,-2.521718,-4.805468,-8.524869,-0.296618,-8.806832,1.811159,2.047578,4.374154,0.175427,6.308759,4.418912,-8.764121,-5.740785,6.403606,-7.431222,8.892562,-7.920860,-9.806990,-3.293092,9.757487,7.267011,-5.358787,6.624611,-0.054528,4.053800,-9.158932,-2.111785,-9.503719,-6.571658,-5.365839,-6.289962,9.682607,7.853432,4.806778,1.943516,-8.464016,-2.823800,4.488454,9.453221,-5.166379,0.493332,8.960995,8.712124,-2.471973,3.917967,6.745559,-9.276674,5.288154,-9.456291,3.528226,3.574045,-6.633449,-4.240888,-1.079085,9.574502,-9.262955,0.069074,9.719062,7.301039,-7.127457,-9.550327,-6.473010,-9.331809,-6.117089,1.177296,-5.945942,7.525314,-5.478038,-7.917174,1.167593,8.019317,-5.871415,-4.390462,9.294780,0.232745,-9.202007,7.032742,0.217900,-4.978996,-5.963361,3.027929,4.952603,-2.257570,8.720924,-3.692963,-4.690481,-6.955718,-6.562674,-2.523003,6.739873,9.833823,1.803798,-5.350996,-7.339368,-8.321577,-7.179195,-5.895441,6.710908,4.159428,6.107447,2.517763,9.999063,2.653295,-9.553129,-8.324665,4.864780,-4.041920,-1.837519,1.726507,3.652606,-1.364263,-7.366933,0.685265,6.639334,-4.323343,-4.686657,-7.506438,4.103614,5.053558,-0.295686,3.776397,1.864643,-6.747322,6.552940,3.134213,-8.620503,-3.621050,-4.392626,-1.975472,1.051275,-5.288754,-2.786177,0.400217,-5.273641,-3.688234,-7.441126,2.006165,2.322147,-6.623830,5.191228,7.497217,6.720736,-0.821179,-2.738567,2.573903,5.082870,1.626516,-2.422449,-9.171284,-4.656334,3.399437,-2.339685,-9.548209,3.875317,-3.933976,-7.606727,-0.511975,-0.397260,1.074607,0.655570,-8.421099,0.997061,-4.874857,-2.232848,-8.705002,7.146222,-4.019214,-6.555087,5.170949,5.202157,7.449870,-0.671375,3.550995,-0.448281,3.056283,5.271202,4.986241,4.527454,-9.102846,-6.063967,-7.341202,9.586561,0.155903,-6.541668,7.632769,8.671560,5.331747,-6.934388,-2.478411,-1.024384,-6.165079,9.144776,-4.712351,6.885130,-3.898740,8.011479,-6.113766,0.267274,6.893310,-3.825507,4.651709,8.339267,5.638947,6.322327,-5.342580,6.949963,0.778216,-3.548311,-4.712887,8.806705,6.747280,2.160194,6.041751,-3.156652,-0.143919,3.657815,-6.778745,9.823038,-1.098453,7.019901,-1.482959,1.254058,0.816992,6.854548,1.597419,-2.857679,4.354115,-4.700884,7.918435,2.968929,-6.744914,1.069894,0.534751,-3.196882,-6.592125,2.427138,2.262416,-1.075966,-4.260210,-8.829367,-2.451963,7.497466,-0.867180,-7.309232,-0.185338,-5.491634,-8.060254,9.206614,-7.272262,9.924949,9.104999,8.259936,2.566596,1.438809,9.009942,-5.349724,-9.876622,9.430501,4.446597,-3.538648,-1.603991,-4.722965,6.584366,-0.801676,-3.727060,-8.884503,-0.976535,-1.690744,6.450768,-7.955280,2.086094,7.955782,-3.470590,-9.446568,-1.342721,1.846257,3.113624,-4.278036,6.823102,-8.303856,-6.686675,2.687261,-0.651895,8.564612,5.287575,-6.761822,-7.322387,-8.273809,0.095746,-2.486982,-8.968744,-2.789269,-8.355992,-1.236674,5.343721,8.007915,5.143589,4.804743,-3.393140,5.852700,-0.302992,-2.437417,4.649744,9.731993,7.926841,7.450644,5.843897,-7.423614,-6.201798,2.402718,4.265036,7.547614,9.132596,6.939467,7.096968,1.962982,-2.779638,-8.562957,-2.945099,-1.093225,-2.100038,1.812538,2.658308,2.449242,-8.441659,-6.303265,9.148842,-2.721848,-3.654630,-8.193159,3.566167,9.072447,8.221265,8.077092,8.539687,8.897806,8.349348,1.015691,-3.241486,-6.724389,2.094946,8.570076,8.770950,4.703340,0.667448,1.079102,3.561071,-9.495505,6.595408,-0.407258,-1.751104,-0.846721,9.299818,-2.428017,-9.529409,-1.053836,5.664810,-1.176123,-7.449950,-3.789340,2.545489,-0.645517,-4.415472,9.977031,-1.785043,-7.860498,0.331699,7.219585,-2.074728,5.478312,-0.356155,-5.906217,1.924761,-9.457016,-3.855125,7.009609,8.744555,-7.848666,-7.050132,2.929853,-6.024635,0.988507,-8.530047,-5.651532,8.166948,3.951981,7.677524,8.262118,-7.638885,-4.100947,8.044224,-4.516040,6.213201,-5.077892,-8.690404,2.708477,-8.860550,-0.218321,6.882578,8.363045,-1.659043,-3.316324,9.240354,-2.551712,-0.436087,-7.878613,-9.299616,-3.674607,-2.641074,-7.887615,-0.093447,5.200689,-2.359306,2.306591,-6.906461,-0.696354,0.094666,-3.023432,5.887978,-0.552356,-3.749472,7.883209,5.729503,-4.796456,-1.206525,-3.744029,-2.470026,8.321758,3.792547,-3.728369,-8.972490,2.655787,-8.043429,-3.125415,-3.834868,0.973190,0.948375,-7.555548,-0.153806,-7.510417,8.617698,7.294360,-9.194565,-8.592923,7.437519,1.471107,-9.601430,3.116595,5.292011,-4.768065,-0.844818,-0.362992,-4.327610,-2.924841,4.566923,6.031336,5.664889,7.069563,-6.996508,5.056923,-1.255779,8.246400,1.341540,9.831489,-5.126571,3.846281,2.934760,-7.878807,-1.912422,-4.460477,-2.436193,-5.713458,-0.739964,7.607180,0.203247,-8.604257,-4.689115,-2.516720,-5.583852,-4.551335,1.186393,1.844811,3.123437,-5.344863,-2.169239,4.119740,1.212942,-4.545354,1.090668,-7.271234,8.159133,6.973595,-4.180128,5.792310,1.533410,2.675725,1.617378,-8.803064,-0.980610,-7.571389,6.943079,6.991485,0.925890,5.803179,-1.885677,-8.587721,-3.843114,3.228933,3.681005,-4.628736,-1.362418,-5.553797,-0.832557,-7.582271,2.934427,-5.629387,-3.891972,8.315974,8.800778,4.760149,-7.317793,9.533833,5.979232,5.073142,-5.411221,9.879350,6.442297,-6.580337,-9.417131,1.670806,-1.715702,2.823193,2.950370,-7.276498,7.854263,-9.293920,4.940490,-8.145592,-8.383581,-3.784888,4.395843,4.917916,3.162735,3.413653,-3.174820,7.302285,-9.858203,-9.046820,-5.453671,-5.314890,-7.425494,5.133976,1.492435,-6.958445,-4.558127,-9.922251,-2.159125,-3.418023,4.796764,-7.832871,-1.877361,-7.075826,-1.009660,1.714351,-6.407078,-0.143582,-2.097513,-2.906208,0.299340,-3.509648,6.136301,-3.854565,-9.451529,1.645575,-0.511958,-3.762742,-3.489814,0.602774,8.895628,7.077945,-1.812718,-5.374989,5.269179,-0.109661,7.857196,-1.558130,8.345470,-7.967974,-8.163138,-0.922343,2.043694,7.699848,1.531330,-6.833444,8.266663,-3.577527,6.241954,2.696260,-3.577114,-6.699486,-1.825701,-5.975059,8.078758,9.145465,0.754295,-6.218307,-3.735124,-9.936105,-1.048169,-1.275880,-2.235837,3.832104,7.816743,-2.332394,5.091448,7.079234,-9.874078,3.753444,0.943351,4.029599,-7.837426,2.363610,0.927690,8.075092,7.109020,-2.581048,-7.453174,8.622947,-1.193037,6.262137,-7.388278,7.690104,0.465898,-0.798756,5.180095,2.577793,0.577246,5.113926,-6.553270,-6.890452,-6.312054,3.271963,4.275129,3.090757,-6.990105,3.269516,9.892802,7.634230,9.005959,7.418053,9.791736,8.754761,-0.165845,-8.204926,6.341251,-0.721854,4.854765,-1.993971,-7.429388,-7.320256,0.267210,-3.174016,-6.367955,8.162811,1.978327,-7.129242,1.141130,-9.730266,-5.678823,-7.435419,9.363931,-6.756169,-2.747231,1.165644,-1.983844,3.458863,2.745751,-6.520572,-0.120501,-7.838800,2.700464,-6.975708,-6.859604,-9.134169,9.192432,-2.773049,7.170581,9.321101,4.535609,-9.143361,-7.080933,7.624055,2.934763,8.259514,8.620523,-4.717719,7.805449,6.648932,1.139264,-5.112906,-3.428088,9.840869,8.631815,7.614489,-7.008116,-3.927724,-7.703767,-9.363928,-4.202234,5.783469,8.701834,-7.382434,-8.307855,-8.902786,8.620631,5.276327,2.585575,5.524347,1.896369,-4.860415,-0.103617,3.680998,-7.283167,7.568377,9.408889,3.985172,-6.665566,2.170352,9.633780,-1.402121,3.108377,5.692161,-0.133958,2.892518,4.238076,1.642349,0.976428,-4.280625,8.845916,-8.155043,-4.568541,7.793191,4.480961,-0.219312,3.674981,6.768228,-9.928050,9.053212,9.958790,-5.411374,-3.154725,-4.683759,-9.724659,-7.738889,-1.964890,7.683705,-7.049435,4.235973,6.877645,-3.206671,-0.602406,3.194222,-2.817363,-7.891096,-3.354669,5.466927,-8.659142,-1.260910,-7.446184,-2.661573,4.803081,-9.870105,7.718795,8.041786,7.559334,3.474334,8.037309,-7.880824,4.950189,3.726428,7.095411,0.790439,-2.549645,1.803087,-6.312016,-1.242319,7.243246,2.118344,-7.582702,8.286458,-8.386199,-2.036947,-9.016710,-2.244105,3.161190,8.603832,-2.127662,-6.628007,-5.677080,5.536236,-3.891010,-8.054083,-2.062912,-5.167868,-1.820287,-2.479743,-5.801555], dtype = "float32")#candidate|3548|(1440,)|const|float32
const_3549 = relay.const([-10,2,4,-10,-1,8,3,6,5,-4,7,7,-4,6,7,-7,-6,3,-3,2,9,7,-2,-5,2,2,-1,7,-8,-3,6,2,-1,3,-7,-9,-5,-2,1,5,-7,3,8,3,-2,-2,8,-2,10,4,2,-6,2,-7,-5,6,-9,-10,-8,-4,-9,9,-10,-6,-8,-8,4,1,-3,-8,-9,2,5,7,-5,6,-7,1,7,10,8,10,-3,7,-7,4,-1,-8,-8,-4,7,-7,6,-4,5,-2,1,2,-3,9,4,-10,10,3,-2,-1,6,5,-7,-7,-4,-5,1,8,8,3,-1,-9,10,10,-9,-3,10,9,9,-10,-2,-8,2,-6,1,4,-2,-4,-5,6,-5,10,-9,3,-4,-10,5,1,4,-2,7,-9,-9,3,7,-9,-8,-10,-10,4,-3,10,2,9,-9,1,7,6,4,1,1,-4,10,8,6,-4,8,-10,7,8,-10,-3,2,-2,-1,8,2,-4,7,-4,6,1,-4,-8,-10,-7,9,9,1,6,4,-5,7,3,-3,-4,-7,-7,-7,3,3,-10,-2,-4,10,-5,5,5,1,-3,-6,-5,3,7,-7,9,-10,2,10,5,5,8,-3,-1,2,-9,2,-3,-6,-7,1,-2,-7,-5,10,8,-1,7,-9,8,-4,-2,-3,-1,7,3,-6,-9,1,1,-5,9,5,-1,6,-6,8,-7,4,1,8,7,1,8,-1,3,9,-3,-8,9,-4,4,-4,3,1,-7,-10,-4,2,10,4,-1,-5,-7,9,-7,-2,4], dtype = "int64")#candidate|3549|(294,)|const|int64
call_3546 = relay.TupleGetItem(func_2491_call(relay.reshape(var_3547.astype('float32'), [6, 16, 1]), relay.reshape(const_3548.astype('float32'), [6, 16, 15]), relay.reshape(const_3548.astype('float64'), [6, 16, 15]), relay.reshape(const_3549.astype('int64'), [294,]), ), 4)
call_3550 = relay.TupleGetItem(func_2496_call(relay.reshape(var_3547.astype('float32'), [6, 16, 1]), relay.reshape(const_3548.astype('float32'), [6, 16, 15]), relay.reshape(const_3548.astype('float64'), [6, 16, 15]), relay.reshape(const_3549.astype('int64'), [294,]), ), 4)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3571 = relay.TupleGetItem(func_2536_call(), 0)
call_3572 = relay.TupleGetItem(func_2537_call(), 0)
func_2595_call = mod.get_global_var('func_2595')
func_2596_call = mutated_mod.get_global_var('func_2596')
call_3578 = func_2595_call()
call_3579 = func_2595_call()
output = relay.Tuple([call_3514,call_3536,var_3537,call_3546,var_3547,const_3548,const_3549,call_3571,call_3578,])
output2 = relay.Tuple([call_3515,call_3538,var_3537,call_3550,var_3547,const_3548,const_3549,call_3572,call_3579,])
func_3592 = relay.Function([var_3537,var_3547,], output)
mod['func_3592'] = func_3592
mod = relay.transform.InferType()(mod)
mutated_mod['func_3592'] = func_3592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3592_call = mutated_mod.get_global_var('func_3592')
var_3594 = relay.var("var_3594", dtype = "float64", shape = (416,))#candidate|3594|(416,)|var|float64
var_3595 = relay.var("var_3595", dtype = "float32", shape = (96,))#candidate|3595|(96,)|var|float32
call_3593 = func_3592_call(var_3594,var_3595,)
output = call_3593
func_3596 = relay.Function([var_3594,var_3595,], output)
mutated_mod['func_3596'] = func_3596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_3604 = relay.TupleGetItem(func_2570_call(), 0)
call_3605 = relay.TupleGetItem(func_2571_call(), 0)
func_50_call = mod.get_global_var('func_50')
func_52_call = mutated_mod.get_global_var('func_52')
const_3608 = relay.const([-3.301765,0.196049,-6.908923,4.507127,5.130894,6.918312,-6.389957,2.681916,4.781689,8.313833,7.447692,6.549684,6.566950,4.951127,-9.739362,9.056366,-0.556164,-6.000639,9.347941,6.583495,-5.850667,8.384864,-4.720620,5.192044,6.872474,6.352541,5.337364,0.149263,-6.382373,5.197093,5.414748,3.237525,-7.954643,-1.499627,2.124865,-7.137389,-1.567468,-2.412983,-4.489209,-6.491605,6.213653,1.428992,1.759617,6.724941,3.610695,-5.197090,9.603264,-1.745402,0.820694,-0.810355,2.861601,-5.550334,-8.930609,-8.058306,-7.522214,-3.660537,-0.941807,4.034953,-2.475792,5.737057,4.382989,-2.422275,5.261305,-4.767149,-7.176043,9.763851,-8.590435,2.725725,4.723926,6.035855,8.537435,7.840102,4.272064,6.877242,2.805973,-5.205917,-8.342150,6.557425,3.713039,-3.298219,-9.372650,1.007310,4.131494,4.525833,-7.264569,-4.185988,-8.360440,-0.831786,-6.361609,-3.094171,-9.917438,7.243698,5.184307,1.388606,-0.777593,-6.313023,9.127112,8.160701,4.416089,4.938014,-1.373999,0.230719,7.514008,-2.133627,7.063888,8.783084,1.197228,-9.332621,-8.767020,-4.046385,4.744097,8.898029,-9.553719,0.702302,-0.823309,-5.512883,-3.813366,8.032466,4.506830,-4.946381,-7.471050,-1.381307,-4.570135,8.161303,-4.788030,6.469569,-6.147024,8.122371,-6.361219,-6.924020], dtype = "float64")#candidate|3608|(130,)|const|float64
call_3607 = relay.TupleGetItem(func_50_call(relay.reshape(const_3608.astype('float64'), [13, 10, 1])), 0)
call_3609 = relay.TupleGetItem(func_52_call(relay.reshape(const_3608.astype('float64'), [13, 10, 1])), 0)
uop_3622 = relay.tan(call_3607.astype('float64')) # shape=(13, 10, 9)
uop_3624 = relay.tan(call_3609.astype('float64')) # shape=(13, 10, 9)
output = relay.Tuple([call_3604,const_3608,uop_3622,])
output2 = relay.Tuple([call_3605,const_3608,uop_3624,])
func_3630 = relay.Function([], output)
mod['func_3630'] = func_3630
mod = relay.transform.InferType()(mod)
output = func_3630()
func_3631 = relay.Function([], output)
mutated_mod['func_3631'] = func_3631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_3632 = func_2162_call()
call_3633 = func_2162_call()
output = relay.Tuple([call_3632,])
output2 = relay.Tuple([call_3633,])
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
func_2620_call = mod.get_global_var('func_2620')
func_2622_call = mutated_mod.get_global_var('func_2622')
call_3657 = func_2620_call()
call_3658 = func_2620_call()
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3672 = func_3046_call()
call_3673 = func_3046_call()
uop_3692 = relay.acos(call_3657.astype('float64')) # shape=(4, 9, 6)
uop_3694 = relay.acos(call_3658.astype('float64')) # shape=(4, 9, 6)
func_2840_call = mod.get_global_var('func_2840')
func_2842_call = mutated_mod.get_global_var('func_2842')
call_3699 = relay.TupleGetItem(func_2840_call(), 0)
call_3700 = relay.TupleGetItem(func_2842_call(), 0)
func_2338_call = mod.get_global_var('func_2338')
func_2342_call = mutated_mod.get_global_var('func_2342')
var_3702 = relay.var("var_3702", dtype = "int64", shape = (294,))#candidate|3702|(294,)|var|int64
const_3703 = relay.const([-1.147632,-6.752291,6.129791,7.139020,-3.389374,-6.048735,-4.693772,7.868166,6.555447,7.381964,2.189895,3.530018,-4.040638,-1.476567,-8.035798,2.237562,6.205790,-6.453699,8.538464,3.782690,-0.198808,-7.375419,-4.420272,-7.294287,4.140485,-2.165858,-4.334344,-9.423290,0.635525,-4.598862,-9.485485,6.753017,1.352178,-8.902995,7.929145,-9.007529,0.346393,5.145053,1.326200,0.545627,5.933359,3.267565,-1.428892,-3.133196,-8.237345,9.517566,-2.892000,-2.616606,-8.352572,6.276685,-2.790905,-3.178739,-1.466733,2.526407,3.343066,-0.630516,1.420042,-9.167929,0.821497,3.824984,0.223711,-3.053182,3.161176,8.696199,0.360152,-4.482712,1.147848,4.416083,-7.338278,5.469211,-2.549827,-2.835080,3.933399,0.352163,-5.646159,-0.703908,6.599030,9.809620,4.859224,2.391013,3.138838,2.903680,-6.411533,7.869542,1.505827,-3.988375,-2.454004,3.312420,-9.440891,5.600879,-1.883184,-5.010423,-3.116574,-9.980916,9.451516,7.949832,8.906939,6.220341,5.562399,-0.058137,7.942462,-3.093603,-7.013940,0.295290,-2.752947,4.050403,-4.976045,2.932150,0.985988,-6.478364,1.550494,-9.459977,-3.712033,-9.711848,-7.402418,3.464963,2.723997,4.723608,5.712842,-9.761492,0.418483,-4.226057,-0.528588,1.743084,-1.044837,-6.810389,7.825339,-1.721370,-1.392230,0.285849], dtype = "float64")#candidate|3703|(130,)|const|float64
call_3701 = relay.TupleGetItem(func_2338_call(relay.reshape(var_3702.astype('int64'), [294,]), relay.reshape(const_3703.astype('float64'), [130,]), ), 4)
call_3704 = relay.TupleGetItem(func_2342_call(relay.reshape(var_3702.astype('int64'), [294,]), relay.reshape(const_3703.astype('float64'), [130,]), ), 4)
func_1534_call = mod.get_global_var('func_1534')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_3707 = relay.TupleGetItem(func_1534_call(relay.reshape(var_3702.astype('int64'), [7, 3, 14]), relay.reshape(var_3702.astype('int64'), [7, 3, 14]), relay.reshape(call_3701.astype('float32'), [7, 3, 14]), ), 3)
call_3708 = relay.TupleGetItem(func_1539_call(relay.reshape(var_3702.astype('int64'), [7, 3, 14]), relay.reshape(var_3702.astype('int64'), [7, 3, 14]), relay.reshape(call_3701.astype('float32'), [7, 3, 14]), ), 3)
func_3102_call = mod.get_global_var('func_3102')
func_3104_call = mutated_mod.get_global_var('func_3104')
call_3712 = relay.TupleGetItem(func_3102_call(), 0)
call_3713 = relay.TupleGetItem(func_3104_call(), 0)
output = relay.Tuple([call_3672,uop_3692,call_3699,call_3701,var_3702,const_3703,call_3707,call_3712,])
output2 = relay.Tuple([call_3673,uop_3694,call_3700,call_3704,var_3702,const_3703,call_3708,call_3713,])
func_3724 = relay.Function([var_3702,], output)
mod['func_3724'] = func_3724
mod = relay.transform.InferType()(mod)
var_3725 = relay.var("var_3725", dtype = "int64", shape = (294,))#candidate|3725|(294,)|var|int64
output = func_3724(var_3725)
func_3726 = relay.Function([var_3725], output)
mutated_mod['func_3726'] = func_3726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2784_call = mod.get_global_var('func_2784')
func_2786_call = mutated_mod.get_global_var('func_2786')
call_3732 = relay.TupleGetItem(func_2784_call(), 2)
call_3733 = relay.TupleGetItem(func_2786_call(), 2)
uop_3734 = relay.atan(call_3732.astype('float32')) # shape=(4, 9, 6)
uop_3736 = relay.atan(call_3733.astype('float32')) # shape=(4, 9, 6)
func_2245_call = mod.get_global_var('func_2245')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_3744 = relay.var("var_3744", dtype = "float64", shape = (416,))#candidate|3744|(416,)|var|float64
call_3743 = relay.TupleGetItem(func_2245_call(relay.reshape(var_3744.astype('float64'), [13, 16, 2]), relay.reshape(uop_3734.astype('int8'), [36, 6]), ), 2)
call_3745 = relay.TupleGetItem(func_2248_call(relay.reshape(var_3744.astype('float64'), [13, 16, 2]), relay.reshape(uop_3734.astype('int8'), [36, 6]), ), 2)
func_2784_call = mod.get_global_var('func_2784')
func_2786_call = mutated_mod.get_global_var('func_2786')
call_3780 = relay.TupleGetItem(func_2784_call(), 0)
call_3781 = relay.TupleGetItem(func_2786_call(), 0)
output = relay.Tuple([uop_3734,call_3743,var_3744,call_3780,])
output2 = relay.Tuple([uop_3736,call_3745,var_3744,call_3781,])
func_3805 = relay.Function([var_3744,], output)
mod['func_3805'] = func_3805
mod = relay.transform.InferType()(mod)
var_3806 = relay.var("var_3806", dtype = "float64", shape = (416,))#candidate|3806|(416,)|var|float64
output = func_3805(var_3806)
func_3807 = relay.Function([var_3806], output)
mutated_mod['func_3807'] = func_3807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2707_call = mod.get_global_var('func_2707')
func_2708_call = mutated_mod.get_global_var('func_2708')
call_3823 = relay.TupleGetItem(func_2707_call(), 0)
call_3824 = relay.TupleGetItem(func_2708_call(), 0)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3826 = relay.TupleGetItem(func_2536_call(), 0)
call_3827 = relay.TupleGetItem(func_2537_call(), 0)
output = relay.Tuple([call_3823,call_3826,])
output2 = relay.Tuple([call_3824,call_3827,])
func_3833 = relay.Function([], output)
mod['func_3833'] = func_3833
mod = relay.transform.InferType()(mod)
mutated_mod['func_3833'] = func_3833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mutated_mod.get_global_var('func_3833')
call_3834 = func_3833_call()
output = call_3834
func_3835 = relay.Function([], output)
mutated_mod['func_3835'] = func_3835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3948 = relay.var("var_3948", dtype = "float32", shape = (5, 13, 6))#candidate|3948|(5, 13, 6)|var|float32
var_3949 = relay.var("var_3949", dtype = "float32", shape = (5, 13, 6))#candidate|3949|(5, 13, 6)|var|float32
bop_3950 = relay.floor_divide(var_3948.astype('float32'), relay.reshape(var_3949.astype('float32'), relay.shape_of(var_3948))) # shape=(5, 13, 6)
uop_3968 = relay.sin(var_3948.astype('float32')) # shape=(5, 13, 6)
output = relay.Tuple([bop_3950,uop_3968,])
output2 = relay.Tuple([bop_3950,uop_3968,])
func_3979 = relay.Function([var_3948,var_3949,], output)
mod['func_3979'] = func_3979
mod = relay.transform.InferType()(mod)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3979_call = mutated_mod.get_global_var('func_3979')
var_3981 = relay.var("var_3981", dtype = "float32", shape = (5, 13, 6))#candidate|3981|(5, 13, 6)|var|float32
var_3982 = relay.var("var_3982", dtype = "float32", shape = (5, 13, 6))#candidate|3982|(5, 13, 6)|var|float32
call_3980 = func_3979_call(var_3981,var_3982,)
output = call_3980
func_3983 = relay.Function([var_3981,var_3982,], output)
mutated_mod['func_3983'] = func_3983
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4055 = relay.var("var_4055", dtype = "float64", shape = (15, 11, 4))#candidate|4055|(15, 11, 4)|var|float64
uop_4056 = relay.sqrt(var_4055.astype('float64')) # shape=(15, 11, 4)
output = uop_4056
output2 = uop_4056
func_4063 = relay.Function([var_4055,], output)
mod['func_4063'] = func_4063
mod = relay.transform.InferType()(mod)
mutated_mod['func_4063'] = func_4063
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4064 = relay.var("var_4064", dtype = "float64", shape = (15, 11, 4))#candidate|4064|(15, 11, 4)|var|float64
func_4063_call = mutated_mod.get_global_var('func_4063')
call_4065 = func_4063_call(var_4064)
output = call_4065
func_4066 = relay.Function([var_4064], output)
mutated_mod['func_4066'] = func_4066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3102_call = mod.get_global_var('func_3102')
func_3104_call = mutated_mod.get_global_var('func_3104')
call_4075 = relay.TupleGetItem(func_3102_call(), 0)
call_4076 = relay.TupleGetItem(func_3104_call(), 0)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
var_4092 = relay.var("var_4092", dtype = "float64", shape = (130, 1))#candidate|4092|(130, 1)|var|float64
call_4091 = relay.TupleGetItem(func_2403_call(relay.reshape(var_4092.astype('float64'), [1, 130])), 0)
call_4093 = relay.TupleGetItem(func_2405_call(relay.reshape(var_4092.astype('float64'), [1, 130])), 0)
var_4096 = relay.var("var_4096", dtype = "bool", shape = (4, 9, 6))#candidate|4096|(4, 9, 6)|var|bool
bop_4097 = relay.bitwise_xor(call_4091.astype('uint64'), relay.reshape(var_4096.astype('uint64'), relay.shape_of(call_4091))) # shape=(4, 9, 6)
bop_4100 = relay.bitwise_xor(call_4093.astype('uint64'), relay.reshape(var_4096.astype('uint64'), relay.shape_of(call_4093))) # shape=(4, 9, 6)
output = relay.Tuple([call_4075,var_4092,bop_4097,])
output2 = relay.Tuple([call_4076,var_4092,bop_4100,])
func_4115 = relay.Function([var_4092,var_4096,], output)
mod['func_4115'] = func_4115
mod = relay.transform.InferType()(mod)
mutated_mod['func_4115'] = func_4115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4115_call = mutated_mod.get_global_var('func_4115')
var_4117 = relay.var("var_4117", dtype = "float64", shape = (130, 1))#candidate|4117|(130, 1)|var|float64
var_4118 = relay.var("var_4118", dtype = "bool", shape = (4, 9, 6))#candidate|4118|(4, 9, 6)|var|bool
call_4116 = func_4115_call(var_4117,var_4118,)
output = call_4116
func_4119 = relay.Function([var_4117,var_4118,], output)
mutated_mod['func_4119'] = func_4119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_4125 = relay.TupleGetItem(func_2027_call(), 0)
call_4126 = relay.TupleGetItem(func_2029_call(), 0)
output = call_4125
output2 = call_4126
func_4139 = relay.Function([], output)
mod['func_4139'] = func_4139
mod = relay.transform.InferType()(mod)
output = func_4139()
func_4140 = relay.Function([], output)
mutated_mod['func_4140'] = func_4140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2884_call = mod.get_global_var('func_2884')
func_2886_call = mutated_mod.get_global_var('func_2886')
call_4207 = relay.TupleGetItem(func_2884_call(), 0)
call_4208 = relay.TupleGetItem(func_2886_call(), 0)
func_2884_call = mod.get_global_var('func_2884')
func_2886_call = mutated_mod.get_global_var('func_2886')
call_4219 = relay.TupleGetItem(func_2884_call(), 0)
call_4220 = relay.TupleGetItem(func_2886_call(), 0)
func_3437_call = mod.get_global_var('func_3437')
func_3440_call = mutated_mod.get_global_var('func_3440')
const_4231 = relay.const([True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True], dtype = "bool")#candidate|4231|(216,)|const|bool
call_4230 = relay.TupleGetItem(func_3437_call(relay.reshape(const_4231.astype('bool'), [4, 9, 6])), 3)
call_4232 = relay.TupleGetItem(func_3440_call(relay.reshape(const_4231.astype('bool'), [4, 9, 6])), 3)
output = relay.Tuple([call_4207,call_4219,call_4230,const_4231,])
output2 = relay.Tuple([call_4208,call_4220,call_4232,const_4231,])
func_4241 = relay.Function([], output)
mod['func_4241'] = func_4241
mod = relay.transform.InferType()(mod)
mutated_mod['func_4241'] = func_4241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4241_call = mutated_mod.get_global_var('func_4241')
call_4242 = func_4241_call()
output = call_4242
func_4243 = relay.Function([], output)
mutated_mod['func_4243'] = func_4243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2646_call = mod.get_global_var('func_2646')
func_2647_call = mutated_mod.get_global_var('func_2647')
call_4282 = func_2646_call()
call_4283 = func_2646_call()
output = call_4282
output2 = call_4283
func_4290 = relay.Function([], output)
mod['func_4290'] = func_4290
mod = relay.transform.InferType()(mod)
mutated_mod['func_4290'] = func_4290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4290_call = mutated_mod.get_global_var('func_4290')
call_4291 = func_4290_call()
output = call_4291
func_4292 = relay.Function([], output)
mutated_mod['func_4292'] = func_4292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2884_call = mod.get_global_var('func_2884')
func_2886_call = mutated_mod.get_global_var('func_2886')
call_4318 = relay.TupleGetItem(func_2884_call(), 0)
call_4319 = relay.TupleGetItem(func_2886_call(), 0)
func_1956_call = mod.get_global_var('func_1956')
func_1958_call = mutated_mod.get_global_var('func_1958')
var_4325 = relay.var("var_4325", dtype = "float64", shape = (130,))#candidate|4325|(130,)|var|float64
call_4324 = relay.TupleGetItem(func_1956_call(relay.reshape(var_4325.astype('float64'), [130, 1])), 2)
call_4326 = relay.TupleGetItem(func_1958_call(relay.reshape(var_4325.astype('float64'), [130, 1])), 2)
func_2194_call = mod.get_global_var('func_2194')
func_2198_call = mutated_mod.get_global_var('func_2198')
var_4331 = relay.var("var_4331", dtype = "float32", shape = (650,))#candidate|4331|(650,)|var|float32
call_4330 = func_2194_call(relay.reshape(var_4331.astype('float32'), [5, 10, 13]), relay.reshape(var_4331.astype('float32'), [5, 10, 13]), )
call_4332 = func_2194_call(relay.reshape(var_4331.astype('float32'), [5, 10, 13]), relay.reshape(var_4331.astype('float32'), [5, 10, 13]), )
uop_4337 = relay.atanh(call_4324.astype('float32')) # shape=(130, 1)
uop_4339 = relay.atanh(call_4326.astype('float32')) # shape=(130, 1)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_4362 = relay.TupleGetItem(func_2570_call(), 0)
call_4363 = relay.TupleGetItem(func_2571_call(), 0)
uop_4367 = relay.sinh(uop_4337.astype('float64')) # shape=(130, 1)
uop_4369 = relay.sinh(uop_4339.astype('float64')) # shape=(130, 1)
output = relay.Tuple([call_4318,var_4325,call_4330,var_4331,call_4362,uop_4367,])
output2 = relay.Tuple([call_4319,var_4325,call_4332,var_4331,call_4363,uop_4369,])
func_4371 = relay.Function([var_4325,var_4331,], output)
mod['func_4371'] = func_4371
mod = relay.transform.InferType()(mod)
mutated_mod['func_4371'] = func_4371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4371_call = mutated_mod.get_global_var('func_4371')
var_4373 = relay.var("var_4373", dtype = "float64", shape = (130,))#candidate|4373|(130,)|var|float64
var_4374 = relay.var("var_4374", dtype = "float32", shape = (650,))#candidate|4374|(650,)|var|float32
call_4372 = func_4371_call(var_4373,var_4374,)
output = call_4372
func_4375 = relay.Function([var_4373,var_4374,], output)
mutated_mod['func_4375'] = func_4375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2840_call = mod.get_global_var('func_2840')
func_2842_call = mutated_mod.get_global_var('func_2842')
call_4377 = relay.TupleGetItem(func_2840_call(), 0)
call_4378 = relay.TupleGetItem(func_2842_call(), 0)
output = call_4377
output2 = call_4378
func_4381 = relay.Function([], output)
mod['func_4381'] = func_4381
mod = relay.transform.InferType()(mod)
output = func_4381()
func_4382 = relay.Function([], output)
mutated_mod['func_4382'] = func_4382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4290_call = mod.get_global_var('func_4290')
func_4292_call = mutated_mod.get_global_var('func_4292')
call_4432 = func_4290_call()
call_4433 = func_4290_call()
output = call_4432
output2 = call_4433
func_4440 = relay.Function([], output)
mod['func_4440'] = func_4440
mod = relay.transform.InferType()(mod)
mutated_mod['func_4440'] = func_4440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4440_call = mutated_mod.get_global_var('func_4440')
call_4441 = func_4440_call()
output = call_4441
func_4442 = relay.Function([], output)
mutated_mod['func_4442'] = func_4442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_4466 = func_3046_call()
call_4467 = func_3046_call()
output = relay.Tuple([call_4466,])
output2 = relay.Tuple([call_4467,])
func_4468 = relay.Function([], output)
mod['func_4468'] = func_4468
mod = relay.transform.InferType()(mod)
output = func_4468()
func_4469 = relay.Function([], output)
mutated_mod['func_4469'] = func_4469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mod.get_global_var('func_3638')
func_3640_call = mutated_mod.get_global_var('func_3640')
call_4508 = relay.TupleGetItem(func_3638_call(), 0)
call_4509 = relay.TupleGetItem(func_3640_call(), 0)
output = relay.Tuple([call_4508,])
output2 = relay.Tuple([call_4509,])
func_4512 = relay.Function([], output)
mod['func_4512'] = func_4512
mod = relay.transform.InferType()(mod)
mutated_mod['func_4512'] = func_4512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4512_call = mutated_mod.get_global_var('func_4512')
call_4513 = func_4512_call()
output = call_4513
func_4514 = relay.Function([], output)
mutated_mod['func_4514'] = func_4514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_4519 = relay.TupleGetItem(func_2027_call(), 0)
call_4520 = relay.TupleGetItem(func_2029_call(), 0)
func_4512_call = mod.get_global_var('func_4512')
func_4514_call = mutated_mod.get_global_var('func_4514')
call_4538 = relay.TupleGetItem(func_4512_call(), 0)
call_4539 = relay.TupleGetItem(func_4514_call(), 0)
output = relay.Tuple([call_4519,call_4538,])
output2 = relay.Tuple([call_4520,call_4539,])
func_4543 = relay.Function([], output)
mod['func_4543'] = func_4543
mod = relay.transform.InferType()(mod)
output = func_4543()
func_4544 = relay.Function([], output)
mutated_mod['func_4544'] = func_4544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_4591 = relay.TupleGetItem(func_1728_call(), 1)
call_4592 = relay.TupleGetItem(func_1730_call(), 1)
func_3724_call = mod.get_global_var('func_3724')
func_3726_call = mutated_mod.get_global_var('func_3726')
const_4618 = relay.const([10,6,-4,-8,-7,7,1,3,8,5,-9,7,5,3,6,10,-1,-9,5,-1,2,-8,-3,-2,-10,8,-1,-3,4,8,7,4,-6,4,-2,4,4,-7,-2,9,-6,-3,5,-5,-1,1,-3,-5,-9,2,3,-7,9,-7,7,-3,4,-9,-2,-10,-7,1,5,1,-5,9,-9,9,4,-9,2,1,-7,-9,-7,4,-9,4,-2,-1,-5,9,7,-4,-5,-10,-4,-5,3,2,2,-4,2,6,-2,-5,5,5,-3,3,-1,-5,7,-5,-3,-10,2,7,-3,-8,-7,-4,-8,-6,-7,6,-5,-2,-2,-3,-4,9,9,10,8,9,-2,10,3,10,9,7,-9,-4,-7,-6,-2,-7,-3,-4,-4,6,7,5,-6,-9,2,-8,-6,2,9,-6,-2,-3,9,-6,10,10,-10,7,-1,10,4,-4,10,6,3,2,5,2,3,-7,-2,8,2,-9,-2,6,-6,-6,6,8,4,-5,-5,2,-5,-1,-6,10,-6,2,-7,-4,9,-1,-4,4,-1,8,8,-6,-9,-1,-5,2,9,9,-2,-10,3,-8,2,-6,3,-1,-3,3,1,6,6,-7,-6,10,9,1,-1,10,10,-6,-9,-5,1,6,-3,-8,-4,1,-1,-8,-1,2,-9,-3,8,4,-4,2,7,7,-2,-9,10,-6,1,1,4,-1,-6,2,6,1,-2,-5,-1,-9,9,-1,7,2,-1,1,-6,6,9,-6,-3,4,10,-4,-4,-5,-2,2,4,-1,-8,-10,-5,8,6,10,1,-5], dtype = "int64")#candidate|4618|(294,)|const|int64
call_4617 = relay.TupleGetItem(func_3724_call(relay.reshape(const_4618.astype('int64'), [294,])), 6)
call_4619 = relay.TupleGetItem(func_3726_call(relay.reshape(const_4618.astype('int64'), [294,])), 6)
uop_4624 = relay.asinh(const_4618.astype('float32')) # shape=(294,)
func_4139_call = mod.get_global_var('func_4139')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_4630 = func_4139_call()
call_4631 = func_4139_call()
output = relay.Tuple([call_4591,call_4617,uop_4624,call_4630,])
output2 = relay.Tuple([call_4592,call_4619,uop_4624,call_4631,])
func_4641 = relay.Function([], output)
mod['func_4641'] = func_4641
mod = relay.transform.InferType()(mod)
output = func_4641()
func_4642 = relay.Function([], output)
mutated_mod['func_4642'] = func_4642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_4649 = func_4139_call()
call_4650 = func_4139_call()
output = relay.Tuple([call_4649,])
output2 = relay.Tuple([call_4650,])
func_4661 = relay.Function([], output)
mod['func_4661'] = func_4661
mod = relay.transform.InferType()(mod)
mutated_mod['func_4661'] = func_4661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4661_call = mutated_mod.get_global_var('func_4661')
call_4662 = func_4661_call()
output = call_4662
func_4663 = relay.Function([], output)
mutated_mod['func_4663'] = func_4663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_4664 = relay.TupleGetItem(func_2570_call(), 0)
call_4665 = relay.TupleGetItem(func_2571_call(), 0)
func_3805_call = mod.get_global_var('func_3805')
func_3807_call = mutated_mod.get_global_var('func_3807')
const_4694 = relay.const([[4.956745,-7.195080,-3.026023,-0.809682,7.956368,3.675869,-7.032617,0.859662,6.495931,-9.461864,5.608091,-3.866070,-3.886103,-7.206039,2.397382,6.524379,3.580981,8.428275,-3.897465,-5.579869,-7.591932,-7.377069,1.066060,6.764186,0.517901,4.718206,9.909007,-0.248826,2.870411,3.839954,-9.192235,9.423663,-5.713645,4.581783,1.449284,-1.845210,9.240594,-9.891328,-6.510058,-8.306812,4.870852,-6.906851,1.898797,-6.903105,1.435830,-4.479013,-4.950519,-2.758516,-3.901551,2.406652,4.345206,6.802982,-5.062327,3.777892,5.576538,5.791504,4.968439,-3.556730,-3.433565,0.120971,-5.328822,4.983364,-5.939874,9.718023,9.250366,-0.197618,-1.570085,-2.703208,6.812557,-2.128607,6.067638,-3.072429,7.367688,4.801351,7.445482,-6.517997,-5.747019,2.723216,5.812755,-4.747867,0.908219,3.784919,-9.134174,9.809798,8.228007,5.944508,1.548423,-2.569834,-8.758951,-5.871428,-5.118555,2.893043,-1.004298,3.787991,9.833511,-6.689455,-2.460242,-0.707595,2.472097,1.436659,6.101907,4.949369,-7.129554,-1.504788,-1.791856,-1.661565,4.247056,5.028908,-3.295017,4.510228,-6.875489,0.370449,8.988195,-2.731211,5.105538,7.390262,-4.354243,7.648727,-6.880551,5.216827,-4.684181,-8.752366,9.020148,9.395727,-2.951107,4.830310,-1.809350,-8.519851,-7.305304,9.679102,-2.193022,7.295186,1.617290,1.314614,-3.887916,-0.686262,-2.217723,-3.345169,1.882325,-7.423109,-4.856197,-7.743839,-2.957731,-7.363542,5.672516,-3.155160,-0.008098,-8.230818,-7.815361,-9.136329,-4.681399,0.998109,8.786626,-3.157280,7.027495,-1.820780,-3.264822,-2.495594,6.211881,-3.847043,-3.601796,-2.621463,-6.625005,9.028444,-0.022655,8.225785,-5.044224,-4.076744,-5.631845,-7.500227,1.689516,8.006350,-5.925064,-7.233729,-6.837331,-3.333930,7.000233,4.519301,-7.376985,-7.909286,-5.288604,6.908929,-1.639019,-8.807778,3.518231,-5.456627,-8.388768,-5.665557,0.390508,-7.675832,8.348073,0.437638,-3.029143,-0.670221,5.918602,2.329788,-6.787062,-1.629370,-2.300783,6.750367,-0.986991,-0.665382,7.606699,7.464269,7.524695,-0.997536,-1.764726,9.271696,1.341518,1.323400,-3.848316,-8.974073,-2.019082,5.916422,-7.932167,-1.074855,-3.892580,5.059791,7.555505,2.772614,-3.932137,-8.425155,7.534313,5.662736,2.963602,0.486272,-8.293368,0.363434,-6.476721,8.031651,9.701213,3.753112,7.027952,-6.744415,9.681790,7.191267,9.478320,6.411915,-3.029095,8.342674,1.672481,0.378235,7.120787,-1.348921,-0.387479,-0.348932,0.955292,4.473533,-2.194472,-9.211112,2.423239,2.489180,9.424126,0.658439,-6.814003,7.343109,6.177030,5.481949,5.717105,0.855893,6.860225,-7.519873,7.468216,1.617504,5.813164,-0.570698,-7.716822,5.874653,-5.110822,6.028528,-4.507340,-0.269257,6.563542,-4.475068,-2.514037,-7.367402,4.994760,-6.158477,7.867491,-6.917535,9.702334,0.006240,-2.201976,6.978795,-7.467578,0.164531,-1.794434,-9.038420,7.072182,-3.323936,-1.856347,-0.914050,7.159880,1.910986,-9.372059,6.763155,-3.212445,0.420104,-6.382284,4.835123,7.337197,0.324270,-7.552555,-7.093545,-5.328678,5.955198,6.916241,-7.707496,3.548556,7.225434,8.819861,3.793489,-8.196279,-8.658306,-1.810435,9.325970,7.883342,0.016654,-8.456721,6.436134,-3.898279,-9.299063,-5.918406,1.128517,-7.564337,-2.654197,1.356683,7.573095,-3.378941,-9.659442,1.586135,0.761476,-9.111961,-3.003249,-1.970930,9.219406,7.669170,-5.523811,-8.630031,9.071571,6.927570,-6.685736,3.589689,-1.859162,-1.896820,-3.880880,-8.545615,-7.116546,-9.974681,0.574557,-4.668114,-0.642925,-5.234905,-1.844199,-1.583516,6.378672,7.430615,-4.856933,3.789402,-1.352542,-6.421179,0.681283,-9.106208,6.850541,4.191027,0.327606,-8.417144,5.558519,7.944169,8.894800,0.764927,1.591993,9.770232,0.022133,-8.979896,-5.935299,6.458079,0.605792,4.129200,-8.175321,5.075404,-3.718997,2.967755,1.934913,2.204804,-2.387844,2.245341,2.452667,-8.400568,-6.357155,4.763395,3.375655,-3.769944,-5.788229,7.755695,-9.806083,1.059459,-7.318540,-1.448220,7.859850,0.259512,-9.367073,0.076609,9.496053,3.994342,-2.711073,-7.719087,1.583343,-6.946890,-7.589105,-1.348371,-2.267115,0.637647,9.884304,-6.348266,-1.642390]], dtype = "float64")#candidate|4694|(1, 416)|const|float64
call_4693 = relay.TupleGetItem(func_3805_call(relay.reshape(const_4694.astype('float64'), [416,])), 2)
call_4695 = relay.TupleGetItem(func_3807_call(relay.reshape(const_4694.astype('float64'), [416,])), 2)
output = relay.Tuple([call_4664,call_4693,const_4694,])
output2 = relay.Tuple([call_4665,call_4695,const_4694,])
func_4697 = relay.Function([], output)
mod['func_4697'] = func_4697
mod = relay.transform.InferType()(mod)
mutated_mod['func_4697'] = func_4697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4697_call = mutated_mod.get_global_var('func_4697')
call_4698 = func_4697_call()
output = call_4698
func_4699 = relay.Function([], output)
mutated_mod['func_4699'] = func_4699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_4702 = func_4139_call()
call_4703 = func_4139_call()
func_2194_call = mod.get_global_var('func_2194')
func_2198_call = mutated_mod.get_global_var('func_2198')
var_4709 = relay.var("var_4709", dtype = "float32", shape = (650,))#candidate|4709|(650,)|var|float32
call_4708 = func_2194_call(relay.reshape(var_4709.astype('float32'), [5, 10, 13]), relay.reshape(var_4709.astype('float32'), [5, 10, 13]), )
call_4710 = func_2194_call(relay.reshape(var_4709.astype('float32'), [5, 10, 13]), relay.reshape(var_4709.astype('float32'), [5, 10, 13]), )
bop_4711 = relay.floor_mod(call_4708.astype('float32'), relay.reshape(var_4709.astype('float32'), relay.shape_of(call_4708))) # shape=(5, 10, 13)
bop_4714 = relay.floor_mod(call_4710.astype('float32'), relay.reshape(var_4709.astype('float32'), relay.shape_of(call_4710))) # shape=(5, 10, 13)
var_4737 = relay.var("var_4737", dtype = "float32", shape = (5, 10, 13))#candidate|4737|(5, 10, 13)|var|float32
bop_4738 = relay.maximum(call_4708.astype('float64'), relay.reshape(var_4737.astype('float64'), relay.shape_of(call_4708))) # shape=(5, 10, 13)
bop_4741 = relay.maximum(call_4710.astype('float64'), relay.reshape(var_4737.astype('float64'), relay.shape_of(call_4710))) # shape=(5, 10, 13)
func_3724_call = mod.get_global_var('func_3724')
func_3726_call = mutated_mod.get_global_var('func_3726')
var_4746 = relay.var("var_4746", dtype = "int64", shape = (294,))#candidate|4746|(294,)|var|int64
call_4745 = relay.TupleGetItem(func_3724_call(relay.reshape(var_4746.astype('int64'), [294,])), 2)
call_4747 = relay.TupleGetItem(func_3726_call(relay.reshape(var_4746.astype('int64'), [294,])), 2)
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_4755 = relay.TupleGetItem(func_2536_call(), 0)
call_4756 = relay.TupleGetItem(func_2537_call(), 0)
uop_4758 = relay.cos(bop_4738.astype('float32')) # shape=(5, 10, 13)
uop_4760 = relay.cos(bop_4741.astype('float32')) # shape=(5, 10, 13)
output = relay.Tuple([call_4702,bop_4711,call_4745,var_4746,call_4755,uop_4758,])
output2 = relay.Tuple([call_4703,bop_4714,call_4747,var_4746,call_4756,uop_4760,])
func_4777 = relay.Function([var_4709,var_4737,var_4746,], output)
mod['func_4777'] = func_4777
mod = relay.transform.InferType()(mod)
mutated_mod['func_4777'] = func_4777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4777_call = mutated_mod.get_global_var('func_4777')
var_4779 = relay.var("var_4779", dtype = "float32", shape = (650,))#candidate|4779|(650,)|var|float32
var_4780 = relay.var("var_4780", dtype = "float32", shape = (5, 10, 13))#candidate|4780|(5, 10, 13)|var|float32
var_4781 = relay.var("var_4781", dtype = "int64", shape = (294,))#candidate|4781|(294,)|var|int64
call_4778 = func_4777_call(var_4779,var_4780,var_4781,)
output = call_4778
func_4782 = relay.Function([var_4779,var_4780,var_4781,], output)
mutated_mod['func_4782'] = func_4782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4512_call = mod.get_global_var('func_4512')
func_4514_call = mutated_mod.get_global_var('func_4514')
call_4816 = relay.TupleGetItem(func_4512_call(), 0)
call_4817 = relay.TupleGetItem(func_4514_call(), 0)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
var_4844 = relay.var("var_4844", dtype = "float64", shape = (130,))#candidate|4844|(130,)|var|float64
call_4843 = relay.TupleGetItem(func_2403_call(relay.reshape(var_4844.astype('float64'), [1, 130])), 4)
call_4845 = relay.TupleGetItem(func_2405_call(relay.reshape(var_4844.astype('float64'), [1, 130])), 4)
func_3505_call = mod.get_global_var('func_3505')
func_3508_call = mutated_mod.get_global_var('func_3508')
const_4855 = relay.const([[6,5,-1,-7,8,-8,7,4,7,-3,-5,-8,-8,2,8,7,-4,-9,5,-3,-1,-4,2,4,-3,8,7,6,9,-9,8,5,2,-10,-8,-10,3,-7,-3,4,-1,-5,-10,-4,-9,-8,-10,-10,6,1,-2,-3,8,-9,5,8,-6,2,2,-5,-8,-7,-5,-5,6,5,9,-2,-1,8,2,10,9,-4,-8,1,3,8,-4,10,-9,7,-4,4,9,1,-10,-9,-3,-7,5,8,-7,-7,9,2,-4,-5,9,4,-3,-9,-6,-9,5,-1,-5,10,5,-2,5,-2,2,-7,-7,9,8,1,6,2,-8,-4,9,-3,-1,1,-7,-7,8,-2,-7,-5,8,-8,7,-8,10,-8,-3,-5,5,2,-7,-3,-3,2,-5,-4,6,-9,-9,-10,8,7,-8,-8,8,-5,7,4,4,-1,-4,3,-4,-4,9,3,9,-1,-4,-10,-10,-9,-4,8,-8,8,-3,-3,5,-1,9,-4,-4,5,-5,-10,1,-4,2,-4,1,4,5,1],[5,4,8,4,4,-9,6,6,9,-2,-3,3,8,-8,-5,3,-4,5,7,-3,-1,-10,4,-6,-7,7,-7,-6,6,-10,-6,2,-9,2,-8,-7,-9,-10,4,-9,-6,-2,5,-10,3,-3,-2,-7,-1,7,3,-10,10,7,-6,8,3,7,-8,-10,-8,10,-7,10,-7,7,10,6,7,-7,-2,-7,5,-4,2,5,-8,-7,-3,2,6,4,1,8,-3,-1,10,-1,-1,-9,10,10,-9,2,-5,-6,6,-9,-7,-4,-3,-5,-2,-7,9,3,-10,-7,1,-2,4,9,5,-8,6,3,7,-10,2,2,-5,-3,8,-3,9,-9,-3,-6,8,-3,8,-2,3,5,-3,-7,2,3,-1,-2,2,-5,10,7,7,-2,5,-3,-8,-4,-7,-9,-2,-2,-9,-3,-6,7,-2,-5,4,6,-3,-10,9,-4,-4,7,5,8,4,4,10,5,6,10,9,-1,-7,3,-4,4,8,-5,1,-7,-5,-4,-2,6,10,10,-6,-10,-2,10],[-10,6,-6,-2,-2,-3,-10,3,-5,-10,7,-4,10,7,-7,-8,1,-6,2,-7,7,-3,-6,-8,7,6,7,8,-4,-9,-2,-9,-2,-2,-2,-1,9,-9,2,6,7,-5,1,-2,-8,7,10,3,-10,-6,-5,5,-3,-7,-2,-6,6,-1,-5,-4,-6,1,5,-7,10,-9,-10,-9,7,-2,10,7,-9,2,3,-5,7,4,3,-6,5,-7,10,-10,3,-7,1,-8,-4,4,-8,-6,-8,-6,-4,-3,-10,3,-8,8,-6,4,-8,-8,5,-10,5,-8,8,2,-10,10,7,9,-6,-5,-9,10,1,10,3,1,-7,9,-4,-9,7,-4,1,-10,-2,1,-5,-1,-10,2,-10,-1,3,4,2,4,3,4,3,2,8,-7,4,-1,10,10,-8,8,-1,-9,-6,-10,10,2,7,-9,7,10,-5,-6,4,-4,6,-4,-4,8,3,-10,4,-6,-8,-10,2,-6,2,-1,-7,1,-9,-10,5,5,-8,10,-9,-6,1,1,7,2],[9,-8,-10,-10,1,2,-8,3,-3,1,-9,-10,5,6,1,3,-1,8,9,10,8,9,2,3,7,9,2,-8,5,1,2,-5,7,6,-1,-10,-2,-6,-1,10,-4,-3,10,-7,7,-8,4,-2,9,10,6,-1,-7,1,-6,5,9,10,3,-2,-5,-7,-8,-3,9,-6,-1,3,2,7,6,9,4,-7,-7,5,-1,-3,3,5,9,-7,8,10,6,1,-1,-9,10,-10,-7,10,-7,-7,1,2,-5,2,-1,-7,-10,-2,9,-6,7,7,-10,2,-2,-10,2,4,-5,5,9,-4,10,-9,-7,-9,10,-8,3,-2,10,-7,-5,4,-5,5,-10,-2,7,9,-8,-10,-4,-3,-10,-1,6,-5,-9,1,7,-10,9,9,-7,9,9,-4,-8,2,-1,-8,-3,9,1,7,-10,-5,3,2,-4,-3,-10,6,5,6,10,-2,9,4,3,-8,-10,-9,-8,-1,4,5,-3,2,8,-4,5,9,9,-2,7,-5,-4,8,-7,-4]], dtype = "int16")#candidate|4855|(4, 196)|const|int16
call_4854 = relay.TupleGetItem(func_3505_call(relay.reshape(const_4855.astype('int16'), [784,])), 4)
call_4856 = relay.TupleGetItem(func_3508_call(relay.reshape(const_4855.astype('int16'), [784,])), 4)
func_2784_call = mod.get_global_var('func_2784')
func_2786_call = mutated_mod.get_global_var('func_2786')
call_4863 = relay.TupleGetItem(func_2784_call(), 0)
call_4864 = relay.TupleGetItem(func_2786_call(), 0)
const_4874 = relay.const([[-4,8,7,10,7,4,-10,-10,-10,-1,-4,7,7,-6,-6,5,-8,-10,6,-8,1,10,7,-4,-3,-3,-9,8,-6,-5,3,-10,2,-5,4,-5,5,8,7,8,8,-10,-4,5,3,2,-9,-9,6,3,-7,-5,-4,-6,-5,-5,-8,2,-3,3,6,-6,-2,7,-8,8,-1,-8,5,7,10,5,-7,1,-3,-8,2,5,6,1,-4,-9,-1,-9,-3,-10,-10,-1,1,7,-6,4,-8,3,-1,-9,-3,-10,-7,3,-7,5,8,-4,-7,5,-5,-3,-10,-6,9,7,-4,-6,-8,-3,2,2,-3,10,-7,-3,-6,5,1,6,-7,-1,2,5,8,6,-5,1,5,8,-10,6,7,3,-3,9,-4,2,-2,5,-7,2,-9,2,6,-10,2,2,5,9,-6,9,-3,-5,2,-4,3,10,9,-8,1,1,3,-5,3,-8,6,-9,2,5,8,-10,-7,2,2,3,9,-9,9,1,-9,1,8,-6,7,-4,-1,5,5,-4],[-9,-2,-10,9,4,1,8,-1,-3,-7,-6,-5,-5,7,-8,-9,-7,-5,2,6,3,9,3,-8,-5,-9,5,-2,-4,2,-9,9,4,2,-10,-1,-10,-4,10,-1,8,10,4,4,10,-10,-9,-6,6,8,-8,9,-1,3,7,-8,4,8,1,-7,-8,-1,-7,7,-5,-9,5,-3,1,8,9,-4,-4,-2,2,6,-8,6,-2,-1,9,-9,6,-1,-7,-8,4,1,4,-5,-5,-8,-7,-8,-7,-7,-9,-3,10,3,-2,4,-4,-6,-8,-9,-3,6,1,-3,5,9,8,-8,-5,-6,3,-4,2,-7,4,-3,-5,9,3,8,-1,1,-6,-10,9,1,3,-10,7,5,-5,10,-9,8,10,9,1,-3,-8,-10,-8,-8,-8,7,-6,-9,-3,3,-6,4,-4,-9,5,-4,6,10,6,-4,8,10,-4,-7,7,-8,10,1,9,9,-4,8,8,4,8,6,9,-2,-6,1,8,8,-5,1,1,-7,4,4,3,-4,6,-7],[-10,10,-7,-9,2,4,-8,-1,-7,-3,4,-1,-5,-10,-6,6,5,2,-8,-8,10,-10,-6,-7,-1,-2,-10,-4,9,-6,8,-1,-7,-6,3,7,-3,-4,-8,-2,3,-4,8,-6,1,-1,3,3,-4,6,2,-3,-10,5,-7,-7,-4,1,-10,-8,8,-1,3,10,-4,7,10,10,-8,-8,-4,5,-9,-10,3,9,1,-2,-5,-4,-1,-2,2,2,8,2,6,-2,6,-3,3,-2,-3,9,-9,6,3,-2,1,2,4,3,-3,-5,8,8,10,-4,-4,-1,-7,4,7,4,10,7,-1,-5,9,3,-10,9,-3,-4,-7,2,4,-3,-4,8,2,-9,8,-9,-6,4,-7,7,-5,7,-8,7,4,2,6,1,7,-3,6,2,6,9,1,3,6,10,-10,-7,-7,-4,1,3,7,-3,-9,6,-2,-1,8,-9,-6,10,7,10,-6,-9,2,-3,7,4,10,3,3,-5,10,7,6,-3,5,-7,10,8,-7,10,6,1],[-4,-7,2,9,-9,-9,-6,-8,-6,9,-10,-7,-7,-2,-1,-8,9,1,9,-3,-8,3,-7,-2,5,-10,-10,1,-5,2,-6,-10,-6,-6,3,-5,-4,-5,-9,-5,-10,-9,-1,2,3,-2,2,4,7,5,9,-10,-8,5,2,2,-4,-6,3,-3,-10,5,-10,-2,-7,6,-6,-3,1,-2,10,9,-6,1,3,-6,-10,6,8,-7,-4,-4,-9,-5,-5,-7,2,8,-3,7,-2,10,4,2,-8,8,1,-2,-7,5,5,-6,8,-5,3,-8,7,-9,-7,-4,1,7,-3,6,-8,-3,-3,-10,-5,3,-8,-4,-8,-7,-5,8,-2,10,5,-7,-7,6,1,10,-10,5,3,-5,2,5,-3,-5,-9,-10,5,7,-10,-1,-6,7,5,6,-1,10,-10,-5,10,-10,7,5,-9,-3,3,10,-8,-7,-8,10,1,5,6,6,9,7,6,-7,6,4,5,-1,10,5,-3,9,6,-7,5,-10,-1,-2,1,-4,1,-6,-3,-1]], dtype = "int16")#candidate|4874|(4, 196)|const|int16
bop_4875 = relay.greater(const_4855.astype('bool'), relay.reshape(const_4874.astype('bool'), relay.shape_of(const_4855))) # shape=(4, 196)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_4878 = relay.TupleGetItem(func_3026_call(), 0)
call_4879 = relay.TupleGetItem(func_3028_call(), 0)
uop_4882 = relay.sqrt(const_4855.astype('float32')) # shape=(4, 196)
output = relay.Tuple([call_4816,call_4843,var_4844,call_4854,call_4863,bop_4875,call_4878,uop_4882,])
output2 = relay.Tuple([call_4817,call_4845,var_4844,call_4856,call_4864,bop_4875,call_4879,uop_4882,])
func_4884 = relay.Function([var_4844,], output)
mod['func_4884'] = func_4884
mod = relay.transform.InferType()(mod)
mutated_mod['func_4884'] = func_4884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4885 = relay.var("var_4885", dtype = "float64", shape = (130,))#candidate|4885|(130,)|var|float64
func_4884_call = mutated_mod.get_global_var('func_4884')
call_4886 = func_4884_call(var_4885)
output = call_4886
func_4887 = relay.Function([var_4885], output)
mutated_mod['func_4887'] = func_4887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_4917 = func_4139_call()
call_4918 = func_4139_call()
func_2536_call = mod.get_global_var('func_2536')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_4920 = relay.TupleGetItem(func_2536_call(), 0)
call_4921 = relay.TupleGetItem(func_2537_call(), 0)
var_4925 = relay.var("var_4925", dtype = "bool", shape = (4, 9, 6))#candidate|4925|(4, 9, 6)|var|bool
bop_4926 = relay.less(call_4917.astype('bool'), relay.reshape(var_4925.astype('bool'), relay.shape_of(call_4917))) # shape=(4, 9, 6)
bop_4929 = relay.less(call_4918.astype('bool'), relay.reshape(var_4925.astype('bool'), relay.shape_of(call_4918))) # shape=(4, 9, 6)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_4937 = relay.TupleGetItem(func_2570_call(), 0)
call_4938 = relay.TupleGetItem(func_2571_call(), 0)
output = relay.Tuple([call_4920,bop_4926,call_4937,])
output2 = relay.Tuple([call_4921,bop_4929,call_4938,])
func_4948 = relay.Function([var_4925,], output)
mod['func_4948'] = func_4948
mod = relay.transform.InferType()(mod)
var_4949 = relay.var("var_4949", dtype = "bool", shape = (4, 9, 6))#candidate|4949|(4, 9, 6)|var|bool
output = func_4948(var_4949)
func_4950 = relay.Function([var_4949], output)
mutated_mod['func_4950'] = func_4950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2707_call = mod.get_global_var('func_2707')
func_2708_call = mutated_mod.get_global_var('func_2708')
call_4961 = relay.TupleGetItem(func_2707_call(), 0)
call_4962 = relay.TupleGetItem(func_2708_call(), 0)
output = relay.Tuple([call_4961,])
output2 = relay.Tuple([call_4962,])
func_4969 = relay.Function([], output)
mod['func_4969'] = func_4969
mod = relay.transform.InferType()(mod)
output = func_4969()
func_4970 = relay.Function([], output)
mutated_mod['func_4970'] = func_4970
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4974 = relay.const([[[-7,3,10,-10,-8],[-10,-5,-5,-6,8],[7,4,9,10,-3],[3,-7,-2,8,3],[-4,-10,-9,-6,1],[6,1,7,-5,1],[1,8,10,4,1],[-3,-4,3,-7,8],[-2,-7,6,6,-10],[-9,-1,-8,-8,-7],[4,3,-3,9,5],[10,-4,4,-1,-1],[-7,2,9,9,4],[4,7,4,-4,-2],[4,8,-8,-8,-3]],[[2,1,-6,-7,6],[10,-9,-9,-9,-10],[4,2,10,6,-3],[-6,7,-2,-6,9],[-8,3,-7,2,5],[-6,4,3,-8,-1],[-8,-7,-4,9,5],[1,-8,-3,-7,1],[-7,-3,3,-6,-6],[5,3,10,-10,-5],[-8,10,-3,3,8],[-3,10,-5,-5,7],[7,5,3,-5,-6],[-8,9,2,-1,-3],[8,-5,6,-3,-10]],[[-2,2,6,5,-8],[4,-5,6,-6,-2],[-9,6,1,3,-3],[-6,-9,-2,-6,6],[8,-2,2,10,-6],[-8,-5,8,-8,-3],[5,6,10,8,-7],[-9,-6,-7,10,6],[-2,-2,1,-4,-2],[-10,6,10,-5,1],[-5,-8,3,9,5],[-1,2,-3,-5,1],[-1,4,-6,1,-3],[5,5,10,1,1],[-7,-10,-8,-3,9]],[[2,-3,-7,-1,10],[3,3,-9,3,-4],[-5,-9,-1,9,1],[8,-5,-2,-1,1],[6,-7,9,3,7],[8,-8,6,-5,-5],[-10,-2,5,-9,6],[8,-3,2,-4,-6],[2,-2,3,4,-10],[4,4,-6,9,-5],[-5,-8,1,-2,5],[-5,-4,-1,-2,4],[-4,5,6,6,9],[2,-8,4,-10,-4],[4,4,-8,-4,-10]],[[4,7,-1,-3,8],[-10,-5,1,-10,4],[6,5,8,4,4],[8,-7,1,8,5],[-5,-6,-5,-10,6],[9,3,-3,-7,-3],[-3,3,6,8,-8],[-9,9,-3,-10,9],[6,9,2,-2,-9],[4,-4,3,-10,5],[3,-1,7,9,7],[-5,-6,6,-4,-8],[1,-6,8,-8,-10],[6,-5,10,-3,3],[-4,4,-1,-9,9]]], dtype = "uint32")#candidate|4974|(5, 15, 5)|const|uint32
var_4975 = relay.var("var_4975", dtype = "uint32", shape = (5, 15, 5))#candidate|4975|(5, 15, 5)|var|uint32
bop_4976 = relay.bitwise_or(const_4974.astype('uint32'), relay.reshape(var_4975.astype('uint32'), relay.shape_of(const_4974))) # shape=(5, 15, 5)
output = bop_4976
output2 = bop_4976
func_4986 = relay.Function([var_4975,], output)
mod['func_4986'] = func_4986
mod = relay.transform.InferType()(mod)
mutated_mod['func_4986'] = func_4986
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4987 = relay.var("var_4987", dtype = "uint32", shape = (5, 15, 5))#candidate|4987|(5, 15, 5)|var|uint32
func_4986_call = mutated_mod.get_global_var('func_4986')
call_4988 = func_4986_call(var_4987)
output = call_4988
func_4989 = relay.Function([var_4987], output)
mutated_mod['func_4989'] = func_4989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4661_call = mod.get_global_var('func_4661')
func_4663_call = mutated_mod.get_global_var('func_4663')
call_5002 = relay.TupleGetItem(func_4661_call(), 0)
call_5003 = relay.TupleGetItem(func_4663_call(), 0)
output = call_5002
output2 = call_5003
func_5009 = relay.Function([], output)
mod['func_5009'] = func_5009
mod = relay.transform.InferType()(mod)
mutated_mod['func_5009'] = func_5009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5009_call = mutated_mod.get_global_var('func_5009')
call_5010 = func_5009_call()
output = call_5010
func_5011 = relay.Function([], output)
mutated_mod['func_5011'] = func_5011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5009_call = mod.get_global_var('func_5009')
func_5011_call = mutated_mod.get_global_var('func_5011')
call_5056 = func_5009_call()
call_5057 = func_5009_call()
var_5061 = relay.var("var_5061", dtype = "bool", shape = (4, 9, 6))#candidate|5061|(4, 9, 6)|var|bool
bop_5062 = relay.maximum(call_5056.astype('int32'), relay.reshape(var_5061.astype('int32'), relay.shape_of(call_5056))) # shape=(4, 9, 6)
bop_5065 = relay.maximum(call_5057.astype('int32'), relay.reshape(var_5061.astype('int32'), relay.shape_of(call_5057))) # shape=(4, 9, 6)
output = relay.Tuple([bop_5062,])
output2 = relay.Tuple([bop_5065,])
func_5073 = relay.Function([var_5061,], output)
mod['func_5073'] = func_5073
mod = relay.transform.InferType()(mod)
mutated_mod['func_5073'] = func_5073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5074 = relay.var("var_5074", dtype = "bool", shape = (4, 9, 6))#candidate|5074|(4, 9, 6)|var|bool
func_5073_call = mutated_mod.get_global_var('func_5073')
call_5075 = func_5073_call(var_5074)
output = call_5075
func_5076 = relay.Function([var_5074], output)
mutated_mod['func_5076'] = func_5076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5127 = relay.var("var_5127", dtype = "float32", shape = (12, 16, 10))#candidate|5127|(12, 16, 10)|var|float32
uop_5128 = relay.cosh(var_5127.astype('float32')) # shape=(12, 16, 10)
bop_5142 = relay.maximum(var_5127.astype('float32'), relay.reshape(uop_5128.astype('float32'), relay.shape_of(var_5127))) # shape=(12, 16, 10)
output = relay.Tuple([bop_5142,])
output2 = relay.Tuple([bop_5142,])
func_5147 = relay.Function([var_5127,], output)
mod['func_5147'] = func_5147
mod = relay.transform.InferType()(mod)
var_5148 = relay.var("var_5148", dtype = "float32", shape = (12, 16, 10))#candidate|5148|(12, 16, 10)|var|float32
output = func_5147(var_5148)
func_5149 = relay.Function([var_5148], output)
mutated_mod['func_5149'] = func_5149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_5153 = func_2162_call()
call_5154 = func_2162_call()
output = call_5153
output2 = call_5154
func_5156 = relay.Function([], output)
mod['func_5156'] = func_5156
mod = relay.transform.InferType()(mod)
mutated_mod['func_5156'] = func_5156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mutated_mod.get_global_var('func_5156')
call_5157 = func_5156_call()
output = call_5157
func_5158 = relay.Function([], output)
mutated_mod['func_5158'] = func_5158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2840_call = mod.get_global_var('func_2840')
func_2842_call = mutated_mod.get_global_var('func_2842')
call_5208 = relay.TupleGetItem(func_2840_call(), 0)
call_5209 = relay.TupleGetItem(func_2842_call(), 0)
output = relay.Tuple([call_5208,])
output2 = relay.Tuple([call_5209,])
func_5215 = relay.Function([], output)
mod['func_5215'] = func_5215
mod = relay.transform.InferType()(mod)
mutated_mod['func_5215'] = func_5215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mutated_mod.get_global_var('func_5215')
call_5216 = func_5215_call()
output = call_5216
func_5217 = relay.Function([], output)
mutated_mod['func_5217'] = func_5217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mod.get_global_var('func_3638')
func_3640_call = mutated_mod.get_global_var('func_3640')
call_5235 = relay.TupleGetItem(func_3638_call(), 0)
call_5236 = relay.TupleGetItem(func_3640_call(), 0)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_5243 = relay.TupleGetItem(func_3026_call(), 1)
call_5244 = relay.TupleGetItem(func_3028_call(), 1)
func_3979_call = mod.get_global_var('func_3979')
func_3983_call = mutated_mod.get_global_var('func_3983')
var_5255 = relay.var("var_5255", dtype = "float32", shape = (65, 6))#candidate|5255|(65, 6)|var|float32
call_5254 = relay.TupleGetItem(func_3979_call(relay.reshape(var_5255.astype('float32'), [5, 13, 6]), relay.reshape(var_5255.astype('float32'), [5, 13, 6]), ), 1)
call_5256 = relay.TupleGetItem(func_3983_call(relay.reshape(var_5255.astype('float32'), [5, 13, 6]), relay.reshape(var_5255.astype('float32'), [5, 13, 6]), ), 1)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_5261 = func_1845_call()
call_5262 = func_1845_call()
var_5268 = relay.var("var_5268", dtype = "float32", shape = (65, 6))#candidate|5268|(65, 6)|var|float32
bop_5269 = relay.left_shift(var_5255.astype('uint64'), relay.reshape(var_5268.astype('uint64'), relay.shape_of(var_5255))) # shape=(65, 6)
uop_5278 = relay.sinh(bop_5269.astype('float32')) # shape=(65, 6)
uop_5283 = relay.exp(uop_5278.astype('float64')) # shape=(65, 6)
output = relay.Tuple([call_5235,call_5243,call_5254,call_5261,uop_5283,])
output2 = relay.Tuple([call_5236,call_5244,call_5256,call_5262,uop_5283,])
func_5287 = relay.Function([var_5255,var_5268,], output)
mod['func_5287'] = func_5287
mod = relay.transform.InferType()(mod)
mutated_mod['func_5287'] = func_5287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5287_call = mutated_mod.get_global_var('func_5287')
var_5289 = relay.var("var_5289", dtype = "float32", shape = (65, 6))#candidate|5289|(65, 6)|var|float32
var_5290 = relay.var("var_5290", dtype = "float32", shape = (65, 6))#candidate|5290|(65, 6)|var|float32
call_5288 = func_5287_call(var_5289,var_5290,)
output = call_5288
func_5291 = relay.Function([var_5289,var_5290,], output)
mutated_mod['func_5291'] = func_5291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4697_call = mod.get_global_var('func_4697')
func_4699_call = mutated_mod.get_global_var('func_4699')
call_5319 = relay.TupleGetItem(func_4697_call(), 1)
call_5320 = relay.TupleGetItem(func_4699_call(), 1)
var_5329 = relay.var("var_5329", dtype = "float64", shape = (416,))#candidate|5329|(416,)|var|float64
bop_5330 = relay.divide(call_5319.astype('float64'), relay.reshape(var_5329.astype('float64'), relay.shape_of(call_5319))) # shape=(416,)
bop_5333 = relay.divide(call_5320.astype('float64'), relay.reshape(var_5329.astype('float64'), relay.shape_of(call_5320))) # shape=(416,)
output = bop_5330
output2 = bop_5333
func_5347 = relay.Function([var_5329,], output)
mod['func_5347'] = func_5347
mod = relay.transform.InferType()(mod)
mutated_mod['func_5347'] = func_5347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5348 = relay.var("var_5348", dtype = "float64", shape = (416,))#candidate|5348|(416,)|var|float64
func_5347_call = mutated_mod.get_global_var('func_5347')
call_5349 = func_5347_call(var_5348)
output = call_5349
func_5350 = relay.Function([var_5348], output)
mutated_mod['func_5350'] = func_5350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_5414 = relay.TupleGetItem(func_2570_call(), 0)
call_5415 = relay.TupleGetItem(func_2571_call(), 0)
output = relay.Tuple([call_5414,])
output2 = relay.Tuple([call_5415,])
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
var_5442 = relay.var("var_5442", dtype = "uint32", shape = (16, 16, 12))#candidate|5442|(16, 16, 12)|var|uint32
var_5443 = relay.var("var_5443", dtype = "uint32", shape = (16, 16, 12))#candidate|5443|(16, 16, 12)|var|uint32
bop_5444 = relay.bitwise_and(var_5442.astype('uint32'), relay.reshape(var_5443.astype('uint32'), relay.shape_of(var_5442))) # shape=(16, 16, 12)
func_4115_call = mod.get_global_var('func_4115')
func_4119_call = mutated_mod.get_global_var('func_4119')
var_5448 = relay.var("var_5448", dtype = "float64", shape = (1, 130))#candidate|5448|(1, 130)|var|float64
var_5449 = relay.var("var_5449", dtype = "bool", shape = (216,))#candidate|5449|(216,)|var|bool
call_5447 = relay.TupleGetItem(func_4115_call(relay.reshape(var_5448.astype('float64'), [130, 1]), relay.reshape(var_5449.astype('bool'), [4, 9, 6]), ), 0)
call_5450 = relay.TupleGetItem(func_4119_call(relay.reshape(var_5448.astype('float64'), [130, 1]), relay.reshape(var_5449.astype('bool'), [4, 9, 6]), ), 0)
output = relay.Tuple([bop_5444,call_5447,var_5448,var_5449,])
output2 = relay.Tuple([bop_5444,call_5450,var_5448,var_5449,])
func_5451 = relay.Function([var_5442,var_5443,var_5448,var_5449,], output)
mod['func_5451'] = func_5451
mod = relay.transform.InferType()(mod)
var_5452 = relay.var("var_5452", dtype = "uint32", shape = (16, 16, 12))#candidate|5452|(16, 16, 12)|var|uint32
var_5453 = relay.var("var_5453", dtype = "uint32", shape = (16, 16, 12))#candidate|5453|(16, 16, 12)|var|uint32
var_5454 = relay.var("var_5454", dtype = "float64", shape = (1, 130))#candidate|5454|(1, 130)|var|float64
var_5455 = relay.var("var_5455", dtype = "bool", shape = (216,))#candidate|5455|(216,)|var|bool
output = func_5451(var_5452,var_5453,var_5454,var_5455,)
func_5456 = relay.Function([var_5452,var_5453,var_5454,var_5455,], output)
mutated_mod['func_5456'] = func_5456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_5582 = relay.TupleGetItem(func_3026_call(), 0)
call_5583 = relay.TupleGetItem(func_3028_call(), 0)
func_3724_call = mod.get_global_var('func_3724')
func_3726_call = mutated_mod.get_global_var('func_3726')
const_5603 = relay.const([[-2],[8],[6],[5],[-9],[-6],[-3],[9],[4],[5],[4],[7],[-9],[-4],[10],[-7],[-8],[2],[-8],[-2],[5],[7],[4],[4],[-3],[-7],[6],[10],[1],[-8],[-1],[3],[-9],[-3],[-3],[-5],[2],[6],[7],[5],[-9],[-10],[-6],[-2],[-4],[10],[-5],[-5],[10],[-5],[-3],[-3],[2],[3],[1],[3],[10],[-7],[-6],[7],[-7],[-3],[10],[9],[8],[-4],[4],[-7],[7],[8],[-10],[8],[-6],[10],[3],[-10],[-2],[5],[3],[-3],[9],[1],[5],[10],[10],[9],[-2],[-1],[3],[-10],[7],[-7],[5],[3],[7],[8],[-5],[9],[-6],[3],[-8],[-5],[-1],[-9],[-6],[-3],[9],[3],[3],[3],[-6],[-5],[-7],[-3],[3],[9],[8],[2],[-8],[8],[-9],[10],[10],[-3],[1],[-4],[-6],[-8],[-1],[-6],[-4],[-6],[8],[-6],[10],[-4],[-2],[9],[8],[-6],[10],[6],[8],[1],[-2],[4],[3],[-2],[9],[-1],[1],[-7],[10],[6],[10],[6],[3],[7],[3],[-1],[-4],[-5],[-6],[-10],[-5],[5],[6],[9],[-10],[1],[1],[1],[9],[-5],[6],[9],[4],[1],[-1],[6],[-1],[1],[3],[-1],[-7],[2],[-2],[-1],[-2],[3],[-6],[-2],[-6],[-2],[-3],[4],[9],[1],[-7],[4],[7],[-3],[-10],[-7],[-5],[-10],[3],[-1],[2],[-8],[2],[-9],[9],[-3],[-4],[-4],[3],[-9],[-4],[-5],[9],[1],[-7],[4],[6],[6],[-6],[-8],[-7],[-3],[10],[-4],[-7],[-5],[-1],[9],[6],[-5],[2],[2],[-1],[-7],[5],[4],[-8],[3],[-4],[-10],[9],[-1],[8],[2],[2],[6],[-7],[4],[-9],[5],[-6],[-6],[-5],[4],[-7],[10],[2],[8],[-3],[-5],[-8],[-9],[-1],[2],[-3],[4],[5],[-8],[8],[-10],[6],[10],[-5],[-9],[1],[-3],[5],[5],[-6],[4],[4],[-1],[-7],[-1],[-10],[-9]], dtype = "int64")#candidate|5603|(294, 1)|const|int64
call_5602 = relay.TupleGetItem(func_3724_call(relay.reshape(const_5603.astype('int64'), [294,])), 5)
call_5604 = relay.TupleGetItem(func_3726_call(relay.reshape(const_5603.astype('int64'), [294,])), 5)
var_5606 = relay.var("var_5606", dtype = "int64", shape = (294, 11))#candidate|5606|(294, 11)|var|int64
bop_5607 = relay.logical_and(const_5603.astype('bool'), var_5606.astype('bool')) # shape=(294, 11)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_5628 = relay.TupleGetItem(func_5215_call(), 0)
call_5629 = relay.TupleGetItem(func_5217_call(), 0)
func_3630_call = mod.get_global_var('func_3630')
func_3631_call = mutated_mod.get_global_var('func_3631')
call_5634 = relay.TupleGetItem(func_3630_call(), 1)
call_5635 = relay.TupleGetItem(func_3631_call(), 1)
func_2784_call = mod.get_global_var('func_2784')
func_2786_call = mutated_mod.get_global_var('func_2786')
call_5641 = relay.TupleGetItem(func_2784_call(), 2)
call_5642 = relay.TupleGetItem(func_2786_call(), 2)
output = relay.Tuple([call_5582,call_5602,bop_5607,call_5628,call_5634,call_5641,])
output2 = relay.Tuple([call_5583,call_5604,bop_5607,call_5629,call_5635,call_5642,])
func_5643 = relay.Function([var_5606,], output)
mod['func_5643'] = func_5643
mod = relay.transform.InferType()(mod)
mutated_mod['func_5643'] = func_5643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5644 = relay.var("var_5644", dtype = "int64", shape = (294, 11))#candidate|5644|(294, 11)|var|int64
func_5643_call = mutated_mod.get_global_var('func_5643')
call_5645 = func_5643_call(var_5644)
output = call_5645
func_5646 = relay.Function([var_5644], output)
mutated_mod['func_5646'] = func_5646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4381_call = mod.get_global_var('func_4381')
func_4382_call = mutated_mod.get_global_var('func_4382')
call_5662 = func_4381_call()
call_5663 = func_4381_call()
var_5664 = relay.var("var_5664", dtype = "bool", shape = (4, 9, 6))#candidate|5664|(4, 9, 6)|var|bool
bop_5665 = relay.multiply(call_5662.astype('int64'), relay.reshape(var_5664.astype('int64'), relay.shape_of(call_5662))) # shape=(4, 9, 6)
bop_5668 = relay.multiply(call_5663.astype('int64'), relay.reshape(var_5664.astype('int64'), relay.shape_of(call_5663))) # shape=(4, 9, 6)
output = relay.Tuple([bop_5665,])
output2 = relay.Tuple([bop_5668,])
func_5679 = relay.Function([var_5664,], output)
mod['func_5679'] = func_5679
mod = relay.transform.InferType()(mod)
mutated_mod['func_5679'] = func_5679
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5680 = relay.var("var_5680", dtype = "bool", shape = (4, 9, 6))#candidate|5680|(4, 9, 6)|var|bool
func_5679_call = mutated_mod.get_global_var('func_5679')
call_5681 = func_5679_call(var_5680)
output = call_5681
func_5682 = relay.Function([var_5680], output)
mutated_mod['func_5682'] = func_5682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_5719 = func_1845_call()
call_5720 = func_1845_call()
func_2620_call = mod.get_global_var('func_2620')
func_2622_call = mutated_mod.get_global_var('func_2622')
call_5737 = func_2620_call()
call_5738 = func_2620_call()
uop_5742 = relay.log(call_5737.astype('float64')) # shape=(4, 9, 6)
uop_5744 = relay.log(call_5738.astype('float64')) # shape=(4, 9, 6)
func_4115_call = mod.get_global_var('func_4115')
func_4119_call = mutated_mod.get_global_var('func_4119')
const_5760 = relay.const([9.243879,-5.970174,-7.994682,0.636041,2.822967,-6.878993,-4.628777,-4.251884,8.378500,1.246420,2.827446,6.965891,6.582943,-6.168927,-8.303545,-7.408019,2.754847,-6.193259,-4.739547,-8.991305,-3.040412,2.116098,0.031764,-0.747031,-8.741269,3.297511,4.415221,-8.429156,0.924239,-6.330647,-9.424930,8.586621,6.915039,2.511300,7.078611,7.623436,-0.588390,-0.637613,2.412710,-6.047646,-5.254340,3.298268,-7.756290,-6.780538,-9.436262,-9.991062,9.579296,-6.812161,7.942956,-1.208283,0.081135,-4.268650,0.483085,4.705500,8.411117,-2.996724,5.036889,-6.733294,7.232849,9.747452,1.913164,3.560085,4.043365,6.217239,5.423050,8.426230,4.473729,1.512433,-0.067129,2.680981,-9.416920,0.110578,0.790850,-5.514680,-7.448674,-4.301845,5.344140,4.289713,6.881882,8.794274,-8.549771,5.601983,-6.673111,-4.993286,1.225125,8.175655,-3.142884,-9.421278,-9.715901,-8.705670,-2.408100,-0.418107,-2.803365,8.369819,-1.436900,1.861505,0.276124,-2.991923,6.977541,9.097348,8.322191,-8.047176,3.817053,4.757223,8.456870,3.885133,7.804555,3.903614,6.155425,5.157423,4.164718,-4.865262,-9.767492,1.166499,-8.464878,-6.366867,3.300680,3.219331,5.567169,-3.182267,-8.563310,8.506630,7.372899,-8.770776,8.563949,-5.700340,-7.366119,2.592498,7.495712,-8.963132], dtype = "float64")#candidate|5760|(130,)|const|float64
call_5759 = relay.TupleGetItem(func_4115_call(relay.reshape(const_5760.astype('float64'), [130, 1]), relay.reshape(uop_5742.astype('bool'), [4, 9, 6]), ), 1)
call_5761 = relay.TupleGetItem(func_4119_call(relay.reshape(const_5760.astype('float64'), [130, 1]), relay.reshape(uop_5742.astype('bool'), [4, 9, 6]), ), 1)
func_3437_call = mod.get_global_var('func_3437')
func_3440_call = mutated_mod.get_global_var('func_3440')
call_5763 = relay.TupleGetItem(func_3437_call(relay.reshape(uop_5742.astype('bool'), [4, 9, 6])), 1)
call_5764 = relay.TupleGetItem(func_3440_call(relay.reshape(uop_5742.astype('bool'), [4, 9, 6])), 1)
func_1576_call = mod.get_global_var('func_1576')
func_1578_call = mutated_mod.get_global_var('func_1578')
const_5770 = relay.const([-5.481024,-9.875355,3.815217,1.691513,-5.240788,-3.539460,0.630588,3.021932,0.600078,-2.424094,-7.792739,-2.275768,-8.635488,3.329908,6.891649,-6.611137,-2.038220,-3.876838,-8.714303,5.323506,-7.229716,-8.389397,1.900712,-7.424698,7.479139,-9.951685,6.891449,-6.026210,-5.074993,9.884275,-3.953569,6.736997,-6.994021,-4.567684,3.232918,-8.639519,8.910601,1.223721,-5.897624,6.781020,0.445187,-1.584069,-7.426372,-0.644332,-0.731174,9.601158,8.104020,9.904294,-3.957075,-2.076935,-9.605991,1.642831,8.076434,-9.586841,-5.283601,6.834774,2.397355,-0.387363,-4.589416,-2.698626,6.990030,3.135395,-8.426682,-1.991916,-6.233537,-8.856775,5.363910,8.678893,-3.825510,0.776619,9.163586,-0.475367,-7.620999,7.826576,4.179726,9.930334,0.461265,0.511710,-8.930496,-2.970560,-4.808743,3.971060,-4.773116,-1.513543,-8.516709,1.444210,-2.499086,-0.258673,6.464617,2.286864,5.922788,8.895337,8.043323,-3.768845,-4.827499,9.700199,2.297995,7.187822,7.619562,-8.412102,0.634465,1.278182,-0.483499,-0.247841,9.973271,-0.419647,-2.301343,6.619956,4.174679,4.044983,-7.048475,-5.317437,3.372600,6.179051,-3.562441,-3.351572,-4.143775,4.995693,9.630587,-2.251633,-6.444837,7.498664,-1.255002,-9.348431,-9.411030,8.511251,-7.392431,-5.132612,0.060578,-2.434024,-0.327620,9.504148,5.676325,8.003915,-6.839594,0.708239,-1.378528,-5.525994,-1.120655,-0.354626,-3.969515,9.980717,-2.468848,5.173461,-3.652591,4.272751,-0.170801,1.262292,4.327217,2.527415,-7.250526,-8.557230,0.847939,9.171869,-9.597358,2.956157,7.210832,0.682376,-0.497893,-7.815769,7.686435,4.805618,-4.444099,4.754912,2.105524,-4.293051,5.607859,4.541264,7.018435,-2.207477,-0.209189,-7.777682,1.371958,4.113513,-6.402658,-4.337469,5.825814,-9.356020,-4.758507,-6.971238,-1.729144,3.330528,2.387377,-9.281910,9.203930,-6.509796,-2.672554,1.962694,5.380400,-6.901474,-3.489801,5.727364,-4.360620,-5.769407,7.090231,9.412549,8.561822,0.010225,1.762017,8.242355,8.402178,-4.260820,-9.722769,9.051800,1.429309,-7.248295,-7.801216,6.750698,4.794985,1.983287], dtype = "float64")#candidate|5770|(210,)|const|float64
call_5769 = func_1576_call(relay.reshape(const_5770.astype('float64'), [10, 3, 7]))
call_5771 = func_1576_call(relay.reshape(const_5770.astype('float64'), [10, 3, 7]))
func_2245_call = mod.get_global_var('func_2245')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_5786 = relay.var("var_5786", dtype = "float64", shape = (416,))#candidate|5786|(416,)|var|float64
call_5785 = relay.TupleGetItem(func_2245_call(relay.reshape(var_5786.astype('float64'), [13, 16, 2]), relay.reshape(uop_5742.astype('int8'), [36, 6]), ), 2)
call_5787 = relay.TupleGetItem(func_2248_call(relay.reshape(var_5786.astype('float64'), [13, 16, 2]), relay.reshape(uop_5742.astype('int8'), [36, 6]), ), 2)
func_4468_call = mod.get_global_var('func_4468')
func_4469_call = mutated_mod.get_global_var('func_4469')
call_5797 = relay.TupleGetItem(func_4468_call(), 0)
call_5798 = relay.TupleGetItem(func_4469_call(), 0)
func_50_call = mod.get_global_var('func_50')
func_52_call = mutated_mod.get_global_var('func_52')
call_5802 = relay.TupleGetItem(func_50_call(relay.reshape(const_5760.astype('float64'), [13, 10, 1])), 0)
call_5803 = relay.TupleGetItem(func_52_call(relay.reshape(const_5760.astype('float64'), [13, 10, 1])), 0)
func_2071_call = mod.get_global_var('func_2071')
func_2074_call = mutated_mod.get_global_var('func_2074')
const_5806 = relay.const([-7,5,-6,-2,4,10,6,-1,-6,8,-2,4,-7,8,-5,3,-7,-6,3,-9,-2,6,-4,-2,7,2,6,-9,-4,-4,1,3,-8,-2,-6,9,-2,5,1,-8,7,10,-5,-8,-5,10,-2,7,-9,-2,-1,-3,7,7,-5,-8,7,8,6,-3,-8,10,-5,1,-5,-10,-5,9,1,10,3,10,6,1,4,5,-6,-4,-2,-6,-10,-5,-9,7,-10,-10,6,2,8,6,-9,5,-5,-8,-8,6,-1,2,-5,10,9,8,-9,-7,-6,-2,5,-2,-8,9,-5,3,8,-3,-8,8,-4,3,9,-4,-5,7,4,10,10,-8,-8,10,-10,-1,-8,6,-7,9,8,-8,8,1,-7,-5,-4,-1,-6,10,-3,-6,2,-7,10,-5,-9,-1,10,-10,5,-3,8,3,6,2,2,4,-10,3,7,8,10,-5,-1,9,-10,-7,10,-4,3,8,2,1,3,1,1,7,9,4,-9,-8,-7,9,4,4,7,-5,3,2,10,-7,-5,2,8,-3,-1,6,-5,5,-6,9,8,4,-9,-7,-4,-8,9,-10,-10,-2,4,-8,2,-10,-10,-4,4,10,-6,10,1,8,2,7,-3,-2,6,7,5,6,8,-8,8,4,6,6,6,7,4,-9,-4,3,4,8,7,7,-6,6,2,9,-5,-5,-1,-8,-8,-9,9,2,3,-5,8,4,6,9,1,7,-5,9,-7,-10,-4,-9,4,-10,-5,-5,-6,8,-10,-1,-7,9,1,9,-4,6,9,-5], dtype = "int64")#candidate|5806|(294,)|const|int64
call_5805 = relay.TupleGetItem(func_2071_call(relay.reshape(const_5806.astype('int64'), [294,])), 0)
call_5807 = relay.TupleGetItem(func_2074_call(relay.reshape(const_5806.astype('int64'), [294,])), 0)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_5814 = func_1845_call()
call_5815 = func_1845_call()
uop_5830 = relay.acos(call_5759.astype('float64')) # shape=(130, 1)
uop_5832 = relay.acos(call_5761.astype('float64')) # shape=(130, 1)
bop_5839 = relay.floor_divide(uop_5830.astype('float64'), relay.reshape(call_5759.astype('float64'), relay.shape_of(uop_5830))) # shape=(130, 1)
bop_5842 = relay.floor_divide(uop_5832.astype('float64'), relay.reshape(call_5761.astype('float64'), relay.shape_of(uop_5832))) # shape=(130, 1)
uop_5849 = relay.cosh(uop_5830.astype('float32')) # shape=(130, 1)
uop_5851 = relay.cosh(uop_5832.astype('float32')) # shape=(130, 1)
bop_5852 = relay.divide(uop_5849.astype('float64'), const_5770.astype('float64')) # shape=(130, 210)
bop_5855 = relay.divide(uop_5851.astype('float64'), const_5770.astype('float64')) # shape=(130, 210)
output = relay.Tuple([call_5719,uop_5742,const_5760,call_5763,call_5769,call_5785,var_5786,call_5797,call_5802,call_5805,const_5806,call_5814,bop_5839,bop_5852,])
output2 = relay.Tuple([call_5720,uop_5744,const_5760,call_5764,call_5771,call_5787,var_5786,call_5798,call_5803,call_5807,const_5806,call_5815,bop_5842,bop_5855,])
func_5859 = relay.Function([var_5786,], output)
mod['func_5859'] = func_5859
mod = relay.transform.InferType()(mod)
mutated_mod['func_5859'] = func_5859
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5860 = relay.var("var_5860", dtype = "float64", shape = (416,))#candidate|5860|(416,)|var|float64
func_5859_call = mutated_mod.get_global_var('func_5859')
call_5861 = func_5859_call(var_5860)
output = call_5861
func_5862 = relay.Function([var_5860], output)
mutated_mod['func_5862'] = func_5862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_5936 = relay.TupleGetItem(func_5215_call(), 0)
call_5937 = relay.TupleGetItem(func_5217_call(), 0)
output = call_5936
output2 = call_5937
func_5940 = relay.Function([], output)
mod['func_5940'] = func_5940
mod = relay.transform.InferType()(mod)
output = func_5940()
func_5941 = relay.Function([], output)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_6002 = relay.TupleGetItem(func_3833_call(), 1)
call_6003 = relay.TupleGetItem(func_3835_call(), 1)
output = call_6002
output2 = call_6003
func_6014 = relay.Function([], output)
mod['func_6014'] = func_6014
mod = relay.transform.InferType()(mod)
mutated_mod['func_6014'] = func_6014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6014_call = mutated_mod.get_global_var('func_6014')
call_6015 = func_6014_call()
output = call_6015
func_6016 = relay.Function([], output)
mutated_mod['func_6016'] = func_6016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_6028 = func_1903_call()
call_6029 = func_1903_call()
const_6038 = relay.const([[[False,True,True,True,False,False],[False,True,True,False,False,True],[True,False,True,False,False,False],[True,True,False,True,True,True],[False,True,True,False,False,False],[True,False,True,False,True,True],[True,False,False,False,False,False],[True,True,False,False,True,True],[False,False,False,True,True,True]],[[False,False,True,False,False,True],[False,True,False,True,False,True],[False,True,True,True,True,False],[True,False,True,False,True,True],[True,True,True,True,False,True],[True,True,True,False,True,True],[True,True,True,True,False,True],[True,False,False,False,True,True],[False,True,True,False,True,False]],[[True,False,False,False,True,False],[True,False,True,False,False,False],[False,False,True,True,True,True],[False,False,False,False,True,True],[True,True,False,False,True,True],[True,False,True,True,True,True],[True,False,True,True,True,False],[True,True,False,True,False,True],[False,False,False,False,False,True]],[[False,True,False,False,True,False],[False,False,False,True,True,True],[False,True,False,False,False,True],[False,True,False,False,False,False],[True,True,False,True,True,False],[False,True,True,True,False,False],[True,False,True,True,True,False],[True,False,True,True,False,True],[False,False,True,False,False,True]]], dtype = "bool")#candidate|6038|(4, 9, 6)|const|bool
bop_6039 = relay.bitwise_or(call_6028.astype('int8'), relay.reshape(const_6038.astype('int8'), relay.shape_of(call_6028))) # shape=(4, 9, 6)
bop_6042 = relay.bitwise_or(call_6029.astype('int8'), relay.reshape(const_6038.astype('int8'), relay.shape_of(call_6029))) # shape=(4, 9, 6)
func_6014_call = mod.get_global_var('func_6014')
func_6016_call = mutated_mod.get_global_var('func_6016')
call_6044 = func_6014_call()
call_6045 = func_6014_call()
func_1534_call = mod.get_global_var('func_1534')
func_1539_call = mutated_mod.get_global_var('func_1539')
var_6059 = relay.var("var_6059", dtype = "int64", shape = (294,))#candidate|6059|(294,)|var|int64
call_6058 = relay.TupleGetItem(func_1534_call(relay.reshape(var_6059.astype('int64'), [7, 3, 14]), relay.reshape(var_6059.astype('int64'), [7, 3, 14]), relay.reshape(var_6059.astype('float32'), [7, 3, 14]), ), 2)
call_6060 = relay.TupleGetItem(func_1539_call(relay.reshape(var_6059.astype('int64'), [7, 3, 14]), relay.reshape(var_6059.astype('int64'), [7, 3, 14]), relay.reshape(var_6059.astype('float32'), [7, 3, 14]), ), 2)
func_1786_call = mod.get_global_var('func_1786')
func_1790_call = mutated_mod.get_global_var('func_1790')
var_6065 = relay.var("var_6065", dtype = "int8", shape = (100, 2))#candidate|6065|(100, 2)|var|int8
call_6064 = relay.TupleGetItem(func_1786_call(relay.reshape(var_6065.astype('int8'), [10, 2, 10]), relay.reshape(var_6065.astype('int8'), [10, 2, 10]), ), 0)
call_6066 = relay.TupleGetItem(func_1790_call(relay.reshape(var_6065.astype('int8'), [10, 2, 10]), relay.reshape(var_6065.astype('int8'), [10, 2, 10]), ), 0)
func_1576_call = mod.get_global_var('func_1576')
func_1578_call = mutated_mod.get_global_var('func_1578')
const_6077 = relay.const([[-6.129557,9.453486,8.809621,8.101924,-1.615640,4.470442],[8.715136,-2.269799,0.347364,-9.379306,-5.924188,1.810841],[-0.066964,-9.770586,5.852166,3.757271,-9.120089,3.577617],[-5.758351,5.452611,0.559692,3.871683,-5.244547,-2.767420],[9.787252,-4.043776,-4.122567,4.178110,-8.570580,-4.951156],[-9.627071,6.679558,-5.937084,-0.060815,8.673582,9.590110],[6.956703,-3.010009,2.716965,4.016812,2.609271,-9.461054],[5.102140,-1.262263,-2.801880,3.450311,-3.607925,5.762571],[5.024234,5.535966,-1.318041,0.442057,-9.376633,2.986174],[-9.969335,-8.180128,-5.387259,-2.637904,-4.754999,0.895294],[8.342541,3.600116,0.963887,-0.476147,0.471744,-9.037711],[8.866516,0.593013,8.107162,2.465541,7.698443,8.909111],[-4.029915,6.952298,-3.787795,4.428564,6.072845,-5.483300],[-0.694173,-7.487545,-7.850546,9.829939,-7.795601,3.465204],[1.850523,-5.331348,6.372384,7.266654,5.587554,-3.548705],[5.674744,9.213434,0.446350,-0.587816,-0.216843,8.220965],[2.117697,-7.194285,4.050907,2.519114,-5.787075,9.223269],[6.429141,-2.243037,0.587865,-2.421665,-0.527580,5.370431],[7.667001,1.324479,-4.689205,8.672841,8.158932,-8.178303],[0.697112,-9.084911,5.464422,2.852588,-2.856114,7.050783],[3.182675,-8.896315,3.081646,6.978942,4.231516,-1.179532],[7.437100,7.552895,-0.651590,1.003242,7.305539,6.347224],[3.220155,9.483014,-2.442046,1.405125,2.202400,-5.308937],[2.454046,3.413389,-1.345946,9.189148,2.091360,0.747574],[-8.458448,-0.602389,-0.941118,-1.909643,-9.784501,9.002594],[-7.195778,-7.484962,-6.992695,-4.140242,-6.039699,3.761938],[5.423752,-5.325861,2.016576,-2.414069,-8.576822,-7.190798],[7.688190,-0.901553,-6.905532,-2.347660,-1.508318,-1.653650],[8.986902,5.559579,6.967344,3.906169,4.759706,4.780002],[9.636792,-1.272119,-9.938284,-8.500408,0.336603,-7.919894],[-9.684616,-2.604141,8.010002,6.757129,3.971458,2.541569],[8.634463,4.537927,-0.152360,-3.771084,1.905077,-8.423659],[1.446132,4.312195,1.494338,-4.656766,-5.349387,6.708100],[-6.672143,6.370851,8.599646,-2.618926,0.567739,4.493318],[-6.585351,8.798472,-1.020973,-4.522094,-2.630551,-8.318443]], dtype = "float64")#candidate|6077|(35, 6)|const|float64
call_6076 = func_1576_call(relay.reshape(const_6077.astype('float64'), [10, 3, 7]))
call_6078 = func_1576_call(relay.reshape(const_6077.astype('float64'), [10, 3, 7]))
uop_6079 = relay.sqrt(var_6065.astype('float64')) # shape=(100, 2)
func_4063_call = mod.get_global_var('func_4063')
func_4066_call = mutated_mod.get_global_var('func_4066')
var_6108 = relay.var("var_6108", dtype = "float64", shape = (660,))#candidate|6108|(660,)|var|float64
call_6107 = func_4063_call(relay.reshape(var_6108.astype('float64'), [15, 11, 4]))
call_6109 = func_4063_call(relay.reshape(var_6108.astype('float64'), [15, 11, 4]))
func_5679_call = mod.get_global_var('func_5679')
func_5682_call = mutated_mod.get_global_var('func_5682')
call_6111 = relay.TupleGetItem(func_5679_call(relay.reshape(const_6038.astype('bool'), [4, 9, 6])), 0)
call_6112 = relay.TupleGetItem(func_5682_call(relay.reshape(const_6038.astype('bool'), [4, 9, 6])), 0)
func_2523_call = mod.get_global_var('func_2523')
func_2526_call = mutated_mod.get_global_var('func_2526')
const_6118 = relay.const([[7.674280,-3.247834,-3.994001,-3.152760],[-4.156188,-4.337130,-2.503053,-8.556109],[-2.777702,-1.004116,6.284648,-6.161932],[-9.671275,-6.710731,-1.336150,-0.870710],[5.269602,-2.352230,7.599074,-2.388350],[-8.192119,0.929876,-8.488646,8.066271],[-2.496273,-1.607155,-3.372787,0.918801],[2.063561,-3.643011,-3.445451,3.696883]], dtype = "float64")#candidate|6118|(8, 4)|const|float64
call_6117 = func_2523_call(relay.reshape(const_6118.astype('float64'), [8, 4, 1]))
call_6119 = func_2523_call(relay.reshape(const_6118.astype('float64'), [8, 4, 1]))
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_6126 = func_2162_call()
call_6127 = func_2162_call()
output = relay.Tuple([bop_6039,call_6044,call_6058,var_6059,call_6064,call_6076,const_6077,uop_6079,call_6107,var_6108,call_6111,call_6117,const_6118,call_6126,])
output2 = relay.Tuple([bop_6042,call_6045,call_6060,var_6059,call_6066,call_6078,const_6077,uop_6079,call_6109,var_6108,call_6112,call_6119,const_6118,call_6127,])
func_6135 = relay.Function([var_6059,var_6065,var_6108,], output)
mod['func_6135'] = func_6135
mod = relay.transform.InferType()(mod)
var_6136 = relay.var("var_6136", dtype = "int64", shape = (294,))#candidate|6136|(294,)|var|int64
var_6137 = relay.var("var_6137", dtype = "int8", shape = (100, 2))#candidate|6137|(100, 2)|var|int8
var_6138 = relay.var("var_6138", dtype = "float64", shape = (660,))#candidate|6138|(660,)|var|float64
output = func_6135(var_6136,var_6137,var_6138,)
func_6139 = relay.Function([var_6136,var_6137,var_6138,], output)
mutated_mod['func_6139'] = func_6139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4969_call = mod.get_global_var('func_4969')
func_4970_call = mutated_mod.get_global_var('func_4970')
call_6222 = relay.TupleGetItem(func_4969_call(), 0)
call_6223 = relay.TupleGetItem(func_4970_call(), 0)
output = call_6222
output2 = call_6223
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
func_4381_call = mod.get_global_var('func_4381')
func_4382_call = mutated_mod.get_global_var('func_4382')
call_6245 = func_4381_call()
call_6246 = func_4381_call()
output = relay.Tuple([call_6245,])
output2 = relay.Tuple([call_6246,])
func_6258 = relay.Function([], output)
mod['func_6258'] = func_6258
mod = relay.transform.InferType()(mod)
output = func_6258()
func_6259 = relay.Function([], output)
mutated_mod['func_6259'] = func_6259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_6277 = func_6224_call()
call_6278 = func_6224_call()
output = call_6277
output2 = call_6278
func_6279 = relay.Function([], output)
mod['func_6279'] = func_6279
mod = relay.transform.InferType()(mod)
output = func_6279()
func_6280 = relay.Function([], output)
mutated_mod['func_6280'] = func_6280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6279_call = mod.get_global_var('func_6279')
func_6280_call = mutated_mod.get_global_var('func_6280')
call_6323 = func_6279_call()
call_6324 = func_6279_call()
output = relay.Tuple([call_6323,])
output2 = relay.Tuple([call_6324,])
func_6325 = relay.Function([], output)
mod['func_6325'] = func_6325
mod = relay.transform.InferType()(mod)
mutated_mod['func_6325'] = func_6325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6325_call = mutated_mod.get_global_var('func_6325')
call_6326 = func_6325_call()
output = call_6326
func_6327 = relay.Function([], output)
mutated_mod['func_6327'] = func_6327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_6353 = relay.TupleGetItem(func_3026_call(), 0)
call_6354 = relay.TupleGetItem(func_3028_call(), 0)
output = call_6353
output2 = call_6354
func_6355 = relay.Function([], output)
mod['func_6355'] = func_6355
mod = relay.transform.InferType()(mod)
output = func_6355()
func_6356 = relay.Function([], output)
mutated_mod['func_6356'] = func_6356
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6404 = relay.var("var_6404", dtype = "uint16", shape = (15, 10, 3))#candidate|6404|(15, 10, 3)|var|uint16
const_6405 = relay.const([[[1,6,-4],[-9,-10,-5],[-2,-7,7],[-6,-6,-5],[-2,6,-6],[-9,2,3],[10,-9,2],[-9,6,1],[6,4,-2],[2,1,-10]],[[-4,5,6],[-2,-2,7],[6,-10,5],[-4,9,-3],[-8,-5,-3],[-5,5,3],[-8,8,-9],[-3,2,-5],[-5,10,-8],[6,-5,2]],[[-5,-7,7],[-2,6,-4],[-4,9,-2],[-4,3,2],[-6,5,9],[-1,6,-7],[-7,-7,-10],[9,-2,1],[-1,1,-9],[-5,-1,-8]],[[10,9,5],[-1,6,7],[-1,-1,3],[6,-6,-9],[-10,-2,5],[-5,9,-10],[-9,-9,1],[2,-2,-4],[4,-10,7],[-9,-2,-9]],[[-3,3,-8],[8,-4,-6],[-5,-6,3],[4,1,10],[-5,-8,2],[-5,4,4],[-1,-1,1],[1,-6,-5],[-8,-8,4],[1,-7,-8]],[[6,3,-1],[2,-1,-6],[-8,10,-5],[-5,-5,4],[-1,1,-3],[6,-2,1],[-7,-5,6],[3,-10,2],[-8,-10,7],[4,-10,5]],[[-6,5,1],[-3,-9,-7],[4,2,2],[1,8,5],[-5,3,-6],[9,1,-3],[-9,1,7],[-4,-9,-6],[10,-3,9],[6,-8,9]],[[9,-9,-1],[-3,9,10],[-5,6,5],[-6,-9,5],[-8,-4,-10],[-2,1,1],[2,-6,-9],[6,5,9],[5,-4,4],[-4,8,9]],[[-9,9,2],[5,4,-6],[8,-9,7],[-10,3,9],[-3,2,-9],[9,3,9],[8,1,5],[-6,-3,-5],[-3,5,1],[5,-4,-5]],[[-7,-2,-4],[6,-9,5],[6,7,8],[-10,-1,9],[8,7,-1],[7,-9,-6],[2,-7,9],[-4,-5,4],[7,6,-8],[3,9,8]],[[-2,-7,5],[-6,-7,9],[6,3,-6],[-7,-3,-2],[-10,-9,-3],[-8,-3,8],[2,5,8],[7,7,7],[9,8,-7],[-4,-3,5]],[[-9,5,-1],[10,-8,3],[10,9,-10],[-3,-8,-10],[1,-5,7],[2,-4,8],[9,-9,6],[2,9,-5],[6,7,-9],[3,1,4]],[[-8,3,-3],[-9,2,9],[9,-4,-3],[-9,-7,2],[-5,7,3],[-3,-10,-4],[1,5,-1],[-1,-8,-9],[4,-7,-4],[8,-8,-5]],[[-8,1,-9],[1,8,3],[-4,8,-1],[-2,-4,-7],[-10,8,-2],[8,-5,8],[-5,4,-8],[-3,-3,-2],[-1,-9,-5],[-3,-1,-2]],[[8,-1,-2],[5,-9,-3],[7,-7,10],[-5,6,-5],[-8,6,1],[-10,-10,2],[-1,1,7],[7,9,-4],[-5,-7,-3],[-2,3,2]]], dtype = "uint16")#candidate|6405|(15, 10, 3)|const|uint16
bop_6406 = relay.not_equal(var_6404.astype('bool'), relay.reshape(const_6405.astype('bool'), relay.shape_of(var_6404))) # shape=(15, 10, 3)
uop_6414 = relay.rsqrt(var_6404.astype('float32')) # shape=(15, 10, 3)
uop_6422 = relay.exp(var_6404.astype('float32')) # shape=(15, 10, 3)
func_2245_call = mod.get_global_var('func_2245')
func_2248_call = mutated_mod.get_global_var('func_2248')
const_6425 = relay.const([[-2.021117,-0.508704,7.234111,-4.535248,-7.133532,0.820741,8.059408,6.213211,5.862146,0.920403,4.334269,-1.952364,7.421323,-0.001086,0.043525,8.480049,8.914207,3.831160,-7.079705,9.942892,9.858545,1.645333,8.391848,0.139101,8.498598,-9.030361],[8.810794,-7.571969,-3.596541,-2.307557,-3.326928,-0.837773,8.810403,0.606087,8.134964,-3.662527,1.492725,6.142135,4.799456,8.080598,2.011530,8.318990,-3.300725,3.058639,-1.945440,4.365061,-3.940352,-2.928823,0.507238,2.810830,-2.092231,8.641909],[5.877408,8.819622,3.363593,7.736567,-7.730816,8.698995,-3.284840,-0.074911,-2.972808,-5.383417,9.548287,-3.568074,-7.063562,4.474260,-9.857432,-1.818344,-0.256265,-3.418587,-8.939263,-6.575503,-1.970380,-4.339386,0.206463,8.109552,-5.201540,-3.521478],[-8.324416,-0.672670,-0.459511,1.466480,5.601345,-4.173608,0.306910,5.310635,-8.744530,3.521118,-3.585985,5.283448,-1.106001,5.547507,-4.203754,-3.018021,1.407161,3.282817,-5.415974,-7.151029,-8.949867,2.165945,9.761639,-3.212983,7.310567,-2.468989],[5.533740,1.982397,-6.203381,-7.479380,-2.350177,1.063893,1.004867,1.898726,3.845915,9.542818,-7.408005,-8.382363,-8.441653,3.548691,-3.655190,2.846001,2.333054,8.733146,1.221940,2.093504,-8.259293,0.499541,4.898410,3.199727,-6.619743,5.105463],[-8.675122,-0.640663,-8.679372,-9.573839,2.851937,-0.092031,-7.093580,-3.195253,0.167034,0.590572,-6.836347,3.878040,9.202072,4.460508,-5.446701,-1.476821,-5.431430,3.906399,-7.008700,7.962488,4.805540,-2.740848,1.124384,0.247184,-1.295168,-7.926487],[-6.002110,9.377036,-7.835184,4.688027,4.358547,0.522478,2.666632,-9.710973,-3.654084,9.962806,8.151201,8.345120,1.056613,4.308631,9.791182,-1.229386,6.068543,0.244634,-0.183893,-1.171117,-2.612923,5.600042,-8.275261,3.852773,6.208584,-3.086085],[5.897536,6.348276,6.676625,-5.429663,-9.705568,-4.508042,-1.396787,-2.321281,-4.960611,-2.208894,-8.098653,-3.402734,7.121082,-9.054888,6.161745,5.069145,-2.402899,7.977921,1.328657,3.988021,-2.453701,-3.358244,9.830622,-2.432640,9.336254,9.914097],[-9.065767,3.159386,5.384152,2.197696,-8.073837,6.925972,6.538650,-3.102101,7.751470,2.216729,4.912944,-7.416622,-0.770059,3.600524,-1.207409,7.865837,-3.666454,-0.580849,-5.149693,-1.180357,9.482154,-9.374638,-8.812393,8.421998,-7.238979,-7.289346],[-4.659848,-1.822593,7.994065,7.991969,-2.583372,-1.322054,6.450594,3.245205,-7.201916,-5.987615,5.065116,3.311372,-1.936584,9.323674,4.856990,-8.936157,7.414723,-8.404985,-0.041046,-0.378349,-5.547858,-3.091738,0.112830,-9.504602,1.422657,4.768017],[3.802236,8.954227,-5.284376,-5.389275,-7.042714,9.314205,2.435658,-8.882747,3.898596,7.287918,2.777469,4.496039,3.071924,7.410446,3.722596,5.546888,6.485318,-9.294406,-5.820966,8.008537,7.755367,-5.781708,-6.229060,0.268802,1.306384,5.290145],[-2.843077,3.565283,-0.376444,-1.719244,-7.810798,-9.962055,-4.085863,9.427133,7.264590,1.746038,2.445155,-4.008403,-1.527939,-6.049440,-5.613411,5.198385,-5.174540,-6.604680,0.409675,-8.828703,-2.151266,3.251858,7.814619,9.418223,0.410912,-8.945049],[-2.395758,-5.828429,-1.287667,-3.010227,-4.568560,9.831553,2.581693,-6.877636,-1.921723,-6.617441,3.767546,-9.112371,-9.191074,-4.319527,-7.461216,-8.039641,7.490279,-3.885010,3.313028,-4.202818,-6.837923,5.867570,7.879699,-1.864221,-5.293992,-1.654836],[-4.769950,4.672708,5.010713,-8.501387,-2.812812,-0.676930,6.862175,9.556478,-0.763389,-4.967216,2.037680,-2.576117,4.801455,-2.512105,4.765699,-0.705223,2.083077,-2.210726,9.467609,4.894356,5.986424,9.198516,-4.960409,-9.547477,-1.986923,2.334372],[-4.573572,-5.131002,-9.687002,5.083614,8.973339,7.062871,4.919187,8.642032,-6.133578,-5.604463,7.700750,-8.461836,-4.746910,-2.858558,9.230373,-6.238648,3.400712,-2.775571,-7.130590,6.045326,7.878099,-0.687674,-9.097349,7.012742,-3.696771,-0.109597],[2.647075,2.425654,6.238864,-5.266751,4.785289,-8.044973,5.585712,-9.163850,2.265910,4.066898,-3.628866,1.995030,-7.460818,6.415140,6.958887,-5.764657,-5.036321,-2.280837,0.904335,6.720695,-8.312053,1.066480,-6.758243,6.981924,4.764511,-8.380106]], dtype = "float64")#candidate|6425|(16, 26)|const|float64
var_6426 = relay.var("var_6426", dtype = "int8", shape = (36, 6))#candidate|6426|(36, 6)|var|int8
call_6424 = relay.TupleGetItem(func_2245_call(relay.reshape(const_6425.astype('float64'), [13, 16, 2]), relay.reshape(var_6426.astype('int8'), [36, 6]), ), 1)
call_6427 = relay.TupleGetItem(func_2248_call(relay.reshape(const_6425.astype('float64'), [13, 16, 2]), relay.reshape(var_6426.astype('int8'), [36, 6]), ), 1)
uop_6428 = relay.atan(uop_6422.astype('float64')) # shape=(15, 10, 3)
bop_6435 = relay.maximum(uop_6428.astype('uint64'), relay.reshape(uop_6414.astype('uint64'), relay.shape_of(uop_6428))) # shape=(15, 10, 3)
func_6135_call = mod.get_global_var('func_6135')
func_6139_call = mutated_mod.get_global_var('func_6139')
var_6439 = relay.var("var_6439", dtype = "int64", shape = (294,))#candidate|6439|(294,)|var|int64
const_6440 = relay.const([[-10,2,8,1,6,-5,-10,3,7,7,8,2,-4,6,-6,3,3,-3,3,8],[5,4,8,-3,-3,3,-4,5,9,-8,-4,-2,-6,9,1,9,-1,-1,-10,1],[5,-7,1,6,1,-5,-5,-3,-4,-8,-10,-10,10,9,6,-5,4,-1,-4,-4],[-3,2,-10,6,-9,-8,3,-1,9,-3,10,7,10,10,7,10,5,-5,-9,6],[7,-7,1,-3,8,7,-4,1,-4,-7,-4,-10,-9,3,-8,-5,4,7,-10,8],[-4,5,1,1,8,8,-5,1,5,-1,5,-10,-10,6,5,9,1,9,-9,-9],[10,-8,-8,-8,-5,8,7,-2,-4,8,-2,-3,8,-7,4,-3,-5,-9,2,-8],[8,-8,5,-3,-8,-10,-7,-3,5,-1,6,-5,-7,-6,2,5,-3,7,2,-6],[-3,1,1,5,4,7,2,-10,6,7,1,10,-6,1,8,-8,-6,-1,1,-5],[1,-6,3,5,4,-7,-5,-9,3,9,-9,-2,-4,-2,-8,3,-10,-4,4,4]], dtype = "int8")#candidate|6440|(10, 20)|const|int8
const_6441 = relay.const([0.583091,-2.302269,-5.188091,2.575622,5.024856,2.539553,5.552966,2.944232,0.085610,-1.362397,4.771597,-9.074525,5.498665,-7.482452,-4.663920,-5.886457,9.782078,1.116036,7.693602,8.463212,7.754046,-3.789301,-7.149976,5.001315,-1.728260,3.629756,2.479210,9.120684,-8.894607,1.982624,0.695698,-6.943323,-8.695486,6.738391,-9.415969,9.332090,4.218812,-7.211398,1.681478,7.916844,2.351482,7.930786,-2.907802,-4.772733,-4.888155,2.347685,8.852256,-3.666381,-3.545378,-6.793231,-4.291357,-7.570223,5.739118,7.068817,-6.798593,-3.995641,-6.122596,-1.947556,0.767804,0.317116,1.645284,5.071110,-6.103216,-9.419527,5.642831,4.630915,-9.247747,2.702833,-4.970975,4.212447,4.473770,8.276497,9.674005,3.928917,-9.380586,7.876298,3.516574,-0.007027,-2.525622,-2.221741,3.014416,-7.219138,-5.971706,-7.562251,-7.589622,8.873476,8.984381,9.722035,9.656533,5.126154,7.495740,2.483877,-7.839864,-3.229157,-8.929465,-9.856152,-8.669116,-9.653521,8.705369,-8.802368,-2.367472,5.981216,-2.935993,-6.421610,2.865448,7.879766,-0.991055,-8.866329,-1.476200,-1.079302,5.794082,1.251624,6.250450,-2.650231,-3.755386,-1.332080,6.369607,-8.995423,6.158457,7.738869,4.553763,9.839050,2.176232,-1.611070,6.474696,-0.779065,9.182165,-3.578368,0.197537,8.579037,5.510367,-9.093162,-6.978387,-9.696986,-0.918101,-9.522127,-8.006215,6.724366,3.260993,-5.860207,-1.691295,-3.732928,-2.385587,-5.646574,8.041895,5.136198,-1.615073,9.395336,-2.740942,-7.828999,7.121329,-3.489415,-7.663873,5.612634,0.628614,-6.704666,4.725953,-3.179899,-4.083113,8.578627,-5.055537,-5.743903,1.448972,0.955937,-3.744258,-9.251447,6.551733,0.592262,-6.600989,2.892195,-5.815001,-2.779565,-9.126811,7.782790,6.681928,3.677344,1.656587,-4.705991,3.370376,4.431373,6.958880,-9.128329,-6.557453,6.299712,-9.459413,2.266718,-3.224858,-5.532961,-3.506613,4.089291,5.772026,9.688381,0.127696,0.172034,-1.416847,-9.594368,-3.254547,-8.633627,-9.250396,4.760305,-8.877223,-8.649032,-2.144455,-5.657481,-0.784505,1.774149,-4.408664,5.344298,-4.877240,-5.008185,1.124358,9.352178,9.371207,-0.046014,0.545848,9.927623,-3.726193,-4.603012,-9.113487,1.142494,2.526665,-2.969642,-9.149215,8.301046,-9.628278,1.186279,-4.522388,2.491061,-9.811440,0.790282,-8.798851,7.648652,-1.976763,3.164060,-9.114459,-4.584955,1.383175,8.774352,-6.558185,4.326376,2.968869,-5.358221,8.564692,6.902011,8.057421,5.535162,0.458093,9.172615,-0.752089,8.173820,8.364477,-4.892806,-1.063755,-4.121360,-7.314442,-1.467265,-0.115113,7.188605,-4.083475,9.707241,-6.112955,5.342671,-8.268937,3.811498,-2.054212,7.115788,-5.063142,-9.876873,-2.499546,6.853187,-8.474754,-8.352541,-6.947034,-0.660654,-0.601101,8.049486,-9.765165,9.945401,9.458014,-1.689170,7.439763,0.980801,7.568621,-4.633609,4.581180,2.531846,0.043948,-7.162260,6.868328,8.922493,2.785252,-6.681119,4.721448,-5.225314,3.472201,-4.514311,-7.290766,-1.867848,-3.233843,7.040016,5.936256,9.160471,-2.870333,-5.464418,8.857386,-9.883942,-1.964014,-6.687753,-8.152327,-8.923541,9.205852,-7.594833,3.070797,-0.273401,8.522297,0.969884,-5.957434,-0.970016,-2.220852,-7.710061,-5.414414,-9.561276,-6.833251,-0.638537,6.082280,-2.252427,-0.301916,0.230872,8.797474,2.562101,2.078984,2.538300,3.136618,6.941770,7.375100,6.926761,-2.177588,-7.588642,6.159080,3.700045,-6.763871,5.988257,-6.775631,-9.247445,-5.636460,-8.471829,-9.018015,8.312108,0.010425,3.411188,0.507575,-9.852363,0.589372,-9.423107,-3.736308,3.916040,1.665132,6.749023,2.635598,9.505739,3.711901,-9.055187,-9.700825,1.096119,-4.968955,-2.824185,-5.922952,0.152681,4.116726,-5.797662,3.672002,-6.140653,-5.785233,-4.237686,0.795837,-0.636106,7.061918,-9.343447,-7.795066,-5.562037,7.042705,-5.503277,4.635099,6.756512,1.783276,-8.522982,8.839767,5.193565,-1.471459,-5.213009,-6.106805,-8.634711,3.834125,7.303732,8.288710,-7.682004,-5.586373,-5.200762,-0.592181,-9.574959,1.205543,-7.469397,-0.373584,-3.314876,5.247834,-5.069125,0.888829,7.307476,-7.592136,3.852699,-5.051494,-4.959799,-5.075969,8.967846,-3.984463,3.509714,-2.386333,-2.459143,3.627160,-2.306056,2.661294,-7.133394,5.215414,0.093686,-6.265435,0.587375,-8.669514,3.207463,-8.387887,1.871610,9.160255,-6.002502,-7.665213,-0.893073,-3.446147,-0.997723,1.449182,-3.037739,3.476508,-7.562240,-0.786488,-8.250787,7.030513,-5.283792,-0.969187,-0.141730,-2.492315,-3.101538,-7.947976,-7.829120,8.233729,-5.105292,-5.911601,2.651484,9.583719,5.746204,-3.398545,-5.301544,-0.719797,5.771807,7.120239,-2.455323,4.118712,-6.597033,2.532167,-0.726959,-5.411532,3.631129,4.600993,-9.890189,1.044113,6.952761,4.683075,7.766708,-8.029161,3.448923,0.323875,4.730779,-0.652713,-1.730041,-7.645017,-7.284555,8.748439,3.499734,-4.046857,0.884269,-1.948713,3.776408,5.273246,7.598572,-1.710639,5.546500,-0.083553,-9.835385,-1.145643,-2.951112,9.114797,2.326766,-2.166991,2.208636,-4.828388,-2.517037,2.703774,3.660063,3.723831,-1.146244,7.716665,4.998926,-6.344304,-0.530223,-3.431792,-1.120620,2.723754,-6.949473,-4.649091,-8.708218,8.942863,9.945898,8.274648,9.316222,7.577766,-6.991394,6.106350,-2.001493,9.731391,-6.562854,2.012374,2.712725,6.700548,7.520393,3.869533,-6.048263,-9.616934,-8.132987,-7.208077,-7.928406,5.291616,-4.103768,-6.078267,0.574820,4.239724,3.391920,-3.450517,1.417052,3.500477,7.340899,9.780789,8.837871,-1.352177,5.676827,5.615499,-8.846856,-9.609949,6.388473,-4.073772,-8.737244,-6.662906,-6.804911,-6.672985,-1.335869,-8.768419,-3.612554,-5.749482,-3.341689,2.637253,3.507034,3.357518,-8.883356,2.708022,2.781227,-6.998940,1.482038,6.863472,1.033928,-8.814691,7.626850,8.287885,-3.098067,6.482659,-4.645775,-9.104298,8.855514,-4.463099,5.792341,2.890447,5.297402,-1.303016,6.814064,-6.609735,8.481681,-4.567473,-6.553736,-9.979731,0.681836,7.094469,0.886941,-8.476401,7.249717,-6.971731,-6.226586,6.102169,1.391771,-6.198196,-6.150410,1.893819,4.964183,-2.317097,0.994465,-3.838600,9.149408,8.809287,0.515400,4.329211,-9.401825,4.325590,-8.272181,-7.959620,-0.409597,-7.576858,7.844130,-8.387117,1.651534,-0.632629,-8.946255,-6.688670,-0.728500,-0.819726,8.271560,7.716754,6.169103,-2.052853,6.903669,7.853716,5.147690,-0.221324,6.955267,-2.906848,-3.873036,0.841645,5.709723,-3.596647,2.586756,-0.869252,-3.322505,-9.715510,-1.610126,1.000032,4.508186,-2.666833,-4.544255,-3.011011,2.577502,8.901025,6.062327,-6.193021,-8.218230,9.316119,2.305499,-7.408913,2.655592], dtype = "float64")#candidate|6441|(660,)|const|float64
call_6438 = relay.TupleGetItem(func_6135_call(relay.reshape(var_6439.astype('int64'), [294,]), relay.reshape(const_6440.astype('int8'), [100, 2]), relay.reshape(const_6441.astype('float64'), [660,]), ), 9)
call_6442 = relay.TupleGetItem(func_6139_call(relay.reshape(var_6439.astype('int64'), [294,]), relay.reshape(const_6440.astype('int8'), [100, 2]), relay.reshape(const_6441.astype('float64'), [660,]), ), 9)
func_3102_call = mod.get_global_var('func_3102')
func_3104_call = mutated_mod.get_global_var('func_3104')
call_6449 = relay.TupleGetItem(func_3102_call(), 0)
call_6450 = relay.TupleGetItem(func_3104_call(), 0)
func_3592_call = mod.get_global_var('func_3592')
func_3596_call = mutated_mod.get_global_var('func_3596')
var_6452 = relay.var("var_6452", dtype = "float32", shape = (2, 48))#candidate|6452|(2, 48)|var|float32
call_6451 = relay.TupleGetItem(func_3592_call(relay.reshape(const_6425.astype('float64'), [416,]), relay.reshape(var_6452.astype('float32'), [96,]), ), 1)
call_6453 = relay.TupleGetItem(func_3596_call(relay.reshape(const_6425.astype('float64'), [416,]), relay.reshape(var_6452.astype('float32'), [96,]), ), 1)
output = relay.Tuple([bop_6406,call_6424,const_6425,var_6426,bop_6435,call_6438,var_6439,const_6440,const_6441,call_6449,call_6451,var_6452,])
output2 = relay.Tuple([bop_6406,call_6427,const_6425,var_6426,bop_6435,call_6442,var_6439,const_6440,const_6441,call_6450,call_6453,var_6452,])
func_6454 = relay.Function([var_6404,var_6426,var_6439,var_6452,], output)
mod['func_6454'] = func_6454
mod = relay.transform.InferType()(mod)
var_6455 = relay.var("var_6455", dtype = "uint16", shape = (15, 10, 3))#candidate|6455|(15, 10, 3)|var|uint16
var_6456 = relay.var("var_6456", dtype = "int8", shape = (36, 6))#candidate|6456|(36, 6)|var|int8
var_6457 = relay.var("var_6457", dtype = "int64", shape = (294,))#candidate|6457|(294,)|var|int64
var_6458 = relay.var("var_6458", dtype = "float32", shape = (2, 48))#candidate|6458|(2, 48)|var|float32
output = func_6454(var_6455,var_6456,var_6457,var_6458,)
func_6459 = relay.Function([var_6455,var_6456,var_6457,var_6458,], output)
mutated_mod['func_6459'] = func_6459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_6515 = func_4139_call()
call_6516 = func_4139_call()
output = call_6515
output2 = call_6516
func_6517 = relay.Function([], output)
mod['func_6517'] = func_6517
mod = relay.transform.InferType()(mod)
output = func_6517()
func_6518 = relay.Function([], output)
mutated_mod['func_6518'] = func_6518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4381_call = mod.get_global_var('func_4381')
func_4382_call = mutated_mod.get_global_var('func_4382')
call_6537 = func_4381_call()
call_6538 = func_4381_call()
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_6560 = relay.TupleGetItem(func_2027_call(), 0)
call_6561 = relay.TupleGetItem(func_2029_call(), 0)
func_4063_call = mod.get_global_var('func_4063')
func_4066_call = mutated_mod.get_global_var('func_4066')
const_6569 = relay.const([-9.460213,-0.316941,-2.942982,2.101983,-2.137020,-3.475445,-1.614246,-8.020412,-5.977599,-1.444179,5.545965,-4.534015,-8.872634,1.686195,4.021236,0.844557,-0.760077,-1.156388,-4.233702,4.972127,7.461290,5.803779,0.377085,8.397784,7.847258,-8.429975,4.923810,-5.793083,2.286558,3.093886,8.404563,-4.579061,5.543361,-2.566157,-2.623927,-4.349295,-7.543073,4.783474,6.403396,6.369442,-4.320769,-3.729266,7.751141,6.839688,-2.608087,1.678760,2.713151,4.766952,-3.712426,1.266872,0.310924,3.149945,8.481875,6.441534,5.806713,7.765928,4.758281,-2.253774,7.790251,3.527035,-2.709790,3.215560,-8.960186,-9.190916,-3.986840,-7.942924,-4.790212,6.262538,-2.271162,-3.734033,-5.070986,-2.384237,6.863970,-1.392536,-6.512857,-8.393801,-0.110108,1.206853,-3.467471,-5.634765,8.935889,-3.029952,-8.779736,1.357602,1.038278,-0.554838,2.771179,0.832004,0.538656,5.383555,6.202513,8.353790,3.776848,-3.753291,-4.981338,4.416995,5.859510,2.914615,8.958940,3.478807,7.968574,-9.438295,-5.697715,7.027157,1.340971,8.299591,8.131203,1.420951,5.089451,-9.741433,-2.946018,2.908955,-3.606252,1.934808,3.316600,-5.108452,-9.990079,-8.952007,-0.223301,3.912194,-7.928841,-7.733556,7.980247,1.607262,4.776182,-5.783429,6.742782,-4.651366,0.730582,1.061186,-4.023994,6.581095,8.411817,1.802785,2.171110,2.649100,1.003991,7.543809,5.804656,-4.586733,9.617023,-2.461756,-6.107919,-2.426068,-7.095564,3.960982,4.850307,-1.543851,-1.971609,-1.649122,-0.437888,1.347953,9.002374,-8.731551,2.608502,0.562728,4.014499,3.115134,-7.962384,2.898948,-3.454130,3.388081,2.513285,-8.179433,1.703527,-1.022804,-5.034544,-5.474528,-8.051154,1.250164,7.081519,-0.814605,-7.746345,-1.186209,1.747016,-2.660386,-1.437328,4.133020,5.881293,1.824418,-5.712520,-4.178246,-7.038655,-3.392717,3.657653,-3.185936,9.034567,8.966348,6.393039,-2.866478,-0.104909,-4.487912,3.256805,-2.414028,1.877872,1.076002,2.088072,-4.978396,-0.008055,3.963048,-4.518338,-1.848576,-0.440426,-8.908779,-2.144247,7.122282,6.809032,6.718977,0.929918,6.782929,-0.510824,9.049394,-2.471180,9.150833,-9.854104,-5.072454,-3.460408,-5.818211,-8.351743,-6.828020,-6.114550,2.397086,7.586068,-3.188636,8.941149,0.710458,-1.722165,2.922312,4.129720,-7.697545,8.480880,-1.176552,9.740695,1.048511,3.860969,-0.667971,0.333883,5.452312,1.992238,7.153370,9.015759,-4.389837,0.256608,-9.703236,-5.250204,0.008824,6.946340,2.278484,-0.127570,7.743572,1.253085,5.009374,1.047084,4.463232,-2.927679,1.799386,-6.342281,-6.731175,-0.009390,-4.915827,9.339941,-9.304941,3.571397,1.187503,-8.162286,-8.351212,1.080604,-2.648744,-8.465296,1.625942,7.620496,4.875587,-2.211103,7.032461,-0.432597,3.315678,2.068769,3.581901,5.826232,5.443676,8.824437,5.338537,0.575438,5.320433,-9.524089,8.260493,-8.427193,5.080921,-2.285932,5.958785,-5.247221,-0.955342,-7.684886,-2.647017,-3.152611,-0.821349,9.768561,-4.618309,6.533668,7.197270,-7.609976,8.448107,5.821585,9.578910,-0.306636,-1.769271,5.384621,-5.120592,-3.398812,-9.861538,-6.933494,-8.167491,-2.405462,8.216649,9.585060,4.374926,7.205116,-4.295762,4.167808,-5.156353,-9.446954,-0.982079,9.846201,4.714470,-7.187519,-7.960237,-7.665944,-6.251632,-2.087399,3.172614,-4.616939,2.777593,3.572309,-3.040802,-3.907219,-4.655597,-7.752202,-0.468478,-2.168384,9.860086,7.584249,2.520935,7.114309,5.065364,8.908797,8.506031,8.583875,2.339040,-9.759142,-6.256126,-2.804579,8.220582,4.748199,-1.113789,0.322020,-5.122484,-6.653362,3.762499,-5.506240,3.196153,0.959055,9.036344,6.757100,7.453642,5.009718,-3.188917,6.835052,-1.695846,-0.146114,-1.098458,-2.764971,-2.632765,-4.950174,-4.573414,-1.797982,9.526469,-2.599405,9.523071,2.379256,6.779166,-9.397965,4.280678,1.197095,-9.192233,-0.742847,-7.327674,-7.611984,3.064827,-9.999868,2.182838,2.050553,-0.302772,3.669204,-3.616590,-0.907104,7.660303,0.788917,-0.893210,-9.462046,-0.391708,9.885267,-1.669250,-4.940521,6.339640,2.880667,1.366354,4.406489,5.440082,1.079098,9.833662,7.657928,-1.614720,5.875259,-7.634964,-7.091119,0.930698,1.426529,0.110264,6.123532,-6.219158,7.509800,-8.844045,4.898070,9.960936,2.728426,-8.323712,-2.551071,2.564625,-2.138665,2.044967,0.861491,-7.697929,-8.987249,-6.298170,-6.816892,0.303458,-2.263279,-1.453014,2.102845,7.486160,0.131808,8.166667,-4.156546,8.425275,-4.974372,2.102991,0.651827,-8.050473,3.583517,-6.911719,0.816514,9.147841,0.951405,1.305429,-6.890083,1.796795,1.787640,8.373857,4.238428,-9.823759,2.966846,2.754330,5.340473,2.023328,-2.719334,0.598161,1.300472,-3.947130,-0.711153,8.691149,-8.350556,-6.110298,5.861461,7.005157,2.662819,6.419845,-7.456753,0.882910,-6.834625,-9.377115,-6.401416,4.769952,2.556638,-1.612062,4.518540,-2.717221,-5.719331,1.157554,-1.206104,4.219763,-3.761752,-7.629215,6.015233,7.393680,-1.885223,0.639383,7.568165,-4.202545,-4.130918,-1.083159,-2.260607,6.365868,-2.749379,7.487395,0.689538,-1.553035,3.462909,-6.288625,-2.027276,-2.842316,-2.506795,-7.468985,-0.461663,-1.775632,3.320902,9.813339,9.829213,7.658601,5.708481,-9.714219,0.339635,4.882437,3.397692,2.054753,0.996341,3.535581,3.027002,8.701466,-7.079302,-1.523535,-7.177472,-7.645484,-6.582849,2.601857,-9.992780,0.846511,-9.557037,-9.893578,-3.040558,-9.728885,4.669906,8.817371,3.422439,6.413794,-5.400994,1.102076,8.839073,-4.979098,3.321456,0.861355,3.028101,8.678439,2.948886,-8.193833,-3.041331,4.228218,-1.936887,-4.167821,9.284331,8.656251,-9.135060,4.492820,-8.908214,6.715974,3.772785,0.747168,3.166525,1.463308,-3.308695,0.518810,-1.027156,3.624604,6.735943,-2.721738,8.130602,5.758299,-4.872574,0.403689,-7.602398,7.621552,8.641131,1.626891,3.242467,-0.606184,-6.348041,-7.485329,-4.194933,8.712698,-2.949460,6.008374,4.184567,7.080724,7.650155,8.731336,7.660648,8.520840,1.437575,-9.121700,4.719380,4.928510,-9.040589,-3.609530,9.558507,-0.918717,5.336044,9.206907,-2.209409,3.121739,9.925491,-0.506919,7.311583,8.600934,-8.103759,4.989738,-3.759856,3.532044,7.782993,-1.809899,7.347622,-3.248939,-5.855203,1.290821,-4.301635,-4.433066,3.395292,-0.241685,-1.657280,-6.408851,4.779930,9.314030,-3.213676,-2.140176,-0.661110,-3.021042,-2.637882,5.569730,-4.336090,7.384951,5.035353,-8.587887,-8.925599,7.201445,-5.208704,6.091496,5.009315,-1.402197,7.692745,4.784056,0.935078,1.447914,-9.576388,-9.692728,-0.815538,6.157829,5.053483,-5.835698,9.458794,-0.138623,3.213474,6.206905], dtype = "float64")#candidate|6569|(660,)|const|float64
call_6568 = func_4063_call(relay.reshape(const_6569.astype('float64'), [15, 11, 4]))
call_6570 = func_4063_call(relay.reshape(const_6569.astype('float64'), [15, 11, 4]))
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_6576 = relay.TupleGetItem(func_1728_call(), 1)
call_6577 = relay.TupleGetItem(func_1730_call(), 1)
func_1885_call = mod.get_global_var('func_1885')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_6579 = func_1885_call(relay.reshape(call_6537.astype('float32'), [3, 12, 6]))
call_6580 = func_1885_call(relay.reshape(call_6537.astype('float32'), [3, 12, 6]))
func_4884_call = mod.get_global_var('func_4884')
func_4887_call = mutated_mod.get_global_var('func_4887')
var_6586 = relay.var("var_6586", dtype = "float64", shape = (130,))#candidate|6586|(130,)|var|float64
call_6585 = relay.TupleGetItem(func_4884_call(relay.reshape(var_6586.astype('float64'), [130,])), 3)
call_6587 = relay.TupleGetItem(func_4887_call(relay.reshape(var_6586.astype('float64'), [130,])), 3)
bop_6593 = relay.equal(call_6568.astype('bool'), relay.reshape(const_6569.astype('bool'), relay.shape_of(call_6568))) # shape=(15, 11, 4)
bop_6596 = relay.equal(call_6570.astype('bool'), relay.reshape(const_6569.astype('bool'), relay.shape_of(call_6570))) # shape=(15, 11, 4)
func_5679_call = mod.get_global_var('func_5679')
func_5682_call = mutated_mod.get_global_var('func_5682')
call_6603 = relay.TupleGetItem(func_5679_call(relay.reshape(call_6579.astype('bool'), [4, 9, 6])), 0)
call_6604 = relay.TupleGetItem(func_5682_call(relay.reshape(call_6579.astype('bool'), [4, 9, 6])), 0)
output = relay.Tuple([call_6537,call_6560,call_6576,call_6579,call_6585,var_6586,bop_6593,call_6603,])
output2 = relay.Tuple([call_6538,call_6561,call_6577,call_6580,call_6587,var_6586,bop_6596,call_6604,])
func_6605 = relay.Function([var_6586,], output)
mod['func_6605'] = func_6605
mod = relay.transform.InferType()(mod)
mutated_mod['func_6605'] = func_6605
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6606 = relay.var("var_6606", dtype = "float64", shape = (130,))#candidate|6606|(130,)|var|float64
func_6605_call = mutated_mod.get_global_var('func_6605')
call_6607 = func_6605_call(var_6606)
output = call_6607
func_6608 = relay.Function([var_6606], output)
mutated_mod['func_6608'] = func_6608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_6638 = relay.TupleGetItem(func_3833_call(), 1)
call_6639 = relay.TupleGetItem(func_3835_call(), 1)
func_6454_call = mod.get_global_var('func_6454')
func_6459_call = mutated_mod.get_global_var('func_6459')
var_6655 = relay.var("var_6655", dtype = "uint16", shape = (10, 45))#candidate|6655|(10, 45)|var|uint16
const_6656 = relay.const([6,5,3,4,-1,-8,1,-1,8,-2,9,-3,-6,9,6,5,2,-7,8,-3,-4,5,10,10,1,2,-2,5,6,2,-4,2,-8,4,-10,-4,-7,-2,5,6,-6,6,-3,-7,-4,1,-5,7,3,7,10,10,2,-6,-3,-3,-1,8,1,-5,2,7,10,-1,5,8,1,3,-9,-8,-1,3,1,6,-5,-7,6,6,-7,-10,-5,10,-6,9,1,-8,-10,2,10,-3,8,4,5,-1,5,9,-10,5,-1,1,-4,2,-2,5,-4,-9,-10,8,10,-10,-9,-6,7,4,8,7,8,5,-6,2,-1,-2,-1,-8,8,-8,8,-7,-7,-10,8,-4,9,-6,10,-4,-6,-1,9,-2,7,5,5,-10,-2,-5,10,-9,-9,-5,-1,-1,9,8,1,-4,-9,6,10,-6,8,7,1,10,-10,-10,-6,-2,4,3,-9,6,8,3,1,2,-9,9,6,-1,-6,9,-3,-9,8,-4,8,6,3,-4,9,4,-7,-9,4,-9,-2,-4,-7,3,4,-4,-9,-8,10,-9,-8,-6,-7,9,-4,4,9,2,-3,-3], dtype = "int8")#candidate|6656|(216,)|const|int8
var_6657 = relay.var("var_6657", dtype = "int64", shape = (294,))#candidate|6657|(294,)|var|int64
const_6658 = relay.const([-9.994678,6.062687,-6.281009,3.498953,6.514836,-5.862328,-4.142298,-9.032831,2.225775,5.029068,2.106795,0.828218,-3.586278,-7.666091,4.965527,7.219475,7.279729,-6.884988,9.732041,6.514062,7.625377,-1.027096,2.897262,5.082970,9.308049,-0.777188,-8.055914,4.467097,-0.620642,3.312113,6.758897,4.634574,1.880825,-8.555639,1.247230,3.639075,5.423511,-7.411447,0.401577,9.476908,-3.047381,9.546852,9.080512,5.114029,-4.586934,-1.318559,7.615380,-8.706950,7.359820,1.824253,-3.999508,4.042814,-8.866544,6.042423,1.568075,-9.093854,-9.381818,4.321133,-9.027795,8.233509,8.938305,-0.262033,5.580050,4.807025,5.693087,5.112335,2.334061,5.513704,-9.021212,5.747801,9.142614,0.443046,-0.259638,-1.186258,0.191612,4.173696,8.815746,4.880988,7.580355,0.089235,0.238808,-1.178867,-8.345950,-8.614849,-2.934587,-4.907937,0.964179,9.764496,-1.030409,3.504352,3.320211,-9.856633,-8.499084,6.527756,-9.254610,4.464770], dtype = "float32")#candidate|6658|(96,)|const|float32
call_6654 = relay.TupleGetItem(func_6454_call(relay.reshape(var_6655.astype('uint16'), [15, 10, 3]), relay.reshape(const_6656.astype('int8'), [36, 6]), relay.reshape(var_6657.astype('int64'), [294,]), relay.reshape(const_6658.astype('float32'), [2, 48]), ), 5)
call_6659 = relay.TupleGetItem(func_6459_call(relay.reshape(var_6655.astype('uint16'), [15, 10, 3]), relay.reshape(const_6656.astype('int8'), [36, 6]), relay.reshape(var_6657.astype('int64'), [294,]), relay.reshape(const_6658.astype('float32'), [2, 48]), ), 5)
output = relay.Tuple([call_6638,call_6654,var_6655,const_6656,var_6657,const_6658,])
output2 = relay.Tuple([call_6639,call_6659,var_6655,const_6656,var_6657,const_6658,])
func_6661 = relay.Function([var_6655,var_6657,], output)
mod['func_6661'] = func_6661
mod = relay.transform.InferType()(mod)
var_6662 = relay.var("var_6662", dtype = "uint16", shape = (10, 45))#candidate|6662|(10, 45)|var|uint16
var_6663 = relay.var("var_6663", dtype = "int64", shape = (294,))#candidate|6663|(294,)|var|int64
output = func_6661(var_6662,var_6663,)
func_6664 = relay.Function([var_6662,var_6663,], output)
mutated_mod['func_6664'] = func_6664
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6670 = relay.var("var_6670", dtype = "float32", shape = (2, 10, 9))#candidate|6670|(2, 10, 9)|var|float32
uop_6671 = relay.asin(var_6670.astype('float32')) # shape=(2, 10, 9)
output = uop_6671
output2 = uop_6671
func_6681 = relay.Function([var_6670,], output)
mod['func_6681'] = func_6681
mod = relay.transform.InferType()(mod)
var_6682 = relay.var("var_6682", dtype = "float32", shape = (2, 10, 9))#candidate|6682|(2, 10, 9)|var|float32
output = func_6681(var_6682)
func_6683 = relay.Function([var_6682], output)
mutated_mod['func_6683'] = func_6683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_6714 = relay.TupleGetItem(func_5418_call(), 0)
call_6715 = relay.TupleGetItem(func_5420_call(), 0)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_6716 = relay.TupleGetItem(func_5418_call(), 0)
call_6717 = relay.TupleGetItem(func_5420_call(), 0)
func_1956_call = mod.get_global_var('func_1956')
func_1958_call = mutated_mod.get_global_var('func_1958')
const_6761 = relay.const([[-0.620885,3.288549,7.224595,-7.429617,-7.986356,-1.931560,9.798240,-5.356322,-9.277236,-6.890455],[-5.261708,-3.865398,-3.358643,4.845018,6.195153,-3.603967,2.589578,-4.434249,-4.231338,-2.303492],[-1.568002,9.934693,1.798709,-5.073639,-0.326654,-5.922134,-9.688530,6.340539,-5.396155,-6.351221],[-2.112329,5.638318,-5.737920,0.873468,7.630679,5.213915,-7.480194,4.429667,-3.759213,2.734583],[-8.453315,-8.273787,8.996168,2.195859,-8.266068,5.581766,-4.705348,-9.592889,-4.471133,-3.953191],[-3.990570,9.069452,-3.386235,-9.469140,-7.676196,5.433710,9.921747,-3.068490,-9.973434,-4.539480],[4.348520,0.539791,-0.635553,-1.255788,5.521258,-4.237941,6.557197,-7.814723,7.765858,-8.636951],[7.764773,-6.032980,6.839018,7.268249,6.367425,-2.235924,5.046736,-8.766042,-7.252423,-9.753850],[5.568633,0.266894,-8.938888,4.066596,-8.667279,7.034454,5.951566,-8.758371,-9.062955,-9.523047],[4.288855,-5.077557,5.799711,-1.052593,-0.097505,6.773099,-5.560147,-4.062530,6.224898,-2.061165],[7.504544,1.845657,4.723422,-9.223516,7.564404,3.008168,4.839212,0.928852,6.283301,-9.950854],[-2.036595,0.940843,-5.801476,4.161960,3.743062,8.141962,0.371060,-3.621781,-7.389964,4.194301],[1.065932,-8.229642,-9.281861,7.599308,-0.263894,7.230185,-1.720674,9.585913,-4.463955,-8.426133]], dtype = "float64")#candidate|6761|(13, 10)|const|float64
call_6760 = relay.TupleGetItem(func_1956_call(relay.reshape(const_6761.astype('float64'), [130, 1])), 2)
call_6762 = relay.TupleGetItem(func_1958_call(relay.reshape(const_6761.astype('float64'), [130, 1])), 2)
output = relay.Tuple([call_6714,call_6716,call_6760,const_6761,])
output2 = relay.Tuple([call_6715,call_6717,call_6762,const_6761,])
func_6769 = relay.Function([], output)
mod['func_6769'] = func_6769
mod = relay.transform.InferType()(mod)
mutated_mod['func_6769'] = func_6769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mutated_mod.get_global_var('func_6769')
call_6770 = func_6769_call()
output = call_6770
func_6771 = relay.Function([], output)
mutated_mod['func_6771'] = func_6771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2646_call = mod.get_global_var('func_2646')
func_2647_call = mutated_mod.get_global_var('func_2647')
call_6839 = func_2646_call()
call_6840 = func_2646_call()
output = relay.Tuple([call_6839,])
output2 = relay.Tuple([call_6840,])
func_6846 = relay.Function([], output)
mod['func_6846'] = func_6846
mod = relay.transform.InferType()(mod)
mutated_mod['func_6846'] = func_6846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6846_call = mutated_mod.get_global_var('func_6846')
call_6847 = func_6846_call()
output = call_6847
func_6848 = relay.Function([], output)
mutated_mod['func_6848'] = func_6848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4440_call = mod.get_global_var('func_4440')
func_4442_call = mutated_mod.get_global_var('func_4442')
call_6849 = func_4440_call()
call_6850 = func_4440_call()
output = call_6849
output2 = call_6850
func_6852 = relay.Function([], output)
mod['func_6852'] = func_6852
mod = relay.transform.InferType()(mod)
output = func_6852()
func_6853 = relay.Function([], output)
mutated_mod['func_6853'] = func_6853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mod.get_global_var('func_4641')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_6928 = relay.TupleGetItem(func_4641_call(), 2)
call_6929 = relay.TupleGetItem(func_4642_call(), 2)
func_4641_call = mod.get_global_var('func_4641')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_6935 = relay.TupleGetItem(func_4641_call(), 0)
call_6936 = relay.TupleGetItem(func_4642_call(), 0)
func_3724_call = mod.get_global_var('func_3724')
func_3726_call = mutated_mod.get_global_var('func_3726')
call_6950 = relay.TupleGetItem(func_3724_call(relay.reshape(call_6928.astype('int64'), [294,])), 4)
call_6951 = relay.TupleGetItem(func_3726_call(relay.reshape(call_6928.astype('int64'), [294,])), 4)
func_1885_call = mod.get_global_var('func_1885')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_6954 = func_1885_call(relay.reshape(call_6935.astype('float32'), [3, 12, 6]))
call_6955 = func_1885_call(relay.reshape(call_6935.astype('float32'), [3, 12, 6]))
func_50_call = mod.get_global_var('func_50')
func_52_call = mutated_mod.get_global_var('func_52')
const_6957 = relay.const([[6.174669,-0.350657,-5.219041,-5.061215,0.768340,-4.957603,-6.647083,-1.558212,-0.464949,-6.387114],[-8.950814,9.390718,1.640123,-4.287842,-7.761724,-4.092122,-1.922506,-9.207994,-5.899981,-7.474757],[8.525909,5.359100,-8.612922,2.484089,-7.352335,3.399956,3.287364,5.167019,-3.126172,-4.845608],[4.097408,-7.961815,1.972662,-2.667815,-2.882308,9.902384,-2.747364,4.087994,-0.846316,8.436644],[-2.326311,1.935080,4.657872,-2.258313,-6.950755,-6.053022,5.002631,-8.271231,3.379298,7.715590],[5.348973,7.084488,7.591691,-7.352814,4.491705,6.066465,-0.158304,5.315858,9.824172,3.427830],[-7.202734,0.088700,9.631003,-6.369597,1.773753,-1.378418,-2.104838,-3.989736,-1.372948,-8.951600],[-7.775769,9.916452,-5.449537,-4.697096,-9.611061,-4.995777,-2.754810,4.892098,9.593385,-0.345697],[5.334373,7.986479,6.716647,9.210167,-5.367777,3.307224,7.736047,1.996165,-8.104016,-4.956102],[-7.428045,9.396158,-1.604610,-8.734808,6.483131,-1.699028,9.706944,-3.694948,7.345483,-8.715445],[6.924140,-9.617645,-6.207817,5.415849,-3.393145,3.490373,-6.341839,0.841524,2.388404,-6.155432],[-8.995518,4.452129,-8.179845,-5.889956,-8.298548,0.428085,2.096705,-7.877136,2.951124,-6.384115],[6.123920,-8.308488,-0.551925,5.819422,9.966500,-1.330522,-7.026575,2.242071,-4.493676,6.725943]], dtype = "float64")#candidate|6957|(13, 10)|const|float64
call_6956 = relay.TupleGetItem(func_50_call(relay.reshape(const_6957.astype('float64'), [13, 10, 1])), 0)
call_6958 = relay.TupleGetItem(func_52_call(relay.reshape(const_6957.astype('float64'), [13, 10, 1])), 0)
output = relay.Tuple([call_6928,call_6935,call_6950,call_6954,call_6956,const_6957,])
output2 = relay.Tuple([call_6929,call_6936,call_6951,call_6955,call_6958,const_6957,])
func_6967 = relay.Function([], output)
mod['func_6967'] = func_6967
mod = relay.transform.InferType()(mod)
mutated_mod['func_6967'] = func_6967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6967_call = mutated_mod.get_global_var('func_6967')
call_6968 = func_6967_call()
output = call_6968
func_6969 = relay.Function([], output)
mutated_mod['func_6969'] = func_6969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_7017 = func_3046_call()
call_7018 = func_3046_call()
output = call_7017
output2 = call_7018
func_7035 = relay.Function([], output)
mod['func_7035'] = func_7035
mod = relay.transform.InferType()(mod)
output = func_7035()
func_7036 = relay.Function([], output)
mutated_mod['func_7036'] = func_7036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4468_call = mod.get_global_var('func_4468')
func_4469_call = mutated_mod.get_global_var('func_4469')
call_7064 = relay.TupleGetItem(func_4468_call(), 0)
call_7065 = relay.TupleGetItem(func_4469_call(), 0)
output = call_7064
output2 = call_7065
func_7071 = relay.Function([], output)
mod['func_7071'] = func_7071
mod = relay.transform.InferType()(mod)
output = func_7071()
func_7072 = relay.Function([], output)
mutated_mod['func_7072'] = func_7072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6279_call = mod.get_global_var('func_6279')
func_6280_call = mutated_mod.get_global_var('func_6280')
call_7108 = func_6279_call()
call_7109 = func_6279_call()
func_2338_call = mod.get_global_var('func_2338')
func_2342_call = mutated_mod.get_global_var('func_2342')
const_7116 = relay.const([-2,-2,4,4,-3,-10,-5,7,-2,3,4,-5,-2,5,3,-1,-7,-9,4,-2,-2,7,-7,9,3,-7,9,-5,4,-6,4,-2,-2,-3,6,-5,-10,-6,-7,6,-8,-8,-2,-7,5,-5,-3,-1,10,1,-1,-6,7,10,8,5,-9,-2,5,1,-5,10,-3,-10,5,3,-6,-9,-1,-8,-6,-5,-7,8,-8,-4,5,-10,-3,3,2,5,5,2,4,-6,-4,-5,-10,4,2,-9,-10,-7,-9,-10,-6,-10,9,-10,-3,-3,-7,-9,3,-5,9,-4,-4,1,-1,4,-6,-10,-6,9,-7,8,1,3,1,1,-1,-1,5,-8,-3,-4,9,-5,4,-6,-4,-7,4,-1,7,6,-6,-4,-9,5,-7,2,-3,-10,-8,-10,-3,-9,6,-3,-3,-10,8,-2,-6,-10,8,-6,-6,7,-5,10,3,-4,-1,-9,-5,-5,-3,-9,-4,2,10,2,-6,-4,8,-8,3,-10,-6,1,10,-4,5,-3,-4,-2,5,-4,4,4,2,-3,-4,1,3,-1,10,-7,-3,-5,-5,3,8,3,-5,-4,-6,2,-9,10,-7,-5,8,-1,2,8,-2,7,10,1,-6,-2,3,2,9,6,-5,-2,-2,-6,2,2,-6,-3,1,-2,1,9,2,-6,5,8,2,3,-6,10,2,9,3,6,7,10,4,2,3,8,1,-8,-7,-10,-1,-8,-2,-2,-8,-10,-6,3,-10,-7,-4,-2,10,-1,-2,-9,-1,5,3,-8,-8,8,-9,-6,-7,-3,-10,9,5,-7], dtype = "int64")#candidate|7116|(294,)|const|int64
var_7117 = relay.var("var_7117", dtype = "float64", shape = (130,))#candidate|7117|(130,)|var|float64
call_7115 = relay.TupleGetItem(func_2338_call(relay.reshape(const_7116.astype('int64'), [294,]), relay.reshape(var_7117.astype('float64'), [130,]), ), 1)
call_7118 = relay.TupleGetItem(func_2342_call(relay.reshape(const_7116.astype('int64'), [294,]), relay.reshape(var_7117.astype('float64'), [130,]), ), 1)
output = relay.Tuple([call_7108,call_7115,const_7116,var_7117,])
output2 = relay.Tuple([call_7109,call_7118,const_7116,var_7117,])
func_7119 = relay.Function([var_7117,], output)
mod['func_7119'] = func_7119
mod = relay.transform.InferType()(mod)
mutated_mod['func_7119'] = func_7119
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7120 = relay.var("var_7120", dtype = "float64", shape = (130,))#candidate|7120|(130,)|var|float64
func_7119_call = mutated_mod.get_global_var('func_7119')
call_7121 = func_7119_call(var_7120)
output = call_7121
func_7122 = relay.Function([var_7120], output)
mutated_mod['func_7122'] = func_7122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4440_call = mod.get_global_var('func_4440')
func_4442_call = mutated_mod.get_global_var('func_4442')
call_7127 = func_4440_call()
call_7128 = func_4440_call()
func_1786_call = mod.get_global_var('func_1786')
func_1790_call = mutated_mod.get_global_var('func_1790')
var_7132 = relay.var("var_7132", dtype = "int8", shape = (200,))#candidate|7132|(200,)|var|int8
call_7131 = relay.TupleGetItem(func_1786_call(relay.reshape(var_7132.astype('int8'), [10, 2, 10]), relay.reshape(var_7132.astype('int8'), [10, 2, 10]), ), 0)
call_7133 = relay.TupleGetItem(func_1790_call(relay.reshape(var_7132.astype('int8'), [10, 2, 10]), relay.reshape(var_7132.astype('int8'), [10, 2, 10]), ), 0)
output = relay.Tuple([call_7127,call_7131,var_7132,])
output2 = relay.Tuple([call_7128,call_7133,var_7132,])
func_7139 = relay.Function([var_7132,], output)
mod['func_7139'] = func_7139
mod = relay.transform.InferType()(mod)
mutated_mod['func_7139'] = func_7139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7140 = relay.var("var_7140", dtype = "int8", shape = (200,))#candidate|7140|(200,)|var|int8
func_7139_call = mutated_mod.get_global_var('func_7139')
call_7141 = func_7139_call(var_7140)
output = call_7141
func_7142 = relay.Function([var_7140], output)
mutated_mod['func_7142'] = func_7142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6355_call = mod.get_global_var('func_6355')
func_6356_call = mutated_mod.get_global_var('func_6356')
call_7144 = func_6355_call()
call_7145 = func_6355_call()
output = call_7144
output2 = call_7145
func_7158 = relay.Function([], output)
mod['func_7158'] = func_7158
mod = relay.transform.InferType()(mod)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7158_call = mutated_mod.get_global_var('func_7158')
call_7159 = func_7158_call()
output = call_7159
func_7160 = relay.Function([], output)
mutated_mod['func_7160'] = func_7160
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7175 = relay.var("var_7175", dtype = "float32", shape = (1, 1, 3))#candidate|7175|(1, 1, 3)|var|float32
uop_7176 = relay.log2(var_7175.astype('float32')) # shape=(1, 1, 3)
uop_7182 = relay.cos(uop_7176.astype('float64')) # shape=(1, 1, 3)
output = relay.Tuple([uop_7182,])
output2 = relay.Tuple([uop_7182,])
func_7190 = relay.Function([var_7175,], output)
mod['func_7190'] = func_7190
mod = relay.transform.InferType()(mod)
var_7191 = relay.var("var_7191", dtype = "float32", shape = (1, 1, 3))#candidate|7191|(1, 1, 3)|var|float32
output = func_7190(var_7191)
func_7192 = relay.Function([var_7191], output)
mutated_mod['func_7192'] = func_7192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5940_call = mod.get_global_var('func_5940')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_7294 = func_5940_call()
call_7295 = func_5940_call()
uop_7302 = relay.sinh(call_7294.astype('float32')) # shape=(4, 9, 6)
uop_7304 = relay.sinh(call_7295.astype('float32')) # shape=(4, 9, 6)
output = uop_7302
output2 = uop_7304
func_7323 = relay.Function([], output)
mod['func_7323'] = func_7323
mod = relay.transform.InferType()(mod)
mutated_mod['func_7323'] = func_7323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7323_call = mutated_mod.get_global_var('func_7323')
call_7324 = func_7323_call()
output = call_7324
func_7325 = relay.Function([], output)
mutated_mod['func_7325'] = func_7325
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7357 = relay.const([[[1,4,4,2,-4,10,-5,3,6]],[[-4,-4,5,-7,-5,8,6,9,9]],[[-1,-5,-4,-5,3,-8,-5,-9,-1]],[[9,9,2,9,7,9,3,4,2]],[[-2,-9,-5,7,-9,9,1,7,-1]],[[5,6,-9,-5,2,-2,-1,3,1]],[[-7,6,-3,8,-4,-3,-2,6,-2]],[[3,-9,1,1,-6,-2,-2,5,6]],[[4,3,-7,-4,7,-6,-7,8,-8]],[[-7,-1,-3,2,-3,-5,7,3,9]],[[8,-8,3,6,5,-6,-3,1,-8]],[[10,-2,-6,-1,6,5,-1,-1,8]],[[5,6,5,4,-6,5,-3,-5,5]],[[-2,4,-10,5,2,2,-2,1,8]]], dtype = "uint16")#candidate|7357|(14, 1, 9)|const|uint16
const_7358 = relay.const([[[-6,-9,3,6,-7,-7,9,8,2]],[[3,-1,-3,6,2,-10,8,-2,-6]],[[10,-10,5,5,3,-5,1,1,5]],[[-7,-6,6,4,3,-10,-8,3,7]],[[-7,1,-8,-7,4,-2,-9,-1,8]],[[4,-9,9,-6,-2,-6,6,-3,-3]],[[3,1,7,-8,2,5,5,3,4]],[[5,-8,-10,8,-10,-5,6,-5,7]],[[2,-8,5,6,3,-3,-3,9,-7]],[[-8,7,8,10,-3,-10,-7,-8,-7]],[[-10,-10,-4,10,-1,-1,-9,3,-6]],[[9,-4,-3,5,-9,4,-5,-10,-7]],[[-7,-4,-5,-9,3,-10,5,-6,-6]],[[-5,8,-3,1,9,4,-8,5,1]]], dtype = "uint16")#candidate|7358|(14, 1, 9)|const|uint16
bop_7359 = relay.equal(const_7357.astype('bool'), relay.reshape(const_7358.astype('bool'), relay.shape_of(const_7357))) # shape=(14, 1, 9)
func_2595_call = mod.get_global_var('func_2595')
func_2596_call = mutated_mod.get_global_var('func_2596')
call_7365 = func_2595_call()
call_7366 = func_2595_call()
bop_7373 = relay.greater(const_7358.astype('bool'), relay.reshape(bop_7359.astype('bool'), relay.shape_of(const_7358))) # shape=(14, 1, 9)
bop_7380 = relay.power(const_7357.astype('float64'), relay.reshape(const_7358.astype('float64'), relay.shape_of(const_7357))) # shape=(14, 1, 9)
uop_7383 = relay.acos(const_7357.astype('float32')) # shape=(14, 1, 9)
output = relay.Tuple([call_7365,bop_7373,bop_7380,uop_7383,])
output2 = relay.Tuple([call_7366,bop_7373,bop_7380,uop_7383,])
func_7404 = relay.Function([], output)
mod['func_7404'] = func_7404
mod = relay.transform.InferType()(mod)
mutated_mod['func_7404'] = func_7404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7404_call = mutated_mod.get_global_var('func_7404')
call_7405 = func_7404_call()
output = call_7405
func_7406 = relay.Function([], output)
mutated_mod['func_7406'] = func_7406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6014_call = mod.get_global_var('func_6014')
func_6016_call = mutated_mod.get_global_var('func_6016')
call_7413 = func_6014_call()
call_7414 = func_6014_call()
func_6967_call = mod.get_global_var('func_6967')
func_6969_call = mutated_mod.get_global_var('func_6969')
call_7417 = relay.TupleGetItem(func_6967_call(), 3)
call_7418 = relay.TupleGetItem(func_6969_call(), 3)
output = relay.Tuple([call_7413,call_7417,])
output2 = relay.Tuple([call_7414,call_7418,])
func_7425 = relay.Function([], output)
mod['func_7425'] = func_7425
mod = relay.transform.InferType()(mod)
mutated_mod['func_7425'] = func_7425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7425_call = mutated_mod.get_global_var('func_7425')
call_7426 = func_7425_call()
output = call_7426
func_7427 = relay.Function([], output)
mutated_mod['func_7427'] = func_7427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_7492 = relay.TupleGetItem(func_3833_call(), 1)
call_7493 = relay.TupleGetItem(func_3835_call(), 1)
output = relay.Tuple([call_7492,])
output2 = relay.Tuple([call_7493,])
func_7494 = relay.Function([], output)
mod['func_7494'] = func_7494
mod = relay.transform.InferType()(mod)
mutated_mod['func_7494'] = func_7494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7494_call = mutated_mod.get_global_var('func_7494')
call_7495 = func_7494_call()
output = call_7495
func_7496 = relay.Function([], output)
mutated_mod['func_7496'] = func_7496
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7497 = relay.var("var_7497", dtype = "float64", shape = (6, 5, 10))#candidate|7497|(6, 5, 10)|var|float64
uop_7498 = relay.sigmoid(var_7497.astype('float64')) # shape=(6, 5, 10)
output = uop_7498
output2 = uop_7498
func_7522 = relay.Function([var_7497,], output)
mod['func_7522'] = func_7522
mod = relay.transform.InferType()(mod)
var_7523 = relay.var("var_7523", dtype = "float64", shape = (6, 5, 10))#candidate|7523|(6, 5, 10)|var|float64
output = func_7522(var_7523)
func_7524 = relay.Function([var_7523], output)
mutated_mod['func_7524'] = func_7524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_7534 = func_1903_call()
call_7535 = func_1903_call()
var_7540 = relay.var("var_7540", dtype = "bool", shape = (4, 9, 6))#candidate|7540|(4, 9, 6)|var|bool
bop_7541 = relay.subtract(call_7534.astype('uint64'), relay.reshape(var_7540.astype('uint64'), relay.shape_of(call_7534))) # shape=(4, 9, 6)
bop_7544 = relay.subtract(call_7535.astype('uint64'), relay.reshape(var_7540.astype('uint64'), relay.shape_of(call_7535))) # shape=(4, 9, 6)
output = relay.Tuple([bop_7541,])
output2 = relay.Tuple([bop_7544,])
func_7552 = relay.Function([var_7540,], output)
mod['func_7552'] = func_7552
mod = relay.transform.InferType()(mod)
mutated_mod['func_7552'] = func_7552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7553 = relay.var("var_7553", dtype = "bool", shape = (4, 9, 6))#candidate|7553|(4, 9, 6)|var|bool
func_7552_call = mutated_mod.get_global_var('func_7552')
call_7554 = func_7552_call(var_7553)
output = call_7554
func_7555 = relay.Function([var_7553], output)
mutated_mod['func_7555'] = func_7555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5158_call = mutated_mod.get_global_var('func_5158')
call_7622 = func_5156_call()
call_7623 = func_5156_call()
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_7668 = relay.TupleGetItem(func_5418_call(), 0)
call_7669 = relay.TupleGetItem(func_5420_call(), 0)
output = relay.Tuple([call_7622,call_7668,])
output2 = relay.Tuple([call_7623,call_7669,])
func_7671 = relay.Function([], output)
mod['func_7671'] = func_7671
mod = relay.transform.InferType()(mod)
output = func_7671()
func_7672 = relay.Function([], output)
mutated_mod['func_7672'] = func_7672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_7726 = func_6224_call()
call_7727 = func_6224_call()
output = relay.Tuple([call_7726,])
output2 = relay.Tuple([call_7727,])
func_7736 = relay.Function([], output)
mod['func_7736'] = func_7736
mod = relay.transform.InferType()(mod)
mutated_mod['func_7736'] = func_7736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7736_call = mutated_mod.get_global_var('func_7736')
call_7737 = func_7736_call()
output = call_7737
func_7738 = relay.Function([], output)
mutated_mod['func_7738'] = func_7738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4661_call = mod.get_global_var('func_4661')
func_4663_call = mutated_mod.get_global_var('func_4663')
call_7739 = relay.TupleGetItem(func_4661_call(), 0)
call_7740 = relay.TupleGetItem(func_4663_call(), 0)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_7746 = relay.TupleGetItem(func_2570_call(), 0)
call_7747 = relay.TupleGetItem(func_2571_call(), 0)
func_6967_call = mod.get_global_var('func_6967')
func_6969_call = mutated_mod.get_global_var('func_6969')
call_7765 = relay.TupleGetItem(func_6967_call(), 5)
call_7766 = relay.TupleGetItem(func_6969_call(), 5)
func_3437_call = mod.get_global_var('func_3437')
func_3440_call = mutated_mod.get_global_var('func_3440')
call_7770 = relay.TupleGetItem(func_3437_call(relay.reshape(call_7739.astype('bool'), [4, 9, 6])), 3)
call_7771 = relay.TupleGetItem(func_3440_call(relay.reshape(call_7739.astype('bool'), [4, 9, 6])), 3)
output = relay.Tuple([call_7739,call_7746,call_7765,call_7770,])
output2 = relay.Tuple([call_7740,call_7747,call_7766,call_7771,])
func_7779 = relay.Function([], output)
mod['func_7779'] = func_7779
mod = relay.transform.InferType()(mod)
output = func_7779()
func_7780 = relay.Function([], output)
mutated_mod['func_7780'] = func_7780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_7806 = relay.TupleGetItem(func_1728_call(), 2)
call_7807 = relay.TupleGetItem(func_1730_call(), 2)
func_4661_call = mod.get_global_var('func_4661')
func_4663_call = mutated_mod.get_global_var('func_4663')
call_7812 = relay.TupleGetItem(func_4661_call(), 0)
call_7813 = relay.TupleGetItem(func_4663_call(), 0)
output = relay.Tuple([call_7806,call_7812,])
output2 = relay.Tuple([call_7807,call_7813,])
func_7824 = relay.Function([], output)
mod['func_7824'] = func_7824
mod = relay.transform.InferType()(mod)
mutated_mod['func_7824'] = func_7824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7824_call = mutated_mod.get_global_var('func_7824')
call_7825 = func_7824_call()
output = call_7825
func_7826 = relay.Function([], output)
mutated_mod['func_7826'] = func_7826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7404_call = mod.get_global_var('func_7404')
func_7406_call = mutated_mod.get_global_var('func_7406')
call_7836 = relay.TupleGetItem(func_7404_call(), 2)
call_7837 = relay.TupleGetItem(func_7406_call(), 2)
uop_7846 = relay.sin(call_7836.astype('float32')) # shape=(14, 1, 9)
uop_7848 = relay.sin(call_7837.astype('float32')) # shape=(14, 1, 9)
uop_7863 = relay.acosh(uop_7846.astype('float64')) # shape=(14, 1, 9)
uop_7865 = relay.acosh(uop_7848.astype('float64')) # shape=(14, 1, 9)
output = uop_7863
output2 = uop_7865
func_7871 = relay.Function([], output)
mod['func_7871'] = func_7871
mod = relay.transform.InferType()(mod)
output = func_7871()
func_7872 = relay.Function([], output)
mutated_mod['func_7872'] = func_7872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7323_call = mod.get_global_var('func_7323')
func_7325_call = mutated_mod.get_global_var('func_7325')
call_7881 = func_7323_call()
call_7882 = func_7323_call()
output = call_7881
output2 = call_7882
func_7885 = relay.Function([], output)
mod['func_7885'] = func_7885
mod = relay.transform.InferType()(mod)
mutated_mod['func_7885'] = func_7885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mutated_mod.get_global_var('func_7885')
call_7886 = func_7885_call()
output = call_7886
func_7887 = relay.Function([], output)
mutated_mod['func_7887'] = func_7887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6852_call = mod.get_global_var('func_6852')
func_6853_call = mutated_mod.get_global_var('func_6853')
call_7936 = func_6852_call()
call_7937 = func_6852_call()
output = relay.Tuple([call_7936,])
output2 = relay.Tuple([call_7937,])
func_7946 = relay.Function([], output)
mod['func_7946'] = func_7946
mod = relay.transform.InferType()(mod)
mutated_mod['func_7946'] = func_7946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7946_call = mutated_mod.get_global_var('func_7946')
call_7947 = func_7946_call()
output = call_7947
func_7948 = relay.Function([], output)
mutated_mod['func_7948'] = func_7948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5940_call = mod.get_global_var('func_5940')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_8012 = func_5940_call()
call_8013 = func_5940_call()
func_7824_call = mod.get_global_var('func_7824')
func_7826_call = mutated_mod.get_global_var('func_7826')
call_8016 = relay.TupleGetItem(func_7824_call(), 0)
call_8017 = relay.TupleGetItem(func_7826_call(), 0)
func_50_call = mod.get_global_var('func_50')
func_52_call = mutated_mod.get_global_var('func_52')
const_8025 = relay.const([-1.978035,4.232072,9.472875,9.287229,-2.051082,4.959236,-5.504992,-5.407450,8.144505,-1.643068,-4.235511,-0.052129,0.461020,4.739517,2.185272,5.191814,-9.242328,6.800253,1.053826,-7.112570,5.452408,7.417899,8.954169,2.442936,-6.209792,-8.026885,1.775168,-8.399711,-8.759785,4.471473,-1.423738,6.123573,7.443977,-5.009644,7.354393,5.478243,-0.226385,-3.147877,-3.191600,-1.024331,1.580300,3.167846,8.455610,2.529813,7.464001,1.270793,-9.380326,0.940640,7.053166,-5.552110,-5.321586,9.528669,8.988170,-7.810666,8.004968,-2.521441,9.543451,1.060895,8.993006,-6.818520,-8.439265,-0.949041,-8.938118,-1.438246,0.021393,6.857693,-2.677493,-3.714034,-1.668504,-0.592253,3.472489,8.100180,-5.841721,4.709566,6.009085,7.634307,1.097066,-9.848916,1.475198,-2.885280,-2.749365,-8.528376,-4.585556,-5.636293,8.732833,6.386064,4.415480,4.049318,9.030652,4.255960,7.362749,-4.907164,-7.185879,-8.920605,-8.034980,-6.181012,-4.472453,1.004844,1.876997,-2.829193,-0.498025,9.792409,-9.566172,-9.163137,6.632161,-3.564509,-6.185314,8.383900,-3.297199,-6.618786,-2.325297,6.195471,4.230308,-4.958260,-4.265879,2.738774,-0.890462,-2.322044,8.188142,-6.170205,-2.289653,7.419007,-2.797207,1.805438,4.124243,2.720252,-1.644803,-4.996102,4.041507,-4.174949], dtype = "float64")#candidate|8025|(130,)|const|float64
call_8024 = relay.TupleGetItem(func_50_call(relay.reshape(const_8025.astype('float64'), [13, 10, 1])), 0)
call_8026 = relay.TupleGetItem(func_52_call(relay.reshape(const_8025.astype('float64'), [13, 10, 1])), 0)
var_8052 = relay.var("var_8052", dtype = "float64", shape = (13, 10, 9))#candidate|8052|(13, 10, 9)|var|float64
bop_8053 = relay.multiply(call_8024.astype('float32'), relay.reshape(var_8052.astype('float32'), relay.shape_of(call_8024))) # shape=(13, 10, 9)
bop_8056 = relay.multiply(call_8026.astype('float32'), relay.reshape(var_8052.astype('float32'), relay.shape_of(call_8026))) # shape=(13, 10, 9)
output = relay.Tuple([call_8012,call_8016,const_8025,bop_8053,])
output2 = relay.Tuple([call_8013,call_8017,const_8025,bop_8056,])
func_8057 = relay.Function([var_8052,], output)
mod['func_8057'] = func_8057
mod = relay.transform.InferType()(mod)
var_8058 = relay.var("var_8058", dtype = "float64", shape = (13, 10, 9))#candidate|8058|(13, 10, 9)|var|float64
output = func_8057(var_8058)
func_8059 = relay.Function([var_8058], output)
mutated_mod['func_8059'] = func_8059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7824_call = mod.get_global_var('func_7824')
func_7826_call = mutated_mod.get_global_var('func_7826')
call_8067 = relay.TupleGetItem(func_7824_call(), 0)
call_8068 = relay.TupleGetItem(func_7826_call(), 0)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
var_8076 = relay.var("var_8076", dtype = "float64", shape = (70,))#candidate|8076|(70,)|var|float64
call_8075 = relay.TupleGetItem(func_235_call(relay.reshape(var_8076.astype('float64'), [1, 10, 7])), 0)
call_8077 = relay.TupleGetItem(func_237_call(relay.reshape(var_8076.astype('float64'), [1, 10, 7])), 0)
output = relay.Tuple([call_8067,call_8075,var_8076,])
output2 = relay.Tuple([call_8068,call_8077,var_8076,])
func_8089 = relay.Function([var_8076,], output)
mod['func_8089'] = func_8089
mod = relay.transform.InferType()(mod)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8090 = relay.var("var_8090", dtype = "float64", shape = (70,))#candidate|8090|(70,)|var|float64
func_8089_call = mutated_mod.get_global_var('func_8089')
call_8091 = func_8089_call(var_8090)
output = call_8091
func_8092 = relay.Function([var_8090], output)
mutated_mod['func_8092'] = func_8092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_8143 = func_2162_call()
call_8144 = func_2162_call()
output = call_8143
output2 = call_8144
func_8147 = relay.Function([], output)
mod['func_8147'] = func_8147
mod = relay.transform.InferType()(mod)
output = func_8147()
func_8148 = relay.Function([], output)
mutated_mod['func_8148'] = func_8148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_8157 = func_2162_call()
call_8158 = func_2162_call()
func_5679_call = mod.get_global_var('func_5679')
func_5682_call = mutated_mod.get_global_var('func_5682')
var_8186 = relay.var("var_8186", dtype = "bool", shape = (216,))#candidate|8186|(216,)|var|bool
call_8185 = relay.TupleGetItem(func_5679_call(relay.reshape(var_8186.astype('bool'), [4, 9, 6])), 0)
call_8187 = relay.TupleGetItem(func_5682_call(relay.reshape(var_8186.astype('bool'), [4, 9, 6])), 0)
func_7035_call = mod.get_global_var('func_7035')
func_7036_call = mutated_mod.get_global_var('func_7036')
call_8192 = func_7035_call()
call_8193 = func_7035_call()
func_1534_call = mod.get_global_var('func_1534')
func_1539_call = mutated_mod.get_global_var('func_1539')
var_8205 = relay.var("var_8205", dtype = "int64", shape = (294,))#candidate|8205|(294,)|var|int64
call_8204 = relay.TupleGetItem(func_1534_call(relay.reshape(var_8205.astype('int64'), [7, 3, 14]), relay.reshape(var_8205.astype('int64'), [7, 3, 14]), relay.reshape(var_8205.astype('float32'), [7, 3, 14]), ), 0)
call_8206 = relay.TupleGetItem(func_1539_call(relay.reshape(var_8205.astype('int64'), [7, 3, 14]), relay.reshape(var_8205.astype('int64'), [7, 3, 14]), relay.reshape(var_8205.astype('float32'), [7, 3, 14]), ), 0)
output = relay.Tuple([call_8157,call_8185,var_8186,call_8192,call_8204,var_8205,])
output2 = relay.Tuple([call_8158,call_8187,var_8186,call_8193,call_8206,var_8205,])
func_8211 = relay.Function([var_8186,var_8205,], output)
mod['func_8211'] = func_8211
mod = relay.transform.InferType()(mod)
var_8212 = relay.var("var_8212", dtype = "bool", shape = (216,))#candidate|8212|(216,)|var|bool
var_8213 = relay.var("var_8213", dtype = "int64", shape = (294,))#candidate|8213|(294,)|var|int64
output = func_8211(var_8212,var_8213,)
func_8214 = relay.Function([var_8212,var_8213,], output)
mutated_mod['func_8214'] = func_8214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7035_call = mod.get_global_var('func_7035')
func_7036_call = mutated_mod.get_global_var('func_7036')
call_8358 = func_7035_call()
call_8359 = func_7035_call()
output = relay.Tuple([call_8358,])
output2 = relay.Tuple([call_8359,])
func_8360 = relay.Function([], output)
mod['func_8360'] = func_8360
mod = relay.transform.InferType()(mod)
mutated_mod['func_8360'] = func_8360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8360_call = mutated_mod.get_global_var('func_8360')
call_8361 = func_8360_call()
output = call_8361
func_8362 = relay.Function([], output)
mutated_mod['func_8362'] = func_8362
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8389 = relay.const([[[True,True,True,False],[False,False,False,False],[False,True,True,False],[True,True,False,True],[True,True,False,False],[False,False,False,False]],[[True,False,True,False],[True,False,False,False],[False,True,False,False],[False,False,False,False],[True,False,False,True],[True,True,False,True]],[[False,False,True,True],[False,False,True,True],[False,False,True,False],[False,False,False,False],[True,True,True,True],[True,True,True,True]],[[True,False,False,True],[True,False,False,True],[False,True,False,False],[True,True,True,False],[True,False,False,False],[False,False,False,False]],[[True,True,True,True],[True,True,False,False],[True,False,True,False],[False,True,True,False],[True,False,False,False],[True,True,False,True]],[[True,False,True,False],[True,True,False,False],[True,True,True,False],[False,True,False,True],[True,False,True,True],[True,True,True,False]],[[True,True,True,False],[False,True,True,False],[False,False,False,True],[False,False,True,True],[True,True,True,False],[False,True,True,False]],[[True,True,True,True],[False,True,True,True],[False,False,True,True],[False,True,True,False],[True,True,True,True],[True,False,False,False]]], dtype = "bool")#candidate|8389|(8, 6, 4)|const|bool
var_8390 = relay.var("var_8390", dtype = "bool", shape = (8, 6, 4))#candidate|8390|(8, 6, 4)|var|bool
bop_8391 = relay.logical_or(const_8389.astype('bool'), relay.reshape(var_8390.astype('bool'), relay.shape_of(const_8389))) # shape=(8, 6, 4)
output = relay.Tuple([bop_8391,])
output2 = relay.Tuple([bop_8391,])
func_8397 = relay.Function([var_8390,], output)
mod['func_8397'] = func_8397
mod = relay.transform.InferType()(mod)
mutated_mod['func_8397'] = func_8397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8398 = relay.var("var_8398", dtype = "bool", shape = (8, 6, 4))#candidate|8398|(8, 6, 4)|var|bool
func_8397_call = mutated_mod.get_global_var('func_8397')
call_8399 = func_8397_call(var_8398)
output = call_8399
func_8400 = relay.Function([var_8398], output)
mutated_mod['func_8400'] = func_8400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_8410 = func_4139_call()
call_8411 = func_4139_call()
func_1903_call = mod.get_global_var('func_1903')
func_1904_call = mutated_mod.get_global_var('func_1904')
call_8415 = func_1903_call()
call_8416 = func_1903_call()
output = relay.Tuple([call_8410,call_8415,])
output2 = relay.Tuple([call_8411,call_8416,])
func_8426 = relay.Function([], output)
mod['func_8426'] = func_8426
mod = relay.transform.InferType()(mod)
output = func_8426()
func_8427 = relay.Function([], output)
mutated_mod['func_8427'] = func_8427
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8483 = relay.var("var_8483", dtype = "int32", shape = ())#candidate|8483|()|var|int32
var_8484 = relay.var("var_8484", dtype = "int32", shape = (1, 12, 3))#candidate|8484|(1, 12, 3)|var|int32
bop_8485 = relay.not_equal(var_8483.astype('bool'), var_8484.astype('bool')) # shape=(1, 12, 3)
func_2523_call = mod.get_global_var('func_2523')
func_2526_call = mutated_mod.get_global_var('func_2526')
var_8508 = relay.var("var_8508", dtype = "float64", shape = (32,))#candidate|8508|(32,)|var|float64
call_8507 = func_2523_call(relay.reshape(var_8508.astype('float64'), [8, 4, 1]))
call_8509 = func_2523_call(relay.reshape(var_8508.astype('float64'), [8, 4, 1]))
output = relay.Tuple([bop_8485,call_8507,var_8508,])
output2 = relay.Tuple([bop_8485,call_8509,var_8508,])
func_8529 = relay.Function([var_8483,var_8484,var_8508,], output)
mod['func_8529'] = func_8529
mod = relay.transform.InferType()(mod)
mutated_mod['func_8529'] = func_8529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8529_call = mutated_mod.get_global_var('func_8529')
var_8531 = relay.var("var_8531", dtype = "int32", shape = ())#candidate|8531|()|var|int32
var_8532 = relay.var("var_8532", dtype = "int32", shape = (1, 12, 3))#candidate|8532|(1, 12, 3)|var|int32
var_8533 = relay.var("var_8533", dtype = "float64", shape = (32,))#candidate|8533|(32,)|var|float64
call_8530 = func_8529_call(var_8531,var_8532,var_8533,)
output = call_8530
func_8534 = relay.Function([var_8531,var_8532,var_8533,], output)
mutated_mod['func_8534'] = func_8534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4468_call = mod.get_global_var('func_4468')
func_4469_call = mutated_mod.get_global_var('func_4469')
call_8544 = relay.TupleGetItem(func_4468_call(), 0)
call_8545 = relay.TupleGetItem(func_4469_call(), 0)
func_7425_call = mod.get_global_var('func_7425')
func_7427_call = mutated_mod.get_global_var('func_7427')
call_8558 = relay.TupleGetItem(func_7425_call(), 0)
call_8559 = relay.TupleGetItem(func_7427_call(), 0)
func_1885_call = mod.get_global_var('func_1885')
func_1888_call = mutated_mod.get_global_var('func_1888')
const_8563 = relay.const([-9.359318,8.620593,-0.952599,-2.253662,5.774669,1.356693,7.863847,5.247123,6.587158,-0.747353,1.617574,-0.153484,-1.698685,-3.797020,-7.153881,-8.265688,6.160288,-6.366953,-1.629106,-3.749259,-3.271267,-1.996335,-7.276714,-9.749819,5.114591,-2.321430,6.199403,9.552176,1.181284,8.174190,-4.505534,-6.606699,-4.675585,1.761025,3.365125,-6.465649,0.878753,8.220717,9.426275,-8.940096,2.003536,0.242111,6.530788,-5.537641,9.824606,7.117613,6.999102,5.204681,-8.975225,9.693573,-3.654450,8.611899,-8.099904,7.920254,2.108505,-5.773431,8.779479,6.502020,-0.098023,3.483900,-6.190402,1.607073,6.833347,2.102693,4.039654,1.150333,-3.267027,-4.408051,-6.242337,-1.607871,3.064679,-6.963796,4.578946,1.134802,9.080209,2.064290,3.813951,6.202055,1.284275,-1.147520,8.034620,-2.458593,4.054263,-1.828918,-5.644596,8.542195,-8.030223,-3.065573,7.624152,2.842296,6.610534,-5.235822,-0.309491,1.937336,-1.314166,-6.379636,7.271909,-4.036674,5.524932,-9.286962,6.828609,2.788028,4.438062,3.023578,-6.240603,3.567198,1.024244,-1.882353,-5.000496,9.475185,-9.922481,-9.555890,-1.202849,-3.830373,-3.713125,-9.865500,-1.108626,8.086062,3.089618,-6.637654,1.970000,3.702699,-0.797281,-3.345658,8.403923,0.837268,-4.825312,-5.219176,-3.344038,-0.894652,3.323557,8.425066,8.714380,-1.855239,7.419507,-9.387042,-3.499492,-8.770247,0.655067,8.252310,-3.806058,-5.688333,6.042083,-7.024184,2.207908,-5.014220,2.184495,-7.973160,-6.366028,1.102063,-9.185453,-1.101144,-6.023263,5.143852,-8.249005,-5.094981,9.745176,6.266019,7.745911,5.771074,-9.351832,-5.177588,1.870541,-8.163284,4.157708,6.315646,0.231875,-5.619053,-0.172326,-6.093958,2.728766,-0.713323,5.945615,1.154598,8.864272,-9.921048,-3.280788,9.829397,6.814049,4.937509,9.339099,-0.729284,-5.557422,-2.461744,-9.504525,6.159634,-5.018214,1.273533,8.520312,-4.355613,8.330939,0.318423,8.297124,9.184411,-0.604928,1.471351,5.833439,2.421015,7.654128,5.851436,-0.200736,4.437397,-8.366602,-2.246638,8.751389,-5.541245,3.507198,-9.091572,-1.884534,-2.153141,-3.306056,-2.355688,0.890977,7.729783,-4.586177,8.173910], dtype = "float32")#candidate|8563|(216,)|const|float32
call_8562 = func_1885_call(relay.reshape(const_8563.astype('float32'), [3, 12, 6]))
call_8564 = func_1885_call(relay.reshape(const_8563.astype('float32'), [3, 12, 6]))
func_1286_call = mod.get_global_var('func_1286')
func_1289_call = mutated_mod.get_global_var('func_1289')
call_8567 = relay.TupleGetItem(func_1286_call(relay.reshape(const_8563.astype('int8'), [4, 9, 6])), 2)
call_8568 = relay.TupleGetItem(func_1289_call(relay.reshape(const_8563.astype('int8'), [4, 9, 6])), 2)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_8575 = func_1845_call()
call_8576 = func_1845_call()
func_8057_call = mod.get_global_var('func_8057')
func_8059_call = mutated_mod.get_global_var('func_8059')
const_8579 = relay.const([[-3.887399,-5.357542,1.581896,-6.674597,2.353639,4.610071,-9.185894,6.207871,0.344575,6.230164,-7.571339,-1.263669,6.911001,-7.347521,-6.337648,0.911123,-2.029229,7.887370,6.299042,-9.299941,-0.763020,-3.828072,-8.066011,-1.356058,-6.516376,0.971968,7.688278,0.863351,8.155218,-0.743116,-7.476934,-4.677127,9.944627,9.492066,1.615560,-8.567965,1.437627,-3.673241,-5.848518,8.297230,-4.511120,6.755628,-1.837501,-6.838710,-5.210204,7.427238,-9.371304,9.331906,9.024960,9.812948,7.142532,-9.050101,-5.135402,-1.104156,-7.799919,6.734072,-1.885064,-8.202540,0.556557,-0.943441,3.853489,2.268464,7.820411,-9.116948,5.972803,7.365752,7.413615,5.177946,-7.252618,-4.707153,-4.183055,-9.325670,-8.349334,0.485350,4.570062,-7.807566,-2.376496,7.610396,-3.441787,-3.380981,3.453545,-3.262715,-8.805994,-2.887006,-0.383679,9.736621,1.449060,4.232430,-1.866251,2.913119,1.915442,-5.594879,8.506115,0.353951,6.675865,3.128093,-5.142786,3.437602,-1.856843,8.675309,-0.152720,6.782265,-0.889121,-0.022438,7.745427,2.311963,7.547643,-3.300230,3.503773,-2.719992,-1.381040,1.098037,-2.365030,1.634705,-1.559201,4.532000,6.724127,-7.503352,9.580212,-4.991837,0.314369,8.476473,9.455668,9.491672,-2.444192,-3.355630,-6.691473,9.756379,-8.387019,0.147049,3.839459,-0.743763,8.227949,5.699937,1.101633,7.251482,7.104730,2.608380,8.545495,0.754654,-8.863929,-8.713493,2.749786,6.832701,-8.712080,-9.650457,3.802555,-7.018638,-8.321431,-5.992859,4.996913,-2.107421,-3.004467,3.512251,-2.702987,3.579374,-4.699805,3.781962,6.381579,-8.051200,3.908264,-6.376825,3.368461,6.299885,-0.072666,4.089216,-2.965265,-2.435792,6.743969,-4.326394,-8.472210,-8.572351,5.217704,-5.598315,1.802403,-9.518609,6.747054,3.378070,6.014002,-7.554102,-6.266055,1.017467,7.857740,-5.055838,2.059934,3.296175,-3.923815,0.091372,0.198600,0.591761,-2.853717,-3.317509,-1.295253,-4.354142,-2.922892,8.447806,-6.248768,1.479878,-1.309475,-6.776023,-8.609078,1.010180,8.035762,-5.951045,-5.838290,1.390600,6.896488,-2.497819,-5.605561,7.450197,-5.271564,3.722019,3.687580,-9.382687,-2.133825,-8.167854,-5.530692,-4.733754,-0.065857,4.515520,-4.851913,8.113730,-9.123300,9.761532,-2.633634,9.396361,5.767890,8.491746,-1.935366,-9.021911,-2.424851,7.236758,-9.562803,-5.548337],[0.556954,1.789952,0.674334,8.207935,-1.303253,-7.942504,-3.646672,3.452668,-3.097754,-6.090692,6.546199,-0.054271,6.139382,-2.225628,6.276089,-5.795737,-0.158956,-0.820133,-3.231383,4.645438,-9.869942,2.206132,-7.872343,-4.492053,6.364273,9.279165,3.798684,-1.231742,6.513097,-1.162077,-8.774774,0.619060,-8.451404,-5.130979,-9.688098,4.326038,7.244036,4.411053,-3.704356,-6.469766,-4.333807,-9.394446,6.765318,2.389910,9.555580,8.519594,-9.522787,1.778769,-5.738642,-6.080740,7.870231,0.847912,-7.633293,-0.344283,-4.087601,6.888425,-6.958795,-2.475794,-8.806967,5.293232,3.739049,5.022347,7.303827,-1.061872,-6.768670,-7.573016,1.491603,-5.756170,-6.828075,-8.881769,-7.252585,-5.523877,0.743337,-5.841367,-5.045421,9.390867,5.195657,2.514175,8.729968,-9.057237,-2.361846,-2.049926,2.304530,-9.100047,5.345665,-4.520641,-1.505599,2.597463,-1.511069,8.941921,6.591577,-7.178444,-4.637036,0.349272,-8.064919,8.586520,5.960679,-7.010044,9.043049,-5.961587,2.706793,-9.845867,1.993750,1.413299,8.078244,-5.735238,8.921890,6.695307,5.375969,-3.313515,0.724772,-2.029257,7.104185,6.468390,0.747101,9.174203,-5.225399,-7.551441,7.885380,0.700868,0.046198,1.840451,9.102445,-0.889717,-6.093103,-8.686044,-6.880116,-8.266275,6.684266,-8.641039,2.300305,9.254666,2.682991,-0.355097,8.078046,-4.152627,1.733573,2.635182,-4.559457,8.887640,-0.737482,-4.685632,2.824935,-7.970362,-3.061392,8.521955,0.348606,-4.949344,4.576601,9.156034,-6.033708,7.488848,-3.385208,-4.167024,-9.659250,6.995402,0.161799,3.410635,-9.206475,9.653939,2.944782,-3.115503,9.613849,1.423445,6.035165,1.115793,-1.558421,-0.266622,-6.442925,-9.348349,-0.457882,1.835736,2.254043,-2.183634,1.152548,4.996671,8.133112,1.144779,-7.948780,9.750114,3.350271,2.213110,1.671616,-5.159936,3.075254,-6.266629,-8.649318,8.412997,-2.657641,3.508366,-0.463602,-8.113336,9.838944,-3.252687,6.387199,5.033807,2.093019,-6.983623,-0.154223,-2.923360,5.404556,-5.491501,-8.276901,-0.903752,9.852507,-9.552244,-7.342683,5.944970,-0.471904,2.057809,1.567019,9.969110,0.009234,4.603228,-0.093062,3.773364,-2.238883,-5.312271,-8.511415,-1.829961,-9.042269,5.534101,3.741630,-5.249947,-3.412595,5.442572,3.115254,-1.189933,0.097285,-8.210684,5.362015,1.853678,5.598350,5.300491],[-6.169454,-6.546469,-5.437919,1.538624,-2.789031,-7.729806,3.196440,2.358747,-1.119478,-6.375029,6.772330,7.147780,-5.341565,5.223099,-8.925897,2.197598,-8.171832,-7.837206,3.093491,-6.589526,3.899911,0.804324,3.841683,9.704108,-9.289297,8.436243,4.308443,6.481833,9.572178,3.770711,3.780154,3.432506,-3.224951,-9.451180,4.146527,-3.684141,0.333607,-8.384807,-1.814664,-9.737562,6.773262,-3.437272,6.478131,-9.218570,-5.792398,-7.917020,4.541122,4.915814,3.686890,8.065570,1.380760,-8.173618,2.763269,3.205386,-5.798649,4.714482,3.286112,-9.518668,3.143523,8.096552,1.237099,0.516461,3.351976,-9.754010,-7.426217,-7.839630,3.544806,3.286022,0.370365,-2.957227,-0.353349,2.387454,-4.160674,-6.625068,-3.331012,0.343061,-5.634068,-5.830281,-5.186165,-4.563227,0.149445,-3.551166,0.132071,8.698511,-1.911627,8.288611,1.880369,-9.547866,-4.442012,8.750349,-7.297428,-3.409078,9.500698,6.157097,-2.011239,2.212931,-1.238768,-0.687513,4.957807,-1.160240,-7.959875,-9.984274,-2.046774,6.240672,-9.055740,9.564914,0.024414,2.758343,1.685659,-4.560744,-5.746511,5.470413,4.835381,6.412482,0.986207,-8.962365,6.715584,-0.102753,4.926335,-3.636197,-3.389143,8.521881,-4.761773,6.970222,7.428754,5.217561,2.149383,-1.253884,-1.261772,2.081292,2.381096,7.179845,-2.737735,-0.045585,8.572622,9.789277,-1.932461,-2.538655,0.949047,-5.016173,0.610224,4.574305,-7.687509,-2.375883,9.261066,6.926924,8.463585,3.564959,-7.271399,-0.501120,-1.570367,8.408280,-0.485836,5.134049,9.676233,-3.305915,3.936623,9.061875,4.612975,4.168550,7.307224,6.508303,2.569524,9.717283,-9.812663,-7.456352,0.653617,0.646790,8.534724,-5.008549,5.908799,1.269884,-5.067482,-3.947072,-8.202910,-6.248234,-5.638306,2.783157,-7.359040,0.769182,-4.751295,0.448850,-2.195948,1.424174,-3.442308,-8.284073,-5.228945,-6.979363,3.389217,-9.278538,-4.413366,4.432323,-7.311649,6.442173,2.707572,5.431586,-5.586641,-4.966948,3.551900,-5.462586,2.066215,1.024197,-6.790860,-0.121661,8.762926,-1.911523,1.333071,-4.738602,-3.663010,-5.736674,0.517431,9.990656,-4.894150,-1.471766,4.146173,4.245559,2.966083,-1.648177,3.062167,7.955636,2.434827,-6.778678,-5.844807,-6.972308,-3.666542,-4.739551,-8.976375,4.153893,7.558289,-9.929467,-4.791973,5.025483,1.185008,-1.253621],[-9.730113,5.235062,7.979783,-3.643615,-8.830312,-4.523680,6.546728,-7.546626,-6.536359,2.764662,1.427476,-5.604926,3.390654,-3.499031,0.221489,5.651997,-2.725655,0.743064,0.488009,7.775645,-4.933462,-7.448331,4.918905,5.783646,6.406855,8.704171,-2.172512,-1.137168,-2.515139,-8.222736,2.913467,8.667562,-9.617285,8.553867,0.265971,-8.101771,-9.755079,4.143172,1.824620,6.336884,6.060249,-5.345130,-7.811387,-2.395806,7.698187,-2.980267,-6.100940,-2.836916,-3.951805,-3.736607,2.385406,2.764907,-5.322427,3.745427,2.229891,-0.681237,7.873486,3.160797,8.242301,-1.977151,-1.766507,-7.952415,6.553924,-4.994658,-8.130763,4.049823,5.883502,-4.153557,6.167321,6.442150,-5.809925,-7.599291,-5.471690,-2.654018,3.231335,-7.636317,5.259526,-7.998396,-9.251983,1.190280,-3.724151,-8.350927,1.240834,6.058010,-2.243676,-6.927087,-8.962484,-3.735300,-0.720086,-9.904480,-2.683310,4.017213,6.763671,-1.303178,-5.609038,8.273436,-1.537240,-4.975680,-1.820052,-3.179764,5.589068,0.770871,0.411328,-5.444591,-0.132231,7.562600,-7.799197,6.595090,1.724014,5.508927,5.672499,-4.643017,-6.497278,6.091349,-1.961574,6.615262,-1.113179,1.728954,-8.339512,0.835835,-2.086966,9.495142,-3.448900,2.159376,-6.344961,4.189454,8.655221,9.519161,1.374061,-5.850301,7.849079,9.607327,-0.396533,3.083752,-6.718174,-2.581572,-3.325287,1.036782,-1.709128,-7.802949,7.694307,-9.052363,2.623377,-2.312362,-0.974905,-7.063739,-4.508652,-0.447137,-8.115220,-7.952541,-3.137259,4.669659,-0.083761,1.362986,4.516804,-5.723626,-1.563228,8.486545,-0.324924,-7.787414,-5.730486,-2.533032,-8.072760,-0.070839,2.263950,9.471093,0.346856,-2.031464,-4.117286,-6.952056,8.143642,-7.383007,9.483526,6.225577,-5.011324,-5.458646,-0.370697,5.620118,2.198091,6.452885,-3.117887,6.222870,8.838315,-9.121361,5.225711,-2.865697,9.086284,-6.381680,-0.210459,-3.570574,8.247359,-8.129547,-0.362434,-8.675751,4.772529,-3.287203,8.128046,2.360678,5.622640,-0.338895,-0.715714,4.027318,2.904635,-8.995532,8.547045,-5.846685,1.260742,-9.498097,8.828462,-6.174834,-8.250704,-1.160530,-0.736709,-0.367656,9.058158,-7.135246,7.923933,5.446702,-8.956825,6.248857,1.887856,-6.365323,-4.192763,-4.331328,-7.318919,-9.063940,8.847151,-3.800952,-9.980062,5.293188,0.914197,3.321627,4.507724,0.912093],[-0.509945,6.663040,7.502761,-2.743340,-5.656448,6.765715,4.463233,8.180452,-0.465476,-6.739294,-8.173338,2.397355,-2.213942,7.329178,4.060289,8.789438,7.162827,6.834331,-0.032770,-6.246830,-6.459245,1.298204,9.866636,-2.632121,-8.169089,-1.421793,-7.404033,-7.174086,-4.635555,-5.786294,2.368614,3.528359,-0.924414,6.691918,-6.444376,9.916973,1.486195,6.647619,9.315492,-7.364257,-4.056716,7.360604,-1.501796,6.202226,5.392306,6.715757,2.357939,2.961666,9.927050,7.180369,-9.667450,9.637050,2.400039,-7.662645,-5.068509,8.671341,4.604731,-8.580712,-2.152195,-8.682120,2.943906,-2.448665,-3.120041,5.386174,-6.626051,0.795450,1.358965,-9.439307,4.820025,-6.880738,-8.292276,6.833134,-0.883177,7.619799,1.090025,-5.995907,5.544787,-5.769324,-2.484130,-5.745878,-8.722419,8.317359,-8.254592,-2.474837,-5.451729,6.542262,-1.462030,-5.751216,-4.268307,-9.962685,7.091972,3.072317,3.773812,-4.482405,6.245729,9.979238,-0.086946,2.612024,-5.624290,2.302780,-1.315138,2.234583,8.508735,8.435075,-3.708497,6.472362,-3.540893,-1.129641,-1.210814,4.982605,2.538421,7.945807,2.256034,-8.282617,4.223353,-0.817849,4.226948,-7.556897,5.422851,-8.588360,6.011981,1.023250,-8.855818,-1.310788,-6.784658,-4.222134,-0.521140,-3.803138,3.638035,5.419950,-3.435512,-6.492308,-6.145238,-8.822618,3.034642,4.947656,-3.829520,-2.996179,-8.474459,-0.473180,3.983927,0.277165,-0.120190,9.879113,-4.869310,-0.732721,6.087994,-1.909756,-6.269274,8.391527,-9.206123,-1.824628,-7.091570,8.090179,5.656556,1.404190,0.901336,-6.890367,-2.914739,8.783481,2.381987,0.812448,-1.646677,-1.459650,-2.245025,-4.189717,-0.970661,-8.452279,-7.334175,9.385580,8.675749,-0.200808,0.446903,-6.352505,-0.250240,0.588042,-6.262128,-3.503538,-0.717748,9.947033,3.237245,0.903670,-0.988916,-7.069424,-5.359238,6.590542,-6.357864,-8.682400,-2.708608,-8.833082,-1.982030,-7.090556,-5.265769,4.021086,2.081654,-0.388504,8.511330,-3.728106,7.424659,-8.679943,6.142538,1.555107,0.495008,3.614042,-1.800880,-0.506317,0.215497,1.628373,-0.336175,2.833490,8.168962,-4.878368,0.948198,1.653501,2.403980,-6.720994,6.871879,-2.171293,3.546630,-7.806773,1.932317,-8.661760,-0.314076,5.651273,2.972078,-4.589828,-9.595888,3.819353,-0.028188,-3.853377,-0.821632,-6.510502,-6.053358,-0.933604]], dtype = "float64")#candidate|8579|(5, 234)|const|float64
call_8578 = relay.TupleGetItem(func_8057_call(relay.reshape(const_8579.astype('float64'), [13, 10, 9])), 1)
call_8580 = relay.TupleGetItem(func_8059_call(relay.reshape(const_8579.astype('float64'), [13, 10, 9])), 1)
var_8591 = relay.var("var_8591", dtype = "float64", shape = (5, 234))#candidate|8591|(5, 234)|var|float64
bop_8592 = relay.less_equal(const_8579.astype('bool'), relay.reshape(var_8591.astype('bool'), relay.shape_of(const_8579))) # shape=(5, 234)
uop_8598 = relay.log2(bop_8592.astype('float32')) # shape=(5, 234)
output = relay.Tuple([call_8544,call_8558,call_8562,const_8563,call_8567,call_8575,call_8578,uop_8598,])
output2 = relay.Tuple([call_8545,call_8559,call_8564,const_8563,call_8568,call_8576,call_8580,uop_8598,])
func_8605 = relay.Function([var_8591,], output)
mod['func_8605'] = func_8605
mod = relay.transform.InferType()(mod)
mutated_mod['func_8605'] = func_8605
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8606 = relay.var("var_8606", dtype = "float64", shape = (5, 234))#candidate|8606|(5, 234)|var|float64
func_8605_call = mutated_mod.get_global_var('func_8605')
call_8607 = func_8605_call(var_8606)
output = call_8607
func_8608 = relay.Function([var_8606], output)
mutated_mod['func_8608'] = func_8608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_8621 = func_2162_call()
call_8622 = func_2162_call()
output = relay.Tuple([call_8621,])
output2 = relay.Tuple([call_8622,])
func_8625 = relay.Function([], output)
mod['func_8625'] = func_8625
mod = relay.transform.InferType()(mod)
mutated_mod['func_8625'] = func_8625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8625_call = mutated_mod.get_global_var('func_8625')
call_8626 = func_8625_call()
output = call_8626
func_8627 = relay.Function([], output)
mutated_mod['func_8627'] = func_8627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7494_call = mod.get_global_var('func_7494')
func_7496_call = mutated_mod.get_global_var('func_7496')
call_8631 = relay.TupleGetItem(func_7494_call(), 0)
call_8632 = relay.TupleGetItem(func_7496_call(), 0)
output = relay.Tuple([call_8631,])
output2 = relay.Tuple([call_8632,])
func_8648 = relay.Function([], output)
mod['func_8648'] = func_8648
mod = relay.transform.InferType()(mod)
mutated_mod['func_8648'] = func_8648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8648_call = mutated_mod.get_global_var('func_8648')
call_8649 = func_8648_call()
output = call_8649
func_8650 = relay.Function([], output)
mutated_mod['func_8650'] = func_8650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_8668 = func_4139_call()
call_8669 = func_4139_call()
output = relay.Tuple([call_8668,])
output2 = relay.Tuple([call_8669,])
func_8672 = relay.Function([], output)
mod['func_8672'] = func_8672
mod = relay.transform.InferType()(mod)
output = func_8672()
func_8673 = relay.Function([], output)
mutated_mod['func_8673'] = func_8673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7824_call = mod.get_global_var('func_7824')
func_7826_call = mutated_mod.get_global_var('func_7826')
call_8710 = relay.TupleGetItem(func_7824_call(), 1)
call_8711 = relay.TupleGetItem(func_7826_call(), 1)
func_7552_call = mod.get_global_var('func_7552')
func_7555_call = mutated_mod.get_global_var('func_7555')
call_8714 = relay.TupleGetItem(func_7552_call(relay.reshape(call_8710.astype('bool'), [4, 9, 6])), 0)
call_8715 = relay.TupleGetItem(func_7555_call(relay.reshape(call_8710.astype('bool'), [4, 9, 6])), 0)
func_4381_call = mod.get_global_var('func_4381')
func_4382_call = mutated_mod.get_global_var('func_4382')
call_8721 = func_4381_call()
call_8722 = func_4381_call()
func_2840_call = mod.get_global_var('func_2840')
func_2842_call = mutated_mod.get_global_var('func_2842')
call_8725 = relay.TupleGetItem(func_2840_call(), 0)
call_8726 = relay.TupleGetItem(func_2842_call(), 0)
output = relay.Tuple([call_8710,call_8714,call_8721,call_8725,])
output2 = relay.Tuple([call_8711,call_8715,call_8722,call_8726,])
func_8732 = relay.Function([], output)
mod['func_8732'] = func_8732
mod = relay.transform.InferType()(mod)
output = func_8732()
func_8733 = relay.Function([], output)
mutated_mod['func_8733'] = func_8733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_8739 = relay.TupleGetItem(func_2570_call(), 0)
call_8740 = relay.TupleGetItem(func_2571_call(), 0)
output = relay.Tuple([call_8739,])
output2 = relay.Tuple([call_8740,])
func_8808 = relay.Function([], output)
mod['func_8808'] = func_8808
mod = relay.transform.InferType()(mod)
output = func_8808()
func_8809 = relay.Function([], output)
mutated_mod['func_8809'] = func_8809
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8819 = relay.const([[[0.049790,2.035707,5.288370,8.428107,1.741548],[-5.321377,4.258636,-7.977532,0.496035,-3.115991],[-5.310666,0.855372,1.994050,-0.549967,1.868071],[4.694548,-2.751616,-2.359016,-6.890829,-0.099830],[6.448791,6.427793,4.013010,2.682786,0.076435],[-4.083352,8.737082,-9.687884,9.936330,1.781513]],[[-7.506159,-9.243181,8.608455,-9.772586,-7.231613],[3.661092,-4.525689,-1.644372,4.063325,-7.088503],[-6.546810,-1.538313,-8.929478,-4.481991,-0.937243],[2.678875,2.072678,7.299950,-1.530570,-5.456870],[-4.082065,-7.639909,-9.537779,9.103582,4.386424],[4.240208,-8.892483,1.115218,-8.906601,1.530313]],[[1.886292,3.440576,-5.300386,6.037203,-1.842879],[6.231643,-7.741863,1.735549,-2.502727,-7.715616],[-6.370593,4.988877,5.374668,-5.039452,3.506165],[-8.536456,-1.691746,7.626874,-7.651612,8.982442],[-4.406440,-8.119231,7.057565,9.365565,-6.415925],[2.537521,1.555901,4.193107,6.453202,-0.983080]],[[7.148651,3.144165,-3.298219,-1.654820,9.713172],[-7.680879,-7.909496,-3.793611,-5.415436,-7.768637],[9.852864,-5.713940,-3.353595,-3.407450,3.965913],[-9.130638,8.975256,-0.654788,-5.758156,8.411849],[-4.963478,4.176682,-2.599553,-6.119988,-7.261667],[1.598371,-6.474360,-8.005006,1.406158,-8.220495]],[[-2.375169,-4.133354,-6.581477,5.272278,3.669779],[5.639481,-7.230915,2.777490,-4.839976,-3.192434],[-6.767760,8.039689,4.198353,3.316774,-4.551482],[9.702127,0.836342,-5.645402,-1.957981,-3.520185],[-2.342385,9.335435,1.943050,1.285230,2.451785],[-7.407965,6.530497,-7.184062,2.793248,-8.303168]],[[-8.819523,-0.547681,1.609243,5.696833,3.200796],[2.928834,9.831681,-8.185838,5.847070,4.786598],[1.797806,-3.693265,0.512828,9.438852,9.500482],[-9.534312,8.191830,1.529407,5.156833,-5.872844],[-2.011670,1.173577,8.715940,-7.237279,6.610086],[9.807452,0.711198,-8.271763,-0.231761,-5.832523]],[[7.824618,0.536706,7.697906,9.175359,-4.213943],[5.827845,2.527131,-6.091473,3.778062,-5.600417],[-1.199751,6.789802,5.878965,-5.424358,-6.206907],[1.984832,1.678585,-9.016575,4.110633,-9.451898],[-9.562716,1.884776,-5.399324,-9.515688,-9.100424],[-1.781103,-7.825124,1.556080,5.091189,8.849186]],[[-2.520959,6.499424,-7.521110,-4.165108,6.013902],[3.753105,7.956044,-3.469508,-2.434857,9.532132],[2.861974,-8.825380,9.164186,8.867329,7.963779],[-8.007647,-0.210342,-8.486825,-5.210303,-1.068306],[4.939302,3.472627,-1.900459,-5.131365,-9.750038],[-8.009161,6.340504,7.950959,-3.821529,-6.697250]],[[7.897779,3.519817,-7.352232,-5.263418,-6.400632],[5.094221,-4.433513,-0.177017,-5.411559,-7.737722],[-0.605420,-8.407129,3.785281,9.243663,-6.213421],[6.519558,-3.596156,4.985222,-9.223185,3.881768],[6.597080,-6.103709,6.463731,-3.217678,1.152746],[-2.067813,0.564808,-2.298176,-2.398601,-9.581995]]], dtype = "float32")#candidate|8819|(9, 6, 5)|const|float32
uop_8820 = relay.atanh(const_8819.astype('float32')) # shape=(9, 6, 5)
output = relay.Tuple([uop_8820,])
output2 = relay.Tuple([uop_8820,])
func_8829 = relay.Function([], output)
mod['func_8829'] = func_8829
mod = relay.transform.InferType()(mod)
mutated_mod['func_8829'] = func_8829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8829_call = mutated_mod.get_global_var('func_8829')
call_8830 = func_8829_call()
output = call_8830
func_8831 = relay.Function([], output)
mutated_mod['func_8831'] = func_8831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7425_call = mod.get_global_var('func_7425')
func_7427_call = mutated_mod.get_global_var('func_7427')
call_8857 = relay.TupleGetItem(func_7425_call(), 1)
call_8858 = relay.TupleGetItem(func_7427_call(), 1)
output = call_8857
output2 = call_8858
func_8863 = relay.Function([], output)
mod['func_8863'] = func_8863
mod = relay.transform.InferType()(mod)
mutated_mod['func_8863'] = func_8863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8863_call = mutated_mod.get_global_var('func_8863')
call_8864 = func_8863_call()
output = call_8864
func_8865 = relay.Function([], output)
mutated_mod['func_8865'] = func_8865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8426_call = mod.get_global_var('func_8426')
func_8427_call = mutated_mod.get_global_var('func_8427')
call_8866 = relay.TupleGetItem(func_8426_call(), 0)
call_8867 = relay.TupleGetItem(func_8427_call(), 0)
func_1786_call = mod.get_global_var('func_1786')
func_1790_call = mutated_mod.get_global_var('func_1790')
const_8887 = relay.const([-9,-10,6,-2,2,-7,2,4,2,5,2,-2,5,6,9,3,10,2,5,-4,5,-6,7,-4,1,10,9,4,5,3,9,-5,1,7,-1,-3,-2,-7,10,-8,1,6,10,-3,2,-3,3,-2,-3,-8,-7,5,9,-8,3,2,4,3,8,10,-3,-2,9,9,-10,8,-10,-9,-5,10,5,-2,-9,-2,5,8,-3,2,-4,-5,2,6,-8,-2,3,1,-5,-8,1,3,2,-2,10,8,-9,-10,6,-2,10,7,8,-1,2,9,-9,-7,-4,7,-5,9,6,4,3,4,1,-7,9,4,-9,-3,5,-1,-1,4,3,-9,-3,9,-8,-1,6,8,8,-5,6,9,-9,2,-1,5,10,-1,8,8,4,-5,-7,-6,-6,6,-10,-5,5,1,6,10,-2,6,2,8,-1,-6,7,-5,-4,8,6,-5,3,-7,-3,-2,7,-7,-1,-4,-7,5,6,-10,1,-4,-1,7,4,2,10,-2,-1,-7,3,9,4,5,-3,10,-5,8,3,10], dtype = "int8")#candidate|8887|(200,)|const|int8
call_8886 = relay.TupleGetItem(func_1786_call(relay.reshape(const_8887.astype('int8'), [10, 2, 10]), relay.reshape(const_8887.astype('int8'), [10, 2, 10]), ), 0)
call_8888 = relay.TupleGetItem(func_1790_call(relay.reshape(const_8887.astype('int8'), [10, 2, 10]), relay.reshape(const_8887.astype('int8'), [10, 2, 10]), ), 0)
output = relay.Tuple([call_8866,call_8886,const_8887,])
output2 = relay.Tuple([call_8867,call_8888,const_8887,])
func_8893 = relay.Function([], output)
mod['func_8893'] = func_8893
mod = relay.transform.InferType()(mod)
output = func_8893()
func_8894 = relay.Function([], output)
mutated_mod['func_8894'] = func_8894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mod.get_global_var('func_4641')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_8924 = relay.TupleGetItem(func_4641_call(), 1)
call_8925 = relay.TupleGetItem(func_4642_call(), 1)
output = call_8924
output2 = call_8925
func_8932 = relay.Function([], output)
mod['func_8932'] = func_8932
mod = relay.transform.InferType()(mod)
output = func_8932()
func_8933 = relay.Function([], output)
mutated_mod['func_8933'] = func_8933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_8952 = relay.TupleGetItem(func_6769_call(), 2)
call_8953 = relay.TupleGetItem(func_6771_call(), 2)
const_8959 = relay.const([[-6.209291,-5.244391,-9.727506,-0.774289,-6.287507,9.539000,7.621439,3.814338,7.597464,-7.666288,-5.101272,-2.257083],[3.643931,-0.686902,-4.323707,-6.431265,6.162151,9.915022,-8.553297,-7.845134,-8.233342,2.871661,2.363172,9.436139],[-3.464749,8.996487,8.490460,7.811373,6.003096,-3.011994,5.675383,-1.722576,7.895697,-3.650281,7.797296,-8.205642],[-9.663506,6.900668,-5.140901,-6.902375,1.685643,-0.207067,-1.940894,1.830727,9.249270,4.359192,-0.390273,8.592996],[6.428191,0.910252,6.073922,1.818695,-2.073636,7.512466,4.038850,6.134025,-0.736334,7.200683,2.237914,-6.586858],[-5.713327,1.847331,3.368605,-9.399980,9.963768,3.091661,-4.647853,-1.790330,-5.139210,4.249005,-0.680284,-7.549432],[-7.629937,9.846199,-6.244214,-9.871676,8.978302,0.955160,7.634259,0.568519,-8.946561,2.530093,7.038497,7.739197],[7.430367,-9.396828,4.864444,-6.909242,-6.448267,0.575026,3.484431,-7.410005,3.055281,6.248272,4.680450,6.526131],[-4.913313,-1.215307,3.109677,4.767786,8.712635,-4.323864,-4.445206,-7.095060,-3.534603,5.450514,-1.293677,-3.788350],[0.214330,-6.374527,-3.318933,-8.532253,-0.484795,8.730827,-9.061813,-2.191878,-9.834441,-7.170867,-9.366822,2.776358],[-6.499013,-5.410135,-3.347701,7.370428,6.130799,7.139894,6.977516,-4.002035,-5.877173,5.677065,-1.920296,-2.256396],[-4.833022,1.987711,-3.069894,4.849922,0.826132,4.304620,-5.694010,2.420299,-5.588485,-0.046385,0.796977,5.612420],[-4.335965,-3.541220,-2.500356,0.091541,-3.487014,2.941628,5.244961,1.386684,1.170423,9.176824,7.140561,1.351830],[5.072717,-4.352907,-0.156365,-2.448675,-0.617195,1.713243,-3.067603,-8.317275,1.212595,9.159593,-2.832477,2.273219],[1.164504,-4.499105,3.152441,-4.287357,6.959829,6.742342,-1.613249,-3.101159,0.977434,5.633074,-5.858826,-1.731034],[-5.347447,-9.493495,-1.359922,-0.133463,-9.617430,3.416181,-1.197231,-4.402055,-4.004953,7.942984,-0.411032,7.896716],[1.271283,4.130854,-1.689589,0.837148,1.633959,-3.929400,5.949007,2.823920,8.059170,6.541394,-8.202649,6.181227],[-3.894971,7.315532,-5.437788,-0.475022,0.577094,4.883629,4.353895,-2.058790,-6.238446,-0.157344,8.406949,-8.596929],[-1.299868,-5.516590,7.170730,0.602407,-6.806364,-4.320652,-5.944261,-3.970025,-7.093020,9.746727,-8.787689,-2.489650],[-4.773546,-0.886546,-6.941697,-9.112922,8.543626,2.222841,-7.643074,-1.452677,1.436827,6.218982,6.954946,-1.355152],[1.725250,1.319848,1.664764,6.618560,-0.257944,-7.392232,-6.867146,-2.642640,3.338833,-1.000961,-4.071474,2.712957],[-9.999471,1.448474,-9.533220,8.065305,-7.170494,-1.366376,0.640292,3.503273,7.344147,-6.023747,5.022788,8.353672],[8.865924,-2.520469,-7.302601,8.018241,3.307261,-4.037629,-0.090566,5.274745,-5.326804,2.704976,2.286126,-5.487544],[-6.130806,-6.267042,8.693393,-2.587719,-9.501703,-5.881727,-3.036895,0.653485,2.525960,-3.174238,5.363928,-1.166345],[1.882094,0.189029,-1.675166,0.519859,9.657611,-7.093058,-4.116771,5.249674,-3.926579,0.220166,4.163700,-2.228017],[7.550233,3.244468,-3.269072,-6.883598,7.850292,3.332558,4.450719,-9.502772,-0.330017,9.895361,4.783232,1.560563],[5.389747,9.262413,8.248212,9.445022,-4.791777,-6.581502,-0.194421,-8.591891,-9.630136,4.489540,-0.305666,-7.343473],[3.925219,1.746595,-5.653253,-7.420672,-6.865909,5.567244,2.854983,-7.354978,4.458032,-3.080272,7.443126,3.806535],[-9.686426,-5.752971,-7.647300,-1.854518,-0.689708,-4.909576,-9.719294,-1.489463,-5.168052,4.369076,-1.534541,8.602848],[-1.667951,5.732741,-9.864177,5.899743,-5.523811,-2.033179,7.862349,-5.506343,-5.065789,-4.264627,6.040454,0.689975],[-8.301875,2.560270,-9.494825,-0.796717,-8.340313,2.207673,-1.756595,-1.038362,-4.842207,4.521131,1.362728,0.308183],[5.734358,-6.779656,1.735703,-6.962477,-3.091099,-9.778567,7.851050,5.191591,7.235295,-0.855988,-1.978254,-1.680992],[9.858889,-7.352336,6.722656,2.082770,2.724713,1.056354,6.690031,8.794570,9.568102,9.753717,-2.042579,-4.513529],[1.186726,-6.986311,6.616279,-1.340485,-8.343686,1.134724,-5.092804,-9.307234,9.665580,-4.700108,-3.236453,-4.002144],[-8.881175,-9.472071,9.430945,-0.286791,0.438207,-7.130971,2.554415,-8.798422,1.339161,3.848950,-6.742842,1.576073],[1.875739,-3.704697,4.470758,4.242232,-6.714667,8.460709,-3.474284,-9.303079,-2.754994,7.580104,6.193180,3.781122],[0.092577,6.775999,4.263738,9.685755,-5.818043,-0.081704,3.417146,3.648726,2.510774,1.092785,-8.601360,5.453311],[-7.638741,-8.876810,-2.232151,-0.680325,-4.370545,4.486196,-0.601475,-5.080025,2.125926,6.910265,-6.146353,-7.280555],[4.550835,-3.619244,-7.597744,-9.887922,-4.604148,-4.890561,-8.629193,-1.572189,-5.767592,-0.206198,6.639539,-9.565952],[0.426100,5.815562,-2.873610,8.623431,1.002362,-5.096293,-7.244941,-0.494963,5.116984,1.714989,9.466119,2.680575],[-4.539242,-8.900460,-0.075812,-8.265750,-8.502180,-5.083743,1.287874,-2.824054,9.003580,-3.073302,0.393837,-5.395195],[-4.085845,1.405285,2.795173,1.617637,-6.957661,3.976548,-8.549678,0.219896,1.499043,-9.126260,3.813784,5.828343],[5.081724,-9.000816,-9.836589,7.526610,9.142010,-7.740114,6.353456,-1.225557,-3.656193,9.121178,8.270076,1.052606],[-0.277021,0.695881,4.419489,-5.588924,8.344320,2.894661,1.741590,-2.018175,0.327758,7.961066,-3.517228,1.727658],[-9.015166,-8.898196,9.482940,-8.021260,0.641270,0.893586,4.477946,3.858552,7.277264,-4.884109,1.235223,1.790625],[-9.998938,-6.116783,-9.737846,1.956111,-1.164835,-9.171505,6.417462,4.886623,-8.931544,9.421396,-9.611133,-9.033686],[-6.192341,-2.716562,6.993583,-8.638035,-0.631568,8.749263,-7.357894,1.496019,-6.170338,-8.071370,3.867624,-1.328205],[6.400792,7.901741,-3.681372,6.682265,-1.813854,-7.983176,5.108831,5.258281,8.768719,-6.791974,6.806037,-3.352848],[2.807699,-4.146211,-7.229526,-7.712477,-3.612079,8.749895,-2.071773,1.574447,-9.634807,-0.354099,2.108769,-7.272744],[-4.075531,-9.254324,-8.092239,6.283730,-3.553079,-1.503267,-4.030747,-6.606733,-3.564586,0.203855,-8.330809,-2.768739],[2.863464,-9.126686,-5.087385,4.826731,6.013655,0.230925,1.057490,5.890074,-9.584078,-8.666090,-7.078569,2.338555],[8.422295,7.781024,-1.399638,-1.744163,8.814490,-8.078083,6.294281,-6.345709,3.241623,2.047390,7.295633,-5.484699],[-3.449743,-6.712211,2.523538,-9.027071,0.876335,-5.050661,2.882610,8.781937,9.981467,-9.954712,1.739841,3.034043],[-4.118977,6.723145,0.417144,8.812974,3.923303,7.221652,-7.400659,4.709661,8.560205,7.781374,-9.719101,4.667559],[-2.934011,3.071302,2.262626,-2.014275,4.549755,4.959588,-0.086866,-6.424037,-7.588920,-6.215806,2.980617,-4.244082],[-2.578486,4.046704,-4.498117,-4.204989,1.200326,3.826292,0.379696,-4.671483,9.113356,4.989154,2.821382,5.780664],[3.521060,-6.250575,8.789179,-7.024666,-8.721118,1.103056,-1.541958,5.985623,7.445103,-5.923429,-0.052840,5.455959],[-3.859837,6.451006,-2.266717,-6.429637,1.171295,3.338698,1.037155,-7.692884,9.213542,0.380503,1.372945,5.995917],[1.374543,6.646498,5.212460,4.264871,-0.613426,5.857978,-6.353044,-1.699741,-8.246239,-3.238418,2.754569,6.525876],[-6.754090,4.816429,3.404103,-7.805229,-7.741229,-7.522297,-0.434507,-1.720483,7.835362,-3.301947,5.763876,5.494899],[-3.958798,6.915950,-5.964647,-4.398706,9.412210,-2.181457,0.634185,0.264752,6.779407,4.644845,-7.425298,-4.578257],[0.580206,2.318891,6.748526,-9.703266,-1.794196,-7.656802,-5.073111,-4.883366,-5.119401,-4.323331,6.516700,5.660746],[5.075955,7.701629,-6.074874,2.371610,-0.321382,-9.752584,7.587596,4.050609,4.818783,-6.623809,-5.433347,2.621712],[-0.363440,-7.662537,-0.559622,-0.812962,-5.767007,6.088282,0.860329,-2.608174,2.178947,2.186044,3.240988,-5.624499],[-0.542244,-9.909467,7.002690,3.749234,8.662749,-9.858288,-1.163582,-2.728438,-5.989568,5.101944,-7.936383,7.779359],[5.774869,9.402476,2.835105,4.796506,-8.885360,-4.500300,3.950149,3.409021,-2.465331,-5.893939,-1.220236,4.186707],[-4.812017,-6.633897,7.495740,-5.139185,3.592247,6.487203,-9.169407,-1.986981,6.837150,-3.383889,4.737762,0.415260],[5.205260,-0.145478,-4.412017,-0.288945,-8.159920,-5.836020,-6.692444,-7.872737,-7.915893,-0.286670,-6.033125,8.139367],[-0.507672,7.661341,-0.901473,3.069344,-0.750943,3.615473,4.125489,-7.054842,4.204822,9.360234,6.050950,4.757340],[-3.252282,-3.654064,-3.245434,-1.435821,-0.317432,-9.162434,-4.289509,-2.798103,7.046341,-5.926633,-2.086078,3.930725],[5.496032,6.869466,-9.864549,-9.984902,3.044926,-4.180987,-0.846724,-7.047173,-7.534163,4.513127,-0.557776,2.940770],[-3.728848,-9.815249,-4.382654,-8.534975,9.963129,5.072381,-6.749638,-9.149138,-7.072334,4.751103,5.454528,4.772048],[5.069590,-9.045840,8.099696,7.860454,3.769320,-8.650260,6.218747,2.539396,-6.844425,4.006462,-1.749332,-2.906899],[-3.411803,-9.512376,7.488460,4.323426,-7.983735,-0.764487,9.955675,5.619153,-1.544172,2.316013,-2.963138,-5.155954],[0.972693,8.393815,7.182235,-3.434558,-0.834542,7.034103,2.016735,-0.772762,-7.523152,3.205248,-6.384562,4.192156],[-7.366535,7.767660,6.186743,6.092072,1.496779,6.037835,6.436916,-4.079442,-4.814878,2.121991,-1.438608,1.744367],[6.763744,-5.008013,-1.093064,-9.577158,-6.424109,2.050169,5.539492,-3.736280,-3.659972,5.872652,-7.451088,9.382488],[0.333175,-2.113004,-7.558652,-3.250409,-9.018076,7.089120,-1.297537,1.579067,7.607087,0.814391,3.226914,2.979189],[5.703080,8.680432,-8.870006,-5.058438,-1.699161,4.919838,-6.662570,-9.426987,0.725210,7.878563,7.820323,-0.265173],[-8.664680,4.617095,-7.190841,6.905263,4.837332,0.488712,1.086975,0.403638,-8.469371,-1.296476,-7.178396,4.418036],[-6.355851,-5.144852,2.450132,9.691047,-0.798338,4.179962,5.739349,-3.104595,-7.219923,5.225143,5.936246,3.833546],[6.237545,-7.768056,-9.971715,6.804904,9.301399,-1.908386,6.231949,-1.292791,-3.892645,-1.790633,-3.934847,-7.635199],[-5.676058,-7.785891,-4.283901,6.558059,9.622186,3.131647,5.261056,-2.261732,-2.167046,3.155209,-7.366635,4.410687],[0.141854,5.330376,-3.910411,-0.542221,5.669805,-6.399050,-4.033746,4.122066,-3.286943,4.454480,-6.567166,-0.955631],[-3.933848,-3.669879,3.420031,5.625071,1.139128,-6.205376,-5.614068,-7.829457,7.196643,7.723642,-7.442207,7.003749],[-4.562437,-1.490750,-9.858177,0.266053,-4.755904,-5.214989,-0.754250,-5.720523,-5.993418,9.564552,-4.906275,-2.541276],[6.396910,5.929605,-0.805877,-5.182822,-5.118635,7.261379,3.269581,5.009579,-7.374886,3.789765,-2.368440,-7.060387],[-7.653802,6.877430,2.436210,-2.596110,-3.267333,-9.458294,-8.125432,0.324338,9.082333,6.150470,5.168930,-2.443232],[-4.728132,-6.540945,-3.637344,9.883728,8.702422,2.870399,-1.361807,0.054957,2.766899,-9.239439,-2.801898,-8.200545],[-6.137207,-6.548699,5.943498,-6.772461,-1.513998,-3.768052,1.104009,8.187916,-9.625385,-2.302500,-5.771125,8.511821],[7.404291,7.269565,5.469425,-2.084860,1.368183,-6.797570,2.700140,3.987909,7.925940,-4.816729,2.471304,0.283116],[-9.016651,4.650814,6.667313,0.620662,-4.096838,-8.924983,-6.860044,7.810716,7.800740,-3.187349,-1.638944,-0.432947],[5.640807,0.599969,-0.242621,3.564498,-6.617667,8.523915,3.457269,-1.705517,0.771125,-8.800145,3.848409,-0.612053],[8.891584,-2.492486,-7.668747,1.404486,1.453229,-6.427869,-8.087915,9.352710,-1.571815,-4.877553,1.114695,3.220997],[-8.204461,-7.698947,-4.964982,-1.619377,-3.411942,4.399600,-4.394981,-7.561360,4.029795,6.079985,-5.152983,-7.422813],[-0.248864,2.729314,-3.000356,-9.604153,-2.903013,-0.234199,1.608665,-8.787712,7.241719,-1.899967,-3.212734,-3.568213],[-7.760076,6.731347,-8.850409,6.011060,5.595214,-0.108335,-9.685282,-3.691951,8.304842,1.197996,1.051868,-6.771843],[7.657387,-6.589055,-3.470802,-0.251965,4.413110,3.306731,7.171571,-1.192653,1.644030,-6.413209,0.359461,-0.354653],[-3.025928,-8.813857,7.795232,-9.664816,1.153698,9.828070,0.522944,-7.145433,6.833401,-1.096864,1.333109,1.660832],[7.142237,-8.855898,-5.961274,-8.460593,-6.031273,8.553027,1.765866,-0.585462,-8.173963,-0.259718,0.862559,-9.836809],[0.232810,-7.092554,1.134444,9.286052,4.342435,-7.295617,1.909240,-9.580286,5.169241,9.183338,-6.567142,3.402873],[3.450562,-5.613861,8.868078,-4.193417,-6.666925,8.319443,-6.472305,-0.978421,-7.272775,-9.449294,7.796640,5.479125],[-4.229525,-6.508997,-9.720588,9.129627,8.288000,7.756808,6.935723,9.286406,-5.650475,7.474063,-1.704002,-2.405949],[-9.897006,-0.992813,-2.990256,-4.458040,-1.444624,1.802453,0.930809,9.174417,-5.074720,1.226223,-3.444973,4.140840],[7.473583,6.824708,5.067377,-7.570911,-4.239757,6.554209,-2.509141,3.780343,-3.909743,1.857795,-3.906182,4.262668],[2.359360,-9.778402,3.999774,-1.034487,-8.043550,-7.714341,-0.166684,-0.431779,5.090347,1.343416,8.127906,8.895841],[8.652564,2.004525,4.820108,-8.311009,7.950037,-7.791420,9.406403,3.883037,-3.968582,9.999246,-8.781905,-8.903645],[1.647800,5.887111,-7.592099,4.722118,-7.680358,9.768792,0.335183,-5.435382,-0.069926,0.378384,-4.728068,-6.687764],[0.827681,2.572913,5.822654,8.159395,9.543204,0.032318,7.072131,8.605105,-4.736498,3.397276,-9.023699,-0.317347],[-8.528020,-7.133290,0.149705,-4.610748,-2.578839,-1.011518,9.935538,3.466357,8.300015,-5.785599,8.022682,-9.784967],[1.935314,4.437658,3.276033,-0.795726,6.170566,-0.246955,1.853768,2.458125,-5.130970,1.677938,-4.802010,-1.014934],[-8.803584,-1.329209,-4.165715,1.796557,6.645352,-4.536110,-9.294165,-9.090217,3.044259,-8.217802,4.207921,0.774505],[-4.682134,0.215764,5.780809,-6.835057,9.566737,6.537784,1.762098,3.780669,7.639155,4.903723,-1.739788,8.284276],[5.234568,4.098431,-2.965183,-7.528227,6.261210,2.417907,-6.813464,-0.809270,-4.118798,2.903232,-4.161121,-3.886148],[-3.766455,-7.990932,-7.332583,9.428573,3.801624,-7.258941,9.938989,-2.024312,4.863080,8.668766,1.865648,1.315847],[7.337259,3.154935,0.212010,1.513367,-7.540698,-5.185972,3.738637,-6.230491,-4.672596,-1.516096,7.178272,7.517827],[-3.129545,-6.349418,-5.213606,-3.349892,2.336966,-9.646616,9.791630,-4.988618,9.574038,-6.206867,-4.262774,7.470544],[-6.062071,-3.909736,1.161214,-5.426396,-6.407292,3.039849,-5.510174,-8.184142,-8.061496,-2.751089,-4.084329,7.220920],[5.539549,0.434872,-2.425018,6.541703,-4.479723,-7.631208,6.185801,-8.607527,-7.496109,-4.481679,5.388561,-4.061393],[8.901414,7.896765,2.406752,6.353121,6.599174,6.744374,-2.411287,-9.399473,-2.614627,-2.069417,3.098227,-3.701393],[-8.717296,-3.150536,5.065449,5.842862,9.028502,4.582234,0.572131,5.526086,6.269725,-9.773039,0.590366,-0.491163],[-1.248776,5.708391,0.258743,3.438199,2.542352,0.685126,-9.166651,6.697690,-7.861576,-2.230378,-9.354162,-3.120308],[-6.288185,5.902122,5.612760,-2.494784,-7.826411,3.176649,0.741125,5.185929,-0.110798,3.790596,-6.614523,-7.760504],[5.143908,-8.696446,-8.047690,3.087739,-4.415162,2.455206,9.660862,6.036187,3.669201,6.649397,9.098738,2.861433],[-6.920647,-1.843251,-4.120012,4.281698,4.167383,2.213812,-4.412291,3.597167,7.825133,-9.296493,-4.273382,-6.787737],[-3.224565,-6.208618,-7.814699,3.533513,-2.959298,1.931398,-5.217828,7.171690,8.786250,6.954026,6.372942,-2.435340],[7.801576,6.029295,-2.687669,-6.154101,-8.100473,-8.466782,-3.435300,9.398820,9.523286,7.101636,9.868027,5.882332],[8.075998,-6.226535,1.620667,6.781986,3.015129,-3.693387,-7.641861,-9.962757,2.636003,-7.784995,-5.974139,6.793950],[-9.028828,0.059611,7.151813,-6.575367,5.211105,2.825994,1.790023,-3.921834,-1.334450,-4.968347,3.923785,5.269751],[5.356081,-7.961940,8.815141,0.785269,3.288258,4.871975,-5.731585,7.498743,-9.516306,-3.682225,-9.392678,-0.414080]], dtype = "float64")#candidate|8959|(130, 12)|const|float64
bop_8960 = relay.power(call_8952.astype('float64'), const_8959.astype('float64')) # shape=(130, 12)
bop_8963 = relay.power(call_8953.astype('float64'), const_8959.astype('float64')) # shape=(130, 12)
func_2491_call = mod.get_global_var('func_2491')
func_2496_call = mutated_mod.get_global_var('func_2496')
var_8966 = relay.var("var_8966", dtype = "float32", shape = (96,))#candidate|8966|(96,)|var|float32
var_8967 = relay.var("var_8967", dtype = "float32", shape = (1440,))#candidate|8967|(1440,)|var|float32
const_8968 = relay.const([[-7,10],[-10,-1],[3,5],[-6,6],[8,6],[1,-6],[2,10],[6,-1],[-8,4],[-10,-2],[-9,-10],[7,-4],[-2,-6],[6,9],[4,1],[-1,2],[-3,-7],[5,10],[8,9],[-8,2],[-3,4],[-10,9],[-4,5],[3,5],[8,-1],[-5,7],[2,1],[-8,1],[-3,3],[2,1],[-4,-1],[8,5],[10,-8],[-8,10],[-2,-10],[-6,-4],[-10,4],[10,-7],[-4,1],[4,7],[-3,-1],[-2,1],[-2,4],[3,-6],[-6,-6],[8,1],[2,3],[2,-10],[-6,4],[-1,-2],[5,10],[-6,5],[-7,-8],[-4,6],[-5,-2],[10,9],[-4,-6],[9,10],[5,-6],[-6,-1],[-3,9],[-8,-3],[-5,-9],[10,1],[-3,1],[-4,-8],[10,-8],[-4,-1],[-5,-4],[5,-7],[4,-3],[4,-10],[-10,8],[1,1],[-7,-10],[-7,8],[1,-7],[9,5],[10,10],[4,10],[1,8],[-4,-7],[-7,4],[8,-5],[5,-3],[8,10],[10,3],[-1,9],[-10,8],[-5,7],[-2,5],[-4,-6],[4,3],[-1,-9],[4,6],[4,-9],[-2,10],[-10,1],[-9,-1],[-7,-10],[-10,5],[6,4],[-8,5],[-6,8],[-1,-7],[-7,-4],[-5,7],[-4,4],[-10,5],[3,-5],[-2,4],[-7,7],[-3,9],[-3,6],[10,1],[-2,7],[-6,-7],[-4,1],[-5,3],[7,9],[4,-10],[3,-6],[-1,6],[-2,5],[-5,-6],[-5,2],[-1,-1],[3,-8],[10,-6],[6,-7],[-7,-2],[3,-8],[10,-5],[2,-4],[-2,-1],[8,4],[7,-2],[-9,2],[1,-8],[1,-3],[1,-5],[-7,8],[-5,6],[6,3],[9,-8],[4,8],[-4,-2]], dtype = "int64")#candidate|8968|(147, 2)|const|int64
call_8965 = relay.TupleGetItem(func_2491_call(relay.reshape(var_8966.astype('float32'), [6, 16, 1]), relay.reshape(var_8967.astype('float32'), [6, 16, 15]), relay.reshape(var_8967.astype('float64'), [6, 16, 15]), relay.reshape(const_8968.astype('int64'), [294,]), ), 6)
call_8969 = relay.TupleGetItem(func_2496_call(relay.reshape(var_8966.astype('float32'), [6, 16, 1]), relay.reshape(var_8967.astype('float32'), [6, 16, 15]), relay.reshape(var_8967.astype('float64'), [6, 16, 15]), relay.reshape(const_8968.astype('int64'), [294,]), ), 6)
func_1885_call = mod.get_global_var('func_1885')
func_1888_call = mutated_mod.get_global_var('func_1888')
var_8972 = relay.var("var_8972", dtype = "float32", shape = (216,))#candidate|8972|(216,)|var|float32
call_8971 = func_1885_call(relay.reshape(var_8972.astype('float32'), [3, 12, 6]))
call_8973 = func_1885_call(relay.reshape(var_8972.astype('float32'), [3, 12, 6]))
output = relay.Tuple([bop_8960,call_8965,var_8966,var_8967,const_8968,call_8971,var_8972,])
output2 = relay.Tuple([bop_8963,call_8969,var_8966,var_8967,const_8968,call_8973,var_8972,])
func_8976 = relay.Function([var_8966,var_8967,var_8972,], output)
mod['func_8976'] = func_8976
mod = relay.transform.InferType()(mod)
var_8977 = relay.var("var_8977", dtype = "float32", shape = (96,))#candidate|8977|(96,)|var|float32
var_8978 = relay.var("var_8978", dtype = "float32", shape = (1440,))#candidate|8978|(1440,)|var|float32
var_8979 = relay.var("var_8979", dtype = "float32", shape = (216,))#candidate|8979|(216,)|var|float32
output = func_8976(var_8977,var_8978,var_8979,)
func_8980 = relay.Function([var_8977,var_8978,var_8979,], output)
mutated_mod['func_8980'] = func_8980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2029_call = mutated_mod.get_global_var('func_2029')
call_8995 = relay.TupleGetItem(func_2027_call(), 0)
call_8996 = relay.TupleGetItem(func_2029_call(), 0)
output = relay.Tuple([call_8995,])
output2 = relay.Tuple([call_8996,])
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
func_2595_call = mod.get_global_var('func_2595')
func_2596_call = mutated_mod.get_global_var('func_2596')
call_9035 = func_2595_call()
call_9036 = func_2595_call()
output = call_9035
output2 = call_9036
func_9038 = relay.Function([], output)
mod['func_9038'] = func_9038
mod = relay.transform.InferType()(mod)
mutated_mod['func_9038'] = func_9038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9038_call = mutated_mod.get_global_var('func_9038')
call_9039 = func_9038_call()
output = call_9039
func_9040 = relay.Function([], output)
mutated_mod['func_9040'] = func_9040
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9084 = relay.const([[[-4.147510,-0.677663,8.579943,-2.437502,-1.534506,7.202551,-8.860652,3.854303],[8.738523,0.856430,-4.027090,-1.475255,9.621303,-7.927064,0.068446,-2.550650],[-7.522280,-1.256710,-5.920786,1.072638,2.861521,-4.264934,3.672589,-7.425682],[-4.048732,5.917006,8.573258,-3.567715,5.324415,-0.015231,-5.347097,1.959746],[0.891787,-1.172202,-4.917340,9.030015,-3.017909,-4.609954,3.307429,-8.587597],[-7.431842,-5.924901,1.149428,-1.960852,-8.192544,-1.407527,8.241574,7.910923],[7.124113,-0.046549,8.556139,-1.360714,1.558504,1.132169,7.844691,-7.360346],[-4.111950,3.802400,8.669991,-1.569069,-8.465036,-2.844649,-3.750733,-9.179674],[-8.706589,-6.631132,-4.159624,0.605310,4.067719,-7.340582,5.571563,-6.978764],[-0.917299,0.597859,0.468290,9.538724,-0.176017,5.546241,6.315646,6.622437],[-8.586234,6.183494,-0.964386,5.279751,6.938159,-9.952095,-4.376037,-7.300181]],[[-5.550963,2.481110,-6.921791,4.129166,-6.486355,5.921077,-4.594361,4.810099],[-2.699604,-7.350833,-0.164996,-9.198063,2.540908,-2.221538,7.610900,-3.285045],[-6.932945,9.601721,-1.960901,-6.737456,1.065196,-5.232392,-3.939352,1.612529],[-1.041713,0.275565,7.644517,4.081811,-0.344789,-7.726764,-9.440133,5.926189],[-2.541147,7.200542,6.924906,-5.856748,-3.273767,-0.908065,-8.950659,9.805704],[6.393851,0.760384,2.208923,-0.669042,-1.414066,9.411891,9.543905,-3.916002],[-7.973849,0.342278,8.913108,-3.699532,-3.407703,-6.014545,-0.774416,-7.962060],[-1.508805,-5.158478,-5.404950,8.773121,-6.217113,7.284727,7.145324,5.198606],[-4.653304,9.151102,-2.333125,1.241614,-7.579436,-6.913069,1.182299,3.655800],[-5.876219,7.493845,-5.189184,-3.782939,-1.487404,-9.324699,4.407982,4.234254],[-7.890267,0.240462,-6.356206,-2.316764,-2.449830,-8.422202,2.006292,1.267140]],[[9.791437,-1.817554,7.832391,-7.899235,-2.619196,7.002537,5.437018,8.610557],[8.701266,-1.200224,6.839734,-4.253895,4.600285,-7.112981,-8.738130,0.691614],[-8.661223,6.055457,-8.448244,0.033647,4.300104,-4.870101,8.076507,-2.397989],[-2.750075,7.796608,1.080468,5.385050,-2.601305,5.534785,4.343180,-6.097449],[-8.526823,9.795776,-9.495203,-1.998720,6.278938,-7.061319,-7.044011,9.199538],[8.910315,9.097412,-7.580691,-8.568338,-8.800452,-9.285246,-4.064014,5.592003],[-3.378303,1.998830,-9.979079,-2.463427,-7.055138,-0.068406,-1.502946,3.804573],[-9.670061,-4.717783,2.466850,4.309871,3.950094,4.698784,6.553744,-9.959916],[5.688479,-3.544844,0.626129,1.380540,5.899404,1.106114,1.224205,4.874514],[2.035531,-6.381312,-9.426285,-3.971399,2.639037,9.592873,-8.239237,0.181189],[1.107404,5.456037,-4.169294,-8.937008,7.731622,2.153912,-1.790547,-3.239324]],[[5.111880,-8.175760,6.255411,7.899324,-2.411865,6.235576,-0.232434,-1.694579],[-4.695018,8.128179,-2.435548,-9.463122,1.532245,-3.973081,-3.967124,2.414153],[-0.319142,-0.731191,-9.416795,-9.138279,-6.984201,9.701458,-1.409740,1.698605],[-0.216324,-4.455463,-4.948753,-6.485348,-3.514005,-6.553894,2.973543,-9.194476],[1.870552,3.313147,-1.837540,1.150151,5.248041,-4.255950,-7.837361,-0.915633],[-5.011830,-7.941671,8.816219,-3.597095,5.298655,8.617270,-5.757101,-0.038959],[-2.065082,3.626011,-3.358959,2.950018,4.653609,5.329824,8.171524,-8.848373],[-1.979774,6.901628,5.246014,-4.917671,-7.599734,-7.344875,5.512311,-7.198894],[-0.749084,0.006318,-6.130218,4.585200,-1.917104,-9.765360,-4.530801,1.643053],[3.295846,9.067176,-6.636425,0.768688,9.826181,5.271506,1.023230,-4.217570],[3.606901,-7.330893,-0.686502,3.531992,-3.670441,4.711297,1.377763,-5.717284]],[[2.910646,2.325008,8.643851,-6.390163,-5.284992,9.422283,0.778727,-6.019163],[5.607411,0.628589,-6.468372,-7.848984,-3.627824,3.663539,-0.260234,-4.723755],[9.811827,0.481273,-3.810503,4.301423,4.296868,-6.521411,-4.140120,3.288904],[0.219836,-4.067443,-2.725465,6.195087,-9.578196,-0.954180,-1.381888,-5.658479],[-4.789451,-6.407483,0.131563,-1.612492,-8.512665,8.886245,8.586580,2.615235],[3.747592,-1.433538,-7.459740,-3.631965,-9.861357,-9.852914,7.610211,0.895226],[-4.288578,4.040653,6.107736,2.115544,-8.616895,3.205830,7.801528,7.354869],[-8.278593,-6.069744,9.010304,8.933742,7.733686,-7.863393,-1.156701,1.751010],[2.328854,-3.146443,-3.933053,-7.470972,-0.925018,-7.910195,-3.661938,9.802121],[9.103759,-8.708226,-3.370893,-2.343043,8.234816,7.029708,-7.008653,-8.597711],[7.278528,7.979076,-3.081389,-8.400616,3.973101,4.762493,-3.563665,-4.378401]],[[-9.526267,-0.821473,-8.656538,1.251991,3.928979,7.645672,4.761248,2.542406],[-5.248242,-0.660129,8.935722,3.622928,7.246004,-3.143229,6.597808,1.661303],[4.997420,7.510536,-1.200274,6.522960,2.261804,-9.847328,7.386642,5.088844],[-3.371545,-7.391850,-1.306764,-0.304903,-8.007379,-0.966036,8.431431,-1.897814],[5.122498,-4.306151,-6.374079,-9.459356,-3.543956,-5.215476,-4.091441,1.972840],[2.288910,-3.909153,5.593033,9.643572,-5.167241,-5.042223,4.735107,-4.119367],[-3.107775,-9.292388,6.963746,-4.484846,9.213239,0.775274,-1.946036,-7.166198],[-1.727878,9.701436,4.780247,-2.336921,-8.042644,6.736553,8.463708,7.580396],[-7.440692,-4.920671,-7.664120,8.737045,6.035390,2.843802,9.684510,8.188671],[6.909827,-4.433435,1.194446,-5.734545,1.407980,4.411535,1.174694,-4.183207],[-0.267072,4.268254,9.809844,0.456963,2.504086,-7.404571,-9.615316,6.390603]],[[-7.950000,7.993683,-1.293188,-6.831497,4.005795,-6.938738,-9.773285,2.512268],[0.504433,1.672618,1.364881,0.561858,3.824184,-1.052438,4.908088,1.101527],[4.416086,9.542666,-5.403111,3.893083,7.460214,5.358453,-3.803606,-3.562023],[7.998803,-4.475372,-8.949069,-1.979225,5.829960,-3.532147,-0.441960,-4.663563],[-0.551706,9.112955,5.417133,-6.563819,-5.459888,-2.623129,-6.010330,-1.108120],[-3.637320,5.082881,-9.000282,9.660862,-8.496986,-2.316124,1.648929,-8.200117],[-1.393510,7.242361,-0.846152,-2.559470,3.732900,0.490080,6.180214,2.435003],[-0.546273,7.149282,-0.654509,-0.908770,-7.468355,8.958425,6.620859,4.317130],[9.051369,-3.327525,-5.452356,-7.528119,0.374564,-2.691329,4.301972,4.039218],[-2.368332,-5.120594,1.558553,5.469727,7.036220,8.864731,-9.459135,-8.470533],[3.952668,5.867945,2.060971,7.331828,5.353522,-2.576341,-4.922088,-2.171365]],[[-6.687327,7.019855,2.359863,9.071684,-4.949165,8.125032,4.592640,-9.592172],[-6.590768,-6.302488,-7.539057,4.313904,2.954085,-6.749957,8.857350,-5.583937],[-6.024715,3.421339,-1.573999,-1.759650,1.603006,4.409140,-0.943687,-4.756987],[3.800000,-5.720672,-3.363708,1.367724,3.800686,7.809738,-2.253173,-9.857923],[-3.197847,-7.054412,-1.924524,6.983636,8.113185,-9.788421,-6.558149,-9.157009],[-6.170532,9.586613,-0.079668,-8.260233,0.837423,-0.557001,-4.319072,-7.852667],[-2.747565,4.458179,6.400572,9.985885,-4.541120,-2.414344,-2.885459,-1.933642],[-9.998874,2.526905,7.715354,-0.273757,-6.299726,-5.216516,-5.395147,4.081052],[-7.475846,4.389667,8.336478,-3.795217,2.938261,-2.626051,9.599564,-7.133610],[7.408480,3.481517,6.584741,0.969739,-5.427842,-8.214379,-6.895477,-8.999998],[3.569110,-4.470604,-1.517201,-5.149164,-1.832035,6.777594,5.316701,7.301398]],[[8.057245,0.401834,-6.871480,-9.152934,5.739481,3.908808,-1.507044,-1.870301],[-5.852173,-4.317425,9.443744,-2.886538,-3.444560,3.132596,6.581160,-3.687207],[6.569452,7.805415,-6.474242,2.035870,9.528019,2.508812,-7.751382,7.529305],[-5.029449,5.208178,-9.681841,0.417232,5.486718,-1.900416,4.110638,4.217988],[7.769463,0.990693,7.091679,5.479001,3.997772,-2.403330,-5.126315,-7.213117],[-2.007610,-8.513696,1.004252,8.334414,-0.866026,0.399791,-3.369998,5.657869],[-1.845399,9.086205,5.673342,-9.789477,5.415894,-5.897201,-8.584285,-4.319003],[-6.112158,7.124469,7.701173,-3.675830,-0.120577,3.272437,-9.761964,-3.226701],[4.947525,-7.133560,-1.309811,-5.648996,-1.859346,2.730041,0.108077,9.210800],[-8.341507,-9.288136,9.288946,-6.937874,-3.227514,-3.777288,-1.872688,6.934223],[-6.403859,-8.071004,-4.432555,-2.324830,1.716531,0.949616,9.418812,-4.953065]],[[5.532618,8.602604,1.600047,8.663697,-2.555182,-9.873805,-9.933494,-6.177595],[-5.866152,-7.078068,8.301063,6.843955,-7.712835,-4.844534,2.403333,-7.649887],[1.150442,7.307207,2.977882,-0.269016,-8.088159,-1.908377,7.420464,5.808870],[0.785855,-9.701581,-7.332249,5.753225,4.358156,-0.494069,-1.602272,7.555046],[8.902238,-6.069207,0.133921,-3.044468,4.771936,2.199281,8.342921,-5.988402],[-0.003833,-7.584974,-8.225186,0.572084,4.304883,-2.231427,-9.223744,3.237482],[-7.735903,-2.264570,-0.073692,1.856048,6.704910,-0.146802,4.205700,6.843549],[-3.046793,-1.912267,3.036323,-1.450527,-4.506124,-6.603098,-5.683033,-7.770292],[0.494284,7.572380,8.540222,-8.615242,3.812423,9.779818,9.237896,-8.389202],[-6.135770,0.464754,-7.949167,-6.318559,-5.400953,-5.188381,-1.730819,-0.876362],[7.769628,-6.199965,-4.944699,-2.743053,2.231410,3.872242,-4.144288,-7.987302]],[[-4.294454,2.594065,2.943213,4.276041,-0.785208,3.793790,-3.517671,3.033861],[1.051247,-0.978887,-0.362852,1.185434,9.468571,-0.179847,-2.869586,-7.058604],[-9.770308,6.144998,-8.998924,-1.245185,-1.252790,1.901742,1.461966,4.344841],[-8.644960,-3.441448,-1.691472,1.447392,-4.340204,4.715503,-2.565408,-9.469733],[6.770470,3.928835,-7.091293,9.305075,0.877957,-9.069361,9.675031,4.466059],[2.087777,-5.245470,6.244506,2.471550,1.760124,-2.698244,8.590493,5.120012],[-6.244810,-2.583636,-9.137792,-8.428346,-8.300053,-1.501593,-9.366453,-4.010885],[7.445706,9.502050,-2.479321,0.144422,6.827130,3.102003,-3.058544,-7.901708],[8.728349,8.570391,-0.108014,0.755307,-2.423689,-2.135529,3.317136,5.131748],[2.670436,4.460333,1.155926,9.272331,-1.315706,9.666624,6.563060,-7.309184],[-3.946708,-4.234405,5.453891,-5.745347,1.323645,-4.774775,0.103508,-4.784954]]], dtype = "float64")#candidate|9084|(11, 11, 8)|const|float64
uop_9085 = relay.atanh(const_9084.astype('float64')) # shape=(11, 11, 8)
output = relay.Tuple([uop_9085,])
output2 = relay.Tuple([uop_9085,])
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
	relay.transform.Legalize(),
	relay.transform.FoldConstant(),
	relay.transform.ToANormalForm(),
	relay.transform.ToGraphNormalForm(),
	relay.transform.SimplifyInference(),
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
