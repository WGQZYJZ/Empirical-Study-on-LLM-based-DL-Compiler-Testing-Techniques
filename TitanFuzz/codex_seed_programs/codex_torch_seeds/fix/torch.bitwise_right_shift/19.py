'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
input = torch.tensor([[0, 1, 2, 3], [4, 5, 6, 7]])
output = torch.bitwise_right_shift(input, 1)
print(output)