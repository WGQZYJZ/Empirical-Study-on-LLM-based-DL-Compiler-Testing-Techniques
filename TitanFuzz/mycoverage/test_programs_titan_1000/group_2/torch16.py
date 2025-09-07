import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
torch.minimum(input_tensor, other_tensor)
input_tensor = torch.randn(2, 3)
torch.min(input_tensor)
torch.min(input_tensor, dim=0, keepdim=False)