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
        self.conv1 = torch.nn.Conv2d(10, 20, 5, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, stride=2, padding=1)

    def forward(self, x1):
        v1 = F.relu6(inputs)
        v2 = F.relu(self.conv1(v1))
        v3 = F.relu(self.conv2(v2))
        return v3



func = Model().to('cpu')


x1 = torch.randn(16, 10, 56, 56)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'inputs' is not defined

jit:
NameError: name 'inputs' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''