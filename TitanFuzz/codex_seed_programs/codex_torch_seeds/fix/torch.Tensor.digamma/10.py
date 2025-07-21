'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
input_data = torch.rand(10)
print('Input data: ', input_data)
print('Digamma of input data: ', input_data.digamma())