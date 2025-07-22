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
        self.conv_transpose5 = torch.nn.ConvTranspose1d(2, 1, 5, stride=4, padding=3)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(32, 32, 9, stride=2)
        self.conv_transpose3 = torch.nn.ConvTranspose3d(75, 17, 2, stride=2)

    def forward(self, input):
        v1 = self.conv_transpose5(input)
        v2 = torch.zeros([1, 1, 10]).fill_(3)
        v3 = (v2 + v1)
        v4 = torch.clamp(v3, min=0)
        v5 = torch.clamp(v4, max=6)
        v6 = (v1 * v5)
        v7 = (v6 / 6)
        v8 = self.conv_transpose2(v7)
        v9 = torch.zeros([1, 32, 1, 1]).fill_(3)
        v10 = (v9 + v8)
        v11 = torch.clamp(v10, min=0)
        v12 = torch.clamp(v11, max=6)
        v13 = (v8 * v12)
        v14 = (v13 / 6)
        v15 = self.conv_transpose3(v14)
        v16 = torch.zeros([1, 75, 2, 2, 2]).fill_(3)
        v17 = (v16 + v15)
        v18 = torch.clamp(v17, min=0)
        v19 = torch.clamp(v18, max=6)
        v20 = (v15 * v19)
        v21 = (v20 / 6)
        return v21




func = Model().to('cuda')



input = torch.randn(1, 2, 50)


test_inputs = [input]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (195) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 1, 10)), FakeTensor(..., device='cuda:0', size=(1, 1, 195))), **{}):
Attempting to broadcast a dimension of length 195 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 195]); but expected shape should be broadcastable to [1, 1, 10]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''