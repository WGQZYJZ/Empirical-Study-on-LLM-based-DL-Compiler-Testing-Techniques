'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and_\ntorch.Tensor.logical_and_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False], [False, True]])
other = torch.tensor([[True, True], [False, True]])
output_tensor = torch.Tensor.logical_and_(input_tensor, other)
print(output_tensor)