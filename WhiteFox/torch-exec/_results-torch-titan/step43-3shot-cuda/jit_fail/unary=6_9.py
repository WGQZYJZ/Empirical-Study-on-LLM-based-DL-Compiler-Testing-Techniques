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
        self.quant = torch.quantization.QuantStub()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.relu = torch.nn.ReLU()
        self.dequant = torch.quantization.DeQuantStub()
        self.add = torch.nn.quantized.FloatFunctional()

    def forward(self, x1):
        x1 = self.quant(x1)
        x2 = self.conv(x1)
        x3 = torch.clamp_min(x2, 0)
        x4 = torch.clamp_max(x3, 6)
        x5 = self.conv(x1)
        x6 = self.relu(x5)
        x7 = self.dequant(x6)
        x8 = self.add.add(x2, x7)
        x9 = self.add.mul(x8, x4)
        x10 = self.add.div(x9, self.add.scalar(6))
        return x10




func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'FloatFunctional' object has no attribute 'div'

jit:
div

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''