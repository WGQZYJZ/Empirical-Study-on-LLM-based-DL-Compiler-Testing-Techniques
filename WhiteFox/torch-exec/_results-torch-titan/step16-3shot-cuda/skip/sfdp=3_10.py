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

    def __init__(self, query, key, value, dropout_p, scale_factor=1.0):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=1, embed_dim=query.shape[2], dropout=dropout_p)
        print(f'''input query
{query}
input key
{key}
input value
{value}''')
        self.attention.eval()
        self.attention.set_weights(query, key, value)
        print(f'''ouput query
{self.attention.in_proj_weight[0]}
ouput key
{self.attention.in_proj_weight[1]}
ouput value
{self.attention.in_proj_weight[2]}''')
        self.attention.train()
        self.scale_factor = scale_factor

    def forward(self, query, key, value):
        qk = self.attention.in_proj_weight[0].mm(self.attention.in_proj_weight[1].transpose(0, 1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = F.softmax(scaled_qk, dim=(- 1))
        dropout_qk = F.dropout(softmax_qk, p=self.attention.dropout, training=True)
        output = dropout_qk.mm(self.attention.in_proj_weight[2])
        return output



query = 1
key = 1
value = 1
dropout_p = 1

func = Model(query, key, value, dropout_p).to('cuda')



x0 = torch.randn(1, 64, 64)



x1 = torch.randn(1, 65, 64, 64)



x2 = torch.randn(1, 65, 64, 64)



x3 = torch.randn(1, 64, 64)


test_inputs = [x0, x1, x2, x3]
