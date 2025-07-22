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



class SelfAttention(torch.nn.Module):

    def __init__(self, embed_dim, num_heads, dropout_p, attention_type='dot'):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.attention_type = attention_type
        self.fc1 = torch.nn.Linear(embed_dim, embed_dim)
        self.fc2 = torch.nn.Linear(embed_dim, embed_dim)
        self.attn_dropout = torch.nn.Dropout(dropout_p)
        if (attention_type == 'general'):
            self.attn = torch.nn.Linear(embed_dim, embed_dim)
        else:
            self.attn = None

    def forward(self, x):
        query = self.fc1(x)
        value = self.fc2(x)
        attn1 = torch.matmul(query, value.transpose((- 2), (- 1)))
        if (self.attention_type == 'general'):
            attn2 = self.attn(x)
            attn = (attn1 + attn2)
        else:
            attn = attn1
        attn = self.attn_dropout(attn.softmax(dim=(- 1)))
        return torch.matmul(attn, value)



embed_dim = 1
num_heads = 1
dropout_p = 1

func = SelfAttention(embed_dim, num_heads, dropout_p).to('cuda')



x = torch.randn(100, 16, 1024)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1600x1024 and 1x1)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(100, 16, 1024)),), **{}):
a and b must have same reduction dim, but got [1600, 1024] X [1, 1].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''