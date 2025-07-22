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
        self.dense1 = torch.nn.Linear(4, 20)
        self.q_linear = torch.nn.Linear(4, 20)
        self.k_linear = torch.nn.Linear(4, 20)
        self.v_linear = torch.nn.Linear(4, 20)

    def forward(self, query, key, value, mask):
        (b_s, nq) = query.shape[:2]
        nk = key.shape[2]
        nv = value.shape[2]
        q = torch.reshape(self.q_linear(query), [b_s, nq, 1, 20])
        k = torch.reshape(self.k_linear(key), [b_s, 1, nk, 20])
        v = torch.reshape(self.v_linear(value), [b_s, 1, nv, 20])
        dots = torch.matmul(q, k)
        dots = dots / math.sqrt(20)
        if mask is not None:
            mask_value = -1000000000.0
            dots = torch.where(mask == 0, dots, mask_value)
        attn_weight = torch.softmax(dots, dim=-1)
        output = torch.matmul(attn_weight, v)
        return output


func = Model().to('cpu')


batch_size = 4
query = torch.randn(batch_size, 22, 4)

batch_size = 4
key = torch.randn(batch_size, 50, 4)

batch_size = 4
value = torch.randn(batch_size, 50, 4)

batch_size = 4

mask = torch.ones([batch_size, 22, 50], dtype=torch.uint8)

test_inputs = [query, key, value, mask]

# JIT_FAIL
'''
direct:
shape '[4, 1, 4, 20]' is invalid for input of size 4000

jit:
Failed running call_function <built-in method reshape of type object at 0x78b81eb96ec0>(*(FakeTensor(..., size=(4, 50, 20)), [4, 1, 4, 20]), **{}):
shape '[4, 1, 4, 20]' is invalid for input of size 4000

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''