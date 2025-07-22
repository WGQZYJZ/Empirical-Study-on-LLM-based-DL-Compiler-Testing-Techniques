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
        self.conv_t = torch.nn.ConvTranspose2d(1, 6, 5, stride=1, padding=0, bias=False)
        self.act = torch.nn.PReLU(6)

    def forward(self, x6):
        z5 = self.conv_t(x6)
        z6 = z5 > 0
        z7 = z5 * 0.995
        z8 = torch.where(z6, z5, z7)
        z9 = self.act(z8)
        return torch.nn.functional.log_softmax(torch.nn.functional.layer_norm(z9, [1, 1, 24, 35]))



func = Model().to('cpu')


x6 = torch.randn(3, 1, 65, 24)

test_inputs = [x6]

# JIT_FAIL
'''
direct:
Given normalized_shape=[1, 1, 24, 35], expected input with shape [*, 1, 1, 24, 35], but got input of size[3, 6, 69, 28]

jit:
Failed running call_function <function layer_norm at 0x7747c8f70040>(*(FakeTensor(..., size=(3, 6, 69, 28)), [1, 1, 24, 35]), **{}):
Given normalized_shape=[1, 1, 24, 35], expected input with shape [1, 1, 24, 35], but got input of size torch.Size([3, 6, 69, 28])

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''