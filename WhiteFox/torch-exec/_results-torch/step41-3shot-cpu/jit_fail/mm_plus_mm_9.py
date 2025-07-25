import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class Model(torch.nn.Module):

    def forward(self, input1, input2, input3):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input2)
        t3 = torch.mm(input1, input2)
        t4 = torch.mm(input1, input2)
        t5 = torch.mm(input2, input3)
        t6 = t1 + t2
        t7 = torch.mm(input2, input1)
        t8 = torch.mm(input3, input1)
        t9 = t6 - t7
        t10 = t6 + t8
        t11 = t9 * t10
        t12 = torch.mm(input1, torch.mm(input3, input1))
        t13 = t11 + t12
        t14 = torch.mm(input1, input3)
        t15 = torch.mm(input3, input1)
        t16 = torch.mm(input3, input2)
        t17 = torch.mm(input3, input2)
        t18 = t14 + t15
        t19 = torch.mm(input3, input3)
        t20 = torch.mm(input2, input3)
        t21 = torch.mm(input3, input1)
        t22 = t20 + t21
        t23 = t19 + t22
        t24 = t13 + t23
        t25 = t24 * t18
        t26 = t25 + t17
        t27 = torch.mm(input1, input3)
        t28 = torch.mm(input1, input1)
        t29 = torch.mm(input2, input1)
        t30 = torch.mm(input1, input3)
        t31 = torch.mm(input2, input3)
        t32 = torch.mm(input1, input3)
        t33 = torch.mm(input1, input3)
        t34 = torch.mm(input1, input2)
        t35 = torch.mm(input1, input3)
        t36 = t34 + t35
        t37 = t33 + t36
        t38 = torch.mm(input1, input2)
        t39 = torch.mm(input1, input1)
        t40 = torch.mm(input1, input3)
        t41 = torch.mm(input1, input3)
        t42 = torch.mm(input2, input2)
        t43 = torch.mm(input3, input2)
        t44 = torch.mm(input2, input1)
        t45 = torch.mm(input2, input1)
        t46 = torch.mm(input1, input2)
        t47 = torch.mm(input2, input2)
        t48 = torch.mm(input2, input3)
        t49 = torch.mm(input2, input3)
        t50 = torch.mm(input2, input3)
        t51 = torch.mm(input2, input3)
        t52 = torch.mm(input3, input2)
        t53 = torch.mm(input3, input2)
        t54 = torch.mm(input2, input3)
        t55 = torch.mm(input3, input3)
        t56 = torch.mm(input2, input1)
        t57 = torch.mm(input2, input1)
        t58 = torch.mm(input2, input3)
        t59 = torch.mm(input2, input2)
        t60 = torch.mm(input2, input2)
        t61 = torch.mm(input2, input3)
        t62 = torch.mm(input3, input2)
        t63 = torch.mm(input1, input2)
        t64 = torch.mm(input1, input3)
        t65 = t38 + t39
        t66 = t37 + t65
        t67 = list(range(1)) - t64
        t68 = t66 * t67
        t69 = t46 + t50
        t70 = t47 + t51
        t71 = t44 + t52
        t72 = t45 + t53
        t73 = t69 + t70
        t74 = t68 + t71
        t75 = t64 - t72
        t76 = t68 + t73
        t77 = t75 + t76
        t78 = t58 + t59
        t79 = t60 + t61
        t80 = t63 + t68
        t81 = t65 * t78
        t82 = t77 + t80
        t83 = t79 + t82
        t84 = t81 + t83
        t85 = t84 * t74
        t86 = t85 - t62
        t87 = t85 + t62
        t88 = t84 * t77
        t89 = t64 - t70
        t90 = t85 * t76
        t91 = t88 + t89
        t92 = t90 + t91
        t93 = t92 * t74
        t94 = t93 * t61
        t95 = t93 * t60
        t96 = t95 - t59
        t97 = t81 * t63
        t98 = t93 - t94
        t99 = t96 + t97
        t100 = t98 + t99
        t101 = t87 + t100
        t102 = t87 * t86
        t103 = t101 * t79
        t104 = t102 * t60
        t105 = t103 * t59
        t106 = (t104 - t105) * (t89 * t60) + (t103 + t105) * (t90 * t61)
        t107 = torch.cat(t106, dim=-1)
        t108 = t107 * t88
        t109 = t92 * t88
        t110 = t107 * t95
        t111 = t97 * t92
        t112 = t108 * t86
        t113 = t109 * t86
        t114 = t110 * t86
        t115 = t111 * t86
        t116 = t112 - t113
        t117 = t114 - t115
        t118 = t116 + t117
        t119 = t107 * t101
        t120 = t118 + t119
        t121 = t107 + t120
        t122 = t119 * t88
        t123 = t118 * t95
        t124 = t122 * t86
        t125 = t123 * t86
        t126 = t107 * t88
        t127 = t107 * t95
        t128 = t126 * t86
        t129 = t127 * t86
        t130 = t128 - t129
        t131 = t124 + t125
        t132 = t130 + t131
        t133 = t107 - t121
        t134 = t132 - t133
        t135 = t134 * t86
        t136 = t134 * t97
        t137 = t135 - t136
        return t137



func = Model().to('cpu')


input1 = torch.randn(3, 3)

input2 = torch.randn(3, 3)

input3 = torch.randn(3, 3)

test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for -: 'list' and 'Tensor'

jit:
Failed running call_function <built-in function sub>(*([0], FakeTensor(..., size=(s0, s0))), **{}):
unsupported operand type(s) for -: 'immutable_list' and 'FakeTensor'

from user code:
   File "<string>", line 82, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''