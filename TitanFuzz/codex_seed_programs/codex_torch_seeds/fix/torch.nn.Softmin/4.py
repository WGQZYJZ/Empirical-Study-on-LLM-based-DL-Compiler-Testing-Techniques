'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.nn.Softmin(dim=1)(input_tensor)
print('Output tensor: ', output_tensor)