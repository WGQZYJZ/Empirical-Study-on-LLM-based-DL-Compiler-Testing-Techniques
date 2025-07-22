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

    def forward(self, Q5, K, V, mask):
        qk = ((Q5 @ K.transpose((- 2), (- 1))) / math.sqrt(Q5.size((- 1))))
        qk = (qk + mask)
        attn = F.softmax(qk, dim=(- 1))
        output = (attn @ V)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 3, 56, 56)



K = torch.randn(1, 3, 56, 56)



V = torch.randn(1, 3, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).unsqueeze(0).unsqueeze(0).double()


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
expected scalar type Float but found Double

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmph4rjdgyh/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmph4rjdgyh', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmph4rjdgyh/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''