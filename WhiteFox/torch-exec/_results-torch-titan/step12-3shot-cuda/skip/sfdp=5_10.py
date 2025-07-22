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

    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        scaled_dot_product = torch.matmul((query / math.sqrt(self.input_shape)), key.transpose((- 2), (- 1)))
        scores = nn.functional.dropout(scaled_dot_product, p=self.dropout, training=training)
        attn_weights = torch.softmax(scores, dim=(- 1), dtype=at.float)
        output = torch.matmul(attn_weights, value)
        self(query, key, value, attn_weights)
        return output



func = MultiheadAttention(d_model=512, num_heads=8, dropout=0.1).to('cuda')



query = torch.randn(8, 60, 512)



key = torch.randn(8, 100, 512)



value = torch.randn(8, 100, 512)


test_inputs = [query, key, value]
