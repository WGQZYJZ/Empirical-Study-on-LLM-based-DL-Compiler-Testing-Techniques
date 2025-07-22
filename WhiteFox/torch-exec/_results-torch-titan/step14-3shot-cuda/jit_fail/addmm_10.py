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

    def forward(self, x1, x2, inp1, inp2, inp3):
        v1 = torch.mm(inp1, inp2)
        v2 = (v1 + x1)
        v3 = torch.mm(v2, x2)
        v4 = torch.mm(v3, v1)
        return v4




func = Model().to('cuda')



x1 = torch.randn(3, 5)



x2 = torch.randn(5, 3)



inp1 = torch.randn(6, 2)



inp2 = torch.randn(2, 4)



inp3 = torch.randn(4, 6)


test_inputs = [x1, x2, inp1, inp2, inp3]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(6, 4)), FakeTensor(..., device='cuda:0', size=(3, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([3, 5]); but expected shape should be broadcastable to [6, 4]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''