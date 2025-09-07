import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
torch.nn.init.uniform_(input_tensor, a=0.0, b=1.0)
input_tensor = torch.rand(2, 3)
torch.nn.init.normal_(input_tensor, mean=0.0, std=1.0)