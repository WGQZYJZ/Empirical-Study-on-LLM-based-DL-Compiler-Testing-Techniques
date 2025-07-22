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

    def __init__(self, negative_slope):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 1, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.nn.functional.pixel_shuffle(v1, 4)
        v3 = self.conv2(v2)
        v4 = torch.nn.functional.pixel_shuffle(v3, 4)
        v5 = self.conv3(v4)
        return v5




negative_slope = 0.1


func = Model(negative_slope).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
pixel_shuffle expects its input's 'channel' dimension to be divisible by the square of upscale_factor, but input.size(-3)=8 is not divisible by 16

jit:
Failed running call_function <built-in method pixel_shuffle of type object at 0x7940922699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), 4), **{}):
Invalid input shape for pixel_shuffle: torch.Size([1, 8, 66, 66]) with upscale_factor = 4

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''