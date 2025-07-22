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
        super().__init__()
        self.layers = nn.Sequential(nn.BatchNorm2d(2), nn.ReLU(inplace=True), nn.Linear(2, 4))

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack(([x] * 2), dim=1)
        x = torch.cat((x, x, x), dim=2)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
expected 4D input (got 3D input)

jit:
Failed running call_module L__self___layers_0(*(FakeTensor(..., device='cuda:0', size=(2, 2, 2)),), **{}):
expected 4D input (got 3D input)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''