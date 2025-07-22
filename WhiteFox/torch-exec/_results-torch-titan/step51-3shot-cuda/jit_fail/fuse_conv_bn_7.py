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
        self.t1 = torch.nn.Conv2d(3, 10, 3)
        self.t2 = torch.nn.Dropout(0.2)
        self.t3 = torch.nn.ConvTranspose2d(10, 3, 3)

    def forward(self, x):
        x = self.t1(x)
        x = self.t2(x)
        torch.manual_seed(1)
        x = self.t3(x)
        torch.manual_seed(1)
        x = self.t3(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 3, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 3, 3, 3], expected input[1, 3, 10, 10] to have 10 channels, but got 3 channels instead

jit:
Failed running call_module L__self___t3(*(FakeTensor(..., device='cuda:0', size=(1, 3, 10, 10)),), **{}):
Given transposed=1, weight of size [10, 3, 3, 3], expected input[1, 3, 10, 10] to have 10 channels, but got 3 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''