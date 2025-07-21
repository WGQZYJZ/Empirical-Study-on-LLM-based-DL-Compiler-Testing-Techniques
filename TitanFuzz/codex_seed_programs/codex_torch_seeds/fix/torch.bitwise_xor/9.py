'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
other = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
print(torch.bitwise_xor(input, other))