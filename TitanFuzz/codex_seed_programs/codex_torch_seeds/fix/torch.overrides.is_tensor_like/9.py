'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
input_data = [1, 2, 3, 4, 5]
is_tensor_like = torch.overrides.is_tensor_like(input_data)
print('Is input_data a tensor? ', is_tensor_like)
input_data = torch.tensor(input_data)
is_tensor_like = torch.overrides.is_tensor_like(input_data)
print('Is input_data a tensor? ', is_tensor_like)
input_data = torch.randn(3, 3)
is_tensor_like = torch.overrides.is_tensor_like(input_data)
print('Is input_data a tensor? ', is_tensor_like)