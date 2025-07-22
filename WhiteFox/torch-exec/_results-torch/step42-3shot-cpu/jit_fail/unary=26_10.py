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
        self.conv_t = torch.nn.ConvTranspose2d(6, 3, 3, stride=2, padding=1, bias=False, dilation=1, groups=1, output_padding=1)
        self.batch_norm = torch.nn.BatchNorm2d(3)

    def forward(self, x4):
        t1 = self.conv_t(x4)
        t2 = t1 > 0
        t3 = t1 * -0.7
        t4 = torch.where(t2, t1, t3)
        t5 = t4 < -0.5
        t6 = torch.where(t5, t4, torch.full_like(t4, -0.5))
        return self.batch_norm(t6)



func = Model().to('cpu')



x4 = torch.tensor([[[[1.4339, 1.0922, -0.6388, -0.1103, 0.1963], [0.3688, -1.3627, 0.4187, -3.6826, 0.6972], [0.3013, 0.6479, -0.8276, -0.609, -0.3269], [-1.0935, -0.696, 0.7967, -0.1933, -1.1418]], [[0.252, 1.0449, 1.4477, 0.6704, 0.332], [-1.117, -0.0059, 0.9746, 1.4818, 1.4852], [0.365, -0.6202, 0.9495, 0.5305, 0.0139], [-0.0812, 2.4373, -0.4203, -0.2284, 1.8471]], [[-0.9821, 1.2651, -0.0592, -1.8132, -0.7374], [-0.086, 0.6335, -0.3244, -0.3862, 0.1286], [-0.3208, -0.0389, 0.5319, 0.5077, 1.111], [-0.7375, 2.591, -1.9562, -0.2144, 1.4472]]]], dtype=torch.float32)

test_inputs = [x4]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [6, 3, 3, 3], expected input[1, 3, 4, 5] to have 6 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x726da0396ec0>(*(FakeTensor(..., size=(1, 3, 4, 5)), Parameter(FakeTensor(..., size=(6, 3, 3, 3), requires_grad=True)), None, (2, 2), (1, 1), (1, 1), 1, (1, 1)), **{}):
Given transposed=1, weight of size [6, 3, 3, 3], expected input[1, 3, 4, 5] to have 6 channels, but got 3 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''