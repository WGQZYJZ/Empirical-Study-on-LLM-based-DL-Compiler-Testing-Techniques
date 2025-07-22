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
        self.conv_t = torch.nn.ConvTranspose2d(19, 64, 3, stride=3, padding=1, bias=False)

    def forward(self, x):
        x1 = self.conv_t(x)
        x2 = torch.nn.LayerNorm([64, 12, 9], 33.31347222788556)
        return x2(x1)




func = Model().to('cuda')



x = torch.randn(4, 19, 93, 85)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument weight in method wrapper_CUDA__native_layer_norm)

jit:
Failed running call_function <function layer_norm at 0x7d25b23a3d30>(*(FakeTensor(..., device='cuda:0', size=(4, 64, 277, 253)), (64, 12, 9), Parameter(FakeTensor(..., size=(64, 12, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(64, 12, 9), requires_grad=True)), 33.31347222788556), **{}):
Given normalized_shape=[64, 12, 9], expected input with shape [64, 12, 9], but got input of size torch.Size([4, 64, 277, 253])

from user code:
   File "<string>", line 24, in <resume in forward>
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/normalization.py", line 196, in forward
    return F.layer_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''