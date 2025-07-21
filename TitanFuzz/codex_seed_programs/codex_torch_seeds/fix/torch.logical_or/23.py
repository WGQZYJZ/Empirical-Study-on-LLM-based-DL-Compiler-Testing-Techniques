'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_or\ntorch.logical_or(input, other, *, out=None)\n'
import torch
tensor_1 = torch.tensor([[True, False], [True, True]])
tensor_2 = torch.tensor([[False, False], [False, True]])
print(torch.logical_or(tensor_1, tensor_2))