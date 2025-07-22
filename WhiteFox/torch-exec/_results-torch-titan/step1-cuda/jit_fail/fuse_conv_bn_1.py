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
        self.conv = torch.nn.Conv2d(3, 3, 3, bias=True)
        self.batch_norm = torch.nn.BatchNorm2d(3, affine=False)

    def forward(self, x1):
        v1 = F.relu(self.conv(x1))
        v2 = F.batch_norm(x1, None, None, None, None, False, 0, self.conv.weight, self.conv.bias)
        return v1



func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
batch_norm() takes from 3 to 8 positional arguments but 9 were given

jit:
Failed running call_function <function batch_norm at 0x7c3914724b80>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32)), None, None, None, None, False, 0, Parameter(FakeTensor(..., device='cuda:0', size=(3, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(3,), requires_grad=True))), **{}):
batch_norm() takes from 3 to 8 positional arguments but 9 were given

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''