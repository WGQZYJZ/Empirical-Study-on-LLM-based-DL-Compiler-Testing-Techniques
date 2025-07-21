'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma_\ntorch.Tensor.polygamma_(_input_tensor, n)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
print('Polygamma: ', torch.Tensor.polygamma_(input_tensor, 2))