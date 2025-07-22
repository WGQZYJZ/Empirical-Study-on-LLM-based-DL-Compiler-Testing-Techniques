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

    def forward(self, input_tensor, mask):
        qk = input_tensor
        scaled_qk = torch.matmul(qk, qk.transpose(-2, -1))
        scaled_qk = (scaled_qk / inv_scale_factor.view(inv_scale_factor.numel())).masked_fill(mask == 0, float('-inf'))
        dropout_qk = torch.nn.functional.dropout(torch.nn.Softmax(dim=-1)(scaled_qk), p=dropout_p)
        output = torch.nn.functional.linear(dropout_qk, value)
        return (output, mask)


func = Model().to('cpu')


n = 64
mask = torch.ones(n)

n = 64
n = 64
n = 64
input_tensor = torch.randn(n, n, n)

test_inputs = [mask, input_tensor]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got -2)

jit:
Failed running call_method transpose(*(FakeTensor(..., size=(64,)), -2, -1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got -2)

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''