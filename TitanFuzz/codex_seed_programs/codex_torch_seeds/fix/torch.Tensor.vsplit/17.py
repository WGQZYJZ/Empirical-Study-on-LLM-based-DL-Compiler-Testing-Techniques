'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
import torch
input_tensor = torch.arange(start=0, end=24, out=torch.FloatTensor())
input_tensor = input_tensor.view(3, 4, 2)
output_tensor = torch.Tensor.vsplit(input_tensor, split_size_or_sections=2)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)