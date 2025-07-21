'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu\ntorch.Tensor.triu(_input_tensor, diagonal=0)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(_input_tensor.triu(diagonal=0))