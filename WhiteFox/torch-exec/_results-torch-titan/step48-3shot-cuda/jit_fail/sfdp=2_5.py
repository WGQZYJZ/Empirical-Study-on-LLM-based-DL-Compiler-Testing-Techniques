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

    def __init__(self, num_classes, hidden_size, drop_out):
        super().__init__()
        self.linear1 = torch.nn.Linear(hidden_size, hidden_size)
        self.linear2 = torch.nn.Linear(hidden_size, num_classes)
        self.dropout = torch.nn.Dropout(drop_out)

    def forward(self, x3, x4):
        v3 = self.linear1(x3)
        v4 = self.dropout(v3)
        v5 = self.linear2(v4)
        v7 = torch.matmul(v5, x4.transpose((- 2), (- 1)))
        return v7



num_classes = 1
hidden_size = 1
drop_out = 1

func = Model(num_classes, hidden_size, drop_out).to('cuda')



x3 = torch.randn(2, 10)



x4 = torch.randn(2, 128, 10)


test_inputs = [x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x10 and 1x1)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(2, 10)),), **{}):
a and b must have same reduction dim, but got [2, 10] X [1, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''