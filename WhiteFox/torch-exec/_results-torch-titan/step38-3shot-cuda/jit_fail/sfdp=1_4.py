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

    def forward(self, q, k, v, scale_factor, is_training=True):
        q = torch.matmul(q, k.transpose(1, 0))
        scaled_qk = q.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5, training=is_training)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cuda')



q = torch.randn(3, 16)



k = torch.randn(16, 28)



v = torch.randn(16, 28)

scale_factor = 1

test_inputs = [q, k, v, scale_factor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x16 and 28x16)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b533d6699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 16)), FakeTensor(..., device='cuda:0', size=(28, 16))), **{}):
a and b must have same reduction dim, but got [3, 16] X [28, 16].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''