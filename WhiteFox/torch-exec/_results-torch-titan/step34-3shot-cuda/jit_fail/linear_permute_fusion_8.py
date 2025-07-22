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
        self.conv = torch.nn.Conv2d(3, 3, 2, bias=False).requires_grad_(False)

    def forward(self, x1, x2):
        x2 = self.conv(x2)
        return torch.nn.functional.max_pool2d((x1 + x2), 3)




func = Model().to('cuda')



x1 = torch.randn(4, 3, 8, 8, requires_grad=True)



x2 = torch.randn(4, 3, 10, 10)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (9) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(4, 3, 8, 8)), FakeTensor(..., device='cuda:0', size=(4, 3, 9, 9))), **{}):
Attempting to broadcast a dimension of length 9 at -1! Mismatching argument at index 1 had torch.Size([4, 3, 9, 9]); but expected shape should be broadcastable to [4, 3, 8, 8]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''