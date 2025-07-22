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
        self.conv_t = torch.nn.ConvTranspose2d(2, 6, 5, stride=2, padding=1, bias=False)

    def forward(self, x12):
        x1 = self.conv_t(x12)
        x2 = x1 > 0
        x3 = x1 * -9.821
        x4 = torch.where(x2, x1, x3)
        x5 = torch.transpose(x4, 1, 3)
        x6 = torch.transpose(x4, 2, 3)
        return torch.nn.functional.pixel_shuffle(x5, 3)



func = Model().to('cpu')


x12 = torch.randn(2, 2, 24, 99)

test_inputs = [x12]

# JIT_FAIL
'''
direct:
pixel_shuffle expects its input's 'channel' dimension to be divisible by the square of upscale_factor, but input.size(-3)=199 is not divisible by 9

jit:
Failed running call_function <built-in method pixel_shuffle of type object at 0x71727a396ec0>(*(FakeTensor(..., size=(2, 199, 49, 6)), 3), **{}):
Invalid input shape for pixel_shuffle: torch.Size([2, 199, 49, 6]) with upscale_factor = 3

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''