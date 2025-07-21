'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
torch.Tensor.tril_(input_tensor, diagonal=0)
print('Input tensor: ', input_tensor)