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
        self.fc = torch.nn.Linear(3, 8)

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


func = Model().to('cpu')


query = torch.randn(1, 3, 128)

key = torch.randn(1, 3, 512)

value = torch.randn(1, 3, 512)

attn_mask = torch.randn(1, 1, 1, 512)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 512].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, 3, 128)), FakeTensor(..., size=(1, 512, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 512].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''