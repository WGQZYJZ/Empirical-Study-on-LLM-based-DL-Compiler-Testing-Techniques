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

    def __init__(self, x1):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.8)
        self.fc = torch.nn.Linear(in_features=x1.size(1), out_features=8, bias=True)

    def forward(self, x1):
        v1 = self.dropout(x1)
        v2 = torch.relu(v1)
        return torch.relu(self.fc(v2))


x1 = torch.randn(1, 512, 100, 100)

func = Model(x1).to('cuda')


x1 = torch.randn(1, 512, 100, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (51200x100 and 512x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 512, 100, 100)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 512), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [51200, 100] X [512, 8].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''