'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(3, 3)
input_tensor.mul_(2)
print(input_tensor)