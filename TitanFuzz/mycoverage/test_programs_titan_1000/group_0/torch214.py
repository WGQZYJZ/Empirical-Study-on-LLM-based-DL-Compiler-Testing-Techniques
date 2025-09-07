import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(low=0, high=255, size=(1, 1, 4, 4), dtype=torch.uint8)
output = torch.nn.functional.pixel_unshuffle(input, 2)