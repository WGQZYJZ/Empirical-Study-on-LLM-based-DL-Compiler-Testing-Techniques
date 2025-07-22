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
        self.conv = torch.nn.Conv2d(3, 32, 3, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv(x1)
        v3 = self.conv(x1)
        v4 = self.conv(x1)
        v5 = self.conv(x1)
        v6 = self.conv(x1)
        v7 = self.conv(x1)
        v8 = ((((((((v1 + v2) + v3) + v4) + v5) + v6) + v7) + x1) + x1)
        v9 = torch.relu(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (111) must match the size of tensor b (224) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 111, 111)), FakeTensor(..., device='cuda:0', size=(1, 3, 224, 224))), **{}):
Attempting to broadcast a dimension of length 224 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 224, 224]); but expected shape should be broadcastable to [1, 32, 111, 111]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''