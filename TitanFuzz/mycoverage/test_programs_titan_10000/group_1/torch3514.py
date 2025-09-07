import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(10, 10)
torch.Tensor.tensor_split(input_tensor, indices_or_sections=5, dim=0)