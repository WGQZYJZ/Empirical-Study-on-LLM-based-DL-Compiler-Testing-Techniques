import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])
output_data = torch.nn.functional.one_hot(input_data, num_classes=5)