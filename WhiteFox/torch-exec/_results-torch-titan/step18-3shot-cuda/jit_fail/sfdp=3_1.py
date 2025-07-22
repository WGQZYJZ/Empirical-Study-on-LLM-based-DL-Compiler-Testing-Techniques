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
        self.query = torch.nn.Parameter(torch.rand(16, 32, 9, 9))
        self.key = torch.nn.Parameter(torch.rand(16, 32, 11, 11))
        self.value = torch.nn.Parameter(torch.rand(16, 32, 11, 11))

    def forward(self, x1):
        return scaled_dot_product_attention(self.query, self.key, self.value)



func = Model().to('cuda')



x1 = torch.randn(8, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'scaled_dot_product_attention' is not defined

jit:
name 'scaled_dot_product_attention' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''