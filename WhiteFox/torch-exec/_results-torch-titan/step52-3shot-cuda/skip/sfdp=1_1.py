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



class ScaledDotProductAttention(nn.Module):

    def __init__(self, dropout, **unused):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, q_tensor, k_tensor, v_tensor):
        qk_tensor = torch.matmul(q_tensor, k_tensor.transpose((- 2), (- 1)))
        scale_factor = (k_tensor.size((- 1)) ** 0.5)
        inv_scale_factor = (1.0 / scale_factor)
        scaled_dot_product_tensor = (qk_tensor * inv_scale_factor)
        softmax_qk_tensor = F.softmax(scaled_dot_product_tensor, dim=(- 1))
        dropout_qk_tensor = self.dropout(softmax_qk_tensor)
        output_tensor = torch.matmul(dropout_qk_tensor, v_tensor)
        return output_tensor




class BertSelfAttention(nn.Module):

    def __init__(self, num_hidden_layers, **unused):
        super().__init__()
        self.attention = nn.ModuleList([ScaledDotProductAttention(dropout) for _ in range(num_hidden_layers)])

    def forward(self, hidden_states):
        for attention_layer in self.attention:
            hidden_states = attention_layer(hidden_states, hidden_states, hidden_states)
        return hidden_states



num_hidden_layers = 1
func = BertSelfAttention(1).to('cuda')



hidden_states = torch.randn(6, 128, 32, 4096)


test_inputs = [hidden_states]
