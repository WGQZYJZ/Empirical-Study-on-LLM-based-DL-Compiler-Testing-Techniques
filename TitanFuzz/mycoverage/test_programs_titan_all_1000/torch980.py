import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
abs_transform = torch.distributions.transforms.AbsTransform()
output_data = abs_transform(input_data)