'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
output = torch.bitwise_right_shift(input, other)
print(output)