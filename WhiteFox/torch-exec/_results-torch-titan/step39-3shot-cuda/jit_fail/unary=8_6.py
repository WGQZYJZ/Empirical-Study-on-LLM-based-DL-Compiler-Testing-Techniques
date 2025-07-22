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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=5, padding=0, output_padding=0, bias=False)
        self.conv = torch.nn.Conv2d(3, 2, kernel_size=5, padding=2)

    def forward(self, x1, x2):
        x2 = self.conv(x2)
        v1 = self.conv_transpose(x1)
        v2 = (v1 + x2)
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)



x2 = torch.randn(1, 3, 8, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (20) must match the size of tensor b (8) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 20, 20)), FakeTensor(..., device='cuda:0', size=(1, 2, 8, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 8, 8]); but expected shape should be broadcastable to [1, 8, 20, 20]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''