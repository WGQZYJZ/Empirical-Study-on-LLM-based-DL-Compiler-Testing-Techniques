'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma_\ntorch.Tensor.mvlgamma_(_input_tensor, p)\n'
import torch
data = torch.rand(5, 4)
print('Input data is: ', data)
print('Output data is: ', torch.Tensor.mvlgamma_(data, 1))