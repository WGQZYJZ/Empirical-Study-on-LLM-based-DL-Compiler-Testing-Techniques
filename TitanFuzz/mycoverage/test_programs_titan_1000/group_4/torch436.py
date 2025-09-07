import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(1, 11, dtype=torch.float32)
output_tensor = torch.Tensor.narrow(input_tensor, 0, 2, 5)