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

    def __init__(self, negative_slope=1):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 15, (7, 9), 3, 3, 2, 1, 1)

    def forward(self, x):
        x2 = self.conv_t(x)
        x3 = (x2 > 0)
        x4 = (x2 * self.negative_slope)
        x5 = torch.where(x3, x2, x4)
        return x5




func = Model().to('cuda')



x = torch.randn(8, 3, 16, 16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'negative_slope'

jit:
negative_slope

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''