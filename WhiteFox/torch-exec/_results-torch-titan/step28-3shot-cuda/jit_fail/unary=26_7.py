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

    def __init__(self, w_in):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(w_in, 3, (3, 7), stride=2, padding=4)

    def forward(self, x):
        x1 = self.conv_t(x)
        return x1




w_in = random.randint(20, 60)


func = Model(w_in).to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___conv_t(*(1,), **{}):
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''