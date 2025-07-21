'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
input_tensor = torch.rand((1, 3, 3))
print(input_tensor)
output_tensor = input_tensor.sum_to_size((1, 5, 5))
print(output_tensor)