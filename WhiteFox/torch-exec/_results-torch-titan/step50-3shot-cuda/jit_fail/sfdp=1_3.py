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

    def __init__(self, input_size: int, num_heads: int):
        super().__init__()
        self.q = torch.nn.Linear(input_size, input_size)
        self.k = torch.nn.Linear(input_size, input_size)
        self.v = torch.nn.Linear(input_size, input_size)
        self.output = torch.nn.Linear(input_size, input_size)
        self.input_size = input_size

    def forward(self, x):
        q = self.q(x)
        k = self.k(x)
        v = self.v(x)
        scaled_qk = torch.matmul(q, k.transpose((- 2), (- 1))).div((self.input_size ** 0.5))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = torch.matmul(dropout_qk, v)
        output = self.output(output)
        return output



input_size = 1
num_heads = 1
func = Model(1000, 16).to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___q(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''