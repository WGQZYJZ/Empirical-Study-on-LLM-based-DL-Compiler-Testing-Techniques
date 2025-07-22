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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 32, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = torch.nn.functional.interpolate(v1, scale_factor=(1.0, 2.0), mode='nearest')
        v3 = (v2 + x2)
        v4 = torch.nn.functional.relu(v3)
        v5 = self.conv2(v4)
        v6 = torch.nn.functional.interpolate(v5, scale_factor=(1.0, 1.0), mode='nearest')
        v7 = (v6 + x1)
        v8 = torch.nn.functional.relu(v7)
        v9 = self.conv3(v8)
        v10 = torch.nn.functional.interpolate(x1, scale_factor=(1.0, 2.0), mode='nearest')
        v11 = torch.nn.functional.interpolate(x2, scale_factor=(1.0, 2.0), mode='nearest')
        v12 = ((v9 + v10) + v11)
        v13 = torch.nn.functional.relu(v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 128)), FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 64, 64]); but expected shape should be broadcastable to [1, 16, 64, 128]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''