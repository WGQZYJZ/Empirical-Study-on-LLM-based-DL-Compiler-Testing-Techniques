import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1.2, 3.4, 5.6, 7.8, 9.0])
boundaries = torch.tensor([3.0, 6.0, 9.0])
output = torch.bucketize(input_data, boundaries)