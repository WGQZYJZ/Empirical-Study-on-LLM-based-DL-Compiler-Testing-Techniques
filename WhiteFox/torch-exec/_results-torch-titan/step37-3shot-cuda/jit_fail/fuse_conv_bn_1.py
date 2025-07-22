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
        self.features = torch.nn.Sequential(torch.nn.Conv1d(1, 32, kernel_size=3, stride=2, padding=1, bias=False), torch.nn.BatchNorm1d(32, momentum=0.1), torch.nn.ReLU(inplace=True), torch.nn.Conv1d(32, 32, kernel_size=3, stride=2, padding=1, bias=False), torch.nn.BatchNorm1d(32, momentum=0.1), torch.nn.ReLU(inplace=True), torch.nn.Conv1d(32, 32, kernel_size=3, stride=2, padding=1, bias=False), torch.nn.BatchNorm1d(32, momentum=0.1), torch.nn.ReLU(inplace=True), torch.nn.Conv1d(32, 32, kernel_size=3, stride=2, padding=1, bias=False), torch.nn.BatchNorm1d(32, momentum=0.1), torch.nn.ReLU(inplace=True), torch.nn.Linear(32, 8))

    def forward(self, x):
        return self.features(x)




func = Model().to('cuda')



x = torch.randn(1, 1, 30)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x2 and 32x8)

jit:
Failed running call_module L__self___features_12(*(FakeTensor(..., device='cuda:0', size=(1, 32, 2)),), **{}):
a and b must have same reduction dim, but got [32, 2] X [32, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''