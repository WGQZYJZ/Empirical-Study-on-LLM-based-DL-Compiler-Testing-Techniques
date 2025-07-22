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

    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input2, input3)
        t2 = torch.mm(input3, input1)
        t3 = t1 + t2
        return t3



func = Model().to('cpu')


input1 = torch.randn(5, 3)

input2 = torch.randn(3, 3)

input3 = torch.randn(3, 5)

input4 = torch.randn(5, 3)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(3, 5)), FakeTensor(..., size=(3, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([3, 3]); but expected shape should be broadcastable to [3, 5]

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''