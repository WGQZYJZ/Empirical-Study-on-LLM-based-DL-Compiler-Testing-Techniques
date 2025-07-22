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

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

class _PipelinedPipelinedBertEncoderLayer(nn.Module):

    def __init__(self):
        super().__init__()
        self.attention = _PipelinedPipelinedBertAttention(config)
        self.output = _BertOutput(config)
        if self.is_decoder:
            self.crossattention = _PipelinedPipelinedBertAttention(config)
            self.crossoutput = _BertOutput(config)


func = _PipelinedPipelinedBertEncoderLayer().to('cpu')


query = torch.randn(20, 8, 32)

key = torch.randn(20, 8, 32)

value = torch.randn(20, 8, 32)

inv_scale_factor = torch.randn(20, 8, 1)
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]
