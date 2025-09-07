import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3)
softmax_transform = torch.distributions.transforms.SoftmaxTransform(cache_size=0)
output_data = softmax_transform(input_data)