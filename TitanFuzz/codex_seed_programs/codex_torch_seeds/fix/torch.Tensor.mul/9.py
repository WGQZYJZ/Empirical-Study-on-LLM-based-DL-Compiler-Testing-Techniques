'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.mul(input_tensor, 10)
print(input_tensor)
print(output_tensor)