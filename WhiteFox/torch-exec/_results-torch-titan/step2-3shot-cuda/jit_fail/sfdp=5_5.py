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
        self.attn = torch.nn.MultiheadAttention(64, 4)

    def forward(self, x1, x2):
        (x3, x4) = self.attn(x1, x2, x2)
        return x3



func = Model().to('cuda')



x1 = torch.randn(1, 64, 4, 28)



x2 = torch.randn(1, 64, 28, 28)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

jit:
Failed running call_module L__self___attn(*(FakeTensor(..., device='cuda:0', size=(1, 64, 4, 28)), FakeTensor(..., device='cuda:0', size=(1, 64, 28, 28)), FakeTensor(..., device='cuda:0', size=(1, 64, 28, 28))), **{}):
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''