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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(224, 256)
        self.other = other

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 + self.other)
        v3 = F.relu(v2)
        return v3



other = 1
func = Model(torch.randn(1, 224, 224)).to('cuda')



x = torch.randn(1, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (256) must match the size of tensor b (224) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 224, 256)), FakeTensor(..., device='cuda:0', size=(1, 224, 224))), **{}):
Attempting to broadcast a dimension of length 224 at -1! Mismatching argument at index 1 had torch.Size([1, 224, 224]); but expected shape should be broadcastable to [1, 224, 256]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''