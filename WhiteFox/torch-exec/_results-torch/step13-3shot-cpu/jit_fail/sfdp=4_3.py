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
        self.query = torch.nn.Parameter(torch.empty(20, 10).uniform_(-0.1, 0.1))
        self.key = torch.nn.Parameter(torch.empty(20, 20).uniform_(-0.1, 0.1))
        self.value = torch.nn.Parameter(torch.empty(20, 10).uniform_(-0.1, 0.1))

    def forward(self, x1):
        q = self.query
        k = self.key
        v = self.value
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        if x1 is not None:
            attn_mask = (x1 == 0).float().unsqueeze(1).unsqueeze(1).expand(x1.size(0), 1, x1.size(1), x1.size(1))
            qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output


func = Model().to('cpu')


x1 = torch.arange(20).unsqueeze(0).unsqueeze(1).expand(1, 1, 20)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x10 and 20x20)

jit:
Failed running call_function <built-in function matmul>(*(Parameter(FakeTensor(..., size=(20, 10), requires_grad=True)), FakeTensor(..., size=(20, 20), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [20, 10] X [20, 20].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''