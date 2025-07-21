import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, requires_grad=True)
torch.nn.utils.clip_grad_norm_(input_data, max_norm=1)