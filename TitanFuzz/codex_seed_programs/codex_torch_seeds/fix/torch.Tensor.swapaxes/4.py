'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
print(input_tensor)
output_tensor = input_tensor.swapaxes(1, 2)
print(output_tensor)