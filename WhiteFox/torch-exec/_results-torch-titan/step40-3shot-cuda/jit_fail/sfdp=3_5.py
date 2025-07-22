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

    def forward(query, key, value, scale_factor, dropout_p):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = (v1 * scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        output = v4.matmul(value)
        return output




func = Model().to('cuda')



dim_size = (128 + 128)


seq_len = 3


batch_size = 1


query = torch.randn(batch_size, seq_len, dim_size)



dim_size = (128 + 128)


seq_len = 3


batch_size = 1


key = torch.randn(batch_size, seq_len, dim_size)



dim_size = (128 + 128)


seq_len = 3


batch_size = 1


value = torch.randn(batch_size, seq_len, dim_size)




scale_factor = torch.sigmoid(torch.randn(1))


test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
matmul(): argument 'input' (position 1) must be Tensor, not Model

jit:
matmul(): argument 'input' (position 1) must be Tensor, not Model
'''