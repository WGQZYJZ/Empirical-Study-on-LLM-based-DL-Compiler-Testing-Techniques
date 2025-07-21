'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square_\ntorch.Tensor.square_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
print(torch.Tensor.square_(input_tensor))