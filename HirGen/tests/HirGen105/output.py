import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_46 = relay.const([[[-0.564462,0.583748,5.639707,1.492711,-1.639545,-1.682306,2.512703,0.197970,-6.929666],[4.712713,-7.065476,2.531627,1.366504,-2.473108,1.818311,-3.434902,8.407530,5.683963],[6.531122,2.737515,2.489169,-7.748126,7.222184,-1.855239,-2.986897,4.355870,6.907939]],[[-1.369124,2.514992,7.078505,-7.971425,-0.922123,-9.584658,2.362949,5.139763,5.033775],[-6.297589,7.741371,2.829107,6.408458,-2.552282,-6.536453,0.499819,-3.733063,6.053143],[6.078024,6.618787,1.262440,9.627984,5.024220,9.937972,4.419635,9.314613,-6.246078]],[[2.016654,-8.939818,-5.651653,9.139965,1.200481,-2.526638,-4.382930,-1.336373,9.568369],[6.550060,-7.226905,1.763149,5.690110,-1.700104,-7.080180,9.468123,-6.965075,6.250414],[3.198733,3.192649,-2.842363,2.159178,6.459121,-0.253044,-6.040846,-5.108324,-2.229756]]], dtype = "float32")#candidate|46|(3, 3, 9)|const|float32
var_47 = relay.var("var_47", dtype = "float32", shape = (3, 3, 9))#candidate|47|(3, 3, 9)|var|float32
bop_48 = relay.less(const_46.astype('bool'), relay.reshape(var_47.astype('bool'), relay.shape_of(const_46))) # shape=(3, 3, 9)
uop_58 = relay.acos(var_47.astype('float64')) # shape=(3, 3, 9)
uop_61 = relay.sqrt(var_47.astype('float64')) # shape=(3, 3, 9)
output = relay.Tuple([bop_48,uop_58,uop_61,])
output2 = relay.Tuple([bop_48,uop_58,uop_61,])
func_69 = relay.Function([var_47,], output)
mod['func_69'] = func_69
mod = relay.transform.InferType()(mod)
var_70 = relay.var("var_70", dtype = "float32", shape = (3, 3, 9))#candidate|70|(3, 3, 9)|var|float32
output = func_69(var_70)
func_71 = relay.Function([var_70], output)
mutated_mod['func_71'] = func_71
mutated_mod = relay.transform.InferType()(mutated_mod)
const_78 = relay.const([[[-3.298595,6.232101,-8.300504,9.530403,-1.367764,-8.897248,6.566900,7.854646,1.431828],[-6.514146,-8.274773,6.316390,0.359152,6.957058,-6.871269,3.230296,1.777285,-0.163235],[2.936992,6.603064,5.747590,-7.530230,-2.862050,9.801768,8.647496,0.211256,-4.602689],[-0.854081,0.248305,0.110276,-3.190123,1.549634,8.434431,-4.318945,8.054270,-0.270404],[9.402263,0.505434,-2.725608,0.236855,7.128997,1.339568,-6.447229,7.174834,8.706613],[9.533650,8.308835,-0.751696,9.615491,6.029203,-2.762195,9.977886,0.983694,8.427776],[5.052804,7.283791,3.424288,4.427847,-4.037833,-7.203679,4.450859,-9.888295,-8.139639],[4.084385,3.040329,-4.731853,-1.665436,5.161895,-0.206448,0.531256,-4.583260,-0.147331],[3.360893,3.008082,-7.327342,-4.308816,2.808591,-9.778515,3.973503,8.795229,8.911055],[-8.278552,-1.293084,7.324308,4.901819,-7.010451,5.501847,6.235794,-2.627093,0.513049],[-2.084767,-7.220515,-1.381982,1.174376,-7.420434,-1.259729,-0.882612,1.273031,-8.157402],[-8.675591,1.463686,0.100044,2.556777,-4.436543,4.595326,5.214207,7.337993,-1.930555],[-3.272867,2.051657,-8.689958,-3.972092,-9.638877,8.000462,-7.986710,-6.650396,8.129861],[3.427084,4.721919,-1.329012,7.256035,-2.795051,-1.315531,-1.598414,1.872516,8.161230],[9.761774,-1.340877,-9.443678,-0.925307,8.982849,-2.557842,9.524833,-4.370175,1.029712]]], dtype = "float32")#candidate|78|(1, 15, 9)|const|float32
uop_79 = relay.rsqrt(const_78.astype('float32')) # shape=(1, 15, 9)
output = uop_79
output2 = uop_79
func_100 = relay.Function([], output)
mod['func_100'] = func_100
mod = relay.transform.InferType()(mod)
mutated_mod['func_100'] = func_100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_100_call = mutated_mod.get_global_var('func_100')
call_101 = func_100_call()
output = call_101
func_102 = relay.Function([], output)
mutated_mod['func_102'] = func_102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_111 = func_100_call()
call_112 = func_100_call()
output = call_111
output2 = call_112
func_124 = relay.Function([], output)
mod['func_124'] = func_124
mod = relay.transform.InferType()(mod)
output = func_124()
func_125 = relay.Function([], output)
mutated_mod['func_125'] = func_125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_135 = func_100_call()
call_136 = func_100_call()
output = relay.Tuple([call_135,])
output2 = relay.Tuple([call_136,])
func_139 = relay.Function([], output)
mod['func_139'] = func_139
mod = relay.transform.InferType()(mod)
output = func_139()
func_140 = relay.Function([], output)
mutated_mod['func_140'] = func_140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_180 = relay.TupleGetItem(func_139_call(), 0)
call_181 = relay.TupleGetItem(func_140_call(), 0)
uop_182 = relay.log10(call_180.astype('float32')) # shape=(1, 15, 9)
uop_184 = relay.log10(call_181.astype('float32')) # shape=(1, 15, 9)
func_69_call = mod.get_global_var('func_69')
func_71_call = mutated_mod.get_global_var('func_71')
var_188 = relay.var("var_188", dtype = "float32", shape = (81,))#candidate|188|(81,)|var|float32
call_187 = relay.TupleGetItem(func_69_call(relay.reshape(var_188.astype('float32'), [3, 3, 9])), 2)
call_189 = relay.TupleGetItem(func_71_call(relay.reshape(var_188.astype('float32'), [3, 3, 9])), 2)
output = relay.Tuple([uop_182,call_187,var_188,])
output2 = relay.Tuple([uop_184,call_189,var_188,])
func_190 = relay.Function([var_188,], output)
mod['func_190'] = func_190
mod = relay.transform.InferType()(mod)
var_191 = relay.var("var_191", dtype = "float32", shape = (81,))#candidate|191|(81,)|var|float32
output = func_190(var_191)
func_192 = relay.Function([var_191], output)
mutated_mod['func_192'] = func_192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_229 = func_100_call()
call_230 = func_100_call()
uop_260 = relay.log(call_229.astype('float32')) # shape=(1, 15, 9)
uop_262 = relay.log(call_230.astype('float32')) # shape=(1, 15, 9)
bop_268 = relay.floor_mod(uop_260.astype('float64'), relay.reshape(call_229.astype('float64'), relay.shape_of(uop_260))) # shape=(1, 15, 9)
bop_271 = relay.floor_mod(uop_262.astype('float64'), relay.reshape(call_230.astype('float64'), relay.shape_of(uop_262))) # shape=(1, 15, 9)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_285 = func_100_call()
call_286 = func_100_call()
func_124_call = mod.get_global_var('func_124')
func_125_call = mutated_mod.get_global_var('func_125')
call_290 = func_124_call()
call_291 = func_124_call()
func_124_call = mod.get_global_var('func_124')
func_125_call = mutated_mod.get_global_var('func_125')
call_292 = func_124_call()
call_293 = func_124_call()
bop_302 = relay.multiply(uop_260.astype('int8'), relay.reshape(call_285.astype('int8'), relay.shape_of(uop_260))) # shape=(1, 15, 9)
bop_305 = relay.multiply(uop_262.astype('int8'), relay.reshape(call_286.astype('int8'), relay.shape_of(uop_262))) # shape=(1, 15, 9)
bop_318 = relay.mod(bop_302.astype('float64'), relay.reshape(bop_268.astype('float64'), relay.shape_of(bop_302))) # shape=(1, 15, 9)
bop_321 = relay.mod(bop_305.astype('float64'), relay.reshape(bop_271.astype('float64'), relay.shape_of(bop_305))) # shape=(1, 15, 9)
func_69_call = mod.get_global_var('func_69')
func_71_call = mutated_mod.get_global_var('func_71')
var_325 = relay.var("var_325", dtype = "float32", shape = (81,))#candidate|325|(81,)|var|float32
call_324 = relay.TupleGetItem(func_69_call(relay.reshape(var_325.astype('float32'), [3, 3, 9])), 0)
call_326 = relay.TupleGetItem(func_71_call(relay.reshape(var_325.astype('float32'), [3, 3, 9])), 0)
uop_334 = relay.log2(call_285.astype('float32')) # shape=(1, 15, 9)
uop_336 = relay.log2(call_286.astype('float32')) # shape=(1, 15, 9)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_348 = func_100_call()
call_349 = func_100_call()
output = relay.Tuple([call_290,call_292,bop_318,call_324,var_325,uop_334,call_348,])
output2 = relay.Tuple([call_291,call_293,bop_321,call_326,var_325,uop_336,call_349,])
func_352 = relay.Function([var_325,], output)
mod['func_352'] = func_352
mod = relay.transform.InferType()(mod)
mutated_mod['func_352'] = func_352
mutated_mod = relay.transform.InferType()(mutated_mod)
var_353 = relay.var("var_353", dtype = "float32", shape = (81,))#candidate|353|(81,)|var|float32
func_352_call = mutated_mod.get_global_var('func_352')
call_354 = func_352_call(var_353)
output = call_354
func_355 = relay.Function([var_353], output)
mutated_mod['func_355'] = func_355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_394 = relay.TupleGetItem(func_139_call(), 0)
call_395 = relay.TupleGetItem(func_140_call(), 0)
output = relay.Tuple([call_394,])
output2 = relay.Tuple([call_395,])
func_396 = relay.Function([], output)
mod['func_396'] = func_396
mod = relay.transform.InferType()(mod)
output = func_396()
func_397 = relay.Function([], output)
mutated_mod['func_397'] = func_397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_124_call = mod.get_global_var('func_124')
func_125_call = mutated_mod.get_global_var('func_125')
call_411 = func_124_call()
call_412 = func_124_call()
output = relay.Tuple([call_411,])
output2 = relay.Tuple([call_412,])
func_414 = relay.Function([], output)
mod['func_414'] = func_414
mod = relay.transform.InferType()(mod)
output = func_414()
func_415 = relay.Function([], output)
mutated_mod['func_415'] = func_415
mutated_mod = relay.transform.InferType()(mutated_mod)
const_438 = relay.const([[[6.381927,-9.076200,7.923965,-4.710216,-7.301513,0.775296,-3.497146],[2.171635,-1.415947,-2.032613,2.737998,3.803747,-5.037660,6.774326],[3.974357,7.667634,2.057212,7.768936,8.421371,7.280691,-3.693212],[-2.119232,9.562435,5.451508,-8.094521,6.783103,-6.638655,-5.416486],[5.046715,-3.551419,0.800579,4.808592,7.211964,3.492089,6.114165],[-4.017818,4.825136,-0.643027,-5.322686,6.564483,-9.545386,-4.847715],[3.025434,2.216297,-5.869619,9.966726,7.315617,-2.917484,-1.940322],[0.396561,6.094318,6.975497,-6.351515,2.798566,1.017746,-4.592292]],[[4.181536,-1.740763,8.089083,4.759406,2.899043,7.688946,-6.299014],[5.532383,3.365110,-1.268059,3.303907,-5.343930,6.549709,-8.146238],[-8.012172,-8.608969,-0.961059,-3.538671,-3.237663,5.393827,8.090735],[-6.578207,4.565232,-7.786611,-6.023637,1.587340,-1.774453,-1.544086],[5.708877,-0.312254,1.794118,4.193334,9.197173,0.166707,-0.200666],[3.347967,-8.105067,4.558406,8.784361,-5.238155,-5.360295,9.939944],[7.041341,-3.741991,9.002342,-5.875185,-0.917041,-0.797748,-7.777759],[1.909042,-8.544007,-6.530093,0.945809,-5.811196,4.785517,-1.960909]],[[-7.564198,-2.871838,0.029701,-5.812436,9.901726,2.302764,1.805240],[5.736219,-7.301140,-6.104961,2.277312,2.061719,-3.240605,5.859460],[-9.808548,4.386519,-7.341530,0.895663,-4.858495,-5.053299,-4.156163],[2.590965,2.481615,4.183875,-3.232795,-1.182097,-9.833972,-4.341181],[-9.103451,-4.747669,8.541321,2.663057,9.892445,-2.555518,6.904510],[0.173381,-8.527476,2.414103,8.544914,9.355704,-2.942834,3.937041],[6.618837,6.887183,-8.679464,4.007283,0.440898,0.094826,4.072873],[-8.747286,-0.080014,-5.109238,5.376509,-1.099853,9.487847,-2.632109]],[[5.315599,-8.974228,6.301384,-2.602623,-8.923021,7.803737,7.856431],[-5.559523,-4.356057,1.215283,8.645229,-7.294111,9.181597,2.681271],[-4.697811,-4.136622,-2.583417,4.077312,-6.400701,4.303131,8.711571],[-0.137079,0.167015,1.288738,6.786151,-2.478185,-2.069972,8.790403],[7.627576,-9.003787,-8.050090,4.201663,-5.466177,-6.385750,7.257625],[6.005163,2.488788,2.402260,-5.213083,-0.058241,0.309042,-7.947608],[1.875311,9.401557,4.151929,5.838521,-9.087610,-3.373268,9.846739],[5.271795,-9.725465,7.054438,-9.935486,-2.599914,6.783901,-2.075631]],[[8.776493,-9.207464,2.299653,1.017655,-3.467976,-9.088189,2.775073],[7.896282,-6.341886,2.382047,7.093770,-9.619002,6.506313,-1.370733],[8.055440,7.429657,-5.617741,-8.723180,8.806517,-1.685344,-1.602948],[-0.750676,4.057111,-3.590089,-9.994562,-5.222262,-2.714987,3.976419],[6.030250,-1.766431,1.818677,1.787430,3.811488,0.392361,7.791722],[-7.996946,-6.571144,7.903414,-6.383044,6.559411,-1.465753,-6.074926],[-4.576725,-4.887811,-8.286669,9.028186,1.021011,9.587981,-9.564699],[9.552148,-8.624609,6.800607,7.413631,-1.511985,-8.241101,-5.304169]],[[2.830916,7.812418,9.036660,3.609061,-8.070743,6.661212,6.077367],[-5.163704,6.706330,3.996214,-4.397868,-1.112634,9.309362,6.191950],[0.347766,-0.801351,9.959366,-2.304150,-4.267493,-6.181173,-0.269158],[-2.815676,-1.386641,1.598165,-2.273439,2.593614,9.842664,-7.436504],[-7.213070,-4.729095,-8.948066,-6.430237,-2.603422,-8.496603,-5.061895],[5.337398,-7.314964,-4.288826,1.893337,-1.981556,-2.352683,-2.830840],[3.302292,-4.103019,-7.582935,7.083657,-2.154385,-9.185274,4.865895],[8.301041,4.261335,-1.931613,-5.259568,-0.135367,2.797481,6.954561]],[[-1.904233,4.841878,6.943955,2.273632,6.855231,-5.838579,-0.573533],[-7.793027,0.407569,3.098744,9.597592,-2.147768,-6.057026,5.192339],[1.874880,9.851841,-4.273659,7.142534,7.409572,3.723587,-3.947570],[-3.827870,7.259754,-5.227211,-9.610624,7.847797,4.745232,8.830350],[9.503537,8.115400,6.087180,-4.379279,-3.924904,3.708240,5.250519],[-2.906505,-6.750974,-5.355291,7.840109,-6.732936,8.294178,2.132631],[4.117027,-1.741704,1.314879,8.167325,0.920400,-3.983922,-3.716248],[8.563973,7.708072,8.621954,-1.001542,0.806047,-0.082365,4.640300]],[[2.855904,-0.091989,0.705390,3.272665,1.325195,4.808830,1.014967],[-9.798746,-1.357262,9.645056,9.225992,2.719101,-2.434086,6.306647],[2.777807,-4.452248,-2.484064,7.291332,-3.304071,-2.270666,-5.984551],[-8.106464,-3.366671,6.589168,-9.065749,-4.858209,9.795170,3.085558],[-1.445743,-8.653640,1.258096,-1.535241,3.402702,3.612630,0.843237],[6.009446,9.347697,8.662793,-4.676167,-4.278581,2.707421,-7.077969],[1.165174,-7.032898,1.399058,5.308737,-2.751090,-7.099705,8.018574],[1.061293,5.776395,-9.657479,-9.359429,-9.966832,-7.133269,7.454054]],[[9.454745,-0.931509,5.818755,-7.626940,9.733571,1.823520,-8.089609],[-0.324446,9.170658,-2.988146,-1.183493,9.209545,-1.866187,-3.143023],[6.776783,-6.776424,6.530016,2.426347,2.791642,5.640063,5.208772],[-3.123145,-2.111529,9.909013,-2.950897,6.311768,6.084988,7.091398],[-0.185090,-6.340517,7.235127,7.163537,-4.419875,8.747225,-1.807164],[-6.661614,7.866944,3.898163,1.042717,8.640720,-6.996320,2.699472],[-3.695579,6.660099,-1.371161,-8.715976,-6.160976,-7.914511,-5.266332],[6.402317,8.367504,-0.575061,-6.304107,-1.915530,-6.359667,-8.296498]]], dtype = "float64")#candidate|438|(9, 8, 7)|const|float64
uop_439 = relay.log10(const_438.astype('float64')) # shape=(9, 8, 7)
var_444 = relay.var("var_444", dtype = "float64", shape = (9, 8, 7))#candidate|444|(9, 8, 7)|var|float64
bop_445 = relay.divide(uop_439.astype('float32'), relay.reshape(var_444.astype('float32'), relay.shape_of(uop_439))) # shape=(9, 8, 7)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_455 = func_100_call()
call_456 = func_100_call()
uop_465 = relay.atanh(bop_445.astype('float64')) # shape=(9, 8, 7)
output = relay.Tuple([call_455,uop_465,])
output2 = relay.Tuple([call_456,uop_465,])
func_475 = relay.Function([var_444,], output)
mod['func_475'] = func_475
mod = relay.transform.InferType()(mod)
mutated_mod['func_475'] = func_475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_476 = relay.var("var_476", dtype = "float64", shape = (9, 8, 7))#candidate|476|(9, 8, 7)|var|float64
func_475_call = mutated_mod.get_global_var('func_475')
call_477 = func_475_call(var_476)
output = call_477
func_478 = relay.Function([var_476], output)
mutated_mod['func_478'] = func_478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_517 = func_100_call()
call_518 = func_100_call()
func_69_call = mod.get_global_var('func_69')
func_71_call = mutated_mod.get_global_var('func_71')
var_528 = relay.var("var_528", dtype = "float32", shape = (9, 9))#candidate|528|(9, 9)|var|float32
call_527 = relay.TupleGetItem(func_69_call(relay.reshape(var_528.astype('float32'), [3, 3, 9])), 1)
call_529 = relay.TupleGetItem(func_71_call(relay.reshape(var_528.astype('float32'), [3, 3, 9])), 1)
output = relay.Tuple([call_517,call_527,var_528,])
output2 = relay.Tuple([call_518,call_529,var_528,])
func_530 = relay.Function([var_528,], output)
mod['func_530'] = func_530
mod = relay.transform.InferType()(mod)
mutated_mod['func_530'] = func_530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_531 = relay.var("var_531", dtype = "float32", shape = (9, 9))#candidate|531|(9, 9)|var|float32
func_530_call = mutated_mod.get_global_var('func_530')
call_532 = func_530_call(var_531)
output = call_532
func_533 = relay.Function([var_531], output)
mutated_mod['func_533'] = func_533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_539 = relay.TupleGetItem(func_414_call(), 0)
call_540 = relay.TupleGetItem(func_415_call(), 0)
uop_576 = relay.erf(call_539.astype('float32')) # shape=(1, 15, 9)
uop_578 = relay.erf(call_540.astype('float32')) # shape=(1, 15, 9)
func_396_call = mod.get_global_var('func_396')
func_397_call = mutated_mod.get_global_var('func_397')
call_583 = relay.TupleGetItem(func_396_call(), 0)
call_584 = relay.TupleGetItem(func_397_call(), 0)
output = relay.Tuple([uop_576,call_583,])
output2 = relay.Tuple([uop_578,call_584,])
func_586 = relay.Function([], output)
mod['func_586'] = func_586
mod = relay.transform.InferType()(mod)
mutated_mod['func_586'] = func_586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mutated_mod.get_global_var('func_586')
call_587 = func_586_call()
output = call_587
func_588 = relay.Function([], output)
mutated_mod['func_588'] = func_588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_625 = relay.TupleGetItem(func_139_call(), 0)
call_626 = relay.TupleGetItem(func_140_call(), 0)
var_631 = relay.var("var_631", dtype = "float32", shape = (12, 15, 9))#candidate|631|(12, 15, 9)|var|float32
bop_632 = relay.left_shift(call_625.astype('uint64'), var_631.astype('uint64')) # shape=(12, 15, 9)
bop_635 = relay.left_shift(call_626.astype('uint64'), var_631.astype('uint64')) # shape=(12, 15, 9)
bop_645 = relay.less_equal(call_625.astype('bool'), var_631.astype('bool')) # shape=(12, 15, 9)
bop_648 = relay.less_equal(call_626.astype('bool'), var_631.astype('bool')) # shape=(12, 15, 9)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_651 = relay.TupleGetItem(func_414_call(), 0)
call_652 = relay.TupleGetItem(func_415_call(), 0)
bop_659 = relay.divide(call_625.astype('float32'), relay.reshape(call_651.astype('float32'), relay.shape_of(call_625))) # shape=(1, 15, 9)
bop_662 = relay.divide(call_626.astype('float32'), relay.reshape(call_652.astype('float32'), relay.shape_of(call_626))) # shape=(1, 15, 9)
output = relay.Tuple([bop_632,bop_645,bop_659,])
output2 = relay.Tuple([bop_635,bop_648,bop_662,])
func_665 = relay.Function([var_631,], output)
mod['func_665'] = func_665
mod = relay.transform.InferType()(mod)
mutated_mod['func_665'] = func_665
mutated_mod = relay.transform.InferType()(mutated_mod)
var_666 = relay.var("var_666", dtype = "float32", shape = (12, 15, 9))#candidate|666|(12, 15, 9)|var|float32
func_665_call = mutated_mod.get_global_var('func_665')
call_667 = func_665_call(var_666)
output = call_667
func_668 = relay.Function([var_666], output)
mutated_mod['func_668'] = func_668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_683 = relay.TupleGetItem(func_414_call(), 0)
call_684 = relay.TupleGetItem(func_415_call(), 0)
output = call_683
output2 = call_684
func_685 = relay.Function([], output)
mod['func_685'] = func_685
mod = relay.transform.InferType()(mod)
output = func_685()
func_686 = relay.Function([], output)
mutated_mod['func_686'] = func_686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_687 = func_100_call()
call_688 = func_100_call()
output = call_687
output2 = call_688
func_689 = relay.Function([], output)
mod['func_689'] = func_689
mod = relay.transform.InferType()(mod)
output = func_689()
func_690 = relay.Function([], output)
mutated_mod['func_690'] = func_690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_689_call = mod.get_global_var('func_689')
func_690_call = mutated_mod.get_global_var('func_690')
call_807 = func_689_call()
call_808 = func_689_call()
output = relay.Tuple([call_807,])
output2 = relay.Tuple([call_808,])
func_822 = relay.Function([], output)
mod['func_822'] = func_822
mod = relay.transform.InferType()(mod)
output = func_822()
func_823 = relay.Function([], output)
mutated_mod['func_823'] = func_823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_822_call = mod.get_global_var('func_822')
func_823_call = mutated_mod.get_global_var('func_823')
call_852 = relay.TupleGetItem(func_822_call(), 0)
call_853 = relay.TupleGetItem(func_823_call(), 0)
func_475_call = mod.get_global_var('func_475')
func_478_call = mutated_mod.get_global_var('func_478')
const_874 = relay.const([-5.346245,-1.664300,-2.677594,-2.367335,-9.545596,5.993203,7.187777,8.603446,-4.197639,-4.863831,-4.302428,-1.074803,-4.796620,-7.172670,-5.489464,4.081837,-3.132367,-9.657663,-9.287733,0.069448,7.622473,-4.535710,3.427411,4.484115,3.817409,-4.051570,0.819299,-7.278560,-5.997715,7.430281,-6.536936,2.366406,-0.142399,-8.311657,4.977829,8.251859,-4.934861,2.679222,-2.153953,-8.102118,-7.674528,7.026844,8.879010,-1.204635,-1.061664,4.505588,-7.377952,3.464976,-8.614031,3.073470,8.734739,-8.829546,-7.729192,6.780218,-0.440746,-0.389858,-4.121989,-8.087195,-5.442106,5.903324,-2.257203,5.732327,1.407754,3.044894,-8.308740,9.259879,7.665575,-3.690215,-1.191384,-5.313905,3.965102,5.436017,-0.847374,8.878977,-6.889248,7.597554,3.691112,-2.937727,1.087010,-5.489003,-7.246193,2.498014,9.639880,-5.948689,7.561200,-7.197548,6.768078,-6.271833,2.601662,-1.978845,-1.627404,-0.643312,9.581949,4.932621,-3.782184,-6.239354,3.488547,7.123523,3.063348,-6.135798,-2.417162,2.873266,7.753379,-7.011252,-8.870156,-4.426922,-4.210487,-4.172958,0.109472,9.713295,-3.873761,8.193989,3.694868,-0.216107,-1.950759,-3.519262,-4.752404,-4.185071,8.704693,-4.615868,-9.230652,0.690403,-9.208990,-0.946739,0.355067,5.081074,1.626126,5.524738,7.463818,-3.014322,0.616076,8.171126,-9.137569,7.159951,-3.198526,5.023541,-0.496566,7.193531,2.823218,3.732036,9.327287,-0.203918,4.912833,-6.518597,4.185993,-5.819009,6.948572,-3.033869,2.775071,4.344362,-3.357243,-1.865123,0.464814,1.516377,4.139405,9.180419,3.583607,-2.434781,-9.592651,-6.346666,6.367763,-7.595586,-2.526174,-6.758360,-0.927153,5.156291,0.189726,1.039508,5.522960,6.719137,8.155951,-4.846536,-0.346645,5.552903,7.079768,-5.460297,-4.140460,9.336463,-0.471685,4.104665,9.233520,6.941423,-3.873742,-3.809893,9.344772,2.218952,-9.409749,2.989254,-7.483370,5.599627,-2.478611,-6.726052,-8.681294,3.873318,8.844683,7.996572,2.828761,9.844783,-0.761691,-8.671742,6.763424,-6.420595,6.253476,-7.284423,5.413054,7.833517,-3.066440,-7.222881,3.664421,2.891555,-7.259394,5.721193,3.833789,-5.917849,-2.344638,5.037794,-1.507549,-8.333518,0.286848,1.436555,-7.355547,9.981216,-1.831755,-8.807061,3.555996,-7.586810,-5.808571,-8.325288,9.527875,8.845608,1.595918,2.334232,5.042133,3.705858,2.460645,1.034046,7.147705,-4.618611,-2.353942,2.401542,-3.731273,-1.009258,6.920190,-5.718090,8.089866,8.915903,-2.425089,-7.935027,-4.609938,-7.988589,-5.710055,8.809663,-9.393184,9.123794,-5.718220,0.995549,-8.397033,-9.005467,-7.770699,-9.496430,-8.103775,-9.920719,7.874147,-6.030612,-3.280880,0.792796,-5.035759,-3.700248,-5.605669,-7.313938,-5.984816,2.990086,0.130189,-2.328266,-8.944038,4.974280,-5.573127,5.898119,-2.403705,2.418837,-0.937235,0.361091,-8.801954,-7.071348,1.521273,9.815172,-0.979370,-3.439423,-1.826043,6.624349,-8.647638,-2.839905,-2.696361,-2.881084,0.455284,6.446378,-9.825010,2.772366,-1.030479,5.980709,-3.564943,9.757414,9.044283,-0.771288,-7.779106,-2.136279,-1.276206,-3.611337,-3.953362,5.106118,-2.533156,4.953800,3.088443,4.864163,-7.923485,5.477714,-1.425014,6.049117,-0.485205,3.973058,6.821854,3.577909,-6.057430,-8.422680,-2.797667,5.477773,-2.416994,4.554142,6.480891,6.257560,0.370190,-8.037172,7.142657,3.267152,5.645139,8.571456,-3.279267,-9.967292,-1.404920,4.940706,-2.848352,2.472073,-8.147657,-8.176372,-9.604799,9.656192,-9.977939,6.775122,-4.441418,7.692747,5.431142,-6.322439,-5.764248,5.975139,-7.304611,2.714257,6.354242,9.693160,-2.381766,4.096702,-6.973510,-7.532472,-2.774628,-6.375538,1.616329,-2.033389,-7.426298,-4.970133,8.502820,7.757053,7.455824,-3.809324,-8.451202,-7.969791,6.384664,2.510475,-6.913766,-2.189278,9.468616,0.049525,-5.646666,5.750996,0.226502,6.751522,5.787181,-8.759873,-5.222121,8.986105,-6.560686,0.547397,8.508560,2.714312,-1.445423,-4.650233,7.303389,-7.385946,1.803002,-9.358628,-1.387735,5.506885,7.327433,-9.601231,-7.387766,-4.270083,4.800737,-0.766192,-8.960795,-1.893047,1.183835,-3.091458,7.876762,6.570425,-0.513933,7.338705,0.804278,9.645704,-1.269310,-7.490333,3.659323,6.761449,-2.561991,-5.526676,-5.399627,-3.588873,5.509897,-2.207320,0.706959,-4.888646,4.343371,-1.943282,-0.947937,0.033312,3.805765,-9.176501,-0.150823,3.286126,6.660585,2.060806,2.488213,-4.092067,-0.232187,1.879444,-3.794294,-8.450503,4.891170,-4.368486,-8.343014,-0.625645,-5.518790,-1.594654,-5.731595,2.829757,7.125700,8.899839,-1.889597,-5.099317,-9.828555,7.345638,6.850543,8.021442,-5.720858,-8.516792,3.657224,5.373611,4.124763,1.730165,6.171273,-2.647522,8.321966,0.776891,6.649891,0.181135,3.493502,-5.997306,-5.743941,4.570271,9.410808,7.653502,-8.436939,-5.073495,-6.982213,-0.832904,7.683593,7.386169,-3.054649,-5.689521,-2.261978,-6.651129,-1.838577,-5.767383,-5.030832,-8.026731,9.639338,-1.900576,-9.109117,-2.881444,-5.527638,-4.543390,6.520129,5.360494,9.281156,0.676985,6.655045,8.893403], dtype = "float64")#candidate|874|(504,)|const|float64
call_873 = relay.TupleGetItem(func_475_call(relay.reshape(const_874.astype('float64'), [9, 8, 7])), 0)
call_875 = relay.TupleGetItem(func_478_call(relay.reshape(const_874.astype('float64'), [9, 8, 7])), 0)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_888 = func_100_call()
call_889 = func_100_call()
output = relay.Tuple([call_852,call_873,const_874,call_888,])
output2 = relay.Tuple([call_853,call_875,const_874,call_889,])
func_910 = relay.Function([], output)
mod['func_910'] = func_910
mod = relay.transform.InferType()(mod)
output = func_910()
func_911 = relay.Function([], output)
mutated_mod['func_911'] = func_911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_974 = relay.var("var_974", dtype = "float64", shape = (7, 4, 10))#candidate|974|(7, 4, 10)|var|float64
uop_975 = relay.acos(var_974.astype('float64')) # shape=(7, 4, 10)
output = uop_975
output2 = uop_975
func_978 = relay.Function([var_974,], output)
mod['func_978'] = func_978
mod = relay.transform.InferType()(mod)
var_979 = relay.var("var_979", dtype = "float64", shape = (7, 4, 10))#candidate|979|(7, 4, 10)|var|float64
output = func_978(var_979)
func_980 = relay.Function([var_979], output)
mutated_mod['func_980'] = func_980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_686_call = mutated_mod.get_global_var('func_686')
call_1003 = func_685_call()
call_1004 = func_685_call()
output = call_1003
output2 = call_1004
func_1007 = relay.Function([], output)
mod['func_1007'] = func_1007
mod = relay.transform.InferType()(mod)
output = func_1007()
func_1008 = relay.Function([], output)
mutated_mod['func_1008'] = func_1008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_822_call = mod.get_global_var('func_822')
func_823_call = mutated_mod.get_global_var('func_823')
call_1056 = relay.TupleGetItem(func_822_call(), 0)
call_1057 = relay.TupleGetItem(func_823_call(), 0)
func_1007_call = mod.get_global_var('func_1007')
func_1008_call = mutated_mod.get_global_var('func_1008')
call_1061 = func_1007_call()
call_1062 = func_1007_call()
output = relay.Tuple([call_1056,call_1061,])
output2 = relay.Tuple([call_1057,call_1062,])
func_1070 = relay.Function([], output)
mod['func_1070'] = func_1070
mod = relay.transform.InferType()(mod)
mutated_mod['func_1070'] = func_1070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mutated_mod.get_global_var('func_1070')
call_1071 = func_1070_call()
output = call_1071
func_1072 = relay.Function([], output)
mutated_mod['func_1072'] = func_1072
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1114 = relay.var("var_1114", dtype = "uint8", shape = (9, 6, 9))#candidate|1114|(9, 6, 9)|var|uint8
var_1115 = relay.var("var_1115", dtype = "uint8", shape = (9, 6, 9))#candidate|1115|(9, 6, 9)|var|uint8
bop_1116 = relay.left_shift(var_1114.astype('uint8'), relay.reshape(var_1115.astype('uint8'), relay.shape_of(var_1114))) # shape=(9, 6, 9)
uop_1122 = relay.sqrt(var_1115.astype('float64')) # shape=(9, 6, 9)
output = relay.Tuple([bop_1116,uop_1122,])
output2 = relay.Tuple([bop_1116,uop_1122,])
func_1127 = relay.Function([var_1114,var_1115,], output)
mod['func_1127'] = func_1127
mod = relay.transform.InferType()(mod)
mutated_mod['func_1127'] = func_1127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mutated_mod.get_global_var('func_1127')
var_1129 = relay.var("var_1129", dtype = "uint8", shape = (9, 6, 9))#candidate|1129|(9, 6, 9)|var|uint8
var_1130 = relay.var("var_1130", dtype = "uint8", shape = (9, 6, 9))#candidate|1130|(9, 6, 9)|var|uint8
call_1128 = func_1127_call(var_1129,var_1130,)
output = call_1128
func_1131 = relay.Function([var_1129,var_1130,], output)
mutated_mod['func_1131'] = func_1131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1133 = relay.TupleGetItem(func_586_call(), 0)
call_1134 = relay.TupleGetItem(func_588_call(), 0)
func_665_call = mod.get_global_var('func_665')
func_668_call = mutated_mod.get_global_var('func_668')
var_1142 = relay.var("var_1142", dtype = "float32", shape = (1620,))#candidate|1142|(1620,)|var|float32
call_1141 = relay.TupleGetItem(func_665_call(relay.reshape(var_1142.astype('float32'), [12, 15, 9])), 0)
call_1143 = relay.TupleGetItem(func_668_call(relay.reshape(var_1142.astype('float32'), [12, 15, 9])), 0)
func_190_call = mod.get_global_var('func_190')
func_192_call = mutated_mod.get_global_var('func_192')
var_1147 = relay.var("var_1147", dtype = "float32", shape = (81,))#candidate|1147|(81,)|var|float32
call_1146 = relay.TupleGetItem(func_190_call(relay.reshape(var_1147.astype('float32'), [81,])), 1)
call_1148 = relay.TupleGetItem(func_192_call(relay.reshape(var_1147.astype('float32'), [81,])), 1)
bop_1152 = relay.logical_xor(var_1147.astype('uint8'), relay.reshape(call_1146.astype('uint8'), relay.shape_of(var_1147))) # shape=(81,)
bop_1155 = relay.logical_xor(var_1147.astype('uint8'), relay.reshape(call_1148.astype('uint8'), relay.shape_of(var_1147))) # shape=(81,)
output = relay.Tuple([call_1133,call_1141,var_1142,bop_1152,])
output2 = relay.Tuple([call_1134,call_1143,var_1142,bop_1155,])
func_1159 = relay.Function([var_1142,var_1147,], output)
mod['func_1159'] = func_1159
mod = relay.transform.InferType()(mod)
var_1160 = relay.var("var_1160", dtype = "float32", shape = (1620,))#candidate|1160|(1620,)|var|float32
var_1161 = relay.var("var_1161", dtype = "float32", shape = (81,))#candidate|1161|(81,)|var|float32
output = func_1159(var_1160,var_1161,)
func_1162 = relay.Function([var_1160,var_1161,], output)
mutated_mod['func_1162'] = func_1162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_910_call = mod.get_global_var('func_910')
func_911_call = mutated_mod.get_global_var('func_911')
call_1183 = relay.TupleGetItem(func_910_call(), 2)
call_1184 = relay.TupleGetItem(func_911_call(), 2)
output = relay.Tuple([call_1183,])
output2 = relay.Tuple([call_1184,])
func_1197 = relay.Function([], output)
mod['func_1197'] = func_1197
mod = relay.transform.InferType()(mod)
mutated_mod['func_1197'] = func_1197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mutated_mod.get_global_var('func_1197')
call_1198 = func_1197_call()
output = call_1198
func_1199 = relay.Function([], output)
mutated_mod['func_1199'] = func_1199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_689_call = mod.get_global_var('func_689')
func_690_call = mutated_mod.get_global_var('func_690')
call_1211 = func_689_call()
call_1212 = func_689_call()
var_1227 = relay.var("var_1227", dtype = "float32", shape = (9, 15, 9))#candidate|1227|(9, 15, 9)|var|float32
bop_1228 = relay.less_equal(call_1211.astype('bool'), var_1227.astype('bool')) # shape=(9, 15, 9)
bop_1231 = relay.less_equal(call_1212.astype('bool'), var_1227.astype('bool')) # shape=(9, 15, 9)
bop_1238 = relay.bitwise_xor(bop_1228.astype('int32'), relay.reshape(var_1227.astype('int32'), relay.shape_of(bop_1228))) # shape=(9, 15, 9)
bop_1241 = relay.bitwise_xor(bop_1231.astype('int32'), relay.reshape(var_1227.astype('int32'), relay.shape_of(bop_1231))) # shape=(9, 15, 9)
func_190_call = mod.get_global_var('func_190')
func_192_call = mutated_mod.get_global_var('func_192')
var_1248 = relay.var("var_1248", dtype = "float32", shape = (81,))#candidate|1248|(81,)|var|float32
call_1247 = relay.TupleGetItem(func_190_call(relay.reshape(var_1248.astype('float32'), [81,])), 0)
call_1249 = relay.TupleGetItem(func_192_call(relay.reshape(var_1248.astype('float32'), [81,])), 0)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_1264 = relay.TupleGetItem(func_414_call(), 0)
call_1265 = relay.TupleGetItem(func_415_call(), 0)
uop_1277 = relay.sqrt(call_1264.astype('float32')) # shape=(1, 15, 9)
uop_1279 = relay.sqrt(call_1265.astype('float32')) # shape=(1, 15, 9)
bop_1280 = relay.mod(uop_1277.astype('float32'), bop_1228.astype('float32')) # shape=(9, 15, 9)
bop_1283 = relay.mod(uop_1279.astype('float32'), bop_1231.astype('float32')) # shape=(9, 15, 9)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_1304 = relay.TupleGetItem(func_414_call(), 0)
call_1305 = relay.TupleGetItem(func_415_call(), 0)
bop_1310 = relay.logical_xor(uop_1277.astype('uint8'), relay.reshape(call_1264.astype('uint8'), relay.shape_of(uop_1277))) # shape=(1, 15, 9)
bop_1313 = relay.logical_xor(uop_1279.astype('uint8'), relay.reshape(call_1265.astype('uint8'), relay.shape_of(uop_1279))) # shape=(1, 15, 9)
output = relay.Tuple([bop_1238,call_1247,var_1248,bop_1280,call_1304,bop_1310,])
output2 = relay.Tuple([bop_1241,call_1249,var_1248,bop_1283,call_1305,bop_1313,])
func_1314 = relay.Function([var_1227,var_1248,], output)
mod['func_1314'] = func_1314
mod = relay.transform.InferType()(mod)
mutated_mod['func_1314'] = func_1314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1314_call = mutated_mod.get_global_var('func_1314')
var_1316 = relay.var("var_1316", dtype = "float32", shape = (9, 15, 9))#candidate|1316|(9, 15, 9)|var|float32
var_1317 = relay.var("var_1317", dtype = "float32", shape = (81,))#candidate|1317|(81,)|var|float32
call_1315 = func_1314_call(var_1316,var_1317,)
output = call_1315
func_1318 = relay.Function([var_1316,var_1317,], output)
mutated_mod['func_1318'] = func_1318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_1336 = relay.TupleGetItem(func_414_call(), 0)
call_1337 = relay.TupleGetItem(func_415_call(), 0)
func_685_call = mod.get_global_var('func_685')
func_686_call = mutated_mod.get_global_var('func_686')
call_1343 = func_685_call()
call_1344 = func_685_call()
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
call_1347 = relay.TupleGetItem(func_1197_call(), 0)
call_1348 = relay.TupleGetItem(func_1199_call(), 0)
output = relay.Tuple([call_1336,call_1343,call_1347,])
output2 = relay.Tuple([call_1337,call_1344,call_1348,])
func_1355 = relay.Function([], output)
mod['func_1355'] = func_1355
mod = relay.transform.InferType()(mod)
mutated_mod['func_1355'] = func_1355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1355_call = mutated_mod.get_global_var('func_1355')
call_1356 = func_1355_call()
output = call_1356
func_1357 = relay.Function([], output)
mutated_mod['func_1357'] = func_1357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1404 = relay.TupleGetItem(func_586_call(), 0)
call_1405 = relay.TupleGetItem(func_588_call(), 0)
func_1127_call = mod.get_global_var('func_1127')
func_1131_call = mutated_mod.get_global_var('func_1131')
const_1407 = relay.const([[9,6],[4,-1],[3,-4],[-9,-1],[9,3],[9,-9],[2,-7],[-2,-5],[-2,8],[-9,6],[-10,7],[3,6],[5,-10],[-7,-1],[-5,-4],[-9,9],[-10,-9],[5,-10],[-8,-6],[-4,2],[4,-4],[-1,10],[5,-6],[-4,8],[-1,2],[-2,2],[-7,10],[-3,-1],[-2,-1],[-1,-2],[6,-1],[-10,-2],[-5,6],[-7,9],[9,7],[10,2],[-2,9],[-4,8],[-7,-8],[-7,8],[7,1],[-4,-9],[-8,8],[4,-3],[1,-2],[3,4],[-10,-8],[7,10],[2,9],[10,3],[-6,-7],[9,1],[-2,-6],[2,4],[6,-10],[10,6],[-9,-1],[7,-8],[-3,5],[5,-5],[-8,3],[-2,-3],[-10,1],[3,3],[-6,-1],[-6,-6],[-6,-2],[-9,-9],[9,9],[2,2],[-7,2],[-2,-1],[9,1],[-3,-6],[-8,-9],[7,-3],[3,-8],[6,-6],[2,-2],[-5,3],[5,1],[1,-6],[-10,-7],[6,-5],[-6,1],[-2,-4],[5,1],[6,-5],[-9,10],[6,10],[-2,2],[1,-6],[-10,-8],[4,-1],[5,-10],[-7,4],[1,-8],[10,10],[-9,2],[2,6],[5,-6],[-5,9],[-8,-2],[3,-3],[-10,1],[10,-3],[-6,8],[1,9],[7,4],[-2,-1],[3,7],[9,-2],[2,-8],[9,-1],[4,-4],[-5,-10],[10,-6],[8,-5],[1,9],[-4,9],[-6,-8],[8,-9],[-3,7],[6,2],[-3,8],[-6,-10],[-7,-8],[-10,6],[-6,1],[8,-6],[3,-8],[-3,6],[-9,-5],[7,3],[-6,2],[-8,4],[-5,-7],[6,-5],[-9,1],[5,7],[-2,-8],[-10,1],[-2,6],[5,3],[6,4],[-3,5],[2,-5],[-3,-1],[-7,-2],[-10,4],[9,-1],[1,-4],[-3,-1],[9,-2],[3,-8],[-10,-1],[-7,-3],[-7,-10],[-9,3],[-4,7],[7,-8],[7,7],[-7,-6],[5,-3],[2,3],[5,8],[-4,-3],[7,-8],[1,1],[3,-8],[5,7],[-1,4],[6,-3],[-1,-6],[9,1],[-1,-10],[-4,8],[1,6],[-10,-7],[3,4],[-9,10],[-7,2],[6,-4],[4,-7],[7,6],[3,-3],[4,4],[1,7],[-5,9],[5,-10],[9,-8],[-9,3],[-4,1],[10,-10],[4,-4],[-2,-3],[1,-10],[5,7],[-5,-7],[4,10],[9,-5],[5,-5],[-7,-4],[-1,-7],[10,7],[9,-9],[1,-1],[-8,-2],[2,7],[-3,8],[1,-1],[8,-3],[7,-4],[-5,1],[3,-2],[-2,-9],[4,-2],[8,10],[-2,10],[-1,8],[4,-4],[-7,9],[-8,-2],[-9,-5],[-8,-1],[6,6],[2,-8],[10,1],[-10,-4],[-10,8],[6,-6],[-4,8],[-7,8],[10,-5],[-9,-5],[9,-2],[-1,-7],[-3,-6],[-6,4],[5,-9],[2,-10],[-1,-7],[8,-9]], dtype = "uint8")#candidate|1407|(243, 2)|const|uint8
call_1406 = relay.TupleGetItem(func_1127_call(relay.reshape(const_1407.astype('uint8'), [9, 6, 9]), relay.reshape(const_1407.astype('uint8'), [9, 6, 9]), ), 0)
call_1408 = relay.TupleGetItem(func_1131_call(relay.reshape(const_1407.astype('uint8'), [9, 6, 9]), relay.reshape(const_1407.astype('uint8'), [9, 6, 9]), ), 0)
func_910_call = mod.get_global_var('func_910')
func_911_call = mutated_mod.get_global_var('func_911')
call_1416 = relay.TupleGetItem(func_910_call(), 1)
call_1417 = relay.TupleGetItem(func_911_call(), 1)
func_1355_call = mod.get_global_var('func_1355')
func_1357_call = mutated_mod.get_global_var('func_1357')
call_1419 = relay.TupleGetItem(func_1355_call(), 2)
call_1420 = relay.TupleGetItem(func_1357_call(), 2)
bop_1431 = relay.power(const_1407.astype('float32'), relay.reshape(call_1406.astype('float32'), relay.shape_of(const_1407))) # shape=(243, 2)
bop_1434 = relay.power(const_1407.astype('float32'), relay.reshape(call_1408.astype('float32'), relay.shape_of(const_1407))) # shape=(243, 2)
uop_1439 = relay.log10(const_1407.astype('float32')) # shape=(243, 2)
uop_1448 = relay.asinh(uop_1439.astype('float64')) # shape=(243, 2)
bop_1461 = relay.mod(uop_1448.astype('float32'), relay.reshape(bop_1431.astype('float32'), relay.shape_of(uop_1448))) # shape=(243, 2)
bop_1464 = relay.mod(uop_1448.astype('float32'), relay.reshape(bop_1434.astype('float32'), relay.shape_of(uop_1448))) # shape=(243, 2)
bop_1469 = relay.equal(bop_1461.astype('bool'), relay.reshape(uop_1448.astype('bool'), relay.shape_of(bop_1461))) # shape=(243, 2)
bop_1472 = relay.equal(bop_1464.astype('bool'), relay.reshape(uop_1448.astype('bool'), relay.shape_of(bop_1464))) # shape=(243, 2)
uop_1473 = relay.exp(uop_1448.astype('float32')) # shape=(243, 2)
uop_1482 = relay.cosh(uop_1473.astype('float32')) # shape=(243, 2)
func_1314_call = mod.get_global_var('func_1314')
func_1318_call = mutated_mod.get_global_var('func_1318')
var_1485 = relay.var("var_1485", dtype = "float32", shape = (1215,))#candidate|1485|(1215,)|var|float32
var_1486 = relay.var("var_1486", dtype = "float32", shape = (81,))#candidate|1486|(81,)|var|float32
call_1484 = relay.TupleGetItem(func_1314_call(relay.reshape(var_1485.astype('float32'), [9, 15, 9]), relay.reshape(var_1486.astype('float32'), [81,]), ), 3)
call_1487 = relay.TupleGetItem(func_1318_call(relay.reshape(var_1485.astype('float32'), [9, 15, 9]), relay.reshape(var_1486.astype('float32'), [81,]), ), 3)
bop_1488 = relay.logical_and(uop_1482.astype('bool'), relay.reshape(call_1406.astype('bool'), relay.shape_of(uop_1482))) # shape=(243, 2)
bop_1491 = relay.logical_and(uop_1482.astype('bool'), relay.reshape(call_1408.astype('bool'), relay.shape_of(uop_1482))) # shape=(243, 2)
bop_1505 = relay.subtract(bop_1488.astype('int64'), relay.reshape(bop_1431.astype('int64'), relay.shape_of(bop_1488))) # shape=(243, 2)
bop_1508 = relay.subtract(bop_1491.astype('int64'), relay.reshape(bop_1434.astype('int64'), relay.shape_of(bop_1491))) # shape=(243, 2)
func_69_call = mod.get_global_var('func_69')
func_71_call = mutated_mod.get_global_var('func_71')
call_1509 = relay.TupleGetItem(func_69_call(relay.reshape(var_1486.astype('float32'), [3, 3, 9])), 0)
call_1510 = relay.TupleGetItem(func_71_call(relay.reshape(var_1486.astype('float32'), [3, 3, 9])), 0)
var_1513 = relay.var("var_1513", dtype = "bool", shape = (243, 2))#candidate|1513|(243, 2)|var|bool
bop_1514 = relay.divide(bop_1469.astype('float32'), relay.reshape(var_1513.astype('float32'), relay.shape_of(bop_1469))) # shape=(243, 2)
bop_1517 = relay.divide(bop_1472.astype('float32'), relay.reshape(var_1513.astype('float32'), relay.shape_of(bop_1472))) # shape=(243, 2)
var_1524 = relay.var("var_1524", dtype = "float32", shape = (243, 2))#candidate|1524|(243, 2)|var|float32
bop_1525 = relay.logical_xor(uop_1482.astype('int8'), relay.reshape(var_1524.astype('int8'), relay.shape_of(uop_1482))) # shape=(243, 2)
func_689_call = mod.get_global_var('func_689')
func_690_call = mutated_mod.get_global_var('func_690')
call_1535 = func_689_call()
call_1536 = func_689_call()
bop_1542 = relay.minimum(bop_1488.astype('uint64'), relay.reshape(bop_1431.astype('uint64'), relay.shape_of(bop_1488))) # shape=(243, 2)
bop_1545 = relay.minimum(bop_1491.astype('uint64'), relay.reshape(bop_1434.astype('uint64'), relay.shape_of(bop_1491))) # shape=(243, 2)
output = relay.Tuple([call_1404,call_1416,call_1419,call_1484,var_1485,var_1486,bop_1505,call_1509,bop_1514,bop_1525,call_1535,bop_1542,])
output2 = relay.Tuple([call_1405,call_1417,call_1420,call_1487,var_1485,var_1486,bop_1508,call_1510,bop_1517,bop_1525,call_1536,bop_1545,])
func_1546 = relay.Function([var_1485,var_1486,var_1513,var_1524,], output)
mod['func_1546'] = func_1546
mod = relay.transform.InferType()(mod)
var_1547 = relay.var("var_1547", dtype = "float32", shape = (1215,))#candidate|1547|(1215,)|var|float32
var_1548 = relay.var("var_1548", dtype = "float32", shape = (81,))#candidate|1548|(81,)|var|float32
var_1549 = relay.var("var_1549", dtype = "bool", shape = (243, 2))#candidate|1549|(243, 2)|var|bool
var_1550 = relay.var("var_1550", dtype = "float32", shape = (243, 2))#candidate|1550|(243, 2)|var|float32
output = func_1546(var_1547,var_1548,var_1549,var_1550,)
func_1551 = relay.Function([var_1547,var_1548,var_1549,var_1550,], output)
mutated_mod['func_1551'] = func_1551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1553 = relay.TupleGetItem(func_586_call(), 0)
call_1554 = relay.TupleGetItem(func_588_call(), 0)
var_1559 = relay.var("var_1559", dtype = "float32", shape = (2, 15, 9))#candidate|1559|(2, 15, 9)|var|float32
bop_1560 = relay.minimum(call_1553.astype('int32'), var_1559.astype('int32')) # shape=(2, 15, 9)
bop_1563 = relay.minimum(call_1554.astype('int32'), var_1559.astype('int32')) # shape=(2, 15, 9)
output = bop_1560
output2 = bop_1563
func_1564 = relay.Function([var_1559,], output)
mod['func_1564'] = func_1564
mod = relay.transform.InferType()(mod)
mutated_mod['func_1564'] = func_1564
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1565 = relay.var("var_1565", dtype = "float32", shape = (2, 15, 9))#candidate|1565|(2, 15, 9)|var|float32
func_1564_call = mutated_mod.get_global_var('func_1564')
call_1566 = func_1564_call(var_1565)
output = call_1566
func_1567 = relay.Function([var_1565], output)
mutated_mod['func_1567'] = func_1567
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1583 = relay.var("var_1583", dtype = "float64", shape = (7, 16, 6))#candidate|1583|(7, 16, 6)|var|float64
var_1584 = relay.var("var_1584", dtype = "float64", shape = (7, 16, 6))#candidate|1584|(7, 16, 6)|var|float64
bop_1585 = relay.subtract(var_1583.astype('float64'), relay.reshape(var_1584.astype('float64'), relay.shape_of(var_1583))) # shape=(7, 16, 6)
bop_1590 = relay.logical_and(bop_1585.astype('bool'), relay.reshape(var_1583.astype('bool'), relay.shape_of(bop_1585))) # shape=(7, 16, 6)
func_1564_call = mod.get_global_var('func_1564')
func_1567_call = mutated_mod.get_global_var('func_1567')
var_1594 = relay.var("var_1594", dtype = "float32", shape = (270,))#candidate|1594|(270,)|var|float32
call_1593 = func_1564_call(relay.reshape(var_1594.astype('float32'), [2, 15, 9]))
call_1595 = func_1564_call(relay.reshape(var_1594.astype('float32'), [2, 15, 9]))
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
call_1601 = relay.TupleGetItem(func_1197_call(), 0)
call_1602 = relay.TupleGetItem(func_1199_call(), 0)
func_1564_call = mod.get_global_var('func_1564')
func_1567_call = mutated_mod.get_global_var('func_1567')
call_1617 = func_1564_call(relay.reshape(call_1593.astype('float32'), [2, 15, 9]))
call_1618 = func_1564_call(relay.reshape(call_1593.astype('float32'), [2, 15, 9]))
func_124_call = mod.get_global_var('func_124')
func_125_call = mutated_mod.get_global_var('func_125')
call_1624 = func_124_call()
call_1625 = func_124_call()
uop_1627 = relay.cosh(call_1593.astype('float64')) # shape=(2, 15, 9)
uop_1629 = relay.cosh(call_1595.astype('float64')) # shape=(2, 15, 9)
output = relay.Tuple([bop_1590,var_1594,call_1601,call_1617,call_1624,uop_1627,])
output2 = relay.Tuple([bop_1590,var_1594,call_1602,call_1618,call_1625,uop_1629,])
func_1652 = relay.Function([var_1583,var_1584,var_1594,], output)
mod['func_1652'] = func_1652
mod = relay.transform.InferType()(mod)
mutated_mod['func_1652'] = func_1652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1652_call = mutated_mod.get_global_var('func_1652')
var_1654 = relay.var("var_1654", dtype = "float64", shape = (7, 16, 6))#candidate|1654|(7, 16, 6)|var|float64
var_1655 = relay.var("var_1655", dtype = "float64", shape = (7, 16, 6))#candidate|1655|(7, 16, 6)|var|float64
var_1656 = relay.var("var_1656", dtype = "float32", shape = (270,))#candidate|1656|(270,)|var|float32
call_1653 = func_1652_call(var_1654,var_1655,var_1656,)
output = call_1653
func_1657 = relay.Function([var_1654,var_1655,var_1656,], output)
mutated_mod['func_1657'] = func_1657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_822_call = mod.get_global_var('func_822')
func_823_call = mutated_mod.get_global_var('func_823')
call_1681 = relay.TupleGetItem(func_822_call(), 0)
call_1682 = relay.TupleGetItem(func_823_call(), 0)
output = call_1681
output2 = call_1682
func_1706 = relay.Function([], output)
mod['func_1706'] = func_1706
mod = relay.transform.InferType()(mod)
output = func_1706()
func_1707 = relay.Function([], output)
mutated_mod['func_1707'] = func_1707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_124_call = mod.get_global_var('func_124')
func_125_call = mutated_mod.get_global_var('func_125')
call_1720 = func_124_call()
call_1721 = func_124_call()
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_1733 = relay.TupleGetItem(func_139_call(), 0)
call_1734 = relay.TupleGetItem(func_140_call(), 0)
output = relay.Tuple([call_1720,call_1733,])
output2 = relay.Tuple([call_1721,call_1734,])
func_1764 = relay.Function([], output)
mod['func_1764'] = func_1764
mod = relay.transform.InferType()(mod)
mutated_mod['func_1764'] = func_1764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1764_call = mutated_mod.get_global_var('func_1764')
call_1765 = func_1764_call()
output = call_1765
func_1766 = relay.Function([], output)
mutated_mod['func_1766'] = func_1766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1819 = relay.TupleGetItem(func_586_call(), 0)
call_1820 = relay.TupleGetItem(func_588_call(), 0)
func_910_call = mod.get_global_var('func_910')
func_911_call = mutated_mod.get_global_var('func_911')
call_1829 = relay.TupleGetItem(func_910_call(), 0)
call_1830 = relay.TupleGetItem(func_911_call(), 0)
output = relay.Tuple([call_1819,call_1829,])
output2 = relay.Tuple([call_1820,call_1830,])
func_1863 = relay.Function([], output)
mod['func_1863'] = func_1863
mod = relay.transform.InferType()(mod)
output = func_1863()
func_1864 = relay.Function([], output)
mutated_mod['func_1864'] = func_1864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_686_call = mutated_mod.get_global_var('func_686')
call_1881 = func_685_call()
call_1882 = func_685_call()
output = relay.Tuple([call_1881,])
output2 = relay.Tuple([call_1882,])
func_1891 = relay.Function([], output)
mod['func_1891'] = func_1891
mod = relay.transform.InferType()(mod)
output = func_1891()
func_1892 = relay.Function([], output)
mutated_mod['func_1892'] = func_1892
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1893 = relay.var("var_1893", dtype = "uint64", shape = ())#candidate|1893|()|var|uint64
const_1894 = relay.const([[[-7,10,10],[3,3,4],[-8,2,5],[8,4,2],[-10,8,1],[6,6,5],[4,-8,5],[-8,3,2],[-5,-8,10],[7,-4,-2],[6,-2,-5],[-10,6,8],[2,-8,-6],[-4,1,-4]],[[-1,-1,-5],[9,-10,-2],[1,6,2],[1,-1,-8],[7,2,6],[-9,4,-2],[-4,8,6],[-10,4,2],[-1,-9,-2],[-9,-10,9],[6,3,-9],[-9,-7,-8],[9,-8,6],[-10,-5,-9]],[[-5,-7,1],[3,5,7],[10,-8,3],[10,4,6],[7,6,2],[-10,6,-3],[7,-4,1],[-8,-5,8],[4,1,-5],[7,2,6],[1,-2,7],[-3,1,-9],[-7,5,-7],[4,-10,-9]],[[-2,9,-2],[-2,4,7],[1,-8,-7],[7,5,-10],[5,-2,-6],[2,-9,-4],[7,-5,1],[-2,4,-5],[6,7,-3],[2,8,5],[-8,6,7],[10,5,4],[-9,-8,-8],[-4,-6,6]],[[5,-9,5],[-8,10,-10],[-3,2,-8],[-6,5,-10],[9,-7,-4],[-4,2,-3],[-7,10,7],[6,-4,2],[3,1,-3],[10,4,5],[-2,-8,-4],[1,-3,9],[-3,-10,1],[9,9,3]],[[10,2,-5],[-3,-7,1],[-1,3,3],[4,8,3],[7,5,-1],[-7,-6,-6],[-9,-5,-1],[10,-9,5],[-6,8,-4],[-3,-2,-6],[9,-3,-4],[5,7,2],[6,-9,4],[7,-5,-3]],[[-5,-8,7],[9,7,10],[-10,-7,-4],[-6,-8,7],[8,-3,2],[-2,4,-5],[3,-6,3],[-4,-10,-1],[-7,-7,1],[8,-2,4],[8,-3,5],[-1,10,-1],[-3,8,-5],[10,-6,-6]],[[2,8,-6],[8,-8,6],[6,4,-7],[3,-9,3],[-1,-5,-9],[6,6,5],[-6,-5,3],[10,1,9],[10,-5,-4],[2,-1,-4],[9,-2,-6],[6,-2,-10],[4,-6,3],[-10,9,1]],[[-6,-1,-9],[7,-7,-2],[6,8,-1],[-2,-8,10],[6,-6,7],[-10,-2,8],[-6,-9,4],[7,-1,7],[-3,9,-7],[-5,-10,2],[8,-10,3],[-2,-5,-3],[6,8,-8],[1,3,-3]],[[2,-7,-8],[-2,1,7],[-10,-2,-3],[3,-8,7],[5,7,2],[10,9,6],[4,-4,-10],[8,3,6],[-6,5,9],[2,-2,3],[9,7,1],[-5,-1,-10],[3,2,8],[2,-4,-2]],[[1,-10,2],[-4,-9,1],[4,4,7],[8,-10,8],[8,-5,-8],[-9,10,-1],[-3,5,8],[1,-2,-9],[9,-10,10],[10,-9,10],[2,8,9],[4,6,5],[5,-6,-2],[-9,6,9]],[[-9,-4,4],[8,3,5],[5,5,1],[5,-7,5],[10,10,3],[-2,10,3],[-9,-7,-8],[8,6,-7],[5,-2,-7],[-4,1,2],[5,10,-9],[-7,-3,3],[-9,-5,4],[1,-5,4]],[[10,-8,-1],[-8,-6,2],[-1,-4,-5],[6,-9,8],[-4,-5,-4],[3,-8,-6],[3,7,-4],[3,-8,-8],[5,7,-6],[9,6,10],[-4,3,-4],[-3,6,-6],[-7,-4,7],[7,7,-8]],[[-9,-4,3],[-6,-7,-9],[1,-9,1],[7,-4,2],[4,-3,-3],[3,-10,-8],[1,7,4],[-10,-9,-2],[-4,-8,-8],[2,-10,-3],[8,7,-3],[8,-9,-1],[-5,8,9],[4,-6,4]]], dtype = "uint64")#candidate|1894|(14, 14, 3)|const|uint64
bop_1895 = relay.equal(var_1893.astype('bool'), const_1894.astype('bool')) # shape=(14, 14, 3)
bop_1905 = relay.floor_mod(bop_1895.astype('float32'), var_1893.astype('float32')) # shape=(14, 14, 3)
bop_1908 = relay.less_equal(var_1893.astype('bool'), bop_1905.astype('bool')) # shape=(14, 14, 3)
output = bop_1908
output2 = bop_1908
func_1927 = relay.Function([var_1893,], output)
mod['func_1927'] = func_1927
mod = relay.transform.InferType()(mod)
var_1928 = relay.var("var_1928", dtype = "uint64", shape = ())#candidate|1928|()|var|uint64
output = func_1927(var_1928)
func_1929 = relay.Function([var_1928], output)
mutated_mod['func_1929'] = func_1929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_910_call = mod.get_global_var('func_910')
func_911_call = mutated_mod.get_global_var('func_911')
call_1951 = relay.TupleGetItem(func_910_call(), 3)
call_1952 = relay.TupleGetItem(func_911_call(), 3)
output = call_1951
output2 = call_1952
func_1958 = relay.Function([], output)
mod['func_1958'] = func_1958
mod = relay.transform.InferType()(mod)
mutated_mod['func_1958'] = func_1958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mutated_mod.get_global_var('func_1958')
call_1959 = func_1958_call()
output = call_1959
func_1960 = relay.Function([], output)
mutated_mod['func_1960'] = func_1960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_1964 = relay.TupleGetItem(func_1070_call(), 1)
call_1965 = relay.TupleGetItem(func_1072_call(), 1)
var_1977 = relay.var("var_1977", dtype = "float32", shape = (7, 15, 9))#candidate|1977|(7, 15, 9)|var|float32
bop_1978 = relay.greater(call_1964.astype('bool'), var_1977.astype('bool')) # shape=(7, 15, 9)
bop_1981 = relay.greater(call_1965.astype('bool'), var_1977.astype('bool')) # shape=(7, 15, 9)
func_1355_call = mod.get_global_var('func_1355')
func_1357_call = mutated_mod.get_global_var('func_1357')
call_1992 = relay.TupleGetItem(func_1355_call(), 1)
call_1993 = relay.TupleGetItem(func_1357_call(), 1)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_1996 = relay.TupleGetItem(func_414_call(), 0)
call_1997 = relay.TupleGetItem(func_415_call(), 0)
uop_2005 = relay.sigmoid(var_1977.astype('float64')) # shape=(7, 15, 9)
bop_2012 = relay.divide(uop_2005.astype('float32'), call_1964.astype('float32')) # shape=(7, 15, 9)
bop_2015 = relay.divide(uop_2005.astype('float32'), call_1965.astype('float32')) # shape=(7, 15, 9)
uop_2021 = relay.log(uop_2005.astype('float64')) # shape=(7, 15, 9)
const_2023 = relay.const([[[-0.362729,5.302513,6.923352,-3.147547,-5.896168,6.074449,-9.153673,-3.209903,-3.642282],[3.601884,3.745064,7.474038,-0.072254,2.919905,5.342581,-5.752352,-2.392228,3.444832],[0.571177,-4.024625,8.035152,8.328601,-2.094815,9.953617,-1.492169,7.406619,0.391471],[1.276756,3.048810,6.789614,-7.957210,9.662676,-1.000702,-5.767936,-2.203226,6.804734],[-4.660650,6.171587,4.693705,-3.180170,8.803026,0.200854,-6.631087,-2.044928,9.195132],[-8.869722,6.408184,8.482592,7.628809,-6.045268,-4.371721,4.698245,-6.826652,2.692739],[4.149965,-1.401984,0.694424,7.587768,-3.196248,-7.073218,-8.427056,9.661266,-9.706744],[3.877059,-8.059192,0.211230,2.844782,-0.205560,-5.226861,1.476327,4.965438,-4.211712],[-7.117827,-1.078028,-2.573439,-6.214373,-4.008997,-0.805618,-4.765394,-4.062557,8.923084],[6.701958,-6.134699,5.272835,6.502106,-7.001528,-6.996834,-0.761471,5.779400,0.704669],[0.377232,-0.703088,-0.576087,-7.208375,-0.945597,2.047481,-9.867634,-3.286248,-3.869137],[3.851719,9.276489,-0.214043,7.425805,-8.393306,-6.377611,-8.155588,8.914285,6.813284],[6.273600,2.384719,-4.459709,-5.465219,4.436572,9.237969,-2.289617,-2.896346,-3.838443],[3.386345,6.246749,-8.894311,1.601523,8.866943,0.258375,-4.302344,-0.247600,-4.153567],[9.059790,2.063857,-5.228358,-4.174202,-5.608677,-6.867606,-9.115456,-9.140663,5.777717]],[[2.387347,3.950608,8.389766,4.529974,5.491053,1.891655,-3.713166,-0.015215,-0.381827],[-2.690761,5.552662,6.168098,9.286613,3.119207,6.795085,3.147389,-4.750520,9.873243],[5.078460,2.429369,-2.581050,6.210194,5.377005,-1.605956,-4.172244,7.880578,1.607388],[5.539288,-0.607634,-9.675232,6.503571,-8.171434,-9.476541,6.346697,-0.243135,8.869960],[-4.836430,8.776940,-3.512182,8.465689,-6.789701,6.603167,7.708347,-9.111488,6.443885],[6.651667,-4.001452,-3.129763,3.958452,4.116467,7.350569,-6.641175,6.539707,9.150534],[2.428982,-9.751317,2.800581,-2.316420,-5.220596,-4.972367,6.957161,-0.200507,3.307961],[7.150182,-8.167399,-4.508431,4.687327,0.966867,-2.106760,-2.039880,1.472190,0.498343],[-2.806049,6.552767,0.911829,8.766078,2.779753,-4.053721,-2.327156,0.477683,-5.271029],[-4.945955,-9.991094,-5.280011,7.127784,7.217780,4.880554,7.746238,-7.445686,-6.445646],[3.934812,-4.574088,0.564469,7.924725,-5.068826,8.469743,2.093801,-7.459555,7.734898],[-5.440907,-3.187842,-0.313329,3.751877,3.890053,-3.401243,7.079975,8.487671,9.789278],[-1.504803,2.575910,6.526200,-1.424353,-6.666563,6.690071,3.062122,-2.683862,2.205748],[-9.308122,4.436123,-0.067402,0.429383,1.230349,3.684693,-3.753158,9.082867,1.249738],[-4.620753,1.891298,-3.763733,-1.832979,5.460221,3.748689,5.013022,1.131354,-1.938430]],[[6.735746,0.436156,-2.522953,6.508560,-4.532431,-0.326964,1.193917,0.064177,-7.760037],[6.089676,-2.065230,9.838051,7.497367,8.785882,9.638961,-2.502098,3.757336,8.435751],[5.505659,-9.019798,-2.465795,9.025434,4.913052,-5.338688,-0.684930,1.591960,-9.231112],[2.354411,3.826561,-3.024760,-0.245805,9.379788,-3.420158,3.500551,0.936248,-3.236685],[3.712482,-8.236130,-4.652432,-0.169651,-8.381902,1.186175,-7.313648,2.645932,9.290527],[7.806348,-9.114490,-3.669150,0.811472,-1.142868,4.258292,-3.981004,-7.011640,-0.688489],[-5.104150,-1.365588,-5.061048,9.841479,-3.807363,-4.117585,7.714640,9.411565,0.300794],[-8.656087,8.705100,2.698412,4.466114,6.936931,-2.257486,6.787613,-3.656284,-9.093076],[1.143178,-9.961567,-0.873686,-3.784369,-4.017490,4.490365,6.966752,-8.988814,3.252194],[3.771488,-1.702258,-6.845489,-0.978083,3.347448,8.223562,2.001063,3.827728,-7.814743],[5.565965,0.849952,-3.696528,5.028688,8.385249,8.457028,6.620205,5.771766,4.015439],[8.492205,4.039265,8.521035,-6.040247,-8.829738,-5.414929,8.752239,0.489207,8.655685],[8.875918,8.967716,-4.874542,5.266551,4.204217,2.073880,9.652861,6.034071,4.486932],[5.754160,5.807762,-5.439850,7.410247,4.464854,-2.295103,-2.170875,0.800976,-9.545337],[-4.952102,-4.439087,7.286759,8.876126,-4.733950,4.848737,6.157937,7.065418,-5.739808]],[[-1.001099,4.335349,-1.702053,-3.384225,8.732703,-4.950593,0.110553,-8.204257,9.732721],[-8.625326,-3.163831,0.304985,-5.594733,-6.760686,2.621402,2.294866,-6.611211,-5.516325],[1.944637,-8.106396,-2.426033,-0.384896,1.598371,1.433317,-6.228028,6.778899,-8.544128],[3.757511,6.170005,-1.529388,-3.558111,-3.777063,-1.854447,-7.858122,5.346920,3.768257],[7.217728,-6.081697,-1.472757,4.760890,8.727510,7.741286,3.212898,-7.365886,-2.255397],[-0.073403,6.822754,-2.930178,4.014024,1.197027,1.967467,-5.412574,-8.913291,2.933222],[2.867176,-5.785099,-6.337717,-9.818582,-7.794967,-6.439222,-2.437331,2.222703,-1.354645],[5.270856,-1.038424,-4.314259,3.278831,1.439778,4.724206,-5.526751,4.731945,8.706057],[-3.717518,-0.732526,5.657432,-7.145732,0.964315,6.565007,8.814697,7.963336,1.702989],[0.021245,-7.199048,-2.607069,2.054035,-7.323599,7.211345,-0.606659,-2.228647,-0.469308],[-7.869932,9.979019,4.147696,5.945286,2.305335,-5.916146,-6.552368,-2.008100,-2.618341],[8.710228,7.819750,8.839227,1.890361,7.456224,-4.984822,6.919237,-8.760159,-1.415337],[7.777393,-7.989099,-2.265608,1.256432,-9.694458,3.776702,9.787991,-0.494278,6.690599],[3.357264,-9.514153,-3.308048,8.283750,0.044330,-5.409007,0.860559,6.795771,-0.806881],[-9.320006,-5.449986,1.956242,-5.282277,-2.041780,-5.767594,-3.908724,0.608603,-5.229590]],[[1.172806,4.193436,6.275080,-5.555982,-9.885119,-3.168014,6.465427,-2.680190,0.725714],[2.544644,-2.441668,-9.265093,6.170904,9.387108,3.420138,-5.078514,8.974865,6.673264],[6.680144,9.641627,6.687656,2.301706,-6.376172,9.677723,7.665046,2.912014,-6.148856],[-5.481533,-0.341251,-2.399623,9.578710,-2.295564,5.350171,1.781779,0.031575,-1.635253],[-9.983386,8.251135,0.181121,-5.921573,-0.528381,7.365778,-4.256910,-4.990635,0.380945],[-2.858122,-9.288754,0.657606,2.256164,-8.956836,7.079005,6.023055,-3.249082,-5.505387],[0.314456,9.623300,0.615485,5.526657,-3.096996,-9.274778,-6.603877,0.743697,-6.825845],[-4.369060,4.687826,-1.763824,2.420599,6.686332,0.918514,-7.140791,-9.560088,-6.535658],[-1.379058,7.507290,5.543241,-7.529357,0.463553,-7.315825,-0.733725,4.217391,-2.034888],[-3.275165,0.925725,1.574252,9.106042,-8.496872,4.927605,2.650995,-4.861963,0.490144],[3.082553,4.601316,0.240477,-6.774823,9.187745,2.526286,0.767902,2.706965,6.985566],[7.409363,-0.770607,8.473178,-6.793116,8.534641,0.758816,1.515639,-5.146743,6.469415],[-7.447002,9.547764,9.678852,8.531056,-4.185133,-7.804074,-5.966792,1.420737,4.316807],[-3.264831,1.748978,-9.314697,-6.530269,9.790529,-6.605318,-2.453341,-8.336624,-3.969975],[2.548992,9.885899,1.113968,9.876270,7.272180,-9.825704,8.828274,1.295866,9.204627]],[[-4.817278,0.363945,-7.690691,-2.484649,-2.153766,7.313122,2.477945,8.194617,-5.467261],[-2.273916,-1.620537,-8.675256,-8.655955,7.507852,8.655900,4.207860,6.416610,9.913528],[-7.519478,-4.815128,7.620227,-3.699184,-3.085466,0.610499,-2.904526,0.373259,8.958639],[1.836075,6.467952,7.399071,2.227291,-2.536756,1.148686,8.139724,-4.617328,5.587533],[5.998241,-3.795265,9.688615,-7.998662,3.782837,-3.926244,-2.655023,-5.841531,-8.206566],[-2.597317,-2.132026,-0.159431,-0.129962,7.494972,-2.685714,-6.296578,-0.536779,4.001743],[-6.526003,5.808259,3.663620,9.860461,-3.275645,-6.483494,4.256592,-8.952324,9.001784],[-2.770861,-4.354776,-9.053126,-2.695389,-8.564935,0.582874,-8.027261,-7.389551,3.618672],[2.278056,1.103478,-4.707885,-7.517501,-5.953853,7.667079,-3.537128,4.951341,-8.572196],[9.248629,2.460847,5.649044,3.658704,-1.498254,-1.406204,-4.513823,-4.937425,2.977322],[7.394782,3.075444,-0.266286,2.633054,-1.656480,-3.921858,0.770345,4.153509,3.677958],[8.130517,-7.034463,-0.007293,-1.415440,-7.757107,-3.489310,8.686607,3.305366,2.450365],[-8.289369,-1.983090,-7.455890,1.237881,-2.739854,-0.024796,3.163574,5.240708,8.641075],[-3.614900,-7.128398,0.865068,-3.769797,-2.355197,9.368626,-2.983498,-4.097251,-1.717106],[0.456240,-2.517125,-1.062471,1.084268,7.499504,5.697673,8.698368,-7.605570,-6.528330]],[[-2.535743,-6.204041,-9.832017,1.758325,6.714727,-2.173981,-2.744757,6.052170,3.950254],[5.769069,-4.568268,8.828167,8.766547,0.044555,-6.993071,3.307815,1.494862,4.454507],[9.580247,-5.189786,2.982334,-6.032837,-0.561288,-0.115675,3.681290,-4.925900,-1.003143],[5.605684,-9.990645,5.103804,-4.176744,-5.781928,3.427293,-5.221499,-5.308659,2.617794],[2.875044,0.542726,-6.377263,8.510994,9.444637,3.509485,-9.337936,0.586944,6.495706],[8.167444,-3.716882,6.914708,-2.516185,-7.044232,-6.861181,-5.902457,-7.998173,9.760533],[8.363340,-3.126661,1.694511,4.842709,1.916152,-4.867979,8.121089,-2.916925,5.830044],[6.648036,7.643333,-5.973632,-6.548159,7.350017,-5.773242,9.051887,-7.665606,-7.053695],[9.499236,0.447901,1.870206,4.753729,7.035417,-7.896263,-4.423604,-5.346282,7.616210],[7.276118,3.234183,-7.793068,-3.277293,-5.125144,-8.288276,-0.056089,-0.573731,-4.669690],[3.402202,-4.795640,3.152605,-3.105577,5.897798,-0.329837,3.149944,-1.206806,-8.959967],[8.011169,-1.150028,1.344474,-8.554011,-0.005413,0.200655,-8.413191,-9.495879,-7.733741],[6.045161,8.057865,5.350048,-2.740382,-7.816247,-8.315493,1.672941,6.762391,0.811501],[-9.058643,-5.479373,-6.890706,3.871459,-8.263950,8.961703,-2.697149,7.119213,2.915115],[5.435245,-3.699460,-5.729097,-8.117787,-9.052229,4.756662,9.529547,2.461575,-9.640638]]], dtype = "float64")#candidate|2023|(7, 15, 9)|const|float64
bop_2024 = relay.power(uop_2005.astype('float32'), relay.reshape(const_2023.astype('float32'), relay.shape_of(uop_2005))) # shape=(7, 15, 9)
bop_2033 = relay.logical_or(uop_2021.astype('bool'), relay.reshape(uop_2005.astype('bool'), relay.shape_of(uop_2021))) # shape=(7, 15, 9)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_2036 = func_100_call()
call_2037 = func_100_call()
func_822_call = mod.get_global_var('func_822')
func_823_call = mutated_mod.get_global_var('func_823')
call_2046 = relay.TupleGetItem(func_822_call(), 0)
call_2047 = relay.TupleGetItem(func_823_call(), 0)
output = relay.Tuple([bop_1978,call_1992,call_1996,bop_2012,bop_2024,bop_2033,call_2036,call_2046,])
output2 = relay.Tuple([bop_1981,call_1993,call_1997,bop_2015,bop_2024,bop_2033,call_2037,call_2047,])
func_2050 = relay.Function([var_1977,], output)
mod['func_2050'] = func_2050
mod = relay.transform.InferType()(mod)
mutated_mod['func_2050'] = func_2050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2051 = relay.var("var_2051", dtype = "float32", shape = (7, 15, 9))#candidate|2051|(7, 15, 9)|var|float32
func_2050_call = mutated_mod.get_global_var('func_2050')
call_2052 = func_2050_call(var_2051)
output = call_2052
func_2053 = relay.Function([var_2051], output)
mutated_mod['func_2053'] = func_2053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_124_call = mod.get_global_var('func_124')
func_125_call = mutated_mod.get_global_var('func_125')
call_2104 = func_124_call()
call_2105 = func_124_call()
output = call_2104
output2 = call_2105
func_2118 = relay.Function([], output)
mod['func_2118'] = func_2118
mod = relay.transform.InferType()(mod)
output = func_2118()
func_2119 = relay.Function([], output)
mutated_mod['func_2119'] = func_2119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_2133 = relay.TupleGetItem(func_1764_call(), 1)
call_2134 = relay.TupleGetItem(func_1766_call(), 1)
func_910_call = mod.get_global_var('func_910')
func_911_call = mutated_mod.get_global_var('func_911')
call_2136 = relay.TupleGetItem(func_910_call(), 1)
call_2137 = relay.TupleGetItem(func_911_call(), 1)
uop_2144 = relay.acosh(call_2136.astype('float64')) # shape=(1, 15, 9)
uop_2146 = relay.acosh(call_2137.astype('float64')) # shape=(1, 15, 9)
uop_2147 = relay.cos(uop_2144.astype('float64')) # shape=(1, 15, 9)
uop_2149 = relay.cos(uop_2146.astype('float64')) # shape=(1, 15, 9)
bop_2162 = relay.floor_divide(uop_2147.astype('float64'), relay.reshape(call_2136.astype('float64'), relay.shape_of(uop_2147))) # shape=(1, 15, 9)
bop_2165 = relay.floor_divide(uop_2149.astype('float64'), relay.reshape(call_2137.astype('float64'), relay.shape_of(uop_2149))) # shape=(1, 15, 9)
func_352_call = mod.get_global_var('func_352')
func_355_call = mutated_mod.get_global_var('func_355')
var_2167 = relay.var("var_2167", dtype = "float32", shape = (81,))#candidate|2167|(81,)|var|float32
call_2166 = relay.TupleGetItem(func_352_call(relay.reshape(var_2167.astype('float32'), [81,])), 0)
call_2168 = relay.TupleGetItem(func_355_call(relay.reshape(var_2167.astype('float32'), [81,])), 0)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_2174 = relay.TupleGetItem(func_139_call(), 0)
call_2175 = relay.TupleGetItem(func_140_call(), 0)
output = relay.Tuple([call_2133,bop_2162,call_2166,var_2167,call_2174,])
output2 = relay.Tuple([call_2134,bop_2165,call_2168,var_2167,call_2175,])
func_2190 = relay.Function([var_2167,], output)
mod['func_2190'] = func_2190
mod = relay.transform.InferType()(mod)
mutated_mod['func_2190'] = func_2190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2191 = relay.var("var_2191", dtype = "float32", shape = (81,))#candidate|2191|(81,)|var|float32
func_2190_call = mutated_mod.get_global_var('func_2190')
call_2192 = func_2190_call(var_2191)
output = call_2192
func_2193 = relay.Function([var_2191], output)
mutated_mod['func_2193'] = func_2193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
call_2242 = relay.TupleGetItem(func_1197_call(), 0)
call_2243 = relay.TupleGetItem(func_1199_call(), 0)
output = call_2242
output2 = call_2243
func_2258 = relay.Function([], output)
mod['func_2258'] = func_2258
mod = relay.transform.InferType()(mod)
mutated_mod['func_2258'] = func_2258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2258_call = mutated_mod.get_global_var('func_2258')
call_2259 = func_2258_call()
output = call_2259
func_2260 = relay.Function([], output)
mutated_mod['func_2260'] = func_2260
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2306 = relay.var("var_2306", dtype = "uint32", shape = (4, 8, 7))#candidate|2306|(4, 8, 7)|var|uint32
var_2307 = relay.var("var_2307", dtype = "uint32", shape = (4, 8, 7))#candidate|2307|(4, 8, 7)|var|uint32
bop_2308 = relay.subtract(var_2306.astype('uint32'), relay.reshape(var_2307.astype('uint32'), relay.shape_of(var_2306))) # shape=(4, 8, 7)
output = bop_2308
output2 = bop_2308
func_2317 = relay.Function([var_2306,var_2307,], output)
mod['func_2317'] = func_2317
mod = relay.transform.InferType()(mod)
mutated_mod['func_2317'] = func_2317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mutated_mod.get_global_var('func_2317')
var_2319 = relay.var("var_2319", dtype = "uint32", shape = (4, 8, 7))#candidate|2319|(4, 8, 7)|var|uint32
var_2320 = relay.var("var_2320", dtype = "uint32", shape = (4, 8, 7))#candidate|2320|(4, 8, 7)|var|uint32
call_2318 = func_2317_call(var_2319,var_2320,)
output = call_2318
func_2321 = relay.Function([var_2319,var_2320,], output)
mutated_mod['func_2321'] = func_2321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1007_call = mod.get_global_var('func_1007')
func_1008_call = mutated_mod.get_global_var('func_1008')
call_2332 = func_1007_call()
call_2333 = func_1007_call()
func_1863_call = mod.get_global_var('func_1863')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_2334 = relay.TupleGetItem(func_1863_call(), 1)
call_2335 = relay.TupleGetItem(func_1864_call(), 1)
uop_2346 = relay.exp(call_2332.astype('float32')) # shape=(1, 15, 9)
uop_2348 = relay.exp(call_2333.astype('float32')) # shape=(1, 15, 9)
output = relay.Tuple([call_2334,uop_2346,])
output2 = relay.Tuple([call_2335,uop_2348,])
func_2356 = relay.Function([], output)
mod['func_2356'] = func_2356
mod = relay.transform.InferType()(mod)
mutated_mod['func_2356'] = func_2356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mutated_mod.get_global_var('func_2356')
call_2357 = func_2356_call()
output = call_2357
func_2358 = relay.Function([], output)
mutated_mod['func_2358'] = func_2358
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2407 = relay.const(-1, dtype = "int32")#candidate|2407|()|const|int32
var_2408 = relay.var("var_2408", dtype = "int32", shape = (1, 1, 16))#candidate|2408|(1, 1, 16)|var|int32
bop_2409 = relay.subtract(const_2407.astype('int32'), var_2408.astype('int32')) # shape=(1, 1, 16)
const_2443 = relay.const([[[9,-3,10,-3,-7,-8,10,8,-8,5,-7,10,7,2,-5,1],[10,-3,2,-3,-6,-10,4,-8,-10,4,10,-9,-2,-8,-1,-10],[-7,-1,-6,-9,-7,1,-8,-8,1,-6,-5,-8,5,3,9,6],[4,-4,-6,-5,4,8,4,-2,5,-6,2,-7,-3,10,-4,7],[-6,10,-6,4,-2,3,8,3,-3,6,-6,-2,-3,-1,1,-7],[-1,-8,4,8,-4,-6,-8,8,9,-7,-6,3,3,8,-4,-10],[4,1,-10,5,-1,8,9,1,9,2,8,7,-3,-5,10,1]],[[3,-1,2,1,-7,3,7,6,3,-1,7,-2,1,-5,-3,6],[-8,-1,4,-4,-2,-9,-10,-3,4,1,10,-2,-1,3,-3,1],[7,-4,3,2,-2,4,-7,-4,-1,-4,10,-5,5,4,8,-1],[-7,-3,-10,8,7,3,-9,7,-4,4,-9,5,-6,1,-6,6],[-7,6,6,-1,-7,9,3,-7,-8,-1,9,-2,4,-6,6,-6],[3,-2,7,1,10,-2,-5,8,-10,-4,-4,4,10,10,2,-10],[-7,1,8,10,2,-8,10,2,-6,9,-3,-8,2,8,6,-8]],[[-2,9,-3,-7,10,3,3,10,-2,-9,-1,-7,-7,-9,-4,-7],[8,-8,4,5,9,4,3,-1,-4,-9,7,9,10,-6,5,-1],[-9,3,2,-9,-7,-5,8,5,-6,6,10,-7,3,5,7,2],[-4,-9,-4,1,3,2,-2,3,3,1,-7,4,-2,-10,4,6],[7,-6,6,-4,3,-10,3,5,3,9,-4,1,-1,-6,-3,5],[-10,2,-10,4,-2,-10,-10,-3,1,-4,-7,5,-6,-5,5,-2],[4,-10,-2,-2,1,-1,9,5,-10,-6,-3,-4,-2,-9,-2,-2]],[[7,-3,-6,-3,-8,-9,10,6,-2,6,-5,-6,3,4,10,-4],[-9,4,-3,-4,3,8,9,5,8,9,-4,-10,4,-4,1,-9],[-4,-6,2,-6,5,-2,9,8,-1,-1,-3,3,7,10,-3,10],[4,4,8,-2,-5,-9,-2,-2,-3,-9,3,4,1,-10,2,4],[6,3,10,-8,10,9,-6,8,-5,-8,10,8,5,-8,8,7],[9,-7,-5,-6,-6,-8,8,-4,4,-1,5,8,9,-8,-7,10],[-5,7,-6,5,-9,-4,1,-10,-9,9,-10,3,4,-6,-8,-9]],[[7,-3,10,-5,-2,-4,7,10,-2,-10,-8,4,6,-3,10,9],[9,-2,-9,5,-8,-8,2,-10,9,-1,-7,-10,-4,-9,-6,-4],[10,1,-3,-3,-5,5,-1,4,-7,8,9,-6,3,-9,-4,2],[-9,3,9,-2,-9,4,1,1,-2,-1,8,-5,-5,-10,7,2],[4,5,-1,8,1,-3,9,-10,4,-3,9,3,-10,2,4,-1],[-9,-2,3,-2,3,9,-1,4,-10,-10,-2,-4,8,10,-10,-2],[9,-9,5,9,9,1,-8,-9,-9,1,4,4,1,-5,6,2]],[[-1,-8,-4,-6,6,5,10,4,3,-3,-1,10,-2,5,-10,3],[-7,8,9,-4,-1,1,-5,3,8,-6,4,1,10,-5,-2,-4],[1,-10,-7,-5,5,10,-1,-7,-10,8,-10,-9,6,1,-4,6],[-8,-6,-1,3,-9,4,-5,-8,6,8,-6,6,-5,-9,3,-2],[10,-6,-1,6,10,-7,-3,-2,3,-6,-1,9,9,-4,-3,-3],[-4,-3,6,4,-1,4,8,-4,-10,-7,3,6,6,-6,6,-2],[-6,7,6,9,2,1,1,-10,6,-1,-5,-2,-9,-8,6,7]]], dtype = "int32")#candidate|2443|(6, 7, 16)|const|int32
bop_2444 = relay.right_shift(var_2408.astype('uint8'), const_2443.astype('uint8')) # shape=(6, 7, 16)
output = relay.Tuple([bop_2409,bop_2444,])
output2 = relay.Tuple([bop_2409,bop_2444,])
func_2457 = relay.Function([var_2408,], output)
mod['func_2457'] = func_2457
mod = relay.transform.InferType()(mod)
mutated_mod['func_2457'] = func_2457
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2458 = relay.var("var_2458", dtype = "int32", shape = (1, 1, 16))#candidate|2458|(1, 1, 16)|var|int32
func_2457_call = mutated_mod.get_global_var('func_2457')
call_2459 = func_2457_call(var_2458)
output = call_2459
func_2460 = relay.Function([var_2458], output)
mutated_mod['func_2460'] = func_2460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2258_call = mod.get_global_var('func_2258')
func_2260_call = mutated_mod.get_global_var('func_2260')
call_2480 = func_2258_call()
call_2481 = func_2258_call()
func_1355_call = mod.get_global_var('func_1355')
func_1357_call = mutated_mod.get_global_var('func_1357')
call_2502 = relay.TupleGetItem(func_1355_call(), 2)
call_2503 = relay.TupleGetItem(func_1357_call(), 2)
output = relay.Tuple([call_2480,call_2502,])
output2 = relay.Tuple([call_2481,call_2503,])
func_2505 = relay.Function([], output)
mod['func_2505'] = func_2505
mod = relay.transform.InferType()(mod)
output = func_2505()
func_2506 = relay.Function([], output)
mutated_mod['func_2506'] = func_2506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_2507 = relay.TupleGetItem(func_1891_call(), 0)
call_2508 = relay.TupleGetItem(func_1892_call(), 0)
output = relay.Tuple([call_2507,])
output2 = relay.Tuple([call_2508,])
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
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_2572 = relay.TupleGetItem(func_2356_call(), 0)
call_2573 = relay.TupleGetItem(func_2358_call(), 0)
func_1159_call = mod.get_global_var('func_1159')
func_1162_call = mutated_mod.get_global_var('func_1162')
const_2598 = relay.const([[9.040333,-2.719359,4.988379,-4.241811,2.962954,3.540721,-9.811207,-3.926969,-7.412641,-7.877206,-8.559120,-4.097333,1.617454,4.969376,6.774626,8.268511,-0.335263,-8.402230],[-5.031282,-0.412231,-3.548902,4.564460,9.569306,9.344709,-2.058521,-1.845828,0.634647,-0.102324,2.277788,-3.728977,-3.024626,2.584157,-4.701459,6.687977,-2.809832,-1.166510],[1.565518,2.014819,-9.212832,-7.625832,2.089511,1.638435,-6.059001,5.730289,3.438448,-4.319221,8.240610,-3.448596,8.577420,-8.344122,3.172169,4.762564,0.244969,1.287938],[5.099943,-3.115384,7.368634,3.590004,-4.056966,3.321177,0.334075,4.189690,2.140144,-4.738139,4.061519,-8.639273,3.450479,5.744961,0.979601,-1.863995,0.208316,2.426033],[-8.636724,-6.893470,0.348855,-5.355632,9.801371,-8.560778,9.892003,-9.091631,2.651082,-8.068622,-8.405849,8.203455,-1.309296,-6.629719,9.878845,-0.808027,-2.463979,-6.805376],[-4.079097,-8.089052,-0.253813,-0.496590,7.894586,3.399870,-2.246794,-0.766317,9.590249,-1.746869,1.321659,9.118306,-4.703364,1.459076,-3.039924,-2.072064,-2.769761,9.086136],[1.827519,9.433164,-0.053216,-7.004919,-0.894517,2.344325,-8.635832,4.858669,-9.120105,-5.546675,3.131828,3.424711,7.882362,-1.296039,1.564939,6.596151,-0.255463,7.250277],[3.194477,1.624249,-4.350977,7.308398,-1.165174,9.631437,-9.469928,9.058132,6.532144,5.022650,-5.897220,-8.352871,1.953568,7.200475,-0.908113,-3.163350,-5.293132,4.248417],[-1.772376,1.321128,-8.252571,4.145773,4.421747,-4.321610,-6.722013,5.105251,3.078392,-5.024776,6.360348,-5.140736,-3.090802,2.002369,-7.683459,-3.600831,-9.311046,5.978215],[-0.945684,7.526071,7.123863,-9.403278,0.138971,7.695718,2.680558,-0.084903,1.746212,5.114343,8.520764,-2.394269,8.669906,8.926411,-0.093624,-5.605274,4.541618,-4.178336],[0.321433,-1.542460,1.900398,-3.709505,4.827277,2.566579,0.631323,6.895400,-9.503318,4.955013,-2.167890,3.080391,8.249079,9.684679,5.172662,-0.053092,-6.863994,4.862732],[-7.743458,-9.812842,-0.931948,-9.456352,-4.873056,9.628597,1.883293,1.270020,7.141537,-9.543655,-2.210954,3.077667,-4.947945,2.480930,4.179007,-7.866072,-4.555784,2.296373],[-8.250498,-0.597733,3.783597,0.502673,-4.428588,-3.734020,3.820005,7.519967,-7.961007,0.793688,-8.633162,9.817608,-4.189635,6.534099,0.587186,6.882298,-4.393270,-7.976806],[5.387015,-3.740958,-2.865909,6.597974,0.123179,-7.707805,-1.674422,-8.448327,-2.623093,-6.315166,6.387174,6.447015,-3.473335,8.368514,-5.680456,1.157455,6.487831,-5.526747],[-3.599543,-9.866387,-1.041870,-5.816512,-6.616588,6.625187,-0.223687,7.488333,8.920772,-2.420832,-9.016989,-2.535732,-8.085414,-9.982002,7.996202,0.438145,4.314074,8.424266],[-8.530995,-1.768618,8.080265,0.083224,4.790315,6.362807,3.716149,-3.486932,0.751003,6.177752,-2.302530,-4.148010,-5.259647,-6.050908,5.407083,9.007065,1.387989,-3.722052],[2.216713,-6.389867,1.028804,6.924702,-7.271983,-0.543719,-4.952761,4.494922,6.138056,-2.192289,0.533955,1.656525,-9.041298,5.503673,-0.237330,-8.171691,7.916274,-4.285338],[3.968877,-6.508632,-3.051571,4.917096,-6.962617,1.844027,-5.845810,5.428982,-5.845779,-2.184208,3.016206,-9.322178,-6.781090,6.248447,-4.454945,-2.596902,3.340618,4.893236],[2.962350,-3.773018,6.303123,7.515915,3.016312,7.188869,-0.445802,-6.473441,6.377693,5.604551,-3.884087,-2.746095,3.789130,-8.343941,1.874877,-0.315293,-9.106291,-3.418587],[-5.875115,-2.126776,-6.132872,-9.029520,0.223586,-5.932192,9.304838,-8.903904,-3.055246,-9.051434,8.988686,-1.451708,-1.266502,3.229635,1.598063,-9.362419,-4.262261,8.183352],[3.359666,2.412565,-6.150574,6.856535,8.256453,3.224401,-0.188483,5.043146,-8.164419,-9.340191,-2.194756,-5.340990,1.929806,-8.378602,2.169366,-0.009231,3.757150,9.309043],[1.216541,7.749324,9.915095,-3.422681,0.659928,0.646191,1.042124,-9.734122,-9.163862,0.199702,-0.469556,9.329890,7.278353,-2.853064,3.371315,6.941845,-2.369426,7.836792],[7.700054,-1.938193,-9.760321,9.509007,4.554431,3.538790,-3.642429,-0.440226,-4.847719,-3.885388,8.287715,-3.180635,-5.248169,-7.177952,2.294040,-0.934439,0.284530,3.711499],[9.804048,-4.767254,-8.782986,-5.061244,-8.687282,2.866194,-9.323389,5.905756,-0.026193,-7.788880,1.049889,-8.343623,-5.442864,7.395425,4.304663,0.103467,5.584478,5.768154],[-7.596625,-4.580711,-7.073175,8.798716,9.127090,3.408424,0.616105,3.076990,-4.114061,8.519883,-4.361647,-4.090588,7.760682,-9.692657,3.086530,-6.808743,5.240998,9.794409],[4.262658,-0.053740,7.970237,-9.173644,6.424902,4.287141,3.813583,4.416586,2.919227,2.974809,9.929236,-2.302204,-3.086618,-9.446710,2.387159,5.252981,5.880236,-9.816325],[0.439776,1.300491,-1.033120,-6.606681,2.887455,4.178274,-5.872801,4.733644,3.604015,-8.279410,-3.516000,3.717273,-8.403798,-6.532230,9.829537,-9.667010,-7.855232,4.843932],[-9.891645,-1.918686,5.928437,6.776415,4.282417,-7.766176,-3.028063,-6.851507,6.986994,-7.503686,-6.853760,6.421826,1.363017,2.489467,5.331629,-2.144551,-9.367838,4.858814],[8.558343,8.119711,1.880960,9.497168,7.801245,7.398206,6.050909,-6.526421,-5.742989,5.172830,-0.818622,1.867989,-5.690065,8.600205,1.329409,-5.963079,4.007651,0.473209],[4.199265,-5.356825,-5.792733,-7.887591,-8.935623,2.103420,-4.996233,-1.927946,6.441966,3.351247,-3.739608,9.640994,9.878367,-0.121597,3.245575,-0.350352,-4.875742,4.810146],[-0.356989,-2.937040,3.187055,0.802916,5.171814,-9.239292,-4.019601,-1.811967,-0.107612,-7.835308,5.588855,8.848694,-6.218255,-2.957919,-9.398915,7.951536,0.425169,6.832648],[3.534245,-9.012872,3.472879,-0.373704,-4.795506,-0.241853,-5.249681,1.921920,7.685176,-8.400630,-0.111902,-1.313725,9.115415,9.981694,7.414733,0.561349,5.418244,2.720407],[-3.980844,-5.630199,-6.083175,0.005971,0.766610,2.701505,1.429166,-7.236218,-5.346083,7.616745,-7.575006,-8.885920,2.142424,8.731765,1.420924,1.895890,-5.859031,3.839139],[-4.714875,2.162110,4.439789,-6.286152,-0.423519,-2.945352,1.563687,-5.176454,-2.319116,-1.092048,-5.444026,-0.573789,-6.817144,0.520695,-7.273363,-1.739986,-3.961665,-3.239343],[-5.461243,-4.179799,-4.355780,6.281242,-0.509564,6.742403,-7.745238,0.237392,8.701129,-6.122665,1.315423,-2.145956,-2.912181,5.783306,-3.994440,-8.790331,-9.726336,-2.463018],[7.386656,7.150986,2.021165,-0.227464,-0.821137,9.726122,-3.467665,2.530999,6.085381,0.194435,-2.875365,-4.708175,-3.505073,4.315853,-1.429302,3.145068,2.534859,1.671326],[-9.104256,-7.999954,0.023360,-9.226359,-6.984760,-9.104004,-8.865142,6.432558,-7.594044,8.569094,8.038394,7.887800,-5.273596,6.593469,5.777201,3.968146,4.853652,-7.691975],[6.116169,-4.529397,0.775471,7.104994,-4.761149,-6.494755,9.489790,2.984035,1.906030,-7.801567,-6.466188,7.301648,-3.275965,6.737200,6.574956,5.579480,-5.662155,-6.579157],[-4.582242,2.545369,-8.704397,1.018425,-8.332134,-0.917205,1.127377,2.208673,9.063562,-0.224328,0.558245,0.587463,6.485179,7.513581,-5.991913,1.460529,-6.419393,9.572017],[5.554690,-1.490714,0.532667,0.578048,7.908391,-7.652000,5.921739,-4.177531,-5.877307,3.992948,-6.063332,-6.558817,-3.832679,8.157328,-9.315821,-6.792615,8.282998,7.755181],[6.556004,-3.405603,-9.570158,2.299098,1.959753,-3.203889,7.764658,3.889596,7.578130,-6.151914,-7.714815,-4.492979,-8.766957,-0.461230,4.615537,2.402171,-2.899127,5.748853],[-5.151374,-1.468403,-9.194123,-7.743718,6.118486,-4.182442,2.429269,-2.838972,-3.777691,-6.327525,4.655202,2.925442,3.308928,-0.109842,-0.009034,-0.752926,-9.489550,-0.736197],[4.179723,4.351023,-3.371607,6.707242,-9.811756,1.828171,-8.246711,-5.589722,-0.935685,-8.679451,-1.791140,9.820271,-1.487309,3.121687,5.156714,-9.915780,-1.700678,3.329569],[2.553121,-2.216975,-6.403252,-7.147019,-9.202291,5.270843,-6.721971,-0.027656,-6.148813,4.173378,2.974687,1.183023,-2.204129,0.344895,1.057496,-6.591749,-9.059908,4.929746],[-4.151705,7.651409,-6.418691,-5.813003,0.605391,9.044244,-3.573989,-0.937148,8.332711,-5.069504,7.308505,8.274718,-5.401104,5.429234,-4.564856,-2.144356,3.777628,5.937998],[-6.916783,-8.669403,-0.470942,2.409838,3.407297,-8.561698,2.654684,-3.828439,8.042546,-8.668668,5.227845,-8.706575,-3.682264,5.135292,-1.623552,6.332014,-8.239332,-7.851724],[5.404063,4.667546,-4.218059,3.075040,2.046134,-2.220097,3.496029,-3.725206,5.299899,9.128035,4.927794,9.648919,0.698730,-0.791507,-4.542288,1.498036,-6.472718,-7.978924],[-6.081728,2.367268,-3.312059,-3.584057,-0.023792,-6.118305,4.014707,2.525661,-6.396835,3.436258,4.828463,0.561538,-9.216742,6.773824,-9.485102,3.242910,0.350648,-6.092995],[0.262578,-5.904722,3.012861,9.367000,-2.190346,-2.604316,4.978857,-8.774037,0.601466,-3.249733,-2.422900,6.275299,-7.523882,-7.018724,5.260933,3.361605,2.836127,-6.933853],[-3.426766,-8.805811,-6.095572,-1.023238,-1.064610,-2.319661,-8.074801,8.833488,-1.716648,6.299498,-5.083237,-9.082007,-5.531122,-4.704023,0.501156,5.757279,-6.457119,-4.610344],[-1.881322,-8.506116,-6.045946,-7.678024,6.411339,0.005198,-6.723371,-7.616903,-6.547200,-4.567573,-8.551331,5.241210,7.847461,-5.999832,-5.287478,-9.610275,1.877757,1.527278],[7.624186,-4.574708,2.002615,-5.543990,3.832864,-5.934683,-3.205984,-8.819844,2.440406,-5.725142,-1.446191,-0.039057,-0.649326,3.411693,3.477497,7.891550,2.763046,-1.116061],[2.363928,-4.154188,1.946677,0.245203,-4.766105,5.778202,1.321753,-4.037872,-6.810273,-3.939765,-0.411823,-6.848690,-1.854082,-8.823011,5.760665,-0.599167,-1.663085,0.356366],[-0.789217,6.566042,0.735940,-1.701435,-2.074019,-8.347875,-2.941070,9.362906,7.652972,-1.985746,9.272293,5.250646,6.256374,-4.850525,-3.110337,-6.498511,-9.874148,7.118102],[-8.788995,-3.594042,7.199991,8.242135,3.479316,-8.726775,-9.636617,-7.266511,8.274696,-3.533186,7.484096,-1.023977,9.706253,-8.249708,-3.658812,5.646936,-1.595365,-1.050548],[-3.501150,9.852734,-2.264733,-2.718655,-3.324627,2.668022,-2.072046,8.204657,-2.762156,-6.647555,-3.884607,9.876948,-9.957670,7.691068,-4.886950,-6.639356,5.631034,-0.266434],[6.486816,-1.521884,9.172964,-6.167400,0.861049,3.883019,9.927953,1.519962,9.674376,8.232674,5.371583,-0.478343,-6.735802,0.775606,-4.281141,4.628235,-5.175632,1.677084],[1.981526,-6.340495,7.273488,-3.231323,6.240044,-2.916334,-1.503702,-6.207001,-3.063909,8.099973,-8.112559,-8.148748,-3.042577,-4.926789,8.514959,-3.867580,4.801074,-7.606395],[2.012109,-4.560368,-3.127617,7.165187,-8.132370,1.529115,-8.647257,9.549351,8.428627,0.685149,5.101187,-9.190400,5.381214,-1.222631,5.163543,-4.124020,8.722420,6.220225],[3.043808,7.402981,6.738542,5.806119,3.873086,-1.295353,-7.489274,0.927221,2.050858,7.905599,-3.969379,-7.099029,-4.228959,-6.451889,7.345126,0.772252,-1.089525,-1.810927],[7.256413,1.493107,-0.590890,2.135903,4.236074,-1.294043,7.521636,-2.574661,7.409729,2.621570,0.040628,-3.968903,-8.001953,3.800834,-7.558105,-4.635973,2.308152,-4.932926],[0.786312,3.030910,-0.621997,8.609317,6.510792,-6.381702,-1.997234,-8.705047,0.506578,-2.146244,-2.983618,2.671094,7.328160,5.038412,6.107083,-7.539622,9.754520,-8.893422],[-6.731351,7.005467,5.252333,-7.985709,-9.451559,3.779455,9.484535,8.285772,6.151739,-0.044711,-4.704728,-3.744787,-0.729773,-5.996735,-2.468587,7.239288,-6.518311,-7.004094],[-7.550920,-1.788465,3.578619,7.358605,5.190999,-6.329707,2.277744,-5.246085,-8.605952,1.234828,4.604370,0.548871,-0.985260,-1.411555,1.219983,-6.134525,-4.834605,-8.972931],[-7.382039,-9.346294,-7.881023,2.585359,-7.680328,4.467578,-8.631255,6.038086,-1.951474,6.728666,9.917177,-3.211785,-5.221920,4.039766,3.704864,-1.145869,8.049026,1.352609],[0.974378,2.239069,-0.102520,9.923343,8.052042,7.458912,5.184555,8.963169,-7.885767,0.065944,-1.740232,2.550425,5.166434,-3.177003,5.665844,-6.987489,-1.255881,-4.430201],[9.508396,0.685584,-5.135353,-0.885237,0.706860,-2.322565,2.317255,-1.570910,-4.509745,5.149805,6.939323,-2.448122,-3.780189,4.136293,-6.670408,7.026670,1.324606,1.785197],[7.252976,7.673274,4.917329,9.986254,-1.684087,-7.647237,0.482050,-4.917410,4.993800,0.669857,4.034766,-2.933268,-8.541651,9.958790,-1.331302,9.491557,9.831705,-8.031352],[7.832954,7.960361,4.782809,-0.198781,-1.531131,3.127619,-0.273967,5.213468,-1.448838,6.802311,7.108834,-7.307985,7.155439,-9.282968,2.801417,0.031748,-7.825584,-7.303664],[7.823642,-0.820534,5.041730,7.995075,2.060531,9.999546,1.293212,-9.089175,-3.576375,-6.524433,5.583651,-1.283757,-5.819318,2.046639,-5.614338,-7.499256,-3.534930,2.227051],[2.629812,8.055383,3.015152,-0.702370,-6.965026,-6.746196,9.630425,-1.957467,7.981194,3.446636,0.988218,-1.204443,-6.858246,4.352083,5.840597,-0.773945,5.661788,2.638263],[1.575859,7.603404,6.250880,-2.601373,4.160903,4.651570,4.372270,-2.132036,1.052773,-1.525130,8.614745,-1.614850,0.646254,4.482233,5.555003,8.552049,-0.822809,-0.150501],[-4.704276,4.895345,6.450579,-7.933895,0.094783,8.847320,7.568980,2.712104,3.730168,-4.477088,-1.742300,-2.647830,-7.224639,-3.436661,-1.958422,-7.169009,2.086909,-7.814952],[-1.189493,3.850663,9.992317,-0.923182,2.649535,-2.450123,-2.165569,4.020473,-6.862365,-3.940766,5.699569,-1.601240,0.548389,9.469513,-8.226383,9.459012,-5.536474,-4.630139],[-1.148813,8.861175,-9.594390,-2.110998,-8.300024,-4.971931,7.011915,9.143718,6.585907,0.173562,1.547643,-4.041993,-9.535718,-9.304757,-6.790090,0.200240,-1.932256,-4.134701],[-9.291917,6.547294,-5.145127,9.858922,-7.082246,3.648205,-6.395597,-5.262322,4.454758,2.267071,-0.809250,-4.892311,4.444132,4.248526,-6.867949,-8.570183,7.073616,6.034877],[9.725733,1.379577,-3.890832,-2.676623,4.108869,-3.186254,6.695199,6.246107,9.672303,-2.964436,2.991231,-8.769108,-8.325757,-8.216131,-0.599921,1.266366,-4.583407,2.220071],[6.121341,-0.616832,-6.496361,5.493113,-5.371461,-3.341828,0.327558,-2.960877,-6.809089,-6.668440,-2.275275,-1.404719,4.293442,-7.467018,4.943822,-7.111170,5.293781,7.875185],[8.374846,0.728846,8.775224,7.652908,5.816189,4.465851,6.384109,-4.984314,-4.752295,-3.473430,-9.930195,-3.927875,6.335091,4.578413,2.632021,-7.760765,4.010825,-3.239096],[4.899304,0.774992,-7.800483,5.753529,8.760966,1.709642,-6.336075,4.277077,-2.662371,-2.576086,-9.240475,7.909801,9.058337,-3.836478,0.982836,7.870903,-4.407839,5.807466],[-7.436687,-8.100975,-3.326073,7.330986,-6.099046,-4.568861,-7.487643,-9.203626,-5.051992,-3.492880,7.455173,-9.600503,-9.798355,-7.887500,0.918393,3.659515,-7.170300,3.849517],[0.978423,2.149572,5.995495,-9.794282,3.139613,-9.505450,-7.056998,9.933195,5.280609,2.186039,9.446157,-5.724773,8.734100,-2.505162,-8.341962,5.396858,4.646324,2.544059],[-5.340626,-5.724043,-9.771851,2.078643,-9.163561,-9.064960,-7.506772,8.880607,7.070106,-2.056963,4.230564,-6.241869,-9.478796,6.889614,0.913807,-9.408610,-8.920444,3.901786],[8.197784,-4.525590,6.992545,5.629571,-7.378431,4.249040,1.818834,-0.948228,4.317443,-7.479983,-4.725167,9.934021,-8.382335,3.193587,-8.801814,8.910110,3.576568,8.147472],[-4.943206,0.275524,9.696623,1.910064,-4.353664,3.454755,-8.600181,-5.200735,5.872602,-7.558992,8.282357,9.253493,-6.446201,-5.240267,-9.863194,-5.864456,-9.143562,5.195596],[1.166915,-7.783470,-2.726954,8.647631,4.835125,-7.478749,3.443119,-3.876631,-7.020506,-3.953062,-9.022154,2.867295,6.613170,-8.303485,2.470174,0.986364,-7.915411,-0.705384],[-8.560043,2.874601,2.452299,-9.802049,0.798752,-4.044779,-8.774770,-4.838548,4.750708,0.269784,-5.284492,-3.677486,9.734471,-7.331778,-4.843553,4.337212,-0.050101,-0.610272],[-8.635259,-7.392530,-1.615209,7.729890,6.234520,4.952919,2.803437,4.518737,-0.699684,7.040461,-3.285262,8.418240,1.359210,7.330589,-9.005365,3.054118,-1.717040,-5.193096],[-7.277593,-0.746012,6.170180,-6.698740,-1.464063,-5.603488,-5.291565,2.861788,7.887791,6.572977,5.872595,-2.489043,-8.742967,-6.707643,8.340491,9.719319,-9.178335,-1.185973],[-8.468348,7.800907,-5.074070,1.663812,7.748648,7.518165,-8.991533,0.817857,4.311710,1.674778,-9.351958,5.764282,-9.939967,8.352123,-7.703388,-9.612575,0.583079,7.224518]], dtype = "float32")#candidate|2598|(90, 18)|const|float32
var_2599 = relay.var("var_2599", dtype = "float32", shape = (27, 3))#candidate|2599|(27, 3)|var|float32
call_2597 = relay.TupleGetItem(func_1159_call(relay.reshape(const_2598.astype('float32'), [1620,]), relay.reshape(var_2599.astype('float32'), [81,]), ), 2)
call_2600 = relay.TupleGetItem(func_1162_call(relay.reshape(const_2598.astype('float32'), [1620,]), relay.reshape(var_2599.astype('float32'), [81,]), ), 2)
output = relay.Tuple([call_2572,call_2597,const_2598,var_2599,])
output2 = relay.Tuple([call_2573,call_2600,const_2598,var_2599,])
func_2603 = relay.Function([var_2599,], output)
mod['func_2603'] = func_2603
mod = relay.transform.InferType()(mod)
var_2604 = relay.var("var_2604", dtype = "float32", shape = (27, 3))#candidate|2604|(27, 3)|var|float32
output = func_2603(var_2604)
func_2605 = relay.Function([var_2604], output)
mutated_mod['func_2605'] = func_2605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_2660 = relay.TupleGetItem(func_586_call(), 1)
call_2661 = relay.TupleGetItem(func_588_call(), 1)
output = relay.Tuple([call_2660,])
output2 = relay.Tuple([call_2661,])
func_2662 = relay.Function([], output)
mod['func_2662'] = func_2662
mod = relay.transform.InferType()(mod)
mutated_mod['func_2662'] = func_2662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2662_call = mutated_mod.get_global_var('func_2662')
call_2663 = func_2662_call()
output = call_2663
func_2664 = relay.Function([], output)
mutated_mod['func_2664'] = func_2664
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2880 = relay.var("var_2880", dtype = "float32", shape = (2, 14, 10))#candidate|2880|(2, 14, 10)|var|float32
uop_2881 = relay.asin(var_2880.astype('float32')) # shape=(2, 14, 10)
output = relay.Tuple([uop_2881,])
output2 = relay.Tuple([uop_2881,])
func_2887 = relay.Function([var_2880,], output)
mod['func_2887'] = func_2887
mod = relay.transform.InferType()(mod)
mutated_mod['func_2887'] = func_2887
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2888 = relay.var("var_2888", dtype = "float32", shape = (2, 14, 10))#candidate|2888|(2, 14, 10)|var|float32
func_2887_call = mutated_mod.get_global_var('func_2887')
call_2889 = func_2887_call(var_2888)
output = call_2889
func_2890 = relay.Function([var_2888], output)
mutated_mod['func_2890'] = func_2890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_2897 = relay.TupleGetItem(func_1070_call(), 0)
call_2898 = relay.TupleGetItem(func_1072_call(), 0)
output = call_2897
output2 = call_2898
func_2903 = relay.Function([], output)
mod['func_2903'] = func_2903
mod = relay.transform.InferType()(mod)
mutated_mod['func_2903'] = func_2903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2903_call = mutated_mod.get_global_var('func_2903')
call_2904 = func_2903_call()
output = call_2904
func_2905 = relay.Function([], output)
mutated_mod['func_2905'] = func_2905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_2910 = relay.TupleGetItem(func_1764_call(), 1)
call_2911 = relay.TupleGetItem(func_1766_call(), 1)
uop_2914 = relay.atanh(call_2910.astype('float32')) # shape=(1, 15, 9)
uop_2916 = relay.atanh(call_2911.astype('float32')) # shape=(1, 15, 9)
bop_2918 = relay.maximum(uop_2914.astype('float32'), relay.reshape(call_2910.astype('float32'), relay.shape_of(uop_2914))) # shape=(1, 15, 9)
bop_2921 = relay.maximum(uop_2916.astype('float32'), relay.reshape(call_2911.astype('float32'), relay.shape_of(uop_2916))) # shape=(1, 15, 9)
output = relay.Tuple([bop_2918,])
output2 = relay.Tuple([bop_2921,])
func_2922 = relay.Function([], output)
mod['func_2922'] = func_2922
mod = relay.transform.InferType()(mod)
mutated_mod['func_2922'] = func_2922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2922_call = mutated_mod.get_global_var('func_2922')
call_2923 = func_2922_call()
output = call_2923
func_2924 = relay.Function([], output)
mutated_mod['func_2924'] = func_2924
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2947 = relay.var("var_2947", dtype = "float64", shape = (8, 4, 10))#candidate|2947|(8, 4, 10)|var|float64
uop_2948 = relay.sin(var_2947.astype('float64')) # shape=(8, 4, 10)
output = uop_2948
output2 = uop_2948
func_2950 = relay.Function([var_2947,], output)
mod['func_2950'] = func_2950
mod = relay.transform.InferType()(mod)
var_2951 = relay.var("var_2951", dtype = "float64", shape = (8, 4, 10))#candidate|2951|(8, 4, 10)|var|float64
output = func_2950(var_2951)
func_2952 = relay.Function([var_2951], output)
mutated_mod['func_2952'] = func_2952
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2978 = relay.var("var_2978", dtype = "float32", shape = (14, 6, 11))#candidate|2978|(14, 6, 11)|var|float32
uop_2979 = relay.acosh(var_2978.astype('float32')) # shape=(14, 6, 11)
func_1652_call = mod.get_global_var('func_1652')
func_1657_call = mutated_mod.get_global_var('func_1657')
var_2998 = relay.var("var_2998", dtype = "float64", shape = (8, 84))#candidate|2998|(8, 84)|var|float64
const_2999 = relay.const([-2.421209,-9.078007,7.956023,-8.571834,8.135548,9.768165,-3.886138,7.062320,6.258118,-0.921787,7.778306,-9.439436,-0.737906,-7.191319,-3.326650,-0.299443,3.426790,5.603949,-4.594623,-3.323097,3.552603,8.778449,-2.034343,7.916736,-9.752934,6.717573,4.283875,-4.104902,3.582359,5.546566,7.319460,-5.741120,-8.270423,5.476187,8.507761,-0.156713,-5.137111,5.635644,8.717016,-5.864490,-6.941431,7.843436,0.014200,-0.810018,-4.575720,-3.130377,5.239048,-9.137802,-3.509630,-4.406463,0.225603,-6.271354,0.037262,-0.205573,-2.064420,-1.625212,-9.366329,-2.663023,3.951656,-9.366635,-4.484257,4.637928,3.341706,2.082355,-6.990713,-1.995145,7.075406,1.167022,-3.295359,5.694743,-7.921478,2.414901,2.909122,-1.146746,-0.091694,6.751244,5.839018,5.845153,-2.954782,-8.176802,-6.462110,5.599303,0.460437,-2.138454,-7.864200,-0.558388,-4.050897,-1.788736,-9.661884,-3.517239,2.147471,1.636738,3.771364,-7.241057,-7.884327,-8.332071,5.715561,-6.711367,-9.180856,-7.546194,-6.071463,8.506510,-7.850758,-1.724315,-6.124985,-3.334556,-4.097684,-3.765196,-0.931854,-3.088857,9.273115,4.295644,-8.331336,3.889007,3.165716,5.482251,-3.463789,-6.060276,-3.752355,3.203133,7.083026,0.784475,-6.465738,2.377903,-2.780447,3.192511,-4.308443,-6.018129,-6.139571,6.951615,8.751365,7.630965,1.474955,-8.025307,-9.916064,-0.136400,1.829300,-2.478783,0.681885,-2.987491,1.726308,1.408510,0.637928,-5.788464,2.387733,5.559722,-0.897350,8.250346,-0.604007,-9.030443,0.619256,-7.963463,-5.723426,-5.524174,8.010567,2.826696,-2.354708,-1.471109,-3.579675,3.614335,7.438038,-5.692111,8.447666,1.626140,6.520138,4.983254,4.429318,-1.938487,-0.034509,4.665223,1.485458,-6.986966,-6.536600,5.287514,8.032762,-1.934444,5.392394,-5.209424,-1.154070,-9.680878,8.509632,7.686464,-2.045114,-2.829381,-6.376798,-9.167342,-4.937021,-5.142789,9.013702,1.538432,-3.457166,1.573688,-9.915658,6.438767,-5.221220,2.615034,2.143426,-2.603444,-0.329933,-2.688572,-4.838092,-9.725936,0.554124,9.268609,5.513605,5.325278,6.663609,3.239577,-1.035646,-4.456418,1.693545,0.984480,-2.637367,-0.974380,-8.045056,-3.302243,1.275161,-0.891689,0.789550,5.308433,-7.336511,-0.390195,-9.123836,-0.622690,-8.179530,9.632020,-7.034937,-4.105140,-3.783508,6.294101,0.134065,0.574896,-9.511028,4.005587,-3.121812,-4.211144,9.181379,-4.778546,1.180072,0.958101,1.196589,6.711054,3.023550,0.089842,-6.409973,-0.814144,-5.705925,-1.954517,0.026301,-1.444751,-9.278645,5.030975,7.999715,2.039010,-1.515289,6.019977,2.821578,6.650421,-8.642778,-9.976966,1.342451,1.972301,8.560372,-0.649068,3.206865,-7.021012,-0.652409,-0.640706,8.152141,-8.626080], dtype = "float32")#candidate|2999|(270,)|const|float32
call_2997 = relay.TupleGetItem(func_1652_call(relay.reshape(var_2998.astype('float64'), [7, 16, 6]), relay.reshape(var_2998.astype('float64'), [7, 16, 6]), relay.reshape(const_2999.astype('float32'), [270,]), ), 1)
call_3000 = relay.TupleGetItem(func_1657_call(relay.reshape(var_2998.astype('float64'), [7, 16, 6]), relay.reshape(var_2998.astype('float64'), [7, 16, 6]), relay.reshape(const_2999.astype('float32'), [270,]), ), 1)
uop_3002 = relay.tan(uop_2979.astype('float32')) # shape=(14, 6, 11)
output = relay.Tuple([call_2997,var_2998,const_2999,uop_3002,])
output2 = relay.Tuple([call_3000,var_2998,const_2999,uop_3002,])
func_3007 = relay.Function([var_2978,var_2998,], output)
mod['func_3007'] = func_3007
mod = relay.transform.InferType()(mod)
mutated_mod['func_3007'] = func_3007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3007_call = mutated_mod.get_global_var('func_3007')
var_3009 = relay.var("var_3009", dtype = "float32", shape = (14, 6, 11))#candidate|3009|(14, 6, 11)|var|float32
var_3010 = relay.var("var_3010", dtype = "float64", shape = (8, 84))#candidate|3010|(8, 84)|var|float64
call_3008 = func_3007_call(var_3009,var_3010,)
output = call_3008
func_3011 = relay.Function([var_3009,var_3010,], output)
mutated_mod['func_3011'] = func_3011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2662_call = mod.get_global_var('func_2662')
func_2664_call = mutated_mod.get_global_var('func_2664')
call_3062 = relay.TupleGetItem(func_2662_call(), 0)
call_3063 = relay.TupleGetItem(func_2664_call(), 0)
output = relay.Tuple([call_3062,])
output2 = relay.Tuple([call_3063,])
func_3071 = relay.Function([], output)
mod['func_3071'] = func_3071
mod = relay.transform.InferType()(mod)
output = func_3071()
func_3072 = relay.Function([], output)
mutated_mod['func_3072'] = func_3072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mod.get_global_var('func_1863')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_3209 = relay.TupleGetItem(func_1863_call(), 0)
call_3210 = relay.TupleGetItem(func_1864_call(), 0)
func_822_call = mod.get_global_var('func_822')
func_823_call = mutated_mod.get_global_var('func_823')
call_3219 = relay.TupleGetItem(func_822_call(), 0)
call_3220 = relay.TupleGetItem(func_823_call(), 0)
output = relay.Tuple([call_3209,call_3219,])
output2 = relay.Tuple([call_3210,call_3220,])
func_3228 = relay.Function([], output)
mod['func_3228'] = func_3228
mod = relay.transform.InferType()(mod)
mutated_mod['func_3228'] = func_3228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3228_call = mutated_mod.get_global_var('func_3228')
call_3229 = func_3228_call()
output = call_3229
func_3230 = relay.Function([], output)
mutated_mod['func_3230'] = func_3230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3071_call = mod.get_global_var('func_3071')
func_3072_call = mutated_mod.get_global_var('func_3072')
call_3240 = relay.TupleGetItem(func_3071_call(), 0)
call_3241 = relay.TupleGetItem(func_3072_call(), 0)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_3255 = relay.TupleGetItem(func_2511_call(), 0)
call_3256 = relay.TupleGetItem(func_2513_call(), 0)
output = relay.Tuple([call_3240,call_3255,])
output2 = relay.Tuple([call_3241,call_3256,])
func_3262 = relay.Function([], output)
mod['func_3262'] = func_3262
mod = relay.transform.InferType()(mod)
output = func_3262()
func_3263 = relay.Function([], output)
mutated_mod['func_3263'] = func_3263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_3330 = relay.TupleGetItem(func_1891_call(), 0)
call_3331 = relay.TupleGetItem(func_1892_call(), 0)
const_3341 = relay.const([[[6.570872,4.219203,-3.540891,-7.029841,-3.111779,6.832725,-3.923367,4.482059,9.964224],[0.117757,-5.120990,1.084667,-4.313404,-4.600423,-0.622531,-1.847401,-1.771886,8.778158],[-2.272544,-5.090681,-5.030408,-0.627425,8.532053,-6.849988,-4.349447,-6.043936,-4.927200],[-7.964783,-9.727202,3.169892,-3.686053,-4.240281,7.303772,4.418209,3.618349,-7.903700],[3.368474,6.314005,4.340917,0.420820,8.965054,-1.485832,-2.693590,-7.358214,5.901293],[3.807622,7.657258,-9.715004,4.903369,-1.414893,2.612223,-7.074657,9.876985,7.379056],[2.138932,3.505745,-7.400160,5.187084,-1.592051,-9.225296,8.187139,6.464353,8.387631],[1.633895,5.758451,-8.598396,-3.252571,-9.841950,-8.417896,-7.265234,-7.200048,-4.327937],[8.387168,7.491053,8.282892,7.624221,8.534356,3.949229,1.710297,-1.625583,-3.060193],[5.872100,6.009770,-5.406569,-2.235922,-6.266548,-9.981836,7.931348,-5.462184,9.354812],[-3.786838,-5.857626,6.338403,8.017180,-0.078565,-0.808688,-6.570830,7.445968,0.726993],[6.683603,9.651873,-4.885476,-3.763769,1.491069,1.416533,-2.428767,-0.528921,1.565564],[-4.710885,-4.281439,-9.451456,4.690307,-1.791169,2.825038,-3.167364,0.300826,-5.399828],[-6.150391,-7.593879,1.993503,-5.512756,3.777647,-6.504258,5.256160,8.430980,1.691385],[-2.367927,-3.762078,4.116756,-8.473129,-3.791580,7.390127,5.818472,1.352476,-6.907339]],[[1.560501,-4.185546,2.062093,-9.583178,2.399781,-4.231490,0.109666,1.267919,7.536286],[9.362653,4.311258,-4.397150,-4.258293,-1.468700,1.680514,-9.201920,3.264862,4.044873],[4.631576,7.857602,-4.630317,3.621307,-6.804845,4.100841,-4.754291,9.223589,2.078707],[-1.936132,-7.158039,1.084337,1.242497,-2.708034,9.177357,7.244296,0.268159,2.907178],[-8.112686,-0.963035,-6.311480,1.925693,-9.802725,-2.313274,-5.733442,-7.475144,8.765398],[-5.616112,6.403370,4.380447,-4.415377,-6.346192,-6.822825,0.773887,-8.797427,5.224102],[-4.351405,1.274244,-7.875833,-1.957598,8.847425,0.233413,-3.067885,2.408594,-8.131779],[-8.732430,-0.235983,2.891658,0.257881,1.918485,-0.997723,-4.674830,6.534938,9.436415],[0.751760,-4.094679,-9.587815,4.876001,9.588958,1.640037,4.747674,9.648328,-8.913411],[-9.597634,2.333337,7.496454,0.697241,-0.238665,-9.028573,-2.806997,3.488595,-9.789052],[-3.087726,9.552850,-1.870396,4.643543,-9.270858,3.102989,7.193649,-2.375377,-9.765136],[-7.353993,4.237659,-7.284693,0.841868,6.575811,-7.465143,-0.229883,1.800943,-4.504201],[-4.139387,-7.429414,-8.314725,6.920062,7.324751,9.215794,-1.253286,7.949608,-0.190564],[7.286505,-2.011486,4.989460,-2.789787,8.584226,8.284309,2.703061,-7.709894,-7.056748],[-2.818967,-5.117987,-3.321038,0.853371,-6.687166,-8.195302,-4.411630,-9.124851,0.200869]],[[9.486047,0.939732,3.004192,0.396696,8.727421,-8.684123,-4.972629,5.367757,5.767057],[-3.799568,-5.997444,8.105251,-1.022803,-4.515771,0.526650,-4.715757,3.984126,1.845836],[-7.992688,-7.126638,-7.142715,1.385547,6.795692,-5.297248,-2.844905,9.266044,9.321010],[-9.353182,-9.285305,-3.194053,-6.345227,8.558294,-9.353112,-8.377305,0.715473,-1.609029],[-4.668759,-1.464264,5.645751,-3.348772,-7.037875,-1.815312,-0.232186,9.667602,-6.476133],[-1.544273,-2.254244,-2.179731,1.098485,9.367163,6.209297,-1.283535,2.663580,0.372648],[0.638069,3.477574,3.116166,9.120021,-4.898970,7.645452,-8.012577,8.469321,2.560317],[-9.266246,-4.692527,7.239413,1.392745,1.356194,-3.535543,4.513323,-7.983144,7.192434],[6.700098,-1.678434,6.751350,-9.347548,5.796214,-6.102018,9.726361,1.292018,-0.353073],[-9.536469,8.235273,9.041643,-0.837380,6.336269,2.451781,2.412193,-3.852898,-0.290077],[5.494904,3.179027,-0.349231,0.469679,-6.447190,5.050704,9.775112,8.591620,-3.451312],[-6.537107,9.802377,5.191949,3.244484,8.472182,-2.708704,5.499894,-6.212394,1.524601],[5.425998,2.508579,0.358058,-1.714113,-1.537442,1.624948,-5.387602,2.644293,-8.561978],[-3.580941,4.368958,7.528884,7.968174,5.745233,4.495304,-4.388329,9.908056,0.037369],[8.387258,4.131293,2.855055,-4.641135,3.238283,5.314573,-4.752797,0.330922,-9.341749]],[[-7.493062,2.412352,4.293204,-9.665399,8.462874,7.530935,-5.229435,6.629774,-7.388458],[7.553442,-6.969024,8.405392,-6.343170,-2.143421,3.358155,-2.787672,-5.524607,-4.023883],[-8.684274,-8.190779,-2.604674,-5.678981,-7.010890,1.119347,-4.586980,2.699976,4.696988],[5.892900,-9.363925,7.879760,-0.039742,5.812685,7.396486,-9.628002,-5.278493,-4.944113],[0.953429,-6.278778,-2.357390,-6.275975,-4.964364,2.646480,-1.341672,5.918893,-6.175894],[2.413358,-2.306210,-2.978611,-7.965149,5.411190,2.464675,8.753490,8.982804,-0.081328],[3.540296,-6.400981,-1.771664,0.246610,-9.835155,4.248996,4.618546,3.465615,-9.057777],[-1.822077,1.225413,2.624373,5.886729,0.009415,-6.278261,-3.248250,-1.464315,1.424769],[-7.813637,-9.208342,5.347120,-7.549678,-3.728471,-0.761256,2.843578,6.309819,4.320244],[8.304178,9.972683,1.875974,-9.958846,-9.043069,-4.085697,0.824225,-2.951438,-1.503128],[3.761054,7.723023,-7.526229,-9.046985,-5.438299,-8.293813,5.623252,-0.645067,-9.355608],[-3.958238,9.886263,-8.100513,8.012924,-8.025006,0.483090,5.234567,8.633139,-6.031949],[9.392001,2.437148,-4.028461,9.435124,0.679458,-6.218597,5.304474,-4.440420,8.807152],[-3.856404,-1.711217,2.328948,1.250151,4.124377,9.714772,5.324651,-0.708553,-2.534741],[-3.509642,-3.819650,5.181672,-8.726425,-7.952441,2.069201,2.665290,-6.898570,-9.078431]],[[6.611410,-2.053163,0.227984,-3.530495,-6.048114,4.465952,9.354362,-0.682968,-3.722417],[-5.035572,-1.793405,3.022699,3.239622,-7.235979,1.524233,3.897082,-6.893319,8.838967],[5.528443,-3.667794,-5.868139,-0.720776,-4.498767,-0.487089,-5.597024,8.338541,6.692746],[-1.512780,1.898398,-4.394312,6.627650,9.930090,8.039470,1.113255,-5.564758,0.841015],[-5.832302,-7.837230,-1.257957,2.872684,8.767664,-9.474444,6.684973,6.147360,9.805619],[5.449089,2.994204,-3.154336,1.586701,1.909091,-3.990985,3.767239,-1.042736,3.902831],[-5.790628,1.930898,7.833124,-0.687142,-5.189872,0.817545,1.778121,0.391378,8.536429],[2.644175,5.839113,-2.194569,3.587411,-1.862838,6.867841,0.104458,-2.104677,9.896976],[-7.530646,6.890881,-4.343304,-2.634826,4.117795,-1.155047,1.392099,-3.512922,2.620444],[-8.574566,-0.157894,-8.117571,-9.463891,3.234046,0.276339,-9.133344,-6.961973,-1.353155],[-1.744838,-7.050174,-6.464132,-7.254828,-9.805561,0.715614,0.414459,3.795822,-5.934872],[0.825628,7.651322,-5.720444,-1.455690,-2.628995,-2.127447,9.823675,7.760742,-8.939399],[-8.853419,9.148355,2.895120,-4.133825,8.711360,-4.771118,-6.629678,-8.823185,-7.166690],[-3.000109,-7.387615,7.486588,7.975528,8.434853,-1.705838,2.408174,0.118586,-5.972564],[2.492651,4.216860,-1.678691,-5.072644,-7.220292,-9.605956,6.262678,3.708658,1.308718]],[[-1.522841,1.037199,6.103732,-4.594555,-0.995494,5.833140,-8.429358,-6.058833,5.366239],[-4.046123,1.202271,6.120383,1.547222,-2.172672,-5.245430,-0.691832,-1.968388,-0.358386],[2.114115,-3.270057,-3.318279,-6.098672,-4.496126,3.663508,5.538394,-6.287804,-5.399183],[-2.885433,-8.967844,-3.271941,-4.601714,-8.976537,-7.811024,-9.507532,1.376962,8.780527],[6.909687,-1.198612,-2.717285,9.165213,5.532424,-1.502792,6.218946,-9.860091,4.621425],[-6.943555,1.255859,6.687325,-9.823920,0.490618,-2.620253,0.278969,7.692889,-1.209954],[6.085804,9.712260,3.676012,-4.030732,9.964444,-3.164746,1.033513,-3.733702,7.063450],[-0.111799,-2.510619,1.678962,4.681200,-2.975646,9.727862,-1.880984,-9.258008,2.030671],[-6.126674,1.397945,-9.356040,-8.807655,-0.589468,-1.432038,-8.866537,8.518958,4.129478],[-2.544148,-9.390250,0.050488,6.883297,-0.440123,0.921981,3.710530,-8.404959,9.782730],[-4.041665,-9.192174,5.097441,3.053297,-3.298650,-8.039905,3.061453,-3.393526,3.528920],[8.522269,6.109495,-5.841810,-4.132030,-3.273598,-6.212471,0.877244,-2.891157,-6.731789],[0.109636,9.907585,-2.012916,7.843038,-8.505813,9.004758,3.419264,-3.880735,0.060343],[6.832024,-6.484014,-7.190267,-4.162546,-9.314800,3.864014,-4.650737,-9.896017,-9.159992],[8.654655,-3.266766,3.569482,6.047581,8.805587,-8.925120,-7.144080,-1.438548,5.756422]],[[-7.206583,-7.081707,-6.424133,3.211237,-6.123588,0.420464,-7.069856,-0.868663,-5.528350],[3.239606,-1.550747,-3.426011,6.448103,3.771921,8.525435,-2.840276,-6.566943,-2.646709],[-4.500730,4.326638,2.304274,-3.968349,5.506230,5.518649,-6.987031,7.810337,0.207983],[1.793213,-2.673613,-8.562246,-1.425533,9.459443,8.392213,9.022658,2.304062,3.875953],[2.641614,0.205855,-4.689362,0.064253,8.371555,-9.910834,-7.842770,7.091236,-1.368122],[-8.393478,-1.507117,9.139412,-3.882968,2.355261,6.054898,-0.447350,-3.568399,8.037382],[-9.979561,-6.551934,5.021393,-2.931374,-6.159164,-9.104047,4.346588,4.255677,6.172012],[-4.585270,-2.768131,1.976377,-6.833892,-6.527858,8.788045,7.494621,-9.045014,6.618594],[-8.987666,9.712181,2.991124,7.025247,1.474473,-9.042516,4.719116,-9.420992,8.141764],[9.342718,9.073456,-5.003989,1.953548,9.592167,1.759239,0.781826,-7.318097,3.573871],[9.424286,7.135028,0.697751,6.685444,-9.612247,-7.308735,1.587250,7.132278,-2.540271],[-4.525761,9.434073,5.204919,-2.030910,9.820192,-9.285499,7.977673,7.596456,-2.337981],[-8.241201,-7.153787,3.494296,-5.701105,-7.638214,9.418102,-6.344138,7.647100,7.128382],[-1.168094,4.281410,8.008742,-3.377266,8.905961,2.369659,1.598654,4.687089,-6.991663],[-4.088529,-6.782176,-1.129357,1.160933,8.598865,-5.788415,-4.633741,-4.342484,-3.974883]],[[2.054752,-5.672779,7.972377,-4.988445,-7.957069,-1.985928,-2.919152,6.370616,2.224602],[-2.111074,-8.679839,3.732454,9.712569,-9.817686,-6.785617,0.547040,8.777738,-0.244321],[2.029555,3.773912,7.781508,-3.859066,5.045382,-7.234234,0.054732,6.996114,-8.951274],[-2.374087,-1.903922,9.584337,-5.654394,-8.112544,0.963812,-6.800290,3.313025,-5.381325],[3.729479,-4.302759,-8.107452,7.795778,-8.812055,-8.800244,-9.916418,-6.476080,5.160188],[2.410422,-5.893405,4.851003,-2.061240,-5.420672,-8.333695,-7.988867,3.038295,-5.790732],[0.507038,6.126168,-2.504795,-9.549387,-1.827242,-3.270739,3.127548,9.545865,5.222509],[2.532113,-5.878101,-2.563850,-8.082096,-5.385786,3.162166,5.303581,8.719037,-8.879285],[-4.330951,-7.560505,5.614011,-1.458443,-0.043698,-9.913025,2.183291,3.613948,0.445213],[-2.853719,1.992444,5.863950,5.792031,8.544215,5.753628,-3.748488,5.167068,9.282435],[3.602247,2.215482,4.212567,-0.227081,5.688721,6.323743,0.287256,-0.441450,-1.435094],[1.425501,-6.904256,-3.853187,4.747815,-2.896317,6.529580,5.657089,1.792168,-8.996725],[2.207247,8.162985,4.767497,6.042429,-6.148725,5.229855,-4.858304,-2.302224,1.429849],[-7.269301,-8.448707,2.724990,-4.800117,-7.909698,6.702850,1.868482,1.485735,0.230977],[7.428642,4.417670,-3.837202,-8.070500,-2.282465,-4.061895,-4.802542,-8.003651,4.430759]],[[-4.442297,-2.439668,9.318207,-5.266481,-0.782180,-2.478543,-5.302752,1.757210,8.610852],[-6.533921,-3.051530,6.039328,-0.995667,8.965914,-8.218953,9.960100,0.024010,8.181808],[0.895099,6.088938,-9.577717,-2.773646,2.362649,-2.550772,5.778209,-9.602138,6.160733],[-8.656459,9.490951,-5.070320,-7.677962,6.312629,-7.280503,7.158392,-7.574752,2.246780],[-1.718340,0.435311,7.799590,-5.587605,-9.486776,-6.838186,-0.901365,7.255099,9.046430],[4.423898,7.899498,7.840112,-2.252263,-1.390797,1.025451,6.456819,5.171225,1.326260],[-1.078034,9.869187,-6.970930,6.906870,7.259520,2.312553,-9.694987,-1.895145,0.936189],[7.629108,-2.929896,-1.590806,-0.762520,7.237621,-0.699060,-6.170978,7.799051,7.511096],[-6.122301,-1.870518,1.460410,-5.331544,3.007554,-3.369575,-9.099661,-6.632572,7.029395],[-1.444847,-4.478030,1.178823,-3.932634,6.136942,8.307706,9.054059,1.493240,3.946426],[4.593119,1.601315,8.848855,3.807873,1.268004,-6.835947,-6.089290,-2.105498,3.325074],[9.670365,-3.654864,7.769368,7.289602,7.449762,-7.632432,-0.376050,-8.211144,-8.475616],[9.930949,3.427499,9.063332,6.565522,-9.651567,-2.059076,6.866800,9.240519,0.622118],[8.850268,7.825411,2.663115,-6.062760,-2.848446,1.272134,-4.074011,-6.355666,-8.792687],[3.515426,-5.986273,2.173361,0.202147,-8.775080,-2.072893,4.535137,2.441151,-6.084200]],[[9.277295,-0.275014,7.415186,-3.648922,-6.368115,7.347345,9.618276,-6.697606,-1.347714],[-5.316220,-5.955577,-9.398318,-2.225263,-7.727742,0.896808,4.647161,2.675049,-0.428138],[4.297390,-4.335278,5.190420,-6.302407,6.412508,-7.121372,7.272536,3.807729,-4.608397],[-8.766245,-2.356418,-8.952932,-6.143084,-2.123954,9.811212,-6.976910,3.196753,-1.778470],[3.129676,5.300482,6.946881,-1.719828,2.324490,-8.582323,-5.412372,-9.964275,3.838453],[-7.987392,-7.677514,-4.182873,7.836609,4.058057,5.182677,8.484461,-8.123574,6.944633],[2.819394,-9.158172,-3.055134,-9.079958,-0.136239,8.294965,1.194129,8.839474,-8.884005],[8.346853,-1.782085,-2.928682,-5.986363,-2.346147,9.927043,-4.328172,-8.504565,8.971695],[8.667011,3.830010,-3.384747,9.354506,-7.939192,-6.796064,-3.100457,-5.097209,-7.557561],[5.373148,-5.957571,0.109555,4.464047,-8.393829,2.885207,-0.390668,2.924633,-0.414242],[-3.757181,9.356120,-6.808828,0.710092,9.988301,2.815006,5.351305,-6.455443,4.414222],[8.225653,2.207409,-6.719257,3.829213,6.626693,-7.573416,-2.560940,-3.895379,1.233575],[6.740998,5.396547,-0.973458,-6.452214,6.891844,5.654605,2.886187,-8.337873,5.210411],[1.609132,0.282519,8.706633,-4.490568,4.705049,-3.973636,1.495542,6.504032,-5.649205],[9.899826,8.126213,-0.027787,9.769329,8.246749,-6.835915,-5.173543,4.611881,3.602607]],[[8.011104,6.620249,-0.909010,3.165846,9.048498,-5.527048,-4.330550,4.328341,5.258551],[4.103173,6.182375,-7.040193,3.418164,5.835723,-7.149461,9.951516,-6.405087,-9.007623],[-6.390099,-6.915196,8.989529,-5.543562,-1.105546,6.882937,6.474298,9.103223,-1.245331],[-2.794759,-0.089142,-6.942448,-2.247775,8.916317,-1.821103,2.519122,8.565858,9.581353],[8.445415,5.083186,1.271739,1.741801,3.587641,1.198925,-5.171382,8.500963,1.865974],[2.227020,2.069724,-0.964246,8.958788,3.822355,3.180742,5.324772,-6.478152,-3.952030],[2.001528,-3.034050,-1.628563,-8.167376,3.437933,-3.539068,-3.341072,0.141840,-0.486034],[9.008851,8.900359,-5.317100,6.696510,5.484854,-4.785709,5.733928,7.973467,-8.313943],[2.431807,-5.720890,-2.664955,8.018293,8.307374,1.753153,-9.209731,3.301930,1.348594],[-1.698046,7.773849,-0.620632,-0.850308,1.399167,1.685987,7.128086,7.951078,6.148690],[-1.436676,-6.566317,3.274769,8.355387,-9.881065,-6.743066,4.664196,2.121497,-9.887994],[-1.210258,6.532578,1.490272,-4.253799,-1.417190,-7.929938,8.057353,-9.973490,-6.391677],[6.056069,-4.375412,-4.920353,1.395109,9.322164,-8.160502,-9.784048,-0.464218,0.118152],[-0.918367,1.027869,5.685355,7.224694,-5.582631,-8.617083,0.301766,6.425445,4.513186],[-9.104067,3.418072,5.784682,-7.460193,-7.193865,-0.237373,-1.519748,4.795872,2.190206]],[[0.488959,-1.210506,-0.318662,5.004049,-5.237449,7.773942,-6.874534,9.386203,-3.407864],[-4.120128,-2.311825,9.704554,-3.826128,-6.592091,1.586778,-0.536795,-9.825042,7.905344],[4.817232,-2.086809,8.016484,7.988565,-2.905756,4.844777,-9.708639,3.811817,-4.409036],[0.351062,-2.668017,7.337383,4.716981,-6.009426,-7.831876,-1.983060,-6.326420,8.636873],[8.392629,-5.743498,2.653695,-4.124945,5.302811,5.128761,-6.661839,-5.990867,-2.627563],[7.815522,0.775203,9.808667,5.914654,8.479309,-5.977413,6.490019,0.944129,1.275593],[3.998770,-9.906369,8.276434,-3.635143,-6.931210,-5.653653,-3.743184,-1.326085,-1.810964],[6.766081,-1.669197,9.888312,-2.001233,-1.013998,-5.187131,-8.591056,6.825395,-6.666327],[-4.799407,-7.907703,0.262147,5.904803,-2.532691,6.380536,5.217593,-0.875566,7.065285],[7.798500,-1.211908,-3.085982,1.598099,-8.921321,0.984403,-2.237184,-9.765526,0.705250],[3.761820,1.855420,-0.394466,-4.960658,-2.782891,8.627587,6.235894,3.247024,-5.660837],[-5.655071,-1.389402,-9.139437,-1.505882,-0.460165,-5.174039,-8.938120,-9.203968,4.760487],[9.988759,5.475122,4.411001,2.379489,8.446100,-1.419668,-2.339823,7.725704,-5.309532],[0.423764,-6.504704,5.934672,3.038005,1.999813,3.816709,-8.481313,-8.781779,-5.766037],[3.571685,-2.373740,-2.785823,-7.317111,-9.250009,-6.468210,-9.157943,8.492179,3.945172]],[[5.993102,-4.101182,-2.413050,8.004876,-6.704743,-0.936203,1.435451,6.181708,-9.369759],[0.062405,-1.170787,7.063426,-6.306474,-6.021986,-2.950860,-1.709324,-5.642957,-8.066581],[-2.813078,-2.668299,-4.063742,-2.257529,-5.986551,0.737680,8.487998,6.311600,-7.039700],[-1.826217,-2.035897,-8.925813,-2.874776,-6.080363,-6.023596,-3.927655,2.151739,8.508285],[5.329214,8.140102,5.852749,5.814455,1.045385,9.243959,5.950799,-2.773430,-1.274895],[-9.757137,1.409120,-8.824335,-8.186117,9.238631,6.715338,0.331702,-8.563053,-7.874059],[8.628682,-7.363090,-1.757104,1.714364,-6.295166,-2.794921,-2.390965,1.263225,4.898757],[1.973724,-8.307024,4.214502,-3.585715,7.239560,-8.741302,-0.932697,6.243372,-8.092897],[-6.527307,4.062645,-3.823268,-5.567486,-3.105802,-5.532593,5.482122,2.510505,-6.216460],[8.239535,3.055383,8.376868,-3.397111,-2.588710,4.016120,8.712339,-2.640703,-2.455930],[-9.308324,5.358309,-2.692892,0.053612,-6.627854,-0.106646,5.880401,9.380411,-7.253161],[-7.908409,-6.201160,-4.134435,-0.037488,-3.096832,-0.121851,0.095212,6.641491,5.947400],[-8.040779,6.430596,-3.199162,-6.344291,7.180450,-7.666150,-9.203143,-9.972276,3.570763],[-1.051227,-8.428849,-3.438498,1.738250,-2.674406,9.175077,4.428137,-1.468997,-6.219125],[-0.307096,-8.720949,-0.025342,0.712897,-5.082194,7.520162,-4.780944,8.073861,-9.626561]]], dtype = "float32")#candidate|3341|(13, 15, 9)|const|float32
bop_3342 = relay.bitwise_or(call_3330.astype('uint16'), const_3341.astype('uint16')) # shape=(13, 15, 9)
bop_3345 = relay.bitwise_or(call_3331.astype('uint16'), const_3341.astype('uint16')) # shape=(13, 15, 9)
output = bop_3342
output2 = bop_3345
func_3354 = relay.Function([], output)
mod['func_3354'] = func_3354
mod = relay.transform.InferType()(mod)
mutated_mod['func_3354'] = func_3354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3354_call = mutated_mod.get_global_var('func_3354')
call_3355 = func_3354_call()
output = call_3355
func_3356 = relay.Function([], output)
mutated_mod['func_3356'] = func_3356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2903_call = mod.get_global_var('func_2903')
func_2905_call = mutated_mod.get_global_var('func_2905')
call_3409 = func_2903_call()
call_3410 = func_2903_call()
output = call_3409
output2 = call_3410
func_3429 = relay.Function([], output)
mod['func_3429'] = func_3429
mod = relay.transform.InferType()(mod)
output = func_3429()
func_3430 = relay.Function([], output)
mutated_mod['func_3430'] = func_3430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_414_call = mod.get_global_var('func_414')
func_415_call = mutated_mod.get_global_var('func_415')
call_3446 = relay.TupleGetItem(func_414_call(), 0)
call_3447 = relay.TupleGetItem(func_415_call(), 0)
output = relay.Tuple([call_3446,])
output2 = relay.Tuple([call_3447,])
func_3453 = relay.Function([], output)
mod['func_3453'] = func_3453
mod = relay.transform.InferType()(mod)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3453_call = mutated_mod.get_global_var('func_3453')
call_3454 = func_3453_call()
output = call_3454
func_3455 = relay.Function([], output)
mutated_mod['func_3455'] = func_3455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_3481 = relay.TupleGetItem(func_2356_call(), 0)
call_3482 = relay.TupleGetItem(func_2358_call(), 0)
func_2118_call = mod.get_global_var('func_2118')
func_2119_call = mutated_mod.get_global_var('func_2119')
call_3483 = func_2118_call()
call_3484 = func_2118_call()
output = relay.Tuple([call_3481,call_3483,])
output2 = relay.Tuple([call_3482,call_3484,])
func_3499 = relay.Function([], output)
mod['func_3499'] = func_3499
mod = relay.transform.InferType()(mod)
output = func_3499()
func_3500 = relay.Function([], output)
mutated_mod['func_3500'] = func_3500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3354_call = mod.get_global_var('func_3354')
func_3356_call = mutated_mod.get_global_var('func_3356')
call_3577 = func_3354_call()
call_3578 = func_3354_call()
uop_3579 = relay.atanh(call_3577.astype('float64')) # shape=(13, 15, 9)
uop_3581 = relay.atanh(call_3578.astype('float64')) # shape=(13, 15, 9)
output = relay.Tuple([uop_3579,])
output2 = relay.Tuple([uop_3581,])
func_3586 = relay.Function([], output)
mod['func_3586'] = func_3586
mod = relay.transform.InferType()(mod)
mutated_mod['func_3586'] = func_3586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3586_call = mutated_mod.get_global_var('func_3586')
call_3587 = func_3586_call()
output = call_3587
func_3588 = relay.Function([], output)
mutated_mod['func_3588'] = func_3588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_910_call = mod.get_global_var('func_910')
func_911_call = mutated_mod.get_global_var('func_911')
call_3631 = relay.TupleGetItem(func_910_call(), 1)
call_3632 = relay.TupleGetItem(func_911_call(), 1)
var_3636 = relay.var("var_3636", dtype = "float32", shape = (15, 15, 9))#candidate|3636|(15, 15, 9)|var|float32
bop_3637 = relay.bitwise_or(call_3631.astype('int64'), var_3636.astype('int64')) # shape=(15, 15, 9)
bop_3640 = relay.bitwise_or(call_3632.astype('int64'), var_3636.astype('int64')) # shape=(15, 15, 9)
bop_3649 = relay.add(var_3636.astype('uint32'), call_3631.astype('uint32')) # shape=(15, 15, 9)
bop_3652 = relay.add(var_3636.astype('uint32'), call_3632.astype('uint32')) # shape=(15, 15, 9)
output = relay.Tuple([bop_3637,bop_3649,])
output2 = relay.Tuple([bop_3640,bop_3652,])
func_3676 = relay.Function([var_3636,], output)
mod['func_3676'] = func_3676
mod = relay.transform.InferType()(mod)
var_3677 = relay.var("var_3677", dtype = "float32", shape = (15, 15, 9))#candidate|3677|(15, 15, 9)|var|float32
output = func_3676(var_3677)
func_3678 = relay.Function([var_3677], output)
mutated_mod['func_3678'] = func_3678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3262_call = mod.get_global_var('func_3262')
func_3263_call = mutated_mod.get_global_var('func_3263')
call_3754 = relay.TupleGetItem(func_3262_call(), 1)
call_3755 = relay.TupleGetItem(func_3263_call(), 1)
func_3071_call = mod.get_global_var('func_3071')
func_3072_call = mutated_mod.get_global_var('func_3072')
call_3758 = relay.TupleGetItem(func_3071_call(), 0)
call_3759 = relay.TupleGetItem(func_3072_call(), 0)
output = relay.Tuple([call_3754,call_3758,])
output2 = relay.Tuple([call_3755,call_3759,])
func_3770 = relay.Function([], output)
mod['func_3770'] = func_3770
mod = relay.transform.InferType()(mod)
output = func_3770()
func_3771 = relay.Function([], output)
mutated_mod['func_3771'] = func_3771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_3806 = func_1958_call()
call_3807 = func_1958_call()
var_3813 = relay.var("var_3813", dtype = "float32", shape = (8, 15, 9))#candidate|3813|(8, 15, 9)|var|float32
bop_3814 = relay.right_shift(call_3806.astype('uint16'), var_3813.astype('uint16')) # shape=(8, 15, 9)
bop_3817 = relay.right_shift(call_3807.astype('uint16'), var_3813.astype('uint16')) # shape=(8, 15, 9)
uop_3834 = relay.exp(bop_3814.astype('float64')) # shape=(8, 15, 9)
uop_3836 = relay.exp(bop_3817.astype('float64')) # shape=(8, 15, 9)
bop_3841 = relay.multiply(call_3806.astype('int64'), var_3813.astype('int64')) # shape=(8, 15, 9)
bop_3844 = relay.multiply(call_3807.astype('int64'), var_3813.astype('int64')) # shape=(8, 15, 9)
uop_3849 = relay.atanh(uop_3834.astype('float64')) # shape=(8, 15, 9)
uop_3851 = relay.atanh(uop_3836.astype('float64')) # shape=(8, 15, 9)
output = relay.Tuple([bop_3841,uop_3849,])
output2 = relay.Tuple([bop_3844,uop_3851,])
func_3852 = relay.Function([var_3813,], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
mutated_mod['func_3852'] = func_3852
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3853 = relay.var("var_3853", dtype = "float32", shape = (8, 15, 9))#candidate|3853|(8, 15, 9)|var|float32
func_3852_call = mutated_mod.get_global_var('func_3852')
call_3854 = func_3852_call(var_3853)
output = call_3854
func_3855 = relay.Function([var_3853], output)
mutated_mod['func_3855'] = func_3855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
call_3860 = relay.TupleGetItem(func_1197_call(), 0)
call_3861 = relay.TupleGetItem(func_1199_call(), 0)
func_530_call = mod.get_global_var('func_530')
func_533_call = mutated_mod.get_global_var('func_533')
var_3899 = relay.var("var_3899", dtype = "float32", shape = (81,))#candidate|3899|(81,)|var|float32
call_3898 = relay.TupleGetItem(func_530_call(relay.reshape(var_3899.astype('float32'), [9, 9])), 0)
call_3900 = relay.TupleGetItem(func_533_call(relay.reshape(var_3899.astype('float32'), [9, 9])), 0)
func_978_call = mod.get_global_var('func_978')
func_980_call = mutated_mod.get_global_var('func_980')
const_3905 = relay.const([-1.677343,-9.935400,-4.271119,-4.515740,-6.211124,8.550081,1.972529,9.297281,7.505094,-3.076652,3.760982,9.463819,5.423375,-7.472783,3.631899,-9.912878,-2.142129,-9.294120,4.090577,-2.198352,-4.701911,-7.814010,6.739241,-5.248307,-1.219866,-1.761848,-8.894978,-7.152350,0.310404,-6.685319,-9.309295,-4.121992,-0.199362,0.592763,0.558119,6.682417,3.389744,-6.316658,1.731801,1.122858,1.107621,-3.230280,6.234377,9.331685,4.307914,4.715420,-3.347049,1.218584,-4.999898,-3.496763,-2.909323,9.584393,2.106623,-5.429183,-1.520013,6.293368,8.131209,-2.932916,-7.192059,8.667854,5.585027,4.260297,5.852678,-5.742633,5.263310,9.095305,-2.465707,-2.474850,-3.836103,1.729336,-1.669256,-1.610521,-5.827829,7.209666,-4.971730,-8.463688,6.331366,-1.770813,-3.829641,7.537526,3.980258,2.232273,1.711521,-1.313352,-2.558443,5.707491,-8.861459,5.903396,-5.824713,3.575003,0.192943,-8.804106,-6.566219,6.856622,-3.235220,-5.448470,-9.577155,2.498130,2.706859,0.416947,0.510987,3.295020,0.159199,-1.457529,3.496227,-9.900487,-1.297695,4.138928,5.560435,5.817466,9.244937,-2.857954,-8.518570,-4.506270,6.511569,3.448659,-6.787101,-2.801752,9.382291,9.934571,-7.000312,-3.891709,-9.600964,1.684860,-4.210032,6.811054,0.048062,8.995057,-2.546138,3.123121,-3.377149,-5.557411,0.454626,-5.626020,-6.922577,1.657526,3.758522,3.943580,-6.895808,-2.378808,3.082482,-3.384499,2.413183,-6.586328,7.932817,7.257481,1.154054,-4.414618,-5.597880,3.764257,-1.887292,4.363108,-4.152715,-7.790824,-3.698314,-5.162473,-4.904584,-3.723287,-6.334782,6.824045,-3.915416,3.756018,9.230332,9.961117,-4.050780,-8.946464,6.058125,8.887326,-9.608639,-8.404161,-5.905205,-0.420512,-9.666348,-5.863114,-6.893641,-1.616064,-6.610216,-6.435494,-0.094036,5.604750,-5.146238,1.639553,6.747972,-9.130591,-1.278826,-9.199671,7.573170,-6.159281,1.760500,-7.991053,-8.288935,8.952175,8.822430,-9.599135,0.050997,-3.520516,4.574567,7.659126,-5.239038,-8.957966,8.008842,4.956782,-2.621927,-8.948675,-1.558960,4.587766,4.441328,8.542624,-4.632389,-5.033251,0.419548,9.191739,0.108975,-7.993668,-2.062111,-2.863700,5.998214,-9.222021,1.668664,-5.573893,-8.796837,7.667777,-4.032890,-8.990094,-8.866032,-0.356494,4.055637,9.332790,-9.433031,9.794274,-0.100774,-0.166529,4.562854,1.498785,0.999706,8.577881,1.236177,-3.447025,6.292449,-9.261061,2.364384,-3.698518,3.959181,2.950624,5.323187,-0.360010,5.114840,4.415584,-9.010612,5.623952,-9.417537,1.495864,0.957980,9.495891,-3.192079,0.594004,-5.173778,-5.156993,5.322362,-8.138509,-8.945158,-4.396869,9.245750,2.424383,5.105364,-6.924414,0.755634,0.953205,8.899074,1.793408,6.501856,9.324155,-2.169658,3.614640,-7.224651,-6.346699,-0.556728,-9.587119,7.397463,2.590254], dtype = "float64")#candidate|3905|(280,)|const|float64
call_3904 = func_978_call(relay.reshape(const_3905.astype('float64'), [7, 4, 10]))
call_3906 = func_978_call(relay.reshape(const_3905.astype('float64'), [7, 4, 10]))
uop_3915 = relay.cos(var_3899.astype('float64')) # shape=(81,)
bop_3932 = relay.add(uop_3915.astype('uint16'), relay.reshape(var_3899.astype('uint16'), relay.shape_of(uop_3915))) # shape=(81,)
output = relay.Tuple([call_3860,call_3898,call_3904,const_3905,bop_3932,])
output2 = relay.Tuple([call_3861,call_3900,call_3906,const_3905,bop_3932,])
func_3935 = relay.Function([var_3899,], output)
mod['func_3935'] = func_3935
mod = relay.transform.InferType()(mod)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3936 = relay.var("var_3936", dtype = "float32", shape = (81,))#candidate|3936|(81,)|var|float32
func_3935_call = mutated_mod.get_global_var('func_3935')
call_3937 = func_3935_call(var_3936)
output = call_3937
func_3938 = relay.Function([var_3936], output)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_4021 = relay.TupleGetItem(func_1891_call(), 0)
call_4022 = relay.TupleGetItem(func_1892_call(), 0)
func_1927_call = mod.get_global_var('func_1927')
func_1929_call = mutated_mod.get_global_var('func_1929')
const_4037 = relay.const(-6, dtype = "uint64")#candidate|4037|()|const|uint64
call_4036 = func_1927_call(relay.reshape(const_4037.astype('uint64'), []))
call_4038 = func_1927_call(relay.reshape(const_4037.astype('uint64'), []))
output = relay.Tuple([call_4021,call_4036,const_4037,])
output2 = relay.Tuple([call_4022,call_4038,const_4037,])
func_4044 = relay.Function([], output)
mod['func_4044'] = func_4044
mod = relay.transform.InferType()(mod)
mutated_mod['func_4044'] = func_4044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4044_call = mutated_mod.get_global_var('func_4044')
call_4045 = func_4044_call()
output = call_4045
func_4046 = relay.Function([], output)
mutated_mod['func_4046'] = func_4046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4044_call = mod.get_global_var('func_4044')
func_4046_call = mutated_mod.get_global_var('func_4046')
call_4082 = relay.TupleGetItem(func_4044_call(), 2)
call_4083 = relay.TupleGetItem(func_4046_call(), 2)
func_1706_call = mod.get_global_var('func_1706')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_4088 = func_1706_call()
call_4089 = func_1706_call()
bop_4094 = relay.not_equal(call_4082.astype('bool'), call_4088.astype('bool')) # shape=(1, 15, 9)
bop_4097 = relay.not_equal(call_4083.astype('bool'), call_4089.astype('bool')) # shape=(1, 15, 9)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_4099 = relay.TupleGetItem(func_1070_call(), 1)
call_4100 = relay.TupleGetItem(func_1072_call(), 1)
output = relay.Tuple([bop_4094,call_4099,])
output2 = relay.Tuple([bop_4097,call_4100,])
func_4101 = relay.Function([], output)
mod['func_4101'] = func_4101
mod = relay.transform.InferType()(mod)
mutated_mod['func_4101'] = func_4101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4101_call = mutated_mod.get_global_var('func_4101')
call_4102 = func_4101_call()
output = call_4102
func_4103 = relay.Function([], output)
mutated_mod['func_4103'] = func_4103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2922_call = mod.get_global_var('func_2922')
func_2924_call = mutated_mod.get_global_var('func_2924')
call_4104 = relay.TupleGetItem(func_2922_call(), 0)
call_4105 = relay.TupleGetItem(func_2924_call(), 0)
const_4106 = relay.const([[[3.861273,-8.221107,6.318863,5.080818,5.846860,-3.179228,2.764032,-6.533787,-5.234981],[-0.591573,8.254338,8.033379,6.536215,1.566958,1.379483,1.808184,-7.556732,5.408745],[6.377162,-0.217770,8.443407,-9.194617,6.210754,8.452468,-3.499010,-9.901723,4.072232],[9.217022,-2.234046,4.657790,9.790339,-2.331190,-4.949331,3.054295,2.059504,-8.783150],[-5.018105,2.687414,8.176080,-7.883294,-3.051101,1.513233,-7.425765,2.166497,5.219313],[1.693797,8.906980,8.466168,7.773223,5.716154,-1.759497,-0.450819,6.511699,-5.958821],[-4.999323,-1.356444,3.367381,-2.983229,-2.587422,-7.456975,-0.214808,-8.936465,-0.328714],[-9.323812,-6.779419,-3.338179,2.897211,-1.291969,-9.002840,-3.167054,6.026595,5.516253],[-8.132063,-9.787910,4.548059,5.243878,-2.776407,-7.012431,2.257683,2.800260,-2.902972],[-5.709435,-5.081004,-8.334724,-0.968854,0.327331,3.534980,-8.527392,-2.585426,-1.211865],[-6.132398,-3.624137,3.304070,1.778764,9.999026,9.497679,-9.296464,9.523898,-3.356301],[4.580441,-8.236398,-3.890696,5.109693,-9.243030,5.843267,-3.327872,-2.570148,3.865657],[0.753810,-4.890947,4.670555,-1.302834,6.085337,-1.318193,-5.997098,-6.387957,-4.125051],[-8.483235,-9.801099,6.901978,-0.070783,6.159928,-4.057173,-3.211190,0.762828,-2.019278],[-9.156881,-3.663109,5.944706,4.375034,-0.753979,-9.830225,-6.735292,-8.160887,3.570576]],[[7.802438,9.683146,-8.815467,1.921947,9.168664,1.576569,6.071029,3.314015,-3.517803],[-7.265828,-9.906304,7.647638,6.436575,4.610691,-2.084370,9.218695,-9.404351,-7.455990],[8.186486,-8.181044,-7.175841,-0.997039,4.463489,6.243127,-9.305637,-4.877684,-0.975339],[-9.084787,2.130251,-3.268613,-2.400618,9.379322,-5.416568,-8.979473,5.462819,7.664445],[-1.368955,2.718314,4.379624,1.577913,-6.626386,-0.845264,-0.220199,-5.980924,-3.941595],[2.854487,9.931399,-8.475112,7.735046,4.930632,6.875058,-7.274043,-7.449444,7.745229],[7.990498,-7.788724,-4.340958,-3.392726,3.503401,4.821504,2.941861,-5.466775,4.861338],[6.903282,7.339457,-5.147915,7.407243,5.167178,-1.038890,7.302752,1.466365,-9.477972],[-5.631284,-5.070771,0.579389,2.282888,9.119990,7.138773,-3.028829,6.611846,1.913152],[-3.321104,-2.331967,9.174816,5.684277,-8.381664,-2.237579,-3.583174,-6.996254,-7.894862],[-3.168742,-8.168990,0.548072,9.005612,-1.582789,-1.898397,-5.086967,-0.395753,-1.918345],[0.817249,-3.430607,-7.263710,-6.202801,6.948984,-7.319708,1.991233,-4.337482,-2.221644],[7.511989,3.698475,-5.690076,-8.559935,7.686939,1.048313,-4.013797,1.358391,4.417265],[0.696077,-0.984110,-4.240690,-9.216633,-9.229564,5.911092,-3.676019,-0.024119,6.946940],[4.890032,2.553791,-4.880866,-1.672706,5.279255,-3.374059,-8.138943,4.865613,-7.302262]],[[7.778577,0.094142,2.463703,-1.672602,5.213486,-4.906484,6.105039,-2.261624,-7.571344],[7.151704,9.690993,-2.860164,1.435036,2.230412,0.745890,-2.602597,-6.913705,-3.344420],[8.610936,-6.557128,2.222116,8.411407,-4.420589,1.494188,-0.144701,-0.106148,-7.670326],[6.058780,7.541319,-3.325026,2.820978,6.403117,-9.737306,2.484704,-5.608422,-9.224655],[-6.987547,-7.810596,-0.826095,1.801590,-7.188269,-8.963592,-8.305614,3.115447,0.816091],[7.324625,-9.391547,-2.264559,-6.201261,-3.366863,2.545247,5.170961,-8.569961,4.093996],[5.234540,-5.035365,-0.812142,-2.604904,-5.149266,-9.593306,7.120879,-5.018997,-1.371892],[-7.300868,9.875741,2.495110,-0.788302,-4.407712,-0.790922,5.425513,2.076005,3.664316],[-3.048444,-6.072252,6.673569,-3.986681,-9.153995,1.125306,-2.307873,-0.407318,-0.545485],[-4.192959,-0.629163,-8.985613,-9.891069,-5.438406,1.951792,7.425353,-7.030386,-9.136968],[-0.552804,-1.393431,-4.909071,5.275691,-2.439324,-2.139161,0.155184,0.030933,4.831446],[-5.882802,8.225928,8.766504,5.659481,-8.409557,0.218143,3.248662,-4.977405,-7.067892],[4.799410,9.267261,4.860049,2.301643,-9.106414,-2.986033,-5.940605,-8.373032,-1.511648],[-5.258925,-7.760252,5.149609,9.488094,-0.730314,-8.290296,-3.986944,-9.643622,1.044379],[4.302529,4.434640,2.948799,-7.390044,-7.499491,0.511393,-1.931381,-5.532758,4.259781]],[[-4.555510,1.449017,-5.869885,-2.055292,6.170754,-4.149990,-2.587074,3.429895,5.727901],[-5.203326,-6.374560,-5.550489,5.105337,0.677933,-3.036912,0.487858,-3.366796,4.650362],[-0.800608,5.498186,-0.847824,0.532695,-3.003752,-9.516774,5.437784,7.060360,-2.865091],[-8.007590,-1.961989,0.332040,-3.434723,-9.376049,4.465181,1.327236,5.402215,-0.986850],[-7.492162,-3.105116,-7.179583,-8.031968,1.752561,-7.332379,-5.304161,0.342558,-2.035893],[6.742993,9.652792,9.836381,0.554444,7.134818,-2.524964,-1.707792,7.096144,5.316454],[-5.303176,1.065882,8.559306,6.442687,-7.830396,-0.007728,9.224761,5.370856,5.767412],[-1.282403,9.335556,5.918706,6.243552,-3.671064,7.367729,-9.458252,-7.421813,3.386250],[8.444255,1.048847,-5.770861,4.621161,2.325477,-7.097627,3.476484,7.347727,-1.689429],[-6.223452,-4.475848,-4.293061,-2.169188,7.983001,6.684497,-9.311874,4.051121,-4.777156],[-1.314581,-4.263923,6.834715,-2.336874,4.932888,0.615354,9.585907,2.274444,4.882300],[9.878420,-4.521579,-0.629284,8.576584,8.386264,-7.552526,-3.952807,6.842621,-5.418632],[-4.672813,7.165969,-1.224233,4.435206,8.313756,7.202518,2.005926,-2.093844,-2.205135],[3.343802,-8.333939,-4.362430,-1.738811,5.351369,9.425695,-3.460581,-9.888468,8.585996],[0.906864,-3.391447,0.268412,7.773085,-6.900745,9.179223,-3.918058,4.003088,7.619149]],[[5.538587,-9.223764,9.298360,-8.658515,0.321750,6.074851,5.811222,-0.581055,5.918571],[4.251571,-2.027280,7.440533,-4.479844,-9.575366,-4.320174,-0.305528,0.094980,-7.100368],[-9.469477,1.462540,0.933741,0.850181,9.662791,9.660089,7.606315,0.730005,-5.083674],[8.646974,-1.439479,-3.142408,6.346668,-6.360513,-7.609859,4.000684,2.286279,-0.564891],[-3.272663,5.418680,0.562731,-8.188724,3.110631,-8.711436,-5.344114,2.635452,4.856859],[4.306101,-8.928059,-8.471041,-3.926051,9.395662,-9.245270,7.167760,3.456867,-1.306768],[6.139276,-5.462082,-0.845180,-7.948089,-2.316853,9.197979,-1.354082,8.371244,-7.891258],[9.208668,8.054745,-5.654415,-8.417128,-3.237188,-3.509630,2.398710,-1.370948,-9.482844],[-2.206177,5.606156,-7.374176,1.873461,-2.857362,7.661434,-5.458717,2.805952,-5.639268],[9.003602,4.620256,-5.892723,-4.796612,1.021506,2.252992,4.699588,7.854469,9.674369],[4.792005,-9.241494,0.932771,-0.943730,-0.611497,6.076431,5.627465,1.484058,1.659329],[-5.911046,5.278641,-0.602635,8.783761,6.423840,-9.407450,7.864177,9.804518,8.022395],[1.878153,-3.549353,-2.075330,-9.292824,-3.320487,-3.857555,-8.841829,4.825689,3.465414],[-9.630695,1.100505,3.752391,-6.953303,2.766613,-0.325452,-6.368997,-0.802011,4.213313],[5.917021,-2.700771,3.542241,6.581754,3.704718,-8.289207,-4.792138,8.242119,-8.228501]],[[3.282916,4.121106,-1.308635,-8.704972,-6.977319,1.087844,7.825857,4.438905,-9.171683],[-2.577188,-7.248714,-0.044856,-3.505382,-5.285688,-7.700540,-1.278743,2.946954,-1.063021],[2.930765,8.589688,1.732451,3.117389,3.228287,-1.090603,-4.618641,5.999433,-3.391956],[5.300739,-0.868504,-3.357661,-7.830712,-3.162129,6.327059,3.120081,2.793471,-4.409108],[2.334117,4.792172,-8.682171,-9.581759,6.646234,-1.813154,0.995858,-0.912534,5.616038],[-1.756928,-8.250794,5.048953,4.401363,-1.930371,8.379087,0.493854,5.634355,7.052946],[-5.702865,-7.377069,2.205199,5.542172,-3.645830,-7.181063,-2.863840,0.965253,-3.522582],[-4.293400,5.985693,-5.277124,3.247906,3.041378,3.551062,1.675538,-3.054800,8.090278],[-0.767466,-3.378508,-5.887984,-8.762417,7.724039,6.600959,-9.060721,4.732593,1.378966],[4.652912,9.259677,3.440992,3.223329,-4.596200,-1.652599,-8.801145,-2.287528,5.232095],[7.432098,3.947559,2.797906,-5.468502,2.318774,7.282410,-6.596003,2.819943,3.959152],[-5.303719,9.309041,-9.303489,-5.479528,-4.066536,4.811529,0.279075,3.713362,9.560659],[-2.526019,7.164552,5.700221,-5.611859,0.465500,7.887036,-7.454313,7.193324,-6.306420],[1.786914,-2.444266,8.417205,8.867878,6.863749,3.647956,3.538999,-5.162417,4.451207],[9.158366,7.050262,-8.528632,7.111000,-5.240680,-4.088910,-7.845260,6.204714,-9.082102]],[[-6.616354,-3.112832,-3.999853,-4.284807,0.091608,-7.010728,-1.037339,-8.895353,-3.657723],[-3.377553,6.366564,2.992554,0.618918,0.056157,-7.150253,8.467136,2.504114,-0.470747],[2.941487,0.651420,-0.506689,-1.003277,3.655293,-9.650480,5.571597,7.668584,-7.576517],[-9.933781,-2.217026,-8.280665,9.779071,4.597413,6.915652,5.136447,-8.541056,5.383010],[-7.075954,8.937045,-0.084966,-9.403300,-1.469702,-5.063917,-3.613263,-9.197282,-1.408949],[8.634094,-6.097658,-8.321660,5.972800,-6.434960,-5.974812,-7.825347,2.064328,-4.409511],[9.324093,6.892974,-4.604447,-8.015908,7.535919,4.295888,-4.088386,0.915699,7.375734],[-8.713656,0.172917,-6.761219,6.186876,0.617750,-9.809085,-4.244048,-7.135291,7.645798],[-3.392073,6.830933,-4.225186,5.200795,4.508175,0.400098,9.223187,9.776338,1.686150],[-3.685305,-3.951532,4.229189,-5.273930,7.197906,-2.813540,1.852777,-5.352191,-1.487235],[-0.004510,3.081006,-7.637482,-6.864696,4.308103,0.582391,-4.380867,5.606959,7.120136],[1.944857,-5.132729,-3.337489,-8.788728,5.556397,-2.210764,6.217988,-7.886231,-5.976641],[-0.635062,-6.999747,2.585447,-6.415275,2.360568,-0.858843,-6.761009,-8.401650,-0.077204],[1.295583,6.742779,-0.540520,-2.351125,-6.274511,-1.188083,-6.309756,2.050591,-2.027496],[-4.733222,-3.634581,-0.497279,-1.676788,8.412887,-0.852844,4.483144,-8.110493,-2.127476]],[[-3.104650,-8.882606,5.623465,2.203407,4.739533,-6.444538,4.224023,-2.592247,4.118635],[9.410598,-5.532721,-0.046180,-0.747011,-3.001416,-2.583861,8.443173,-9.771138,1.888537],[7.790732,3.255459,-1.621827,-6.645273,-1.776212,5.694705,-7.669995,1.021083,9.591360],[8.780277,6.993500,-5.647874,-8.824012,-6.044658,-8.319345,9.453560,-8.757007,-6.426705],[-6.438500,4.315316,-6.708939,-7.682207,3.372074,2.222465,-2.184031,-5.185557,-6.134731],[0.250815,1.621142,5.637590,-2.523516,7.327082,9.606498,2.661942,-2.418311,-7.349326],[8.334385,4.921365,-3.575286,-2.734400,7.914799,-8.679280,5.948497,5.010736,1.293528],[-1.979144,8.995884,5.918032,-1.107502,-8.331958,1.725266,8.380441,-4.375433,3.795367],[7.215380,0.705174,-4.055225,-1.001295,5.271329,-3.516158,6.653812,-3.091297,-1.526896],[5.151394,-8.180334,-9.176121,0.121991,5.142115,-9.852108,-7.931079,-2.437802,1.000945],[-8.393606,-6.445614,3.916743,-9.908299,-9.458488,8.874088,-7.151325,0.518527,-5.176080],[-2.310970,2.127854,3.578883,-0.602088,3.050657,9.582162,-2.277854,-0.824328,-8.991658],[0.016063,-1.889112,5.751358,5.209589,3.331227,3.633396,-0.629366,5.714341,3.181437],[4.475780,-4.428235,-7.015139,5.955746,4.059383,7.876312,8.058084,8.631948,-4.553203],[4.612516,-4.711313,-3.502191,9.619506,-0.334669,-5.015698,4.587056,0.534118,-4.556627]]], dtype = "float32")#candidate|4106|(8, 15, 9)|const|float32
bop_4107 = relay.equal(call_4104.astype('bool'), const_4106.astype('bool')) # shape=(8, 15, 9)
bop_4110 = relay.equal(call_4105.astype('bool'), const_4106.astype('bool')) # shape=(8, 15, 9)
output = bop_4107
output2 = bop_4110
func_4129 = relay.Function([], output)
mod['func_4129'] = func_4129
mod = relay.transform.InferType()(mod)
mutated_mod['func_4129'] = func_4129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4129_call = mutated_mod.get_global_var('func_4129')
call_4130 = func_4129_call()
output = call_4130
func_4131 = relay.Function([], output)
mutated_mod['func_4131'] = func_4131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4101_call = mod.get_global_var('func_4101')
func_4103_call = mutated_mod.get_global_var('func_4103')
call_4193 = relay.TupleGetItem(func_4101_call(), 1)
call_4194 = relay.TupleGetItem(func_4103_call(), 1)
var_4207 = relay.var("var_4207", dtype = "float32", shape = (3, 15, 9))#candidate|4207|(3, 15, 9)|var|float32
bop_4208 = relay.less(call_4193.astype('bool'), var_4207.astype('bool')) # shape=(3, 15, 9)
bop_4211 = relay.less(call_4194.astype('bool'), var_4207.astype('bool')) # shape=(3, 15, 9)
output = relay.Tuple([bop_4208,])
output2 = relay.Tuple([bop_4211,])
func_4216 = relay.Function([var_4207,], output)
mod['func_4216'] = func_4216
mod = relay.transform.InferType()(mod)
var_4217 = relay.var("var_4217", dtype = "float32", shape = (3, 15, 9))#candidate|4217|(3, 15, 9)|var|float32
output = func_4216(var_4217)
func_4218 = relay.Function([var_4217], output)
mutated_mod['func_4218'] = func_4218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_4250 = relay.TupleGetItem(func_1891_call(), 0)
call_4251 = relay.TupleGetItem(func_1892_call(), 0)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_4253 = relay.TupleGetItem(func_2511_call(), 0)
call_4254 = relay.TupleGetItem(func_2513_call(), 0)
uop_4255 = relay.sigmoid(call_4250.astype('float64')) # shape=(1, 15, 9)
uop_4257 = relay.sigmoid(call_4251.astype('float64')) # shape=(1, 15, 9)
func_1355_call = mod.get_global_var('func_1355')
func_1357_call = mutated_mod.get_global_var('func_1357')
call_4276 = relay.TupleGetItem(func_1355_call(), 1)
call_4277 = relay.TupleGetItem(func_1357_call(), 1)
output = relay.Tuple([call_4253,uop_4255,call_4276,])
output2 = relay.Tuple([call_4254,uop_4257,call_4277,])
func_4284 = relay.Function([], output)
mod['func_4284'] = func_4284
mod = relay.transform.InferType()(mod)
output = func_4284()
func_4285 = relay.Function([], output)
mutated_mod['func_4285'] = func_4285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_4296 = relay.TupleGetItem(func_139_call(), 0)
call_4297 = relay.TupleGetItem(func_140_call(), 0)
uop_4303 = relay.asin(call_4296.astype('float32')) # shape=(1, 15, 9)
uop_4305 = relay.asin(call_4297.astype('float32')) # shape=(1, 15, 9)
func_3429_call = mod.get_global_var('func_3429')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_4306 = func_3429_call()
call_4307 = func_3429_call()
output = relay.Tuple([uop_4303,call_4306,])
output2 = relay.Tuple([uop_4305,call_4307,])
func_4308 = relay.Function([], output)
mod['func_4308'] = func_4308
mod = relay.transform.InferType()(mod)
mutated_mod['func_4308'] = func_4308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4308_call = mutated_mod.get_global_var('func_4308')
call_4309 = func_4308_call()
output = call_4309
func_4310 = relay.Function([], output)
mutated_mod['func_4310'] = func_4310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3499_call = mod.get_global_var('func_3499')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_4347 = relay.TupleGetItem(func_3499_call(), 1)
call_4348 = relay.TupleGetItem(func_3500_call(), 1)
func_1127_call = mod.get_global_var('func_1127')
func_1131_call = mutated_mod.get_global_var('func_1131')
var_4367 = relay.var("var_4367", dtype = "uint8", shape = (1, 486))#candidate|4367|(1, 486)|var|uint8
call_4366 = relay.TupleGetItem(func_1127_call(relay.reshape(var_4367.astype('uint8'), [9, 6, 9]), relay.reshape(var_4367.astype('uint8'), [9, 6, 9]), ), 0)
call_4368 = relay.TupleGetItem(func_1131_call(relay.reshape(var_4367.astype('uint8'), [9, 6, 9]), relay.reshape(var_4367.astype('uint8'), [9, 6, 9]), ), 0)
bop_4374 = relay.bitwise_and(call_4366.astype('uint64'), relay.reshape(var_4367.astype('uint64'), relay.shape_of(call_4366))) # shape=(9, 6, 9)
bop_4377 = relay.bitwise_and(call_4368.astype('uint64'), relay.reshape(var_4367.astype('uint64'), relay.shape_of(call_4368))) # shape=(9, 6, 9)
output = relay.Tuple([call_4347,bop_4374,])
output2 = relay.Tuple([call_4348,bop_4377,])
func_4381 = relay.Function([var_4367,], output)
mod['func_4381'] = func_4381
mod = relay.transform.InferType()(mod)
mutated_mod['func_4381'] = func_4381
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4382 = relay.var("var_4382", dtype = "uint8", shape = (1, 486))#candidate|4382|(1, 486)|var|uint8
func_4381_call = mutated_mod.get_global_var('func_4381')
call_4383 = func_4381_call(var_4382)
output = call_4383
func_4384 = relay.Function([var_4382], output)
mutated_mod['func_4384'] = func_4384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_4396 = relay.TupleGetItem(func_1891_call(), 0)
call_4397 = relay.TupleGetItem(func_1892_call(), 0)
output = call_4396
output2 = call_4397
func_4407 = relay.Function([], output)
mod['func_4407'] = func_4407
mod = relay.transform.InferType()(mod)
mutated_mod['func_4407'] = func_4407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mutated_mod.get_global_var('func_4407')
call_4408 = func_4407_call()
output = call_4408
func_4409 = relay.Function([], output)
mutated_mod['func_4409'] = func_4409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4101_call = mod.get_global_var('func_4101')
func_4103_call = mutated_mod.get_global_var('func_4103')
call_4427 = relay.TupleGetItem(func_4101_call(), 1)
call_4428 = relay.TupleGetItem(func_4103_call(), 1)
func_2050_call = mod.get_global_var('func_2050')
func_2053_call = mutated_mod.get_global_var('func_2053')
const_4432 = relay.const([-4.536468,3.329224,-8.134057,3.937520,4.839432,-8.332141,7.526635,-8.748832,7.075268,-0.351686,-9.313544,-7.702756,9.226097,-6.168499,7.771074,2.110906,7.916089,1.800390,-9.331489,-2.862242,-0.800467,3.854603,8.123309,2.184797,4.469120,-0.141419,3.572553,-1.192792,9.325404,3.978096,-0.266644,9.856445,-6.242563,8.898287,2.492257,-8.333788,2.386418,-7.742124,-8.852575,2.063093,4.995530,6.279883,-6.921257,6.666121,-3.855165,8.768821,7.375030,-1.854146,8.084002,-1.563407,-0.221944,-7.535034,3.131469,-8.189296,-4.320117,3.211489,-5.981779,-0.665725,-7.584337,-8.818860,2.350001,3.397461,-5.917878,-6.736685,2.727382,5.751365,7.409849,2.590291,-4.811091,-6.565948,-3.183320,-1.826206,7.895854,2.796603,-4.807712,-2.430521,2.270489,-0.729426,-4.351748,1.207233,8.468613,8.299460,-7.476375,3.921823,-3.534133,4.443581,2.739276,9.999168,9.517239,-9.817910,0.325718,9.004032,-7.488967,-1.402806,-3.396109,1.184817,-7.815890,-4.515827,6.521577,6.419554,-4.412451,-3.443266,-6.682674,-7.667163,6.115922,5.141516,4.111023,4.969051,-1.064151,-5.121291,-7.395479,4.703123,-1.560438,6.457729,9.731276,-2.566938,-3.357029,-6.494061,-1.788728,-9.760647,3.833113,-4.281041,-7.545403,8.513490,-1.018527,9.116475,3.564462,6.610069,-9.939770,5.609953,-9.300166,2.085389,1.673748,1.793859,-7.802423,1.756248,-6.822928,3.866471,4.609503,2.932282,-7.965096,-1.329187,0.633250,-7.391987,0.299527,-4.887563,2.585304,-9.621384,8.180766,-5.079131,9.256287,1.596390,-2.465511,-2.930306,1.092535,7.291347,-6.217369,6.352040,8.482863,9.978554,-8.951269,-4.585937,-8.941449,-8.178027,6.137992,9.686854,-7.858002,-6.010533,3.353700,-7.545426,-8.338191,5.587664,-1.919240,7.842689,-0.048338,-7.051464,-1.789626,-4.023753,4.714000,-4.483875,1.165344,7.803543,-8.413588,-3.423503,-5.533087,6.286273,-5.691723,5.260371,0.585259,2.019067,9.237601,-0.027332,-3.454189,-6.794621,6.111114,-5.587602,9.949100,-4.164839,7.335662,9.080118,-6.310554,9.678657,9.886150,8.899938,9.164687,-4.074037,-8.106872,-1.476138,4.746513,-2.327210,2.266271,-6.414906,-8.845656,-7.541584,3.006069,8.864146,-9.315194,2.303885,5.184571,6.022236,3.512309,9.267974,-0.241110,-3.146138,7.343316,1.676940,-4.589454,5.755139,-5.573822,-4.093808,7.231496,0.901026,-0.106959,-6.655159,5.693888,-8.045550,8.272875,-0.530089,0.156629,-6.238753,9.734509,2.195599,6.758665,-9.830507,1.623931,9.658477,-5.524774,-2.947461,7.128670,-5.524602,-7.733124,0.859599,6.449334,-4.194039,6.634473,7.287487,-8.442939,-9.443741,5.111458,8.519469,7.042671,1.514105,-2.282179,5.709508,-5.910748,-2.625848,-7.885496,7.034678,-0.970493,9.545626,-2.557583,-5.782784,1.602293,-1.346852,-5.474854,5.029420,-2.100541,7.345529,4.736463,7.670009,5.990962,-6.826608,2.183838,7.632059,8.783811,4.399176,6.723124,-1.025320,-1.029795,8.679198,7.996643,6.978198,1.516873,-4.971529,8.050484,3.166010,8.744307,-5.477437,3.703431,-1.715846,-6.239857,-0.964536,-9.783030,7.988311,6.065027,7.102800,2.715937,-5.701347,4.031688,7.400617,-5.945131,5.341418,8.023034,5.144355,5.848902,6.799095,4.215831,4.115110,4.272992,5.865874,9.780375,6.953966,9.188702,-4.073109,-9.698258,2.634230,-1.736256,-0.759104,-5.463260,-2.743265,-7.370450,-1.785991,5.848207,1.330183,-8.415848,3.826172,4.164448,-5.075535,-0.241984,5.097392,9.775167,-2.949172,-1.619460,3.352745,-3.036416,-7.750335,7.437407,-6.922216,9.575975,6.679233,-8.731989,6.567904,3.999287,-6.644945,-0.204687,-4.207885,-3.635994,1.679311,-6.972206,-6.746824,-1.056475,4.026173,3.065825,-5.608303,8.358518,-6.170251,-2.624916,9.478707,3.885039,-1.653109,9.148752,0.179392,2.338191,-8.047984,0.607209,-9.953125,-0.637992,-8.075734,0.197330,-1.846698,-5.798828,7.010744,-6.918918,4.251864,-3.995037,-3.410766,-7.358162,-9.027837,-5.747056,6.476391,2.699642,-0.368855,0.463621,4.605671,3.865967,4.902410,-7.342257,6.548223,3.553467,-3.624313,-3.104921,-0.395982,9.953839,-4.451099,0.910049,9.374222,2.147005,-4.297090,-1.899727,3.214803,8.916679,-1.059721,6.381333,0.581190,-6.028990,7.480479,-0.988144,2.052663,-9.933348,0.264298,-9.480597,-3.196754,-7.149348,-8.180994,-3.993660,7.493169,5.684130,0.675967,5.271612,1.952174,-8.405038,-9.661358,-7.480593,-7.354625,2.515386,4.162246,1.276239,6.048903,-0.584921,-3.982498,4.268410,1.022595,0.582689,-4.416589,2.456363,-8.155245,-4.388255,-8.667467,4.122878,7.491980,-2.332726,-9.592960,-0.084453,-6.804842,8.395020,3.036188,-7.823894,7.378339,5.400664,-1.331089,-0.795413,-5.296854,6.657861,3.020224,-0.173521,2.291550,3.283345,-7.007697,3.212143,0.128772,2.073173,5.102471,6.862086,-1.196680,-1.225696,5.335330,7.301788,7.952413,-2.887764,7.808056,8.215001,1.611271,-3.392209,-2.748882,-6.546952,2.219197,-9.219881,4.122687,3.214174,-6.109492,-4.508248,-8.053601,-4.227875,-3.742821,9.261835,2.512304,-9.210950,2.917822,-5.511000,-8.720234,4.576308,-9.398145,7.702155,2.695302,6.346059,-1.265439,3.677030,-9.701484,2.523220,-2.101336,-4.321194,4.584067,5.542398,-2.794273,4.208420,-1.261260,-6.320669,-6.703720,5.561861,-5.750233,-7.917798,-0.774854,-1.567335,9.242276,-0.884023,-0.824414,5.298704,5.121378,-9.637958,-9.633067,0.661792,7.802737,3.537973,9.030558,5.864087,-2.017138,-2.936882,-2.523435,5.934020,-2.294774,5.905430,-1.993195,1.047990,9.249923,2.664480,3.577770,9.373554,-5.670497,-1.291539,1.617091,-1.113275,4.195252,-0.290920,6.847061,2.835901,5.344580,-4.281169,1.242098,-2.401712,7.766434,-8.795074,-4.687115,4.542638,3.329807,-7.669642,-6.719586,-7.075097,1.306249,9.218131,-2.647963,8.977978,5.167872,4.258276,6.667792,-4.474150,-9.460264,9.626117,-1.088437,1.743445,-9.562595,-0.247547,-1.381168,0.869067,1.621347,-1.570147,8.324722,-7.137143,6.092693,-5.408598,2.485020,-8.302420,4.125729,-5.363731,-9.450665,2.065948,7.394214,6.061008,-6.524003,4.970066,3.454886,4.796859,9.447055,-8.288266,-1.864321,5.268014,0.650751,9.307645,3.212825,-9.659501,1.042569,0.348505,7.931546,4.767078,4.408533,4.171755,-3.034996,3.913900,-8.285879,0.225364,-1.285467,-4.082302,-0.669499,1.213818,7.179649,9.980354,6.709770,5.518837,-9.774434,1.742695,-2.427774,-1.142366,7.771258,-4.786086,8.048344,-8.217191,7.385198,1.443411,-8.465387,7.236865,-1.890841,5.532975,5.841079,-9.055224,2.728888,5.116410,2.377804,-1.084851,-5.433719,-1.908971,-9.918207,1.044327,-8.341803,4.819723,1.301063,-0.241289,-3.267558,-9.360434,1.837239,1.670759,-9.655577,-6.534220,-5.253322,-0.347440,4.553647,5.301292,-0.712661,6.506111,4.423270,7.961817,-4.239894,8.940897,4.949604,-4.039712,-4.047182,0.079001,3.968666,-7.455667,3.056506,-5.807610,-0.303579,-7.012014,-9.733417,4.286963,3.511951,9.762533,-3.340456,-5.982913,-6.434385,-5.788421,-8.618210,8.884065,9.587118,3.817984,-5.445799,-5.103079,1.834779,7.367758,-9.413231,-7.257352,-2.558593,9.725843,-0.521593,-7.113188,5.342308,4.919326,7.238268,1.453860,1.765558,8.940497,-7.902454,-5.267240,-7.448258,0.186686,-6.562578,-0.446258,1.638209,8.857986,7.116563,-9.397876,5.437108,-8.614059,-1.449976,6.233643,7.636763,-1.615080,-2.717658,6.619149,-6.609799,-4.780936,-4.064535,1.559875,-9.258466,6.276776,2.361098,-0.574167,-5.090488,5.882493,-4.929782,-9.148759,0.759668,2.177090,5.028510,-8.043448,-3.521413,-8.052348,-2.247559,-1.136794,-4.090689,-1.886736,-5.146626,-9.516660,-1.139568,8.264648,3.288822,-7.844890,-3.587265,-0.757119,-3.714210,-7.861674,4.153672,-4.413668,-6.251105,7.227544,-5.173164,-7.871666,-4.523345,9.740422,-7.700575,-3.166495,-4.627274,-3.854147,-5.971354,-0.466087,-2.144494,5.232518,7.320538,7.958012,2.335886,9.907545,-1.240307,-0.828524,-5.234504,1.598170,-9.027857,-1.275871,-0.756348,-8.926145,-2.799752,-4.426754,4.694753,-7.935532,4.694215,-7.549092,-1.542056,-7.063565,-4.762615,-6.550027,1.995472,2.508058,0.081898,-3.671701,8.630083,-3.084988,-0.092786,-3.122658,8.155361,-4.827125,-1.940601,9.975230,-4.342721,8.272256,-2.785592,-0.247477,-4.593765,0.752696,1.228790,7.502389,-7.087095,-9.439839,-8.996817,-9.335190,-0.653639,-3.352386,-1.849268,3.946256,-9.657167,8.087855,-9.772865,-5.968283,7.285523,-4.742899,2.882542,2.057655,-7.587949,-4.421139,-9.767388,-5.639272,-9.602195,9.254160,-8.193848,0.202642,-7.572058,0.322560,-1.882998,7.041309,6.627607,5.192811,5.389842,0.429749,-2.679914,8.145080,-7.005203,6.121394,-0.072815,4.551217,-0.513498,8.275777,0.153786,8.076590,-8.557945,-2.981733,7.385247,5.843960,-1.997159,-9.401043,-0.168410,-4.312495,4.415512,9.206079,-5.062085,-8.242048,-4.359257,9.507651,-6.788758,4.411115,0.913699,-9.104711,1.275003,-0.946716,-3.407240,7.882875,-7.513665,-7.726276,9.537320,8.329840,-4.923684,-6.945534,-4.759231,9.274150,3.504204,2.310859,-3.193550,4.323295,3.721580,8.107876,-0.128994,2.743696,-5.037250,-2.672681,0.078583,-7.637697,6.914634,-7.914317,-7.650487,-7.157135,3.249204,7.987584,3.469931,6.848828,-5.317520,9.270710,7.281551,4.950050,-7.466942,-5.986978,0.881176,0.618569,0.041156,-3.736524,6.152589,5.277282,4.674488,-2.662741,2.105121,4.280445,6.615363,-2.679045,3.211749,-5.979398,7.355532,-3.787618,4.905004,5.868078,6.131055,4.444656,-6.734219,6.731556,6.925326,3.141077,-9.467342,-2.287168,2.019822,-7.376307,-6.726153,-0.516185], dtype = "float32")#candidate|4432|(945,)|const|float32
call_4431 = relay.TupleGetItem(func_2050_call(relay.reshape(const_4432.astype('float32'), [7, 15, 9])), 3)
call_4433 = relay.TupleGetItem(func_2053_call(relay.reshape(const_4432.astype('float32'), [7, 15, 9])), 3)
output = relay.Tuple([call_4427,call_4431,const_4432,])
output2 = relay.Tuple([call_4428,call_4433,const_4432,])
func_4435 = relay.Function([], output)
mod['func_4435'] = func_4435
mod = relay.transform.InferType()(mod)
mutated_mod['func_4435'] = func_4435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4435_call = mutated_mod.get_global_var('func_4435')
call_4436 = func_4435_call()
output = call_4436
func_4437 = relay.Function([], output)
mutated_mod['func_4437'] = func_4437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_100_call = mod.get_global_var('func_100')
func_102_call = mutated_mod.get_global_var('func_102')
call_4444 = func_100_call()
call_4445 = func_100_call()
output = call_4444
output2 = call_4445
func_4447 = relay.Function([], output)
mod['func_4447'] = func_4447
mod = relay.transform.InferType()(mod)
mutated_mod['func_4447'] = func_4447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4447_call = mutated_mod.get_global_var('func_4447')
call_4448 = func_4447_call()
output = call_4448
func_4449 = relay.Function([], output)
mutated_mod['func_4449'] = func_4449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1764_call = mod.get_global_var('func_1764')
func_1766_call = mutated_mod.get_global_var('func_1766')
call_4470 = relay.TupleGetItem(func_1764_call(), 0)
call_4471 = relay.TupleGetItem(func_1766_call(), 0)
func_3354_call = mod.get_global_var('func_3354')
func_3356_call = mutated_mod.get_global_var('func_3356')
call_4472 = func_3354_call()
call_4473 = func_3354_call()
var_4493 = relay.var("var_4493", dtype = "float32", shape = (8, 15, 9))#candidate|4493|(8, 15, 9)|var|float32
bop_4494 = relay.less(call_4470.astype('bool'), var_4493.astype('bool')) # shape=(8, 15, 9)
bop_4497 = relay.less(call_4471.astype('bool'), var_4493.astype('bool')) # shape=(8, 15, 9)
func_2922_call = mod.get_global_var('func_2922')
func_2924_call = mutated_mod.get_global_var('func_2924')
call_4503 = relay.TupleGetItem(func_2922_call(), 0)
call_4504 = relay.TupleGetItem(func_2924_call(), 0)
uop_4510 = relay.sinh(var_4493.astype('float64')) # shape=(8, 15, 9)
func_2317_call = mod.get_global_var('func_2317')
func_2321_call = mutated_mod.get_global_var('func_2321')
var_4514 = relay.var("var_4514", dtype = "uint32", shape = (224,))#candidate|4514|(224,)|var|uint32
call_4513 = func_2317_call(relay.reshape(var_4514.astype('uint32'), [4, 8, 7]), relay.reshape(var_4514.astype('uint32'), [4, 8, 7]), )
call_4515 = func_2317_call(relay.reshape(var_4514.astype('uint32'), [4, 8, 7]), relay.reshape(var_4514.astype('uint32'), [4, 8, 7]), )
output = relay.Tuple([call_4472,bop_4494,call_4503,uop_4510,call_4513,var_4514,])
output2 = relay.Tuple([call_4473,bop_4497,call_4504,uop_4510,call_4515,var_4514,])
func_4535 = relay.Function([var_4493,var_4514,], output)
mod['func_4535'] = func_4535
mod = relay.transform.InferType()(mod)
var_4536 = relay.var("var_4536", dtype = "float32", shape = (8, 15, 9))#candidate|4536|(8, 15, 9)|var|float32
var_4537 = relay.var("var_4537", dtype = "uint32", shape = (224,))#candidate|4537|(224,)|var|uint32
output = func_4535(var_4536,var_4537,)
func_4538 = relay.Function([var_4536,var_4537,], output)
mutated_mod['func_4538'] = func_4538
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4551 = relay.const([[[-9,-4,5,4,9,2,6,8],[6,2,1,1,4,7,-10,-3],[9,6,3,-3,7,-8,7,-1],[-10,-2,-2,-6,-7,-4,3,7],[-7,8,-2,-2,-6,6,-6,6]],[[-1,6,-3,10,5,-6,3,10],[8,-10,9,-3,-4,-10,-5,-4],[-7,2,3,2,7,-8,-3,2],[6,-4,-6,4,6,-8,-2,-9],[-7,1,-2,9,10,2,8,5]],[[-8,3,-7,-3,10,-6,-8,-1],[6,6,-4,-9,-4,8,-5,-8],[-1,6,-5,-1,-2,7,-1,-6],[2,-7,7,-3,-9,3,-3,6],[9,3,4,-10,2,8,-8,2]],[[-6,-8,-5,4,-1,7,-7,9],[-8,1,-8,-10,-10,2,3,-10],[3,2,9,1,2,-4,-4,6],[-5,3,9,2,10,-9,-9,3],[-7,1,2,5,-3,-2,2,-6]],[[6,10,1,-5,9,-7,3,2],[7,-3,9,-3,-7,-7,5,-7],[3,8,-3,-6,-7,3,-4,-9],[10,10,-1,10,-7,8,10,-5],[-5,8,4,-2,-8,-2,-10,3]],[[-4,-1,-3,-3,-8,4,-6,-3],[-10,3,-5,-8,10,5,-10,1],[-1,-8,-5,-9,-2,3,10,1],[4,-5,-8,2,-2,9,-7,-7],[-5,7,6,3,8,5,9,-9]]], dtype = "int16")#candidate|4551|(6, 5, 8)|const|int16
var_4552 = relay.var("var_4552", dtype = "int16", shape = (6, 5, 8))#candidate|4552|(6, 5, 8)|var|int16
bop_4553 = relay.bitwise_or(const_4551.astype('int16'), relay.reshape(var_4552.astype('int16'), relay.shape_of(const_4551))) # shape=(6, 5, 8)
func_1314_call = mod.get_global_var('func_1314')
func_1318_call = mutated_mod.get_global_var('func_1318')
const_4557 = relay.const([1.686669,-6.555902,-8.634031,9.734500,0.575494,4.525603,2.696583,-1.653059,7.106716,0.509871,-9.401002,7.416452,-1.668149,-7.914742,1.458315,-8.214002,0.888345,1.328763,-3.514759,-5.927206,1.503262,1.905713,-9.912349,1.207484,1.214515,6.797884,-2.902782,5.291651,-0.255267,-6.208537,-1.337700,1.725151,3.388184,9.300312,0.637238,1.797170,2.883149,-6.899974,-0.803190,9.078271,-7.799850,0.223448,0.241512,1.295799,-9.313628,-1.007544,-7.465481,9.970094,-4.117495,0.867774,-8.137597,3.232958,3.824874,2.748352,9.925141,-0.353443,3.031817,-5.480785,-7.267406,6.596668,9.342164,7.368656,8.025848,3.989844,1.229183,1.124233,-7.896781,6.874758,-1.073037,9.610106,5.625960,2.397922,-6.161001,-8.074566,5.526456,5.675092,5.420867,-7.845268,3.570872,-7.598337,6.426989,-6.994091,-8.528601,6.358268,2.267615,-4.980993,-0.626909,2.821320,1.007244,-5.238644,1.342843,1.166152,-4.555005,5.929151,-7.025585,3.375475,-3.518914,3.467952,8.278534,7.178248,7.556149,-9.207245,-9.173255,-5.295443,8.375765,-6.034279,9.806181,7.265740,-1.217289,0.359488,-7.518836,-3.700629,4.300107,-1.478615,-1.239079,7.544221,8.192873,-5.723644,2.719921,-0.677182,4.210591,-2.076351,-7.349788,-7.839548,-6.797653,1.405241,-2.540502,3.624078,0.658206,7.691812,-8.968901,-8.610576,-8.404694,9.240885,5.296515,-4.091436,-8.852520,3.832115,-3.853304,0.612691,-1.640070,6.734235,-0.149033,-3.724727,-6.834973,-4.137132,-8.866905,5.832972,5.437366,-9.089364,-6.955009,6.134990,8.892892,3.513332,-9.422495,6.610375,-7.516550,-8.670403,8.520337,-2.554886,-0.436028,-8.840812,3.555543,0.073176,-9.813673,-4.606935,-5.374774,-5.325150,-1.194353,4.163416,-1.264424,6.697837,6.845206,-0.047827,-5.931514,2.309113,8.173707,6.648863,9.815699,1.552785,9.318678,-9.634548,3.482200,6.959833,-0.765144,-6.434905,1.353376,6.848332,3.332281,-4.656901,4.078758,-6.388377,0.658858,1.136017,-7.735685,7.822845,-4.345600,2.054612,-5.734283,-5.149103,6.673547,2.572242,-8.897895,-1.477455,-0.170335,-1.864814,-4.552715,-6.334339,-4.827462,-9.922645,-8.493444,-0.714968,8.906689,-1.203124,3.396327,-7.191556,-6.692750,0.135545,6.204065,-0.048802,-8.192881,3.369618,-5.268020,4.784915,5.009281,9.101732,7.154472,3.383406,-7.112960,-8.408035,-8.031332,-7.523682,-4.016715,6.967941,6.293085,-6.678552,-6.042283,-8.270233,4.792275,-8.803104,6.637638,6.931989,9.248517,2.446314,-9.336384,3.437336,1.085181,3.031450,-3.730365,0.579124,0.243806,9.842439,1.221466,-2.725416,6.778005,4.945953,-7.594545,1.076630,0.317847,0.185693,-8.532074,-6.222237,6.194866,-9.423898,6.108964,6.757675,1.776176,-0.053695,2.973210,8.092066,1.478817,3.215596,0.028510,-1.610710,-6.891868,9.590969,-2.864977,-0.325242,1.783488,1.149335,-0.704447,2.466390,-3.140437,-1.804222,-6.827447,-3.990786,-8.776196,-7.897897,4.976885,4.763775,-0.678865,-3.661674,-6.571607,-5.423234,6.155275,-6.428747,5.079300,6.473362,-8.540050,1.047098,-1.711896,-7.344939,6.960817,-3.593310,8.643902,-5.953361,-4.069283,1.009504,1.683299,5.443336,6.213733,-2.312511,8.386787,-3.232573,7.414981,2.040016,-1.741123,3.944375,-8.562155,-4.061913,3.043731,5.923660,3.931791,-5.526104,3.423808,-5.465055,-7.777846,3.094514,-4.720566,6.847109,9.275371,6.617554,-0.043861,6.799007,1.550507,7.041211,6.978238,-1.589681,8.681882,9.695750,-1.158659,4.041221,0.950292,3.974304,8.680198,0.559907,3.909435,-6.021321,1.569009,-3.945496,1.588766,7.029295,-4.540316,8.129762,4.545237,-7.412582,-5.855614,-2.310076,-7.076172,-7.099989,-6.755517,-7.708524,-6.251354,2.021968,0.650595,-9.477826,0.376249,3.639511,-3.712800,9.618691,1.187957,0.152809,-5.635938,0.711294,9.018520,-6.417226,-1.854481,0.347556,0.577374,-4.977517,-2.892798,7.142224,9.551620,-3.818415,7.646483,1.262916,0.313436,7.030611,-3.699913,6.319642,-8.444432,5.823892,-1.680317,5.135303,7.759522,-9.210339,9.192688,-4.780708,-2.718471,-8.597956,-1.420454,7.313573,-9.331597,6.437594,1.099870,3.673509,-7.690163,-3.098913,4.408470,-7.201461,-6.893818,0.160096,-3.622861,-3.959155,-6.469863,4.587561,-5.718668,-6.539964,7.085126,4.702330,-1.370432,-1.444966,2.283844,-8.243560,-1.623213,2.527057,2.013286,-9.690683,-2.084015,4.993532,1.822617,-9.324687,1.766333,7.742968,-4.037415,1.517209,8.747031,-1.216943,5.326573,4.949922,6.828395,-7.498703,8.489959,5.986854,7.266235,-9.318129,9.374763,-1.459386,-2.823543,2.982319,-6.285195,3.848215,-6.448644,-2.418681,-8.820380,5.364772,-0.574578,4.969884,3.497196,-4.355025,8.029980,0.896175,7.207943,3.635708,6.593598,-1.927180,9.776522,9.877012,0.541747,7.763817,-2.510748,-4.643821,-6.223799,-1.533705,-4.415625,-1.066745,-7.708966,-7.950113,1.175534,5.964437,-6.077615,-4.187996,0.965012,8.815135,8.292423,2.745681,6.934441,9.812772,7.378909,5.339961,-1.092253,6.074028,-5.972955,-4.482977,6.859653,-1.602797,4.918013,9.526409,6.270129,-2.380664,-1.447521,-6.369969,1.165879,7.269734,7.752571,-2.555499,9.529558,-7.738573,5.714076,2.235943,-7.734068,-1.977194,7.225947,9.956902,-8.102935,7.540557,2.208288,-5.039523,8.820437,9.245945,5.335921,-6.887770,8.539249,-9.374332,5.180082,7.568241,5.217999,-2.172933,8.988077,7.716273,4.093159,-3.101790,-3.690718,8.671826,9.408743,9.962023,-1.130865,3.663380,-2.845401,-7.420935,8.512747,-8.558743,9.863546,2.001381,-4.191541,-4.916296,-0.976029,-6.983305,8.317466,-8.829111,-7.306834,9.967222,-1.769367,-8.301018,-6.876608,-3.997036,-1.995057,7.591195,1.116672,-2.373085,0.492980,1.929629,-1.089302,6.220483,6.744254,-0.084406,0.771190,-3.803019,-5.367360,-8.414368,6.324020,-9.494204,2.355571,8.091384,4.868732,-3.613055,-8.473568,-0.205677,1.721012,1.324706,3.815124,-1.112338,9.411744,-9.056913,5.199224,0.361702,-8.753359,-8.320995,4.739835,-0.397984,-0.914463,5.776322,8.045902,0.781274,2.960341,4.779117,-2.054306,5.132890,9.590195,9.949266,4.602200,5.505155,-9.621000,1.924378,-7.605097,-1.596340,6.004560,8.343255,2.015005,6.011069,8.959369,-3.581602,5.527176,-3.739240,9.840297,4.460542,-8.238287,-9.017444,9.382517,-4.702504,-4.869121,-2.684308,-9.983673,-5.192432,-2.365530,0.303718,-0.610471,7.823817,6.076538,-6.305360,2.379693,1.608132,8.395161,-3.706390,-0.931785,-7.908607,-5.403816,-2.998212,-7.606923,-3.584293,-2.547949,2.638985,2.741013,-5.321905,-0.195402,-3.532992,9.517470,2.481707,3.115301,4.023458,-6.493733,-5.543485,-7.047642,5.454717,1.917424,0.520545,2.238047,4.949612,1.833538,-5.910207,-2.033511,2.460308,-6.602238,-7.275672,-8.855397,8.474582,8.422007,1.350280,-1.781988,0.587294,4.353114,-2.690862,5.942994,4.596095,6.994992,-2.493017,-1.634498,2.692164,-5.421634,5.314222,4.626451,9.177198,-5.346356,-4.312166,0.224457,0.523554,-7.517833,-7.479646,2.504444,-1.816025,4.706864,-6.590348,-9.547496,-6.186953,-5.966072,-9.831096,7.196041,-9.674538,-1.003082,-4.826795,-4.298233,-3.838166,5.558724,-9.290147,3.142593,-0.319281,3.822548,-5.121720,-2.052561,-0.268194,-8.738417,8.690044,-4.965579,-9.907149,-8.845948,2.741240,-6.416905,-0.599081,-8.002878,-4.784084,0.353553,-0.026395,0.798939,4.886188,7.161631,-2.551589,-7.830468,5.827361,-8.892250,3.146343,6.667163,8.808956,7.504769,6.395341,5.393466,8.766866,-0.876516,6.683645,-6.755450,-9.722210,6.482796,-4.357463,-3.185381,-4.625383,3.570510,3.828556,-7.890956,-8.751565,-6.532666,6.494293,9.145418,8.965268,-5.343228,4.714339,3.989193,9.041506,9.712098,-9.957420,4.345205,-5.871526,-0.482157,2.699553,-0.363844,-3.831390,-1.133521,-9.137267,-8.673223,4.678771,4.952822,-7.186640,-6.148749,4.408689,3.076746,4.539677,-1.220081,1.806512,-8.717570,-8.578199,-1.417940,9.429579,-7.073534,-5.287723,2.306227,-0.692839,-1.072639,6.925757,-1.050322,-5.145735,-7.698049,-8.787661,0.149484,-6.320060,4.738249,0.783960,4.434515,-6.578982,-5.265301,0.693824,-0.502655,-8.537747,-6.199983,-0.485799,-7.909862,-6.317913,-9.403493,-3.577100,-6.826540,2.414010,0.795570,9.670707,-6.988537,-3.942705,-3.330390,-6.459202,1.076770,9.869927,2.968115,-4.716143,2.084628,-7.511853,-5.892501,6.196354,7.552883,-6.564213,5.125801,-0.934866,9.526643,4.834991,-4.651641,-5.310609,-4.246975,6.591688,6.007989,-9.779765,-7.642895,6.768665,8.555979,4.292421,4.467845,8.364158,0.945918,-4.910826,-9.104459,-9.091686,-0.959120,0.397093,-1.114102,-9.651729,-6.560674,-6.245098,8.264019,7.035372,6.888964,-8.664198,-4.098229,8.844050,9.245186,-8.822016,7.867572,-2.202667,-3.187774,1.008793,-0.903956,-0.366852,-1.720657,3.535470,-0.144799,-3.746186,7.380084,2.641330,-6.861452,4.455684,-5.817091,1.774769,-7.561560,9.564864,1.448881,8.021914,-7.172030,9.455935,1.401441,2.692224,2.088602,0.258653,-1.179591,8.569214,9.428556,-7.855484,-8.465202,-5.863230,9.033616,8.603032,-7.514344,-8.050620,3.239539,6.593154,-8.939069,-1.181256,-8.122492,-1.060270,-4.086110,1.681661,-7.332870,-5.450153,7.200584,4.504459,-2.867593,-0.511621,3.654385,-9.247668,-5.390140,8.957264,-0.398998,-3.018379,4.853599,5.086648,-5.225144,-2.411135,-0.053971,-7.645417,1.857550,-7.043642,-5.267541,-2.568194,8.307553,-1.186808,-9.790573,-4.521419,-6.300305,8.188623,4.448883,6.674361,9.251346,-0.580366,-7.211500,2.521152,-9.551247,-8.808433,-8.087408,-6.746440,9.564187,9.295222,0.902745,-4.383917,3.410894,2.350802,-7.438126,-6.543750,-0.098147,0.318383,0.339934,-9.515605,-0.587292,5.351047,5.056577,-3.441655,-1.577282,-1.242276,2.762587,9.838526,-3.253320,2.953471,-4.250614,-5.482002,-1.396811,9.131932,5.141775,4.551490,-4.896010,-0.817309,-5.501412,-0.854150,4.170222,-0.230737,9.666345,1.829049,1.756121,-4.953810,-8.701033,-6.022468,-4.545594,0.029231,-9.297578,6.449398,0.812255,-5.729040,-4.189102,-6.932487,-1.405235,-9.691619,3.870250,7.851893,-8.872334,-3.153471,8.788323,8.662939,-5.749028,7.171808,0.976069,-7.866506,-1.826977,2.235857,6.526910,-4.382151,-3.197299,-4.724728,-1.491413,-8.707148,9.588600,-5.268242,-4.042221,4.547603,-6.953437,3.499629,8.538964,-6.945811,-9.921993,0.201766,1.066330,1.278979,-7.247915,3.468074,-9.772047,-1.557928,-6.147621,-7.483996,-5.615040,-6.829121,-3.722121,5.215541,9.980771,5.050711,9.078149,7.161950,4.734733,-2.458576,-0.961262,-7.710885,-5.081274,5.140530,5.018903,8.941193,2.744835,-0.886382,7.869688,4.786897,9.941337,-8.382851,3.901138,-7.954489,8.280028,4.161467,-4.896765,-5.860489,-9.223431,-7.520089,4.565273,1.080132,4.042178,-6.389359,0.102691,5.376216,-6.774808,4.401863,8.682558,-6.812454,5.193739,5.910593,-8.090418,-8.246945,1.966382,-3.910806,-6.094337,7.313932,-8.809441,-4.252072,4.632637,-7.012969,5.475067,-9.017865,7.754099,9.940520,-2.121593,1.018980,-7.782036,8.024298,-9.508789,-4.839409,4.414885,-7.651533,3.066894,-7.076334,-7.163052,9.930630,-3.238645,-9.935527,-9.307092,-9.758728,-0.546783,3.776542,8.133780,-1.079367,9.024048,-5.359157,-8.321489,-9.589531,1.949214,0.656361,3.978662,-4.136425,-0.468940,-5.603541,-6.996946,4.384338,-8.884466,-5.032610,0.286604,0.087424,5.256496,6.770375,-5.557369,-8.034060,-2.270919,0.531732,-6.449136,-5.419022,-1.229609,4.318926,2.947510,-7.913991,-3.244507,-4.605476,6.425182,-0.749354,5.238396,5.461872,3.268459,-8.668313,6.070379,7.833536,4.194444,-0.395347,-6.205449,-8.269122,-9.722318,6.826197,7.259558,-0.691555,6.909698,-3.354820,-2.102295,-8.682383,2.088936,-6.461921,-4.929111,-6.292463,4.258153,-5.167479,-4.282075,7.140499,7.351473,1.272603,-4.446276,2.631019,-8.132852,6.892473,2.967855,-6.584253,-9.687812,5.623473,7.204892,-7.030286,-7.893075,-0.904027,5.273637,3.316430,9.815311,-2.860377,-0.837499,3.253766,2.038139,-5.655636,2.445659,0.454791,0.749684,-2.239841,-2.303772,2.352274,3.598856,7.319746,6.533498,7.576863,-6.877384,2.551678,-7.329978,8.777554,2.615018,-2.893544,5.066656,-5.646062,1.847154,3.628348,5.637909,-6.388294,-3.179559,8.078175,7.508618,-8.708015,-2.607926,-6.409092,0.153848,-9.632804,7.598802,6.505890,-8.747538], dtype = "float32")#candidate|4557|(1215,)|const|float32
const_4558 = relay.const([[3.022622],[3.601095],[-7.986045],[-1.678040],[9.864404],[0.604733],[-2.830943],[-9.288687],[0.200300],[-4.652147],[-7.464800],[4.823315],[7.798560],[-9.207559],[0.178782],[4.618346],[2.753104],[5.970659],[9.863975],[0.051208],[-0.639856],[4.486003],[0.259168],[-1.838785],[-5.326645],[5.317258],[-9.458295],[-8.929813],[-9.194949],[-4.421919],[-3.644038],[-3.140234],[-8.211255],[3.548337],[6.235939],[-5.562823],[4.010200],[-1.444393],[-8.531351],[-3.262376],[8.666673],[8.907126],[-7.993348],[4.806783],[-8.333797],[4.748787],[3.492113],[-4.472311],[2.960333],[-9.933884],[3.695688],[-2.734615],[-2.013589],[7.358616],[-0.893508],[6.196180],[1.535997],[9.526494],[-5.004588],[-1.148644],[-2.888274],[-1.850008],[-2.675372],[5.479821],[-8.202918],[-4.281840],[1.025230],[0.084145],[-6.907379],[-7.928876],[-0.403526],[-4.169948],[-7.067663],[8.494517],[3.313991],[2.624426],[3.202485],[6.915073],[-5.125003],[1.463370],[-7.089680]], dtype = "float32")#candidate|4558|(81, 1)|const|float32
call_4556 = relay.TupleGetItem(func_1314_call(relay.reshape(const_4557.astype('float32'), [9, 15, 9]), relay.reshape(const_4558.astype('float32'), [81,]), ), 5)
call_4559 = relay.TupleGetItem(func_1318_call(relay.reshape(const_4557.astype('float32'), [9, 15, 9]), relay.reshape(const_4558.astype('float32'), [81,]), ), 5)
output = relay.Tuple([bop_4553,call_4556,const_4557,const_4558,])
output2 = relay.Tuple([bop_4553,call_4559,const_4557,const_4558,])
func_4561 = relay.Function([var_4552,], output)
mod['func_4561'] = func_4561
mod = relay.transform.InferType()(mod)
var_4562 = relay.var("var_4562", dtype = "int16", shape = (6, 5, 8))#candidate|4562|(6, 5, 8)|var|int16
output = func_4561(var_4562)
func_4563 = relay.Function([var_4562], output)
mutated_mod['func_4563'] = func_4563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_4584 = relay.TupleGetItem(func_586_call(), 1)
call_4585 = relay.TupleGetItem(func_588_call(), 1)
var_4608 = relay.var("var_4608", dtype = "float32", shape = (16, 15, 9))#candidate|4608|(16, 15, 9)|var|float32
bop_4609 = relay.less_equal(call_4584.astype('bool'), var_4608.astype('bool')) # shape=(16, 15, 9)
bop_4612 = relay.less_equal(call_4585.astype('bool'), var_4608.astype('bool')) # shape=(16, 15, 9)
func_1652_call = mod.get_global_var('func_1652')
func_1657_call = mutated_mod.get_global_var('func_1657')
var_4620 = relay.var("var_4620", dtype = "float64", shape = (672,))#candidate|4620|(672,)|var|float64
var_4621 = relay.var("var_4621", dtype = "float32", shape = (90, 3))#candidate|4621|(90, 3)|var|float32
call_4619 = relay.TupleGetItem(func_1652_call(relay.reshape(var_4620.astype('float64'), [7, 16, 6]), relay.reshape(var_4620.astype('float64'), [7, 16, 6]), relay.reshape(var_4621.astype('float32'), [270,]), ), 3)
call_4622 = relay.TupleGetItem(func_1657_call(relay.reshape(var_4620.astype('float64'), [7, 16, 6]), relay.reshape(var_4620.astype('float64'), [7, 16, 6]), relay.reshape(var_4621.astype('float32'), [270,]), ), 3)
bop_4630 = relay.greater(call_4584.astype('bool'), var_4608.astype('bool')) # shape=(16, 15, 9)
bop_4633 = relay.greater(call_4585.astype('bool'), var_4608.astype('bool')) # shape=(16, 15, 9)
func_3354_call = mod.get_global_var('func_3354')
func_3356_call = mutated_mod.get_global_var('func_3356')
call_4637 = func_3354_call()
call_4638 = func_3354_call()
func_3071_call = mod.get_global_var('func_3071')
func_3072_call = mutated_mod.get_global_var('func_3072')
call_4641 = relay.TupleGetItem(func_3071_call(), 0)
call_4642 = relay.TupleGetItem(func_3072_call(), 0)
bop_4652 = relay.floor_mod(var_4608.astype('float64'), call_4641.astype('float64')) # shape=(16, 15, 9)
bop_4655 = relay.floor_mod(var_4608.astype('float64'), call_4642.astype('float64')) # shape=(16, 15, 9)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_4657 = func_1958_call()
call_4658 = func_1958_call()
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
call_4669 = relay.TupleGetItem(func_1197_call(), 0)
call_4670 = relay.TupleGetItem(func_1199_call(), 0)
output = relay.Tuple([bop_4609,call_4619,var_4620,var_4621,bop_4630,call_4637,bop_4652,call_4657,call_4669,])
output2 = relay.Tuple([bop_4612,call_4622,var_4620,var_4621,bop_4633,call_4638,bop_4655,call_4658,call_4670,])
func_4685 = relay.Function([var_4608,var_4620,var_4621,], output)
mod['func_4685'] = func_4685
mod = relay.transform.InferType()(mod)
mutated_mod['func_4685'] = func_4685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4685_call = mutated_mod.get_global_var('func_4685')
var_4687 = relay.var("var_4687", dtype = "float32", shape = (16, 15, 9))#candidate|4687|(16, 15, 9)|var|float32
var_4688 = relay.var("var_4688", dtype = "float64", shape = (672,))#candidate|4688|(672,)|var|float64
var_4689 = relay.var("var_4689", dtype = "float32", shape = (90, 3))#candidate|4689|(90, 3)|var|float32
call_4686 = func_4685_call(var_4687,var_4688,var_4689,)
output = call_4686
func_4690 = relay.Function([var_4687,var_4688,var_4689,], output)
mutated_mod['func_4690'] = func_4690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_689_call = mod.get_global_var('func_689')
func_690_call = mutated_mod.get_global_var('func_690')
call_4702 = func_689_call()
call_4703 = func_689_call()
output = relay.Tuple([call_4702,])
output2 = relay.Tuple([call_4703,])
func_4705 = relay.Function([], output)
mod['func_4705'] = func_4705
mod = relay.transform.InferType()(mod)
mutated_mod['func_4705'] = func_4705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4705_call = mutated_mod.get_global_var('func_4705')
call_4706 = func_4705_call()
output = call_4706
func_4707 = relay.Function([], output)
mutated_mod['func_4707'] = func_4707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4308_call = mod.get_global_var('func_4308')
func_4310_call = mutated_mod.get_global_var('func_4310')
call_4719 = relay.TupleGetItem(func_4308_call(), 1)
call_4720 = relay.TupleGetItem(func_4310_call(), 1)
output = call_4719
output2 = call_4720
func_4729 = relay.Function([], output)
mod['func_4729'] = func_4729
mod = relay.transform.InferType()(mod)
mutated_mod['func_4729'] = func_4729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4729_call = mutated_mod.get_global_var('func_4729')
call_4730 = func_4729_call()
output = call_4730
func_4731 = relay.Function([], output)
mutated_mod['func_4731'] = func_4731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4308_call = mod.get_global_var('func_4308')
func_4310_call = mutated_mod.get_global_var('func_4310')
call_4738 = relay.TupleGetItem(func_4308_call(), 1)
call_4739 = relay.TupleGetItem(func_4310_call(), 1)
output = relay.Tuple([call_4738,])
output2 = relay.Tuple([call_4739,])
func_4740 = relay.Function([], output)
mod['func_4740'] = func_4740
mod = relay.transform.InferType()(mod)
output = func_4740()
func_4741 = relay.Function([], output)
mutated_mod['func_4741'] = func_4741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3770_call = mod.get_global_var('func_3770')
func_3771_call = mutated_mod.get_global_var('func_3771')
call_4791 = relay.TupleGetItem(func_3770_call(), 0)
call_4792 = relay.TupleGetItem(func_3771_call(), 0)
const_4793 = relay.const([[[-5.819488,-1.099771,-2.808856,-1.799461,4.633338,-2.145795,-4.682176,8.116778,6.494079],[7.198889,0.897732,-5.070248,-8.046095,4.029357,-8.619844,1.860384,-2.767652,-8.878405],[-5.807434,-1.614078,-2.167889,-3.295059,4.428736,0.164678,6.704130,9.672625,6.088102],[-1.727056,5.263712,-5.809218,-0.137479,-6.811083,8.083572,-5.326294,5.245539,6.462928],[2.747491,-5.008339,8.167750,1.815152,0.651733,-1.844320,4.280050,-0.352685,-6.389533],[-6.036948,4.008837,6.279925,0.058546,-6.329777,-2.951687,2.275772,-0.652464,0.968389],[0.460677,-3.019968,6.185282,7.862402,7.796219,8.403192,-7.402692,-5.276954,-8.872251],[-5.281612,2.906663,-7.258969,-7.860755,7.605531,-7.173998,-6.642681,-8.033210,-3.231906],[0.353955,-2.759290,7.107237,-9.606398,6.990859,8.746285,-5.963125,-0.864840,5.935277],[-5.809490,-7.309097,-5.936054,-2.429865,-8.423851,0.168476,-7.038856,-8.806555,2.265437],[-0.501541,7.552226,-4.837542,5.296052,-7.505768,1.239751,-3.126867,8.804002,2.002436],[5.064610,-6.998335,-0.710990,-3.706099,9.831839,7.488347,5.047796,-0.929163,-9.691693],[4.494741,-7.320775,8.047884,5.635331,8.459989,-6.841381,-5.877276,-7.320179,2.915601],[-8.077622,8.813644,-9.404131,-1.425253,-4.869737,-5.626177,-7.048952,-0.325815,4.518878],[-6.525172,8.585262,3.100230,-6.884308,-0.620808,-0.150249,-8.203542,2.220282,-4.599726]],[[-6.727132,5.941004,-9.115087,4.310522,-7.628844,2.947393,2.148267,-7.181792,3.989652],[-3.006819,-6.463659,-5.935599,-9.556979,4.185304,-0.486609,1.920869,7.672326,1.461406],[-4.836776,-5.082050,-0.400868,-1.158640,2.118265,-1.752369,-8.120382,-5.013835,3.117258],[-0.436392,4.324078,-5.597259,4.399938,0.362030,-8.695395,-4.315551,9.534031,8.740658],[-6.705282,-2.346497,2.030956,-8.689933,6.102366,-5.836288,6.010128,7.719754,-0.130033],[-6.072764,4.969873,-9.205592,-0.143983,4.353430,2.952151,2.982029,-0.656102,8.809486],[1.349952,-4.661680,9.544931,5.991323,0.204436,8.980693,-9.158188,9.905627,7.940724],[-8.053004,0.688627,-7.559404,-4.234696,-0.823678,1.789111,-4.920582,-9.091588,1.722267],[0.198455,-8.805706,0.058004,9.396581,-2.845813,-6.475725,-1.593362,3.437082,-0.056061],[0.624408,-6.109129,7.714637,9.254224,-8.378377,-4.573762,8.563520,-0.140891,-3.957938],[-2.269490,-2.978175,4.551514,-0.297258,3.216172,1.538729,0.437436,-3.053807,-4.588344],[5.244417,-5.204064,7.498982,-6.285269,-5.734370,1.837156,-4.087599,-6.531161,-1.041340],[9.407235,-0.909157,-3.516121,-6.263430,-7.335913,2.971972,9.955058,-8.372433,-4.387651],[-0.391146,7.482448,-4.643227,-9.015033,-9.187883,6.168587,-0.485666,9.670831,0.863706],[-3.707682,-7.057472,-0.050819,5.765065,-3.455597,0.296993,-4.621043,0.784679,3.947291]],[[-0.494233,8.681966,-2.259140,3.373919,8.936364,9.082674,-0.784876,9.457006,-8.207973],[3.344384,0.796273,-1.223909,-2.262093,-3.272830,-1.467908,6.400182,8.086301,7.314702],[4.206036,-9.942860,4.036550,8.879562,6.503688,-3.214555,6.603741,-5.387205,-1.521044],[4.519046,0.374082,-6.142611,9.706176,-2.202680,-3.235515,6.318341,-8.617555,6.599571],[0.960075,4.052306,8.084804,1.054684,2.065663,4.429440,-1.350978,4.169382,-4.348721],[6.525456,9.558227,3.020043,7.692946,-1.123214,-9.407789,4.482841,-1.004675,1.228158],[0.422589,-3.060159,-0.589453,-8.295118,2.845184,-5.676440,1.579447,9.465792,7.410307],[8.259344,0.758903,-0.947837,9.667556,-6.737653,-8.503488,0.499963,-5.913368,2.161153],[3.231166,9.330249,6.292168,-7.944336,4.713335,5.517496,-4.154251,4.950716,-2.727130],[-9.491135,2.868092,-7.916344,-0.496049,9.307209,1.566698,4.243197,-7.392857,2.706900],[-1.754879,0.384732,-9.585353,-3.503317,7.924056,-9.545821,5.999960,3.980822,5.154511],[-1.513757,7.098977,-5.905233,-5.206081,6.735273,-1.147392,-9.806947,-0.256049,-3.567087],[6.347691,-3.258547,-0.566284,-0.336142,9.592712,1.131568,3.183328,-7.357208,4.521291],[-0.769755,-5.392800,4.688965,-2.332071,1.706284,0.845935,8.411277,-7.913540,8.460406],[7.417970,-9.697185,2.840902,5.330504,4.464613,3.053500,7.257741,3.178258,1.227204]],[[-5.897251,-2.857347,-7.581715,-9.423436,-7.665842,2.635610,2.448794,-5.161754,0.406024],[0.894059,-6.360015,-6.981393,-6.318343,1.498253,3.533310,-7.199602,4.145734,5.201599],[-8.373589,2.362194,-9.476105,-0.267347,3.619535,5.065308,-1.040698,-4.461771,-4.098122],[-3.786599,-7.431414,-9.618714,-6.344040,3.394245,0.260773,8.365498,-7.614053,4.594682],[-9.473811,7.286391,-8.793779,-5.028843,7.897332,2.766185,-7.827625,-3.514787,-1.758686],[-3.982266,9.207565,-6.389404,0.521355,-6.761914,-6.796928,-8.060310,2.916639,5.858793],[7.996622,-6.634276,-6.958950,-0.871438,0.057245,1.178537,6.009970,-3.163776,8.574971],[8.343622,9.041025,6.225727,6.646795,-6.675633,2.428178,-3.736580,8.634855,2.419802],[2.948177,-1.803574,4.695278,-8.095229,-7.917754,2.276348,9.720640,-9.636168,6.027930],[-8.824891,8.352680,1.772052,-1.051748,5.395923,0.715320,4.061082,-3.572391,2.521975],[5.765339,-9.888383,4.099345,-8.928393,0.968844,9.550959,-4.298726,7.666515,-5.502833],[-8.695197,8.009586,-2.084927,-7.243108,6.538047,-7.538753,-6.392628,-6.390755,4.939760],[9.764272,-9.190138,-4.276336,5.753008,4.905383,-2.730153,8.702078,7.198023,9.030736],[8.893717,2.821768,-8.147093,-5.502423,-1.832991,-3.744781,-0.922941,9.060240,-7.549438],[-7.974159,-6.819504,-8.696955,6.307460,7.529819,-9.978721,-3.821220,-8.380259,-1.236696]]], dtype = "float32")#candidate|4793|(4, 15, 9)|const|float32
bop_4794 = relay.logical_xor(call_4791.astype('uint32'), const_4793.astype('uint32')) # shape=(4, 15, 9)
bop_4797 = relay.logical_xor(call_4792.astype('uint32'), const_4793.astype('uint32')) # shape=(4, 15, 9)
output = relay.Tuple([bop_4794,])
output2 = relay.Tuple([bop_4797,])
func_4800 = relay.Function([], output)
mod['func_4800'] = func_4800
mod = relay.transform.InferType()(mod)
output = func_4800()
func_4801 = relay.Function([], output)
mutated_mod['func_4801'] = func_4801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1863_call = mod.get_global_var('func_1863')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_4857 = relay.TupleGetItem(func_1863_call(), 0)
call_4858 = relay.TupleGetItem(func_1864_call(), 0)
output = call_4857
output2 = call_4858
func_4863 = relay.Function([], output)
mod['func_4863'] = func_4863
mod = relay.transform.InferType()(mod)
output = func_4863()
func_4864 = relay.Function([], output)
mutated_mod['func_4864'] = func_4864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2511_call = mod.get_global_var('func_2511')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_4911 = relay.TupleGetItem(func_2511_call(), 0)
call_4912 = relay.TupleGetItem(func_2513_call(), 0)
output = call_4911
output2 = call_4912
func_4921 = relay.Function([], output)
mod['func_4921'] = func_4921
mod = relay.transform.InferType()(mod)
mutated_mod['func_4921'] = func_4921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4921_call = mutated_mod.get_global_var('func_4921')
call_4922 = func_4921_call()
output = call_4922
func_4923 = relay.Function([], output)
mutated_mod['func_4923'] = func_4923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_4943 = relay.TupleGetItem(func_1070_call(), 0)
call_4944 = relay.TupleGetItem(func_1072_call(), 0)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_4947 = relay.TupleGetItem(func_139_call(), 0)
call_4948 = relay.TupleGetItem(func_140_call(), 0)
func_2887_call = mod.get_global_var('func_2887')
func_2890_call = mutated_mod.get_global_var('func_2890')
var_4950 = relay.var("var_4950", dtype = "float32", shape = (1, 280))#candidate|4950|(1, 280)|var|float32
call_4949 = relay.TupleGetItem(func_2887_call(relay.reshape(var_4950.astype('float32'), [2, 14, 10])), 0)
call_4951 = relay.TupleGetItem(func_2890_call(relay.reshape(var_4950.astype('float32'), [2, 14, 10])), 0)
func_685_call = mod.get_global_var('func_685')
func_686_call = mutated_mod.get_global_var('func_686')
call_4955 = func_685_call()
call_4956 = func_685_call()
uop_4964 = relay.sqrt(call_4949.astype('float32')) # shape=(2, 14, 10)
uop_4966 = relay.sqrt(call_4951.astype('float32')) # shape=(2, 14, 10)
bop_4969 = relay.less_equal(call_4943.astype('bool'), relay.reshape(call_4947.astype('bool'), relay.shape_of(call_4943))) # shape=(1, 15, 9)
bop_4972 = relay.less_equal(call_4944.astype('bool'), relay.reshape(call_4948.astype('bool'), relay.shape_of(call_4944))) # shape=(1, 15, 9)
output = relay.Tuple([var_4950,call_4955,uop_4964,bop_4969,])
output2 = relay.Tuple([var_4950,call_4956,uop_4966,bop_4972,])
func_4975 = relay.Function([var_4950,], output)
mod['func_4975'] = func_4975
mod = relay.transform.InferType()(mod)
mutated_mod['func_4975'] = func_4975
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4976 = relay.var("var_4976", dtype = "float32", shape = (1, 280))#candidate|4976|(1, 280)|var|float32
func_4975_call = mutated_mod.get_global_var('func_4975')
call_4977 = func_4975_call(var_4976)
output = call_4977
func_4978 = relay.Function([var_4976], output)
mutated_mod['func_4978'] = func_4978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mod.get_global_var('func_4407')
func_4409_call = mutated_mod.get_global_var('func_4409')
call_4983 = func_4407_call()
call_4984 = func_4407_call()
const_5003 = relay.const([[[8.134878,-0.379590,7.709196,-8.585463,4.337858,-3.805196,0.087547,-6.618267,-1.231917],[-8.937930,5.178920,7.856503,7.470365,3.256909,4.269442,-8.369495,-1.756351,0.911755],[-4.138694,-3.199351,-5.574910,6.315247,-7.230575,-2.003981,7.293551,2.200115,6.032087],[7.262302,-8.011717,-4.616915,8.263259,-3.690925,4.001383,0.420792,9.076541,-0.611401],[-7.347949,-4.954181,7.427681,1.588204,6.855863,9.622570,-8.842574,1.419004,7.050674],[-2.771925,-9.589447,9.454417,-1.642343,-6.679087,-1.928207,-6.968873,-4.976782,1.074501],[9.507043,-0.437042,0.535695,-9.646520,-7.988970,-7.421141,2.770803,0.631352,-6.053174],[3.099118,4.225391,-1.438769,-9.430053,2.939073,6.139280,-9.175325,0.641718,0.647707],[-4.115046,-9.179986,-4.719427,0.622561,-3.177849,5.535110,5.468160,8.842567,-6.534883],[-0.591337,-8.908582,-2.956895,8.765363,7.876504,7.314714,8.445385,-7.786711,2.102667],[0.974621,-7.092694,6.052871,-4.768559,-0.280731,2.405504,0.384049,-5.206904,9.923199],[-5.264179,1.578887,-1.391365,-1.426095,6.026928,4.236156,0.094157,2.800058,-4.237788],[-6.039214,3.173370,1.728155,5.738049,-9.253550,-7.062520,-9.987170,-3.149352,-6.523288],[4.546380,6.513895,4.725226,3.422668,0.246412,-6.549517,3.002877,-5.101137,-1.765195],[6.082485,-8.941104,8.014601,-6.306379,6.884566,4.996921,8.337929,6.369009,5.454196]],[[9.229144,8.794234,9.359675,3.706184,-6.497724,7.176905,5.447119,2.321428,1.515169],[-0.587755,-9.440629,-1.120919,-0.339366,-1.801271,-6.498817,-7.385565,-6.305864,-4.859889],[-7.257016,-4.413701,0.028928,3.052538,0.117891,4.398952,5.811293,-7.476571,1.300255],[9.456473,-8.657584,6.082025,-6.195575,-4.024168,-3.800920,-1.995286,-6.566721,8.044508],[0.969368,-2.718515,7.171064,7.215225,-1.128663,1.593749,-7.230002,7.510403,-7.513361],[-0.854368,-3.345776,-4.280024,0.594796,6.919469,3.033774,-6.670197,1.124528,6.570571],[-7.670992,4.434883,-1.518974,-5.321447,-5.612791,9.683339,7.447965,4.650763,2.503834],[-0.876856,-7.176487,-4.402429,-7.749728,-9.093195,-8.009403,3.167596,-6.206329,4.273612],[1.670632,-8.405632,6.063490,-1.926175,6.955619,-4.558053,2.472604,4.796256,4.171997],[-0.724710,-2.461076,2.376333,-6.970405,9.785372,-1.856617,-2.437258,6.846160,2.064387],[-9.296870,1.216629,3.157092,-7.503896,-1.743340,-7.901379,-5.266776,6.558728,-8.004103],[4.727475,2.436926,1.786113,3.572950,0.103475,-2.406551,7.267272,8.927702,-1.937515],[-3.569124,6.637527,8.029354,-7.255553,-0.248990,-4.326785,8.080510,-0.155030,1.058754],[-2.808943,0.135047,8.917410,-1.696459,-2.327220,4.816261,-6.210553,-1.469578,-8.624841],[9.547184,1.376903,-3.061363,-3.024316,8.794913,1.048042,9.390225,1.580465,7.859251]],[[-1.279200,9.232982,9.873341,-8.961072,-1.874677,-8.338556,-5.812447,-2.555662,7.170139],[7.062886,-9.155612,-4.891190,0.146703,1.183572,-4.448276,3.523404,-5.698807,-6.442488],[4.996840,6.385839,8.631183,-9.961021,1.043145,3.955516,-5.088963,2.596429,9.033218],[-7.278998,9.432931,9.737508,-4.867459,-9.776028,0.352088,3.008784,7.092691,-7.992338],[-8.092756,-6.147842,1.886109,-1.267085,8.451234,-1.203275,-1.648444,1.229505,-8.061277],[1.563081,-6.938157,8.206849,-2.542022,-2.718025,6.560854,-0.818290,-4.574888,-0.279650],[-0.734810,5.779173,-5.717462,-5.995586,-3.138645,-5.047381,-6.141190,3.447048,6.077862],[-2.287117,1.854819,-5.669093,-7.770530,-5.431895,3.349133,-5.959202,-9.672818,6.993647],[-2.854518,1.291585,-8.773229,6.591029,7.123137,5.222256,-8.771341,6.216932,-8.034480],[-9.749977,-8.353390,5.445481,7.874460,-7.026100,8.986468,-6.351596,1.614499,-9.551199],[4.019746,4.071390,6.960139,-4.380354,-1.604634,4.316120,1.899287,1.527627,3.462255],[6.397993,7.490906,-2.866793,-1.340051,-9.247399,-0.917599,5.587430,-9.827719,-7.136249],[9.956969,6.414985,-5.539330,-0.617840,7.499546,-4.356298,9.930723,9.730153,3.713850],[6.539543,3.566962,8.683407,1.562106,8.924840,3.032434,9.468239,-1.669534,4.519305],[1.271885,-5.682259,5.547678,0.269496,8.627080,8.275620,-1.374343,-6.107851,-1.363623]]], dtype = "float32")#candidate|5003|(3, 15, 9)|const|float32
bop_5004 = relay.bitwise_and(call_4983.astype('uint16'), const_5003.astype('uint16')) # shape=(3, 15, 9)
bop_5007 = relay.bitwise_and(call_4984.astype('uint16'), const_5003.astype('uint16')) # shape=(3, 15, 9)
uop_5009 = relay.tan(bop_5004.astype('float32')) # shape=(3, 15, 9)
uop_5011 = relay.tan(bop_5007.astype('float32')) # shape=(3, 15, 9)
output = uop_5009
output2 = uop_5011
func_5016 = relay.Function([], output)
mod['func_5016'] = func_5016
mod = relay.transform.InferType()(mod)
output = func_5016()
func_5017 = relay.Function([], output)
mutated_mod['func_5017'] = func_5017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_5018 = func_1958_call()
call_5019 = func_1958_call()
const_5022 = relay.const([[[5.994633,3.792833,-5.086103,-7.898818,-8.424941,1.744544,-8.242607,-1.839215,-0.776609],[3.256356,-5.391113,2.729771,0.718596,-5.725442,-9.422820,8.874203,-1.202583,0.758691],[2.579963,-1.475872,-7.558813,6.617869,-0.671002,8.442553,-3.213680,8.391853,-9.028690],[-5.675438,1.490283,-2.198223,-7.652888,-1.231927,-3.293032,-4.753925,4.225630,2.888424],[-9.954542,-3.846912,6.622011,1.190150,-9.104492,-3.946275,4.292503,-0.855532,0.580653],[-7.604293,3.528489,-6.238259,6.811180,8.512089,-8.177061,-3.931587,-7.377470,7.563647],[-0.289227,1.515953,4.841877,8.949463,-1.662979,6.743278,-6.781677,-9.678480,-7.038050],[5.514340,8.240421,-7.135971,-1.229154,-2.485531,2.540366,-6.006318,-9.789354,-1.644234],[7.016310,4.880178,-8.546667,-0.732740,-2.646354,-4.044390,6.081984,-4.070095,-7.936351],[-2.433966,7.820597,1.033017,-8.259371,7.489302,7.642646,-2.568780,6.170480,9.891621],[7.507910,3.793821,-4.656070,-5.302635,6.425407,-9.482942,-9.722142,-0.732351,5.235547],[-0.945321,9.041619,-3.208490,-3.351135,-4.808326,-6.757056,7.292041,8.972170,-5.725853],[-8.139254,8.795590,1.618655,8.106749,3.090815,-0.141514,-5.776580,-8.315868,-3.328730],[-6.940685,-8.075568,-3.079903,-6.405567,-2.364067,-9.231335,2.033379,3.169477,0.441269],[-3.388461,-8.042695,-9.630476,-7.593541,-5.983745,8.185389,-9.336875,9.757505,-0.207557]],[[0.915898,9.615517,-0.425662,-0.800269,-3.038172,-7.660406,0.818734,-1.404951,-3.625601],[-1.922483,4.025642,-0.411484,7.605917,4.417585,3.367612,-9.466626,-2.213940,-1.480411],[-3.299676,9.346427,-8.058801,-8.691004,-9.088981,-2.453239,4.293865,-9.930754,3.013687],[8.485678,0.483830,3.683312,-2.723502,2.235378,2.707997,0.693836,3.894393,-3.300370],[4.136895,3.760012,6.776497,-7.000142,-0.964740,-8.444387,8.412899,-2.250548,-2.767601],[4.307257,4.622975,0.618924,-8.925207,-5.095907,1.269076,-7.224119,5.807835,1.519307],[0.885976,-9.348670,-2.747488,9.470521,-9.205309,-2.868858,5.259535,-9.582763,-1.865664],[0.863412,-2.866654,-5.370862,-8.281345,-6.787757,-9.260297,-3.681588,-6.534003,4.622727],[4.386552,-6.968335,-7.192924,-5.234913,8.511430,6.238645,3.766499,-6.219848,-2.738058],[9.725746,7.526606,7.605619,2.453713,1.984911,-8.084734,-1.023780,7.475526,0.047615],[5.128969,6.152594,-8.460310,8.793188,4.648906,-7.739178,-6.794186,-2.641384,6.358320],[-4.765356,-2.368056,-4.395608,-6.297969,-8.300169,-3.672297,-3.945192,-2.324652,-0.320461],[-6.552524,-7.305428,6.472330,8.806501,-7.534428,-1.746571,6.016172,4.954002,-3.055444],[-9.478195,-9.936503,7.027017,9.650643,8.830988,3.748087,-4.395970,3.210800,-0.250073],[5.506978,-7.712520,1.720911,-9.819109,3.345852,-5.104074,4.081867,8.561853,-8.224938]],[[-7.301350,-1.065158,5.716440,5.461853,0.720015,-3.238847,-5.606972,2.433549,0.829799],[2.397723,-0.302002,9.220647,-3.066834,3.243498,7.166687,-5.481734,9.747010,5.321608],[1.320620,6.657766,2.593607,-0.935643,5.228472,-1.387905,-5.359331,-8.967537,3.804410],[-8.739124,6.704579,5.404154,4.665225,-3.942754,-4.685359,9.427694,7.734313,-1.513777],[-7.010101,-3.574522,-3.017773,-9.243418,-3.859123,8.527825,5.857520,5.243293,-8.973400],[9.760453,7.732297,-5.153782,0.360260,7.884454,-3.736425,3.395899,-4.142464,0.683849],[-5.275967,4.231655,-7.726547,-3.684480,-8.648401,-9.982816,-8.492931,-9.307682,-7.145335],[9.332417,-2.134067,-4.378379,-6.572583,7.051275,3.320075,-6.643867,5.795388,-2.710403],[-5.411518,3.106150,-3.293710,9.749458,6.428577,-8.128691,7.052682,3.347249,-9.388383],[-4.360621,9.170064,6.175850,-9.476387,-7.930021,-6.308850,-2.604679,-5.579604,7.995097],[1.786048,9.209574,6.306464,-9.190612,-4.311442,-7.971056,3.805407,5.688047,8.672455],[3.067874,-5.441946,6.753799,-1.888432,-8.316766,1.905697,-1.057206,-4.046849,9.500867],[2.662306,-6.551612,8.202406,7.925856,-3.032182,6.135652,8.642249,0.575410,-1.267683],[-2.826448,-4.128275,9.272480,8.137220,7.877414,-4.542431,3.816430,-0.484490,9.111783],[-3.445321,9.026594,9.905619,-0.904660,1.077967,3.403943,-1.916759,9.499943,-8.960484]],[[-4.740617,-5.668187,5.682384,-3.674627,-7.181402,6.237850,-6.991680,-4.132335,-5.124437],[-0.363210,3.507061,-1.300723,-3.401545,-2.667374,-2.776764,-4.063966,-8.844642,-2.594695],[1.436675,-2.660987,2.762226,5.366750,-7.890370,7.030191,-5.014992,7.901921,-6.564316],[-0.160479,3.253946,-5.340123,8.981117,-6.656735,0.127785,7.468002,-7.070696,-9.399689],[4.700013,0.023578,-6.458570,-0.189745,1.930830,-8.914937,-7.385402,-4.448771,3.786700],[0.214991,2.741194,7.573039,-4.782571,-7.395530,-7.507755,-2.441104,-4.111449,0.618680],[2.002458,4.940053,-8.711766,-4.994860,-5.640350,-2.796405,5.603820,-4.389903,2.194613],[7.673372,7.392072,-6.283851,-9.240708,7.119574,3.974206,5.642556,1.230485,0.870453],[-5.198445,-7.471993,-5.195188,9.446059,-2.899796,-6.801086,6.455738,5.658029,7.114911],[-8.275020,-4.929404,0.350403,1.114129,-4.129965,8.781498,-0.786661,2.542981,8.596438],[5.205132,3.377018,-7.647814,5.603174,3.397974,-8.812231,6.034867,0.290114,3.886412],[5.995595,8.551150,9.612103,4.509475,2.433104,-9.881081,-9.591473,6.977702,9.607089],[6.221857,8.256950,2.995687,-0.789746,-7.474197,-1.869758,-1.825560,-3.382132,-7.313335],[-7.381911,1.577134,-4.062727,-5.223306,1.486462,2.582878,-0.081904,-0.727863,5.724208],[1.153466,-7.177090,6.828837,3.032067,-5.926236,-2.423774,3.077613,-5.634292,-1.876468]],[[-3.179861,6.861781,-9.354899,-6.328053,7.050797,-0.787799,-0.430148,-7.206755,7.284105],[-2.325732,6.686912,8.713577,5.185234,6.750928,5.943696,-2.815598,-3.136051,-7.184755],[-1.185419,9.754920,4.028515,6.064561,-8.542056,-9.878448,5.651063,-4.737422,9.046308],[-7.873536,1.573297,-8.316923,4.448497,-3.614855,-4.354653,-3.632735,-9.732548,-9.588873],[6.548329,4.298819,-6.130311,-4.742135,-0.733960,-7.510115,-4.065607,-7.566211,-5.364956],[-8.631365,-3.718135,-4.899640,4.918735,6.469587,-0.917624,6.562577,7.609673,4.170384],[-0.922111,-4.417937,6.004181,-8.176270,4.574613,6.754355,3.259058,-5.870210,-9.753930],[-9.413465,3.420772,5.899731,-8.962064,-0.360881,-2.455310,4.235219,6.870689,9.148838],[-8.838627,-8.697152,1.411924,-7.821687,1.566565,-4.589886,0.052877,-8.365495,-1.139609],[-2.561468,-3.717983,2.764596,1.414067,-8.793611,-6.340467,4.307349,1.238335,-2.743553],[7.122785,-1.213719,7.064054,-5.815208,6.317524,-1.270216,8.713629,-8.509522,4.927794],[-5.231043,-1.502599,1.397796,-0.490959,-4.133865,-6.781748,-1.954573,6.434946,-3.253448],[4.002512,5.777294,4.289163,8.784160,-9.082441,2.406124,5.399925,-3.870529,-3.826738],[-5.810964,-9.038158,-9.471955,3.469375,-5.586557,9.710002,-5.962477,-3.678481,-0.333644],[8.438562,-9.328468,4.104906,1.155174,7.868556,6.060346,3.660181,-1.226617,-9.219889]]], dtype = "float32")#candidate|5022|(5, 15, 9)|const|float32
bop_5023 = relay.add(call_5018.astype('uint8'), const_5022.astype('uint8')) # shape=(5, 15, 9)
bop_5026 = relay.add(call_5019.astype('uint8'), const_5022.astype('uint8')) # shape=(5, 15, 9)
output = relay.Tuple([bop_5023,])
output2 = relay.Tuple([bop_5026,])
func_5027 = relay.Function([], output)
mod['func_5027'] = func_5027
mod = relay.transform.InferType()(mod)
mutated_mod['func_5027'] = func_5027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5027_call = mutated_mod.get_global_var('func_5027')
call_5028 = func_5027_call()
output = call_5028
func_5029 = relay.Function([], output)
mutated_mod['func_5029'] = func_5029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mod.get_global_var('func_3429')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_5061 = func_3429_call()
call_5062 = func_3429_call()
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
const_5070 = relay.const([0.365780,-3.027217,8.796992,-2.113590,-8.886899,2.689169,-4.103907,-2.322655,-0.355826,-8.696877,2.707040,-2.981547,0.243877,-3.093718,5.611931,0.213198,6.144790,9.232359,-1.350948,1.725899,-0.383759,1.470268,3.356685,-0.248100,6.303704,-1.373619,9.249128,-2.566274,6.425314,7.687766,-1.397603,7.383452,2.730110,-7.133570,-7.102565,-1.603978,-3.191454,2.981228,-2.744159,6.422936,6.941222,-2.068059,1.327381,4.596360,1.710230,4.225151,-6.044827,7.119857,9.727984,0.123793,2.703536,-8.250357,8.294443,3.323002,3.660973,-2.793694,3.942532,-0.592470,4.143994,0.739482,-6.409900,-4.975823,4.865507,-3.875749,-3.557878,-7.105468,-8.899783,4.324544,-3.171101,2.101192,-5.264680,-8.434775,-1.177584,-7.209857,4.260761,-9.569058,-2.921537,-5.309102,-8.133812,-5.886882,-4.126535], dtype = "float32")#candidate|5070|(81,)|const|float32
call_5069 = relay.TupleGetItem(func_2190_call(relay.reshape(const_5070.astype('float32'), [81,])), 2)
call_5071 = relay.TupleGetItem(func_2193_call(relay.reshape(const_5070.astype('float32'), [81,])), 2)
func_4284_call = mod.get_global_var('func_4284')
func_4285_call = mutated_mod.get_global_var('func_4285')
call_5075 = relay.TupleGetItem(func_4284_call(), 1)
call_5076 = relay.TupleGetItem(func_4285_call(), 1)
output = relay.Tuple([call_5061,call_5069,const_5070,call_5075,])
output2 = relay.Tuple([call_5062,call_5071,const_5070,call_5076,])
func_5077 = relay.Function([], output)
mod['func_5077'] = func_5077
mod = relay.transform.InferType()(mod)
output = func_5077()
func_5078 = relay.Function([], output)
mutated_mod['func_5078'] = func_5078
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5111 = relay.var("var_5111", dtype = "int16", shape = (13, 1, 4))#candidate|5111|(13, 1, 4)|var|int16
var_5112 = relay.var("var_5112", dtype = "int16", shape = (13, 7, 4))#candidate|5112|(13, 7, 4)|var|int16
bop_5113 = relay.add(var_5111.astype('int16'), var_5112.astype('int16')) # shape=(13, 7, 4)
uop_5118 = relay.sqrt(bop_5113.astype('float32')) # shape=(13, 7, 4)
func_978_call = mod.get_global_var('func_978')
func_980_call = mutated_mod.get_global_var('func_980')
var_5122 = relay.var("var_5122", dtype = "float64", shape = (140, 2))#candidate|5122|(140, 2)|var|float64
call_5121 = func_978_call(relay.reshape(var_5122.astype('float64'), [7, 4, 10]))
call_5123 = func_978_call(relay.reshape(var_5122.astype('float64'), [7, 4, 10]))
output = relay.Tuple([uop_5118,call_5121,var_5122,])
output2 = relay.Tuple([uop_5118,call_5123,var_5122,])
func_5132 = relay.Function([var_5111,var_5112,var_5122,], output)
mod['func_5132'] = func_5132
mod = relay.transform.InferType()(mod)
var_5133 = relay.var("var_5133", dtype = "int16", shape = (13, 1, 4))#candidate|5133|(13, 1, 4)|var|int16
var_5134 = relay.var("var_5134", dtype = "int16", shape = (13, 7, 4))#candidate|5134|(13, 7, 4)|var|int16
var_5135 = relay.var("var_5135", dtype = "float64", shape = (140, 2))#candidate|5135|(140, 2)|var|float64
output = func_5132(var_5133,var_5134,var_5135,)
func_5136 = relay.Function([var_5133,var_5134,var_5135,], output)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5149 = relay.var("var_5149", dtype = "float64", shape = (9, 10, 13))#candidate|5149|(9, 10, 13)|var|float64
uop_5150 = relay.sinh(var_5149.astype('float64')) # shape=(9, 10, 13)
bop_5164 = relay.not_equal(uop_5150.astype('bool'), relay.reshape(var_5149.astype('bool'), relay.shape_of(uop_5150))) # shape=(9, 10, 13)
output = relay.Tuple([bop_5164,])
output2 = relay.Tuple([bop_5164,])
func_5168 = relay.Function([var_5149,], output)
mod['func_5168'] = func_5168
mod = relay.transform.InferType()(mod)
mutated_mod['func_5168'] = func_5168
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5169 = relay.var("var_5169", dtype = "float64", shape = (9, 10, 13))#candidate|5169|(9, 10, 13)|var|float64
func_5168_call = mutated_mod.get_global_var('func_5168')
call_5170 = func_5168_call(var_5169)
output = call_5170
func_5171 = relay.Function([var_5169], output)
mutated_mod['func_5171'] = func_5171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_124_call = mod.get_global_var('func_124')
func_125_call = mutated_mod.get_global_var('func_125')
call_5252 = func_124_call()
call_5253 = func_124_call()
const_5275 = relay.const([[[-6.291322,1.153386,9.524523,-3.406826,-3.965519,0.720237,7.674633,-4.245200,-8.480936],[6.518960,1.507220,3.448603,-9.687262,2.189906,-2.112480,-4.421848,-1.218735,1.924865],[7.462482,-8.171459,-3.984624,4.879166,-6.626302,-5.100732,-8.856373,-0.494243,1.913101],[7.227252,-4.219343,5.529674,6.739326,-1.569122,8.994324,9.474556,8.482912,-4.866203],[2.750687,1.796201,7.497693,8.327389,-8.326981,4.206622,3.056083,6.832250,0.136985],[-5.651632,4.414367,4.066424,-7.105327,1.345444,-7.955513,-2.564366,0.215993,7.773647],[3.322093,-9.223004,-9.390960,-5.571897,2.537515,-8.255893,-2.277479,1.298929,0.447351],[-5.929596,-7.876798,5.554716,9.266010,-9.493185,8.507842,1.696286,-4.980461,-8.953146],[6.208298,-6.257128,6.511983,-2.975511,-7.419898,1.693539,-2.960917,5.241293,2.236874],[8.468388,-4.261028,0.288983,0.176099,7.269666,2.156334,-9.346139,-3.811787,1.299142],[7.373802,5.978103,4.170761,2.056044,-0.243274,-1.932418,4.981727,-8.141585,-6.882121],[-2.645205,-5.890480,1.010059,5.049536,-5.185797,4.084050,6.845269,8.196420,-8.331263],[1.184182,-8.340337,-7.459148,6.681779,-8.021856,-8.613338,-0.058480,-1.997139,-1.970292],[-0.330052,-9.963511,9.061264,-5.122670,-9.735935,9.543235,-2.485090,9.345347,-9.448843],[-2.871918,0.528685,4.912835,1.989292,-4.025986,-5.051197,2.307003,0.374648,8.872196]],[[0.310922,2.336733,-9.103605,-7.821925,-1.090614,9.981372,-2.704992,-9.493757,5.544179],[2.648037,9.437853,-5.354603,-7.801898,-3.847787,6.694613,-0.608993,1.480920,8.566501],[-1.646050,1.425340,1.393615,9.822969,-7.996607,3.540750,9.986974,-4.714364,2.077957],[-4.570916,-3.719959,6.158444,-9.389314,7.310658,3.867685,3.577799,-9.363580,-2.827382],[-2.743652,5.285011,-3.094468,-2.922675,1.262145,-5.534985,5.497833,-0.574596,-6.612637],[-3.841142,0.751599,-4.725504,-8.186118,-9.658142,-3.306471,-6.335736,-5.690725,8.934278],[-0.658641,-6.517090,-7.734484,-8.830856,0.819554,-9.515692,-5.731192,6.332708,-6.128992],[5.844242,0.086920,2.969133,-5.846772,-5.385523,-7.842011,0.782898,8.169837,-0.025657],[1.780678,-3.190117,-8.775641,-2.777271,8.722486,-6.234305,1.505694,-2.320186,-6.944060],[0.325972,4.305345,2.591731,4.597822,-7.329283,8.502054,4.533857,-6.991142,7.006192],[-2.796251,5.321959,5.612501,1.237819,9.545648,-9.263422,7.800586,9.469653,9.709849],[-2.905707,1.230013,-2.807371,-1.256704,5.298904,2.235379,4.958490,-1.863161,8.326689],[-2.031591,4.460040,-0.853575,8.459125,4.136908,-7.914239,-1.047576,1.411376,5.527121],[-7.984744,8.519460,-7.139373,-0.730588,-9.863816,1.909487,6.509689,-3.882017,2.672295],[-3.212846,1.201945,7.615229,-1.282198,-7.267275,-3.217712,6.531194,7.901009,-4.275684]],[[4.516643,3.259690,-9.034505,5.288150,4.285561,-6.509056,-3.203132,7.011261,-8.381678],[8.008707,-7.057714,-0.091956,-2.154668,2.564971,8.768673,4.578632,0.854606,-9.383653],[8.614644,9.525598,-7.156539,-3.006571,-4.972333,-1.941531,-0.150246,6.485525,7.279860],[3.034911,-5.655210,-2.060359,3.266067,-4.594744,-3.916537,-0.418100,5.881089,-1.612496],[7.180696,-8.470338,2.359829,-3.164236,5.666377,-2.604191,1.720238,-7.640256,9.361321],[1.541645,-2.675619,3.018211,2.500335,5.411905,3.347262,-1.491903,-8.561088,-9.250291],[3.464545,1.808342,-4.387057,7.494523,-3.317331,7.261370,-4.888076,-5.762591,4.090408],[-5.434498,3.618798,7.914447,0.128114,6.155712,-5.758829,2.380160,-6.365795,-0.514379],[8.814586,-6.849600,8.297592,3.097141,7.488797,4.159869,3.404612,1.092338,6.486050],[1.059582,-2.542353,-8.554215,-7.149321,-1.186764,-2.003217,3.944164,-9.947564,3.572523],[-3.930593,-8.612342,-6.388001,-3.751748,9.478246,-8.482502,-9.307227,5.873623,-9.136249],[3.628113,-6.036397,5.379062,7.544412,-0.213118,1.123745,7.587956,-9.639665,3.672291],[9.515050,-9.998907,1.137818,9.831927,-2.011496,-8.321074,-5.988724,3.829388,2.236806],[-2.395090,0.449794,-4.274349,-8.360518,-3.982874,7.606636,-8.129680,9.865352,9.372200],[3.333770,-0.741447,-0.016736,1.160451,3.643196,1.286241,4.274488,0.526717,-3.806770]],[[9.006271,6.263376,9.897623,8.274392,-4.052081,-2.259606,0.890118,-4.775186,8.583871],[-6.187183,-1.438014,4.074219,-2.584654,9.418146,4.393686,-5.652914,-6.234961,4.984999],[-4.557524,6.437051,5.527467,2.915798,-7.954981,6.418444,-9.572701,-6.021272,7.665364],[-0.299470,-4.479654,0.328205,3.101516,8.943709,9.552549,4.224725,9.179428,-6.349227],[-3.781996,-2.211608,-8.908873,-2.162075,8.106863,0.636726,-9.547168,4.547823,8.357008],[-5.975478,-9.077113,-2.279423,-6.335926,4.343876,3.981037,1.231651,2.603546,-3.900487],[2.055860,-0.100844,0.385863,3.758074,1.330863,-9.201534,5.952628,8.238388,-4.138046],[3.664001,9.526435,3.650796,9.744943,-8.240963,-3.685555,-5.944934,5.795421,-2.785406],[-9.075457,-8.964441,-1.298082,-4.759948,-3.206147,3.829910,6.212514,7.561086,-2.107119],[5.231580,0.956027,-1.645792,-4.083313,8.773714,-3.321594,-8.867635,7.121648,-0.316305],[-8.550440,0.406589,5.096143,9.549557,-2.777094,1.054872,3.125465,-4.201284,7.137516],[-8.074930,1.569704,3.958724,-8.104836,-5.512212,2.744530,7.806001,3.210364,-4.912435],[-9.743791,1.865355,-4.543168,2.910989,-5.488209,8.122904,-7.207538,0.269818,5.822221],[4.504662,9.563016,-1.947899,8.189473,-0.276739,-6.129619,3.786691,-6.854303,2.271192],[6.653299,1.545965,-0.860780,7.144317,-7.842912,-5.657163,-9.821977,1.288183,7.503694]],[[-7.639738,-3.518300,7.085227,9.141155,3.307612,-1.420963,-5.905673,2.196858,5.029547],[-0.091213,-2.088782,3.817499,4.341592,3.259404,8.837685,-8.743091,8.332218,-5.259851],[5.444167,3.463581,-3.883438,-0.291505,7.346900,-2.877759,1.104392,-5.589065,2.039742],[0.850720,1.983815,-3.039160,1.551539,-8.965764,0.608665,-6.600470,-1.427584,3.119309],[3.611588,4.934080,7.034018,8.278218,4.694884,-6.000711,0.180932,0.839450,-2.099736],[-2.432821,-1.714125,-4.517333,4.422403,-1.066924,-0.726828,-6.639759,3.058181,9.466610],[2.228727,-3.887563,-9.472434,-0.584172,-3.457844,-2.685577,1.955858,-5.198635,0.441007],[9.986815,1.115623,-2.254044,2.185071,1.557814,-1.964880,2.250006,8.242314,-4.612208],[-0.648681,-5.105905,-4.159595,-0.705292,8.818109,0.541579,1.673856,8.456134,4.124135],[7.776157,3.639252,6.926130,6.662286,7.048185,-2.841421,-3.985107,-6.240813,3.377483],[0.942379,-5.903008,0.268750,4.020095,-7.690070,8.412797,-8.241902,-1.763786,-5.472583],[4.317331,-9.543310,-6.479348,9.840257,-3.213146,0.555077,-6.001344,2.841625,2.333178],[4.760937,9.065511,-4.806400,8.320775,1.263706,-8.082972,8.129089,7.766067,-7.094178],[3.450744,-8.961848,-8.240740,3.752015,-0.058784,5.326880,1.264075,-1.498999,7.010240],[-7.271149,8.826730,-3.019788,1.105588,-0.661686,-8.303054,-0.195854,-6.786183,0.887692]],[[3.995893,8.349823,7.331557,5.522367,6.467194,9.334257,-5.959128,1.322120,-1.709660],[3.412755,-0.847862,-6.562482,4.419699,-4.333643,-5.623474,-5.557333,-6.406881,8.341504],[-6.896535,8.254150,5.325809,-7.961576,-1.391933,0.549956,-0.653874,-6.835027,-2.126501],[5.109234,6.119351,4.484091,3.369320,4.475654,-3.706158,9.111925,-4.123240,-8.568661],[4.750016,4.662327,8.407608,-2.827833,-8.702073,-9.680727,-2.943728,-4.037097,4.784518],[1.561570,8.884220,-8.176436,9.738835,-3.113002,-2.271490,9.099825,-1.868275,2.270092],[-7.011404,0.252190,-3.373807,5.086695,7.982206,5.104677,-7.786017,3.504883,2.521433],[2.769383,9.104089,-2.090882,-0.427106,1.978369,0.936886,-0.265739,3.766691,-4.491349],[2.741179,-0.867023,9.690683,4.257829,-5.892277,2.497304,4.615770,-8.174755,-6.252556],[-7.558655,8.700440,0.949050,9.969005,-2.594313,8.768115,-1.580099,-4.713348,4.512275],[-6.032082,8.258634,5.915794,8.538844,7.584102,2.075582,-2.029062,4.052300,-7.304680],[-7.342316,-1.052856,-4.072702,6.935975,7.857389,4.448670,8.515514,5.727820,-2.745912],[4.306870,8.028486,6.032026,8.643907,9.301044,4.091302,6.682250,8.309590,-4.026682],[-4.486114,-1.526845,-3.009357,-6.578748,-6.817024,-7.132824,9.397624,-6.678687,6.676446],[5.544605,7.522625,6.475189,-7.750056,5.207292,-2.793048,7.755549,0.301982,-1.160331]],[[6.388450,-8.642783,7.648261,-8.184487,-6.536114,0.751744,9.917862,-8.726976,3.070937],[5.330160,9.527152,1.838416,2.357197,-0.519779,5.115331,-5.896840,4.190606,-9.564327],[1.773111,1.229386,3.445917,3.553497,-3.702447,8.043694,5.315992,8.482849,1.053356],[7.555067,-1.272241,-1.981639,-6.137039,-9.979176,6.408971,-5.611673,-3.059503,-5.166559],[7.429729,-3.002854,-6.637017,0.955606,-1.363911,-3.193701,-2.982633,-0.086170,4.826523],[-8.018315,1.962411,8.831891,3.965934,-1.647406,-4.771304,9.439926,-0.129543,2.929430],[1.018104,2.049852,6.585814,-7.119694,0.312882,-2.372819,2.222962,-8.194897,-0.955721],[1.572286,-7.411045,5.453672,-2.058743,-0.192331,-3.029263,8.434938,-4.895633,7.858062],[-9.449735,3.578845,0.959473,-3.190994,-5.108876,7.638236,5.613769,-3.311751,-0.644856],[-0.309807,-4.630148,-4.603303,-6.148015,3.858037,-2.708466,-4.953236,-2.034826,-5.483722],[-7.466057,-9.144988,3.963949,7.459798,-3.227425,-5.549016,8.638152,6.230930,3.696162],[-9.754608,-5.132785,4.801277,-0.133870,7.938038,6.930336,-1.637928,4.147280,2.782650],[0.703522,2.810932,-4.674337,-2.475429,-7.225805,-9.404246,9.424026,8.122889,-8.044821],[-5.975264,-5.488582,9.480058,8.920551,9.702600,-1.078964,-0.058115,9.105327,6.187072],[0.936737,4.932779,5.239679,-2.152612,-0.779222,-8.321925,-8.391993,-2.273623,5.144205]],[[-6.367451,6.497293,0.970098,-4.241713,0.702881,0.259007,-0.686776,6.262769,-1.522271],[1.649044,2.032084,-4.448860,-1.604841,9.838604,4.188318,-8.303560,1.113348,-8.353666],[4.529711,-7.479483,-3.937257,7.795968,6.882383,6.073191,1.562236,-8.771070,-5.696954],[8.287564,3.259906,4.046218,5.477726,-7.825155,-5.766420,1.483145,-9.395579,-4.266328],[4.792926,8.468899,-1.006940,-5.612105,3.300364,6.678784,5.729378,-3.464797,4.468544],[3.671043,5.759315,5.571078,-5.764461,9.601723,0.236646,-0.044510,9.429952,5.704919],[-6.901388,9.717925,-1.584974,3.152270,4.989715,-5.588731,-5.565133,5.686034,3.087151],[6.518766,7.613145,-7.970933,-0.817801,3.367336,-9.540837,-6.130942,-2.967756,-9.504889],[-6.450742,-7.970934,3.777120,-4.425676,7.812345,3.923105,-2.071766,-4.971705,5.973416],[-2.960696,3.505218,8.298340,-5.509188,-7.790100,-6.111292,9.192794,3.338939,-3.291923],[-6.598547,-3.632792,6.820232,6.302140,-2.827763,8.506613,-1.572161,5.394414,-9.513822],[-4.840752,-2.093613,4.052563,6.067085,8.104567,2.044231,-9.629856,-5.354026,6.639503],[-7.260004,-0.856348,-9.094885,8.646451,5.719556,3.478829,0.072429,6.579705,-7.892577],[-6.993771,7.710217,-2.100173,-9.021633,5.953015,6.494253,-2.924130,6.025944,-3.035588],[-0.804195,-6.894365,2.187933,5.211161,9.597523,-3.670488,-2.437907,-9.171566,7.682966]]], dtype = "float32")#candidate|5275|(8, 15, 9)|const|float32
bop_5276 = relay.left_shift(call_5252.astype('int32'), const_5275.astype('int32')) # shape=(8, 15, 9)
bop_5279 = relay.left_shift(call_5253.astype('int32'), const_5275.astype('int32')) # shape=(8, 15, 9)
output = relay.Tuple([bop_5276,])
output2 = relay.Tuple([bop_5279,])
func_5288 = relay.Function([], output)
mod['func_5288'] = func_5288
mod = relay.transform.InferType()(mod)
mutated_mod['func_5288'] = func_5288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5288_call = mutated_mod.get_global_var('func_5288')
call_5289 = func_5288_call()
output = call_5289
func_5290 = relay.Function([], output)
mutated_mod['func_5290'] = func_5290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2118_call = mod.get_global_var('func_2118')
func_2119_call = mutated_mod.get_global_var('func_2119')
call_5313 = func_2118_call()
call_5314 = func_2118_call()
var_5326 = relay.var("var_5326", dtype = "float32", shape = (9, 15, 9))#candidate|5326|(9, 15, 9)|var|float32
bop_5327 = relay.right_shift(call_5313.astype('uint16'), var_5326.astype('uint16')) # shape=(9, 15, 9)
bop_5330 = relay.right_shift(call_5314.astype('uint16'), var_5326.astype('uint16')) # shape=(9, 15, 9)
func_4407_call = mod.get_global_var('func_4407')
func_4409_call = mutated_mod.get_global_var('func_4409')
call_5336 = func_4407_call()
call_5337 = func_4407_call()
output = relay.Tuple([bop_5327,call_5336,])
output2 = relay.Tuple([bop_5330,call_5337,])
func_5345 = relay.Function([var_5326,], output)
mod['func_5345'] = func_5345
mod = relay.transform.InferType()(mod)
mutated_mod['func_5345'] = func_5345
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5346 = relay.var("var_5346", dtype = "float32", shape = (9, 15, 9))#candidate|5346|(9, 15, 9)|var|float32
func_5345_call = mutated_mod.get_global_var('func_5345')
call_5347 = func_5345_call(var_5346)
output = call_5347
func_5348 = relay.Function([var_5346], output)
mutated_mod['func_5348'] = func_5348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4921_call = mod.get_global_var('func_4921')
func_4923_call = mutated_mod.get_global_var('func_4923')
call_5373 = func_4921_call()
call_5374 = func_4921_call()
func_3935_call = mod.get_global_var('func_3935')
func_3938_call = mutated_mod.get_global_var('func_3938')
const_5399 = relay.const([[-1.894188,1.258951,-1.100548,5.871676,7.005127,-5.984008,5.018091,3.865623,-7.446792],[-6.559248,2.342669,7.852364,-1.582407,-5.129157,-8.918080,1.590208,-9.514341,5.498790],[0.668877,1.606506,-5.529407,-4.393145,2.366718,2.958154,8.638025,3.526085,-9.732715],[7.338242,-3.424171,5.129910,-5.949101,9.216606,5.727410,2.908174,6.490682,7.478817],[-3.874055,9.679488,-6.112055,-8.018404,8.412135,-0.504029,-2.406787,-2.090244,4.490638],[2.910606,-9.848633,3.961266,7.923304,0.139493,0.032401,-3.181220,-6.027289,-5.845451],[9.135171,-7.777403,-9.658862,-5.409598,7.126109,4.251474,-8.640993,-0.019303,7.657082],[-0.112013,1.089127,-8.054815,-3.679588,-1.141405,-0.988174,4.255377,3.536610,-7.753861],[6.134648,-7.338193,-6.380736,1.630750,-3.084232,8.429151,8.400799,1.518359,7.158336]], dtype = "float32")#candidate|5399|(9, 9)|const|float32
call_5398 = relay.TupleGetItem(func_3935_call(relay.reshape(const_5399.astype('float32'), [81,])), 0)
call_5400 = relay.TupleGetItem(func_3938_call(relay.reshape(const_5399.astype('float32'), [81,])), 0)
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
call_5401 = relay.TupleGetItem(func_2190_call(relay.reshape(const_5399.astype('float32'), [81,])), 0)
call_5402 = relay.TupleGetItem(func_2193_call(relay.reshape(const_5399.astype('float32'), [81,])), 0)
var_5418 = relay.var("var_5418", dtype = "float64", shape = (504,))#candidate|5418|(504,)|var|float64
bop_5419 = relay.floor_divide(call_5398.astype('float32'), relay.reshape(var_5418.astype('float32'), relay.shape_of(call_5398))) # shape=(504,)
bop_5422 = relay.floor_divide(call_5400.astype('float32'), relay.reshape(var_5418.astype('float32'), relay.shape_of(call_5400))) # shape=(504,)
output = relay.Tuple([call_5373,const_5399,call_5401,bop_5419,])
output2 = relay.Tuple([call_5374,const_5399,call_5402,bop_5422,])
func_5426 = relay.Function([var_5418,], output)
mod['func_5426'] = func_5426
mod = relay.transform.InferType()(mod)
var_5427 = relay.var("var_5427", dtype = "float64", shape = (504,))#candidate|5427|(504,)|var|float64
output = func_5426(var_5427)
func_5428 = relay.Function([var_5427], output)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4101_call = mod.get_global_var('func_4101')
func_4103_call = mutated_mod.get_global_var('func_4103')
call_5436 = relay.TupleGetItem(func_4101_call(), 0)
call_5437 = relay.TupleGetItem(func_4103_call(), 0)
func_4921_call = mod.get_global_var('func_4921')
func_4923_call = mutated_mod.get_global_var('func_4923')
call_5450 = func_4921_call()
call_5451 = func_4921_call()
func_665_call = mod.get_global_var('func_665')
func_668_call = mutated_mod.get_global_var('func_668')
const_5471 = relay.const([-8.628650,0.771180,5.010889,6.217371,5.950201,-7.212141,-2.628537,3.404370,2.551324,-7.258089,9.325709,7.444696,-5.469322,4.522364,-8.083423,3.281969,-2.093783,8.736251,-3.855717,-5.181938,4.591047,-8.284398,-2.493690,7.124888,3.052627,-6.023988,-5.475597,3.391113,-4.397761,-2.312272,7.100873,0.829183,-5.789954,9.775613,5.752455,-4.481033,-4.028992,5.881853,4.422632,-6.654198,-4.280044,8.787437,-8.682515,4.296294,-9.314716,5.335614,-0.763256,8.848001,6.981257,7.753124,-8.598035,9.735631,0.761746,5.175101,5.951016,0.636318,7.512307,-2.430770,7.025173,-8.073586,8.057619,3.825295,-4.955312,2.297532,5.937833,-4.831149,-3.539797,-3.850303,-9.866070,-0.316055,6.307448,2.469004,7.347887,-4.549345,-1.397276,-5.182662,-1.283409,2.358948,-6.089260,-2.721042,3.348214,1.027596,-1.330430,0.994736,1.691024,7.773662,-5.844975,1.108040,-2.556982,-9.060287,-5.521474,9.013863,5.333827,3.348687,7.436120,5.362790,1.217591,-4.562181,7.930461,-0.570731,-7.089046,7.382808,7.050516,-0.297889,1.338882,-8.469567,6.730697,-3.523502,-4.891815,-4.190453,-2.582209,-4.080834,-2.806257,6.494737,0.366433,-6.728976,0.471036,-2.391892,7.870812,0.786335,7.570633,-3.127429,6.250679,8.657577,8.235764,5.744011,-6.513332,9.248325,-0.511359,-2.410110,-8.037389,5.902744,-5.981273,-7.054238,-4.939499,-1.395410,7.077746,-7.279469,-6.049193,-4.221383,6.318318,7.407179,-0.845557,-3.175879,1.491168,-6.550782,-6.261833,-0.604989,1.697478,-4.398168,-3.662959,7.149027,6.899173,-9.781788,-1.783679,8.655637,-0.583304,4.715145,7.007158,8.083430,-1.048939,8.164801,-4.311159,1.982707,-9.348015,7.800259,8.733738,1.049371,6.487379,-4.838817,-8.588200,4.913330,-0.793512,6.093897,8.951294,-1.865132,-7.160758,-7.962606,6.884110,-5.220793,3.273351,-2.432537,4.933698,9.229156,0.656383,-7.252697,-8.057629,-3.191948,-5.163399,-0.116522,6.597296,6.972680,-4.148691,-3.027805,0.229658,-0.854123,-4.151108,1.400129,-8.574474,-5.834803,-8.058629,6.468145,8.904416,7.658504,-3.411436,6.625168,0.626676,5.456094,-4.946649,1.933317,1.965554,-4.776647,9.841816,0.561414,-8.779751,6.578790,-7.881215,0.905545,2.298371,3.273406,4.956510,2.023687,9.246571,-2.562470,-2.594908,0.899166,6.141000,5.006970,-3.632929,-2.258672,8.387700,3.604140,3.845580,0.866308,-6.507024,-7.130371,0.639326,-1.061195,-4.798974,-4.636189,-0.270459,-3.945951,4.737879,-1.505702,-7.193992,-7.019206,8.167217,8.000128,8.767964,8.275215,5.839165,7.163728,4.344992,3.493213,-7.620086,-0.357490,-8.017039,7.182686,-6.181800,2.946291,-2.480063,-0.075053,6.236785,-8.357970,-9.849363,-0.002789,1.382784,-9.921931,3.969565,3.943611,6.147941,1.494117,-8.642691,0.071430,-6.789170,-5.965743,4.094603,-3.348415,-2.373009,2.398012,-8.925455,2.861569,4.287498,-4.078703,6.906781,-0.840393,7.562526,-5.314428,-6.821616,4.339444,-4.960853,-3.997956,-9.399260,0.680584,5.562188,-0.344054,-2.532181,-9.719986,6.306122,7.848812,-2.827128,-2.201165,9.124427,8.220366,-3.902344,-8.734404,-3.373370,-7.521127,-5.728606,-7.435603,-7.368891,7.737562,-4.318302,-3.927480,5.218075,-6.583866,-6.693998,8.313209,-0.956744,3.435464,1.248199,3.378494,-5.195599,5.373303,7.676391,6.435634,-6.419171,4.520008,-0.845798,-8.218372,3.451128,3.320726,2.842808,2.032495,5.509570,1.654057,-1.525300,1.890672,-1.871227,9.452687,-5.320113,-0.257291,-4.802188,1.487083,2.190766,-3.639761,-6.214343,-5.646314,-0.960611,4.700462,5.276267,8.427854,-9.731474,-8.489838,0.279817,-4.478425,-4.121748,-0.646081,-6.986455,7.237340,0.939613,-3.889459,5.504816,-1.909658,-5.687296,-4.683986,-2.519633,-4.374316,-1.562484,8.212715,-3.157849,6.403742,-7.258461,2.996436,5.116737,7.119626,-9.386867,-0.598080,-1.638728,-0.551366,8.606745,-8.122621,-7.104596,-3.388851,-6.276350,-4.001328,1.386110,1.292071,0.174795,6.965288,-0.773087,3.447699,-5.850239,-5.950792,-1.563985,-3.517649,7.177337,8.311949,6.333675,-6.388506,-0.155807,-4.441216,-9.061274,2.346411,4.293102,-3.020384,1.028996,-1.531047,-7.291205,9.416283,5.643718,-6.011962,-6.757983,-3.853132,4.502884,5.818751,6.177219,7.523181,-0.891222,8.125512,7.757822,2.170000,-9.992048,4.797835,-5.450953,7.146406,-9.250891,7.183528,-4.096069,-7.813325,-0.801600,7.495221,3.214394,-6.434492,7.421669,3.066612,2.432839,-6.801377,7.969545,-3.262742,-2.477132,3.276488,1.439190,4.294714,1.736454,2.616376,-3.768895,1.713462,-5.357838,3.218799,-3.138675,-3.079179,7.057231,7.754579,-6.486842,-8.786073,0.666073,3.927817,-0.677930,-1.312028,-5.391859,-1.481150,-1.590300,0.681502,1.307000,8.280391,5.767250,9.053078,-0.450706,4.148137,0.126068,5.668109,-1.004447,1.040284,6.035108,-8.335150,-3.949297,-5.242733,-8.430815,5.361960,-2.348661,2.880171,-6.869963,-9.656671,1.797338,-0.459577,-5.878255,-8.342980,-4.621808,1.191829,8.258577,-1.535683,-7.517539,0.821533,-6.122409,-7.060654,3.849590,-9.103321,1.188935,-6.167292,6.038433,9.921540,-9.869935,-7.675257,3.773205,-1.100389,4.306275,-2.937473,-6.708501,-9.020463,-4.300979,3.767908,6.282175,-2.789772,6.375997,9.982998,6.152827,-7.888005,-2.291278,-6.754373,-0.391459,8.673735,1.057556,-1.476929,0.878464,-7.163663,6.547854,0.745361,-4.462872,0.361437,-1.095557,-6.054132,8.547123,5.810604,1.358633,-2.910114,-0.280945,8.825224,8.389418,1.853463,-9.582268,4.089308,-5.947789,-9.665297,-7.286846,-0.434424,1.478501,-4.487433,5.579563,-0.059899,3.368607,-4.401522,-3.889376,-5.615287,1.287951,-1.159627,1.337434,-4.217593,-5.128024,-3.596195,-2.627662,8.779449,8.096436,4.333625,1.749318,4.978768,-1.571010,7.317474,3.320392,-8.160787,9.520322,6.322694,-5.737793,-3.765167,-9.116756,8.373795,4.257739,-7.409032,-6.157212,2.904090,-1.514920,8.220323,0.590610,5.807699,-9.810252,2.833126,4.606518,-5.354351,-3.479317,-4.207213,-6.962766,-3.265877,9.356372,-9.545434,-3.454133,2.160820,0.220622,7.003076,3.151158,9.633185,-7.244394,-7.368367,4.311613,-5.962307,0.744377,3.865606,-7.210344,-4.056753,-8.758706,-1.866333,-3.471303,5.512772,-0.480216,-2.260641,-2.997135,4.937358,8.398568,-3.812270,-0.108414,-9.168377,8.300708,6.363124,1.541441,2.554017,1.566672,-5.836909,-9.109832,0.258648,-5.842031,-4.079641,7.614153,-0.254557,7.045399,-7.350860,6.548300,-0.249041,-1.988794,-5.141007,3.059817,0.395672,9.592342,-5.500416,-3.461325,-1.154802,-6.685485,3.311381,-4.157364,-9.221007,-0.629067,-3.047297,6.985217,-7.672013,-4.266382,-7.069933,0.307172,-6.199171,6.968236,-1.202631,-9.703592,7.667287,9.371618,3.507274,-0.166550,-0.316594,-9.330910,-6.628037,8.265712,1.345615,4.191832,5.806144,9.531528,-9.392970,-6.836407,-9.785448,8.103710,4.896339,-8.593956,4.410925,-1.695516,9.476703,-6.806360,3.690556,0.620788,9.813160,-4.847638,7.841755,1.721937,-2.403696,-1.837707,-1.917535,-7.669620,-8.917938,-9.171987,2.903054,1.100507,7.851586,-1.376861,1.845606,4.478820,6.782661,2.365621,-3.572568,-2.552002,3.001793,8.462861,-9.213164,8.401732,9.221555,-0.999152,3.328911,1.886732,9.964094,3.264513,1.181490,-4.072692,-2.076308,0.178395,-9.546572,7.886985,-5.366473,4.984017,2.008127,-4.835154,9.317575,5.196539,-8.469242,3.882276,9.398348,5.795725,-3.185101,4.037168,4.626224,5.196683,-6.882380,1.885360,2.981782,6.642544,-3.013885,0.897092,4.442161,-9.218942,-4.855384,2.867707,-8.061399,-1.236810,-8.642042,0.821057,6.446299,7.224897,6.319761,-9.291788,-5.304824,6.649732,0.400114,-2.686079,-3.298949,7.150189,-8.968446,-6.197714,1.605445,8.780225,-0.526858,6.035691,6.379160,6.249491,-3.608749,-8.442206,7.895815,9.322306,-6.168378,6.873544,-1.827603,9.311935,-2.049784,6.597932,6.776666,8.915410,0.765638,6.973650,-8.568256,5.198930,-2.541451,1.722683,-7.870466,3.925896,-8.061634,7.620213,9.420067,5.062361,-8.959926,5.638117,-0.718191,7.585414,2.922189,-7.214104,7.826470,-9.629210,7.911608,0.038366,-7.676063,2.816748,-1.957356,2.466852,1.941839,3.782273,1.762359,6.137904,7.771507,9.469105,9.986014,-5.554694,-5.647595,6.172022,-8.997676,1.347748,6.392107,8.706864,4.805065,1.971252,-0.084720,-5.955695,9.920867,2.650833,-3.484588,8.435037,-4.415291,-9.394709,4.247585,4.419545,-8.100526,-7.631176,2.904628,2.290576,1.130749,2.858124,1.056988,5.391395,-6.581171,-6.931694,-2.553344,-3.349107,3.979477,0.491130,-6.310414,2.730714,2.225384,-7.065757,1.471234,7.547248,-8.469680,-8.534965,-6.960015,-1.133611,-9.705179,1.739103,5.885308,-2.032736,-1.731891,0.684913,-3.430611,2.841901,-4.622757,-3.269122,-5.830865,-6.070228,-9.784175,-1.532279,5.761594,3.146199,1.575183,-1.984796,6.136891,-1.989284,-2.358027,-7.177697,-9.772375,-9.008323,-6.201513,-7.999744,-5.590179,5.197210,-5.256059,8.784793,7.148029,0.222648,5.238118,6.635380,-0.618221,-8.977515,8.749513,6.865122,-7.935257,-2.535815,-1.740324,0.267701,-8.284716,-8.435238,0.293649,-1.786715,-8.160614,9.814187,0.212894,-3.666734,-9.454809,-9.101348,-2.039718,2.806277,9.620255,8.362752,8.528948,-7.949093,4.892775,-7.147764,-6.575408,4.624816,-3.256271,-7.182847,7.642739,-1.330752,3.865874,0.424649,-2.863146,-2.175456,4.712519,-1.739555,3.611151,-8.705876,3.340797,1.439636,7.369782,-1.749379,6.988576,5.125548,-9.334874,0.280589,-3.107278,0.430235,4.444559,-2.444926,3.808776,0.773545,5.851573,7.924318,-9.049813,-3.475511,-6.955379,-3.717566,9.650064,-0.512315,1.574358,1.139661,5.767948,-6.632328,-1.311396,8.123733,2.664192,-7.972248,-9.587498,1.095130,-9.645704,-2.962471,0.532979,4.564248,-0.175122,-3.342941,9.036311,8.415730,-9.659487,5.215536,-6.890130,-6.503462,-0.963002,-8.138994,-3.722123,6.693389,1.332738,4.921764,-9.209554,1.458752,6.651012,-9.541359,0.591248,4.750668,-2.718832,-8.972149,6.768279,-9.730413,-9.992272,-9.270375,5.311869,8.781068,3.980146,0.420923,6.124634,-5.272496,-1.195318,9.927181,-8.093463,7.828572,-5.988643,9.373084,-6.334839,0.677898,-6.432163,5.414608,4.799304,-1.874292,-5.128354,2.331720,-6.968506,-4.275882,-1.952967,-7.846678,-1.730725,3.276292,5.631372,-1.452664,1.719422,-2.154102,6.334141,1.898965,5.728361,5.876337,8.561635,6.722815,-8.951516,-6.134700,-8.349511,4.452995,-5.498294,8.140003,8.340125,3.972096,5.404400,-3.847453,9.480033,2.336197,3.807692,-9.773742,0.579311,-1.030253,0.734102,6.560764,2.704732,-0.475424,8.174494,7.089804,6.115824,3.891206,4.754528,8.765893,5.078355,0.624645,3.390977,2.494873,5.201225,-4.705489,-0.321881,-3.800116,-0.065596,7.719199,-4.181175,-6.532724,1.872069,-8.772377,9.516758,-1.748389,3.460675,2.482711,9.878146,0.503492,-8.993024,-2.424021,9.903840,-2.086636,6.997837,-3.751132,0.530339,-2.486580,-4.274279,5.370990,-6.092286,1.223677,2.327679,9.601461,7.116889,7.298423,-0.192260,3.335988,4.039122,-1.487912,1.915207,-3.951646,2.343868,-2.106102,-5.225560,-0.689065,7.553945,-3.776464,-1.687920,3.259347,-3.932940,-6.443624,-3.448189,0.407444,9.416691,2.518205,-0.308721,3.077671,-8.489950,8.753140,0.697791,2.720433,5.298676,9.717119,8.698897,-5.076828,-1.030652,4.426925,-1.268015,-7.974460,-0.967183,-6.059706,0.465295,-4.199342,2.791455,-1.239200,0.518516,1.679461,1.911190,1.742192,-5.037267,5.442121,-5.815365,5.449025,2.783859,-8.386173,6.658440,-4.584120,8.265272,-3.010254,-1.197558,0.865331,9.252006,0.314581,-1.737806,0.221363,-8.585604,9.118659,5.092544,4.336242,-6.758795,-0.175764,-6.451070,-1.818332,-6.892206,9.538662,-2.483817,-1.954759,4.975488,-6.569792,-7.505674,-1.661067,-0.625602,6.333011,9.651263,-1.969247,0.705787,5.390088,4.468316,0.773075,4.291378,9.346255,5.814373,0.954906,5.573977,-1.732450,5.538707,-1.821544,-9.945426,-2.038965,-5.239753,7.799540,7.047357,5.319677,9.732414,-7.439318,3.571241,-0.318392,-8.470058,-0.776690,4.060271,1.589465,1.373041,2.891772,-9.344583,4.930624,-6.438466,-9.645326,-6.384840,3.429456,-7.804068,-0.131702,2.805735,-3.294570,-9.552942,0.362007,-7.504445,-7.665884,-4.548140,5.106923,6.004959,9.048367,-2.449173,-5.448283,2.323072,-2.730105,2.092738,-4.072510,9.311203,-9.547288,8.834867,3.578419,8.370305,4.056065,0.178412,-5.339816,-1.121274,6.406877,2.241026,6.573579,7.563890,-9.361110,-1.288036,6.721026,3.983181,0.623834,6.703597,-9.005743,-6.376436,-0.130178,0.780040,4.462197,-6.096223,-8.948326,-6.791288,-8.869482,8.441999,-7.345640,6.406412,9.205449,-0.282156,7.887515,2.192864,-8.926119,-2.546952,-6.121638,8.810727,9.221498,-6.423581,3.446353,6.912359,-4.599974,-3.651816,-1.922221,-1.100324,-6.923751,-5.037091,-6.041207,-8.568821,5.062228,5.259182,-6.302983,3.777880,-1.473771,9.079688,-4.858282,8.848155,4.048448,-7.663845,-0.521515,2.408276,3.137819,-9.615196,3.895916,-4.201139,5.282202,-3.193626,-5.798651,4.035183,0.688931,-5.265230,2.325524,-2.507364,8.886460,-0.960250,9.399117,-0.220972,4.558406,-9.754556,4.078971,-7.066076,-7.988828,-0.517214,-6.633399,1.593311,-5.644822,-8.849716,-5.886072,-4.502489,2.347935,0.709466,-9.003572,1.258896,-3.350191,7.370298,-1.474593,1.793089,-5.870794,3.033304,8.946967,0.721167,-0.571520,-0.191518,-0.123448,-3.013655,9.071554,7.916471,9.560319,-6.176101,-6.673813,-1.271976,9.231003,-9.966701,3.290628,-7.821256,-6.268925,4.311353,5.656499,4.041254,-6.745664,2.275483,6.107380,-8.576520,7.573027,3.956741,-1.182605,-7.080983,6.003482,8.236547,-3.744335,4.650222,9.514530,5.022258,-1.127668,3.275898,-6.183639,9.199304,6.781866,5.376386,-1.110556,-0.950138,-7.847184,-3.604625,0.720020,-7.187437,8.024381,7.172890,-2.318106,-2.174641,2.988801,-9.745018,-6.537634,-0.514836,8.915960,0.345385,-7.515221,-0.858596,-9.310779,-9.148279,-9.883730,-9.003002,-5.647080,9.118225,-9.607217,-0.545111,3.254301,-2.554092,-6.464475,3.667726,-1.244147,7.541722,-1.010277,0.222465,-4.936429,2.018405,-6.785049,-3.607792,5.848316,-3.299573,1.259901,6.624935,3.768627,9.729631,-3.724578,3.184562,9.341668,6.524697,-8.905748,-1.734968,-9.557592,6.294927,7.940606,-4.808561,1.543797,2.910574,6.641789,2.623107,-0.330854,-4.377210,9.219619,3.589270,-2.386333,5.688446,1.551551,5.762957,1.257066,-1.969017,-5.601383,9.664905,9.585299,2.168651,2.084839,3.334666,2.888217,5.449647,9.157581,8.681061,3.736037,-2.460117,-0.748235,2.980945,0.286604,5.106527,-1.014123,0.393501,6.775383,-7.189091,-1.262509,-8.725942,2.833843,-9.261631,-1.849253,-0.213269,-5.842237,-2.647217,-0.147321,-8.115695,3.937022,2.750073,-1.056356,-8.786597,8.945992,3.880332,-8.461446,9.063676,8.730022,0.561073,3.654631,9.449865,-8.799313,0.635385,8.202007,-8.806841,1.996525,-4.391893,0.174859,8.732639,6.510819,-3.772355,-2.666421,4.363893,2.014879,6.226276,-8.506536,7.255337,-7.240060,0.956018,-0.281001,-2.528906,-7.055457,-7.666506,0.830190,-1.699999,-5.301818,0.078423,0.455264,-6.927343,6.158462,6.339908,-0.022945,-4.132625,2.550872,9.578601,-8.685372,7.738778,-6.477659,-3.935018,5.312994,8.767317,5.123806,-4.042917,0.602584,6.219441,-2.802055,2.436502,7.750921,1.147599,8.852337,2.286619,8.736794,-0.248303,-1.445296,4.537744,-7.826744,1.785075,5.865389,-4.854363,-6.758026,7.588166,-8.170824,1.238541,3.080394,0.674343,0.014842,-4.543971,9.350459,7.539659,6.567753,-6.390228,8.181621,7.756727,8.927393,4.238011,1.424373,8.386035,6.882170,-7.296959,5.882791,-4.458276,-1.237538,5.885404,4.612337,8.045593,-5.840429,-8.361983,0.597949,-7.921669,6.076588,-8.740599,5.458046,1.394956,-7.942394,6.665226,1.356076,9.216354,-1.725411,3.946762,1.298381,-6.631150,-1.448496,1.501577,-3.156777,2.741769,7.195859,-6.648696,7.455905,-4.588433,6.990147,0.161031,4.226451,-0.504866,-5.339082,0.248008,-4.762379,9.068326,9.249149,-5.077605,-9.733547,3.830375,6.706075,-8.721602,6.121187,4.136367,-3.519654,3.267921,0.918116,8.308766,-5.654207,3.209848,-2.348904,2.207839,8.094765,8.189576,2.520716,5.550373,9.070972,9.061983,-4.676924,5.589275,-5.025821,-6.615218,4.767896,1.586914,8.235923,-4.976250,3.823741,6.404490,-6.871075,-3.355974], dtype = "float32")#candidate|5471|(1620,)|const|float32
call_5470 = relay.TupleGetItem(func_665_call(relay.reshape(const_5471.astype('float32'), [12, 15, 9])), 2)
call_5472 = relay.TupleGetItem(func_668_call(relay.reshape(const_5471.astype('float32'), [12, 15, 9])), 2)
output = relay.Tuple([call_5436,call_5450,call_5470,const_5471,])
output2 = relay.Tuple([call_5437,call_5451,call_5472,const_5471,])
func_5480 = relay.Function([], output)
mod['func_5480'] = func_5480
mod = relay.transform.InferType()(mod)
mutated_mod['func_5480'] = func_5480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5480_call = mutated_mod.get_global_var('func_5480')
call_5481 = func_5480_call()
output = call_5481
func_5482 = relay.Function([], output)
mutated_mod['func_5482'] = func_5482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1007_call = mod.get_global_var('func_1007')
func_1008_call = mutated_mod.get_global_var('func_1008')
call_5483 = func_1007_call()
call_5484 = func_1007_call()
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_5487 = relay.TupleGetItem(func_2356_call(), 0)
call_5488 = relay.TupleGetItem(func_2358_call(), 0)
bop_5497 = relay.power(call_5483.astype('float64'), relay.reshape(call_5487.astype('float64'), relay.shape_of(call_5483))) # shape=(1, 15, 9)
bop_5500 = relay.power(call_5484.astype('float64'), relay.reshape(call_5488.astype('float64'), relay.shape_of(call_5484))) # shape=(1, 15, 9)
output = bop_5497
output2 = bop_5500
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
