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
        self.conv_t1 = torch.nn.ConvTranspose2d(292, 292, 3, stride=1, padding=1, bias=False)
        self.conv_t2 = torch.nn.ConvTranspose2d(292, 15, 5, stride=2, padding=3, bias=False)

    def forward(self, x8):
        v5 = self.conv_t1(x8)
        v6 = (v5 > 0)
        v7 = (v5 * (- 1.6052))
        v8 = torch.where(v6, v5, v7)
        v9 = self.conv_t2(x8)
        v10 = (v9 > 0)
        v11 = (v9 * (- 1.1195))
        v12 = torch.where(v10, v9, v11)
        return (v8 + v12)




func = Model().to('cuda')



x8 = torch.randn(24, 292, 77, 93)


test_inputs = [x8]

# JIT_FAIL
'''
direct:
The size of tensor a (93) must match the size of tensor b (183) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(24, 292, 77, 93)), FakeTensor(..., device='cuda:0', size=(24, 15, 151, 183))), **{}):
Attempting to broadcast a dimension of length 183 at -1! Mismatching argument at index 1 had torch.Size([24, 15, 151, 183]); but expected shape should be broadcastable to [24, 292, 77, 93]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''