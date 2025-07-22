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
        self.linear = torch.nn.Linear(16, 32)

    def forward(self, t1, t2):
        v1 = self.linear(t1)
        v2 = (v1 + t2)
        v3 = v2.relu()
        return v3



func = Model().to('cuda')



t1 = torch.randn(1, 16)



t2 = torch.zeros(1, 16)


test_inputs = [t1, t2]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 32)), FakeTensor(..., device='cuda:0', size=(1, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([1, 16]); but expected shape should be broadcastable to [1, 32]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''