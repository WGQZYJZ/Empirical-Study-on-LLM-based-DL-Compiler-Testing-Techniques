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

    def __init__(self, max_value=torch.tensor(1.68)):
        super(Model, self).__init__()
        self.tanh = torch.nn.Tanh()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 1, 3, stride=2, padding=0)
        self.clamp_max = torch.nn.Hardtanh(max_value=max_value.item())
        self.output = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_max(v1, max_value)
        v3 = self.tanh(v2)
        v4 = self.output(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 24, 24)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'max_value' is not defined

jit:
name 'max_value' is not defined

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''