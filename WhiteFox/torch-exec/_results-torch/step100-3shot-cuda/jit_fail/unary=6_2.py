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
        self.conv1 = torch.nn.Conv2d(3, 32, (4, 1), stride=(2, 1), padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, (1, 4), stride=(1, 1), padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 + 3
        v4 = torch.clamp(v3, min=0, max=6)
        v5 = torch.mul(v1, v4)
        v6 = v5 / 6
        return v6.unsqueeze(-1)



func = Model().to('cuda')


x1 = torch.randn(1, 3, 128, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (258) must match the size of tensor b (257) at non-singleton dimension 3

jit:
Failed running call_function <built-in method mul of type object at 0x72eb15196ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64, s0 + 2)), FakeTensor(..., device='cuda:0', size=(1, 64, 66, s0 + 1))), **{}):
The size of tensor a (s0 + 2) must match the size of tensor b (s0 + 1) at non-singleton dimension 3)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''