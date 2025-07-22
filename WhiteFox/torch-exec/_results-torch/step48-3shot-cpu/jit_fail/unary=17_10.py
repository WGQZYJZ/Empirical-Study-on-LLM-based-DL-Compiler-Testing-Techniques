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
        self.conv1 = torch.nn.ConvTranspose3d(1, 10, kernel_size=(2, 4, 6), stride=(2, 2, 2))
        self.conv2 = torch.nn.ConvTranspose3d(10, 20, kernel_size=(2, 3, 5), stride=(1, 3, 1))
        self.conv3 = torch.nn.ConvTranspose3d(20, 1, kernel_size=(2, 2, 4), stride=(1, 3, 4))

    def forward(self, x0):
        v0 = self.conv1(x0)
        v1 = torch.relu(v0)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        v4 = self.conv3(torch.unsqueeze(v3, dim=0))
        return torch.tanh(torch.squeeze(v4, dim=0))



func = Model().to('cpu')


x0 = torch.randn(1, 1, 16, 32, 32)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [1, 1, 20, 33, 198, 72]

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x750307996ec0>(*(FakeTensor(..., size=(1, 1, 20, 33, 198, 72)), Parameter(FakeTensor(..., size=(20, 1, 2, 2, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 3, 4), (0, 0, 0), (0, 0, 0), 1, (1, 1, 1)), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [1, 1, 20, 33, 198, 72]

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''