import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
scalar = 2
output_tensor = torch.Tensor.mul_(input_tensor, scalar)