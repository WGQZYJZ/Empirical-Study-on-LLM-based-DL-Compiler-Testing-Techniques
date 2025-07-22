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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(5, 5, stride=1, padding=14, input_size=(11, 10), output_padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = torch.nn.Sigmoid()(v1)
        v3 = (v1 * v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 10, 11)


test_inputs = [x1]
