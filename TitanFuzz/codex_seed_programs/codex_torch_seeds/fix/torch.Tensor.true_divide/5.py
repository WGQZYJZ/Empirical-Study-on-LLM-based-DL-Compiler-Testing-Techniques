'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.true_divide\ntorch.Tensor.true_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(4, 6)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.true_divide(2)
print('output_tensor:', output_tensor)