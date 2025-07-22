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
        self.weight = torch.nn.Parameter(torch.ones(2, 2, 3))

    def forward(self, x1):
        x2 = (self.weight * x1)
        x3 = F.conv2d(x2, x2)
        return x3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (3) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(Parameter(FakeTensor(..., device='cuda:0', size=(2, 2, 3), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -2! Mismatching argument at index 1 had torch.Size([1, 2, 3, 3]); but expected shape should be broadcastable to [1, 2, 2, 3]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''