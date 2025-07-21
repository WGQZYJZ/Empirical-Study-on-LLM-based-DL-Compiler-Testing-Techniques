'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
value = 2
output_tensor = input_tensor.mul(value)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)