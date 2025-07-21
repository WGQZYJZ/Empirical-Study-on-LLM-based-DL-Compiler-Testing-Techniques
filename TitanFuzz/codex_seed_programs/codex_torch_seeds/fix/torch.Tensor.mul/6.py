'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(1, 3)
value = torch.randn(1, 3)
output_tensor = torch.Tensor.mul(input_tensor, value)
print(output_tensor)