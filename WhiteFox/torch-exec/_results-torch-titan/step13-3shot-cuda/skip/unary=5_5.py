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
        self.conv_transpose = torch.nn.ConvTranspose2d(7, 4, 3, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * torch.as_tensor([1.0, 1.0, 2.0, 2.0]))
        v3 = torch.floor((v1 / torch.as_tensor([1.0, 1.0, 2.0, 2.0]))).int()
        v4 = v1.transpose(1, 0)
        v5 = v1.sum(axis=2)
        v6 = torch.sqrt(torch.cumsum((1 / torch.tensor([1.0, 2.0, 3.0, 4.0])), axis=0, initial_value=torch.tensor([0.0, 0.0, 0.0, 0.0])))
        v7 = torch.quantile((5 / 0), torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]))
        v8 = torch.nn.MaxPool2d(2, stride=2, padding=1)
    return v6




func = Model().to('cuda')



x1 = torch.randn(5, 7, 56, 56)


test_inputs = [x1]
