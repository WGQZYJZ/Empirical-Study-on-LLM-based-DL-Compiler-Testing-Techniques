import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(size=(10,), dtype=torch.float32)
output_tensor = torch.Tensor.arctan(input_tensor)