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

    def __init__(self, size, padding=4):
        super().__init__()
        self.size = size
        self.padding = padding

    def get_sliced_tensors(self, x1, x2, x3):
        (b, c, h, w) = x1.shape
        pad_h = (h + (self.padding * 2))
        pad_w = (w + (self.padding * 2))
        x1 = F.pad(x1, (self.padding, ((pad_w - w) - self.padding), self.padding, ((pad_h - h) - self.padding)))
        x2 = F.pad(x2, (self.padding, ((pad_w - w) - self.padding), self.padding, ((pad_h - h) - self.padding)))
        x3 = F.pad(x3, (self.padding, ((pad_w - w) - self.padding), self.padding, ((pad_h - h) - self.padding)))
        slice_h = (h - self.size)
        slice_w = (w - self.size)
        pad_h = self.padding
        pad_w = self.padding
        x1 = x1[:, :, pad_h:(pad_h + slice_h), pad_w:(pad_w + slice_w)]
        x2 = x2[:, :, pad_h:(pad_h + slice_h), pad_w:(pad_w + slice_w)]
        x3 = x3[:, :, pad_h:(pad_h + slice_h), pad_w:(pad_w + slice_w)]
        return (x1, x2, x3)

    def forward(self, x1, x2, x3):
        (x1, x2, x3) = self.get_sliced_tensors(x1, x2, x3)
        return torch.cat([x1, x2, x3], dim=1)



size = 1
func = Model(17).to('cuda')



x1 = torch.randn(2, 3, 64, 64)



x2 = torch.randn(2, 3, 64, 64)



x3 = torch.randn(2, 3, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6z0q8fho/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6z0q8fho', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6z0q8fho/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''