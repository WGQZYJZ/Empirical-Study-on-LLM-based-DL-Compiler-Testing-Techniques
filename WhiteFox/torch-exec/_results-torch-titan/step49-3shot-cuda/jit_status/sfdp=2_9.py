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

    def forward(self, q_data, k_data):
        q = torch.randn(8, 8, 5, 1, device=q_data.device)
        k = torch.randn(8, 8, 5, 1, device=q_data.device)
        matmul1 = q.matmul(k.transpose((- 2), (- 1)))
        div1 = matmul1.div(torch.tensor(8.0, device=matmul1.device))
        softmax1 = div1.softmax(dim=(- 1))
        dropout = torch.nn.functional.dropout(softmax1, p=0.5)
        m = dropout.matmul(torch.randn(8, 8, 5, 10, device=dropout.device))
        return m



func = Model().to('cuda')



q_data = torch.randn(1, 8, 5, 1, device='cpu')



k_data = torch.randn(1, 8, 5, 1, device='cpu')


test_inputs = [q_data, k_data]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2ka7ulm6/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp2ka7ulm6', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp2ka7ulm6/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''