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
        self.conv = torch.nn.Conv2d(16, 32, (3, 3), (2, 2), padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 * 0.75)
        return v2




func = Model().to('cuda')




x = torch.randn(1, 16, 64, 64, dtype=torch.float16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Input type (c10::Half) and bias type (float) should be the same

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64), dtype=torch.float16),), **{}):
Input type (c10::Half) and bias type (float) should be the same

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''