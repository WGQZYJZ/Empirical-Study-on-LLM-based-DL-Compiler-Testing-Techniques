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

    def __init__(self, num_heads=1):
        super().__init__()
        self.multiheaded_attention = torch.nn.MultiheadAttention(embed_dim=256, num_heads=num_heads, dropout=0.1)

    def forward(self, x1, x2):
        x1 = x1.permute((1, 0, 2))
        x2 = x2.permute((1, 0, 2))
        qk_v = self.multiheaded_attention(x1, x1, x1)
        softmax_qk = torch.nn.functional.softmax(qk_v[0], dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        scaled_qk = torch.tensor(1.0 / math.sqrt(qk_v[0].size(-1))) * dropout_qk
        output = (torch.matmul(dropout_qk, qk_v[0]),)
        return output


func = Model().to('cpu')


x1 = torch.randn(3, 5, 256)

x2 = torch.randn(3, 5, 256)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [5, 256] but got: [5, 3].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a2149596ec0>(*(FakeTensor(..., size=(5, 3, 256)), FakeTensor(..., size=(5, 3, 256))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [5, 256] but got: [5, 3].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''