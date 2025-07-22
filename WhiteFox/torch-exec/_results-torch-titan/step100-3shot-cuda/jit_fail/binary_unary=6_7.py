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
        self.linear = torch.nn.Linear(32, 16)

    def forward(self, x1):
        x = self.linear(x1)
        x = (x - other)
        x = relu(x)
        return x



func = Model().to('cuda')



x1 = torch.randn(1, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (512) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 16)), FakeTensor(..., size=(1, 512))), **{}):
Attempting to broadcast a dimension of length 512 at -1! Mismatching argument at index 1 had torch.Size([1, 512]); but expected shape should be broadcastable to [1, 16]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''