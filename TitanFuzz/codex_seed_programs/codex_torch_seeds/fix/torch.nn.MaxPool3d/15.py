'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.randn(20, 16, 50, 32, 45)
print('Input data: ', input_data.size())
max_pooling_layer = torch.nn.MaxPool3d(kernel_size=(2, 2, 2), stride=2)
output = max_pooling_layer(input_data)
print('Output data: ', output.size())