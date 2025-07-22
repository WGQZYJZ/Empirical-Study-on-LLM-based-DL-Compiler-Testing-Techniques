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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 16, 3, stride=1)
        self.maxpool = torch.nn.MaxPool2d(4)
        self.dropout = torch.nn.Dropout2d(p=0.2)
        self.relu = torch.nn.ReLU6()
        self.layernorm = torch.nn.LayerNorm([32, 16])
        self.gelu = torch.nn.GELU()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.maxpool(v1)
        v3 = self.dropout(v2)
        v4 = self.relu(v3)
        v5 = self.layernorm(v4)
        v6 = self.gelu(v5)
        return torch.tanh(v6)



func = ModelTanh().to('cpu')


x = torch.randn(1, 4, 48, 48)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given normalized_shape=[32, 16], expected input with shape [*, 32, 16], but got input of size[1, 16, 11, 11]

jit:
Failed running call_function <function layer_norm at 0x7bc9e1cf0040>(*(FakeTensor(..., size=(1, 16, 11, 11)), (32, 16), Parameter(FakeTensor(..., size=(32, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(32, 16), requires_grad=True)), 1e-05), **{}):
Given normalized_shape=[32, 16], expected input with shape [32, 16], but got input of size torch.Size([1, 16, 11, 11])

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/normalization.py", line 217, in forward
    return F.layer_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''