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

    def __init__(self, num_heads=2, dropout=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.dropout = dropout
        self.scale_factor = (1 / (dropout * num_heads))

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = v1.div(self.scale_factor)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=self.dropout)
        output = v4.matmul(x3)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 2, 5)



x2 = torch.randn(1, 2, 4)



x3 = torch.randn(1, 4, 6)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x709d082699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 5)), FakeTensor(..., device='cuda:0', size=(1, 4, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''