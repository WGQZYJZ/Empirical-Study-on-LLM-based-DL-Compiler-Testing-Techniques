import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 10, dtype=torch.float32)
threshold = 3
value = (- 1)
output_data = torch.nn.functional.threshold(input_data, threshold, value)