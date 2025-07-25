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

class QueryKeyAttentionModel(torch.nn.Module):

    def __init__(self, num_heads, scaling_factor=1.0 / math.sqrt(77), dropout_p=0.2):
        super().__init__()
        self.scaling_factor = scaling_factor
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.project_query = torch.nn.Linear(77, 22, bias=False)
        self.project_key = torch.nn.Linear(77, 22, bias=False)
        self.project_value = torch.nn.Linear(77, 22)

    def forward(self, query, key):
        q2 = self.project_query(query)
        k2 = self.project_key(key)
        v2 = self.project_value(key)
        q3 = q2.view(q2.size(0), q2.size(1), self.num_heads, 22 // self.num_heads)
        q4 = q3.permute(0, 2, 1, 3)
        k3 = k2.view(k2.size(0), k2.size(1), self.num_heads, 22 // self.num_heads)
        k4 = k3.permute(0, 2, 1, 3)
        qk = torch.matmul(q4, k4.transpose(-2, -1))
        scaled_qk = qk * self.scaling_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, v2)
        return output


num_heads = 1

func = QueryKeyAttentionModel(num_heads).to('cpu')


x1 = torch.randn(1, 120, 22)

x2 = torch.randn(1, 200, 22)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (120x22 and 77x22)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 120, 22)), Parameter(FakeTensor(..., size=(22, 77), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [120, 22] X [77, 22].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''