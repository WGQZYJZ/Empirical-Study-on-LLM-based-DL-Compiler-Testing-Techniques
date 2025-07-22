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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(6, 9, 2, stride=1, padding=0, dilation=1, output_padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(9, 10, 5, stride=3, padding=1, dilation=2, output_padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = (v2 + 3)
        v4 = torch.clamp(v3, min=0)
        v5 = torch.clamp(v4, max=6)
        v6 = (v1 * v5)
        v7 = (v6 / 6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 6, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (9) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 9, 9, 9)), FakeTensor(..., device='cuda:0', size=(1, 10, 32, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 10, 32, 32]); but expected shape should be broadcastable to [1, 9, 9, 9]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''