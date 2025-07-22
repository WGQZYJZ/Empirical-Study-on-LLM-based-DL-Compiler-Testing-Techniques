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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(3, 8, 7, 2, 2)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(8, 11, 3, 1, 1, bias=False)
        self.conv = torch.nn.Conv2d(11, 16, 3, 1, 1)
        self.linear_1 = torch.nn.Linear(12544, 512)
        self.linear_2 = torch.nn.Linear(512, 2)
        self.relu_1 = torch.nn.ReLU()
        self.relu_2 = torch.nn.ReLU()
        self.relu_3 = torch.nn.ReLU()
        self.relu_4 = torch.nn.ReLU()
        self.relu_5 = torch.nn.ReLU()
        self.relu_6 = torch.nn.ReLU()
        self.gelu_1 = torch.nn.GELU()
        self.gelu_2 = torch.nn.GELU()
        self.gelu_3 = torch.nn.GELU()
        self.gelu_4 = torch.nn.GELU()
        self.gelu_5 = torch.nn.GELU()
        self.sigmoid = torch.nn.Sigmoid()
        self.dropout_1 = torch.nn.Dropout(p=0.5)
        self.dropout_2 = torch.nn.Dropout(p=0.5)
        self.dropout_3 = torch.nn.Dropout(p=0.5)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv_transpose_2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv(v4)
        v6 = self.linear_1(v5.reshape((1, (- 1))))
        v7 = self.relu_1(v6)
        v8 = self.dropout_1(v7)
        v9 = self.linear_2(v8)
        v10 = self.sigmoid(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3225616 and 12544x512)

jit:
Failed running call_module L__self___linear_1(*(FakeTensor(..., device='cuda:0', size=(1, 3225616)),), **{}):
a and b must have same reduction dim, but got [1, 3225616] X [12544, 512].

from user code:
   File "<string>", line 46, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''