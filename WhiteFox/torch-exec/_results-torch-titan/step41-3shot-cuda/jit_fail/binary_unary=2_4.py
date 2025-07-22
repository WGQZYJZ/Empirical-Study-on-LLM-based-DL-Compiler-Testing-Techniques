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
        self.conv1 = torch.nn.Conv2d(3, 2, 1, stride=1, padding=0)
        self.conv2 = torch.nn.ConvTranspose2d(2, 4, 1, stride=3, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        t1 = (v1 - 0.6)
        v2 = self.conv2(v1)
        t2 = (v2 + x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (296) must match the size of tensor b (100) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 296, 296)), FakeTensor(..., device='cuda:0', size=(1, 3, 100, 100))), **{}):
Attempting to broadcast a dimension of length 100 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 100, 100]); but expected shape should be broadcastable to [1, 4, 296, 296]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''