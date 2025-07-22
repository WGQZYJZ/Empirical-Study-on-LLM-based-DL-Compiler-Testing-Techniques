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

    def forward(self, x1, x2, x3):
        x4 = torch.cat((x1, x2, x3), 1)
        v1 = x4[:, (- 1)]
        v2 = torch.flip(x1, [2, 3])
        v3 = v2[:, ::2, ::2]
        v4 = torch.cat([x4, v3], 1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 3)



x2 = torch.randn(1)



x3 = torch.randn(1)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 1

jit:
Failed running call_function <built-in method flip of type object at 0x71886a2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3)), [2, 3]), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''