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
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 8, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(8, 8, 3, stride=2)
        self.conv5 = torch.nn.Conv2d(8, 8, 3, stride=2)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = torch.zeros_like(v2)
        t1 = self.conv3(v1)
        t2 = self.conv4(t1)
        t3 = (v2 + t2)
        t4 = self.conv5(t3)
        t5 = self.conv4(t4)
        v4 = (v3 + t5)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 57, 57)



x2 = torch.randn(1, 3, 57, 57)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (59) must match the size of tensor b (30) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 59, 59)), FakeTensor(..., device='cuda:0', size=(1, 8, 30, 30))), **{}):
Attempting to broadcast a dimension of length 30 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 30, 30]); but expected shape should be broadcastable to [1, 16, 59, 59]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''