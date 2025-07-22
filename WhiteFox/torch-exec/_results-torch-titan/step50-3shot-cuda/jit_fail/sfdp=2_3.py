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

    def __init__(self, num_heads, embed_size, dropout_p=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)
        self.dropout_p = dropout_p

    def forward(self, enc_input, dec_input):
        q = torch.matmul(query, self.key.transpose((- 2), (- 1)))
        k = torch.matmul(value, self.key.transpose((- 2), (- 1)))
        v = torch.matmul(key, self.value.transpose((- 2), (- 1)))
        q /= self.scale_factor
        dot_product = (q @ k.transpose((- 2), (- 1)))
        softmax_attn = nn.functional.softmax(dot_product, dim=(- 1)).type_as(query)
        attn = self.dropout(attn)
        out = (attn @ v)
        return out



num_heads = 1
embed_size = 1
func = Model(3, 6).to('cuda')



enc_input = torch.randn(2, 3, 5)



dec_input = torch.randn(2, 3, 4)


test_inputs = [enc_input, dec_input]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'key'

jit:
key

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''