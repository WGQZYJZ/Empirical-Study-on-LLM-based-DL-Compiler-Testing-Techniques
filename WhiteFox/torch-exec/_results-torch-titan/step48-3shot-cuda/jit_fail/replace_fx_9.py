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
        self.l = torch.nn.LayerNorm(2, elementwise_affine=True)

    def forward(self, x):
        return self.l(x)




func = Model().to('cuda')



x = torch.ones(1, 2, 10, 20)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given normalized_shape=[2], expected input with shape [*, 2], but got input of size[1, 2, 10, 20]

jit:
Failed running call_module L__self___l(*(FakeTensor(..., device='cuda:0', size=(1, 2, 10, 20)),), **{}):
Given normalized_shape=[2], expected input with shape [2], but got input of size torch.Size([1, 2, 10, 20])

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''