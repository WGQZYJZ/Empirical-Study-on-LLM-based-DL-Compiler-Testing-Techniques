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

    def __init__(self, batch_size, dim_q, dim_k, dim_v, num_heads, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p
        self.q = torch.nn.Linear(dim_q, dim_q)
        self.k = torch.nn.Linear(dim_k, dim_k)
        self.v = torch.nn.Linear(dim_v, dim_v)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, x1):
        x2 = torch.nn.functional.relu(self.q(x1))
        x3 = torch.nn.functional.relu(self.k(x1))
        x4 = torch.nn.functional.relu(self.v(x1))
        qk = torch.matmul(x2, x3.transpose((- 2), (- 1)))
        scaled_qk = qk.div(np.sqrt(self.dim_k))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x4)
        return output



batch_size = 1
dim_q = 1
dim_k = 1
dim_v = 1
num_heads = 1
dropout_p = 1

func = Model(batch_size, dim_q, dim_k, dim_v, num_heads, dropout_p).to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___q(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''