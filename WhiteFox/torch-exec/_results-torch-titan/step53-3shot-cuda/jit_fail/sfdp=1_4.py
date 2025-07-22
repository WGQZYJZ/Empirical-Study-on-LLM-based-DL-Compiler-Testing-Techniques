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

    def __init__(self, hidden_size, num_heads=8, dropout=0.0):
        super().__init__()
        self.query_projection = torch.nn.Linear(hidden_size, hidden_size)
        self.key_projection = torch.nn.Linear(hidden_size, hidden_size)
        self.value_projection = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, query, key, value, mask=None):
        q = self.query_projection(query)
        k = self.key_projection(key)
        v = self.value_projection(value)
        a = torch.matmul(q, k.transpose((- 2), (- 1)))
        if (mask is not None):
            mask = mask[:, None, None, :]
            a = a.masked_fill((mask == 0), (- np.inf))
        inv_scale_factor = np.sqrt(k.shape[(- 1)])
        scaled_a = (a / inv_scale_factor)
        scaled_a = F.softmax(scaled_a, dim=(- 1))
        a = scaled_a
        if dropout:
            a = F.dropout(scaled_a, p=dropout)
        output = torch.matmul(a, v)
        return output



hidden_size = 1
func = Model(1024, num_heads=8).to('cuda')



query = torch.randn(1, 128, 1024)



key = torch.randn(1, 128, 16, 1024)



value = torch.randn(1, 128, 16, 1024)




mask = torch.zeros(1, 128, 16).to(torch.bool)


test_inputs = [query, key, value, mask]

# JIT_FAIL
'''
direct:
name 'dropout' is not defined

jit:
name 'dropout' is not defined

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''