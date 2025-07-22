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
        self.conv_transpose = torch.nn.ConvTranspose1d(in_channels=1, out_channels=1, kernel_size=3, stride=2, padding=1, dilation=1, groups=1, bias=True)

    def forward(self, x1, x2):
        v1 = self.conv_transpose(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v2 - x2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(100, 1, 10)



x2 = torch.randn(100, 1, 10)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (19) must match the size of tensor b (10) at non-singleton dimension 2

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(100, 1, 19)), FakeTensor(..., device='cuda:0', size=(100, 1, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([100, 1, 10]); but expected shape should be broadcastable to [100, 1, 19]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''