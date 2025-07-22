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
        self.attention_dropout = 0.1
        self.attention_mask = torch.tensor([[[[0, 0], [0, 0]]]], dtype=torch.float)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.matmul1 = torch.nn.Linear(288, 288, bias=False)
        self.matmul2 = torch.nn.Linear(288, 288, bias=False)
        self.matmul3 = torch.nn.Linear(288, 288, bias=False)

    def forward(self, x):
        v0 = self.matmul1(x)
        v1 = self.matmul2(x)
        qk = v0 @ v1.transpose(-2, -1)
        qk = qk / math.sqrt(math.sqrt(qk.size(-1)))
        qk = qk + self.attention_mask
        attn_weight = self.softmax(qk)
        v3 = self.matmul3(x)
        v4 = attn_weight @ v3
        v5 = v4 * v2
        return v5


func = Model().to('cpu')



x = torch.randn(1, 288, dtype=torch.float)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x288)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, 1, 2, 2)), FakeTensor(..., size=(1, 288))), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 288].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''