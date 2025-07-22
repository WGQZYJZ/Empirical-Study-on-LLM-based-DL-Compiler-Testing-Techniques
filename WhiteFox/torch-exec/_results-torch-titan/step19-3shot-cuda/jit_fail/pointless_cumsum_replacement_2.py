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
        self.model = torch.nn.modules.rnn.GRUCell(10, 20, bias=False)

    def forward(self, input, hx):
        (h1, c) = self.model(input, hx)
        return (h1, torch.cat([h1, c], 1))




func = Model().to('cuda')



input = torch.randn(1, 10, device='cuda:0')



hx = torch.randn(1, 20, device='cuda:0')


test_inputs = [input, hx]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 2, got 1)

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 20)), 1), **{}):
index 1 is out of bounds for dimension 0 with size 1

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''