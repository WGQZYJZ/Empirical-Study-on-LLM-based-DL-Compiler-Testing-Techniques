'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
data = torch.arange(start=0, end=9, dtype=torch.float32).reshape(3, 3)
print('Input data: ', data)
result = torch.Tensor.vsplit(data, 3)
print('Result: ', result)