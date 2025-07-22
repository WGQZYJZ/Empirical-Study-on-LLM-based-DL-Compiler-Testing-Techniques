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

    def forward(self, qk, attn_mask, value):
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


func = Model().to('cpu')


qk = torch.randn(1, 2, 2, 16)

attn_mask = torch.randn(1, 2, 2, 2)

value = torch.randn(1, 2, 2, 16)

test_inputs = [qk, attn_mask, value]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 2, 2, 16)), FakeTensor(..., size=(1, 2, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 2, 2]); but expected shape should be broadcastable to [1, 2, 2, 16]

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''