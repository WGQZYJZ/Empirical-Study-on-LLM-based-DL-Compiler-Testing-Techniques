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
        torch.manual_seed(1)
        self.conv = torch.nn.Conv2d(3, 3, 3)
        torch.manual_seed(1)
        self.layernorm = torch.nn.LayerNorm(3)

    def forward(self, x2):
        x = self.conv(x2)
        y = self.layernorm(x)
        return y




func = Model().to('cuda')



x2 = torch.randn(1, 3, 6, 6)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given normalized_shape=[3], expected input with shape [*, 3], but got input of size[1, 3, 4, 4]

jit:
Failed running call_module L__self___layernorm(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4)),), **{}):
Given normalized_shape=[3], expected input with shape [3], but got input of size torch.Size([1, 3, 4, 4])

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''