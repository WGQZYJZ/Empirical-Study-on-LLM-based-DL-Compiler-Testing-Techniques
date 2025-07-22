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

    def forward(self, input):
        t1 = torch.matmul(input, input)
        a1 = torch.nn.ReLU(t1)
        a2 = torch.nn.ReLU(t1)
        t2 = torch.matmul(input, input)
        a3 = torch.nn.ReLU(t2)
        a4 = torch.nn.ReLU(t2)
        return (((a1 + a2) + a3) + a4)




func = Model().to('cuda')



input = torch.arange(6).reshape(2, 3)


test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 2x3)

jit:
Failed running call_function <built-in method matmul of type object at 0x7480ada699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(2, 3), dtype=torch.int64)), **{}):
a and b must have same reduction dim, but got [2, 3] X [2, 3].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''