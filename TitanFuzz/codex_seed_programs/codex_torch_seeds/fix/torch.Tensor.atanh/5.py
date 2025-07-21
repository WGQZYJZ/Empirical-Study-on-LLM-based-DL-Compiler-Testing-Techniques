'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atanh\ntorch.Tensor.atanh(_input_tensor)\n'
import torch
data = torch.randn(2, 3)
print('Input: ', data)
print('Output: ', data.atanh())