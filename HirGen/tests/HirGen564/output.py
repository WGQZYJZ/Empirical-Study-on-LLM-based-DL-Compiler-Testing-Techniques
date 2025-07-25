import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_358 = relay.var("var_358", dtype = "float32", shape = (13, 10, 2))#candidate|358|(13, 10, 2)|var|float32
var_359 = relay.var("var_359", dtype = "float32", shape = (13, 10, 2))#candidate|359|(13, 10, 2)|var|float32
bop_360 = relay.floor_mod(var_358.astype('float32'), relay.reshape(var_359.astype('float32'), relay.shape_of(var_358))) # shape=(13, 10, 2)
var_367 = relay.var("var_367", dtype = "float32", shape = (13, 10, 2))#candidate|367|(13, 10, 2)|var|float32
bop_368 = relay.maximum(var_358.astype('uint32'), relay.reshape(var_367.astype('uint32'), relay.shape_of(var_358))) # shape=(13, 10, 2)
output = relay.Tuple([bop_360,bop_368,])
output2 = relay.Tuple([bop_360,bop_368,])
func_410 = relay.Function([var_358,var_359,var_367,], output)
mod['func_410'] = func_410
mod = relay.transform.InferType()(mod)
var_411 = relay.var("var_411", dtype = "float32", shape = (13, 10, 2))#candidate|411|(13, 10, 2)|var|float32
var_412 = relay.var("var_412", dtype = "float32", shape = (13, 10, 2))#candidate|412|(13, 10, 2)|var|float32
var_413 = relay.var("var_413", dtype = "float32", shape = (13, 10, 2))#candidate|413|(13, 10, 2)|var|float32
output = func_410(var_411,var_412,var_413,)
func_414 = relay.Function([var_411,var_412,var_413,], output)
mutated_mod['func_414'] = func_414
mutated_mod = relay.transform.InferType()(mutated_mod)
const_492 = relay.const([[[-6.436375,4.295050,-8.386494,1.546866,-1.559768,0.855492,-1.777358,7.468388],[3.447721,9.449822,-9.313162,3.411661,-2.915758,6.159665,-5.022077,0.721833],[-0.279841,-9.761302,-7.088987,4.898051,9.660511,-7.527586,-6.218261,-6.492930],[-2.307367,-7.393785,4.521580,7.059550,1.010004,3.579592,6.376374,-6.922866],[6.872815,-0.747446,-6.121582,-7.252125,-0.960821,0.864309,1.769381,-0.928755],[-9.268361,-0.672568,-6.467168,9.460895,-9.424085,-6.559810,9.109009,-1.055062],[8.313918,-8.926650,-8.706464,6.950015,4.574375,6.853246,-7.680895,5.931901]]], dtype = "float64")#candidate|492|(1, 7, 8)|const|float64
uop_493 = relay.cosh(const_492.astype('float64')) # shape=(1, 7, 8)
output = uop_493
output2 = uop_493
func_495 = relay.Function([], output)
mod['func_495'] = func_495
mod = relay.transform.InferType()(mod)
output = func_495()
func_496 = relay.Function([], output)
mutated_mod['func_496'] = func_496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_495_call = mod.get_global_var('func_495')
func_496_call = mutated_mod.get_global_var('func_496')
call_517 = func_495_call()
call_518 = func_495_call()
output = call_517
output2 = call_518
func_526 = relay.Function([], output)
mod['func_526'] = func_526
mod = relay.transform.InferType()(mod)
output = func_526()
func_527 = relay.Function([], output)
mutated_mod['func_527'] = func_527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_570 = func_526_call()
call_571 = func_526_call()
output = call_570
output2 = call_571
func_574 = relay.Function([], output)
mod['func_574'] = func_574
mod = relay.transform.InferType()(mod)
output = func_574()
func_575 = relay.Function([], output)
mutated_mod['func_575'] = func_575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_598 = func_526_call()
call_599 = func_526_call()
output = relay.Tuple([call_598,])
output2 = relay.Tuple([call_599,])
func_600 = relay.Function([], output)
mod['func_600'] = func_600
mod = relay.transform.InferType()(mod)
mutated_mod['func_600'] = func_600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_600_call = mutated_mod.get_global_var('func_600')
call_601 = func_600_call()
output = call_601
func_602 = relay.Function([], output)
mutated_mod['func_602'] = func_602
mutated_mod = relay.transform.InferType()(mutated_mod)
const_665 = relay.const([[[0.550688,-2.924682],[-2.920244,6.514061],[0.373179,-5.398354],[-0.894219,3.305632],[-1.420009,6.068919],[8.760364,5.882818],[-7.509277,4.884859],[0.964638,-5.205531],[-7.103766,-6.044496],[-1.395966,-1.268684],[4.310137,8.187672],[-4.426075,4.716976],[1.790810,-8.283338],[-9.863962,-2.685247],[6.101633,5.194595]],[[-9.968203,3.385266],[-1.000241,-3.348089],[-6.451897,-9.901768],[6.086510,4.495820],[8.357343,-3.054177],[9.239006,8.742626],[-8.368792,-3.179202],[3.950716,-1.407624],[2.119095,-9.815802],[-7.553275,0.616696],[-3.661709,-5.610293],[9.795897,5.088581],[-6.068178,3.496416],[4.678700,9.799447],[-5.154392,7.004811]],[[1.570198,-9.048655],[8.532223,-4.407946],[4.928773,-4.758863],[4.371462,6.689195],[-2.913636,8.338783],[-4.389214,-7.725217],[5.959807,-6.259270],[3.977337,-9.017901],[1.584791,-1.595092],[1.961923,-2.398151],[-8.848879,-4.038273],[9.353221,-7.639379],[1.355833,-9.120256],[-0.200323,6.068731],[-7.991156,-3.359987]],[[0.480355,-3.726777],[0.100234,5.491902],[8.593734,3.369548],[2.448315,-9.068969],[5.817462,-2.081145],[-9.834638,-1.682890],[-0.333515,6.742916],[3.895960,-4.856160],[-9.661349,-0.131436],[8.745860,-7.730297],[2.882247,-6.606409],[-1.964228,-0.228261],[9.588129,-7.868980],[3.021279,6.378504],[-5.351367,7.792935]],[[-9.577348,-3.438471],[-9.679569,-1.195138],[-0.919174,9.006215],[-5.770827,-5.468431],[-5.761936,-3.914503],[-5.230844,2.065081],[5.640417,7.286212],[3.329639,-5.853873],[-7.332738,-0.059855],[5.056273,1.727694],[-5.753052,3.380384],[-6.919004,6.787182],[-3.073030,4.283916],[-0.364876,5.145933],[1.571461,8.213678]]], dtype = "float64")#candidate|665|(5, 15, 2)|const|float64
const_666 = relay.const([[[-8.363781,-9.913624],[-5.940685,0.734912],[7.983154,-3.823437],[-6.523469,6.017977],[1.845493,2.996939],[-5.773337,-7.762507],[4.731040,-2.381917],[-0.988923,-1.931270],[0.749214,-3.829225],[-9.871039,4.395953],[6.779063,1.319218],[9.312436,1.158636],[-0.993507,4.787039],[-2.014579,-4.925396],[8.158181,-3.643777]],[[-0.962536,-1.366146],[1.258074,-6.021971],[-8.975203,8.604710],[0.411151,8.697130],[8.298149,-6.443861],[9.487844,-3.133873],[6.427602,1.550052],[6.193996,-0.916815],[3.477320,-1.746908],[9.462060,-4.878358],[-9.260990,8.609754],[-1.959938,-9.814884],[2.727030,-3.048017],[-6.807965,-1.468172],[6.791762,-1.405795]],[[7.818793,2.461274],[3.621961,1.612185],[-3.730222,-6.941782],[-1.722359,-4.891122],[-7.335329,-4.165386],[2.655800,-1.419458],[-8.387115,2.543666],[4.017273,-1.604021],[1.120270,8.228692],[4.346936,9.216977],[-8.818430,0.753245],[-5.193408,-2.927492],[-8.553690,-1.238686],[7.699737,-3.392752],[-9.678433,5.021684]],[[6.611201,-1.782776],[1.849997,-9.043627],[9.620655,-3.782649],[2.386334,-5.810238],[-0.155369,8.621493],[2.881953,-8.138978],[-4.296864,-8.612361],[6.485437,-2.216983],[-3.490554,8.113806],[-5.704469,-6.867924],[8.009883,-7.786919],[-2.514057,-6.922218],[5.954250,-6.497299],[-9.653705,0.262845],[9.619861,4.334240]],[[8.947536,8.752741],[-7.112644,-8.734138],[-7.739802,-5.444337],[6.994162,6.813690],[0.310183,-5.799805],[8.209150,-2.655855],[-8.785575,-4.578416],[3.325381,-6.197139],[-5.076256,-1.227133],[-6.155726,9.127136],[-9.256469,-0.206007],[-4.621680,2.160043],[-2.611186,-6.638965],[-9.457698,9.801087],[-7.533668,-9.535623]]], dtype = "float64")#candidate|666|(5, 15, 2)|const|float64
bop_667 = relay.power(const_665.astype('float64'), relay.reshape(const_666.astype('float64'), relay.shape_of(const_665))) # shape=(5, 15, 2)
const_672 = relay.const([[[4.137280,0.916577],[-6.450324,-6.234580],[3.993213,4.241192],[4.201058,-0.494428],[-1.112473,1.698565],[-9.070477,-0.761722],[7.501707,-5.370006],[-6.864707,5.198643],[7.676361,9.146952],[-9.365093,-1.790683],[7.290160,1.299906],[1.331653,-4.325850],[-0.504575,1.918694],[3.526988,3.294510],[-1.335849,9.136215]],[[7.323470,-2.138327],[-0.319435,9.911435],[-0.915537,-1.396937],[4.894392,-6.595908],[1.433385,-7.785106],[4.508837,-0.340249],[0.813979,7.995970],[3.448720,-0.637278],[4.912917,2.856381],[4.712508,-4.465297],[5.042517,9.984725],[9.236809,7.137350],[-6.907487,-5.850374],[-9.921600,5.570165],[-2.711087,8.399705]],[[1.702204,-9.408904],[9.833759,-8.977991],[-1.056714,-1.326595],[4.712039,-6.434388],[8.288936,-2.877442],[-1.880458,3.659741],[8.394195,-5.619764],[-9.968427,-8.085180],[-1.831722,-0.710303],[-3.354339,-5.799140],[-9.898270,-4.540885],[-9.855109,-2.629252],[2.473659,8.873866],[6.538650,-0.531650],[6.475002,-1.223794]],[[-2.293739,-4.609581],[7.446245,-3.684441],[0.455859,4.803247],[7.751149,-8.955894],[-7.325174,-0.136248],[5.509300,0.335314],[-0.485808,3.115694],[1.006584,4.828945],[-1.310007,-3.326413],[6.879630,-7.015919],[5.054936,-0.494868],[7.937579,-2.401461],[6.131197,6.675452],[-1.108039,5.705757],[-4.858601,2.042090]],[[-9.503540,-9.535843],[-4.606339,-4.941735],[8.470468,-0.394968],[-1.853551,-2.052485],[5.129296,-8.575429],[3.895189,1.951226],[-7.611186,-8.572526],[-3.931036,-7.195173],[7.362948,7.192454],[2.997307,9.098671],[-2.630451,8.630450],[-8.214517,8.453245],[-6.407006,-3.445200],[2.818907,-9.525387],[-5.206260,7.522313]]], dtype = "float64")#candidate|672|(5, 15, 2)|const|float64
bop_673 = relay.greater_equal(const_665.astype('bool'), relay.reshape(const_672.astype('bool'), relay.shape_of(const_665))) # shape=(5, 15, 2)
output = relay.Tuple([bop_667,bop_673,])
output2 = relay.Tuple([bop_667,bop_673,])
func_676 = relay.Function([], output)
mod['func_676'] = func_676
mod = relay.transform.InferType()(mod)
output = func_676()
func_677 = relay.Function([], output)
mutated_mod['func_677'] = func_677
mutated_mod = relay.transform.InferType()(mutated_mod)
var_703 = relay.var("var_703", dtype = "float32", shape = (9, 4, 2))#candidate|703|(9, 4, 2)|var|float32
uop_704 = relay.rsqrt(var_703.astype('float32')) # shape=(9, 4, 2)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_718 = func_574_call()
call_719 = func_574_call()
output = relay.Tuple([uop_704,call_718,])
output2 = relay.Tuple([uop_704,call_719,])
func_720 = relay.Function([var_703,], output)
mod['func_720'] = func_720
mod = relay.transform.InferType()(mod)
var_721 = relay.var("var_721", dtype = "float32", shape = (9, 4, 2))#candidate|721|(9, 4, 2)|var|float32
output = func_720(var_721)
func_722 = relay.Function([var_721], output)
mutated_mod['func_722'] = func_722
mutated_mod = relay.transform.InferType()(mutated_mod)
var_735 = relay.var("var_735", dtype = "float64", shape = (1, 9, 10))#candidate|735|(1, 9, 10)|var|float64
var_736 = relay.var("var_736", dtype = "float64", shape = (1, 9, 10))#candidate|736|(1, 9, 10)|var|float64
bop_737 = relay.power(var_735.astype('float64'), relay.reshape(var_736.astype('float64'), relay.shape_of(var_735))) # shape=(1, 9, 10)
output = relay.Tuple([bop_737,])
output2 = relay.Tuple([bop_737,])
func_746 = relay.Function([var_735,var_736,], output)
mod['func_746'] = func_746
mod = relay.transform.InferType()(mod)
var_747 = relay.var("var_747", dtype = "float64", shape = (1, 9, 10))#candidate|747|(1, 9, 10)|var|float64
var_748 = relay.var("var_748", dtype = "float64", shape = (1, 9, 10))#candidate|748|(1, 9, 10)|var|float64
output = func_746(var_747,var_748,)
func_749 = relay.Function([var_747,var_748,], output)
mutated_mod['func_749'] = func_749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_756 = func_526_call()
call_757 = func_526_call()
func_410_call = mod.get_global_var('func_410')
func_414_call = mutated_mod.get_global_var('func_414')
var_767 = relay.var("var_767", dtype = "float32", shape = (260,))#candidate|767|(260,)|var|float32
call_766 = relay.TupleGetItem(func_410_call(relay.reshape(var_767.astype('float32'), [13, 10, 2]), relay.reshape(var_767.astype('float32'), [13, 10, 2]), relay.reshape(var_767.astype('float32'), [13, 10, 2]), ), 1)
call_768 = relay.TupleGetItem(func_414_call(relay.reshape(var_767.astype('float32'), [13, 10, 2]), relay.reshape(var_767.astype('float32'), [13, 10, 2]), relay.reshape(var_767.astype('float32'), [13, 10, 2]), ), 1)
bop_788 = relay.logical_or(call_766.astype('bool'), relay.reshape(var_767.astype('bool'), relay.shape_of(call_766))) # shape=(13, 10, 2)
bop_791 = relay.logical_or(call_768.astype('bool'), relay.reshape(var_767.astype('bool'), relay.shape_of(call_768))) # shape=(13, 10, 2)
func_600_call = mod.get_global_var('func_600')
func_602_call = mutated_mod.get_global_var('func_602')
call_798 = relay.TupleGetItem(func_600_call(), 0)
call_799 = relay.TupleGetItem(func_602_call(), 0)
bop_806 = relay.less_equal(call_798.astype('bool'), relay.reshape(call_756.astype('bool'), relay.shape_of(call_798))) # shape=(1, 7, 8)
bop_809 = relay.less_equal(call_799.astype('bool'), relay.reshape(call_757.astype('bool'), relay.shape_of(call_799))) # shape=(1, 7, 8)
func_746_call = mod.get_global_var('func_746')
func_749_call = mutated_mod.get_global_var('func_749')
var_816 = relay.var("var_816", dtype = "float64", shape = (90, 1))#candidate|816|(90, 1)|var|float64
call_815 = relay.TupleGetItem(func_746_call(relay.reshape(var_816.astype('float64'), [1, 9, 10]), relay.reshape(var_816.astype('float64'), [1, 9, 10]), ), 0)
call_817 = relay.TupleGetItem(func_749_call(relay.reshape(var_816.astype('float64'), [1, 9, 10]), relay.reshape(var_816.astype('float64'), [1, 9, 10]), ), 0)
func_495_call = mod.get_global_var('func_495')
func_496_call = mutated_mod.get_global_var('func_496')
call_819 = func_495_call()
call_820 = func_495_call()
const_825 = relay.const([[[True,False],[False,True],[True,False],[False,False],[False,False],[True,False],[True,True],[False,False],[True,True],[True,False]],[[False,True],[False,True],[True,True],[True,False],[False,False],[False,True],[False,False],[False,True],[False,False],[True,False]],[[True,False],[False,False],[False,False],[False,True],[False,True],[True,False],[True,False],[True,False],[True,False],[False,False]],[[False,False],[True,False],[False,False],[True,False],[False,True],[False,True],[True,False],[True,True],[True,True],[True,True]],[[True,False],[True,False],[False,False],[False,False],[False,False],[False,True],[False,True],[True,False],[True,True],[False,False]],[[False,False],[True,True],[False,True],[True,True],[False,False],[False,True],[False,True],[True,True],[True,True],[True,False]],[[True,True],[True,True],[False,False],[True,False],[True,True],[False,True],[True,True],[True,False],[False,False],[True,True]],[[False,False],[False,False],[True,False],[True,True],[True,False],[True,True],[True,False],[False,False],[False,False],[False,False]],[[True,False],[True,True],[True,False],[True,False],[False,False],[True,False],[False,True],[True,False],[True,False],[True,True]],[[True,False],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[True,False],[False,False],[False,True]],[[False,True],[True,True],[False,False],[True,False],[True,False],[True,False],[False,True],[False,False],[True,True],[False,False]],[[True,True],[False,False],[True,True],[False,True],[True,False],[False,True],[True,False],[False,True],[False,True],[True,True]],[[True,False],[True,True],[True,False],[True,True],[True,False],[True,False],[True,True],[False,False],[False,False],[True,True]]], dtype = "bool")#candidate|825|(13, 10, 2)|const|bool
bop_826 = relay.right_shift(bop_788.astype('int16'), relay.reshape(const_825.astype('int16'), relay.shape_of(bop_788))) # shape=(13, 10, 2)
bop_829 = relay.right_shift(bop_791.astype('int16'), relay.reshape(const_825.astype('int16'), relay.shape_of(bop_791))) # shape=(13, 10, 2)
bop_835 = relay.less(call_756.astype('bool'), relay.reshape(call_798.astype('bool'), relay.shape_of(call_756))) # shape=(1, 7, 8)
bop_838 = relay.less(call_757.astype('bool'), relay.reshape(call_799.astype('bool'), relay.shape_of(call_757))) # shape=(1, 7, 8)
func_410_call = mod.get_global_var('func_410')
func_414_call = mutated_mod.get_global_var('func_414')
call_855 = relay.TupleGetItem(func_410_call(relay.reshape(bop_788.astype('float32'), [13, 10, 2]), relay.reshape(call_766.astype('float32'), [13, 10, 2]), relay.reshape(var_767.astype('float32'), [13, 10, 2]), ), 1)
call_856 = relay.TupleGetItem(func_414_call(relay.reshape(bop_788.astype('float32'), [13, 10, 2]), relay.reshape(call_766.astype('float32'), [13, 10, 2]), relay.reshape(var_767.astype('float32'), [13, 10, 2]), ), 1)
uop_865 = relay.asinh(bop_788.astype('float32')) # shape=(13, 10, 2)
uop_867 = relay.asinh(bop_791.astype('float32')) # shape=(13, 10, 2)
var_868 = relay.var("var_868", dtype = "bool", shape = (13, 10, 2))#candidate|868|(13, 10, 2)|var|bool
bop_869 = relay.multiply(const_825.astype('float32'), relay.reshape(var_868.astype('float32'), relay.shape_of(const_825))) # shape=(13, 10, 2)
output = relay.Tuple([bop_806,call_815,var_816,call_819,bop_826,bop_835,call_855,uop_865,bop_869,])
output2 = relay.Tuple([bop_809,call_817,var_816,call_820,bop_829,bop_838,call_856,uop_867,bop_869,])
func_872 = relay.Function([var_767,var_816,var_868,], output)
mod['func_872'] = func_872
mod = relay.transform.InferType()(mod)
mutated_mod['func_872'] = func_872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_872_call = mutated_mod.get_global_var('func_872')
var_874 = relay.var("var_874", dtype = "float32", shape = (260,))#candidate|874|(260,)|var|float32
var_875 = relay.var("var_875", dtype = "float64", shape = (90, 1))#candidate|875|(90, 1)|var|float64
var_876 = relay.var("var_876", dtype = "bool", shape = (13, 10, 2))#candidate|876|(13, 10, 2)|var|bool
call_873 = func_872_call(var_874,var_875,var_876,)
output = call_873
func_877 = relay.Function([var_874,var_875,var_876,], output)
mutated_mod['func_877'] = func_877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_899 = func_574_call()
call_900 = func_574_call()
uop_922 = relay.rsqrt(call_899.astype('float32')) # shape=(1, 7, 8)
uop_924 = relay.rsqrt(call_900.astype('float32')) # shape=(1, 7, 8)
output = uop_922
output2 = uop_924
func_925 = relay.Function([], output)
mod['func_925'] = func_925
mod = relay.transform.InferType()(mod)
output = func_925()
func_926 = relay.Function([], output)
mutated_mod['func_926'] = func_926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_600_call = mod.get_global_var('func_600')
func_602_call = mutated_mod.get_global_var('func_602')
call_937 = relay.TupleGetItem(func_600_call(), 0)
call_938 = relay.TupleGetItem(func_602_call(), 0)
var_939 = relay.var("var_939", dtype = "float64", shape = (16, 7, 8))#candidate|939|(16, 7, 8)|var|float64
bop_940 = relay.floor_mod(call_937.astype('float64'), var_939.astype('float64')) # shape=(16, 7, 8)
bop_943 = relay.floor_mod(call_938.astype('float64'), var_939.astype('float64')) # shape=(16, 7, 8)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
var_947 = relay.var("var_947", dtype = "float32", shape = (36, 2))#candidate|947|(36, 2)|var|float32
call_946 = relay.TupleGetItem(func_720_call(relay.reshape(var_947.astype('float32'), [9, 4, 2])), 0)
call_948 = relay.TupleGetItem(func_722_call(relay.reshape(var_947.astype('float32'), [9, 4, 2])), 0)
bop_951 = relay.greater(var_947.astype('bool'), relay.reshape(call_946.astype('bool'), relay.shape_of(var_947))) # shape=(36, 2)
bop_954 = relay.greater(var_947.astype('bool'), relay.reshape(call_948.astype('bool'), relay.shape_of(var_947))) # shape=(36, 2)
func_495_call = mod.get_global_var('func_495')
func_496_call = mutated_mod.get_global_var('func_496')
call_960 = func_495_call()
call_961 = func_495_call()
output = relay.Tuple([bop_940,bop_951,call_960,])
output2 = relay.Tuple([bop_943,bop_954,call_961,])
func_966 = relay.Function([var_939,var_947,], output)
mod['func_966'] = func_966
mod = relay.transform.InferType()(mod)
mutated_mod['func_966'] = func_966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_966_call = mutated_mod.get_global_var('func_966')
var_968 = relay.var("var_968", dtype = "float64", shape = (16, 7, 8))#candidate|968|(16, 7, 8)|var|float64
var_969 = relay.var("var_969", dtype = "float32", shape = (36, 2))#candidate|969|(36, 2)|var|float32
call_967 = func_966_call(var_968,var_969,)
output = call_967
func_970 = relay.Function([var_968,var_969,], output)
mutated_mod['func_970'] = func_970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1025 = relay.var("var_1025", dtype = "float32", shape = (13, 14, 2))#candidate|1025|(13, 14, 2)|var|float32
uop_1026 = relay.sinh(var_1025.astype('float32')) # shape=(13, 14, 2)
func_746_call = mod.get_global_var('func_746')
func_749_call = mutated_mod.get_global_var('func_749')
var_1044 = relay.var("var_1044", dtype = "float64", shape = (90,))#candidate|1044|(90,)|var|float64
call_1043 = relay.TupleGetItem(func_746_call(relay.reshape(var_1044.astype('float64'), [1, 9, 10]), relay.reshape(var_1044.astype('float64'), [1, 9, 10]), ), 0)
call_1045 = relay.TupleGetItem(func_749_call(relay.reshape(var_1044.astype('float64'), [1, 9, 10]), relay.reshape(var_1044.astype('float64'), [1, 9, 10]), ), 0)
output = relay.Tuple([uop_1026,call_1043,var_1044,])
output2 = relay.Tuple([uop_1026,call_1045,var_1044,])
func_1052 = relay.Function([var_1025,var_1044,], output)
mod['func_1052'] = func_1052
mod = relay.transform.InferType()(mod)
var_1053 = relay.var("var_1053", dtype = "float32", shape = (13, 14, 2))#candidate|1053|(13, 14, 2)|var|float32
var_1054 = relay.var("var_1054", dtype = "float64", shape = (90,))#candidate|1054|(90,)|var|float64
output = func_1052(var_1053,var_1054,)
func_1055 = relay.Function([var_1053,var_1054,], output)
mutated_mod['func_1055'] = func_1055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_1057 = func_526_call()
call_1058 = func_526_call()
output = relay.Tuple([call_1057,])
output2 = relay.Tuple([call_1058,])
func_1071 = relay.Function([], output)
mod['func_1071'] = func_1071
mod = relay.transform.InferType()(mod)
mutated_mod['func_1071'] = func_1071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mutated_mod.get_global_var('func_1071')
call_1072 = func_1071_call()
output = call_1072
func_1073 = relay.Function([], output)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1112 = relay.TupleGetItem(func_1071_call(), 0)
call_1113 = relay.TupleGetItem(func_1073_call(), 0)
func_410_call = mod.get_global_var('func_410')
func_414_call = mutated_mod.get_global_var('func_414')
var_1115 = relay.var("var_1115", dtype = "float32", shape = (260,))#candidate|1115|(260,)|var|float32
call_1114 = relay.TupleGetItem(func_410_call(relay.reshape(var_1115.astype('float32'), [13, 10, 2]), relay.reshape(var_1115.astype('float32'), [13, 10, 2]), relay.reshape(var_1115.astype('float32'), [13, 10, 2]), ), 1)
call_1116 = relay.TupleGetItem(func_414_call(relay.reshape(var_1115.astype('float32'), [13, 10, 2]), relay.reshape(var_1115.astype('float32'), [13, 10, 2]), relay.reshape(var_1115.astype('float32'), [13, 10, 2]), ), 1)
uop_1117 = relay.log10(var_1115.astype('float32')) # shape=(260,)
uop_1128 = relay.sqrt(uop_1117.astype('float64')) # shape=(260,)
output = relay.Tuple([call_1112,call_1114,uop_1128,])
output2 = relay.Tuple([call_1113,call_1116,uop_1128,])
func_1130 = relay.Function([var_1115,], output)
mod['func_1130'] = func_1130
mod = relay.transform.InferType()(mod)
mutated_mod['func_1130'] = func_1130
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1131 = relay.var("var_1131", dtype = "float32", shape = (260,))#candidate|1131|(260,)|var|float32
func_1130_call = mutated_mod.get_global_var('func_1130')
call_1132 = func_1130_call(var_1131)
output = call_1132
func_1133 = relay.Function([var_1131], output)
mutated_mod['func_1133'] = func_1133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_1197 = func_526_call()
call_1198 = func_526_call()
uop_1223 = relay.log10(call_1197.astype('float64')) # shape=(1, 7, 8)
uop_1225 = relay.log10(call_1198.astype('float64')) # shape=(1, 7, 8)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
const_1231 = relay.const([-9.449177,5.463618,6.456998,-0.222925,1.460553,6.591477,-7.493909,3.865829,5.547852,-5.266327,7.186909,-8.903379,8.196027,4.163808,4.901045,-6.013802,0.442655,-1.891071,4.833345,-2.579781,-1.958694,-7.818712,5.887162,7.579257,3.803378,-1.872984,-9.069260,5.361651,4.621321,-1.195305,6.909692,2.480785,-6.592124,8.327241,-3.513179,-4.727681,-2.914105,0.884231,3.639985,-5.826001,-8.200147,0.373581,8.487879,7.522919,4.087267,-3.772290,-1.053302,8.920389,4.954773,4.092500,-8.784411,-8.092232,-1.613739,-6.724706,-7.039828,-3.712529,-7.263788,4.606265,-3.390334,-6.663077,-1.569103,8.594817,-1.316527,2.407371,0.319668,-7.113509,-5.168998,-9.433688,-0.626724,-7.956250,3.290759,-6.992472], dtype = "float32")#candidate|1231|(72,)|const|float32
call_1230 = relay.TupleGetItem(func_720_call(relay.reshape(const_1231.astype('float32'), [9, 4, 2])), 1)
call_1232 = relay.TupleGetItem(func_722_call(relay.reshape(const_1231.astype('float32'), [9, 4, 2])), 1)
bop_1255 = relay.logical_or(uop_1223.astype('bool'), relay.reshape(call_1197.astype('bool'), relay.shape_of(uop_1223))) # shape=(1, 7, 8)
bop_1258 = relay.logical_or(uop_1225.astype('bool'), relay.reshape(call_1198.astype('bool'), relay.shape_of(uop_1225))) # shape=(1, 7, 8)
output = relay.Tuple([call_1230,const_1231,bop_1255,])
output2 = relay.Tuple([call_1232,const_1231,bop_1258,])
func_1260 = relay.Function([], output)
mod['func_1260'] = func_1260
mod = relay.transform.InferType()(mod)
mutated_mod['func_1260'] = func_1260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1260_call = mutated_mod.get_global_var('func_1260')
call_1261 = func_1260_call()
output = call_1261
func_1262 = relay.Function([], output)
mutated_mod['func_1262'] = func_1262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_495_call = mod.get_global_var('func_495')
func_496_call = mutated_mod.get_global_var('func_496')
call_1309 = func_495_call()
call_1310 = func_495_call()
output = relay.Tuple([call_1309,])
output2 = relay.Tuple([call_1310,])
func_1316 = relay.Function([], output)
mod['func_1316'] = func_1316
mod = relay.transform.InferType()(mod)
output = func_1316()
func_1317 = relay.Function([], output)
mutated_mod['func_1317'] = func_1317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1327 = relay.TupleGetItem(func_1071_call(), 0)
call_1328 = relay.TupleGetItem(func_1073_call(), 0)
var_1335 = relay.var("var_1335", dtype = "float64", shape = (9, 7, 8))#candidate|1335|(9, 7, 8)|var|float64
bop_1336 = relay.multiply(call_1327.astype('int32'), var_1335.astype('int32')) # shape=(9, 7, 8)
bop_1339 = relay.multiply(call_1328.astype('int32'), var_1335.astype('int32')) # shape=(9, 7, 8)
output = relay.Tuple([bop_1336,])
output2 = relay.Tuple([bop_1339,])
func_1340 = relay.Function([var_1335,], output)
mod['func_1340'] = func_1340
mod = relay.transform.InferType()(mod)
mutated_mod['func_1340'] = func_1340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1341 = relay.var("var_1341", dtype = "float64", shape = (9, 7, 8))#candidate|1341|(9, 7, 8)|var|float64
func_1340_call = mutated_mod.get_global_var('func_1340')
call_1342 = func_1340_call(var_1341)
output = call_1342
func_1343 = relay.Function([var_1341], output)
mutated_mod['func_1343'] = func_1343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_1348 = func_574_call()
call_1349 = func_574_call()
var_1360 = relay.var("var_1360", dtype = "float64", shape = (1, 7, 8))#candidate|1360|(1, 7, 8)|var|float64
bop_1361 = relay.floor_divide(call_1348.astype('float32'), relay.reshape(var_1360.astype('float32'), relay.shape_of(call_1348))) # shape=(1, 7, 8)
bop_1364 = relay.floor_divide(call_1349.astype('float32'), relay.reshape(var_1360.astype('float32'), relay.shape_of(call_1349))) # shape=(1, 7, 8)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1372 = relay.TupleGetItem(func_1071_call(), 0)
call_1373 = relay.TupleGetItem(func_1073_call(), 0)
func_746_call = mod.get_global_var('func_746')
func_749_call = mutated_mod.get_global_var('func_749')
const_1375 = relay.const([5.160641,-4.720806,9.893124,9.885379,-6.545748,6.792314,7.688456,8.923653,2.386688,0.867840,-1.103119,8.494056,-9.938474,-1.231405,-1.959196,-2.398201,-0.740872,9.205381,-6.405150,6.093727,7.302970,2.079690,0.175095,-6.960038,-5.477682,-7.485777,-2.513809,-3.519802,8.788069,-9.270173,4.375116,8.658253,7.770130,-3.638788,-0.353385,-1.876364,-2.556455,-6.706922,-8.472172,0.234656,-0.975990,-2.057488,2.413439,5.389245,7.662745,-9.570392,-9.755498,-1.729722,-9.837087,-4.739477,-7.709296,7.958789,-4.140564,7.711488,-6.587233,2.112104,-8.423476,8.469814,-6.352585,-2.612148,-8.495892,-2.451268,4.469920,5.491185,0.673504,-3.111600,-4.980444,3.913371,2.226925,-8.086161,3.414135,-3.122370,5.712687,9.892837,-7.665406,9.364546,5.507570,-6.463607,-2.056138,-2.648582,8.776978,1.202698,-3.767735,-1.416811,3.792714,2.217827,-2.413884,4.978671,4.591512,4.810749], dtype = "float64")#candidate|1375|(90,)|const|float64
call_1374 = relay.TupleGetItem(func_746_call(relay.reshape(const_1375.astype('float64'), [1, 9, 10]), relay.reshape(const_1375.astype('float64'), [1, 9, 10]), ), 0)
call_1376 = relay.TupleGetItem(func_749_call(relay.reshape(const_1375.astype('float64'), [1, 9, 10]), relay.reshape(const_1375.astype('float64'), [1, 9, 10]), ), 0)
const_1390 = relay.const([[[1.525506,3.986954,2.359565,5.312125,-6.807124,-3.827698,-9.833234,-0.094068],[-2.659323,-6.899743,-8.699026,6.141868,4.672806,0.100695,5.852064,2.767786],[-8.374218,3.559193,-2.913993,4.162207,5.491737,1.897786,-2.995057,-6.683407],[-8.858754,0.125486,-0.349573,-3.079352,2.920132,-6.910014,-8.257407,3.032117],[-9.310158,-7.033151,6.637152,4.225236,1.496988,-4.841230,2.582917,-3.460045],[-4.553145,-5.777706,9.585106,-6.233559,-0.377578,9.933602,-3.799208,9.316584],[5.625373,5.264559,-4.936397,2.575357,5.762347,1.850467,-6.538024,-7.084896]],[[-4.778580,1.575556,6.029898,-9.283157,-6.029144,-6.578152,-5.062320,-1.774357],[6.961409,-3.421289,-2.617759,7.804457,3.110091,-9.185151,4.588000,-8.577415],[-6.691079,7.792150,5.906967,0.527413,5.726684,-9.933922,-0.165277,8.496929],[-1.465826,7.137990,4.271055,-8.119918,2.682594,2.242376,4.206596,-4.905797],[1.331016,4.715423,2.484578,4.934623,-0.680186,-2.977377,-0.570568,-5.326769],[3.121818,8.549600,4.890120,-4.334201,1.092297,6.886399,4.140737,-4.310529],[9.069536,-0.794160,-9.356748,8.091856,6.570789,9.589876,8.184138,2.235223]],[[1.881875,7.656351,-9.249463,-2.734243,9.212083,3.570118,3.667446,-0.133658],[0.860050,-2.828604,-9.876923,9.701509,0.479409,2.364122,-8.308673,-4.868332],[9.885329,-3.975025,8.857168,7.967016,-5.148610,0.988814,-2.015110,-3.299645],[-3.136982,-6.043778,-1.561883,6.629543,-3.062036,-6.222329,4.148557,3.297711],[3.881869,-6.479943,-0.280748,4.253944,-0.418425,-5.197408,-5.744553,8.849851],[5.427450,4.271145,3.218804,-8.061190,5.776211,-5.511123,1.410745,-2.615664],[-4.597983,7.902726,-6.524009,9.918511,0.274881,-9.789716,3.391895,1.118812]],[[1.647036,-6.296764,4.465078,-5.673187,-6.577251,2.128578,-5.603021,-6.321896],[-3.466527,5.106451,-1.827799,-5.488660,8.724559,-2.856058,-1.678998,1.010804],[-1.546277,-9.046356,-8.809270,2.838989,4.706599,-4.937579,-7.179529,-5.265437],[-5.537120,5.732453,1.724306,0.961341,-7.388784,2.553297,7.984185,-0.116691],[-3.662793,6.913908,-8.122753,6.593846,3.432430,4.681267,-0.522648,-1.445057],[-0.272165,-4.291789,1.815267,-2.120565,7.601684,-0.927418,-5.078556,-6.505238],[2.143392,-5.290892,-0.753865,-5.982060,6.708649,4.587016,3.510338,8.049114]],[[-0.379730,5.651488,4.698471,3.588914,3.036868,8.718299,7.854831,9.685771],[9.690698,-2.826896,4.726414,9.073996,-7.627045,6.352695,-6.025928,0.122041],[-3.438473,7.938975,-6.996146,-2.925030,-8.538983,-9.715401,2.694453,0.234388],[0.918145,6.030396,-8.627751,2.205055,5.972968,-5.519345,1.322714,-8.247656],[8.814473,9.507805,1.725904,4.808814,9.929531,8.484642,9.864130,2.306667],[-2.530370,-2.709287,7.563942,5.755857,-3.971940,3.849782,-9.526048,4.533725],[8.677788,1.353288,-1.906730,-7.118095,-1.820508,-6.045328,-6.355854,-5.487905]]], dtype = "float64")#candidate|1390|(5, 7, 8)|const|float64
bop_1391 = relay.logical_xor(call_1348.astype('uint8'), const_1390.astype('uint8')) # shape=(5, 7, 8)
bop_1394 = relay.logical_xor(call_1349.astype('uint8'), const_1390.astype('uint8')) # shape=(5, 7, 8)
func_1340_call = mod.get_global_var('func_1340')
func_1343_call = mutated_mod.get_global_var('func_1343')
const_1399 = relay.const([-8.905267,8.087732,3.250714,2.961939,2.027712,3.651706,-2.371937,-6.835183,-1.391054,-2.279890,1.940509,-6.564825,-7.494515,4.917894,3.997531,9.655290,4.701063,-8.344376,5.693417,8.482630,9.213098,-5.304834,-5.768370,6.644217,7.171696,-7.650605,-8.042206,-6.848718,9.626862,-7.260613,-8.008562,-4.416514,5.515170,-9.603145,-3.327406,7.535288,-5.462142,-3.968692,-0.285148,-1.913765,5.158390,-4.296692,0.824701,-2.681806,-9.523913,0.162050,-9.032573,-2.713825,-9.777006,-6.320195,4.848702,5.399231,-9.950140,-7.406856,7.272728,-1.551824,-3.221263,-0.646224,0.884320,-4.283588,-2.984902,-0.128815,-1.879929,-3.202431,2.064976,3.598253,-4.090561,0.328378,-4.145410,7.488295,-6.688168,-4.987702,0.006595,-2.446573,5.191147,-3.631785,4.298342,9.204153,-1.989079,-5.100127,-2.143332,-0.238726,-9.716887,6.676250,2.173963,3.291436,-7.103853,-6.598181,-2.835254,-3.762595,-4.916178,1.493233,9.142845,0.929654,-8.600999,-2.857858,0.321147,8.729639,-3.588819,5.629992,-0.188489,4.895133,-6.203056,-2.027611,-1.054217,1.648155,3.260658,-1.801127,1.976936,-7.224451,-6.903109,-1.999996,3.396111,5.797035,7.166383,-5.493253,1.249579,-3.303709,5.322979,2.331756,-3.413299,-6.196798,8.630395,-7.060437,-0.771846,5.650968,6.843281,8.629025,3.726854,-8.289458,8.772951,-7.239993,-2.192050,-6.047656,8.216278,-0.986771,-2.147689,-9.101805,4.674240,-4.879707,8.659588,-1.105165,-1.115984,-8.603069,0.473033,-5.533602,1.588888,4.726458,7.954225,5.145892,2.123009,-3.626911,4.669555,-0.249241,-7.154302,-4.194744,-8.730832,-1.069164,-7.001580,-6.392939,-0.129761,-0.183672,-8.712539,7.023938,-0.664016,-3.326284,-4.816198,3.292397,4.783435,9.246722,5.879182,-0.520514,-4.443818,-8.870021,4.929779,-7.693138,7.805523,2.940331,0.667317,6.694040,8.939107,6.046184,2.919939,6.932762,-9.875639,-8.505867,1.332735,3.200066,5.710391,-5.159317,8.258273,-8.709915,-6.447667,-8.676075,2.329859,4.095269,0.737388,-4.313831,9.466214,-1.892758,-0.368476,1.146760,2.304001,-7.098324,-6.555930,3.037111,1.583742,-4.055821,7.271095,5.734455,7.539780,8.430540,-7.700747,2.460640,-6.051816,3.043069,-8.151921,-3.423410,-7.853336,-1.310067,3.613840,-8.469996,-2.963090,-6.549536,6.561187,-9.336709,-4.941452,8.542342,8.755329,7.506794,-5.467130,6.934827,9.135616,-3.370278,-5.252855,0.990354,-9.593394,-3.345209,-7.965843,-0.760572,3.069743,-2.281030,2.670901,-9.768540,-8.722652,-7.337138,-1.781804,3.217864,6.486683,7.920053,5.189255,2.940521,-8.517841,-6.376762,4.526854,-6.470708,3.180709,-1.692967,7.937887,0.670073,-1.807159,-7.399117,3.742394,5.858460,-9.139496,-9.890934,4.125753,6.334140,-2.394831,-8.298365,5.985519,-5.643924,-4.145598,5.519176,5.048943,7.583729,-8.416653,-7.701777,-5.108946,-9.292094,7.086275,-1.799950,-9.746099,-4.424226,4.500808,-8.790946,-2.465684,7.418773,-4.642901,-7.392102,1.432397,9.870198,7.679040,-0.775671,7.575881,-0.551727,3.655991,9.457651,9.338719,-7.451665,6.434801,2.300252,2.543894,-5.872294,0.918468,4.516508,-1.270018,-3.197124,9.617654,9.324807,9.446480,8.847574,-5.883038,-2.195459,-2.518930,-3.674478,-7.055463,1.856572,-6.028199,2.044441,-8.325986,7.792652,5.386377,6.884840,-3.384938,-2.334201,-5.538812,-3.358293,-8.456496,-2.866735,-8.694335,-8.495633,-8.911790,-7.572197,5.860329,-0.531196,2.594070,7.953390,3.971820,5.868615,4.198544,0.735066,3.826225,4.184643,4.205628,-5.760463,-4.784726,-3.961179,4.084781,-6.951479,-7.912762,-6.780312,-0.451384,-0.785335,-1.913273,2.492618,1.646793,-0.365768,-2.412401,1.317488,8.911410,3.926614,-4.115366,8.720797,6.793543,7.440116,-1.188574,5.435829,0.610275,4.198306,1.958661,9.416384,0.276961,8.386993,6.940984,7.504122,-8.843659,3.110912,-3.675432,-5.822182,-3.457529,2.205408,-8.450668,1.577875,6.336974,3.795547,1.437394,5.528227,-8.275433,-9.104547,4.646950,1.479155,7.117603,1.088867,1.294942,5.889674,1.751637,-2.064948,7.537890,0.417917,-1.413614,6.266953,0.018843,5.736941,4.956192,-9.345523,5.183750,-3.321088,-0.372856,0.576142,-0.285323,3.549009,8.827447,0.394072,2.605830,1.560982,5.168405,8.728224,-3.424397,4.864402,-1.789861,-0.443260,7.460810,-4.876209,-7.249604,2.715992,-8.614024,-1.964124,-5.931284,-1.030050,-2.153677,-3.800901,-1.344806,7.014406,-7.128772,-1.103018,-3.433366,-9.055545,-8.699929,4.276546,-8.040668,4.329050,2.019952,4.422242,9.627486,8.008566,8.247391,0.926739,7.535365,-7.485091,9.333395,-6.681613,-1.667383,4.460328,-9.448744,6.019180,8.072587,8.179735,6.161832,0.564124,9.513355,-4.851078,-8.969687,-1.622969,-5.641863,1.425522,-4.214340,8.169784,-4.665873,4.262961,4.818051,-2.245676,7.921887,0.056610,-0.818959,3.661751,1.834879,-1.185317,4.162133,7.262275,-3.906036,-8.350709,8.782352,9.195772,-5.006000,-6.823601,8.468705,4.342711,-9.033142,8.591693,5.377613,-0.373110,2.237106,-6.278975,-3.119960,-9.297699,-4.105019,5.928315,8.275836,9.258174,9.863853,0.821556,-4.097903,5.351114], dtype = "float64")#candidate|1399|(504,)|const|float64
call_1398 = relay.TupleGetItem(func_1340_call(relay.reshape(const_1399.astype('float64'), [9, 7, 8])), 0)
call_1400 = relay.TupleGetItem(func_1343_call(relay.reshape(const_1399.astype('float64'), [9, 7, 8])), 0)
func_410_call = mod.get_global_var('func_410')
func_414_call = mutated_mod.get_global_var('func_414')
const_1416 = relay.const([2.021984,4.711653,-4.789687,1.433086,-4.280184,5.717213,-7.478629,-1.900740,8.603751,0.647944,8.134664,6.414062,-9.881690,2.425698,-6.743657,3.853369,-0.540999,8.384587,-1.030698,-5.001100,3.289658,3.183534,-6.044871,-8.109425,9.700696,0.801691,-6.687384,9.444663,-5.156497,-7.262241,3.225437,-3.763092,-2.433561,4.872419,6.598726,1.066853,5.141345,-1.827007,-6.008901,4.429358,-0.297701,-2.277273,3.778301,-2.448806,-2.409413,-6.430339,-5.217961,0.373515,-0.867714,5.202552,-0.601730,5.539353,8.551352,0.645955,-5.873845,-6.905834,-6.106902,9.640652,-8.138339,6.918494,-5.920171,-2.742711,-3.392570,5.683052,-1.885382,-7.728558,4.733574,-5.542452,-4.863868,-1.081376,-7.204110,2.076536,0.600896,-4.851570,-7.941236,-7.365080,9.902520,-7.189002,-0.917190,7.988922,-0.525734,0.453415,3.562949,7.688346,-5.040054,-2.541009,-4.951738,0.569894,-2.479546,7.001355,2.773268,2.519152,-9.965867,-8.089096,1.841974,-2.294224,-3.314101,2.021699,0.273534,0.815309,-8.616844,7.097481,5.777359,-6.766601,-4.415939,7.894396,1.623919,1.425583,-0.567534,-2.579500,8.430217,6.129916,-2.318636,7.925031,9.447871,9.884040,-4.615233,-2.625900,0.703892,6.486819,-5.340124,4.044348,0.133285,-8.229051,5.654257,2.331342,2.256708,-2.317521,3.142284,4.351241,-5.696446,-0.197268,9.318751,-3.956049,5.180402,5.974488,-3.134857,3.238893,1.248942,2.931418,-4.383297,0.213984,-9.918777,2.605097,2.853097,-0.182066,-5.066002,-6.224952,-5.934412,-7.563615,-7.779896,3.433570,9.701954,-7.164969,-2.126034,5.639339,-3.733466,-7.579476,-8.432755,-2.565396,1.740435,2.956934,4.925457,2.075677,-9.224328,4.892633,2.607163,-1.558204,0.469522,0.923046,-1.599909,-9.467330,9.867744,8.765551,-1.899234,2.772385,0.836542,3.699790,-6.987024,-6.114012,4.026825,4.821797,-4.568185,2.670162,-1.691942,-9.142792,6.264716,7.159311,0.739182,-8.943479,-2.187852,4.179666,-4.674914,-6.845554,-1.407053,4.660644,-5.948266,-1.935203,-8.212325,-4.358174,2.849246,-4.402932,0.002019,9.713976,-4.547685,6.520015,-2.626773,-4.355306,6.886432,9.249660,5.640568,8.187235,-0.501246,8.187426,7.737569,9.807429,-4.021848,3.187831,-1.251021,-7.617991,-8.264430,6.388814,9.519828,5.923068,1.934556,-1.957183,-7.876163,-1.313144,3.464397,2.652163,-1.786783,5.447991,-8.831816,-5.621333,-0.276856,-8.374045,-4.065407,5.650274,1.801118,6.930157,2.534393,-3.816050,2.890084,-3.585843,-8.773323,-9.093737,2.633750,6.960190,-8.439531,-3.288932,-6.481149,-6.209573,-8.771480,-5.328552,-8.637762,-2.053865,9.939825,3.013298,-7.888526,-4.211333], dtype = "float32")#candidate|1416|(260,)|const|float32
call_1415 = relay.TupleGetItem(func_410_call(relay.reshape(const_1416.astype('float32'), [13, 10, 2]), relay.reshape(const_1416.astype('float32'), [13, 10, 2]), relay.reshape(const_1416.astype('float32'), [13, 10, 2]), ), 0)
call_1417 = relay.TupleGetItem(func_414_call(relay.reshape(const_1416.astype('float32'), [13, 10, 2]), relay.reshape(const_1416.astype('float32'), [13, 10, 2]), relay.reshape(const_1416.astype('float32'), [13, 10, 2]), ), 0)
output = relay.Tuple([bop_1361,call_1372,call_1374,const_1375,bop_1391,call_1398,const_1399,call_1415,const_1416,])
output2 = relay.Tuple([bop_1364,call_1373,call_1376,const_1375,bop_1394,call_1400,const_1399,call_1417,const_1416,])
func_1421 = relay.Function([var_1360,], output)
mod['func_1421'] = func_1421
mod = relay.transform.InferType()(mod)
mutated_mod['func_1421'] = func_1421
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1422 = relay.var("var_1422", dtype = "float64", shape = (1, 7, 8))#candidate|1422|(1, 7, 8)|var|float64
func_1421_call = mutated_mod.get_global_var('func_1421')
call_1423 = func_1421_call(var_1422)
output = call_1423
func_1424 = relay.Function([var_1422], output)
mutated_mod['func_1424'] = func_1424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_1449 = func_574_call()
call_1450 = func_574_call()
func_1130_call = mod.get_global_var('func_1130')
func_1133_call = mutated_mod.get_global_var('func_1133')
const_1452 = relay.const([2.879781,-5.484658,9.133670,-0.236988,-2.148903,8.796176,6.747324,-7.548106,4.034336,-2.544366,8.780208,2.768007,3.241400,9.118039,7.874552,5.128935,-3.316694,3.651205,-6.696779,-3.080988,-0.989139,-5.378060,0.605270,9.928868,8.262862,-0.826608,2.622063,-3.585868,-4.032740,4.885628,7.498240,6.265309,5.778596,7.000184,-6.755762,-6.711122,-5.962829,7.344605,4.222968,-5.309093,-8.642634,1.117854,-6.500262,-3.948333,2.961139,3.070382,-6.353939,4.997543,9.104404,2.792047,-2.657178,-4.507052,2.970525,0.848708,9.205209,9.742511,-9.676822,4.809717,-8.015759,-0.320155,1.809019,-8.878327,-1.195248,6.546772,-7.018649,0.651597,-6.514579,6.431234,2.186578,-6.281362,-2.100071,-9.049369,-0.398240,-3.321060,7.999822,6.773629,-7.791621,-3.334435,2.060531,-1.584616,3.427188,-5.810017,-5.660048,0.333632,-7.579806,-0.352972,9.384128,-0.353379,-0.113098,-7.716548,3.606221,-6.033546,8.245333,-0.577567,2.319643,-6.156301,-8.591834,-5.260432,4.504360,2.018591,-7.512990,-1.120892,-2.486265,4.902815,4.947790,1.916690,4.686692,-7.507482,-8.836798,5.097326,-7.627037,-1.346184,4.299026,3.187380,-5.112287,-8.621112,-9.515321,-4.524273,9.729256,5.562678,2.845747,0.533586,-8.522333,1.721105,-2.500756,-5.546043,4.817925,-5.643653,-8.320682,5.435843,-4.752492,0.392356,-3.859151,4.756707,7.345321,5.295177,3.204113,-4.455332,-0.523767,5.553963,-0.312092,3.662651,-2.847603,-0.827064,9.466120,-9.056004,-2.338602,-1.334136,3.396467,-0.457055,-0.329071,-1.329720,8.803302,-3.251444,-6.865433,-4.855083,8.918032,-6.895280,4.771432,-0.024200,-5.625624,-1.791715,-4.415039,-9.290993,8.755128,0.346501,-1.368894,7.446372,-5.818213,5.372531,3.682653,3.875133,-6.181533,2.981221,4.332044,-7.307068,-4.179982,-3.733323,-3.755040,-3.808189,2.813962,7.952533,0.010618,8.387309,-9.248774,0.705236,5.659565,7.286788,-0.534766,8.404731,-6.690487,-5.534807,2.882043,-2.978694,0.265923,6.100664,-4.574137,-2.858722,8.713551,5.741851,-7.283888,-8.036030,8.401559,1.274628,-5.565233,4.862027,8.652466,1.202327,-0.094836,-1.507971,-2.104101,5.819216,-8.779802,0.352530,7.077572,-8.391625,4.470046,0.602887,-8.793613,-8.269429,-1.196624,0.114078,2.102095,-7.286009,-5.453806,8.861157,-7.401802,6.557928,-7.571479,-5.356008,8.231195,-0.242709,9.173438,-8.517970,-4.908465,-5.487769,-7.016735,-2.046169,-2.140666,-6.317899,3.918584,-8.372857,-8.661530,6.148276,-4.507914,-0.286813,-9.875626,-8.278086,3.814745,2.440208,5.045921,-1.049682,2.944882,-2.785433,5.811797,8.619856,-3.232437,-6.771286,4.499180,-7.052397], dtype = "float32")#candidate|1452|(260,)|const|float32
call_1451 = relay.TupleGetItem(func_1130_call(relay.reshape(const_1452.astype('float32'), [260,])), 1)
call_1453 = relay.TupleGetItem(func_1133_call(relay.reshape(const_1452.astype('float32'), [260,])), 1)
var_1463 = relay.var("var_1463", dtype = "float64", shape = (16, 7, 8))#candidate|1463|(16, 7, 8)|var|float64
bop_1464 = relay.logical_xor(call_1449.astype('int16'), var_1463.astype('int16')) # shape=(16, 7, 8)
bop_1467 = relay.logical_xor(call_1450.astype('int16'), var_1463.astype('int16')) # shape=(16, 7, 8)
func_676_call = mod.get_global_var('func_676')
func_677_call = mutated_mod.get_global_var('func_677')
call_1471 = relay.TupleGetItem(func_676_call(), 1)
call_1472 = relay.TupleGetItem(func_677_call(), 1)
bop_1481 = relay.add(var_1463.astype('int64'), call_1449.astype('int64')) # shape=(16, 7, 8)
bop_1484 = relay.add(var_1463.astype('int64'), call_1450.astype('int64')) # shape=(16, 7, 8)
func_410_call = mod.get_global_var('func_410')
func_414_call = mutated_mod.get_global_var('func_414')
call_1494 = relay.TupleGetItem(func_410_call(relay.reshape(const_1452.astype('float32'), [13, 10, 2]), relay.reshape(const_1452.astype('float32'), [13, 10, 2]), relay.reshape(const_1452.astype('float32'), [13, 10, 2]), ), 1)
call_1495 = relay.TupleGetItem(func_414_call(relay.reshape(const_1452.astype('float32'), [13, 10, 2]), relay.reshape(const_1452.astype('float32'), [13, 10, 2]), relay.reshape(const_1452.astype('float32'), [13, 10, 2]), ), 1)
output = relay.Tuple([call_1451,const_1452,bop_1464,call_1471,bop_1481,call_1494,])
output2 = relay.Tuple([call_1453,const_1452,bop_1467,call_1472,bop_1484,call_1495,])
func_1497 = relay.Function([var_1463,], output)
mod['func_1497'] = func_1497
mod = relay.transform.InferType()(mod)
var_1498 = relay.var("var_1498", dtype = "float64", shape = (16, 7, 8))#candidate|1498|(16, 7, 8)|var|float64
output = func_1497(var_1498)
func_1499 = relay.Function([var_1498], output)
mutated_mod['func_1499'] = func_1499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1317_call = mutated_mod.get_global_var('func_1317')
call_1505 = relay.TupleGetItem(func_1316_call(), 0)
call_1506 = relay.TupleGetItem(func_1317_call(), 0)
func_966_call = mod.get_global_var('func_966')
func_970_call = mutated_mod.get_global_var('func_970')
const_1508 = relay.const([-2.009496,-7.099006,8.646042,-1.884790,-8.821264,3.872696,9.779394,2.965682,-4.292965,-2.061746,4.594545,-8.773970,1.039531,-5.704741,-0.978344,8.770710,-1.760564,3.533801,-0.350719,6.989247,8.151595,2.166553,-7.413458,-2.825375,-6.395435,-0.871012,6.415004,-1.946398,0.441522,2.894762,9.900033,-3.494250,-1.343374,5.062732,9.791026,8.298247,-1.806116,-7.754351,2.640890,3.821426,5.421706,2.655831,-1.627231,2.787059,-5.669297,4.749134,-3.611821,-0.342393,4.402881,6.932830,-9.886224,-1.591403,7.022274,9.033584,3.460148,1.084100,-5.330266,0.181500,-5.453867,-6.063394,5.214407,-3.046196,-9.930932,-2.650482,-3.409869,-8.355304,5.535584,1.420286,8.567845,1.862011,8.837201,-0.392736,-3.601616,3.374605,-6.968581,0.689046,1.213824,0.380417,-1.707927,-5.132438,-1.151305,0.113596,8.489240,-9.496855,5.492533,3.049403,-2.163505,-1.284464,-2.501808,0.542475,-1.011310,-5.365102,-6.219732,5.030335,-9.377605,-0.742537,-3.345900,-6.800017,-4.031146,6.609759,-6.791377,0.613478,-6.736936,9.798866,4.045365,1.553224,-4.517995,1.976305,-6.520278,8.108915,-0.645299,7.369613,-6.295032,-9.289021,-5.069314,-8.532399,6.174428,-8.000681,-2.993147,-8.311639,-7.640416,7.198529,8.881220,-5.995585,9.555530,-2.737509,0.523622,-9.060818,9.913250,-0.545268,-0.360696,6.703825,-7.026773,8.092071,5.206332,-4.667958,-4.088071,-9.654986,4.484735,0.023849,6.814250,-7.435891,2.409470,-7.769664,-6.241129,-2.998784,5.252102,-0.964194,9.607206,-0.074572,5.246470,5.231547,-2.073914,7.053399,-7.786925,-2.375442,8.337252,-6.790278,-1.927918,5.154159,9.101188,0.925903,5.915017,5.662636,-5.162372,-2.708205,-9.573637,0.006239,2.332119,-9.410393,0.005051,5.133288,-5.871566,5.035502,-4.639597,7.742804,-8.164166,3.480071,-9.605216,1.001359,-5.626161,-1.427893,0.820382,-9.769773,-3.729416,-7.187971,1.639351,-7.575896,4.624366,-1.038512,3.907987,9.473958,8.619566,3.041307,7.318600,-7.951027,-5.678685,7.877116,-2.397770,6.985619,-7.673392,-3.094040,5.652836,0.103387,-2.792571,0.985087,0.276534,9.340997,6.483742,-0.760752,6.800048,-5.987408,8.049856,5.542815,1.035161,7.361340,-5.006124,-7.688295,-9.377630,-9.000479,7.652361,-6.987540,5.128977,9.926213,6.652291,2.787663,-7.557096,-8.369895,5.404185,8.388053,-4.042535,9.521890,-1.545714,7.138170,4.864426,3.127409,8.051759,-2.752266,-4.311378,3.642865,4.700715,-1.785972,-1.633510,-5.255235,6.846569,5.563105,-5.796466,-8.370844,-5.114856,9.743100,-4.329686,-3.271176,7.289820,-1.265341,8.710298,5.367661,-0.570269,-6.988744,-1.708722,0.018526,3.736753,-4.574322,5.572956,-6.574130,-2.420871,2.062439,1.486392,-0.512346,-5.306795,-6.933658,-4.687469,7.391569,7.773318,6.251986,-6.456177,3.204788,1.876312,9.783544,3.723737,-2.427705,3.432501,-9.012495,-5.069449,8.202583,5.197312,-4.331127,7.514178,-1.258380,0.831015,5.974887,-0.821203,9.231698,-5.400744,-4.122397,4.263038,0.671729,9.691374,0.118831,-4.602901,-7.114448,-2.358768,7.038432,-6.828292,-7.551644,4.976016,9.584314,9.505956,-7.969848,6.879444,9.524823,4.506556,-9.249690,-0.910288,-2.168725,-5.138388,-6.752593,9.832045,5.512395,7.802395,-4.090414,7.689752,8.452202,-7.870132,-2.363129,-7.144600,-3.753282,-8.858765,-6.224089,-6.863276,7.041484,-8.855394,4.510351,5.303470,8.287289,6.575099,5.244424,-3.414983,2.986746,-3.129496,-2.938906,0.748265,0.392461,4.682359,-7.965956,-8.032772,2.906747,8.462367,6.337418,3.451107,8.659558,-5.379774,7.459978,3.947229,8.019470,-3.612956,7.187016,7.101471,6.926417,-7.979838,-2.122228,9.896505,9.267639,1.691985,3.590141,-2.387653,7.863452,2.981644,9.150111,7.209261,2.915139,-3.680301,4.091457,7.705211,7.949807,-8.947909,-0.661015,0.957626,-3.938054,-1.288350,6.502210,-6.040905,5.307352,2.669318,8.745402,-0.137703,-6.184769,1.285648,-6.138513,-2.967618,-5.277191,2.715735,-1.294751,2.791838,6.545763,-5.788606,-2.620275,8.137395,-7.180865,-8.764423,4.282432,-0.501787,4.571135,0.273216,-3.064513,7.915605,-8.250954,-6.552783,1.762010,6.566710,1.357081,0.398507,9.045536,-3.458949,3.011999,1.526171,4.462394,-6.893455,1.447681,-0.490824,1.816285,-8.346485,-7.565496,-6.470860,-6.654804,4.426363,7.703524,7.410342,9.041298,7.810320,-9.045501,-5.278473,-1.678361,4.729219,-3.899606,-3.520596,1.881773,-8.341847,0.281528,-2.629980,-2.387300,3.172954,-3.084382,-6.540741,-6.184708,2.930236,-8.390312,-9.041269,-8.540906,-5.461009,0.670899,0.442141,-5.421239,3.813405,-6.840539,1.892964,9.231817,4.186479,-6.448276,4.916308,3.923082,2.332529,-8.578433,-7.133963,3.531660,-8.796257,5.948775,-5.939548,0.199339,8.458576,9.121477,-5.765391,-7.394685,-9.154473,-5.542175,9.042642,-1.087133,2.993683,1.757380,-0.308588,2.055773,2.443806,-7.614627,-1.900328,1.181976,7.937128,-9.282513,2.158099,2.562051,6.967342,-0.616977,8.458552,-1.445721,2.711825,8.158542,-4.023555,-8.026095,0.951627,0.446423,-9.631325,-9.155803,5.294790,-1.113854,6.234170,4.007589,9.234544,4.885457,-0.795514,2.493949,0.704655,4.198990,5.197086,-8.479826,-8.739277,-6.730192,-6.118068,6.099660,-0.863993,7.179293,9.450093,-6.093341,-9.829678,-2.681920,3.212502,-0.250115,-9.817186,5.112103,-5.012736,-8.983109,5.684633,1.521866,7.522390,-9.482138,-3.723804,7.088363,-1.732551,-4.049754,-3.196257,5.150808,9.074276,-9.758049,-8.562521,3.961602,7.587924,7.041271,9.694997,5.705621,3.859647,-2.304911,5.676773,-6.222326,2.919440,-3.913122,1.867950,-3.088870,4.534809,-1.786886,-4.923536,-9.909015,4.268845,-4.366983,4.413181,-0.450135,1.716681,-8.642716,-0.757662,-3.434163,-6.461736,7.178128,3.993387,-8.768251,4.720746,-9.161271,-6.944628,6.328293,-9.104194,-3.318062,5.047343,5.966401,2.641448,1.775095,-7.206291,-1.858352,-2.424809,-0.392245,9.066489,4.418944,0.951485,-1.847454,-8.127749,4.747932,5.238702,-5.065038,-5.937253,-7.620557,-8.887044,-0.644762,7.723451,9.723139,-9.874483,9.658400,-1.161478,-5.963651,-6.156015,4.297778,8.745226,-6.575718,7.452544,5.427347,-3.198245,0.892610,-2.241523,8.863034,-8.281036,5.482105,-0.850238,-1.810224,6.822918,-2.833097,1.853733,9.478535,-8.555791,-4.252817,-5.868836,-0.165610,8.852529,9.659315,2.222295,8.220509,7.403750,-7.774003,-1.803202,-0.626547,-8.767865,0.550384,0.568242,-5.998486,-5.014824,6.686017,-5.170383,2.562481,9.966212,1.790999,8.971528,0.617851,-3.980828,-0.929584,-0.428008,-0.562814,4.801034,4.497181,-7.420544,3.282891,-3.525823,-2.850742,-3.209201,-0.132740,-4.742033,-1.659107,-0.665456,4.170620,7.480998,3.480586,-3.237487,-8.045167,-1.666568,-7.374765,4.081936,1.267135,-4.095761,5.635822,-2.649580,8.729069,2.842403,-8.353626,7.495744,-9.304994,-5.335442,-6.843562,-7.282345,-8.256462,-7.565675,4.340047,-6.086216,2.349761,-3.660739,5.792942,-8.726664,-1.973406,-5.367647,-3.503876,-9.229294,5.058443,-3.320973,0.474978,-7.411458,3.955467,1.855831,6.560743,-5.977495,-9.834503,8.118942,4.910539,-9.170351,7.915116,-6.100526,-8.792997,8.829673,2.917145,-2.303514,-1.401601,2.684569,4.433631,-9.582713,-7.417896,-8.804696,-0.154680,7.913203,9.116557,2.192853,-3.130359,-4.419108,-0.503589,-5.389932,-6.909964,-9.530390,-2.186704,-6.918313,-3.717225,-4.223878,1.401541,-1.068205,-3.775742,3.012348,5.356287,-4.916584,5.606692,4.407744,-4.728281,0.323522,-4.392527,1.915026,9.555302,-9.781266,1.067709,1.118432,9.742056,-6.554567,8.862511,-8.165349,-6.397054,-3.853914,4.570373,2.662590,-3.536405,-2.556336,-7.051848,4.995278,-3.903600,-8.057378,-8.256206,-0.763668,1.742353,4.701926,8.034028,0.782778,-3.359281,8.606448,2.986922,-6.268379,9.428838,-2.197374,-8.990819,-8.489788,-5.715322,-3.204283,-7.887130,-4.615932,0.274737,-8.633077,8.041817,-3.196092,9.151669,-9.360122,-0.363974,-7.442927,3.638272,-0.556399,-0.755271,-2.989102,5.456260,7.867239,-6.950937,7.570637,8.738282,-4.272028,7.783493,6.093578,-3.118819,-5.891863,-3.736897,-0.115322,1.055766,9.907133,0.063587,-5.219724,1.005401,-4.449651,-9.659617,2.689898,2.724574,-7.364770,4.721805,-5.450514,2.707128,-6.037157,7.362985,-2.168718,2.698689,3.813546,7.494486,4.587694,7.023013,-6.993036,7.963544,-2.117382,0.267484,-2.932613,-9.151377,-0.133815,2.211723,7.221303,-5.260285,1.373128,7.054443,-1.682661,5.567863,8.871518,-4.874858,-4.402914,-4.677148,-4.519193,9.956894,-3.564325,6.506619,-5.964034,6.457746,-8.785236,4.977144,-6.247051,-8.731377,8.764106,-4.861901,-8.070779,7.451138,8.272839,1.329898,6.974470,-8.980127,-1.043522,8.595250,-8.172603,-6.653786,-3.394226,-7.285624,4.906687,0.004751,-6.646953,7.687484,-8.614586,7.932657,-7.635034,-7.111461,-8.487934,2.218526,-3.632818,4.928186,-7.690337,4.712383,6.876113,9.491582,-2.830945,2.345431,-3.575217,-1.726125,8.061917,-9.123771,-4.037504,-1.632670,3.241108,-1.809763,-9.387245,-2.495039,9.004764,6.894912,-0.575521,3.021898], dtype = "float64")#candidate|1508|(896,)|const|float64
const_1509 = relay.const([-2.361763,9.058768,-7.814005,2.355365,-6.716644,7.944467,-6.868452,4.927859,7.574702,5.694271,-1.047445,8.352072,0.314943,4.863674,3.197190,-2.292568,-6.966462,-6.829937,-4.917527,-2.538326,9.796198,-2.773780,1.222040,-4.801186,-3.329348,6.150521,-9.531229,7.104116,-5.430179,-2.715688,3.782945,7.849547,-3.016338,-5.617198,0.354699,8.126837,-7.653441,-7.717937,-4.108654,-8.594147,-6.280645,8.616274,-0.448280,-4.962019,8.555263,3.505764,-9.711384,0.141560,-1.989276,9.475716,-8.700611,-3.805198,-7.809954,-0.734866,2.973061,0.243489,-3.461151,-2.455492,4.879784,7.398137,8.387261,-8.379112,6.442081,0.661950,0.265733,-7.228821,0.563104,9.336102,2.046392,-2.859264,-4.592148,5.765933], dtype = "float32")#candidate|1509|(72,)|const|float32
call_1507 = relay.TupleGetItem(func_966_call(relay.reshape(const_1508.astype('float64'), [16, 7, 8]), relay.reshape(const_1509.astype('float32'), [36, 2]), ), 0)
call_1510 = relay.TupleGetItem(func_970_call(relay.reshape(const_1508.astype('float64'), [16, 7, 8]), relay.reshape(const_1509.astype('float32'), [36, 2]), ), 0)
output = relay.Tuple([call_1505,call_1507,const_1508,const_1509,])
output2 = relay.Tuple([call_1506,call_1510,const_1508,const_1509,])
func_1513 = relay.Function([], output)
mod['func_1513'] = func_1513
mod = relay.transform.InferType()(mod)
mutated_mod['func_1513'] = func_1513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1513_call = mutated_mod.get_global_var('func_1513')
call_1514 = func_1513_call()
output = call_1514
func_1515 = relay.Function([], output)
mutated_mod['func_1515'] = func_1515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_926_call = mutated_mod.get_global_var('func_926')
call_1527 = func_925_call()
call_1528 = func_925_call()
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
call_1557 = relay.TupleGetItem(func_1421_call(relay.reshape(call_1527.astype('float64'), [1, 7, 8])), 7)
call_1558 = relay.TupleGetItem(func_1424_call(relay.reshape(call_1527.astype('float64'), [1, 7, 8])), 7)
uop_1560 = relay.sigmoid(call_1527.astype('float32')) # shape=(1, 7, 8)
uop_1562 = relay.sigmoid(call_1528.astype('float32')) # shape=(1, 7, 8)
bop_1565 = relay.maximum(uop_1560.astype('int64'), relay.reshape(call_1527.astype('int64'), relay.shape_of(uop_1560))) # shape=(1, 7, 8)
bop_1568 = relay.maximum(uop_1562.astype('int64'), relay.reshape(call_1528.astype('int64'), relay.shape_of(uop_1562))) # shape=(1, 7, 8)
output = relay.Tuple([call_1557,bop_1565,])
output2 = relay.Tuple([call_1558,bop_1568,])
func_1578 = relay.Function([], output)
mod['func_1578'] = func_1578
mod = relay.transform.InferType()(mod)
output = func_1578()
func_1579 = relay.Function([], output)
mutated_mod['func_1579'] = func_1579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1590 = relay.TupleGetItem(func_1071_call(), 0)
call_1591 = relay.TupleGetItem(func_1073_call(), 0)
output = call_1590
output2 = call_1591
func_1594 = relay.Function([], output)
mod['func_1594'] = func_1594
mod = relay.transform.InferType()(mod)
output = func_1594()
func_1595 = relay.Function([], output)
mutated_mod['func_1595'] = func_1595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_1628 = relay.TupleGetItem(func_1578_call(), 1)
call_1629 = relay.TupleGetItem(func_1579_call(), 1)
func_410_call = mod.get_global_var('func_410')
func_414_call = mutated_mod.get_global_var('func_414')
var_1670 = relay.var("var_1670", dtype = "float32", shape = (260,))#candidate|1670|(260,)|var|float32
call_1669 = relay.TupleGetItem(func_410_call(relay.reshape(var_1670.astype('float32'), [13, 10, 2]), relay.reshape(var_1670.astype('float32'), [13, 10, 2]), relay.reshape(var_1670.astype('float32'), [13, 10, 2]), ), 0)
call_1671 = relay.TupleGetItem(func_414_call(relay.reshape(var_1670.astype('float32'), [13, 10, 2]), relay.reshape(var_1670.astype('float32'), [13, 10, 2]), relay.reshape(var_1670.astype('float32'), [13, 10, 2]), ), 0)
output = relay.Tuple([call_1628,call_1669,var_1670,])
output2 = relay.Tuple([call_1629,call_1671,var_1670,])
func_1683 = relay.Function([var_1670,], output)
mod['func_1683'] = func_1683
mod = relay.transform.InferType()(mod)
var_1684 = relay.var("var_1684", dtype = "float32", shape = (260,))#candidate|1684|(260,)|var|float32
output = func_1683(var_1684)
func_1685 = relay.Function([var_1684], output)
mutated_mod['func_1685'] = func_1685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_1707 = relay.TupleGetItem(func_1578_call(), 0)
call_1708 = relay.TupleGetItem(func_1579_call(), 0)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_1711 = relay.TupleGetItem(func_1578_call(), 0)
call_1712 = relay.TupleGetItem(func_1579_call(), 0)
uop_1713 = relay.cosh(call_1711.astype('float64')) # shape=(13, 10, 2)
uop_1715 = relay.cosh(call_1712.astype('float64')) # shape=(13, 10, 2)
func_600_call = mod.get_global_var('func_600')
func_602_call = mutated_mod.get_global_var('func_602')
call_1730 = relay.TupleGetItem(func_600_call(), 0)
call_1731 = relay.TupleGetItem(func_602_call(), 0)
output = relay.Tuple([call_1707,uop_1713,call_1730,])
output2 = relay.Tuple([call_1708,uop_1715,call_1731,])
func_1733 = relay.Function([], output)
mod['func_1733'] = func_1733
mod = relay.transform.InferType()(mod)
mutated_mod['func_1733'] = func_1733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1733_call = mutated_mod.get_global_var('func_1733')
call_1734 = func_1733_call()
output = call_1734
func_1735 = relay.Function([], output)
mutated_mod['func_1735'] = func_1735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1513_call = mod.get_global_var('func_1513')
func_1515_call = mutated_mod.get_global_var('func_1515')
call_1744 = relay.TupleGetItem(func_1513_call(), 1)
call_1745 = relay.TupleGetItem(func_1515_call(), 1)
var_1746 = relay.var("var_1746", dtype = "float64", shape = (16, 7, 8))#candidate|1746|(16, 7, 8)|var|float64
bop_1747 = relay.bitwise_and(call_1744.astype('int64'), relay.reshape(var_1746.astype('int64'), relay.shape_of(call_1744))) # shape=(16, 7, 8)
bop_1750 = relay.bitwise_and(call_1745.astype('int64'), relay.reshape(var_1746.astype('int64'), relay.shape_of(call_1745))) # shape=(16, 7, 8)
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_1760 = relay.TupleGetItem(func_1733_call(), 1)
call_1761 = relay.TupleGetItem(func_1735_call(), 1)
output = relay.Tuple([bop_1747,call_1760,])
output2 = relay.Tuple([bop_1750,call_1761,])
func_1764 = relay.Function([var_1746,], output)
mod['func_1764'] = func_1764
mod = relay.transform.InferType()(mod)
mutated_mod['func_1764'] = func_1764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1765 = relay.var("var_1765", dtype = "float64", shape = (16, 7, 8))#candidate|1765|(16, 7, 8)|var|float64
func_1764_call = mutated_mod.get_global_var('func_1764')
call_1766 = func_1764_call(var_1765)
output = call_1766
func_1767 = relay.Function([var_1765], output)
mutated_mod['func_1767'] = func_1767
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1797 = relay.var("var_1797", dtype = "float64", shape = (9, 1, 5))#candidate|1797|(9, 1, 5)|var|float64
uop_1798 = relay.sqrt(var_1797.astype('float64')) # shape=(9, 1, 5)
output = relay.Tuple([uop_1798,])
output2 = relay.Tuple([uop_1798,])
func_1805 = relay.Function([var_1797,], output)
mod['func_1805'] = func_1805
mod = relay.transform.InferType()(mod)
var_1806 = relay.var("var_1806", dtype = "float64", shape = (9, 1, 5))#candidate|1806|(9, 1, 5)|var|float64
output = func_1805(var_1806)
func_1807 = relay.Function([var_1806], output)
mutated_mod['func_1807'] = func_1807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1513_call = mod.get_global_var('func_1513')
func_1515_call = mutated_mod.get_global_var('func_1515')
call_1892 = relay.TupleGetItem(func_1513_call(), 1)
call_1893 = relay.TupleGetItem(func_1515_call(), 1)
output = relay.Tuple([call_1892,])
output2 = relay.Tuple([call_1893,])
func_1894 = relay.Function([], output)
mod['func_1894'] = func_1894
mod = relay.transform.InferType()(mod)
mutated_mod['func_1894'] = func_1894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1894_call = mutated_mod.get_global_var('func_1894')
call_1895 = func_1894_call()
output = call_1895
func_1896 = relay.Function([], output)
mutated_mod['func_1896'] = func_1896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_926_call = mutated_mod.get_global_var('func_926')
call_1914 = func_925_call()
call_1915 = func_925_call()
output = relay.Tuple([call_1914,])
output2 = relay.Tuple([call_1915,])
func_1916 = relay.Function([], output)
mod['func_1916'] = func_1916
mod = relay.transform.InferType()(mod)
mutated_mod['func_1916'] = func_1916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1916_call = mutated_mod.get_global_var('func_1916')
call_1917 = func_1916_call()
output = call_1917
func_1918 = relay.Function([], output)
mutated_mod['func_1918'] = func_1918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_926_call = mutated_mod.get_global_var('func_926')
call_1925 = func_925_call()
call_1926 = func_925_call()
const_1931 = relay.const([[[4.324388,1.261429,7.733393,7.075393,-4.939320,9.343120,-7.275699,-3.098948],[2.587819,-4.890880,-5.953881,2.711510,-6.194138,6.272400,8.264957,-0.006738],[5.948570,6.692339,2.868780,8.865113,-3.805087,6.170673,-5.496717,8.832275],[2.598100,-5.751701,8.574906,-2.771779,-0.050443,-5.467964,-7.421752,-3.197286],[-9.733630,-4.437283,-5.470113,-0.704946,-6.531211,7.922738,8.984970,5.945635],[-0.423065,-5.696820,4.481708,-2.256304,6.899613,-0.578432,0.748181,6.578968],[-5.803659,9.691813,1.908027,6.266414,-4.214255,-6.445305,1.034068,-9.324718]],[[9.861818,-6.121722,3.124079,-6.758882,0.169286,-1.694721,0.290812,9.010247],[4.431568,-3.390013,-6.363186,-9.690583,-8.649924,-4.192970,-5.759420,-7.763276],[-6.561823,5.128790,6.102649,-9.001551,-0.516585,4.685592,-9.325516,6.544817],[-7.510378,-5.832006,-3.428835,6.887786,-5.171833,-4.342006,-7.463604,-6.837634],[8.451675,-1.348928,-8.406398,-5.026469,9.236339,-9.826257,-3.856479,3.697732],[-3.521518,0.676894,-2.741229,1.185553,-7.558988,-8.917296,-8.074979,8.023147],[-7.482560,-6.857419,-7.442048,1.857286,1.427021,6.877066,2.290363,-9.701268]],[[7.530934,-4.562722,-1.405300,-5.500242,-7.572683,0.402132,3.656956,-7.968656],[-3.695351,-6.166308,3.376662,-2.978405,-2.066984,-8.993113,-8.077521,8.400575],[-3.122676,9.124900,6.018314,-8.689596,-9.694197,8.525190,-9.942385,0.402640],[-9.045140,-9.645718,0.064622,-6.242982,-3.093088,-0.261692,7.238756,-9.176589],[4.415139,-3.840519,5.934116,-3.902275,-8.117315,-1.501657,-6.874435,4.461854],[0.232227,-0.359377,-7.655751,-0.818572,-3.007016,5.986352,-5.400811,6.268928],[-4.232759,5.681989,-8.774512,2.572659,2.206081,-3.235819,-5.035069,-4.703419]],[[7.174010,-2.423028,-3.797707,-2.738747,6.033449,-1.586563,-1.980148,-5.840598],[-6.644387,-7.470843,2.170543,1.845743,8.255094,-1.705931,-3.124734,-9.981391],[-9.643326,1.993020,3.493998,0.853286,-3.916024,9.958735,4.305735,6.990374],[5.367062,0.892884,1.064846,8.553312,-7.234053,-3.725971,-8.178484,-2.464097],[-2.259374,3.426673,3.806920,-1.229792,0.081604,-9.086219,1.753312,-0.464057],[-0.943648,-6.212780,-3.039913,-4.935214,0.669487,4.131239,1.643838,-2.274540],[-4.234324,-8.571952,-0.106800,0.805844,-0.762205,3.115714,1.492281,-7.402181]],[[3.993327,1.384666,-2.990232,-7.707802,4.643329,6.964059,0.609117,-0.816101],[-8.889913,2.594525,0.913669,-5.669705,4.503923,-1.984555,4.370069,-8.479020],[7.482346,-9.264797,2.742906,9.696967,2.578182,-8.444830,1.149626,-4.987745],[6.929283,-0.876621,-0.383764,-9.979433,-0.434931,-5.773908,7.604535,-2.714637],[-2.772353,-6.134630,8.027126,-3.413984,-6.784179,6.549757,0.862316,2.611796],[-4.926095,-6.837053,-6.951606,-1.992747,0.142822,-5.238240,9.712063,5.869080],[-5.885685,6.527157,3.971300,-9.234289,-0.267198,7.197873,5.956929,-3.393656]],[[7.697789,-0.139525,6.611223,-4.163445,3.410769,6.917987,-6.241981,-8.907678],[-9.918851,-3.653501,-3.368093,-0.890023,3.277680,-7.159202,-9.122931,-2.931794],[2.633896,-5.292041,9.969840,9.174047,3.913353,7.193792,6.493739,-3.751973],[9.584461,-7.954050,1.665798,4.988202,-0.451630,1.557752,-7.562329,-4.246603],[-2.881775,6.479380,-3.773299,-1.426701,9.429738,2.802012,-5.980325,9.882353],[-9.529340,6.140115,-9.196853,-8.651365,-5.909660,2.082549,5.793324,9.925490],[-1.247331,9.845358,4.988253,6.845926,8.573349,-4.835254,-6.718036,-7.697864]],[[2.989827,0.936159,-1.330061,-9.019396,7.908311,9.624227,-6.711605,9.160570],[2.771079,6.505686,-9.761066,-5.482314,6.798165,6.604869,-9.663127,-5.233972],[8.317141,1.006312,-9.705980,8.307536,4.308283,-5.368732,5.796823,4.426010],[1.672491,5.957359,9.284611,5.548941,-9.419890,-7.895679,-0.989476,-2.591211],[-0.283087,6.420227,-4.199058,3.431772,-6.230343,5.710742,9.339191,-3.660684],[5.868601,-6.626217,4.563607,1.620265,0.308136,-3.200129,-5.748491,7.953979],[-9.557639,7.145461,6.893851,6.241705,2.193094,8.137127,9.945520,0.203178]],[[-1.833390,9.450359,1.210931,1.678376,-0.089061,1.198938,1.635906,-8.843359],[4.096670,-2.151416,-1.533712,-1.072742,-9.900424,-4.002470,-3.362340,-6.123033],[1.782008,-5.751173,-0.357017,7.928563,-8.317622,5.024676,-0.696274,8.015753],[-8.169972,-6.384437,4.878314,-4.755331,2.928797,9.330027,-1.121126,-8.187912],[5.901502,-6.011799,-1.538429,4.946043,-7.344665,-2.980608,-9.073942,4.729046],[8.391613,0.278869,-1.409142,-2.993266,-1.040476,1.511644,8.633900,-9.908445],[1.999090,-5.406405,0.035060,-9.156498,4.551360,-4.387862,-2.987523,-4.661046]],[[3.751770,6.324275,0.811183,8.724916,6.881440,-3.114845,-6.457225,-0.495585],[9.877770,-7.689756,-7.768582,3.726345,0.457667,9.062510,3.595253,-3.384050],[4.977252,-4.851288,4.650632,-9.863542,6.182808,-0.639126,1.035207,1.663204],[9.261274,4.820099,-4.683723,6.016537,-9.651155,9.982501,-9.236589,1.325294],[0.217823,-7.539111,0.896695,-9.250695,1.536147,2.943916,8.341957,-3.638594],[-1.037149,-7.647606,-6.317801,-1.660948,-5.933059,-0.994335,2.965935,-9.291313],[1.776299,-0.342893,1.198233,7.961462,3.112714,2.115822,9.809618,2.224174]],[[-2.721883,-9.135166,-8.799815,7.617576,6.560401,7.960218,3.136031,9.400055],[7.269525,-6.077209,-9.405890,6.827848,-8.602925,-2.784057,-5.982813,7.257662],[6.376210,6.122380,-3.809867,-7.078201,-6.205714,0.776618,9.262856,4.646482],[-1.373220,8.233472,2.978588,-8.947583,-4.264278,-2.902501,-7.757549,5.259638],[2.199483,7.351440,2.545957,2.398351,-7.820773,-6.983966,-6.200407,-9.793315],[8.538647,2.043259,-6.775803,-2.373914,6.962988,-7.062842,-9.532180,9.151903],[-3.144297,8.605792,2.228563,-0.195929,0.949503,7.931030,-4.050425,-5.786176]],[[-9.513658,-0.535266,0.155550,8.368305,7.029231,7.832157,2.261927,-2.770237],[8.908302,2.825891,-8.096356,-4.915191,-4.871657,1.904977,2.629113,-7.875144],[-7.978002,6.319444,3.440557,-4.894981,-8.076107,-5.066520,-4.871397,5.722945],[7.797500,-1.063918,-7.976550,2.161796,7.960894,1.280105,8.807567,-2.815345],[2.618680,2.058076,-9.807423,6.137132,1.520154,-5.583769,-5.113547,-8.729259],[-1.489820,-8.321652,0.151888,-0.536581,-6.791365,-6.300635,8.529826,0.856679],[-6.870013,-3.394427,-7.494645,7.495061,8.989886,-3.091991,3.116165,7.153093]],[[4.186574,4.017941,-7.522230,1.602567,3.902323,-6.167638,-1.744982,6.876921],[-9.109002,7.622606,-7.254613,2.305113,-9.974129,4.902223,-7.336387,-5.648517],[-3.367945,-0.116620,6.667554,-8.377695,0.028172,0.943591,-7.533572,-5.597136],[-4.966482,-2.751544,-6.562616,2.254002,8.988498,5.389409,0.470693,3.992565],[8.451274,-4.815487,-4.124256,6.727167,9.785445,7.312071,-4.987182,5.082534],[-8.442056,7.989305,4.512928,8.543840,1.168863,-6.983280,-1.850545,1.668148],[8.816124,-1.368044,-7.064451,-2.578823,0.678336,0.181192,8.490031,-6.337988]]], dtype = "float32")#candidate|1931|(12, 7, 8)|const|float32
bop_1932 = relay.equal(call_1925.astype('bool'), const_1931.astype('bool')) # shape=(12, 7, 8)
bop_1935 = relay.equal(call_1926.astype('bool'), const_1931.astype('bool')) # shape=(12, 7, 8)
uop_1941 = relay.atanh(call_1925.astype('float64')) # shape=(1, 7, 8)
uop_1943 = relay.atanh(call_1926.astype('float64')) # shape=(1, 7, 8)
func_925_call = mod.get_global_var('func_925')
func_926_call = mutated_mod.get_global_var('func_926')
call_1945 = func_925_call()
call_1946 = func_925_call()
bop_1948 = relay.equal(uop_1941.astype('bool'), relay.reshape(call_1925.astype('bool'), relay.shape_of(uop_1941))) # shape=(1, 7, 8)
bop_1951 = relay.equal(uop_1943.astype('bool'), relay.reshape(call_1926.astype('bool'), relay.shape_of(uop_1943))) # shape=(1, 7, 8)
var_1955 = relay.var("var_1955", dtype = "bool", shape = (10, 7, 8))#candidate|1955|(10, 7, 8)|var|bool
bop_1956 = relay.bitwise_or(bop_1948.astype('uint16'), var_1955.astype('uint16')) # shape=(10, 7, 8)
bop_1959 = relay.bitwise_or(bop_1951.astype('uint16'), var_1955.astype('uint16')) # shape=(10, 7, 8)
uop_1965 = relay.sinh(const_1931.astype('float64')) # shape=(12, 7, 8)
output = relay.Tuple([bop_1932,call_1945,bop_1956,uop_1965,])
output2 = relay.Tuple([bop_1935,call_1946,bop_1959,uop_1965,])
func_1967 = relay.Function([var_1955,], output)
mod['func_1967'] = func_1967
mod = relay.transform.InferType()(mod)
var_1968 = relay.var("var_1968", dtype = "bool", shape = (10, 7, 8))#candidate|1968|(10, 7, 8)|var|bool
output = func_1967(var_1968)
func_1969 = relay.Function([var_1968], output)
mutated_mod['func_1969'] = func_1969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_2034 = relay.TupleGetItem(func_1071_call(), 0)
call_2035 = relay.TupleGetItem(func_1073_call(), 0)
func_1805_call = mod.get_global_var('func_1805')
func_1807_call = mutated_mod.get_global_var('func_1807')
var_2045 = relay.var("var_2045", dtype = "float64", shape = (1, 45))#candidate|2045|(1, 45)|var|float64
call_2044 = relay.TupleGetItem(func_1805_call(relay.reshape(var_2045.astype('float64'), [9, 1, 5])), 0)
call_2046 = relay.TupleGetItem(func_1807_call(relay.reshape(var_2045.astype('float64'), [9, 1, 5])), 0)
output = relay.Tuple([call_2034,call_2044,var_2045,])
output2 = relay.Tuple([call_2035,call_2046,var_2045,])
func_2053 = relay.Function([var_2045,], output)
mod['func_2053'] = func_2053
mod = relay.transform.InferType()(mod)
mutated_mod['func_2053'] = func_2053
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2054 = relay.var("var_2054", dtype = "float64", shape = (1, 45))#candidate|2054|(1, 45)|var|float64
func_2053_call = mutated_mod.get_global_var('func_2053')
call_2055 = func_2053_call(var_2054)
output = call_2055
func_2056 = relay.Function([var_2054], output)
mutated_mod['func_2056'] = func_2056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1317_call = mutated_mod.get_global_var('func_1317')
call_2067 = relay.TupleGetItem(func_1316_call(), 0)
call_2068 = relay.TupleGetItem(func_1317_call(), 0)
uop_2092 = relay.sinh(call_2067.astype('float32')) # shape=(1, 7, 8)
uop_2094 = relay.sinh(call_2068.astype('float32')) # shape=(1, 7, 8)
func_1052_call = mod.get_global_var('func_1052')
func_1055_call = mutated_mod.get_global_var('func_1055')
const_2105 = relay.const([0.381746,-1.103536,9.600798,9.403785,8.716484,-7.850000,-8.112224,5.628291,-3.776955,-9.055335,9.522929,-5.995533,9.577295,1.148172,2.245815,-6.207415,5.161122,-1.610260,1.706472,6.389762,8.793546,6.007078,3.142854,-4.232776,-6.641954,-8.124440,-3.102446,0.551944,-9.458536,-6.757113,0.262903,-0.168303,5.404284,4.894885,3.185735,0.958879,-4.516027,-3.117835,-2.456508,-3.650035,3.729551,-0.399145,8.488696,0.495292,-5.441368,3.791536,-3.852948,-6.507901,5.744393,3.238846,-1.323982,1.542201,1.225223,6.567366,-7.393988,-2.673445,-8.030992,9.377084,7.456500,9.820803,-3.352333,6.087540,2.036686,-2.498975,-9.274436,9.309599,7.493239,5.388992,-9.484619,-9.119878,-1.951205,1.353177,3.415590,-7.993813,5.411801,0.581364,9.117784,3.267787,-9.070275,5.206323,0.342628,-5.989215,8.268799,4.701970,-2.984553,-7.768576,-3.026459,1.433583,6.638607,-2.008387,-5.608482,-6.842005,7.561645,-5.945682,-6.588626,-2.755928,-0.949774,-0.907405,-1.858961,9.166083,3.951092,-4.773142,3.674117,3.750338,7.021002,-3.453237,0.986851,9.989899,-9.636913,5.779916,2.719387,-6.470166,-6.146678,3.448951,-7.590022,2.737871,8.421820,0.965295,3.080036,6.736053,2.661257,-9.811176,-8.435777,5.351658,9.664605,8.007649,-6.944775,-0.580107,-0.717326,8.327832,2.215163,-5.930284,-7.607966,1.985716,0.313634,2.463908,-1.181283,6.313348,8.527947,5.193040,7.797662,-5.315829,-5.619257,-9.287442,-6.353939,8.552162,-3.954015,-7.125820,-3.473773,1.027435,-0.411673,-6.457953,-0.170708,-9.638392,-7.426833,1.229023,-0.034382,6.419803,-3.169813,-5.164664,3.655297,-6.483443,9.032240,3.577338,8.026391,8.046231,7.632291,-5.876003,-3.341180,6.116329,6.369552,-1.385179,-3.520880,-2.112779,-2.664368,-2.319633,3.599237,9.803866,7.082088,-7.597396,4.956313,7.860794,4.664857,8.163666,-9.669678,-3.637171,6.897189,2.660803,-8.391807,-5.407561,-3.378375,-7.290833,-3.810712,7.657671,-8.216857,-3.024424,2.029920,-3.224443,0.423533,-2.441623,6.191151,4.801367,-7.593145,-3.471601,0.136748,1.794966,3.714646,3.343635,5.715807,-7.011950,-6.715633,-2.939321,-5.085224,-9.676774,-9.633410,1.573768,6.554601,-1.104672,5.596861,-8.652269,2.790234,9.917363,2.064424,-8.219337,7.457087,1.045161,6.698186,0.099226,-5.434873,-8.701278,7.989758,-9.366309,-8.314870,-6.818775,-5.305438,-6.563257,-4.141754,-4.625573,-9.667084,-7.936507,0.160851,1.573676,6.993986,-1.088258,-8.305290,-3.937047,-2.067350,-2.645665,8.083462,7.481412,5.067771,-2.137217,4.843859,-5.484119,6.853202,1.404018,-2.870026,-5.126504,4.957566,6.375558,7.682396,7.185992,0.413789,-5.866072,-7.036017,-3.925246,-5.090756,3.272739,9.257519,7.455535,6.968029,-8.983709,-8.804607,7.687815,0.013779,6.909493,0.234607,0.808791,0.836174,6.186940,4.367241,7.813906,-2.668440,1.655553,-8.913228,3.681682,0.423897,6.647148,-7.937044,8.811515,-3.615085,-7.112756,-9.601490,-8.351091,5.929846,0.472018,6.749902,-8.047284,-7.861695,9.997076,7.717971,-2.294019,-1.685388,-1.093527,-0.256945,1.747821,-3.234445,-0.967799,2.097765,-0.492513,6.761368,8.141354,0.483090,-4.877387,2.562876,-1.794374,-5.995401,0.477295,4.690562,2.177164,9.314342,-5.294994,-8.568842,-2.094387,0.014012,8.958959,2.139994,6.980588,-8.004500,-2.538516,4.496455,-1.668518,7.434922,5.935103,9.143832,-6.959199,3.757181,7.791564,-7.208121,0.716117,-8.567357,-9.806090,9.941807,-1.548648,3.240363,6.700557,-0.849867,3.140800,2.712223,-1.860029,5.072552,6.184811,2.058900,1.397447,5.300186,9.874093,7.244609,6.164961,5.177764,-1.533166,-0.906106,8.373217,-0.267609,-4.560426], dtype = "float32")#candidate|2105|(364,)|const|float32
const_2106 = relay.const([[2.362429],[-7.753045],[-0.224991],[4.080046],[-7.234880],[2.152814],[8.678027],[6.937916],[-7.546917],[7.592922],[-9.391427],[-4.006421],[7.640714],[4.392466],[-6.773628],[-3.984986],[0.475100],[-7.211826],[-1.180241],[9.226807],[-2.174549],[-8.066793],[9.024958],[-7.666869],[2.458936],[-1.642515],[5.169102],[-9.019909],[-6.782167],[-1.525177],[-0.195783],[1.982326],[-2.355358],[-9.194159],[1.539781],[0.848721],[-0.132347],[-7.387557],[3.734362],[2.903545],[-1.908036],[6.196130],[-0.197588],[8.177463],[2.465208],[-9.031952],[-9.504902],[-0.377262],[1.467742],[3.580162],[-9.957970],[0.131449],[-5.470939],[3.830344],[-9.952100],[-4.903919],[-4.350452],[-2.523519],[1.388008],[4.337056],[9.663783],[-8.150861],[0.243224],[-2.878534],[7.287381],[-4.002579],[-6.335436],[7.499710],[7.738655],[6.318614],[3.246079],[-7.927172],[6.619877],[1.498394],[-5.107180],[1.158567],[-0.175631],[2.772679],[-5.920138],[-9.286206],[5.253762],[-1.745607],[-1.682884],[-1.686240],[-6.892643],[7.855756],[4.231419],[2.713457],[-8.522490],[5.432481]], dtype = "float64")#candidate|2106|(90, 1)|const|float64
call_2104 = relay.TupleGetItem(func_1052_call(relay.reshape(const_2105.astype('float32'), [13, 14, 2]), relay.reshape(const_2106.astype('float64'), [90,]), ), 0)
call_2107 = relay.TupleGetItem(func_1055_call(relay.reshape(const_2105.astype('float32'), [13, 14, 2]), relay.reshape(const_2106.astype('float64'), [90,]), ), 0)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_2108 = relay.TupleGetItem(func_1894_call(), 0)
call_2109 = relay.TupleGetItem(func_1896_call(), 0)
func_495_call = mod.get_global_var('func_495')
func_496_call = mutated_mod.get_global_var('func_496')
call_2113 = func_495_call()
call_2114 = func_495_call()
output = relay.Tuple([uop_2092,call_2104,const_2105,const_2106,call_2108,call_2113,])
output2 = relay.Tuple([uop_2094,call_2107,const_2105,const_2106,call_2109,call_2114,])
func_2122 = relay.Function([], output)
mod['func_2122'] = func_2122
mod = relay.transform.InferType()(mod)
mutated_mod['func_2122'] = func_2122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2122_call = mutated_mod.get_global_var('func_2122')
call_2123 = func_2122_call()
output = call_2123
func_2124 = relay.Function([], output)
mutated_mod['func_2124'] = func_2124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_2160 = relay.TupleGetItem(func_1894_call(), 0)
call_2161 = relay.TupleGetItem(func_1896_call(), 0)
output = relay.Tuple([call_2160,])
output2 = relay.Tuple([call_2161,])
func_2164 = relay.Function([], output)
mod['func_2164'] = func_2164
mod = relay.transform.InferType()(mod)
output = func_2164()
func_2165 = relay.Function([], output)
mutated_mod['func_2165'] = func_2165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_2264 = relay.TupleGetItem(func_1071_call(), 0)
call_2265 = relay.TupleGetItem(func_1073_call(), 0)
uop_2276 = relay.cos(call_2264.astype('float32')) # shape=(1, 7, 8)
uop_2278 = relay.cos(call_2265.astype('float32')) # shape=(1, 7, 8)
func_1513_call = mod.get_global_var('func_1513')
func_1515_call = mutated_mod.get_global_var('func_1515')
call_2286 = relay.TupleGetItem(func_1513_call(), 3)
call_2287 = relay.TupleGetItem(func_1515_call(), 3)
output = relay.Tuple([uop_2276,call_2286,])
output2 = relay.Tuple([uop_2278,call_2287,])
func_2291 = relay.Function([], output)
mod['func_2291'] = func_2291
mod = relay.transform.InferType()(mod)
mutated_mod['func_2291'] = func_2291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2291_call = mutated_mod.get_global_var('func_2291')
call_2292 = func_2291_call()
output = call_2292
func_2293 = relay.Function([], output)
mutated_mod['func_2293'] = func_2293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_2314 = relay.TupleGetItem(func_1578_call(), 1)
call_2315 = relay.TupleGetItem(func_1579_call(), 1)
const_2318 = relay.const([[[6,-8,6,-2,10,7,-10,5],[-5,7,-9,-10,9,1,3,2],[10,4,3,-10,3,-10,-8,-10],[-5,4,9,6,1,-6,3,-6],[5,-8,-9,3,8,4,-8,8],[3,-9,9,-2,3,7,-3,-9],[-4,-9,7,-2,3,8,2,7]],[[1,-2,3,3,10,-2,-2,3],[9,-6,4,-9,5,8,-7,-5],[-3,1,8,2,1,-5,6,-8],[10,9,-3,10,-8,-7,5,5],[6,-4,9,6,-1,-4,9,-9],[-7,2,9,-10,-10,5,-9,-3],[-6,1,4,-7,10,-1,-3,-7]],[[-1,4,1,-8,-1,6,3,4],[8,-5,5,-9,-3,-4,-1,1],[-2,-1,-7,3,1,-7,-1,-4],[-6,-3,-2,6,3,4,-2,3],[9,6,4,-5,1,1,-3,-10],[5,2,6,-5,-1,-10,-5,7],[-8,10,-4,-6,7,4,-2,10]],[[6,7,3,8,4,-5,2,2],[6,-9,-9,3,2,-5,-2,2],[-9,1,-4,4,-8,6,2,9],[4,-8,2,-6,-9,-9,-5,2],[-1,-6,1,-2,8,10,-7,-7],[6,1,-7,4,-7,-8,3,8],[2,-8,5,-5,-7,-4,3,-5]],[[-7,8,-3,-1,-3,-7,-10,10],[-9,6,-8,9,-5,8,-4,-6],[9,-6,-6,5,9,-8,6,-2],[8,-1,6,-10,10,-8,2,7],[8,6,-4,5,-2,4,-1,-5],[2,-5,-5,-1,4,-1,-3,-10],[6,5,6,5,3,5,4,4]],[[7,6,6,-7,7,9,-10,3],[4,6,-7,7,10,5,4,-10],[9,-3,3,5,9,2,-2,5],[-2,-7,2,1,8,6,5,2],[-1,-9,4,6,8,3,2,8],[-1,-5,9,-4,3,-8,3,-2],[-5,-1,-5,-4,-9,-2,7,7]],[[5,10,9,8,4,-10,-5,3],[3,1,-5,10,-6,-4,-4,-2],[4,-2,5,-5,-5,-6,-9,-2],[-5,2,-2,3,-7,-10,10,10],[3,7,2,-7,-8,9,1,2],[6,5,8,-5,-5,-8,6,-8],[-9,-7,6,-10,-6,-2,2,-3]],[[5,8,8,-10,8,-7,-5,-5],[10,7,-5,-10,8,8,-3,-10],[-2,4,4,2,-2,-8,6,3],[-7,-3,9,-5,-5,-1,-7,1],[-1,-7,10,7,-2,9,10,5],[-2,2,-4,-10,-2,-1,2,-8],[8,-8,-7,-10,-9,9,3,-7]],[[-4,6,-7,-9,9,-8,2,6],[3,10,-6,-1,3,4,-3,1],[-1,-7,5,-9,-6,7,-5,9],[6,8,-4,-7,-8,-1,4,-2],[8,5,-5,-2,-3,8,2,8],[1,-10,-6,1,9,-6,-3,10],[-8,-9,-1,-4,9,-6,1,9]]], dtype = "int64")#candidate|2318|(9, 7, 8)|const|int64
bop_2319 = relay.maximum(call_2314.astype('uint32'), const_2318.astype('uint32')) # shape=(9, 7, 8)
bop_2322 = relay.maximum(call_2315.astype('uint32'), const_2318.astype('uint32')) # shape=(9, 7, 8)
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_2325 = relay.TupleGetItem(func_1733_call(), 1)
call_2326 = relay.TupleGetItem(func_1735_call(), 1)
output = relay.Tuple([bop_2319,call_2325,])
output2 = relay.Tuple([bop_2322,call_2326,])
func_2334 = relay.Function([], output)
mod['func_2334'] = func_2334
mod = relay.transform.InferType()(mod)
mutated_mod['func_2334'] = func_2334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2334_call = mutated_mod.get_global_var('func_2334')
call_2335 = func_2334_call()
output = call_2335
func_2336 = relay.Function([], output)
mutated_mod['func_2336'] = func_2336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1260_call = mod.get_global_var('func_1260')
func_1262_call = mutated_mod.get_global_var('func_1262')
call_2375 = relay.TupleGetItem(func_1260_call(), 1)
call_2376 = relay.TupleGetItem(func_1262_call(), 1)
output = relay.Tuple([call_2375,])
output2 = relay.Tuple([call_2376,])
func_2391 = relay.Function([], output)
mod['func_2391'] = func_2391
mod = relay.transform.InferType()(mod)
output = func_2391()
func_2392 = relay.Function([], output)
mutated_mod['func_2392'] = func_2392
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2399 = relay.const(-3, dtype = "uint8")#candidate|2399|()|const|uint8
var_2400 = relay.var("var_2400", dtype = "uint8", shape = (9, 3, 12))#candidate|2400|(9, 3, 12)|var|uint8
bop_2401 = relay.maximum(const_2399.astype('uint8'), var_2400.astype('uint8')) # shape=(9, 3, 12)
output = bop_2401
output2 = bop_2401
func_2411 = relay.Function([var_2400,], output)
mod['func_2411'] = func_2411
mod = relay.transform.InferType()(mod)
mutated_mod['func_2411'] = func_2411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2412 = relay.var("var_2412", dtype = "uint8", shape = (9, 3, 12))#candidate|2412|(9, 3, 12)|var|uint8
func_2411_call = mutated_mod.get_global_var('func_2411')
call_2413 = func_2411_call(var_2412)
output = call_2413
func_2414 = relay.Function([var_2412], output)
mutated_mod['func_2414'] = func_2414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_2444 = relay.TupleGetItem(func_1894_call(), 0)
call_2445 = relay.TupleGetItem(func_1896_call(), 0)
uop_2467 = relay.sigmoid(call_2444.astype('float32')) # shape=(16, 7, 8)
uop_2469 = relay.sigmoid(call_2445.astype('float32')) # shape=(16, 7, 8)
var_2472 = relay.var("var_2472", dtype = "float64", shape = (16, 7, 8))#candidate|2472|(16, 7, 8)|var|float64
bop_2473 = relay.greater_equal(call_2444.astype('bool'), relay.reshape(var_2472.astype('bool'), relay.shape_of(call_2444))) # shape=(16, 7, 8)
bop_2476 = relay.greater_equal(call_2445.astype('bool'), relay.reshape(var_2472.astype('bool'), relay.shape_of(call_2445))) # shape=(16, 7, 8)
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
var_2478 = relay.var("var_2478", dtype = "float64", shape = (56,))#candidate|2478|(56,)|var|float64
call_2477 = relay.TupleGetItem(func_1421_call(relay.reshape(var_2478.astype('float64'), [1, 7, 8])), 8)
call_2479 = relay.TupleGetItem(func_1424_call(relay.reshape(var_2478.astype('float64'), [1, 7, 8])), 8)
output = relay.Tuple([uop_2467,bop_2473,call_2477,var_2478,])
output2 = relay.Tuple([uop_2469,bop_2476,call_2479,var_2478,])
func_2490 = relay.Function([var_2472,var_2478,], output)
mod['func_2490'] = func_2490
mod = relay.transform.InferType()(mod)
mutated_mod['func_2490'] = func_2490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2490_call = mutated_mod.get_global_var('func_2490')
var_2492 = relay.var("var_2492", dtype = "float64", shape = (16, 7, 8))#candidate|2492|(16, 7, 8)|var|float64
var_2493 = relay.var("var_2493", dtype = "float64", shape = (56,))#candidate|2493|(56,)|var|float64
call_2491 = func_2490_call(var_2492,var_2493,)
output = call_2491
func_2494 = relay.Function([var_2492,var_2493,], output)
mutated_mod['func_2494'] = func_2494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2291_call = mod.get_global_var('func_2291')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_2579 = relay.TupleGetItem(func_2291_call(), 1)
call_2580 = relay.TupleGetItem(func_2293_call(), 1)
output = call_2579
output2 = call_2580
func_2584 = relay.Function([], output)
mod['func_2584'] = func_2584
mod = relay.transform.InferType()(mod)
output = func_2584()
func_2585 = relay.Function([], output)
mutated_mod['func_2585'] = func_2585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1513_call = mod.get_global_var('func_1513')
func_1515_call = mutated_mod.get_global_var('func_1515')
call_2638 = relay.TupleGetItem(func_1513_call(), 3)
call_2639 = relay.TupleGetItem(func_1515_call(), 3)
output = call_2638
output2 = call_2639
func_2643 = relay.Function([], output)
mod['func_2643'] = func_2643
mod = relay.transform.InferType()(mod)
output = func_2643()
func_2644 = relay.Function([], output)
mutated_mod['func_2644'] = func_2644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_495_call = mod.get_global_var('func_495')
func_496_call = mutated_mod.get_global_var('func_496')
call_2658 = func_495_call()
call_2659 = func_495_call()
uop_2670 = relay.sqrt(call_2658.astype('float32')) # shape=(1, 7, 8)
uop_2672 = relay.sqrt(call_2659.astype('float32')) # shape=(1, 7, 8)
output = relay.Tuple([uop_2670,])
output2 = relay.Tuple([uop_2672,])
func_2675 = relay.Function([], output)
mod['func_2675'] = func_2675
mod = relay.transform.InferType()(mod)
output = func_2675()
func_2676 = relay.Function([], output)
mutated_mod['func_2676'] = func_2676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2731 = relay.var("var_2731", dtype = "float64", shape = (16, 1, 2))#candidate|2731|(16, 1, 2)|var|float64
const_2732 = relay.const([[[-1.832107,-6.919322],[-9.959684,-3.295828],[1.225139,4.978635],[-8.082472,6.246495],[-8.798223,2.490118],[-2.663728,9.062542],[0.298786,-4.523142],[3.908778,-6.230394],[9.583176,-7.226946],[-1.705025,-5.548915],[-9.289366,-7.458322],[-3.627487,5.689222],[1.277121,-7.233320],[5.389435,-9.501447]],[[-7.144441,-4.057190],[-9.765709,0.717543],[4.065280,-4.435602],[-6.965184,8.258558],[-2.308434,-4.050844],[-3.633817,2.461317],[-4.534144,0.485290],[-8.937971,-9.041186],[8.476951,-1.903055],[2.997488,0.470821],[-2.793072,-7.189763],[-6.127539,6.759333],[2.344277,-5.438940],[0.170125,0.594539]],[[5.321060,-7.386044],[1.670199,-5.120228],[9.067995,-9.237580],[-1.028796,-7.973868],[9.090845,-9.233005],[-3.116962,-9.280857],[0.724223,4.223357],[8.544951,-1.181201],[-6.139730,-9.795262],[0.400585,-5.010056],[3.597627,2.449158],[-1.844882,-9.653957],[-6.639004,5.971041],[8.284715,4.074399]],[[-6.774859,5.018631],[3.942092,-3.113445],[-6.377854,4.113372],[2.635564,8.195028],[2.096014,9.710182],[-8.659897,5.090365],[-8.387032,1.514064],[1.485912,-5.455534],[-1.781849,5.286565],[5.665031,3.297992],[-1.877245,1.885028],[-6.478492,-1.204892],[2.287038,3.472870],[-3.073396,-9.925094]],[[7.014387,-0.928221],[-1.010820,0.275112],[-3.096654,4.466571],[-3.216273,-2.007975],[4.656600,5.967479],[-6.531136,6.817422],[3.873372,5.888295],[-3.726098,-3.323799],[4.033825,-3.964677],[3.129103,-0.957348],[-0.559540,1.782393],[-5.931929,3.474436],[8.807416,5.918273],[-7.770914,1.873532]],[[1.692132,1.898168],[-5.451905,-0.390873],[-2.054437,-4.567402],[-3.353044,-3.050477],[-2.064678,1.302946],[3.879541,-2.559148],[8.590836,-8.105365],[1.506390,0.649645],[-0.670125,-9.677876],[-7.609040,-3.590902],[8.808779,-2.936798],[-8.608747,-0.267322],[-3.787765,5.747004],[-2.859499,-6.117783]],[[-7.598404,3.699306],[-6.226867,-3.731727],[-7.152626,-8.246812],[4.371730,7.216445],[0.099752,-4.537931],[-4.037585,-9.707822],[1.351409,-6.636027],[8.896107,8.407259],[2.990299,6.778971],[-7.203167,-8.845556],[-0.177511,7.297534],[-3.166038,-5.892919],[3.418629,5.710647],[2.364722,-4.418072]],[[9.004859,-8.242747],[-4.236083,-4.254327],[9.173741,4.008187],[-9.262973,-6.897563],[-9.924281,-9.558682],[-0.715814,-3.529948],[-2.038474,-2.560801],[2.916373,-8.045797],[7.439400,-0.769016],[-9.640265,-2.924494],[-0.239756,4.752324],[8.600378,-3.284728],[-3.360652,-7.768602],[9.171526,-3.662472]],[[-7.033035,-2.154882],[8.644934,2.155340],[7.617677,-3.612489],[-9.201813,7.973234],[7.027598,3.801108],[-4.948389,-9.110836],[1.913383,-7.637029],[-9.186271,-1.106403],[7.571986,-7.786908],[0.384491,1.086793],[8.894253,-6.864695],[-8.365063,7.781580],[7.431370,8.842451],[-4.537100,-0.965254]],[[-1.771464,-7.393436],[5.820680,-8.112443],[0.716830,7.420221],[-1.996482,-7.514707],[1.839925,9.185247],[-4.557411,7.477703],[-5.876993,-1.490513],[-2.710913,-5.532393],[0.191074,7.988857],[3.723499,6.053251],[2.939377,4.253234],[1.370114,0.632009],[-2.773419,3.195219],[3.290349,-1.257633]],[[0.393771,-4.418590],[3.246341,-4.368188],[-0.923303,3.881808],[7.079433,-1.711396],[-2.784839,-0.843746],[4.639677,-3.375876],[1.741334,4.966720],[-3.899372,-9.796813],[-1.081221,4.056668],[6.439825,-6.969456],[-2.416909,3.580588],[-0.030653,-7.947929],[3.885460,-4.445572],[-2.916678,-8.342343]],[[-6.474127,5.867665],[-1.056758,-6.883825],[-4.561560,-4.783325],[-6.726970,2.642624],[9.504347,-8.849667],[2.039945,-0.469770],[-1.140088,2.591929],[3.165761,-3.957808],[6.610699,-7.050337],[0.778300,-2.913647],[-8.148472,3.348209],[7.684384,1.448990],[5.339088,-9.317622],[-9.225833,7.590071]],[[-8.773082,-3.219554],[-4.541023,5.377532],[-2.406568,8.626912],[6.097976,3.799982],[6.432960,-9.378853],[-8.051934,3.335554],[5.909203,-8.531805],[-9.530935,-0.103829],[-2.177096,-5.830407],[9.235439,8.597107],[8.511767,5.294014],[-7.209179,-0.643993],[3.443251,2.818383],[9.406502,3.378278]],[[-4.965228,-2.199919],[1.548199,5.198708],[3.853723,4.045412],[-8.394854,-2.490244],[5.809962,-4.521967],[3.895120,4.644480],[4.024964,-5.605280],[6.731752,0.631121],[9.372944,-5.517215],[9.459418,-1.932569],[0.483136,7.740110],[-5.145118,3.915742],[-6.139835,-5.683398],[7.663029,-1.349811]],[[-9.670275,3.880301],[3.209598,9.034511],[-6.809913,9.334259],[-3.861736,8.407743],[5.300047,5.126657],[-9.362220,-5.997494],[-1.884221,-0.586157],[-9.180324,-5.379396],[7.824756,2.918729],[-0.108040,6.738949],[-0.131904,-5.021253],[5.995583,4.195303],[1.316381,-2.036534],[7.655323,-9.640916]],[[3.205901,8.034357],[5.739182,-8.139631],[6.081799,6.533577],[6.476140,8.621025],[-7.971961,-7.295962],[8.986496,-3.261253],[-1.210192,-1.914676],[2.734659,6.315879],[-0.303764,7.165506],[-0.638090,-9.748942],[5.089193,6.247825],[7.647873,-3.614229],[5.918860,5.192726],[-1.199265,6.867664]]], dtype = "float64")#candidate|2732|(16, 14, 2)|const|float64
bop_2733 = relay.power(var_2731.astype('float64'), const_2732.astype('float64')) # shape=(16, 14, 2)
func_2334_call = mod.get_global_var('func_2334')
func_2336_call = mutated_mod.get_global_var('func_2336')
call_2745 = relay.TupleGetItem(func_2334_call(), 1)
call_2746 = relay.TupleGetItem(func_2336_call(), 1)
func_1340_call = mod.get_global_var('func_1340')
func_1343_call = mutated_mod.get_global_var('func_1343')
var_2768 = relay.var("var_2768", dtype = "float64", shape = (504, 1))#candidate|2768|(504, 1)|var|float64
call_2767 = relay.TupleGetItem(func_1340_call(relay.reshape(var_2768.astype('float64'), [9, 7, 8])), 0)
call_2769 = relay.TupleGetItem(func_1343_call(relay.reshape(var_2768.astype('float64'), [9, 7, 8])), 0)
output = relay.Tuple([bop_2733,call_2745,call_2767,var_2768,])
output2 = relay.Tuple([bop_2733,call_2746,call_2769,var_2768,])
func_2773 = relay.Function([var_2731,var_2768,], output)
mod['func_2773'] = func_2773
mod = relay.transform.InferType()(mod)
var_2774 = relay.var("var_2774", dtype = "float64", shape = (16, 1, 2))#candidate|2774|(16, 1, 2)|var|float64
var_2775 = relay.var("var_2775", dtype = "float64", shape = (504, 1))#candidate|2775|(504, 1)|var|float64
output = func_2773(var_2774,var_2775,)
func_2776 = relay.Function([var_2774,var_2775,], output)
mutated_mod['func_2776'] = func_2776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_676_call = mod.get_global_var('func_676')
func_677_call = mutated_mod.get_global_var('func_677')
call_2787 = relay.TupleGetItem(func_676_call(), 1)
call_2788 = relay.TupleGetItem(func_677_call(), 1)
uop_2789 = relay.cosh(call_2787.astype('float32')) # shape=(5, 15, 2)
uop_2791 = relay.cosh(call_2788.astype('float32')) # shape=(5, 15, 2)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_2796 = relay.TupleGetItem(func_1578_call(), 1)
call_2797 = relay.TupleGetItem(func_1579_call(), 1)
output = relay.Tuple([uop_2789,call_2796,])
output2 = relay.Tuple([uop_2791,call_2797,])
func_2799 = relay.Function([], output)
mod['func_2799'] = func_2799
mod = relay.transform.InferType()(mod)
mutated_mod['func_2799'] = func_2799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2799_call = mutated_mod.get_global_var('func_2799')
call_2800 = func_2799_call()
output = call_2800
func_2801 = relay.Function([], output)
mutated_mod['func_2801'] = func_2801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1513_call = mod.get_global_var('func_1513')
func_1515_call = mutated_mod.get_global_var('func_1515')
call_2808 = relay.TupleGetItem(func_1513_call(), 3)
call_2809 = relay.TupleGetItem(func_1515_call(), 3)
output = relay.Tuple([call_2808,])
output2 = relay.Tuple([call_2809,])
func_2810 = relay.Function([], output)
mod['func_2810'] = func_2810
mod = relay.transform.InferType()(mod)
output = func_2810()
func_2811 = relay.Function([], output)
mutated_mod['func_2811'] = func_2811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1594_call = mod.get_global_var('func_1594')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_2851 = func_1594_call()
call_2852 = func_1594_call()
output = relay.Tuple([call_2851,])
output2 = relay.Tuple([call_2852,])
func_2860 = relay.Function([], output)
mod['func_2860'] = func_2860
mod = relay.transform.InferType()(mod)
mutated_mod['func_2860'] = func_2860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2860_call = mutated_mod.get_global_var('func_2860')
call_2861 = func_2860_call()
output = call_2861
func_2862 = relay.Function([], output)
mutated_mod['func_2862'] = func_2862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1260_call = mod.get_global_var('func_1260')
func_1262_call = mutated_mod.get_global_var('func_1262')
call_2863 = relay.TupleGetItem(func_1260_call(), 0)
call_2864 = relay.TupleGetItem(func_1262_call(), 0)
output = relay.Tuple([call_2863,])
output2 = relay.Tuple([call_2864,])
func_2869 = relay.Function([], output)
mod['func_2869'] = func_2869
mod = relay.transform.InferType()(mod)
output = func_2869()
func_2870 = relay.Function([], output)
mutated_mod['func_2870'] = func_2870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_2883 = func_2584_call()
call_2884 = func_2584_call()
output = call_2883
output2 = call_2884
func_2899 = relay.Function([], output)
mod['func_2899'] = func_2899
mod = relay.transform.InferType()(mod)
output = func_2899()
func_2900 = relay.Function([], output)
mutated_mod['func_2900'] = func_2900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_2937 = relay.TupleGetItem(func_2799_call(), 0)
call_2938 = relay.TupleGetItem(func_2801_call(), 0)
func_2411_call = mod.get_global_var('func_2411')
func_2414_call = mutated_mod.get_global_var('func_2414')
const_2940 = relay.const([[7],[-10],[-1],[-6],[-3],[-6],[5],[-4],[-1],[-10],[1],[-9],[10],[6],[3],[7],[-7],[6],[9],[8],[-3],[3],[-4],[-9],[-9],[2],[-6],[2],[10],[-3],[-2],[-3],[-5],[-7],[-1],[8],[-3],[1],[9],[10],[6],[1],[4],[7],[-9],[-9],[1],[10],[-10],[-2],[-5],[-4],[3],[-4],[5],[10],[8],[3],[-5],[6],[-3],[5],[-8],[9],[3],[1],[-4],[-6],[10],[7],[6],[7],[1],[3],[-4],[-9],[5],[-10],[10],[-3],[3],[-3],[-8],[-1],[-1],[-6],[-10],[-8],[-4],[-6],[-2],[-7],[1],[-2],[-9],[8],[-6],[6],[-1],[4],[7],[-6],[2],[-7],[-5],[-7],[8],[-5],[-1],[1],[-1],[-1],[-9],[-3],[-6],[-10],[-7],[-10],[-2],[-7],[10],[5],[-8],[-8],[-7],[-9],[10],[-5],[9],[-1],[7],[7],[-10],[4],[2],[9],[5],[-1],[-6],[4],[-1],[-2],[-4],[-2],[-7],[7],[-4],[7],[-9],[-6],[-2],[4],[-8],[-2],[7],[-8],[10],[-9],[-10],[-7],[-4],[2],[-7],[2],[10],[9],[-10],[1],[2],[-4],[9],[7],[-3],[4],[-7],[-2],[-5],[9],[-3],[-10],[-6],[7],[5],[-5],[1],[-4],[-1],[-2],[7],[-8],[6],[5],[2],[5],[-2],[8],[-5],[-5],[-5],[7],[-10],[-8],[2],[-5],[-3],[5],[-3],[-5],[4],[-10],[-7],[4],[5],[4],[10],[6],[2],[10],[2],[-5],[6],[-8],[-10],[-4],[3],[1],[-4],[5],[6],[1],[-1],[-5],[1],[-9],[1],[-9],[5],[6],[10],[-10],[-3],[4],[5],[9],[9],[9],[-7],[2],[-2],[-10],[-8],[9],[-6],[-7],[-4],[1],[7],[7],[3],[5],[-5],[1],[-1],[-9],[-8],[5],[10],[7],[9],[-4],[10],[-10],[-1],[9],[4],[7],[10],[-3],[-2],[5],[3],[-6],[-6],[-1],[-7],[-7],[10],[-4],[-6],[-4],[-8],[-10],[-10],[-9],[-5],[-2],[4],[3],[3],[4],[9],[-8],[1],[-10],[6],[-7],[-7],[-3],[10],[-9],[8],[-5],[-1],[4],[-2],[-3],[10],[-10],[5],[9],[-5],[6],[-5],[-9]], dtype = "uint8")#candidate|2940|(324, 1)|const|uint8
call_2939 = func_2411_call(relay.reshape(const_2940.astype('uint8'), [9, 3, 12]))
call_2941 = func_2411_call(relay.reshape(const_2940.astype('uint8'), [9, 3, 12]))
func_1764_call = mod.get_global_var('func_1764')
func_1767_call = mutated_mod.get_global_var('func_1767')
const_2947 = relay.const([2.291274,-2.285470,7.177166,-6.850471,-6.875857,6.041397,3.733776,-5.053231,5.929847,9.245246,9.392369,-0.823268,-1.802480,1.202503,5.910832,-2.899172,-4.809884,-4.056117,8.277956,-3.123545,-6.048395,-2.299513,-8.303232,1.561107,3.149593,-1.129635,-9.551721,-2.520228,-8.694628,-3.020415,5.525200,0.266650,4.121735,0.770687,-8.527119,7.150668,2.202944,8.253410,-3.599927,9.840965,5.809531,-3.799405,-9.882158,-7.534029,6.061120,1.584154,8.615602,-9.290467,-5.518430,2.720919,9.265458,8.878956,-8.475432,-9.836941,4.928814,7.496935,8.186257,-2.994869,-9.377912,7.317795,-1.117593,-1.429273,7.192074,-2.977366,-5.017846,-6.953311,-9.986787,-1.259663,-3.333250,-7.883621,3.967650,-0.659547,1.527951,-5.393068,1.974369,1.974142,-1.002689,0.137388,6.942300,5.389396,-4.942460,1.395015,1.658292,5.543322,4.719147,-3.416230,1.687814,8.002892,0.064578,-6.436790,2.897229,-6.348202,3.960070,8.195393,-1.143207,-0.498144,7.839181,5.026288,-0.054816,-2.295103,-0.892173,-7.043758,-1.990285,9.357867,1.215529,-7.991016,2.402355,1.281109,1.910423,0.064598,8.789907,-3.526799,-6.299981,-4.303062,-6.867214,-8.681388,7.411371,5.218047,-1.494630,8.668176,-7.151714,3.516239,9.631332,2.718097,8.599008,-4.101255,-0.902346,2.324503,-4.180168,7.595500,5.772376,-0.765330,-4.348458,-3.182429,-7.983651,8.441284,3.078537,-1.906988,2.818516,2.118201,6.014123,9.080703,-5.033212,-5.227550,-6.841156,-1.428464,2.186062,-0.687446,-8.918612,-5.239839,1.856181,7.916580,-2.339333,2.336055,2.091563,1.960057,-2.459862,3.550736,6.281508,0.361961,6.912352,4.877496,-9.592402,2.231549,-7.287694,8.706164,0.186158,4.148221,5.842099,2.081133,1.969571,5.705981,5.489375,5.305105,-6.754962,2.422618,-4.691457,-7.404426,-0.989337,1.110779,8.908599,-9.167355,5.414843,0.755714,-0.938858,-7.344631,6.908538,5.452723,-6.979397,4.847493,-5.491008,-6.819766,-5.139676,6.042029,-9.634079,2.913153,-5.857658,-7.550049,8.553901,-7.389816,-5.204888,-4.962541,-7.193164,3.466400,-7.634049,3.256244,7.623511,8.850414,-2.787615,-7.424393,5.683735,-0.083525,-9.229012,0.660102,-2.795319,4.915623,-0.354027,-3.047676,-9.767256,2.951774,9.253053,6.571549,9.837520,-8.772145,6.823439,-3.525164,-6.486954,-6.947519,-2.052250,3.494880,3.372607,7.455833,-2.602956,-4.248711,6.611586,6.932673,-1.028478,3.721176,4.917985,2.331653,2.290887,2.428410,1.453952,-6.621059,6.796511,-8.299688,-4.124877,3.845209,-1.068299,6.360649,1.126940,-0.847827,1.544930,0.124129,1.619867,-6.003543,0.602305,-7.667038,1.320208,-4.618328,-6.975775,-2.275412,-2.649175,8.682200,6.729925,8.798484,3.728911,0.724592,8.427635,1.308351,8.225393,3.469867,6.269607,3.954109,-2.330600,-0.403448,1.467299,-3.977569,-1.728245,-3.064970,-2.133734,-3.010608,2.043957,5.066032,3.959676,0.831343,-1.687273,4.181271,-5.774425,-6.314409,-2.292502,-2.680370,3.735188,9.948255,-3.255973,-6.097386,3.683525,8.564982,-8.206279,-4.522715,5.944184,-9.451102,-2.603082,-3.446102,4.150559,-4.757340,1.618781,8.236198,6.937463,-9.385488,-0.897279,-1.432388,8.535696,-8.609605,-1.611675,8.660801,-8.723298,0.374730,7.477825,5.061484,0.962103,-1.741839,-2.139995,0.248556,1.965274,-4.326529,-5.187453,5.580392,-9.659654,6.698404,-3.798666,-1.764519,1.246069,-5.624209,3.715929,8.292097,2.516206,0.804567,3.493976,0.452426,-6.272374,-3.693599,-5.848345,7.413061,2.075123,-4.577830,9.277455,-8.092466,-5.504547,-5.548827,-1.380201,-5.761077,4.251448,-5.745248,1.603595,4.096088,8.422752,-3.963980,-4.428436,-7.740405,9.429466,2.220073,9.895274,8.698303,-4.318458,-6.881183,9.212661,-9.499793,-9.342137,1.393710,-1.100731,-4.344226,-1.284553,-6.531866,-4.241569,-5.235125,5.075197,-0.253518,4.361125,-4.395969,2.811920,-6.054906,-2.357223,-4.129980,4.452510,-4.559712,-2.194373,8.861150,1.124567,4.974319,-3.693892,6.695210,-5.910169,0.880271,9.708723,5.340211,-4.086846,2.379260,2.639649,2.472911,2.894479,-5.822825,-3.205888,-0.796222,2.343129,4.268104,3.391339,2.299150,6.051855,0.599811,3.877162,3.175900,9.714757,-0.096392,-1.631499,4.185766,6.920978,-1.725510,-5.715921,7.016337,-4.819451,1.887717,-2.298828,1.239435,3.972612,-9.376336,-8.112303,-7.201297,9.558465,-2.393151,6.564780,5.940688,8.556570,-0.686619,0.416810,-7.916531,8.241435,1.059648,-7.967572,2.294840,-4.071964,-7.733996,7.273507,-1.418138,3.900946,6.319909,-7.290006,7.462901,-0.963301,7.603807,-2.734737,8.060334,-2.484826,2.615706,-9.341182,-6.257774,-6.641673,5.079826,-4.016163,-1.321800,-3.039703,-6.108540,9.467117,-7.392321,2.864869,3.493367,8.315691,8.568418,9.594204,9.028726,7.574522,-7.796361,-5.724733,-0.128191,5.414023,9.753173,-2.211380,0.439039,8.243739,6.100419,0.479972,-7.593801,1.991966,-6.295602,-6.028616,-7.339585,-9.118337,-2.194907,-0.825075,2.195372,0.071905,5.290550,-0.218842,0.895599,4.997778,-5.765877,2.790212,1.922632,7.917744,-8.633835,2.343776,4.281225,5.961442,7.644590,-0.560756,-2.372217,9.805270,2.566008,-2.944162,8.369175,0.625645,-3.126758,2.757924,-2.262711,-1.974072,-7.573101,0.033716,7.591750,7.933403,6.121916,6.971242,-8.384832,4.574622,-2.482889,-0.017186,6.472862,6.120111,5.598793,-8.773135,1.230686,-6.854551,-4.954333,-8.413184,-8.928848,-2.750727,2.821439,0.550917,-7.565516,-5.273806,-6.822093,6.035165,-0.522090,-8.714883,3.792845,6.249127,0.116501,-1.683362,-8.852845,1.452401,4.885143,-1.744818,4.742460,-7.727076,-1.406621,-4.281511,1.272754,1.680526,-2.548539,0.677366,-0.793982,5.950389,-7.455278,4.538033,-1.768508,-8.277071,7.255069,-2.458640,-7.327626,-6.237044,0.354548,-5.635772,-8.252741,8.438878,1.637752,-7.252998,2.873956,7.366663,-5.524805,-9.228616,3.217984,-3.998976,5.487246,5.362326,8.467931,1.647385,-3.268474,4.896318,0.491089,7.588117,-1.622214,-0.523194,4.397423,1.155858,-8.082222,-6.895524,-0.755489,-8.961108,-3.048541,-9.556872,-0.445758,-8.329168,0.987886,9.492172,-3.031150,4.134196,3.781547,6.266127,5.253177,-5.210670,-2.584962,9.641513,4.496680,3.205715,5.168505,0.840139,4.362624,-2.893787,0.477566,4.259256,-0.704938,-5.894439,-4.680293,8.823404,6.587849,0.563660,-2.975035,-3.186017,4.601540,2.326944,4.123307,-4.962448,7.790835,0.721328,-7.467323,-5.745194,3.234590,-2.549225,-5.126610,9.309316,4.088661,-7.634838,5.473026,1.799326,-3.011869,1.518619,1.223424,-6.247962,-3.393930,-4.446144,-3.393079,-0.201133,6.737830,8.569694,-7.119090,3.583884,5.771843,4.684777,9.543085,8.140381,-8.956942,4.044053,-2.043796,-9.994616,-0.110659,-0.859269,7.718394,-8.402272,9.804296,8.590654,0.309543,-1.082396,-4.433865,5.082911,-1.546335,2.282478,-7.994458,8.784531,-3.418460,5.078102,-9.057408,1.371937,-6.390420,-2.140548,3.216779,5.672284,8.835275,0.480398,-9.261953,8.274075,-3.998638,4.463578,6.433789,0.800408,-9.420671,-1.854014,-3.725872,-1.421583,-1.045061,7.972014,-3.669705,-0.942400,-1.514776,1.322397,-5.650638,9.864072,6.282127,9.862946,4.987090,-9.857242,-1.734732,-7.260962,-4.013590,7.493796,-6.281427,-3.681918,-4.711116,-0.040194,2.086109,2.054825,-0.515983,-6.707367,2.506476,-8.798872,-6.209812,-4.382211,-5.388033,-5.772899,3.641735,9.119944,-5.088648,3.293881,-6.256421,7.394108,8.977483,9.065692,8.644777,-0.700219,-8.125236,-7.044069,0.848090,0.504380,9.593932,7.774586,4.620470,-5.841784,-6.862606,-0.478415,2.209854,-5.423714,-8.201231,-6.484686,5.003862,-3.395370,-1.336907,0.415778,6.855223,8.581397,-3.703740,-5.501978,8.641520,8.656631,-5.304524,-1.553973,1.884662,-1.495160,-6.739593,8.429794,7.484213,2.026540,-5.499740,-9.378343,8.968277,3.134193,-4.800350,-4.860892,-2.371800,4.460691,2.685946,1.859179,4.211211,1.953157,-3.611787,6.034148,-4.452728,9.124633,1.419881,1.734768,8.522264,-4.866515,-8.132223,0.565402,-5.919032,4.027484,-2.226623,-7.244251,-0.860624,-1.600918,4.517008,5.753838,-6.472830,-3.298849,-4.643510,7.633575,-7.196371,1.631345,-2.020859,-5.215326,0.167095,-9.925466,-7.449015,5.510955,-0.505211,2.967408,-8.639694,-4.467975,-1.532523,-2.231134,-9.762999,-5.577138,-7.272637,5.550458,5.512702,1.464704,8.889950,-9.372925,5.071963,-1.166859,9.424092,8.091983,-7.845856,9.462636,-2.067928,4.587828,5.426570,-9.454433,4.581834,-0.523101,6.987441,-7.236550,3.437253,-8.295543,-9.871846,6.376502,-1.623418,8.918001,-7.295336,2.905961,5.558983,7.485817,0.187366,-2.678630,4.939541,0.943255,-5.858403,4.852471,-4.487593,-4.234749,-2.761472,8.965717,-7.514787,-2.720025,3.122828,-9.191856,-8.367227,8.555610,6.116083,9.826735,-3.278103,7.435880,-7.179969,-5.934270,-0.959974,6.633050,-1.380952,9.206752,-1.137931,2.541183,-3.994332,-9.998493,6.247649,-3.030134,1.689135,4.735752,-6.353620,-2.592901,3.289632,4.026046,-9.962915,1.326804,2.510911,4.982954,-3.266548,7.054797,-1.387064,5.308846,6.459210], dtype = "float64")#candidate|2947|(896,)|const|float64
call_2946 = relay.TupleGetItem(func_1764_call(relay.reshape(const_2947.astype('float64'), [16, 7, 8])), 0)
call_2948 = relay.TupleGetItem(func_1767_call(relay.reshape(const_2947.astype('float64'), [16, 7, 8])), 0)
output = relay.Tuple([call_2937,call_2939,const_2940,call_2946,const_2947,])
output2 = relay.Tuple([call_2938,call_2941,const_2940,call_2948,const_2947,])
func_2971 = relay.Function([], output)
mod['func_2971'] = func_2971
mod = relay.transform.InferType()(mod)
output = func_2971()
func_2972 = relay.Function([], output)
mutated_mod['func_2972'] = func_2972
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2976 = relay.var("var_2976", dtype = "int32", shape = ())#candidate|2976|()|var|int32
var_2977 = relay.var("var_2977", dtype = "int32", shape = (7, 13, 10))#candidate|2977|(7, 13, 10)|var|int32
bop_2978 = relay.logical_xor(var_2976.astype('int32'), var_2977.astype('int32')) # shape=(7, 13, 10)
uop_2990 = relay.log(bop_2978.astype('float32')) # shape=(7, 13, 10)
output = uop_2990
output2 = uop_2990
func_3006 = relay.Function([var_2976,var_2977,], output)
mod['func_3006'] = func_3006
mod = relay.transform.InferType()(mod)
var_3007 = relay.var("var_3007", dtype = "int32", shape = ())#candidate|3007|()|var|int32
var_3008 = relay.var("var_3008", dtype = "int32", shape = (7, 13, 10))#candidate|3008|(7, 13, 10)|var|int32
output = func_3006(var_3007,var_3008,)
func_3009 = relay.Function([var_3007,var_3008,], output)
mutated_mod['func_3009'] = func_3009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2810_call = mod.get_global_var('func_2810')
func_2811_call = mutated_mod.get_global_var('func_2811')
call_3023 = relay.TupleGetItem(func_2810_call(), 0)
call_3024 = relay.TupleGetItem(func_2811_call(), 0)
output = relay.Tuple([call_3023,])
output2 = relay.Tuple([call_3024,])
func_3034 = relay.Function([], output)
mod['func_3034'] = func_3034
mod = relay.transform.InferType()(mod)
output = func_3034()
func_3035 = relay.Function([], output)
mutated_mod['func_3035'] = func_3035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_676_call = mod.get_global_var('func_676')
func_677_call = mutated_mod.get_global_var('func_677')
call_3055 = relay.TupleGetItem(func_676_call(), 0)
call_3056 = relay.TupleGetItem(func_677_call(), 0)
func_1340_call = mod.get_global_var('func_1340')
func_1343_call = mutated_mod.get_global_var('func_1343')
const_3069 = relay.const([5.046927,-2.416627,-0.927919,-5.623927,-2.469239,3.773860,2.428155,8.810453,1.659920,-1.839740,-3.522524,8.812063,-8.755606,0.100087,-6.760129,-6.381282,9.566403,3.114211,5.982459,-7.992585,-4.022519,-8.962529,5.092355,-4.795252,-6.135938,7.038711,-8.628333,7.990111,2.930825,-3.111413,-6.483782,8.581085,4.237558,-2.204740,5.631052,3.307125,-5.206050,1.773832,6.325158,-4.494487,-7.592173,-9.717194,-7.390131,2.887367,-4.115531,2.327628,0.552200,-9.525557,7.334457,2.636627,7.803763,-3.322462,-8.510061,7.375775,9.613091,4.963835,-4.721707,-4.150223,6.643754,-5.584374,-1.467191,-3.849529,-4.517419,-2.752076,7.181423,-8.813237,-0.573801,-8.334276,-9.915665,0.586136,3.249686,-8.257908,-7.082471,-1.458443,-8.387592,-1.465681,-2.427641,-9.599803,7.205416,-2.156174,-0.437960,-1.370285,9.369079,6.663847,-6.038194,4.745682,6.544235,3.826397,5.067967,1.866406,-6.773968,-0.241423,7.169485,-2.161795,9.324492,1.048365,0.562952,5.015079,5.784165,2.881573,6.605303,3.732722,-8.556280,-3.260488,3.302513,6.861938,7.394606,-3.028816,2.944967,-1.349731,-9.322994,-7.087281,2.112718,-0.305341,3.881953,-0.566934,9.203851,0.034031,9.923572,6.709483,-4.507627,-3.367187,-2.447873,-0.864936,3.997226,-2.809687,-7.045567,-5.649088,-7.798268,-7.351185,-8.511066,-4.275969,8.097736,9.835835,-9.057001,6.471154,1.891919,-3.339686,-9.197190,9.855941,5.207295,8.213916,3.030082,9.016441,2.932811,6.493930,5.787471,3.196814,1.755811,0.524397,4.370202,-1.316060,-3.346756,-0.095947,6.040734,2.448140,6.993619,0.974601,-2.883558,7.568532,-4.037549,8.828288,-4.387256,-0.368143,4.243288,6.688664,-9.407004,0.866415,3.558509,-1.585891,-6.413484,2.791555,-8.261758,-8.888634,-9.833897,-4.813690,-7.994743,-3.996815,-2.346725,-5.188553,-1.693417,-8.545513,-4.140090,1.321019,5.638359,-1.652015,0.179211,-6.289095,-6.760648,-4.215198,-3.719339,-2.930799,-7.574848,5.387265,9.983106,-5.982333,-1.239388,4.796532,8.547238,-0.735590,-9.441323,-4.541088,-8.808346,4.719521,3.195677,0.057251,2.820871,-8.298845,-9.550842,-2.875204,6.323562,4.249921,-5.602735,-8.078517,-2.978995,-8.257036,-1.171985,-1.525877,0.248946,9.257870,-4.967347,-6.183908,-2.450787,5.648694,4.269905,3.602035,8.805070,-7.018582,3.530796,9.778639,1.896179,-3.287125,-4.567022,-2.800211,-5.279058,-5.284237,1.349174,-4.556380,8.786126,-2.636921,-3.764933,0.059814,4.437766,5.292038,8.855979,-2.270919,-6.094461,-3.139589,1.169398,8.314845,-3.315815,-8.879710,-1.415980,-9.679155,4.673849,-4.560575,-8.028122,5.908180,8.294934,-5.491058,0.663698,6.696741,3.188840,-6.503015,0.617118,-7.558832,2.747008,4.194950,-3.768247,2.963225,-7.907505,3.803148,4.944043,-0.813420,2.801513,7.134993,6.533715,-7.916211,-7.439512,-1.252982,-4.892164,-0.176552,2.904201,-8.145954,9.507936,6.597111,6.114811,-9.822480,7.771749,-1.023313,7.268783,1.182034,-3.236897,6.823756,-7.271149,-4.197897,-0.861129,-5.244355,-4.281051,3.216649,-6.302674,-2.891242,5.636750,6.610034,7.971672,0.151983,2.369273,-8.074405,3.572179,7.581737,7.388178,-7.434937,-4.276327,4.424005,0.155728,-2.759174,-7.142206,-4.240802,0.583946,-7.083753,1.155466,7.106414,5.348362,-3.635644,7.714475,-7.392486,-7.203957,-2.833764,-2.107048,2.559807,7.220406,8.770524,-4.729584,1.596664,4.125736,8.407240,-6.006118,-5.630624,-0.604012,-2.144229,-1.877907,-1.161688,7.670794,8.291539,-6.737367,-0.580487,-5.740764,5.970276,3.507367,-0.662309,7.197008,9.459919,-3.541736,5.486800,-5.872201,-7.450661,-6.287295,9.445996,1.835844,1.746152,-6.175148,8.268133,-6.974393,9.876209,-6.975768,-1.969377,4.851744,8.786506,2.294955,-3.248194,-4.343877,-7.535690,9.568651,-1.503159,-4.683498,9.323650,3.175835,0.109440,1.788362,9.817701,-9.335532,8.798260,6.464335,1.217644,3.982518,1.472992,-5.257312,2.799996,7.339702,6.424948,7.176261,-4.488316,1.072374,-6.955618,0.754427,-2.846510,-9.491370,5.658706,-6.328902,-2.224787,2.148646,5.629799,-0.575483,4.374369,7.860792,6.231569,7.705774,3.308384,-3.019972,-8.235719,-3.035553,2.149017,-7.821487,-3.121989,-9.064157,1.288471,-4.233783,8.855974,1.135129,1.753661,2.009115,3.102832,-0.466572,-5.417678,5.666603,-8.474469,5.229503,-1.164229,4.810389,2.050494,6.394824,0.323648,9.113941,-5.684626,1.921556,8.841909,6.519710,-0.440450,-3.687264,-5.526622,0.395105,8.541669,-1.842473,-3.929315,-4.734581,1.689740,-4.182497,-9.872657,-9.273869,-1.217925,-6.295595,-4.866607,4.960209,7.291845,0.839805,8.332653,5.730856,-2.424757,-6.001060,6.167189,-8.813193,-1.353698,5.997180,-5.133148,-1.147221,4.759166,5.681470,-9.738760,-5.329194,-1.241879,0.604522,-4.139095,-5.245427,-8.312505,-2.708696,6.053979,1.700834,4.026683,-4.486196,-0.539922,7.677904,0.712648,5.019791,8.144300,-2.332257,-2.511647,7.053659,-7.660682,4.333651,-9.587418,-6.009115,-2.527660,6.586997,-2.931722,9.998775,-5.540504,-4.847439,8.384005,5.515138,-6.166689,-2.544933,2.384758,3.732243,0.934193], dtype = "float64")#candidate|3069|(504,)|const|float64
call_3068 = relay.TupleGetItem(func_1340_call(relay.reshape(const_3069.astype('float64'), [9, 7, 8])), 0)
call_3070 = relay.TupleGetItem(func_1343_call(relay.reshape(const_3069.astype('float64'), [9, 7, 8])), 0)
output = relay.Tuple([call_3055,call_3068,const_3069,])
output2 = relay.Tuple([call_3056,call_3070,const_3069,])
func_3079 = relay.Function([], output)
mod['func_3079'] = func_3079
mod = relay.transform.InferType()(mod)
output = func_3079()
func_3080 = relay.Function([], output)
mutated_mod['func_3080'] = func_3080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_3112 = func_526_call()
call_3113 = func_526_call()
output = call_3112
output2 = call_3113
func_3132 = relay.Function([], output)
mod['func_3132'] = func_3132
mod = relay.transform.InferType()(mod)
output = func_3132()
func_3133 = relay.Function([], output)
mutated_mod['func_3133'] = func_3133
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3264 = relay.var("var_3264", dtype = "int16", shape = (12, 13, 16))#candidate|3264|(12, 13, 16)|var|int16
var_3265 = relay.var("var_3265", dtype = "int16", shape = (12, 13, 16))#candidate|3265|(12, 13, 16)|var|int16
bop_3266 = relay.left_shift(var_3264.astype('int16'), relay.reshape(var_3265.astype('int16'), relay.shape_of(var_3264))) # shape=(12, 13, 16)
func_2164_call = mod.get_global_var('func_2164')
func_2165_call = mutated_mod.get_global_var('func_2165')
call_3281 = relay.TupleGetItem(func_2164_call(), 0)
call_3282 = relay.TupleGetItem(func_2165_call(), 0)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_3285 = relay.TupleGetItem(func_1578_call(), 0)
call_3286 = relay.TupleGetItem(func_1579_call(), 0)
output = relay.Tuple([bop_3266,call_3281,call_3285,])
output2 = relay.Tuple([bop_3266,call_3282,call_3286,])
func_3292 = relay.Function([var_3264,var_3265,], output)
mod['func_3292'] = func_3292
mod = relay.transform.InferType()(mod)
var_3293 = relay.var("var_3293", dtype = "int16", shape = (12, 13, 16))#candidate|3293|(12, 13, 16)|var|int16
var_3294 = relay.var("var_3294", dtype = "int16", shape = (12, 13, 16))#candidate|3294|(12, 13, 16)|var|int16
output = func_3292(var_3293,var_3294,)
func_3295 = relay.Function([var_3293,var_3294,], output)
mutated_mod['func_3295'] = func_3295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_676_call = mod.get_global_var('func_676')
func_677_call = mutated_mod.get_global_var('func_677')
call_3297 = relay.TupleGetItem(func_676_call(), 0)
call_3298 = relay.TupleGetItem(func_677_call(), 0)
var_3310 = relay.var("var_3310", dtype = "float64", shape = (5, 15, 2))#candidate|3310|(5, 15, 2)|var|float64
bop_3311 = relay.multiply(call_3297.astype('uint64'), relay.reshape(var_3310.astype('uint64'), relay.shape_of(call_3297))) # shape=(5, 15, 2)
bop_3314 = relay.multiply(call_3298.astype('uint64'), relay.reshape(var_3310.astype('uint64'), relay.shape_of(call_3298))) # shape=(5, 15, 2)
output = relay.Tuple([bop_3311,])
output2 = relay.Tuple([bop_3314,])
func_3329 = relay.Function([var_3310,], output)
mod['func_3329'] = func_3329
mod = relay.transform.InferType()(mod)
mutated_mod['func_3329'] = func_3329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3330 = relay.var("var_3330", dtype = "float64", shape = (5, 15, 2))#candidate|3330|(5, 15, 2)|var|float64
func_3329_call = mutated_mod.get_global_var('func_3329')
call_3331 = func_3329_call(var_3330)
output = call_3331
func_3332 = relay.Function([var_3330], output)
mutated_mod['func_3332'] = func_3332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_3377 = relay.TupleGetItem(func_1894_call(), 0)
call_3378 = relay.TupleGetItem(func_1896_call(), 0)
var_3391 = relay.var("var_3391", dtype = "float64", shape = (16, 7, 8))#candidate|3391|(16, 7, 8)|var|float64
bop_3392 = relay.multiply(call_3377.astype('float32'), relay.reshape(var_3391.astype('float32'), relay.shape_of(call_3377))) # shape=(16, 7, 8)
bop_3395 = relay.multiply(call_3378.astype('float32'), relay.reshape(var_3391.astype('float32'), relay.shape_of(call_3378))) # shape=(16, 7, 8)
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
var_3400 = relay.var("var_3400", dtype = "float64", shape = (56,))#candidate|3400|(56,)|var|float64
call_3399 = relay.TupleGetItem(func_1421_call(relay.reshape(var_3400.astype('float64'), [1, 7, 8])), 0)
call_3401 = relay.TupleGetItem(func_1424_call(relay.reshape(var_3400.astype('float64'), [1, 7, 8])), 0)
output = relay.Tuple([bop_3392,call_3399,var_3400,])
output2 = relay.Tuple([bop_3395,call_3401,var_3400,])
func_3406 = relay.Function([var_3391,var_3400,], output)
mod['func_3406'] = func_3406
mod = relay.transform.InferType()(mod)
mutated_mod['func_3406'] = func_3406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3406_call = mutated_mod.get_global_var('func_3406')
var_3408 = relay.var("var_3408", dtype = "float64", shape = (16, 7, 8))#candidate|3408|(16, 7, 8)|var|float64
var_3409 = relay.var("var_3409", dtype = "float64", shape = (56,))#candidate|3409|(56,)|var|float64
call_3407 = func_3406_call(var_3408,var_3409,)
output = call_3407
func_3410 = relay.Function([var_3408,var_3409,], output)
mutated_mod['func_3410'] = func_3410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3466 = relay.var("var_3466", dtype = "float64", shape = (5, 11, 2))#candidate|3466|(5, 11, 2)|var|float64
const_3467 = relay.const([[[-3.112328,-2.036641],[-2.923877,1.672590],[-5.554114,1.571456],[4.580115,5.784011],[1.916220,-1.847892],[-6.799835,-5.828300],[6.667640,-0.810424],[2.574899,-1.997352],[5.047920,-3.355862],[7.485707,-0.476188],[-5.689166,6.522293]],[[2.605417,-4.592820],[-3.106367,-6.682785],[-2.639845,-1.072774],[0.577791,-6.248194],[-8.814759,-1.538006],[4.767663,2.631459],[-4.812620,-5.160324],[8.389114,-3.244710],[9.210605,-4.370487],[-7.786389,-7.329909],[0.099126,-8.874585]],[[-7.876611,-5.416817],[9.264608,-7.189942],[0.046481,1.585414],[6.261779,-9.559937],[3.014173,9.616762],[-3.313275,-6.022496],[0.977711,1.638736],[-2.562866,3.661658],[-9.153085,3.806554],[8.604903,-8.217053],[-8.478534,-1.804160]],[[-4.064813,-2.793787],[-3.508746,-6.206678],[9.195840,2.417382],[8.815524,-2.480462],[-6.151100,-4.593423],[9.089212,-9.127655],[-5.233222,9.220931],[-2.666788,-2.137000],[-9.934129,-7.852527],[0.471071,9.418948],[-7.151305,1.416506]],[[-4.282060,4.311104],[1.098706,6.194159],[8.285156,3.907782],[4.796828,-4.916724],[5.506065,-1.442316],[-8.597272,-7.889009],[7.148963,-9.734584],[-6.398441,6.905682],[1.512923,6.265202],[5.066626,0.831421],[-1.347625,-7.273747]]], dtype = "float64")#candidate|3467|(5, 11, 2)|const|float64
bop_3468 = relay.mod(var_3466.astype('float64'), relay.reshape(const_3467.astype('float64'), relay.shape_of(var_3466))) # shape=(5, 11, 2)
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
const_3474 = relay.const([-2.400753,-1.574197,-9.397605,7.797527,-1.854544,-3.619682,-4.151806,-5.826116,-2.679383,-6.299283,-3.864224,1.528818,1.446331,8.353685,0.862522,4.707536,-3.757308,1.346793,7.919344,-6.969780,-4.926736,6.386180,7.565068,3.805561,-8.930131,-7.208908,3.490983,9.972899,9.949351,8.167581,9.460980,3.251009,-7.064360,2.428831,1.628420,9.315628,-6.364108,5.710348,0.678683,3.975962,-1.627386,-0.875195,8.960293,5.324893,0.800430,-9.918827,2.903785,-0.629036,-1.757239,5.712094,4.993602,8.098834,-2.183609,0.379571,-1.234192,0.659014], dtype = "float64")#candidate|3474|(56,)|const|float64
call_3473 = relay.TupleGetItem(func_1421_call(relay.reshape(const_3474.astype('float64'), [1, 7, 8])), 0)
call_3475 = relay.TupleGetItem(func_1424_call(relay.reshape(const_3474.astype('float64'), [1, 7, 8])), 0)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_3479 = relay.TupleGetItem(func_1578_call(), 1)
call_3480 = relay.TupleGetItem(func_1579_call(), 1)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_3507 = func_526_call()
call_3508 = func_526_call()
output = relay.Tuple([bop_3468,call_3473,const_3474,call_3479,call_3507,])
output2 = relay.Tuple([bop_3468,call_3475,const_3474,call_3480,call_3508,])
func_3519 = relay.Function([var_3466,], output)
mod['func_3519'] = func_3519
mod = relay.transform.InferType()(mod)
mutated_mod['func_3519'] = func_3519
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3520 = relay.var("var_3520", dtype = "float64", shape = (5, 11, 2))#candidate|3520|(5, 11, 2)|var|float64
func_3519_call = mutated_mod.get_global_var('func_3519')
call_3521 = func_3519_call(var_3520)
output = call_3521
func_3522 = relay.Function([var_3520], output)
mutated_mod['func_3522'] = func_3522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2869_call = mod.get_global_var('func_2869')
func_2870_call = mutated_mod.get_global_var('func_2870')
call_3527 = relay.TupleGetItem(func_2869_call(), 0)
call_3528 = relay.TupleGetItem(func_2870_call(), 0)
output = relay.Tuple([call_3527,])
output2 = relay.Tuple([call_3528,])
func_3536 = relay.Function([], output)
mod['func_3536'] = func_3536
mod = relay.transform.InferType()(mod)
output = func_3536()
func_3537 = relay.Function([], output)
mutated_mod['func_3537'] = func_3537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1916_call = mod.get_global_var('func_1916')
func_1918_call = mutated_mod.get_global_var('func_1918')
call_3557 = relay.TupleGetItem(func_1916_call(), 0)
call_3558 = relay.TupleGetItem(func_1918_call(), 0)
var_3565 = relay.var("var_3565", dtype = "float32", shape = (5, 7, 8))#candidate|3565|(5, 7, 8)|var|float32
bop_3566 = relay.minimum(call_3557.astype('float64'), var_3565.astype('float64')) # shape=(5, 7, 8)
bop_3569 = relay.minimum(call_3558.astype('float64'), var_3565.astype('float64')) # shape=(5, 7, 8)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_3585 = relay.TupleGetItem(func_1894_call(), 0)
call_3586 = relay.TupleGetItem(func_1896_call(), 0)
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_3597 = relay.TupleGetItem(func_3034_call(), 0)
call_3598 = relay.TupleGetItem(func_3035_call(), 0)
output = relay.Tuple([bop_3566,call_3585,call_3597,])
output2 = relay.Tuple([bop_3569,call_3586,call_3598,])
func_3604 = relay.Function([var_3565,], output)
mod['func_3604'] = func_3604
mod = relay.transform.InferType()(mod)
var_3605 = relay.var("var_3605", dtype = "float32", shape = (5, 7, 8))#candidate|3605|(5, 7, 8)|var|float32
output = func_3604(var_3605)
func_3606 = relay.Function([var_3605], output)
mutated_mod['func_3606'] = func_3606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_3627 = relay.TupleGetItem(func_2799_call(), 1)
call_3628 = relay.TupleGetItem(func_2801_call(), 1)
func_2643_call = mod.get_global_var('func_2643')
func_2644_call = mutated_mod.get_global_var('func_2644')
call_3649 = func_2643_call()
call_3650 = func_2643_call()
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_3654 = func_574_call()
call_3655 = func_574_call()
output = relay.Tuple([call_3627,call_3649,call_3654,])
output2 = relay.Tuple([call_3628,call_3650,call_3655,])
func_3681 = relay.Function([], output)
mod['func_3681'] = func_3681
mod = relay.transform.InferType()(mod)
output = func_3681()
func_3682 = relay.Function([], output)
mutated_mod['func_3682'] = func_3682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1916_call = mod.get_global_var('func_1916')
func_1918_call = mutated_mod.get_global_var('func_1918')
call_3683 = relay.TupleGetItem(func_1916_call(), 0)
call_3684 = relay.TupleGetItem(func_1918_call(), 0)
func_1764_call = mod.get_global_var('func_1764')
func_1767_call = mutated_mod.get_global_var('func_1767')
const_3706 = relay.const([4.759123,-5.012312,-8.071554,9.220997,-6.765233,-9.335465,-0.718930,-6.862310,-1.641016,-7.992483,-5.661178,-1.057351,-1.797491,8.877355,2.965220,8.118992,-0.631897,-3.707722,5.997058,1.080055,-8.968796,-6.773900,-7.028054,-2.828814,-6.650649,-8.506464,-7.120986,6.112266,0.846981,-2.790488,4.624005,6.255720,2.627545,-3.927919,8.605583,3.485567,4.503407,3.881295,-1.296630,-0.118462,-9.713003,-9.772582,4.301511,5.038210,-9.993188,2.623569,9.331940,4.138741,-6.758517,8.583993,3.502992,-0.720772,-3.446381,-2.059275,8.172964,-1.370980,7.466514,-4.697488,-1.707347,2.954146,-0.563342,-6.270997,-6.699220,-4.965454,5.716326,-0.447046,-7.183861,5.635961,-9.612515,-2.834598,-0.615040,0.207858,5.545588,-0.370332,8.171193,-4.626442,6.760345,-1.959562,-7.966677,-3.567825,-1.410091,-7.535116,1.138154,-5.521782,1.706363,8.365652,8.165499,7.838178,0.556946,-1.573464,-9.414236,-5.212161,4.779472,8.330457,2.716004,4.812635,-6.866266,3.548883,9.389524,-0.430540,-0.223996,-0.806869,-4.564465,-5.487059,3.241572,8.128688,1.064787,0.577813,-4.466513,-4.257678,0.755840,1.289391,9.854764,7.613736,-0.243966,5.826701,-5.306066,-8.570322,5.044882,-3.433350,7.794785,-4.180544,6.324568,2.946328,-4.831325,1.305995,7.786508,-8.647352,9.419454,8.447844,8.289815,-4.427783,-5.498306,-6.410120,7.083861,6.725518,-1.551696,8.786800,2.329499,6.494814,-5.014921,8.270253,-4.458546,-9.246546,-0.844751,7.149343,-3.668724,1.496511,2.480776,9.182488,-8.145498,6.471977,-5.256357,-6.354292,-5.472262,-7.627694,-2.588480,-7.862501,5.590270,4.685083,2.439596,2.296828,-6.257825,-6.978387,-7.506656,1.445278,-6.934643,-2.638317,8.493817,7.654368,-8.571868,9.259650,4.458224,5.612865,-6.680895,-5.195024,-6.179481,-7.491284,-3.756880,-3.862924,-0.390472,3.068230,-7.484710,0.558242,-8.986676,8.259838,-5.392065,-2.097929,9.553980,-2.251906,-7.845446,1.350316,-5.221831,2.642896,-4.607201,-6.778841,0.719690,-7.616653,1.622210,-2.823233,-3.943166,-1.669694,-6.835429,-5.776673,6.343675,1.450831,-9.382568,-2.555690,-2.920164,3.713236,8.228312,0.575944,-5.957991,-8.848180,-9.217506,7.772990,3.910991,5.389683,-1.826550,0.759172,9.970871,5.891045,8.673333,-0.845266,-8.488016,-5.427144,6.998793,-8.631239,7.562228,9.760544,7.482556,-5.681846,4.305739,-2.820379,-4.269646,3.729650,0.132544,5.548048,-7.183087,-7.685639,0.425171,-5.563622,5.055764,-0.552423,6.299207,-1.932087,8.094617,2.175496,-4.587912,-4.850780,4.483831,-6.509590,6.808852,2.314674,-4.387548,-7.546332,1.280363,-8.159403,7.315541,5.523095,2.364734,-8.110675,8.104274,0.142999,9.497207,-3.885092,0.275589,5.841806,-8.935637,-8.558093,3.112722,-1.820582,7.000508,7.423450,-2.945840,6.328823,-2.937030,-8.110604,-8.877975,2.863604,3.135678,-9.873785,9.698492,4.529331,7.357756,-9.506010,-2.471666,7.172450,8.005564,4.962765,7.011620,3.018378,-7.031281,3.937946,9.525363,-9.155961,-8.921474,7.317748,5.252283,8.170512,-7.273994,6.025078,3.303052,-3.133334,2.083578,-8.723514,1.225351,-2.660854,0.174362,-0.528079,-9.320229,5.558208,5.605899,-9.143592,-9.027279,8.119497,6.065994,6.044585,8.450218,-8.361482,9.946396,-8.452636,-3.495681,-1.535658,-0.997375,7.312680,-2.828652,-7.416578,2.153160,-1.553441,-4.300862,2.649746,-0.114840,-2.480411,-1.744756,-8.960265,0.511169,-5.591575,7.036292,2.523820,1.661611,-5.912590,-9.710757,-5.286088,-3.934981,7.469353,-2.803202,-8.036104,0.859506,9.491526,8.346212,-6.035131,-7.861781,0.541851,0.460257,8.602092,8.910190,-7.542841,-0.201889,9.504813,3.773615,-8.413280,2.938988,-1.958142,3.590978,8.339960,2.777013,-1.082168,-6.561609,3.038385,-7.956520,6.279502,1.621419,9.895514,-1.070993,-7.487431,0.207086,8.505642,6.672109,-3.813950,1.225366,-3.135197,7.393430,-3.292381,-1.963893,7.533081,5.019414,-3.262170,5.805628,-9.744942,-0.417916,7.773406,8.228127,0.027896,7.796844,-1.577863,0.344188,1.192846,2.052734,-7.774774,-2.863860,-2.800103,-4.661558,-6.601401,9.201624,1.030278,8.241272,9.741317,-5.530027,6.330816,-4.632502,-7.740859,-4.438631,-0.950013,-6.261305,6.581516,5.901801,-8.147506,-7.489742,4.930085,0.904894,-9.182117,7.453482,-4.422888,-5.750984,8.450140,4.644891,-1.938781,-1.121544,2.179158,5.711217,8.071563,-2.288577,9.068969,-2.505017,-6.231897,7.195789,-4.674705,1.805297,-5.348755,-7.423815,-7.111686,-7.162450,-5.886906,-0.031447,5.776786,-3.383865,-3.409863,-1.735779,-3.941266,-0.377324,-5.945590,3.536385,-3.996647,4.840741,-6.022895,0.440266,3.785053,9.074928,-9.955115,9.593427,7.094264,-9.171376,6.696234,8.788605,5.779693,-6.965343,-3.621690,-5.487202,-2.909929,2.232089,7.005663,-8.525957,-9.851527,-3.372982,4.226903,-0.890896,-1.374987,-6.702072,1.011710,5.379586,0.224155,6.112727,8.528317,-7.418770,5.446463,-6.059049,-7.246937,-4.598842,-5.118319,8.647112,-7.388403,-4.449754,-4.643142,-2.684836,6.906437,-4.085174,-9.308992,-2.546900,9.207763,8.357210,-4.977247,-2.614113,-1.818569,-9.347316,0.390323,-1.060769,2.548421,-4.147767,9.345479,-3.059019,-4.031945,5.548536,-9.170703,-1.234806,9.097805,-4.958615,9.339316,-9.848896,3.446271,-1.495465,7.295253,6.273116,-0.877232,-4.274093,-9.304681,-5.429862,-8.325698,8.571956,8.242790,-5.199116,-6.725283,-5.838069,2.825336,1.063786,4.569974,-4.961790,0.086018,-9.131916,0.895789,6.550690,0.307148,3.072117,-7.970443,-4.319688,-6.659146,-7.124361,9.936376,0.771480,8.727704,-7.268727,-2.120904,5.636740,-9.275929,0.799261,3.649085,7.801835,-1.853510,-9.478059,-9.805971,-8.370366,5.202134,6.698021,-3.622365,-5.387006,1.268119,-2.908104,1.047416,1.734719,0.674070,7.920699,-4.465774,2.516812,6.756664,6.581073,-0.963946,4.188225,-5.257523,8.400596,7.746380,-1.254738,-4.579853,-6.420169,5.801481,1.325298,4.722616,9.542874,5.386245,-2.219351,-2.726356,-5.405008,-7.090715,-2.125792,-0.627721,9.189017,8.850846,6.205292,-7.086752,3.281698,1.042062,6.582660,-5.125036,-0.696780,2.439828,-4.610212,-7.835038,2.515342,-6.449967,8.870593,5.123114,-1.828470,4.037839,-9.726622,-8.338454,1.377504,-7.312183,-6.008662,2.803590,-0.276684,8.659608,-2.245468,-9.135541,-1.403415,3.909377,9.797721,-6.646448,-3.583000,4.375594,-8.129936,-3.095585,-9.604357,-1.322108,3.184664,7.374989,-7.929860,1.991302,1.118151,-9.895380,-7.235207,7.656135,-2.282947,-5.425547,0.359560,4.681898,6.476152,7.020068,-8.536038,-5.643731,6.304834,-7.713666,-3.343767,-9.110115,9.943042,-7.004894,3.502911,5.792477,3.784791,-4.171388,-2.449700,-7.448000,0.998590,3.157976,6.574252,-9.335660,9.933879,3.426100,-6.862188,9.100519,-4.426998,0.076462,-3.890764,-8.138457,-5.105021,-8.707980,-1.896711,-8.400044,7.457460,-7.712980,8.892242,3.335337,3.432849,1.657884,8.964028,9.236711,-5.522583,8.569294,9.555596,-8.045522,-9.896154,-1.662036,-0.443397,-3.578442,-8.574453,-5.822796,2.821577,6.226765,-7.682978,-4.686433,9.910791,-2.788746,6.539167,-0.169770,9.402337,-7.632931,-2.678350,-0.476937,-1.939217,-3.639744,2.489445,-4.801566,-4.750126,0.461820,-5.425438,-2.322917,8.969650,2.528168,-6.554370,-3.248058,3.231311,4.488366,3.494179,-4.471597,7.038193,5.533138,6.459986,4.228137,4.314027,0.512638,1.225399,5.950214,-9.285332,3.183655,9.978123,-9.703340,-4.861439,-5.168417,0.260389,8.027548,7.752094,-2.644146,7.347470,-6.084069,-3.329079,-2.641078,-3.830736,5.183141,0.516877,5.662208,-5.868421,6.921217,-5.395691,-9.536749,-2.348436,-6.493498,-5.702960,-6.143652,-8.069948,-0.335015,-6.742973,-5.178538,4.158862,3.474056,-6.682141,8.271430,-6.402677,-0.955686,-0.572158,9.136413,-3.302332,-7.910473,-1.327626,-9.570860,0.031960,5.451520,-6.429149,-5.556561,9.060037,-0.854248,2.639421,-4.242385,-5.890631,-7.069841,-4.143517,5.119528,4.099626,1.754245,-8.751902,-9.086001,6.795717,-1.701533,-3.010940,1.027936,-5.820524,5.443004,1.000929,-1.615024,-4.271754,-0.788205,-7.383428,-1.816155,7.743157,7.455888,4.782967,5.186307,8.390811,-7.928926,0.197068,-8.481054,7.722990,7.095595,6.923907,-7.817438,-0.138651,-3.737271,-5.934975,-9.755662,6.413866,-6.824665,9.940112,2.368865,3.757059,-9.579077,3.195944,-9.040002,6.140428,9.864154,8.686265,-3.251290,-2.706455,-2.344359,8.421854,-5.655083,-9.710973,-2.220048,-3.332346,6.116603,1.199703,-3.318100,-2.117252,-4.593498,-1.252686,-5.761098,1.265334,7.274200,-0.942206,1.797903,-7.184596,-3.500429,-5.565391,7.568573,-5.489128,-6.606857,-2.075251,-0.835091,6.036101,-8.836293,-5.013623,-1.170162,-3.867046,2.749869,3.027904,-6.715876,-7.759663,7.472804,1.807634,2.286422,9.026254,-2.361708,3.843614,-6.690661,3.658209,-3.707701,0.161897,2.002604,2.739022,-8.995802,2.418196,-1.688838,2.581024,-3.215764,-6.511995,-6.246723,1.569085,-3.074365,5.439023,-0.958340,8.729883,-8.979591,0.875145,-7.393786,-8.838011,2.522992,-4.888684,3.266816,8.661814,-3.202886], dtype = "float64")#candidate|3706|(896,)|const|float64
call_3705 = relay.TupleGetItem(func_1764_call(relay.reshape(const_3706.astype('float64'), [16, 7, 8])), 0)
call_3707 = relay.TupleGetItem(func_1767_call(relay.reshape(const_3706.astype('float64'), [16, 7, 8])), 0)
output = relay.Tuple([call_3683,call_3705,const_3706,])
output2 = relay.Tuple([call_3684,call_3707,const_3706,])
func_3718 = relay.Function([], output)
mod['func_3718'] = func_3718
mod = relay.transform.InferType()(mod)
mutated_mod['func_3718'] = func_3718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3718_call = mutated_mod.get_global_var('func_3718')
call_3719 = func_3718_call()
output = call_3719
func_3720 = relay.Function([], output)
mutated_mod['func_3720'] = func_3720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2122_call = mod.get_global_var('func_2122')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_3734 = relay.TupleGetItem(func_2122_call(), 5)
call_3735 = relay.TupleGetItem(func_2124_call(), 5)
func_2490_call = mod.get_global_var('func_2490')
func_2494_call = mutated_mod.get_global_var('func_2494')
var_3746 = relay.var("var_3746", dtype = "float64", shape = (224, 4))#candidate|3746|(224, 4)|var|float64
call_3745 = relay.TupleGetItem(func_2490_call(relay.reshape(var_3746.astype('float64'), [16, 7, 8]), relay.reshape(call_3734.astype('float64'), [56,]), ), 0)
call_3747 = relay.TupleGetItem(func_2494_call(relay.reshape(var_3746.astype('float64'), [16, 7, 8]), relay.reshape(call_3734.astype('float64'), [56,]), ), 0)
uop_3749 = relay.acos(call_3734.astype('float64')) # shape=(1, 7, 8)
uop_3751 = relay.acos(call_3735.astype('float64')) # shape=(1, 7, 8)
uop_3766 = relay.rsqrt(var_3746.astype('float64')) # shape=(224, 4)
func_2490_call = mod.get_global_var('func_2490')
func_2494_call = mutated_mod.get_global_var('func_2494')
call_3776 = relay.TupleGetItem(func_2490_call(relay.reshape(call_3745.astype('float64'), [16, 7, 8]), relay.reshape(call_3734.astype('float64'), [56,]), ), 2)
call_3777 = relay.TupleGetItem(func_2494_call(relay.reshape(call_3745.astype('float64'), [16, 7, 8]), relay.reshape(call_3734.astype('float64'), [56,]), ), 2)
uop_3784 = relay.acos(uop_3766.astype('float32')) # shape=(224, 4)
uop_3786 = relay.sinh(uop_3784.astype('float64')) # shape=(224, 4)
uop_3788 = relay.cos(uop_3784.astype('float64')) # shape=(224, 4)
bop_3791 = relay.logical_xor(uop_3788.astype('uint16'), relay.reshape(uop_3784.astype('uint16'), relay.shape_of(uop_3788))) # shape=(224, 4)
func_2122_call = mod.get_global_var('func_2122')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_3796 = relay.TupleGetItem(func_2122_call(), 5)
call_3797 = relay.TupleGetItem(func_2124_call(), 5)
output = relay.Tuple([call_3745,uop_3749,call_3776,uop_3786,bop_3791,call_3796,])
output2 = relay.Tuple([call_3747,uop_3751,call_3777,uop_3786,bop_3791,call_3797,])
func_3805 = relay.Function([var_3746,], output)
mod['func_3805'] = func_3805
mod = relay.transform.InferType()(mod)
var_3806 = relay.var("var_3806", dtype = "float64", shape = (224, 4))#candidate|3806|(224, 4)|var|float64
output = func_3805(var_3806)
func_3807 = relay.Function([var_3806], output)
mutated_mod['func_3807'] = func_3807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_926_call = mutated_mod.get_global_var('func_926')
call_3887 = func_925_call()
call_3888 = func_925_call()
var_3891 = relay.var("var_3891", dtype = "float32", shape = (1, 7, 8))#candidate|3891|(1, 7, 8)|var|float32
bop_3892 = relay.right_shift(call_3887.astype('uint8'), relay.reshape(var_3891.astype('uint8'), relay.shape_of(call_3887))) # shape=(1, 7, 8)
bop_3895 = relay.right_shift(call_3888.astype('uint8'), relay.reshape(var_3891.astype('uint8'), relay.shape_of(call_3888))) # shape=(1, 7, 8)
func_3329_call = mod.get_global_var('func_3329')
func_3332_call = mutated_mod.get_global_var('func_3332')
var_3914 = relay.var("var_3914", dtype = "float64", shape = (150,))#candidate|3914|(150,)|var|float64
call_3913 = relay.TupleGetItem(func_3329_call(relay.reshape(var_3914.astype('float64'), [5, 15, 2])), 0)
call_3915 = relay.TupleGetItem(func_3332_call(relay.reshape(var_3914.astype('float64'), [5, 15, 2])), 0)
output = relay.Tuple([bop_3892,call_3913,var_3914,])
output2 = relay.Tuple([bop_3895,call_3915,var_3914,])
func_3918 = relay.Function([var_3891,var_3914,], output)
mod['func_3918'] = func_3918
mod = relay.transform.InferType()(mod)
mutated_mod['func_3918'] = func_3918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3918_call = mutated_mod.get_global_var('func_3918')
var_3920 = relay.var("var_3920", dtype = "float32", shape = (1, 7, 8))#candidate|3920|(1, 7, 8)|var|float32
var_3921 = relay.var("var_3921", dtype = "float64", shape = (150,))#candidate|3921|(150,)|var|float64
call_3919 = func_3918_call(var_3920,var_3921,)
output = call_3919
func_3922 = relay.Function([var_3920,var_3921,], output)
mutated_mod['func_3922'] = func_3922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_3953 = relay.TupleGetItem(func_1071_call(), 0)
call_3954 = relay.TupleGetItem(func_1073_call(), 0)
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_3976 = relay.TupleGetItem(func_3034_call(), 0)
call_3977 = relay.TupleGetItem(func_3035_call(), 0)
output = relay.Tuple([call_3953,call_3976,])
output2 = relay.Tuple([call_3954,call_3977,])
func_3984 = relay.Function([], output)
mod['func_3984'] = func_3984
mod = relay.transform.InferType()(mod)
output = func_3984()
func_3985 = relay.Function([], output)
mutated_mod['func_3985'] = func_3985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2971_call = mod.get_global_var('func_2971')
func_2972_call = mutated_mod.get_global_var('func_2972')
call_4028 = relay.TupleGetItem(func_2971_call(), 2)
call_4029 = relay.TupleGetItem(func_2972_call(), 2)
var_4034 = relay.var("var_4034", dtype = "uint8", shape = (324, 14))#candidate|4034|(324, 14)|var|uint8
bop_4035 = relay.logical_and(call_4028.astype('bool'), var_4034.astype('bool')) # shape=(324, 14)
bop_4038 = relay.logical_and(call_4029.astype('bool'), var_4034.astype('bool')) # shape=(324, 14)
var_4040 = relay.var("var_4040", dtype = "uint8", shape = (324, 14))#candidate|4040|(324, 14)|var|uint8
bop_4041 = relay.less(var_4034.astype('bool'), relay.reshape(var_4040.astype('bool'), relay.shape_of(var_4034))) # shape=(324, 14)
func_1594_call = mod.get_global_var('func_1594')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_4059 = func_1594_call()
call_4060 = func_1594_call()
output = relay.Tuple([bop_4035,bop_4041,call_4059,])
output2 = relay.Tuple([bop_4038,bop_4041,call_4060,])
func_4066 = relay.Function([var_4034,var_4040,], output)
mod['func_4066'] = func_4066
mod = relay.transform.InferType()(mod)
var_4067 = relay.var("var_4067", dtype = "uint8", shape = (324, 14))#candidate|4067|(324, 14)|var|uint8
var_4068 = relay.var("var_4068", dtype = "uint8", shape = (324, 14))#candidate|4068|(324, 14)|var|uint8
output = func_4066(var_4067,var_4068,)
func_4069 = relay.Function([var_4067,var_4068,], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4100 = relay.var("var_4100", dtype = "float32", shape = ())#candidate|4100|()|var|float32
const_4101 = relay.const([[[2.497455,9.181918,6.562809,-9.369714,-1.587062,9.138471,7.936231,-0.173088,9.977341]],[[-9.690029,4.127103,-0.582255,-6.681696,4.563186,6.936263,-4.722400,-4.341783,-3.430567]],[[3.209801,7.478632,9.483502,8.119207,-6.581187,-7.394355,0.195383,1.573314,-6.864427]],[[0.432071,-5.780775,-9.504869,4.538201,-9.612228,-3.309117,6.418516,-1.574835,-4.564279]],[[1.985657,-4.446432,6.295242,-4.161238,3.296245,9.487027,4.564181,4.803361,4.514212]],[[1.478041,-0.886383,6.914593,-4.756034,-7.829112,3.157394,7.103802,-5.870053,-2.595249]],[[-1.038528,-8.768941,4.004143,7.860546,-3.614558,-6.595536,-6.452722,-6.763305,6.009927]],[[-9.495760,3.361968,-5.411179,9.999931,4.746254,8.301490,3.013184,-3.695609,-2.013801]],[[2.682144,-6.986432,-3.164376,6.096256,8.341708,9.861825,8.765939,-9.778847,-9.682786]],[[-1.772684,-7.573231,-0.856734,3.169537,-0.497745,5.125152,3.018594,-0.385296,3.230143]],[[-5.466213,-5.814744,-4.451687,5.109230,5.220240,-3.679623,-4.378303,4.654689,4.906056]],[[7.473192,9.329261,-5.421069,-4.189712,3.135637,-0.113967,1.796642,6.032908,-1.459781]],[[7.400462,-0.636737,6.105177,-1.086914,7.927863,2.815967,1.128358,4.336589,-9.070376]],[[-0.777730,-2.398221,1.667716,-4.821453,4.868256,-2.498747,1.222334,8.153155,-6.658588]],[[0.658728,8.328770,-1.313546,4.136650,0.571573,-2.152670,-2.718204,-2.240957,-3.277345]]], dtype = "float32")#candidate|4101|(15, 1, 9)|const|float32
bop_4102 = relay.floor_divide(var_4100.astype('float32'), const_4101.astype('float32')) # shape=(15, 1, 9)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_4110 = relay.TupleGetItem(func_1894_call(), 0)
call_4111 = relay.TupleGetItem(func_1896_call(), 0)
output = relay.Tuple([bop_4102,call_4110,])
output2 = relay.Tuple([bop_4102,call_4111,])
func_4112 = relay.Function([var_4100,], output)
mod['func_4112'] = func_4112
mod = relay.transform.InferType()(mod)
mutated_mod['func_4112'] = func_4112
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4113 = relay.var("var_4113", dtype = "float32", shape = ())#candidate|4113|()|var|float32
func_4112_call = mutated_mod.get_global_var('func_4112')
call_4114 = func_4112_call(var_4113)
output = call_4114
func_4115 = relay.Function([var_4113], output)
mutated_mod['func_4115'] = func_4115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mod.get_global_var('func_1071')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_4122 = relay.TupleGetItem(func_1071_call(), 0)
call_4123 = relay.TupleGetItem(func_1073_call(), 0)
output = call_4122
output2 = call_4123
func_4134 = relay.Function([], output)
mod['func_4134'] = func_4134
mod = relay.transform.InferType()(mod)
output = func_4134()
func_4135 = relay.Function([], output)
mutated_mod['func_4135'] = func_4135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_4159 = relay.TupleGetItem(func_3034_call(), 0)
call_4160 = relay.TupleGetItem(func_3035_call(), 0)
output = call_4159
output2 = call_4160
func_4169 = relay.Function([], output)
mod['func_4169'] = func_4169
mod = relay.transform.InferType()(mod)
mutated_mod['func_4169'] = func_4169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4169_call = mutated_mod.get_global_var('func_4169')
call_4170 = func_4169_call()
output = call_4170
func_4171 = relay.Function([], output)
mutated_mod['func_4171'] = func_4171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1578_call = mod.get_global_var('func_1578')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_4231 = relay.TupleGetItem(func_1578_call(), 1)
call_4232 = relay.TupleGetItem(func_1579_call(), 1)
output = call_4231
output2 = call_4232
func_4254 = relay.Function([], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4254_call = mutated_mod.get_global_var('func_4254')
call_4255 = func_4254_call()
output = call_4255
func_4256 = relay.Function([], output)
mutated_mod['func_4256'] = func_4256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1260_call = mod.get_global_var('func_1260')
func_1262_call = mutated_mod.get_global_var('func_1262')
call_4270 = relay.TupleGetItem(func_1260_call(), 0)
call_4271 = relay.TupleGetItem(func_1262_call(), 0)
output = relay.Tuple([call_4270,])
output2 = relay.Tuple([call_4271,])
func_4280 = relay.Function([], output)
mod['func_4280'] = func_4280
mod = relay.transform.InferType()(mod)
output = func_4280()
func_4281 = relay.Function([], output)
mutated_mod['func_4281'] = func_4281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3984_call = mod.get_global_var('func_3984')
func_3985_call = mutated_mod.get_global_var('func_3985')
call_4300 = relay.TupleGetItem(func_3984_call(), 1)
call_4301 = relay.TupleGetItem(func_3985_call(), 1)
func_676_call = mod.get_global_var('func_676')
func_677_call = mutated_mod.get_global_var('func_677')
call_4312 = relay.TupleGetItem(func_676_call(), 0)
call_4313 = relay.TupleGetItem(func_677_call(), 0)
var_4315 = relay.var("var_4315", dtype = "float64", shape = (5, 15, 2))#candidate|4315|(5, 15, 2)|var|float64
bop_4316 = relay.less_equal(call_4312.astype('bool'), relay.reshape(var_4315.astype('bool'), relay.shape_of(call_4312))) # shape=(5, 15, 2)
bop_4319 = relay.less_equal(call_4313.astype('bool'), relay.reshape(var_4315.astype('bool'), relay.shape_of(call_4313))) # shape=(5, 15, 2)
output = relay.Tuple([call_4300,bop_4316,])
output2 = relay.Tuple([call_4301,bop_4319,])
func_4325 = relay.Function([var_4315,], output)
mod['func_4325'] = func_4325
mod = relay.transform.InferType()(mod)
mutated_mod['func_4325'] = func_4325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4326 = relay.var("var_4326", dtype = "float64", shape = (5, 15, 2))#candidate|4326|(5, 15, 2)|var|float64
func_4325_call = mutated_mod.get_global_var('func_4325')
call_4327 = func_4325_call(var_4326)
output = call_4327
func_4328 = relay.Function([var_4326], output)
mutated_mod['func_4328'] = func_4328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3132_call = mod.get_global_var('func_3132')
func_3133_call = mutated_mod.get_global_var('func_3133')
call_4336 = func_3132_call()
call_4337 = func_3132_call()
output = relay.Tuple([call_4336,])
output2 = relay.Tuple([call_4337,])
func_4349 = relay.Function([], output)
mod['func_4349'] = func_4349
mod = relay.transform.InferType()(mod)
output = func_4349()
func_4350 = relay.Function([], output)
mutated_mod['func_4350'] = func_4350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4349_call = mod.get_global_var('func_4349')
func_4350_call = mutated_mod.get_global_var('func_4350')
call_4367 = relay.TupleGetItem(func_4349_call(), 0)
call_4368 = relay.TupleGetItem(func_4350_call(), 0)
func_1594_call = mod.get_global_var('func_1594')
func_1595_call = mutated_mod.get_global_var('func_1595')
call_4371 = func_1594_call()
call_4372 = func_1594_call()
output = relay.Tuple([call_4367,call_4371,])
output2 = relay.Tuple([call_4368,call_4372,])
func_4382 = relay.Function([], output)
mod['func_4382'] = func_4382
mod = relay.transform.InferType()(mod)
output = func_4382()
func_4383 = relay.Function([], output)
mutated_mod['func_4383'] = func_4383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_926_call = mutated_mod.get_global_var('func_926')
call_4445 = func_925_call()
call_4446 = func_925_call()
output = call_4445
output2 = call_4446
func_4449 = relay.Function([], output)
mod['func_4449'] = func_4449
mod = relay.transform.InferType()(mod)
output = func_4449()
func_4450 = relay.Function([], output)
mutated_mod['func_4450'] = func_4450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_4469 = func_2899_call()
call_4470 = func_2899_call()
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_4496 = func_526_call()
call_4497 = func_526_call()
output = relay.Tuple([call_4469,call_4496,])
output2 = relay.Tuple([call_4470,call_4497,])
func_4521 = relay.Function([], output)
mod['func_4521'] = func_4521
mod = relay.transform.InferType()(mod)
mutated_mod['func_4521'] = func_4521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4521_call = mutated_mod.get_global_var('func_4521')
call_4522 = func_4521_call()
output = call_4522
func_4523 = relay.Function([], output)
mutated_mod['func_4523'] = func_4523
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4524 = relay.var("var_4524", dtype = "int64", shape = (2, 8, 15))#candidate|4524|(2, 8, 15)|var|int64
var_4525 = relay.var("var_4525", dtype = "int64", shape = (2, 8, 15))#candidate|4525|(2, 8, 15)|var|int64
bop_4526 = relay.logical_xor(var_4524.astype('int64'), relay.reshape(var_4525.astype('int64'), relay.shape_of(var_4524))) # shape=(2, 8, 15)
func_4280_call = mod.get_global_var('func_4280')
func_4281_call = mutated_mod.get_global_var('func_4281')
call_4535 = relay.TupleGetItem(func_4280_call(), 0)
call_4536 = relay.TupleGetItem(func_4281_call(), 0)
output = relay.Tuple([bop_4526,call_4535,])
output2 = relay.Tuple([bop_4526,call_4536,])
func_4548 = relay.Function([var_4524,var_4525,], output)
mod['func_4548'] = func_4548
mod = relay.transform.InferType()(mod)
var_4549 = relay.var("var_4549", dtype = "int64", shape = (2, 8, 15))#candidate|4549|(2, 8, 15)|var|int64
var_4550 = relay.var("var_4550", dtype = "int64", shape = (2, 8, 15))#candidate|4550|(2, 8, 15)|var|int64
output = func_4548(var_4549,var_4550,)
func_4551 = relay.Function([var_4549,var_4550,], output)
mutated_mod['func_4551'] = func_4551
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4562 = relay.const([[[-3.687914,-5.192238,5.148836,-3.863375,7.048209,-4.134449,-6.914774,-6.296490,-5.658734],[-0.134255,2.597244,4.313195,-0.642298,-5.892724,-0.692435,6.461457,6.147197,-1.577122],[-1.097506,-7.563529,-1.767066,-2.416335,-1.784092,8.227658,1.472652,9.282166,-5.765260],[1.988294,7.418600,9.099169,8.051790,-8.064824,-3.940572,-3.775416,-5.114448,0.275844],[8.677397,0.648022,-4.191400,-1.057553,-2.714529,-8.645956,-7.990250,0.178669,-5.255172],[1.213406,6.138157,-0.683244,7.161328,7.677177,4.006123,-4.554120,-6.530580,3.046549],[-9.188469,-4.250096,8.862254,-9.011061,-7.334209,8.907399,-6.026244,3.459039,2.347850],[0.796407,-3.214931,-4.009729,4.158309,-1.278542,-3.777072,-7.599950,3.679845,4.742652],[-5.956916,-4.706721,7.896824,9.804855,-9.192521,-3.363203,-6.419128,-1.919257,-4.656126],[0.792129,-3.122885,5.864700,0.243085,0.646087,0.087148,0.567055,-6.975767,-3.698607],[-0.523867,2.083362,-4.653308,-8.138977,-7.732530,8.614642,5.107136,-2.999083,-2.103074],[-8.858642,-2.317563,-0.628392,-3.769127,3.500346,6.173455,-2.073667,4.502288,4.761988]],[[1.551100,-0.455528,-8.756166,-7.090950,-5.200801,6.021463,1.550125,-5.123676,-9.817290],[8.791427,5.464846,1.733760,-0.866645,-7.963693,-0.287977,-5.273522,0.329930,0.958819],[-5.487829,2.952051,-2.516109,-8.140244,-8.084025,2.510631,4.836276,3.251642,1.894969],[-5.982534,-1.816206,0.014994,-1.205579,9.311733,0.478676,4.938688,-7.535781,-7.872966],[-8.296003,-1.534795,-6.483229,0.436364,-2.981318,-0.129982,5.522408,-6.368212,4.734568],[-6.440979,6.330828,5.367727,-6.329288,-6.587057,1.272256,-4.097270,9.402194,-6.763858],[-3.280268,-5.756422,-5.831385,5.145126,0.145638,8.862120,2.870239,-8.590593,9.119282],[5.546315,-7.236486,4.810995,6.870065,4.271556,-3.863095,-3.241949,4.915448,-0.843562],[4.480101,-7.444396,5.097608,9.637782,0.204250,0.826246,7.815676,4.401508,-2.400935],[1.742472,-3.010219,1.631869,-3.133166,8.893019,-7.547625,3.487628,3.768685,-9.325646],[8.764532,-9.405930,0.660361,-5.656472,-2.676736,-8.097562,-8.427064,-7.551888,9.605342],[4.835498,0.553188,2.479533,-4.018607,7.743195,-8.031152,-0.265183,8.262421,5.137048]],[[-5.934199,3.395575,1.375972,-4.928702,6.673851,-5.250127,-1.834296,-7.163782,-5.396411],[7.712862,-7.276990,1.739638,-4.431140,0.384565,-5.333908,-4.013668,-3.031571,7.663748],[8.282415,2.425072,8.708886,2.166481,0.513171,8.090245,-1.536561,4.382928,-6.624718],[7.703610,-9.816285,-4.820766,9.253243,-5.806761,3.262701,6.824433,3.093062,2.149401],[-3.699673,-6.882126,7.814657,-7.410791,-0.149024,-8.645956,-6.044966,8.372238,-8.350044],[8.528151,-3.361349,2.441862,1.736711,-4.756812,2.088401,4.611186,3.994567,-4.582982],[-7.951007,-1.305693,-6.197803,9.944592,-9.680310,1.618118,-6.942490,0.903434,-7.445449],[-2.983130,2.254880,-2.045738,9.074866,0.511406,5.728417,2.621061,-1.884373,-3.390114],[-1.849016,8.858884,-4.648484,-8.137366,1.502986,9.727669,-0.848993,3.799141,2.396013],[8.466803,-6.750946,3.022990,-6.431994,4.349479,-8.512195,2.160520,4.068277,1.323952],[0.014515,-3.414352,0.188418,1.678613,-9.052790,-2.574289,-7.412964,-4.484747,-3.072311],[6.251979,-2.637168,8.928414,-0.960867,3.712232,8.083249,-3.529664,-1.205168,6.983216]],[[-2.846965,-8.664348,7.872106,-1.873105,-8.814031,-1.231100,-1.730550,9.521374,-1.849482],[7.808080,4.422727,-8.878025,-7.826616,9.998968,-1.167213,-8.608834,0.848521,5.703957],[7.094774,0.239013,-0.375628,-0.266787,0.820788,9.836061,-0.040922,-8.787877,4.024997],[-5.138797,6.768214,1.151537,-1.766367,1.792566,-0.953556,7.635187,-0.300034,5.302518],[-9.059386,-4.881343,8.715461,-0.327268,-8.139715,1.248718,9.641808,4.724538,9.074800],[-2.430965,9.055120,-1.068112,-2.991100,1.016594,-5.695758,3.936804,8.197181,-8.303470],[5.760652,-9.989845,6.723602,-2.908440,-0.910171,-5.331590,-3.808908,0.152032,-5.586582],[1.640289,1.842985,6.428024,3.760746,4.165086,-7.530394,2.376211,-2.985756,-9.342166],[2.988096,-1.916716,-3.551907,8.778726,-2.228760,-0.999690,-3.208913,9.741264,4.008961],[8.745389,-8.954277,1.375193,-1.136327,-2.267245,-8.987999,3.894083,2.928702,7.511456],[-2.491683,-6.297631,-2.310709,0.588976,-0.724150,-0.149866,7.617298,-8.434342,-7.762023],[9.817541,-6.200215,0.896216,-1.894539,-6.952918,7.871216,6.248140,3.353609,-8.350708]],[[8.535971,-0.765727,-5.297686,0.609723,1.229221,9.805963,4.658453,-8.259473,9.619605],[-9.063909,-1.065482,4.135537,4.450060,8.675495,0.994938,-8.520898,0.793342,-1.076581],[6.549959,-0.213583,-5.670755,1.721618,-3.255291,4.536962,8.973558,1.989801,4.946654],[1.941580,5.023890,8.143166,-6.156078,0.496609,-8.204934,-9.308684,6.936015,-4.434986],[-2.116572,8.618351,-2.101242,-3.727486,4.272689,5.806088,7.638916,8.422013,-7.932983],[1.732272,-4.453103,-5.976000,-7.522827,-0.789763,8.648975,1.004905,-7.061659,-1.769770],[-4.810302,6.568913,-1.045295,-3.419853,9.237044,1.143856,-0.536671,6.286460,4.035339],[3.737754,-8.736338,-8.669139,4.108010,6.821827,-7.962858,-4.097281,7.016861,-4.033735],[-9.522970,0.439299,-9.471274,6.334402,3.529023,8.936993,8.302476,-7.693543,3.146800],[5.046094,8.589166,-5.153231,0.482662,-4.444905,-9.306030,-0.427823,4.601390,3.443152],[-2.845209,-7.978815,6.538904,3.702351,-9.086491,-8.953764,-2.620961,-0.367218,-2.855739],[4.366057,7.776558,-9.338315,7.492501,3.459749,-9.045444,-9.273191,5.110089,-9.660346]],[[9.837334,5.822210,-7.095409,6.845933,-7.220774,-6.221823,-7.388779,-2.922960,6.899601],[-6.231864,5.602096,0.998051,-8.579835,2.379834,-0.753514,-6.444106,2.458966,5.263628],[9.447301,-4.243972,4.420491,-7.342377,-2.831184,3.024208,-2.574480,-9.889224,1.649440],[0.470729,-0.004629,-9.891587,2.909586,-1.699463,-7.774821,-1.611748,-1.364188,4.781198],[2.476933,1.857433,-9.250883,0.492070,-7.410896,0.231755,4.383056,2.298309,2.276657],[-7.128189,-7.002981,9.334910,-8.017335,-7.041537,-4.794119,-1.786278,-0.209587,7.822620],[5.845494,5.614881,3.982671,6.292883,1.521146,-9.948463,-1.570838,2.491998,8.527996],[-9.857700,-2.701273,-6.909551,-3.632467,-9.701621,-7.613143,-9.074370,-2.813720,-1.165985],[-1.803261,-3.536935,-5.535490,-3.128958,3.001711,-6.134213,-1.046450,5.626976,3.749744],[6.758816,-5.796593,-8.071930,9.947154,-7.618517,-5.422176,5.142138,8.894417,9.520230],[-5.449692,-8.547413,6.513030,-5.631043,1.345182,8.469188,4.109844,6.616390,-3.388183],[2.223840,-3.153792,-1.184928,-8.676137,9.639397,9.616198,6.864875,-9.558469,-5.441432]],[[-6.671865,6.611909,-6.053118,6.797903,6.383221,1.364358,-4.316025,6.663322,7.779290],[-2.006579,-5.631600,3.998202,-7.344259,4.356329,-6.171508,-2.431061,0.206454,4.057414],[-8.650295,0.945501,9.075709,-0.773997,2.131942,-9.883099,9.243578,-5.651852,-8.910287],[8.925656,9.174188,4.980533,-8.683958,-8.306085,0.217005,4.043079,-6.927702,6.306176],[-5.077916,-9.547678,2.004277,-7.499367,5.922398,-5.833289,-1.804024,-7.110365,6.087454],[9.018281,3.346090,6.036993,0.060995,6.234636,6.330782,4.291319,-3.830067,-7.312239],[-4.067087,-6.820776,9.225561,7.070074,-0.577349,4.259522,5.349766,-4.589223,9.115141],[7.937122,-8.914701,-0.064820,1.979012,4.432072,6.822534,-6.008915,-9.943250,1.985376],[7.785064,3.761847,-7.865360,2.186230,-3.036078,5.901644,9.623714,-7.018568,9.778251],[-6.408630,3.105053,-3.366948,1.478002,-5.210062,6.471451,0.252455,8.339061,-2.351287],[-4.511982,5.705115,6.091932,-6.894570,-0.056818,3.733433,9.851257,-9.355291,1.128011],[-9.816473,6.350903,8.656637,-1.432491,-6.209313,1.977830,-8.823506,-4.897435,-4.700076]],[[-3.761995,1.672747,-1.231573,-6.047216,-8.238736,-1.430721,2.277546,-5.609246,6.867700],[2.258636,-9.570182,4.834160,-6.294374,3.517999,-5.103520,0.221110,-5.358074,1.394706],[8.466587,3.256335,-9.018349,7.284611,-3.457466,6.837728,3.766409,6.364274,-2.367142],[-8.865087,-8.877339,3.873818,7.702329,5.537701,0.393567,-1.637535,-4.623558,-3.060372],[9.762784,-4.203609,1.622607,-3.116833,-6.188635,3.150339,-8.620145,-5.597681,1.101354],[7.130973,-3.721141,8.110945,2.897950,-9.787402,7.593250,5.258035,-0.682699,-7.964700],[5.517344,6.441838,-5.205967,-9.528194,-3.350814,-5.450038,-6.648014,-8.206890,-3.181131],[8.824331,-7.352896,-6.870602,-7.756032,-1.874068,7.676231,3.102056,7.590308,2.209757],[4.385272,3.364507,-0.011266,7.603640,9.942276,3.407581,4.527866,-6.282550,-1.423675],[3.457597,-0.979216,5.264007,-3.354056,-1.987311,5.668487,-2.801038,9.173251,-8.249682],[1.519069,-2.454466,-9.507745,-5.094210,-3.765351,5.398393,9.654377,-5.693846,-7.699754],[-3.211660,-3.376368,9.790172,-9.445566,-1.491677,6.606107,3.339240,-2.434793,7.542277]],[[2.752347,3.438387,-6.233980,-3.662959,5.737617,9.096358,-5.968553,3.724139,-3.358112],[0.896600,-4.353843,-4.251240,-8.493177,-4.734165,-2.559164,5.754829,4.797984,2.705437],[5.121882,-4.812318,-9.459657,0.608186,8.277782,6.315662,8.071732,-5.395088,-7.422655],[7.159269,-9.315210,-9.767070,3.672445,-6.123151,-1.784833,6.636885,6.565797,-4.164839],[8.361961,-6.424828,-6.866834,5.293153,-2.721832,6.707822,-3.067665,-6.014613,-4.805164],[3.549240,-9.353832,2.187603,-9.067449,6.896036,-1.462462,0.232723,5.394511,-1.913566],[-5.791342,3.184656,7.894176,0.259256,9.131653,-4.714377,-7.394270,9.991219,3.346581],[1.664254,1.284186,5.698475,6.599103,-1.721066,-5.284358,-9.770311,-6.231008,-7.042796],[3.771428,0.889988,4.835344,-6.942058,-9.601615,-9.982825,-7.276256,3.354277,-0.272289],[9.684195,8.251353,-0.332206,-7.902761,-7.189754,-9.185517,-1.132240,8.032901,-6.099063],[3.858983,-3.316372,7.584171,4.189990,4.735942,2.862314,4.411688,3.320026,-9.526316],[5.030774,-4.965968,0.373272,-6.793150,-5.773124,-8.153744,-0.331093,-8.870188,9.399269]]], dtype = "float32")#candidate|4562|(9, 12, 9)|const|float32
uop_4563 = relay.atan(const_4562.astype('float32')) # shape=(9, 12, 9)
output = relay.Tuple([uop_4563,])
output2 = relay.Tuple([uop_4563,])
func_4581 = relay.Function([], output)
mod['func_4581'] = func_4581
mod = relay.transform.InferType()(mod)
mutated_mod['func_4581'] = func_4581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4581_call = mutated_mod.get_global_var('func_4581')
call_4582 = func_4581_call()
output = call_4582
func_4583 = relay.Function([], output)
mutated_mod['func_4583'] = func_4583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2291_call = mod.get_global_var('func_2291')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_4652 = relay.TupleGetItem(func_2291_call(), 1)
call_4653 = relay.TupleGetItem(func_2293_call(), 1)
output = relay.Tuple([call_4652,])
output2 = relay.Tuple([call_4653,])
func_4659 = relay.Function([], output)
mod['func_4659'] = func_4659
mod = relay.transform.InferType()(mod)
output = func_4659()
func_4660 = relay.Function([], output)
mutated_mod['func_4660'] = func_4660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_4759 = relay.TupleGetItem(func_3536_call(), 0)
call_4760 = relay.TupleGetItem(func_3537_call(), 0)
output = relay.Tuple([call_4759,])
output2 = relay.Tuple([call_4760,])
func_4778 = relay.Function([], output)
mod['func_4778'] = func_4778
mod = relay.transform.InferType()(mod)
mutated_mod['func_4778'] = func_4778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4778_call = mutated_mod.get_global_var('func_4778')
call_4779 = func_4778_call()
output = call_4779
func_4780 = relay.Function([], output)
mutated_mod['func_4780'] = func_4780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_4862 = func_526_call()
call_4863 = func_526_call()
output = relay.Tuple([call_4862,])
output2 = relay.Tuple([call_4863,])
func_4870 = relay.Function([], output)
mod['func_4870'] = func_4870
mod = relay.transform.InferType()(mod)
output = func_4870()
func_4871 = relay.Function([], output)
mutated_mod['func_4871'] = func_4871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4877 = relay.var("var_4877", dtype = "float32", shape = (5, 11, 1))#candidate|4877|(5, 11, 1)|var|float32
uop_4878 = relay.tan(var_4877.astype('float32')) # shape=(5, 11, 1)
output = uop_4878
output2 = uop_4878
func_4880 = relay.Function([var_4877,], output)
mod['func_4880'] = func_4880
mod = relay.transform.InferType()(mod)
mutated_mod['func_4880'] = func_4880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4881 = relay.var("var_4881", dtype = "float32", shape = (5, 11, 1))#candidate|4881|(5, 11, 1)|var|float32
func_4880_call = mutated_mod.get_global_var('func_4880')
call_4882 = func_4880_call(var_4881)
output = call_4882
func_4883 = relay.Function([var_4881], output)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4934 = relay.var("var_4934", dtype = "float32", shape = (9, 11, 11))#candidate|4934|(9, 11, 11)|var|float32
uop_4935 = relay.log(var_4934.astype('float32')) # shape=(9, 11, 11)
output = relay.Tuple([uop_4935,])
output2 = relay.Tuple([uop_4935,])
func_4942 = relay.Function([var_4934,], output)
mod['func_4942'] = func_4942
mod = relay.transform.InferType()(mod)
mutated_mod['func_4942'] = func_4942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4943 = relay.var("var_4943", dtype = "float32", shape = (9, 11, 11))#candidate|4943|(9, 11, 11)|var|float32
func_4942_call = mutated_mod.get_global_var('func_4942')
call_4944 = func_4942_call(var_4943)
output = call_4944
func_4945 = relay.Function([var_4943], output)
mutated_mod['func_4945'] = func_4945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2643_call = mod.get_global_var('func_2643')
func_2644_call = mutated_mod.get_global_var('func_2644')
call_4987 = func_2643_call()
call_4988 = func_2643_call()
func_2053_call = mod.get_global_var('func_2053')
func_2056_call = mutated_mod.get_global_var('func_2056')
var_5003 = relay.var("var_5003", dtype = "float64", shape = (1, 45))#candidate|5003|(1, 45)|var|float64
call_5002 = relay.TupleGetItem(func_2053_call(relay.reshape(var_5003.astype('float64'), [1, 45])), 1)
call_5004 = relay.TupleGetItem(func_2056_call(relay.reshape(var_5003.astype('float64'), [1, 45])), 1)
output = relay.Tuple([call_4987,call_5002,var_5003,])
output2 = relay.Tuple([call_4988,call_5004,var_5003,])
func_5019 = relay.Function([var_5003,], output)
mod['func_5019'] = func_5019
mod = relay.transform.InferType()(mod)
var_5020 = relay.var("var_5020", dtype = "float64", shape = (1, 45))#candidate|5020|(1, 45)|var|float64
output = func_5019(var_5020)
func_5021 = relay.Function([var_5020], output)
mutated_mod['func_5021'] = func_5021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3132_call = mod.get_global_var('func_3132')
func_3133_call = mutated_mod.get_global_var('func_3133')
call_5075 = func_3132_call()
call_5076 = func_3132_call()
func_1340_call = mod.get_global_var('func_1340')
func_1343_call = mutated_mod.get_global_var('func_1343')
var_5079 = relay.var("var_5079", dtype = "float64", shape = (504,))#candidate|5079|(504,)|var|float64
call_5078 = relay.TupleGetItem(func_1340_call(relay.reshape(var_5079.astype('float64'), [9, 7, 8])), 0)
call_5080 = relay.TupleGetItem(func_1343_call(relay.reshape(var_5079.astype('float64'), [9, 7, 8])), 0)
func_2675_call = mod.get_global_var('func_2675')
func_2676_call = mutated_mod.get_global_var('func_2676')
call_5089 = relay.TupleGetItem(func_2675_call(), 0)
call_5090 = relay.TupleGetItem(func_2676_call(), 0)
func_2411_call = mod.get_global_var('func_2411')
func_2414_call = mutated_mod.get_global_var('func_2414')
var_5097 = relay.var("var_5097", dtype = "uint8", shape = (18, 18))#candidate|5097|(18, 18)|var|uint8
call_5096 = func_2411_call(relay.reshape(var_5097.astype('uint8'), [9, 3, 12]))
call_5098 = func_2411_call(relay.reshape(var_5097.astype('uint8'), [9, 3, 12]))
output = relay.Tuple([call_5075,call_5078,var_5079,call_5089,call_5096,var_5097,])
output2 = relay.Tuple([call_5076,call_5080,var_5079,call_5090,call_5098,var_5097,])
func_5103 = relay.Function([var_5079,var_5097,], output)
mod['func_5103'] = func_5103
mod = relay.transform.InferType()(mod)
var_5104 = relay.var("var_5104", dtype = "float64", shape = (504,))#candidate|5104|(504,)|var|float64
var_5105 = relay.var("var_5105", dtype = "uint8", shape = (18, 18))#candidate|5105|(18, 18)|var|uint8
output = func_5103(var_5104,var_5105,)
func_5106 = relay.Function([var_5104,var_5105,], output)
mutated_mod['func_5106'] = func_5106
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5138 = relay.var("var_5138", dtype = "uint8", shape = (14, 8, 6))#candidate|5138|(14, 8, 6)|var|uint8
var_5139 = relay.var("var_5139", dtype = "uint8", shape = (14, 8, 6))#candidate|5139|(14, 8, 6)|var|uint8
bop_5140 = relay.bitwise_xor(var_5138.astype('uint8'), relay.reshape(var_5139.astype('uint8'), relay.shape_of(var_5138))) # shape=(14, 8, 6)
output = relay.Tuple([bop_5140,])
output2 = relay.Tuple([bop_5140,])
func_5146 = relay.Function([var_5138,var_5139,], output)
mod['func_5146'] = func_5146
mod = relay.transform.InferType()(mod)
var_5147 = relay.var("var_5147", dtype = "uint8", shape = (14, 8, 6))#candidate|5147|(14, 8, 6)|var|uint8
var_5148 = relay.var("var_5148", dtype = "uint8", shape = (14, 8, 6))#candidate|5148|(14, 8, 6)|var|uint8
output = func_5146(var_5147,var_5148,)
func_5149 = relay.Function([var_5147,var_5148,], output)
mutated_mod['func_5149'] = func_5149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2869_call = mod.get_global_var('func_2869')
func_2870_call = mutated_mod.get_global_var('func_2870')
call_5190 = relay.TupleGetItem(func_2869_call(), 0)
call_5191 = relay.TupleGetItem(func_2870_call(), 0)
output = relay.Tuple([call_5190,])
output2 = relay.Tuple([call_5191,])
func_5200 = relay.Function([], output)
mod['func_5200'] = func_5200
mod = relay.transform.InferType()(mod)
output = func_5200()
func_5201 = relay.Function([], output)
mutated_mod['func_5201'] = func_5201
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5223 = relay.var("var_5223", dtype = "float32", shape = (11, 1, 5))#candidate|5223|(11, 1, 5)|var|float32
uop_5224 = relay.acosh(var_5223.astype('float32')) # shape=(11, 1, 5)
bop_5226 = relay.divide(uop_5224.astype('float64'), relay.reshape(var_5223.astype('float64'), relay.shape_of(uop_5224))) # shape=(11, 1, 5)
output = bop_5226
output2 = bop_5226
func_5234 = relay.Function([var_5223,], output)
mod['func_5234'] = func_5234
mod = relay.transform.InferType()(mod)
mutated_mod['func_5234'] = func_5234
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5235 = relay.var("var_5235", dtype = "float32", shape = (11, 1, 5))#candidate|5235|(11, 1, 5)|var|float32
func_5234_call = mutated_mod.get_global_var('func_5234')
call_5236 = func_5234_call(var_5235)
output = call_5236
func_5237 = relay.Function([var_5235], output)
mutated_mod['func_5237'] = func_5237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4382_call = mod.get_global_var('func_4382')
func_4383_call = mutated_mod.get_global_var('func_4383')
call_5258 = relay.TupleGetItem(func_4382_call(), 0)
call_5259 = relay.TupleGetItem(func_4383_call(), 0)
func_1967_call = mod.get_global_var('func_1967')
func_1969_call = mutated_mod.get_global_var('func_1969')
const_5266 = relay.const([False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,False], dtype = "bool")#candidate|5266|(560,)|const|bool
call_5265 = relay.TupleGetItem(func_1967_call(relay.reshape(const_5266.astype('bool'), [10, 7, 8])), 3)
call_5267 = relay.TupleGetItem(func_1969_call(relay.reshape(const_5266.astype('bool'), [10, 7, 8])), 3)
output = relay.Tuple([call_5258,call_5265,const_5266,])
output2 = relay.Tuple([call_5259,call_5267,const_5266,])
func_5275 = relay.Function([], output)
mod['func_5275'] = func_5275
mod = relay.transform.InferType()(mod)
output = func_5275()
func_5276 = relay.Function([], output)
mutated_mod['func_5276'] = func_5276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_5312 = relay.TupleGetItem(func_1894_call(), 0)
call_5313 = relay.TupleGetItem(func_1896_call(), 0)
output = call_5312
output2 = call_5313
func_5314 = relay.Function([], output)
mod['func_5314'] = func_5314
mod = relay.transform.InferType()(mod)
output = func_5314()
func_5315 = relay.Function([], output)
mutated_mod['func_5315'] = func_5315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_600_call = mod.get_global_var('func_600')
func_602_call = mutated_mod.get_global_var('func_602')
call_5413 = relay.TupleGetItem(func_600_call(), 0)
call_5414 = relay.TupleGetItem(func_602_call(), 0)
const_5419 = relay.const([[[5.709542,-2.552306,7.715368,-8.341053,7.233704,1.077848,1.566736,9.875014],[3.745001,-6.121315,6.352347,2.153735,-6.599677,-0.737572,-7.950555,4.909217],[8.006739,5.097797,-5.766236,-8.723516,2.149073,7.061022,-9.131497,3.283762],[-0.870749,-6.182592,-1.968833,-8.779831,-3.770501,5.873404,-7.178353,-8.689691],[3.771587,-8.174044,8.098277,0.697504,5.513997,5.442159,5.965479,8.886876],[-5.940050,4.250531,0.843242,-3.086944,-9.315124,-3.657332,-4.248465,2.403298],[-7.642677,1.782012,-2.294896,-6.703458,9.827103,4.632093,-3.721051,6.320231]],[[-4.840673,3.915631,-8.385366,4.513516,4.394779,7.195567,4.176535,4.351744],[-3.123166,1.117762,-9.050118,-7.239966,-7.101764,-0.563143,-3.907373,4.210548],[2.565489,-7.705628,-0.028419,-4.115601,5.446502,0.250529,-4.475784,-6.404155],[0.829853,2.916950,1.948450,-0.036234,7.910335,-7.984209,-4.101860,8.374994],[-7.331938,4.064798,7.327068,6.960920,8.110266,8.359287,9.140503,-7.349693],[-2.567280,-1.360138,-6.707092,5.430063,-6.940291,7.495327,4.334565,-9.619433],[2.252582,4.860741,2.199589,9.672269,9.325327,9.478500,3.862184,-3.583029]],[[2.106703,0.952069,4.857810,-3.785040,0.044708,-3.094547,-4.242803,-9.996029],[-2.085986,-6.543056,-5.934351,-3.720634,3.388240,8.899243,0.700895,-4.310913],[-2.115331,-7.851611,-4.312696,1.005666,6.507875,-6.773886,-6.326930,6.954822],[-1.854070,8.663980,9.884422,7.882321,5.435302,2.300392,-7.823881,7.323123],[-8.900233,-7.250352,-5.451947,-2.456731,4.560347,0.221533,6.166377,-4.132657],[5.306594,6.702079,2.336273,2.322810,1.553189,0.946789,-2.240786,-7.716106],[5.847371,0.516561,2.896231,4.788786,-4.882489,-0.983827,1.388518,-4.573609]],[[-4.965418,5.019473,-6.290674,-1.693961,-5.965149,6.371936,2.810479,1.039522],[-2.120891,-1.641159,-6.103926,-3.733260,0.993419,-4.239223,5.160998,5.737465],[-2.452286,2.355500,8.590484,-7.407658,5.644933,-2.494565,-5.944691,9.729686],[-9.957824,-1.555025,0.193705,7.366544,3.738962,1.808242,-0.243831,1.797389],[-9.893669,1.057899,-1.469346,5.679359,6.473392,-8.231922,1.073129,-4.077122],[-6.116985,-0.251626,5.806682,-0.929279,4.386541,7.958525,-4.013130,7.036440],[4.808242,-8.271994,-3.021170,-2.110668,0.103910,5.185318,-8.871736,-9.133165]],[[-6.288301,5.871798,-2.625471,5.020768,7.563023,-2.965172,1.706101,-1.522908],[-2.061291,-0.323974,-7.740451,3.696860,-5.718859,-5.555548,-2.995171,2.849273],[5.554338,4.511257,-6.485087,-5.160054,0.297803,5.649020,-5.109877,-6.607962],[-9.366237,8.131496,0.742243,-9.630433,-3.302525,-8.112948,1.331015,8.002104],[-4.083516,-5.878118,8.270975,1.433300,4.860867,8.219406,-1.096265,6.128084],[5.046431,-5.558296,4.744353,-6.608640,5.998866,-3.460930,-5.217941,-4.223642],[-7.439533,0.096264,7.617462,3.845735,3.284140,-7.103640,-8.784380,-1.590059]],[[-2.335670,-3.863784,7.322911,7.912404,1.995933,1.090010,-0.431273,1.096577],[-0.132248,-1.319217,4.949593,9.741348,9.843415,-4.335086,3.443494,3.863446],[4.038086,1.720682,-2.571614,-8.573358,-0.229908,5.419757,5.519883,-9.764138],[3.701970,0.736192,-1.696942,8.216686,-1.525997,2.942472,-3.069356,2.276893],[-8.434409,-6.733421,-2.315749,-9.378941,-9.895721,3.452225,-0.665948,0.187729],[-2.049535,-7.786662,7.864255,-9.039993,-8.287940,0.137698,-6.540423,-5.065077],[7.035344,7.870348,0.840396,1.628798,8.419539,4.056053,-3.279155,9.189301]],[[9.695179,2.574207,0.653090,-3.435353,1.928460,-5.384117,7.514476,-1.245320],[8.298134,-7.049323,6.040588,-1.444956,-4.623218,8.957276,3.275615,1.472042],[-4.889141,0.309727,7.183002,6.031204,-2.152893,-3.684224,6.143420,-0.910749],[9.225122,8.510009,-3.035008,7.066741,-2.138645,4.283539,-5.819019,-7.692354],[7.085804,-6.445628,-9.376260,7.707594,-8.200988,-5.861588,-2.080534,-7.122360],[7.420066,1.921097,-0.801682,-0.490972,7.718183,-8.910133,-7.931810,-0.566932],[-6.302225,-7.608438,1.433547,3.593936,-4.558737,1.406769,2.042872,-1.763877]],[[8.373667,-3.674428,-9.338335,-3.050488,5.093145,3.291172,-4.277015,7.527471],[0.375456,3.298098,-5.957511,-9.188678,-4.456916,2.165468,2.189401,-4.010020],[7.068766,-9.466283,1.647329,0.765809,1.558062,-0.609945,4.773323,0.096851],[-0.886938,9.057994,9.140056,7.341296,0.425834,9.387709,-6.843484,3.290867],[9.146271,5.912292,9.204967,9.011950,-5.125239,-5.636360,8.646279,-3.740503],[-5.949695,-6.300948,1.512371,9.788902,3.489522,8.212112,-5.691385,6.005944],[6.375844,-9.894674,-5.521888,3.572280,1.766650,-1.592989,1.461231,-6.126904]],[[-8.063138,-3.656978,-7.769395,-4.508066,-7.771947,6.522664,-6.966543,-9.965484],[-4.088620,-9.788019,-2.732121,8.975734,8.116652,4.274944,-6.593103,-3.566106],[-4.215879,-5.391794,-7.507390,-5.283416,-3.668356,5.129260,6.230944,-6.659969],[-4.214953,-1.800032,2.502250,3.334111,4.936399,2.527181,-0.926311,-9.607041],[-1.118767,-9.194106,8.452853,-4.095409,-5.282029,-1.137420,0.216567,4.311677],[-6.881050,2.426623,1.457913,-9.006326,7.368994,-1.128765,-1.337094,-9.550502],[3.585426,1.750665,-1.658822,1.837087,-9.264552,-9.245959,-8.098418,1.134650]],[[3.078102,-8.548456,4.029297,5.521489,5.592958,7.375648,-0.636805,-1.585921],[-4.592871,-2.656903,6.226991,3.974437,0.554412,-3.654985,-0.380834,-7.791461],[-7.328150,-7.850700,-1.323857,-2.524216,-6.525086,2.831996,0.331763,-5.489450],[8.053261,-5.610287,-0.401253,-3.967984,9.989713,-5.465464,5.747260,9.275173],[7.631859,3.012640,5.371414,2.434640,2.660212,-8.593294,1.257786,-6.076565],[0.399764,7.371791,8.444820,-5.548169,-8.174371,-4.774894,6.126633,1.661407],[0.837167,-8.868395,-9.610974,-8.341003,-5.201994,3.597972,-5.528417,2.649647]]], dtype = "float64")#candidate|5419|(10, 7, 8)|const|float64
bop_5420 = relay.subtract(call_5413.astype('uint32'), const_5419.astype('uint32')) # shape=(10, 7, 8)
bop_5423 = relay.subtract(call_5414.astype('uint32'), const_5419.astype('uint32')) # shape=(10, 7, 8)
func_4870_call = mod.get_global_var('func_4870')
func_4871_call = mutated_mod.get_global_var('func_4871')
call_5428 = relay.TupleGetItem(func_4870_call(), 0)
call_5429 = relay.TupleGetItem(func_4871_call(), 0)
output = relay.Tuple([bop_5420,call_5428,])
output2 = relay.Tuple([bop_5423,call_5429,])
func_5443 = relay.Function([], output)
mod['func_5443'] = func_5443
mod = relay.transform.InferType()(mod)
output = func_5443()
func_5444 = relay.Function([], output)
mutated_mod['func_5444'] = func_5444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2122_call = mod.get_global_var('func_2122')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_5479 = relay.TupleGetItem(func_2122_call(), 2)
call_5480 = relay.TupleGetItem(func_2124_call(), 2)
output = relay.Tuple([call_5479,])
output2 = relay.Tuple([call_5480,])
func_5483 = relay.Function([], output)
mod['func_5483'] = func_5483
mod = relay.transform.InferType()(mod)
output = func_5483()
func_5484 = relay.Function([], output)
mutated_mod['func_5484'] = func_5484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5314_call = mod.get_global_var('func_5314')
func_5315_call = mutated_mod.get_global_var('func_5315')
call_5509 = func_5314_call()
call_5510 = func_5314_call()
uop_5513 = relay.erf(call_5509.astype('float64')) # shape=(16, 7, 8)
uop_5515 = relay.erf(call_5510.astype('float64')) # shape=(16, 7, 8)
output = relay.Tuple([uop_5513,])
output2 = relay.Tuple([uop_5515,])
func_5518 = relay.Function([], output)
mod['func_5518'] = func_5518
mod = relay.transform.InferType()(mod)
output = func_5518()
func_5519 = relay.Function([], output)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3984_call = mod.get_global_var('func_3984')
func_3985_call = mutated_mod.get_global_var('func_3985')
call_5570 = relay.TupleGetItem(func_3984_call(), 0)
call_5571 = relay.TupleGetItem(func_3985_call(), 0)
output = relay.Tuple([call_5570,])
output2 = relay.Tuple([call_5571,])
func_5593 = relay.Function([], output)
mod['func_5593'] = func_5593
mod = relay.transform.InferType()(mod)
mutated_mod['func_5593'] = func_5593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5593_call = mutated_mod.get_global_var('func_5593')
call_5594 = func_5593_call()
output = call_5594
func_5595 = relay.Function([], output)
mutated_mod['func_5595'] = func_5595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_5718 = relay.TupleGetItem(func_1733_call(), 0)
call_5719 = relay.TupleGetItem(func_1735_call(), 0)
output = relay.Tuple([call_5718,])
output2 = relay.Tuple([call_5719,])
func_5722 = relay.Function([], output)
mod['func_5722'] = func_5722
mod = relay.transform.InferType()(mod)
mutated_mod['func_5722'] = func_5722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5722_call = mutated_mod.get_global_var('func_5722')
call_5723 = func_5722_call()
output = call_5723
func_5724 = relay.Function([], output)
mutated_mod['func_5724'] = func_5724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2810_call = mod.get_global_var('func_2810')
func_2811_call = mutated_mod.get_global_var('func_2811')
call_5746 = relay.TupleGetItem(func_2810_call(), 0)
call_5747 = relay.TupleGetItem(func_2811_call(), 0)
output = relay.Tuple([call_5746,])
output2 = relay.Tuple([call_5747,])
func_5759 = relay.Function([], output)
mod['func_5759'] = func_5759
mod = relay.transform.InferType()(mod)
output = func_5759()
func_5760 = relay.Function([], output)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5759_call = mod.get_global_var('func_5759')
func_5760_call = mutated_mod.get_global_var('func_5760')
call_5785 = relay.TupleGetItem(func_5759_call(), 0)
call_5786 = relay.TupleGetItem(func_5760_call(), 0)
output = call_5785
output2 = call_5786
func_5809 = relay.Function([], output)
mod['func_5809'] = func_5809
mod = relay.transform.InferType()(mod)
output = func_5809()
func_5810 = relay.Function([], output)
mutated_mod['func_5810'] = func_5810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5809_call = mod.get_global_var('func_5809')
func_5810_call = mutated_mod.get_global_var('func_5810')
call_5824 = func_5809_call()
call_5825 = func_5809_call()
output = relay.Tuple([call_5824,])
output2 = relay.Tuple([call_5825,])
func_5877 = relay.Function([], output)
mod['func_5877'] = func_5877
mod = relay.transform.InferType()(mod)
output = func_5877()
func_5878 = relay.Function([], output)
mutated_mod['func_5878'] = func_5878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2675_call = mod.get_global_var('func_2675')
func_2676_call = mutated_mod.get_global_var('func_2676')
call_5923 = relay.TupleGetItem(func_2675_call(), 0)
call_5924 = relay.TupleGetItem(func_2676_call(), 0)
func_3006_call = mod.get_global_var('func_3006')
func_3009_call = mutated_mod.get_global_var('func_3009')
const_5928 = relay.const(-9, dtype = "int32")#candidate|5928|()|const|int32
const_5929 = relay.const([2,-7,-3,10,-1,-9,2,8,-10,4,3,1,-4,-10,-5,-1,2,8,10,-1,4,-4,3,-4,8,-5,7,-7,-2,6,-1,-4,6,10,-2,7,-3,6,-4,9,10,5,1,10,10,-1,-2,3,1,-4,-6,-2,-3,-3,1,-8,-7,8,-4,3,4,-4,3,6,1,-8,10,-6,-10,-9,2,-2,2,-8,10,-2,-7,3,-4,-3,-1,-3,-3,-6,-7,-6,2,-9,7,3,-9,2,-3,-4,-7,3,-10,-1,-5,-7,-1,5,-10,10,-2,-3,-9,-8,1,9,-1,-6,-1,3,3,2,5,-7,-2,10,-1,-6,9,1,6,-10,6,-9,2,-7,-3,10,6,1,-6,3,-6,-8,-3,-5,-10,-7,10,5,7,10,9,-8,-9,5,1,-3,-7,2,-1,-8,-1,-9,-2,-6,6,-8,5,-2,-6,2,-4,-4,7,8,2,-8,4,7,-4,4,-8,5,-10,-10,3,-6,6,-8,6,10,6,1,7,-4,1,-9,2,-4,10,-1,-7,-1,-6,7,-7,-10,-5,10,8,-1,4,6,3,-10,-8,-9,9,8,-1,9,-2,-2,9,8,-8,4,10,-9,2,7,2,4,8,-9,9,-8,7,9,-1,-1,8,2,7,-1,5,-10,-4,8,-8,-2,7,1,9,9,-7,-1,-8,-2,-6,-6,1,-8,2,-8,5,1,-1,5,2,-9,6,3,3,-1,-8,-2,6,-5,-9,1,4,-7,6,-4,8,7,-3,8,-8,9,-7,-7,2,-1,5,-7,8,4,8,2,3,-9,-2,4,-7,7,5,-9,4,-10,-6,9,-10,5,5,3,-7,-4,-3,-8,-3,-6,-7,-7,-7,-3,3,6,-9,3,-10,-1,1,5,-6,-4,-10,-9,-7,9,1,-8,5,8,-5,-5,-9,2,-2,6,2,8,2,8,-2,-5,10,-7,-7,9,8,-9,-2,1,-7,-3,6,-10,9,-10,-6,3,-10,1,7,-1,5,6,-10,3,-3,-8,-8,-9,-8,-9,6,10,-4,5,-4,8,8,-7,2,-8,8,4,-4,-4,-4,7,-5,-7,-2,10,-3,-5,4,-1,-4,1,-5,-10,8,1,7,1,9,-2,-2,-6,3,-6,-5,-5,-4,-3,-1,-7,-8,-10,-10,-8,-1,-1,3,8,9,4,10,5,4,-4,10,4,2,3,-5,3,3,8,1,3,7,6,-5,-1,8,3,-7,-7,1,4,-3,1,-3,4,-3,4,2,-9,-2,7,-6,-7,7,5,-4,-3,8,-4,1,2,5,-5,-9,-6,-5,-10,-3,-7,1,-6,10,5,-1,8,-9,7,-10,10,7,8,-9,4,-5,2,-2,4,-8,-2,10,-5,2,-10,6,-2,8,-6,10,8,-10,5,9,-4,8,5,7,4,2,2,6,3,-3,10,9,-1,8,-1,-5,3,-2,-3,10,6,3,-2,-1,-4,3,10,-2,1,8,9,8,9,4,-6,-9,-10,2,1,8,10,9,-5,4,5,9,-5,7,6,-4,-8,9,-5,-10,4,2,-1,-5,-4,-2,1,2,-10,-8,2,1,4,10,10,-6,7,-10,8,5,-4,-10,2,-1,-3,-1,2,7,-3,-5,-6,-9,10,-3,7,-2,-7,-8,-4,-1,7,-4,-5,4,7,-1,2,-9,-9,3,-10,-7,-7,8,-3,10,3,8,6,-6,-5,9,-6,2,-1,-1,9,-10,2,-8,8,-4,4,1,-6,-7,5,-8,2,-8,2,4,7,8,3,-4,-5,-6,-10,3,3,5,-3,10,-3,-8,6,-8,7,4,-1,-5,-7,-7,7,3,7,-9,-10,-8,5,-10,8,-6,2,-9,10,-1,-4,-6,-8,2,-6,8,7,-1,-1,-3,-6,8,-3,-5,10,2,4,-6,4,10,6,-5,5,5,-6,-7,-1,4,-9,-9,-3,-4,6,1,-9,-1,2,-7,-4,3,5,4,-2,-2,-7,3,-9,-7,8,-8,-1,-1,6,10,-4,-2,2,5,-6,6,-7,1,5,-2,10,-1,10,3,-1,8,5,-4,-7,10,7,5,4,-9,-6,3,4,6,-5,-10,2,-10,9,4,5,7,10,6,-8,7,10,1,-6,-8,5,-7,-7,6,3,9,-3,-9,-8,9,2,1,5,-5,-8,2,-10,-4,6,-2,7,-6,-8,3,10,10,-7,-5,3,-3,-3,-6,-2,2,10,6,3,-8,-6,5,-3,9,7,2,4,-1,-2,9,-9,3,-3,7,-10,-7,5,4,8,-10,7,-5,9,7,-4,7,-7,5,9,8,-6,-8,8,1,-7,-2,-2,7,-2,-5,1,2,-10,10,8,1,-4,8,-2,9,-9,6,-6,5,9,6,9,10,6,9,9,-1,10,4,-8,3,-3,-9,4,-9,-1,3,-5,-1,4,-7,1,-5,-7,1,1], dtype = "int32")#candidate|5929|(910,)|const|int32
call_5927 = func_3006_call(relay.reshape(const_5928.astype('int32'), []), relay.reshape(const_5929.astype('int32'), [7, 13, 10]), )
call_5930 = func_3006_call(relay.reshape(const_5928.astype('int32'), []), relay.reshape(const_5929.astype('int32'), [7, 13, 10]), )
func_2053_call = mod.get_global_var('func_2053')
func_2056_call = mutated_mod.get_global_var('func_2056')
const_5936 = relay.const([-7.225615,7.704047,8.926876,1.141013,9.687985,-4.584088,1.088227,5.087260,-8.911543,-0.207513,8.625620,-7.896642,-4.714624,0.647304,3.901010,3.262675,9.786197,9.492308,-2.871921,-5.917659,-2.387947,9.214228,-9.750374,5.170582,-0.669879,-1.736394,-6.671865,-3.570243,2.400227,-2.598287,-9.088831,8.248573,-9.070284,7.703717,0.294688,-5.727857,-2.883612,0.755044,-6.295100,7.748112,-3.673162,-4.348756,-7.699161,6.700403,-0.269717], dtype = "float64")#candidate|5936|(45,)|const|float64
call_5935 = relay.TupleGetItem(func_2053_call(relay.reshape(const_5936.astype('float64'), [1, 45])), 1)
call_5937 = relay.TupleGetItem(func_2056_call(relay.reshape(const_5936.astype('float64'), [1, 45])), 1)
output = relay.Tuple([call_5923,call_5927,const_5928,const_5929,call_5935,const_5936,])
output2 = relay.Tuple([call_5924,call_5930,const_5928,const_5929,call_5937,const_5936,])
func_5939 = relay.Function([], output)
mod['func_5939'] = func_5939
mod = relay.transform.InferType()(mod)
mutated_mod['func_5939'] = func_5939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mutated_mod.get_global_var('func_5939')
call_5940 = func_5939_call()
output = call_5940
func_5941 = relay.Function([], output)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2122_call = mod.get_global_var('func_2122')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_5968 = relay.TupleGetItem(func_2122_call(), 5)
call_5969 = relay.TupleGetItem(func_2124_call(), 5)
const_5979 = relay.const([[[-8.186001,-5.629195,-9.242098,1.861485,4.617837,0.061341,-0.858383,5.273539],[4.569938,8.484991,-2.951302,-5.055375,7.801747,9.685558,2.464734,4.100041],[-2.935881,1.374045,1.879134,1.260989,-6.672038,7.804440,7.374955,-0.190829],[5.118118,-2.845079,3.772199,-0.572115,1.016792,-4.096940,-8.431046,-8.539377],[8.896977,4.047108,-9.682193,6.101698,1.834736,-6.628148,4.946989,2.157674],[-6.338918,7.685437,2.620247,2.967635,4.467652,5.423874,1.554080,-2.375062],[-4.081594,4.813665,-4.692061,0.914730,-3.459417,-1.739066,-5.399514,-1.762481]],[[6.066459,-6.149291,-5.597035,3.835334,1.326275,0.472005,-7.234982,5.985214],[-6.588648,-0.188234,1.539353,-9.721618,8.325182,2.686602,7.229718,-1.182975],[9.458162,2.143598,-5.293496,5.519603,0.277959,4.259452,-0.201162,-8.798877],[2.886063,9.434928,-3.110804,-7.136998,5.364305,9.660880,-6.907932,2.460628],[-1.863160,1.333600,-9.118337,-1.482992,0.149205,4.639251,-8.573192,-6.283514],[-9.462235,-3.276506,-2.804722,-3.621906,3.487265,-0.240599,-0.667564,1.416629],[-5.355591,6.959112,-1.624054,-2.096387,5.483145,2.556662,-2.061009,-5.734597]],[[-6.797764,3.151874,4.278801,-1.326936,-2.313578,-6.472745,-2.709255,0.829421],[-2.324632,2.335193,9.088902,6.344843,-4.876992,-1.325700,-7.011007,7.461908],[-2.240848,0.897232,5.013729,-1.791832,-5.527909,-2.107232,-5.789825,9.456981],[-4.988269,3.056609,7.580199,2.136464,-2.962242,-5.004849,-3.611218,9.755099],[-8.992480,-6.644526,-2.386746,3.327400,-2.642519,3.304551,-9.007942,1.668774],[-8.664763,-6.357259,5.229119,8.811760,7.740135,3.039615,8.900943,-0.254777],[9.945583,3.027202,7.422373,1.817426,-0.194154,7.886438,3.685226,-7.775178]],[[4.135914,4.667425,-2.999573,-7.766900,-6.443326,0.447843,-0.311973,-6.244001],[-3.208761,5.004955,-3.501089,0.116025,-6.425355,3.926009,-7.617815,6.666956],[-1.116466,-6.100331,2.370345,8.296083,-6.933534,6.238280,-9.851906,5.147392],[-1.716763,3.917249,3.889430,9.831856,1.565289,5.252259,-1.146639,1.870002],[-7.832456,9.130978,4.609404,7.401100,1.386333,-4.751715,-9.128532,3.795693],[5.982343,-2.376036,1.675903,-4.033675,-7.840941,-2.886803,-4.282289,-9.838765],[-5.912355,-8.277922,-9.040843,5.891761,-8.063152,5.022473,9.076110,8.691603]],[[2.237292,0.471747,-7.548194,1.329297,-9.202389,7.639833,-2.112316,2.470924],[-6.947334,-6.014298,9.579811,-9.624074,9.144668,1.725363,-2.955852,3.488874],[-6.290459,5.029081,-5.613581,8.426364,-2.474201,0.213253,-2.492406,4.071673],[-4.364266,0.339487,-1.293858,-5.242229,-7.454244,-7.259834,-1.703051,-2.830056],[7.216581,6.830447,9.393137,-6.503789,-8.584157,-7.865105,-7.462282,3.340377],[5.566976,-4.926905,-7.762582,1.123662,-6.549932,-4.064697,-0.528117,9.063674],[-2.025464,2.062143,-2.521364,0.309333,-9.499333,3.647245,-1.808683,4.837688]],[[-3.241711,7.268313,-5.625280,4.969431,-8.755408,-8.647199,-7.434098,-0.603309],[-7.239185,-9.153670,9.705638,7.170033,9.902819,-9.575794,0.102924,1.652573],[-5.139559,2.361390,-8.261264,6.143305,-2.539660,7.945948,-4.325738,3.217699],[3.506939,3.625469,6.141896,-8.777840,3.561656,-5.808987,8.857654,-6.823188],[-4.401477,-2.678794,-1.258790,-3.825618,7.661670,-4.539247,7.422868,2.650263],[4.025091,-8.057150,9.576845,-7.673538,8.378819,-0.465782,-7.125987,-8.925275],[-6.295313,0.661748,0.373460,6.984991,5.555786,-4.617894,6.475928,-3.859754]],[[-3.722849,8.329399,0.623069,-7.338685,7.066216,4.675677,-7.673747,-3.216664],[7.130774,4.697141,5.018613,2.443180,-4.663057,-5.157039,6.364141,6.964487],[0.919562,-9.958352,-2.037084,4.293695,7.329529,9.464193,8.103144,-2.702271],[-3.018518,3.384948,-7.208134,-8.853451,-9.602080,-7.866519,5.124471,8.669439],[-6.959686,-2.603151,-3.287640,-7.668309,-1.029513,1.517473,-7.830665,-2.782772],[-3.459188,-6.175528,3.353333,0.678387,5.791353,6.240494,1.447487,7.805874],[-0.777064,-2.453010,-6.673367,-1.230025,6.800622,-9.954613,2.628027,-9.240114]],[[-0.719151,-2.811369,4.389255,5.726337,1.022846,-3.698641,1.145283,9.933700],[0.888988,-4.596746,-1.479651,-6.164154,9.099452,3.746599,-5.492937,-2.881212],[1.476570,-0.545710,-6.396384,4.995385,-8.810110,8.278100,-1.602114,-1.018534],[-9.064664,9.208360,6.462433,-1.708295,-8.938486,-0.532480,0.997501,3.591831],[0.943536,-7.270020,1.627364,-9.391801,6.250916,6.687775,-9.161976,9.597329],[-8.496212,4.875816,-8.446508,-6.066075,-6.264605,5.905586,6.241850,-7.932394],[-6.573379,9.639833,-4.793316,-8.688132,3.571057,3.678837,8.217396,-3.522675]],[[0.021960,3.199537,-3.794399,-8.373204,-4.948427,-6.207592,-8.271138,0.909519],[7.955836,-6.838164,-8.700704,6.396171,-8.859859,7.871770,2.769462,-2.927514],[1.551487,9.822225,5.636870,-8.912366,8.946883,-7.209946,2.652647,0.333673],[-5.220212,5.985286,-2.759212,-5.050811,6.785102,-9.998471,6.217896,-9.027950],[-9.564402,-9.187009,2.658348,-1.545056,-2.683715,7.105072,-4.034431,-8.302459],[-4.581548,6.337037,7.794055,-2.393435,6.659669,1.565588,5.774323,8.831206],[9.986301,8.641116,6.508496,-3.321968,-0.484579,5.008041,-2.302921,3.470583]],[[9.355354,4.452720,-6.612752,-9.219604,-2.834572,6.215071,8.972120,2.057128],[-3.069569,2.441894,-0.862156,0.858184,3.332509,7.431956,8.559908,0.063401],[7.149188,7.711804,-9.838184,8.472850,7.656479,-6.975748,-8.062739,-5.685787],[-5.955508,-5.118249,3.410590,-1.049614,-6.918584,-4.154527,-4.880617,4.274821],[-0.170787,-5.274296,-4.051642,3.503712,-9.099098,-6.552321,5.860629,6.646020],[-2.705521,9.029853,-4.908385,0.803589,8.161582,-6.641324,7.401493,-7.209700],[-9.528621,-0.384716,-3.707476,-0.031651,9.232829,8.770063,2.308163,-9.048497]],[[-2.866449,6.658971,7.244630,-7.362922,-6.570683,2.201684,-7.750142,5.210024],[-0.143115,1.873198,3.336538,9.524832,-6.490009,-8.110405,5.544728,1.413649],[-3.495950,-2.958986,9.770074,-1.966413,5.315544,2.515272,1.219779,-4.475679],[-9.307861,1.959584,-3.421681,-3.882801,5.204080,-6.634110,-4.699818,9.014417],[2.392606,-0.481008,-2.194076,-1.015644,-7.624433,2.117775,7.051186,2.272754],[3.511445,6.256128,1.641941,-6.630066,-4.853653,-9.072301,-7.141363,9.631763],[6.222942,3.459401,9.163013,-2.593783,1.514507,7.074666,3.195225,6.834339]],[[5.624233,-6.851785,-7.794078,-8.945381,-4.874423,3.206385,-3.748920,-8.366384],[9.677868,5.738326,7.333402,-1.409927,6.657696,3.889125,2.103928,6.717339],[-7.836047,6.555961,-9.071380,5.666319,-2.714535,4.353881,-3.389596,4.970742],[6.839838,-8.576428,-5.846956,-7.708408,-6.992152,-4.490178,-8.631106,8.366495],[-9.832605,8.090313,-3.772370,0.971589,-8.509620,5.618937,-6.156243,-7.052400],[2.764409,-0.111314,6.101186,6.000800,8.582493,7.012651,2.198912,-3.245149],[-9.526762,-9.920557,-4.447249,6.896662,-8.091700,8.333379,5.400642,8.476961]],[[-4.192407,-6.676135,-1.723284,-7.629051,-1.897487,1.801838,-2.747179,5.609391],[5.408529,2.645491,8.715517,-9.532774,9.839973,-1.950170,5.730428,1.808665],[1.632712,-9.154451,3.393514,5.063604,-0.769810,8.939747,-5.524645,2.378676],[-7.124982,-1.793184,-6.635212,6.471916,-3.896057,-8.563950,7.898596,-4.277282],[-9.663521,-9.326045,1.163461,3.172298,-4.936949,-5.940685,2.934629,5.908799],[-1.980022,7.473269,-2.050524,-6.703605,-4.545629,2.429597,-0.538026,-8.592019],[-3.337171,-8.379955,0.684315,0.787206,-9.604736,-7.829577,-0.760936,1.764387]],[[4.650100,6.568335,3.778524,6.581874,-3.749416,-1.759898,-1.682961,7.814851],[6.931602,-5.293122,8.270712,8.382708,4.972028,6.768528,5.188054,-0.168526],[1.519789,-8.679765,0.835378,-1.068503,-2.548110,-3.484338,-8.833878,6.975426],[2.684114,-3.737384,-4.078870,-3.144350,1.865451,8.083758,-6.193735,-7.735976],[1.754654,-2.299269,-9.837010,-8.481663,0.395288,3.436251,4.081717,-6.737580],[-6.902980,9.479930,-1.410223,-4.534245,-3.945446,-6.112913,2.270872,-9.487119],[1.996976,4.493691,-8.797663,2.317248,-5.364134,8.316159,6.361057,-5.324914]]], dtype = "float64")#candidate|5979|(14, 7, 8)|const|float64
bop_5980 = relay.add(call_5968.astype('float64'), const_5979.astype('float64')) # shape=(14, 7, 8)
bop_5983 = relay.add(call_5969.astype('float64'), const_5979.astype('float64')) # shape=(14, 7, 8)
output = bop_5980
output2 = bop_5983
func_5984 = relay.Function([], output)
mod['func_5984'] = func_5984
mod = relay.transform.InferType()(mod)
output = func_5984()
func_5985 = relay.Function([], output)
mutated_mod['func_5985'] = func_5985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_6033 = func_2584_call()
call_6034 = func_2584_call()
func_4066_call = mod.get_global_var('func_4066')
func_4069_call = mutated_mod.get_global_var('func_4069')
const_6046 = relay.const([7,7,7,6,-1,5,-6,-1,-2,2,2,8,4,5,8,-1,-7,-4,-8,4,-5,-7,-1,-1,-3,5,-7,-7,5,-10,5,10,2,6,-4,-1,-9,-10,-9,7,6,-9,5,5,-5,4,8,4,10,2,-2,3,-1,6,-5,-2,-5,3,5,1,-5,-2,1,-5,-7,4,-9,-3,-9,-10,1,3,-1,7,6,-9,-3,4,-8,4,3,7,3,2,-6,-6,4,-3,8,4,8,-5,-4,-4,7,8,-5,3,4,4,10,6,-1,-1,-1,-5,8,-9,-10,-5,-2,-8,-9,-9,-8,2,2,4,-1,4,-9,10,-10,10,-3,-6,1,5,7,-2,4,-7,-5,10,5,7,-5,-3,-7,5,-1,6,7,1,-5,10,-8,6,7,9,-1,8,-5,-9,8,-4,-4,-1,4,-6,-5,-8,3,-6,9,-4,4,-4,-5,-3,8,-1,8,5,4,-10,-8,-1,10,3,7,-2,1,1,-1,-10,2,3,-5,-1,-10,7,-9,10,8,-1,-5,5,10,-4,10,2,-7,-1,3,-1,-5,2,-7,-3,10,-7,8,-10,9,1,-10,-3,-10,-1,-8,-8,9,7,4,8,-6,10,-10,-2,6,10,8,5,8,3,-8,-9,10,-2,5,-10,-8,5,-3,-7,-4,-7,8,2,-9,4,-3,6,-10,-2,10,-6,-4,-6,-1,6,-10,8,6,-6,5,4,-4,5,-9,-8,9,-7,8,8,6,5,-8,4,4,-8,-9,-9,3,8,9,10,2,10,9,-1,3,-1,-2,-4,-2,-7,7,7,-10,-3,-10,10,8,-4,-10,-4,-3,-6,7,-3,-4,-3,6,2,-2,8,6,6,8,5,-4,-2,3,4,-8,2,-7,3,-4,1,10,9,-5,-9,2,-10,-2,-5,-8,6,6,-8,-2,8,7,-3,-9,2,5,9,-7,8,-9,6,-4,5,-10,-4,-7,-10,2,-9,6,-6,-5,2,2,-1,3,-2,8,8,2,2,-4,4,-8,8,-6,-4,-7,-1,6,-4,7,-5,-5,7,-5,-7,-3,-7,-5,2,-7,-2,-5,-7,-5,10,-7,1,10,-9,6,5,8,10,-7,5,-1,2,10,-6,10,-10,-1,-9,6,-7,8,4,6,-1,6,-8,-3,-2,-10,1,-4,-7,10,7,7,-10,8,3,8,6,10,-1,-6,9,9,4,-8,8,8,-6,9,-2,-2,10,8,3,4,2,-5,4,10,-7,10,6,3,4,8,1,-8,-9,9,-4,-6,-10,7,6,3,-6,3,2,-4,7,2,-1,9,9,-1,-2,1,-9,8,-8,3,6,7,-1,6,-2,-6,-3,2,6,6,4,9,-8,1,10,3,9,5,1,-7,-2,-6,1,-4,3,4,9,-1,2,6,-7,7,-9,5,4,10,9,8,4,-9,-5,-4,-8,-3,8,-2,8,-10,-2,4,-1,3,-10,9,6,-3,-1,-5,-2,9,8,5,-1,-3,-2,-2,-3,2,-5,-9,1,1,-9,-2,3,-10,-3,8,-2,8,10,-8,4,-8,4,-9,9,8,-6,-6,-4,-1,3,-2,10,2,1,-3,-1,3,6,2,-3,3,3,-8,8,-5,-1,-8,8,-1,10,-3,2,-8,-9,6,-1,1,10,4,-1,9,-7,-2,-6,3,6,-7,-3,9,-3,3,-5,1,-6,-3,1,8,8,-4,-3,-8,-4,-9,10,-6,4,9,4,5,3,6,10,4,5,10,-5,-9,3,-4,6,6,-9,-1,4,-2,6,5,-5,-1,8,-10,-10,-2,9,-6,7,-6,8,1,3,-1,5,-4,6,1,-7,-7,-10,-7,-6,-3,-4,1,-6,4,-10,-10,-2,5,10,-1,7,-1,6,5,1,-7,8,-7,-4,6,9,-1,10,10,-2,-4,-9,-7,3,7,3,-10,-1,5,-9,9,5,-8,6,3,-9,10,-2,-10,-10,-8,2,3,-5,1,7,2,2,7,8,-7,-6,4,5,-2,5,-7,10,-10,-8,10,3,-7,4,4,-3,10,9,9,9,8,-5,-9,-6,-9,2,-8,-3,-1,-9,8,5,3,-1,-7,-8,-4,-1,-8,-4,9,-8,2,-4,-8,-9,6,6,7,4,10,10,-6,7,-5,-5,-6,1,-6,-4,-7,3,-4,-5,-8,8,2,4,-6,-4,-1,-5,-1,8,1,-2,-2,4,-3,10,7,-3,-3,-6,9,9,-8,10,3,5,-9,-6,1,10,8,-9,-5,3,1,-8,1,2,-6,-7,2,2,-10,-4,-8,-8,4,1,-2,-9,6,-5,9,-4,-2,1,-4,7,3,6,-6,10,-2,9,-5,-8,8,-10,5,-9,7,-2,6,7,-1,-1,-9,-4,1,-6,-2,1,-2,-6,-5,3,-6,4,-6,-1,6,-3,4,8,1,-4,-10,4,4,-8,-4,10,8,1,-7,-1,6,-7,-1,6,1,-8,4,5,-1,-8,6,6,4,-9,2,3,6,-10,5,1,-5,8,-9,9,8,7,-5,-1,2,9,2,6,2,-4,-2,-4,2,-8,7,-2,-5,10,-4,1,10,4,10,9,5,-10,6,4,5,10,-1,8,3,-8,-8,-7,-8,2,10,-1,-5,-4,2,3,-1,-1,7,-6,7,1,2,-6,6,10,1,3,-10,-1,4,-2,-8,7,4,8,-9,9,-5,-2,6,1,1,5,2,6,1,2,2,-5,-3,10,-1,3,-7,-9,7,2,5,-1,-5,-2,6,-4,-1,7,-1,6,-7,8,-4,-6,-8,-10,6,-9,-10,-7,-4,5,1,1,-8,-4,8,6,10,4,10,2,-7,9,1,-4,-9,2,2,2,2,4,7,-3,-3,6,1,3,8,-7,-6,-5,3,-4,3,-4,1,5,1,-6,5,10,-1,-5,-5,-9,-5,-7,-4,-3,7,3,7,-8,6,-5,-6,-8,-9,6,-5,-4,-1,-9,2,-3,-1,-6,6,9,8,2,8,-10,3,1,-3,10,-6,3,1,8,4,-2,-10,10,-4,1,-4,-1,9,7,-6,9,6,-1,-8,10,-5,-10,-3,10,-7,-9,3,10,-9,5,-5,-9,-6,9,1,6,2,-10,10,-2,10,8,9,-7,-6,-4,-9,-4,-5,-1,-4,2,-4,-3,-2,-1,-4,8,-10,2,9,9,-10,3,5,2,10,7,6,-8,3,-3,-10,-10,7,-6,-7,4,-5,-1,-10,2,-8,-4,7,5,3,6,-10,-4,8,3,5,1,6,-4,6,6,3,8,-2,-9,-10,8,3,9,2,-5,1,8,-7,-4,8,-6,-10,10,-7,6,-6,-1,6,10,-4,-6,-2,-2,9,-1,8,6,4,-1,-7,-10,1,3,1,-7,10,-10,8,-1,-2,1,-2,9,7,8,-8,8,-2,-9,6,-8,9,-9,1,-3,-4,4,-3,3,2,-3,-10,2,-4,4,8,8,-1,-4,1,-5,2,-3,2,-5,7,-7,-1,-8,-1,-8,-6,6,-5,10,-8,1,4,-4,-1,-3,9,7,2,-6,10,3,10,3,-10,1,10,7,-9,-2,-10,-9,8,8,3,-2,5,1,5,-1,7,-2,-8,-2,-9,-7,1,5,-4,-7,6,10,-5,9,6,-4,3,-1,6,-8,-6,-4,-3,-6,2,3,-3,1,5,7,-9,-4,10,5,-7,-2,10,-1,5,-9,1,6,7,3,5,-3,2,7,3,1,-7,-6,-7,9,4,-10,1,10,-3,-8,-2,3,8,-7,3,2,1,6,-5,-1,-4,8,8,3,-9,-10,-2,7,4,-3,-4,-7,-5,2,-10,2,5,-1,-6,-4,5,-7,6,9,8,7,10,-6,6,6,-2,-2,-8,1,7,-8,9,1,9,-7,5,2,5,10,-5,-9,-5,-5,-8,-7,-2,-9,-2,8,2,2,-9,-3,-2,8,-1,8,2,1,10,4,2,-4,-6,10,8,-9,6,-3,-7,8,10,6,-9,-9,-2,2,-8,2,9,-6,-6,3,-7,2,7,-1,-8,-8,-3,-8,2,3,-4,-6,9,-9,-6,-6,-9,6,2,5,-6,9,-10,6,-6,-1,-6,-3,-2,-9,-5,1,7,3,5,-9,9,-2,-4,-8,-9,-1,10,1,8,-10,7,10,7,3,-9,4,-10,-6,5,7,5,-1,3,6,-2,-4,-8,-4,6,-8,10,5,-8,-6,-5,9,10,6,3,-3,-10,5,1,-2,9,-4,-10,8,-9,3,7,1,-3,9,9,-3,8,7,-9,8,7,-6,-2,6,-1,3,-2,-3,3,3,3,1,5,-3,-6,-4,-7,-9,7,10,4,-5,-10,-3,10,5,1,-7,5,-5,-2,-4,-1,8,10,-7,-3,-1,1,-6,-10,-4,-8,-1,10,-5,-7,3,-4,8,-9,8,-7,5,-5,-9,-3,-7,-4,5,6,-8,1,-3,-2,-10,-7,-5,9,2,-2,-8,2,7,6,1,3,5,3,-2,-8,-10,-9,9,4,2,10,10,-9,-9,-8,-7,2,-9,-9,-1,-1,3,-5,-10,2,4,5,-4,-2,9,3,-3,7,1,-10,6,5,-3,-10,1,6,5,-1,4,-2,-5,9,4,-9,6,9,-3,1,-7,9,-2,5,-6,6,4,-5,7,-7,3,-3,-7,1,1,8,-3,-7,-1,2,-3,-9,10,-5,9,-5,-8,-1,3,7,-2,-3,1,9,4,-1,-4,3,-8,9,10,10,-4,-5,3,-2,-6,-1,5,-10,3,-8,-6,1,9,9,-3,7,2,-6,-5,-9,3,7,9,-9,-1,-9,9,-8,9,-8,-10,2,7,6,-6,3,4,9,1,8,-6,8,-9,2,8,2,4,-10,4,5,9,-9,-1,-8,8,-2,-3,8,9,-1,1,-4,9,-8,-8,-3,4,-1,2,-5,7,3,-10,-1,-2,-5,-6,-7,-3,-8,-9,-9,6,-6,-1,-9,10,8,4,10,-4,8,-6,-6,10,-1,6,-2,1,-1,10,-3,-3,-10,-2,2,5,-7,2,9,9,1,-1,-8,-2,7,8,-2,-2,-7,-3,2,10,9,5,6,-10,-9,-9,-3,5,-2,-1,5,7,10,2,7,3,4,6,10,-6,-8,6,-7,-3,-4,-5,10,1,-1,-1,-5,-6,10,8,9,9,-2,-1,5,-9,-10,8,-6,7,-1,8,1,-4,8,-3,9,-4,-8,-9,-9,-2,3,-7,8,-10,4,-7,-4,8,-5,8,-4,3,7,4,10,-5,7,-4,7,6,-4,6,5,7,-6,4,-7,-3,10,-10,-5,-5,-6,9,-5,-7,-7,-4,-9,-2,5,-7,4,-7,-9,-5,2,7,1,3,3,2,3,4,-8,-8,-2,-7,5,1,9,-8,-7,8,3,1,-1,5,2,5,6,3,8,-6,-4,-9,-4,5,-4,-9,-6,2,-5,1,-6,7,10,2,2,3,7,-8,-8,4,7,10,4,-1,1,-6,10,1,-5,-10,-2,-10,4,4,2,6,1,-5,10,-8,9,9,9,-9,-2,-9,1,-5,-9,9,-7,3,2,5,-3,4,6,1,-3,10,-9,-10,-10,7,4,-3,10,-10,-1,6,-7,5,-4,-1,-7,2,9,8,9,-9,1,5,-7,6,8,-3,4,2,-4,-5,-3,-7,-1,2,-10,2,-4,-3,-9,-8,-2,-6,8,-6,-1,3,8,-6,7,-8,10,8,-6,-4,1,4,4,-2,7,7,9,-10,2,-5,-4,5,2,8,6,2,4,5,-7,-10,-6,-2,7,-3,10,9,2,9,-9,3,9,-5,3,-2,-6,5,-1,9,1,-8,-2,6,-1,10,-4,-5,8,7,-9,-2,-1,-9,5,10,-9,-8,5,7,-1,-6,-1,7,3,3,-4,9,1,10,5,4,10,7,6,-1,-4,-1,8,-4,-3,-2,-1,4,8,-10,4,9,3,-9,-1,-5,9,-9,5,7,10,7,-2,-5,-3,-5,8,10,1,2,10,-6,5,-6,-9,-10,-6,-2,6,-1,2,-5,-10,-4,4,3,-5,-5,-6,-1,-5,6,8,2,-3,2,-10,8,3,3,9,-1,6,-7,8,5,-10,7,-9,1,-3,-9,-1,-3,10,2,-1,-6,-1,-7,-2,2,-5,8,-9,6,-4,-5,6,7,-3,7,-2,-10,7,-1,10,-1,-4,9,-9,-5,3,-8,-9,5,4,5,5,10,-3,-3,6,-9,4,-6,-6,6,3,6,-10,4,-3,1,-4,-1,4,1,-7,-2,10,-6,9,4,7,-5,-1,9,8,1,3,-9,6,-8,-10,-4,8,-5,-1,10,10,-4,-4,4,-5,2,-5,-6,10,-3,-4,-3,8,-1,8,8,-9,-9,-5,3,-6,-9,-7,-3,9,-9,5,-5,-9,-4,10,-5,2,9,4,9,-8,-2,-1,4,-3,3,7,2,4,5,6,2,5,-7,-5,1,-3,10,2,-6,-1,2,4,-7,10,4,-3,5,-10,-9,9,10,-6,7,-6,-2,9,8,10,6,7,-7,6,2,-6,-3,-2,-6,3,6,-6,10,-2,1,-4,-3,6,-5,4,2,-8,-5,-8,-9,-4,-2,-5,8,-3,-9,-7,-7,-4,9,10,6,-4,8,-1,3,-6,-8,1,8,6,-8,10,7,-10,2,6,9,8,-4,-6,6,5,-3,-1,-8,-8,9,-6,4,3,-7,3,-2,3,9,4,3,1,-8,7,-9,-4,5,-5,5,4,-10,6,-9,8,2,5,-3,-3,7,7,-7,4,-1,2,10,6,4,-10,4,-10,1,-2,-2,-5,5,6,-3,5,-3,7,-4,1,-6,-10,10,5,-5,-4,-1,5,1,9,4,-5,2,8,5,-5,-2,-1,5,4,4,7,8,-1,-5,-10,-4,-4,7,4,3,4,2,-8,1,7,9,-1,7,-6,2,-9,-1,3,-5,1,-6,-3,-10,5,2,-9,7,-8,1,5,9,10,-7,1,1,9,-9,-6,-1,2,-5,4,10,6,-5,-3,-5,6,5,3,9,1,-4,7,-8,-1,-10,4,-7,9,1,8,-2,-7,2,-3,2,1,1,-3,6,3,-9,4,-9,-9,5,-6,2,6,-3,-6,-4,-1,4,-5,8,-6,9,2,-5,8,-8,10,8,-5,6,-6,-10,-5,-2,7,-2,-6,7,9,-9,-3,-3,-7,9,-10,5,5,-2,2,-3,-4,3,8,-6,-1,5,-1,9,7,-4,-2,4,6,10,-2,8,9,-5,-1,-3,-7,-8,-7,10,4,-3,-5,-6,3,-1,-10,-10,-10,8,-8,-6,1,3,9,-2,-7,1,-1,3,4,10,2,-5,-7,-8,5,-7,-7,4,6,-1,10,5,9,-5,3,-9,7,1,-10,-6,2,1,6,5,1,6,-10,-3,10,-3,5,-10,-9,-4,-10,4,-6,1,-2,3,-4,7,10,4,7,-5,-1,-5,-7,-9,-1,-9,2,8,-8,-7,2,8,-3,-5,2,-3,4,3,-8,8,-9,-6,-7,-3,7,-9,6,-2,10,1,7,4,1,5,-2,-9,-10,-2,-9,-1,-8,5,8,5,5,9,-10,-5,2,10,-1,-7,-2,-9,3,-9,-2,7,4,-9,7,-2,1,-8,7,7,7,-10,-2,-1,-9,-7,7,-3,5,-9,-10,-9,-10,3,7,5,3,-4,-4,-9,-7,6,-10,4,-10,10,-6,10,8,-3,-3,-8,6,1,-8,5,-9,-1,1,-6,8,1,-5,-10,-4,7,-1,-4,-8,7,7,3,-4,-5,-10,5,7,10,7,-4,-2,8,7,-2,-9,2,10,2,-10,6,9,7,-7,7,-8,-7,-3,8,7,4,-7,-3,-2,9,-3,-5,8,8,1,-1,8,1,-3,3,7,7,6,2,-5,3,8,10,-9,1,-6,9,10,-7,-9,2,-10,3,-9,7,6,3,7,9,-2,4,-7,-1,-4,-10,1,-10,-3,8,-8,7,6,-7,3,-6,10,-2,6,-4,4,-3,7,5,-8,3,9,-9,10,-5,-6,8,5,-1,-5,-1,-10,-1,10,9,10,-4,-4,1,3,-6,1,2,-4,-8,1,-8,-4,10,-5,-1,-2,4,-2,-9,5,1,-9,-1,-10,-2,8,2,8,-5,-10,10,5,-8,-10,-1,4,8,-7,-6,10,9,-9,10,-2,2,3,-4,3,3,-2,-8,-6,-10,7,-1,-6,-5,-1,2,-9,-5,-4,9,2,-3,-6,-1,-7,-7,-4,1,9,5,-10,1,-9,2,-5,3,2,-4,-4,3,3,-6,-8,-7,3,-5,8,2,4,3,4,-9,-9,-7,5,4,9,6,-7,4,-6,-2,-7,-4,-10,-10,-10,-1,3,1,7,7,7,3,8,-1,8,-9,-10,8,9,-4,-9,9,2,-10,-9,-7,10,-8,9,3,5,-2,6,-4,-8,-7,3,8,7,-8,-7,-1,-5,5,10,-1,9,-9,5,-1,4,-1,3,-4,-9,7,7,3,6,-8,-4,-1,-4,10,-6,2,9,8,-5,4,-5,10,-8,-6,8,3,2,-7,-4,6,9,1,3,2,2,-2,7,-2,6,9,1,8,-6,2,3,4,-5,-10,4,6,7,6,-1,-9,6,3,-2,3,-7,9,-4,-1,-8,9,2,10,5,-3,2,-5,2,8,-6,-1,7,-2,3,-1,-4,-2,6,-6,-6,7,-3,-8,8,-8,-6,-9,10,-7,-5,-1,9,-5,-3,-5,-4,-9,-5,-3,-1,-1,-1,-4,-4,-4,-9,9,-8,10,7,-4,-8,-7,8,-7,-2,-9,-1,-4,4,-3,2,-1,-8,6,8,8,3,-10,7,1,8,-2,3,-3,3,3,9,8,7,-5,-3,5,-8,6,-4,5,-7,2,-1,10,-2,1,-7,9,4,2,-6,-3,2,2,-8,-10,1,6,9,-10,-7,4,-10,9,-8,-1,-6,9,-8,5,-7,1,-9,2,3,10,-2,3,7,6,-10,10,-5,-5,-1,9,5,7,-6,-3,10,-8,-8,-4,4,-2,9,2,2,-7,8,-2,5,-9,8,-2,3,-3,-3,-6,9,1,10,3,3,-9,-3,5,10,-1,-6,-9,4,-2,10,-4,-7,-8,2,-3,1,-7,-2,-2,-8,3,7,5,-5,-8,6,-6,9,-2,-7,-8,-6,3,-7,2,-8,-9,8,-6,-2,10,6,-3,-3,-8,9,-9,8,10,-6,3,9,1,-10,10,1,2,-7,-4,9,1,7,2,9,-3,6,1,9,-1,-6,1,-3,5,-7,10,-1,5,-8,-3,8,-2,-3,-10,-4,1,3,7,6,-6,1,10,-7,-9,-1,4,2,4,10,10,-4,-3,-5,-3,-2,-4,6,-6,9,10,2,9,-1,-9,-4,2,-10,-5,5,3,-8,4,-1,9,-8,9,-4,-3,-1,3,-1,-5,1,-5,-7,-6,7,3,10,1,-2,1,-1,10,-7,7,-9,1,2,6,6,6,-2,5,-10,4,-7,7,-9,9,-9,6,-1,-8,2,-2,-6,6,-9,1,-7,3,-8,-3,-7,-3,-1,8,5,-4,-2,9,-7,5,6,-7,-1,-7,1,5,2,-8,-8,-4,-2,4,-5,1,8,9,-4,-6,-7,3,5,-7,10,2,10,3,-4,-6,-9,-2,3,-8,-8,-9,9,10,-3,-5,-2,1,2,-6,10,-9,8,-6,3,-5,10,3,-9,-5,1,5,6,-7,-1,-9,4,-2,9,3,-1,2,-4,3,9,-6,-8,6,-9,4,-8,3,-1,6,2,-2,8,6,-9,3,-7,-10,10,-10,-9,-8,-9,8,-5,-10,4,2,7,1,-7,6,5,-10,2,-3,6,7,-2,5,-1,-6,8,4,6,-3,-4,-8,7,-4,-9,9,8,-1,10,10,3,-6,-6,8,10,6,4,-2,1,7,3,-5,1,3,-2,-3,-1,-7,1,-10,1,-4,-9,6,-10,-1,-1,6,-2,3,2,-10,9,1,-5,1,-6,-10,1,6,-9,6,3,9,-1,-1,2,-9,9,9,8,9,-6,10,5,1,-4,1,1,3,6,-6,-5,7,4,7,9,7,-7,5,2,3,2,-3,7,4,2,-2,-6,1,7,1,6,-1,4,2,-1,2,-2,-6,-3,-2,4,-1,3,8,2,5,-5,10,2,5,-8,7,-4,-10,-5,3,6,-8,8,10,5,-9,-4,10,-2,9,4,1,-9,6,-3,5,-4,2,-1,3,10,8,2,7,-3,-3,2,-6,5,9,4,1,9,2,-6,7,9,-9,3,5,4,-4,2,-9,5,-6,2,-7,-1,-2,-7,4,-4,9,10,-5,1,-1,3,-1,6,7,7,8,6,8,8,-1,4,4,-1,-6,-10,7,-7,-2,-8,-8,7,-6,5,-6,5,-9,-7,-2,-2,3,7,7,-10,6,2,-6,1,1,5,3,7,10,-7,-2,-5,2,5,-8,10,5,-8,-10,5,7,3,2,3,1,6,-8,-10,-5,-2,2,-4,6,9,5,1,4,3,1,-7,4,10,6,-4,5,-1,10,5,1,3,-8,7,6,9,4,4,1,1,1,8,1,-4,-7,6,3,-4,-4,4,-1,-1,-8,6,-8,9,-4,7,6,-8,-10,-3,-6,5,-9,1,-1,6,7,1,9,-7,6,-10,-7,5,3,-2,4,10,-6,3,3,-1,1,8,-3,-5,-8,9,-1,3,-2,-4,2,-10,-7,8,-4,2,10,-7,2,-1,-7,8,-7,-6,5,9,-6,-8,4,2,-6,3,-4,-10,-4,-9,-3,3,-5,1,10,9,-9,-8,-6,2,5,-1,-8,5,4,-7,8,-7,10,7,9,4,7,-2,-2,-7,10,8,-9,-1,7,-9,9,-10,-5,-7,-4,-4,-4,-2,-1,-7,-6,-10,-8,-9,-1,1,-4,7,7,6,6,10,4,-8,2,-7,-8,5,-8,-2,5,-8,-4,10,10,3,-4,8,9,-5,1,1,-7,-7,3,3,-3,-6,-6,8,-10,4,8,-4,-7,-9,-8,-10,-7,9,8,-9,-3,-8,9,6,1,-5,-9,-7,5,7,-6,-10,3,4,-3,2,8,-6,-8,-8,10,9,2,8,-9,5,-1,10,-6,7,7,-7,1,-2,6,9,5,7,-1,-9,1,8,8,-10,-2,4,-10,6,4,2,10,-6,-9,-4,-10,-5,-8,-7,-2,-9,-5,6,3,7,-10,7,-2,6,-8,4,-5,10,-3,-10,-3,-9,-1,4,-7,-3,-9,8,3,-1,-4,8,-5,5,-7,-10,3,1,-4,-9,-3,7,-3,3,9,-5,-10,-4,-5,-2,-3,5,2,1,-8,-7,5,4,9,1,3,2,-3,8,-9,-8,-3,-10,8,8,-4,-10,-9,6,-2,-9,-5,8,-1,-3,7,3,-6,-2,4,2,-7,6,7,-7,9,3,6,9,8,-8,-5,4,1,8,7,5,2,-9,3,9,-1,3,4,5,-6,-8,3,2,5,1,-2,6,-8,-5,1,3,6,1,10,3,-8,-6,-10,-7,10,9,-4,6,-1,5,4,-4,-3,-10,3,-10,-4,-4,-7,-3,10,-1,-8,8,-7,-1,-10,9,2,-10,-5,-7,-7,5,-1,2,-2,-6,9,2,-9,-5,2,4,-7,10,-3,1,6,-5,-6,-8,10,-1,-8,-5,5,-5,5,-2,4,-4,-7,-6,-3,-9,7,-7,1,-6,-10,5,-2,-4,-10,1,8,-10,10,-7,-8,-2,-4,-4,9,-4,-2,8,-9,-10,9,-10,7,-2,-7,-10,5,-10,2,-4,5,-4,6,8,4,-2,-9,10,4,3,-8,6,6,2,1,3,-3,4,6,-3,-2,-3,-9,7,4,-5,-4,6,9,9,4,-8,6,-4,-4,3,4,-8,-9,-6,-6,5,-4,-9,-1,-6,8,-1,8,9,4,9,-9,1,-2,1,10,8,-7,8,5,2,-8,2,-10,-9,4,-10,-4,3,8,6,1,1,-10,5,-2,1,-2,7,3,-4,-3,1,7,-3,-7,-2,-4,-6,1,10,-2,5,-1,6,10,10,-6,1,5,8,-5,-10,-1,-3,-10,8,-3,4,9,7,-9,3,10,-9,-9,4,-7,-5,1,-5,-1,10,7,-8,-5,-6,-4,4,-4,-6,9,-9,6], dtype = "uint8")#candidate|6046|(4536,)|const|uint8
call_6045 = relay.TupleGetItem(func_4066_call(relay.reshape(const_6046.astype('uint8'), [324, 14]), relay.reshape(const_6046.astype('uint8'), [324, 14]), ), 1)
call_6047 = relay.TupleGetItem(func_4069_call(relay.reshape(const_6046.astype('uint8'), [324, 14]), relay.reshape(const_6046.astype('uint8'), [324, 14]), ), 1)
func_1497_call = mod.get_global_var('func_1497')
func_1499_call = mutated_mod.get_global_var('func_1499')
var_6052 = relay.var("var_6052", dtype = "float64", shape = (896,))#candidate|6052|(896,)|var|float64
call_6051 = relay.TupleGetItem(func_1497_call(relay.reshape(var_6052.astype('float64'), [16, 7, 8])), 5)
call_6053 = relay.TupleGetItem(func_1499_call(relay.reshape(var_6052.astype('float64'), [16, 7, 8])), 5)
var_6056 = relay.var("var_6056", dtype = "uint32", shape = (13, 10, 2))#candidate|6056|(13, 10, 2)|var|uint32
bop_6057 = relay.less(call_6051.astype('bool'), relay.reshape(var_6056.astype('bool'), relay.shape_of(call_6051))) # shape=(13, 10, 2)
bop_6060 = relay.less(call_6053.astype('bool'), relay.reshape(var_6056.astype('bool'), relay.shape_of(call_6053))) # shape=(13, 10, 2)
func_5939_call = mod.get_global_var('func_5939')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_6071 = relay.TupleGetItem(func_5939_call(), 5)
call_6072 = relay.TupleGetItem(func_5941_call(), 5)
bop_6075 = relay.not_equal(const_6046.astype('bool'), relay.reshape(call_6045.astype('bool'), relay.shape_of(const_6046))) # shape=(4536,)
bop_6078 = relay.not_equal(const_6046.astype('bool'), relay.reshape(call_6047.astype('bool'), relay.shape_of(const_6046))) # shape=(4536,)
func_1260_call = mod.get_global_var('func_1260')
func_1262_call = mutated_mod.get_global_var('func_1262')
call_6079 = relay.TupleGetItem(func_1260_call(), 0)
call_6080 = relay.TupleGetItem(func_1262_call(), 0)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_6081 = func_526_call()
call_6082 = func_526_call()
output = relay.Tuple([call_6033,var_6052,bop_6057,call_6071,bop_6075,call_6079,call_6081,])
output2 = relay.Tuple([call_6034,var_6052,bop_6060,call_6072,bop_6078,call_6080,call_6082,])
func_6090 = relay.Function([var_6052,var_6056,], output)
mod['func_6090'] = func_6090
mod = relay.transform.InferType()(mod)
var_6091 = relay.var("var_6091", dtype = "float64", shape = (896,))#candidate|6091|(896,)|var|float64
var_6092 = relay.var("var_6092", dtype = "uint32", shape = (13, 10, 2))#candidate|6092|(13, 10, 2)|var|uint32
output = func_6090(var_6091,var_6092,)
func_6093 = relay.Function([var_6091,var_6092,], output)
mutated_mod['func_6093'] = func_6093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2675_call = mod.get_global_var('func_2675')
func_2676_call = mutated_mod.get_global_var('func_2676')
call_6100 = relay.TupleGetItem(func_2675_call(), 0)
call_6101 = relay.TupleGetItem(func_2676_call(), 0)
output = call_6100
output2 = call_6101
func_6102 = relay.Function([], output)
mod['func_6102'] = func_6102
mod = relay.transform.InferType()(mod)
output = func_6102()
func_6103 = relay.Function([], output)
mutated_mod['func_6103'] = func_6103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4134_call = mod.get_global_var('func_4134')
func_4135_call = mutated_mod.get_global_var('func_4135')
call_6123 = func_4134_call()
call_6124 = func_4134_call()
output = relay.Tuple([call_6123,])
output2 = relay.Tuple([call_6124,])
func_6163 = relay.Function([], output)
mod['func_6163'] = func_6163
mod = relay.transform.InferType()(mod)
mutated_mod['func_6163'] = func_6163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6163_call = mutated_mod.get_global_var('func_6163')
call_6164 = func_6163_call()
output = call_6164
func_6165 = relay.Function([], output)
mutated_mod['func_6165'] = func_6165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_6166 = func_526_call()
call_6167 = func_526_call()
output = call_6166
output2 = call_6167
func_6171 = relay.Function([], output)
mod['func_6171'] = func_6171
mod = relay.transform.InferType()(mod)
output = func_6171()
func_6172 = relay.Function([], output)
mutated_mod['func_6172'] = func_6172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2869_call = mod.get_global_var('func_2869')
func_2870_call = mutated_mod.get_global_var('func_2870')
call_6183 = relay.TupleGetItem(func_2869_call(), 0)
call_6184 = relay.TupleGetItem(func_2870_call(), 0)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_6185 = func_2899_call()
call_6186 = func_2899_call()
uop_6215 = relay.erf(call_6183.astype('float32')) # shape=(1, 7, 8)
uop_6217 = relay.erf(call_6184.astype('float32')) # shape=(1, 7, 8)
bop_6221 = relay.bitwise_or(call_6183.astype('int64'), relay.reshape(uop_6215.astype('int64'), relay.shape_of(call_6183))) # shape=(1, 7, 8)
bop_6224 = relay.bitwise_or(call_6184.astype('int64'), relay.reshape(uop_6217.astype('int64'), relay.shape_of(call_6184))) # shape=(1, 7, 8)
func_3079_call = mod.get_global_var('func_3079')
func_3080_call = mutated_mod.get_global_var('func_3080')
call_6225 = relay.TupleGetItem(func_3079_call(), 0)
call_6226 = relay.TupleGetItem(func_3080_call(), 0)
output = relay.Tuple([call_6185,bop_6221,call_6225,])
output2 = relay.Tuple([call_6186,bop_6224,call_6226,])
func_6249 = relay.Function([], output)
mod['func_6249'] = func_6249
mod = relay.transform.InferType()(mod)
output = func_6249()
func_6250 = relay.Function([], output)
mutated_mod['func_6250'] = func_6250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4659_call = mod.get_global_var('func_4659')
func_4660_call = mutated_mod.get_global_var('func_4660')
call_6281 = relay.TupleGetItem(func_4659_call(), 0)
call_6282 = relay.TupleGetItem(func_4660_call(), 0)
func_2122_call = mod.get_global_var('func_2122')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_6288 = relay.TupleGetItem(func_2122_call(), 3)
call_6289 = relay.TupleGetItem(func_2124_call(), 3)
func_3329_call = mod.get_global_var('func_3329')
func_3332_call = mutated_mod.get_global_var('func_3332')
const_6307 = relay.const([1.622791,-9.190247,4.131289,-1.934908,4.822725,-8.453016,5.077631,3.939378,0.680540,6.590115,9.607003,-3.163546,-0.814852,7.708997,-6.555810,-3.071224,1.618387,-1.291749,-1.858060,-5.966552,-0.661928,-3.307856,3.307491,-8.887061,1.492790,0.792369,-3.265240,8.679470,0.383846,-3.887700,-6.066522,0.648599,-5.439967,-9.328685,-4.009641,-4.984820,6.227475,-9.167513,9.119456,7.420462,-0.870197,9.456363,-4.790861,4.947852,0.568682,-8.206913,1.582151,3.906026,9.120464,-8.351850,-0.901351,-1.542026,1.559980,-2.651531,4.641667,-5.377265,7.490858,-0.176993,-1.917273,1.456188,-3.780374,2.913305,8.151329,2.220251,-3.689935,-2.098753,-1.968608,1.845789,5.121536,-3.595501,8.267645,0.117907,-1.581185,6.401449,5.837615,-8.255520,-3.199466,0.082690,-2.460108,-6.115041,-9.826257,4.228281,3.549762,9.034733,8.858249,6.542292,-3.275165,9.173755,-2.400420,6.153565,4.487470,2.342961,-0.577075,5.749947,2.491179,4.619895,-0.264403,7.300629,0.678951,-4.039328,-8.422133,-3.100242,-0.427756,-9.468873,-9.765060,5.030109,5.672958,7.472868,3.546200,0.584075,-4.938455,1.798818,6.187982,-7.608566,3.100218,4.188080,-9.350576,-4.517148,0.816254,2.246853,-1.591784,9.650350,-1.445935,0.542529,3.648196,-9.506826,-8.140868,-0.174143,-5.483139,-9.965651,-1.833432,-9.494591,9.255923,7.689977,8.477899,-7.364390,9.784290,6.060916,-2.903486,-0.476583,9.729354,3.951638,-0.129523,-2.196830,-0.270366,-9.215145,-5.918540,2.013611,7.917926,7.157847], dtype = "float64")#candidate|6307|(150,)|const|float64
call_6306 = relay.TupleGetItem(func_3329_call(relay.reshape(const_6307.astype('float64'), [5, 15, 2])), 0)
call_6308 = relay.TupleGetItem(func_3332_call(relay.reshape(const_6307.astype('float64'), [5, 15, 2])), 0)
func_1683_call = mod.get_global_var('func_1683')
func_1685_call = mutated_mod.get_global_var('func_1685')
const_6314 = relay.const([[1.391690,-7.236872,-2.577294,-1.849185],[-8.194904,7.479239,-4.184100,-3.978939],[-3.104465,-6.554343,5.897859,-2.713870],[2.504054,8.360026,-3.685352,5.370077],[-3.771849,-1.626364,3.165307,0.516269],[-3.568188,7.680257,9.471525,-7.159434],[-0.564100,3.763659,-2.782981,-4.357065],[8.326070,-8.620854,-8.151650,-7.693587],[5.959107,9.247602,0.639785,-8.762324],[3.655347,6.922625,7.506200,-3.809029],[-2.268802,4.844841,-6.214734,-4.154396],[-3.293383,0.337188,-8.131453,5.594762],[-8.059846,-3.893864,9.487618,3.035493],[-2.009337,1.715146,-9.110751,-4.195632],[-7.293571,-1.760100,0.441117,-2.228926],[8.622867,-7.633299,5.436569,8.597423],[8.295012,-8.002440,2.546276,0.191002],[-0.205165,7.373179,4.183252,8.155121],[-1.565007,-4.362071,-1.054009,0.749860],[-7.955230,5.766398,0.861296,3.745431],[-9.396781,-1.378592,3.850779,6.622753],[-5.061484,3.867915,-6.908386,6.160148],[-6.025425,3.900662,6.773555,-2.171679],[-0.916077,7.856566,-1.069158,-5.896620],[-7.288734,-4.929375,6.567381,0.859932],[6.335067,7.139659,1.385841,-1.086344],[-9.292099,-9.337353,-2.941819,4.863350],[-3.276635,-2.879269,5.113104,2.576136],[7.994540,0.460946,-4.941952,3.996001],[3.846142,0.624252,0.194342,-4.002367],[6.558419,7.443634,5.015899,9.285867],[-1.945003,7.328580,-1.414329,7.169791],[-5.313077,-6.902767,-9.063461,-2.238105],[-2.445770,-2.728508,6.508076,8.177508],[-8.396890,-1.482490,9.907984,7.528331],[-1.999099,8.249301,-9.652251,-9.814809],[-9.642341,3.877031,-1.830759,-6.473895],[5.419927,1.130724,-0.951575,-4.244642],[0.768106,-6.546844,-5.327443,-2.361619],[-0.933533,1.612283,9.384257,-1.546333],[3.227298,-8.762209,2.499632,-0.513583],[9.932678,-5.094344,0.376202,-4.108315],[1.256292,0.755894,1.420575,-1.903639],[-1.369338,-3.944736,-5.340827,5.790115],[-1.597363,3.168741,-7.185701,-7.990061],[6.840129,7.648743,8.697012,-0.541666],[1.395377,-4.130338,6.855629,-1.179229],[2.366241,8.694194,5.964396,4.371163],[-1.832772,-2.697739,-0.470422,4.988106],[1.609378,-4.606723,-0.125983,0.163540],[3.023838,-8.967315,6.552446,-7.680183],[8.006447,-6.430543,-2.159349,-1.278249],[-9.979469,8.200119,-3.682147,8.780474],[-6.910842,-6.003454,-7.770082,-6.549279],[-8.837479,-9.948976,8.666490,-6.618964],[8.822128,-6.315829,-2.389164,-3.630455],[6.187041,2.024933,-2.049182,9.858886],[3.856320,-5.417653,2.103197,5.681574],[4.628542,2.412453,-5.319827,-7.664057],[-3.772932,7.327655,3.011882,-7.757737],[0.060813,-5.914363,-9.022964,-7.056711],[-7.509196,4.802655,4.488284,7.246737],[-1.194790,-5.023102,-1.978690,-6.602979],[4.101200,5.454160,-8.740659,0.300500],[3.446450,3.703791,9.503144,2.387108]], dtype = "float32")#candidate|6314|(65, 4)|const|float32
call_6313 = relay.TupleGetItem(func_1683_call(relay.reshape(const_6314.astype('float32'), [260,])), 0)
call_6315 = relay.TupleGetItem(func_1685_call(relay.reshape(const_6314.astype('float32'), [260,])), 0)
uop_6316 = relay.log2(const_6314.astype('float64')) # shape=(65, 4)
output = relay.Tuple([call_6281,call_6288,call_6306,const_6307,call_6313,uop_6316,])
output2 = relay.Tuple([call_6282,call_6289,call_6308,const_6307,call_6315,uop_6316,])
func_6318 = relay.Function([], output)
mod['func_6318'] = func_6318
mod = relay.transform.InferType()(mod)
output = func_6318()
func_6319 = relay.Function([], output)
mutated_mod['func_6319'] = func_6319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3681_call = mod.get_global_var('func_3681')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_6350 = relay.TupleGetItem(func_3681_call(), 0)
call_6351 = relay.TupleGetItem(func_3682_call(), 0)
output = relay.Tuple([call_6350,])
output2 = relay.Tuple([call_6351,])
func_6357 = relay.Function([], output)
mod['func_6357'] = func_6357
mod = relay.transform.InferType()(mod)
output = func_6357()
func_6358 = relay.Function([], output)
mutated_mod['func_6358'] = func_6358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5877_call = mod.get_global_var('func_5877')
func_5878_call = mutated_mod.get_global_var('func_5878')
call_6369 = relay.TupleGetItem(func_5877_call(), 0)
call_6370 = relay.TupleGetItem(func_5878_call(), 0)
func_4778_call = mod.get_global_var('func_4778')
func_4780_call = mutated_mod.get_global_var('func_4780')
call_6380 = relay.TupleGetItem(func_4778_call(), 0)
call_6381 = relay.TupleGetItem(func_4780_call(), 0)
func_2810_call = mod.get_global_var('func_2810')
func_2811_call = mutated_mod.get_global_var('func_2811')
call_6398 = relay.TupleGetItem(func_2810_call(), 0)
call_6399 = relay.TupleGetItem(func_2811_call(), 0)
func_4942_call = mod.get_global_var('func_4942')
func_4945_call = mutated_mod.get_global_var('func_4945')
const_6424 = relay.const([[8.059428,-3.417585,7.576976,-2.224545,9.465315,-2.158821,-5.302880,8.244044,4.392142,-6.187124,4.544488,3.923114,6.475377,-5.678439,-8.450854,7.268950,0.023260,5.490211,6.061491,-7.356030,8.941534,3.233585,5.545571,8.051425,4.648674,-1.714156,3.832045,4.979156,-4.875645,-5.100893,-1.676246,4.205347,5.937084,-0.628520,-5.109840,-5.512246,2.921063,-6.787342,-4.755783,3.843444,8.594727,5.421504,-3.665885,9.315402,-1.570221,2.269442,-8.571091,-0.652134,3.985676,-0.785701,-1.676633,-0.861265,-6.897840,-6.932589,-9.313272,0.601871,0.561686,-3.312390,2.770442,-7.867898,-5.586309,-1.762239,-1.299342,-5.690461,8.916725,-4.951700,4.131977,-1.660457,6.209062,9.253918,-9.918191,5.345342,6.133149,7.956011,3.655153,-3.486947,9.199616,-2.561142,-6.926506,-6.953811,2.883145,2.995247,5.620050,4.062636,-5.715696,-8.499258,7.882906,-5.639313,-2.698920,0.454264,2.612969,6.109998,-1.295967,0.066291,-7.226156,-6.484095,-4.961877,5.278972,8.896500],[-4.192147,2.420840,6.884079,-3.298098,5.812610,5.162022,-9.143161,-7.949554,-9.995408,-3.840629,1.526190,5.170808,-3.323952,4.779262,7.514237,-9.675339,-1.366761,-8.298098,-6.305275,8.979499,0.480034,-1.619487,-6.521063,0.554839,4.080669,-2.557128,9.556042,0.592082,7.427158,7.764808,9.637977,-3.011966,6.355939,7.471535,4.339508,5.525240,-9.150510,-3.264694,-5.580983,8.969249,1.807759,4.329389,5.721068,3.119187,0.087371,8.589540,-5.155970,7.024545,-7.665793,-1.409451,4.186262,5.928136,7.789322,-0.147008,2.666435,-7.603310,0.972068,5.290750,-4.339014,0.043161,9.541541,-9.670375,-8.097811,7.663986,2.944315,-6.196592,8.520457,-5.999414,-8.406897,2.566898,-2.335568,-7.189484,1.421951,-9.682450,-5.269630,3.039841,-9.204141,-4.954289,8.023875,4.512157,6.675124,-4.727736,4.452158,5.525858,7.825241,-0.845405,-2.547426,-5.886244,-7.581745,8.210826,-1.691012,7.207747,2.469314,-2.125156,1.666597,6.523038,0.180876,-2.533494,-4.478573],[-6.453125,-2.235168,7.667501,-1.661566,-6.640692,-2.294076,3.955157,-2.343138,4.901732,-3.606738,1.513016,3.288238,-1.949908,-1.992440,-5.612065,1.396050,-2.841143,8.801506,-0.381198,2.768719,-1.733442,1.499299,1.340406,-6.943918,6.107586,-2.809518,7.145120,9.479671,-6.354835,-0.771474,-6.174005,-2.403011,0.609535,-9.855212,5.431456,-8.813810,4.425349,9.343380,9.131346,2.018549,6.209321,3.207808,7.064980,-3.780602,-9.534545,-6.394695,-5.068833,-0.832354,-8.731850,-2.757911,-7.469651,-8.092400,-9.090354,-3.631201,4.866835,-8.093653,4.291661,4.285064,-1.859260,6.271803,-1.803376,2.213176,-6.894692,-0.569597,-5.833873,-3.370580,6.138262,-1.059475,-4.611191,-4.784030,-7.678309,-1.636467,-6.118027,-2.850017,-1.456517,-2.957012,-2.785934,9.086404,5.359942,1.286486,-2.050959,-1.606885,-7.677597,0.313073,-9.964363,8.597772,-0.040130,-5.988042,3.012697,2.193324,-0.424371,3.322904,6.893897,1.752436,-3.943051,-5.728460,-9.195665,6.687545,3.663495],[-4.961368,-6.924486,-8.610456,6.267017,1.721065,-9.267118,-1.505181,-1.102567,9.172846,8.149638,-9.044904,7.053445,-8.403412,-5.200602,8.698128,2.157337,5.707522,5.233225,-6.498095,-0.337782,8.736176,9.156256,-6.897737,9.284514,0.201500,-9.577082,5.155388,4.347696,-0.710981,9.622465,3.967426,8.367078,-8.869120,2.237160,8.344053,-6.959968,-9.213543,1.178336,-2.599537,-1.436908,7.566712,6.609013,-9.407275,-4.796337,-0.132248,-8.163550,-6.152364,-2.759530,-4.011613,-4.439453,-8.090222,2.426026,-2.406887,3.427639,7.744342,-2.109185,-0.418456,1.409388,-5.474855,2.847091,1.621425,1.939506,4.016612,-8.703821,9.397058,-7.991307,-8.751864,-5.444803,-6.434703,1.240819,7.972842,-4.910355,1.164846,-0.533014,5.854551,9.310371,-8.098993,0.765894,-9.384382,9.385569,-3.811295,5.999076,3.832007,7.591781,7.427072,-9.137095,-4.167931,7.551864,-9.593811,-1.749047,7.226474,4.265911,-3.259602,-0.962387,-1.606862,-8.342717,7.762543,9.065331,7.961713],[-1.773416,8.506514,9.781667,0.858807,-3.343887,-7.761920,5.904907,-5.007953,8.484928,5.897080,1.027172,-5.567895,-9.255668,-3.794988,-7.179111,-6.435271,-0.082662,5.567606,-6.408579,-5.498133,9.656574,5.560918,8.292234,6.986050,-6.171890,-2.564796,-2.909192,3.476562,-8.046732,4.023028,1.143914,0.009224,3.089620,5.762888,0.586530,-4.438531,-8.445473,5.156808,5.847334,9.995581,-1.740139,-6.166208,-5.021716,5.019018,8.196506,7.829795,8.163170,-4.139829,-7.544282,-8.251388,-5.962195,-5.493255,-2.402211,-1.933907,-2.187729,5.241044,6.557160,6.484791,3.074540,-1.461439,9.731514,6.987831,-0.854338,-2.068654,2.281032,-0.154516,3.761190,-2.126956,-6.689511,-4.982191,-5.166323,9.409120,1.111399,9.710312,-3.312811,1.290762,-8.974604,-3.320188,-3.783132,9.707620,8.165803,9.041211,-4.698270,-0.851153,-5.351867,8.785415,-1.661258,-1.233093,8.542258,-3.512245,2.788012,-7.479720,-2.680454,-0.607795,7.452174,-5.695518,5.451410,5.312810,1.939076],[4.417235,-5.120742,4.129674,9.826060,-0.470167,0.295673,-8.382507,-8.427823,-5.573626,9.331717,-1.195591,-8.404958,2.500780,-6.439365,4.828644,-4.728112,-8.070352,7.123545,1.263675,2.810479,-0.782353,-8.907522,-9.757923,0.499301,8.850547,6.603528,5.505896,-6.834404,-9.641766,2.194664,0.145946,-3.432213,6.547432,2.485544,-5.095003,-7.483927,1.348405,-8.434323,-7.091732,3.930627,-8.979936,3.093572,-5.903943,8.521622,-1.213338,4.665362,-5.267838,5.249156,6.593677,9.093981,-5.602589,-8.280590,-4.035405,3.028861,-0.226453,3.578016,3.028708,-7.460481,-7.023819,-6.044115,6.717315,-0.602523,6.070453,1.602796,-7.482553,1.106392,-0.259134,9.949056,-9.963513,6.064932,4.239161,8.231617,8.059925,-0.467299,8.476881,8.434488,-4.434495,0.880858,8.087901,7.267353,1.402365,-3.161830,-8.958040,-9.661377,-3.462248,-8.834265,-1.625210,6.057839,0.599069,-6.113218,-7.156553,1.211527,4.425836,8.515659,3.552081,4.325147,8.531260,5.090029,1.375420],[-3.232945,2.525603,1.951510,-2.540901,-3.957542,-8.450307,0.566749,-3.922917,-3.785629,1.282962,-3.132246,-1.822691,7.702191,-2.355029,1.728921,-1.575799,0.041290,-3.637999,-4.477514,0.254454,5.670501,4.286430,9.624688,7.508604,3.676835,6.805794,-2.365188,0.141221,4.457151,-1.202928,4.762768,-1.000055,-8.692255,9.290029,8.607175,7.182092,2.012957,9.929434,-9.079847,-0.530680,6.071074,-5.353877,0.598651,4.545148,8.998699,4.513484,1.225491,9.091663,4.245849,-8.632707,-3.831321,7.125203,-8.173443,-1.701398,7.309091,-3.373961,-5.354734,-5.438648,1.476626,-1.592221,2.649406,4.464069,1.862892,3.066289,-3.324100,1.485635,6.186059,-7.593057,-1.922336,7.676299,4.167010,-5.929264,-8.053280,0.992986,4.349623,-4.355534,5.785304,8.364378,-6.822297,9.651078,-4.475788,9.179819,3.769624,3.829203,-8.667989,-1.650832,-7.934070,5.017574,6.599048,-4.421479,-7.328651,-1.632966,0.269529,-8.579700,-9.500552,-7.434425,1.584368,-9.068675,7.092979],[-5.502057,-4.547262,6.368659,0.302552,0.824081,5.110232,3.451187,-2.167335,9.401755,7.457074,-5.860722,-6.245563,-7.431103,-0.926492,-4.217836,-7.428412,-5.712188,4.763149,-4.180755,-9.313951,-6.342346,2.761444,-3.196053,4.538093,3.566171,7.886309,-2.477381,-3.609254,3.171366,5.829170,-6.001851,-7.718807,7.926352,-5.656684,2.168755,5.910570,-0.778192,9.446114,8.669743,0.902138,-0.457451,-6.374461,-8.529572,5.056932,3.354651,5.020933,4.361654,-8.259647,-1.360029,-2.614399,-4.164328,3.919729,-0.116506,8.395790,7.545677,5.205266,1.495652,-9.303592,-2.782710,-1.467093,-2.972524,-4.202205,3.788097,-4.044059,7.409047,2.156874,7.630136,0.662434,-7.557594,6.948862,7.901489,5.671100,-8.885030,-5.209975,5.911076,-4.868911,-0.743723,1.364044,-0.191602,6.588941,-7.012679,1.099797,7.926906,-1.161913,5.373514,9.016954,-9.863931,6.058918,-9.381443,5.534348,-2.135799,-0.986380,-0.946625,7.742790,6.179097,0.387875,9.026446,1.607970,5.856863],[-0.625346,4.559199,3.842694,-2.656644,-9.568281,-4.865958,7.036133,-5.531995,8.170999,4.110101,9.458929,-5.949649,8.146808,6.193409,-2.794685,-1.387167,8.820126,4.913068,0.204135,2.037150,-9.230909,7.832228,7.564808,9.957454,4.512223,7.956676,-8.144846,7.777757,1.014670,-2.461688,8.781302,0.471626,1.626767,8.095159,-8.059971,-4.002678,-0.144169,-1.096578,6.200152,-0.843420,3.206184,1.866891,4.708721,2.158508,5.264664,2.150417,-4.430966,9.544320,3.235126,-1.579681,-2.339296,-8.810777,-1.286595,-0.071515,3.058184,-0.574037,-1.924077,-0.270604,-4.365073,-6.684828,1.394148,-9.957603,-3.943452,7.641891,-2.809731,-2.080175,1.315868,5.820430,3.205026,1.362230,0.115901,3.117242,-5.445651,1.287105,3.423939,-8.689721,0.136297,-9.239271,9.045772,5.926695,0.328493,-7.208011,2.864378,9.430640,8.102529,4.552485,-8.378328,-6.024612,-8.942284,-4.299307,3.883557,-7.746657,5.635560,9.411853,5.896557,6.951387,-9.396507,5.714431,0.774618],[-4.833518,2.417135,7.131953,8.253513,-3.665700,-1.058207,2.849428,-7.032990,-1.452669,4.365634,-1.891952,1.692927,6.848395,0.952719,5.253831,0.127756,3.881361,0.384769,3.968923,-1.606972,-5.305857,-7.644632,-8.435846,7.477906,-2.035127,-3.885554,0.267712,-2.304237,6.787707,2.888795,3.383450,5.840960,-9.777634,8.477975,2.892866,6.124025,-0.457543,6.359575,-8.223905,-4.542082,1.591358,5.649442,-6.548976,-5.915380,6.586972,-4.390709,-2.073402,3.930048,-4.666497,-3.711021,-5.845074,0.018422,9.921684,-5.842778,3.344838,7.481393,3.473202,-0.936931,-7.547880,-1.200337,-5.723023,-3.522898,-0.006982,3.561891,0.212796,-1.555624,-1.020056,-5.677263,-5.485232,9.183823,4.367120,0.216582,-9.465891,-1.555504,-9.524222,-3.060959,0.983359,1.918287,9.710876,-3.272410,2.956295,-4.731063,-3.652260,7.049551,1.835336,3.484402,4.671024,-9.629495,-8.905334,2.680785,7.036568,2.025061,-3.814952,-1.205806,-9.633247,-5.799820,0.264649,9.547782,-6.956927],[-0.877132,9.005153,-2.394207,-0.226738,-4.063992,-1.519611,9.742947,-8.855254,-3.973093,-7.600096,-7.423812,-8.085112,-5.971883,9.318700,6.134473,-7.063029,-6.906304,2.942719,6.067314,8.407992,-9.283146,4.280466,7.856640,3.182673,-6.540427,-2.968742,-9.648015,-7.485554,-3.995156,-6.892382,7.060193,1.089880,-0.673982,-9.074234,5.241284,-7.141523,7.427590,8.335410,0.353293,9.895068,-0.430085,-8.685262,-1.579884,5.851731,-3.398559,-1.640131,6.338405,9.685435,4.757162,7.602496,5.650089,-3.078789,8.128667,9.660683,-7.025300,-0.439668,-5.162773,6.703770,7.537407,4.146138,-4.397447,3.669153,-0.545508,-8.082031,2.628497,-3.132932,1.728841,9.062069,-2.244232,1.475987,5.608115,-5.477464,-2.188717,-6.058403,-9.467129,2.807594,-3.683695,-0.562363,-4.289253,-1.735525,-7.058014,-5.544639,5.475655,-8.758163,2.702058,8.417933,-2.551912,-2.648663,6.193464,-5.925136,7.253251,8.170139,4.221883,-4.541134,-9.367389,8.296671,2.338507,-8.974913,6.332627]], dtype = "float32")#candidate|6424|(11, 99)|const|float32
call_6423 = relay.TupleGetItem(func_4942_call(relay.reshape(const_6424.astype('float32'), [9, 11, 11])), 0)
call_6425 = relay.TupleGetItem(func_4945_call(relay.reshape(const_6424.astype('float32'), [9, 11, 11])), 0)
func_5483_call = mod.get_global_var('func_5483')
func_5484_call = mutated_mod.get_global_var('func_5484')
call_6437 = relay.TupleGetItem(func_5483_call(), 0)
call_6438 = relay.TupleGetItem(func_5484_call(), 0)
func_2291_call = mod.get_global_var('func_2291')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_6450 = relay.TupleGetItem(func_2291_call(), 1)
call_6451 = relay.TupleGetItem(func_2293_call(), 1)
func_3536_call = mod.get_global_var('func_3536')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_6469 = relay.TupleGetItem(func_3536_call(), 0)
call_6470 = relay.TupleGetItem(func_3537_call(), 0)
uop_6471 = relay.erf(call_6437.astype('float64')) # shape=(364,)
uop_6473 = relay.erf(call_6438.astype('float64')) # shape=(364,)
func_495_call = mod.get_global_var('func_495')
func_496_call = mutated_mod.get_global_var('func_496')
call_6474 = func_495_call()
call_6475 = func_495_call()
bop_6476 = relay.left_shift(call_6380.astype('int32'), relay.reshape(call_6474.astype('int32'), relay.shape_of(call_6380))) # shape=(1, 7, 8)
bop_6479 = relay.left_shift(call_6381.astype('int32'), relay.reshape(call_6475.astype('int32'), relay.shape_of(call_6381))) # shape=(1, 7, 8)
output = relay.Tuple([call_6369,call_6398,call_6423,const_6424,call_6450,call_6469,uop_6471,bop_6476,])
output2 = relay.Tuple([call_6370,call_6399,call_6425,const_6424,call_6451,call_6470,uop_6473,bop_6479,])
func_6483 = relay.Function([], output)
mod['func_6483'] = func_6483
mod = relay.transform.InferType()(mod)
output = func_6483()
func_6484 = relay.Function([], output)
mutated_mod['func_6484'] = func_6484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_925_call = mod.get_global_var('func_925')
func_926_call = mutated_mod.get_global_var('func_926')
call_6610 = func_925_call()
call_6611 = func_925_call()
output = call_6610
output2 = call_6611
func_6623 = relay.Function([], output)
mod['func_6623'] = func_6623
mod = relay.transform.InferType()(mod)
output = func_6623()
func_6624 = relay.Function([], output)
mutated_mod['func_6624'] = func_6624
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6625 = relay.var("var_6625", dtype = "float64", shape = (11, 9, 16))#candidate|6625|(11, 9, 16)|var|float64
uop_6626 = relay.atanh(var_6625.astype('float64')) # shape=(11, 9, 16)
uop_6639 = relay.exp(var_6625.astype('float32')) # shape=(11, 9, 16)
bop_6641 = relay.bitwise_and(uop_6626.astype('uint32'), relay.reshape(uop_6639.astype('uint32'), relay.shape_of(uop_6626))) # shape=(11, 9, 16)
func_2490_call = mod.get_global_var('func_2490')
func_2494_call = mutated_mod.get_global_var('func_2494')
var_6646 = relay.var("var_6646", dtype = "float64", shape = (896,))#candidate|6646|(896,)|var|float64
const_6647 = relay.const([4.677385,5.231725,6.150686,7.417329,6.651818,5.758876,6.868699,2.150316,-5.685453,-6.064926,8.312965,-1.988203,9.809932,-0.803906,-7.596769,-6.507098,-3.765488,-8.432989,0.981309,-9.514887,4.222224,-1.322687,-2.292148,-2.865998,-2.562127,-0.814441,2.832780,0.917082,9.170351,1.724947,4.635020,2.987845,8.927111,5.769151,9.131183,9.656457,-1.687201,-8.312103,6.891005,4.973522,5.287460,-8.839373,-1.142815,-0.641851,0.142007,0.543364,0.469230,-8.438906,5.608173,-8.274706,-5.832489,5.626089,8.985234,9.534045,-6.180338,1.051879], dtype = "float64")#candidate|6647|(56,)|const|float64
call_6645 = relay.TupleGetItem(func_2490_call(relay.reshape(var_6646.astype('float64'), [16, 7, 8]), relay.reshape(const_6647.astype('float64'), [56,]), ), 1)
call_6648 = relay.TupleGetItem(func_2494_call(relay.reshape(var_6646.astype('float64'), [16, 7, 8]), relay.reshape(const_6647.astype('float64'), [56,]), ), 1)
output = relay.Tuple([bop_6641,call_6645,var_6646,const_6647,])
output2 = relay.Tuple([bop_6641,call_6648,var_6646,const_6647,])
func_6653 = relay.Function([var_6625,var_6646,], output)
mod['func_6653'] = func_6653
mod = relay.transform.InferType()(mod)
mutated_mod['func_6653'] = func_6653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6653_call = mutated_mod.get_global_var('func_6653')
var_6655 = relay.var("var_6655", dtype = "float64", shape = (11, 9, 16))#candidate|6655|(11, 9, 16)|var|float64
var_6656 = relay.var("var_6656", dtype = "float64", shape = (896,))#candidate|6656|(896,)|var|float64
call_6654 = func_6653_call(var_6655,var_6656,)
output = call_6654
func_6657 = relay.Function([var_6655,var_6656,], output)
mutated_mod['func_6657'] = func_6657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2291_call = mod.get_global_var('func_2291')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_6674 = relay.TupleGetItem(func_2291_call(), 0)
call_6675 = relay.TupleGetItem(func_2293_call(), 0)
output = call_6674
output2 = call_6675
func_6681 = relay.Function([], output)
mod['func_6681'] = func_6681
mod = relay.transform.InferType()(mod)
output = func_6681()
func_6682 = relay.Function([], output)
mutated_mod['func_6682'] = func_6682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5314_call = mod.get_global_var('func_5314')
func_5315_call = mutated_mod.get_global_var('func_5315')
call_6699 = func_5314_call()
call_6700 = func_5314_call()
var_6704 = relay.var("var_6704", dtype = "float64", shape = (16, 7, 8))#candidate|6704|(16, 7, 8)|var|float64
bop_6705 = relay.bitwise_xor(call_6699.astype('int8'), relay.reshape(var_6704.astype('int8'), relay.shape_of(call_6699))) # shape=(16, 7, 8)
bop_6708 = relay.bitwise_xor(call_6700.astype('int8'), relay.reshape(var_6704.astype('int8'), relay.shape_of(call_6700))) # shape=(16, 7, 8)
uop_6710 = relay.atan(var_6704.astype('float32')) # shape=(16, 7, 8)
output = relay.Tuple([bop_6705,uop_6710,])
output2 = relay.Tuple([bop_6708,uop_6710,])
func_6714 = relay.Function([var_6704,], output)
mod['func_6714'] = func_6714
mod = relay.transform.InferType()(mod)
var_6715 = relay.var("var_6715", dtype = "float64", shape = (16, 7, 8))#candidate|6715|(16, 7, 8)|var|float64
output = func_6714(var_6715)
func_6716 = relay.Function([var_6715], output)
mutated_mod['func_6716'] = func_6716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_6739 = relay.TupleGetItem(func_2799_call(), 0)
call_6740 = relay.TupleGetItem(func_2801_call(), 0)
uop_6741 = relay.sqrt(call_6739.astype('float64')) # shape=(5, 15, 2)
uop_6743 = relay.sqrt(call_6740.astype('float64')) # shape=(5, 15, 2)
func_5234_call = mod.get_global_var('func_5234')
func_5237_call = mutated_mod.get_global_var('func_5237')
var_6753 = relay.var("var_6753", dtype = "float32", shape = (55, 1))#candidate|6753|(55, 1)|var|float32
call_6752 = func_5234_call(relay.reshape(var_6753.astype('float32'), [11, 1, 5]))
call_6754 = func_5234_call(relay.reshape(var_6753.astype('float32'), [11, 1, 5]))
var_6759 = relay.var("var_6759", dtype = "float64", shape = (11, 9, 5))#candidate|6759|(11, 9, 5)|var|float64
bop_6760 = relay.greater_equal(call_6752.astype('bool'), var_6759.astype('bool')) # shape=(11, 9, 5)
bop_6763 = relay.greater_equal(call_6754.astype('bool'), var_6759.astype('bool')) # shape=(11, 9, 5)
output = relay.Tuple([uop_6741,var_6753,bop_6760,])
output2 = relay.Tuple([uop_6743,var_6753,bop_6763,])
func_6776 = relay.Function([var_6753,var_6759,], output)
mod['func_6776'] = func_6776
mod = relay.transform.InferType()(mod)
var_6777 = relay.var("var_6777", dtype = "float32", shape = (55, 1))#candidate|6777|(55, 1)|var|float32
var_6778 = relay.var("var_6778", dtype = "float64", shape = (11, 9, 5))#candidate|6778|(11, 9, 5)|var|float64
output = func_6776(var_6777,var_6778,)
func_6779 = relay.Function([var_6777,var_6778,], output)
mutated_mod['func_6779'] = func_6779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4382_call = mod.get_global_var('func_4382')
func_4383_call = mutated_mod.get_global_var('func_4383')
call_6781 = relay.TupleGetItem(func_4382_call(), 0)
call_6782 = relay.TupleGetItem(func_4383_call(), 0)
output = relay.Tuple([call_6781,])
output2 = relay.Tuple([call_6782,])
func_6783 = relay.Function([], output)
mod['func_6783'] = func_6783
mod = relay.transform.InferType()(mod)
mutated_mod['func_6783'] = func_6783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6783_call = mutated_mod.get_global_var('func_6783')
call_6784 = func_6783_call()
output = call_6784
func_6785 = relay.Function([], output)
mutated_mod['func_6785'] = func_6785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5443_call = mod.get_global_var('func_5443')
func_5444_call = mutated_mod.get_global_var('func_5444')
call_6786 = relay.TupleGetItem(func_5443_call(), 1)
call_6787 = relay.TupleGetItem(func_5444_call(), 1)
func_3604_call = mod.get_global_var('func_3604')
func_3606_call = mutated_mod.get_global_var('func_3606')
var_6796 = relay.var("var_6796", dtype = "float32", shape = (280,))#candidate|6796|(280,)|var|float32
call_6795 = relay.TupleGetItem(func_3604_call(relay.reshape(var_6796.astype('float32'), [5, 7, 8])), 2)
call_6797 = relay.TupleGetItem(func_3606_call(relay.reshape(var_6796.astype('float32'), [5, 7, 8])), 2)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
call_6799 = relay.TupleGetItem(func_720_call(relay.reshape(call_6795.astype('float32'), [9, 4, 2])), 1)
call_6800 = relay.TupleGetItem(func_722_call(relay.reshape(call_6795.astype('float32'), [9, 4, 2])), 1)
func_4449_call = mod.get_global_var('func_4449')
func_4450_call = mutated_mod.get_global_var('func_4450')
call_6803 = func_4449_call()
call_6804 = func_4449_call()
output = relay.Tuple([call_6786,call_6795,var_6796,call_6799,call_6803,])
output2 = relay.Tuple([call_6787,call_6797,var_6796,call_6800,call_6804,])
func_6807 = relay.Function([var_6796,], output)
mod['func_6807'] = func_6807
mod = relay.transform.InferType()(mod)
mutated_mod['func_6807'] = func_6807
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6808 = relay.var("var_6808", dtype = "float32", shape = (280,))#candidate|6808|(280,)|var|float32
func_6807_call = mutated_mod.get_global_var('func_6807')
call_6809 = func_6807_call(var_6808)
output = call_6809
func_6810 = relay.Function([var_6808], output)
mutated_mod['func_6810'] = func_6810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_6812 = func_2899_call()
call_6813 = func_2899_call()
func_6090_call = mod.get_global_var('func_6090')
func_6093_call = mutated_mod.get_global_var('func_6093')
var_6819 = relay.var("var_6819", dtype = "float64", shape = (896,))#candidate|6819|(896,)|var|float64
const_6820 = relay.const([-9,9,3,-2,-4,4,-6,6,-1,-7,2,-1,-5,-3,10,-6,1,8,-1,10,9,-7,-4,-6,10,3,-9,4,-3,6,7,2,-7,-1,1,2,-5,4,-4,2,4,-5,2,-6,8,-6,-1,-2,9,5,-7,1,-7,-9,5,-6,9,-1,-1,-5,6,4,2,-6,-1,2,-9,10,-7,-1,-2,-1,-8,-1,-7,6,8,1,-7,-10,9,8,6,-5,7,-7,-3,-10,-1,10,9,-5,7,8,2,-4,-1,-10,10,-4,-3,4,1,7,-8,4,-2,-6,-3,-4,-2,8,1,-4,5,-6,9,2,-7,-2,7,-10,-2,-9,1,-4,2,-8,-1,-3,-8,-3,-10,-7,-8,-10,4,4,-8,-3,-8,4,10,-2,2,-7,4,-9,7,-3,-4,9,-7,-2,-8,6,1,-6,9,1,-5,4,-10,-6,-9,-1,-4,-9,-3,-3,-7,9,-8,2,-4,9,-3,1,-7,10,5,-9,2,-7,-2,-8,-1,10,3,-7,4,8,-10,-1,-5,-5,10,9,-3,-7,-1,5,-3,1,4,6,-3,-5,1,-2,-5,-9,10,-7,6,-9,10,-7,6,10,6,-7,-10,2,8,-10,-10,8,-6,-6,-8,9,8,10,6,5,7,10,6,-1,-5,-7,-1,-4,7,-9,-4,10,4,7,1,-1,8,8,-3,-8,1,3,8,6], dtype = "uint32")#candidate|6820|(260,)|const|uint32
call_6818 = relay.TupleGetItem(func_6090_call(relay.reshape(var_6819.astype('float64'), [896,]), relay.reshape(const_6820.astype('uint32'), [13, 10, 2]), ), 5)
call_6821 = relay.TupleGetItem(func_6093_call(relay.reshape(var_6819.astype('float64'), [896,]), relay.reshape(const_6820.astype('uint32'), [13, 10, 2]), ), 5)
func_4134_call = mod.get_global_var('func_4134')
func_4135_call = mutated_mod.get_global_var('func_4135')
call_6837 = func_4134_call()
call_6838 = func_4134_call()
output = relay.Tuple([call_6812,call_6818,var_6819,const_6820,call_6837,])
output2 = relay.Tuple([call_6813,call_6821,var_6819,const_6820,call_6838,])
func_6843 = relay.Function([var_6819,], output)
mod['func_6843'] = func_6843
mod = relay.transform.InferType()(mod)
var_6844 = relay.var("var_6844", dtype = "float64", shape = (896,))#candidate|6844|(896,)|var|float64
output = func_6843(var_6844)
func_6845 = relay.Function([var_6844], output)
mutated_mod['func_6845'] = func_6845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1894_call = mod.get_global_var('func_1894')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_6907 = relay.TupleGetItem(func_1894_call(), 0)
call_6908 = relay.TupleGetItem(func_1896_call(), 0)
output = relay.Tuple([call_6907,])
output2 = relay.Tuple([call_6908,])
func_6913 = relay.Function([], output)
mod['func_6913'] = func_6913
mod = relay.transform.InferType()(mod)
mutated_mod['func_6913'] = func_6913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6913_call = mutated_mod.get_global_var('func_6913')
call_6914 = func_6913_call()
output = call_6914
func_6915 = relay.Function([], output)
mutated_mod['func_6915'] = func_6915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5314_call = mod.get_global_var('func_5314')
func_5315_call = mutated_mod.get_global_var('func_5315')
call_6950 = func_5314_call()
call_6951 = func_5314_call()
var_6964 = relay.var("var_6964", dtype = "float64", shape = (16, 7, 8))#candidate|6964|(16, 7, 8)|var|float64
bop_6965 = relay.maximum(call_6950.astype('uint32'), relay.reshape(var_6964.astype('uint32'), relay.shape_of(call_6950))) # shape=(16, 7, 8)
bop_6968 = relay.maximum(call_6951.astype('uint32'), relay.reshape(var_6964.astype('uint32'), relay.shape_of(call_6951))) # shape=(16, 7, 8)
func_1130_call = mod.get_global_var('func_1130')
func_1133_call = mutated_mod.get_global_var('func_1133')
const_6972 = relay.const([1.224075,-4.002312,-3.515684,7.538166,-2.117737,-8.046852,9.701334,-0.719449,7.328418,-4.312165,-8.240131,-6.026513,3.723898,-1.658645,-5.384101,9.793846,-6.296958,-8.482653,-1.035588,-4.719909,-4.355629,7.385226,0.781234,-5.461303,0.934229,-5.192705,-6.544755,-5.659273,8.143767,-7.001630,-5.653870,2.163047,9.533771,6.749291,-8.749834,-5.607145,4.964644,-7.592307,-6.782527,6.784197,-0.476367,9.601819,0.802149,-0.474121,8.484897,-1.722607,-3.321164,-5.722338,6.041142,2.403859,4.626155,-2.643043,9.644537,0.425952,4.851405,0.836594,-1.618597,2.619027,-9.286402,2.136642,-2.443852,-6.126085,4.419693,1.635842,-4.953760,-4.273399,-1.796243,-3.553154,-0.750829,7.194046,5.428242,2.224576,-6.184622,6.526494,-1.294190,-6.411767,-9.411391,8.524970,2.627108,-3.537771,0.553333,2.183103,2.357518,-4.868089,0.474600,0.654194,-5.295022,-8.977673,6.662158,-5.678261,-5.944224,1.566521,2.818997,1.433240,6.487915,-9.353123,-4.321799,-6.768387,-2.021141,4.748936,1.048981,-1.873636,0.426980,-9.011475,-7.840684,-4.085263,4.437252,8.424074,-8.609238,8.971793,-5.105398,9.987398,8.770003,-5.923407,-9.756011,2.913783,-5.429794,3.491606,-1.359370,6.869374,-5.990266,-9.761025,6.538803,-0.327451,-9.216777,9.720504,-7.635770,7.422132,-5.959906,2.528558,-3.657685,-1.429695,-4.265718,-3.035023,3.879292,4.176424,-1.813213,0.278356,0.901581,2.610780,7.232746,-9.737753,5.543661,5.555906,0.914340,-6.629672,5.362800,-8.741062,6.329346,9.074609,-5.824121,-9.474396,-5.992354,-3.932105,-9.292378,5.427313,-0.602223,5.270601,1.504552,-4.108294,7.845122,-3.301020,4.209170,-5.058183,-1.085342,-1.766901,-6.360085,5.869130,-7.472918,-7.681478,4.690889,6.508910,8.198665,-8.712458,1.447875,1.385339,9.526777,-1.238870,-9.364013,5.939628,-6.847627,-1.311809,4.397489,9.540079,1.626797,-8.629856,3.992669,8.105474,-0.915773,1.300845,-4.636761,-1.721885,7.542430,-9.597879,0.463907,-2.848340,9.014544,-7.025482,-1.514419,3.451940,8.611962,-2.778712,0.057058,3.396762,1.834603,9.700260,8.642731,-8.214098,-5.698029,-5.687608,-1.243162,4.784889,8.749048,-8.930324,1.837259,-0.123774,5.319651,1.005712,-9.369131,-2.863934,-0.744394,3.567364,1.364947,-0.797367,-0.944871,4.899814,1.190144,9.969737,-2.561345,-7.037807,1.383954,-1.753489,1.829528,1.978931,-8.231090,-6.267361,9.144549,-1.366181,4.225141,8.522334,-5.967656,-8.643383,6.724996,-7.089074,-7.194865,-2.507095,9.445984,-9.927155,-2.156344,-8.319938,-3.773461,0.672041,-0.895484,-7.982746,-2.397272,-6.420886,2.146451,-6.019205,-6.281581,-5.496900], dtype = "float32")#candidate|6972|(260,)|const|float32
call_6971 = relay.TupleGetItem(func_1130_call(relay.reshape(const_6972.astype('float32'), [260,])), 2)
call_6973 = relay.TupleGetItem(func_1133_call(relay.reshape(const_6972.astype('float32'), [260,])), 2)
bop_6977 = relay.less_equal(var_6964.astype('bool'), relay.reshape(call_6950.astype('bool'), relay.shape_of(var_6964))) # shape=(16, 7, 8)
bop_6980 = relay.less_equal(var_6964.astype('bool'), relay.reshape(call_6951.astype('bool'), relay.shape_of(var_6964))) # shape=(16, 7, 8)
func_6357_call = mod.get_global_var('func_6357')
func_6358_call = mutated_mod.get_global_var('func_6358')
call_6985 = relay.TupleGetItem(func_6357_call(), 0)
call_6986 = relay.TupleGetItem(func_6358_call(), 0)
uop_6988 = relay.asin(bop_6965.astype('float32')) # shape=(16, 7, 8)
uop_6990 = relay.asin(bop_6968.astype('float32')) # shape=(16, 7, 8)
func_5234_call = mod.get_global_var('func_5234')
func_5237_call = mutated_mod.get_global_var('func_5237')
const_7000 = relay.const([-8.882356,4.119964,-3.374663,-5.458274,-3.714241,7.006998,-0.662479,-5.664263,2.822122,-7.098478,-9.969810,-3.258902,-8.669279,7.455781,2.284804,-9.344798,0.886465,5.375925,-7.224434,5.877006,9.568978,2.681597,-2.678358,-3.506181,3.617015,-1.226945,-1.114722,9.582095,-7.005113,-0.561536,-9.206476,-1.292956,8.054126,4.351328,0.833648,-8.809343,4.141665,-9.467147,-7.009710,-4.197146,8.006945,3.913276,0.868667,-4.700069,-4.058198,1.479209,4.934565,-1.828211,4.733369,3.413314,-1.895114,-7.397041,2.784635,-5.179750,5.084270], dtype = "float32")#candidate|7000|(55,)|const|float32
call_6999 = func_5234_call(relay.reshape(const_7000.astype('float32'), [11, 1, 5]))
call_7001 = func_5234_call(relay.reshape(const_7000.astype('float32'), [11, 1, 5]))
func_6714_call = mod.get_global_var('func_6714')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_7002 = relay.TupleGetItem(func_6714_call(relay.reshape(var_6964.astype('float64'), [16, 7, 8])), 1)
call_7003 = relay.TupleGetItem(func_6716_call(relay.reshape(var_6964.astype('float64'), [16, 7, 8])), 1)
uop_7004 = relay.asinh(uop_6988.astype('float32')) # shape=(16, 7, 8)
uop_7006 = relay.asinh(uop_6990.astype('float32')) # shape=(16, 7, 8)
output = relay.Tuple([call_6971,const_6972,bop_6977,call_6985,call_6999,const_7000,call_7002,uop_7004,])
output2 = relay.Tuple([call_6973,const_6972,bop_6980,call_6986,call_7001,const_7000,call_7003,uop_7006,])
func_7007 = relay.Function([var_6964,], output)
mod['func_7007'] = func_7007
mod = relay.transform.InferType()(mod)
mutated_mod['func_7007'] = func_7007
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7008 = relay.var("var_7008", dtype = "float64", shape = (16, 7, 8))#candidate|7008|(16, 7, 8)|var|float64
func_7007_call = mutated_mod.get_global_var('func_7007')
call_7009 = func_7007_call(var_7008)
output = call_7009
func_7010 = relay.Function([var_7008], output)
mutated_mod['func_7010'] = func_7010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5593_call = mod.get_global_var('func_5593')
func_5595_call = mutated_mod.get_global_var('func_5595')
call_7021 = relay.TupleGetItem(func_5593_call(), 0)
call_7022 = relay.TupleGetItem(func_5595_call(), 0)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_7024 = func_574_call()
call_7025 = func_574_call()
func_5809_call = mod.get_global_var('func_5809')
func_5810_call = mutated_mod.get_global_var('func_5810')
call_7034 = func_5809_call()
call_7035 = func_5809_call()
output = relay.Tuple([call_7021,call_7024,call_7034,])
output2 = relay.Tuple([call_7022,call_7025,call_7035,])
func_7043 = relay.Function([], output)
mod['func_7043'] = func_7043
mod = relay.transform.InferType()(mod)
mutated_mod['func_7043'] = func_7043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7043_call = mutated_mod.get_global_var('func_7043')
call_7044 = func_7043_call()
output = call_7044
func_7045 = relay.Function([], output)
mutated_mod['func_7045'] = func_7045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6913_call = mod.get_global_var('func_6913')
func_6915_call = mutated_mod.get_global_var('func_6915')
call_7179 = relay.TupleGetItem(func_6913_call(), 0)
call_7180 = relay.TupleGetItem(func_6915_call(), 0)
output = relay.Tuple([call_7179,])
output2 = relay.Tuple([call_7180,])
func_7218 = relay.Function([], output)
mod['func_7218'] = func_7218
mod = relay.transform.InferType()(mod)
output = func_7218()
func_7219 = relay.Function([], output)
mutated_mod['func_7219'] = func_7219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1260_call = mod.get_global_var('func_1260')
func_1262_call = mutated_mod.get_global_var('func_1262')
call_7241 = relay.TupleGetItem(func_1260_call(), 1)
call_7242 = relay.TupleGetItem(func_1262_call(), 1)
output = call_7241
output2 = call_7242
func_7252 = relay.Function([], output)
mod['func_7252'] = func_7252
mod = relay.transform.InferType()(mod)
output = func_7252()
func_7253 = relay.Function([], output)
mutated_mod['func_7253'] = func_7253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_7264 = func_2899_call()
call_7265 = func_2899_call()
output = call_7264
output2 = call_7265
func_7315 = relay.Function([], output)
mod['func_7315'] = func_7315
mod = relay.transform.InferType()(mod)
output = func_7315()
func_7316 = relay.Function([], output)
mutated_mod['func_7316'] = func_7316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7328 = relay.var("var_7328", dtype = "uint32", shape = (16, 2, 4))#candidate|7328|(16, 2, 4)|var|uint32
var_7329 = relay.var("var_7329", dtype = "uint32", shape = (16, 2, 4))#candidate|7329|(16, 2, 4)|var|uint32
bop_7330 = relay.right_shift(var_7328.astype('uint32'), relay.reshape(var_7329.astype('uint32'), relay.shape_of(var_7328))) # shape=(16, 2, 4)
output = relay.Tuple([bop_7330,])
output2 = relay.Tuple([bop_7330,])
func_7339 = relay.Function([var_7328,var_7329,], output)
mod['func_7339'] = func_7339
mod = relay.transform.InferType()(mod)
var_7340 = relay.var("var_7340", dtype = "uint32", shape = (16, 2, 4))#candidate|7340|(16, 2, 4)|var|uint32
var_7341 = relay.var("var_7341", dtype = "uint32", shape = (16, 2, 4))#candidate|7341|(16, 2, 4)|var|uint32
output = func_7339(var_7340,var_7341,)
func_7342 = relay.Function([var_7340,var_7341,], output)
mutated_mod['func_7342'] = func_7342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4254_call = mod.get_global_var('func_4254')
func_4256_call = mutated_mod.get_global_var('func_4256')
call_7370 = func_4254_call()
call_7371 = func_4254_call()
output = call_7370
output2 = call_7371
func_7381 = relay.Function([], output)
mod['func_7381'] = func_7381
mod = relay.transform.InferType()(mod)
mutated_mod['func_7381'] = func_7381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7381_call = mutated_mod.get_global_var('func_7381')
call_7382 = func_7381_call()
output = call_7382
func_7383 = relay.Function([], output)
mutated_mod['func_7383'] = func_7383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4449_call = mod.get_global_var('func_4449')
func_4450_call = mutated_mod.get_global_var('func_4450')
call_7394 = func_4449_call()
call_7395 = func_4449_call()
uop_7399 = relay.log(call_7394.astype('float64')) # shape=(1, 7, 8)
uop_7401 = relay.log(call_7395.astype('float64')) # shape=(1, 7, 8)
output = relay.Tuple([uop_7399,])
output2 = relay.Tuple([uop_7401,])
func_7402 = relay.Function([], output)
mod['func_7402'] = func_7402
mod = relay.transform.InferType()(mod)
mutated_mod['func_7402'] = func_7402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7402_call = mutated_mod.get_global_var('func_7402')
call_7403 = func_7402_call()
output = call_7403
func_7404 = relay.Function([], output)
mutated_mod['func_7404'] = func_7404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7418 = relay.var("var_7418", dtype = "uint16", shape = (8, 15, 8))#candidate|7418|(8, 15, 8)|var|uint16
var_7419 = relay.var("var_7419", dtype = "uint16", shape = (8, 15, 8))#candidate|7419|(8, 15, 8)|var|uint16
bop_7420 = relay.right_shift(var_7418.astype('uint16'), relay.reshape(var_7419.astype('uint16'), relay.shape_of(var_7418))) # shape=(8, 15, 8)
func_7402_call = mod.get_global_var('func_7402')
func_7404_call = mutated_mod.get_global_var('func_7404')
call_7423 = relay.TupleGetItem(func_7402_call(), 0)
call_7424 = relay.TupleGetItem(func_7404_call(), 0)
output = relay.Tuple([bop_7420,call_7423,])
output2 = relay.Tuple([bop_7420,call_7424,])
func_7429 = relay.Function([var_7418,var_7419,], output)
mod['func_7429'] = func_7429
mod = relay.transform.InferType()(mod)
var_7430 = relay.var("var_7430", dtype = "uint16", shape = (8, 15, 8))#candidate|7430|(8, 15, 8)|var|uint16
var_7431 = relay.var("var_7431", dtype = "uint16", shape = (8, 15, 8))#candidate|7431|(8, 15, 8)|var|uint16
output = func_7429(var_7430,var_7431,)
func_7432 = relay.Function([var_7430,var_7431,], output)
mutated_mod['func_7432'] = func_7432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7315_call = mod.get_global_var('func_7315')
func_7316_call = mutated_mod.get_global_var('func_7316')
call_7443 = func_7315_call()
call_7444 = func_7315_call()
output = call_7443
output2 = call_7444
func_7452 = relay.Function([], output)
mod['func_7452'] = func_7452
mod = relay.transform.InferType()(mod)
mutated_mod['func_7452'] = func_7452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7452_call = mutated_mod.get_global_var('func_7452')
call_7453 = func_7452_call()
output = call_7453
func_7454 = relay.Function([], output)
mutated_mod['func_7454'] = func_7454
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7532 = relay.var("var_7532", dtype = "float64", shape = (9, 11, 2))#candidate|7532|(9, 11, 2)|var|float64
uop_7533 = relay.rsqrt(var_7532.astype('float64')) # shape=(9, 11, 2)
func_2391_call = mod.get_global_var('func_2391')
func_2392_call = mutated_mod.get_global_var('func_2392')
call_7535 = relay.TupleGetItem(func_2391_call(), 0)
call_7536 = relay.TupleGetItem(func_2392_call(), 0)
bop_7540 = relay.not_equal(uop_7533.astype('bool'), relay.reshape(var_7532.astype('bool'), relay.shape_of(uop_7533))) # shape=(9, 11, 2)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_7546 = relay.TupleGetItem(func_2799_call(), 0)
call_7547 = relay.TupleGetItem(func_2801_call(), 0)
func_6913_call = mod.get_global_var('func_6913')
func_6915_call = mutated_mod.get_global_var('func_6915')
call_7556 = relay.TupleGetItem(func_6913_call(), 0)
call_7557 = relay.TupleGetItem(func_6915_call(), 0)
output = relay.Tuple([call_7535,bop_7540,call_7546,call_7556,])
output2 = relay.Tuple([call_7536,bop_7540,call_7547,call_7557,])
func_7564 = relay.Function([var_7532,], output)
mod['func_7564'] = func_7564
mod = relay.transform.InferType()(mod)
var_7565 = relay.var("var_7565", dtype = "float64", shape = (9, 11, 2))#candidate|7565|(9, 11, 2)|var|float64
output = func_7564(var_7565)
func_7566 = relay.Function([var_7565], output)
mutated_mod['func_7566'] = func_7566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5722_call = mod.get_global_var('func_5722')
func_5724_call = mutated_mod.get_global_var('func_5724')
call_7568 = relay.TupleGetItem(func_5722_call(), 0)
call_7569 = relay.TupleGetItem(func_5724_call(), 0)
func_3718_call = mod.get_global_var('func_3718')
func_3720_call = mutated_mod.get_global_var('func_3720')
call_7572 = relay.TupleGetItem(func_3718_call(), 1)
call_7573 = relay.TupleGetItem(func_3720_call(), 1)
func_3132_call = mod.get_global_var('func_3132')
func_3133_call = mutated_mod.get_global_var('func_3133')
call_7595 = func_3132_call()
call_7596 = func_3132_call()
func_746_call = mod.get_global_var('func_746')
func_749_call = mutated_mod.get_global_var('func_749')
var_7620 = relay.var("var_7620", dtype = "float64", shape = (90,))#candidate|7620|(90,)|var|float64
call_7619 = relay.TupleGetItem(func_746_call(relay.reshape(var_7620.astype('float64'), [1, 9, 10]), relay.reshape(var_7620.astype('float64'), [1, 9, 10]), ), 0)
call_7621 = relay.TupleGetItem(func_749_call(relay.reshape(var_7620.astype('float64'), [1, 9, 10]), relay.reshape(var_7620.astype('float64'), [1, 9, 10]), ), 0)
output = relay.Tuple([call_7568,call_7572,call_7595,call_7619,var_7620,])
output2 = relay.Tuple([call_7569,call_7573,call_7596,call_7621,var_7620,])
func_7628 = relay.Function([var_7620,], output)
mod['func_7628'] = func_7628
mod = relay.transform.InferType()(mod)
mutated_mod['func_7628'] = func_7628
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7629 = relay.var("var_7629", dtype = "float64", shape = (90,))#candidate|7629|(90,)|var|float64
func_7628_call = mutated_mod.get_global_var('func_7628')
call_7630 = func_7628_call(var_7629)
output = call_7630
func_7631 = relay.Function([var_7629], output)
mutated_mod['func_7631'] = func_7631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4349_call = mod.get_global_var('func_4349')
func_4350_call = mutated_mod.get_global_var('func_4350')
call_7652 = relay.TupleGetItem(func_4349_call(), 0)
call_7653 = relay.TupleGetItem(func_4350_call(), 0)
var_7661 = relay.var("var_7661", dtype = "float64", shape = (1, 7, 8))#candidate|7661|(1, 7, 8)|var|float64
bop_7662 = relay.logical_and(call_7652.astype('bool'), relay.reshape(var_7661.astype('bool'), relay.shape_of(call_7652))) # shape=(1, 7, 8)
bop_7665 = relay.logical_and(call_7653.astype('bool'), relay.reshape(var_7661.astype('bool'), relay.shape_of(call_7653))) # shape=(1, 7, 8)
output = relay.Tuple([bop_7662,])
output2 = relay.Tuple([bop_7665,])
func_7666 = relay.Function([var_7661,], output)
mod['func_7666'] = func_7666
mod = relay.transform.InferType()(mod)
var_7667 = relay.var("var_7667", dtype = "float64", shape = (1, 7, 8))#candidate|7667|(1, 7, 8)|var|float64
output = func_7666(var_7667)
func_7668 = relay.Function([var_7667], output)
mutated_mod['func_7668'] = func_7668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mod.get_global_var('func_4280')
func_4281_call = mutated_mod.get_global_var('func_4281')
call_7672 = relay.TupleGetItem(func_4280_call(), 0)
call_7673 = relay.TupleGetItem(func_4281_call(), 0)
var_7677 = relay.var("var_7677", dtype = "float64", shape = (15, 7, 8))#candidate|7677|(15, 7, 8)|var|float64
bop_7678 = relay.floor_divide(call_7672.astype('float64'), var_7677.astype('float64')) # shape=(15, 7, 8)
bop_7681 = relay.floor_divide(call_7673.astype('float64'), var_7677.astype('float64')) # shape=(15, 7, 8)
output = bop_7678
output2 = bop_7681
func_7691 = relay.Function([var_7677,], output)
mod['func_7691'] = func_7691
mod = relay.transform.InferType()(mod)
var_7692 = relay.var("var_7692", dtype = "float64", shape = (15, 7, 8))#candidate|7692|(15, 7, 8)|var|float64
output = func_7691(var_7692)
func_7693 = relay.Function([var_7692], output)
mutated_mod['func_7693'] = func_7693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_7699 = relay.TupleGetItem(func_3034_call(), 0)
call_7700 = relay.TupleGetItem(func_3035_call(), 0)
func_1260_call = mod.get_global_var('func_1260')
func_1262_call = mutated_mod.get_global_var('func_1262')
call_7760 = relay.TupleGetItem(func_1260_call(), 1)
call_7761 = relay.TupleGetItem(func_1262_call(), 1)
func_2411_call = mod.get_global_var('func_2411')
func_2414_call = mutated_mod.get_global_var('func_2414')
const_7764 = relay.const([[-1,1,-3,-8,-6,7,1,1,-2,9,-9,1,6,-1,-7,-5,3,-6],[-6,1,1,9,5,5,5,7,9,-7,-7,-5,5,-5,-7,7,5,5],[-6,-9,6,-2,10,-5,9,-5,-8,1,2,2,-6,5,6,7,-6,-7],[-2,3,8,10,10,4,-8,3,-10,3,5,9,-10,5,3,-8,1,-7],[-9,-6,4,7,2,6,-5,2,-7,-3,-5,2,-10,-5,4,-2,8,-4],[-8,6,2,-4,1,9,6,4,8,-1,6,3,-7,3,-5,-8,9,-2],[10,-8,-3,8,6,-3,7,7,2,-3,5,4,4,-2,10,2,2,-10],[4,4,-1,6,-3,-9,-3,5,10,-9,-5,-5,-4,4,8,1,-3,4],[4,-2,-3,3,5,3,9,-10,-2,9,4,2,-9,-6,9,-8,9,1],[1,5,2,-3,-1,-5,-10,9,-10,-7,-3,3,10,3,1,1,-8,2],[-6,2,8,10,-4,1,7,4,1,-10,-1,2,8,6,2,7,10,7],[9,-5,6,8,8,-5,-1,1,1,4,1,-5,-5,-2,2,-5,9,-3],[-8,2,4,4,-4,5,-2,-3,8,-5,10,10,-9,4,-6,6,-9,1],[-6,7,2,3,1,-7,4,2,9,10,8,9,1,8,-2,1,6,7],[-2,-3,6,3,-2,-8,8,1,9,10,5,-10,-8,6,3,-3,-2,7],[4,10,7,-7,5,3,-7,-4,2,1,8,-8,-9,-5,5,2,4,-7],[9,7,1,-8,2,3,9,-8,1,8,-4,4,-5,-3,8,9,2,-3],[-4,5,4,-2,4,-10,5,-7,-8,-2,-9,1,3,-9,6,9,-3,-7]], dtype = "uint8")#candidate|7764|(18, 18)|const|uint8
call_7763 = func_2411_call(relay.reshape(const_7764.astype('uint8'), [9, 3, 12]))
call_7765 = func_2411_call(relay.reshape(const_7764.astype('uint8'), [9, 3, 12]))
output = relay.Tuple([call_7699,call_7760,call_7763,const_7764,])
output2 = relay.Tuple([call_7700,call_7761,call_7765,const_7764,])
func_7766 = relay.Function([], output)
mod['func_7766'] = func_7766
mod = relay.transform.InferType()(mod)
output = func_7766()
func_7767 = relay.Function([], output)
mutated_mod['func_7767'] = func_7767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6681_call = mod.get_global_var('func_6681')
func_6682_call = mutated_mod.get_global_var('func_6682')
call_7773 = func_6681_call()
call_7774 = func_6681_call()
func_3681_call = mod.get_global_var('func_3681')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_7777 = relay.TupleGetItem(func_3681_call(), 2)
call_7778 = relay.TupleGetItem(func_3682_call(), 2)
func_720_call = mod.get_global_var('func_720')
func_722_call = mutated_mod.get_global_var('func_722')
var_7783 = relay.var("var_7783", dtype = "float32", shape = (72,))#candidate|7783|(72,)|var|float32
call_7782 = relay.TupleGetItem(func_720_call(relay.reshape(var_7783.astype('float32'), [9, 4, 2])), 1)
call_7784 = relay.TupleGetItem(func_722_call(relay.reshape(var_7783.astype('float32'), [9, 4, 2])), 1)
func_2490_call = mod.get_global_var('func_2490')
func_2494_call = mutated_mod.get_global_var('func_2494')
const_7793 = relay.const([5.831047,2.110436,-2.256878,-6.283752,-1.389407,-3.749527,6.014582,0.134068,0.057141,9.528675,-8.995994,3.858085,7.633243,2.933614,-5.013148,4.140406,-8.254445,7.031803,-7.629084,6.438277,-6.334415,-5.709860,0.785543,9.666468,-2.449874,3.186408,5.283023,-5.081611,8.882246,5.879725,9.142794,3.846940,8.820159,-8.860837,4.379117,-2.591171,1.808401,6.461227,-8.588728,9.260568,1.247480,-7.411026,5.204289,6.875416,-3.608047,7.174856,3.932912,1.880430,2.679648,-3.345580,6.216557,2.524353,1.581627,1.815447,2.924168,-8.559389,4.701966,0.654584,4.431789,-5.003358,6.307899,-8.713808,-9.206412,2.530731,0.766694,-6.420909,-2.041152,-7.760013,-8.723480,-1.270861,-6.970849,-4.194389,8.651883,2.394526,-6.703730,-4.500379,3.188174,-9.156407,-2.550314,5.013862,-9.442027,-5.123452,8.929200,-7.324560,-5.887095,1.328160,-1.781408,-9.097315,3.134763,-8.671002,7.605405,7.812166,5.718965,1.043876,9.803017,-9.424919,-0.893100,4.668340,9.947283,-0.775098,-4.883024,-8.674611,3.828953,-0.478125,-0.814567,3.723370,7.773525,-7.881072,-1.005812,-6.274313,3.461552,4.868629,6.143957,1.901392,6.176951,-8.054589,-9.379013,-9.582494,5.828684,-0.871818,6.000707,-1.731429,4.150066,-5.531874,-0.220776,0.521391,5.468941,9.003951,8.518583,5.483897,-0.880071,-0.392301,-8.717863,9.685166,1.015554,-0.810493,0.876325,2.126997,9.637878,-6.333868,-0.219086,8.782833,6.118718,-5.091568,-6.493820,1.737472,0.695340,0.064970,-2.133881,-7.092745,-3.831302,-2.780295,4.996432,-5.644785,1.381126,-7.580024,9.202973,7.730746,-5.244429,5.967870,2.343472,-0.366916,2.309017,3.643754,-6.819489,6.406036,-3.735172,-8.126664,-3.049523,-3.893797,9.012071,8.317525,5.532686,0.173495,2.284181,-5.716687,9.497219,7.163967,-0.802869,-7.229705,-0.052153,8.710851,-7.973234,-1.147427,5.194582,-0.411745,3.870890,4.282301,7.664693,2.432613,4.499748,0.124525,-2.908666,1.415657,9.610385,0.296503,-1.993833,-5.085141,-3.035088,2.183311,-9.223239,-6.278869,1.330462,-2.628687,1.403159,2.702534,3.563609,0.922471,-2.241579,-8.511333,8.400393,1.156569,-1.930845,-4.630962,5.574825,-2.882641,2.249367,9.142941,-4.657824,6.849706,9.578000,2.298738,-7.878560,-4.953149,3.955456,-6.736305,-3.398334,-5.991311,-4.032542,7.036788,-9.629083,6.113934,8.709063,4.268318,-4.640733,5.764376,0.749722,-4.934331,0.041264,-7.809734,7.933312,8.674396,1.650581,-5.869795,-4.658909,9.203684,-6.430589,0.343352,1.858242,6.431445,8.953039,-3.910711,5.368663,-2.182045,8.281693,-6.965052,-8.134265,7.236523,9.374740,3.600005,7.496118,3.499208,2.792305,9.626196,2.590494,-0.383201,9.621037,0.124295,6.906888,-3.006460,6.466513,4.877469,-2.187165,8.715945,-4.439881,-4.379663,3.292624,9.898489,-7.597954,0.324147,-7.006790,-0.812417,-5.053640,-4.543267,-0.746461,9.754650,7.185771,8.568507,4.499415,-3.923434,6.213554,4.301960,-5.993947,4.720917,-1.520713,-4.815299,-3.029847,-8.589233,-2.820324,-4.899809,7.489314,-7.307795,-3.611560,1.778878,-8.835858,8.861784,-3.386902,-3.398833,-9.407648,8.323437,1.333729,4.174587,-4.247770,-4.543553,-9.078789,2.539122,-8.113034,4.849859,5.527620,-1.958339,-5.544245,7.181788,0.176250,7.582153,3.332485,-8.595875,-6.926245,-3.323555,5.385114,7.735643,5.679722,-5.007534,2.867420,-9.525572,-7.034894,-4.448074,1.294347,9.356823,-5.904565,-3.397079,7.101206,-1.437990,-0.425694,-2.354938,0.762245,7.972032,1.671480,9.525470,7.810501,4.445332,-8.187935,-8.705316,-7.894860,-4.910501,-0.174240,-2.901008,8.751109,6.333599,-0.405215,-6.274671,-1.485580,-0.818739,9.202146,-3.936653,-2.206510,-5.073038,0.454802,-1.344158,-4.508277,-2.314293,1.026732,-5.685811,7.685880,-1.189878,0.096687,-0.898005,-1.250889,5.625108,-2.797669,5.672060,-0.951624,4.886131,-0.216022,1.651266,3.377395,-3.023516,-1.601805,2.233852,-5.391282,5.662033,-3.213567,9.904639,8.018692,-1.936381,-5.526672,-1.496266,0.379095,6.244937,1.315023,-5.061353,-4.977304,7.537898,7.157551,6.082460,-5.037033,-8.826193,-2.488582,2.402013,-5.385776,1.835321,8.291878,4.777386,6.356039,0.529046,6.483996,9.051979,-6.607863,6.945985,-8.267447,2.451948,7.607859,0.261553,-8.473810,4.576273,0.558826,6.443877,-5.514163,7.215282,2.536106,-2.950126,6.891176,0.999272,-3.978412,3.285438,5.886608,9.271072,-2.932055,-7.473362,-5.623102,-3.755980,-9.738568,-6.122311,-7.228396,-5.966920,-4.927561,3.023208,3.056498,6.027277,9.075736,-3.747013,-5.514504,3.118900,-5.887200,0.523676,-9.196572,-3.570795,3.093175,9.517453,6.082255,-9.691682,0.798403,2.111926,-7.031791,-7.078324,0.329848,-0.296779,3.420248,7.623579,6.144653,-0.508360,-5.170778,-5.187942,4.389808,3.736265,1.754843,9.369216,3.591149,9.734135,9.454798,6.568832,-6.886232,-2.762346,-6.333628,-8.215866,-1.456141,0.260827,4.211559,0.028566,4.899544,4.842951,-9.670892,9.043084,1.683127,4.663398,8.407259,-7.116826,-5.868739,6.049686,-9.835142,-2.226354,-0.626004,8.859094,3.965410,-5.481917,6.598296,0.549647,-4.831637,-9.544970,-5.827349,8.155723,-1.825197,9.261569,-8.166704,5.243041,-7.207344,-5.875979,4.019679,6.578753,-7.988517,-6.758804,6.237268,7.720025,-4.003257,-3.941453,0.698754,-9.848901,4.700063,-9.620815,-7.486079,-9.320048,3.668467,1.073435,-5.038917,5.649639,3.265883,-8.435220,8.995651,-9.440594,7.622043,-1.785587,-0.387943,6.807761,3.309130,-8.599725,1.997759,-8.143804,7.926098,-3.494979,-6.556080,-8.875944,6.339059,1.668540,-2.883567,-2.914181,-4.693118,-4.914690,-2.517708,-2.113872,9.801456,7.385603,7.617284,6.430654,-4.621161,-7.400078,3.863121,-8.733851,3.693970,3.593304,2.568374,-1.186009,5.562760,2.180009,-8.828780,9.619617,-1.504745,-7.253348,-1.047999,-5.195917,6.308350,-1.029363,5.562937,4.835431,-5.960546,-6.672141,2.244664,3.766197,6.279595,-3.830380,-3.788669,8.179632,-5.469756,-4.587832,7.915215,0.237531,5.519098,0.718847,-3.126171,8.322206,7.907020,9.487473,-1.509767,8.453180,4.801910,3.765441,7.731728,-8.964835,0.151482,7.611554,2.826669,8.973447,-0.023737,9.215667,-2.002875,9.643120,-8.187142,-0.094181,1.586304,-9.835705,7.702397,-0.967400,-5.884284,-6.501422,3.343987,-9.138219,7.128539,8.893441,-4.758196,-6.368415,7.162327,-6.487624,-0.990334,5.988270,2.619070,-9.284204,8.378082,0.267628,4.200902,8.740738,8.777201,2.468021,-9.018094,-7.529800,8.235389,0.973921,-0.642162,-4.652784,-6.829459,-8.055747,6.647849,-0.799810,9.601447,-7.336214,1.828627,5.273432,9.914253,4.908617,0.195431,-9.489838,2.836286,-4.879636,-3.575790,-4.932486,-1.666355,-9.774798,-2.012647,-2.330289,-2.048584,-0.140428,7.607336,7.102995,2.006395,-2.008777,-9.835339,8.610027,-2.855539,-4.125807,8.108124,3.651953,8.728221,7.434816,-2.724070,-6.787891,1.169911,-3.490170,-1.539643,5.654534,5.353915,7.362577,6.719192,1.560729,-5.110282,-2.191260,-3.814388,2.169730,1.051910,6.304406,-5.877004,-6.725060,4.372197,-7.024583,-0.106836,8.358239,1.814796,-3.987851,0.938357,-4.728077,1.881620,6.640859,-0.993328,3.569327,-1.517990,1.512829,-3.856933,-3.556258,5.156441,-4.119709,-9.569990,2.485704,-7.319987,-0.731720,2.391130,5.497138,9.704354,-5.207654,4.486057,5.729220,4.215893,-8.317778,1.009445,6.565995,-8.893533,-5.482589,4.757403,-8.648331,4.113242,4.023992,-5.002369,6.879300,-0.185082,5.331771,-8.756009,0.233790,-0.345323,2.567186,-2.816159,-2.660085,-8.960362,8.863678,-1.982154,1.119538,6.472166,-0.017336,4.204307,5.581135,6.917166,1.013065,-0.208197,4.191686,3.497235,-4.989059,6.692004,-1.376245,4.985597,0.377070,7.961188,-0.525236,-5.206786,-3.307694,-8.263142,7.685164,8.791809,0.844052,9.804490,-8.131385,-0.448528,-0.060618,5.855121,8.712476,-1.152131,-3.590071,-7.714424,-2.002963,3.136693,-4.360966,3.933157,2.153747,9.643402,-7.212154,-0.550565,3.635467,9.310048,-1.717966,-8.854195,4.278186,8.063576,-7.178207,-2.730938,-1.681068,-2.025480,-5.622803,-4.292750,-1.616721,-0.880437,-0.648767,8.647597,3.268998,0.797401,9.080642,-5.233119,-1.458728,-3.038770,3.518557,-1.665954,-3.919717,-6.219843,-7.139705,-4.334617,-9.980266,2.716503,3.754230,-0.999084,4.848834,1.345978,4.790509,8.357953,1.520333,5.345387,6.976694,-4.700429,-4.242006,-5.242226,4.500349,7.134315,3.431649,-0.901389,3.664457,-8.767272,-4.748037,0.712993,6.672323,1.268523,-7.497008,6.390510,-7.057183,0.011291,-8.032858,4.652368,-4.832931,-6.037005,2.854343,8.818560,3.672273,9.494170,5.404973,-0.574107,-1.923742,4.354343,-0.443522,-2.186308,-7.572207,8.169799,0.378289,-8.701154,5.648403,6.728500,4.475343,8.118979,-5.249978,-4.966771,8.090506,-5.404469,-8.423787,-3.247695,-9.410357,-4.473272,-1.662743,-8.861541,-0.806846,7.790867,9.516664,2.384001,3.281641,5.200652,2.477769,8.340365,-7.358914,-3.272864,9.216223,9.551981,9.155270,-2.072571,6.929702,1.798222,5.048124,6.783615,-8.698750], dtype = "float64")#candidate|7793|(896,)|const|float64
call_7792 = relay.TupleGetItem(func_2490_call(relay.reshape(const_7793.astype('float64'), [16, 7, 8]), relay.reshape(call_7782.astype('float64'), [56,]), ), 2)
call_7794 = relay.TupleGetItem(func_2494_call(relay.reshape(const_7793.astype('float64'), [16, 7, 8]), relay.reshape(call_7782.astype('float64'), [56,]), ), 2)
func_4325_call = mod.get_global_var('func_4325')
func_4328_call = mutated_mod.get_global_var('func_4328')
const_7796 = relay.const([-7.814463,-9.348894,-2.150319,9.154209,9.723942,2.191876,-9.191833,-4.014916,0.863920,-3.099329,-8.133958,-0.863526,5.321579,6.754080,7.808477,-6.262575,4.749564,-0.667804,0.380177,1.840708,-5.651767,4.885819,7.130565,8.254114,-4.133635,-7.687660,1.664328,5.477171,2.358058,-9.277514,2.216040,-0.072586,9.066130,-3.376039,-7.017070,-3.638908,0.891152,-3.709676,7.184964,9.386178,5.150535,-0.169484,-4.382811,3.258888,-6.393656,5.932261,0.947590,6.115228,-8.344403,2.483569,0.518089,3.044807,6.523912,7.999703,5.398615,0.823603,-5.406703,-0.182677,8.622780,9.518255,7.952315,0.679376,-3.469029,5.786941,-5.762809,-2.727981,-8.185314,-3.098695,6.241637,-7.727242,5.010459,5.941501,-9.750360,-2.973377,-3.272139,9.145990,-0.684111,-8.986332,7.554114,8.237690,-4.441704,5.850143,-8.298622,-6.927318,-4.104916,-0.540088,-1.883148,3.269049,9.691654,-6.892098,1.392293,7.941228,-6.210486,1.740309,-2.889161,-5.136909,-6.015445,2.275373,3.413512,-0.549968,5.971982,4.172385,-1.528636,-2.535115,0.668735,7.639490,-5.022686,-1.127055,-8.601792,0.302603,5.358745,9.975562,6.878141,-0.543073,1.573988,-8.943700,5.005859,-2.997566,6.210355,-5.482930,-7.619871,5.331567,-9.599272,2.720824,5.674140,8.936162,-1.564015,-2.038343,-1.192211,4.340950,9.398586,-5.559896,1.813502,0.610260,8.158905,5.044206,9.092245,-8.664072,8.768552,6.342346,-8.376288,0.574210,4.363618,8.020073,-4.026806,0.996885,-5.763732,-1.397039,6.639171,-1.165048], dtype = "float64")#candidate|7796|(150,)|const|float64
call_7795 = relay.TupleGetItem(func_4325_call(relay.reshape(const_7796.astype('float64'), [5, 15, 2])), 1)
call_7797 = relay.TupleGetItem(func_4328_call(relay.reshape(const_7796.astype('float64'), [5, 15, 2])), 1)
output = relay.Tuple([call_7773,call_7777,call_7782,var_7783,call_7792,const_7793,call_7795,const_7796,])
output2 = relay.Tuple([call_7774,call_7778,call_7784,var_7783,call_7794,const_7793,call_7797,const_7796,])
func_7802 = relay.Function([var_7783,], output)
mod['func_7802'] = func_7802
mod = relay.transform.InferType()(mod)
var_7803 = relay.var("var_7803", dtype = "float32", shape = (72,))#candidate|7803|(72,)|var|float32
output = func_7802(var_7803)
func_7804 = relay.Function([var_7803], output)
mutated_mod['func_7804'] = func_7804
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7819 = relay.var("var_7819", dtype = "float64", shape = (2, 16, 16))#candidate|7819|(2, 16, 16)|var|float64
uop_7820 = relay.asinh(var_7819.astype('float64')) # shape=(2, 16, 16)
bop_7824 = relay.greater_equal(uop_7820.astype('bool'), relay.reshape(var_7819.astype('bool'), relay.shape_of(uop_7820))) # shape=(2, 16, 16)
output = bop_7824
output2 = bop_7824
F = relay.Function([var_7819,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7819,], output2)
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
