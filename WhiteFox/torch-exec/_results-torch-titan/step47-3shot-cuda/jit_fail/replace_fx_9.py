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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()
        self.lstm = torch.nn.LSTM(220, 512, 2, bidirectional=True)
        self.linear = torch.nn.Linear((512 * 2), 4)

    def forward(self, x1, x2):
        a = (x1 + x2)
        b = torch.abs(a)
        c = self.relu(b)
        (d, e) = self.lstm(c)
        f = self.linear(d)
        return torch.nn.functional.dropout(f, p=0.75)




func = model().to('cuda')



x1 = torch.randn(1, 2, 220)



x2 = torch.randn(1, 4, 220)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 220)), FakeTensor(..., device='cuda:0', size=(1, 4, 220))), **{}):
Attempting to broadcast a dimension of length 4 at -2! Mismatching argument at index 1 had torch.Size([1, 4, 220]); but expected shape should be broadcastable to [1, 2, 220]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''