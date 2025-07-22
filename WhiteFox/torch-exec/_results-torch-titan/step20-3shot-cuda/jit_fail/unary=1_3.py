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

        def __linear__(x1):
            return x1

        def __weight__(out_features):
            return torch.tensor((torch.rand(out_features) * 100))

        def __bias__(out_features):
            return torch.tensor(torch.rand(out_features))
        self.linear1 = torch.nn.Linear(900, 2200, bias=True)
        self.linear2 = torch.nn.Linear(2200, 900, bias=True)
        self.linear1.weight = torch.nn.Parameter(__linear__(__weight__(2200)))
        self.linear1.bias = torch.nn.Parameter(__bias__(2200))
        self.linear2.weight = torch.nn.Parameter(__linear__(__weight__(900)))
        self.linear2.bias = torch.nn.Parameter(__bias__(900))

    def forward(self, x1):
        t1 = self.linear1(x1)
        t2 = (t1 * 0.5)
        t3 = (t1 + (((t1 * t1) * t1) * 0.044715))
        t4 = (t3 * 0.7978845608028654)
        t5 = torch.tanh(t4)
        t6 = (t5 + 1)
        t7 = (t2 * t6)
        return self.linear2(t7)



func = Model().to('cuda')



x1 = torch.randn(1, 900)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat2 must be a matrix, got 1-D tensor

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 900)),), **{}):
b must be 2D

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''