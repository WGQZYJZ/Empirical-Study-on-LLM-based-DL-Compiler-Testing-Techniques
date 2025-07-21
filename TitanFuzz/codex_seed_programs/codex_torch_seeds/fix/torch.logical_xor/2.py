'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
input = torch.tensor([[True, True], [True, False], [False, True], [False, False]], dtype=torch.bool)
other = torch.tensor([[True, False], [True, False], [False, True], [False, False]], dtype=torch.bool)
output = torch.logical_xor(input, other)
print(output)