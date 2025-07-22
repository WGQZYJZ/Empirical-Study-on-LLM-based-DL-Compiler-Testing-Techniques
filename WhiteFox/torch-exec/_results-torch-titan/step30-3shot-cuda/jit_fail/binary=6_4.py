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

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        (x, y) = x1.size()
        v1 = x1.view(x, (- 1))
        v2 = torch.ones([y, 1], dtype=torch.float32).cuda()
        v3 = torch.mv(v2, v1)
        return (x2[v3] - x1)



func = Model().to('cuda')



v4 = torch.rand([9, 4])



x2 = torch.randn(1, 1, 64, 64)


test_inputs = [v4, x2]

# JIT_FAIL
'''
direct:
vector + matrix @ vector expected, got 1, 2, 2

jit:
Failed running call_function <built-in method mv of type object at 0x7dd7ed6699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 1)), FakeTensor(..., device='cuda:0', size=(9, 4))), **{}):
matrix @ vector expected, got 2, 2

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''