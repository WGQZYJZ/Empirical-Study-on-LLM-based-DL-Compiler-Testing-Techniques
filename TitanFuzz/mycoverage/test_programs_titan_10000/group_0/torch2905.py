import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.cholesky(input_tensor, upper=False)
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.cholesky(input_tensor, upper=True)