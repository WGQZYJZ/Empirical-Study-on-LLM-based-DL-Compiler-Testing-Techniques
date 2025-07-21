'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 10, (4, 4), dtype=torch.int32)
print(input)
output = torch.bitwise_left_shift(input, 2)
print(output)