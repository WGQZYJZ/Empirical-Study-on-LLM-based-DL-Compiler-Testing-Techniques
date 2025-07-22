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
        self.conv2 = torch.nn.Conv2d(2, out_channels=2, kernel_size=5, stride=3, padding=3)
        self.soft_relu = torch.nn.Softsign()

    def forward(self, x1):
        v1 = self.conv2()
        v2 = self.soft_relu(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() missing 1 required positional argument: 'input'

jit:
Failed running call_module L__self___conv2(*(), **{}):
forward() missing 1 required positional argument: 'input'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''