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

    def forward(self, Q4, K4, V4, mask):
        qk = ((Q4 @ K4.transpose((- 2), (- 1))) / math.sqrt(Q4.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ V4)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 2, 4, 4)



K = torch.randn(1, 2, 4, 4)



V = torch.randn(1, 2, 4, 4)




mask = (torch.rand(1, 4, 4) > 0.7).fill_(float((- 100000)))


test_inputs = [Q, K, V, mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_ju98o8g/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_ju98o8g', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_ju98o8g/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''