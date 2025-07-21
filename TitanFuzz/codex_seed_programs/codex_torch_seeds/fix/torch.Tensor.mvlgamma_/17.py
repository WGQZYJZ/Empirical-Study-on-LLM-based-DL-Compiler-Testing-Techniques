'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma_\ntorch.Tensor.mvlgamma_(_input_tensor, p)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input tensor: ', input_tensor)
torch.Tensor.mvlgamma_(input_tensor, 2)
print('Output tensor: ', input_tensor)