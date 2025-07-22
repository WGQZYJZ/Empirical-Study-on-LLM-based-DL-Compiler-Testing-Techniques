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
        self.key = torch.nn.Linear(64, 64)
        self.query = torch.nn.Linear(64, 64)

    def forward(self, v1):
        k = self.key(v1)
        q = self.query(v1)
        mat = torch.matmul(q, k.transpose((- 1), (- 2)))
        scaled_mat = (mat / 140737488355328)
        softmax_mat = torch.nn.functional.softmax(scaled_mat, dim=(- 1))
        dropout_mat = torch.nn.functional.dropout(softmax_mat, p=0.1)
        output = torch.matmul(dropout_mat, v1)
        return output



func = Model().to('cuda')



v1 = torch.randn(1, 32, 64)


test_inputs = [v1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbrodskqd/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpbrodskqd', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpbrodskqd/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''