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
        self.flatten3 = torch.nn.Flatten(0, 1)
        self.flatten2 = torch.nn.Flatten(0, 2)
        self.linear1 = torch.nn.Linear(2, 1)
        self.linear2 = torch.nn.Linear(2, 2)
        self.linear3 = torch.nn.Linear(2, 2)
        self.linear4 = torch.nn.Linear(2, 2)
        self.linear5 = torch.nn.Linear(2, 2)
        self.linear6 = torch.nn.Linear(2, 2)

    def forward(self, x):
        v1 = torch.nn.functional.leaky_relu(x, 0.20000000298023224, False)
        v2 = torch.nn.functional.hardsigmoid(v1)
        v3 = torch.nn.functional.hardtanh(v2)
        v4 = torch.nn.functional.hardtanh(v3)
        v5 = torch.nn.functional.leaky_relu(v4, 0.20000000298023224, False)
        v6 = torch.nn.functional.hardtanh(v5)
        v7 = torch.nn.functional.hardsigmoid(v6)
        x1 = torch.nn.functional.hardsigmoid(v7)
        x2 = torch.nn.functional.leaky_relu(x1, 0.09999999403953552, False)
        v8 = torch.nn.functional.hardsigmoid(x2)
        x3 = torch.nn.functional.hardtanh(v8)
        v9 = x3.permute(0, 2, 1)
        v9 = (v9 + self.flatten3.bias.view(1, 2, 2))
        v9 = (x3 + v9)
        v10 = self.reshape5(self.flatten3(self.flatten2(v9)))
        v10 = v10.permute(0, 2, 1)
        v11 = (v9 - self.flatten2.bias.view(1, 2, 2))
        v11 = (x3 * v11)
        v11 = (v11 / 0.949999988079071)
        v12 = self.linear6(torch.nn.functional.relu(v11))
        v11 = torch.nn.functional.relu(torch.nn.functional.hardtanh(v11))
        v13 = self.flatten3(torch.nn.functional.hardtanh(v11))
        v14 = self.linear4(torch.nn.functional.relu(v13))
        v14 = v14.permute(0, 2, 1)
        v11 = (v14 + v12)
        v11 = v11.permute(0, 2, 1)
        v9 = self.reshape1(v9)
        v9 = (v9 + self.linear1.bias.view(1, 2, 1))
        v10 = v10.permute(0, 2, 1)
        v10 = (v10 + self.linear2.bias.view(1, 1, 2))
        v9 = self.reshape1(v9)
        v9 = v9.permute(0, 2, 1)
        v12 = (v9 - self.linear2.bias.view(1, 2, 1))
        v12 = (x3 * v12)
        v12 = (v12 / 0.949999988079071)
        v13 = self.linear3(torch.nn.functional.swish(v12))
        v12 = torch.nn.functional.swish(torch.nn.functional.hardtanh(v12))
        v14 = x3.permute(0, 2, 1)
        v15 = self.reshape2(v14)
        v11 = (v12 + v11)
        v11 = (x3 + v11)
        v14 = self.reshape3(v14)
        v15 = v15.permute(0, 2, 1)
        v15 = (v15 + self.linear4.bias.view(1, 2, 1))
        v15 = (v11 == v15)
        v15 = (v15 * v14)
        v15 = (v15 * 0.949999988079071)
        v15 = v15.permute(0, 2, 1)
        v15 = torch.nn.functional.hardtanh(v15)
        v13 = (v13 - self.flatten2.bias.view(1, 2, 2))
        v13 = (x3 * v13)
        v13 = (v13 / 0.949999988079071)
        v9 = v13.reshape(1, 4)
        v16 = self.linear5(v9)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Flatten' object has no attribute 'bias'

jit:
bias

from user code:
   File "<string>", line 41, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''