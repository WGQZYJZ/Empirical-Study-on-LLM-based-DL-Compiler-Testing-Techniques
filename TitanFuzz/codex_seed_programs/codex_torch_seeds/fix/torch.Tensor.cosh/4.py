'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cosh\ntorch.Tensor.cosh(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(torch.Tensor.cosh(input_tensor))