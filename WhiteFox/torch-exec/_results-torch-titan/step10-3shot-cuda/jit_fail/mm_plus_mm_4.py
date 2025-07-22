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
        t1 = torch.mm(input1, input3)
        t2 = torch.mm(input3, input3)
        t3 = torch.mm(input4, input1)
        t4 = torch.mm(input2, input1)
        return (((t1 + t2) + t3) + t4)




func = Model().to('cuda')



input1 = torch.randn(5, 3)



input2 = torch.randn(5, 3)



input3 = torch.randn(5, 3)



input4 = torch.randn(5, 3)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x3 and 5x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7169d30699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 3)), FakeTensor(..., device='cuda:0', size=(5, 3))), **{}):
a and b must have same reduction dim, but got [5, 3] X [5, 3].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''