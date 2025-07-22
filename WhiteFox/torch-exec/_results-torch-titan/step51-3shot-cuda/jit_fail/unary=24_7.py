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

    def forward(self, x):
        t = x.shape[3]
        negative_slope = 1.37857933
        v1 = torch.nn.functional.conv2d(x, torch.zeros((32, 1, 1, 1)), bias=torch.ones(32), stride=(1, 4), padding=(0, 0))
        v2 = torch.reshape((1 - (v1 / 6)), ((- 1), 32, t))
        v3 = (1 + ((v1 - 6) / 0.02))
        v4 = (0.48681433 + ((v1 - 2.73333325) * 1.75934))
        v5 = (3.9999952 + ((t - 6) / 11.424742))
        v6 = (v2 - 0.76293294)
        v7 = (((v6 / v3) * v4) + 0.7999996)
        v8 = (1 - torch.abs(v1))
        v9 = (v5 * torch.round((1 + v7)))
        v10 = (0.486815 + ((v8 - 6) / v9))
        v11 = ((torch.round(((1 - v10) / torch.max(v10, v1))) * 1) - v10)
        v12 = ((1 + torch.nn.functional.softplus(v11)) + (((- v11) * v10) + torch.log(float((- 1)))))
        v13 = (v1 * v12)
        v14 = torch.where((v13 > 0), v13, (v13 * negative_slope))
        return v14




func = Model().to('cuda')



x1 = torch.randn(34, 32, 75, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 1, 1, 1], expected input[34, 32, 75, 32] to have 1 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c30854699e0>(*(FakeTensor(..., device='cuda:0', size=(34, 32, 75, 32)), FakeTensor(..., size=(32, 1, 1, 1))), **{'bias': FakeTensor(..., size=(32,)), 'stride': (1, 4), 'padding': (0, 0)}):
Given groups=1, weight of size [32, 1, 1, 1], expected input[34, 32, 75, 32] to have 1 channels, but got 32 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''