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
        conv = torch.nn.Conv1d
        bn = torch.nn.BatchNorm1d
        relu = torch.nn.ReLU(inplace=True)
        self.feature = torch.nn.Sequential(conv(11, 3, padding=4, stride=2), conv(3, 64, kernel_size=3, stride=1, padding=1), conv(64, 64, stride=2), conv(64, 64, groups=64, kernel_size=3, padding=1, stride=1), bn(64, momentum=0.5), relu, conv(64, 64, groups=64, kernel_size=3, padding=1), conv(64, 64, groups=64, kernel_size=3, padding=1), conv(64, 64, groups=64, kernel_size=3, padding=1), bn(64, momentum=0.5), relu, conv(64, 96, groups=32, kernel_size=2, padding=1), bn(96, momentum=0.5), relu)
        self.classifier = torch.nn.Sequential(conv(96, 256, kernel_size=2, padding=1), bn(256, momentum=0.5), relu, conv(256, 256, kernel_size=2, padding=1), conv(256, 256, kernel_size=1), bn(256, momentum=0.5), relu, conv(256, 20, kernel_size=2, padding=1))

    def forward(self, x):
        x = self.feature(x)
        x = self.classifier(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 11, 26)


test_inputs = [x]
