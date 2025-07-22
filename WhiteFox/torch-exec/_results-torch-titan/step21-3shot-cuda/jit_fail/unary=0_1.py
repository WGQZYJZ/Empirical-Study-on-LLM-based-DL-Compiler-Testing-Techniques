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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 10, stride=1)
        self.conv2 = nn.Conv2d(32, 10, 5, stride=1)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(((10 * 11) * 11), 200)
        self.fc2 = nn.Linear(200, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = self.conv2_drop(self.conv2(x))
        x = x.view((- 1), ((10 * 11) * 11))
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        return F.log_softmax(self.fc2(x), dim=1)




func = Model().to('cuda')



x = torch.randn(1, 1, 88, 187)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[-1, 1210]' is invalid for input of size 29750

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 10, 35, 85)), -1, 1210), **{}):
shape '[-1, 1210]' is invalid for input of size 29750

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''