import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_174 = relay.var("var_174", dtype = "int8", shape = (7, 9, 9))#candidate|174|(7, 9, 9)|var|int8
const_175 = relay.const([[[8,4,5,-1,-8,-8,-7,6,10],[5,-2,4,1,1,2,1,-3,7],[-1,-10,3,-1,-4,10,3,-7,10],[-10,1,-2,3,6,6,-5,-2,-5],[-4,7,3,1,3,-1,-7,-6,2],[-5,1,2,-3,-6,3,-3,-8,-4],[-8,-1,3,3,-4,-2,7,3,7],[5,4,8,-3,-4,-9,-5,5,7],[-7,10,1,8,-7,6,-6,-5,-4]],[[-10,4,-1,-4,10,-10,9,-1,-9],[-1,10,7,4,-1,-6,2,4,-9],[8,1,5,7,1,3,10,-6,-1],[-10,-8,2,8,9,-1,-6,2,-7],[9,10,-3,9,-4,8,9,8,9],[-3,-5,8,1,-5,3,9,-7,1],[10,5,-6,9,1,5,9,-8,10],[-2,-3,-3,10,-8,1,-9,9,6],[9,3,5,1,-7,10,-8,-8,9]],[[5,3,6,-3,6,-1,7,8,-1],[7,-6,-2,4,9,8,3,-7,9],[2,-10,-1,-1,-2,-10,3,-6,4],[5,7,9,-2,-1,1,-4,-9,5],[9,10,-6,-6,-10,8,-8,9,7],[-3,2,-9,3,10,-2,-3,1,-2],[-6,6,1,-7,8,-6,-7,5,-10],[-2,10,4,7,2,-3,-4,5,4],[-5,6,-10,-2,9,4,-4,4,-10]],[[-7,-8,-4,-5,9,-10,7,3,-3],[-6,-9,2,6,-10,1,3,-9,-9],[1,3,6,-4,-3,6,1,10,-7],[-1,-10,7,3,1,10,-6,4,2],[5,2,-2,-3,-10,-1,5,2,-5],[7,9,-1,-8,8,6,-3,-6,8],[-5,9,2,-4,3,2,-5,5,7],[-10,5,-6,-10,2,3,-3,1,-4],[3,-1,4,-4,2,-4,7,5,-4]],[[3,-9,-1,6,-3,-8,-1,-6,7],[4,10,3,9,8,4,-5,7,5],[-8,-1,-10,-9,10,-1,-7,10,-3],[3,-5,-5,4,-5,6,10,10,7],[10,9,3,-7,-7,8,-10,-3,4],[1,10,1,-7,-9,2,-7,4,-10],[-9,5,-6,7,6,8,-8,7,8],[-3,7,-1,8,9,7,-6,8,10],[6,9,-9,-9,-9,-4,-4,-1,-9]],[[-10,-2,10,2,-6,9,6,5,-7],[-4,1,5,-10,2,-10,6,9,-10],[-9,-7,5,-3,1,-4,-10,7,2],[7,-10,7,-2,-1,3,2,-6,-9],[4,9,9,6,-4,9,6,1,-6],[8,-1,1,-2,8,-3,-8,10,-4],[3,-8,-4,6,-4,-6,5,-8,-4],[-10,1,4,-8,1,-2,-9,-7,-3],[-4,1,-5,-10,-2,7,-9,-2,-7]],[[-4,-1,-5,2,-7,8,9,8,-4],[6,3,4,2,7,2,2,-8,-5],[-5,4,-5,3,-8,6,6,-6,10],[9,1,-7,9,-1,2,2,2,-9],[-10,-2,3,-10,10,8,-6,-3,4],[-2,-9,1,-10,1,9,-10,2,7],[2,4,3,-3,8,6,7,-4,2],[10,-8,-3,-10,-8,-8,10,2,5],[6,4,5,-8,9,-3,-1,10,-3]]], dtype = "int8")#candidate|175|(7, 9, 9)|const|int8
bop_176 = relay.left_shift(var_174.astype('int8'), relay.reshape(const_175.astype('int8'), relay.shape_of(var_174))) # shape=(7, 9, 9)
output = bop_176
output2 = bop_176
func_180 = relay.Function([var_174,], output)
mod['func_180'] = func_180
mod = relay.transform.InferType()(mod)
var_181 = relay.var("var_181", dtype = "int8", shape = (7, 9, 9))#candidate|181|(7, 9, 9)|var|int8
output = func_180(var_181)
func_182 = relay.Function([var_181], output)
mutated_mod['func_182'] = func_182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_759 = relay.var("var_759", dtype = "uint8", shape = ())#candidate|759|()|var|uint8
var_760 = relay.var("var_760", dtype = "uint8", shape = (7, 16, 6))#candidate|760|(7, 16, 6)|var|uint8
bop_761 = relay.logical_xor(var_759.astype('uint8'), var_760.astype('uint8')) # shape=(7, 16, 6)
output = bop_761
output2 = bop_761
func_765 = relay.Function([var_759,var_760,], output)
mod['func_765'] = func_765
mod = relay.transform.InferType()(mod)
mutated_mod['func_765'] = func_765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_765_call = mutated_mod.get_global_var('func_765')
var_767 = relay.var("var_767", dtype = "uint8", shape = ())#candidate|767|()|var|uint8
var_768 = relay.var("var_768", dtype = "uint8", shape = (7, 16, 6))#candidate|768|(7, 16, 6)|var|uint8
call_766 = func_765_call(var_767,var_768,)
output = call_766
func_769 = relay.Function([var_767,var_768,], output)
mutated_mod['func_769'] = func_769
mutated_mod = relay.transform.InferType()(mutated_mod)
var_892 = relay.var("var_892", dtype = "int16", shape = (13, 15, 5))#candidate|892|(13, 15, 5)|var|int16
var_893 = relay.var("var_893", dtype = "int16", shape = (13, 15, 5))#candidate|893|(13, 15, 5)|var|int16
bop_894 = relay.bitwise_or(var_892.astype('int16'), relay.reshape(var_893.astype('int16'), relay.shape_of(var_892))) # shape=(13, 15, 5)
output = relay.Tuple([bop_894,])
output2 = relay.Tuple([bop_894,])
func_900 = relay.Function([var_892,var_893,], output)
mod['func_900'] = func_900
mod = relay.transform.InferType()(mod)
var_901 = relay.var("var_901", dtype = "int16", shape = (13, 15, 5))#candidate|901|(13, 15, 5)|var|int16
var_902 = relay.var("var_902", dtype = "int16", shape = (13, 15, 5))#candidate|902|(13, 15, 5)|var|int16
output = func_900(var_901,var_902,)
func_903 = relay.Function([var_901,var_902,], output)
mutated_mod['func_903'] = func_903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1193 = relay.var("var_1193", dtype = "bool", shape = (1, 11, 13))#candidate|1193|(1, 11, 13)|var|bool
var_1194 = relay.var("var_1194", dtype = "bool", shape = (15, 11, 13))#candidate|1194|(15, 11, 13)|var|bool
bop_1195 = relay.logical_or(var_1193.astype('bool'), var_1194.astype('bool')) # shape=(15, 11, 13)
output = relay.Tuple([bop_1195,])
output2 = relay.Tuple([bop_1195,])
func_1204 = relay.Function([var_1193,var_1194,], output)
mod['func_1204'] = func_1204
mod = relay.transform.InferType()(mod)
var_1205 = relay.var("var_1205", dtype = "bool", shape = (1, 11, 13))#candidate|1205|(1, 11, 13)|var|bool
var_1206 = relay.var("var_1206", dtype = "bool", shape = (15, 11, 13))#candidate|1206|(15, 11, 13)|var|bool
output = func_1204(var_1205,var_1206,)
func_1207 = relay.Function([var_1205,var_1206,], output)
mutated_mod['func_1207'] = func_1207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1308 = relay.var("var_1308", dtype = "uint16", shape = (8, 14, 4))#candidate|1308|(8, 14, 4)|var|uint16
const_1309 = relay.const([[[-7,-9,-3,7],[-6,3,-4,4],[-6,4,7,1],[10,6,4,-9],[-6,5,-5,1],[3,9,2,-7],[4,-6,-3,-4],[4,2,-7,8],[9,-7,6,-6],[-1,6,6,4],[5,1,-6,-10],[7,8,-4,9],[8,6,3,-2],[-4,-10,2,-2]],[[-3,-6,8,-1],[9,-10,6,4],[7,-7,-1,7],[-9,-8,10,-1],[-3,-5,-4,-7],[-6,6,10,7],[2,-10,-4,10],[3,-6,6,-7],[4,-1,10,1],[-6,-9,9,-4],[9,5,8,-9],[-3,-3,4,-9],[3,7,7,1],[-5,10,4,6]],[[-7,-9,8,7],[4,-2,1,5],[1,-9,-9,10],[1,-1,-3,10],[-10,4,-6,-1],[10,-7,7,6],[5,6,6,-10],[-5,1,8,7],[-10,-9,-9,-7],[6,-1,7,10],[-3,-5,-2,5],[6,5,-5,5],[3,-2,-4,5],[-2,-4,-4,-10]],[[-1,-7,4,2],[5,-5,2,-8],[1,9,-8,7],[9,-10,4,-1],[8,9,9,9],[9,-8,3,-5],[-5,-2,-9,4],[10,2,-3,10],[2,-1,-1,8],[-8,2,-4,8],[1,4,-10,-7],[-2,4,-3,-7],[6,-7,2,-8],[4,2,6,9]],[[3,-7,-10,3],[3,-7,2,1],[-6,4,8,8],[1,-1,-3,4],[2,9,6,-5],[-9,-5,-8,8],[9,-2,5,8],[-2,-3,-1,-1],[6,6,3,-1],[2,3,2,-4],[5,-7,-5,-6],[-8,-2,-6,10],[4,-4,-5,-9],[-2,-9,-6,-7]],[[-6,-1,1,-8],[8,6,4,6],[3,-4,6,7],[6,2,8,2],[4,-5,-5,-4],[2,7,-7,3],[-4,8,10,9],[1,7,1,-5],[5,1,-2,2],[-4,-7,1,-9],[-7,-6,2,5],[7,5,3,6],[-10,9,2,4],[-2,7,3,10]],[[-2,-8,-2,-10],[-7,8,4,2],[-8,6,4,-6],[-2,-2,8,4],[-8,6,7,8],[2,-8,9,10],[2,-9,-5,3],[-9,-10,-6,-9],[-9,2,-3,-4],[8,1,1,-9],[7,-1,5,10],[8,-5,8,-7],[-10,-7,-3,8],[-2,-1,10,7]],[[-9,2,2,-10],[-5,5,8,10],[-4,1,-7,-1],[9,3,-3,9],[-1,-6,6,-3],[8,4,-3,3],[1,-5,4,9],[-9,5,5,3],[-8,8,2,4],[-1,-5,-3,2],[-6,-4,4,-6],[-6,-4,-6,8],[4,7,-7,-8],[-7,3,-5,4]]], dtype = "uint16")#candidate|1309|(8, 14, 4)|const|uint16
bop_1310 = relay.subtract(var_1308.astype('uint16'), relay.reshape(const_1309.astype('uint16'), relay.shape_of(var_1308))) # shape=(8, 14, 4)
output = bop_1310
output2 = bop_1310
func_1320 = relay.Function([var_1308,], output)
mod['func_1320'] = func_1320
mod = relay.transform.InferType()(mod)
mutated_mod['func_1320'] = func_1320
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1321 = relay.var("var_1321", dtype = "uint16", shape = (8, 14, 4))#candidate|1321|(8, 14, 4)|var|uint16
func_1320_call = mutated_mod.get_global_var('func_1320')
call_1322 = func_1320_call(var_1321)
output = call_1322
func_1323 = relay.Function([var_1321], output)
mutated_mod['func_1323'] = func_1323
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1621 = relay.const(3, dtype = "uint16")#candidate|1621|()|const|uint16
var_1622 = relay.var("var_1622", dtype = "uint16", shape = (1, 4, 6))#candidate|1622|(1, 4, 6)|var|uint16
bop_1623 = relay.minimum(const_1621.astype('uint16'), var_1622.astype('uint16')) # shape=(1, 4, 6)
bop_1637 = relay.multiply(var_1622.astype('uint64'), const_1621.astype('uint64')) # shape=(1, 4, 6)
func_1204_call = mod.get_global_var('func_1204')
func_1207_call = mutated_mod.get_global_var('func_1207')
const_1641 = relay.const([False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False], dtype = "bool")#candidate|1641|(143,)|const|bool
var_1642 = relay.var("var_1642", dtype = "bool", shape = (2145,))#candidate|1642|(2145,)|var|bool
call_1640 = relay.TupleGetItem(func_1204_call(relay.reshape(const_1641.astype('bool'), [1, 11, 13]), relay.reshape(var_1642.astype('bool'), [15, 11, 13]), ), 0)
call_1643 = relay.TupleGetItem(func_1207_call(relay.reshape(const_1641.astype('bool'), [1, 11, 13]), relay.reshape(var_1642.astype('bool'), [15, 11, 13]), ), 0)
func_1320_call = mod.get_global_var('func_1320')
func_1323_call = mutated_mod.get_global_var('func_1323')
var_1646 = relay.var("var_1646", dtype = "uint16", shape = (448,))#candidate|1646|(448,)|var|uint16
call_1645 = func_1320_call(relay.reshape(var_1646.astype('uint16'), [8, 14, 4]))
call_1647 = func_1320_call(relay.reshape(var_1646.astype('uint16'), [8, 14, 4]))
bop_1648 = relay.logical_xor(bop_1637.astype('uint32'), const_1621.astype('uint32')) # shape=(1, 4, 6)
bop_1653 = relay.add(bop_1623.astype('int64'), relay.reshape(var_1622.astype('int64'), relay.shape_of(bop_1623))) # shape=(1, 4, 6)
output = relay.Tuple([call_1640,const_1641,var_1642,call_1645,var_1646,bop_1648,bop_1653,])
output2 = relay.Tuple([call_1643,const_1641,var_1642,call_1647,var_1646,bop_1648,bop_1653,])
func_1659 = relay.Function([var_1622,var_1642,var_1646,], output)
mod['func_1659'] = func_1659
mod = relay.transform.InferType()(mod)
mutated_mod['func_1659'] = func_1659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1659_call = mutated_mod.get_global_var('func_1659')
var_1661 = relay.var("var_1661", dtype = "uint16", shape = (1, 4, 6))#candidate|1661|(1, 4, 6)|var|uint16
var_1662 = relay.var("var_1662", dtype = "bool", shape = (2145,))#candidate|1662|(2145,)|var|bool
var_1663 = relay.var("var_1663", dtype = "uint16", shape = (448,))#candidate|1663|(448,)|var|uint16
call_1660 = func_1659_call(var_1661,var_1662,var_1663,)
output = call_1660
func_1664 = relay.Function([var_1661,var_1662,var_1663,], output)
mutated_mod['func_1664'] = func_1664
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1754 = relay.const([[[-1.994035,-2.420118,0.302135,7.499683,0.100341,6.605424,-8.054984,7.808335,-9.775691,-8.493171,-0.233421,6.946776,5.005181],[-3.992208,7.637292,-5.647324,5.357795,8.522849,0.720941,-9.506968,-7.300641,-5.114493,-4.466162,5.746916,-1.226467,-2.172959],[-0.021810,-8.637799,-1.182114,-2.254206,-9.643295,0.898503,3.743943,-5.284140,9.003323,2.902036,2.609490,6.010901,8.199790],[-5.769919,-8.802972,7.831476,9.065245,-8.597204,-0.413874,6.990868,6.212234,-1.822670,7.564134,-3.884746,8.133671,7.485106],[7.482365,1.547956,8.544073,-7.955835,-0.936907,-9.301663,-8.352130,-6.087417,7.561491,8.057005,-7.914299,9.356656,2.506701]],[[0.091045,1.411629,9.094573,8.758024,6.329238,-2.594380,-4.991747,5.119078,-5.079740,-6.675599,2.436457,-8.348480,-9.839827],[-7.589906,0.826981,5.994955,9.864319,2.907689,-7.390262,0.775563,4.909643,6.498515,-0.704848,-3.631020,-2.052547,0.003503],[-8.783778,6.593476,8.679679,-2.870021,5.459267,9.882504,-4.322965,9.641471,9.887447,-0.326097,-3.442000,-3.892432,1.402422],[-6.201539,5.609616,5.869423,3.175788,6.593142,-1.933008,7.769386,3.886403,-3.612616,6.437451,-1.423922,-3.441061,9.529713],[3.781652,-5.002472,-3.066159,-9.810277,-8.750274,2.954952,-4.957633,-1.304622,-0.815387,-9.685948,-3.121155,2.546498,-2.032126]],[[-1.283776,0.769177,-6.377423,-8.340524,8.987112,6.298842,-6.884134,7.881268,4.600583,-7.265257,-1.753583,-5.799775,9.767609],[-4.288281,-3.044505,-0.940732,1.896825,0.841359,-3.462837,-1.395815,-7.376843,-4.444450,-8.457893,6.442805,8.936154,2.754195],[-2.703047,3.970527,6.738490,7.692088,-3.988198,-3.193503,4.251029,0.496773,6.545521,7.346462,9.349548,6.673463,5.498286],[-5.350164,-5.663178,-0.285009,7.214049,-4.558197,7.234648,-6.703628,-2.135758,-5.565596,-4.395529,2.520489,7.282024,-0.543180],[-3.366722,-9.424907,-1.529415,8.864480,8.720865,3.516264,7.710224,5.115019,3.958764,-6.979335,-9.436837,1.701207,5.510273]],[[4.884568,1.927033,4.334401,9.979375,9.950013,-6.256615,-9.981459,2.926287,-0.571390,-5.895504,0.582981,-0.679992,1.990554],[-6.168435,9.096074,9.440910,3.582905,-9.214512,7.221907,-2.814400,5.067045,3.376235,-7.005127,-7.059071,7.930344,-8.469634],[-5.643235,-9.292082,-3.859231,2.676947,-5.390155,-7.155624,0.764650,7.668936,-6.597013,-1.678917,-2.293996,5.223019,-3.201425],[-4.632744,-7.807763,-5.230928,6.637738,-2.175603,-2.229707,3.873621,7.516367,-3.119642,7.120830,5.195800,4.354357,0.325707],[1.702748,5.389972,-6.821585,7.334000,-0.286395,-7.951031,-3.172260,1.746322,-7.942735,-9.053160,-7.874650,-6.947547,-3.168626]],[[5.193792,5.245994,7.933659,-8.628090,-2.674570,-1.633689,0.722765,-5.014585,-6.226937,2.435107,7.316172,4.715343,0.857373],[-0.165344,0.549023,7.097270,-8.539531,4.597322,3.386726,-6.146012,7.421035,1.049791,-7.536738,-8.861859,-6.709608,-6.705621],[7.741794,9.027259,-4.830605,-5.484871,-9.410820,-2.135401,0.934849,4.394179,0.385370,-1.367300,-5.748469,-0.009971,6.137378],[-4.242910,-3.297736,9.387715,-6.125296,-0.058841,-3.889282,-4.067088,-1.897160,-8.016806,-6.012105,-5.402726,2.377612,-3.552927],[-6.360360,-0.810492,9.234629,8.942189,-2.598244,9.393397,-3.769657,6.338198,9.914132,1.790655,-3.746248,9.608303,0.852457]]], dtype = "float64")#candidate|1754|(5, 5, 13)|const|float64
uop_1755 = relay.rsqrt(const_1754.astype('float64')) # shape=(5, 5, 13)
output = uop_1755
output2 = uop_1755
func_1758 = relay.Function([], output)
mod['func_1758'] = func_1758
mod = relay.transform.InferType()(mod)
mutated_mod['func_1758'] = func_1758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mutated_mod.get_global_var('func_1758')
call_1759 = func_1758_call()
output = call_1759
func_1760 = relay.Function([], output)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1774 = func_1758_call()
call_1775 = func_1758_call()
func_765_call = mod.get_global_var('func_765')
func_769_call = mutated_mod.get_global_var('func_769')
var_1780 = relay.var("var_1780", dtype = "uint8", shape = ())#candidate|1780|()|var|uint8
const_1781 = relay.const([-9,-2,8,-2,7,7,-4,-4,9,-6,-9,-5,-3,1,1,-3,2,-1,-9,5,1,-5,10,-4,3,5,-10,-5,1,1,1,6,-1,8,-10,-6,-6,-5,-2,-3,-2,-1,1,3,1,7,2,-7,-10,3,-9,10,3,10,-8,-2,-3,1,8,-9,-10,1,10,4,-5,2,9,-9,-9,10,2,-6,-7,-1,2,4,-4,3,4,-6,4,3,1,-6,1,-6,7,7,10,9,-6,4,-7,-6,4,-10,-1,4,6,-10,5,9,-1,-8,-6,3,-9,4,1,6,3,4,2,-3,7,5,-1,-5,-3,-3,1,1,-10,5,6,-9,-1,2,-2,-2,-10,2,-3,4,-2,-7,3,-3,4,6,-3,-8,9,-8,4,-9,-8,6,8,1,8,-4,-7,-4,7,2,7,4,1,5,3,2,5,-5,9,-4,4,-8,5,2,3,1,4,-4,-9,-2,2,-4,-1,9,-4,7,-3,9,-8,-9,6,1,-7,-7,-5,-9,-1,6,-1,-10,-10,-3,3,-10,-4,1,10,10,-8,-6,-3,2,7,6,4,2,-4,-6,8,5,4,-2,10,6,6,-3,-6,-5,-4,2,6,2,1,-6,-2,1,-6,2,2,6,-9,-8,-3,-9,-3,-4,5,8,2,4,-4,-1,7,-8,1,-10,-2,-5,-1,-1,7,3,1,-9,5,8,10,2,5,8,-4,6,7,1,10,-2,9,-9,7,5,1,3,-7,9,-5,-7,3,6,-9,-8,1,3,7,4,10,-8,-5,2,-6,-3,8,-1,-5,1,-4,-4,10,8,-9,-1,-2,-2,10,8,-5,-8,-2,5,3,-3,6,-3,5,4,-4,5,-6,2,2,-3,-2,1,-7,3,-2,-9,4,-7,-5,-4,-7,-4,9,8,-9,-8,9,5,6,8,-6,8,-10,8,-7,-6,-5,-5,10,4,4,10,-3,-9,-3,-9,-5,9,-4,-5,-3,-3,-5,1,-2,3,-8,9,-8,-10,-7,-1,8,2,-1,10,7,-2,-2,8,-9,9,-5,-9,-9,7,-2,10,10,-1,-8,5,-6,10,10,-3,-10,-6,-1,8,-8,5,3,9,7,6,-10,-1,-10,4,8,8,-10,-10,1,-2,-5,8,-2,3,6,-7,4,3,-8,3,6,3,-6,-8,3,8,7,-7,-3,-2,-4,5,4,10,-9,-9,4,1,-5,9,-1,7,2,-8,-8,4,-7,8,1,5,-2,-4,-6,-6,-6,-10,-1,4,3,-8,2,1,-5,3,10,5,-4,-8,-4,1,3,-6,8,-8,1,10,-2,-3,3,-4,-5,4,-7,-10,-1,10,2,-6,5,-1,-4,8,-3,2,8,-8,-4,-4,7,2,7,-9,8,-1,-3,-9,-3,-2,9,-2,-1,-4,1,6,4,-5,3,-3,-1,-4,-7,1,2,-6,-9,-10,9,5,-3,-7,2,9,-7,-6,9,3,5,-5,9,-9,-2,-9,2,10,-9,-2,10,-6,-8,-5,4,-2,-6,-7,-10,3,5,10,10,-5,-6,9,2,5,10,6,10,3,7,-10,6,9,-7,-1,1,-5,-4,-5,2,6,-1,-5,10,-6,-10,4,-2,-9,3,8,-9,5,9,-10,1,10,8,-1,-5,-5,-5,-3,1,-8,6,-2,-8,6,6,-6,-2,7,4,-8,6,6,-10,10,10,10,3,1,-7,-7,-5,-10,-1,-8,-6,6,10,5,10,5,-5,-6,-7,8,-5,6,7,-8,-2,5,-5,-2,-2,6,4,2,6,-8,6,-6,-10,-3,-8,-7,-1,10], dtype = "uint8")#candidate|1781|(672,)|const|uint8
call_1779 = func_765_call(relay.reshape(var_1780.astype('uint8'), []), relay.reshape(const_1781.astype('uint8'), [7, 16, 6]), )
call_1782 = func_765_call(relay.reshape(var_1780.astype('uint8'), []), relay.reshape(const_1781.astype('uint8'), [7, 16, 6]), )
func_1320_call = mod.get_global_var('func_1320')
func_1323_call = mutated_mod.get_global_var('func_1323')
var_1788 = relay.var("var_1788", dtype = "uint16", shape = (448,))#candidate|1788|(448,)|var|uint16
call_1787 = func_1320_call(relay.reshape(var_1788.astype('uint16'), [8, 14, 4]))
call_1789 = func_1320_call(relay.reshape(var_1788.astype('uint16'), [8, 14, 4]))
func_1204_call = mod.get_global_var('func_1204')
func_1207_call = mutated_mod.get_global_var('func_1207')
var_1797 = relay.var("var_1797", dtype = "bool", shape = (13, 11))#candidate|1797|(13, 11)|var|bool
const_1798 = relay.const([True,False,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False], dtype = "bool")#candidate|1798|(2145,)|const|bool
call_1796 = relay.TupleGetItem(func_1204_call(relay.reshape(var_1797.astype('bool'), [1, 11, 13]), relay.reshape(const_1798.astype('bool'), [15, 11, 13]), ), 0)
call_1799 = relay.TupleGetItem(func_1207_call(relay.reshape(var_1797.astype('bool'), [1, 11, 13]), relay.reshape(const_1798.astype('bool'), [15, 11, 13]), ), 0)
output = relay.Tuple([call_1774,call_1779,var_1780,const_1781,call_1787,var_1788,call_1796,var_1797,const_1798,])
output2 = relay.Tuple([call_1775,call_1782,var_1780,const_1781,call_1789,var_1788,call_1799,var_1797,const_1798,])
func_1804 = relay.Function([var_1780,var_1788,var_1797,], output)
mod['func_1804'] = func_1804
mod = relay.transform.InferType()(mod)
mutated_mod['func_1804'] = func_1804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1804_call = mutated_mod.get_global_var('func_1804')
var_1806 = relay.var("var_1806", dtype = "uint8", shape = ())#candidate|1806|()|var|uint8
var_1807 = relay.var("var_1807", dtype = "uint16", shape = (448,))#candidate|1807|(448,)|var|uint16
var_1808 = relay.var("var_1808", dtype = "bool", shape = (13, 11))#candidate|1808|(13, 11)|var|bool
call_1805 = func_1804_call(var_1806,var_1807,var_1808,)
output = call_1805
func_1809 = relay.Function([var_1806,var_1807,var_1808,], output)
mutated_mod['func_1809'] = func_1809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1893 = func_1758_call()
call_1894 = func_1758_call()
func_1320_call = mod.get_global_var('func_1320')
func_1323_call = mutated_mod.get_global_var('func_1323')
var_1905 = relay.var("var_1905", dtype = "uint16", shape = (448,))#candidate|1905|(448,)|var|uint16
call_1904 = func_1320_call(relay.reshape(var_1905.astype('uint16'), [8, 14, 4]))
call_1906 = func_1320_call(relay.reshape(var_1905.astype('uint16'), [8, 14, 4]))
output = relay.Tuple([call_1893,call_1904,var_1905,])
output2 = relay.Tuple([call_1894,call_1906,var_1905,])
func_1917 = relay.Function([var_1905,], output)
mod['func_1917'] = func_1917
mod = relay.transform.InferType()(mod)
var_1918 = relay.var("var_1918", dtype = "uint16", shape = (448,))#candidate|1918|(448,)|var|uint16
output = func_1917(var_1918)
func_1919 = relay.Function([var_1918], output)
mutated_mod['func_1919'] = func_1919
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2033 = relay.var("var_2033", dtype = "float32", shape = (3, 16, 13))#candidate|2033|(3, 16, 13)|var|float32
var_2034 = relay.var("var_2034", dtype = "float32", shape = (3, 16, 13))#candidate|2034|(3, 16, 13)|var|float32
bop_2035 = relay.maximum(var_2033.astype('float32'), relay.reshape(var_2034.astype('float32'), relay.shape_of(var_2033))) # shape=(3, 16, 13)
output = relay.Tuple([bop_2035,])
output2 = relay.Tuple([bop_2035,])
func_2040 = relay.Function([var_2033,var_2034,], output)
mod['func_2040'] = func_2040
mod = relay.transform.InferType()(mod)
mutated_mod['func_2040'] = func_2040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2040_call = mutated_mod.get_global_var('func_2040')
var_2042 = relay.var("var_2042", dtype = "float32", shape = (3, 16, 13))#candidate|2042|(3, 16, 13)|var|float32
var_2043 = relay.var("var_2043", dtype = "float32", shape = (3, 16, 13))#candidate|2043|(3, 16, 13)|var|float32
call_2041 = func_2040_call(var_2042,var_2043,)
output = call_2041
func_2044 = relay.Function([var_2042,var_2043,], output)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2056 = func_1758_call()
call_2057 = func_1758_call()
output = relay.Tuple([call_2056,])
output2 = relay.Tuple([call_2057,])
func_2060 = relay.Function([], output)
mod['func_2060'] = func_2060
mod = relay.transform.InferType()(mod)
output = func_2060()
func_2061 = relay.Function([], output)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2068 = relay.var("var_2068", dtype = "uint64", shape = (8, 7, 8))#candidate|2068|(8, 7, 8)|var|uint64
var_2069 = relay.var("var_2069", dtype = "uint64", shape = (8, 7, 8))#candidate|2069|(8, 7, 8)|var|uint64
bop_2070 = relay.right_shift(var_2068.astype('uint64'), relay.reshape(var_2069.astype('uint64'), relay.shape_of(var_2068))) # shape=(8, 7, 8)
bop_2075 = relay.logical_and(var_2069.astype('bool'), relay.reshape(bop_2070.astype('bool'), relay.shape_of(var_2069))) # shape=(8, 7, 8)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_2084 = relay.TupleGetItem(func_1917_call(relay.reshape(bop_2075.astype('uint16'), [448,])), 0)
call_2085 = relay.TupleGetItem(func_1919_call(relay.reshape(bop_2075.astype('uint16'), [448,])), 0)
uop_2087 = relay.sqrt(var_2069.astype('float32')) # shape=(8, 7, 8)
uop_2093 = relay.atan(uop_2087.astype('float32')) # shape=(8, 7, 8)
func_1659_call = mod.get_global_var('func_1659')
func_1664_call = mutated_mod.get_global_var('func_1664')
const_2096 = relay.const([[8,-6],[7,6],[7,5],[8,-6],[10,7],[-5,-1],[10,-6],[-3,7],[6,-8],[1,6],[8,1],[-9,10]], dtype = "uint16")#candidate|2096|(12, 2)|const|uint16
var_2097 = relay.var("var_2097", dtype = "bool", shape = (2145,))#candidate|2097|(2145,)|var|bool
call_2095 = relay.TupleGetItem(func_1659_call(relay.reshape(const_2096.astype('uint16'), [1, 4, 6]), relay.reshape(var_2097.astype('bool'), [2145,]), relay.reshape(var_2068.astype('uint16'), [448,]), ), 4)
call_2098 = relay.TupleGetItem(func_1664_call(relay.reshape(const_2096.astype('uint16'), [1, 4, 6]), relay.reshape(var_2097.astype('bool'), [2145,]), relay.reshape(var_2068.astype('uint16'), [448,]), ), 4)
func_765_call = mod.get_global_var('func_765')
func_769_call = mutated_mod.get_global_var('func_769')
var_2116 = relay.var("var_2116", dtype = "uint8", shape = ())#candidate|2116|()|var|uint8
var_2117 = relay.var("var_2117", dtype = "uint8", shape = (672,))#candidate|2117|(672,)|var|uint8
call_2115 = func_765_call(relay.reshape(var_2116.astype('uint8'), []), relay.reshape(var_2117.astype('uint8'), [7, 16, 6]), )
call_2118 = func_765_call(relay.reshape(var_2116.astype('uint8'), []), relay.reshape(var_2117.astype('uint8'), [7, 16, 6]), )
bop_2122 = relay.maximum(uop_2093.astype('int8'), relay.reshape(bop_2070.astype('int8'), relay.shape_of(uop_2093))) # shape=(8, 7, 8)
bop_2125 = relay.floor_divide(bop_2122.astype('float32'), relay.reshape(uop_2087.astype('float32'), relay.shape_of(bop_2122))) # shape=(8, 7, 8)
output = relay.Tuple([bop_2075,call_2084,call_2095,const_2096,var_2097,call_2115,var_2116,var_2117,bop_2125,])
output2 = relay.Tuple([bop_2075,call_2085,call_2098,const_2096,var_2097,call_2118,var_2116,var_2117,bop_2125,])
func_2130 = relay.Function([var_2068,var_2069,var_2097,var_2116,var_2117,], output)
mod['func_2130'] = func_2130
mod = relay.transform.InferType()(mod)
var_2131 = relay.var("var_2131", dtype = "uint64", shape = (8, 7, 8))#candidate|2131|(8, 7, 8)|var|uint64
var_2132 = relay.var("var_2132", dtype = "uint64", shape = (8, 7, 8))#candidate|2132|(8, 7, 8)|var|uint64
var_2133 = relay.var("var_2133", dtype = "bool", shape = (2145,))#candidate|2133|(2145,)|var|bool
var_2134 = relay.var("var_2134", dtype = "uint8", shape = ())#candidate|2134|()|var|uint8
var_2135 = relay.var("var_2135", dtype = "uint8", shape = (672,))#candidate|2135|(672,)|var|uint8
output = func_2130(var_2131,var_2132,var_2133,var_2134,var_2135,)
func_2136 = relay.Function([var_2131,var_2132,var_2133,var_2134,var_2135,], output)
mutated_mod['func_2136'] = func_2136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2161 = relay.var("var_2161", dtype = "int16", shape = (14, 12, 4))#candidate|2161|(14, 12, 4)|var|int16
const_2162 = relay.const([[[9,3,9,7],[-3,2,-8,-3],[8,8,4,-3],[5,-3,4,-8],[-9,8,-3,4],[7,6,-8,6],[2,7,-4,-2],[-8,10,7,6],[7,6,9,7],[-5,1,2,9],[-3,-8,7,-6],[7,8,1,1]],[[-7,9,-6,4],[-9,-5,2,5],[-8,-2,4,-1],[-3,-6,10,4],[4,-3,-10,-2],[-2,2,-10,-1],[3,-3,-1,-10],[1,1,-3,1],[8,6,3,-9],[-6,10,9,4],[5,8,4,-4],[-6,-8,-10,4]],[[5,6,-1,-2],[5,3,-5,5],[-6,8,3,-5],[-7,-7,2,-4],[3,-4,2,-9],[9,-10,-1,-4],[10,-7,4,-3],[4,7,-1,-4],[9,-9,5,-8],[2,-1,-5,-1],[7,-7,9,3],[9,-3,8,-7]],[[7,-10,5,-9],[7,1,-2,-6],[-10,1,2,5],[3,4,-5,-10],[8,-5,9,-10],[-1,-10,-3,6],[-9,3,1,5],[-5,-5,1,-3],[7,-1,-1,3],[-10,-8,7,-6],[-1,10,-4,5],[-7,10,-8,-8]],[[-10,-1,8,6],[7,2,-6,-2],[5,10,-8,-9],[-7,-4,1,-10],[-1,-5,-5,8],[4,5,10,8],[9,7,3,4],[-6,-5,-10,-9],[5,9,-4,1],[-9,-8,4,-4],[-2,-2,-6,4],[-5,-8,-3,-4]],[[-2,8,2,-4],[6,1,5,-2],[-6,-3,1,6],[-4,10,3,6],[9,-1,-5,-3],[6,8,-9,10],[5,10,1,-1],[-10,4,5,1],[6,-6,-9,-10],[4,8,-10,-1],[-4,-2,-6,-1],[4,-2,-7,-4]],[[8,-4,10,4],[3,7,2,10],[-8,-2,3,-1],[-3,7,-9,-3],[-10,4,10,-4],[-1,8,-1,-9],[9,3,9,1],[8,-1,7,-4],[10,9,-7,5],[-5,1,-9,3],[4,-2,-10,4],[-10,-7,-9,-6]],[[-2,-9,7,8],[6,6,-2,7],[-4,8,1,6],[-6,-10,7,-4],[-10,-9,-8,9],[-8,1,-3,-5],[-9,-3,-6,-4],[3,7,-10,8],[-3,-9,3,7],[2,-1,-8,1],[9,8,4,-8],[-5,-4,6,-7]],[[8,2,-3,-5],[6,-9,2,2],[6,7,-1,7],[-1,-3,5,-8],[5,4,-8,2],[-5,-2,10,8],[-3,8,-1,-10],[-7,7,-2,-5],[-6,6,10,-10],[10,1,6,-8],[4,5,-10,-8],[-7,-1,2,7]],[[-6,4,10,10],[7,-1,-1,-4],[-4,2,1,3],[7,-8,-1,-6],[5,-1,-5,-6],[-2,-5,-6,10],[5,6,-4,-5],[-4,-9,-7,9],[7,8,3,-2],[3,-8,4,8],[1,-7,-4,5],[5,-2,1,4]],[[-5,7,8,-1],[-7,-9,8,-2],[1,6,-4,-5],[5,1,1,3],[10,4,-1,1],[5,-1,-7,-5],[-4,6,-2,-9],[8,-4,-7,-7],[-8,9,7,9],[9,-6,-7,-5],[-2,1,1,2],[9,-10,-4,7]],[[7,3,-5,-5],[-4,-9,4,2],[-6,-1,-2,-6],[-8,7,-3,-3],[-10,6,9,-10],[-4,4,4,5],[10,6,-8,10],[9,7,-4,6],[-9,9,-4,2],[7,-6,-3,-10],[-7,-2,-1,1],[2,3,2,-1]],[[-2,10,-9,-3],[-8,9,2,-4],[-8,-5,1,-10],[-6,2,-2,9],[-1,-9,-1,9],[3,-9,-9,-5],[-1,5,-6,8],[8,10,-1,6],[-9,-4,-1,-8],[-1,1,-1,-7],[7,-8,-7,-5],[-4,-6,7,9]],[[-1,6,6,-6],[2,6,-6,-10],[5,5,2,-8],[8,-5,10,-1],[-9,-2,-1,-3],[-8,10,2,-6],[-6,10,3,-8],[1,-6,-7,1],[5,2,-2,1],[-6,3,-1,-6],[9,6,-3,3],[-8,-7,7,5]]], dtype = "int16")#candidate|2162|(14, 12, 4)|const|int16
bop_2163 = relay.greater(var_2161.astype('bool'), relay.reshape(const_2162.astype('bool'), relay.shape_of(var_2161))) # shape=(14, 12, 4)
output = relay.Tuple([bop_2163,])
output2 = relay.Tuple([bop_2163,])
func_2176 = relay.Function([var_2161,], output)
mod['func_2176'] = func_2176
mod = relay.transform.InferType()(mod)
var_2177 = relay.var("var_2177", dtype = "int16", shape = (14, 12, 4))#candidate|2177|(14, 12, 4)|var|int16
output = func_2176(var_2177)
func_2178 = relay.Function([var_2177], output)
mutated_mod['func_2178'] = func_2178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2060_call = mod.get_global_var('func_2060')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2194 = relay.TupleGetItem(func_2060_call(), 0)
call_2195 = relay.TupleGetItem(func_2061_call(), 0)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
var_2216 = relay.var("var_2216", dtype = "uint16", shape = (448,))#candidate|2216|(448,)|var|uint16
call_2215 = relay.TupleGetItem(func_1917_call(relay.reshape(var_2216.astype('uint16'), [448,])), 1)
call_2217 = relay.TupleGetItem(func_1919_call(relay.reshape(var_2216.astype('uint16'), [448,])), 1)
output = relay.Tuple([call_2194,call_2215,var_2216,])
output2 = relay.Tuple([call_2195,call_2217,var_2216,])
func_2225 = relay.Function([var_2216,], output)
mod['func_2225'] = func_2225
mod = relay.transform.InferType()(mod)
mutated_mod['func_2225'] = func_2225
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2226 = relay.var("var_2226", dtype = "uint16", shape = (448,))#candidate|2226|(448,)|var|uint16
func_2225_call = mutated_mod.get_global_var('func_2225')
call_2227 = func_2225_call(var_2226)
output = call_2227
func_2228 = relay.Function([var_2226], output)
mutated_mod['func_2228'] = func_2228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2431 = func_1758_call()
call_2432 = func_1758_call()
func_1659_call = mod.get_global_var('func_1659')
func_1664_call = mutated_mod.get_global_var('func_1664')
const_2439 = relay.const([-5,4,-1,1,2,-10,-6,-5,5,-9,1,2,1,-6,-2,3,9,3,2,-6,6,7,4,-5], dtype = "uint16")#candidate|2439|(24,)|const|uint16
const_2440 = relay.const([False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False], dtype = "bool")#candidate|2440|(2145,)|const|bool
const_2441 = relay.const([9,-3,-4,-9,-1,3,4,-6,-4,-10,-10,-1,4,-5,9,-8,-6,9,2,-8,3,-5,-3,-5,-6,7,5,4,-1,-2,-5,-1,3,-2,10,-10,-1,-9,5,-3,-1,8,10,5,3,4,-8,-10,6,8,1,-8,-4,-9,3,2,4,-9,-4,-8,4,6,8,4,7,10,1,-2,-7,4,5,-3,7,-5,-10,1,-8,5,2,-10,3,-9,-9,9,-4,-5,10,7,-4,2,7,6,-8,-1,-4,9,2,4,-9,-7,-10,3,4,9,4,2,3,-7,2,-1,-1,-6,8,-4,4,1,6,4,-4,8,4,-9,9,-8,-8,-7,-9,1,2,-6,9,-2,9,-4,9,-1,1,10,8,1,6,4,-1,-5,-2,-9,8,5,7,10,-3,-1,-3,-6,-10,6,7,3,6,-10,1,-9,-1,6,-8,-8,-7,5,1,-2,2,-6,7,6,-9,2,-8,-9,-9,-8,1,-8,-4,-2,-6,-5,10,7,3,3,-10,4,-9,-6,9,-7,-2,3,-8,3,7,4,9,9,5,-6,8,-4,4,-7,-5,-3,9,-5,1,3,-5,-7,8,-8,7,-9,-3,-4,-2,8,-5,-6,-9,3,6,7,-3,-8,2,8,-8,-6,2,8,1,3,8,-2,10,-8,1,8,2,7,-1,-3,1,-10,7,9,3,-6,1,2,3,-8,5,-8,-1,1,1,-1,-1,-7,8,-8,6,-5,-6,-8,5,5,1,9,10,6,-1,-4,-9,-3,-5,-1,9,-9,1,3,-5,-7,2,2,5,-3,-6,-1,8,-3,6,-7,8,-7,-5,-8,-9,-9,-3,2,9,-6,-4,10,-10,-8,-7,-1,-1,5,-1,8,-9,10,8,-2,9,1,-5,-7,4,-3,-8,-5,5,9,-4,-5,-6,7,-6,10,-6,-9,2,6,-1,6,-5,10,-10,5,6,6,-4,-5,-3,6,-3,-10,2,10,7,1,-4,4,-10,7,9,-7,10,3,-4,-3,-5,2,3,9,8,3,-2,6,-4,-9,10,-7,-7,-6,-9,-10,3,2,-5,-5,-4,5,-3,-10,-5,3,-7,10,9,5,-4,-6,6,-3,10,4,-4,2,9,8,2,-1,-10,-3,6,10,-2,7,4,-8,7,10,8,-1,-7,3,2,8,-7,-2,-8,5,1,-9,3,1,9,3,7,-6,-5,-4], dtype = "uint16")#candidate|2441|(448,)|const|uint16
call_2438 = relay.TupleGetItem(func_1659_call(relay.reshape(const_2439.astype('uint16'), [1, 4, 6]), relay.reshape(const_2440.astype('bool'), [2145,]), relay.reshape(const_2441.astype('uint16'), [448,]), ), 6)
call_2442 = relay.TupleGetItem(func_1664_call(relay.reshape(const_2439.astype('uint16'), [1, 4, 6]), relay.reshape(const_2440.astype('bool'), [2145,]), relay.reshape(const_2441.astype('uint16'), [448,]), ), 6)
bop_2483 = relay.mod(call_2438.astype('float32'), relay.reshape(const_2439.astype('float32'), relay.shape_of(call_2438))) # shape=(1, 4, 6)
bop_2486 = relay.mod(call_2442.astype('float32'), relay.reshape(const_2439.astype('float32'), relay.shape_of(call_2442))) # shape=(1, 4, 6)
output = relay.Tuple([call_2431,const_2440,const_2441,bop_2483,])
output2 = relay.Tuple([call_2432,const_2440,const_2441,bop_2486,])
func_2494 = relay.Function([], output)
mod['func_2494'] = func_2494
mod = relay.transform.InferType()(mod)
mutated_mod['func_2494'] = func_2494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mutated_mod.get_global_var('func_2494')
call_2495 = func_2494_call()
output = call_2495
func_2496 = relay.Function([], output)
mutated_mod['func_2496'] = func_2496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2533 = func_1758_call()
call_2534 = func_1758_call()
output = relay.Tuple([call_2533,])
output2 = relay.Tuple([call_2534,])
func_2535 = relay.Function([], output)
mod['func_2535'] = func_2535
mod = relay.transform.InferType()(mod)
mutated_mod['func_2535'] = func_2535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mutated_mod.get_global_var('func_2535')
call_2536 = func_2535_call()
output = call_2536
func_2537 = relay.Function([], output)
mutated_mod['func_2537'] = func_2537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2683 = func_1758_call()
call_2684 = func_1758_call()
func_2040_call = mod.get_global_var('func_2040')
func_2044_call = mutated_mod.get_global_var('func_2044')
var_2686 = relay.var("var_2686", dtype = "float32", shape = (2, 312))#candidate|2686|(2, 312)|var|float32
call_2685 = relay.TupleGetItem(func_2040_call(relay.reshape(var_2686.astype('float32'), [3, 16, 13]), relay.reshape(var_2686.astype('float32'), [3, 16, 13]), ), 0)
call_2687 = relay.TupleGetItem(func_2044_call(relay.reshape(var_2686.astype('float32'), [3, 16, 13]), relay.reshape(var_2686.astype('float32'), [3, 16, 13]), ), 0)
uop_2692 = relay.rsqrt(call_2685.astype('float64')) # shape=(3, 16, 13)
uop_2694 = relay.rsqrt(call_2687.astype('float64')) # shape=(3, 16, 13)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2702 = func_1758_call()
call_2703 = func_1758_call()
output = relay.Tuple([call_2683,var_2686,uop_2692,call_2702,])
output2 = relay.Tuple([call_2684,var_2686,uop_2694,call_2703,])
func_2727 = relay.Function([var_2686,], output)
mod['func_2727'] = func_2727
mod = relay.transform.InferType()(mod)
mutated_mod['func_2727'] = func_2727
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2728 = relay.var("var_2728", dtype = "float32", shape = (2, 312))#candidate|2728|(2, 312)|var|float32
func_2727_call = mutated_mod.get_global_var('func_2727')
call_2729 = func_2727_call(var_2728)
output = call_2729
func_2730 = relay.Function([var_2728], output)
mutated_mod['func_2730'] = func_2730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_2738 = relay.TupleGetItem(func_2494_call(), 0)
call_2739 = relay.TupleGetItem(func_2496_call(), 0)
output = relay.Tuple([call_2738,])
output2 = relay.Tuple([call_2739,])
func_2752 = relay.Function([], output)
mod['func_2752'] = func_2752
mod = relay.transform.InferType()(mod)
output = func_2752()
func_2753 = relay.Function([], output)
mutated_mod['func_2753'] = func_2753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2060_call = mod.get_global_var('func_2060')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2754 = relay.TupleGetItem(func_2060_call(), 0)
call_2755 = relay.TupleGetItem(func_2061_call(), 0)
output = relay.Tuple([call_2754,])
output2 = relay.Tuple([call_2755,])
func_2776 = relay.Function([], output)
mod['func_2776'] = func_2776
mod = relay.transform.InferType()(mod)
mutated_mod['func_2776'] = func_2776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2776_call = mutated_mod.get_global_var('func_2776')
call_2777 = func_2776_call()
output = call_2777
func_2778 = relay.Function([], output)
mutated_mod['func_2778'] = func_2778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2752_call = mod.get_global_var('func_2752')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_2798 = relay.TupleGetItem(func_2752_call(), 0)
call_2799 = relay.TupleGetItem(func_2753_call(), 0)
func_2130_call = mod.get_global_var('func_2130')
func_2136_call = mutated_mod.get_global_var('func_2136')
const_2801 = relay.const([6,-4,-6,-3,-4,-3,3,3,-10,1,5,9,6,3,7,-4,3,3,-6,-8,-7,3,-10,2,-9,5,-1,-5,4,-10,7,-6,-3,-2,7,-3,-9,-6,5,3,1,7,4,-10,10,-9,-5,7,-4,-8,7,7,8,-8,-1,6,-9,-5,-6,1,-6,-1,7,-10,-7,2,-10,3,-4,2,10,-7,-2,1,-7,4,-7,4,-4,-5,-3,-6,-7,4,8,7,3,-8,-6,2,3,7,-10,-4,-7,5,7,6,10,5,5,9,-6,2,-6,-7,2,-1,-9,9,3,8,9,3,-6,-9,-2,9,-5,-2,-9,2,-5,6,-7,9,-2,9,5,-1,2,-1,8,2,5,6,3,7,-2,-1,1,8,-1,5,1,-6,-5,9,9,1,-5,9,-5,-7,1,-6,10,-6,-3,6,4,-8,8,-6,-9,2,2,-4,-8,-5,-9,-3,-3,1,-7,-1,-6,4,6,-1,-7,-9,-4,7,5,3,1,4,-3,1,9,-3,-10,-1,6,-1,4,-1,4,10,-10,-3,9,8,-4,3,2,10,-2,-8,2,-1,-1,7,-2,7,2,-6,9,4,-4,7,-3,-8,8,5,-7,-10,-1,-6,-4,9,-2,8,9,-5,6,-7,-10,6,-2,2,7,8,7,-3,6,8,6,-1,7,-8,-1,4,1,-1,-8,2,3,5,3,-2,1,1,7,4,10,-6,8,-2,7,2,6,-3,4,-10,8,-10,-3,6,-2,1,2,-5,-7,-9,-2,-10,-7,-7,2,9,-1,-7,-7,4,5,5,5,8,-7,-8,8,-7,-2,-5,4,-2,-3,9,6,-1,-1,8,6,-1,3,-2,-7,7,3,-2,5,2,-7,-10,-6,-3,7,6,5,6,5,10,-9,1,-8,9,-1,3,-1,10,-4,-6,-2,6,-8,-7,10,-6,4,-1,2,-8,-2,-10,6,10,-1,-2,-9,-2,1,-9,-1,-2,-2,-9,-4,7,2,8,-5,7,-5,1,-7,2,-6,-1,-5,2,-5,-4,-10,4,10,9,10,-3,6,10,9,-1,2,4,4,-9,-8,9,-5,9,5,-3,5,10,10,-5,4,7,-10,5,4,-7,6,10,9,9,1,-8,7,-8,-10,7,-10,9,-5,8,-6,-4,10,-8,-5,-2,-8,-3,-8,2,-3,-1,-5,-5,-5,-10,7,-5,-9,-6], dtype = "uint64")#candidate|2801|(448,)|const|uint64
const_2802 = relay.const([True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False], dtype = "bool")#candidate|2802|(2145,)|const|bool
var_2803 = relay.var("var_2803", dtype = "uint8", shape = ())#candidate|2803|()|var|uint8
var_2804 = relay.var("var_2804", dtype = "uint8", shape = (672,))#candidate|2804|(672,)|var|uint8
call_2800 = relay.TupleGetItem(func_2130_call(relay.reshape(const_2801.astype('uint64'), [8, 7, 8]), relay.reshape(const_2801.astype('uint64'), [8, 7, 8]), relay.reshape(const_2802.astype('bool'), [2145,]), relay.reshape(var_2803.astype('uint8'), []), relay.reshape(var_2804.astype('uint8'), [672,]), ), 5)
call_2805 = relay.TupleGetItem(func_2136_call(relay.reshape(const_2801.astype('uint64'), [8, 7, 8]), relay.reshape(const_2801.astype('uint64'), [8, 7, 8]), relay.reshape(const_2802.astype('bool'), [2145,]), relay.reshape(var_2803.astype('uint8'), []), relay.reshape(var_2804.astype('uint8'), [672,]), ), 5)
output = relay.Tuple([call_2798,call_2800,const_2801,const_2802,var_2803,var_2804,])
output2 = relay.Tuple([call_2799,call_2805,const_2801,const_2802,var_2803,var_2804,])
func_2808 = relay.Function([var_2803,var_2804,], output)
mod['func_2808'] = func_2808
mod = relay.transform.InferType()(mod)
var_2809 = relay.var("var_2809", dtype = "uint8", shape = ())#candidate|2809|()|var|uint8
var_2810 = relay.var("var_2810", dtype = "uint8", shape = (672,))#candidate|2810|(672,)|var|uint8
output = func_2808(var_2809,var_2810,)
func_2811 = relay.Function([var_2809,var_2810,], output)
mutated_mod['func_2811'] = func_2811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2825 = relay.var("var_2825", dtype = "float32", shape = ())#candidate|2825|()|var|float32
const_2826 = relay.const([[[7.101633,5.640223,1.824806,-5.380842,-2.717561,7.749349]],[[1.616885,8.808169,7.798424,8.389812,-8.413948,4.159736]],[[-4.912130,-7.081198,-8.438958,9.244453,-0.507565,9.790994]],[[-9.555964,-3.546740,9.495836,0.896404,-1.436002,-7.683116]],[[8.310605,6.962438,-4.830649,7.990331,3.329530,1.221140]],[[-1.012148,-7.748155,-3.050665,-3.257014,0.868638,7.701054]],[[-3.438215,5.758269,6.142730,5.147114,-3.118096,7.631192]],[[9.027839,4.575506,-2.374442,-5.009383,9.149207,-4.225895]],[[7.892027,-2.537751,4.248676,6.375607,-8.789710,-9.413498]],[[9.257978,-4.991652,0.580330,-3.056615,-8.523153,7.978973]],[[-6.930563,8.113526,-7.757099,1.510270,-5.871680,7.457084]]], dtype = "float32")#candidate|2826|(11, 1, 6)|const|float32
bop_2827 = relay.subtract(var_2825.astype('float32'), const_2826.astype('float32')) # shape=(11, 1, 6)
var_2831 = relay.var("var_2831", dtype = "float32", shape = (11, 3, 6))#candidate|2831|(11, 3, 6)|var|float32
bop_2832 = relay.power(bop_2827.astype('float32'), var_2831.astype('float32')) # shape=(11, 3, 6)
bop_2837 = relay.logical_or(bop_2827.astype('bool'), var_2831.astype('bool')) # shape=(11, 3, 6)
func_765_call = mod.get_global_var('func_765')
func_769_call = mutated_mod.get_global_var('func_769')
const_2847 = relay.const([1,4,9,-8,-2,-4,2,7,6,1,8,-10,10,-7,1,2,2,-10,7,-9,-4,6,-5,-3,2,6,1,8,-7,6,7,-2,1,-3,1,5,-4,-3,-7,-9,-10,9,-2,5,-4,-1,-6,-3,4,5,-7,-3,5,-10,-2,-1,6,6,-9,-9,-9,-3,3,1,-3,5,9,10,3,6,1,-8,7,8,4,-6,-8,-7,6,-10,-8,-8,-2,1,-10,-1,-4,1,2,5,7,-10,-4,-7,8,-9,4,-3,8,4,-3,-3,3,-8,3,2,9,-8,10,3,-5,-4,2,7,-3,1,5,5,-8,-2,8,-3,-7,-10,-6,-7,-5,-4,-10,8,2,-1,1,-5,-9,-2,-5,6,7,3,6,6,2,-10,-1,-6,-6,-1,3,8,7,10,6,-5,1,6,-7,1,-4,-2,9,-9,-4,-4,8,-8,-1,-8,6,9,9,-7,10,6,10,9,5,-4,10,-6,9,5,4,-10,5,8,-5,-2,6,8,-7,7,7,-3,-1,-5,-6,-4,-2,-1,-4,-4,-5,-5,-6,8,2,-9,9,3,-4,-10,-9,-9,9,-9,-10,-1,1,7,-10,5,2,-10,8,9,-4,-10,-5,3,10,4,-8,4,-2,-9,8,4,-5,-1,10,5,-10,4,-4,7,2,2,10,-9,9,-5,-9,-6,-5,-9,6,-6,9,-2,-10,4,2,-4,-2,-5,1,9,-10,6,2,10,-1,6,10,-10,-7,-2,10,3,9,4,-9,1,8,5,-5,9,3,6,1,4,10,-9,4,-6,-10,-4,-3,-8,-2,-2,2,-5,-5,8,6,-4,-10,9,-4,6,5,-5,-4,-1,10,5,3,6,-8,-3,-6,1,1,7,-4,1,4,-10,-1,-7,4,-2,10,8,2,-4,-10,4,6,-9,6,-2,10,-1,4,-3,-7,-9,2,-7,-9,-3,-8,2,-8,-6,3,-7,1,5,3,4,-2,9,10,-8,-8,6,8,10,1,10,-4,-6,-2,-10,6,7,7,-3,5,-6,2,9,-1,6,6,3,-3,-5,-9,-2,-9,6,6,-2,1,-5,1,-3,-4,-2,4,-10,-8,4,8,-6,-4,2,10,-4,-4,-3,3,-7,6,-7,9,-7,-2,6,-6,6,3,-1,-4,7,4,-2,8,3,-1,2,10,8,-2,-2,5,8,6,4,-4,7,-10,4,10,-10,10,2,-5,3,-5,4,5,-9,-1,2,-3,-5,9,1,-7,-2,-6,6,-7,7,-4,-3,2,1,-6,-1,1,3,5,1,8,-8,10,-4,-3,-10,-1,-7,4,10,-10,-10,-9,10,9,-4,5,-9,-6,-1,-3,7,3,-1,-1,-6,2,-1,-8,-2,2,-4,-10,1,6,-6,-4,-5,6,-3,-6,9,4,-8,-10,-1,-8,9,-8,7,-4,-4,-5,-3,-6,-1,5,10,-9,6,-9,-2,-2,9,3,5,-7,4,-10,7,3,-8,-6,-2,9,4,6,6,-1,9,9,1,-5,-9,2,-10,-4,7,-1,6,-6,-7,-10,-10,8,-3,5,2,-9,-4,-9,-7,-7,4,1,7,10,-10,6,1,1,-10,10,-4,-7,9,5,10,10,9,3,1,-9,-6,-2,1,-3,-10,5,1,4,-9,-5,8,-4,-9,2,-4,2,6,-9,7,-7,4,-1,-5,4,-4,4,6,-1,-7,-6,4,3,2,-6,-5,-6,-9,3,-3,-10,7,9,4,-8,-2,1,10,5,-7,1,-6,-8,-5,8,7,-5,2,8,3,-6,-10,-1,3,4,-7,-10,3,7,-1], dtype = "uint8")#candidate|2847|(672,)|const|uint8
call_2846 = func_765_call(relay.reshape(var_2825.astype('uint8'), []), relay.reshape(const_2847.astype('uint8'), [7, 16, 6]), )
call_2848 = func_765_call(relay.reshape(var_2825.astype('uint8'), []), relay.reshape(const_2847.astype('uint8'), [7, 16, 6]), )
bop_2858 = relay.equal(var_2831.astype('bool'), relay.reshape(bop_2837.astype('bool'), relay.shape_of(var_2831))) # shape=(11, 3, 6)
output = relay.Tuple([bop_2832,call_2846,const_2847,bop_2858,])
output2 = relay.Tuple([bop_2832,call_2848,const_2847,bop_2858,])
func_2865 = relay.Function([var_2825,var_2831,], output)
mod['func_2865'] = func_2865
mod = relay.transform.InferType()(mod)
mutated_mod['func_2865'] = func_2865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2865_call = mutated_mod.get_global_var('func_2865')
var_2867 = relay.var("var_2867", dtype = "float32", shape = ())#candidate|2867|()|var|float32
var_2868 = relay.var("var_2868", dtype = "float32", shape = (11, 3, 6))#candidate|2868|(11, 3, 6)|var|float32
call_2866 = func_2865_call(var_2867,var_2868,)
output = call_2866
func_2869 = relay.Function([var_2867,var_2868,], output)
mutated_mod['func_2869'] = func_2869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2060_call = mod.get_global_var('func_2060')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2871 = relay.TupleGetItem(func_2060_call(), 0)
call_2872 = relay.TupleGetItem(func_2061_call(), 0)
uop_2895 = relay.log2(call_2871.astype('float32')) # shape=(5, 5, 13)
uop_2897 = relay.log2(call_2872.astype('float32')) # shape=(5, 5, 13)
output = uop_2895
output2 = uop_2897
func_2905 = relay.Function([], output)
mod['func_2905'] = func_2905
mod = relay.transform.InferType()(mod)
mutated_mod['func_2905'] = func_2905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2905_call = mutated_mod.get_global_var('func_2905')
call_2906 = func_2905_call()
output = call_2906
func_2907 = relay.Function([], output)
mutated_mod['func_2907'] = func_2907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_2911 = func_2905_call()
call_2912 = func_2905_call()
output = call_2911
output2 = call_2912
func_2915 = relay.Function([], output)
mod['func_2915'] = func_2915
mod = relay.transform.InferType()(mod)
output = func_2915()
func_2916 = relay.Function([], output)
mutated_mod['func_2916'] = func_2916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2933 = func_1758_call()
call_2934 = func_1758_call()
var_2935 = relay.var("var_2935", dtype = "float64", shape = (5, 5, 13))#candidate|2935|(5, 5, 13)|var|float64
bop_2936 = relay.subtract(call_2933.astype('float64'), relay.reshape(var_2935.astype('float64'), relay.shape_of(call_2933))) # shape=(5, 5, 13)
bop_2939 = relay.subtract(call_2934.astype('float64'), relay.reshape(var_2935.astype('float64'), relay.shape_of(call_2934))) # shape=(5, 5, 13)
func_2865_call = mod.get_global_var('func_2865')
func_2869_call = mutated_mod.get_global_var('func_2869')
var_2947 = relay.var("var_2947", dtype = "float32", shape = ())#candidate|2947|()|var|float32
const_2948 = relay.const([6.119487,6.979819,3.754913,-6.873596,-4.665299,-7.948739,8.207571,0.270051,-0.695463,1.717739,-3.649630,4.725981,-1.991799,-0.977176,2.830236,2.657262,-2.810666,6.039553,-9.901193,8.060884,5.940539,-6.767414,4.935423,8.830679,3.728011,3.119102,4.543889,-6.721704,1.092678,0.890506,-6.576631,0.820840,-4.335590,-0.025305,-6.680440,0.564873,-1.035647,-6.665776,3.454415,0.005999,-0.560711,7.597681,9.413624,8.323448,-6.787764,8.600665,4.910898,7.911349,2.146478,5.003848,-5.789300,-2.951924,-1.485815,-1.463915,-4.140490,-8.195677,1.539617,-8.190640,7.517261,9.137340,-7.975302,3.645410,1.796371,3.407047,-3.115116,9.459370,6.609001,9.396861,-3.275059,-5.167372,-5.077929,-7.048087,-9.025424,-2.245455,-8.856083,7.643652,6.028974,2.125525,2.950232,2.285320,0.424634,-3.617206,-1.833767,-2.159812,-7.566881,7.438248,0.810608,-1.139946,-3.293942,8.181568,-6.462416,-9.646317,5.174868,-4.892903,-2.044147,9.513889,-9.325439,6.096803,9.110595,-0.580382,-6.940257,-9.433888,7.598603,8.040193,-5.779389,-6.197520,2.261909,-3.825811,-7.056294,4.236574,-2.860047,-7.600656,9.528766,-3.685303,6.673337,-3.710394,-0.274775,0.806319,4.603571,-2.317746,-8.279987,-6.669389,8.634633,-6.760035,9.215078,-6.022020,-5.302731,7.880530,-9.519612,2.881265,-2.598944,4.898125,-2.717209,-0.802686,9.308491,4.956349,3.980681,4.832443,-1.623234,8.895420,-5.913542,-1.490416,-1.674495,-8.190554,7.961821,4.478657,2.725997,-2.007899,7.512875,7.141812,9.575358,-7.437176,-6.299437,2.627264,-1.709195,-7.119269,2.551919,1.192863,-9.922681,-3.968290,5.260169,0.404333,7.384313,9.358640,-7.922926,4.516226,7.603652,6.017092,-9.972000,3.157898,4.924466,5.671579,-7.082958,-2.643305,-7.115646,-4.012153,-9.515803,-6.697099,3.559607,8.267137,-1.675735,-8.868064,-1.049166,9.270764,-9.545939,1.070818,-9.945828,-5.302830,-2.544832,-2.909358,-7.808027,-3.257593,-8.230406,-7.164339,-0.774439,-0.806782,-5.252568,1.927878], dtype = "float32")#candidate|2948|(198,)|const|float32
call_2946 = relay.TupleGetItem(func_2865_call(relay.reshape(var_2947.astype('float32'), []), relay.reshape(const_2948.astype('float32'), [11, 3, 6]), ), 1)
call_2949 = relay.TupleGetItem(func_2869_call(relay.reshape(var_2947.astype('float32'), []), relay.reshape(const_2948.astype('float32'), [11, 3, 6]), ), 1)
uop_2950 = relay.log2(call_2946.astype('float64')) # shape=(7, 16, 6)
uop_2952 = relay.log2(call_2949.astype('float64')) # shape=(7, 16, 6)
output = relay.Tuple([bop_2936,var_2947,const_2948,uop_2950,])
output2 = relay.Tuple([bop_2939,var_2947,const_2948,uop_2952,])
func_2956 = relay.Function([var_2935,var_2947,], output)
mod['func_2956'] = func_2956
mod = relay.transform.InferType()(mod)
var_2957 = relay.var("var_2957", dtype = "float64", shape = (5, 5, 13))#candidate|2957|(5, 5, 13)|var|float64
var_2958 = relay.var("var_2958", dtype = "float32", shape = ())#candidate|2958|()|var|float32
output = func_2956(var_2957,var_2958,)
func_2959 = relay.Function([var_2957,var_2958,], output)
mutated_mod['func_2959'] = func_2959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2915_call = mod.get_global_var('func_2915')
func_2916_call = mutated_mod.get_global_var('func_2916')
call_2984 = func_2915_call()
call_2985 = func_2915_call()
output = relay.Tuple([call_2984,])
output2 = relay.Tuple([call_2985,])
func_2994 = relay.Function([], output)
mod['func_2994'] = func_2994
mod = relay.transform.InferType()(mod)
mutated_mod['func_2994'] = func_2994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mutated_mod.get_global_var('func_2994')
call_2995 = func_2994_call()
output = call_2995
func_2996 = relay.Function([], output)
mutated_mod['func_2996'] = func_2996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3001 = relay.TupleGetItem(func_2535_call(), 0)
call_3002 = relay.TupleGetItem(func_2537_call(), 0)
uop_3041 = relay.exp(call_3001.astype('float64')) # shape=(5, 5, 13)
uop_3043 = relay.exp(call_3002.astype('float64')) # shape=(5, 5, 13)
output = relay.Tuple([uop_3041,])
output2 = relay.Tuple([uop_3043,])
func_3046 = relay.Function([], output)
mod['func_3046'] = func_3046
mod = relay.transform.InferType()(mod)
output = func_3046()
func_3047 = relay.Function([], output)
mutated_mod['func_3047'] = func_3047
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3113 = relay.const([[[2.653014,2.784188,6.348266,6.290558,-9.592019],[-5.887360,-1.639910,9.200282,-9.057438,5.686446],[3.086948,7.543457,-2.455241,4.847570,8.958409],[-8.899048,2.753531,9.467699,-4.070775,4.934959],[-3.927983,8.558278,0.340943,-9.741018,-6.918979],[2.487435,-0.796751,-4.849941,1.122595,-0.422901],[-2.267059,3.349010,-5.425549,-7.017735,0.801375],[-5.708040,0.531770,6.932026,-0.158216,-3.807793],[9.401466,3.997135,-0.527529,9.569886,8.187315],[-3.260562,-0.566862,1.164665,8.070580,-8.178115],[8.324873,-0.714361,-9.343613,1.887447,-5.019185]],[[-9.609663,6.470077,4.245928,2.946663,-4.016050],[-2.323849,-7.211111,-7.409833,-0.154377,5.008818],[0.689963,6.322131,7.025183,1.113936,-6.269404],[-6.860190,8.167238,-1.169841,6.700816,2.960938],[1.690545,9.672870,3.935159,2.667677,9.096487],[-8.302696,-1.941086,-1.208341,2.422325,-3.177526],[6.709827,-0.912712,8.596534,8.925925,-4.240821],[-5.601517,7.543218,0.620290,6.154063,-7.407398],[4.681263,7.402348,-2.950914,6.441876,4.868915],[8.728311,-5.685131,-6.417197,1.383699,5.497149],[-6.971262,9.160180,2.376250,-6.054231,0.216160]],[[9.151827,1.025444,-7.719066,-5.704290,-0.855884],[-7.889268,5.471833,7.239461,-2.820590,8.701815],[7.344866,2.457135,6.698836,9.200483,7.353356],[-4.559658,-5.338902,-0.219950,0.728554,-5.811419],[-3.456559,-0.701646,-4.679808,7.801876,-7.678150],[-8.556877,8.687267,-7.753482,-3.707624,-4.833037],[-8.536555,-3.547699,8.708581,-2.360021,0.408107],[-4.832486,9.066934,5.550509,-2.452898,-3.640100],[-8.440174,-9.027580,-9.159821,-7.796826,5.496849],[-1.515876,-3.149129,-4.261025,4.697962,-8.361242],[5.883928,1.718027,2.628406,-9.614327,8.614783]],[[-1.094005,2.096328,5.626071,3.853448,-5.022140],[6.536472,3.898868,2.551652,4.647524,-3.364642],[-8.023810,-3.501117,-4.600799,-5.866510,7.033435],[3.893985,3.743241,9.939604,-2.366153,2.289395],[9.445389,9.671839,-4.755923,-1.115708,-1.784904],[0.935230,-9.806077,-0.677485,-8.155796,-6.311754],[-7.702385,0.251312,-9.506317,8.792657,-7.688433],[-0.952471,1.080469,-5.297816,-0.544779,3.098129],[3.724080,7.992105,-8.244470,-1.433997,7.434446],[-0.185877,-0.140333,5.642601,-1.949620,6.580718],[8.951717,-9.547356,4.679749,-5.977694,3.432453]],[[-1.140586,4.787138,5.036002,9.965555,-4.445413],[-1.427456,0.364373,-4.610965,9.318623,4.969200],[7.830034,-3.652643,2.637634,-2.444220,-6.304830],[3.606746,-8.287687,-0.453693,-1.045272,4.954563],[-7.775750,7.312186,-6.273868,6.110752,5.106959],[-4.213850,0.998727,-7.713860,1.076081,4.214712],[4.722754,-3.927770,5.406285,4.001853,1.408271],[-6.717757,-0.815004,8.092553,4.275937,-5.174170],[2.692651,-6.961796,-1.334389,4.363511,6.486318],[1.702674,6.479982,2.496096,-5.487164,-3.763455],[6.308081,-6.048317,-6.123437,4.604843,-0.736688]],[[-9.879795,-7.426243,-9.708124,-3.833746,-9.088699],[-0.267190,-2.985621,-4.132230,-2.560848,-7.090170],[-2.439567,9.854252,9.463304,-7.796144,-2.273466],[-7.535803,-2.681777,7.790493,4.716965,-1.738468],[3.278560,0.507593,-1.631236,8.178409,8.645879],[1.493528,-3.520065,-6.305897,-9.940020,-2.121898],[6.526276,-7.591675,1.658679,-0.987002,2.653582],[6.781503,-3.184455,-0.984057,-5.585866,8.704287],[3.075909,6.227021,-3.874012,1.422274,-2.095975],[1.684245,-7.216740,0.768803,5.016723,1.770296],[-5.043231,1.166145,7.231478,6.715712,-9.276010]],[[3.869669,4.348857,4.515938,-4.759891,-6.627344],[-6.203275,-8.329117,3.119313,-0.780708,-8.769169],[2.237289,-1.593301,0.627336,-7.230845,7.197590],[6.914307,-4.618672,6.126789,-9.004089,-7.730445],[-3.208502,-2.286589,-4.624203,-5.490813,-2.233873],[-6.879426,8.743319,1.366292,-1.070794,6.432993],[-8.404822,5.201918,4.949317,-6.081092,-1.836629],[3.392511,9.349992,-3.830417,4.581032,-4.926728],[5.895599,-1.724101,-2.278436,5.355634,2.845380],[-1.096650,7.313599,2.090030,3.460404,2.914874],[-6.690740,-6.248459,-1.938838,8.551586,-9.026893]],[[-2.977358,-3.666049,-6.600918,-3.126216,-4.234398],[2.189351,3.587995,-4.863841,8.141768,-1.052562],[4.379188,6.017586,-4.163043,-5.288099,-6.603561],[0.898902,-3.629482,3.500632,-3.770273,-3.323191],[2.364275,-5.531948,3.622733,2.342905,-8.829388],[9.056002,9.303671,5.883962,-3.053827,2.838774],[-2.306780,6.100871,7.339130,-3.883062,-3.778519],[-8.595616,-7.881058,-6.484399,7.337582,-0.854802],[6.537316,1.871677,4.968918,-3.464028,4.220173],[-0.426705,6.230269,-9.065795,-0.580881,-5.548489],[-0.460500,-2.348575,9.836508,-0.835883,8.501972]],[[-1.062280,-7.198342,2.725650,8.922758,0.357002],[5.140204,-0.103492,-7.758072,4.751424,1.528657],[0.313426,-5.196354,-6.647433,9.521936,-9.898411],[-1.164550,3.661053,4.439195,-2.140993,7.502804],[0.061430,9.527496,1.835425,-5.896432,-6.129443],[-1.586674,9.011705,8.486934,2.877887,-2.124933],[1.363251,-7.117845,3.456803,9.914871,-4.844850],[-9.052114,-2.575464,-5.739227,3.070443,-2.280229],[-0.480548,1.088909,-4.496936,-6.318905,8.897699],[9.926421,7.270860,-4.848484,4.890009,-1.389915],[-2.218380,3.109833,-2.172173,-8.012190,3.096094]],[[6.769374,5.587222,9.363094,2.087118,0.531991],[6.612750,-3.590794,4.777938,7.375528,-9.435443],[-0.567219,-5.410768,2.077418,0.422878,-9.821180],[1.928969,9.290142,9.808400,-0.713404,-3.530860],[2.770974,-6.099993,-4.956574,-4.928057,5.238494],[8.896913,8.143220,6.351027,-2.699379,-5.538507],[3.748718,-3.227465,0.534664,-9.030465,-6.662546],[3.624735,-9.816152,3.169558,4.540599,-5.394105],[5.015292,6.690548,-1.794004,7.356920,4.210963],[7.900799,9.045173,8.830916,4.682202,-2.548969],[-5.293741,-9.410242,-1.243666,4.399320,3.411613]],[[-2.641715,0.270961,-9.609876,-1.128518,-9.869230],[3.441487,6.668440,0.367221,8.383785,-5.568694],[6.585742,-5.909498,9.307532,9.693837,-9.840625],[-2.344350,7.099671,-8.125814,3.578106,-6.552110],[5.731502,-7.843171,-3.555073,0.887401,-9.270042],[-8.694361,6.283414,3.889464,9.119920,4.650467],[-5.825134,-5.575372,-2.207630,2.497962,8.427266],[5.221015,4.683184,7.637347,-9.893316,-7.044600],[-6.363921,-1.379251,7.745754,-1.794563,-1.239137],[-0.703369,-9.777387,8.525202,-9.053779,-8.212771],[-3.927628,-7.749912,2.067553,0.607431,-7.955713]],[[8.091351,-5.495627,-3.862836,0.794777,-4.736282],[8.049327,-7.833960,1.627248,-8.404042,-0.804412],[-0.638664,-4.306570,1.292542,-4.708596,0.257739],[-1.947921,-6.250838,-3.166196,-4.620043,8.610271],[-3.333670,0.172388,-6.604585,-3.803837,-9.189062],[-5.113896,9.293982,1.877946,-1.260915,6.228184],[2.124723,-7.088653,3.757491,-6.160490,5.422392],[-9.512143,-2.300570,-3.490547,1.348666,9.299432],[-0.018104,-9.452339,0.914460,-8.011994,9.768970],[9.501387,6.649107,-7.897743,8.860095,-9.633768],[0.643879,-6.829612,-7.530675,-9.967597,7.765017]]], dtype = "float64")#candidate|3113|(12, 11, 5)|const|float64
uop_3114 = relay.sin(const_3113.astype('float64')) # shape=(12, 11, 5)
output = relay.Tuple([uop_3114,])
output2 = relay.Tuple([uop_3114,])
func_3121 = relay.Function([], output)
mod['func_3121'] = func_3121
mod = relay.transform.InferType()(mod)
mutated_mod['func_3121'] = func_3121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mutated_mod.get_global_var('func_3121')
call_3122 = func_3121_call()
output = call_3122
func_3123 = relay.Function([], output)
mutated_mod['func_3123'] = func_3123
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3140 = relay.var("var_3140", dtype = "int16", shape = (13, 14, 16))#candidate|3140|(13, 14, 16)|var|int16
var_3141 = relay.var("var_3141", dtype = "int16", shape = (13, 14, 16))#candidate|3141|(13, 14, 16)|var|int16
bop_3142 = relay.bitwise_xor(var_3140.astype('int16'), relay.reshape(var_3141.astype('int16'), relay.shape_of(var_3140))) # shape=(13, 14, 16)
func_2865_call = mod.get_global_var('func_2865')
func_2869_call = mutated_mod.get_global_var('func_2869')
var_3146 = relay.var("var_3146", dtype = "float32", shape = ())#candidate|3146|()|var|float32
var_3147 = relay.var("var_3147", dtype = "float32", shape = (198,))#candidate|3147|(198,)|var|float32
call_3145 = relay.TupleGetItem(func_2865_call(relay.reshape(var_3146.astype('float32'), []), relay.reshape(var_3147.astype('float32'), [11, 3, 6]), ), 2)
call_3148 = relay.TupleGetItem(func_2869_call(relay.reshape(var_3146.astype('float32'), []), relay.reshape(var_3147.astype('float32'), [11, 3, 6]), ), 2)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3149 = relay.TupleGetItem(func_2994_call(), 0)
call_3150 = relay.TupleGetItem(func_2996_call(), 0)
func_2915_call = mod.get_global_var('func_2915')
func_2916_call = mutated_mod.get_global_var('func_2916')
call_3160 = func_2915_call()
call_3161 = func_2915_call()
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3162 = relay.TupleGetItem(func_2994_call(), 0)
call_3163 = relay.TupleGetItem(func_2996_call(), 0)
output = relay.Tuple([bop_3142,call_3145,var_3146,var_3147,call_3149,call_3160,call_3162,])
output2 = relay.Tuple([bop_3142,call_3148,var_3146,var_3147,call_3150,call_3161,call_3163,])
func_3173 = relay.Function([var_3140,var_3141,var_3146,var_3147,], output)
mod['func_3173'] = func_3173
mod = relay.transform.InferType()(mod)
mutated_mod['func_3173'] = func_3173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3173_call = mutated_mod.get_global_var('func_3173')
var_3175 = relay.var("var_3175", dtype = "int16", shape = (13, 14, 16))#candidate|3175|(13, 14, 16)|var|int16
var_3176 = relay.var("var_3176", dtype = "int16", shape = (13, 14, 16))#candidate|3176|(13, 14, 16)|var|int16
var_3177 = relay.var("var_3177", dtype = "float32", shape = ())#candidate|3177|()|var|float32
var_3178 = relay.var("var_3178", dtype = "float32", shape = (198,))#candidate|3178|(198,)|var|float32
call_3174 = func_3173_call(var_3175,var_3176,var_3177,var_3178,)
output = call_3174
func_3179 = relay.Function([var_3175,var_3176,var_3177,var_3178,], output)
mutated_mod['func_3179'] = func_3179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3244 = relay.var("var_3244", dtype = "float32", shape = (13, 2, 9))#candidate|3244|(13, 2, 9)|var|float32
const_3245 = relay.const([[[9.128083,6.387852,-2.642242,5.483327,-8.060482,-3.356561,-5.844131,-0.496016,1.911752],[-0.853418,-7.480625,-4.641457,7.158880,-8.662924,-1.787312,-1.528493,7.075146,-1.003432]],[[9.987042,4.798025,-8.772580,-1.450464,-0.049325,-1.937940,-7.936072,4.783307,-5.499807],[7.435011,-0.174650,2.194715,-4.277670,-2.356988,-4.348711,0.642067,-1.126102,0.600697]],[[-0.897225,-2.959803,-8.586766,7.139127,7.919705,-2.676871,-0.962906,3.099066,2.737684],[0.115087,-1.316994,4.050883,1.507741,6.342579,-4.883981,-6.130147,-7.804325,7.714571]],[[8.057035,3.033711,-9.833910,-6.110352,-5.556145,4.398109,8.298207,7.585093,-9.136085],[-7.461546,0.770335,5.608829,-1.117775,0.387561,-3.656900,-6.605101,0.167504,-1.269676]],[[1.324369,-6.669835,9.007289,3.015362,-0.280616,-3.942806,9.209400,-5.859637,-3.998023],[-5.563179,-8.308273,-2.904573,9.012870,-8.022743,-2.629403,-0.953046,-9.897139,6.886594]],[[-1.707836,-9.093817,2.126801,0.686012,0.818585,-9.378458,0.557417,-1.406671,-9.212397],[9.147557,7.565370,-1.555837,-2.544784,2.914692,1.192889,-2.041185,4.435092,-6.266150]],[[-7.397073,-8.168913,-2.758559,3.282600,7.606798,7.764952,-1.195386,9.068923,-7.150438],[-9.570025,-2.189950,5.247168,-7.588708,5.060373,-8.327331,7.723908,6.786904,-9.943300]],[[-9.313359,-9.958202,-4.117301,1.686243,-2.930240,-9.931760,-4.124289,8.342629,7.618655],[-9.200380,8.590406,0.840528,9.253451,-2.606262,-8.877417,-2.441246,-2.571587,6.055046]],[[-0.478381,-7.348751,0.157326,-8.177028,3.349187,7.632852,-5.726132,-8.000048,3.524502],[-1.324578,-2.928554,-1.684068,4.083617,4.379745,8.339215,-0.464856,7.567718,-6.150119]],[[-5.409270,-3.760248,-8.891345,-0.011793,2.173162,-3.933130,-4.236390,-4.170683,5.437627],[-3.961825,6.465146,9.708030,-9.217031,2.790019,-7.422739,-3.830791,-2.398229,-3.823036]],[[-8.591413,8.928097,0.162325,9.087923,-5.534859,6.387887,-5.208363,0.561321,3.504799],[-9.695432,-9.278170,-8.107436,7.893295,5.503421,5.985809,-7.127908,-6.858281,-7.775010]],[[-7.959581,-7.796457,2.121879,-8.290052,0.776431,8.940531,-0.082621,-8.508457,4.553894],[6.138610,0.697293,-7.019647,-0.939411,7.157216,9.852400,1.437962,9.891689,-5.585284]],[[7.859881,-5.437769,-2.766083,6.577204,5.571755,-4.565232,-8.853480,7.950820,-2.286967],[5.826747,-1.911328,-2.978187,-5.429367,6.460275,6.106955,-5.082278,4.416718,8.900363]]], dtype = "float32")#candidate|3245|(13, 2, 9)|const|float32
bop_3246 = relay.floor_divide(var_3244.astype('float32'), relay.reshape(const_3245.astype('float32'), relay.shape_of(var_3244))) # shape=(13, 2, 9)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3250 = relay.TupleGetItem(func_3046_call(), 0)
call_3251 = relay.TupleGetItem(func_3047_call(), 0)
output = relay.Tuple([bop_3246,call_3250,])
output2 = relay.Tuple([bop_3246,call_3251,])
func_3265 = relay.Function([var_3244,], output)
mod['func_3265'] = func_3265
mod = relay.transform.InferType()(mod)
mutated_mod['func_3265'] = func_3265
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3266 = relay.var("var_3266", dtype = "float32", shape = (13, 2, 9))#candidate|3266|(13, 2, 9)|var|float32
func_3265_call = mutated_mod.get_global_var('func_3265')
call_3267 = func_3265_call(var_3266)
output = call_3267
func_3268 = relay.Function([var_3266], output)
mutated_mod['func_3268'] = func_3268
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3270 = relay.var("var_3270", dtype = "float32", shape = ())#candidate|3270|()|var|float32
var_3271 = relay.var("var_3271", dtype = "float32", shape = (2, 1, 10))#candidate|3271|(2, 1, 10)|var|float32
bop_3272 = relay.minimum(var_3270.astype('float32'), var_3271.astype('float32')) # shape=(2, 1, 10)
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_3275 = relay.TupleGetItem(func_2776_call(), 0)
call_3276 = relay.TupleGetItem(func_2778_call(), 0)
bop_3295 = relay.greater(var_3271.astype('bool'), relay.reshape(bop_3272.astype('bool'), relay.shape_of(var_3271))) # shape=(2, 1, 10)
func_900_call = mod.get_global_var('func_900')
func_903_call = mutated_mod.get_global_var('func_903')
var_3300 = relay.var("var_3300", dtype = "int16", shape = (975,))#candidate|3300|(975,)|var|int16
call_3299 = relay.TupleGetItem(func_900_call(relay.reshape(var_3300.astype('int16'), [13, 15, 5]), relay.reshape(var_3300.astype('int16'), [13, 15, 5]), ), 0)
call_3301 = relay.TupleGetItem(func_903_call(relay.reshape(var_3300.astype('int16'), [13, 15, 5]), relay.reshape(var_3300.astype('int16'), [13, 15, 5]), ), 0)
func_2865_call = mod.get_global_var('func_2865')
func_2869_call = mutated_mod.get_global_var('func_2869')
const_3307 = relay.const([-4.820816,-7.749164,-9.258430,8.080836,-1.643772,-2.927736,7.796718,8.623382,9.604382,-2.690850,-4.811757,-6.076947,-3.469251,-2.696145,-3.867083,-6.754241,-0.996677,-6.749456,9.962241,7.934702,-1.609857,2.095650,1.400677,-7.902229,-7.957422,-9.249672,-0.691407,0.131516,4.963880,-4.013933,-5.618415,-4.140082,1.393417,4.102583,6.911864,5.004625,-0.854063,1.792446,0.824761,-2.010766,6.354452,-1.768844,4.071726,-5.819624,6.572593,4.863302,6.834308,-1.212816,-7.995050,0.574970,-4.184367,1.565090,2.686027,-2.899316,8.820357,7.614161,7.679313,-2.415690,6.009280,-7.479514,-4.900558,-3.026081,3.662832,-9.920540,-2.276089,9.129699,-4.367405,4.106783,-9.586623,-3.367090,-6.998148,-5.746842,6.671153,-6.119510,6.736006,1.201603,-5.412118,-5.298485,1.103460,4.771365,-2.782927,-3.701759,-5.890480,5.701347,-4.267419,-1.060718,5.931661,-4.093788,9.558053,4.951446,1.438213,-2.728227,-8.692520,-2.792605,-3.160993,5.784926,-0.060341,6.645877,9.878322,1.801967,5.050761,-4.886134,-3.839794,1.416650,2.338023,1.759772,-6.864884,2.266466,-6.245867,-2.915779,7.169166,7.048079,8.601094,-1.833051,4.067032,-0.160713,7.049114,4.084532,-1.892986,-9.136922,2.034406,-0.291708,6.458923,-0.607224,3.952994,-4.924153,-5.548482,1.282407,0.985579,-7.160102,3.531379,9.426145,8.093107,1.230129,5.051473,-9.425189,5.388470,-4.893700,-3.293532,-6.492624,7.018545,-3.371394,-6.664976,-3.841621,-0.337969,3.159407,4.884568,-6.848918,1.265352,-5.659319,3.233841,-4.409512,-6.856683,-1.112738,5.018833,-6.012574,8.851924,9.347794,-4.834619,4.368325,-0.199405,9.680204,5.707454,3.848688,9.280441,-5.684843,-3.223816,5.505154,1.932552,0.601075,-7.983590,-9.602045,-1.829496,7.289011,7.585249,5.494253,2.586032,5.290062,7.258668,-6.834376,6.290727,6.495973,8.761408,-0.301284,-4.266830,2.206740,8.589542,3.204855,7.084953,2.072831,0.722872,5.223393,9.721094,-1.620129,8.251717,5.297685,9.773435,-5.346978], dtype = "float32")#candidate|3307|(198,)|const|float32
call_3306 = relay.TupleGetItem(func_2865_call(relay.reshape(var_3270.astype('float32'), []), relay.reshape(const_3307.astype('float32'), [11, 3, 6]), ), 0)
call_3308 = relay.TupleGetItem(func_2869_call(relay.reshape(var_3270.astype('float32'), []), relay.reshape(const_3307.astype('float32'), [11, 3, 6]), ), 0)
func_2752_call = mod.get_global_var('func_2752')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_3311 = relay.TupleGetItem(func_2752_call(), 0)
call_3312 = relay.TupleGetItem(func_2753_call(), 0)
func_2956_call = mod.get_global_var('func_2956')
func_2959_call = mutated_mod.get_global_var('func_2959')
call_3319 = relay.TupleGetItem(func_2956_call(relay.reshape(call_3311.astype('float64'), [5, 5, 13]), relay.reshape(var_3270.astype('float32'), []), ), 2)
call_3320 = relay.TupleGetItem(func_2959_call(relay.reshape(call_3311.astype('float64'), [5, 5, 13]), relay.reshape(var_3270.astype('float32'), []), ), 2)
output = relay.Tuple([call_3275,bop_3295,call_3299,var_3300,call_3306,const_3307,call_3311,call_3319,])
output2 = relay.Tuple([call_3276,bop_3295,call_3301,var_3300,call_3308,const_3307,call_3312,call_3320,])
func_3321 = relay.Function([var_3270,var_3271,var_3300,], output)
mod['func_3321'] = func_3321
mod = relay.transform.InferType()(mod)
mutated_mod['func_3321'] = func_3321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3321_call = mutated_mod.get_global_var('func_3321')
var_3323 = relay.var("var_3323", dtype = "float32", shape = ())#candidate|3323|()|var|float32
var_3324 = relay.var("var_3324", dtype = "float32", shape = (2, 1, 10))#candidate|3324|(2, 1, 10)|var|float32
var_3325 = relay.var("var_3325", dtype = "int16", shape = (975,))#candidate|3325|(975,)|var|int16
call_3322 = func_3321_call(var_3323,var_3324,var_3325,)
output = call_3322
func_3326 = relay.Function([var_3323,var_3324,var_3325,], output)
mutated_mod['func_3326'] = func_3326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3335 = relay.TupleGetItem(func_2994_call(), 0)
call_3336 = relay.TupleGetItem(func_2996_call(), 0)
output = relay.Tuple([call_3335,])
output2 = relay.Tuple([call_3336,])
func_3341 = relay.Function([], output)
mod['func_3341'] = func_3341
mod = relay.transform.InferType()(mod)
output = func_3341()
func_3342 = relay.Function([], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3349 = relay.var("var_3349", dtype = "bool", shape = (12, 12, 8))#candidate|3349|(12, 12, 8)|var|bool
var_3350 = relay.var("var_3350", dtype = "bool", shape = (12, 12, 8))#candidate|3350|(12, 12, 8)|var|bool
bop_3351 = relay.logical_and(var_3349.astype('bool'), relay.reshape(var_3350.astype('bool'), relay.shape_of(var_3349))) # shape=(12, 12, 8)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
var_3361 = relay.var("var_3361", dtype = "uint16", shape = (448,))#candidate|3361|(448,)|var|uint16
call_3360 = relay.TupleGetItem(func_1917_call(relay.reshape(var_3361.astype('uint16'), [448,])), 1)
call_3362 = relay.TupleGetItem(func_1919_call(relay.reshape(var_3361.astype('uint16'), [448,])), 1)
output = relay.Tuple([bop_3351,call_3360,var_3361,])
output2 = relay.Tuple([bop_3351,call_3362,var_3361,])
func_3386 = relay.Function([var_3349,var_3350,var_3361,], output)
mod['func_3386'] = func_3386
mod = relay.transform.InferType()(mod)
var_3387 = relay.var("var_3387", dtype = "bool", shape = (12, 12, 8))#candidate|3387|(12, 12, 8)|var|bool
var_3388 = relay.var("var_3388", dtype = "bool", shape = (12, 12, 8))#candidate|3388|(12, 12, 8)|var|bool
var_3389 = relay.var("var_3389", dtype = "uint16", shape = (448,))#candidate|3389|(448,)|var|uint16
output = func_3386(var_3387,var_3388,var_3389,)
func_3390 = relay.Function([var_3387,var_3388,var_3389,], output)
mutated_mod['func_3390'] = func_3390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3402 = relay.TupleGetItem(func_3046_call(), 0)
call_3403 = relay.TupleGetItem(func_3047_call(), 0)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3409 = relay.TupleGetItem(func_2535_call(), 0)
call_3410 = relay.TupleGetItem(func_2537_call(), 0)
bop_3419 = relay.floor_divide(call_3402.astype('float64'), relay.reshape(call_3409.astype('float64'), relay.shape_of(call_3402))) # shape=(5, 5, 13)
bop_3422 = relay.floor_divide(call_3403.astype('float64'), relay.reshape(call_3410.astype('float64'), relay.shape_of(call_3403))) # shape=(5, 5, 13)
func_1320_call = mod.get_global_var('func_1320')
func_1323_call = mutated_mod.get_global_var('func_1323')
var_3428 = relay.var("var_3428", dtype = "uint16", shape = (448,))#candidate|3428|(448,)|var|uint16
call_3427 = func_1320_call(relay.reshape(var_3428.astype('uint16'), [8, 14, 4]))
call_3429 = func_1320_call(relay.reshape(var_3428.astype('uint16'), [8, 14, 4]))
output = relay.Tuple([bop_3419,call_3427,var_3428,])
output2 = relay.Tuple([bop_3422,call_3429,var_3428,])
func_3430 = relay.Function([var_3428,], output)
mod['func_3430'] = func_3430
mod = relay.transform.InferType()(mod)
var_3431 = relay.var("var_3431", dtype = "uint16", shape = (448,))#candidate|3431|(448,)|var|uint16
output = func_3430(var_3431)
func_3432 = relay.Function([var_3431], output)
mutated_mod['func_3432'] = func_3432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3462 = relay.TupleGetItem(func_3046_call(), 0)
call_3463 = relay.TupleGetItem(func_3047_call(), 0)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_3470 = func_1758_call()
call_3471 = func_1758_call()
func_3173_call = mod.get_global_var('func_3173')
func_3179_call = mutated_mod.get_global_var('func_3179')
const_3474 = relay.const([-1,-10,-7,7,-7,-3,9,3,8,-4,-6,1,10,10,-8,5,-2,-8,-7,2,7,-10,7,-6,7,-3,-8,2,-10,7,5,-9,7,9,2,10,7,4,5,10,-1,-6,-9,-8,-1,9,8,-7,5,1,-7,5,-2,1,-2,-9,6,-3,-4,-4,-9,-2,-10,4,-5,1,5,-8,-8,6,10,4,-1,-10,9,9,-6,-4,10,-2,-2,-6,10,8,3,-1,-7,2,3,2,-8,9,-2,2,3,-4,6,4,6,-7,3,-3,-10,-10,-6,4,-3,-10,10,-6,6,9,-2,2,-6,6,-5,-2,3,-10,4,5,-1,-4,-8,3,2,8,7,-1,-8,-2,7,10,6,1,5,9,4,6,-4,8,1,2,-5,-8,-10,-8,4,7,9,2,-7,-2,6,10,7,8,3,7,-2,3,-7,1,8,-3,-7,10,8,2,10,-6,2,-6,-5,-3,9,-1,6,10,-9,8,8,9,-10,1,-4,8,4,-9,8,-6,-1,-5,-6,-10,6,10,-7,-3,9,-8,3,-7,1,-4,1,6,-6,8,4,6,7,7,6,-3,-3,7,7,1,-1,7,-6,5,-3,-3,-10,-10,-8,1,6,6,-4,-5,9,9,2,4,-8,-7,2,10,2,3,7,-1,-7,-2,10,-4,-5,8,8,3,-3,-6,2,-10,-6,-2,6,-3,2,6,5,2,-10,5,-4,-5,-1,-1,9,-7,4,-5,5,-3,-5,9,-6,10,-1,5,5,2,3,1,7,-4,-9,9,-6,3,1,1,-4,5,-6,-3,-2,-7,10,-6,5,-6,-8,-2,-1,-8,-8,-2,-10,10,-7,8,-7,4,-2,4,10,-4,7,5,-1,-10,3,-3,-9,10,-5,-7,3,2,4,5,-8,-2,-4,-4,-9,-6,-6,-5,10,-3,4,-9,-3,-2,-9,-1,-5,3,-10,-6,1,1,-9,-4,-4,5,-9,4,-7,9,5,-2,-2,10,2,-1,8,-10,-10,5,1,1,6,2,-4,-9,10,9,-8,4,-7,-3,-8,-9,9,-10,5,2,7,-5,4,9,-7,6,7,5,4,8,-3,10,-2,4,-4,-9,8,-1,7,-8,6,10,-3,-9,5,9,-4,-9,9,-6,-10,3,10,-2,-4,3,-4,7,-8,-4,-2,10,-4,-4,4,8,-4,2,7,-3,2,-2,9,-4,6,9,-3,-5,9,1,-9,7,-10,-7,3,-7,-4,-3,-10,9,5,5,-10,-6,-10,-4,6,2,2,-2,-7,-10,-9,3,10,-7,-1,-4,3,-2,6,1,9,5,-3,4,7,-1,9,-8,-6,-5,-7,2,8,4,9,-4,-1,10,8,-3,10,-5,-6,7,10,-2,10,9,-7,-3,-10,-7,-8,4,10,4,9,-8,-2,10,-8,1,6,7,-4,-2,-7,-5,5,-2,-7,5,-6,5,-10,2,-9,6,-4,1,-5,-2,3,9,9,6,-8,5,6,1,-7,3,-7,-3,4,-9,-8,-3,-10,-2,-4,8,9,-5,5,10,3,8,-4,1,5,-7,10,-6,2,1,6,7,5,10,-2,-10,6,4,-10,-8,-4,-10,6,-7,3,2,9,5,-3,-2,9,-9,1,-5,-8,-8,7,-7,3,1,1,-7,5,2,1,3,7,3,7,1,-10,-6,-8,-9,-4,-8,4,-5,1,6,-3,-10,-5,10,-2,5,-1,-8,-3,-9,7,-4,-5,1,8,8,10,-4,4,5,5,5,-3,5,9,-5,-1,9,-9,4,10,1,-1,-5,8,-8,-1,9,7,2,-7,-4,7,4,8,3,9,7,6,-4,1,-7,4,-8,1,-9,-6,-7,-10,1,1,3,-8,2,4,10,8,10,5,-5,8,7,8,-9,8,-4,3,-3,-2,7,-10,1,-6,2,-9,-10,-10,2,-2,6,-2,1,10,8,-8,7,-4,6,9,1,-4,6,-1,-3,9,5,2,7,-1,-3,10,6,8,3,-1,-5,9,-10,10,-5,5,-2,-7,8,-6,6,-10,-1,6,8,-10,6,-6,10,-2,-7,-5,3,-10,10,9,-5,8,-9,-1,6,10,1,-10,2,-5,8,-9,-2,9,8,-7,1,8,10,7,-1,9,2,2,-1,4,9,-10,4,-2,-1,5,4,2,-3,1,-5,-7,-8,-3,-7,10,-2,-6,2,-1,9,-5,-9,7,5,7,8,8,-4,9,-10,7,9,-10,-3,8,-7,5,1,10,-1,7,-3,-9,8,6,7,1,9,9,-4,-4,-1,9,-2,-7,7,4,8,5,-1,5,-6,-4,-2,9,-1,9,3,-3,6,-9,1,-3,7,9,10,-8,2,3,6,-2,-4,-10,-8,3,-10,-8,-4,-3,8,-2,6,7,3,-4,2,7,-6,5,9,-9,-8,3,-8,6,-8,6,-8,4,5,-10,3,-4,-6,4,-7,-6,1,-1,-6,9,-7,10,8,-7,-1,1,-6,-2,6,-2,2,-9,9,-6,-9,1,-7,-1,4,-1,7,-6,7,-9,-7,-5,9,3,-6,-5,1,-10,6,7,-1,2,10,-3,9,7,3,4,-8,9,6,-8,9,-7,-9,-4,3,-8,-5,10,-3,9,-1,-7,10,2,2,-2,7,-8,6,-9,-10,-3,-10,-1,10,-8,-3,-9,-4,10,10,-1,-3,-5,2,1,-3,-1,9,-5,-1,1,9,-8,8,1,2,-5,2,6,-6,-6,-1,-9,8,-9,-6,-5,-10,-9,1,-6,-3,-7,-3,-7,-8,-7,1,-1,-1,-9,3,-1,5,1,2,-8,-10,-8,-6,1,9,6,3,10,-10,-10,-1,5,-5,-3,-6,1,-5,-9,3,8,-8,-5,-2,7,-4,-6,-10,-4,-9,-1,7,9,1,5,-7,-8,-5,-8,-10,10,3,-10,9,7,10,-1,10,-10,-9,4,6,-3,-7,-2,7,2,10,-3,7,-6,-10,3,-8,-10,8,5,10,-8,10,-5,-2,4,-8,-10,7,-1,5,-6,8,10,-1,-9,4,7,7,-2,8,2,5,10,-10,-10,6,-7,-1,10,3,-3,9,2,4,5,-10,-8,1,-8,1,-5,1,9,9,7,9,3,-2,3,1,-5,-7,7,-3,8,-10,-10,6,-4,-9,9,1,-7,6,-6,-8,-9,6,-2,8,2,4,8,1,5,3,9,5,-6,8,10,-6,2,3,-2,5,-7,-6,-8,-9,9,6,-5,-6,4,6,1,-2,-6,6,-8,-4,9,-1,8,-8,1,7,-7,-8,8,-6,10,9,-7,-5,-5,9,8,-10,10,-3,4,-7,-4,3,-3,-8,-8,-8,-3,9,2,3,8,6,1,-6,-1,7,10,-7,10,-5,-4,3,-5,-7,-10,9,-4,-5,6,4,-6,5,3,-10,-5,1,-7,-7,9,-3,6,9,7,-7,-7,2,-1,1,9,7,6,5,4,-10,-8,6,-3,4,-6,4,-9,7,5,4,-9,10,-8,-1,-9,-9,-3,10,7,5,4,-9,8,-5,-3,-7,-1,-10,-3,5,-3,8,-9,-2,-2,-2,-8,3,6,-7,8,-3,-2,-8,-7,7,-7,-8,3,3,-6,-4,-7,-10,-5,-1,-2,10,1,-9,2,10,10,4,-7,9,-5,10,9,2,-7,-7,-1,-3,6,3,-9,-7,-1,2,-9,3,-3,-3,-3,6,-2,-6,-9,-5,4,-3,3,2,1,3,-5,6,-1,10,-6,1,9,-2,10,-3,7,7,-6,-3,-5,6,3,9,3,-8,-6,-8,8,-3,-7,-3,10,2,1,2,-2,-7,2,-10,5,-3,-7,-8,-9,3,5,10,-6,-3,8,2,-6,4,6,3,2,-6,5,3,-5,1,10,7,-4,10,6,1,-4,-9,8,4,8,-8,4,-10,-6,8,2,2,8,5,8,7,2,-2,10,2,-6,4,2,8,2,-5,-3,-10,9,-6,-3,8,-3,-8,4,2,10,1,-7,-9,-7,5,1,3,-3,8,-6,-3,-5,-9,-1,-3,6,-3,3,3,-8,1,6,-1,7,-4,4,-9,8,-9,10,8,-6,-10,-4,-8,-3,-2,-7,5,2,6,-7,-4,4,4,7,-1,-4,1,-3,-10,2,-5,-5,-2,2,-3,-2,5,-4,1,10,4,4,-2,6,3,-4,-6,1,-7,5,-3,9,-4,-9,-4,-8,3,-6,9,6,10,2,-2,4,-7,9,6,10,-3,-7,-7,9,-7,4,-9,-9,2,-4,6,4,-7,-5,-3,2,-5,-6,4,-2,-10,-6,-9,-7,8,-5,-1,2,-4,-10,-4,-6,3,-1,7,7,-2,-6,10,3,-9,4,1,-8,3,-3,-2,5,-9,2,4,3,2,8,-7,10,3,-5,-2,-9,-3,-1,1,2,-6,6,-4,5,-10,-10,8,-2,5,-7,-2,-1,1,4,10,2,2,6,-8,-4,6,7,3,6,9,-5,10,-8,10,4,7,7,-5,5,-6,4,-2,-7,-2,-5,6,2,7,-10,-9,6,8,5,-8,7,-1,7,3,10,-9,-4,6,5,-3,10,-7,10,-10,1,5,-2,-10,-2,5,6,-9,-8,-6,8,-8,-1,-5,-10,-6,-4,8,9,-7,1,-3,5,-7,6,-8,1,5,8,-5,-8,1,3,-10,-9,1,8,-7,5,7,-5,10,-10,-2,-6,9,9,5,-1,-2,9,-10,-9,-1,-9,10,3,4,4,2,-2,-3,2,2,-1,2,10,-1,7,3,-10,3,-2,7,-10,5,1,-4,-4,-6,1,-8,-10,-7,-9,-4,-3,2,-4,1,-9,8,4,7,-6,-4,-1,-5,-9,7,-5,7,-1,-5,-10,-9,-5,-3,8,-9,-2,-3,-5,-3,3,4,-2,7,-2,8,-3,4,-3,6,-8,-8,-8,-3,-9,7,6,-1,-2,4,3,9,9,3,-2,-5,-4,1,4,-4,10,-7,3,-5,-6,-3,10,-4,-5,3,6,8,-3,-1,-4,-1,6,-3,6,6,-8,1,-10,7,4,3,-9,1,3,-10,8,-3,1,-5,-3,-1,9,9,8,5,9,3,10,-2,5,9,-5,-8,-10,5,4,-6,-7,4,-4,-7,-6,1,-4,6,4,3,-10,6,-5,-3,5,4,6,-7,-7,-1,5,-9,-4,-8,-2,10,5,-4,-6,-9,-6,-5,3,3,6,-2,-8,10,6,2,1,10,7,6,10,-6,-10,-1,5,-2,-9,-4,3,-9,-3,7,-3,8,10,3,9,10,-4,-4,-6,2,9,10,-1,1,10,-8,4,2,9,-5,7,-10,6,-10,8,-8,9,1,9,-3,-7,-1,-6,6,-8,-4,8,-6,7,7,-1,2,-4,-9,4,-1,5,-3,-7,-6,2,10,3,-4,-5,6,9,5,3,-6,7,10,-3,1,-4,5,-9,7,4,-4,4,4,-10,-7,-2,-1,-4,1,6,5,10,-7,6,1,-7,8,5,-7,10,9,8,-3,3,-10,-5,-8,-5,-4,-10,1,-9,1,9,-10,-3,-3,1,5,-7,2,10,-6,6,5,6,7,3,1,7,2,-10,-3,10,-4,1,-8,-5,-5,8,-1,6,-10,-6,-2,10,-3,1,-3,1,8,3,-10,-2,-3,5,-3,-10,1,-3,8,-8,-6,-6,10,6,9,3,10,-4,-8,-7,-1,5,2,6,-1,-1,-5,-8,4,4,5,-3,-5,-8,-8,-3,1,-3,-5,-2,-3,-5,-2,5,9,7,9,9,-7,-8,-3,5,8,-6,7,1,-5,-2,1,2,7,4,-9,1,-1,4,9,-9,-7,1,-4,-8,3,5,7,6,7,1,4,-6,10,-10,-9,-5,-3,-2,1,8,-10,-9,-2,-1,4,7,-4,2,10,1,2,-6,4,-6,2,10,8,-8,-2,-1,3,-4,-8,-10,-2,-10,1,-1,-7,-2,10,-10,-1,1,9,10,10,8,-4,-10,1,9,5,-7,-7,-1,10,7,10,-5,-2,1,-10,-3,9,-1,3,-2,-9,3,9,5,5,-9,2,4,-10,9,5,-6,-3,-7,-6,7,2,-3,1,-8,-2,3,-2,1,3,-4,9,-7,7,-1,4,8,5,5,-9,-6,2,6,-6,8,4,2,-3,8,-2,1,-8,-2,-10,10,-1,-10,-6,1,-1,5,-2,-1,-5,-5,9,-7,-4,-9,-7,4,7,-3,10,5,2,1,7,10,-2,-1,10,-9,6,-1,-8,2,-10,-6,-8,6,-1,5,10,9,8,-4,-9,-7,10,1,4,5,8,-8,4,-8,2,2,7,-1,-5,-7,7,-1,-3,-7,6,3,-5,2,-7,-4,-2,-1,10,-7,-9,9,-8,5,5,-8,-5,-4,-4,-10,7,-1,10,1,4,-3,10,-8,-4,-10,6,9,1,-2,2,-7,3,1,10,1,7,8,8,8,1,-1,3,8,5,-8,-9,-7,5,-6,-7,-10,5,-4,7,6,-9,7,-1,6,5,3,1,8,8,-10,3,1,-9,2,8,-6,-9,9,-7,3,10,-8,8,6,10,-2,7,4,2,-2,5,7,10,-3,-2,-9,-4,3,2,9,5,-8,7,-8,7,-9,-9,-8,2,-4,-10,7,1,-8,-9,-5,-8,-7,-5,2,-7,8,-7,5,-8,6,-5,3,-2,6,-8,8,-6,-1,-1,6,-3,-6,-1,-4,1,6,-2,9,-10,7,-10,3,9,-10,6,10,8,-4,8,-7,-7,-6,-4,4,2,3,6,9,-10,8,2,-7,-6,1,-8,-5,-5,-5,6,4,-5,-1,5,-6,6,2,4,2,2,-3,4,-7,-7,-10,6,-2,-5,9,2,4,1,-7,7,4,3,-10,-3,7,-1,-6,5,7,-10,7,-4,-9,-8,2,6,-5,-3,-7,3,-10,-3,3,-4,-5,7,-6,4,9,-2,7,7,8,-6,8,-10,-6,-5,-8,-9,1,6,8,3,-2,-8,-6,1,-7,-10,8,5,1,-7,9,2,4,7,8,9,8,8,-4,-7,-8,10,-5,4,-5,4,4,3,-6,10,-4,-3,-8,-4,10,7,-8,-5,-2,-10,-7,10,-4,1,-5,3,10,2,9,-4,9,8,-8,2,-2,-6,9,-10,1,3,2,5,-4,-4,3,3,-7,1,3,-5,6,-4,9,5,7,6,-4,3,-8,-2,-5,4,7,9,-7,-7,-8,-7,6,7,-2,7,5,-5,-9,5,1,5,-3,9,9,-6,-6,-5,6,10,-4,3,6,-2,4,-8,5,4,8,-1,-7,3,9,-8,10,3,2,3,6,3,-3,7,-4,9,4,8,-6,-5,-1,-9,10,6,2,1,7,1,7,-9,1,-1,-7,-6,-2,-7,5,-3,-10,6,8,-1,3,6,-10,-9,4,-5,10,3,4,4,-8,4,-6,1,10,-1,-3,-3,2,5,-5,-9,2,9,-2,3,2,9,10,3,1,2,-1,-7,8,-10,-2,10,-1,-10,-1,-4,-2,2,10,-1,7,4,-8,-2,-5,-1,-1,9,-9,-6,1,5,2,5,-1,2,-10,8,9,6,4,9,8,7,8,-8,-3,4,8,-9,4,1,-10,-3,10,-5,7,-10,-3,-2,2,1,3,-5,5,-2,-5,-4,-1,-6,-6,-5,-4,-10,6,9,4,-7,5,7,-4,-10,1,6,1,-5,2,2,7,-2,-5,-2,2,3,-1,-9,3,-4,3,8,-1,-9,-3,8,2,-4,10,4,-7,-9,-1,-3,-8,-9,-6,-5,10,-9,-4,6,6,4,7,-10,-9,3,9,-4,-3,-8,-2,10,-8,6], dtype = "int16")#candidate|3474|(2912,)|const|int16
const_3475 = relay.const(4.198062, dtype = "float32")#candidate|3475|()|const|float32
const_3476 = relay.const([-3.941777,-5.718601,9.985735,9.017988,2.350829,-6.395845,2.941254,-0.274643,-5.703481,2.325977,0.549138,4.311105,6.204303,-1.398315,0.073434,-6.164702,6.441063,-1.860486,9.685411,-1.725854,6.431673,6.971567,0.072130,8.803228,-7.419727,3.610795,-2.658854,-3.725342,1.440553,-4.334325,-4.995060,2.697478,5.684879,3.224960,1.680614,2.414423,-7.637733,0.111462,0.021560,-3.995887,0.042686,1.615297,-3.987141,2.260268,-9.843596,-9.393419,9.389131,8.367833,1.269279,3.485640,-6.489062,-4.307131,-8.130381,0.775786,-8.333267,9.864164,4.401909,0.402885,6.944414,-2.866420,-0.561052,-6.769884,-9.354933,4.325454,-8.052991,-2.304457,0.308213,-3.030292,-6.664061,5.104752,6.179084,-7.093410,8.245748,-1.104807,6.204256,7.801976,1.006336,6.928658,1.465345,0.986706,7.311710,-3.018402,-1.845422,-2.681404,-1.895230,4.335674,6.723204,0.385878,2.306569,7.687452,-6.904668,3.132533,-0.730342,1.241905,2.046318,-8.604038,-3.680570,7.737020,7.780222,3.700476,-1.997948,4.812469,-4.708215,-8.899127,-9.831605,-8.400144,-6.373877,-9.504874,-3.923970,-9.309106,-1.256846,4.538790,-0.996887,-3.773254,-3.806722,3.653907,-9.298241,-1.556643,9.616423,5.032738,-2.283177,-8.552873,0.845784,-3.132062,-0.199481,3.237160,5.583144,6.304709,4.941367,6.326703,1.680958,-4.881287,9.066460,8.066639,-7.510699,-0.547864,-0.840096,4.486664,2.148964,-1.638297,5.922021,-1.193939,-4.109117,-5.568687,6.052965,3.742123,-5.358085,7.236175,4.098270,5.607093,4.613580,-6.389343,-6.868927,8.038404,8.412309,-7.135884,9.422850,2.197542,-7.616740,4.065655,1.771940,4.439902,4.201329,8.775344,6.669346,-9.741495,-5.715756,-5.111042,-6.080295,-4.678075,1.110806,-7.692683,-0.975571,-0.051363,9.502152,-0.345008,0.658847,3.774238,-8.361034,2.347912,0.294872,-3.260796,-5.679281,-6.360832,-9.509461,7.541325,2.041903,-1.632183,6.335030,1.758752,9.567341,-1.909293,2.445877,8.580859,-1.661690,5.517581,-0.713741,-3.474652], dtype = "float32")#candidate|3476|(198,)|const|float32
call_3473 = relay.TupleGetItem(func_3173_call(relay.reshape(const_3474.astype('int16'), [13, 14, 16]), relay.reshape(const_3474.astype('int16'), [13, 14, 16]), relay.reshape(const_3475.astype('float32'), []), relay.reshape(const_3476.astype('float32'), [198,]), ), 4)
call_3477 = relay.TupleGetItem(func_3179_call(relay.reshape(const_3474.astype('int16'), [13, 14, 16]), relay.reshape(const_3474.astype('int16'), [13, 14, 16]), relay.reshape(const_3475.astype('float32'), []), relay.reshape(const_3476.astype('float32'), [198,]), ), 4)
func_2130_call = mod.get_global_var('func_2130')
func_2136_call = mutated_mod.get_global_var('func_2136')
const_3491 = relay.const([-8,-2,-5,10,4,-1,-8,-1,-7,4,6,3,-7,-4,2,4,2,-1,-4,10,-10,1,9,3,-4,10,-10,-3,1,7,-3,-5,7,-3,-9,-9,6,-9,1,-3,-8,-5,5,-7,-7,2,-7,6,-3,7,2,2,-7,4,-2,-4,-9,-1,9,1,-2,6,9,5,1,-5,9,2,8,-3,5,9,8,-8,-7,3,-3,-1,10,-4,10,-5,-5,-5,5,3,7,3,1,-2,-2,10,-3,8,8,8,1,7,10,-1,1,-4,6,-4,9,-7,-1,4,7,1,4,-1,3,-1,1,-8,5,-1,-9,8,-4,-9,-2,-1,7,-4,3,5,5,-7,-9,-9,8,5,-8,5,10,7,9,2,-3,-6,-2,-10,-9,5,3,4,5,-9,6,7,10,-7,3,4,6,2,-10,-6,9,-9,-7,-6,-6,-7,10,8,7,10,7,-8,3,2,2,2,-1,-4,8,3,6,4,-4,-8,8,-3,-2,-7,-10,-6,-6,4,3,-6,-9,-5,-8,10,3,-5,6,5,10,2,-10,-2,1,4,3,5,10,6,-10,4,-4,4,8,9,3,7,10,-10,5,-6,-7,-2,-2,-8,5,-6,10,1,9,-5,-1,-6,2,-3,1,7,10,-6,8,-5,-4,1,2,2,-2,-4,1,-6,-7,2,-8,-7,-8,3,4,8,10,2,1,-3,-2,8,8,-6,4,-4,-7,-3,3,1,-3,-5,-8,4,4,-4,6,-2,7,1,6,-4,-8,7,2,-7,7,-9,-1,-6,-2,-3,-4,5,1,-1,-3,1,1,-3,8,-7,3,1,10,-9,8,1,5,3,3,-6,-8,-10,-6,1,2,-8,5,7,5,-8,-9,6,6,-3,-3,7,-5,10,9,-5,1,-4,-1,10,10,-2,8,5,5,-4,7,8,10,3,-1,-10,2,-9,-8,2,8,7,9,-9,-9,1,-6,-8,-10,8,1,-6,-4,7,-5,-8,-2,8,-6,-6,-1,9,-7,-4,9,-10,9,-5,-2,-3,-3,1,-7,-5,-7,-7,9,4,4,4,-9,8,-2,-9,5,-3,-6,-2,-3,-7,9,9,-2,5,-10,-1,-3,4,-2,-2,-6,5,-1,-4,-7,7,5,-3,6,2,7,4,4,7,-3,-5,8,-1,-9,5,8,-2,-5,-9,-5,8,8,-3,-2,-10,-1,-3], dtype = "uint64")#candidate|3491|(448,)|const|uint64
const_3492 = relay.const([False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True], dtype = "bool")#candidate|3492|(2145,)|const|bool
const_3493 = relay.const([-9,6,-5,4,9,-6,2,-1,-5,10,-1,3,10,4,-8,2,2,-3,-6,2,6,-2,-3,-7,-8,-2,-3,-4,10,-6,1,-8,-5,3,7,-1,-1,-3,5,-3,-8,-4,10,3,-6,-10,6,1,8,-7,7,-10,-10,-5,5,-8,2,4,-7,-6,4,9,4,3,4,-9,-7,-1,3,2,5,1,-1,1,-1,-3,3,-7,4,2,-2,-10,1,-6,9,-4,-9,4,-9,-9,2,-7,6,3,-4,9,-6,-4,2,1,9,6,2,9,-4,4,-2,10,-3,-9,8,2,7,-10,6,-10,9,-5,7,2,10,-7,7,10,2,8,7,3,5,-3,-5,8,-1,6,-4,-9,-6,-9,-6,4,2,8,-1,-3,4,-1,-1,4,-3,1,-9,-4,-1,-10,5,4,6,-7,5,-5,-8,-2,7,-4,-6,-8,7,2,8,-4,-3,-10,-2,-6,-9,-10,9,-9,-5,9,-7,-8,10,2,-1,-10,-5,-5,-9,8,4,-6,-7,3,5,-5,6,7,-5,-3,5,3,6,-9,-1,-3,-4,-9,-4,-2,4,-3,5,6,1,8,-3,-10,-9,3,5,-6,-7,-9,-7,3,-2,-4,8,-7,-1,9,-4,-4,7,4,5,2,-4,2,3,5,-2,2,-8,3,2,5,8,-10,7,8,5,-4,2,-10,-3,-10,-5,7,1,-3,1,-10,9,5,-5,8,4,9,-9,-8,-6,-7,3,4,-3,7,-7,4,-7,2,3,-2,-3,10,-1,-2,1,8,5,-9,9,4,-3,3,-9,-3,-6,-1,7,-9,-4,-5,-2,10,-3,6,5,9,10,1,9,-4,-1,2,-10,6,3,8,4,-3,-7,8,-8,-1,1,8,7,2,10,-8,8,2,-7,7,10,-6,-8,10,-3,4,4,3,7,9,-3,6,3,3,10,-1,9,-9,4,-4,-2,-3,2,10,-3,-5,-8,-8,-10,-2,10,-3,1,-5,-3,3,9,4,6,-1,2,7,-8,10,-3,-10,-6,-1,7,1,9,5,-4,9,2,-8,5,-2,-10,3,-7,-8,6,-9,9,4,5,-4,-10,-8,-3,5,-4,1,3,9,6,2,-1,4,-10,6,10,6,-2,-10,-5,-3,4,-4,9,-5,-3,7,-8,3,-9,-5,10,-7,-10,-9,2,5,-7,2,-2,-1,6,10,8,1,-2,-8,-2,5,4,6,-6,-3,-7,1,2,8,-7,-1,2,4,-10,6,-7,-3,-5,-8,-9,-5,6,10,7,3,4,1,-5,10,7,-9,-7,7,1,-6,-6,9,-9,9,6,-10,-7,-8,5,-10,-6,-7,1,-6,1,3,4,-1,-10,9,-4,8,-9,4,4,6,-2,4,7,6,-3,7,-10,10,-7,-7,9,2,2,4,1,8,3,7,-4,-9,-9,-4,-5,2,-5,-4,-6,4,2,8,8,-7,9,-4,-6,-10,1,5,-10,7,5,2,8,1,-4,3,4,4,5,-6,2,5,10,9,-6,7,-10,5,5,-7,-3,-10,4,2,-3,-8,4,10,3,6,-8,1,4,-7,1,7,-6,-5,-2,-10,5,3,3,-5,-5,-6,-6,2,-4,-10,-2,-1,5,-3,-2,3,2,7,1,2,3,-2,8,10,2,-8,-6,-7,6,-7,2,6,-7,-1,-4,-6,-2,7,-2,-3,6,3,10,-2,-1,-5,-10,8,3,-8,4,-4,-4,-6,8,3,1,-6,7,9,7,-2,4,-4,1,4,8,10,8,8,-7,2,8,-3,5,6,6,9,-8,-9], dtype = "uint8")#candidate|3493|(672,)|const|uint8
call_3490 = relay.TupleGetItem(func_2130_call(relay.reshape(const_3491.astype('uint64'), [8, 7, 8]), relay.reshape(const_3491.astype('uint64'), [8, 7, 8]), relay.reshape(const_3492.astype('bool'), [2145,]), relay.reshape(const_3475.astype('uint8'), []), relay.reshape(const_3493.astype('uint8'), [672,]), ), 1)
call_3494 = relay.TupleGetItem(func_2136_call(relay.reshape(const_3491.astype('uint64'), [8, 7, 8]), relay.reshape(const_3491.astype('uint64'), [8, 7, 8]), relay.reshape(const_3492.astype('bool'), [2145,]), relay.reshape(const_3475.astype('uint8'), []), relay.reshape(const_3493.astype('uint8'), [672,]), ), 1)
output = relay.Tuple([call_3462,call_3470,call_3473,const_3474,const_3475,const_3476,call_3490,const_3491,const_3492,const_3493,])
output2 = relay.Tuple([call_3463,call_3471,call_3477,const_3474,const_3475,const_3476,call_3494,const_3491,const_3492,const_3493,])
func_3496 = relay.Function([], output)
mod['func_3496'] = func_3496
mod = relay.transform.InferType()(mod)
mutated_mod['func_3496'] = func_3496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3496_call = mutated_mod.get_global_var('func_3496')
call_3497 = func_3496_call()
output = call_3497
func_3498 = relay.Function([], output)
mutated_mod['func_3498'] = func_3498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3508 = relay.TupleGetItem(func_2535_call(), 0)
call_3509 = relay.TupleGetItem(func_2537_call(), 0)
func_2727_call = mod.get_global_var('func_2727')
func_2730_call = mutated_mod.get_global_var('func_2730')
var_3518 = relay.var("var_3518", dtype = "float32", shape = (624, 1))#candidate|3518|(624, 1)|var|float32
call_3517 = relay.TupleGetItem(func_2727_call(relay.reshape(var_3518.astype('float32'), [2, 312])), 1)
call_3519 = relay.TupleGetItem(func_2730_call(relay.reshape(var_3518.astype('float32'), [2, 312])), 1)
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_3523 = relay.TupleGetItem(func_3121_call(), 0)
call_3524 = relay.TupleGetItem(func_3123_call(), 0)
var_3530 = relay.var("var_3530", dtype = "float64", shape = (12, 11, 5))#candidate|3530|(12, 11, 5)|var|float64
bop_3531 = relay.left_shift(call_3523.astype('int8'), relay.reshape(var_3530.astype('int8'), relay.shape_of(call_3523))) # shape=(12, 11, 5)
bop_3534 = relay.left_shift(call_3524.astype('int8'), relay.reshape(var_3530.astype('int8'), relay.shape_of(call_3524))) # shape=(12, 11, 5)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_3552 = relay.TupleGetItem(func_2535_call(), 0)
call_3553 = relay.TupleGetItem(func_2537_call(), 0)
output = relay.Tuple([call_3508,call_3517,var_3518,bop_3531,call_3552,])
output2 = relay.Tuple([call_3509,call_3519,var_3518,bop_3534,call_3553,])
func_3558 = relay.Function([var_3518,var_3530,], output)
mod['func_3558'] = func_3558
mod = relay.transform.InferType()(mod)
mutated_mod['func_3558'] = func_3558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3558_call = mutated_mod.get_global_var('func_3558')
var_3560 = relay.var("var_3560", dtype = "float32", shape = (624, 1))#candidate|3560|(624, 1)|var|float32
var_3561 = relay.var("var_3561", dtype = "float64", shape = (12, 11, 5))#candidate|3561|(12, 11, 5)|var|float64
call_3559 = func_3558_call(var_3560,var_3561,)
output = call_3559
func_3562 = relay.Function([var_3560,var_3561,], output)
mutated_mod['func_3562'] = func_3562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_3619 = relay.TupleGetItem(func_3121_call(), 0)
call_3620 = relay.TupleGetItem(func_3123_call(), 0)
func_1320_call = mod.get_global_var('func_1320')
func_1323_call = mutated_mod.get_global_var('func_1323')
const_3622 = relay.const([6,10,10,-7,4,8,6,10,-4,-8,7,2,-10,-3,7,-6,1,-3,5,3,5,-3,-7,4,-9,-6,4,4,-4,-10,-2,-8,-2,3,2,7,1,-8,-3,8,7,-8,1,7,-8,8,3,2,-6,-5,5,6,3,2,10,-10,5,-8,-2,4,1,-2,10,2,-3,4,10,-3,8,9,-7,-3,-8,9,-5,10,6,10,7,2,8,5,-8,1,4,-3,10,3,8,-6,4,-9,-9,6,1,-4,-6,7,7,-1,9,-2,-2,6,9,-3,9,5,2,-4,1,-4,-6,10,-10,-6,7,-7,-5,8,-7,6,2,-4,5,9,-5,-1,-3,-6,-6,-3,2,-1,-5,10,-8,7,-10,-8,10,-8,-8,8,4,6,6,-2,-1,7,9,-7,-6,1,-9,10,4,-6,9,-6,8,2,3,-4,4,-10,9,-2,-6,-10,9,6,-7,8,8,8,7,-4,3,-5,-9,2,4,4,6,-5,-3,-8,5,6,-1,-1,-4,1,1,6,10,-10,1,-6,-8,-2,2,-3,8,-8,4,9,4,-7,5,7,-3,-2,2,1,-9,-3,5,-5,5,-3,-5,-9,2,6,-1,-5,-9,-9,6,-1,3,5,-9,-10,-8,-3,7,3,-10,-9,1,7,2,3,4,-5,7,4,2,10,8,4,5,-5,4,8,-9,-5,1,-2,-1,3,-7,-6,2,1,-9,-5,10,-1,-5,10,-6,-8,-5,3,7,4,2,5,5,-3,-10,-9,10,5,-3,-1,1,5,10,-2,3,-1,5,10,-3,-2,-3,3,3,9,4,4,-1,-3,-8,-8,-10,-7,-6,-7,-1,-1,-2,-8,-2,-2,8,6,-6,10,4,6,-10,3,1,6,8,6,2,4,10,-2,1,-8,7,-2,8,8,-10,-4,8,-5,-7,-6,-7,-5,-6,7,-5,6,-5,-4,4,-2,3,-7,8,-7,5,6,-4,8,9,9,8,-7,-2,7,5,4,5,-8,3,10,1,-7,6,-6,1,-1,1,-4,-1,2,-10,1,-8,-10,6,-9,7,-1,3,10,-3,3,-8,-8,7,4,-4,5,-6,3,7,7,9,-7,-3,6,-7,-9,-5,-4,7,-2,-3,-3,1,10,-7,2,-5,10,-7,6,-7,-10,2,-5,-2,-9,3,5,-7,4,2,-2,6,-6,10,6,7,-10], dtype = "uint16")#candidate|3622|(448,)|const|uint16
call_3621 = func_1320_call(relay.reshape(const_3622.astype('uint16'), [8, 14, 4]))
call_3623 = func_1320_call(relay.reshape(const_3622.astype('uint16'), [8, 14, 4]))
output = relay.Tuple([call_3619,call_3621,const_3622,])
output2 = relay.Tuple([call_3620,call_3623,const_3622,])
func_3634 = relay.Function([], output)
mod['func_3634'] = func_3634
mod = relay.transform.InferType()(mod)
mutated_mod['func_3634'] = func_3634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3634_call = mutated_mod.get_global_var('func_3634')
call_3635 = func_3634_call()
output = call_3635
func_3636 = relay.Function([], output)
mutated_mod['func_3636'] = func_3636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_3647 = relay.TupleGetItem(func_3121_call(), 0)
call_3648 = relay.TupleGetItem(func_3123_call(), 0)
output = call_3647
output2 = call_3648
func_3656 = relay.Function([], output)
mod['func_3656'] = func_3656
mod = relay.transform.InferType()(mod)
output = func_3656()
func_3657 = relay.Function([], output)
mutated_mod['func_3657'] = func_3657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3658 = relay.var("var_3658", dtype = "float32", shape = (3, 11, 12))#candidate|3658|(3, 11, 12)|var|float32
uop_3659 = relay.acos(var_3658.astype('float32')) # shape=(3, 11, 12)
output = uop_3659
output2 = uop_3659
func_3666 = relay.Function([var_3658,], output)
mod['func_3666'] = func_3666
mod = relay.transform.InferType()(mod)
mutated_mod['func_3666'] = func_3666
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3667 = relay.var("var_3667", dtype = "float32", shape = (3, 11, 12))#candidate|3667|(3, 11, 12)|var|float32
func_3666_call = mutated_mod.get_global_var('func_3666')
call_3668 = func_3666_call(var_3667)
output = call_3668
func_3669 = relay.Function([var_3667], output)
mutated_mod['func_3669'] = func_3669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3680 = relay.TupleGetItem(func_2994_call(), 0)
call_3681 = relay.TupleGetItem(func_2996_call(), 0)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3702 = relay.TupleGetItem(func_2994_call(), 0)
call_3703 = relay.TupleGetItem(func_2996_call(), 0)
output = relay.Tuple([call_3680,call_3702,])
output2 = relay.Tuple([call_3681,call_3703,])
func_3712 = relay.Function([], output)
mod['func_3712'] = func_3712
mod = relay.transform.InferType()(mod)
mutated_mod['func_3712'] = func_3712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mutated_mod.get_global_var('func_3712')
call_3713 = func_3712_call()
output = call_3713
func_3714 = relay.Function([], output)
mutated_mod['func_3714'] = func_3714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2752_call = mod.get_global_var('func_2752')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_3720 = relay.TupleGetItem(func_2752_call(), 0)
call_3721 = relay.TupleGetItem(func_2753_call(), 0)
func_3430_call = mod.get_global_var('func_3430')
func_3432_call = mutated_mod.get_global_var('func_3432')
var_3731 = relay.var("var_3731", dtype = "uint16", shape = (448,))#candidate|3731|(448,)|var|uint16
call_3730 = relay.TupleGetItem(func_3430_call(relay.reshape(var_3731.astype('uint16'), [448,])), 0)
call_3732 = relay.TupleGetItem(func_3432_call(relay.reshape(var_3731.astype('uint16'), [448,])), 0)
func_1204_call = mod.get_global_var('func_1204')
func_1207_call = mutated_mod.get_global_var('func_1207')
const_3736 = relay.const([True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True], dtype = "bool")#candidate|3736|(143,)|const|bool
var_3737 = relay.var("var_3737", dtype = "bool", shape = (2145,))#candidate|3737|(2145,)|var|bool
call_3735 = relay.TupleGetItem(func_1204_call(relay.reshape(const_3736.astype('bool'), [1, 11, 13]), relay.reshape(var_3737.astype('bool'), [15, 11, 13]), ), 0)
call_3738 = relay.TupleGetItem(func_1207_call(relay.reshape(const_3736.astype('bool'), [1, 11, 13]), relay.reshape(var_3737.astype('bool'), [15, 11, 13]), ), 0)
func_3430_call = mod.get_global_var('func_3430')
func_3432_call = mutated_mod.get_global_var('func_3432')
call_3747 = relay.TupleGetItem(func_3430_call(relay.reshape(var_3731.astype('uint16'), [448,])), 0)
call_3748 = relay.TupleGetItem(func_3432_call(relay.reshape(var_3731.astype('uint16'), [448,])), 0)
output = relay.Tuple([call_3720,call_3730,var_3731,call_3735,const_3736,var_3737,call_3747,])
output2 = relay.Tuple([call_3721,call_3732,var_3731,call_3738,const_3736,var_3737,call_3748,])
func_3750 = relay.Function([var_3731,var_3737,], output)
mod['func_3750'] = func_3750
mod = relay.transform.InferType()(mod)
mutated_mod['func_3750'] = func_3750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3750_call = mutated_mod.get_global_var('func_3750')
var_3752 = relay.var("var_3752", dtype = "uint16", shape = (448,))#candidate|3752|(448,)|var|uint16
var_3753 = relay.var("var_3753", dtype = "bool", shape = (2145,))#candidate|3753|(2145,)|var|bool
call_3751 = func_3750_call(var_3752,var_3753,)
output = call_3751
func_3754 = relay.Function([var_3752,var_3753,], output)
mutated_mod['func_3754'] = func_3754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3756 = relay.TupleGetItem(func_3046_call(), 0)
call_3757 = relay.TupleGetItem(func_3047_call(), 0)
output = call_3756
output2 = call_3757
func_3774 = relay.Function([], output)
mod['func_3774'] = func_3774
mod = relay.transform.InferType()(mod)
mutated_mod['func_3774'] = func_3774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3774_call = mutated_mod.get_global_var('func_3774')
call_3775 = func_3774_call()
output = call_3775
func_3776 = relay.Function([], output)
mutated_mod['func_3776'] = func_3776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3817 = relay.TupleGetItem(func_2994_call(), 0)
call_3818 = relay.TupleGetItem(func_2996_call(), 0)
output = relay.Tuple([call_3817,])
output2 = relay.Tuple([call_3818,])
func_3833 = relay.Function([], output)
mod['func_3833'] = func_3833
mod = relay.transform.InferType()(mod)
output = func_3833()
func_3834 = relay.Function([], output)
mutated_mod['func_3834'] = func_3834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3834_call = mutated_mod.get_global_var('func_3834')
call_3900 = relay.TupleGetItem(func_3833_call(), 0)
call_3901 = relay.TupleGetItem(func_3834_call(), 0)
output = relay.Tuple([call_3900,])
output2 = relay.Tuple([call_3901,])
func_3902 = relay.Function([], output)
mod['func_3902'] = func_3902
mod = relay.transform.InferType()(mod)
mutated_mod['func_3902'] = func_3902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3902_call = mutated_mod.get_global_var('func_3902')
call_3903 = func_3902_call()
output = call_3903
func_3904 = relay.Function([], output)
mutated_mod['func_3904'] = func_3904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3496_call = mod.get_global_var('func_3496')
func_3498_call = mutated_mod.get_global_var('func_3498')
call_3922 = relay.TupleGetItem(func_3496_call(), 6)
call_3923 = relay.TupleGetItem(func_3498_call(), 6)
var_3934 = relay.var("var_3934", dtype = "float64", shape = (5, 5, 13))#candidate|3934|(5, 5, 13)|var|float64
bop_3935 = relay.right_shift(call_3922.astype('uint16'), relay.reshape(var_3934.astype('uint16'), relay.shape_of(call_3922))) # shape=(5, 5, 13)
bop_3938 = relay.right_shift(call_3923.astype('uint16'), relay.reshape(var_3934.astype('uint16'), relay.shape_of(call_3923))) # shape=(5, 5, 13)
func_1659_call = mod.get_global_var('func_1659')
func_1664_call = mutated_mod.get_global_var('func_1664')
var_3943 = relay.var("var_3943", dtype = "uint16", shape = (24,))#candidate|3943|(24,)|var|uint16
var_3944 = relay.var("var_3944", dtype = "bool", shape = (2145,))#candidate|3944|(2145,)|var|bool
var_3945 = relay.var("var_3945", dtype = "uint16", shape = (4, 112))#candidate|3945|(4, 112)|var|uint16
call_3942 = relay.TupleGetItem(func_1659_call(relay.reshape(var_3943.astype('uint16'), [1, 4, 6]), relay.reshape(var_3944.astype('bool'), [2145,]), relay.reshape(var_3945.astype('uint16'), [448,]), ), 0)
call_3946 = relay.TupleGetItem(func_1664_call(relay.reshape(var_3943.astype('uint16'), [1, 4, 6]), relay.reshape(var_3944.astype('bool'), [2145,]), relay.reshape(var_3945.astype('uint16'), [448,]), ), 0)
func_3321_call = mod.get_global_var('func_3321')
func_3326_call = mutated_mod.get_global_var('func_3326')
var_3948 = relay.var("var_3948", dtype = "float32", shape = ())#candidate|3948|()|var|float32
const_3949 = relay.const([[-9.781284,-7.929429,6.481069,9.960643,4.911073,1.594138,-1.675906,-0.050771,-9.721026,1.418489,0.333580,0.749496,9.028408,3.367362,1.163052,3.266851,-7.828017,-0.673649,-8.046137,6.645353]], dtype = "float32")#candidate|3949|(1, 20)|const|float32
const_3950 = relay.const([4,-2,2,2,2,-2,-5,-8,-10,-7,8,2,1,2,-3,7,-4,-10,9,-6,-1,1,5,-6,-8,7,-3,7,2,1,-8,-5,-5,1,-6,-4,7,-4,7,-7,-3,4,5,3,-1,-5,1,3,4,2,3,6,3,2,1,8,-8,-3,-4,-10,-1,1,-4,7,-8,-7,-7,1,-4,2,6,1,-2,7,-1,8,4,3,6,8,-1,7,8,9,-4,-9,-1,-6,-7,9,-4,9,10,7,-5,4,-8,5,-2,7,-5,8,-7,1,9,-1,10,-10,5,8,10,8,-4,5,-9,-2,9,2,-4,9,4,-6,-1,7,-4,7,-9,-4,-10,-7,-1,3,8,-5,10,-8,5,1,10,3,-2,-8,5,-4,-10,4,-1,-3,-4,-3,-4,1,3,-7,-9,-7,-3,4,6,3,-10,-9,-5,9,-3,-4,-3,8,6,-1,8,-7,-2,10,-2,3,-1,-2,5,6,6,-4,-4,5,10,4,-3,-10,6,10,-5,10,5,2,5,-9,5,-10,-8,8,10,-7,-5,-7,-8,-10,1,-9,-4,-8,7,10,1,-1,-4,6,-3,4,-1,-10,7,2,-2,4,-3,2,10,-4,-1,-9,-5,6,7,7,-2,-6,9,-9,-2,6,7,-5,-2,-9,3,-8,2,-8,8,6,-2,-3,4,-1,-6,10,-7,-2,4,-1,-9,9,5,-2,-1,-2,-3,-6,-6,-3,-6,-8,10,1,3,-4,1,6,1,8,6,-6,5,-6,-1,-5,-4,1,3,1,-3,10,8,-9,-4,10,-7,9,-10,-4,5,-7,10,-4,-9,-1,-2,6,9,-9,-4,-2,-7,4,-7,-10,6,3,5,-1,4,9,-6,-6,-2,-7,5,-7,2,2,10,2,-9,-1,4,-1,7,4,4,-8,4,5,7,-2,3,-8,5,-8,7,-1,5,-9,1,-6,1,3,3,5,-10,-9,-2,-8,9,3,7,-6,7,5,-7,5,8,5,6,1,10,2,9,1,6,-3,-2,-7,4,-7,4,-1,1,-2,-8,4,-3,10,-6,1,8,7,2,-7,6,9,7,10,8,5,-7,3,-3,3,5,1,7,-3,2,7,-5,7,6,8,-1,9,-1,-9,7,-6,-5,8,-7,-1,1,8,-4,-8,4,4,10,-5,-6,-7,-8,7,-10,-3,6,-7,-2,4,9,4,-9,-1,2,10,-10,-2,8,2,-6,8,-9,-10,-9,6,-8,3,1,-4,10,2,1,-10,5,8,5,1,10,-6,8,10,4,-1,7,-9,-1,9,-7,10,1,1,-3,-1,-6,1,10,-9,-5,1,-10,-1,3,1,-10,-2,-9,6,-7,-5,5,10,7,10,-2,6,-5,-2,-10,8,6,-1,-5,6,-4,-7,-7,4,8,8,7,1,4,10,-8,1,2,-8,-1,-1,5,3,6,-8,3,2,1,-4,9,-6,-4,-1,-1,3,3,-6,-1,10,8,10,3,3,-7,6,1,-5,1,9,-6,3,-4,10,9,3,-8,-1,4,5,-9,1,3,4,3,5,8,9,-6,-7,8,4,-2,-9,7,10,-6,-7,-7,2,-6,9,6,6,-8,-9,-3,-4,-6,-1,-8,-10,-2,-3,9,6,4,-7,-5,2,-6,-10,4,5,-9,-4,9,-1,-2,-9,10,6,3,4,-8,9,-9,-6,3,4,10,-10,3,-10,-4,6,6,-9,9,5,10,-3,5,2,1,-1,-4,-9,-10,2,10,9,-3,-5,2,10,-5,10,2,-9,8,5,-1,-10,5,-7,1,-3,4,7,-9,7,9,6,-1,-6,5,4,-6,-6,-4,8,-9,-10,-8,-1,3,10,7,-5,1,9,3,-1,-8,1,-8,-9,-7,-1,7,1,10,-4,-7,7,-2,-3,2,5,-1,-3,-5,-5,1,-7,-8,10,10,-6,3,-7,4,2,-6,-5,5,-5,10,3,7,-10,8,4,-4,-9,6,3,-9,-5,4,-1,7,9,9,-1,-2,3,10,2,-10,2,6,-7,10,10,-1,1,1,7,2,6,8,-5,-9,-6,-9,-6,-2,2,4,-6,-4,-6,6,7,-3,3,-4,-2,7,-3,-6,3,-3,-10,6,-3,2,7,3,8,-7,-7,-1,-6,-7,-7,2,-1,-5,-2,-8,1,-2,-1,-2,-1,2,-2,7,3,10,8,-2,-5,-3,-5,-1,2,7,-8,-4,2,7,9,3,-1,-6,5,10,-2,-6,-6,5,2,-1,3,-1,1,8,-3,6,3,3,-7,-7,-7,-7,-2,3,4,-4,1,-3,-5,-4,1,-2,-9,4,9,-8,6,1,8,2,8,-1,3,-1,7,7,-3,-4,-4,-2,-2,1,-6,8,6,7,7,-3,4,-9,7,-8,-4,7,-3,-3,1,-6,6,-10,5,-6,-5,-5,1,9,1,-2,-10,-5,10,-1,-3,6,1,2,3,-10,-7,9,-10,-7,8,8,-6,2,-2,-7,-7,4,10,4,6,-4,-9,-2,-3,-2,6,-8,2,10,-2,10,-9,9,-4,3,-9,2,1,-8,3,-3,9,-3,3,6,-10,7,3,-1,1,7,-2,-9,-5,7,-5,6,4,-7,-3,-2], dtype = "int16")#candidate|3950|(975,)|const|int16
call_3947 = relay.TupleGetItem(func_3321_call(relay.reshape(var_3948.astype('float32'), []), relay.reshape(const_3949.astype('float32'), [2, 1, 10]), relay.reshape(const_3950.astype('int16'), [975,]), ), 3)
call_3951 = relay.TupleGetItem(func_3326_call(relay.reshape(var_3948.astype('float32'), []), relay.reshape(const_3949.astype('float32'), [2, 1, 10]), relay.reshape(const_3950.astype('int16'), [975,]), ), 3)
output = relay.Tuple([bop_3935,call_3942,var_3943,var_3944,var_3945,call_3947,var_3948,const_3949,const_3950,])
output2 = relay.Tuple([bop_3938,call_3946,var_3943,var_3944,var_3945,call_3951,var_3948,const_3949,const_3950,])
func_3953 = relay.Function([var_3934,var_3943,var_3944,var_3945,var_3948,], output)
mod['func_3953'] = func_3953
mod = relay.transform.InferType()(mod)
var_3954 = relay.var("var_3954", dtype = "float64", shape = (5, 5, 13))#candidate|3954|(5, 5, 13)|var|float64
var_3955 = relay.var("var_3955", dtype = "uint16", shape = (24,))#candidate|3955|(24,)|var|uint16
var_3956 = relay.var("var_3956", dtype = "bool", shape = (2145,))#candidate|3956|(2145,)|var|bool
var_3957 = relay.var("var_3957", dtype = "uint16", shape = (4, 112))#candidate|3957|(4, 112)|var|uint16
var_3958 = relay.var("var_3958", dtype = "float32", shape = ())#candidate|3958|()|var|float32
output = func_3953(var_3954,var_3955,var_3956,var_3957,var_3958,)
func_3959 = relay.Function([var_3954,var_3955,var_3956,var_3957,var_3958,], output)
mutated_mod['func_3959'] = func_3959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3634_call = mod.get_global_var('func_3634')
func_3636_call = mutated_mod.get_global_var('func_3636')
call_3961 = relay.TupleGetItem(func_3634_call(), 2)
call_3962 = relay.TupleGetItem(func_3636_call(), 2)
output = call_3961
output2 = call_3962
func_3963 = relay.Function([], output)
mod['func_3963'] = func_3963
mod = relay.transform.InferType()(mod)
mutated_mod['func_3963'] = func_3963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3963_call = mutated_mod.get_global_var('func_3963')
call_3964 = func_3963_call()
output = call_3964
func_3965 = relay.Function([], output)
mutated_mod['func_3965'] = func_3965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3902_call = mod.get_global_var('func_3902')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_4021 = relay.TupleGetItem(func_3902_call(), 0)
call_4022 = relay.TupleGetItem(func_3904_call(), 0)
var_4041 = relay.var("var_4041", dtype = "float32", shape = (5, 5, 13))#candidate|4041|(5, 5, 13)|var|float32
bop_4042 = relay.left_shift(call_4021.astype('uint32'), relay.reshape(var_4041.astype('uint32'), relay.shape_of(call_4021))) # shape=(5, 5, 13)
bop_4045 = relay.left_shift(call_4022.astype('uint32'), relay.reshape(var_4041.astype('uint32'), relay.shape_of(call_4022))) # shape=(5, 5, 13)
func_2176_call = mod.get_global_var('func_2176')
func_2178_call = mutated_mod.get_global_var('func_2178')
const_4050 = relay.const([6,5,-3,-5,-9,2,9,-8,-7,-4,-6,-8,2,1,2,-5,1,6,1,8,6,-5,-4,-10,4,10,10,4,-1,-7,5,1,4,-2,7,-6,10,10,8,4,3,-2,1,6,1,3,7,-5,-1,5,7,-3,-7,-10,2,-5,-10,-1,-2,-1,10,2,9,-6,4,-10,-5,7,-7,-4,-1,-5,7,1,3,-4,-9,-8,-4,1,-8,-9,6,-4,3,4,-9,4,-7,7,9,2,-8,6,-7,-9,8,7,-2,-8,10,-8,5,5,8,-1,-3,-5,-5,2,6,4,-7,-1,-3,5,-3,2,-8,-9,9,3,4,3,-7,-9,6,10,-6,4,9,3,-4,-1,2,-7,1,4,-10,-5,4,1,-9,3,1,7,7,-4,-6,1,5,10,-2,1,1,-8,-10,-5,9,6,-3,3,-2,-1,2,-6,-2,2,1,3,-7,-9,9,6,1,-9,5,-6,-9,-7,9,-9,-2,-4,-4,6,-9,10,10,7,8,-8,9,1,-1,8,-4,2,8,8,4,-3,3,-10,-1,-6,4,-3,-8,-9,-5,-10,6,4,5,-5,-7,3,-4,-3,-1,-6,-5,-5,5,3,-5,-8,2,-6,-3,-7,1,-10,-4,-2,4,-9,8,1,10,-3,6,7,-3,-6,-3,-7,-4,3,-2,4,-2,-4,-6,4,-10,2,-6,5,-9,-6,-3,-9,1,-6,7,-10,10,1,-2,4,2,9,3,7,-2,-6,-9,-1,-7,5,6,6,1,4,2,7,-3,2,-8,-10,4,-7,-3,5,-7,7,-8,-1,-8,-4,2,4,8,3,-5,-8,3,3,-6,-7,1,-6,6,-1,2,-5,-7,-2,-5,10,-2,-10,-4,10,-5,2,-2,8,6,10,-5,2,6,-6,1,-2,6,5,-6,7,3,-9,10,2,-7,3,9,-3,-1,7,-8,-4,-10,-2,5,8,-3,-4,-4,-8,-9,2,-8,7,7,3,1,-8,6,7,-3,1,6,6,2,-1,-5,-2,-10,-2,3,2,3,-4,2,-4,10,9,-3,-6,-9,9,-1,-6,-2,-10,6,-8,2,9,7,8,-1,3,-4,-10,-7,-8,1,-1,-4,7,-3,-10,9,10,5,3,-9,-1,-5,-7,-1,1,10,-7,3,4,-1,4,4,-5,-3,6,-7,4,-9,6,-7,3,9,4,4,-1,-2,4,-8,-6,1,5,-8,-2,2,-6,7,10,9,-9,10,9,-6,2,4,-6,-10,3,-2,7,-4,-4,-2,6,-8,8,8,2,10,7,1,-9,6,1,10,1,2,-5,-2,8,10,8,3,2,-3,9,4,-7,1,-8,5,-7,5,-1,-4,6,7,2,3,7,-4,-10,-6,9,-4,-10,-6,-7,-6,-7,1,6,7,-2,-1,6,5,4,-4,9,-9,10,4,6,10,-2,-7,9,-6,4,-9,-5,-8,-4,-1,2,-9,-5,2,5,-7,2,-5,7,3,-3,2,5,-6,-4,-1,8,9,-5,7,2,6,7,5,5,5,-10,-5,-7,-5,7,-7,6,-8,-10,10,8,-6,-7,7,10,-9,9,5,-4,-8,6,4,5,4,9,-9,-10,-10,-7,1,10,-8,-6,8,-5,1,-6,-7,8,-8,7,-2,2,6,-2,7,-8,3,-1,-4,-7,-2,-9,-6,2,2,9,10,7,-1,4,-10,-6,-4,4,-5,-2,-6,8,8,5,-1,5,6,-7,2,6,4,5,-8,8,9,-10,1,-6,8,-10,-6,2,6,8,3,-9,3,-4,2,6,-4,-6,-4,5], dtype = "int16")#candidate|4050|(672,)|const|int16
call_4049 = relay.TupleGetItem(func_2176_call(relay.reshape(const_4050.astype('int16'), [14, 12, 4])), 0)
call_4051 = relay.TupleGetItem(func_2178_call(relay.reshape(const_4050.astype('int16'), [14, 12, 4])), 0)
func_1204_call = mod.get_global_var('func_1204')
func_1207_call = mutated_mod.get_global_var('func_1207')
const_4053 = relay.const([True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False], dtype = "bool")#candidate|4053|(143,)|const|bool
const_4054 = relay.const([False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True], dtype = "bool")#candidate|4054|(2145,)|const|bool
call_4052 = relay.TupleGetItem(func_1204_call(relay.reshape(const_4053.astype('bool'), [1, 11, 13]), relay.reshape(const_4054.astype('bool'), [15, 11, 13]), ), 0)
call_4055 = relay.TupleGetItem(func_1207_call(relay.reshape(const_4053.astype('bool'), [1, 11, 13]), relay.reshape(const_4054.astype('bool'), [15, 11, 13]), ), 0)
output = relay.Tuple([bop_4042,call_4049,const_4050,call_4052,const_4053,const_4054,])
output2 = relay.Tuple([bop_4045,call_4051,const_4050,call_4055,const_4053,const_4054,])
func_4066 = relay.Function([var_4041,], output)
mod['func_4066'] = func_4066
mod = relay.transform.InferType()(mod)
var_4067 = relay.var("var_4067", dtype = "float32", shape = (5, 5, 13))#candidate|4067|(5, 5, 13)|var|float32
output = func_4066(var_4067)
func_4068 = relay.Function([var_4067], output)
mutated_mod['func_4068'] = func_4068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3963_call = mod.get_global_var('func_3963')
func_3965_call = mutated_mod.get_global_var('func_3965')
call_4073 = func_3963_call()
call_4074 = func_3963_call()
output = relay.Tuple([call_4073,])
output2 = relay.Tuple([call_4074,])
func_4086 = relay.Function([], output)
mod['func_4086'] = func_4086
mod = relay.transform.InferType()(mod)
output = func_4086()
func_4087 = relay.Function([], output)
mutated_mod['func_4087'] = func_4087
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4108 = relay.var("var_4108", dtype = "int32", shape = ())#candidate|4108|()|var|int32
var_4109 = relay.var("var_4109", dtype = "int32", shape = (3, 9, 9))#candidate|4109|(3, 9, 9)|var|int32
bop_4110 = relay.less(var_4108.astype('bool'), var_4109.astype('bool')) # shape=(3, 9, 9)
output = bop_4110
output2 = bop_4110
func_4133 = relay.Function([var_4108,var_4109,], output)
mod['func_4133'] = func_4133
mod = relay.transform.InferType()(mod)
var_4134 = relay.var("var_4134", dtype = "int32", shape = ())#candidate|4134|()|var|int32
var_4135 = relay.var("var_4135", dtype = "int32", shape = (3, 9, 9))#candidate|4135|(3, 9, 9)|var|int32
output = func_4133(var_4134,var_4135,)
func_4136 = relay.Function([var_4134,var_4135,], output)
mutated_mod['func_4136'] = func_4136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_4226 = func_2905_call()
call_4227 = func_2905_call()
output = call_4226
output2 = call_4227
func_4228 = relay.Function([], output)
mod['func_4228'] = func_4228
mod = relay.transform.InferType()(mod)
output = func_4228()
func_4229 = relay.Function([], output)
mutated_mod['func_4229'] = func_4229
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4266 = relay.var("var_4266", dtype = "int16", shape = (7, 15, 11))#candidate|4266|(7, 15, 11)|var|int16
var_4267 = relay.var("var_4267", dtype = "int16", shape = (7, 15, 11))#candidate|4267|(7, 15, 11)|var|int16
bop_4268 = relay.less_equal(var_4266.astype('bool'), relay.reshape(var_4267.astype('bool'), relay.shape_of(var_4266))) # shape=(7, 15, 11)
func_3321_call = mod.get_global_var('func_3321')
func_3326_call = mutated_mod.get_global_var('func_3326')
const_4278 = relay.const(-0.461705, dtype = "float32")#candidate|4278|()|const|float32
var_4279 = relay.var("var_4279", dtype = "float32", shape = (20,))#candidate|4279|(20,)|var|float32
const_4280 = relay.const([10,3,-8,7,9,-9,9,-2,5,-9,8,-3,-1,8,-2,5,9,-8,-6,4,4,-4,3,10,-8,10,-9,7,-9,-3,9,3,-8,6,-5,3,-8,-2,3,-8,1,10,-10,9,-9,-10,-2,8,-3,-8,-9,-8,6,-7,-4,-3,-2,4,-10,-1,7,7,6,1,-4,-8,10,9,9,-6,-10,7,-3,-3,-6,-2,-8,2,6,3,-4,4,-8,9,-10,2,5,-1,-2,1,-9,-1,-2,10,8,-2,4,-4,1,-4,10,1,7,6,-6,-7,2,1,3,-5,-3,-3,3,3,-3,-2,-3,10,7,-9,-7,-8,-4,-4,-8,-8,-6,-2,-8,-10,2,-4,7,6,4,-6,10,9,-3,-3,-1,-6,9,5,-2,8,9,2,-8,9,-2,2,-1,9,3,8,10,3,3,9,-5,1,1,-9,2,10,4,-9,2,-10,-10,2,-4,1,5,3,9,1,9,-8,7,-8,-1,-6,5,-1,-8,-6,8,-10,-9,10,-6,7,-10,-8,-6,-7,-3,1,3,-4,-5,-3,-10,-3,-3,9,3,-9,-5,-9,5,-8,-1,8,-1,4,3,-8,-8,5,3,5,2,-8,-10,7,-2,-4,6,-6,-4,-4,6,1,-2,-7,10,10,3,10,4,1,-4,7,-8,-6,3,-9,-1,-3,7,-7,-10,-1,-4,10,-10,-4,-9,2,-5,-10,-8,7,1,2,8,7,6,-4,-8,-10,7,-3,-8,4,3,2,-2,1,-9,-3,2,-6,7,3,-6,8,-9,-10,5,-10,5,-2,-3,2,7,8,7,-10,-5,4,5,5,-10,-1,-6,-5,-5,1,9,-7,-1,8,10,-4,2,-8,-9,-3,7,-6,-6,-5,-8,-8,-10,-5,-1,-10,-4,8,4,5,1,6,1,-1,3,-8,2,9,-1,6,-1,5,-3,-3,10,-2,-5,9,10,-5,-5,5,-6,-3,1,9,6,-9,-8,5,10,1,6,3,7,1,10,-3,-2,-3,8,7,9,-2,-10,-7,6,8,-5,10,-1,-7,-8,-7,-1,-3,6,2,8,4,-4,-8,8,-4,9,8,8,-10,8,-7,2,7,-2,3,4,7,8,-8,-1,9,8,-1,5,-3,3,-1,9,-2,10,10,3,-1,3,7,-4,6,-6,-10,-2,-3,2,9,5,-4,-9,8,-2,-4,10,8,10,10,3,-8,-3,-10,-8,-8,-10,-7,-7,-10,-5,1,-8,1,-3,7,-3,2,7,-2,-1,-9,5,2,2,-8,-8,2,7,3,4,-7,6,-4,-1,9,9,5,-5,-3,-8,-2,9,2,7,8,-7,10,-6,6,1,9,7,-1,10,-9,-4,-5,-7,10,4,7,5,-5,-2,-8,8,10,-1,8,-4,10,-10,-2,3,2,2,-7,7,-7,2,-1,-5,8,3,-9,-4,6,7,-2,-1,-8,-6,-9,-6,3,4,-10,6,-8,5,7,-8,5,2,-6,4,4,-8,2,-1,-3,8,5,3,-4,-1,-8,-5,-6,2,7,-7,-3,-4,-10,1,-2,-9,4,10,-2,10,-2,5,-9,-2,-1,7,-4,3,8,9,3,-6,-2,9,-7,-8,-4,-9,-9,1,-9,-6,-3,-9,2,-10,-6,4,-3,5,-1,-9,5,-8,-8,-4,1,-10,-10,-5,6,7,-10,-1,-3,-2,-7,-7,-8,5,-8,-3,-1,-1,-1,-3,-2,9,1,-6,4,7,9,-4,-3,-5,1,7,-2,-5,5,-9,8,8,10,4,-1,7,-6,-1,1,-7,-3,-4,-5,7,7,-8,8,4,1,1,-10,-4,-9,-5,-10,-3,-9,7,6,-5,-3,-9,10,-8,3,2,6,-10,-10,5,7,2,-5,-9,4,5,6,8,-9,-4,-6,6,4,-8,8,6,-1,1,-9,6,-4,-3,-7,6,-9,-8,1,-8,-1,1,10,-7,8,-9,-8,-10,-8,-5,-6,-10,-3,2,4,9,6,5,9,-1,9,2,4,10,-9,-4,-7,-9,-5,-6,-1,-4,-7,7,10,3,-5,-7,-8,-1,-3,1,-1,10,-1,5,-1,3,8,4,-5,7,1,-10,-10,-8,-8,-3,-1,-5,1,-6,-10,2,6,-8,-4,-4,-1,-8,7,-6,-4,2,-3,-8,8,7,-3,-10,7,-2,4,-8,2,6,1,-4,10,-10,4,7,2,-2,5,5,-9,-6,5,-8,9,8,-5,-5,-8,-7,-3,-6,10,-1,9,8,-5,3,-8,8,-4,-7,9,-1,9,1,2,-10,-5,-9,6,-6,-4,10,-7,-9,-7,9,2,-4,10,4,3,4,4,-4,-3,-3,7,-8,6,-7,-8,8,8,1,-5,10,1,-6,9,9,-10,8,-10,4,-4,6,9,1,5,-3,-9,10,9,8,8,10,10,5,-4,5,-2,-1,-6,-8,6,-3,6,-8,-9,-3,-2,5,2,-3,9,-6,10,1,2,6,1,-5,-3,2,-9,-1,1,-6,-5,1,8,6,7,-5,7,8,-3,6,8,-9,4,-10,3,-8,-5,-2,-6,-1,6,-3,7,4,8,5,-8,5,-2,7,-2,-4,3,10,-6,4,8,6,3,-5,-10,9,5,-9,10,4,2,9], dtype = "int16")#candidate|4280|(975,)|const|int16
call_4277 = relay.TupleGetItem(func_3321_call(relay.reshape(const_4278.astype('float32'), []), relay.reshape(var_4279.astype('float32'), [2, 1, 10]), relay.reshape(const_4280.astype('int16'), [975,]), ), 2)
call_4281 = relay.TupleGetItem(func_3326_call(relay.reshape(const_4278.astype('float32'), []), relay.reshape(var_4279.astype('float32'), [2, 1, 10]), relay.reshape(const_4280.astype('int16'), [975,]), ), 2)
func_180_call = mod.get_global_var('func_180')
func_182_call = mutated_mod.get_global_var('func_182')
var_4284 = relay.var("var_4284", dtype = "int8", shape = (567,))#candidate|4284|(567,)|var|int8
call_4283 = func_180_call(relay.reshape(var_4284.astype('int8'), [7, 9, 9]))
call_4285 = func_180_call(relay.reshape(var_4284.astype('int8'), [7, 9, 9]))
output = relay.Tuple([bop_4268,call_4277,const_4278,var_4279,const_4280,call_4283,var_4284,])
output2 = relay.Tuple([bop_4268,call_4281,const_4278,var_4279,const_4280,call_4285,var_4284,])
func_4296 = relay.Function([var_4266,var_4267,var_4279,var_4284,], output)
mod['func_4296'] = func_4296
mod = relay.transform.InferType()(mod)
var_4297 = relay.var("var_4297", dtype = "int16", shape = (7, 15, 11))#candidate|4297|(7, 15, 11)|var|int16
var_4298 = relay.var("var_4298", dtype = "int16", shape = (7, 15, 11))#candidate|4298|(7, 15, 11)|var|int16
var_4299 = relay.var("var_4299", dtype = "float32", shape = (20,))#candidate|4299|(20,)|var|float32
var_4300 = relay.var("var_4300", dtype = "int8", shape = (567,))#candidate|4300|(567,)|var|int8
output = func_4296(var_4297,var_4298,var_4299,var_4300,)
func_4301 = relay.Function([var_4297,var_4298,var_4299,var_4300,], output)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_4374 = relay.TupleGetItem(func_2994_call(), 0)
call_4375 = relay.TupleGetItem(func_2996_call(), 0)
output = call_4374
output2 = call_4375
func_4382 = relay.Function([], output)
mod['func_4382'] = func_4382
mod = relay.transform.InferType()(mod)
output = func_4382()
func_4383 = relay.Function([], output)
mutated_mod['func_4383'] = func_4383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_4473 = relay.TupleGetItem(func_3046_call(), 0)
call_4474 = relay.TupleGetItem(func_3047_call(), 0)
func_4133_call = mod.get_global_var('func_4133')
func_4136_call = mutated_mod.get_global_var('func_4136')
var_4476 = relay.var("var_4476", dtype = "int32", shape = ())#candidate|4476|()|var|int32
const_4477 = relay.const([[-3,-1,5,2,-3,-2,-6,2,3,10,8,1,-7,-2,10,4,6,4,-9,3,-9,-9,-3,6,9,-7,-1,6,9,10,-1,1,-2,-1,3,3,6,-8,2,-5,4,-5,-10,3,-10,1,9,-9,6,2,-1,-3,8,7,7,-9,4,6,-7,-7,1,-6,-7,9,-4,-5,7,-1,-9,-5,10,7,-9,10,-1,-3,-5,1,6,7,5,3,10,-7,2,-7,-7,8,9,-2,-5,1,5,-1,-3,9,2,2,-7,3,2,-4,6,4,10,-4,-10,4,-8,-6,-3,1,-8,7,1,-9,-2,3,-4,5,-3,-8,5,-8,-9,8,-1,7,-3,7,8,8,-8,10,-5,8,4,-3,-10,-4,5,-2,2,-8,-6,8,10,4,6,-3,-8,1,9,-1,-4,9,-6,8,2,10,10,4,5,-9,1,-3,3,1,9,10,-4,5,-9,7,-8,1,-6,-7,2,-3,7,4,-2,-9,-4,6,-9,-9,5,-2,-2,10,-8,8,-4,5,-6,3,-3,-1,-3,-6,-10,-1,-10,8,5,-9,-7,-5,5,-6,10,-3,2,-1,-2,7,3,-5,-10,4,-10,-10,-7,10,6,6,-5,-6,-2,-2,-5,4,-7,-10,1,6,-6,-8,3,8,-6]], dtype = "int32")#candidate|4477|(1, 243)|const|int32
call_4475 = func_4133_call(relay.reshape(var_4476.astype('int32'), []), relay.reshape(const_4477.astype('int32'), [3, 9, 9]), )
call_4478 = func_4133_call(relay.reshape(var_4476.astype('int32'), []), relay.reshape(const_4477.astype('int32'), [3, 9, 9]), )
const_4480 = relay.const([[[True,False,False,True,False,False,False,False,False],[True,False,True,False,False,True,False,True,False],[False,True,False,False,False,False,False,False,True],[False,True,False,False,True,False,False,False,False],[True,False,True,True,False,True,False,False,True],[True,False,True,True,False,False,False,True,False],[False,True,False,False,True,True,False,True,False],[False,False,False,False,True,True,True,False,True],[False,False,True,False,False,True,True,True,True]],[[True,True,False,True,False,True,True,False,False],[False,False,False,True,False,False,True,False,True],[False,False,True,True,False,True,False,False,True],[True,True,True,True,False,False,True,True,False],[True,False,False,True,True,False,True,False,False],[True,True,True,False,False,True,True,True,True],[True,False,False,False,True,True,True,False,False],[False,False,True,False,True,False,True,False,True],[True,False,True,False,True,False,True,False,False]],[[False,True,False,True,False,False,True,True,True],[True,False,False,True,False,False,False,True,True],[False,False,True,True,True,True,False,True,True],[True,False,True,True,False,False,True,False,True],[True,True,False,True,False,False,True,True,True],[True,False,False,False,False,False,True,False,True],[True,False,True,False,True,True,True,True,False],[True,False,False,False,False,True,False,True,False],[True,False,True,False,True,True,False,True,False]]], dtype = "bool")#candidate|4480|(3, 9, 9)|const|bool
bop_4481 = relay.mod(call_4475.astype('float32'), relay.reshape(const_4480.astype('float32'), relay.shape_of(call_4475))) # shape=(3, 9, 9)
bop_4484 = relay.mod(call_4478.astype('float32'), relay.reshape(const_4480.astype('float32'), relay.shape_of(call_4478))) # shape=(3, 9, 9)
func_2727_call = mod.get_global_var('func_2727')
func_2730_call = mutated_mod.get_global_var('func_2730')
const_4487 = relay.const([1.242200,-1.240984,4.864164,5.418372,-5.991056,1.721186,0.295955,-4.593532,-9.280582,-5.555749,2.865161,-0.860697,9.549882,7.261409,-7.471266,0.156415,-3.425434,8.713840,3.873537,0.343302,9.259085,5.323585,-3.472119,1.759294,-1.339799,0.895861,-9.246731,9.316283,9.531973,-4.495300,2.067920,6.095336,2.450673,9.303012,8.004555,-4.732189,1.964500,-5.127568,-9.642263,-3.543014,1.793463,-1.367967,-3.464978,8.055852,9.620063,6.323987,7.665098,-3.590413,6.145530,0.840672,5.323431,-1.097225,1.378679,-8.360424,-2.476044,-1.032489,-1.347084,7.396951,-0.020168,-2.308347,-4.048102,-3.039865,6.890668,-7.640294,-6.950439,2.075178,-4.614595,-6.855560,-2.433827,9.877107,-4.824941,-8.909589,-3.973881,6.313592,-5.584037,-6.981731,9.668306,-2.359408,-9.518208,5.695339,-6.367592,-1.537110,-3.620461,-0.675423,8.578322,-3.506503,-3.184634,-2.785986,-0.013203,9.336732,-4.195756,-3.648254,0.190308,-8.687448,5.330548,-1.213832,-6.653824,-0.008002,-2.262887,-7.021887,-6.011274,8.734314,8.483536,-7.802206,9.766034,6.119836,0.347649,2.985522,-0.941243,-2.684642,9.956025,-5.377509,3.328661,9.587470,4.463316,3.463100,-5.003947,-5.812811,1.663286,2.771526,1.132379,-2.339962,-3.714251,1.193527,4.815970,6.763459,-1.254477,-3.514431,-3.274233,5.382824,4.883225,-3.587482,1.504136,-2.373354,1.378922,1.882748,-2.215438,1.796300,4.535561,4.568927,0.062419,-5.458998,-7.063545,8.671158,-2.071093,5.884359,-2.178298,2.141851,-6.341023,-7.588185,3.698224,-4.061784,0.418046,9.158305,-3.070812,0.806675,2.101825,-9.425611,-5.723124,-7.227045,-3.789911,3.756837,6.788820,0.148057,-9.941982,2.968595,1.117619,0.749023,-1.732671,-0.419090,8.710242,-8.457430,9.775741,2.973225,-9.967384,-5.310143,6.754164,5.539000,-1.243641,-6.657854,-1.925942,-2.320445,-4.238915,-6.895806,-5.420042,3.476886,-5.449869,-1.862870,-7.495005,-1.780825,-5.193157,-0.084344,-9.104726,-1.702071,-9.133628,9.300443,5.971446,-5.413147,0.145245,-8.410079,8.627879,8.166010,9.783853,0.742308,5.319095,-3.511443,-8.523990,2.052700,0.942225,4.639262,8.858051,-7.989178,7.735719,-5.711546,-9.732423,-7.457748,-6.598535,2.476869,-7.521017,-0.588798,-5.273176,0.172468,6.996325,1.138065,-1.355047,-7.604207,8.114265,-3.612539,6.788054,8.692760,3.476895,-8.490096,-1.861087,9.286396,-8.474704,-0.760943,5.655423,-0.583433,8.842134,6.556835,-8.789426,6.806938,-5.254769,-3.792294,-0.606059,3.863610,-3.694252,8.749896,-6.164252,2.530377,-9.743014,6.557966,0.501524,-1.361827,-5.430004,-1.561856,7.445216,-8.578669,-9.719883,-8.947705,8.493483,-7.353030,0.619431,-7.483570,6.156032,-7.515042,4.956589,9.042274,9.102855,5.655113,0.926158,3.846819,5.974983,-9.735630,-2.208163,-4.428026,9.907637,9.005545,1.244156,-4.293232,0.703861,-1.600374,-9.415360,0.116202,-9.433528,8.867766,6.417843,-1.896261,8.678368,-2.800942,0.120162,1.605057,3.013286,5.201929,-6.639787,5.220202,0.190025,-9.884289,7.170935,4.275395,8.965184,9.300988,5.708492,8.606538,4.335367,7.228867,2.546047,6.422849,2.748023,8.783044,-2.472393,-3.781858,-1.887555,0.515318,-3.050278,9.474907,-1.921568,-2.589048,0.182371,-1.142577,8.522902,5.591339,-9.327778,-3.624735,-8.423918,9.768181,-3.022392,-8.434431,-2.999743,4.341406,-8.177993,-1.641263,4.668181,1.851334,0.777822,1.779483,0.538957,6.306840,9.661520,2.183013,6.520709,-7.967887,-5.756172,-8.190548,8.030880,-7.657229,7.067397,-4.785853,2.200041,1.226143,4.320055,-2.025899,1.615471,-2.160876,0.537221,-6.814312,-5.017485,-8.826769,2.362358,5.132781,-1.697945,9.886470,4.902228,5.146358,0.847976,8.535525,4.721137,9.206752,4.090058,-3.827308,4.863059,5.026589,5.869459,3.143634,-5.620840,0.815431,-3.710043,-6.899908,-3.153123,-2.675794,-0.896283,-0.867015,9.661056,0.331888,7.189015,0.126771,-4.258092,-2.995759,6.673939,5.109586,8.216128,-7.758621,7.930524,2.623821,-3.305567,3.117364,8.596521,4.942732,6.729812,0.974241,-8.395118,7.939538,8.014123,-8.252237,4.498979,-8.671118,2.448088,-9.010963,-4.674437,-3.654625,-5.667973,2.704372,-5.267259,-4.874870,6.348748,-0.973876,0.808394,3.110784,-1.479315,4.842754,1.068952,-0.494736,-6.034286,9.262985,-7.315607,-0.276840,9.422472,-3.772018,-8.624949,7.548255,-8.534144,4.304756,6.561440,-4.547866,-9.679079,-9.464955,6.966503,-9.955805,9.033474,-4.593964,-5.603983,-7.330175,8.353286,3.351199,-9.184608,7.842531,-8.930284,-5.066624,8.373127,9.840128,-7.882361,2.971351,-0.930770,9.051530,2.009469,5.291141,-1.620870,8.960917,-5.833102,6.735537,3.594995,3.363802,7.702509,-3.158147,-5.306076,0.245812,0.323960,4.929510,-5.091339,0.988419,-9.637344,5.823416,3.847715,-4.759000,1.263291,-5.422736,7.883893,4.371453,5.908253,5.222376,7.869592,-7.001544,-6.221381,7.719970,-0.540213,-0.413890,2.371983,-8.990946,9.492027,5.782279,-3.331670,6.204625,3.176975,6.440409,-6.992034,6.101328,5.666350,-4.222363,0.729133,-7.572360,9.856773,-4.673872,5.802340,7.442825,-0.869195,0.948812,-2.710177,-4.847993,0.503211,-3.075458,-8.696382,-6.049530,3.366009,1.354011,-7.761731,-4.782503,8.734555,-8.592024,6.624500,8.350262,-8.427159,2.498027,7.184947,7.180163,5.656005,3.252351,3.968615,9.847664,-4.448188,2.810781,-0.269643,-2.738031,-3.267586,-9.918685,-5.407509,8.374718,6.651767,1.093780,-8.973661,6.919265,-4.089863,-6.977033,-7.302494,-8.776572,-4.724031,1.182311,-9.538762,-7.441934,0.756666,-5.980334,-5.012345,-4.628380,-0.435803,9.488458,-3.634801,-1.071735,2.124796,-4.018854,-4.835806,-0.965698,-7.920062,-9.097787,-3.849929,-4.534892,5.497637,3.601364,-5.839912,6.532349,-4.996479,-5.038183,-4.299176,0.151038,1.646411,8.147648,6.396893,-9.788978,-6.527687,-8.271114,-5.825151,-3.405223,6.540711,3.784654,5.635161,0.668555,1.539690,8.598234,-3.177947,0.284122,-2.599477,-7.884997,9.397292,-9.588867,3.463092,-8.596481,3.286115,0.069412,-3.831352,-0.451954,-3.322526,5.233648,3.711545,6.504002,-6.861654,5.713837,0.216199,-5.703413,2.848728,-1.970515,1.707029,-1.728183,0.059389,0.263716,-7.635244,-9.524425,0.974486,9.256772,-7.410986,4.674361,5.919898,1.064884,-3.319121,2.631143,-0.620620,-3.349385], dtype = "float32")#candidate|4487|(624,)|const|float32
call_4486 = relay.TupleGetItem(func_2727_call(relay.reshape(const_4487.astype('float32'), [2, 312])), 1)
call_4488 = relay.TupleGetItem(func_2730_call(relay.reshape(const_4487.astype('float32'), [2, 312])), 1)
output = relay.Tuple([call_4473,var_4476,const_4477,bop_4481,call_4486,const_4487,])
output2 = relay.Tuple([call_4474,var_4476,const_4477,bop_4484,call_4488,const_4487,])
func_4489 = relay.Function([var_4476,], output)
mod['func_4489'] = func_4489
mod = relay.transform.InferType()(mod)
var_4490 = relay.var("var_4490", dtype = "int32", shape = ())#candidate|4490|()|var|int32
output = func_4489(var_4490)
func_4491 = relay.Function([var_4490], output)
mutated_mod['func_4491'] = func_4491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2060_call = mod.get_global_var('func_2060')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_4496 = relay.TupleGetItem(func_2060_call(), 0)
call_4497 = relay.TupleGetItem(func_2061_call(), 0)
func_2808_call = mod.get_global_var('func_2808')
func_2811_call = mutated_mod.get_global_var('func_2811')
const_4512 = relay.const(1, dtype = "uint8")#candidate|4512|()|const|uint8
var_4513 = relay.var("var_4513", dtype = "uint8", shape = (672, 1))#candidate|4513|(672, 1)|var|uint8
call_4511 = relay.TupleGetItem(func_2808_call(relay.reshape(const_4512.astype('uint8'), []), relay.reshape(var_4513.astype('uint8'), [672,]), ), 2)
call_4514 = relay.TupleGetItem(func_2811_call(relay.reshape(const_4512.astype('uint8'), []), relay.reshape(var_4513.astype('uint8'), [672,]), ), 2)
func_3558_call = mod.get_global_var('func_3558')
func_3562_call = mutated_mod.get_global_var('func_3562')
var_4525 = relay.var("var_4525", dtype = "float32", shape = (624,))#candidate|4525|(624,)|var|float32
const_4526 = relay.const([6.910059,5.965199,-3.093988,-2.008106,-6.581131,3.138120,5.925114,7.874301,8.999302,3.646457,2.290886,-0.490933,1.554997,-8.819112,8.998988,5.693013,0.760735,9.472653,3.572511,4.284955,2.738943,-2.477411,3.094530,4.961720,-5.237432,0.416749,7.742406,-7.628993,9.998481,1.766447,-4.241608,4.451746,3.352647,-8.304700,5.503853,4.423044,-0.540406,3.214658,2.125382,-9.996753,5.967534,0.870884,1.545129,8.440863,-1.764056,0.906499,4.868766,-9.426713,-7.841187,4.387744,-0.465851,-6.276514,2.887300,-8.412686,4.836804,-4.526623,-6.322101,0.749384,4.280532,-0.588778,6.402718,0.181701,7.382126,-1.475425,-5.547304,0.942296,-3.828001,8.243122,1.674417,-8.746343,-7.850797,-3.376777,-9.533073,0.589064,-8.927884,1.647611,1.633413,1.379556,-9.022959,-2.366837,1.213050,6.459149,-5.625908,7.668332,-9.552594,-1.677663,2.422749,8.012385,-8.325846,0.449630,-9.178644,-8.688479,7.661401,-7.596619,9.262024,-3.310614,-0.839541,-1.997817,-6.545697,4.088443,8.673426,-0.679667,-2.668227,-5.119577,-9.540096,0.216573,-3.625221,-2.919766,0.177190,3.422534,-0.870800,-8.563187,9.283602,8.301314,-5.318600,-8.862646,-6.186046,-0.842760,-3.890634,0.605061,4.016104,-9.643301,-1.514574,0.890300,3.980278,8.478285,8.655900,7.514438,-2.287697,-9.419256,7.658367,1.829761,2.534355,-6.337931,-7.355637,-4.846756,-3.842981,-4.741151,-1.903713,4.099960,-1.615052,8.369373,-6.895029,0.547152,8.468184,9.598309,-4.573568,-0.415024,0.588042,-8.223817,-9.210156,2.297379,1.618875,8.772599,3.599641,5.186488,5.727546,6.128504,2.409966,6.787563,2.077017,2.579344,8.922965,7.297311,-0.598377,-4.264962,1.747073,-2.285543,2.700566,-8.344863,-0.929163,7.259578,-3.260936,2.584984,9.320834,-5.754283,3.776923,-6.528461,1.202192,8.280665,8.330935,-5.401546,9.326286,5.891895,-5.000340,-9.034039,-3.706098,5.288238,-8.030751,-1.550939,8.424815,-3.924246,9.877062,7.687428,5.547685,-9.472870,-1.376081,4.199186,7.252405,2.402788,-4.104583,-0.983754,6.154904,6.984437,-4.031438,4.931612,-3.885672,9.043828,-9.293559,-4.291620,6.392360,7.437139,3.532731,-4.939676,3.383087,-7.948605,6.749056,-8.452813,-6.404554,-7.057037,-8.865910,-3.322302,-9.994310,-9.909005,-5.829594,-1.006999,3.963062,-6.715530,-9.831643,-9.197210,-5.559003,3.866051,9.813080,-1.478309,8.957057,0.118289,-1.615742,-2.726182,5.348171,9.913284,9.185579,4.709828,7.374014,4.419232,-9.177345,-7.910491,-0.357546,-0.825284,1.129437,-0.562793,-9.384013,-0.930738,0.502200,9.720802,1.633899,0.610519,-4.642489,-9.524230,-9.167147,2.744555,7.382495,3.509662,6.988812,0.455452,-7.948336,2.750059,4.689368,2.687920,-2.069278,9.943432,0.669557,-0.415763,-2.491023,-9.676710,-1.180482,3.765737,6.184707,3.930350,4.758737,4.832847,-7.464176,-9.232769,2.377194,4.297618,-5.629621,7.973673,4.263643,1.680379,-6.805200,-8.146554,7.277392,-1.791981,-2.902864,5.379742,8.607354,9.736454,8.827214,8.153315,1.792734,-2.238675,-0.128464,3.300008,1.494332,7.684329,-4.140287,-7.592399,2.985570,-5.104424,-1.948684,9.430671,8.511770,-9.021688,-4.160258,5.435733,-3.436654,2.955685,3.894307,-8.200979,6.543141,8.064521,4.774349,9.548670,-0.069017,-7.937757,2.340812,-7.952470,-0.783741,8.458867,6.499256,-4.897521,-7.963014,-6.470213,-8.984175,-8.959666,-1.280013,-6.352231,9.185419,-1.617781,8.669676,9.329539,7.697858,1.460926,-3.442545,-3.059487,1.852672,4.570460,0.056459,-8.836751,-7.932448,1.749575,-6.537025,-3.196360,-6.091892,8.647014,8.860418,-4.110034,1.790949,-3.498048,0.355314,3.651172,5.783438,-7.093900,-4.975097,-9.900507,-4.839362,2.703925,7.830426,-2.600872,-3.511884,-2.330177,-1.258154,-7.434471,-6.486312,9.147290,-1.852828,3.320755,8.909091,-3.615622,-2.591243,-0.090252,-2.732413,0.009382,3.005742,4.306447,5.927485,9.653891,5.010957,0.587219,-0.941543,2.824303,7.695965,-7.634811,-8.725308,-5.669564,-2.397813,8.820012,-2.748519,-5.677333,1.966408,-9.383765,3.365538,-7.227992,1.094444,5.342214,5.452678,-7.521203,4.626381,8.118675,4.373060,-1.337882,5.100657,1.882106,-4.399141,8.111370,0.421423,-7.722772,-8.929034,2.278854,9.436589,0.022958,2.507424,3.758316,0.907889,3.563586,6.018158,-4.034168,1.685182,-8.962361,3.558696,6.309445,5.979265,-0.893584,8.784854,-5.111414,-4.508000,3.258582,5.874856,-0.485059,2.631083,-3.848893,2.064874,0.321347,-1.065014,-2.320836,-9.944029,-0.803245,0.563754,1.144493,8.288511,2.902820,3.059037,2.492706,-3.622346,8.754988,8.493304,-6.113983,-8.621685,-1.316241,1.561390,5.904417,-9.204606,-6.542442,-2.274402,-0.598170,9.193674,9.282298,-5.192415,3.818460,-6.729360,3.216953,-5.229480,-1.052954,8.799110,4.897934,5.479110,-7.936513,4.588587,8.326327,-4.567268,7.040835,-6.849272,2.020097,7.720795,2.673431,9.030137,-8.930730,-6.441427,7.950557,4.945391,-2.162518,6.297172,-5.698991,4.349410,-9.025863,-7.858027,3.960413,-2.236757,4.186782,-7.077972,3.915732,9.311908,5.430977,-6.221868,-0.726369,-8.896757,-3.119724,8.634260,-3.550632,-1.973348,5.073254,-5.656973,2.085771,6.105556,-1.681118,7.672831,8.614178,0.609406,-2.247597,1.531525,5.509712,-2.960005,8.527051,5.251701,-4.817965,-3.019474,-3.238891,6.366280,6.978092,-2.524739,-9.002483,7.351727,5.216733,-9.753552,-7.936467,-2.212377,0.463014,0.825873,-6.464807,-9.621743,1.158274,-0.527676,4.770202,3.968741,-3.466024,3.386816,-6.526385,1.245222,0.923978,6.973922,9.857731,-0.266559,-0.171894,-9.676765,-3.745720,-8.857972,5.366997,5.591878,-8.328713,-3.394915,-8.643468,8.776667,-1.040830,-2.877535,-1.102391,-5.292798,9.458238,4.882420,-7.317444,7.866106,-1.165168,-1.602026,-3.759717,7.068088,5.833716,-4.892498,4.355399,-9.455258,-5.553884,5.906157,-9.842034,-5.991171,-6.921375,-7.068947,7.663803,3.567101,9.743537,-5.511729,4.109582,-2.361966,1.960206,4.879242,-3.446494,-9.288984,-7.839667,7.531830,0.237482,8.562003,5.089595,9.391278,3.789560,0.015287,-2.795337,-4.507955,2.006971,-2.994315,9.434978,0.488453,7.795914,-2.908503,6.706553,2.821322,-4.857682,6.538944,-1.232131,-5.287841,1.463836,-6.156294,8.286674,-1.088838,6.916374,0.611174,-3.217955,-8.404914,9.969656,6.370065,-1.499830,1.979534,5.883618,1.406281,9.482562,1.635091,3.820713,7.416506,7.396010,2.387367,-0.706414,6.792333,3.313264,1.088747,0.582441,1.755798,6.966321,-0.026988,3.523328,-4.270251,9.173388,-6.286986,7.626676,-7.727987,9.937390,7.881725,-3.284487,-0.775341,-3.157333,-2.887039,-0.230294,0.103283,6.845955,2.226912,6.547690], dtype = "float64")#candidate|4526|(660,)|const|float64
call_4524 = relay.TupleGetItem(func_3558_call(relay.reshape(var_4525.astype('float32'), [624, 1]), relay.reshape(const_4526.astype('float64'), [12, 11, 5]), ), 1)
call_4527 = relay.TupleGetItem(func_3562_call(relay.reshape(var_4525.astype('float32'), [624, 1]), relay.reshape(const_4526.astype('float64'), [12, 11, 5]), ), 1)
bop_4544 = relay.left_shift(const_4512.astype('uint32'), call_4524.astype('uint32')) # shape=(2, 312)
bop_4547 = relay.left_shift(const_4512.astype('uint32'), call_4527.astype('uint32')) # shape=(2, 312)
uop_4559 = relay.acosh(call_4524.astype('float32')) # shape=(2, 312)
uop_4561 = relay.acosh(call_4527.astype('float32')) # shape=(2, 312)
var_4565 = relay.var("var_4565", dtype = "float32", shape = (2, 312))#candidate|4565|(2, 312)|var|float32
bop_4566 = relay.mod(uop_4559.astype('float32'), relay.reshape(var_4565.astype('float32'), relay.shape_of(uop_4559))) # shape=(2, 312)
bop_4569 = relay.mod(uop_4561.astype('float32'), relay.reshape(var_4565.astype('float32'), relay.shape_of(uop_4561))) # shape=(2, 312)
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_4572 = relay.TupleGetItem(func_3046_call(), 0)
call_4573 = relay.TupleGetItem(func_3047_call(), 0)
uop_4575 = relay.asin(bop_4566.astype('float32')) # shape=(2, 312)
uop_4577 = relay.asin(bop_4569.astype('float32')) # shape=(2, 312)
output = relay.Tuple([call_4496,call_4511,var_4513,var_4525,const_4526,bop_4544,call_4572,uop_4575,])
output2 = relay.Tuple([call_4497,call_4514,var_4513,var_4525,const_4526,bop_4547,call_4573,uop_4577,])
func_4585 = relay.Function([var_4513,var_4525,var_4565,], output)
mod['func_4585'] = func_4585
mod = relay.transform.InferType()(mod)
var_4586 = relay.var("var_4586", dtype = "uint8", shape = (672, 1))#candidate|4586|(672, 1)|var|uint8
var_4587 = relay.var("var_4587", dtype = "float32", shape = (624,))#candidate|4587|(624,)|var|float32
var_4588 = relay.var("var_4588", dtype = "float32", shape = (2, 312))#candidate|4588|(2, 312)|var|float32
output = func_4585(var_4586,var_4587,var_4588,)
func_4589 = relay.Function([var_4586,var_4587,var_4588,], output)
mutated_mod['func_4589'] = func_4589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3341_call = mod.get_global_var('func_3341')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_4609 = relay.TupleGetItem(func_3341_call(), 0)
call_4610 = relay.TupleGetItem(func_3342_call(), 0)
output = relay.Tuple([call_4609,])
output2 = relay.Tuple([call_4610,])
func_4639 = relay.Function([], output)
mod['func_4639'] = func_4639
mod = relay.transform.InferType()(mod)
output = func_4639()
func_4640 = relay.Function([], output)
mutated_mod['func_4640'] = func_4640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4382_call = mod.get_global_var('func_4382')
func_4383_call = mutated_mod.get_global_var('func_4383')
call_4781 = func_4382_call()
call_4782 = func_4382_call()
func_2060_call = mod.get_global_var('func_2060')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_4796 = relay.TupleGetItem(func_2060_call(), 0)
call_4797 = relay.TupleGetItem(func_2061_call(), 0)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_4807 = relay.TupleGetItem(func_2494_call(), 1)
call_4808 = relay.TupleGetItem(func_2496_call(), 1)
output = relay.Tuple([call_4781,call_4796,call_4807,])
output2 = relay.Tuple([call_4782,call_4797,call_4808,])
func_4823 = relay.Function([], output)
mod['func_4823'] = func_4823
mod = relay.transform.InferType()(mod)
mutated_mod['func_4823'] = func_4823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4823_call = mutated_mod.get_global_var('func_4823')
call_4824 = func_4823_call()
output = call_4824
func_4825 = relay.Function([], output)
mutated_mod['func_4825'] = func_4825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_4842 = relay.TupleGetItem(func_4639_call(), 0)
call_4843 = relay.TupleGetItem(func_4640_call(), 0)
func_3496_call = mod.get_global_var('func_3496')
func_3498_call = mutated_mod.get_global_var('func_3498')
call_4853 = relay.TupleGetItem(func_3496_call(), 3)
call_4854 = relay.TupleGetItem(func_3498_call(), 3)
func_3341_call = mod.get_global_var('func_3341')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_4855 = relay.TupleGetItem(func_3341_call(), 0)
call_4856 = relay.TupleGetItem(func_3342_call(), 0)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_4865 = func_2905_call()
call_4866 = func_2905_call()
func_4489_call = mod.get_global_var('func_4489')
func_4491_call = mutated_mod.get_global_var('func_4491')
const_4873 = relay.const(-5, dtype = "int32")#candidate|4873|()|const|int32
call_4872 = relay.TupleGetItem(func_4489_call(relay.reshape(const_4873.astype('int32'), [])), 5)
call_4874 = relay.TupleGetItem(func_4491_call(relay.reshape(const_4873.astype('int32'), [])), 5)
func_180_call = mod.get_global_var('func_180')
func_182_call = mutated_mod.get_global_var('func_182')
const_4881 = relay.const([7,-4,7,6,-2,10,3,-1,-9,3,6,4,4,3,4,-5,-3,7,-2,5,-6,-7,-6,-7,-1,10,2,9,5,-1,5,10,-4,-7,10,10,6,6,8,-6,8,6,-1,3,-8,-7,-2,-2,-3,-3,-2,10,-10,9,-4,9,-2,-9,2,1,8,-5,-4,-7,6,2,4,-6,-10,4,-10,5,8,3,8,1,1,-8,-5,-1,-6,-8,5,-5,-9,-9,2,8,-8,3,6,-3,2,-1,-8,-7,-5,5,9,5,10,6,9,-5,7,-4,2,10,-1,-10,-3,-3,3,8,-9,1,-8,3,-1,4,-4,2,10,-1,-3,9,-9,-4,-2,6,7,1,4,-3,-2,-4,-9,-4,8,-9,-6,9,-3,-8,5,-6,-9,10,-3,-10,-1,-3,1,-7,-1,-2,-5,2,3,-2,-2,-3,-9,8,-5,9,3,4,9,4,10,-9,-8,4,1,-2,-6,7,7,7,4,-7,10,-4,5,-3,6,1,-4,-3,-10,-1,-9,10,-4,9,-5,-6,10,-5,7,-1,1,5,4,2,5,10,2,4,-9,5,-9,-8,-8,-5,1,8,-5,-7,4,-5,-5,-7,-5,2,-3,-7,-7,-3,-9,9,-4,4,-3,2,-2,-8,-10,-3,-3,-8,-1,1,9,2,4,-8,2,10,2,-3,-7,-1,-4,-3,-9,-5,5,8,-10,1,-4,2,10,-1,2,-9,3,-5,4,5,-8,-6,4,6,-6,10,6,8,-2,8,-3,2,-7,-4,-6,8,9,8,10,9,-10,8,9,-2,4,-4,7,4,2,6,-7,3,-8,9,-4,4,9,10,7,-10,1,10,9,-1,2,-10,-4,4,3,-10,4,-5,-7,1,-6,-6,5,7,10,5,-5,-10,10,-1,-7,-4,-6,-4,-3,-6,7,7,10,6,-2,-1,-7,-8,-4,2,1,-2,2,-9,-2,3,8,1,-6,9,9,-6,2,-5,-2,-8,2,9,6,8,-4,-9,-5,-2,7,-8,1,3,6,10,5,-3,7,-1,-2,3,2,-8,-4,5,-4,-8,-6,10,10,-2,-7,-2,-8,9,1,-8,6,7,8,1,-6,-7,-3,4,7,8,2,-10,2,4,1,-4,8,7,7,8,-9,6,3,5,8,6,3,2,-5,-7,-8,5,6,2,2,-7,-6,-4,2,1,-3,10,4,1,10,-6,-1,-2,5,-8,-3,-7,-7,8,-10,-9,-7,-9,3,-2,10,-9,1,5,5,-2,-10,7,-1,7,3,6,-5,3,-7,-8,3,5,9,9,-7,4,1,3,6,3,5,1,4,-5,9,5,1,7,4,-7,8,-6,-1,-8,10,6,1,-3,-1,4,-4,-5,1,-6,-9,-5,4,-5,2,-4,7,10,-9,-10,3,-4,3,1,-1,-10,-2,7,-8,-5,-8,-7,-2,2,9,-4,6,-9,-7,-4,9,-9,10,-9,10,1,4,2,4,-7,-6,5,-9,10,5,4,-1,-7,1,-1,9,-9,-9], dtype = "int8")#candidate|4881|(567,)|const|int8
call_4880 = func_180_call(relay.reshape(const_4881.astype('int8'), [7, 9, 9]))
call_4882 = func_180_call(relay.reshape(const_4881.astype('int8'), [7, 9, 9]))
func_4585_call = mod.get_global_var('func_4585')
func_4589_call = mutated_mod.get_global_var('func_4589')
var_4890 = relay.var("var_4890", dtype = "uint8", shape = (672,))#candidate|4890|(672,)|var|uint8
call_4889 = relay.TupleGetItem(func_4585_call(relay.reshape(var_4890.astype('uint8'), [672, 1]), relay.reshape(call_4872.astype('float32'), [624,]), relay.reshape(call_4872.astype('float32'), [2, 312]), ), 2)
call_4891 = relay.TupleGetItem(func_4589_call(relay.reshape(var_4890.astype('uint8'), [672, 1]), relay.reshape(call_4872.astype('float32'), [624,]), relay.reshape(call_4872.astype('float32'), [2, 312]), ), 2)
func_1804_call = mod.get_global_var('func_1804')
func_1809_call = mutated_mod.get_global_var('func_1809')
var_4898 = relay.var("var_4898", dtype = "uint16", shape = (448,))#candidate|4898|(448,)|var|uint16
const_4899 = relay.const([True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False], dtype = "bool")#candidate|4899|(143,)|const|bool
call_4897 = relay.TupleGetItem(func_1804_call(relay.reshape(const_4873.astype('uint8'), []), relay.reshape(var_4898.astype('uint16'), [448,]), relay.reshape(const_4899.astype('bool'), [13, 11]), ), 6)
call_4900 = relay.TupleGetItem(func_1809_call(relay.reshape(const_4873.astype('uint8'), []), relay.reshape(var_4898.astype('uint16'), [448,]), relay.reshape(const_4899.astype('bool'), [13, 11]), ), 6)
bop_4902 = relay.minimum(const_4899.astype('float32'), call_4889.astype('float32')) # shape=(672, 143)
bop_4905 = relay.minimum(const_4899.astype('float32'), call_4891.astype('float32')) # shape=(672, 143)
output = relay.Tuple([call_4842,call_4853,call_4855,call_4865,call_4872,const_4873,call_4880,const_4881,var_4890,call_4897,var_4898,bop_4902,])
output2 = relay.Tuple([call_4843,call_4854,call_4856,call_4866,call_4874,const_4873,call_4882,const_4881,var_4890,call_4900,var_4898,bop_4905,])
func_4918 = relay.Function([var_4890,var_4898,], output)
mod['func_4918'] = func_4918
mod = relay.transform.InferType()(mod)
mutated_mod['func_4918'] = func_4918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4918_call = mutated_mod.get_global_var('func_4918')
var_4920 = relay.var("var_4920", dtype = "uint8", shape = (672,))#candidate|4920|(672,)|var|uint8
var_4921 = relay.var("var_4921", dtype = "uint16", shape = (448,))#candidate|4921|(448,)|var|uint16
call_4919 = func_4918_call(var_4920,var_4921,)
output = call_4919
func_4922 = relay.Function([var_4920,var_4921,], output)
mutated_mod['func_4922'] = func_4922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4937 = relay.var("var_4937", dtype = "float32", shape = (10, 14, 16))#candidate|4937|(10, 14, 16)|var|float32
uop_4938 = relay.sigmoid(var_4937.astype('float32')) # shape=(10, 14, 16)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_4950 = func_2905_call()
call_4951 = func_2905_call()
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_4963 = relay.TupleGetItem(func_3121_call(), 0)
call_4964 = relay.TupleGetItem(func_3123_call(), 0)
uop_4976 = relay.erf(uop_4938.astype('float64')) # shape=(10, 14, 16)
output = relay.Tuple([call_4950,call_4963,uop_4976,])
output2 = relay.Tuple([call_4951,call_4964,uop_4976,])
func_4986 = relay.Function([var_4937,], output)
mod['func_4986'] = func_4986
mod = relay.transform.InferType()(mod)
var_4987 = relay.var("var_4987", dtype = "float32", shape = (10, 14, 16))#candidate|4987|(10, 14, 16)|var|float32
output = func_4986(var_4987)
func_4988 = relay.Function([var_4987], output)
mutated_mod['func_4988'] = func_4988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_5019 = relay.TupleGetItem(func_2994_call(), 0)
call_5020 = relay.TupleGetItem(func_2996_call(), 0)
output = call_5019
output2 = call_5020
func_5039 = relay.Function([], output)
mod['func_5039'] = func_5039
mod = relay.transform.InferType()(mod)
output = func_5039()
func_5040 = relay.Function([], output)
mutated_mod['func_5040'] = func_5040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4823_call = mod.get_global_var('func_4823')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_5041 = relay.TupleGetItem(func_4823_call(), 0)
call_5042 = relay.TupleGetItem(func_4825_call(), 0)
output = relay.Tuple([call_5041,])
output2 = relay.Tuple([call_5042,])
func_5050 = relay.Function([], output)
mod['func_5050'] = func_5050
mod = relay.transform.InferType()(mod)
output = func_5050()
func_5051 = relay.Function([], output)
mutated_mod['func_5051'] = func_5051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_5068 = relay.TupleGetItem(func_2535_call(), 0)
call_5069 = relay.TupleGetItem(func_2537_call(), 0)
func_3902_call = mod.get_global_var('func_3902')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_5081 = relay.TupleGetItem(func_3902_call(), 0)
call_5082 = relay.TupleGetItem(func_3904_call(), 0)
output = relay.Tuple([call_5068,call_5081,])
output2 = relay.Tuple([call_5069,call_5082,])
func_5083 = relay.Function([], output)
mod['func_5083'] = func_5083
mod = relay.transform.InferType()(mod)
output = func_5083()
func_5084 = relay.Function([], output)
mutated_mod['func_5084'] = func_5084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2752_call = mod.get_global_var('func_2752')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_5177 = relay.TupleGetItem(func_2752_call(), 0)
call_5178 = relay.TupleGetItem(func_2753_call(), 0)
output = relay.Tuple([call_5177,])
output2 = relay.Tuple([call_5178,])
func_5182 = relay.Function([], output)
mod['func_5182'] = func_5182
mod = relay.transform.InferType()(mod)
mutated_mod['func_5182'] = func_5182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5183 = func_5182_call()
output = call_5183
func_5184 = relay.Function([], output)
mutated_mod['func_5184'] = func_5184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_5206 = relay.TupleGetItem(func_2494_call(), 2)
call_5207 = relay.TupleGetItem(func_2496_call(), 2)
output = call_5206
output2 = call_5207
func_5227 = relay.Function([], output)
mod['func_5227'] = func_5227
mod = relay.transform.InferType()(mod)
mutated_mod['func_5227'] = func_5227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5227_call = mutated_mod.get_global_var('func_5227')
call_5228 = func_5227_call()
output = call_5228
func_5229 = relay.Function([], output)
mutated_mod['func_5229'] = func_5229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4382_call = mod.get_global_var('func_4382')
func_4383_call = mutated_mod.get_global_var('func_4383')
call_5244 = func_4382_call()
call_5245 = func_4382_call()
output = call_5244
output2 = call_5245
func_5252 = relay.Function([], output)
mod['func_5252'] = func_5252
mod = relay.transform.InferType()(mod)
mutated_mod['func_5252'] = func_5252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5252_call = mutated_mod.get_global_var('func_5252')
call_5253 = func_5252_call()
output = call_5253
func_5254 = relay.Function([], output)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_5271 = relay.TupleGetItem(func_2535_call(), 0)
call_5272 = relay.TupleGetItem(func_2537_call(), 0)
func_4133_call = mod.get_global_var('func_4133')
func_4136_call = mutated_mod.get_global_var('func_4136')
const_5320 = relay.const(-9, dtype = "int32")#candidate|5320|()|const|int32
const_5321 = relay.const([4,2,-7,-7,-7,4,-5,8,-2,-8,-3,4,9,9,8,-6,-1,-4,-9,-9,8,-2,8,6,3,10,-6,-7,6,5,-7,-8,9,-7,3,-5,-1,5,-8,-1,6,-7,6,9,8,-7,5,5,9,6,-10,-4,-9,10,1,6,-3,-10,-7,-2,-3,3,-6,5,2,9,2,5,-4,7,-8,-5,-8,-1,-3,1,2,7,-2,-7,-4,8,-2,7,8,3,9,-9,4,3,1,-5,-7,4,5,-4,10,4,5,-9,-7,10,-2,-4,-7,4,-2,2,3,9,-9,-6,-6,-10,4,-5,6,7,-4,-4,10,10,1,1,10,-2,4,-8,10,3,-1,-3,4,3,-10,1,-7,2,-5,-1,-5,-5,-3,-1,-3,9,1,-9,1,-4,-2,-3,-8,-8,9,7,4,-5,7,4,-8,-5,2,-7,9,7,8,10,-8,8,-8,3,9,3,-4,7,7,-3,8,-3,1,6,-2,5,5,-7,-8,-8,-8,2,-5,4,-1,-2,-6,3,7,-7,8,-8,3,9,-8,10,-8,-8,1,5,-10,2,4,-3,7,-9,-10,-9,2,6,-4,6,9,5,5,-6,8,10,5,10,-3,-8,-6,8,6,-6,2,-10,-5,3,-6,-8,6,6,-1], dtype = "int32")#candidate|5321|(243,)|const|int32
call_5319 = func_4133_call(relay.reshape(const_5320.astype('int32'), []), relay.reshape(const_5321.astype('int32'), [3, 9, 9]), )
call_5322 = func_4133_call(relay.reshape(const_5320.astype('int32'), []), relay.reshape(const_5321.astype('int32'), [3, 9, 9]), )
uop_5323 = relay.atanh(const_5321.astype('float32')) # shape=(243,)
output = relay.Tuple([call_5271,call_5319,const_5320,uop_5323,])
output2 = relay.Tuple([call_5272,call_5322,const_5320,uop_5323,])
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
func_3774_call = mod.get_global_var('func_3774')
func_3776_call = mutated_mod.get_global_var('func_3776')
call_5421 = func_3774_call()
call_5422 = func_3774_call()
output = call_5421
output2 = call_5422
func_5444 = relay.Function([], output)
mod['func_5444'] = func_5444
mod = relay.transform.InferType()(mod)
output = func_5444()
func_5445 = relay.Function([], output)
mutated_mod['func_5445'] = func_5445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3656_call = mod.get_global_var('func_3656')
func_3657_call = mutated_mod.get_global_var('func_3657')
call_5480 = func_3656_call()
call_5481 = func_3656_call()
func_2040_call = mod.get_global_var('func_2040')
func_2044_call = mutated_mod.get_global_var('func_2044')
const_5483 = relay.const([-0.833165,-5.668786,-1.213959,9.835527,6.154341,1.427902,9.104346,-6.674710,-3.814495,1.589115,-5.008548,-4.140175,1.797341,-7.641087,-9.208423,6.777046,-0.751485,3.038688,1.195836,-5.966488,-0.838838,1.585822,-6.527853,2.434416,-9.036830,3.776627,4.240755,-0.775726,1.784321,7.852180,0.321487,-1.552982,-0.730311,-6.576338,-5.609545,1.309736,-1.816870,8.914387,-2.272312,8.426967,7.055084,0.737585,2.104967,-7.416272,1.256772,-8.737245,-7.474182,-2.070354,-3.743791,-7.177876,0.985210,9.915802,-0.345862,1.243061,9.014636,8.607573,9.138964,2.330530,2.947378,3.843386,-2.999985,9.739848,2.070580,1.582703,-0.235206,-9.039526,1.485759,6.612518,-7.140946,9.066517,9.560780,7.625226,0.510563,3.319632,-6.538434,4.492952,0.473307,7.948252,-8.775652,-8.548014,-4.518039,4.404680,4.084877,4.811022,3.437381,3.452734,8.000507,3.234104,-5.553991,9.372685,9.886008,0.933969,3.257512,0.985407,8.521701,-6.074955,6.232670,-2.072983,-5.737524,-8.379042,-5.228284,1.533624,-0.972342,-5.308937,9.887879,2.072821,2.267931,1.853261,6.301480,-4.733164,8.877696,-3.980691,-9.554255,2.436322,-6.906476,-7.148455,6.917342,3.049656,-9.273787,-1.902186,7.979927,6.493507,-8.163967,-1.310373,6.435766,5.821239,4.115530,3.470380,-0.529746,2.607357,4.255763,8.391185,4.227073,-8.552891,-4.555566,7.319529,7.161958,-8.703778,-6.518944,3.374397,-4.457148,-1.566503,0.899964,9.218600,-2.630728,-1.786653,0.773592,-5.616072,-9.159230,-5.509221,-5.400389,1.580106,-5.740359,5.296859,-9.320107,2.920143,8.403395,-4.873982,5.147138,-5.341682,-4.260611,1.359315,-6.938304,-5.607534,1.407339,-5.277483,2.011421,5.872055,1.591591,-6.567856,8.576699,-9.052052,0.746513,9.903096,1.944743,-7.886733,6.815229,7.675925,8.255100,-6.326194,-1.403195,-6.245154,-1.496383,-0.277906,2.591641,6.225119,-1.256884,2.234521,7.169047,-6.945370,5.437404,-0.231079,4.318601,-3.629534,-2.672496,4.425057,9.062490,-4.467297,0.484424,-5.860604,9.487189,1.202105,6.845134,9.225208,-3.571368,2.649164,-4.479929,-6.186269,7.004382,-1.457412,3.235602,5.803056,-0.400752,2.841389,-3.990356,-7.479319,6.339082,8.569712,-4.505835,2.488180,-7.266510,-6.936900,4.896821,-9.649525,-6.433455,-7.834188,-3.817509,-5.478315,6.468128,-8.598108,7.280828,5.803656,4.574678,-0.383853,8.583051,-2.961825,-8.084247,-1.107931,4.189296,3.465356,3.841889,9.121996,2.737085,-8.544947,5.457986,-0.561011,1.634475,-2.161629,-0.488134,1.900132,-8.687200,6.442969,-6.015455,-9.803156,2.387282,5.195442,8.387924,-7.864209,7.089844,9.974287,-8.171344,0.027070,9.816118,-9.892414,-2.204266,4.461516,2.098177,-3.570379,-0.410637,4.867283,-9.095867,2.514669,7.982520,-5.053383,-1.210658,-4.568224,0.466374,4.435992,3.411614,-6.270612,7.842394,-1.591553,-9.105989,-8.357804,-5.720630,-6.894922,2.075147,-9.638197,-2.877446,4.718279,3.965619,2.256237,5.805274,7.256916,-9.970351,6.080268,-5.695130,-6.582063,-2.103132,8.604817,-3.409467,9.276734,6.677021,-4.559637,-0.629444,5.104282,7.769498,-8.140205,3.890803,2.321038,3.057487,7.626836,8.366984,-0.167830,-8.945730,-0.042722,-7.627715,-9.553184,0.021162,5.547305,-4.111011,8.161586,5.244746,8.434525,-1.866802,-3.182713,4.654221,5.174147,1.668239,-1.471710,4.658572,-7.300061,-6.122004,-0.152856,4.895073,6.582390,-4.382067,-8.080725,-2.056913,-0.814982,-3.008716,-7.481941,-6.704487,-5.240123,8.577998,3.905664,2.969705,-2.068756,6.402661,-5.086194,-2.363567,-2.638196,-2.507977,-7.821889,-0.880257,6.852656,2.137786,-8.166811,9.736094,1.802886,8.777260,-5.580905,-5.596340,-0.592909,2.338725,3.478332,-9.793652,-7.188841,-5.513226,4.599361,0.759099,4.031874,-6.430833,-9.654827,4.034304,2.071678,-1.433063,1.626485,-6.358503,-7.410770,-6.235589,-9.713732,-0.998501,-8.470646,5.528700,0.830750,-8.498503,-1.817720,2.528647,4.487762,-1.518908,1.784880,-2.413180,-6.333392,3.573740,-9.771621,-2.493962,-6.582672,9.187279,3.205234,0.513328,2.573014,5.810688,-8.162056,-9.532612,6.904846,-8.292371,9.830844,-4.558538,-2.253335,6.357354,3.155379,8.871096,-2.637480,-3.686077,2.477327,-3.855031,-7.790603,-4.152159,-8.583618,-6.321344,-7.804611,7.229526,3.527060,0.372008,6.881673,-6.985761,-9.911546,-6.533592,-2.664416,-6.795326,-5.311020,-5.391493,-5.539223,-3.603531,9.878925,3.552543,1.497902,1.762091,-2.629649,-5.476361,2.543931,-8.912265,-3.247364,-1.245146,-3.112394,8.829674,-6.157375,1.252472,-8.421402,0.557304,-1.410239,3.827906,0.088040,-0.252408,1.098043,2.750137,6.770356,-8.312481,8.494374,-4.225488,8.070598,-8.591755,9.609799,1.837737,9.024576,0.015484,9.270024,-2.508852,2.569740,-8.407196,0.394111,-4.755288,5.957802,1.814373,0.565087,-1.389157,3.749443,-1.355434,-2.287567,-9.282389,4.308713,0.299994,1.627303,6.639683,-3.483152,6.070603,-3.659301,-5.030138,5.208826,-0.632138,0.060849,4.339598,2.120732,1.709239,9.480453,-8.278002,7.354922,5.526007,3.541492,-4.353164,-9.261279,6.503682,3.327062,5.012880,2.728878,3.753088,-9.089602,1.076321,0.208270,-9.170520,1.544189,6.702299,-2.008335,7.027683,5.526678,-1.301478,1.833330,-1.265374,4.706476,0.089613,9.534089,-8.079485,-8.836833,-6.530777,-3.756942,-5.021869,2.938256,0.287631,2.121379,0.475643,-0.616882,-5.209484,6.464929,-6.268057,-4.113830,-8.058368,-1.280859,-9.298539,-5.380249,-3.006945,3.581510,-3.194166,-2.908153,-6.166190,-2.348071,6.245411,5.884711,8.237565,-7.844507,-4.853142,9.054039,5.716286,9.170962,-2.309903,-6.992682,-6.398923,-0.274726,-9.694877,-8.597283,-0.002492,-1.037271,9.292314,5.948183,-0.002804,-7.292669,0.912914,6.709354,-4.516505,-0.393631,5.280247,5.944564,-4.651484,-5.821379,2.986856,9.585430,-9.438936,3.405392,-2.086316,-9.203239,-1.471929,8.231309,-8.213210,-1.455182,6.935265,-3.071786,8.204606,-3.039231,0.034615,-1.338955,-4.805562,-7.602893,9.806742,-2.513414,-4.126952,6.850178,-8.567915,-7.853201,4.651321,9.637909,5.484525,2.154807,7.600177,-0.200128,0.878484,8.776828,9.484307,-6.507542,2.387494,-2.898282,1.872263,7.270659,-3.688637,-2.912487,-0.281190,-4.614166,6.428523,9.219260,4.473828,0.890422,-8.690449,-6.739110,-5.446271,0.119992], dtype = "float32")#candidate|5483|(624,)|const|float32
call_5482 = relay.TupleGetItem(func_2040_call(relay.reshape(const_5483.astype('float32'), [3, 16, 13]), relay.reshape(const_5483.astype('float32'), [3, 16, 13]), ), 0)
call_5484 = relay.TupleGetItem(func_2044_call(relay.reshape(const_5483.astype('float32'), [3, 16, 13]), relay.reshape(const_5483.astype('float32'), [3, 16, 13]), ), 0)
func_1659_call = mod.get_global_var('func_1659')
func_1664_call = mutated_mod.get_global_var('func_1664')
const_5486 = relay.const([-7,6,-3,10,-3,10,6,-4,10,2,7,6,3,10,-1,2,1,-8,10,-4,-2,-4,4,-1], dtype = "uint16")#candidate|5486|(24,)|const|uint16
const_5487 = relay.const([True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False], dtype = "bool")#candidate|5487|(2145,)|const|bool
const_5488 = relay.const([3,8,-5,10,-8,-2,-5,-8,10,5,8,4,-3,6,-7,1,2,5,-8,1,-1,6,3,-5,1,-6,-9,-4,1,4,8,-7,7,-10,-7,10,5,4,-9,3,-10,10,3,-4,6,10,7,4,9,8,6,-6,3,9,10,5,-4,1,-1,-10,5,8,-7,-6,8,-2,4,-5,9,-1,9,9,1,9,-7,6,10,5,-8,-2,7,-1,4,-7,10,-2,-6,-2,-2,-10,1,2,1,7,-2,-6,-4,9,-2,1,-8,1,-5,-2,4,-6,9,-4,-7,2,9,8,4,1,6,10,-6,-10,3,-6,6,-4,1,-5,-9,8,4,3,-5,-4,8,-7,-4,-3,-10,8,2,1,9,2,3,-10,-9,-5,-9,7,4,2,-2,-8,8,8,-5,-5,-5,4,8,4,-7,2,-9,-3,-3,-10,-4,7,4,1,-6,-4,3,8,-2,-1,-1,-2,9,3,2,7,4,7,-1,7,-7,8,-1,-3,9,9,-6,2,10,-9,9,-8,2,-10,6,-8,-8,-2,3,1,9,3,5,-1,9,7,6,2,5,-10,-1,3,-5,10,2,9,3,7,7,5,9,-7,-9,4,-3,4,-3,5,2,5,9,5,5,-2,-1,-10,8,7,6,-1,8,-5,10,8,-7,8,-8,-8,5,7,6,8,5,-3,-9,-2,-8,7,-6,2,9,-9,-2,-1,-6,5,-8,-8,-10,-3,-5,-7,1,3,-10,-1,4,7,-7,-5,9,-7,-2,-9,7,-3,-9,5,4,-9,2,5,-10,-4,-1,9,6,6,-4,2,8,-6,-8,9,1,-8,8,3,-6,-4,-5,-8,1,-10,-10,10,10,7,9,1,3,-4,-3,-6,3,9,-3,8,-2,2,-3,-1,8,-2,-5,-8,-2,-7,9,-5,5,2,-10,3,9,5,-8,6,8,1,-10,-2,-1,-9,-4,7,-8,-9,-7,2,8,1,-8,1,6,-9,-1,1,10,4,-2,-3,-8,-9,-5,-5,10,10,-3,-4,-3,5,4,7,6,7,-2,10,-5,9,2,4,9,10,4,-1,8,2,4,7,-1,-7,5,7,6,9,-9,2,8,10,-7,-3,-8,9,4,-3,-8,-10,-10,4,-2,-6,9,-8,9,1,2,-10,-8,-4,5,-9,-8,10,5,-3,-9,7,6,-7,7,10,-1,-10], dtype = "uint16")#candidate|5488|(448,)|const|uint16
call_5485 = relay.TupleGetItem(func_1659_call(relay.reshape(const_5486.astype('uint16'), [1, 4, 6]), relay.reshape(const_5487.astype('bool'), [2145,]), relay.reshape(const_5488.astype('uint16'), [448,]), ), 3)
call_5489 = relay.TupleGetItem(func_1664_call(relay.reshape(const_5486.astype('uint16'), [1, 4, 6]), relay.reshape(const_5487.astype('bool'), [2145,]), relay.reshape(const_5488.astype('uint16'), [448,]), ), 3)
uop_5496 = relay.log(call_5480.astype('float64')) # shape=(12, 11, 5)
uop_5498 = relay.log(call_5481.astype('float64')) # shape=(12, 11, 5)
uop_5501 = relay.cos(uop_5496.astype('float64')) # shape=(12, 11, 5)
uop_5503 = relay.cos(uop_5498.astype('float64')) # shape=(12, 11, 5)
func_4585_call = mod.get_global_var('func_4585')
func_4589_call = mutated_mod.get_global_var('func_4589')
var_5505 = relay.var("var_5505", dtype = "uint8", shape = (672,))#candidate|5505|(672,)|var|uint8
call_5504 = relay.TupleGetItem(func_4585_call(relay.reshape(var_5505.astype('uint8'), [672, 1]), relay.reshape(call_5482.astype('float32'), [624,]), relay.reshape(const_5483.astype('float32'), [2, 312]), ), 3)
call_5506 = relay.TupleGetItem(func_4589_call(relay.reshape(var_5505.astype('uint8'), [672, 1]), relay.reshape(call_5482.astype('float32'), [624,]), relay.reshape(const_5483.astype('float32'), [2, 312]), ), 3)
func_5330_call = mod.get_global_var('func_5330')
func_5332_call = mutated_mod.get_global_var('func_5332')
call_5510 = relay.TupleGetItem(func_5330_call(), 3)
call_5511 = relay.TupleGetItem(func_5332_call(), 3)
output = relay.Tuple([call_5482,const_5483,call_5485,const_5486,const_5487,const_5488,uop_5501,call_5504,var_5505,call_5510,])
output2 = relay.Tuple([call_5484,const_5483,call_5489,const_5486,const_5487,const_5488,uop_5503,call_5506,var_5505,call_5511,])
func_5515 = relay.Function([var_5505,], output)
mod['func_5515'] = func_5515
mod = relay.transform.InferType()(mod)
mutated_mod['func_5515'] = func_5515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5516 = relay.var("var_5516", dtype = "uint8", shape = (672,))#candidate|5516|(672,)|var|uint8
func_5515_call = mutated_mod.get_global_var('func_5515')
call_5517 = func_5515_call(var_5516)
output = call_5517
func_5518 = relay.Function([var_5516], output)
mutated_mod['func_5518'] = func_5518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4086_call = mod.get_global_var('func_4086')
func_4087_call = mutated_mod.get_global_var('func_4087')
call_5646 = relay.TupleGetItem(func_4086_call(), 0)
call_5647 = relay.TupleGetItem(func_4087_call(), 0)
var_5656 = relay.var("var_5656", dtype = "uint16", shape = (448,))#candidate|5656|(448,)|var|uint16
bop_5657 = relay.floor_divide(call_5646.astype('float64'), relay.reshape(var_5656.astype('float64'), relay.shape_of(call_5646))) # shape=(448,)
bop_5660 = relay.floor_divide(call_5647.astype('float64'), relay.reshape(var_5656.astype('float64'), relay.shape_of(call_5647))) # shape=(448,)
func_3496_call = mod.get_global_var('func_3496')
func_3498_call = mutated_mod.get_global_var('func_3498')
call_5682 = relay.TupleGetItem(func_3496_call(), 8)
call_5683 = relay.TupleGetItem(func_3498_call(), 8)
output = relay.Tuple([bop_5657,call_5682,])
output2 = relay.Tuple([bop_5660,call_5683,])
func_5689 = relay.Function([var_5656,], output)
mod['func_5689'] = func_5689
mod = relay.transform.InferType()(mod)
var_5690 = relay.var("var_5690", dtype = "uint16", shape = (448,))#candidate|5690|(448,)|var|uint16
output = func_5689(var_5690)
func_5691 = relay.Function([var_5690], output)
mutated_mod['func_5691'] = func_5691
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5736 = relay.var("var_5736", dtype = "uint64", shape = (8, 14, 16))#candidate|5736|(8, 14, 16)|var|uint64
var_5737 = relay.var("var_5737", dtype = "uint64", shape = (8, 14, 16))#candidate|5737|(8, 14, 16)|var|uint64
bop_5738 = relay.less_equal(var_5736.astype('bool'), relay.reshape(var_5737.astype('bool'), relay.shape_of(var_5736))) # shape=(8, 14, 16)
func_765_call = mod.get_global_var('func_765')
func_769_call = mutated_mod.get_global_var('func_769')
var_5750 = relay.var("var_5750", dtype = "uint8", shape = ())#candidate|5750|()|var|uint8
var_5751 = relay.var("var_5751", dtype = "uint8", shape = (168, 4))#candidate|5751|(168, 4)|var|uint8
call_5749 = func_765_call(relay.reshape(var_5750.astype('uint8'), []), relay.reshape(var_5751.astype('uint8'), [7, 16, 6]), )
call_5752 = func_765_call(relay.reshape(var_5750.astype('uint8'), []), relay.reshape(var_5751.astype('uint8'), [7, 16, 6]), )
func_2130_call = mod.get_global_var('func_2130')
func_2136_call = mutated_mod.get_global_var('func_2136')
const_5757 = relay.const([-3,-4,1,7,-9,2,8,-7,8,-6,9,-10,6,-5,3,2,9,10,-4,-1,9,4,3,8,5,8,2,8,-5,4,-9,3,-4,9,-9,-1,-6,-8,6,-2,10,4,-8,-1,-7,1,3,5,-9,5,7,-6,1,-5,10,10,7,-3,8,8,-10,1,-2,-1,3,9,-4,-4,-9,-3,-6,10,-7,-10,10,8,6,-3,6,-9,10,8,1,8,-2,-10,4,-4,6,5,4,5,-5,-6,2,9,-3,5,-10,3,-4,10,6,8,-10,7,-6,-3,9,-1,7,3,6,2,-3,-8,2,6,4,8,-4,-7,7,1,-1,9,2,-6,1,6,4,2,4,4,9,3,8,8,-1,-1,3,8,3,-6,1,10,-8,3,-8,3,8,-3,-7,2,-9,-10,-3,8,2,10,-7,-1,3,-10,-1,-8,-6,-5,-3,-1,-10,-7,-9,8,-8,-7,1,2,3,4,-5,-3,7,-6,-5,-3,7,-9,-4,10,-7,8,6,-1,4,-3,10,-1,-3,7,3,-4,-1,-7,-2,-6,-5,-7,8,1,5,-2,7,-2,-8,10,-9,2,-1,-5,-7,10,-7,6,-6,9,9,6,3,-10,-9,4,7,7,4,-1,-5,6,9,-1,-9,6,-10,-7,4,-5,8,-10,3,4,-1,2,-5,2,-2,-9,-1,-10,1,3,-7,-8,-8,-9,-6,-10,-8,-5,-3,-9,9,-8,6,1,-7,3,-5,-8,-9,-5,2,2,-10,-4,-5,9,-2,-4,5,4,-4,-6,9,-1,3,-1,-3,-4,1,7,-3,-2,3,3,-3,-10,5,-5,9,3,4,-6,9,2,-10,-10,5,-9,-7,-6,9,-9,-1,-9,2,2,-7,7,-8,8,9,-2,9,3,-4,-8,5,7,2,6,-9,-4,-5,-2,9,1,-9,2,-6,2,6,-3,7,-8,-8,-5,-1,5,9,8,-9,-5,4,6,4,10,-8,-2,-2,6,-3,9,9,1,-3,-5,10,3,-7,5,-5,-1,7,1,-2,-3,7,8,-8,-3,7,-5,8,-2,5,4,2,4,-7,-3,2,-5,-10,5,3,8,8,7,-9,8,-6,-3,-10,-2,-4,7,10,6,-4,-7,3,-6,-7,4,4,2,-6,10,4,2,-6,-7,-2,8,6,-4,-9,7,-5,-3,-4,-1,-10,8,-7,-3,1,1], dtype = "uint64")#candidate|5757|(448,)|const|uint64
const_5758 = relay.const([False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False], dtype = "bool")#candidate|5758|(2145,)|const|bool
call_5756 = relay.TupleGetItem(func_2130_call(relay.reshape(const_5757.astype('uint64'), [8, 7, 8]), relay.reshape(const_5757.astype('uint64'), [8, 7, 8]), relay.reshape(const_5758.astype('bool'), [2145,]), relay.reshape(var_5750.astype('uint8'), []), relay.reshape(var_5751.astype('uint8'), [672,]), ), 7)
call_5759 = relay.TupleGetItem(func_2136_call(relay.reshape(const_5757.astype('uint64'), [8, 7, 8]), relay.reshape(const_5757.astype('uint64'), [8, 7, 8]), relay.reshape(const_5758.astype('bool'), [2145,]), relay.reshape(var_5750.astype('uint8'), []), relay.reshape(var_5751.astype('uint8'), [672,]), ), 7)
uop_5785 = relay.acosh(const_5758.astype('float64')) # shape=(2145,)
output = relay.Tuple([bop_5738,call_5749,var_5750,var_5751,call_5756,const_5757,uop_5785,])
output2 = relay.Tuple([bop_5738,call_5752,var_5750,var_5751,call_5759,const_5757,uop_5785,])
func_5788 = relay.Function([var_5736,var_5737,var_5750,var_5751,], output)
mod['func_5788'] = func_5788
mod = relay.transform.InferType()(mod)
mutated_mod['func_5788'] = func_5788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5788_call = mutated_mod.get_global_var('func_5788')
var_5790 = relay.var("var_5790", dtype = "uint64", shape = (8, 14, 16))#candidate|5790|(8, 14, 16)|var|uint64
var_5791 = relay.var("var_5791", dtype = "uint64", shape = (8, 14, 16))#candidate|5791|(8, 14, 16)|var|uint64
var_5792 = relay.var("var_5792", dtype = "uint8", shape = ())#candidate|5792|()|var|uint8
var_5793 = relay.var("var_5793", dtype = "uint8", shape = (168, 4))#candidate|5793|(168, 4)|var|uint8
call_5789 = func_5788_call(var_5790,var_5791,var_5792,var_5793,)
output = call_5789
func_5794 = relay.Function([var_5790,var_5791,var_5792,var_5793,], output)
mutated_mod['func_5794'] = func_5794
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5796 = relay.const(-5, dtype = "uint64")#candidate|5796|()|const|uint64
var_5797 = relay.var("var_5797", dtype = "uint64", shape = (2, 2, 1))#candidate|5797|(2, 2, 1)|var|uint64
bop_5798 = relay.bitwise_xor(const_5796.astype('uint64'), var_5797.astype('uint64')) # shape=(2, 2, 1)
output = bop_5798
output2 = bop_5798
func_5807 = relay.Function([var_5797,], output)
mod['func_5807'] = func_5807
mod = relay.transform.InferType()(mod)
mutated_mod['func_5807'] = func_5807
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5808 = relay.var("var_5808", dtype = "uint64", shape = (2, 2, 1))#candidate|5808|(2, 2, 1)|var|uint64
func_5807_call = mutated_mod.get_global_var('func_5807')
call_5809 = func_5807_call(var_5808)
output = call_5809
func_5810 = relay.Function([var_5808], output)
mutated_mod['func_5810'] = func_5810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_5841 = relay.TupleGetItem(func_3121_call(), 0)
call_5842 = relay.TupleGetItem(func_3123_call(), 0)
func_2130_call = mod.get_global_var('func_2130')
func_2136_call = mutated_mod.get_global_var('func_2136')
const_5844 = relay.const([-6,2,2,1,-8,-7,-9,9,-6,-4,-7,-1,5,2,9,-3,8,-7,7,-4,-6,-3,1,-6,3,5,3,2,-6,-5,-2,4,-6,-10,10,8,-4,-4,5,4,-10,-9,-7,-2,7,-9,-8,7,-3,-8,1,-2,9,2,6,3,8,-8,2,7,-9,-6,-9,-10,-2,-9,4,-9,-7,-6,-8,-8,10,-1,-8,-2,7,2,5,-2,10,-1,3,7,3,-3,-4,-9,-7,-9,-3,1,-2,-7,5,-5,9,9,-6,-3,2,1,-5,4,-3,8,-7,5,2,-8,3,1,-7,-5,-9,-3,-2,-10,-7,2,9,-7,7,-6,5,-7,7,-10,10,-9,-4,9,9,5,-4,-7,7,9,-5,4,-9,8,-8,-10,6,5,-6,-5,6,10,-9,4,10,-9,-8,-4,-3,-5,-1,-7,-8,6,-9,-6,3,6,4,7,3,6,-10,-10,-3,3,-2,2,3,2,8,-6,6,2,-1,-4,6,6,10,-10,1,-8,4,-2,5,8,2,6,-7,9,-9,2,3,-3,6,-8,7,-1,-6,-7,-7,-6,-10,-8,-3,4,-8,-7,-6,5,-6,-10,-1,-3,4,-1,6,9,-2,-10,3,-6,2,-3,-6,2,-3,6,-5,-4,10,9,5,-9,-6,1,-6,-10,8,9,-2,-7,-5,-1,-1,-9,-10,-6,-8,-9,7,4,7,-2,-5,-1,3,-2,-1,9,7,3,-8,-2,6,-3,-3,8,10,5,2,4,3,4,-8,4,-2,-5,-7,-9,8,8,10,1,6,9,1,-3,-1,8,1,7,2,6,-8,-4,8,8,-8,1,-7,1,-6,-2,-1,-6,-6,-6,6,-6,6,1,-2,5,9,3,6,4,10,9,-8,-4,10,1,-3,-8,-8,4,-9,-1,4,-2,10,2,-4,1,-6,6,-6,-1,5,9,-8,3,-3,6,10,8,6,8,-3,-1,6,6,-4,3,6,-3,7,2,2,-7,-5,-10,9,10,9,-2,7,-6,-2,-10,-1,3,-9,-9,-2,-3,5,10,3,5,-9,4,-4,-7,-9,5,10,-1,-4,9,-9,4,8,-10,-4,-3,-2,1,9,-4,-4,2,8,2,4,-7,6,8,5,-4,-3,-2,-4,-2,-2,3,5,2,9,-7,-7,-7,-8,-6,-3,4,5,-10,10,4,-6,7,-2,-7,5,3,10,5], dtype = "uint64")#candidate|5844|(448,)|const|uint64
var_5845 = relay.var("var_5845", dtype = "bool", shape = (2145,))#candidate|5845|(2145,)|var|bool
const_5846 = relay.const(-1, dtype = "uint8")#candidate|5846|()|const|uint8
const_5847 = relay.const([[10,-5,2,-10,-5,1,10,-9,5,-6,-5,10,-8,7,-6,2,-3,-8,4,3,-10,5,8,-7,-3,-9,-7,6,-3,-5,6,-6,-4,-3,-2,-8,-1,-4,-6,-3,-3,-9,-1,-8,-6,5,10,-2,-8,5,-1,2,-7,-10,5,-1,-6,-9,-3,-3,-1,2,10,10,-9,7,9,4,8,-8,-9,-3,1,-4,-2,5,5,-7,-3,4,1,4,3,-5,-1,-5,-3,-7,-10,-9,8,-8,-3,-10,1,2,5,5,5,-10,4,-7,4,3,5,-8,6,-5,-10,-7,9,6,-7,-6,10,7,1,-3,9,1,-8,8,5,-4,8,-8,3,5,-5,-10,-6,1,4,4,-9,-1,4,-2,-3,-5,-10,-2,-7,4,-5,-6,-3,8,-10,3,7,-6,-3,9,-5,-9,-7,9,-7,5,7,-4,-8,-10,-5,8,8,5,4,-9,8,5,10,-9,-9,10,-6,8,7,2,2,-5,6,4,-4,1,5,-9,-4,-4,5,-10,-8,-4,-8,-8,6,3,-3,-2,-1,9,10,1,-8,-6,-10,-3,7,-5,2,5,9,10,4,9,4,9,5,8,6,-8,2,-7,9,-4,-7,8,7,-8,-9,-6,4,-9,-9,4,-4,-4,-4,-5,-4,1,-10,-9,-9,9,1,-3,5,4,10,9,-10,2,5,6,-8,3,8,-6,7,4,-5,5,-10,3,-6,-6,7,-2,-5,4,-7,-3,8,-1,9,5,4,-3,8,8,8,4,-2,-10,5,4,2,7,9,7,5,1,3,-8,9,6,-10,5,-9,10,-10,7,4,-3,2,-10,-3,8,6,-6,-2,2,-5,3,-3,-9,9,-6,10,5,-9,-10,-9,-8,-6,10,9,9,1,9,7,9,-5,-9],[6,6,-3,10,7,-5,-2,-3,6,-6,-6,-3,4,8,-8,-4,-5,2,7,9,9,10,-10,-2,-7,-5,3,3,-9,7,-10,-2,1,2,-5,5,5,-3,8,-1,-4,-7,4,6,-1,-1,-6,-7,-6,-7,9,2,7,9,3,-2,6,-5,9,4,-8,2,-9,-1,9,-5,-1,-2,-4,-6,1,-5,-9,-7,-4,10,-7,6,-3,-2,-8,-1,-4,7,-2,-7,5,9,-4,2,-9,-2,5,4,-6,8,-3,-2,2,9,4,-6,-9,3,-3,-3,-5,1,-2,8,3,-3,7,-5,7,-2,9,-2,-4,4,-9,-2,-10,6,9,-4,-10,-9,2,-5,-8,-2,6,7,-8,-9,-8,1,3,-1,-1,-5,2,9,9,-3,-2,6,-8,10,-4,4,2,-9,5,9,5,-7,7,-10,-10,3,-9,-2,10,4,-2,5,4,-1,3,2,-4,-2,-7,-7,-7,-10,7,-3,5,2,-4,3,8,4,4,9,9,8,6,-2,4,-7,-6,-10,8,8,7,-9,-5,-8,10,-6,-9,-4,10,7,-10,4,5,-6,-6,-6,-4,-9,9,-8,3,8,10,6,-10,1,7,7,-1,-6,7,-7,-6,-2,4,-6,5,10,7,-5,-10,10,-4,-1,2,-10,-1,2,5,-4,3,7,-5,-5,-6,-1,7,-6,-8,5,-8,9,-4,-9,-2,-10,-7,6,6,4,2,-10,7,-1,5,-7,3,-2,-4,5,-8,-4,2,4,-1,-1,6,-3,9,9,2,-9,-9,-9,4,2,9,-6,6,-8,-10,2,-2,10,1,-9,5,-7,9,-9,1,6,7,-8,3,10,7,-1,6,-2,1,1,9,10,5,-10,3,6,-7,-3,-2,-4,-4,10,6,-9,3,-3]], dtype = "uint8")#candidate|5847|(2, 336)|const|uint8
call_5843 = relay.TupleGetItem(func_2130_call(relay.reshape(const_5844.astype('uint64'), [8, 7, 8]), relay.reshape(const_5844.astype('uint64'), [8, 7, 8]), relay.reshape(var_5845.astype('bool'), [2145,]), relay.reshape(const_5846.astype('uint8'), []), relay.reshape(const_5847.astype('uint8'), [672,]), ), 8)
call_5848 = relay.TupleGetItem(func_2136_call(relay.reshape(const_5844.astype('uint64'), [8, 7, 8]), relay.reshape(const_5844.astype('uint64'), [8, 7, 8]), relay.reshape(var_5845.astype('bool'), [2145,]), relay.reshape(const_5846.astype('uint8'), []), relay.reshape(const_5847.astype('uint8'), [672,]), ), 8)
func_5689_call = mod.get_global_var('func_5689')
func_5691_call = mutated_mod.get_global_var('func_5691')
call_5856 = relay.TupleGetItem(func_5689_call(relay.reshape(call_5843.astype('uint16'), [448,])), 0)
call_5857 = relay.TupleGetItem(func_5691_call(relay.reshape(call_5843.astype('uint16'), [448,])), 0)
func_3712_call = mod.get_global_var('func_3712')
func_3714_call = mutated_mod.get_global_var('func_3714')
call_5859 = relay.TupleGetItem(func_3712_call(), 0)
call_5860 = relay.TupleGetItem(func_3714_call(), 0)
func_5227_call = mod.get_global_var('func_5227')
func_5229_call = mutated_mod.get_global_var('func_5229')
call_5872 = func_5227_call()
call_5873 = func_5227_call()
uop_5887 = relay.log2(const_5847.astype('float64')) # shape=(2, 336)
func_3386_call = mod.get_global_var('func_3386')
func_3390_call = mutated_mod.get_global_var('func_3390')
var_5898 = relay.var("var_5898", dtype = "bool", shape = (1152,))#candidate|5898|(1152,)|var|bool
call_5897 = relay.TupleGetItem(func_3386_call(relay.reshape(var_5898.astype('bool'), [12, 12, 8]), relay.reshape(var_5898.astype('bool'), [12, 12, 8]), relay.reshape(call_5872.astype('uint16'), [448,]), ), 1)
call_5899 = relay.TupleGetItem(func_3390_call(relay.reshape(var_5898.astype('bool'), [12, 12, 8]), relay.reshape(var_5898.astype('bool'), [12, 12, 8]), relay.reshape(call_5872.astype('uint16'), [448,]), ), 1)
output = relay.Tuple([call_5841,call_5843,const_5844,var_5845,const_5846,call_5856,call_5859,call_5872,uop_5887,call_5897,var_5898,])
output2 = relay.Tuple([call_5842,call_5848,const_5844,var_5845,const_5846,call_5857,call_5860,call_5873,uop_5887,call_5899,var_5898,])
func_5914 = relay.Function([var_5845,var_5898,], output)
mod['func_5914'] = func_5914
mod = relay.transform.InferType()(mod)
mutated_mod['func_5914'] = func_5914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5914_call = mutated_mod.get_global_var('func_5914')
var_5916 = relay.var("var_5916", dtype = "bool", shape = (2145,))#candidate|5916|(2145,)|var|bool
var_5917 = relay.var("var_5917", dtype = "bool", shape = (1152,))#candidate|5917|(1152,)|var|bool
call_5915 = func_5914_call(var_5916,var_5917,)
output = call_5915
func_5918 = relay.Function([var_5916,var_5917,], output)
mutated_mod['func_5918'] = func_5918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5083_call = mod.get_global_var('func_5083')
func_5084_call = mutated_mod.get_global_var('func_5084')
call_5938 = relay.TupleGetItem(func_5083_call(), 0)
call_5939 = relay.TupleGetItem(func_5084_call(), 0)
func_3386_call = mod.get_global_var('func_3386')
func_3390_call = mutated_mod.get_global_var('func_3390')
const_5971 = relay.const([False,False,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False], dtype = "bool")#candidate|5971|(1152,)|const|bool
var_5972 = relay.var("var_5972", dtype = "uint16", shape = (448,))#candidate|5972|(448,)|var|uint16
call_5970 = relay.TupleGetItem(func_3386_call(relay.reshape(const_5971.astype('bool'), [12, 12, 8]), relay.reshape(const_5971.astype('bool'), [12, 12, 8]), relay.reshape(var_5972.astype('uint16'), [448,]), ), 1)
call_5973 = relay.TupleGetItem(func_3390_call(relay.reshape(const_5971.astype('bool'), [12, 12, 8]), relay.reshape(const_5971.astype('bool'), [12, 12, 8]), relay.reshape(var_5972.astype('uint16'), [448,]), ), 1)
var_5975 = relay.var("var_5975", dtype = "uint16", shape = (448,))#candidate|5975|(448,)|var|uint16
bop_5976 = relay.logical_xor(var_5972.astype('uint8'), relay.reshape(var_5975.astype('uint8'), relay.shape_of(var_5972))) # shape=(448,)
output = relay.Tuple([call_5938,call_5970,const_5971,bop_5976,])
output2 = relay.Tuple([call_5939,call_5973,const_5971,bop_5976,])
func_5990 = relay.Function([var_5972,var_5975,], output)
mod['func_5990'] = func_5990
mod = relay.transform.InferType()(mod)
mutated_mod['func_5990'] = func_5990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5990_call = mutated_mod.get_global_var('func_5990')
var_5992 = relay.var("var_5992", dtype = "uint16", shape = (448,))#candidate|5992|(448,)|var|uint16
var_5993 = relay.var("var_5993", dtype = "uint16", shape = (448,))#candidate|5993|(448,)|var|uint16
call_5991 = func_5990_call(var_5992,var_5993,)
output = call_5991
func_5994 = relay.Function([var_5992,var_5993,], output)
mutated_mod['func_5994'] = func_5994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_6004 = func_1758_call()
call_6005 = func_1758_call()
var_6009 = relay.var("var_6009", dtype = "float64", shape = (5, 5, 13))#candidate|6009|(5, 5, 13)|var|float64
bop_6010 = relay.greater_equal(call_6004.astype('bool'), relay.reshape(var_6009.astype('bool'), relay.shape_of(call_6004))) # shape=(5, 5, 13)
bop_6013 = relay.greater_equal(call_6005.astype('bool'), relay.reshape(var_6009.astype('bool'), relay.shape_of(call_6005))) # shape=(5, 5, 13)
func_3666_call = mod.get_global_var('func_3666')
func_3669_call = mutated_mod.get_global_var('func_3669')
const_6026 = relay.const([8.046223,9.787622,9.611752,7.861709,6.342587,-1.299070,5.227323,8.401025,-9.727859,-6.810286,5.419891,7.130729,6.921373,5.489618,9.160134,6.619448,8.682673,0.155546,-3.693299,-2.069601,-1.360258,9.367843,1.137823,0.505213,-9.696262,5.394722,6.760635,-0.631086,-8.289280,6.315205,2.825725,-9.800131,3.461319,5.034131,-3.516090,-9.158933,-8.662078,6.617850,-9.770852,8.598292,-8.368382,-2.232275,7.842475,-5.148546,-8.336297,5.142780,-1.328725,8.900474,-2.462290,0.786131,-8.973879,7.115494,-0.063890,2.105437,-1.217199,6.915463,7.150194,-1.174379,9.126782,-0.912221,-8.310697,5.529813,-0.802780,6.895267,2.737341,8.821482,-4.839915,2.286275,2.053248,2.918824,7.221291,-4.322452,-6.172668,-7.538320,7.705450,-7.506442,-1.256663,3.854468,-0.782874,5.304539,0.864057,4.649993,-8.397654,-0.538094,9.854427,3.696725,5.245865,4.772441,-2.310863,2.665208,0.666958,9.014195,1.416724,-8.633881,7.773887,2.394399,-2.709106,-3.255456,6.802593,7.102685,-4.165516,-7.850453,-8.054314,-9.597237,4.366128,6.118637,3.211220,-6.424455,1.468989,-2.359563,4.534898,4.348637,-8.251197,-5.726432,3.649452,5.787739,-9.838543,4.214265,0.445062,2.205402,1.316884,1.484945,5.148619,0.199667,-8.014625,-5.423115,2.150044,-0.633653,8.470354,-1.054441,-8.177468,8.869493,8.874485,6.925047,-4.998278,2.245620,7.555310,-3.504555,-7.511487,4.137048,0.560931,-4.148231,-3.977845,-4.965106,2.025778,-7.841025,-8.366499,-0.972604,-4.500442,8.706005,-0.077037,-7.000269,3.716674,8.340908,-0.912819,9.366394,-4.193256,-5.955713,-5.464388,-5.906981,8.038504,9.322926,-3.119185,5.974569,0.899702,2.822142,8.853027,-9.072453,-3.097210,0.907499,-2.319495,-3.465130,-5.566327,5.590619,-6.146022,9.866656,-7.943464,8.475537,-3.850686,8.104312,7.844114,-2.721071,-1.744290,-6.232203,-4.275715,5.461157,-5.650118,1.659577,1.329970,9.862091,-1.431778,4.843042,9.413811,-7.395281,-3.992562,6.614240,-4.479646,-1.172045,-4.133376,-6.198008,-6.732500,-2.002257,8.654444,-0.598016,-1.240882,-1.190722,-1.676053,-0.720059,0.217257,9.252047,-2.242309,9.208457,-6.782486,-5.509466,-8.191166,4.101950,-1.276536,1.370784,3.358650,-2.327178,7.600696,7.923412,0.478800,4.561649,-6.041365,-7.846393,-5.733574,0.337563,8.481992,2.594977,-3.111063,9.143541,-9.076217,8.292058,-8.224698,-3.912830,-8.574966,9.419751,5.527014,-6.467119,4.529421,-1.542695,7.311842,2.538751,9.906182,-5.971121,3.143500,5.133020,4.998902,-6.180706,-4.647406,3.463816,-0.633349,-7.268557,-6.071400,0.076491,3.811079,2.670429,0.563346,-9.399056,0.919706,0.868039,-7.825873,3.678043,2.512331,5.633307,-7.101667,-8.321881,1.522386,-9.456516,-6.087383,3.454361,7.351275,-5.748405,1.034904,-4.755208,2.900805,-0.223418,-8.611303,5.800614,3.980328,8.561660,-8.750084,-7.519635,7.817997,5.364405,-0.514890,8.824958,3.508108,-1.072637,-6.181674,3.259174,-3.958352,0.984626,9.452473,-2.600153,0.441738,-2.684603,-6.006515,5.399272,0.133481,5.364341,-4.184906,-0.358944,-3.360007,-8.484034,3.777604,-2.830387,9.253483,-2.503689,1.264198,8.703575,-8.042266,-4.990934,-3.654675,-0.224478,-9.433439,6.212481,4.747817,-3.536139,2.081648,-2.494251,-3.064684,-5.276635,4.420449,3.610619,-2.025325,3.539605,-4.519833,0.738804,-7.281420,4.977033,7.873433,7.868021,-0.661206,-0.757599,-4.763390,-7.159525,4.962301,5.917441,0.309396,6.066862,0.864912,-8.996812,-3.840195,5.857694,-7.368640,2.152724,6.765620,-6.780207,-7.760674,6.001745,5.402371,-2.456571,9.476308,8.931859,-5.838150,-1.882033,-2.364154,4.033234,-7.096486,4.830822,7.286130,-8.912137,8.360145,-3.320717,2.942102,-9.871166,3.777117,5.407191,-3.945981,0.784662,-7.346493,0.474272,6.237877,9.641548,0.252805,-7.544907,-7.727983,7.877192,7.598443,9.494738,-6.765818,7.768222,-3.983926,-6.407168,-3.531784,9.102275,5.145186,6.471073,-5.267071,-5.831684,8.242059,-4.198594,5.231723,1.965886], dtype = "float32")#candidate|6026|(396,)|const|float32
call_6025 = func_3666_call(relay.reshape(const_6026.astype('float32'), [3, 11, 12]))
call_6027 = func_3666_call(relay.reshape(const_6026.astype('float32'), [3, 11, 12]))
func_3712_call = mod.get_global_var('func_3712')
func_3714_call = mutated_mod.get_global_var('func_3714')
call_6045 = relay.TupleGetItem(func_3712_call(), 0)
call_6046 = relay.TupleGetItem(func_3714_call(), 0)
output = relay.Tuple([bop_6010,call_6025,const_6026,call_6045,])
output2 = relay.Tuple([bop_6013,call_6027,const_6026,call_6046,])
func_6055 = relay.Function([var_6009,], output)
mod['func_6055'] = func_6055
mod = relay.transform.InferType()(mod)
var_6056 = relay.var("var_6056", dtype = "float64", shape = (5, 5, 13))#candidate|6056|(5, 5, 13)|var|float64
output = func_6055(var_6056)
func_6057 = relay.Function([var_6056], output)
mutated_mod['func_6057'] = func_6057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_6151 = relay.TupleGetItem(func_2994_call(), 0)
call_6152 = relay.TupleGetItem(func_2996_call(), 0)
func_5330_call = mod.get_global_var('func_5330')
func_5332_call = mutated_mod.get_global_var('func_5332')
call_6169 = relay.TupleGetItem(func_5330_call(), 3)
call_6170 = relay.TupleGetItem(func_5332_call(), 3)
var_6190 = relay.var("var_6190", dtype = "float32", shape = (243,))#candidate|6190|(243,)|var|float32
bop_6191 = relay.not_equal(call_6169.astype('bool'), relay.reshape(var_6190.astype('bool'), relay.shape_of(call_6169))) # shape=(243,)
bop_6194 = relay.not_equal(call_6170.astype('bool'), relay.reshape(var_6190.astype('bool'), relay.shape_of(call_6170))) # shape=(243,)
func_5807_call = mod.get_global_var('func_5807')
func_5810_call = mutated_mod.get_global_var('func_5810')
var_6199 = relay.var("var_6199", dtype = "uint64", shape = (4, 1))#candidate|6199|(4, 1)|var|uint64
call_6198 = func_5807_call(relay.reshape(var_6199.astype('uint64'), [2, 2, 1]))
call_6200 = func_5807_call(relay.reshape(var_6199.astype('uint64'), [2, 2, 1]))
var_6201 = relay.var("var_6201", dtype = "uint64", shape = (2, 2, 15))#candidate|6201|(2, 2, 15)|var|uint64
bop_6202 = relay.less(call_6198.astype('bool'), var_6201.astype('bool')) # shape=(2, 2, 15)
bop_6205 = relay.less(call_6200.astype('bool'), var_6201.astype('bool')) # shape=(2, 2, 15)
output = relay.Tuple([call_6151,bop_6191,var_6199,bop_6202,])
output2 = relay.Tuple([call_6152,bop_6194,var_6199,bop_6205,])
func_6207 = relay.Function([var_6190,var_6199,var_6201,], output)
mod['func_6207'] = func_6207
mod = relay.transform.InferType()(mod)
var_6208 = relay.var("var_6208", dtype = "float32", shape = (243,))#candidate|6208|(243,)|var|float32
var_6209 = relay.var("var_6209", dtype = "uint64", shape = (4, 1))#candidate|6209|(4, 1)|var|uint64
var_6210 = relay.var("var_6210", dtype = "uint64", shape = (2, 2, 15))#candidate|6210|(2, 2, 15)|var|uint64
output = func_6207(var_6208,var_6209,var_6210,)
func_6211 = relay.Function([var_6208,var_6209,var_6210,], output)
mutated_mod['func_6211'] = func_6211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3834_call = mutated_mod.get_global_var('func_3834')
call_6218 = relay.TupleGetItem(func_3833_call(), 0)
call_6219 = relay.TupleGetItem(func_3834_call(), 0)
output = call_6218
output2 = call_6219
func_6227 = relay.Function([], output)
mod['func_6227'] = func_6227
mod = relay.transform.InferType()(mod)
mutated_mod['func_6227'] = func_6227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mutated_mod.get_global_var('func_6227')
call_6228 = func_6227_call()
output = call_6228
func_6229 = relay.Function([], output)
mutated_mod['func_6229'] = func_6229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_6260 = relay.TupleGetItem(func_4639_call(), 0)
call_6261 = relay.TupleGetItem(func_4640_call(), 0)
func_3833_call = mod.get_global_var('func_3833')
func_3834_call = mutated_mod.get_global_var('func_3834')
call_6263 = relay.TupleGetItem(func_3833_call(), 0)
call_6264 = relay.TupleGetItem(func_3834_call(), 0)
output = relay.Tuple([call_6260,call_6263,])
output2 = relay.Tuple([call_6261,call_6264,])
func_6265 = relay.Function([], output)
mod['func_6265'] = func_6265
mod = relay.transform.InferType()(mod)
mutated_mod['func_6265'] = func_6265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6265_call = mutated_mod.get_global_var('func_6265')
call_6266 = func_6265_call()
output = call_6266
func_6267 = relay.Function([], output)
mutated_mod['func_6267'] = func_6267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_6278 = relay.TupleGetItem(func_4639_call(), 0)
call_6279 = relay.TupleGetItem(func_4640_call(), 0)
func_2040_call = mod.get_global_var('func_2040')
func_2044_call = mutated_mod.get_global_var('func_2044')
var_6286 = relay.var("var_6286", dtype = "float32", shape = (624,))#candidate|6286|(624,)|var|float32
call_6285 = relay.TupleGetItem(func_2040_call(relay.reshape(var_6286.astype('float32'), [3, 16, 13]), relay.reshape(var_6286.astype('float32'), [3, 16, 13]), ), 0)
call_6287 = relay.TupleGetItem(func_2044_call(relay.reshape(var_6286.astype('float32'), [3, 16, 13]), relay.reshape(var_6286.astype('float32'), [3, 16, 13]), ), 0)
uop_6291 = relay.atan(call_6285.astype('float32')) # shape=(3, 16, 13)
uop_6293 = relay.atan(call_6287.astype('float32')) # shape=(3, 16, 13)
output = relay.Tuple([call_6278,var_6286,uop_6291,])
output2 = relay.Tuple([call_6279,var_6286,uop_6293,])
func_6295 = relay.Function([var_6286,], output)
mod['func_6295'] = func_6295
mod = relay.transform.InferType()(mod)
mutated_mod['func_6295'] = func_6295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6296 = relay.var("var_6296", dtype = "float32", shape = (624,))#candidate|6296|(624,)|var|float32
func_6295_call = mutated_mod.get_global_var('func_6295')
call_6297 = func_6295_call(var_6296)
output = call_6297
func_6298 = relay.Function([var_6296], output)
mutated_mod['func_6298'] = func_6298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_6328 = relay.TupleGetItem(func_2535_call(), 0)
call_6329 = relay.TupleGetItem(func_2537_call(), 0)
output = call_6328
output2 = call_6329
func_6352 = relay.Function([], output)
mod['func_6352'] = func_6352
mod = relay.transform.InferType()(mod)
output = func_6352()
func_6353 = relay.Function([], output)
mutated_mod['func_6353'] = func_6353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4382_call = mod.get_global_var('func_4382')
func_4383_call = mutated_mod.get_global_var('func_4383')
call_6386 = func_4382_call()
call_6387 = func_4382_call()
output = call_6386
output2 = call_6387
func_6390 = relay.Function([], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
output = func_6390()
func_6391 = relay.Function([], output)
mutated_mod['func_6391'] = func_6391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2915_call = mod.get_global_var('func_2915')
func_2916_call = mutated_mod.get_global_var('func_2916')
call_6408 = func_2915_call()
call_6409 = func_2915_call()
output = relay.Tuple([call_6408,])
output2 = relay.Tuple([call_6409,])
func_6412 = relay.Function([], output)
mod['func_6412'] = func_6412
mod = relay.transform.InferType()(mod)
output = func_6412()
func_6413 = relay.Function([], output)
mutated_mod['func_6413'] = func_6413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5182_call = mod.get_global_var('func_5182')
func_5184_call = mutated_mod.get_global_var('func_5184')
call_6421 = relay.TupleGetItem(func_5182_call(), 0)
call_6422 = relay.TupleGetItem(func_5184_call(), 0)
const_6424 = relay.const([[[3.997866,0.979553,7.556145,6.966282,3.320616,-8.997620,-4.418712,-1.426735,-5.586204,2.256696,-4.505032,-0.997216,6.003846],[-8.717935,1.564974,-6.493212,-3.251007,-1.739908,8.578935,-6.933580,-6.176160,8.874212,-5.462432,-8.871191,-7.908755,6.155667],[-2.848397,-3.475063,-6.483230,-5.340171,-6.707041,3.011652,-2.343099,9.215933,8.766712,-0.715684,-2.422626,-8.623638,-2.805866],[6.919564,-2.818578,3.554181,-7.573841,-1.280813,-7.465129,-4.051551,6.118128,9.451551,1.285826,-7.488112,6.612165,-5.488200],[-3.657912,-2.293235,9.184421,9.885870,-5.920974,-7.604400,-1.468297,-5.703735,9.185122,-6.040143,-8.891879,9.372916,-8.725687]],[[-7.377190,-1.658610,6.569510,-7.238538,9.988457,8.505505,6.784921,8.842000,-6.661398,3.361630,5.731873,1.254294,2.494113],[1.499550,2.647122,-3.639865,3.278290,-8.423676,-4.296614,6.429455,-2.735642,-7.131723,-3.505497,1.960615,-3.928479,2.152281],[-1.257595,5.249162,-3.370749,-8.888101,-2.321512,-7.933750,7.035997,-9.913410,0.163710,-5.434943,-3.799631,8.817009,-6.083112],[9.238684,8.487965,-5.777034,3.935493,-0.364022,9.318468,2.987846,5.749191,0.108759,-3.367314,-7.697882,3.458640,7.254808],[-0.008823,2.274525,9.125888,0.678645,6.941119,-6.769227,2.815748,6.794854,8.775235,-6.924214,-2.343616,-6.704904,9.508787]],[[-6.347426,5.358600,-9.501678,-5.615839,-3.258579,-9.931486,8.987340,-9.860912,-2.061190,-5.585608,-6.205486,-9.495932,-5.783828],[-9.178241,6.540406,-2.025635,6.233100,0.568977,9.395523,7.095270,8.644204,9.154823,7.810099,6.062646,2.563041,5.197679],[9.792856,-8.965932,-9.585666,-2.794612,-5.007470,1.976588,-0.271440,5.684160,0.140911,-3.454632,-4.421726,9.888967,6.065583],[8.579317,-6.979443,-3.903007,-7.201986,4.258403,5.795222,-0.004398,-3.664363,4.913079,-9.557928,-1.866678,9.629489,-3.363244],[-1.774756,-2.227293,-1.467283,-2.713772,-9.090805,6.978930,0.219493,-6.232583,-1.369748,-9.906229,-4.489493,-1.239037,-3.901090]],[[-7.780430,6.381693,0.006360,-0.197210,5.627512,3.574566,8.327331,-2.834392,-7.127334,-6.843811,-4.833725,5.030285,7.002642],[9.709915,-5.085804,2.957983,6.959056,-3.751717,-9.543809,-8.883386,3.952429,-4.671505,-8.808970,9.712806,-5.749427,3.636068],[4.287759,-5.449470,-2.612139,-5.480209,3.220114,-0.066630,-4.895218,-6.480408,6.615457,-4.638958,-0.180638,-2.373161,5.540817],[-8.413763,4.758531,-0.324567,-1.075128,7.250878,-0.009931,-8.124957,9.599288,9.105507,5.333575,8.592012,-7.909482,2.984839],[-0.328801,1.756380,-4.567027,6.192491,4.925330,-2.301560,-8.256429,3.823190,2.587105,5.742520,-8.659086,-0.308663,-7.343382]],[[-6.776595,7.561506,2.222336,4.083991,3.676657,-4.934023,7.090583,-6.480697,-6.434417,-8.386339,-0.553137,5.454771,-5.154989],[-1.873201,5.889612,-3.183398,6.028039,7.782737,7.695937,-7.050804,-3.845409,-0.819448,-7.939154,1.571366,5.055323,-8.244669],[7.669500,8.522118,4.153737,-1.049020,-3.511134,3.166199,-3.794175,6.103129,5.636397,-1.227255,-3.864209,-7.367903,-6.445908],[2.353105,3.389305,5.066254,1.576047,-0.635816,-3.093221,4.432647,-2.229176,-2.344458,-1.777739,-1.076518,0.475435,5.302230],[0.416566,9.389111,-2.454486,-0.464962,-5.962321,-0.498140,-9.043978,6.353356,-3.890982,-0.190837,5.349722,4.573201,-5.567645]]], dtype = "float64")#candidate|6424|(5, 5, 13)|const|float64
bop_6425 = relay.not_equal(call_6421.astype('bool'), relay.reshape(const_6424.astype('bool'), relay.shape_of(call_6421))) # shape=(5, 5, 13)
bop_6428 = relay.not_equal(call_6422.astype('bool'), relay.reshape(const_6424.astype('bool'), relay.shape_of(call_6422))) # shape=(5, 5, 13)
output = bop_6425
output2 = bop_6428
func_6433 = relay.Function([], output)
mod['func_6433'] = func_6433
mod = relay.transform.InferType()(mod)
output = func_6433()
func_6434 = relay.Function([], output)
mutated_mod['func_6434'] = func_6434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6352_call = mod.get_global_var('func_6352')
func_6353_call = mutated_mod.get_global_var('func_6353')
call_6443 = func_6352_call()
call_6444 = func_6352_call()
output = relay.Tuple([call_6443,])
output2 = relay.Tuple([call_6444,])
func_6450 = relay.Function([], output)
mod['func_6450'] = func_6450
mod = relay.transform.InferType()(mod)
mutated_mod['func_6450'] = func_6450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6450_call = mutated_mod.get_global_var('func_6450')
call_6451 = func_6450_call()
output = call_6451
func_6452 = relay.Function([], output)
mutated_mod['func_6452'] = func_6452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5330_call = mod.get_global_var('func_5330')
func_5332_call = mutated_mod.get_global_var('func_5332')
call_6455 = relay.TupleGetItem(func_5330_call(), 0)
call_6456 = relay.TupleGetItem(func_5332_call(), 0)
func_900_call = mod.get_global_var('func_900')
func_903_call = mutated_mod.get_global_var('func_903')
const_6464 = relay.const([-5,8,-10,5,-8,3,9,-2,4,4,-8,6,6,-7,5,4,2,-1,-7,-8,-9,-7,-2,5,-3,-5,-10,6,-1,3,-8,-8,-3,3,-7,-4,-1,-7,2,-9,3,-7,5,6,-8,-3,-10,-9,2,-4,4,-5,1,-9,6,-9,4,-1,-1,6,-8,8,-2,2,10,2,3,8,-1,-8,-7,-7,5,9,-7,-7,-7,-4,3,-4,-9,6,6,-8,3,6,-5,10,-3,7,-7,6,1,-5,-5,9,5,-7,-1,10,1,5,-8,-7,7,2,2,8,-7,10,-1,-5,-4,9,-5,3,-4,-3,5,-5,8,6,5,-3,-6,2,2,4,-10,-5,-2,3,7,8,8,4,-1,5,-4,-10,-3,-8,10,3,6,4,-6,-4,5,-5,-7,10,-1,6,7,-6,8,5,7,-9,6,1,-2,-3,8,1,-10,3,-8,-9,-7,-3,-8,-5,6,7,1,4,-2,-2,8,4,-6,9,8,-9,2,1,2,-6,2,-2,1,8,-4,4,4,10,-8,4,-9,-2,6,-3,-9,-9,-4,4,9,-3,-2,5,-8,6,3,2,4,3,7,-10,-8,-7,-10,-2,-3,-1,1,-1,-10,4,10,5,2,-5,7,7,-4,8,5,2,4,-5,9,5,-4,3,5,-5,8,-7,-5,10,9,3,9,-6,-1,7,4,9,1,9,2,6,-5,-6,-7,2,-6,4,4,-6,8,5,7,9,8,7,-5,3,-6,-4,5,1,-3,-7,-4,2,-8,3,4,7,-1,3,7,-7,5,8,-7,1,5,-7,-1,-10,-7,-8,4,-3,10,-2,-2,-2,10,6,10,-7,7,5,-2,-1,-7,-10,-4,9,-8,3,-9,8,-4,7,4,-2,-8,1,1,9,-8,-10,-9,-6,-9,9,-3,-9,3,-2,10,8,-10,-7,8,8,4,-10,-4,-2,-7,-1,9,-9,8,9,-5,7,5,-4,-2,1,-10,-1,-9,-7,5,7,2,6,7,-7,2,8,9,-2,-4,-9,8,-1,2,-3,10,10,-6,-9,2,5,-1,3,5,-5,2,5,3,-7,6,1,-10,5,9,-8,1,7,6,-5,9,2,-3,1,5,-10,-8,6,-6,-1,-6,-6,-4,-2,-6,3,-5,7,4,-4,6,3,-7,-9,1,-7,-2,-5,-7,7,3,9,5,-6,3,-1,5,4,-2,-4,6,-9,6,3,10,-9,9,1,-3,4,-8,-9,-6,7,-6,8,-4,-8,-2,8,-2,7,4,-7,6,6,-4,-8,-6,8,-8,5,5,4,6,-9,8,4,-5,-10,-10,-6,-9,-5,-9,-10,9,-9,-9,-2,-5,-7,-9,5,-10,5,-1,-4,-5,-9,2,-3,3,7,-7,10,2,-4,-6,6,-4,-6,2,-7,-1,-5,-6,-3,-2,-2,9,-2,-9,5,5,-1,-10,6,-1,1,9,-2,-6,-5,-7,-9,9,9,-8,-3,-6,2,3,10,-2,3,-8,-8,2,-5,10,-7,-3,-7,3,-4,6,4,5,-3,-6,-10,-5,-1,4,6,-9,-3,1,3,-1,2,-4,-7,2,-8,8,7,8,10,3,6,-1,4,2,-6,4,-10,-4,-9,-9,-7,7,-10,-1,9,-6,-3,7,-1,-5,-1,4,-9,-10,-5,7,6,5,1,6,-7,8,-1,9,3,8,-7,7,1,6,8,7,7,2,7,1,-2,5,-3,7,2,-2,-10,-7,-8,-4,-6,2,4,-5,-4,4,-5,-3,-5,6,8,8,-9,-6,8,5,4,9,-3,-6,1,5,10,6,-8,7,-2,-3,-10,10,-10,1,-4,1,-5,6,-8,-3,9,-6,-4,3,7,-1,-7,-4,7,1,8,-1,-1,-10,-8,-7,-2,3,5,-6,-4,-9,7,7,3,-7,4,-5,-5,-3,-9,1,3,-9,-2,3,1,6,-5,6,-5,-8,-1,1,9,-10,-4,10,-6,10,-6,-1,-2,9,-2,-7,5,3,10,3,-9,8,5,5,-8,7,-7,-3,7,-8,4,-3,3,-7,1,-2,5,6,-1,1,-7,3,1,2,-7,-7,8,-4,-8,-1,2,-3,-7,-7,1,8,-8,-9,9,7,4,9,-3,-10,-3,-2,-6,2,-6,-2,6,-5,2,-3,5,-9,1,-10,10,-7,-1,-9,-4,2,9,6,-5,2,-5,8,-5,1,-4,2,9,10,6,8,-2,1,6,9,-6,-9,-5,1,6,6,2,-8,5,10,-7,5,-9,-1,2,6,-10,-9,6,3,-3,-3,-6,6,9,7,6,-7,8,2,9,-10,-5,-4,-10,-2,-7,-9,-8,-6,-3,-4,5,-4,1,-3,-3,9,-1,-6,7,7,5,-9,-1,9,-10,-2,4,9,1,-6,-4,-2,-6,-9,8,-9,10,-7,4,4,9,-10,2,-10,1,9,1,-2,2,1,5,-7,9,7,-10,-7,7,-3,7,3,-9,5,6,8,1,9,9,-5,10,2,-3,8,-6,-10,-4,5,5,-7,9,10,3,8,-5,-10,4,-4,1,-8,5,-2,-1,4,8,9,-7,9,-8,1,1,10,-5,4,-8,-3,-8,-2,3,-7,7,10,4,-3,-8,6], dtype = "int16")#candidate|6464|(975,)|const|int16
call_6463 = relay.TupleGetItem(func_900_call(relay.reshape(const_6464.astype('int16'), [13, 15, 5]), relay.reshape(const_6464.astype('int16'), [13, 15, 5]), ), 0)
call_6465 = relay.TupleGetItem(func_903_call(relay.reshape(const_6464.astype('int16'), [13, 15, 5]), relay.reshape(const_6464.astype('int16'), [13, 15, 5]), ), 0)
output = relay.Tuple([call_6455,call_6463,const_6464,])
output2 = relay.Tuple([call_6456,call_6465,const_6464,])
func_6475 = relay.Function([], output)
mod['func_6475'] = func_6475
mod = relay.transform.InferType()(mod)
output = func_6475()
func_6476 = relay.Function([], output)
mutated_mod['func_6476'] = func_6476
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6533 = relay.const([[[-9,-3,-2,10,-5,-2,5,6],[8,8,-5,-5,-10,-7,9,2],[-6,6,1,9,2,-8,3,10],[-9,1,7,-6,4,-3,-3,-4],[10,-8,5,-5,-9,3,9,5],[6,-10,2,9,-1,3,-5,-4],[-7,4,-8,-9,3,10,9,-8],[1,-5,-7,-3,7,2,-4,-7],[-7,-5,1,3,-7,-6,8,1],[-3,4,-3,8,-4,-1,7,1],[8,-10,-1,-3,-3,7,2,-3],[-6,-4,-4,6,3,8,5,5],[-9,-4,-5,1,5,-1,5,1],[1,-10,-10,-4,-4,-4,-4,-4]],[[-3,3,5,-7,-1,-5,-2,-10],[6,7,6,8,6,1,-2,-4],[5,-2,-3,-1,9,3,-4,4],[2,-5,-5,-8,-6,10,6,-2],[3,-1,7,1,8,7,6,4],[-7,6,-2,4,5,-8,9,-4],[-6,-7,7,-8,1,-6,1,6],[-9,-9,-9,10,8,-7,-10,7],[5,10,1,4,-5,10,-2,-3],[1,1,6,5,1,-9,2,6],[2,-7,6,-5,-4,7,3,7],[4,3,-1,-2,-2,-3,8,2],[-7,-3,2,4,-4,4,-10,1],[-10,2,5,-4,-8,1,-8,8]],[[-2,8,10,10,2,-3,-4,6],[9,7,-3,-2,10,7,-6,5],[5,-2,7,10,7,-2,6,-6],[6,-2,4,10,-7,2,-3,1],[-2,4,6,-9,-5,-5,8,7],[-5,-3,-3,5,-1,3,-5,3],[-9,5,10,10,4,6,7,6],[-4,-2,-3,9,3,-7,8,6],[-6,3,-6,1,8,-1,-5,-8],[-9,8,-7,-5,10,-1,-3,-6],[-9,-7,1,4,-7,8,-6,-1],[-9,7,7,-10,-4,-5,-9,8],[-9,-2,2,4,5,-9,8,-5],[10,-3,-4,4,-4,-6,2,-1]],[[-8,-3,-1,10,-7,-8,-1,-2],[-7,-8,7,-8,2,6,-8,5],[1,8,3,9,-9,4,2,-2],[10,9,-1,2,2,7,4,6],[8,-9,-2,-2,7,-2,2,9],[4,-3,6,-10,3,8,7,-5],[8,7,-2,10,5,-10,3,-10],[9,4,7,6,9,-9,8,3],[-8,5,-7,9,6,-8,-1,8],[10,-9,-3,-8,9,-9,1,-4],[-2,9,3,-3,1,7,-10,4],[-6,10,10,-10,-7,-7,-2,-9],[9,4,-8,-2,-10,1,-4,1],[-9,-9,-1,7,9,8,4,-4]],[[5,-4,8,-10,-7,-8,7,10],[2,-5,8,1,-6,9,-8,3],[-4,6,5,8,-8,-2,6,1],[3,1,7,-1,4,-3,4,6],[2,-7,10,6,4,3,2,-9],[1,6,-3,3,8,2,9,-7],[-1,-6,2,1,2,5,9,6],[-6,-9,3,8,5,1,-7,-5],[-7,-9,4,4,-3,7,4,3],[-10,-1,-4,2,7,5,6,-2],[10,-1,-9,-8,5,-6,1,-1],[2,3,8,-9,-1,-1,-4,-1],[4,9,-6,-8,2,-1,3,-5],[-1,5,4,-8,-8,-5,2,5]],[[5,-9,-10,-3,3,7,-6,-3],[1,-10,-1,1,5,-10,-9,3],[10,6,-1,4,4,7,6,-7],[-7,-1,5,-6,7,7,2,1],[-4,-1,7,-8,-7,-1,7,9],[4,2,1,10,-5,-5,1,-8],[4,-9,-7,3,1,6,-1,2],[6,-7,-6,-6,-5,10,8,10],[-9,4,-5,-9,-1,6,1,-1],[4,5,-4,10,3,-3,10,-2],[2,5,3,4,1,7,-10,1],[6,-3,-9,8,-5,-1,-6,-1],[9,8,2,-5,3,-4,-2,-4],[-3,7,-2,-1,7,1,5,4]]], dtype = "int64")#candidate|6533|(6, 14, 8)|const|int64
var_6534 = relay.var("var_6534", dtype = "int64", shape = (6, 14, 8))#candidate|6534|(6, 14, 8)|var|int64
bop_6535 = relay.less(const_6533.astype('bool'), relay.reshape(var_6534.astype('bool'), relay.shape_of(const_6533))) # shape=(6, 14, 8)
output = relay.Tuple([bop_6535,])
output2 = relay.Tuple([bop_6535,])
func_6542 = relay.Function([var_6534,], output)
mod['func_6542'] = func_6542
mod = relay.transform.InferType()(mod)
var_6543 = relay.var("var_6543", dtype = "int64", shape = (6, 14, 8))#candidate|6543|(6, 14, 8)|var|int64
output = func_6542(var_6543)
func_6544 = relay.Function([var_6543], output)
mutated_mod['func_6544'] = func_6544
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6553 = relay.const([[[8.586362,-8.385193,-1.371129,9.298300,-7.438283,-4.363468,6.484886,9.248316,-2.905545],[-9.993443,-2.498056,9.007776,8.251192,1.948762,0.673926,-9.615352,9.220586,-4.258406],[-0.364698,6.754383,5.733987,2.225160,-9.579058,2.232051,-0.382163,9.343416,-8.378571],[-0.660675,-7.112722,-7.058098,-1.139700,-5.171878,-6.665780,8.212891,5.296897,3.312091],[0.012186,2.247337,-0.881317,-7.929720,-8.058392,4.415762,-7.269025,-4.665019,0.744499],[3.103003,1.414992,5.356718,-5.104062,-0.357116,1.261529,-2.224331,-6.578370,1.750443]],[[-6.706965,8.503862,4.616256,-8.805751,9.067331,0.236486,5.060247,-0.243360,-9.029772],[-2.672306,1.254383,-6.805884,5.163794,3.549087,-0.270474,-2.271104,-8.293283,6.649418],[-9.463708,-1.610159,-3.429121,-5.776122,-2.439367,-7.478298,-5.992487,3.512826,2.890400],[-2.977536,7.839035,-0.271105,-0.690631,-3.540601,6.349607,3.025178,4.104468,5.734192],[8.400443,-4.304871,-7.657695,-6.064535,9.947983,-6.467350,-8.026071,8.644093,-4.287248],[9.249181,-7.849409,-8.547753,-7.512016,0.366404,2.061992,8.927544,-6.771241,-0.341271]],[[2.107219,5.466333,-3.119473,4.033117,5.650832,-4.221727,9.895814,-5.879018,-7.100652],[2.866318,-9.415697,-1.776082,0.168171,-5.969426,2.675013,-8.377005,-7.970170,-3.741454],[-5.066253,9.281157,-7.670519,1.373001,1.452100,-3.706478,-6.005970,-6.414015,-4.973162],[-0.868950,3.581055,-6.667487,0.623470,3.174994,-2.502608,0.137095,5.156836,-2.886196],[-7.914848,9.257669,-1.426514,5.906321,9.568948,5.836604,5.289772,9.373600,8.391191],[1.328608,5.998881,-1.377858,-4.190743,-6.535380,-9.298556,-2.486354,-7.758803,-9.220409]],[[3.116182,-7.259840,-4.731549,-2.945048,3.338057,-8.490306,3.089663,-4.407260,-7.535293],[2.505412,-6.691053,-8.349447,-2.280525,7.577958,7.793826,9.267034,-5.813847,3.701315],[-1.811340,-4.613615,-9.354141,-5.383173,-0.460080,-2.091068,7.862511,-8.424490,5.441786],[-5.258477,7.538150,-2.560576,0.732006,7.294897,1.362546,-2.042819,-3.657845,-1.351769],[4.010457,2.244779,9.941578,-8.294523,4.875732,-6.377994,-1.793708,-6.047203,-7.987332],[-8.742233,4.280177,4.163324,-4.739581,-2.738677,-3.656486,1.087285,8.790799,-6.273588]],[[-8.866365,7.391284,1.338347,-6.210517,-7.777030,5.496217,-1.324246,-0.232440,1.551908],[-7.009638,-4.256909,-6.470046,2.347264,-8.763570,-9.854930,0.081119,-4.311764,-7.938796],[-4.792737,2.854763,-1.537124,-9.013812,-6.122941,-3.051690,-3.945170,2.109845,0.923743],[-5.930446,-9.663964,5.860626,2.514029,6.156013,7.606972,2.189573,8.368232,-4.437653],[0.247925,-2.637091,9.603191,2.140800,9.026468,-5.998183,-3.248370,-0.075576,-5.530964],[-8.458572,-9.015359,8.151845,0.979709,-6.187947,7.930903,-9.394990,8.137857,-7.039272]],[[9.127739,-2.859452,-9.429600,7.356038,8.795295,8.619112,9.111956,5.390168,-5.932881],[6.769828,7.730116,-6.803908,-8.726547,1.740839,3.266944,5.596639,0.655332,0.030086],[-4.257473,0.727110,-9.774423,1.241239,-9.149577,-1.748854,2.072311,-2.907251,8.948095],[3.012149,-1.724299,8.209740,-4.202643,-6.476017,-4.680015,-6.821126,3.946189,2.249246],[-6.132434,4.259140,6.450470,5.496683,-4.580271,-8.671468,-3.863689,4.641862,-7.002915],[-9.982833,4.948945,9.225284,4.496555,3.419302,6.775537,-4.769514,5.452808,-4.695065]],[[9.699842,-3.603347,0.895499,4.899270,-1.051970,-2.773158,2.771259,-4.311177,-8.724507],[2.542915,0.290981,-6.076275,4.811928,-2.184151,-7.930660,0.475420,2.317774,2.505312],[-8.975958,-1.457534,-3.332511,-3.098007,-7.532603,-4.215152,-6.130317,-6.996872,-6.591716],[-7.340585,6.664706,6.949287,6.764827,-5.680616,-5.894210,4.963202,-6.053079,8.718899],[9.503100,6.478349,-3.018090,-8.441188,6.395992,-3.570361,6.012307,2.434507,-8.116508],[-6.555153,9.550059,-6.226883,8.658531,7.383328,7.216709,-8.604455,-5.566115,-7.459335]],[[9.177334,0.698193,9.109178,0.973932,-5.719404,-5.069797,7.434080,-7.325870,8.203193],[-3.848240,-1.570521,-2.762694,-1.988463,-9.413453,-2.055279,-5.902980,7.385990,-3.231410],[8.590291,7.834743,-9.289990,-4.656286,4.480478,8.490094,0.569789,7.192732,4.641929],[-5.377189,-9.817512,-4.300852,1.974150,-6.592215,-6.441556,-6.754004,-4.108250,8.968470],[8.118593,-1.565930,-9.992039,0.427372,2.834141,3.935251,-1.163750,7.465713,5.068989],[-4.077390,-1.000670,3.975609,5.852522,-4.563112,-0.314509,4.966671,-9.455027,-7.172360]],[[2.454622,-1.955021,-9.088840,1.008230,0.284792,5.924576,-8.933665,-3.944145,-7.393151],[2.155686,5.910196,-9.049120,2.222091,7.301723,4.410285,-6.749927,5.974805,-6.069439],[-8.292364,-9.224491,-9.703807,-4.034137,3.551468,3.103285,9.242430,-5.521397,-2.877562],[-9.342696,-9.102020,1.195178,5.244572,-0.041851,7.896251,-4.310788,-0.668750,4.614842],[-5.491861,9.960095,-9.651707,9.719742,1.415149,-8.229696,-1.273374,5.960277,-3.323895],[8.759923,-2.148755,-7.683654,-0.548094,0.320315,-0.428619,0.249947,6.584940,-7.959324]],[[3.708597,9.594245,7.178735,-9.599168,-9.736439,-6.400780,2.113083,-3.784367,2.582815],[2.755475,9.228096,-3.523950,9.771451,-7.763156,-4.096724,5.476470,-1.880218,-1.741353],[-8.772109,-8.401325,-9.142309,-8.594118,-2.136080,6.006350,8.717103,4.312610,-5.010812],[-8.211224,2.057472,-6.527066,-2.940926,8.021611,-8.648058,-9.992207,-2.889272,9.594456],[-9.824380,-0.209104,-1.374872,-0.178707,-7.156769,-1.432142,-1.566138,4.565797,7.168149],[3.335372,6.367646,-0.032163,6.883598,-0.606182,4.594441,-2.827746,2.591232,-4.159567]],[[3.004370,-8.399727,-2.707874,-5.602824,7.585719,-0.410294,4.948848,-9.949253,-6.060789],[-8.338870,-3.205451,-1.555378,-9.056822,1.839644,0.250807,7.611090,-9.527291,3.801561],[-2.718883,3.596924,0.908803,-5.742443,-2.858876,6.215410,5.194190,-2.737866,-5.240674],[-4.592522,2.603427,7.955160,9.555589,4.200770,-7.543867,2.221701,-2.502254,-9.124293],[-6.084240,-5.307960,-7.420663,-7.005450,2.064014,3.189281,9.866471,-9.010671,6.464636],[6.174961,-3.718438,-6.387147,9.608475,9.682053,6.272525,1.552236,-5.067835,-7.526710]]], dtype = "float32")#candidate|6553|(11, 6, 9)|const|float32
var_6554 = relay.var("var_6554", dtype = "float32", shape = (11, 6, 9))#candidate|6554|(11, 6, 9)|var|float32
bop_6555 = relay.mod(const_6553.astype('float32'), relay.reshape(var_6554.astype('float32'), relay.shape_of(const_6553))) # shape=(11, 6, 9)
func_6450_call = mod.get_global_var('func_6450')
func_6452_call = mutated_mod.get_global_var('func_6452')
call_6560 = relay.TupleGetItem(func_6450_call(), 0)
call_6561 = relay.TupleGetItem(func_6452_call(), 0)
output = relay.Tuple([bop_6555,call_6560,])
output2 = relay.Tuple([bop_6555,call_6561,])
func_6573 = relay.Function([var_6554,], output)
mod['func_6573'] = func_6573
mod = relay.transform.InferType()(mod)
var_6574 = relay.var("var_6574", dtype = "float32", shape = (11, 6, 9))#candidate|6574|(11, 6, 9)|var|float32
output = func_6573(var_6574)
func_6575 = relay.Function([var_6574], output)
mutated_mod['func_6575'] = func_6575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6352_call = mod.get_global_var('func_6352')
func_6353_call = mutated_mod.get_global_var('func_6353')
call_6580 = func_6352_call()
call_6581 = func_6352_call()
func_2808_call = mod.get_global_var('func_2808')
func_2811_call = mutated_mod.get_global_var('func_2811')
var_6588 = relay.var("var_6588", dtype = "uint8", shape = ())#candidate|6588|()|var|uint8
const_6589 = relay.const([[2,7,5,-3],[6,-1,4,5],[10,-9,8,6],[5,5,7,-10],[7,6,9,-10],[-3,-3,7,-9],[2,7,-9,-3],[-2,-10,4,-10],[9,2,7,-2],[-3,1,3,-6],[8,-6,-6,-3],[-5,-9,-3,9],[-7,10,1,6],[7,5,-5,-6],[4,-4,-8,9],[2,-4,7,8],[4,-7,10,-10],[-1,6,8,1],[-3,-10,-3,-6],[-9,9,4,1],[5,-5,-1,1],[-2,8,-8,-9],[5,2,2,-1],[10,6,-7,-4],[-5,7,-3,-10],[5,2,8,-6],[5,-2,-8,6],[5,4,1,4],[4,-3,-8,-2],[10,8,-7,2],[-4,7,-9,10],[6,-6,9,-2],[9,-1,-8,-2],[7,8,-4,-8],[-7,10,9,-10],[5,4,5,-8],[1,3,-2,-8],[7,-7,-6,-1],[9,1,-3,-6],[6,-6,-4,-5],[-4,2,5,9],[6,5,8,-7],[7,-8,6,1],[-2,2,1,-10],[-8,-5,2,5],[7,-10,-5,-5],[-4,5,4,1],[-2,1,10,2],[-6,1,10,-6],[7,3,4,4],[-8,-5,4,-10],[8,-4,3,-6],[-3,-6,4,-10],[-9,-3,-1,-8],[-4,5,10,-6],[7,9,-6,-8],[2,1,-8,-7],[6,-10,6,9],[-3,-10,8,-1],[6,6,5,-10],[-9,-4,-2,6],[10,-6,-3,6],[9,-1,4,1],[-4,-9,-2,5],[-9,-8,10,8],[9,-8,-9,10],[-2,5,5,-3],[5,-7,2,6],[-2,2,-10,4],[4,-4,8,-1],[7,4,3,10],[-1,5,-10,7],[-7,6,9,9],[-3,8,-8,-10],[6,8,3,-7],[4,10,-3,8],[5,-7,3,10],[8,-5,-9,-1],[1,4,7,8],[1,7,-6,4],[-8,-8,7,-9],[7,1,-1,1],[-2,-3,4,10],[1,9,-4,-1],[-6,-5,8,-7],[-8,-1,1,-8],[-4,-1,6,6],[-1,-7,10,5],[-6,8,-4,6],[-3,8,8,-6],[1,-5,-9,4],[-5,-2,6,2],[10,5,3,4],[10,-10,2,-3],[1,9,8,-9],[4,-10,9,-2],[10,-10,9,-10],[10,7,6,-2],[-7,-9,4,-8],[7,9,-9,-4],[-10,-3,10,8],[-5,-1,-7,10],[-6,1,-6,8],[-6,-1,2,6],[-4,1,-2,4],[-5,8,8,8],[-8,-3,7,-10],[-10,1,-10,4],[-4,8,5,5],[6,4,1,9],[-10,-4,6,3],[6,-10,9,-10],[8,-10,9,4],[9,1,-9,-9],[-3,-7,8,-6],[2,-3,-7,-5],[-1,9,2,-5],[-9,-3,9,7],[-9,-10,4,3],[2,-8,-1,6],[-10,1,-6,5],[5,6,-3,5],[-7,9,2,9],[8,-3,-2,10],[-3,6,-9,7],[-10,-9,5,-3],[2,-6,-3,-8],[-4,-1,-1,-6],[2,-4,-2,5],[5,5,10,6],[1,6,-9,-9],[9,-7,1,-5],[-7,3,3,3],[4,9,9,5],[7,8,-8,-9],[6,-7,1,-7],[-2,-2,-8,2],[5,5,-7,6],[4,10,-10,8],[4,1,9,8],[10,-6,-4,-2],[10,-5,-10,10],[4,5,-8,-7],[10,10,10,1],[-7,-10,-5,-4],[-2,1,1,-5],[1,8,-2,-4],[7,-2,-3,6],[-9,-2,1,-1],[-4,-4,-6,-9],[-10,6,4,-4],[5,7,-8,5],[9,2,-3,2],[5,-4,6,8],[2,10,6,-6],[-2,7,6,-7],[-1,-5,-2,-4],[3,-8,3,7],[-1,-1,10,8],[-2,2,-8,5],[8,6,6,-6],[9,-10,-9,-8],[-3,-7,-8,-7],[-7,10,-7,-5],[-6,-4,-10,-3],[-4,9,-1,4],[-6,9,4,-6],[-4,-8,-3,8]], dtype = "uint8")#candidate|6589|(168, 4)|const|uint8
call_6587 = relay.TupleGetItem(func_2808_call(relay.reshape(var_6588.astype('uint8'), []), relay.reshape(const_6589.astype('uint8'), [672,]), ), 0)
call_6590 = relay.TupleGetItem(func_2811_call(relay.reshape(var_6588.astype('uint8'), []), relay.reshape(const_6589.astype('uint8'), [672,]), ), 0)
output = relay.Tuple([call_6580,call_6587,var_6588,const_6589,])
output2 = relay.Tuple([call_6581,call_6590,var_6588,const_6589,])
func_6611 = relay.Function([var_6588,], output)
mod['func_6611'] = func_6611
mod = relay.transform.InferType()(mod)
mutated_mod['func_6611'] = func_6611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6612 = relay.var("var_6612", dtype = "uint8", shape = ())#candidate|6612|()|var|uint8
func_6611_call = mutated_mod.get_global_var('func_6611')
call_6613 = func_6611_call(var_6612)
output = call_6613
func_6614 = relay.Function([var_6612], output)
mutated_mod['func_6614'] = func_6614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5444_call = mod.get_global_var('func_5444')
func_5445_call = mutated_mod.get_global_var('func_5445')
call_6657 = func_5444_call()
call_6658 = func_5444_call()
output = relay.Tuple([call_6657,])
output2 = relay.Tuple([call_6658,])
func_6680 = relay.Function([], output)
mod['func_6680'] = func_6680
mod = relay.transform.InferType()(mod)
mutated_mod['func_6680'] = func_6680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6680_call = mutated_mod.get_global_var('func_6680')
call_6681 = func_6680_call()
output = call_6681
func_6682 = relay.Function([], output)
mutated_mod['func_6682'] = func_6682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_6716 = func_2905_call()
call_6717 = func_2905_call()
var_6741 = relay.var("var_6741", dtype = "float32", shape = (5, 5, 13))#candidate|6741|(5, 5, 13)|var|float32
bop_6742 = relay.bitwise_or(call_6716.astype('uint64'), relay.reshape(var_6741.astype('uint64'), relay.shape_of(call_6716))) # shape=(5, 5, 13)
bop_6745 = relay.bitwise_or(call_6717.astype('uint64'), relay.reshape(var_6741.astype('uint64'), relay.shape_of(call_6717))) # shape=(5, 5, 13)
func_4823_call = mod.get_global_var('func_4823')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_6750 = relay.TupleGetItem(func_4823_call(), 0)
call_6751 = relay.TupleGetItem(func_4825_call(), 0)
output = relay.Tuple([bop_6742,call_6750,])
output2 = relay.Tuple([bop_6745,call_6751,])
func_6752 = relay.Function([var_6741,], output)
mod['func_6752'] = func_6752
mod = relay.transform.InferType()(mod)
var_6753 = relay.var("var_6753", dtype = "float32", shape = (5, 5, 13))#candidate|6753|(5, 5, 13)|var|float32
output = func_6752(var_6753)
func_6754 = relay.Function([var_6753], output)
mutated_mod['func_6754'] = func_6754
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6785 = relay.const([[[-3,9,3,1,-4,-4,-1,10,-6,-4],[-8,4,6,-3,-7,4,-7,2,-2,10],[10,-10,6,2,10,-6,3,-2,-5,1],[-5,4,9,-4,8,6,7,1,-9,9],[7,8,3,-2,5,10,10,4,1,10]],[[-3,9,6,7,-1,3,-10,-1,-2,-1],[6,-7,-7,-6,10,-8,-6,-2,7,8],[-4,9,3,-6,2,-2,-1,5,-9,-6],[10,-9,-5,1,-10,1,1,7,9,-8],[3,9,8,-3,4,-3,7,3,5,-1]],[[2,-9,1,8,3,1,8,1,-2,1],[6,-4,-10,-3,10,9,8,-6,8,-9],[2,7,9,-5,2,1,-4,1,10,8],[-9,-4,9,-6,-6,9,6,-9,4,10],[-10,6,-3,-7,-10,-5,-5,4,10,10]],[[8,5,5,-10,8,9,-8,3,1,-6],[-6,-9,-9,5,-6,5,-4,7,6,2],[-7,1,5,9,-5,-10,6,-2,-4,-4],[1,4,4,7,-9,2,-10,-3,9,3],[-7,-5,-2,-7,3,9,-5,-9,4,-6]],[[5,-1,5,9,6,-9,5,-7,10,-5],[9,5,5,-10,-10,-4,-8,-9,8,6],[10,-8,-9,3,-1,2,-2,-4,3,-8],[2,-7,6,3,3,-10,5,9,-5,3],[1,-5,-2,-10,5,-7,9,-7,-9,-6]],[[10,-7,-4,-6,9,6,-5,-10,2,-2],[-7,3,-3,10,-1,-6,4,3,-2,-8],[10,-10,5,-2,2,-3,4,-7,-8,-1],[-3,9,2,5,5,-4,5,10,4,8],[-9,-4,-9,-10,-8,-8,-9,8,1,7]],[[9,2,3,-6,5,2,-7,7,-9,-2],[9,10,7,1,-3,5,-10,-6,9,2],[7,10,-4,9,5,2,1,3,-2,-7],[5,-9,-9,9,-8,-3,-7,-9,1,6],[-9,-9,-4,8,7,3,5,6,-8,3]],[[-6,-2,-1,-5,1,8,2,8,-10,-4],[-2,-8,8,3,6,5,-4,6,10,-10],[5,-10,-7,-4,7,-3,-4,5,4,-9],[6,4,-1,-7,-4,-3,-5,7,-1,9],[9,-6,3,-5,9,-7,10,-5,4,3]],[[7,4,-6,5,1,5,8,-3,3,9],[-1,-7,10,1,1,9,-9,3,-5,5],[4,8,-1,2,8,-8,-8,10,-6,-1],[7,7,4,-3,10,-6,8,-4,-6,3],[-10,3,-5,-7,7,7,7,-2,-6,1]],[[-1,-8,-5,-7,1,-3,2,-8,-10,-7],[-2,-1,-10,1,7,10,2,-6,10,-6],[-5,1,-4,4,5,-2,-8,7,7,-2],[1,2,-9,8,4,-2,2,8,-6,1],[6,8,8,1,-3,-10,4,8,2,7]],[[-10,7,-6,-8,-7,-4,4,-6,7,-10],[10,-5,-3,10,-8,3,5,2,5,4],[10,-7,-7,-1,-10,-5,8,-5,-4,6],[9,4,1,7,-5,-2,-6,1,1,10],[-10,2,-6,1,-9,5,-8,5,-2,-9]],[[-3,2,-9,-3,-7,-2,7,-7,8,-6],[-6,-8,-10,8,-5,-1,-8,-6,-7,7],[-3,1,10,6,5,-8,2,7,-9,4],[-2,10,7,6,8,-8,-10,-2,6,-2],[-9,1,-4,-1,-5,-7,-9,6,-7,-10]],[[4,6,4,6,-8,-10,-7,-8,1,-6],[-6,3,1,1,-2,3,-8,1,8,1],[-4,-5,-2,-3,-6,-1,-3,-8,-6,2],[-2,5,5,2,-3,-1,4,9,-3,-2],[1,-1,-10,1,-10,5,8,-9,-5,-8]],[[4,5,-9,5,-7,1,10,6,-1,-5],[10,2,-9,-2,-4,5,2,-7,6,-3],[8,-3,-7,6,4,8,1,-3,-3,-7],[7,-4,-3,10,-2,2,-8,-8,-4,3],[-8,-5,3,1,4,2,3,-10,8,6]]], dtype = "uint64")#candidate|6785|(14, 5, 10)|const|uint64
var_6786 = relay.var("var_6786", dtype = "uint64", shape = (14, 5, 10))#candidate|6786|(14, 5, 10)|var|uint64
bop_6787 = relay.less(const_6785.astype('bool'), relay.reshape(var_6786.astype('bool'), relay.shape_of(const_6785))) # shape=(14, 5, 10)
output = bop_6787
output2 = bop_6787
func_6795 = relay.Function([var_6786,], output)
mod['func_6795'] = func_6795
mod = relay.transform.InferType()(mod)
var_6796 = relay.var("var_6796", dtype = "uint64", shape = (14, 5, 10))#candidate|6796|(14, 5, 10)|var|uint64
output = func_6795(var_6796)
func_6797 = relay.Function([var_6796], output)
mutated_mod['func_6797'] = func_6797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3834_call = mutated_mod.get_global_var('func_3834')
call_6805 = relay.TupleGetItem(func_3833_call(), 0)
call_6806 = relay.TupleGetItem(func_3834_call(), 0)
func_4823_call = mod.get_global_var('func_4823')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_6811 = relay.TupleGetItem(func_4823_call(), 0)
call_6812 = relay.TupleGetItem(func_4825_call(), 0)
func_2727_call = mod.get_global_var('func_2727')
func_2730_call = mutated_mod.get_global_var('func_2730')
const_6815 = relay.const([3.888817,-8.162052,9.408456,-2.432931,9.469604,0.110066,-2.276713,5.699526,-9.731873,-5.503103,8.377894,2.616753,5.638099,-4.438806,-2.535904,7.972929,2.736011,8.988150,4.670257,-7.652186,2.301349,-2.512966,-0.099507,-4.035814,-8.184263,0.868822,-6.552459,-1.965244,-5.120357,-2.922136,-7.822658,-2.881119,4.368385,-4.383322,2.660612,-4.649893,3.243312,-8.297993,-3.747497,-4.224730,3.008543,-4.464150,-1.861803,7.534765,8.265366,9.804412,-2.755170,0.582618,9.516620,-3.824713,-4.971402,-7.128924,5.088371,4.263965,1.633355,-0.531061,5.153689,-0.868502,-5.596516,3.321352,-6.193276,0.003578,-5.449929,-0.082438,2.128809,4.713643,1.639416,9.591486,-4.511782,2.366581,-5.941291,1.619718,-2.877070,1.052649,6.015315,4.206177,0.370881,-9.534467,2.999920,7.303346,-4.455381,6.551566,-1.202028,-4.642209,7.523343,-3.096425,-0.520720,-8.660208,-0.269301,1.231145,-2.323304,5.455935,0.036138,0.085134,-9.169250,9.408825,9.662515,7.826384,9.809044,1.853154,7.160101,-3.661559,2.944990,-4.044443,-2.960101,6.685693,-1.909568,-6.966244,1.923397,3.161086,3.354471,-3.200598,0.345118,-1.194458,0.019257,0.666424,-5.683254,-5.534504,-9.524065,7.547183,-1.417019,5.164215,5.744932,3.483973,-4.547296,-3.233092,2.007150,-1.686239,-2.202109,-8.008985,-0.029868,-1.020067,0.206579,-0.974419,-4.834374,4.865219,0.234472,4.729518,-9.476874,5.645953,9.009354,-4.975811,-5.577552,7.245057,-0.811657,-7.827593,-9.310917,6.849166,-5.760162,3.132454,1.941082,1.167496,-7.012026,6.195429,2.025643,0.333815,-8.360589,-0.228513,-7.521752,-0.809736,0.794431,-2.531038,4.563616,5.045157,4.431007,-7.800818,1.468541,2.209894,1.774322,0.631886,2.134708,4.321230,-1.950009,-5.233808,-8.570020,2.827226,-3.042135,6.574941,8.531608,3.881232,6.277662,9.307131,9.586252,-8.005012,7.887846,-4.079711,-2.732792,6.564458,7.317256,-5.804025,-5.874289,6.833315,5.582747,-0.555847,0.707426,4.572682,-2.206714,-9.700261,-5.783980,-5.787826,-8.398986,-6.404638,-8.093299,6.380313,-3.595654,6.063967,-3.908369,8.385935,7.445986,-2.691370,8.107592,-4.416999,4.884214,3.842690,0.276014,3.842266,-6.969714,1.299730,7.775897,-4.103006,-7.637973,-5.938532,-6.879332,-0.481030,-2.359280,7.476723,-0.555771,6.013511,-1.892158,8.139417,-4.766007,4.544407,4.323821,9.132671,4.502309,-2.587372,-0.812801,-0.580018,-0.829514,-8.766043,-4.999695,-9.204019,4.997520,-8.786696,-0.442003,-1.997352,-9.395312,-5.641056,-4.337069,1.965388,3.053589,5.944372,-3.471731,4.692905,-8.226602,0.597799,1.591202,8.929680,7.912213,-1.098355,-4.650911,-2.442671,-3.291264,-7.023785,8.256051,-6.280237,7.557329,-7.022296,-7.131336,-1.455041,3.225547,6.423927,9.543896,-2.819121,-4.098946,-4.528174,0.098732,0.442809,1.916304,-3.913899,1.753712,-5.204623,-9.056603,9.417044,-9.608117,7.784885,5.258420,-4.768758,3.489453,-1.109228,1.760228,-5.889682,6.589515,-1.293303,3.398324,9.320350,9.486772,4.237363,-1.812736,-3.618701,-9.144619,4.277631,-7.239575,-9.511564,-1.086527,6.308258,-7.271083,-0.646231,-2.019551,-0.627585,1.697244,-0.413496,7.699021,-4.074062,-6.205236,-3.498861,-7.989711,7.386735,9.594812,-4.782263,-7.039704,2.149814,-2.335947,-3.707521,-1.153974,-5.484664,1.881343,8.851014,9.692472,-5.018044,-3.700968,-4.594470,-1.660236,-2.834112,-2.438407,2.951352,-1.733712,1.143731,-4.620980,3.481797,-3.206911,-9.153946,6.440675,5.471278,1.792301,-1.230172,-4.414145,-7.476695,-2.911909,2.914258,-1.550749,6.495907,8.967850,1.071500,1.818358,1.442700,-3.353288,0.956968,0.749757,-2.652173,-8.546072,-0.300310,-1.828972,-3.220160,9.672390,8.268376,-5.482622,5.645399,7.351223,-6.647824,3.510494,-0.154230,1.495008,9.941061,-7.285496,-8.231016,3.521122,-8.974629,4.541013,-1.067443,-5.631558,-1.240730,1.437810,-0.049203,-7.119441,4.208207,-3.262588,-9.551724,0.557154,-2.925163,6.560209,-6.184943,-2.426388,-3.713273,1.730676,-4.782792,-8.450724,9.227489,-2.497519,-2.299531,-9.353360,8.449540,-4.505111,-9.230076,6.855130,2.600539,9.495605,1.225198,-4.479718,-3.736093,4.540654,7.882666,3.785543,6.240071,3.513687,3.982563,5.917529,-2.028430,-1.280820,7.033157,-5.302000,-2.082591,-9.113548,1.223861,-0.032472,7.136722,-0.460377,5.456627,9.080264,-3.360618,5.477469,-1.427598,-9.278757,-9.898412,0.568526,-9.879292,-5.264876,-6.985066,5.329005,-7.620788,0.099182,7.942979,-5.394696,0.009354,3.023502,-1.399313,8.847196,8.195039,-5.346656,-6.086986,5.119000,7.023070,-9.684933,-8.993446,8.002045,4.712122,-8.743696,-9.961914,5.045414,-8.982922,6.936767,8.496503,0.988320,-5.991989,-6.173043,-5.669746,-6.314727,-3.149327,9.817560,-0.443227,6.150506,7.847179,-7.462472,-0.783705,5.077818,-0.199235,-4.804601,-2.036490,-9.621361,5.032346,7.097334,-4.741951,3.423017,-6.675659,1.850121,1.170418,-3.133478,3.045211,-2.470254,3.830262,-5.898482,5.198800,4.724397,8.837579,-3.594128,4.945030,-0.340736,7.759386,-5.451236,-2.404466,-3.098374,-0.036415,-0.851862,2.291965,0.325740,-7.890276,-2.220835,-7.410929,8.296439,9.162216,-1.531971,-9.837961,-6.274068,-2.755546,0.384324,4.715138,-8.834582,7.097574,0.434182,-3.936038,9.177600,-0.162305,-6.920164,2.496610,-8.740749,3.972314,0.916120,7.177685,-7.780071,-4.956632,-5.399033,4.874482,3.483250,5.544759,-2.771442,-2.853140,6.172563,7.539773,2.670390,7.729602,-1.755252,0.791182,-8.121756,3.180848,-6.767069,6.358286,5.339483,-0.365633,4.753650,9.606703,8.785100,6.636154,3.319773,-7.643506,2.909435,-4.805272,-4.222980,-6.376066,6.071753,2.183243,7.059908,-2.566983,-6.292705,-0.249194,9.317605,9.185251,6.754695,0.060587,8.010396,5.069498,5.256734,-7.646551,2.475556,0.017166,7.963800,5.143537,5.574308,0.940111,-2.845618,9.089383,-5.588913,-0.055590,6.416826,-5.353430,2.613209,3.556646,6.888480,-1.530680,-1.438888,0.457606,6.453336,9.384412,7.905769,-6.355600,-9.155370,3.679009,-8.135753,-3.480328,8.536935,-4.503442,-0.127540,8.700949,-6.399529,5.790340,1.216860,-3.815522,3.196865,2.910079,-4.971926,-2.144082,2.229253,5.080497,8.020170,9.933789,-8.374506,6.405564,-7.660318,7.804977,-9.395641,0.628072,9.845382,-9.263866,5.440572,0.499617], dtype = "float32")#candidate|6815|(624,)|const|float32
call_6814 = relay.TupleGetItem(func_2727_call(relay.reshape(const_6815.astype('float32'), [2, 312])), 1)
call_6816 = relay.TupleGetItem(func_2730_call(relay.reshape(const_6815.astype('float32'), [2, 312])), 1)
const_6821 = relay.const([4.483050,1.719558,9.496280,-7.151700,2.266194,-6.584442,-1.223447,0.041222,2.887510,1.425940,4.499633,-1.759500,9.217095,-6.677319,-8.417162,-8.805021,-4.482666,-8.839022,-6.085785,5.988581,-1.139303,-0.747694,7.225372,5.797952,-6.656457,-3.212590,-1.704806,4.940424,3.746526,0.153221,8.376476,7.394709,2.509330,-6.340285,-0.442508,9.417328,5.258118,-5.030777,-8.281148,7.592020,-5.682331,-1.835436,-2.580363,-3.766252,4.022340,0.010639,-9.539776,-9.604761,-0.061938,7.814338,-0.322632,3.053718,-9.407550,-4.113776,6.850135,0.571439,-5.427797,-6.367871,-5.181847,-3.881522,-1.032404,-7.077742,-5.606318,9.083053,4.449636,-3.757646,6.660808,3.295332,9.875180,-3.533623,-9.295432,-8.150969,7.415856,9.582969,1.265071,3.349511,-7.938085,-6.662576,-8.994532,7.882589,-5.691927,7.422209,-2.904517,5.929561,0.314071,-7.624497,-3.423992,-1.796174,-8.652992,9.396885,7.546517,1.061752,-6.557045,-3.689534,0.597149,7.883814,2.579553,-6.409991,7.884131,4.921550,4.793793,-0.222035,-3.869264,-7.894928,0.119050,3.342129,-7.759107,-5.251706,-7.518460,-5.844082,-2.070285,-3.089973,-3.616222,1.032724,-1.177056,-0.965082,4.987579,6.903008,1.755113,-9.338828,4.857000,5.621439,-1.934853,6.153489,3.745940,2.201620,1.477225,9.966622,-6.052106,3.841961,-7.911013,-0.109540,2.651408,6.407642,3.094650,9.789524,9.119094,6.598804,-9.248648,2.115702,-3.538401,4.979315,-1.729581,1.848265,-8.481794,2.609370,9.409095,-8.416808,-2.286079,9.168998,8.747054,-2.925522,-1.388302,-8.282132,-1.171599,-7.560172,-3.422971,-3.689067,-3.582266,5.327491,5.113144,4.877385,4.459950,8.771125,-0.237866,6.766628,8.496345,-1.939428,0.370903,-1.123579,-2.316767,-7.490326,-4.856663,1.655883,2.640966,1.111637,-2.958415,7.735557,-6.648371,7.269464,5.727331,-7.110736,-8.811301,-5.811533,-5.032229,-0.951878,5.959253,2.150727,6.138131,9.489317,-9.951351,8.206168,4.735894,-8.383641,4.446634,-2.362602,-7.509738,0.139983,-7.686625,9.593025,-0.502979,6.883406,-4.804274,-3.382690,-7.266335,-1.691197,-7.180678,2.044015,-5.849900,-9.093174,1.614846,5.945859,1.837442,-9.032820,-0.224099,-1.531635,3.667789,1.102013,8.271091,-9.022025,3.162564,-8.273549,-6.085683,9.901218,0.698032,4.763111,9.443858,-2.286407,5.065027,-7.182439,-5.133838,9.505209,-7.667620,-2.985648,-5.801185,1.390000,9.392515,8.686053,6.798216,6.399287,-5.660175,0.632684,5.248637,2.855717,1.220493,-7.998699,-0.989885,5.196988,-4.641946,-1.184240,-4.081967,-2.718579,6.031742,-5.861860,9.168533,1.336555,-4.342337,1.359452,3.635808,-5.204976,-0.071486,-8.944320,-9.597839,3.773811,1.841443,7.143976,-0.866292,-9.929648,-3.178086,-5.342749,-5.111447,2.010013,5.700444,-5.867252,8.899937,0.373578,8.228235,3.449957,0.231042,5.410943,-9.515444,1.969086,-4.673039,1.307933,-9.137261,-6.189548,4.188374,3.435484,-2.106421,8.575136,-6.840653,0.418443,5.978066,-8.440020,-3.218812,6.225252,-7.824648,6.028809,-4.511589,0.250421,-3.737468,1.158142,-3.204466,-3.507487,-4.210703,-9.419361,-4.423407,6.892139,-0.674833,5.626684,7.969723,-8.023906,1.472356,-6.129446,-8.068010,-7.028439,-4.464758,-9.103251,-0.322090,8.044039,5.255636,3.156006,-5.505230,6.642749,-7.545701,4.196093,2.396636,-6.626539,0.918565,4.389708,-4.062006,-6.865651,4.185781,1.978988,-6.737494,2.419834,7.208073,6.220921,6.715153,-3.971221,6.275199,4.044288,8.910463,2.088855,-2.230514,-6.126338,-3.105408,1.780087,-0.529733,4.033249,-7.103428,-1.321989,-8.365479,0.158752,-3.233669,1.588223,1.457935,-9.543552,-9.622964,2.642495,-4.049177,-4.261246,-7.437582,8.073794,-7.445068,7.882122,4.494604,-0.915347,-8.933626,4.132075,-4.510763,-5.099574,9.712309,-5.873102,8.614444,-0.460137,-5.025178,-3.494104,9.261578,5.741127,1.424816,-3.465481,-3.386937,-1.369040,-4.339666,2.029617,-7.733371,-7.160057,-6.369722,-9.306953,-9.302644,-7.793997,2.745661,7.302330,-9.388044,-4.300993,-2.588804,-5.934413,-3.003001,8.698491,-5.376500,1.475271,-8.087244,-3.177954,-9.941638,-7.479943,4.851757,3.394645,-3.561164,9.037178,2.325329,-1.279813,-4.639592,-6.314233,1.669419,1.908104,-4.708310,-3.819278,-5.612497,-7.519433,2.686114,7.151803,1.578018,9.572167,-0.060846,-3.263441,8.783000,3.935930,4.332314,-7.528981,9.787203,-2.185101,-2.364135,-3.046396,5.724904,6.284297,-4.307202,6.563293,-5.324225,0.296344,-6.436613,-0.407873,-1.033768,4.346092,-6.647096,-9.406305,-9.454993,1.016365,2.673817,7.461331,-2.318950,-7.961787,-2.086843,-0.083859,-0.673230,1.038674,5.234177,-8.756067,5.061121,1.813137,8.556047,4.191083,-2.182797,-6.685648,-2.175283,-2.104386,4.804108,5.872981,8.274796,-2.273447,6.696125,-6.403233,4.409221,-0.232716,-0.101237,-6.127999,2.152938,7.810948,6.560733,-9.992120,-7.741962,-2.318598,1.450173,7.518326,-0.170181,-1.598496,4.025909,-9.371746,-3.027242,8.518420,2.901925,-1.269943,9.015482,-5.261814,-8.816731,-7.819028,-3.406021,-9.872548,7.480595,-1.716534,1.696973,4.648160,7.071193,8.150855,8.163645,-2.130501,1.723819,8.921779,2.317270,9.478542,-8.221820,-1.154573,-8.049407,-0.135966,-6.439860,2.574387,-1.046090,-6.100854,8.727218,7.802428,-8.597926,0.861819,-3.362742,-6.175819,-9.881243,5.462280,0.386317,7.198127,-2.836875,7.158566,-3.618515,-9.041648,-1.445683,-4.742954,6.373713,-7.468834,-5.904391,4.361235,-5.121916,-4.410970,7.565125,-3.808015,9.715128,-8.688062,2.625204,-0.957178,2.061581,-0.135262,1.230706,1.751346,-0.901840,-7.000036,9.515106,-4.534726,0.012946,-1.920970,-8.302499,5.524299,6.638007,-1.373800,-3.398564,-7.703618,4.257830,4.681639,-4.852858,6.464903,-0.295483,1.212129,6.235606,8.957474,-0.108695,1.001177,-0.953361,-4.321697,5.489539,7.856416,3.081081,2.975013,-2.729608,6.484106,6.392562,-6.961310,-5.574969,4.028148,1.046884,-5.711973,-1.797854,-0.392454,-1.210040,-2.133580,7.021079,3.090861,-4.141540,-1.667765,0.704051,5.492255,-6.337403,-3.906184,3.170457,9.270657,7.755385,-2.565828,1.492636,-4.443414,0.727587,8.685229,-2.351505,1.148299,3.671466,-6.678598,9.014654,9.424228,0.839091,-3.561480,0.375679,2.110189,8.924709,2.011291,-4.225685,-1.514849,-6.431274,4.090253,7.369213,7.177004], dtype = "float32")#candidate|6821|(624,)|const|float32
bop_6822 = relay.maximum(const_6815.astype('uint16'), relay.reshape(const_6821.astype('uint16'), relay.shape_of(const_6815))) # shape=(624,)
func_6433_call = mod.get_global_var('func_6433')
func_6434_call = mutated_mod.get_global_var('func_6434')
call_6850 = func_6433_call()
call_6851 = func_6433_call()
func_3046_call = mod.get_global_var('func_3046')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_6856 = relay.TupleGetItem(func_3046_call(), 0)
call_6857 = relay.TupleGetItem(func_3047_call(), 0)
output = relay.Tuple([call_6805,call_6811,call_6814,bop_6822,call_6850,call_6856,])
output2 = relay.Tuple([call_6806,call_6812,call_6816,bop_6822,call_6851,call_6857,])
func_6861 = relay.Function([], output)
mod['func_6861'] = func_6861
mod = relay.transform.InferType()(mod)
output = func_6861()
func_6862 = relay.Function([], output)
mutated_mod['func_6862'] = func_6862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6413_call = mutated_mod.get_global_var('func_6413')
call_6868 = relay.TupleGetItem(func_6412_call(), 0)
call_6869 = relay.TupleGetItem(func_6413_call(), 0)
output = call_6868
output2 = call_6869
func_6870 = relay.Function([], output)
mod['func_6870'] = func_6870
mod = relay.transform.InferType()(mod)
mutated_mod['func_6870'] = func_6870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6870_call = mutated_mod.get_global_var('func_6870')
call_6871 = func_6870_call()
output = call_6871
func_6872 = relay.Function([], output)
mutated_mod['func_6872'] = func_6872
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6883 = relay.var("var_6883", dtype = "int32", shape = (2, 11, 12))#candidate|6883|(2, 11, 12)|var|int32
var_6884 = relay.var("var_6884", dtype = "int32", shape = (2, 11, 12))#candidate|6884|(2, 11, 12)|var|int32
bop_6885 = relay.bitwise_and(var_6883.astype('int32'), relay.reshape(var_6884.astype('int32'), relay.shape_of(var_6883))) # shape=(2, 11, 12)
func_2040_call = mod.get_global_var('func_2040')
func_2044_call = mutated_mod.get_global_var('func_2044')
var_6895 = relay.var("var_6895", dtype = "float32", shape = (624,))#candidate|6895|(624,)|var|float32
call_6894 = relay.TupleGetItem(func_2040_call(relay.reshape(var_6895.astype('float32'), [3, 16, 13]), relay.reshape(var_6895.astype('float32'), [3, 16, 13]), ), 0)
call_6896 = relay.TupleGetItem(func_2044_call(relay.reshape(var_6895.astype('float32'), [3, 16, 13]), relay.reshape(var_6895.astype('float32'), [3, 16, 13]), ), 0)
bop_6901 = relay.power(var_6884.astype('float32'), relay.reshape(bop_6885.astype('float32'), relay.shape_of(var_6884))) # shape=(2, 11, 12)
output = relay.Tuple([call_6894,var_6895,bop_6901,])
output2 = relay.Tuple([call_6896,var_6895,bop_6901,])
func_6905 = relay.Function([var_6883,var_6884,var_6895,], output)
mod['func_6905'] = func_6905
mod = relay.transform.InferType()(mod)
mutated_mod['func_6905'] = func_6905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6905_call = mutated_mod.get_global_var('func_6905')
var_6907 = relay.var("var_6907", dtype = "int32", shape = (2, 11, 12))#candidate|6907|(2, 11, 12)|var|int32
var_6908 = relay.var("var_6908", dtype = "int32", shape = (2, 11, 12))#candidate|6908|(2, 11, 12)|var|int32
var_6909 = relay.var("var_6909", dtype = "float32", shape = (624,))#candidate|6909|(624,)|var|float32
call_6906 = func_6905_call(var_6907,var_6908,var_6909,)
output = call_6906
func_6910 = relay.Function([var_6907,var_6908,var_6909,], output)
mutated_mod['func_6910'] = func_6910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2915_call = mod.get_global_var('func_2915')
func_2916_call = mutated_mod.get_global_var('func_2916')
call_6937 = func_2915_call()
call_6938 = func_2915_call()
func_6573_call = mod.get_global_var('func_6573')
func_6575_call = mutated_mod.get_global_var('func_6575')
var_6942 = relay.var("var_6942", dtype = "float32", shape = (594,))#candidate|6942|(594,)|var|float32
call_6941 = relay.TupleGetItem(func_6573_call(relay.reshape(var_6942.astype('float32'), [11, 6, 9])), 0)
call_6943 = relay.TupleGetItem(func_6575_call(relay.reshape(var_6942.astype('float32'), [11, 6, 9])), 0)
output = relay.Tuple([call_6937,call_6941,var_6942,])
output2 = relay.Tuple([call_6938,call_6943,var_6942,])
func_6954 = relay.Function([var_6942,], output)
mod['func_6954'] = func_6954
mod = relay.transform.InferType()(mod)
mutated_mod['func_6954'] = func_6954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6955 = relay.var("var_6955", dtype = "float32", shape = (594,))#candidate|6955|(594,)|var|float32
func_6954_call = mutated_mod.get_global_var('func_6954')
call_6956 = func_6954_call(var_6955)
output = call_6956
func_6957 = relay.Function([var_6955], output)
mutated_mod['func_6957'] = func_6957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_6993 = relay.TupleGetItem(func_2535_call(), 0)
call_6994 = relay.TupleGetItem(func_2537_call(), 0)
output = relay.Tuple([call_6993,])
output2 = relay.Tuple([call_6994,])
func_7017 = relay.Function([], output)
mod['func_7017'] = func_7017
mod = relay.transform.InferType()(mod)
output = func_7017()
func_7018 = relay.Function([], output)
mutated_mod['func_7018'] = func_7018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4228_call = mod.get_global_var('func_4228')
func_4229_call = mutated_mod.get_global_var('func_4229')
call_7019 = func_4228_call()
call_7020 = func_4228_call()
output = relay.Tuple([call_7019,])
output2 = relay.Tuple([call_7020,])
func_7027 = relay.Function([], output)
mod['func_7027'] = func_7027
mod = relay.transform.InferType()(mod)
output = func_7027()
func_7028 = relay.Function([], output)
mutated_mod['func_7028'] = func_7028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3963_call = mod.get_global_var('func_3963')
func_3965_call = mutated_mod.get_global_var('func_3965')
call_7043 = func_3963_call()
call_7044 = func_3963_call()
output = relay.Tuple([call_7043,])
output2 = relay.Tuple([call_7044,])
func_7055 = relay.Function([], output)
mod['func_7055'] = func_7055
mod = relay.transform.InferType()(mod)
mutated_mod['func_7055'] = func_7055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7055_call = mutated_mod.get_global_var('func_7055')
call_7056 = func_7055_call()
output = call_7056
func_7057 = relay.Function([], output)
mutated_mod['func_7057'] = func_7057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2915_call = mod.get_global_var('func_2915')
func_2916_call = mutated_mod.get_global_var('func_2916')
call_7096 = func_2915_call()
call_7097 = func_2915_call()
output = relay.Tuple([call_7096,])
output2 = relay.Tuple([call_7097,])
func_7114 = relay.Function([], output)
mod['func_7114'] = func_7114
mod = relay.transform.InferType()(mod)
mutated_mod['func_7114'] = func_7114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7114_call = mutated_mod.get_global_var('func_7114')
call_7115 = func_7114_call()
output = call_7115
func_7116 = relay.Function([], output)
mutated_mod['func_7116'] = func_7116
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7178 = relay.const([[[4.567325,-1.365938,1.370001,9.753996,3.552590,9.409058],[3.069438,-9.357343,1.828395,7.279130,6.459177,5.543738],[-0.503563,-6.526083,9.302362,-3.495116,-3.826543,-8.995417],[2.773647,8.866120,8.758542,-7.510680,-9.862156,5.604454],[4.283657,2.369966,6.348746,7.648247,-1.681129,-8.850435],[1.262920,-1.679740,-5.055711,0.355071,-2.701444,-9.404482],[7.625234,5.130767,-2.868507,-8.356729,3.738326,-8.645297],[-8.406579,-7.293870,-3.365792,-5.926735,2.263638,0.792864],[5.376444,-3.423575,7.431482,-1.068686,2.799578,2.923682],[-8.005816,8.506305,9.484794,-9.614327,0.693281,-5.715740]],[[-2.937489,-6.207426,7.351819,0.836739,-7.527958,-5.049065],[-9.468654,1.545737,-5.461552,8.717678,-7.265418,-1.544127],[5.766192,3.455742,6.626289,-2.522145,9.772033,-2.364771],[-1.737025,0.109435,0.539471,-7.954351,-0.934467,3.060663],[-6.436496,-4.985550,9.650611,-8.101750,8.559285,-7.071259],[6.971661,-0.479454,7.398742,7.614840,-7.576625,-5.886077],[1.481407,-3.030501,-7.966557,-0.084559,-4.330173,9.706609],[-3.297691,-9.714094,-1.351522,-9.408591,2.942318,-4.956824],[9.935801,-2.692507,-0.012311,6.709730,-2.209884,-3.831260],[2.860505,0.388421,1.487224,-6.503251,2.024860,3.072667]],[[3.148454,0.327182,7.591847,0.739405,-0.222047,-8.249750],[-2.167887,-1.221274,1.431748,-9.683566,8.911530,3.889648],[-0.320907,-0.411270,-5.935260,8.665819,-4.302767,9.277791],[-2.855834,-6.755719,-1.170115,-3.618469,8.920575,1.564719],[2.686108,2.440458,-7.654386,0.967081,-6.235797,-2.153220],[7.544046,-2.630815,-1.001328,3.794840,-6.000860,6.049995],[6.360928,-2.527073,-6.284631,7.539591,3.126101,7.944213],[1.917453,-1.711193,-0.732392,7.050850,8.557092,1.023232],[7.009349,-3.381024,6.952081,-0.668043,2.889823,5.409294],[1.928487,4.345000,8.883564,-3.349691,9.914525,0.278172]],[[6.886405,-0.531712,-6.851558,-3.102795,-3.950496,-8.730633],[9.622576,-6.508717,5.893879,-5.451524,1.237378,4.593636],[-3.893584,5.084684,-9.944118,-5.065120,0.414949,-3.015373],[-1.920150,2.809579,-6.511697,-6.917778,4.064279,-1.038284],[-2.289712,4.674728,3.336810,6.081849,-1.587711,6.735859],[4.289071,-3.081595,-2.324310,-6.105206,6.236512,-3.104981],[6.514867,3.534262,0.704808,0.962000,7.241329,5.848620],[7.775342,-7.254853,-7.356733,9.603673,5.944276,-4.942236],[-9.141472,3.883091,2.896343,3.453504,-0.691983,6.489346],[1.576194,-1.126098,2.690854,3.264902,-7.441385,-7.558470]],[[8.051926,-8.573607,1.509969,6.199840,9.948182,7.563837],[-3.320823,-2.576420,-1.980583,-6.607129,-7.895801,-9.134443],[5.380621,0.700154,4.573523,-1.373434,3.649643,-6.138493],[4.004646,-5.931454,-7.116938,1.584985,7.570059,9.553183],[9.233770,1.730261,-6.144741,6.988793,6.723475,8.975666],[-6.912778,0.196073,-6.779047,-6.685953,0.130727,6.412151],[0.459058,-6.695681,-3.337649,-6.078347,-5.866019,8.737634],[0.645435,-8.280779,4.662175,6.348899,9.360402,9.198445],[-4.720558,3.612395,9.547986,5.382916,-2.683642,6.313587],[-7.734244,-1.417865,8.255009,4.059702,2.447344,5.234829]],[[-6.426400,-6.713347,5.863236,5.658042,-3.872369,-6.260883],[8.595736,-9.926637,8.281740,-6.398259,8.382266,-5.078101],[0.282158,9.153701,3.457082,3.932325,5.162045,3.787048],[-5.872333,4.739232,-5.755920,-5.361720,6.193104,0.446370],[-3.602162,-3.785632,-7.438103,-9.755139,2.825317,-5.900304],[-7.246131,-2.175113,-5.408678,-1.864630,-6.592357,3.460015],[6.215101,1.372565,-9.905943,-3.969076,-8.299716,-1.855854],[4.592189,-4.975833,-2.136726,-5.006805,8.142146,-6.252080],[-7.669025,-1.247405,-9.554890,7.416459,3.735219,1.156044],[7.662906,-0.057024,-5.607878,7.148600,2.058193,-6.809901]],[[-5.314156,-9.602162,9.870443,4.981814,8.016388,3.287056],[2.701968,-1.066194,4.430718,-9.402106,4.563569,-1.656557],[1.350841,7.560066,-7.691457,-8.545660,-4.184999,-6.697407],[-9.465718,-1.420420,9.375791,4.543771,-2.508276,9.769859],[6.000227,6.708395,-8.097151,6.972895,1.187104,-0.563954],[-5.164005,-7.519923,6.775335,9.641547,0.786018,8.037890],[0.069891,3.879044,-3.129267,1.029609,9.337716,-0.633528],[-2.268369,0.069810,8.582006,6.894189,9.384267,-2.492991],[-7.988640,-8.534092,1.569154,-6.031675,-7.926484,7.895035],[-3.099503,7.286105,2.551344,8.698732,3.104246,0.841640]],[[-9.928261,-5.726390,-2.964403,-7.761909,-0.870069,-4.857633],[1.298735,-8.912942,2.353899,-6.031039,-1.698998,1.581316],[-4.973609,-2.506205,3.359131,-0.113476,-8.969543,7.070356],[1.133636,-1.832361,-4.694855,-7.567132,8.736503,-2.991914],[-2.773138,8.709408,-6.081771,-7.235006,6.610262,-9.907722],[-5.194982,5.115493,3.675335,6.305458,-2.896088,3.098657],[0.672150,-6.936119,-4.035051,6.944698,-1.625927,-4.262787],[1.636027,2.399858,7.483310,9.999579,-5.985229,-5.623138],[-2.479229,-1.313031,4.662190,6.456516,6.875943,-2.981091],[-8.634803,-0.241046,-5.913359,0.737810,6.407304,-7.244294]],[[-7.745619,-9.488346,-0.964363,5.505858,6.322150,-5.759469],[6.774125,7.224896,1.362408,-2.460134,0.754069,-6.937429],[2.836633,6.262791,-1.523150,1.689462,2.893666,0.905596],[5.968187,-6.082932,1.852265,9.512649,2.599815,6.608533],[-8.035135,-0.631494,0.055213,0.381094,4.235029,0.175320],[1.702919,-4.293555,4.777592,-5.582122,-6.105522,6.555239],[0.550932,-0.823086,4.395420,-0.672206,-7.640062,7.657221],[1.522357,-8.428982,5.580253,7.612662,6.430741,9.227190],[5.886344,4.007740,0.165124,7.024711,2.379997,2.785135],[-9.314315,0.858132,-6.708676,-9.298883,4.279281,-0.903179]],[[-4.675315,2.311075,-6.403130,-6.980043,3.383161,3.423050],[-9.676087,2.861520,9.855468,-9.548240,-4.261365,-9.841141],[-9.874185,0.826489,6.860662,-3.736806,1.916712,2.060604],[4.427811,1.427103,2.303830,6.084159,-1.537182,-7.587456],[9.992420,4.866594,-9.300487,-6.147464,-6.404925,-0.537632],[-6.164258,5.394169,3.664551,4.451872,5.856922,8.150135],[2.739102,-5.795038,7.140630,9.740833,-8.718645,5.929861],[-5.863019,8.143601,6.277092,3.213240,3.842192,3.220205],[3.797151,8.826865,5.191000,-6.121952,1.588728,-4.525541],[0.393835,8.606201,-2.343450,-5.219330,-0.332287,7.799117]],[[9.361013,2.523765,-5.476351,3.418186,4.539309,-7.834374],[3.053738,-3.391669,0.286447,-5.974787,-8.625709,-8.515620],[-7.645591,-1.529624,3.062684,-5.563427,-8.395038,2.566609],[-4.723985,-4.607875,5.782947,-2.995432,7.282983,8.481393],[-1.500438,7.013939,3.431655,6.089009,-2.459185,-4.107116],[-1.504004,4.011503,7.150926,2.751920,1.819365,4.773070],[-0.475461,-4.211021,-8.800094,-2.478444,1.575460,-3.811293],[-9.898107,-3.999975,0.338303,-7.286227,7.481848,-9.852514],[-7.395116,-9.726118,6.139232,-8.759599,9.007523,-4.343234],[-5.457003,-7.744415,-3.428742,-3.834092,6.273556,-7.591124]],[[2.826826,-3.050395,-8.137228,1.977819,-3.947463,-6.918167],[-1.732008,5.349297,4.565449,9.445586,-6.886180,9.084655],[-2.173957,7.319318,-3.862303,-3.287100,-0.470180,-7.726085],[5.696013,9.049832,3.346968,-5.503884,-6.644741,-7.387253],[7.552755,0.342681,1.805671,-2.775823,-3.371147,9.600255],[1.967623,8.426294,-3.660867,-2.702095,7.829253,8.296628],[-8.923747,-1.941075,6.200621,-3.545934,8.591017,4.018153],[4.542257,-8.302522,8.708493,-2.143780,-6.537575,8.221035],[-5.024309,-5.244989,6.492184,-8.767690,2.686387,2.196382],[5.999347,5.389357,7.842695,-0.559200,4.220757,4.648607]],[[-2.460238,7.146945,0.334109,-1.178374,0.331872,9.228485],[-1.760859,-5.321331,4.602374,0.104330,1.935063,2.268464],[7.454153,3.956005,-8.162379,0.812790,4.256920,3.029192],[7.186312,-5.947508,2.956033,-0.686230,9.846743,7.568564],[-5.732726,-7.581997,-2.084850,-8.152899,0.570724,-7.240673],[-5.749341,-7.469613,-2.945915,-9.976878,9.205129,-4.002636],[6.649352,5.228653,5.178392,2.391838,5.166162,-8.592059],[9.013963,7.489571,-8.822039,-5.898635,9.748541,-2.251778],[7.781058,-3.379595,7.377484,9.367688,8.302497,-3.946358],[6.661677,-8.160121,6.219733,-1.448131,2.132333,9.034702]],[[6.484261,9.009658,-7.631510,9.857607,-8.378156,6.161280],[-2.848671,-6.242969,8.840556,0.060082,-8.930145,1.679880],[-7.429618,-8.690105,7.736068,0.324883,-4.363038,1.542753],[7.303824,-8.657578,-4.287368,6.834104,-8.614020,-8.251265],[-7.522780,-9.214633,3.314377,-3.484838,-6.245229,-9.727862],[-3.628160,-5.173162,-7.154800,-2.297600,-4.273705,0.946196],[-8.970424,-7.653542,8.911808,-2.970255,-3.012589,-6.769027],[-1.365566,8.971344,-4.395108,-3.185670,7.926059,3.857646],[-1.022129,1.549416,-5.009701,-5.728308,-4.752610,5.762024],[0.381867,9.798084,-6.067225,-6.677924,1.735706,4.515226]],[[1.788277,-3.580788,8.052531,-6.928949,1.599982,-0.239787],[-7.390004,-0.696345,6.265722,-9.780097,4.102426,-4.897976],[-1.694626,-1.467632,-3.050381,6.552796,7.557295,4.055613],[8.827165,0.256901,2.417757,-1.531507,-8.389075,-2.126150],[-6.912678,-5.516772,2.957062,1.739548,8.872495,6.008414],[-0.064963,6.650538,-6.152134,-0.340780,-8.255665,1.817611],[2.197389,-6.143285,-7.633900,-0.801067,9.019478,0.564911],[0.686137,-5.525357,-8.792257,6.429459,-1.182029,0.109584],[3.826125,-7.707716,9.214323,4.739943,0.308302,-0.110209],[6.180780,-3.629572,7.671381,2.944611,7.995213,-7.823954]],[[4.088771,-7.118316,-3.932963,-9.931792,5.732460,-7.215219],[-0.758451,4.386664,6.818333,-3.733516,-1.237638,7.055482],[-0.149435,0.295261,8.441856,5.510206,4.967294,-0.565935],[7.779481,2.658454,-6.023289,7.987617,2.635130,-0.524400],[-2.428415,8.554815,-6.971479,4.978172,5.741730,-5.892887],[-6.893075,2.723041,6.883534,1.634660,4.660968,0.604376],[-8.983184,-3.778300,4.396336,-0.677376,8.396428,7.834665],[5.517695,-1.953694,1.810175,0.123470,9.255259,1.865126],[-5.669458,0.174288,0.417500,6.573232,-0.455105,7.979519],[7.845029,1.549351,-4.977640,-8.380324,3.431123,-1.055582]]], dtype = "float64")#candidate|7178|(16, 10, 6)|const|float64
uop_7179 = relay.cos(const_7178.astype('float64')) # shape=(16, 10, 6)
uop_7194 = relay.acos(uop_7179.astype('float64')) # shape=(16, 10, 6)
func_6905_call = mod.get_global_var('func_6905')
func_6910_call = mutated_mod.get_global_var('func_6910')
const_7208 = relay.const([3,2,-9,-9,-5,-6,4,-8,5,-3,8,3,-8,-2,-4,1,5,5,-6,-5,-5,-1,-4,-1,4,7,8,5,8,-6,-4,-10,-2,1,1,10,-8,7,1,10,-4,7,-6,9,-8,6,3,1,1,5,9,-10,-8,8,8,5,6,5,2,5,8,4,-7,9,6,-2,1,1,-10,9,10,10,-3,7,9,-7,-3,-10,-5,-8,5,5,3,-5,6,3,-5,-1,9,6,-4,-7,-4,-7,8,-8,-7,-8,9,-5,7,-1,10,3,-2,7,1,-2,3,-2,9,5,-2,-8,6,6,-1,6,-10,1,7,9,4,-3,-5,9,6,1,4,-1,-5,2,3,-9,6,-7,10,2,-9,10,-1,-9,-10,5,10,-4,2,-2,5,-1,1,-5,6,-4,4,1,10,2,-10,6,2,6,-10,-2,10,-8,-1,-4,2,-4,-2,2,6,-4,1,-8,-3,-1,-3,-8,6,7,-10,-6,9,-9,-6,-2,6,-1,-9,-4,-3,3,-7,10,6,-1,-8,-9,9,-5,10,9,7,-5,-9,7,3,2,9,-1,9,1,1,4,7,-6,1,5,5,2,-8,-10,9,8,3,-4,5,2,5,-5,9,9,7,8,3,-10,9,9,1,5,-9,8,4,10,-10,-2,-6,-1,-5,9,-8,-7,8,-6,-5,6,-2,8,6,5,-4,-9], dtype = "int32")#candidate|7208|(264,)|const|int32
const_7209 = relay.const([-8.337205,-9.619450,1.430694,-3.897780,4.614187,-6.394041,-1.324435,8.922426,4.450579,6.579817,-7.272921,-6.913200,2.895719,-1.302905,-0.966058,-5.720138,8.265651,7.776011,8.887829,4.995691,-0.944253,0.982200,-2.138685,3.606802,-6.616365,0.758645,9.366510,4.854773,-7.775103,2.823111,-3.946469,1.380076,-6.472237,-3.029356,0.348965,-5.983205,-7.083391,-2.468275,-9.441120,-0.666739,-0.858473,-5.295327,-6.992666,0.516745,6.870621,0.951633,-4.551650,4.864643,1.596300,-1.247180,2.212083,-2.463766,-7.151042,-7.853494,-2.935711,3.940177,9.478664,-3.947745,-8.426653,-0.074789,-6.085537,4.058261,2.099807,8.004969,-8.274520,4.703984,3.228370,6.897722,-3.904789,-5.825100,6.366061,-8.749355,2.739023,-4.306937,-9.399924,4.021378,-7.907193,7.825316,0.386788,-0.726384,-6.054127,-2.890988,4.386685,1.404091,6.410520,7.591060,1.861604,1.632952,-7.227043,-5.527202,8.639441,-7.732745,-3.991408,0.315250,-6.017954,-9.464712,9.688879,-0.007298,-5.470996,-8.377924,-1.222510,-6.461083,0.999280,-7.868258,8.655186,-2.292034,4.971509,-5.883128,-0.079026,0.640040,5.118619,0.906113,-8.721680,-6.281918,0.130357,7.730106,-4.243697,-0.160164,4.435612,7.470651,8.385089,4.881807,-8.792737,1.859805,8.612277,-3.020716,-5.009280,2.619028,1.897901,1.395845,3.224091,-5.600320,2.505301,1.620145,-1.210627,6.037233,3.859169,-4.789850,8.678808,-4.112875,-9.166488,5.676231,1.912978,-6.685204,-4.430838,0.432676,-2.559259,0.880428,-5.731335,-6.240453,-2.100137,7.414413,3.286217,2.841888,2.020750,5.898599,-1.972366,-6.222824,-8.794727,0.665751,-8.370710,-9.131197,-8.818052,-9.234118,-3.100330,9.802220,6.562130,-5.063578,-8.751713,9.459786,-5.463705,-7.483257,0.379075,-1.264095,1.777171,9.687088,-8.354609,-5.556868,9.051696,-4.719628,4.242775,-1.865397,-8.932338,2.524713,1.278632,-8.720301,-0.408018,-5.408266,0.562963,0.211067,-1.866475,-6.030915,-4.945812,-0.656682,-1.905007,8.014118,-4.018344,-0.074941,5.863086,-2.553698,-5.691737,-6.419465,9.480681,-9.948078,4.018621,2.120099,-3.689166,-0.291690,-5.217513,4.371575,6.808013,-2.484896,-7.968432,-4.015776,9.308012,-1.769757,3.674823,-3.657803,-4.892260,4.911910,-3.618125,7.261435,7.611813,3.847324,-5.945158,-6.321349,8.659238,-2.649334,7.771966,6.304223,4.082126,-9.304602,-0.019837,4.693253,3.383657,-9.746977,1.028861,3.961275,-8.426697,-8.843690,2.182313,-7.401195,0.851873,-3.507496,-1.475490,7.152433,-0.078712,-4.333219,-5.347360,6.015387,2.527324,4.179960,0.330590,2.671851,4.281986,5.670753,-1.750362,-3.225318,-0.862879,-8.616519,-0.953391,-7.564282,6.506739,-2.814985,-6.955403,5.865869,0.971958,-5.847220,6.679305,-1.730911,0.250329,5.637239,-0.109509,8.671444,4.742150,5.630578,-7.248750,-4.012142,-8.817260,5.532997,-2.651415,-6.482171,-4.297671,-0.013814,-0.298167,-7.571566,-5.891334,0.015877,2.690530,1.224987,-6.570175,8.668301,-9.373326,-5.441704,-7.361582,0.400129,0.627811,-8.823696,-2.120261,1.067830,-6.642939,-1.421443,-5.831356,6.372196,4.119557,-5.988973,9.692006,-6.421555,7.431812,-1.469637,-6.584401,-1.442611,-3.919095,2.849278,9.797682,7.132700,5.963461,5.627217,-5.784790,2.655079,8.547380,6.290650,6.149606,6.379761,3.203685,-0.467460,2.605880,4.197032,-9.223748,9.308542,8.577695,4.052406,-4.834417,-7.816338,2.509803,-1.041415,1.368146,6.653535,7.092559,4.171440,-0.431393,1.523031,-7.681276,4.487265,0.499860,3.102944,-1.182410,0.389770,3.503447,5.010484,-0.832476,8.120958,3.862906,-9.416855,4.225340,7.916518,-7.199372,-4.243449,2.493610,3.355106,-4.439926,-5.719861,4.010457,1.164391,3.568218,5.078130,7.465925,-6.264914,3.233171,7.090610,-2.081718,-1.381968,7.774725,-1.648117,9.944658,-0.190864,-1.910192,-6.695719,-3.560098,-3.746740,-3.396663,9.108297,-3.214817,-7.166493,4.847506,9.221116,8.201233,-6.998903,-6.209661,6.273844,-7.853831,6.988064,-7.983741,-2.653386,3.881388,9.089148,-0.256193,0.386427,-5.812354,-2.843852,-5.219691,0.744979,1.778774,-8.466809,-8.457832,3.877853,4.271483,5.200634,-1.129118,7.791705,-4.038507,3.995861,6.792930,-1.331302,2.742125,1.430677,-7.865823,3.002079,-8.541056,5.329038,4.578122,5.900329,9.452566,6.310562,-4.338313,4.884895,8.263626,1.014057,-7.617831,-9.871680,-7.490303,3.696997,-6.498508,4.249179,-0.112033,-3.823914,8.280146,4.273808,-5.886795,6.192076,8.327031,-4.183317,8.900614,4.985269,9.184341,1.302130,-9.453999,-8.103939,0.358564,9.760974,-2.079118,-3.962382,-8.752023,-9.297631,-5.408211,8.278443,-3.982717,-6.620760,-6.787101,2.072751,3.638680,7.372667,2.744484,-1.930041,2.401660,8.984927,1.560638,-8.168928,5.091344,6.485441,-3.656570,9.903164,-1.281881,-0.383499,1.529539,-7.671252,6.923106,-1.568922,9.622922,8.860366,9.571475,-1.195318,-5.346516,-3.542667,8.247163,9.602537,-8.196080,-4.245346,-7.721995,8.446568,4.103668,-4.879041,-7.313390,4.364794,-4.876556,-0.735662,1.941972,-2.921136,5.301754,3.482528,-5.399469,-5.496697,3.402551,9.191624,-8.144704,-8.280306,-0.027847,-6.697446,4.997882,-3.719803,-5.722311,6.178239,0.151649,-7.674024,-6.898974,2.320564,-8.417088,-6.037636,1.992093,-0.523499,-6.386809,6.576320,8.615320,5.162640,1.114540,-1.857110,4.348249,-2.116959,-0.881884,4.786512,-6.590103,2.094127,2.258769,6.172329,-9.988222,-6.408586,-2.610823,0.464997,4.025494,-6.382815,6.915061,-5.662729,6.101288,9.551823,6.688315,-0.787481,-8.260553,6.166915,1.882896,-0.626818,-0.095736,8.265501,-4.068357,-5.469405,7.711288,-7.052344,-6.135441,9.452129,8.244510,6.393516,-0.036804,8.959218,6.090891,-3.116588,0.613570,-2.998462,5.651137,-5.471282,4.513636,0.906035,6.022477,5.338815,-8.708054,7.895772,5.498564,9.316991,3.736160,-7.304228,7.343844,5.000841,1.236011,-2.193287,4.189522,-1.109839,9.106815,-0.983724,-7.871859,-1.478885,-5.401894,-9.005589,-4.184128,4.023880,-6.322261,4.569844,-7.356262,-1.712699,-3.177164,-6.180294,1.104108,-2.827249,-7.910793,-9.527865,-2.247441,-7.516437,-3.364608,9.997978,-0.645545,-0.343031,-7.898675,-4.510378,1.039602,8.551405,9.917416,8.268149,-8.432228,4.069988,-0.735233,9.923227,4.549864,-4.087522,3.403388,-8.403422,-7.057316,-5.513510], dtype = "float32")#candidate|7209|(624,)|const|float32
call_7207 = relay.TupleGetItem(func_6905_call(relay.reshape(const_7208.astype('int32'), [2, 11, 12]), relay.reshape(const_7208.astype('int32'), [2, 11, 12]), relay.reshape(const_7209.astype('float32'), [624,]), ), 2)
call_7210 = relay.TupleGetItem(func_6910_call(relay.reshape(const_7208.astype('int32'), [2, 11, 12]), relay.reshape(const_7208.astype('int32'), [2, 11, 12]), relay.reshape(const_7209.astype('float32'), [624,]), ), 2)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_7211 = func_2905_call()
call_7212 = func_2905_call()
output = relay.Tuple([uop_7194,call_7207,const_7208,const_7209,call_7211,])
output2 = relay.Tuple([uop_7194,call_7210,const_7208,const_7209,call_7212,])
func_7213 = relay.Function([], output)
mod['func_7213'] = func_7213
mod = relay.transform.InferType()(mod)
output = func_7213()
func_7214 = relay.Function([], output)
mutated_mod['func_7214'] = func_7214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6450_call = mod.get_global_var('func_6450')
func_6452_call = mutated_mod.get_global_var('func_6452')
call_7290 = relay.TupleGetItem(func_6450_call(), 0)
call_7291 = relay.TupleGetItem(func_6452_call(), 0)
output = relay.Tuple([call_7290,])
output2 = relay.Tuple([call_7291,])
func_7298 = relay.Function([], output)
mod['func_7298'] = func_7298
mod = relay.transform.InferType()(mod)
mutated_mod['func_7298'] = func_7298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7298_call = mutated_mod.get_global_var('func_7298')
call_7299 = func_7298_call()
output = call_7299
func_7300 = relay.Function([], output)
mutated_mod['func_7300'] = func_7300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3902_call = mod.get_global_var('func_3902')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_7309 = relay.TupleGetItem(func_3902_call(), 0)
call_7310 = relay.TupleGetItem(func_3904_call(), 0)
func_5444_call = mod.get_global_var('func_5444')
func_5445_call = mutated_mod.get_global_var('func_5445')
call_7315 = func_5444_call()
call_7316 = func_5444_call()
func_2915_call = mod.get_global_var('func_2915')
func_2916_call = mutated_mod.get_global_var('func_2916')
call_7350 = func_2915_call()
call_7351 = func_2915_call()
func_5050_call = mod.get_global_var('func_5050')
func_5051_call = mutated_mod.get_global_var('func_5051')
call_7381 = relay.TupleGetItem(func_5050_call(), 0)
call_7382 = relay.TupleGetItem(func_5051_call(), 0)
output = relay.Tuple([call_7309,call_7315,call_7350,call_7381,])
output2 = relay.Tuple([call_7310,call_7316,call_7351,call_7382,])
func_7398 = relay.Function([], output)
mod['func_7398'] = func_7398
mod = relay.transform.InferType()(mod)
output = func_7398()
func_7399 = relay.Function([], output)
mutated_mod['func_7399'] = func_7399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7409 = relay.var("var_7409", dtype = "float64", shape = (16, 4, 3))#candidate|7409|(16, 4, 3)|var|float64
uop_7410 = relay.exp(var_7409.astype('float64')) # shape=(16, 4, 3)
output = relay.Tuple([uop_7410,])
output2 = relay.Tuple([uop_7410,])
func_7415 = relay.Function([var_7409,], output)
mod['func_7415'] = func_7415
mod = relay.transform.InferType()(mod)
var_7416 = relay.var("var_7416", dtype = "float64", shape = (16, 4, 3))#candidate|7416|(16, 4, 3)|var|float64
output = func_7415(var_7416)
func_7417 = relay.Function([var_7416], output)
mutated_mod['func_7417'] = func_7417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6413_call = mutated_mod.get_global_var('func_6413')
call_7449 = relay.TupleGetItem(func_6412_call(), 0)
call_7450 = relay.TupleGetItem(func_6413_call(), 0)
func_7398_call = mod.get_global_var('func_7398')
func_7399_call = mutated_mod.get_global_var('func_7399')
call_7457 = relay.TupleGetItem(func_7398_call(), 2)
call_7458 = relay.TupleGetItem(func_7399_call(), 2)
output = relay.Tuple([call_7449,call_7457,])
output2 = relay.Tuple([call_7450,call_7458,])
func_7468 = relay.Function([], output)
mod['func_7468'] = func_7468
mod = relay.transform.InferType()(mod)
output = func_7468()
func_7469 = relay.Function([], output)
mutated_mod['func_7469'] = func_7469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7298_call = mod.get_global_var('func_7298')
func_7300_call = mutated_mod.get_global_var('func_7300')
call_7488 = relay.TupleGetItem(func_7298_call(), 0)
call_7489 = relay.TupleGetItem(func_7300_call(), 0)
func_6795_call = mod.get_global_var('func_6795')
func_6797_call = mutated_mod.get_global_var('func_6797')
var_7516 = relay.var("var_7516", dtype = "uint64", shape = (700,))#candidate|7516|(700,)|var|uint64
call_7515 = func_6795_call(relay.reshape(var_7516.astype('uint64'), [14, 5, 10]))
call_7517 = func_6795_call(relay.reshape(var_7516.astype('uint64'), [14, 5, 10]))
output = relay.Tuple([call_7488,call_7515,var_7516,])
output2 = relay.Tuple([call_7489,call_7517,var_7516,])
func_7525 = relay.Function([var_7516,], output)
mod['func_7525'] = func_7525
mod = relay.transform.InferType()(mod)
var_7526 = relay.var("var_7526", dtype = "uint64", shape = (700,))#candidate|7526|(700,)|var|uint64
output = func_7525(var_7526)
func_7527 = relay.Function([var_7526], output)
mutated_mod['func_7527'] = func_7527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_7584 = relay.TupleGetItem(func_2994_call(), 0)
call_7585 = relay.TupleGetItem(func_2996_call(), 0)
func_2176_call = mod.get_global_var('func_2176')
func_2178_call = mutated_mod.get_global_var('func_2178')
var_7587 = relay.var("var_7587", dtype = "int16", shape = (672,))#candidate|7587|(672,)|var|int16
call_7586 = relay.TupleGetItem(func_2176_call(relay.reshape(var_7587.astype('int16'), [14, 12, 4])), 0)
call_7588 = relay.TupleGetItem(func_2178_call(relay.reshape(var_7587.astype('int16'), [14, 12, 4])), 0)
func_3833_call = mod.get_global_var('func_3833')
func_3834_call = mutated_mod.get_global_var('func_3834')
call_7589 = relay.TupleGetItem(func_3833_call(), 0)
call_7590 = relay.TupleGetItem(func_3834_call(), 0)
output = relay.Tuple([call_7584,call_7586,var_7587,call_7589,])
output2 = relay.Tuple([call_7585,call_7588,var_7587,call_7590,])
func_7592 = relay.Function([var_7587,], output)
mod['func_7592'] = func_7592
mod = relay.transform.InferType()(mod)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7593 = relay.var("var_7593", dtype = "int16", shape = (672,))#candidate|7593|(672,)|var|int16
func_7592_call = mutated_mod.get_global_var('func_7592')
call_7594 = func_7592_call(var_7593)
output = call_7594
func_7595 = relay.Function([var_7593], output)
mutated_mod['func_7595'] = func_7595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_7684 = relay.TupleGetItem(func_2535_call(), 0)
call_7685 = relay.TupleGetItem(func_2537_call(), 0)
func_4986_call = mod.get_global_var('func_4986')
func_4988_call = mutated_mod.get_global_var('func_4988')
const_7698 = relay.const([[-0.147948,-6.299072],[3.189700,-1.515382],[-4.597488,9.460598],[-9.845540,-9.475178],[-1.983259,-8.110219],[-9.888490,8.768745],[8.677560,6.102501],[5.064068,8.013621],[-6.002467,3.235799],[-8.701750,-4.001283],[-9.617926,6.056553],[-6.349521,3.802141],[-9.318306,1.886367],[-9.001572,-8.798949],[-9.019089,-0.611529],[-2.431062,6.909544],[4.209329,-1.408243],[8.843784,-6.117424],[-1.123317,-6.338751],[6.077163,7.806739],[3.200867,2.463012],[7.299286,8.901065],[1.666989,4.298724],[2.592933,-4.325501],[9.457827,-7.631502],[-1.429040,-5.493636],[-1.168318,7.894616],[8.894372,4.941508],[-3.059445,-5.311000],[4.933125,4.250610],[5.649202,-0.263754],[7.829240,-0.172148],[-1.931424,7.461006],[1.717644,2.864950],[-6.030781,-9.871936],[-5.528969,-5.208148],[-1.761186,-1.007399],[-5.791059,-5.194611],[5.682677,4.824768],[7.495588,9.910934],[-7.665627,-2.513405],[3.050769,-1.543941],[9.570067,2.531642],[-4.261394,-4.854721],[-4.861109,-7.041969],[-3.184083,9.743445],[-2.304212,-8.709850],[-8.679283,9.057553],[4.441205,-8.686726],[6.428412,-3.321634],[8.873718,-0.839304],[-0.754859,-1.119923],[-9.492806,7.590707],[0.242212,-5.350502],[3.877942,-8.047949],[-0.880541,5.515538],[0.773817,-7.017279],[-0.161749,4.355373],[-0.748022,3.297754],[-6.154183,-4.874763],[6.701450,9.821037],[-3.927270,-9.789408],[7.762686,3.313872],[-2.118650,0.678998],[-2.711654,-6.907955],[-0.100602,5.904089],[-8.513950,2.514829],[-3.673925,1.485246],[-1.292668,1.386661],[-2.653148,-2.198242],[-8.127790,8.031082],[-1.719786,-9.212178],[7.820402,8.204968],[0.072575,-8.070977],[-3.962958,-4.828411],[3.082928,-2.088724],[3.724744,-8.012071],[0.293895,9.313142],[-2.796838,-1.024705],[5.063360,-2.932166],[8.415064,-9.876037],[-2.506996,-8.088491],[4.185554,9.446844],[-4.502110,-7.801890],[6.324788,2.733566],[6.766434,-0.652169],[-4.429774,5.985740],[-7.970925,-3.944569],[6.843301,-0.154822],[1.756881,-1.410361],[5.844437,-9.938142],[9.375113,1.383053],[1.251816,9.503654],[1.702488,9.749773],[-7.178620,2.550871],[-2.165701,4.550770],[7.249788,6.826209],[-1.134974,4.533650],[6.059208,-0.943400],[-4.744241,-0.182894],[-1.682988,-9.968852],[9.447834,5.042398],[-7.683031,-3.836794],[-6.249025,5.203989],[1.741530,6.685522],[-7.459131,-6.784604],[-0.405268,5.653616],[-6.286153,-9.391532],[8.419381,8.778180],[-1.441530,9.031350],[1.093818,9.392072],[2.940005,2.341906],[7.002331,-2.573930],[8.729911,-0.969681],[1.716771,-2.075455],[7.448173,4.743354],[-2.633691,7.024388],[8.489863,8.087321],[2.963855,2.482856],[3.896066,0.750442],[1.576314,8.314590],[-6.964953,-3.470322],[1.866420,-0.312588],[6.568772,0.151546],[-9.411182,6.889230],[5.952901,-4.411817],[4.756964,9.373411],[5.448282,-1.027812],[2.934920,4.134764],[8.598575,0.104307],[0.672287,4.342564],[6.479993,-8.054706],[9.206989,-5.909495],[-6.408549,5.958106],[-5.524293,7.267545],[-3.287985,-1.831434],[1.506416,0.989894],[0.356922,3.464425],[-1.825990,2.937859],[5.000100,2.580237],[4.116993,-3.309203],[5.832478,-6.732077],[-2.011821,3.690077],[9.848694,-7.823853],[9.708902,4.805329],[9.665379,6.666233],[8.222356,5.031228],[-9.202463,4.515843],[-0.762854,-8.281164],[-9.710655,7.491753],[-4.443207,2.507686],[-2.342784,-1.632653],[6.950283,-0.434159],[-8.138550,3.246672],[5.410023,-4.263085],[8.789601,3.757486],[9.142231,7.698297],[-7.884652,3.429492],[7.509675,-6.860075],[-7.997718,-5.622271],[-0.068334,-9.236495],[-8.497869,-5.413031],[0.841866,-0.992519],[2.549023,-8.862025],[9.018894,-8.379155],[6.240234,-7.252737],[-3.061256,-7.954886],[0.505731,-9.710436],[-4.269499,-0.196000],[-6.750952,-5.240745],[8.800265,2.871445],[-3.274616,-2.265434],[4.396292,-4.497897],[-3.278198,-0.763754],[2.208224,7.352217],[6.395364,9.494593],[9.073055,-5.221654],[-4.054521,5.598314],[1.624985,-1.584088],[-7.011047,3.778316],[2.442880,-6.280351],[-8.234322,-3.499567],[-8.132315,-8.880070],[-4.228461,8.767959],[0.031250,2.742909],[-3.861622,-9.821347],[6.366625,0.506513],[2.077305,-6.237549],[-5.336985,-1.021175],[4.740383,7.393865],[-3.738998,2.865509],[9.396258,-6.577647],[-0.285222,-3.645212],[-6.405490,8.703625],[-5.087613,-6.956170],[1.203212,-4.934792],[7.089921,0.478444],[-8.922180,-5.147733],[-7.140626,3.426063],[-7.865456,8.500841],[6.431546,7.932059],[-7.803198,-0.144843],[-7.059023,-7.692200],[6.459961,0.606062],[7.458961,0.789015],[8.415246,-6.098076],[9.363887,3.392551],[-5.486666,-6.644887],[8.751822,1.698088],[-4.471785,-1.766600],[-4.419617,7.986106],[1.855785,4.047103],[3.954291,-0.764656],[-7.872337,-9.341118],[-8.990134,-6.671112],[-8.950529,9.822881],[-8.038387,3.785536],[-3.666450,1.489036],[-5.342007,-7.770254],[-0.750439,-2.827845],[-8.185547,-1.292664],[-8.920551,-9.522556],[3.323922,9.099604],[1.037403,1.046275],[9.743446,7.379999],[-4.893248,2.008144],[2.695598,-2.603779],[4.079987,0.139080],[-4.901308,-0.739745],[-4.957665,6.864864],[2.636870,-3.074587],[3.497568,5.207910],[-6.236900,-7.890788],[9.851558,-7.446822],[7.724355,-0.761353],[3.154583,-1.505296],[-0.545458,-2.636458],[5.572950,-4.811614],[-2.885755,-0.464346],[-5.944299,5.895140],[-3.002320,8.572118],[7.999584,-2.569628],[-9.459451,5.186889],[-1.138268,9.418048],[-5.112144,9.048079],[-1.372188,8.731675],[-5.696888,-2.016503],[4.290982,-3.990217],[-5.660253,9.081072],[4.727367,-9.291366],[0.150327,8.716639],[-2.391564,-2.581313],[6.895661,-1.877323],[1.713818,-8.099181],[4.192003,-5.340838],[-1.676608,-0.918580],[-8.732300,-0.982619],[6.719356,1.013673],[-4.666352,-5.772037],[-0.834294,-9.943472],[4.680317,0.594059],[-6.688776,-5.126005],[-7.454208,-4.899842],[0.187097,9.206374],[-9.085094,8.713158],[3.475852,-9.674985],[-0.677233,-8.322861],[7.885768,-6.079930],[2.731986,8.821768],[9.583734,-2.213541],[-7.110277,4.720514],[8.806593,2.456110],[-8.170786,-0.856715],[-8.385291,-9.461331],[2.754216,2.958348],[2.502619,5.391593],[0.647138,-4.238495],[1.291810,-8.304890],[4.860506,7.785442],[5.325407,-3.547258],[-3.561808,0.068219],[-0.984441,8.834280],[-1.381160,-8.025340],[-4.864748,-6.976519],[6.429179,-0.762046],[6.854808,-7.214937],[-4.452819,-2.322908],[4.563782,-8.174601],[8.171367,-5.171455],[9.324462,6.696768],[-4.970584,7.234222],[-2.509246,-3.608180],[-1.084734,-6.902645],[2.440468,-2.896091],[-4.497006,6.857211],[5.007982,5.181978],[1.639495,-7.892610],[4.630725,-3.623429],[-8.478014,-1.462942],[-0.962893,-4.805565],[-5.236744,-7.204154],[0.582343,5.004719],[8.076841,5.348237],[-4.825600,0.465559],[-7.767456,-1.480400],[-8.709903,1.451725],[-9.636931,5.486005],[-5.602383,2.789542],[-5.773330,9.865429],[-9.142649,6.300952],[1.789590,1.020691],[-4.656992,-6.687117],[-1.620933,-7.421901],[1.530121,4.547963],[-9.350237,-2.429971],[-0.903134,2.570733],[-2.388931,5.094271],[7.749355,-8.391996],[7.759920,7.080955],[4.885303,9.767362],[-9.950300,-8.007347],[3.009769,-9.954063],[-6.537130,3.567989],[-6.560500,9.936938],[3.935790,-0.838939],[5.706516,1.204591],[-2.217095,-0.365000],[-0.248228,0.062848],[-8.897262,3.048842],[-5.844200,2.292744],[-7.692006,7.318791],[0.823278,3.068054],[5.814776,2.107876],[1.573957,-2.731922],[9.320273,8.865256],[-4.381832,7.534690],[-2.031649,-9.562604],[-7.049573,0.297185],[-9.593976,3.247816],[5.222341,-2.725688],[-4.983327,8.142683],[6.549414,5.718511],[7.903460,-4.137628],[-4.336774,-8.351591],[-3.599677,8.805955],[-6.884496,-5.479055],[9.214939,-6.683262],[-4.732071,-8.543691],[-2.992394,-2.221982],[0.688166,8.566174],[-5.236317,-9.409212],[5.468351,4.894855],[6.524639,-4.843261],[1.584700,8.048362],[-5.230562,9.143483],[-4.049357,-5.762508],[-6.846059,-5.408731],[-1.126932,-9.237592],[-0.292938,4.068749],[3.350461,1.578819],[8.777555,-0.285377],[-8.073663,-0.194242],[0.002695,-7.214726],[0.564922,-9.524492],[2.228934,7.735898],[-5.129022,1.889490],[-0.062681,-9.644812],[9.039869,-0.094131],[0.130333,-7.373851],[-6.335884,3.502054],[-7.344238,-0.350208],[-4.499031,2.862966],[7.265676,6.749107],[-0.657561,-1.972676],[-0.483730,-2.177039],[9.668412,-4.122690],[3.832169,-5.395880],[1.444455,7.933494],[1.792200,9.972773],[3.836227,-9.669330],[1.496654,-1.725053],[-8.585904,-8.791738],[-8.852979,-3.578254],[-4.227384,-3.062824],[7.714783,5.705713],[-8.254317,1.764364],[-0.483508,4.367270],[0.139123,7.632108],[-2.422845,2.661371],[-3.699349,8.903940],[-4.978569,-1.570510],[-5.576270,7.298944],[-3.789777,9.540168],[1.827319,-9.637747],[0.653479,4.338195],[4.680797,-5.978153],[9.344836,-3.088779],[2.625477,-9.171859],[-0.532956,-4.501705],[7.983897,-6.230371],[6.415660,9.791973],[-7.759861,-7.552587],[7.886269,3.114937],[-8.025727,-3.763054],[8.715414,-3.166034],[-9.559596,-3.584718],[4.751889,-7.796050],[-8.841841,-9.381055],[-2.812839,8.291765],[-4.817180,-4.392336],[2.762340,-1.680589],[5.473245,7.351477],[-6.484023,-6.390327],[-2.061013,7.137610],[0.061604,1.398102],[-6.487066,5.478373],[3.315012,-3.646175],[5.704273,8.091617],[-6.765620,-3.533970],[5.575613,-1.329064],[5.379086,-8.536946],[1.855235,-9.945913],[5.664698,4.231073],[0.715105,-6.487857],[3.800313,-1.411760],[-0.774848,4.909966],[-0.121791,-6.064105],[-3.735629,4.774304],[3.794674,2.098174],[6.062479,-2.046155],[5.332042,-0.022901],[-9.930773,2.987334],[0.335844,-5.394008],[-3.819000,-9.566801],[-8.483276,-4.849172],[8.551080,-7.221182],[5.066462,-8.379027],[6.266155,-1.256144],[-1.245989,-2.112092],[6.845120,-8.647599],[3.789635,-3.233427],[-0.524377,-9.023144],[-5.634010,5.430192],[-0.297706,-5.948687],[-8.629633,-2.891654],[7.990425,-1.565206],[-1.386738,9.085388],[1.068611,-0.496709],[-1.739457,-9.495277],[-3.936887,1.798604],[4.760553,-1.162730],[5.117745,4.727423],[1.786578,1.014501],[-9.918882,-5.439798],[-5.058153,2.101707],[7.041485,3.315085],[-4.297962,3.350718],[-5.479110,0.712894],[5.547512,-6.152602],[2.016516,-6.883974],[1.199589,3.767924],[-4.153519,-5.078457],[2.736856,-6.418021],[-2.896986,9.496888],[1.972769,7.930055],[7.759158,0.877888],[-8.302110,6.860997],[4.371089,1.905813],[-7.806628,9.246652],[-1.409366,4.653606],[7.412780,3.221933],[6.646160,-4.834627],[5.776054,4.404862],[4.137369,6.948227],[-3.424942,2.170786],[5.936520,-8.388028],[7.802407,-2.331955],[-7.726066,-0.779859],[6.805969,5.402718],[-6.587609,7.616501],[9.723531,-2.470895],[8.622913,-2.120746],[6.620054,8.554737],[-8.260507,-0.137830],[0.208867,-2.718203],[-3.257125,7.219328],[-0.170769,0.874522],[6.313446,-7.956948],[0.235471,8.161647],[-3.982177,-7.012373],[5.506939,-5.092805],[8.823798,0.563236],[6.622074,-7.721638],[-1.832863,9.686920],[-6.165075,2.697812],[7.502726,-4.422073],[3.884475,3.408113],[-4.082924,2.327523],[-6.413001,3.652105],[-0.331594,-4.592003],[-7.984379,8.060334],[0.517229,0.875072],[2.143188,0.749489],[-7.281969,5.578779],[0.146656,-6.805065],[-6.558170,9.195025],[9.201245,3.629834],[3.606840,-1.915563],[-0.063915,8.608022],[-1.251107,-7.453848],[5.236186,6.596998],[6.429188,3.195173],[6.687208,-9.137519],[8.455288,-9.027988],[0.378545,-8.248053],[-1.760446,-2.903410],[9.446792,-1.448505],[8.025019,6.411953],[-3.271422,-7.720436],[-3.845680,-9.573729],[2.841028,4.155236],[-2.985904,-7.218767],[6.167503,-9.907608],[8.944605,7.551382],[-3.339697,-1.903707],[-4.594137,5.214067],[-1.874372,-4.560070],[4.774651,3.040638],[-4.840572,-2.793723],[-8.227986,-4.061993],[6.381606,4.274907],[1.072857,0.686043],[-1.411923,9.171788],[-9.763853,5.551598],[8.029378,5.388533],[-8.868252,6.581384],[3.256045,0.759109],[-4.790723,-5.978537],[7.736609,-2.387107],[-5.141487,-8.207062],[-9.187133,7.999026],[-6.419404,1.482440],[-5.098162,9.161820],[2.936633,5.119588],[-3.367327,4.616716],[-9.402131,-8.842509],[5.810187,7.397653],[2.223464,4.685340],[8.086338,-3.638451],[2.976446,0.726298],[-1.902842,6.770030],[-4.257465,-0.717645],[3.489316,5.914201],[3.088429,7.683932],[5.193416,-6.997433],[5.633689,-7.015023],[-1.677578,-6.945066],[-6.763072,-7.215172],[-7.782234,8.743978],[-7.246270,1.868038],[0.600372,-5.584639],[1.685088,2.470395],[-2.301153,9.496506],[6.820479,-9.336991],[-2.607202,-9.747661],[7.184411,2.044785],[-3.724150,-6.339562],[-7.182891,-3.764167],[-1.121754,6.425188],[6.485517,-0.833914],[-0.277011,0.118415],[1.138457,-4.520291],[-2.975397,0.889047],[3.369017,-2.686115],[2.023228,-3.446100],[-1.700718,2.024102],[6.110534,-9.470023],[4.135581,-7.394211],[-9.073441,-5.993008],[-9.822675,6.225599],[3.548909,-8.678198],[3.350118,-8.408903],[9.460572,0.069898],[8.766359,-1.142466],[6.398043,3.226400],[-3.418375,-8.420327],[6.637305,-2.509584],[1.374030,7.207996],[-3.663051,3.274223],[-2.783166,-4.893483],[7.292842,3.919208],[-9.061184,7.478315],[9.375562,1.629150],[3.124197,-5.186558],[-5.562322,-3.684356],[5.976391,-7.142841],[5.237480,4.195405],[3.433939,1.319007],[7.889642,7.605973],[-9.210219,0.019929],[-6.286193,5.636779],[3.972899,-8.137652],[4.613765,2.727746],[-2.446262,-9.331622],[-1.972882,3.576443],[-2.821389,-4.272105],[-3.852163,3.388517],[-2.908181,-0.400472],[6.516091,-4.312872],[0.506922,-7.267277],[9.157918,8.864760],[8.157893,0.282626],[-8.397059,9.736968],[4.624299,-5.825979],[-8.996009,3.499377],[4.509620,3.195839],[6.709352,8.954847],[-1.237919,1.153971],[5.992834,-0.763546],[8.224061,-2.188593],[-0.225973,-7.703866],[8.432628,4.093531],[-6.548995,3.757804],[-1.224536,6.137611],[-6.273156,5.834309],[-7.673362,6.019027],[2.234427,1.768149],[9.982984,-0.247812],[2.373699,-8.763892],[-3.270380,-5.983831],[-2.463715,-7.592095],[-3.099487,-0.656598],[-5.761513,-2.365817],[9.228881,-7.135297],[7.949986,8.264155],[-2.325142,-1.712182],[-9.134730,-3.030410],[2.965729,7.302590],[-9.095231,-1.227229],[9.366905,-9.279763],[-2.384970,6.821783],[-5.908919,4.499168],[4.266652,-7.714013],[-6.617083,4.731558],[2.519948,6.640419],[9.246700,-0.437471],[-9.745798,-5.733666],[-0.516522,6.409627],[9.541816,-8.103503],[8.711102,8.099987],[-1.669424,-4.878977],[3.949883,4.395975],[5.771751,4.864169],[9.436843,7.506708],[-1.244246,-3.934609],[-6.766442,-6.716734],[-0.361136,9.475644],[-1.539476,-4.864636],[-6.136138,7.068903],[-8.520516,1.578021],[-1.557718,-8.959175],[-2.774907,3.429461],[-0.898889,7.664577],[-6.287318,-1.287264],[-0.758282,-7.355997],[0.556299,0.757038],[9.697528,2.113199],[6.061566,5.650887],[2.308879,-5.276989],[3.798239,-2.606868],[3.438070,-5.374299],[5.370341,-9.187190],[-6.280206,-7.732894],[0.910573,-8.811670],[4.198481,-0.763395],[-2.161439,-2.297218],[-2.964154,7.178546],[-7.448022,6.620743],[-1.885327,7.305560],[-8.435206,6.760222],[-7.548819,-8.307675],[-4.725799,-2.808381],[-4.606934,-2.681964],[5.258985,-7.397001],[9.686026,0.009921],[-4.693593,8.909013],[9.080343,-9.915886],[-1.574174,-7.628087],[-1.244439,-6.777829],[8.502636,-4.754256],[-4.842998,-5.633681],[9.853431,3.884181],[1.392433,-3.275175],[8.066863,-3.992250],[4.166928,-5.081081],[-6.859056,-2.344734],[-6.755156,0.957643],[-6.304853,3.196301],[8.323498,-4.850038],[7.535862,6.058702],[-5.271815,-1.779554],[-7.766357,-3.434075],[7.161301,9.978590],[-9.815395,-8.858863],[9.051083,-3.187187],[1.491315,-0.199019],[-4.792064,8.848954],[-5.329855,-8.087726],[5.516730,-0.377418],[6.920474,4.472122],[2.174068,-0.445007],[-0.414786,-8.675095],[8.861358,3.719783],[9.648108,7.277642],[-1.907453,3.476790],[0.928931,-7.522010],[-6.672932,-2.115481],[8.403963,-1.484896],[9.332211,-1.794988],[-0.827528,0.867624],[-7.995471,-9.703174],[-6.296467,9.100759],[9.341626,3.315037],[-3.857958,5.578082],[-5.722559,-5.962181],[2.016124,-2.221032],[0.334727,-7.773123],[-2.277901,7.799850],[7.650334,-2.227983],[7.349731,-8.371006],[-5.745250,-6.678613],[5.136423,2.599866],[3.372117,-2.426649],[-6.954987,1.162164],[2.096798,6.820158],[3.675179,-0.786794],[9.164188,-9.479367],[-4.991702,6.023757],[-8.204182,1.017038],[6.653187,3.483760],[-2.074660,8.846508],[8.550669,8.522882],[-8.056903,-1.677037],[9.118812,-7.482610],[9.402754,-0.649521],[-5.474709,-0.150060],[4.854198,-1.203528],[-3.173078,2.388331],[6.438080,7.758411],[-8.202210,-0.005765],[-6.443138,-1.003531],[1.380884,-2.290892],[-6.152534,5.330619],[-0.100688,6.729948],[7.603820,-9.039161],[-7.164621,5.700871],[-1.471819,-8.429027],[9.433861,7.986976],[0.203570,6.850504],[2.720222,2.151281],[-3.744885,-2.068450],[-1.293352,-9.660951],[0.500960,4.591748],[7.180780,-5.469240],[3.210708,-0.067717],[2.580186,-5.079703],[1.654818,0.976765],[6.636741,-1.191533],[6.297548,-4.533283],[2.657532,-5.538045],[4.326234,-8.836847],[-1.159663,-9.164475],[6.603143,-6.727453],[3.007407,2.284565],[-6.248881,1.517981],[7.940428,-6.042689],[-2.978395,-5.306908],[9.427393,-4.402203],[-7.575912,6.167114],[1.442546,-7.542512],[-9.206830,8.309892],[-1.826389,1.443358],[-0.517172,-0.936071],[-3.404579,-5.295587],[-2.913907,-0.429916],[6.848433,-9.945981],[7.126119,-1.680082],[-8.230995,1.152556],[3.575719,-8.612345],[8.340160,7.388783],[-7.178134,8.591541],[-3.294213,7.325673],[-0.021612,-4.669909],[-8.722045,8.377907],[4.381312,4.139356],[3.067076,-7.777103],[1.387744,-7.414738],[-3.162285,-3.922715],[8.731742,-4.448960],[-3.729045,-8.431188],[1.677121,-4.841045],[-7.803941,-3.523441],[-7.741846,3.696976],[-2.380103,-8.713764],[-5.981387,2.887900],[-4.297682,4.179433],[2.788873,8.718932],[8.944559,3.306233],[8.925273,-4.270893],[6.509996,5.254860],[-6.986908,2.996420],[-8.099043,9.038484],[-2.576026,-8.861065],[-7.777580,6.130512],[5.057883,6.731276],[-6.849833,1.205027],[8.091847,8.903845],[-4.518811,-9.066739],[6.923781,-6.547308],[1.474450,-2.683936],[-2.926177,9.753854],[-4.822132,-5.053605],[8.369629,-4.528871],[-1.987909,3.379107],[-7.423013,5.393485],[6.943423,0.340115],[4.907235,7.823723],[8.140472,6.873242],[-2.044602,2.639419],[8.422350,-9.734580],[7.245543,-4.193004],[-4.012158,9.726550],[6.420523,-3.251208],[-0.281879,8.979386],[1.621477,0.863875],[4.499891,-9.867342],[4.886228,-3.512624],[0.465615,1.304805],[-9.813423,1.568621],[-4.086784,6.299022],[2.270991,-0.279980],[3.858191,9.517354],[-3.145089,-1.047913],[5.036005,6.781500],[-3.680107,2.028332],[-3.051594,-3.703148],[4.760157,-1.471986],[8.154188,7.543865],[4.735326,-1.237961],[2.317019,9.803946],[-8.656877,4.472639],[-6.317643,-2.013422],[0.604702,-5.349260],[2.863879,-5.891187],[-5.236061,-2.994627],[-0.503558,-4.793244],[8.245569,-7.321481],[2.175707,5.228338],[8.473021,7.079135],[7.255198,-0.926283],[-3.508939,0.617302],[-0.471372,-7.606300],[-3.978968,-6.901967],[-1.231864,-1.886310],[8.278433,-5.718782],[-0.092618,3.536031],[3.110945,1.677883],[-5.495351,6.278277],[-6.447591,-3.441849],[-3.013316,-0.156172],[1.178726,7.297095],[6.079596,-5.295283],[-5.078277,9.156047],[-6.304501,9.336714],[-9.681705,-1.889945],[-8.480011,7.748768],[-5.184130,5.322478],[-8.163159,3.603479],[-1.533891,7.603788],[-3.992105,7.425483],[-8.332881,3.548356],[5.816749,-4.322104],[8.835621,-4.501351],[-7.567096,9.495249],[-2.719476,1.355951],[-7.693914,-1.584266],[3.781908,-1.376948],[3.596065,3.196404],[6.807260,-2.240515],[3.176567,-0.613563],[-6.411409,-7.223401],[-8.909459,9.884032],[8.638097,5.098364],[-1.297812,-5.709562],[9.768760,8.608193],[-0.134399,-8.266076],[-7.569760,-5.954102],[-7.653178,-5.192980],[-4.302465,5.043163],[-8.467494,3.082273],[-3.156006,7.868570],[-2.023367,-7.328943],[5.308360,3.185956],[-1.583502,9.685897],[-1.534566,-5.995312],[-8.659277,0.292111],[-1.302043,5.872447],[-1.854639,-2.317520],[0.338045,1.536246],[3.294511,2.908149],[1.902408,1.403951],[-0.278398,-5.170080],[-7.730771,6.097332],[-8.901030,6.821868],[-6.476750,4.720850],[3.828270,3.544239],[-2.893079,5.301301],[-0.455083,-9.649937],[5.423070,-2.851728],[-9.785816,-9.060700],[3.746737,7.538943],[6.764958,-6.884940],[5.521800,-5.196125],[2.746051,5.763974],[-9.991332,-1.321051],[1.367850,-4.471086],[-2.138542,-3.535672],[-4.854755,9.797949],[4.478137,1.310619],[-7.953146,-3.443106],[7.339210,-0.324267],[-4.229384,-5.053438],[-9.719281,0.337529],[9.285434,-1.348835],[-2.740155,-6.791287],[-0.096310,4.806740],[-9.690722,-1.952055],[-0.710984,-1.228922],[0.515207,7.216723],[-1.437799,-8.467332],[-1.450769,-1.557944],[9.463716,9.563564],[-0.437603,-1.597168],[0.435732,-8.698734],[-0.064078,-1.255796],[7.592059,9.741596],[-3.379245,-4.665761],[-0.516521,4.235439],[-0.425782,6.476652],[1.267675,-0.789625],[-2.180818,-5.873101],[-8.745089,-0.707705],[4.365390,9.948639],[3.234899,1.431987],[3.591552,9.075272],[-7.018968,-7.708979],[-6.691252,-2.432424],[-7.432907,6.811786],[-5.577842,4.447215],[-2.716771,4.597375],[-0.513188,-6.433756],[2.744566,8.509960],[8.752773,2.217076],[-5.181969,8.531229],[2.676749,-9.089995],[-0.077186,-6.616454],[4.335784,6.209531],[3.077885,6.911870],[1.915492,-7.752615],[9.198411,-1.859297],[-0.682866,-5.376348],[3.169413,2.521418],[9.950777,6.207518],[-6.068647,-0.489797],[7.582208,1.366059],[8.671570,-0.313093],[9.305902,0.301015],[2.378850,5.930566],[5.582830,-3.984170],[2.912393,7.605453],[4.464817,-0.004774],[5.466739,4.490882],[-6.452292,4.410953],[0.292986,9.925605],[-6.623126,0.320092],[-0.040939,5.176239],[-9.369507,-4.647039],[-6.736999,-5.209092],[-2.353597,5.707681],[-2.835469,-6.265809],[1.271069,-0.073969],[-5.614929,8.607992],[-6.155026,-4.172639],[-0.654459,4.985904],[3.501108,-2.627057],[3.249515,2.075094],[-4.502791,6.106042],[1.727921,3.147801],[-5.937896,9.689123],[5.796225,8.229938],[1.771158,-8.174624],[-5.221169,-3.658648],[-6.748749,1.943209],[3.316574,4.865580],[8.101873,-1.277854],[0.264726,1.269607],[0.163119,-6.138872],[-1.121289,9.375847],[0.014097,0.378915],[6.284402,3.063517],[-0.348835,3.218552],[9.176104,5.356252],[-5.386271,6.444062],[-9.129355,5.901142],[9.722226,-2.422848],[6.457163,0.368362],[-2.402994,-0.651809],[-6.804824,9.464082],[-8.375298,-8.485628],[9.310849,-2.259093],[-6.121558,1.605813],[5.919792,-4.949563],[-3.032502,-1.408976],[-1.685523,-2.790170],[-6.444590,-7.620905],[-9.905089,0.730974],[9.802732,-7.507520],[-0.327885,-3.623859],[-8.182407,0.336753],[-4.172489,-6.829724],[-0.400562,-5.000374],[-2.812230,7.052266],[-0.885116,6.906520],[4.145190,2.927478],[5.166349,-4.669174],[8.780846,-0.076947],[-8.929860,1.643070],[6.720766,-9.744118],[-9.459871,1.469317],[5.980119,7.301415],[-0.480825,3.475135],[4.562487,-2.691707],[-7.683511,-1.556240],[3.064718,-6.286638],[-7.948802,-6.233175],[3.398007,-0.129886],[-5.137606,7.972406],[-8.633259,4.636052],[8.900325,1.613755],[1.328504,7.270474],[-0.757989,4.936367],[-0.392355,2.823197],[5.124363,2.678215],[-0.644260,-1.990103],[0.808308,2.452203],[-8.666915,-4.088860],[4.100639,1.861629],[-6.637322,-3.745543],[-0.542767,-7.881065],[5.868822,-4.025167],[-2.014742,-6.511928],[4.841002,3.388023],[-2.701540,-1.618198],[3.680277,-9.902191],[-1.187221,3.704075],[7.831600,9.524359],[-2.332465,-5.588116],[-7.412419,-2.070503],[-2.447323,2.918945],[-6.177836,-4.007858],[6.064147,2.161698],[-1.941214,6.089079],[7.667487,5.036269],[0.405250,3.226751],[-0.332527,6.999031],[-4.376948,3.411607],[-7.104573,-7.371746],[0.728992,2.879052],[5.056390,0.947737],[7.302309,8.883145],[-7.022011,2.260011],[3.653178,6.436360],[-4.752748,-5.995415],[-9.459991,-0.251560],[9.493096,4.587752],[6.972647,4.702239],[-2.338640,-4.829045],[-9.024137,-3.988988],[-3.290105,-2.199761],[-4.711750,-8.397487],[-5.422510,2.397139],[-8.016438,-3.920980],[-9.066328,9.548259],[-9.692641,5.811272],[7.384066,-4.417610],[6.375176,-2.045830],[-8.287781,9.134123],[-0.420232,-3.053745],[6.058392,-6.482428],[7.626019,6.700640],[-5.548637,8.800622],[5.000453,8.036786],[1.289857,-9.843172],[9.725973,-5.334760],[1.204310,-7.794279],[2.512595,5.230096],[5.206444,1.101137],[-8.739894,-0.838487],[5.076275,2.715277],[-2.567517,0.120813],[4.896827,-6.155404],[5.277648,-0.498228],[4.206814,-2.933053],[5.676502,6.729896],[4.069238,8.180135],[4.443457,7.769742],[-3.857654,6.213965],[5.249063,-5.483400],[2.519912,7.468728],[8.608501,9.558612]], dtype = "float32")#candidate|7698|(1120, 2)|const|float32
call_7697 = relay.TupleGetItem(func_4986_call(relay.reshape(const_7698.astype('float32'), [10, 14, 16])), 1)
call_7699 = relay.TupleGetItem(func_4988_call(relay.reshape(const_7698.astype('float32'), [10, 14, 16])), 1)
func_3656_call = mod.get_global_var('func_3656')
func_3657_call = mutated_mod.get_global_var('func_3657')
call_7704 = func_3656_call()
call_7705 = func_3656_call()
func_7298_call = mod.get_global_var('func_7298')
func_7300_call = mutated_mod.get_global_var('func_7300')
call_7707 = relay.TupleGetItem(func_7298_call(), 0)
call_7708 = relay.TupleGetItem(func_7300_call(), 0)
func_2060_call = mod.get_global_var('func_2060')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_7709 = relay.TupleGetItem(func_2060_call(), 0)
call_7710 = relay.TupleGetItem(func_2061_call(), 0)
func_5788_call = mod.get_global_var('func_5788')
func_5794_call = mutated_mod.get_global_var('func_5794')
const_7719 = relay.const([-9,5,-1,-3,5,-9,2,-8,-7,8,-1,2,-8,7,10,-2,-8,-10,10,-7,3,-10,9,-4,2,4,9,-5,10,6,1,-8,-5,-1,2,-1,-4,-10,10,-1,-5,6,-10,4,7,9,8,-9,6,9,8,2,1,-6,5,-5,-2,-8,-4,-4,2,8,-1,-4,-9,-4,3,8,10,-6,1,7,2,10,8,4,-7,2,1,4,1,6,6,9,-10,-10,6,-6,5,-2,-10,-4,1,7,-4,-4,9,-10,-4,10,3,4,-9,6,8,6,-6,-5,4,1,-2,-2,4,5,-10,3,5,3,-10,6,8,-6,-2,-3,4,4,-8,-7,10,-2,7,6,-5,-5,-9,-2,5,-3,-10,3,2,-10,-8,5,-8,-8,4,-8,2,-3,6,-10,-5,10,-1,7,-2,6,-1,10,9,6,-2,2,10,5,-3,9,-1,-1,-1,6,5,-5,-4,-8,1,-6,-10,6,-6,-6,-9,-4,3,1,-6,-7,-2,7,-5,8,-1,-10,-3,-3,-9,-7,-5,7,8,1,-8,5,9,5,-7,10,9,2,-6,2,-5,4,-10,9,-10,4,-7,5,8,-9,-4,4,-1,-7,1,-4,8,8,8,8,6,-3,10,8,-9,5,-8,-9,5,-7,5,5,-7,1,-8,1,-10,4,4,8,-9,-9,1,-5,5,-5,1,-2,-10,-6,-2,2,-1,4,8,-1,6,-3,1,5,10,-6,9,3,-1,-8,4,-8,6,-4,-5,-3,-6,-10,-6,3,-5,1,7,5,-1,-4,3,-3,6,-7,-2,-2,9,-7,6,-3,9,7,7,7,-5,4,2,10,5,-1,-8,-5,-4,1,2,-3,9,-10,-9,6,-5,3,8,-7,9,-9,-10,3,9,-6,-8,-4,10,-3,9,5,2,3,-1,2,-8,-8,-7,4,5,-7,-2,9,-4,-1,4,1,3,-5,-6,-6,-9,-7,-5,2,-3,-2,1,7,8,2,-3,9,7,-2,-2,-1,5,9,9,2,2,8,-7,-3,-2,-8,-8,-1,-10,1,-3,3,8,-8,3,10,-5,-1,3,7,10,10,-2,-4,6,-4,-8,5,-9,5,-4,-9,3,-1,-3,10,6,1,3,-10,-3,-5,3,8,-6,6,-6,-1,5,5,-2,3,-7,8,2,-8,-4,7,-7,-9,-6,5,10,-2,7,2,4,-9,-2,10,5,-10,-1,6,9,-10,-2,10,-10,4,-2,9,4,7,-5,9,-3,8,-5,3,-2,3,-8,6,7,-7,8,5,6,-7,6,-2,6,-6,-6,7,2,4,2,9,-1,8,-4,1,-4,-4,8,-1,8,5,6,6,9,7,-9,1,-3,-9,-2,1,-3,-6,1,-3,-7,-4,10,1,9,1,4,-10,-10,6,-1,6,1,5,1,2,-6,-3,8,6,-1,7,-8,4,8,-8,6,5,7,-3,7,8,-4,10,6,1,-4,3,-9,-9,-7,-8,-2,4,4,-2,5,-6,1,-2,3,-4,-6,-8,6,-2,6,-9,4,10,1,10,-1,4,4,1,-1,-4,-4,10,10,4,-3,-4,6,-6,5,-4,2,-10,-6,-6,6,4,4,1,-5,2,9,4,2,-4,-5,5,6,6,6,9,-3,5,6,-3,-2,10,1,-7,-5,9,-1,9,-8,9,8,8,-10,9,9,-8,7,2,-5,8,-2,-2,-1,-10,8,5,-7,7,5,5,10,-5,-3,-4,8,10,10,10,-3,-10,-10,-6,5,-6,3,-6,-5,9,-8,10,-8,-5,-2,-8,5,-7,3,4,9,10,-9,5,9,-6,1,-2,-6,-5,-4,-3,-3,6,4,-5,9,-6,-4,-6,7,10,10,6,1,-4,8,-5,-6,8,10,4,1,-10,1,5,-8,7,-9,1,6,-4,-3,-7,2,10,9,1,-3,4,-7,-3,6,-10,-3,-4,8,-5,-8,9,-10,-2,-2,10,6,-1,-4,5,-4,-6,7,8,-1,4,5,-1,-2,-3,-8,2,-8,-4,-7,4,-3,8,2,3,7,5,1,-9,9,-9,-7,-8,6,-7,10,-4,-2,2,6,-9,3,7,2,-10,9,7,-2,9,6,1,-7,-8,5,7,5,4,-2,5,8,4,-5,-3,5,-5,10,-6,8,10,-3,-5,-4,8,4,9,-7,1,-3,8,-8,8,8,-7,-9,-2,-5,-1,-7,-3,2,-3,5,10,-8,-6,1,4,-8,-8,9,1,6,-1,1,-4,-7,2,2,-2,10,7,-1,-3,-4,-8,-8,9,1,6,5,6,8,-6,10,9,5,3,8,9,-6,7,5,7,7,9,3,3,-3,-10,-8,-5,6,3,6,8,-8,-8,-2,-9,10,8,-3,-5,-4,1,7,-9,8,10,1,-7,-4,1,2,2,10,-7,5,-1,-10,-2,-10,1,10,-1,-7,1,-3,-7,4,9,1,7,10,4,-10,-7,7,8,7,-10,8,-8,-4,8,-6,2,-4,3,6,-4,-6,-7,-6,10,-4,10,2,3,-4,-5,-1,-6,-5,9,-8,10,-3,-9,-3,4,9,-9,1,6,6,-4,8,2,-10,-7,-5,6,-7,6,-4,-9,-4,6,2,-1,-3,3,-6,7,7,8,-4,-7,1,-10,4,10,8,3,7,-8,10,4,-10,6,6,7,-10,8,2,6,9,-3,-1,-9,-2,-9,-2,-10,3,-10,-10,6,3,-1,5,-2,3,-3,4,3,3,-10,-4,-7,-8,5,-6,-10,-8,-6,8,9,-3,-6,-6,-3,-2,6,-5,4,-2,1,-1,-8,2,3,-10,-1,-5,-10,-7,-2,7,-4,4,6,-8,-5,6,9,-7,-7,-5,2,7,-2,6,-3,5,7,-7,5,-8,2,2,-3,6,-6,10,10,1,-4,-8,-1,-6,2,1,-7,-6,6,-2,8,1,-8,3,10,2,2,3,-4,-4,-2,-2,6,2,9,-1,4,3,2,-2,10,8,-3,-5,-2,3,-4,5,-4,-3,10,10,-5,6,6,4,1,8,-3,-10,2,8,-8,-7,9,5,-6,-5,-7,2,10,-1,-6,-6,-4,5,-10,5,8,-2,3,-10,6,10,8,-9,6,1,1,-4,-4,2,-3,-5,8,-10,9,-8,5,6,-1,-6,-7,10,6,2,4,5,-10,8,2,-8,6,-3,5,-8,6,-3,1,-10,1,7,5,-3,-6,2,-7,-6,8,7,1,-10,-9,2,10,7,4,-7,9,4,8,-3,6,-1,-1,10,4,-10,4,-3,4,6,-5,6,2,9,-8,7,2,-8,4,6,9,1,8,10,3,1,-10,1,-9,-1,3,-10,-4,9,-8,8,-10,1,-10,-1,6,10,-1,7,1,6,6,8,-8,-9,-1,6,-5,-9,-7,-9,-2,-10,-8,-4,4,3,-10,9,-10,-4,5,-10,6,-7,-10,7,-5,-9,-5,2,-5,-1,-7,-2,-1,8,8,-8,7,-9,-2,-1,5,-10,2,-4,-8,-3,7,2,4,6,7,-6,9,-3,4,-8,5,1,-1,-6,2,-5,-7,-9,-8,2,-6,2,-6,6,1,8,1,5,6,2,3,9,6,-10,2,2,10,3,10,-5,5,-9,3,-10,-7,7,2,9,-3,-6,3,-2,3,1,7,4,-7,10,-7,7,7,-6,-1,10,-6,-8,4,3,7,9,-10,-10,8,-7,2,-10,9,9,3,-5,-4,9,4,5,6,9,-9,-4,-7,-1,-6,-10,-7,6,-6,8,-3,8,-8,1,7,9,7,2,-4,-6,1,5,3,-7,-4,1,-9,7,3,1,-7,5,-6,1,9,-10,3,8,9,-7,8,10,-6,-7,6,9,10,9,-3,8,10,-2,-5,9,6,9,-3,-5,6,7,10,5,-2,-8,7,-8,-3,-9,1,-4,-3,4,10,4,9,-9,-9,-1,-1,9,4,-6,-8,-5,3,7,-10,4,10,9,-1,-10,-5,3,-9,-5,-10,10,-7,6,-4,-8,3,6,1,-5,-6,-5,4,-6,-10,6,3,7,-10,-10,5,-9,-1,4,-2,6,-3,-8,1,-2,6,-1,5,-1,-3,9,10,-8,3,-4,-2,3,-3,4,5,-5,5,2,-5,5,3,-6,2,-5,-10,1,1,-9,7,10,-7,-4,2,2,-10,-7,-1,-5,1,-1,1,2,8,-8,-3,8,3,6,-10,5,5,3,5,2,-10,-6,5,-2,-1,7,-7,8,6,5,2,6,-2,-5,8,4,10,-6,-9,-9,9,6,2,-7,-8,4,2,7,-10,-10,2,4,-5,-9,1,7,-6,7,9,-6,-6,-8,2,-2,-10,9,-8,5,5,10,-4,7,3,7,8,10,-4,2,-4,6,-7,-7,8,-10,8,3,8,3,4,3,1,-5,2,9,-2,-9,2,5,7,-4,-7,6,-7,-9,9,4,-7,-5,8,2,-10,10,4,3,3,6,-4,-9,3,3,-2,-2,-8,6,10,6,9,-4,-3,4,-4,-8,-5,1,-7,-8,1,-5,-6,5,-1,9,-8,2,-10,9,-7,2,6,-7,-8,-1,6,10,-9,1,-7,-9,-3,-8,5,7,-6,3,-4,4,-5,3,-3,5,-7,1,7,10,-2,5,8,1,-2,-8,3,8,-7,1,-3,1,5,5,3,-3,6,4,9,9,-8,-6,9,10,5,5,10,-8,-7,6,-8,6,-7,1,-4,5,-7,4,5,3,5,-7,-3,7,-8,1,4,-4,-10,4,5,-7,-2,-10,2,8,9,-2,2,2,4], dtype = "uint64")#candidate|7719|(1792,)|const|uint64
const_7720 = relay.const(5, dtype = "uint8")#candidate|7720|()|const|uint8
var_7721 = relay.var("var_7721", dtype = "uint8", shape = (672, 1))#candidate|7721|(672, 1)|var|uint8
call_7718 = relay.TupleGetItem(func_5788_call(relay.reshape(const_7719.astype('uint64'), [8, 14, 16]), relay.reshape(const_7719.astype('uint64'), [8, 14, 16]), relay.reshape(const_7720.astype('uint8'), []), relay.reshape(var_7721.astype('uint8'), [168, 4]), ), 1)
call_7722 = relay.TupleGetItem(func_5794_call(relay.reshape(const_7719.astype('uint64'), [8, 14, 16]), relay.reshape(const_7719.astype('uint64'), [8, 14, 16]), relay.reshape(const_7720.astype('uint8'), []), relay.reshape(var_7721.astype('uint8'), [168, 4]), ), 1)
func_3558_call = mod.get_global_var('func_3558')
func_3562_call = mutated_mod.get_global_var('func_3562')
const_7748 = relay.const([-6.314868,4.186917,1.020720,-1.859265,-8.583447,0.629356,6.865495,-3.036645,-4.898459,-8.691123,-8.137906,-1.368374,9.510830,7.366526,-7.835432,0.886860,3.133444,-7.353507,-1.439348,7.559162,-9.130427,6.567367,-1.259574,0.866930,7.730743,3.437905,0.300032,-8.847096,-8.333768,-4.985523,-4.961342,0.985227,-4.095824,-4.093556,-2.698391,7.086901,6.503813,-2.843249,-1.220695,-0.764309,-5.989604,8.917793,9.706278,-1.501791,1.861628,4.566596,-7.814977,-0.495011,-4.902731,2.776534,-4.965065,3.425074,-8.415644,9.630565,-7.339854,-5.878860,5.333596,-0.173347,6.515238,3.428667,9.403923,-4.068755,3.431086,1.605696,-4.463677,5.506329,1.158941,-8.223103,-6.951971,0.651397,3.648934,3.630814,8.823782,2.058895,-8.356998,-7.930231,3.949234,0.230724,7.134627,3.505619,-6.964525,-7.143719,8.770808,2.033252,-5.216304,-1.627512,-2.268005,-1.413296,-7.284010,-6.686748,-9.823171,-4.709966,-2.715457,2.442856,-5.968340,8.908397,9.488105,3.363131,-9.066959,-8.819064,1.456509,-2.344056,0.185810,3.782971,-0.047027,-2.057769,-3.145056,4.837707,5.940307,-6.776470,3.802656,-9.879977,8.050248,8.341155,-5.458805,-6.043674,4.343035,3.979537,-3.978714,-9.254199,-7.025743,6.050940,2.594789,9.607291,7.332771,4.808416,7.802259,7.307184,3.543009,-1.998164,7.794272,7.181281,9.251677,2.297351,7.631619,9.988954,-5.715918,4.143728,6.667018,-4.572046,-4.143257,7.483768,6.722007,3.702304,1.166484,-8.954932,-1.327275,9.015180,-1.847569,7.266042,-3.835071,-1.372657,-2.549991,1.306774,-7.675835,-9.988660,8.158070,9.928937,7.673178,0.989903,-2.892153,6.824736,0.604190,5.483519,6.979279,1.439740,4.503440,-5.800922,8.454264,7.843670,-1.332108,9.945279,9.609129,-8.463464,0.561973,4.821518,-1.436334,-6.317366,-6.728391,0.688267,0.200568,6.062659,-2.490384,-0.101178,9.507395,-9.899622,9.389293,5.992842,-0.434703,6.476972,6.670543,8.080979,1.888483,2.215113,8.229740,3.035596,-5.149973,1.180419,7.602664,-3.435178,7.620706,-9.347245,-0.417753,1.057133,1.365433,-4.242132,-6.587856,-0.586728,-4.212351,8.416759,4.473862,-7.057329,5.919293,-2.956026,8.909726,-5.291956,5.585944,4.307435,-9.824749,-6.517646,-0.267460,4.772969,2.641314,-3.812346,0.758836,8.679793,0.890848,-4.404282,-8.077730,7.379982,-4.684368,-8.368405,-8.590287,5.146425,0.429178,-5.159772,8.047070,-2.311925,-7.141041,-9.956510,-1.344475,-0.004720,5.774224,-0.676306,0.585105,4.032336,1.556131,-4.539545,7.376749,3.173314,6.053104,-6.083249,7.660174,0.794880,-4.939617,0.020412,-4.243308,-6.316354,9.952364,8.687890,-2.228463,-9.851034,-9.410669,8.870313,-8.087569,-6.473945,-4.821994,-8.096085,8.327981,4.157804,0.857310,-9.225596,-2.222546,7.078222,-5.813438,8.331214,5.121249,-8.406609,-3.573916,-1.395199,-3.026505,-0.856979,1.507926,-4.596872,4.233117,-5.080614,8.240305,-8.286738,8.911261,3.138612,-2.185110,-1.707607,-0.811331,7.808770,-3.836558,4.666214,9.613393,-3.678918,2.704951,7.879789,-3.337808,5.232513,7.997389,-7.774812,-7.331929,-8.901570,-9.807415,-9.220113,8.292523,0.391554,4.927060,3.608353,-8.519390,-9.611050,-9.473094,-5.697425,5.317149,-2.458814,6.436500,-1.871169,-2.310113,-5.736023,3.117056,0.365374,2.606166,4.174980,-2.840047,8.027544,-2.533339,-2.515622,3.294501,8.931359,-6.337486,1.785823,-2.319463,3.703938,-6.072995,1.712601,7.390825,9.452895,3.532724,4.922916,1.554611,1.099679,-5.486733,-4.384988,-0.543120,1.541276,-0.929783,3.510710,-0.996115,5.196802,-0.820211,-9.743562,-2.192962,-3.179383,-0.720302,5.650061,-7.278890,9.585178,-8.719563,3.838041,-5.581469,3.044381,9.530228,2.208467,-3.656065,7.806352,-9.509178,-5.978881,1.343739,-8.992001,-6.399583,5.138496,-7.437996,-6.899188,-3.250246,-7.423888,-4.636703,7.970743,-7.926855,4.649599,-1.687851,1.363165,-9.741633,8.071584,4.577986,-5.769521,5.409736,-9.199967,-2.596738,-2.804353,-4.872420,1.897559,-1.639829,2.956644,-5.118356,6.081750,6.099726,3.311006,-7.196368,5.899488,-9.679968,-5.534769,5.705084,-5.920821,6.995227,-0.593593,2.333221,-0.557503,9.914246,-9.933534,-6.851368,-2.603446,-4.466782,7.515240,-3.843219,-6.136730,-1.187682,-2.522258,-9.966805,-7.959545,1.698134,2.209788,-3.697194,-8.463725,3.532798,8.362721,8.292108,6.123723,2.809469,-7.531628,1.054692,9.739067,9.568977,2.232263,-9.395468,6.403584,7.904207,-4.998654,-7.601247,2.995603,3.354493,3.393656,-9.592969,-0.251773,-5.352897,1.854710,-4.237404,6.268049,-3.340248,5.284334,-7.726921,-6.201591,6.228971,-8.367578,0.873542,-0.709141,-1.893929,6.524756,-6.804601,0.405797,8.511417,7.660144,8.786392,4.513707,0.533469,-3.370213,-2.166489,7.428306,9.030032,6.185383,2.945487,1.750507,-5.803999,-6.428960,-7.938446,4.430211,-8.856571,6.224480,4.853681,3.291788,4.571755,7.986130,-0.489074,-5.913232,-2.836912,7.431807,2.382801,9.250735,1.687663,-2.227002,4.945533,6.741401,-6.549802,5.327405,-8.988512,7.587604,-5.893251,5.394908,8.211278,-8.800994,3.182565,-4.824477,-6.416986,-8.443911,5.925732,-4.532510,-3.202738,3.522944,-4.453463,1.864038,5.327314,7.811304,6.584789,6.624553,-4.901077,-2.817885,0.230891,-8.052320,-1.697292,0.102972,7.790061,1.552969,-7.497639,3.572188,7.378550,3.410386,3.132057,6.758221,9.569858,6.270773,-0.466729,6.744032,-8.252143,-7.584971,2.579998,7.063429,2.825466,-0.769248,6.313491,-0.228721,-3.160174,0.132111,-0.433806,-0.902711,7.342349,2.219074,1.726419,2.460046,-9.448232,6.799012,-5.595848,4.759153,3.988956,2.765941,4.738160,4.601602,2.709661,2.394932,0.207933,7.950230,6.106340,8.480997,5.951963,1.926069,-4.728375,9.375548,0.943222,-4.332122,4.561783,8.463555,5.901436,-1.774107,5.306493,0.393007,-8.186017,-9.744391,2.589634,-6.832784,-8.589095,0.675175,-0.954885,9.199340,1.528485,-4.302623,7.759751,6.072062,8.374175,2.627182,0.820141,8.517241,9.148941,3.143617,2.002981,-9.911605,3.737349,-3.517259,-6.616313,4.735999,7.415855,-0.756665,6.576249,-9.446868,-3.865787,-0.605229,-3.529060,9.128074,5.931226,-8.564506,-8.104014,-1.187253,-6.215490,-0.997971,8.324359,-1.773032,5.026014,3.938608,-6.900605,9.962458,-5.958336,-5.373268,-0.228838,-1.419491], dtype = "float32")#candidate|7748|(624,)|const|float32
call_7747 = relay.TupleGetItem(func_3558_call(relay.reshape(const_7748.astype('float32'), [624, 1]), relay.reshape(call_7697.astype('float64'), [12, 11, 5]), ), 3)
call_7749 = relay.TupleGetItem(func_3562_call(relay.reshape(const_7748.astype('float32'), [624, 1]), relay.reshape(call_7697.astype('float64'), [12, 11, 5]), ), 3)
output = relay.Tuple([call_7684,call_7697,const_7698,call_7704,call_7707,call_7709,call_7718,const_7719,const_7720,var_7721,call_7747,const_7748,])
output2 = relay.Tuple([call_7685,call_7699,const_7698,call_7705,call_7708,call_7710,call_7722,const_7719,const_7720,var_7721,call_7749,const_7748,])
func_7750 = relay.Function([var_7721,], output)
mod['func_7750'] = func_7750
mod = relay.transform.InferType()(mod)
mutated_mod['func_7750'] = func_7750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7751 = relay.var("var_7751", dtype = "uint8", shape = (672, 1))#candidate|7751|(672, 1)|var|uint8
func_7750_call = mutated_mod.get_global_var('func_7750')
call_7752 = func_7750_call(var_7751)
output = call_7752
func_7753 = relay.Function([var_7751], output)
mutated_mod['func_7753'] = func_7753
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7810 = relay.var("var_7810", dtype = "uint8", shape = (2, 3, 15))#candidate|7810|(2, 3, 15)|var|uint8
var_7811 = relay.var("var_7811", dtype = "uint8", shape = (2, 3, 15))#candidate|7811|(2, 3, 15)|var|uint8
bop_7812 = relay.greater_equal(var_7810.astype('bool'), relay.reshape(var_7811.astype('bool'), relay.shape_of(var_7810))) # shape=(2, 3, 15)
func_1320_call = mod.get_global_var('func_1320')
func_1323_call = mutated_mod.get_global_var('func_1323')
const_7827 = relay.const([4,-5,6,-9,9,4,9,7,-7,4,-4,5,1,-10,-1,-2,-2,5,-7,1,-4,-9,6,5,-9,-5,3,6,7,2,10,3,3,8,-2,-5,-3,-9,10,-10,-2,2,3,3,6,2,-1,8,2,-5,-4,-1,7,-3,4,6,8,-5,-7,-5,-4,-9,-1,-3,2,7,10,-2,-8,4,8,-9,-9,9,1,-1,2,-3,8,4,-4,5,-1,-1,-1,2,-4,-8,-5,10,-3,-2,2,6,1,-1,2,-9,4,3,-4,5,-6,-2,9,9,-3,-7,-8,7,4,4,-4,1,4,3,9,-5,-10,7,9,3,7,-8,-4,4,-1,-6,-3,2,10,-3,-3,7,-7,7,10,-9,2,4,2,-4,8,7,6,7,7,9,10,5,10,-5,-4,9,-2,1,-1,-7,4,10,-7,6,-7,-4,-10,-8,3,-3,8,2,-5,5,10,6,-10,-4,3,9,-6,9,-1,8,-10,10,5,1,-7,-9,-10,8,1,-7,3,-4,-8,-7,-10,5,-8,-10,-7,4,-7,8,7,-7,10,-3,-1,-4,-10,10,-7,-1,-9,9,-10,-7,-3,-4,5,-1,9,-9,-10,1,-5,-1,-7,-9,-3,-2,1,-10,6,-7,7,-5,-1,-7,9,-1,9,1,6,2,-8,4,6,6,-8,-5,8,-3,6,9,8,-4,-6,4,-4,-1,3,-4,9,-4,-10,6,-9,-8,-1,-4,9,-9,-2,-6,1,1,-5,6,-2,3,-7,3,-9,5,-9,8,-7,-2,-2,-7,8,-9,-2,6,-3,-9,7,-10,-2,6,-4,-1,3,-1,-2,8,-6,-10,3,-4,5,9,-5,2,-4,1,5,8,-5,-5,-7,6,1,4,4,-10,-3,-2,-8,8,-3,1,-2,7,7,-4,-4,-10,8,9,-3,-10,-10,5,-9,1,3,-1,10,-4,-10,3,-1,-9,8,9,-6,8,-1,3,7,1,5,-6,-10,2,-3,1,2,2,-7,3,-10,-9,-3,3,8,1,6,6,10,-5,7,-6,8,-10,9,-10,4,1,6,9,-8,5,8,1,3,2,1,-8,-3,6,2,2,7,-5,-9,-5,5,-4,-5,-4,10,10,-1,2,7,-8,4,-6,5,-4,-6,-3,2,7,-2,-8,4,-4,6,-10,4,3,8,-8,1,-7,-10,-7,8,10,4,2,5,2], dtype = "uint16")#candidate|7827|(448,)|const|uint16
call_7826 = func_1320_call(relay.reshape(const_7827.astype('uint16'), [8, 14, 4]))
call_7828 = func_1320_call(relay.reshape(const_7827.astype('uint16'), [8, 14, 4]))
output = relay.Tuple([bop_7812,call_7826,const_7827,])
output2 = relay.Tuple([bop_7812,call_7828,const_7827,])
func_7837 = relay.Function([var_7810,var_7811,], output)
mod['func_7837'] = func_7837
mod = relay.transform.InferType()(mod)
var_7838 = relay.var("var_7838", dtype = "uint8", shape = (2, 3, 15))#candidate|7838|(2, 3, 15)|var|uint8
var_7839 = relay.var("var_7839", dtype = "uint8", shape = (2, 3, 15))#candidate|7839|(2, 3, 15)|var|uint8
output = func_7837(var_7838,var_7839,)
func_7840 = relay.Function([var_7838,var_7839,], output)
mutated_mod['func_7840'] = func_7840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6450_call = mod.get_global_var('func_6450')
func_6452_call = mutated_mod.get_global_var('func_6452')
call_7858 = relay.TupleGetItem(func_6450_call(), 0)
call_7859 = relay.TupleGetItem(func_6452_call(), 0)
func_6573_call = mod.get_global_var('func_6573')
func_6575_call = mutated_mod.get_global_var('func_6575')
var_7883 = relay.var("var_7883", dtype = "float32", shape = (594, 1))#candidate|7883|(594, 1)|var|float32
call_7882 = relay.TupleGetItem(func_6573_call(relay.reshape(var_7883.astype('float32'), [11, 6, 9])), 0)
call_7884 = relay.TupleGetItem(func_6575_call(relay.reshape(var_7883.astype('float32'), [11, 6, 9])), 0)
output = relay.Tuple([call_7858,call_7882,var_7883,])
output2 = relay.Tuple([call_7859,call_7884,var_7883,])
func_7893 = relay.Function([var_7883,], output)
mod['func_7893'] = func_7893
mod = relay.transform.InferType()(mod)
mutated_mod['func_7893'] = func_7893
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7894 = relay.var("var_7894", dtype = "float32", shape = (594, 1))#candidate|7894|(594, 1)|var|float32
func_7893_call = mutated_mod.get_global_var('func_7893')
call_7895 = func_7893_call(var_7894)
output = call_7895
func_7896 = relay.Function([var_7894], output)
mutated_mod['func_7896'] = func_7896
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7957 = relay.var("var_7957", dtype = "float64", shape = (12, 11, 5))#candidate|7957|(12, 11, 5)|var|float64
uop_7958 = relay.rsqrt(var_7957.astype('float64')) # shape=(12, 11, 5)
func_6611_call = mod.get_global_var('func_6611')
func_6614_call = mutated_mod.get_global_var('func_6614')
const_7974 = relay.const(-2, dtype = "uint8")#candidate|7974|()|const|uint8
call_7973 = relay.TupleGetItem(func_6611_call(relay.reshape(const_7974.astype('uint8'), [])), 0)
call_7975 = relay.TupleGetItem(func_6614_call(relay.reshape(const_7974.astype('uint8'), [])), 0)
output = relay.Tuple([uop_7958,call_7973,const_7974,])
output2 = relay.Tuple([uop_7958,call_7975,const_7974,])
func_7982 = relay.Function([var_7957,], output)
mod['func_7982'] = func_7982
mod = relay.transform.InferType()(mod)
var_7983 = relay.var("var_7983", dtype = "float64", shape = (12, 11, 5))#candidate|7983|(12, 11, 5)|var|float64
output = func_7982(var_7983)
func_7984 = relay.Function([var_7983], output)
mutated_mod['func_7984'] = func_7984
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8005 = relay.const([[-6.606914],[-0.742275],[9.613459],[-3.898516],[4.220439],[-2.544975],[-0.876208],[-7.350703]], dtype = "float32")#candidate|8005|(8, 1)|const|float32
var_8006 = relay.var("var_8006", dtype = "float32", shape = (8, 1))#candidate|8006|(8, 1)|var|float32
bop_8007 = relay.greater_equal(const_8005.astype('bool'), relay.reshape(var_8006.astype('bool'), relay.shape_of(const_8005))) # shape=(8, 1)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_8013 = func_2905_call()
call_8014 = func_2905_call()
output = relay.Tuple([bop_8007,call_8013,])
output2 = relay.Tuple([bop_8007,call_8014,])
func_8019 = relay.Function([var_8006,], output)
mod['func_8019'] = func_8019
mod = relay.transform.InferType()(mod)
var_8020 = relay.var("var_8020", dtype = "float32", shape = (8, 1))#candidate|8020|(8, 1)|var|float32
output = func_8019(var_8020)
func_8021 = relay.Function([var_8020], output)
mutated_mod['func_8021'] = func_8021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_8028 = relay.TupleGetItem(func_4639_call(), 0)
call_8029 = relay.TupleGetItem(func_4640_call(), 0)
output = relay.Tuple([call_8028,])
output2 = relay.Tuple([call_8029,])
func_8032 = relay.Function([], output)
mod['func_8032'] = func_8032
mod = relay.transform.InferType()(mod)
mutated_mod['func_8032'] = func_8032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8032_call = mutated_mod.get_global_var('func_8032')
call_8033 = func_8032_call()
output = call_8033
func_8034 = relay.Function([], output)
mutated_mod['func_8034'] = func_8034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7468_call = mod.get_global_var('func_7468')
func_7469_call = mutated_mod.get_global_var('func_7469')
call_8049 = relay.TupleGetItem(func_7468_call(), 0)
call_8050 = relay.TupleGetItem(func_7469_call(), 0)
func_6390_call = mod.get_global_var('func_6390')
func_6391_call = mutated_mod.get_global_var('func_6391')
call_8058 = func_6390_call()
call_8059 = func_6390_call()
func_2176_call = mod.get_global_var('func_2176')
func_2178_call = mutated_mod.get_global_var('func_2178')
const_8086 = relay.const([6,6,-5,-10,-8,-3,5,10,-7,-1,3,-4,10,-3,1,-2,6,-1,-5,-6,-8,-1,-2,8,-6,-8,8,9,-5,-7,-10,5,7,9,-9,-6,-5,-9,7,-10,-6,-2,-2,2,-5,6,-8,-1,7,6,6,-4,-8,-10,2,-10,8,-5,-4,10,6,5,4,-10,8,10,7,-5,-7,-1,-4,-9,2,-7,-1,-4,-10,4,6,7,-9,6,-1,10,-7,-8,2,7,1,8,8,2,2,-2,-7,2,7,3,-10,-5,4,10,-1,7,1,-6,9,7,-4,-10,9,9,10,4,-5,-9,-4,-6,-5,7,-10,3,10,1,-8,-7,4,2,7,4,-7,-2,1,6,-1,-2,-5,-10,-4,1,3,10,3,1,-10,-2,9,9,-2,-6,7,5,2,9,8,9,-7,1,10,7,-1,8,5,-10,2,1,5,-5,3,4,-5,5,1,-9,-9,3,-9,10,8,-10,-9,4,-9,2,5,3,8,-10,-3,-1,9,-4,7,-2,-5,7,-5,7,-10,-4,-4,4,5,4,5,4,-1,2,-2,3,7,1,-3,-4,7,9,-6,-5,7,3,-7,5,3,6,-2,-5,10,-10,4,7,3,5,9,2,-1,7,2,-6,9,-2,-2,9,3,-7,3,-8,-2,-8,5,6,-5,-4,4,3,1,-6,2,-4,-5,10,7,-8,3,9,-6,-3,-9,-9,6,-8,-7,9,2,-2,4,-6,-2,-7,10,2,-2,-6,-2,4,7,7,8,1,7,6,-9,-2,7,-7,-9,3,-6,2,6,-9,10,6,10,-6,5,10,-4,-5,6,-10,-5,-4,-3,-10,-4,1,3,-2,7,1,9,5,8,6,4,-6,-8,9,-7,-2,7,5,-3,4,4,-1,9,-8,-8,8,10,-2,-4,-2,9,4,-7,8,7,-9,9,7,6,6,10,7,-8,10,7,7,-8,-5,-1,5,7,2,-6,6,2,7,6,2,10,-9,4,6,-6,-6,-6,-6,7,-8,5,-6,-6,9,-4,7,2,2,2,9,10,5,-8,-6,-9,9,-10,2,-5,-9,1,4,4,3,-7,3,10,1,9,5,4,3,-9,2,-4,-7,-7,-2,9,6,-10,3,-7,9,6,7,10,-5,-2,4,-8,-5,-4,-5,-4,10,9,3,-10,5,8,7,9,6,-9,-9,3,-1,3,-9,6,-1,5,-3,8,-2,-10,-6,-2,-2,5,7,7,7,5,-7,5,6,-3,6,4,10,6,-5,-8,-9,-8,3,8,5,5,-2,9,-2,-4,-6,6,-4,-3,1,6,6,-10,-1,-10,10,10,8,10,4,10,-4,-7,9,7,-1,3,7,8,-2,6,-6,3,-6,5,9,-1,2,-3,-7,-4,-3,10,10,10,8,3,-2,9,-3,7,2,5,5,-6,8,5,-8,-3,-2,-2,1,-4,4,-9,8,9,4,-5,-3,3,2,5,10,-8,-3,3,-6,4,-10,10,-9,-9,4,1,-4,1,2,-6,3,5,6,9,6,-5,8,-4,4,-1,-7,8,-9,-7,-4,-3,9,-3,7,9,7,2,9,2,1,-4,8,-8,-2,7,-10,-4,-8,5,1,3,-2,-3,10,6,1,-8,5,-5,2,4,-10,-2,7,8,-5,-8,-5,-10,6,-4,8,-5,9,2,10,5,4,2,7,1,-2,-1,-8,10,6,1,8,-9,-6,8,4,-7,1,2,-1,9,10,8,10,-3,4,10,-2,8,-9,3,10,-4,9,-8,-6,2,9,-5,-10], dtype = "int16")#candidate|8086|(672,)|const|int16
call_8085 = relay.TupleGetItem(func_2176_call(relay.reshape(const_8086.astype('int16'), [14, 12, 4])), 0)
call_8087 = relay.TupleGetItem(func_2178_call(relay.reshape(const_8086.astype('int16'), [14, 12, 4])), 0)
output = relay.Tuple([call_8049,call_8058,call_8085,const_8086,])
output2 = relay.Tuple([call_8050,call_8059,call_8087,const_8086,])
func_8090 = relay.Function([], output)
mod['func_8090'] = func_8090
mod = relay.transform.InferType()(mod)
mutated_mod['func_8090'] = func_8090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8090_call = mutated_mod.get_global_var('func_8090')
call_8091 = func_8090_call()
output = call_8091
func_8092 = relay.Function([], output)
mutated_mod['func_8092'] = func_8092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7468_call = mod.get_global_var('func_7468')
func_7469_call = mutated_mod.get_global_var('func_7469')
call_8120 = relay.TupleGetItem(func_7468_call(), 1)
call_8121 = relay.TupleGetItem(func_7469_call(), 1)
output = call_8120
output2 = call_8121
func_8129 = relay.Function([], output)
mod['func_8129'] = func_8129
mod = relay.transform.InferType()(mod)
output = func_8129()
func_8130 = relay.Function([], output)
mutated_mod['func_8130'] = func_8130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2915_call = mod.get_global_var('func_2915')
func_2916_call = mutated_mod.get_global_var('func_2916')
call_8157 = func_2915_call()
call_8158 = func_2915_call()
output = relay.Tuple([call_8157,])
output2 = relay.Tuple([call_8158,])
func_8184 = relay.Function([], output)
mod['func_8184'] = func_8184
mod = relay.transform.InferType()(mod)
output = func_8184()
func_8185 = relay.Function([], output)
mutated_mod['func_8185'] = func_8185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3834_call = mutated_mod.get_global_var('func_3834')
call_8203 = relay.TupleGetItem(func_3833_call(), 0)
call_8204 = relay.TupleGetItem(func_3834_call(), 0)
func_4918_call = mod.get_global_var('func_4918')
func_4922_call = mutated_mod.get_global_var('func_4922')
var_8207 = relay.var("var_8207", dtype = "uint8", shape = (672,))#candidate|8207|(672,)|var|uint8
var_8208 = relay.var("var_8208", dtype = "uint16", shape = (8, 56))#candidate|8208|(8, 56)|var|uint16
call_8206 = relay.TupleGetItem(func_4918_call(relay.reshape(var_8207.astype('uint8'), [672,]), relay.reshape(var_8208.astype('uint16'), [448,]), ), 0)
call_8209 = relay.TupleGetItem(func_4922_call(relay.reshape(var_8207.astype('uint8'), [672,]), relay.reshape(var_8208.astype('uint16'), [448,]), ), 0)
func_2535_call = mod.get_global_var('func_2535')
func_2537_call = mutated_mod.get_global_var('func_2537')
call_8212 = relay.TupleGetItem(func_2535_call(), 0)
call_8213 = relay.TupleGetItem(func_2537_call(), 0)
var_8214 = relay.var("var_8214", dtype = "uint16", shape = (8, 56))#candidate|8214|(8, 56)|var|uint16
bop_8215 = relay.logical_or(var_8208.astype('bool'), relay.reshape(var_8214.astype('bool'), relay.shape_of(var_8208))) # shape=(8, 56)
output = relay.Tuple([call_8203,call_8206,var_8207,call_8212,bop_8215,])
output2 = relay.Tuple([call_8204,call_8209,var_8207,call_8213,bop_8215,])
func_8224 = relay.Function([var_8207,var_8208,var_8214,], output)
mod['func_8224'] = func_8224
mod = relay.transform.InferType()(mod)
var_8225 = relay.var("var_8225", dtype = "uint8", shape = (672,))#candidate|8225|(672,)|var|uint8
var_8226 = relay.var("var_8226", dtype = "uint16", shape = (8, 56))#candidate|8226|(8, 56)|var|uint16
var_8227 = relay.var("var_8227", dtype = "uint16", shape = (8, 56))#candidate|8227|(8, 56)|var|uint16
output = func_8224(var_8225,var_8226,var_8227,)
func_8228 = relay.Function([var_8225,var_8226,var_8227,], output)
mutated_mod['func_8228'] = func_8228
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8230 = relay.var("var_8230", dtype = "float64", shape = (10, 4, 2))#candidate|8230|(10, 4, 2)|var|float64
uop_8231 = relay.exp(var_8230.astype('float64')) # shape=(10, 4, 2)
uop_8242 = relay.log(var_8230.astype('float32')) # shape=(10, 4, 2)
func_6954_call = mod.get_global_var('func_6954')
func_6957_call = mutated_mod.get_global_var('func_6957')
var_8249 = relay.var("var_8249", dtype = "float32", shape = (3, 198))#candidate|8249|(3, 198)|var|float32
call_8248 = relay.TupleGetItem(func_6954_call(relay.reshape(var_8249.astype('float32'), [594,])), 2)
call_8250 = relay.TupleGetItem(func_6957_call(relay.reshape(var_8249.astype('float32'), [594,])), 2)
bop_8254 = relay.add(uop_8242.astype('uint16'), relay.reshape(uop_8231.astype('uint16'), relay.shape_of(uop_8242))) # shape=(10, 4, 2)
output = relay.Tuple([call_8248,var_8249,bop_8254,])
output2 = relay.Tuple([call_8250,var_8249,bop_8254,])
func_8258 = relay.Function([var_8230,var_8249,], output)
mod['func_8258'] = func_8258
mod = relay.transform.InferType()(mod)
mutated_mod['func_8258'] = func_8258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8258_call = mutated_mod.get_global_var('func_8258')
var_8260 = relay.var("var_8260", dtype = "float64", shape = (10, 4, 2))#candidate|8260|(10, 4, 2)|var|float64
var_8261 = relay.var("var_8261", dtype = "float32", shape = (3, 198))#candidate|8261|(3, 198)|var|float32
call_8259 = func_8258_call(var_8260,var_8261,)
output = call_8259
func_8262 = relay.Function([var_8260,var_8261,], output)
mutated_mod['func_8262'] = func_8262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7468_call = mod.get_global_var('func_7468')
func_7469_call = mutated_mod.get_global_var('func_7469')
call_8299 = relay.TupleGetItem(func_7468_call(), 0)
call_8300 = relay.TupleGetItem(func_7469_call(), 0)
func_4066_call = mod.get_global_var('func_4066')
func_4068_call = mutated_mod.get_global_var('func_4068')
call_8305 = relay.TupleGetItem(func_4066_call(relay.reshape(call_8299.astype('float32'), [5, 5, 13])), 4)
call_8306 = relay.TupleGetItem(func_4068_call(relay.reshape(call_8299.astype('float32'), [5, 5, 13])), 4)
output = relay.Tuple([call_8299,call_8305,])
output2 = relay.Tuple([call_8300,call_8306,])
func_8314 = relay.Function([], output)
mod['func_8314'] = func_8314
mod = relay.transform.InferType()(mod)
mutated_mod['func_8314'] = func_8314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8314_call = mutated_mod.get_global_var('func_8314')
call_8315 = func_8314_call()
output = call_8315
func_8316 = relay.Function([], output)
mutated_mod['func_8316'] = func_8316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6450_call = mod.get_global_var('func_6450')
func_6452_call = mutated_mod.get_global_var('func_6452')
call_8346 = relay.TupleGetItem(func_6450_call(), 0)
call_8347 = relay.TupleGetItem(func_6452_call(), 0)
output = relay.Tuple([call_8346,])
output2 = relay.Tuple([call_8347,])
func_8351 = relay.Function([], output)
mod['func_8351'] = func_8351
mod = relay.transform.InferType()(mod)
output = func_8351()
func_8352 = relay.Function([], output)
mutated_mod['func_8352'] = func_8352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3656_call = mod.get_global_var('func_3656')
func_3657_call = mutated_mod.get_global_var('func_3657')
call_8504 = func_3656_call()
call_8505 = func_3656_call()
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_8511 = relay.TupleGetItem(func_2776_call(), 0)
call_8512 = relay.TupleGetItem(func_2778_call(), 0)
output = relay.Tuple([call_8504,call_8511,])
output2 = relay.Tuple([call_8505,call_8512,])
func_8532 = relay.Function([], output)
mod['func_8532'] = func_8532
mod = relay.transform.InferType()(mod)
output = func_8532()
func_8533 = relay.Function([], output)
mutated_mod['func_8533'] = func_8533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_8556 = relay.TupleGetItem(func_2776_call(), 0)
call_8557 = relay.TupleGetItem(func_2778_call(), 0)
output = call_8556
output2 = call_8557
func_8558 = relay.Function([], output)
mod['func_8558'] = func_8558
mod = relay.transform.InferType()(mod)
mutated_mod['func_8558'] = func_8558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8558_call = mutated_mod.get_global_var('func_8558')
call_8559 = func_8558_call()
output = call_8559
func_8560 = relay.Function([], output)
mutated_mod['func_8560'] = func_8560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5227_call = mod.get_global_var('func_5227')
func_5229_call = mutated_mod.get_global_var('func_5229')
call_8591 = func_5227_call()
call_8592 = func_5227_call()
func_3321_call = mod.get_global_var('func_3321')
func_3326_call = mutated_mod.get_global_var('func_3326')
const_8598 = relay.const(4.997502, dtype = "float32")#candidate|8598|()|const|float32
var_8599 = relay.var("var_8599", dtype = "float32", shape = (20,))#candidate|8599|(20,)|var|float32
var_8600 = relay.var("var_8600", dtype = "int16", shape = (975,))#candidate|8600|(975,)|var|int16
call_8597 = relay.TupleGetItem(func_3321_call(relay.reshape(const_8598.astype('float32'), []), relay.reshape(var_8599.astype('float32'), [2, 1, 10]), relay.reshape(var_8600.astype('int16'), [975,]), ), 4)
call_8601 = relay.TupleGetItem(func_3326_call(relay.reshape(const_8598.astype('float32'), []), relay.reshape(var_8599.astype('float32'), [2, 1, 10]), relay.reshape(var_8600.astype('int16'), [975,]), ), 4)
uop_8616 = relay.log10(call_8597.astype('float64')) # shape=(11, 3, 6)
uop_8618 = relay.log10(call_8601.astype('float64')) # shape=(11, 3, 6)
func_4066_call = mod.get_global_var('func_4066')
func_4068_call = mutated_mod.get_global_var('func_4068')
var_8630 = relay.var("var_8630", dtype = "float32", shape = (325,))#candidate|8630|(325,)|var|float32
call_8629 = relay.TupleGetItem(func_4066_call(relay.reshape(var_8630.astype('float32'), [5, 5, 13])), 3)
call_8631 = relay.TupleGetItem(func_4068_call(relay.reshape(var_8630.astype('float32'), [5, 5, 13])), 3)
uop_8639 = relay.cosh(uop_8616.astype('float32')) # shape=(11, 3, 6)
uop_8641 = relay.cosh(uop_8618.astype('float32')) # shape=(11, 3, 6)
output = relay.Tuple([call_8591,const_8598,var_8599,var_8600,call_8629,var_8630,uop_8639,])
output2 = relay.Tuple([call_8592,const_8598,var_8599,var_8600,call_8631,var_8630,uop_8641,])
func_8645 = relay.Function([var_8599,var_8600,var_8630,], output)
mod['func_8645'] = func_8645
mod = relay.transform.InferType()(mod)
mutated_mod['func_8645'] = func_8645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8645_call = mutated_mod.get_global_var('func_8645')
var_8647 = relay.var("var_8647", dtype = "float32", shape = (20,))#candidate|8647|(20,)|var|float32
var_8648 = relay.var("var_8648", dtype = "int16", shape = (975,))#candidate|8648|(975,)|var|int16
var_8649 = relay.var("var_8649", dtype = "float32", shape = (325,))#candidate|8649|(325,)|var|float32
call_8646 = func_8645_call(var_8647,var_8648,var_8649,)
output = call_8646
func_8650 = relay.Function([var_8647,var_8648,var_8649,], output)
mutated_mod['func_8650'] = func_8650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6870_call = mod.get_global_var('func_6870')
func_6872_call = mutated_mod.get_global_var('func_6872')
call_8659 = func_6870_call()
call_8660 = func_6870_call()
output = relay.Tuple([call_8659,])
output2 = relay.Tuple([call_8660,])
func_8661 = relay.Function([], output)
mod['func_8661'] = func_8661
mod = relay.transform.InferType()(mod)
mutated_mod['func_8661'] = func_8661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8661_call = mutated_mod.get_global_var('func_8661')
call_8662 = func_8661_call()
output = call_8662
func_8663 = relay.Function([], output)
mutated_mod['func_8663'] = func_8663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3634_call = mod.get_global_var('func_3634')
func_3636_call = mutated_mod.get_global_var('func_3636')
call_8763 = relay.TupleGetItem(func_3634_call(), 0)
call_8764 = relay.TupleGetItem(func_3636_call(), 0)
uop_8775 = relay.exp(call_8763.astype('float64')) # shape=(12, 11, 5)
uop_8777 = relay.exp(call_8764.astype('float64')) # shape=(12, 11, 5)
output = relay.Tuple([uop_8775,])
output2 = relay.Tuple([uop_8777,])
func_8785 = relay.Function([], output)
mod['func_8785'] = func_8785
mod = relay.transform.InferType()(mod)
mutated_mod['func_8785'] = func_8785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8785_call = mutated_mod.get_global_var('func_8785')
call_8786 = func_8785_call()
output = call_8786
func_8787 = relay.Function([], output)
mutated_mod['func_8787'] = func_8787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5039_call = mod.get_global_var('func_5039')
func_5040_call = mutated_mod.get_global_var('func_5040')
call_8815 = func_5039_call()
call_8816 = func_5039_call()
output = call_8815
output2 = call_8816
func_8881 = relay.Function([], output)
mod['func_8881'] = func_8881
mod = relay.transform.InferType()(mod)
mutated_mod['func_8881'] = func_8881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8881_call = mutated_mod.get_global_var('func_8881')
call_8882 = func_8881_call()
output = call_8882
func_8883 = relay.Function([], output)
mutated_mod['func_8883'] = func_8883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7298_call = mod.get_global_var('func_7298')
func_7300_call = mutated_mod.get_global_var('func_7300')
call_8921 = relay.TupleGetItem(func_7298_call(), 0)
call_8922 = relay.TupleGetItem(func_7300_call(), 0)
output = call_8921
output2 = call_8922
func_8940 = relay.Function([], output)
mod['func_8940'] = func_8940
mod = relay.transform.InferType()(mod)
mutated_mod['func_8940'] = func_8940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8940_call = mutated_mod.get_global_var('func_8940')
call_8941 = func_8940_call()
output = call_8941
func_8942 = relay.Function([], output)
mutated_mod['func_8942'] = func_8942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2752_call = mod.get_global_var('func_2752')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_8990 = relay.TupleGetItem(func_2752_call(), 0)
call_8991 = relay.TupleGetItem(func_2753_call(), 0)
func_900_call = mod.get_global_var('func_900')
func_903_call = mutated_mod.get_global_var('func_903')
const_8996 = relay.const([-7,5,-2,-3,-1,-4,1,-10,-9,-1,-8,6,3,-7,1,5,-3,-5,-5,7,-7,-2,4,5,2,8,2,-2,-9,5,3,5,-2,-10,1,2,8,-6,-8,6,6,10,9,2,-10,-9,9,-8,-6,-8,6,3,-4,8,10,3,-7,6,6,-5,7,9,8,8,8,1,6,9,4,3,1,-2,1,-6,5,3,-5,-1,2,7,5,-5,1,-2,-3,-9,-1,5,-8,-8,2,9,6,8,-9,-9,2,-7,9,-8,-4,-1,7,-8,-4,-9,8,4,8,-1,7,-1,-3,2,8,8,-8,-9,-4,-3,3,-7,-10,4,-10,-4,6,-8,4,5,-3,-5,2,7,1,6,-1,-5,-1,8,-4,10,8,1,9,5,6,4,-4,-6,10,8,-3,4,-2,7,7,-7,7,-8,-3,10,-4,9,-5,2,-7,7,-5,-3,-3,4,10,-4,1,-5,6,-4,-2,-8,-8,-2,-5,4,-10,-7,-9,-3,-6,8,-1,-10,10,9,8,7,-10,-10,8,4,-3,2,-6,1,-4,-7,-1,3,-2,-3,10,6,-1,-6,2,-8,3,-7,3,-8,8,-1,4,-2,6,9,-7,7,-5,6,3,4,-2,-6,10,3,1,7,-9,6,-4,1,-1,-7,1,4,7,-1,-1,-5,3,9,3,-3,-4,-6,-5,-10,-5,-3,-2,10,6,-2,10,-8,-5,-1,2,1,-3,6,3,-4,-5,-7,-5,10,-10,-8,10,-5,2,5,8,-4,2,10,-6,-6,-1,-9,9,8,2,8,-4,6,9,-4,5,9,-7,-3,-3,-5,-1,3,-4,9,-8,7,-2,-8,2,7,7,5,4,7,10,-4,-8,2,7,-7,8,7,-7,-8,-6,-6,-10,-8,-2,4,9,-2,-4,-9,4,7,2,-2,6,7,7,-6,-6,-1,-9,10,-2,5,7,-10,1,-4,9,1,-8,-9,2,9,-10,-8,-7,7,1,7,5,8,5,1,8,1,-10,10,-6,2,9,-4,-8,-6,-4,-4,2,-7,4,1,9,7,-2,1,-5,-3,3,-3,-10,-8,3,3,6,2,-7,-3,5,-6,-8,-5,10,-9,7,3,-2,2,-7,-1,-7,4,-8,-10,10,1,3,-2,6,-7,3,10,3,1,7,4,6,7,6,8,3,3,-7,-10,-6,8,9,5,2,-3,-9,-2,-6,1,-8,7,10,9,4,-2,8,-10,-2,8,-4,-2,7,-9,4,-4,-9,-4,-2,-8,-6,-7,-4,9,5,-7,-10,1,4,-10,-10,-1,-9,9,9,8,-10,10,-5,8,-8,-8,-6,6,10,8,-4,10,3,-3,-9,-8,7,10,8,-1,-5,-5,-9,-10,-8,-1,-7,-4,-10,-3,-9,7,10,9,7,4,-8,-4,-1,7,5,2,7,-2,-4,-6,-7,-10,-10,7,-8,1,2,-2,-2,-2,7,8,-9,-2,5,-5,-3,-3,1,-2,3,-4,9,-9,7,7,-5,-7,-3,-5,-9,5,5,-4,-10,-5,10,-9,7,9,7,-7,8,7,5,4,-4,5,-8,6,-5,-10,-2,3,5,3,-9,6,-6,-1,-7,-6,-5,-2,2,-9,-1,-4,-8,-2,1,6,-8,7,5,5,-6,-5,-2,4,-5,10,1,-10,-1,3,10,1,-2,-1,10,-9,7,-7,-10,-2,3,-10,-6,-5,-5,-8,-8,2,-9,6,-1,8,-10,-10,6,-5,3,-3,-6,-7,-9,-5,-6,-4,3,6,7,-3,-9,-7,-4,1,-8,8,5,6,-10,10,9,3,-5,6,-5,1,2,6,-10,5,3,1,-1,-3,-7,1,8,6,2,-7,10,10,6,10,-3,2,-2,-8,-2,-8,-6,5,-10,9,-4,1,-6,10,7,6,8,-9,-4,5,-8,5,9,-7,-2,5,3,-3,-8,-1,-4,-6,6,3,10,6,-1,9,-10,1,3,1,3,-6,-7,-6,5,-3,5,3,-4,-5,-9,-6,-1,2,-2,-1,-6,-6,4,-6,-1,-2,-5,-6,-1,7,-5,10,10,9,6,9,-7,-7,-6,-9,-3,5,-3,8,-2,-5,-8,1,6,1,10,-6,-4,7,7,7,5,8,3,-4,-1,-9,4,8,-2,4,7,-8,-4,-1,10,-8,7,3,-2,-4,7,-3,-5,-3,-9,8,8,7,2,-2,3,7,6,2,8,4,-3,-6,-9,7,7,-2,-3,6,6,-8,-10,10,7,-5,-2,-10,-5,3,-9,-1,-8,-1,3,-6,7,-7,1,2,-1,-4,-5,10,-3,5,-3,-8,9,-2,9,1,-6,-5,-8,-6,6,-4,4,-5,6,1,-6,2,10,-10,-4,9,9,-8,2,6,3,9,3,-6,-3,8,-8,7,-4,9,7,-7,-1,-3,-8,1,8,-7,-5,8,2,9,6,-1,4,6,9,8,-8,-5,10,6,-5,9,-9,-9,-2,-2,6,-7,-3,-4,8,-4,-2,3,-2,-2,-5,8,7,-5,-6,7,2,4,9,-10,9,3,1,-5,-8,-2,7,7,5,-1,10,-3,-2,-10,5,7,-3,7,-10,-7,-1,-9,6,10,-9,4,-1,-4,4,-5,3,2,6,-10,-4], dtype = "int16")#candidate|8996|(975,)|const|int16
call_8995 = relay.TupleGetItem(func_900_call(relay.reshape(const_8996.astype('int16'), [13, 15, 5]), relay.reshape(const_8996.astype('int16'), [13, 15, 5]), ), 0)
call_8997 = relay.TupleGetItem(func_903_call(relay.reshape(const_8996.astype('int16'), [13, 15, 5]), relay.reshape(const_8996.astype('int16'), [13, 15, 5]), ), 0)
output = relay.Tuple([call_8990,call_8995,const_8996,])
output2 = relay.Tuple([call_8991,call_8997,const_8996,])
func_9005 = relay.Function([], output)
mod['func_9005'] = func_9005
mod = relay.transform.InferType()(mod)
mutated_mod['func_9005'] = func_9005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9005_call = mutated_mod.get_global_var('func_9005')
call_9006 = func_9005_call()
output = call_9006
func_9007 = relay.Function([], output)
mutated_mod['func_9007'] = func_9007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8129_call = mod.get_global_var('func_8129')
func_8130_call = mutated_mod.get_global_var('func_8130')
call_9024 = func_8129_call()
call_9025 = func_8129_call()
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_9029 = relay.TupleGetItem(func_2494_call(), 0)
call_9030 = relay.TupleGetItem(func_2496_call(), 0)
output = relay.Tuple([call_9024,call_9029,])
output2 = relay.Tuple([call_9025,call_9030,])
func_9031 = relay.Function([], output)
mod['func_9031'] = func_9031
mod = relay.transform.InferType()(mod)
mutated_mod['func_9031'] = func_9031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9031_call = mutated_mod.get_global_var('func_9031')
call_9032 = func_9031_call()
output = call_9032
func_9033 = relay.Function([], output)
mutated_mod['func_9033'] = func_9033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8032_call = mod.get_global_var('func_8032')
func_8034_call = mutated_mod.get_global_var('func_8034')
call_9060 = relay.TupleGetItem(func_8032_call(), 0)
call_9061 = relay.TupleGetItem(func_8034_call(), 0)
func_9031_call = mod.get_global_var('func_9031')
func_9033_call = mutated_mod.get_global_var('func_9033')
call_9085 = relay.TupleGetItem(func_9031_call(), 0)
call_9086 = relay.TupleGetItem(func_9033_call(), 0)
output = relay.Tuple([call_9060,call_9085,])
output2 = relay.Tuple([call_9061,call_9086,])
func_9087 = relay.Function([], output)
mod['func_9087'] = func_9087
mod = relay.transform.InferType()(mod)
mutated_mod['func_9087'] = func_9087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9087_call = mutated_mod.get_global_var('func_9087')
call_9088 = func_9087_call()
output = call_9088
func_9089 = relay.Function([], output)
mutated_mod['func_9089'] = func_9089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_9103 = relay.TupleGetItem(func_3121_call(), 0)
call_9104 = relay.TupleGetItem(func_3123_call(), 0)
func_3833_call = mod.get_global_var('func_3833')
func_3834_call = mutated_mod.get_global_var('func_3834')
call_9105 = relay.TupleGetItem(func_3833_call(), 0)
call_9106 = relay.TupleGetItem(func_3834_call(), 0)
func_180_call = mod.get_global_var('func_180')
func_182_call = mutated_mod.get_global_var('func_182')
var_9108 = relay.var("var_9108", dtype = "int8", shape = (567,))#candidate|9108|(567,)|var|int8
call_9107 = func_180_call(relay.reshape(var_9108.astype('int8'), [7, 9, 9]))
call_9109 = func_180_call(relay.reshape(var_9108.astype('int8'), [7, 9, 9]))
output = relay.Tuple([call_9103,call_9105,call_9107,var_9108,])
output2 = relay.Tuple([call_9104,call_9106,call_9109,var_9108,])
func_9120 = relay.Function([var_9108,], output)
mod['func_9120'] = func_9120
mod = relay.transform.InferType()(mod)
var_9121 = relay.var("var_9121", dtype = "int8", shape = (567,))#candidate|9121|(567,)|var|int8
output = func_9120(var_9121)
func_9122 = relay.Function([var_9121], output)
mutated_mod['func_9122'] = func_9122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5182_call = mod.get_global_var('func_5182')
func_5184_call = mutated_mod.get_global_var('func_5184')
call_9181 = relay.TupleGetItem(func_5182_call(), 0)
call_9182 = relay.TupleGetItem(func_5184_call(), 0)
output = call_9181
output2 = call_9182
func_9187 = relay.Function([], output)
mod['func_9187'] = func_9187
mod = relay.transform.InferType()(mod)
output = func_9187()
func_9188 = relay.Function([], output)
mutated_mod['func_9188'] = func_9188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_9217 = relay.TupleGetItem(func_4639_call(), 0)
call_9218 = relay.TupleGetItem(func_4640_call(), 0)
output = call_9217
output2 = call_9218
func_9231 = relay.Function([], output)
mod['func_9231'] = func_9231
mod = relay.transform.InferType()(mod)
output = func_9231()
func_9232 = relay.Function([], output)
mutated_mod['func_9232'] = func_9232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2905_call = mod.get_global_var('func_2905')
func_2907_call = mutated_mod.get_global_var('func_2907')
call_9261 = func_2905_call()
call_9262 = func_2905_call()
func_3341_call = mod.get_global_var('func_3341')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_9264 = relay.TupleGetItem(func_3341_call(), 0)
call_9265 = relay.TupleGetItem(func_3342_call(), 0)
func_7027_call = mod.get_global_var('func_7027')
func_7028_call = mutated_mod.get_global_var('func_7028')
call_9306 = relay.TupleGetItem(func_7027_call(), 0)
call_9307 = relay.TupleGetItem(func_7028_call(), 0)
output = relay.Tuple([call_9261,call_9264,call_9306,])
output2 = relay.Tuple([call_9262,call_9265,call_9307,])
func_9335 = relay.Function([], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
mutated_mod['func_9335'] = func_9335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mutated_mod.get_global_var('func_9335')
call_9336 = func_9335_call()
output = call_9336
func_9337 = relay.Function([], output)
mutated_mod['func_9337'] = func_9337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_9361 = relay.TupleGetItem(func_4639_call(), 0)
call_9362 = relay.TupleGetItem(func_4640_call(), 0)
output = call_9361
output2 = call_9362
func_9367 = relay.Function([], output)
mod['func_9367'] = func_9367
mod = relay.transform.InferType()(mod)
mutated_mod['func_9367'] = func_9367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9367_call = mutated_mod.get_global_var('func_9367')
call_9368 = func_9367_call()
output = call_9368
func_9369 = relay.Function([], output)
mutated_mod['func_9369'] = func_9369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3496_call = mod.get_global_var('func_3496')
func_3498_call = mutated_mod.get_global_var('func_3498')
call_9376 = relay.TupleGetItem(func_3496_call(), 7)
call_9377 = relay.TupleGetItem(func_3498_call(), 7)
output = call_9376
output2 = call_9377
func_9388 = relay.Function([], output)
mod['func_9388'] = func_9388
mod = relay.transform.InferType()(mod)
mutated_mod['func_9388'] = func_9388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9388_call = mutated_mod.get_global_var('func_9388')
call_9389 = func_9388_call()
output = call_9389
func_9390 = relay.Function([], output)
mutated_mod['func_9390'] = func_9390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_9453 = relay.TupleGetItem(func_2994_call(), 0)
call_9454 = relay.TupleGetItem(func_2996_call(), 0)
func_4986_call = mod.get_global_var('func_4986')
func_4988_call = mutated_mod.get_global_var('func_4988')
var_9456 = relay.var("var_9456", dtype = "float32", shape = (280, 8))#candidate|9456|(280, 8)|var|float32
call_9455 = relay.TupleGetItem(func_4986_call(relay.reshape(var_9456.astype('float32'), [10, 14, 16])), 1)
call_9457 = relay.TupleGetItem(func_4988_call(relay.reshape(var_9456.astype('float32'), [10, 14, 16])), 1)
output = relay.Tuple([call_9453,call_9455,var_9456,])
output2 = relay.Tuple([call_9454,call_9457,var_9456,])
func_9464 = relay.Function([var_9456,], output)
mod['func_9464'] = func_9464
mod = relay.transform.InferType()(mod)
var_9465 = relay.var("var_9465", dtype = "float32", shape = (280, 8))#candidate|9465|(280, 8)|var|float32
output = func_9464(var_9465)
func_9466 = relay.Function([var_9465], output)
mutated_mod['func_9466'] = func_9466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_9471 = relay.TupleGetItem(func_2994_call(), 0)
call_9472 = relay.TupleGetItem(func_2996_call(), 0)
func_6905_call = mod.get_global_var('func_6905')
func_6910_call = mutated_mod.get_global_var('func_6910')
const_9483 = relay.const([5,-7,10,8,-5,4,-9,-1,6,-5,7,5,5,6,-8,5,9,-2,-5,6,5,8,-4,10,-8,-5,7,8,9,5,5,1,-3,2,-3,5,-10,-1,-1,-6,-8,-6,3,8,-8,-9,4,-8,5,2,-10,-6,-10,-5,-2,8,2,-4,7,-6,4,1,-5,2,1,-8,10,1,4,9,-9,-5,-2,-7,-8,8,-8,9,-10,-5,-4,-1,-10,-4,-10,-10,1,-1,2,-6,9,-4,2,2,6,-2,2,-7,-8,7,-6,-7,2,-2,4,-7,-1,-1,8,-5,-3,-7,2,5,8,8,-9,-3,-2,5,4,-10,5,-9,7,7,3,-4,1,5,-3,3,7,-3,2,5,-2,-2,6,-1,-7,2,-6,5,8,-5,4,-1,6,9,5,-6,9,-5,-9,-10,7,-6,-8,10,-4,7,5,-8,3,2,3,5,8,-7,-8,-5,8,-10,6,-4,-5,8,-8,-2,6,-9,2,1,5,8,6,10,5,-2,-10,-1,7,4,8,8,-1,-2,-2,2,-2,3,-6,-2,5,-3,-2,7,-6,7,-10,-9,-4,4,6,7,8,6,5,4,3,2,-2,7,1,-3,10,1,-4,4,-1,-8,1,3,-3,3,-4,1,5,5,3,8,-9,1,-4,-3,-6,-3,4,-2,-5,-3,9,5,2,-1,-8,-10,5,-8,6,3,-2,-8], dtype = "int32")#candidate|9483|(264,)|const|int32
const_9484 = relay.const([-8.621672,-6.363738,8.611919,-3.313477,-9.364626,-1.971495,-7.623627,-1.003224,6.848524,-3.503833,-2.950041,-8.229440,8.620412,1.387999,-5.252423,2.362164,-7.227872,-2.826626,-4.896497,5.664045,1.881880,-8.751940,-2.774153,-8.130776,-2.589694,2.306452,2.363473,4.330118,-7.731911,-5.290723,0.245943,-5.435533,8.683716,-6.332948,6.378403,6.931100,5.977789,-4.772459,-8.753928,0.240551,2.915337,-1.583734,-3.985701,-0.069550,-6.849983,4.693001,-3.275414,6.667862,-0.310855,5.521960,-4.826820,5.189423,7.025922,8.817151,-3.874478,-3.013510,8.093325,-2.479871,-7.581815,-5.888716,8.291518,-8.578618,1.342194,-3.164477,6.196266,0.505831,-3.555941,3.983129,-1.881245,4.087655,9.752538,9.399593,-4.864507,6.402821,-7.101295,-1.801053,3.699191,4.580380,-3.244039,9.296961,1.119445,1.024048,2.361209,6.223045,3.131468,-3.885331,-6.876580,1.412001,4.242456,1.644685,2.407282,-8.396207,7.080485,0.739550,5.801226,6.110889,-1.267737,-1.676295,-8.027569,7.462842,-1.523964,-5.976605,8.259087,-0.789952,-1.975801,-8.594679,6.800584,1.290621,-2.661078,-4.909395,4.233107,2.838999,5.371028,6.000153,6.133277,7.184545,-2.178007,8.733255,-8.147725,-6.001859,0.011458,-1.493271,7.377934,4.524491,-8.394047,1.061443,-9.676112,1.890451,-7.503240,2.638415,-4.500757,-0.199913,-6.374887,-0.753346,7.036797,-0.187612,-8.099542,1.780430,-0.958894,0.282433,-7.641533,-0.603946,5.076077,-6.701443,-8.441319,-0.551283,0.621029,2.980615,-6.489121,-9.476393,-9.744207,-5.795498,0.153067,5.755555,7.938845,-2.556791,7.203829,-7.992335,2.206040,5.123855,-9.957748,-9.806107,-7.121240,2.535808,4.115321,-4.417276,-3.767848,-3.841321,-5.197257,3.996686,8.898911,3.940142,-3.621331,5.590741,9.115523,4.952700,-4.840241,8.033794,3.922083,4.696702,-7.014979,4.686592,2.399067,-8.788327,5.477233,3.722877,7.149208,5.629941,-0.667518,1.546190,1.693830,7.538045,-7.226242,-8.311995,5.396736,9.824060,1.817583,1.411094,-7.044289,-0.479299,2.364570,-0.404918,7.961433,1.493706,2.819056,2.925420,2.474938,-1.912367,8.526985,-9.546209,4.970890,-1.660215,-3.470803,1.343194,8.507970,-8.343072,6.791761,8.406873,-3.774735,-4.785826,-3.388156,5.793321,-9.533793,6.710332,-7.825315,-0.529399,1.933291,4.964158,-6.043238,2.279429,-8.041939,4.242711,-5.855797,-5.509709,7.430182,-7.826180,-3.814750,9.274396,-4.346415,-1.338283,-9.259659,-6.740200,1.326699,1.207282,-9.455355,6.506136,-8.272561,-7.501067,-9.427295,-8.917501,8.764350,5.724378,-5.882400,-2.827372,1.417703,7.609621,0.542491,-1.483154,5.177038,3.656465,-6.354845,7.304410,2.157390,3.729767,-1.588423,5.730371,0.835507,-8.511172,4.805908,-7.402653,2.347590,9.659073,5.694707,-0.997558,9.560709,-4.106882,-2.935684,7.797534,2.908370,7.934908,-3.232489,2.397592,6.313766,8.731520,-8.977599,-1.230049,0.218253,-2.573028,3.234019,-6.212443,-8.031084,-8.660890,-6.410226,-2.792089,-9.077367,9.668005,-2.365544,-3.461101,-7.783069,5.788870,9.320126,7.409722,5.665425,2.371146,-6.404028,8.960082,-3.347518,2.756499,1.754539,-9.574567,-1.625750,-8.055428,-0.828388,-6.292290,-3.404290,3.905784,9.106401,4.411011,0.375217,3.907460,-0.855553,-7.023435,-1.096132,5.793502,-6.382966,-5.037654,0.833362,7.770692,3.128128,6.492010,0.791558,-1.812256,7.583852,7.138357,-0.810508,-8.301058,-1.875221,-2.629310,-0.852501,-6.555881,5.503144,7.062399,-9.984792,4.771764,1.259580,5.014187,6.225632,9.808367,0.178515,8.586525,-8.850103,-3.471655,1.753621,2.860567,-0.588265,-0.228371,-7.403631,7.748207,-2.215565,6.934390,0.732396,4.828827,-4.646351,1.578812,5.980767,0.763122,-9.379722,-2.380813,-8.851202,8.657205,-8.445657,5.583712,-2.598970,4.114235,2.524407,-5.355959,2.550816,9.108404,-5.846608,-5.983678,-1.301237,2.887766,1.633190,-4.461844,-4.888541,8.505224,5.003556,8.737733,2.350544,-0.384385,5.433359,8.123553,-1.161942,-6.654917,8.062261,2.101146,8.324701,-6.639937,-8.323253,-9.350968,-2.914691,1.572625,-8.217648,1.031919,7.791226,-7.784491,-0.775002,-1.103808,0.356770,-4.171936,5.287390,-4.274293,-2.012902,2.006749,6.261336,6.725926,2.129525,2.358794,-4.557475,4.568891,-4.064651,-4.785996,6.942656,-4.472375,-6.584825,7.753196,-9.084712,-3.367796,-8.385615,3.112106,4.848082,-1.693489,-7.004691,6.847273,-4.009034,-5.630300,-8.678032,-7.609961,1.963877,-9.559701,4.540791,0.549454,8.683317,-6.985969,-6.563084,2.573890,6.832200,-5.270976,8.705571,-5.462788,3.663560,6.302038,7.531681,5.992828,-3.506354,-9.088404,-9.479751,2.615213,9.256690,1.008442,9.652679,-2.701214,-4.090625,-3.018812,-5.813939,-4.825302,-9.100080,0.014374,2.127842,-7.001886,4.145870,6.426755,2.293337,3.135659,-9.654852,-4.067073,-0.648639,-8.546022,8.243864,-6.173909,6.669897,0.441774,-6.819362,-5.164110,-2.183629,6.582570,3.337875,8.624092,0.149911,-2.809677,9.798717,-3.510586,5.444256,6.111784,2.782067,-8.319724,-6.836206,-5.676467,-5.759267,-5.735808,-1.058934,-3.300678,-3.264550,-8.916130,4.964908,0.905626,6.360062,-4.039829,4.989789,6.001257,5.230305,7.095567,-4.178978,8.031595,-9.731900,5.425711,6.772427,4.418519,8.326288,-1.770022,-3.646767,8.684256,8.026616,-1.694265,5.868830,7.144307,8.262613,-5.188726,6.619451,-5.625900,6.881251,-5.075610,-1.215610,-0.222174,0.299293,-9.737692,8.923452,6.230389,9.283016,2.583927,9.588722,0.681638,5.545470,-0.670585,0.227767,9.258265,-3.286705,-9.433088,7.022571,-7.973201,7.378127,-8.972670,2.712583,4.702670,5.812109,8.249166,0.583592,7.679929,5.978036,9.524571,-4.974322,3.516477,-6.694466,5.728820,3.307170,-7.738890,-5.952953,1.310976,-2.467804,-1.753452,6.650713,0.165820,6.766742,9.692544,-7.764505,6.869343,6.946607,-9.092191,-3.715157,5.204753,4.785386,-4.994354,-4.796691,3.292048,-2.454128,-7.746781,-8.736023,9.980355,-4.338417,-9.220614,2.022759,-5.289189,-9.248725,7.680678,-1.905237,-6.515553,-2.935406,-8.478285,-2.527168,-3.825091,4.730239,-2.475719,-4.936905,2.511492,7.576859,1.267691,-3.817661,1.213270,-3.863856,3.363528,-8.278328,4.682811,4.640229,0.155922,7.282476,-3.325413,5.516560,-7.929059,-7.460400,-6.197937,9.696359,1.467939,9.907312,9.461843], dtype = "float32")#candidate|9484|(624,)|const|float32
call_9482 = relay.TupleGetItem(func_6905_call(relay.reshape(const_9483.astype('int32'), [2, 11, 12]), relay.reshape(const_9483.astype('int32'), [2, 11, 12]), relay.reshape(const_9484.astype('float32'), [624,]), ), 0)
call_9485 = relay.TupleGetItem(func_6910_call(relay.reshape(const_9483.astype('int32'), [2, 11, 12]), relay.reshape(const_9483.astype('int32'), [2, 11, 12]), relay.reshape(const_9484.astype('float32'), [624,]), ), 0)
uop_9488 = relay.cos(const_9484.astype('float64')) # shape=(624,)
output = relay.Tuple([call_9471,call_9482,const_9483,uop_9488,])
output2 = relay.Tuple([call_9472,call_9485,const_9483,uop_9488,])
func_9498 = relay.Function([], output)
mod['func_9498'] = func_9498
mod = relay.transform.InferType()(mod)
mutated_mod['func_9498'] = func_9498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9498_call = mutated_mod.get_global_var('func_9498')
call_9499 = func_9498_call()
output = call_9499
func_9500 = relay.Function([], output)
mutated_mod['func_9500'] = func_9500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_9501 = relay.TupleGetItem(func_2494_call(), 3)
call_9502 = relay.TupleGetItem(func_2496_call(), 3)
output = relay.Tuple([call_9501,])
output2 = relay.Tuple([call_9502,])
func_9503 = relay.Function([], output)
mod['func_9503'] = func_9503
mod = relay.transform.InferType()(mod)
output = func_9503()
func_9504 = relay.Function([], output)
mutated_mod['func_9504'] = func_9504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9031_call = mod.get_global_var('func_9031')
func_9033_call = mutated_mod.get_global_var('func_9033')
call_9590 = relay.TupleGetItem(func_9031_call(), 0)
call_9591 = relay.TupleGetItem(func_9033_call(), 0)
output = call_9590
output2 = call_9591
func_9602 = relay.Function([], output)
mod['func_9602'] = func_9602
mod = relay.transform.InferType()(mod)
output = func_9602()
func_9603 = relay.Function([], output)
mutated_mod['func_9603'] = func_9603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5252_call = mod.get_global_var('func_5252')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_9642 = func_5252_call()
call_9643 = func_5252_call()
output = relay.Tuple([call_9642,])
output2 = relay.Tuple([call_9643,])
func_9671 = relay.Function([], output)
mod['func_9671'] = func_9671
mod = relay.transform.InferType()(mod)
mutated_mod['func_9671'] = func_9671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9671_call = mutated_mod.get_global_var('func_9671')
call_9672 = func_9671_call()
output = call_9672
func_9673 = relay.Function([], output)
mutated_mod['func_9673'] = func_9673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mod.get_global_var('func_9335')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_9686 = relay.TupleGetItem(func_9335_call(), 0)
call_9687 = relay.TupleGetItem(func_9337_call(), 0)
output = call_9686
output2 = call_9687
func_9690 = relay.Function([], output)
mod['func_9690'] = func_9690
mod = relay.transform.InferType()(mod)
mutated_mod['func_9690'] = func_9690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9690_call = mutated_mod.get_global_var('func_9690')
call_9691 = func_9690_call()
output = call_9691
func_9692 = relay.Function([], output)
mutated_mod['func_9692'] = func_9692
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9742 = relay.var("var_9742", dtype = "uint16", shape = (6, 12, 4))#candidate|9742|(6, 12, 4)|var|uint16
var_9743 = relay.var("var_9743", dtype = "uint16", shape = (6, 12, 4))#candidate|9743|(6, 12, 4)|var|uint16
bop_9744 = relay.less(var_9742.astype('bool'), relay.reshape(var_9743.astype('bool'), relay.shape_of(var_9742))) # shape=(6, 12, 4)
bop_9749 = relay.maximum(var_9742.astype('int32'), relay.reshape(var_9743.astype('int32'), relay.shape_of(var_9742))) # shape=(6, 12, 4)
output = relay.Tuple([bop_9744,bop_9749,])
output2 = relay.Tuple([bop_9744,bop_9749,])
func_9758 = relay.Function([var_9742,var_9743,], output)
mod['func_9758'] = func_9758
mod = relay.transform.InferType()(mod)
mutated_mod['func_9758'] = func_9758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9758_call = mutated_mod.get_global_var('func_9758')
var_9760 = relay.var("var_9760", dtype = "uint16", shape = (6, 12, 4))#candidate|9760|(6, 12, 4)|var|uint16
var_9761 = relay.var("var_9761", dtype = "uint16", shape = (6, 12, 4))#candidate|9761|(6, 12, 4)|var|uint16
call_9759 = func_9758_call(var_9760,var_9761,)
output = call_9759
func_9762 = relay.Function([var_9760,var_9761,], output)
mutated_mod['func_9762'] = func_9762
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9812 = relay.const([[[4.522175,3.605032,6.891424,-3.182151,9.480728,7.014095,3.872325,8.777570,0.879795,-5.623807,-2.960398,-7.280949],[-0.785433,-6.670186,-3.196370,-8.011872,5.839474,-8.396021,6.840592,2.462982,-3.707926,3.504266,3.748175,-5.538669],[6.521315,-5.181251,5.504974,-2.462260,0.436251,6.461418,2.148305,3.257947,3.565338,6.507315,-5.445326,7.909573],[-4.599991,2.698267,-7.375915,-6.838461,-0.031305,5.714107,9.291054,0.407546,5.761864,1.554079,-2.168623,7.702801],[-2.945545,9.864433,-3.397994,-2.673316,3.395298,-3.334508,6.579678,6.425181,-1.956063,-5.913572,-5.043600,-6.786054],[-4.770696,-5.378285,7.079246,-7.592137,9.093991,-8.519696,2.830668,-0.659589,-4.087581,-9.492806,3.963479,-5.546761],[-4.108112,1.988735,-0.555810,-1.762182,1.295776,-3.930015,9.864978,3.586055,-0.890276,-1.983478,-3.727024,-4.090551],[7.870131,-9.954561,-4.591770,-6.639488,8.123171,3.851934,-5.520636,-4.624186,5.747500,-7.331303,-7.436671,4.353123]],[[7.953099,-7.254863,-6.227188,4.226378,4.057137,-9.628764,-3.891819,-3.798057,-9.831027,5.537992,-3.336397,2.323088],[-4.822968,-5.030612,1.566915,5.389578,9.549786,-2.338312,-4.777590,4.042782,3.838001,6.665019,8.790590,-8.276815],[-1.725944,-1.081970,5.208545,-2.610302,7.536916,-4.128484,-4.141575,3.558263,4.687494,9.834964,5.460899,3.771888],[-7.805082,-2.897855,7.819013,3.560489,5.494911,-8.332304,7.793325,-7.788521,6.306300,4.195696,9.798287,3.848208],[-0.315486,-5.409377,4.322836,8.732067,0.232029,1.184194,-1.059320,-9.727979,-2.454298,-1.136310,9.232644,-7.666960],[-1.594563,-8.662852,6.821968,-4.781707,-5.880794,1.851360,4.382663,9.096716,7.710584,2.179228,4.762267,8.114651],[-6.236009,-4.806560,-1.816709,-4.084646,-3.794569,-3.877117,-1.773147,-9.820396,-3.672234,-2.716163,-7.194425,-9.384401],[0.427445,8.752646,5.547725,-7.101418,-0.519610,6.815864,-2.726802,9.342024,-8.975143,-2.534639,8.472186,6.179680]],[[-0.441644,4.822984,3.512500,-1.841126,3.431102,1.388486,-9.415326,-3.957537,-7.828406,-7.527607,3.359864,-3.548235],[4.318267,-3.866526,9.872297,-2.257897,5.766125,-4.182960,5.569438,2.328071,-6.252099,0.795292,0.716429,1.076231],[3.722386,-6.294498,-7.950950,-3.236559,3.410695,-2.692154,-5.489942,-8.980903,-2.790329,-6.164199,-2.342515,-4.536750],[7.954008,3.834876,5.325907,-7.684096,-8.928456,6.420112,6.540563,7.301896,-7.283290,6.221031,-1.450085,-8.286541],[-0.689678,9.972948,2.289569,8.605186,9.781285,9.482960,-8.286456,-9.595841,-6.987689,2.598176,2.644913,-0.323919],[-8.447306,6.475891,3.955527,8.544001,-8.825531,-1.259897,-2.046747,-3.189952,9.525667,-7.614744,-9.674597,-1.713757],[-6.880822,-9.515998,-6.463547,4.118640,9.191551,-2.434991,-9.845480,-2.865830,-2.886188,-2.989984,6.368820,-1.984767],[-5.218756,-5.389641,7.559505,6.615459,-2.175107,-2.561420,-4.987999,9.163962,-7.716896,9.066518,7.165677,6.182960]],[[-2.304929,-7.722766,5.866580,-7.907537,5.429456,-1.398553,-2.854302,-2.618876,4.829999,2.437841,-0.338451,5.822502],[-5.862688,2.527140,9.725850,0.031742,4.368226,9.061697,1.300687,-7.699292,-5.764677,3.093348,6.384330,6.649388],[-8.423700,-6.892139,4.178198,0.290342,-5.275935,9.885599,-4.072025,-9.102868,-2.793016,-5.612346,0.224875,-2.117426],[9.749419,-1.514201,0.529020,3.835006,9.093829,-0.965845,-8.295128,-6.113385,-5.785832,-3.828280,2.655751,-8.613771],[-9.961048,8.613431,-0.747568,2.073011,3.423922,-9.424848,5.149997,7.518603,3.890257,8.668225,5.749302,2.360089],[3.595048,-7.527765,-4.813275,-2.324117,9.195333,-0.605286,0.820798,4.845041,-4.682399,8.675789,-4.052341,-5.877757],[-5.713429,9.152091,7.933342,2.843922,-4.794542,8.878418,7.334447,1.682600,9.391057,-3.137475,0.684196,-0.966362],[3.964503,8.448542,-3.554257,4.013091,5.704600,-6.297140,3.231522,9.281500,-1.945425,-6.439710,-7.613726,-7.586736]],[[-8.122270,-2.910636,6.732443,1.769528,-5.318089,-8.606078,-9.958512,0.240106,-1.615595,-7.617528,3.439471,3.614886],[1.270768,4.228760,8.883862,9.574006,-6.076805,8.358324,-1.344960,-7.631037,5.268584,7.266782,2.407853,8.267128],[4.245655,5.312585,1.346922,-1.641957,9.524049,-4.815483,6.357788,-3.936599,2.055754,7.179405,-0.575491,-9.121111],[-1.100281,1.284511,-9.951360,4.550539,-5.352100,-5.988541,8.459764,-1.566860,6.279005,0.878182,4.237492,-1.339547],[1.507812,-6.128352,-2.768497,1.332184,1.998000,-3.055973,9.484070,4.119664,-2.130504,8.162481,-1.037838,-4.437277],[-0.270961,-8.473777,4.529217,-9.616656,0.352696,-9.132522,0.982451,-7.818727,-0.491265,-4.747843,0.547660,-7.987369],[-8.136996,1.399599,7.023108,-1.437271,-4.071412,3.882774,7.379624,-3.373266,2.813708,-9.544875,1.932007,4.895067],[8.706687,3.362241,1.309467,3.039279,-5.689659,-3.943005,-7.662913,3.381342,8.827005,5.857755,4.852334,7.513850]],[[-6.456217,1.036194,2.509712,-3.138363,9.392393,9.205757,8.925609,-0.441059,6.090842,5.761097,1.537466,-4.012100],[-2.131008,5.008186,-7.597063,-1.740498,2.520051,-6.357395,-2.267653,2.986587,-4.398627,-6.050079,5.634886,0.606843],[2.098279,3.395220,-3.964353,3.088161,7.740812,-6.066750,-8.993485,-3.473043,-6.079523,-9.377971,7.592472,-6.867885],[-4.417869,8.642527,3.267843,-1.613615,-3.225805,4.981446,-5.571759,3.895861,-0.234817,3.456267,-1.696484,-7.527135],[-3.855408,2.353002,-0.799838,4.563626,-8.843810,9.160780,-0.036529,-2.514478,6.612951,8.754157,-6.332373,6.896958],[-2.661824,3.853393,-2.744411,2.001637,-7.438943,1.222353,5.181557,9.192001,0.524061,5.866175,1.011904,-9.124724],[-4.630743,-4.274132,-0.453587,6.114032,-9.718121,2.422522,-7.614511,9.721612,3.087137,4.218786,6.655535,-0.074612],[4.915366,-8.472110,3.845993,3.427933,-4.915202,0.152120,0.967340,2.644803,2.762247,4.673645,-7.792594,4.135106]]], dtype = "float32")#candidate|9812|(6, 8, 12)|const|float32
const_9813 = relay.const([[[-1.375480,2.990561,6.279392,-3.464727,4.937163,1.998181,2.989202,-5.760737,-3.968282,0.323647,4.701771,6.997072],[-5.443056,7.882607,0.529602,4.379968,-7.178542,9.166988,1.611531,3.141103,6.496646,-2.934442,8.369772,3.609891],[-1.257852,4.168574,-1.072869,-1.650630,-0.570096,-0.374556,-6.045878,5.611752,-5.972413,5.498597,9.903521,2.764926],[9.750031,7.387792,-5.827086,-4.587423,-4.822274,7.394926,-9.926020,6.687301,4.422084,0.525979,6.593166,-7.985221],[1.064814,-0.841120,7.890827,1.466653,4.045802,7.660213,-9.066471,-0.794121,1.237833,1.672849,-2.732065,8.046712],[-0.719206,0.933467,1.305215,4.004084,9.747376,6.297477,3.755910,7.256211,-6.928451,4.857308,3.648059,3.854085],[5.497921,-3.321926,1.596920,9.387971,-5.535000,-6.724140,0.456553,-7.828315,6.246959,8.399521,2.500264,7.247535],[8.216788,-6.574731,-6.364735,6.263303,-4.597617,8.955134,8.967959,8.835075,-5.854609,-1.242503,3.575907,-9.141210]],[[-5.797983,-6.564671,9.757813,6.817126,-4.346949,2.478108,5.830191,-6.167529,-5.644999,-0.208344,-0.894843,-9.298521],[7.202050,-2.888634,3.880635,2.867021,-9.896188,4.286236,2.350592,-1.807068,-1.841823,-8.838520,0.184695,5.032325],[6.747913,6.060043,2.434349,-5.857189,-7.290719,-6.214096,6.924757,-6.707959,5.695092,0.569055,-0.807702,-5.887558],[2.958325,5.094793,7.595428,0.002553,-0.972999,-5.883774,-7.523717,-5.838034,-2.247905,-0.773102,-1.280972,0.628123],[3.488599,-1.139946,6.184248,-9.902625,2.598453,8.765838,2.566775,7.362507,7.138156,8.340616,-5.439787,4.264632],[-1.846550,4.381411,-9.074378,-3.784589,2.742235,0.957591,3.562754,-8.343476,6.295236,3.928774,-1.943391,-3.333657],[8.466362,6.728220,0.838592,-5.066759,-4.335755,-9.499576,-9.002481,-4.119417,5.400422,-5.674390,-7.883137,-4.611266],[-3.982424,-6.679489,-7.498684,9.877524,-4.247405,-6.308122,2.997983,-7.230534,-0.414139,-2.220564,5.626069,-2.624564]],[[-1.961339,-3.393111,6.527704,2.953362,-7.946365,-4.446206,-8.366497,-8.563065,-1.278014,7.798661,4.947989,-5.655787],[-4.061753,2.318948,7.473104,6.448779,-6.317468,-2.246134,-4.420286,-6.984014,8.244732,2.658539,-0.332886,0.399231],[-5.542757,-6.314482,-1.554773,1.698572,5.903032,-0.123862,7.180381,-5.628631,0.147788,7.602746,-9.022397,5.401361],[3.898430,-4.204061,-4.942740,-8.155056,-6.587812,9.820806,3.964240,9.098754,2.673891,-1.888205,2.419030,-3.096608],[0.161815,-3.207759,8.843377,-1.125137,8.037845,-5.908781,-0.677729,-3.801316,4.390855,4.167471,9.384593,7.055056],[-8.946100,8.048670,9.157473,1.156989,2.433410,-7.167507,2.548102,2.208297,1.267601,-5.951368,4.448922,-7.869128],[-5.916380,0.085211,6.945377,-2.772584,-9.460790,8.552160,-5.528120,7.832148,7.019147,-2.705364,-1.997335,0.996158],[-1.990080,1.218124,-5.782826,-6.315627,1.621533,-7.794744,8.664051,-9.339187,-4.470085,4.109782,-9.823206,0.496521]],[[-2.223644,-2.710264,4.168427,1.688110,-5.190989,1.733467,-3.463077,0.821297,-9.827208,-9.648469,5.153345,8.700569],[8.017053,-3.767147,2.416158,0.562683,6.572998,-3.698978,9.433648,-4.074713,-5.548660,-6.961968,-9.010468,-5.636014],[-3.622360,-0.410886,-1.496046,8.989015,-6.524527,3.217339,3.883393,3.982056,7.815156,-7.928399,6.518134,-2.649564],[-3.159823,3.429717,-3.236752,4.289655,-2.158070,-2.792978,-1.525055,-4.970335,9.895233,-1.653971,-9.629622,-3.653840],[-7.373736,-0.042564,5.147737,8.162635,-9.285325,-4.423286,3.515938,2.877826,1.995189,-0.103539,0.887084,-0.711523],[-7.200217,-8.498228,1.872200,-3.696866,0.808945,5.805256,5.060014,-1.979572,5.689763,1.176901,4.427007,0.721656],[-0.986819,-8.321820,-7.873306,1.742434,4.565631,-6.311143,-0.270177,-3.672798,0.295560,-5.860335,4.352890,-4.490397],[-3.413876,9.988921,-8.289141,-8.351269,-7.004460,6.829066,-7.309299,8.521819,-2.813624,-2.730734,3.762994,-3.794794]],[[-3.136328,7.135536,4.506760,4.067948,6.332784,9.149913,8.751036,1.235322,-4.176952,-9.532280,1.590537,0.570833],[4.931596,-1.946822,-5.772063,-5.814955,6.931171,-0.570759,4.329696,-7.865697,-4.004389,3.066399,-8.224931,8.767202],[0.104581,1.991765,-5.725175,-4.286449,-8.194477,-4.592776,6.264760,7.563914,-8.382529,6.583759,6.092345,0.448135],[-6.643810,9.991230,0.083126,0.971142,2.462012,4.263182,5.765330,1.664504,-5.488987,3.068915,-6.157519,-9.954917],[-7.195302,9.510141,-5.693300,-3.383376,6.304683,7.799835,-2.975323,5.650314,4.187181,0.110105,-3.935934,-4.762119],[-2.845239,-4.347798,-0.118233,-8.845742,-7.144084,7.123969,-1.439742,0.214272,2.306734,-4.680805,-7.818941,1.945384],[-7.399719,-1.454248,-0.647216,7.263232,-1.990425,2.690018,-3.107707,-3.380176,0.830895,1.258849,7.799363,3.699357],[2.560359,-5.814819,0.530373,5.961281,2.663384,-7.187974,-5.254880,-2.088103,5.065755,-2.056220,5.028116,4.453753]],[[-6.151351,-3.023463,9.674430,-8.273901,4.964120,-3.277508,5.218622,-1.502033,-9.735711,-9.502282,-0.983610,9.809393],[-2.421686,-4.696867,-1.184542,1.511249,-1.771864,-3.602451,8.881147,8.688550,-2.395565,-5.690984,8.488693,-7.956646],[1.660599,4.022935,3.584052,-0.570234,-5.071850,-5.979074,-9.385227,2.982182,2.964267,-6.087422,-0.472492,-7.956762],[-8.236283,-7.393558,8.545712,7.998138,5.544175,5.722064,2.709778,5.109761,-8.410104,0.231014,9.939363,5.308057],[-3.322725,0.770639,3.582870,5.885079,-4.041370,-3.606120,-3.468990,8.771349,-1.353394,5.631796,-9.033525,6.308433],[-0.851032,9.586981,4.441455,-4.541959,-9.218037,-9.958126,2.406893,8.060194,-1.070543,-0.432053,7.169341,-8.682063],[-1.794728,-2.247139,-6.198302,2.643580,-2.024893,-1.052780,1.553665,7.795998,3.259832,-3.955196,-0.174654,-9.592262],[3.751604,7.416026,-7.593470,-9.198345,7.099793,3.023417,-0.767903,-0.302042,7.936151,-6.108695,-9.594213,8.353862]]], dtype = "float32")#candidate|9813|(6, 8, 12)|const|float32
bop_9814 = relay.less(const_9812.astype('bool'), relay.reshape(const_9813.astype('bool'), relay.shape_of(const_9812))) # shape=(6, 8, 12)
func_8090_call = mod.get_global_var('func_8090')
func_8092_call = mutated_mod.get_global_var('func_8092')
call_9818 = relay.TupleGetItem(func_8090_call(), 1)
call_9819 = relay.TupleGetItem(func_8092_call(), 1)
func_3634_call = mod.get_global_var('func_3634')
func_3636_call = mutated_mod.get_global_var('func_3636')
call_9821 = relay.TupleGetItem(func_3634_call(), 2)
call_9822 = relay.TupleGetItem(func_3636_call(), 2)
output = relay.Tuple([bop_9814,call_9818,call_9821,])
output2 = relay.Tuple([bop_9814,call_9819,call_9822,])
func_9836 = relay.Function([], output)
mod['func_9836'] = func_9836
mod = relay.transform.InferType()(mod)
mutated_mod['func_9836'] = func_9836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9836_call = mutated_mod.get_global_var('func_9836')
call_9837 = func_9836_call()
output = call_9837
func_9838 = relay.Function([], output)
mutated_mod['func_9838'] = func_9838
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9848 = relay.const([[[-0.995321,3.819691,6.391635,2.673958,-0.328378,-4.223059,5.237256,-6.823291,1.226034,0.632378,-5.848698,-1.814329,-8.863540,-7.430372],[1.864454,5.723296,7.437987,-4.643380,-2.961783,-3.244162,-5.326864,3.351092,0.465858,-2.057173,-3.639007,2.907981,1.468302,-4.600720],[-5.990306,1.582740,-6.340717,-1.232180,4.937441,-4.394989,-5.818913,-1.064753,-1.784811,-6.033241,1.405748,-3.671763,-4.804247,7.555806],[3.765005,3.941584,-3.690817,2.828000,6.448046,-2.019405,-7.333359,4.843738,8.413357,1.180703,3.421986,-3.502586,6.765428,2.300293],[-7.785270,6.736087,-6.563077,-8.718462,2.482567,-5.969920,0.890489,-0.769068,8.045067,-7.177664,5.444742,-6.899811,1.206352,-0.871942],[2.804920,-9.289659,-7.492486,7.504064,-5.054076,0.981517,4.942479,-5.400831,-4.855662,0.273695,-3.184743,-1.260312,4.363108,5.406833]],[[1.355973,8.015518,3.208313,6.141171,-0.629948,-6.449918,-4.219614,-8.239978,7.563312,-9.674131,2.625648,-0.523553,1.027731,-2.016191],[8.654097,3.544826,6.563688,-0.730504,-1.661358,-2.789797,-7.524080,3.448572,-5.412756,5.142282,-4.950250,4.372210,6.454579,-5.046179],[-4.740910,8.439654,-6.268885,8.380062,-4.862526,-1.256245,3.018603,4.548403,2.772791,-6.266698,-4.160240,-9.068524,6.413940,9.385422],[8.159784,0.227275,-1.791494,4.236204,1.172896,-6.480714,-8.981633,-7.898836,7.248193,-0.148199,-3.746596,-0.316698,-8.581168,1.032433],[-1.254369,-4.244825,-0.981877,3.235287,-8.807205,7.123544,0.056498,0.434314,-1.059962,3.853603,7.292883,7.988380,-4.221645,5.024298],[-1.310328,-9.618630,2.580113,-7.644695,-8.338583,-1.705594,-9.963910,-5.121245,4.878628,-9.602907,9.619529,7.916717,7.018032,-7.570669]],[[-6.935950,-1.890641,3.141727,9.502963,4.074970,-9.109659,2.673937,-5.528317,1.301252,-4.650523,6.791639,-8.224534,-6.369306,6.602670],[-3.969974,-4.065675,3.995808,1.597312,1.654728,1.771087,-2.897770,2.066756,-1.810894,-4.868806,-8.679539,-3.909595,5.938091,4.543367],[-5.156487,9.005953,-3.289032,8.496796,-9.462568,-9.598999,4.202802,-9.001302,-3.568325,-7.384285,5.838843,-7.830895,6.080931,2.569222],[9.317046,-2.656830,-3.460654,7.150972,4.696636,-6.949553,9.633170,-2.277272,5.699248,9.690433,-0.525820,-0.703243,-7.713384,4.739300],[-9.448605,-3.839859,0.284613,4.387557,-8.762798,2.294283,-1.266182,9.854979,-4.432538,-8.140076,-6.050983,4.500397,4.936284,-0.966772],[-2.516961,5.975300,0.763333,3.375373,4.861566,-2.826390,8.641072,0.886819,6.945905,1.410091,-2.308793,2.668621,6.958239,3.180656]],[[0.433994,-4.571905,-4.421651,-2.378763,3.303745,-6.573040,-8.630205,-4.462016,-0.806814,4.980219,-6.566991,-1.008913,7.076597,4.132680],[-1.477020,3.987585,8.595350,-3.859662,-0.492788,6.085945,-3.667119,-3.931452,-9.767259,-5.936697,-4.056626,-2.705730,-9.980560,-1.695537],[4.181426,6.070336,-3.351827,9.828724,-5.652751,7.673733,-5.105481,6.798571,0.603797,2.855805,-8.536182,-5.174116,-1.999713,-4.913348],[7.100788,-2.629704,-3.986736,9.688630,-9.715488,-6.567172,-6.440360,0.361459,-0.028043,7.461440,-5.402916,2.134677,-4.515870,-0.115867],[4.108936,9.550174,2.690220,4.767881,1.713617,-1.365270,3.606765,0.297938,0.034865,-9.478186,2.542681,0.633556,-7.093582,-2.233243],[-6.789198,0.033163,9.909315,9.443664,-1.078021,1.415139,5.715515,-3.522907,-4.873984,-8.347794,-6.801796,-1.366329,-8.577948,-3.252919]],[[-5.873990,8.652419,5.556651,-7.254779,0.423606,4.379441,-9.941321,-7.662668,-0.162102,-2.370870,-7.465140,-5.989952,2.673195,-7.610615],[-2.426182,4.852076,9.959040,-9.331783,1.304172,-1.826686,-0.005523,7.927432,-6.386703,-6.854816,-0.712831,0.283434,3.904933,5.893069],[-0.091129,-8.449325,-4.476120,-2.739682,-0.181625,-7.503198,8.301549,-2.414457,-8.171634,4.940916,9.183086,-5.333711,-5.745058,-0.670661],[1.328210,9.204208,7.224128,2.995107,2.755949,-2.817992,-2.373073,0.528975,3.693161,3.059098,2.533882,-0.912573,-8.395247,-7.866235],[-8.286402,-9.902229,1.048809,-4.669313,8.199237,-8.102670,2.942459,-4.636012,-0.483022,9.284579,3.500428,8.953559,0.507297,-9.072261],[-4.704076,9.255522,8.373991,3.695085,7.271768,-2.409141,1.434181,2.065973,5.667231,-6.174103,9.504882,4.840147,-4.509053,-3.819226]],[[-8.637103,5.132833,7.894522,4.932443,-2.184897,4.026925,-4.916791,-9.355102,5.435087,-3.422541,6.651228,-4.300457,3.992779,2.339443],[-6.804362,7.858928,-1.745015,-6.381398,4.976767,2.169898,-3.887865,4.741876,-7.751508,-8.694556,5.081591,-9.278291,9.243197,-1.105835],[-9.168805,-3.671130,2.508456,3.060052,-6.443481,2.089423,4.739477,7.696595,-6.534344,3.827355,-9.952628,-9.742224,-2.675044,-6.036436],[0.725455,-1.527754,-8.736778,-8.662099,3.652484,-8.396078,9.015950,4.628127,-9.352264,-5.698075,-4.697263,3.649763,9.926842,-7.899785],[-0.408950,1.921938,2.736077,0.702359,-0.054784,7.122095,9.748642,6.679030,-9.191357,1.581859,2.338260,3.415803,9.864752,-8.157579],[-6.364881,1.035991,5.094945,-9.221716,-0.896511,2.675999,9.954439,-0.217285,-5.373649,-3.189646,5.323680,9.197030,1.484128,-1.583795]],[[1.558594,-4.000819,7.203728,-0.901847,-1.957720,-1.187480,-3.636506,-0.501753,-4.468120,-1.297047,-6.570033,8.881272,-3.930166,3.166065],[3.046563,2.051469,-6.197719,-8.196078,6.047373,9.043993,0.339489,-3.738892,8.601809,-9.507206,-2.430338,-1.286568,2.813739,-1.707054],[-9.721622,3.264101,8.991074,-2.066176,-3.946131,4.228451,0.388897,-4.570097,-4.631473,-6.758681,7.457885,-3.197932,5.512649,-0.949721],[-9.300059,-7.567507,-3.828866,1.193466,-0.295485,-0.741324,-7.162392,-2.138099,-6.953065,3.964679,-2.545714,-8.761622,-3.408477,5.459229],[6.379573,-3.366864,-3.213167,-7.115039,-8.703609,-7.371997,7.919772,-1.968382,-3.837045,8.096960,8.589101,-0.144659,-1.904414,5.288844],[5.902420,-9.221274,-2.166948,-5.901767,8.379687,-6.338571,-2.365581,0.969708,3.159144,-2.105158,-0.052256,-0.224553,-1.791363,0.984250]],[[7.332054,5.995688,0.782232,3.354477,-4.601341,-9.360780,-5.036632,6.281092,9.284952,-2.929595,-5.127174,0.972307,-9.138774,-9.515989],[-3.638301,5.691733,-4.999082,-5.641633,-9.883644,-9.773207,6.909356,-4.524264,0.901906,2.643084,-5.886588,2.604315,-1.105371,-0.159652],[-6.310478,8.151778,-5.675076,-7.147555,8.780545,1.251008,-5.580209,-7.643052,-5.929570,5.892729,-2.789780,5.684559,-3.267845,-7.375467],[1.179034,4.149726,1.280044,-1.778935,6.417181,7.181196,6.246195,-0.596661,-9.011774,8.887659,2.200061,-2.091081,7.780168,7.122013],[-0.920340,-1.442402,-1.414075,6.451164,-8.558361,8.061314,-6.611478,-7.761734,5.924253,3.802371,0.669930,0.778078,5.947728,3.308944],[0.376438,-5.526748,-3.050217,6.132127,-9.393609,-6.294080,-6.543467,-9.840802,-5.167478,-8.817071,0.922684,9.042630,-2.995092,5.515664]],[[-3.062267,3.733363,5.382414,6.777054,-6.418122,-5.024135,6.610512,-9.452279,6.365477,-0.876289,4.012993,1.425589,-3.204212,-5.389569],[6.663506,-8.742541,-6.694285,0.140874,3.914511,3.904575,1.099089,-4.623586,-6.313545,-4.996941,8.767965,-6.148757,4.823673,8.029709],[-6.365111,5.964462,-1.080656,-6.964651,2.446488,-7.646543,-2.206434,-4.741878,-4.249684,7.635362,2.723461,-0.005459,-1.758521,-2.416416],[-9.729877,-5.555545,2.872624,6.131149,3.001806,-4.312566,1.112136,-2.746238,-9.231382,-2.117204,1.754252,6.218701,8.361304,-2.442529],[-7.160009,-6.568239,-1.990533,-8.121949,-0.916918,1.454202,6.154905,-9.142858,5.258542,-5.551837,0.299771,-6.131902,-9.775401,-4.744973],[4.282618,-0.355821,3.130766,-5.319431,8.180400,8.684939,-9.848794,5.774177,-2.413271,9.169066,-7.463097,9.136702,-6.234008,8.959199]],[[8.244160,-3.016259,-2.271995,2.480341,3.209652,0.788152,-6.281680,-7.669167,-8.045909,-9.596319,4.910328,-0.306933,6.496264,-9.654104],[0.416607,3.273189,2.520754,6.697398,-4.270527,9.368183,-3.810980,-9.125468,5.814554,-1.064545,-8.063296,-3.316545,-1.197125,-1.565664],[-2.008648,7.849665,-3.248870,-1.450396,-9.232359,6.341829,-4.737584,6.441803,2.707080,3.391127,-3.211146,-1.027741,-4.710612,8.237429],[1.795132,6.542094,-5.803588,1.414520,1.056066,-9.412278,6.114262,-8.245571,-3.903711,9.213442,1.453883,-0.483086,-9.113404,-7.558016],[1.044847,5.113323,5.122700,-8.756703,7.108733,-9.270032,8.426538,-7.277946,-4.395549,1.185623,-3.291814,4.943096,1.062306,-1.357069],[-4.260117,6.084815,-3.537767,8.174262,6.101339,1.604679,3.001391,0.588424,-6.201639,-8.530091,-9.848066,3.391403,-8.286802,-9.646152]],[[-7.925137,4.933610,0.590342,-3.710769,1.805485,-1.697632,1.981975,8.115023,5.848390,7.082447,-8.977670,7.910379,2.946703,-7.411432],[9.825957,-0.522898,5.919826,-6.514917,-9.856478,-2.550080,-8.859444,-4.283801,-3.932261,2.426709,-1.374932,3.879840,-9.258897,7.822609],[6.846457,7.292673,-3.432824,-9.530013,3.208115,-6.308058,8.081041,2.031252,5.414723,2.713223,1.603743,-5.722080,0.928737,-1.801325],[-3.095219,-5.798394,2.703721,-0.118261,5.294965,1.447799,1.505220,-5.636227,-7.992209,0.243887,9.515025,8.374177,3.704826,-0.369322],[8.298696,-9.814323,-0.892065,4.514753,-4.030754,2.402674,-6.213466,-8.023766,-1.978156,-0.819913,-7.105262,5.614452,-9.315754,-2.447524],[-3.191675,2.025000,1.003178,7.762783,-2.418578,-5.833768,-1.782099,-3.929459,-6.847112,-4.822038,0.442498,-6.929854,-4.770071,7.950305]]], dtype = "float64")#candidate|9848|(11, 6, 14)|const|float64
uop_9849 = relay.acos(const_9848.astype('float64')) # shape=(11, 6, 14)
output = uop_9849
output2 = uop_9849
func_9854 = relay.Function([], output)
mod['func_9854'] = func_9854
mod = relay.transform.InferType()(mod)
output = func_9854()
func_9855 = relay.Function([], output)
mutated_mod['func_9855'] = func_9855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mod.get_global_var('func_3712')
func_3714_call = mutated_mod.get_global_var('func_3714')
call_9856 = relay.TupleGetItem(func_3712_call(), 0)
call_9857 = relay.TupleGetItem(func_3714_call(), 0)
output = call_9856
output2 = call_9857
func_9861 = relay.Function([], output)
mod['func_9861'] = func_9861
mod = relay.transform.InferType()(mod)
mutated_mod['func_9861'] = func_9861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9861_call = mutated_mod.get_global_var('func_9861')
call_9862 = func_9861_call()
output = call_9862
func_9863 = relay.Function([], output)
mutated_mod['func_9863'] = func_9863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9836_call = mod.get_global_var('func_9836')
func_9838_call = mutated_mod.get_global_var('func_9838')
call_9918 = relay.TupleGetItem(func_9836_call(), 1)
call_9919 = relay.TupleGetItem(func_9838_call(), 1)
output = call_9918
output2 = call_9919
func_9930 = relay.Function([], output)
mod['func_9930'] = func_9930
mod = relay.transform.InferType()(mod)
output = func_9930()
func_9931 = relay.Function([], output)
mutated_mod['func_9931'] = func_9931
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9932 = relay.const(2, dtype = "int16")#candidate|9932|()|const|int16
var_9933 = relay.var("var_9933", dtype = "int16", shape = (4, 7, 4))#candidate|9933|(4, 7, 4)|var|int16
bop_9934 = relay.right_shift(const_9932.astype('int16'), var_9933.astype('int16')) # shape=(4, 7, 4)
func_8314_call = mod.get_global_var('func_8314')
func_8316_call = mutated_mod.get_global_var('func_8316')
call_9940 = relay.TupleGetItem(func_8314_call(), 1)
call_9941 = relay.TupleGetItem(func_8316_call(), 1)
func_9120_call = mod.get_global_var('func_9120')
func_9122_call = mutated_mod.get_global_var('func_9122')
var_9948 = relay.var("var_9948", dtype = "int8", shape = (567,))#candidate|9948|(567,)|var|int8
call_9947 = relay.TupleGetItem(func_9120_call(relay.reshape(var_9948.astype('int8'), [567,])), 2)
call_9949 = relay.TupleGetItem(func_9122_call(relay.reshape(var_9948.astype('int8'), [567,])), 2)
func_7017_call = mod.get_global_var('func_7017')
func_7018_call = mutated_mod.get_global_var('func_7018')
call_9956 = relay.TupleGetItem(func_7017_call(), 0)
call_9957 = relay.TupleGetItem(func_7018_call(), 0)
func_3265_call = mod.get_global_var('func_3265')
func_3268_call = mutated_mod.get_global_var('func_3268')
const_9959 = relay.const([-0.777194,5.860242,8.269675,-1.701836,1.936482,6.039520,8.155909,9.203556,-7.156721,7.798440,9.070666,-5.309161,-4.524693,7.724642,-6.862784,7.039332,-9.372773,7.959213,2.870418,1.782052,-2.015934,-1.573629,-9.021730,4.884540,2.072494,-1.317358,1.761329,-8.325366,6.599487,6.319245,-2.499853,-1.137277,3.144454,-7.706146,6.683503,-7.151341,-1.150501,8.880402,-5.338561,0.489504,-0.697808,-2.415959,4.974703,8.822162,-4.746366,-8.361966,8.996112,5.165734,-1.408076,3.739668,2.114237,-2.789827,3.509480,-9.554194,-6.913427,2.160282,1.962270,-1.861056,5.254452,8.124491,5.742840,-2.463174,-4.098690,8.352272,3.454598,-1.177300,-8.294582,-0.346637,4.759212,7.915407,1.515150,-5.640948,-6.542188,8.203893,-3.692206,3.415461,-8.483146,-9.631995,1.393537,0.358926,-7.724673,-0.824966,-6.591712,-4.121636,8.465678,-0.598500,5.827860,-4.605727,2.107565,6.411553,-8.233268,1.506861,-3.228541,-1.348996,-4.134405,-0.144074,1.532025,6.156780,9.004983,3.260806,-4.362515,7.338398,-8.636475,2.094023,5.118138,8.664042,-0.057159,-3.423629,-3.602021,-1.139964,7.193926,-5.139702,1.719699,-5.620668,8.191461,-6.825382,2.914699,2.410565,0.281761,-0.952616,4.845098,-8.410406,-7.032301,-5.755058,0.727201,1.234840,6.127246,-2.281801,-4.522652,-1.710471,-7.049399,7.014330,-3.136300,-3.908743,2.539080,1.868034,-0.133130,-2.118646,-3.457172,-8.283321,-7.436962,-1.840959,5.891126,-1.145180,-1.206385,7.788029,5.598571,-9.905636,-1.432879,6.883212,5.852884,-6.751254,9.003863,8.363806,-9.901232,4.814230,7.213979,-2.385467,-5.124346,-0.110950,7.652057,-1.486494,-4.885633,1.358227,4.556927,6.134539,8.682593,-0.723504,-7.854792,-9.471243,4.856292,5.463914,-3.847707,7.025728,7.342226,3.746690,-9.986474,7.102723,-4.993036,8.936344,-8.021373,7.030349,-9.742634,-1.902707,4.079729,1.975399,-4.349565,5.653779,9.354115,-6.194329,1.801708,9.685333,5.841054,-1.835406,9.234023,0.276674,-8.339513,2.253409,-0.921273,-1.898882,9.118509,1.354532,-3.395224,-6.368908,7.235541,-4.076046,-7.810356,-8.879076,1.353522,7.189050,-6.149581,-9.889780,4.712493,-9.584610,0.022283,5.858509,-5.013116,-2.162840,-7.517699,-4.623332,3.070197,-3.742673,7.320901,2.784531,1.602106,5.062460,7.639117,6.427516,-2.254684,5.681869,-6.135943,-8.457809,8.010215,7.797862], dtype = "float32")#candidate|9959|(234,)|const|float32
call_9958 = relay.TupleGetItem(func_3265_call(relay.reshape(const_9959.astype('float32'), [13, 2, 9])), 1)
call_9960 = relay.TupleGetItem(func_3268_call(relay.reshape(const_9959.astype('float32'), [13, 2, 9])), 1)
uop_9961 = relay.cosh(var_9948.astype('float64')) # shape=(567,)
uop_9968 = relay.acosh(var_9933.astype('float64')) # shape=(4, 7, 4)
output = relay.Tuple([bop_9934,call_9940,call_9947,call_9956,call_9958,const_9959,uop_9961,uop_9968,])
output2 = relay.Tuple([bop_9934,call_9941,call_9949,call_9957,call_9960,const_9959,uop_9961,uop_9968,])
func_9970 = relay.Function([var_9933,var_9948,], output)
mod['func_9970'] = func_9970
mod = relay.transform.InferType()(mod)
mutated_mod['func_9970'] = func_9970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9970_call = mutated_mod.get_global_var('func_9970')
var_9972 = relay.var("var_9972", dtype = "int16", shape = (4, 7, 4))#candidate|9972|(4, 7, 4)|var|int16
var_9973 = relay.var("var_9973", dtype = "int8", shape = (567,))#candidate|9973|(567,)|var|int8
call_9971 = func_9970_call(var_9972,var_9973,)
output = call_9971
func_9974 = relay.Function([var_9972,var_9973,], output)
mutated_mod['func_9974'] = func_9974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7213_call = mod.get_global_var('func_7213')
func_7214_call = mutated_mod.get_global_var('func_7214')
call_10008 = relay.TupleGetItem(func_7213_call(), 2)
call_10009 = relay.TupleGetItem(func_7214_call(), 2)
output = relay.Tuple([call_10008,])
output2 = relay.Tuple([call_10009,])
func_10012 = relay.Function([], output)
mod['func_10012'] = func_10012
mod = relay.transform.InferType()(mod)
output = func_10012()
func_10013 = relay.Function([], output)
mutated_mod['func_10013'] = func_10013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5227_call = mod.get_global_var('func_5227')
func_5229_call = mutated_mod.get_global_var('func_5229')
call_10035 = func_5227_call()
call_10036 = func_5227_call()
func_6295_call = mod.get_global_var('func_6295')
func_6298_call = mutated_mod.get_global_var('func_6298')
const_10046 = relay.const([-6.964571,-1.566624,4.633051,4.121631,2.707036,8.190345,8.801148,-0.536620,-5.164723,7.084178,5.555404,-3.042243,1.938137,-8.530663,4.660062,2.102910,-9.128288,5.928889,-9.281007,7.945609,-5.778203,-4.027821,5.840743,0.403743,9.475911,2.275782,3.652345,5.048402,-8.170782,1.867388,-1.374596,8.185504,4.306007,-8.249363,-9.998138,9.554305,3.312277,-5.102388,-9.199682,-0.628328,-4.442616,5.196594,-3.798906,2.354798,-0.199878,-2.485162,3.724666,1.054974,-4.286273,-4.738207,7.369408,6.210998,7.502070,2.843695,7.294930,-7.988171,6.419587,-4.860291,-9.295349,-2.826641,-6.620857,8.706730,9.337364,-7.690494,4.969019,-4.623531,9.163423,4.192513,7.163674,-0.862096,-0.764414,0.832548,-3.702416,0.146729,2.759316,2.094112,9.640362,5.919472,-5.554002,-3.892434,-3.018341,-5.784573,6.870329,1.489573,6.569881,5.225173,-7.009384,7.580792,-7.145776,9.946152,8.685275,-5.217233,-6.742369,6.469111,2.706074,-7.941508,-4.663018,3.277851,-5.140256,-5.137197,3.006186,1.382697,-2.997543,-6.330235,-1.446081,-4.288359,2.356375,-0.154687,-0.081479,-5.916912,6.702893,-7.781196,9.035469,8.351529,-5.190228,0.402356,-6.634259,2.186105,-6.498782,6.140550,9.794756,-7.620779,-9.250749,-7.720281,-0.325747,9.710987,1.155719,8.571704,9.598763,-5.427703,-7.442173,7.118937,6.824851,-1.021314,1.745314,-1.906226,0.715473,2.612120,7.341477,0.478900,-7.460846,7.804730,-1.135127,-6.202377,-6.029727,8.400536,7.218530,7.676617,3.470051,-5.116948,0.175548,2.570293,8.111211,2.568077,5.201095,-9.210294,4.969081,8.439198,-2.499488,4.740345,7.916947,0.953130,-4.145468,8.769665,-8.925567,-7.266806,-7.494178,7.729010,-2.061310,-4.644694,7.496718,4.810593,-4.486153,-0.779008,-9.834991,1.972404,-8.795505,-0.542810,4.055438,-9.265903,5.302970,-8.268032,-1.193626,9.802679,-2.279593,-0.122260,-7.521468,-9.842690,4.844309,3.988273,-1.014812,9.241722,-9.159368,5.618364,5.297787,2.822266,-9.761178,-2.798864,9.468076,2.952707,5.320846,8.914417,9.224050,-7.045875,-3.065634,3.283844,8.893380,3.239188,-5.535377,2.131520,-0.420407,7.361315,-0.368182,-8.024687,8.302477,6.172008,4.385774,8.083734,-6.998298,0.734586,7.676774,-9.010504,1.651279,-2.123937,-4.806426,4.788413,7.040999,-1.209469,-3.186827,0.702156,-3.829940,-9.227169,-4.745159,7.514750,-8.761875,8.770628,2.256372,-1.027542,-1.488422,-2.685436,-3.628795,2.795470,-3.172188,-8.975929,-9.423723,1.812069,-7.655444,9.247261,5.780898,-7.825395,2.108981,5.164144,7.413182,-6.629948,0.349518,-8.997369,-8.914512,5.899005,7.780560,-3.762836,8.703978,3.894994,5.117714,-5.607551,1.853140,-9.185286,0.377288,6.304919,3.979582,-3.480851,-9.348135,6.224922,-2.086310,-2.437499,-2.274373,-6.461836,-0.999802,4.775099,-4.691926,-5.806471,-7.686117,-6.391814,-8.859561,-1.114628,5.242230,-2.797336,-9.495591,9.686931,-7.808490,-0.104024,-6.641107,7.574082,-5.105771,-3.932560,-0.159479,-2.629068,-2.918860,-5.922258,-5.267567,-5.131088,4.789528,-3.755047,-3.482523,9.127804,2.750355,6.015407,-6.193341,-5.764168,-0.018847,8.816657,9.265438,1.266063,-3.469820,-5.962904,3.072795,1.172621,-0.189590,-8.996001,3.511205,1.665779,0.678989,-1.892504,0.495812,8.781105,2.975453,1.545325,-5.538198,-3.195826,-8.908971,-9.787686,-8.531152,3.870149,1.119439,7.059551,8.372828,1.628163,-1.886277,-0.700094,-6.134863,0.222324,-3.449965,-6.003824,3.334593,4.237728,9.809292,0.383894,4.673810,-9.304515,-9.089453,1.658196,7.023681,4.236082,-1.496733,4.564233,2.961123,3.373288,8.798520,-9.799411,-3.577499,8.518164,8.280346,3.242983,2.746261,4.342758,-4.264118,3.643121,0.631635,0.954448,-7.258425,-3.311754,7.844548,3.517357,7.722873,2.083333,3.131973,-1.727046,-4.733552,-3.068997,6.656736,7.787170,-7.200888,8.426151,6.717022,-7.757750,-7.819558,5.059121,-5.930698,-1.113768,5.948621,3.629484,-3.941639,4.551971,-7.416980,-0.971285,-8.708954,6.731086,-4.117426,-0.074158,5.707905,1.349631,-8.860980,2.998637,2.130974,-4.633202,6.603566,-5.606280,9.223775,-2.348493,2.053434,-2.309779,5.834331,-4.944095,-0.912611,2.955280,4.530333,3.971305,-6.692874,-2.896086,6.525858,-7.553436,8.287649,-9.710943,-0.848474,-3.857296,-5.304668,5.699887,-0.535678,2.306929,6.633886,-9.722232,-5.368742,-2.522240,-5.053277,-3.554354,8.912550,-0.956547,4.528682,-8.754140,-6.372508,7.651856,9.633860,-8.516087,5.280540,-7.076334,-8.664578,5.855487,2.211069,1.916074,4.874125,4.749622,-7.333535,9.813168,-8.632647,-7.216804,-1.317395,9.176229,-2.199753,7.062352,-8.313935,-7.766780,-1.191703,9.856943,1.234507,5.614144,-6.218334,-1.368579,-5.777711,7.608817,4.321810,2.507659,9.479478,9.885839,-4.285965,7.318429,-2.281962,-3.533624,-3.617882,-4.794781,-0.672101,-0.062164,-5.763413,-1.009134,-0.830158,-5.517249,4.602592,4.533048,-2.069660,-2.729860,4.963914,0.046884,-7.384698,-8.542902,1.969779,-3.025421,-6.389730,2.441071,7.484974,3.937555,0.824472,1.033560,-6.547697,9.210862,5.139746,5.098439,-5.544347,0.162876,-3.925381,1.726118,-9.971665,-4.858613,-8.907925,-8.180481,7.658326,4.994830,4.845096,2.795386,3.696785,-6.607259,-7.473022,0.752691,7.954701,7.729340,-7.855092,7.699486,7.472870,8.870236,1.495591,1.495867,9.899334,6.004207,-4.916868,-6.916343,-1.651786,-8.361407,2.146284,8.798598,-1.291188,-6.028845,7.270132,-9.677855,7.337656,-7.350677,4.457219,6.077726,-6.054955,2.945392,1.488354,-9.877289,-8.184839,1.944918,-5.924721,-7.692255,7.534945,1.183052,7.805540,4.174926,6.024194,1.171658,-9.734094,0.464344,-1.735728,8.126891,2.326560,4.001997,-7.154545,9.299790,1.578263,-1.586122,-9.079581,0.826736,4.150107,3.346644,-2.585945,0.726889,7.961707,9.423755,0.446319,-2.775749,-2.743175,-0.344413,-0.439501,4.616618,-1.637243,-2.812563,7.087174,-8.432742,8.855599,8.739033,-6.493675,-0.054039,2.738454,4.880392,-0.611290,0.021777,5.978078,9.480034,0.970443,2.713590,-7.583936,8.526406,1.256004,-2.889207,8.035566,-2.086828,-8.185390,6.355249,-0.972322,-1.168237,-8.822145,6.149860,-6.278994,1.881374,8.924454,7.677924,2.220070,2.152515,-1.789775,8.509327,3.981333,5.345035,-3.119013,-4.532862,-4.808878,7.704936], dtype = "float32")#candidate|10046|(624,)|const|float32
call_10045 = relay.TupleGetItem(func_6295_call(relay.reshape(const_10046.astype('float32'), [624,])), 0)
call_10047 = relay.TupleGetItem(func_6298_call(relay.reshape(const_10046.astype('float32'), [624,])), 0)
func_9005_call = mod.get_global_var('func_9005')
func_9007_call = mutated_mod.get_global_var('func_9007')
call_10048 = relay.TupleGetItem(func_9005_call(), 0)
call_10049 = relay.TupleGetItem(func_9007_call(), 0)
func_7017_call = mod.get_global_var('func_7017')
func_7018_call = mutated_mod.get_global_var('func_7018')
call_10060 = relay.TupleGetItem(func_7017_call(), 0)
call_10061 = relay.TupleGetItem(func_7018_call(), 0)
output = relay.Tuple([call_10035,call_10045,const_10046,call_10048,call_10060,])
output2 = relay.Tuple([call_10036,call_10047,const_10046,call_10049,call_10061,])
func_10078 = relay.Function([], output)
mod['func_10078'] = func_10078
mod = relay.transform.InferType()(mod)
mutated_mod['func_10078'] = func_10078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10078_call = mutated_mod.get_global_var('func_10078')
call_10079 = func_10078_call()
output = call_10079
func_10080 = relay.Function([], output)
mutated_mod['func_10080'] = func_10080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_10162 = func_1758_call()
call_10163 = func_1758_call()
func_5330_call = mod.get_global_var('func_5330')
func_5332_call = mutated_mod.get_global_var('func_5332')
call_10176 = relay.TupleGetItem(func_5330_call(), 0)
call_10177 = relay.TupleGetItem(func_5332_call(), 0)
func_4228_call = mod.get_global_var('func_4228')
func_4229_call = mutated_mod.get_global_var('func_4229')
call_10191 = func_4228_call()
call_10192 = func_4228_call()
func_9930_call = mod.get_global_var('func_9930')
func_9931_call = mutated_mod.get_global_var('func_9931')
call_10204 = func_9930_call()
call_10205 = func_9930_call()
func_9464_call = mod.get_global_var('func_9464')
func_9466_call = mutated_mod.get_global_var('func_9466')
const_10215 = relay.const([[-0.297589,-7.501105,-5.832735,9.272398,-8.773891,0.020724,9.016597,-0.973094,-0.798332,9.004310,-8.635323,2.026409,1.347390,-5.993771,-8.627908,9.989690,8.316811,-7.614461,4.829742,-2.499033,3.588313,-3.876130,-9.747126,-1.223134,3.924289,8.606602,-5.678885,8.959732,3.353993,8.236674,3.315326,8.290774,-3.268414,-3.294268,2.415668,-4.877128,-6.492286,7.708946,0.067095,-8.040646,8.910537,-4.861088,-8.514365,5.292825,3.231290,-9.570178,-4.323277,-6.849246,3.924163,-1.383066,0.829373,8.987947,0.058698,-0.511126,-0.823547,-4.839730,-1.183188,-5.741667,-4.968439,-4.566049,-2.656611,-1.125256,-6.883974,-8.433569,-0.524820,-1.679292,8.008713,8.891585,-0.183517,3.025416,-4.759125,-4.236346,-1.260696,-9.354969,6.436645,-8.001365,7.250530,-2.850994,8.175120,4.129391,5.524617,4.262918,2.375577,-4.443258,-9.663132,-5.158351,7.250180,4.288305,6.626658,-6.959981,2.156591,5.712719,5.588410,-5.364392,-4.838047,-3.088010,-1.455064,-4.922066,6.319284,3.075479,-5.813649,-6.708655,6.709673,3.679303,4.652646,8.092022,-0.446298,1.378550,-3.697299,4.903085,0.708450,-5.906139,4.376417,4.212455,4.059241,7.853871,7.049981,9.861553,9.788322,6.917926,-1.384138,5.733639,2.764499,0.597488,4.346978,-9.679157,-3.463211,-0.251884,4.659060,-8.636234,-1.925275,-8.010294,-2.411254,-2.754536,-2.502828,-0.923740,-5.133888,-8.262411,0.573805,5.208057,-3.129272,0.330495,6.230704,-9.666817,-3.313993,2.862024,-3.889728,-2.774649,-9.548536,0.264784,-6.978550,7.866298,2.124308,3.277309,1.202534,9.898643,-5.149363,5.802506,-6.408169,6.920911],[-0.281141,-3.543071,-2.073472,2.747244,7.619938,-6.695134,4.745616,9.666956,3.355166,7.927925,3.595503,-8.762069,2.944005,6.306419,3.872555,-4.734708,-9.376416,7.148909,8.134583,3.518610,7.166300,2.426104,1.761281,3.451944,4.495103,-0.450158,-8.890267,-1.520349,-3.636092,8.167658,-1.012586,6.614084,-3.389282,-4.153421,-1.132171,2.312120,8.914247,-9.131614,8.739577,4.055816,-5.162827,8.743410,-3.660563,-3.207297,-6.106944,-2.921838,-5.139409,2.233620,-4.747200,-8.354167,4.829498,-1.148105,-3.578860,6.874312,5.053209,-1.718500,-0.062187,-2.413681,-2.098589,4.160299,-6.097687,5.315299,-1.299049,-9.270019,-8.336016,2.204118,-8.836640,-9.765915,-1.871987,-8.264330,-5.493231,9.971779,-1.571322,7.517571,-4.501773,2.643531,9.324304,7.736439,2.057803,-8.787924,5.732016,1.372600,-7.736132,-7.392360,-6.115112,-2.282685,-0.269632,4.675359,5.850295,2.757957,-0.120373,-3.192576,8.709316,4.082186,9.298792,5.940285,0.618826,-1.593689,-4.518042,-4.441446,0.045303,-5.447130,-9.941249,0.637028,-8.965327,1.573773,3.180115,-9.593383,-9.403538,-4.883123,-6.178888,-7.951254,-7.985790,2.240336,4.841703,0.331824,-5.080685,-7.385391,-5.229698,-6.910412,-8.491622,3.711217,0.131807,8.153989,7.238107,-5.295147,0.099114,7.813165,4.263804,-1.847493,-2.966289,-8.947153,7.111669,6.866050,-2.979752,5.242938,2.683822,-6.391604,-9.716214,-5.989904,0.197515,0.553830,9.843036,4.388709,5.213374,-2.219147,8.015842,-9.977869,8.611387,-0.994784,3.308631,3.913531,-8.985540,-5.248818,7.713519,-8.716576,1.816219,5.131980,-8.310510,8.840531],[-8.920822,3.128957,-1.192980,1.937413,3.022069,6.475419,1.869872,-5.894761,3.075519,-5.567119,5.800048,0.022545,5.607021,-3.042035,6.933246,7.320777,4.148959,-0.553751,8.999290,5.917232,6.711508,4.655603,6.091924,2.526421,-4.592511,1.497006,-8.438680,-9.776299,5.230733,-3.393180,1.478140,6.269132,-4.337139,-9.665126,1.357995,1.659816,5.153156,6.400893,-6.921721,0.069747,-9.027123,-3.349629,3.273819,-5.305658,8.764215,-2.543797,9.442447,6.599724,1.662130,1.345961,-6.343173,6.888554,9.697014,-3.355728,8.743165,9.661501,3.345307,2.686528,-6.780005,4.364120,-6.566321,-2.422619,5.196920,8.555508,-2.893272,4.133150,5.681707,-6.358984,7.603808,-4.511384,-3.822506,8.347995,-0.257501,-3.303158,-2.139755,-7.723044,3.629803,-9.800820,2.889134,9.818974,-8.381309,-4.922557,-7.832893,0.421933,1.286133,-0.174941,4.483970,4.818976,-2.427839,-8.548794,-1.506646,2.639276,-8.874160,-1.149732,-7.593551,0.001199,7.205493,-1.818610,-2.128221,8.690613,-3.463013,5.029009,7.707684,4.143986,-7.628995,4.982695,-9.220648,0.859836,-0.941084,-5.946776,4.925988,-2.934363,2.927507,-0.471536,-7.268509,-6.224123,-2.723027,-7.567351,-3.344095,8.483715,7.459306,2.134836,-6.899847,-7.481823,0.489161,5.827880,-7.477616,5.100568,-2.363604,3.374828,3.248361,8.838887,7.495761,-5.961546,7.354351,1.743292,-8.805722,8.898404,3.059983,2.702296,-5.685776,3.199651,-1.502290,5.276762,3.471984,0.369272,-0.308662,-0.761621,-1.969077,8.283090,-0.852999,8.483565,-4.525263,5.934117,-0.566636,-2.731751,8.543767,-0.678663,-6.021462,2.615573],[-1.882886,-6.459316,8.550973,3.076579,0.919412,-3.723778,8.129653,-3.649359,-4.380500,9.919000,9.779596,8.279351,6.667243,-7.380973,9.260653,2.803989,2.495083,-9.818646,-3.311011,-9.305924,1.062700,-1.188116,-3.511022,-3.789238,-7.892319,-3.654311,9.828042,5.387829,9.366541,-3.242366,2.269674,-5.798443,6.049329,7.833373,-5.672082,-2.737580,-7.707564,-6.923320,3.086970,1.324510,-2.440875,9.723973,-6.999438,6.656721,0.109066,-8.029553,1.518459,9.326138,-5.270754,1.706007,-2.073484,-2.514743,-2.074849,-1.086657,9.050208,4.672202,8.431145,8.842346,2.532290,9.233234,-1.411216,5.704944,-5.631429,-6.972006,-7.876566,-4.397835,7.427316,6.637310,6.654459,-7.163282,-1.797183,7.550266,-7.308285,2.487892,1.175907,-3.795006,-0.047127,0.103701,-6.215567,9.248147,7.903060,-8.023072,-9.109212,-1.380149,6.075030,-7.760759,6.722466,5.941819,-9.570681,4.235762,6.718443,8.533077,-4.512218,-7.012721,7.145903,9.761102,0.601666,6.882625,6.786894,-5.477650,-3.413263,-3.352637,-6.374680,-1.458228,-6.014835,-1.585745,3.354413,-3.172433,-6.455919,8.180730,-8.109119,9.019269,-4.586553,-9.225625,-9.953976,-4.885597,3.119554,-5.439562,-7.006506,6.621969,4.188497,-5.792387,7.965878,-2.892010,9.685052,9.832772,-4.744962,-0.048335,-8.388358,-3.691686,6.607686,2.888793,-1.035322,-5.885469,-2.910448,9.593606,5.787234,8.883153,-2.585636,-8.147496,6.052228,-5.265083,-0.650691,-4.594172,3.252550,-4.381126,7.520182,3.203843,2.883047,-0.975282,5.207597,6.117049,5.734425,-0.383367,-6.355154,9.993767,-2.098042,8.981337,-8.343152,4.210583],[4.849837,-6.006558,-1.024882,-3.959024,2.079841,3.792069,-3.244070,0.081587,9.901359,-3.420019,5.315942,6.209484,3.842733,-8.966543,-0.447962,5.260449,5.069050,-0.375165,5.421462,-5.358199,9.526950,-4.504045,-9.892051,8.090493,3.972284,-0.024517,-3.566961,-4.697759,-4.233612,3.585285,6.595662,-5.745830,1.645809,-7.499670,0.985941,1.280607,-2.293521,4.041151,-3.968239,8.675973,-9.523615,-8.658530,9.423604,-3.098050,4.502169,4.012887,-3.268488,-3.126633,-8.177417,-9.333066,6.663543,4.736884,6.651149,-9.735180,1.794691,2.809073,8.858077,-9.235507,8.861146,7.543208,3.033675,2.156443,-3.505926,5.741783,-2.737735,5.706005,4.645596,5.081617,3.344800,-1.199337,3.660462,-6.621984,5.048726,-0.746785,9.040074,-2.961533,-5.750502,-4.177586,6.700056,4.760056,4.611950,6.489734,9.732046,-7.299141,-3.693442,-5.451327,-5.736924,6.668405,3.835929,-0.555053,0.411067,1.677690,-4.967128,-6.430469,0.411562,5.915506,-3.498030,-2.372957,-4.893418,-4.604598,7.062653,-3.280375,7.870815,-0.425617,3.951490,7.858577,1.231904,-6.704765,-6.093055,7.396771,5.183529,3.350911,2.669941,8.208773,-6.348077,-5.449245,-9.936486,3.397334,-0.541661,0.125900,9.304531,-5.520721,4.573371,-2.396257,-7.376044,-6.575102,2.195997,4.066872,2.046571,-3.683028,2.657023,1.721283,8.523068,3.468916,-0.011501,-6.581508,-8.810096,-2.325083,8.904700,3.413629,-2.126032,7.544069,0.984760,-5.840968,-9.032666,-1.377056,-7.749049,5.443007,4.188193,6.736607,4.676496,2.572776,6.401423,-5.853526,-5.380811,-3.367519,4.483731,-4.143593,-8.135973,1.722006],[0.828450,-9.146497,3.893144,-2.204679,2.915406,7.984730,4.313116,-2.068761,-2.361712,0.406937,-9.421274,-3.879824,-6.787878,5.912229,3.342839,8.226317,-8.791581,-5.800186,3.746510,-0.603846,8.672781,-7.244197,-2.171331,1.668505,2.579924,-9.577922,-1.471860,9.213780,6.479514,1.579805,1.400272,-3.149559,5.560421,0.272966,7.531247,5.742331,7.334829,5.621030,-2.892253,0.031473,0.125995,2.172716,-5.142158,-7.947168,2.659317,-7.253200,-7.680401,1.157004,-5.901520,3.781513,-4.904111,-0.687246,-5.558843,-5.500388,-3.793525,-1.341972,5.685677,7.501916,-0.255305,8.670067,4.141703,-9.933970,-6.267774,2.871541,-5.153112,-7.270973,9.542647,8.782461,-0.042803,-3.683116,1.450092,3.131443,2.597356,-0.904325,-5.688533,4.387345,4.194567,-2.923067,2.744101,-1.949178,-6.546662,2.229304,1.633652,0.249807,-5.980394,-0.548216,-2.961480,-3.167167,-4.971752,0.147722,-2.192726,4.735242,-8.008081,-4.148751,9.973892,1.365127,4.552803,-7.124708,9.348495,0.589829,9.349304,1.635257,4.860723,1.560378,-1.386141,-4.109753,-6.945455,3.514913,4.867739,-8.200045,-5.632958,-5.263041,-7.710034,2.084812,-8.386282,4.798119,-5.268403,5.243965,-2.129487,-2.086209,9.361899,-3.462759,-0.661501,-3.473727,0.126540,-5.710900,2.535987,7.698242,2.356142,2.514495,1.275820,-5.018466,-5.853006,4.503498,-1.711945,6.476881,2.847324,4.243429,7.554505,8.470478,9.798952,5.660817,8.494674,-1.195782,3.479182,-2.759128,2.282339,-4.042407,3.293402,-6.755395,8.293138,8.662440,3.645642,-4.691279,7.501996,7.521517,-8.360708,7.234162,-8.200801,-4.959077],[1.322426,-0.001277,8.438854,-8.425164,0.687750,7.334432,1.408699,8.839082,4.536451,9.098004,4.869875,8.804208,9.988216,2.956215,6.692067,6.841967,4.334453,9.686206,0.442088,7.149992,-5.991833,5.842565,1.492214,9.080346,7.328001,5.974432,3.267204,-4.828928,9.697703,-4.709932,5.903769,-4.678331,-2.466895,-7.268888,5.951038,-5.432470,-9.422235,8.456888,-9.070484,-4.122369,-3.520065,-1.626429,9.296432,-4.234416,4.504997,0.168893,9.408220,4.833489,7.487827,6.103798,3.273088,-8.078138,0.346750,7.687220,-8.070116,8.303091,-7.371844,8.136038,-4.458837,-3.751043,-2.219537,4.536975,3.986141,4.999188,-8.378262,-3.357484,-2.145848,2.782099,-5.362204,6.956915,-1.070087,8.748734,0.327782,-1.222910,2.079961,6.674013,-4.677097,7.746891,9.174119,-3.116419,8.142769,9.141206,-1.187299,3.284299,9.418466,3.941292,-8.613422,-7.456400,4.907135,1.384282,-9.939475,2.211906,1.368142,-3.878314,9.093196,-8.150443,2.666331,0.816138,-5.366193,4.774204,7.347201,-3.785512,4.146112,7.743469,9.809237,9.684102,8.125250,2.170211,6.072405,6.485582,-2.329805,6.754467,3.678112,1.801262,-6.481626,-1.319061,-2.408143,4.696185,6.245064,-1.500941,0.570019,-0.557992,-1.296528,-6.927629,-8.442764,3.654407,2.030168,-9.230558,3.016812,2.359624,-6.904394,5.635819,-2.537119,7.796695,-1.995468,-0.363755,9.031992,-1.391460,-0.350354,-9.029390,1.883110,-2.339073,-2.761417,6.691051,-5.595016,9.408951,-7.054892,2.554636,6.577411,7.587497,7.919020,-6.992832,-4.994374,-6.756933,8.620976,0.639619,-0.774021,0.932981,8.327736,-2.878465],[2.771849,-1.424422,0.521121,-4.304834,-8.468110,-6.378830,-5.379716,3.827267,1.593881,6.586711,-0.775648,6.972738,-1.290980,5.333471,-0.629643,-7.874560,-3.170627,3.474976,-9.819676,-5.099225,6.489830,-4.012469,7.568080,2.130447,-9.059207,0.154723,1.333670,5.091641,-5.068512,1.189503,8.763532,-6.049491,7.829205,8.722094,-8.731511,-5.329429,-7.694590,0.637115,-1.108949,-9.639588,0.871086,6.507198,5.133166,7.739383,-4.990781,-8.792402,-5.663089,5.443372,-8.339031,6.371657,-7.202817,5.317653,6.121553,7.393984,7.627585,-8.163187,6.772754,1.762622,-7.002259,-3.487055,-3.201553,-1.702726,-3.631995,-2.542403,-2.743810,4.751533,9.392055,1.270969,5.409936,7.299349,1.958439,5.293975,5.650205,4.158743,8.418811,-1.895459,-1.835706,-5.513869,-0.349831,6.370118,0.580948,-5.485946,6.674258,7.471199,-0.140196,7.920659,-9.894204,-5.728048,-3.991926,1.302379,-9.473089,2.102780,1.289668,6.749569,-2.981420,-4.257544,2.070996,-0.289358,6.970113,1.229779,-7.214297,2.262966,0.779973,1.303286,4.002393,-3.491105,-9.980758,-5.211648,4.055327,-7.000842,-4.985210,5.991272,0.997288,1.179028,7.407993,-5.497142,0.871280,-3.387631,1.031932,-7.605473,3.828087,-4.292618,-9.799876,1.937192,-0.596661,9.975392,-1.343230,-7.089915,1.407911,-4.999189,-7.124135,-8.201611,-9.296777,1.637422,-1.563291,-5.411386,-6.344636,-2.862052,8.027243,-1.111129,0.037363,3.623626,2.850323,8.683578,4.102215,4.914176,-6.811853,0.290485,6.404453,-4.028488,6.107340,2.447856,-7.794863,-8.097669,0.393018,0.427668,4.400820,-7.947752,0.325604,7.461487],[-9.401699,-5.168303,-1.161991,8.557681,-4.632121,-6.175665,4.363436,9.012540,5.393139,4.927830,4.974341,5.970006,9.913708,1.579030,7.222651,7.364762,7.634803,-0.248193,-0.239791,7.227345,8.198513,-9.807675,9.331904,-7.121983,3.311456,7.608542,3.888897,3.360740,6.979022,5.012585,2.333468,-3.759889,-3.497734,0.034082,-8.691574,-2.946813,-5.148579,-2.650228,-9.884332,-5.952044,5.472433,-1.982953,-2.938680,0.793196,-9.928744,-5.826510,-9.875344,3.656092,5.981250,3.468686,8.378624,0.149098,-3.721284,-1.107648,9.951548,-0.811747,-6.032773,7.903252,9.418797,-6.535427,5.925746,3.276430,1.256618,-0.058781,7.133155,7.832456,5.183489,-2.316042,-1.278909,5.466949,8.596803,-4.738872,-6.826340,-9.482010,0.757913,-6.787534,7.001751,-5.271893,-4.044658,8.125638,-7.574057,-6.729857,-6.192411,0.254633,3.624952,-7.446807,-8.480415,1.490948,-1.004074,-6.690022,-5.146444,-4.097357,3.966951,6.841636,2.196761,2.072959,5.173734,-0.580395,9.159833,-0.173142,-3.632701,0.393746,-1.554154,4.476859,0.282004,-3.966812,-7.284519,8.287462,7.401333,1.710059,-0.119772,-9.740463,4.477776,5.239783,-8.823375,7.164195,-2.150046,5.624713,9.871380,8.360435,0.126069,0.334416,-8.449747,0.426481,3.409770,-4.051843,8.173070,6.459752,3.931797,5.196226,-6.874912,-2.794526,-5.570085,9.068134,4.623943,-6.096049,-5.845386,-1.572691,-7.132636,-5.413827,2.855315,6.264127,1.443780,8.881507,2.105410,-3.137231,8.484573,-5.763155,5.897573,-4.469864,-8.904707,5.922352,-4.972020,3.169963,9.035641,-9.734159,6.146257,5.507924,-2.485382,9.852829],[-9.597281,0.020471,8.387733,0.900152,-2.288858,0.339047,-6.200124,4.279712,-3.151779,6.578948,6.308928,-9.460123,-1.765647,1.164599,-1.911386,-1.137345,0.776686,0.862205,-3.759303,7.443155,-7.226501,7.361082,9.299700,1.226973,-7.742841,2.767439,-5.619238,-7.063078,8.909539,9.282925,-6.830611,-0.491593,7.997149,-6.674892,-3.797056,-8.562635,-1.784597,8.865676,1.257727,-3.803487,-1.732858,1.433031,3.251864,8.944503,1.291351,0.377251,-8.217950,7.202643,5.376089,7.332235,3.578857,-7.885537,-1.771068,3.364543,-7.731010,4.183877,4.546267,2.445538,-4.359845,-3.108459,6.068462,2.532955,0.254519,4.329306,6.830868,7.994921,4.622501,-1.655055,1.959537,2.625021,9.391080,-4.522513,4.125576,-4.623281,-8.955962,2.848690,-4.985121,-2.533389,-0.916255,-6.552241,-8.698967,-4.736095,8.492741,3.704216,5.735330,-0.243945,7.898891,9.037125,-9.693284,-5.241265,-2.939646,-9.184988,6.271814,5.760556,-3.344563,8.893251,7.870363,-2.095066,-0.468453,9.774566,-6.360364,4.629190,0.267516,-3.052747,-3.436043,-9.446023,9.019581,6.066300,0.482702,-5.137665,-5.061710,4.435997,1.691711,-4.583472,7.276743,8.298996,1.475925,-9.758278,-4.180065,-0.644872,9.804775,5.621796,9.480148,0.997083,5.021706,-9.933018,1.656820,0.318558,-2.002224,3.296842,-4.383081,6.059052,4.568600,-2.663739,0.620240,-1.646028,4.906029,5.966175,-7.856262,-3.230615,-6.716000,8.800173,-9.443636,-0.447598,-0.625212,-9.013841,8.132189,-0.642368,9.649940,-0.392904,8.006642,-5.449874,-2.234546,3.524063,-5.229592,6.760457,-2.442880,1.812733,6.951153,2.921706],[0.693007,-0.130866,-7.758142,5.825128,6.385053,-5.047357,-2.015073,-9.801481,-5.265767,7.476388,3.568918,7.121361,4.311885,-6.366840,-4.660124,-1.931183,9.083686,-0.836534,8.045004,-4.699984,8.734013,9.011728,8.203141,9.510591,9.380291,-3.166466,5.015806,-2.508419,-1.542774,8.715613,6.678672,-4.325397,5.040787,-8.805049,-6.997129,8.281305,2.506415,6.700348,-7.044413,-4.625108,9.591948,-8.719453,-0.911410,2.784675,2.222306,3.976149,-2.191719,-9.899546,8.257921,-7.624951,3.926085,0.137541,-6.832420,6.151145,1.841548,-9.649678,-1.390184,0.719242,-5.980519,-1.660525,-5.734701,-6.382190,2.078929,-3.371661,0.478827,3.113765,-7.065182,8.293616,6.725948,-8.495115,-3.844240,-7.971138,8.549308,4.522416,-3.547897,-0.384509,1.382428,-4.537358,2.479677,0.197728,0.373701,4.807083,-6.396125,5.576880,1.888090,-5.378761,-6.494316,-0.664838,0.370369,8.900137,8.487910,-4.371397,-9.197267,-3.702339,8.157982,-7.218084,-6.159645,-6.660458,-4.347898,-5.797641,3.984574,8.369406,3.464962,-2.965452,0.497103,5.111669,8.343312,-3.928272,-4.066441,6.035737,-3.736179,-7.681403,0.692274,8.106429,-6.050083,4.342332,1.454463,-6.695161,-0.977242,1.282932,-4.368522,6.008871,-0.865104,-1.452487,-7.877234,-0.431283,2.067408,5.083208,0.892611,2.087364,-0.841030,-6.770344,6.892990,0.965981,5.998150,-0.886234,4.991052,0.420822,2.598408,-4.908378,1.358371,-6.139730,9.614667,6.995492,5.524922,8.127404,9.796890,3.375952,-7.362748,-8.248745,6.028220,5.462091,-0.918955,-5.199901,-7.493604,2.646556,1.090632,7.874174,6.281040,3.419986],[4.242613,1.998481,-6.218322,6.012828,9.837521,-3.610586,-1.757426,5.332536,-2.524640,-1.052670,-6.015717,-0.481154,-6.124169,-0.091029,-7.370150,-5.148808,-9.877295,-2.486327,-9.941338,5.339056,-2.164528,-6.544980,-4.697004,0.371153,5.088353,4.713176,-5.690060,2.728851,5.474769,-8.793906,5.697591,7.018312,-4.456867,4.179794,-5.448211,-2.041677,-4.844551,6.464256,-4.712990,-5.563798,8.542796,9.122924,7.624754,-4.319588,4.818659,2.579235,0.616776,-0.785205,-7.921926,-3.063970,4.454644,6.781085,2.272070,-4.689353,-6.560034,4.660143,-4.435535,8.768753,5.952356,8.754020,-7.795213,5.570730,3.287707,-8.310634,3.536348,-9.330886,6.122005,2.018261,7.584065,9.902879,-0.282397,0.171018,4.912356,-2.747503,-0.529189,0.088232,-3.797463,-2.222342,8.967746,-9.585273,2.299624,1.789460,-9.334919,5.398051,-9.280186,0.193240,3.571906,1.761522,7.814328,6.320416,1.109326,5.887540,1.842897,-5.048221,-7.106572,-8.180483,6.398358,-3.993722,-1.856876,2.429346,-3.594056,7.827499,6.417716,9.610350,-1.746135,-7.154328,3.875155,-9.572112,9.455820,7.637082,2.055517,9.496774,0.042317,-7.131703,5.329360,-1.218973,0.966923,0.027338,7.606488,0.245086,1.561628,3.880265,6.828956,-6.937011,-2.128489,-9.030364,4.450670,5.398414,-5.944848,-0.448699,0.819453,5.675355,-8.769946,-1.834049,8.921366,4.923884,4.758609,-5.267633,-7.802043,-7.249946,-1.418633,-4.837842,-1.295885,6.939156,-3.829838,2.509494,-2.630847,-6.610719,4.648372,-4.118333,-4.374554,-4.673680,9.198317,2.860848,7.069499,-6.491494,-5.353664,5.913771,-0.770693,8.846496],[-1.670657,8.489020,-0.206063,1.885342,-1.287998,-5.996548,0.627322,-6.827452,9.014074,9.786305,7.298789,6.294839,-8.735611,7.037319,1.102016,7.234625,6.031338,-6.197035,-1.800627,0.077474,-0.802169,-1.030840,-0.379498,-4.508763,-5.334786,-4.026240,6.568200,0.388963,-7.357552,5.973269,-4.001102,2.401851,1.630658,2.632979,8.402004,-5.767850,-0.293213,-9.826338,4.075555,9.239462,-1.581087,-4.173209,1.216703,5.473588,-0.906052,2.728423,-6.961708,-6.290382,-0.012619,5.029265,-1.228351,2.686055,-6.309044,-4.901604,-7.790089,6.469659,5.105522,9.953680,-8.976340,6.227162,4.140267,9.102065,7.666393,6.589480,2.521502,-2.988975,-3.262153,-1.968644,0.856441,-9.812368,-9.401696,-9.171007,2.362054,-9.578994,-4.721050,-5.895289,-5.313009,7.931268,4.565998,-1.686124,-6.343038,0.155423,-0.595644,1.840144,-8.189803,-5.459710,-6.534241,-9.116338,-3.613430,4.390698,-0.050953,-8.857379,5.842378,3.431187,-9.086662,0.473588,-9.836824,4.991299,-2.319582,-9.842689,-4.305732,-6.601063,9.250910,3.991769,3.420555,-6.154621,-6.343939,9.312056,5.284664,0.746211,-6.290155,-1.090250,9.960376,8.661323,-0.225403,-2.872471,-0.894802,2.457484,7.830793,1.829468,6.850297,0.218683,-1.908464,5.420701,0.745886,9.993913,2.757510,-4.802474,2.470535,3.403358,2.993416,0.923074,-8.106003,3.651889,9.181107,-6.922595,-3.079509,-1.854370,-6.218493,-3.974503,-2.931725,3.645203,5.191453,-0.093170,-7.128693,8.582062,9.208287,2.467964,4.071138,-6.798662,-1.739641,-7.581461,-0.404448,6.577766,-1.616740,-4.259689,-7.422763,9.826623,4.887280,-5.852752],[7.289583,7.041240,-1.574887,-1.828904,2.576504,-5.955846,3.929341,-6.744142,-0.200256,9.827136,-8.387695,1.206207,3.950989,-6.064715,8.156986,-1.333976,-3.192311,0.105418,1.627486,0.397196,-3.391316,-3.539798,-3.726564,4.681483,-7.802083,5.031379,-7.012786,6.424567,4.241310,-8.575909,3.480757,8.493063,-6.339363,-9.037353,-4.887211,-9.226295,-9.336375,7.934963,-9.923107,5.330685,8.198424,3.789557,9.316552,2.051506,-1.185138,5.166128,4.891631,-0.851421,-6.770267,6.426124,-0.112338,2.828068,-1.262379,8.659669,-5.636838,7.617156,0.779875,4.266915,-2.831802,-7.302855,5.307952,-6.352522,-3.915333,-4.462723,2.379650,-1.119376,-6.569415,-4.638132,-6.112468,9.846130,-3.019574,-0.493625,2.691792,5.834842,-9.239110,-9.785993,8.855208,-1.964063,9.198156,-8.428478,-8.248714,-2.857483,8.001359,2.362130,-8.541174,-0.862013,-2.997569,1.084825,-7.669852,1.251189,-1.724267,-6.015966,-5.575881,7.005103,-0.843947,-1.524525,-4.722339,2.230037,-3.676402,7.269996,6.802702,3.960328,-5.972790,2.364130,4.607829,-2.119173,-5.897911,-3.153526,4.159749,3.270344,4.230786,7.111483,-2.363313,7.514786,3.499455,-3.675223,-1.286939,-4.844408,-1.848542,-5.652292,-7.850628,8.142935,7.977643,0.583577,1.786896,-3.235745,4.861141,0.826940,-0.781779,-8.078028,2.947734,-2.322415,-0.694650,8.087490,-8.488592,3.454104,-9.780745,-9.094743,-3.269623,-0.436901,-8.041144,-6.499935,-9.340965,3.477576,7.044884,0.552649,-1.875528,-9.829553,-5.093872,1.876268,7.505284,-0.172034,2.077439,-7.553010,-4.026299,-3.928911,8.045835,-7.871680,-2.328312,8.161027]], dtype = "float32")#candidate|10215|(14, 160)|const|float32
call_10214 = relay.TupleGetItem(func_9464_call(relay.reshape(const_10215.astype('float32'), [280, 8])), 0)
call_10216 = relay.TupleGetItem(func_9466_call(relay.reshape(const_10215.astype('float32'), [280, 8])), 0)
output = relay.Tuple([call_10162,call_10176,call_10191,call_10204,call_10214,const_10215,])
output2 = relay.Tuple([call_10163,call_10177,call_10192,call_10205,call_10216,const_10215,])
func_10218 = relay.Function([], output)
mod['func_10218'] = func_10218
mod = relay.transform.InferType()(mod)
mutated_mod['func_10218'] = func_10218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10218_call = mutated_mod.get_global_var('func_10218')
call_10219 = func_10218_call()
output = call_10219
func_10220 = relay.Function([], output)
mutated_mod['func_10220'] = func_10220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7017_call = mod.get_global_var('func_7017')
func_7018_call = mutated_mod.get_global_var('func_7018')
call_10249 = relay.TupleGetItem(func_7017_call(), 0)
call_10250 = relay.TupleGetItem(func_7018_call(), 0)
output = call_10249
output2 = call_10250
func_10251 = relay.Function([], output)
mod['func_10251'] = func_10251
mod = relay.transform.InferType()(mod)
mutated_mod['func_10251'] = func_10251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10251_call = mutated_mod.get_global_var('func_10251')
call_10252 = func_10251_call()
output = call_10252
func_10253 = relay.Function([], output)
mutated_mod['func_10253'] = func_10253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5182_call = mod.get_global_var('func_5182')
func_5184_call = mutated_mod.get_global_var('func_5184')
call_10286 = relay.TupleGetItem(func_5182_call(), 0)
call_10287 = relay.TupleGetItem(func_5184_call(), 0)
output = relay.Tuple([call_10286,])
output2 = relay.Tuple([call_10287,])
func_10293 = relay.Function([], output)
mod['func_10293'] = func_10293
mod = relay.transform.InferType()(mod)
mutated_mod['func_10293'] = func_10293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10293_call = mutated_mod.get_global_var('func_10293')
call_10294 = func_10293_call()
output = call_10294
func_10295 = relay.Function([], output)
mutated_mod['func_10295'] = func_10295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5050_call = mod.get_global_var('func_5050')
func_5051_call = mutated_mod.get_global_var('func_5051')
call_10311 = relay.TupleGetItem(func_5050_call(), 0)
call_10312 = relay.TupleGetItem(func_5051_call(), 0)
func_6390_call = mod.get_global_var('func_6390')
func_6391_call = mutated_mod.get_global_var('func_6391')
call_10315 = func_6390_call()
call_10316 = func_6390_call()
output = relay.Tuple([call_10311,call_10315,])
output2 = relay.Tuple([call_10312,call_10316,])
func_10329 = relay.Function([], output)
mod['func_10329'] = func_10329
mod = relay.transform.InferType()(mod)
mutated_mod['func_10329'] = func_10329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10329_call = mutated_mod.get_global_var('func_10329')
call_10330 = func_10329_call()
output = call_10330
func_10331 = relay.Function([], output)
mutated_mod['func_10331'] = func_10331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8661_call = mod.get_global_var('func_8661')
func_8663_call = mutated_mod.get_global_var('func_8663')
call_10364 = relay.TupleGetItem(func_8661_call(), 0)
call_10365 = relay.TupleGetItem(func_8663_call(), 0)
func_6412_call = mod.get_global_var('func_6412')
func_6413_call = mutated_mod.get_global_var('func_6413')
call_10425 = relay.TupleGetItem(func_6412_call(), 0)
call_10426 = relay.TupleGetItem(func_6413_call(), 0)
func_10329_call = mod.get_global_var('func_10329')
func_10331_call = mutated_mod.get_global_var('func_10331')
call_10433 = relay.TupleGetItem(func_10329_call(), 1)
call_10434 = relay.TupleGetItem(func_10331_call(), 1)
func_2865_call = mod.get_global_var('func_2865')
func_2869_call = mutated_mod.get_global_var('func_2869')
const_10440 = relay.const(-4.847022, dtype = "float32")#candidate|10440|()|const|float32
var_10441 = relay.var("var_10441", dtype = "float32", shape = (198,))#candidate|10441|(198,)|var|float32
call_10439 = relay.TupleGetItem(func_2865_call(relay.reshape(const_10440.astype('float32'), []), relay.reshape(var_10441.astype('float32'), [11, 3, 6]), ), 1)
call_10442 = relay.TupleGetItem(func_2869_call(relay.reshape(const_10440.astype('float32'), []), relay.reshape(var_10441.astype('float32'), [11, 3, 6]), ), 1)
func_6207_call = mod.get_global_var('func_6207')
func_6211_call = mutated_mod.get_global_var('func_6211')
const_10444 = relay.const([-1.074589,-5.253440,6.203744,-0.165292,-4.032992,5.862245,-5.452582,-8.327859,6.414739,1.397402,6.949936,9.927983,8.597773,-6.133560,2.845303,-9.759031,9.074699,7.138417,9.659186,0.668985,3.038762,-1.692511,6.963347,-6.035229,8.575418,6.306864,2.180296,-9.639712,8.071874,9.389258,-6.147761,4.790724,-4.772731,-0.927345,-7.369243,3.597374,-1.672395,5.028792,-9.533861,1.604763,-3.513500,-1.895940,0.415082,-9.218019,4.428044,4.944571,8.371159,7.517776,7.338262,0.325896,2.042080,0.447571,-5.875240,-3.871132,-2.582625,8.483414,-6.145508,-2.589856,-7.249404,-1.399051,1.108580,4.272272,-7.018603,-6.387447,-3.912682,-8.132832,8.659388,-4.529549,-3.897856,-7.689072,-9.414039,3.586910,-6.722849,-2.213710,-3.952845,-4.672096,-0.755813,7.958002,7.558004,-2.123372,0.424683,6.425336,-2.390926,7.730670,-2.842548,4.715601,0.334684,5.806627,6.980147,-7.433922,2.723643,5.320237,-3.493082,-5.753527,-8.668007,0.012556,5.287334,-6.024759,-3.757800,1.027724,-9.216128,4.880674,5.104175,3.440439,-5.106306,2.903067,-3.920505,2.525709,0.464846,-1.565150,-8.696347,0.011502,5.609775,0.617230,4.699840,-3.290708,-7.749427,4.684790,2.145735,-1.985271,-7.576905,0.184945,-9.854626,1.285405,-4.428728,5.419302,-4.853891,1.175514,5.446487,3.732657,5.351821,-1.578392,-6.869279,7.396930,-6.175453,3.666589,2.532815,5.463787,-4.433108,6.692893,4.429904,2.578929,-8.274831,0.859757,-3.892137,-2.180462,-2.280116,2.437806,2.214838,-6.752515,-2.114584,-8.160282,-7.368626,7.247025,2.101374,-2.442916,4.160055,-6.428257,-2.618018,0.426289,-4.817073,-8.363898,-0.320710,8.076875,-5.736701,1.059168,-6.931355,8.934842,-5.468783,4.762622,2.017409,-4.589184,1.228930,-5.867554,-8.101708,-4.547067,-8.962419,7.122234,-9.714123,-1.902212,8.960925,2.980539,6.434034,-3.225345,6.284278,3.695656,2.796583,-4.355775,-8.763663,-8.503528,-3.385601,-0.159144,7.623723,-0.677896,-6.859818,5.060497,-9.007239,8.675624,7.653770,9.023965,7.505083,8.631586,-4.201085,-9.983351,5.164620,6.341989,8.855577,-9.148236,-2.284163,5.668692,6.832520,-2.078791,1.567456,8.572673,9.616662,-2.965550,-8.945426,-2.841201,9.555871,3.205573,2.325757,-1.733716,-3.472267,-5.504381,5.328383,-2.349047,-2.748139,7.431844,-6.254362,-2.878053,3.734848,8.043098,-0.298880,2.241863,-3.551403,-9.500380,6.990534,-2.928285,0.952231,-0.828317,-7.335421,7.027282,5.500119], dtype = "float32")#candidate|10444|(243,)|const|float32
const_10445 = relay.const([-10,9,4,9], dtype = "uint64")#candidate|10445|(4,)|const|uint64
const_10446 = relay.const([[10,6],[-10,-1],[-6,5],[-8,10],[6,7],[-10,-3],[-7,-2],[-6,3],[-6,-1],[-9,7],[1,-9],[-8,-3],[8,10],[3,2],[-4,6],[-1,-7],[9,-3],[2,6],[-2,4],[-3,6],[-9,9],[4,1],[6,-9],[8,3],[-3,6],[6,1],[-6,-10],[6,-10],[6,8],[-1,-7]], dtype = "uint64")#candidate|10446|(30, 2)|const|uint64
call_10443 = relay.TupleGetItem(func_6207_call(relay.reshape(const_10444.astype('float32'), [243,]), relay.reshape(const_10445.astype('uint64'), [4, 1]), relay.reshape(const_10446.astype('uint64'), [2, 2, 15]), ), 2)
call_10447 = relay.TupleGetItem(func_6211_call(relay.reshape(const_10444.astype('float32'), [243,]), relay.reshape(const_10445.astype('uint64'), [4, 1]), relay.reshape(const_10446.astype('uint64'), [2, 2, 15]), ), 2)
const_10448 = relay.const([[[-4,4,-2,-3,-8,9],[-9,6,9,-1,10,-6],[8,-3,10,8,-8,7],[1,-2,10,9,-6,1],[6,4,5,-5,6,5],[-3,4,-3,1,1,-5],[7,-2,-10,10,-6,-4],[-6,5,8,-10,1,2],[4,-8,-9,6,6,8],[-3,-1,-5,-2,-3,-5],[-5,2,10,1,-7,9],[-1,-3,4,-4,2,-8],[2,9,6,-8,10,8],[4,-4,-8,9,9,-10],[-3,-2,2,1,-1,-1],[4,-8,9,-4,5,4]],[[-10,-5,-2,4,9,-10],[7,7,4,4,7,-4],[-8,-7,-8,-8,-3,9],[-10,-1,-10,-4,-4,6],[-8,8,2,2,-10,-5],[-2,-7,10,10,-1,-10],[4,10,4,-6,8,-10],[5,2,-2,6,-4,9],[-10,-3,-10,2,9,-1],[-9,7,-2,10,8,-5],[-9,-6,-7,-6,-4,10],[5,9,5,7,9,-3],[-1,-10,-5,1,7,6],[2,3,-2,-1,6,-9],[4,-6,1,5,2,-3],[10,10,1,3,7,-9]],[[-8,4,-2,4,-2,-10],[2,7,1,-3,-3,-2],[9,8,-3,7,-9,7],[5,-9,4,1,5,1],[7,-8,-9,7,-8,-5],[3,-2,4,-4,-3,-7],[-2,-4,-4,4,-1,4],[-3,-7,7,1,6,2],[5,1,9,-6,6,-10],[4,-4,6,-4,-10,-1],[-5,-6,-6,-2,-4,-10],[1,-8,3,-9,-1,4],[4,10,9,2,-6,6],[9,-4,1,8,7,10],[3,8,6,-5,10,-4],[-9,-4,5,6,7,8]],[[1,9,3,9,-1,-2],[-9,-7,4,-9,-8,-5],[-4,-8,10,-9,4,-10],[-9,3,-6,-7,3,5],[5,-8,8,7,-4,-4],[-1,-5,1,9,6,2],[-6,8,-2,7,-10,10],[10,-1,10,-1,8,-5],[-3,1,-8,-3,1,-6],[-6,-10,-7,6,6,2],[-5,-9,8,2,-2,-3],[5,7,-7,8,-3,2],[9,-7,-7,2,-1,3],[-7,-3,7,1,9,-9],[-8,-10,7,1,9,-10],[-7,8,-3,9,7,1]],[[7,-7,8,3,-5,9],[6,-8,9,3,10,6],[-4,3,7,5,-6,10],[-10,-9,7,-7,-9,-10],[-10,-4,4,-4,-5,10],[-3,-5,9,2,-2,4],[-1,4,5,8,-7,-8],[2,-9,-10,-8,6,-1],[-3,-4,-8,-4,-1,-8],[-2,-2,1,-10,-1,-2],[10,4,-5,10,-2,3],[-5,6,5,2,4,-4],[3,10,5,-7,-3,-2],[7,-8,-8,-8,8,-9],[-10,8,-7,1,-10,-6],[-2,-1,-3,3,5,-1]],[[-2,8,-3,-3,-9,8],[-5,4,9,-10,2,-4],[-2,-6,-10,-2,8,-4],[-6,-5,-8,-9,-2,-10],[-4,10,2,2,4,-3],[-7,-1,-2,3,2,2],[-10,4,-5,-3,-5,-4],[10,2,-4,-10,-9,-5],[4,10,-7,-7,-5,-1],[7,9,8,10,-1,-1],[7,-7,10,9,9,1],[2,-3,1,7,-7,-2],[2,-2,-4,10,-4,-8],[-9,8,6,6,-9,7],[4,-8,2,7,-3,7],[-3,9,-5,2,5,4]],[[1,-3,2,10,4,8],[-1,-10,-5,10,-7,5],[-7,6,7,5,-3,-8],[-8,10,10,10,2,-4],[10,-6,4,-8,6,-2],[5,3,-6,4,1,8],[1,-3,-9,-3,10,3],[-9,-6,5,10,-7,-2],[5,-9,-10,-8,-4,-8],[-5,-1,8,-10,4,-4],[5,-3,-8,-7,10,9],[-2,3,-5,8,-1,8],[2,-8,5,-9,7,-3],[6,-10,-6,8,-4,-4],[1,-3,-3,-4,9,3],[-4,-2,-4,-8,7,-7]]], dtype = "uint8")#candidate|10448|(7, 16, 6)|const|uint8
bop_10449 = relay.bitwise_or(call_10439.astype('int16'), relay.reshape(const_10448.astype('int16'), relay.shape_of(call_10439))) # shape=(7, 16, 6)
bop_10452 = relay.bitwise_or(call_10442.astype('int16'), relay.reshape(const_10448.astype('int16'), relay.shape_of(call_10442))) # shape=(7, 16, 6)
output = relay.Tuple([call_10364,call_10425,call_10433,const_10440,var_10441,call_10443,const_10444,const_10445,const_10446,bop_10449,])
output2 = relay.Tuple([call_10365,call_10426,call_10434,const_10440,var_10441,call_10447,const_10444,const_10445,const_10446,bop_10452,])
func_10453 = relay.Function([var_10441,], output)
mod['func_10453'] = func_10453
mod = relay.transform.InferType()(mod)
var_10454 = relay.var("var_10454", dtype = "float32", shape = (198,))#candidate|10454|(198,)|var|float32
output = func_10453(var_10454)
func_10455 = relay.Function([var_10454], output)
mutated_mod['func_10455'] = func_10455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7468_call = mod.get_global_var('func_7468')
func_7469_call = mutated_mod.get_global_var('func_7469')
call_10539 = relay.TupleGetItem(func_7468_call(), 0)
call_10540 = relay.TupleGetItem(func_7469_call(), 0)
func_10251_call = mod.get_global_var('func_10251')
func_10253_call = mutated_mod.get_global_var('func_10253')
call_10551 = func_10251_call()
call_10552 = func_10251_call()
func_6265_call = mod.get_global_var('func_6265')
func_6267_call = mutated_mod.get_global_var('func_6267')
call_10553 = relay.TupleGetItem(func_6265_call(), 1)
call_10554 = relay.TupleGetItem(func_6267_call(), 1)
output = relay.Tuple([call_10539,call_10551,call_10553,])
output2 = relay.Tuple([call_10540,call_10552,call_10554,])
func_10556 = relay.Function([], output)
mod['func_10556'] = func_10556
mod = relay.transform.InferType()(mod)
mutated_mod['func_10556'] = func_10556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mutated_mod.get_global_var('func_10556')
call_10557 = func_10556_call()
output = call_10557
func_10558 = relay.Function([], output)
mutated_mod['func_10558'] = func_10558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6352_call = mod.get_global_var('func_6352')
func_6353_call = mutated_mod.get_global_var('func_6353')
call_10639 = func_6352_call()
call_10640 = func_6352_call()
func_6542_call = mod.get_global_var('func_6542')
func_6544_call = mutated_mod.get_global_var('func_6544')
var_10642 = relay.var("var_10642", dtype = "int64", shape = (672,))#candidate|10642|(672,)|var|int64
call_10641 = relay.TupleGetItem(func_6542_call(relay.reshape(var_10642.astype('int64'), [6, 14, 8])), 0)
call_10643 = relay.TupleGetItem(func_6544_call(relay.reshape(var_10642.astype('int64'), [6, 14, 8])), 0)
func_8558_call = mod.get_global_var('func_8558')
func_8560_call = mutated_mod.get_global_var('func_8560')
call_10644 = func_8558_call()
call_10645 = func_8558_call()
func_9464_call = mod.get_global_var('func_9464')
func_9466_call = mutated_mod.get_global_var('func_9466')
const_10654 = relay.const([4.600861,-3.497846,4.079321,4.422197,8.691066,-2.694969,6.437390,-2.030729,-3.883417,1.450254,-2.895795,8.026905,4.191088,7.967374,-7.866023,5.921826,8.721502,7.641785,-2.408944,-7.807680,9.463785,-9.144387,-6.693864,3.258880,-2.124091,-0.106538,2.839787,-6.482680,6.254711,2.525938,8.186207,-7.605237,-6.730438,0.687380,-5.360304,3.518002,-1.259193,-5.133730,-0.205769,7.664152,-6.198894,1.532382,5.476685,-2.688194,-2.296676,-4.436706,-5.823684,-8.605514,8.921306,3.642633,4.424380,1.192480,-6.656345,-4.275537,6.298382,5.108360,9.387817,6.226267,1.298236,-5.101477,8.708165,5.687327,3.194722,3.688100,3.584982,-4.152919,3.774267,-1.951655,5.089803,-8.107633,-9.543039,-9.163633,-3.731084,6.889680,7.366102,9.544003,-9.257071,0.377052,-2.677634,-3.920857,9.571818,-5.213732,-5.865896,8.243629,-6.681757,3.855921,2.052290,-4.345413,1.140920,9.164666,9.362266,-6.028501,5.049751,4.576906,-6.176077,5.405368,-7.930600,-3.005270,-5.039116,-5.514016,5.160604,-7.234682,6.049510,-3.171964,-5.980207,-9.713466,5.994157,8.196552,-1.171937,-5.391406,9.405997,-4.894363,-2.984588,-0.799972,-5.434976,3.655044,-7.887217,8.972671,-0.031090,3.668273,5.872709,2.105018,-0.390661,-9.013697,1.913575,3.458868,-2.294969,7.723781,-2.110793,-4.802333,-7.451203,-1.520327,9.300782,0.581805,8.630302,-8.113384,-5.500274,9.070287,-2.759316,1.956218,6.732349,-6.604730,-6.934051,-1.451941,-5.676293,-8.849610,-6.385823,1.984183,-5.932792,1.003186,4.739698,-3.464433,9.448775,-5.210270,9.933422,-9.996131,-2.249469,3.774453,-8.773861,8.877540,-1.768489,9.389087,-2.888592,-5.422723,1.102118,4.196934,9.498220,-3.844111,6.205740,-5.953229,-7.029424,3.484532,-7.971425,-4.440721,-3.502913,3.766709,8.429156,2.784249,0.265242,-7.203322,-8.169344,-6.703882,8.298912,-1.461388,0.303990,-4.358450,1.008485,2.011769,-6.121086,-8.288667,2.415226,3.030717,5.547956,6.679002,-5.416657,4.850255,0.185572,-7.601985,9.035259,2.681084,4.363454,-2.074814,-9.291416,-8.632058,1.511080,5.201222,-2.146610,5.982729,-1.398172,2.194575,-5.284558,8.900509,-1.857227,5.680983,-9.841976,-6.631515,-7.380911,3.163095,-2.847293,7.836109,-0.254878,5.223923,1.273730,-8.704212,3.982811,-0.047717,8.564644,7.426037,4.236436,6.067852,7.905771,0.341860,-0.669204,-9.861337,9.619308,2.507844,1.227158,-0.723271,8.053744,-8.662613,-1.028490,1.480384,-6.893515,9.406656,9.563577,1.427453,9.491701,-5.437946,5.082283,-2.098917,-5.799478,0.616759,-2.514706,-3.818232,-1.854804,-2.595751,4.715564,-8.216051,-3.490205,2.960777,-7.048230,8.105367,2.030362,-0.900970,-1.141140,4.855367,-2.612563,-2.182417,0.179301,-0.887130,3.140970,-1.498951,-8.507552,-0.174394,0.414382,-5.362801,7.888875,7.886929,4.289731,7.341103,-1.194097,-8.300263,6.535764,-9.145880,3.283308,7.467664,3.014046,0.122562,-5.516924,8.749399,2.710446,-0.671017,8.743644,-0.357795,9.945656,-1.327624,-5.958858,-5.609039,-5.223190,-5.248659,2.316041,-0.949384,-6.299700,4.024009,-1.589626,-0.483671,-9.247876,-0.962202,-6.871241,8.015907,-4.805644,6.462068,-6.479507,4.355724,-5.827921,4.272642,4.799564,3.181420,7.405743,-4.663020,7.457226,-7.563396,1.434339,2.466265,2.229810,1.628103,-7.738912,-8.644778,-3.386195,3.728951,-8.125440,4.882183,2.898003,8.258875,1.363307,-1.178550,-6.192047,-0.815584,3.366778,1.238362,-2.136145,-7.041646,6.166344,-5.809617,-9.687919,5.654878,-2.837838,-3.716606,2.876913,-5.190816,-4.878114,9.627464,1.418664,-0.390612,9.117568,8.166195,7.309500,-6.608833,8.678312,-2.701353,2.814863,-5.667065,-4.153686,4.097617,-6.955126,-9.782942,-0.796511,9.856871,-1.045607,-0.806347,5.143508,6.041257,2.825816,6.198629,-7.826925,3.892691,0.301621,1.988743,-7.359092,8.738439,1.170826,4.691345,1.337213,7.888028,3.730435,7.572579,-0.575752,8.241332,7.405730,-3.204734,-3.858931,0.316810,0.917529,-9.303237,3.023656,-1.641727,0.043083,-9.488069,-1.355550,-9.646649,9.452873,-8.714552,2.351276,2.310126,-7.603292,-6.375739,2.862315,2.214567,3.524286,7.834139,0.908907,3.635695,6.254229,-1.253333,5.258155,7.244813,-9.877573,-2.863573,3.161683,-9.321833,2.011954,4.040959,-4.549000,5.273810,-2.259792,-4.725651,-8.132677,-3.759224,0.573180,8.843277,-8.346914,8.378579,-7.260568,-6.521368,-0.482113,-5.250193,6.016650,-0.302667,-4.401524,5.740138,-2.414262,-2.358208,5.877068,1.227560,8.699353,-4.494613,3.705948,7.057371,4.433781,-6.366735,-9.258174,-5.518797,-8.556974,-2.100486,-8.917466,0.006334,4.181914,-6.759516,-7.567976,-3.973822,-5.850560,3.336437,-9.820956,-7.378390,-1.833628,8.222276,6.076999,5.157828,7.896946,-9.485447,0.745577,-1.531869,6.580447,-4.297954,-8.510997,-9.533630,2.457791,8.355755,-8.529934,4.946816,-2.142216,0.667821,-2.672971,3.285836,-8.087832,-5.416474,3.921430,7.239937,6.071419,-8.608534,-2.066808,-7.946432,9.661056,4.395436,2.289467,-7.463879,-6.039207,5.525518,-4.149334,-9.246073,-9.642435,8.115569,2.604516,4.798854,-4.660060,5.407611,-1.013663,-2.905918,9.161256,3.328977,-9.668269,-7.502570,0.710376,-9.477048,-0.125147,5.378682,1.753164,-9.223031,3.169272,4.599476,7.880341,-2.896955,-7.611309,9.446964,-2.989640,3.779994,0.289859,6.981464,6.748020,-9.471959,-3.148138,9.888112,-7.988429,7.164041,3.735702,5.350676,8.957803,-2.242076,-4.564021,0.580782,-1.524854,-7.156682,-7.467517,-1.532683,1.615168,4.391239,-0.805966,4.775848,-9.415602,-8.898083,7.485124,-0.343706,5.876185,-5.355151,0.086096,1.951563,-9.472288,9.599590,2.059687,7.992699,-6.216220,9.654555,0.118683,-3.094535,3.680067,3.026114,-8.253694,4.682030,-7.807910,-9.376991,3.922391,6.053525,6.339571,-6.722849,-7.152244,6.666875,-6.467689,-0.159346,2.312109,6.095275,0.827610,1.475853,-7.245299,-8.531567,-1.244569,-7.479619,-5.021057,-9.055611,-5.305063,-1.307973,-3.292440,-4.559084,-2.044653,-3.837133,1.435934,-7.349649,-2.058611,-8.311215,-0.658457,2.856302,2.811211,-8.852859,6.276318,3.136331,5.036226,-6.027541,2.917990,-5.349207,1.076584,1.702127,-7.044875,-1.396029,3.188120,-8.277559,4.334028,5.703571,8.388401,-5.294121,-3.514060,5.490994,7.217741,7.877420,-5.712256,6.387299,-5.276785,-3.655547,-9.791751,1.454221,3.294226,-2.430223,2.646467,-2.533317,4.667957,6.201299,-1.665649,-5.993845,-7.139981,8.859917,9.060665,0.058301,5.166221,1.146458,-5.132772,-4.879482,-2.198961,-4.759146,-0.307746,-1.677031,1.902725,8.210760,-0.067716,3.605553,2.785132,3.261089,8.471509,-0.889882,-7.973899,1.654716,-2.237485,3.158151,-0.308112,-3.948693,-3.966222,-7.806886,-6.788296,6.953638,0.996988,1.071599,6.265977,-5.963123,7.752229,-1.837188,-3.960103,-0.862930,3.466561,4.365454,7.170789,-2.228567,-2.279540,6.034580,-7.015711,-9.122453,-4.409361,-9.946052,-3.419804,-1.937884,1.293694,-9.423512,-7.987307,-7.366330,-7.509874,9.764716,9.413688,0.501764,4.509508,-6.228286,5.145922,6.646119,-1.862090,-4.852953,-2.192229,4.896734,5.499647,3.307701,-1.849849,9.124716,5.888868,1.049172,-5.811047,3.778289,0.515273,4.788723,-9.480481,-5.372786,-9.628835,3.578674,-0.035393,-8.762388,-7.387399,5.271093,3.726566,6.712525,-2.481499,4.309327,3.671256,-5.634171,-7.757848,-4.496648,-3.984255,3.406772,7.069623,-4.105503,5.904592,7.521501,-4.555919,8.270541,8.835658,4.863488,6.763840,-5.565596,8.752324,9.428590,-7.368232,-7.943933,4.462680,7.749587,-2.115346,-9.791378,-9.653683,-1.753715,-7.165998,-0.213653,-9.271065,5.670922,-8.116129,0.883578,-9.180310,0.802719,-1.925727,-7.225517,6.884700,-9.071435,6.023678,-6.273909,-0.290522,-2.035620,-0.137756,-3.980396,-5.818426,-7.925035,6.955809,-8.244488,-2.286050,-4.491400,5.999209,-6.166329,-9.269274,7.612243,3.767279,0.175089,-1.473531,6.376979,-5.929843,9.368160,3.044241,5.291880,6.547214,3.101002,7.844561,-8.706322,-0.286723,7.928175,6.820412,-4.402522,-0.485703,-3.130223,2.943490,3.489142,1.162119,2.447911,-2.454704,7.253517,-4.720330,-4.810257,-5.535039,7.358029,7.597404,4.394510,4.060789,-1.949173,7.718842,-4.359121,-1.205093,-6.764986,-3.793331,-4.526158,-3.929683,7.656845,-9.166952,-9.545724,-8.555947,9.182092,8.537810,5.597551,-7.332033,-8.687236,-6.945629,4.873408,8.839914,3.994109,4.813908,-2.256216,4.257153,-9.273023,7.000334,1.295129,-9.467391,-0.364080,6.091709,-1.252649,2.680781,-7.741430,3.327564,-3.404739,6.842290,8.805069,7.841399,2.048096,5.257614,5.269470,-9.701798,-4.530844,0.004969,-7.968383,-8.170290,2.304070,-8.376222,-6.912690,4.051634,-9.066625,-1.283348,3.891894,2.637559,-9.041041,-4.536617,-8.744601,-0.129111,-1.247394,7.161744,6.440706,3.678771,3.068286,-8.867446,-0.370024,-1.297865,-5.212309,-1.498694,-2.155964,-9.922887,-2.946454,-3.221748,-9.805279,3.142595,1.296615,6.702934,3.492967,3.936215,-2.294028,-0.973460,7.839874,7.726346,9.621754,0.158761,-7.576748,-6.490706,-8.326650,7.566397,-9.815962,6.622150,0.817227,-0.571352,-6.284507,8.013796,3.562644,2.570582,-0.856364,-6.512318,-0.058339,9.543933,-6.624704,7.444047,1.833760,3.841403,0.669010,9.232642,8.097284,9.948036,2.406485,5.332744,-8.504243,5.926709,3.613017,-7.730066,1.332111,-4.981987,-0.008686,-1.173254,-9.613507,0.566539,5.712505,-2.762983,-7.112014,-0.760741,-9.557166,-9.965487,-9.016484,0.751798,1.021797,4.352353,-5.836527,-2.787407,8.615145,-9.002868,-9.211677,3.704216,-9.909803,5.272703,-8.211381,-9.841127,8.365633,7.207887,-8.174007,1.758580,0.875816,-2.349460,2.006494,-8.633217,3.775723,-8.062013,-8.613322,3.421557,-9.093337,0.282432,-2.567688,3.413329,-7.647318,7.598760,-9.905056,-5.160527,1.441843,9.192311,-3.954959,6.434660,-7.699540,6.914047,-6.720279,1.723936,3.309016,4.231436,-7.967484,0.417422,0.197010,5.176823,-9.934423,6.107205,-0.181304,-1.195751,-2.748136,-7.187204,8.185121,1.144934,1.873770,-1.381002,0.554722,-7.438395,8.073344,-6.709469,4.569715,-1.966437,-4.670596,3.447040,-0.573389,5.099995,-2.253403,6.168307,8.290070,5.409453,6.785925,-5.778963,5.394637,-1.583573,-0.031711,9.311861,-4.233415,9.347228,-1.774591,8.537373,-1.296061,2.387329,-8.860515,8.663763,-7.093933,-5.795980,-4.521261,-2.769371,-6.666583,-7.346392,-0.406765,-4.245428,6.771899,9.827579,-4.787225,-2.104631,3.876909,4.220428,-6.792732,1.742674,9.338350,-1.449168,-2.513165,7.034647,3.823242,-9.757045,-1.065313,-6.083358,-7.768352,1.325014,-7.961991,-1.948040,5.613609,-9.706756,-6.963765,-4.451306,2.857762,9.012174,-0.940881,-4.511695,4.937952,0.898672,9.104031,4.504501,2.351709,9.340436,6.402756,8.254424,3.581359,-2.841965,6.742721,-0.019526,-3.099913,3.095846,-4.731927,-7.291318,-9.294407,5.519167,-7.983223,3.842736,3.894111,1.032280,-6.282901,-5.156536,-0.919640,4.200703,6.663587,1.177103,-3.838127,-4.584112,-2.048697,-9.293852,-8.335425,1.835103,-6.918844,-2.157879,4.285339,-4.669923,-8.812641,3.102139,-3.919222,2.091047,-0.730868,7.596618,8.031589,-2.962110,-8.936153,-2.087168,-1.577076,2.172666,-7.137307,0.343485,-4.702116,-5.491489,-7.391184,3.643242,-6.240645,-6.042886,8.212789,9.184746,-5.196881,7.198569,-3.805956,2.982292,9.673524,-8.568790,6.007084,1.003232,4.170549,-6.736576,4.228185,-1.870623,-6.458904,0.409181,-8.606290,-1.225425,-0.907659,-1.826592,9.093735,6.590618,-0.605780,5.036520,5.543499,5.521213,-4.851154,-5.632740,-0.634894,6.407776,-4.298677,-5.253084,-9.797369,1.950002,-5.396739,2.954692,0.106898,-2.009202,-6.885001,8.075205,-7.803174,9.451984,5.154052,3.023584,-5.717921,-1.763033,3.837481,-0.549742,-4.820734,-8.558110,9.428993,-3.940862,-4.722895,-4.208369,-6.153155,3.689799,3.514944,9.547675,-1.613614,-1.804117,-1.265933,5.286111,3.605278,0.918717,2.405490,3.904780,1.547317,-6.110993,-5.123947,8.733113,-5.162231,-0.974479,7.439857,-9.653742,-2.731305,-8.382501,-6.340498,-5.537416,3.192953,1.269147,8.876046,4.909916,-0.318969,-8.584020,0.506083,-2.299859,-7.964515,5.305109,-0.991993,-5.548710,-0.043862,3.023135,-4.842008,-4.425053,7.139486,0.135731,-3.874383,-6.893369,-5.564704,-0.205954,-2.801710,7.915402,1.931756,-2.707613,0.765028,-9.467705,2.381010,-2.871381,8.292342,-8.547621,-2.968705,3.112880,-3.106431,4.842809,-2.332007,-8.263234,-6.982869,-9.833847,-1.543147,-3.559894,5.984378,9.127224,-5.838755,-0.207986,7.694480,2.692042,-1.917361,-1.642656,-9.737472,0.960463,0.145025,6.620266,-5.251306,1.724120,-7.905487,-2.653476,-4.713789,-3.791942,1.197660,-4.666687,4.362123,-6.719176,-8.734824,1.408612,-4.815198,-5.764672,-2.551546,-3.549484,7.537765,-5.145876,4.670015,2.897379,-4.728554,-3.155198,-5.211456,-1.340774,-1.687443,-6.477086,-9.636662,2.138937,-5.863086,-1.391797,9.295601,6.388446,0.620862,-9.879893,-5.491826,-7.840561,-5.918065,-9.713565,-5.241627,-8.955401,6.944674,1.615450,-6.163212,5.654011,-0.885748,-9.965173,-9.052769,-3.223373,8.537336,-5.559186,-8.118249,-9.140341,6.900839,-3.391254,-7.465019,2.030562,3.137401,4.963010,4.348334,-9.586682,-0.713978,-5.994283,6.422692,-4.792144,2.185616,-4.133800,-8.456464,-2.335021,-8.855601,0.473724,-1.776593,-7.890045,2.385370,7.259213,-0.483271,6.015397,-3.705216,6.985838,-1.439173,-2.626977,-1.543092,-4.160201,-4.010935,3.567229,2.472779,4.079478,9.768271,1.265045,1.878808,5.907610,-4.323695,-9.094726,-9.446675,-3.188227,-7.138489,3.409374,-4.494255,5.763574,-4.163257,0.100985,5.244906,4.530179,-9.574428,8.593159,-4.201162,-1.009528,9.420170,3.163270,-3.566352,4.146154,2.960166,-4.078520,-2.128229,-6.903304,-1.793320,-6.455660,-7.254923,-3.408945,-8.153844,-6.218915,-5.195279,2.637900,4.960162,-0.101487,3.890157,-0.225880,-2.259496,-7.216748,-8.696302,8.992741,-6.278405,-9.188005,-0.058565,5.853835,3.227560,3.071278,-1.790495,7.295220,4.529596,-6.261502,9.950715,5.779607,9.299950,-4.768584,-4.483073,-6.431323,0.668321,2.883355,9.969261,-4.171880,-0.088544,-1.856026,1.512094,1.903407,8.918639,2.281320,-3.057642,-8.414031,-8.152200,-6.631356,1.981052,9.859791,2.784426,-7.634522,6.947941,5.169482,-9.137487,8.137992,-9.210731,-0.968873,-9.834085,-0.532894,4.421394,-3.156420,-9.579247,-2.946511,8.189642,-9.350058,3.890757,3.095474,-9.090926,-7.122169,-4.087501,-6.420808,-6.893212,9.684733,-0.774201,-2.955231,-8.412914,7.366589,3.286022,-0.092914,0.864137,6.951344,9.501462,6.554225,-1.549122,-2.706612,7.143957,8.719788,-3.781195,-3.044997,-2.301035,-0.899321,9.181609,1.081192,2.477830,5.085224,9.111822,8.453044,5.775421,-1.128262,1.324070,2.511123,1.993217,-8.620190,4.251187,-2.132647,5.191313,-7.761751,-3.967213,3.607556,-6.512014,-1.114474,-5.104582,-8.202803,-9.252172,9.430391,-1.020458,7.339574,7.390339,6.500291,-5.712412,-3.496434,-3.319465,4.630631,9.615752,-3.664990,1.172081,8.419168,9.739333,-6.409930,-4.971353,0.944583,-8.481313,-3.582844,-5.539476,-7.629589,5.281632,1.680854,0.332198,-0.650236,0.969589,-7.911736,7.895076,-3.174689,-9.280417,-5.512722,-1.693198,0.186175,-8.674246,-3.274732,5.519916,-6.814214,-9.385660,-2.042702,-5.598522,-2.803056,6.875733,-2.121047,-7.360158,9.157351,3.282789,0.721458,9.820347,-5.652199,-8.375990,0.708372,6.566224,-0.468093,5.868123,-3.291249,7.127924,6.003154,9.842351,5.944996,9.673860,-0.628012,-4.281049,-7.782338,-4.012995,-4.334718,-5.330398,-4.816556,8.404306,2.257297,7.414003,-8.989056,-4.804071,-6.645013,4.576250,0.649185,-7.120367,-1.249596,1.124521,7.127811,8.225327,-5.867876,5.135292,-1.472075,5.740491,0.541632,8.956593,0.607681,6.789001,6.311821,3.627544,9.637528,6.128752,-1.731536,0.915774,-5.112108,3.448785,-2.661283,-1.392445,3.755343,-3.091147,-8.082910,-5.674587,8.290696,4.733718,6.372313,1.805269,0.963920,-3.930520,2.541400,4.584453,-3.404215,-6.496458,2.025062,0.360078,-8.144852,3.843127,2.538860,-9.210551,5.304872,-3.896347,-2.508716,-6.238237,-3.824427,9.647607,-2.511698,0.740255,-3.767616,1.015037,-2.177336,-3.390200,-6.328940,-6.976051,-8.292343,-5.394039,-3.090353,-2.975534,-2.188616,-8.272165,1.713818,-8.734516,-2.917541,-5.117172,1.997178,-6.335179,8.014459,-3.151538,-7.667972,5.739422,2.579962,6.195903,-4.369669,-1.604099,-4.919703,5.479607,-6.572470,2.398888,-3.173087,8.673421,7.775414,0.457058,5.407124,-7.435929,-8.977715,-5.711001,5.778022,-7.735153,7.330882,-8.488683,2.963631,2.439436,9.809528,8.956292,-8.693848,9.583892,-5.768484,-2.674011,-3.034258,-9.492205,6.259422,-6.286859,-1.189532,-6.063685,4.384844,2.364090,3.702133,-2.024047,7.857624,-4.743458,8.073434,2.169885,-6.658049,4.909833,-2.284509,-4.119819,-7.012443,-9.530694,3.180025,-4.880025,7.052796,5.487027,-9.921965,9.626292,0.024265,3.606086,1.665552,2.952807,8.758510,-0.911270,-1.448363,6.644963,3.661762,8.394467,-6.400706,3.202885,0.173898,-3.469633,-6.111051,4.767021,7.496245,-5.151895,3.497940,7.435309,-3.552884,-7.955795,-0.057712,3.866833,3.930249,-9.251814,-6.148959,0.195326,-2.834798,8.845554,6.835718,1.135176,-8.348226,3.687376,7.095531,-1.730213,-2.985027,-0.297495,-5.953554,-1.508046,-9.442865,7.065478,-2.010198,-4.988212,4.300748,5.636836,-9.224188,8.523928,1.610372,-2.850901,0.234268,-5.734711,9.469338,-9.199334,6.470340,7.440216,1.353164,-6.364774,4.478993,2.007302,6.990600,2.330392,7.673035,-3.805533,3.815201,2.974882,1.457701,-3.752153,-8.947119,-6.752781,3.337554,4.868910,-3.662215,-3.088936,-1.741191,-2.089993,-5.544174,3.728269,2.722082,-4.307875,-6.945899,0.520366,-6.841182,-1.183725,6.434189,-6.579449,-1.036295,8.249513,5.781544,-0.232733,9.958850,2.490823,-5.617878,4.079286,-7.521398,-7.958968,2.059737,-9.284505,0.135898,-4.512838,3.205710,4.593170,-0.267398,8.798161,-3.514125,1.410390,-1.445163,0.807104,0.419148,-9.702818,3.286999,-2.985317,4.338377,-2.113031,6.557608,0.286573,4.710822,-7.369920,1.180989,1.105007,7.108575,-3.174280,-8.601067,-9.758184,-2.393881,0.127514,4.773823,4.719891,3.988917,2.267633,-6.888797,7.242636,4.480766,-6.105418,4.384637,-5.730570,-1.332304,9.222462,8.766436,5.595320,-8.569848,8.359314,-5.404562,-0.772054,-5.712193,4.751982,-2.153461,-7.417864,-2.416245,2.970827,-1.304788,9.254442,-9.879878,7.991568,-3.257886,5.799328,-2.036270,8.908583,3.288545,-7.632740,1.289463,6.980545,-3.176748,-9.195453,-7.356057,3.224593,5.099786,6.191939,3.127811,4.353975,6.763871,-5.354222,3.402520,3.693863,-9.666661,-4.915349,2.798240,6.423863,2.802873,-0.451946,3.181117,2.105865,-5.163036,-5.268709,4.911556,-4.846628,6.332039,-6.265776,-5.033775,0.164294,6.765882,-4.494711,4.164773,8.817572,1.233813,-3.357370,1.192172,-3.081955,1.869087,9.828681,-9.872768,8.219107,-8.976749,0.049145,7.881097,8.687415,-8.507542,4.780932,-2.836666,3.628612,2.606373,-9.409069,4.969681,-9.114896,-1.959537,4.226798,4.413102,-7.832375,3.372100,-8.318545,-8.880418,6.365846,-1.970804,5.246231,7.023111,-4.167562,-6.720190,8.865430,1.098863,-5.396160,0.136326,5.672267,4.833273,6.589817,6.297624,8.216724,3.897154,-6.490646,-6.600478,-6.396947,-0.912839,-1.801412,-7.086293,-3.795583,3.004152,8.350142,6.524030,-8.983865,-6.337699,5.400247,1.563890,0.926513,9.918261,-4.144797,2.167366,-0.300972,-2.017645,1.421231,-3.239001,-9.012063,-4.975743,2.393220,-1.711540,-1.429288,1.808865,-8.782405,0.974808,9.398197,-5.508679,-0.890387,6.601925,3.649274,2.905271,-3.676322,7.154952,2.928246,-3.585032,8.759615,-9.171679,5.114056,4.415300,6.854336,3.026000,1.679721,-7.897555,-8.724113,-0.057699,3.864332,-6.305015,-9.067745,7.077122,0.361413,-0.120692,-7.855830,4.152553,-0.664573,-5.328863,7.575248,-1.160834,6.881322,-8.107728,-2.145691,3.143113,-1.977770,3.051103,1.864438,-6.173872,-3.371473,6.335303,-3.029476,-5.634733,9.962354,-1.687865,7.225112,-5.162422,7.147542,-1.080733,4.891956,-4.982641,8.760504,-4.390708,-6.390473,5.650564,1.932842,1.804167,6.573269,-8.866714,-5.694690,1.149467,-4.679101,-4.321084,-4.591712,8.692830,0.731412,8.198795,-9.406056,7.022359,5.424794,9.235483,-6.890633,-2.613854,2.670151,-4.730561,4.674521,0.003403,0.884928,3.291405,-3.655823,-4.389073,-7.963609,-7.153575,0.594381,9.228852,-7.496856,-0.661519,-7.798596,5.178721,4.247290,1.210272,3.931964,-9.102252,5.490453,6.421456,6.513033,4.927446,5.622544,-5.009141,6.657078,6.182742,-9.948801,-0.883324,-2.990429,-0.767470,-8.456342,-1.139034,-6.769243,-4.782972,6.716309,0.620841,1.028778,-6.387437,-7.587912,-8.548767,0.642700,-2.944831,7.003783,-3.130376,-4.990007,4.509250,-3.245461,-3.972686,0.756552,-3.901999,-3.081708,2.313453,-3.130515,5.294361,-5.510089,4.794488,5.640892,2.448248,-8.677425,6.366363,9.098197,3.277929,-9.329863,-4.138832,5.897612,-9.253860,2.055613,9.525918,-8.986408,-1.314406,-4.922056,-9.182392,4.855639,-0.166261,3.195364,-8.106036,1.049445,-6.261474,-8.855717,6.728160,-3.155519,3.778169,1.878285,3.714825,0.874528,-0.782621,6.907248,-5.881991,-8.493132,5.038506,-5.866885,-1.147995,4.937419,7.683370,-0.010817,0.155718,4.683131,-0.109703,-4.186254,-2.881268,5.249568,4.825737,2.737687,-0.201751,8.210735,7.212959,9.204674,5.683675,-5.773554,-1.452612,0.843627,8.330090,6.223222,0.842080,-6.788104,6.424217,-7.741867,-1.367435,-9.697577,3.425242,-3.395647,7.674677,9.519700,6.062010,-3.268258,-3.344482,9.591335,-9.338891,3.022747,-3.248257,0.799957,8.035533,9.173094,0.055484,-8.232432,1.644626,2.117819,5.084090,6.580511,-0.184150,-7.350022,1.402615,7.154146,-9.597551,6.973761,-8.287060,1.996790,-3.379982,9.253168,-3.294356,-8.869189,3.378843,9.538559,-2.932977,0.938802,-9.998549,8.892423,7.322390,4.283667,2.500483,8.692118,0.212912,-7.438809,2.833236,3.402590,3.098208,3.966912,7.925477,0.659769,0.334628,-4.890407,6.959019,3.659871,-7.382641,-8.607476,8.900816,3.147136,-8.732327,-1.514275,-3.112429,-9.727533,4.627830,-6.468407,-4.746877,7.452617,-2.950243,4.271155,5.618230,-4.964530,9.459546,-8.954016,-2.007181,7.362923,0.469898,-5.958024,5.636381,9.805847,-6.455289,8.184540,-4.905807,-6.283962,-2.020300,-0.208366,-6.539871,-1.994134,9.899784,-1.710535,-5.226337,6.891559,1.618036,0.063538,-4.781704,-6.905903,-4.003807,1.604527,-7.373501,2.533578,2.706738,-7.886527,7.540263,7.469891], dtype = "float32")#candidate|10654|(2240,)|const|float32
call_10653 = relay.TupleGetItem(func_9464_call(relay.reshape(const_10654.astype('float32'), [280, 8])), 0)
call_10655 = relay.TupleGetItem(func_9466_call(relay.reshape(const_10654.astype('float32'), [280, 8])), 0)
output = relay.Tuple([call_10639,call_10641,var_10642,call_10644,call_10653,const_10654,])
output2 = relay.Tuple([call_10640,call_10643,var_10642,call_10645,call_10655,const_10654,])
func_10672 = relay.Function([var_10642,], output)
mod['func_10672'] = func_10672
mod = relay.transform.InferType()(mod)
mutated_mod['func_10672'] = func_10672
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10673 = relay.var("var_10673", dtype = "int64", shape = (672,))#candidate|10673|(672,)|var|int64
func_10672_call = mutated_mod.get_global_var('func_10672')
call_10674 = func_10672_call(var_10673)
output = call_10674
func_10675 = relay.Function([var_10673], output)
mutated_mod['func_10675'] = func_10675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5444_call = mod.get_global_var('func_5444')
func_5445_call = mutated_mod.get_global_var('func_5445')
call_10720 = func_5444_call()
call_10721 = func_5444_call()
func_8661_call = mod.get_global_var('func_8661')
func_8663_call = mutated_mod.get_global_var('func_8663')
call_10725 = relay.TupleGetItem(func_8661_call(), 0)
call_10726 = relay.TupleGetItem(func_8663_call(), 0)
output = relay.Tuple([call_10720,call_10725,])
output2 = relay.Tuple([call_10721,call_10726,])
func_10734 = relay.Function([], output)
mod['func_10734'] = func_10734
mod = relay.transform.InferType()(mod)
output = func_10734()
func_10735 = relay.Function([], output)
mutated_mod['func_10735'] = func_10735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9671_call = mod.get_global_var('func_9671')
func_9673_call = mutated_mod.get_global_var('func_9673')
call_10736 = relay.TupleGetItem(func_9671_call(), 0)
call_10737 = relay.TupleGetItem(func_9673_call(), 0)
func_3750_call = mod.get_global_var('func_3750')
func_3754_call = mutated_mod.get_global_var('func_3754')
var_10741 = relay.var("var_10741", dtype = "uint16", shape = (448,))#candidate|10741|(448,)|var|uint16
const_10742 = relay.const([True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True], dtype = "bool")#candidate|10742|(2145,)|const|bool
call_10740 = relay.TupleGetItem(func_3750_call(relay.reshape(var_10741.astype('uint16'), [448,]), relay.reshape(const_10742.astype('bool'), [2145,]), ), 2)
call_10743 = relay.TupleGetItem(func_3754_call(relay.reshape(var_10741.astype('uint16'), [448,]), relay.reshape(const_10742.astype('bool'), [2145,]), ), 2)
output = relay.Tuple([call_10736,call_10740,var_10741,const_10742,])
output2 = relay.Tuple([call_10737,call_10743,var_10741,const_10742,])
func_10759 = relay.Function([var_10741,], output)
mod['func_10759'] = func_10759
mod = relay.transform.InferType()(mod)
var_10760 = relay.var("var_10760", dtype = "uint16", shape = (448,))#candidate|10760|(448,)|var|uint16
output = func_10759(var_10760)
func_10761 = relay.Function([var_10760], output)
mutated_mod['func_10761'] = func_10761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_10769 = relay.TupleGetItem(func_2994_call(), 0)
call_10770 = relay.TupleGetItem(func_2996_call(), 0)
func_8645_call = mod.get_global_var('func_8645')
func_8650_call = mutated_mod.get_global_var('func_8650')
const_10772 = relay.const([[-4.329249,7.070093],[-5.771545,-7.965045],[6.489187,2.187360],[5.887804,5.165514],[6.058713,-4.394924],[-7.704353,-2.038594],[9.017076,0.237838],[-5.556613,5.151093],[3.829430,6.099923],[6.782559,-2.950078]], dtype = "float32")#candidate|10772|(10, 2)|const|float32
var_10773 = relay.var("var_10773", dtype = "int16", shape = (975, 1))#candidate|10773|(975, 1)|var|int16
call_10771 = relay.TupleGetItem(func_8645_call(relay.reshape(const_10772.astype('float32'), [20,]), relay.reshape(var_10773.astype('int16'), [975,]), relay.reshape(call_10769.astype('float32'), [325,]), ), 5)
call_10774 = relay.TupleGetItem(func_8650_call(relay.reshape(const_10772.astype('float32'), [20,]), relay.reshape(var_10773.astype('int16'), [975,]), relay.reshape(call_10769.astype('float32'), [325,]), ), 5)
func_5788_call = mod.get_global_var('func_5788')
func_5794_call = mutated_mod.get_global_var('func_5794')
var_10782 = relay.var("var_10782", dtype = "uint64", shape = (1792, 1))#candidate|10782|(1792, 1)|var|uint64
var_10783 = relay.var("var_10783", dtype = "uint8", shape = ())#candidate|10783|()|var|uint8
const_10784 = relay.const([10,-10,9,-4,-9,-5,-2,-8,-9,5,-1,-6,3,-5,1,-1,-3,6,6,-6,8,2,4,-2,-8,-6,10,-5,4,-4,-9,7,-5,-8,5,-5,-9,-5,-8,5,4,7,3,-8,2,-3,-6,-7,-5,5,-8,5,1,10,4,7,9,1,6,1,3,2,-4,4,1,9,10,-9,-5,10,8,-7,-1,-9,10,-6,-3,4,-5,-5,8,10,-10,-10,-1,4,10,-4,-2,10,4,6,-4,3,9,-10,3,-4,10,-10,4,10,-7,-7,-1,2,-2,-3,9,10,5,4,1,-5,-3,3,10,3,8,-6,-6,-4,-9,5,-2,-7,-4,-9,10,-5,8,2,1,-5,5,10,2,-10,-1,-10,-1,-4,-5,-9,6,9,3,-3,-7,5,-2,3,-1,6,9,8,10,-4,-4,1,8,5,-9,8,-9,-10,-8,-6,8,-2,7,-7,-10,3,4,6,-3,-5,-3,10,6,2,3,-4,9,7,3,-2,-5,-1,-6,2,9,-4,2,4,-6,-3,-6,1,4,1,4,-4,-6,-9,-1,-4,2,-5,-3,-4,7,7,6,-9,6,10,3,10,-9,4,3,2,-7,10,8,-9,1,8,-4,2,9,3,-7,1,-3,8,6,-9,-7,-5,3,7,1,-3,-4,-6,-6,5,1,9,-3,-10,-7,2,-8,-8,-10,-6,2,-6,4,-9,3,6,-2,-10,4,-3,-8,6,3,-8,-8,-6,4,9,5,2,4,4,5,-2,-5,-3,-2,-1,-10,10,1,-2,-7,5,-3,-10,5,4,9,10,-10,6,-1,-7,-6,-2,-2,-2,-7,10,1,8,5,7,-9,9,1,1,4,4,-6,7,-1,6,-5,10,8,4,-2,-1,-8,-10,8,1,-1,2,-1,5,5,10,10,7,-1,-1,-10,4,3,-8,-7,-2,4,-6,-10,-7,-4,6,10,-10,-2,4,5,3,3,-8,-2,1,-6,-1,9,3,6,5,-3,-6,8,-1,9,-1,-5,5,3,5,2,-6,-5,-2,10,-8,-4,10,-6,5,4,8,-6,9,8,9,-2,-10,-5,10,10,8,4,-8,-8,-4,10,4,-4,7,8,1,-10,7,-3,-1,-6,-9,-7,-1,-9,-7,-8,6,5,5,1,3,6,7,6,-2,-8,-3,7,10,-2,6,-10,-5,8,-10,5,-10,-1,8,-8,-2,-1,-9,-2,6,-6,5,7,-2,-7,3,6,-10,-4,-6,9,7,4,10,-5,-9,1,10,3,2,-6,1,2,-1,-2,-9,7,-4,-3,7,1,2,10,-9,-4,3,9,2,-7,-8,-1,1,4,-7,10,-7,-9,-4,-1,-4,-5,6,10,5,-2,6,9,-1,5,-2,-3,-9,-9,3,-7,6,-3,5,-2,-1,-3,-10,-6,-7,-9,9,9,-6,10,-8,-8,8,9,-3,4,-7,-2,-9,-10,-3,-9,-2,-8,-7,-10,5,1,7,5,-1,5,3,-7,-8,-3,7,-1,10,-9,-10,-4,-9,6,-5,8,-9,-5,2,9,10,-1,3,10,-3,-10,10,-6,1,4,3,1,7,-6,-2,1,6,1,-3,-1,-1,-9,-7,9,7,5,7,3,3,-5,4,-7,7,8,-10,-6,3,4,-10,-9,8,8,9,-1,9,-7,1,3,-5,-8,1,-8,1,4,6,-10,-7,-2,-8,-9,1,1,-4,-10,7,-4,1,-3,-5,-4,2,5,-2,6,-2,-10,2,2,6,-3,-9,-3,10,-5,-5,-3,-4,-4,7,-8,-4,-9,10,2,-5,-10,5,-9,9], dtype = "uint8")#candidate|10784|(672,)|const|uint8
call_10781 = relay.TupleGetItem(func_5788_call(relay.reshape(var_10782.astype('uint64'), [8, 14, 16]), relay.reshape(var_10782.astype('uint64'), [8, 14, 16]), relay.reshape(var_10783.astype('uint8'), []), relay.reshape(const_10784.astype('uint8'), [168, 4]), ), 1)
call_10785 = relay.TupleGetItem(func_5794_call(relay.reshape(var_10782.astype('uint64'), [8, 14, 16]), relay.reshape(var_10782.astype('uint64'), [8, 14, 16]), relay.reshape(var_10783.astype('uint8'), []), relay.reshape(const_10784.astype('uint8'), [168, 4]), ), 1)
func_3953_call = mod.get_global_var('func_3953')
func_3959_call = mutated_mod.get_global_var('func_3959')
const_10789 = relay.const([4,-3,-6,9,5,-3,4,-9,-2,-10,-4,-8,4,2,7,-8,-1,-9,1,10,-4,9,10,6], dtype = "uint16")#candidate|10789|(24,)|const|uint16
var_10790 = relay.var("var_10790", dtype = "bool", shape = (2145,))#candidate|10790|(2145,)|var|bool
const_10791 = relay.const([-3,-8,-6,-4,10,-3,2,10,1,-1,5,-2,-7,-9,7,10,-8,8,9,-6,-2,1,-8,-7,-1,4,8,2,-8,-2,-6,4,1,7,-2,10,-9,-9,-4,-8,7,-2,1,10,-9,-4,-7,1,10,9,-1,7,-3,-1,-5,1,-4,-6,-9,4,-1,4,-7,-7,3,1,8,-5,6,-6,-4,2,-2,-3,-5,8,7,3,7,3,5,-3,3,3,-4,2,-8,8,-3,8,7,-3,9,8,-5,5,6,4,-8,1,-6,1,-9,3,-7,-9,8,-1,-7,1,2,1,-4,9,4,3,5,3,1,8,-6,4,-9,10,-6,10,-7,-7,-8,4,-8,-1,10,-9,-9,-1,-3,10,2,10,1,9,10,8,4,-9,8,5,5,1,8,10,8,5,-10,-1,6,-8,8,4,9,-4,5,-8,-3,4,-10,-5,6,10,7,-8,3,-9,3,1,-9,2,-4,4,-9,1,3,-10,7,7,-5,-7,1,7,1,8,3,-6,10,6,-8,-1,-2,10,-2,3,1,6,-8,-6,1,1,-3,4,-6,-3,7,5,-4,9,3,-5,-2,6,4,-10,-7,-10,9,4,-4,10,-10,1,2,-1,-1,-1,9,-4,-1,-9,-7,-7,-3,-2,7,-8,-6,10,-10,3,7,-4,-1,-1,-7,1,9,10,10,-9,-3,3,-10,5,3,-9,2,-9,6,-7,8,6,-5,-9,8,1,9,-1,4,6,6,10,-1,-2,6,-7,-5,-4,-9,5,-3,9,10,-8,7,-4,1,10,-2,10,-10,-4,2,-5,-1,8,-9,-3,-8,3,-6,8,-2,3,9,-2,10,3,-4,-3,-1,6,-10,6,1,-5,10,-6,10,-6,3,-9,6,5,10,-4,8,8,-10,-8,-8,9,6,10,-5,4,-4,10,-5,-9,-2,-6,2,2,10,4,3,-6,9,5,-10,-3,-4,-4,10,5,-6,-4,-5,-2,-6,-5,-10,-2,-4,-4,-7,-1,-3,-3,-10,-7,-7,5,-9,1,1,-8,4,9,-6,6,-1,-6,6,7,6,-10,-7,9,10,-1,3,-2,-7,8,-6,-9,-3,-1,-4,5,-4,-7,10,7,5,2,9,-6,7,-2,-10,7,-5,4,-1,-1,4,8,-3,5,-4,5,-1,2,7,-8,-6,-10,-7,10,3,-3,-9,-2,-3,-8,2,-2], dtype = "uint16")#candidate|10791|(448,)|const|uint16
call_10788 = relay.TupleGetItem(func_3953_call(relay.reshape(call_10769.astype('float64'), [5, 5, 13]), relay.reshape(const_10789.astype('uint16'), [24,]), relay.reshape(var_10790.astype('bool'), [2145,]), relay.reshape(const_10791.astype('uint16'), [4, 112]), relay.reshape(var_10783.astype('float32'), []), ), 1)
call_10792 = relay.TupleGetItem(func_3959_call(relay.reshape(call_10769.astype('float64'), [5, 5, 13]), relay.reshape(const_10789.astype('uint16'), [24,]), relay.reshape(var_10790.astype('bool'), [2145,]), relay.reshape(const_10791.astype('uint16'), [4, 112]), relay.reshape(var_10783.astype('float32'), []), ), 1)
uop_10805 = relay.atanh(var_10773.astype('float32')) # shape=(975, 1)
bop_10817 = relay.multiply(var_10782.astype('uint8'), var_10790.astype('uint8')) # shape=(1792, 2145)
output = relay.Tuple([call_10769,call_10771,const_10772,call_10781,var_10783,const_10784,call_10788,const_10789,const_10791,uop_10805,bop_10817,])
output2 = relay.Tuple([call_10770,call_10774,const_10772,call_10785,var_10783,const_10784,call_10792,const_10789,const_10791,uop_10805,bop_10817,])
func_10820 = relay.Function([var_10773,var_10782,var_10783,var_10790,], output)
mod['func_10820'] = func_10820
mod = relay.transform.InferType()(mod)
mutated_mod['func_10820'] = func_10820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10820_call = mutated_mod.get_global_var('func_10820')
var_10822 = relay.var("var_10822", dtype = "int16", shape = (975, 1))#candidate|10822|(975, 1)|var|int16
var_10823 = relay.var("var_10823", dtype = "uint64", shape = (1792, 1))#candidate|10823|(1792, 1)|var|uint64
var_10824 = relay.var("var_10824", dtype = "uint8", shape = ())#candidate|10824|()|var|uint8
var_10825 = relay.var("var_10825", dtype = "bool", shape = (2145,))#candidate|10825|(2145,)|var|bool
call_10821 = func_10820_call(var_10822,var_10823,var_10824,var_10825,)
output = call_10821
func_10826 = relay.Function([var_10822,var_10823,var_10824,var_10825,], output)
mutated_mod['func_10826'] = func_10826
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10842 = relay.var("var_10842", dtype = "bool", shape = (5, 2, 2))#candidate|10842|(5, 2, 2)|var|bool
const_10843 = relay.const([[[False,False],[True,False]],[[True,False],[False,True]],[[False,True],[False,True]],[[False,True],[True,False]],[[False,True],[True,True]]], dtype = "bool")#candidate|10843|(5, 2, 2)|const|bool
bop_10844 = relay.logical_and(var_10842.astype('bool'), relay.reshape(const_10843.astype('bool'), relay.shape_of(var_10842))) # shape=(5, 2, 2)
output = relay.Tuple([bop_10844,])
output2 = relay.Tuple([bop_10844,])
func_10862 = relay.Function([var_10842,], output)
mod['func_10862'] = func_10862
mod = relay.transform.InferType()(mod)
var_10863 = relay.var("var_10863", dtype = "bool", shape = (5, 2, 2))#candidate|10863|(5, 2, 2)|var|bool
output = func_10862(var_10863)
func_10864 = relay.Function([var_10863], output)
mutated_mod['func_10864'] = func_10864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9005_call = mod.get_global_var('func_9005')
func_9007_call = mutated_mod.get_global_var('func_9007')
call_10888 = relay.TupleGetItem(func_9005_call(), 0)
call_10889 = relay.TupleGetItem(func_9007_call(), 0)
output = relay.Tuple([call_10888,])
output2 = relay.Tuple([call_10889,])
func_10914 = relay.Function([], output)
mod['func_10914'] = func_10914
mod = relay.transform.InferType()(mod)
mutated_mod['func_10914'] = func_10914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10914_call = mutated_mod.get_global_var('func_10914')
call_10915 = func_10914_call()
output = call_10915
func_10916 = relay.Function([], output)
mutated_mod['func_10916'] = func_10916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3963_call = mod.get_global_var('func_3963')
func_3965_call = mutated_mod.get_global_var('func_3965')
call_10939 = func_3963_call()
call_10940 = func_3963_call()
output = call_10939
output2 = call_10940
func_10947 = relay.Function([], output)
mod['func_10947'] = func_10947
mod = relay.transform.InferType()(mod)
mutated_mod['func_10947'] = func_10947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10947_call = mutated_mod.get_global_var('func_10947')
call_10948 = func_10947_call()
output = call_10948
func_10949 = relay.Function([], output)
mutated_mod['func_10949'] = func_10949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10914_call = mod.get_global_var('func_10914')
func_10916_call = mutated_mod.get_global_var('func_10916')
call_10964 = relay.TupleGetItem(func_10914_call(), 0)
call_10965 = relay.TupleGetItem(func_10916_call(), 0)
output = relay.Tuple([call_10964,])
output2 = relay.Tuple([call_10965,])
func_10968 = relay.Function([], output)
mod['func_10968'] = func_10968
mod = relay.transform.InferType()(mod)
output = func_10968()
func_10969 = relay.Function([], output)
mutated_mod['func_10969'] = func_10969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8184_call = mod.get_global_var('func_8184')
func_8185_call = mutated_mod.get_global_var('func_8185')
call_11018 = relay.TupleGetItem(func_8184_call(), 0)
call_11019 = relay.TupleGetItem(func_8185_call(), 0)
output = call_11018
output2 = call_11019
func_11032 = relay.Function([], output)
mod['func_11032'] = func_11032
mod = relay.transform.InferType()(mod)
mutated_mod['func_11032'] = func_11032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11032_call = mutated_mod.get_global_var('func_11032')
call_11033 = func_11032_call()
output = call_11033
func_11034 = relay.Function([], output)
mutated_mod['func_11034'] = func_11034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9930_call = mod.get_global_var('func_9930')
func_9931_call = mutated_mod.get_global_var('func_9931')
call_11035 = func_9930_call()
call_11036 = func_9930_call()
func_10218_call = mod.get_global_var('func_10218')
func_10220_call = mutated_mod.get_global_var('func_10220')
call_11050 = relay.TupleGetItem(func_10218_call(), 1)
call_11051 = relay.TupleGetItem(func_10220_call(), 1)
func_2727_call = mod.get_global_var('func_2727')
func_2730_call = mutated_mod.get_global_var('func_2730')
var_11056 = relay.var("var_11056", dtype = "float32", shape = (8, 78))#candidate|11056|(8, 78)|var|float32
call_11055 = relay.TupleGetItem(func_2727_call(relay.reshape(var_11056.astype('float32'), [2, 312])), 3)
call_11057 = relay.TupleGetItem(func_2730_call(relay.reshape(var_11056.astype('float32'), [2, 312])), 3)
output = relay.Tuple([call_11035,call_11050,call_11055,var_11056,])
output2 = relay.Tuple([call_11036,call_11051,call_11057,var_11056,])
func_11063 = relay.Function([var_11056,], output)
mod['func_11063'] = func_11063
mod = relay.transform.InferType()(mod)
mutated_mod['func_11063'] = func_11063
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11064 = relay.var("var_11064", dtype = "float32", shape = (8, 78))#candidate|11064|(8, 78)|var|float32
func_11063_call = mutated_mod.get_global_var('func_11063')
call_11065 = func_11063_call(var_11064)
output = call_11065
func_11066 = relay.Function([var_11064], output)
mutated_mod['func_11066'] = func_11066
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11073 = relay.var("var_11073", dtype = "float64", shape = (13, 2, 13))#candidate|11073|(13, 2, 13)|var|float64
uop_11074 = relay.exp(var_11073.astype('float64')) # shape=(13, 2, 13)
bop_11078 = relay.subtract(uop_11074.astype('int64'), relay.reshape(var_11073.astype('int64'), relay.shape_of(uop_11074))) # shape=(13, 2, 13)
func_8351_call = mod.get_global_var('func_8351')
func_8352_call = mutated_mod.get_global_var('func_8352')
call_11086 = relay.TupleGetItem(func_8351_call(), 0)
call_11087 = relay.TupleGetItem(func_8352_call(), 0)
output = relay.Tuple([bop_11078,call_11086,])
output2 = relay.Tuple([bop_11078,call_11087,])
func_11091 = relay.Function([var_11073,], output)
mod['func_11091'] = func_11091
mod = relay.transform.InferType()(mod)
var_11092 = relay.var("var_11092", dtype = "float64", shape = (13, 2, 13))#candidate|11092|(13, 2, 13)|var|float64
output = func_11091(var_11092)
func_11093 = relay.Function([var_11092], output)
mutated_mod['func_11093'] = func_11093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mod.get_global_var('func_9335')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_11176 = relay.TupleGetItem(func_9335_call(), 2)
call_11177 = relay.TupleGetItem(func_9337_call(), 2)
output = relay.Tuple([call_11176,])
output2 = relay.Tuple([call_11177,])
func_11182 = relay.Function([], output)
mod['func_11182'] = func_11182
mod = relay.transform.InferType()(mod)
mutated_mod['func_11182'] = func_11182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11182_call = mutated_mod.get_global_var('func_11182')
call_11183 = func_11182_call()
output = call_11183
func_11184 = relay.Function([], output)
mutated_mod['func_11184'] = func_11184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5039_call = mod.get_global_var('func_5039')
func_5040_call = mutated_mod.get_global_var('func_5040')
call_11197 = func_5039_call()
call_11198 = func_5039_call()
output = relay.Tuple([call_11197,])
output2 = relay.Tuple([call_11198,])
func_11208 = relay.Function([], output)
mod['func_11208'] = func_11208
mod = relay.transform.InferType()(mod)
output = func_11208()
func_11209 = relay.Function([], output)
mutated_mod['func_11209'] = func_11209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6265_call = mod.get_global_var('func_6265')
func_6267_call = mutated_mod.get_global_var('func_6267')
call_11241 = relay.TupleGetItem(func_6265_call(), 0)
call_11242 = relay.TupleGetItem(func_6267_call(), 0)
func_2130_call = mod.get_global_var('func_2130')
func_2136_call = mutated_mod.get_global_var('func_2136')
const_11270 = relay.const([-8,-6,-7,-1,-10,-2,5,-10,-10,-8,3,3,-2,-9,5,-1,-8,-4,-1,-5,-5,10,3,-7,-10,-3,-6,-6,-9,-1,6,9,-9,10,6,-3,-2,-3,2,7,-6,4,7,10,-7,-10,3,9,-10,3,4,-9,8,3,-3,-1,-3,10,-9,5,9,10,-5,-5,-10,3,6,-4,3,6,10,-4,6,-4,-2,2,-4,-7,-3,-6,-3,-1,-10,-7,4,10,3,-8,7,6,1,-3,2,6,2,-2,-10,8,-8,6,8,-6,9,2,6,-7,7,1,-10,7,-8,1,-2,1,-1,1,-2,-10,3,-9,1,-7,6,10,-7,-9,7,-5,8,8,3,-9,-8,-8,-1,9,4,2,4,-5,-2,5,6,-8,-6,-4,-6,3,-9,5,9,4,10,3,-10,4,-5,-1,9,-7,-6,3,1,-5,9,2,4,1,-4,7,-5,5,-9,2,4,2,-10,1,1,4,6,7,-4,3,5,1,2,-1,-2,9,-2,-7,8,-4,6,10,-3,-1,7,4,-5,-3,3,-7,7,-3,1,-1,-10,9,-2,7,5,-4,-3,6,5,4,-3,3,9,9,5,-10,-9,-8,-5,8,-2,-6,-3,2,4,-4,-9,7,10,-1,-9,10,7,9,-3,-3,1,2,2,10,2,-2,-10,2,-8,6,1,5,6,-1,3,5,-3,-8,1,-2,-3,-5,-5,4,9,1,6,7,10,-2,-1,-6,4,-3,3,7,10,-8,10,-10,-2,8,-7,-1,-4,-9,-7,-3,-9,5,10,6,7,-8,-6,5,-1,7,1,-2,-8,-2,-6,-8,-9,-4,9,2,-4,5,1,9,3,8,1,-1,-3,-7,-7,-1,-2,-7,7,-8,-2,-2,-1,4,4,-9,4,-5,2,5,9,-6,-4,-1,-4,1,-10,-8,-1,-6,-6,1,7,-6,-8,-8,10,-5,7,-3,-4,9,-5,-4,1,1,-7,7,8,2,-6,-4,-4,-9,6,-4,-4,2,-1,-8,-8,-10,-3,8,-10,-9,1,-3,4,-6,3,1,-2,-9,-1,5,-7,-6,-10,4,-5,8,-8,-2,10,3,7,-1,8,4,-8,-3,-2,5,-3,3,2,5,2,-4,-5,-8,-2,-5,-10,2,-6,2,3,-1,8,4,7,2,7,4,3,-8,2,5,-10,1,-3,-3,2,-1,-10,-2,4,-8], dtype = "uint64")#candidate|11270|(448,)|const|uint64
const_11271 = relay.const([True,False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,False], dtype = "bool")#candidate|11271|(2145,)|const|bool
const_11272 = relay.const(-7, dtype = "uint8")#candidate|11272|()|const|uint8
const_11273 = relay.const([2,10,-6,-10,10,2,-5,10,7,-4,-6,-8,-8,-4,7,-3,-5,-6,9,-10,2,-3,-1,2,-8,2,9,2,-5,10,-8,-1,-7,3,-5,-5,5,5,-2,3,-5,-7,-4,-10,5,-3,5,7,-2,-6,-5,3,10,5,7,5,4,-4,10,9,6,-10,5,10,8,-4,8,3,9,1,6,6,5,10,6,3,-3,-2,8,8,8,9,1,-4,-9,-6,9,7,-4,1,10,1,-7,-2,4,3,1,-8,5,3,-6,-1,1,-3,6,-2,-8,-10,7,-1,9,3,-7,2,-4,4,-4,-7,4,7,-3,-6,5,7,-7,2,-4,8,9,-1,-5,-3,1,-1,7,5,-8,-1,7,4,8,-10,3,2,-7,3,10,-10,-5,8,-10,3,3,10,2,4,10,-2,3,2,-9,-2,4,-1,-5,-2,9,-3,-9,-2,7,-1,-3,9,-7,6,8,4,-1,1,-4,-1,8,7,6,-8,-9,-9,2,-8,9,-4,3,-10,-6,2,-6,5,8,-1,5,-7,-8,7,-2,-10,9,7,5,8,-8,1,5,10,-2,-8,-10,-1,9,2,-1,4,10,1,9,-9,10,-3,-8,6,5,6,9,8,5,1,4,-7,-7,2,-10,6,-8,2,-3,-5,4,-4,1,3,1,6,-1,10,3,-5,2,2,-10,8,-5,-2,6,-2,-7,5,-10,3,-5,-9,-6,1,6,8,8,-1,-10,-3,-10,-3,1,5,10,1,3,-4,-6,7,-8,10,-2,10,6,6,8,3,1,1,7,5,-3,3,3,1,-4,9,6,5,3,-7,5,2,-9,-7,4,10,-10,7,10,5,3,-1,-3,8,-2,-9,-7,2,4,2,-1,5,3,3,2,-9,-1,-3,-7,-10,-7,5,-10,8,8,1,-2,1,8,1,1,6,-2,-8,-1,-9,7,-2,3,-10,4,10,-8,3,6,-10,6,1,-7,7,7,-8,-10,-3,4,5,5,-4,-8,-10,1,-1,8,-4,-1,4,-7,-4,5,-1,1,5,-1,8,5,4,-10,2,-7,2,9,7,6,-2,-9,10,-9,5,-3,9,-2,4,8,-7,-4,4,-3,-9,2,-4,6,-10,-8,-5,7,6,7,-1,-6,1,-7,5,-5,3,-8,8,-10,9,3,-6,9,10,-2,10,-9,-7,-5,-8,-7,-8,9,-10,-6,4,6,2,2,1,2,1,4,10,2,-10,3,5,7,9,-8,-5,-3,-8,-8,10,-2,-3,-2,-6,3,5,-7,7,8,7,9,10,6,10,7,-4,-2,7,-10,-8,10,-10,-6,9,3,1,8,7,-7,10,6,7,2,1,7,-6,5,-4,-3,6,-10,9,6,4,2,1,9,-7,2,-3,-1,5,-7,8,5,5,1,-7,-1,-2,6,-2,-3,-4,-10,3,-7,9,1,-3,1,4,-3,1,-2,8,8,1,-10,-6,3,2,-8,-4,-8,5,-5,1,8,2,5,-7,8,6,-4,-10,10,7,-5,-6,5,4,10,8,9,9,-7,-9,-4,-5,-5,-5,1,4,-2,10,-4,7,-10,-6,-2,5,1,6,-8,6,-8,-10,-1,-4,9,-10,8,8,4,-9,9,8,7,-7,-7,-8,-4,-3,-5,9,2,-6,9,-10,-10,-1,-2,-10,5,6,2,6,-4,-10,7,-4,9,9,8,2,6,-6,6,-1,-3,4,1,-1,10,-8,1,4,-6,1,-2,-1,-10,-9,2,7,7,1,1,6,5,8,8,7,7,-7,1,-7], dtype = "uint8")#candidate|11273|(672,)|const|uint8
call_11269 = relay.TupleGetItem(func_2130_call(relay.reshape(const_11270.astype('uint64'), [8, 7, 8]), relay.reshape(const_11270.astype('uint64'), [8, 7, 8]), relay.reshape(const_11271.astype('bool'), [2145,]), relay.reshape(const_11272.astype('uint8'), []), relay.reshape(const_11273.astype('uint8'), [672,]), ), 3)
call_11274 = relay.TupleGetItem(func_2136_call(relay.reshape(const_11270.astype('uint64'), [8, 7, 8]), relay.reshape(const_11270.astype('uint64'), [8, 7, 8]), relay.reshape(const_11271.astype('bool'), [2145,]), relay.reshape(const_11272.astype('uint8'), []), relay.reshape(const_11273.astype('uint8'), [672,]), ), 3)
output = relay.Tuple([call_11241,call_11269,const_11270,const_11271,const_11272,const_11273,])
output2 = relay.Tuple([call_11242,call_11274,const_11270,const_11271,const_11272,const_11273,])
func_11280 = relay.Function([], output)
mod['func_11280'] = func_11280
mod = relay.transform.InferType()(mod)
mutated_mod['func_11280'] = func_11280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11280_call = mutated_mod.get_global_var('func_11280')
call_11281 = func_11280_call()
output = call_11281
func_11282 = relay.Function([], output)
mutated_mod['func_11282'] = func_11282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6265_call = mod.get_global_var('func_6265')
func_6267_call = mutated_mod.get_global_var('func_6267')
call_11299 = relay.TupleGetItem(func_6265_call(), 1)
call_11300 = relay.TupleGetItem(func_6267_call(), 1)
output = call_11299
output2 = call_11300
func_11304 = relay.Function([], output)
mod['func_11304'] = func_11304
mod = relay.transform.InferType()(mod)
mutated_mod['func_11304'] = func_11304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11304_call = mutated_mod.get_global_var('func_11304')
call_11305 = func_11304_call()
output = call_11305
func_11306 = relay.Function([], output)
mutated_mod['func_11306'] = func_11306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6870_call = mod.get_global_var('func_6870')
func_6872_call = mutated_mod.get_global_var('func_6872')
call_11359 = func_6870_call()
call_11360 = func_6870_call()
output = call_11359
output2 = call_11360
func_11377 = relay.Function([], output)
mod['func_11377'] = func_11377
mod = relay.transform.InferType()(mod)
output = func_11377()
func_11378 = relay.Function([], output)
mutated_mod['func_11378'] = func_11378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10218_call = mod.get_global_var('func_10218')
func_10220_call = mutated_mod.get_global_var('func_10220')
call_11407 = relay.TupleGetItem(func_10218_call(), 2)
call_11408 = relay.TupleGetItem(func_10220_call(), 2)
func_8090_call = mod.get_global_var('func_8090')
func_8092_call = mutated_mod.get_global_var('func_8092')
call_11409 = relay.TupleGetItem(func_8090_call(), 1)
call_11410 = relay.TupleGetItem(func_8092_call(), 1)
output = relay.Tuple([call_11407,call_11409,])
output2 = relay.Tuple([call_11408,call_11410,])
func_11419 = relay.Function([], output)
mod['func_11419'] = func_11419
mod = relay.transform.InferType()(mod)
mutated_mod['func_11419'] = func_11419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11419_call = mutated_mod.get_global_var('func_11419')
call_11420 = func_11419_call()
output = call_11420
func_11421 = relay.Function([], output)
mutated_mod['func_11421'] = func_11421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10968_call = mod.get_global_var('func_10968')
func_10969_call = mutated_mod.get_global_var('func_10969')
call_11505 = relay.TupleGetItem(func_10968_call(), 0)
call_11506 = relay.TupleGetItem(func_10969_call(), 0)
func_8661_call = mod.get_global_var('func_8661')
func_8663_call = mutated_mod.get_global_var('func_8663')
call_11511 = relay.TupleGetItem(func_8661_call(), 0)
call_11512 = relay.TupleGetItem(func_8663_call(), 0)
output = relay.Tuple([call_11505,call_11511,])
output2 = relay.Tuple([call_11506,call_11512,])
func_11520 = relay.Function([], output)
mod['func_11520'] = func_11520
mod = relay.transform.InferType()(mod)
output = func_11520()
func_11521 = relay.Function([], output)
mutated_mod['func_11521'] = func_11521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2752_call = mod.get_global_var('func_2752')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_11533 = relay.TupleGetItem(func_2752_call(), 0)
call_11534 = relay.TupleGetItem(func_2753_call(), 0)
output = relay.Tuple([call_11533,])
output2 = relay.Tuple([call_11534,])
func_11548 = relay.Function([], output)
mod['func_11548'] = func_11548
mod = relay.transform.InferType()(mod)
output = func_11548()
func_11549 = relay.Function([], output)
mutated_mod['func_11549'] = func_11549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7114_call = mod.get_global_var('func_7114')
func_7116_call = mutated_mod.get_global_var('func_7116')
call_11552 = relay.TupleGetItem(func_7114_call(), 0)
call_11553 = relay.TupleGetItem(func_7116_call(), 0)
output = relay.Tuple([call_11552,])
output2 = relay.Tuple([call_11553,])
func_11555 = relay.Function([], output)
mod['func_11555'] = func_11555
mod = relay.transform.InferType()(mod)
mutated_mod['func_11555'] = func_11555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11555_call = mutated_mod.get_global_var('func_11555')
call_11556 = func_11555_call()
output = call_11556
func_11557 = relay.Function([], output)
mutated_mod['func_11557'] = func_11557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7468_call = mod.get_global_var('func_7468')
func_7469_call = mutated_mod.get_global_var('func_7469')
call_11579 = relay.TupleGetItem(func_7468_call(), 0)
call_11580 = relay.TupleGetItem(func_7469_call(), 0)
output = call_11579
output2 = call_11580
func_11590 = relay.Function([], output)
mod['func_11590'] = func_11590
mod = relay.transform.InferType()(mod)
output = func_11590()
func_11591 = relay.Function([], output)
mutated_mod['func_11591'] = func_11591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9671_call = mod.get_global_var('func_9671')
func_9673_call = mutated_mod.get_global_var('func_9673')
call_11605 = relay.TupleGetItem(func_9671_call(), 0)
call_11606 = relay.TupleGetItem(func_9673_call(), 0)
output = relay.Tuple([call_11605,])
output2 = relay.Tuple([call_11606,])
func_11617 = relay.Function([], output)
mod['func_11617'] = func_11617
mod = relay.transform.InferType()(mod)
mutated_mod['func_11617'] = func_11617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11617_call = mutated_mod.get_global_var('func_11617')
call_11618 = func_11617_call()
output = call_11618
func_11619 = relay.Function([], output)
mutated_mod['func_11619'] = func_11619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5227_call = mod.get_global_var('func_5227')
func_5229_call = mutated_mod.get_global_var('func_5229')
call_11694 = func_5227_call()
call_11695 = func_5227_call()
output = relay.Tuple([call_11694,])
output2 = relay.Tuple([call_11695,])
func_11705 = relay.Function([], output)
mod['func_11705'] = func_11705
mod = relay.transform.InferType()(mod)
output = func_11705()
func_11706 = relay.Function([], output)
mutated_mod['func_11706'] = func_11706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5083_call = mod.get_global_var('func_5083')
func_5084_call = mutated_mod.get_global_var('func_5084')
call_11725 = relay.TupleGetItem(func_5083_call(), 1)
call_11726 = relay.TupleGetItem(func_5084_call(), 1)
func_11304_call = mod.get_global_var('func_11304')
func_11306_call = mutated_mod.get_global_var('func_11306')
call_11751 = func_11304_call()
call_11752 = func_11304_call()
output = relay.Tuple([call_11725,call_11751,])
output2 = relay.Tuple([call_11726,call_11752,])
func_11759 = relay.Function([], output)
mod['func_11759'] = func_11759
mod = relay.transform.InferType()(mod)
mutated_mod['func_11759'] = func_11759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11759_call = mutated_mod.get_global_var('func_11759')
call_11760 = func_11759_call()
output = call_11760
func_11761 = relay.Function([], output)
mutated_mod['func_11761'] = func_11761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8881_call = mod.get_global_var('func_8881')
func_8883_call = mutated_mod.get_global_var('func_8883')
call_11768 = func_8881_call()
call_11769 = func_8881_call()
func_6265_call = mod.get_global_var('func_6265')
func_6267_call = mutated_mod.get_global_var('func_6267')
call_11770 = relay.TupleGetItem(func_6265_call(), 1)
call_11771 = relay.TupleGetItem(func_6267_call(), 1)
output = relay.Tuple([call_11768,call_11770,])
output2 = relay.Tuple([call_11769,call_11771,])
func_11772 = relay.Function([], output)
mod['func_11772'] = func_11772
mod = relay.transform.InferType()(mod)
mutated_mod['func_11772'] = func_11772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11772_call = mutated_mod.get_global_var('func_11772')
call_11773 = func_11772_call()
output = call_11773
func_11774 = relay.Function([], output)
mutated_mod['func_11774'] = func_11774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10968_call = mod.get_global_var('func_10968')
func_10969_call = mutated_mod.get_global_var('func_10969')
call_11795 = relay.TupleGetItem(func_10968_call(), 0)
call_11796 = relay.TupleGetItem(func_10969_call(), 0)
func_8940_call = mod.get_global_var('func_8940')
func_8942_call = mutated_mod.get_global_var('func_8942')
call_11802 = func_8940_call()
call_11803 = func_8940_call()
func_2060_call = mod.get_global_var('func_2060')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_11807 = relay.TupleGetItem(func_2060_call(), 0)
call_11808 = relay.TupleGetItem(func_2061_call(), 0)
output = relay.Tuple([call_11795,call_11802,call_11807,])
output2 = relay.Tuple([call_11796,call_11803,call_11808,])
func_11811 = relay.Function([], output)
mod['func_11811'] = func_11811
mod = relay.transform.InferType()(mod)
output = func_11811()
func_11812 = relay.Function([], output)
mutated_mod['func_11812'] = func_11812
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11888 = relay.var("var_11888", dtype = "float32", shape = (14, 3, 7))#candidate|11888|(14, 3, 7)|var|float32
uop_11889 = relay.sqrt(var_11888.astype('float32')) # shape=(14, 3, 7)
func_7893_call = mod.get_global_var('func_7893')
func_7896_call = mutated_mod.get_global_var('func_7896')
const_11904 = relay.const([-5.731420,5.472191,-2.871599,-8.841023,-9.704710,3.049623,-6.853011,8.676244,4.454004,1.059239,5.769400,8.933078,-0.277267,-2.039892,-1.541622,-5.593807,-3.797151,-2.634862,-2.357437,-1.912408,6.255962,5.139844,-4.887539,-5.894903,5.646285,-1.353414,-4.873818,-4.741695,-4.843381,3.211751,-8.367428,1.124111,6.068684,9.088988,-8.892457,-8.610851,-4.134111,1.311308,-7.729591,-5.153313,-1.920345,-2.406998,-0.338356,6.905223,0.948855,9.182802,-4.662740,-2.923858,-0.868511,-7.832819,-2.082604,-9.619452,-1.703945,6.347788,-9.349749,-2.671067,6.831102,5.249080,9.506694,-1.633899,5.250158,-4.663968,-6.577847,6.012145,-3.614750,3.007487,-1.408149,0.185361,4.807252,9.850730,3.093267,-2.639922,-4.595569,-3.422326,5.893825,9.976935,2.333944,-5.399335,-3.026253,-6.647147,5.579802,7.299493,-9.047574,-2.251778,-7.900417,3.025098,1.651593,-8.840411,1.751083,5.270622,0.831057,-9.233504,-6.925250,-7.362538,-0.255299,-4.178680,-6.234876,-5.513444,-0.019342,-0.912748,-7.566149,-7.717983,-9.210086,-3.756930,-3.813620,-3.977403,-8.208979,-6.931446,7.300420,3.756623,1.764594,-4.180941,-8.575355,-5.929983,4.325440,5.533531,-5.253783,-2.810633,-3.428885,4.585552,-7.629905,-2.587683,-9.230963,-8.432920,8.018263,1.067130,0.229528,-2.113456,-8.280455,-6.310701,7.458332,-3.477929,-8.599982,-6.554339,7.176017,4.899924,7.632239,-0.117856,-7.137758,-9.191333,-6.000740,-0.977335,4.934222,6.398397,-7.388163,9.186421,9.650804,6.430048,-1.372716,-5.113128,9.214158,-6.538432,5.870446,-7.172022,7.727016,9.982120,3.466231,2.154783,-8.859710,-4.303562,-3.668028,0.744440,9.476327,3.117648,-0.264265,3.231980,1.852624,1.892383,-6.516802,-0.420566,-0.349160,-0.944047,-7.068208,-3.031342,-1.278541,7.265978,-4.455625,7.727191,5.026099,-1.645539,-6.256604,-7.927532,6.843880,6.079345,2.868149,3.091847,0.460499,5.302997,1.189871,8.256715,5.013422,-4.153180,5.252970,6.701364,7.298545,-9.704996,-0.311868,4.784879,-4.388463,3.333443,8.757206,2.789342,-4.579323,-0.886901,-2.772473,-2.073365,-3.242986,-3.104035,-5.161861,-9.118974,0.500957,2.286517,1.107288,3.274980,0.523801,-0.409700,8.607833,-2.171342,-0.190803,3.842807,-4.530351,-9.791863,-2.161635,-3.900985,5.358219,-4.650384,1.095988,-0.194225,1.055304,8.316059,-8.003621,0.437522,5.454679,-0.611716,-6.459927,3.066369,8.516215,1.153325,-5.020846,-8.185485,-8.043352,-3.300001,-8.373992,6.187535,-9.037362,2.659965,-6.197938,-7.975269,-2.507435,6.240134,-7.401094,2.631806,2.486441,2.285041,-5.723062,6.177670,9.957284,-5.637472,-5.140739,3.255942,-3.696730,6.050120,4.396347,0.122724,-5.763857,-7.813201,5.994617,-1.142304,-0.785356,-5.305453,2.396586,1.423869,7.931467,0.622234,3.483863,-2.236373,5.083421,-7.529502,1.079602,-6.612130,3.990736,-3.681041,-4.663379,7.457974,-1.248783,6.656861,3.216522,-4.686738,-2.581980,-8.176314,-6.343793,-6.294966,-9.505558,-5.862867,-3.237574,-7.385918,2.291426,-1.259864,1.350833,-4.119700,4.911122,-0.504018,5.079401,6.648904,-9.568331,8.125146,-0.898843,-8.964295,8.639833,-5.947141,6.869329,3.347326,2.587890,-3.531590,4.866044,-0.737784,-5.011154,8.227943,-9.978263,6.907158,-2.559860,1.558563,-1.051910,9.112819,3.176359,2.798630,-1.240510,3.173617,-3.452287,6.831309,6.629189,-8.582350,-0.880403,9.475830,-8.886198,4.156142,1.621441,8.683800,-4.399411,9.666825,-2.972310,-7.776368,4.904432,-2.873839,9.131875,8.480278,-2.793416,-0.257814,2.425824,6.101987,-0.445810,-4.770770,7.046317,-1.236203,2.620247,9.007948,-1.010162,-9.090376,-7.253012,-5.122361,-8.919999,-3.447400,0.820965,2.816500,-8.480024,4.859246,1.145022,-5.011553,0.901870,-9.147839,3.841320,7.089008,5.931388,4.111996,-3.660819,3.379486,-7.851385,7.851668,-8.293677,-6.189392,1.431482,-3.929896,-7.344897,-5.806382,7.323128,-8.947366,-5.547410,-9.714442,4.605224,2.989780,8.713920,9.896757,-2.981898,-8.132204,4.444599,2.601278,-5.259805,-0.562386,5.337437,-8.855251,1.904774,8.327098,-2.142132,-1.585059,8.374776,-7.145854,-6.430011,-1.138346,-9.188564,-1.492296,-7.146419,1.120036,3.316056,6.712955,-3.870656,7.087052,-1.402898,5.510079,-0.019553,-5.813075,-7.709597,7.247021,-0.579743,8.018911,-4.966701,5.632867,-1.977773,8.747824,-0.466484,-4.852262,-9.691825,-2.826969,-4.252079,-8.753227,4.965638,-4.067663,7.801849,0.221745,-2.267726,-6.411068,-6.477039,8.879456,-7.794309,-0.176371,7.420621,5.168474,-2.767947,-5.208890,-4.216365,9.561048,9.301790,4.670290,5.483549,0.008034,3.472134,-9.031781,5.004227,-0.161904,-5.948720,-6.760017,1.614450,-4.632102,3.234412,-5.267823,1.619677,-8.855107,-6.618730,4.418794,-8.675560,6.067146,-3.411814,8.862249,8.452408,-7.959247,-9.234815,7.376294,-1.840428,8.844590,-4.329776,4.821774,0.058306,-5.489238,3.075823,-2.882530,-3.295908,-1.853936,4.846927,-6.390110,2.697851,7.487102,2.105354,-2.631562,-8.307027,-8.238707,1.492351,-5.713247,8.504776,-9.555755,-4.098680,-9.265057,-6.907988,8.157601,-9.207739,-0.754908,-4.142912,7.135899,-3.397324,-8.639610,8.066035,0.856883,-0.552654,3.939633,6.212557,1.921254,-5.155350,-9.717590,-7.709778,6.035757,-6.576213,-8.523432,6.223551,-9.080152,0.169404,-9.474887,8.588195,-5.915193,0.829071,8.393468,3.046858,-4.474056,-8.037114,8.910719,-5.723646,1.570105,-0.329491,-0.883024,1.078339,-6.568301,2.327715,4.865628,-7.961226,-1.684378,-4.570824,-0.278462,-1.044654,6.487394,-3.399204,2.835690,4.698074,6.874566,8.870929,8.810036,-1.386626,3.690774,-7.460926,0.509963,-8.383387,-9.651204,1.180552,3.901624,4.115882,7.480688,8.760123,9.452527,3.799022,-7.407871,-4.298947,-1.549627,7.695580,-9.906227,-7.499406,7.097817,4.255075,1.147391,-7.265410,9.470486,-3.377765,2.718980,7.888180,-3.580000,0.417601,7.219465,3.844529,1.952909,-6.326158,-3.672771,3.849288,0.246601,-0.220903,8.002906,3.987153,-4.259006,3.659930,0.775403], dtype = "float32")#candidate|11904|(594,)|const|float32
call_11903 = relay.TupleGetItem(func_7893_call(relay.reshape(const_11904.astype('float32'), [594, 1])), 1)
call_11905 = relay.TupleGetItem(func_7896_call(relay.reshape(const_11904.astype('float32'), [594, 1])), 1)
func_8224_call = mod.get_global_var('func_8224')
func_8228_call = mutated_mod.get_global_var('func_8228')
const_11930 = relay.const([-7,-6,5,-9,4,-10,9,-8,9,4,9,-5,5,8,-5,6,-7,-1,6,7,-7,9,-4,-10,3,6,-4,-10,4,8,-2,1,7,-2,-9,1,7,-2,10,-3,-8,4,-1,2,6,-3,4,-8,6,-6,-10,-3,-8,5,8,1,-10,-7,-3,4,-1,-8,1,-8,7,-3,10,1,2,-7,7,-6,7,5,4,-7,-6,-10,2,-5,-1,-3,6,-10,-9,9,-9,10,2,-5,-5,-1,-9,10,-10,-8,7,3,-5,-4,-4,-10,-9,8,-8,-8,-7,-5,-10,8,4,-3,9,-4,9,-9,-2,5,-3,-5,-7,-5,-3,-3,-7,-5,8,2,1,2,-8,4,-3,-3,3,-7,-2,5,5,10,-8,5,-10,3,-6,3,5,-4,-8,5,7,-4,-6,-6,-8,5,9,1,-8,3,1,-6,5,7,8,-7,-3,4,9,-10,-4,2,-6,5,1,-6,5,-9,3,-6,-7,4,3,1,9,10,8,-9,8,8,3,2,-7,8,6,-1,-6,-4,4,-2,1,-6,-5,3,10,-1,-5,-1,-3,-2,-5,-3,-7,-2,6,-4,8,-6,-7,-4,-10,10,-9,8,1,10,-3,9,-4,1,-8,5,-4,-9,-9,8,10,-7,-2,-1,-6,-1,8,1,4,1,8,8,-8,5,-1,-9,2,10,-2,6,-3,-9,8,10,3,-6,9,2,-2,-5,9,-6,9,-4,-6,-10,-1,10,10,-3,-3,-1,2,10,-10,7,-8,-2,-10,9,-9,6,10,9,-8,-3,1,1,-9,7,5,-9,-8,3,7,3,1,-6,-5,-10,-9,-4,-9,4,-8,-5,7,-8,-5,3,3,10,7,-6,4,5,-1,4,6,7,-8,-6,6,-10,-7,7,-10,3,-4,10,-8,-1,-6,10,2,-5,-8,5,-7,9,9,3,4,7,-8,7,-3,-5,-5,2,-2,8,-10,-8,-2,-2,-4,10,-2,5,3,-5,10,7,7,-3,-10,9,-7,-8,3,-8,8,4,-3,9,-8,-4,4,-6,-5,-10,-9,5,-5,3,-7,-6,8,-5,8,1,-8,-6,8,-5,-10,-10,-3,5,9,9,-2,1,4,5,1,8,10,-4,-6,5,-6,-5,9,-9,1,-6,-5,-2,-4,1,-2,-5,-4,3,9,-8,-1,4,-6,-8,-2,-7,-1,6,-8,1,7,-2,-8,-3,-3,2,7,-3,2,7,6,-1,-6,2,-5,2,2,2,-1,7,-9,9,6,6,-5,-1,8,-8,10,-8,5,-6,-6,-7,7,-2,-2,2,-2,7,3,6,2,6,6,-9,-4,9,5,-8,9,-7,-8,10,-7,-7,5,-2,9,-10,-1,-7,-4,-8,2,1,5,-4,-7,3,3,4,3,-6,-5,-7,-7,-3,1,-2,-7,-8,-1,5,9,1,10,-10,3,-7,-4,5,9,4,1,-4,-7,1,5,5,6,5,-3,-10,3,-5,4,-8,-9,-4,8,-9,10,-2,-7,-10,5,10,-2,-4,-10,2,8,8,4,-8,-1,7,6,-8,-8,-6,6,3,-8,3,-8,1,-6,-5,-2,3,9,-5,-9,10,1,-2,-1,5,6,9,-4,1,-1,10,-1,-5,3,5,-2,1,10,10,-2,3,2,1,-4,8,1,7,3,2,3,-7,-4,-8,-4,8,-5,2,-4,-5,-9,4,-1,4,4,-9,3,1,4,2,10,-4,4,4,10,6,2,-1,-2,6,-9,4,1,-1,-7,-5,-6,3,4,8,7,-3,-8,2,7,6,5,2,-7,10,-10,2,3,-6], dtype = "uint8")#candidate|11930|(672,)|const|uint8
const_11931 = relay.const([9,9,-8,6,7,-10,-1,-4,10,8,7,7,1,-5,5,2,7,-7,10,-5,-7,1,9,-3,-9,10,-8,-5,5,8,9,5,1,1,5,8,2,-2,-5,1,-9,-9,-8,-5,-4,6,-3,9,10,7,7,-9,-5,1,7,3,5,-2,4,-7,-2,-4,-1,-1,5,8,3,1,8,7,4,-3,10,1,5,-6,10,-2,-5,3,10,9,1,-3,-2,6,10,2,-5,8,10,6,4,-10,-2,-6,-8,-8,-7,-6,3,2,3,5,-8,9,7,-7,-3,1,-3,10,3,8,10,8,10,-9,5,-1,9,2,-7,-8,-9,-8,7,4,5,-2,10,8,-10,-2,-1,10,5,7,-3,2,5,4,7,3,-4,7,-5,-3,-4,-1,-6,-6,-5,2,-9,9,4,5,3,-3,1,8,-7,-10,-6,7,-4,-4,7,6,-8,-9,8,4,-9,8,-9,5,-7,-8,-8,4,9,10,4,3,10,-6,5,10,9,4,-6,5,-6,8,-7,5,-2,5,10,8,7,8,6,-5,-8,6,-2,9,3,1,10,7,2,6,9,3,1,-9,3,-3,-5,-5,9,4,-9,-1,2,1,-1,7,2,-5,3,-10,-10,-7,4,-1,-6,-3,9,-6,-4,-8,-5,-3,6,1,-4,6,-6,8,-5,-2,-3,9,-1,-4,3,7,8,6,10,3,-10,7,-2,-5,5,1,4,-9,-7,7,-6,2,6,7,-7,1,1,-3,-4,-1,8,4,-4,-5,7,-2,10,-8,4,-2,8,-8,3,4,-10,6,-9,-9,7,-3,-8,9,9,-4,-7,-3,2,-5,-1,-4,-6,-10,-5,5,3,-8,2,-8,-7,3,-9,-10,-8,-5,4,1,-2,-2,-9,8,-6,2,-4,-9,1,6,10,2,-10,6,-8,3,-9,-6,-5,-10,-1,-7,3,7,-9,5,-8,7,3,4,-4,1,4,-2,2,-10,-4,-9,4,-10,-2,4,1,-7,-9,-6,-8,6,4,10,2,10,-8,5,-8,7,-2,-9,-4,-7,-9,-6,10,8,-2,10,10,-1,3,-2,-3,-1,10,5,-8,9,-5,-4,-6,7,-3,-5,-10,-3,4,-6,-4,1,-8,-10,-9,2,3,-9,8,-9,6,8,-10,-9,-8,-1,-1,-8,1,5,-6,-5,5,-8,-9,-8,10,-1,6,-7], dtype = "uint16")#candidate|11931|(448,)|const|uint16
call_11929 = relay.TupleGetItem(func_8224_call(relay.reshape(const_11930.astype('uint8'), [672,]), relay.reshape(const_11931.astype('uint16'), [8, 56]), relay.reshape(const_11931.astype('uint16'), [8, 56]), ), 0)
call_11932 = relay.TupleGetItem(func_8228_call(relay.reshape(const_11930.astype('uint8'), [672,]), relay.reshape(const_11931.astype('uint16'), [8, 56]), relay.reshape(const_11931.astype('uint16'), [8, 56]), ), 0)
output = relay.Tuple([uop_11889,call_11903,const_11904,call_11929,const_11930,const_11931,])
output2 = relay.Tuple([uop_11889,call_11905,const_11904,call_11932,const_11930,const_11931,])
func_11938 = relay.Function([var_11888,], output)
mod['func_11938'] = func_11938
mod = relay.transform.InferType()(mod)
var_11939 = relay.var("var_11939", dtype = "float32", shape = (14, 3, 7))#candidate|11939|(14, 3, 7)|var|float32
output = func_11938(var_11939)
func_11940 = relay.Function([var_11939], output)
mutated_mod['func_11940'] = func_11940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11942 = relay.var("var_11942", dtype = "float64", shape = (16, 4, 15))#candidate|11942|(16, 4, 15)|var|float64
uop_11943 = relay.log2(var_11942.astype('float64')) # shape=(16, 4, 15)
func_9854_call = mod.get_global_var('func_9854')
func_9855_call = mutated_mod.get_global_var('func_9855')
call_11957 = func_9854_call()
call_11958 = func_9854_call()
func_10012_call = mod.get_global_var('func_10012')
func_10013_call = mutated_mod.get_global_var('func_10013')
call_11961 = relay.TupleGetItem(func_10012_call(), 0)
call_11962 = relay.TupleGetItem(func_10013_call(), 0)
func_9758_call = mod.get_global_var('func_9758')
func_9762_call = mutated_mod.get_global_var('func_9762')
const_11970 = relay.const([9,3,9,5,-3,-3,-10,-7,-5,5,6,-4,-9,7,8,-9,1,2,-9,6,-5,5,5,2,-6,-6,4,1,-5,-3,10,9,5,-3,-10,8,-7,3,-9,-4,3,9,-9,3,9,-8,10,-2,1,-1,4,10,-4,-3,-1,-2,-6,2,-1,1,2,3,-1,7,10,-4,-7,6,-1,-8,6,5,-9,7,-3,-4,-10,-7,1,2,3,-8,4,4,2,6,-2,-8,-7,4,5,-6,-4,7,-8,9,-7,-2,8,6,9,-6,4,-3,10,2,-3,10,1,5,6,-9,-8,8,8,-5,-8,8,-6,-5,-6,2,7,-1,9,8,-7,-2,9,-10,-4,3,-8,3,2,10,7,1,4,-10,5,2,-6,-8,4,3,-3,-9,-9,-4,-10,-9,6,9,-2,-5,-1,-1,-1,2,-7,3,-3,-10,5,-1,10,-2,-2,8,-3,2,-2,-1,-2,-10,9,-8,6,-3,3,3,-8,10,7,-5,-1,-4,-2,5,7,-4,9,-9,1,3,7,-7,-3,4,-3,10,-8,6,-9,-5,-6,-3,2,-9,1,8,10,-3,-2,-4,-8,8,9,7,5,-4,-2,8,-6,-8,1,-7,9,3,-8,6,-1,1,10,-10,1,-10,1,-6,6,-8,-10,-7,6,10,-9,10,-5,-2,1,4,7,5,-3,-7,-7,-6,-1,-5,5,10,6,-5,-5,7,-10,7,4,-7,5,6,10,-8,-6,-7,8,4,9,4,6,-9,-2,-4,-10,-3,-7,-6], dtype = "uint16")#candidate|11970|(288,)|const|uint16
call_11969 = relay.TupleGetItem(func_9758_call(relay.reshape(const_11970.astype('uint16'), [6, 12, 4]), relay.reshape(const_11970.astype('uint16'), [6, 12, 4]), ), 1)
call_11971 = relay.TupleGetItem(func_9762_call(relay.reshape(const_11970.astype('uint16'), [6, 12, 4]), relay.reshape(const_11970.astype('uint16'), [6, 12, 4]), ), 1)
bop_11978 = relay.divide(uop_11943.astype('float32'), relay.reshape(var_11942.astype('float32'), relay.shape_of(uop_11943))) # shape=(16, 4, 15)
output = relay.Tuple([call_11957,call_11961,call_11969,const_11970,bop_11978,])
output2 = relay.Tuple([call_11958,call_11962,call_11971,const_11970,bop_11978,])
F = relay.Function([var_11942,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11942,], output2)
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
