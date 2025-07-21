'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_or_\ntorch.Tensor.logical_or_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False], [True, False]], dtype=torch.bool)
other = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
output_tensor = input_tensor.logical_or_(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)