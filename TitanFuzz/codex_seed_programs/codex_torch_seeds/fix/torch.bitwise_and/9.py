'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
data = torch.randint(0, 2, (4, 4), dtype=torch.int8)
result = torch.bitwise_and(data, torch.ones((4, 4), dtype=torch.int8))
print(data)
print(result)