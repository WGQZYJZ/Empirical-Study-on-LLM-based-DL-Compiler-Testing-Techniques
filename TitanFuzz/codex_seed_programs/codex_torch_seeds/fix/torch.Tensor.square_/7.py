'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square_\ntorch.Tensor.square_(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 5)
print(input_tensor)
torch.Tensor.square_(input_tensor)
print(input_tensor)