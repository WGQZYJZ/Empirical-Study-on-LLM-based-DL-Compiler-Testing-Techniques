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
        super(self).__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, inputs, output_size, attention_probs_dropout_prob, hidden_dropout_prob):
        hidden_size = inputs.shape[-1]
        query = self.linear(inputs)
        query = query / np.sqrt(hidden_size)
        key = self.linear(inputs)
        key = key / np.sqrt(hidden_size)
        key_t = torch.transpose(key, -2, -1)
        dot = torch.matmul(query, key_t)
        mask = torch.ones(inputs.shape, dtype=torch.float32)
        dot = dot + mask
        attention_mask = torch.ones((attention_probs.size(0), attention_probs.size(1), attention_probs.size(1)), dtype=torch.float32)
        attention_probs = F.dropout(input=attention_mask, p=attention_probs_dropout_prob)
        attention_probs = F.softmax(attention_probs)
        attention_probs = F.dropout(input=attention_probs, p=dropout_prob)


func = Model().to('cpu')


inputs = torch.randn(8, 8, 4)
output_size = 1
attention_probs_dropout_prob = 1
hidden_dropout_prob = 1

test_inputs = [inputs, output_size, attention_probs_dropout_prob, hidden_dropout_prob]
