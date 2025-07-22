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
        self.conv = torch.nn.Conv3d(3, 8, 1, stride=1, padding=1)
        self.other_conv = torch.nn.Conv1d(8, 8, 9)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (3 + v1)
        v3 = v2.relu6()
        v4 = v3.normalize(1)
        v5 = self.other_conv(v4)
        v6 = (3 + v5)
        v7 = v6.relu6()
        v8 = v7.normalize(1)
        return v8




func = Model().to('cuda')



x1 = torch.randn(5, 3, 64, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'relu6'

jit:
Failed running call_method relu6(*(FakeTensor(..., device='cuda:0', size=(5, 8, 66, 66, 66)),), **{}):
'FakeTensor' object has no attribute 'relu6'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''