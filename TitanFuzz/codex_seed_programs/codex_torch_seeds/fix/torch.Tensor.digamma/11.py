'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
input_data = torch.randn(1, 3, 3)
output = input_data.digamma()
print('input_data: ', input_data)
print('output: ', output)