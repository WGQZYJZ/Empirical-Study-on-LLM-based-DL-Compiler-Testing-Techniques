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
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        return self.bn((self.conv(x) + x))




func = Model().to('cuda')



x = torch.randn(1, 3, 6, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (6) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4)), FakeTensor(..., device='cuda:0', size=(1, 3, 6, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 6, 6]); but expected shape should be broadcastable to [1, 3, 4, 4]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''