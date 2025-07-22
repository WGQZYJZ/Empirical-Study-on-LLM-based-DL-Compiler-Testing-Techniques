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
        self.conv1 = torch.nn.Conv1d(768, 512, 24)
        self.layer = torch.nn.LayerNorm(512)
        self.drop = torch.nn.Dropout(0.1)

    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = self.layer(x2)
        x4 = self.drop(x3)
        x5 = self.drop(x1)
        x6 = torch.rand_like(x5)
        return x6




func = Model().to('cuda')



x1 = torch.randn(8, 768, 512)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given normalized_shape=[512], expected input with shape [*, 512], but got input of size[8, 512, 489]

jit:
Failed running call_module L__self___layer(*(FakeTensor(..., device='cuda:0', size=(8, 512, 489)),), **{}):
Given normalized_shape=[512], expected input with shape [512], but got input of size torch.Size([8, 512, 489])

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''