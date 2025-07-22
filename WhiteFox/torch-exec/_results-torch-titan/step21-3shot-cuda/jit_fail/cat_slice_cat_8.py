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
        super(Model, self).__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.cat((x1, x2), 1)
        v2 = v1[:, (- 9223372036854775808):]
        v3 = v2[:, :16]
        v4 = torch.cat((v1, v3), 1)
        v5 = (v4 - x3)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 1, 8, 8)



x2 = torch.randn(1, 1, 8, 8)



x3 = torch.randn(1, 1, 4, 4)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 8, 8)), FakeTensor(..., device='cuda:0', size=(1, 1, 4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 4, 4]); but expected shape should be broadcastable to [1, 4, 8, 8]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''