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

    def __init__(self, min_value, max_value):
        super(Model, self).__init__()
        self.leaky_relu_3 = torch.nn.LeakyReLU()
        self.bn = torch.nn.BatchNorm2d(3)
        self.conv9bit = torch.quantization.fake_quantize_per_tensor_affine(torch.nn.Conv2d(3, 8, 1, stride=1, padding=1), scale=0.015794, zero_point=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        x1 = self.bn(x1)
        x1 = self.conv9bit(x1)
        x2 = x1.clamp(self.min_value, self.max_value)
        x3 = self.leaky_relu_3(x2)
        return x3




min_value = 0


max_value = 6.4


func = Model(min_value, max_value).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]
