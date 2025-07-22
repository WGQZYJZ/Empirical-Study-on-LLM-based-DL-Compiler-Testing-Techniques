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
        self.query_projection = torch.nn.Linear(64, 32)
        self.key_projection = torch.nn.Linear(64, 32)
        self.value_projection = torch.nn.Linear(64, 32)
        self.inv_scale_factor = torch.nn.Parameter(torch.Tensor([1.0]))
        self.dropout_p = 0.5

    def forward(self, x1, x2):
        q = self.query_projection(x1)
        k = self.key_projection(x2)
        v = self.value_projection(x2)
        return scaled_matmul_attention(q, k, v, self.inv_scale_factor, self.dropout_p)


func = Model().to('cpu')


x1 = torch.randn(1, 32, 64)

x2 = torch.randn(1, 128, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'scaled_matmul_attention' is not defined

jit:
NameError: name 'scaled_matmul_attention' is not defined

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''