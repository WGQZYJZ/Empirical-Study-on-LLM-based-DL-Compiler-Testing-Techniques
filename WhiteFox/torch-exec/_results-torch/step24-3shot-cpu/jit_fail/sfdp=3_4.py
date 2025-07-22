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

    def __init__(self, num_heads=1, dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.scale_factor = (self.num_heads * self.num_heads) ** 0.5

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.mul(self.scale_factor)
        v3 = F.softmax(v2, dim=-1)
        v3 = F.dropout(v3, self.dropout_p)
        v4 = torch.matmul(v3, x3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(2, 4, 5)

x2 = torch.randn(2, 4, 10)

x3 = torch.randn(2, 4, 16)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 10].

jit:
Failed running call_function <built-in method matmul of type object at 0x76b4acf96ec0>(*(FakeTensor(..., size=(2, 4, 5)), FakeTensor(..., size=(2, 10, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 10].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''