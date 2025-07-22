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



class ModelTanh_1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 7, 1, stride=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh_1().to('cuda')




x = torch.randn(1, 3, 32, 32, dtype=torch.float16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Input type (c10::Half) and bias type (float) should be the same

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32), dtype=torch.float16),), **{}):
Input type (c10::Half) and bias type (float) should be the same

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''