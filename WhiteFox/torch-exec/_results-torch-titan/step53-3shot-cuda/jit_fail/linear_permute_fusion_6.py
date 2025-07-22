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
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x3):
        v0 = (x3 + self.linear.weight)
        v1 = v0.permute(0, 2, 1)
        v2 = v1.contiguous()
        return v2




func = Model().to('cuda')



x3 = torch.randn(1, 2, 2)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(4, 2), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 4 at -2! Mismatching argument at index 1 had torch.Size([4, 2]); but expected shape should be broadcastable to [1, 2, 2]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''