'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.le\ntorch.Tensor.le(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output_tensor = input_tensor.le(other)
print('Output tensor:', output_tensor)