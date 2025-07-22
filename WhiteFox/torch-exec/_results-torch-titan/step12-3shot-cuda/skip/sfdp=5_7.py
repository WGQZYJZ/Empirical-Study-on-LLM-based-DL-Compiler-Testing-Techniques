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

    def __init__(self, hidden_size):
        super().__init__()
        self.attn_dropout_p = 0.5
        __init_weights_in_qkv__(self, hidden_size)

    def forward(self, q, k, v, q_mask=None):
        qk = (q @ k.transpose((- 2), (- 1)))
        qk = (qk / math.sqrt(q.size((- 1))))
        if (q_mask is not None):
            q = (q * q_mask)
        qk = (qk + self.attention_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, self.dropout_p, True)
        output = (attn_weight @ v)
        return output



hidden_size = 1
func = Model(hidden_size).to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.rand(1, 15, 128, 32)



x3 = torch.rand(1, 15, 128, 32)

q = 1

test_inputs = [x1, x2, x3, q]
