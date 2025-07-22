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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, inp)
        v2 = (v1 + x2)
        return v2




func = Model().to('cuda')



x1 = torch.randn(238, 38)



x2 = torch.randn(2, 1)



inp = torch.randn(38, 1)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (238) must match the size of tensor b (2) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(238, 1)), FakeTensor(..., device='cuda:0', size=(2, 1))), **{}):
Attempting to broadcast a dimension of length 2 at -2! Mismatching argument at index 1 had torch.Size([2, 1]); but expected shape should be broadcastable to [238, 1]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''