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
        v1 = torch.mm(x, y)
        v2 = torch.mul(v1, x)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 224)



y = torch.randn(224, 2)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (224) at non-singleton dimension 1

jit:
Failed running call_function <built-in method mul of type object at 0x7b316f4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2)), FakeTensor(..., device='cuda:0', size=(1, 224))), **{}):
Attempting to broadcast a dimension of length 224 at -1! Mismatching argument at index 1 had torch.Size([1, 224]); but expected shape should be broadcastable to [1, 2]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''