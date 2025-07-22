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

class A(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_0 = nn.ConvTranspose2d(3, 2, 3, padding=1, stride=2)
        self.conv_1 = nn.ConvTranspose2d(2, 3, 3, padding=1, stride=2)

    def forward(self, x):
        y1 = F.relu(self.conv_0(x))
        output = F.relu(self.conv_1(y))
        return output



func = A().to('cpu')


x_1 = torch.randn(1, 3, 32, 32)

test_inputs = [x_1]

# JIT_FAIL
'''
direct:
name 'y' is not defined

jit:
NameError: name 'y' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''