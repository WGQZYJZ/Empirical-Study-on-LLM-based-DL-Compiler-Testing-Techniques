"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
torch.nn.init.kaiming_normal_(input_data, mode='fan_in', nonlinearity='leaky_relu')
print('Output data: ', input_data)