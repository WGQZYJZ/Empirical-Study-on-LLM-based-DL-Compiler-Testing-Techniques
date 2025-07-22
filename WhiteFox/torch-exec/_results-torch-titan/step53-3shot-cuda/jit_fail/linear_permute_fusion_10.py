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

    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 1)
        self.linear_2 = torch.nn.Linear(2, 1)

    def forward(self, x3, x4, x5):
        v2 = x4.flatten(0, 1)
        v3 = x5.flatten(0, 1)
        v4 = torch.cat((v2, v3), 0)
        v5 = torch.stack((v2, v3), 0)
        v6 = v4.transpose(0, 1)
        return (v4, v5, v6)
        v1 = x3
        v2 = torch.nn.functional.linear(v1, self.linear_1.weight, self.linear_1.bias)
        v3 = torch.nn.functional.linear(v1, self.linear_2.weight, self.linear_2.bias)
        v4 = (v2 == v3)
        v5 = (v2 > v3)
        v6 = (v4 | v5)
        return (v4, v5, v6)




func = Model().to('cuda')



x3 = torch.randn(1, 2, 2)



x4 = torch.randn(2, 1)



x5 = torch.randn(1, 2, 1)


test_inputs = [x3, x4, x5]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 1 and 2

jit:
Failed running call_function <built-in method stack of type object at 0x76cb1c0699e0>(*((FakeTensor(..., device='cuda:0', size=(2,)), FakeTensor(..., device='cuda:0', size=(2, 1))), 0), **{}):
stack expects each tensor to be equal size, but got torch.Size([2]) at entry 0and torch.Size([2, 1]) at entry 1

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''