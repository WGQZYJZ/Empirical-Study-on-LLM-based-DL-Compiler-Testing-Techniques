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

    def __init__(self, num_heads=1):
        super().__init__()
        self.num_heads = num_heads

    def forward(self, x1, x2, x3):
        y1 = x1.matmul(x2.transpose((- 2), (- 1)))
        y2 = (y1 / self.num_heads)
        y3 = y2.softmax(dim=(- 1))
        y4 = torch.nn.functional.dropout(y3)
        out = y4.matmul(x3)
        return out



func = Model(num_heads=12).to('cuda')



x1 = torch.randn(1, 12, 1024)



x2 = torch.randn(1, 12, 2048)



x3 = torch.randn(1, 2048)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [1, 2048].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 12, 1024)), FakeTensor(..., device='cuda:0', size=(1, 2048, 12))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [1, 2048].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''