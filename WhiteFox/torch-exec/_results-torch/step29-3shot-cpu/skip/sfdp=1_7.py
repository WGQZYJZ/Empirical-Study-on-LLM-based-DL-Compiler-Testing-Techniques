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

    def forward(self, __input_tensor, __input_tensor):
        k0 = torch.tensor([[[1.0], [1.0]]], requires_grad=True)
        k1 = torch.tensor([[[1.0, 1.0], [1.0, 1.0]]], requires_grad=True)
        k2 = torch.tensor([[[1.0, 1.0, 0.0], [1.0, 1.0, 1.0]]], requires_grad=True)
        k = torch.cat((k0, k1, k2), dim=-1)
        v0 = torch.tensor([[[0.0, 1.0, 1.0]]], requires_grad=True)
        v1 = torch.tensor([[[0.0, 1.0, 1.0], [0.0, 1.0, 1.0]]], requires_grad=True)
        v2 = torch.tensor([[[0.0, 0.0, 1.0], [1.0, 1.0, 1.0]]], requires_grad=True)
        v = torch.cat((v0, v1, v2), dim=-1)
        q0 = torch.tensor([[[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]]], requires_grad=True)
        q1 = torch.tensor([[[0.0, 0.0, 1.0], [1.0, 1.0, 1.0]]], requires_grad=True)
        q2 = torch.tensor([[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]], requires_grad=True)
        q3 = torch.tensor([[[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]]], requires_grad=True)
        q4 = torch.tensor([[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]], requires_grad=True)
        q5 = torch.tensor([[[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]], requires_grad=True)
        q = torch.cat((q0, q1, q2, q3, q4, q5), dim=-1)
        scale_factor = torch.tensor([[[1.0]], [[2.0]], [[1.5]]], requires_grad=False)
        inv_scale_factor = scale_factor.pow(-1)
        dropout_p = 0.5
        k = torch.nn.functional.dropout(k, p=dropout_p)
        v = torch.nn.functional.dropout(v, p=dropout_p)
        q = torch.nn.functional.dropout(q, p=dropout_p)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 6, 3, requires_grad=True)

x2 = torch.randn(1, 6, 3, requires_grad=True)

test_inputs = [x1, x2]
