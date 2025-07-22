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

    def forward(self, x1):
        z1 = torch.add(torch.nn.functional.dropout(x1, 0.0, False, False), torch.tensor([40], dtype=torch.float64))
        z2 = torch.add(z1, 1.5)
        s1 = torch.pow(z2, 2)
        x2 = torch.add(torch.nn.functional.interpolate(s1, [30], mode='linear', align_corners=True), 0.6)
        x3 = torch.add(torch.nn.functional.silu(x2), 21)
        x4 = torch.nn.functional.adaptive_avg_pool2d(x3, (769,))
        x5 = torch.nn.functional.silu(x4, self.a61, self.a61214)



func = Model().to('cuda')



x1 = torch.randn((1, 3, 4))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in method add of type object at 0x7570450699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4)), FakeTensor(..., size=(1,), dtype=torch.float64)), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''