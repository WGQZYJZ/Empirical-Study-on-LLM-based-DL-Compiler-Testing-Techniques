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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(128, 48, 3, stride=1, padding=1, dilation=1)
        self.conv2 = torch.nn.ConvTranspose2d(48, 128, 3, stride=2, padding=1, dilation=1, bias=True)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(t1)
        t3 = (t2 > 0)
        t4 = (t2 * self.negative_slope)
        t5 = torch.where(t3, t2, t4)
        return t5




negative_slope = (- 0.1)


func = Model(negative_slope).to('cuda')



x1 = torch.randn(32, 128, 25, 25)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'negative_slope'

jit:
negative_slope

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''