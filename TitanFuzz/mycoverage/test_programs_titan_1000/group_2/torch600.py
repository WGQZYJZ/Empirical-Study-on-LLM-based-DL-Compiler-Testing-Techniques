import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
threshold_value = 0.5
output_data = torch.nn.functional.threshold(input_data, threshold_value, 0)