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

    def __init__(self, hidden_size):
        super().__init__()
        n_head = 4
        self.h = 8
        self.d = hidden_size
        self.query = torch.nn.Linear(hidden_size, hidden_size)
        self.key = torch.nn.Linear(hidden_size, hidden_size)
        self.value = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, q, k, v):
        attn_mask = torch.zeros(k.size()[0], 1, k.size()[1], k.size()[1], dtype=torch.float32)
        qk = self.query(q)
        qk = (qk @ k.transpose((- 2), (- 1)))
        qk = (qk / np.sqrt(self.d))
        attn_mask = torch.zeros(k.size()[0], 4, k.size()[1], k.size()[1], dtype=torch.float32)
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk)
        output = (value @ attn_weight)




hidden_size = 512

func = Model(hidden_size).to('cuda')

q = 1
k = 1
v = 1

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
'int' object has no attribute 'size'

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''