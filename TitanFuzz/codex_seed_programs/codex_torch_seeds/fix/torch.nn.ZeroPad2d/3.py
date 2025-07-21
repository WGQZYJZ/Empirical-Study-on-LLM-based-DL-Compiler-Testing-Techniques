'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
from torch.autograd import Variable
import torch
input_data = torch.randn(1, 1, 3, 3)
print('input_data: ', input_data)
padding = (0, 1, 1, 0)
zero_pad_layer = torch.nn.ZeroPad2d(padding)
output_data = zero_pad_layer(Variable(input_data))
print('output_data: ', output_data)