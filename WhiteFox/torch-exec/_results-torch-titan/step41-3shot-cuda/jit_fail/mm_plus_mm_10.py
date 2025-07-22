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

    def forward(self, in0, in1, in2, in3, in4):
        t1 = (torch.mm(in0, in1) + torch.mm(in2, torch.mm(in3, in4)))
        return t1




func = Model().to('cuda')



in0 = torch.randn(3, 3)



in1 = torch.randn(3, 3)



in2 = torch.randn(2, 3)



in3 = torch.randn(2, 2)



in4 = torch.randn(3, 2)


test_inputs = [in0, in1, in2, in3, in4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 3x2)

jit:
Failed running call_function <built-in method mm of type object at 0x7a4b8bc699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., device='cuda:0', size=(3, 2))), **{}):
a and b must have same reduction dim, but got [2, 2] X [3, 2].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''