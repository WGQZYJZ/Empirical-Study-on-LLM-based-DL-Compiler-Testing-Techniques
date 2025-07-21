'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, True], [True, False]])
other_tensor = torch.tensor([[True, True], [True, False]])
result = input_tensor.logical_and(other_tensor)
print(result)