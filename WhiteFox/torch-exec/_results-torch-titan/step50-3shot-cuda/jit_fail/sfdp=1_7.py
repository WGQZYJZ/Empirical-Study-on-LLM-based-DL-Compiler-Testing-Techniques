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
        self.dot = torch.nn.Linear(100, 100)
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x1, x2):
        v1 = self.dot(x1)
        v2 = torch.matmul(x2, v1.transpose((- 2), (- 1)))
        v3 = (v2 / 1000)
        v4 = torch.nn.functional.softmax(v3, (- 1))
        v5 = self.dropout(v4)
        v6 = torch.matmul(v5, x2)
        return v6



func = Model().to('cuda')



x1 = torch.randn(128, 100)



x2 = torch.randn(128, 100, 100)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [128, 128] but got: [128, 100].

jit:
Failed running call_function <built-in method matmul of type object at 0x7492628699e0>(*(FakeTensor(..., device='cuda:0', size=(128, 100, 128)), FakeTensor(..., device='cuda:0', size=(128, 100, 100))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [128, 128] but got: [128, 100].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''