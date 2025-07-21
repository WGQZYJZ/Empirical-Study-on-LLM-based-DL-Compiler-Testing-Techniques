'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.normal_\ntorch.Tensor.normal_(_input_tensor, mean=0, std=1, *, generator=None)\n'
import torch
input_data = torch.rand(2, 3, 5)
print('Input data: \n', input_data)
output_data = torch.Tensor.normal_(input_data, mean=0, std=1)
print('Output data: \n', output_data)