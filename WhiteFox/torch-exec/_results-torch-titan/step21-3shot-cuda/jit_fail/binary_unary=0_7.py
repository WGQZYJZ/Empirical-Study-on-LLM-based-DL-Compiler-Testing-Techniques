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
        self.conv1 = torch.nn.Conv2d(4, 6, 4, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(6, 6, 4, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(6, 6, 4, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(6, 6, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.norm(v7, dim=(- 1))
        v9 = torch.transpose(v8, (- 1), 1)
        v10 = torch.matmul(v9, v7)
        v11 = torch.sigmoid(v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 4, 31, 55)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [6, 6] but got: [6, 28].

jit:
Failed running call_function <built-in method matmul of type object at 0x7dfb0a4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 28, 6)), FakeTensor(..., device='cuda:0', size=(1, 6, 28, 52))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [6, 6] but got: [6, 28].

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''