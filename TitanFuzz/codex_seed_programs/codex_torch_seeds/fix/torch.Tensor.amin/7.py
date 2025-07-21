'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 4)
output_tensor = input_tensor.amin(dim=1, keepdim=True)
print('Input tensor:', input_tensor)
print('Output tensor:', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amax\ntorch.Tensor.amax(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 4)
output_tensor = input_tensor.amax(dim=1, keepdim=True)