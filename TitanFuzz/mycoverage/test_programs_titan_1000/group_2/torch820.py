import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 30, 45, 60, 90]], dtype=torch.float)
output_tensor = torch.Tensor.deg2rad(input_tensor)