'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.randn(3, 4)
swapped_tensor = input_tensor.swapaxes(0, 1)
print(swapped_tensor)