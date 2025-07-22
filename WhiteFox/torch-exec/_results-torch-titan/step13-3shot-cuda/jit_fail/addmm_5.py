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

    def forward(self, x1, x2, inp1, inp2):
        v1 = (x2 * inp1)
        v2 = torch.mm(x1, v1)
        v3 = (inp2 * v2)
        v4 = (x1 + v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 0)



x2 = torch.randn(0, 222)



inp1 = torch.randn(1, 1)



inp2 = torch.randn(1, 1)


test_inputs = [x1, x2, inp1, inp2]

# JIT_FAIL
'''
direct:
The size of tensor a (0) must match the size of tensor b (222) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 0)), FakeTensor(..., device='cuda:0', size=(1, 222))), **{}):
Attempting to broadcast a dimension of length 222 at -1! Mismatching argument at index 1 had torch.Size([1, 222]); but expected shape should be broadcastable to [1, 0]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''