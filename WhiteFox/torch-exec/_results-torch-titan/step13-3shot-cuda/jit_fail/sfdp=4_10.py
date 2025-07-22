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

    def forward(self, x1, x2, x3):
        v1 = (x1 @ x2.transpose((- 1), (- 2)))
        v2 = (v1 / math.sqrt(x1.size((- 1))))
        v3 = (v2 + x3)
        v4 = F.softmax(v3, dim=(- 1))
        v5 = (v4 @ x3)
        return v5



func = Model().to('cuda')



__input1__ = torch.randn(1, 2, 3)



__input2__ = torch.randn(1, 3, 2)



__input3__ = torch.randn(1, 3, 4)


test_inputs = [__input1__, __input2__, __input3__]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 2].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3)), FakeTensor(..., device='cuda:0', size=(1, 2, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''