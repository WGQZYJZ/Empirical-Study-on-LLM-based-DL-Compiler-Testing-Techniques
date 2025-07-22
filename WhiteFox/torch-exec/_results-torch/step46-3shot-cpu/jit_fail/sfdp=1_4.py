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

    def __init__(self, query_value_dimension):
        super().__init__()
        self.qkv = torch.nn.Linear(query_value_dimension, 3 * query_value_dimension, bias=False)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        s = self.qkv(query).shape
        scale_factor = torch.sqrt(torch.tensor(s[-1], dtype=torch.float))
        inv_scale_factor = 1.0 / scale_factor
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(value)
        return output


query_value_dimension = 1

func = Model(query_value_dimension).to('cpu')


query = torch.tensor([[-0.7358642204284668, -0.9455091905593872]])

key = torch.tensor([[-0.8529059023857117, 0.3162973244142532]])

value = torch.tensor([[0.400022784280777, 0.4586286592578888]])

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 1x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2)), Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [1, 2] X [1, 3].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''