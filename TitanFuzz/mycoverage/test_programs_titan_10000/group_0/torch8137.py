import torch
from torch import nn
from torch.autograd import Variable

input_tensor = np.random.rand(2, 3)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1, generator=None)