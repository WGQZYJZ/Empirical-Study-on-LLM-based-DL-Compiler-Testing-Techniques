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
        self.other_conv = torch.nn.Conv2d(8, 8, 9)

    def forward(self, input_tensor):
        t1 = self.conv(input_tensor)
        t2 = (3 + t1)
        t3 = t2.clamp_(min=0, max=6)
        t4 = t3.div(6)
        t5 = t4.permute(0, 2, 3, 1)
        t6 = self.other_conv(t5)
        t7 = t6.clamp_max(6)
        t8 = t7.div(6)
        t9 = t8.permute(0, 3, 1, 2)
        t10 = t9.clamp_max(6)
        t11 = t10.div(6)
        return t11




func = Model().to('cuda')



input_tensor = torch.randn(3, 3, 64, 64)


test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 8, 9, 9], expected input[3, 66, 66, 8] to have 8 channels, but got 66 channels instead

jit:
Failed running call_module L__self___other_conv(*(FakeTensor(..., device='cuda:0', size=(3, 66, 66, 8)),), **{}):
Given groups=1, weight of size [8, 8, 9, 9], expected input[3, 66, 66, 8] to have 8 channels, but got 66 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''