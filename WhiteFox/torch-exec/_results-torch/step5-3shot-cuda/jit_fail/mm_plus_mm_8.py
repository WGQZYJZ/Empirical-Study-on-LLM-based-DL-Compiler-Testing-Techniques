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
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = t1 + t2
        t4 = torch.sigmoid(t3)
        t5 = torch.tanh(t4)
        return t5



func = Model().to('cuda')


input1 = torch.randn(1, 64)

input2 = torch.randn(64, 1)

input3 = torch.randn(64, 64)

input4 = torch.randn(1, 64)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x64 and 1x64)

jit:
Failed running call_function <built-in method mm of type object at 0x7610a6f96ec0>(*(FakeTensor(..., device='cuda:0', size=(s3, s4)), FakeTensor(..., device='cuda:0', size=(1, s2))), **{}):
a and b must have same reduction dim, but got [s3, s4] X [1, s2].

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''