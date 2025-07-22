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
        self.biasb = torch.nn.Parameter(torch.zeros(25920, 1, 1))
        self.scaleb = torch.nn.Parameter(torch.full((25920, 1, 1), 0.21))

    def forward(self, qt, k):
        a1 = torch.matmul(qt, k.transpose(-2, -1))
        a2 = a1 * self.scaleb
        a3 = a2.softmax(dim=-1)
        a4 = torch.nn.functional.dropout(a3, p=0.7978529607897845)
        a5 = torch.matmul(a4, self.biasb)
        a6 = a5 + qt
        return a6


func = Model().to('cuda')


qt = torch.randn(1, 3, 64, 64)

k = torch.randn(1, 3, 64, 64)

test_inputs = [qt, k]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (25920) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(25920, 1, 1), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 25920 at -3! Mismatching argument at index 1 had torch.Size([25920, 1, 1]); but expected shape should be broadcastable to [1, 3, 64, 64]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''