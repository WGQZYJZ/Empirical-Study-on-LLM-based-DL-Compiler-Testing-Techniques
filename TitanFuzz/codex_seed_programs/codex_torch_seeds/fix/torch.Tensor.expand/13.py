'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = input_tensor.expand(3, 2, 3)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand_as\ntorch.Tensor.expand_as(_input_tensor, _other_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])