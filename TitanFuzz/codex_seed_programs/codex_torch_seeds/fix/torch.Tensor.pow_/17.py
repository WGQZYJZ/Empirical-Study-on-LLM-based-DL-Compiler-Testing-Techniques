'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(10)
torch.Tensor.pow_(input_tensor, exponent=3)
print(input_tensor)