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

    def forward(self, input1, input2, input3, input4):
        t = torch.mm(input1, input4)
        return (input3 + input1)




func = Model().to('cuda')



input1 = torch.randn(1)



input2 = torch.randn(1)



input3 = torch.randn(1)



input4 = torch.randn(1)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x73d518e699e0>(*(FakeTensor(..., device='cuda:0', size=(1,)), FakeTensor(..., device='cuda:0', size=(1,))), **{}):
a must be 2D

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''