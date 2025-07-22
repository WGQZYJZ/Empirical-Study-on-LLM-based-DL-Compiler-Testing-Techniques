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

    def forward(self, inp):
        v1 = torch.mm(inp, inp)
        v2 = (v1 + torch.eye(2, dtype=torch.float))
        return v2.size(0)




func = Model().to('cuda')




inp = torch.eye(5, dtype=torch.float)


test_inputs = [inp]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (2) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., size=(2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([2, 2]); but expected shape should be broadcastable to [5, 5]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''