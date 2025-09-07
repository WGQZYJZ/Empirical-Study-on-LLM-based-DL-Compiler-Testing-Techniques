import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- float('inf')), float('inf'), float('nan'), 0.0])
is_neginf = torch.isneginf(input_data)