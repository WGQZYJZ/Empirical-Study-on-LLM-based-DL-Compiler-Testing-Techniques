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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=self.min_value)
        v3 = torch.clamp_max(v2, max=self.max_value)
        return v3


min_value = 0.1
max_value = 0.5
func = Model(min_value, max_value).to('cpu')















x1 = torch.tensor([[[-float('inf'), -float('inf'), -float('inf')], [-float('inf'), -float('inf'), -float('inf')], [0.13429049, 0.42054142, 0.49232574]], [[-float('inf'), -float('inf'), -float('inf')], [-float('inf'), -float('inf'), -float('inf')], [0.16724844, 0.54488579, 0.13837028]], [[0.37899566, 0.49897517, 0.57421803], [0.04109592, 0.0537002, 0.10894445], [0.49481009, 0.2592683, 0.41894564]], [[0.56204269, 0.08512115, 0.33184175], [0.55831719, 0.54522006, 0.53325084], [0.43586658, 0.3994147, 0.40781801]], [[0.15681072, 0.30640938, 0.3510543], [0.36911216, 0.20468537, 0.33771543], [0.36799981, 0.35813716, 0.19680074]], [[-0.01074977, 0.55161162, 0.0129508], [0.57406411, 0.25938863, 0.31956928], [0.53489292, 0.20629274, 0.53235047]], [[0.58171878, 0.50436866, 0.33519348], [0.53819465, 0.55675534, 0.06166232], [0.31104006, 0.14132397, 0.50913526]]], dtype=torch.float32)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5w3dnfxy/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp5w3dnfxy/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp5w3dnfxy', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''