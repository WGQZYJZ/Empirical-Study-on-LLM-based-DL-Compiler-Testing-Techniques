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



class ModelNew1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 2, 2)
        self.dropout = torch.nn.Dropout(0.1)
        self.conv2 = torch.nn.Conv2d(6, 2, 2)
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x):
        x = self.conv(x)
        x = self.dropout(x)
        x = self.conv2(x)
        x = torch.rand_like(x)
        x = torch.nn.functional.dropout(x)
        x = self.linear1(x)
        return x




func = ModelNew1().to('cuda')



x1 = torch.randn(2, 3, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 6, 2, 2], expected input[2, 2, 1, 1] to have 6 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(2, 2, 1, 1)),), **{}):
Given groups=1, weight of size [2, 6, 2, 2], expected input[2, 2, 1, 1] to have 6 channels, but got 2 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''