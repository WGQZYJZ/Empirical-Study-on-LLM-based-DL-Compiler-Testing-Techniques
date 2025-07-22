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



class MultiheadAttention(nn.Module):

    def __init__(self, n_head, d_model, d_k, d_v, dropout=0):
        super(MultiheadAttention, self).__init__()
        self.n_head = n_head
        self.d_k = d_k
        self.d_v = d_v
        self.w_qs = nn.Linear(d_model, (n_head * d_k))
        self.w_ks = nn.Linear(d_model, (n_head * d_k))
        self.w_vs = nn.Linear(d_model, (n_head * d_v))
        nn.init.normal_(self.w_qs.weight, mean=0, std=np.sqrt((2.0 / (d_model + d_k))))
        nn.init.normal_(self.w_ks.weight, mean=0, std=np.sqrt((2.0 / (d_model + d_k))))
        nn.init.normal_(self.w_vs.weight, mean=0, std=np.sqrt((2.0 / (d_model + d_v))))
        nn.init.constant_(self.w_qs.bias, 0)
        nn.init.constant_(self.w_ks.bias, 0)
        nn.init.constant_(self.w_vs.bias, 0)
        self.attention = ScaledDotProductAttention(temperature=np.power(d_k, 0.5))
        self.layer_norm = nn.LayerNorm(d_model)
        self.fc = nn.Linear((n_head * d_v), d_model)
        nn.init.xavier_normal_(self.fc.weight)
        nn.init.constant_(self.fc.bias, 0)
        self.dropout = nn.Dropout(dropout)

    def forward(self, q, k, v, mask=None):
        d_k = self.d_k
        d_v = self.d_v
        n_head = self.n_head
        sz_b = q.size(0)
        len_q = q.size(1)
        len_k = k.size(1)
        len_v = v.size(1)
        residual = q
        q = self.w_qs(q).view(sz_b, len_q, n_head, d_k)
        k = self.w_ks(k).view(sz_b, len_k, n_head, d_k)
        v = self.w_vs(v).view(sz_b, len_v, n_head, d_v)
        q = q.permute(2, 0, 1, 3).contiguous().view((- 1), len_q, d_k)
        k = k.permute(2, 0, 1, 3).contiguous().view((- 1), len_k, d_k)
        v = v.permute(2, 0, 1, 3).contiguous().view((- 1), len_v, d_v)
        mask = mask.repeat(n_head, 1, 1)
        (output, attn) = self.attention(q, k, v, mask=mask)
        output = output.view(n_head, sz_b, len_q, d_v)
        output = output.permute(1, 2, 0, 3).contiguous().view(sz_b, len_q, (- 1))
        output = self.dropout(self.fc(output))
        output = self.layer_norm((output + residual))
        return (output, attn)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.multiheadattention = MultiheadAttention(2, 20, 5, 5)

    def forward(self, x1, x2, x3):
        (v1, _) = self.multiheadattention(x1, x2, x3)
        return v1



func = Model().to('cuda')



x1 = torch.randn(1, 10, 20)



x2 = torch.randn(1, 15, 20)



x3 = torch.randn(1, 16, 20)


test_inputs = [x1, x2, x3]
