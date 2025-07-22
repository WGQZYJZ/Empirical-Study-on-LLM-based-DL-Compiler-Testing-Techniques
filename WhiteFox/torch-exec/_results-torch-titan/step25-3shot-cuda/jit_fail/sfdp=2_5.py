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
        self.matmul1 = torch.nn.Linear(12, 33)
        self.matmul2 = torch.nn.Linear(33, 44)

    def forward(self, x1, x2):
        v1 = self.matmul1(x1)
        v2 = self.matmul2(x2)
        v3 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v4 = v3.div(10)
        v5 = torch.nn.functional.softmax(v4, dim=(- 1))
        v6 = torch.nn.functional.dropout(v5, p=0.2)
        v7 = torch.matmul(v6, v2)
        return v7



func = Model().to('cuda')



x1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)



x2 = torch.randn(1, 8, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not Conv2d

jit:
linear(): argument 'input' (position 1) must be Tensor, not Conv2d
'''