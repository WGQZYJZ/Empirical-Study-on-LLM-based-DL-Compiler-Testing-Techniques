'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rsqrt_\ntorch.Tensor.rsqrt_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:\n', input_tensor)
torch.Tensor.rsqrt_(input_tensor)
print('Output tensor:\n', input_tensor)