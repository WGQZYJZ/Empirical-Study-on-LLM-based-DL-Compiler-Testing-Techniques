'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
input1 = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
input2 = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
output = torch.bitwise_and(input1, input2)
print(output)