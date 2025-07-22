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
        self.avgpool = torch.nn.AvgPool2d(kernel_size=(8, 8), stride=(10, 10))
        self.linear = torch.nn.Linear((224 * 224), 4096)

    def forward(self, x1):
        v1 = self.avgpool(x1)
        v2 = v1.view(((- 1), self.linear.in_features))
        v3 = self.linear(v2)
        v4 = (v3 * 0.5)
        v5 = (v3 * 0.7071068)
        v7 = v5.mean((- 1))
        v8 = (v4 + v7)
        v9 = v8.reshape(((- 1), 3, 32, 32))
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 7, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 50176]' is invalid for input of size 700

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 7, 10, 10)), (-1, 50176)), **{}):
shape '[-1, 50176]' is invalid for input of size 700

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''