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



class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(128, 128)
        self.k = torch.nn.Linear(128, 128)
        self.v = torch.nn.Linear(128, 128)
        self.scale = math.sqrt(128)

    def forward(self, q, k, v, attn_mask):
        qk = ((q @ k.transpose((- 2), (- 1))) / self.scale)
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v)
        return output



func = Model1().to('cuda')



x1 = torch.randn(1, 128)



x2 = torch.randn(1, 128)



x3 = torch.randn(1, 128)



x4 = torch.randn(1, 1, 128, 128)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x128 and 1x128)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 128, 128)), FakeTensor(..., device='cuda:0', size=(1, 128))), **{}):
a and b must have same reduction dim, but got [128, 128] X [1, 128].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''