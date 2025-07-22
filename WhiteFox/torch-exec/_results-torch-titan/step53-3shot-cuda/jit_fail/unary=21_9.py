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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.convA = torch.nn.Conv2d(3, 8, 1)
        self.convB = torch.nn.Conv2d(3, 16, 1)
        self.convC = torch.nn.Conv2d(3, 32, 1)
        self.convD = torch.nn.Conv2d(3, 64, 1)

    def forward(self, x1):
        v1 = self.convA(x1)
        v2 = self.convB(x1)
        v3 = self.convC(x1)
        v4 = self.convD(x1)
        x = torch.tanh((((v1 + v2) + v3) + v4))
        return x




func = ModelTanh().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64))), **{}):
Attempting to broadcast a dimension of length 16 at -3! Mismatching argument at index 1 had torch.Size([1, 16, 64, 64]); but expected shape should be broadcastable to [1, 8, 64, 64]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''