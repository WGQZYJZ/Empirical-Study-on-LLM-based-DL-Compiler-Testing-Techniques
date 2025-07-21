'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not_\ntorch.Tensor.logical_not_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[True, False], [True, True]])
print(input_tensor)
print(torch.Tensor.logical_not_(input_tensor))