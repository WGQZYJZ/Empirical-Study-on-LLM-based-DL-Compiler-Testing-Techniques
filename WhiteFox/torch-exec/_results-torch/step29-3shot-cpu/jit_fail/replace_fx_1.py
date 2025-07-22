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
        self.linear1 = torch.nn.Linear(22, 2)
        self.relu1 = torch.nn.ReLU()
        self.layer_norm1 = torch.nn.LayerNorm([22])
        self.dense1 = torch.nn.Linear(2, 3)
        self.dropout1 = torch.nn.Dropout(0.3)
        self.tanh1 = torch.nn.Tanh()

    def forward(self, a1):
        q2 = self.linear1(a1)
        q4 = self.relu1(q2)
        q5 = self.layer_norm1(q2)
        q3 = self.dense1(q4)
        q1 = self.dropout1(q2)
        q1 = self.tanh1(q2)
        return q1



func = Model().to('cpu')


x1 = torch.randn(1, 22)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given normalized_shape=[22], expected input with shape [*, 22], but got input of size[1, 2]

jit:
Failed running call_function <function layer_norm at 0x7a87538f1040>(*(FakeTensor(..., size=(1, 2)), (22,), Parameter(FakeTensor(..., size=(22,), requires_grad=True)), Parameter(FakeTensor(..., size=(22,), requires_grad=True)), 1e-05), **{}):
Given normalized_shape=[22], expected input with shape [22], but got input of size torch.Size([1, 2])

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/normalization.py", line 217, in forward
    return F.layer_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''