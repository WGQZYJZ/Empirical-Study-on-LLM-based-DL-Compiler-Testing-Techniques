'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
input = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.int8)
other = torch.tensor([[1, 0], [1, 0], [1, 1], [0, 0]], dtype=torch.int8)
output = torch.bitwise_and(input, other)
print(output)