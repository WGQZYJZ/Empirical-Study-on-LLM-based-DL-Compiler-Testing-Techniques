import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.rand(10, 3)
split_tensor = torch.split(tensor, split_size_or_sections=5, dim=0)