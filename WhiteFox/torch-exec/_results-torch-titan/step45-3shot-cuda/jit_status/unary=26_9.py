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
        self.conv_t = torch.nn.ConvTranspose2d(113, 97, 1, stride=1, padding=0, bias=False)

    def forward(self, x6):
        l1 = self.conv_t(x6)
        l2 = (l1 > 0)
        l3 = (l1 * (- 0.6))
        l4 = torch.where(l2, l1, l3)
        return torch.nn.functional.relu(l4)




func = Model().to('cuda')



x6 = torch.randn(25, 113, 13, 17)


test_inputs = [x6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_k6zjdbq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_k6zjdbq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_k6zjdbq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''