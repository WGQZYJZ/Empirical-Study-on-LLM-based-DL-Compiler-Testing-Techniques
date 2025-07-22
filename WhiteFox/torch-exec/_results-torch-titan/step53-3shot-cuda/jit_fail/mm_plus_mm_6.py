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
        v1 = torch.mm(input3, input4)
        v2 = torch.mm(input3, input4)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        return (v1 + v2)




func = Model().to('cuda')



input1 = torch.randn(35, 16)



input2 = torch.randn(35, 16)



input3 = torch.randn(35, 16)



input4 = torch.randn(35, 16)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (35x16 and 35x16)

jit:
Failed running call_function <built-in method mm of type object at 0x7ff1592699e0>(*(FakeTensor(..., device='cuda:0', size=(35, 16)), FakeTensor(..., device='cuda:0', size=(35, 16))), **{}):
a and b must have same reduction dim, but got [35, 16] X [35, 16].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''