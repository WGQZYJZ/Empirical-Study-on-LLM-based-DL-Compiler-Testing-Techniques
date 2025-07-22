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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.ln1 = torch.nn.LayerNorm([1, 8, 8])
        self.ln2 = torch.nn.LayerNorm([1, 8, 8])

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = (v1 + v2)
        v4 = self.ln1(v3)
        v5 = self.ln2(v3)
        v6 = v4.mul(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given normalized_shape=[1, 8, 8], expected input with shape [*, 1, 8, 8], but got input of size[1, 8, 66, 66]

jit:
Failed running call_module L__self___ln1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)),), **{}):
Given normalized_shape=[1, 8, 8], expected input with shape [1, 8, 8], but got input of size torch.Size([1, 8, 66, 66])

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''