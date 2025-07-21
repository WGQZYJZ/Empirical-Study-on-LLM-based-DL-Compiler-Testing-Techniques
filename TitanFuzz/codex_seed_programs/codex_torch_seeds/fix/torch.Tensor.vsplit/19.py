'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randint(1, 10, (3, 4))
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.vsplit(2)
print('Output tensor: ', output_tensor)