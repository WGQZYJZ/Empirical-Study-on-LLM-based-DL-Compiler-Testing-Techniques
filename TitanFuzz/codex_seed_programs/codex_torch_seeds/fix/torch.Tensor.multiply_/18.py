'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply_\ntorch.Tensor.multiply_(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(3, 4)
torch.Tensor.multiply_(input_tensor, 2)
print(input_tensor)