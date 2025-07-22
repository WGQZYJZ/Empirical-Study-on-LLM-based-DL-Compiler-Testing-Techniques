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

    def forward(self, x1):
        v1 = nn.ConvTranspose1d(5, 2, kernel_size=3)
        v2 = nn.ConvTranspose2d(5, 2, kernel_size=3)
        v3 = nn.ConvTranspose3d(5, 2, kernel_size=3)
        v4 = v3.forward(x1)
        v5 = v2.forward(v4)
        v6 = v1.forward(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(3, 5, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [3, 5, 3]

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x740485f96ec0>(*(FakeTensor(..., size=(3, 5, 3)), Parameter(FakeTensor(..., size=(5, 2, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (0, 0, 0), 1, (1, 1, 1)), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [3, 5, 3]

from user code:
   File "<string>", line 19, in torch_dynamo_resume_in_forward_at_18
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''