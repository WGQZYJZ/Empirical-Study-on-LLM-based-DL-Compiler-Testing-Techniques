'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
input1 = torch.randn(2, 3)
input2 = torch.randn(2, 3)
max_value = torch.maximum(input1, input2)
print(max_value)