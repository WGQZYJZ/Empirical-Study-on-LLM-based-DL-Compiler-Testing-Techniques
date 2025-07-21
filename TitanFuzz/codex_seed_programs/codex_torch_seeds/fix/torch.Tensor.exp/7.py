'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exp\ntorch.Tensor.exp(_input_tensor)\n'
import torch
input_data = torch.randn(1, 3)
output_data = torch.Tensor.exp(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)