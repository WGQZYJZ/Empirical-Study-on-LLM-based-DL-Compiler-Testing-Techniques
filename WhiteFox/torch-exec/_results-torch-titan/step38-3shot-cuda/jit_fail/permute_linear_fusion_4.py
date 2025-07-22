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

    def __init__(self) -> None:
        super().__init__()
        self.model1 = nn.Sequential(nn.Conv2d(1, 1, kernel_size=(1, 1), stride=(1, 1)), nn.Conv2d(20, 4, kernel_size=(1, 1), stride=(1, 1)))
        self.model2 = nn.Identity()
        self.model3 = nn.Sequential(nn.Conv2d(1, 1, kernel_size=(1, 1), stride=(2, 2)), nn.Conv2d(20, 4, kernel_size=(2, 2), stride=(1, 1)), nn.Conv2d(1, 1, kernel_size=(1, 1), stride=(2, 2)), nn.Conv2d(4, 5, kernel_size=(2, 2), stride=(1, 1)))

    def forward(self, x):
        y1 = torch.zeros_like(x)
        y1.requires_grad_(True)
        y2 = y1
        y3 = y1
        x0 = x.shape[0]
        x1 = x.shape[1]
        x2 = x.shape[2]
        x3 = x.shape[3]
        y1 = y1.view((y1.shape[0], 1, 1, y1.shape[1]))
        y1 = y1.expand((y1.shape[0], 4, y1.shape[2], y1.shape[3]))
        y1 = y1.reshape((1, 4, y1.shape[2], y1.shape[3]))
        y4 = self.model1(x)
        y5 = self.model2(x1)
        y6 = self.model3(x)
        y4 = y4.view((y4.shape[0], 20, y1.shape[2], y1.shape[3]))
        y4 = y4.transpose(2, 1).slice(2, int((y3.shape[2] * 0.5)), y3.shape[2])
        y4 = y4.transpose(2, 1).slice(2, int((y3.shape[2] * 0.5)), y3.shape[2])
        y_ = torch.relu(y4)
        y4 = y_.min(dim=(- 1))[0]
        y4 = y_.max(dim=(- 1))[0]
        y4 = torch.relu(y4)
        y4 = y4.contiguous().view((y4.shape[0], 4, y4.shape[1], y4.shape[2]))
        y4 = y4.clone(memory_format=torch.contiguous_format)
        y4 = y4.transpose(1, 2).view((y4.shape[0], y4.shape[1], (y4.shape[2] * y4.shape[3])))
        y4 = y4.contiguous().view((y4.shape[0], y4.shape[1], (y4.shape[2] * y4.shape[3])))
        y4 = y4.clone(memory_format=torch.contiguous_format)
        return y4




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 1, 1, 2]' is invalid for input of size 8

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2), requires_grad=True), (1, 1, 1, 2)), **{}):
shape '[1, 1, 1, 2]' is invalid for input of size 8

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''