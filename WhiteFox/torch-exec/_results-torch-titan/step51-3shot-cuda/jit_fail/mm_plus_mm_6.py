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

    def __init__(self, hidden):
        super().__init__()
        self.hidden = hidden

    def forward(self, input, hidden):
        t1 = torch.nn.ReLU()(hidden)
        t2 = torch.mm(input, t1)
        t3 = (t1 + t2)
        t4 = torch.mm(input, t2)
        t5 = (t3 + t4)
        return (t5, t4)



hidden = 1

func = Model(hidden).to('cuda')



input1 = torch.randn(100, 100)



input2 = torch.randn(100)


test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
mat2 must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x72c26b8699e0>(*(FakeTensor(..., device='cuda:0', size=(100, 100)), FakeTensor(..., device='cuda:0', size=(100,))), **{}):
b must be 2D

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''