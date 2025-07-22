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



class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()

    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input1, input4)
        t = torch.mm(input4, input2)
        t = (t + t1)
        t = torch.mm(input3, input2)
        t = (t + t)
        return t




func = Model().to('cuda')



input1 = torch.randn(5, 8)



input2 = torch.randn(8, 16)



input3 = torch.randn(16, 5)



input4 = torch.randn(5, 16)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x8 and 5x16)

jit:
Failed running call_function <built-in method mm of type object at 0x73d518e699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 8)), FakeTensor(..., device='cuda:0', size=(5, 16))), **{}):
a and b must have same reduction dim, but got [5, 8] X [5, 16].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''