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

    def forward(self, input0, input1, input2, input3):
        t0 = torch.mm(input0, input1)
        t1 = torch.mm(input2, input3)
        t2 = torch.mm(t0, t1)
        return torch.mm(t0, t1)




func = Model().to('cuda')



input0 = torch.randn(1, 1)



input1 = torch.randn(5, 5)



input2 = torch.randn(5, 5)



input3 = torch.randn(5, 5)


test_inputs = [input0, input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 5x5)

jit:
Failed running call_function <built-in method mm of type object at 0x7822a94699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1)), FakeTensor(..., device='cuda:0', size=(5, 5))), **{}):
a and b must have same reduction dim, but got [1, 1] X [5, 5].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''