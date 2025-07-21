'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[1.3, 2.5, 5.6, 10.1], [1.2, 2.4, 5.8, 10.2], [1.1, 2.3, 5.9, 10.3]])
output_tensor = torch.Tensor.floor_divide(input_tensor, 2)
print('Input tensor:\n', input_tensor)
print('Output tensor:\n', output_tensor)