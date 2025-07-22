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
        self.linear = torch.nn.Linear(2, 2)
        self.linear1 = torch.nn.Linear(2, 2)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.softmax = torch.nn.Softmax(dim=2)
        self.tanh = torch.nn.Tanh()
        self.sigmoid1 = torch.nn.Sigmoid()
        self.linear2 = torch.nn.Linear(2, 2)
        self.linear2a = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        v3 = torch.ops.aten.dropout(v3, p=0.1, train=False, inplace=False)
        v3 = self.relu(v3)
        v3 = self.softmax(v3)
        v3 = self.tanh(v3)
        w = v3.permute(0, 2, 1)
        return w



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
aten::dropout() expected at most 3 argument(s) but received 4 argument(s). Declaration: aten::dropout(Tensor input, float p, bool train) -> Tensor

jit:
Failed running call_function aten.dropout(*(FakeTensor(..., size=(1, 2, 2)),), **{'p': 0.1, 'train': False, 'inplace': False}):
aten::dropout() expected at most 3 argument(s) but received 4 argument(s). Declaration: aten::dropout(Tensor input, float p, bool train) -> Tensor

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''