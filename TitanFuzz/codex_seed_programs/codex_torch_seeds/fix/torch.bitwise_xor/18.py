'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
other = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
print(torch.bitwise_xor(input, other))