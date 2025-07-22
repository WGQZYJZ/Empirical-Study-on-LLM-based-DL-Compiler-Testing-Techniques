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
        self.down = torch.nn.Conv2d(3, 8, 4, stride=2, padding=1)
        self.up = torch.nn.ConvTranspose2d(8, 8, 4, stride=2, padding=1)
        self.act = torch.nn.Sigmoid()

    def forward(self, x1, x2):
        v1 = self.down(x1)
        v2 = self.up(v1)
        v3 = self.act((v2 - x2))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)



x2 = torch.randn(1, 3, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 16, 16)), FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 32, 32]); but expected shape should be broadcastable to [1, 8, 16, 16]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''