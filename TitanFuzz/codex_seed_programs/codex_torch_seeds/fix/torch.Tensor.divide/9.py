'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor)
print(torch.Tensor.divide(input_tensor, 2))
print(torch.Tensor.divide(input_tensor, 2, rounding_mode='floor'))
print(torch.Tensor.divide(input_tensor, 2, rounding_mode='ceil'))
print(torch.Tensor.divide(input_tensor, 2, rounding_mode='half_away_from_zero'))