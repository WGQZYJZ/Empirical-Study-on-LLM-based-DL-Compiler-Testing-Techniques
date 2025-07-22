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
        t1 = torch.mm(input2, input1)
        t2 = (t1 + torch.mm(input4, input1))
        t3 = torch.mm(input2, input4)
        t4 = (torch.mm(input3, input1) + torch.mm(input3, input2))
        t5 = (t3 + t4)
        return t5




func = Model().to('cuda')



input1 = torch.randn(4, 6)



input2 = torch.randn(4, 6)



input3 = torch.randn(6, 4)



input4 = torch.randn(4, 6)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x6 and 4x6)

jit:
Failed running call_function <built-in method mm of type object at 0x77e77ec699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 6)), FakeTensor(..., device='cuda:0', size=(4, 6))), **{}):
a and b must have same reduction dim, but got [4, 6] X [4, 6].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''