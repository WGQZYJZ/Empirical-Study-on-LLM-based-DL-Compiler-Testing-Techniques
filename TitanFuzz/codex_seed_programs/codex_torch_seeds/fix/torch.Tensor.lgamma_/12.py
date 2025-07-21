'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma_\ntorch.Tensor.lgamma_(_input_tensor)\n'
import torch
x = torch.randn(4, 4)
print('Input: ', x)
result = torch.Tensor.lgamma_(x)
print('Output: ', result)