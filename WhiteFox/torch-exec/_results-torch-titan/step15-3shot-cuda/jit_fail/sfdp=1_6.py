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



class Attention(torch.nn.Module):

    def __init__(self, hidden_size, dropout_p=0.2):
        super().__init__()
        self.w_q = torch.nn.Linear(hidden_size, hidden_size)
        self.w_k = torch.nn.Linear(hidden_size, hidden_size)
        self.w_v = torch.nn.Linear(hidden_size, hidden_size)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, q, k, v, mask):
        q_ = self.w_q(q)
        k_ = self.w_k(k)
        v_ = self.w_v(v)
        output = self.dropout((torch.matmul(q_, k_.transpose(0, 1)) / math.sqrt(k_.size((- 1)))))
        if (mask is not None):
            output.masked_fill_((mask.unsqueeze(1) == 0), (- 1000000000.0))
        return output



hidden_size = 1

func = Attention(hidden_size).to('cuda')



q = torch.randn(16, 32, 16)



k = torch.randn(16, 32, 16)



v = torch.randn(16, 32, 16)


q = torch.randn(16, 32, 16)





q = torch.randn(16, 32, 16)


q = torch.randn(16, 32, 16)


q = torch.randn(16, 32, 16)



mask = torch.where((torch.arange(q.size(1)).to(q.device) < 16), torch.tensor([1]).to(q.device), torch.tensor([0]).to(q.device))


test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x16 and 1x1)

jit:
Failed running call_module L__self___w_q(*(FakeTensor(..., device='cuda:0', size=(16, 32, 16)),), **{}):
a and b must have same reduction dim, but got [512, 16] X [1, 1].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''