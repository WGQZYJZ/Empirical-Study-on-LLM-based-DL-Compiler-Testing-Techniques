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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, input_tensor):
        t1 = self.conv(input_tensor)
        t2 = t1.clone()
        t3 = (self.conv(t2) + 4)
        t4 = torch.clamp(t3, min=t3.mean(), max=(t3.mean() + 3))
        t5 = (t4 / 3)
        return t5




func = Model().to('cuda')



input_tensor = torch.randn(1, 3, 64, 64)


test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 8, 66, 66] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)),), **{}):
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 8, 66, 66] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''