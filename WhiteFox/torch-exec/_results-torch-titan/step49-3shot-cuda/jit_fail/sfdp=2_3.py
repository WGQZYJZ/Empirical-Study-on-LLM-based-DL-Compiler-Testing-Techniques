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
        self.fc1 = torch.nn.Linear(4, 1)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        v1 = self.fc1(qk)
        v2 = v1.div(10)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.2)
        output = v4.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(8, 3, 4, 4)



key = torch.randn(8, 3, 5, 5)



value = torch.randn(8, 3, 7, 7)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [24, 4] but got: [24, 5].

jit:
Failed running call_function <built-in method matmul of type object at 0x7ccbffe699e0>(*(FakeTensor(..., device='cuda:0', size=(8, 3, 4, 4)), FakeTensor(..., device='cuda:0', size=(8, 3, 5, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [24, 4] but got: [24, 5].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''