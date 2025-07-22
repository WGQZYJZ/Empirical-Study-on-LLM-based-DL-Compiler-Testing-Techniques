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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.attention_dropout = nn.Dropout(config.attention_dropout)
        self.dropout = nn.Dropout(config.dropout)
        self.output_layer = nn.Linear(config.attention_dim, self.output_dim)

    def forward(self, query, key, value, mask):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(math.sqrt(query.size((- 1))))
        if (mask is not None):
            if (not hasattr(mask, 'dtype')):
                mask = mask.byte()
            if (len(mask.size()) < len(scaled_qk.size())):
                mask = mask.unsqueeze(1)
            mask = mask.unsqueeze(1).repeat(1, query.size(1), 1, 1)
            scaled_qk.masked_fill_(mask, (- 10000.0))
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=(- 1))
        dropout_qk = self.attention_dropout(softmax_qk)
        output = torch.matmul(dropout_qk, value)
        return self.dropout(output)



func = Model().to('cuda')

query = 1
key = 1
value = 1
mask = 1

test_inputs = [query, key, value, mask]
