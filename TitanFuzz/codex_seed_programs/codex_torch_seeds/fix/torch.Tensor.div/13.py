'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = input_tensor.div(3)
print('Input tensor:\n', input_tensor)
print('Output tensor:\n', output_tensor)