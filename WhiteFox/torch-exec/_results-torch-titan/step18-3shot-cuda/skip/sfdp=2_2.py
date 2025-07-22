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



class MultiHeadAttentionWithDropout(torch.nn.Module):

    def __init__(self, num_head, head_size, dropout_p=0.5):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(head_size, num_head)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, q, k, v):
        (v, att_scores) = self.attention(q, k, v)
        v = self.dropout(v)
        return (v, att_scores)




num_head = 3

head_size = 1
func = MultiHeadAttentionWithDropout(num_head, num_head, dropout_p).to('cuda')



query = torch.randn(128, 10, 16)



key = torch.randn(128, 11, 16)

q = 1

test_inputs = [query, key, q]
