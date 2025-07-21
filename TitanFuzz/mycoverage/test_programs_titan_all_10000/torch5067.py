import torch
from torch import nn
from torch.autograd import Variable
input = torch.ones(1, 1, 3, 3)
conv_transpose = torch.nn.ConvTranspose2d(1, 1, 3, stride=2, padding=1, output_padding=1)