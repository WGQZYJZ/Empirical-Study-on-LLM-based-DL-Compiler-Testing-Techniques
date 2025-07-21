'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil\ntorch.Tensor.ceil(_input_tensor)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data: ', input_data)
output = torch.Tensor.ceil(input_data)
print('Output: ', output)