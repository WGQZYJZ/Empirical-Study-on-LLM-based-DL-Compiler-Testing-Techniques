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

    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=-1)
        self.relu = torch.nn.ReLU()
        self.conv = torch.nn.Conv1d(2, 2, 2)
        self.fc = torch.nn.Linear(2, 2)
        self.bn = torch.nn.BatchNorm1d(2)

    def forward(self, input_1, input_2):
        x = self.conv(input_1)
        x = self.fc(x)
        x = self.bn(x)
        x = self.softmax(x)
        x = self.relu(x)
        x = x + input_2
        return x



func = Model().to('cpu')


input_1 = torch.randn(1, 2, 8)

input_2 = torch.randn(1, 2, 8)

test_inputs = [input_1, input_2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x7 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 7)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 7] X [2, 2].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''