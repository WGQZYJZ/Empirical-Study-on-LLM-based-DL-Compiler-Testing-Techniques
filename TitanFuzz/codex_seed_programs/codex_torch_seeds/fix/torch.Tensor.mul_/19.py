'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(3, 3)
value = 2
torch.Tensor.mul_(input_tensor, value)
print(input_tensor)