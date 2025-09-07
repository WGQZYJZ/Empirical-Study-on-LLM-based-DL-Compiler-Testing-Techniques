import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.cumprod_(input_tensor, dim=1, dtype=torch.float32)