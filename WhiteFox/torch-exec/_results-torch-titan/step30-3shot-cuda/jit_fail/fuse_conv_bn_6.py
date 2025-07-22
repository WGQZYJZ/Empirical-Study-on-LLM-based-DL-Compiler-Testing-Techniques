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
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.relu = torch.nn.ReLU()
        self.conv = torch.nn.Conv1d(2, 2, 2)
        self.fc = torch.nn.Linear(2, 2)
        self.bn = torch.nn.BatchNorm1d(2)

    def forward(self, input_1, input_2):
        x = self.conv(input_1)
        x = self.fc(x)
        x = self.bn(x)
        x = self.softmax(x)
        x = self.relu(x)
        x = (x + input_2)
        return x




func = Model().to('cuda')



input_1 = torch.randn(1, 2, 8)



input_2 = torch.randn(1, 2, 8)


test_inputs = [input_1, input_2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x7 and 2x2)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 2, 7)),), **{}):
a and b must have same reduction dim, but got [2, 7] X [2, 2].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''