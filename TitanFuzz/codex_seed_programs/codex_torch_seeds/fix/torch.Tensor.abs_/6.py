'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.abs_\ntorch.Tensor.abs_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
torch.Tensor.abs_(input_tensor)
print(input_tensor)
input_tensor = torch.randn(3, 3)
print(torch.abs(input_tensor))
input_tensor = torch.randn(3, 3)
print(input_tensor.abs())
input_tensor = torch.randn(3, 3)
print(torch.abs(input_tensor))