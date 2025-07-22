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

    def forward(self, x1, x2):
        w1 = x1.permute(1, 2, 0)
        y1 = torch.bmm(x2, w1)
        w2 = x2.permute(1, 2, 0)
        y2 = torch.bmm(w2, x1)
        y3 = y1.permute(1, 2, 0)
        return torch.matmul(x2, y3)




func = Model().to('cuda')



x1 = torch.randn(3, 2, 2)



x2 = torch.randn(3, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 2] but got: [2, 2].

jit:
Failed running call_function <built-in method bmm of type object at 0x7f789fe699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 2, 2)), FakeTensor(..., device='cuda:0', size=(2, 2, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 2] but got: [2, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''