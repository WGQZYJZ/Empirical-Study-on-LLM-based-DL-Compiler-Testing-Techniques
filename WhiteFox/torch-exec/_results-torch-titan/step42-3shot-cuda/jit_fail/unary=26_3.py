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
        super(Model, self).__init__()
        self.conv_t = torch.nn.ConvTranspose3d(65, 1, 2, stride=2, dilation=1, bias=False, output_padding=0, padding=0)

    def forward(self, x8):
        y5 = torch.ones(x8.shape[2:])
        y6 = (y5 + 0.562)
        y7 = torch.clamp(y6, min=0.5, max=1)
        y8 = torch.ones(x8.shape).cuda()
        y9 = (y7 * y8)
        y10 = ((x8 * y5) * y9)
        return y10




func = Model().to('cuda')



x8 = torch.randn(9, 65, 7, 9, 9).to('cuda')


test_inputs = [x8]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(7, 9, 9)), FakeTensor(..., device='cuda:0', size=(9, 65, 7, 9, 9))), **{}):
Unhandled FakeTensor Device Propagation for aten.mul.Tensor, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''