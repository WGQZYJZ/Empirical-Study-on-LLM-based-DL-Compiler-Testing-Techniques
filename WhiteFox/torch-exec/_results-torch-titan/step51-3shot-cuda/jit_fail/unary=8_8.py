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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(32, 15, 3, stride=2, padding=1, output_padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(15, 15, 3, stride=2, padding=1, output_padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(15, 32, 3, stride=1, padding=0, output_padding=0)

    def forward(self, x1):
        x2 = self.conv_transpose1(x1)
        x3 = self.conv_transpose2(x2)
        x4 = self.conv_transpose3(x3)
        x5 = (x1 + x4)
        v1 = (x5 + 3)
        v2 = torch.clamp(v1, min=0)
        v3 = torch.clamp(v2, max=6)
        v4 = (x5 * v3)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 32, 35, 35)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (35) must match the size of tensor b (140) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 35, 35)), FakeTensor(..., device='cuda:0', size=(1, 32, 140, 140))), **{}):
Attempting to broadcast a dimension of length 140 at -1! Mismatching argument at index 1 had torch.Size([1, 32, 140, 140]); but expected shape should be broadcastable to [1, 32, 35, 35]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''