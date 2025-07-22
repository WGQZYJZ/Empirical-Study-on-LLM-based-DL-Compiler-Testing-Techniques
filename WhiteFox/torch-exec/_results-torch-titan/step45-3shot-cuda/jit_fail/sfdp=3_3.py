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
        self.m1 = torch.nn.Linear(4, 8)
        self.m2 = torch.nn.Linear(8, 8)

    def forward(self, x1):
        qk = torch.matmul(x1, self.m1.weight.t())
        v1 = self.m1(x1)
        v2 = torch.matmul(v1, self.m2.weight.t())
        scale_factor = (- 0.5)
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=1)
        dropout_p = 0.2
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v2)
        return output



func = Model().to('cuda')



x1 = torch.randn(2, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x8 and 2x8)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(2, 8)), FakeTensor(..., device='cuda:0', size=(2, 8))), **{}):
a and b must have same reduction dim, but got [2, 8] X [2, 8].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''