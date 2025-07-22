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

    def __init__(self, hidden_size, num_attention_heads, attention_probs_dropout_prob, layer_norm_eps):
        super().__init__()
        self.q = torch.nn.Linear(hidden_size, hidden_size)
        self.k = torch.nn.Linear(hidden_size, hidden_size)
        self.v = torch.nn.Linear(hidden_size, hidden_size)
        self.proj = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, q, k, v, mask):
        q = self.q(q)
        k = self.k(k)
        v = self.v(v)
        q = (q / math.sqrt(k.size((- 1))))
        q = (q * mask)
        k = (k + q.masked_fill((~ mask), float((- 10000.0))).unsqueeze((- 1)))
        context_weight = torch.nn.Softmax(dim=(- 1))(k)
        context_weight = torch.nn.Dropout(self.dropout_prob)(context_weight)
        out = (context_weight @ v)
        return self.layer_norm((out + residual))



hidden_size = 1
num_attention_heads = 1
attention_probs_dropout_prob = 1
layer_norm_eps = 1

func = Model(hidden_size, num_attention_heads, attention_probs_dropout_prob, layer_norm_eps).to('cuda')

q = 1
k = 1
v = 1
mask = 1

test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___q(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''