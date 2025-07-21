import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5, 5, 5))
torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3))(input)
torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3), return_indices=True)(input)
torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3), return_indices=False)(input)
torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3), return_indices=True)(input)[0]
torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3), return_indices=True)(input)[1]