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

    def __init__(self, num_classes: int=1000):
        super(Model, self).__init__()
        self.conv0 = nn.Conv2d(3, 32, kernel_size=(5, 5), stride=(1, 1), bias=False)
        self.features1 = nn.Sequential()
        self.features4 = nn.Sequential()
        self.features8 = nn.Sequential()
        self.features16 = nn.Sequential()
        self.features32 = nn.Sequential()
        self.extra0 = nn.Sequential()
        feature_layer_dimensions = [1, 1, 1, 1, 1]
        self.branch1 = Branch(self.conv0, [[512, 1, 1], [256, 1, 1], [64, 1, 1], [64, 1, 1]], feature_layer_dimensions, num_classes)
        self.branch2 = Branch(self.conv0, [[384, 2, 2], [192, 2, 2], [96, 2, 2], [96, 1, 1]], feature_layer_dimensions, num_classes)

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))

class Branch(nn.Module):

    def __init__(self, backbone, inception0, feature_layer_dimensions, num_classes):
        super(Branch, self).__init__()
        self.inception0 = inception.Inception_V4_Inception(inception0[-1], inception0, feature_dim=feature_layer_dimensions[0])
        self.inception1 = inception.Inception_V4_Inception(64, inception0, feature_dim=feature_layer_dimensions[1])

    def forward(self, x):
        return self.inception0(x) + self.inception1(x)


backbone = 1
inception0 = 1
feature_layer_dimensions = 1
num_classes = 1

func = Branch(backbone, inception0, feature_layer_dimensions, num_classes).to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
