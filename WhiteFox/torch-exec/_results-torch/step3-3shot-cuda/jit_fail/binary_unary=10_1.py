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
        self.fc1 = torch.nn.Linear(64, 16)
        self.fc2 = torch.nn.Linear(128, 64)

    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = torch.cat((v1, x1), dim=1)
        v3 = self.fc2(v2)
        v4 = torch.sigmoid(v3)
        return v4


func = Model().to('cuda')


x1 = torch.randn(20, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x80 and 128x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(20, 80)), Parameter(FakeTensor(..., device='cuda:0', size=(64, 128), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [20, 80] X [128, 64].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''