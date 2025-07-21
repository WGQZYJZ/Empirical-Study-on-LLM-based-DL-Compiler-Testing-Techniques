'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.true_divide\ntorch.Tensor.true_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(4, 4)
value = 2
divided_tensor = torch.Tensor.true_divide(input_tensor, value)
print('input_tensor:', input_tensor)
print('divided_tensor:', divided_tensor)