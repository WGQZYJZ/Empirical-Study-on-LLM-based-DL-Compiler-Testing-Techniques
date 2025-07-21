'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d()\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 2, 3)
print('Input data: ', input_data)
softmax = nn.Softmax2d()
output_data = softmax(input_data)
print('Output data: ', output_data)