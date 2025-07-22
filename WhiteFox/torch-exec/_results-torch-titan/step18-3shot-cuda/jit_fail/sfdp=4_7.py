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

    def __init__(self, d_model, nhead, num_encoder_layers=1):
        super().__init__()
        encoder_layer = torch.nn.TransformerEncoderLayer(d_model, nhead)
        self.transformer_encoder = torch.nn.TransformerEncoder(encoder_layer, num_encoder_layers)

    def forward(self, src, src_mask=None):
        output = self.transformer_encoder(src, src_mask)
        return output



d_model = 1
nhead = 1

func = Model(d_model, nhead).to('cuda')



src = torch.randn(10, 64, 128)



src_mask = torch.randn(10, 1, 64, 64).round()


test_inputs = [src, src_mask]

# JIT_FAIL
'''
direct:
For batched (3-D) `query`, expected `attn_mask` to be `None`, 2-D or 3-D but found 4-D tensor instead

jit:
Failed running call_module L__self___transformer_encoder(*(FakeTensor(..., device='cuda:0', size=(10, 64, 128)), FakeTensor(..., device='cuda:0', size=(10, 1, 64, 64))), **{}):
For batched (3-D) `query`, expected `attn_mask` to be `None`, 2-D or 3-D but found 4-D tensor instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''