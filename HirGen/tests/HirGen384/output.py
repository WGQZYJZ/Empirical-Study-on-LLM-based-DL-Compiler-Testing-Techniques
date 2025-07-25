import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_19 = relay.const([[[3.871888,-3.639732,9.575091,8.994751,2.694314,6.863876,-9.313778,1.177593,-5.574800,8.007202,-3.637959,7.428358,2.227206,-7.636344,6.712512,3.284298],[-8.332836,-1.150927,0.308010,6.134228,8.452961,-9.923041,0.853865,3.629247,-7.702261,0.422393,-0.545946,7.159508,8.153917,5.120011,0.454035,-3.368139],[-2.123636,9.672512,-1.988591,-7.095069,8.349266,-7.102568,8.042500,5.687533,-6.242275,-7.041132,4.330015,-4.379195,-5.044763,9.554462,7.867708,0.320012],[-9.126518,5.903853,1.915148,-1.695898,-9.065558,-6.278834,-0.664883,0.858988,-7.307343,2.893724,9.240360,0.244541,0.433578,7.534633,-0.479170,-3.520958],[-1.848512,8.094615,1.590549,-0.786676,-5.729640,7.797749,-4.225460,2.070591,8.217699,-6.803707,2.108164,-5.401090,-8.363163,3.907701,-1.765694,0.340846],[2.926818,5.749112,-5.241698,-4.902261,-4.815635,5.767210,-2.338467,1.681147,2.732052,-4.355977,1.135076,7.056374,-7.969197,-2.722908,-9.924256,5.592376],[4.765715,3.652330,4.030494,-5.053295,3.373808,-2.522732,5.409730,8.454756,-5.550430,4.539154,-3.886784,0.068803,8.975845,-3.464102,-4.949129,6.427768],[-2.313016,2.538086,-5.392212,5.997216,-4.497442,9.628322,6.083348,-7.490585,-9.093833,-8.337803,4.641024,6.658831,1.663496,-8.259892,-6.701855,2.871034],[-1.911172,-0.338622,8.157069,5.518128,0.084712,4.814198,5.542954,-8.116927,6.399962,2.520704,9.767105,3.679395,-5.621840,-2.417693,0.142115,7.050581],[-0.279536,-6.704349,9.619877,6.928070,-4.665894,0.877482,1.233282,9.671614,-1.108070,7.563796,2.158591,0.549226,-9.097888,-6.572046,3.997886,-9.151575],[6.266712,9.245684,-7.813635,-1.462367,2.087072,-9.967481,1.225405,2.437037,-8.814654,2.353439,9.116653,8.274160,-0.279427,2.152954,2.718396,-3.806643],[-2.637448,1.466026,-9.295967,4.638486,-6.384199,-3.339877,7.275579,5.289308,-0.649728,-3.121809,3.817828,-6.573407,0.124849,-9.228277,7.297633,-0.189886],[-4.839149,-6.669427,0.071814,2.870504,4.414230,6.993393,5.049942,4.537417,-3.553115,-6.339350,7.693378,9.667804,-5.774264,-9.621830,-7.243440,-9.558634]],[[-8.361913,-1.420993,-4.401949,8.563969,5.130166,3.592109,-2.303782,2.169816,-6.922874,-8.011638,-8.209512,-2.886093,5.656263,-2.216822,3.275194,6.370039],[1.648911,8.303119,5.417644,2.290519,-6.334660,5.030588,5.933483,8.387032,-7.504336,-4.419801,6.962126,-4.618042,3.538924,0.988585,7.343847,-5.812415],[-6.688650,-2.120376,6.929709,-1.921132,-0.520767,-8.700024,-4.276937,9.254693,3.694192,2.724687,2.092311,-7.043571,-5.297483,1.912871,-1.055819,-8.310279],[-8.329527,-9.660206,1.626444,4.762646,-8.530621,1.245889,4.472540,-2.380308,-0.684347,1.075952,9.312504,-3.806388,4.350139,5.756580,-0.552269,-4.413284],[-2.542520,-2.214887,-0.755688,-0.416407,1.868638,3.206831,-5.538614,1.252624,-0.590869,-0.650811,-8.610874,3.486453,1.406384,1.417451,4.889748,-2.370775],[-2.884214,9.998987,-8.271107,-8.842805,8.622573,-0.658245,1.387273,3.289733,-0.101876,9.540556,-2.296046,2.648331,6.051680,8.780481,-3.902035,-0.017080],[-5.266049,4.811256,4.709386,-3.275443,-2.403630,1.532499,2.523504,5.703614,-2.553243,-8.969901,3.473146,-4.942277,5.457224,1.025018,9.117187,-3.276370],[8.680741,-6.566040,7.872071,-8.285900,2.782464,2.342988,-9.391633,7.542399,3.040694,4.043627,2.796506,1.729264,-1.852320,-7.183765,3.410269,6.587492],[0.531653,3.341560,8.685822,-8.624609,1.358998,8.182348,-1.674612,5.193628,-5.681212,-0.107924,-4.926162,-5.002865,6.581856,4.285272,-8.713229,2.394854],[-7.511486,-4.134672,-0.393706,4.826317,0.004662,8.031993,8.101569,7.588951,-1.313703,2.890925,-9.138723,9.450565,-8.077303,-3.777844,3.138324,-6.892571],[-2.038491,1.521747,2.904679,7.569636,1.244313,-4.566201,6.046183,8.978906,-7.062886,-2.494513,-7.658960,-5.273633,-7.563103,7.479928,-7.334239,-1.806111],[0.328546,-2.152027,-3.411942,0.323275,-3.649172,-8.732513,2.902196,6.082164,-4.674371,-5.822960,7.966888,9.763884,8.421265,-4.485992,9.900276,5.034397],[-1.324986,0.131010,0.160243,6.588121,7.453568,0.180171,1.759157,-1.990155,-6.941723,-5.344816,4.116576,-6.645909,8.304307,-3.693604,5.961291,7.865373]],[[3.908659,-7.407022,9.042366,9.763467,4.866392,6.148100,0.295331,-6.796551,7.932404,-8.431707,-2.665759,6.021264,0.024142,-1.979425,5.283910,-4.574224],[8.512684,9.218392,-5.156703,4.301386,8.226812,-1.076264,-2.778137,8.703201,-3.323043,-4.638684,-3.923700,-1.179496,9.753540,-4.512824,-2.456321,-1.712425],[9.176099,-5.992607,-4.170489,8.693856,-6.542472,-4.590465,-3.416169,-1.586362,9.180315,3.590500,9.719238,8.690221,5.634675,2.706639,9.713572,4.635700],[-9.645736,-7.324206,0.489974,-5.769604,-1.061967,-1.316660,-5.004091,8.271849,3.367775,1.795269,-8.481648,3.980238,-3.287784,9.017545,-0.557798,-3.499125],[-3.879462,1.142276,-9.763376,7.528828,1.021227,5.812328,0.771317,3.476029,-3.114275,0.758898,-0.082013,-3.753369,4.884000,-9.034353,-4.589880,-2.674718],[8.811397,-6.938801,-1.251645,-8.329336,0.883541,4.932517,-5.695540,3.438127,-5.031783,5.522982,5.762467,3.844203,8.940305,3.659572,8.318006,-7.982338],[7.500714,-5.177108,3.312749,4.037913,9.994800,3.853403,-6.828664,-9.548009,0.682894,7.088059,6.594181,4.118806,-1.825788,-5.541077,7.793307,-6.735058],[1.675644,-1.007382,-7.890289,4.594770,-3.532110,4.533985,1.500090,2.440653,-5.048136,9.779068,-4.002513,-1.276134,7.942660,-4.206078,-4.783207,-5.116152],[5.248390,-7.903067,-3.863260,7.411920,-4.222061,6.548322,-0.461142,-4.961888,9.646573,-9.992621,-8.401145,-8.371183,6.014732,-4.799866,-6.706419,4.744128],[7.283975,4.179860,8.630115,4.242690,1.553633,9.083749,2.004844,-8.313925,-8.633777,-3.006276,-3.865050,-1.216168,8.315040,2.641827,8.669963,-0.065830],[-0.915665,4.386192,-5.225147,7.924167,3.125845,-7.292885,-0.057439,-9.589111,2.844193,9.273357,0.008775,-3.795635,5.649355,-5.130797,-2.438100,8.299937],[-5.796175,1.186422,4.615951,9.990410,9.953929,-9.434941,-5.310435,-7.417711,6.967442,0.277759,-6.557410,-0.380788,1.200227,-1.874836,7.735226,-6.765376],[-1.130798,-2.504427,-0.097623,6.608485,5.008962,5.997516,-6.776645,-6.773738,-3.847315,-9.789545,6.853152,-3.249929,-6.184050,-6.619810,-3.144414,2.674435]],[[-7.668019,5.864206,3.000631,8.843391,-7.384065,5.704449,-5.616611,-3.374747,9.714293,9.683088,8.673953,-4.183622,2.970529,1.452398,4.122880,-4.847414],[1.390314,0.290906,-3.366875,4.893872,1.525216,2.636728,-4.945503,-7.535883,6.276293,-3.064708,0.061790,-1.891610,-6.233172,6.443634,-0.990980,3.126388],[3.559982,7.264142,2.869548,-2.916820,4.104224,2.146235,6.317872,5.385996,2.606243,-2.103706,-1.964412,3.203669,-3.503981,1.145901,8.623252,-5.189452],[4.780918,-1.599469,3.583848,7.326735,3.814429,-3.160066,1.783109,0.613094,-0.177396,7.277955,-0.959492,2.282654,3.720300,7.991601,1.047325,9.853451],[0.417612,-5.128256,-3.554913,8.446173,-1.771871,3.142891,-2.364723,-9.955165,-7.996051,6.379677,3.527690,2.905782,3.148386,7.861709,7.656585,3.740954],[-2.946950,4.740514,-8.227890,-1.863889,-2.020964,-0.973230,-0.182936,4.634354,-7.891091,3.663937,3.295215,5.977878,-9.700116,-6.738120,8.714799,-2.279468],[2.601020,7.600279,1.063359,-4.844374,4.086596,-0.068047,4.951279,-8.602558,-1.745953,3.415594,-8.141173,5.832937,3.737411,-2.972827,4.871859,8.068433],[-0.393203,-1.020277,-1.631619,-3.994249,1.669037,-7.550321,-9.540282,8.502887,-6.477856,7.254088,1.289912,0.654088,-9.293265,8.029225,8.184279,-5.367409],[5.805948,0.160665,6.454978,4.479565,-7.684786,7.921086,-6.281845,8.393677,-6.418812,-8.643044,7.040881,-2.434918,1.785925,-2.653566,-1.951029,1.742410],[6.531629,-5.724385,-4.744030,-3.221177,8.286994,1.177502,-3.151081,-0.951996,6.359149,-4.572832,8.045170,-4.353921,-3.348924,2.665533,6.604763,0.140111],[0.926284,7.509541,8.272003,-0.643717,-9.157462,2.160079,-7.494248,5.002802,-8.443684,9.435601,-6.580880,-5.610663,-2.899259,-7.455599,-9.269361,-8.282295],[4.268954,4.178903,8.835386,7.311884,-5.626778,-4.286494,-8.069442,-6.321749,0.667115,-4.375476,-1.907835,4.708970,-2.466253,-4.385087,8.525544,-5.746389],[7.281366,0.908034,6.579803,-4.370241,6.209564,0.067697,-9.566735,-7.907049,1.547492,9.955362,-6.568892,-2.365799,-0.818195,7.487249,5.738124,-3.294286]],[[-1.699075,-3.350223,-9.494353,8.898641,4.861922,-2.838860,-6.815685,-8.054360,8.367503,0.993186,-6.245012,1.766479,6.872666,-9.575120,-6.285590,4.227404],[-8.236485,1.749975,-8.872669,0.852068,5.176176,2.793086,-8.269675,8.980414,9.899966,2.757356,-5.243925,2.167846,-7.439588,-0.904874,-6.374927,6.648162],[7.943656,-2.252690,0.382378,-5.962637,0.688812,-6.978941,0.948228,8.641266,3.706696,-8.014037,5.914368,0.493159,0.372338,9.023935,6.880857,-4.802299],[7.488888,-8.256336,-0.092060,4.188044,-3.260850,-0.748155,7.603388,-7.630888,-5.397556,-3.072620,-6.387229,7.482760,1.746504,-0.464052,1.212584,-8.469877],[6.133531,2.299621,9.227424,3.242851,8.434574,5.832037,9.960545,7.655145,-2.091865,-5.999243,0.885943,-8.852941,-6.433178,7.852759,7.234621,-5.321211],[-3.348848,8.662523,-8.294727,1.584460,-6.644897,-8.165417,-5.079291,1.154738,2.739846,-9.852677,-0.108144,5.735968,7.514673,-8.159746,-5.757757,5.364711],[5.686317,-7.052142,5.898538,2.975611,-2.877652,8.459953,0.730748,1.837403,-3.170104,4.045470,-8.783071,8.305926,5.760925,0.208302,-2.627432,-7.057257],[9.439105,9.951055,-0.296948,-6.475807,-0.136417,2.570291,-5.604903,-8.625054,-5.928303,6.116694,2.583493,-6.305865,1.230324,-7.060737,-7.484276,8.855428],[-2.554966,-0.913582,8.056723,7.942866,0.144953,8.766100,-9.822849,-5.877328,8.066764,1.436234,5.037584,2.594133,3.524659,-0.974118,-0.786894,7.978657],[8.651280,5.168186,-9.243502,-3.226940,9.126569,-5.975621,-0.855470,2.505313,-6.810884,-0.593246,-5.881256,-9.594623,9.655718,-3.809961,-8.140435,-1.020019],[0.706639,-3.999746,1.644846,4.103128,-4.543799,-5.335734,8.273282,-5.145863,-2.233059,5.397326,-5.464216,8.942804,-7.901984,4.161929,0.076838,-1.037244],[6.780871,5.465663,-2.310782,-2.996594,-0.920778,6.531340,-9.062528,2.002491,-6.824082,0.964497,9.745130,-4.166481,-0.248345,-5.788107,-7.910875,3.198990],[-9.804788,-0.217598,0.263648,2.306149,2.832393,8.856264,3.869853,-4.901040,0.096402,-8.140032,-0.302907,9.946277,8.986139,7.724780,-8.002626,1.011029]],[[6.354869,8.121173,-6.059880,-4.726784,1.411205,9.976617,-9.710606,-2.578746,-0.450357,-9.393969,-6.257021,7.610472,-8.657577,7.933718,0.582726,1.653300],[-9.740916,-0.520102,8.668835,-9.978224,-2.251736,7.036639,1.633294,6.749346,5.216382,5.948653,8.802234,4.709026,3.939337,-9.738221,9.714170,0.971162],[0.816274,4.426825,-9.249689,0.623851,1.568431,6.500299,9.084847,-7.079232,5.531541,-8.845766,9.363284,-1.160065,-5.657646,3.296183,-2.907432,5.928384],[-8.959024,-2.433809,-7.863841,-6.612098,4.124146,-0.720164,-1.662609,5.929660,-8.674079,-6.587932,8.016958,-6.120758,0.012058,6.355090,-9.927352,9.630728],[2.756196,1.762708,-7.479943,-2.593188,-1.826230,-6.729891,8.345375,-3.722595,4.679606,8.952102,2.758332,-7.008005,-2.005672,-0.816747,-2.738796,8.233964],[3.611191,0.938622,-1.516502,7.483535,-8.534151,2.271485,5.830220,-4.072674,-2.178608,3.990363,5.524332,0.823561,-4.084638,9.098770,2.151859,-0.232277],[6.197198,-7.852787,1.215441,-9.987760,2.500922,-5.769541,1.641458,1.482185,-2.981580,0.855993,-4.637846,7.282811,-0.306346,2.407742,-2.106969,8.181077],[6.496881,1.765983,8.295972,4.806297,-1.721361,-1.180757,-1.420840,1.554479,-6.988841,-3.920452,0.009804,9.490843,-9.036513,-3.211714,2.509428,1.187326],[3.228946,0.104653,-3.359704,-1.981090,-1.202012,9.131668,-4.898102,-3.317603,0.891355,-4.332461,-3.117025,3.090571,-0.784628,2.514159,5.967516,1.463291],[-4.729859,7.465427,2.840222,0.301848,-7.460316,-9.471771,3.346509,-4.567793,5.866897,-6.102538,-4.486472,3.639380,0.324362,-5.195949,0.994172,2.425351],[0.047284,-8.269610,-1.494010,-6.733230,-4.930669,-2.739314,5.326551,4.801710,9.814980,9.163482,8.828746,-1.342334,5.883219,1.984722,-2.418760,-1.717752],[0.627919,-6.345981,-8.797114,4.590168,8.752321,1.560497,-4.587577,-4.375449,-8.945225,8.164112,-0.820472,-2.790415,5.546791,-8.626232,-0.811428,7.042369],[9.230450,-4.822009,-1.478521,7.464098,5.121403,8.565972,3.756987,9.291248,6.307575,8.979831,-7.243366,6.791220,0.067708,-2.609238,7.137182,0.466163]],[[7.457898,-4.989627,3.380205,-4.283639,-5.708326,-5.404431,6.788368,6.527773,7.801834,-6.772094,-6.476779,2.930371,7.051857,-4.322516,4.008131,2.222944],[2.829320,-4.980517,2.706338,3.372846,-1.846432,5.358850,1.859046,-6.553371,1.048150,-7.418617,6.776330,0.935388,4.003315,7.827727,-7.788200,-3.916173],[-2.077896,-6.823281,6.795965,-8.804167,-5.481809,4.394506,-1.612272,-1.347161,-5.482936,-3.017281,-9.370479,-4.211725,1.480687,-6.529825,-1.170804,4.022000],[7.743925,0.145301,1.947172,1.581566,3.185711,1.321354,-2.840202,-7.948166,-1.879552,-6.884805,-8.751009,6.533330,-9.410349,6.478319,-1.805452,-0.834238],[2.501918,-5.455529,4.717664,-0.626366,-4.513398,-9.769701,6.845792,6.745158,1.353994,-0.467908,-0.164934,4.324564,2.698704,1.099335,1.038166,0.178128],[0.993308,8.827501,9.847136,-9.343913,9.932820,2.521390,9.909192,7.617720,-2.018144,-8.980393,8.233954,-1.504295,3.314739,-3.397424,0.358349,5.372960],[9.696708,8.447963,-0.249261,-4.084668,-2.574300,-2.411984,-2.538239,1.829935,8.232307,4.111468,1.910793,3.002265,1.640553,-2.144727,7.967165,-2.376157],[-3.822782,-6.985085,7.255925,2.966213,-6.192627,2.683552,4.864852,5.377001,-9.119031,8.927912,-9.631550,-0.087970,-4.309489,-3.488044,-5.899817,-5.246134],[-0.787315,5.907032,3.624087,-6.297186,-6.521983,-3.287520,-3.260030,-8.720580,-7.276892,-1.336108,-9.067819,-1.456290,4.075581,8.388604,5.935724,7.103178],[-9.122418,4.762448,1.405686,2.005351,5.607656,2.253383,3.640071,8.973842,8.426091,7.757388,-6.840848,-5.377907,-8.751827,-0.176045,1.070506,-5.647649],[-7.853087,0.583028,1.111964,-8.499967,-4.020299,-2.932736,9.975682,0.925226,6.631901,1.079847,-6.005579,-9.519289,6.851430,3.076806,-9.688512,-7.950586],[5.133865,-9.864705,-2.133953,-9.216988,-4.698270,-6.324831,-3.332288,-2.189343,-7.942014,2.526165,7.817406,-2.078770,-1.177431,8.100693,7.885111,-6.013263],[9.677786,1.837470,0.717514,-4.792155,-7.308936,9.018948,-5.363514,-9.679823,3.795340,9.176008,0.275137,2.120720,6.716709,-6.997215,-0.816121,-1.633705]],[[0.460845,3.043247,4.860942,-3.350257,1.049989,-4.668773,9.251257,-1.985432,-6.487237,8.517165,6.552841,-0.027564,8.793617,1.692375,2.294497,6.295951],[3.196670,1.494608,-9.840951,-7.441788,0.494729,5.495318,-6.581385,-4.312619,-2.286035,-5.531542,-5.695207,-6.159894,-6.000646,-8.876415,8.259100,-8.603234],[-1.690203,5.612291,-9.518873,-2.719969,-7.003453,-1.117073,-2.027830,-3.915200,5.637497,-5.851355,6.219803,2.833365,8.878696,3.824718,-4.349689,7.585780],[4.173263,5.831053,2.338359,1.824424,-0.791634,-3.646082,-1.616650,5.312639,0.651180,-2.988023,-5.785969,-7.795690,3.282085,9.683449,-4.057078,-6.435466],[8.989649,1.924767,-6.479134,6.434061,-7.646329,2.434317,-4.866799,-0.961083,-9.296724,-9.419367,6.418578,-3.849963,-1.683494,-6.683509,8.377298,-2.380117],[-7.928879,3.028058,-2.201816,7.231003,-3.104931,-4.231363,6.925727,-4.917996,2.908141,5.189335,-5.873704,7.184631,1.276765,6.832006,-3.244289,0.115158],[9.504292,2.421526,1.414659,-3.612150,7.870611,-6.826942,-8.617801,2.449458,8.778337,-2.969093,-1.862898,-1.461307,2.812684,-8.609732,5.000706,-4.594748],[-3.508075,4.496384,5.739499,2.470922,-1.075257,4.216894,3.018133,-6.210046,8.071896,-2.709522,-4.252998,9.505127,-0.984449,8.246829,-0.865306,-0.414986],[-9.709337,-4.160395,0.310244,-3.616112,-5.819784,-3.016657,-3.283343,-7.121286,5.819032,-4.464677,-8.975116,4.123542,3.259936,-5.276777,7.604357,6.120701],[-3.543975,8.261426,5.465607,9.399165,8.313171,5.225145,-0.669697,-7.858047,-3.571062,5.040282,-9.845960,0.082931,-7.357470,2.532765,-5.538659,6.167938],[9.023394,9.127422,-8.065351,-8.745057,-4.812085,-0.890619,5.140424,4.737470,2.860715,-9.217143,0.066872,3.315273,-6.307782,9.420696,8.859812,3.278211],[5.891895,-1.759604,-3.664185,-5.547787,-9.593711,6.413761,4.573392,-5.638714,-3.509982,-0.693181,-4.581695,0.902406,2.929585,-9.310456,2.825914,2.830488],[-6.753012,-7.259018,-6.106720,2.787662,8.458145,-4.505826,5.479859,2.638886,-3.772739,-0.405350,-6.029561,7.056383,-2.930765,-6.022182,9.857395,5.193421]]], dtype = "float64")#candidate|19|(8, 13, 16)|const|float64
uop_20 = relay.cos(const_19.astype('float64')) # shape=(8, 13, 16)
uop_23 = relay.exp(uop_20.astype('float32')) # shape=(8, 13, 16)
uop_34 = relay.tan(uop_23.astype('float32')) # shape=(8, 13, 16)
bop_37 = relay.logical_xor(uop_23.astype('uint8'), relay.reshape(uop_34.astype('uint8'), relay.shape_of(uop_23))) # shape=(8, 13, 16)
output = relay.Tuple([bop_37,])
output2 = relay.Tuple([bop_37,])
func_49 = relay.Function([], output)
mod['func_49'] = func_49
mod = relay.transform.InferType()(mod)
output = func_49()
func_50 = relay.Function([], output)
mutated_mod['func_50'] = func_50
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_103 = relay.TupleGetItem(func_49_call(), 0)
call_104 = relay.TupleGetItem(func_50_call(), 0)
output = call_103
output2 = call_104
func_108 = relay.Function([], output)
mod['func_108'] = func_108
mod = relay.transform.InferType()(mod)
mutated_mod['func_108'] = func_108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mutated_mod.get_global_var('func_108')
call_109 = func_108_call()
output = call_109
func_110 = relay.Function([], output)
mutated_mod['func_110'] = func_110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_133 = relay.TupleGetItem(func_49_call(), 0)
call_134 = relay.TupleGetItem(func_50_call(), 0)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_145 = func_108_call()
call_146 = func_108_call()
bop_155 = relay.right_shift(call_145.astype('int64'), relay.reshape(call_133.astype('int64'), relay.shape_of(call_145))) # shape=(8, 13, 16)
bop_158 = relay.right_shift(call_146.astype('int64'), relay.reshape(call_134.astype('int64'), relay.shape_of(call_146))) # shape=(8, 13, 16)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_163 = func_108_call()
call_164 = func_108_call()
var_177 = relay.var("var_177", dtype = "uint8", shape = (8, 13, 16))#candidate|177|(8, 13, 16)|var|uint8
bop_178 = relay.floor_divide(call_133.astype('float32'), relay.reshape(var_177.astype('float32'), relay.shape_of(call_133))) # shape=(8, 13, 16)
bop_181 = relay.floor_divide(call_134.astype('float32'), relay.reshape(var_177.astype('float32'), relay.shape_of(call_134))) # shape=(8, 13, 16)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_190 = relay.TupleGetItem(func_49_call(), 0)
call_191 = relay.TupleGetItem(func_50_call(), 0)
bop_193 = relay.minimum(var_177.astype('float64'), relay.reshape(bop_178.astype('float64'), relay.shape_of(var_177))) # shape=(8, 13, 16)
bop_196 = relay.minimum(var_177.astype('float64'), relay.reshape(bop_181.astype('float64'), relay.shape_of(var_177))) # shape=(8, 13, 16)
output = relay.Tuple([bop_155,call_163,call_190,bop_193,])
output2 = relay.Tuple([bop_158,call_164,call_191,bop_196,])
func_200 = relay.Function([var_177,], output)
mod['func_200'] = func_200
mod = relay.transform.InferType()(mod)
var_201 = relay.var("var_201", dtype = "uint8", shape = (8, 13, 16))#candidate|201|(8, 13, 16)|var|uint8
output = func_200(var_201)
func_202 = relay.Function([var_201], output)
mutated_mod['func_202'] = func_202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_238 = relay.var("var_238", dtype = "uint64", shape = (9, 14, 3))#candidate|238|(9, 14, 3)|var|uint64
var_239 = relay.var("var_239", dtype = "uint64", shape = (9, 14, 3))#candidate|239|(9, 14, 3)|var|uint64
bop_240 = relay.greater_equal(var_238.astype('bool'), relay.reshape(var_239.astype('bool'), relay.shape_of(var_238))) # shape=(9, 14, 3)
output = bop_240
output2 = bop_240
func_248 = relay.Function([var_238,var_239,], output)
mod['func_248'] = func_248
mod = relay.transform.InferType()(mod)
var_249 = relay.var("var_249", dtype = "uint64", shape = (9, 14, 3))#candidate|249|(9, 14, 3)|var|uint64
var_250 = relay.var("var_250", dtype = "uint64", shape = (9, 14, 3))#candidate|250|(9, 14, 3)|var|uint64
output = func_248(var_249,var_250,)
func_251 = relay.Function([var_249,var_250,], output)
mutated_mod['func_251'] = func_251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_297 = func_108_call()
call_298 = func_108_call()
output = relay.Tuple([call_297,])
output2 = relay.Tuple([call_298,])
func_316 = relay.Function([], output)
mod['func_316'] = func_316
mod = relay.transform.InferType()(mod)
output = func_316()
func_317 = relay.Function([], output)
mutated_mod['func_317'] = func_317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_325 = relay.TupleGetItem(func_316_call(), 0)
call_326 = relay.TupleGetItem(func_317_call(), 0)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_331 = relay.TupleGetItem(func_49_call(), 0)
call_332 = relay.TupleGetItem(func_50_call(), 0)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_334 = relay.TupleGetItem(func_49_call(), 0)
call_335 = relay.TupleGetItem(func_50_call(), 0)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_345 = func_108_call()
call_346 = func_108_call()
func_200_call = mod.get_global_var('func_200')
func_202_call = mutated_mod.get_global_var('func_202')
call_349 = relay.TupleGetItem(func_200_call(relay.reshape(call_334.astype('uint8'), [8, 13, 16])), 2)
call_350 = relay.TupleGetItem(func_202_call(relay.reshape(call_334.astype('uint8'), [8, 13, 16])), 2)
output = relay.Tuple([call_325,call_331,call_334,call_345,call_349,])
output2 = relay.Tuple([call_326,call_332,call_335,call_346,call_350,])
func_353 = relay.Function([], output)
mod['func_353'] = func_353
mod = relay.transform.InferType()(mod)
mutated_mod['func_353'] = func_353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mutated_mod.get_global_var('func_353')
call_354 = func_353_call()
output = call_354
func_355 = relay.Function([], output)
mutated_mod['func_355'] = func_355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_398 = relay.TupleGetItem(func_49_call(), 0)
call_399 = relay.TupleGetItem(func_50_call(), 0)
uop_407 = relay.asinh(call_398.astype('float32')) # shape=(8, 13, 16)
uop_409 = relay.asinh(call_399.astype('float32')) # shape=(8, 13, 16)
func_200_call = mod.get_global_var('func_200')
func_202_call = mutated_mod.get_global_var('func_202')
call_425 = relay.TupleGetItem(func_200_call(relay.reshape(call_398.astype('uint8'), [8, 13, 16])), 0)
call_426 = relay.TupleGetItem(func_202_call(relay.reshape(call_398.astype('uint8'), [8, 13, 16])), 0)
func_248_call = mod.get_global_var('func_248')
func_251_call = mutated_mod.get_global_var('func_251')
const_431 = relay.const([-1,-6,-1,4,10,5,9,-7,-4,-3,-2,3,-6,7,3,9,-7,4,10,7,-1,-5,4,-3,-5,-9,1,-8,4,-9,9,2,1,-4,-5,-2,3,7,1,6,-6,2,-8,8,-6,-10,3,1,-7,8,5,-10,-9,-6,5,-4,-8,2,-7,-7,-7,9,10,-7,-6,10,-5,2,7,2,-1,-7,-5,6,-9,-6,-1,-8,9,-9,-10,-8,1,-9,-9,2,-9,2,8,-5,-10,-5,8,-3,1,-1,1,8,-1,-2,-9,-4,-3,-2,4,-2,-10,7,-2,-4,2,-6,7,7,-2,-10,-3,-1,1,-9,-3,-1,-8,1,-9,-5,-2,-6,-6,7,-9,-8,3,1,3,1,1,-8,-10,-10,-4,10,7,-5,8,-8,-10,9,6,-1,10,-4,6,1,-1,-5,-8,-2,-2,8,10,-6,2,6,-7,-8,1,-9,4,-2,-5,-1,-3,-7,-10,2,-1,-10,4,-3,-5,8,-3,-2,1,5,1,6,-10,9,-8,-2,9,-1,10,-4,5,10,10,-8,-5,6,8,2,-5,-10,1,-1,3,-5,-6,-9,-2,-10,2,5,10,5,-3,7,-7,-10,-8,3,3,-6,7,-9,-6,-3,-6,6,-10,-5,8,-9,-9,-5,10,-10,-6,-1,6,3,-6,8,5,-9,5,-5,5,7,-5,-3,-2,9,3,-2,7,-1,-4,-6,-5,1,8,-2,-2,-7,5,3,4,7,1,4,-7,-10,6,-9,2,10,7,-2,-2,9,8,-5,5,8,3,3,-9,-10,-10,5,-10,1,4,8,2,-3,9,-5,-8,-10,6,-1,-6,-1,10,10,8,7,7,-8,-5,1,9,-8,-8,-7,2,1,-1,-6,-8,-2,10,-8,7,5,-9,5,4,-4,-4,9,3,7,4,-6,10,7,-7,6,-3,5,-9,9,-6,6,-5,7,6,-1,-7,-3,5,6,6,-8,-3,10,-5,-3,-3,-10,-5,6,3,4,-6,-9,-10,7,-9,7,-9,-3], dtype = "uint64")#candidate|431|(378,)|const|uint64
call_430 = func_248_call(relay.reshape(const_431.astype('uint64'), [9, 14, 3]), relay.reshape(const_431.astype('uint64'), [9, 14, 3]), )
call_432 = func_248_call(relay.reshape(const_431.astype('uint64'), [9, 14, 3]), relay.reshape(const_431.astype('uint64'), [9, 14, 3]), )
output = relay.Tuple([uop_407,call_425,call_430,const_431,])
output2 = relay.Tuple([uop_409,call_426,call_432,const_431,])
func_449 = relay.Function([], output)
mod['func_449'] = func_449
mod = relay.transform.InferType()(mod)
mutated_mod['func_449'] = func_449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mutated_mod.get_global_var('func_449')
call_450 = func_449_call()
output = call_450
func_451 = relay.Function([], output)
mutated_mod['func_451'] = func_451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_452 = relay.TupleGetItem(func_49_call(), 0)
call_453 = relay.TupleGetItem(func_50_call(), 0)
func_248_call = mod.get_global_var('func_248')
func_251_call = mutated_mod.get_global_var('func_251')
var_472 = relay.var("var_472", dtype = "uint64", shape = (6, 63))#candidate|472|(6, 63)|var|uint64
call_471 = func_248_call(relay.reshape(var_472.astype('uint64'), [9, 14, 3]), relay.reshape(var_472.astype('uint64'), [9, 14, 3]), )
call_473 = func_248_call(relay.reshape(var_472.astype('uint64'), [9, 14, 3]), relay.reshape(var_472.astype('uint64'), [9, 14, 3]), )
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_475 = relay.TupleGetItem(func_449_call(), 1)
call_476 = relay.TupleGetItem(func_451_call(), 1)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_481 = relay.TupleGetItem(func_316_call(), 0)
call_482 = relay.TupleGetItem(func_317_call(), 0)
output = relay.Tuple([call_452,call_471,var_472,call_475,call_481,])
output2 = relay.Tuple([call_453,call_473,var_472,call_476,call_482,])
func_487 = relay.Function([var_472,], output)
mod['func_487'] = func_487
mod = relay.transform.InferType()(mod)
var_488 = relay.var("var_488", dtype = "uint64", shape = (6, 63))#candidate|488|(6, 63)|var|uint64
output = func_487(var_488)
func_489 = relay.Function([var_488], output)
mutated_mod['func_489'] = func_489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_517 = relay.TupleGetItem(func_353_call(), 1)
call_518 = relay.TupleGetItem(func_355_call(), 1)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_542 = relay.TupleGetItem(func_316_call(), 0)
call_543 = relay.TupleGetItem(func_317_call(), 0)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_549 = relay.TupleGetItem(func_316_call(), 0)
call_550 = relay.TupleGetItem(func_317_call(), 0)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_555 = relay.TupleGetItem(func_316_call(), 0)
call_556 = relay.TupleGetItem(func_317_call(), 0)
uop_561 = relay.sqrt(call_549.astype('float32')) # shape=(8, 13, 16)
uop_563 = relay.sqrt(call_550.astype('float32')) # shape=(8, 13, 16)
func_248_call = mod.get_global_var('func_248')
func_251_call = mutated_mod.get_global_var('func_251')
var_573 = relay.var("var_573", dtype = "uint64", shape = (378,))#candidate|573|(378,)|var|uint64
call_572 = func_248_call(relay.reshape(var_573.astype('uint64'), [9, 14, 3]), relay.reshape(var_573.astype('uint64'), [9, 14, 3]), )
call_574 = func_248_call(relay.reshape(var_573.astype('uint64'), [9, 14, 3]), relay.reshape(var_573.astype('uint64'), [9, 14, 3]), )
output = relay.Tuple([call_517,call_542,call_555,uop_561,call_572,var_573,])
output2 = relay.Tuple([call_518,call_543,call_556,uop_563,call_574,var_573,])
func_578 = relay.Function([var_573,], output)
mod['func_578'] = func_578
mod = relay.transform.InferType()(mod)
mutated_mod['func_578'] = func_578
mutated_mod = relay.transform.InferType()(mutated_mod)
var_579 = relay.var("var_579", dtype = "uint64", shape = (378,))#candidate|579|(378,)|var|uint64
func_578_call = mutated_mod.get_global_var('func_578')
call_580 = func_578_call(var_579)
output = call_580
func_581 = relay.Function([var_579], output)
mutated_mod['func_581'] = func_581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_594 = relay.TupleGetItem(func_449_call(), 0)
call_595 = relay.TupleGetItem(func_451_call(), 0)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_607 = relay.TupleGetItem(func_316_call(), 0)
call_608 = relay.TupleGetItem(func_317_call(), 0)
uop_624 = relay.erf(call_594.astype('float32')) # shape=(8, 13, 16)
uop_626 = relay.erf(call_595.astype('float32')) # shape=(8, 13, 16)
uop_629 = relay.atanh(call_607.astype('float32')) # shape=(8, 13, 16)
uop_631 = relay.atanh(call_608.astype('float32')) # shape=(8, 13, 16)
output = relay.Tuple([uop_624,uop_629,])
output2 = relay.Tuple([uop_626,uop_631,])
func_635 = relay.Function([], output)
mod['func_635'] = func_635
mod = relay.transform.InferType()(mod)
output = func_635()
func_636 = relay.Function([], output)
mutated_mod['func_636'] = func_636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_704 = relay.TupleGetItem(func_635_call(), 1)
call_705 = relay.TupleGetItem(func_636_call(), 1)
output = relay.Tuple([call_704,])
output2 = relay.Tuple([call_705,])
func_720 = relay.Function([], output)
mod['func_720'] = func_720
mod = relay.transform.InferType()(mod)
mutated_mod['func_720'] = func_720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mutated_mod.get_global_var('func_720')
call_721 = func_720_call()
output = call_721
func_722 = relay.Function([], output)
mutated_mod['func_722'] = func_722
mutated_mod = relay.transform.InferType()(mutated_mod)
var_740 = relay.var("var_740", dtype = "float64", shape = (14, 6, 2))#candidate|740|(14, 6, 2)|var|float64
uop_741 = relay.log2(var_740.astype('float64')) # shape=(14, 6, 2)
output = uop_741
output2 = uop_741
func_752 = relay.Function([var_740,], output)
mod['func_752'] = func_752
mod = relay.transform.InferType()(mod)
mutated_mod['func_752'] = func_752
mutated_mod = relay.transform.InferType()(mutated_mod)
var_753 = relay.var("var_753", dtype = "float64", shape = (14, 6, 2))#candidate|753|(14, 6, 2)|var|float64
func_752_call = mutated_mod.get_global_var('func_752')
call_754 = func_752_call(var_753)
output = call_754
func_755 = relay.Function([var_753], output)
mutated_mod['func_755'] = func_755
mutated_mod = relay.transform.InferType()(mutated_mod)
var_765 = relay.var("var_765", dtype = "uint8", shape = ())#candidate|765|()|var|uint8
var_766 = relay.var("var_766", dtype = "uint8", shape = (15, 16, 13))#candidate|766|(15, 16, 13)|var|uint8
bop_767 = relay.less_equal(var_765.astype('bool'), var_766.astype('bool')) # shape=(15, 16, 13)
uop_770 = relay.cosh(bop_767.astype('float64')) # shape=(15, 16, 13)
bop_781 = relay.logical_and(uop_770.astype('bool'), var_765.astype('bool')) # shape=(15, 16, 13)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_808 = relay.TupleGetItem(func_635_call(), 1)
call_809 = relay.TupleGetItem(func_636_call(), 1)
output = relay.Tuple([bop_781,call_808,])
output2 = relay.Tuple([bop_781,call_809,])
func_813 = relay.Function([var_765,var_766,], output)
mod['func_813'] = func_813
mod = relay.transform.InferType()(mod)
var_814 = relay.var("var_814", dtype = "uint8", shape = ())#candidate|814|()|var|uint8
var_815 = relay.var("var_815", dtype = "uint8", shape = (15, 16, 13))#candidate|815|(15, 16, 13)|var|uint8
output = func_813(var_814,var_815,)
func_816 = relay.Function([var_814,var_815,], output)
mutated_mod['func_816'] = func_816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_824 = relay.TupleGetItem(func_353_call(), 0)
call_825 = relay.TupleGetItem(func_355_call(), 0)
var_830 = relay.var("var_830", dtype = "uint8", shape = (8, 13, 16))#candidate|830|(8, 13, 16)|var|uint8
bop_831 = relay.equal(call_824.astype('bool'), relay.reshape(var_830.astype('bool'), relay.shape_of(call_824))) # shape=(8, 13, 16)
bop_834 = relay.equal(call_825.astype('bool'), relay.reshape(var_830.astype('bool'), relay.shape_of(call_825))) # shape=(8, 13, 16)
func_578_call = mod.get_global_var('func_578')
func_581_call = mutated_mod.get_global_var('func_581')
const_836 = relay.const([-7,-8,-3,7,-9,-9,7,-8,-6,8,-1,-4,-8,3,3,-2,-5,5,9,3,2,-8,2,7,-4,-1,-1,4,-3,3,10,-6,-6,-4,-4,-4,1,-5,-9,2,-1,-10,9,10,-10,-7,10,7,6,-2,10,-5,7,-5,-4,2,9,6,6,9,-10,-6,2,8,-7,-8,-8,10,-5,-4,4,-4,9,-3,7,1,-10,10,10,-2,2,-6,7,8,4,2,-9,1,6,3,7,3,-10,-1,-2,-9,-5,5,-2,-5,-4,-4,-1,10,-10,3,6,-5,10,7,1,6,-3,-9,3,-1,8,3,4,-1,8,-4,-1,-1,6,-2,-3,4,-9,-1,6,-3,-1,8,-2,10,4,-4,-2,7,-2,5,-7,-3,2,1,8,-4,10,4,10,2,9,-10,-1,-9,6,-10,4,7,9,-6,4,8,2,8,8,-8,3,8,-7,-9,-2,3,-4,2,10,10,7,-10,2,3,-5,8,2,-4,-2,9,-3,10,5,-1,-9,1,-1,-7,8,-6,4,2,2,3,10,10,4,-3,1,6,-4,-9,7,-1,-7,-7,-3,-7,7,-8,1,2,-9,4,8,-1,-6,-9,-6,5,9,6,-1,4,-2,4,-2,1,-1,1,-7,-2,-5,-4,-3,-8,-3,4,-7,9,-5,-5,9,-10,10,-10,6,-10,4,3,4,-10,6,-8,-4,-4,-2,-8,4,-1,-9,-3,-2,-7,-6,-2,4,7,9,4,-6,2,9,9,8,-10,-1,-6,-6,7,-5,-2,4,8,-7,-7,-3,9,1,-7,-9,9,-2,3,8,-9,3,-2,1,10,-2,-10,-10,-7,8,1,1,-5,5,-10,-10,-5,-10,-1,5,-8,-2,2,-7,2,-10,-1,5,3,-8,10,-4,2,-2,-5,-6,-3,-1,-8,-3,6,-5,4,4,7,-4,1,-4,10,-6,2,-7,-10,-2,-1,-1,10,-3,-4,-4,9,10,6,3,-1,-10,-2,-9,-9,3,8,4,-9,-2,4], dtype = "uint64")#candidate|836|(378,)|const|uint64
call_835 = relay.TupleGetItem(func_578_call(relay.reshape(const_836.astype('uint64'), [378,])), 1)
call_837 = relay.TupleGetItem(func_581_call(relay.reshape(const_836.astype('uint64'), [378,])), 1)
func_578_call = mod.get_global_var('func_578')
func_581_call = mutated_mod.get_global_var('func_581')
call_843 = relay.TupleGetItem(func_578_call(relay.reshape(const_836.astype('uint64'), [378,])), 2)
call_844 = relay.TupleGetItem(func_581_call(relay.reshape(const_836.astype('uint64'), [378,])), 2)
output = relay.Tuple([bop_831,call_835,const_836,call_843,])
output2 = relay.Tuple([bop_834,call_837,const_836,call_844,])
func_848 = relay.Function([var_830,], output)
mod['func_848'] = func_848
mod = relay.transform.InferType()(mod)
mutated_mod['func_848'] = func_848
mutated_mod = relay.transform.InferType()(mutated_mod)
var_849 = relay.var("var_849", dtype = "uint8", shape = (8, 13, 16))#candidate|849|(8, 13, 16)|var|uint8
func_848_call = mutated_mod.get_global_var('func_848')
call_850 = func_848_call(var_849)
output = call_850
func_851 = relay.Function([var_849], output)
mutated_mod['func_851'] = func_851
mutated_mod = relay.transform.InferType()(mutated_mod)
var_869 = relay.var("var_869", dtype = "float64", shape = (1, 16, 14))#candidate|869|(1, 16, 14)|var|float64
uop_870 = relay.sigmoid(var_869.astype('float64')) # shape=(1, 16, 14)
output = uop_870
output2 = uop_870
func_883 = relay.Function([var_869,], output)
mod['func_883'] = func_883
mod = relay.transform.InferType()(mod)
var_884 = relay.var("var_884", dtype = "float64", shape = (1, 16, 14))#candidate|884|(1, 16, 14)|var|float64
output = func_883(var_884)
func_885 = relay.Function([var_884], output)
mutated_mod['func_885'] = func_885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_895 = relay.TupleGetItem(func_635_call(), 1)
call_896 = relay.TupleGetItem(func_636_call(), 1)
output = relay.Tuple([call_895,])
output2 = relay.Tuple([call_896,])
func_897 = relay.Function([], output)
mod['func_897'] = func_897
mod = relay.transform.InferType()(mod)
mutated_mod['func_897'] = func_897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_897_call = mutated_mod.get_global_var('func_897')
call_898 = func_897_call()
output = call_898
func_899 = relay.Function([], output)
mutated_mod['func_899'] = func_899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_905 = relay.TupleGetItem(func_49_call(), 0)
call_906 = relay.TupleGetItem(func_50_call(), 0)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_910 = relay.TupleGetItem(func_353_call(), 4)
call_911 = relay.TupleGetItem(func_355_call(), 4)
output = relay.Tuple([call_905,call_910,])
output2 = relay.Tuple([call_906,call_911,])
func_925 = relay.Function([], output)
mod['func_925'] = func_925
mod = relay.transform.InferType()(mod)
mutated_mod['func_925'] = func_925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mutated_mod.get_global_var('func_925')
call_926 = func_925_call()
output = call_926
func_927 = relay.Function([], output)
mutated_mod['func_927'] = func_927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_927_call = mutated_mod.get_global_var('func_927')
call_950 = relay.TupleGetItem(func_925_call(), 1)
call_951 = relay.TupleGetItem(func_927_call(), 1)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_956 = relay.TupleGetItem(func_635_call(), 1)
call_957 = relay.TupleGetItem(func_636_call(), 1)
func_848_call = mod.get_global_var('func_848')
func_851_call = mutated_mod.get_global_var('func_851')
call_961 = relay.TupleGetItem(func_848_call(relay.reshape(call_956.astype('uint8'), [8, 13, 16])), 3)
call_962 = relay.TupleGetItem(func_851_call(relay.reshape(call_956.astype('uint8'), [8, 13, 16])), 3)
func_897_call = mod.get_global_var('func_897')
func_899_call = mutated_mod.get_global_var('func_899')
call_977 = relay.TupleGetItem(func_897_call(), 0)
call_978 = relay.TupleGetItem(func_899_call(), 0)
uop_981 = relay.sigmoid(call_956.astype('float32')) # shape=(8, 13, 16)
uop_983 = relay.sigmoid(call_957.astype('float32')) # shape=(8, 13, 16)
func_752_call = mod.get_global_var('func_752')
func_755_call = mutated_mod.get_global_var('func_755')
const_1006 = relay.const([-8.258038,0.402740,5.328627,9.651499,-3.659906,2.566405,2.901209,9.949764,4.635909,8.836151,3.135481,-8.716671,4.789504,0.592512,7.342411,-6.605125,7.764523,-6.389870,-5.496443,-9.679171,-7.662318,-3.839127,-8.097803,-1.071576,-0.978549,3.368667,8.954497,4.373468,-5.616026,-7.667957,0.807106,8.285129,-9.780729,-0.978146,3.167194,5.410696,-5.381336,6.820805,-9.215555,9.189310,0.359707,-1.800967,-9.869209,8.036858,3.876022,-2.315101,0.094568,3.686056,-7.588919,-8.685697,6.760988,4.414225,0.714228,-4.521411,-0.526136,-8.957200,-9.995098,6.589231,-6.342330,4.040258,-5.482498,8.838047,2.731017,9.059816,-7.027211,7.796498,-1.914443,4.922235,6.422981,2.004200,3.508226,3.813768,-3.822642,-4.352100,-9.637051,-8.910937,-3.453335,-3.141922,3.412691,6.476884,1.765599,5.777756,8.311961,-2.181518,-2.164987,0.914445,6.958095,9.939628,7.930819,8.407279,-0.519886,-0.539679,6.917256,-2.860014,-7.474053,-6.130298,9.420585,8.195911,-1.518177,5.407224,5.196248,2.913768,-0.915065,8.235891,-9.058118,9.971574,-5.262461,2.168646,-5.065261,-5.995185,1.577048,-7.436201,-9.115579,-7.025101,2.140430,0.679691,-1.738845,-8.885342,-2.015059,-7.115644,-9.367165,1.159205,1.797967,-2.484991,-5.972553,-0.613288,5.109523,-6.640220,3.145308,-9.225991,8.813078,9.219648,-3.850679,-6.026138,6.493391,-1.626060,-4.806392,0.778127,-2.198730,3.553645,-7.540039,8.341407,-9.735015,-5.463065,-9.244617,7.262004,-7.325219,2.147969,-6.089210,6.098934,-5.192118,0.919670,8.397184,-6.275241,-5.447428,8.027646,7.672928,-1.846090,-0.113612,3.247935,7.460586,-4.617301,-8.006168,6.315318,1.912551,-7.168809,-4.845521,-7.353560], dtype = "float64")#candidate|1006|(168,)|const|float64
call_1005 = func_752_call(relay.reshape(const_1006.astype('float64'), [14, 6, 2]))
call_1007 = func_752_call(relay.reshape(const_1006.astype('float64'), [14, 6, 2]))
output = relay.Tuple([call_950,call_961,call_977,uop_981,call_1005,const_1006,])
output2 = relay.Tuple([call_951,call_962,call_978,uop_983,call_1007,const_1006,])
func_1016 = relay.Function([], output)
mod['func_1016'] = func_1016
mod = relay.transform.InferType()(mod)
mutated_mod['func_1016'] = func_1016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1016_call = mutated_mod.get_global_var('func_1016')
call_1017 = func_1016_call()
output = call_1017
func_1018 = relay.Function([], output)
mutated_mod['func_1018'] = func_1018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_1047 = relay.TupleGetItem(func_353_call(), 0)
call_1048 = relay.TupleGetItem(func_355_call(), 0)
func_848_call = mod.get_global_var('func_848')
func_851_call = mutated_mod.get_global_var('func_851')
call_1057 = relay.TupleGetItem(func_848_call(relay.reshape(call_1047.astype('uint8'), [8, 13, 16])), 1)
call_1058 = relay.TupleGetItem(func_851_call(relay.reshape(call_1047.astype('uint8'), [8, 13, 16])), 1)
func_848_call = mod.get_global_var('func_848')
func_851_call = mutated_mod.get_global_var('func_851')
call_1059 = relay.TupleGetItem(func_848_call(relay.reshape(call_1057.astype('uint8'), [8, 13, 16])), 0)
call_1060 = relay.TupleGetItem(func_851_call(relay.reshape(call_1057.astype('uint8'), [8, 13, 16])), 0)
output = relay.Tuple([call_1047,call_1057,call_1059,])
output2 = relay.Tuple([call_1048,call_1058,call_1060,])
func_1067 = relay.Function([], output)
mod['func_1067'] = func_1067
mod = relay.transform.InferType()(mod)
mutated_mod['func_1067'] = func_1067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mutated_mod.get_global_var('func_1067')
call_1068 = func_1067_call()
output = call_1068
func_1069 = relay.Function([], output)
mutated_mod['func_1069'] = func_1069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_1087 = relay.TupleGetItem(func_1016_call(), 4)
call_1088 = relay.TupleGetItem(func_1018_call(), 4)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_1101 = relay.TupleGetItem(func_635_call(), 1)
call_1102 = relay.TupleGetItem(func_636_call(), 1)
output = relay.Tuple([call_1087,call_1101,])
output2 = relay.Tuple([call_1088,call_1102,])
func_1107 = relay.Function([], output)
mod['func_1107'] = func_1107
mod = relay.transform.InferType()(mod)
mutated_mod['func_1107'] = func_1107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mutated_mod.get_global_var('func_1107')
call_1108 = func_1107_call()
output = call_1108
func_1109 = relay.Function([], output)
mutated_mod['func_1109'] = func_1109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_1179 = func_108_call()
call_1180 = func_108_call()
output = call_1179
output2 = call_1180
func_1181 = relay.Function([], output)
mod['func_1181'] = func_1181
mod = relay.transform.InferType()(mod)
mutated_mod['func_1181'] = func_1181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1181_call = mutated_mod.get_global_var('func_1181')
call_1182 = func_1181_call()
output = call_1182
func_1183 = relay.Function([], output)
mutated_mod['func_1183'] = func_1183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_927_call = mutated_mod.get_global_var('func_927')
call_1231 = relay.TupleGetItem(func_925_call(), 0)
call_1232 = relay.TupleGetItem(func_927_call(), 0)
var_1251 = relay.var("var_1251", dtype = "uint8", shape = (8, 13, 16))#candidate|1251|(8, 13, 16)|var|uint8
bop_1252 = relay.bitwise_and(call_1231.astype('uint64'), relay.reshape(var_1251.astype('uint64'), relay.shape_of(call_1231))) # shape=(8, 13, 16)
bop_1255 = relay.bitwise_and(call_1232.astype('uint64'), relay.reshape(var_1251.astype('uint64'), relay.shape_of(call_1232))) # shape=(8, 13, 16)
output = bop_1252
output2 = bop_1255
func_1264 = relay.Function([var_1251,], output)
mod['func_1264'] = func_1264
mod = relay.transform.InferType()(mod)
var_1265 = relay.var("var_1265", dtype = "uint8", shape = (8, 13, 16))#candidate|1265|(8, 13, 16)|var|uint8
output = func_1264(var_1265)
func_1266 = relay.Function([var_1265], output)
mutated_mod['func_1266'] = func_1266
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1276 = relay.var("var_1276", dtype = "float64", shape = (14, 5, 13))#candidate|1276|(14, 5, 13)|var|float64
const_1277 = relay.const([[[5.581077,0.168252,2.465907,-7.217305,-5.464408,-5.738038,2.178291,-1.044676,-2.115045,8.756187,4.849419,8.975057,7.286085],[-5.706714,-5.759278,-1.210891,7.626696,-1.574288,0.702084,4.280339,6.407066,-4.557817,7.768985,0.543900,-3.177706,-7.838722],[8.654968,-3.228038,-0.844717,-4.062422,-7.897051,-5.890152,-3.915662,0.568594,8.573647,8.716584,-9.436827,-5.976612,7.175616],[-1.411356,-4.241990,2.162148,-2.809933,-9.887404,2.710512,5.152776,6.422170,9.159438,-5.151846,7.821691,3.945695,-3.348376],[-6.478678,-4.180710,4.859007,-1.446958,4.005832,1.193899,3.266115,5.393464,-6.571558,9.237719,-0.406921,0.344363,8.551769]],[[2.306070,0.432907,-9.485672,-1.498750,3.523606,0.492884,1.711997,-0.700422,-2.550705,7.289913,-5.843848,-1.657009,7.237617],[-6.800520,-4.499590,-8.923829,1.115159,3.475626,3.369257,-0.465293,2.270187,-0.491047,-5.125210,1.015593,5.339443,-7.238604],[-1.458827,4.976073,-2.176390,-9.564963,7.328396,-7.850789,0.571323,-0.908112,6.961915,4.012433,8.701955,0.806649,-7.026879],[-8.178228,0.550409,7.050008,-5.649854,-8.912230,9.272924,9.703012,7.463472,3.279882,7.104251,2.076881,-1.129086,-9.538701],[3.113787,8.862048,-1.681412,7.329046,8.743468,-4.757396,1.472165,-6.975378,3.177300,6.541807,1.938771,8.467411,-0.425219]],[[5.524943,-8.511235,-8.363119,5.161930,5.814853,-1.090849,-3.310367,-4.456779,3.498267,3.888560,-9.563281,4.892825,6.233496],[-2.966790,8.454447,0.191989,7.248591,-1.377777,6.318166,5.751615,-6.272240,6.282652,0.180115,2.564557,4.537499,-5.790524],[5.809793,0.703458,-7.826535,-0.928832,3.227245,-2.320710,1.277868,-3.003066,3.583883,9.720052,7.582614,-6.969966,-5.033077],[9.421284,-9.166955,5.972901,2.407634,-7.963441,-2.302960,-1.003010,-8.183366,-2.861518,0.672203,2.562948,1.332691,-5.800597],[3.565233,3.440366,-4.286801,-0.271852,6.606819,1.010110,-0.353818,-5.417374,-0.679965,-8.015311,-8.737365,-5.899554,-9.680671]],[[-3.464106,-0.210085,-7.449797,8.913483,-4.653329,9.096739,-5.585204,-7.308858,0.593516,4.955568,-0.757973,-9.225260,-8.046611],[2.282880,1.206051,-9.419623,0.276840,-3.077646,8.310777,-2.773572,-2.088676,-0.503240,-1.501108,-1.986964,7.699575,6.742259],[8.902265,4.265873,-3.863320,-6.126094,-1.711867,8.095807,8.760035,3.935217,7.204873,-0.527388,5.404077,-9.038497,-7.603596],[-6.243084,-1.432227,7.314468,5.136852,-5.214586,3.347514,3.393977,5.059684,-7.141285,4.379493,8.331250,6.938669,-3.687961],[-5.143197,-3.212209,1.636610,0.313025,-7.531383,7.235076,3.216231,-8.427257,-1.495911,-1.573239,-2.923306,-0.669874,-7.966582]],[[3.376670,-3.517491,0.136849,-6.511971,0.443001,-6.216062,-4.875133,2.183302,-4.327653,8.877806,7.544144,9.146480,7.788914],[-4.126093,0.045910,-8.325649,-0.238914,-9.081301,7.088618,5.572912,-0.267978,4.610361,8.982183,-0.279652,9.599269,-8.348926],[1.683275,-8.084336,5.096979,-6.824210,-3.954638,5.229945,4.667120,-5.586797,4.700546,2.700909,4.489829,-5.757604,3.598032],[-3.040547,-7.321073,-6.157447,-1.494225,-9.848742,0.852409,-3.752980,3.111553,7.418131,5.881102,-4.776559,7.693371,-1.802591],[-2.850197,4.841342,4.492919,7.612288,-1.523388,7.538632,-4.884704,0.884262,8.480290,6.130348,5.981955,8.076982,-1.011256]],[[9.120041,-3.992821,-9.910717,-4.866913,-4.685409,-5.968596,6.388271,4.847655,9.407249,4.984228,-7.468033,2.124089,8.873090],[-2.023895,0.407237,-7.909296,-2.397740,1.548426,-3.098713,9.949336,6.329959,-0.719268,-0.988458,-7.984929,4.931820,-1.457089],[-9.081979,-3.574090,7.950496,-5.808992,3.949374,9.954923,1.424236,6.088453,7.454569,3.519900,-4.046638,8.177708,3.664590],[-0.941746,4.942287,-9.816079,-1.318276,-2.592238,8.498723,0.883813,7.607458,6.016972,8.166406,-3.409723,8.159774,9.943302],[5.954683,-4.026293,-8.773409,-8.182669,-8.705756,8.655425,3.888006,-6.377470,4.405929,2.715803,-0.846150,7.798180,0.221497]],[[-8.691732,9.090877,-2.033629,9.261965,-0.661551,-5.624177,7.804329,9.397054,5.902806,-5.249310,-8.907575,8.125310,7.064481],[-2.611760,4.988755,-9.809140,-4.098469,-4.203804,8.806041,9.138204,3.411050,-6.180106,-4.315662,-3.184682,-2.490273,1.867515],[-6.534042,-6.162265,5.939588,-5.274353,9.137232,-0.285283,7.765052,-1.740577,-6.639391,-8.630915,3.037903,7.570912,-5.268438],[-5.105663,-5.651993,1.963349,-0.294791,-8.904180,-4.889718,9.827139,-9.698167,8.136135,-0.138045,-6.186224,-6.161177,-5.795285],[4.942147,6.957664,9.396075,-2.781324,-6.349767,-1.301509,3.696278,-6.367980,-0.290958,4.298891,0.411319,-3.147959,8.065916]],[[3.282119,1.674019,8.231824,9.290987,-6.483636,-1.141269,-4.032878,2.416942,-3.547754,-1.548863,-3.413277,-4.148076,3.985693],[2.520208,6.174034,-2.926544,-7.402101,-5.412394,-9.377216,-7.771266,2.137593,2.099854,4.887958,-3.327887,4.871826,-5.649660],[8.917919,-4.849731,0.026807,-1.453251,-4.073679,9.461153,-8.567370,-7.580248,0.780562,-4.235175,-7.841850,-1.324780,-6.104876],[1.833410,1.599143,8.470147,-0.644816,6.489484,3.978873,-2.462583,-6.959088,-2.376675,3.056553,4.492319,-1.845091,8.624904],[9.273560,-9.951322,8.092752,-8.330643,-5.870254,3.215320,0.342261,-7.483287,5.753899,-0.210916,-9.332825,-3.343329,0.501976]],[[-1.191586,3.246556,-5.777426,7.878299,-0.882293,-3.625084,-2.229726,3.947955,8.224205,-3.251590,0.047830,-9.558070,-5.551064],[5.169299,4.173058,-5.242121,-2.219519,4.283574,8.106445,1.494855,1.698885,-4.787498,-3.773453,-6.476380,-2.627973,7.970968],[-2.033678,2.319247,-6.780507,8.433848,6.024377,9.201875,-3.959280,9.054301,-8.168804,6.915063,-7.080778,3.967991,8.688323],[1.117102,-1.113104,-3.655726,-0.447795,6.041048,-5.039125,-2.925184,8.082005,1.863190,8.875032,4.553991,7.916537,3.001942],[-7.128546,9.081595,-4.835925,7.557574,5.443999,1.586358,4.416879,9.307495,-7.719446,7.220371,3.168354,3.192356,1.855697]],[[-1.630041,8.848302,4.779924,-0.122401,-8.067963,8.887048,-9.222225,9.075370,-2.306604,-9.080135,-1.126922,-2.828233,-9.225710],[-7.081133,-5.071401,-3.151331,-0.027277,-9.814345,4.216651,-0.617760,-9.774486,9.360394,9.720021,-3.040855,6.678763,8.606265],[5.443248,-3.091036,2.068763,4.873496,-1.545433,9.554218,-2.669526,-1.275729,-0.922609,2.990796,-6.353264,6.582891,4.185756],[-3.995858,6.401253,-4.926820,8.529995,-2.377067,8.340859,-0.808276,-6.954767,-7.703220,5.056194,-9.179140,-5.634931,-7.401595],[3.801818,-0.129293,-6.049873,0.940389,-6.855403,-8.730201,-7.047362,-4.786488,8.914813,-3.209095,-5.382101,-1.896328,2.430395]],[[-9.938338,-9.625485,4.845944,-0.115039,-6.359625,-2.364584,-1.442228,2.714229,-7.048786,-2.676919,1.788868,6.247532,9.638918],[-7.425297,4.935115,-7.296633,1.624715,0.532622,-0.239505,-6.175081,-0.300815,2.114210,9.966958,0.642515,-0.669502,1.438848],[4.158641,0.867915,-6.493711,-2.050234,-4.436014,0.829061,6.007294,-2.930684,9.934135,-1.363202,7.349880,-9.500014,-8.874347],[-7.181712,8.942765,-1.529266,-9.996756,8.609512,-1.572485,-0.071845,8.366738,-9.992831,-8.350915,-9.279737,-1.808673,4.426413],[-2.675003,-8.048348,-1.252798,-8.308078,-1.935960,-6.971265,-3.817019,-9.277058,-9.032447,1.339448,-9.523278,-0.063885,-6.509470]],[[-2.830704,-4.800263,-1.557048,-0.304494,2.221416,0.992265,-1.767041,4.814577,-9.731010,3.809935,-4.714815,-3.132543,9.585834],[8.234806,7.600086,-9.245312,-8.636510,-6.260560,-7.150013,-7.823063,3.076313,1.039808,7.824449,-4.153705,-6.018762,-5.259436],[3.585886,4.210872,-0.121059,2.146031,-4.824879,0.767447,-8.769289,-8.387560,-4.658387,-6.134728,-4.369989,-2.025040,-6.935333],[-3.712189,-2.185049,8.536078,2.253265,-5.810989,-3.420117,0.601208,6.605505,4.140431,-5.085694,-0.222202,-6.289840,-3.975070],[-5.779824,8.145336,-4.350526,-8.802063,-5.165390,-5.464010,-1.463030,6.739024,-6.499532,5.422855,-3.316936,4.321515,-7.464495]],[[7.786545,6.658711,-3.403814,-3.227197,-9.314266,8.601686,3.305820,0.617098,7.624063,-2.442412,-8.268893,5.254427,9.842878],[-9.313419,7.275238,-7.421869,-5.838556,-1.786628,-6.127123,-2.467666,8.306684,6.003465,3.759520,3.576559,-6.150050,-9.493825],[-7.462625,-1.851505,8.885658,2.237053,-7.073364,0.573494,6.970080,3.359853,9.312925,-8.180687,5.246461,0.488369,-0.580984],[8.616410,7.158669,9.281514,0.833450,7.603443,3.277045,4.023056,-5.193387,-0.203700,1.842115,7.680061,3.110401,0.736007],[6.620214,8.784428,7.189684,-4.020779,-1.584232,3.904872,-7.048176,-4.621921,1.006717,5.240046,0.062052,0.656174,3.186148]],[[2.904259,-3.423665,6.713978,4.878830,-2.197405,3.904052,6.703625,-4.115120,8.733846,7.543543,-8.365562,-0.181513,5.980386],[0.477610,-9.976469,4.060784,1.779319,-9.457387,-2.908766,-9.365557,6.505698,2.515087,4.212651,3.819961,-0.624631,9.244095],[9.575241,-7.555959,9.178338,2.255257,-8.500381,0.653383,-0.609525,-3.401607,5.853994,7.458675,-7.506454,-9.178279,1.877864],[1.676794,-2.700399,-4.006726,-7.526950,-2.983047,8.321669,2.554068,2.676338,0.437052,-9.792732,-1.660463,-0.840542,-7.834935],[-3.175596,8.369189,-4.089973,-9.849072,0.600148,-1.439178,8.109425,4.286945,-5.287190,4.377997,6.187573,-3.169791,-3.056370]]], dtype = "float64")#candidate|1277|(14, 5, 13)|const|float64
bop_1278 = relay.floor_divide(var_1276.astype('float64'), relay.reshape(const_1277.astype('float64'), relay.shape_of(var_1276))) # shape=(14, 5, 13)
bop_1284 = relay.less_equal(const_1277.astype('bool'), relay.reshape(bop_1278.astype('bool'), relay.shape_of(const_1277))) # shape=(14, 5, 13)
uop_1292 = relay.log(bop_1278.astype('float32')) # shape=(14, 5, 13)
output = relay.Tuple([bop_1284,uop_1292,])
output2 = relay.Tuple([bop_1284,uop_1292,])
func_1296 = relay.Function([var_1276,], output)
mod['func_1296'] = func_1296
mod = relay.transform.InferType()(mod)
var_1297 = relay.var("var_1297", dtype = "float64", shape = (14, 5, 13))#candidate|1297|(14, 5, 13)|var|float64
output = func_1296(var_1297)
func_1298 = relay.Function([var_1297], output)
mutated_mod['func_1298'] = func_1298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_1387 = relay.TupleGetItem(func_635_call(), 1)
call_1388 = relay.TupleGetItem(func_636_call(), 1)
output = call_1387
output2 = call_1388
func_1396 = relay.Function([], output)
mod['func_1396'] = func_1396
mod = relay.transform.InferType()(mod)
output = func_1396()
func_1397 = relay.Function([], output)
mutated_mod['func_1397'] = func_1397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_1417 = relay.TupleGetItem(func_49_call(), 0)
call_1418 = relay.TupleGetItem(func_50_call(), 0)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_1432 = func_108_call()
call_1433 = func_108_call()
func_487_call = mod.get_global_var('func_487')
func_489_call = mutated_mod.get_global_var('func_489')
const_1440 = relay.const([-6,7,-1,4,-7,7,10,-7,4,9,-3,-3,-3,-5,-9,-9,-1,-6,1,8,-8,-7,4,7,5,-7,6,-1,-4,-4,-7,7,-3,2,4,-10,-6,3,1,9,3,-4,8,1,-4,-5,10,-10,-7,-7,-4,-5,5,10,5,2,5,-10,3,-5,6,1,3,1,4,1,6,-8,-4,-9,-8,-9,-8,8,-10,-2,2,-6,-5,-7,6,6,-5,-5,3,-8,-6,7,-5,7,7,-2,3,6,-7,-6,2,-5,8,-4,5,-3,-6,-4,5,-6,3,1,-8,-5,-9,-7,4,-8,3,3,-1,-8,-7,9,4,-4,3,-2,-2,7,-9,-4,8,3,-3,9,3,2,10,1,9,10,1,-5,10,-6,-6,-9,-2,6,-9,1,4,1,7,7,-7,7,8,1,-4,4,7,4,8,-5,9,-8,-9,7,10,1,-1,-5,10,5,-3,4,6,9,10,-10,8,-1,6,-3,2,-6,-2,-1,9,8,7,-1,-2,7,-2,2,-7,-7,3,-1,-5,9,10,-4,6,-8,-4,7,9,1,-3,1,5,4,1,-2,-2,6,9,-8,1,-1,7,2,-4,-7,-5,-6,8,8,-5,6,9,9,3,4,-7,9,-3,-2,-6,-3,-9,3,10,7,-10,-5,8,-9,-3,-4,-10,-4,6,9,3,6,2,9,9,-9,2,7,8,-10,-1,-9,7,-3,9,6,-5,-4,-10,-2,3,-7,7,-5,-10,-8,-7,-3,2,7,9,3,-8,4,2,-8,-9,-9,8,3,-7,10,-8,10,8,-9,-3,-2,1,-10,4,-9,-2,9,-2,-8,1,-5,-1,-7,4,-8,10,9,-8,4,6,4,10,6,8,-3,3,8,-2,-7,-4,-3,-6,4,1,7,9,-5,-9,-3,6,5,-3,-7,1,1,-10,-8,7,2,9,-5,-5,1,3,10,-9,1,10,-9,4,4,4,-10,-5,-9,6,-7,6,4,2,-9,10,5,1,-1,-3,9], dtype = "uint64")#candidate|1440|(378,)|const|uint64
call_1439 = relay.TupleGetItem(func_487_call(relay.reshape(const_1440.astype('uint64'), [6, 63])), 0)
call_1441 = relay.TupleGetItem(func_489_call(relay.reshape(const_1440.astype('uint64'), [6, 63])), 0)
func_1181_call = mod.get_global_var('func_1181')
func_1183_call = mutated_mod.get_global_var('func_1183')
call_1449 = func_1181_call()
call_1450 = func_1181_call()
bop_1487 = relay.add(call_1417.astype('int8'), relay.reshape(call_1449.astype('int8'), relay.shape_of(call_1417))) # shape=(8, 13, 16)
bop_1490 = relay.add(call_1418.astype('int8'), relay.reshape(call_1450.astype('int8'), relay.shape_of(call_1418))) # shape=(8, 13, 16)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_1495 = relay.TupleGetItem(func_1016_call(), 0)
call_1496 = relay.TupleGetItem(func_1018_call(), 0)
output = relay.Tuple([call_1432,call_1439,const_1440,bop_1487,call_1495,])
output2 = relay.Tuple([call_1433,call_1441,const_1440,bop_1490,call_1496,])
func_1501 = relay.Function([], output)
mod['func_1501'] = func_1501
mod = relay.transform.InferType()(mod)
output = func_1501()
func_1502 = relay.Function([], output)
mutated_mod['func_1502'] = func_1502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_897_call = mod.get_global_var('func_897')
func_899_call = mutated_mod.get_global_var('func_899')
call_1506 = relay.TupleGetItem(func_897_call(), 0)
call_1507 = relay.TupleGetItem(func_899_call(), 0)
func_897_call = mod.get_global_var('func_897')
func_899_call = mutated_mod.get_global_var('func_899')
call_1509 = relay.TupleGetItem(func_897_call(), 0)
call_1510 = relay.TupleGetItem(func_899_call(), 0)
output = relay.Tuple([call_1506,call_1509,])
output2 = relay.Tuple([call_1507,call_1510,])
func_1515 = relay.Function([], output)
mod['func_1515'] = func_1515
mod = relay.transform.InferType()(mod)
output = func_1515()
func_1516 = relay.Function([], output)
mutated_mod['func_1516'] = func_1516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1501_call = mod.get_global_var('func_1501')
func_1502_call = mutated_mod.get_global_var('func_1502')
call_1612 = relay.TupleGetItem(func_1501_call(), 0)
call_1613 = relay.TupleGetItem(func_1502_call(), 0)
output = call_1612
output2 = call_1613
func_1622 = relay.Function([], output)
mod['func_1622'] = func_1622
mod = relay.transform.InferType()(mod)
output = func_1622()
func_1623 = relay.Function([], output)
mutated_mod['func_1623'] = func_1623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_1673 = relay.TupleGetItem(func_449_call(), 1)
call_1674 = relay.TupleGetItem(func_451_call(), 1)
output = relay.Tuple([call_1673,])
output2 = relay.Tuple([call_1674,])
func_1682 = relay.Function([], output)
mod['func_1682'] = func_1682
mod = relay.transform.InferType()(mod)
mutated_mod['func_1682'] = func_1682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1682_call = mutated_mod.get_global_var('func_1682')
call_1683 = func_1682_call()
output = call_1683
func_1684 = relay.Function([], output)
mutated_mod['func_1684'] = func_1684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1682_call = mod.get_global_var('func_1682')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_1720 = relay.TupleGetItem(func_1682_call(), 0)
call_1721 = relay.TupleGetItem(func_1684_call(), 0)
func_1296_call = mod.get_global_var('func_1296')
func_1298_call = mutated_mod.get_global_var('func_1298')
const_1741 = relay.const([2.888966,-6.750854,-7.527498,3.377272,-7.947858,-7.456173,-6.913122,1.187686,-8.781704,-8.188393,-3.708054,1.241290,4.299182,9.014281,8.842416,-0.072299,-3.226470,5.725147,9.202500,-9.034943,5.662240,1.331210,-3.905033,-9.384548,8.743358,-3.862146,-0.652213,3.338255,5.123446,-4.606785,-9.427889,7.032327,-8.390488,3.163315,-4.352678,1.186739,-4.153808,9.858338,8.244286,-4.988389,-8.700377,-1.111807,-9.483775,5.775162,-6.124708,6.918473,-8.816732,-3.835368,8.464878,6.498761,4.724022,-7.717651,3.095902,-0.075243,4.008537,-1.747774,-0.919711,9.317934,-6.711390,-4.924879,-2.506488,9.180554,-5.044169,8.773688,-1.782254,7.498344,0.155941,6.999793,7.356649,8.410814,-4.322997,9.292395,-3.307189,-9.801610,1.353963,-2.543145,-7.802615,-9.549881,4.570283,-3.954543,-6.330015,4.108158,8.985380,4.226816,-6.730300,-5.674630,-0.796909,1.156899,-7.105359,5.817436,-9.923747,4.235485,-3.247775,-8.468434,-4.817201,8.508593,-2.711782,-0.348079,4.234801,4.963577,5.326451,8.612714,7.014316,-5.195816,-7.911216,4.430759,5.657511,6.460337,-3.310432,6.054902,-4.966863,-0.781589,7.148900,0.735125,-9.860201,7.970296,-7.330921,8.663969,6.150345,4.646274,9.759906,5.079681,9.985010,-1.335900,-8.606991,-5.147703,-6.621201,5.494456,-0.381191,4.620789,0.490141,-2.956020,5.074852,9.179124,7.701020,-7.370135,2.203924,-2.463501,-9.728983,7.020894,-1.534774,3.647279,-3.024755,8.543952,3.531639,0.480827,7.967936,-4.622948,0.718495,0.716441,-7.792452,0.052591,9.744452,0.821721,0.153156,-3.279531,-5.581449,-8.949670,0.503417,3.128349,-6.444075,3.744568,-0.371757,-8.226275,-9.466623,6.817458,6.214550,-4.738800,-9.858778,-6.965021,-1.746930,4.307962,7.510379,8.651305,1.388059,6.990784,0.243366,7.563295,8.292479,1.810542,-4.237255,-3.286217,-2.001145,-4.314283,-0.458393,-1.270460,-1.106405,-0.850498,6.453412,-4.771469,-0.740347,9.745394,-3.246656,-5.044248,-8.275992,5.820292,-5.653014,0.554150,3.115786,5.558659,-9.129306,-6.530875,2.836186,-9.809178,2.049705,-2.940173,1.509897,9.057288,-6.551741,5.232034,-9.964135,4.218051,-1.508654,4.901451,4.677716,-1.104121,-3.853045,-3.812219,1.993868,-1.484150,5.471684,-2.796502,-6.271498,-4.567626,6.584618,-5.275231,1.691153,-7.995009,-1.319103,7.210525,-6.779315,2.650731,-7.381600,7.813423,4.961715,-1.332535,-5.436579,2.276564,1.849154,9.595374,9.120521,-6.354380,-9.709484,-2.838954,-2.003474,-5.138123,4.832881,0.316525,1.520100,4.432894,-1.120635,3.606535,0.715888,-3.115374,-4.244961,5.910598,9.296659,-8.521681,1.836909,-4.488478,-4.940795,-6.225660,-6.657569,-6.761768,-7.177241,-8.347530,6.837089,0.231693,-9.275858,3.743910,-2.578303,-0.494540,-9.845816,3.794565,-9.048214,3.865776,-7.237493,-2.205407,2.155512,-5.458716,7.319821,3.484232,-4.906627,5.567471,-2.372043,8.633097,8.078483,-2.661537,4.699940,2.212466,5.205237,-4.063369,5.805333,-7.481719,7.337428,-8.215378,-9.202678,-8.439314,0.611898,0.628573,-1.310247,-4.702747,5.740696,-3.763625,-6.496687,-8.668004,-6.243178,3.641844,7.905880,1.710447,-6.138276,8.802687,9.132613,8.650767,0.668143,-3.866783,4.481739,-3.290179,7.422980,9.122387,-0.468855,3.069204,4.874634,-3.475153,-2.517918,6.090372,-7.785965,8.875216,-3.803971,-1.980034,-9.689804,-5.563516,7.751572,-3.622860,3.349813,-9.902316,6.450537,-8.570373,-4.293683,5.771510,-7.138013,9.906281,-6.131976,-8.316704,7.105285,-4.258867,5.211189,2.972959,1.590265,1.781491,-1.795615,5.189879,9.860847,-5.592232,-2.071399,4.403670,-9.698071,7.878466,7.170930,-7.294624,-7.825621,-4.503202,1.873392,-4.706737,1.247174,6.279408,5.677609,0.887153,-1.830792,-9.086191,-1.856003,-5.312263,-6.402387,8.281509,1.231335,-8.174504,-6.846127,-3.730768,1.529421,6.108341,-2.873505,-6.571666,0.552909,7.704758,7.621242,-8.317635,0.253392,-1.235303,9.948243,1.959786,1.392617,-9.427406,7.863556,2.418619,-6.208035,3.552359,8.463768,-2.863728,-8.238328,1.028201,-9.647017,6.357083,-4.333498,2.848555,4.040327,-8.575557,2.755286,-0.957296,8.685519,1.828604,-3.987318,0.013446,-7.826648,-7.115719,2.482140,-5.559954,-1.919029,7.548916,8.777606,-7.521394,9.489676,-6.683104,7.596670,8.385881,-8.713359,-4.633986,-5.127752,6.325274,-7.723924,7.171433,3.657102,8.920665,0.357760,-7.492473,4.639686,7.472835,5.100314,9.495803,-6.329035,-0.099236,3.817707,-3.690706,-3.527415,-3.741216,8.276142,-5.622714,8.426433,-6.898745,-5.620910,-2.635680,0.147811,-5.501657,5.718204,-4.465546,2.211004,-6.962858,5.171690,-4.467640,-6.913195,-6.806343,-5.631744,-0.014585,-4.978771,-8.925805,0.745728,5.331972,-4.502049,-4.092040,5.700574,8.652197,0.832901,-5.771984,-7.980363,-5.113140,3.737467,0.445142,6.722001,-3.090487,-1.469687,-5.145007,6.379500,5.167168,1.544417,6.653969,-8.021225,0.632713,-3.873401,-8.175432,-4.655974,-8.171522,-5.443473,0.798301,3.346697,8.978435,-4.844337,-5.053862,4.863740,3.546309,4.292267,-8.619617,-1.304043,7.524382,4.120467,0.122403,-9.429382,8.366518,2.419105,-4.785201,-6.120716,1.827536,4.483375,-8.452469,3.891218,7.185074,-4.803297,-5.913294,-0.050369,-6.357573,9.705942,5.624804,0.154707,-0.592504,-1.743619,5.739936,2.052880,9.374949,-9.298420,1.314709,-9.195853,-0.220794,-3.281222,9.341829,-4.482766,-3.304493,5.521291,5.513216,6.528173,-2.178753,-9.237674,-4.059279,-4.395117,-3.462028,-4.605414,-3.518176,8.784510,6.386456,1.234064,-5.958829,-9.344675,7.568751,-0.430015,-3.514183,6.996336,4.907809,4.229981,7.746002,-6.993196,-5.196403,5.679609,5.760271,-5.213656,5.384858,1.762921,3.208261,-1.096904,3.459147,-0.400401,-2.850210,-5.426444,9.192868,-9.164970,9.636365,6.049721,2.382870,-3.672698,5.270563,2.400450,-3.207165,-9.581963,7.053084,4.826394,1.164597,-4.122716,6.001323,-3.080316,-7.124585,1.819606,1.051767,-5.389547,5.134412,0.565631,2.613109,6.805887,6.957740,2.399803,9.940263,5.476250,-1.707772,-1.145912,1.532646,8.709071,4.203850,8.278959,6.029982,6.544883,4.067504,3.339560,-6.534135,-5.939355,-3.123264,-2.030842,-9.410373,-8.404578,5.682445,-2.984820,8.646757,3.982099,-7.756871,0.918062,-2.918990,8.761602,0.665455,-9.771194,7.682507,0.126097,-2.574194,6.829464,-8.284588,-5.674030,0.803682,-5.389908,-7.585712,1.811359,-1.697764,-7.621056,-7.777428,-8.353421,-0.631427,7.646691,-0.559255,4.757512,-0.763473,5.733507,-0.233464,-3.729632,9.657404,8.999304,-7.085539,-1.477184,5.521891,1.220433,-1.411192,-2.235060,-7.429572,9.983091,-4.957107,-6.490521,4.447699,3.554370,8.094899,3.144337,-4.818168,-3.948738,-9.200385,-6.631291,4.873819,8.252982,7.823894,-6.496453,2.392797,-8.373240,-0.829757,-2.320495,3.446936,7.962582,9.278631,0.772557,3.697677,2.921383,-9.892873,-4.838357,0.637772,-8.359105,0.865727,7.583127,-2.249930,-3.909254,-3.440506,-7.624601,8.051490,-7.329487,1.054561,-3.922261,4.335352,-2.343227,7.297246,2.688089,-8.890886,-4.898981,-1.017328,-0.081567,0.060030,9.745566,3.716771,3.724230,9.989210,7.477408,7.494153,-1.517680,6.232166,1.152447,2.880855,-7.457485,-4.299605,0.047272,-1.411468,9.491138,-9.294294,5.999257,-1.444090,-5.771803,-8.973066,-3.364312,-8.110504,-4.521477,5.713872,-8.239551,-2.389028,-0.832977,6.046904,3.907428,8.072860,-5.615944,1.813447,1.889312,-1.797769,0.820542,-1.415336,5.572368,-9.624357,-1.688847,5.341282,-2.021726,5.185752,-6.230586,-0.039958,-7.518881,-3.582812,-5.697177,-1.643908,4.787312,4.811383,1.528258,8.352426,-8.378464,-5.437197,4.897787,-0.897156,6.533507,5.537774,-3.905456,8.452839,3.993852,6.338672,0.117443,-8.666734,3.584307,-0.741867,1.961128,5.241621,0.593237,-7.749364,6.007034,1.654270,1.264412,-2.594487,-5.341018,-3.072913,1.894193,8.291271,-0.477188,8.223077,-8.755736,-0.138026,3.526997,3.730731,-7.572795,-2.484654,-6.863375,-5.702122,-8.124022,-7.952180,8.880147,-1.027395,-2.621879,5.152033,5.264688,-6.816847,-7.026479,1.431718,-5.406172,8.258787,7.757390,-1.015756,0.001683,4.690526,2.675147,-5.638389,-0.407433,5.328321,0.162398,7.227350,-6.773799,-2.983885,4.487254,-0.626838,-7.834912,-3.565993,7.033986,-6.983965,3.101939,-1.609729,4.381790,5.046407,-3.332192,-8.711620,-6.580843,-6.123754,-1.176197,3.637849,5.605652,0.333228,6.058261,8.582522,7.886812,2.021174,8.400199,1.829459,3.725980,-2.252280,-5.375045,5.796281,8.957113,2.321118,-2.464479,9.016587,-6.933331,7.154265,-7.088085,7.836132,-1.824596,-5.108299,-1.738120,-7.013116,8.127379,2.441347,-6.862318,-8.278004,5.640662,0.867266,-7.616574,4.429690,6.076450,7.021961,8.495989,7.410380,4.958455,0.438934,-4.126103,0.510812,-3.711841,1.614898,0.547185,-0.900663,0.366934,-3.921007,-3.090327,-8.065989,1.787278,0.850048,-6.880534,-9.736378,7.562671,-3.716984,-7.643710,9.780372,-1.704578,2.863691,-1.672040,-2.311256,5.430911,1.677625,-9.750706,1.961907,4.400829,-0.222530,-4.611077,-9.099024,-4.377688,9.983221,-6.236017,-6.469534,1.406582,6.136113,9.179513,2.255688,-2.962075,7.981608,-0.388449,-0.377364], dtype = "float64")#candidate|1741|(910,)|const|float64
call_1740 = relay.TupleGetItem(func_1296_call(relay.reshape(const_1741.astype('float64'), [14, 5, 13])), 0)
call_1742 = relay.TupleGetItem(func_1298_call(relay.reshape(const_1741.astype('float64'), [14, 5, 13])), 0)
bop_1747 = relay.floor_mod(call_1740.astype('float64'), relay.reshape(const_1741.astype('float64'), relay.shape_of(call_1740))) # shape=(14, 5, 13)
bop_1750 = relay.floor_mod(call_1742.astype('float64'), relay.reshape(const_1741.astype('float64'), relay.shape_of(call_1742))) # shape=(14, 5, 13)
func_925_call = mod.get_global_var('func_925')
func_927_call = mutated_mod.get_global_var('func_927')
call_1762 = relay.TupleGetItem(func_925_call(), 0)
call_1763 = relay.TupleGetItem(func_927_call(), 0)
output = relay.Tuple([call_1720,bop_1747,call_1762,])
output2 = relay.Tuple([call_1721,bop_1750,call_1763,])
func_1769 = relay.Function([], output)
mod['func_1769'] = func_1769
mod = relay.transform.InferType()(mod)
mutated_mod['func_1769'] = func_1769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mutated_mod.get_global_var('func_1769')
call_1770 = func_1769_call()
output = call_1770
func_1771 = relay.Function([], output)
mutated_mod['func_1771'] = func_1771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_1903 = func_108_call()
call_1904 = func_108_call()
func_200_call = mod.get_global_var('func_200')
func_202_call = mutated_mod.get_global_var('func_202')
call_1905 = relay.TupleGetItem(func_200_call(relay.reshape(call_1903.astype('uint8'), [8, 13, 16])), 2)
call_1906 = relay.TupleGetItem(func_202_call(relay.reshape(call_1903.astype('uint8'), [8, 13, 16])), 2)
output = relay.Tuple([call_1903,call_1905,])
output2 = relay.Tuple([call_1904,call_1906,])
func_1909 = relay.Function([], output)
mod['func_1909'] = func_1909
mod = relay.transform.InferType()(mod)
output = func_1909()
func_1910 = relay.Function([], output)
mutated_mod['func_1910'] = func_1910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_1915 = relay.TupleGetItem(func_449_call(), 2)
call_1916 = relay.TupleGetItem(func_451_call(), 2)
uop_1917 = relay.cos(call_1915.astype('float64')) # shape=(9, 14, 3)
uop_1919 = relay.cos(call_1916.astype('float64')) # shape=(9, 14, 3)
bop_1926 = relay.divide(call_1915.astype('float64'), relay.reshape(uop_1917.astype('float64'), relay.shape_of(call_1915))) # shape=(9, 14, 3)
bop_1929 = relay.divide(call_1916.astype('float64'), relay.reshape(uop_1919.astype('float64'), relay.shape_of(call_1916))) # shape=(9, 14, 3)
bop_1930 = relay.left_shift(bop_1926.astype('uint32'), relay.reshape(uop_1917.astype('uint32'), relay.shape_of(bop_1926))) # shape=(9, 14, 3)
bop_1933 = relay.left_shift(bop_1929.astype('uint32'), relay.reshape(uop_1919.astype('uint32'), relay.shape_of(bop_1929))) # shape=(9, 14, 3)
func_1909_call = mod.get_global_var('func_1909')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_1944 = relay.TupleGetItem(func_1909_call(), 0)
call_1945 = relay.TupleGetItem(func_1910_call(), 0)
output = relay.Tuple([bop_1930,call_1944,])
output2 = relay.Tuple([bop_1933,call_1945,])
func_1947 = relay.Function([], output)
mod['func_1947'] = func_1947
mod = relay.transform.InferType()(mod)
mutated_mod['func_1947'] = func_1947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1947_call = mutated_mod.get_global_var('func_1947')
call_1948 = func_1947_call()
output = call_1948
func_1949 = relay.Function([], output)
mutated_mod['func_1949'] = func_1949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_1975 = func_1396_call()
call_1976 = func_1396_call()
func_848_call = mod.get_global_var('func_848')
func_851_call = mutated_mod.get_global_var('func_851')
call_2010 = relay.TupleGetItem(func_848_call(relay.reshape(call_1975.astype('uint8'), [8, 13, 16])), 0)
call_2011 = relay.TupleGetItem(func_851_call(relay.reshape(call_1975.astype('uint8'), [8, 13, 16])), 0)
output = relay.Tuple([call_1975,call_2010,])
output2 = relay.Tuple([call_1976,call_2011,])
func_2016 = relay.Function([], output)
mod['func_2016'] = func_2016
mod = relay.transform.InferType()(mod)
output = func_2016()
func_2017 = relay.Function([], output)
mutated_mod['func_2017'] = func_2017
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2052 = relay.var("var_2052", dtype = "uint8", shape = (14, 12, 10))#candidate|2052|(14, 12, 10)|var|uint8
var_2053 = relay.var("var_2053", dtype = "uint8", shape = (14, 12, 10))#candidate|2053|(14, 12, 10)|var|uint8
bop_2054 = relay.bitwise_or(var_2052.astype('uint8'), relay.reshape(var_2053.astype('uint8'), relay.shape_of(var_2052))) # shape=(14, 12, 10)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
var_2058 = relay.var("var_2058", dtype = "uint8", shape = ())#candidate|2058|()|var|uint8
const_2059 = relay.const([5,2,5,10,-2,-10,-7,3,-3,-6,5,7,2,9,10,-9,-6,-8,-8,10,-9,6,-9,7,-8,-4,-8,-8,-3,-8,5,-8,10,-3,4,10,-6,-9,-9,-9,-3,10,4,-2,7,9,-7,4,-3,-8,10,2,8,1,2,-6,10,4,6,-2,4,-6,8,-10,4,-10,10,10,-5,-7,10,-10,9,-6,-10,9,-10,8,-2,-1,-8,3,-4,8,-6,6,6,6,-2,2,3,-7,-6,-10,-5,9,3,3,-6,7,-4,8,9,-7,10,-4,-3,-3,5,-1,6,4,-1,5,8,9,-4,-3,-5,-5,-2,-6,-9,-7,-4,-5,-8,2,-5,-9,10,4,9,9,8,6,3,6,-3,-6,-3,9,-9,-3,7,-9,3,1,3,-3,3,2,3,8,2,3,7,7,1,2,3,5,7,8,-5,2,2,4,1,-1,7,6,-4,-10,4,-4,-5,3,-4,-3,-3,7,-6,-3,4,-10,6,5,-1,-4,8,4,-7,-7,-9,10,-7,9,7,-2,4,1,10,-9,-2,-7,-2,-6,-7,10,5,-10,-6,-6,1,-3,10,6,-2,2,-7,-6,8,-8,5,5,-7,-10,5,7,6,2,3,-7,-2,-1,-5,-10,7,2,-7,1,1,10,-7,-4,4,-10,-4,4,-5,-9,-1,7,-8,-1,-3,2,4,-2,6,6,1,-8,3,3,8,10,10,9,-6,4,3,-5,-5,-7,-2,2,1,10,-2,3,4,9,-3,-3,-1,10,2,-10,-4,-9,-2,-2,9,-6,-5,-10,4,-3,2,-8,3,-8,5,2,-6,8,2,-10,1,1,-7,-5,4,10,3,8,5,-1,-3,10,5,-9,7,7,7,6,-3,-5,-8,-1,-4,-9,7,1,-6,-1,-8,-8,-10,-7,-7,1,3,-4,-4,1,8,-6,1,-4,8,-8,8,5,4,-6,-4,-8,-6,5,-9,-7,10,1,3,-8,3,-9,-5,10,8,-8,-3,-7,-9,9,3,-7,9,6,-3,5,2,8,10,-7,-4,-1,1,7,2,-10,-2,-10,4,5,10,-5,3,2,-3,-10,-3,-7,-8,-4,10,7,-10,-5,3,-4,-7,5,-4,1,-5,-6,3,3,-8,4,-1,-2,-10,-7,-4,-5,-10,10,9,-3,6,5,3,-3,-4,-10,9,-8,-8,1,-6,2,-7,1,-4,10,-4,-9,2,-9,-10,1,-3,-10,6,3,-8,-9,7,-10,-4,3,7,4,-6,4,-6,-7,8,9,9,-7,9,1,-5,7,3,-7,3,-10,6,5,2,2,9,1,5,4,-5,-8,-8,-10,-6,-1,-8,-8,-6,-8,-4,6,2,-9,7,-9,-10,5,-3,-9,1,9,-1,-6,1,5,4,9,1,1,3,2,-8,-1,1,-1,10,-4,9,7,-7,5,6,-7,2,-8,-9,-8,7,-7,7,-3,-8,-7,-10,-6,1,-6,5,-5,-1,-2,3,-7,-7,-9,2,3,-2,8,-7,8,-8,-4,-10,-10,1,-3,-9,-5,5,-5,9,-9,-8,-2,3,-4,4,4,8,7,5,4,-8,-10,-4,-10,-3,-1,-7,-8,2,-1,-2,2,-10,-1,-7,-9,-3,-10,6,-7,10,-1,-2,-7,-3,-1,-5,6,2,-2,-2,5,-2,2,4,6,-1,1,6,-6,-6,5,-1,-9,-10,-1,-2,8,1,1,-1,-9,3,-6,8,9,10,-5,7,-6,-7,-9,-3,-4,-9,2,-9,2,3,-1,1,-2,6,-4,3,1,-6,8,9,6,6,-8,10,-9,10,-1,1,-4,1,9,-9,-4,1,8,6,8,1,9,9,-2,7,2,7,5,5,5,-6,-2,-5,-9,-4,4,-4,-7,-10,-2,4,-7,1,2,7,3,-6,-2,-3,3,5,-3,10,-2,10,-1,9,7,1,-7,7,-4,2,8,-5,3,8,-1,-5,-1,8,-9,-2,-6,-8,-5,-10,1,-5,7,10,1,5,6,-6,5,1,-10,4,9,-10,10,3,4,-2,9,-3,8,4,-8,-1,6,-10,-6,-6,-8,-7,-6,2,10,1,4,10,1,-5,6,-3,9,-1,-10,8,-3,6,7,7,2,7,-1,-9,10,-9,-2,-1,8,6,10,3,10,3,9,-7,8,-6,-10,9,-9,-8,-3,-1,-2,-6,-2,-8,-10,2,-10,8,-10,5,9,9,4,-6,8,-5,-6,-7,-2,1,-5,-1,9,-1,6,-10,-1,1,-8,-10,6,-9,8,3,10,-2,-6,-7,4,7,-5,-3,5,2,2,-10,-1,3,6,9,-9,-10,-6,1,7,8,-2,-10,6,2,6,-6,-2,6,6,-5,-10,9,2,-6,7,-2,-8,8,6,1,4,1,-10,-6,-6,-9,-4,2,10,6,5,-8,4,-6,8,6,-7,-7,-6,3,-2,8,-3,-3,-2,2,-10,-2,-8,7,-8,-9,-10,3,-9,-7,9,8,-6,6,-3,5,1,-2,-8,7,3,-2,-2,10,9,4,-3,-1,7,-6,8,-6,1,-9,6,-4,2,2,8,7,7,9,-6,-8,-10,3,-10,-8,-4,9,-3,-9,-8,10,2,5,-1,-1,7,-9,-6,6,3,6,-10,-9,7,-7,10,-10,5,4,-2,-4,-4,7,-7,-7,-8,8,-9,1,7,-10,-7,7,-8,9,-6,10,-8,-2,-1,-5,-4,-6,-2,-9,-7,3,-1,-6,-3,-10,10,9,-8,-2,1,-5,2,8,-10,-4,5,-1,-10,-5,3,-2,-9,8,-3,6,10,1,-5,-6,5,10,-7,-6,9,10,1,5,-2,-5,5,-10,-3,5,-9,2,2,4,4,-6,3,3,9,-4,-10,7,2,-10,-8,2,-7,1,-6,-9,-7,3,3,6,3,7,10,-1,-1,7,6,-7,6,2,-5,4,6,-1,-5,-4,-8,-4,-3,1,7,-7,1,-6,4,-3,-9,-8,-6,5,-10,10,8,-6,-10,-8,9,10,9,-7,3,1,-6,-8,-2,4,2,9,7,-4,4,-3,-7,-3,10,1,-1,-7,3,-9,-10,4,6,-3,-9,-9,-9,6,-7,4,8,-1,10,-5,-3,6,7,5,-5,6,5,9,-10,-2,3,-4,-3,-9,3,6,10,1,-3,-3,-5,6,-6,8,9,5,-7,-4,-6,-5,-9,-8,2,6,-6,-6,10,2,7,6,-1,-10,3,-1,9,9,7,-6,-5,-6,3,-3,-6,-3,-7,10,9,8,-8,-1,7,4,7,4,-4,4,-2,2,-2,-2,-3,8,-4,6,-5,8,6,3,4,7,8,7,8,10,4,10,-4,-9,-3,2,-1,10,-4,3,10,8,-9,10,4,-9,1,6,-8,-6,2,-10,10,-2,-3,-4,5,3,-7,-3,-4,-1,-10,2,4,10,6,8,-10,-10,-5,7,6,-4,-4,6,-7,-5,-4,6,5,-3,-6,6,-1,-10,-3,-4,9,-4,5,3,8,1,-2,-1,3,-9,7,8,4,-4,-4,-7,-8,-6,-2,-7,6,4,4,-9,1,9,-1,-6,2,-3,-2,-1,-3,5,7,-8,9,5,7,-2,9,-6,6,-7,-4,7,5,8,7,5,-7,-7,7,10,5,4,-3,6,4,10,-8,-6,6,-10,1,-7,10,-5,-7,3,-8,7,7,3,-9,-9,-9,-9,-1,8,-6,-10,-8,-5,3,8,-7,5,8,-7,-8,-5,3,5,-5,-8,7,-9,-7,1,-2,-1,4,5,3,-1,8,1,-10,-7,-9,-5,-7,5,-7,-3,-7,-10,-2,5,6,-8,9,-8,-6,-3,-4,-3,-3,2,-7,2,9,7,8,-7,-5,1,-4,5,7,-5,8,-1,-6,-2,-8,-9,8,-10,-7,3,4,9,4,-6,-4,2,-8,-5,-6,9,3,4,-5,8,-3,-3,-6,5,-6,2,3,-4,-7,-9,-7,-10,8,2,10,5,-2,2,-3,-9,-9,1,-5,5,3,6,4,-8,3,6,-1,-9,-1,2,-10,-3,10,-1,8,-6,9,8,-1,8,10,7,6,6,-9,-1,7,-5,7,-1,-3,-5,10,-8,2,5,9,-3,8,-2,8,-3,7,-2,-6,-1,-2,1,-2,5,4,-7,-1,-8,2,5,3,-4,8,9,1,-2,8,8,-4,-3,-2,9,-1,-10,9,2,3,-4,-2,-6,-3,-9,-4,1,8,4,4,-3,4,-7,-1,3,-5,-7,-2,-3,3,-5,6,5,-10,6,-6,-9,4,-1,7,9,3,-10,-8,9,4,10,-2,8,6,7,2,-2,6,-1,9,6,3,8,-8,5,-5,-3,-10,10,-4,-9,3,-5,7,1,-4,-2,2,2,-9,3,2,10,7,-9,6,-7,9,9,6,2,6,8,-3,9,7,-5,-8,-10,-4,-5,-7,9,-2,10,8,-9,7,4,8,-4,-5,-4,4,9,-5,6,7,-5,-6,9,10,-8,-7,-9,-4,-10,9,-6,-9,1,-1,5,-4,7,7,4,5,-4,-2,5,-5,-9,-10,9,9,-5,-9,-8,-1,3,-2,5,8,-8,-4,8,-10,6,-1,-1,-7,3,-5,8,-8,3,-9,5,-2,8,6,7,-5,7,-10,-8,-3,2,4,3,3,1,-6,9,-9,-4,-5,4,4,7,8,-8,10,8,-1,5,-6,-6,-5,2,2,-3,-5,-8,-6,2,2,-4,1,6,2,-4,10,-5,-4,10,-1,4,8,6,9,-10,9,1,6,1,-9,-10,-6,-5,-10,-8,-6,8,6,-9,-3,4,-3,-1,2,-8,-9,-1,3,-5,1,-5,-8,2,-8,-9,-2,-2,-9,7,-7,4,3,-8,3,9,-9,-10,7,10,-5,-8,-1,-5,5,2,6,5,3,-6,-1,8,-1,-6,2,-4,3,5,4,2,3,9,-2,-9,-10,-3,3,-10,2,3,-1,1,10,-8,8,-2,-6,10,-5,-4,5,-7,-9,-3,2,4,-2,5,-3,-4,3,-1,9,8,10,1,9,6,-5,-8,-4,10,7,7,10,-10,9,3,-3,-4,-3,10,4,-2,6,8,4,3,-5,3,4,-2,5,3,-8,-4,-1,-7,-2,-4,8,-6,9,-6,-2,4,2,-10,-3,6,-9,6,-5,-5,-9,5,8,-2,3,-5,-6,-4,5,5,9,1,2,-8,-8,3,-9,-7,-2,-5,-8,3,-1,10,10,-6,-9,-7,-4,-7,5,4,-10,2,-1,-10,-9,-2,-9,6,10,-10,-1,-9,9,9,-7,9,-5,3,10,-4,-4,9,9,-5,-9,7,2,-5,1,7,9,7,-9,-10,2,7,-10,-1,4,-7,1,-3,9,3,1,10,-8,-6,7,-5,9,7,10,8,6,-7,9,-1,7,10,6,10,7,2,-1,3,8,-1,9,-4,-7,3,10,-6,-10,5,-6,-3,-10,-7,1,-4,9,9,7,3,4,-1,2,3,4,9,2,3,6,-6,-7,5,-6,-3,10,8,-2,10,4,5,9,10,-5,-5,2,-7,2,6,-10,2,5,-2,6,-2,-5,-10,10,-8,-2,5,6,4,7,5,-9,5,-6,-2,1,5,-10,10,7,-4,-3,-3,-4,-7,7,6,1,-9,-8,-1,6,5,-3,5,-5,8,-9,-6,-8,-3,7,10,-9,-6,3,-10,-3,4,-9,3,9,1,4,10,-10,-8,2,-6,-8,-10,2,-9,-4,-1,1,9,7,9,-7,3,2,6,-9,5,-5,-8,6,1,10,6,-6,-3,-5,4,1,-1,9,9,10,-3,10,1,9,-7,-4,4,8,-4,-10,-8,6,-6,-7,-2,8,1,9,5,7,-8,-4,2,-10,6,-7,-2,4,-7,-4,7,4,-9,3,10,-5,1,-3,-5,9,6,6,8,-8,2,-6,2,-8,-3,-7,8,-5,3,-2,-2,10,7,-6,7,-4,5,-7,-9,10,-3,-9,10,10,2,4,2,-2,3,6,1,8,-9,5,-9,2,-3,-4,4,6,7,2,5,10,1,7,-7,9,1,4,10,-3,6,6,5,-6,4,-2,1,9,10,-7,1,3,-2,4,-2,7,-6,9,-8,2,4,-3,5,-10,-7,2,-3,-2,1,-8,-10,-4,-7,8,10,9,5,1,-3,-5,-6,-8,1,3,-5,4,6,-4,10,10,3,4,-9,-7,5,-5,-8,-1,3,10,5,-3,-1,5,10,-3,-3,8,3,-6,-5,1,-4,-2,-8,-6,6,3,-8,-3,4,-9,3,8,-1,4,7,-1,10,9,8,1,5,-3,4,9,-2,-4,-6,-2,-1,6,4,9,3,-1,1,6,8,9,5,-10,8,3,8,-2,-2,5,6,-9,1,-1,-2,2,-6,9,-1,-10,5,-3,-7,-10,-3,-4,-10,-9,2,7,5,-3,-10,-2,-3,10,-6,-9,-9,-3,-7,-1,-1,-9,-10,-7,4,8,4,5,-4,5,9,4,-4,-10,3,7,-4,9,3,-1,-7,2,-10,-9,1,4,-8,10,5,-5,3,-4,-8,-1,8,9,10,7,8,4,-9,-1,-7,1,1,2,-7,3,9,8,7,-3,9,-6,-5,6,1,1,10,-1,9,7,2,-3,3,8,-1,6,8,-6,-2,-7,2,2,1,3,9,-5,-9,1,2,-9,-10,-2,6,-1,4,3,5,10,-9,5,-2,-10,-1,-2,-2,-5,-5,-3,8,-9,-4,-8,8,-5,2,6,2,-4,10,-5,6,-7,10,-2,-3,-1,-1,-6,-9,-7,-4,-5,-2,-9,-5,-5,8,-4,3,5,4,5,-4,-6,3,-4,-8,-3,-5,3,1,-5,-1,7,2,9,7,3,4,-6,3,-6,-8,1,3,5,3,3,8,7,-2,-6,-10,-4,-10,-3,-2,-6,-8,-4,-3,7,1,-10,-9,-9,-3,2,5,10,-6,-8,4,9,-1,4,-3,9,-10,3,6,-10,6,-4,8,4,-9,-2,-6,-6,5,-2,3,-2,-10,2,-4,5,-4,1,-3,6,7,6,3,2,-5,6,-8,1,-1,4,-5,7,7,3,-3,3,-9,3,2,9,2,5,2,-7,-9,10,9,-5,-5,8,9,8,-2,-9,-8,4,-4,9,-3,10,-7,-7,-8,-5,-3,1,-6,-10,-9,5,-9,-9,-5,8,-3,1,-9,-8,-1,1,8,5,-10,4,-6,-9,5,-6,4,-8,2,-9,-8,-9,-2,4,-4,-5,6,6,-6,6,2,-2,6,7,1,-9,5,-1,-2,-8,-6,3,-2,-5,-3,-2,1,-3,-5,-6,-6,-7,-7,-7,-5,-3,10,4,-4,-2,8,-4,-7,-7,-9,1,10,-6,8,3,-10,4,-4,-2,7,-7,-8,-3,10,-1,5,-4,-2,1,6,5,2,-8,2,-5,5,-2,-3,-2,-9,1,7,-8,-6,10,2,-9,-9,-1,6,9,-7,6,8,-2,1,10,7,-8,6,4,-5,4,-10,6,10,9,6,7,5,8,3,5,-5,-2,1,1,-10,4,10,6,-5,7,-2,3,4,-5,-1,-6,3,1,5,-2,9,-5,-3,-8,7,10,-10,7,8,10,2,8,-3,1,-3,2,-8,10,9,-2,5,-4,-4,-10,4,-4,3,4,-2,-3,8,6,6,7,-4,-10,8,-6,8,7,-6,-8,4,5,7,-1,-7,8,1,-7,-4,-5,-4,9,9,-3,8,3,3,7,8,-4,-7,8,-10,4,-5,-8,-2,-2,4,5,7,3,-6,2,10,-2,-10,4,7,-4,9,-5,1,-3,3,5,5,-1,-10,-8,-1,-7,1,9,-1,4,6,-4,-7,2,-4,1,4,-2,-7,5,3,6,-5,-3,1,8,-7,6,9,3,4,-5,-5,5,9,9,3,-5,-4,7,-6,-5,-9,-6,-9,-4,-10,-3,7,-9,9,-10,7,3,6,7,6,4,4,-6,8,8,-10,-6,-9,7,5,10,-5,-3,2,-4,3,6,9,-10,3,-6,1,1,-7,7,8,-5,-10,-5,-8,1,-6,-1,-10,-1,-1,7,8,-1,8,10,7,8,-2,10,-1,-5,9,-1,7,1,8,-9,5,5,9,-9,1,-4,2,4,4,-8,5,1,1,1,9,10,-1,-9,-2,-7,-8,5,4,3,1,10,-3,10,-4,-5,-3,8,2,6,-6,7,5,-3,-5,8,8,-4,10,4,6,-6,-8,5,-4,6,-8,-5,8,4,4,9,-10,2,-8,-4,10,5,6,8,5,-9,8,7,-2,9,-1,-8,3,10,10,8,-6,8,7,4,-1,-4,-9,-6,2,-6,6,-5,-8,4,1,-8,7,10,1,5,-7,2,9,-6,5,-5,10,2,7,7], dtype = "uint8")#candidate|2059|(3120,)|const|uint8
call_2057 = relay.TupleGetItem(func_813_call(relay.reshape(var_2058.astype('uint8'), []), relay.reshape(const_2059.astype('uint8'), [15, 16, 13]), ), 1)
call_2060 = relay.TupleGetItem(func_816_call(relay.reshape(var_2058.astype('uint8'), []), relay.reshape(const_2059.astype('uint8'), [15, 16, 13]), ), 1)
bop_2062 = relay.subtract(var_2053.astype('uint8'), relay.reshape(bop_2054.astype('uint8'), relay.shape_of(var_2053))) # shape=(14, 12, 10)
output = relay.Tuple([call_2057,var_2058,const_2059,bop_2062,])
output2 = relay.Tuple([call_2060,var_2058,const_2059,bop_2062,])
func_2112 = relay.Function([var_2052,var_2053,var_2058,], output)
mod['func_2112'] = func_2112
mod = relay.transform.InferType()(mod)
var_2113 = relay.var("var_2113", dtype = "uint8", shape = (14, 12, 10))#candidate|2113|(14, 12, 10)|var|uint8
var_2114 = relay.var("var_2114", dtype = "uint8", shape = (14, 12, 10))#candidate|2114|(14, 12, 10)|var|uint8
var_2115 = relay.var("var_2115", dtype = "uint8", shape = ())#candidate|2115|()|var|uint8
output = func_2112(var_2113,var_2114,var_2115,)
func_2116 = relay.Function([var_2113,var_2114,var_2115,], output)
mutated_mod['func_2116'] = func_2116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_2127 = relay.TupleGetItem(func_316_call(), 0)
call_2128 = relay.TupleGetItem(func_317_call(), 0)
output = relay.Tuple([call_2127,])
output2 = relay.Tuple([call_2128,])
func_2135 = relay.Function([], output)
mod['func_2135'] = func_2135
mod = relay.transform.InferType()(mod)
mutated_mod['func_2135'] = func_2135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2135_call = mutated_mod.get_global_var('func_2135')
call_2136 = func_2135_call()
output = call_2136
func_2137 = relay.Function([], output)
mutated_mod['func_2137'] = func_2137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_2164 = relay.TupleGetItem(func_1016_call(), 5)
call_2165 = relay.TupleGetItem(func_1018_call(), 5)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_2170 = func_1396_call()
call_2171 = func_1396_call()
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_2178 = relay.TupleGetItem(func_49_call(), 0)
call_2179 = relay.TupleGetItem(func_50_call(), 0)
output = relay.Tuple([call_2164,call_2170,call_2178,])
output2 = relay.Tuple([call_2165,call_2171,call_2179,])
func_2201 = relay.Function([], output)
mod['func_2201'] = func_2201
mod = relay.transform.InferType()(mod)
mutated_mod['func_2201'] = func_2201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mutated_mod.get_global_var('func_2201')
call_2202 = func_2201_call()
output = call_2202
func_2203 = relay.Function([], output)
mutated_mod['func_2203'] = func_2203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1501_call = mod.get_global_var('func_1501')
func_1502_call = mutated_mod.get_global_var('func_1502')
call_2257 = relay.TupleGetItem(func_1501_call(), 2)
call_2258 = relay.TupleGetItem(func_1502_call(), 2)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_2272 = relay.TupleGetItem(func_2016_call(), 1)
call_2273 = relay.TupleGetItem(func_2017_call(), 1)
uop_2287 = relay.sigmoid(call_2257.astype('float64')) # shape=(378,)
uop_2289 = relay.sigmoid(call_2258.astype('float64')) # shape=(378,)
output = relay.Tuple([call_2272,uop_2287,])
output2 = relay.Tuple([call_2273,uop_2289,])
func_2290 = relay.Function([], output)
mod['func_2290'] = func_2290
mod = relay.transform.InferType()(mod)
mutated_mod['func_2290'] = func_2290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2290_call = mutated_mod.get_global_var('func_2290')
call_2291 = func_2290_call()
output = call_2291
func_2292 = relay.Function([], output)
mutated_mod['func_2292'] = func_2292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_2314 = func_1396_call()
call_2315 = func_1396_call()
output = call_2314
output2 = call_2315
func_2340 = relay.Function([], output)
mod['func_2340'] = func_2340
mod = relay.transform.InferType()(mod)
output = func_2340()
func_2341 = relay.Function([], output)
mutated_mod['func_2341'] = func_2341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1622_call = mod.get_global_var('func_1622')
func_1623_call = mutated_mod.get_global_var('func_1623')
call_2344 = func_1622_call()
call_2345 = func_1622_call()
var_2346 = relay.var("var_2346", dtype = "uint8", shape = (8, 13, 16))#candidate|2346|(8, 13, 16)|var|uint8
bop_2347 = relay.divide(call_2344.astype('float64'), relay.reshape(var_2346.astype('float64'), relay.shape_of(call_2344))) # shape=(8, 13, 16)
bop_2350 = relay.divide(call_2345.astype('float64'), relay.reshape(var_2346.astype('float64'), relay.shape_of(call_2345))) # shape=(8, 13, 16)
func_1501_call = mod.get_global_var('func_1501')
func_1502_call = mutated_mod.get_global_var('func_1502')
call_2371 = relay.TupleGetItem(func_1501_call(), 2)
call_2372 = relay.TupleGetItem(func_1502_call(), 2)
output = relay.Tuple([bop_2347,call_2371,])
output2 = relay.Tuple([bop_2350,call_2372,])
func_2377 = relay.Function([var_2346,], output)
mod['func_2377'] = func_2377
mod = relay.transform.InferType()(mod)
var_2378 = relay.var("var_2378", dtype = "uint8", shape = (8, 13, 16))#candidate|2378|(8, 13, 16)|var|uint8
output = func_2377(var_2378)
func_2379 = relay.Function([var_2378], output)
mutated_mod['func_2379'] = func_2379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_2384 = func_108_call()
call_2385 = func_108_call()
output = call_2384
output2 = call_2385
func_2387 = relay.Function([], output)
mod['func_2387'] = func_2387
mod = relay.transform.InferType()(mod)
mutated_mod['func_2387'] = func_2387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2387_call = mutated_mod.get_global_var('func_2387')
call_2388 = func_2387_call()
output = call_2388
func_2389 = relay.Function([], output)
mutated_mod['func_2389'] = func_2389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2387_call = mod.get_global_var('func_2387')
func_2389_call = mutated_mod.get_global_var('func_2389')
call_2393 = func_2387_call()
call_2394 = func_2387_call()
uop_2401 = relay.sin(call_2393.astype('float32')) # shape=(8, 13, 16)
uop_2403 = relay.sin(call_2394.astype('float32')) # shape=(8, 13, 16)
output = uop_2401
output2 = uop_2403
func_2439 = relay.Function([], output)
mod['func_2439'] = func_2439
mod = relay.transform.InferType()(mod)
mutated_mod['func_2439'] = func_2439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2439_call = mutated_mod.get_global_var('func_2439')
call_2440 = func_2439_call()
output = call_2440
func_2441 = relay.Function([], output)
mutated_mod['func_2441'] = func_2441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_2456 = relay.TupleGetItem(func_316_call(), 0)
call_2457 = relay.TupleGetItem(func_317_call(), 0)
output = call_2456
output2 = call_2457
func_2473 = relay.Function([], output)
mod['func_2473'] = func_2473
mod = relay.transform.InferType()(mod)
mutated_mod['func_2473'] = func_2473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2473_call = mutated_mod.get_global_var('func_2473')
call_2474 = func_2473_call()
output = call_2474
func_2475 = relay.Function([], output)
mutated_mod['func_2475'] = func_2475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_2481 = relay.TupleGetItem(func_1769_call(), 2)
call_2482 = relay.TupleGetItem(func_1771_call(), 2)
uop_2483 = relay.log2(call_2481.astype('float64')) # shape=(8, 13, 16)
uop_2485 = relay.log2(call_2482.astype('float64')) # shape=(8, 13, 16)
func_1909_call = mod.get_global_var('func_1909')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_2500 = relay.TupleGetItem(func_1909_call(), 1)
call_2501 = relay.TupleGetItem(func_1910_call(), 1)
bop_2519 = relay.logical_and(call_2500.astype('bool'), relay.reshape(uop_2483.astype('bool'), relay.shape_of(call_2500))) # shape=(8, 13, 16)
bop_2522 = relay.logical_and(call_2501.astype('bool'), relay.reshape(uop_2485.astype('bool'), relay.shape_of(call_2501))) # shape=(8, 13, 16)
output = relay.Tuple([bop_2519,])
output2 = relay.Tuple([bop_2522,])
func_2523 = relay.Function([], output)
mod['func_2523'] = func_2523
mod = relay.transform.InferType()(mod)
mutated_mod['func_2523'] = func_2523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2523_call = mutated_mod.get_global_var('func_2523')
call_2524 = func_2523_call()
output = call_2524
func_2525 = relay.Function([], output)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2529 = relay.var("var_2529", dtype = "int32", shape = (1, 13))#candidate|2529|(1, 13)|var|int32
var_2530 = relay.var("var_2530", dtype = "int32", shape = (1, 13))#candidate|2530|(1, 13)|var|int32
bop_2531 = relay.right_shift(var_2529.astype('int32'), relay.reshape(var_2530.astype('int32'), relay.shape_of(var_2529))) # shape=(1, 13)
output = bop_2531
output2 = bop_2531
func_2534 = relay.Function([var_2529,var_2530,], output)
mod['func_2534'] = func_2534
mod = relay.transform.InferType()(mod)
var_2535 = relay.var("var_2535", dtype = "int32", shape = (1, 13))#candidate|2535|(1, 13)|var|int32
var_2536 = relay.var("var_2536", dtype = "int32", shape = (1, 13))#candidate|2536|(1, 13)|var|int32
output = func_2534(var_2535,var_2536,)
func_2537 = relay.Function([var_2535,var_2536,], output)
mutated_mod['func_2537'] = func_2537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mod.get_global_var('func_1107')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_2572 = relay.TupleGetItem(func_1107_call(), 0)
call_2573 = relay.TupleGetItem(func_1109_call(), 0)
output = call_2572
output2 = call_2573
func_2574 = relay.Function([], output)
mod['func_2574'] = func_2574
mod = relay.transform.InferType()(mod)
output = func_2574()
func_2575 = relay.Function([], output)
mutated_mod['func_2575'] = func_2575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_2607 = relay.TupleGetItem(func_449_call(), 1)
call_2608 = relay.TupleGetItem(func_451_call(), 1)
output = relay.Tuple([call_2607,])
output2 = relay.Tuple([call_2608,])
func_2609 = relay.Function([], output)
mod['func_2609'] = func_2609
mod = relay.transform.InferType()(mod)
output = func_2609()
func_2610 = relay.Function([], output)
mutated_mod['func_2610'] = func_2610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2473_call = mod.get_global_var('func_2473')
func_2475_call = mutated_mod.get_global_var('func_2475')
call_2668 = func_2473_call()
call_2669 = func_2473_call()
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_2690 = relay.TupleGetItem(func_1067_call(), 2)
call_2691 = relay.TupleGetItem(func_1069_call(), 2)
output = relay.Tuple([call_2668,call_2690,])
output2 = relay.Tuple([call_2669,call_2691,])
func_2697 = relay.Function([], output)
mod['func_2697'] = func_2697
mod = relay.transform.InferType()(mod)
mutated_mod['func_2697'] = func_2697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2697_call = mutated_mod.get_global_var('func_2697')
call_2698 = func_2697_call()
output = call_2698
func_2699 = relay.Function([], output)
mutated_mod['func_2699'] = func_2699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2290_call = mod.get_global_var('func_2290')
func_2292_call = mutated_mod.get_global_var('func_2292')
call_2715 = relay.TupleGetItem(func_2290_call(), 0)
call_2716 = relay.TupleGetItem(func_2292_call(), 0)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
call_2733 = relay.TupleGetItem(func_720_call(), 0)
call_2734 = relay.TupleGetItem(func_722_call(), 0)
uop_2741 = relay.cosh(call_2715.astype('float64')) # shape=(8, 13, 16)
uop_2743 = relay.cosh(call_2716.astype('float64')) # shape=(8, 13, 16)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_2744 = relay.TupleGetItem(func_49_call(), 0)
call_2745 = relay.TupleGetItem(func_50_call(), 0)
output = relay.Tuple([call_2733,uop_2741,call_2744,])
output2 = relay.Tuple([call_2734,uop_2743,call_2745,])
func_2751 = relay.Function([], output)
mod['func_2751'] = func_2751
mod = relay.transform.InferType()(mod)
mutated_mod['func_2751'] = func_2751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mutated_mod.get_global_var('func_2751')
call_2752 = func_2751_call()
output = call_2752
func_2753 = relay.Function([], output)
mutated_mod['func_2753'] = func_2753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_2782 = func_108_call()
call_2783 = func_108_call()
output = relay.Tuple([call_2782,])
output2 = relay.Tuple([call_2783,])
func_2785 = relay.Function([], output)
mod['func_2785'] = func_2785
mod = relay.transform.InferType()(mod)
mutated_mod['func_2785'] = func_2785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2785_call = mutated_mod.get_global_var('func_2785')
call_2786 = func_2785_call()
output = call_2786
func_2787 = relay.Function([], output)
mutated_mod['func_2787'] = func_2787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1181_call = mod.get_global_var('func_1181')
func_1183_call = mutated_mod.get_global_var('func_1183')
call_2883 = func_1181_call()
call_2884 = func_1181_call()
func_2574_call = mod.get_global_var('func_2574')
func_2575_call = mutated_mod.get_global_var('func_2575')
call_2900 = func_2574_call()
call_2901 = func_2574_call()
output = relay.Tuple([call_2883,call_2900,])
output2 = relay.Tuple([call_2884,call_2901,])
func_2902 = relay.Function([], output)
mod['func_2902'] = func_2902
mod = relay.transform.InferType()(mod)
mutated_mod['func_2902'] = func_2902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mutated_mod.get_global_var('func_2902')
call_2903 = func_2902_call()
output = call_2903
func_2904 = relay.Function([], output)
mutated_mod['func_2904'] = func_2904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
call_2910 = relay.TupleGetItem(func_720_call(), 0)
call_2911 = relay.TupleGetItem(func_722_call(), 0)
output = call_2910
output2 = call_2911
func_2912 = relay.Function([], output)
mod['func_2912'] = func_2912
mod = relay.transform.InferType()(mod)
output = func_2912()
func_2913 = relay.Function([], output)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1682_call = mod.get_global_var('func_1682')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_2917 = relay.TupleGetItem(func_1682_call(), 0)
call_2918 = relay.TupleGetItem(func_1684_call(), 0)
func_1682_call = mod.get_global_var('func_1682')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_2922 = relay.TupleGetItem(func_1682_call(), 0)
call_2923 = relay.TupleGetItem(func_1684_call(), 0)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
const_2937 = relay.const(8, dtype = "uint8")#candidate|2937|()|const|uint8
var_2938 = relay.var("var_2938", dtype = "uint8", shape = (3120,))#candidate|2938|(3120,)|var|uint8
call_2936 = relay.TupleGetItem(func_813_call(relay.reshape(const_2937.astype('uint8'), []), relay.reshape(var_2938.astype('uint8'), [15, 16, 13]), ), 1)
call_2939 = relay.TupleGetItem(func_816_call(relay.reshape(const_2937.astype('uint8'), []), relay.reshape(var_2938.astype('uint8'), [15, 16, 13]), ), 1)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_2951 = func_108_call()
call_2952 = func_108_call()
output = relay.Tuple([call_2917,call_2922,call_2936,const_2937,var_2938,call_2951,])
output2 = relay.Tuple([call_2918,call_2923,call_2939,const_2937,var_2938,call_2952,])
func_2955 = relay.Function([var_2938,], output)
mod['func_2955'] = func_2955
mod = relay.transform.InferType()(mod)
var_2956 = relay.var("var_2956", dtype = "uint8", shape = (3120,))#candidate|2956|(3120,)|var|uint8
output = func_2955(var_2956)
func_2957 = relay.Function([var_2956], output)
mutated_mod['func_2957'] = func_2957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_3048 = relay.TupleGetItem(func_635_call(), 1)
call_3049 = relay.TupleGetItem(func_636_call(), 1)
output = call_3048
output2 = call_3049
func_3058 = relay.Function([], output)
mod['func_3058'] = func_3058
mod = relay.transform.InferType()(mod)
mutated_mod['func_3058'] = func_3058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3058_call = mutated_mod.get_global_var('func_3058')
call_3059 = func_3058_call()
output = call_3059
func_3060 = relay.Function([], output)
mutated_mod['func_3060'] = func_3060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2135_call = mod.get_global_var('func_2135')
func_2137_call = mutated_mod.get_global_var('func_2137')
call_3094 = relay.TupleGetItem(func_2135_call(), 0)
call_3095 = relay.TupleGetItem(func_2137_call(), 0)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_3096 = relay.TupleGetItem(func_1016_call(), 5)
call_3097 = relay.TupleGetItem(func_1018_call(), 5)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_3107 = relay.TupleGetItem(func_635_call(), 1)
call_3108 = relay.TupleGetItem(func_636_call(), 1)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_3119 = relay.TupleGetItem(func_1016_call(), 2)
call_3120 = relay.TupleGetItem(func_1018_call(), 2)
output = relay.Tuple([call_3094,call_3096,call_3107,call_3119,])
output2 = relay.Tuple([call_3095,call_3097,call_3108,call_3120,])
func_3136 = relay.Function([], output)
mod['func_3136'] = func_3136
mod = relay.transform.InferType()(mod)
mutated_mod['func_3136'] = func_3136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mutated_mod.get_global_var('func_3136')
call_3137 = func_3136_call()
output = call_3137
func_3138 = relay.Function([], output)
mutated_mod['func_3138'] = func_3138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1501_call = mod.get_global_var('func_1501')
func_1502_call = mutated_mod.get_global_var('func_1502')
call_3151 = relay.TupleGetItem(func_1501_call(), 1)
call_3152 = relay.TupleGetItem(func_1502_call(), 1)
var_3153 = relay.var("var_3153", dtype = "uint8", shape = (8, 13, 16))#candidate|3153|(8, 13, 16)|var|uint8
bop_3154 = relay.greater_equal(call_3151.astype('bool'), relay.reshape(var_3153.astype('bool'), relay.shape_of(call_3151))) # shape=(8, 13, 16)
bop_3157 = relay.greater_equal(call_3152.astype('bool'), relay.reshape(var_3153.astype('bool'), relay.shape_of(call_3152))) # shape=(8, 13, 16)
func_248_call = mod.get_global_var('func_248')
func_251_call = mutated_mod.get_global_var('func_251')
var_3163 = relay.var("var_3163", dtype = "uint64", shape = (378,))#candidate|3163|(378,)|var|uint64
call_3162 = func_248_call(relay.reshape(var_3163.astype('uint64'), [9, 14, 3]), relay.reshape(var_3163.astype('uint64'), [9, 14, 3]), )
call_3164 = func_248_call(relay.reshape(var_3163.astype('uint64'), [9, 14, 3]), relay.reshape(var_3163.astype('uint64'), [9, 14, 3]), )
output = relay.Tuple([bop_3154,call_3162,var_3163,])
output2 = relay.Tuple([bop_3157,call_3164,var_3163,])
func_3169 = relay.Function([var_3153,var_3163,], output)
mod['func_3169'] = func_3169
mod = relay.transform.InferType()(mod)
mutated_mod['func_3169'] = func_3169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3169_call = mutated_mod.get_global_var('func_3169')
var_3171 = relay.var("var_3171", dtype = "uint8", shape = (8, 13, 16))#candidate|3171|(8, 13, 16)|var|uint8
var_3172 = relay.var("var_3172", dtype = "uint64", shape = (378,))#candidate|3172|(378,)|var|uint64
call_3170 = func_3169_call(var_3171,var_3172,)
output = call_3170
func_3173 = relay.Function([var_3171,var_3172,], output)
mutated_mod['func_3173'] = func_3173
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3180 = relay.var("var_3180", dtype = "float64", shape = (3, 4, 2))#candidate|3180|(3, 4, 2)|var|float64
var_3181 = relay.var("var_3181", dtype = "float64", shape = (3, 4, 2))#candidate|3181|(3, 4, 2)|var|float64
bop_3182 = relay.floor_divide(var_3180.astype('float64'), relay.reshape(var_3181.astype('float64'), relay.shape_of(var_3180))) # shape=(3, 4, 2)
bop_3187 = relay.right_shift(var_3181.astype('int64'), relay.reshape(var_3180.astype('int64'), relay.shape_of(var_3181))) # shape=(3, 4, 2)
func_2340_call = mod.get_global_var('func_2340')
func_2341_call = mutated_mod.get_global_var('func_2341')
call_3195 = func_2340_call()
call_3196 = func_2340_call()
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3202 = relay.TupleGetItem(func_2523_call(), 0)
call_3203 = relay.TupleGetItem(func_2525_call(), 0)
output = relay.Tuple([bop_3182,bop_3187,call_3195,call_3202,])
output2 = relay.Tuple([bop_3182,bop_3187,call_3196,call_3203,])
func_3207 = relay.Function([var_3180,var_3181,], output)
mod['func_3207'] = func_3207
mod = relay.transform.InferType()(mod)
mutated_mod['func_3207'] = func_3207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3207_call = mutated_mod.get_global_var('func_3207')
var_3209 = relay.var("var_3209", dtype = "float64", shape = (3, 4, 2))#candidate|3209|(3, 4, 2)|var|float64
var_3210 = relay.var("var_3210", dtype = "float64", shape = (3, 4, 2))#candidate|3210|(3, 4, 2)|var|float64
call_3208 = func_3207_call(var_3209,var_3210,)
output = call_3208
func_3211 = relay.Function([var_3209,var_3210,], output)
mutated_mod['func_3211'] = func_3211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2574_call = mod.get_global_var('func_2574')
func_2575_call = mutated_mod.get_global_var('func_2575')
call_3226 = func_2574_call()
call_3227 = func_2574_call()
output = relay.Tuple([call_3226,])
output2 = relay.Tuple([call_3227,])
func_3234 = relay.Function([], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
output = func_3234()
func_3235 = relay.Function([], output)
mutated_mod['func_3235'] = func_3235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1622_call = mod.get_global_var('func_1622')
func_1623_call = mutated_mod.get_global_var('func_1623')
call_3251 = func_1622_call()
call_3252 = func_1622_call()
output = relay.Tuple([call_3251,])
output2 = relay.Tuple([call_3252,])
func_3267 = relay.Function([], output)
mod['func_3267'] = func_3267
mod = relay.transform.InferType()(mod)
output = func_3267()
func_3268 = relay.Function([], output)
mutated_mod['func_3268'] = func_3268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_3284 = relay.TupleGetItem(func_3234_call(), 0)
call_3285 = relay.TupleGetItem(func_3235_call(), 0)
func_2112_call = mod.get_global_var('func_2112')
func_2116_call = mutated_mod.get_global_var('func_2116')
const_3327 = relay.const([[-8,-7,-3,-7,4,10,-6,-3,-6,7,-9,-8,6,7,-5,-8,2,-4,-10,2,3,-4,-4,9,3,7,-10,-4,1,4,2,7,-7,9,-3,3,-4,6,-5,-8,-3,-2,-10,-9,-10,4,-5,8,-3,-1,-9,-4,-3,-10,5,9,-1,-3,7,-1,-5,9,-10,-3,-7,1,9,8,4,-10,-8,-1,10,-1,5,2,-8,1,-1,1,1,3,-7,-1,10,4,-2,8,-6,-9,-2,-1,5,8,-8,-1,3,8,4,3,-5,-4,9,-9,1,-7,10,-3,2,10,-4,-1,-6,7,10,-7,-6,-10,-3,1,10,8,8,4,5,-1,6,6,-1,-3,4,4,1,4,-6,7,-4,5,-6,-3],[-4,10,6,-3,10,10,7,3,-9,-1,3,-10,-3,-9,3,-2,6,-8,-1,-1,-8,-4,-4,-3,1,9,-2,-10,-5,5,-3,-4,10,-5,-2,1,-7,5,9,8,9,-5,8,7,-8,-1,1,2,-9,4,3,-3,10,6,5,-1,-1,7,-4,3,7,3,-9,-1,3,-2,-9,-9,-3,8,6,4,6,9,8,-1,5,-4,10,5,-9,10,-1,8,-3,-4,8,8,-1,-3,8,5,8,10,-3,1,-1,1,-1,8,7,-1,-1,-8,-6,1,-7,-9,-6,-4,5,2,-8,10,3,-1,1,5,3,-4,6,-6,2,7,4,6,7,-5,-10,-4,4,-3,-1,5,-4,4,-4,3,6,5],[-1,9,-8,7,-1,3,8,10,-6,3,4,2,-10,6,-4,7,-2,7,3,10,-5,-1,10,-2,6,8,7,-8,2,-4,-4,6,-7,6,7,6,-10,6,-8,-6,-6,-4,2,-9,-7,3,-3,-9,-1,2,2,1,7,-10,6,9,10,-2,-7,-7,3,6,-10,-6,-10,3,8,-2,9,-10,-9,6,4,10,-8,-6,8,7,-8,10,-1,10,7,4,5,3,-7,-3,-5,-2,1,-6,-9,8,-5,-5,-3,6,8,-6,-8,-7,5,3,3,7,-3,-3,-7,10,-1,-10,10,4,8,9,8,10,-7,7,10,6,-8,-6,3,-9,-10,9,-5,-6,-3,-8,4,-6,2,-5,-7,6,3,2],[-9,-8,-8,-9,-10,-5,-1,-3,2,7,3,6,4,-7,5,1,-8,1,8,8,-4,-8,-5,-1,10,-1,-2,3,1,1,7,8,-2,1,8,7,-10,8,-8,4,-8,1,4,-6,-5,-10,10,8,-6,4,-8,-9,-8,8,7,5,9,-7,-1,-9,-1,-9,-7,-5,-7,1,1,-6,7,6,7,1,-7,-10,-3,-5,10,-5,2,-1,2,6,10,-4,-5,-2,2,-8,-2,-9,9,-9,-7,-5,-8,-10,8,4,8,-6,-8,7,4,1,6,-10,6,-4,-8,4,5,6,7,-3,8,8,-10,8,-10,9,-10,1,-10,9,-1,-4,6,-10,-10,10,2,5,-2,-5,3,10,-3,-9,5,-9],[-4,5,-2,5,-9,1,-4,3,-9,-10,-2,-8,-1,-6,-9,-3,9,-5,4,-5,4,4,2,3,8,8,6,-5,-4,-3,7,8,-5,-10,-2,2,1,-5,3,-4,3,-1,7,6,-6,-8,9,2,8,3,-5,5,10,8,-8,-4,-6,2,10,9,-8,-10,1,-3,2,-9,2,4,4,3,6,-4,2,-8,-3,6,-1,10,-8,3,10,8,5,-2,-4,10,-2,-4,10,5,-8,7,-1,3,2,9,5,-4,9,-9,10,-5,-6,7,9,-1,6,6,7,-7,3,-10,3,-1,9,7,1,-2,-9,3,4,6,-2,-7,2,-7,-8,-5,1,5,-6,-9,-4,-4,-1,-10,-10,5,9,-10],[-4,7,-6,-4,8,6,4,3,-8,1,-3,-4,-9,5,-9,-10,4,6,10,4,3,-6,-7,5,3,5,-10,8,-10,-9,10,3,-9,-1,-10,10,8,2,-2,-1,4,-2,-8,6,-7,-6,-8,-8,-9,5,5,5,-1,9,4,10,-9,-4,7,5,-9,-9,-2,-2,-8,-2,-4,6,-4,9,-4,-9,3,10,-5,4,-7,-9,-1,-2,9,2,3,-9,1,-8,-8,10,8,3,-6,-7,1,-2,6,1,-9,1,1,10,1,-8,3,-2,7,-6,6,6,9,10,-1,3,6,-2,7,10,8,-6,-6,-1,8,8,9,1,-1,5,6,1,-5,8,3,-9,5,-9,6,6,5,9,-5,4],[-3,-7,9,8,1,6,-5,-2,-10,1,-10,1,-8,-9,-1,10,-2,-1,-5,4,7,9,-5,-10,1,-1,8,-6,2,-1,10,7,8,-4,-6,-10,-8,-5,-9,8,-6,-1,-2,-1,2,-7,3,6,-1,6,-9,-8,-7,-10,10,6,-6,2,-4,4,7,8,-5,-1,5,4,8,-10,7,-9,7,-2,-2,3,-7,2,8,4,-6,-2,6,4,-7,7,4,10,-3,8,-5,1,-10,6,5,-5,-4,-2,2,4,-10,-3,9,10,4,-7,-1,-2,1,2,7,5,-2,-2,4,-4,-7,1,-10,5,-10,-6,-1,3,6,6,-1,-5,-9,-9,-2,-7,2,4,10,-10,4,-1,-4,-6,10,-4],[-4,-7,-7,-6,-1,-10,1,-7,-7,-1,-4,-5,7,-9,-5,1,5,2,6,2,1,10,-8,-4,7,8,-8,-10,-6,5,5,1,-3,9,-1,7,-5,-5,-6,-9,-4,4,2,8,-4,-9,8,6,-5,1,8,-9,6,7,2,-5,-5,-10,-5,-4,1,6,5,1,9,-5,1,-9,7,9,3,6,4,-6,-4,6,6,-5,5,9,1,10,-8,-8,-8,4,10,-1,8,3,-10,7,4,4,-1,5,9,-3,6,-3,6,-8,-7,-3,8,7,9,-1,10,-2,10,-1,3,-7,-5,5,-6,-10,-6,10,-2,-2,-4,2,10,-5,3,9,-1,-7,7,-8,9,-9,-4,8,9,5,-5,-7],[4,5,-9,-3,3,5,-6,-4,-2,9,-4,-1,7,6,4,-4,7,-6,-6,-7,1,-10,6,1,8,5,6,-5,-2,4,-6,4,10,2,-1,6,2,10,-9,-7,2,9,5,-3,-6,-3,-7,-8,9,2,8,3,-3,7,7,-1,3,8,-3,-7,10,-3,-6,-4,10,4,-6,-7,1,3,7,8,-3,10,-9,-8,6,6,2,-7,-9,-10,10,-6,-9,-3,-4,-8,5,-6,4,3,-3,2,-10,8,1,-4,3,-4,-10,1,-7,-4,9,-7,2,-3,-1,-2,3,10,-8,-5,-4,-7,7,2,-9,6,-4,10,-5,3,-7,8,-7,-4,-3,-9,-9,3,4,-9,2,10,-10,-4,-3,-4],[-3,10,9,6,2,-8,2,8,9,-1,-5,-6,1,-2,8,5,-6,-1,9,-8,-5,-6,2,-2,-3,1,-6,-5,-9,-3,2,-8,5,7,1,8,4,2,10,-6,-9,-3,5,5,-4,1,-8,-6,10,-10,-9,-6,4,8,4,-9,2,-9,9,-1,2,-10,-4,-5,10,-5,6,3,-9,-4,-6,5,4,-4,-8,7,-10,-10,3,-9,3,-3,7,-6,6,1,-2,9,2,10,-8,-10,4,-3,5,4,-5,-6,-3,-9,4,-3,6,-4,-5,8,1,-4,-8,-4,6,-3,-6,-3,1,10,-2,4,6,8,-2,7,-2,10,7,-3,3,5,-4,8,2,3,-10,-4,4,-10,-6,-10,9,8],[-4,-10,-8,-6,-5,10,-2,-9,-1,-1,-5,-1,-7,9,3,-1,-10,-5,5,-3,-6,6,-7,10,-10,-2,1,5,-6,-1,4,7,-10,4,-6,8,9,9,10,1,2,8,9,-9,-10,6,-2,-9,7,-2,2,4,3,-5,-5,-7,-2,-2,8,7,-4,3,-6,-2,8,6,1,1,-3,9,5,-9,-10,-9,2,8,9,-2,4,9,-8,-3,-5,5,1,8,-3,-2,-7,3,6,-3,-3,-9,-1,-2,-3,1,7,6,1,3,-2,-7,7,6,3,8,8,-4,8,-9,-1,9,-6,8,-10,3,10,-10,-2,-10,-8,1,-8,7,3,6,-8,-5,-9,-4,-6,2,-9,-2,-7,-5,3,-10],[-5,8,5,-3,1,7,-1,-1,-10,-2,3,9,8,-6,-4,-3,-5,8,-5,3,8,-7,3,-7,-1,3,5,-6,7,-6,-10,1,-10,-5,1,2,-10,-2,7,5,10,-9,-1,8,7,-1,4,2,3,10,5,-7,9,7,7,-3,9,2,7,10,-5,-2,-4,-3,-10,-3,3,10,-9,9,9,3,-3,10,6,-7,10,1,2,3,5,8,7,-3,5,2,-5,3,-9,-10,-2,7,-6,6,-2,-1,6,-8,-9,7,4,-9,-4,9,-7,2,7,3,-8,1,-7,-9,-4,-6,-8,9,4,-1,2,4,8,-1,5,-6,3,5,2,5,-8,8,-5,8,-5,-10,8,8,-9,-8,-3,1]], dtype = "uint8")#candidate|3327|(12, 140)|const|uint8
const_3328 = relay.const(7, dtype = "uint8")#candidate|3328|()|const|uint8
call_3326 = relay.TupleGetItem(func_2112_call(relay.reshape(const_3327.astype('uint8'), [14, 12, 10]), relay.reshape(const_3327.astype('uint8'), [14, 12, 10]), relay.reshape(const_3328.astype('uint8'), []), ), 2)
call_3329 = relay.TupleGetItem(func_2116_call(relay.reshape(const_3327.astype('uint8'), [14, 12, 10]), relay.reshape(const_3327.astype('uint8'), [14, 12, 10]), relay.reshape(const_3328.astype('uint8'), []), ), 2)
uop_3331 = relay.sigmoid(const_3327.astype('float64')) # shape=(12, 140)
func_1515_call = mod.get_global_var('func_1515')
func_1516_call = mutated_mod.get_global_var('func_1516')
call_3336 = relay.TupleGetItem(func_1515_call(), 1)
call_3337 = relay.TupleGetItem(func_1516_call(), 1)
var_3341 = relay.var("var_3341", dtype = "uint8", shape = (12, 140))#candidate|3341|(12, 140)|var|uint8
bop_3342 = relay.less(const_3327.astype('bool'), relay.reshape(var_3341.astype('bool'), relay.shape_of(const_3327))) # shape=(12, 140)
output = relay.Tuple([call_3284,call_3326,const_3328,uop_3331,call_3336,bop_3342,])
output2 = relay.Tuple([call_3285,call_3329,const_3328,uop_3331,call_3337,bop_3342,])
func_3352 = relay.Function([var_3341,], output)
mod['func_3352'] = func_3352
mod = relay.transform.InferType()(mod)
mutated_mod['func_3352'] = func_3352
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3353 = relay.var("var_3353", dtype = "uint8", shape = (12, 140))#candidate|3353|(12, 140)|var|uint8
func_3352_call = mutated_mod.get_global_var('func_3352')
call_3354 = func_3352_call(var_3353)
output = call_3354
func_3355 = relay.Function([var_3353], output)
mutated_mod['func_3355'] = func_3355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_3360 = func_2912_call()
call_3361 = func_2912_call()
uop_3378 = relay.acos(call_3360.astype('float64')) # shape=(8, 13, 16)
uop_3380 = relay.acos(call_3361.astype('float64')) # shape=(8, 13, 16)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_3384 = relay.TupleGetItem(func_2751_call(), 2)
call_3385 = relay.TupleGetItem(func_2753_call(), 2)
bop_3393 = relay.logical_or(uop_3378.astype('bool'), relay.reshape(call_3384.astype('bool'), relay.shape_of(uop_3378))) # shape=(8, 13, 16)
bop_3396 = relay.logical_or(uop_3380.astype('bool'), relay.reshape(call_3385.astype('bool'), relay.shape_of(uop_3380))) # shape=(8, 13, 16)
output = bop_3393
output2 = bop_3396
func_3409 = relay.Function([], output)
mod['func_3409'] = func_3409
mod = relay.transform.InferType()(mod)
mutated_mod['func_3409'] = func_3409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3409_call = mutated_mod.get_global_var('func_3409')
call_3410 = func_3409_call()
output = call_3410
func_3411 = relay.Function([], output)
mutated_mod['func_3411'] = func_3411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2609_call = mod.get_global_var('func_2609')
func_2610_call = mutated_mod.get_global_var('func_2610')
call_3422 = relay.TupleGetItem(func_2609_call(), 0)
call_3423 = relay.TupleGetItem(func_2610_call(), 0)
var_3445 = relay.var("var_3445", dtype = "int64", shape = (8, 13, 16))#candidate|3445|(8, 13, 16)|var|int64
bop_3446 = relay.maximum(call_3422.astype('float32'), relay.reshape(var_3445.astype('float32'), relay.shape_of(call_3422))) # shape=(8, 13, 16)
bop_3449 = relay.maximum(call_3423.astype('float32'), relay.reshape(var_3445.astype('float32'), relay.shape_of(call_3423))) # shape=(8, 13, 16)
output = bop_3446
output2 = bop_3449
func_3471 = relay.Function([var_3445,], output)
mod['func_3471'] = func_3471
mod = relay.transform.InferType()(mod)
mutated_mod['func_3471'] = func_3471
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3472 = relay.var("var_3472", dtype = "int64", shape = (8, 13, 16))#candidate|3472|(8, 13, 16)|var|int64
func_3471_call = mutated_mod.get_global_var('func_3471')
call_3473 = func_3471_call(var_3472)
output = call_3473
func_3474 = relay.Function([var_3472], output)
mutated_mod['func_3474'] = func_3474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_3476 = relay.TupleGetItem(func_2902_call(), 1)
call_3477 = relay.TupleGetItem(func_2904_call(), 1)
func_200_call = mod.get_global_var('func_200')
func_202_call = mutated_mod.get_global_var('func_202')
var_3484 = relay.var("var_3484", dtype = "uint8", shape = (1664,))#candidate|3484|(1664,)|var|uint8
call_3483 = relay.TupleGetItem(func_200_call(relay.reshape(var_3484.astype('uint8'), [8, 13, 16])), 2)
call_3485 = relay.TupleGetItem(func_202_call(relay.reshape(var_3484.astype('uint8'), [8, 13, 16])), 2)
output = relay.Tuple([call_3476,call_3483,var_3484,])
output2 = relay.Tuple([call_3477,call_3485,var_3484,])
func_3500 = relay.Function([var_3484,], output)
mod['func_3500'] = func_3500
mod = relay.transform.InferType()(mod)
var_3501 = relay.var("var_3501", dtype = "uint8", shape = (1664,))#candidate|3501|(1664,)|var|uint8
output = func_3500(var_3501)
func_3502 = relay.Function([var_3501], output)
mutated_mod['func_3502'] = func_3502
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3557 = relay.const([[[True,False,True,False,True],[False,True,False,False,True]],[[True,False,False,False,False],[True,False,True,True,False]],[[True,True,True,False,False],[False,False,False,True,False]],[[False,True,False,True,True],[True,True,True,True,False]],[[False,True,False,False,True],[False,False,True,True,True]],[[True,False,False,True,True],[False,True,True,False,True]],[[True,False,False,True,False],[True,True,True,False,False]]], dtype = "bool")#candidate|3557|(7, 2, 5)|const|bool
var_3558 = relay.var("var_3558", dtype = "bool", shape = (7, 2, 5))#candidate|3558|(7, 2, 5)|var|bool
bop_3559 = relay.logical_or(const_3557.astype('bool'), relay.reshape(var_3558.astype('bool'), relay.shape_of(const_3557))) # shape=(7, 2, 5)
output = relay.Tuple([bop_3559,])
output2 = relay.Tuple([bop_3559,])
func_3572 = relay.Function([var_3558,], output)
mod['func_3572'] = func_3572
mod = relay.transform.InferType()(mod)
var_3573 = relay.var("var_3573", dtype = "bool", shape = (7, 2, 5))#candidate|3573|(7, 2, 5)|var|bool
output = func_3572(var_3573)
func_3574 = relay.Function([var_3573], output)
mutated_mod['func_3574'] = func_3574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2439_call = mod.get_global_var('func_2439')
func_2441_call = mutated_mod.get_global_var('func_2441')
call_3598 = func_2439_call()
call_3599 = func_2439_call()
output = call_3598
output2 = call_3599
func_3608 = relay.Function([], output)
mod['func_3608'] = func_3608
mod = relay.transform.InferType()(mod)
mutated_mod['func_3608'] = func_3608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3608_call = mutated_mod.get_global_var('func_3608')
call_3609 = func_3608_call()
output = call_3609
func_3610 = relay.Function([], output)
mutated_mod['func_3610'] = func_3610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_3611 = func_2912_call()
call_3612 = func_2912_call()
output = call_3611
output2 = call_3612
func_3620 = relay.Function([], output)
mod['func_3620'] = func_3620
mod = relay.transform.InferType()(mod)
output = func_3620()
func_3621 = relay.Function([], output)
mutated_mod['func_3621'] = func_3621
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3632 = relay.var("var_3632", dtype = "float64", shape = (3, 10, 13))#candidate|3632|(3, 10, 13)|var|float64
uop_3633 = relay.log2(var_3632.astype('float64')) # shape=(3, 10, 13)
func_1181_call = mod.get_global_var('func_1181')
func_1183_call = mutated_mod.get_global_var('func_1183')
call_3635 = func_1181_call()
call_3636 = func_1181_call()
output = relay.Tuple([uop_3633,call_3635,])
output2 = relay.Tuple([uop_3633,call_3636,])
func_3638 = relay.Function([var_3632,], output)
mod['func_3638'] = func_3638
mod = relay.transform.InferType()(mod)
mutated_mod['func_3638'] = func_3638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3639 = relay.var("var_3639", dtype = "float64", shape = (3, 10, 13))#candidate|3639|(3, 10, 13)|var|float64
func_3638_call = mutated_mod.get_global_var('func_3638')
call_3640 = func_3638_call(var_3639)
output = call_3640
func_3641 = relay.Function([var_3639], output)
mutated_mod['func_3641'] = func_3641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1501_call = mod.get_global_var('func_1501')
func_1502_call = mutated_mod.get_global_var('func_1502')
call_3662 = relay.TupleGetItem(func_1501_call(), 3)
call_3663 = relay.TupleGetItem(func_1502_call(), 3)
uop_3689 = relay.atan(call_3662.astype('float64')) # shape=(8, 13, 16)
uop_3691 = relay.atan(call_3663.astype('float64')) # shape=(8, 13, 16)
output = relay.Tuple([uop_3689,])
output2 = relay.Tuple([uop_3691,])
func_3715 = relay.Function([], output)
mod['func_3715'] = func_3715
mod = relay.transform.InferType()(mod)
output = func_3715()
func_3716 = relay.Function([], output)
mutated_mod['func_3716'] = func_3716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_3720 = relay.TupleGetItem(func_3234_call(), 0)
call_3721 = relay.TupleGetItem(func_3235_call(), 0)
func_3058_call = mod.get_global_var('func_3058')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_3724 = func_3058_call()
call_3725 = func_3058_call()
output = relay.Tuple([call_3720,call_3724,])
output2 = relay.Tuple([call_3721,call_3725,])
func_3728 = relay.Function([], output)
mod['func_3728'] = func_3728
mod = relay.transform.InferType()(mod)
output = func_3728()
func_3729 = relay.Function([], output)
mutated_mod['func_3729'] = func_3729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2697_call = mod.get_global_var('func_2697')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_3773 = relay.TupleGetItem(func_2697_call(), 1)
call_3774 = relay.TupleGetItem(func_2699_call(), 1)
func_2112_call = mod.get_global_var('func_2112')
func_2116_call = mutated_mod.get_global_var('func_2116')
const_3785 = relay.const([[-7,-10,-5,1],[-1,-7,3,9],[7,2,-8,1],[-1,-5,8,-2],[8,-6,-10,-8],[-5,5,8,7],[-9,-1,9,-2],[2,-5,-5,-5],[-6,3,-9,10],[-5,-1,10,-8],[-9,7,2,-8],[9,5,10,-6],[-3,6,-1,8],[-3,10,-9,2],[9,7,3,6],[-9,-5,-2,-7],[9,9,-8,-7],[-5,4,-5,-3],[-10,-6,6,-2],[-4,5,-9,1],[4,9,8,-4],[-2,9,7,-10],[2,9,-7,-2],[9,6,-10,7],[10,7,-3,-3],[1,2,5,6],[-9,5,5,8],[-5,-5,3,8],[-9,1,7,-7],[-5,-6,-3,10],[-7,-10,2,-8],[2,3,-7,-9],[7,-10,-4,-1],[-8,-1,-1,-2],[6,1,-8,9],[4,5,3,8],[4,2,-7,-8],[2,-5,-10,1],[9,-6,-3,-8],[6,-8,9,-1],[-6,-2,-8,7],[2,2,8,-10],[5,5,2,5],[-1,9,1,-5],[-2,3,9,-9],[1,-3,-5,10],[-10,8,-2,-1],[5,3,7,6],[-6,9,-6,-4],[-10,-10,1,-4],[6,-6,4,1],[7,-5,1,4],[-10,-3,-1,-5],[-8,-7,8,-2],[5,3,5,-9],[8,-9,-7,8],[-5,-4,-10,9],[-8,6,8,-10],[-10,-2,-7,-9],[7,7,10,9],[-8,4,-4,5],[1,-5,3,-4],[8,-8,-9,1],[-3,-7,-6,10],[3,-2,-1,6],[10,1,-7,-4],[2,-2,-9,6],[3,-6,-4,-3],[-2,-2,1,5],[1,3,-2,5],[-1,7,-1,-3],[-8,3,5,7],[-8,2,-8,1],[2,9,2,-10],[-2,4,-9,10],[-6,-9,9,-2],[-6,-8,-9,6],[-4,-7,-1,-1],[5,-10,4,2],[-3,3,-9,-2],[-9,-7,-1,10],[-10,-2,-6,-5],[2,-5,-5,6],[-10,-3,6,-3],[-6,-3,-5,-2],[2,5,-9,-10],[6,-7,4,3],[4,4,1,-7],[8,-6,3,-6],[-2,-4,1,-9],[-1,2,-10,1],[2,6,-5,-2],[2,-5,-6,1],[-4,-6,-1,6],[1,-7,-4,7],[-8,-1,7,-5],[1,-6,-5,-4],[4,-5,-7,8],[2,1,8,4],[-2,-6,-6,9],[-2,-6,-2,5],[-10,-2,3,3],[7,-1,-3,-8],[10,5,4,-5],[9,-1,-2,6],[7,7,9,-7],[-5,9,3,-4],[-1,1,4,-4],[-9,-5,-3,1],[10,2,-9,6],[-7,-3,-2,5],[7,-3,-4,-8],[-1,-4,-6,6],[4,-5,-7,6],[-6,6,5,5],[9,-4,4,10],[5,-10,10,6],[4,-6,4,4],[-10,-10,-4,-6],[3,-8,4,-2],[1,-7,-10,4],[6,-4,1,-10],[8,5,-5,7],[-4,4,-4,-4],[-8,7,-6,9],[-2,-2,-3,-5],[4,-5,2,6],[-6,4,7,-6],[-1,-1,3,-10],[-7,7,5,-10],[-1,-8,4,10],[6,-1,-2,-6],[-9,1,-10,-6],[-3,6,-4,-7],[-9,9,2,-7],[-3,-9,-5,-7],[5,8,-9,2],[-7,10,-3,6],[3,-9,-5,1],[-5,3,7,-6],[-10,-8,9,8],[8,-9,6,-5],[1,4,-10,-3],[7,-7,-6,9],[-7,2,8,-4],[-10,7,8,-5],[-8,6,5,-3],[5,-9,2,4],[4,7,-10,8],[4,7,1,-1],[-2,7,6,8],[-1,-10,-4,2],[4,1,10,5],[-7,6,-6,-7],[3,6,7,9],[-10,10,-7,3],[4,7,-5,10],[7,-2,-4,-3],[-6,-6,-2,10],[8,-9,4,6],[8,-4,6,-7],[-1,-9,-7,-3],[1,5,-6,7],[-2,-9,-8,4],[10,9,3,2],[4,-10,2,-3],[3,-6,2,5],[10,2,-2,-4],[-6,10,-8,5],[2,2,-1,8],[-4,4,-8,1],[4,-3,-2,9],[-1,-9,-1,-10],[2,-6,-8,6],[9,-9,-9,-2],[-6,9,4,-7],[-7,4,1,-1],[-6,5,-3,8],[-10,-6,1,-2],[-7,-6,1,5],[-10,-7,3,-3],[5,4,6,10],[1,5,-6,-9],[-1,3,8,1],[-9,6,-4,-10],[6,7,-8,-10],[-2,10,-5,10],[-6,8,-3,10],[5,3,-7,-10],[-8,7,-5,6],[-3,7,5,-1],[-2,-5,-8,-6],[-4,-2,-1,6],[-9,-7,1,2],[-8,-3,6,-6],[-5,-5,7,-3],[10,4,6,-3],[4,-9,-3,-10],[-10,8,6,-4],[6,-1,-3,-5],[-10,6,-8,2],[1,8,2,7],[-10,-8,8,7],[-3,8,-5,-9],[-10,2,6,-2],[5,10,-8,9],[-9,-2,1,2],[10,-2,-1,-7],[-5,-2,2,5],[4,5,2,7],[3,8,-1,-9],[-10,-3,1,-3],[10,7,-9,-9],[10,4,10,-1],[1,8,-2,2],[-10,-3,4,9],[-3,-5,-9,-7],[10,10,3,4],[3,-7,-1,-4],[-3,-3,-3,2],[-7,10,1,6],[9,1,9,5],[9,4,-10,-2],[7,9,-8,-8],[7,-2,3,10],[-5,-3,6,6],[-9,-5,3,9],[3,-10,10,5],[-3,-6,6,-10],[4,-9,1,-6],[-8,-7,-8,-10],[8,-1,7,-6],[2,1,-7,-3],[4,3,-7,-6],[-10,5,3,1],[7,-2,6,7],[9,8,-8,-6],[2,2,8,4],[2,8,-5,9],[-10,6,-10,-6],[10,-4,4,5],[-1,3,4,9],[-7,3,7,5],[4,3,-6,-2],[2,7,10,-2],[-6,2,2,-5],[-8,4,2,-3],[3,-2,-3,-5],[4,1,-3,-5],[-9,8,8,-2],[-4,4,-6,-4],[-2,-5,-3,-2],[-4,3,5,6],[-4,-5,8,3],[-6,7,3,-10],[-10,-2,7,1],[6,-7,-1,6],[7,-10,-1,-6],[1,6,5,-10],[10,9,7,-9],[6,-5,10,2],[3,10,-8,-10],[10,-2,-3,-3],[6,2,-3,-8],[8,-4,5,4],[2,3,-2,7],[-8,-8,-3,5],[2,7,-8,-2],[8,-3,-6,2],[-2,-5,5,-6],[-5,5,-5,9],[6,3,-3,-10],[-5,-6,3,6],[-3,2,7,3],[4,9,-8,9],[6,-10,8,-10],[5,1,-3,5],[-10,-4,-5,-6],[-6,-10,-3,8],[10,-8,10,-1],[-1,-4,1,-10],[4,-7,-2,-10],[10,-3,-7,-4],[-1,-5,-8,7],[-9,6,8,-1],[10,3,-3,-2],[-1,7,8,-6],[2,1,10,-3],[-6,-10,-5,-9],[3,8,-5,8],[-7,-5,-6,5],[4,10,-3,4],[-2,-8,-7,3],[-8,-5,-3,-8],[-10,5,-6,4],[8,6,6,5],[-6,6,-7,-5],[-4,-10,5,-7],[-3,-1,-5,-10],[8,6,-8,4],[3,7,-3,-7],[-3,1,-4,-5],[3,5,10,10],[-1,-1,-9,-3],[9,2,-4,-8],[-5,7,9,6],[7,-9,7,4],[-6,-9,2,-7],[5,2,8,8],[-10,3,-6,-1],[-2,-9,-10,9],[8,2,3,2],[9,-7,5,-2],[-10,-2,6,3],[-4,7,5,-9],[-7,4,10,-7],[-9,6,10,7],[-3,-8,4,6],[-4,-1,10,-2],[3,-4,2,-2],[6,5,5,5],[4,-8,-5,-8],[7,5,-1,4],[-5,-7,-10,7],[6,-1,3,3],[-9,8,7,-10],[5,-2,4,-2],[-6,5,-7,-3],[2,6,-10,-5],[-9,-3,-10,1],[-10,-4,2,-7],[-7,4,3,-9],[-1,-4,-5,2],[-3,2,-9,9],[-9,8,-10,-8],[7,1,9,-7],[-6,-3,-2,-6],[-1,-8,-3,-2],[9,2,4,8],[-3,-1,10,5],[9,-8,-7,5],[3,8,10,8],[1,1,-3,-7],[8,1,6,-4],[5,7,8,-10],[5,9,-8,-5],[9,4,-4,8],[-1,-2,2,5],[9,9,-3,-10],[-7,-4,-6,-5],[8,4,-2,-6],[9,1,5,3],[7,-1,3,9],[-8,6,-5,-8],[-2,-4,5,9],[-7,9,8,6],[-4,-6,-10,-6],[9,2,-4,-6],[5,3,10,-5],[-6,-1,-6,10],[5,6,10,-4],[5,4,8,-6],[-9,-2,2,-8],[-2,3,-7,8],[6,7,-8,-8],[9,-4,3,10],[10,-3,-9,-1],[1,9,-6,9],[-2,9,-9,5],[-2,-7,-1,-6],[-8,3,1,10],[-9,-9,-5,6],[-9,7,5,-6],[-3,9,9,-4],[6,4,-5,-9],[-3,-9,9,6],[-2,5,-9,2],[3,5,-9,-9],[-10,2,9,-10],[-2,-1,-4,-10],[-1,2,6,-1],[7,1,9,-3],[-4,4,10,6],[-3,-2,3,3],[-7,-6,-1,1],[7,6,-3,4],[-7,9,-4,-9],[1,4,-3,9],[-4,-2,2,-2],[7,-4,8,8],[-8,-3,3,1],[-3,-7,4,8],[-1,-2,6,-1],[-4,5,-2,-9],[9,7,4,-5],[5,-5,8,-8],[6,9,5,-6],[4,1,4,10],[-2,7,-5,2],[2,2,1,-8],[-1,8,8,3],[7,10,3,-7],[9,2,-4,-5],[-4,-8,-8,-1],[-3,2,-6,3],[-10,5,5,10],[-5,9,1,-8],[2,9,4,6],[10,9,5,-9],[9,8,-7,-9],[5,4,1,-8],[-9,2,8,1],[7,5,-3,5],[-8,7,5,8],[3,3,-3,8],[7,-5,7,-6],[5,-6,-6,10],[6,-1,-3,-9],[2,-2,-3,9],[10,9,-10,-4]], dtype = "uint8")#candidate|3785|(420, 4)|const|uint8
const_3786 = relay.const(3, dtype = "uint8")#candidate|3786|()|const|uint8
call_3784 = relay.TupleGetItem(func_2112_call(relay.reshape(const_3785.astype('uint8'), [14, 12, 10]), relay.reshape(const_3785.astype('uint8'), [14, 12, 10]), relay.reshape(const_3786.astype('uint8'), []), ), 3)
call_3787 = relay.TupleGetItem(func_2116_call(relay.reshape(const_3785.astype('uint8'), [14, 12, 10]), relay.reshape(const_3785.astype('uint8'), [14, 12, 10]), relay.reshape(const_3786.astype('uint8'), []), ), 3)
func_752_call = mod.get_global_var('func_752')
func_755_call = mutated_mod.get_global_var('func_755')
const_3795 = relay.const([4.275112,-1.562849,-9.808960,-3.717045,7.531678,2.558615,-3.997519,-2.393681,1.729172,-2.932162,7.996337,4.272717,-4.544257,8.541722,-2.227323,-5.338297,-8.845308,4.013543,1.317513,-7.900147,-3.340666,-8.323662,5.448399,3.587532,-4.598392,6.283558,0.334089,5.610709,4.570687,8.351479,4.404093,7.104773,-4.007395,6.779324,-6.695882,-4.886426,9.061528,5.537647,1.868576,-5.584326,-5.101778,-6.127626,-0.129967,-5.805162,-6.870383,7.797855,8.715622,8.556327,0.429920,6.285274,-5.751044,-4.678608,-0.863939,5.732858,-6.830193,6.131114,6.089242,-4.536654,-5.277456,3.086456,5.658167,-0.123208,-8.817309,-3.987068,-0.706142,0.151447,-8.156551,1.302874,-0.622929,-5.351264,-0.152695,2.043879,2.021156,7.992877,-5.629934,-0.577530,9.264549,-3.172223,-4.447440,-6.847740,-5.805399,-6.423937,5.990434,-4.632508,-6.728243,5.993444,-9.356902,-8.140420,-1.078217,7.411254,2.620986,-3.322635,4.138311,-3.563910,-1.037885,-3.581512,-7.105841,2.325752,-9.571853,9.840714,-6.276046,8.973515,-7.738835,2.180507,6.268104,9.048541,-4.667746,-8.910160,3.825918,-2.118216,3.627399,-3.002435,0.970369,4.874891,7.445416,-9.232074,5.900336,3.719962,9.196538,2.956112,3.308855,8.490792,-2.021152,9.440787,-6.379010,4.464376,9.150636,-0.695574,9.122352,-3.606308,-6.172546,4.165943,1.685932,8.812233,6.200889,9.014938,-9.865397,-7.195985,-8.783343,-4.927677,1.489471,-6.460627,1.058234,3.929436,7.765481,-5.765809,-6.746175,1.730412,-7.549694,3.406010,0.464460,-9.910313,3.300910,4.569879,8.153539,5.460826,8.802319,7.897224,-2.629445,-4.910883,-8.305887,1.365494,-0.858294,-6.572270,-4.981340,-5.608386,5.411435,3.586183], dtype = "float64")#candidate|3795|(168,)|const|float64
call_3794 = func_752_call(relay.reshape(const_3795.astype('float64'), [14, 6, 2]))
call_3796 = func_752_call(relay.reshape(const_3795.astype('float64'), [14, 6, 2]))
output = relay.Tuple([call_3773,call_3784,const_3785,const_3786,call_3794,const_3795,])
output2 = relay.Tuple([call_3774,call_3787,const_3785,const_3786,call_3796,const_3795,])
func_3800 = relay.Function([], output)
mod['func_3800'] = func_3800
mod = relay.transform.InferType()(mod)
mutated_mod['func_3800'] = func_3800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3800_call = mutated_mod.get_global_var('func_3800')
call_3801 = func_3800_call()
output = call_3801
func_3802 = relay.Function([], output)
mutated_mod['func_3802'] = func_3802
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3834 = relay.var("var_3834", dtype = "bool", shape = (7, 15, 9))#candidate|3834|(7, 15, 9)|var|bool
var_3835 = relay.var("var_3835", dtype = "bool", shape = (7, 15, 9))#candidate|3835|(7, 15, 9)|var|bool
bop_3836 = relay.logical_and(var_3834.astype('bool'), relay.reshape(var_3835.astype('bool'), relay.shape_of(var_3834))) # shape=(7, 15, 9)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3846 = relay.TupleGetItem(func_2523_call(), 0)
call_3847 = relay.TupleGetItem(func_2525_call(), 0)
func_1622_call = mod.get_global_var('func_1622')
func_1623_call = mutated_mod.get_global_var('func_1623')
call_3850 = func_1622_call()
call_3851 = func_1622_call()
var_3852 = relay.var("var_3852", dtype = "bool", shape = (7, 15, 9))#candidate|3852|(7, 15, 9)|var|bool
bop_3853 = relay.left_shift(var_3834.astype('uint16'), relay.reshape(var_3852.astype('uint16'), relay.shape_of(var_3834))) # shape=(7, 15, 9)
output = relay.Tuple([bop_3836,call_3846,call_3850,bop_3853,])
output2 = relay.Tuple([bop_3836,call_3847,call_3851,bop_3853,])
func_3868 = relay.Function([var_3834,var_3835,var_3852,], output)
mod['func_3868'] = func_3868
mod = relay.transform.InferType()(mod)
var_3869 = relay.var("var_3869", dtype = "bool", shape = (7, 15, 9))#candidate|3869|(7, 15, 9)|var|bool
var_3870 = relay.var("var_3870", dtype = "bool", shape = (7, 15, 9))#candidate|3870|(7, 15, 9)|var|bool
var_3871 = relay.var("var_3871", dtype = "bool", shape = (7, 15, 9))#candidate|3871|(7, 15, 9)|var|bool
output = func_3868(var_3869,var_3870,var_3871,)
func_3872 = relay.Function([var_3869,var_3870,var_3871,], output)
mutated_mod['func_3872'] = func_3872
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3921 = relay.var("var_3921", dtype = "float32", shape = (3, 8, 14))#candidate|3921|(3, 8, 14)|var|float32
var_3922 = relay.var("var_3922", dtype = "float32", shape = (3, 8, 14))#candidate|3922|(3, 8, 14)|var|float32
bop_3923 = relay.mod(var_3921.astype('float32'), relay.reshape(var_3922.astype('float32'), relay.shape_of(var_3921))) # shape=(3, 8, 14)
output = bop_3923
output2 = bop_3923
func_3938 = relay.Function([var_3921,var_3922,], output)
mod['func_3938'] = func_3938
mod = relay.transform.InferType()(mod)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3938_call = mutated_mod.get_global_var('func_3938')
var_3940 = relay.var("var_3940", dtype = "float32", shape = (3, 8, 14))#candidate|3940|(3, 8, 14)|var|float32
var_3941 = relay.var("var_3941", dtype = "float32", shape = (3, 8, 14))#candidate|3941|(3, 8, 14)|var|float32
call_3939 = func_3938_call(var_3940,var_3941,)
output = call_3939
func_3942 = relay.Function([var_3940,var_3941,], output)
mutated_mod['func_3942'] = func_3942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3953 = relay.var("var_3953", dtype = "bool", shape = (5, 7, 10))#candidate|3953|(5, 7, 10)|var|bool
var_3954 = relay.var("var_3954", dtype = "bool", shape = (5, 7, 10))#candidate|3954|(5, 7, 10)|var|bool
bop_3955 = relay.logical_and(var_3953.astype('bool'), relay.reshape(var_3954.astype('bool'), relay.shape_of(var_3953))) # shape=(5, 7, 10)
output = relay.Tuple([bop_3955,])
output2 = relay.Tuple([bop_3955,])
func_3959 = relay.Function([var_3953,var_3954,], output)
mod['func_3959'] = func_3959
mod = relay.transform.InferType()(mod)
var_3960 = relay.var("var_3960", dtype = "bool", shape = (5, 7, 10))#candidate|3960|(5, 7, 10)|var|bool
var_3961 = relay.var("var_3961", dtype = "bool", shape = (5, 7, 10))#candidate|3961|(5, 7, 10)|var|bool
output = func_3959(var_3960,var_3961,)
func_3962 = relay.Function([var_3960,var_3961,], output)
mutated_mod['func_3962'] = func_3962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2135_call = mod.get_global_var('func_2135')
func_2137_call = mutated_mod.get_global_var('func_2137')
call_3967 = relay.TupleGetItem(func_2135_call(), 0)
call_3968 = relay.TupleGetItem(func_2137_call(), 0)
output = relay.Tuple([call_3967,])
output2 = relay.Tuple([call_3968,])
func_3972 = relay.Function([], output)
mod['func_3972'] = func_3972
mod = relay.transform.InferType()(mod)
mutated_mod['func_3972'] = func_3972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3972_call = mutated_mod.get_global_var('func_3972')
call_3973 = func_3972_call()
output = call_3973
func_3974 = relay.Function([], output)
mutated_mod['func_3974'] = func_3974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3608_call = mod.get_global_var('func_3608')
func_3610_call = mutated_mod.get_global_var('func_3610')
call_4011 = func_3608_call()
call_4012 = func_3608_call()
func_2112_call = mod.get_global_var('func_2112')
func_2116_call = mutated_mod.get_global_var('func_2116')
const_4018 = relay.const([[-5,3],[-5,8],[-2,-3],[5,9],[-9,-6],[-9,7],[10,-5],[-5,6],[5,-4],[4,8],[-2,-4],[-6,-4],[-5,4],[-7,-7],[4,-9],[10,-10],[5,-5],[6,4],[4,-5],[-8,-5],[-1,10],[-1,-5],[8,3],[9,2],[7,-2],[3,-1],[3,-5],[-4,7],[-9,-1],[3,-7],[-10,-10],[-6,-3],[-2,-6],[-3,9],[-2,9],[7,9],[-3,8],[8,7],[-6,7],[9,-4],[4,-3],[-6,3],[9,4],[-7,3],[5,6],[-9,-3],[9,-8],[9,9],[-4,2],[-7,8],[6,3],[4,5],[-1,7],[3,-6],[10,-1],[6,6],[-2,-9],[-3,6],[-10,-5],[9,8],[-1,8],[2,6],[-8,5],[-7,-3],[7,-10],[3,-2],[-9,7],[-8,-5],[-9,5],[-7,-7],[8,-10],[-1,3],[-8,-8],[1,2],[-8,-7],[6,-9],[5,8],[5,-8],[5,5],[10,4],[3,9],[-4,5],[1,-10],[1,6],[1,9],[-1,-8],[-4,2],[1,4],[-10,9],[3,7],[3,5],[-7,2],[-4,4],[8,2],[5,8],[4,1],[2,-9],[3,10],[-1,3],[-5,6],[6,7],[-3,5],[-4,5],[2,3],[7,10],[-6,-9],[-5,-7],[-5,-2],[-6,-4],[7,-7],[10,-3],[10,-6],[-6,9],[7,2],[-10,2],[3,-6],[-2,-6],[-10,4],[-8,2],[-2,7],[7,1],[5,5],[2,1],[-1,4],[9,-6],[6,-9],[-8,-4],[-1,10],[8,1],[-7,-9],[4,-4],[-8,2],[-10,-8],[-8,-9],[-10,-7],[-4,1],[8,-5],[8,4],[5,9],[-8,-5],[-9,3],[2,4],[-6,4],[-9,2],[-7,-2],[3,9],[8,5],[8,4],[-3,-5],[-2,-6],[1,8],[5,7],[9,6],[-9,-3],[-2,-3],[-8,-8],[-6,5],[-1,6],[-1,1],[-4,-7],[-2,-6],[10,8],[-8,2],[1,-7],[10,-7],[-5,4],[5,1],[8,4],[-10,10],[10,2],[2,5],[4,10],[-6,-7],[-10,-6],[-8,6],[-2,5],[3,-4],[7,2],[-1,-3],[-9,-1],[2,5],[-10,-6],[-7,-4],[5,4],[5,10],[5,-1],[8,-1],[7,-1],[1,10],[10,-10],[2,-7],[1,4],[9,-8],[-5,9],[3,8],[2,-10],[9,2],[9,6],[6,-8],[-5,3],[-6,6],[-1,3],[-5,-5],[-2,1],[8,3],[-7,-9],[-2,-8],[-1,9],[-5,7],[2,-10],[-2,-5],[2,8],[-9,-7],[1,7],[-5,10],[-9,1],[6,10],[9,6],[-4,8],[6,6],[-10,-2],[-1,2],[-8,-9],[-3,-1],[-2,6],[10,5],[-2,-2],[10,4],[2,-8],[-8,8],[7,5],[10,9],[-6,3],[7,-1],[-2,7],[-2,-1],[10,-9],[2,-6],[-7,-8],[-8,10],[4,-1],[-3,1],[-7,5],[-1,6],[-8,2],[4,-10],[1,-7],[5,-3],[1,9],[8,7],[-8,7],[-3,-5],[-9,10],[6,-4],[7,6],[-9,10],[-4,-3],[-9,-10],[-7,10],[-1,8],[1,5],[7,4],[3,8],[8,-3],[9,7],[-8,-8],[-3,4],[1,-5],[-1,10],[2,-4],[2,6],[-1,4],[-4,-9],[7,9],[4,-3],[-7,-7],[-9,-10],[1,-5],[-7,-4],[-1,-8],[1,-9],[-3,-8],[4,-1],[-10,-1],[7,1],[7,-10],[-8,-5],[-7,3],[-10,-6],[-1,-1],[-4,5],[-5,4],[-10,-10],[10,5],[8,-4],[-5,-3],[-9,10],[-1,-2],[7,10],[8,2],[10,6],[3,7],[-3,6],[-10,-3],[-8,-9],[-7,-6],[10,4],[4,5],[9,-4],[-5,6],[6,6],[-1,-6],[-5,9],[-8,4],[-3,-6],[-6,10],[4,-10],[9,-9],[-7,2],[5,8],[3,-9],[4,-8],[4,3],[9,-5],[-7,4],[-10,10],[9,9],[10,-5],[7,-3],[-9,-8],[-7,3],[4,10],[5,-9],[8,-4],[1,-2],[-5,3],[1,4],[9,3],[3,-3],[-3,10],[7,-5],[-9,2],[4,-1],[1,2],[-4,-1],[6,-10],[-1,-6],[5,4],[-5,9],[-8,4],[-6,-3],[-2,8],[9,8],[7,-6],[10,3],[-8,-9],[6,7],[-8,-5],[9,-1],[1,7],[-1,7],[3,-6],[-3,-10],[6,6],[-7,5],[5,2],[-8,-4],[-2,-8],[4,-3],[-9,9],[8,5],[-9,5],[3,5],[-9,-1],[-10,5],[4,7],[1,4],[-10,1],[2,-1],[8,-9],[5,-10],[-1,-1],[-8,4],[-10,-1],[-2,-10],[-9,10],[9,-4],[-9,-8],[9,9],[1,-2],[6,2],[-7,-6],[9,3],[7,1],[7,2],[10,-10],[-2,-8],[1,-3],[-6,-5],[-9,5],[-9,7],[-4,-3],[-6,6],[-9,-5],[-7,3],[3,-7],[10,-5],[6,-6],[-8,2],[-3,-4],[-2,-3],[7,1],[10,-4],[-9,-5],[4,7],[-10,5],[-7,-2],[4,9],[6,-6],[-9,7],[-10,-6],[3,-7],[1,-6],[-6,-1],[-10,5],[-8,-9],[-6,7],[3,-7],[-4,-1],[4,3],[9,-6],[-2,1],[-9,3],[1,-2],[-8,-2],[-3,-1],[4,6],[-9,5],[8,-4],[10,10],[2,-7],[-7,7],[9,4],[10,1],[-9,-4],[-3,4],[-10,-4],[4,10],[-9,-6],[-7,10],[6,-8],[-9,-2],[3,5],[-5,-9],[-9,-5],[-7,8],[3,10],[1,-4],[4,-3],[8,-1],[1,10],[5,1],[4,-9],[-3,7],[-5,4],[9,-2],[1,-5],[-1,1],[-2,-8],[-10,-3],[4,-5],[10,-1],[-1,2],[-6,-2],[-10,-5],[3,4],[6,-2],[-10,-1],[6,-1],[10,-3],[8,2],[10,10],[-10,2],[10,-9],[-10,5],[8,2],[3,-2],[7,3],[-9,-1],[8,-8],[6,-6],[-7,-5],[7,-7],[-5,9],[-2,1],[6,-7],[1,-5],[-7,1],[-4,10],[-1,-10],[-4,-3],[4,6],[-5,-7],[5,6],[-10,-6],[4,2],[4,1],[8,6],[-6,10],[-3,10],[-5,8],[1,-5],[7,-1],[9,-2],[7,10],[5,-5],[7,3],[-4,-7],[-9,9],[3,2],[3,2],[7,7],[-7,7],[-3,3],[10,9],[8,-10],[-2,-7],[-3,4],[2,-10],[-10,-1],[3,9],[10,5],[7,-3],[1,1],[2,-8],[-9,-1],[-10,10],[-7,9],[8,-6],[-9,10],[5,2],[-7,-9],[3,4],[-2,2],[7,6],[-10,-3],[-2,-9],[-10,-8],[2,-10],[2,-8],[7,-6],[-8,-4],[8,-8],[-4,9],[10,8],[6,-6],[5,7],[-5,4],[-6,4],[-7,-6],[8,-7],[5,-10],[-5,4],[6,10],[-5,-3],[-2,4],[-5,2],[7,-1],[2,-7],[4,-3],[-8,10],[6,-7],[9,-3],[7,8],[4,-6],[-10,5],[-2,10],[-2,7],[-9,-5],[-9,7],[-4,-10],[6,3],[-10,2],[-5,-1],[-3,-5],[3,6],[8,-4],[-8,4],[1,-3],[4,8],[6,-3],[9,9],[4,-7],[-5,8],[6,10],[-4,8],[-10,2],[-8,7],[10,-4],[-3,-3],[7,5],[-4,-5],[4,-6],[2,2],[6,6],[-4,-9],[-3,7],[6,-7],[9,4],[5,-6],[5,-7],[-10,8],[5,-10],[-7,7],[-2,9],[4,2],[8,-9],[-7,1],[-10,10],[-1,6],[2,-7],[4,2],[8,-7],[-7,-6],[-5,7],[-3,-4],[9,3],[-2,-6],[-4,5],[6,-8],[-9,7],[-4,-9],[9,10],[6,-6],[-10,7],[-7,-10],[5,-3],[-5,5],[3,-7],[6,-5],[6,8],[-3,-7],[3,-7],[-6,-5],[2,-3],[-6,8],[2,-8],[5,-5],[1,3],[10,-7],[5,-5],[-10,-5],[8,-9],[8,-6],[7,1],[9,5],[1,-4],[-1,4],[-6,8],[-1,10],[10,-4],[9,1],[3,-1],[9,-2],[3,9],[-8,9],[-4,-2],[9,4],[1,10],[-7,-9],[-4,-3],[-6,1],[-3,-5],[-5,-5],[-3,-6],[8,4],[8,-3],[-6,7],[3,-2],[7,8],[8,-10],[-8,-4],[3,3],[-1,-5],[4,6],[-2,-1],[5,4],[1,-3],[-7,-1],[-10,-8],[-6,8],[-2,8],[3,-6],[-9,2],[10,-7],[1,-9],[-2,5],[-7,9],[-8,3],[-2,-3],[-9,9],[-6,3],[8,9],[9,-8],[-8,5],[8,1],[10,3],[6,-6],[5,-2],[-8,-8],[-4,-4],[5,-4],[-4,10],[-10,7],[6,-2],[8,-5],[5,5],[-2,-8],[2,-9],[-3,-1],[9,-1],[2,-9],[-8,1],[10,8],[-5,7],[-7,-4],[-10,-3],[-6,-1],[6,6],[-8,8],[-7,-1],[-5,10],[-3,7],[-5,-7],[6,9],[-6,8],[2,4],[8,-7],[9,2],[8,-5],[-3,3],[3,-5],[3,2],[-6,-3],[-4,-10],[9,9],[-7,3],[5,10],[-10,7],[2,4],[-8,5],[5,-2],[-7,1],[-10,-3],[3,4],[-3,7],[-7,7],[-10,5],[5,2],[9,1],[6,1],[4,5],[-9,-7],[-3,-6],[-1,-8],[-3,-1],[-4,-10],[-6,-9],[5,-8],[-4,-6],[2,-5],[-8,-5],[-5,-1],[7,-9],[-4,-6],[-2,-3],[-6,3],[6,3],[5,-4],[1,3],[4,4],[-8,4],[2,4],[-4,-10],[-10,10],[-4,-5],[-1,1],[8,-7],[10,4],[4,1],[8,1],[-4,4],[-6,1],[9,7],[7,-3],[-2,9],[-2,3],[3,-6],[-9,4],[-10,7],[-5,5],[6,-6],[-2,10],[-7,-7],[4,-9],[-3,-9],[-5,-8],[-3,10],[5,6],[7,-4],[8,4],[-3,-8],[-10,5],[3,-8],[6,3],[10,1],[-9,5],[-6,-7],[-5,2],[2,6],[-7,5],[-4,8],[8,-1],[-5,4],[-1,3],[9,4],[1,-3],[-7,4],[9,-6],[4,-3],[7,3],[-10,7],[-7,9],[-10,-2],[-8,-5],[4,-9],[-1,-8],[-10,9],[6,-1],[-10,-8]], dtype = "uint8")#candidate|4018|(840, 2)|const|uint8
var_4019 = relay.var("var_4019", dtype = "uint8", shape = ())#candidate|4019|()|var|uint8
call_4017 = relay.TupleGetItem(func_2112_call(relay.reshape(const_4018.astype('uint8'), [14, 12, 10]), relay.reshape(const_4018.astype('uint8'), [14, 12, 10]), relay.reshape(var_4019.astype('uint8'), []), ), 1)
call_4020 = relay.TupleGetItem(func_2116_call(relay.reshape(const_4018.astype('uint8'), [14, 12, 10]), relay.reshape(const_4018.astype('uint8'), [14, 12, 10]), relay.reshape(var_4019.astype('uint8'), []), ), 1)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_4021 = relay.TupleGetItem(func_2523_call(), 0)
call_4022 = relay.TupleGetItem(func_2525_call(), 0)
uop_4028 = relay.atan(const_4018.astype('float64')) # shape=(840, 2)
uop_4050 = relay.sin(uop_4028.astype('float64')) # shape=(840, 2)
bop_4053 = relay.bitwise_or(uop_4028.astype('int32'), relay.reshape(uop_4050.astype('int32'), relay.shape_of(uop_4028))) # shape=(840, 2)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_4060 = func_2912_call()
call_4061 = func_2912_call()
output = relay.Tuple([call_4011,call_4017,var_4019,call_4021,bop_4053,call_4060,])
output2 = relay.Tuple([call_4012,call_4020,var_4019,call_4022,bop_4053,call_4061,])
func_4067 = relay.Function([var_4019,], output)
mod['func_4067'] = func_4067
mod = relay.transform.InferType()(mod)
mutated_mod['func_4067'] = func_4067
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4068 = relay.var("var_4068", dtype = "uint8", shape = ())#candidate|4068|()|var|uint8
func_4067_call = mutated_mod.get_global_var('func_4067')
call_4069 = func_4067_call(var_4068)
output = call_4069
func_4070 = relay.Function([var_4068], output)
mutated_mod['func_4070'] = func_4070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_4085 = func_108_call()
call_4086 = func_108_call()
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_4098 = relay.TupleGetItem(func_353_call(), 2)
call_4099 = relay.TupleGetItem(func_355_call(), 2)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_4107 = relay.TupleGetItem(func_449_call(), 1)
call_4108 = relay.TupleGetItem(func_451_call(), 1)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_4126 = relay.TupleGetItem(func_2751_call(), 0)
call_4127 = relay.TupleGetItem(func_2753_call(), 0)
output = relay.Tuple([call_4085,call_4098,call_4107,call_4126,])
output2 = relay.Tuple([call_4086,call_4099,call_4108,call_4127,])
func_4156 = relay.Function([], output)
mod['func_4156'] = func_4156
mod = relay.transform.InferType()(mod)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4156_call = mutated_mod.get_global_var('func_4156')
call_4157 = func_4156_call()
output = call_4157
func_4158 = relay.Function([], output)
mutated_mod['func_4158'] = func_4158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_4190 = func_2912_call()
call_4191 = func_2912_call()
output = call_4190
output2 = call_4191
func_4196 = relay.Function([], output)
mod['func_4196'] = func_4196
mod = relay.transform.InferType()(mod)
mutated_mod['func_4196'] = func_4196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mutated_mod.get_global_var('func_4196')
call_4197 = func_4196_call()
output = call_4197
func_4198 = relay.Function([], output)
mutated_mod['func_4198'] = func_4198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3800_call = mod.get_global_var('func_3800')
func_3802_call = mutated_mod.get_global_var('func_3802')
call_4213 = relay.TupleGetItem(func_3800_call(), 1)
call_4214 = relay.TupleGetItem(func_3802_call(), 1)
func_752_call = mod.get_global_var('func_752')
func_755_call = mutated_mod.get_global_var('func_755')
var_4225 = relay.var("var_4225", dtype = "float64", shape = (168,))#candidate|4225|(168,)|var|float64
call_4224 = func_752_call(relay.reshape(var_4225.astype('float64'), [14, 6, 2]))
call_4226 = func_752_call(relay.reshape(var_4225.astype('float64'), [14, 6, 2]))
var_4230 = relay.var("var_4230", dtype = "uint8", shape = (14, 12, 10))#candidate|4230|(14, 12, 10)|var|uint8
bop_4231 = relay.maximum(call_4213.astype('uint64'), relay.reshape(var_4230.astype('uint64'), relay.shape_of(call_4213))) # shape=(14, 12, 10)
bop_4234 = relay.maximum(call_4214.astype('uint64'), relay.reshape(var_4230.astype('uint64'), relay.shape_of(call_4214))) # shape=(14, 12, 10)
output = relay.Tuple([call_4224,var_4225,bop_4231,])
output2 = relay.Tuple([call_4226,var_4225,bop_4234,])
func_4258 = relay.Function([var_4225,var_4230,], output)
mod['func_4258'] = func_4258
mod = relay.transform.InferType()(mod)
var_4259 = relay.var("var_4259", dtype = "float64", shape = (168,))#candidate|4259|(168,)|var|float64
var_4260 = relay.var("var_4260", dtype = "uint8", shape = (14, 12, 10))#candidate|4260|(14, 12, 10)|var|uint8
output = func_4258(var_4259,var_4260,)
func_4261 = relay.Function([var_4259,var_4260,], output)
mutated_mod['func_4261'] = func_4261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3715_call = mod.get_global_var('func_3715')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_4290 = relay.TupleGetItem(func_3715_call(), 0)
call_4291 = relay.TupleGetItem(func_3716_call(), 0)
output = relay.Tuple([call_4290,])
output2 = relay.Tuple([call_4291,])
func_4294 = relay.Function([], output)
mod['func_4294'] = func_4294
mod = relay.transform.InferType()(mod)
mutated_mod['func_4294'] = func_4294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4294_call = mutated_mod.get_global_var('func_4294')
call_4295 = func_4294_call()
output = call_4295
func_4296 = relay.Function([], output)
mutated_mod['func_4296'] = func_4296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1181_call = mod.get_global_var('func_1181')
func_1183_call = mutated_mod.get_global_var('func_1183')
call_4326 = func_1181_call()
call_4327 = func_1181_call()
output = relay.Tuple([call_4326,])
output2 = relay.Tuple([call_4327,])
func_4328 = relay.Function([], output)
mod['func_4328'] = func_4328
mod = relay.transform.InferType()(mod)
output = func_4328()
func_4329 = relay.Function([], output)
mutated_mod['func_4329'] = func_4329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2387_call = mod.get_global_var('func_2387')
func_2389_call = mutated_mod.get_global_var('func_2389')
call_4348 = func_2387_call()
call_4349 = func_2387_call()
func_3620_call = mod.get_global_var('func_3620')
func_3621_call = mutated_mod.get_global_var('func_3621')
call_4362 = func_3620_call()
call_4363 = func_3620_call()
output = relay.Tuple([call_4348,call_4362,])
output2 = relay.Tuple([call_4349,call_4363,])
func_4374 = relay.Function([], output)
mod['func_4374'] = func_4374
mod = relay.transform.InferType()(mod)
mutated_mod['func_4374'] = func_4374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4375 = func_4374_call()
output = call_4375
func_4376 = relay.Function([], output)
mutated_mod['func_4376'] = func_4376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_4386 = relay.TupleGetItem(func_353_call(), 2)
call_4387 = relay.TupleGetItem(func_355_call(), 2)
func_3620_call = mod.get_global_var('func_3620')
func_3621_call = mutated_mod.get_global_var('func_3621')
call_4390 = func_3620_call()
call_4391 = func_3620_call()
func_1622_call = mod.get_global_var('func_1622')
func_1623_call = mutated_mod.get_global_var('func_1623')
call_4392 = func_1622_call()
call_4393 = func_1622_call()
output = relay.Tuple([call_4386,call_4390,call_4392,])
output2 = relay.Tuple([call_4387,call_4391,call_4393,])
func_4399 = relay.Function([], output)
mod['func_4399'] = func_4399
mod = relay.transform.InferType()(mod)
output = func_4399()
func_4400 = relay.Function([], output)
mutated_mod['func_4400'] = func_4400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3800_call = mod.get_global_var('func_3800')
func_3802_call = mutated_mod.get_global_var('func_3802')
call_4401 = relay.TupleGetItem(func_3800_call(), 1)
call_4402 = relay.TupleGetItem(func_3802_call(), 1)
output = call_4401
output2 = call_4402
func_4426 = relay.Function([], output)
mod['func_4426'] = func_4426
mod = relay.transform.InferType()(mod)
output = func_4426()
func_4427 = relay.Function([], output)
mutated_mod['func_4427'] = func_4427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_4460 = func_108_call()
call_4461 = func_108_call()
output = relay.Tuple([call_4460,])
output2 = relay.Tuple([call_4461,])
func_4493 = relay.Function([], output)
mod['func_4493'] = func_4493
mod = relay.transform.InferType()(mod)
output = func_4493()
func_4494 = relay.Function([], output)
mutated_mod['func_4494'] = func_4494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2785_call = mod.get_global_var('func_2785')
func_2787_call = mutated_mod.get_global_var('func_2787')
call_4517 = relay.TupleGetItem(func_2785_call(), 0)
call_4518 = relay.TupleGetItem(func_2787_call(), 0)
output = relay.Tuple([call_4517,])
output2 = relay.Tuple([call_4518,])
func_4521 = relay.Function([], output)
mod['func_4521'] = func_4521
mod = relay.transform.InferType()(mod)
output = func_4521()
func_4522 = relay.Function([], output)
mutated_mod['func_4522'] = func_4522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
call_4528 = relay.TupleGetItem(func_720_call(), 0)
call_4529 = relay.TupleGetItem(func_722_call(), 0)
output = relay.Tuple([call_4528,])
output2 = relay.Tuple([call_4529,])
func_4538 = relay.Function([], output)
mod['func_4538'] = func_4538
mod = relay.transform.InferType()(mod)
output = func_4538()
func_4539 = relay.Function([], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_4562 = relay.TupleGetItem(func_49_call(), 0)
call_4563 = relay.TupleGetItem(func_50_call(), 0)
func_2609_call = mod.get_global_var('func_2609')
func_2610_call = mutated_mod.get_global_var('func_2610')
call_4570 = relay.TupleGetItem(func_2609_call(), 0)
call_4571 = relay.TupleGetItem(func_2610_call(), 0)
func_4156_call = mod.get_global_var('func_4156')
func_4158_call = mutated_mod.get_global_var('func_4158')
call_4585 = relay.TupleGetItem(func_4156_call(), 0)
call_4586 = relay.TupleGetItem(func_4158_call(), 0)
output = relay.Tuple([call_4562,call_4570,call_4585,])
output2 = relay.Tuple([call_4563,call_4571,call_4586,])
func_4607 = relay.Function([], output)
mod['func_4607'] = func_4607
mod = relay.transform.InferType()(mod)
mutated_mod['func_4607'] = func_4607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4607_call = mutated_mod.get_global_var('func_4607')
call_4608 = func_4607_call()
output = call_4608
func_4609 = relay.Function([], output)
mutated_mod['func_4609'] = func_4609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3409_call = mod.get_global_var('func_3409')
func_3411_call = mutated_mod.get_global_var('func_3411')
call_4648 = func_3409_call()
call_4649 = func_3409_call()
func_2112_call = mod.get_global_var('func_2112')
func_2116_call = mutated_mod.get_global_var('func_2116')
var_4686 = relay.var("var_4686", dtype = "uint8", shape = (84, 20))#candidate|4686|(84, 20)|var|uint8
var_4687 = relay.var("var_4687", dtype = "uint8", shape = ())#candidate|4687|()|var|uint8
call_4685 = relay.TupleGetItem(func_2112_call(relay.reshape(var_4686.astype('uint8'), [14, 12, 10]), relay.reshape(var_4686.astype('uint8'), [14, 12, 10]), relay.reshape(var_4687.astype('uint8'), []), ), 3)
call_4688 = relay.TupleGetItem(func_2116_call(relay.reshape(var_4686.astype('uint8'), [14, 12, 10]), relay.reshape(var_4686.astype('uint8'), [14, 12, 10]), relay.reshape(var_4687.astype('uint8'), []), ), 3)
bop_4692 = relay.right_shift(call_4685.astype('int16'), relay.reshape(var_4686.astype('int16'), relay.shape_of(call_4685))) # shape=(14, 12, 10)
bop_4695 = relay.right_shift(call_4688.astype('int16'), relay.reshape(var_4686.astype('int16'), relay.shape_of(call_4688))) # shape=(14, 12, 10)
func_2439_call = mod.get_global_var('func_2439')
func_2441_call = mutated_mod.get_global_var('func_2441')
call_4696 = func_2439_call()
call_4697 = func_2439_call()
bop_4705 = relay.add(var_4686.astype('int16'), var_4687.astype('int16')) # shape=(84, 20)
output = relay.Tuple([call_4648,bop_4692,call_4696,bop_4705,])
output2 = relay.Tuple([call_4649,bop_4695,call_4697,bop_4705,])
func_4712 = relay.Function([var_4686,var_4687,], output)
mod['func_4712'] = func_4712
mod = relay.transform.InferType()(mod)
mutated_mod['func_4712'] = func_4712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4712_call = mutated_mod.get_global_var('func_4712')
var_4714 = relay.var("var_4714", dtype = "uint8", shape = (84, 20))#candidate|4714|(84, 20)|var|uint8
var_4715 = relay.var("var_4715", dtype = "uint8", shape = ())#candidate|4715|()|var|uint8
call_4713 = func_4712_call(var_4714,var_4715,)
output = call_4713
func_4716 = relay.Function([var_4714,var_4715,], output)
mutated_mod['func_4716'] = func_4716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4718 = relay.var("var_4718", dtype = "int32", shape = ())#candidate|4718|()|var|int32
var_4719 = relay.var("var_4719", dtype = "int32", shape = (9, 14, 1))#candidate|4719|(9, 14, 1)|var|int32
bop_4720 = relay.greater(var_4718.astype('bool'), var_4719.astype('bool')) # shape=(9, 14, 1)
output = bop_4720
output2 = bop_4720
func_4731 = relay.Function([var_4718,var_4719,], output)
mod['func_4731'] = func_4731
mod = relay.transform.InferType()(mod)
mutated_mod['func_4731'] = func_4731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4731_call = mutated_mod.get_global_var('func_4731')
var_4733 = relay.var("var_4733", dtype = "int32", shape = ())#candidate|4733|()|var|int32
var_4734 = relay.var("var_4734", dtype = "int32", shape = (9, 14, 1))#candidate|4734|(9, 14, 1)|var|int32
call_4732 = func_4731_call(var_4733,var_4734,)
output = call_4732
func_4735 = relay.Function([var_4733,var_4734,], output)
mutated_mod['func_4735'] = func_4735
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4744 = relay.const([[[2.497082,9.611929],[-7.890669,8.348183],[1.581487,7.581396],[1.556443,-5.221475],[3.598819,3.593524],[-4.452913,-9.519587],[9.376657,-0.249804],[2.128593,0.946248],[-1.292328,0.369720],[-9.588251,-5.104387],[9.207958,-3.652362]],[[0.886335,3.008009],[-2.758385,1.764622],[-8.569618,-3.054731],[-7.209636,-8.906968],[-4.819065,-6.794759],[-7.189132,5.000411],[-4.889516,5.190040],[8.774210,-0.660593],[-3.356536,6.656577],[-4.501377,1.306010],[5.973299,7.863855]],[[-3.536023,4.712978],[4.851531,8.142173],[3.701278,3.766521],[-7.280964,7.395430],[-0.247059,-7.288285],[8.334369,3.277170],[3.345069,8.160084],[-2.450041,-6.546659],[-4.824044,9.924780],[6.534436,4.039843],[-4.093994,7.616306]],[[2.806725,-8.026056],[-3.150969,-5.203282],[9.663587,-0.809132],[-6.082376,1.630993],[-2.346514,-2.701940],[7.202063,-4.755060],[-7.112299,1.365358],[-7.090980,-9.765302],[8.251082,-2.901589],[8.985764,-1.460509],[-3.640936,5.310493]],[[-4.335011,-7.036539],[-1.416081,8.952655],[-5.821918,3.420678],[5.931569,6.605699],[3.238904,-8.049266],[6.057195,-0.398414],[0.335152,8.435157],[0.977516,7.995770],[9.940248,-5.967887],[-6.986750,0.920945],[-6.835085,0.007654]],[[1.937712,2.078501],[-5.432447,6.235087],[-8.648659,8.806437],[-3.594593,-0.254479],[7.099364,4.926634],[8.239139,8.638088],[7.885068,-2.007052],[8.654520,-6.876129],[6.731159,5.830030],[1.401436,6.907522],[-7.333662,5.721494]],[[4.119358,9.049786],[5.118673,4.381449],[-7.207584,-3.603442],[1.248059,5.875432],[4.048679,2.714924],[-8.513905,-3.466133],[1.247652,6.440526],[-6.634579,2.452555],[-4.368774,7.623413],[8.408909,-8.306861],[6.642192,-4.459088]],[[-6.711835,8.027980],[7.671254,-8.401866],[9.938690,8.710969],[-7.559164,-8.169209],[8.160935,-7.017764],[-2.711044,-4.687092],[-5.075095,-7.938801],[9.385536,-5.706274],[-7.266726,2.841409],[-5.062206,6.446865],[9.363858,-1.969491]],[[-1.731581,-3.699462],[-6.776897,5.922773],[-6.960039,9.029722],[3.042386,-2.188710],[-8.775741,-5.986050],[-1.847137,-9.489866],[7.612458,-0.237148],[-7.220727,-9.969491],[-6.068801,-0.569783],[6.830766,5.058481],[3.057521,-9.792838]]], dtype = "float64")#candidate|4744|(9, 11, 2)|const|float64
uop_4745 = relay.atan(const_4744.astype('float64')) # shape=(9, 11, 2)
output = uop_4745
output2 = uop_4745
func_4747 = relay.Function([], output)
mod['func_4747'] = func_4747
mod = relay.transform.InferType()(mod)
output = func_4747()
func_4748 = relay.Function([], output)
mutated_mod['func_4748'] = func_4748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_4754 = relay.TupleGetItem(func_2751_call(), 0)
call_4755 = relay.TupleGetItem(func_2753_call(), 0)
output = relay.Tuple([call_4754,])
output2 = relay.Tuple([call_4755,])
func_4774 = relay.Function([], output)
mod['func_4774'] = func_4774
mod = relay.transform.InferType()(mod)
mutated_mod['func_4774'] = func_4774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mutated_mod.get_global_var('func_4774')
call_4775 = func_4774_call()
output = call_4775
func_4776 = relay.Function([], output)
mutated_mod['func_4776'] = func_4776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3608_call = mod.get_global_var('func_3608')
func_3610_call = mutated_mod.get_global_var('func_3610')
call_4850 = func_3608_call()
call_4851 = func_3608_call()
output = relay.Tuple([call_4850,])
output2 = relay.Tuple([call_4851,])
func_4854 = relay.Function([], output)
mod['func_4854'] = func_4854
mod = relay.transform.InferType()(mod)
mutated_mod['func_4854'] = func_4854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4854_call = mutated_mod.get_global_var('func_4854')
call_4855 = func_4854_call()
output = call_4855
func_4856 = relay.Function([], output)
mutated_mod['func_4856'] = func_4856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4493_call = mod.get_global_var('func_4493')
func_4494_call = mutated_mod.get_global_var('func_4494')
call_4877 = relay.TupleGetItem(func_4493_call(), 0)
call_4878 = relay.TupleGetItem(func_4494_call(), 0)
var_4886 = relay.var("var_4886", dtype = "uint8", shape = (8, 13, 16))#candidate|4886|(8, 13, 16)|var|uint8
bop_4887 = relay.mod(call_4877.astype('float64'), relay.reshape(var_4886.astype('float64'), relay.shape_of(call_4877))) # shape=(8, 13, 16)
bop_4890 = relay.mod(call_4878.astype('float64'), relay.reshape(var_4886.astype('float64'), relay.shape_of(call_4878))) # shape=(8, 13, 16)
output = relay.Tuple([bop_4887,])
output2 = relay.Tuple([bop_4890,])
func_4899 = relay.Function([var_4886,], output)
mod['func_4899'] = func_4899
mod = relay.transform.InferType()(mod)
mutated_mod['func_4899'] = func_4899
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4900 = relay.var("var_4900", dtype = "uint8", shape = (8, 13, 16))#candidate|4900|(8, 13, 16)|var|uint8
func_4899_call = mutated_mod.get_global_var('func_4899')
call_4901 = func_4899_call(var_4900)
output = call_4901
func_4902 = relay.Function([var_4900], output)
mutated_mod['func_4902'] = func_4902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_4982 = relay.TupleGetItem(func_2751_call(), 1)
call_4983 = relay.TupleGetItem(func_2753_call(), 1)
output = relay.Tuple([call_4982,])
output2 = relay.Tuple([call_4983,])
func_4984 = relay.Function([], output)
mod['func_4984'] = func_4984
mod = relay.transform.InferType()(mod)
output = func_4984()
func_4985 = relay.Function([], output)
mutated_mod['func_4985'] = func_4985
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5001 = relay.const([[[6,2,1,10,-10,10,-6,-4,-10,-8,8,-2,2,-9,3,-4],[9,2,-7,5,-1,-5,-5,-1,-4,10,2,-4,9,-3,-3,3],[10,3,10,-7,3,7,10,3,-8,-10,4,5,9,6,-4,5]],[[6,3,6,-6,-3,4,-10,-1,-9,1,7,7,-5,-10,-3,2],[3,-5,9,-7,-4,-8,-8,-5,10,-10,-5,4,9,-8,9,2],[-7,-2,-10,-9,-9,-1,5,-6,3,3,5,7,-1,8,4,3]],[[-9,-10,-3,-3,5,1,-9,7,3,9,5,-1,10,-6,9,10],[6,7,10,-4,-4,-6,-10,-5,3,8,-2,6,-8,8,4,3],[9,-1,-10,3,10,6,-2,-4,9,-5,-2,-2,-5,-6,-2,1]],[[1,-10,9,-4,5,-2,5,2,-9,-4,9,-9,-10,-3,6,-4],[8,-7,-9,9,-4,-9,-8,-2,1,5,-2,2,3,-4,1,-7],[4,-7,8,-5,6,1,8,-10,9,-6,-2,-5,-6,-6,-9,-6]],[[-7,-3,9,-7,-3,-9,-2,-9,4,4,-6,3,-9,8,1,10],[7,5,3,-10,-10,9,-10,5,-4,2,-9,1,-5,6,3,6],[-1,-5,-10,-3,6,2,-8,9,-5,1,7,2,1,8,3,-3]],[[2,9,2,4,-3,3,-3,-3,-3,-2,6,-2,3,-10,-3,-3],[10,-9,-5,10,9,-9,-8,-3,-9,-3,1,4,7,-2,-5,-9],[8,-7,1,1,3,-4,-4,-3,-4,-2,4,-10,-7,5,-7,9]],[[2,-8,-5,5,-1,-10,8,2,2,8,9,8,10,10,-8,5],[-4,3,6,-7,10,5,-3,-1,-10,-10,9,-7,-1,-8,-5,-9],[10,8,3,-2,-5,3,4,10,5,5,7,-4,-8,-7,7,-3]],[[7,2,9,3,3,-9,-9,2,-8,-9,10,5,-8,-2,8,4],[7,5,2,-9,3,-3,-6,6,4,2,9,-4,10,1,-3,3],[-3,-5,6,3,1,-2,2,4,-5,2,4,2,5,-1,-10,-8]],[[5,-9,9,-2,7,9,4,-7,-10,5,-6,7,2,-10,4,-7],[-3,-2,8,5,10,7,9,-4,-5,-2,-8,4,7,-2,4,-10],[8,1,9,-5,2,-2,-8,-10,7,-5,1,3,-5,-8,8,6]],[[-3,-4,-3,-1,1,-7,-10,-1,1,2,-7,-9,-1,9,-9,5],[-2,-4,8,-9,7,-7,5,5,-3,-7,1,-3,4,-4,-7,-5],[-10,5,2,-6,-1,7,-8,-9,1,-3,1,7,-8,-8,-9,-7]],[[2,6,5,3,4,10,-6,5,5,8,-6,1,5,10,-4,5],[-6,-8,-5,-6,4,-1,5,6,5,-7,-8,-6,10,8,-2,8],[8,-10,-10,1,2,-2,9,-8,3,-7,4,5,9,7,-10,1]],[[4,8,8,6,1,-9,-8,-7,2,2,-5,-9,-2,-6,-3,8],[-8,9,-8,-8,-5,-9,3,3,-10,-1,-4,1,-7,8,-4,7],[-7,-10,3,3,-6,-2,10,4,2,5,6,-4,3,-10,2,-10]]], dtype = "int16")#candidate|5001|(12, 3, 16)|const|int16
var_5002 = relay.var("var_5002", dtype = "int16", shape = (12, 3, 16))#candidate|5002|(12, 3, 16)|var|int16
bop_5003 = relay.logical_xor(const_5001.astype('int16'), relay.reshape(var_5002.astype('int16'), relay.shape_of(const_5001))) # shape=(12, 3, 16)
bop_5011 = relay.minimum(const_5001.astype('uint16'), relay.reshape(bop_5003.astype('uint16'), relay.shape_of(const_5001))) # shape=(12, 3, 16)
uop_5021 = relay.asin(bop_5011.astype('float64')) # shape=(12, 3, 16)
output = relay.Tuple([uop_5021,])
output2 = relay.Tuple([uop_5021,])
func_5023 = relay.Function([var_5002,], output)
mod['func_5023'] = func_5023
mod = relay.transform.InferType()(mod)
mutated_mod['func_5023'] = func_5023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5024 = relay.var("var_5024", dtype = "int16", shape = (12, 3, 16))#candidate|5024|(12, 3, 16)|var|int16
func_5023_call = mutated_mod.get_global_var('func_5023')
call_5025 = func_5023_call(var_5024)
output = call_5025
func_5026 = relay.Function([var_5024], output)
mutated_mod['func_5026'] = func_5026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_5034 = relay.TupleGetItem(func_4774_call(), 0)
call_5035 = relay.TupleGetItem(func_4776_call(), 0)
func_578_call = mod.get_global_var('func_578')
func_581_call = mutated_mod.get_global_var('func_581')
const_5084 = relay.const([8,8,-6,-9,1,-7,-5,-5,-4,2,9,7,-10,10,-4,9,-6,-10,-4,-9,4,7,6,-8,-10,2,-10,3,-7,-5,8,3,-5,-10,-3,-3,3,-8,-3,3,-9,-3,3,-10,-8,3,1,4,10,-4,-3,4,6,-6,8,-2,-4,7,-2,-10,-2,-10,3,-8,10,-8,8,8,3,4,-5,10,3,9,-4,8,3,8,4,9,-5,-6,10,-6,-9,-6,-9,4,-4,9,-1,4,7,-10,-6,-4,7,-6,5,9,4,-8,2,5,2,-3,-3,7,-7,-10,9,5,-5,4,-5,-5,8,2,-3,5,-2,-10,-5,4,7,6,9,3,-4,-5,-10,8,4,-10,-10,4,-3,-9,-3,-2,-9,8,10,4,-6,5,-1,-6,4,2,10,7,2,4,1,8,2,1,-7,8,-6,-1,-5,-2,4,-6,-1,10,1,1,-7,5,6,5,-1,-7,5,5,-7,-2,10,5,-1,5,6,7,6,7,5,5,5,6,10,-4,6,-7,-6,-8,-5,10,-10,7,8,-9,-5,3,-8,4,8,-6,5,-1,-6,-9,-3,-4,-7,-10,-6,10,-5,3,-9,3,6,2,-3,-4,3,9,4,10,6,-8,10,4,-8,1,6,5,-3,5,3,4,3,-3,-7,-2,-2,5,-8,-9,6,6,-4,-5,-9,1,-10,-7,8,-3,2,8,-4,5,-2,10,4,3,6,-5,8,6,-2,-2,4,5,-9,-1,-10,6,-3,-1,2,-5,3,3,7,-9,6,-7,-7,8,9,-10,8,-10,-4,-9,6,3,5,1,7,9,3,4,2,5,-3,-10,-3,-3,-3,3,8,1,6,-3,3,-6,2,6,4,-5,8,-10,-8,-10,-5,2,-3,-5,6,9,4,6,7,-9,-5,8,2,6,10,10,-1,9,5,10,-5,-1,-8,4,10,6,2,1,-3,5,-5,1,9,-9,-5,6,-1,1,-5,-3,-2,2,-5,7,2,-3,7,2], dtype = "uint64")#candidate|5084|(378,)|const|uint64
call_5083 = relay.TupleGetItem(func_578_call(relay.reshape(const_5084.astype('uint64'), [378,])), 3)
call_5085 = relay.TupleGetItem(func_581_call(relay.reshape(const_5084.astype('uint64'), [378,])), 3)
output = relay.Tuple([call_5034,call_5083,const_5084,])
output2 = relay.Tuple([call_5035,call_5085,const_5084,])
func_5093 = relay.Function([], output)
mod['func_5093'] = func_5093
mod = relay.transform.InferType()(mod)
output = func_5093()
func_5094 = relay.Function([], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4493_call = mod.get_global_var('func_4493')
func_4494_call = mutated_mod.get_global_var('func_4494')
call_5107 = relay.TupleGetItem(func_4493_call(), 0)
call_5108 = relay.TupleGetItem(func_4494_call(), 0)
func_5093_call = mod.get_global_var('func_5093')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_5114 = relay.TupleGetItem(func_5093_call(), 2)
call_5115 = relay.TupleGetItem(func_5094_call(), 2)
output = relay.Tuple([call_5107,call_5114,])
output2 = relay.Tuple([call_5108,call_5115,])
func_5138 = relay.Function([], output)
mod['func_5138'] = func_5138
mod = relay.transform.InferType()(mod)
mutated_mod['func_5138'] = func_5138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5138_call = mutated_mod.get_global_var('func_5138')
call_5139 = func_5138_call()
output = call_5139
func_5140 = relay.Function([], output)
mutated_mod['func_5140'] = func_5140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_5158 = relay.TupleGetItem(func_2201_call(), 0)
call_5159 = relay.TupleGetItem(func_2203_call(), 0)
output = relay.Tuple([call_5158,])
output2 = relay.Tuple([call_5159,])
func_5167 = relay.Function([], output)
mod['func_5167'] = func_5167
mod = relay.transform.InferType()(mod)
output = func_5167()
func_5168 = relay.Function([], output)
mutated_mod['func_5168'] = func_5168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3728_call = mod.get_global_var('func_3728')
func_3729_call = mutated_mod.get_global_var('func_3729')
call_5204 = relay.TupleGetItem(func_3728_call(), 1)
call_5205 = relay.TupleGetItem(func_3729_call(), 1)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_5206 = relay.TupleGetItem(func_2523_call(), 0)
call_5207 = relay.TupleGetItem(func_2525_call(), 0)
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_5215 = relay.TupleGetItem(func_2377_call(relay.reshape(call_5206.astype('uint8'), [8, 13, 16])), 0)
call_5216 = relay.TupleGetItem(func_2379_call(relay.reshape(call_5206.astype('uint8'), [8, 13, 16])), 0)
func_1107_call = mod.get_global_var('func_1107')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_5222 = relay.TupleGetItem(func_1107_call(), 1)
call_5223 = relay.TupleGetItem(func_1109_call(), 1)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_5239 = relay.TupleGetItem(func_3136_call(), 2)
call_5240 = relay.TupleGetItem(func_3138_call(), 2)
output = relay.Tuple([call_5204,call_5206,call_5215,call_5222,call_5239,])
output2 = relay.Tuple([call_5205,call_5207,call_5216,call_5223,call_5240,])
func_5243 = relay.Function([], output)
mod['func_5243'] = func_5243
mod = relay.transform.InferType()(mod)
output = func_5243()
func_5244 = relay.Function([], output)
mutated_mod['func_5244'] = func_5244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5167_call = mod.get_global_var('func_5167')
func_5168_call = mutated_mod.get_global_var('func_5168')
call_5357 = relay.TupleGetItem(func_5167_call(), 0)
call_5358 = relay.TupleGetItem(func_5168_call(), 0)
output = relay.Tuple([call_5357,])
output2 = relay.Tuple([call_5358,])
func_5363 = relay.Function([], output)
mod['func_5363'] = func_5363
mod = relay.transform.InferType()(mod)
mutated_mod['func_5363'] = func_5363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5363_call = mutated_mod.get_global_var('func_5363')
call_5364 = func_5363_call()
output = call_5364
func_5365 = relay.Function([], output)
mutated_mod['func_5365'] = func_5365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4747_call = mod.get_global_var('func_4747')
func_4748_call = mutated_mod.get_global_var('func_4748')
call_5369 = func_4747_call()
call_5370 = func_4747_call()
var_5380 = relay.var("var_5380", dtype = "float64", shape = (9, 11, 2))#candidate|5380|(9, 11, 2)|var|float64
bop_5381 = relay.multiply(call_5369.astype('int16'), relay.reshape(var_5380.astype('int16'), relay.shape_of(call_5369))) # shape=(9, 11, 2)
bop_5384 = relay.multiply(call_5370.astype('int16'), relay.reshape(var_5380.astype('int16'), relay.shape_of(call_5370))) # shape=(9, 11, 2)
output = bop_5381
output2 = bop_5384
func_5410 = relay.Function([var_5380,], output)
mod['func_5410'] = func_5410
mod = relay.transform.InferType()(mod)
var_5411 = relay.var("var_5411", dtype = "float64", shape = (9, 11, 2))#candidate|5411|(9, 11, 2)|var|float64
output = func_5410(var_5411)
func_5412 = relay.Function([var_5411], output)
mutated_mod['func_5412'] = func_5412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_5428 = relay.TupleGetItem(func_2523_call(), 0)
call_5429 = relay.TupleGetItem(func_2525_call(), 0)
func_2112_call = mod.get_global_var('func_2112')
func_2116_call = mutated_mod.get_global_var('func_2116')
var_5486 = relay.var("var_5486", dtype = "uint8", shape = (1680,))#candidate|5486|(1680,)|var|uint8
const_5487 = relay.const(7, dtype = "uint8")#candidate|5487|()|const|uint8
call_5485 = relay.TupleGetItem(func_2112_call(relay.reshape(var_5486.astype('uint8'), [14, 12, 10]), relay.reshape(var_5486.astype('uint8'), [14, 12, 10]), relay.reshape(const_5487.astype('uint8'), []), ), 1)
call_5488 = relay.TupleGetItem(func_2116_call(relay.reshape(var_5486.astype('uint8'), [14, 12, 10]), relay.reshape(var_5486.astype('uint8'), [14, 12, 10]), relay.reshape(const_5487.astype('uint8'), []), ), 1)
output = relay.Tuple([call_5428,call_5485,var_5486,const_5487,])
output2 = relay.Tuple([call_5429,call_5488,var_5486,const_5487,])
func_5495 = relay.Function([var_5486,], output)
mod['func_5495'] = func_5495
mod = relay.transform.InferType()(mod)
var_5496 = relay.var("var_5496", dtype = "uint8", shape = (1680,))#candidate|5496|(1680,)|var|uint8
output = func_5495(var_5496)
func_5497 = relay.Function([var_5496], output)
mutated_mod['func_5497'] = func_5497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1181_call = mod.get_global_var('func_1181')
func_1183_call = mutated_mod.get_global_var('func_1183')
call_5519 = func_1181_call()
call_5520 = func_1181_call()
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
const_5525 = relay.const(9, dtype = "uint8")#candidate|5525|()|const|uint8
const_5526 = relay.const([9,9,4,-2,2,2,-5,-3,-4,-4,-4,-5,-4,2,10,-7,9,10,3,-4,-1,-6,9,-5,-6,1,8,9,-4,5,-4,4,10,9,-7,-10,-9,7,6,8,-10,3,5,-2,-5,-5,-9,4,-3,3,-6,-10,-9,-1,-10,-10,10,-2,7,3,1,3,-9,1,10,3,9,10,-4,-5,-2,7,-8,6,-3,9,7,3,-9,-9,8,-6,7,7,9,-6,-6,-2,3,2,-6,-7,-3,10,-7,-2,1,4,-3,7,-2,4,7,-4,3,4,1,2,-6,-7,-1,9,-6,-10,-3,-5,-10,-5,-5,5,9,5,3,-3,2,-1,10,7,-5,8,-3,-5,10,-10,-10,-2,6,-8,-7,-9,2,5,2,-7,8,6,-8,4,10,-4,-9,-1,4,-6,-2,-9,7,-6,8,7,-1,-7,4,9,-5,8,9,-3,-1,-1,5,9,6,2,-1,9,-4,2,-10,-5,4,-3,3,4,-4,-8,7,-1,-3,8,-2,5,-7,-5,8,4,-1,4,2,9,7,4,-5,8,8,1,6,7,2,10,9,-3,2,8,9,1,7,9,-2,9,6,-3,3,-6,1,-7,2,3,-9,-10,-8,-4,8,-6,-10,-2,4,-9,-5,-4,-10,7,2,8,10,-10,6,-5,7,5,-6,-4,-2,7,-9,-6,-3,3,-4,7,-6,4,10,6,-1,-5,-10,9,-3,1,-9,-2,-9,-8,-3,-7,-1,-1,-2,-10,-10,2,-5,1,-7,-1,9,-7,-6,1,9,10,-1,-2,-10,6,9,-1,8,4,6,10,-1,-4,-3,8,-3,3,-1,-6,9,-4,-9,5,-9,-5,-6,-10,3,6,7,1,2,1,-2,6,-9,2,-5,7,7,7,-6,-2,9,8,-10,5,4,-7,2,-8,4,-1,6,-1,10,8,-4,-9,-6,10,-8,10,-10,-6,2,5,5,-3,2,6,3,-1,2,-4,7,-4,9,-4,-3,-5,-8,1,4,4,9,9,-4,8,10,-4,-6,-1,6,-7,-8,4,-1,-9,8,-1,3,-8,2,-3,-8,7,-7,2,-4,2,1,9,-10,7,4,-6,1,4,-2,4,-3,-5,-1,-4,7,-10,2,10,-10,4,8,10,4,3,-2,5,9,-8,8,-7,7,-3,9,-3,-2,-2,6,2,-10,7,3,7,-5,-4,8,8,-1,4,-4,-8,5,1,-3,-5,-7,5,6,1,9,-4,9,2,-5,-9,-5,-7,8,-6,-10,-6,-5,4,4,-3,-3,10,3,1,8,6,8,8,3,8,4,8,-4,-1,10,-1,-4,-6,-1,-2,-8,6,4,-3,-7,8,-5,-1,1,-9,-7,-7,-1,6,9,-3,-6,2,-5,5,-5,3,1,3,5,6,-2,3,-3,5,6,-10,9,2,-8,5,-2,-5,4,7,-2,3,6,-7,-4,-3,-2,-3,-7,-4,6,8,10,2,-3,-5,-4,9,2,-10,-8,-7,8,-1,6,7,7,-9,1,2,2,9,6,7,3,6,-10,2,-4,-10,10,-4,3,5,7,-7,7,-7,5,-10,-9,2,1,7,8,-6,7,7,-3,3,2,-1,8,-1,-9,-3,-1,-8,-10,-6,4,-7,1,-2,-6,6,-7,-8,-4,9,-4,-2,7,5,-4,-8,-4,1,8,-2,8,-6,-7,-9,-5,-2,1,4,-3,9,-2,8,-1,1,-2,-8,3,5,-8,10,-3,4,6,5,-9,-9,-9,-6,7,2,2,-10,-1,4,-1,5,-7,-9,-7,4,-7,6,9,-8,9,6,7,-4,-10,10,-3,7,-3,4,-1,5,-1,-5,1,5,-3,-9,6,3,-4,-9,-9,10,3,2,-4,1,6,-4,-1,-6,1,-9,1,-4,6,-3,-10,-4,6,-4,-3,-6,4,5,-10,-4,-8,-9,-4,3,8,4,8,-8,4,-5,-10,-5,10,2,4,-2,-8,1,-5,1,-10,-1,2,5,3,4,-2,10,2,-3,-7,-7,7,6,-2,-7,-3,-3,10,-3,-9,-10,10,2,-9,8,-1,10,5,-3,-4,-1,1,-4,-3,7,5,-4,5,-7,-2,-2,-2,-4,8,-3,-10,-1,-10,3,1,-7,5,-3,9,7,-7,-8,-9,3,10,2,-10,-10,-8,-6,-2,7,-6,2,-10,-1,-7,-5,9,-6,6,8,2,8,2,-9,9,-4,4,-2,-4,-3,-10,-7,-6,10,2,-10,6,4,-4,-2,9,-7,3,-9,-10,6,-1,-1,-8,3,-8,4,-10,4,1,6,6,-3,1,-4,4,-3,6,6,-4,4,9,-10,6,5,-1,-7,2,-4,2,6,-9,-5,-2,9,-7,1,-2,-8,-2,8,-4,10,5,-1,-3,4,-5,-9,9,4,-10,3,6,10,4,3,3,6,-7,-6,1,2,-1,4,8,8,-2,10,4,-6,-10,-8,2,10,10,-10,9,8,3,-10,9,9,-10,-9,-8,5,-6,10,9,-7,-9,-10,9,6,10,-2,-5,2,1,2,-8,9,1,2,-1,-9,-6,-7,-8,8,3,9,-3,5,-2,-3,-5,-6,2,-8,-9,-3,7,9,-5,5,6,-7,-5,-3,1,-1,8,5,-5,5,10,-8,-8,-2,5,2,-3,2,-3,-9,1,-3,7,-1,8,8,-3,-5,-5,-7,-6,2,10,-1,7,7,10,-8,-5,3,4,3,8,-8,5,-3,-4,2,9,7,3,-5,-6,-2,-4,6,6,5,7,7,1,-1,-7,1,6,3,3,-2,2,2,1,-4,-9,-1,4,-6,-9,10,-2,1,8,-7,1,2,7,9,-5,-5,2,9,-5,1,-6,2,-1,-7,-7,1,-6,-1,-10,3,3,-8,-5,1,5,-7,-2,-8,2,-1,10,4,7,-10,-6,-10,2,-6,-6,8,10,2,-4,4,-8,2,-8,-5,-4,2,10,10,2,1,-4,1,6,-5,-6,4,-5,3,5,-6,6,10,10,10,-6,9,-1,4,-4,10,10,-7,2,-6,-9,-7,-10,1,-7,-1,-3,2,1,-3,-5,-6,-9,-9,2,-10,-8,5,2,-10,-8,-1,-1,7,1,8,5,2,-6,4,4,2,9,-2,5,1,2,6,-8,-7,5,4,9,1,-5,-5,9,3,-7,10,-6,7,4,1,-6,-9,-2,-10,-1,6,6,-6,-3,4,3,-1,-4,5,4,9,6,3,-3,9,-4,1,-10,-8,4,-2,3,-4,-6,6,-8,-1,3,10,-7,-3,8,4,8,3,-1,9,-10,2,5,-5,-2,-5,2,-4,-8,1,-8,-4,-6,-8,-1,2,3,7,-1,9,1,-8,-3,2,-7,7,-10,2,7,-5,-9,2,-1,8,-3,5,4,7,-8,-7,1,-2,5,7,4,-2,8,-4,5,3,10,-4,-5,-2,-7,10,2,-1,6,1,-1,-4,9,8,-2,3,-10,8,7,8,8,-4,-10,7,4,-7,-3,3,-10,7,3,6,9,9,-2,2,5,-2,2,2,-9,10,-9,-3,4,-3,-10,-10,-10,6,8,-4,3,-9,-7,-2,9,6,3,-8,-9,-3,9,9,4,3,-3,-4,-5,3,3,8,-7,1,4,-8,10,2,-7,-9,6,3,-1,8,-2,-7,8,7,10,5,9,4,7,9,9,-6,-1,6,6,7,-9,-2,-10,2,9,3,-3,7,5,5,-7,-10,-10,2,2,-5,-6,8,8,-5,9,4,4,-1,9,-4,-7,-5,-1,-4,-8,4,7,-9,1,-3,3,2,1,8,-9,6,-7,4,10,10,8,2,-5,-4,7,9,-7,9,4,9,10,-1,8,4,3,8,6,-9,-2,-9,10,-1,9,-6,7,-6,1,-5,-3,1,-3,-9,8,1,-1,-9,10,-8,9,-2,9,7,-7,1,3,6,-10,4,3,7,6,4,7,-5,-8,-7,6,7,8,3,-9,-5,6,-8,-5,-2,3,6,-8,10,-9,2,-3,-1,8,-10,5,-7,-7,9,-10,-2,6,4,-1,1,1,7,2,-5,-4,-7,-4,-1,9,-10,10,1,10,-2,-2,-2,6,-9,7,-1,10,-9,4,5,9,-2,7,-7,-1,-9,3,5,1,2,-7,1,2,-4,-2,-2,4,2,-9,10,9,2,5,5,-3,-5,1,8,6,2,10,-8,9,-6,8,-2,-9,3,4,-9,-5,7,-10,1,-8,-3,8,3,-1,8,8,10,-4,1,-1,7,5,-1,-9,-1,7,7,5,-3,-10,-8,2,-6,-1,6,-9,7,7,9,2,6,5,-5,3,1,-10,10,8,-10,-4,10,-1,5,7,-7,7,-8,-5,7,10,1,-8,4,6,-5,-2,4,-2,-3,-5,5,4,-6,-6,-8,10,6,10,-4,-2,9,-3,-9,-1,3,-5,-2,4,1,-3,-4,-8,-3,-10,7,5,8,-8,-3,1,7,-6,6,-6,-8,6,2,-6,-2,-1,8,4,3,5,3,4,4,8,10,7,-5,-3,8,-3,4,1,9,2,-9,10,4,3,-5,-10,-7,4,1,-10,-5,-1,-4,-2,10,-6,2,-3,1,-6,9,3,2,-9,-3,6,-9,-8,9,-9,-6,10,-3,4,-10,-4,6,-4,-3,5,-9,3,-8,-4,-10,8,8,-2,2,8,-8,-9,-8,-5,4,-6,-9,-5,-7,-3,-2,3,-10,2,2,-2,-2,7,3,-10,9,2,-2,-6,5,-8,-2,-6,7,-4,10,1,6,2,9,-6,8,10,-4,1,-8,4,-1,4,-10,8,4,-2,9,-10,5,-9,-4,3,5,-5,4,-7,-10,4,1,10,3,-6,7,3,1,-7,2,1,5,-2,-5,-3,-10,-7,-8,6,10,-6,-9,-2,-2,3,8,-3,10,-1,4,2,-2,-7,-7,-4,9,7,-10,6,6,7,-3,-9,8,10,8,10,-10,-10,1,5,5,-6,10,8,3,-2,-8,9,-10,7,-10,8,3,-10,-4,-6,8,-4,6,-4,7,-3,-4,-10,3,4,4,5,10,2,10,-2,10,7,-8,-4,5,-10,2,-7,7,10,3,-9,-3,-8,-8,3,6,5,1,9,-9,-8,8,9,5,5,7,3,-4,4,1,4,-9,1,10,-9,8,-1,-3,10,-2,-5,10,10,9,7,-3,-9,-10,6,2,-9,3,7,-2,3,3,-4,8,-8,-8,-8,4,7,10,3,9,4,-6,7,9,4,7,-6,10,3,7,-2,3,-6,-1,6,-5,-1,1,-10,7,4,-2,1,6,-1,-7,5,-2,-2,-2,-2,-9,7,-2,-2,-1,-5,1,-6,-9,-10,-1,6,-8,6,-7,8,-5,7,3,6,-10,-8,6,5,-4,2,2,9,-4,-1,-5,-8,3,8,7,-10,7,-5,6,6,5,-3,6,6,-9,3,-5,4,6,-3,-6,-9,5,-5,4,-8,9,-7,-5,7,1,8,2,-3,4,3,-1,2,-4,4,8,8,-5,-4,-7,6,4,-3,6,7,2,-9,-2,-6,7,6,-3,-5,-9,-1,-4,6,3,-4,-5,-8,-1,-1,-9,1,8,3,10,-2,-9,-7,1,10,-3,2,7,9,8,-3,7,-5,1,-6,8,-2,-10,1,-2,-5,5,-5,7,2,-1,2,-9,5,-5,-1,-9,-9,9,2,10,6,-5,10,4,7,7,5,6,-3,1,5,6,2,-5,7,-4,-3,-6,10,4,-7,-9,-6,4,-8,-5,8,-9,7,7,-9,8,1,-6,-4,-10,-1,7,6,9,10,-8,-5,9,1,7,8,-6,9,-1,10,8,-10,1,6,-1,5,-5,8,-6,3,-1,-9,9,8,-3,-1,2,-5,1,-6,-8,-4,3,8,-3,3,1,2,1,1,-8,6,8,-6,5,-3,-3,7,-9,7,7,5,-3,-1,6,-2,-8,4,-2,-5,2,-1,5,3,6,-7,2,-2,-10,1,6,-10,-2,10,-7,-10,-5,4,-10,7,8,10,5,-3,6,10,-7,-8,-5,2,5,10,4,3,2,-1,-3,8,-4,4,-7,4,7,5,-10,5,-1,-9,-1,-1,2,3,5,-5,4,-9,-6,-9,4,-4,-8,-2,-3,4,-5,5,8,-3,9,4,-9,-8,-7,-7,-8,-7,-9,-7,-2,-6,-7,4,-9,10,7,3,6,-3,6,-6,-3,3,2,6,-3,10,-3,7,1,2,-1,4,-8,-2,6,-1,1,-3,-5,8,9,-10,-4,6,4,3,-7,-5,-3,9,7,10,-5,-4,2,-8,1,5,7,-1,3,8,-9,3,4,-3,2,-2,8,7,9,3,5,7,1,-5,-10,-4,-10,2,1,-6,3,-9,-3,1,4,-3,-1,-3,6,9,-2,6,-10,-5,-8,-3,10,-1,10,4,5,-5,8,1,7,-10,10,1,6,2,-1,-4,9,-4,9,-7,7,-3,1,7,-3,-6,-4,-5,-7,4,-2,-8,6,-3,2,-1,1,4,-9,9,9,-5,4,-1,6,8,-6,2,10,6,5,-1,-3,-6,5,4,-1,-4,8,-6,3,-6,-2,-10,6,-4,-5,-7,9,1,-1,7,6,8,9,10,-10,2,9,-6,-7,-5,-7,-3,8,-2,10,2,5,10,4,7,-10,-5,8,-3,-2,-1,3,-7,7,1,-1,5,-2,9,7,-9,-4,8,-8,8,1,10,3,-6,-9,10,-1,5,2,-9,-9,-7,-7,-6,6,-6,3,-3,-5,9,-8,-3,5,-2,3,7,-4,-6,1,-3,-6,-6,-4,5,7,-3,-4,4,4,6,9,-9,10,-1,7,-8,4,-2,-2,-10,-3,-4,9,6,-3,-1,8,5,-7,-8,4,-7,-9,-9,-8,-10,1,-9,9,4,-2,6,4,7,-10,6,-3,2,-2,3,-9,-4,-4,-9,-10,6,-7,-1,4,2,5,7,9,-9,10,2,4,8,-10,-2,-1,4,1,-8,-3,8,-8,-5,-4,-7,-6,-2,6,-10,-8,-7,-3,6,6,8,4,-9,-10,-7,-9,-9,-7,5,10,8,-8,-8,5,4,5,1,1,-2,-4,-7,5,-8,-4,6,10,3,-8,-8,4,2,-7,1,-3,-9,1,-10,10,1,-4,-2,-8,2,-8,8,-6,3,3,1,6,3,-6,6,-2,1,-1,-10,-8,6,7,-7,-4,6,4,-5,7,-10,10,8,10,-2,2,3,-6,-5,-4,-6,5,-8,-7,-9,-1,-7,4,7,-5,-8,-10,-9,1,1,-8,-6,9,2,-8,-2,10,2,-5,10,9,-8,-7,7,-1,-3,-7,2,2,-4,2,1,-3,8,3,7,3,1,2,-10,-8,2,2,1,-5,-6,1,3,-2,4,-6,-7,8,-1,-6,3,-3,-9,-8,-1,-7,2,-6,-4,5,-4,-2,-1,9,-3,6,10,3,-6,-2,-6,8,9,-4,-2,2,9,9,6,-6,4,5,1,5,-10,6,8,-3,-8,1,-5,8,-8,-8,6,1,5,-5,-3,4,9,-9,-6,3,1,-3,-8,-2,9,-9,1,-8,8,-3,-6,-6,10,4,-10,-7,-3,-9,3,-7,9,-9,8,9,1,-10,-2,1,-4,8,-2,-6,5,-5,-7,1,10,8,-7,5,2,2,4,6,10,1,-8,8,2,-4,-8,7,-4,6,-4,9,6,2,7,-7,1,-3,-7,-4,6,10,-4,-2,1,-10,-10,-1,-2,-8,2,-8,-3,3,1,1,-7,3,-7,2,4,-3,2,-1,-8,3,-4,2,-1,-9,6,10,-2,-7,-8,7,10,6,-5,-6,6,2,10,7,-10,-4,6,-10,-6,7,5,-6,3,8,-1,-8,4,6,5,7,-10,2,2,-6,8,-4,9,-9,-4,-8,-1,-1,-10,3,8,1,-9,-6,4,1,7,-6,-5,-9,-1,-3,7,9,1,-1,2,-9,-2,1,-10,9,-8,-4,-7,6,-1,-2,5,4,-5,-6,-6,5,-1,5,1,-9,-6,-5,-9,4,-2,-8,10,-2,8,2,-5,1,5,7,9,-6,2,-9,4,9,-10,2,1,-4,4,-1,3,4,10,-4,9,4,-3,10,-6,5,8,-5,5,-7,3,7,2,4,5,10,9,-7,9,-2,-8,3,6,6,9,-10,1,-8,3,4,-1,-3,-10,-3,-8,8,-3,6,10,3,-5,-2,2,-9,4,-2,2,5,6,5,-4,3,-3,-9,9,10,4,-2,4,1,7,-2,9,-2,-7,2,-7,1,2,-3,-3,-6,-5,-5,-10,-8,10,-7,-9,-7,-6,-8,-1,-5,10,-5,10,-1,-10,5,-3,-8,-5,3,5,-8,8,-6,-4,4,-10,6], dtype = "uint8")#candidate|5526|(3120,)|const|uint8
call_5524 = relay.TupleGetItem(func_813_call(relay.reshape(const_5525.astype('uint8'), []), relay.reshape(const_5526.astype('uint8'), [15, 16, 13]), ), 0)
call_5527 = relay.TupleGetItem(func_816_call(relay.reshape(const_5525.astype('uint8'), []), relay.reshape(const_5526.astype('uint8'), [15, 16, 13]), ), 0)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
call_5538 = relay.TupleGetItem(func_720_call(), 0)
call_5539 = relay.TupleGetItem(func_722_call(), 0)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_5542 = relay.TupleGetItem(func_635_call(), 0)
call_5543 = relay.TupleGetItem(func_636_call(), 0)
func_3471_call = mod.get_global_var('func_3471')
func_3474_call = mutated_mod.get_global_var('func_3474')
call_5555 = func_3471_call(relay.reshape(call_5542.astype('int64'), [8, 13, 16]))
call_5556 = func_3471_call(relay.reshape(call_5542.astype('int64'), [8, 13, 16]))
output = relay.Tuple([call_5519,call_5524,const_5525,const_5526,call_5538,call_5542,call_5555,])
output2 = relay.Tuple([call_5520,call_5527,const_5525,const_5526,call_5539,call_5543,call_5556,])
func_5571 = relay.Function([], output)
mod['func_5571'] = func_5571
mod = relay.transform.InferType()(mod)
mutated_mod['func_5571'] = func_5571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5571_call = mutated_mod.get_global_var('func_5571')
call_5572 = func_5571_call()
output = call_5572
func_5573 = relay.Function([], output)
mutated_mod['func_5573'] = func_5573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_5584 = relay.TupleGetItem(func_2016_call(), 0)
call_5585 = relay.TupleGetItem(func_2017_call(), 0)
func_4258_call = mod.get_global_var('func_4258')
func_4261_call = mutated_mod.get_global_var('func_4261')
var_5594 = relay.var("var_5594", dtype = "float64", shape = (6, 28))#candidate|5594|(6, 28)|var|float64
var_5595 = relay.var("var_5595", dtype = "uint8", shape = (1680,))#candidate|5595|(1680,)|var|uint8
call_5593 = relay.TupleGetItem(func_4258_call(relay.reshape(var_5594.astype('float64'), [168,]), relay.reshape(var_5595.astype('uint8'), [14, 12, 10]), ), 1)
call_5596 = relay.TupleGetItem(func_4261_call(relay.reshape(var_5594.astype('float64'), [168,]), relay.reshape(var_5595.astype('uint8'), [14, 12, 10]), ), 1)
var_5631 = relay.var("var_5631", dtype = "float64", shape = (6, 28))#candidate|5631|(6, 28)|var|float64
bop_5632 = relay.minimum(var_5594.astype('float32'), relay.reshape(var_5631.astype('float32'), relay.shape_of(var_5594))) # shape=(6, 28)
output = relay.Tuple([call_5584,call_5593,var_5595,bop_5632,])
output2 = relay.Tuple([call_5585,call_5596,var_5595,bop_5632,])
func_5638 = relay.Function([var_5594,var_5595,var_5631,], output)
mod['func_5638'] = func_5638
mod = relay.transform.InferType()(mod)
var_5639 = relay.var("var_5639", dtype = "float64", shape = (6, 28))#candidate|5639|(6, 28)|var|float64
var_5640 = relay.var("var_5640", dtype = "uint8", shape = (1680,))#candidate|5640|(1680,)|var|uint8
var_5641 = relay.var("var_5641", dtype = "float64", shape = (6, 28))#candidate|5641|(6, 28)|var|float64
output = func_5638(var_5639,var_5640,var_5641,)
func_5642 = relay.Function([var_5639,var_5640,var_5641,], output)
mutated_mod['func_5642'] = func_5642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4374_call = mod.get_global_var('func_4374')
func_4376_call = mutated_mod.get_global_var('func_4376')
call_5652 = relay.TupleGetItem(func_4374_call(), 1)
call_5653 = relay.TupleGetItem(func_4376_call(), 1)
output = relay.Tuple([call_5652,])
output2 = relay.Tuple([call_5653,])
func_5670 = relay.Function([], output)
mod['func_5670'] = func_5670
mod = relay.transform.InferType()(mod)
mutated_mod['func_5670'] = func_5670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5670_call = mutated_mod.get_global_var('func_5670')
call_5671 = func_5670_call()
output = call_5671
func_5672 = relay.Function([], output)
mutated_mod['func_5672'] = func_5672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2135_call = mod.get_global_var('func_2135')
func_2137_call = mutated_mod.get_global_var('func_2137')
call_5743 = relay.TupleGetItem(func_2135_call(), 0)
call_5744 = relay.TupleGetItem(func_2137_call(), 0)
func_5093_call = mod.get_global_var('func_5093')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_5760 = relay.TupleGetItem(func_5093_call(), 0)
call_5761 = relay.TupleGetItem(func_5094_call(), 0)
func_3058_call = mod.get_global_var('func_3058')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_5773 = func_3058_call()
call_5774 = func_3058_call()
func_5410_call = mod.get_global_var('func_5410')
func_5412_call = mutated_mod.get_global_var('func_5412')
var_5780 = relay.var("var_5780", dtype = "float64", shape = (198,))#candidate|5780|(198,)|var|float64
call_5779 = func_5410_call(relay.reshape(var_5780.astype('float64'), [9, 11, 2]))
call_5781 = func_5410_call(relay.reshape(var_5780.astype('float64'), [9, 11, 2]))
func_3938_call = mod.get_global_var('func_3938')
func_3942_call = mutated_mod.get_global_var('func_3942')
const_5787 = relay.const([4.535273,-2.884547,3.874831,-1.056319,4.902037,-0.810630,6.540755,-5.727099,7.340211,5.316041,1.877251,-9.608966,4.627810,7.988207,-1.749384,-2.584484,-1.422944,8.032061,1.065746,8.839583,5.811511,-9.884233,7.672973,7.809449,8.289402,-2.195414,-8.331849,-0.171589,-5.088367,-3.551179,-3.643592,-3.825134,7.069622,0.531690,-5.173254,5.184114,-9.336530,-6.282316,-1.923606,-3.688693,-4.714255,-3.882157,-3.672964,-8.371277,7.288192,3.836288,-4.547338,-7.117078,9.531155,-5.141939,-3.090831,4.123172,6.092095,-1.513372,0.459310,-1.169693,-1.992751,-4.557540,6.834274,6.038057,-3.910254,-8.929047,-2.374300,-8.292893,-8.877695,1.211402,2.044036,-7.041654,1.976559,-2.377533,7.508312,-1.719903,-7.896977,-1.862152,-3.013900,-4.059534,8.712972,1.652649,8.419480,1.000110,-2.633934,-0.341266,-9.046277,9.501662,-0.554630,-3.721571,-6.321757,8.440685,-8.282793,-8.199278,1.352340,2.232354,0.180193,-1.534064,-7.846801,0.403202,3.202406,-6.058944,-9.032660,4.611501,-4.331892,-4.054613,-4.201950,3.079443,-7.318123,8.785729,-6.488508,-7.577149,1.840884,-0.610184,-7.933047,7.811262,1.182670,0.646614,3.745330,-9.649656,3.099017,-8.057064,-9.985780,-5.334139,9.421661,-3.066297,-6.229429,7.626653,-0.616816,8.797140,2.359922,-5.693974,0.903866,-9.288892,-1.478739,-0.602990,-4.841122,4.724794,-2.882401,7.039949,-6.110127,8.177438,-7.997230,-5.466826,-8.031917,8.734408,-8.082784,-2.500090,-0.737358,-7.332378,-8.291555,-0.745895,7.119567,3.129312,0.118641,5.857412,9.484911,-2.009519,-0.183539,-8.762630,-9.658314,-8.205361,6.743880,-8.104948,-6.119612,-5.018592,7.286484,1.212996,-9.248229,-4.629841,5.763721,3.031090,-7.069642,-4.668930,2.712889,2.246112,-9.971934,-3.491196,8.308237,2.828776,-0.286631,-0.621409,-9.181093,-9.995333,-0.918195,-8.782450,2.576568,-7.451524,6.886022,-6.475435,2.283896,7.764416,7.039121,2.060026,-8.875680,-9.970358,-9.059346,1.604662,-4.124788,-9.097340,-7.795786,-5.312787,-3.335804,-1.326741,3.560045,-2.300578,-8.937705,8.086290,-0.408245,-5.414285,7.519844,1.080858,4.280957,3.626119,-9.355390,4.122925,-8.051136,-8.682775,-7.467670,6.945078,4.538753,0.135277,4.920298,-6.565957,2.543471,-3.555004,8.082829,3.722266,-0.343944,9.100467,-4.998677,-0.959495,-9.681805,9.692230,4.905906,3.794598,0.983817,-7.823570,7.659711,-9.814314,-6.356814,3.067504,-0.658167,-5.132809,2.254822,5.821912,-3.026628,1.656916,7.319981,-8.503564,3.399356,0.777517,-4.316477,5.581044,-8.477927,-1.787001,-5.076948,1.189740,-5.255676,-5.518437,9.920221,1.230804,7.981345,-1.946635,-7.684804,2.858400,-0.774215,-8.823606,-7.727788,-7.612918,3.149406,4.029242,1.832810,-3.696784,4.349593,1.466578,-7.308796,-3.187717,8.748306,-6.573660,6.974699,9.433425,4.252364,-7.367575,8.470603,-8.258800,-2.931849,6.241721,-1.912430,7.796986,-5.788988,-6.344131,-5.240822,-1.408785,-2.037504,6.726347,-9.651253,6.371141,-2.158601,7.833740,5.516634,-4.489435,-8.158549,0.675459,0.172657,-4.065975,3.057511,-4.127838,3.672931,-2.850152,-7.268901,-1.696457,-4.043719,-7.442585,2.934221,0.966872,1.982715,-3.359170,7.302455,8.173820,4.104761,-7.803764,-9.413979,-9.354277,8.432569,5.521169,-2.485746,-6.697182,-1.491906,1.973937,-6.379052,-1.838529,-4.654169,2.387867,-9.237792,-4.139288,-4.507004,-4.176710,4.412595,2.118772], dtype = "float32")#candidate|5787|(336,)|const|float32
call_5786 = func_3938_call(relay.reshape(const_5787.astype('float32'), [3, 8, 14]), relay.reshape(const_5787.astype('float32'), [3, 8, 14]), )
call_5788 = func_3938_call(relay.reshape(const_5787.astype('float32'), [3, 8, 14]), relay.reshape(const_5787.astype('float32'), [3, 8, 14]), )
var_5815 = relay.var("var_5815", dtype = "float32", shape = (3, 8, 14))#candidate|5815|(3, 8, 14)|var|float32
bop_5816 = relay.greater_equal(call_5786.astype('bool'), relay.reshape(var_5815.astype('bool'), relay.shape_of(call_5786))) # shape=(3, 8, 14)
bop_5819 = relay.greater_equal(call_5788.astype('bool'), relay.reshape(var_5815.astype('bool'), relay.shape_of(call_5788))) # shape=(3, 8, 14)
bop_5824 = relay.bitwise_or(bop_5816.astype('uint32'), relay.reshape(call_5786.astype('uint32'), relay.shape_of(bop_5816))) # shape=(3, 8, 14)
bop_5827 = relay.bitwise_or(bop_5819.astype('uint32'), relay.reshape(call_5788.astype('uint32'), relay.shape_of(bop_5819))) # shape=(3, 8, 14)
func_4712_call = mod.get_global_var('func_4712')
func_4716_call = mutated_mod.get_global_var('func_4716')
const_5837 = relay.const([[-7,-5,5,5,-9,5,6,-1,-4,5,-1,-7,7,7,-1,4,-10,-10,6,7,6,1,1,-5,3,1,10,4,-7,-1,-9,-8,-5,-4,-4,6,4,-1,9,9,5,7,-7,-5,3,-3,-10,-1,-1,-5,5,-4,7,5,-1,-10,-4,2,-10,-6,-2,5,-1,-6,-1,-7,2,-7,-7,7,-5,-4,5,-10,2,6,-4,5,-7,-10,-10,7,10,-3,6,-7,-6,-2,7,-6,8,5,4,9,-9,-4,-10,10,-4,-9,2,1,-8,-1,-5,-6,-10,6,8,-9,-6,5,1,6,-10,-6,-2,4,-2,-7,-3,-1,-1,-9,2,-8,-9,4,10,-5,-6,5,-2,2,-4,-10,-9,10,-7,10,4,-8,1,-3,4,3,1,-2,9,-6,10,-9,-6,-10,7,2,8,-4,-2,1,-7,7,-6,-10,10,9,-3,-10,9,-1,10,10,3,-8,-3,10,5,7,-4,-8,4,-6,-8,-5,6,5,-9,-5,-9,7,2,-9,5,-10,-4,5,8,6,-8,2,8,10,-2,-2,-8,10,-8,-8,-8,2,-9,-1,-6,10,9,10,9,7,-4,10,-9,3,3,8,10,-3,-7,-5,-1,-9,-6,8,-8,7,-3,8,-9,-7,10,4,-7,10,-1,-9,9,5,-6,3,5,9,-6,9,-6,2,4,-10,2,5,5,8,-1,-1,5,2,-3,9,6,9,-6,9,-6,3,9,3,-3,9,-5,10,6,1,2,1,2,1,-8,10,-9,1,-10,-1,-9,-6,1,-4,9,-6,-9,-3,6,9,-4,9,-3,-1,-9,7,-3,10,-10,-2,-4,-3,7,6,-10,1,-5,9,-3,10,-3,9,9,-3,-6,9,7,-4,8,10,-4,-1,-3,6,1,7,-2,-1,6,7,10,5,-8,2,9,-3,2,4,6,-1,-6,10,-7,-9,6,-8,-4,2,1,7,3,-7,-5,2,2,6,-4,-8,-9,5,-4,10,3,9,5,6,-7,-4,-3,-2,2,5,-6,8,-9,-1,-5,9,4,-3,-6,-6,1,3,-8,9,5,-7,-6,-8,-9,7,1,-5,-6,5,-9,-4,3,-4,-4,-3,8,2,7,10,1,2,-3,-9,5,-2,-5,5,-6,10,-6,1,-3,10,4,-5,-9,-7,4,-3,1,3,2,5,1,-7,6,-2,10,-8,6,-9,10,7,-5,-3,6,4,8,-5,5,-7,-2,2,5,-6,3,3,-3,-9,1,-5,-2,6,-10,-10,-4,6,7,8,9,-2,1,-8,-8,-5,1,-7,-10,-4,5,-5,-2,-3,-10,3,-6,2,2,6,-8,-2,-2,3,-3,2,10,5,2,-1,10,2,8,-5,-5,-2,-1,-2,-3,-5,-2,4,-8,-2,-10,1,-8,8,-8,-8,-6,-5,-7,10,-2,8,-3,5,-5,10,-1,-5,-7,-7,-6,7,9,8,9,-8,2,6,-2,7,-8,-1,1,10,-9,-2,-3,-6,10,-10,2,3,-6,1,10,5,6,-8,4,-6,6,9,-8,-4,10,9,-2,8,-1,-7,-9,-8,-2,6,6,-10,-10,4,3,8,9,-5,-10,-8,4,-4,10,9,-10,-8,7,-1,-5,4,-2,-1,-10,4,1,-4,9,-9,-10,1,-3,8,-4,-6,-3,-9,5,-10,8,6,7,-6,8,5,4,-7,4,-9,-6,9,7,6,10,8,9,-9,4,3,9,-9,4,9,3,6,3,9,-5,-4,3,5,6,8,-9,3,9,-10,9,-8,-7,4,-10,-2,1,2,-9,-8,2,6,-9,7,2,10,7,8,4,6,6,-1,-7,3,-1,-1,-6,-2,10,2,9,5,-10,1,-6,8,-8,-1,3,1,4,6,-10,5,-2,-2,-7,-8,-2,10,8,2,-6,-1,8,2,-3,-3,9,-5,-3,1,-5,-8,9,-7,-6,3,5,-3,-7,6,-5,4,-5,6,-5,-9,-5,-1,4,1,8,-4,-1,7,-1,-7,2,-10,-10,8,-3,-10,-3,-5,9,-9,-4,-2,-1,3,4,8,-1,6,7,1,-10,-2,-1,1,5,-9,-4,-3,3,-7,-6,-4,7,2,-3,-6,3,-7,-7,4,-10,-10,-7,-9,1,-7,5,5,3,-6,8,1,-1,6,7,-1,-7,9,-6,-2,8,-3,3,5,-5,2,4,-7,-10,-7,4,-3,-9,-5,-3,-1,6,-4,-1,-3,-9,-2,-10,1,3,-8,4,-10,-4,-7,1,9],[-3,6,-1,2,8,4,6,-8,3,-10,5,-1,6,-7,-7,6,-7,-6,3,-10,-4,7,-2,-9,-10,4,-8,4,5,10,-8,-2,9,3,5,-3,8,9,4,4,8,9,5,1,-7,-1,-7,9,-2,10,-6,6,-10,5,-6,5,-9,9,10,-3,1,9,7,-6,2,8,-6,3,1,9,9,1,-10,1,8,-6,-7,9,-5,-5,-8,7,7,-1,10,-8,-5,8,-9,7,2,-8,-2,-5,1,-6,-4,4,-4,2,6,6,8,9,2,7,-1,7,2,-2,3,-2,2,-8,3,-2,-9,10,-2,-7,7,2,-8,3,2,-3,-5,2,2,-6,10,-2,8,-10,-1,7,-10,-7,-10,8,-6,-7,-5,10,6,10,4,7,-4,-2,-4,4,-2,4,-9,-3,3,-8,6,-6,2,10,-10,7,6,10,2,5,4,5,-2,-10,8,-3,-8,9,-5,-7,8,8,5,5,1,-9,-7,-10,-3,-4,-10,7,6,-9,7,-3,-10,-8,-10,-2,2,7,8,-8,8,3,-1,-10,-6,-5,3,-7,-2,9,9,2,-7,-1,-4,7,3,4,2,-8,-10,-3,-4,7,-7,-5,-10,-6,-3,1,5,3,-1,9,-10,-4,-3,-7,-9,-10,-3,-3,-3,-1,5,6,-1,10,-6,7,-8,-8,10,-8,10,-5,7,7,8,-6,9,7,-1,-1,-5,-2,-1,-6,6,10,-3,8,-5,-10,10,-8,-6,-8,-1,3,-1,-1,-7,-3,-2,-8,8,-5,-2,7,-10,2,1,2,-3,8,-2,-6,7,-2,10,3,8,2,4,-4,6,10,-8,-9,-1,-4,-7,2,8,2,5,-8,3,7,-1,2,6,9,8,6,-7,4,1,-8,1,-6,5,-3,8,-8,10,-8,-5,2,-5,3,-9,7,-3,8,7,2,10,2,5,6,-1,-4,3,10,-4,-1,-1,4,5,10,6,4,9,-5,-6,-2,9,-1,-3,2,5,-2,-4,-10,8,1,-4,-1,10,9,-9,3,8,10,-7,9,-8,6,-7,10,-8,9,-5,7,8,-3,1,-5,-2,-10,-9,-10,-2,-8,-5,-6,7,-7,8,8,-1,3,7,-1,-4,7,-10,10,-3,10,-5,3,2,4,3,5,5,6,-5,10,-5,-5,-1,-8,-3,4,-5,-2,4,-8,-10,-1,-1,6,3,7,2,-5,-9,9,1,10,10,-4,7,-3,5,3,-2,-5,-4,3,6,-1,10,5,-5,9,6,-10,-7,2,-7,-9,-4,4,-7,-6,-6,8,-10,9,-9,-1,-4,-9,-1,3,6,7,-8,-9,-7,-10,5,10,2,-1,10,7,10,-4,-9,-3,1,-6,-10,-4,2,-1,-1,-2,-2,5,4,5,1,9,6,-4,9,-6,7,-7,1,5,10,-6,-10,-6,4,-10,-3,-5,-10,-6,1,9,1,6,-5,3,-10,-2,1,-7,-9,9,8,1,-5,7,10,-3,-4,-10,-1,6,3,2,-6,-10,-5,-7,3,9,4,3,1,-4,4,-6,8,-6,2,6,6,2,-4,-4,-4,4,-10,3,-2,8,10,3,-6,10,7,-3,-1,4,-4,4,-1,8,-5,5,-8,7,7,-6,9,10,-4,-6,-9,-2,-9,1,-5,3,1,-9,-3,7,-6,-2,10,10,-4,-9,-9,4,-7,9,-5,2,-2,-5,9,2,6,4,-3,-4,-3,10,3,-1,10,-2,2,-8,-9,7,6,7,3,-2,6,-5,-8,-2,-10,3,2,-2,-3,9,5,2,-9,-5,-8,1,10,4,3,-1,8,-3,-1,-5,9,-4,3,-8,-5,-5,10,1,-3,10,-1,-1,4,1,2,8,1,-6,2,-5,6,1,7,8,7,8,-6,8,6,5,-5,-9,-9,-1,10,-7,9,2,10,-5,-5,-4,5,-5,1,-9,5,3,5,-6,-3,9,2,5,1,-8,5,1,4,-1,6,-1,9,8,9,7,6,3,9,-2,10,-1,2,6,-8,10,8,6,5,-1,7,-8,4,-2,1,-7,4,7,10,1,-2,-1,-2,10,-10,-4,7,-1,-3,-7,-7,-5,-10,4,-10,7,7,4,4,9,-3,10,-2,2,-2,-10,-1,9,-9,-1,-9,1,-6,-5,9,4,-6,-1,-5,-6,1,-7,2,6,-8,-10,-5,5,8,-2,6,6,-2,2,1,4,3,4,9,7,-7,6,-10,5,-3,-4,7,-10,-8,-6]], dtype = "uint8")#candidate|5837|(2, 840)|const|uint8
var_5838 = relay.var("var_5838", dtype = "uint8", shape = ())#candidate|5838|()|var|uint8
call_5836 = relay.TupleGetItem(func_4712_call(relay.reshape(const_5837.astype('uint8'), [84, 20]), relay.reshape(var_5838.astype('uint8'), []), ), 1)
call_5839 = relay.TupleGetItem(func_4716_call(relay.reshape(const_5837.astype('uint8'), [84, 20]), relay.reshape(var_5838.astype('uint8'), []), ), 1)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_5860 = relay.TupleGetItem(func_2016_call(), 1)
call_5861 = relay.TupleGetItem(func_2017_call(), 1)
output = relay.Tuple([call_5743,call_5760,call_5773,call_5779,var_5780,const_5787,bop_5824,call_5836,const_5837,var_5838,call_5860,])
output2 = relay.Tuple([call_5744,call_5761,call_5774,call_5781,var_5780,const_5787,bop_5827,call_5839,const_5837,var_5838,call_5861,])
func_5880 = relay.Function([var_5780,var_5815,var_5838,], output)
mod['func_5880'] = func_5880
mod = relay.transform.InferType()(mod)
mutated_mod['func_5880'] = func_5880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5880_call = mutated_mod.get_global_var('func_5880')
var_5882 = relay.var("var_5882", dtype = "float64", shape = (198,))#candidate|5882|(198,)|var|float64
var_5883 = relay.var("var_5883", dtype = "float32", shape = (3, 8, 14))#candidate|5883|(3, 8, 14)|var|float32
var_5884 = relay.var("var_5884", dtype = "uint8", shape = ())#candidate|5884|()|var|uint8
call_5881 = func_5880_call(var_5882,var_5883,var_5884,)
output = call_5881
func_5885 = relay.Function([var_5882,var_5883,var_5884,], output)
mutated_mod['func_5885'] = func_5885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_5914 = relay.TupleGetItem(func_3234_call(), 0)
call_5915 = relay.TupleGetItem(func_3235_call(), 0)
func_2112_call = mod.get_global_var('func_2112')
func_2116_call = mutated_mod.get_global_var('func_2116')
var_5919 = relay.var("var_5919", dtype = "uint8", shape = (1680,))#candidate|5919|(1680,)|var|uint8
const_5920 = relay.const(-7, dtype = "uint8")#candidate|5920|()|const|uint8
call_5918 = relay.TupleGetItem(func_2112_call(relay.reshape(var_5919.astype('uint8'), [14, 12, 10]), relay.reshape(var_5919.astype('uint8'), [14, 12, 10]), relay.reshape(const_5920.astype('uint8'), []), ), 1)
call_5921 = relay.TupleGetItem(func_2116_call(relay.reshape(var_5919.astype('uint8'), [14, 12, 10]), relay.reshape(var_5919.astype('uint8'), [14, 12, 10]), relay.reshape(const_5920.astype('uint8'), []), ), 1)
func_3638_call = mod.get_global_var('func_3638')
func_3641_call = mutated_mod.get_global_var('func_3641')
var_5929 = relay.var("var_5929", dtype = "float64", shape = (390,))#candidate|5929|(390,)|var|float64
call_5928 = relay.TupleGetItem(func_3638_call(relay.reshape(var_5929.astype('float64'), [3, 10, 13])), 1)
call_5930 = relay.TupleGetItem(func_3641_call(relay.reshape(var_5929.astype('float64'), [3, 10, 13])), 1)
bop_5931 = relay.mod(call_5918.astype('float32'), var_5929.astype('float32')) # shape=(390,)
bop_5934 = relay.mod(call_5921.astype('float32'), var_5929.astype('float32')) # shape=(390,)
output = relay.Tuple([call_5914,var_5919,const_5920,call_5928,bop_5931,])
output2 = relay.Tuple([call_5915,var_5919,const_5920,call_5930,bop_5934,])
func_5944 = relay.Function([var_5919,var_5929,], output)
mod['func_5944'] = func_5944
mod = relay.transform.InferType()(mod)
var_5945 = relay.var("var_5945", dtype = "uint8", shape = (1680,))#candidate|5945|(1680,)|var|uint8
var_5946 = relay.var("var_5946", dtype = "float64", shape = (390,))#candidate|5946|(390,)|var|float64
output = func_5944(var_5945,var_5946,)
func_5947 = relay.Function([var_5945,var_5946,], output)
mutated_mod['func_5947'] = func_5947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mod.get_global_var('func_4196')
func_4198_call = mutated_mod.get_global_var('func_4198')
call_5983 = func_4196_call()
call_5984 = func_4196_call()
func_1264_call = mod.get_global_var('func_1264')
func_1266_call = mutated_mod.get_global_var('func_1266')
call_6001 = func_1264_call(relay.reshape(call_5983.astype('uint8'), [8, 13, 16]))
call_6002 = func_1264_call(relay.reshape(call_5983.astype('uint8'), [8, 13, 16]))
func_2785_call = mod.get_global_var('func_2785')
func_2787_call = mutated_mod.get_global_var('func_2787')
call_6004 = relay.TupleGetItem(func_2785_call(), 0)
call_6005 = relay.TupleGetItem(func_2787_call(), 0)
output = relay.Tuple([call_5983,call_6001,call_6004,])
output2 = relay.Tuple([call_5984,call_6002,call_6005,])
func_6006 = relay.Function([], output)
mod['func_6006'] = func_6006
mod = relay.transform.InferType()(mod)
mutated_mod['func_6006'] = func_6006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6006_call = mutated_mod.get_global_var('func_6006')
call_6007 = func_6006_call()
output = call_6007
func_6008 = relay.Function([], output)
mutated_mod['func_6008'] = func_6008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_6026 = relay.TupleGetItem(func_1016_call(), 5)
call_6027 = relay.TupleGetItem(func_1018_call(), 5)
output = relay.Tuple([call_6026,])
output2 = relay.Tuple([call_6027,])
func_6039 = relay.Function([], output)
mod['func_6039'] = func_6039
mod = relay.transform.InferType()(mod)
mutated_mod['func_6039'] = func_6039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6039_call = mutated_mod.get_global_var('func_6039')
call_6040 = func_6039_call()
output = call_6040
func_6041 = relay.Function([], output)
mutated_mod['func_6041'] = func_6041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mod.get_global_var('func_49')
func_50_call = mutated_mod.get_global_var('func_50')
call_6118 = relay.TupleGetItem(func_49_call(), 0)
call_6119 = relay.TupleGetItem(func_50_call(), 0)
func_5363_call = mod.get_global_var('func_5363')
func_5365_call = mutated_mod.get_global_var('func_5365')
call_6120 = relay.TupleGetItem(func_5363_call(), 0)
call_6121 = relay.TupleGetItem(func_5365_call(), 0)
func_5138_call = mod.get_global_var('func_5138')
func_5140_call = mutated_mod.get_global_var('func_5140')
call_6138 = relay.TupleGetItem(func_5138_call(), 0)
call_6139 = relay.TupleGetItem(func_5140_call(), 0)
func_2697_call = mod.get_global_var('func_2697')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_6140 = relay.TupleGetItem(func_2697_call(), 1)
call_6141 = relay.TupleGetItem(func_2699_call(), 1)
func_1515_call = mod.get_global_var('func_1515')
func_1516_call = mutated_mod.get_global_var('func_1516')
call_6165 = relay.TupleGetItem(func_1515_call(), 0)
call_6166 = relay.TupleGetItem(func_1516_call(), 0)
func_635_call = mod.get_global_var('func_635')
func_636_call = mutated_mod.get_global_var('func_636')
call_6175 = relay.TupleGetItem(func_635_call(), 0)
call_6176 = relay.TupleGetItem(func_636_call(), 0)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
var_6183 = relay.var("var_6183", dtype = "uint8", shape = ())#candidate|6183|()|var|uint8
const_6184 = relay.const([5,7,-2,-3,4,-2,-5,-9,-10,-1,4,4,-9,4,-2,-1,3,-2,10,8,3,1,10,7,6,-10,1,-8,1,-4,-5,7,-3,-4,8,-9,2,7,7,-2,3,5,-10,-4,5,1,3,9,-10,-10,-3,-9,10,-6,1,2,-4,10,10,-4,-2,-6,-6,2,7,4,3,-6,-1,-10,4,10,8,1,-4,4,3,-2,6,5,-7,5,4,3,-4,10,6,6,-10,4,4,-3,-2,6,-10,-1,-1,7,8,1,-4,9,-10,7,-4,5,1,-6,2,2,2,9,2,9,5,-1,10,10,-7,-2,-10,-10,5,-5,-8,9,10,3,3,1,1,-8,6,-1,-6,5,-9,4,-8,3,6,6,-1,8,-1,1,-5,-3,6,3,4,-6,10,9,1,-4,3,4,10,-7,3,5,6,8,-1,-5,-8,9,3,7,-9,2,2,-7,10,-7,3,-2,1,2,10,6,10,-7,5,-8,7,-8,8,5,-1,-10,4,3,1,-7,5,-10,-1,8,2,-2,-10,8,-8,-7,-5,5,-10,-5,6,-3,-5,5,-1,-4,3,-10,8,2,-2,7,7,-9,10,7,5,-8,4,-10,8,-5,-2,5,-6,-8,-5,6,-8,-8,-8,-6,-8,7,8,6,1,-9,8,-1,-1,3,-5,-10,5,-3,7,-7,-4,5,-2,-1,4,-4,-6,-9,5,4,10,-4,6,-9,9,-5,10,6,-5,-5,-9,-1,5,1,-1,-1,-3,-7,4,-9,4,5,-8,-8,-2,-1,-1,5,4,5,2,-8,2,-1,3,-9,-8,1,-7,-10,-9,9,5,5,9,5,-5,-4,10,3,-5,-10,-9,10,7,5,1,7,8,-5,1,6,-7,-3,6,-10,-10,-6,9,-5,4,-4,5,-10,3,-10,9,10,-6,1,-1,-3,-9,-10,-4,7,-4,-2,-4,2,10,-2,7,3,7,5,6,8,8,-6,-10,10,-5,3,-7,-9,-4,-5,4,-4,5,6,-9,7,-10,-2,7,6,-6,-3,1,-9,-4,-6,6,7,9,-3,8,8,6,-10,-1,8,3,-10,5,9,-6,6,-5,5,6,4,1,-2,3,-1,8,2,1,6,-1,-5,-2,-1,2,4,-8,-2,2,6,-5,10,8,-7,-3,-7,9,-3,3,-1,2,4,6,8,9,-5,-3,-10,-8,2,-9,10,-8,-1,9,-7,7,-2,5,-3,6,-3,-5,-1,-9,8,9,7,1,10,2,-2,7,4,-3,-10,-6,-9,-5,6,1,-3,-10,-10,8,10,7,9,-3,8,9,-7,9,6,6,8,-5,-10,9,5,-9,-9,6,-10,10,-7,6,-6,9,8,3,5,-5,3,4,-5,-5,-1,2,-10,-9,-3,-10,-9,10,-6,-3,3,3,-4,-5,2,-1,9,-4,6,-3,-10,10,3,9,5,8,8,3,10,8,6,-7,-3,-3,4,-1,-8,-6,-1,8,-4,3,2,5,3,-6,-3,3,3,8,-1,-4,10,-10,6,6,-8,4,-4,-2,2,-6,-2,-2,7,2,9,-7,-9,-9,-6,-5,-3,-4,5,5,-3,-2,-4,-10,6,-8,-2,-3,1,6,-6,-4,9,7,-4,-3,5,-4,2,9,7,-3,10,10,10,3,-6,-5,4,8,6,9,-7,-10,6,-8,-7,-2,9,-2,-9,-4,-1,9,-3,-7,10,-10,-6,7,4,-7,-8,-7,2,-5,4,3,8,-3,10,-10,6,9,-4,6,-4,8,1,-9,5,-3,1,4,-9,-2,9,-1,-4,6,9,-6,4,-4,-9,1,7,5,-1,9,8,-1,3,-9,-4,-7,-9,-7,6,2,-4,-1,7,9,5,-8,-9,-9,2,-1,6,-9,-10,-8,8,4,-2,-1,3,7,-9,-2,-3,-1,10,1,-10,1,-9,-6,10,6,-5,3,10,5,-4,-6,-7,-1,-10,4,-5,10,5,-10,8,-9,7,-2,-1,-4,3,1,10,-10,6,-2,9,6,10,9,2,-2,9,3,10,-2,-9,6,6,-10,1,7,6,4,-7,-5,-2,-9,-10,8,2,-4,6,2,5,6,6,6,5,9,4,5,2,6,8,3,-5,-3,-4,-2,-7,-6,2,-4,-1,-10,-8,2,9,-3,1,7,10,8,-2,-6,9,-1,-4,-9,-9,-2,4,-10,-4,-1,8,3,-7,5,-1,10,3,-10,-8,1,-8,8,-9,-8,-1,7,7,7,-1,7,3,10,3,-10,1,-10,-6,-10,7,7,-6,-5,-4,-9,7,7,-7,6,8,-1,-7,7,-1,8,4,-6,-10,3,5,9,2,-4,2,7,5,-1,10,6,3,-9,-1,-7,-8,-7,6,7,-1,-7,8,-6,-1,-5,-3,2,7,4,8,9,4,9,1,10,-4,8,10,-4,1,3,2,-9,-9,-7,4,1,3,2,3,-9,-8,8,10,-10,-3,4,-8,-4,-6,4,-8,-2,6,-8,-5,-7,-3,10,8,6,-2,-5,-5,-9,-10,3,-9,-3,-8,-3,8,-5,-4,-8,-6,4,-7,2,7,-3,6,7,10,10,8,10,-5,9,-1,-2,1,6,-4,-10,-2,8,-10,3,2,7,-1,8,-1,5,-3,-8,4,2,4,1,-8,4,-1,-7,4,-4,10,-1,8,4,5,-6,8,9,4,8,6,-8,-10,-1,-1,-9,9,-4,6,-8,2,1,4,1,-7,-7,-2,-3,2,-9,1,3,-8,6,-7,-4,-8,8,-5,9,-10,7,5,-6,-6,-9,-3,-6,1,4,6,-6,2,-6,3,-9,4,-6,-7,-6,-9,9,-9,-2,7,-10,-5,5,10,-6,-9,-5,2,3,-6,-4,6,-7,-8,-9,7,6,-8,1,6,-3,2,-1,-1,-8,5,-10,-5,8,-7,8,8,6,-9,-4,-4,-10,-4,3,-5,-2,2,1,-10,1,-8,9,-5,2,2,8,2,2,-9,1,5,6,5,5,8,3,6,-2,9,-4,-1,-8,-2,-8,7,-7,-3,10,-10,-7,10,6,4,-9,-3,5,-5,6,-3,-8,-4,-3,-8,8,9,-6,-5,-6,-2,1,8,-9,7,2,-10,10,-7,-2,9,5,-7,-8,-5,9,-1,-1,6,-4,5,-3,-8,8,10,-10,-2,-7,-6,-9,-3,-8,-1,-3,-9,10,-5,-7,-7,-8,-5,-8,-5,-3,-3,-4,3,1,1,10,3,3,2,10,-7,10,9,8,-4,7,-7,4,-2,-3,8,-2,3,6,-7,9,-7,7,-7,-1,8,-8,8,-5,4,-1,3,-1,1,4,-8,-2,-1,2,-4,7,-1,-8,-7,-9,-3,1,-6,-4,2,4,2,4,7,-1,8,-4,5,8,-3,10,7,-3,6,9,5,9,-1,3,8,8,2,-5,-2,-6,1,-2,-7,-3,-2,2,-8,-7,3,-5,-1,-9,5,-9,-8,-3,-3,9,-9,5,-7,-9,8,-1,5,4,-9,1,8,10,-7,6,7,1,8,-7,3,-9,3,1,-6,-8,-9,-10,10,-2,-4,-8,4,8,3,6,-3,-6,6,8,4,8,4,-10,-9,-3,1,-5,1,6,1,2,8,4,-7,6,6,-7,-4,-5,9,10,-9,4,10,-4,1,-7,-3,-3,-3,4,-6,10,-9,-5,-4,10,-9,3,-2,10,-2,6,-10,-6,9,2,2,-5,10,-9,6,8,-4,7,-6,1,6,3,-6,8,-10,3,6,-3,10,9,-1,-3,7,-1,1,-1,1,4,5,-5,4,-7,7,-7,1,-5,2,-5,10,-2,-10,-7,-8,-8,-4,-10,-2,9,6,-8,-1,-9,-1,-3,-2,3,9,3,-2,2,6,4,-8,9,8,-1,10,-3,-6,-3,1,-10,-9,-8,8,7,-2,3,-4,4,-10,1,6,-1,2,1,-2,-2,6,2,-9,-7,9,-1,-4,5,1,-4,-1,7,10,7,-9,-5,-10,-10,-5,10,-8,-7,5,8,7,10,8,-1,5,2,-8,10,3,7,-6,-4,-7,9,-10,-5,-9,-6,4,5,7,5,4,1,7,7,-4,-10,-1,-10,-5,7,4,1,3,9,-3,3,-2,-7,4,-10,5,9,8,7,8,7,9,10,-6,-2,-1,-8,-3,2,9,8,-4,9,8,-7,-4,-8,4,5,-7,1,-3,-3,-6,-6,6,8,-2,-4,-5,-9,-5,1,5,3,4,9,5,-8,6,-5,-7,-4,1,9,9,4,5,7,-5,3,4,-9,-4,9,10,-4,-6,5,-6,-3,2,-1,5,8,-8,-9,3,-1,-6,8,-4,-2,1,-8,-2,6,-10,-5,-4,-7,4,-5,6,5,-8,-8,7,5,-7,-7,-3,5,9,-10,-2,7,5,-6,-10,4,6,-10,-2,-1,7,-8,-8,-8,2,1,-7,2,10,2,9,-8,8,5,5,8,3,-6,8,9,-2,-4,9,-8,1,1,-7,-4,8,-4,-7,-7,-8,-1,-7,-6,1,5,-7,-10,-4,-10,-1,6,6,-4,-2,-1,-6,-9,-5,9,9,7,-8,4,-10,-4,9,-10,-10,5,-7,-4,-3,5,10,-5,1,-4,-2,2,-3,3,-4,8,-9,-8,1,1,-5,-3,2,5,-3,2,-7,5,1,-3,-1,1,-4,-6,10,-1,4,1,4,-1,5,10,10,-4,-5,7,10,8,6,-2,-1,-1,-7,-3,10,-7,7,-9,-5,7,-3,-8,2,-8,-1,-3,3,7,8,-2,4,-3,7,8,-6,5,-9,2,-10,10,-9,4,-6,-2,1,-3,3,5,-8,3,-10,-3,1,2,6,-3,-2,-6,7,3,4,-4,1,-9,4,5,10,5,-3,-5,7,-3,4,-9,1,-9,-9,-4,-4,-9,4,-4,-2,-8,-6,-6,-8,3,-2,2,-6,8,6,6,-4,-10,-1,-3,-7,-1,-3,-7,-8,4,5,-3,7,-8,5,4,-1,10,-3,6,-3,3,4,8,2,-3,-5,10,10,-6,-4,-6,9,8,8,-9,10,8,4,7,-7,-3,-9,-6,-2,5,7,10,9,5,1,10,-10,7,-4,9,7,6,4,-4,-6,-10,-4,8,-8,3,-9,-1,3,2,-4,-9,-3,-6,6,-3,1,-7,6,10,-8,-3,6,-5,-4,6,-8,-7,-1,7,-5,2,-4,2,-4,-3,-3,-9,-2,8,3,-2,-3,1,-3,3,-9,-5,6,2,-8,-2,3,2,8,-9,-7,2,-1,-4,-1,2,4,4,5,-7,3,5,-1,-9,-10,9,-9,-5,-4,-5,-8,9,-8,-1,9,7,-9,7,-1,8,7,9,8,8,-5,-1,4,6,-2,-3,4,2,4,3,8,-9,1,-2,-1,5,3,-10,7,-9,2,-10,3,10,-5,-5,6,-7,9,10,-10,-10,2,-2,-6,7,-2,-6,3,2,-9,-1,10,-6,7,-3,-10,2,2,2,-4,8,8,-10,-10,-8,-3,5,-7,4,-4,3,-7,7,-8,9,-10,9,-3,-10,3,-9,9,10,5,-1,1,5,10,9,-3,-1,7,10,9,2,-7,10,5,1,-4,-8,-8,-4,7,6,4,-10,7,3,-9,10,4,-10,-2,10,5,10,5,2,7,-1,-7,-4,-2,-2,9,-6,4,5,-9,1,-7,5,-4,3,5,4,6,8,-4,8,4,8,10,-3,8,-10,4,-6,-2,-2,2,9,-6,3,-7,3,5,-9,-5,-3,-6,-10,10,-9,-5,-9,8,5,5,4,-9,1,-6,-10,-3,-4,7,9,9,10,-10,-1,7,4,3,3,-3,-7,-7,10,1,-6,7,8,5,8,-6,-4,4,-4,6,-9,2,-7,-5,8,10,-6,1,-3,-1,2,1,-10,-5,-1,2,9,-6,-4,3,8,-7,-2,-6,5,-7,5,-2,-2,1,-8,-3,-8,3,-1,5,-2,4,3,9,9,4,4,1,2,1,-5,-7,7,-9,6,10,8,-2,-5,-8,6,10,-7,10,-3,9,7,-2,-6,5,-5,-10,8,-2,4,7,2,-4,8,-6,4,8,-1,-8,-3,9,-7,-1,-4,7,-2,9,-4,3,-4,-3,-6,2,5,-6,-2,-6,-7,-3,9,6,6,5,8,-4,-9,-3,-9,-4,-4,3,-7,-4,-4,-5,8,-4,9,-6,9,9,6,5,-6,2,-1,-7,-3,-5,5,2,3,8,7,-9,4,8,-2,9,-2,-10,-5,-3,6,-5,-10,-6,5,5,10,2,-3,-7,-3,-3,-5,-10,-9,-9,3,-8,3,5,10,1,5,-7,4,-1,8,4,8,4,-8,-2,10,-3,-8,2,10,9,7,-4,-9,9,-1,-1,-6,-6,-9,-5,-10,2,9,-7,7,4,1,-4,7,8,-6,-6,-3,9,1,-10,2,-1,6,-10,2,-7,-4,-5,-6,-8,9,7,6,-3,9,8,-5,-4,4,4,-10,3,3,6,1,4,-9,4,-8,-10,2,10,-8,-10,10,2,-6,5,-3,9,-6,3,-3,-9,-6,7,1,-7,4,3,1,6,-8,-7,4,4,6,-5,8,9,7,2,-5,-8,6,5,-5,-9,3,-6,1,-7,1,7,10,-3,-1,-6,6,7,5,3,2,5,-5,10,-2,4,-3,-3,6,1,-1,-6,-2,10,3,-7,3,-10,-4,-6,-9,10,-1,6,-8,-5,-5,7,1,5,1,9,-6,4,-9,-6,3,4,-8,-9,9,-5,-4,4,-10,-1,2,6,-9,10,3,8,-2,9,-3,6,4,-8,4,6,-10,-4,5,2,10,-3,10,8,6,-3,8,2,-1,-2,2,-8,3,5,-1,5,1,-4,-1,-2,-2,7,4,-3,2,1,-3,8,-2,5,2,-5,-8,-3,-3,-6,-9,6,4,10,7,2,2,-6,-5,-6,-3,-1,1,-9,-8,-1,2,2,-9,4,6,5,-7,10,4,-10,-8,7,2,6,-5,-9,-4,-2,3,-10,3,-5,-6,2,-5,-6,-1,4,1,5,7,-2,5,6,2,-7,1,3,8,-7,8,-6,6,-6,10,-4,7,7,-10,10,-9,6,8,5,-7,-9,-6,5,4,9,-5,10,9,-2,10,-2,8,7,9,1,6,10,4,-4,-7,4,-5,1,-4,4,6,3,6,-9,-3,1,-2,-1,-4,-7,-9,-2,7,-10,-10,-5,2,2,7,5,4,1,-4,-2,-9,-9,2,-3,-7,-2,-1,5,6,-3,9,-4,1,8,-10,-6,-1,-5,8,-6,5,4,-6,1,-6,-4,2,9,3,-1,-10,-2,-3,6,9,8,9,-9,-1,-6,5,-2,-9,-2,-8,7,-1,-1,-6,-6,10,-8,-6,-7,-9,3,-2,-1,-6,3,-8,-6,-9,-3,-5,-9,-3,-7,8,-7,6,9,7,-8,4,8,4,-1,10,-8,-1,3,8,4,-3,-2,-2,-6,-2,-3,10,8,-5,6,3,4,5,-9,-7,-10,5,-7,3,-8,-10,1,2,5,-10,-5,-7,8,-4,8,3,2,-7,7,-4,5,3,5,7,3,3,4,-6,-3,-1,-2,6,-4,-4,-3,3,-4,5,-4,-1,2,6,3,8,2,6,6,9,7,1,2,9,2,7,-8,4,2,6,2,3,5,-10,-3,1,4,1,5,2,-6,5,1,4,9,-1,3,-5,-3,-7,7,8,9,-7,-1,-4,-10,-3,-6,4,-6,-6,-9,7,-9,-10,-4,6,-8,-10,2,8,-2,-4,-7,-6,5,3,-5,8,5,-8,6,4,9,-5,-7,4,5,10,8,6,-7,7,-9,6,3,-3,-8,-5,1,7,-4,-9,-10,-10,6,10,-6,5,-4,-9,5,-7,7,1,1,-5,-10,1,-5,8,10,-5,7,-2,-1,9,3,2,-6,-7,2,2,-8,3,8,3,1,4,7,10,-7,5,-3,-9,9,-9,-9,4,6,9,9,9,9,8,9,6,-7,5,8,-2,-9,-10,2,6,-3,9,6,-2,3,-10,9,10,7,-7,-9,-3,-8,9,-1,7,9,-4,5,-1,-7,1,-7,4,-6,10,-10,6,-10,-9,1,2,3,4,-5,8,-5,10,10,7,-4,3,-4,1,7,4,5,5,-6,-8,3,-3,-5,-10,8,2,8,6,-8,7,-7,1,-1,-2,5,-7,5,7,-4,4,-6,-4,4,8,6,-5,-8,-7,-5,5,-10,-8,-4,-5,-2,2,5,-4,-5,1,10,6,-4,-7,5,-9,-4,-2,-4,9,-5,-5,9,9,4,7,8,1,10,1,10,2,8,4,-10,7,-4,-4,-6,6,5,-3,9,-6,-4,4,-8,-9,10,-8,4,4,2,2,-4], dtype = "uint8")#candidate|6184|(3120,)|const|uint8
call_6182 = relay.TupleGetItem(func_813_call(relay.reshape(var_6183.astype('uint8'), []), relay.reshape(const_6184.astype('uint8'), [15, 16, 13]), ), 1)
call_6185 = relay.TupleGetItem(func_816_call(relay.reshape(var_6183.astype('uint8'), []), relay.reshape(const_6184.astype('uint8'), [15, 16, 13]), ), 1)
output = relay.Tuple([call_6118,call_6120,call_6138,call_6140,call_6165,call_6175,call_6182,var_6183,const_6184,])
output2 = relay.Tuple([call_6119,call_6121,call_6139,call_6141,call_6166,call_6176,call_6185,var_6183,const_6184,])
func_6193 = relay.Function([var_6183,], output)
mod['func_6193'] = func_6193
mod = relay.transform.InferType()(mod)
var_6194 = relay.var("var_6194", dtype = "uint8", shape = ())#candidate|6194|()|var|uint8
output = func_6193(var_6194)
func_6195 = relay.Function([var_6194], output)
mutated_mod['func_6195'] = func_6195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6039_call = mod.get_global_var('func_6039')
func_6041_call = mutated_mod.get_global_var('func_6041')
call_6221 = relay.TupleGetItem(func_6039_call(), 0)
call_6222 = relay.TupleGetItem(func_6041_call(), 0)
func_6039_call = mod.get_global_var('func_6039')
func_6041_call = mutated_mod.get_global_var('func_6041')
call_6228 = relay.TupleGetItem(func_6039_call(), 0)
call_6229 = relay.TupleGetItem(func_6041_call(), 0)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_6234 = relay.TupleGetItem(func_4521_call(), 0)
call_6235 = relay.TupleGetItem(func_4522_call(), 0)
func_3715_call = mod.get_global_var('func_3715')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_6245 = relay.TupleGetItem(func_3715_call(), 0)
call_6246 = relay.TupleGetItem(func_3716_call(), 0)
output = relay.Tuple([call_6221,call_6228,call_6234,call_6245,])
output2 = relay.Tuple([call_6222,call_6229,call_6235,call_6246,])
func_6253 = relay.Function([], output)
mod['func_6253'] = func_6253
mod = relay.transform.InferType()(mod)
mutated_mod['func_6253'] = func_6253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6253_call = mutated_mod.get_global_var('func_6253')
call_6254 = func_6253_call()
output = call_6254
func_6255 = relay.Function([], output)
mutated_mod['func_6255'] = func_6255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5167_call = mod.get_global_var('func_5167')
func_5168_call = mutated_mod.get_global_var('func_5168')
call_6333 = relay.TupleGetItem(func_5167_call(), 0)
call_6334 = relay.TupleGetItem(func_5168_call(), 0)
func_1909_call = mod.get_global_var('func_1909')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_6346 = relay.TupleGetItem(func_1909_call(), 1)
call_6347 = relay.TupleGetItem(func_1910_call(), 1)
func_4156_call = mod.get_global_var('func_4156')
func_4158_call = mutated_mod.get_global_var('func_4158')
call_6362 = relay.TupleGetItem(func_4156_call(), 1)
call_6363 = relay.TupleGetItem(func_4158_call(), 1)
output = relay.Tuple([call_6333,call_6346,call_6362,])
output2 = relay.Tuple([call_6334,call_6347,call_6363,])
func_6371 = relay.Function([], output)
mod['func_6371'] = func_6371
mod = relay.transform.InferType()(mod)
output = func_6371()
func_6372 = relay.Function([], output)
mutated_mod['func_6372'] = func_6372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_6414 = relay.TupleGetItem(func_4774_call(), 0)
call_6415 = relay.TupleGetItem(func_4776_call(), 0)
func_4294_call = mod.get_global_var('func_4294')
func_4296_call = mutated_mod.get_global_var('func_4296')
call_6417 = relay.TupleGetItem(func_4294_call(), 0)
call_6418 = relay.TupleGetItem(func_4296_call(), 0)
func_3500_call = mod.get_global_var('func_3500')
func_3502_call = mutated_mod.get_global_var('func_3502')
call_6425 = relay.TupleGetItem(func_3500_call(relay.reshape(call_6417.astype('uint8'), [1664,])), 0)
call_6426 = relay.TupleGetItem(func_3502_call(relay.reshape(call_6417.astype('uint8'), [1664,])), 0)
func_5495_call = mod.get_global_var('func_5495')
func_5497_call = mutated_mod.get_global_var('func_5497')
var_6435 = relay.var("var_6435", dtype = "uint8", shape = (1680,))#candidate|6435|(1680,)|var|uint8
call_6434 = relay.TupleGetItem(func_5495_call(relay.reshape(var_6435.astype('uint8'), [1680,])), 3)
call_6436 = relay.TupleGetItem(func_5497_call(relay.reshape(var_6435.astype('uint8'), [1680,])), 3)
func_4538_call = mod.get_global_var('func_4538')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_6442 = relay.TupleGetItem(func_4538_call(), 0)
call_6443 = relay.TupleGetItem(func_4539_call(), 0)
output = relay.Tuple([call_6414,call_6417,call_6425,call_6434,var_6435,call_6442,])
output2 = relay.Tuple([call_6415,call_6418,call_6426,call_6436,var_6435,call_6443,])
func_6444 = relay.Function([var_6435,], output)
mod['func_6444'] = func_6444
mod = relay.transform.InferType()(mod)
var_6445 = relay.var("var_6445", dtype = "uint8", shape = (1680,))#candidate|6445|(1680,)|var|uint8
output = func_6444(var_6445)
func_6446 = relay.Function([var_6445], output)
mutated_mod['func_6446'] = func_6446
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6470 = relay.var("var_6470", dtype = "int16", shape = (11, 3, 8))#candidate|6470|(11, 3, 8)|var|int16
const_6471 = relay.const([[[-1,3,1,1,-3,-2,-5,7],[10,-9,-9,-2,-4,-6,-7,10],[-9,-8,-2,6,-7,-10,-7,-6]],[[-2,-9,3,-9,-10,-1,-5,-7],[-5,5,-3,-5,-1,-1,-1,-3],[-3,5,4,2,-8,2,-5,8]],[[-3,-7,3,-5,6,-3,4,-9],[10,2,7,9,6,-7,-10,10],[7,10,-9,6,-2,2,7,-2]],[[5,-1,7,-6,-1,5,-1,7],[-4,9,1,-1,-6,-8,4,10],[-1,2,8,10,-4,-3,1,4]],[[-6,-1,10,-9,-4,-1,-4,-10],[9,2,3,-9,10,-1,-1,-8],[-7,3,10,-6,-8,7,-8,-8]],[[10,-4,-5,-9,4,-5,6,-3],[2,-2,7,-9,7,-8,2,9],[7,4,-8,-4,6,9,-3,-4]],[[-8,7,6,-10,-1,-5,-4,6],[10,3,4,4,7,1,6,4],[4,1,7,-3,2,3,4,9]],[[-9,6,10,-3,-3,-8,10,5],[5,-3,9,-3,4,9,3,-4],[8,6,-9,-4,3,-3,4,-6]],[[6,-1,5,-6,-10,-9,-2,-5],[-2,-8,-10,-5,-6,6,8,9],[1,-9,-6,5,1,-8,6,5]],[[4,1,8,7,-4,-4,-4,6],[-4,2,-9,5,3,-5,7,-7],[3,-3,5,3,-2,2,9,-3]],[[-1,1,6,-2,-7,5,6,5],[1,-8,-9,-6,9,10,3,9],[10,6,5,-4,6,8,-3,-1]]], dtype = "int16")#candidate|6471|(11, 3, 8)|const|int16
bop_6472 = relay.not_equal(var_6470.astype('bool'), relay.reshape(const_6471.astype('bool'), relay.shape_of(var_6470))) # shape=(11, 3, 8)
output = bop_6472
output2 = bop_6472
func_6475 = relay.Function([var_6470,], output)
mod['func_6475'] = func_6475
mod = relay.transform.InferType()(mod)
var_6476 = relay.var("var_6476", dtype = "int16", shape = (11, 3, 8))#candidate|6476|(11, 3, 8)|var|int16
output = func_6475(var_6476)
func_6477 = relay.Function([var_6476], output)
mutated_mod['func_6477'] = func_6477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6253_call = mod.get_global_var('func_6253')
func_6255_call = mutated_mod.get_global_var('func_6255')
call_6482 = relay.TupleGetItem(func_6253_call(), 1)
call_6483 = relay.TupleGetItem(func_6255_call(), 1)
func_2340_call = mod.get_global_var('func_2340')
func_2341_call = mutated_mod.get_global_var('func_2341')
call_6494 = func_2340_call()
call_6495 = func_2340_call()
func_1515_call = mod.get_global_var('func_1515')
func_1516_call = mutated_mod.get_global_var('func_1516')
call_6498 = relay.TupleGetItem(func_1515_call(), 0)
call_6499 = relay.TupleGetItem(func_1516_call(), 0)
output = relay.Tuple([call_6482,call_6494,call_6498,])
output2 = relay.Tuple([call_6483,call_6495,call_6499,])
func_6520 = relay.Function([], output)
mod['func_6520'] = func_6520
mod = relay.transform.InferType()(mod)
output = func_6520()
func_6521 = relay.Function([], output)
mutated_mod['func_6521'] = func_6521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4984_call = mod.get_global_var('func_4984')
func_4985_call = mutated_mod.get_global_var('func_4985')
call_6545 = relay.TupleGetItem(func_4984_call(), 0)
call_6546 = relay.TupleGetItem(func_4985_call(), 0)
output = relay.Tuple([call_6545,])
output2 = relay.Tuple([call_6546,])
func_6548 = relay.Function([], output)
mod['func_6548'] = func_6548
mod = relay.transform.InferType()(mod)
output = func_6548()
func_6549 = relay.Function([], output)
mutated_mod['func_6549'] = func_6549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2785_call = mod.get_global_var('func_2785')
func_2787_call = mutated_mod.get_global_var('func_2787')
call_6642 = relay.TupleGetItem(func_2785_call(), 0)
call_6643 = relay.TupleGetItem(func_2787_call(), 0)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_6655 = relay.TupleGetItem(func_316_call(), 0)
call_6656 = relay.TupleGetItem(func_317_call(), 0)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_6693 = func_2912_call()
call_6694 = func_2912_call()
func_578_call = mod.get_global_var('func_578')
func_581_call = mutated_mod.get_global_var('func_581')
var_6717 = relay.var("var_6717", dtype = "uint64", shape = (6, 63))#candidate|6717|(6, 63)|var|uint64
call_6716 = relay.TupleGetItem(func_578_call(relay.reshape(var_6717.astype('uint64'), [378,])), 3)
call_6718 = relay.TupleGetItem(func_581_call(relay.reshape(var_6717.astype('uint64'), [378,])), 3)
var_6726 = relay.var("var_6726", dtype = "uint64", shape = (6, 63))#candidate|6726|(6, 63)|var|uint64
bop_6727 = relay.mod(var_6717.astype('float64'), relay.reshape(var_6726.astype('float64'), relay.shape_of(var_6717))) # shape=(6, 63)
uop_6745 = relay.erf(bop_6727.astype('float64')) # shape=(6, 63)
uop_6751 = relay.exp(var_6717.astype('float32')) # shape=(6, 63)
var_6757 = relay.var("var_6757", dtype = "float64", shape = (6, 63))#candidate|6757|(6, 63)|var|float64
bop_6758 = relay.logical_xor(uop_6745.astype('int16'), relay.reshape(var_6757.astype('int16'), relay.shape_of(uop_6745))) # shape=(6, 63)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_6761 = relay.TupleGetItem(func_3136_call(), 1)
call_6762 = relay.TupleGetItem(func_3138_call(), 1)
uop_6768 = relay.sin(uop_6751.astype('float32')) # shape=(6, 63)
func_5880_call = mod.get_global_var('func_5880')
func_5885_call = mutated_mod.get_global_var('func_5885')
const_6773 = relay.const([-4.082836,-8.733787,3.092437,-8.558882,-7.888846,4.912088,0.952567,-1.135612,-5.212165,4.095552,-1.485420,2.261513,-6.744147,7.581421,-6.329076,5.060112,9.145132,3.248842,8.364914,0.844084,0.596424,-2.722412,-9.960551,-8.399505,-5.719074,-8.564509,-9.194548,6.209094,3.594387,2.289817,7.006651,-6.947148,-5.963273,1.621265,0.129929,8.958991,1.186137,9.784662,-4.836162,5.030549,-8.656215,7.978611,1.107868,0.155240,2.158225,-5.746808,0.024172,-8.822638,8.890546,3.286579,-9.388250,9.000858,3.503669,6.067635,-0.671059,-8.864312,-9.914762,-0.605167,6.740816,-9.002234,-0.261072,0.988659,-9.308720,6.917842,6.369081,-7.974477,2.773468,2.033346,0.546962,-6.943326,3.305459,-9.353074,-0.947737,-7.380276,-4.148116,-4.694664,8.112078,-7.801707,1.345076,6.797438,-1.982761,3.487338,6.013807,-1.476170,3.042865,9.721191,-3.196552,9.248719,-7.310829,-6.284775,-0.333376,7.796092,-8.999539,6.189532,0.827711,-8.566508,0.677265,2.802275,-1.899090,9.202887,-8.669780,3.039183,-0.432908,6.869652,-9.012582,9.332538,-0.982359,-1.587063,-6.221757,1.776021,3.403700,8.058105,4.287700,8.217780,7.100932,3.384653,7.678586,-3.350209,8.768140,-4.556684,5.737440,6.486327,-6.810006,-7.903446,2.277814,-3.513988,4.953899,9.108442,-9.499362,-1.187486,4.435374,0.768682,-4.329515,-4.195846,7.911235,5.782233,-2.449554,7.373227,2.167814,4.005607,1.356740,8.202309,-0.448885,2.368130,4.428321,-5.558748,0.582623,-4.948959,9.998272,-7.320364,1.366611,5.732126,-4.712382,4.446504,-7.741175,-9.821147,-6.685918,-7.555480,2.261626,-7.810175,0.333735,5.976265,-6.322947,7.090294,0.362019,2.335606,2.825911,-9.107669,6.075333,7.874027,7.449351,4.265253,1.613956,-7.070636,7.149223,-8.805236,9.112597,7.837356,1.334123,7.643513,-0.030257,8.842726,0.542278,0.399979,5.661869,-4.576066,3.259002,2.130331,4.539564,0.757247,-3.521196,6.494752,8.195626,8.948169,5.934448,8.243130,0.846984,-5.102251], dtype = "float64")#candidate|6773|(198,)|const|float64
const_6774 = relay.const([-9.862660,2.481550,6.201590,7.600059,-2.969839,2.362794,-5.302342,-7.415218,-0.072537,-1.063288,-2.893792,6.096821,-0.989027,-2.423749,-1.102493,2.274690,6.510950,-1.036172,1.044290,1.989243,-6.137859,-6.481009,6.772445,-4.034332,-5.085295,-3.026690,1.051560,1.771832,8.918546,4.779664,1.615492,-1.168425,3.267006,-8.215455,-9.752220,-4.102092,-7.020468,9.936630,3.134864,3.259034,-2.878748,-8.842290,-6.889024,-9.843226,7.615000,8.331400,-5.990937,8.926459,-4.277505,-3.966806,9.356829,4.634153,0.953455,0.799313,-4.887211,-7.985170,-5.024764,-7.806253,-8.874408,-0.833787,-2.110291,6.191080,-7.241829,-3.476174,-5.818067,6.684557,5.297946,4.977265,-4.029954,5.116826,-0.169371,5.815329,-5.143470,5.403562,-3.255653,-2.453027,8.635375,5.496585,-9.467664,-6.751341,-3.482006,-9.484738,-5.961797,-6.279073,7.032679,8.850079,-1.245546,-8.437453,9.466772,1.108493,-4.219985,-8.360475,5.313656,6.628029,-5.186925,-3.469321,0.873754,-9.329627,6.537597,-4.604951,5.690151,-1.826966,6.599766,-2.504381,-4.848963,-8.717819,-7.610451,-2.993290,7.602082,6.866589,4.666733,-9.863806,2.271189,-5.059813,-2.835839,4.799525,-4.952969,8.363584,-9.645098,-7.587690,6.655278,2.427296,-0.169228,-5.873618,2.238222,2.129416,6.003599,-0.162730,-1.577150,0.200193,6.873928,-7.499497,-1.134402,5.176320,-8.884759,3.087719,6.273863,7.763920,-2.614162,9.820208,9.340906,-3.438569,-1.003053,5.879381,7.016148,6.718653,8.836993,1.676203,3.342900,1.638994,-8.869878,-4.725050,4.720592,7.692053,6.485773,-1.507938,8.815560,3.476500,2.896919,2.706280,-3.450371,4.712477,-9.899930,8.284140,-7.236749,3.533743,-6.803062,-2.440698,1.160270,4.000656,-7.098369,-6.127866,0.384752,3.989230,-0.725551,7.499336,-4.440891,4.805624,3.456794,-6.364560,5.835734,6.379675,5.795534,3.988581,6.384998,1.812272,-8.297108,-3.310110,-0.952307,-4.581011,-6.058822,5.854460,4.955342,8.322877,1.300940,-3.508935,-8.798490,-9.870906,0.102102,-3.824236,8.780572,-2.599034,7.728570,2.793349,-7.858114,2.849229,6.337122,8.176343,5.893654,-7.235771,8.903641,3.762976,-4.142883,8.302151,3.791426,-6.455662,-5.714592,4.815369,2.885405,7.565640,-6.558536,-9.053763,6.469816,-3.083473,3.299619,4.720078,0.368470,-2.148715,6.220821,8.024173,6.890420,7.597205,-6.462423,-7.554385,2.218407,-6.995516,-5.790582,3.858171,-6.177818,-8.367455,-5.029967,-1.622055,-4.702208,3.697290,5.424989,-7.138996,0.098876,-9.831292,-1.932502,9.183470,-0.872952,-7.565223,1.547404,-5.469260,1.715135,2.304822,-8.218374,-7.100269,-5.570398,-5.066026,-7.043334,-4.487101,-7.766365,-7.944435,4.448591,-2.034287,7.892838,-4.674473,4.267907,-2.950574,4.227567,-6.974899,-0.686499,-8.260177,4.688581,-1.254228,-1.813435,5.689535,6.999182,6.861598,0.451755,-9.505323,-5.967473,2.734224,1.555582,2.415115,3.314857,-3.001835,-0.738763,-4.508560,-6.060672,4.530187,-7.391071,7.172500,-8.728081,-2.670336,0.088467,-1.733484,-6.280944,5.877230,-0.959677,-7.220126,-9.859134,5.991924,-1.555628,-2.946077,-8.985822,6.123390,-8.852006,-8.378185,8.278088,5.917989,0.381505,8.959543,2.504335,7.027256,3.388480,-3.638466,-8.282610,-9.777660,8.470237,5.111165,-5.295171,-4.431075,-0.964832,-9.364841,-1.993243,-5.515131,2.540356,4.312702,-6.989494,-2.842864,-9.513639,4.464211,-7.526301,6.173630], dtype = "float32")#candidate|6774|(336,)|const|float32
const_6775 = relay.const(1, dtype = "uint8")#candidate|6775|()|const|uint8
call_6772 = relay.TupleGetItem(func_5880_call(relay.reshape(const_6773.astype('float64'), [198,]), relay.reshape(const_6774.astype('float32'), [3, 8, 14]), relay.reshape(const_6775.astype('uint8'), []), ), 5)
call_6776 = relay.TupleGetItem(func_5885_call(relay.reshape(const_6773.astype('float64'), [198,]), relay.reshape(const_6774.astype('float32'), [3, 8, 14]), relay.reshape(const_6775.astype('uint8'), []), ), 5)
uop_6777 = relay.sinh(uop_6768.astype('float32')) # shape=(6, 63)
bop_6782 = relay.subtract(uop_6768.astype('float32'), relay.reshape(bop_6758.astype('float32'), relay.shape_of(uop_6768))) # shape=(6, 63)
output = relay.Tuple([call_6642,call_6655,call_6693,call_6716,call_6761,call_6772,const_6773,const_6774,const_6775,uop_6777,bop_6782,])
output2 = relay.Tuple([call_6643,call_6656,call_6694,call_6718,call_6762,call_6776,const_6773,const_6774,const_6775,uop_6777,bop_6782,])
func_6791 = relay.Function([var_6717,var_6726,var_6757,], output)
mod['func_6791'] = func_6791
mod = relay.transform.InferType()(mod)
var_6792 = relay.var("var_6792", dtype = "uint64", shape = (6, 63))#candidate|6792|(6, 63)|var|uint64
var_6793 = relay.var("var_6793", dtype = "uint64", shape = (6, 63))#candidate|6793|(6, 63)|var|uint64
var_6794 = relay.var("var_6794", dtype = "float64", shape = (6, 63))#candidate|6794|(6, 63)|var|float64
output = func_6791(var_6792,var_6793,var_6794,)
func_6795 = relay.Function([var_6792,var_6793,var_6794,], output)
mutated_mod['func_6795'] = func_6795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1501_call = mod.get_global_var('func_1501')
func_1502_call = mutated_mod.get_global_var('func_1502')
call_6824 = relay.TupleGetItem(func_1501_call(), 3)
call_6825 = relay.TupleGetItem(func_1502_call(), 3)
output = call_6824
output2 = call_6825
func_6858 = relay.Function([], output)
mod['func_6858'] = func_6858
mod = relay.transform.InferType()(mod)
mutated_mod['func_6858'] = func_6858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6858_call = mutated_mod.get_global_var('func_6858')
call_6859 = func_6858_call()
output = call_6859
func_6860 = relay.Function([], output)
mutated_mod['func_6860'] = func_6860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6371_call = mod.get_global_var('func_6371')
func_6372_call = mutated_mod.get_global_var('func_6372')
call_6861 = relay.TupleGetItem(func_6371_call(), 0)
call_6862 = relay.TupleGetItem(func_6372_call(), 0)
output = call_6861
output2 = call_6862
func_6889 = relay.Function([], output)
mod['func_6889'] = func_6889
mod = relay.transform.InferType()(mod)
output = func_6889()
func_6890 = relay.Function([], output)
mutated_mod['func_6890'] = func_6890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1181_call = mod.get_global_var('func_1181')
func_1183_call = mutated_mod.get_global_var('func_1183')
call_6897 = func_1181_call()
call_6898 = func_1181_call()
output = relay.Tuple([call_6897,])
output2 = relay.Tuple([call_6898,])
func_6938 = relay.Function([], output)
mod['func_6938'] = func_6938
mod = relay.transform.InferType()(mod)
output = func_6938()
func_6939 = relay.Function([], output)
mutated_mod['func_6939'] = func_6939
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6966 = relay.var("var_6966", dtype = "uint64", shape = (1, 10, 1))#candidate|6966|(1, 10, 1)|var|uint64
var_6967 = relay.var("var_6967", dtype = "uint64", shape = (1, 10, 12))#candidate|6967|(1, 10, 12)|var|uint64
bop_6968 = relay.equal(var_6966.astype('bool'), var_6967.astype('bool')) # shape=(1, 10, 12)
bop_6971 = relay.power(bop_6968.astype('float64'), relay.reshape(var_6967.astype('float64'), relay.shape_of(bop_6968))) # shape=(1, 10, 12)
uop_6984 = relay.sigmoid(var_6966.astype('float64')) # shape=(1, 10, 1)
func_2534_call = mod.get_global_var('func_2534')
func_2537_call = mutated_mod.get_global_var('func_2537')
const_6993 = relay.const([-6,-3,7,5,-10,-10,-4,-4,2,-9,10,4,-2], dtype = "int32")#candidate|6993|(13,)|const|int32
call_6992 = func_2534_call(relay.reshape(const_6993.astype('int32'), [1, 13]), relay.reshape(const_6993.astype('int32'), [1, 13]), )
call_6994 = func_2534_call(relay.reshape(const_6993.astype('int32'), [1, 13]), relay.reshape(const_6993.astype('int32'), [1, 13]), )
output = relay.Tuple([bop_6971,uop_6984,call_6992,const_6993,])
output2 = relay.Tuple([bop_6971,uop_6984,call_6994,const_6993,])
func_6999 = relay.Function([var_6966,var_6967,], output)
mod['func_6999'] = func_6999
mod = relay.transform.InferType()(mod)
var_7000 = relay.var("var_7000", dtype = "uint64", shape = (1, 10, 1))#candidate|7000|(1, 10, 1)|var|uint64
var_7001 = relay.var("var_7001", dtype = "uint64", shape = (1, 10, 12))#candidate|7001|(1, 10, 12)|var|uint64
output = func_6999(var_7000,var_7001,)
func_7002 = relay.Function([var_7000,var_7001,], output)
mutated_mod['func_7002'] = func_7002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6889_call = mod.get_global_var('func_6889')
func_6890_call = mutated_mod.get_global_var('func_6890')
call_7007 = func_6889_call()
call_7008 = func_6889_call()
output = relay.Tuple([call_7007,])
output2 = relay.Tuple([call_7008,])
func_7018 = relay.Function([], output)
mod['func_7018'] = func_7018
mod = relay.transform.InferType()(mod)
output = func_7018()
func_7019 = relay.Function([], output)
mutated_mod['func_7019'] = func_7019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_7028 = relay.TupleGetItem(func_1016_call(), 1)
call_7029 = relay.TupleGetItem(func_1018_call(), 1)
func_2534_call = mod.get_global_var('func_2534')
func_2537_call = mutated_mod.get_global_var('func_2537')
var_7031 = relay.var("var_7031", dtype = "int32", shape = (13,))#candidate|7031|(13,)|var|int32
call_7030 = func_2534_call(relay.reshape(var_7031.astype('int32'), [1, 13]), relay.reshape(var_7031.astype('int32'), [1, 13]), )
call_7032 = func_2534_call(relay.reshape(var_7031.astype('int32'), [1, 13]), relay.reshape(var_7031.astype('int32'), [1, 13]), )
func_487_call = mod.get_global_var('func_487')
func_489_call = mutated_mod.get_global_var('func_489')
const_7081 = relay.const([-10,3,-5,-10,7,-8,5,-1,-8,-3,-7,-5,3,-8,-8,4,-9,1,-10,-7,-3,9,-9,-8,9,1,2,-7,-8,6,3,5,-9,-5,9,5,7,10,6,-2,-9,-5,1,-8,8,-6,-5,2,-9,-4,-9,8,5,-1,-8,-10,-7,10,6,8,3,4,7,6,2,-2,-9,4,-10,8,7,-5,-2,2,-4,-1,-6,-8,2,-9,-4,-5,3,8,4,1,4,6,2,4,-10,-6,-2,1,8,8,3,4,3,-1,-6,10,8,-5,-6,6,-4,2,7,-9,3,7,-3,4,-3,-4,-7,8,-10,6,2,2,6,-1,9,-10,-9,10,9,7,9,2,6,3,-3,-4,5,-10,-3,-6,10,5,-6,-1,-9,9,-10,5,-1,3,-7,10,4,3,-2,10,-6,1,-7,6,-1,-5,-6,-6,-7,2,8,8,-5,-9,-1,-10,1,-10,4,-8,3,-7,-2,-7,-3,-4,4,-3,2,-5,-1,1,-6,4,-9,8,-4,2,-7,-4,9,-3,8,1,10,-5,2,-4,-9,10,-9,-1,-1,-8,1,3,9,-4,-4,9,4,4,3,4,-6,-1,3,9,-2,-4,-8,4,3,-6,-4,10,10,4,3,5,-2,-6,6,-1,-4,-3,2,-2,7,3,-3,-1,-8,-4,5,-2,-4,4,-6,10,9,-4,3,7,4,-3,-6,7,3,5,-3,-7,-7,-8,-5,5,-2,-7,5,-6,6,5,8,-6,-5,1,9,-4,-8,-1,3,-8,-5,1,-9,-8,-8,6,6,9,4,1,7,-2,-10,-9,-7,7,10,-1,-6,-5,-3,-10,-5,-2,8,-4,9,-9,7,1,5,-7,7,-5,8,-5,10,-9,6,-6,3,7,-4,-2,-4,-6,-10,-5,10,7,-9,8,-10,6,8,-10,2,4,4,8,8,9,6,4,2,-5,-8,2,-9,3,10,10,-1,-9,-10,-6,-2,8,-9,-7,8,1,2,3,2,1,-1,6,-5,8], dtype = "uint64")#candidate|7081|(378,)|const|uint64
call_7080 = relay.TupleGetItem(func_487_call(relay.reshape(const_7081.astype('uint64'), [6, 63])), 4)
call_7082 = relay.TupleGetItem(func_489_call(relay.reshape(const_7081.astype('uint64'), [6, 63])), 4)
output = relay.Tuple([call_7028,call_7030,var_7031,call_7080,const_7081,])
output2 = relay.Tuple([call_7029,call_7032,var_7031,call_7082,const_7081,])
func_7083 = relay.Function([var_7031,], output)
mod['func_7083'] = func_7083
mod = relay.transform.InferType()(mod)
var_7084 = relay.var("var_7084", dtype = "int32", shape = (13,))#candidate|7084|(13,)|var|int32
output = func_7083(var_7084)
func_7085 = relay.Function([var_7084], output)
mutated_mod['func_7085'] = func_7085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_897_call = mod.get_global_var('func_897')
func_899_call = mutated_mod.get_global_var('func_899')
call_7115 = relay.TupleGetItem(func_897_call(), 0)
call_7116 = relay.TupleGetItem(func_899_call(), 0)
output = relay.Tuple([call_7115,])
output2 = relay.Tuple([call_7116,])
func_7149 = relay.Function([], output)
mod['func_7149'] = func_7149
mod = relay.transform.InferType()(mod)
output = func_7149()
func_7150 = relay.Function([], output)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_7165 = relay.TupleGetItem(func_2523_call(), 0)
call_7166 = relay.TupleGetItem(func_2525_call(), 0)
output = relay.Tuple([call_7165,])
output2 = relay.Tuple([call_7166,])
func_7171 = relay.Function([], output)
mod['func_7171'] = func_7171
mod = relay.transform.InferType()(mod)
output = func_7171()
func_7172 = relay.Function([], output)
mutated_mod['func_7172'] = func_7172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_7238 = relay.TupleGetItem(func_353_call(), 4)
call_7239 = relay.TupleGetItem(func_355_call(), 4)
output = call_7238
output2 = call_7239
func_7276 = relay.Function([], output)
mod['func_7276'] = func_7276
mod = relay.transform.InferType()(mod)
mutated_mod['func_7276'] = func_7276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7276_call = mutated_mod.get_global_var('func_7276')
call_7277 = func_7276_call()
output = call_7277
func_7278 = relay.Function([], output)
mutated_mod['func_7278'] = func_7278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_7302 = relay.TupleGetItem(func_353_call(), 2)
call_7303 = relay.TupleGetItem(func_355_call(), 2)
output = relay.Tuple([call_7302,])
output2 = relay.Tuple([call_7303,])
func_7309 = relay.Function([], output)
mod['func_7309'] = func_7309
mod = relay.transform.InferType()(mod)
output = func_7309()
func_7310 = relay.Function([], output)
mutated_mod['func_7310'] = func_7310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2135_call = mod.get_global_var('func_2135')
func_2137_call = mutated_mod.get_global_var('func_2137')
call_7329 = relay.TupleGetItem(func_2135_call(), 0)
call_7330 = relay.TupleGetItem(func_2137_call(), 0)
output = relay.Tuple([call_7329,])
output2 = relay.Tuple([call_7330,])
func_7342 = relay.Function([], output)
mod['func_7342'] = func_7342
mod = relay.transform.InferType()(mod)
mutated_mod['func_7342'] = func_7342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7342_call = mutated_mod.get_global_var('func_7342')
call_7343 = func_7342_call()
output = call_7343
func_7344 = relay.Function([], output)
mutated_mod['func_7344'] = func_7344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7348 = relay.var("var_7348", dtype = "float32", shape = (8, 1, 1))#candidate|7348|(8, 1, 1)|var|float32
uop_7349 = relay.asin(var_7348.astype('float32')) # shape=(8, 1, 1)
func_1264_call = mod.get_global_var('func_1264')
func_1266_call = mutated_mod.get_global_var('func_1266')
var_7374 = relay.var("var_7374", dtype = "uint8", shape = (1664,))#candidate|7374|(1664,)|var|uint8
call_7373 = func_1264_call(relay.reshape(var_7374.astype('uint8'), [8, 13, 16]))
call_7375 = func_1264_call(relay.reshape(var_7374.astype('uint8'), [8, 13, 16]))
func_578_call = mod.get_global_var('func_578')
func_581_call = mutated_mod.get_global_var('func_581')
const_7388 = relay.const([[-9],[1],[6],[-4],[-5],[-2],[-5],[3],[-8],[-1],[-4],[9],[-2],[3],[-7],[2],[-5],[-1],[2],[-5],[2],[-9],[6],[-5],[10],[-1],[6],[8],[1],[7],[-10],[1],[3],[-4],[7],[1],[1],[-10],[-5],[-1],[10],[7],[4],[-5],[1],[-2],[-10],[-4],[-6],[7],[2],[-5],[-9],[7],[-10],[7],[2],[8],[-3],[10],[5],[-3],[-6],[-8],[-7],[-6],[-5],[9],[-7],[-10],[-7],[-9],[-2],[7],[-7],[1],[1],[-7],[-3],[9],[-3],[9],[7],[-4],[6],[-3],[10],[6],[-8],[1],[-1],[9],[6],[-9],[4],[9],[5],[7],[-7],[8],[6],[10],[7],[2],[-8],[3],[3],[3],[10],[8],[-2],[-3],[-6],[10],[-3],[9],[-2],[-5],[-5],[-4],[-10],[-6],[1],[-4],[-1],[-6],[1],[1],[10],[-1],[10],[2],[10],[-2],[-6],[2],[5],[1],[-5],[-6],[-9],[-1],[-2],[8],[-2],[2],[-2],[7],[-2],[9],[-7],[-6],[-6],[8],[-1],[-10],[-7],[-1],[-3],[-8],[1],[-8],[-6],[4],[-6],[-8],[1],[5],[10],[-3],[-10],[-1],[3],[-5],[-4],[-1],[6],[-5],[6],[10],[2],[7],[1],[-3],[7],[-2],[-8],[-3],[9],[-7],[-2],[-8],[-10],[1],[-4],[-10],[-1],[10],[-10],[5],[-10],[4],[1],[8],[7],[3],[-4],[8],[-5],[1],[-3],[6],[9],[8],[-10],[7],[-1],[9],[-8],[6],[-4],[5],[-1],[3],[-5],[5],[-7],[-2],[8],[6],[-4],[-9],[3],[10],[7],[-9],[4],[-1],[8],[-1],[10],[10],[7],[-4],[1],[-5],[2],[-9],[4],[-8],[-5],[3],[10],[4],[-10],[2],[-1],[5],[-2],[4],[-10],[8],[5],[-7],[-7],[3],[10],[1],[10],[10],[10],[-9],[-4],[-10],[-5],[2],[7],[7],[7],[4],[-9],[-6],[-3],[-10],[4],[-4],[-4],[5],[9],[-6],[4],[-10],[-8],[-3],[-3],[1],[-4],[-2],[5],[9],[-4],[4],[-5],[-7],[6],[9],[-3],[-1],[9],[8],[-2],[3],[-5],[10],[-7],[-9],[-3],[-8],[-2],[3],[2],[8],[-4],[-8],[2],[5],[2],[-10],[1],[7],[3],[8],[9],[-4],[-2],[-6],[2],[2],[2],[9],[4],[10],[1],[5],[1],[9],[-9],[10],[4],[-6],[-5],[-3],[-8],[-5],[2],[4],[9],[4],[-3],[-2],[-10],[-10],[10],[5],[-6],[-10],[-5],[1],[5],[4],[1],[5],[-4],[-2],[5],[-3],[6],[4]], dtype = "uint64")#candidate|7388|(378, 1)|const|uint64
call_7387 = relay.TupleGetItem(func_578_call(relay.reshape(const_7388.astype('uint64'), [378,])), 1)
call_7389 = relay.TupleGetItem(func_581_call(relay.reshape(const_7388.astype('uint64'), [378,])), 1)
func_883_call = mod.get_global_var('func_883')
func_885_call = mutated_mod.get_global_var('func_885')
var_7392 = relay.var("var_7392", dtype = "float64", shape = (224, 1))#candidate|7392|(224, 1)|var|float64
call_7391 = func_883_call(relay.reshape(var_7392.astype('float64'), [1, 16, 14]))
call_7393 = func_883_call(relay.reshape(var_7392.astype('float64'), [1, 16, 14]))
var_7394 = relay.var("var_7394", dtype = "float32", shape = (8, 16, 1))#candidate|7394|(8, 16, 1)|var|float32
bop_7395 = relay.power(uop_7349.astype('float64'), var_7394.astype('float64')) # shape=(8, 16, 1)
func_4538_call = mod.get_global_var('func_4538')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_7398 = relay.TupleGetItem(func_4538_call(), 0)
call_7399 = relay.TupleGetItem(func_4539_call(), 0)
output = relay.Tuple([call_7373,var_7374,call_7387,const_7388,call_7391,var_7392,bop_7395,call_7398,])
output2 = relay.Tuple([call_7375,var_7374,call_7389,const_7388,call_7393,var_7392,bop_7395,call_7399,])
func_7401 = relay.Function([var_7348,var_7374,var_7392,var_7394,], output)
mod['func_7401'] = func_7401
mod = relay.transform.InferType()(mod)
var_7402 = relay.var("var_7402", dtype = "float32", shape = (8, 1, 1))#candidate|7402|(8, 1, 1)|var|float32
var_7403 = relay.var("var_7403", dtype = "uint8", shape = (1664,))#candidate|7403|(1664,)|var|uint8
var_7404 = relay.var("var_7404", dtype = "float64", shape = (224, 1))#candidate|7404|(224, 1)|var|float64
var_7405 = relay.var("var_7405", dtype = "float32", shape = (8, 16, 1))#candidate|7405|(8, 16, 1)|var|float32
output = func_7401(var_7402,var_7403,var_7404,var_7405,)
func_7406 = relay.Function([var_7402,var_7403,var_7404,var_7405,], output)
mutated_mod['func_7406'] = func_7406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_7442 = relay.TupleGetItem(func_4774_call(), 0)
call_7443 = relay.TupleGetItem(func_4776_call(), 0)
output = relay.Tuple([call_7442,])
output2 = relay.Tuple([call_7443,])
func_7485 = relay.Function([], output)
mod['func_7485'] = func_7485
mod = relay.transform.InferType()(mod)
output = func_7485()
func_7486 = relay.Function([], output)
mutated_mod['func_7486'] = func_7486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6548_call = mod.get_global_var('func_6548')
func_6549_call = mutated_mod.get_global_var('func_6549')
call_7498 = relay.TupleGetItem(func_6548_call(), 0)
call_7499 = relay.TupleGetItem(func_6549_call(), 0)
func_7342_call = mod.get_global_var('func_7342')
func_7344_call = mutated_mod.get_global_var('func_7344')
call_7500 = relay.TupleGetItem(func_7342_call(), 0)
call_7501 = relay.TupleGetItem(func_7344_call(), 0)
output = relay.Tuple([call_7498,call_7500,])
output2 = relay.Tuple([call_7499,call_7501,])
func_7504 = relay.Function([], output)
mod['func_7504'] = func_7504
mod = relay.transform.InferType()(mod)
output = func_7504()
func_7505 = relay.Function([], output)
mutated_mod['func_7505'] = func_7505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_7517 = relay.TupleGetItem(func_2902_call(), 1)
call_7518 = relay.TupleGetItem(func_2904_call(), 1)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_7535 = relay.TupleGetItem(func_1769_call(), 2)
call_7536 = relay.TupleGetItem(func_1771_call(), 2)
output = relay.Tuple([call_7517,call_7535,])
output2 = relay.Tuple([call_7518,call_7536,])
func_7543 = relay.Function([], output)
mod['func_7543'] = func_7543
mod = relay.transform.InferType()(mod)
output = func_7543()
func_7544 = relay.Function([], output)
mutated_mod['func_7544'] = func_7544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2387_call = mod.get_global_var('func_2387')
func_2389_call = mutated_mod.get_global_var('func_2389')
call_7574 = func_2387_call()
call_7575 = func_2387_call()
func_7485_call = mod.get_global_var('func_7485')
func_7486_call = mutated_mod.get_global_var('func_7486')
call_7578 = relay.TupleGetItem(func_7485_call(), 0)
call_7579 = relay.TupleGetItem(func_7486_call(), 0)
func_2112_call = mod.get_global_var('func_2112')
func_2116_call = mutated_mod.get_global_var('func_2116')
var_7589 = relay.var("var_7589", dtype = "uint8", shape = (1680,))#candidate|7589|(1680,)|var|uint8
const_7590 = relay.const(8, dtype = "uint8")#candidate|7590|()|const|uint8
call_7588 = relay.TupleGetItem(func_2112_call(relay.reshape(var_7589.astype('uint8'), [14, 12, 10]), relay.reshape(var_7589.astype('uint8'), [14, 12, 10]), relay.reshape(const_7590.astype('uint8'), []), ), 0)
call_7591 = relay.TupleGetItem(func_2116_call(relay.reshape(var_7589.astype('uint8'), [14, 12, 10]), relay.reshape(var_7589.astype('uint8'), [14, 12, 10]), relay.reshape(const_7590.astype('uint8'), []), ), 0)
func_5410_call = mod.get_global_var('func_5410')
func_5412_call = mutated_mod.get_global_var('func_5412')
const_7596 = relay.const([6.187608,0.933128,2.150011,6.857489,8.381213,2.745615,-2.462367,2.455404,-2.764181,0.390239,1.127636,-1.997175,7.046759,-8.356923,-8.388071,-0.288433,-1.674140,3.766049,2.300170,3.114107,2.821362,-2.754210,-7.366985,8.278922,-0.295501,-5.376826,-8.213680,-5.125915,-4.561284,0.533328,4.717785,-4.846465,5.095411,5.737283,6.056381,0.511427,5.989401,-0.057444,0.353514,-3.046326,-7.269125,6.860849,5.813613,7.967451,5.612058,5.431729,-0.713195,-4.864428,4.299446,6.514943,-2.100129,2.289986,-5.082783,4.325087,-7.963795,3.723135,-6.063457,8.977672,1.272295,3.999818,1.457954,3.196056,9.737388,6.092849,8.392586,1.253054,5.219097,5.692101,-2.645076,5.261847,3.392146,7.966181,-9.070504,7.824023,0.026891,-1.329831,3.613484,6.821573,4.233031,-5.777197,0.635532,-5.981974,-6.059476,-1.908046,-4.866656,5.736152,2.091235,3.757789,-8.501753,1.305413,4.842150,-3.365203,0.127777,8.421126,6.819949,9.341016,5.915251,8.087610,0.170091,-2.273279,-0.261276,2.081920,8.331413,5.441799,-3.118729,0.308731,-1.245669,-6.578088,4.657822,-4.169929,1.129132,7.756833,5.178676,9.586814,5.034324,-4.261185,8.778472,4.660502,-3.632483,-9.644233,0.176449,-5.479271,-6.113326,8.348053,8.955953,-0.408091,2.023004,5.236728,-3.407126,4.796656,9.509228,7.606820,-8.568015,2.670406,9.518418,2.811253,3.861854,-9.959618,-3.996078,-4.865662,4.171910,6.273449,-6.601363,1.870713,4.579904,-8.095888,-7.658734,7.603010,-5.551475,2.149157,7.455340,-1.035256,3.113610,-6.792380,-9.978035,7.904223,8.941343,-9.702817,3.476313,-6.092080,7.516728,8.529299,0.784213,-2.093230,8.581026,8.256327,-1.015141,-9.412339,3.358202,9.819555,6.552802,2.130617,3.309606,-7.577221,-3.133994,3.456227,-3.655056,4.821668,-7.160536,5.176520,-1.968888,-7.442764,3.277209,-9.400916,3.958733,-1.472472,-6.957017,6.786692,-2.485925,-1.417840,-3.588609,-2.298143,2.856472,-0.008587,9.435278,4.186326,1.514331,-6.506601], dtype = "float64")#candidate|7596|(198,)|const|float64
call_7595 = func_5410_call(relay.reshape(const_7596.astype('float64'), [9, 11, 2]))
call_7597 = func_5410_call(relay.reshape(const_7596.astype('float64'), [9, 11, 2]))
output = relay.Tuple([call_7574,call_7578,call_7588,var_7589,const_7590,call_7595,const_7596,])
output2 = relay.Tuple([call_7575,call_7579,call_7591,var_7589,const_7590,call_7597,const_7596,])
func_7601 = relay.Function([var_7589,], output)
mod['func_7601'] = func_7601
mod = relay.transform.InferType()(mod)
mutated_mod['func_7601'] = func_7601
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7602 = relay.var("var_7602", dtype = "uint8", shape = (1680,))#candidate|7602|(1680,)|var|uint8
func_7601_call = mutated_mod.get_global_var('func_7601')
call_7603 = func_7601_call(var_7602)
output = call_7603
func_7604 = relay.Function([var_7602], output)
mutated_mod['func_7604'] = func_7604
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7606 = relay.var("var_7606", dtype = "float32", shape = (9, 13, 1))#candidate|7606|(9, 13, 1)|var|float32
uop_7607 = relay.acosh(var_7606.astype('float32')) # shape=(9, 13, 1)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_7610 = func_1396_call()
call_7611 = func_1396_call()
func_6999_call = mod.get_global_var('func_6999')
func_7002_call = mutated_mod.get_global_var('func_7002')
var_7627 = relay.var("var_7627", dtype = "uint64", shape = (10,))#candidate|7627|(10,)|var|uint64
const_7628 = relay.const([2,9,7,-1,-7,3,-10,-9,7,-3,7,-1,-7,-7,1,-8,-3,4,-6,-2,-3,-5,8,-5,-5,7,10,-4,-6,-1,8,-3,-8,-1,-3,7,8,8,7,10,2,3,-5,3,7,-2,3,6,-2,8,-9,-3,7,4,-5,-8,-4,-2,-8,-4,-7,10,2,3,-4,-1,-6,-4,4,-6,4,7,-5,-7,-2,-7,-7,-2,6,3,8,7,-6,6,-8,-10,-6,-10,-8,5,-8,-10,1,6,-9,9,2,-1,6,-2,-10,9,-1,-9,6,8,6,2,10,-7,6,-6,4,9,-5,-6,-3,-2,-4,3], dtype = "uint64")#candidate|7628|(120,)|const|uint64
call_7626 = relay.TupleGetItem(func_6999_call(relay.reshape(var_7627.astype('uint64'), [1, 10, 1]), relay.reshape(const_7628.astype('uint64'), [1, 10, 12]), ), 1)
call_7629 = relay.TupleGetItem(func_7002_call(relay.reshape(var_7627.astype('uint64'), [1, 10, 1]), relay.reshape(const_7628.astype('uint64'), [1, 10, 12]), ), 1)
output = relay.Tuple([uop_7607,call_7610,call_7626,var_7627,const_7628,])
output2 = relay.Tuple([uop_7607,call_7611,call_7629,var_7627,const_7628,])
func_7631 = relay.Function([var_7606,var_7627,], output)
mod['func_7631'] = func_7631
mod = relay.transform.InferType()(mod)
var_7632 = relay.var("var_7632", dtype = "float32", shape = (9, 13, 1))#candidate|7632|(9, 13, 1)|var|float32
var_7633 = relay.var("var_7633", dtype = "uint64", shape = (10,))#candidate|7633|(10,)|var|uint64
output = func_7631(var_7632,var_7633,)
func_7634 = relay.Function([var_7632,var_7633,], output)
mutated_mod['func_7634'] = func_7634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6253_call = mod.get_global_var('func_6253')
func_6255_call = mutated_mod.get_global_var('func_6255')
call_7642 = relay.TupleGetItem(func_6253_call(), 1)
call_7643 = relay.TupleGetItem(func_6255_call(), 1)
func_4899_call = mod.get_global_var('func_4899')
func_4902_call = mutated_mod.get_global_var('func_4902')
const_7669 = relay.const([1,-2,8,-9,-9,-8,9,9,9,-10,2,-2,3,-1,-5,8,10,-9,6,-5,-2,2,-9,7,2,8,3,-2,4,-3,-2,4,-1,-4,10,-3,-4,-4,-3,-1,-8,10,-1,-2,-4,5,-5,9,4,4,5,-6,2,2,-5,-2,-3,6,3,-10,-4,4,-6,7,8,-3,1,-2,3,8,-6,-1,-1,3,-7,-2,10,10,10,-5,1,3,-9,-2,-8,10,-1,3,10,-7,-10,9,4,5,7,4,8,-1,-2,-1,5,8,-4,7,8,-2,2,8,9,2,5,-7,3,2,-10,10,6,-1,-9,-4,-2,-5,6,-2,9,4,-10,-9,-6,2,7,1,-10,-4,3,-3,-4,1,4,-6,9,-10,-10,4,1,-4,-8,2,9,4,-3,9,7,-9,5,-7,7,3,-6,3,-3,-6,4,-6,5,7,8,7,-7,-10,4,-5,5,-8,5,8,10,6,3,1,1,-6,-5,6,-9,-2,-4,-4,5,7,5,7,-1,-1,6,-10,9,7,9,6,10,3,-7,10,-8,3,4,9,4,10,2,-8,-8,-7,-10,4,-2,-3,-3,10,-2,5,2,3,-1,-7,-5,-6,-10,9,-5,-10,-10,-6,8,4,-9,-7,-2,9,5,8,9,-4,-6,-10,6,8,5,-8,-7,2,-1,7,9,-7,-1,4,-9,-2,-1,-6,4,-4,-5,3,-7,8,-2,-1,2,-5,5,5,-8,-8,9,6,7,6,2,-4,2,7,10,7,10,-6,-3,-10,10,-2,4,-6,-9,3,-10,2,-10,10,-9,-3,-10,5,-2,6,4,2,-5,-9,1,-6,6,4,7,7,2,-6,-10,6,7,-5,10,-9,8,-7,-9,-1,-1,2,-9,-5,-8,5,-3,2,-3,-10,-6,7,-8,-4,-7,1,-10,-7,1,-1,-2,-9,-7,4,-7,4,5,7,4,-8,4,1,2,4,10,4,-4,-7,-3,-3,-9,-2,-6,8,10,-3,7,10,-9,-5,-4,1,4,-8,-2,9,-6,6,2,2,-9,-8,-6,-8,-7,-6,-3,-6,8,6,-5,-9,-6,2,8,9,8,6,8,-3,-6,-3,-7,-8,4,-2,10,9,8,-5,-7,6,2,9,3,-2,-10,-7,-5,-9,8,-10,-7,-6,2,3,-6,3,8,-7,-6,1,-5,3,3,10,5,2,9,-7,7,-10,-9,-2,-9,-2,-1,8,-1,-7,5,8,7,4,-7,-9,-2,-9,4,-10,2,5,-4,9,-6,-10,6,-2,7,1,8,-8,8,1,-1,-2,-2,-6,10,2,4,8,1,2,-8,1,2,-4,7,2,-8,-10,-1,-9,-2,8,4,-5,-8,2,-2,9,2,-8,-3,-8,-3,3,3,-7,-4,2,-3,-4,5,-4,-9,-3,-10,-10,1,6,-6,-10,-3,-5,-1,7,-3,-2,7,5,3,-6,1,6,4,8,10,-1,4,-10,-3,7,-9,4,9,9,9,2,1,-2,1,9,7,-4,5,3,2,6,1,7,-7,-1,-4,-6,3,2,-9,5,10,-4,5,5,-9,9,8,1,2,4,7,3,-2,-3,-5,-5,-10,-1,8,2,-4,-1,-7,-8,4,-7,3,-10,6,-6,-4,7,1,8,-2,9,1,8,2,-1,9,-7,7,-9,-3,-3,5,-10,7,-6,-6,7,-4,-7,1,3,5,4,7,6,-10,6,10,2,2,8,-6,9,-8,-6,-4,10,-9,3,10,6,10,-5,-6,10,8,9,-3,-4,5,-1,-1,8,9,-7,-3,-1,5,-5,-5,-10,-3,5,-9,8,-8,-3,-3,-8,2,-1,8,-8,-8,-3,-6,-3,4,-6,8,-5,6,-5,8,-9,-1,-5,-2,2,-4,2,8,2,5,4,-3,-2,-8,-7,-2,-9,7,-2,5,-1,-8,10,10,9,1,1,-4,-2,-9,1,5,2,3,3,9,8,6,-3,-9,2,-8,3,-3,6,-6,-3,8,3,1,-9,9,-8,-5,-1,-5,-4,5,5,-4,10,-10,1,8,9,-1,10,6,-6,10,7,10,6,-1,-3,-4,7,6,3,-3,3,-3,-5,-2,-1,-10,-8,10,-8,-7,-7,4,8,-1,5,-5,7,3,8,3,-10,8,5,-1,10,-4,10,1,9,1,6,-2,6,5,3,-5,-2,10,-2,10,9,-9,3,7,3,-6,5,-4,-5,7,8,2,7,-7,3,1,3,-10,-1,6,6,7,-2,-2,-9,-7,-3,8,3,10,-5,5,-4,-4,-4,1,4,1,8,-3,4,-5,-10,-8,-10,-8,-3,5,-2,4,-9,5,-2,9,2,10,-3,5,-8,8,-3,-5,3,-6,8,8,5,-1,2,1,-2,-1,4,10,-9,3,9,2,7,5,-8,-3,10,1,3,-7,-1,-2,4,-8,-4,-9,-9,3,9,-1,2,-9,5,-6,2,-7,-2,9,-3,-3,9,2,-2,-4,-4,9,9,10,-10,4,10,4,-10,-9,1,4,1,6,10,8,6,-1,7,-9,-8,10,4,-9,8,-9,-10,-7,-8,6,-4,1,-2,-3,6,8,4,-3,2,3,1,-7,5,-2,8,1,4,9,6,7,-3,7,2,6,-3,-4,-10,-7,-6,10,-9,-3,4,-1,8,-6,2,10,5,-6,2,-7,2,1,-3,1,3,6,-7,-2,4,8,3,-10,2,9,7,-10,7,6,-2,3,2,-5,-8,-6,2,8,1,-4,-5,9,-10,-2,10,-9,6,8,-3,7,-7,-4,6,-6,2,-10,-4,9,-7,3,1,-2,3,-5,2,-8,4,1,3,-6,9,2,-4,9,3,3,-3,-1,4,3,-7,-8,-10,-10,8,8,2,3,10,-1,6,-7,6,5,5,7,-10,2,4,3,-7,-9,2,7,8,4,-2,4,2,-8,-9,6,10,9,9,-5,-6,7,10,7,4,3,6,-3,-7,3,6,5,-7,-1,10,-3,2,-2,6,2,3,-5,1,7,-9,-5,-10,-2,-9,-3,8,-5,8,5,-7,5,10,-10,9,2,8,4,10,-4,8,-7,-5,-9,10,-8,-8,-8,6,1,5,-7,1,-10,-9,9,4,-6,-8,4,6,4,9,-4,10,-2,1,10,1,2,-4,9,-8,-9,-9,-4,-6,-3,-10,10,4,-7,-3,6,4,-6,-8,-10,-2,-3,-1,10,-5,2,1,7,6,-10,-8,-3,-2,-5,-3,-7,4,-8,6,2,-2,-9,6,6,-10,9,3,-4,-10,-7,4,10,3,4,-7,-5,1,-1,1,-7,6,-3,-9,-3,-6,1,-4,1,-10,-1,9,7,-1,7,8,5,1,4,-2,8,-7,1,4,1,5,3,7,6,-10,9,6,-5,-9,10,6,-1,-8,6,-4,-6,-10,-5,-2,-6,1,-2,9,-7,-4,4,-4,3,-9,6,6,2,-2,3,-7,6,-6,6,-6,6,1,-2,-6,1,-5,-9,-8,9,8,-5,2,-3,-2,4,6,-1,-9,-4,-9,-10,-1,-5,10,2,-5,2,-10,6,6,3,-9,8,5,-2,-8,-9,1,-9,-8,-8,-8,2,5,-2,-5,2,-7,-1,4,-9,8,-1,-1,-10,1,-4,8,7,-2,-4,-1,-1,9,-3,5,-3,-9,4,5,1,-3,5,10,7,-10,-9,9,1,1,-9,5,3,-8,-4,-10,1,9,-5,7,-1,4,7,-1,9,2,2,4,1,-2,-7,1,6,-3,1,4,6,-5,1,-1,9,2,1,9,-6,-7,3,-10,-10,-9,-2,4,-1,2,4,-4,-7,8,-10,9,6,-10,4,8,-2,4,10,-1,6,4,-9,4,-3,-3,9,-1,-10,6,1,-7,-10,7,10,10,-3,9,-3,7,5,-10,-4,1,-4,-7,10,-7,8,10,-4,-7,7,9,8,7,-10,8,-10,9,6,8,-3,-6,-9,-10,-9,9,10,5,6,1,-8,1,10,1,-7,3,2,-10,8,-3,6,4,-10,5,-2,3,7,-10,-5,6,10,1,-1,-4,-10,9,-8,1,3,-5,2,6,5,8,-7,-1,4,-10,2,5,2,5,6,-10,-2,5,-7,5,7,10,-10,4,5,-10,-9,-7,10,10,10,6,-7,9,-9,3,-10,3,-8,-5,-10,-7,3,-9,10,8,1,5,4,-1,-8,1,1,-1,1,-1,-2,-8,-6,9,-8,7,2,9,-6,9,9,6,-5,1,3,-5,-2,-2,-3,4,10,3,3,-8,-4,-5,-8,-5,5,7,9,5,-8,-8,9,-2,-3,-1,-7,-5,5,-8,-8,5,10,-3,5,-10,6,4,2,-6,-1,1,-7,2,6,-4,4,10,-1,-3,-1,-1,-3,-4,-3,9,-7,-5,-7,-6,-9,-7,-10,-7,8,-9,-4,-7,9,1,-4,-7,3,7,1,2,4,10,-6,6], dtype = "uint8")#candidate|7669|(1664,)|const|uint8
call_7668 = relay.TupleGetItem(func_4899_call(relay.reshape(const_7669.astype('uint8'), [8, 13, 16])), 0)
call_7670 = relay.TupleGetItem(func_4902_call(relay.reshape(const_7669.astype('uint8'), [8, 13, 16])), 0)
func_7504_call = mod.get_global_var('func_7504')
func_7505_call = mutated_mod.get_global_var('func_7505')
call_7681 = relay.TupleGetItem(func_7504_call(), 0)
call_7682 = relay.TupleGetItem(func_7505_call(), 0)
bop_7698 = relay.not_equal(const_7669.astype('bool'), relay.reshape(call_7681.astype('bool'), relay.shape_of(const_7669))) # shape=(1664,)
bop_7701 = relay.not_equal(const_7669.astype('bool'), relay.reshape(call_7682.astype('bool'), relay.shape_of(const_7669))) # shape=(1664,)
uop_7709 = relay.cosh(const_7669.astype('float64')) # shape=(1664,)
output = relay.Tuple([call_7642,call_7668,bop_7698,uop_7709,])
output2 = relay.Tuple([call_7643,call_7670,bop_7701,uop_7709,])
func_7717 = relay.Function([], output)
mod['func_7717'] = func_7717
mod = relay.transform.InferType()(mod)
output = func_7717()
func_7718 = relay.Function([], output)
mutated_mod['func_7718'] = func_7718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_7805 = relay.TupleGetItem(func_2016_call(), 1)
call_7806 = relay.TupleGetItem(func_2017_call(), 1)
func_4328_call = mod.get_global_var('func_4328')
func_4329_call = mutated_mod.get_global_var('func_4329')
call_7818 = relay.TupleGetItem(func_4328_call(), 0)
call_7819 = relay.TupleGetItem(func_4329_call(), 0)
func_248_call = mod.get_global_var('func_248')
func_251_call = mutated_mod.get_global_var('func_251')
const_7821 = relay.const([5,-5,-10,-7,4,7,5,-6,1,-2,-9,-7,10,9,3,10,-1,-10,6,9,-5,-7,2,1,-9,6,-5,-1,2,-2,7,2,-6,1,2,-2,-8,-9,4,4,4,-1,5,-3,-9,2,8,-6,-6,6,8,-9,9,-9,-8,6,4,-1,9,-6,9,-6,1,1,10,-9,9,7,6,1,-10,7,6,5,-4,-4,10,-1,-2,2,4,-10,-9,-1,4,10,10,-8,-9,-2,5,-5,-5,-7,1,-9,-3,5,8,7,-9,4,8,6,6,-8,3,7,2,-5,7,5,4,2,-8,-2,7,6,9,-3,-1,9,6,4,-1,-10,-4,8,7,-10,8,9,9,3,9,-4,-8,-4,8,-4,-6,9,1,10,7,10,1,3,7,7,-3,-6,-3,-5,10,-3,-6,-8,2,-3,-7,6,-4,-5,4,-9,-2,-8,-7,9,-2,6,7,-5,4,-7,4,-7,2,-1,4,3,-5,3,4,1,-6,-6,-3,-3,-10,7,6,2,6,6,3,5,10,2,-4,2,2,-5,8,3,10,1,4,6,9,9,1,2,6,5,-6,9,4,6,-4,1,-9,-4,10,-6,-1,-2,10,4,-7,5,-8,5,10,6,-10,-2,9,-5,-3,7,5,6,5,-3,-1,-10,-5,-2,4,-3,-7,5,-8,-5,9,-6,-5,-10,-4,-5,-1,5,7,3,9,10,-10,2,-5,-10,10,9,-10,-6,-3,-1,-5,2,-6,-5,-2,1,-10,-1,-9,-9,7,-6,8,1,-4,-8,1,-1,9,-3,3,-5,6,-7,-7,4,6,-10,4,8,8,-7,9,5,7,1,2,4,9,3,-10,9,8,2,5,-10,-7,-9,8,-6,-3,-7,-10,3,4,5,-4,2,8,-4,4,-3,4,9,9,6,-2,-7,6,2,-7,-4,5,-10,9,-3,9,-4,-1,4,-8,-2,-5,-3,-8,-1,-5,-3,-2,-3,-9,4,6,3,-2,-7,-7,-3,7,-3], dtype = "uint64")#candidate|7821|(378,)|const|uint64
call_7820 = func_248_call(relay.reshape(const_7821.astype('uint64'), [9, 14, 3]), relay.reshape(const_7821.astype('uint64'), [9, 14, 3]), )
call_7822 = func_248_call(relay.reshape(const_7821.astype('uint64'), [9, 14, 3]), relay.reshape(const_7821.astype('uint64'), [9, 14, 3]), )
output = relay.Tuple([call_7805,call_7818,call_7820,const_7821,])
output2 = relay.Tuple([call_7806,call_7819,call_7822,const_7821,])
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
func_3409_call = mod.get_global_var('func_3409')
func_3411_call = mutated_mod.get_global_var('func_3411')
call_7827 = func_3409_call()
call_7828 = func_3409_call()
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_7837 = relay.TupleGetItem(func_3234_call(), 0)
call_7838 = relay.TupleGetItem(func_3235_call(), 0)
func_7083_call = mod.get_global_var('func_7083')
func_7085_call = mutated_mod.get_global_var('func_7085')
var_7862 = relay.var("var_7862", dtype = "int32", shape = (13, 1))#candidate|7862|(13, 1)|var|int32
call_7861 = relay.TupleGetItem(func_7083_call(relay.reshape(var_7862.astype('int32'), [13,])), 3)
call_7863 = relay.TupleGetItem(func_7085_call(relay.reshape(var_7862.astype('int32'), [13,])), 3)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_7869 = relay.TupleGetItem(func_2902_call(), 0)
call_7870 = relay.TupleGetItem(func_2904_call(), 0)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
var_7885 = relay.var("var_7885", dtype = "uint8", shape = ())#candidate|7885|()|var|uint8
const_7886 = relay.const([[8,10,-5,-8,2,5,6,5,-4,-8,-9,-9,-5,8,4,4,5,4,2,-3,8,10,-4,7,-1,6,3,-2,10,4,9,-7,-2,6,-3,-8,7,-4,-3,8,-6,-6,4,7,-2,-9,1,-7,7,6,-2,-2,2,-9,8,9,-4,3,4,3,5,7,7,8,7,5,-8,-10,4,-3,7,-6,-6,-10,-3,4,-4,-3,-5,7,6,-3,1,-7,3,7,4,2,6,-10,-4,6,-9,8,-1,8,-9,6,-4,-4,4,8,7,-10,3,-2,8,4,-7,1,-9,9,-10,5,7,3,-1,9,-3,10,9,-3,-10,-2,1,-8,2,8,2,8,-5,1,3,5,-9,10,-9,-4,-9,-9,-2,1,-4,-6,6,-8,-6,-8,-8,-5,-10,-6,-9,7,9,-10,-2,-2,2,7,-3,-9,-3,-10,-10,10,1,8,-6,-9,2,3,10,2,-5,-2,-3,9,-9,-7,-3,8,2,-5,-10,3,-4,8,6,-8,9,1,-2,-8,-9,-10,1,-8,4,1,-10,8,3,-9,-5,9,-8,6,1,1,-8,-2,-6,1,-6,6,7,1,7,6,-9,-6,5,9,7,-6,8,5,10,6,8,-3,5,4,6,-5,-5,1,4,-6,9,-7,9,3,-8,7,-2,-1,-4,2,-7,4,8,3,-7,-3,8,5,2,9,10,5,8,-10,5,4,-9,-3,6,-8,-5,-1,-3,-2,-8,-4,-9,-10,-9,9,4,-3,2,9,3,10,10,-1,-10,7,-6,-6,-2,-1,-9,-4,-4,6,-4,-3,-4,-5,2,7,-10,10,7,-10,2,-1,-2,6,1,-1,8,-4,-4,-9,6,10,2,10,4,2,1,-9,-8,6,-6,6,10,-6,-10,3,-1,-10,3,-6,-9,-4,-2,1,7,-9,6,-7,-7,1,10,-3,-6,-5,2,7,8,2,-4,9,-4,-4,-8,-7,4,2,3,-4,-8,-8,-2,2,6,-1,-8,-2,1,-3,7,-3,9,6,1,-10,10,-9,-5,-2,6,-5,-4,-9,5,5,5,4,3,5,-1,-5,7,3,7,-6,1,-9,8,-3,1,4,3,-9,7,2,-3,1,1,3,-1,10,10,-10,-9,-1,8,8,3,-10,3,10,-9,7,7,7,-9,-2,8,7,-3,-8,4,-2,3,-9,4,-4,2,-4,-1,7,-1,9,8,-5,-4,2,8,5,6,8,5,6,3,-6,-2,-4,-9,10,-1,-10,9,1,8,9,-9,-5,-10,2,10,8,9,4,-9,9,1,-4,-1,-8,-10,4,-7,-4,1,-10,1,4,-4,-10,-3,2,8,6,3,-10,-2,-2,5,-6,1,-9,8,4,2,-6,5,-10,-5,4,-10,-9,-1,3,-9,4,7,-2,-7,-8,2,-3,-1,8,9,2,-8,-2,-3,7,-4,-2,6,-7,-10,-3,6,-7,-1,10,1,-7,-4,8,-2,9,-7,8,-5,-8,7,-7,-7,9,-3,6,-3,-3,-2,4,7,3,-4,-7,3,2,-7,4,-5,-4,1,10,-4,1,-3,3,10,-4,-4,-3,-8,-10,6,-3,-4,7,8,1,2,10,-9,-5,-9,-1,-2,2,9,-7,6,6,-6,7,-2,-5,-2,-10,-8,-8,-4,9,-5,-5,7,-1,-1,-4,2,8,2,2,8,5,-7,-4,3,-8,-8,-7,5,5,7,-1,-1,-6,-4,-6,-10,-10,-5,-9,-8,9,10,-1,5,10,-5,2,-2,10,-7,-10,-9,-4,-5,-3,10,10,-9,4,7,8,5,-10,8,-2,-10,10,3,4,-6,2,10,-5,-3,4,3,3,-2,6,7,-3,-10,-4,6,10,6,8,-4,-6,-4,-8,-2,8,8,-4,-1,9,9,-4,-5,8,6,7,3,-10,4,5,-1,-2,6,-1,10,-8,-7,-7,-9,-2,-3,7,-2,4,-7,4,1,-4,-1,-5,8,1,8,-8,2,-1,10,-2,7,10,4,-1,-1,3,-1,-2,-4,6,10,-6,-3,9,7,8,5,7,6,-4,2,-9,-8,3,6,1,-3,-10,5,2,9,7,9,-3,3,-2,-7,-9,-5,-6,-2,-9,-7,3,-10,-6,-4,5,9,8,7,9,2,10,2,8,-4,-1,8,3,-9,-7,5,8,-1,-8,-8,-4,-6,-6,10,-6,-3,-5,3,10,-10,6,-10,9,-3,-10,5,9,-8,-2,3,3,5,8,10,9,-5,-7,-3,6,3,-7,10,10,3,6,-9,1,-1,-1,6,-2,7,8,6,-6,-2,9,-10,-9,2,8,-6,-5,-1,7,8,-10,9,-7,-4,3,-7,-7,3,10,3,7,1,4,10,-9,3,7,9,-6,-8,-10,-1,-4,5,10,-3,7,10,-6,-7,1,6,1,-4,2,-5,-9,-1,1,-6,-6,-7,-5,-8,-9,7,4,-8,1,-9,-5,3,-1,6,2,4,-3,3,-9,-8,-6,8,6,-3,9,-10,-6,-8,-7,10,6,-7,4,4,1,-2,5,-6,-8,-10,3,-1,2,8,4,1,10,7,-8,-7,-3,7,-9,-2,4,-3,-3,7,-4,7,5,-7,5,-10,5,3,8,-9,-3,-3,-5,5,3,-3,9,4,-7,-10,7,5,-9,1,8,-6,2,-7,6,-5,6,-7,-8,-10,3,7,-1,-1,3,-10,5,2,-5,-4,-3,-1,9,-3,-8,3,-4,-1,-5,7,-6,6,3,9,-9,1,4,-10,-8,1,7,-7,-6,-5,-3,-6,-1,10,-2,-2,-4,2,4,2,-6,-8,-8,-5,-5,3,5,7,-6,10,8,9,-4,9,-7,-10,5,-6,-6,5,-1,9,2,2,3,-5,3,-10,-9,4,1,8,5,6,5,3,2,4,8,-1,7,9,-2,-6,1,6,8,-7,-8,-2,-6,2,7,-3,3,3,2,9,-4,-6,7,-6,-5,-7,5,7,4,-1,-7,-5,10,10,3,-7,-6,-1,-4,9,-9,-2,4,8,-1,1,3,8,-8,-7,-2,8,-9,3,6,-3,-6,1,-6,-2,-8,-5,-10,8,5,-9,-2,-3,7,-2,-5,10,-2,3,-2,5,7,4,-6,7,8,6,-2,8,-4,2,7,-3,5,-9,1,10,5,-7,-6,2,-10,-1,7,2,2,-5,8,-2,-5,1,-4,-6,-4,-1,7,2,10,-10,5,-10,-5,-9,-4,5,9,-7,-8,-3,-8,-1,-6,10,8,-4,-1,-3,-1,9,-3,-7,2,-7,-9,-1,7,-9,4,-10,1,-7,-2,7,3,3,10,-10,3,3,2,-6,5,-1,-7,5,-8,-10,-5,6,-3,-5,8,-7,7,-3,-3,7,8,-9,2,5,-6,-2,2,-8,6,9,-1,7,6,6,-2,-9,4,5,2,5,3,-9,-7,9,2,-9,4,-2,7,2,-2,8,-1,-1,-3,2,-8,-2,-10,10,8,-7,-5,-7,-7,-2,1,7,4,-4,-8,4,9,-1,-8,-1,8,1,4,-10,8,-2,-3,-3,-6,-4,5,-10,-6,1,10,10,-9,5,-2,4,6,-1,4,-6,10,7,-9,-10,-8,9,-5,9,-4,7,9,6,-9,4,10,6,-9,-7,-9,-3,10,-6,5,-10,8,-4,1,4,-6,5,-6,8,-3,-4,-6,9,1,10,1,-4,7,7,8,10,-10,2,6,-3,-8,3,-6,-9,-10,-4,1,1,5,-6,1,-1,-2,9,4,9,1,-6,-6,7,-6,-6,-10,-4,5,10,-7,7,5,-7,9,2,8,10,-5,-10,9,-7,-5,4,1,7,4,-7,-1,-9,-10,4,-9,4,3,-4,-3,9,-1,9,-6,8,-4,10,-9,8,10,-1,-8,4,2,2,-10,-3,-6,1,-3,-4,5,-2,5,-8,-4,3,-4,1,-4,1,-8,4,-1,5,-5,-8,-5,7,-10,2,-3,-6,-1,-5,4,10,2,-3,9,6,-9,6,-7,-1,-9,-3,-9,9,5,-6,2,10,-9,7,-3,4,7,5,3,3,10,-4,2,-10,9,-8,9,5,5,8,4,9,9,7,1,-8,3,-1,-7,-4,4,-7,3,2,3,5,1,-1,9,6,8,-10,-4,-8,9,-7,-5,9,6,8,-3,-9,9,5,-7,-8,3,-6,9,9,-5,5,3,-9,-7,-10,-10],[-3,8,8,10,-10,6,-1,-9,4,-9,3,-3,2,-1,-10,-3,1,4,-9,-7,-7,-7,9,1,8,-4,-3,-5,-9,-9,-9,-4,8,-2,-10,7,2,-8,-10,4,-10,-10,7,1,-4,-3,-5,-3,-2,-9,2,2,10,6,-10,7,-1,6,-6,2,-7,3,3,-2,-1,-9,-9,-8,2,8,-6,-3,-5,5,-4,-1,5,3,-10,-2,8,-3,-4,-5,-6,-8,9,1,10,5,-6,-7,10,8,-4,10,-4,8,-7,6,-7,8,-6,10,-9,-2,-3,6,8,5,6,4,10,8,5,3,-8,8,1,4,6,7,-6,3,8,-3,-5,4,9,5,8,7,-8,-4,4,-1,3,-10,-2,2,-2,4,-2,-3,4,6,-3,-10,6,3,9,10,3,-2,4,-5,-6,2,-1,10,2,-7,-7,-9,8,-4,-6,-2,6,-4,-5,5,-1,-3,3,-8,-7,1,10,8,-9,-9,-7,-4,3,3,8,-3,-6,-1,-8,-3,2,1,-3,-1,9,9,-1,1,10,1,-10,7,1,-5,5,-3,2,-10,-3,9,-3,2,-3,7,4,1,2,-2,-4,-1,-4,7,-10,-5,9,7,-4,5,9,-1,10,9,-10,7,9,-4,-2,-1,7,7,1,8,-2,-5,5,-6,-7,-6,-9,2,1,-10,-6,-7,-8,9,-8,-9,9,5,-9,8,-7,5,-7,3,3,-1,6,-2,-2,-8,-7,5,8,-2,1,2,-4,6,-4,-9,4,-5,-10,7,-7,6,-1,-4,9,5,-3,9,-6,9,6,6,-10,10,-8,-3,1,1,-8,-10,-8,-8,4,10,-4,9,-9,-8,5,-8,-5,8,-10,-8,1,-7,5,-1,5,-10,-2,-9,-3,9,-6,-1,-10,9,-7,10,6,-6,-5,9,-8,-10,-7,1,-9,10,-9,-8,-1,9,-3,5,-6,-10,7,10,-6,6,-1,-3,-7,-6,5,5,9,3,3,-3,8,2,1,-1,-4,2,3,-4,10,7,3,3,-6,-6,-6,-9,-2,-2,-3,-2,1,2,9,6,-7,-7,7,-2,10,-3,9,-3,-3,4,9,4,-9,-5,4,8,-8,-10,6,-7,2,-3,2,-1,-4,-2,10,2,-4,-8,2,-10,10,3,-1,-2,-10,3,-2,6,1,8,8,1,-1,-10,4,3,-9,-9,7,-5,-6,-9,-5,6,-5,-7,6,-6,-8,10,-8,5,-9,10,-6,3,5,2,-8,-4,-5,-7,9,-10,10,9,2,7,-10,9,4,-10,5,7,-4,-6,1,10,5,-7,9,-2,1,4,8,9,-7,-9,3,-4,8,-4,1,3,3,2,-7,2,-6,9,-2,-4,-7,9,-10,7,-3,8,-6,-10,2,-2,6,7,10,4,6,1,2,3,3,9,-4,9,-10,10,3,-1,6,3,-5,10,-6,5,10,-7,10,10,4,6,10,-6,-8,4,-6,-1,-3,-4,-3,6,-9,-6,-8,4,6,6,6,9,-10,7,9,10,-1,10,5,7,6,4,-2,7,-8,3,6,7,6,-5,6,-6,2,-10,9,-1,-1,-10,3,10,-2,-5,-9,-6,8,10,7,-10,-10,-3,6,-6,1,1,-3,5,-5,6,5,-7,-3,7,-2,6,7,-1,-5,1,2,2,-2,3,-9,9,8,7,4,-9,10,8,-7,10,5,2,3,3,10,3,2,3,2,3,-3,2,-10,-9,-9,-2,2,2,-5,1,10,5,9,-3,-8,-7,-9,-4,-1,-7,-4,5,-1,1,3,-3,7,-4,-8,7,3,6,-5,10,-5,-6,-6,-5,1,4,10,-6,7,-5,-7,2,-8,-2,1,1,-9,-7,2,-3,-9,-5,-4,8,-3,8,-5,1,-9,8,-5,7,8,10,-7,-2,-9,7,-10,-9,-6,-2,-5,6,-6,-5,-5,-8,4,2,-10,-10,-3,-6,-10,5,-10,-8,-10,1,9,8,8,-7,-3,-6,5,-3,10,1,-4,7,3,-1,8,-10,9,10,-1,10,8,-8,9,-3,-1,-1,1,9,3,-9,-3,7,7,7,-6,4,2,-9,3,2,-6,-1,10,3,1,4,2,-5,-1,-9,-1,5,4,6,7,3,2,-2,-5,6,8,-1,-1,1,1,1,10,-9,1,4,-5,3,3,8,10,-4,-3,-3,3,6,-2,8,-4,-8,2,5,9,3,-3,9,-6,-6,-10,-1,10,7,-6,-6,1,9,6,-9,2,-8,-4,10,2,8,4,-6,-9,-8,7,-7,-10,2,-2,2,4,1,-6,9,-7,-1,6,-7,2,2,-1,-8,7,8,2,3,1,7,3,7,-4,-2,8,7,-5,9,-8,-9,-8,2,9,9,7,9,-3,1,7,-8,-3,4,4,5,2,-6,-3,4,4,-1,-9,-3,7,10,9,8,2,1,-5,7,10,-10,2,4,7,-6,-6,-1,-5,4,8,6,-3,-8,-1,8,10,4,-3,-7,4,9,2,-2,10,1,-9,9,-1,-2,4,6,9,-6,-10,3,6,-3,-1,-7,2,-8,-2,3,-4,8,5,3,-5,6,-4,9,-10,-10,9,9,-3,2,-4,1,-10,-9,2,-10,-1,-10,7,4,-4,-6,10,-4,-4,10,-1,-9,7,-7,10,-6,6,-7,-7,-10,-5,-6,6,2,8,10,-3,10,7,-9,-7,-9,2,7,8,2,6,10,10,1,-4,-5,2,-6,-7,7,1,8,-3,-5,-2,6,-7,-9,-8,4,3,-10,-7,3,3,-7,-7,10,-9,3,-3,9,-5,6,-9,9,10,-7,6,-2,-4,-5,-3,3,9,-3,-4,4,-1,5,1,-3,1,-1,-2,8,-1,6,-6,-5,-6,-9,1,2,-6,-3,8,9,6,10,2,-5,-9,-4,-2,1,-7,8,6,1,6,-8,-10,8,8,5,4,-2,10,7,6,10,10,1,-10,7,-6,2,3,-3,8,2,7,4,-9,1,-2,-1,3,-8,4,-10,-10,8,4,6,-9,-5,-2,8,-1,9,2,-6,1,9,-1,8,3,7,-7,-1,-3,3,-5,-9,9,-2,7,7,5,-5,-7,8,-1,1,-1,-2,-9,10,-7,-2,6,-9,-3,-2,4,-5,-2,-5,9,1,-6,-4,10,-9,-10,3,-5,10,-1,-8,-10,8,-7,5,6,-8,8,7,4,7,7,4,4,-1,4,10,2,6,-8,5,-6,8,5,-2,-1,4,8,-1,-2,7,-2,10,2,3,-6,6,1,5,-9,-4,-5,10,8,6,-6,6,10,1,-1,-4,3,10,-3,-10,2,-5,-4,-10,8,2,9,-1,-5,10,7,4,3,-5,-9,-1,1,-5,10,-9,1,2,1,-6,-6,-2,-10,4,-10,-4,-4,-7,-10,1,-8,-10,-4,-9,-8,1,1,8,10,9,-10,1,7,-10,2,6,-4,9,3,-4,4,6,9,-9,7,-10,-10,-1,-9,-3,-4,3,7,7,1,-10,5,10,-1,4,10,3,5,6,-8,-6,-10,-2,2,-7,-9,8,5,9,-1,-2,-6,-1,-2,8,-8,2,-5,6,-2,-2,2,-6,-10,-2,7,-9,10,8,7,-2,2,4,8,7,-3,-4,9,-5,-4,-7,3,-8,6,-7,-1,9,-4,-5,10,-6,-2,-1,10,-9,3,7,-4,10,-10,2,-9,9,3,-8,5,-8,-6,-8,-5,5,5,-3,-9,-8,2,-2,-2,-6,2,-7,-10,4,4,-6,-8,-6,-3,1,-3,-10,-10,8,3,8,8,2,10,7,7,4,2,-8,10,6,-10,-2,9,4,-6,7,6,3,5,-2,3,10,8,2,-7,3,5,8,7,-7,-2,6,-4,-6,1,3,-7,-1,9,5,2,-5,-3,-2,-5,-3,1,-7,-10,-4,-4,-7,10,-6,-1,-6,8,9,-4,-2,-8,-8,-4,-6,9,-7,8,3,-4,-6,-9,8,-4,1,-6,9,-9,6,3,10,-3,6,-5,-7,10,-3,-6,8,-6,7,1,-9,-4,-4,7,10,2,-1,-5,-5,-2,3,7,-7,10,6,-10,2,2,-3,-3,-8,7,4,-10,4,-5,-9,8,-7,9,-10,10,5,1,10,-10,-8,10,8,1,3,1,-10,7,7,-3,-5,2,-5,-9,-6,-5,-6,8,-6]], dtype = "uint8")#candidate|7886|(2, 1560)|const|uint8
call_7884 = relay.TupleGetItem(func_813_call(relay.reshape(var_7885.astype('uint8'), []), relay.reshape(const_7886.astype('uint8'), [15, 16, 13]), ), 0)
call_7887 = relay.TupleGetItem(func_816_call(relay.reshape(var_7885.astype('uint8'), []), relay.reshape(const_7886.astype('uint8'), [15, 16, 13]), ), 0)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_7893 = relay.TupleGetItem(func_4521_call(), 0)
call_7894 = relay.TupleGetItem(func_4522_call(), 0)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_7902 = relay.TupleGetItem(func_2902_call(), 1)
call_7903 = relay.TupleGetItem(func_2904_call(), 1)
output = relay.Tuple([call_7827,call_7837,call_7861,var_7862,call_7869,call_7884,var_7885,const_7886,call_7893,call_7902,])
output2 = relay.Tuple([call_7828,call_7838,call_7863,var_7862,call_7870,call_7887,var_7885,const_7886,call_7894,call_7903,])
func_7904 = relay.Function([var_7862,var_7885,], output)
mod['func_7904'] = func_7904
mod = relay.transform.InferType()(mod)
var_7905 = relay.var("var_7905", dtype = "int32", shape = (13, 1))#candidate|7905|(13, 1)|var|int32
var_7906 = relay.var("var_7906", dtype = "uint8", shape = ())#candidate|7906|()|var|uint8
output = func_7904(var_7905,var_7906,)
func_7907 = relay.Function([var_7905,var_7906,], output)
mutated_mod['func_7907'] = func_7907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_7909 = relay.TupleGetItem(func_2902_call(), 1)
call_7910 = relay.TupleGetItem(func_2904_call(), 1)
func_7904_call = mod.get_global_var('func_7904')
func_7907_call = mutated_mod.get_global_var('func_7907')
const_7913 = relay.const([[5,-2,-9,10,9,2,3,-7,-7,-9,9,5,-4]], dtype = "int32")#candidate|7913|(1, 13)|const|int32
var_7914 = relay.var("var_7914", dtype = "uint8", shape = ())#candidate|7914|()|var|uint8
call_7912 = relay.TupleGetItem(func_7904_call(relay.reshape(const_7913.astype('int32'), [13, 1]), relay.reshape(var_7914.astype('uint8'), []), ), 6)
call_7915 = relay.TupleGetItem(func_7907_call(relay.reshape(const_7913.astype('int32'), [13, 1]), relay.reshape(var_7914.astype('uint8'), []), ), 6)
output = relay.Tuple([call_7909,call_7912,const_7913,var_7914,])
output2 = relay.Tuple([call_7910,call_7915,const_7913,var_7914,])
func_7916 = relay.Function([var_7914,], output)
mod['func_7916'] = func_7916
mod = relay.transform.InferType()(mod)
var_7917 = relay.var("var_7917", dtype = "uint8", shape = ())#candidate|7917|()|var|uint8
output = func_7916(var_7917)
func_7918 = relay.Function([var_7917], output)
mutated_mod['func_7918'] = func_7918
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7959 = relay.var("var_7959", dtype = "uint16", shape = (14, 14, 4))#candidate|7959|(14, 14, 4)|var|uint16
var_7960 = relay.var("var_7960", dtype = "uint16", shape = (14, 14, 4))#candidate|7960|(14, 14, 4)|var|uint16
bop_7961 = relay.bitwise_xor(var_7959.astype('uint16'), relay.reshape(var_7960.astype('uint16'), relay.shape_of(var_7959))) # shape=(14, 14, 4)
output = relay.Tuple([bop_7961,])
output2 = relay.Tuple([bop_7961,])
func_7972 = relay.Function([var_7959,var_7960,], output)
mod['func_7972'] = func_7972
mod = relay.transform.InferType()(mod)
var_7973 = relay.var("var_7973", dtype = "uint16", shape = (14, 14, 4))#candidate|7973|(14, 14, 4)|var|uint16
var_7974 = relay.var("var_7974", dtype = "uint16", shape = (14, 14, 4))#candidate|7974|(14, 14, 4)|var|uint16
output = func_7972(var_7973,var_7974,)
func_7975 = relay.Function([var_7973,var_7974,], output)
mutated_mod['func_7975'] = func_7975
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7982 = relay.var("var_7982", dtype = "float32", shape = (7, 15, 14))#candidate|7982|(7, 15, 14)|var|float32
var_7983 = relay.var("var_7983", dtype = "float32", shape = (7, 15, 14))#candidate|7983|(7, 15, 14)|var|float32
bop_7984 = relay.divide(var_7982.astype('float32'), relay.reshape(var_7983.astype('float32'), relay.shape_of(var_7982))) # shape=(7, 15, 14)
func_6006_call = mod.get_global_var('func_6006')
func_6008_call = mutated_mod.get_global_var('func_6008')
call_7994 = relay.TupleGetItem(func_6006_call(), 0)
call_7995 = relay.TupleGetItem(func_6008_call(), 0)
output = relay.Tuple([bop_7984,call_7994,])
output2 = relay.Tuple([bop_7984,call_7995,])
func_8011 = relay.Function([var_7982,var_7983,], output)
mod['func_8011'] = func_8011
mod = relay.transform.InferType()(mod)
mutated_mod['func_8011'] = func_8011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8011_call = mutated_mod.get_global_var('func_8011')
var_8013 = relay.var("var_8013", dtype = "float32", shape = (7, 15, 14))#candidate|8013|(7, 15, 14)|var|float32
var_8014 = relay.var("var_8014", dtype = "float32", shape = (7, 15, 14))#candidate|8014|(7, 15, 14)|var|float32
call_8012 = func_8011_call(var_8013,var_8014,)
output = call_8012
func_8015 = relay.Function([var_8013,var_8014,], output)
mutated_mod['func_8015'] = func_8015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4493_call = mod.get_global_var('func_4493')
func_4494_call = mutated_mod.get_global_var('func_4494')
call_8104 = relay.TupleGetItem(func_4493_call(), 0)
call_8105 = relay.TupleGetItem(func_4494_call(), 0)
output = call_8104
output2 = call_8105
func_8113 = relay.Function([], output)
mod['func_8113'] = func_8113
mod = relay.transform.InferType()(mod)
output = func_8113()
func_8114 = relay.Function([], output)
mutated_mod['func_8114'] = func_8114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3620_call = mod.get_global_var('func_3620')
func_3621_call = mutated_mod.get_global_var('func_3621')
call_8144 = func_3620_call()
call_8145 = func_3620_call()
func_8011_call = mod.get_global_var('func_8011')
func_8015_call = mutated_mod.get_global_var('func_8015')
var_8152 = relay.var("var_8152", dtype = "float32", shape = (1470,))#candidate|8152|(1470,)|var|float32
call_8151 = relay.TupleGetItem(func_8011_call(relay.reshape(var_8152.astype('float32'), [7, 15, 14]), relay.reshape(var_8152.astype('float32'), [7, 15, 14]), ), 0)
call_8153 = relay.TupleGetItem(func_8015_call(relay.reshape(var_8152.astype('float32'), [7, 15, 14]), relay.reshape(var_8152.astype('float32'), [7, 15, 14]), ), 0)
output = relay.Tuple([call_8144,call_8151,var_8152,])
output2 = relay.Tuple([call_8145,call_8153,var_8152,])
func_8154 = relay.Function([var_8152,], output)
mod['func_8154'] = func_8154
mod = relay.transform.InferType()(mod)
mutated_mod['func_8154'] = func_8154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8155 = relay.var("var_8155", dtype = "float32", shape = (1470,))#candidate|8155|(1470,)|var|float32
func_8154_call = mutated_mod.get_global_var('func_8154')
call_8156 = func_8154_call(var_8155)
output = call_8156
func_8157 = relay.Function([var_8155], output)
mutated_mod['func_8157'] = func_8157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6938_call = mod.get_global_var('func_6938')
func_6939_call = mutated_mod.get_global_var('func_6939')
call_8163 = relay.TupleGetItem(func_6938_call(), 0)
call_8164 = relay.TupleGetItem(func_6939_call(), 0)
func_6444_call = mod.get_global_var('func_6444')
func_6446_call = mutated_mod.get_global_var('func_6446')
var_8188 = relay.var("var_8188", dtype = "uint8", shape = (1680,))#candidate|8188|(1680,)|var|uint8
call_8187 = relay.TupleGetItem(func_6444_call(relay.reshape(var_8188.astype('uint8'), [1680,])), 2)
call_8189 = relay.TupleGetItem(func_6446_call(relay.reshape(var_8188.astype('uint8'), [1680,])), 2)
uop_8228 = relay.atanh(call_8187.astype('float32')) # shape=(14, 6, 2)
uop_8230 = relay.atanh(call_8189.astype('float32')) # shape=(14, 6, 2)
output = relay.Tuple([call_8163,var_8188,uop_8228,])
output2 = relay.Tuple([call_8164,var_8188,uop_8230,])
func_8238 = relay.Function([var_8188,], output)
mod['func_8238'] = func_8238
mod = relay.transform.InferType()(mod)
mutated_mod['func_8238'] = func_8238
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8239 = relay.var("var_8239", dtype = "uint8", shape = (1680,))#candidate|8239|(1680,)|var|uint8
func_8238_call = mutated_mod.get_global_var('func_8238')
call_8240 = func_8238_call(var_8239)
output = call_8240
func_8241 = relay.Function([var_8239], output)
mutated_mod['func_8241'] = func_8241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8273 = relay.var("var_8273", dtype = "bool", shape = ())#candidate|8273|()|var|bool
var_8274 = relay.var("var_8274", dtype = "bool", shape = (1, 8, 14))#candidate|8274|(1, 8, 14)|var|bool
bop_8275 = relay.logical_or(var_8273.astype('bool'), var_8274.astype('bool')) # shape=(1, 8, 14)
uop_8283 = relay.asinh(var_8274.astype('float32')) # shape=(1, 8, 14)
output = relay.Tuple([bop_8275,uop_8283,])
output2 = relay.Tuple([bop_8275,uop_8283,])
func_8296 = relay.Function([var_8273,var_8274,], output)
mod['func_8296'] = func_8296
mod = relay.transform.InferType()(mod)
var_8297 = relay.var("var_8297", dtype = "bool", shape = ())#candidate|8297|()|var|bool
var_8298 = relay.var("var_8298", dtype = "bool", shape = (1, 8, 14))#candidate|8298|(1, 8, 14)|var|bool
output = func_8296(var_8297,var_8298,)
func_8299 = relay.Function([var_8297,var_8298,], output)
mutated_mod['func_8299'] = func_8299
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8305 = relay.var("var_8305", dtype = "uint8", shape = ())#candidate|8305|()|var|uint8
var_8306 = relay.var("var_8306", dtype = "uint8", shape = (6, 6, 7))#candidate|8306|(6, 6, 7)|var|uint8
bop_8307 = relay.subtract(var_8305.astype('uint8'), var_8306.astype('uint8')) # shape=(6, 6, 7)
func_5495_call = mod.get_global_var('func_5495')
func_5497_call = mutated_mod.get_global_var('func_5497')
const_8321 = relay.const([3,7,-9,-10,1,-1,-5,2,8,-5,5,-2,4,8,-2,-1,4,-8,-10,-9,-10,-9,-7,4,-9,2,4,3,-7,9,7,-4,-7,3,3,-10,4,10,2,-7,-7,-3,2,-1,8,-8,-2,-7,9,8,-3,6,10,7,10,-3,2,9,3,-2,-2,7,7,4,-3,7,-3,-1,9,-4,-3,-9,2,-8,-8,5,3,3,-5,5,9,4,-8,-4,-5,7,7,1,-4,4,9,1,3,-3,10,6,3,1,5,8,4,-9,3,-10,-1,6,-8,-4,-2,-9,7,10,-5,9,6,3,-3,3,-2,-3,-9,-3,-8,8,-3,10,2,10,-3,-9,-6,-1,5,-5,8,8,-6,4,7,4,9,-10,4,-10,8,-7,4,-5,1,3,-9,7,-3,1,-3,10,9,-4,-1,-1,6,5,-6,-8,-4,6,-4,-1,4,-7,-7,10,6,-10,-2,7,-8,9,-7,-9,-10,4,-8,2,-7,8,5,-1,-3,9,-1,-5,-1,1,1,-8,-4,8,-5,1,-9,-7,8,5,-6,-9,1,4,-8,1,-4,2,-1,-8,-1,10,10,4,3,1,4,-8,4,8,-6,1,9,-8,6,-9,-6,8,-8,6,-2,3,-7,-10,3,-2,10,-9,-1,-1,2,7,-3,-4,7,-2,-8,-4,6,-7,3,-9,7,2,-2,6,-7,2,9,-10,-7,-5,9,-2,-3,-5,-2,-9,-2,-8,6,-8,8,4,7,6,-8,1,-10,4,3,2,-4,4,-2,10,-6,-2,10,4,9,9,8,-5,-2,6,8,1,-8,10,7,7,-10,-10,4,8,-1,-1,7,-1,-2,-6,-4,-4,4,-2,6,6,10,-8,9,8,-3,1,4,10,-9,-8,-5,-7,8,2,9,-2,6,-3,-6,-5,9,-8,9,1,-6,3,3,4,9,5,-6,7,9,-6,-1,1,-8,5,8,-5,4,10,10,-9,10,7,3,7,-3,6,-6,4,-7,-1,-4,3,-6,5,7,-7,10,-4,-9,4,5,-6,6,-5,10,9,-2,-1,-7,8,-2,10,10,-6,6,3,-9,-4,-10,1,-5,-1,5,9,10,-6,2,-4,-2,1,10,1,2,6,4,-1,10,-8,-6,6,4,-8,-8,9,1,-9,-6,2,-8,2,-6,1,-9,-10,5,2,-6,8,-3,3,10,6,-4,6,7,-2,-4,-8,5,9,3,-1,-2,-4,-7,2,1,-3,-8,-5,-8,-9,-3,5,-6,7,-6,10,-7,-4,1,10,-5,5,4,8,8,-4,4,-6,-4,10,1,-7,-4,3,-8,-7,9,-4,-3,-5,-10,1,-10,6,2,-3,6,3,2,7,-2,1,-8,4,-1,-4,8,7,-4,2,-9,-1,5,-4,4,5,6,7,2,7,8,4,-9,-4,2,-3,8,-5,-9,-10,-2,9,10,6,-5,7,4,-1,-2,8,-2,-6,-4,-5,-4,8,-9,-6,10,3,4,-3,1,3,-1,-1,3,-3,-10,2,3,-10,4,1,7,-1,4,-1,-10,-10,9,-3,-9,-9,-7,3,-8,2,8,-8,-7,-9,-5,-8,7,5,9,8,4,-9,8,-3,-4,10,8,8,-9,8,7,10,-6,-2,2,-5,7,9,7,-2,7,-2,10,-2,-6,4,8,9,-8,9,3,8,9,3,-9,6,7,-1,-7,-5,-3,6,4,5,8,-3,9,1,9,5,-1,4,-6,-2,-7,-4,7,-4,-7,4,-5,10,-10,-4,-5,9,-8,3,-7,7,-3,8,2,4,3,9,-6,-3,-10,-7,4,2,-8,-7,9,3,-4,-3,-3,10,-4,5,7,-6,3,-3,-9,2,-7,4,-3,-7,8,-5,-6,8,-5,-10,10,-1,-9,-3,-9,-6,2,-4,9,-1,-3,9,-3,-1,-1,-3,9,8,-10,6,6,8,4,-2,-5,-9,3,-10,-4,-7,2,-7,-5,8,-4,7,-6,7,-8,2,-5,-2,8,5,2,6,3,4,-8,5,7,-1,8,-5,-10,10,10,4,-3,-10,2,-9,-1,2,5,1,-9,7,2,-4,10,8,5,8,10,2,-5,-6,6,-6,-5,-3,7,2,9,-2,9,1,-1,-3,-8,-2,8,9,-5,-2,-10,-7,-4,-8,4,-4,-1,8,-3,-2,5,-1,-3,-6,-5,-1,3,6,6,2,6,-4,8,-1,-10,-1,-9,8,5,10,-2,9,-6,5,-8,3,-3,-5,6,4,-8,-3,-9,9,-4,-8,-8,6,-9,-6,-9,5,6,5,-5,-10,-5,-2,-3,-10,7,-3,-4,-9,-9,-2,-5,-10,-8,-5,-3,-5,-5,3,-7,-4,1,-9,8,8,4,8,8,10,-3,8,-9,4,-2,-3,10,-1,-7,-5,-8,-4,4,2,10,-7,-7,10,-8,10,-1,-8,8,-3,-10,2,1,10,8,7,-4,-2,7,-4,6,6,-5,-8,4,2,10,-3,7,-8,7,-2,10,-1,4,4,9,7,4,1,-7,-1,-4,-1,10,-6,5,-8,-10,3,-4,3,-7,-9,6,-7,10,3,2,5,-1,9,-6,2,5,9,-10,-3,3,-10,-2,3,6,-4,-9,-2,-9,-8,-7,-1,4,2,-4,-5,-6,7,3,-10,7,-9,4,-7,-2,5,5,-2,8,5,8,9,4,-4,8,-5,-7,-9,6,3,1,7,-6,5,2,3,9,-6,10,9,3,2,8,2,-7,2,-4,6,-10,3,-10,-2,10,1,9,7,3,5,-1,5,-3,-10,8,9,6,9,-10,-6,-10,-10,8,-4,-9,6,7,9,-10,9,4,5,-1,7,-5,2,3,-8,-9,4,1,-7,-3,8,-7,1,-6,3,-1,7,-5,-3,10,9,-4,-9,-5,3,7,1,-10,-5,-1,4,-9,9,-1,-2,6,2,6,-6,2,-9,5,-10,4,-1,-4,-6,7,6,-10,9,-10,9,-6,7,6,-6,-5,6,-4,4,-4,-10,8,9,4,7,10,-8,-10,-6,-10,-7,-1,-6,-10,4,5,-4,-9,2,-10,-5,-4,1,-7,-10,9,6,10,6,4,-5,3,-3,-2,-4,-5,-5,2,-3,-2,10,10,-3,7,4,9,-2,9,-3,-2,3,5,-8,-3,8,4,9,3,6,-1,-3,2,-5,3,-3,-4,-4,-6,10,3,-7,5,1,-7,-7,-9,-1,6,-3,-3,-5,3,-9,-2,-8,-6,-2,-10,8,3,-6,-6,5,-4,-2,-3,5,6,2,-1,-5,-7,8,3,5,-9,-8,9,-8,10,-9,7,-6,5,3,10,3,-8,-5,6,4,-2,-2,-4,5,8,-6,7,10,-3,2,-2,3,5,-10,9,-6,-6,3,9,-5,-3,4,4,5,-8,3,1,1,-5,9,-4,-4,-5,4,8,-5,-2,-2,-4,6,-6,-1,4,-5,2,2,10,8,-6,1,2,4,6,10,4,9,4,7,1,-8,7,-9,-7,-2,1,-4,1,7,-3,7,-5,-7,10,9,-7,4,-7,3,-2,-5,-10,6,-7,1,3,9,-8,-9,2,10,6,-5,5,-9,3,-9,-4,-6,-1,-3,9,-2,-10,-5,-10,-6,-7,1,9,10,-3,6,-6,-10,-3,9,7,-9,4,-1,-9,3,8,-9,-6,-10,9,-6,-10,10,-9,5,4,-3,8,-5,1,-4,-5,-7,-1,8,2,-5,-10,8,-5,5,9,-8,-4,-5,-2,-5,1,6,8,3,9,4,2,1,5,7,-8,10,-7,-8,-3,7,-4,7,8,1,8,1,7,7,9,-5,-8,-8,1,5,-8,9,7,3,-8,5,10,-5,-7,9,6,-5,-3,1,-1,-10,-1,5,7,-3,4,10,-3,1,7,8,-7,10,-9,4,7,3,4,-6,-5,5,-5,3,2,-8,7,-4,10,-4,3,3,1,8,1,6,2,-5,-8,5,-4,1,-8,6,9,8,-6,-3,-6,-2,-6,-5,2,5,10,-10,-10,8,5,7,1,-7,-8,-6,3,3,8,6,-2,10,1,-8,2,-1,9,-3,5,9,-10,10,-7,-1,-3,-7,-1,6,-8,3,10,8,-3,-10,-1,-2,8,-4,-4,-1,5,-1,4,6,-2,3,4,3,-2,-6,4,6,1,-6,-7,4,-5,-6,-2,3,5,8,-7,7,-4,2,10,-1,-8,-5,-3,6,-4,7,9,10,5,-1,6,10,10,9,2,10,6,6,4,9,6,-4,7,-9,9,-3,-10,7,8,10,8,1,-5,5,-9,-9,-10,2,-8,-10,-10,4,-7,-10,8,5,9,-10,-3,6,-9,8,10,9,-10,-7,-3,2,3,-4,-1,-7,-7,7,-1,-3,-9,-4,-3,-9,3,5,6,-5,-1,-9,10,-5,4,6,-4,-8,9,4,-6,-7,6,2,-1,-10,-5,-5,5,-1,-1,-6,5,-7,-5,-6,-3,-9,-7,2,7,-8,-1,7,-4,-6,-5,-9,-6,5,-9,-4], dtype = "uint8")#candidate|8321|(1680,)|const|uint8
call_8320 = relay.TupleGetItem(func_5495_call(relay.reshape(const_8321.astype('uint8'), [1680,])), 3)
call_8322 = relay.TupleGetItem(func_5497_call(relay.reshape(const_8321.astype('uint8'), [1680,])), 3)
func_2609_call = mod.get_global_var('func_2609')
func_2610_call = mutated_mod.get_global_var('func_2610')
call_8327 = relay.TupleGetItem(func_2609_call(), 0)
call_8328 = relay.TupleGetItem(func_2610_call(), 0)
output = relay.Tuple([bop_8307,call_8320,const_8321,call_8327,])
output2 = relay.Tuple([bop_8307,call_8322,const_8321,call_8328,])
func_8342 = relay.Function([var_8305,var_8306,], output)
mod['func_8342'] = func_8342
mod = relay.transform.InferType()(mod)
var_8343 = relay.var("var_8343", dtype = "uint8", shape = ())#candidate|8343|()|var|uint8
var_8344 = relay.var("var_8344", dtype = "uint8", shape = (6, 6, 7))#candidate|8344|(6, 6, 7)|var|uint8
output = func_8342(var_8343,var_8344,)
func_8345 = relay.Function([var_8343,var_8344,], output)
mutated_mod['func_8345'] = func_8345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3608_call = mod.get_global_var('func_3608')
func_3610_call = mutated_mod.get_global_var('func_3610')
call_8453 = func_3608_call()
call_8454 = func_3608_call()
func_7543_call = mod.get_global_var('func_7543')
func_7544_call = mutated_mod.get_global_var('func_7544')
call_8482 = relay.TupleGetItem(func_7543_call(), 1)
call_8483 = relay.TupleGetItem(func_7544_call(), 1)
func_1515_call = mod.get_global_var('func_1515')
func_1516_call = mutated_mod.get_global_var('func_1516')
call_8488 = relay.TupleGetItem(func_1515_call(), 0)
call_8489 = relay.TupleGetItem(func_1516_call(), 0)
func_2574_call = mod.get_global_var('func_2574')
func_2575_call = mutated_mod.get_global_var('func_2575')
call_8510 = func_2574_call()
call_8511 = func_2574_call()
output = relay.Tuple([call_8453,call_8482,call_8488,call_8510,])
output2 = relay.Tuple([call_8454,call_8483,call_8489,call_8511,])
func_8516 = relay.Function([], output)
mod['func_8516'] = func_8516
mod = relay.transform.InferType()(mod)
output = func_8516()
func_8517 = relay.Function([], output)
mutated_mod['func_8517'] = func_8517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_8528 = relay.TupleGetItem(func_1067_call(), 2)
call_8529 = relay.TupleGetItem(func_1069_call(), 2)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_8532 = relay.TupleGetItem(func_316_call(), 0)
call_8533 = relay.TupleGetItem(func_317_call(), 0)
output = relay.Tuple([call_8528,call_8532,])
output2 = relay.Tuple([call_8529,call_8533,])
func_8558 = relay.Function([], output)
mod['func_8558'] = func_8558
mod = relay.transform.InferType()(mod)
output = func_8558()
func_8559 = relay.Function([], output)
mutated_mod['func_8559'] = func_8559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2473_call = mod.get_global_var('func_2473')
func_2475_call = mutated_mod.get_global_var('func_2475')
call_8578 = func_2473_call()
call_8579 = func_2473_call()
output = relay.Tuple([call_8578,])
output2 = relay.Tuple([call_8579,])
func_8593 = relay.Function([], output)
mod['func_8593'] = func_8593
mod = relay.transform.InferType()(mod)
mutated_mod['func_8593'] = func_8593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8593_call = mutated_mod.get_global_var('func_8593')
call_8594 = func_8593_call()
output = call_8594
func_8595 = relay.Function([], output)
mutated_mod['func_8595'] = func_8595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3972_call = mod.get_global_var('func_3972')
func_3974_call = mutated_mod.get_global_var('func_3974')
call_8635 = relay.TupleGetItem(func_3972_call(), 0)
call_8636 = relay.TupleGetItem(func_3974_call(), 0)
func_8011_call = mod.get_global_var('func_8011')
func_8015_call = mutated_mod.get_global_var('func_8015')
var_8642 = relay.var("var_8642", dtype = "float32", shape = (1470,))#candidate|8642|(1470,)|var|float32
call_8641 = relay.TupleGetItem(func_8011_call(relay.reshape(var_8642.astype('float32'), [7, 15, 14]), relay.reshape(var_8642.astype('float32'), [7, 15, 14]), ), 0)
call_8643 = relay.TupleGetItem(func_8015_call(relay.reshape(var_8642.astype('float32'), [7, 15, 14]), relay.reshape(var_8642.astype('float32'), [7, 15, 14]), ), 0)
const_8648 = relay.const([0.036620,3.349193,-9.983298,-1.390400,5.144969,7.155483,3.386924,-4.471339,6.597353,3.160964,0.632348,-8.879867,-9.903226,-3.352520,-7.183493,-1.320868,8.461838,4.890076,-5.696317,-2.901019,-8.312962,3.776553,7.030386,-6.092838,-4.287279,-6.027126,3.053912,-9.630223,5.120366,9.407739,-4.366064,4.122001,0.493187,3.645078,4.783557,-2.029052,-3.480369,7.688755,8.689308,-3.250432,0.307863,6.792320,-0.403739,-3.965779,5.693853,4.748303,-2.247211,6.783778,-9.702055,4.935932,-5.928037,8.174953,4.304258,-0.887814,-7.341888,-5.634952,-2.876195,-2.698528,2.866104,-9.559755,-8.773997,-7.572339,5.418506,2.004078,6.029680,9.085290,-6.881563,-6.845885,4.189678,-1.304633,5.605373,7.458112,0.451664,-8.210198,3.557515,9.677409,4.876441,-0.459791,4.706398,-2.598478,-7.825539,-7.901731,-4.616722,2.750136,1.257047,9.457510,-3.779857,-5.699534,-4.002140,4.580305,-6.539907,-7.937305,-7.264681,-4.180140,-8.810748,-8.193450,-6.772104,5.271003,0.410715,-2.635383,-3.571431,-7.777484,-7.131344,-0.668071,8.978770,-2.781046,-8.380755,0.017712,0.825996,-9.016808,-5.398248,0.585978,6.624556,6.663751,3.971037,-6.378886,6.393534,-9.629462,4.491506,7.301880,-8.476555,-3.385423,-8.937681,-0.688233,2.552547,6.877613,3.225021,-7.308148,9.124283,-4.512166,1.703965,-8.212187,8.174807,1.282326,-1.431705,2.416586,-1.655186,2.089703,-6.580715,5.865365,0.558858,8.205181,0.292843,8.401510,-1.850384,0.075243,-1.980844,-1.422243,-5.193097,1.194351,-3.842724,-8.219748,-5.742915,6.652461,9.160952,9.829789,4.224207,0.387566,-4.246253,3.408495,-1.212916,5.479844,3.557049,-7.207856,2.957266,-8.273236,6.513439,-3.111527,-6.024263,-5.467046,-3.663891,-5.293376,-0.614005,-0.409118,6.422114,0.123382,-2.686059,-5.602171,0.152483,-9.633634,-7.179179,-6.330071,4.538010,-7.630953,7.831002,5.794685,-2.927004,3.950913,5.437792,7.432012,-9.973638,7.921031,4.385738,-6.610875,-2.728341,7.660703,2.031308,-2.519227,2.341136,-9.460791,9.205311,-8.029159,-9.640401,8.729244,-4.838002,-9.037930,2.357002,6.666794,4.036478,1.121018,-9.370988,3.649845,0.547104,-1.121134,-6.562859,0.059318,-1.928026,4.146513,6.695386,1.250701,5.874258,-2.459202,0.767343,-0.867154,8.501642,-6.288734,-0.896625,9.384219,-4.437227,-8.072961,8.537750,-8.641793,-9.367941,-3.227430,-1.845482,8.653830,5.171544,8.541256,3.785040,3.665229,8.775724,9.383466,2.011424,5.163433,-1.585267,-5.420311,8.919537,-0.054098,-5.980851,-1.769112,-7.167298,0.397423,2.502631,-0.890559,-3.919445,-7.321607,3.237353,3.118355,-6.763228,-7.897057,5.070659,-8.028747,-3.713384,-7.226576,2.543554,1.912810,-2.457987,6.159813,2.068607,-2.488017,-5.375244,-6.087681,-3.222205,-4.130796,-9.436769,-6.042969,-2.131096,1.065545,0.213308,5.485813,-7.839166,-2.447769,1.584149,-3.709571,3.323391,-6.564164,7.044339,8.800057,7.873142,1.790898,0.790289,2.945156,-8.295304,-1.145855,-7.313324,1.614994,-2.195524,6.699451,6.282618,6.622623,-8.259562,-6.626179,-1.749986,-3.259983,-3.200935,6.989380,4.245436,9.144241,9.607993,7.173830,5.670312,-7.889727,-6.439272,-5.590476,-5.635942,-9.957981,8.778973,-0.093019,-0.057311,6.838574,-6.807489,-5.728938,2.105493,-0.551477,2.820733,-7.266748,-4.702354,1.904898,-8.135866,-0.838676,5.200083,-2.906134,-6.644407,-8.796534,0.455039,8.024392,-8.115089,6.766613,6.440379,5.796212,5.303276,8.692022,-8.258489,-0.120001,-2.309483,4.490122,8.411710,7.675039,6.543572,-9.880038,1.950064,-6.976999,-5.113365,-9.394709,9.695170,-4.155382,1.867425,-6.840877,-6.957372,0.338130,-4.779274,-3.373324,-5.710070,0.025682,4.184926,-2.495781,8.719326,5.706773,-4.541811,1.904652,6.621329,-7.438445,4.144003,-3.488780,7.042383,6.796578,6.448920,4.014447,6.218782,0.647898,-3.928420,6.044050,-4.513329,6.187808,-3.935114,0.257369,1.593926,1.691810,-9.819887,-0.939948,7.844824,1.225551,-7.421367,-2.565605,6.139829,-2.374066,5.262796,3.932117,-7.148038,-3.661564,6.576820,-7.784693,3.187594,-2.483659,-2.449075,2.473081,-7.323500,-3.302739,2.893782,-2.806915,-9.830456,-0.063304,-6.140041,8.476763,6.561940,-9.520153,7.936572,6.744783,-9.948678,8.805724,-2.159367,-1.928387,2.542583,3.523948,9.638259,-1.340451,8.795554,6.570654,-1.590790,-4.533357,-5.836445,6.969810,-7.414095,-0.813533,-4.399213,6.174909,-2.702212,8.595688,-3.341718,-8.201399,-5.478317,5.246968,4.506006,8.839650,2.723466,8.140083,-4.948223,-4.488579,7.385925,0.244481,-6.408645,4.404607,-7.800694,-5.157153,3.638550,-4.989129,2.195829,0.293895,-8.859576,1.466616,1.211992,0.168154,2.982342,-9.655073,-8.981606,-0.725351,-3.021520,8.241281,-6.617542,8.954293,-4.799272,4.402029,6.259223,8.684501,7.113195,2.786863,8.371360,2.268980,-0.671166,-1.162656,1.888207,1.982511,-6.379551,6.530146,0.498084,-1.122463,-5.391676,0.031910,7.696611,-3.914525,2.269969,5.592327,-9.501549,7.687705,-4.454135,-5.600075,-9.247707,2.267286,-1.805505,6.088547,5.719509,-4.445638,1.443827,0.636838,-1.819542,-2.304811,6.634507,-7.382541,-9.147695,1.265692,8.413701,-6.558068,0.895698,-9.885460,-5.206409,0.579309,-8.802565,-2.910820,-9.705040,-0.601824,2.690071,-7.105485,-1.625023,-4.406689,6.400211,4.885186,6.677530,-0.676395,4.111943,7.276293,6.845885,3.406470,-8.785156,2.280988,0.041794,8.412637,-5.417067,8.181467,-1.941187,7.619679,3.984650,1.103953,0.715995,-8.669697,-7.285848,-0.313639,-6.972978,1.843761,4.639760,3.818656,-2.353565,9.374839,8.701237,4.910797,7.961950,2.918519,4.054028,1.123228,-4.081928,0.375453,7.564246,-1.774015,0.541915,-8.055800,1.352457,7.055631,-1.383230,-9.336726,-8.583126,-9.367834,0.141948,-5.592865,-1.219974,2.767146,5.277941,9.838486,-0.499463,9.515980,-0.438163,7.642715,4.112190,4.401962,1.556944,1.230290,-8.229239,7.344018,7.095472,-0.450277,-4.434938,6.702149,5.300704,-5.049520,-0.527038,1.770912,-8.557878,-3.934767,-9.255108,5.275397,-2.201272,9.543012,-2.753064,-2.008336,-1.733305,4.066817,-5.835607,9.463892,-1.963478,7.803727,4.364588,1.232586,8.614800,7.052857,3.455877,-4.481059,-5.555926,-7.874652,-6.330563,-2.301927,-5.328757,4.183674,-8.891340,-7.082529,9.010715,-8.923826,-2.239103,-2.207843,2.062798,1.952191,-5.927335,-4.089364,9.274483,-8.611351,4.136007,0.359366,-9.331517,-5.211149,0.977693,3.701570,6.860887,8.074595,1.266448,9.182654,4.565146,-8.257487,-0.838685,-1.971835,3.624479,-8.038266,-4.961799,-5.401765,-5.411988,3.623932,5.826092,-2.036478,-3.688189,6.428825,2.105906,6.878686,0.770762,8.281202,-0.781901,-6.792047,-3.667991,4.803100,-4.224939,7.859080,-5.131717,-7.601659,-4.955243,-9.853995,-9.421097,-8.018414,8.002384,-2.543464,6.828631,-7.712045,-2.983133,-0.440123,5.967724,0.828960,1.167317,0.952585,2.206684,-4.289411,-1.709144,2.589480,-4.218101,0.251485,0.239305,-8.263078,4.899446,-8.568277,7.916006,-7.806327,-3.544041,-5.903704,-5.602040,-7.183459,1.995616,5.632007,4.922581,-5.009549,6.647727,5.377942,-7.256076,1.006659,4.775830,9.153010,-7.230283,5.211159,9.465892,3.401990,1.337115,9.053789,-3.559339,2.031626,2.923485,0.256661,2.355300,7.319631,-0.159665,6.549821,7.756096,9.488309,-9.798349,-4.194702,-3.890327,5.517449,7.021285,3.833314,-1.412882,-0.074261,-5.785618,-7.464718,-9.441004,7.971214,-0.987214,-0.540364,5.321522,-8.147769,9.656868,8.084281,-9.988088,3.595003,-5.996527,3.009728,5.600755,-1.176100,4.395281,0.917678,2.068107,-6.218621,5.160850,8.828773,-7.858364,-4.983855,-3.071715,-6.428391,4.462920,5.495025,-0.506868,-0.794555,-5.767430,0.108116,3.003336,3.096430,-4.000767,-2.866254,2.957773,-9.121334,0.774714,2.793031,4.161111,-2.277292,5.051639,-7.686775,-3.843840,-8.122968,8.567239,-9.242573,-2.956697,1.168412,-2.136874,7.952608,2.691269,4.635249,-2.300822,0.474220,-3.847179,-4.599829,1.322986,8.368679,1.306800,-8.443212,-5.967757,0.373175,-6.696490,9.735884,1.876744,-1.850742,-0.089047,8.289132,-9.693130,-4.964558,9.476842,0.418493,0.675263,-7.927941,-7.537427,-5.585926,-9.551630,7.488305,-6.248982,4.780840,4.703200,1.057701,7.693510,9.430449,9.143725,9.370816,-1.423759,6.253264,5.189055,7.332239,-4.020307,-2.927408,7.963861,7.933322,-4.364971,5.861176,6.973056,-9.590317,-8.177849,-0.496581,6.735597,-0.983850,-4.481795,-5.725724,2.454109,4.444837,9.338897,-4.237833,-9.319652,-0.082589,-4.609734,-7.386988,-3.660868,8.271137,-8.228462,-8.471971,7.029885,-1.038338,-0.597894,5.668576,-6.260440,5.372806,5.665376,-1.703537,-8.595884,-0.742734,5.164056,-7.573312,5.166570,-2.496353,3.664346,-8.072708,4.955755,6.232444,4.175101,3.338248,9.514394,3.351359,8.567699,-9.432769,-2.408404,-9.802343,-2.801819,-1.553683,-2.128954,4.736525,9.390450,-1.106371,-7.768917,2.308634,0.577511,4.443633,3.393157,9.125003,0.292036,-3.121485,-7.542196,5.392043,1.470603,7.937711,-2.908158,-1.952268,-1.180631,-2.798821,-0.979810,-8.998216,-4.075350,-9.311625,-9.581371,-1.379872,-0.364910,9.552258,-0.446132,1.707986,-5.793909,5.839420,2.174138,3.539203,1.757925,7.443836,6.794863,9.278500,5.675853,9.979774,4.123746,2.601532,5.446912,-1.104881,0.686177,1.654313,-6.906343,-8.080504,-3.723032,1.572346,7.354753,8.426460,-1.844455,9.143594,6.311270,5.104717,-6.117640,-7.738053,-8.212124,5.527636,-4.065524,0.929041,-9.771711,-6.498555,1.284423,-4.820043,-3.696658,3.154874,-2.592860,5.374910,-1.558007,-3.245532,8.439181,-4.964424,8.983356,-5.955290,-5.516377,3.923179,2.859567,-0.154157,1.352326,-8.172119,-5.261759,3.596543,-0.885380,-7.349305,9.047341,4.659557,4.943209,-9.085445,-9.386788,-2.808406,8.406993,7.532343,-7.783038,8.926652,-5.754387,6.882366,-9.699327,0.960433,4.958900,2.459990,-9.671635,-8.700830,-0.474253,-2.272353,2.232285,5.082904,-4.775318,8.202617,-4.703061,3.456309,-3.960473,-8.705445,5.088957,6.622816,5.417965,5.864075,-3.806661,-0.618614,7.502858,5.811399,2.619335,0.341620,5.641882,-2.361426,7.840458,-7.267458,3.632068,-4.928813,-5.969045,3.682044,-3.913991,0.663371,-2.394261,3.357979,-2.590024,-2.568389,-6.597876,-3.073881,1.283822,1.755584,-4.644352,-5.424878,-8.539921,-9.663488,3.684493,9.784145,-1.131521,-7.674312,-1.279329,-0.520976,-1.366267,-2.514022,-4.624405,-7.373611,-1.937446,5.646899,8.685288,-4.160173,-5.882864,-6.115681,-1.882840,-0.433633,-5.775792,-2.503219,-0.033913,5.258134,1.233448,3.765526,-8.134704,5.426597,-7.093199,5.080746,0.331180,5.745545,-9.243803,0.917451,2.867613,-9.525694,-2.375506,-5.215569,9.774026,1.145735,-9.406329,1.963019,-2.010373,2.767662,7.392285,-2.443266,-2.911198,-8.575882,5.726864,4.204969,5.604187,-5.725490,-4.004725,8.344123,-2.983160,1.108328,7.722041,-9.342779,4.724805,-0.341667,-8.129638,2.404102,4.385663,-1.255839,1.512102,2.173167,6.649231,-1.547313,7.194024,6.403854,-9.023873,-1.771636,9.680299,6.701433,-2.565907,2.902857,-9.391653,6.500647,7.981269,-2.459869,5.075104,6.960953,6.540099,7.754590,7.775313,4.766761,8.776491,-9.379541,-9.853178,1.412767,2.697520,1.604623,-2.776328,8.520861,-6.856866,-0.977164,-9.597540,-3.601692,-6.272916,-8.784353,4.406342,9.144752,8.481841,6.437998,-8.589649,-6.101043,-4.226031,3.406215,-2.887268,-4.704114,0.447039,-0.766750,-7.545812,0.800161,-7.244414,8.330040,2.292919,-6.633952,-2.489405,-9.108719,5.685799,-2.335319,3.153430,-3.376281,7.511000,-4.253987,9.535149,-8.941881,-2.080719,-5.864214,6.774253,-9.438546,8.709918,1.943343,-6.520799,-0.276636,-9.218500,7.529388,-5.149528,7.373272,-5.794662,-7.205127,-3.590452,-9.025471,0.945730,-6.836170,-3.925458,6.449702,1.304795,2.929460,7.145471,8.841005,-1.821574,6.976958,-8.349801,-7.932736,-3.196327,7.196575,0.904320,2.644837,-1.724613,2.720845,-5.009555,-3.793365,3.885819,-9.559773,3.335088,-9.798664,-7.648370,4.652836,-6.673638,-8.292036,-0.990830,-4.976706,2.385333,-3.597793,3.934491,-8.126308,1.830047,5.001207,-4.059126,7.797264,-8.746453,8.297980,2.058983,0.444090,4.563237,-5.919479,6.605422,3.006543,0.749077,2.460750,-1.085772,-9.043896,-4.128464,-5.965255,4.285172,8.030301,-1.682799,5.508623,3.517508,9.446290,-0.215091,-8.048172,-7.851811,-6.527228,-9.020710,-0.899988,1.972601,-0.726804,9.687139,-0.372781,-0.797199,-7.020682,-7.470400,-9.641605,-3.512255,-8.593227,2.334540,6.177395,0.278280,0.364319,8.400416,-5.047316,6.906600,-1.312115,4.417814,9.133195,-9.668629,-1.519283,1.569843,-0.366906,1.250024,-5.684106,-0.536259,-5.918589,6.476005,7.473914,-9.114858,0.116323,-3.646919,-0.297381,-7.667348,3.425345,9.864899,-7.675180,-6.058283,-2.568172,5.937383,-0.677694,-0.899666,9.050310,1.735247,-9.592426,-2.684409,4.372535,-5.562969,6.388778,5.405242,7.915127,-9.362210,-3.805547,2.113890,-8.744140,9.093531,-4.749067,-0.579334,-8.965906,-0.749397,1.347000,-6.296189,5.769980,-8.336714,-7.299419,8.580441,-9.795841,5.363941,-8.910207,2.375494,4.738304,3.377862,0.858730,-5.719283,6.048959,-1.624057,4.647669,3.387238,3.566298,3.036424,-6.510837,-3.477016,7.274583,6.621973,-5.000658,-9.505428,7.795147,3.357599,1.310466,-2.926712,-4.539013,0.805012,-5.211642,-4.021588,-8.394202,4.177970,-8.636019,5.337889,6.394156,8.487786,-1.866794,4.008169,2.688735,-3.508462,-1.795687,-1.541320,3.443896,0.974573,-2.838729,-8.925704,4.405951,1.455398,3.644315,6.617743,3.946882,-4.906493,9.752725,-6.038570,-3.270260,2.422136,4.248861,0.617131,-2.644774,-2.122241,-2.029494,4.289747,-4.824425,4.733293,-9.779158,-7.410145,8.096991,5.090039,1.841209,8.536027,-1.687384,-0.566575,-0.934510,-9.979802,-5.598664,-2.767116,9.207374,0.421851,-8.016803,0.441104,1.643767,9.210984,-7.011279,5.685115,-7.546268,0.029404,-7.825590,-8.878593,0.592823,3.028428,-1.774830,-7.962058,5.417001,6.311449,-9.515405,-5.279931,0.743755,-5.444796,-9.851945,5.796919,2.023951,2.586500,-3.161488,-3.019260,4.317153,-0.907870,4.877500,6.190710,-6.789193,3.274455,-7.940806,-5.949465,4.416721,9.062424,2.503717,-0.843045,-2.601570,-6.032865,2.740191,-7.284386,-8.561773,-0.317589,-5.197924,-8.990240,0.465263,1.478849,-1.149785,1.565360,3.339558,9.321238,5.387281,8.492587,-9.832093,-3.882861,-9.289091,-1.528513,7.495413,6.199858,-0.138090,-7.242497,9.484024,4.938525,-5.710365,5.855408,-3.262645,-2.428072,-2.351198,3.836211,7.826122,-9.390420,-1.318748,-0.901874,-4.987937,8.466391,1.274840,-3.219305,-2.712303,-4.394322,-2.400157,-5.200925,6.437312,-6.289221,-7.403564,-8.190805,0.970519,6.957487,4.126243,-6.391077,5.635293,-9.780163,8.464894,8.849540,8.674995,-0.925051,4.392855], dtype = "float32")#candidate|8648|(1470,)|const|float32
bop_8649 = relay.logical_and(var_8642.astype('bool'), relay.reshape(const_8648.astype('bool'), relay.shape_of(var_8642))) # shape=(1470,)
output = relay.Tuple([call_8635,call_8641,bop_8649,])
output2 = relay.Tuple([call_8636,call_8643,bop_8649,])
func_8654 = relay.Function([var_8642,], output)
mod['func_8654'] = func_8654
mod = relay.transform.InferType()(mod)
mutated_mod['func_8654'] = func_8654
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8655 = relay.var("var_8655", dtype = "float32", shape = (1470,))#candidate|8655|(1470,)|var|float32
func_8654_call = mutated_mod.get_global_var('func_8654')
call_8656 = func_8654_call(var_8655)
output = call_8656
func_8657 = relay.Function([var_8655], output)
mutated_mod['func_8657'] = func_8657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1181_call = mod.get_global_var('func_1181')
func_1183_call = mutated_mod.get_global_var('func_1183')
call_8694 = func_1181_call()
call_8695 = func_1181_call()
output = call_8694
output2 = call_8695
func_8702 = relay.Function([], output)
mod['func_8702'] = func_8702
mod = relay.transform.InferType()(mod)
mutated_mod['func_8702'] = func_8702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8702_call = mutated_mod.get_global_var('func_8702')
call_8703 = func_8702_call()
output = call_8703
func_8704 = relay.Function([], output)
mutated_mod['func_8704'] = func_8704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8113_call = mod.get_global_var('func_8113')
func_8114_call = mutated_mod.get_global_var('func_8114')
call_8751 = func_8113_call()
call_8752 = func_8113_call()
func_7717_call = mod.get_global_var('func_7717')
func_7718_call = mutated_mod.get_global_var('func_7718')
call_8768 = relay.TupleGetItem(func_7717_call(), 1)
call_8769 = relay.TupleGetItem(func_7718_call(), 1)
func_7904_call = mod.get_global_var('func_7904')
func_7907_call = mutated_mod.get_global_var('func_7907')
const_8773 = relay.const([-6,-4,-7,-3,8,-3,8,6,-10,-3,7,9,7], dtype = "int32")#candidate|8773|(13,)|const|int32
const_8774 = relay.const(1, dtype = "uint8")#candidate|8774|()|const|uint8
call_8772 = relay.TupleGetItem(func_7904_call(relay.reshape(const_8773.astype('int32'), [13, 1]), relay.reshape(const_8774.astype('uint8'), []), ), 2)
call_8775 = relay.TupleGetItem(func_7907_call(relay.reshape(const_8773.astype('int32'), [13, 1]), relay.reshape(const_8774.astype('uint8'), []), ), 2)
output = relay.Tuple([call_8751,call_8768,call_8772,const_8773,const_8774,])
output2 = relay.Tuple([call_8752,call_8769,call_8775,const_8773,const_8774,])
func_8786 = relay.Function([], output)
mod['func_8786'] = func_8786
mod = relay.transform.InferType()(mod)
output = func_8786()
func_8787 = relay.Function([], output)
mutated_mod['func_8787'] = func_8787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2574_call = mod.get_global_var('func_2574')
func_2575_call = mutated_mod.get_global_var('func_2575')
call_8806 = func_2574_call()
call_8807 = func_2574_call()
output = relay.Tuple([call_8806,])
output2 = relay.Tuple([call_8807,])
func_8815 = relay.Function([], output)
mod['func_8815'] = func_8815
mod = relay.transform.InferType()(mod)
output = func_8815()
func_8816 = relay.Function([], output)
mutated_mod['func_8816'] = func_8816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5093_call = mod.get_global_var('func_5093')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_8847 = relay.TupleGetItem(func_5093_call(), 2)
call_8848 = relay.TupleGetItem(func_5094_call(), 2)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_8859 = func_108_call()
call_8860 = func_108_call()
func_578_call = mod.get_global_var('func_578')
func_581_call = mutated_mod.get_global_var('func_581')
call_8867 = relay.TupleGetItem(func_578_call(relay.reshape(call_8847.astype('uint64'), [378,])), 4)
call_8868 = relay.TupleGetItem(func_581_call(relay.reshape(call_8847.astype('uint64'), [378,])), 4)
output = relay.Tuple([call_8847,call_8859,call_8867,])
output2 = relay.Tuple([call_8848,call_8860,call_8868,])
func_8884 = relay.Function([], output)
mod['func_8884'] = func_8884
mod = relay.transform.InferType()(mod)
output = func_8884()
func_8885 = relay.Function([], output)
mutated_mod['func_8885'] = func_8885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_8919 = relay.TupleGetItem(func_353_call(), 1)
call_8920 = relay.TupleGetItem(func_355_call(), 1)
output = call_8919
output2 = call_8920
func_8921 = relay.Function([], output)
mod['func_8921'] = func_8921
mod = relay.transform.InferType()(mod)
mutated_mod['func_8921'] = func_8921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8921_call = mutated_mod.get_global_var('func_8921')
call_8922 = func_8921_call()
output = call_8922
func_8923 = relay.Function([], output)
mutated_mod['func_8923'] = func_8923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8949 = relay.var("var_8949", dtype = "int8", shape = (16, 8, 11))#candidate|8949|(16, 8, 11)|var|int8
const_8950 = relay.const([[[3,6,5,-5,8,-1,6,-2,-1,-4,-8],[-5,-7,-3,4,-4,7,2,-5,2,-1,-6],[-1,1,-9,-10,-9,5,-6,10,10,-9,-4],[-8,8,-4,-2,-5,1,9,-8,-7,4,3],[-10,1,9,-8,1,-3,5,7,8,-4,-5],[-8,-2,1,9,-9,9,1,-10,-10,-5,1],[10,9,7,6,-6,6,-1,7,1,1,6],[5,-10,-8,-9,7,6,-7,9,6,10,-5]],[[-10,-3,8,10,-5,-1,-1,-2,-9,-10,-4],[9,-2,1,8,-3,8,-9,9,10,6,10],[2,8,2,-6,6,-10,-2,-8,-8,-1,8],[-3,-9,2,-6,-3,-6,-10,10,5,-3,2],[-7,-10,-5,1,2,2,-1,-9,9,-7,-4],[5,5,9,8,-5,-4,-10,-5,4,-7,1],[3,4,1,-8,8,-8,-7,1,10,10,3],[5,-1,5,7,3,-5,1,8,-10,7,9]],[[7,-7,6,-1,7,6,6,3,9,-1,-5],[-2,-6,-7,-10,-4,8,4,-1,2,-2,6],[-4,-9,-7,9,7,-4,4,3,-10,3,-2],[-2,3,-3,-6,2,9,5,6,-7,7,-3],[5,-7,4,-2,8,-1,10,5,-2,6,-8],[7,-4,6,-8,-2,-6,-7,-10,9,3,-8],[-4,6,10,5,-2,-4,7,-10,9,-7,3],[-7,10,-3,-6,3,4,5,-3,1,-5,4]],[[5,6,-7,8,6,5,1,-1,8,6,5],[-5,-4,-6,3,10,5,1,10,4,-5,3],[8,3,-8,-10,-2,3,-3,-4,10,-4,1],[-7,-7,10,9,-7,7,-2,1,-2,-7,9],[-6,6,-9,3,8,-5,-10,-6,-8,7,-3],[2,1,6,-1,-9,10,-6,-8,10,-8,10],[8,10,-6,-1,6,-2,-9,6,-3,-10,-10],[3,3,3,-8,3,8,-4,-8,5,10,2]],[[6,-3,3,-4,-8,-1,10,-6,9,-6,1],[-3,-5,-5,-8,6,9,2,3,-6,-3,-5],[3,1,9,10,7,8,-4,7,-4,-5,-4],[-6,5,1,-9,8,8,-5,-7,6,10,6],[-1,-7,7,7,-9,2,4,-1,-10,6,-8],[-4,6,1,-3,2,-9,8,-9,9,9,3],[5,-8,-2,-4,5,-9,7,9,-6,-4,7],[3,9,7,5,3,5,6,4,-2,-9,10]],[[-3,-6,9,4,-3,4,-10,2,-5,5,4],[9,-3,-7,-4,-8,5,5,-5,-9,-7,10],[8,-3,9,-2,1,-3,6,9,-8,-6,1],[8,-2,4,-4,9,8,-4,1,-10,-9,9],[4,5,2,-4,7,-9,-10,10,-9,5,-10],[4,5,4,-8,9,-8,3,-10,-5,10,-5],[8,4,4,-7,-6,-4,7,-5,10,7,10],[7,7,-6,5,7,5,-3,1,-3,-2,-8]],[[-6,6,-8,-1,-2,-10,-10,6,-6,-3,6],[-1,-5,-4,3,6,4,5,-4,10,-5,-7],[-5,-4,-7,5,2,-10,4,4,5,-7,3],[-9,-8,-6,-9,10,7,-6,-1,-10,9,-2],[6,-10,-7,8,-1,-10,7,-4,9,2,-9],[10,1,5,-2,5,-2,-6,4,-2,4,3],[-9,10,2,2,2,3,4,5,4,3,-5],[-8,7,-5,3,-4,7,-8,8,2,6,1]],[[-5,7,6,-9,10,-1,7,-6,6,-3,-4],[3,5,-1,-3,2,-9,-9,-10,8,-6,-5],[-5,-5,2,3,3,7,-3,10,1,4,-2],[8,1,-1,5,2,-6,-10,-7,4,10,9],[-2,-9,-4,6,6,-7,8,-6,4,2,4],[-10,-8,4,-10,1,-3,-6,3,-4,-3,-8],[1,-5,-1,-6,-10,8,3,-6,-5,4,9],[-7,-9,3,-4,-5,6,-7,-7,-4,9,5]],[[-3,2,9,-8,-5,3,5,-8,-9,-3,2],[-4,3,8,-9,6,5,10,6,-4,-2,-5],[-5,8,-7,-10,1,10,1,7,-10,-10,1],[-8,-7,-5,1,7,-6,-9,4,-2,3,-8],[-9,-2,8,-3,-3,5,5,-10,2,10,10],[1,-9,10,4,-4,-5,-3,2,1,8,7],[5,-2,3,-7,3,1,-2,4,9,10,-6],[-6,-10,6,-2,-3,-10,-8,-7,8,-4,2]],[[9,3,-3,1,-7,-10,3,-4,10,-4,2],[-3,-6,9,-1,-7,6,-10,2,-8,8,5],[-5,8,6,-4,-5,-7,2,-2,-8,7,6],[1,-9,-6,-9,10,-10,9,-4,4,2,2],[-9,10,3,1,3,9,3,8,-8,7,-1],[-6,9,-4,-3,-6,-1,10,-4,-3,-3,8],[10,9,6,-6,2,2,3,-4,-2,-9,-9],[-7,9,9,-4,9,4,-2,6,9,-1,1]],[[7,-10,-8,-6,-7,-9,4,-10,4,4,9],[-8,5,5,8,-2,3,-6,9,7,4,4],[-3,-10,-4,-5,-2,8,-10,-5,-10,3,-7],[6,2,5,1,-8,2,3,2,-8,1,-2],[-10,-9,-4,-8,5,8,-7,-7,-10,3,5],[-9,4,-1,-3,7,-10,8,3,4,9,-7],[-4,-5,1,8,5,-3,3,3,-7,-1,-9],[8,4,9,-3,-10,-1,1,4,-8,-5,8]],[[-4,-5,-3,5,-7,3,-6,-7,-9,4,-1],[-3,-2,-5,-3,4,6,-8,8,-3,8,-8],[-8,-1,-1,8,10,8,4,1,-6,7,-6],[3,6,-1,-1,9,4,-8,-5,-7,-10,8],[-6,-3,6,4,-3,-8,-2,5,7,-5,-2],[-4,-9,-3,-5,3,2,6,6,-3,-7,-9],[-9,-4,-6,7,-2,-8,-3,-10,-4,10,10],[7,5,6,1,3,-8,6,6,6,4,10]],[[5,-8,4,-6,-5,2,-10,-4,-2,1,-5],[-7,-10,-10,-9,4,10,-2,9,3,-8,3],[-1,-9,5,-6,6,-1,8,-1,-4,10,4],[-10,-9,-6,-8,-7,8,-4,5,-1,-5,7],[8,2,-10,5,2,10,10,10,-7,-7,-2],[-5,-4,10,-3,-5,-5,-10,-7,1,-2,-5],[-7,10,-10,8,-9,1,-1,3,7,2,4],[7,1,-5,8,-5,2,10,2,4,-1,5]],[[5,6,5,-2,-4,-2,-6,7,-6,-1,-8],[10,9,1,8,-3,-3,5,-1,-7,-3,-9],[6,4,-10,8,-6,-8,-4,-8,-5,7,2],[-6,-6,-9,9,-9,5,7,-8,3,-5,10],[2,-2,-9,-6,1,-5,4,8,-3,8,-2],[-5,-10,-4,-1,-4,2,-1,7,1,1,4],[9,9,-1,-2,-4,3,3,-10,-2,9,-10],[-5,10,-4,-2,-6,-10,-5,-6,4,-1,-7]],[[-4,1,1,2,-10,10,-2,3,-3,-7,8],[4,6,-5,6,-3,8,8,4,1,-6,-4],[-5,4,-7,-3,-2,6,-6,7,2,-4,-4],[10,-2,-1,-3,-7,-1,-8,-2,1,9,-4],[-10,-9,-10,5,-3,1,-5,6,-5,-6,-5],[-7,7,-1,-9,1,3,-4,-3,7,3,3],[-10,7,1,-4,-10,-3,10,3,-8,-9,-6],[-6,-3,5,2,-5,7,10,7,-4,6,6]],[[-3,7,5,2,10,-8,-4,-10,-3,9,-9],[9,4,3,-3,7,-7,-5,10,-4,9,5],[7,10,-4,-1,9,-1,3,2,-2,-10,-3],[3,-6,6,-1,7,-8,-9,5,7,1,-6],[1,-10,4,6,-7,-1,-8,-8,-7,8,-1],[2,-8,-1,-7,1,2,-5,-1,6,-9,-1],[-3,5,-4,-9,-9,-5,10,-4,-3,-6,-8],[3,-1,-9,5,7,-1,-2,-3,-3,2,7]]], dtype = "int8")#candidate|8950|(16, 8, 11)|const|int8
bop_8951 = relay.greater_equal(var_8949.astype('bool'), relay.reshape(const_8950.astype('bool'), relay.shape_of(var_8949))) # shape=(16, 8, 11)
func_200_call = mod.get_global_var('func_200')
func_202_call = mutated_mod.get_global_var('func_202')
var_8956 = relay.var("var_8956", dtype = "uint8", shape = (1664,))#candidate|8956|(1664,)|var|uint8
call_8955 = relay.TupleGetItem(func_200_call(relay.reshape(var_8956.astype('uint8'), [8, 13, 16])), 2)
call_8957 = relay.TupleGetItem(func_202_call(relay.reshape(var_8956.astype('uint8'), [8, 13, 16])), 2)
output = relay.Tuple([bop_8951,call_8955,var_8956,])
output2 = relay.Tuple([bop_8951,call_8957,var_8956,])
func_8966 = relay.Function([var_8949,var_8956,], output)
mod['func_8966'] = func_8966
mod = relay.transform.InferType()(mod)
var_8967 = relay.var("var_8967", dtype = "int8", shape = (16, 8, 11))#candidate|8967|(16, 8, 11)|var|int8
var_8968 = relay.var("var_8968", dtype = "uint8", shape = (1664,))#candidate|8968|(1664,)|var|uint8
output = func_8966(var_8967,var_8968,)
func_8969 = relay.Function([var_8967,var_8968,], output)
mutated_mod['func_8969'] = func_8969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7717_call = mod.get_global_var('func_7717')
func_7718_call = mutated_mod.get_global_var('func_7718')
call_8981 = relay.TupleGetItem(func_7717_call(), 3)
call_8982 = relay.TupleGetItem(func_7718_call(), 3)
uop_8985 = relay.exp(call_8981.astype('float32')) # shape=(1664,)
uop_8987 = relay.exp(call_8982.astype('float32')) # shape=(1664,)
func_8593_call = mod.get_global_var('func_8593')
func_8595_call = mutated_mod.get_global_var('func_8595')
call_8988 = relay.TupleGetItem(func_8593_call(), 0)
call_8989 = relay.TupleGetItem(func_8595_call(), 0)
output = relay.Tuple([uop_8985,call_8988,])
output2 = relay.Tuple([uop_8987,call_8989,])
func_8990 = relay.Function([], output)
mod['func_8990'] = func_8990
mod = relay.transform.InferType()(mod)
output = func_8990()
func_8991 = relay.Function([], output)
mutated_mod['func_8991'] = func_8991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7309_call = mod.get_global_var('func_7309')
func_7310_call = mutated_mod.get_global_var('func_7310')
call_9022 = relay.TupleGetItem(func_7309_call(), 0)
call_9023 = relay.TupleGetItem(func_7310_call(), 0)
func_7276_call = mod.get_global_var('func_7276')
func_7278_call = mutated_mod.get_global_var('func_7278')
call_9028 = func_7276_call()
call_9029 = func_7276_call()
output = relay.Tuple([call_9022,call_9028,])
output2 = relay.Tuple([call_9023,call_9029,])
func_9045 = relay.Function([], output)
mod['func_9045'] = func_9045
mod = relay.transform.InferType()(mod)
mutated_mod['func_9045'] = func_9045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9045_call = mutated_mod.get_global_var('func_9045')
call_9046 = func_9045_call()
output = call_9046
func_9047 = relay.Function([], output)
mutated_mod['func_9047'] = func_9047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_9048 = relay.TupleGetItem(func_3234_call(), 0)
call_9049 = relay.TupleGetItem(func_3235_call(), 0)
output = call_9048
output2 = call_9049
func_9052 = relay.Function([], output)
mod['func_9052'] = func_9052
mod = relay.transform.InferType()(mod)
mutated_mod['func_9052'] = func_9052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9052_call = mutated_mod.get_global_var('func_9052')
call_9053 = func_9052_call()
output = call_9053
func_9054 = relay.Function([], output)
mutated_mod['func_9054'] = func_9054
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9069 = relay.const([[[False,True,False],[True,True,False]],[[False,False,True],[False,False,True]],[[True,True,False],[True,False,False]],[[True,True,True],[True,False,True]],[[False,True,False],[True,True,False]],[[True,True,True],[True,False,False]],[[True,True,True],[False,True,True]],[[False,False,False],[False,True,False]],[[False,True,False],[False,False,False]],[[True,True,True],[True,False,False]]], dtype = "bool")#candidate|9069|(10, 2, 3)|const|bool
var_9070 = relay.var("var_9070", dtype = "bool", shape = (10, 2, 3))#candidate|9070|(10, 2, 3)|var|bool
bop_9071 = relay.logical_and(const_9069.astype('bool'), relay.reshape(var_9070.astype('bool'), relay.shape_of(const_9069))) # shape=(10, 2, 3)
output = bop_9071
output2 = bop_9071
func_9082 = relay.Function([var_9070,], output)
mod['func_9082'] = func_9082
mod = relay.transform.InferType()(mod)
mutated_mod['func_9082'] = func_9082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9083 = relay.var("var_9083", dtype = "bool", shape = (10, 2, 3))#candidate|9083|(10, 2, 3)|var|bool
func_9082_call = mutated_mod.get_global_var('func_9082')
call_9084 = func_9082_call(var_9083)
output = call_9084
func_9085 = relay.Function([var_9083], output)
mutated_mod['func_9085'] = func_9085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2439_call = mod.get_global_var('func_2439')
func_2441_call = mutated_mod.get_global_var('func_2441')
call_9108 = func_2439_call()
call_9109 = func_2439_call()
output = relay.Tuple([call_9108,])
output2 = relay.Tuple([call_9109,])
func_9116 = relay.Function([], output)
mod['func_9116'] = func_9116
mod = relay.transform.InferType()(mod)
mutated_mod['func_9116'] = func_9116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9116_call = mutated_mod.get_global_var('func_9116')
call_9117 = func_9116_call()
output = call_9117
func_9118 = relay.Function([], output)
mutated_mod['func_9118'] = func_9118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mod.get_global_var('func_4196')
func_4198_call = mutated_mod.get_global_var('func_4198')
call_9121 = func_4196_call()
call_9122 = func_4196_call()
output = relay.Tuple([call_9121,])
output2 = relay.Tuple([call_9122,])
func_9153 = relay.Function([], output)
mod['func_9153'] = func_9153
mod = relay.transform.InferType()(mod)
output = func_9153()
func_9154 = relay.Function([], output)
mutated_mod['func_9154'] = func_9154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9052_call = mod.get_global_var('func_9052')
func_9054_call = mutated_mod.get_global_var('func_9054')
call_9173 = func_9052_call()
call_9174 = func_9052_call()
func_8702_call = mod.get_global_var('func_8702')
func_8704_call = mutated_mod.get_global_var('func_8704')
call_9206 = func_8702_call()
call_9207 = func_8702_call()
output = relay.Tuple([call_9173,call_9206,])
output2 = relay.Tuple([call_9174,call_9207,])
func_9210 = relay.Function([], output)
mod['func_9210'] = func_9210
mod = relay.transform.InferType()(mod)
output = func_9210()
func_9211 = relay.Function([], output)
mutated_mod['func_9211'] = func_9211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4156_call = mod.get_global_var('func_4156')
func_4158_call = mutated_mod.get_global_var('func_4158')
call_9265 = relay.TupleGetItem(func_4156_call(), 1)
call_9266 = relay.TupleGetItem(func_4158_call(), 1)
func_1682_call = mod.get_global_var('func_1682')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_9272 = relay.TupleGetItem(func_1682_call(), 0)
call_9273 = relay.TupleGetItem(func_1684_call(), 0)
output = relay.Tuple([call_9265,call_9272,])
output2 = relay.Tuple([call_9266,call_9273,])
func_9286 = relay.Function([], output)
mod['func_9286'] = func_9286
mod = relay.transform.InferType()(mod)
mutated_mod['func_9286'] = func_9286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9286_call = mutated_mod.get_global_var('func_9286')
call_9287 = func_9286_call()
output = call_9287
func_9288 = relay.Function([], output)
mutated_mod['func_9288'] = func_9288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8884_call = mod.get_global_var('func_8884')
func_8885_call = mutated_mod.get_global_var('func_8885')
call_9289 = relay.TupleGetItem(func_8884_call(), 0)
call_9290 = relay.TupleGetItem(func_8885_call(), 0)
func_9082_call = mod.get_global_var('func_9082')
func_9085_call = mutated_mod.get_global_var('func_9085')
var_9298 = relay.var("var_9298", dtype = "bool", shape = (3, 20))#candidate|9298|(3, 20)|var|bool
call_9297 = func_9082_call(relay.reshape(var_9298.astype('bool'), [10, 2, 3]))
call_9299 = func_9082_call(relay.reshape(var_9298.astype('bool'), [10, 2, 3]))
func_2574_call = mod.get_global_var('func_2574')
func_2575_call = mutated_mod.get_global_var('func_2575')
call_9300 = func_2574_call()
call_9301 = func_2574_call()
uop_9310 = relay.sqrt(call_9297.astype('float64')) # shape=(10, 2, 3)
uop_9312 = relay.sqrt(call_9299.astype('float64')) # shape=(10, 2, 3)
bop_9326 = relay.add(uop_9310.astype('uint64'), relay.reshape(call_9297.astype('uint64'), relay.shape_of(uop_9310))) # shape=(10, 2, 3)
bop_9329 = relay.add(uop_9312.astype('uint64'), relay.reshape(call_9299.astype('uint64'), relay.shape_of(uop_9312))) # shape=(10, 2, 3)
output = relay.Tuple([call_9289,var_9298,call_9300,bop_9326,])
output2 = relay.Tuple([call_9290,var_9298,call_9301,bop_9329,])
func_9336 = relay.Function([var_9298,], output)
mod['func_9336'] = func_9336
mod = relay.transform.InferType()(mod)
var_9337 = relay.var("var_9337", dtype = "bool", shape = (3, 20))#candidate|9337|(3, 20)|var|bool
output = func_9336(var_9337)
func_9338 = relay.Function([var_9337], output)
mutated_mod['func_9338'] = func_9338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mod.get_global_var('func_1107')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_9393 = relay.TupleGetItem(func_1107_call(), 1)
call_9394 = relay.TupleGetItem(func_1109_call(), 1)
func_7504_call = mod.get_global_var('func_7504')
func_7505_call = mutated_mod.get_global_var('func_7505')
call_9395 = relay.TupleGetItem(func_7504_call(), 0)
call_9396 = relay.TupleGetItem(func_7505_call(), 0)
output = relay.Tuple([call_9393,call_9395,])
output2 = relay.Tuple([call_9394,call_9396,])
func_9405 = relay.Function([], output)
mod['func_9405'] = func_9405
mod = relay.transform.InferType()(mod)
output = func_9405()
func_9406 = relay.Function([], output)
mutated_mod['func_9406'] = func_9406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8815_call = mod.get_global_var('func_8815')
func_8816_call = mutated_mod.get_global_var('func_8816')
call_9465 = relay.TupleGetItem(func_8815_call(), 0)
call_9466 = relay.TupleGetItem(func_8816_call(), 0)
func_1622_call = mod.get_global_var('func_1622')
func_1623_call = mutated_mod.get_global_var('func_1623')
call_9479 = func_1622_call()
call_9480 = func_1622_call()
func_3471_call = mod.get_global_var('func_3471')
func_3474_call = mutated_mod.get_global_var('func_3474')
call_9537 = func_3471_call(relay.reshape(call_9479.astype('int64'), [8, 13, 16]))
call_9538 = func_3471_call(relay.reshape(call_9479.astype('int64'), [8, 13, 16]))
func_6999_call = mod.get_global_var('func_6999')
func_7002_call = mutated_mod.get_global_var('func_7002')
var_9540 = relay.var("var_9540", dtype = "uint64", shape = (10,))#candidate|9540|(10,)|var|uint64
var_9541 = relay.var("var_9541", dtype = "uint64", shape = (120,))#candidate|9541|(120,)|var|uint64
call_9539 = relay.TupleGetItem(func_6999_call(relay.reshape(var_9540.astype('uint64'), [1, 10, 1]), relay.reshape(var_9541.astype('uint64'), [1, 10, 12]), ), 1)
call_9542 = relay.TupleGetItem(func_7002_call(relay.reshape(var_9540.astype('uint64'), [1, 10, 1]), relay.reshape(var_9541.astype('uint64'), [1, 10, 12]), ), 1)
output = relay.Tuple([call_9465,call_9479,call_9537,call_9539,var_9540,var_9541,])
output2 = relay.Tuple([call_9466,call_9480,call_9538,call_9542,var_9540,var_9541,])
func_9545 = relay.Function([var_9540,var_9541,], output)
mod['func_9545'] = func_9545
mod = relay.transform.InferType()(mod)
var_9546 = relay.var("var_9546", dtype = "uint64", shape = (10,))#candidate|9546|(10,)|var|uint64
var_9547 = relay.var("var_9547", dtype = "uint64", shape = (120,))#candidate|9547|(120,)|var|uint64
output = func_9545(var_9546,var_9547,)
func_9548 = relay.Function([var_9546,var_9547,], output)
mutated_mod['func_9548'] = func_9548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7543_call = mod.get_global_var('func_7543')
func_7544_call = mutated_mod.get_global_var('func_7544')
call_9568 = relay.TupleGetItem(func_7543_call(), 1)
call_9569 = relay.TupleGetItem(func_7544_call(), 1)
output = relay.Tuple([call_9568,])
output2 = relay.Tuple([call_9569,])
func_9576 = relay.Function([], output)
mod['func_9576'] = func_9576
mod = relay.transform.InferType()(mod)
mutated_mod['func_9576'] = func_9576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9576_call = mutated_mod.get_global_var('func_9576')
call_9577 = func_9576_call()
output = call_9577
func_9578 = relay.Function([], output)
mutated_mod['func_9578'] = func_9578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7717_call = mod.get_global_var('func_7717')
func_7718_call = mutated_mod.get_global_var('func_7718')
call_9596 = relay.TupleGetItem(func_7717_call(), 0)
call_9597 = relay.TupleGetItem(func_7718_call(), 0)
output = call_9596
output2 = call_9597
func_9616 = relay.Function([], output)
mod['func_9616'] = func_9616
mod = relay.transform.InferType()(mod)
mutated_mod['func_9616'] = func_9616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9616_call = mutated_mod.get_global_var('func_9616')
call_9617 = func_9616_call()
output = call_9617
func_9618 = relay.Function([], output)
mutated_mod['func_9618'] = func_9618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_9654 = func_2912_call()
call_9655 = func_2912_call()
output = call_9654
output2 = call_9655
func_9668 = relay.Function([], output)
mod['func_9668'] = func_9668
mod = relay.transform.InferType()(mod)
output = func_9668()
func_9669 = relay.Function([], output)
mutated_mod['func_9669'] = func_9669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4747_call = mod.get_global_var('func_4747')
func_4748_call = mutated_mod.get_global_var('func_4748')
call_9670 = func_4747_call()
call_9671 = func_4747_call()
output = relay.Tuple([call_9670,])
output2 = relay.Tuple([call_9671,])
func_9675 = relay.Function([], output)
mod['func_9675'] = func_9675
mod = relay.transform.InferType()(mod)
output = func_9675()
func_9676 = relay.Function([], output)
mutated_mod['func_9676'] = func_9676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9616_call = mod.get_global_var('func_9616')
func_9618_call = mutated_mod.get_global_var('func_9618')
call_9727 = func_9616_call()
call_9728 = func_9616_call()
output = relay.Tuple([call_9727,])
output2 = relay.Tuple([call_9728,])
func_9756 = relay.Function([], output)
mod['func_9756'] = func_9756
mod = relay.transform.InferType()(mod)
output = func_9756()
func_9757 = relay.Function([], output)
mutated_mod['func_9757'] = func_9757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mod.get_global_var('func_1107')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_9767 = relay.TupleGetItem(func_1107_call(), 0)
call_9768 = relay.TupleGetItem(func_1109_call(), 0)
output = relay.Tuple([call_9767,])
output2 = relay.Tuple([call_9768,])
func_9769 = relay.Function([], output)
mod['func_9769'] = func_9769
mod = relay.transform.InferType()(mod)
output = func_9769()
func_9770 = relay.Function([], output)
mutated_mod['func_9770'] = func_9770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6371_call = mod.get_global_var('func_6371')
func_6372_call = mutated_mod.get_global_var('func_6372')
call_9782 = relay.TupleGetItem(func_6371_call(), 2)
call_9783 = relay.TupleGetItem(func_6372_call(), 2)
func_7601_call = mod.get_global_var('func_7601')
func_7604_call = mutated_mod.get_global_var('func_7604')
var_9785 = relay.var("var_9785", dtype = "uint8", shape = (840, 2))#candidate|9785|(840, 2)|var|uint8
call_9784 = relay.TupleGetItem(func_7601_call(relay.reshape(var_9785.astype('uint8'), [1680,])), 4)
call_9786 = relay.TupleGetItem(func_7604_call(relay.reshape(var_9785.astype('uint8'), [1680,])), 4)
var_9789 = relay.var("var_9789", dtype = "uint8", shape = (7, 3, 11))#candidate|9789|(7, 3, 11)|var|uint8
bop_9790 = relay.greater_equal(call_9784.astype('bool'), var_9789.astype('bool')) # shape=(7, 3, 11)
bop_9793 = relay.greater_equal(call_9786.astype('bool'), var_9789.astype('bool')) # shape=(7, 3, 11)
func_9668_call = mod.get_global_var('func_9668')
func_9669_call = mutated_mod.get_global_var('func_9669')
call_9806 = func_9668_call()
call_9807 = func_9668_call()
output = relay.Tuple([call_9782,var_9785,bop_9790,call_9806,])
output2 = relay.Tuple([call_9783,var_9785,bop_9793,call_9807,])
func_9810 = relay.Function([var_9785,var_9789,], output)
mod['func_9810'] = func_9810
mod = relay.transform.InferType()(mod)
var_9811 = relay.var("var_9811", dtype = "uint8", shape = (840, 2))#candidate|9811|(840, 2)|var|uint8
var_9812 = relay.var("var_9812", dtype = "uint8", shape = (7, 3, 11))#candidate|9812|(7, 3, 11)|var|uint8
output = func_9810(var_9811,var_9812,)
func_9813 = relay.Function([var_9811,var_9812,], output)
mutated_mod['func_9813'] = func_9813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4374_call = mod.get_global_var('func_4374')
func_4376_call = mutated_mod.get_global_var('func_4376')
call_9819 = relay.TupleGetItem(func_4374_call(), 0)
call_9820 = relay.TupleGetItem(func_4376_call(), 0)
func_1264_call = mod.get_global_var('func_1264')
func_1266_call = mutated_mod.get_global_var('func_1266')
call_9824 = func_1264_call(relay.reshape(call_9819.astype('uint8'), [8, 13, 16]))
call_9825 = func_1264_call(relay.reshape(call_9819.astype('uint8'), [8, 13, 16]))
func_9675_call = mod.get_global_var('func_9675')
func_9676_call = mutated_mod.get_global_var('func_9676')
call_9836 = relay.TupleGetItem(func_9675_call(), 0)
call_9837 = relay.TupleGetItem(func_9676_call(), 0)
output = relay.Tuple([call_9819,call_9824,call_9836,])
output2 = relay.Tuple([call_9820,call_9825,call_9837,])
func_9851 = relay.Function([], output)
mod['func_9851'] = func_9851
mod = relay.transform.InferType()(mod)
output = func_9851()
func_9852 = relay.Function([], output)
mutated_mod['func_9852'] = func_9852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6371_call = mod.get_global_var('func_6371')
func_6372_call = mutated_mod.get_global_var('func_6372')
call_9871 = relay.TupleGetItem(func_6371_call(), 1)
call_9872 = relay.TupleGetItem(func_6372_call(), 1)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_9877 = relay.TupleGetItem(func_2902_call(), 1)
call_9878 = relay.TupleGetItem(func_2904_call(), 1)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_9883 = relay.TupleGetItem(func_1769_call(), 0)
call_9884 = relay.TupleGetItem(func_1771_call(), 0)
output = relay.Tuple([call_9871,call_9877,call_9883,])
output2 = relay.Tuple([call_9872,call_9878,call_9884,])
func_9905 = relay.Function([], output)
mod['func_9905'] = func_9905
mod = relay.transform.InferType()(mod)
output = func_9905()
func_9906 = relay.Function([], output)
mutated_mod['func_9906'] = func_9906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9915 = relay.var("var_9915", dtype = "float64", shape = (5, 8, 8))#candidate|9915|(5, 8, 8)|var|float64
uop_9916 = relay.acos(var_9915.astype('float64')) # shape=(5, 8, 8)
output = uop_9916
output2 = uop_9916
func_9919 = relay.Function([var_9915,], output)
mod['func_9919'] = func_9919
mod = relay.transform.InferType()(mod)
var_9920 = relay.var("var_9920", dtype = "float64", shape = (5, 8, 8))#candidate|9920|(5, 8, 8)|var|float64
output = func_9919(var_9920)
func_9921 = relay.Function([var_9920], output)
mutated_mod['func_9921'] = func_9921
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9951 = relay.const([[[-2,7,-4,-8,-1,-4,-6,10,-1,4,-2,2,-10,8],[-8,4,-9,-10,9,-3,4,3,2,-1,-10,2,-8,1],[-3,-2,9,3,-6,10,10,8,-1,-5,-6,6,1,-7],[2,9,-9,8,-6,6,3,-9,-9,6,10,5,-10,-4]],[[-8,-2,-9,6,3,-5,-3,10,9,9,-6,2,-8,6],[7,-1,-10,-5,-5,8,5,6,6,-3,7,7,-7,-1],[-5,5,6,-8,10,-9,4,-2,1,-6,3,-4,-3,6],[-9,7,6,7,-9,-2,10,-1,-7,5,10,-6,3,5]],[[-2,-8,-10,6,-6,-9,8,3,1,2,6,7,-9,10],[3,-9,-8,8,1,-5,-7,-3,6,-4,-9,-8,-6,-2],[-5,8,-8,5,-6,-6,-4,-6,-7,-7,5,1,-10,9],[-3,-2,3,-8,-8,9,-3,3,-7,-10,9,7,-1,-8]],[[-9,-6,7,-1,-7,-3,2,-1,6,2,-4,-8,-2,-7],[-3,-3,-1,5,4,-10,4,7,5,1,-3,-7,-7,-10],[-7,-1,1,5,2,1,5,-8,3,5,5,-1,10,7],[-2,6,3,2,-3,5,-6,-1,6,-1,7,8,1,2]],[[9,9,-8,1,-6,5,-9,-5,7,-7,5,3,-4,-6],[4,8,-9,3,4,9,6,-9,4,-9,10,-5,3,-7],[-1,-2,10,8,-7,-7,4,10,9,4,-5,-4,10,10],[-7,8,9,-5,-2,-10,-2,9,-2,6,10,5,-5,-8]],[[8,8,-6,-5,8,8,1,-8,-5,-10,6,10,-8,-1],[6,7,1,9,-2,2,4,-2,8,-9,7,-3,7,-10],[10,9,-3,8,-4,1,1,7,-3,-10,7,7,-9,6],[4,3,7,10,10,6,-4,1,-10,3,-7,8,2,-9]],[[-4,9,3,1,-3,2,8,-9,-4,-2,-1,10,7,4],[-1,-2,-10,-4,2,4,8,-1,5,1,-2,-6,5,1],[-5,-3,7,-5,4,-1,5,-4,-5,-9,6,-2,2,-9],[7,3,4,10,9,2,5,2,1,4,8,6,5,2]],[[7,8,-3,8,5,1,-5,9,-6,-1,4,5,-3,8],[1,7,1,-4,6,-2,-1,-7,5,6,7,-10,-5,3],[-8,-5,-10,8,10,8,5,-1,2,-3,-3,10,-8,-1],[7,-10,6,3,2,7,-5,-1,4,5,7,-5,-6,-2]]], dtype = "int32")#candidate|9951|(8, 4, 14)|const|int32
const_9952 = relay.const([[[2,-6,9,1,-4,-8,-4,-2,10,5,-5,9,-8,9],[-4,2,10,-3,7,-4,2,-9,2,-7,1,-6,-6,2],[-8,6,5,9,5,6,-8,5,4,-6,-7,-1,-7,-7],[-3,-7,-2,-6,10,-4,-7,-8,-3,-5,-9,5,6,-4]],[[-4,5,2,2,-4,10,-2,-2,-9,6,-5,10,1,-10],[1,9,-7,-7,-6,-4,5,-8,-2,-8,1,10,-4,-10],[6,-10,-5,6,-5,2,2,-4,2,6,4,-3,-9,-1],[-5,-7,-10,-10,8,-9,-9,-6,7,-7,-4,10,-6,-3]],[[8,-7,-4,4,3,-8,-9,4,8,-6,10,3,-6,-3],[8,9,-7,-6,1,4,-3,-5,-1,-8,-10,3,8,5],[-1,-8,4,2,4,-4,-10,-10,-3,3,5,3,8,7],[-2,-1,1,-1,-5,-8,-4,5,-1,7,10,-9,3,-2]],[[10,6,2,-6,-7,7,1,-2,-8,-9,9,-6,-5,-8],[9,-1,7,-2,5,1,-4,-5,-8,9,1,6,3,-3],[-10,-9,10,7,-7,8,6,5,2,4,6,-5,-3,-1],[4,7,4,3,5,-3,1,-6,3,-7,-3,4,-6,8]],[[-1,-4,-2,8,-6,-2,-3,3,8,-10,-1,7,-6,3],[9,1,-10,-4,-7,-10,7,4,-1,-3,6,-2,-10,1],[2,-10,-5,3,-6,-8,3,-8,2,-10,8,-3,-9,-1],[6,5,-6,-2,-5,-6,4,-6,2,7,3,-8,-3,7]],[[-8,10,-2,3,-9,-1,-2,5,-3,-2,4,-10,9,10],[-10,3,-7,1,8,-9,9,-1,-9,6,9,6,9,10],[5,-1,7,3,9,-5,-8,-5,-8,-7,-7,10,2,7],[3,1,-9,5,6,-2,-9,-3,-5,3,7,10,-4,-9]],[[-8,10,-6,-9,3,3,-1,-4,5,-7,-8,-2,4,-10],[-6,-7,-5,-6,-7,-8,-1,2,9,2,5,-2,2,7],[-10,6,-6,-8,1,-6,9,1,-6,-9,8,6,-3,-6],[4,2,-10,8,3,-9,-10,-3,10,8,-6,10,2,-7]],[[6,-1,7,-4,2,-5,10,9,10,10,7,-5,-8,-7],[10,-3,-7,7,-8,3,5,-6,3,-4,1,-2,-1,-1],[1,-9,-6,-9,7,-9,9,6,9,8,1,-6,5,1],[6,-4,2,9,-8,-10,-6,-1,-10,-10,10,2,9,2]]], dtype = "int32")#candidate|9952|(8, 4, 14)|const|int32
bop_9953 = relay.bitwise_and(const_9951.astype('int32'), relay.reshape(const_9952.astype('int32'), relay.shape_of(const_9951))) # shape=(8, 4, 14)
output = relay.Tuple([bop_9953,])
output2 = relay.Tuple([bop_9953,])
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
	relay.transform.ToBasicBlockNormalForm(),
	relay.transform.FuseOps(3),
	relay.transform.DefuseOps(),
	relay.transform.SimplifyExpr(),
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
