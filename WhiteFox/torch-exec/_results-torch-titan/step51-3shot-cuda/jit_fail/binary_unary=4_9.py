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
        self.linear = torch.nn.Linear(768, 2048)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        v3 = nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 768)



other = torch.randn(768)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (2048) must match the size of tensor b (768) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2048)), FakeTensor(..., device='cuda:0', size=(768,))), **{}):
Attempting to broadcast a dimension of length 768 at -1! Mismatching argument at index 1 had torch.Size([768]); but expected shape should be broadcastable to [1, 2048]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''