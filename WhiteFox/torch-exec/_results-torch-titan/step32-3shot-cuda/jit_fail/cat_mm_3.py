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

    def forward(self, x):
        t1 = torch.zeros([6, 4])
        t2 = torch.zeros([4, 6])
        t1 = (t1 + t2)
        t3 = torch.zeros([6, 4])
        v1 = torch.view_as_strided(t1, shape=[3, 2, 2], stride=[1, 2, 2], writeable=True)
        v2 = (torch.zeros([1, 1]) + v1[:, 0, 0])
        return v2




func = Model().to('cuda')



x = torch.zeros([2, 2])


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(6, 4)), FakeTensor(..., size=(4, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([4, 6]); but expected shape should be broadcastable to [6, 4]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''