import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(3, 4, 5)
reshape_transform = torch.distributions.transforms.ReshapeTransform((3, 4, 5), (5, 12))
output_data = reshape_transform(input_data)