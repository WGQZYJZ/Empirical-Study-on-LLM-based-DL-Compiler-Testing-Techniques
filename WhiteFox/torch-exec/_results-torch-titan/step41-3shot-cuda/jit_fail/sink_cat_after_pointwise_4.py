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

    def forward(self, x, y):
        z = torch.cat((x, y), dim=0)
        w = (z + (2 * y))
        return w




func = Model().to('cuda')



x = torch.randn(3, 1)



y = torch.ones(3, 1)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (3) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(6, 1)), FakeTensor(..., device='cuda:0', size=(3, 1))), **{}):
Attempting to broadcast a dimension of length 3 at -2! Mismatching argument at index 1 had torch.Size([3, 1]); but expected shape should be broadcastable to [6, 1]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''