'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_data = torch.randn(3, 4, 5)
print(input_data)
output_data = input_data.swapaxes(1, 2)
print(output_data)