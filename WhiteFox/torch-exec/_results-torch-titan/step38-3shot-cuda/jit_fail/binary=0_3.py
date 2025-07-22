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
        self.convA = torch.nn.Conv2d(2, 2, 2, stride=2, padding=2)
        self.convB = torch.nn.Conv2d(2, 2, 3, stride=3, padding=3)

    def forward(self, x1, other):
        v1 = self.convA(x1)
        v2 = self.convB(v1)
        v3 = (v2 * other)
        v4 = (v3 * other)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 16, 16)



other = torch.randn(1, 2, 4, 4)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 5, 5)), FakeTensor(..., device='cuda:0', size=(1, 2, 4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 4, 4]); but expected shape should be broadcastable to [1, 2, 5, 5]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''