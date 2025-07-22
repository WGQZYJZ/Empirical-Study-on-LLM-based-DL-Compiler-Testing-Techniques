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
        self.linear = torch.nn.Linear(2, 2)
        self.batch_norm = torch.nn.BatchNorm2d(num_features=2, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v2 = (v2 * 2)
        v3 = v2.unsqueeze(1)
        v4 = self.batch_norm(v3)
        v5 = v4.squeeze(1)
        v6 = (v2 + v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 1 elements not 2

jit:
Failed running call_module L__self___batch_norm(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2)),), **{}):
running_mean should contain 1 elements not 2

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''