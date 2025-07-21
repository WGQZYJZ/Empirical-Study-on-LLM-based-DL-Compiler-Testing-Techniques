import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 12, dtype=torch.float32).reshape(4, 3)
output_tensor = torch.Tensor.narrow(input_tensor, dimension=0, start=1, length=2)