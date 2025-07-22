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



class ScaledDotProductAttention(torch.nn.Module):

    def __init__(self, embed_dim):
        super().__init__()
        self.inv_scale_factor = torch.sqrt(torch.FloatTensor([embed_dim])).to(device)

    def forward(self, q, k, v, mask=None, dropout_p=0.5):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



embed_dim = 1

func = ScaledDotProductAttention(embed_dim).to('cuda')



query = torch.randn(2, 2, 10)



key = torch.randn(2, 4, 10)




mask = torch.zeros(2, 2).to(torch.bool)

q = 1
k = 1

test_inputs = [query, key, mask, q, k]
