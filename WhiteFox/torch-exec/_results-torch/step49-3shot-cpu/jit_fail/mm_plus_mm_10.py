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

    def forward(self, input1, input2):
        mm1 = torch.mm(input1, input2)
        mm2 = torch.mm(input2, input1)
        t2 = mm2 + input1
        t3 = mm1 + t2
        t5 = t2 + t3
        t6 = t3 + t2
        t7 = t6 + input2
        return t7



func = Model().to('cpu')


input1 = torch.randn(80, 97)

input2 = torch.randn(97, 80)

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
The size of tensor a (97) must match the size of tensor b (80) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(97, 97)), FakeTensor(..., size=(80, 97))), **{}):
Attempting to broadcast a dimension of length 80 at -2! Mismatching argument at index 1 had torch.Size([80, 97]); but expected shape should be broadcastable to [97, 97]

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''