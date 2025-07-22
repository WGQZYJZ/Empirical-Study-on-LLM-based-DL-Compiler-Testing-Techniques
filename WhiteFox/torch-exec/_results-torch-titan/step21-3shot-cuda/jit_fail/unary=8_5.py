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



class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.layers = [torch.nn.Sequential(torch.nn.Conv2d(59, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1)), nn.BatchNorm2d(64), nn.ReLU())]

    def forward(self, x1):
        v1 = torch.nn.functional.relu(self.layers[0](x1))
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 59, 30, 40)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
Failed running call_module self___layers_0_1(*(FakeTensor(..., device='cuda:0', size=(1, 64, 30, 40)),), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''