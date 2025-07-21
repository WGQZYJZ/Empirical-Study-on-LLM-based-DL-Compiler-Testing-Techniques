'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
print(input_tensor)
output_tensor = torch.Tensor.swapaxes(input_tensor, 0, 2)
print(output_tensor)