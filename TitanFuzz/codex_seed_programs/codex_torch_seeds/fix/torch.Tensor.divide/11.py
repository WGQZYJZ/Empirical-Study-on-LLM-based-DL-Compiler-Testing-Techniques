'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.tensor([[4, 4, 4], [4, 4, 4]])
print(input_tensor.divide(2))
print(input_tensor.divide(2, rounding_mode='floor'))
print(input_tensor.divide(2, rounding_mode='ceil'))
print(input_tensor.divide(2, rounding_mode='trunc'))
print(input_tensor.divide(2, rounding_mode='round'))