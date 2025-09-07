import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.eig(_input_tensor, eigenvectors=False)