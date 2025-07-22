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
        self.key_project = torch.nn.Linear(input_dimension, (head_num * head_dimension))
        self.query_project = torch.nn.Linear(input_dimension, (head_num * head_dimension))
        self.value_project = torch.nn.Linear(input_dimension, (head_num * head_dimension))

    def forward(self, q, k, v):
        k = self.key_project(k)
        k = k.view(k.size(0), q.size(1), head_num, head_dimension)
        k = k.transpose(1, 2)
        q = self.query_project(q)
        q = q.view(q.size(0), q.size(1), head_num, head_dimension)
        q = q.transpose(1, 2)
        v = self.value_project(v)
        v = v.view(v.size(0), v.size(1), head_num, head_dimension)
        v = v.transpose(1, 2)
        scale_factor = (head_dimension ** (- 0.5))
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        output = output.transpose(1, 2)
        output = output.reshape(output.size(0), output.size(1), (output.size(2) * output.size(3)))
        return output



func = Model().to('cuda')



q = torch.randn(1, 512)



k = torch.randn(1, 1024)



v = torch.randn(1, 1024)


test_inputs = [q, k, v]
