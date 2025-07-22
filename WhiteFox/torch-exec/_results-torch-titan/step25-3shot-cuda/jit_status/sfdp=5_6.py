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
        self.heads = 32
        self.seq_len = 512
        self.dim = (128 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask[:, None, None, :])
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 32, 768, 128)



key = torch.randn(1, 32, 768, 128)



value = torch.randn(1, 32, 768, 128)



attn_mask = torch.randn(1, 768, 768)


test_inputs = [query, key, value, attn_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
RuntimeError: expand: the requested shape has too few dimensions!


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''