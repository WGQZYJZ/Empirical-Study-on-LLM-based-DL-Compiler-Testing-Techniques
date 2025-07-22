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

    def forward(self, x1):
        b = {}
        a = {}
        c = {'strides': (1024, 1), 'requires_grad': False, 'padding': (0, 0), 'dilation': (1, 1), 'is_mkldnn': False, 'output_padding': (0, 0), 'groups': 1}
        a['dtype'] = torch.float64
        b['dtype'] = torch.float64
        a['shape'] = (4096, 512)
        a['m'] = torch.nn.ConvTranspose2d(a['shape'][1], a['shape'][0], (10, 1), stride=c['strides'], padding=c['padding'], output_padding=c['output_padding'], groups=c['groups'], bias=True, dilation=c['dilation'])
        a['m'].to(a['dtype'])
        b = todevice(b, a['dtype'])
        t1 = torch.full([1024, 512], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = a['m'](t1)
        return b['to'](t2)



func = Model().to('cpu')


x1 = torch.randn(1, 1024, 1, 1, device='cuda:0')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'todevice' is not defined

jit:
NameError: name 'todevice' is not defined

from user code:
   File "<string>", line 27, in torch_dynamo_resume_in_forward_at_26


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''