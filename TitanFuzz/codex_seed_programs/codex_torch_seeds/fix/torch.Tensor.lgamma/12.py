'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma\ntorch.Tensor.lgamma(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
lgamma_tensor = input_tensor.lgamma()
print('lgamma_tensor: ', lgamma_tensor)