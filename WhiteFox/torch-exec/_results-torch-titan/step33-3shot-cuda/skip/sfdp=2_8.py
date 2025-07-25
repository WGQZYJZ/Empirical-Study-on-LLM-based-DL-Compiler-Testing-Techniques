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

    def __init__(self, input_tensor):
        super().__init__()
        self.num_heads = __FILL_IN_YOUR_CODE_HERE__
        input_channels = input_tensor.size(1)
        self.query = torch.nn.Linear(input_tensor.size(1), input_channels)
        self.key = torch.nn.Linear(input_tensor.size(1), input_channels)
        self.value = torch.nn.Linear(input_tensor.size(1), input_channels)

    def forward(self, x):
        query = self.query(x).view(x.size(0), self.num_heads, x.size(1), 1).transpose(1, 2)
        key = self.key(x).view(x.size(0), self.num_heads, x.size(1), 1).transpose(1, 2)
        value = self.value(x).view(x.size(0), self.num_heads, x.size(1), 1).transpose(1, 2)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(__FILL_IN_YOUR_CODE_HERE__)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=__FILL_IN_YOUR_CODE_HERE__)
        output = torch.matmul(dropout_qk, value)
        return output.squeeze((- 1)).transpose(1, 2)



input_tensor = 1
func = Model(__FILL_IN_YOUR_CODE_HERE__).to('cuda')



x = torch.randn(8, 64, 32)


test_inputs = [x]
