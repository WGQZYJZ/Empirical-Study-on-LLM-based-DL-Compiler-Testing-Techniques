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

    def forward(self, x1, other):
        v1 = x1.flatten(1)
        v2 = (v1 + other)
        v3 = v2.reshape_as(x1)
        return v3



func = Model().to('cuda')



x1 = torch.randn(10, 3, 4, 4)



other = torch.randn(10, 12)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (48) must match the size of tensor b (12) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(10, 48)), FakeTensor(..., device='cuda:0', size=(10, 12))), **{}):
Attempting to broadcast a dimension of length 12 at -1! Mismatching argument at index 1 had torch.Size([10, 12]); but expected shape should be broadcastable to [10, 48]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''