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
        self.linear = torch.nn.Linear(256, 1000)
        self.convt1 = torch.nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=(26, 26), stride=(2, 2), padding=(0,), dilation=(1,))
        self.leakyrecti = torch.nn.LeakyReLU()
        self.layernorm = torch.nn.LayerNorm(normalized_shape=[1000, 1, 1])
        self.linear2 = torch.nn.Linear(1000, 11968)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2.unsqueeze(0)
        v4 = self.convt1(v3)
        v5 = self.leakyrecti(v4)
        v6 = v5.squeeze(0)
        v7 = self.layernorm(v6)
        v8 = self.linear2(v7)
        y = torch.sigmoid(v8)
        return y




func = Model().to('cuda')



x1 = torch.randn(1, 256, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given normalized_shape=[1000, 1, 1], expected input with shape [*, 1000, 1, 1], but got input of size[1, 26, 2024]

jit:
Failed running call_module L__self___layernorm(*(FakeTensor(..., device='cuda:0', size=(1, 26, 2024)),), **{}):
Given normalized_shape=[1000, 1, 1], expected input with shape [1000, 1, 1], but got input of size torch.Size([1, 26, 2024])

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''