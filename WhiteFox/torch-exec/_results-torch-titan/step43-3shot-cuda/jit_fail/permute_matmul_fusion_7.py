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

        def _init_weights(m):
            if (type(m) == torch.nn.Linear):
                torch.nn.init.xavier_uniform(m.weight)
                m.bias.data.fill_(0.01)
        self.conv3x3 = torch.nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = torch.nn.Linear(in_features=1344, out_features=75, bias=True)
        self.fc2 = torch.nn.Linear(in_features=75, out_features=11, bias=True)
        self.apply(_init_weights)

    def forward(self, x):
        x = self.conv3x3(x)
        x = self.pool(x)
        x = x.view(x.size(0), (- 1))
        x = self.fc1(x)
        x = torch.nn.functional.relu(x)
        x = torch.nn.functional.dropout(x, training=True)
        x = self.fc2(x)
        x = torch.nn.functional.relu(x)
        x = torch.nn.functional.dropout(x, training=True)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 3, 40, 30)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1596 and 1344x75)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(1, 1596)),), **{}):
a and b must have same reduction dim, but got [1, 1596] X [1344, 75].

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''