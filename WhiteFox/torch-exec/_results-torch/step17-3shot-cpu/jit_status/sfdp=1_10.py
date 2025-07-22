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

    def __init__(self, query, key, value, inv_scale_factor, dropout_p: float=0.25) -> None:
        super().__init__()
        self._dropout_p = dropout_p
        self._inv_scale_factor = inv_scale_factor

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self._inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self._dropout_p)
        output = dropout_qk.matmul(value)
        return output


query = torch.randn(1, 256, 256)
key = torch.randn(1, 256, 256)
value = torch.randn(1, 256, 256)
inv_scale_factor = 1
func = Model(query, key, value, inv_scale_factor).to('cpu')


query = torch.randn(1, 256, 256)

key = torch.randn(1, 256, 256)

value = torch.randn(1, 256, 256)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptaspu6cr/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmptaspu6cr/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmptaspu6cr', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''