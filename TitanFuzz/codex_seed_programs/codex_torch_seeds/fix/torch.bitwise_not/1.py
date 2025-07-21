'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input = torch.randint(0, 2, (2, 2), dtype=torch.uint8)
print(input)
output = torch.bitwise_not(input)
print(output)