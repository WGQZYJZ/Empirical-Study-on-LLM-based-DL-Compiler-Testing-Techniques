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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(2, 4, 3, stride=2, padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(4, 4, 2, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = (v1 * 0.5)
        v4 = (v1 * 0.7071067811865476)
        v5 = torch.erf(v4)
        v6 = (v3 + 1)
        v7 = (v2 * v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 2, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (17) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 4, 17, 17))), **{}):
Attempting to broadcast a dimension of length 17 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 17, 17]); but expected shape should be broadcastable to [1, 4, 32, 32]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''