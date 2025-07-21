import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(start=0, end=10, step=1, dtype=torch.float32)
output_tensor = torch.Tensor.nextafter_(input_tensor, other=10.0)