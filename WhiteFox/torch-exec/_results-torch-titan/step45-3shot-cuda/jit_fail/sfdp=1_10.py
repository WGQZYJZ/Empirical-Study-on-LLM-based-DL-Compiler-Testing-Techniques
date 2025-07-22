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

    def __init__(self, dim, num_heads, ffn_dim, dropout):
        super().__init__()
        self.wq = torch.nn.Linear(dim, (num_heads * dim))
        self.wk = torch.nn.Linear(dim, (num_heads * dim))
        self.wv = torch.nn.Linear(dim, (num_heads * dim))
        self.wo = torch.nn.Linear(dim, (num_heads * dim))
        self.dropout = dropout

    def forward(self, query, key, value, mask):
        dim_key = key.size((- 1))
        v_qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        v_qk = v_qk.div((dim_key ** 0.5))
        v_dropout = torch.nn.functional.dropout(v_softmax, p=self.dropout)
        v_output = self.wo(v_dropout)
        return v_output



dim = 1
num_heads = 1
ffn_dim = 1
dropout = 1
func = Model(dim, num_heads, ffn_dim, dropout).to('cuda')




mask = torch.empty(1, 1, 1024, dtype=torch.float32).bernoulli_(0.5)

query = 1
key = 1
value = 1

test_inputs = [mask, query, key, value]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
'int' object has no attribute 'size'

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''