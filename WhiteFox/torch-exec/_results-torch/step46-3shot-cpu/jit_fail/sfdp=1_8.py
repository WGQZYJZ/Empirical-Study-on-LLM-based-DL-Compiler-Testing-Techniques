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

    def __init__(self, hidden_size=4):
        super().__init__()
        self.hidden_size = hidden_size

    def forward(self, q, k, v, mask=None, bias=None):
        scores = torch.matmul(q, k.transpose(-2, -1))
        scores /= np.sqrt(self.hidden_size)
        if bias is not None:
            scores += bias
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1000000000.0)
        p_attn = F.softmax(scores, dim=-1)
        if self.training:
            p_attn = dropout(p_attn, self.dropout_p)
        output = torch.matmul(p_attn, v)
        return (output, p_attn)


func = Model(embed_dim).to('cpu')


embed_dim = 32
q = torch.randn(6, 10, embed_dim)

embed_dim = 32
k = torch.randn(11, 10, embed_dim)

embed_dim = 32
v = torch.randn(11, 10, embed_dim)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (11) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x75fcae796ec0>(*(FakeTensor(..., size=(6, 10, 32)), FakeTensor(..., size=(11, 32, 10))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''