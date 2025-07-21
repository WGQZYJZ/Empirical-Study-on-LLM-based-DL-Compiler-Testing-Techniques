'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
input_tensor = torch.randn(5, 5)
print(input_tensor)
output_tensor = torch.Tensor.sum_to_size(input_tensor, 2, 3)
print(output_tensor)
'\nTask 4: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
output_tensor = torch.Tensor.sum_to_size(input_tensor, 2, 3, 2)
print(output_tensor)