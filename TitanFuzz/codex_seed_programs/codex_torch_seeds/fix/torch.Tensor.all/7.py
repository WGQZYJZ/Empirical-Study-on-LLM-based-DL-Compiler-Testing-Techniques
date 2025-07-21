'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3, 3)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.all(input_tensor, dim=1, keepdim=True)
print('Output tensor: \n', output_tensor)