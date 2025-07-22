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
        super(Model, self).__init__()

    def forward(self, input1, input2):
        t1 = input1
        t2 = input2
        t3 = t1
        for i in range(100):
            if i % 2 == 0:
                t3 = t1 + torch.mm(t2, t3)
            else:
                t3 = t1 + torch.mm(t3, t2)
        return t3 + t1



func = Model().to('cpu')


input1 = torch.randn(4, 10)

input2 = torch.randn(10, 4)

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (10) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(4, 10)), FakeTensor(..., size=(10, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -2! Mismatching argument at index 1 had torch.Size([10, 10]); but expected shape should be broadcastable to [4, 10]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''