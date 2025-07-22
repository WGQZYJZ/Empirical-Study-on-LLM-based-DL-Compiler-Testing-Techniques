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

    def __init__(self, dim_model, num_heads, dropout_p):
        super().__init__()
        head_dim = (dim_model // num_heads)
        self.linear_query = torch.nn.Linear(dim_model, dim_model)
        self.linear_key = torch.nn.Linear(dim_model, dim_model)
        self.linear_value = torch.nn.Linear(dim_model, dim_model)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, q, k, v, mask, inv_scale_factor):
        q = self.linear_query(q).view(q.size(0), q.size(1), q.size(2), num_heads, head_dim).transpose(2, 3)
        k = self.linear_key(k).view(k.size(0), k.size(1), k.size(2), num_heads, head_dim).transpose(2, 3)
        v = self.linear_value(v).view(v.size(0), v.size(1), v.size(2), num_heads, head_dim).transpose(2, 3)
        q = q.div(math.sqrt(head_dim))
        scaled_qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = scaled_qk.div(inv_scale_factor)
        softmax_q = self.softmax(scaled_qk.float())
        softmax_q = softmax_q.to(dtype=q.dtype)
        dropout_q = self.dropout(softmax_q)
        output = torch.matmul(dropout_q, v)
        output = output.view(output.size(0), output.size(1), output.size(2), (- 1)).transpose(2, 3)
        output = output.contiguous().view(output.size(0), output.size(1), (- 1))
        return output



dim_model = 1
num_heads = 1
dropout_p = 1

func = Model(dim_model, num_heads, dropout_p).to('cuda')



q = torch.randn(2, 20, 1, 1, 256)



k = torch.randn(2, 20, 1, 1, 256)



v = torch.randn(2, 20, 1, 1, 256)


k = torch.randn(2, 20, 1, 1, 256)


q = torch.randn(2, 20, 1, 1, 256)


q = torch.randn(2, 20, 1, 1, 256)




q = torch.randn(2, 20, 1, 1, 256)


mask = torch.ones(q.size(0), q.size(1), k.size(1)).to(dtype=torch.bool).to(q.device)



q = torch.randn(2, 20, 1, 1, 256)


inv_scale_factor = torch.ones((1, 1, 1, 1)).to(q.device)


test_inputs = [q, k, v, mask, inv_scale_factor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (40x256 and 1x1)

jit:
Failed running call_module L__self___linear_query(*(FakeTensor(..., device='cuda:0', size=(2, 20, 1, 1, 256)),), **{}):
a and b must have same reduction dim, but got [40, 256] X [1, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''