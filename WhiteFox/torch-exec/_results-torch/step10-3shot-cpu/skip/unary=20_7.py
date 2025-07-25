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

class UpsampleBlock(nn.Module):

    def __init__(self, in_channels: int, out_channels: int, conv_channel_multiplier: int=2, num_layers: int=4, kernel_size: int=3, stride: int=1):
        super().__init__()
        channels = in_channels
        layers = [nn.Upsample(scale_factor=(1, 2), mode='bicubic'), nn.ZeroPad2d([0, 1, 0, 0]), nn.Conv2d(in_channels, channels * conv_channel_multiplier, kernel_size=1, stride=1, bias=False), nn.BatchNorm2d(channels * conv_channel_multiplier), nn.ZeroPad2d([kernel_size // 2 - 1, kernel_size // 2 - 1, kernel_size // 2 - 1, kernel_size // 2 - 1]), nn.ReLU()]
        for _ in range(num_layers - 1):
            layers += [nn.ConvTranspose2d(channels, channels, kernel_size=kernel_size, stride=stride, pad=kernel_size // 2, bias=False), nn.BatchNorm2d(channels), nn.ReLU()]
            channels *= conv_channel_multiplier
        layers += [nn.ConvTranspose2d(channels, out_channels, kernel_size=kernel_size, stride=stride, pad=kernel_size // 2, bias=False), nn.BatchNorm2d(out_channels), nn.ReLU()]
        self.skip = nn.ConvTranspose2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False)
        self.module = nn.Sequential(*layers)

    def forward(self, input: torch.Tensor):
        return self.module(input) + self.skip(input)

class UpsamplingModel(nn.Module):

    def __init__(self, in_channels: int, out_channels: int, width_multiplier: float=2.0, channel_multiplier: int=2, num_layers: int=4, kernel_size: int=3, stride: int=1):
        super().__init__()
        down_layers: List[UpsampleBlock] = []
        in_channels = int(in_channels)
        out_channels = channel_multiplier * pow(2, math.log2(width_multiplier) - 1) * out_channels
        channel_multiplier_ = int(pow(width_multiplier, 1 / num_layers) * channel_multiplier)
        for i in range(math.log2(width_multiplier)):
            out_channels_ = channel_multiplier_ * pow(2, i)
            if in_channels != out_channels_:
                down_layers.append(UpsampleBlock(in_channels, out_channels_, channel_multiplier_, num_layers, kernel_size, stride if i == 0 else 1))
                in_channels = out_channels_
        self.skip = nn.ConvTranspose2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False)
        self.down = nn.Sequential(*down_layers)

    def forward(self, input: torch.Tensor):
        return self.skip(self.down(input))


in_channels = 1
out_channels = 1

func = UpsamplingModel(in_channels, out_channels).to('cpu')

input = 1

test_inputs = [input]
