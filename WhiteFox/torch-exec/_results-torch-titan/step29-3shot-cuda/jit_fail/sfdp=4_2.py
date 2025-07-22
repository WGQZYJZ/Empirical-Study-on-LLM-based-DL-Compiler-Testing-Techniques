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
        self.layer = torch.nn.TransformerEncoder(encoder_layer=torch.nn.TransformerEncoderLayer(d_model=64, nhead=4), num_layers=2, norm=torch.nn.LayerNorm(64))

    def forward(self, src, src_mask):
        output = self.layer(src, src_mask=src_mask)
        return output




func = Model().to('cuda')



src = torch.randn(10, 32, 512)



src_mask = (torch.rand(32, 32) > 0).float().cuda()


test_inputs = [src, src_mask]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'src_mask'

jit:
Failed running call_module L__self___layer(*(FakeTensor(..., device='cuda:0', size=(10, 32, 512)),), **{'src_mask': FakeTensor(..., device='cuda:0', size=(32, 32))}):
forward() got an unexpected keyword argument 'src_mask'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''