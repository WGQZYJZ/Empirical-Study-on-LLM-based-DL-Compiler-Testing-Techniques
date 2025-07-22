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
        self.layers = nn.Linear(2, 4)
        self.batchnorm = nn.BatchNorm1d(num_features=4)

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x), dim=1)
        x = x.flatten(start_dim=1)
        x = self.batchnorm(x)
        x = x.unsqueeze(dim=1).unsqueeze(dim=1)
        x = torch.concat((x, x), dim=0)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 8 elements not 4

jit:
Failed running call_function <function batch_norm at 0x750db5f69e50>(*(FakeTensor(..., size=(s0, 8)), FakeTensor(..., size=(4,)), FakeTensor(..., size=(4,)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 8 elements not 4

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''