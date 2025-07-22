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

    def __init__(self, num_heads, num_classes, d_input_dim, d_kv):
        super().__init__()
        self.num_heads = num_heads
        self.num_classes = num_classes
        self.d_kv = d_kv
        self.d_head = (d_kv // num_heads)
        self.attn_q = torch.nn.Linear(d_input_dim, d_input_dim)
        self.attn_k = torch.nn.Linear(d_input_dim, d_input_dim)
        self.attn_v = torch.nn.Linear(d_input_dim, d_input_dim)
        self.class_proj = torch.nn.Linear(d_input_dim, num_classes)

    def forward(self, query, key, value, dropout_rates):
        Q = self.attn_q(query)
        K = self.attn_k(key)
        V = self.attn_v(value)
        Q = Q.reshape(Q.shape[0], (- 1), self.num_heads, self.d_head).permute([0, 2, 1, 3])
        K = K.reshape(K.shape[0], (- 1), self.num_heads, self.d_head).permute([0, 2, 1, 3])
        V = V.reshape(V.shape[0], (- 1), self.num_heads, self.d_head).permute([0, 2, 1, 3])
        attn_logits = (torch.matmul(Q, K.transpose((- 2), (- 1))) / (self.d_head ** 0.5))
        inv_scale_factor = ((1.0 / Q.shape[(- 1)]) ** 0.5)
        dropout_probs = (1 - dropout_rates)
        attn_weights = F.dropout(F.softmax((attn_logits * inv_scale_factor), dim=(- 1)), p=dropout_probs, training=True)
        attn_output = torch.matmul(attn_weights, V)
        attn_output = attn_output.transpose(1, 2).reshape(shape=[(- 1), Q.shape[1], (self.num_heads * self.d_head)])
        logits = self.class_proj(attn_output)
        return logits



num_heads = 1
num_classes = 1
d_input_dim = 1
d_kv = 1

func = Model(num_heads, num_classes, d_input_dim, d_kv).to('cuda')



x_query = torch.randn(size=(1, 512, 1024))

query = 1
key = 1
value = 1

test_inputs = [x_query, query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x1024 and 1x1)

jit:
Failed running call_module L__self___attn_q(*(FakeTensor(..., device='cuda:0', size=(1, 512, 1024)),), **{}):
a and b must have same reduction dim, but got [512, 1024] X [1, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''