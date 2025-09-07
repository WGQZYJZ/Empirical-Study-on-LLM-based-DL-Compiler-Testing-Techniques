import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([0.2, 0.4, 0.6, 0.8])
result = torch.bernoulli(input_data)
output_data = torch.Tensor([0.0, 0.0, 0.0, 0.0])
result = torch.bernoulli(input_data, out=output_data)
g = torch.Generator()
result = torch.bernoulli(input_data, generator=g)
result = torch.bernoulli(input_data, generator=g, out=output_data)