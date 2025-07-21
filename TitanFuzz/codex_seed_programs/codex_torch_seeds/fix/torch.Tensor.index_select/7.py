'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.rand(3, 5)
print('Input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.index_select(input_tensor, 0, torch.LongTensor([0, 2]))
print('Output tensor:')
print(output_tensor)