'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 10, (3, 3))
other = torch.randint(0, 10, (3, 3))
output = torch.bitwise_right_shift(input, other)
print(output)