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



class Model1(torch.nn.Module):

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv1d(3, 19, kernel_size=(3,), stride=(1,), padding=(1,))
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1, self.min, self.max)
        return v2




min = None


max = None


func = Model1(min, max).to('cuda')



x1 = torch.randn(2, 3, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
torch.clamp: At least one of 'min' or 'max' must not be None

jit:
Failed running call_function <built-in method clamp of type object at 0x7ad33c4699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 19, 64)), None, None), **{}):
clamp called but both min and max are none!

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''