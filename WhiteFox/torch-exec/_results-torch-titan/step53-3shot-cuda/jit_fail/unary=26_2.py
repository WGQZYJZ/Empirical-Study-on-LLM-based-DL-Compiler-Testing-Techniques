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
        self.conv2d = torch.nn.ConvTranspose2d(336, 230, 3, stride=1, padding=1, bias=True)

    def forward(self, x4):
        p1 = self.conv2d(x4)
        p2 = (p1 > 0)
        p3 = (p1 * 0.775)
        p4 = torch.where(p2, p1, p3)
        return torch.quantize_per_tensor(torch.reshape(p4, (13, 230, (- 1))), (- 2.904), 0, dtype=2)




func = Model().to('cuda')



x4 = torch.randn(3, 336, 15, 10)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
shape '[13, 230, -1]' is invalid for input of size 103500

jit:
Failed running call_function <built-in method reshape of type object at 0x75d60a4699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 230, 15, 10)), (13, 230, -1)), **{}):
shape '[13, 230, -1]' is invalid for input of size 103500

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''