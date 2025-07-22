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
        v1 = input1.mm(input2)
        v2 = input3.mm(input4)
        v3 = (v1 + v2)
        r = torch.mm(v3, input4)
        return r




func = Model().to('cuda')



input1 = torch.randn(2, 10)



input2 = torch.randn(20, 2)



input3 = torch.randn(2, 20)



input4 = torch.randn(21, 2)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x10 and 20x2)

jit:
Failed running call_method mm(*(FakeTensor(..., device='cuda:0', size=(2, 10)), FakeTensor(..., device='cuda:0', size=(20, 2))), **{}):
a and b must have same reduction dim, but got [2, 10] X [20, 2].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''