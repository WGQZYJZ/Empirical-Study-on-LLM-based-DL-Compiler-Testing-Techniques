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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(inp, x1)
        v2 = (v1 + x2.T)
        v3 = v2.contiguous()
        return v1




func = Model().to('cuda')



x1 = torch.randn(5, 5)



x2 = torch.randn(5, 3)



inp = torch.randn(4, 5)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (3) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(4, 5)), FakeTensor(..., device='cuda:0', size=(3, 5))), **{}):
Attempting to broadcast a dimension of length 3 at -2! Mismatching argument at index 1 had torch.Size([3, 5]); but expected shape should be broadcastable to [4, 5]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''