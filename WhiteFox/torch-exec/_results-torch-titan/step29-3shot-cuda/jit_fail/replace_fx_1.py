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




func = Model().to('cuda')



x1 = torch.randn(1, 22)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given normalized_shape=[22], expected input with shape [*, 22], but got input of size[1, 2]

jit:
Failed running call_module L__self___layer_norm1(*(FakeTensor(..., device='cuda:0', size=(1, 2)),), **{}):
Given normalized_shape=[22], expected input with shape [22], but got input of size torch.Size([1, 2])

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''