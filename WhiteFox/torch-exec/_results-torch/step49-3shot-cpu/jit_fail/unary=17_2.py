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

        def block(in_filters, out_filters, kernel_size=3, stride=1):
            layers = [nn.ConvTranspose2d(in_filters, out_filters, kernel_size, stride, padding=1), nn.BatchNorm2d(out_filters), nn.ReLU(True)]
            return nn.Sequential(*layers)
        self.model = nn.Sequential(block(2, 16), block(16, 32), nn.ConvTranspose2d(32, 3, kernel_size=3, stride=1, padding=1), nn.Tanh())

    def forward(self, z):
        return self.model(z)



func = Model().to('cpu')


z = torch.randn(1, 2)

test_inputs = [z]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 2]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7c0a25b96ec0>(*(FakeTensor(..., size=(1, 2)), Parameter(FakeTensor(..., size=(2, 16, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 2]

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''