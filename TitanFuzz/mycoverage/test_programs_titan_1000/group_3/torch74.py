import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(10, (2, 3), dtype=torch.float)
output_tensor = torch.Tensor.normal_(input_tensor, mean=1, std=3)